# VisionClaw Agent

[![CI](https://github.com/Huskyauto/VisionClaw-Agent-Public-Release/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Huskyauto/VisionClaw-Agent-Public-Release/actions/workflows/ci.yml)
[![Stars](https://img.shields.io/github/stars/Huskyauto/VisionClaw-Agent-Public-Release?style=social)](https://github.com/Huskyauto/VisionClaw-Agent-Public-Release/stargazers)
[![Live demo](https://img.shields.io/badge/live%20demo-agenticcorporation.net-2ea44f)](https://agenticcorporation.net)
[![Docs](https://img.shields.io/badge/docs-FORK--SETUP.md-blue)](FORK-SETUP.md)
[![Roadmap](https://img.shields.io/badge/roadmap-public-purple)](ROADMAP.md)

### ▶ Watch the 84-second demo

A narrated walkthrough of the **live** platform — every frame is a real page from the running app (counts match [`docs/CURRENT_PLATFORM_TOTALS.md`](docs/CURRENT_PLATFORM_TOTALS.md)).

[![Watch the VisionClaw demo video](docs/assets/demo-poster.jpg)](https://github.com/Huskyauto/VisionClaw-Agent-Public-Release/releases/download/demo-v1/visionclaw-demo.mp4)

> Click the image to play/download the MP4 (1080p, ~12 MB, hosted as a release asset).

### The Self-Hosted AI Operating System for Agencies & Operators

**An open-source, multi-tenant AI agent workspace — documents, research & workflows. Built for agencies, operators, and founders who want an always-on AI operations team they own and host themselves: your keys, your database, your infrastructure. No per-seat SaaS, no vendor lock-in.**

**Created by Robert Washburn** | huskyauto@gmail.com | [Live demo: agenticcorporation.net](https://agenticcorporation.net)

> Not affiliated with the unrelated AR/wearable "VisionClaw" project. This is the AI agent platform.

> **Reviewing this repo (human or AI)?** Start with [`docs/FOR-EXTERNAL-REVIEWERS.md`](docs/FOR-EXTERNAL-REVIEWERS.md) — auto-regenerated at every mirror build with current code-shape facts and deliberate architecture decisions. Current machine-readable release metrics are in [`docs/release-facts.json`](docs/release-facts.json), with the readable rendering in [`docs/CURRENT_PLATFORM_TOTALS.md`](docs/CURRENT_PLATFORM_TOTALS.md).

---

## ⚠️ Autonomous Pipelines Disclaimer (please read before forking)

VisionClaw ships several **autonomous decision pipelines** — the multi-model jury (`jury_triage`), the Agentic CI Self-Healer, and downstream implementer hooks. In this public release these pipelines are **safe-by-default**:

- **Auto-apply is OFF.** The jury votes and writes a human-readable decision log for your review, but it does **not** automatically queue fixes for code-mutation or apply verdicts to your codebase.
- **To opt in**, set `JURY_AUTOAPPLY=1` in your environment. This enables the implementer-pickup seam (`data/jury-decisions/queue.json`). Only enable this if you have read the code, understand the risk model, and have your own test/rollback discipline in place — autonomous code-mutation can corrupt data, break auth, leak secrets, or commit broken code if your guardrails aren't set up.
- **No warranty.** This project is provided AS-IS under its open-source license. The maintainers, contributors, and any platform hosting the source (including Replit) are not responsible for outcomes when you enable autonomous pipelines in your own deployment. The defaults are deliberately conservative; if you change them, you own the consequences.
- **Reporting:** if you find a safety bug in the gated-off default path (i.e. something autonomous happens without `JURY_AUTOAPPLY=1`), please open a GitHub issue or email huskyauto@gmail.com.

---

## What Is This?

VisionClaw Agent is an open-source, multi-tenant AI platform where 18 specialized agents work together to produce real deliverables — research reports, legal documents, financial models, marketing campaigns, slide decks, spreadsheets, and PDFs.

Instead of a single chatbot, you get a full agent workforce. Give it a task. The right agent picks it up, selects the right tools, coordinates with other agents when needed, and delivers a finished result. Every decision is traceable, every action is governed, and every integration degrades gracefully when not configured.

**Fork it. Configure your API keys. Deploy. You have an AI operations team.**

**The app runs with just one LLM key and a Postgres database.** Everything else — email, payments, voice, Drive — is optional and appears automatically when you add the key.

**Latest source update — R137+sec (October 19, 2026): Business pilots, company report packages and evidence-first operations.** Owner-only health/re-scan, release, governance and cost/routing pilots; read-only website readiness; sourced company reports with required audio; private alert logs; receipt-backed delivery checks, outcome-first briefings and video packaging. Private report packages are excluded from generic tenant file access. [Feature/access matrix](docs/platform-update-2026-10-19.md). Forks need their own credentials, entitlements and configuration. Focused live pilot verification is not universal certification; GitHub synchronization is not website publication.

Roughly 320k lines of TypeScript across 1,100+ files. 40+ pages. **428 total registered tools · 386 public documented tools · 68 total skills · 146 active capabilities · 18 personas · 195 declared / 276 live development tables · 41 governance rules · 887 platform indexes · 86 curated AI models · 6 AI providers · 6 deployment targets.** These are an October 19 **development evidence snapshot**, not live production telemetry. The public tool index deliberately excludes trusted-persona-only tools. Current release facts: [`docs/release-facts.json`](docs/release-facts.json). Browsable indexes: [`docs/tools.md`](docs/tools.md) · [`docs/personas.md`](docs/personas.md).

### October 9–14 source updates

- **Treasury:** owner-only historical stock/crypto paper replays, explicit fees/slippage, frozen strategy presets and persisted benchmark evidence. No real-money orders, broker connection or profitability certification.
- **AgentID:** optional agent sign-in with OIDC validation, state/nonce/PKCE, session rotation and token-expiry enforcement. Agents receive non-admin trial scope. Human sign-in remains available; full authenticated production lifecycle verification is not claimed.
- **Robert:** personal/emotional-life specialist with private tenant context. Shared installation defaults contain no private owner history; persona synchronization preserves names and environment-local identities.
- **Model evidence and cost controls:** requested, resolved and provider-reported models are distinct. Routine/demanding owner model preferences retain authorized fallbacks. CheaperInference is an opt-in paid owner fallback with shared $20 UTC-day reserve-before-spend accounting; it is not an application-wide daily limit, a free lane or permission to change all users' routing.
- **Conversation recovery:** progress-based stream deadlines, correction-aware compaction, recent-context budgeting, fenced approval leases and advisory history comparisons. No automatic opaque-action replay or new paid retries.
- **Account/file boundaries:** tenant-bound storage/Drive operations, owner-only voice configuration with UI masking, scoped watchdog/approval evidence and content-bound verifier snapshots. Production verifier success and capacity remain unverified.
- **Advisory coordination:** Muse's owner outbox/poll workflow is partial; queueing is not delivery proof. A Cue/Felix setup document is not a new active integration or verified cross-conversation reply channel.
- **Portable builds:** public npm tarballs, Node 22.22+, explicit public-test classification and sanitized append-only mirror updates. Research material is tested before adoption: REA informed an AST import check, while REA runtime installation, HERMES and permanent worktree swarms remain unimplemented.

[Full feature/status matrix and source-folder guide](docs/platform-update-2026-10-14.md). Owner integrations are optional; forks must supply their own services. Historical release notes below remain historical.

**R136.1 development pilot:** Treasury adds owner-only historical stock/crypto paper replays
with Bitcoin/Ethereum/Solana choices; frozen trend/reversion/breakout/rolling-RSI presets, measured costs/returns, next-open fills, matched benchmark
and optional Jev shadow/model interpretation. No real orders, broker connection,
automatic strategy promotion or promised profitable trading.

### Earlier October 4–8 source improvements and their limits

- **Owner juries across topics:** subscription-first recovery preserves successful answers and seat-owned evidence. Explicit model identity contracts remain pinned; failed seats do not become fake successes. Standard Compute supplies bounded pinned-model fallback, not an opaque smart-routing verdict. Native paid exceptions require separate authority and conservative reservations; account quotas are finite.
- **Chat-only GitHub Copilot:** official SDK, trusted owner-authored question, fresh isolated subprocess, shared 20-attempt daily quota, one concurrent request and 120-second deadline. No file/shell/MCP tools, ambient customer context, retries, provider fallback or default-model changes. Forks configure their own GitHub subscription access.
- **Haiku 5.5 content repurposing:** fixed medium effort for the existing eligible paid operation, with tenant admission and observed-usage accounting. Drafts do not automatically publish or schedule. Global model routing and automatic effort selection are unchanged.
- **Model availability:** Muse Spark 1.3 is registered with context and token rates; saved 1.1 selections retain accounting. The existing 04:30 UTC daily OpenRouter sync watches official text-only Beam listings and persists validated rates with adoption. Beam is not currently available; catalog discovery is not inference, quality or flat-rate entitlement proof.
- **Evidence-first income discovery and CI:** candidate-owned quotations/URLs distinguish observations from proposals; insufficient evidence stays incomplete. REA informed the existing parser-based domain-boundary gate, not a new installed toolkit.
- **Security maintenance:** global skill-prompt export is owner-only; Beam token costs survive adoption/restart. Compatible dependency patches address identified advisories, including proxy-address handling. Existing Drive ownership guards were verified; the initial contrary allegation was withdrawn. See [review scope, results and remaining gaps](docs/reviews/2026-10-08-app-review.md), not a blanket security certification.
- **Privacy and ownership:** tenant checks precede upload completion, subagent inspection and schedule changes. Drive operations require trusted ancestry and verified file bytes; HTTP file authorization shares one canonical identity with static serving. Exact tool rosters survive model recovery paths.
- **Memory and anonymous chat:** bounded pre-inference judgments can skip optional memory work; uncertainty preserves the existing path. Public chat excludes private retrieval, skill prompts and tools, with atomic daily admissions and capped responses.
- **Durable recovery:** weekly-maintenance work uses fenced leases and explicit mail outcomes; video recovery retains ownership and heavy-work capacity. Replay checks artifact paths, freshness and grading/archive evidence rather than guessing success.
- **Owner-only planning and diagnostics:** opportunity filing, on-hold offer concepts, knowledge-quality reporting, prior-research revisit, read-only MCP project briefs, and verifier memory diagnostics. These do not activate sales, outreach, autonomous customer fulfillment, or a completed verification.
- **Owner-Felix API/A2A routing:** **GPT-5.4** is pinned to Replit's managed OpenAI transport for this ingress only. Other tenants, personas and ordinary interactive chats are unchanged. Managed inference can consume account credits; a flat/local cost label is not billing proof.
- **Evidence before adoption:** cross-case trials retain negative results. A rejected offline AI-Newton candidate did not replace the runtime evaluator.

**Unresolved readiness gates:** the proposed aggregate $20 daily metered-AI authority is **not enforced application-wide**. Production verifier completion, production schema parity, fresh source-bound tenant-audit evidence, external collaborator instructions and post-publish replay require separate verification. A Git repository backs up tracked source—not secrets, databases, uploads or ignored workspace configuration. Forks must configure their own services; sanitized source is not a configured clone of the hosted instance.

---

## Who is this for?

- **Agencies** — give every client a multi-agent operations team without burning headcount.
- **Operators & founders** — replace 5-10 SaaS subscriptions with one agent workforce you own.
- **Solo entrepreneurs** — run a research / content / sales / finance team of one.
- **Research teams** — a real testbed for multi-agent orchestration, AHB safety layers, and tool governance.

## What can it actually do?

Out of the box, ask it to:

- Research a market, build the comparison spreadsheet, ship the PDF
- Draft a proposal, contract, or pitch deck (with vision-graded slide art)
- Analyze a contract for risk across 9 regulatory frameworks
- Run a deep research sweep across arXiv / HN / Reddit / press releases
- Build a financial forecast with charts and exec summary
- Plan a content calendar, generate the posts, schedule them
- Send invoices, track CRM, run an outreach sequence
- Produce a YouTube long-form or Short, end to end (script → render → upload)

Every deliverable lands as a real file (PDF, XLSX, PPTX, MP4, MP3) in Google Drive or local storage — not a chat transcript.

## 60-second quickstart

```bash
git clone https://github.com/Huskyauto/VisionClaw-Agent-Public-Release.git
cd VisionClaw-Agent-Public-Release && npm install
export DATABASE_URL="postgresql://localhost/visionclaw"
export SESSION_SECRET="$(openssl rand -hex 32)"
export OPENAI_API_KEY="sk-..."   # or ANTHROPIC_API_KEY
npm run dev                      # http://localhost:5000
```

That's it. The platform auto-creates the schema, seeds 18 personas + 41 governance rules, and redirects you to `/setup`. First account becomes admin.

Don't want to run it locally? Look at the **live deployment**: [agenticcorporation.net](https://agenticcorporation.net).

## Architecture at a glance

Every request — human chat or autonomous loop — passes through the same safety layer before it can touch a tool, and every tool call lands in a tenant-isolated Postgres. One pipeline, no side doors:

```mermaid
flowchart TB
    U["User / Autonomous loops<br/>(heartbeat · scheduled tasks · self-repair)"] --> CE["Chat Engine (SSE)"]
    CE --> SAFETY

    subgraph SAFETY["AHB Safety Layer — every call passes through"]
        direction TB
        IG["Intent gate<br/>(fail-OPEN, logged)"] --- DP["Destructive-tool policy<br/>(fail-CLOSED)"]
        RG["Outbound redaction gate"] --- TC["Tenant context<br/>(AsyncLocalStorage)"]
    end

    SAFETY --> CEO["CEO orchestrator (Felix)"]
    CEO --> ROUTER["Agent Router"]
    ROUTER --> P1["Specialist personas<br/>(Engineer · Writer · Research · Finance · Legal · …)"]
    ROUTER --> P2["Imported Claude Code agents<br/>(runtime adapter)"]

    P1 --> TOOLS
    P2 --> TOOLS

    subgraph TOOLS["Tool layer — 428 total registered tools"]
        direction TB
        T1["File I/O · web · email · LLM · payments · drive"]
        T2["TNR snapshots — irreversible calls are undoable"]
        T3["Tracing spans — parent-linked causality tree"]
        T4["Admission control — priority pool + rate limits"]
    end

    TOOLS --> DB[("PostgreSQL + pgvector<br/>tenant-isolated: every WHERE filters tenant_id")]
```

<details>
<summary>Plain-text version of the same diagram</summary>

```
                          ┌────────────────────────────────────────┐
                          │  AHB safety layer (intent + policy)    │
                          │  • intent gate (fail-OPEN, logged)     │
                          │  • destructive-tool policy (fail-CLOSE)│
                          │  • outbound redaction gate             │
                          │  • tenant-context (AsyncLocalStorage)  │
                          └─────────────┬──────────────────────────┘
                                        │  every call passes through
                                        ▼
   User ──▶ Chat Engine (SSE) ──▶ CEO (Felix) ──▶ Agent Router ──┐
                                                                 │
        ┌────────────────────────────────────────────────────────┤
        ▼                ▼                ▼                ▼     ▼
   Specialist       Specialist       Specialist        ...   Imported
   persona          persona          persona                 Claude Code
   (Forge,          (Scribe,         (Neptune,               agents (with
    Engineer)        Writer)          Research)              runtime adapter)
        │                │                │                       │
        └──────┬─────────┴────────────────┴───────────────────────┘
               │  tool dispatch (428 total registered tools)
               ▼
   ┌──────────────────────────────────────────────────────────────┐
   │  Tool layer: file I/O · web · email · LLM · payments · drive │
   │  • TNR snapshots (R100) on irreversible calls — undoable     │
   │  • Tracing spans (R101) parent-linked into causality tree   │
   │  • Admission control (R102) priority pool + rate limit       │
   └──────────────────────────────────────────────────────────────┘
               │
               ▼
   PostgreSQL + pgvector  (tenant-isolated; every WHERE filters tenant_id)
```

</details>

Browse the full lineup: [tools index](docs/tools.md) · [personas index](docs/personas.md).

---

## Tested & CI-protected

This is not vibe-coded. Every push validates the complete public-test manifest and runs environment-appropriate GitHub Actions suites. The public `npm test` command is a small mirror-smoke contract, not a claim that every classified test runs locally; database and integration suites run only in provisioned CI, while browser/special and source-only checks remain visibly classified for manual review. **Note:** the public-mirror CI workflow at `.github/workflows/ci.yml` is preserved on every snapshot since 2026-05-06 (HyperAgent review followup). Counts and badges below reflect what actually runs on the public mirror; for live source-of-truth platform metrics, see [`docs/CURRENT_PLATFORM_TOTALS.md`](docs/CURRENT_PLATFORM_TOTALS.md).

| Gate | What it proves | Status |
|---|---|---|
| `build` | Production bundle compiles end-to-end | ✅ hard gate |
| `security-tests` | **158 tests across 16 files in 6 categories** — SSRF/DNS-rebinding, admin auth, recipe validation + atomic writes, webhook signatures, trigger rate-limit, tenant isolation, conversation IDOR, background-queue durability + reclaim boundaries, destructive-command rails (the deny-list that blocks `db:push --force`, `DROP TABLE`, `git push --force`, `rm -rf /`, etc.), LLM cost-rate-card correctness, tool-dispatch contract, **tenant-context hardening** (41 tests — the strict `tenantScope()` storage helper that rejects every fail-open shape, the `STRICT_TENANT_CONTEXT` env flag with `assertTenantContext()` runtime guard, and end-to-end propagation through chat → assertTenantContext → step-ledger → AsyncLocalStorage → recordExecution with a live-DB persist round-trip; full source paths and call-site line numbers in [`docs/EVIDENCE.md`](docs/EVIDENCE.md)) | ✅ hard gate |
| `docker` | Multi-stage image builds, container boots clean, `/healthz` returns 200 | ✅ hard gate |
| `typecheck` | `tsc --noEmit` — tracked and burning down | informational |
| `silent-failure-hunter` | Greps `server/` + `shared/` for the silent-failure shapes that bit us before (`tenantId ?? 1`, default-1 params, log-and-swallow catches, literal-secret fallbacks); uploads the full scan report as a 30-day workflow artifact on every PR | informational |
| `tool-smoke-test` | Staged smoke-test + documentation program across the governed tool catalog (407/407 cataloged verified at last full re-scan; 21 stages of 21; doc-only tools are never auto-invoked); $0 / no LLM / no tenant, one stage per session | **COMPLETE — 407 of 407 cataloged verified · 21/21 stages signed off · 0 flags** (refreshed 2026-07-24) |

Run the supported local mirror smoke contract with `npm test`. The full manifest, CI history, destructive-command deny-list, and silent-failure baseline are in [`docs/`](docs/).

---

## ⚡ Deploy your own copy

| Platform | One-click |
|---|---|
| **Replit** | [Open in Replit →](https://replit.com/github/Huskyauto/VisionClaw-Agent-Public-Release) |
| **Render** | [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Huskyauto/VisionClaw-Agent-Public-Release) |
| **Railway** | [![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template?template=https%3A%2F%2Fgithub.com%2FHuskyauto%2FVisionClaw-Agent-Public-Release) |
| **Docker** | `docker compose up` — see [FORK-SETUP.md](FORK-SETUP.md) |

After deploy, you'll need a Postgres database with the `vector` extension (Render and Railway can provision one for you), one LLM key (`OPENAI_API_KEY` or `ANTHROPIC_API_KEY`), and a `SESSION_SECRET`. Everything else is optional.

### 🛠 Want it installed for you?

The platform is free and always will be — but standing up a production instance (database, keys, integrations, governance, backups) takes real platform knowledge. I offer a **done-for-you deployment service**: your own instance, on your infrastructure, configured safely by the author.

- **Standard Install — $750**: live in under a week, keys + core integrations wired, governance defaults reviewed with you, live walkthrough, 2 weeks of email support
- **Pro Setup — $1,500**: everything above plus up to 3 custom personas for your workflows, Stripe/multi-tenant setup, automated backups, 30 days of priority support

You own everything — code, data, keys, infrastructure. No lock-in, ever. **Email huskyauto@gmail.com with subject "Deploy"** — tell me your hosting preference and what you want the agents doing. Launch price: first 5 installs at these rates.

<p align="center">
  <img src="docs/images/screenshot-home.jpg" alt="VisionClaw Landing Page" width="800" />
</p>
<p align="center"><em>Landing page with live agent activity feed and command center stats</em></p>

<p align="center">
  <img src="docs/images/screenshot-setup.jpg" alt="VisionClaw Setup Dashboard" width="800" />
</p>
<p align="center"><em>First-run setup dashboard — real-time status of every integration</em></p>

---

## Try These Prompts

Once you're set up, paste any of these into the chat to see the platform in action:

| Prompt | What Happens |
|--------|-------------|
| "Research the top 5 competitors in [your industry] and build me a comparison spreadsheet" | Radar researches, Atlas structures data, exports a formatted .xlsx to Google Drive |
| "Draft a professional proposal for [client name] based on our last conversation" | Scribe pulls context from memory, writes a styled PDF, Proof reviews it for quality |
| "Analyze this contract for risks" *(attach a PDF)* | Luna scans for 20 risk patterns across 9 regulatory frameworks, scores compliance |
| "Create a weekly content calendar for our social media" | Teagan builds a structured plan with post ideas, hashtags, and optimal timing |
| "Give me a financial forecast for Q3 based on current revenue trends" | Cassandra models projections, generates charts, delivers an executive summary |
| "What happened in AI news this week?" | Neptune runs a deep research sweep across arXiv, HN, Reddit, and tech blogs |

---

## 📸 Tour — what you actually see

Real screenshots from the live instance at [agenticcorporation.net](https://agenticcorporation.net).

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="docs/images/tour-hero.jpg"><img src="docs/images/tour-hero.jpg" alt="Landing hero — Hire an AI corporation, not another chatbot" /></a>
      <p align="center"><sub><b>Landing hero</b> — value prop in one line, with three real CTAs.</sub></p>
    </td>
    <td width="50%" valign="top">
      <a href="docs/images/tour-command-center.jpg"><img src="docs/images/tour-command-center.jpg" alt="Historical Command Center screenshot — interface illustration, not current metric or deployment evidence" /></a>
      <p align="center"><sub><b>Command Center</b> — live counts, recent ops with status pills, capability chips.</sub></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="docs/images/tour-agent-activity.jpg"><img src="docs/images/tour-agent-activity.jpg" alt="Agent Activity Feed — Neptune, Luna, Cassandra, Scribe, Felix shipping work" /></a>
      <p align="center"><sub><b>Agent Activity Feed</b> — Neptune ships research, Luna runs compliance, Cassandra builds the Excel model, Felix delivers the styled PDF.</sub></p>
    </td>
    <td width="50%" valign="top">
      <a href="docs/images/tour-moa.jpg"><img src="docs/images/tour-moa.jpg" alt="Mixture of Agents — 4 frontier proposers + Opus aggregator" /></a>
      <p align="center"><sub><b>Mixture of Agents</b> — 4 frontier proposers (Sonnet · GPT-4.1 · Gemini 2.5 Pro · DeepSeek Reasoner) feed a Claude Opus aggregator for ensemble-quality answers.</sub></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="docs/images/tour-code-proposals.jpg"><img src="docs/images/tour-code-proposals.jpg" alt="Gated Code Proposals — shadow verifier in a git worktree" /></a>
      <p align="center"><sub><b>Gated Code Proposals (R25)</b> — nightly research generates real edits; a shadow verifier compiles each in an isolated git worktree before any human reviewer sees it.</sub></p>
    </td>
    <td width="50%" valign="top">
      <a href="docs/images/tour-glasses.jpg"><img src="docs/images/tour-glasses.jpg" alt="Glasses Gateway — Meta Ray-Ban + Gemini Live" /></a>
      <p align="center"><sub><b>Glasses Gateway</b> — Meta Ray-Ban smart glasses stream POV video and audio to a tenant-isolated gateway with sub-second voice replies via Gemini Live.</sub></p>
    </td>
  </tr>
</table>

---

## Platform at a Glance — October 19 Development Evidence

> This is the dated development snapshot, not live production telemetry. Counts agree with [docs/release-facts.json](docs/release-facts.json) and [docs/CURRENT_PLATFORM_TOTALS.md](docs/CURRENT_PLATFORM_TOTALS.md); documentation was reconciled October 19.

| Metric | Count |
|--------|-------|
| AI Agents (Personas) | 18 |
| Tools (total registered) | 428 |
| Tools (public documented) | 386 |
| AI Models in Core Registry | 86 curated |
| Daily Catalog Discovery | 1000+ models scanned on OpenRouter |
| AI Providers | 6 (OpenAI, Anthropic, Google, xAI, OpenRouter, Perplexity) |
| Governance Rules | 41 |
| Corporate Operation Scaffolds | 75 |
| Corporate Departments | 12 |
| Skills | 68 total (63 DB-seeded skills + 5 platform agent skills) |
| Frontend Pages | 40+ |
| API Endpoints | 300+ |
| Database Tables | 195 declared / 276 live development |
| Platform Indexes | 887 (617 non-PK) |

---

## How It Works

```
  User Request
       │
       ▼
┌──────────────────┐     ┌─────────────────────────────┐
│   Chat Engine    │────▶│   Agent Router              │
│  (SSE streaming) │     │   picks best agent for task  │
└──────────────────┘     └──────────┬──────────────────┘
                                   │
                    ┌──────────────┼──────────────┐
                    ▼              ▼              ▼
              ┌──────────┐  ┌──────────┐  ┌──────────┐
              │  Felix   │  │ Minerva  │  │ Neptune  │  ... 18 agents
              │  (CEO)   │  │(Strategy)│  │(Research)│
              └────┬─────┘  └────┬─────┘  └────┬─────┘
                   │             │              │
                   ▼             ▼              ▼
            ┌─────────────────────────────────────────┐
            │     428 Total Registered Tools          │
            │  Search · Write · Build · Analyze ·     │
            │  Email · Pay · Generate · Research       │
            └──────────────────┬──────────────────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
        ┌────────────┐   ┌────────────┐   ┌────────────┐
        │ PostgreSQL │   │ Google     │   │ 6 AI       │
        │ + pgvector │   │ Drive      │   │ providers  │
        │ D195/L276  │   │ storage    │   │ 86 curated │
        └────────────┘   └────────────┘   └────────────┘
```

Database diagram: D = declared tables; L = live development tables. Counts use the October 19 evidence snapshot, not live production telemetry.

**Example flow:** You say "Research competitor pricing and build me a comparison spreadsheet."
1. The **Chat Engine** routes to **Felix** (CEO) who sees this needs research + document production
2. Felix spawns **Radar** (Intelligence) to research competitors and **Atlas** (Metrics) to structure the data
3. Radar uses web search and scraping tools, deposits findings into the knowledge base
4. Atlas pulls findings, builds a formatted Excel spreadsheet, uploads to Google Drive
5. You get back a summary with a download link — no manual steps

---

## The 18-Agent Team

Every agent has a defined role, personality, skill set, and operating rules. They work independently or collaborate through orchestration engines.

| Agent | Role | What They Do |
|-------|------|-------------|
| **VisionClaw** | Personal Assistant | Default conversational agent — handles general tasks, delegates complex ones |
| **Felix** | CEO / COO | Revenue strategy, task orchestration, multi-agent DAG decomposition |
| **Forge** | Staff Engineer | Code execution, engineering standards, infrastructure, security review |
| **Teagan** | Content Marketing | Social media strategy, content calendars, brand voice, ad copy |
| **Blueprint** | Innovation Lead | Skill creation, tool learning, self-improvement, capability expansion |
| **Chief of Staff** | Operations Director | System health monitoring, task routing, scheduling, daily operations |
| **Scribe** | Content Creator | Long-form writing, editing, SEO content, documentation, blog posts |
| **Proof** | Quality Reviewer | Proofreading, fact-checking, QA, content review, accuracy scoring |
| **Radar** | Intelligence Analyst | Market intelligence, competitive analysis, trend tracking, OSINT |
| **Neptune** | Deep Research | Academic analysis, overnight autonomous research, multimedia deep dives |
| **Apollo** | Revenue & Pipeline | Sales outreach, lead qualification, pipeline management, CRM |
| **Atlas** | Metrics & Reporting | Analytics, dashboards, KPI tracking, data visualization |
| **Cassandra** | CFO | Budgets, forecasting, P&L modeling, financial analysis |
| **Luna** | Legal & Compliance | Contract review, regulatory compliance, risk assessment, legal drafting |
| **Minerva** | Strategic Planner | Plan-of-record drafting, decision-theory analysis, Felix approval-loop partner; closes the auto-apply → strategic-plan loop for the proactive self-healing engine (R63) |
| **Robert** | Personal & Emotional-Life Specialist | Long-term personal context, journaling, emotional check-ins, pattern recognition, and practical next actions |
| **Hermes** | Growth Hacker | Acquisition experiments — pre-registered hypotheses, weekly launch/readout cycles, CAC-per-channel scoreboard, kill/scale decisions |
| **Echo** | UX Researcher | Voice of the user — grounds product decisions in real user needs, time-to-insight, closed feedback loops |

---

## Feature Overview

### AI & Intelligence

- **86 Curated AI Models in the Development Registry** with configured routing across supported providers. Bring your own provider credentials — availability and billing are governed by provider and account terms, not a promise of universally free inference.
- **Adaptive Model Discovery (R73)** — a daily background task scans OpenRouter's full catalog of 1000+ models, tier-classifies each by completion price (reasoning / powerful / balanced / fast), probes the Replit gateway for new releases, and emails the owner a ranked digest of new models worth adding to the registry. Hard caps prevent inbox spam (10 alerts/run max), lifetime dedupe prevents re-alerts, and silent days mean nothing changed.
- **Streaming Responses** via Server-Sent Events (SSE) — real-time token-by-token output
- **Thinking Mode** — explainable reasoning with decision traces for complex problems
- **Model Failover** — automatic fallback to healthy providers when one goes down
- **Context Window Management** — automatic conversation compaction that preserves every fact before summarizing
- **Cost Ledger with Token Telemetry** — every byte across every provider boundary is tracked in a per-tenant cost ledger; orchestrator bills callers automatically via `onTokenUsage` callbacks with row-level pg_advisory locks preventing double-counting

### Document & Content Production

- **PDF Reports** — executive-quality styled PDFs with cover pages, branded headers/footers, charts, and tables
- **Word Documents (.docx)** — professional documents with formatting, headers, and styles
- **Excel Spreadsheets (.xlsx)** — auto-formatted workbooks with formulas and conditional formatting
- **Google Slides** — automated presentation generation delivered to Google Drive
- **Charts & Diagrams** — Recharts visualizations and Mermaid.js diagrams rendered to PNG
- **PDF Form Filling** — fill existing PDF forms programmatically
- **Invoices** — professional invoices with line items, taxes, and branding

### Research & Intelligence

- **Autonomous Overnight Research** — configurable research programs that run autonomously, with LLM-judged experiment scoring and auto-deposit of findings into your knowledge base
- **Web Search** — powered by Perplexity with Wikipedia and Jina fallbacks
- **Deep Web Scraping** — Firecrawl integration for full-site crawling and markdown extraction
- **Trend Research** — parallel scanning across Reddit, Hacker News, Polymarket, and X/Twitter
- **Competitive Intelligence** — automated competitor analysis with structured output

### Memory & Knowledge

- **Semantic Memory Palace** — hierarchical memory organized by Wing and Room with three-tier recall (Hot/Warm/Cold)
- **Zero-Loss Compaction** — full pre-compaction transcripts archived and recoverable; every fact extracted before conversation summarization
- **Vector Knowledge Base** — RAG-powered knowledge retrieval with MMR diversity re-ranking
- **Temporal Knowledge** — subject-predicate-object facts with time validity tracking
- **Dialectic User Modeling** — three internal agents (Deriver, Dialectic, Dreamer) progressively build a profile of each user from conversations

### Multi-Agent Orchestration

- **Crews** — agent teams with defined roles, goals, and backstories working toward a shared objective
- **Flows** — event-driven workflow pipelines that chain agent actions
- **Minds** — 4-role deliberation system (Proposer, Critic, Synthesizer, Judge) for complex decisions
- **Auto-Orchestration** — the COO automatically decomposes complex requests into DAG task graphs and delegates to specialists
- **Subagent Spawning** — agents can spawn child agents for sub-tasks with full tool access
- **Chain of Debates** — multi-persona deliberation where 3-6 specialists argue complex questions from different perspectives

### Communication & Integrations

- **Email** — built-in email server with tenant-specific inboxes, send/reply, and notification handling
- **WhatsApp** — full bot integration for sending/receiving messages and approval workflows
- **Telegram** — bot integration for external interaction
- **Discord** — bot integration for team communication
- **Google Workspace** — Gmail, Calendar, Sheets, Docs, Slides, and Contacts integration
- **Google Drive** — primary storage for generated deliverables; every project gets a dedicated Drive folder with automatic backup

### Payment Processing

- **Stripe** — subscription management, checkout sessions, usage billing, and customer portal
- **Stripe Connect** — tenants can connect their own Stripe accounts for white-label payment processing
- **Coinbase Commerce** — cryptocurrency payments via hosted checkout
- **Coinbase CDP** — on-chain wallet management and balance checks
- **Usage Metering** — token tracking and feature access limits tied to billing tiers

### Voice & Media

- **Text-to-Speech** — ElevenLabs integration with 23+ voice profiles
- **Voice Conversations** — real-time voice input/output with configurable wake words
- **Image Generation** — DALL-E and Replit AI image generation
- **Video Production** — scene-based MP4 pipeline with parallel TTS, Ken Burns motion, 25+ transitions, and background music

### Project Management

- **Project Brain** — filing cabinet system linking conversations, files, notes, and Google Drive assets to projects
- **Scheduled Tasks** — cron-like automation for recurring agent work
- **Activity Logging** — comprehensive system-wide activity tracking
- **Agent Board** — visual overview of all agent activities and status

### Governance & Safety

- **41 Governance Rules** — built-in rules controlling agent autonomy and behavior
- **Process Governor** — enforces execution limits and approval requirements
- **Trust Engine** — evaluates safety and reliability of tool calls; high-risk actions require human approval
- **Prompt Injection Scanner** — detects and blocks malicious injection attempts
- **3-Layer Failure Recovery:**
  1. Self-correction retry with adjusted parameters
  2. Lean mode fallback to a lighter model on overload
  3. Backup agent reroute to mapped specialist
- **5-Part Failure Transparency** — when recovery can't fully succeed, the user is told what failed, why, what was tried, what succeeded, and what they should know
- **Critique Agent** — every response auto-evaluated on accuracy, completeness, relevance, and clarity (scored 1-10); low scores trigger auto-refinement

### Multi-Tenant Architecture

- **Full Tenant Isolation** — each tenant has separate conversations, memory, projects, files, settings, and billing; isolation extends to background services so the heartbeat engine's working memory, knowledge writes, daily notes, task list, and activity logs are all tenant-scoped at the storage layer
- **Per-Tenant WhatsApp/Email/Payment** — communication and payment channels isolated by tenant
- **Encryption at Rest** — Telegram bot tokens and WhatsApp/Baileys session credentials are encrypted with AES-256-GCM via a key derived from `SESSION_SECRET`; backward-compatible with legacy plaintext rows so existing installs auto-upgrade on first write
- **Team Management** — invite users, manage roles, and control access
- **API Keys** — per-tenant API key management for external integrations

### Developer & Admin Tools

- **Settings Dashboard** — comprehensive admin panel with tabs for General, Payments, Integrations, Voice, Tools, Security, Data, and Tenants
- **Diagnostics** — stuck task detection, health monitoring, provider latency testing
- **Heartbeat Engine** — system health monitoring with configurable check intervals
- **Auto-Tuner** — autonomous performance optimization that runs daily
- **Webhook System** — inbound/outbound webhook triggers for external automation
- **MCP Server** — Model Context Protocol server for AI tool integration
- **Backup & Restore** — automated daily backups to Google Drive with manual export/import
- **Vault** — secure credential storage for sensitive data

---

## Technical Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | React 18, TypeScript, Vite, TailwindCSS, shadcn/ui, Wouter, TanStack Query v5 |
| **Backend** | Express.js, TypeScript, Node.js 22.12+ |
| **Database** | PostgreSQL with pgvector extension, Drizzle ORM |
| **AI Routing** | OpenAI, Anthropic, Google Gemini, xAI Grok, OpenRouter, Perplexity |
| **Real-time** | Server-Sent Events (SSE) for streaming |
| **Auth** | Email/Password with HMAC-SHA256, Admin PIN, Replit OAuth, Google OAuth |
| **Validation** | Zod schemas with drizzle-zod integration |
| **Security** | Helmet, CSRF protection, rate limiting, injection scanning |
| **File Storage** | Google Drive (primary), local uploads (fallback) |
| **Payments** | Stripe, Coinbase Commerce, Coinbase CDP |
| **Voice** | ElevenLabs TTS (23+ voices) |
| **Search** | Perplexity, Firecrawl, Jina, Wikipedia |

---

## Repository Structure

```
client/                       # React frontend
  src/
    pages/                    # 40+ route pages
    components/               # Reusable UI components (shadcn/ui)
    hooks/                    # Custom React hooks
    lib/                      # Utilities, query client, API helpers
server/                       # Express backend
  chat-engine.ts              # Core AI conversation engine with streaming
  tools.ts                    # Legacy tool facade + dispatcher (strangler-fig split in progress)
  tools/                      # 428 total registered tools — per-domain modules (70+ domains) + shared middleware
    domains/                  # crm, finance, media, legal, knowledge, delivery, governance, ...
    middleware/               # Extracted dispatch middleware (policy, telemetry, tenant seam)
  routes.ts                   # 300+ API endpoints
  site-config.ts              # Centralized env-driven configuration
  seed.ts                     # Database seeding (190 declared / 271 development tables, 41 rules, 18 personas)
  heartbeat.ts                # Background task scheduler with model-catalog sync (R73)
  model-catalog.ts            # Daily OpenRouter catalog scan + gateway probe (R73)
  orchestrator-ledger.ts      # Per-tenant cost ledger with pg_advisory locks (R73.B)
  agent-manager.ts            # Autonomous agent orchestration
  subagents.ts                # Hierarchical agent spawning
  agent-channels.ts           # Internal agent messaging system
  google-drive.ts             # Google Drive integration
  stripe-connect.ts           # Stripe payment processing
  coinbase-commerce.ts        # Crypto payment processing
  whatsapp.ts                 # WhatsApp bot integration
  email.ts                    # Email server and tenant inboxes
  scaffolding.ts              # 75 corporate operation scaffolds
shared/
  schema.ts                   # Drizzle ORM schema (182 declared / 262 live — see docs/CURRENT_PLATFORM_TOTALS.md)
scripts/
  clean-for-release.sh        # Sanitize codebase for public release
FORK-SETUP.md                 # Detailed setup instructions
```

---

## Getting Started

### Prerequisites

- **Node.js 22.12+** (or a Replit account)
- **PostgreSQL** database
- **At least one AI provider API key** (OpenAI, Anthropic, Google, or xAI)

### Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/Huskyauto/VisionClaw-Agent-Public-Release.git
cd VisionClaw-Agent-Public-Release

# 2. Install dependencies
npm install

# 3. Set required environment variables
export DATABASE_URL="postgresql://user:pass@host:5432/dbname"
export SESSION_SECRET="$(openssl rand -hex 32)"
export OPENAI_API_KEY="sk-..."   # Or ANTHROPIC_API_KEY, XAI_API_KEY, etc.

# 4. Start the platform
npm run dev

# 5. Open your browser
# Visit http://localhost:5000
# Fresh deploys auto-redirect to /setup
```

### What Happens on First Run

In under 10 minutes, you go from `git clone` to a live dashboard with 18 agents, seeded governance, and a `/setup` checklist that tells you exactly what's configured and what's missing.

1. The database auto-creates all 258 live tables and full index set
2. 41 governance rules and 18 AI personas are seeded automatically
3. You're redirected to the **Setup Checklist** at `/setup` showing what's configured
4. Click **Create Account** — the first account becomes the admin
5. Start chatting — the AI is ready to work

### Environment Variables

See [FORK-SETUP.md](./FORK-SETUP.md) for the complete list. Here's the quick reference:

#### Required

| Variable | What It Does |
|----------|-------------|
| `DATABASE_URL` | PostgreSQL connection string |
| `SESSION_SECRET` | Random string for session encryption |
| One AI key | `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `XAI_API_KEY`, or `OPENROUTER_API_KEY` |

#### Recommended (Branding)

| Variable | What It Does | Default |
|----------|-------------|---------|
| `SITE_PLATFORM_NAME` | Your platform's display name everywhere | `VisionClaw` |
| `SITE_COMPANY_NAME` | Company name for branding | `Your Company` |
| `SITE_OWNER_EMAIL` | Admin contact email | _(empty)_ |
| `SITE_WEBSITE_URL` | Your public URL | _(empty)_ |

#### Optional (Unlock More Features)

| Variable | What It Unlocks |
|----------|----------------|
| `ELEVENLABS_API_KEY` | Voice synthesis (23+ voices, text-to-speech) |
| `FIRECRAWL_API_KEY` | Advanced web scraping and full-site crawling |
| `BROWSERLESS_API_KEY` | PDF generation and browser automation |
| `STRIPE_LIVE_SECRET_KEY` + `STRIPE_LIVE_PUBLISHABLE_KEY` | Payment processing and subscriptions |
| `COINBASE_COMMERCE_API_KEY` | Cryptocurrency payments |
| `GOOGLE_DRIVE_ROOT_FOLDER_ID` | Google Drive file storage and backups |
| `AGENTMAIL_API_KEY` + `AGENTMAIL_INBOX` | Email sending/receiving |
| `TELEGRAM_BOT_TOKEN` | Telegram bot integration |
| `DISCORD_BOT_TOKEN` | Discord bot integration |
| `X_API_KEY` + `X_API_SECRET` + `X_ACCESS_TOKEN` + `X_ACCESS_TOKEN_SECRET` | X/Twitter posting and search |

---

## Graceful Degradation

Features that aren't configured don't break the app — they gracefully disappear:

| Missing Config | What Happens |
|---------------|-------------|
| No email key | Email, WhatsApp pages hidden from sidebar |
| No Telegram token | Telegram page hidden |
| No Stripe keys | Payments page hidden from admin panel |
| No Drive folder | Files saved locally; Drive tools show "not configured" |
| No ElevenLabs key | Voice tools return "not configured" |
| No Firecrawl/Browserless | Scraping tools fall back gracefully |
| No Coinbase keys | Crypto payment features disabled |
| No OAuth client IDs | OAuth connection buttons hidden |

The `/setup` page gives you a real-time checklist showing exactly what's configured and what's not.

---

## Admin Settings

Once logged in as admin, the **Settings** page (`/settings`) gives you control over everything:

| Tab | What You Configure |
|-----|-------------------|
| **General** | Agent name, personality, default AI model, API keys, OAuth connections, billing |
| **Payments** | Stripe/Coinbase integration, pricing plans, subscription tiers |
| **Integrations** | Discord bot, public chat settings, webhooks, system hooks |
| **Voice** | Wake words, text-to-speech provider, voice profiles |
| **Tools** | Browser/search settings, code sandbox, safety limits, rate limiting |
| **Security** | Access PIN, auth health monitoring |
| **Data** | Backup to Google Drive (manual + automated at 3 AM UTC), export/import |
| **Tenants** | Multi-tenant management for agency deployments |

---

## Pages & Navigation

The platform includes 40+ pages organized by function:

**Core:** Home, Chat, Inbox, Email, Projects, Files, Documents

**AI Management:** Personas, Memory, Knowledge, Skills, Skills Marketplace, Agent Board, Agentic Operations

**Intelligence:** Research, Insights, Content Writing, Scheduled Tasks

**Communication:** WhatsApp, Telegram, Discord (with approval workflows)

**Admin:** Settings, Analytics, Activity Logs, Heartbeat, Team, API Keys, MCP, Webhooks, Channel Routing, Payments

**Public:** Landing Page, Architecture Overview, Login/Signup, Legal Pages (Terms, Privacy, About, Contact, Refund)

---

## Agentic Design Patterns

These are the patterns we actually use in daily production — not just research papers:

1. **Parallel Tool Execution** — read-only tools run concurrently via Promise.all; mutating tools execute sequentially for causal ordering
2. **Critique Agent / Self-Correction** — every response auto-evaluated across 4 dimensions (accuracy, completeness, relevance, clarity); scores below 6/10 trigger auto-refinement
3. **Chain of Debates** — 3-6 specialist agents argue complex questions from their domain expertise; synthesizes a recommendation with consensus level
4. **Tree-of-Thought Reasoning** — 2-5 distinct analytical branches evaluated by a meta-reasoning judge for optimal answers
5. **Auto-Orchestration** — complex requests decomposed into DAG task graphs with dependency tracking and parallel execution
6. **Dialectic User Modeling** — three agents (Deriver, Dialectic, Dreamer) progressively understand user preferences and behavior

---

## Deployment

> **Self-hosted only.** You must deploy on your own infrastructure — your own Replit account, your own server, your own Docker host. We do not provide hosting, shared instances, or managed deployments. Every fork runs independently with its own database, API keys, and configuration.

The primary application works on any Node.js 22.12+ hosting:

- **Replit:** Create your own Replit account, import the repo, set secrets in the Secrets panel, hit Run
- **Railway/Render:** Connect your repo, set env vars, deploy
- **Docker:** `docker-compose up -d` — includes PostgreSQL with pgvector, ready out of the box
- **VPS:** Clone, `npm install`, set env vars, `npm run dev`
- **Port:** Serves frontend and backend on a single port (default: 5000)

```bash
git clone https://github.com/Huskyauto/VisionClaw-Agent-Public-Release.git
cd VisionClaw-Agent-Public-Release
cp .env.example .env   # edit with your API keys
docker-compose up -d    # or: npm install && npm run dev
```

---

## About the Name

**VisionClaw Agent** is an independent AI agent platform — not related to the [Intent-Lab/VisionClaw](https://github.com/Intent-Lab/VisionClaw) project (a smart glasses AI assistant for Meta Ray-Ban). This repo is a standalone, self-hosted multi-tenant operations platform. It works with just an LLM provider and PostgreSQL — no external ecosystem required.

---

## Roadmap

Areas under active development:

- **Modularization** — Breaking down large server files (routes, tools) into domain-specific modules for easier navigation and community contribution
- **Type safety** — Incremental migration from `any` types to strict TypeScript interfaces
- **CI/CD** — GitHub Actions pipeline for lint, typecheck, and automated testing
- **Plugin architecture** — Making it easier to add custom tools and agents without modifying core files
- **API documentation** — OpenAPI/Swagger spec for the 300+ endpoints

Community contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Built With

VisionClaw Agent was originally built and hosted on [Replit](https://replit.com) — a collaborative cloud development platform that makes it easy to build, deploy, and share full-stack applications. Replit's integrated environment, managed PostgreSQL, one-click deployments, and AI-assisted development made it possible to go from idea to production-ready platform without managing infrastructure. If you're looking for the fastest way to fork and run your own instance, Replit is a great place to start.

---

## License

The repository source and documentation are licensed under the [MIT License](LICENSE).
That repository-level grant does **not** automatically license every component
that may be used with or referenced by the project: third-party dependencies,
hosted services, provider APIs, generated assets, and separately distributed
plugins retain their own applicable terms. Review the relevant component and
provider terms before redistribution or production use.

---

**Created by Robert Washburn** | huskyauto@gmail.com

---

## Revision History

Brief one-liners. Full play-by-play in [REVISIONS.md](REVISIONS.md).

| Round | Date | Headline |
|---|---|---|
| **R125+155+sec6** | 2026-08-21 | **Immutable harness provenance hardened.** Evaluation and learned runtime-addendum history now records a content-addressed, non-secret configuration fingerprint: typed capture profiles reject arbitrary persisted configuration, composite tenant references prevent cross-customer provenance links, and transactional activation preserves the active addendum if a replacement write fails. Verification: focused manifest tests, typecheck, production build, full 233-suite run, live development-database constraint/index verification, and independent final review. |
| **R125+155+sec5** | 2026-08-19 | **Tenant-isolation hardening now protects identity transitions, automatic analysis, commerce links, and password-reset credentials.** Account changes cancel stale cached work and replace credentials before tenant state is exposed, so delayed bootstrap/CSRF responses and platform retries cannot render or replay a prior customer’s work. Tenant-specific agentic analysis stays tenant-local; catalog/payment-link creation proves mission and outreach-sequence ownership before reuse or Stripe metadata creation; reset links pair their tenant identifier with an opaque 256-bit secret and lookup requires both that tenant and the keyed HMAC. Verification: 30 focused regressions, typecheck, production build, full 232-suite run, wiring audit, browser smoke test, and independent architect plus silent-failure reviews clean. |
| **R125+155+sec3** | 2026-08-19 | **Tenant-isolation audit remediation closes two HIGH findings and one MEDIUM.** Agent-run state changes bind run and tenant identity; automatic memory work is tenant-local, cursor-stable, prompt-bounded, and durable-flush ordered; approval claims record their audit step atomically and interrupted work recovers to a terminal state. |
| **R125+155+sec2** | 2026-08-19 | **Managed DB-skill prompt boundary hardened, agents disagree honestly, and generic videos hold attention more deliberately.** A HIGH was closed across every managed-skill path: unsafe content can no longer enter through alternate admin, marketplace, proposal, seed, or phantom-memory writers and later become a system instruction. One shared fail-closed storage boundary validates creates and locked final-state updates; prompt reads accept only active/enabled records and revalidate them independently; oversized content and demonstrated Unicode/confusable scanner evasions block; a repository guard prevents direct skill-table mutations outside storage. Universal persona guidance now separates emotional validation from endorsing unsupported claims. Generic video planning adds a real curiosity gap, delayed payoff, meaningful progression, and natural non-invented CTAs; the dedicated Built With Bob weekly recap remains unchanged. Verification: 25/25 focused checks, typecheck clean, 63 live skills audited with zero unsafe, two clean independent final reviews. |
| **R125+155+sec** | 2026-08-18 | **Sharper skill focus for every agent, plus a full-platform security review with three fixes.** Every skill handed to an agent is now tagged with its semantic fit to the current request (High/Medium/Low, with an explicitly named skill always winning) — strictly advisory and fail-open, so scoring problems fall back to the prior behavior. A weekly watchdog compares all skills pairwise and flags near-duplicates for merge or prune before they blur agent precision (first run: 70 skills, zero merge-worthy duplicates). The 72-hour security review (two independent passes over all sensitive areas plus every touched file) closed one HIGH — WhatsApp approvals are now locked to the approver's own workspace, closing a cross-tenant approval path on short-code collisions — and two MEDIUMs: evidence-confidence ratings restored end-to-end on research reports, and approval timeouts now honor the configured window instead of a hardcoded 2 minutes. |
| **R125+154** | 2026-08-17 | **One integrity rulebook for every self-improving loop, delivery emails that always carry a backup link, and publishing un-stuck.** A new loop-integrity governance skill (skills 52 → 53, 155 reference surfaces) puts every auto-apply loop — skill optimizer, research engine, jury auto-apply, repair autofix, plan-replay — under one 5-principle evaluator-integrity contract: the improved thing never reaches the judging thing, LLM-reviews-LLM stays advisory, held-out never-seen signals close the metric-gaming channel, quality fails open while safety fails closed, and any gate relaxation must itself pass the audit. Distilled from the AQuA and CUDA Agent papers plus the platform's own verifier-gaming incidents; architect-reviewed with zero corrections. Video and audio delivery emails now carry a permanent Google Drive backup link alongside instant-play whenever a Drive view link is available, and publish reliability was restored (stale auto-added port mappings removed from the deploy config). |
| **R125+153+sec** | 2026-08-14 | **Derived API recipes — watch a site once, then skip the browser — 5 new tools, 4 HIGH closed across 4 architect rounds before ship.** While an agent browses, the platform passively captures the site's own background data calls (per-tenant, in-memory, credentials structurally scrubbed before buffering); one $0-lane call distills them into a saved recipe; replay re-fetches the data browser-free in ~1s via an SSRF-jailed, connection-pinned fetch with every redirect hop re-validated (max 3). Review closed pre-ship: dead capture attach (feature would have silently never worked), redirect SSRF + DNS-rebinding TOCTOU, credential retention in captured bodies, and URL userinfo leakage — plus tenant-scoped re-verify updates and a `DERIVED_API_DISABLED` kill switch across all five tools. Tools 408 → 413, tables 228 → 229, indexes 676 → 679. |
| **R125+152** | 2026-08-13 | **"Best of the best" drafting program + model refresh + 72h review (0 CRITICAL/HIGH, 3 MEDIUM closed).** Paid deliverables draft each section via 3 parallel cheap-frontier models (DeepSeek V4 Pro 0813, GLM-5.2, Gemini 3.7 Flash) + a strong redrafter, fail-open to the free path; the same trio ships platform-wide as the MoA `premium` pool (metered spend owner-only under a daily ceiling). DeepSeek default → V4 Pro 0813; Gemini 3.7 Flash added escalation-only. Review fixes: Gemini 3.7 Flash priced in all three cost maps, ensemble tool description resynced to runtime, pricing/premium-pool regression tests pinned. |
| **R125+151** | 2026-08-13 | **Smarter tool choice from contrast notes + nightly plan pre-warm + Diagram Design skill + research-graph HIGH fix.** Contrastive tool-choice notes (arXiv 2601.12538) teach the router from near-miss tool picks; a nightly pre-warm builds the plan-replay cache before business hours; the Diagram Design skill (MIT, 27 diagram types) reaches all 18 agents; and the research evidence graph got its own `research_evidence_triples` table, fixing a HIGH table-collision finding. Tables 227 → 228, indexes 673 → 676, skills 154 reference surfaces. |
| **R125+150+sec** | 2026-08-11 | **Knowledge retrieval learns from use + flagship Claude models at $0 — 1 CRITICAL + 2 HIGH + 2 MEDIUM closed, every fix verified by a round-2 architect pass.** Every knowledge retrieval now records an access count and last-accessed time, and proven-useful knowledge wins ranking ties — strictly as a tie-breaker, so relevance always dominates. Platform-wide knowledge briefs are finally visible to semantic search. claude-opus-5, claude-opus-4-8, and claude-fable-5 now serve through the flat-rate lane at $0 (live-verified). **CRITICAL:** a failed boot migration can no longer silently break knowledge search — boot verifies the columns exist (schema-scoped) and logs the exact manual fix. **HIGH #1:** a broken search tier can no longer masquerade as 'no results' — a loud DEGRADED signal fires before the fail-open keyword fallback. **HIGH #2:** flat-rate Claude spend was recorded as metered Anthropic spend and counted against the daily circuit breaker — now excluded and ledgered at $0. **MEDIUMs:** permanent schema errors logged once; schema-scoped verification. Gates: type-check clean, wiring audit CLEAN, round-2 architect PASS. |
| **R125+149+sec** | 2026-08-10 | **Whole-project thorough code review — 4 HIGH + 2 MEDIUM closed, every fix verified by a round-2 architect pass.** **HIGH #1:** helper-agent spawning fell back to the admin tenant when no tenant id was supplied — now fails closed without a verified numeric tenant id, with the tool path forwarding the dispatcher-stamped trusted tenant and the admin route resolving the request tenant explicitly. **HIGH #2:** the inbound email webhook verified its HMAC over a re-serialized JSON body — it now verifies over the exact captured raw request bytes (stringify only as a dev fallback). **HIGH #3:** both user-upload routes backed files up to Google Drive with a public share link — vault backups are now private; only explicit customer deliverables get share links. **HIGH #4:** the CEO orchestrator pace gate soft-allowed on a database error with no concurrency bound — an in-memory reservation cap is now enforced unconditionally (reserve-then-check, release on cap hit), so a DB outage bounds rather than unbounds parallelism. **MEDIUMs:** credential-vault last-used updates tenant-scoped; chromium + all 5 ffmpeg capability probes run under a sanitized child environment (3 probe sites caught by the round-2 pass). Gates: tsc 0, suite 231 suites green, seamtests green, wiring audit CLEAN. |
| **R125+148+sec** | 2026-08-09 | **Rate-limit pace-not-kill + research avenue spreading + 72h security review round 4 — 2 HIGH + 2 MEDIUM closed, second-pass hardening applied.** Agents wait (≤70s) instead of dying on minute-window rate limits, with sibling-tool suggestions on minute denials and consolidate-don't-switch on hour/day (spend-ceiling evasion guard), avenue-spreading doctrine across all 18 personas + 10 regression tests. **HIGH #1:** competitor-research fetcher moved onto the shared SSRF jail (DNS-resolved private-address rejection + connect-time IP pinning, relative redirects resolved correctly, streamed 2MB byte cap). **HIGH #2:** weekly wedge digest fail-closed — DB failures report "metrics unavailable" instead of fake zero-traction recommendations; canonical wedge-tag matching. **MEDIUMs:** expensive-tool backstop restored to exact 48/48 parity; mission reply scan MISSION_ID strict decimal validation (malformed values no longer widen the scan to all missions). Second architect pass verified; suite 225 suites green. |
| **R125+147+sec** | 2026-08-06 | **Premium $497 AI Readiness Audit report + 72h security review round 3 — 3 HIGH + 2 MEDIUM + 1 LOW closed, 1 HIGH false positive probe-disproven, second architect pass PASS.** The self-serve audit deliverable is upgraded to the premium styled report (dark gradient cover, stats grid, branded sections). **HIGH #1:** checkout fulfillment trusted the mission id straight from Stripe metadata (app-writable — never trust it back) for cost attribution and review-queue linkage; the id is now resolved against the real mission AND gated on a post-approval stage before any use — invalid ids drop to null with a warning, fulfillment is never blocked. **HIGH #2:** a successful HTTP response with a corrupt body could previously ship a broken PDF to a paying customer; the styled renderer now runs a fail-closed integrity gate (minimum size, PDF magic bytes, a real parse, at least one page) before anything is written or persisted, with an automatic plain-renderer fallback. **HIGH #3:** the data-protection backup reads and purge child deletes now carry explicit tenant predicates. **False positive (logged):** the claim that a fire-and-forget cost write loses its mission attribution was disproven with a live Node probe (async context binds at continuation registration) — and a synchronous snapshot was added as defense-in-depth anyway, pinned by test. **MEDIUMs:** a prospect reply that pauses an outreach enrollment can no longer be overwritten back to active by an in-flight send (conditional tenant-scoped update, skipped rows excluded from the sent count); one pre-existing fallback deferred + documented in the known-gaps register. Gates: tsc 0, seamtests 85/85, full suite 223 suites green. |
| **R125+146+sec** | 2026-08-02 | **72h whole-app security review — 3 HIGH + 2 MEDIUM closed, second architect pass PASS.** **HIGH #1:** the capability-map API performed no tenant resolution and included per-agent blocked-tool policy edges — any authenticated tenant could enumerate exactly which tools every role is forbidden to use; the route now requires tenant resolution and returns policy edges only to platform admins (personas/capabilities stay visible to all). **HIGH #2:** one model was priced via a generic family prefix; an exact pricing row was added plus a new prefix-shadowing order guard in the pricing-drift suite — which immediately caught a second live shadowed-prefix mispricing, also fixed. The guard fails the build on any longer model id captured by a shorter first-match prefix. **HIGH #3 (pre-existing):** the email-reply endpoint never verified message ownership on the shared provider inbox — one tenant could reply into another tenant's thread; replies now require a tenant-scoped ownership match (404 on mismatch), pinned by a source-scan regression test. **MEDIUMs:** scratchpad reads fail CLOSED without tenant ctx; per-row scheduled-post status UPDATEs pin the tenant. Gates: tsc 0, seamtests 85/85, suite 173/173, wiring audit CLEAN (408 tools). |
| **R125+146** | 2026-08-01 | **Agent Insights — real agent scorecards, a live capability map, and step-by-step workflow replay.** Three new tenant-facing observability surfaces backed by 4 read-only, tenant-scoped API endpoints. **Agent Scorecards:** each agent's real 7/30/90-day track record — tasks + success rate from the activity ledger, actual spend + cost-per-task from the cost ledger, average quality /100 from the step grader, and the tenant's human-approval rate. **Capability Map:** a searchable goals → capabilities → agents → tools map from the live capability registry, including per-agent blocked-tool edges. **Workflow Replay:** replay any finished run step by step (agent, tools, duration, output, grader score + rationale, plus planned-but-never-executed steps), strictly read-only. Architect-hardened pre-ship: lifecycle log events filtered out of replay (no phantom steps), per-step grades joined exactly on the step number (off-by-one fixed), and replay text passes a widened redaction layer (emails, phones, Bearer/Authorization, cookies, connection-string credentials, key/password assignments, long opaque tokens) pinned by 14 dedicated tests. Gates: tsc 0, seamtests 85/85, full suite 170/170 suites green. |
| **R125+145** | 2026-08-01 | **Admin-auth consistency + whole-app 72h security review — 1 HIGH and 5 MEDIUMs closed, second architect pass PASS.** Admin rights are now consistent across both sign-in paths: `/api/auth/user` returns `isAdmin` for flagged admins (admin tenant OR the tenant `is_admin` flag), matching `/api/tenants/me`, and `isAdminRequest` honors the flag identically on the session-auth and token paths. Owner-email detection merges the primary owner-email secret with the legacy list, and the admin tenant can never be silently rebound to a different auth subject (binding only on empty or exact match). 72h review (3 parallel architect passes over 123 changed files + the sensitive core): **HIGH** — `replyToEmail` bypassed the outbound credential-redaction gate every regular outbound email passes through; fail-closed text+html gates added and pinned by a static regression test. MEDIUMs: internal event resolver resolves tenant once at entry and fails CLOSED when missing; usage-insights pricing map synced with the model refresh (first-match-wins ordering); voice conversations route through the tenant-aware client factory so per-tenant keys and subscription lanes apply; two wedge scripts gained tenant-scoped SQL. Gates: tsc 0, seamtests 69/69, full suite green, wiring audit CLEAN. |
| **R125+143** | 2026-08-01 | **All 18 agents fully wired — expanded scopes for 7 personas + completed capability registry + universal tool awareness + a five-layer persona-drift defense line.** Seven personas gain market-validated expanded scopes (reauthored natively, never copied): Teagan (AEO/GEO + AI-citation optimization), Hermes (paid-media ops under the CEO budget gate — $0 spend without approval, unchanged), Apollo (discovery-call prep / proposals / pipeline hygiene), Echo (cross-channel feedback synthesis + ethical-nudge review), Cassandra (FP&A / controller / investment memos / tax flags), Luna (DPO-grade compliance + vendor review), Proof (a11y / reality / perf checks) — every spend/approval and privacy boundary preserved, blocks written byte-identical to both identity source files AND the live DB. The cross-agent capability registry is completed for all 18 agents (Hermes, Echo, and Robert were previously invisible to cross-agent routing; Robert's stale role corrected). All 18 personas re-synced against the full 408-tool registry — wiring audit CLEAN (0 dead tools / 0 drift / 0 schema gaps / 0 orphans). A five-layer persona-drift defense line (identity drift both directions, operating-loop drift, tools-doc drift, unified persona-doc writers, fail-closed curated-doc staleness gate in the mirror build) locks agent identities to source of truth. 72h review (3 parallel architect passes over 127 changed files + the sensitive core): **0 security findings**, 1 HIGH correctness fixed (duplicate generated Drizzle declarations for 4 live self-repair tables — the orphan audit now scans the self-repair schema module). Gates: tsc 0, seamtests 71/71. |
| **R125+140+sec** | 2026-07-30 | **Self-repair conformance gate + corrupt-render delivery block + 72h review closing 2 HIGH fail-closed.** The guarded repo-surgeon gains a plan-vs-diff conformance gate: the declared edit scope is compared to the actual working-tree delta after every fix attempt — any undeclared touched file triggers automatic rollback, conformance is recorded per attempt, and a rollback counts toward the durable stop budget (fail-closed rollback pinned by the `repo-surgeon-conformance` suite). A video-finalize corruption gate verifies final artifacts BEFORE done/upload — invalid output fails CLOSED back to retryable with an incident report, so a corrupt render can never be delivered. Outbound email/reply/scheduled-post now report `outbound_quality_gate_degraded` on scanner fail-open. 72h review (3 parallel architect passes + wiring audit exit 0): server 0 CRITICAL / 0 HIGH; **HIGH #1** — the public-mirror build script accepted unknown flags and proceeded to a live force-push (strict allowlist, exit 2 fail-closed; same class swept into the escalation resolver + jury-queue drainer); **HIGH #2** — the client ErrorBoundary rendered raw `error.message` (now safe generic copy); MEDIUM sweep (observable catches, stale stats). Plus `glm-5.2` pricing drift fixed in both maps and the stale-string preflight gate cured of a glob@7 ESM-import break. |
| **R125+139** | 2026-07-28 | **Majority-rule autonomous repair + fail-closed mirror doc guards.** The 3-frontier-model repair jury's auto-fix gate moves from UNANIMOUS to STRICT MAJORITY (`majority >= floor(total/2)+1`): a 2/3 (3/4, 3/5…) FIX routes to the guarded repo-surgeon; a majority ACCEPT/REJECT terminally closes the incident with votes + rationale. Every guard intact + test-pinned — escalation-flag override, fix-direction concordance floor (0.45), protected-surface block, `REPAIR_AUTOFIX_ENABLED` opt-in, typecheck/test-or-rollback, prod refusal; new invariants cover even jury sizes (2-of-4 must NOT act) and malformed vote cardinality (empty votes ⇒ 3-seat default). 66/66 unit tests, tsc 0. The public-mirror build gains fail-closed persona-count (stage 0.1) + tool-count (stage 0.2) doc guards — docs/personas.md and docs/tools.md drift vs the live registry/DB aborts the build; comparison logic lives in a pure lib with a DB-free test suite wired into the canonical run. 72h whole-app review (2 parallel architect passes): 0 CRITICAL / 0 HIGH server-side; two stale marketing stats caught + fixed. |
| **R125+138** | 2026-07-28 | **Personas 16 → 18 — Hermes (Growth Hacker) + Echo (UX Researcher) onboard per the 9-step safety checklist**, both on the moderate intent gate with persona-voice refusals; intent-gate hardening adds hint-tier + fallback-regex coverage for 3 previously under-covered restricted categories. AHB adversarial suite extended (10 attack + 6 benign fixtures): 68/68 pass, ASR 0%. |
| **R125+137.94** | 2026-07-27 | **The AI Fix Kit ships for the $1,997 done-for-you audit tier (tools 407 → 408), and a 72h full-platform sweep hard-locks done-for-you orders to human review — they can never auto-ship.** New `generate_audit_fix_kit` tool: SSRF-jailed site re-fetch, 3 LLM files grounded only on fetched content + audit findings with fail-closed domain-grounding validators (14/14), deterministic robots additions + README, collision-proof zip (orderId slug + random hex — feature-round HIGH fix), `<<<UNTRUSTED_PAGE_CONTENT>>>` prompt-injection boundary, attached to the HITL review item; kit failure holds the order for manual review, never blocks the audit PDF. **72h sweep (3 parallel architect passes over all 87 files touched in 72h + the sensitive core): 1 HIGH** — `canAuto` in the Stripe webhook handler could auto-ship a DFY order past the review queue; now hard-gated `!isDfyManualOnly` (done-for-you = manual-only, always). **1 MEDIUM** — explicit `TOOL_POLICIES.generate_audit_fix_kit` row (sensitive/structured-args/trustedPersonasOnly). 1 MEDIUM deferred + documented (webhook-level DFY e2e harness). Gates: tsc 0, suite 155/155, seamtests 69/69, wiring audit CLEAN (408 tools). |
| **R125+137.89 → +137.93** | 2026-07-26 | **The AI-spend meter is hardened against multi-counting** — a 72h full-platform sweep (3 parallel architect passes + wiring audit CLEAN) closes a HIGH where the cost-tracking wrapper mutated the shared cached SDK client: stacked wrappers recorded one API call N times in the cost ledger and raced tenant billing attribution; rebuilt as a request-local Proxy facade (probe-verified exactly 1 record per call). A Google Vertex AI express provider lane goes live (x-goog-api-key auth, OpenAI-compat endpoint, $0 cost-safety policy untouched, verified end-to-end); the nightly isolation audit's 77 kept severe findings all verdict FALSE POSITIVE across 8 parallel read-only passes; and the nightly skill optimizer gains a fail-open behavior-shift pre-jury filter that culls inert candidates before any paid jury call (kill switch `SKILL_OPT_SHIFT=off`, 15 hermetic tests). |
| **R125+137.85 → +137.88+sec** | 2026-07-25 | **claude-opus-5 becomes the default Anthropic flagship, a Grok 4.5 review triage ships three fail-safe governance upgrades, a tenant-isolation triage campaign verdicts all 256 kept severe findings behind a new fail-closed suppression allowlist, and a sixth 72h post-edit review closes 6 findings — release window R125+137.85 → +137.88+sec.** **.85 — claude-opus-5 default flagship:** verified live against the provider's live model list + OpenRouter ($5/$25 per M, 1M context, 128K max output) and wired across the provider registry, MoA proposer/aggregator rosters, context-window guard, cost-ledger + resource-predictor pricing, Claude Runner, escalation valve, and persona doctrine (all personas re-synced); the $0 lane pin is deliberately untouched. **.86 — Grok 4.5 review triage (3 items):** a fail-closed proof-of-premise demand-validation gate BEFORE any Revenue Mission experiment draft; outcome-driven learning promotion turning graded deliverables into generated eval seeds for the nightly skill optimizer (new `deliverable_grade_events` table — tables 224 → 225; fail-open, the hand-authored registry is never mutated); and mission-level hard budget caps failing closed (pre-launch headroom assert + post-spend auto-pause on evidence writes). **.87+sec — tenant-isolation triage campaign:** all 256 kept severe findings verdicted by 8 parallel read-only passes — 250 verified FALSE POSITIVE, 6 REAL fixed in code (admin-only project scoping, flow-step ownership check, tenant-scoped delivery idempotency, customer/project ownership checks on invoicing/expenses); a new fail-closed suppression allowlist (exact file + deterministic structural anchor + verbatim issue fragment; a null anchor can NEVER suppress; suppressed findings stay in the report audit trail) survived three architect over-suppression rounds incl. a generation-contract test proving every shipped anchor reproducible from snapshot findings. **.88+sec — sixth 72h post-edit review (3 architect slices + 2 fix-confirmation passes): 6 fixes** — a HIGH customer-ownership check on interaction logging, invoice creation wrapped in a DB transaction, allowlist suppression gated on full audit coverage, the Claude Runner default model bumped to claude-opus-5, and the commerce SKU unique index made composite `(tenant_id, sku)` with the matching `ON CONFLICT` target (regression caught by the architect's second pass, runtime-verified via a rolled-back probe); 1 FALSE POSITIVE logged (api-v1 scope enforcement is central via the auth middleware). Gates: tsc 0, seamtests 69/69, suite 152/152, wiring audit CLEAN. |
| **R125+137.83 → +137.84+sec** | 2026-07-24 | **The platform starts watching the external threat landscape, pre-compaction handoffs become proactive, session memory injection gains tuning knobs, and a fifth 72h whole-app security review closes 1 HIGH kill-race in the Revenue Missions launch path with a final 0 CRITICAL pass.** **.83:** a $0 / no-LLM / no-DB weekly external threat-intel feed sha256-diffs two external AI-agent attack/research feeds against local state and keyword-maps NEW entries to the threat model's coverage classes — wired as advisory weekly-maintenance Pass 18 (YELLOW-never-RED, fail-open); plus a proactive pre-compaction handoff trigger and `MEMORY_PROACTIVE_MAX_INJECTED` / `MEMORY_PROACTIVE_MIN_CONFIDENCE` knobs on session-start context injection (fail-open env parsing). **.84+sec — fifth 72h whole-app review (3 parallel architect passes, loop-until-clean): 0 CRITICAL.** 1 HIGH fixed — the Revenue Missions kill-race: the launch path now persists `sequence_id` via a guarded `UPDATE … WHERE status='launching' AND sequence_id IS NULL RETURNING id` and throws on 0 rows, with the final 'live' UPDATE guarded `AND status='launching'` — a concurrent kill can no longer race a launch into a zombie live experiment. MEDIUMs fixed: Stripe webhook paid gates fail CLOSED on a missing `payment_status` (dispatcher AND checkout-completed handler); an admin route moved inside the admin-gated block; stale stats resynced; the threat-intel feed made truly advisory (always exit 0, loud stderr, 2MB body cap); 3 raw fetches moved onto `fetchWithTimeout` with try/continue polling. Gates: tsc 0, suite 150/150, seamtests 69/69, wiring audit CLEAN; second architect pass PASS. |
| **R125+137.80 → +137.82+sec** | 2026-07-24 | **The Loop Engineering playbook lands as a live capability, the Gold Exemplar Library goes live (tables 223 → 224), and a fourth 72h whole-app security review closes 2 HIGHs in the Revenue Missions launch path with a final 0 CRITICAL / 0 HIGH pass.** **.80 — Loop Engineering:** a new operational runbook captures 7 goal-based iterative-fix loops — Type Error Killer, Test Gap Closer, Dead Code Sweeper, Dependency Updater, Pattern Migrator, Lint Fixer, Doc Gap Filler — each with Goal / Rules / Verify-after-each-step / Exit-when structure, adapted with the gate-suite, 2-failed-corrections, and never-weaken-a-guard rules; registered as a live capability and ingested into agent knowledge so all personas discover it (skills 43 → 44 platform runbooks, 144 reference surfaces; capabilities → 131). **.81 — Gold Exemplar Library:** a new tenant-scoped `deliverable_exemplars` table (tables 223 → 224; sha256-deduped, cap 5 auto-graded per tenant+format, owner-marked exemplars never evicted) — deliverables graded ≥90 are captured fire-and-forget (fail-open) and injected as top-2 few-shot guidance into every future deliverable of the same format; the grading tool gains an optional content excerpt; 5 pipeline input hints updated; runtime-probed for store / fetch / tenant isolation / below-bar. **.82+sec — fourth 72h whole-app review (3 parallel architect passes, loop-until-clean ×4): 0 CRITICAL.** 2 HIGHs fixed in the Revenue Missions launch path: a silent rollback-catch removed in favor of a composite error, stale-'launching' claim recovery made reachable via a stale-claim gate, and the duplicate-send window closed by persisting the sequence id immediately after creation — before enrollment. 2 MEDIUMs fixed (reply-scan token no longer persisted in raw evidence; stale stats resynced), 3 deferred-accepted with documented rationale. +5 regression tests (mission guards 138/138). Gates: tsc 0, suite 150/150, seamtests green, wiring audit CLEAN; final architect pass PASS. |
| **R125+137.77+sec → +137.79+sec** | 2026-07-23 | **A second 72h security sweep closes 2 HIGHs + 3 MEDIUMs on the Stripe paid-state gate and fulfillment tenancy, Revenue Missions lands its validation gate + per-tenant capital pool, and a third 72h whole-app review comes back 0 CRITICAL / 0 HIGH.** **.77+sec — 2 HIGHs:** the Stripe paid-state gate now sits at the TOP of the delivery-event handler — no fulfillment handler (setup fee, subscription activation, paid flips, delivery) can fire on an unpaid delayed-payment completion, with `async_payment_succeeded` re-entry and idempotent handlers making paid-event replay safe; the heartbeat delegate route gained strict Zod validation. **3 MEDIUMs:** audit fulfillment tenant identity fail-closed; a write-time SSRF assert on connector base URLs (HTTPS-only, no internal hosts/IP literals); paid-flow tenant derived from the env-configurable owner-tenant single source of truth. **.78 — Revenue Missions validation & capital:** a deterministic $0 pre-launch validation gate (40/30/30 scoring, threshold 70, fail-closed ABOVE every experiment insert), a per-tenant agent-capital pool (tables 222 → 223; unseeded = no ceiling, seeded = 25% risk ceiling) with idempotent realized-margin settlement (advisory lock + CAS), and retrospective→scanner advisory re-ranking; the auto-approve tier was explicitly REJECTED — human approval stays fail-closed by design; guard tests 81 → 133. **.79+sec — third 72h whole-app review (3 parallel architect passes over ~120 files + the sensitive core): 0 CRITICAL / 0 HIGH.** 2 MEDIUMs fixed — a durable capital-settlement retry sweep (idempotent, degraded-sweep telemetry; double-settle race verified safe on a second pass) and a public changelog resync. Gates: tsc 0, mission guards 133/133, suite 150/150, seamtests 69/69, wiring audit CLEAN, stale-strings CLEAN 13/13. |
| **R125+137.73+sec → +137.76+sec** | 2026-07-23 | **The platform closes its first full sell-and-fulfill loop and burns down the tenant-isolation audit backlog, capped by a 72h whole-app architect review.** **.73+sec — tenant-isolation burn-down:** all 99 kept HIGH/CRITICAL nightly-audit findings triaged in 5 parallel passes — 17 REAL fixed across 15 sites (fail-closed tenant identity in storage/compaction/data-protection, ownership checks across revenue-missions/business-tools/agent-channels, scoped SELECTs, tenant defaults removed with a live schema ALTER), 82 named-benign false positives, and the nightly audit gained a strict suppressible system-sweep pattern. **.74 — sell & fulfill closed:** a products DB catalog (path-validated at register AND webhook lookup), 3 owner-only commerce tools (tools 404 → 407; Stripe calls carry deterministic idempotency keys), and a self-serve audit product that auto-fulfills on Stripe payment with post-purchase sequence enrollment. **.75 — Revenue Missions gap closures:** a mission retrospective hook (0-100 scoring + lessons/ROI on kill/scale), a fail-closed pre-spawn budget gate (explicit null-spend refuse), and a $0/no-LLM background opportunity scanner (proposal-only, capacity-guarded); guard tests 60 → 81. **.76+sec — 72h whole-app review (3 parallel architect passes):** 1 HIGH closed (a paid webhook hardcoded the owner tenant; now derives it from the env-configurable single source of truth) + 3 MEDIUMs (tenant-scoped atomic soft-delete with RETURNING; the compaction memory extractor now routes through the storage-boundary PII redaction guard — closing the last durable-store redaction bypass; the experiment concurrency cap is race-proofed with a per-tenant advisory transaction lock after round 2 correctly rejected a bare count-guard at READ COMMITTED). Gates: tsc 0, suite 150/150, seamtests 69/69, guards 81/81, architect PASS. |
| **R125+137.66 → +137.72** | 2026-07-23 | **The Revenue Missions engine ships end-to-end (S1–S5) — the platform can propose, draft, and run capped revenue experiments under owner-only gates, with every claim backed by verifiable evidence — plus a 72h architect review closing one HIGH owner-gate finding.** **S1+S2 (.66):** 3 new tables (tables 218 → 221), a deterministic mission stage machine (kill-from-any-stage), an owner-only 7-endpoint router, and a read-only Gmail sample harvest → draft packet with zero send paths pre-approval; hard caps clamp at 25 prospects / 3 contacts / $25 per experiment — mission rows can tighten, never raise. **S3 (.67):** approve → capped outreach send with a race-safe claim + rollback, a fail-closed pre-send spend gate, a mandatory opt-out line, and a read-only reply scan feeding deduped evidence. **S4 (.68):** the Stripe evidence hook (fail-closed metadata, per-refund identity, post-approval stage gate) + an admin mission console. **S5 (.69/.70):** 5 owner-only mission tools (tools 399 → 404; approve/kill deliberately NOT tools — human-in-the-loop only), an autonomy ladder (reinvestment 10% / $250 cap), a capital allocator + portfolio review, an evidence-gated scoring rubric, and a max-3-concurrent-experiments cap enforced fail-closed above the draft insert. **Security (.71/.72):** a 72h whole-app review closed ONE HIGH — an owner-only tool gate had hardcoded the owner tenant and diverged from the env-configurable single source of truth; mission AND cost-ledger owner tools now derive the owner tenant from one place, pinned by env-driven regression tests; all other sensitive surfaces verified clean. Gates: tsc 0, suite 150/150, seamtests 69/69, 89 guard tests, architect PASS. |
| **R125+137.65+sec** | 2026-07-22 | **72h full-app review round 4 — the platform's most sensitive core (intent gate, tool policy, dispatcher, chat engine, auth, storage) comes back CLEAN across 3 parallel architect passes over 110 changed files, and the last isolation gap in the autonomous wake scheduler is closed fail-closed.** The scheduler that wakes agents for future work now refuses to write anything without a verified positive-integer tenant identity — guarded before any database write and pinned by a 7-case regression test added to the permanent suite. A flagged `/api/v1/a2a` scope concern was verified FALSE POSITIVE (scope enforcement is central: `authMiddleware` → `checkApiKeyScopes` with the `POST /api/v1/a2a → chat` rule). Rounds 2–4 of the 72h series total: 5 MEDIUM tenant-isolation findings closed, 0 CRITICAL/HIGH. Gates: tsc 0, seamtests 69/69, suite 149/149, preflight-stale CLEAN, architect PASS. |
| **R125+137.59 → +137.64+sec** | 2026-07-22 | **The platform starts learning from its own tool choices and opens an agent-to-agent front door** — all five Kimi-K3 review recommendations land (condition-based wakes, episode playbooks, outcome-learned persona routing, inbound A2A task acceptance via JSON-RPC 2.0, an Autonomy Scoreboard), a record-only tool mis-pick telemetry ledger goes live, the TOOL RECALL doctrine makes every persona re-scan its full inventory before saying "I can't", a production maintenance-cron incident is fixed at the root, and two 72h security review rounds close four MEDIUM tenant-isolation findings. |
| **R125+137.51 → +137.58** | 2026-07-21 | **The platform starts auditing its own model reality — every hardcoded model id verified weekly against LIVE provider lists (Pass 16) and every pricing map against live OpenRouter rates (Pass 17); a CRITICAL tar CVE patched; a 72h review lands two remediation batches; every autonomous loop gets a mechanically-proven L0–L3 readiness grade.** **R125+137.51:** Loop Doctor L0–L3 rubric — per-loop grades with mechanically-proven kill-switch/attempt-cap/run-log evidence (declared-but-absent token = ERROR); fleet L3=3, L2=6. **R125+137.52:** wiring-audit health pass closes 9 orphan tables (introspect script's hardcoded list predated the research/sandbox/social tables). **R125+137.53:** CI-failure backlog triage — 48 digest items → 4 root causes, all fixed, incl. a CRITICAL tar CVE (GHSA-vmf3-w455-68vh) patched via surgical lockfile bump (0 critical vulns); silent-failure HIGH budget locked DOWN 53→52. **R125+137.54:** 72h remediation batch 1 — sandbox tool handlers admin-tenant-gated, Zod/tenant validation on sandbox PATCH + insights-apply + agentic sweep, seed heartbeat DELETE sentinel-restricted, portfolio script onto the mandatory delivery pipeline. **R125+137.55:** self-healing scorer model — pinned id verified against live /v1/models, LOUD fallback to the newest live Sonnet on retirement. **R125+137.56:** model-currency audit (weekly Pass 16) — first run caught 4 retired dated Anthropic ids still serving as the DEFAULT fallback across ~20 active files, all swept to live aliases. **R125+137.57:** model-pricing audit (weekly Pass 17) — all 3 pricing maps verified against live OpenRouter rates; first run reconciled 28 stale prices. **R125+137.58:** 72h remediation batch 2 — ~20 research-engine sites gain explicit tenant filters, 5 research routes Zod-validated, gmail refresh log redacted to an allowlist, skill-seeker fails closed on missing tenant, tables count resynced to the live 216. Gates: tsc 0, seamtests 69/69, suite 147/147, cost 49/49, preflight CLEAN, architect PASS. |
| **R125+137.45 → +137.50** | 2026-07-20 | **The platform starts working ahead of you — Proactive Commitment Drafting turns approaching deadlines into ready-to-approve HITL draft cards (structurally send-incapable); a CRITICAL credential-file leak in the uploads sync is closed with a boot-time dotfile purge; all 10 maintenance crons are prebundled so production can never lose them; a 10-file god-file cleanup locks its ceilings DOWN; and an IdeaBrowser MASTER sweep simulates the best of the 256-idea scored archive (winner: AI-Native Readiness Audit, ~$38.9k probability-weighted expected profit).** 72h retrospective (3 architect passes over 80 files / 223 commits) closed 1 MEDIUM (per-tenant boot-backfill skip check) + 3 LOW. Gates: tsc 0, suite 147/147, seamtests 69/69, wiring CLEAN, preflight CLEAN. |
| **R125+137.41 → +137.44** | 2026-07-19 | **The Simulation Sandbox becomes actionable — jury-vetted promotion of sandbox findings into a reviewed Improvement list (never auto-apply), TTL retention, and honest INCONCLUSIVE verdicts — plus a weekly IdeaBrowser money-scenario pipeline and a review/sync round with permanent race-regression pins.** **R125+137.41 (72h review, 2 HIGH + 1 MEDIUM):** an `INCONCLUSIVE` verdict added to BOTH sandbox report unions — a run with zero replays, zero graded results, or more errors than successes can never collapse to a reassuring NO_CHANGE (CRITICAL/DRIFT still win); grading failures emit `[sandbox-grade]` telemetry, failed-status UPDATE catches log loud, and a read-time `stale` marker (running >30 min) surfaces on the sandbox routes + an ecosystem-health `staleRunningCount`. **R125+137.42:** the IdeaBrowser weekly money-scenario pipeline — a Monday cron ingests 7 days of captured business ideas, scores them, runs per-idea scenario simulations producing `successProbabilityPct` + probability-weighted `expectedProfitUsd`, ranks the top 5, and delivers the report through the delivery pipeline + owner email (safe `--test` mode with zero side effects; live run verified). **R125+137.43:** a new `sandbox_promote` tool (trusted-personas-only, sensitive/HIGH fail-closed policy; tools 398 → 399) routes sandbox findings through the 3-frontier-model jury into a durable `sandbox_improvements` table — a `jury_pending` row is INSERTed BEFORE triage so a jury failure leaves an auditable record; ACCEPT/FIX → approved, REJECT → rejected, anything else escalates; nothing ever auto-applies. Plus admin GET/PATCH routes, an Improvement list card on `/admin/sandbox`, and weekly TTL retention (improvements survive run deletion via `ON DELETE SET NULL`). **R125+137.44:** permanent promote-race regression pins in the canonical suite (concurrent promotes of the same run can never double-insert or double-triage), the stale-string preflight gains a `scripts/` surface rule (stale counts in operator scripts now trip CI), and every marketing/dashboard/README surface resynced. Gates: tsc 0, seamtests 69/69, suite 146/146, wiring audit CLEAN, preflight CLEAN, architect PASS. |
| **R125+137.30 → +137.40** | 2026-07-19 | **The Simulation Sandbox contract completes S1–S5 — the platform can replay its own past safety decisions and model choices offline, under a hard per-run spend cap, and report what WOULD have changed.** `sandbox_run`/`sandbox_report` registered as a born-migrated domain (fail-closed tool policies, trusted-personas-only; tools 396 → 398), sandbox tables extracted to `shared/models/sandbox.ts` (tables 213 → 215), a `/admin/sandbox` admin UI over admin-gated launch routes (5s-wait/202-detach with race-safe timer cleanup), Sandbox probe #16 on the ecosystem-health dashboard, and the model-swap helper's cap clamped to the shared `MAX_PER_RUN_CAP_USD = 5` (architect-caught drift from 50). E2E smoke replayed 5/5 live safety decisions with verdict NO_CHANGE. Also in the window: a metered escalation valve for the self-repair loop (exactly ONE frontier diagnostic turn on a prior-collapse stall — judgment only, fail-OPEN, never on the final attempt), two standing-registry model registrations (`meta/muse-spark-1.1` paid + `nvidia/nemotron-3-ultra-550b:free` — neither touches the jury pools or the frontier reserve), the weekly video recap made self-healing and incident-proof (explicit date-window extraction cures the wrong-week incident; labeled weight-fact extraction cures the wrong-numbers incident), and a Tool Reliability card (SQL-bounded worst/top-N with redacted failure reasons). Gates: tsc 0, seamtests 69/69, suite 146/146, sandbox tests 16/16, architect PASS. |
| **R125+137.26 → +137.29-review** | 2026-07-17 | **An external frontier-model code review of this very repo, triaged end-to-end — the owner's email purged from every server runtime path, the changelog becomes data, the mirror gains a DDL schema snapshot + fail-closed stats refresh + tagged releases, an `: any` ratchet gate lands, Kimi-K3 joins as a frontier reserve, and a 72h review closes 3 MEDIUMs with permanent regression pins.** **R125+137.26:** `moonshotai/kimi-k3` (1M context) registered across all 5 model maps as a frontier RESERVE — never in the standing proposer set; a pure gate fires at most one backfill call, only when a main-round frontier proposer fails on the metered path (9/9 gate tests). **R125+137.27:** an external Kimi-K3 review ran against this public mirror; every finding was re-verified on main and the hardcoded owner email was removed from ALL server runtime paths — policy seeding, inbox-quarantine allowlist, ingest identity (new `GMAIL_INGEST_ADDRESS` env, fails closed loudly when unset), and the security.txt contact chain are now env-driven, with fail-closed refusal wherever the address is missing. **R125+137.28:** the mirror build refreshes the authoritative platform-totals doc BEFORE copying (fail-closed if still dirty — the count doc can no longer ship stale) and a ratchet-DOWN-only `: any`/`as any` budget gate (baseline 6,949) runs as weekly-maintenance Pass 14. **R125+137.29:** the 190-entry changelog extracted to data (`updates.json` + a 42-icon map), the mirror emits `docs/schema-snapshot.sql` via pg_dump so forkers can diff DDL between snapshots, and every mirror push is now stamped with a `r125.137.x` tag + GitHub Release. **72h review (2 architect rounds):** 3 MEDIUMs closed fail-closed — an api-v1 conversation-messages query re-anchored on a tenant-scoping JOIN + tenant filter, the tag-release CLI rejects unknown flags before any GitHub call, and the any-budget gate stops safely on an unreadable scan file with the baseline untouched — each pinned by a permanent regression test (suite 144/144). |
| **R125+137.23 → +137.25-review** | 2026-07-16 | **The platform learns to retire its own dead tools and forge new ones from unmet demand, the tool-router gains a hard cap, the public API speaks the AG-UI protocol, and a 72h review closes 2 MEDIUMs.** **R125+137.23:** a Tool Eviction/Retirement loop — a flag-only classifier with human-in-the-loop approvals (exemptions fail CLOSED via strict parsing, a registry sanity guard, and a ≤10-candidates/run dedupe; 20 candidates queued across the first 2 runs) — plus Tool Forge Phase 2, which turns recorded unmet-capability demand into budget-claimed LLM module proposals (≤1/run, nothing ever auto-lands); both run as weekly heartbeat crons. **R125+137.23-fable:** external-review follow-ups — the admin PIN check consolidated onto the one canonical peppered hasher, curing a boot reconciler that had been silently re-downgrading the stored hash to a public static salt every boot; a static guard test pins the salt literal to its single legitimate home. **R125+137.24:** a verified external-review finding fixed — the tool router could exceed its own `maxTools` budget with no slice-back; a new pure `enforceToolCap()` trims by priority order at both overshoot sites, never trims always-included tools, leaves escape hatches deliberately uncapped, and logs per-turn trim counts + a schema-token estimate (invariant tests in the suite). **R125+137.25:** an AG-UI protocol adapter — `POST /api/v1/agui/run` on the public API v1 surface (Bearer key, chat scope, with a static scope-parity guard test pinning every mounted api-v1 POST to an auth rule) replays a completed chat turn as ordered AG-UI SSE events (RUN_STARTED → TOOL_CALL_* → TEXT_MESSAGE_* → RUN_FINISHED/RUN_ERROR); fail-closed thread parsing, tenant-scoped continuation, keepalives + timeout race + client-disconnect handling. **72h review (2 architect rounds):** 2 MEDIUMs closed — a public checkout error handler was logging raw provider error objects (now message + type/status/requestId only), and the scope-parity guard test was bypassable (rewritten to a structural comment-stripped parse with first-match-wins semantics mirroring the runtime checker). Gates: tsc 0, stale-string preflight CLEAN, seam tests 68/68, suite 143/143, wiring audit CLEAN. |
| **R125+137.20 → +137.22** | 2026-07-15 | **Six OpenClaw-inspired native features + seeded-fraud judge proof + spec-vs-test authority + a Drive connector-lookup fix + a clean 72h review (indexes 626 → 627).** **R125+137.20:** the Google Drive connector lookup now falls back to the unfiltered connection list when the filtered query returns 0 items, curing broken document uploads, memory backups, and reconnects (verified live). **R125+137.21 (Fable-method borrows):** seeded-fraud completion fixtures in CI prove the deterministic verification layer fails CLOSED against a deliberately gullible LLM judge (a live probe caught 4/4 planted frauds), and a spec-vs-test authority rule in the repo-surgeon forces "cannot fix" on any spec/test conflict — authoritative at the executor and pinned by an adversarial regression test. **R125+137.22 (OpenClaw-inspired, all native):** a tenant-guarded, PII-redacted, race-safe commitments/open-loop miner (unique partial index + ON CONFLICT — indexes 626 → 627); a summary-quality audit with a deterministic fallback wired as a fail-open backstop at the conversation-compaction chokepoint (a failed compaction can no longer silently lose file paths or identifiers); operator-text-as-untrusted wrapping; first-failure-wins health root-cause ordering; a skill code-safety scanner; and a record-only egress telemetry ring buffer. **72h review:** 1 HIGH closed (the summary-quality lib had zero runtime callsites — now wired), 2 MEDIUM closed (two public/tenant routes moved onto centralized Zod validation), 1 FALSE POSITIVE logged (a cross-tenant read already admin-gated at dispatch). Gates: tsc 0, build 0, seam tests green, stale-string preflight CLEAN, architect PASS twice. |
| **R125+137.14 → +137.19** | 2026-07-14 | **Skill-optimizer evaluation upgrades + two god-file splits + Tool Forge Phase 1 + a clean 72h review — no advertised-count change, all gates green.** **Skill-optimizer:** RULER-style relative group ranking added as a measure-first, NON-blocking third judge lane in the evaluator A/B (one anonymized, seed-shuffled group-ranking call per case; parsing fails CLOSED, runtime fails OPEN, never touches the apply decision; kill switch `SKILL_OPT_RULER=off`); plus prior-collapse detection — an embedding-space near-dupe tracker over prior failed/rejected proposals (fail-OPEN on every path, kill switch `PRIOR_COLLAPSE=off`), wired opt-in into the skill-optimizer and repo-surgeon so a semantic re-proposal of an already-rejected/failed change skips the spend and escalates instead of looping. **God-file splits:** the `server/routes.ts` monolith had its Tier-1 auth/tenants/admin endpoints extracted verbatim (≈7,794 → 7,329 lines, behavior-preserving) alongside a new regression proof that the code-execution sandbox's real control is the VM layer (the keyword blocklist is defense-in-depth only); and tools-layer split slice S34 moved `google_workspace` out of the legacy `tools.