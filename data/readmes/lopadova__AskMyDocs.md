# AskMyDocs — AI Hub & Intelligent Agentic Platform for the Enterprise

> **Enterprise RAG + Knowledge Graph + Agentic Tool Use, self-hostable, MIT licensed.**

AskMyDocs is a self-hostable AI hub for enterprise knowledge. It fuses
hybrid retrieval-augmented generation (pgvector + FTS + reranker), a
typed canonical knowledge graph with human-gated promotion, a streaming
chat surface on the Vercel AI SDK, and a full admin operations cockpit
into a single Laravel platform. It is the open-source, on-prem alternative
to Glean / Notion AI / ChatGPT Enterprise — without the per-seat lock-in.

<p align="center">
  <img src="resources/cover-AskMyDocs.png" alt="AskMyDocs" width="100%" />
</p>


<p align="center">
  <a href="#quick-start-5-minutes"><img src="https://img.shields.io/badge/Laravel-FF2D20?style=flat-square&logo=laravel&logoColor=white" alt="Laravel"></a>
  <a href="#features-by-area"><img src="https://img.shields.io/badge/Claude-Compatible-cc785c?style=flat-square&logo=anthropic&logoColor=white" alt="Claude"></a>
  <a href="#features-by-area"><img src="https://img.shields.io/badge/OpenAI-Compatible-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI"></a>
  <a href="#features-by-area"><img src="https://img.shields.io/badge/Gemini-Compatible-4285F4?style=flat-square&logo=google&logoColor=white" alt="Gemini"></a>
  <a href="#features-by-area"><img src="https://img.shields.io/badge/OpenRouter-Multi--Model-6366f1?style=flat-square" alt="OpenRouter"></a>
  <a href="#features-by-area"><img src="https://img.shields.io/badge/Regolo.ai-EU-10b981?style=flat-square" alt="Regolo.ai"></a>
  <a href="#features-by-area"><img src="https://img.shields.io/badge/MCP-Server-0ea5e9?style=flat-square" alt="MCP Server"></a>
  <a href="#features-by-area"><img src="https://img.shields.io/badge/Canonical--KB-typed-ff7a00?style=flat-square" alt="Canonical KB"></a>
  <a href="#features-by-area"><img src="https://img.shields.io/badge/Knowledge%20Graph-typed-7c3aed?style=flat-square" alt="Knowledge Graph"></a>
  <a href="#features-by-area"><img src="https://img.shields.io/badge/Anti--Repetition-%E2%9A%A0%EF%B8%8F%20built--in-dc2626?style=flat-square" alt="Anti-Repetition Memory"></a>
  <a href="#prerequisites"><img src="https://img.shields.io/badge/PostgreSQL-pgvector-336791?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL + pgvector"></a>
  <a href="#license"><img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License"></a>
  <a href="#universal-connectors"><img src="https://img.shields.io/badge/connectors-native-0ea5e9?style=flat-square" alt="Native Connectors"></a>
  <a href="#quality--observability"><img src="https://img.shields.io/badge/tests-PHPUnit%20%2B%20Vitest%20%2B%20Playwright-brightgreen?style=flat-square" alt="PHPUnit + Vitest + Playwright"></a>
</p>

<p align="center">
  <strong>Ask your docs. Get grounded answers. See the sources. Run agentic tools.</strong>
</p>


# CHATBOT UI/UX
![AskMyDoc - ChatBot.png](resources/screenshots/AskMyDoc%20-%20ChatBot.png)

# DASHBOARD UI/UX
![AskMyDoc - Dashboard.png](resources/screenshots/AskMyDoc%20-%20Dashboard.png)

---

## Table of Contents

- [What it is](#what-it-is)
- [Why AskMyDocs — the 7 moats](#why-askmydocs--the-7-moats)
- [✨ Universal Connectors](#universal-connectors)
- [✨ Modern Chat Surface (Vercel AI SDK UI)](#modern-chat-surface-vercel-ai-sdk-ui)
- [✨ KITT — Knowledge Interface Tour Toolkit](#kitt--knowledge-interface-tour-toolkit)
- [✨ Institutional Memory — anti-repetition retrieval over a living knowledge graph](#-institutional-memory--anti-repetition-retrieval-over-a-living-knowledge-graph)
- [✨ Auto-Wiki — self-compiling agentic knowledge tier](#-auto-wiki--self-compiling-agentic-knowledge-tier-v811)
- [Features by area](#features-by-area)
  - [Retrieval & Knowledge](#retrieval--knowledge)
  - [Chat & Conversation](#chat--conversation)
  - [Security & Compliance](#security--compliance)
  - [Admin & Operations](#admin--operations)
  - [Integrations & Extensibility](#integrations--extensibility)
  - [Quality & Observability](#quality--observability)
- [Quick start (5 minutes)](#quick-start-5-minutes)
- [Architecture](#architecture)
- [Roadmap](#roadmap)
- [Documentation](#documentation)
- [Screenshots gallery](#screenshots-gallery)
- [Sister packages](#sister-packages)
- [Contributing](#contributing)
- [License](#license)
- [Changelog](#changelog)

---

## What it is

**What.** AskMyDocs is an **AI hub for enterprise knowledge** built on
Laravel 13 + PostgreSQL + pgvector. It ingests markdown, text, PDF and
DOCX documents — and, since v8.36, **scans and images via OCR**
(pluggable docling / Mistral OCR / vision-LLM / tesseract drivers) — into
a typed canonical knowledge graph, answers
questions over them with streaming RAG, exposes the same knowledge as
MCP tools for any agentic client (Claude Desktop, Claude Code,
Cursor, custom agents), and ships a full React admin SPA — KPI
dashboard, canonical KB explorer with inline editor and graph viewer,
log viewer (five tabs), whitelisted Artisan maintenance runner, daily
AI-insights panel, and a self-compiling **Auto-Wiki** admin (health /
indices / explorer with promote-auto→human / per-project settings,
v8.12) — all behind Spatie role-based access control with audit trails
on every destructive mutation.

**Why.** Most "RAG over docs" tools treat your KB as a pile of
interchangeable chunks. They re-discover the answer from zero on every
query, never persist what your team has *already decided*, and
re-propose options that were explicitly dismissed three quarters ago.
SaaS competitors (Glean, ChatGPT Enterprise, Notion AI) either lock
you into per-seat contracts and proprietary data residency, or charge
~$500K/year for the on-prem option. AskMyDocs is MIT-licensed,
self-hostable, EU-sovereign-feasible, and ships a typed canonical layer
with human-gated promotion that no public competitor offers.

**For whom.** Enterprise teams ingesting their architectural decisions
/ runbooks / standards / incidents / domain concepts into a *navigable*
KB; operators of regulated-industry RAG (GDPR, AI Act) needing
field-level PII redaction at every persistence boundary; engineering
orgs that want LLMs to stop re-proposing rejected approaches; Italian
software companies filing under `documentazione_idonea` Patent Box;
and anyone allergic to vendor lock-in.

---

## 📖 Official Documentation

The full documentation — quickstart, guides, integrations, architecture deep-dives,
and API/CLI reference — lives at:

### **→ [doc.askmydocs.padosoft.com](https://doc.askmydocs.padosoft.com/)**

This README is the above-the-fold pitch; the documentation site is the
authoritative, argued, diagrammed reference.

---

## Why AskMyDocs — the 7 moats

These differentiators come from the public competitor audit at
[`docs/v4-platform/AUDIT-2026-05-11-competitor-comparison.md`](docs/v4-platform/AUDIT-2026-05-11-competitor-comparison.md)
(Section 3, "Where AskMyDocs is genuinely AHEAD"), the v8.11 Auto-Wiki
cycle, and the [Annota AI gap audit](docs/v4-platform/AUDIT-2026-09-11-annota-ai-gap.md)
that drove the v8.36 → v8.39 Document Intelligence cycle. They are the moats
no other public RAG platform — open-source or SaaS — currently ships.

| ★ | Moat | One-line |
|:---:|---|---|
| ★ | **Human-gated canonical promotion pipeline** (ADR 0003) | Three-stage API (`/suggest` → `/candidates` → `/promote`) holds the LLM at "draft"; only humans (git push → GH Action) and operators (`kb:promote` CLI) commit canonical storage. Immutable `kb_canonical_audit` trail. No public competitor splits "AI proposes" from "human writes" this way. |
| ★ | **Retrieval-time knowledge graph + rejected-approach injection** | `GraphExpander` walks `kb_edges` 1-hop at every query and folds neighbours into the `SearchResult`. `RejectedApproachInjector` vector-correlates the query against `rejected-approach` canonical docs and surfaces them under a ⚠ marker so the LLM stops re-proposing dismissed options. ChatGPT Enterprise / Glean / Vectara do not do this. |
| ★ | **PII redaction at 11 persistence boundaries** (default-OFF, granular per touch-point) | `padosoft/laravel-pii-redactor` v1.2 wired at 11 touch-points across observers, middleware, Monolog processor, failed-job listener, Flow payload redactor, insights inspector. EU-GDPR-grade *field-level* redaction inside the app boundary — not just data-residency. Every knob default-OFF so v3 / v4.0 hosts see byte-identical behaviour until they opt in. |
| ★ | **MIT-licensed, self-hostable, on-prem feasible** (no $500K/yr vendor contract) | Vectara is the only competitor that ships on-prem ($500K/yr public list). Glean / Notion AI / ChatGPT Enterprise / M365 Copilot are SaaS-only. AskMyDocs runs on any Laravel + PostgreSQL + pgvector host with zero vendor lock-in; the entire sister-package stack is MIT and independently reusable. |
| ★ | **Eval-harness CI gate + nightly LLM-as-judge + adversarial cohorts + retrieval-metric source-of-truth** | `padosoft/eval-harness` v1.3 RAG regression gate on every PR (4 datasets / 1 baseline + 3 adversarial / 7 metrics including custom `CitationGroundednessMetric` + `CosineGroundednessMetric`); `eval:nightly` Artisan cron at 05:30 UTC with three-fence cost guard, regression detection vs prior baseline, `Log::alert` + sidecar on regression; adversarial-lane nightly opt-in shipped in v4.4. **Since v8.18 it is also a runtime `require` dependency**: the retrieval-metric math (MRR, nDCG@k) is delegated to it through a single anti-corruption adapter (`PackageMetricAdapter`), so the package — not bespoke host code — is the source of truth for ranking metrics. Out-of-the-box eval surface nobody else publicly ships. |
| ★ | **Self-compiling Auto-Wiki tier behind an anti-hallucination firewall** (v8.11) | A second-class **`auto` tier** the system *builds itself* — on ingest the LLM enriches frontmatter (tags / summary / cross-refs / evidence-tier), materialises a navigable graph, synthesizes new `domain-concept` pages, indexes + lints them, agentically navigates (multi-hop BFS), and cross-model-reviews its own output — yet the **reranker firewall always ranks human-`accepted` > auto > raw**, so machine knowledge never silently becomes authoritative. Every layer is reversible, audited, tenant-scoped, default-ON-but-degradable, and exposed PHP + HTTP API + MCP. No public RAG platform ships a self-maintaining knowledge tier *behind* a human-vouched firewall. |
| ★ | **Document Intelligence closing the Annota AI gap end to end** (v8.36 → v8.39) | *File → reviewed Markdown → portable, agent-consumable wiki* — the exact seam a 2026 competitor audit found us missing, closed without cutting the corner they did. OCR of scans/images with pluggable drivers (docling / Mistral OCR / vision-LLM / tesseract); the converted Markdown genuinely **stored** as a versioned conversion artifact, not a lossy chunk reconstruction; a Digitization Review loop where an agent **proposes** a text correction and a human approves it — never an ungated `update_document_page`-style rewrite; an already-compiled, hash-manifested portable wiki export with a live `.mcp.json` back-link; and the maintenance cron itself upgradeable to a named, observable, tenant-scoped delegated routine. See the [full comparison](#how-it-compares--the-annota-ai-gap-closed-v836--v839) below. |

### Plus: a closed-loop **KB Lifecycle Intelligence** suite (v8.7 → v8.39)

Beyond the moats, the v8.7–v8.11 cycles shipped a closed governance loop most
RAG tools simply don't have — the exact capabilities the
[2026 Affine KB Buyer's Guide](docs/v4-platform/AUDIT-2026-06-02-affine-buyers-guide-gap.md)
tells buyers to demand:

- **Content-gap analytics** — every question the KB *couldn't* answer (sync **and** streaming
  refusals) is ranked under **Admin → Content Gaps** so editors write the missing article next.
  The guide names this in three separate sections; few competitors expose it at all.
- **Obsolescence intelligence on every change *and delete*** — the AI deep-analysis flags which
  *other* docs a change (or deletion) makes stale or dangling, suggest-only, human-gated.
- **Synonym expansion + per-query multilingual FTS** — the guide literally lists "Synonym
  Expansion: does the AI connect industry terms?" (shipped v8.7) and multilingual consistency
  (shipped v8.8).
- **Review cadence + archival, not deletion** — automated stale-review reminders + the Cloud
  Time Machine (browse / diff / restore any version) — the guide's "Review Cadence and Archival
  Policy" governance section, shipped.
- **Graph-native navigation** — a chat-side **Related** panel walks the knowledge graph straight
  from a grounded answer.
- **Self-compiling Auto-Wiki** (v8.11) — ingest auto-enriches frontmatter + materialises graph
  edges, synthesizes recurring-concept pages, maintains per-tenant index hubs, lints wiki health,
  agentically navigates multi-hop, cross-model-reviews auto pages, applies change/delete
  suggestions, and self-maintains on a daily schedule — all behind the human > auto > raw
  firewall. See the dedicated section below.
- **Engagement & Intelligence Suite** (v8.15) — a proactive, multi-channel **digest** (newly
  created / promoted docs · stale review queue · top unanswered questions · KB-health trend ·
  "your attention needed"; modified-doc activity shows in the headline metrics) delivered to
  **email + Discord + Slack + Teams + an in-app feed** with
  an opt-in AI narrative on a dedicated free model; an admin engagement dashboard (contributor
  leaderboard / coverage / answer-rate / decision-debt trend) and a personal **My KB** dashboard
  (your score / rank / impact / review queue); **gamification** (config-driven badges
  over real contribution metrics, **default-ON since v8.18**); and (v8.18) an **AI coaching
  layer** — curation-quality metrics turned into LLM coaching cards + project/tenant health
  narratives (`GET /api/me/coaching`, admin insights panel, `KbGamificationInsightsTool`),
  degrading to deterministic copy when the model is off. Built to surpass Stack Overflow for
  Teams / Zendesk / Notion on packaging + delivery breadth; every capability tri-surface
  (PHP + API + MCP). See the [doc-site](https://padosoft.mintlify.app/engagement-suite).
- **AI FinOps spend governance** (v8.16) — a cross-provider AI-spend layer: an immutable per-call
  usage **ledger**, N-scope **budgets**, a policy DSL, chargeback, forecasting + anomaly detection
  and multi-channel alerts, attributed per tenant, behind a method-aware admin gate. Every provider
  moved onto the `laravel/ai` SDK (ADR 0015) so spend is metered natively; **real server-side
  per-turn cost** now lands on every chat log (replacing the old client-side guess), and 3 MCP read
  tools expose spend to agents. See the [doc-site](https://padosoft.mintlify.app/ai-finops).
- **Credential-based connectors** (v8.17) — the connector framework gains its first **non-OAuth**
  source: an **IMAP** mailbox (host/port/encryption/username/password, **delegated XOAUTH2**, or
  **Microsoft 365 app-only** OAuth2 client-credentials via `IMAP.AccessAsApp` — unattended, no user
  sign-in, `connector-imap` **^1.5**) activatable entirely from **Admin → Connectors**.
  The mechanism is **generic + schema-driven** (a connector
  advertises `SupportsCredentialForm`; the host renders the form and routes the **secret straight to
  the encrypted vault, never `config_json`**) — any future credential connector works unchanged. See
  the [doc-site](https://padosoft.mintlify.app/connectors-credential).
  **IMAP connections are serialized per mailbox** (host+port+username, **cross-tenant**) so a server
  never returns *"Too many simultaneous connections"*: at most one live connection per account at a
  time across every surface, and concurrent same-mailbox sync jobs **re-queue** instead of piling up.
  Tunable via `CONNECTOR_IMAP_SERIALIZE_CONNECTIONS` (default on; needs an atomic lock store / Redis)
  + `CONNECTOR_IMAP_MAILBOX_LOCK_*`. See the
  [doc-site](https://padosoft.mintlify.app/connectors-imap-serialization).
  A **transient transport drop** on a live session (the classic *"fwrite(): SSL: Broken pipe"* /
  connection-reset / idle drop Gmail & Exchange trigger mid-sync) is **absorbed by one
  close-and-retry on a fresh connection** — nested **inside** the per-mailbox lock, so the retry
  never opens a second connection — instead of hard-failing the run and leaving the install stuck at
  *"Not synced yet"*. Auth failures are never retried. Tunable via `CONNECTOR_IMAP_RECONNECT_ON_DROP`
  (default on), `CONNECTOR_IMAP_RECONNECT_MAX_ATTEMPTS`, `CONNECTOR_IMAP_RECONNECT_RETRY_DELAY_MS`.
- **API connector — endpoints as live LLM tools** (v8.27, `padosoft/askmydocs-connector-api`) — a
  NEW paradigm: instead of ingesting, each configured HTTP **endpoint (Rotta)** becomes a **tool the
  LLM can call live during chat**, so the model can pull **fresh** data (orders, stock, tracking…)
  straight from the customer's APIs on top of the indexed knowledge. A "Test connessione" call
  auto-infers the input/output schema and generates the tool definition; execution is **server-side
  only** — the model supplies just the `llm` parameter values and never sees URLs/headers/secrets.
   SSRF-guarded (`UrlGuard`), encrypted credentials, per-route timeout/retry/rate-limit/cache + output
   cap; auth none/API-key/Bearer/Basic/custom/OAuth2-cc; works across OpenAI, OpenRouter, Anthropic and
   Gemini. Configure under **Admin → API Connectors**. The durable multi-call retrieval loop, SSE protocol, safety budgets and mock-server test procedure are documented in the [agentic API retrieval runbook](docs/runbooks/agentic-api-retrieval.md). **Full-history imports are durable and bounded**: selected folders are divided into date windows, each UID batch checkpoints in SQL, and `kb-ingest` workers index independently. Configure the master switch, queue, batch/job caps, fetch size, stale-worker recovery and oldest accepted date with `CONNECTOR_IMAP_BACKFILL_ENABLED`, `CONNECTOR_IMAP_BACKFILL_QUEUE`, `CONNECTOR_IMAP_BACKFILL_BATCH_SIZE`, `CONNECTOR_IMAP_BACKFILL_MAX_MESSAGES_PER_JOB`, `CONNECTOR_IMAP_BACKFILL_FETCH_SIZE`, `CONNECTOR_IMAP_BACKFILL_STALE_MINUTES` and `CONNECTOR_IMAP_BACKFILL_ABSOLUTE_START`.  The operation is available through Admin HTTP/UI and the write-capable `KbImapBackfillTool` MCP tool.
- **AI Guardrails on the live chat path** (v8.19) — every chat turn is **screened on input** (a
  malicious / policy-violating prompt becomes a localized refusal — never a 500 — with an append-only
  audit row) and **sanitized on output** (exfil links defanged before the answer reaches the client),
  via `padosoft/laravel-ai-guardrails` behind a host adapter. Modes `enforce`/`monitor`/`off`; an
  8-screen admin SPA mounts at `/admin/ai-guardrails` (default-OFF). See the
  [doc-site](https://padosoft.mintlify.app/ai-guardrails).
- **Agentic Knowledge Reports** (v8.19) — the Tabular Review engine gains genuinely **agentic
  columns**: `graph` columns resolve a **deterministic, LLM-free** governance metric from the
  canonical graph, `verify` columns run a bounded anti-hallucination second pass that downgrades a
  flag when the value isn't backed by cited evidence. A flagship **"Canonical KB Governance Audit"**
  preset turns the KB into an auditable, per-cell-cited matrix, with a 16-template ready-made library
  and an evidence side-panel. See the [doc-site](https://padosoft.mintlify.app/agentic-knowledge-reports).
- **Invite-by-code & referral suite** (v8.22) — onboarding the way a growth team runs it: campaigns,
  multi-use + vanity codes, **referrals + rewards + waitlist**, fail-open anti-abuse (HMAC'd PII), and
  funnel analytics, powered by the standalone `padosoft/laravel-invitations` engine whose **atomic,
  idempotent, concurrency-safe** redemption (a single conditional `UPDATE … WHERE current_uses <
  max_uses`) makes seat-count safe under load. Each invite carries a per-tenant **grant** — a Spatie
  role *and* KB project memberships — so one code provisions access across one or more tenants at
  once (GRANT-never-REVOKE). Tri-surface (PHP + HTTP + 3 MCP tools), admin gated by
  `can:manageInvitations`, surfaced as a **native in-app admin** (invite-funnel dashboard with 11 live
  KPIs, a campaign builder with the multi-tenant grant editor, code inventory with batch generation /
  CSV export / revoke, a direct-invitation sender, and referral / reward / waitlist / anti-abuse tables)
  inside the unified admin chrome, and a closed-beta `INVITE_REQUIRED` signup gate that is
  **default-OFF**. See the [doc-site](https://padosoft.mintlify.app/invitations).
- **Document Intelligence — file → reviewed Markdown → portable, agent-consumable wiki**
  (v8.36 → v8.39) — closes the exact gap a competitor audit
  ([Annota AI](docs/v4-platform/AUDIT-2026-09-11-annota-ai-gap.md)) found: **OCR of scans and
  images** (`OcrConverter`, pluggable docling / Mistral OCR / vision-LLM / tesseract drivers,
  figures extracted to `images/`, LaTeX formulas, per-page confidence, and a FinOps cost estimate
  on the upload modal — v8.36/W1); the converted Markdown now genuinely **stored** as a real
  conversion artifact on the existing *Cloud Time Machine* — faithful document diff/restore
  instead of a chunk reconstruction, versions born on correction with `actor`/`reason` (v8.36/W2);
  a **Digitization Review** loop — OCR'd content is born in the `auto` tier and promoted to
  `human` on approval, the anti-hallucination reranker firewall's `human > auto` ordering now
  covering non-canonical rows too, an MCP `KbProposeTextCorrectionTool` that **proposes** a
  correction and never commits one (the explicit inverse of a competitor's ungated
  `update_document_page`), and a `ReviewTab` admin UI (v8.37/W3); **Portable Wiki Export** —
  `kb:export-wiki` ships an ACL-filtered, hash-manifested, **already-compiled** `raw/`+`wiki/`
  folder with a `.mcp.json` pointing back at the live server (placeholder credential env-vars
  only, never an embedded token), an idempotent async HTTP surface, and `kb:import-wiki`
  returning edits as human-gated promotion candidates, never a direct write (v8.38/W4); and
  **Auto-Wiki maintenance as a delegated routine** — the existing nightly maintenance cron can
  now optionally run as a named, observable routine via `padosoft/laravel-routines`, tenant-scoped
  entirely by the host since the engine has none of its own concept of a tenant (v8.39/W5). Every
  surface tri-surface (PHP + HTTP + MCP), every flag default-**OFF**, both states tested (R43).
  See [Documents & OCR](https://padosoft.mintlify.app/documents-and-ocr),
  [Digitization Review](https://padosoft.mintlify.app/digitization-review),
  [Portable Wiki Export](https://padosoft.mintlify.app/portable-wiki-export),
  [Auto-Wiki](https://padosoft.mintlify.app/auto-wiki), and the
  [full Annota AI comparison](#how-it-compares--the-annota-ai-gap-closed-v836--v839) below.

---

## ✨ Universal Connectors

**Plug AskMyDocs into Google Drive, Notion, OneDrive, Evernote, Fabric, Confluence, Jira (OAuth in one click) and IMAP mailboxes (credential form) — every document chunked and cited correctly per source.**

Most "RAG over docs" tools either expect a pile of pre-flattened
markdown or ship a single brittle "Google Drive sync" feature. AskMyDocs
ships a real **connector framework** + **eight native connectors**
+ **per-source chunkers** so every external knowledge corpus lands in
the canonical KB with its provenance, native IDs, ACL hints, and
status preserved — and gets chunked the way that source actually wants
to be chunked.

- **8 native connectors** — **OAuth** (v4.5): `google-drive` (OAuth2 + delta-query), `notion` (OAuth2 + block paginator), `evernote` (OAuth + `.enex` bulk import), `fabric` (API-key, OAuth pending upstream), `onedrive` (Microsoft Graph delta-query — supports `text/markdown` / `text/plain` / `application/pdf`; Office formats `.docx` / `.xlsx` / `.pptx` ingestion deferred), `confluence` (Atlassian OAuth 2.0 3LO; `cloud_id` persisted in tenant-scoped `connector_credentials.extra_json.cloud_id`, optionally reused by a Jira install in the same tenant/workspace), `jira` (Atlassian OAuth 2.0 3LO + ADF-to-markdown + injection-safe JQL builder); **credential** (v8.17): `imap` — the first **credential-based** connector (host/port/encryption/username/password **or** XOAUTH2 Gmail/M365), body + headers + attachments.
- **Credential-based connectors (v8.17)** — a **generic, schema-driven** mechanism (no IMAP-specific code in the host): a connector implements `SupportsCredentialForm` and the host renders a credential form, validates it dynamically, and routes the **secret straight to the encrypted vault** (never to `config_json`). `POST /api/admin/connectors/{name}/configure` activates it from the panel — basic-auth pings + vaults (bad login → 422), XOAUTH2 redirects through the standard callback. Any future credential connector (SMTP, API-key sources) reuses the same form + endpoint unchanged. See the [credential-connectors doc](https://padosoft.mintlify.app/connectors-credential).
- **Per-source chunkers** — `NotionBlockChunker` / `ConfluencePageChunker` / `OfficeDocChunker` / `AtomicNoteChunker` / `JiraIssueChunker` / `PdfPageChunker` dispatched via `PipelineRegistry::resolveChunker()` (R23 FQCN-validated + `supports()` mutex-checked at boot).
- **Rich frontmatter capture** — every connector populates document-level metadata (`connector`, `external_id`, `external_url`, native timestamps) plus chunk-level metadata (`source_type`, `search_tags` (top-level in chunk metadata), `recency_bucket`, ACL hint, status, preamble-path). Drives `KbSearchService` facets + `Reranker` Layer-4 signals (tag overlap + recency + status-active + preamble-match).
- **Admin install flow at `/app/admin/connectors`** — React SPA + Spatie super-admin gate; OAuth connectors use a signed OAuth callback, credential connectors a host-rendered schema-driven form; per-installation `connector_installations` + `connector_credentials` rows + scheduler-driven incremental sync via `App\Jobs\ConnectorSyncJob`.
- **Opt-in live-test recording infrastructure** — `tests/Live/Connectors/` skeleton + per-provider env-var guard + `docs/v4-platform/RUNBOOK-live-fixture-recording.md` junior-proof setup guide. CI runs only `Unit` + `Feature`; operators refresh fixtures explicitly when provider APIs drift.

### How it compares

| Capability | AskMyDocs v4.5 | Glean | Notion AI | ChatGPT Enterprise | M365 Copilot | Mendable | Vectara |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Self-hostable + connector framework | ✅ MIT | ❌ SaaS | ❌ SaaS | ❌ SaaS | ❌ SaaS | ❌ SaaS | ❌ $500K/yr |
| Native Google Drive | ✅ | ✅ | ❌ | ✅ | ❌ | partial | ❌ |
| Native Notion | ✅ | ✅ | ✅ | ✅ | ❌ | partial | ❌ |
| Native OneDrive | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ |
| Native Evernote | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Native Confluence | ✅ | ✅ | ❌ | ❌ | partial | partial | ❌ |
| Native Jira | ✅ | ✅ | ❌ | ❌ | ❌ | partial | ❌ |
| Native IMAP / email (credential) | ✅ (v8.17) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Source-aware chunking framework | ✅ | private | ❌ | ❌ | ❌ | partial | partial |
| Plugin/package extensibility | ✅ (v4.6 packages + v8.17 credential form) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Try it.** Read [`docs/connectors/README.md`](docs/connectors/README.md)
for the developer guide (10-method `ConnectorInterface` contract +
auto-discovery + framework reuse pattern), then log in as a
super-admin and navigate to `/app/admin/connectors` to install the first
connector.

---

## ✨ Modern Chat Surface (Vercel AI SDK UI)

**Stop / regenerate / branch / inline-edit / token-cost meter — the chat surface every modern AI app should have, with full streaming citations and suggested follow-ups.**

The chat UX gap against Claude Desktop / ChatGPT Plus / Vercel
reference apps is what 90% of first-time users notice and 0% of
self-hostable RAG OSS ships. v4.5 closes that gap on all seven Tier 1
affordances plus the first Tier 2 win (suggested follow-ups), built on
top of the v4.0 Vercel AI SDK v6 `UIMessageChunk` streaming foundation.

- **7 Tier 1 features** — stop-streaming button (`AbortController`-backed), regenerate-last-assistant, branch-from-message endpoint (forks the conversation tree), inline-edit user message, token+cost meter (BE `config('ai.cost_rates')`), enhanced per-message provider+model+timestamp badge, copy-code-block.
- **Suggested follow-up pills** — `SuggestedFollowupGenerator` derives three follow-up prompts from the assistant's last reply; renders as clickable pill chips under the message; submits via the streaming endpoint when clicked.
- **Full Vercel AI SDK v6 message-parts integration** — `MessageStreamController` emits canonical `start` / `text-start` / `text-delta` / `text-end` / `source-url` / `data` / `finish` frames over SSE; `useChatStream()` exposes `data-state="idle|loading|ready|empty|error"` for deterministic Playwright waits (SDK `submitted` and `streaming` statuses both map to `loading` via `mapStatusToDataState()` — see `frontend/src/features/chat/map-status-to-data-state.test.ts`).
- **Canvas-ready architecture (artifact panel deferred to v5.x)** — Tier 2 stretch (tool-result rendering, streaming source-document parts, conversation export, image attachments, artifact panel) is deliberately deferred to a v5.x milestone so it can be designed alongside the MCP **client** tool-result surface and share one storage contract. See ADR 0008 D4.
- **Zero-config for OpenAI / Anthropic / Gemini / OpenRouter / Regolo** — every provider runs on the `laravel/ai` SDK (since v8.16, ADR 0015), so AI FinOps meters them natively. Anthropic + Gemini are fully SDK; OpenAI + OpenRouter are hybrid (SDK for no-tools chat + embeddings, raw `Http::` `/chat/completions` for the MCP tool-calling turn the SDK can't host); Regolo via the `padosoft/laravel-ai-regolo` SDK adapter. `AiManager::chatStream()` synthesises a single-chunk SSE for providers without native streaming via the `FallbackStreaming` trait.

**Try it.** Open `/app/chat` in the React SPA. Start a long answer
and hit Stop; click Regenerate; hover the assistant message and pick
Branch (a new conversation forks from that point); pick a follow-up
pill chip to chain into the next prompt; hover any code block for the
Copy button.

---

## ✨ KITT — Knowledge Interface Tour Toolkit

**KITT (Knowledge Interface Tour Toolkit) is a one-`<script>` embeddable, page-aware, agentic AI assistant for any website — it answers grounded questions with citations, *reads the page*, and (when allowed) drives it: clicks, types, navigates, submits, and calls your backend tools.**

![AskMyDoc - KITT.jpeg](resources/screenshots/AskMyDoc%20-%20KITT.jpeg)

Most "chat widget" products are a stateless text box bolted to a generic
LLM. **KITT** is the embeddable surface of the *same* AskMyDocs retrieval
stack — grounded, cited, tenant-isolated — **plus** a bounded ReAct loop
that perceives and acts on the host page. A customer pastes a snippet; the
widget captures a structured snapshot of the current page (regions, fields,
actions, messages, outline) and reasons about what's actually on screen.

- **Embed in one snippet** — `<script>window.AskMyDocsWidget = { key: 'pk_…', apiBase: '…' }</script>` + the async loader. Three layouts: a floating `helper` launcher, an `inline` mounted block, or an always-open `fullscreen` viewport. Theme, title, skill and a structured pre-conversation welcome card (`intro`: image/icon, title, text, benefits and suggested questions) are configurable per key or per page.
- **Grounded + cited, never a generic bot** — the widget runs the first-party `KbSearchService` + reranker + refusal gate, scoped to the key's tenant + project. The browser **never** names a tenant — tenant/project are resolved server-side from the key (R30); cross-key/cross-tenant session access is `404` (anti-IDOR).
- **Agentic by design** — the LLM emits tool calls executed in the page DOM (`click` / `type` / `select` / `navigate_to` / `submit_form` / `wait_for` + ~15 more), or server-side via `/exec-tool` (`search_knowledge_base`), in a bounded loop with per-session step + consecutive-error caps. **Skills** (JSON manifests under `resources/widget/skills/*`) declare which tools, what auto-annotation rules, and the run policies.
- **Host-Tools Protocol (HTP)** — your app can expose its *own* tools to the agent ("create order", "set rate"), **double-gated** (per key *and* per skill) and **off by default**. The page is annotated with stable, verb-based `data-kitt-*` attributes (`region` / `field` / `action` / `message` / `locale` / `skip`); `data-kitt-sensitive` and `type=password`/`hidden` values are force-nulled server-side so secrets never reach the LLM or the step log.
- **Secure embedding** — exact-match `Origin` allowlist (browser mode) or `sk_` secret (server-to-server); **single-use, origin-bound session tokens** consumed atomically under a lock (R21, hashed at rest, rate-limit checked *before* burn); snapshot byte + count caps; `javascript:`/`data:`/protocol-relative navigation blocked on both server and client; PII masked on every persisted step (Italian VAT masking is checksum-validated so non-PII codes stay readable).
- **Full admin surface** — `/app/admin/widget` (super-admin): create / rotate / revoke keys, manage allowed origins + theme + welcome content, toggle host-tools, copy the ready-made embed snippet, and replay every session step (PII-masked).

**Try it.** As super-admin, open `/app/admin/widget`, create a key (set a
`project_key` + your site's origin), copy the **Embed code** snippet into
your page, and reload. Locally, set `WIDGET_DEMO_ENABLED=true` and open
`/widget-demo` for a self-contained annotated demo page (add `?mode=inline`
or `?mode=fullscreen`; add `&user_auth=1` to exercise authenticated history).
Full developer guide:
[`docs/kitt/INTEGRATION.md`](docs/kitt/INTEGRATION.md).

> **Security & embedding.** KITT is a cross-origin embeddable *and* an
> agentic (page-driving) surface, so before embedding it on anything beyond a
> public, low-sensitivity page, read the
> [**Security & threat model**](docs/kitt/INTEGRATION.md#14-security--threat-model)
> section of the integration guide — it documents exactly what is enforced and
> *why* (tenant isolation, exact-match origin allowlist, no-credential CORS, no
> host-page XSS, credential-field and navigation guards), the residual/inherent
> risks of a public embeddable agent (public-key abuse, prompt-injection-driven
> actions, data egress to the LLM), and the **best practices the operator and
> the host site must follow to mitigate them** — including `data-kitt-skip` to
> keep sensitive page regions out of the snapshot.

## ✨ Desktop & mobile client + token authentication

**A native Tauri v2 + React desktop/iOS client — and the stateless Bearer-token auth flow that powers any non-browser client without a cookie/CSRF dance.**

The React SPA authenticates with Sanctum's *stateful* cookie flow (CSRF
round-trip), which is exactly wrong for a native app, a CLI, or a CI runner. So
AskMyDocs ships a **second transport** behind the same `auth:sanctum` guard —
least-privilege, finite-expiry Bearer tokens — plus a reference desktop client
that proves it end to end.

- **`POST /api/auth/token`** — verifies credentials with **no session, no CSRF**
  and returns a Sanctum personal access token (`201 { token, token_type:
  "Bearer", user }`). The token is scoped to exactly `kb:read` + `kb:chat`
  (never the `['*']` wildcard) and **self-expires after 30 days**, so a token
  leaked from a lost device revokes itself server-side. `POST
  /api/auth/token/revoke` is the stateless sign-out (`204`).
- **`EnforceTokenAbility` (`token.ability:<ability>`)** — a per-route gate that
  constrains **only** Bearer PATs (`403` `token_ability_forbidden` if a token is
  scoped wrong) and is a **no-op for the cookie SPA**, so dual-auth routes
  (`/api/kb/chat`, `/api/kb/documents/search`, `/api/kb/documents/{documentId}/preview`)
  serve both transports without breaking either.
- **Tauri v2 desktop client** (`desktop/`) — login, grounded chat with clickable
  markdown citations, document search, and a full-page source-document viewer.
  Conversation threads persist **locally**; all backend calls go through the
  Tauri HTTP plugin so the backend needs **no CORS change**.
- **iOS from the same codebase** — Tauri v2 mobile, responsive UI with
  safe-area insets and an off-canvas thread drawer, no native code changes.

**Try it.** `cd desktop && npm install && npm run tauri dev`. Full runbook —
including the iOS build flow — in [`desktop/README.md`](desktop/README.md); the
auth flow is documented in the
[doc site](https://padosoft.mintlify.app/desktop-client).

## ✨ Institutional Memory — anti-repetition retrieval over a living knowledge graph

**Your KB doesn't just store documents — it remembers what your team decided,
refuses to let the LLM re-propose approaches you already rejected, and keeps that
memory current by itself.**

Commodity RAG treats your corpus as interchangeable chunks: it re-discovers the
answer from zero on every query, never persists what was *already decided*, and
happily re-suggests an option your team dismissed three quarters ago. AskMyDocs
ships a **typed canonical layer** (decisions / runbooks / standards / incidents /
integrations / domain-concepts / **rejected-approaches**) over a lightweight
**knowledge graph** — and wires both straight into retrieval, so the memory is
not a passive archive but an active participant in every answer.

**How your searches benefit — on every query, automatically:**

- **Graph-expanded recall** — `GraphExpander` walks `kb_edges` one hop out from
  each canonical seed hit and folds the connected decisions / runbooks / concepts
  into the result set, so the answer carries the surrounding context a bare vector
  match would miss (config-gated; a clean no-op for tenants with no canonical docs).
- **Anti-repetition firewall** — `RejectedApproachInjector` vector-correlates the
  query against your `rejected-approach` docs and surfaces the dismissed options
  under a ⚠ marker in the prompt, so the model stops re-proposing exactly what your
  team already ruled out. This is the single most-requested behaviour commodity RAG
  cannot give you, because it has nowhere to *store* a rejection.
- **Evidence-aware weighting** — every retrieved chunk carries its evidence tier
  (`guideline > peer_reviewed > official > … > unverified`); the prompt flags
  low-confidence claims so an answer never leans on a blog post as if it were a
  ratified standard.
- **Trust-ranked fusion** — the reranker fuses vector + keyword + heading signals
  and **always ranks human-`accepted` > `auto` > raw**, so machine-written
  knowledge can enrich an answer but never silently outranks a human-vouched
  decision.

**How the memory self-updates and maintains itself** — the part that keeps it
from rotting (the self-compiling engine detailed in the
[Auto-Wiki](#-auto-wiki--self-compiling-agentic-knowledge-tier-v811) section below):

- **On ingest**, an LLM compiler enriches each document's frontmatter (tags /
  summary / cross-references) and materialises those cross-references into real
  graph edges + nodes — so a freshly-landed doc becomes *navigable* immediately,
  with zero manual linking.
- **Recurring concepts** that appear across many documents are synthesized into
  brand-new `domain-concept` pages, grounded *only* in the docs that mention them —
  the KB grows its own connective tissue instead of waiting for someone to write it.
- **A daily maintenance sweep** rebuilds the per-tenant index hubs, lints the graph
  (dangling / orphan / stale cross-references, with safe auto-fix), and backfills
  enrichment — so "knowledge improves over time" rather than decaying.
- **An independent, cross-model review-LLM** audits every auto-generated page for
  grounding, novelty and contradictions before it is trusted — and the entire
  self-maintaining tier sits *behind* the human > auto > raw firewall, fully
  reversible and audited.

Every layer is tenant-scoped (R30), written to the immutable `kb_canonical_audit`
trail, and config-gated (default-degradable, R43) — and, per R44, exposed across
PHP + HTTP API + MCP. **No public RAG platform — open-source or SaaS — ships
institutional memory that both *feeds retrieval* and *maintains itself* behind a
human-vouched firewall.**

**Try it.** Promote a `decision` doc and a `rejected-approach` doc (git push → GH
Action, or the `kb:promote` CLI), then ask the chat a question near the rejected
option: the ⚠ rejected-approaches block appears inside the grounded answer, and the
chat-side **Related** panel walks the graph straight from the decision you just
promoted.

---

## ✨ Auto-Wiki — self-compiling agentic knowledge tier (v8.11)

Inspired by Andrej Karpathy's *LLM-Wiki* pattern (raw → wiki → schema layers;
ingest / query / lint ops) and **AutoSci** (concept pages + graph edges, entity
index, BFS exploration, cross-model review), AskMyDocs **compiles its own wiki**
on top of every ingested corpus — and keeps it healthy over time — without ever
weakening the human-vouched authoritative tier.

The cornerstone is a **second-class `auto` tier** (`knowledge_documents.generation_source ∈ {human, auto}`):
AI-compiled knowledge is real, searchable and navigable, but an
**anti-hallucination reranker firewall always ranks human-`accepted` > `auto` > raw**,
and an admin can promote `auto` → human. Every layer is reversible, audited to
`kb_canonical_audit`, tenant-scoped (R30), and config-gated (default-ON but
cleanly degradable to today's behaviour, R43).

Shipped incrementally across **v8.11.0 → v8.11.10** (each its own tagged release):

| Phase | Capability |
|---|---|
| **Foundations** (v8.11.0) | The `auto` tier discriminator + reranker firewall + layered `AutoWikiGate` + dedicated AI-model override + source-retention config + ADR 0014. |
| **Compiler** (v8.11.1) | After ingest, the LLM auto-enriches frontmatter — tags / summary / aliases / cross-references (allow-listed to real neighbours, anti-hallucination) → `frontmatter_json._autowiki`. |
| **Evidence-tier** (v8.11.2) | An evidence-strength axis (`guideline > peer_reviewed > official > … > unverified`) derived in the same call + surfaced in the RAG prompt to flag low-confidence claims ([AutoSci #67](https://github.com/skyllwt/AutoSci/issues/67)). |
| **Graph canonicalization** (v8.11.3) | Cross-references become real `kb_edges` + `kb_nodes` — the auto tier becomes *navigable*; every auto doc gets a stable `auto-`-namespaced slug. |
| **Concept synthesis** (v8.11.4) | Recurring concepts across a project become **new `domain-concept` pages**, grounded in the docs that mention them (AutoSci `/prefill` dedup). |
| **Indices + log** (v8.11.5) | Per-project roll-ups + a **per-tenant index hub** (the agentic map) + the auto-wiki operation log. |
| **Lint / health** (v8.11.6) | Deterministic checks — dangling / orphan / stale-cross-ref / missing-index — with safe auto-fix. |
| **Agentic navigation** (v8.11.7) | Multi-hop, cycle-safe **BFS** over the graph, anchor-driven from the index — the "navigate the wiki" primitive beyond 1-hop expansion. |
| **Cross-model review** (v8.11.8) | An *independent* review-LLM audits each auto page for grounding / novelty / **contradictions** before it's trusted. |
| **Apply engine** (v8.11.9) | Change/delete suggestions become concrete, audited, reversible mutations (add cross-ref / deprecate impacted) — manual + opt-in auto-apply (default-OFF). |
| **Scheduled maintenance** (v8.11.10) | A daily sweep that rebuilds indices, lints, and backfills enrichment so "knowledge improves over time". |

**Tri-surface everywhere (R44):** every capability is exposed and consumable via
**PHP** (Artisan commands: `kb:evidence-tier`, `kb:wiki-link`,
`kb:synthesize-concepts`, `kb:wiki-index`, `kb:wiki-lint`, `kb:wiki-navigate`,
`kb:wiki-review`, `kb:apply-suggestion`, `kb:wiki-maintain`, `kb:wiki-promote`),
**HTTP API** (RBAC-gated admin endpoints under `/api/admin/kb/*`), and **MCP**
(the `enterprise-kb` server grew from 14 → **34 tools**, incl.
`KbWikiNavigateTool` as the primary agentic surface, `KbWikiPromoteTool` for
promote/discard, the v8.15 engagement trio `KbEngagementSummaryTool` /
`KbDigestPreviewTool` / `KbUserBadgesTool`, the v8.16 AI FinOps read trio
`FinOpsSpendSummaryTool` / `FinOpsTopModelsTool` / `FinOpsBudgetStatusTool`,
the v8.18 AI gamification read tool `KbGamificationInsightsTool`, the v8.19
AI Guardrails posture tool `KbGuardrailsInsightsTool` and the v8.19 Agentic
Knowledge Reports reader `KbRunReportTool`) — all thin layers over one shared
core service per capability.

**Admin Wiki UI (v8.12.0):** a full web surface on the whole engine — **Wiki
Health** (lint + safe auto-fix), **Wiki Indices** (hub + per-project roll-ups +
operation log + rebuild), **Wiki Explorer** (browse by tier, promote auto→human,
discard), **Doc Insights → Apply** (turn change/delete suggestions into audited
reversible mutations), **Auto-Wiki Settings** (per-project auto-build gate), and
**tier-badged chat citations** (auto vs human-vouched) — every screen real-data
Playwright-covered (R13).

### Database
```env
DB_CONNECTION=pgsql
DB_HOST=127.0.0.1
DB_PORT=5432
DB_DATABASE=askmydocs
DB_USERNAME=postgres
DB_PASSWORD=secret
```

### AI Provider

The system supports **five providers**, all on the `laravel/ai` SDK since v8.16 (ADR 0015) so AI FinOps meters every provider through the SDK lifecycle events. Anthropic + Gemini are fully on the SDK; OpenAI + OpenRouter are hybrid — the SDK serves no-tools chat + embeddings, while the MCP tool-calling turn stays on raw `Http::` `/chat/completions` because the SDK owns its own tool loop and can't host AskMyDocs's external-MCP loop. Regolo runs through the `padosoft/laravel-ai-regolo` SDK adapter (built on `Laravel\Ai`).

Config file: `config/ai.php`

#### Defaults

```env
# Chat provider. Supported: openai, anthropic, gemini, openrouter, regolo
AI_PROVIDER=openrouter

# Embeddings provider. Must support embeddings (openai, gemini, regolo, openrouter).
# Anthropic does NOT offer embeddings. OpenRouter exposes OpenAI-compatible
# /v1/embeddings (since Oct 2025) routing openai/text-embedding-3-small (default)
# and qwen/qwen3-embedding-4b. Leave empty to let AiManager reuse AI_PROVIDER
# when the default chat provider supports embeddings; otherwise it falls back
# to the first embeddings-capable provider with a configured API key in this order:
# openai → openrouter → regolo → gemini. The 1536-dim defaults (openai +
# openrouter) come first so the stock KB_EMBEDDINGS_DIMENSIONS=1536 pgvector
# schema stays consistent under auto-selection — regolo (4096) and gemini
# (768) require a pgvector resize in lock-step, set AI_EMBEDDINGS_PROVIDER
# explicitly to opt in.
AI_EMBEDDINGS_PROVIDER=openai
```

#### OpenAI

```env
AI_PROVIDER=openai
OPENAI_API_KEY=sk-...
OPENAI_CHAT_MODEL=gpt-4o
OPENAI_EMBEDDINGS_MODEL=text-embedding-3-small
OPENAI_TEMPERATURE=0.2
OPENAI_MAX_TOKENS=4096
OPENAI_TIMEOUT=120
```

#### Anthropic (Claude)

Anthropic has no embeddings endpoint, so pair it with any embeddings-capable provider — OpenAI, OpenRouter, Regolo, or Gemini. If `AI_EMBEDDINGS_PROVIDER` is left empty, `AiManager` auto-selects the first one with a configured API key in this order: openai → openrouter → regolo → gemini. The 1536-dim defaults (OpenAI's `text-embedding-3-small` + OpenRouter routing the same model) come first so a deployment with the stock `KB_EMBEDDINGS_DIMENSIONS=1536` pgvector schema stays consistent under auto-selection; Regolo (4096) and Gemini (768) require a `vector(N)` resize and a matching `KB_EMBEDDINGS_DIMENSIONS` change before use, so set `AI_EMBEDDINGS_PROVIDER=regolo|gemini` explicitly when you've migrated.

```env
AI_PROVIDER=anthropic
AI_EMBEDDINGS_PROVIDER=openai

ANTHROPIC_API_KEY=sk-ant-...
ANTHROPIC_CHAT_MODEL=claude-sonnet-4-20250514
OPENAI_API_KEY=sk-...
```

#### Google Gemini

Gemini supports both chat and embeddings. `text-embedding-004` is **768-dim**, so switching embedding providers requires updating `KB_EMBEDDINGS_DIMENSIONS` **and** re-indexing.

```env
AI_PROVIDER=gemini
GEMINI_API_KEY=AIza...
GEMINI_CHAT_MODEL=gemini-2.0-flash
GEMINI_EMBEDDINGS_MODEL=text-embedding-004
```

#### OpenRouter (multi-model gateway) — default

OpenRouter proxies hundreds of models. Since Oct 2025 it also exposes an
OpenAI-compatible `/v1/embeddings` endpoint, so it can serve both chat
and embeddings from the same gateway. Default embedding model is
`openai/text-embedding-3-small` (1536 dims — matches the default
`KB_EMBEDDINGS_DIMENSIONS`, no re-index needed). Alternative
`qwen/qwen3-embedding-4b` (2560 dims) requires resizing the pgvector
column on `knowledge_chunks.embedding` + `embedding_cache.embedding`
and re-indexing. Pair with a separate provider if you prefer.

```env
AI_PROVIDER=openrouter
AI_EMBEDDINGS_PROVIDER=openrouter

OPENROUTER_API_KEY=sk-or-...
OPENROUTER_CHAT_MODEL=openai/gpt-4o-mini
OPENROUTER_EMBEDDINGS_MODEL=openai/text-embedding-3-small
OPENROUTER_APP_NAME="AskMyDocs"
OPENROUTER_SITE_URL=https://kb.example.com
```

#### Regolo.ai (by Seeweb)

EU-based, GDPR-compliant, **OpenAI-compatible** REST API. Supports chat, streaming, embeddings, and reranking via the [`padosoft/laravel-ai-regolo`](https://github.com/padosoft/laravel-ai-regolo) extension on top of the official `laravel/ai` SDK. Get keys at [dashboard.regolo.ai](https://dashboard.regolo.ai) and see [docs.regolo.ai](https://docs.regolo.ai) for the full model catalogue.

```env
AI_PROVIDER=regolo
AI_EMBEDDINGS_PROVIDER=regolo

REGOLO_API_KEY=...
REGOLO_BASE_URL=https://api.regolo.ai/v1

# Chat models — `cheapest` / `smartest` aliases pick the right model for
# cost-vs-quality shortcuts (see `Lab::Cheapest` / `Lab::Smartest` in laravel/ai).
REGOLO_CHAT_MODEL=Llama-3.3-70B-Instruct
REGOLO_CHAT_MODEL_CHEAPEST=Llama-3.1-8B-Instruct
REGOLO_CHAT_MODEL_SMARTEST=Llama-3.3-70B-Instruct

# Embeddings — set KB_EMBEDDINGS_DIMENSIONS to the same value below.
REGOLO_EMBEDDINGS_MODEL=Qwen3-Embedding-8B
REGOLO_EMBEDDINGS_DIMENSIONS=4096

# Reranker — used when KB_RERANKING_ENABLED=true.
REGOLO_RERANKING_MODEL=jina-reranker-v2

# Transport + per-call defaults. `REGOLO_MAX_TOKENS` / `REGOLO_TEMPERATURE`
# are the provider-level fallbacks; per-call `$options['max_tokens']` /
# `$options['temperature']` (e.g. `ConversationController::generateTitle`
# capping titles at 60 tokens) take precedence.
REGOLO_TIMEOUT=120
REGOLO_MAX_TOKENS=4096
REGOLO_TEMPERATURE=0.2
```

#### Embedding dimension gotcha

If you change the embeddings provider/model (e.g. from OpenAI 1536-dim to Gemini 768-dim):

1. Update `KB_EMBEDDINGS_DIMENSIONS` in `.env`
2. Create a new migration that resizes the `embedding` `vector(N)` column on `knowledge_chunks` and `embedding_cache`
3. Flush the cache so stale-dimension vectors don't pollute retrieval — call `app(\App\Services\Kb\EmbeddingCacheService::class)->flush()` (or scope by retired provider with `->flush('openai')`) from a tinker session. `kb:prune-embedding-cache --days=N` only evicts rows older than N days and returns early when `N <= 0`, so it is **not** a full-flush substitute.
4. Re-index all documents

### AI FinOps — spend governance (v8.16)

Cost governance over AI spend is provided by
[`padosoft/laravel-ai-finops`](https://github.com/padosoft/laravel-ai-finops)
(+ the companion React admin panel
[`padosoft/laravel-ai-finops-admin`](https://github.com/padosoft/laravel-ai-finops-admin)):
a per-call usage ledger, N-scope budgets, a declarative policy DSL, chargeback,
forecasting/anomaly detection, cost-aware routing and multi-channel alerts.

The package meters automatically only for calls that flow through the
`laravel/ai` SDK (here: Regolo). AskMyDocs extends coverage to the
raw-`Http::` providers by hooking `AiManager` — `App\FinOps\AiCallMeter`
records every **synchronous** OpenAI / Anthropic / Gemini / OpenRouter chat
(`chat` / `chatWithHistory`) + embedding into the ledger (non-blocking,
`ChatLogManager`-style; Regolo is skipped to avoid double-counting).
**Streaming chat (`chatStream`, the SSE endpoint) is not yet metered** — a
documented follow-up — so a turn served over streaming is not recorded in the
ledger. Every recorded row is tenant-scoped via `App\Support\TenantContext`
(R30).

The API mounts under `api/admin/ai-finops` behind the admin stack
(`auth:sanctum` + `tenant.authorize` + a **method-aware** gate: reads →
`viewAiFinOps` = super-admin + admin; writes → `manageAiFinOps` =
super-admin). The admin SPA mounts under `/admin/ai-finops` (default OFF).

```bash
# After composer install, create the ai_finops_* tables:
php artisan migrate

# Turn the admin panel on (AI_FINOPS_ADMIN_ENABLED=true) and publish its assets:
php artisan vendor:publish --tag=ai-finops-admin-assets --force
```

```env
AI_FINOPS_ENABLED=true          # master switch (routes + metering hook)
AI_FINOPS_METERING=true         # record usage into the ledger
AI_FINOPS_ENFORCEMENT=false     # hard budget/policy HTTP-402 blocks (opt-in)
AI_FINOPS_CURRENCY=USD          # base = provider list-price currency
AI_FINOPS_DISPLAY_CURRENCY=EUR
AI_FINOPS_RETENTION_DAYS=730
AI_FINOPS_ADMIN_ENABLED=false   # React cockpit at /admin/ai-finops (opt-in)
```

Maintenance crons (Tier-1 slots, staggered in the 04:xx window):
`ai-finops:capture-prices`, `ai-finops:check-alerts`, `ai-finops:prune`.

Since **v8.19** the host runs `padosoft/laravel-ai-finops` **v1.4.0** (`^1.4`),
released onto the `laravel/ai` **0.8** line (the platform-wide migration in v8.19/W1,
[ADR 0016](docs/adr/0016-v819-laravel-ai-0.8-platform-migration.md)); it keeps the
v8.18 fixed-precision **8-dp decimal string** money shape under additive `*_decimal`
keys (no float-rounding drift on small per-token costs). The three FinOps MCP read
tools and `ChatTurnCostResolver` consume the new shape; the existing numeric keys
stay in place (R27 additive).

### Invitations — invite-by-code & referral suite (v8.22)

Onboarding via invite codes + referrals is provided by the standalone
[`padosoft/laravel-invitations`](https://github.com/padosoft/laravel-invitations)
engine, wired tri-surface (R44) into AskMyDocs over its vendor-neutral seams.
The package owns the 9 invite tables (campaigns / codes / invitations /
redemptions / referrals / rewards / waitlist / abuse-signals / analytics) and
the redemption engine; AskMyDocs binds the tenant + provisioning seams:

- the package `TenantResolver` resolves the active **host** tenant
  (`App\Support\TenantContext`), so every invite query/write is tenant-scoped (R30);
- `App\Models\User` implements the package `InvitedAccount` contract;
- `App\Invitations\ProjectMembershipProvisioner` turns an invite's per-tenant
  **grant** into `project_memberships` rows — **GRANT-never-REVOKE** (never
  downgrades an existing membership) and **best-effort** (a fault is logged,
  never thrown). It runs alongside the package's Spatie-role provisioner, so one
  code can grant a role **and** project access across one or more tenants.

Routes auto-mount (no host route file): the admin surface
`/api/admin/invitations/*` (campaigns / code generation / metrics / direct
invitations) behind the SPA-session + `auth:sanctum` + `tenant.authorize` +
`can:manageInvitations` stack (super-admin + admin, R32-matrix-locked); the user
redeem surface `/api/invitations/*` behind the authenticated stack. Three MCP
read/write tools (`Invite{ValidateCode,GenerateCodes,Metrics}Tool`) register on
`KnowledgeBaseServer`.

```bash
# After composer install, create the invite_* tables:
php artisan migrate
```

```env
# Package-level closed-beta gate, read by padosoft/laravel-invitations (NOT by
# the host SPA register endpoint, which is always invite-only — see below).
# Default FALSE (R43 both-states).
INVITE_REQUIRED=false

# Dedicated HMAC secret for signed codes (falls back to APP_KEY-derived
# material when unset). PRODUCTION MUST set its own.
# INVITE_SIGNING_KEY=
# Salt for the HMAC of redemption IP / fingerprint (PII is never plaintext).
# INVITE_PII_SALT=
# INVITE_CODE_LENGTH=8
# INVITE_INVITATION_TTL_DAYS=7
# INVITE_ANTI_ABUSE_ENABLED=true
```

**Sign-up is invite-only and SPA-native.** The React `/register` screen posts to
**`POST /api/auth/register`** — a guest route, throttled `6/min` per IP
(`throttle:register`), sitting outside the `auth:sanctum` group. The controller
resolves the globally unique opaque code with `RegistrationCodeResolver`, then
validates it through the package `CodeValidator` *before* creating the account
(so a bad code never mints an orphan user). It redeems authoritatively via
`RedemptionService` (atomic; run **outside** a DB transaction so the package's
PostgreSQL compensation path is not poisoned); on an exhausted-between-checks
race the brand-new account is **force-deleted** so the invite-only invariant
holds. The account is floored at `viewer` (layered on any grant role —
GRANT-never-revoke) and the SPA session is opened. Every invite-code failure
surfaces as a localized
**422 on the `invite_code` field** (`lang/{en,it}/register.php`, R24). Here
`invite_code` is **always required**, regardless of the `INVITE_REQUIRED` gate. The
whole auth surface — `/login`, `/register`, `/forgot-password`, `/reset-password` —
is the React SPA on a hard reload too; the legacy Blade auth views were removed.

Public registration codes have two explicit intents and are issued from the
global control plane with one Artisan command:

```bash
# Register a new account, then force company onboarding.
php artisan registration-invite:create --uses=1

# Join an existing operational tenant and project; onboarding is skipped.
php artisan registration-invite:create \
  --tenant=acme \
  --project=acme-kb \
  --role=viewer \
  --membership-role=member \
  --uses=1
```

Both forms are stored under the reserved `system-registration` tenant namespace,
which is seeded idempotently and marked `tenants.is_system=true`; it is a
technical partition, never an operational company and never appears in
`/api/auth/me.teams`. A code without `--tenant` carries the
`company_bootstrap` intent and creates **no** membership during registration.
The authenticated account is routed to `/app/onboarding` and cannot enter a
tenant dashboard until `POST /api/auth/onboarding/company` atomically creates
the company tenant, initial project and owner membership; the creator receives
the tenant `super-admin` role. The gate is resumable on the next login and also
applies whenever a normal account has no operational membership. A
`platform.admin` account remains in the global system control plane instead.

A code created with `--tenant` carries one explicit `tenant_join` grant. Its
target must be an active, non-system tenant and every `--project` must already
belong to it; redemption provisions those memberships and enters the company
directly. Registration adds a strict completion layer over the invitation
package's best-effort provisioners: the promised role and memberships are
verified transactionally before a session or token is returned, then
`users.registration_completed_at` is persisted. If the code was consumed but a
database fault prevented provisioning, registration returns
`503 registration_provisioning_pending`; the next valid login resumes from the
immutable redemption. Once completion is marked, removing the user from every
company is treated as an intentional revocation and never restores the old
grant. Neither flow falls back to the legacy slug `default`, which is reserved
and confers no implicit access. After a successful tenant-linked registration,
the SPA opens `/app/welcome/{teamHash}` and names the assigned company before
the user explicitly enters its chat; bootstrap registrations continue directly
to `/app/onboarding`.

The admin surface is a **native, in-app tabbed page** at
`/app/{team}/admin/invitations` (Overview · Campaigns · Codes · Invite ·
Referrals · Rewards · Waitlist · Anti-abuse), built on the same
`/api/admin/invitations/*` core so it stays inside the unified admin chrome +
team switcher — no new tab. It ships the invite-funnel dashboard (all 11
`MetricsService::summary` fields + a proportional funnel), a **campaign builder**
(create/edit with the **multi-tenant grant editor** — a Spatie role + KB project
memberships across one or more tenants), code inventory with batch generation /
Copy-all / CSV export / revoke, a **direct-invitation sender**, and read tables
for referrals, rewards, waitlist and anti-abuse (each with the honest "first 500
rows" truncation notice, since the core read surfaces are capped at 500). The
standalone `padosoft/laravel-invitations-admin` package panel is still offered as
an optional **"Advanced"** launcher, shown **only when
`INVITATIONS_ADMIN_ENABLED=true`** so it never links to the unregistered
`/admin/invitations` 404 (R14/R43); the host learns the flag from the additive
`features.invitations_admin` field on `/api/auth/me` (R27). See the
[doc-site page](https://padosoft.mintlify.app/invitations).

### Storage (Laravel disks)

KB markdown files are read through a Laravel filesystem disk, so the ingestion pipeline is **storage-agnostic**: local for dev, S3 for production, MinIO for on-prem — no code change needed.

Config file: `config/filesystems.php`. The dedicated `kb` disk defaults to `storage/app/kb`:

```env
# Disk used by kb:ingest and DocumentIngestor (see config/filesystems.php)
KB_FILESYSTEM_DISK=kb
KB_DISK_DRIVER=local
# KB_DISK_ROOT=/absolute/path/to/markdown/root

# Optional path prefix prepended to every ingested path
KB_PATH_PREFIX=
```

#### Switching to S3

Install the Flysystem S3 adapter once:

```bash
composer require league/flysystem-aws-s3-v3 "^3.0"
```

Then switch the disk driver and fill the AWS credentials:

```env
KB_FILESYSTEM_DISK=s3

AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_DEFAULT_REGION=eu-west-1
AWS_BUCKET=askmydocs-kb
AWS_URL=
AWS_ENDPOINT=              # set for MinIO / R2 / Wasabi
AWS_USE_PATH_STYLE_ENDPOINT=false
```

#### Ingesting a document

```bash
# Reads storage/app/kb/docs/setup.md (local disk)
php artisan kb:ingest docs/setup.md --project=erp-core --title="Installation Guide"

# Override the disk ad-hoc
php artisan kb:ingest docs/setup.md --project=erp-core --disk=s3
```

### Chat Logging

Chat logging is **off by default**. Enable it to get structured analytics about every Q&A turn.

Config file: `config/chat-log.php`

```env
CHAT_LOG_ENABLED=true
CHAT_LOG_DRIVER=database
CHAT_LOG_DB_CONNECTION=      # optional: dedicated DB connection
CHAT_LOG_RETENTION_DAYS=90   # scheduler rotates rows older than N days
```

#### Fields persisted per interaction

| Field | Description |
|---|---|
| `session_id` | Session UUID (from `X-Session-Id` header or auto-generated) |
| `user_id` | Authenticated user id (nullable) |
| `question` | User question |
| `answer` | Assistant response |
| `project_key` | Project key used as RAG filter |
| `ai_provider` | openai / anthropic / gemini / openrouter / regolo |
| `ai_model` | Specific model used |
| `chunks_count` | Number of retrieved context chunks |
| `sources` | Source document paths that contributed context |
| `prompt_tokens` / `completion_tokens` / `total_tokens` | Token usage |
| `latency_ms` | End-to-end latency |
| `client_ip` / `user_agent` | Client metadata |
| `extra` | JSON for custom fields (e.g. `few_shot_count`) |

Logging is wrapped in try/catch — a driver failure never breaks the user response.

### Knowledge Base

Config file: `config/kb.php`

```env
KB_EMBEDDINGS_DIMENSIONS=1536
KB_MIN_SIMILARITY=0.30
KB_DEFAULT_LIMIT=8
# Timezone the chatbot presents as "now" in the RAG system prompt so it can
# reason about time-relative questions ("documents from last month", "is this
# deadline past?"). The app keeps running on UTC; this only sets the zone the
# bot *displays* (ISO 8601). Must be a valid IANA timezone. Default Europe/Rome.
KB_PROMPT_TIMEZONE=Europe/Rome

# Chunking
KB_CHUNK_TARGET_TOKENS=512
KB_CHUNK_HARD_CAP_TOKENS=1024
# Tail-overlap budget for MarkdownChunker (approx tokens). 0 = off. Since v8.18
# this is active: it carries the tail of each oversized-section piece onto the
# next chunk on paragraph boundaries. APPLIES TO NEW INGESTS ONLY — ingest is
# idempotent on sha256(markdown), so changing this alone won't re-chunk existing
# docs; force a new version (the markdown CONTENT must change, or HARD-delete +
# re-ingest via `kb:delete --force` — a soft delete keeps the chunks).
KB_CHUNK_OVERLAP_TOKENS=64

# Embedding cache
KB_EMBEDDING_CACHE_ENABLED=true
KB_EMBEDDING_CACHE_RETENTION_DAYS=30
```

### `GET /api/kb/documents/search` (v3.0+)

Document title/path autocomplete used by the chat composer's `@mention` popover (T2.7/T2.8). Sanctum-protected.

**Query params:**

- `q` — search string (2-120 chars, escaped for `LIKE` wildcards via `\` + `ESCAPE '\\'` clause per R19; literal `_` and `%` in the query do NOT act as wildcards)
- `project_keys[]` — optional tenant scope (zero or more)

**Response:** `{ "data": [{ "id", "project_key", "title", "source_path", "source_type", "canonical_type" }] }`

Up to 20 results per request. Archived documents are excluded.

### Saved filter presets (v3.0+)

Authenticated users can save / load / delete personal filter combinations via `RESTful /api/chat-filter-presets` (consumed by the FE FilterBar dropdown — UI work in a follow-up FE PR).

- `GET    /api/chat-filter-presets` — list the user's presets (alphabetical by name).
- `POST   /api/chat-filter-presets` — create. Required body: `{ "name": "…", "filters": { … } }`. Per-user uniqueness enforced on `name` (422 on duplicate within the same account). Different users may pick the same display name independently.
- `GET    /api/chat-filter-presets/{id}` — show one. Returns `404` for IDs owned by a different user (deliberate — the API does not leak the existence of other users' presets).
- `PUT    /api/chat-filter-presets/{id}` — update name + filters; same `404` semantics for non-owned rows.
- `DELETE /api/chat-filter-presets/{id}` — delete; `204` on success, `404` for non-owned rows.

The `filters` JSON column carries a serialised RetrievalFilters payload — the same shape the chat controller's `KbChatRequest::toFilters()` consumes. Round-trip is lossless: load preset → POST to `/api/kb/chat` produces identical retrieval scope as if the user had re-selected every filter manually.

### Chat filters (v3.0+)

`POST /api/kb/chat` accepts an optional `filters` object that narrows the retrieval scope BEFORE reranking + graph expansion + rejected-approach injection — filters change the candidate population, not the post-hoc ranking. Every dimension is optional.

```json
{
  "question": "What is our cache invalidation policy?",
  "filters": {
    "project_keys": ["hr-portal", "engineering"],
    "tag_slugs": ["policy", "security"],
    "source_types": ["markdown", "pdf"],
    "canonical_types": ["decision", "runbook"],
    "connector_types": ["local", "google-drive"],
    "doc_ids": [42, 99],
    "folder_globs": ["hr/policies/**"],
    "date_from": "2026-01-01",
    "date_to": "2026-12-31",
    "languages": ["it", "en"]
  }
}
```

Field semantics:

- `project_keys` — multi-tenant scope; takes precedence over the legacy `project_key` field when both are sent.
- `tag_slugs` — match documents tagged with ANY listed slug (T2.3 join, ships in a follow-up).
- `source_types` — one of `markdown`, `text`, `pdf`, `docx` (validated against `App\Support\Kb\SourceType` so adding a new type extends the validator automatically).
- `canonical_types` — one of the `App\Support\Canonical\CanonicalType` enum values currently stored on `knowledge_documents.canonical_type`: `decision`, `module-kb`, `runbook`, `standard`, `incident`, `integration`, `domain-concept`, `rejected-approach`, `project-index`. The validator is built from `CanonicalType::cases()` so adding a new case auto-extends the accepted set.
- `connector_types` — connector identifier strings (for example `local`, `google-drive`, `onedrive`, `notion`, `asana`, `imap`). Accepted in v3.0 but currently a no-op in retrieval until the `connector_type` column is added in v3.1.
- `doc_ids` — explicit document-id allowlist (used by the `@mention` UI in the chat composer, T2.7).
- `folder_globs` — path globs against `source_path`. `*` matches a single segment (does NOT cross `/`), `**` matches across segments (e.g. `hr/policies/**` matches `hr/policies/leave.md` AND `hr/policies/inner/leave.md`), `?` matches a single char (not `/`). Applied PHP-side after the SQL pre-filter via `App\Support\KbPath::matchesAnyGlob` (PostgreSQL has no native fnmatch and `**` doesn't translate to LIKE cleanly).
- `date_from` / `date_to` — ISO 8601 date range against `indexed_at`. `date_to` must be after-or-equal to `date_from`.
- `languages` — ISO 639-1 codes (normalized to lowercase during DTO construction; the validator enforces `size:2`).

Pre-T2.2 callers using the legacy `{question, project_key}` payload keep working unchanged — internally `project_key` is wrapped into `filters.project_keys = [project_key]`. The response `meta.filters_selected` echoes the count of user-selected filter dimensions for the FE composer to render "5 filters selected".

### Multi-format ingest (v3.0+)

`kb:ingest-folder` now picks up `.md`, `.markdown`, `.txt`, `.pdf`, and `.docx` files automatically (default `--pattern` is the union of every supported extension). Operators who want pre-T1.8 markdown-only behavior pass `--pattern=md,markdown` explicitly.

With `KB_OCR_ENABLED=true` (v8.36, ADR 0029) the walker, the API, the upload modal and the connectors also accept `.png`, `.jpg`/`.jpeg`, `.tif`/`.tiff` and `.webp` (`image/*` → `SourceType::IMAGE`), and a PDF with no text layer is routed to OCR instead of being ingested empty. With the flag off (the default) every entry point refuses images exactly as before — see [Scanned documents & OCR](#scanned-documents--ocr-v836) below.

The `POST /api/kb/ingest` endpoint accepts an optional `mime_type` field per document (defaults to `text/markdown` for back-compat). Binary formats (`application/pdf`, `application/vnd.openxmlformats-officedocument.wordprocessingml.document`) require `documents.*.content` to be **base64-encoded**; the controller decodes-or-422 before writing to disk. Text MIMEs (`text/markdown`, `text/x-markdown`, `text/plain`) keep accepting raw content. Unsupported MIME types return 422 with an actionable error naming the supported set.

The `App\Support\Kb\SourceType` enum is a typed helper for the markdown/text/pdf/docx domain — `SourceType::fromMime()` and `SourceType::fromExtension()` are the canonical conversions used by the API controller and the folder walker. The actual ingest routing is config-driven via `config/kb-pipeline.php` (`converters` / `chunkers` / `mime_to_source_type`); adding a new format requires updating BOTH `config/kb-pipeline.php` AND `SourceType::fromMime()` / `fromExtension()` / `toMime()` / `supportedMimes()` so the API/CLI surfaces stay consistent with what the registry resolves.

### UI upload (admin drag-and-drop)

Admins can ingest documents straight from the KB admin page (no CLI / API client
needed). An **Upload** button (and drag-and-drop onto a project/folder node when a
single project is selected) opens a modal: files are buffered on the dedicated
`kb-staging` disk, reviewed, then on **Commit** moved to the canonical `kb` disk and
ingested through the **exact same pipeline** as `kb:ingest-folder` — one
`IngestDocumentJob` per file. The modal then polls
`GET /api/admin/kb/uploads/{batch}/status` and shows per-file progress
(`staged → queued → processing → succeeded | failed`). Accepted formats match the
CLI (`md`, `markdown`, `txt`, `pdf`, `docx`). Stale staging batches are swept daily
by `kb:prune-staging-batches` (retention `KB_STAGING_RETENTION_HOURS`, default 24h).

> **Queue prerequisite.** Meaningful, streaming progress requires an async queue
> and a running worker:
>
> ```bash
> # .env
> QUEUE_CONNECTION=database        # jobs / failed_jobs tables already exist
> # process (supervisor / systemd / Horizon)
> php artisan queue:work --queue=kb-ingest,default
> ```
>
> Under the default `QUEUE_CONNECTION=sync` the commit request runs the ingest
> inline and **blocks** until every file is parsed/chunked/embedded/persisted; the
> status endpoint then returns the terminal state on the first poll. Functional,
> but the per-file progress stream is only visible with a real queue + worker.
> Files canonical-typed (YAML frontmatter) are accepted but flagged with a
> non-blocking warning that they will not be committed to your git `kb/` repo —
> the canonical source of truth stays git → GitHub Action.

### Extending the Ingestion Pipeline

AskMyDocs v3.0 introduces a pluggable ingestion pipeline driven by `config/kb-pipeline.php`. To add support for a new file format:

1. **Implement** `App\Services\Kb\Contracts\ConverterInterface` — convert raw bytes to a `ConvertedDocument` (markdown + extraction metadata). Every converter MUST populate `extractionMeta['filename'] = basename($doc->sourcePath)` so the chunker can attribute chunks back to their source file.
2. **Implement** `App\Services\Kb\Contracts\ChunkerInterface` — or reuse `MarkdownChunker` if your converter outputs markdown (the default for prose formats).
3. **Register** in `config/kb-pipeline.php` under `converters` and `chunkers`.
4. **Map** the MIME type in `mime_to_source_type` so the pipeline can route to the right chunker.

Built-in converters (v3.0):

- `MarkdownPassthroughConverter` — `text/markdown`, `text/x-markdown`
- `TextPassthroughConverter` — `text/plain` (wraps prose in a `# {basename}` header so MarkdownChunker can section it)
- `PdfConverter` — `application/pdf` (smalot/pdfparser primary; falls back to `pdftotext` from Poppler when smalot rejects the file)
- `OcrConverter` (v8.36, `KB_OCR_ENABLED=true` only) — `image/png`, `image/jpeg`, `image/tiff`, `image/webp`; runs the configured OCR driver and emits `## Page N` sections with per-page confidence and figures (see [Scanned documents & OCR](#scanned-documents--ocr-v836))
- `DocxConverter` — `application/vnd.openxmlformats-officedocument.wordprocessingml.document` (parses the `.docx` package via `phpoffice/phpword`; maps `Heading{N}` paragraph styles to `#{×N+1}` markdown headings nested under the basename H1; tables become markdown pipe-tables. Embedded images are NOT extracted in v3.0 — planned for v3.1 with the vision-LLM pipeline.)

**PDF support:** `smalot/pdfparser` is a hard `require` (pure PHP, no system deps). For more robust extraction on complex PDFs (multi-column layouts, certain XFA forms, mixed encodings), install `poppler-utils` on the host (`apt install poppler-utils` on Debian/Ubuntu, `brew install poppler` on macOS) — the `PdfConverter` automatically falls back to the `pdftotext` binary when smalot raises an exception (`KB_PDFTOTEXT_BIN` names the binary; with OCR enabled, a PDF that neither smalot nor pdftotext can read text from is routed to OCR — a parser failure alone never is). `extractionMeta.extraction_strategy` records which strategy was used per document so you can audit the rate of fallbacks in production.

### Scanned documents & OCR (v8.36)

Default **OFF** (`KB_OCR_ENABLED=false`, [ADR 0029](docs/adr/0029-v836-ocr-converter-drivers-and-ocr-provenance.md)). When on:

- **Images** (`png`/`jpeg`/`tiff`/`webp`) become documents through `OcrConverter`; **scanned PDFs** stay with `PdfConverter`, which probes the text layer **per page** (`KB_OCR_PROBE_MIN_CHARS` per page over every page up to `KB_OCR_MAX_PAGES`; `KB_OCR_PROBE_PAGES` bounds the window) and delegates to `OcrService` when no page has text (`empty`), when typed pages and scanned pages coexist (`mixed` — the whole document is OCR'd so no page is lost) or when nothing can read the file. `PdfConverter` is the only PDF match — no overlapping `supports()` (R23).
- **Drivers** (`KB_OCR_DRIVER`): `tesseract` (default, local CLI), `docling` (local CLI, best layout/tables), `mistral-ocr` (remote API), `vision-llm` (a `laravel/ai` vision call on the configured chat provider), `fake` (tests only, refused in production). Remote drivers send the document bytes to a third party **before** the PII seam can see the text, so they run only with `KB_OCR_ALLOW_REMOTE=true` — the registry fails closed otherwise; `mistral-ocr` posts only to a host in `KB_OCR_MISTRAL_ALLOWED_HOSTS`, `vision-llm` goes through `AiManager` like every chat call, and every run is capped **before** egress by `KB_OCR_MAX_PAGES` / `KB_OCR_MAX_BYTES`.
- **Provenance**: every chunk carries `metadata.provenance = "ocr"` and `ocr_confidence`; the document records `extractionMeta.ocr.{driver, remote, reason, pages[], mean_confidence, figures}`. This is the *extraction origin*, orthogonal to the ADR 0028 `provenance_tier` (source authorship).
- **PII**: `ChunkRedactor` (ADR 0020) runs unchanged on the OCR output before embedding. **Figures** land at `{source}.ocr/{run}/images/fig-{page}-{n}.png` on the KB disk (`{run}` = content-addressed key of the OCR'd bytes **and** the engine — driver, its fingerprint, the figure switch — so versions and engines never overwrite each other, and an identical re-ingest through the same engine reuses the recorded run instead of paying again; `KB_OCR_REUSE_ENABLED=false` turns the recorded run off and makes every ingest a new run with its own directory — figures follow `KB_OCR_FIGURES_ENABLED` and the retention mode) and are referenced as `![Figure p.n](images/fig-p-n.png)`.
- **FinOps**: each run is a metered `ocr` purpose (`KB_OCR_RATE_PER_PAGE` × pages for locally-priced drivers; `vision-llm` is metered per token by the SDK hook, not double-counted). The upload modal shows the **estimate before commit** (`GET /api/admin/kb/uploads/{batch}/estimate`).
- **Tri-surface** (R44): `kb:ocr {document} [--status]` · `GET|POST /api/admin/kb/documents/{id}/ocr` · MCP `KbOcrStatusTool` (read-only — an agent can see, not spend).
- **OFF path** (R43): images are refused with the same 422 / "Unsupported file type" as before at the API, the upload modal, the folder walker **and** the connector bridge (recorded as `connector_ingest_refused` in `kb_canonical_audit`); scanned PDFs ingest as empty documents exactly as today.

Docs: [Documents & OCR](https://padosoft.mintlify.app/documents-and-ocr).

### Digitization Review (v8.37)

Default **OFF** (`KB_DIGITIZATION_REVIEW_ENABLED=false`, [ADR 0031](docs/adr/0031-v837-digitization-review-and-auto-tier-mapping.md)). This W3 cycle wires the existing `generation_source` tier (`human` / `auto`, ADR 0014) to what OCR produces: a converted page defaults to `auto` until a person looks at it and **approves** the document (the `auto → human` transition), branched on canonicity — a canonical document's approval reuses the Wiki Explorer's `promote()`; a non-canonical document (the ordinary OCR'd-scan case) gets the identical flip and audit event without touching `canonical_status`. Every mutating entry point is atomic under concurrent approvals (R21 — a `lockForUpdate()`'d re-read decides, never the caller's possibly-stale copy).

- **Reranker firewall closed for OCR**: the `human > auto > raw` anti-hallucination ranking (ADR 0014) now applies to non-canonical rows too — an unreviewed scan (`generation_source = auto`) ranks below a reviewed sibling scan at equal similarity, which was not true before this cycle (the auto-tier penalty used to short-circuit to zero for every non-canonical chunk).
- **Per-page review**: `kb_document_page_reviews` records one row per (tenant, document, page); setting a page's status is an idempotent database-level upsert (`INSERT ... ON CONFLICT/ON DUPLICATE KEY UPDATE`), never a second row even under concurrent reviewers, and a page can be reverted from `reviewed` back to `unreviewed`. A page number is validated against the document's own recorded `metadata.converter.page_count` — a document that was never converted, or a page beyond its real page count, is refused rather than silently accepted.
- **Agent-proposed text corrections (ADR 0031 §6-7)**: an agent may `propose` a probable transcription fix via the MCP `KbProposeTextCorrectionTool`, but only ever writes a CANDIDATE row (`kb_text_correction_candidates`) — never the corpus itself, per ADR 0003's "agent proposes, a person commits" boundary. MCP calls carry a tenant-scoped token with no per-user identity, so proposals share a fixed `mcp:kb-propose-text-correction` actor per tenant, honestly, rather than a fictitious per-user one. `old_text` must occur exactly once on the candidate's page; a replayed call (identical tenant/actor/document/version/page/old/new) returns the SAME candidate rather than a duplicate, and every outcome — accepted, EVERY denied reason, and replayed — is audited, with the whole check-then-act sequence serialized per tenant+actor. A human reviewer then `approve`s or `reject`s the candidate over HTTP only (no MCP write for that decision) — approval is a three-phase flow that atomically claims the candidate (`applying`) before applying anything, refuses a CANONICAL document outright (its YAML frontmatter can't survive chunk-reconstructed re-embedding), re-validates `old_text` against the family's CURRENT live version — reconstructed with page boundaries re-synthesized from chunk metadata when no artifact is retained — (rejecting a now-stale candidate rather than silently misapplying it), and, on success, mints a genuinely NEW version through `DocumentIngestor::reembedFromMarkdown()` — never a write to the original `source_path` binary, and never inside an ambient transaction that could orphan its side effects — flips the candidate to the terminal `applied` state, and writes a `kb_canonical_audit` row (best-effort — a write failure there is logged, never reported to the caller as approval failure). A candidate stuck `applying` after a crashed approval is recoverable via `kb:review-reconcile-stuck-corrections`, not silently indistinguishable from success.
- **Tri-surface, so far**: `kb:review {document} [--page=N --status=reviewed|unreviewed] [--approve] [--report]` (CLI) · `GET /api/admin/kb/documents/{id}/review-summary` (document-wide), `GET .../pages/{n}` (single page), `PATCH .../pages/{n}/review-status`, `POST .../approve`, `GET .../documents/{id}/corrections` (paginated pending queue), `POST .../corrections/{id}/approve`, `POST .../corrections/{id}/reject` (HTTP, admin-gated) · MCP `KbReviewStatusTool` (read-only — reports progress, never marks or approves anything itself) + `KbProposeTextCorrectionTool` (write — a CANDIDATE only). `kb:review-reconcile-stuck-corrections` is a documented R44 single-surface exception (CLI-only, no caller-facing read) — see [Crash recovery](https://padosoft.mintlify.app/digitization-review#gotchas).
- **Review tab**: the admin KB document detail pane has a `Review` tab (`ReviewTab`) wired to the HTTP surfaces above — per-page reviewed/unreviewed toggle with Prev/Next navigation (degrades to an explanatory message when the document has no recorded `page_count`), the document-level Approve action, and the pending correction-candidate queue with approve/reject.
- **Not yet shipped** (deferred past v8.37 GA, documented in the [closure STATUS](docs/v4-platform/STATUS-2026-09-20-v837-w3-closure.md)): the *advanced* review UI (original ↔ Markdown side-by-side, confidence heat-map), the CER/WER quality metrics, and the `laravel-flow` review-queue workflow integration.
- **Config**: `KB_REVIEW_LOW_CONFIDENCE_THRESHOLD=0.70` — the OCR confidence (chunk metadata, W1) below which a span is highlighted in the not-yet-shipped review UI's heat-map; a visual aid only, it never gates approval. `KB_REVIEW_CANDIDATES_PER_HOUR=60` — the rate cap on `KbProposeTextCorrectionTool`, shared **per tenant**, not per user (ADR 0031 §6): the MCP connection carries a tenant-scoped token, not a per-user one, so every caller in the tenant spends from the same hourly budget. `KB_REVIEW_CORRECTIONS_PAGE_SIZE=50` — the cap on `GET .../documents/{id}/corrections`'s pending-candidate queue.

Docs: [Digitization Review](https://padosoft.mintlify.app/digitization-review).

### Portable Wiki Export + candidate-only import (v8.38)

Default **OFF** (`KB_WIKI_EXPORT_ENABLED=false`, [ADR 0032](docs/adr/0032-v838-portable-wiki-export-and-candidate-only-import.md)) — the one flag gates every export AND import surface; there is no separate import-specific flag. W4a shipped the synchronous CLI export core: `kb:export-wiki {--tenant} {--project} {--as-user} {--output}` builds an ACL- and PII-scoped folder (`wiki/`, `raw/`, `README.md`, `AGENTS.md`, `CLAUDE.md`, `MANIFEST.json`) under an operator-chosen directory. The exported set is exactly what `--as-user` may retrieve — computed by authenticating as that user for the export's duration so `AccessScopeScope` (the same global scope every other read surface goes through) applies to the document query itself, never filtered after the fact. `raw/` is the stored conversion artifact or an explicit `raw_missing` manifest entry (never a chunk reconstruction passed off as the original); `wiki/` is the readable compiled page and may legitimately fall back to a reconstruction. Both `raw/` and `wiki/` go through the tenant's PII policy when active — the export inherits the same redaction contract as ingestion, not a weaker one. `MANIFEST.json` hashes every file (sha256) plus a running chain hash so a folder found later can be checked for internal consistency (accidental corruption, a truncated copy) — the chain hash is unkeyed and stored in the same folder it covers, so it is a corruption check, not cryptographic tamper evidence against a malicious actor; that would need a server-held, out-of-band signature, which is not designed yet.

**W4b adds the async HTTP surface** (ADR 0032 §5/§11/§12): `POST /api/admin/kb/exports` (`role:admin|super-admin`) computes an idempotency key from the tenant/principal/project/options/corpus snapshot/authorization digest — a repeat request while nothing has changed reuses the same bundle instead of re-exporting — and queues `ExecuteKbWikiExportJob`, which reloads the requesting `User` by id (never a serialized `Auth` object), re-checks they still hold the export permission, authenticates as them for the export's duration, and clears the guard in `finally` (mirrors `ExecuteAgentRunJob`'s own principal-restoration discipline so a reused queue worker can never leak one export's principal into the next). The job zips the folder and stages it on `kb.staging.disk` (ADR 0029's disk, reused — not a new one). `GET /api/admin/kb/exports/{id}` polls status; `GET .../{id}/download` re-authorizes the CURRENT session against the export's recorded document ids and answers `403 export_invalidated` if any are no longer visible, rather than serving bytes a stale idempotency key happened not to catch — the second, independent gate the ADR requires alongside the idempotency key itself. `kb:prune-wiki-exports [--dry-run]` sweeps expired bundles by `expires_at`, scheduled hourly (`onOneServer()->withoutOverlapping()`, distinct from the once-nightly `kb:prune-staging-batches`).

**W4c closes the loop** (ADR 0032 §4/§7/§11): every exported folder now ships a `.mcp.json` at its root (`KbWikiExportService::buildMcpConfig()`) pointing at the tenant's live MCP server, with `${ASKMYDOCS_MCP_TOKEN}`/`${ASKMYDOCS_TENANT_ID}` as placeholder environment-variable references — never an embedded credential. Every exported page's frontmatter now round-trips through `CanonicalParser` (`slug`/`id`/`type`/`status` ahead of the existing governance fields), so a page pulled back — by hand, by an agent, or via `kb:import-wiki {folder} --tenant= --as-user=` walking a whole local `wiki/` tree — parses back into the same canonical identity it was exported with. Import is **candidate-only** (ADR 0003's "agent proposes, a person commits" boundary, same shape as v8.37/W3b's correction candidates): `KbWikiImportService::importDocument()` never writes `knowledge_documents` itself, only dispatches the same `PromotionFlow` saga `KbPromotionController::promote()` already uses, pausing at a human approval gate. A replay of an already-proposed change (`kb_wiki_import_candidates`'s `idempotency_key`) returns the existing candidate rather than a fresh approval token — `ApprovalTokenManager::reissuePendingForStep()` is one-shot by design. An edit that only changes frontmatter (`type`/`status`/`retrieval_priority`) with an unchanged body still proposes a candidate; a body-only diff would have silently dropped it. Tri-surface (R44): the HTTP `POST /api/admin/kb/imports` and MCP `KbImportWikiTool` both propose a single document; only the CLI walks a local folder, since local filesystem access is the point (same rationale as export's CLI-only shape). `KbCreateExportTool`/`KbGetExportTool` complete the export side's MCP surface.
- **Not yet shipped**: `llms.txt`/`llms-full.txt`, and `include_images`/`--format` variants (both explicitly rejected, never silently ignored, by the async request service — only `format="llm-wiki"` and `include_images=false` are implemented).
- **Config**: `KB_WIKI_EXPORT_ENABLED` (the gate for every export AND import surface), `KB_WIKI_EXPORT_RETENTION_HOURS=24` (drives both the DB row's `expires_at` and the hourly sweep), `KB_WIKI_EXPORT_QUEUE=default` (queue name for `ExecuteKbWikiExportJob`), `KB_WIKI_IMPORT_CANDIDATES_PER_HOUR=30` (per-tenant import-proposal rate limit, checked after the idempotency lookup so a replay never spends the budget), `KB_WIKI_EXPORT_CREATE_REQUESTS_PER_HOUR=10` (per-principal rate limit on MCP-initiated export requests).

Docs: [Portable Wiki Export](https://padosoft.mintlify.app/portable-wiki-export).

### Auto-Wiki maintenance as a delegated routine (v8.39)

Default **OFF** (`KB_WIKI_ROUTINE_ENABLED=false`, [ADR 0033](docs/adr/0033-v839-auto-wiki-maintenance-as-a-delegated-routine.md)) — `kb:wiki-maintain`'s existing nightly cron (index rebuild + lint + backfill un-enriched docs) can optionally run as a named, observable **routine** instead of an anonymous scheduler entry, via `padosoft/laravel-routines` v1.2.0 — a real agentic-routine engine (schedule, dispatch, mandate/consent, budget, escalation), a `require` Composer dependency like every other `padosoft/*` package in this repo (ADR 0033 corrects the plan's original "optional dependency" framing once the real package was installed and read: "optional" means the *feature* an operator may not enable, never the *package* an installation may not have). `WikiMaintenanceRoutineTarget implements RoutineTarget` — a thin adapter over the UNCHANGED `WikiMaintainer` core, declaring the same two action classes (`kb.wiki.compile`, `kb.wiki.lint`) it has always had. `WikiRoutineService` is the one core behind the tri-surface — status, run, and auto-provisioning a `Routine` row on first use, the package's generic `organization_id` column repurposed to hold this app's `tenant_id` (the engine has no tenant concept at all; R30 scoping is entirely this service's job, not the package's). `WikiMaintenanceRoutineGate` is the "no double run, no orphaned run" scheduler decision — keep the legacy cron slot (the safe default) unless the flag is on, the adapter is registered, AND an active routine exists **for the tenant the legacy slot itself services** (`default` — `KbWikiMaintainCommand`'s own signature default), wrapped in `try/catch` and failing safe to "keep the cron" on any database error, since the check runs on every console boot, not only `schedule:run`. The package's own generic admin API (`api/routines/v1`) and its signed webhook ingress (`hooks/routines/{id}`) are both turned **off** by default (`ROUTINES_API_ENABLED=false`, `ROUTINES_WEBHOOKS_ENABLED=false`) — the admin API has no tenant boundary and defaults to cross-tenant read access for any authenticated user with no policy defined, and nothing this app creates is a `trigger_kind=webhook` routine. Tri-surface (R44): `kb:wiki-routine {status|run}` · `GET /api/admin/kb/wiki-routine` + `POST .../run` (`role:admin|super-admin`) · MCP `KbWikiRoutineStatusTool` (read-only — no MCP `run` tool, documented R44 exception, same posture as W1's OCR re-run and W3's review approval).
- **Documented gap, not an oversight** (ADR 0033 §7): no mandate/consent-grant step-up flow is wired this cycle. The routine runs with exactly the authority the unattended cron already had; the engine's `MandateExceeded`/pause-and-ask machinery is real and wired through, but nothing this cycle can trigger it.
- **Independent review caught two must-fix issues before merge** (R36 fallback — neither Copilot nor `@codex review` responded): the gate's "an active routine exists" check was originally un-scoped by tenant, so any OTHER tenant enabling the routine for itself would have silently disabled the shared cron slot `default` still depends on; and the routine-provisioning find-then-create had no lock, a TOCTOU race that could double-provision a routine under concurrent triggers. Both fixed with regression tests proving the actual invariant, not just sequential idempotency.

Docs: [Auto-Wiki](https://padosoft.mintlify.app/auto-wiki).

Built-in chunkers (v3.0):

- `PdfPageChunker` — handles `pdf` and (v8.36) `image` source-types. Slices on the `## Page N` heading boundaries emitted by `PdfConverter`; emits one chunk per non-empty page with `heading_path = "Page N"` so citations like "see page N of foo.pdf" map 1:1 to a single chunk row. Pages exceeding `KB_CHUNK_HARD_CAP_TOKENS` are split intra-page on `\n\n` paragraph boundaries; all pieces of the same page share the same `heading_path` so page-level citations still resolve cleanly.
- `MarkdownChunker` — handles `markdown`, `md`, `text`, `docx` source types (any source whose converter outputs markdown). Uses `section_aware` mode: emits one chunk per ATX heading section with `heading_path` as a `>`-joined breadcrumb of H1-H3 ancestors. Falls back to `paragraph_split` (one chunk per blank-line-separated block) for documents without headings.

The chunker registry is order-significant — `PdfPageChunker` is listed FIRST in `config/kb-pipeline.php`'s `chunkers` so the first-match-wins resolution prefers it for `pdf` over the markdown fallback.

The polymorphic entry point is `DocumentIngestor::ingest(string $projectKey, SourceDocument $source, string $title, array $extraMetadata = [])`. The pre-v3 `ingestMarkdown(...)` is now a thin facade that synthesises a `text/markdown` `SourceDocument` and delegates to `ingest()` — IngestDocumentJob and the GitHub Action keep working unchanged.

### How it compares — the Annota AI gap, closed (v8.36 → v8.39)

The [Annota AI audit](docs/v4-platform/AUDIT-2026-09-11-annota-ai-gap.md) (2026-09-11, baseline v8.35.0) found one competitor moving into our category from the data-preparation side, with a §2.1 "where Annota AI is ahead" matrix that named the exact gap the v8.36 → v8.39 cycle above was built to close. Re-graded against what actually shipped, not the v8.35.0 baseline:

| Capability | v8.35.0 (audit baseline) | v8.39.0 (this cycle) | Annota AI |
|---|:---:|:---:|:---:|
| OCR of scans and images | ❌ | ✅ (`OcrConverter`, W1) | ✅ |
| Layout-aware conversion (tables, figures, LaTeX formulas) | ⚠️ | ✅ (figures to `images/`, LaTeX, W1) | ✅ |
| Per-asset review status (unreviewed → reviewed → approved) | ⚠️ | ✅ (`auto`/`human` tier + `KbReviewService`, W3) | ✅ |
| Immutable versions with faithful diff, correction-time `actor`/`reason` | ⚠️ (versions existed, but were chunk reconstructions born only on re-ingest) | ✅ (real conversion artifacts, correction-time versioning, W2) | ✅ |
| Content export as a portable workspace (`raw/`+`wiki/`, `.mcp.json`, hash-manifested) | ❌ | ✅ (`kb:export-wiki`, W4) | ✅ |
| MCP tools on the preparation loop (propose a correction, create/get an export, import edits) | ❌ | ✅ — but **propose-only by design** (ADR 0003): no MCP tool can set a review status directly, unlike Annota's `update_document_page`/`update_asset_review_status`, which let an agent rewrite content and mark it reviewed with no human gate | ✅ (no human gate) |
| Per-operation cost estimate before commit | ⚠️ | ✅ (FinOps cost estimate on the upload modal, W1) | ✅ |
| Side-by-side original↔Markdown pane with a confidence heat-map, CER/WER metrics | ❌ | ⚠️ **still partial** — the review/approve loop shipped (W3); the advanced side-by-side pane with a heat-map and CER/WER quality metrics is explicitly deferred, documented in the [W3 STATUS](docs/v4-platform/STATUS-2026-09-20-v837-w3-closure.md) | ✅ |
| Image labelling · Magic Select/Annotate · COCO · YOLO training | ❌ | ❌ — **out of domain by design** (audit §3: a different market); the one adjacency worth a small move, a `vision` column in Tabular Review, shipped as **v8.40.0** (W6, [ADR 0034](docs/adr/0034-v840-vision-column-in-tabular-review.md)) once a real image-heavy tenant signal arrived — colour/material/pattern extraction over OCR figures or a standalone product photo, human-reviewed in the existing grid | ✅ / 🔜 |

Where AskMyDocs was already ahead at the audit's baseline (§2.2 — hosted grounded Q&A, multi-tenant + source-ACL isolation, 9 connectors vs upload-only, the canonical layer + human-gated promotion + anti-repetition graph, self-compiling Auto-Wiki behind the `human > auto > raw` firewall, PII redaction + crypto-shred, AI Act as shipped modules, ingest-time provenance + injection boundary, an eval gate in CI, spend governance, tamper-evident audit trails, delegated identity/mandates/scheduled agents that pause to ask) remains unchanged and is not re-litigated here — see the audit's §2.2 for the full matrix. **The overlap that mattered — file → reviewed Markdown → portable, agent-consumable wiki — is closed**, and the two genuinely honest gaps that remain (the advanced review pane, and the mandate/consent step-up flow for the routine engine — [W5 STATUS](docs/v4-platform/STATUS-2026-09-26-v839-w5-closure.md) §7) are documented, not silently dropped.

### Multi-tenant deployment (v4.0)

The v4.0 cycle adds a **per-request tenant context** that scopes every Eloquent query against tenant-aware tables (R30/R31). Historical v3.x rows may still carry the storage value `tenant_id = 'default'`, but `default` is now a reserved, non-operational slug: it is never exposed as a team and never grants access. Every operational request requires an explicit membership in an active, non-system tenant.

**The plumbing**

| Piece | Path | Responsibility |
|---|---|---|
| `TenantContext` | `app/Support/TenantContext.php` | Request-scoped singleton; holds the active `tenant_id` for the duration of one HTTP request or one CLI command |
| `ResolveTenant` middleware | `app/Http/Middleware/ResolveTenant.php` | Reads the tenant from the configured resolver and sets `TenantContext`; runs at the top of the global middleware stack so every controller / job dispatched from the request inherits the context |
| `BelongsToTenant` trait | `app/Models/Concerns/BelongsToTenant.php` | Auto-fills `tenant_id` on `creating` events from `TenantContext::current()`; provides `forTenant($id)` query scope |
| `--tenant=X` CLI option | every domain Artisan command | CLI commands (`kb:ingest-folder`, `kb:rebuild-graph`, `kb:promote`, `insights:compute`) accept the option and set the context before running |

**Configuration (`.env`)**

```bash
# Single-tenant deployment (v3.x backward compatible — DEFAULT)
TENANT_DEFAULT=default
TENANT_RESOLVER=default          # always returns 'default'

# Multi-tenant by HTTP header (suitable for B2B SaaS with API gateway routing)
TENANT_RESOLVER=header
TENANT_HEADER_NAME=X-Tenant-ID

# Multi-tenant by domain (suitable for subdomain-per-customer deployments)
TENANT_RESOLVER=domain
TENANT_DOMAIN_PATTERN='([^.]+)\\.example\\.com'   # captures tenant slug

# Multi-tenant by authenticated user (suitable for shared-host SaaS)
TENANT_RESOLVER=auth
TENANT_USER_COLUMN=tenant_id     # column on the User model that holds the tenant
```

**What's tenant-scoped (and what isn't)**

The tenant-aware models — the authoritative list lives in `tests/Architecture/TenantIdMandatoryTest::TENANT_AWARE_MODELS`, kept in lock-step with the migrations by the architecture test on every CI run (it spans `KnowledgeDocument` / `KnowledgeChunk`, the chat + conversation tables, the `kb_*` graph / canonical / engagement tables, `ProjectMembership` + the first-class `Project`, and the `KbIngestBatch` / `KbIngestBatchItem` upload-tracking pair, among others) — all carry `tenant_id` and use the `BelongsToTenant` trait. The composite FKs on `kb_edges` are **project-scoped** (`(project_key, node_uid)` — intra-project referential integrity); cross-**tenant** isolation is enforced at the **application layer** via the R30 `forTenant()` scope (`BelongsToTenant` auto-stamps on write but adds **no** global read scope), not by the FK — `project_key` is shared across tenants.

`embedding_cache` is **intentionally NOT tenant-aware** — the cache is a cross-tenant reuse layer keyed by the composite `UNIQUE (text_hash, provider, model)` (v4.0.1, widened from `text_hash` alone so multiple provider/model embeddings of the same text coexist without forcing a flush). Sharing embeddings across tenants is a deliberate cost optimisation; `TenantIdMandatoryTest` documents the exclusion.

**The 6 v4 cycle rules guard the boundary**

| Rule | What it enforces |
|---|---|
| **R30** | Every Eloquent query against a tenant-aware table MUST be scoped to the active tenant via `forTenant()` or explicit `where('tenant_id', $ctx->current())` — cross-tenant leak is a GDPR catastrophe |
| **R31** | Every tenant-aware model MUST `use BelongsToTenant;` and list `'tenant_id'` in `$fillable`; `tests/Architecture/TenantIdMandatoryTest.php` enumerates the model list and gates new entries on every CI run |
| **R36** | Mandatory Copilot review + CI green loop on every PR — caught the v4 PR #98 reg