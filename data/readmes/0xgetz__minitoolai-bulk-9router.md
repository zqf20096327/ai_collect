<div align="center">

<img src="brand/logo.svg" width="120" alt="minitoolai-bulk-9router"/>

# minitoolai-bulk-9router

**Bulk MiniToolAI accounts → session cookies & tokens → 62 free models on one OpenAI-compatible endpoint → wired into 9Router.**

[![Node](https://img.shields.io/badge/node-%E2%89%A518-339933?logo=node.js&logoColor=white)](https://nodejs.org)
[![Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)](package.json)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![9Router](https://img.shields.io/badge/9Router-compatible-6d5efc)](https://9router.com)
[![Models](https://img.shields.io/badge/models-62%20working-success)](#-models-that-work)
[![Platform](https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-lightgrey)](#-requirements)

[Bahasa Indonesia](README.id.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [Español](README.es.md)

</div>

---

<img src="brand/banner.svg" alt="banner"/>

## What it does

MiniToolAI exposes a large catalogue of AI models through ordinary PHP pages. Each
tool has a `select_model` dropdown and a small chat handler that answers with a
server-sent-event stream. This toolkit automates the whole chain:

1. **Creates accounts in bulk** — headless Chromium fills the registration form
   (`#username`, `#password`, optional email). No verification mail is involved.
2. **Harvests the session** — `PHPSESSID`, the Cloudflare `cf_clearance` cookie,
   the page `utoken`, a freshly solved Turnstile token and a Playwright-compatible
   storage state, all written to `data/accounts.json` with `0600` permissions.
3. **Serves the models** — an OpenAI-compatible HTTP server
   (`/v1/models`, `/v1/chat/completions`, streaming and non-streaming) that
   round-robins across the harvested accounts and fails over automatically.
4. **Connects to 9Router** — one command registers the adapter as a provider node,
   so every OpenAI-compatible client behind [9Router](https://9router.com) can use
   `minitoolai/<tool>/<model>` like any other model.

> **Zero dependencies.** Node 18+ ships `fetch`, `AbortSignal` and `TextDecoder`,
> and the CDP transport is a hand-rolled RFC 6455 client. `npm install` has
> literally nothing to download.

---

## Requirements

| Item | Notes |
|---|---|
| **Node.js ≥ 18** | 22 LTS recommended. No `npm install` needed. |
| **Chromium / Chrome** | Auto-detected (`chromium`, `google-chrome`, snap, macOS, Windows). Override with `CHROME_PATH=/path/to/chrome`. |
| **A browser you already own (optional)** | Point `CDP_URL` at any Chrome DevTools endpoint (including a cloud browser) to reuse its IP and clearance. |

On a fresh Debian/Ubuntu VPS:

```bash
sudo apt-get update && sudo apt-get install -y nodejs chromium
```

---

## Quick start

```bash
git clone https://github.com/0xgetz/minitoolai-bulk-9router.git
cd minitoolai-bulk-9router

node src/cli.js harvest --count 3      # 3 accounts + sessions, ~25 s each
node src/cli.js list                   # inspect what was harvested
node src/cli.js chat --model gpt-ai/gpt-5-nano --message "hello"
node src/cli.js serve --port 8790      # OpenAI-compatible endpoint
node src/cli.js connect                # register it inside 9Router
```

Three commands later your 9Router instance lists **62 models** under the
`minitoolai/` prefix.

---

## Commands

| Command | What it does |
|---|---|
| `harvest --count N` | Create N accounts and store their sessions. `--email you@x` pins the mailbox, `--email none` skips it. |
| `import --file cookies.json` | Add a cookie export by hand (Chrome JSON export or `{name: value}` map). |
| `list` | Table of harvested accounts. |
| `models` | Every model verified to answer on a free account. |
| `chat --model tool/model --message "…"` | One-off call. Add `--stream` to print deltas live. |
| `test --all` | Probe all 62 models with a real request and report pass/fail. |
| `serve --port 8790` | Start the OpenAI-compatible adapter. |
| `connect --router URL --password PW` | Register the adapter in 9Router. |
| `export --format env\|curl\|json` | Print the raw credentials for your own integration. |

### Useful flags

```
harvest   --cdp wss://…   --headful   --accounts ./data/accounts.json
serve     --api-key KEY   --strategy round-robin|least-used   --host 0.0.0.0
connect   --router http://127.0.0.1:20128  --password 123456  --prefix minitoolai
test      --tool gpt-ai   --concurrency 4   --json report.json
```

Environment variables: `CDP_URL`, `CHROME_PATH`, `MT_ACCOUNTS`, `MT_API_KEY`,
`ROUTER_URL`, `ROUTER_PASSWORD`.

---

## Wiring into 9Router

```bash
# 1. adapter (keep it running, e.g. systemd/pm2/tmux)
node src/cli.js serve --port 8790 --api-key mt-local-key

# 2. register the provider node
node src/cli.js connect \
  --router http://127.0.0.1:20128 \
  --password 123456 \
  --port 8790 \
  --api-key mt-local-key
```

`connect` performs the two API calls 9Router expects:

```
POST /api/provider-nodes  { type:"openai-compatible", prefix, baseUrl, apiType:"chat" }
POST /api/providers       { provider:<node id>, apiKey, name, defaultModel }
```

Then, from any OpenAI client pointed at 9Router:

```python
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:20128/v1", api_key="sk-…")
for chunk in client.chat.completions.create(
    model="minitoolai/deepseek/deepseek-flash",
    messages=[{"role": "user", "content": "Explain paging in 3 lines"}],
    stream=True,
):
    print(chunk.choices[0].delta.content or "", end="")
```

The adapter tags every model with `supportsStreaming: true`, which matters:
9Router relays non-stream calls to provider nodes with `Accept: text/event-stream`
and appends `data: [DONE]` to JSON bodies. Forcing the SSE path makes both kinds of
client work correctly.

---

## Models that work

Probed against a free account with a real request (October 2026). **62 models
answer**; Pro-only ones return `insufficient_credits`.

| Tool | Models (verified) |
|---|---|
| `gpt-ai` | gpt-6-luna, gpt-6.1-sol, gpt-6-sol, gpt-5.6-luna, gpt-5.6-terra, gpt-4o-mini, gpt-5.4-mini, gpt-5.4-nano, gpt-4.1-mini, gpt-4.1-nano, gpt-5-mini, gpt-5-nano, gpt-3.5-turbo |
| `deepseek` | deepseek-flash, deepseek-ai/DeepSeek-V4-Pro-0813, deepseek-ai/DeepSeek-V4-Flash, deepseek-ai/DeepSeek-V3.2, deepseek-ai/DeepSeek-V3.1, deepseek-ai/DeepSeek-V3 |
| `gemini` | gemini-3-flash-preview, gemini-2.5-flash, gemini-2.5-flash-lite, gemma-4-26b-a4b-it, gemma-4-31b-it |
| `grok` | grok-4.5, grok-4.3, grok-build-0.1 |
| `mistral` | mistral-large-latest, devstral-small-latest, devstral-medium-latest, codestral-latest, magistral-small-latest, ministral-3b-latest, ministral-8b-latest, ministral-14b-latest, pixtral-12b, open-mistral-7b, open-mixtral-8x7b |
| `qwen` | qwen3.6-flash, qwen3.6-35b-a3b, qwen3.5-flash, qwen-plus-2025-12-01, qwen3-coder-flash, qwen-flash, qwen-flash-character, qwen-plus-character |
| `llama` | meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8, meta-llama/Llama-4-Scout-17B-16E-Instruct, meta-llama/Llama-Guard-4-12B, meta-llama/Llama-3.3-70B-Instruct-Turbo, meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo, meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo |
| `zai-glm` | GLM-5.3-Flash, GLM-5.2, GLM-4.5-Flash, GLM-4.5-Air, GLM-4-32B-0414-128K, GLM-4.6V-FlashX |
| `xiaomi-mimo` | mimo-v2.6-flash, mimo-v2.6-pro |
| `bytedance-seed` | seed-2-0-mini-260215, seed-1-6-flash-250715 |

`node src/cli.js models` prints the full canonical model ids.
`node src/cli.js test --all` re-checks them against the live site.

**Requires credits** (Pro tier): gpt-plus, claude-pro, super-grok, qwen-max.
**No data returned** at probe time: claude (free), minimax, nemotron, tencent-hy,
gpt-oss, plus a few individual models.

---

## How it works

```
harvest →  /register/  ──►  /login.php  ──►  tool page  ──►  cookies + utoken + Turnstile
                                                                      │
                                                                      ▼
                                                              data/accounts.json
                                                                      │
serve   →  POST /v1/chat/completions ──► pool ──► POST <page>/<x>.php ──► stream token
                                                      └► GET ?streamtoken= ──► SSE ──► JSON/SSE
```

The single-POST + SSE dance, the three different stream dialects and the Turnstile
gate are documented line by line in [`docs/PROTOCOL.md`](docs/PROTOCOL.md).
Diagrams live in [`STRUCTURE.md`](STRUCTURE.md).

---

## Security notes

- `data/accounts.json` is written with mode `0600` and is gitignored. It contains
  live session cookies — treat it like a password file.
- `serve` binds `0.0.0.0` by default. On a public VPS always pass `--api-key`
  (or set `MT_API_KEY`) and firewall the port, or bind `--host 127.0.0.1`.
- `cf_clearance` is bound to the IP and user-agent that solved it. Harvest and run
  on the same machine when possible.
- Model availability, limits and ToS are controlled by MiniToolAI and can change
  without notice. This project is unaffiliated with MiniToolAI or 9Router.

## License

MIT — see [LICENSE](LICENSE).
