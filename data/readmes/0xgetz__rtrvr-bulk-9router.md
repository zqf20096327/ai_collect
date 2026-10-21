# rtrvr-bulk-9router

<p align="center">
  <img src="brand/logo.svg" alt="rtrvr-bulk-9router" width="560">
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-3ddc97?style=for-the-badge" alt="MIT"></a>
  <img src="https://img.shields.io/badge/node-%3E%3D18-0ea5e9?style=for-the-badge&logo=node.js&logoColor=white" alt="Node 18+">
  <img src="https://img.shields.io/badge/dependencies-0-3ddc97?style=for-the-badge" alt="Zero dependencies">
  <img src="https://img.shields.io/badge/9Router-openai--compatible-7c3aed?style=for-the-badge" alt="9Router compatible">
  <img src="https://img.shields.io/badge/models-10%20free-f59e0b?style=for-the-badge" alt="10 free models">
</p>

<p align="center">
  <a href="README.id.md">Bahasa Indonesia</a> ·
  <a href="README.zh.md">中文</a> ·
  <a href="README.ja.md">日本語</a> ·
  <a href="README.es.md">Español</a>
</p>

Bulk-create **Retriever AI (rtrvr.ai)** accounts from a VPS, harvest the **Firebase tokens and session cookies**,
and expose all **10 free managed models** through one OpenAI-compatible pool wired into **9Router**.

Every account starts with **100 free credits / month**. One pool, many accounts, round-robin + failover.

---

## Why this exists

rtrvr.ai hands each new account 100 free credits usable on ten managed models (GPT-6, GLM 5.3, DeepSeek V4, Inkling, MiMo).
This toolkit turns that into a normal OpenAI endpoint, so any client (Claude Code, Cursor, Cline, Copilot, OpenCode…)
can use it through 9Router like any other provider.

- **Zero dependencies** — pure Node 18+ (`fetch`, `http`, `https`). No npm install, no Playwright, no browser.
- **Pure HTTPS signup** — Firebase `signUp` + mail.tm inbox + Firebase sign-in-link exchange. Works on a headless VPS.
- **Token auto-heal** — refresh-token rotation with transparent password re-login fallback.
- **Pool adapter** — multi-account load spreading, `/health`, `/v1/pool`, `/v1/models`.
- **9Router one-liner** — `rtrvr connect` registers the provider node, provider and API key for you.

## Quick start

```bash
git clone https://github.com/0xgetz/rtrvr-bulk-9router.git
cd rtrvr-bulk-9router

node src/cli.js create --count 5      # 5 accounts + tokens + cookies -> data/accounts.json
node src/cli.js list                  # show uid / email / credits
node src/cli.js test --model glm-5.3  # single round-trip check

node src/cli.js serve --port 8790 &   # OpenAI-compatible pool
node src/cli.js connect --router http://127.0.0.1:20128 --password 123456
```

`connect` prints something like:

```json
{
  "apiBase": "http://127.0.0.1:20128/v1",
  "apiKey": "sk-...",
  "models": ["rtrvr/gpt-6-luna", "rtrvr/glm-5.3", "..."]
}
```

Then point any OpenAI client at that base URL with that key.

## CLI reference

| Command | What it does |
| --- | --- |
| `create --count N` | Create N accounts (`--domain`, `--no-verify`, `--proxy`, `--delay ms`) |
| `list` | List accounts in the pool with credits and verification state |
| `verify [--all]` | Re-run the rtrvr.ai sign-in link for accounts that missed it |
| `refresh [--all]` | Rotate Firebase refresh tokens |
| `quota` | Query live credit balance per account |
| `chat --prompt "..."` | One-off completion through the pool (`--model`, `--account`) |
| `health` | Ping every account with a tiny prompt |
| `serve --port 8790` | Start the OpenAI-compatible pool adapter |
| `connect` | Register the adapter into 9Router and mint a router key |
| `models` | Print the model catalog |
| `export --out sessions` | Write `session.json` + cookies per account |

Environment: `DATA_DIR`, `RTRVR_PROXY`, `ROUTER_URL`, `ROUTER_PASSWORD`, `ADAPTER_URL`, `PORT`, `HOST`.

## Models

| Model ID | Name | Note |
| --- | --- | --- |
| `rtrvr/gpt-6-luna` | GPT-6 Luna | default, fast |
| `rtrvr/gpt-6.1-sol` | GPT-6.1 Sol | most capable OpenAI tier |
| `rtrvr/glm-5.3-flash` | GLM 5.3 Flash | fast, vision |
| `rtrvr/glm-5.3` | GLM 5.3 | flagship, 1M context |
| `rtrvr/deepseek-v4-flash` | DeepSeek V4.1 Flash | volume, vision |
| `rtrvr/deepseek-v4-pro` | DeepSeek V4 Pro | most capable DeepSeek |
| `rtrvr/inkling-small` | Inkling Small | fast |
| `rtrvr/inkling` | Inkling | more capable |
| `rtrvr/mimo-v2.5` | MiMo V2.5 Flash | budget |
| `rtrvr/mimo-v2.5-pro` | MiMo V2.5 Pro | deep reasoning |

## HTTP API

```bash
curl $BASE/chat/completions \
  -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"rtrvr/glm-5.3","messages":[{"role":"user","content":"hi"}]}'
```

`/models`, `/chat/completions` (stream + non-stream), `/health`, `/pool`, `/pool/reload`.

## How it works

```
mail.tm inbox ──► Firebase signUp ──► sign-in link ──► idToken + refreshToken + cookies
                                                          │
                                                    accounts.json (0600)
                                                          │
                          ┌───────────────────────────────┴────────────────────────┐
                          │            pool adapter :8790 (OpenAI compatible)     │
                          └───────────────────────────────┬────────────────────────┘
                                                          │  rtrvr extensionRouter / processText
                                                          ▼
                                               rtrvr.ai managed models
```

See [STRUCTURE.md](STRUCTURE.md) for the full tree and [docs/PROTOCOL.md](docs/PROTOCOL.md) for the wire protocol.

## Security

- `data/accounts.json` is written with mode `600`. Never commit it (`.gitignore` covers `data/`, `sessions/`, `.env`).
- Tokens expire hourly; the refresh token rotates on every use — always keep the newest copy.
- Use only accounts you create. Respect rtrvr.ai terms of service and your local laws.

## License

MIT — see [LICENSE](LICENSE).
