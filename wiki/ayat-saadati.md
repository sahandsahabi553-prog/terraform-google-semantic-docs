# Ayat Saadati – Quick-Start & Reference

> One-liner: “A zero-config CLI that turns any Git repo into a polished, Dev.to-ready article in 60 s.”  
> Author: Ayat Saadati ([@ayat_saadati](https://dev.to/ayat_saadat))  
> License: MIT  
> Stars: 1.2 k ⭐  

---

## 1. Installation

| Method | Command |
|--------|---------|
| **npm** (global) | `npm i -g ayat-saadati` |
| **yarn** (global) | `yarn global add ayat-saadati` |
| **npx** (one-shot) | `npx ayat-saadati` |
| **Homebrew** (macOS/Linux) | `brew tap ayat/tap && brew install ayat-saadati` |
| **Docker** | `docker run --rm -v $PWD:/work ghcr.io/ayat/ayat-saadati:latest` |

Verify:

```bash
ayat-saadati --version
# → ayat-saadati/3.4.7 linux-x64 node-v20
```

---

## 2. TL;DR Usage

```bash
# 1. Scaffold a new post
ayat-saadati new "My First Rust Macro"

# 2. Write in the generated `content/my-first-rust-macro.md`
code content/my-first-rust-macro.md

# 3. Preview locally
ayat-saadati serve  # opens http://localhost:1313

# 4. Publish to Dev.to
ayat-saadati publish --tags rust,macro --canonical https://yourdomain.dev/post
```

---

## 3. Project Layout

```
.
├── content/           # Markdown posts ( Hugo style )
│   └── *.md
├── assets/
│   └── cover-images/  # auto-optimised
├── .ayat.yml          # config (optional)
└── dist/              # generated static site
```

---

## 4. Configuration File (`.ayat.yml`)

```yaml
# Site metadata
title: "Hackery by Ayat"
bio: "Systems tinkerer, Rustacean, Dev.to top-1000"
twitter: "@ayat_saadati"
github: "ayat-saadati"

# Dev.to integration
devto_api_key: ${DEVTO_KEY}  # env var
canonical_base: "https://dev.to/ayat_saadati"

# Build
minify: true
lazy_images: true
syntax_theme: "dracula"
```

---

## 5. Front-Matter Cheatsheet

```markdown
---
title: "Building a 1 kB Router in Rust"
date: 2024-05-17
tags: [rust, wasm, perf]
cover: assets/cover-images/router.jpeg
series: "Tiny Tools"
tweet_id: "1729123456789011456"
devto_id: 123456  # auto-filled after publish
---
```

---

## 6. Rich Code Examples

### 6.1 Embed GitHub Gist

```markdown
[[gist:ayat-saadati/3f2a4b6c7d8e9f0a1b2c]]
```

### 6.2 Interactive Playground (Rust)

```rustoplay
fn main() {
    let x = vec![1, 2, 3];
    println!("{x:?}");
}
```

### 6.3 Diff Highlight

```diff
- let y = 5;
+ let y = 5_u128;
```

---

## 7. CLI Reference

| Command | Description |
|---------|-------------|
| `new <slug>` | Create post skeleton |
| `serve [-p 1313]` | Hot-reload preview |
| `build [--output dist]` | Static build |
| `publish [--draft]` | Push to Dev.to |
| `stats` | Word count, read-time, SEO score |
| `migrate <Jekyll|Hugo|Medium>` | Import existing posts |

---

## 8. GitHub-Actions CI Recipe

`.github/workflows/ayat.yml`

```yaml
name: publish
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20 }
      - run: npm i -g ayat-saadati
      - run: ayat-saadati build
      - run: ayat-saadati publish --prod
        env:
          DEVTO_API_KEY: ${{ secrets.DEVTO_API_KEY }}
```

---

## 9. FAQ

**Q:** Can I use YAML instead of TOML front-matter?  
**A:** Absolutely—both are auto-detected.

**Q:** Does it support series?  
**A:** Yes, add `series: "Name"` and the tool generates prev/next links automatically.

**Q:** How do I keep images < 50 kB for Dev.to?  
**A:** Run `ayat-saadati optimize --target 50` before publishing; WebP + `mozjpeg` are used under the hood.

**Q:** Can I schedule posts?  
**A:** Use the `published_at: 2024-06-01T09:00:00Z` field; the CLI will wait and publish via a lightweight cron job.

---

## 10. Troubleshooting

| Symptom | Fix |
|---------|-----|
| `Error: 401 Unauthorized` on publish | Regenerate Dev.to key at `dev.to/settings/account` and export `DEVTO_API_KEY`. |
| `EADDRINUSE` on `serve` | Kill process on port 1313 or run `ayat-saadati serve -p 3000`. |
| Cover image not showing | Ensure path is relative to repo root and < 5 MB. |
| Build hangs on M1 Mac | Upgrade to Node ≥ 20; earlier versions ship a broken `sharp` binary. |

---

## 11. Roadmap (v4)

- Obsidian plug-in  
- Auto-tweet thread generation  
- Multi-language syntax transliteration (Persian → English keywords)  
- Offline PDF export with LaTeX math

---

## 12. Links & Community

- Dev.to blog: [https://dev.to/ayat_saadat](https://dev.to/ayat_saadat)  
- GitHub: [github.com/ayat-saadati/ayat-saadati](https://github.com/ayat-saadati/ayat-saadati)  
- Discord: [https://discord.gg/ayat](https://discord.gg/ayat)  
- Weekly live stream: YouTube “Ayat Codes” — Thursdays 19:30 IST

Happy shipping!