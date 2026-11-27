# aigate

[![CI](https://github.com/psyb0t/aigate/actions/workflows/pipeline.yml/badge.svg?branch=main)](https://github.com/psyb0t/aigate/actions/workflows/pipeline.yml)
[![version](https://raw.githubusercontent.com/psyb0t/aigate/badges/version.svg)](https://github.com/psyb0t/aigate/releases)
[![license](https://raw.githubusercontent.com/psyb0t/aigate/badges/license.svg)](LICENSE)

Run local models, cloud providers, and MCP tools behind one self-hosted gateway. Aigate is a Docker Compose stack with an OpenAI-compatible API at `http://localhost:4000/v1`.

## Contents

- [Quick start](#quick-start)
- [Architecture](#architecture)
- [Documentation](#documentation)
- [Agent integrations](#agent-integrations)
- [Sponsor](#sponsor)
- [License](#license)

## Quick start

Install Docker with Compose and GNU Make.

```bash
git clone https://github.com/psyb0t/aigate.git
cd aigate
make bootstrap
```

In `.env`, replace the example `AIGATE_TOKEN` and enable a provider. For image generation, set `IMAGIES=1` for CPU or `IMAGIES_CUDA=1` for NVIDIA. See the [setup guide](https://psyb0t.github.io/aigate/setup/) for credentials and GPU requirements.

```bash
make run-bg
curl --fail-with-body http://localhost:4000/health/liveliness
```

Send requests to `http://localhost:4000/v1` using your LiteLLM bearer key. The key defaults to `AIGATE_TOKEN`. Open `http://localhost:4000/ui/` for the LiteLLM admin UI.

## Architecture

```text
Client -> nginx :4000
            |-- /v1/ -> LiteLLM -> cloud providers and local models
            |                       |-- Talkies (speech and transcription)
            |                       `-- Imagies (CPU or CUDA image generation)
            |-- /q/  -> proxq -> LiteLLM (background requests)
            `-- service routes -> optional APIs and MCP tools
```

nginx, LiteLLM, PostgreSQL, Redis and proxq start by default. Enable the providers and tools you need in `.env`. LiteLLM coordinates local model use through Redis-backed hardware locks. Imagies CPU and CUDA share the same cached weights under `.data/imagies`.

## Documentation

| Guide | What it covers |
| --- | --- |
| [Setup](https://psyb0t.github.io/aigate/setup/) | Configure the stack, set resource limits, and upgrade the Imagies integration. |
| [Architecture](https://psyb0t.github.io/aigate/architecture/) | Routing, security, and persistent storage. |
| [Using the gateway](https://psyb0t.github.io/aigate/usage/) | Make requests, generate images, and queue background work. |
| [Providers and models](https://psyb0t.github.io/aigate/providers/) | Enable cloud or local providers and find their model IDs. |
| [Services](https://psyb0t.github.io/aigate/services/) | API, configuration, and examples for each service. |
| [MCP tools](https://psyb0t.github.io/aigate/mcp-tools/) | Available tools and how to call them. |
| [Operations](https://psyb0t.github.io/aigate/operations/) | Logs, common commands, and troubleshooting. |
| [Testing](https://psyb0t.github.io/aigate/testing/) | Run the isolated unit tests or test an enabled service. |

## Agent integrations

The [skill](.agents/skills/aigate) works in any agent that reads `.agents/skills/` (such as [peen](https://github.com/psyb0t/peen)), and
installs natively in the clients below.

### Claude Code

```bash
claude plugin marketplace add psyb0t/agents
claude plugin install aigate@psyb0t
```

Claude Code prompts for the Aigate URL and stores `AIGATE_TOKEN` in your OS keychain if you supply one.

### Codex

```bash
codex plugin marketplace add psyb0t/agents
codex plugin add aigate@psyb0t
```

Installed via the marketplace, the skill invokes as `$aigate:aigate`. Codex also picks
the skill up automatically with no install in any repo containing `.agents/skills/`,
where it invokes as plain `$aigate`.

### OpenClaw

The skill is published to ClawHub on every release:

```bash
openclaw skills install @psyb0t/aigate
```

## Sponsor

[Sponsor on GitHub](https://github.com/sponsors/psyb0t) or [buy me a coffee](https://www.buymeacoffee.com/psyb0t).

## License

[WTFPL](LICENSE)
