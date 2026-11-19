<div align="center">

![Awesome API Skills — Visual Overview](https://raw.githubusercontent.com/ashish7802/awesome-api-skills/master/media/banner.png)

# Awesome API Skills

### Structured, strictly schema-validated `SKILL.md` context specifications for AI coding agents — with transparent verification tiers, security hygiene checks, and an interconnected API knowledge graph.

<p>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="MIT License"></a>
  <img src="https://img.shields.io/badge/skills-141%20schema--validated-38bdf8?style=flat-square" alt="141 schema-validated skills">
  <img src="https://img.shields.io/badge/graph-288%20edges-818cf8?style=flat-square" alt="288 graph edges">
  <img src="https://img.shields.io/badge/tests-225%20passing%20(18%20suites)-10b981?style=flat-square" alt="225 passing tests across 18 suites">
</p>

<p>
  <a href="./index.html"><strong>🔍 Interactive Web Application</strong></a> · 
  <a href="./docs/BENCHMARKS_AND_EXAMPLES.md"><strong>📊 Comparisons & Diffs</strong></a> · 
  <a href="./docs/CLI_USAGE.md"><strong>💻 CLI Reference</strong></a> · 
  <a href="./reports/FINAL_INDEPENDENT_AUDIT.md"><strong>🛡️ Independent Audit</strong></a> · 
  <a href="#quick-start"><strong>🚀 Quick Start</strong></a> · 
  <a href="#contributing"><strong>🤝 Contributing</strong></a>
</p>

</div>

---

## 💡 The Problem & The Solution

When AI coding agents (**Claude Code**, **Cursor**, **Cline**, **Continue**, **Windsurf**, or **Codex**) generate code for modern APIs, stale training data frequently causes subtle integration bugs:

* ❌ **Broken Webhook Verification**: Parsing request bodies with `express.json()` before verifying raw-body HMAC signatures (Stripe, Razorpay, WhatsApp Cloud API, Linear, Svix, Paddle, Polar).
* ❌ **Deprecated SDK Methods**: Generating legacy middleware or retired model IDs (e.g., Clerk v4 `authMiddleware` instead of v5 `clerkMiddleware`, or legacy Google Maps endpoints without `X-Goog-FieldMask`).
* ❌ **Unbatched HTTP Loops**: Executing individual `send()` calls instead of chunked batch requests (e.g., Resend `batch.send()` with max 100 emails per request).
* ❌ **Missing Connection Pooling & Bounded Execution**: Spawning unpooled database connections in serverless functions (Neon, Supabase, PostgreSQL) or omitting retry/idempotency handling.

`awesome-api-skills` provides **141 strictly schema-validated `SKILL.md` context specifications** with explicit **verification tiers**, documented AI pitfalls, production checklists, and a synchronized 288-edge knowledge graph.

---

## 🛡️ Transparent Verification Tiers

Instead of blanket "verified" or "official" claims, every skill declares its exact `verificationTier` in `metadata.json` (enforced by `@awesome-api-skills/validator` rules `V-001` through `V-009`):

| Verification Tier | Meaning | Current Count (141 total) |
| :--- | :--- | :---: |
| `officially_maintained` | Maintained directly by the API vendor (`official: true`) | **0** |
| `sandbox_integration_tested` | Executed end-to-end against a live vendor sandbox | **0** |
| `code_example_tested` | Vendor docs checked + TypeScript examples & offline contract/crypto tests passing in Vitest | **16** |
| `documentation_checked` | Vendor docs cross-checked and technical inaccuracies remediated | **4** |
| `schema_validated` | Passes strict JSON Schema (`V-004`), structure (`V-005`), reference integrity (`V-006`), security hygiene (`V-007`), and deprecation (`V-008`) rules | **121** |
| `unverified` | Draft / newly scaffolded skill not yet validated | **0** |

> All `141` skills in this repository are community-authored (`official: false`). Full per-skill audit scores and evidence are published in [`reports/`](./reports/FINAL_INDEPENDENT_AUDIT.md).

---

## ⚡ Real-World Impact: Before vs. After

| Integration Domain | ❌ Without Skill (LLM Guessing) | ✅ With `SKILL.md` (Context Injected) |
| :--- | :--- | :--- |
| **Stripe Webhooks** | Parses JSON with `express.json()`, corrupting the raw payload buffer and failing signature verification. | Injects `express.raw({ type: 'application/json' })` so `stripe.webhooks.constructEvent()` verifies authentic HMAC signatures. |
| **OpenAI Responses API** | Mixes legacy Assistants threads or Chat Completions syntax with Responses endpoints. | Uses `client.responses.create()` with `instructions`, `input`, `previous_response_id`, and `text.format` structured outputs. |
| **Google Maps Platform** | Calls legacy endpoints or sends `X-Goog-FieldMask: *`, triggering expensive Enterprise + Atmosphere SKU billing. | Uses Places (New) v1 / Routes v2 with `X-Goog-Api-Key` header and minimal explicit `X-Goog-FieldMask`. |
| **Clerk Next.js Auth** | Generates deprecated `authMiddleware({ publicRoutes })` causing App Router runtime crashes. | Uses `clerkMiddleware()` with `createRouteMatcher()` matching `@clerk/nextjs` v5+ App Router conventions. |
| **Resend Batch Emails** | Runs a naive `for...of` loop with individual `send()` calls, hitting rate limits — or overflows batch size limits. | Chunks recipients into batches of **up to 100 emails per request** via `resend.batch.send([])` (official API limit). |
| **WhatsApp Cloud API** | Verifies webhooks with the Verify Token instead of the Meta App Secret or sends free-form text past the 24h window. | Verifies `X-Hub-Signature-256` with `WHATSAPP_APP_SECRET` + `crypto.timingSafeEqual` and enforces template messages outside the 24h window. |

> 📖 **Review complete runnable diffs in [docs/BENCHMARKS_AND_EXAMPLES.md](./docs/BENCHMARKS_AND_EXAMPLES.md).**

---

## 🚀 Quick Start

### 1. Direct Copy into Your Project (Zero Dependencies)

```bash
# Clone the repository shallowly
git clone --depth 1 https://github.com/ashish7802/awesome-api-skills.git

# Copy Stripe skill to Claude Code
cp -r awesome-api-skills/skills/stripe .claude/skills/

# Copy OpenAI Responses & Razorpay skills to Cursor
cp -r awesome-api-skills/skills/openai-responses .cursor/skills/
cp -r awesome-api-skills/skills/razorpay .cursor/skills/

# Copy Qdrant & AWS Bedrock skills to generic agent workspace
cp -r awesome-api-skills/skills/qdrant .agents/skills/
cp -r awesome-api-skills/skills/aws-bedrock .agents/skills/
```

Then prompt your assistant:
> *"Use `.claude/skills/stripe/SKILL.md` and `.claude/skills/inngest/SKILL.md` to implement subscription webhooks."*

---

### 2. Using the CLI & Workspace Validator

```bash
# Install dependencies and compile workspace packages
npm install
npm run build:packages

# Multi-word inverted-index search
node packages/cli/dist/bin.js search "embeddings vector rag"

# Strict validation across all 141 skills (rules V-001 through V-009)
npm run validate:skills

# Diagnose repository & registry health
node packages/cli/dist/bin.js doctor

# Audit skill freshness without mutating metadata
node packages/cli/dist/bin.js update --max-age-days 90

# Run reproducible local benchmark suite
npm run benchmark
```

---

## 📚 Skill Catalog (141 Schema-Validated Skills)

| Category | Skills Included |
| :--- | :--- |
| **AI, LLM & Reasoning** | `openai-responses`, `aws-bedrock`, `openrouter`, `langfuse`, `deepseek`, `openai`, `anthropic`, `gemini`, `groq`, `mistral`, `cohere`, `elevenlabs`, `deepgram`, `replicate`, `ollama`, `vllm`, `langchain`, `llamaindex`, `vercel-ai-sdk`, `langgraph`, `anthropic-mcp`, `azure-openai` |
| **Vector DB & Search** | `chromadb`, `qdrant`, `weaviate`, `pinecone`, `meilisearch`, `typesense`, `algolia`, `xquik` |
| **Payments & Billing** | `stripe`, `razorpay`, `paddle`, `lemon-squeezy`, `braintree`, `revenuecat`, `plaid`, `polar` |
| **Workflows & Background** | `inngest`, `trigger-dev`, `bullmq`, `kafka`, `rabbitmq`, `nats`, `redis-streams` |
| **Auth & Security** | `workos`, `svix`, `unkey`, `clerk`, `auth0`, `okta`, `better-auth`, `supabase-ssr`, `jwt`, `oauth2`, `openid-connect` |
| **Databases & ORMs** | `postgresql`, `mysql`, `sqlite`, `better-sqlite3`, `cloudflare-d1`, `mongodb-atlas`, `planetscale`, `neon`, `turso`, `supabase`, `firebase`, `drizzle`, `prisma` |
| **Caching & Rate Limiting** | `redis`, `upstash`, `upstash-ratelimit` |
| **Cloud, Storage & Media** | `cloudflare-r2`, `cloudinary`, `aws-s3`, `aws-dynamodb`, `azure-blob-storage`, `google-cloud-storage` |
| **Serverless & Edge Compute** | `aws-lambda`, `google-cloud-run`, `vercel`, `railway`, `render`, `fly`, `digitalocean`, `cloudflare`, `cloudflare-workers`, `deno-deploy` |
| **Communications & Messaging** | `whatsapp-cloud-api`, `resend`, `postmark`, `sendgrid`, `twilio`, `novu`, `slack`, `discord` |
| **Maps & Geolocation** | `google-maps-platform`, `mapbox` |
| **Productivity & Collaboration** | `notion`, `linear`, `github`, `shopify`, `convex` |
| **Backend & Validation** | `express`, `fastapi`, `nestjs`, `hono`, `trpc`, `zod` |
| **Frontend Frameworks** | `react`, `vue`, `nextjs`, `nuxt`, `sveltekit` |
| **Infrastructure & DevOps** | `docker`, `kubernetes`, `helm`, `terraform`, `pulumi`, `argo-cd`, `github-actions`, `traefik`, `nginx`, `caddy`, `turborepo`, `linux` |
| **Observability & Analytics** | `datadog`, `sentry`, `prometheus`, `grafana`, `loki`, `jaeger`, `opentelemetry`, `mixpanel`, `posthog` |
| **Dev Tools & Testing** | `eslint`, `prettier`, `biome`, `vitest`, `playwright`, `git` |

> 🌐 **Browse the searchable interactive application via `npm run dev`.**

---

## 🏗️ Monorepo Architecture

```
├── skills/                     # 141 SKILL.md specs, metadata.json contracts & examples
├── reports/                    # Independent audit, verification & benchmark reports
├── src/                        # Interactive React + Vite + Tailwind CSS application
├── api/                        # Vercel Serverless Functions (/api/skills, /api/search, /api/validate)
├── packages/
│   ├── cli/                    # CLI binary (search, validate, doctor, install, update, benchmark)
│   ├── core/                   # Orchestration runtime and workspace validation
│   ├── validator/              # Strict schema, link, security hygiene & deprecation engine (V-001..V-009)
│   ├── registry/               # Inverted token index search & registry resolver
│   ├── generator/              # Template engine & SKILL.md artifact compiler
│   ├── sdk/                    # Programmatic Node.js SDK with strict SemVer compatibility checks
│   └── shared-types/           # Shared TypeScript interfaces, VerificationTier enum & JSON Schemas
├── scripts/
│   ├── dev/                    # Dogfooding snapshots, benchmark suite, graph & React data compiler
│   └── generators/             # Metadata & scaffolding utilities
└── vercel.json                 # Vercel fullstack deployment configuration
```

---

## 🎯 Verification & Measured Performance

All figures below are independently measured on this repository (Node `v22.23.2`, Linux x64, 4 vCPU — full methodology in [`reports/BENCHMARK_VERIFICATION_REPORT.md`](./reports/BENCHMARK_VERIFICATION_REPORT.md)):

1. **Strict Schema & Hygiene Validation**: **141/141 skills pass with 0 errors** under strict zero-backfill rules `V-001`–`V-008` (`V-009` transparently emits 24 warnings for legacy stub-only `examples/` folders).
2. **Automated Test Suite**: **225 tests across 18 Vitest suites** pass (including CLI path-traversal security tests, strict validator regression tests, inverted-index search tests, SemVer checks, offline contract/HMAC tests for all 16 new skills, and full 141-skill catalog validation).
3. **Synchronized Knowledge Graph**: **141 nodes and 288 directed edges** (`0` broken edges, `0` duplicate edges).
4. **Reproducible Local Benchmarks (`npm run benchmark`)**:
   - Workspace parse (141 skills): `11.42 ms` cold / `5.64 ms` warm median (`9.68 ms` p95)
   - Inverted-index multi-term search (867 tokens): **`0.359 ms` median** (`0.671 ms` p95), `8/8` top-5 relevance hits
   - Strict catalog validation (`V-001`–`V-008`): `1.04 ms` warm median across 141 skills

---

## 🤝 Contributing

We welcome contributions of new API skills and improvements to existing documentation!

1. **Fork and clone** the repository:
   ```bash
   git clone https://github.com/ashish7802/awesome-api-skills.git
   cd awesome-api-skills
   npm install
   npm run build:packages
   ```
2. **Create or improve a skill** under `skills/<skill-name>/` with `SKILL.md`, `metadata.json`, and realistic runnable examples under `examples/`.
3. **Rebuild graph & web data and run verification gates**:
   ```bash
   node scripts/dev/build-knowledge-graph.js
   node scripts/dev/build-react-data.js
   npm run validate:skills
   npm test
   npm run lint
   ```
4. **Submit a Pull Request**.

See [CONTRIBUTING.md](./CONTRIBUTING.md) and [SECURITY.md](./SECURITY.md) for guidelines and vulnerability reporting.

---

## 📄 License

Distributed under the [MIT License](./LICENSE). © 2026 Awesome API Skills Contributors.
