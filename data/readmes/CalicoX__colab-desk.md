<div align="center">

# Colab Desk

**A lightweight, native macOS desktop workbench & local web app for the official [`google-colab-cli`](https://pypi.org/project/google-colab-cli/) (`colab`).**

Zero runtime npm dependencies · Offline-ready · Bilingual (EN / 中文)

[English](./README.md) · [简体中文](./README.zh-CN.md)

[![CI](https://github.com/CalicoX/colab-desk/actions/workflows/ci.yml/badge.svg)](https://github.com/CalicoX/colab-desk/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/CalicoX/colab-desk?label=macOS%20App)](https://github.com/CalicoX/colab-desk/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Platform](https://img.shields.io/badge/Platform-macOS%20Apple%20Silicon-black.svg)](https://github.com/CalicoX/colab-desk/releases)

</div>

---

Colab Desk turns the official `google-colab-cli` (`colab` binary) into a complete visual GPU/TPU workbench. Drive Google Colab runtimes through **AI Agents**, a **Zero-Agent Direct Script Runner**, **manual CLI commands**, or a **full interactive PTY terminal & split view** — without memorizing CLI flags or re-implementing Google's runtime protocol.

## Table of Contents

- [Key Features](#key-features)
- [Quick Start](#quick-start)
- [Workflow Guides](#workflow-guides)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Architecture](#architecture)
- [Privacy & Security](#privacy--security)
- [License](#license)

## Key Features

### Multi-Agent Hub (Works With or Without Local Agent CLIs)
- **AGY (`agy acp`)**: Native Antigravity ACP protocol integration with Antigravity OAuth/Enterprise login, live plan tier detection, model picker, thinking level (`Low / Medium / High / Extra`), and live quota tracking.
- **Grok (`grok`)**: Streaming NDJSON chat with live thinking stream and real-time weekly quota tracking.
- **OpenCode (`opencode acp`)**: ACP protocol support with 30-day & lifetime token/cost stats.
- **Custom OpenAI-Compatible API Profiles**: Works out of the box with **no local Agent CLI installed** — save multiple profiles (OpenAI, DeepSeek, OpenRouter, Gemini, local Ollama, etc.) with built-in Colab tool calling.
- **Inline Code Execution**: Every fenced code block in an Agent reply has a **`▶ Run`** button (`colab ssh` for Bash/Shell, `colab exec` for Python).

### Direct Parameterized Script Runner (Zero Agent)
- Run Python (`colab exec`) or Bash (`colab ssh`) inference, training, and deployment scripts directly on the Colab VM — **completely bypassing cloud LLMs**.
- Built-in templates for **ComfyUI 1-Click Deployment**, **Diffusers / Image & Video Inference**, and **Custom Scripts**.
- Automatically parses `{{param}}` placeholders in any script into an interactive parameter form, injects variables from your local Env Vault (`ENV` + `COLAB_PARAM_*`), and renders generated images/videos inline when output paths are printed.

### Interactive Colab Terminal & Split View (`⌘J`)
- Automatically appears once connected to an active Colab VM (strictly scoped to remote Colab VMs — no local host shell exposed).
- Switch smoothly between **Chat**, **Split (Chat + Terminal)**, and **Terminal**.
- Powered by locally vendored `xterm.js` + POSIX PTY over WebSocket (`colab ssh -s <session>`), supporting multiple tabs, dynamic resize (`SIGWINCH`), scrollback replay, TUI tools (`vim`, `htop`, `nvidia-smi`, `claude`, `agy`, `opencode`), and 1-click **"Send to Agent"** (grabs the last 50 lines of terminal output into the Agent composer for debugging).

### Live GPU / VRAM Telemetry, Process Killer & Auto Port Forwarding
- Collapsible right inspector (`⌘.`) polls real-time `nvidia-smi` metrics (VRAM, GPU utilization, temperature) — configurable in **Settings → General**.
- **GPU Compute Process List**: Inspect PIDs and per-process VRAM usage with **1-click Kill** (`kill -9`).
- **Auto-Detected Web Ports + Presets**: Automatically detects active listening TCP ports on the VM as 1-click forward-and-open chips, alongside presets for **ComfyUI (`:8188`)**, **Gradio (`:7860`)**, **Jupyter (`:8888`)**, **Ollama (`:11434`)**, **vLLM (`:8000`)**, and **TensorBoard (`:6006`)** via `colab ssh --proxy-mode`.

### Cloud File Explorer & Media Gallery
- Visual browser for `/content` and Google Drive (`/content/drive/MyDrive`) with **List** and **Media Gallery** modes.
- Inline **MP4 / WebM / MOV video playback** (HTTP `206 Range` scrubbing), image/text preview, multi-select **Batch Download**, **1-click Save to Google Drive**, drag-and-drop upload, and **"Analyze with Agent"**.

### Env Vault, Auto-Bootstrap & Local ↔ Cloud Folder Sync
- **Env Vault (`0600`)**: Store `HF_TOKEN`, `CIVITAI_API_KEY`, `WANDB_API_KEY`, etc. locally in `~/.config/colab-desk/state.json` and auto-inject them into `/etc/profile.d/colab-desk-env.sh` & `/root/.bashrc`.
- **Auto-Bootstrap**: Automatically mount Google Drive, enable `hf_transfer`, persist `HF_HOME` on Google Drive, install `uv`, and run a custom startup Bash script whenever a new VM is created (or trigger manually anytime).
- **Local ↔ Cloud Folder Sync**: Bind a local project folder to `/content/...` and push or pull via `tar.gz` over `colab upload`/`download`/`ssh` (automatically excluding `.git`, `node_modules`, `__pycache__`, `.DS_Store`, `.venv`, and `dist`).

### Native macOS Desktop Experience
- Categorized **Settings** modal with instant search (`/`), **Dark / Light / System** theme sync, **System / 中文 / English** language switching, **Command Palette (`⌘K`)**, `.ipynb` / `.md` transcript export, prompt templates, and in-app **Check for Updates** (Settings → About).
- Built-in `colab` CLI diagnostics, one-click `uv`/`pip3` installation, and OAuth sign-in.

---

## Quick Start

### Requirements

- **macOS (Apple Silicon)** for the prebuilt `.app`, or any OS with **Node.js 20+** and **Python 3** for the web app
- **[`google-colab-cli`](https://pypi.org/project/google-colab-cli/)** (`colab` binary — can also be installed and authenticated directly inside **Settings → Colab CLI**)

### Option 1: Download Prebuilt macOS App (Recommended)

1. Download **`Colab-Desk-macOS-arm64.zip`** from [GitHub Releases](https://github.com/CalicoX/colab-desk/releases) (or [`dist/Colab-Desk-macOS-arm64.zip`](./dist/Colab-Desk-macOS-arm64.zip)).
2. Unzip and move **`Colab Desk.app`** to `/Applications`.
3. Because the app is ad-hoc signed, if macOS Gatekeeper warns on first launch, run:
   ```bash
   xattr -cr "/Applications/Colab Desk.app"
   ```
   *(Or right-click `Colab Desk.app` → **Open**.)*

### Option 2: Run as Local Web App

```bash
git clone https://github.com/CalicoX/colab-desk.git
cd colab-desk
npm start
```

Opens at `http://127.0.0.1:4173` (set `PORT=...` to override).

### Option 3: Build & Launch the macOS App from Source

```bash
npm run app
```

Compiles `macos/ColabDesk.swift` into `dist/Colab Desk.app`, generates the squircle icon from `macos/AppIcon.png`, signs ad-hoc, packages `dist/Colab-Desk-macOS-arm64.zip`, and launches the app. Set `COLAB_DESK_NO_LAUNCH=1` to build without launching.

### Run Unit Tests

```bash
npm test
```

---

## Workflow Guides

### 1. Zero-Agent Parameterized Script Runner (Image / Video Generation & ComfyUI)

1. Connect to a GPU session (e.g., `T4`, `L4`, `A100`).
2. Click **Direct Runner** in the top bar (or press `⌘K` → *Direct Script Runner*).
3. Pick a built-in template or write your own Python / Bash script using `{{parameter}}` placeholders:
   ```python
   import os
   prompt = "{{prompt}}"
   steps = int("{{steps}}")
   out_path = "/content/output.png"
   # ... run your model locally on the Colab GPU ...
   print(out_path)
   ```
4. Fill in the auto-generated form fields and click **Run**. Any printed `/content/*.png|jpg|webp|mp4|webm|mov` path is automatically displayed inline with preview & download actions.

### 2. One-Click ComfyUI / WebUI Port Forwarding

- When ComfyUI (`:8188`), Gradio (`:7860`), or any other service starts on the Colab VM, the right inspector (`⌘.`) automatically detects the listening port and shows a clickable chip — click it to open an SSH tunnel via `colab ssh --proxy-mode` and launch it in your browser.
- You can also click the built-in **ComfyUI `:8188`** preset directly.

### 3. Env Vault & Auto-Bootstrap

1. Open **Settings → Colab CLI**.
2. Add keys like `HF_TOKEN`, `CIVITAI_API_KEY`, or `WANDB_API_KEY` in **Env Vault**.
3. Toggle **Auto-Bootstrap on New Session** options (Mount Google Drive, `hf_transfer`, Drive `HF_HOME` cache, install `uv`, or custom Bash script).
4. Every newly created VM is automatically initialized, or click **Bootstrap** in the right inspector to run it on an existing session.

---

## Keyboard Shortcuts

| Shortcut | Action |
| --- | --- |
| `⌘K` | Open global Command Palette (works even when Terminal is focused) |
| `⌘J` | Cycle view mode: Chat → Split → Terminal (when connected to a VM) |
| `⌘B` | Toggle left navigation rail |
| `⌘.` | Toggle right Inspector panel (GPU telemetry, ports, files, sync) |
| `/` | Focus search bar inside Settings |
| `⌘Enter` | Send message / run command |
| `Esc` | Close active modal or palette |

---

## Architecture

- `src/server.mjs` — Zero-dependency HTTP + RFC 6455 WebSocket server (including HTTP `206 Range` media streaming)
- `src/plan.mjs`, `src/run.mjs`, `src/parse.mjs`, `src/desk.mjs` — Official `colab` CLI argv planner, runner, output parser, and session transcript state
- `src/agent.mjs` — ACP (`agy`, `opencode`), Grok NDJSON, and OpenAI-compatible tool-calling Agent hub
- `src/terminal.mjs` & `src/pty-bridge.py` — Interactive Colab SSH PTY manager & WebSocket bridge
- `src/cloud-ops.mjs` — GPU telemetry & process killer, auto port detection, remote file/media explorer, Direct Script Runner, Auto-Bootstrap, folder sync, `.ipynb`/`.md` export, and GitHub update check
- `src/colab-env.mjs` — `colab` CLI diagnostics, one-click `uv`/`pip3` install, and OAuth login
- `src/store.mjs` & `src/i18n.mjs` — Atomic local disk persistence (`0600`) and EN/ZH dictionary
- `macos/ColabDesk.swift` — Lightweight AppKit + `WKWebView` native shell (no login shell, no Keychain access)
- `public/index.html` — Single-file frontend with locally vendored `xterm.js`

## Privacy & Security

- **Local-only storage**: Settings, API keys, and Env Vault entries are stored strictly on your machine in `~/.config/colab-desk/state.json` with `0600` file permissions.
- **Official CLI only**: Colab Desk never handles your Google credentials directly and never re-implements Colab's runtime protocol — all Colab authentication and execution go through the official `colab` binary.
- **Clean builds**: `scripts/build-mac-app.sh` strips local build paths (`-file-prefix-map` + `strip -x`) so release binaries contain no personal paths or user data.

## License

Released under the [MIT License](./LICENSE).
