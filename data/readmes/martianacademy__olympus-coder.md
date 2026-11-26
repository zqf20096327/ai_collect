<div align="center">
  <img src="build/icon-dock.png" width="88" height="88" alt="Olympus Coder icon" />
  <h1>Olympus Coder</h1>
  <p><strong>One native workspace for every ACP coding agent — shared <code>~/.olympus</code> memory, parallel orchestration, built-in code workbench, and end-to-end encrypted phone access.</strong></p>
  <p>
    <code>v0.3.10</code> · <code>Apache-2.0</code> · <code>macOS · Linux VPS · Windows</code> · <code>ACP 2.6 + MCP</code> · <code>100% Free · Zero Login Wall</code>
  </p>
  <p>
    <a href="https://www.producthunt.com/products/olympus-coder?embed=true&amp;utm_source=badge-featured&amp;utm_medium=badge&amp;utm_campaign=badge-olympus-coder" target="_blank" rel="noopener noreferrer"><img alt="Olympus Coder - Open-source desktop &amp; VPS workbench for 18+ AI coding agents | Product Hunt" width="250" height="54" src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1325960&amp;theme=light&amp;t=1795331946472" /></a>
  </p>
  <p>
    <a href="https://olympus.marsnext.in/"><strong>Website</strong></a> ·
    <a href="https://github.com/martianacademy/olympus-coder/releases/latest"><strong>Download v0.3.10</strong></a> ·
    <a href="https://github.com/martianacademy/homebrew-tap"><strong>Homebrew Tap</strong></a> ·
    <a href="PRIVACY.md"><strong>Privacy Policy</strong></a>
  </p>
</div>

<picture>
  <source media="(prefers-color-scheme: light)" srcset="docs/screenshots/light-mode.png" />
  <img src="docs/screenshots/hero-code-mode.png" alt="Olympus Coder — Code Mode workspace with collapsible step timeline, inline diff, and CodeMirror 6 editor" width="100%" />
</picture>

---

## Install

### Desktop App (macOS · Windows · Linux)

macOS via Homebrew (Apple Silicon):

```sh
brew trust martianacademy/tap
brew install --cask martianacademy/tap/olympus-coder
```

Or download an installer from **[Releases](https://github.com/martianacademy/olympus-coder/releases/latest)** (`SHA256SUMS.txt` included):

| Platform | Installer |
| --- | --- |
| macOS · Apple Silicon | [`Olympus.Coder-0.3.10-arm64.dmg`](https://github.com/martianacademy/olympus-coder/releases/latest/download/Olympus.Coder-0.3.10-arm64.dmg) |
| macOS · Intel | [`Olympus.Coder-0.3.10.dmg`](https://github.com/martianacademy/olympus-coder/releases/latest/download/Olympus.Coder-0.3.10.dmg) |
| Windows 10/11 · x64 | [`Olympus.Coder.Setup.0.3.10.exe`](https://github.com/martianacademy/olympus-coder/releases/latest/download/Olympus.Coder.Setup.0.3.10.exe) |
| Linux · x64 (Debian/Ubuntu) | [`olympus-coder_0.3.10_amd64.deb`](https://github.com/martianacademy/olympus-coder/releases/latest/download/olympus-coder_0.3.10_amd64.deb) |
| Linux · x64 (any distro) | [`Olympus.Coder-0.3.10.AppImage`](https://github.com/martianacademy/olympus-coder/releases/latest/download/Olympus.Coder-0.3.10.AppImage) |

Builds are not code-signed yet:
- **macOS:** if Gatekeeper warns, run `xattr -dr com.apple.quarantine "/Applications/Olympus Coder.app"` once.
- **Windows:** on the SmartScreen prompt choose **More info → Run anyway**.
- **Linux:** install the `.deb` with `sudo apt install ./olympus-coder_0.3.10_amd64.deb`. The AppImage needs `chmod +x` and FUSE 2 (`libfuse2`; on Ubuntu 24.04 the package is `libfuse2t64`). If the AppImage exits with a sandbox error on Ubuntu 24.04+, use the `.deb` or start it with `--no-sandbox`.

### Headless Linux / macOS VPS Server (Zero Electron, Control from Phone or Browser)

```sh
curl -fsSL https://raw.githubusercontent.com/martianacademy/olympus-coder/main/scripts/install-server.sh | sh
olympus-server serve --relay --project .   # scan QR from phone over E2EE Cloudflare Relay
```

<details>
<summary>Keep headless server running on Linux boot (systemd)</summary>

```sh
mkdir -p ~/.config/systemd/user
olympus-server serve --relay --print-systemd > ~/.config/systemd/user/olympus-server.service
systemctl --user enable --now olympus-server
```

</details>

---

## Supported Coding Agents (20 Built-In & Registry CLIs · 2.5B+ Free Tokens / Month)

Install, authenticate, and rotate across **Claude Code**, **18 free-tier coding CLIs**, and **Local Ollama** right from **Settings → Agents & login** (plus 46+ total agents from the ACP Registry) — switching agents mid-thread without losing shared project memory:

| Agent | Free Allowance / Tier | Sign-In / Setup |
| :--- | :--- | :--- |
| <img src="docs/logos/claudecode.svg" width="16" height="16" align="top" alt="" /> **Claude Code** (`claude`) | Built-in native ACP (Pro / Max / API) | Reuses existing `claude` CLI login |
| <img src="docs/logos/antigravity.svg" width="16" height="16" align="top" alt="" /> **Google Antigravity** (`agy`) | Free personal Google quota (Gemini & frontier) | 1-click Google OAuth or `GEMINI_API_KEY` |
| <img src="docs/logos/codex.svg" width="16" height="16" align="top" alt="" /> **OpenAI Codex** (`codex`) | ChatGPT Free / Plus CLI allowance | 1-click ChatGPT login or `CODEX_API_KEY` |
| <img src="docs/logos/olympus.svg" width="16" height="16" align="top" alt="" /> **Olympus CLI** (`oly`) | OpenRouter `:free` models & unlimited Ollama (`$0`) | BYO keys, Ollama, or `oly login` |
| <img src="docs/logos/qwen.svg" width="16" height="16" align="top" alt="" /> **Qwen Code** (`qwen-code`) | **2,000 free req/day** (~1.5B tokens/mo) | In-app terminal OAuth or `DASHSCOPE_API_KEY` |
| <img src="docs/logos/geminicli.svg" width="16" height="16" align="top" alt="" /> **Gemini CLI** (`gemini`) | **~1,000 free req/day** (~750M tokens/mo) | Google OAuth (`/auth`) or `GEMINI_API_KEY` |
| <img src="docs/logos/iflow.svg" width="16" height="16" align="top" alt="" /> **iFlow CLI** (`iflow`) | **Uncapped free** Kimi K2, Qwen3 Coder, DeepSeek-V3 | In-app terminal sign-in or `IFLOW_API_KEY` |
| <picture><source media="(prefers-color-scheme: dark)" srcset="docs/logos/dark/opencode.svg" /><img src="docs/logos/opencode.svg" width="16" height="16" align="top" alt="" /></picture> **OpenCode** (`opencode`) | **12 zero-key `$0` models** out of the box | Works immediately or `opencode auth login` |
| <picture><source media="(prefers-color-scheme: dark)" srcset="docs/logos/dark/githubcopilot.svg" /><img src="docs/logos/githubcopilot.svg" width="16" height="16" align="top" alt="" /></picture> **GitHub Copilot** (`copilot`) | **Copilot Free** (50 agent req + 2k completions/mo) | `copilot login` or `GITHUB_TOKEN` |
| <img src="docs/logos/kiro.svg" width="16" height="16" align="top" alt="" /> **Kiro CLI** (`kiro`) | AWS Builder ID Free (50 agentic runs/mo) | `kiro-cli login` (Builder ID / Google / GitHub) |
| <picture><source media="(prefers-color-scheme: dark)" srcset="docs/logos/dark/kilocode.svg" /><img src="docs/logos/kilocode.svg" width="16" height="16" align="top" alt="" /></picture> **Kilo** (`kilo`) | Free signup credits + `$0` community models | `kilo auth login` or `KILOCODE_TOKEN` |
| <picture><source media="(prefers-color-scheme: dark)" srcset="docs/logos/dark/cline.svg" /><img src="docs/logos/cline.svg" width="16" height="16" align="top" alt="" /></picture> **Cline** (`cline`) | Free models + starter credits + BYO keys | `cline auth` or Keychain API keys |
| <picture><source media="(prefers-color-scheme: dark)" srcset="docs/logos/dark/cursor.svg" /><img src="docs/logos/cursor.svg" width="16" height="16" align="top" alt="" /></picture> **Cursor** (`cursor`) | Cursor Free / Hobby monthly agent allowance | `cursor-agent login` |
| <img src="docs/logos/codebuddy.svg" width="16" height="16" align="top" alt="" /> **Codebuddy** (`codebuddy`) | Tencent Cloud free tier with `Auto` routing | `codebuddy login` or `CODEBUDDY_API_KEY` |
| <picture><source media="(prefers-color-scheme: dark)" srcset="docs/logos/dark/qoder.svg" /><img src="docs/logos/qoder.svg" width="16" height="16" align="top" alt="" /></picture> **Qoder CLI** (`qoder`) | Community Free Edition + 14-day Pro trial | `qodercli login` or `QODER_PERSONAL_ACCESS_TOKEN` |
| <img src="docs/logos/mistral.svg" width="16" height="16" align="top" alt="" /> **Mistral Vibe** (`vibe-acp`) | Mistral La Plateforme free Experiment tier | Browser sign-in or `MISTRAL_API_KEY` |
| <picture><source media="(prefers-color-scheme: dark)" srcset="docs/logos/dark/zai.svg" /><img src="docs/logos/zai.svg" width="16" height="16" align="top" alt="" /></picture> **ZCode** (`zcode`) | Z.ai `zai-start-plan` free GLM coding tier | ZCode session or `ZAI_API_KEY` |
| <picture><source media="(prefers-color-scheme: dark)" srcset="docs/logos/dark/goose.svg" /><img src="docs/logos/goose.svg" width="16" height="16" align="top" alt="" /></picture> **Goose** (`goose`) | Open-source (`$0` with Ollama / free API keys) | `goose configure` or `GOOSE_PROVIDER` |
| <img src="docs/logos/openhands.svg" width="16" height="16" align="top" alt="" /> **OpenHands** (`openhands`) | Open-source (`$0` with Ollama / free API keys) | `openhands login` or `LLM_API_KEY` |
| <picture><source media="(prefers-color-scheme: dark)" srcset="docs/logos/dark/ollama.svg" /><img src="docs/logos/ollama.svg" width="16" height="16" align="top" alt="" /></picture> **Local Ollama** | Unlimited 100% offline local coding models | Local Ollama via `oly`, Goose, or OpenHands |

<sub>~2.5B+ monthly token estimate combines Qwen Code + Gemini CLI free daily allowances (~25k coding context) plus uncapped iFlow, 12 zero-key OpenCode models, recurring monthly tiers, and unlimited local Ollama. Upstream quotas are governed by each provider.</sub>

---

## Features

### Multi-Agent ACP Hub & Shared `~/.olympus` Brain
- **Mid-chat agent switching & handoff:** Start in Antigravity, continue in Claude Code, and ask Codex for a read-only **Second Opinion** in the same thread — prior goals, turns, and touched files transfer cleanly.
- **Two-tier persistent memory (`~/.olympus`):** Every agent shares `MEMORY.md`, `INSTRUCTIONS.md`, `BUGS.md`, `AGENTS.md`, skills, and cross-agent session transcripts instead of vendor-siloed folders (`~/.claude`, `~/.codex`, `~/.gemini`).
- **Custom API gateways & session import:** Point compatible agents at Anthropic/OpenAI-compatible providers with OS Keychain encryption, and import existing CLI sessions via ACP `session/list` & `session/load`.

### Calm Chat Timeline, Media Markup & Voice
<table>
  <tr>
    <td width="50%">
      <img src="docs/screenshots/elicitation-card.png" alt="Native ACP Elicitation card" width="100%" />
      <p align="center"><sub><strong>Native ACP Elicitation</strong> — Multi-question forms, custom answers &amp; OAuth inline in chat.</sub></p>
    </td>
    <td width="50%">
      <img src="docs/screenshots/annotate-editor.png" alt="Image and video markup editor" width="100%" />
      <p align="center"><sub><strong>Visual Mark Up</strong> — Draw arrows, circles &amp; numbered pins on screenshots or video frames.</sub></p>
    </td>
  </tr>
</table>

- **Collapsible `WorkGroup` timeline:** Thoughts, file reads/edits, searches, MCP calls, and sub-agents fold into a quiet monochrome strip with clickable right-side image thumbnails, customisable right-edge fade on live steps, and instant permission surfacing.
- **Shared Media Viewer & Mark Up:** Click any chat image, video, PDF, or attachment to zoom/pan in a centered sheet, draw annotations (baked at full resolution with an auto-generated coordinate legend for the agent), or **Add to message** without re-uploading.
- **Queueing, steering, slash commands & context control:** Queue follow-up messages while busy (with edit/remove & live `_session/steering`), autocomplete agent `/` slash commands, track context with a colour-coded ring, `/compact`, or carry over into a fresh thread.
- **Voice dictation & full Appearance studio:** Built-in mic button supporting System dictation, local `whisper.cpp` (auto-detected, Hinglish preset), OpenRouter, or custom OpenAI-compatible servers — plus dark/light themes, density, typography, sidebar spacing, separate phone appearance settings, and a live Theme CSS editor that imports any standard Tailwind / shadcn / [tweakcn](https://tweakcn.com) `globals.css` theme (in a draggable, resizable Settings window so you can watch the app change behind it).

### Built-In Code Workbench, Git Worktrees & Checkpoints
<table>
  <tr>
    <td width="50%">
      <img src="docs/screenshots/live-console.png" alt="Live command console alongside CodeMirror 6 editor" width="100%" />
      <p align="center"><sub><strong>Live Console &amp; CodeMirror 6</strong> — Syntax-highlighted command output alongside unsaved-buffer-aware tabs.</sub></p>
    </td>
    <td width="50%">
      <img src="docs/screenshots/editor-conflict-guard.png" alt="Per-turn shadow-git checkpoint diff and conflict guard" width="100%" />
      <p align="center"><sub><strong>Shadow-Git Checkpoints</strong> — Per-turn diffs (<code>+3 -2</code>), 1-click Undo/Redo &amp; unsaved conflict guard.</sub></p>
    </td>
  </tr>
</table>

- **CodeMirror 6 editor & detachable workbench:** Multi-tab editor with syntax themes, Markdown/KaTeX preview, unsaved-buffer awareness over ACP Client FS, smooth drag-to-reorder tool tabs, and pull-out / pop-out detached tool windows.
- **Per-turn Shadow-Git checkpoints & Git worktrees:** Automatic pre-prompt working-tree snapshots with per-turn diffs & 1-click Undo/Redo without touching `.git`, integrated Git staging/hunks/branches, and isolated **Worktree chats**.
- **WebGL Terminals, Saved Commands & Web Preview:** Multi-tab `node-pty` + `@xterm/addon-webgl` terminals with `⌘F` search, auto-detected 1-click **Run Tests** (*Ask agent to fix*), `EADDRINUSE` port killer, persistent saved commands across restarts, and an embedded localhost **Web Preview**.

### Parallel Orchestrator & Live `Tasks`
- **Built-in `olympus` MCP server:** Lead agents can spawn parallel sub-sessions (`spawn_subsession`), steer or switch models on quota limits (`message_subsession`, `configure_subsession`), run persistent terminals, and manage recurring **Schedules**.
- **Unified `Tasks` & OS process control:** Watch Olympus sub-sessions, native CLI sub-agents (ACP / JetBrains AIR / Antigravity / Claude), and child OS processes with live CPU/RAM meters, **Pause / Resume / Stop**, and thermal alerts.

### Fast Phone UI & End-to-End Encrypted Relay
<div align="center">
  <img src="docs/screenshots/phone-chat.png" width="36%" alt="Olympus Coder mobile chat view" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="docs/screenshots/phone-drawer.png" width="36%" alt="Olympus Coder mobile drawer" />
</div>

- **Full desktop parity from 320px+:** Same responsive app over **Same-Wi-Fi (`:47816`)** or the **AES-256-GCM E2EE Cloudflare Relay** (decryption key stays strictly in the URL `#fragment`) — with slimmed remote chat payloads, lazy-loaded heavy modules, live approvals, file editing, Git, and PTY terminals.
- **App Password & Touch ID lock:** `scrypt`-hashed authentication protects both local and remote sessions, with native macOS **Touch ID** unlock.

---

## Development & Self-Hosting

Requires **Node.js 22+** and native build tools for `node-pty` (Xcode CLT / `build-essential` + Python 3 / VS C++ Build Tools).

```sh
npm install          # install dependencies & rebuild node-pty for Electron
npm run dev          # launch with hot reload
npm run typecheck    # TypeScript check across main, preload, renderer & shared
npm run build        # production bundle -> out/
```

<details>
<summary>Build installers, run tests, self-host Cloudflare Relay &amp; repo layout</summary>

#### Package Desktop & Headless Server
```sh
npm run dist:mac     # macOS .dmg + .zip (arm64 / x64)
npm run dist:win     # Windows NSIS .exe
npm run dist:linux   # Linux .AppImage + .deb
npm run build:server && node scripts/package-server.mjs --portable
```

#### Self-Host the E2EE Cloudflare Relay
```sh
npm run build && node relay/scripts/copy-page.mjs
cd relay && npm install && npx wrangler deploy
```
Paste your `https://<worker>.workers.dev` URL into **Settings → Phone → Relay URL**.

#### Tests & Key Environment Variables
```sh
for t in tests/*.unit.mjs; do node "$t" || exit 1; done
OLYMPUS_TEST_HIDDEN=1 npx electron . --user-data-dir=/tmp/olympus-e2e --remote-debugging-port=9333
```
- `OLYMPUS_HOME` — override `~/.olympus` shared root (legacy `AGENTDESK_SHARED_ROOT` also honoured).
- `OLYMPUS_TEST_HIDDEN=1` — launch Electron hidden without stealing focus for automated CDP tests.

#### Repository Layout
- `src/main/` — Electron main process (ACP client, `acpClientFs`, `acpTerminals`, 46-agent `catalog`, `checkpoints`, `memory`, `orchestrator` MCP, `remote` LAN & `relay` E2EE tunnel).
- `src/renderer/` — Unified responsive React 19 + CodeMirror 6 + xterm.js UI & browser transport bridge.
- `src/shared/` — Cross-process types, quota/patch/slimming helpers.
- `relay/` — Stateless Cloudflare Worker + Durable Object E2EE WebSocket relay.
- `tests/` — Unit suites (`tests/*.unit.mjs`).

</details>

---

## Code signing policy

- **Status:** macOS builds are ad-hoc signed. Windows installers are not code-signed yet. We are applying for the open-source program of SignPath Foundation (not approved yet). If approved, Windows releases will carry: *Free code signing provided by [SignPath.io](https://about.signpath.io), certificate by [SignPath Foundation](https://signpath.org).*
- **What gets signed:** only Windows installers built by GitHub Actions ([`build.yml`](.github/workflows/build.yml)) from a tagged commit of this public repository, after the packaged-app smoke test ([`smoke.yml`](.github/workflows/smoke.yml)) passes. Binaries built anywhere else are never signed.
- **Open-source contents only:** installers ship only open-source components. Anthropic's proprietary Claude Agent SDK is not included. Olympus Coder downloads it from the public npm registry, and verifies its sha512 checksum, the first time you start Claude Code.
- **Team roles:**
  - Committers and reviewers: [Martian Academy](https://github.com/martianacademy) (maintainer). Outside contributions arrive as pull requests and are reviewed by a maintainer before merge.
  - Approvers: [Martian Academy](https://github.com/martianacademy) approves every signing request.
- **Privacy:** this program will not transfer any information to other networked systems unless specifically requested by the user or the person installing or operating it. The only automatic requests are:
  - the update check against GitHub Releases, which can be turned off in **Settings → General → Updates**;
  - the one-time Claude Agent SDK download, made when you choose Claude Code.

  Details: [PRIVACY.md](PRIVACY.md).

## Security, Contributing & License

- **Local-first & zero-knowledge relay:** State lives on disk under `~/.olympus`; provider API keys use OS `safeStorage`; Cloudflare Relay only ever sees `AES-256-GCM` ciphertext. See [PRIVACY.md](PRIVACY.md).
- **Contributing:** Pull requests welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) (DCO sign-off).
- **License:** [Apache License 2.0](LICENSE) · [NOTICE](NOTICE).
