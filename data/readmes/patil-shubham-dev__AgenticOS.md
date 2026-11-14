<div align="center">

# AgenticOS

### A universal desktop harness for AI coding agents — one window, any model, free keys first

**English** · [简体中文](README.zh-CN.md)

![Windows](https://img.shields.io/badge/Windows-x64-0078D4?logo=windows&logoColor=white)
![macOS](https://img.shields.io/badge/macOS-Apple%20Silicon-000000?logo=apple&logoColor=white)
![Cores](https://img.shields.io/badge/cores-DeepSeek%20·%20Codex%20·%20Gemini%20·%20OpenRouter%20·%20Ollama%20·%20more-4D6BFE)
![Node](https://img.shields.io/badge/node-%E2%89%A522.19-3C873A?logo=node.js&logoColor=white)
[![MIT License](https://img.shields.io/badge/license-MIT-2EA44F)](LICENSE)

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="new-2.42304.0/docs/images/session-dark-en.png">
  <img src="new-2.42304.0/docs/images/session-en.png" alt="AgenticOS session view" width="100%">
</picture>

</div>

<br>

## What it is

AgenticOS is a desktop application that puts the Claude Desktop **Code** workflow — sessions, composer, transcript, tool rows, diffs, panes, settings — in front of a **universal model harness**. The UI is a faithful recreation of the Claude Desktop 2.42304.0 interface, built from components sliced out of the shipped app and driven by a thin host layer. The engine behind it is provider-agnostic: every model is a pluggable core, so the app never knows which vendor it is talking to.

The design goal is simple: **the window is ours, the engine is ours, and the default path costs nothing** — free-tier API keys or a fully local model.

- **Same UI, same behavior**: sidebar and session rail, composer with model/effort menus, transcript (working line, tool rows, diffs), task list and next-step box, Context breakdown, settings, menus and shortcuts.
- **Same capabilities**: permission modes and approval cards, plans, side chats, routines, dynamic multi-phase workflows, terminal, preview, files and changes panes, MCP, skills, plugins and hooks.
- **Your model, your keys**: DeepSeek Harness (built in), Codex, Kimi, Qwen, MiniMax, Gemini, OpenCode, ZCode, MiMo, OpenRouter, Groq, Mistral, Cerebras, Ollama / LM Studio, or any OpenAI-compatible endpoint. Per-model display names, context windows and image input.
- **No Claude account**: pay your provider directly, or pay nothing on a free tier. Settings and history stay on your machine.

## Architecture

```
┌──────────────────────────────┐
│  app/  (Electron + React)    │   Window, panes, transcript, settings
│  - src/generated/            │   Official components, sliced by generators
│  - electron/                 │   Main process, preload, IPC, core registry
└──────────────┬───────────────┘
               │  bridge protocol (stdio / JSON events)
┌──────────────▼───────────────┐
│  harness/  (Node ESM)        │   Provider-agnostic engine
│  - packages/*-bridge         │   DeepSeek, Codex, ACP (Kimi/Qwen/…), OpenCode
│  - packages/*-app            │   Session loop, tools, permissions, usage
└──────────────┬───────────────┘
               │  HTTPS / local sockets
┌──────────────▼───────────────┐
│  Model providers             │   Free tiers, paid keys, local servers
└──────────────────────────────┘
```

The app layer is intentionally "dumb": it renders state and forwards intent. Provider logic — auth, endpoints, model catalogs, quirks, rate limits — lives behind adapters in `harness/`. Adding a provider is a new adapter plus a catalog entry, never an app change.

## Tech stack

| Layer | Technology |
|---|---|
| Desktop shell | Electron (main process `electron/main.cjs`) |
| UI | React 19, ProseMirror, xterm.js, Shiki, Phosphor icons, KaTeX |
| Build | Vite, electron-packager, custom generators (`app/scripts/extract-*.mjs`) |
| Engine | Node.js ESM harness packages (`@code-desktop/*`) |
| Protocols | OpenAI-compatible HTTP, Anthropic Messages, Gemini native, ACP, Codex app-server, OpenCode serve |
| Tests | `node --test` (app and harness suites) |
| Language | JavaScript / JSX (ESM) primarily; Python helper scripts in `new-2.42304.0/scripts/` |

## Repository layout

| Path | Contents |
|---|---|
| `new-2.42304.0/` | The current source tree (New UI, recreated from Claude Desktop 2.42304.0). |
| `new-2.42304.0/app/` | Electron + React application. |
| `new-2.42304.0/harness/` | Provider-agnostic engine and adapters. |
| `poc/opencode/` | Measurement probes and evidence from the OpenCode integration PoC. |
| `SPEC.md` | Feature-by-feature spec of the Claude app surface, with one test per feature. |
| `features.md` | Product intent: our own engine and window, running on free keys. |
| `Difference.md` | Gap analysis between the spec and the current implementation. |
| `REVERSE.md` | Verified architecture map, IPC/core inventory, and roadmap notes. |
| `AUDIT.md` | Evidence-based audit: environment, build state, provider architecture, parity. |
| `OpenCode-Integration.md` | Investigation and integration plan for the OpenCode backend. |
| `NOTICE.md` | Third-party attribution. |

## Requirements

- **Node.js 22.19 or newer** (this repo is validated on Node 26).
- **Windows 10/11 x64** or **macOS on Apple Silicon**.
- An API key for at least one provider, **or** a local OpenAI-compatible server (Ollama / LM Studio) for a zero-key setup.

## Installation and development

Everything runs inside the version folder:

```bash
git clone https://github.com/patil-shubham-dev/AgenticOS.git
cd AgenticOS/new-2.42304.0

# Engine
cd harness && npm ci

# App
cd ../app && npm ci

# Run in development
npm run dev

# Build the renderer
npm run build

# Start Electron against the build
npm start
```

> `npm run build` runs `prepare:ui`, which needs the `reference/` assets (fonts, icons) used to slice the interface. Those assets are intentionally **not** committed (large binaries); see `new-2.42304.0/docs/windows.md` and `AUDIT.md`. `npx vite build` works once `public/` assets are present.

Tests:

```bash
cd new-2.42304.0/harness && npm test
cd new-2.42304.0/app && npm test
```

Packaging (Windows / macOS) uses `npm run package:win` or `npm run package` inside `app/` and requires the reference assets.

## Configuration

- **Providers and models** are configured in **Settings › Models**. You can connect an official API key, an OpenAI-compatible base URL + key, or a keyless local server.
- **Keys** are stored locally (Electron `safeStorage` for provider keys; no keys are ever written to the repository). Definitions live in `providers.json`; keys live in OS-protected storage.
- **User data** stays on the machine:
  - Windows: `%APPDATA%\AgenticOS\` (and DeepSeek session data under `~/.dsh/`).
  - macOS: `~/Library/Application Support/AgenticOS/`.
- Only conversation content is sent to the provider you selected. There is no telemetry and no license server.

## Usage

1. Launch the app and open **Settings › Models**.
2. Pick a core — for a free start choose a free-tier preset or point at a local Ollama / LM Studio server.
3. Start a session, describe a task, and approve tool actions as they appear.
4. Use the model menu to change model or reasoning effort per turn; use side chats for quick tangents and the Changes pane to review diffs.

## Implemented features

Shipped and exercised in the current tree:

- Full Claude Desktop Code UI surface: sidebar, session rail, composer, environment bar, transcript, tool rows, diffs, task list, next-step box, Context breakdown.
- Permission modes and approval cards; plans; side chats; routines; dynamic workflows; terminal; preview; files/changes panes; MCP; skills; plugins; hooks.
- Multi-provider engine with adapters for DeepSeek Harness, Codex app-server, ACP agents (Kimi/Qwen/Qwen-family/…), and OpenCode.
- OpenAI-compatible presets, including free-tier providers (OpenRouter, Gemini, Groq, Mistral, Cerebras) and keyless local presets (Ollama, LM Studio).
- Per-model metadata: display name, context window, image input, reasoning effort, tool-calling style.
- Provider-key encryption at rest and redaction in logs/UI.
- Windows support: `win32-x64` packaging path, path-separator fixes, Windows-aware shell handling.

## Roadmap

Planned or in progress — explicitly **not** presented as done:

- Native Anthropic Messages and Gemini protocol adapters (Gemini currently uses the OpenAI-compatible path).
- Fallback routing: model chains (primary → alternate → local) that degrade on rate limits.
- Usage/rate-limit metering surfaced before limits are hit.
- Capability detection maturity: richer per-model degradation of unsupported UI affordances.
- Remaining Windows parity work and full packaging verification on Windows.
- SambaNova preset and additional free-tier providers.
- Broader app-level test coverage for the gaps recorded in `AUDIT.md` §5.3.

## Testing status

This project reports its own test baselines honestly rather than claiming a clean run:

- **Harness suite:** 847 tests — 771 pass, 70 fail (environment-class: Windows symlinks, POSIX signals, missing external CLIs), 6 skipped.
- **App suite:** 5,963 tests — 4,978 pass, 908 fail (dominated by missing `reference/` + `vendor/` inputs and Windows test-harness path bugs, not product logic), 13 cancelled, 64 skipped; roughly 63 minutes.

See `AUDIT.md` §5.3 for the full breakdown.

## Documentation

- [`SPEC.md`](SPEC.md) — feature spec and build plan.
- [`features.md`](features.md) — product intent and free-key strategy.
- [`Difference.md`](Difference.md) — spec vs implementation gap analysis.
- [`REVERSE.md`](REVERSE.md) — verified architecture and integration map.
- [`AUDIT.md`](AUDIT.md) — environment, build, and parity audit.
- [`OpenCode-Integration.md`](OpenCode-Integration.md) — OpenCode backend plan.
- [`NOTICE.md`](NOTICE.md) — third-party attribution.

## License and attribution

Released under the [MIT License](LICENSE).

This project builds on earlier work whose MIT license and attribution are preserved. It is an independent client for the models it drives; it is **not affiliated with, endorsed by, or sponsored by Anthropic**. "Claude" is a trademark of Anthropic, used only to describe the interface this project recreates. Third-party components and their licenses are recorded in [`NOTICE.md`](NOTICE.md).
