
<div align="center">

<br />

<img src="https://img.shields.io/badge/🐾_TokenToll-Usage_Based_Billing-FF6B35?style=for-the-badge&labelColor=1a1a2e" alt="TokenToll" />

<br />
<br />

<h3>The open-source billing engine for AI & SaaS products</h3>

<p><i>Meter tokens. Enforce quotas. Invoice automatically.</i></p>

<br />

<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="License: MIT" /></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" /></a>
<a href="https://fastapi.tiangolo.com/"><img src="https://img.shields.io/badge/FastAPI-0.109+-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI" /></a>
<a href="https://www.typescriptlang.org/"><img src="https://img.shields.io/badge/TypeScript-5.0+-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" /></a>
<a href="https://www.mongodb.com/"><img src="https://img.shields.io/badge/MongoDB-7-47A248?style=flat-square&logo=mongodb&logoColor=white" alt="MongoDB" /></a>
<a href="https://redis.io/"><img src="https://img.shields.io/badge/Redis-7-DC382D?style=flat-square&logo=redis&logoColor=white" alt="Redis" /></a>
<a href="https://www.docker.com/"><img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" /></a>
<a href="https://stripe.com/"><img src="https://img.shields.io/badge/Stripe-Integrated-635BFF?style=flat-square&logo=stripe&logoColor=white" alt="Stripe" /></a>
<a href="http://makeapullrequest.com"><img src="https://img.shields.io/badge/PRs-Welcome-brightgreen?style=flat-square" alt="PRs Welcome" /></a>

<br />
<br />

## Star History

<a href="https://www.star-history.com/?repos=AlameerAshraf%2Ftokentoll&type=timeline&logscale=&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=AlameerAshraf/tokentoll&type=timeline&theme=dark&logscale&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=AlameerAshraf/tokentoll&type=timeline&logscale&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=AlameerAshraf/tokentoll&type=timeline&logscale&legend=top-left" />
 </picture>
</a>

**`12 AI Providers`** · **`5 Pricing Models`** · **`30+ API Endpoints`** · **`Python & Node SDKs`**

<br />

[🚀 Quick Start](#-quick-start) · [🎯 Features](#-features) · [📦 SDKs](#-sdks) · [📖 API Reference](#-api-reference) · [⚙️ Configuration](#%EF%B8%8F-configuration) · [🐳 Deployment](#-deployment) · [🤝 Contributing](#-contributing)

<br />

---

</div>

<br />

## 🐾 What is TokenToll?

> **The problem:** You're building a SaaS on top of LLMs. You need to track usage per customer, enforce quotas, support free tiers and prepaid credits, and generate invoices. Building all that from scratch takes weeks.

> **The solution:** TokenToll gives you a single API to handle all of it. Ingest usage events, define pricing in YAML, and let TokenToll compute costs, enforce limits, generate invoices, and sync to Stripe — or run fully self-hosted.

```
  ┌──────────────┐          ┌──────────────┐          ┌──────────────┐
  │              │  report  │              │  invoice │              │
  │   Your App   │────────▶ │  TokenToll   │────────▶ │   Customer   │
  │  calls LLM   │  tokens  │   API        │  auto    │   gets bill  │
  │              │          │              │          │              │
  └──────────────┘          └──────────────┘          └──────────────┘
```

<br />

## 🎯 Features

<table>
<tr>
<td width="33%" valign="top">

### 📊 Usage Metering

✅ Event ingestion via REST or SDK<br/>
✅ Idempotent (duplicate IDs ignored)<br/>
✅ Batch ingestion<br/>
✅ Multi-meter (tokens, calls, compute)<br/>

---

### 💰 Flexible Pricing

✅ **Per-unit** — `qty × rate`<br/>
✅ **Tiered** — bracket-based rates<br/>
✅ **Volume** — total determines rate<br/>
✅ **Flat** — fixed monthly fee<br/>
✅ **Prepaid** — credit deduction<br/>
✅ **Free tiers** — free allowance<br/>

</td>
<td width="33%" valign="top">

### 🔒 Quotas & Entitlements

✅ Hard limits — block at cap<br/>
✅ Soft limits — alert via webhook<br/>
✅ Budget caps — dollar spending limits<br/>
✅ Alert thresholds — 80%, 100%, etc.<br/>

---

### 🧾 Invoicing & Payments

✅ Auto monthly invoice generation<br/>
✅ Per-meter line items<br/>
✅ Stripe sync or self-hosted<br/>
✅ Prepaid credit auto-apply<br/>
✅ Invoice status tracking<br/>
✅ Retry with exponential backoff<br/>

</td>
<td width="33%" valign="top">

### 🏢 Multi-Tenancy

✅ Full tenant isolation<br/>
✅ Operator super-admin API<br/>
✅ Per-tenant API key rotation<br/>
✅ SHA-256 hashed key storage<br/>

---

### 🔔 Webhooks & Observability

✅ HMAC-SHA256 signed delivery<br/>
✅ 3 event types with auto-retry<br/>
✅ Full audit logging<br/>
✅ Event replay / reconciliation<br/>
✅ Platform analytics endpoint<br/>
✅ Rate limiting per tenant<br/>

</td>
</tr>
</table>

<br />

## 🤖 Built-in AI Provider Pricing

TokenToll ships with pre-configured cost tables for **12 providers** and **100+ models**. Pass `provider` and `model` with your events — costs are calculated automatically.

<table>
<tr>
<td align="center" width="25%"><img src="https://img.shields.io/badge/-OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" /><br/><sub>GPT-4o · o1 · o3</sub></td>
<td align="center" width="25%"><img src="https://img.shields.io/badge/-Anthropic-D4A574?style=for-the-badge&logo=anthropic&logoColor=white" /><br/><sub>Claude 4 · 3.5 · Haiku</sub></td>
<td align="center" width="25%"><img src="https://img.shields.io/badge/-Google-4285F4?style=for-the-badge&logo=google&logoColor=white" /><br/><sub>Gemini 2.5 · Flash</sub></td>
<td align="center" width="25%"><img src="https://img.shields.io/badge/-Mistral-FF7000?style=for-the-badge&logoColor=white" /><br/><sub>Large · Codestral</sub></td>
</tr>
<tr>
<td align="center"><img src="https://img.shields.io/badge/-DeepSeek-4D6BFE?style=for-the-badge&logoColor=white" /><br/><sub>V3 · R1</sub></td>
<td align="center"><img src="https://img.shields.io/badge/-Meta-0467DF?style=for-the-badge&logo=meta&logoColor=white" /><br/><sub>Llama 3 · Llama 4</sub></td>
<td align="center"><img src="https://img.shields.io/badge/-Cohere-39594D?style=for-the-badge&logoColor=white" /><br/><sub>Command R+</sub></td>
<td align="center"><img src="https://img.shields.io/badge/-Groq-F55036?style=for-the-badge&logoColor=white" /><br/><sub>LPU Inference</sub></td>
</tr>
<tr>
<td align="center"><img src="https://img.shields.io/badge/-xAI-000000?style=for-the-badge&logo=x&logoColor=white" /><br/><sub>Grok</sub></td>
<td align="center"><img src="https://img.shields.io/badge/-Perplexity-20808D?style=for-the-badge&logoColor=white" /><br/><sub>Sonar Pro</sub></td>
<td align="center"><img src="https://img.shields.io/badge/-Together_AI-6B4FBB?style=for-the-badge&logoColor=white" /><br/><sub>Open Models</sub></td>
<td align="center"><img src="https://img.shields.io/badge/-Azure_OpenAI-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white" /><br/><sub>Hosted OpenAI</sub></td>
</tr>
</table>

> [!TIP]
> Rates are YAML files in `config/provider_pricing/` — update them anytime and hot-reload without restart.

<br />

## 🏗️ Architecture

```
  ┌─────────────────┐         ┌──────────────────┐         ┌───────────────┐
  │                 │         │                  │         │               │
  │    Your App     │────────▶│   TokenToll API  │────────▶│   MongoDB     │
  │  (SDK / HTTP)   │         │   (FastAPI)      │         │               │
  │                 │         │                  │         └───────────────┘
  └─────────────────┘         └────────┬─────────┘
                                       │
                              ┌────────▼─────────┐
                              │  Redis Streams   │
                              └────────┬─────────┘
                                       │
                     ┌────────────────┼────────────────-┐
                     │                │                 │
              ┌──────▼──────┐  ┌──────▼──────┐   ┌──────▼──────┐
              │  Ingestion  │  │   Invoice   │   │   Webhook   │
              │   Worker    │  │   Worker    │   │   Worker    │
              └─────────────┘  └──────┬──────┘   └─────────────┘
                                      │
                              ┌───────▼────────┐
                              │    Stripe      │
                              │  (optional)    │
                              └────────────────┘
```

| Component | Role |
|:---|:---|
| 🌐 **API Server** | FastAPI REST API — auth, rate limiting, multi-tenant routing |
| ⚡ **Ingestion Worker** | Processes usage events, updates wallets, checks entitlements |
| 💵 **Invoice Worker** | Monthly invoice generation, Stripe sync, credit application |
| 📨 **Webhook Worker** | HMAC-signed delivery with retries to your endpoints |
| 🍃 **MongoDB** | Persistent storage — tenants, customers, events, invoices, audit logs |
| 🔴 **Redis** | Stream-based queue + per-tenant rate limiting |

<br />

## 🚀 Quick Start

> [!NOTE]
> You need Docker & Docker Compose. Stripe is optional — without it, TokenToll runs in manual invoicing mode.

### Step 1 — Start the stack

```bash
git clone https://github.com/AlameerAshraf/tokentoll.git
cd tokentoll
docker compose -f docker/docker-compose.yml up -d
```

### Step 2 — Verify it's running

```bash
curl http://localhost:8000/health | jq
# ✅ {"status": "ok", "database": "ok"}
```

### Step 3 — Create a tenant (your SaaS company)

```bash

curl -s -X POST http://localhost:8000/v1/tenants \
  -H "Content-Type: application/json" \
  -d '{"name": "My SaaS", "slug": "my-saas"}' | jq
```

### Step 4 — Generate an API key

```bash
curl -s -X POST http://localhost:8000/v1/tenants/{tenant_id}/api-keys \
  -d '{"name": "production"}' | jq

# ⚠️ Save the "key" field — shown only once!
```

### Step 5 — Create a customer & send usage

```bash
# Create customer on the "default" plan
curl -s -X POST http://localhost:8000/v1/tenants/{tenant_id}/customers \
  -H "Authorization: Bearer tt_your_key" \
  -H "Content-Type: application/json" \
  -d '{"external_id": "user_123", "plan_id": "default", "name": "Alice"}' | jq

# Report usage
curl -s -X POST http://localhost:8000/v1/events \
  -H "Authorization: Bearer tt_your_key" \
  -H "Content-Type: application/json" \
  -d '{
    "event_id": "evt_001",
    "customer_id": "user_123",
    "meter_name": "token_count",
    "quantity": 1500,
    "provider": "openai",
    "model": "gpt-4o"
  }' | jq
# ✅ {"accepted": 1, "rejected": 0, "errors": []}
```

### Step 6 — Check the balance

```bash
curl -s http://localhost:8000/v1/tenants/{tenant_id}/customers/{customer_id}/balance \
  -H "Authorization: Bearer tt_your_key" | jq
```

> [!TIP]
> For the full 14-phase walkthrough covering **every** feature with `curl`, see **[docs/full-scenario-guide.md](docs/full-scenario-guide.md)**.

<br />

## 📦 SDKs

The SDKs are **not published** to package registries. Build and use them locally from your macine or PUBLISH THEM IF YOU WANT 👍🏻 🐾.

### Build & install locally

**Python SDK**

```bash
# From repo root — editable install (changes apply immediately)
pip install -e ./packages/sdk-python
# or with uv:
uv pip install -e ./packages/sdk-python
```

**Node.js SDK**

```bash
# 1. Build the package (from repo root)
cd packages/sdk-node && npm run build

# 2. In your app, install from the local path
# If your app is inside tokentoll (e.g. apps/dashboard):
npm install ../../packages/sdk-node

# If your app is elsewhere, use an absolute or relative path:
npm install /path/to/tokentoll/packages/sdk-node

# Or add to your package.json dependencies:
# "@tokentoll/sdk-node": "file:../path/to/tokentoll/packages/sdk-node"
```

<table>
<tr>
<td width="50%" valign="top">

### 🐍 Python

```python
from tokentoll import TokenToll

client = TokenToll(
    api_key="tt_your_key",
    base_url="http://localhost:8000",
    tenant_id="your_tenant_id"
)

# 🐾 Emit usage — one line
client.emit("user_123", "token_count", 1500)

# Check balance
balance = client.get_balance("user_123")

# Gate requests on quota
result = client.check_entitlement(
    "user_123", "token_count", 1000
)
if result["allowed"]:
    # serve the request
    ...
```

</td>
<td width="50%" valign="top">

### 💚 Node.js

```typescript
import { TokenToll } from '@tokentoll/sdk-node';

const client = new TokenToll({
  apiKey: 'tt_your_key',
  baseUrl: 'http://localhost:8000',
  tenantId: 'your_tenant_id',
});

// 🐾 Emit usage — one line
await client.emit('user_123', 'token_count', 1500);

// Check balance
const balance = await client.getBalance('user_123');

// Gate requests on quota
const { allowed, remaining } =
  await client.checkEntitlement(
    'user_123', 'token_count', 1000
  );
```

</td>
</tr>
</table>

**Environment variables** (both SDKs): `TOKENTOLL_API_KEY` · `TOKENTOLL_BASE_URL` · `TOKENTOLL_TENANT_ID`

<br />

## 📖 API Reference

> [!NOTE]
> 🐾 **Interactive Swagger UI** is available at [`http://localhost:8000/docs`](http://localhost:8000/docs) when running locally.

### Core Endpoints

| | Method | Path | Auth | Description |
|:---:|:------:|:-----|:----:|:------------|
| 📤 | `POST` | `/v1/events` | Tenant | Ingest usage events (single or batch) |
| 🏢 | `POST` | `/v1/tenants` | Operator | Create a tenant |
| 🏢 | `GET` | `/v1/tenants` | Any | List tenants |
| 🏢 | `PATCH` | `/v1/tenants/{id}` | Any | Update tenant |
| 🏢 | `DELETE` | `/v1/tenants/{id}` | Any | Delete tenant (cascade) |
| 👤 | `POST` | `/v1/tenants/{id}/customers` | Tenant | Create a customer |
| 👤 | `GET` | `/v1/tenants/{id}/customers` | Tenant | List customers |
| 👤 | `PATCH` | `/v1/tenants/{id}/customers/{id}` | Tenant | Update customer / change plan |
| 👤 | `DELETE` | `/v1/tenants/{id}/customers/{id}` | Tenant | Delete customer |
| 💰 | `GET` | `.../customers/{id}/balance` | Tenant | Get usage & credit balance |
| 💰 | `POST` | `.../customers/{id}/credits` | Operator | Add prepaid credits |
| 🔒 | `POST` | `.../customers/{id}/check-entitlement` | Tenant | Check quota before serving |
| 📊 | `PUT` | `.../customers/{id}/budget` | Tenant | Set budget cap & alert thresholds |
| 📊 | `GET` | `.../customers/{id}/budget` | Tenant | Get budget |
| 📊 | `DELETE` | `.../customers/{id}/budget` | Tenant | Remove budget |
| 🧾 | `GET` | `.../customers/{id}/invoices` | Tenant | List invoices |
| 🧾 | `GET` | `/v1/tenants/{id}/invoices/{id}` | Tenant | Get single invoice |
| 🔑 | `POST` | `/v1/tenants/{id}/api-keys` | Any | Create API key |
| 🔑 | `GET` | `/v1/tenants/{id}/api-keys` | Any | List API keys |
| 🔑 | `DELETE` | `/v1/tenants/{id}/api-keys/{id}` | Any | Revoke API key |
| 🔔 | `POST` | `/v1/tenants/{id}/webhooks` | Tenant | Register webhook |
| 🔔 | `GET` | `/v1/tenants/{id}/webhooks` | Tenant | List webhooks |
| 🔔 | `PATCH` | `/v1/tenants/{id}/webhooks/{id}` | Tenant | Update webhook |
| 🔔 | `DELETE` | `/v1/tenants/{id}/webhooks/{id}` | Tenant | Delete webhook |
| 📋 | `GET` | `/v1/tenants/{id}/plans` | Tenant | List plans for tenant |

### Operator Endpoints

| | Method | Path | Description |
|:---:|:------:|:-----|:------------|
| ⚙️ | `GET` | `/v1/config/plans` | List all plan configs |
| ⚙️ | `GET` | `/v1/config/plans/{id}` | Get plan config detail |
| ⚙️ | `PUT` | `/v1/config/plans/{id}` | Create or update plan |
| ⚙️ | `DELETE` | `/v1/config/plans/{id}` | Delete plan |
| 🔄 | `POST` | `/v1/config/reload` | Hot-reload config from YAML |
| 📈 | `GET` | `/v1/analytics` | Platform-wide aggregate stats |
| ⏪ | `POST` | `/v1/tenants/{id}/replay` | Replay events to rebuild usage |
| 🤖 | `GET` | `/v1/providers` | List available provider pricing |

### Authentication

```
Authorization: Bearer tt_...       ← Recommended
X-API-Key: tt_...                  ← Alternative header
?api_key=tt_...                    ← Query parameter
```

<br />

## ⚙️ Configuration

### 📋 Plans — `config/plans/*.yaml`

```yaml
# config/plans/pro.yaml
name: pro
pricing_model: tiered
provider: openai                    # Use built-in provider rates

meters:
  token_count:
    tiers:
      - up_to: 1_000_000           # First 1M tokens
        rate: 0.0001
      - up_to: 10_000_000          # 1M – 10M tokens
        rate: 0.00008
      - up_to: null                 # 10M+ tokens
        rate: 0.00005

entitlements:
  token_count:
    hard_limit: 50_000_000          # 🛑 Block at 50M
    soft_limit: 40_000_000          # ⚠️ Alert at 40M

free_tier:
  token_count: 100_000              # 🎁 First 100K free
```

### 💲 Pricing Models

| Model | Formula | Use Case |
|:------|:--------|:---------|
| `per_unit` | `quantity × rate` | Simple token billing — $0.001/token |
| `tiered` | Rate changes per bracket | Volume discounts — cheaper at scale |
| `volume` | Total volume picks the rate | Enterprise pricing — all units at best rate |
| `flat` | Fixed fee | SaaS subscriptions — $99/month |
| `prepaid` | Deduct from credit balance | Buy $100 in credits, use until gone |

### 📏 Meters — `config/meters/*.yaml`

```yaml
name: token_count
type: token_count         # token_count | request_count | compute_time | custom
unit: tokens
```

### 🤖 Provider Pricing — `config/provider_pricing/*.yaml`

```yaml
provider: openai
currency: USD
updated_at: "2025-03-01"
models:
  gpt-4o:
    input_per_million: 2.50
    output_per_million: 10.00
  gpt-4o-mini:
    input_per_million: 0.15
    output_per_million: 0.60
```

### 🔄 Hot Reload

```bash
curl -X POST http://localhost:8000/v1/config/reload \
  -H "Authorization: Bearer $OPERATOR_KEY"

# ✅ {"reloaded": true, "plans_synced": 4, "meters_synced": 1}
```

<br />

## 🧪 Testing

TokenToll includes integration tests covering **critical billing guarantees**:

```
tests/
├── integration/
│   ├── test_ingestion_idempotency.py   ← Duplicate events never double-counted
│   └── test_tenant_isolation.py        ← Cross-tenant access blocked (403)
└── conftest.py                         ← Shared fixtures
```

| Test | What It Proves |
|:-----|:---------------|
| ✅ **Idempotency** | Same `event_id` sent twice → usage counted only once |
| ✅ **Tenant Isolation** | Tenant A cannot read Tenant B's data → returns `403` |
| ✅ **Cross-Tenant Events** | Events for another tenant's customer → rejected as `unknown_customer` |

### Run Tests

```bash
# Start dependencies
docker compose -f docker/docker-compose.yml up -d mongodb redis

# API integration tests
cd apps/api && uv run pytest -v

# Node SDK tests
cd packages/sdk-node && npm test

# Lint
cd apps/api && ruff check .
```

<br />

## 🐳 Deployment

### Docker Compose (Recommended)

```bash
STRIPE_SECRET_KEY=sk_live_... \
OPERATOR_API_KEY=your-secret \
docker compose -f docker/docker-compose.yml up -d
```

### Services

| Service | Port | Description |
|:--------|:----:|:------------|
| 🌐 `api` | `8000` | FastAPI REST API |
| ⚡ `workers` | — | Ingestion event processor |
| 💵 `invoice-worker` | — | Monthly invoice generator |
| 📨 `webhook-worker` | — | Webhook delivery with retries |
| 🖥️ `dashboard` | `5174` | React operator & customer UI |
| 🍃 `mongodb` | `27018` | Persistent storage |
| 🔴 `redis` | `6379` | Queue + rate limiting |

### Environment Variables

| Variable | Default | Description |
|:---------|:--------|:------------|
| `MONGODB_URI` | `mongodb://localhost:27017/tokentoll` | MongoDB connection |
| `REDIS_URL` | `redis://localhost:6379/0` | Redis connection |
| `STRIPE_SECRET_KEY` | *(none)* | Stripe key — omit for manual invoicing |
| `OPERATOR_API_KEY` | *(none)* | Super-admin key — omit for open bootstrap |
| `RATE_LIMIT_REQUESTS_PER_MINUTE` | `1000` | Per-tenant rate limit |
| `LOG_LEVEL` | `INFO` | Logging verbosity |
| `CONFIG_PATH` | *(auto)* | Path to `config/` directory |
| `INVOICE_INTERVAL_MIN` | `60` | Invoice worker interval (minutes) |

<br />

## 📂 Project Structure

```
tokentoll/
│
├── 🐾 apps/
│   ├── api/                          ← FastAPI REST API
│   │   └── src/
│   │       ├── main.py               ← App entry point & lifespan
│   │       ├── api/
│   │       │   ├── routes/           ← 15 route modules
│   │       │   ├── middleware/       ← Auth (API key) + Rate limiting
│   │       │   └── errors.py        ← Standardized error responses
│   │       ├── models/               ← 12 Beanie ODM document classes
│   │       ├── services/             ← 7 business logic modules
│   │       ├── adapters/             ← MongoDB, Redis, Stripe, Manual
│   │       └── config/               ← YAML loaders + JSON schemas
│   │
│   ├── workers/                      ← Background processors
│   │   └── src/workers/
│   │       ├── ingestion_worker.py   ← Usage event processing
│   │       ├── invoice_worker.py     ← Monthly billing
│   │       └── webhook_worker.py     ← Webhook delivery
│   │
│   └── dashboard/                    ← React + Vite + TypeScript
│       └── src/pages/                ← Operator & customer views
│
├── 📦 packages/
│   ├── sdk-python/                   ← Python SDK (httpx)
│   └── sdk-node/                     ← Node.js SDK (TypeScript)
│
├── ⚙️ config/
│   ├── plans/                        ← Pricing plan definitions
│   ├── meters/                       ← Meter definitions
│   └── provider_pricing/             ← 12 AI provider cost tables
│
├── 🐳 docker/
│   ├── docker-compose.yml            ← Full stack (7 services)
│   ├── Dockerfile.api
│   ├── Dockerfile.workers
│   └── Dockerfile.dashboard
│
└── 📚 docs/
    ├── full-scenario-guide.md        ← Complete HTTP walkthrough (14 phases)
    ├── video-script.md               ← Demo video script
    ├── deployment.md                 ← Production deployment
    └── testing-scenario.md           ← Test scenarios
```

<br />

## 🤝 Contributing

We welcome contributions! TokenToll is open source and community-driven.

### Dev Setup

```bash
# 1. Fork & clone
git clone https://github.com/your-username/tokentoll.git && cd tokentoll

# 2. Start dependencies
docker compose -f docker/docker-compose.yml up -d mongodb redis

# 3. Install & run API
cd apps/api && uv sync && uvicorn src.main:app --reload --port 8000

# 4. Run workers (separate terminals)
cd apps/workers && uv sync
python -m src.workers.main ingestion
python -m src.workers.main invoice
python -m src.workers.main webhook

# 5. Build SDKs (for local use in your projects — see [SDKs](#-sdks))
cd packages/sdk-python && uv sync && pip install -e .   # or: uv pip install -e .
cd packages/sdk-node && npm install && npm run build
```

### Contribution Flow

| Step | Action |
|:----:|:-------|
| 1 | 🍴 **Fork** the repo |
| 2 | 🌿 **Branch** — `git checkout -b feat/my-feature` |
| 3 | ✅ **Test** — `cd apps/api && uv run pytest -v` |
| 4 | 🧹 **Lint** — `ruff check .` |
| 5 | 📬 **PR** — open with a clear description |

<br />

## 📄 License

**MIT** — use it however you want. See [LICENSE](LICENSE) for details.

<br />

---

<div align="center">

<br />

<img src="https://img.shields.io/badge/🐾_TokenToll-Stop_building_billing._Start_shipping_products.-FF6B35?style=for-the-badge&labelColor=1a1a2e" alt="TokenToll" />

<br />
<br />

[🚀 Get Started](#-quick-start) · [📚 Read the Docs](docs/) · [🔗 View API](http://localhost:8000/docs)

<br />

Built with ❤️ for the AI developer community in Egypt 🇪🇬

<br />

</div>
