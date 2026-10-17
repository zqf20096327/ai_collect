# ictpbx-mcp

A [Model Context Protocol](https://modelcontextprotocol.io) server for
**[ICTPBX](https://ictpbx.com)**, the multi-tenant, white-label IP-PBX built on the
ICTCore framework by [ICT Innovations](https://ictinnovations.com).

It lets an AI assistant read your PBX state — extensions, DID numbers, SIP trunk
providers, tenants and live statistics — over the ICTCore REST API. It is
**read-only**: it never places a call or changes configuration.

## Install

```bash
npx -y ictpbx-mcp      # no install
npm install -g ictpbx-mcp
```

Requires Node.js 18 or newer.

## Configure

| Variable | Required | Default | |
|----------|----------|---------|--|
| `ICTPBX_BASE_URL` | yes | | ICTCore REST base, normally ending in `/api`, e.g. `https://your-ictpbx/api` |
| `ICTPBX_USERNAME` | yes | | API account email (ICTCore logs in by email) |
| `ICTPBX_PASSWORD` | yes | | Password for that account |
| `ICTPBX_TIMEOUT_MS` | no | `30000` | Per-request timeout |
| `ICTPBX_TLS_INSECURE` | no | `false` | Skip TLS verification — self-signed test servers only |

### Claude Desktop example

```json
{
  "mcpServers": {
    "ictpbx": {
      "command": "npx",
      "args": ["-y", "ictpbx-mcp"],
      "env": {
        "ICTPBX_BASE_URL": "https://your-ictpbx/api",
        "ICTPBX_USERNAME": "admin@example.com",
        "ICTPBX_PASSWORD": "your-password"
      }
    }
  }
}
```

## Tools

| Tool | What it does |
|------|--------------|
| `ictpbx_pbx_statistics` | Counts of extensions, devices, ring groups, queues, IVRs, voicemails, conferences, gateways |
| `ictpbx_list_extensions` | SIP extensions with username, name, tenant |
| `ictpbx_list_dids` | DID (inbound) numbers, active state and tenant |
| `ictpbx_list_providers` | SIP trunk providers (upstream carriers) |
| `ictpbx_list_tenants` | Tenants (customer organizations) on the PBX |

## How it connects

ICTPBX runs on ICTCore, which authenticates with a JWT from `POST /authenticate`
(login by email) and reads it back from the `Authorization: Bearer` header. The
server fetches the token on first use and refreshes it automatically.

## About

Built by Tahir Almas at [ICT Innovations](https://ictinnovations.com) — the team
behind ICTPBX, ICTContact, ICTDialer, ICTFax and the ICTCore framework these
products share. Learn more at [ictpbx.com](https://ictpbx.com).

MIT licensed. Issues and PRs welcome at
[github.com/ictinnovations/ictpbx-mcp](https://github.com/ictinnovations/ictpbx-mcp).
