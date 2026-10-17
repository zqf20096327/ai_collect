# AgentOp

AgentOp is an outcome-focused parallel agent desktop application that replaces chat-driven AI workflows with a goal-first model. Define high-level goals, let an AI planner break them into tasks, and watch multiple agents execute in parallel — with a dual-layer interface that keeps humans in control without drowning in detail.

![AgentOp](./docs/images/default.png)

## Download

Download the latest release for your platform: **[github.com/macromania/agentop/releases/latest](https://github.com/macromania/agentop/releases/latest)**

| Platform | Architecture | Artifact |
|----------|-------------|----------|
| macOS | Apple Silicon (M1+) | `.dmg` (arm64) |
| macOS | Intel | `.dmg` (x64) |
| Windows | x64 | `.exe` installer |
| Linux | x64 | `.AppImage` or `.deb` |

> **Note**: Binaries are currently unsigned. macOS users: right-click → Open on first launch. Windows users: click "More info" → "Run anyway" on the SmartScreen prompt.

## Overview

AgentOp replaces chat-driven AI workflows with **task/outcome hierarchies**, **parallel agent execution**, and **attention-based delegation**.

- **Goal-first workflow** — Create goals with natural language prompts; an LLM planner automatically decomposes them into structured task hierarchies with sequence groups for parallel and sequential execution.
- **Parallel agent execution** — Multiple Copilot-powered agent sessions run simultaneously on independent tasks under a single goal.
- **Dual-layer visualization** — A clean tree view for tracking goals and tasks at a glance, plus an expandable canvas mind map (DAG) that renders every agent thought, tool call, decision, and output as spatial nodes.
- **Attention system** — Three delegation modes: supervised (human reviews before execution), delegated (agents run freely), and sensitive (always requires approval for destructive operations like file deletion or force push).

### Attention system

AgentOp uses an attention-based delegation system:

| Type | Behavior |
|------|----------|
| `supervised` | Agent waits for human approval before execution |
| `delegated` | Agent executes freely, logs for review |
| `sensitive` | Always requires approval for destructive operations |

### Agent engine

- LLM-driven planning with structured task decomposition and sequence groups
- Session orchestrator with streaming steps, abort/pause/resume, and retry logic
- Sensitive operation detection via pattern matching + LLM self-classification
- Confidence-based decision points with trade-off analysis and suggested questions
- Task clarification flow — agents can flag tasks as needing human input, with scoped discussion threads that can spawn new tasks
- Goal-level context sharing — clarifications and decisions accumulate and are shared across all tasks to prevent duplicate questions
- Task summarization — LLM-generated summaries for completed tasks
- Stuck task recovery — automatic detection and recovery of orphaned/interrupted sessions on startup

### Skills

- Reusable SKILL.md instruction files with YAML frontmatter validation
- Workspace scanning (.github/skills/, .agents/skills/, .claude/skills/)
- GitHub repository browser for discovering and downloading community skills from `anthropics/skills`, `github/awesome-copilot` and `openai/skills`

### MCP

- Configure Model Context Protocol servers (stdio/HTTP/SSE) per goal
- Built-in catalog of 12 servers (Postgres, SQLite, Filesystem, GitHub, Slack, and more)
- Export configuration to mcp.json format

## Features

| Feature | Description |
|---------|-------------|
| [Dual-Layer Interface](docs/features/dual-layer-interface.md) | Tree view for goals/tasks + canvas mind map for agent work |
| [Goal Creation](docs/features/goal-creation.md) | Natural language goal input with delegation level selection |
| [Goal Planning](docs/features/goal-planning.md) | AI-driven task decomposition from a single prompt |
| [Goal Summary](docs/features/goal-summary.md) | LLM-generated overview of a goal's plan and progress |
| [Context Sharing](docs/features/context-sharing.md) | Goal-level context shared across all tasks |
| [Task Details](docs/features/task-details.md) | Live agent session view with thinking, tool calls, and outputs |
| [Task Clarification Context](docs/features/task-clarification-context.md) | How shared context flows into task execution |
| [Task Clarification](docs/features/task-clarification.md) | Agents flag tasks needing human input with discussion threads |
| [Task Summary](docs/features/task-summary.md) | LLM-generated summary for completed tasks |

## What's Next

- Additional AI provider support (Claude, OpenAI, Anthropic)
- Git agent for automatic change tracking and commits
- Docker workspace containers for sandboxed execution
- Cross-agent observation (agents check what others have done to avoid duplicate work)
- WYSIWYG editor for goal creation with AGENTS.md context
- Quality and refactoring improvements (see ai-docs/quality-plan.md)

## About

A small, personal open‑source desktop app built as a learning and experimentation project.
This project is something I’m hacking on in my own time to explore ideas around local developer experiences and AI‑powered tooling. It’s intentionally lightweight, opinionated, and experimental.
This is not a Microsoft project. It’s not affiliated with, endorsed by, or supported by Microsoft. The code does not include any Microsoft confidential information, proprietary source code, or internal assets. Any references to Microsoft products or SDKs are purely descriptive and based on publicly available documentation.
The project is shared openly for learning, feedback, and discussion.

### Why I built this

I wanted a small, concrete way to explore how modern AI SDKs feel in practice when you’re building a real tool—not a demo, not a slide, just something you can run locally and iterate on. This started as a curiosity-driven experiment around developer experience, orchestration, and where things feel smooth versus awkward when you move from APIs to an actual desktop app. I’m sharing it because I find I learn fastest when ideas are visible, imperfect, and open to feedback.

### Status

- **Early-stage and experimental.**
- **Expect rough edges, changing APIs, and breaking changes.**
- **This is very much a “thinking out loud in code” kind of project.**

## Getting started for development

### Prerequisites

- [Bun](https://bun.sh) >= 1.1.0
- [GitHub Copilot CLI](https://github.com/features/copilot/cli)

### Installation

```bash
# Install dependencies
bun install

# Run development mode
bun run dev

# Build for production
bun run build

# Package for distribution
bun run --filter @agentop/electron package
```

## Project structure

```
agentop/
├── apps/
│   └── electron/          # Electron desktop app
│       ├── src/
│       │   ├── main/      # Main process
│       │   ├── preload/   # Context bridge
│       │   └── renderer/  # React UI
│       └── package.json
├── packages/
│   ├── core/              # Shared types
│   └── shared/            # Business logic
│       ├── agent/         # Agent operations
│       ├── database/      # SQLite + Drizzle
│       └── providers/     # AI provider abstraction
├── docs/
└── package.json
```

## Tech stack

| Layer | Technology |
|-------|------------|
| Runtime | Bun |
| Desktop | Electron |
| UI Framework | React |
| Components | shadcn/ui |
| Styling | Tailwind v4 |
| Animations | Framer Motion |
| Canvas | @use-gesture/react + @react-spring/web |
| State | Jotai |
| Database | better-sqlite3 + Drizzle ORM |
| AI SDK | @github/copilot-sdk |

### Technology

The project uses publicly available SDKs and APIs (including Copilot-related tooling) based on their published documentation. Mentions of specific products or trademarks are for compatibility and clarity only.

## License

This project is licensed under the MIT License.
See the LICENSE file for details.
