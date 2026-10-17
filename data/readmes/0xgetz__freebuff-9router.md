<div align="center">

<img src="logo.svg" width="128" alt="freebuff-9router" />

# freebuff-9router

**Free OpenAI-compatible LLM access** (Codebuff/Freebuff free tier) wired into a
[9router](https://github.com/) gateway — device-code OAuth, a local
OpenAI-compatible adapter, and automatic 9router registration of the models
your account actually has.

![license MIT](https://img.shields.io/badge/license-MIT-4FC3F7)
![python 3.11](https://img.shields.io/badge/python-3.11-blue)
![dependencies none](https://img.shields.io/badge/dependencies-none-brightgreen)
![9router ready](https://img.shields.io/badge/9router-ready-8B5CF6)
![model mimo/mimo-v2.5](https://img.shields.io/badge/model-mimo%2Fmimo--v2.5-6D28D9)
![free tier 6 msg/day](https://img.shields.io/badge/free-tier-6%20msg%2Fday-orange)

[English](README.md) · [Bahasa Indonesia](README.id.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md)

</div>

```
freebuff.com ──(device-code login)──> token
      │
      │  POST /api/v1/freebuff/session   (free session, 1h)
      │  POST /api/v1/agent-runs START   (agent run)
      │  POST /api/v1/chat/completions   (SSE, CLI envelope)
      ▼
adapter.py  (127.0.0.1:8787, OpenAI-compatible /v1)
      │
      │  POST /api/provider-nodes  /api/providers  /api/models/custom  /api/combos
      ▼
9router ──> /v1/chat/completions (model "freebuff")
```

Stdlib only. No pip installs.

## Why an adapter?

The Codebuff API is **not** plain OpenAI. Each request needs:

1. a free **session** (`POST /api/v1/freebuff/session` → `instanceId`, ~1h),
2. an **agent run** (`POST /api/v1/agent-runs` `{action:"START"}` → `runId`),
3. the chat POST with a "CLI envelope" or the server rejects it:
   - `codebuff_metadata.run_id` = the runId — **not** top-level `runId`
     (that 400s with `No runId found in request body`)
   - `codebuff_metadata.client_id` = fresh random 13-char base36 per call
     (fixed values like `"cli"` get fingerprinted as a proxy)
   - `codebuff_metadata.cost_mode` = `"free"` (omit → 402 `Out of credits`)
   - `codebuff_metadata.freebuff_instance_id` = session instanceId
   - first system message = the "Buffy" identity marker (else 403
     `free_mode_cli_required`)
   - `User-Agent: Freebuff-CLI/<version>`
   - `provider: {"data_collection":"deny"}`, `stop: ["cb_easp"]`

The adapter hides all of that and streams SSE incrementally (a 9router
upstream fetch kills buffered responses at ~30s → 502).

## Free tier limits

- **6 messages/day** per model (pool `limited`, resets on Pacific day).
- Model is **locked per account** — free limited tier resolves to
  `mimo/mimo-v2.5` regardless of what you request (`session_model_mismatch`).
  `adapter.py` has a `MODEL_AGENT` map for the other free models in case your
  account gets a higher tier.
- On quota exhaustion you'll see 402/429-style upstream errors surfaced as
  OpenAI error objects.

## Usage

```bash
# 1. login (prints a URL; open it in a browser, sign in with GitHub/Google)
python3 login.py --token-out freebuff-token.json

# 2. start the adapter
python3 adapter.py --port 8787 --token freebuff-token.json

# 3. wire into 9router (idempotent — safe to re-run)
python3 wire_9router.py --adapter-port 8787 --token freebuff-token.json \
    --router-url http://127.0.0.1:20128

# or everything at once
./bootstrap.sh
```

`wire_9router.py` does:

1. creates (or reuses) an `openai-compatible` node with prefix `cb`,
2. attaches the freebuff authToken as a connection,
3. asks the adapter which models the account can use and registers each as a
   **custom model** (`/api/models/custom`) so it shows up in the dashboard
   provider page,
4. creates a `freebuff` combo (`cb/<model>`), optionally `--append-combo <id>`
   to append the model as a fallback tail of an existing combo,
5. runs the connection test.

Then chat through the router:

```bash
curl http://<router>/v1/chat/completions \
  -H "Authorization: Bearer <router-api-key>" \
  -d '{"model":"freebuff","messages":[{"role":"user","content":"hi"}]}'
```

## 9router admin auth

The wire script authenticates to 9router with the CLI token:
`x-9r-cli-token: sha256(machineId + "9r-cli-auth" + cliSecret)[:16]`
(paths: `/root/.9router/machine-id`, `/root/.9router/auth/cli-secret` by
default; override with `--machine-id` / `--cli-secret`).

## Files

| file | purpose |
|------|---------|
| `login.py` | device-code OAuth → `freebuff-token.json` |
| `adapter.py` | OpenAI-compatible `/v1` server (session+run dance per request) |
| `wire_9router.py` | idempotent 9router node/connection/models/combo setup |
| `bootstrap.sh` | login → adapter → wire in one shot |

## Disclaimer

For use with accounts you own. Respect Codebuff/Freebuff's ToS and rate
limits; free-tier quotas exist for a reason.
