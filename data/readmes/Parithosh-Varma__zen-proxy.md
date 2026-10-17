# zen-proxy

**Run Claude Code on OpenCode Zen's free models.** A zero-dependency local proxy that speaks Anthropic's Messages API on the front and OpenAI's Chat Completions on the back — so `claude` never knows it isn't talking to Anthropic.

[![Free models](https://img.shields.io/badge/models-Zen%20free%20tier-2ea44f)](https://opencode.ai/zen)
[![Zero deps](https://img.shields.io/badge/dependencies-none-blue)](#why-zero-dependencies)
[![License MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Node 18+](https://img.shields.io/badge/node-18%2B-brightgreen)](#prerequisites)

```
Claude Code ──POST /v1/messages──► zen-proxy ──POST /chat/completions──► OpenCode Zen
                                   Anthropic ⇄ OpenAI
                                   streaming · tool use · thinking
```

No API key required. No `opencode` install required — just Node.

---

## Why

Claude Code only speaks the Anthropic API. OpenCode Zen only speaks OpenAI Chat Completions. Left alone you pick one: pay for Anthropic tokens, or give up Claude Code's agent loop.

zen-proxy removes the choice. It terminates Anthropic-format requests locally, rewrites them to OpenAI format, forwards to Zen, then rewrites the response back — translating streaming deltas, tool calls, and reasoning blocks in both directions.

## Quick start

```sh
git clone https://github.com/Parithosh-Varma/zen-proxy.git
cd zen-proxy
mkdir -p ~/.zen-proxy && cp proxy.js zen-claude ~/.zen-proxy/ && chmod +x ~/.zen-proxy/zen-claude

# start the proxy (defaults: port 8083, model deepseek-v4-flash-free)
node ~/.zen-proxy/proxy.js &
```

Then run Claude Code through the launcher — it exports the env vars for you, so `~/.claude/settings.json` stays untouched:

```sh
ZEN_MODEL=hy3-free ~/.zen-proxy/zen-claude -p "Reply with exactly: ZEN-OK"
```

Prefer a config file? Add this to `~/.claude/settings.json`:

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "http://127.0.0.1:8083",
    "ANTHROPIC_AUTH_TOKEN": "zen",
    "ANTHROPIC_MODEL": "hy3-free",
    "ANTHROPIC_SMALL_FAST_MODEL": "hy3-free"
  }
}
```

## Prerequisites

- **Claude Code** v2.1.233+ — `claude` on your `$PATH`
- **Node.js** 18+ (tested on Node 20)
- Nothing else. No npm install, no lockfile, no build step.

## Why zero dependencies

`proxy.js` is a single 400-line file using only Node's built-in `http` and the global `fetch`. There is no dependency tree to audit, pin, or break on you — which matters when the thing you're running is a credential-adjacent proxy sitting between your editor and a model endpoint.

## Configuration

| Variable | Default | Description |
| --- | --- | --- |
| `PORT` | `8083` | Listen port, bound to `127.0.0.1` |
| `MODEL` | `deepseek-v4-flash-free` | Zen model id to forward to |
| `ZEN_URL` | `https://opencode.ai/zen/v1` | Upstream endpoint |
| `ZEN_KEY` | `public` | Bearer token — `public` is the free tier |

The `zen-claude` launcher reads `ZEN_PORT`, `ZEN_MODEL`, and `ZEN_CONTEXT` instead, and defaults `ZEN_MODEL` to `hy3-free`.

```sh
PORT=9099 MODEL=nemotron-3-ultra-free node ~/.zen-proxy/proxy.js
```

### Endpoints

| Method | Path | Purpose |
| --- | --- | --- |
| `POST` | `/v1/messages` | Anthropic Messages → translated, forwarded |
| `POST` | `/v1/messages/count_tokens` | Local estimate (`chars / 4`) |
| `GET` | `/v1/models` | Returns the configured model |
| `GET` | `/health` | Liveness check |

## What gets translated

| Anthropic | OpenAI | Notes |
| --- | --- | --- |
| `system` prompt | `system` message | Flattened from content blocks |
| `tool_use` block | `tool_calls` entry | Arguments streamed as `input_json_delta` |
| `tool_result` block | `tool` message | Matched back by `tool_use_id` |
| `thinking` block | `reasoning_content` | Streamed as `thinking_delta` |
| `stop_reason` | `finish_reason` | `tool_use` ⇄ `tool_calls`, `max_tokens` ⇄ `length` |

Streaming is translated incrementally — the proxy rewrites Server-Sent Events as they pass through, so Claude Code's UI updates live rather than after the full completion.

## Rate limiting

Zen's free tier is quota-limited. The proxy stamps every upstream request with a **fresh session id** (`zen-proxy-<pid>-<timestamp>`), so its quota bucket is separate from any other OpenCode sessions you're running — requests here won't starve them and vice versa.

If you hit `429 FreeUsageLimitError`, swap `MODEL` to another free-tier id:

```
hy3-free · deepseek-v4-flash-free · nemotron-3-ultra-free
```

## Security notes

- Binds `127.0.0.1` only — not reachable from the network.
- The bearer token sent upstream is whatever `ZEN_KEY` holds; the default `public` is the unauthenticated free tier.
- Claude Code still runs entirely locally. This proxy changes where completions are billed, not where your code is executed.

## License

[MIT](LICENSE)
