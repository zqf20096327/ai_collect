# ACP Client — Multi-Platform AI Agent Hub

<p align="center">
  <strong>One protocol. Three platforms. Eleven AI agents.</strong>
  <br />
  Connect any ACP-compatible AI coding agent from VS Code, terminal, or mobile.
</p>

<p align="center">
  <a href="https://marketplace.visualstudio.com/items?itemName=formulahendry.acp-client"><img src="https://img.shields.io/badge/VS%20Code-Marketplace-blue?logo=visualstudiocode" alt="VS Code Marketplace" /></a>
  <a href="https://www.npmjs.com/package/@acp-mobile/cli"><img src="https://img.shields.io/npm/v/@acp-mobile/cli?label=CLI" alt="CLI npm" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License" /></a>
  <a href="https://github.com/formulahendry/vscode-acp/actions"><img src="https://img.shields.io/github/actions/workflow/status/formulahendry/vscode-acp/.github/workflows/ci.yml?branch=main" alt="CI Status" /></a>
  <a href="https://agentclientprotocol.com"><img src="https://img.shields.io/badge/ACP-Protocol-purple" alt="ACP Protocol" /></a>
  <br />
  <a href="#vscode-extension">VS Code</a> ·
  <a href="#cli">CLI</a> ·
  <a href="#mobile-app">Mobile</a> ·
  <a href="#project-structure">Structure</a> ·
  <a href="CONTRIBUTING.md">Contributing</a>
</p>

<p align="center">
  <a href="README.zh-CN.md">中文版</a>
</p>

---

**ACP Client** is an open-source, multi-platform implementation of the [Agent Client Protocol (ACP)](https://agentclientprotocol.com/). It acts as an **AI agent hub** that lets you connect, switch, and use ACP-compatible AI coding agents across **VS Code, the terminal, and mobile**.

| Platform | Directory | Description |
|----------|-----------|-------------|
| **VS Code Extension** | `packages/vscode` | Chat panel and session management inside VS Code |
| **CLI** | `packages/cli` | Interactive REPL and one-shot commands in the terminal |
| **Mobile App** | `packages/mobile` | Connect to agents from your phone via a WebSocket relay |

This means you can use **GitHub Copilot, Claude Code, Gemini CLI, Qwen Code, Auggie CLI, Qoder CLI, Codex CLI, OpenCode, OpenClaw, Kiro CLI, and Hermes Agent** — all 11 AI coding agents — from whichever interface suits you, without vendor lock-in.

---

## Contents

- [Why ACP?](#why-acp)
- [Architecture Overview](#architecture-overview)
- [Platforms](#platforms)
  - [VS Code Extension](#vscode-extension)
  - [CLI](#cli)
  - [Mobile App](#mobile-app)
- [Supported Agents](#supported-agents)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Development](#development)
- [Related Projects](#related-projects)
- [Contributing](#contributing)

---

## Why ACP?

The AI coding tool landscape is fragmented. Each agent has its own UI, its own protocol, its own integration point. **ACP** solves this by providing a standard JSON-RPC protocol that any agent can implement and any client can consume.

| Problem | ACP Solution |
|---------|-------------|
| Each agent needs its own UI | One client, many agents |
| Switching agents means switching tools | Switch agents in-place via dropdown |
| Mobile access to desktop agents | Relay server + mobile client |
| Proprietary protocols | Open standard (JSON-RPC 2.0 over stdio/WebSocket) |

ACP is the **USB-C of AI coding agents** — one connector for everything.

---

## Architecture Overview

```
                          ┌──────────────────────────────────────┐
                          │         ACP Client (VS Code)          │
                          │  ┌─────────┐  ┌────────┐  ┌────────┐ │
                          │  │  Chat   │  │Session │  │Status  │ │
                          │  │Webview  │  │  Tree  │  │  Bar   │ │
                          │  └────┬────┘  └────┬───┘  └────┬───┘ │
                          │       │             │            │     │
                          │  ┌────▼─────────────▼────────────▼───┐ │
                          │  │         SessionManager            │ │
                          │  │  ConnectionManager  AgentManager  │ │
                          │  └────┬──────────────────────────────┘ │
                          └───────│─────────────────────────────────┘
                                  │ ACP Protocol (JSON-RPC 2.0 over stdio)
          ┌───────────────────────┼───────────────────────────────────────┐
          │                       │                                       │
          ▼                       ▼                                       ▼
  ┌───────────────┐     ┌──────────────────┐                    ┌───────────────┐
  │   CLI Client  │     │  ACP-compatible   │    WebSocket      │  Mobile App   │
  │  (commander)  │     │  AI Agent Process │◄──────────────────►│  (ReactNative)│
  │  REPL / chat  │     │                   │                    │               │
  └───────┬───────┘     │ Claude Code       │                    │  Chat UI      │
          │             │ Gemini CLI        │                    └───────┬───────┘
          │             │ GitHub Copilot    │                            │
          │             │ Qwen Code         │                    ┌───────▼───────┐
          │             │ Codex CLI         │                    │  Relay Server │
          │             │ ...               │                    │  (WebSocket)  │
          │             └───────────────────┘                    │  + SQLite     │
          │                                                      └───────────────┘
          └────────────────────── Shared Core ───────────────────┘
```

All platforms share a **core library** (`packages/shared/`) containing the ACP client implementation, session management, and type definitions. Each platform provides its own UI layer and platform-specific adapters (file system, terminal, permissions).

---

## Platforms

### VS Code Extension

Adds an ACP panel to VS Code's activity bar with:

- **Chat Webview** — Full Markdown rendering, tool call visualization, thinking process display with streaming animation
- **Session Tree** — Browse historical sessions per agent, click to restore context
- **File System Integration** — Agents can read/write workspace files through VS Code's FS API
- **Terminal Execution** — Real-time command output capture
- **Permission Management** — Ask-on-each or auto-approve policies
- **Protocol Traffic Log** — Debug all JSON-RPC messages in real-time

![ACP Client Screenshot](packages/vscode/resources/screenshot.png)

<details>
<summary><strong>Built-in Commands</strong></summary>

| Command | Description |
|---------|-------------|
| `ACP: Connect to Agent` | Connect to an agent |
| `ACP: Disconnect Agent` | Disconnect current agent |
| `ACP: Restart Agent` | Restart agent process |
| `ACP: New Conversation` | Start fresh conversation |
| `ACP: Send Prompt` | Send message to agent |
| `ACP: Cancel Current Turn` | Cancel ongoing response |
| `ACP: Set Agent Mode` | Switch agent working mode |
| `ACP: Set Agent Model` | Switch agent model |
| `ACP: Attach File to Prompt` | Attach file to message |
| `ACP: Show Protocol Traffic` | View JSON-RPC traffic |
| `ACP: Browse Agent Registry` | Discover new agents |

</details>

### CLI

![ACP Client Screenshot](packages/cli/resources/screenshot.png)

Built with [Commander.js](https://github.com/tj/commander.js):

```bash
# Interactive REPL (default)
acp

# Start REPL with auto-connect
acp repl "Claude Code"

# One-shot chat
acp chat "Claude Code" "Explain this codebase"

# Manage agents
acp agent list

# Browse sessions
acp session list "Claude Code"
acp session show "Claude Code" <session-id>

# Configuration
acp config list
acp config set defaultAgent "Gemini CLI"
```

### Mobile App

React Native application that connects through the WebSocket relay server, enabling agent interaction from your phone. The mobile client is chat-only (no file system or terminal capabilities).

### Relay Server

Node.js WebSocket server (`@acp-mobile/server`) that bridges mobile clients to agent processes:

- WebSocket-to-stdio relay for ACP protocol
- SQLite-backed session persistence
- Pino structured logging

---

## Supported Agents

The project ships with **11 pre-configured agents**, ready to use out of the box:

| Agent | Command | Provider |
|-------|---------|----------|
| **GitHub Copilot** | `npx @github/copilot-language-server@latest --acp` | GitHub (Microsoft) |
| **Claude Code** | `npx @agentclientprotocol/claude-agent-acp@latest` | Anthropic |
| **Gemini CLI** | `npx @google/gemini-cli@latest --experimental-acp` | Google |
| **Qwen Code** | `npx @qwen-code/qwen-code@latest --acp --experimental-skills` | Alibaba |
| **Auggie CLI** | `npx @augmentcode/auggie@latest --acp` | Augment |
| **Qoder CLI** | `npx @qoder-ai/qodercli@latest --acp` | Qoder AI |
| **Codex CLI** | `npx @zed-industries/codex-acp@latest` | OpenAI (via Zed) |
| **OpenCode** | `npx opencode-ai@latest acp` | Open Source |
| **OpenClaw** | `npx openclaw acp` | Open Source |
| **Kiro CLI** | `kiro-cli acp` | Kiro |
| **Hermes Agent** | `hermes acp` | Nous Research |

You can also add **any custom ACP-compatible agent** via settings (VS Code) or config file (CLI).

---

## Quick Start

### VS Code Extension

**Run from source (development)**

```bash
cd packages/vscode
npm install
npm run compile
```

Open the `packages/vscode` folder in VS Code and press `F5` to launch the Extension Development Host.

> **Windows + Claude Code users**: If connection fails with `Internal error`, make sure [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) is installed, or configure the `CLAUDE_CODE_EXECUTABLE` environment variable for Claude Code in VS Code settings (`acp.agents`).

### CLI

**Run from source:**

```bash
cd packages/cli
npm install
npm run build
npm link          # Link the acp command to your global PATH
acp agent list    # Verify installation
```

The CLI config file is at `~/.config/acp/config.json` (Windows: `%USERPROFILE%\.config\acp\config.json`). Run `acp config list` to view the current configuration.

### Relay Server

```bash
cd packages/server
npm install
npm run build
npm start

# Listens on ws://localhost:3100 by default
# Override the port with the ACP_SERVER_PORT environment variable
# Mobile app connects through this relay server
```

---

## Project Structure

This is a **monorepo** managed with npm workspaces. All platform-specific packages live under `packages/`.

```
agenthub/
│
├── packages/
│   ├── vscode/                   # VS Code Extension (package.json, webpack, tsconfig)
│   │   ├── src/                  # Extension source code
│   │   │   ├── extension.ts      # Entry point
│   │   │   ├── config/           # Agent configuration & registry client
│   │   │   ├── core/             # AgentManager, ConnectionManager, SessionManager
│   │   │   ├── handlers/         # FileSystem, Terminal, Permission, SessionUpdate
│   │   │   ├── ui/               # ChatWebview, SessionTree, StatusBar
│   │   │   └── utils/            # Logger, StreamAdapter, Telemetry
│   │   ├── resources/            # Icons, screenshots
│   │   └── .vscode/              # Launch config, settings for extension dev
│   │
│   ├── shared/                   # @acp-mobile/shared — core types, managers, MobileAcpClient
│   ├── cli/                      # @acp-mobile/cli — Commander.js CLI with REPL
│   ├── server/                   # @acp-mobile/server — WebSocket relay server
│   └── mobile/                   # React Native mobile app
│
├── .github/workflows/            # CI + publish pipelines
├── docs/                         # Architecture documentation
│
├── package.json                  # Monorepo root (npm workspaces)
├── tsconfig.base.json            # Shared TypeScript config
├── eslint.config.mjs             # ESLint flat config
└── LICENSE                       # MIT
```

---

## Development

### Prerequisites

- Node.js 18+
- VS Code 1.85+ (for extension development)

### Setup

```bash
git clone https://github.com/formulahendry/vscode-acp.git
cd vscode-acp
npm install
```

### VS Code Extension

```bash
cd packages/vscode
npm run compile          # webpack build
```

Open the `packages/vscode/` folder in VS Code and press `F5` to launch the Extension Development Host for debugging.

### CLI

```bash
cd packages/cli
npm run build
```

### Testing

```bash
# Run VS Code extension tests
cd packages/vscode
npm run lint            # ESLint (zero-warning policy)
npm run pretest         # Compile tests + lint
npm test                # Run VS Code extension tests

# Or from root (runs all workspaces)
npm test
```

### Package VSIX

```bash
cd packages/vscode
npm run package                          # webpack production build
npx @vscode/vsce package                 # package as .vsix
```

---

## Related Projects

- [ACP UI](https://github.com/formulahendry/acp-ui) — Modern cross-platform ACP desktop client (Tauri)
- [WeChat ACP](https://github.com/formulahendry/wechat-acp) — Bridge WeChat messages to ACP agents
- [Agent Client Protocol](https://agentclientprotocol.com/) — The open standard

---

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
