<div align="center">

<img src="brand/logo-dark.svg" alt="aigentools-bulk-9router" width="420">

**Bulk-create AIGenTools accounts, harvest their session cookies, and expose all five free models through 9Router as one OpenAI-compatible pool.**

[![Node.js](https://img.shields.io/badge/Node.js-%E2%89%A518-339933?logo=node.js&logoColor=white)](https://nodejs.org)
[![Zero dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)](package.json)
[![OpenAI compatible](https://img.shields.io/badge/API-OpenAI%20compatible-10a37f)](docs/PROTOCOL.md)
[![9Router](https://img.shields.io/badge/9Router-%E2%89%A50.5-7c3aed)](https://9router.com)
[![Models](https://img.shields.io/badge/free%20models-5-8b5cf6)](#free-models)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-555)](#requirements)

[English](README.md) · [Indonesia](README.id.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [Español](README.es.md)

</div>

---

## What it does

```
DuckMail inbox ──► Turnstile token ──► email OTP ──► session cookie ──► adapter ──► 9Router
```

One command creates as many AIGenTools accounts as you ask for, keeps every
session in its own JSON file, and registers a local OpenAI-compatible adapter in
9Router so every client you own (OpenCode, Cline, Continue, LiteLLM, raw SDKs…)
can call:

| Model | Modalities | Free |
| --- | --- | --- |
| `aigentools/DeepSeek-V4.1 Flash` | text, image | ✅ |
| `aigentools/GLM-5.3 Flash` | text, image | ✅ |
| `aigentools/Qwen3.7 Flash` | text, image | ✅ |
| `aigentools/Gemini 2.5 Flash Lite` | text, image, file | ✅ |
| `aigentools/Claude Haiku 5.5` | text, image, file | ✅ |

Free tier: **30 messages/day per account** — rotate sessions to go beyond it.

## Requirements

* **Node.js ≥ 18** (uses global `fetch`). No npm install, no build step.
* A Chromium/Chrome binary for account creation, **or** any CDP endpoint
  (e.g. a Browser Use cloud browser) via `CDP_URL`.
* 9Router (local or self-hosted) reachable from the machine running the adapter.

## Quick start

```bash
git clone https://github.com/0xgetz/aigentools-bulk-9router.git
cd aigentools-bulk-9router

# 1) create accounts (each one ~20–100 s)
CDP_URL=https://your-cdp-endpoint node bin/cli.js provision --count 3

# 2) start the OpenAI-compatible adapter
node adapter.js        # http://127.0.0.1:8793/v1

# 3) register it in 9Router
node bin/cli.js connect --url http://127.0.0.1:20128 \
                        --adapter http://127.0.0.1:8793/v1

# 4) prove all five models answer
node bin/cli.js verify --url http://127.0.0.1:20128 --key sk-...
```

Then use any model from 9Router:

```bash
node bin/chat.js --url http://127.0.0.1:20128 --key sk-... \
  --model "aigentools/Qwen3.7 Flash" --prompt "hello"
```

## CLI

| Command | Description |
| --- | --- |
| `provision --count N [--concurrency N] [--out DIR]` | Create N accounts; newest becomes `session.json` |
| `connect [--url] [--adapter]` | Register adapter node + provider in 9Router |
| `verify --key sk-...` | Call all five free models through 9Router |
| `list` | Show saved sessions and their expiry |
| `models` | Print the free model ids |

### Environment variables

| Variable | Default | Meaning |
| --- | --- | --- |
| `CDP_URL` | local Chromium | Existing browser endpoint (http/ws) |
| `CHROME_PATH` | auto-detect | Chrome binary for the local launcher |
| `DUCKMAIL_BASE` | `https://api.duckmail.sbs` | Inbox API |
| `SESSION_FILE` | `./session.json` | Session used by the adapter |
| `ROUTER_URL` | `http://127.0.0.1:20128` | 9Router origin |
| `ROUTER_PASSWORD` | `123456` | 9Router dashboard password |
| `ADAPTER_URL` | `http://127.0.0.1:8793/v1` | URL 9Router should call |
| `PROVIDER_PREFIX` | `aigentools` | Model prefix inside 9Router |
| `SESSIONS_DIR` | `./sessions` | Where session JSON files are written |

## How it works

1. **Inbox** — a random `aigt…@<domain>` mailbox is created on DuckMail.
2. **Challenge** — a fresh tab renders an invisible-explicit Turnstile widget and
   returns a one-time token (the dialog itself only works with a real modal and
   is kept as a fallback).
3. **OTP** — `send-verification-otp` is called with the token in
   `x-captcha-response`, the 6-digit code is read from the inbox, then
   `sign-in/email-otp` sets the Better-Auth session cookie.
4. **Adapter** — `adapter.js` flattens OpenAI `messages` into an AIGenTools
   thread and mirrors the reply as `chat.completion.chunk` events.
5. **Router** — `connect` creates an `openai-compatible` provider node with the
   `aigentools` prefix; 9Router then exposes `aigentools/<model>` to every
   downstream tool.

Details and every endpoint are documented in [`docs/PROTOCOL.md`](docs/PROTOCOL.md)
and [`STRUCTURE.md`](STRUCTURE.md).

## Project layout

```
aigentools-bulk-9router/
├── adapter.js               OpenAI-compatible server (:8793)
├── bin/
│   ├── cli.js               provision · connect · verify · list · models
│   └── chat.js              tolerant 9Router chat client
├── src/
│   ├── cdp.js               zero-dep CDP client
│   ├── browser.js           Chromium launcher + helpers
│   ├── duckmail.js          mailbox provider
│   ├── aigentools.js        Turnstile + UI fallback sign-in
│   ├── otp.js               email-OTP endpoints
│   └── connect-9router.js   9Router registration
├── sessions/                one JSON per account (git-ignored)
├── brand/                   logo + icon (SVG)
├── docs/PROTOCOL.md         endpoints, catalogue, 9Router quirks
└── STRUCTURE.md             architecture diagrams
```

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `Turnstile error 600010` | The tab must be a **new** tab; the toolkit retries by itself. Keep one tab per account. |
| `email_otp_captcha_failed` | Token expired/reused — rerun; do not submit the same token twice. |
| No code in the inbox | DuckMail keeps the code for 10 min; the CLI polls up to 4 min then retries the whole account. |
| `401` from 9Router `/v1` | Create a client key (`node bin/cli.js connect` does it) and pass it as `Authorization: Bearer sk-…`. |
| Reply is SSE with `stream:false` | 9Router 0.5.99 relay quirk — use `bin/chat.js` or `"stream": true`. |
| `insufficient_credits` | You picked a paid model; the five free ones never charge credits. |

## Notes

* Sessions last 7 days; re-run `provision` to add fresh ones, then restart the
  adapter so it picks up the newest `session.json`.
* The adapter is intended to run on the same host as 9Router (or behind a
  private network); it has no built-in authentication of its own.
* This is an interface to a third-party service. Respect that service's terms
  and the rates you agreed to.

## License

[MIT](LICENSE)
