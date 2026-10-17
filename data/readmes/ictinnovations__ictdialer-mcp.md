# ictdialer-mcp

A [Model Context Protocol](https://modelcontextprotocol.io) server for
**[ICTDialer](https://ictdialer.com)** — the cloud auto-dialer and predictive-dialer
platform from [ICT Innovations](https://ictinnovations.com). ICTDialer.com is the
hosted edition of ICTContact and runs the same engine, so this server speaks that API.

It lets an AI assistant monitor outbound campaigns — list them, check status, read
summaries and per-call results — and, only when you turn writes on, start and stop
them.

## Install

```bash
npx -y ictdialer-mcp      # no install
npm install -g ictdialer-mcp
```

Requires Node.js 18 or newer.

## Configure

| Variable | Required | Default | |
|----------|----------|---------|--|
| `ICTDIALER_BASE_URL` | yes | | Server base URL, without the `/rest` suffix, e.g. `https://your-ictdialer` |
| `ICTDIALER_USERNAME` | yes | | API account username |
| `ICTDIALER_PASSWORD` | yes | | Password for that account |
| `ICTDIALER_MCP_ALLOW_WRITE` | no | `false` | Unlock start/stop campaign (see Safety) |
| `ICTDIALER_TIMEOUT_MS` | no | `30000` | Per-request timeout |
| `ICTDIALER_TLS_INSECURE` | no | `false` | Skip TLS verification — self-signed test servers only |

### Claude Desktop example

```json
{
  "mcpServers": {
    "ictdialer": {
      "command": "npx",
      "args": ["-y", "ictdialer-mcp"],
      "env": {
        "ICTDIALER_BASE_URL": "https://your-ictdialer",
        "ICTDIALER_USERNAME": "admin",
        "ICTDIALER_PASSWORD": "your-password"
      }
    }
  }
}
```

## Tools

Read tools are always available:

| Tool | What it does |
|------|--------------|
| `ictdialer_list_campaigns` | List campaigns (id and name) |
| `ictdialer_campaign_status` | Live status of a campaign (running, stopped) |
| `ictdialer_campaign_summary` | Totals: answered, failed, human vs machine |
| `ictdialer_campaign_result` | Per-call results (contact, response, AMD, DNC) |

Write tools appear only when `ICTDIALER_MCP_ALLOW_WRITE=true`:

| Tool | What it does |
|------|--------------|
| `ictdialer_start_campaign` | Launch a campaign — begins live outbound calling |
| `ictdialer_stop_campaign` | Stop a running campaign |

## Safety

The server is **read-only by default**. Starting a campaign begins live outbound
calling and can cost real money, so `ictdialer_start_campaign` and
`ictdialer_stop_campaign` are not registered at all unless you set
`ICTDIALER_MCP_ALLOW_WRITE=true`.

## How it connects

ICTDialer exposes a form-encoded RPC API at `{base}/rest/<Method>`. Each call carries
the account username and password; the server sends those for you. There is no separate
token to provision.

## About

Built by Tahir Almas at [ICT Innovations](https://ictinnovations.com) — the team behind
ICTDialer, ICTContact, ICTBroadcast, ICTFax and ICTPBX. Learn more at
[ictdialer.com](https://ictdialer.com).

MIT licensed. Issues and PRs welcome at
[github.com/ictinnovations/ictdialer-mcp](https://github.com/ictinnovations/ictdialer-mcp).
