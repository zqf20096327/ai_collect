# Adame

**most recent version downloadable in https://adame.ai**

**Adame is an agentic desktop app for macOS.** It pairs a native Electron + React
interface with a local Python agent backend, so you can run multi-step AI agents —
with tools, skills, an embedded terminal, and your own API keys — directly on your
machine.


## Features

- **Bring your own model.** Works with OpenAI, Anthropic, DeepSeek, or a local
  provider. API keys are stored encrypted on-device via the OS keychain
  (Electron `safeStorage`) — never in plaintext, never sent anywhere but the
  provider you configure.
- **Sign in with ChatGPT.** Optional OpenAI OAuth as an alternative to an API key.
- **Skills.** A large, extensible library of reusable agent skills (`skills/`)
  covering creative work, research, productivity, dev tooling, and more.
- **Tools & MCP.** Built-in tools (filesystem, terminal, and more) plus
  [Model Context Protocol](https://modelcontextprotocol.io) client support for
  connecting external tool servers.
- **Embedded terminal.** A real pty-backed terminal (xterm.js) inside the app.
- **Durable runs.** Turn checkpoints, context compaction, and on-device memory
  keep long agent sessions coherent.
- **image Generation in swarms** Tired of ChatGPT working on one image at a time per session? Adame gets you as many as you wish at once. 

## Architecture

Adame is two processes that talk over JSON-RPC on stdio:

| Layer | Stack | Location |
|-------|-------|----------|
| **Desktop UI** | Electron, React 19, TypeScript, Vite | `src/` |
| **Agent backend** | Python 3.11+ (JSON-RPC over stdio) | `backend/` |
| **Skills** | Markdown + assets, loaded at runtime | `skills/` |

- `src/main` — Electron main process: window, IPC, provider credentials, updater,
  and the bridge that spawns and supervises the backend.
- `src/preload` — the typed, sandboxed bridge exposed to the renderer.
- `src/renderer` — the React UI.
- `src/shared` — types shared across processes.
- `backend/adame_backend` — the agent runtime: providers, tools, skills loader,
  permissions, checkpoints, memory, MCP client, and more.

In **development** the backend runs straight from Python source. In a **packaged**
build it is compiled to a standalone binary (PyInstaller) and bundled, so end
users don't need Python installed.

## Getting started

### Prerequisites

- **macOS** (Adame is currently macOS-focused)
- **Node.js** 20.19+ (required by Vite 7) and npm
- **Python** 3.11 or newer (for development)

### Install

```bash
npm install

# Backend Python dependencies (into a virtualenv is recommended)
python3 -m venv .venv
source .venv/bin/activate
pip install -e backend
```

### Run in development

```bash
npm run dev
```

This launches the Electron app with hot-reload. The backend is started
automatically from `backend/server.py`.

> If you use a virtualenv or a non-default interpreter, point Adame at it with the
> `ADAME_PYTHON` environment variable:
>
> ```bash
> ADAME_PYTHON="$(pwd)/.venv/bin/python" npm run dev
> ```

### Configure a provider

On first launch, open **Settings → Account** and either add an API key
(OpenAI / Anthropic / DeepSeek) or sign in with ChatGPT. Keys are encrypted and
stored locally.

## Building a macOS app

```bash
# Compile the backend to a standalone binary, then build + package the app
npm run package:mac
```

> Note: signing, notarization, and auto-update publishing are configured for the
> original project's infrastructure. If you build your own distributable, update
> the `build` config in `package.json` (signing identity, `appId`, and the
> `publish` URL) to your own.

## Configuration reference

| Environment variable | Purpose |
|----------------------|---------|
| `ADAME_PYTHON` | Path to the Python interpreter used to run the backend in dev. Defaults to `python3`. |
| `ADAME_DATA_DIR` | Override the on-disk directory for app data (sessions, memory, secrets). |

## Project layout

```
.
├── src/            # Electron app (main / preload / renderer / shared)
├── backend/        # Python agent backend
│   ├── server.py           # JSON-RPC stdio entry point
│   └── adame_backend/      # runtime: providers, tools, skills, ...
├── skills/         # bundled agent skills
├── scripts/        # build tooling
└── build/          # app icon + macOS entitlements
```

## Contributing

Issues and pull requests are welcome. Please keep changes focused and, where it
makes sense, verify a dev build runs (`npm run dev`) before opening a PR.

## License

<!-- TODO: choose and add a license (e.g. MIT / Apache-2.0) and a LICENSE file. -->
_License to be determined._

Some bundled skills under `skills/` originate from third parties and carry their
own license files — see the individual skill directories.
