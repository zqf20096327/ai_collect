# Olano

[![CI](https://github.com/olano-ai/olano/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/olano-ai/olano/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/olano-ai/olano?logo=github)](https://github.com/olano-ai/olano/releases)
[![GitHub stars](https://img.shields.io/github/stars/olano-ai/olano?style=flat&logo=github)](https://github.com/olano-ai/olano/stargazers)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue?logo=python&logoColor=white)](pyproject.toml)
[![Docs](https://img.shields.io/badge/docs-docs.olano.ai-blue)](https://docs.olano.ai)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/olano-ai/olano)](https://github.com/olano-ai/olano/commits/main)

Olano is a self-hosted runtime that runs a fleet of AI agents. Each agent has a
configuration file (`agent.json5`), its own workspace on disk, a set of tools and
skills, memory that persists across conversations, a schedule, and the chat
channels where people reach it. One long-running process boots every agent,
keeps the channels connected, runs the scheduler and serves a web dashboard
(Mission Control) and a REST/SSE API; a CLI covers setup, chat and operations.
It is built on LangChain's [Deep Agents](https://github.com/langchain-ai/deepagents)
harness and [LangGraph](https://github.com/langchain-ai/langgraph).

![Mission Control: an agent compares three suppliers, saves a report and hands back the file](docs/user-guide/assets/screenshots/chat.webp)

**What deepagents provides, and what Olano adds.** deepagents is the agent
harness: the agent loop, planning, a filesystem abstraction over pluggable
backends, sub-agent delegation, context summarization, skill loading and
human-in-the-loop interrupts, on top of LangGraph's streaming and
checkpointing. Olano is everything around that harness that turns one agent
into an operated fleet: declarative per-agent configuration, workspaces and
memory, 88 tool integrations with per-agent credentials, 21 messaging
adapters, a scheduler, a Docker shell sandbox with an egress firewall, a
security pipeline, the dashboard and API, MCP and A2A in both directions, and
the server that supervises all of it.

## Features

| Area | What ships |
|---|---|
| **Agents and tools** | One `agent.json5` per agent: model, prompt, tools, subagents, skills, channels, schedule, memory and security settings. 88 toolkit modules (around 900 named tools) covering Google Workspace, Microsoft 365, GitHub, Git, Slack, Notion, Jira, Linear, Asana, Trello, HubSpot, Salesforce, Airtable, Stripe, PayPal, QuickBooks, Shopify, Zapier, Composio, X, LinkedIn, Reddit, YouTube, several market-data and trading venues, crypto wallets, web search, page reading, a headless browser, HTML to PNG/PDF/SVG rendering, SQL, files and more. 14 ready-made toolkit subagents, 21 built-in skills (charts, web research, browser use, design, debugging, planning, code review, and the platform's own self-configuration skills), a document toolchain in the sandbox (LibreOffice, OCR, PDF tools), and starter archetypes with a larger catalog synced from Olano Cloud. |
| **Channels** | 21 platform adapters: Telegram, Discord, Slack, Email (IMAP/SMTP), Signal, Matrix, WhatsApp (bundled Node bridge, plus Twilio and Meta Cloud API variants), Mattermost, Home Assistant, SMS (Twilio), inbound webhooks, DingTalk, Feishu/Lark, WeCom, Weixin, iMessage via BlueBubbles, QQ, DeBox, and an OpenAI-compatible HTTP API. Live progress messages, approvals from chat, per-channel allowlists, and a multi-user mode with per-customer memory. |
| **Memory and learning** | `MEMORY.md` plus daily logs, a markdown notes wiki with backlinks, RAG over workspace documents (Chroma with torch-free embeddings), typed memory and a memory graph, background self-learning that distills transcripts into memory, and Cortex: background reasoning workers (Pulse briefings, ideation, memory gardening, skill authoring) that file their results in an approval queue. |
| **Dashboard** | Mission Control, a React/Vite single-page app served by the runtime: chat, agents, group chats, approvals, scheduler and calendar, memory, knowledge, notes, files, a terminal into the agent's shell, tools, vault, connections, providers, config, logs, activity, insights, issues, revision history, org chart, Cortex, external access and team accounts. Installable as a PWA; desktop and phone layouts. |
| **Security and sandboxing** | Shell commands run in a per-agent Docker sandbox with an egress firewall, or on the host behind an allow-list. Human-in-the-loop approval gates by tool category, trust levels, PII scanning on input and output, prompt-injection input scan and output scrubbing, skill audit, SSRF guard, rate limits and reply policies on external channels, an encrypted credentials vault with per-agent scoping, and automatic revision history of configuration files. |
| **Scheduling and autonomy** | Cron jobs per agent with timezones (APScheduler), `HEARTBEAT.md` polling, an issue tracker shared by agents and humans, outbound webhooks, and autonomy levels with categories that always require approval. |
| **Interoperability** | MCP client (stdio and HTTP, OAuth, connection health loop); MCP server that exposes agents as tools behind a built-in OAuth 2.1 authorization server; A2A client and server on the official `a2a-sdk`; ACP for editor integrations; agent-to-agent messaging inside one deployment. |
| **Model providers** | Bring your own key for Anthropic, OpenAI (API key or ChatGPT/Codex OAuth), Google Gemini, Google Vertex AI, Azure OpenAI, AWS Bedrock, Ollama (local), Groq, Mistral, DeepSeek, xAI, Qwen (DashScope), Moonshot, OpenRouter, Cohere, Fireworks, Together, Hugging Face, NVIDIA NIM and Perplexity. A managed `olano:*` tier exists for deployments connected to Olano Cloud. A deterministic `fake:` model exists for offline tests. |

## Quick start

```bash
curl -fsSL https://raw.githubusercontent.com/olano-ai/olano/main/install.sh | bash
```

That is the Docker install, the recommended one: three containers from the
public images (the runtime, the dashboard and Postgres) in `~/olano`. It checks
for Docker Engine with the Compose plugin (on Linux it offers to install them)
and needs 2 CPUs and 4 GB of RAM. Options go after `bash -s --`:

```bash
curl -fsSL https://raw.githubusercontent.com/olano-ai/olano/main/install.sh | bash -s -- --host olano.example.com   # public https hostname
curl -fsSL https://raw.githubusercontent.com/olano-ai/olano/main/install.sh | bash -s -- --sandbox                  # a Docker shell sandbox per agent
curl -fsSL https://raw.githubusercontent.com/olano-ai/olano/main/install.sh | bash -s -- --source                   # from source instead of Docker
```

Open **http://localhost:3200**. The setup wizard creates your admin account,
asks how your agents' models are paid for (your own provider keys, or an Olano
account key that runs the managed `olano:*` tiers on credits) and introduces
Agent Father, the agent that builds and manages the others. Everything the
install keeps lives in `./data` next to the compose file.
[`deploy/self-host/README.md`](deploy/self-host/README.md) covers updates,
backups and the options.

### From source

Requirements: Python 3.11 or newer (CI runs 3.13) and [uv](https://docs.astral.sh/uv/).
Optional: Node.js (dashboard build, WhatsApp bridge) and Docker (shell sandbox,
Postgres). The `--source` one-liner above clones into `~/olano-src` and does
the same as:

```bash
git clone https://github.com/olano-ai/olano.git
cd olano
./install.sh        # Python, uv, deps, Node, Docker, Chromium, pre-commit; idempotent
                    # (./install.sh --docker from a clone is the Docker install)
# or, with Python and uv already present:
uv sync
```

The installer leaves a project `.venv`; either `source .venv/bin/activate` or
prefix commands with `uv run`.

```bash
export ANTHROPIC_API_KEY=...   # any provider from the table above
olano setup                    # interactive: home directory, provider, first agent
olano doctor                   # health check: dependencies, workspace, vault, model access

olano agents create --name scout --model anthropic:claude-sonnet-4-6
olano --agent scout --message "What can you do?" --stream
olano --agent scout -n "Summarize README.md"   # one-shot, pipe-safe with --quiet

olano serve                    # all agents, channels, scheduler; API on :8765
olano dashboard                # runtime plus the web UI (port 3200 by default)
```

Thread state is checkpointed to Postgres or SQLite: `install.sh` provisions a
Postgres container when Docker is available and falls back to SQLite otherwise.
The repository's own `docker-compose.yml` builds the image from this checkout
(`cp .env.example .env && docker compose up`), which is what you want when
changing the runtime itself.

## Configuration

Agents are JSON5 files (comments and trailing commas allowed). A trimmed example:

```json5
{
  "name": "scout",
  "description": "Research assistant",
  "emoji": "🔎",
  "model": "anthropic:claude-sonnet-4-6",

  "tools": ["safe_shell", "web_search", "page_read"],

  "subagents": [
    {
      "name": "WebAgent",
      "description": "Web research, HTTP, download and screenshot specialist.",
      "system_prompt": "Handle live web research and compare sources.",
      "tools": ["page_read", "page_extract", "http_request", "url_download", "web_search"]
    }
  ],

  "memory": { "markdown": true, "rag": true, "self_learning": true },
  "backend": { "type": "local_shell", "root_dir": "workspace" },
  "security": { "profile": "developer", "trust_level": 3, "hitl_enabled": true, "hitl_shell": true },

  // Bot tokens live in the vault, never in this file.
  "channels": [{ "type": "telegram", "allowed_users": [123456789] }],

  "schedule": [
    {
      "cron": "0 9 * * 1-5",
      "timezone": "America/Costa_Rica",
      "message": "Summarize what changed overnight.",
      "thread_id": "morning-brief"
    }
  ]
}
```

Everything lives under one home directory:

```
~/.olano/                          # new installs; an existing ~/olano/ or ~/.lionclaw/ keeps being used
  config.yaml                      # deployment-wide settings
  organization.yaml                # org chart for agent-to-agent messaging
  agents/<name>/agent.json5        # one agent
  agents/<name>/workspace/         # AGENTS.md, SOUL.md, MEMORY.md, memories/, notes/, skills/ ...
  sessions/  vault/  skills/  catalog/
```

The home is resolved from `--home`, then `OLANO_HOME`, then `LIONCLAW_HOME`,
then `~/.olano` if it exists, then `~/olano` if it exists (an install made
while that visible name was the default), then `~/.lionclaw` if it exists, and
is created at `~/.olano` otherwise. A `~/olano` that is a source checkout
(this repository cloned from your home directory, so it holds `pyproject.toml`
or `.git`) is never the home, so the vault and the agents never land inside a
git work tree. A project-local `agents/` directory is also searched
during development only. Environment variables can be written as `OLANO_*` or
the older `LIONCLAW_*`; both spellings work, and `LIONCLAW_*` wins when both
are set. Two exceptions: `OLANO_HOME` outranks `LIONCLAW_HOME`, and the
variables the deploy scripts write for the compose stack (the image pins, the
home directory name, the pull flag) are not runtime settings and are not
mirrored.

The user guide is published at [docs.olano.ai](https://docs.olano.ai): the
dashboard tab by tab, the full field references for `agent.json5` and
`config.yaml`, feature guides and troubleshooting. Its source is
`docs/user-guide/` in this repository (`uv sync --group docs && uv run mkdocs
serve` previews it), and the same pages are concatenated into
`olano/archetypes/knowledge_user_guide.md`, the copy seeded into every agent
workspace so an agent can answer platform questions from it.

## Architecture

```
agent.json5 -> AgentConfig -> build_agent() -> AgentRunner -> CLI (one-shot)
                                                     |-> runtime server (REST + SSE)
                                                     |-> channel adapters
                                                     |-> scheduler and Cortex workers
                                                     '-> dashboard (over the API)
```

`build_agent()` wires the model, a filesystem or sandbox backend, tools, skills,
middleware and a checkpointer into one deepagents graph; `AgentRunner` streams
a turn as typed events that every surface consumes.

| Package | Role |
|---|---|
| `olano/core` | Agent builder, runner, prompt assembly, checkpointers, MCP setup and health, detached turn execution |
| `olano/config` | `AgentConfig` and the `agent.json5` schema, home resolution, `config.yaml` settings, JSON5 parsing |
| `olano/runtime` | The long-running server: agent boot, FastAPI REST/SSE API, auth, uploads, disk monitor |
| `olano/platforms` | Messaging adapters and the shared progress, delivery and approval machinery |
| `olano/tools` | Toolkit modules, the generated tool-name index, per-agent credential resolution |
| `olano/skills` | Skill discovery, gating and the built-in skills |
| `olano/memory` | Markdown memory, notes store, RAG, typed memory, memory graph, self-learning |
| `olano/scheduler` | APScheduler cron jobs, heartbeat polling, scheduled-job database |
| `olano/security` | HITL policy, trust levels, PII and input/output scanning, shell guard, egress firewall, SSRF guard |
| `olano/dashboard_2.0` | Mission Control (React, Vite, TypeScript) |
| `olano/mcp_server` | Inbound MCP: agents as tools, token store, OAuth 2.1 authorization server |
| `olano/a2a` | A2A client and server, task store |
| `olano/cognition` | Cortex background workers, FAST/DEEP routing, approval guard |
| `olano/catalog` | Cloud catalog sync: models, MCP directory, connectors, skills, archetypes |
| `olano/backends` | The Docker sandbox backend and the interpreter shims every shell lane gets |

Other packages worth knowing: `olano/cli` (Click CLI and the Textual setup
wizard), `olano/vault` (encrypted credentials), `olano/archetypes` (templates,
installer, user guide), `olano/magic_links` (phone-friendly one-time links for
sign-in and secrets), `olano/issues`, `olano/revisions`, `olano/groups` and
`olano/pages`.

## Development

```bash
make dev            # uv sync --group dev, pre-commit install
make check          # ruff lint, format check, mypy
make test           # the full pytest suite, serial
make test-fast      # same suite in parallel (pytest-xdist)
make test-sandbox   # live tests against a real sandbox container (Docker + the sandbox image)
make test-e2e       # Playwright tests for the dashboard (Node + Chromium)
```

Dashboard development runs Vite against a separately started runtime:

```bash
olano serve                                   # API on :8765
cd olano/dashboard_2.0 && npm install && npm run dev   # UI on :3201, proxies /api
npm run build && npm run typecheck && npm run test:unit
```

Where to read next:

- [`CONTRIBUTING.md`](CONTRIBUTING.md): development setup, the checks a change must pass, and the review conventions.
- `CLAUDE.md`: the environment facts and module map maintained for coding agents and humans alike.
- `docs/user-guide/`: the source of [docs.olano.ai](https://docs.olano.ai); `docs/channels/` holds per-channel setup guides and `docs/RELEASING.md` the release procedure.
- `deploy/`: the self-hosted compose stack (`deploy/self-host/`), plus host and all-in-one container deployment scripts.

GitHub Actions: `ci.yml` (lint, format, type check and dependency audit; the
test suite; a package build), `e2e.yml` (browser tests on dashboard changes),
`sandbox-live.yml` (the container suite against the real sandbox image),
`build-images.yml` (`:edge` runtime images from `main` once its checks are
green) and `release.yml` (a `vX.Y.Z` tag, pushed or created by dispatching the
workflow with a version, promotes that commit's images to `:X.Y.Z`, `:X.Y` and
`:latest`, and publishes a GitHub Release).
`docs/RELEASING.md` has the release procedure.

## Status and history

The project started in March 2026 as LionClaw and was renamed Olano in mid
2026. The rename is complete at the product level; the `LIONCLAW_*`
environment variable names, the `~/.lionclaw` and `~/.olano` home directories
of earlier installs and a few internal identifiers remain supported so
existing installs keep working unchanged. Releases are tagged `vX.Y.Z` and
listed on the [releases page](https://github.com/olano-ai/olano/releases); the
deepagents dependency is pinned to an exact release.

## Contributing

Bug reports, ideas and pull requests are welcome. Start with
[CONTRIBUTING.md](CONTRIBUTING.md); everyone taking part agrees to the
[Code of Conduct](CODE_OF_CONDUCT.md).

## Star history

[![Star history chart](https://api.star-history.com/svg?repos=olano-ai/olano&type=Date)](https://star-history.com/#olano-ai/olano&Date)

Daily counts of stars and forks are recorded on the
[`stats` branch](https://github.com/olano-ai/olano/tree/stats) (`history.csv`).

## License, security, acknowledgements

Olano is released under the MIT License ([LICENSE](LICENSE)). Bundled
third-party components keep their own licenses, listed in
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

Security practices and how to report an issue are in
[SECURITY.md](SECURITY.md).

Olano builds on [deepagents](https://github.com/langchain-ai/deepagents) and
[LangGraph](https://github.com/langchain-ai/langgraph) from LangChain. The
messaging adapter package was originally ported from the gateway of
[hermes-agent](https://github.com/NousResearch/hermes-agent) and has been
extended since. The WhatsApp bridge uses
[Baileys](https://github.com/WhiskeySockets/Baileys); the dashboard terminal
uses [xterm.js](https://xtermjs.org/); the charts skill vendors
[Vega-Lite](https://vega.github.io/vega-lite/). Copyright notices and licences
for the third-party code and assets bundled in this repository are listed in
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
