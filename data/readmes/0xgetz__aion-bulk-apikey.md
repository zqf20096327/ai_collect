<div align="center">

<img src="brand/logo.svg" alt="Aion Bulk" width="420">

### Bulk-create Aion Labs accounts, mint API keys, route every model through 9Router.

[![License: MIT](https://img.shields.io/badge/license-MIT-63b3ff?style=flat-square)](LICENSE)
[![Node](https://img.shields.io/badge/node-%E2%89%A518-7c5cff?style=flat-square&logo=node.js&logoColor=white)](https://nodejs.org)
[![Dependencies](https://img.shields.io/badge/dependencies-zero-ff7a59?style=flat-square)](package.json)
[![Models](https://img.shields.io/badge/models-6%20aion--labs-2ea043?style=flat-square)](#models)
[![9Router](https://img.shields.io/badge/9Router-openai--compatible-e8590c?style=flat-square)](https://github.com/decolua/9router)
[![OpenAI API](https://img.shields.io/badge/API-OpenAI--compatible-10a37f?style=flat-square)](#adapter)
[![No build](https://img.shields.io/badge/build-none-informational?style=flat-square)](#quick-start)
[![Languages](https://img.shields.io/badge/README-6%20languages-8fa3bf?style=flat-square)](#languages)

[English](README.md) · [Bahasa Indonesia](README.id.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Deutsch](README.de.md)

</div>

---

## What it does

`aion-bulk-apikey` turns the manual "sign up → open email → confirm → create key" loop on
[aionlabs.ai](https://www.aionlabs.ai) into one command, then puts every key to work:

1. **Creates a fresh inbox** on a disposable mail domain (or any address on a domain you own).
2. **Signs up** in a real browser — fills the form, waits for Cloudflare Turnstile to solve itself,
   submits with native typing so the widget stays attached.
3. **Confirms the email** by following the link found in the inbox.
4. **Mints an API key with a random name** (`amber-ranger-4117`, `solar-spark-6372`, …) and captures
   the plaintext once, because the dashboard never shows it again.
5. **Probes the account** with a real chat completion so a stored row is a working row.
6. **Wires everything into 9Router** as one provider, and/or **serves an OpenAI-compatible pool**
   with round-robin scheduling and failover.

Zero dependencies. No npm install. Node 18+ and a Chrome DevTools endpoint.

## Quick start

```bash
git clone https://github.com/0xgetz/aion-bulk-apikey.git
cd aion-bulk-apikey
```

The CLI launches Chrome/Chromium itself and talks to it over DevTools — nothing to install except a
browser. Point `--chrome` at a binary if it is not on your `PATH`, or attach to an already-running
Chrome with `--cdp` (see [Browser](#browser)).

```bash

# 5 accounts, two at a time, random key names
node src/cli.js create --count 5 --concurrency 2 --models models.json

# call every model on the account
node src/cli.js test

# register the accounts in a local 9Router and smoke-test it
node src/cli.js connect --router http://127.0.0.1:20128 --prefix aion

# or expose them directly as an OpenAI-compatible endpoint on :8790
node src/cli.js serve --port 8790
```

```jsonc
// POST http://127.0.0.1:8790/v1/chat/completions
{ "model": "aion-labs/aion-3.5-mini", "messages": [{ "role": "user", "content": "hi" }] }
```

## Commands

| Command | Purpose |
|---------|---------|
| `create` | Bulk accounts + keys. `--count`, `--concurrency`, `--key-name`, `--key-prefix`, `--no-verify` |
| `test` | Chat-completion call against every model (or `--model <id>`) |
| `connect` | Login to 9Router, create a router key, register provider node + one connection per account, smoke test |
| `serve` | OpenAI-compatible pool: `/v1/models`, `/v1/chat/completions` (stream + non-stream), `/health`, `/pool`, `/pool/reload` |
| `models` | Print or dump the model catalogue |
| `key` | Mint one more key on an already signed-in browser |
| `login` | Sign a browser into an existing account |
| `export` | Dump `accounts.json` as JSON or CSV (`--format csv`) |

## Models

The account tier available at signup exposes six `aion-labs/*` models:

| Model | Context | Tools | $ / 1M in–out |
|-------|---------|-------|----------------|
| `aion-labs/aion-2.0` | 128K | yes | 0.80 / 1.60 |
| `aion-labs/aion-3.0` | 128K | yes | 3.00 / 6.00 |
| `aion-labs/aion-3.0-mini` | 128K | yes | 0.70 / 1.40 |
| `aion-labs/aion-3.5` | 256K | yes | 3.00 / 6.00 |
| `aion-labs/aion-3.5-mini` | 256K | yes | 0.70 / 1.40 |
| `aion-labs/aion-rp-llama-3.1-8b` | 128K | yes | 0.80 / 1.60 |

The list is read live from `GET /v1/models`, so a new model needs no code change.

## Adapter

`serve` starts a small HTTP server that is a drop-in OpenAI endpoint:

```
GET  /v1/models              catalogue
POST /v1/chat/completions    stream and non-stream
GET  /health                 account count
GET  /pool                   per-account usage, health and last error
POST /pool/reload            re-read accounts.json without a restart
```

Requests are distributed round-robin; an account that fails three times in a row is parked until a
success resets it, and every request fails over to the remaining accounts.

## Browser

`create` needs a real Chromium because the signup form is protected by Cloudflare Turnstile. The CLI
finds Chrome, Chromium or Edge on the usual paths, launches it headless on a free port and
closes it when the run ends. Overrides:

| Flag | Meaning |
|------|---------|
| `--chrome <path>` | browser binary to launch (default: auto-detect, or `CHROME_PATH`) |
| `--port 9333` | DevTools port for the launched browser |
| `--headed` | show the window instead of headless (some hosts solve Turnstile more reliably) |
| `--keep-browser` | leave the browser running after the run |
| `--cdp <url>` | attach to a browser you started yourself (`http://127.0.0.1:9222` or a `ws://` endpoint) |

Turnstile is bound to the IP that requested it. Datacenter ranges are challenged far more aggressively,
so run this from a residential connection or route the browser through a residential proxy
(`--proxy socks5://user:pass@host:port`). Without a working browser the run stops with
`turnstile not solved within timeout` or `CDP timeout`.

## Inbox providers

| `--mailbox` | Notes |
|-------------|-------|
| `gmail` *(default)* | Real `@gmail.com` addresses from emailnator (dot-variants of pooled Google mailboxes); `--gmail-type googlemail` or `plus` for other shapes |
| `best-tempmail` | `api.best-tempmail.com`, 5 domains, 120-minute inboxes, 3/day per IP |
| `mailboxtemp` | `mailboxtemp.com`, public API, 60-minute inboxes, 10/day per IP |
| `tempmail` | `api.tempmail.lol`, brand-new subdomains on every call |
| `mailtm` | `mail.tm`; HTTP/2 via curl, automatic backoff on 429 |
| `maildrop` | `api.maildrop.cc` over GraphQL |
| `own` | `--address you@yourdomain` read from your own mail server (`--inbox-api`); `tools/inbox-server.js` is a minimal SMTP/IMAPS/HTTP test server |
| `generic` | Your own provider through `INBOX_CREATE_URL` / `INBOX_LIST_URL` |
| `agent` | Alias-routed agent mailbox |

Aion Labs caps **signups per email domain**, not per IP, and blocks several disposable domains
outright (`Please use a permanent email address — disposable email providers are not supported`).
If you see `Too many recent signups from this email domain`, switch provider or domain — a new proxy
will not help. The default provider rotates domains automatically and parks a domain after its first
refusal. See [docs/PROTOCOL.md](docs/PROTOCOL.md).

## Verified

Run on 2026-10-18 against the live site:

| Check | Result |
|-------|--------|
| Account → email → key (browser flow) | multiple accounts, keys valid at `/v1/chat/completions` |
| Key format | `alv2_` + 43 chars of base64url (`A-Z a-z 0-9 _ -`) |
| `create` → `test` | 6/6 models answered |
| `--mailbox gmail` | real `@gmail.com` accounts created, keys valid, 2/2 in a row |
| Browser auto-launch, zero config | local Chromium found, started, driven and closed by the CLI |
| `connect` → 9Router `/v1/models` | 6 `aion/*` models listed |
| 9Router chat, every model | 6/6 PASS |
| `serve` non-stream / stream | both OK, `/pool` counts usage |
| `node tools/mock-mail.js` | PASS (offline) |

## Files

`accounts.json`, `models.json` and `router.json` appear at runtime and are git-ignored: they hold live
credentials. See [STRUCTURE.md](STRUCTURE.md) for the full map.

## Languages

This README exists in English, Indonesian, Chinese, Japanese, Spanish and German — see the language
row at the top.

## License

MIT © 0xgetz

Aion Labs, 9Router and the mailbox providers are third-party services; this project is not
affiliated with any of them. Use it within their terms.
