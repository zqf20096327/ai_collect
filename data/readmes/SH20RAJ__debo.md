# Debo — Private AI Memory & Context OS

[![Implementation](https://img.shields.io/badge/implementation-in_progress-yellow)](PROJECT_STATUS.md)
[![Production readiness](https://img.shields.io/badge/production_readiness-not_verified-red)](PROJECT_STATUS.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**A personal memory layer for AI: capture your information, retrieve it with provenance, and build toward an assistant that understands your life over time.**

Debo is an open-source project for collecting journals, notes, documents, and connected context in one user-controlled system. Its goal is to make personal information queryable and useful across AI tools without making the model itself the authority over access, permissions, or actions.

> **Honest status:** substantial application code, architecture, and security work exist in the repository. However, the current main branch has not been fully re-verified through a reproducible install, test, typecheck, lint, build, integration-test, and deployment-smoke-test run. Production readiness is **NOT VERIFIED**.

## Why Debo?

AI assistants often lose useful context between conversations, answer without showing where a claim came from, and keep personal context fragmented across services. Debo aims to provide:

- **Persistent personal context** — organize journal entries, notes, documents, and other sources over time.
- **Source-grounded retrieval** — return relevant context with provenance so users can inspect the underlying source.
- **A portable context layer** — expose authorized memory to supported AI clients through the Model Context Protocol (MCP).
- **User-controlled integrations** — connect external services behind explicit authorization and approval boundaries.
- **Privacy and tenant isolation by design** — enforce identity, workspace scope, and permissions in server-side code, never by asking an LLM to decide who may access data.

These are product goals and architectural responsibilities, not a claim that every end-to-end workflow is production-ready today.

## Current status

As of **4 November 2026**, the project is in **Production Build / Post-Phase-16 Hardening**. Historical roadmap phases and the presence of source files do not establish release readiness.

| Area | Current assessment |
|---|---|
| Monorepo, apps, shared packages | Source present; current build not verified |
| Authentication and workspace scoping | Implemented paths exist; end-to-end security evidence incomplete |
| Journal, source, and memory workflows | Partial implementation; provider and lifecycle behavior needs end-to-end verification |
| Agent graph and chat streaming | Source present; model-backed reasoning and verified durable checkpoint release gates remain open |
| MCP and integrations | Architecture and code present; deployment and real-provider behavior must be verified |
| Human approval and action execution | Fail-closed safeguards exist; complete durable approval-to-execution path is not ready |
| Generated UI | Debo-owned renderer is opt-in; official OpenUI integration is not accepted |
| Privacy export and erasure | Cross-store completeness remains a release blocker |
| CI and release evidence | Current main has zero exact-head Actions runs/check-runs; branch metadata reports `protected=false`. The last dispatch attempt (round 62) returned HTTP 422 because Actions were disabled for the connected owner/account; dispatch was not available in this audit |

See [PROJECT_STATUS.md](PROJECT_STATUS.md) for the latest audit record and [the production completion checklist](docs/operations/production-completion-checklist.md) for release blockers.

### How much is done?

**Latest whole-project audit estimates: 2.0–2.5% implementation completion and 0–0.01% production readiness (4 November 2026, audit round 70; audited source main SHA cd361207161ee4d55988af615a8f6e54ca0fa286).** These are confidence-weighted engineering estimates, not measured metrics. The canonical checklist remains 21 implemented-unverified, 0 verified, and 141 open out of 162; the raw implemented-unverified ratio is 12.96%, not a verified completion rate. Round 70 identified a final-mutation membership-cardinality gap across API-key and OAuth-client credential operations, and a stale-role OAuth-client metadata listing boundary. The HTTP API contract was reconciled to the owner/admin API-key creation policy; DEBO-0027 and DEBO-0031 planning records were updated. No application code changed and repository test/build/CI gates remain unverified. See [PROJECT_STATUS.md](PROJECT_STATUS.md) for the full audit, library inventory, evidence and limitations.

 The gateway-rendered public documentation has since been corrected: it identifies MCP as a custom JSON-RPC prototype and Trigger.dev as a pre-production task adapter. The official MCP SDK v2 remains absent, the handler retains the legacy initialize handshake, and the Trigger.dev wrapper's step cache and compensation callbacks are process-local and are not wired to the production worker event path. Treat these capabilities as unverified until DEBO-0020/0021/0022 pass. The implementation estimate reflects source that exists, not verified end-to-end functionality. Recent audits also confirmed that the Trigger.dev wrapper uses process-local step caching rather than durable step execution, the worker remains fail-closed in production, and connector sync can return a hard-coded 12-record success in the development/test executor. The database also lacks composite workspace/source/chunk constraints across source, memory, citation, and journal records, while the Docling conversion call now forwards its configured 500-page and 50 MiB limits to `DocumentConverter.convert()`. That call-site fix is present in source and has an authored forwarding test, but runtime enforcement remains unverified. Separate document-worker blockers remain: zero-chunk results can still be returned as `COMPLETED`, parser failures can fall through to pypdf/regex extraction, and generic or synthetic content/provenance can still be emitted. Authentication-secret entropy and secret-manager/deployment verification, workspace/API-key quota atomicity, workspace provisioning, OAuth rotation (including an in-flight refresh/consent-generation race and authorization codes that are not bound to the consent generation that issued them), and production image provenance also remain unresolved. These are source-level implementation and release risks—not evidence of a live compromise. Production Compose now fails earlier on missing configuration and uses real healthcheck paths, but still references mutable image tags without repository-owned MCP image build/provenance evidence. A tenant-scoped Neon state-snapshot adapter and migration do not establish native LangGraph saver support or atomic whole-graph semantics and have not been applied or integration-tested against Neon. The memory path lacks a canonical Neon memory writer and durable journal-to-provider outbox: journal persistence and Supermemory writes are separate, and retries are not idempotent. Production readiness remains effectively unverified: reproducible install/test/typecheck/lint/build and current-main CI evidence are absent, and approval/execution, authentication/tenant isolation, multi-store privacy, model/citation evaluation, provider/workflow integration, and deployment checks remain release blockers.

A feature should count as complete for release only when its behavior is implemented, authorized, tested, and verified in the target environment—not merely documented or committed.


### Checkpoint persistence status

Debo now contains a tenant-scoped Neon state-snapshot adapter, schema, and migration, and `POST /api/chat` selects it when `DATABASE_URL` points to Neon. Production fails closed rather than falling back to in-memory checkpoints. This is a meaningful implementation step, but the migration has not been applied and restart, concurrency, cross-tenant, and end-to-end behavior remain unverified; it is not yet a claim of native LangGraph checkpoint-saver support or atomic whole-graph transactions. See [the audit record](PROJECT_STATUS.md) and [release checklist](docs/operations/production-completion-checklist.md).

## Architecture at a glance

Debo is a TypeScript-first monorepo. Python is reserved for document processing.

~~~text
Web UI (Next.js) ── AG-UI ── LangGraph agent
                                  |
                     +------------+------------+
                     |            |            |
                Memory layer   Connectors   Debo tools
                     |            |            |
                     +------------+------------+
                                  |
                      Canonical business state
                        Neon PostgreSQL
                                  |
                         Original source files
                            Cloudflare R2

Trigger.dev workflows ── ingestion / background processing
Python document worker ── Docling / document extraction
MCP server ── authorized context for compatible AI clients
~~~

### Technology choices

| Layer | Primary technology | Responsibility |
|---|---|---|
| Web application | Next.js, React, TypeScript | Product UI, authenticated routes, chat |
| Agent orchestration | LangGraph JS | Typed state graph and bounded tool routing |
| Agent-to-UI protocol | AG-UI | Events and streaming between agent and UI |
| Database | Neon PostgreSQL, Drizzle | Canonical business data, permissions, provenance, audit |
| Raw file storage | Cloudflare R2 | Original source objects |
| Memory retrieval | Debo MemoryProvider abstraction, custom Supermemory HTTP adapter | Derived retrieval/index state; end-to-end provider behavior remains unverified |
| Background jobs | Trigger.dev 4.x adapter | Workflow integration exists, but process-local step caching is not production durability |
| Document processing | Python, Docling | Document layout and extraction |
| External AI clients | Custom MCP JSON-RPC server; official TypeScript SDK v2 migration remains open (DEBO-0022) | Tools/resources under server-side authorization; modern SDK v2 conformance is not established |
| Integrations | Custom Composio/Nango HTTP adapters | Provider-specific action/sync behavior remains partially integrated and unverified |

Neon owns canonical Debo business state; R2 owns original binary sources; memory providers hold derived retrieval/index state. External integration providers are not the source of truth for Debo permissions or business entities.

## Repository layout

~~~text
apps/
  web/               Next.js app and API routes
  mcp/               Model Context Protocol server
  worker/            TypeScript worker
  document-worker/   Python document-processing service
  gateway/           Cloudflare edge gateway
packages/
  agent/             LangGraph graphs, nodes, safety and tools
  auth/              Authentication and identity utilities
  citations/         Citation parsing and source-span validation
  config/            Shared runtime configuration
  connectors/        External service integrations
  db/                Drizzle schemas and migrations
  memory/            Memory-provider interfaces and adapters
  mcp/               MCP tools and resources
  permissions/       Authorization and policy logic
  types/             Shared domain types and contracts
  storage/            Object-storage integration
  ui/                 Debo-owned UI components; generative renderer disabled/opt-in
  workflows/          Background workflow definitions
docs/
  architecture/      System boundaries and designs
  adr/                Architecture decision records
  contracts/          API and domain contracts
  specs/               Normative requirements
  research/            Evaluations and evidence
  planning/            Roadmap and backlog
  operations/          Audit reports and release checklists
~~~

This is a navigational overview, not a guarantee that every listed subsystem is complete or deployed.

## Development

The repository uses **Bun workspaces** and **Turborepo**. The root manifest pins the package manager to Bun 1.4.2.

Install dependencies with the repository's locked dependency graph:

~~~bash
bun install --frozen-lockfile
~~~

Useful root scripts:

~~~bash
bun run dev
bun run test
bun run test:python
bun run typecheck
bun run lint
bun run build
~~~

Run these from the repository root. Some integration and production checks require configured services and environment variables; inspect the relevant app/package documentation before running them. Do not treat a command as passed until its exit status and output have been observed.

For a production audit, also verify database migrations against a disposable PostgreSQL instance, tenant-boundary behavior, provider failure/retry paths, and browser/API smoke tests. Never run destructive tests against real user data.

## Security model

Debo's security baseline is intentionally conservative:

- Authorization is enforced in server-side code; the LLM is not an authority.
- Every data operation must resolve canonical userId and workspaceId and enforce workspace scope.
- Imported documents, emails, web content, and connector data are untrusted input.
- Credentials and provider tokens must not be exposed in logs or client responses.
- Destructive and write-capable actions require server-owned policy, explicit approval where required, atomic one-time consumption, and idempotent execution.
- Generated UI may render only validated, allowlisted Debo components; rendering a UI is never permission to perform an action.
- Private memory responses must not be cached publicly.
- Privacy export and erasure must account for PostgreSQL, R2, memory providers, and connected services.

### Important release blockers

The current status records still identify these as incomplete or not adequately verified:

1. Durable Neon-backed LangGraph checkpointing with tenant-bound access controls.
2. Server-owned approval issuance, atomic one-time approval consumption, and idempotent real action executors with recovery for ambiguous outcomes.
3. Genuine model-backed reasoning with reproducible source-grounding and citation evaluations.
4. Complete privacy export and erasure across all stores and connected providers.
5. End-to-end authentication and tenant-isolation evidence.
6. Reproducible install, test, Python test, typecheck, lint, build, migration, and deployment-smoke-test results.

Until these are resolved and evidenced, write-capable or destructive production actions must remain disabled or fail closed.

## Generative UI and OpenUI status

Debo currently contains a **Debo-owned custom renderer**. It is not the official OpenUI Lang runtime and is not CopilotKit. The renderer is opt-in through the environment flag NEXT_PUBLIC_ENABLE_OPENUI_GENERATIVE_UI=true; keep the safe fallback otherwise.

[ADR-0018](docs/adr/ADR-0018-openui-and-agent-harness.md) remains **proposed**. Do not add an official OpenUI or CopilotKit dependency until a bounded feature-flagged proof of concept passes license, compatibility, security, adversarial-test, and reproducible-build gates. AG-UI and Debo's component allowlist remain the intended integration boundaries.

## Documentation guide

Start here before changing architecture or behavior:

- [Agent operating rules](AGENTS.md)
- [Project status and current audit evidence](PROJECT_STATUS.md)
- [System architecture](docs/architecture/system-overview.md)
- [ADR index](docs/adr/README.md)
- [Product and engineering roadmap](docs/planning/ROADMAP.md)
- [Security specification](docs/specs/security-spec.md)
- [Production completion checklist](docs/operations/production-completion-checklist.md)
- [Production build/security audit](docs/operations/production-build-audit-2026-10-25.md)
- [Documentation index](docs/README.md)

When documents conflict, follow the source-of-truth hierarchy in AGENTS.md and reconcile the documentation before implementing affected behavior.

## Contributing

Before opening a contribution:

1. Read AGENTS.md, relevant architecture docs, accepted ADRs, specs/contracts, and the current project status.
2. Check the live main ref and current diff to avoid repeating completed work.
3. Keep changes focused and preserve authentication, tenant isolation, and fail-closed behavior.
4. Add regression tests and run applicable checks.
5. Update status and documentation with exact commit references and evidence.
6. Never claim a test, build, deployment, or security check passed unless it actually ran and passed.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## License

Debo is licensed under the [MIT License](LICENSE).


## Debo mascot

The initial mascot direction is **the Sprout Robot**: a friendly little memory keeper with a midnight-blue face, cyan expression, white shell, and green sprout. The sprout represents personal growth and memories that grow with you.

![Debo Sprout Robot mascot](docs/assets/debo-mascot.svg)

The SVG is a lightweight, scalable source asset suitable for README previews and further refinement. The generated concept art shown in the design discussion is a visual reference; the repository's canonical asset is this editable vector, not a claim that the raster concept art has been committed.

Brand direction:
- **Midnight navy** #101B35 — trust and focus
- **Electric blue** #3B82F6 — intelligence and interaction
- **Soft white** #F8FAFC — clarity
- **Growth green** #65C878 — memory and personal growth

Use the simplified robot head for small app icons, and reserve detailed character illustrations for onboarding, empty states, and marketing. Keep the core mark recognizable at 32 × 32 pixels.


## Brand identity

Debo's mascot is a friendly white-and-silver robot with a midnight-blue face, cyan expression, electric-blue ear lights, and a two-leaf green sprout. The sprout represents growth and memory.

![Debo mascot](apps/web/public/brand/debo-mascot.svg)

**Tagline:** *Your AI companion for a more organized, capable life.*

The app generates its icon, Apple touch icon, and Open Graph/social preview from the brand source, and declares install metadata in the PWA manifest. Editable assets live in [the brand folder](apps/web/public/brand/README.md). Twelve emotion states communicate UI tone; the companion set introduces **Memo** (memory), **Lumi** (learning), and **Orbit** (planning/focus). See the [character guide](docs/brand/characters-and-assets.md) for details.

Palette: navy `#101B35`, electric blue `#3B82F6`, soft white `#F8FAFC`, growth green `#65C878`, cyan `#67E8F9`.
