# AgentForge Desktop

**English** | [简体中文](README.zh-CN.md)

A local-first AI agent workbench for macOS and Windows. AgentForge Desktop pairs a Vue 2 + Vite + Electron shell with an embedded Spring Boot backend and a bundled JRE 8 runtime, so users can install one app, start chatting with an agent, and never touch a terminal or configure a JDK.

![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Windows-4f46e5)
![Electron](https://img.shields.io/badge/Electron-31-47848f)
![Vue](https://img.shields.io/badge/Vue-2.7-42b883)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-2.7-6db33f)
![Java](https://img.shields.io/badge/Java-8-e76f00)

## Why AgentForge Desktop

Most agent frameworks assume a server, a database, and a developer on call. AgentForge Desktop takes the opposite route: the whole runtime lives on the user's machine.

- **Zero setup** — Electron launches the backend JAR on a free local port with a one-time token; no JDK, Maven, or database install required at runtime.
- **Local-first by design** — conversations, memories, and configuration stay in `~/.agentforge-desktop`. SQLite replaces MySQL, and the server binds to `127.0.0.1` only.
- **Real agent loop** — streaming reasoning, tool calls, workspace-aware execution, and cancellable runs, not a chat wrapper.
- **One-click delivery** — build scripts assemble the JAR, JRE, and Electron app for macOS arm64/x64 and Windows x64.

## Features

- **Workbench** — session history, pinned/renamed/deleted conversations, workspace groups with one-click new chats, and a detail pane with markdown, highlighted code blocks, and one-click copy.
- **Taskized streaming & reconnect** — submit/stream/stop/resume tasks over SSE with persisted event sequences and `lastEventSeq` resume; historical messages replay from stored events.
- **Local resources & multimodal** — insert local images, files, and folders inline in the composer at the cursor; resources keep their position in sent and replayed messages. Images are routed to vision-capable models, text files are read into context, and the agent can proactively read paths or folders with the `read_resource` tool.
- **Workspace selection** — bind a local project folder per conversation; import folders by pasting a full path (quoted paths, `file://` and `~/` are supported, with clipboard auto-fill), and start a new chat directly from a workspace group header. The selector moves above the composer for existing workspace sessions and stays hidden for non-workspace sessions.
- **Skills** — global and workspace Skill discovery, a lightweight `skill` tool, and a management page for importing folders or ZIP archives.
- **Human-in-the-loop** — built-in `ask_user` questions plus approval prompts for high-risk bash commands such as `rm`; interrupted tool batches resume from the same message. Frozen snapshots are persisted in SQLite (`ai_agent_interrupt_snapshot`) for audit and runtime rebuilds.
- **Permission modes** — switch between default approvals and full access from the composer. The choice is sent as `mode`, mapped to `PermissionMode.DEFAULT` / `BYPASS`, isolated in the runtime cache, and persisted per session.
- **Session context restore** — the composer keeps each session's draft, selected model, workspace, attached resources, and permission mode; reopening a conversation restores the last input state.
- **In-run instructions** — append extra guidance while the agent is running; queued instructions are injected at the next model boundary and deferred ones return to the composer.
- **Model management** — CRUD, connectivity checks, Function Call tests, explicit vision capability, and per-agent model allowlists/defaults.
- **Agent configuration** — model set, default model, memory window, and a read-only preview of the composed built-in system prompt. Saved changes take effect immediately.
- **Dual render modes** — debug and polished modes for inspecting raw reasoning versus reading the final answer.
- **Hot reload** — editing `conf/config.json` or `conf/models.json` by hand is picked up automatically.
- **Versioned SQLite migrations** — checksum-verified incremental SQL applied at startup, with a manual CLI for troubleshooting.
- **CI-friendly scripts** — `doctor` environment checks, layered build/dev/package/verify scripts, and artifact verification for both platforms.

## Architecture

```text
┌──────────────────────────────────────────────────────────────┐
│ Electron main process                                        │
│  · pick a free port / generate a one-time token              │
│  · spawn runtime/jre/bin/java -jar runtime/server/*.jar      │
│  · wait for /api/local/health, then expose IPC to renderer   │
└───────────────────────────────┬──────────────────────────────┘
                                │ IPC
┌───────────────────────────────▼──────────────────────────────┐
│ Renderer (Vue 2 + Vite + Element UI)                         │
│  · workbench, session history, model & agent pages           │
│  · API client attaches baseUrl + desktop token               │
└───────────────────────────────┬──────────────────────────────┘
                                │ HTTP / SSE (127.0.0.1)
┌───────────────────────────────▼──────────────────────────────┐
│ agentforge-desktop-server (Spring Boot 2.7 / Java 8)         │
│  · ChatController / Session / Message / Model / Agent APIs   │
│  · HarnessAgent + LocalRuntime, resource pipeline, SSE       │
│  · DesktopConfigStore + SQLite schema migrator               │
└──────────────────────────────────────────────────────────────┘
```

## Tech Stack

| Layer | Choice |
| --- | --- |
| Desktop shell | Electron 31 |
| Renderer | Vue 2.7, Vue Router 3, Vite 5, Element UI 2.15 |
| Markdown | markdown-it, highlight.js, KaTeX, DOMPurify |
| Backend | Spring Boot 2.7.18, Java 8, MyBatis 2.3 |
| Persistence | SQLite (sqlite-jdbc 3.46.x) |
| Agent runtime | AgentForge `agentforge-agent-core`, `agentforge-harness-agent`, `agentforge-model-registry` |
| Packaging | spring-boot-maven-plugin, bundled JRE 8, electron-builder |

## Repository Layout

```text
agentforge-desktop-server/   Local Spring Boot backend (SSE, SQLite, agent runtime)
agentforge-desktop-ui/       Vue 2 renderer, Electron main process, build/package scripts
docs/                        Design notes, local debugging guides, and packaging docs
```

## Requirements

- Node.js 22+ and npm 10+
- JDK 8 (Zulu 8 or Temurin 8 recommended)
- Maven 3.9+
- macOS (arm64/x64) or Windows x64

The build scripts auto-detect a JDK at `/Library/Java/JavaVirtualMachines/zulu-8.jdk/Contents/Home`. Override it with `AGENTFORGE_DESKTOP_JAVA_HOME`.

The first build installs the AgentForge core artifacts into the local Maven repository. The source tree is expected at `../../AgentForge`; override with `AGENTFORGE_HOME`.

## Getting Started

```bash
# 0. Read-only environment check: Node/npm/JDK 8/Maven/core artifacts/deps/runtime/disk
cd agentforge-desktop-ui
npm install
npm run doctor

# 1. Start the backend (default port 43179)
cd ../agentforge-desktop-server
mvn spring-boot:run

# 2. Start the desktop app against the local backend
cd ../agentforge-desktop-ui
npm run desktop:dev

# 3. Or build the JAR + embedded runtime and start everything at once
npm run desktop:dev:embedded

# 4. Package the app for the current machine
npm run package:current
```

If Electron downloads are slow, use a mirror:

```bash
ELECTRON_MIRROR=https://npmmirror.com/mirrors/electron/ npm install
```

The Vite dev server runs on `127.0.0.1:1420` and proxies `/api` to `127.0.0.1:43179`. Point it elsewhere with `VITE_PROXY_TARGET`.

## Configuration and Data

| Item | Default location |
| --- | --- |
| Agent config | `~/.agentforge-desktop/conf/config.json` |
| Model config | `~/.agentforge-desktop/conf/models.json` |
| SQLite database | `~/.agentforge-desktop/data/agentforge-desktop.db` |
| Logs | `~/.agentforge-desktop/logs/` |
| Workspace | `~/.agentforge-desktop/workspace/` |

Override the data root with `AGENTFORGE_DESKTOP_ROOT_DIR`, or the config file with `AGENTFORGE_DESKTOP_CONFIG`. API keys can be seeded through `AGENTFORGE_DESKTOP_MODEL_API_KEY`.

Existing installations are migrated automatically: a legacy `config.json` is split into `conf/config.json` and `conf/models.json`.

## Packaging

```bash
# Current machine
npm run package:current

# macOS, both architectures
npm run package:mac -- --arch arm64
npm run package:mac -- --arch intel

# Windows x64 (on a Windows build machine)
npm run package:win-x64
```

macOS local packaging reuses `node_modules/electron/dist` instead of downloading Electron again. JRE locations can be overridden in `packaging.config.local.json`:

```json
{
  "jreHomes": {
    "mac-arm64": "/Library/Java/JavaVirtualMachines/zulu-8.jdk/Contents/Home",
    "mac-x64": "/path/to/macos-x64-jre-8/Contents/Home",
    "win-x64": "C:\\Tools\\jre8-win-x64"
  }
}
```

Use `npm run package:win-x64:cross` to build the Windows artifact from macOS, and `scripts/verify/*.mjs` to validate the produced package.

## Database Migrations

```bash
cd agentforge-desktop-server
./bin/upgrade-sqlite.sh            # apply pending scripts
./bin/upgrade-sqlite.sh --dry-run  # list pending scripts only
```

The embedded migrator applies versioned SQL automatically at startup, records each script with a SHA-256 checksum, and aborts startup if an already-applied script has changed.

## Documentation

- [Design and implementation notes](docs/桌面版agent工作台设计实现/README.md)
- [Local resources and multimodal capabilities](docs/桌面版agent工作台设计实现/核心后端服务设计/文件上传与模态识别能力/AgentForge-Desktop本地资源输入与模态识别实现.md)
- [Changelog](CHANGELOG.md)
- [Local development and verification commands](docs/桌面版agent工作台设计实现/快捷命令与联调验证.md)
- [Embedded desktop startup guide](docs/桌面版agent工作台设计实现/整体快捷流程梳理/本地调试/桌面端内置启动-desktop-dev-embedded.md)
- [Packaging for all three targets](docs/桌面版agent工作台设计实现/整体快捷流程梳理/本地调试/快捷一键打包-三端适配实现详解.md)
- [Unified logging](docs/桌面版agent工作台设计实现/整体快捷流程梳理/本地调试/AgentForge-Desktop日志统一管控详解.md)
- [Startup initialization and SQLite migrations](docs/桌面版agent工作台设计实现/整体快捷流程梳理/本地调试/安装后启动初始化与SQLite增量SQL迁移详解.md)
- [Troubleshooting: stale JVM proxy failures](docs/桌面版agent工作台设计实现/异常问题记录/01、代理关闭后Java进程全部模型请求失败：JVM代理启动时固化导致SOCKS连接拒绝.md)
