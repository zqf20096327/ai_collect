# n8meter

**Know exactly what your n8n AI workflows cost.** n8meter reads token usage out of your n8n executions, prices it against a daily-updated catalog of 2,500+ models, and shows the bill per workflow, per client and per day — on your own machine.

> n8meter is an independent community project and is not affiliated with or endorsed by n8n GmbH.

[![CI](https://github.com/bekkooazar/n8meter/actions/workflows/ci.yml/badge.svg)](https://github.com/bekkooazar/n8meter/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## Quick start

```bash
git clone https://github.com/bekkooazar/n8meter.git
cd n8meter
npm install
npm start
```

Open <http://localhost:4780>. The Settings page opens by itself on a fresh install — paste your n8n URL and an API key (n8n → Settings → n8n API → *Create an API key*), hit **Save & test connection**, and the first numbers appear within a minute.

**Docker:**

```bash
docker compose up -d
```

**Just looking?** `npm run demo` starts the dashboard with sample data — no n8n needed.

## What it does

- **Per-workflow metering** — token usage is pulled from your executions and attributed down to the node and run. Workflows are tracked by ID, so renaming keeps history.
- **Daily price catalog** — 2,500+ models across OpenAI, Anthropic, Google, Mistral, OpenRouter, Bedrock and more, refreshed every 24 h. `-latest` aliases resolve to the newest version.
- **Clients & projects** — group workflows by who they run for; costs split automatically, unassigned spend stays visible.
- **Budgets & alerts** — global, per workflow or per client × daily, weekly or monthly. Crossing a limit fires a Slack-compatible webhook, once per window.
- **Webhook fallback** — no API access (n8n Cloud free tier)? One HTTP Request node at the end of a workflow reports usage to `POST /api/ingest`.
- **Model price index** — the full catalog is browsable at `/prices`.

## How the numbers are made

Where n8n stores provider-billed token counts, n8meter uses those exact numbers. Some LangChain nodes only report an estimate — those rows are flagged with **≈** everywhere they appear, so you always know which is which. Costs are calculated from list prices and are a planning number, not an invoice: caching discounts and batch pricing are not modeled. When in doubt, check against your provider's billing.

Models the catalog doesn't know yet are still tracked (with a visible warning) and re-priced automatically once the catalog learns them.

## Your data stays yours

- Everything lives in a SQLite file on your machine (`./data`, or `DATA_DIR`).
- **No telemetry, no call-home, no analytics.** The only outbound requests are to your own n8n instance, the public [LiteLLM price catalog](https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json), and a currency-rate service for the optional EUR display.
- Prompts and completions are never read or stored — only token counts, models and costs.
- Local and LAN addresses (`localhost`, `192.168.…`, `host.docker.internal`) work out of the box — that's where self-hosted n8n lives. If your n8meter is reachable by people who aren't its operator, set `BLOCK_PRIVATE_URLS=1` to refuse private targets and unusual ports (DNS resolved and re-validated on every redirect).

## Configuration

Everything can be set in the dashboard under **Settings**. For pre-provisioning, `.env` works too:

| Variable | Meaning | Default |
|---|---|---|
| `PORT` | dashboard port | `4780` |
| `DATA_DIR` | where SQLite + config live | `./data` |
| `N8N_URL`, `N8N_API_KEY` | pre-fill the n8n connection | — |
| `POLL_INTERVAL_SEC` | how often to check for new executions | `60` |
| `SUPABASE_URL`, `SUPABASE_ANON_KEY` | optional sign-in (see below) | off |
| `BLOCK_PRIVATE_URLS` | `1` refuses private/LAN targets — for exposed instances | off |

**Exposing n8meter beyond localhost?** Either put it behind your reverse proxy's auth, or enable the built-in optional login by pointing the two Supabase variables at a free [Supabase](https://supabase.com) project. Without either, anyone who can reach the port can see your numbers.

n8n must be storing successful executions (the default on self-hosted instances) for polling to see token data — otherwise use the webhook fallback:

```
POST http://your-n8meter:4780/api/ingest
Content-Type: application/json

{ "workflowName": "{{ $workflow.name }}", "model": "gpt-4o-mini",
  "inputTokens": 1234, "outputTokens": 567, "executionId": "{{ $execution.id }}" }
```

## Development

```bash
npm test   # unit + boot tests, no network required
```

Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Found a security issue? Please report it privately via [SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE). Prices sourced from the openly maintained LiteLLM catalog (MIT).
