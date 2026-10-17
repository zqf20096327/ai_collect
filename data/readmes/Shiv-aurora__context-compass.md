# Context Compass

[![CI Matrix](https://github.com/Shiv-aurora/context-compass/actions/workflows/ci-matrix.yml/badge.svg)](https://github.com/Shiv-aurora/context-compass/actions/workflows/ci-matrix.yml)
[![Release Gate](https://github.com/Shiv-aurora/context-compass/actions/workflows/release-gate.yml/badge.svg)](https://github.com/Shiv-aurora/context-compass/actions/workflows/release-gate.yml)
[![MCP Server](https://img.shields.io/badge/MCP-Server-0A84FF)](https://modelcontextprotocol.io/)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Only-6E56CF)](https://code.claude.com/)
[![Beta](https://img.shields.io/badge/Status-Beta-F59E0B)](https://github.com/Shiv-aurora/context-compass/discussions)
[![Node >=20](https://img.shields.io/badge/Node-%3E%3D20-339933)](https://nodejs.org/)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-D22128)](https://github.com/Shiv-aurora/context-compass/blob/main/LICENSE)
[![Languages](https://img.shields.io/badge/Languages-10-1F6FEB)](https://github.com/Shiv-aurora/context-compass#supported-languages)

Context Compass is a CLI framework for Claude Code that pre-computes behavioral code relationships from git history so Claude can navigate with less context waste and higher retrieval precision.

## Beta

Context Compass is currently in **beta**.

- Primary target: **Claude Code only**
- APIs, behavior, and output format may change during beta
- We welcome both positive feedback and constructive feedback

## Current Scope

Today, Context Compass is optimized for Claude Code.
Support for other tools (Cursor, Windsurf, Antigravity, Codex) is planned after the Claude Code path is fully hardened.

## The Problem

Claude-style coding workflows can waste context budget on blind sequential file discovery before they reach the truly relevant functions.

![Problem Diagram](docs/images/problem-diagram.png)

## How Context Compass Works

Context Compass parses symbols/calls/imports, learns co-edit coupling from git sessions (PMI), and serves compact context bundles through MCP so Claude starts with high-signal context instead of broad exploration.

![How Context Compass Works](docs/images/how-it-works-diagram.png)

## Mode Tradeoffs

Use retrieval modes to tune token cost vs retrieval quality for your task profile.

![Context Compass Modes](docs/images/modes-comparison-diagram.png)

## Evaluation Snapshot (Flask Held-Out)

| Method | Recall@10 | Delta vs baseline | Tokens | Reduction | X fewer |
|---|---:|---:|---:|---:|---:|
| Claude baseline | 54.3% | — | 28,206 | — | — |
| Economy (maxBundles=2) | 37.9% | -16.4 pts | 5,574 | 80.2% | 5.06x |
| Balanced (maxBundles=5) | 65.5% | +11.2 pts | 11,401 | 59.6% | 2.47x |
| Quality (maxBundles=10) | 86.2% | +31.9 pts | 18,313 | 35.1% | 1.54x |

Reproduce on your repo:

```bash
context-compass eval
context-compass eval --json
```

## Installation

```bash
npm install -g context-compass
```

## Prerequisites

- Node.js `>=20`
- [Claude Code](https://code.claude.com/) installed and available as `claude`
- A git repository (history improves behavioral retrieval quality)

## Quick Start

```bash
cd your-project
context-compass init
claude
```

`init` builds the index and wires MCP + SessionStart integration automatically.

## Privacy

Context Compass stores project-local index data under `.context-compass/`.

Optional environment variables:
- `CONTEXT_COMPASS_DISABLE_GLOBAL_STATS=1` — disable user-level cross-project savings aggregation.
- `CONTEXT_COMPASS_ENABLE_GLOBAL_DOMAINS=1` — opt in to cross-project domain aggregation in global stats (disabled by default).
- `CONTEXT_COMPASS_HOME=/custom/path` — override where user-level Context Compass files are stored (default: `~/.context-compass`).

## Commands

- `context-compass` — Show current project status.
- `context-compass init` — Build/rebuild index and install Claude integration.
- `context-compass serve` — Run MCP server over stdio.
- `context-compass install-mcp` — Create/update project `.mcp.json`.
- `context-compass stats` — Show project + global savings dashboard.
- `context-compass savings` — Alias for `stats`.
- `context-compass eval [--json]` — Evaluate retrieval quality on held-out sessions.
- `context-compass mode [economy|balanced|quality]` — Show/set retrieval mode.
- `context-compass enable-hook` — Enable optional legacy `UserPromptSubmit` fallback.
- `context-compass hook-session-start` — Internal SessionStart hook command.
- `context-compass hook-prompt` — Internal fallback prompt hook command.

## Supported Languages

Current support: Python, TypeScript, JavaScript, Go, Rust, Java, C#, Ruby, PHP, Kotlin.

More language support roadmap details will be published next month.
Need a specific language? Open a request: [Language request issue](https://github.com/Shiv-aurora/context-compass/issues/new/choose).

## Contributing (Start Here)

Want to contribute? Start with [CONTRIBUTING.md](CONTRIBUTING.md).
Please also review [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

Required pre-PR verification:

```bash
npm run ci:verify
```

## Feedback

If you hit a bug or unexpected behavior, please open an issue:
- [Open an issue](https://github.com/Shiv-aurora/context-compass/issues/new/choose)

If Context Compass is working well (or not), please share your results in Discussions under the **Feedback** category:
- [GitHub Discussions](https://github.com/Shiv-aurora/context-compass/discussions)

Helpful details to include:
- `context-compass savings`
- `context-compass eval --json`
- repo size and selected mode (`economy`, `balanced`, `quality`)
- what improved, and what still needs work

## Release Check

```bash
npm run release:check
```

This runs typecheck, security audit (`npm audit --omit=dev`), and npm tarball dry-run.

## Security

See [SECURITY.md](SECURITY.md) for vulnerability reporting.

## License

Apache License 2.0. See [LICENSE](LICENSE).
