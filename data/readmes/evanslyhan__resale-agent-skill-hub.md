# SkillHub — Smart Resale Agent

A collection of 8 Claude Code skills + an **MCP Server** implementing a **Multi-Platform Smart Resale Agent**: an AI-powered conversational workflow for C2C second-hand resale that reduces the barriers to listing and selling pre-owned goods.

**v2**: Now runs as a standard MCP server (JSON-RPC over stdio) that any MCP-compatible client can call — Claude Desktop, Cursor, VS Code, or custom web frontends.

## Architecture

```
skillhub/
├── broker_core/                  # Shared engine (pip install -e .)
│   ├── session_manager.py        # Browser login → cookie persistence
│   ├── platform_client.py        # Authenticated platform API clients
│   ├── state_manager.py          # Listing lifecycle state (~/.broker/listings.json)
│   ├── scheduler.py              # launchd (macOS) / cron (Linux) registration
│   ├── audit_logger.py           # Append-only Transparency Log (~/.broker/audit.jsonl)
│   └── mcp_server.py             # ★ MCP Server — 7 tools via JSON-RPC
├── guardrails/                   # ★ Prompt framework (v2)
│   ├── Omni-Agent-Guardrails.yaml
│   └── README.md
├── skills/                       # 8 Claude Code skills
│   ├── personal-broker/          # Hub: orchestrates the 7-step pipeline
│   ├── broker-recognize/         # Step 1: Photo → product info
│   ├── broker-auth/              # Step 3: Bind platform accounts
│   ├── broker-price/             # Step 2: Authenticated price research
│   ├── broker-card/              # Step 4: Listing cards → auto-publish
│   ├── broker-schedule/          # Step 5: Repricing interval & cron/launchd
│   ├── broker-fuse/              # Step 6: Price Shield (floor price)
│   └── broker-delist/            # Step 7: Auto-detect sale → delist all
├── tests/                        # 41 tests
└── docs/                         # Setup guides for MCP clients
```

## The 7-Step Pipeline

```
📷 broker-recognize  →  Photo → structured product info
🔐 broker-auth       →  Open browser → log in once → session persisted
🔍 broker-price      →  Search platforms with session → transparency report
🛡️ broker-fuse       →  ⚠️ GLOBAL INTERCEPTOR — set unbreachable floor price BEFORE publishing
📋 broker-card       →  Generate cards → validate floor → user confirms → auto-publish
⏰ broker-schedule   →  Register launchd/cron for daily repricing checks (floor-gated)
✅ broker-delist     →  Scheduler detects sale → auto-delist all platforms (no confirmation)
```

Each skill can also be invoked standalone (e.g., `/broker-price` for pricing only).

## Prerequisites

### ANTHROPIC_API_KEY (required)

`broker-recognize` uses the **Anthropic API** (Claude Vision) to analyze product photos. Set your API key:

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

Without this key, photo recognition will fail.

### Python 3.9+

### Playwright (for platform auth)

## Quick Start

Pick one path. Path A is recommended for most users.

### Path A: Claude Desktop (recommended, 5 minutes)

**Step 1: Install**
```bash
git clone https://github.com/madguyevans-creator/skillhub.git
cd skillhub && pip install -e .
pip install playwright && playwright install chromium
```

**Step 2: Get API key (one-time)**
Go to [console.anthropic.com](https://console.anthropic.com) → API Keys → create key.
Save it once:
```bash
echo 'sk-ant-your-key' > ~/.broker/api_key
```

**Step 3: Configure Claude Desktop**
Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "skillhub": {
      "command": "python3",
      "args": ["/path/to/skillhub/broker_core/mcp_server.py"],
      "env": { "BROKER_MOCK_MODE": "true" }
    }
  }
}
```

**Step 4: Restart Claude Desktop.** Done.

Open Claude Desktop, say "帮我卖掉这双鞋" + upload photo. Claude automatically calls 7 MCP tools in the correct order.

### Path B: Claude Code CLI

```bash
git clone https://github.com/madguyevans-creator/skillhub.git
cd skillhub && pip install -e .
cp -r skills/* ~/.claude/skills/
```

Use inside Claude Code:
- `/personal-broker` — full pipeline
- `/broker-recognize` — analyze product photo
- `/broker-price` — price research
- `/broker-fuse` — set floor price

### Path C: Demo without any accounts (mock mode)

By default `BROKER_MOCK_MODE=true`. Everything works with realistic simulated data — no API key, no platform accounts needed. Photo recognition returns a demo Nike sneaker.

```bash
git clone https://github.com/madguyevans-creator/skillhub.git
cd skillhub && pip install -e .
# Done — you're in mock mode. Use Path A or B above.
```

### Going real: turn off mock mode

```bash
export BROKER_MOCK_MODE=false
# Then bind platform accounts:
python3 skills/broker-auth/scripts/auth.py --all
# This opens a browser. Log into each platform once. Cookies persist.
```

## Sandbox / Mock Mode

By default, `BROKER_MOCK_MODE=true` — all platform API calls (search, publish, delist) return realistic simulated data. No real HTTP requests are made. This allows:

- **Demo without platform accounts**: test the full pipeline with mock data
- **Safe development**: no risk of accidentally publishing or modifying real listings
- **Anti-scraping avoidance**: no requests that could trigger rate limits or CAPTCHAs

To use real platform APIs, set `BROKER_MOCK_MODE=false` in your environment. Requires platform accounts bound via `broker-auth`.

## Transparency Log

Every AI-assisted decision is recorded to `~/.broker/audit.jsonl` — an append-only, immutable JSONL file. You can always audit what the agent did and why.

**What gets logged:**
- Price research results (`log_pricing`)
- Price shield checks — blocked or passed (`log_fuse_check`)
- Listing publishes (`log_publish`)
- Auto-repricing events (`log_repricing`)
- Delist events (`log_delist`)
- Schedule registrations (`log_schedule_registered`)

**How to view:**
```python
from broker_core import audit_logger
print(audit_logger.format_trail("item_abc123"))  # Human-readable timeline
trail = audit_logger.get_audit_trail("item_abc123")  # Raw JSON array
```

When every action is recorded with rationale, there is no "black box" — the user can always audit what happened and why.

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| **Not web scraping** | Uses user's own session cookies. Searching as a logged-in user, not crawling. |
| **Bind once, reuse** | Platform login happens once via browser. Session persisted until expiry (~30 days). |
| **Sold median pricing** | Recommended price = median of actually-sold comparables. Falls back to 5% below active median. |
| **Price shield as global interceptor** | Every price-mutating action (publish, repricing) validates against the floor. Blocked actions are logged to audit trail. |
| **Auto-execute after confirm** | Once user confirms card + floor + schedule, the system auto-publishes and auto-reprices without re-confirmation. |
| **No confirmation on delist** | When scheduler detects sale on any platform, auto-delist all others immediately. |
| **launchd / cron** | System-level scheduling, no daemon process needed. |
| **Mock mode** | `BROKER_MOCK_MODE=true` by default — safe demo without real accounts or anti-scraping risk. |
| **Append-only Transparency Log** | Immutable JSONL log of every decision. The user can always audit what happened. |

## License

MIT — see [LICENSE](LICENSE)
