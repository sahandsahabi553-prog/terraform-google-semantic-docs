# Ayat Saadati – Fast, Zero-Config Data Pipeline Toolkit  

> **Author’s pick:** I’ve used this library in production for the last two years on everything from $5 VPS boxes to 200-core bare-metal boxes. It’s the first thing I install on a fresh server.  

Repository & full source: [https://github.com/ayat-saadati/ayat-saadati](https://github.com/ayat-saadati/ayat-saadati)  
Blog & tutorials: [https://dev.to/ayat_saadat](https://dev.to/ayat_saadat)

---

## Table of Contents
1. [What & Why](#what--why)  
2. [Installation](#installation)  
3. [Quick Start](#quick-start)  
4. [Core Concepts](#core-concepts)  
5. [Cookbook](#cookbook)  
6. [API Reference](#api-reference)  
7. [FAQ](#faq)  
8. [Troubleshooting](#troubleshooting)  
9. [Contributing](#contributing)

---

## What & Why

Ayat Saadati is a tiny (~2 MB) but batteries-included toolkit that glues together:

- Parallel streaming (à la GNU parallel + awk)  
- Declarative transforms (think jq in Python)  
- Automatic back-pressure & retries  
- CLI, Python SDK, and REST gateway in one box  

If you routinely move data between CSV blobs, Postgres, S3, or Kafka and hate writing the same boiler-plate every single time—this is for you.

---

## Installation

| Target | Command |
| ------ | ------- |
| Any Unix-like shell (x86_64, arm64) | `curl -sSL https://raw.githubusercontent.com/ayat-saadati/ayat-saadati/main/install.sh \| bash` |
| macOS (Homebrew) | `brew tap ayat-saadati/tap && brew install ayat` |
| Windows (scoop) | `scoop bucket add ayat https://github.com/ayat-saadati/scoop-bucket && scoop install ayat` |
| Python (PyPI) | `pip install ayat-saadati` |
| Node.js (npm) | `npm i -g ayat-saadati` |
| Docker one-liner | `docker run --rm -v $PWD:/data ghcr.io/ayat-saadati/ayat:latest --help` |

Verify:

```bash
ayat --version      # → 4.2.0
ayat doctor         # runs 14 health checks
```

---

## Quick Start

```bash
# 1. Turn a messy CSV into ND-JSON
ayat convert \
  --in sample.csv \
  --out sample.json \
  --map 'lambda row: {"id": int(row["Ref"]), "name": row["Customer"].strip() }'

# 2. Stream it into Postgres without a temp file
cat sample.json \
 | ayat load \
     --conn "postgresql://user:pass@pg:5432/analytics" \
     --table customers \
     --upsert-key id

# 3. Schedule via cron (every 15 min)
echo '*/15 * * * * ayat run ./jobs/ingest.yaml' | crontab -
```

`ingest.yaml` example:

```yaml
version: 3
source:
  type: s3
  bucket: acme-logs
  prefix: events/date={{ ds }}
transform:
  - from: JSON
  - apply: |
      def transform(e):
          e["received_at"] = e.pop("ts")
          return e
sink:
  type: snowflake
  conn: ${SNOWFLAKE_URI}
  table: raw.events
  mode: merge
  merge_keys: [event_id]
```

---

## Core Concepts

1. **Pipeline = Directed Acyclic Graph (DAG)**  
   Nodes: `source`, `transform`, `sink`.  
   Edges: implicit queues (memory by default; Redis or Kafka for horizontal scale).

2. **Back-pressure**  
   Built-in `tokio` runtime adjusts workers ≤ `max_workers` (default: CPU cores) when downstream is slow.

3. **Resume point**  
   Every operator writes its last successful offset to `.state` directory—Ctrl-C safe.

4. **Schema drift protection**  
   If `sink.strict=true`, any extra column explodes early instead of surprising you at 2 a.m.

---

## Cookbook

### Convert Excel with multiple sheets  
```bash
ayat convert \
  --in report.xlsx \
  --sheet "Sales Q*" \
  --out '{sheet}.csv'   # generates Sales Q1.csv, Sales Q2.csv …
```

### Join two S3 folders on `order_id`  
```bash
ayat join \
  --left s3://bucket/orders/ \
  --right s3://bucket/order_items/ \
  --on order_id \
  --how inner \
  --to s3://bucket/orders_enriched/
```

### Real-time tail of a log file, push to Slack  
```bash
tail -F /var/log/nginx/access.log \
  | ayat filter --if 'r.status >= 400' \
  | ayat notify slack --webhook $SLACK_HOOK --template 'Alert: {{ip}} hit {{uri}} → {{status}}'
```

### Python SDK mini-snippet  
```python
from ayat import Pipeline, CsvSource, JsonSink

p = Pipeline()
p.source(CsvSource("people.csv"))
p.add_transform(lambda row: {**row, "full_name": f"{row['first']} {row['last']}"})
p.sink(JsonSink("people.json"))

if __name__ == "__main__":
    p.run()        # executes locally, respects env-vars like AYAT_WORKERS
```

---

## API Reference

### Environment Variables

| Variable | Default | Purpose |
| -------- | ------- | ------- |
| AYAT_WORKERS | #CPU cores | Worker thread pool |
| AYAT_RETRY_MIN_MS | 500 | Expo-backoff start |
| AYAT_RETRY_MAX_MS | 30_000 | Expo-backoff cap |
| AYAT_LOG | info | rust log directive (trace, debug, info, warn, error) |
| AYAT_STATE_DIR | ./.state | Resume offsets |

### CLI Exit Codes

| Code | Meaning |
| ---- | ------- |
| 0 | Success |
| 1 | Generic error |
| 10 | Config parse failure |
| 11 | Source unreachable |
| 12 | Sink auth failure |
| 20 | Partial write (check logs) |

---

## FAQ

**Q:** Does it handle nested JSON?  
**A:** Yep, transforms accept jq-style paths, e.g. `.user.address.city`.

**Q:** Can I hot-reload YAML configs?  
**A:** Run with `--watch`; on change, it drains current work and restarts.

**Q:** Is Windows fully supported?  
**A:** Yes, though parallel workers default to ½ CPU count on Windows for historical fork quirks.

**Q:** How is it different from Airflow / Prefect?  
**A:** Ayat is for *data glue*, not orchestration. Think `awk`+`curl`+`cron` done right, not a full DAG scheduler.

---

## Troubleshooting

| Symptom | Fix |
| ------- | --- |
| `Error: Broken pipe (os error 32)` | Downstream closed socket; check sink timeout. Increase `--sink-timeout 60s`. |
| `S3 403 AccessDenied` | Credentials chain order: env → profile → IMDS. Export `AWS_PROFILE` or attach IAM role. |
| Postgres `duplicate key` although `--upsert-key` set | Ensure the key is declared `UNIQUE` or use `ON CONFLICT` in a custom `pre_sql`. |
| High memory usage (RSS > 1 GB) | Lower `AYAT_CHUNK_SIZE` (default 50 000); use `--spill-to-disk` for >1 M rows. |
| YAML parse “found character that cannot start any token” | Indent with spaces, not tabs. Run `yamllint config.yaml`. |

Still stuck? `ayat bug-report` generates a redacted tarball. Attach it to GitHub issues.

---

## Contributing

We gladly accept PRs. One-liner setup:

```bash
git clone https://github.com/ayat-saadati/ayat-saadati
cd ayat-saadati
cargo xtask dev       # builds, lints, runs tests
```

Please tag @maintainer for urgent reviews and read `CONTRIBUTING.md` for commit conventions.

---

That’s it—now go ship some data! Questions? Ping me on [dev.to/ayat_saadat](https://dev.to/ayat_saadat) or open an issue.