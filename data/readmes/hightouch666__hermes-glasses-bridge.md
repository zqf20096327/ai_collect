# Hermes Glasses Bridge

**中文** → [README.zh-CN.md](README.zh-CN.md)

Let smart glasses (voice-assistant hardware) hand work off to *your own* server running [Hermes Agent](https://hermes-agent.nousresearch.com/docs).

You say *"Hermes, turn this week's notes into a report"* → the glasses instantly read back a task ID → the **real Hermes agent** on your server (with its memory, persona and full toolset) does the work in the background → the result is pushed straight to your phone. Want progress? Ask the glasses *"is Hermes done yet?"*.

It also handles **photo hand-off**: have the glasses take a picture and pass it to Hermes. The glasses only ever return a *public URL* — the adapter downloads it locally and hands the file to Hermes' vision tool.

---

## Why this exists

Two hard constraints shaped the whole design:

1. **MCP calls from the glasses time out.** Agent work routinely takes tens of seconds to minutes. Waiting synchronously means guaranteed failure.
2. **Glasses hardware cannot speak up on its own** — it only answers when asked. So results must be pushed to the phone; the glasses fetch them later when the user asks.

The governing principle is therefore: **accept fast, finish slowly.**

## Architecture

```
glasses (voice) → glasses-side Skill → [MCP / HTTPS] → queue server (VPS)
                                                          ↓ long-poll
                                        adapter (machine hosting Hermes) → hermes -z "<user's words>"
                                                          ↓
                                       result written back to queue + pushed to the user's phone
```

Full data flow, the five design invariants, and the database schema → [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

## Layout

```
vps-server/          Queue server (deploy on a VPS / any machine with a public IP)
  server.py            FastMCP + SQLite persistent queue, single file, no external services
  .env.example         Config template
  hermes-glasses-bridge.service      systemd unit
  nginx.conf           nginx reverse proxy + Bearer auth (TLS termination)
  requirements.txt

hermes-adapter/      Adapter (MUST run on the machine that hosts Hermes)
  adapter.py           long-poll → download images → run `hermes -z` → report back + notify
  config.example.json  Config template
  hermes-glasses-bridge-adapter.service   systemd user unit

glasses-skill/       Glasses-side Skill (pure prompt layer, import into the platform)
  SKILL.md             intent routing, failure wording, worked examples
  tool_schema.json     tool definitions, ready to import

docs/
  ARCHITECTURE.md      architecture / data flow / design invariants
  DEPLOY.md            step-by-step deployment (Chinese, with verification commands)
  DEPLOY.en.md         step-by-step deployment (English)
  PITFALLS.md          the pitfall list — read this first

LICENSE              MIT license text
NOTICE.md            upstream attribution (what we kept vs. what we changed)
```

## Quick start

Three steps, each with a verification command (full detail in [docs/DEPLOY.en.md](docs/DEPLOY.en.md)):

```bash
# Step 1 — bring up the queue server on your VPS
cd vps-server && cp .env.example .env && chmod 600 .env
#   → edit .env: MCP_PUBLIC_BASE / MCP_AUTH_TOKEN / MCP_ALLOWED_HOSTS
#   → set up nginx.conf (replace __MCP_AUTH_TOKEN__ with the same token)
#   → verify: curl -sk https://<your-domain>/health
#             expect {"status":"ok",...,"adapter_online":false}

# Step 2 — bring up the adapter on the machine hosting Hermes
cd hermes-adapter && cp config.example.json config.json && chmod 600 config.json
#   → edit config.json: base_url / token / hermes_bin / notify_target
#   → verify: python3 adapter.py
#             log shows "Hermes 桥 adapter 启动"; re-check /health on the VPS
#             expect "adapter_online":true

# Step 3 — import the glasses-side Skill into the platform
#   → replace {{MCP_ID}} in SKILL.md with the tool prefix the platform gives you
#   → MCP server URL: https://<your-domain>/mcp  (do NOT append /mcp twice)
#   → refresh tools, run each one once to debug, then publish
```

## Prerequisites

- A **server with a public IP** (queue server + nginx + TLS certificate). Any VPS works.
- A **machine running Hermes Agent** (the adapter lives here, because it shells out to `hermes`).
- A **domain + HTTPS certificate** (the glasses platform requires HTTPS; use acme.sh or certbot, both free).
- **AI glasses plus a platform account.** This is implemented against the Qianwen AI Hardware platform's MCP spec; any platform that supports streamable HTTP MCP works the same way.

## Security notes

- The queue server **binds to 127.0.0.1 only**; nginx terminates TLS and enforces Bearer auth. **Never expose port 16325 to the internet.**
- `.env` and `config.json` both hold plaintext tokens. Keep them `chmod 600` and **never commit them** (already covered by `.gitignore`).
- The result detail page `/task/<id>/<token>` is guarded by a one-time random token. It is designed to be shareable with a person, but do not post it publicly.
- On the platform side, **give every tool parameter a default value**. The platform's debug page pre-fills every field (strings become empty, numbers become 0, booleans take their schema default); any `required` field makes the debugger fail with "missing required parameter" — which users cannot fix. See [docs/PITFALLS.md](docs/PITFALLS.md).

## Pitfalls

The genuinely valuable part of this project → [docs/PITFALLS.md](docs/PITFALLS.md)

Covered there: the platform filling in every parameter and causing unintended actions, a duplicated `/mcp` in the URL yielding zero tools, the glasses claiming *"I already sent it to Hermes"* when no call was ever made, and trailing full-width punctuation being swallowed into image URLs.

## License and provenance

MIT. The queue server is derived from [hange3514/xiaolongxia-glasses-bridge](https://github.com/hange3514/xiaolongxia-glasses-bridge) (MIT).
We kept its SQLite persistent queue, claim + lease + heartbeat, retry-and-redispatch, attachment
round-trip and result detail page; we replaced the agent runner (OpenClaw → a real Hermes agent),
the adapter (Windows program → a Python adapter on the Hermes host), and the push transport
(Bark → pluggable notification via `hermes send`), and added the image pipeline.

See [LICENSE](LICENSE) for the license text and [NOTICE.md](NOTICE.md) for the detailed, line-by-line attribution.
