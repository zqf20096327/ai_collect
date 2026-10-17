# AnyCoding

> **Remote-control Claude Code, Codex, and other AI coding agents from your phone.**
> Stream your terminal AI session to a native Android app — no USB, no port forwarding, no LAN required.

[![License: Apache 2.0](https://img.shields.io/badge/license-Apache_2.0-blue.svg)](./LICENSE)
[![npm version](https://img.shields.io/npm/v/any-coding.svg)](https://www.npmjs.com/package/any-coding)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey)](#system-requirements)
[![Android](https://img.shields.io/badge/Android-7.0%2B-3DDC84?logo=android&logoColor=white)](#60-second-quick-start)
[![Open Core](https://img.shields.io/badge/model-open--core-orange)](./ARCHITECTURE.md)
[![Discord](https://img.shields.io/badge/Discord-join_chat-5865F2?logo=discord&logoColor=white)](https://discord.gg/HWs6GtCg)

**🌍 Language**: **English** · [中文](./README_ZH.md)

🌐 [**Landing page**](https://gurudin.github.io/anycoding/) &nbsp;·&nbsp;
📦 [**npm**](https://www.npmjs.com/package/any-coding) &nbsp;·&nbsp;
📖 [**Architecture**](./ARCHITECTURE.md) &nbsp;·&nbsp;
💬 [**Discord**](https://discord.gg/HWs6GtCg) &nbsp;·&nbsp;
🐛 [**Issues**](https://github.com/gurudin/anycoding/issues)

---

**AnyCoding** is an open-source toolkit that mirrors your terminal AI coding session — [Claude Code](https://github.com/anthropics/claude-code), [OpenAI Codex](https://github.com/openai/codex), or any other pty-based agent — from your Mac/Linux laptop to your Android phone in real time.

Run `any-coding` in any project directory and what you see on your phone is the **same pty process**: full ANSI color, truecolor, CJK wide characters, alt screen, and bracketed paste — rendered by a native Termux terminal view, not a web embed. Close your laptop, keep coding from the subway.

Two networking modes: **managed cloud relay** (zero config, 30-day free trial) or **fully self-hosted cloudflared direct mode** (no account, no closed-source server in the loop).

---

## Why AnyCoding

| Problem | What AnyCoding does |
|---|---|
| Mobile SSH clients can't drive Claude Code's TUI properly | **Native Termux `TerminalView`** with a Nerd Font and a full VT100 state machine — identical to a desktop terminal |
| Leaving home mid-session means two disconnected agent conversations | Your phone attaches to the **same pty process**. Closing the desktop window doesn't kill it; reconnecting auto-replays a 256 KB buffer |
| ngrok / frp / Tailscale are heavy to set up just for terminal sharing | `any-coding hub --public` spins up a cloudflared quick tunnel — phone scans the QR and connects |
| Sensitive code shouldn't go through third-party servers | Direct mode keeps everything on **your machine + cloudflared's encrypted tunnel** — no closed-source relay in the path |
| Multiple projects, multiple agents running in parallel | Run `any-coding` in each project directory; your phone's top tab bar switches between them |
| Want to host your own relay | Self-host via `ANYCODE_RELAY=https://your.host`, with multi-device management built in |

---

## 60-Second Quick Start

### 1. Install the CLI

```bash
npm install -g any-coding
```

Make sure at least one agent CLI is installed:

```bash
npm install -g @anthropic-ai/claude-code   # Claude Code
npm install -g @openai/codex               # OpenAI Codex
```

### 2. Install the Android app

Download the APK from [Releases](https://github.com/gurudin/anycoding/releases) (Android 7.0+). To build from source, see [`any-code-android/README.md`](./any-code-android/README.md).

### 3. Pick a networking mode

**A) Cloud mode** — managed relay, zero config

```bash
any-coding                    # in any project directory
```

The first run prints a **6-digit pair code and a QR code**. Scan or type it into the app to bind the device. Includes account system and a 30-day trial.

**B) Direct mode** — 100% self-hosted, no account

```bash
any-coding hub --public       # one-time: brew install cloudflared
```

Spins up a cloudflared quick tunnel and prints an `anycode://connect?url=...&token=...` URL + QR. The app scans and connects directly — **no AnyCoding cloud service, no account required**.

```bash
any-coding hub --public --tunnel=none          # LAN only (use your internal IP)
any-coding hub --public --tunnel=cloudflared   # default
```

---

## Features

- **Multi-agent support** — `any-coding claude [args]` / `any-coding codex [args]` with transparent argument passthrough
- **Interactive agent picker** — run `any-coding` with no args to choose Claude or Codex
- **Multi-tab, multi-project** — N `any-coding` processes = N tabs in the Android top bar
- **Session ownership** — desktop-launched sessions show 🖥 and can't be closed from the app (prevents orphaning your desktop viewer)
- **Reconnect replay** — 256 KB ring buffer restores TUI state after network drops or tab switches
- **Native Android terminal** — Termux `TerminalView`: CJK widths, truecolor, alt screen, bracketed paste — all correct
- **Public direct mode** — `hub --public` + cloudflared, zero accounts
- **Cloud relay with subscription gating** — FastAPI relay (closed source), pair codes, device tokens, trial/subscription enforcement
- **Multi-PC from one app** — bind multiple laptops, switch in the device picker
- **Self-hostable relay** — `ANYCODE_RELAY=https://your.host` environment variable
- **Coming soon** — more agents (Gemini / Aider / goose / Open Interpreter), agent plugin manifest system, iOS app, in-app session launcher

---

## Architecture

```
  Cloud Mode                                Direct Mode

  Android app                               Android app
      │ wss                                     │ wss
      ▼                                         ▼
  Hosted relay ◀── wss ─▶ any-coding        Cloudflared ◀── wss ─▶ any-coding
  (managed)               hub (Mac)         tunnel                 hub --public
                              │                                         │
                              ▼                                         ▼
                         pty.spawn(                                pty.spawn(
                           claude / codex)                           claude / codex)
```

- **Why does the Mac dial out?** Any NAT, home router, or coffee-shop WiFi works without port forwarding.
- **Why a local hub process?** So that your desktop Ghostty / iTerm viewer and your phone both attach to the **same pty** — closing the desktop terminal doesn't kill the agent session.
- **Why vendored Termux?** We tried WebView + xterm.js first; background `requestAnimationFrame` throttling, Gboard autocomplete, canvas sizing races, and soft-keyboard viewport jumps made it fragile. Termux's `TerminalView` is the most complete VT100/xterm implementation on Android.
- **Why doesn't the relay parse pty bytes?** Scale, privacy, and protocol agility. Adding a new agent requires zero relay changes.

Full design decisions and data flow in **[ARCHITECTURE.md](./ARCHITECTURE.md)**.

---

## Repository layout

```
anycoding/
├── any-code-cli/                 Node.js CLI (Apache-2.0)
│   ├── wrapper.js                Single file: hub / attach / pair / hub --public / logout
│   └── package.json              bin: any-coding
│
├── any-code-android/             Android app (Kotlin, Apache-2.0)
│   ├── app/                      WebView login/pairing + native terminal activity
│   ├── terminal-emulator/        Vendored Termux VT state machine (Apache-2.0)
│   └── terminal-view/            Vendored Termux Android View (Apache-2.0)
│
├── LICENSE                       Apache License 2.0
├── NOTICE                        Third-party attributions
├── ARCHITECTURE.md               Design decisions, data flow, open-core layering
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
└── .github/                      Issue / PR templates
```

> The cloud relay (FastAPI + MySQL + Redis) that powers accounts, subscriptions, and pair codes is operated as a managed service and is **not part of this repository**. Every client-side component — CLI and Android app — is here under Apache-2.0. Direct mode skips the managed relay entirely.

---

## Commands

| Command | What it does |
|---|---|
| `any-coding` | Interactive picker (1 = Claude, 2 = Codex); launches in the current directory |
| `any-coding claude [args...]` | Launch a Claude Code session; args pass through |
| `any-coding codex [args...]` | Launch an OpenAI Codex session; args pass through |
| `any-coding [legacy args...]` | If the first arg isn't a subcommand, default to Claude (backward-compatible with `-c`, `--dangerously-skip-permissions`, etc.) |
| `any-coding hub` | Run hub in the foreground (debug; default is detached) |
| `any-coding hub --public` | Foreground hub + cloudflared public tunnel (direct mode) |
| `any-coding restart-hub` | Restart hub (⚠️ kills all active sessions) |
| `any-coding pair` | Manually trigger pairing (rescan QR) |
| `any-coding logout` | Delete `~/.any-coding/device.json` and disconnect |

More detail — environment variables, config files, advanced usage — in [`any-code-cli/README.md`](./any-code-cli/README.md).

---

## Roadmap

**AnyCoding's north star is to be _the_ unified mobile front-end for any pty-based AI coding agent.** The roadmap reflects that — agent-ecosystem work is top priority.

### P0 — Agent ecosystem

- **More built-in agents** — `any-coding gemini` ([Gemini CLI](https://github.com/google-gemini/gemini-cli)), `any-coding aider` ([Aider](https://github.com/Aider-AI/aider)), `any-coding goose` ([goose](https://github.com/block/goose)), `any-coding interpreter` ([Open Interpreter](https://github.com/OpenInterpreter/open-interpreter))
- **Agent plugin manifest** — declarative format (binary name, install hint, prompt marker, icon, arg-passthrough rule) so community PRs can add new agents without touching core code. **Design draft**: [`docs/agent-manifest.md`](./docs/agent-manifest.md) — feedback welcome
- **Smart agent picker** — auto-detect which agents are installed locally; the interactive picker shows only what's available + install hints for what isn't

### P1 — Platform reach

- **Linux + Windows validation** — `package.json` already declares compatibility; needs real-device CI
- **iOS app** — SwiftTerm or WebView + xterm.js shell (same hub / relay protocol)
- **Manual pair-code fallback** — paste-a-URL flow when the camera is unavailable

### P2 — Session experience

- **In-app session launcher** — directory picker so sessions can be started from the phone (protocol ready, UI pending)
- **Named / pinned sessions** — friendly titles, reorderable tabs
- **Session log export** — export full ANSI log beyond the 256 KB ring buffer

### P2 — Developer infrastructure

- **GitHub Actions CI** — lint + build CLI + build APK on every PR
- **Signed APK releases** — tag triggers auto-build and attaches APK to GitHub Release
- **One-line installer** — `curl -fsSL install.anycoding.sh | bash` for non-npm environments

### P3 — Stretch

- Message counters (sent / replied) with per-agent accounting
- Server-side usage aggregation (cloud mode, for subscription quota)
- Quick-paste snippets, keyboard shortcuts, agent-specific macros

---

## System requirements

| Component | Minimum |
|---|---|
| CLI host | Node.js **≥ 18** on macOS / Linux / Windows |
| Agent CLI | At least one of `claude` (`@anthropic-ai/claude-code`) or `codex` (`@openai/codex`) |
| Android app | Android **7.0** (API 24)+ |
| Direct mode | `cloudflared` (install via `brew install cloudflared` or equivalent) |
| Self-hosted relay | Python 3.10+, MySQL 8, Redis 6, TLS-terminating reverse proxy |

---

## Privacy

| Mode | What the managed relay records | Prompt / pty content stored? |
|---|---|---|
| **Cloud** (managed relay) | Aggregate per-hour message counts — a row of `(user_id, platform, hour, direction, count)` each hour. Nothing about what you said. | ❌ No. pty bytes pass through relay in-memory only. |
| **`--public` / direct** | **Nothing.** Traffic goes phone ↔ cloudflared ↔ your machine; relay is not in the path. | N/A — relay never sees it. |
| **Self-hosted relay** | Whatever you configure. `ENABLE_STATS=false` disables the stats table; `ANYCODE_RELAY=...` points the CLI at your own relay. | Your call. |

The stats table exists so you can see your own usage (upcoming in-app dashboard) and to power subscription-quota accounting. It does not contain prompts, replies, file contents, or identifiers beyond your own `user_id`. Source of truth: [`any-code-server/`](https://github.com/gurudin/anycoding) (public soon).

---

## Community

- 💬 **[Discord server](https://discord.gg/HWs6GtCg)** — fastest way to ask questions, share setups, discuss new agents, and get dogfood help. Drop in and say hi.
- 🐛 **[GitHub Issues](https://github.com/gurudin/anycoding/issues)** — bug reports and feature requests (templates provided).
- 🔒 **Security**: please do **not** report vulnerabilities on Discord or Issues — see [SECURITY.md](./SECURITY.md) for the private channel.

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=gurudin/anycoding&type=Date)](https://www.star-history.com/#gurudin/anycoding&Date)

---

## Contributing

PRs and issues welcome. Please read first:

- [CONTRIBUTING.md](./CONTRIBUTING.md) — branch strategy, PR workflow, testing requirements (both modes must pass)
- [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) — Contributor Covenant v2.1
- [SECURITY.md](./SECURITY.md) — vulnerability disclosure (includes a safe-harbor clause)

Report bugs or request features on [GitHub Issues](https://github.com/gurudin/anycoding/issues) (templates provided). For anything conversational, join the [Discord](https://discord.gg/HWs6GtCg).

---

## Built on

| Dependency | Role | License |
|---|---|---|
| [node-pty](https://github.com/microsoft/node-pty) | pty process management | MIT |
| [ws](https://github.com/websockets/ws) | Node.js WebSocket | MIT |
| [qrcode-terminal](https://github.com/gtanner/qrcode-terminal) | ASCII QR codes in the terminal | Apache-2.0 |
| [Termux terminal-emulator / terminal-view](https://github.com/termux/termux-app) | Android native VT100 terminal | Apache-2.0 |
| [OkHttp](https://square.github.io/okhttp/) | Android WebSocket client | Apache-2.0 |
| [jsQR](https://github.com/cozmo/jsQR) | WebView QR decoding | Apache-2.0 |
| [cloudflared](https://github.com/cloudflare/cloudflared) | Direct-mode tunnel | Apache-2.0 |
| [JetBrains Mono](https://github.com/JetBrains/JetBrainsMono) | Monospaced terminal font | OFL-1.1 |

Full attributions in [NOTICE](./NOTICE).

---

## License

Licensed under the **[Apache License 2.0](./LICENSE)**.

- `any-code-cli/` and `any-code-android/app/` are original AnyCoding code.
- `any-code-android/terminal-emulator/` and `any-code-android/terminal-view/` are vendored from [Termux](https://github.com/termux/termux-app), retaining the upstream Apache-2.0 license.

Apache-2.0 provides an explicit **patent grant**, is compatible with every dependency above, and is commercial-use friendly. See [NOTICE](./NOTICE) for full third-party attribution.

---

<p align="center">
  <sub>
    Made with ❤️ for everyone who codes on the move.<br>
    <b>Keywords</b>: claude code mobile · claude code android · codex remote · ai coding agent · remote terminal · mobile pty · anthropic · openai codex · cloudflared tunnel · open-core
  </sub>
</p>
