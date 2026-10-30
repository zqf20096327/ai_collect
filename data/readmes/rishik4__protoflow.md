<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/protoflow-logo-white.png">
    <img alt="ProtoFlow" src=".github/assets/protoflow-logo.png" width="420">
  </picture>
</p>

<p align="center">
  <b>AI PCB design on your desktop.</b><br>
  Describe a circuit in plain English. ProtoFlow drafts the schematic with real parts, lays out and routes the board, checks it, and exports native KiCad files and Gerbers.
</p>

<p align="center">
  <a href="#download"><b>Download</b></a> ·
  <a href="docs/README.md"><b>Docs</b></a> ·
  <a href="#use-protoflow-with-your-ai-agent"><b>Agent quick start</b></a> ·
  <a href="https://www.protoflow.ai">Website</a> ·
  <a href="#get-help">Get help</a>
</p>

<p align="center">
  <a href="https://github.com/rishik4/protoflow/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/rishik4/protoflow?label=release&color=3b82f6"></a>
  <img alt="Platforms" src="https://img.shields.io/badge/macOS%20%C2%B7%20Windows%20%C2%B7%20Linux-desktop-0f172a">
  <a href="https://discord.gg/cAzH6XTUmN"><img alt="Discord" src="https://img.shields.io/badge/chat-Discord-5865F2"></a>
</p>

![ProtoFlow designing an ESP32 breakout board from one prompt, then editing a six-layer board with part search, datasheets and a SPICE simulation](docs/media/protoflow-demo.gif)

ProtoFlow is a free desktop app for designing circuit boards, with AI built in. Learn more at **[protoflow.ai](https://www.protoflow.ai)**.

## Download

<!-- downloads:start -->
| Platform | Download | Version |
|---|---|---|
| macOS (Apple silicon and Intel) | [.dmg](https://github.com/rishik4/protoflow/releases/download/v3.3.1/ProtoFlow-3.3.1-macOS.dmg) | [3.3.1](https://github.com/rishik4/protoflow/releases/tag/v3.3.1) |
| Windows 10/11 (x64) | [Installer (.exe)](https://github.com/rishik4/protoflow/releases/download/v3.3.1/ProtoFlow-3.3.1-Windows-x64-Setup.exe) | [3.3.1](https://github.com/rishik4/protoflow/releases/tag/v3.3.1) |
| Linux (x86_64) | [.AppImage](https://github.com/rishik4/protoflow/releases/download/v3.3.1/ProtoFlow-3.3.1-Linux-x86_64.AppImage) · [.tar.gz](https://github.com/rishik4/protoflow/releases/download/v3.3.1/ProtoFlow-3.3.1-Linux-x86_64.tar.gz) | [3.3.1](https://github.com/rishik4/protoflow/releases/tag/v3.3.1) |
| Linux (arm64) | [.AppImage](https://github.com/rishik4/protoflow/releases/download/v3.0.5/ProtoFlow-3.0.5-Linux-arm64.AppImage) · [.tar.gz](https://github.com/rishik4/protoflow/releases/download/v3.0.5/ProtoFlow-3.0.5-Linux-arm64.tar.gz) | [3.0.5](https://github.com/rishik4/protoflow/releases/tag/v3.0.5) |
<!-- downloads:end -->

ProtoFlow is free to download. You only need to install it once, after that it updates itself. These are the same installers [protoflow.ai/download](https://www.protoflow.ai/download?ref=github) serves, and each release has a `SHA256SUMS.txt` if you want to check your download.

### System requirements

| | Requirements |
|---|---|
| macOS | macOS 11 or later. One universal app for Apple silicon and Intel Macs. macOS 14 or later is recommended for the AI features. |
| Windows | Windows 10 or 11, x64. The installer is per-user, so no administrator prompt. |
| Linux | x86_64 or arm64, glibc 2.35 or newer (Ubuntu 22.04 or newer, or a similar distro). The arm64 build can be a few versions behind. |

You also need an internet connection and a free ProtoFlow account. You sign in when the app first opens.

### Install

- **macOS:** open the `.dmg`, drag **Protoflow** into Applications, then open it. The app is signed and notarized by Apple.
- **Windows:** run the setup `.exe` and follow the steps. If SmartScreen says "Windows protected your PC", click **More info**, then **Run anyway**.
- **Linux:** make the AppImage executable (`chmod +x`) and run it. Or unpack the `.tar.gz` and run `install-local.sh`, which adds a menu entry and a `protoflow` launcher.

The [Getting started guide](docs/getting-started.md) has the full steps, then walks you through your first project.

## Use ProtoFlow with your AI agent

Paste this into Claude Code, Codex, Cursor, Gemini CLI, or any coding agent that can run commands:

```text
Install ProtoFlow on this computer and help me start my first circuit board.
Follow https://github.com/rishik4/protoflow/blob/main/AGENTS.md
```

The agent picks the right installer for your system, checks its checksum, installs it, and walks you through your first project. It asks before it installs anything. [AGENTS.md](AGENTS.md) is written for agents, but it's short and readable if you want to see what it will do.

Already use Claude Code or Codex? ProtoFlow's [Max mode](docs/max-mode.md) can run whole-board design work through the agent you already have.

## What you can do with it

### Go from a sentence to a schematic

Type what the circuit should do, for example "USB-C powered ESP32-S3 board with a LiPo charger". ProtoFlow places real, orderable parts, wires them, and runs the electrical checks. Everything it draws stays editable, and you can roll back any AI change. [AI assistant docs](docs/ai-assistant.md)

![ProtoFlow's AI assistant generating a schematic from a prompt](docs/media/ai-generate-board.gif)

### Lay out and route the board

Draw or pick a board outline, auto-place parts, and run the built-in autorouter. Then check the result with DRC and look at it in 3D. [PCB editor](docs/pcb-editor.md) · [Auto-place and autoroute](docs/layout-automation.md)

![ProtoFlow PCB editor: board outline, the autorouter routing traces, then the 3D board view](docs/media/pcb-autoroute-3d.gif)

### Find real parts

Search LCSC and the built-in library in one dialog, open datasheets, and place parts straight into the design. If a part has no symbol or footprint, [Component Lab](docs/component-lab.md) can build one from its datasheet. [Components and parts](docs/components-and-parts.md)

![ProtoFlow's component search dialog finding and placing a part](docs/media/part-search.gif)

### Keep working in KiCad, or bring designs in

ProtoFlow opens and saves `.kicad_sch` and `.kicad_pcb` files directly, so you can switch between ProtoFlow and KiCad on the same project. It also imports designs from other EDA tools. [Files, import and export](docs/files-and-import-export.md)

### Review, collaborate, and ship

Leave comments on parts, edit with a teammate in real time, and step back through visual version history. When the board is ready, export Gerbers, drill files and a BOM, or order boards. [Manufacturing](docs/manufacturing.md)

![Two people editing the same schematic in a live ProtoFlow session](docs/media/collaboration.gif)

## Documentation

Start with **[Getting started](docs/getting-started.md)**. The full index is in [docs/](docs/README.md), and there are more guides at [protoflow.ai/docs](https://www.protoflow.ai/docs?ref=github).

| Design | AI | Board and output | Workspace |
|---|---|---|---|
| [Schematic editor](docs/schematic-editor.md) | [AI assistant](docs/ai-assistant.md) | [PCB editor](docs/pcb-editor.md) | [Files, import and export](docs/files-and-import-export.md) |
| [Components and parts](docs/components-and-parts.md) | [Max mode](docs/max-mode.md) | [Auto-place and autoroute](docs/layout-automation.md) | [Collaboration](docs/collaboration.md) |
| [Wiring](docs/wiring.md) | [Component Lab](docs/component-lab.md) | [Design checks (ERC/DRC)](docs/design-checks.md) | [Comments and reviews](docs/comments-and-reviews.md) |
| [Power and nets](docs/power-and-nets.md) | [What the AI can do](docs/ai-tools.md) | [Manufacturing](docs/manufacturing.md) | [Version control](docs/version-control.md) |
| [Annotations and regions](docs/annotations-and-regions.md) | [Datasheet viewer](docs/datasheet-viewer.md) | [BOM](docs/bom.md) | [Settings](docs/settings.md) |
| [Symbol editor](docs/symbol-editor.md) | | [Simulation](docs/simulation.md) | [UI customization](docs/ui-customization.md) |
| [Footprint editor](docs/footprint-editor.md) | | | [Keyboard shortcuts](docs/keyboard-shortcuts.md) |

## Get help

- **Discord:** ask questions and share boards at [discord.gg/cAzH6XTUmN](https://discord.gg/cAzH6XTUmN).
- **Contact:** [protoflow.ai/contact](https://www.protoflow.ai/contact), or email [admin@protoflow.ai](mailto:admin@protoflow.ai).
- **Docs:** search the [docs index](docs/README.md) or [protoflow.ai/docs](https://www.protoflow.ai/docs?ref=github).

If something in the app doesn't match the docs, check that ProtoFlow is up to date first.

## FAQ

**Is ProtoFlow free?**
Yes. The full editor is free, including PCB layout, autorouting, ERC/DRC, and KiCad and Gerber export, and free accounts get a daily allowance of AI messages. Paid plans add more AI usage, stronger models and Max mode. See [pricing](https://www.protoflow.ai/pricing).

**Does it replace KiCad?**
It can be your whole editor, or you can use it next to KiCad. Both apps read and write the same files.

**Where are my projects stored?**
On your computer. Projects are folders of ordinary files, and uninstalling ProtoFlow doesn't touch them.

## About this repository

- `docs/` has the user guide, with GIFs.
- [Releases](https://github.com/rishik4/protoflow/releases) has the installers, copied from ProtoFlow's official update server.
- [`latest.json`](latest.json) lists the newest installer for each platform, with its SHA-256, so scripts and agents can find it.
- [`AGENTS.md`](AGENTS.md) and [`llms.txt`](llms.txt) are written for AI agents.

ProtoFlow is free to use under its [terms](https://www.protoflow.ai/terms). See the [privacy policy](https://www.protoflow.ai/privacy) for how your data is handled.
