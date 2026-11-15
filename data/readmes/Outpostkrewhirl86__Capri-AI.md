<div align="center">

# CAPRI

### Your personal desktop AI agent. Built for Night City, runs on your PC.

A local-first desktop agent with a cyberpunk soul. Capri sits on your machine, understands your intent, and executes: files, apps, browser, terminal, code. Plug in Claude Code, Codex, Antigravity or any other model backend and let it work.

<br/>

[![Release](https://img.shields.io/github/v/release/Outpostkrewhirl86/capri-ai?style=for-the-badge&color=f5e90a&labelColor=0b0b0f)](https://github.com/Outpostkrewhirl86/capri-ai/releases/latest)
[![Stars](https://img.shields.io/github/stars/Outpostkrewhirl86/capri-ai?style=for-the-badge&color=ff2a6d&labelColor=0b0b0f)](https://github.com/Outpostkrewhirl86/capri-ai/stargazers)
[![Platform](https://img.shields.io/badge/platform-Windows%2010%20%7C%2011-blue?style=for-the-badge&labelColor=0b0b0f)](#installation)
[![Build](https://img.shields.io/badge/build-portable%20ZIP-9d4edd?style=for-the-badge&labelColor=0b0b0f)](#installation)
[![License](https://img.shields.io/github/license/Outpostkrewhirl86/capri-ai?style=for-the-badge&labelColor=0b0b0f)](LICENSE)

[**Download for Windows**](https://github.com/Outpostkrewhirl86/capri-ai/releases/latest) &nbsp;|&nbsp; [Features](#features) &nbsp;|&nbsp; [Architecture](#architecture) &nbsp;|&nbsp; [Roadmap](#roadmap) &nbsp;|&nbsp; [FAQ](#faq)

</div>

---

## What is Capri

Capri is an open desktop AI agent inspired by the aesthetics and ideas of the **Cyberpunk: Edgerunners** universe: a fast, sharp, always-on netrunner assistant that lives on your machine instead of a browser tab.

Most AI tools stop at a chat window. Capri goes further. It is an **agent runtime with a native desktop shell**: it receives a goal in natural language, plans the steps, calls tools on your system, observes the results, and iterates until the job is done. Think of it as your own Jarvis, only with a neon HUD and a much better soundtrack.

Capri is model-agnostic. It wraps the coding and reasoning agents you already use, such as **Claude Code**, **Codex** and **Antigravity**, behind one unified interface, so you can switch the brain without changing the body.

> Capri is an independent fan-inspired project. It is not affiliated with, endorsed by, or sponsored by CD PROJEKT RED, Studio Trigger, Netflix or Anthropic. See [Disclaimer](#disclaimer).

---

## Features

### Agent core

| Capability | Description |
|---|---|
| **Natural language to action** | Describe the outcome you want. Capri decomposes it into a plan of tool calls and executes it step by step. |
| **Multi-backend brain** | Hot-swap between Claude Code, Codex, Antigravity and other compatible agent backends from a single dropdown. |
| **Persistent memory** | Long-term context store so Capri remembers your projects, preferences and recurring workflows between sessions. |
| **Streaming reasoning view** | Watch the plan, tool calls and intermediate results in real time, with the ability to pause, edit or abort at any step. |
| **Task queue** | Fire off multiple jobs and let them run concurrently while you keep working. |

### System control

| Capability | Description |
|---|---|
| **File operations** | Search, read, create, move, rename and batch-process files and folders with natural language. |
| **Terminal execution** | Run shell commands inside a sandboxed session with live output and a full audit log. |
| **App and window control** | Launch applications, focus windows, trigger hotkeys and automate repetitive UI flows. |
| **Browser automation** | Open pages, extract data, fill forms and run multi-step web tasks through a controlled browser context. |
| **Clipboard and screen context** | Optionally feed the current clipboard or a screen region to the agent as context. |

### Developer mode

| Capability | Description |
|---|---|
| **Code agent integration** | Delegate refactors, bug hunts, test generation and repo analysis to your connected coding backend. |
| **Git awareness** | Diff, commit, branch and review changes with natural language, always behind a confirmation gate. |
| **Plugin and tool API** | Register custom tools with a simple JSON schema and let the agent call them. |
| **MCP compatibility** | Connect external tool servers through the Model Context Protocol. |

### Interface

- **Neon HUD overlay.** A lightweight always-on-top panel summoned with a global hotkey.
- **Command palette.** Keyboard-first input with fuzzy search over tools, history and saved workflows.
- **Voice input.** Push-to-talk dictation for hands-free commands.
- **Themes.** Built-in cyberpunk themes with adjustable glow, scanline and glitch intensity, plus a clean minimal mode.
- **Tray mode.** Runs quietly in the system tray with low idle footprint.

---

## Architecture

```
                 +--------------------------------------+
                 |             Capri Desktop            |
                 |   HUD overlay | Palette | Tray | Voice|
                 +------------------+-------------------+
                                    |
                           IPC / event bus
                                    |
                 +------------------v-------------------+
                 |             Agent Runtime            |
                 |  Planner -> Executor -> Observer     |
                 |  Memory store | Task queue | Policy  |
                 +---------+----------------+-----------+
                           |                |
              +------------v---+      +-----v--------------+
              | Backend Adapters|     |    Tool Layer      |
              | Claude Code     |     | FS | Shell | Web   |
              | Codex           |     | Apps | Git | MCP   |
              | Antigravity     |     | Custom plugins     |
              | Custom provider |     +--------------------+
              +-----------------+
```

**Design principles**

- **Local-first.** Your files, memory and logs stay on your machine. Only the prompts and context you choose to send leave it, and only to the backend you configured.
- **Adapter pattern.** Every model backend implements a small, typed interface, so adding a new provider is a matter of writing one adapter.
- **Human in the loop.** Destructive or irreversible actions pass through a configurable policy layer that requires explicit approval.
- **Observable by default.** Every plan, tool call and result is recorded in a structured, inspectable session log.

---

## Installation

> **Current platform support:** Windows 10 and Windows 11 (x64).
> **Current distribution:** portable ZIP build. No installer yet.

Capri ships as a self-contained portable archive. No installation, no registry changes, no admin rights required.

1. Open the [latest release](https://github.com/Outpostkrewhirl86/capri-ai/releases/latest).
2. Download `Capri-portable-x.y.z.zip`.
3. Extract the archive to any folder, for example `D:\Apps\Capri`.
4. Run `Capri.exe`.

On first launch, Capri walks you through connecting a backend.

Because the build is portable, you can keep it on a secondary drive or a USB stick. All settings, memory and logs are stored next to the executable, so moving or backing up Capri is just copying one folder.

**Updating.** Download the new ZIP and extract it over the old folder. Your `config.json`, `memory` and `tools` directories are preserved.

**Windows SmartScreen note.** New releases may not yet have an established reputation, so Windows can show a SmartScreen prompt. If you downloaded the archive from this repository's Releases page, choose **More info** and then **Run anyway**.

---

## Quick start

### 1. Connect a backend

Open **Settings > Backends** and pick the agent you want to power Capri:

| Backend | Setup |
|---|---|
| Claude Code | Sign in with your Anthropic account or provide an API key |
| Codex | Sign in with your OpenAI account or provide an API key |
| Antigravity | Sign in with your Google account |
| Custom | Point Capri at any compatible endpoint |

### 2. Summon Capri

Press the global hotkey (default `Ctrl + Alt + Space`) to open the HUD from anywhere.

### 3. Give it a job

```text
Sort my Downloads folder by file type, move installers into /Installers and delete duplicates older than 30 days.
```

```text
Open the project in D:\dev\netrunner, find why the tests in /auth are failing and propose a fix.
```

```text
Every morning at 9:00, open my dashboard, grab yesterday's numbers and put them in a note.
```

Capri shows its plan first. Approve it, edit it, or let it run in autonomous mode for trusted task types.

---

## Configuration

Capri reads its configuration from `config.json` located next to `Capri.exe`. Everything is also available in the Settings UI.

```json
{
  "backend": "claude-code",
  "hotkey": "Ctrl+Alt+Space",
  "theme": "edgerunner",
  "memory": {
    "enabled": true,
    "retentionDays": 90
  },
  "policy": {
    "requireApproval": ["delete", "shell", "git.push", "network.upload"],
    "autonomousMode": false
  },
  "sandbox": {
    "allowedPaths": ["C:\\Users\\you\\Projects", "C:\\Users\\you\\Downloads"]
  }
}
```

### Registering a custom tool

```json
{
  "name": "check_gpu_temp",
  "description": "Returns the current GPU temperature in Celsius",
  "command": "powershell -File tools/gpu_temp.ps1",
  "input_schema": {
    "type": "object",
    "properties": {},
    "required": []
  }
}
```

Drop the file into the `tools\` folder next to `Capri.exe` and restart Capri. The agent discovers it automatically.

---

## Security and privacy

- **Scoped access.** Capri can only touch directories you explicitly allow.
- **Approval gates.** Deletion, shell execution, pushes and uploads are gated by policy.
- **Audit log.** Every action is written to a local, append-only session log.
- **No telemetry by default.** Capri does not collect usage analytics unless you opt in.
- **Secrets stay local.** API keys and tokens are stored in the Windows Credential Manager, not in plain text.

Found a vulnerability? Please open a private security advisory instead of a public issue.

---

## Roadmap

- [x] Windows desktop shell with HUD overlay (portable)
- [x] Multi-backend adapter layer
- [x] File, shell and app tools
- [x] Portable ZIP build
- [x] Persistent memory
- [ ] Browser automation toolkit
- [ ] Voice input and wake word
- [ ] MCP server marketplace
- [ ] Workflow recorder and shareable macros
- [ ] Multi-agent mode with specialist sub-agents
- [ ] Scheduled and event-triggered tasks
- [ ] macOS and Linux builds
- [ ] Mobile companion for remote task dispatch

Have an idea? Open a [feature request](https://github.com/Outpostkrewhirl86/capri-ai/issues/new).

---

## FAQ

**Is Capri free?**
Capri itself is free and open source. Your chosen backend may require its own subscription or API key.

**Does it work offline?**
The desktop shell, tools and memory work offline. Reasoning requires a connected backend unless you point Capri at a local model endpoint.

**Is this the Capri from the show?**
No. Capri is an original project that borrows the mood of the cyberpunk genre and the Edgerunners universe. It has no official connection to the series.

**Can I use my own model?**
Yes. Implement the backend adapter interface or point Capri at any compatible endpoint.

**Will you support macOS and Linux?**
It is on the roadmap. Windows comes first.

---

## Contributing

Pull requests are welcome. For major changes, open an issue first so we can talk through the design.

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit your changes
4. Push and open a pull request

---

## Community

If Capri saves you time, a star helps other people find it. Bug reports, ideas and feedback live in [Issues](https://github.com/Outpostkrewhirl86/capri-ai/issues).

---

## License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for details.

---

## Disclaimer

Capri is an independent, community project inspired by the cyberpunk genre and the Cyberpunk: Edgerunners universe. All trademarks, series names and related properties belong to their respective owners. No affiliation or endorsement is implied.

<div align="center">

**Wake the hell up, samurai. We have a desktop to run.**

</div>
