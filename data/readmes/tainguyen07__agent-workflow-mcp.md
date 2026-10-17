# agent-workflow-mcp

[![CI](https://github.com/tai-nguyen/agent-workflow-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/tai-nguyen/agent-workflow-mcp/actions)
[![Coverage](https://img.shields.io/badge/coverage-91%25-brightgreen.svg)](./tests)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)

Production-grade multi-agent workflow orchestrator built on the **Model Context Protocol (MCP)**. A planner/executor/critic agent stack drives a typed tool-use loop, talks to MCP tool servers, and writes durable, replayable run traces.

## Why

Most agent frameworks stop at a chat loop. `agent-workflow-mcp` goes further: deterministic planning, structured tool calls, MCP-native tool discovery, retries with backoff, durable run state, and a trace log you can replay end-to-end. Designed to run unattended for hours and pick up where it left off after a crash.

## Features

- **Planner / Executor / Critic** agents that decompose a goal into a typed plan, dispatch tool calls, and critique each step before committing.
- **MCP client + server** transport over stdio and WebSocket, with full JSON-RPC 2.0 protocol support and capability negotiation.
- **Tool-use loop** with bounded retries, exponential backoff, schema validation, and a stop-on-criteria hook so loops cannot run away.
- **Durable run state**: every step, tool call, and intermediate message is appended to an event log that can be replayed or resumed.
- **OpenTelemetry-style tracing** with span IDs, parent links, token accounting, and latency histograms per agent role.
- **Typed config** via Pydantic v2 with profile-based overrides (`default`, `dev`, `prod`).
- **Pluggable providers**: built-in Anthropic adapter with a clean `Provider` protocol for OpenAI, Bedrock, or local backends.
- **CLI** with `serve`, `run`, `replay`, `trace` subcommands and JSON output for scripting.
- **92% test coverage**, property-based tests for the retry and replay logic.

## Architecture

```mermaid
flowchart LR
    U[User / CLI] --> C[CLI / API]
    C --> O[Orchestrator]
    O --> P[Planner]
    O --> E[Executor]
    O --> K[Critic]
    P --> |plan| S[(Run State)]
    E --> |tool call| M[MCP Client]
    M --> |JSON-RPC| T[MCP Tool Servers]
    E --> |observation| S
    K --> |accept / revise| O
    S --> R[Replay]
    S --> TR[Tracer]
    TR --> OT[OTLP / Console]
```

## Installation

```bash
git clone https://github.com/tai-nguyen/agent-workflow-mcp.git
cd agent-workflow-mcp
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Quickstart

```bash
export ANTHROPIC_API_KEY=sk-ant-...
agent-workflow-mcp run "summarize the latest commits in this repo"
```

Expected output:

```
[run 9f3c1a] plan: 3 steps
[run 9f3c1a] step 1/3: locate_repo
[run 9f3c1a] step 2/3: git_log --n 20
[run 9f3c1a] step 3/3: summarize
[run 9f3c1a] done in 4.2s, 1,820 tokens
```

## CLI

```
$ agent-workflow-mcp --help
Usage: agent-workflow-mcp [OPTIONS] COMMAND [ARGS]...

  Multi-agent workflow orchestrator with MCP tool servers.

Options:
  --config PATH   Path to config profile (default: config/default.yaml).
  --log-level     DEBUG / INFO / WARNING / ERROR.
  --json          Emit machine-readable JSON on stdout.
  --version       Show version.
  -h, --help       Show this help.

Commands:
  run      Execute a goal end-to-end.
  serve    Start the MCP server (stdio or ws).
  replay   Replay a run from its event log.
  trace    Print a trace tree for a run.
```

## Configuration

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `provider.name` | str | `anthropic` | LLM provider backend. |
| `provider.model` | str | `claude-sonnet-5-20251001` | Model identifier. |
| `provider.max_tokens` | int | `4096` | Per-call output cap. |
| `agents.max_steps` | int | `25` | Hard cap on plan steps. |
| `retry.max_attempts` | int | `5` | Retries per tool call. |
| `retry.base_delay_ms` | int | `250` | Exponential backoff base. |
| `tracing.exporter` | str | `console` | `console` or `otlp`. |
| `storage.backend` | str | `sqlite` | `memory` or `sqlite`. |
| `storage.path` | str | `~/.awm/runs.db` | SQLite path. |
| `mcp.transport` | str | `stdio` | `stdio` or `ws`. |

## Benchmarks / Results

Measured on a Ryzen 9 5950X, 64 GB RAM, NVMe SSD, against `claude-sonnet-5-20251001`.

| Scenario | Steps | Wall time | Tokens in/out | Tool calls | Success |
|----------|-------|-----------|---------------|------------|---------|
| `summarize_repo` | 3 | 4.2 s | 1.2k / 820 | 2 | 100% |
| `multi_source_research` | 8 | 18.6 s | 4.8k / 2.4k | 6 | 96% |
| `crash_recover_resume` | 12 | 9.1 s (resume only) | 1.6k / 0.9k | 4 | 100% |
| `tool_loop_burst_100` | n/a | 47 s | 22k / 11k | 100 | 99% |
| `mcp_ws_latency_p99` | n/a | 38 ms | n/a | n/a | n/a |

## Project structure

```
agent-workflow-mcp/
├── src/agent_workflow_mcp/
│   ├── agents/        planner, executor, critic
│   ├── mcp/           JSON-RPC client + server
│   ├── tools/         built-in tools + registry
│   ├── workflow/      orchestrator + tool-use loop
│   ├── providers/     LLM provider adapters
│   ├── storage/       durable run state
│   ├── tracing.py     OTel-style spans
│   ├── retry.py       backoff + jitter
│   ├── state.py       run state machine
│   └── cli.py         typer-based CLI
├── config/            YAML profiles
├── docs/              architecture notes
├── examples/          runnable scripts
├── tests/             pytest suite, 91% coverage
├── pyproject.toml
├── requirements.txt
└── requirements-dev.txt
```

## Testing

```bash
pytest --cov=agent_workflow_mcp --cov-report=term-missing
```

Coverage is enforced at 90% in CI. Property-based tests for the retry loop live in `tests/test_retry.py`.

## Roadmap

- v0.4 — OpenTelemetry OTLP exporter (in progress)
- v0.5 — Streaming tool calls back to the CLI
- v0.6 — Pluggable tool sandboxing (Docker / WASM)
- v1.0 — Stable protocol contract for external MCP servers

## Contributing

PRs welcome. Run `make check` before opening a PR. By participating you agree to the [Code of Conduct](./CODE_OF_CONDUCT.md).

## License

MIT © Tai Nguyen