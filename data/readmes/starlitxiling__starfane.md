<p align="center">
  <img src="assets/logo.svg" width="96" height="96" alt="starfane logo" />
</p>

<h1 align="center">starfane</h1>

<p align="center">
  <strong>Lightweight, single-binary Rust control plane for coordinating Claude Code, Codex CLI, Antigravity (<code>agy</code>), and optional shell panes across <code>tmux</code>, <code>zellij</code> (0.44+), and federated remote hosts.</strong>
</p>

<p align="center">
  English · <a href="README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <a href="https://github.com/starlitxiling/starfane/releases"><img src="https://img.shields.io/github/v/release/starlitxiling/starfane?logo=github&label=release" alt="GitHub Release" /></a>
  <img src="https://img.shields.io/badge/rust-1.82%2B-orange?logo=rust" alt="Rust 1.82+" />
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT License" />
  <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey" alt="Platform macOS | Linux" />
  <img src="https://img.shields.io/badge/architecture-BYO--tmux%20%C2%B7%20Zellij%20%C2%B7%20Zero%20Headless-1E1D1B" alt="BYO-tmux · Zellij · Zero Headless" />
  <img src="https://img.shields.io/badge/privacy-Zero%20Telemetry%20%C2%B7%20Local--First-237A4B" alt="Privacy: Zero Telemetry · Local-First" />
</p>

---

## Live Web Console

<p align="center">
  <img src="assets/preview.png" width="100%" alt="starfane embedded Web console showing Claude Code, Codex CLI, AGY, and shell sessions inside tmux" />
</p>

---

## Why `starfane`?

Most coding-agent orchestrators wrap providers in one-shot headless `exec` / `-p` subprocesses or lock you into a heavy desktop Electron shell. `starfane` takes the opposite approach:

- **Zero Headless, BYO-`tmux` & `zellij` (0.44+)**: Keep your real, long-lived interactive `claude`, `codex`, and `agy` panes running in `tmux` or `zellij >= 0.44` via a unified `TerminalMux` abstraction—plus opt-in plain `shell` panes (monitors, scripts, dev terminals) via `[discovery] include_shell_panes = true`. `starfane` attaches unobtrusively via official hooks and stdio MCP, and spawns new interactive panes cleanly inside `~/.agent_session` (or any path you specify).
- **Sub-10ms Hook Hot Path**: `starfane emit` is pure `std` Rust with zero async runtime startup overhead, posting events over a local Unix socket (`starfaned.sock`) and falling back to an on-disk spool if the daemon is restarting.
- **Full History, Bilingual UI & Glyph-Safe Embedded Web Console**: Zero-build native ES Modules (`web/app.js` + `web/js/*.js`) with ETag `304` static serving, deployment-time UI language selection (`[web] lang = "zh" | "en"` or `starfane daemon --lang zh|en`, defaulting to `"zh"` with no in-UI switch clutter), cursor-paginated full conversation transcript (load earlier pages / load all), full terminal scrollback capture (`tmux capture-pane -S -` / `zellij dump-screen --full`) rendered in 200-line `content-visibility: auto` chunks, Prompt TOC, image paste dispatch, slash-command autocomplete, and automatic offscreen `<canvas>` Nerd Font probing + PUA compatibility glyph mapping (plus custom `[web] terminal_font` or `~/.config/starfane/fonts/terminal.woff2` / `.ttf` loading) to eliminate missing-glyph tofu boxes.
- **Multi-Host Federation (`[[nodes]]`)**: Mix zero-install **SSH ControlMaster** hosts (`kind = "ssh"`) for remote servers/GPU containers with full **Peer `starfaned`** federation (`kind = "peer"`, multi-candidate outbound `endpoints` failover & transcript proxying) in one host-grouped sidebar with runtime host renaming (`POST /api/hosts/{id}/rename`).
- **Opt-In Pluggable Notification Routing & Split Ownership**: Silent by default on fresh installs, 100% compatible with two-way `[feishu]` Card 2.0 via `lark-cli`, and extensible via `[[notifiers]]` (`feishu` multi-profile, `telegram` with forum topics, `discord` rich embeds, `slack` Incoming Webhook & Bot API Block Kit, `wecom` Group Robot, `qq` OneBot v11 / webhook gateway, `webhook`, `macos`) and `[[notify_routes]]` (plus secret-free project routing in `.starfane/team.toml`). **Split Ownership** (`node_local` vs `hub`) keeps work credentials isolated on local/peer hosts and prevents duplicate alerts.
- **Native `tmux` Backup & Reboot Restore**: Built-in `[tmux.backup]` periodically saves deduplicated `tmux` session/window/split-layout snapshots, can auto-restore missing sessions on daemon start (`auto_restore_on_start = true`), and optionally re-launches `claude --resume` / `codex resume` sessions (`starfane tmux backup | restore | backups`).
- **Swarm, Subagents & Evidence-Gated Playbooks**: Automatically folds native subagents and Swarm workers under parent sessions, surfaces live context-window utilization and generation throughput (`tok/s`), and provides **Feature Pipeline** (`Plan → Implement → Test & Review → Report`) and **Two-Speed Debug** (`Triage → Deep RCA`) with deterministic G1/G2/G3 verification.
- **Network-Agnostic `AccessGate`**: Precompiled IPv4/IPv6 `allowed_cidrs`, exact & `*.suffix` wildcard `allowed_hosts` (reverse-proxy friendly), named `presets` (`easytier`, `tailscale`), and `[[web.scoped_tokens]]` (`read_only` viewer or peer federation tokens) while strictly rejecting untrusted LAN and public traffic with `403 Forbidden`.

---

## Privacy & Zero-Telemetry Guarantee

`starfane` is **100% local-first** and will **never collect, transmit, fingerprint, or monetize any user data**:

- **Zero Telemetry — Not Even Opt-Out**: `starfane` contains no analytics SDKs (no PostHog, Sentry, Axiom, or external OTLP sinks), no crash reporters, no update-check phone-home requests, and no external web CDNs or third-party fonts. The embedded Web console enforces a strict `Content-Security-Policy` (`default-src 'self'; connect-src 'self'`).
- **Your Prompts, Code, & Credentials Stay Local**: `starfane` never uploads your prompts, transcripts, source code, file paths, usage counts, or hashes of your local `claude` / `codex` / `agy` authentication tokens. It never runs or requires a hosted cloud relay.
- **Zero Default Outbound Network Traffic**: Out of the box (`[[nodes]] = []`, `[[notifiers]] = []`, `[feishu] enabled = false`), `starfaned` makes **zero outbound network connections**—everything stays on your local Unix socket (`starfaned.sock`), loopback interface, and local state files (`~/.local/state/starfane/`).
- **Explicit, Auditable Network Boundaries**: Outbound traffic occurs *only* to destinations you explicitly configure in `~/.config/starfane/config.toml`—your own remote SSH/federated hosts (`crates/starfane-daemon/src/nodes.rs`) or your own notification endpoints (`crates/starfane-daemon/src/notify.rs`, `lark.rs`). Multi-host **Split Ownership** (`node_local` by default) ensures work-machine notification credentials never leave that machine.
- **Don't Trust—Verify**: `starfane` is a compact, zero-`node_modules` Rust workspace that works fully offline / air-gapped. You can audit every outbound call in minutes—and we commit never to introduce default-on or silent telemetry in future releases.

---

## Architecture

<p align="center">
  <img src="assets/architecture.png" width="100%" alt="starfane Architecture Diagram (BYO tmux, starfaned daemon, Control Surfaces)" />
</p>

## Playbooks & Evidence Gate

<p align="center">
  <img src="assets/workflow.png" width="100%" alt="starfane Feature Pipeline and Two-Speed Debug Workflows with G1/G2 Evidence Gate" />
</p>

---

## Quickstart

### Option A: One-Prompt Agent Setup (Recommended)

Send this prompt to Claude Code, Codex CLI, or Antigravity (`agy`). Your agent will inspect prerequisites, **ask for your confirmation before installing missing toolchains or writing hooks**, build `starfane`, and launch the local Web console on `http://127.0.0.1:27418/`:

```text
Please set up and start starfane (https://github.com/starlitxiling/starfane) on this machine and bring up its local Web console:

1. Inspect my environment first (OS, git, rustc/cargo >= 1.82, tmux and/or zellij >= 0.44, and installed agent CLIs: claude / codex / agy).
2. If Rust/Cargo or tmux/zellij is missing, or before modifying any agent hooks/MCP configs, show the exact commands or diff summary and ask for my explicit approval before installing or editing.
3. Clone https://github.com/starlitxiling/starfane.git into ~/starfane (or pull if present), build `cargo build --release --bin starfane`, and symlink `~/.local/bin/starfane` (ensure `~/.local/bin` is on `PATH`).
4. Run `starfane doctor` and `starfane install --all --dry-run`, show me the preview, then run `starfane install --all` once approved.
5. Keep the default loopback config (`127.0.0.1:27418` with token auth enabled; only set `[web] port` in `~/.config/starfane/config.toml` if port 27418 is busy or I request another port, and set `[web] lang = "en"` or pass `--lang en` if I want the English Web UI instead of the default Chinese `"zh"`), start `starfane daemon --detach`, verify `http://127.0.0.1:<port>/api/health` is healthy, and run `starfane web --print-url --no-open` to give me the ready-to-open local URL.
```

### Option B: Manual Setup

#### Prerequisites

- **Rust `1.82+`** and Cargo
- **`tmux`** and/or **`zellij` `>= 0.44`** *(optional; auto-detected when installed)*
- One or more interactive coding CLIs installed and authenticated: [`claude`](https://docs.anthropic.com/en/docs/claude-code), [`codex`](https://developers.openai.com/codex/cli), or `agy`
- *(Optional)* `lark-cli` if you enable two-way Feishu notifications & quote-reply commands

#### 1. Install

**Homebrew (macOS & Linux)** *(recommended)*:

```bash
brew install starlitxiling/tap/starfane
```

**Prebuilt Binaries (GitHub Releases)**:

Download `starfane-<tag>-<target>.tar.gz` from [GitHub Releases](https://github.com/starlitxiling/starfane/releases/latest) (macOS ARM64/Intel & Linux x86_64/ARM64):

```bash
tar -xzf starfane-*.tar.gz
mkdir -p ~/.local/bin
install -m 755 starfane-*/starfane ~/.local/bin/starfane
```

**Build from Source (Rust `1.82+`)**:

```bash
git clone https://github.com/starlitxiling/starfane.git
cd starfane
cargo build --release --bin starfane

mkdir -p ~/.local/bin
ln -sf "$(pwd)/target/release/starfane" ~/.local/bin/starfane
```

Verify `~/.local/bin` is on your `PATH`, then inspect your environment:

```bash
starfane doctor
```

### 2. Install Official Hooks & MCP Registration

Preview changes safely with `--dry-run` first (backs up existing configs automatically and preserves non-starfane hooks, status lines, and Codex `notify` settings):

```bash
starfane install --all --dry-run
starfane install --all
```

> Use `--agent claude`, `--agent codex`, or `--agent agy` to configure individual agents, or `--scope project` inside a repository. Run `starfane uninstall --all` at any time for clean, byte-preserving rollback.

### 3. Start the Daemon & Open the Web Console

```bash
starfane daemon --detach
starfane web
```

Print the resolved console URL without opening a browser:

```bash
starfane web --print-url --no-open
```

---

## Configuration

Create `~/.config/starfane/config.toml` (missing files use safe `127.0.0.1` + token-auth defaults and zero active notifiers):

```toml
[web]
bind = "127.0.0.1"              # Use "0.0.0.0" only when exposing to a private mesh / reverse proxy
port = 27418                    # Override if needed; change to any custom port you prefer
lang = "en"                     # Web console UI language at deployment: "zh" (default) or "en" (no in-UI switch)
auth_enabled = true             # Require per-boot token (or scoped_tokens); false only behind trusted CIDRs
allowed_cidrs = []              # Network-agnostic IPv4/IPv6 CIDRs (e.g. ["10.88.0.0/16", "fd00::/8"])
allowed_hosts = []              # Exact or *.suffix Host/Origin allowlist (e.g. ["console.example.com", "*.ts.net"])
presets = []                    # Optional named presets: ["easytier", "tailscale"]
allow_easytier = true           # Legacy preset toggle (still supported alongside presets/allowed_cidrs)
easytier_cidrs = ["10.144.144.0/24"]
allow_tailscale = false         # Legacy preset toggle (100.64.0.0/10, fd7a:115c:a1e0::/48, *.ts.net)
terminal_font = ""              # Optional local font prepended in Web terminal (e.g. "JetBrainsMono Nerd Font")
                                # Or drop a font at ~/.config/starfane/fonts/terminal.woff2 (or .ttf)

# Optional scoped tokens (read-only viewer or peer federation clients)
# [[web.scoped_tokens]]
# label = "viewer"
# token_env = "STARFANE_VIEWER_TOKEN"
# read_only = true

[notify]
watch_window_secs = 90
escalate_after_secs = 180
away_digest_after_secs = 600    # Coalesce multi-session completions while away
cooldown_secs = 120

[gate]
user_inactive_secs = 15
paste_settle_ms = 250
ack_timeout_ms = 4000
max_pointer_len = 300

# Legacy two-way Feishu card channel (synthesizes logical notifier "feishu-default")
[feishu]
enabled = false
lark_cli = "lark-cli"
chat_id = ""
allow_open_ids = []
allow_chat_ids = []

# Opt-in pluggable notifiers (`feishu`, `telegram`, `discord`, `slack`, `wecom`, `qq`, `webhook`, `macos`)
# [[notifiers]]
# id = "feishu-work"
# kind = "feishu"
# profile = "work"              # Optional `lark-cli --profile <name>`
# chat_id = "oc_xxx"
# ownership = "node_local"      # Default: only notifies for local sessions (keeps credentials isolated)
#
# [[notifiers]]
# id = "tg-ops"
# kind = "telegram"
# bot_token_env = "STARFANE_TG_TOKEN"
# chat_id = "-1001234567890"
# thread_id = 42                # Optional forum topic `message_thread_id`
# api_base_url = "https://api.telegram.org" # Optional proxy/override
# ownership = "hub"             # Can also notify for SSH zero-install hosts
#
# [[notifiers]]
# id = "discord-ops"
# kind = "discord"
# webhook_url_env = "STARFANE_DISCORD_WEBHOOK"
# username = "starfane"         # Optional webhook display name (default: "starfane")
# thread_id = "1234567890123456789" # Optional forum/thread ID (?thread_id=...)
# ownership = "hub"
#
# [[notifiers]]
# id = "slack-ops"
# kind = "slack"
# webhook_url_env = "STARFANE_SLACK_WEBHOOK" # Incoming Webhook mode (Block Kit)
# ownership = "hub"
#
# [[notifiers]]
# id = "slack-bot"
# kind = "slack"
# bot_token_env = "STARFANE_SLACK_BOT_TOKEN" # Or Bot Web API `chat.postMessage` mode
# channel = "C01234567"
# api_base_url = "https://slack.com/api"
# ownership = "hub"
#
# [[notifiers]]
# id = "wecom-ops"
# kind = "wecom"
# webhook_url_env = "STARFANE_WECOM_WEBHOOK" # WeCom Group Robot webhook (markdown / mentioned_list)
# ownership = "hub"
#
# [[notifiers]]
# id = "qq-ops"
# kind = "qq"
# api_base_url = "http://127.0.0.1:3000"     # OneBot v11 HTTP API (NapCat / Lagrange / LLOneBot)
# group_id = "123456789"                     # `group_id` and/or `user_id` (or use `webhook_url_env`)
# bot_token_env = "STARFANE_QQ_ONEBOT_TOKEN" # Optional Bearer access token
# ownership = "hub"
#
# [[notifiers]]
# id = "hook-ops"
# kind = "webhook"
# url = "https://hooks.example.com/starfane"
# secret_env = "STARFANE_WEBHOOK_SECRET"     # Optional Authorization: Bearer token
#
# [[notifiers]]
# id = "macos-local"
# kind = "macos"
# sound = "Glass"               # Optional macOS Notification Center sound
#
# [[notify_routes]]
# node = "tencent"
# project = "workflow"          # Also supports `cwd`, `agent`, `event_kinds`
# notifiers = ["tg-ops", "discord-ops", "slack-ops", "wecom-ops", "qq-ops"]

[paths]
claude = "claude"
codex = "codex"
agy = "agy"
tmux = "tmux"
zellij = "zellij"

[discovery]
include_shell_panes = false     # Set true to include plain tmux/zellij shell/script panes (`shell`)

[tmux]
socket_name = ""                # Optional `tmux -L <name>`

[tmux.backup]
enabled = false                 # Enable periodic tmux layout & agent-resume snapshots
interval_secs = 300             # Minimum 10s when enabled
max_snapshots = 20              # Rolling snapshot-*.json retention count
auto_restore_on_start = false   # Restore latest.json on daemon startup when tmux is empty
restore_agents = true           # Re-launch saved `claude --resume` / `codex resume` sessions
restore_bypass_permissions = false
exclude_sessions = []

[zellij]
enabled = true                  # Auto-discover Zellij (>= 0.44) sessions alongside tmux (skipped if absent)

[node]
id = "local"
display_name = "Local"          # Mutable at runtime via POST /api/hosts/{id}/rename

# Multi-host federation: mix zero-install SSH ControlMaster & peer starfaned daemons
# [[nodes]]
# id = "gpu-box"
# display_name = "GPU Server"
# kind = "ssh"
# ssh_target = "ubuntu@gpu-box" # user@host or ~/.ssh/config alias
# include_shell_panes = true
# notify_ownership = "hub"      # Default for SSH nodes
#
# [[nodes]]
# id = "mac-work"
# display_name = "Work Mac"
# kind = "peer"
# endpoints = ["http://10.144.144.2:27418", "http://100.64.0.2:27418"]
# token_env = "STARFANE_MAC_WORK_TOKEN"
# notify_ownership = "node_local" # Default for Peer nodes (Split Ownership: peer notifies locally)
```

> **Project-Scoped Notification Routing (`.starfane/team.toml`)**: Repositories can declare `[notify] notifiers = ["feishu-work"]` (or `[[notify.routes]]`) referencing **logical notifier IDs only**; credential/URL/secret keys in `.starfane/team.toml` are rejected at parse time.

> **Security Note**: `starfaned` compiles `AccessGate` once at startup and enforces `peer_ip_gate` (loopback `127.0.0.0/8` / `::1`, configured `allowed_cidrs`, and enabled presets), `Host` / same-origin `Origin` checks, and constant-time primary / scoped token authorization on every request. Untrusted LAN (`192.168.x.x`, `10.17.x.x`, `172.16.x.x`) and public IP requests are rejected with `403 Forbidden`.

---

## CLI Reference

| Command | Description |
| :--- | :--- |
| `starfane doctor` | Read-only check of CLIs, hooks, MCP, Codex trust hashes, `tmux` (`history-limit`), `zellij` (`>= 0.44`), daemon, and config |
| `starfane install [--all \| --agent X]` | Install marked hooks & MCP registrations with automatic backups (`--dry-run` supported) |
| `starfane uninstall [--all \| --agent X]` | Cleanly revert starfane-managed hook and MCP entries |
| `starfane daemon [--detach \| --foreground]` | Run the `starfaned` control-plane daemon (`--port`, `--lang zh\|en`, `--web-dir` for UI hot-reload) |
| `starfane web [--print-url] [--no-open]` | Open or print the Web console URL |
| `starfane ls [--all] [--project P]` | List active tmux/zellij/remote sessions, models, context usage, throughput, and pipelines |
| `starfane tmux backup [--force]` | Capture a tmux layout snapshot (`latest.json` + rolling archive, online or offline) |
| `starfane tmux restore [--file P] [--no-agents] [--dry-run]` | Recreate missing tmux sessions/windows/splits and resume saved agent sessions |
| `starfane tmux backups` | List saved tmux layout snapshots |
| `starfane handoff --from A --to B` | Hand off a compact structured context packet between sessions |
| `starfane pipeline new "<utterance>"` | Parse natural-language stage/model bindings and launch a `feature` pipeline |
| `starfane debug "<symptom; bindings>"` | Launch a Two-Speed Debug pipeline (`continue <id>` / `stop <id>`) |
| `starfane review <show\|feedback\|verdict\|precision>` | Inspect evidence-gated `review.v1` findings and historical precision |
| `starfane mcp --agent <claude\|codex\|agy>` | Run stdio MCP server (invoked automatically by registered agents) |
| `starfane emit --agent X` | Sub-10ms synchronous hook event forwarder (invoked by agent hooks) |

### MCP Tools (`starfane mcp`)

Registered agents (`claude`, `codex`, `agy`) receive 10 first-class stdio MCP tools:

- **`list_sessions`** — list live sessions, panes, models, states, and pipeline stages
- **`spawn_session`** — spawn a live interactive `claude` / `codex` / `agy` tmux session (`agent`, optional `model`, `effort`, `project_root`, `tmux_session`, `name`, `prompt`) and return `session_id`, `pane_id`, `tmux_target`, `tmux_label`, `agent`, `model`, `effort`, and `cwd`
- **`create_handoff` / `read_inbox` / `ack_handoff`** — structured cross-agent handoffs and inbox delivery
- **`submit_review` / `submit_falsifier_verdict` / `submit_triage` / `report_milestone`** — evidence-gated review, falsifier, triage, plan, RCA, and final-report submissions
- **`start_pipeline`** — parse natural-language bindings and start a human-confirmed Feature or Debug pipeline

Key new Web/Federation REST endpoints include `GET /api/hosts`, `POST /api/hosts/{id}/rename`, `GET /api/notifiers`, `POST /api/notifiers/mute`, `POST /api/notifiers/{id}/test`, cursor-paginated `GET /api/sessions/{id}/transcript?limit=&before=&all=1`, and full-history `GET /api/panes/{pane_id}/preview?lines=&before_line=&all=1`.

---

## Workspace Layout

```text
crates/
  starfane-proto      # Shared protocol types, HostRecord/HostId, wire schemas, and state transitions (serde-only)
  starfane-emit       # std-only hook collector hot path (<10ms) with offline disk spool
  starfane-adapters   # claude / codex / agy hook install, event normalization, L4 spawn args, doctor checks
  starfane-tmux       # TerminalMux trait, tmux + Zellij (>= 0.44) backends, ExecTransport (local & SSH), 7-point gate, backup/restore
  starfane-evidence   # G1/G2 deterministic evidence verifier for review / triage / rca
  starfane-binding    # Natural-language per-stage agent/model binding parser
  starfane-daemon     # tokio + axum daemon (REST/SSE, AccessGate, NotifyRouter, NodeProvider federation, transcript telemetry, MCP, Feishu)
bin/starfane          # Single CLI entry point
tools/fake-agent      # Interactive TUI + hook sandbox harness
web/                  # Zero-build embedded Web console (HTML/CSS + native ESM)
  index.html
  app.css
  app.js              # ES module entry point & router
  js/                 # Modular frontend: i18n, constants, store, dom, markdown, terminal, api, topbar, composer, workspace, views, overlays
tests/fixtures/       # Anonymized real-world hook payload fixtures (41 cases)
docs/                 # Architecture specs, crate contracts, research notes
```

### Development & Verification

```bash
cargo fmt --all -- --check
cargo clippy --workspace --all-targets -- -D warnings
for f in web/app.js web/js/*.js; do node --check "$f" || exit 1; done
cargo test --workspace
cargo test -p starfane-tmux -- --include-ignored
```

---

## Roadmap

### v0.1 — Core Control Plane & Embedded Console *(Shipped)*
- [x] BYO-`tmux` live pane discovery, 7-point safety injection gate, and official `claude` / `codex` / `agy` hooks + stdio MCP (`starfane emit` `<10ms`)
- [x] Zero-build ESM Web console with full cursor-paginated transcript, full terminal scrollback chunking, Prompt TOC, inline paste/image anchoring, and collapsible intermediate outputs
- [x] Native `[tmux.backup]` periodic layout snapshots, reboot auto-restore, and `claude --resume` / `codex resume` session recovery

### v0.2 — Multiplexer Abstraction, Federation & Guardrails *(Shipped)*
- [x] **Zellij (0.44+) Support** — Unified `TerminalMux` trait + `ZellijMux` session/pane discovery, capture, safe injection, focus, and spawning
- [x] **Multi-Host Federation (`[[nodes]]`)** — Mixed zero-install SSH `ControlMaster` nodes and multi-endpoint Peer `starfaned` nodes with runtime host renaming
- [x] **Pluggable Notification Routing & Split Ownership** — Opt-in `[[notifiers]]` (Feishu multi-profile, Telegram with forum topics, Discord rich embeds, Slack Incoming Webhook & Bot API Block Kit, WeCom Group Robot, QQ OneBot v11 / webhook, Webhook, macOS), `[[notify_routes]]`, and secret-free `.starfane/team.toml` routing
- [x] **Network-Agnostic `AccessGate` & Privacy Guarantee** — Precompiled IPv4/IPv6 `allowed_cidrs`, wildcard `allowed_hosts`, `read_only` / admin `scoped_tokens`, strict CSP, and zero telemetry

### v0.3 — Cross-Host Persistence & Mobile Onboarding *(Planned)*
- [ ] **Zellij Backup & Remote SSH Zellij** — Extend layout snapshot/restore and zero-install SSH discovery to cover remote Zellij sessions alongside `tmux`
- [ ] **Interactive Pairing & Native Chat Adapters** — One-time QR / short-code onboarding for remote Web browsers, plus native Slack and Discord interactive cards
- [ ] **Cross-Host Search & Usage Rollups** — Persistent conversation search and historical token/throughput analytics across federated nodes

### Exploring
- [ ] Pre-built release binaries (GitHub Releases / Homebrew tap) for source-free installation
- [ ] Extensible adapter interface for community coding CLIs beyond `claude`, `codex`, and `agy`

---

## License

[MIT](LICENSE)
