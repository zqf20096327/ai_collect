<div align="center">

<img src="brand/logo.svg" alt="Solar Pool × 9Router" width="520"/>

**Turn the free models inside Solar Chat into a self-healing, load-balanced OpenAI endpoint for 9Router.**

[![License: MIT](https://img.shields.io/badge/License-MIT-6C5CE7.svg?style=flat-square)](LICENSE)
[![Node](https://img.shields.io/badge/Node-18%2B-3C873A.svg?style=flat-square&logo=node.js&logoColor=white)](https://nodejs.org)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB.svg?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Playwright](https://img.shields.io/badge/Playwright-Chromium-2EAD33.svg?style=flat-square&logo=playwright&logoColor=white)](https://playwright.dev)
[![9Router](https://img.shields.io/badge/9Router-0.5.x-FF7A18.svg?style=flat-square)](https://9router.com)
[![OpenAI Compatible](https://img.shields.io/badge/API-OpenAI--Compatible-412991.svg?style=flat-square&logo=openai&logoColor=white)](https://platform.openai.com/docs/api-reference)
[![Self Hosted](https://img.shields.io/badge/Deploy-Self%20Hosted-22C55E.svg?style=flat-square)](#quick-start)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-6C5CE7.svg?style=flat-square)](#)

[English](README.md) · [Indonesia](i18n/README.id.md) · [中文](i18n/README.zh.md) · [日本語](i18n/README.ja.md) · [Español](i18n/README.es.md)

</div>

---

## What is this?

**Solar Pool × 9Router** is a small, dependency-light toolkit that:

1. **Creates a pool of Solar Chat sessions in bulk** — no signup, no email, no captcha.
2. **Keeps every session alive** (auto-refresh, so it never expires).
3. **Serves them as one OpenAI-compatible endpoint** with round-robin rotation and automatic failover.
4. **Wires that endpoint into [9Router](https://9router.com)** so every model shows up under a `solar/` prefix.

Solar Chat (`solar-chat.upstage.ai`) is an **anonymous** chat: it issues each browser a
`solar_session` cookie with a hard **30-minute TTL**, and the chat itself runs over a
**WebSocket** (`solar-chat.v1`), not a REST API. This project handles all of that for you.

> **Why sessions, not accounts?** Solar Chat has no login (`/api/auth/config` → `{"mode":"off"}`).
> "One account" = "one cookie session". So the pool is a pool of sessions — every fresh
> browser context yields an independent one.

---

## Features

| | Feature |
|---|---|
| 🚀 | **Bulk session creation** — spin up N isolated Chromium contexts in parallel |
| ♻️ | **Self-healing** — a background refresher renews every session before the 30-min TTL |
| ⚖️ | **Load balancing** — round-robin across the pool, auto-marks dead sessions |
| 🔌 | **OpenAI-compatible** — `POST /v1/chat/completions` (+ SSE streaming) and `GET /v1/models` |
| 🧭 | **9Router native** — one command registers an `openai-compatible` provider node |
| 🛰️ | **VPS-native** — runs entirely on your own server, no cloud browser required |
| 🪶 | **No heavy deps** — the adapter is pure Node stdlib; the creator uses Playwright |
| 🧩 | **Nine models** — `solar-pro4`, `solar-mini4`, `auto`, `solar-open2`, `mimo-v2.5`, … |

---

## Architecture

```
   your CLI / IDE / any OpenAI client
                │
                ▼
        ┌───────────────────┐
        │   9Router :20128  │   /v1/chat/completions
        │  provider "solar" │   load balance + fallback across providers
        └─────────┬─────────┘
                  │  openai-compatible node  →  adapter :8787/v1
                  ▼
        ┌───────────────────┐        round-robin
        │  Pool Adapter     │───────────────────────────────┐
        │  (adapter.js)     │                               │
        └─────────┬─────────┘                               │
                  │  pick a live account                    │
        ┌─────────┴─────────┬───────────────┬───────────────┤
        ▼                   ▼               ▼               ▼
   ┌─────────┐         ┌─────────┐     ┌─────────┐     ┌─────────┐
   │ acct-1  │         │ acct-2  │     │ acct-3  │ ... │ acct-N  │   accounts.json
   │ session │         │ session │     │ session │     │ session │
   └────┬────┘         └────┬────┘     └────┬────┘     └────┬────┘
        └───────────────────┴───────────────┴───────────────┘
                            │  wss://solar-chat.upstage.ai/api/agent/chat/ws
                            ▼        (cookie: solar_session + aws-waf-token)
                    ┌────────────────────┐
                    │   Solar Chat WS    │
                    │  solar-pro4 / etc. │
                    └────────────────────┘

   ♻️  refresh_pool.py ──► local headless Chromium ──► renews cookies in accounts.json
```

See [`STRUCTURE.md`](STRUCTURE.md) for the full file map and message flow.

---

## Quick start

### 0 · Prerequisites

* **Node 18+** (the adapter uses the global `fetch`).
* **Python 3.9+** + Playwright Chromium:
  ```bash
  pip install playwright
  playwright install --with-deps chromium
  ```
* A running **9Router** (`npm install -g 9router && 9router`, default port `20128`).

### 1 · Clone

```bash
git clone https://github.com/0xgetz/solar-pool-9router.git
cd solar-pool-9router/scripts
```

### 2 · One command

```bash
./run.sh <9router-password> 10
```

That creates **10 sessions**, starts the **pool refresher**, starts the **adapter**, and
**registers it in 9Router**. Done.

### 3 · Use it

```
Base URL : http://localhost:20128/v1
API Key  : <create under 9Router → API Keys>
Model    : solar/solar-pro4
```

```bash
curl http://localhost:20128/v1/chat/completions \
  -H "Authorization: Bearer sk-..." \
  -H "Content-Type: application/json" \
  -d '{"model":"solar/solar-pro4","messages":[{"role":"user","content":"hello"}]}'
```

---

## Manual steps

```bash
# 1. build a pool (3 sessions, 2 at a time)
python3 accounts.py -n 3 -c 2

# 2. keep them alive forever
python3 refresh_pool.py --interval 300 --concurrency 2

# 3. serve the pool as OpenAI-compatible
PORT=8787 node adapter.js

# 4. register into 9Router
node connect-9router.js --base http://localhost:20128 --password <pw> \
     --adapter http://localhost:8787
```

---

## Models

| ID | Notes |
|----|-------|
| `solar-pro4` | flagship, 524k context, reasoning |
| `solar-mini4` | fast + cheap, 524k context, reasoning |
| `auto` | Solar Chat auto-selects |
| `solar-open2` · `solar-mini4-rc` · `solar-pro3` · `solar-pro2` | other Solar models |
| `mimo-v2.5` · `qwen3.6-35b-a3b` | third-party models exposed by Solar Chat |

Pass `"reasoning_effort": "none|minimal|low|medium|high|xhigh|max|adaptive"` for reasoning models.

---

## Adapter API

| Method | Path | Description |
|--------|------|-------------|
| `GET`  | `/v1/models` | OpenAI model list |
| `POST` | `/v1/chat/completions` | chat (`"stream": true` for SSE) |
| `GET`  | `/health` | pool summary (`alive` / `accounts`) |
| `GET`  | `/pool` | per-account health, failures, usage |
| `POST` | `/pool/reload` | re-read `accounts.json` |

---

## CLI reference

**`accounts.py`** — bulk creator

| Flag | Default | Meaning |
|------|---------|---------|
| `-n, --count` | `1` | how many new sessions |
| `-c, --concurrency` | `3` | parallel browser contexts |
| `--out` | `accounts.json` | output file (appended) |
| `--settle` | `9` | seconds to wait after page load |
| `--proxy` | — | `socks5://user:pass@host:port` for browser egress |
| `--headful` | off | show the browser window |
| `--fresh` | off | ignore an existing `accounts.json` |

**`refresh_pool.py`** — keep-alive

| Flag | Default | Meaning |
|------|---------|---------|
| `--interval` | `300` | seconds between refreshes |
| `--concurrency` | `2` | parallel refreshes |
| `--once` | off | refresh a single time and exit |

---

## Deploy as a service

Keep everything running with **systemd**:

```ini
# /etc/systemd/system/solar-pool.service
[Unit]
Description=Solar Pool × 9Router
After=network-online.target
Wants=network-online.target

[Service]
WorkingDirectory=/opt/solar-pool-9router/scripts
ExecStart=/opt/solar-pool-9router/scripts/run.sh ${NINEROUTER_PASSWORD} 10
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable --now solar-pool
```

Prefer `pm2` or `tmux`? Both work — just keep `refresh_pool.py` and `adapter.js` alive.

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `WS upgrade HTTP 202` | The WAF is challenging — re-run `refresh_pool.py --once`; the cookie likely expired. |
| `/health` shows `0 alive` | Run `accounts.py -n 5`, then `refresh_pool.py --once`. |
| Adapter says "Pool empty" | `accounts.json` missing — create accounts first. |
| Playwright launch fails (`libglib`) | `playwright install --with-deps chromium` (needs root/apt). |
| 9Router 404 on chat | Re-run `connect-9router.js`; check the node prefix is `solar`. |
| Chrome not found in Docker | Set `CHROME_PATH=/path/to/chrome`. |

---

## Responsible use

Solar Chat is a free consumer service. This toolkit creates **anonymous sessions**, not
accounts, and adds only modest concurrency. Use it for **personal, low-volume
integration** and respect Upstage's Terms of Service and rate limits. Do not resell
access or hammer the service. The authors are not affiliated with Upstage or 9Router.

---

## License

[MIT](LICENSE) © 2026 [0xgetz](https://github.com/0xgetz)
