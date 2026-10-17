<div align="center">

<img src="assets/banner.png" alt="MiniMax2API" width="820"/>

# MiniMax2API

**OpenAI-compatible API proxy for the MiniMax Agent API.**

[![License: MIT](https://img.shields.io/badge/License-MIT-6ee7ff.svg?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688.svg?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![OpenAI Compatible](https://img.shields.io/badge/OpenAI-Compatible-7c8cff.svg?style=flat-square&logo=openai&logoColor=white)](#)
[![Streaming](https://img.shields.io/badge/Streaming-SSE-c084fc.svg?style=flat-square)](#)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg?style=flat-square&logo=docker&logoColor=white)](Dockerfile)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-8be9ff.svg?style=flat-square)](#contributing)

[English](README.md) · [Bahasa Indonesia](README.id.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [Español](README.es.md)

</div>

---

## What is this?

MiniMax2API turns the **MiniMax Agent** web API (`agent.minimax.io`) into a
standard **OpenAI-compatible** endpoint, so you can use it with any OpenAI SDK,
client, or router (including 9router, OpenWebUI, LibreChat, LangChain, and more).

It handles the reverse-engineered request signing, session management, and
Server-Sent-Events streaming for you — you just talk OpenAI.

> Built on the same idea as [Duck2API](https://github.com/aurora-develop/Duck2api):
> a small, self-hosted, drop-in OpenAI proxy.

## Features

| Feature | Endpoint | Status |
|---------|----------|--------|
| Chat Completions | `POST /v1/chat/completions` | ✅ |
| Streaming (SSE) | `POST /v1/chat/completions` (`stream: true`) | ✅ |
| Model listing | `GET /v1/models` | ✅ |
| Health check | `GET /health` | ✅ |
| Bearer / `x-api-key` auth | all routes | ✅ |
| Multi-turn context | flattened into the prompt | ✅ |
| Docker / Compose | included | ✅ |

## Quick start

### 1. Get your credentials

Log in at <https://agent.minimax.io/>, open DevTools → Console, and run:

```bash
python app/get_credentials.py --json
```

or paste the snippet from `python app/get_credentials.py` directly into the
console. It prints something like:

```json
{"token":"eyJhbGci...","agent_id":"447316105384064","uuid":"1604265c-...","device_id":"52668348","user_id":"561636901788553221"}
```

### 2. Configure

```bash
cp env.template .env
# then edit .env and fill in MM_TOKEN, MM_AGENT_ID, MM_UUID, MM_DEVICE_ID, MM_USER_ID
```

### 3. Run

**Local:**

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cd app && python server.py
```

**Docker:**

```bash
docker build -t minimax2api .
docker run -d --name minimax2api --env-file .env -p 8100:8100 minimax2api
```

**Docker Compose:**

```bash
docker compose up -d
```

## Usage

### cURL

```bash
curl http://localhost:8100/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-minimax-local" \
  -d '{
    "model": "MiniMax-M3.1-Flash-Preview",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

### OpenAI Python SDK

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8100/v1", api_key="sk-minimax-local")

stream = client.chat.completions.create(
    model="MiniMax-M3.1-Flash-Preview",
    messages=[{"role": "user", "content": "Write a haiku about proxies."}],
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
```

Full endpoint reference: **[API.md](API.md)**.

## How it works

```
OpenAI client ──▶ FastAPI (/v1/chat/completions)
                      │
                      ▼
             MiniMaxAdapter  (app/adapter.py)
                      │  signs requests (x-signature, yy)
                      ▼
   POST /agent/{id}/session      → create session
   POST /session/{id}/message    → SSE stream of the reply
```

The MiniMax web app signs every request with a timestamped `x-signature` and a
`yy` fingerprint. `app/sign.py` reproduces that algorithm; `app/adapter.py`
drives the session/turn lifecycle and parses the reply stream.

## Configuration

See [`env.template`](env.template) for every option. The important ones:

| Variable | Required | Description |
|----------|:--------:|-------------|
| `MM_TOKEN` | ✅ | MiniMax JWT |
| `MM_AGENT_ID` | ✅ | Agent id from the `/mavis?id=` URL |
| `MM_UUID` | ✅ | `localStorage.UNIQUE_USER_ID` |
| `MM_DEVICE_ID` | ✅ | `sessionStorage.tab_device_id` |
| `MM_USER_ID` | ✅ | `localStorage.user_detail_agent.realUserID` |
| `MM_MODEL` | – | Model id (default `MiniMax-M3.1-Flash-Preview`) |
| `MM_API_KEY` | – | Require this key on requests (empty = no auth) |
| `PORT` | – | Listen port (default `8100`) |

## Project layout

```
.
├── app/
│   ├── adapter.py         # MiniMax session + streaming logic
│   ├── server.py          # FastAPI OpenAI-compatible server
│   ├── sign.py            # request signing (x-signature, yy)
│   ├── get_credentials.py # helper to extract browser credentials
│   ├── tool_dsml.py       # tool-call parsing helpers
│   └── tool_sieve.py
├── assets/                # logo & banner
├── API.md                 # full API reference
├── Dockerfile
├── docker-compose.yml
├── env.template
└── requirements.txt
```

## Contributing

Issues and pull requests are welcome. Please keep changes focused and test the
server against a live MiniMax session before opening a PR.

## Disclaimer

This project is unofficial and not affiliated with MiniMax. It is intended for
personal and educational use. Respect MiniMax's Terms of Service. Your
credentials stay on your machine — this server only talks to `agent.minimax.io`
on your behalf.

## License

[MIT](LICENSE)
