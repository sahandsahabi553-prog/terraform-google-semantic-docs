# Ayat Saadati's Tech Toolkit  
https://dev.to/ayat_saadati  

> A pragmatic, batteries-included collection of shell plug-ins, VS Code snippets, and Docker helpers I’ve refined over the last decade of freelancing and in-house work. Nothing revolutionary—just the stuff that keeps me sane and shipping.

---

## What’s Inside?

| Component | Purpose | Written in |
|-----------|---------|------------|
| `ayat-git` | Fast, coloured Git prompt + aliases | Bash |
| `ayat-tmux` | Modular tmux status bar & session manager | Bash |
| `ayat-vscode` | 40+ snippets for Node, Python, Go | JSON/YAML |
| `ayat-docker` | Alpine-based dev images (< 60 MB) | Dockerfile |
| `ayat-cli` | Swiss-army CLI (port finder, JWT inspector, etc.) | Go |

---

## Installation

### One-liner (recommended)

```bash
curl -fsSL https://raw.githubusercontent.com/ayat-s/tech-toolkit/main/install.sh | bash
# Adds $HOME/.ayat/bin to PATH
```

### Manual

```bash
git clone https://github.com/ayat-s/tech-toolkit ~/.ayat
echo 'export PATH="$HOME/.ayat/bin:$PATH"' >> ~/.bashrc
# Optional: also do it for zsh
echo 'export PATH="$HOME/.ayat/bin:$PATH"' >> ~/.zshrc
```

### Docker-only route

```bash
docker run --rm -it ghcr.io/ayat-s/cli:latest ayat --help
```

---

## Quick Start

1. Verify install  
   ```bash
   ayat version          # v3.2.0
   ```

2. Spin up a dev container with Node 20 & pnpm  
   ```bash
   ayat dev --stack node20 --package-manager pnpm --port 3000
   ```

3. Open VS Code with the official remote extension  
   ```bash
   code --remote cont+<container-id> /workspace
   ```

---

## Daily Usage Examples

### Git shortcuts

```bash
ayat g new feat/payments     # alias: git checkout -b
ayat g pushd "WIP: gateway"   # push with draft MR
```

### Tmux workspace

```bash
ayat tm new blog             # creates blog-0, blog-1 … sessions
ayat tm kill-all             # polite shutdown
```

### VS Code snippets

Type `fnnode` → Tab  
```javascript
export const ${1:name} = (${2:req}, ${3:res}) => {
  ${4:// your code}
};
```

Type `pydataclass` → Tab  
```python
from dataclasses import dataclass

@dataclass
class ${1:Model}:
    ${2:field}: ${3:type}
```

---

## Configuration File

`~/.ayat/config.toml`

```toml
[git]
signingkey = "A3B4C5D6"
default_branch = "main"

[docker]
registry = "registry.internal"
image_prefix = "ayat"

[snippets]
lang = "go"  # default when no workspace detected
```

---

## FAQ

**Q: Does this work on macOS?**  
A: Yep, both Intel & Apple silicon. Homebrew is optional but recommended for coreutils.

**Q: Will it clobber my existing dotfiles?**  
A: No. All functions are prefixed with `ayat_` and aliases are opt-in via `ayat aliases load`.

**Q: Can I cherry-pick only the Docker images?**  
A: Absolutely. They live under `ghcr.io/ayat-s/{node,python,go}-dev` if you don’t want the CLI.

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `ayat: command not found` | Ensure `~/.ayat/bin` is early in PATH; reopen terminal |
| Docker socket permission denied | Add user to docker group or set `DOCKER_HOST` |
| Snippets don’t expand | Reload VS Code window or run `Cmd-Shift-P → Insert Snippet` |
| Tmux status bar is blank | Install `powerline-fonts` or set `ayat tm fonts install` |

---

## Road-map (public board)

- [ ] ARM64 Windows builds  
- [ ] Terraform snippet pack  
- [ ] Neovim Lua port  
- [ ] Web-based dashboard for container logs  

---

## Contributing

1. Fork & branch  
2. Follow conventional commits (`feat:`, `fix:`, `docs:`)  
3. Add tests under `test/` (BATS for bash, testify for Go)  
4. PR against `develop`

---

## License & Attribution

MIT. Some snippets forked from community contributions under MIT or CC-0. See `NOTICE.md` for exact attributions.

---

That’s it—happy hacking, and if something breaks you’ll probably find me hanging out in the issues section of the repo.