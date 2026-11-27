<div align="center">

# 🤖 netcup-mcp

### Drive your netcup infrastructure from any AI assistant — via the Model Context Protocol

[![CI](https://github.com/fullya99/netcup-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/fullya99/netcup-mcp/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](#-license)
[![MCP](https://img.shields.io/badge/Model%20Context%20Protocol-server-7C3AED.svg)](https://modelcontextprotocol.io)

*"Snapshot web01, then power it off." — let Claude (or any MCP client) operate your netcup VPS fleet, safely and with **full** API coverage.*

[Install](#-install) · [Authenticate](#-authenticate-once) · [Configure](#-configure-your-client) · [Tools](#-tools)

</div>

---

A [Model Context Protocol](https://modelcontextprotocol.io) server that exposes the
[netcup Server Control Panel (SCP)](https://www.netcup.com/) REST API to AI assistants —
Claude Desktop, Claude Code, and any MCP-compatible client.

Built on the shared **[`netcup-api`](https://github.com/fullya99/netcup-cli)** core library, so
the CLI and this server always agree on auth, base URLs and the endpoint catalog.

## ✨ Highlights

|  | |
|---|---|
| 🧰 **Curated tools** | Clear, typed tools for daily ops — servers, snapshots, rDNS, firewall, tasks, metrics. |
| 🌐 **Every endpoint** | A universal trio (`list_endpoints` / `describe_endpoint` / `call_endpoint`) reaches *any* operation by id. |
| 🔮 **Future-proof** | New netcup endpoints become available after `netcup spec update` — no code change. |
| 🔐 **Shared, safe auth** | Reuses the CLI's offline refresh token; never does interactive login; errors are returned, not thrown. |
| 🧩 **One tool per endpoint** | Optional full expansion with `NETCUP_MCP_ALL_TOOLS=1`. |

## 📦 Install

```bash
pip install netcup-mcp          # pulls in netcup-api automatically
```

## 🔑 Authenticate (once)

The server never does interactive login — it reuses the credentials written by the CLI.
Authenticate once:

```bash
pip install netcup-api
netcup auth login               # OAuth2 device flow; stored in ~/.config/netcup-api/
```

## ⚙️ Configure your client

Run it directly to test (`netcup-mcp` speaks MCP over stdio), or wire it into your assistant:

### Claude Desktop / Claude Code

```json
{
  "mcpServers": {
    "netcup": {
      "command": "netcup-mcp",
      "env": {
        "NETCUP_CONFIG_DIR": "/home/youruser/.config/netcup-api"
      }
    }
  }
}
```

> [!TIP]
> Add `"NETCUP_MCP_ALL_TOOLS": "1"` to `env` to expose **every** API endpoint as its own tool.

## 🧰 Tools

| Tool | Purpose |
|------|---------|
| `netcup_whoami` · `netcup_ping` · `netcup_maintenance` | identity & health |
| `netcup_list_servers` · `netcup_get_server` | inventory |
| `netcup_set_server_state` | power **ON** / **OFF** / **SUSPENDED** |
| `netcup_list_snapshots` · `netcup_create_snapshot` · `netcup_revert_snapshot` · `netcup_delete_snapshot` | snapshots |
| `netcup_get_rdns` · `netcup_set_rdns` | reverse DNS |
| `netcup_list_ssh_keys` · `netcup_list_firewall_policies` | keys & firewall |
| `netcup_list_tasks` · `netcup_get_task` | async tasks |
| `netcup_server_metrics` · `netcup_list_interfaces` | metrics & networking |
| 🌟 `netcup_list_endpoints` · `netcup_describe_endpoint` · `netcup_call_endpoint` | **universal access to all endpoints** |

## 🔒 Safety on production infra

This operates **live** infrastructure. Destructive tools (`netcup_set_server_state`,
`netcup_revert_snapshot`, `netcup_delete_snapshot`, and any destructive `netcup_call_endpoint`)
should be confirmed with you before the assistant runs them — set up your client's approval
prompts accordingly.

## 🛠️ Development

```bash
pip install -e ../netcup-cli      # the netcup-api core
pip install -e ".[dev]"
ruff check .                      # lint
pytest -q                         # offline tests
```

See [`CLAUDE.md`](./CLAUDE.md) for the tool model, hard constraints, and contribution rules.

> [!NOTE]
> Until `netcup-api` is on PyPI, CI resolves it via the repo variable `NETCUP_API_GIT`
> (set it to the `netcup-cli` git URL). See [`CLAUDE.md`](./CLAUDE.md).

## 📄 License

[MIT](https://opensource.org/licenses/MIT) © Antoine Chenais

<div align="center"><sub>Not affiliated with netcup GmbH. Use at your own risk on production infrastructure.</sub></div>
