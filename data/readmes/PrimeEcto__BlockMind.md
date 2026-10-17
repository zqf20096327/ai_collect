<p align="center">
  <img src="assets/banner.svg" alt="BlockMind — universal Minecraft server control: one dashboard for hosted and self-hosted servers, with optional MCP access for AI agents" width="100%">
</p>

# BlockMind

**Open-source MCP (Model Context Protocol) connectors that let an AI agent manage your Minecraft server** — read console logs, edit files, change startup settings, start/stop/restart, and debug crashes, all from chat. Works with Claude Code, Claude Desktop, Cline, Cursor, VS Code, Codex, and any other MCP-compatible client. The same connectors power the hosted [BlockMind Minecraft server dashboard](https://www.blockmind.online) — one panel for every supported host plus self-hosted servers.

There are two ways to use BlockMind:

| | What you do | Best for |
|---|---|---|
| **[Use the site](https://www.blockmind.online)** (recommended) | Create a free account, connect your hosts once, and go. The connectors are already deployed, maintained, and metered for you. | Almost everyone — no setup, no deploys. |
| **Self-host the connectors** | Deploy your own Cloudflare Workers from [`worker/`](worker/) in this repo. | People who want the MCP layer on their own infrastructure. |

This repo exists so people can check out and test the BlockMind MCP code themselves. The production workers are deployed straight to Cloudflare via `wrangler`; this repo mirrors that code but is not part of the deployment path.

## The easy way: [the hosted dashboard](https://www.blockmind.online)

1. **Create a free account** — free forever, no card: 3 connected servers and 5,000 weighted AI operations per month.
2. **Connect your hosts once** — paste each provider API key; it is tested, encrypted at rest (AES-256-GCM), and your servers are discovered automatically.
3. **See every server in one dashboard** — status, players, CPU, memory, console, files, and guarded power controls across all your providers. No more logging into five different panels.
4. **Connect your AI client** — create a revocable `bm_` token in the dashboard and paste the generated config into your AI client. Provider keys never enter the AI client; it only ever sees the revocable token.

Dashboard reads go directly from the site to your host and **never** consume AI operations — only AI calls through the metered proxy do. Destructive actions (stop, delete, config changes) always require explicit confirmation, whether a human or an agent presses the button.

## What your AI agent can do

**Read-only (safe):** `list_servers`, `get_server`, `get_server_resources`, `get_console_logs`, `list_files`, `read_file`, `download_file`, `get_startup_variables`

**Guarded (mutating):** `send_command`, `power_action`, `write_file`, `upload_file`, `move_file`, `delete_files`, `update_startup_variable`

The exact tool set depends on your host's API — the table below shows the count per host. Multicraft-based hosts have no HTTP file API, so file tools are absent there; use the panel's FTP/SFTP for file edits.

## Supported hosts — 18 and counting

| Host | Panel / API | MCP tools |
|---|---|---|
| PebbleHost | Pterodactyl | 15 |
| BisectHosting | Starbase (Pterodactyl-compatible) | 15 |
| exaroton | exaroton API | 9 |
| Apex Hosting | Multicraft | 8 |
| Shockbyte | Multicraft | 8 |
| DatHost | DatHost REST API | 10 |
| Nitrado | NitrAPI | 12 |
| GGServers | Pterodactyl | 15 |
| SparkedHost | Pterodactyl | 15 |
| WiseHosting | Pterodactyl | 15 |
| WitherHosting | Pterodactyl | 15 |
| SimpleGameHosting | Pterodactyl | 15 |
| RocketNode | Pterodactyl | 15 |
| Godlike.host | Pterodactyl | 15 |
| DedicatedMC | Pterodactyl | 15 |
| KineticHosting | Pterodactyl | 15 |
| Cybrancee | Pterodactyl | 15 |
| Mintservers | Pterodactyl | 15 |
| **BlockMind Agent** (self-hosted) | Your own PC or VPS | 15 |

Hosted MCP endpoints follow `https://blockmind-<providerId>.blockmindmcp.workers.dev/mcp` (PebbleHost: `https://pebblehost-mcp.blockmindmcp.workers.dev/mcp`).

Not supported: **Aternos** (its terms of service forbid automated access — exaroton comes from the same team with an official API) and **ScalaCube** (no public API).

Curious why? Our [hosting panel API research](https://www.blockmind.online/research/minecraft-hosting-apis) documents which panels expose a real HTTP API, which forbid automation, and the Multicraft signature gotcha.

## How it works

```
your AI agent ──HTTPS──▶ Cloudflare Worker (stateless) ──HTTPS──▶ host's panel API
       ▲                              │
       └──────── MCP tool calls ──────┘   your API key passes through and is forgotten
```

- `worker/src/provider-context.ts` — selects the panel adapter from env vars
  (`PANEL_TYPE`: `pterodactyl` | `exaroton` | `multicraft` | `dathost` | `nitrado`).
- `worker/src/pterodactyl-client.ts` — Pterodactyl client API (plus BisectHosting's
  Starbase file-endpoint quirks).
- `worker/src/exaroton-client.ts` — exaroton REST API client.
- `worker/src/multicraft-client.ts` — Multicraft HTTP API client (HMAC-SHA256 signature).
- `worker/src/dathost-client.ts` / `worker/src/nitrado-client.ts` — DatHost and Nitrado REST clients.
- `worker/src/direct-client.ts` — the self-hosted BlockMind Agent path (your PC or VPS).
- `worker/src/relay-*.ts` — the encrypted relay switchboard for the self-hosted agent.
- `worker/src/tools/*` — MCP tool definitions + handlers per adapter.

Every connector is stateless: no database, no account system. Your provider API key is sent with each request by your AI client and forgotten immediately after. For self-hosted servers, the BlockMind Agent app connects outbound through the encrypted relay — no port forwarding, and your files stay on your machine.

## Self-hosting the connectors

```bash
git clone https://github.com/PrimeEcto/BlockMind.git
cd BlockMind/worker
npm install
npm run dev        # http://localhost:8787 — connect any MCP client to /mcp
```

Local dev accepts `Authorization: Bearer <your host panel API key>` (a `ptlc_…` client key for Pterodactyl panels). Multicraft hosts additionally need the panel username in the `X-Multicraft-User` header.

```bash
# deploy one worker per host (hosts are [env.<host>] blocks in wrangler.toml):
npx wrangler deploy            # PebbleHost (top-level config)
npx wrangler deploy --env exaroton
npx wrangler deploy --env apexhosting
# ...one deploy per provider you want
```

- **Multicraft hosts** (Apex, Shockbyte) authenticate with a panel username **and** an API key: the username travels in the `X-Multicraft-User` header (configurable via `API_USER_HEADER`), the key in `Authorization: Bearer <key>`. Requests missing either get a clear 401.
- **The relay** (`[env.relay]`) is a separate dedicated worker for the self-hosted BlockMind Agent — its own entry point, Durable Object binding, and `/ws` + `/v1/*` routes. It is never bundled into the per-provider MCP workers.
- Worker tests include fixed HMAC-SHA256 signature vectors for Multicraft (`npm test`); if you change the signature logic, update the vectors.

## Disclaimer

BlockMind is not affiliated with Mojang, Microsoft, or any hosting provider. Minecraft is a trademark of Mojang Synergies AB. Provider API keys are supplied by you, used per request, and never stored by the workers. Configs are generated in the browser on the site; keys never touch the server.
