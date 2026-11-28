# SailTerm

**[English](README.md) | [中文](README.zh.md)**

> A cross-platform desktop SSH / SFTP / FTP terminal with AI built in — the AI works on your servers through the established session, but never sees your credentials.

## Why this exists

I'm a developer who has to look after a handful of servers. Doing that day to day meant juggling an SSH client, a file-transfer tool, and a browser tab where I paste error messages and ask an AI what went wrong. Two things bothered me:

1. **The workflow is fragmented** — context keeps getting lost between the terminal, the files, and the answer.
2. **General-purpose AI agents can end up seeing hostnames, accounts, passwords and private keys**, and I didn't want to bet my servers on that.

So I built SailTerm: one desktop app where the terminal, file transfer and AI live together — and where the AI can do its job **without ever touching your credentials**.

I'm not a professional operations engineer, so the feature set reflects what a developer actually needs and probably misses things a real SRE would take for granted. Feedback and pull requests welcome.

## Credentials never reach the AI

- Hosts, accounts, passwords and private keys live only in the Rust core process and are stored in the **OS keychain** (falling back to an AES-256-GCM encrypted file). They never leave it.
- The AI operates **through the already-established SSH session** via a `session_id` handle — it says *what* to do, the app executes it. Write and high-risk actions always require your explicit approval, and everything is recorded in an audit log.
- Terminal output is **sanitized before it goes out to the model**: password / secret / token / private-key-block patterns and internal IPs are masked.

In short: the model sees your problem, never your keys. Full trust boundaries are described in [SECURITY.md](SECURITY.md).

## Architecture

Two process layers, one narrow bridge: the renderer holds no credentials and makes no network requests — everything sensitive lives in the Rust core.

- **Renderer (WebView)** — React 19 + TypeScript + Vite: xterm.js terminal, file / transfer / monitor / audit panels, a lightweight store, i18n and themes. Every Tauri call funnels through `src/lib/tauri/` — no credentials, no network.
- **Rust core (`src-tauri/`)** — a single process owning the sensitive surface:
  - `commands`: IPC entry — the only surface the frontend can call
  - `session`: SSH / SFTP / FTP / Telnet / serial / Mosh sessions (russh · suppaftp)
  - `vault`: credential vault — OS keychain (AES-256-GCM file as fallback)
  - `ai`: orchestration state machine · sanitizer · policy engine · approval · audit · multi-model providers (BYOK)
  - `files` / `db` / `plugin`: transfer queue & cache · SQLite (WAL) + migrations · session recordings · local plugins
- Only two channels cross the seam: **commands (invoke)**, downward, and **event streams** (terminal bytes / transfer progress / streamed AI tokens), upward.

- **The seam is enforced, not just promised**: any frontend file outside `src/lib/tauri/` that touches the Tauri API is rejected by a lint script (`scripts/check-ipc-boundary.sh`); the only two outbound paths are AI provider requests and the SSH/FTP connections themselves, both inside the Rust core.
- **One AI turn, end to end** (where the security model lands architecturally): question → context assembly (archived output already sanitized) → provider replies or calls a tool → policy engine tiers the risk (read-only / write / high-risk) → writes and worse suspend for human approval (editable) → execution goes through the already-open session handle (`session_id`) → output sanitized again before feeding back to the model → loop until an answer. Credentials are in none of these boxes.

| Layer | Choice |
|---|---|
| Desktop framework | Tauri 2 (Rust core + system WebView) |
| Frontend | React 19 + TypeScript + Vite |
| Terminal | xterm.js (+ fit / search / web-links / webgl addons) |
| SSH / FTP | `russh` / `suppaftp` |
| Persistence | SQLite + OS keychain |
| AI | Multi-model provider layer + tool-calling orchestration (lightweight state machine, no heavyweight agent framework) |

## Features

- **Connections**: SSH / SFTP / FTP / FTPS / Telnet / serial / Mosh, local terminal, multi-tab and split views, reconnect, host-key management, SSH key store (private keys stay in the vault)
- **AI**: run commands / read output / transfer files through the session; tiered policy (read-only / write / high-risk) with human approval and edit-before-approve; sanitized output; full audit log; in-terminal agent mode and sidebar chat
- **Files**: dual-pane SFTP/FTP browser, remote editing with confirm-before-write, transfer queue with resume
- **Productivity**: command snippets with variables, multi-host broadcast, SSH local port forwarding, session monitor, session recording & playback, sealed (encrypted) connection export/import, themes, i18n (zh/en), plugin system

## Download

Grab a build from **[Releases](https://github.com/owen-yue/SailTerm/releases)**:

- **macOS (Apple Silicon)**: `SailTerm_0.1.0_aarch64.dmg` — open it and drag SailTerm.app into Applications.
  > This build is signed with a self-signed certificate and **not notarized by Apple**. If Gatekeeper blocks the first launch, **right-click the app → Open → click Open again** once (or run `xattr -cr /Applications/SailTerm.app`).
- **Intel macOS / Windows / Linux**: no prebuilt binary yet — build from source (below).

## Development

Requirements: **Node.js 20+ with pnpm**, **Rust stable**, plus Tauri 2 platform deps (Xcode CLT on macOS; WebView2 + C++ Build Tools on Windows; `webkit2gtk` on Linux).

```bash
pnpm install

pnpm tauri dev       # run the full desktop app with hot reload
pnpm check           # tsc --noEmit + IPC-boundary lint + production build
pnpm test            # frontend unit tests (vitest)
cd src-tauri && cargo test   # Rust unit tests

pnpm tauri build     # production build (per-platform installer in src-tauri/target/release/bundle/)
```

## Packaging

- **macOS**: `bash scripts/package-macos.sh` — builds and assembles a `.dmg` under `dist-bundle/` (uses `hdiutil` directly; the default Tauri dmg script is unreliable in non-interactive environments).
- **Linux**: `bash scripts/package-linux.sh` (deb/rpm/AppImage per Tauri config).
- **Windows**: `pwsh scripts/package.ps1`.

The release flow and the current signing/notarization status are described in [RELEASE.md](RELEASE.md) (the macOS build is signed with a self-signed certificate and not notarized; on first launch you must allow Gatekeeper manually).

## Platform status

- **macOS** is the primary platform, verified on real hardware.
- **Windows / Linux** compile through the same toolchain but are not yet hardware-validated — treat them as experimental; bug reports welcome.
- This is an **early preview (0.x)**. A prebuilt dmg is available for macOS (Apple Silicon) on [Releases](https://github.com/owen-yue/SailTerm/releases); build other platforms from source.

## A note on language

Source comments and the AI tool prompts are written in **Chinese by design** — the prompts are functional instructions to the model, not UI text. The UI itself is fully internationalized (zh/en built in). If you contribute, please keep touched code readable in either language; English translations of comments you touch are welcome.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) for the dev setup, conventions and the checks to run before opening a PR.

## License

MIT — see [LICENSE](LICENSE). Third-party components are listed in [THIRD-PARTY-LICENSES.md](THIRD-PARTY-LICENSES.md) (regenerate after dependency changes: `python3 scripts/gen-third-party-licenses.py`).
