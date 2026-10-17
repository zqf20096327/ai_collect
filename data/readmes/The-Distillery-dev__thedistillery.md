# The Distillery

Cut your input tokens before they reach the model.

The Distillery is a local token-optimization proxy for AI coding tools. It sits between your coding agent and the model API, removes redundant input context, and reports the overall input reduction across your sessions. It is built for developers who want lower model bills without prompt rewriting, workflow changes, or sending code to The Distillery's hosted service for optimization.

[![npm](https://img.shields.io/npm/v/thedistillery?color=f5a623)](https://www.npmjs.com/package/thedistillery)
[![license](https://img.shields.io/badge/license-Elastic--2.0-f5a623)](LICENSE)
[![node](https://img.shields.io/node/v/thedistillery?color=f5a623)](https://nodejs.org)

## Install

```bash
npm install -g thedistillery
```

Requires Node.js `>=20.9.0 <25`.

## Quick Start

```bash
# Log in once
thedistillery auth login

# Start the local proxy
thedistillery start

# Use Claude Code normally, then inspect savings
thedistillery stats
```

`thedistillery start` binds to `127.0.0.1:3080` by default and automatically configures Claude Code routing. For other clients, point the tool at the local Anthropic or OpenAI-compatible endpoint shown below.

## What It Does

The Distillery optimizes request input before it reaches the upstream model API:

1. **Deduplication** - removes identical tool outputs already seen in the session.
2. **Tool output distillation** - trims oversized shell, search, diff, and file outputs while preserving useful head/tail context.
3. **Retention** - keeps the most useful session context when history grows too large.
4. **Prompt-cache placement** - on paid plans, places cache breakpoints automatically where supported.

The displayed reduction is an input-token metric. Output tokens are streamed back unchanged.

## Supported Clients

The Distillery works with Claude Code automatically and with any client that supports a custom Anthropic base URL or OpenAI-compatible base URL.

| Client | Configuration | OpenAI adapter required |
|---|---|---|
| Claude Code | Auto-configured by `thedistillery start` | No |
| Cline | `cline.anthropicBaseUrl` in VS Code settings | No |
| Goose | `ANTHROPIC_HOST=http://localhost:3080` | No |
| Zed | `language_models.anthropic.api_url` in settings | No |
| Aider | `--openai-api-base http://localhost:3080/v1` + `--model openai/claude-sonnet-4-5` | Yes |
| Codex CLI | `OPENAI_BASE_URL=http://localhost:3080/openai/v1` with API-key auth | Yes |

Full client guides live at [thedistillery.dev/clients](https://thedistillery.dev/clients). Codex CLI must use API-key auth; ChatGPT login uses a websocket backend and bypasses `OPENAI_BASE_URL`.

Using AWS Bedrock through Bedrock-Mantle? See [Bedrock setup](https://thedistillery.dev/docs/bedrock-setup).

## Configuration

Create `.distilleryrc.json` in your project directory, or any parent directory, to set a project-level preset:

```json
{ "preset": "smart" }
```

| Preset | Use when | Behavior |
|---|---|---|
| `light` | You want the safest baseline | Deduplication only |
| `smart` | Most coding sessions | Deduplication, tool-output distillation, retention |
| `deep` | Long sessions with large outputs | More aggressive distillation and retention |

Legacy preset names still work: `conservative` maps to `light`, `balanced` maps to `smart`, and `aggressive` maps to `deep`.

Disable compression for a project:

```json
{ "preset": "smart", "compression": false }
```

Environment variables:

| Variable | Description |
|---|---|
| `DISTILLERY_PORT` | Proxy port, default `3080` |
| `DISTILLERY_BYPASS` | Set to `1` for pass-through mode |

## CLI

```bash
thedistillery start              # Start the local proxy
thedistillery start --port 4000  # Use a different port
thedistillery stop               # Stop the proxy
thedistillery stats              # Show cumulative token and cost savings
thedistillery preset smart       # Switch global preset
thedistillery config show        # Show resolved config
thedistillery sessions --detail  # Show recent sessions, Pro only
thedistillery export --format csv --output sessions.csv
thedistillery billing status
thedistillery billing breakdown --month 2026-07
thedistillery billing manage
thedistillery uninstall --dry-run
```

For one-off commands, run a child process with an embedded proxy:

```bash
thedistillery run claude --watch
```

## Data And Privacy

Optimization runs locally on your machine. The hosted service receives usage metadata needed for account, billing, dashboard, alerts, and attribution features: token counts, cost deltas, model/session metadata, and project attribution. It does not receive your code or prompts for optimization.

Local session data is stored in:

```text
~/.distillery/data.db
```

## Self-Hosting And Safety

The proxy is designed for loopback-only use and binds to `127.0.0.1` by default.

Do not bind it to `0.0.0.0` unless you understand the risk. Binding to all interfaces can expose a proxy that forwards requests using your API credentials.

Supported local deployment:

```bash
ANTHROPIC_BASE_URL=http://127.0.0.1:3080
```

## Uninstall

Interactive teardown:

```bash
thedistillery uninstall
```

Preview what would be removed:

```bash
thedistillery uninstall --dry-run
```

Full uninstall guidance: [thedistillery.dev/docs/uninstalling](https://thedistillery.dev/docs/uninstalling).

## Development

```bash
npm install
npm test
npm run build:cli
```

Useful scripts:

```bash
npm run dev                 # Run the CLI from source
npm run benchmark:tokens    # Compare token counts
npm run generate:benchmark  # Regenerate benchmark JSON
npm run build               # Build marketing, dashboard, API, and CLI
```

## Links

- Website: [thedistillery.dev](https://thedistillery.dev)
- App: [app.thedistillery.dev](https://app.thedistillery.dev)
- API: [api.thedistillery.dev](https://api.thedistillery.dev)
- Install guide: [thedistillery.dev/install](https://thedistillery.dev/install)
- Client guides: [thedistillery.dev/clients](https://thedistillery.dev/clients)
- Agent setup guides: [thedistillery.dev/for-agents](https://thedistillery.dev/for-agents)

## License

This project is licensed under the [Elastic License 2.0](https://www.elastic.co/licensing/elastic-license).
