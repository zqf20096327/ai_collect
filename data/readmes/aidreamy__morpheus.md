# Morpheus

**English** | [Português](./docs/readme/README.pt-BR.md) | [Español](./docs/readme/README.es.md) | [Русский](./docs/readme/README.ru.md) | [中文](./docs/readme/README.zh-CN.md) | [日本語](./docs/readme/README.ja.md)

<img width="1910" height="1064" alt="Morpheus terminal interface" src="https://github.com/user-attachments/assets/a80fcff1-068a-44f8-b43d-3e7d7697ecd6" />

Morpheus is a general-purpose coding agent for the terminal. It ships software engineering tools plus *computer tools* that let it interact with graphical applications.

## Why Morpheus?

Morpheus is not meant to replace established coding agents. It is designed to work alongside them as an orchestration layer. Here is why you might want to use it:

- **Multi-agent collaboration**: run different state-of-the-art agents (Claude, Gemini, Codex, Cline, etc.) in the same TUI, creating a shared workspace where they can communicate through a single interface.
- **Experimentation-friendly**: perfect for developers who like trying different agents and combining their strengths instead of committing to a single ecosystem.
- **Manager mode**: keep using your existing agent harnesses while adding orchestration on top, especially useful when working on several smaller tasks at once.
- **Native TUI experience**: configure providers, models and operating modes directly in the interface with minimal manual setup.
- **Modular architecture**: independent, reusable crates for development tools, TUI components, the SDK and memory recall.

## How it differs from other TUI orchestrators

| Feature                                   | Morpheus                                                                                                       | Other TUI orchestrators                                    |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **Multi-agent split panes**               | Run several external agents at once in split panes, each with its own session, model and optional git worktree | Usually single-agent only, or require switching contexts   |
| **Computer tools via accessibility tree** | Reads and drives graphical interfaces through a structured tree, falling back to screenshots only when needed  | Usually screenshot-only, or no GUI interaction             |
| **Rust-based TUI**                        | Built from scratch with Ratatui, inspired by OpenCode's UX                                                     | Often web-based terminals or less optimized interfaces     |
| **Configured in-app**                     | Providers, models and modes configured directly in the TUI                                                     | Often require external config files or CLI flags           |
| **Modular crates**                        | Development tools, TUI widgets, SDK and memory recall as independent, reusable libraries                       | Monolithic architecture with tightly coupled components    |
| **Shared workspace**                      | Multiple agents collaborate through one interface with coordinated task dispatch                               | Agents typically work in isolation                         |

## Highlights

- **Multi-agent mode (`/agents`)**: run external agents (Gemini, Claude, Codex, Cline, and others) alongside the main agent in split panes, all reachable from the same prompt. Each agent keeps its own session, model and optional git worktree, and the main agent coordinates them, dispatching tasks and collecting reports as one team.
- **Computer tools via accessibility tree**: the agent reads and operates graphical interfaces through a structured, compact representation, falling back to screenshots only when needed. Fewer images processed, fewer tokens consumed.
- **TUI built from scratch in Rust** (Ratatui), inspired by OpenCode's UX. Providers, models and operating modes are configured right in the interface with almost zero manual setup.
- **Independent crates**: the development tools live in crates decoupled from the application and can be reused as libraries outside Morpheus.

## Installation

Tested on Linux and Windows. macOS has not been tested yet; if anything fails, [open an issue](https://github.com/aidreamy/morpheus/issues) with as much detail as possible.

**Linux and macOS** (also works on Windows via Git Bash / WSL):

```sh
curl -fsSL https://raw.githubusercontent.com/aidreamy/morpheus/main/download.sh | bash
```

**Windows (PowerShell):**

```powershell
irm https://raw.githubusercontent.com/aidreamy/morpheus/main/download.ps1 | iex
```

> Note: the `curl | bash` command does **not** work in PowerShell or CMD, because Windows has no native `bash`. Use the PowerShell script above instead; Git Bash and WSL also work.

Optional variables: `MORPHEUS_BIN_DIR` (install directory), `MORPHEUS_VERSION` (specific version) and `MORPHEUS_VARIANT` (`slim`, the default, or `slim-embed`, with local RAG via fastembed). `slim-embed` builds are currently published for Linux x64 and Windows x64 only; macOS receives `slim`. On PowerShell, set them as `$env:MORPHEUS_VERSION = "v0.1.0"` before running the command.

After installing, run `morpheus` in your terminal. If the install directory is not on your `PATH`, the script prints the command to add it. If anything goes wrong during installation, open an issue and we will be glad to help.

## Crates

| Crate                                                       | Description                                                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| [`morpheus-tools`](./crates/morpheus-tools/README.md)       | Development tools and computer tools                                                            |
| [`morpheus-tui`](./crates/morpheus-tui/README.md)           | TUI widget library: markdown/diff rendering and layout, the components behind the terminal UI   |
| [`morpheus-sdk`](./crates/morpheus-sdk/README.md)           | Reusable agent primitives: patch engine, tool-call parsing, LSP client and AST intelligence     |
| [`morpheus-recall`](./crates/morpheus-recall/README.md)     | Memory and context recall                                                                       |
| [`morpheus-whatsapp`](./crates/morpheus-whatsapp/README.md) | WhatsApp Web (multi-device) integration: pairing, normalized events and typed sends             |
| [`morpheus-onnx`](./crates/morpheus-onnx/README.md)         | ONNX decision engine (behind the `onnx` feature)                                                |

## Roadmap

- **Laya/ONNX decision engine**: optional `onnx` feature backed by the `morpheus-onnx` crate; see the [crate guide](./docs/onnx/onnx.md).
- **Graph-based harness orchestration**: a new session mode for coordinating multiple harnesses.

## License

GPL-3.0. See [LICENSE](./LICENSE).
