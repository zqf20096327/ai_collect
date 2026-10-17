<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/logo-wordmark.svg">
  <img src="docs/assets/logo-wordmark.svg" alt="Switchboard" width="420">
</picture>

### One endpoint. Every provider. Zero lock-in.

A self-hosted AI gateway that speaks **both the Anthropic and OpenAI wire protocols** on the front — and routes to **any number of upstream providers** on the back.

Streaming · tool calling · vision · automatic failover · circuit breakers · cost tracking · live dashboard

[![CI](https://github.com/Abdelrhman-Official/switchboard/actions/workflows/ci.yml/badge.svg)](https://github.com/Abdelrhman-Official/switchboard/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org)
[![Docker](https://img.shields.io/badge/docker-ready-2496ED.svg)](docker-compose.yml)
[![No telemetry](https://img.shields.io/badge/telemetry-none-brightgreen.svg)](#security)

[Why](#why) · [Quick start](#quick-start) · [Claude Desktop](#connect-claude-desktop--cowork) · [Configuration](#configuration) · [Dashboard](#the-dashboard)

</div>

---

## Why

Every AI provider wants to be your only provider. Tools hardcode endpoints, quotas expire, models get deprecated — and your workflow breaks the moment one vendor has a bad day.

**Switchboard** is a single small Python process that sits between your tools and your providers:

```
                                  ┌──────────────┐
 Claude Desktop / Cowork  ──►     │              │ ──►  Anthropic-native providers
 Claude Code / Cline      ──►     │              │ ──►  OpenAI-compatible providers
 Cursor / Continue        ──►     │  Switchboard │ ──►  OpenRouter, DeepSeek, Groq,
 LibreChat / any UI       ──►     │    (local)   │ ──►  Together, Mistral, vLLM,
 OpenAI & Anthropic SDKs  ──►     │              │ ──►  Ollama, LM Studio, ...
                                  └──────────────┘
                     Anthropic + OpenAI protocols in
        priority / round-robin / weighted / race / lowest-latency out
```

**No accounts. No telemetry. No proxy service.** It runs on your machine; your keys stay in your `.env`.

- **One model name, many providers** — ask for `my-claude`, let the router decide who serves it
- **Provider dies mid-session?** Retries, failover, and circuit breakers keep you working
- **Both protocols, translated live** — Anthropic clients can use OpenAI-only providers, and vice versa, including streaming, tools, and images

## Quick start

Requires Python 3.10+.

```powershell
git clone https://github.com/Abdelrhman-Official/switchboard.git
cd switchboard
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env      # then set GATEWAY_API_KEY to a long random value
py -m app
```

Open `http://127.0.0.1:8787/dashboard` and connect your first provider from the Catalog tab. There is nothing else to configure — `config/providers.yaml` is created for you.

> If you set a `GATEWAY_API_KEY`, the startup log prints a one-click dashboard link that
> already contains a launch token (`/dashboard?token=…`) — click it and you're in, no
> copying keys into browser fields.

The gateway is now on `http://127.0.0.1:8787`:

| Endpoint | Purpose |
|---|---|
| `http://127.0.0.1:8787/dashboard` | Live dashboard |
| `POST /v1/messages` | Anthropic-compatible API |
| `POST /v1/chat/completions` | OpenAI-compatible API |
| `GET /v1/models` | Model list |
| `GET /health` | Health check |

Or with Docker:

```bash
docker compose up --build
```

## Connect Claude Desktop / Cowork

1. Make sure the gateway is running (`py -m app`)
2. Claude Desktop → **Settings → Developer → Configure Third-Party Inference**
3. Fill in:
   - **Connection:** Gateway
   - **Gateway base URL:** `http://127.0.0.1:8787`
   - **Auth scheme:** Bearer
   - **Gateway API key:** the `GATEWAY_API_KEY` from your `.env`
4. Add the model IDs from your `config/providers.yaml` (e.g. `my-claude`)
5. Start chatting — watch it live on the dashboard

## Connect any OpenAI tool

Cursor, Cline, Continue, LibreChat, or the OpenAI SDK — anything that accepts a custom base URL:

```python
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:8787/v1", api_key="your-gateway-key")
stream = client.chat.completions.create(
    model="my-claude",
    messages=[{"role": "user", "content": "hello"}],
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="", flush=True)
```

Tools, images, and streaming all work — translated live between protocols.

## Connect any Anthropic tool

```python
import anthropic

client = anthropic.Anthropic(base_url="http://127.0.0.1:8787", api_key="your-gateway-key")
stream = client.messages.stream(
    model="my-claude",
    max_tokens=1024,
    messages=[{"role": "user", "content": "hello"}],
)
with stream as s:
    for text in s.text_stream:
        print(text, end="", flush=True)
```

Claude Code also works: set `ANTHROPIC_BASE_URL=http://127.0.0.1:8787` and `ANTHROPIC_AUTH_TOKEN=<your-gateway-key>`.

## Features

| Capability | Detail |
|---|---|
| Anthropic-compatible API | `POST /v1/messages`, `POST /v1/messages/count_tokens`, `GET /v1/models` — works with Claude Desktop/Cowork, Claude Code, Anthropic SDKs |
| OpenAI-compatible API | `POST /v1/chat/completions` — works with Cursor, Cline, Continue, LibreChat, OpenAI SDKs |
| SSE streaming | Real-time protocol translation: OpenAI chunks to Anthropic events, and back |
| Tool calling | `tool_use` ↔ function calling — tools, `tool_choice`, conversation history, streaming included |
| Vision | Base64 and URL images, translated between `image` blocks and `image_url` parts |
| Thinking models | Native Anthropic providers pass thinking blocks through untouched |
| 5 routing modes | `priority`, `round_robin`, `weighted`, `race` (first complete response wins), `latency` (adaptive, fastest provider) |
| Reliability | Per-provider retries with exponential backoff, circuit breaker with cooldown + auto-recovery |
| Live dashboard | Requests, success rates, latency, tokens, cost, circuit state, live log |
| Cost tracking | Optional per-model pricing; usage and estimated spend per provider and model |
| Hot reload | Edit `config/providers.yaml` — changes apply on the next request |
| Model aliasing | Clients see `my-claude`; providers receive your upstream model id |
| 50-provider catalog | Pick a provider, paste your key — connection tested, models auto-discovered |
| CORS enabled | Browser-based tools work out of the box |
| Zero bloat | 3 runtime dependencies. No database, no Redis, no signup |

## Configuration

**The easiest way: the dashboard.** Open `http://127.0.0.1:8787/dashboard` → **Catalog** tab → pick from **50 ready-to-use providers**:

- **First-party labs:** OpenAI, Anthropic, Gemini, Grok, Mistral, DeepSeek, Qwen, GLM (Zhipu/Z.ai), Kimi, Doubao/Seed, ERNIE, Hunyuan, MiniMax, Yi, NVIDIA, Cohere, AI21, Perplexity
- **Inference providers:** OpenRouter, Together, Fireworks, Groq, Cerebras, SambaNova, Hugging Face, DeepInfra, Nebius, Novita, Hyperbolic, Featherless, Baseten, Chutes, Vercel AI Gateway, Replicate, Cloudflare Workers AI, and more
- **Local runtimes:** Ollama, vLLM, LM Studio, llama.cpp, Jan, LocalAI, LiteLLM proxy

Paste your API key and Switchboard **tests the connection and loads the provider's live model list automatically** — check the models you want to expose and connect. No file editing, no restart. Local runtimes are detected the moment you open them (no key needed).

Prefer files? Everything lives in `config/providers.yaml` (created on first use; changes hot-reload — no restart). Providers added via the dashboard are written there too, so you can mix both approaches:

```yaml
routing:
  mode: priority              # priority | round_robin | weighted | race | latency
  retries: 1                  # per-provider retries before failing over
  retry_backoff_seconds: 0.5  # exponential: 0.5s, 1s, 2s, ...
  failure_threshold: 3        # consecutive failures before circuit opens
  cooldown_seconds: 30        # how long an open circuit stays open

pricing:                      # optional: $ per million tokens, by exposed model id
  my-claude:
    input_per_mtok: 3.0
    output_per_mtok: 15.0

providers:
  - id: openrouter
    type: openai                       # openai | anthropic
    base_url: https://openrouter.ai/api/v1
    api_key_env: OPENROUTER_API_KEY    # env var holding the key
    priority: 10                       # lower wins in priority mode
    weight: 3                          # relative weight in weighted mode
    models:
      - id: my-claude                  # what clients ask for
        upstream_model: anthropic/claude-sonnet-4.5   # what the provider receives

  - id: backup
    type: anthropic
    base_url: https://api.anthropic.com
    api_key_env: BACKUP_API_KEY
    priority: 20
    models:
      - id: my-claude                  # same id on two providers = free failover
        upstream_model: claude-sonnet-4-5
```

Keys go in `.env`:

```
GATEWAY_API_KEY=some-long-random-string
OPENROUTER_API_KEY=sk-or-...
BACKUP_API_KEY=sk-ant-...
```

### Routing modes

| Mode | Behavior |
|---|---|
| `priority` | Try providers in order of `priority` (lower first), fail over on error |
| `round_robin` | Rotate across providers request by request |
| `weighted` | Pick randomly, weighted by `weight`; others remain as fallback |
| `race` | Fire at all providers concurrently; first complete response wins (non-streaming) |
| `latency` | Adaptive: route to the provider with the best observed average latency |

## The dashboard

Open `http://127.0.0.1:8787/dashboard` (the startup log prints a one-click link):

- **Catalog** — 50 ready-to-use providers; paste an API key and the connection is tested and the live model list loads automatically; check what you want to expose and connect. Local runtimes (Ollama, vLLM, LM Studio...) are probed automatically, no key needed
- **Providers** — enable/disable with a toggle, edit priority and weight, test connections with live latency, update or remove anything
- **Settings** — every routing and reliability knob in one place: pick the routing mode from five explained cards, tune retries, backoff, circuit-breaker threshold/cooldown and timeouts, and set per-model pricing for cost tracking. Changes apply on the next request, no restart
- **Overview** — requests, success rate, tokens, cost, per-provider health with circuit-breaker state, requests-per-minute chart
- **Logs** — live request log with errors and latencies
- No build step, no CDN — works offline, served by the gateway itself

The same data is exposed for scripted monitoring:

```
GET  /admin/catalog                  # the 50-provider catalog
GET  /admin/providers                # configured providers (CRUD)
POST /admin/providers                # add a provider (from catalog or custom)
POST /admin/probe                    # test a key + discover live models (any provider)
PATCH /admin/providers/{id}          # update (enable/disable, models, key, priority, weight)
DELETE /admin/providers/{id}         # remove
POST /admin/providers/{id}/test      # live request round-trip with latency
GET  /admin/stats                    # totals, per-provider, per-model metrics
GET  /admin/logs                     # recent request log
POST /admin/providers/{id}/reset     # close a tripped circuit breaker
GET  /admin/settings                 # routing mode, reliability, pricing
PATCH /admin/settings                # update any setting (validated, applies instantly)
POST /admin/session                  # trade the gateway key for a dashboard session cookie
DELETE /admin/session                # end the dashboard session
```

## Security

- Binds to `127.0.0.1` by default — do not expose it directly to the internet
- **Set `GATEWAY_API_KEY`.** With it unset, the gateway accepts unauthenticated requests (convenient for a single-user machine, dangerous anywhere else). Switchboard logs a warning on startup and shows "auth disabled" in the dashboard footer when this is the case
- Once set, every endpoint except `/health`, `/docs` and `/dashboard` requires `Authorization: Bearer <GATEWAY_API_KEY>` (or `x-api-key`)
- The dashboard authenticates with a `HttpOnly`, `SameSite=Strict` session cookie obtained either from the launch link printed at startup or from the unlock form. The gateway key is never stored in the browser
- Browser access is restricted to `localhost` origins so a random website you visit cannot reach your gateway; SDKs, CLIs and editors are unaffected
- Provider keys live in `.env` (gitignored) and are never returned by the API, shown in the dashboard, or written to logs
- If you must expose the gateway remotely, put it behind HTTPS and keep the API key enabled

## Development

```powershell
pip install -r requirements.txt -r requirements-dev.txt
pytest
```

The suite (90+ tests) covers protocol translation, streaming converters in both directions, routing modes, retries and circuit breakers, provider CRUD, config edge cases, and the full API surface — all against mocked upstreams, no keys needed.

```
app/
  main.py        FastAPI app: endpoints, auth, SSE, admin API, dashboard
  router.py      Routing, failover, retries, circuit breaker, streaming
  transform.py   Anthropic <-> OpenAI request/response translation (tools, vision)
  stream.py      SSE event/chunk converters in both directions
  catalog.py     The 50 ready-to-use providers
  store.py       Provider CRUD, atomic config writes, .env key management
  metrics.py     Usage, cost, and request-log tracking
  config.py      Config loading, normalization, defaults
  static/        The dashboard (single self-contained HTML file)
tests/           pytest suite
```

## Roadmap

- [ ] Prometheus `/metrics` export
- [ ] Per-model routing overrides
- [ ] Response caching for identical requests
- [ ] Budget limits and alerts
- [ ] Provider key rotation helpers

Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

## References

- Claude Desktop third-party inference / gateway setup: https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/claude-desktop/
- Anthropic Messages API: https://docs.anthropic.com/en/api/messages
- OpenAI Chat Completions API: https://platform.openai.com/docs/api-reference/chat

Independent project — not affiliated with Anthropic or OpenAI.

## License

[MIT](LICENSE)
