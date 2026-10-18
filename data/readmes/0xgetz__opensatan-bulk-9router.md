# OpenSatan → 9Router

<p align="center">
  <img src="brand/logo.svg" width="120" alt="opensatan-bulk-9router">
</p>

[🇬🇧 English](README.md) · [🇮🇩 Indonesia](README.id.md) · [🇨🇳 中文](README.zh.md) · [🇯🇵 日本語](README.ja.md) · [🇪🇸 Español](README.es.md) · [🇩🇪 Deutsch](README.de.md)

<p align="center">
  <a href="https://opensatan.com"><img alt="Upstream" src="https://img.shields.io/badge/upstream-opensatan.com-ff3b30"></a>
  <a href="https://9router.com"><img alt="9Router" src="https://img.shields.io/badge/9router-compatible-000000"></a>
  <img alt="Node" src="https://img.shields.io/badge/node-%3E%3D18-3c873a">
  <img alt="Dependencies" src="https://img.shields.io/badge/dependencies-0-brightgreen">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-blue">
  <img alt="E2E" src="https://img.shields.io/badge/e2e-verified-2ea44f">
  <img alt="Streaming" src="https://img.shields.io/badge/streaming-SSE-8b5cf6">
  <img alt="Platform" src="https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-1f6feb">
</p>

Bulk-provision OpenSatan identities, keep them in a rotating pool behind an
OpenAI-compatible adapter, and wire the pool into **9Router** as a normal provider.

OpenSatan has **no accounts and no login** — every visitor is an anonymous identity made of a
`localStorage` session id, an anonymous device id and two age-gate flags. This toolkit harvests those
identities (optionally from a real, isolated Chromium profile per account), checks each one against
the live chat endpoint, stores the session + cookies + optional credit token, and serves the pool
with round-robin + failover.

## Highlights

- **Bulk creator** — `create --count N` provisions N isolated identities (fresh browser context each, or pure HTTP without a browser).
- **Session capture** — session id, anonymous id, localStorage, sessionStorage and every cookie are stored per account.
- **Health gate** — each account is probed with a strict "reply PROBE_OK" prompt before it enters the pool.
- **Pool adapter** — `/v1/chat/completions` (stream + non-stream), `/v1/models`, `/health`, `/pool`, `/pool/reload`, `/v1/verdict`.
- **9Router connector** — creates the provider node, registers the provider, mints a router key and verifies a real completion.
- **Two personas** — `opensatan/satan` (brutal truth) and `opensatan/genie` (cosmic insight).
- **Zero dependencies** — plain Node 18+, including a hand-rolled CDP/WebSocket client for browser capture.

## Quick start

```bash
git clone <repo> && cd opensatan-bulk-9router

# 1) create 5 identities and verify them
node src/cli.js create --count 5

# 2) start the pool adapter (OpenAI-compatible on :8795)
./launch-adapter.sh

# 3) connect the pool to 9Router
ROUTER_URL=http://127.0.0.1:20128 ROUTER_PASSWORD=123456 node src/connect-9router.js
```

Use it from any client through 9Router:

```bash
curl http://127.0.0.1:20128/v1/chat/completions \
  -H "Authorization: Bearer $ROUTER_KEY" -H 'Content-Type: application/json' \
  -d '{"model":"opensatan/satan","messages":[{"role":"user","content":"hello"}]}'
```

## Browser capture (optional)

Some setups want the identity to come from a real browser session (cookies, user agent, age gate).
Start a local Chromium with remote debugging enabled and let the toolkit drive it over CDP:

```bash
chromium --remote-debugging-port=9222 --user-data-dir="$PWD/.chromium-profile" &

CHROME_DEBUG_PORT=9222 node src/cli.js create --count 3 --browser
# or point at an endpoint directly
OS_WS_URL=ws://127.0.0.1:9222/devtools/browser/<id> node src/cli.js create --count 3 --browser
```

Each account gets its own `Target.createBrowserContext` (isolated cookies/storage), the page is
loaded, the age gate is confirmed, `os-session` / `yxp_anon_id` are read, and the context is disposed.
Only the local Chromium you launched is used.
## Models

| Model id | Persona | Notes |
| --- | --- | --- |
| `opensatan/satan` | Satan — brutal truth, zero filter | default |
| `opensatan/genie` | Genie — wisdom, mysticism, cosmic insight | same backbone, different server prompt |
| `gemma-4-26b-a4b-it-uncensored-abliterix-mlx-int5-affine` | backbone id | accepted as an alias of `opensatan/satan` |

## Configuration

| Variable | Default | Meaning |
| --- | --- | --- |
| `POOL_PORT` / `POOL_HOST` | `8795` / `127.0.0.1` | adapter bind |
| `POOL_API_KEY` | — | require a bearer token on the adapter |
| `POOL_MAX_FAILURES` | `3` | failures before an account is cooled down |
| `POOL_COOLDOWN_MS` | `30000` | cooldown window |
| `OS_STORE` | `data/pool.json` | pool file |
| `OS_BASE_URL` | `https://opensatan.com` | upstream origin |
| `OS_MODEL` | backbone id | model sent upstream |
| `OS_CREDIT_TOKEN` | — | optional paid-lane token |
| `OS_BROWSER` / `OS_WS_URL` | — | enable browser capture / CDP endpoint |
| `ROUTER_URL` / `ROUTER_PASSWORD` | `http://127.0.0.1:20128` / `123456` | 9Router |
| `ROUTER_PREFIX` | `opensatan` | provider prefix |

See [`.env.example`](.env.example).

## CLI

```bash
node src/cli.js create  --count 10 [--concurrency 3] [--persona genie] [--browser] [--connect]
node src/cli.js verify  [--file data/pool.json]
node src/cli.js list
node src/cli.js remove  --id <account-id|all>
node src/cli.js connect
node src/cli.js chat    --prompt "hi" --persona genie
```

## Project layout

See [STRUCTURE.md](STRUCTURE.md) for the full diagram and [docs/PROTOCOL.md](docs/PROTOCOL.md) for
the upstream API notes.

## Notes and limits

- The upstream endpoint is public and free: it can rate-limit, change shape or disappear without notice.
- Persona is a server-side system prompt; the underlying model is one Gemma 4 26B uncensored build.
- A `402` from upstream means a drained credit token; the pool keeps serving on the free lane.
- Identities are anonymous; store them like credentials (the file stays out of git by default).

## License

MIT — see [LICENSE](LICENSE).
