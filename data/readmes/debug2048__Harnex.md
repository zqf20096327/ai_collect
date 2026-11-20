<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/brand/logo-dark.svg" />
    <img src="docs/assets/brand/logo-light.svg" alt="Harnex" width="360" />
  </picture>
</p>

<p align="center">English · <a href="README.zh-CN.md">简体中文</a></p>
<p align="center"><strong>Conversations, image creation, and an agent for your projects.</strong></p>
<p align="center">Work with AI in your browser, on your desktop, in the terminal, or inside VS Code.</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-6860ff" alt="License: Apache 2.0" /></a>
  <a href="#choose-your-client"><img src="https://img.shields.io/badge/Platforms-Windows%20%7C%20macOS%20%7C%20Linux-6860ff" alt="Windows, macOS, Linux" /></a>
  <a href="https://linux.do/"><img src="https://img.shields.io/badge/Community-Linux_DO-6860ff" alt="Linux DO community" /></a>
</p>

<p align="center">
  <a href="https://github.com/debug2048/Harnex/releases/latest">Download</a> ·
  <a href="#see-harnex">Screenshots</a> ·
  <a href="#what-you-can-do">Features</a> ·
  <a href="#quick-start">Quick start</a> ·
  <a href="#documentation">Documentation</a> ·
  <a href="https://github.com/debug2048/Harnex/issues">Issues</a>
</p>

Harnex brings AI conversations and project work into one workspace. Ask questions, create images, or give an Agent a task in your project—from understanding the code to making changes and reviewing the result.

Connect the models you prefer, work in local or remote projects, and follow progress as it happens. You can add instructions, approve actions, and stop a task along the way.

## See Harnex

[![Harnex overview: Agent, settings, image creation, TUI and VS Code](docs/assets/screenshots/overview.png)](docs/assets/screenshots/overview.png?raw=1)

## What you can do

| What you need | How Harnex helps |
| --- | --- |
| **Understand and change a project** | Explore code, investigate problems, edit files and run project tasks. |
| **Carry longer tasks forward** | Make a plan, track progress and adjust the direction as work continues. |
| **Create in conversation** | Ask questions, work with documents and images, and generate or edit images with a configured image service. |
| **Stay in control** | Review file changes, respond to approval requests and restore supported file changes from snapshots. |
| **Choose your models and tools** | Connect model services, add skills and MCP tools, and select what each task can use. |
| **Work locally or remotely** | Use local projects or supported SSH workspaces, and schedule tasks in available environments. |

Available model features depend on your provider and configuration. See the [user guide](docs/en/user-guide.md) for details.

## Quick start

[Download the current release](https://github.com/debug2048/Harnex/releases/latest) and choose the artifact matching your operating system and CPU:

| System | Platform in filename | Desktop installer |
| --- | --- | --- |
| Windows x64 | `win32-x64` | `.exe` |
| macOS Apple Silicon (M series) | `darwin-arm64` | `.dmg` |
| macOS Intel | `darwin-x64` | `.dmg` |
| Linux x64 | `linux-x64` | `.AppImage` |
| Linux ARM64 | `linux-arm64` | `.AppImage` |

For CLI/TUI or VS Code, choose the matching `_offline.zip` (Windows) or `_offline.tar.gz` (macOS/Linux). It includes desktop installers (DEB/RPM/AppImage on Linux), a portable Runtime with Java and ripgrep, and both Runtime/UI VSIX packages. No npm or Marketplace account is needed; project-specific tools such as Git and compilers still come from the project environment.

1. Install and open Harnex. A personal conversation is enough for a first check.
2. In **Settings → Models**, configure the protocol, provider URL, API key when required, and exact model ID, then select that model.
3. Ask “Introduce yourself in one sentence” to check the connection. For a project Agent, open your own project and try “Read this project and describe its structure without modifying files.”

Offline packages do not include a model service or API credits. In v1.0.0, Windows installers are unsigned and macOS packages use ad-hoc signing without notarization; Linux needs system GUI libraries. See [first-run instructions](docs/en/installation.md#first-run) for checksums, OS prompts and troubleshooting, and the [release notes](https://github.com/debug2048/Harnex/releases/tag/v1.0.0) for verified scope.

### Run the Web workbench from source

The simplest source-based start is the Web workbench with Docker. You need Docker with Linux containers and **Docker Compose 2.24+**.

From a checkout of this repository:

```bash
docker compose up -d --build
```

Open **http://localhost:18081**, configure a model in **Settings → Models**, and start a conversation or an Agent task. The first build downloads dependencies.

To use an existing host project, choose another installation method, or configure remote access, follow the [installation guide](docs/en/installation.md).

## Choose your client

| Client | Best for | Get started |
| --- | --- | --- |
| **Web** | Conversations and project work in a browser | [Docker](docs/en/installation.md#docker) |
| **Desktop** | A native application window for everyday work | [Desktop installation](docs/en/installation.md#desktop-and-portable-bundles) |
| **CLI / TUI** | Interactive terminal work and scripted tasks | [Release downloads](https://github.com/debug2048/Harnex/releases/latest) and [portable bundles](docs/en/installation.md#desktop-and-portable-bundles) |
| **VS Code** | Working with your project inside the editor | [VS Code installation](docs/en/installation.md#vs-code) |

Distribution targets include Windows x64, macOS Apple Silicon/Intel, and Linux x64/ARM64. Check the [platform requirements](docs/en/installation.md#platforms) and release notes for availability and signing status.

## Documentation

- [Installation and deployment](docs/en/installation.md): installation methods, source builds, upgrades and backups.
- [User guide](docs/en/user-guide.md): conversations, images, Agent tasks, plans, Goals, tools and SSH.
- [Build from source](docs/en/installation.md#source-builds): prerequisites and build commands.
- [中文文档](README.zh-CN.md#文档): Chinese user manual and deployment guide.

## Feedback

Use the [Issue forms](https://github.com/debug2048/Harnex/issues/new/choose) for bugs and suggestions, with the version, OS, client, reproduction steps and sanitized logs. External feedback is accepted through Issues; PR creation is limited to collaborators. See [contributing](CONTRIBUTING.md). Report vulnerabilities privately following [SECURITY.md](SECURITY.md), without posting exploit details in ordinary Issues.

## License

Harnex's own code is licensed under the [Apache License 2.0](LICENSE). Third-party components retain their own licenses; see [docs/licenses](docs/licenses) and the notices distributed with each component.
