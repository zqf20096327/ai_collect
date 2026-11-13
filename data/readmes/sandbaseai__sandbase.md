<p align="center">
  <a href="https://www.sandbase.ai"><img src=".github/social-preview.png" alt="SandBase: one API key, build your personal agent" width="100%"></a>
</p>

<h3 align="center">One API Key. Build Your Personal Agent.</h3>

<p align="center">
  <!-- counts:en --><b>2,000+ models &amp; APIs</b> · 500+ AI models · 2,000+ data APIs from 150+ platforms<br><b>100 free API calls / day</b> · <b>Free sandboxes</b> · <b>Free agents</b><!-- /counts:en -->
</p>

<p align="center">
  <a href="https://github.com/sandbaseai/sandbase/actions/workflows/ci.yml"><img src="https://github.com/sandbaseai/sandbase/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/sandbaseai/sandbase/actions/workflows/refresh.yml"><img src="https://github.com/sandbaseai/sandbase/actions/workflows/refresh.yml/badge.svg" alt="Catalog refreshed daily"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-blue" alt="Apache-2.0"></a>
  <a href="https://github.com/sandbaseai/sandbase/stargazers"><img src="https://img.shields.io/github/stars/sandbaseai/sandbase?style=social" alt="Stars"></a>
</p>

<p align="center">
  <a href="https://www.sandbase.ai/console"><b>Get an API key</b></a> ·
  <a href="docs/INDEX.md">All models &amp; APIs</a> ·
  <a href="docs/platforms/README.md">By platform</a> ·
  <a href="https://www.sandbase.ai/docs/">Docs</a> ·
  <a href="README.zh-CN.md">中文</a>
</p>

---

## Your personal agent in one call

Create an agent, give it a job, get the answer. Every agent can find and call any of the 2,000+ models and APIs on SandBase on its own, and it works in its own sandbox. Agents and sandboxes are free. You pay only for the models and APIs your agent uses.

```python
# pip install "git+https://github.com/sandbaseai/sandbase#subdirectory=sdk/python"
from sandbase import SandBase

sb = SandBase()  # reads SANDBASE_API_KEY

agent = sb.create_agent(
    "deepseek/deepseek-v4-flash",
    instructions="You are my research agent. Use SandBase tools for live data.",
)

reply = sb.run_agent(
    agent["id"],
    "What are people on X saying about AI agents today?",
)
print(reply["output"])
```

In our test run the agent searched for an X API, read its schema and price, called it, and answered with three real posts and their links. It took 45 seconds and needed no setup beyond the key.

<details>
<summary><b>How the agent gets its tools</b></summary>

Every new agent comes with the SandBase tools (discover, inspect, run) by default. You don't need to configure anything. If you set `mcp_connections` yourself, the list replaces the default:

```python
# add your own MCP server and keep the SandBase tools
mcp_connections=[
    {"connection_id": "builtin:sandbase", "server_label": "sandbase_builtin", "required": True},
    {"connection_id": "mcp_...", "server_label": "github", "required": True},
]

# a plain chat agent without tools
mcp_connections=[]
```

The built-in entry must use `server_label: "sandbase_builtin"`. Any other label returns `400`.
</details>

Keep the conversation going with `sb.send(reply["session_id"], "...")`. When the agent is ready, deploy it as an [HTTP Service](https://www.sandbase.ai/docs/agents/services) (`sb.invoke_service(...)`) or put it on a [Schedule](https://www.sandbase.ai/docs/agents/schedules). Agents follow the OpenAI Agents API, so the official OpenAI SDK works as well (`client.beta.agents`, [example](examples/agents/python/openai_agents.py)). TypeScript and Go have the same helpers: `runAgent` and `RunAgent`.

## What your agent gets

| | | Price |
|---|---|---|
| 🧰 **A toolkit** | 2,000+ models and APIs: LLMs, image, video and audio models, plus social, search, SEO, e-commerce and finance data from 100+ platforms | Pay as you go · **100 free API calls / day** |
| 📦 **A place to work** | An isolated sandbox for code, commands and files, compatible with the E2B SDK | **Free** |
| 🤖 **A job** | Sessions, HTTP Services and Schedules on the OpenAgentCore runtime, called through the OpenAI Agents API | **Free** |

## Pick your path

| You are | Start here |
|---|---|
| **Building a personal agent** | [The example above](#your-personal-agent-in-one-call) and the [Python](sdk/python) · [TypeScript](sdk/typescript) · [Go](sdk/go) clients |
| **Using Claude Code, Codex or Cursor** | Paste into your agent: `npm install -g @sandbaseai/cli && sandbase connect` ([CLI / MCP](https://github.com/sandbaseai/cli)) |
| **Calling a model or API from your app** | [Call the pieces directly](#call-the-pieces-directly) |
| **Running a gateway or relay** (new-api, one-api, LiteLLM) | [Relay guide](docs/guides/relay-platforms.md) and [price files](exports/) |
| **An API provider** | [Add your API](integrations/README.md) with a pull request |

## Call the pieces directly

Everything your agent uses is also available to your own code with the same key.

**Any model or API.** Every capability takes the same request: `model` plus its own fields.

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "exa/search", "query": "AI agents"}'
```

```python
sb.run("exa/search", query="AI agents")  # a data API (sync)

sb.run(                                  # a video model (async, run() waits)
    "bytedance/seedance/2.5/text-to-video",
    prompt="a cat surfing",
    duration=4,
)
```

**A sandbox.** Keep the official E2B SDK and point it at SandBase:

```python
# pip install e2b
import os
from e2b import Sandbox

os.environ["E2B_API_KEY"] = os.environ["SANDBASE_API_KEY"]
os.environ["E2B_API_URL"] = "https://sandbox.sandbase.ai"
os.environ["E2B_DOMAIN"] = "sandbox.sandbase.ai"

sbx = Sandbox.create("tpl_...", timeout=120)  # template ids: catalog/sandbox.json
print(sbx.commands.run("python3 -c 'print(40 + 2)'").stdout)
sbx.kill()
```

<details>
<summary><b>TypeScript</b></summary>

```ts
// sdk/typescript: one file, no dependencies
import { SandBase } from "@sandbaseai/sdk";

const sb = new SandBase();
const result = await sb.run("exa/search", {
  query: "AI agents",
});
```
</details>

<details>
<summary><b>Go</b></summary>

```go
import sandbase "github.com/sandbaseai/sandbase/sdk/go"

c, _ := sandbase.NewClient("") // reads SANDBASE_API_KEY
run, err := c.Run(ctx, "exa/search", sandbase.Params{
    "query": "AI agents",
})
```
</details>

<details>
<summary><b>LLMs with the OpenAI SDK</b></summary>

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.sandbase.ai/v1",
    api_key=os.environ["SANDBASE_API_KEY"],
)
client.chat.completions.create(
    model="openai/gpt-6.1-sol",
    messages=[{"role": "user", "content": "Hi"}],
)
```

The Anthropic Messages (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.
</details>

<details>
<summary><b>HTTP file (VS Code / JetBrains)</b></summary>

Open [`examples/http/sandbase.http`](examples/http/sandbase.http) and click *Send Request*. It covers sync and async runs, costs, images, video with webhooks, LLMs, Agents and sandbox templates.
</details>

## What's inside

<!-- inside:en -->
| | Count | Includes |
|---|---|---|
| **AI models** | 500+ | 100+ LLMs, 150+ video, 150+ image, 30+ audio: Alibaba, Google, OpenAI, Kling, ByteDance, MiniMax, Black Forest Labs, xAI, … |
| Social & content | 1,200+ | Douyin, TikTok, Instagram, Xiaohongshu, Weibo, YouTube, Zhihu, Bilibili, Kuaishou, LinkedIn, … |
| Search, SEO & web data | 200+ | DataForSEO, Google, Similarweb, Brave, Bing, DuckDuckGo, Firecrawl, Artificial Analysis, Exa, Scholar, … |
| E-commerce, apps & reviews | 150+ | 1688, Amazon, GetApp, Google Maps, Taobao, TikTok Shop, Clutch, Google Play, JD.com, Trustpilot, … |
| Finance, crypto & markets | 150+ | Polymarket, FRED, Financial Datasets, CoinGecko, Nasdaq, MarketBeat, SECForm4, StockAnalysis, Yahoo Finance, Kalshi, … |
| Companies, people & jobs | 40+ | Web3.career, Apollo, Levels.fyi, Y Combinator, Wellfound, Crunchbase, Glassdoor, Hunter, Indeed, Built In, … |
| More | 150+ | Semrush, IMDb, AAA, Open-Meteo, Tendata, Finviz, Google Hotels, Naver, Foreplay, Google Flights, … |
<!-- /inside:en -->

Every entry has a page with its schema, price and code in four languages. See [all models &amp; APIs](docs/INDEX.md) or [browse by platform](docs/platforms/README.md): [TikTok](docs/platforms/tiktok.md) · [Instagram](docs/platforms/instagram.md) · [YouTube](docs/platforms/youtube.md) · [LinkedIn](docs/platforms/linkedin.md) · [Reddit](docs/platforms/reddit.md) · [Douyin](docs/platforms/douyin.md) · [Xiaohongshu](docs/platforms/xiaohongshu.md) · [DataForSEO](docs/platforms/dataforseo.md) · [Polymarket](docs/platforms/polymarket.md) · [OpenAI](docs/platforms/openai.md) · [Google](docs/platforms/google.md) · [Kling](docs/platforms/kwaivgi.md)

## Pricing

Every model record in `catalog/models/<name>.json` has a structured `pricing` field. If the price depends on parameters, a precomputed price table shows the cost before you call:

```jsonc
// catalog/models/openai/gpt-image-2.5-flare.json → pricing.price_examples
{ "params": { "quality": "low",  "resolution": "1k" }, "usd": 0.01 }
{ "params": { "quality": "high", "resolution": "2k" }, "usd": 0.15 }
{ "params": { "quality": "max",  "resolution": "4k" }, "usd": 1 }
```

- **Free:** sandboxes, Agents, and 100 data-API calls per organization per day (resets 00:00 UTC).
- **Pay as you go:** everything else, at the list price in USD. Failed calls are not charged.
- **Actual cost of a run:** `sb.cost(id)` or `GET /v1/tasks/{id}/cost`.
- **Price history:** the catalog refreshes daily, so `git log -p catalog/` shows every price change.

<details>
<summary><b>Pricing models</b></summary>

| `pricing.model` | Meaning |
|---|---|
| `per_call` | Flat price per successful call |
| `per_token` | `per_million_tokens.input / output`, plus cache multipliers |
| `formula` | Depends on parameters; see `price_examples` and `reference_price` |
| `usage_based` | Metered per call; `reference_price` is typical |
| `free` | No charge |
</details>

<details>
<summary><b>Sync, async and errors</b></summary>

- **sync:** `POST /v1/run` returns `200` with `status: "completed"` and the result in `output` / `outputs`.
- **async:** `POST /v1/run` returns `{"id", "status": "pending"}`. Poll `GET /v1/run/{id}`, or pass `webhook_url` (image, video, audio).
- Only send a `mode` listed in the model record. Unsupported modes return `400`.
- `400` invalid input (checked against `input_schema` before any charge) · `401` bad key · `402` insufficient balance · `429` rate or free-quota limit.
</details>

<details>
<summary><b>Repository layout</b></summary>

| Path | Contents |
|---|---|
| `catalog/index.json` | Every model and API: name, type, modes, endpoint, price summary |
| `catalog/models/<name>.json` | Full record: description, `input_schema`, output schema, modes, pricing, examples |
| `catalog/skills.json`, `catalog/sandbox.json` | Public Skills; sandbox connection settings and templates |
| `docs/` | One page per model and per platform, with code in four languages |
| `openapi/sandbase.openapi.json` | OpenAPI 3.1. Import it into Postman, Apifox, gateways or SDK generators |
| `sdk/python`, `sdk/typescript`, `sdk/go` | Dependency-free clients for models, APIs and Agents |
| `examples/` | `.http`, curl, sandboxes (E2B), Agents (OpenAI SDK) |
| `exports/` | Price and model files for new-api / one-api, LiteLLM, OpenRouter-format tools, and CSV |
| `llms.txt` | A map of this repository for AI assistants |
</details>

<details>
<summary><b>FAQ</b></summary>

**Is SandBase OpenAI-compatible?** Yes. Chat Completions, Responses and the Agents API work with the official OpenAI SDKs at `https://api.sandbase.ai/v1`.

**Can I keep my E2B code?** Yes. Change `E2B_API_KEY`, `E2B_API_URL` and `E2B_DOMAIN`.

**How do I get TikTok, Instagram, YouTube, Douyin or Xiaohongshu data?** Find the endpoint on its [platform page](docs/platforms/README.md) and call `POST /v1/run` with its `model` name. You don't need an account with each platform.

**What is free?** Sandboxes, Agents, and 100 data-API calls a day.

**Can AI coding agents use this?** Yes. [SandBase CLI / MCP](https://github.com/sandbaseai/cli) connects Claude Code, Codex, Cursor and 22 more. AI assistants can also read [`llms.txt`](llms.txt).
</details>

## Add your API

API owners can propose an integration with a pull request under [`integrations/`](integrations/README.md). CI validates it, a maintainer reviews it, and merging starts an automated rollout to every SandBase key.

## Contributing

Found a wrong field or price? Open a [catalog issue](../../issues/new?template=catalog-issue.yml). SDK and example pull requests are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md). If SandBase saves you an integration, a ⭐ helps others find it.

Code is licensed under [Apache-2.0](LICENSE). For the catalog data, see [NOTICE.md](NOTICE.md).
