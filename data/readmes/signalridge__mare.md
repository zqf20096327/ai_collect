<div align="center">

<p>
  <img src="docs/assets/brand/mare-wordmark-dark.svg#gh-dark-mode-only" width="384" height="96" alt="mare">
  <img src="docs/assets/brand/mare-wordmark-light.svg#gh-light-mode-only" width="384" height="96" alt="mare">
</p>

<p><strong>A hyperextensible agent harness.</strong></p>

<p>
  <a href="docs/README.md">Docs</a> ·
  <a href="docs/en/get-started/quickstart.md">Quickstart</a> ·
  <a href="https://signalridge.github.io/mare/en/">Website</a> ·
  <strong>English</strong> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="README.ja.md">日本語</a>
</p>

<p>
  <img src="docs/assets/screenshots/main-dark.svg" width="780" alt="mare terminal interface reading a file, editing it, and showing the diff">
</p>

<p><sub>Recorded from the real TUI against an offline scripted model.</sub></p>

</div>

At its core, mare is a small Rust kernel that confines processes, keeps sessions durable, renders the terminal UI (`mare-tui`), and runs plugins. The agent loop, tools, model providers, compaction, permission policy, status line, and UI components and themes are Lua 5.5 plugins built on [cordis-lua](https://github.com/signalridge/cordis-lua).

## Highlights

- **Built-in and user plugins**: built-ins use the same public Cordis service and event API as user plugins. Run `mare runtime` to inspect shipped sources; to replace a plugin, provide a same-name definition in a higher-precedence source with `override = true`, then run `/reload`.
- **Rust safety boundary**: OS sandboxing (bubblewrap or Landlock on Linux, Seatbelt on macOS, restricted tokens and an optional enhanced tier on Windows), project trust, crash-safe JSONL sessions, pre-edit file snapshots (`/rewind`), and a Lua watchdog stay in Rust.
- **Configured in Lua**: `~/.config/mare/init.lua` plus trusted `.mare/init.lua`, typed for LuaLS via `mare init`, with git package management (`mare.plugins.add` and `mare-lock.json`) and `mare --clean`.
- **Every front end, one session model**: main-screen TUI with native scrollback, headless `-p` / `--json` for scripts and CI, bidirectional mare RPC protocol 3.0 (`--rpc`), authenticated `--web` HTTP/WebSocket RPC, and ACP (`mare acp`) for editors.

## Quick start

**1. Install.** Run the one-line installer, install via a package manager (`brew`, `scoop`, `nix`, `yay`, Docker/GHCR), download a release package or archive (`.deb`, `.rpm`, `.tar.gz`, `.zip`) from [GitHub Releases](https://github.com/signalridge/mare/releases) (see the [installation guide](docs/en/get-started/installation.md)), or build from source with Rust 1.100.0+ and a C compiler:

```sh
# macOS / Linux one-line installer (SHA-256 verified)
curl -fsSL https://signalridge.github.io/mare/install.sh | sh

# Homebrew (macOS / Linux)
brew tap signalridge/tap && brew trust signalridge/tap
brew install --cask mare

# Nix (Flake / NUR)
nix run github:signalridge/mare
nix profile install github:signalridge/nur-packages#mare

# Arch Linux (AUR) & Container (GHCR)
yay -S mare-bin
docker run --rm -it -v "$PWD:/workspace" -w /workspace ghcr.io/signalridge/mare:latest
```

```powershell
# Windows one-line installer (PowerShell, SHA-256 verified)
irm https://signalridge.github.io/mare/install.ps1 | iex

# Scoop (Windows)
scoop bucket add signalridge https://github.com/signalridge/scoop-bucket
scoop install signalridge/mare
```

```sh
# From source with Cargo (or clone and build)
cargo install --git https://github.com/signalridge/mare --locked --bin mare mare-cli
```

**2. Run.** Launch `mare` directly inside a project. When no provider has credentials yet, the TUI walks you through first-run onboarding (provider login, default model, and optional plugins):

```sh
cd ~/src/my-project
mare
```

You can also initialize config and credentials explicitly with `mare init`, `mare login openai` (or pipe an API key with `--with-api-key`), and `mare doctor`.

**3. Configure (`~/.config/mare/init.lua`).** Extend mare with packages from [mare-plugins](https://github.com/signalridge/mare-plugins) or your own Lua plugins built on [cordis-lua](https://github.com/signalridge/cordis-lua):

```lua
mare.setup { model = "openai/gpt-6.1-terra" }
mare.plugin("tools", { bash_timeout_ms = 120000 })

mare.plugins.add {
  { "signalridge/mare-plugins", version = "^1" },
}
```

## Documentation

| Topic | Link |
|---|---|
| Full documentation | [docs/README.md](docs/README.md) · [signalridge.github.io/mare](https://signalridge.github.io/mare/en/) |
| Get started & workflows | [Quickstart](docs/en/get-started/quickstart.md) · [Installation](docs/en/get-started/installation.md) · [Workflows](docs/en/get-started/workflows.md) |
| Configuration & plugins | [init.lua](docs/en/configure/files.md) · [Packages](docs/en/configure/packages.md) · [Writing a plugin](docs/en/extend/writing-a-plugin.md) |
| Safety & interfaces | [Permissions](docs/en/use/permissions.md) · [RPC](docs/en/integrate/rpc.md) · [ACP](docs/en/integrate/acp.md) · [Headless](docs/en/use/headless.md) |
| Architecture & reference | [Subsystems](docs/subsystems/README.md) · [CLI](docs/en/reference/cli.md) · [Lua API](docs/en/extend/lua-api.md) · [RPC reference](docs/en/reference/rpc.md) |
| Project & governance | [NEWS.md](crates/mare-plugin/preset/NEWS.md) · [SECURITY.md](SECURITY.md) · [CONTRIBUTING.md](CONTRIBUTING.md) |

## Acknowledgements

mare stands on the ideas and engineering of these projects:

- [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) & [Cordis](https://github.com/cordiverse/cordis): plugin-first services, events, and a replaceable agent loop.
- [Codex](https://github.com/openai/codex): process execution, OS sandboxing, `apply_patch`, and Rust groundwork.
- [Kimi Code](https://github.com/MoonshotAI/kimi-code): context-recovery footer and secret/log redaction patterns.
- [pi](https://github.com/earendil-works/pi-mono): compaction summary prompts, retry error classification, and project trust flow.
- [Neovim](https://neovim.io/): `init.lua` configuration, typed Lua APIs, and RPC.
- [Yazi](https://yazi-rs.github.io/) & [WezTerm](https://wezterm.org/): Lua plugin/package layout for Rust apps and live-reloaded config as code.

The name comes from the lunar maria: the core is the moon, and plugins are the seas across its surface.

## License

Licensed under the [Apache License, Version 2.0](LICENSE). Third-party attributions and notices are listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
