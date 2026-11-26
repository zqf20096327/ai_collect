# Muse Gateway

[![npm](https://img.shields.io/npm/v/muse-gateway?color=e5484d)](https://www.npmjs.com/package/muse-gateway)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![CI](https://github.com/lynbyte/muse-gateway/actions/workflows/ci.yml/badge.svg)](https://github.com/lynbyte/muse-gateway/actions/workflows/ci.yml)

Turn your own muse.ai accounts into an **OpenAI-compatible API** that runs on your machine or VPS. Chat, images and video, from any tool that speaks the OpenAI API.

> 🇻🇳 Biến tài khoản Muse của bạn thành API chuẩn OpenAI, chạy local hoặc trên VPS. Miễn phí, mã nguồn mở.

![Activity dashboard](docs/images/activity.png)

## Features

- **OpenAI-compatible:** `/v1/chat/completions`, `/v1/responses`, `/v1/images/generations`, `/v1/audio/speech`, `/v1/models`
- **Images, video and voice:** up to 4 images per request, videos through a task API with polling or webhooks, reference images supported, text-to-speech mp3 with Muse's 1,219 voices
- **MCP server** for Claude, Cursor and other agents
- **Account pool:** round-robin, failover or parallel across several Muse accounts, with automatic concurrency per account
- **Dashboard:** accounts, API keys with per-model access, usage stats, generated media, logs
- **Reach it from anywhere:** Cloudflare tunnel, Tailscale, or a Telegram bot (`/vid`, `/img`, `/voice`)
- **Windows tray app:** runs in the background and starts with Windows

## Quick start

Requires Windows 10/11, Node.js ≥ 20.9 and Chrome or Edge.

```bash
npm install -g muse-gateway
muse-gateway
```

Open the dashboard, add a Muse account, create an API key, then point your tool at it:

```python
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:1412/v1", api_key="YOUR_KEY")
reply = client.chat.completions.create(
    model="muse-chat",
    messages=[{"role": "user", "content": "Hello"}],
)
print(reply.choices[0].message.content)
```

Models: `muse-chat`, `muse-image`, `muse-video`, `muse-voice`. The full API reference (tasks, webhooks, errors) is in [npm/README.md](npm/README.md).

| Account pool | Accounts |
|---|---|
| ![Pool settings](docs/images/quota.png) | ![Accounts](docs/images/accounts.png) |

## Fixed URL (optional)

Every feature is free and works without a key. To reach the gateway from the internet, start a Cloudflare quick tunnel (random URL that changes on restart) or use your own Cloudflare tunnel and domain. On a VPS you can also call `http://<server-ip>:1412/v1` directly.

A license key adds a **fixed tunnel URL** issued by the license server in [license-server/](license-server/), which you can also deploy yourself.

## Your responsibility

The gateway drives your own muse.ai accounts through a browser. Check that this fits Muse's terms before using it, and accept the risk that an account may be limited. Only generate content you have the right to make.

## Development

```bash
npm install
npm run dev
```

The dashboard opens at http://localhost:3000 and the API lives under `/v1`. Runtime data goes to `./data`; set `MUSE_DATA_DIR` to use another folder. `data/` never ships in a release.

Run the tests, which need no browser or Muse account:

```bash
npm test
```

## Project layout

| Path | Contents |
|---|---|
| `src/app/v1/` | Public API: chat completions, responses, images, models, tasks |
| `src/app/api/` | Dashboard API and media delivery |
| `src/lib/museDriver.ts` | Drives muse.ai in a browser |
| `src/lib/musePool.ts` | Account selection, cooldowns, idempotency |
| `src/lib/modelKind.ts` | What each model returns (chat / image / video); the only place that decides it |
| `src/lib/tasks.ts` | Background tasks and webhooks |
| `npm/` | Published package: CLI, tray and user README |
| `license-server/` | License service |
| `extension/` | Chrome/Edge extension |

## Release

Follow the runbook in [AGENTS.md](AGENTS.md). Always publish the tarball produced by `npm run package`.

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)
