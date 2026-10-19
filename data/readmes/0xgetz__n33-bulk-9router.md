<p align="center">
  <img src="brand/logo.svg" alt="n33-bulk-9router" width="640">
</p>

<p align="center">
  <a href="https://github.com/0xgetz/n33-bulk-9router/stargazers"><img alt="stars" src="https://img.shields.io/github/stars/0xgetz/n33-bulk-9router?style=for-the-badge&color=8b7cf6&labelColor=0a0a0f"></a>
  <a href="https://github.com/0xgetz/n33-bulk-9router/network/members"><img alt="forks" src="https://img.shields.io/github/forks/0xgetz/n33-bulk-9router?style=for-the-badge&color=5b8cff&labelColor=0a0a0f"></a>
  <a href="LICENSE"><img alt="license" src="https://img.shields.io/github/license/0xgetz/n33-bulk-9router?style=for-the-badge&color=3ddc97&labelColor=0a0a0f"></a>
  <a href="https://github.com/0xgetz/n33-bulk-9router/issues"><img alt="issues" src="https://img.shields.io/github/issues/0xgetz/n33-bulk-9router?style=for-the-badge&color=f5b942&labelColor=0a0a0f"></a>
</p>

<p align="center">
  <img alt="node" src="https://img.shields.io/badge/node-%E2%89%A518-339933?style=flat-square&logo=node.js&logoColor=white">
  <img alt="deps" src="https://img.shields.io/badge/dependencies-0-3ddc97?style=flat-square">
  <img alt="openai" src="https://img.shields.io/badge/OpenAI-compatible-8b7cf6?style=flat-square">
  <img alt="9router" src="https://img.shields.io/badge/9Router-ready-5b8cff?style=flat-square">
</p>

<p align="center">
  <b>English</b> · <a href="docs/README.id.md">Indonesia</a> · <a href="docs/README.zh.md">中文</a> · <a href="docs/README.ja.md">日本語</a> · <a href="docs/README.es.md">Español</a>
</p>

---

## What this is

A zero-dependency Node toolkit that **creates n33.ai accounts in bulk**, **harvests the session cookies** they come back with, and **serves the ten free n33 models through 9Router** as an ordinary OpenAI-compatible provider.

| Capability | Detail |
|---|---|
| Bulk signup | DuckMail (`duckmail.sbs`) mailbox → n33 sign-up → magic-link verification → password sign-in, fully automated (~6 s per account) |
| Session harvest | `__Secure-n33.session_token` cookie stored per account, never an API key (n33 has none) |
| Pool adapter | Round-robin across accounts, cooldown on failure, automatic failover, `/health` and `/pool` introspection |
| 9Router connector | Creates the provider node, registers all ten models, mints a client key and verifies each model through `/v1/chat/completions` |
| Transport | HTTP + SSE streaming and non-streaming, exactly like an OpenAI endpoint |

> **Scope.** It only drives the public web endpoints of n33.ai with the account it just created, for personal experimentation. Respect the n33.ai terms of service.

## Free models

| 9Router model | Name | Provider |
|---|---|---|
| `n33/n33-chat` | Claude Haiku 4.5 *(default)* | Anthropic |
| `n33/n33-claude-sonnet` | Claude Sonnet 5 | Anthropic |
| `n33/n33-claude-opus` | Claude Opus 5 | Anthropic |
| `n33/n33-gpt` | GPT-5.6 Luna | OpenAI |
| `n33/n33-gpt-terra` | GPT-5.6 Terra | OpenAI |
| `n33/n33-gpt-sol` | GPT-5.6 Sol | OpenAI |
| `n33/n33-gpt-astra` | GPT-6 Astra | OpenAI |
| `n33/n33-grok` | Grok 4.5 | xAI |
| `n33/n33-grok-4-6` | Grok 4.6 | xAI |
| `n33/n33-grok-4-7` | Grok 4.7 | xAI |

## Quick start

```bash
git clone https://github.com/0xgetz/n33-bulk-9router.git
cd n33-bulk-9router

# 1. create accounts (2 at a time by default)
node src/cli.js create --count 5 --concurrency 2

# 2. sanity-check sessions and a real chat
node src/cli.js verify

# 3. start the OpenAI-compatible pool
node src/cli.js serve --port 8784

# 4. register everything in 9Router and verify each model
node src/cli.js connect --router http://127.0.0.1:20128 --password 123456 --adapter http://127.0.0.1:8784
```

Then point any OpenAI client at 9Router:

```bash
curl http://127.0.0.1:20128/v1/chat/completions \
  -H "Authorization: Bearer sk-…" \
  -H "Content-Type: application/json" \
  -d '{"model":"n33/n33-grok","messages":[{"role":"user","content":"hello"}]}'
```

## CLI

| Command | Purpose |
|---|---|
| `create --count N [--concurrency 2] [--domains a.shop,b.shop]` | Bulk-create accounts, save JSON/TXT/cookies |
| `verify [--model n33-grok]` | Re-check every stored session with `/api/v1/me` + one chat |
| `serve [--port 8784] [--host 0.0.0.0]` | Run the pool adapter (`/v1/models`, `/v1/chat/completions`, `/health`, `/pool`) |
| `connect [--router URL] [--password PW] [--adapter URL]` | Register node, models and key in 9Router, verify all ten |
| `list` | Print stored accounts |
| `test [--count 2]` | Throw-away accounts + every free model, no files written |

## Data

`./data/accounts.json` (0600), `./data/accounts.txt` (`email|password`) and `./data/cookies.json`. Nothing else is written; sessions expire after 30 days, so rerun `verify` and delete dead rows when they do.

## Requirements

Node.js 18 or newer — global `fetch` and `FormData` are all it uses. No npm install, no native modules, no browser.

## More

- [`STRUCTURE.md`](STRUCTURE.md) — module map and data flow diagram
- [`docs/PROTOCOL.md`](docs/PROTOCOL.md) — n33 auth, chat transport and 9Router registration
- [`LICENSE`](LICENSE) — MIT
