# ictcontact-mcp

A [Model Context Protocol](https://modelcontextprotocol.io) server for
**[ICTContact](https://ictcontact.com)** and its hosted edition
**[ICTDialer.com](https://ictdialer.com)** — the same contact-center engine from
[ICT Innovations](https://ictinnovations.com).

It lets an AI assistant monitor outbound campaigns — list them, check status,
read summaries and per-call results — and, only when you turn writes on, start
and stop them.

## Install

```bash
npx -y ictcontact-mcp      # no install
npm install -g ictcontact-mcp
```

Requires Node.js 18 or newer.

## Configure

| Variable | Required | Default | |
|----------|----------|---------|--|
| `ICTCONTACT_BASE_URL` | yes | | Server base URL, without the `/rest` suffix, e.g. `https://your-ictcontact` |
| `ICTCONTACT_USERNAME` | yes | | API account username |
| `ICTCONTACT_PASSWORD` | yes | | Password for that account |
| `ICTCONTACT_MCP_ALLOW_WRITE` | no | `false` | Unlock start/stop campaign (see Safety) |
| `ICTCONTACT_TIMEOUT_MS` | no | `30000` | Per-request timeout |
| `ICTCONTACT_TLS_INSECURE` | no | `false` | Skip TLS verification — self-signed test servers only |

### Claude Desktop example

```json
{
  "mcpServers": {
    "ictcontact": {
      "command": "npx",
      "args": ["-y", "ictcontact-mcp"],
      "env": {
        "ICTCONTACT_BASE_URL": "https://your-ictcontact",
        "ICTCONTACT_USERNAME": "admin",
        "ICTCONTACT_PASSWORD": "your-password"
      }
    }
  }
}
```

## Tools

Read tools are always available:

| Tool | What it does |
|------|--------------|
| `ictcontact_list_campaigns` | List campaigns (id and name) |
| `ictcontact_campaign_status` | Live status of a campaign (running, stopped) |
| `ictcontact_campaign_summary` | Totals: answered, failed, human vs machine |
| `ictcontact_campaign_result` | Per-call results (contact, response, AMD, DNC) |

Write tools appear only when `ICTCONTACT_MCP_ALLOW_WRITE=true`:

| Tool | What it does |
|------|--------------|
| `ictcontact_start_campaign` | Launch a campaign — begins live outbound calling |
| `ictcontact_stop_campaign` | Stop a running campaign |

## Safety

The server is **read-only by default**. Starting a campaign begins live outbound
calling and can cost real money, so `ictcontact_start_campaign` and
`ictcontact_stop_campaign` are not registered at all unless you set
`ICTCONTACT_MCP_ALLOW_WRITE=true`.

## How it connects

ICTContact and ICTDialer expose a form-encoded RPC API at `{base}/rest/<Method>`.
Each call carries the account username and password; the server sends those for
you. There is no separate token to provision.

## About

Built by Tahir Almas at [ICT Innovations](https://ictinnovations.com) — the team
behind ICTContact, ICTDialer, ICTBroadcast, ICTFax and ICTPBX. Learn more at
[ictcontact.com](https://ictcontact.com) and [ictdialer.com](https://ictdialer.com).

MIT licensed. Issues and PRs welcome at
[github.com/ictinnovations/ictcontact-mcp](https://github.com/ictinnovations/ictcontact-mcp).
