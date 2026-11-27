# flame

[中文](README.zh.md) | English

A Go-based, multi-tenant AI agent platform. It manages agents, skills, tools and workflows as first-class build artifacts,
exposes them as callable endpoints (MCP / RPC), and shows everything currently running in a single runtime ledger.

Ships with a Vue 3 admin console (`desktop/`), shared by the tenant side and the platform side.

> **Want to run the whole thing?** `deploy/poc/` is a two-container demo (the product stack + the LiteLLM gateway) that
> starts with `docker compose` and listens on a single port — see [`deploy/poc/README.md`](deploy/poc/README.md). A prebuilt
> image is published on every push, so running it needs no toolchain. It is a proof of concept, not a production deployment.
>
> **Want to deploy it for real?** Every `v*` tag publishes the five production images to GHCR and one host tarball to
> that release, and installing needs no toolchain either:
> [`deploy/prod/INSTALL.md`](deploy/prod/INSTALL.md) is the command-by-command path — one host first (tier 1), then the
> same install grows onto bare-metal executor nodes (tier 2) and across machines (tier 3), never reinstalled. What each
> directory holds is in [`deploy/prod/README.md`](deploy/prod/README.md).

## Features

**Build artifacts**

- **Agents** — prompt + model + tools + skills, with knowledge bases, tool permissions and a per-agent default reply language
- **Skills** — a capability package of `SKILL.md` plus scripts, executed inside the sandbox
- **Tools** — a tool catalog (MCP / RPC and other inbound capabilities), plugins, and custom tools
- **Workflows** — visual orchestration (nodes / edges / variables) with a debugger, versions and releases

**Runtime**

- **Runtime ledger** — a cross-instance view of what is running (agents + workflows), filterable by type / duration, and cancellable
- **Run history** — persisted records, queryable by workflow / status / time range, exportable as CSV, cleanable per record or by filter
- **Endpoints** — expose an agent or a workflow as an MCP or RPC entry point, with a per-tenant "expose / retract" switch
- **Sandbox** — scripts and commands run in isolated units (docker / nsjail / none) with resource limits and a network kill switch

**Platform**

- **Multi-tenancy** — one PostgreSQL schema per tenant; tenants and their accounts are provisioned from the platform console
- **Asset market** — list and install assets across tenants (`listed` / `delisted`)
- **Settings** — models and connections, server-side auth (apikey / oauth), global variables (secrets encrypted at rest)

## Screenshots

| Runtime ledger · who is running what across instances, filterable by type / duration, cancellable | Run history · persisted records, queryable by workflow / status / time range, exportable as CSV |
|---|---|
| ![Runtime ledger](docs/screenshots/01-runtime.png) | ![Run history](docs/screenshots/02-runtime-history.png) |
| Workflow editor · nodes / edges / variables, with debugger, versions and releases | Agent · prompt + model + tools + skills assembly |
| ![Workflow editor](docs/screenshots/03-flow-editor.png) | ![Agent](docs/screenshots/04-agent.png) |
| Endpoints · expose agents / workflows as MCP / RPC, toggle exposure per tenant | Tools · catalog / plugins / custom tools, three sources in one place |
| ![Endpoints](docs/screenshots/05-endpoints.png) | ![Tools](docs/screenshots/06-capabilities.png) |

## Components

| Directory | Language | Purpose |
|---|---|---|
| `nexus/` | Go | Main service: platform API, tenant API, admin API (default `:27006`) |
| `sandboxd/` | Go | Sandbox daemon: isolated execution of scripts / commands / browser (default `:27081`) |
| `sandboxg/` | Go | Sandbox gateway: unified `/v1/*` for `nexus`, with load balancing and sticky routing (default `:27080`) |
| `tools/` | Go | Shared local libraries used by all three services (`xhttp` / `xsql` / `xlog` / `sandbox` / `code` …) |
| `desktop/` | Vue 3 + Vite | Admin console (dev port `:5173`) |
| `deploy/` | Docker | Deployment: `deploy/poc/` is the two-image demo (product stack + LiteLLM gateway) |

Dependency direction is one-way: the three services reference the local libraries via `replace flame/tools => ../tools`;
`tools` never depends back on any service.

```
browser ── desktop ──> nexus ──┬──> PostgreSQL    business data (one schema per tenant)
                               ├──> Redis         runtime ledger / stop signals / quotas
                               ├──> LiteLLM       model calls
                               └──> sandboxg ──> sandboxd ──> isolated unit
                                                              (docker / nsjail / none)
```

## Design highlights

A few decisions that run through the whole repository and shape both speed and boundaries. The full write-up lives in
[`nexus/docs/design-highlights.md`](nexus/docs/design-highlights.md).

- **Endpoints are called in-process** within the owning tenant: an `rpc` node invoking a flow or an agent pays no network hop,
  and stdio MCP sessions reuse one child process per connection, rebuilt only when the configuration fingerprint changes.
- **Recursion is bounded by a depth limit plus an ancestor-chain check, not a counter**: every cross-run hop creates a fresh
  `ExecContext`, so per-run counters reset. Configuring the limit as `-1` / `0` ("unlimited") is deliberately refused here — for
  pure flow chains this is the only gate.
- **Multi-tenancy is schema-per-tenant with explicit schema qualification**: no reliance on `search_path`, which is unsafe once
  connections are pooled. Quotas and runtime limits are clamped through "system ceiling → tenant → user".
- **An endpoint is one row of target × protocol**: `exposed` only means "visible outside the tenant"; in-tenant calls ignore it.
  Authorization binds to the **target** (agent / flow), not the endpoint, because endpoints can be recreated while targets are
  stable identities.
- **Fewer database reads on the hot path**: the endpoint catalog comes from a run-time snapshot; configuration and quotas use a
  Redis read-through cache (including negative caching); runtime parameters are frozen once when a run starts.

## Requirements

- Go **1.25+**
- Node **18+** (frontend build)
- PostgreSQL **14+**
- Redis **7+**
- LiteLLM Proxy (model calls; disable with `litellm.enabled` if you don't need models)
- Optional: Docker (`mode: docker` for `sandboxd`, recommended in production), Consul (service discovery)

## Quick start

### 1. Start dependencies

Run PostgreSQL and Redis locally (default ports `5432` / `6379`), and LiteLLM (on `:4000`) if you need models.

### 2. Configure nexus

```bash
cp nexus/config.example.yaml nexus/config.yaml
```

Then edit `nexus/config.yaml`; at minimum change the database connection, `jwt.secret_key` and `litellm.master_key`.

Everything can also come from environment variables (`${VAR}` is expanded before YAML parsing):

```bash
# Linux / macOS
export JWT_SECRET="$(openssl rand -base64 48)"
export LITELLM_MASTER_KEY="sk-..."
# Windows PowerShell
$env:JWT_SECRET = [Convert]::ToBase64String([byte[]](1..48 | ForEach-Object { Get-Random -Maximum 256 }))
```

> A leaked `jwt.secret_key` means anyone can self-sign a token and operate on any tenant. Always use a random value and never
> commit it. The real `nexus/config.yaml` is excluded by `.gitignore`.

### 3. Start the services

```bash
# nexus
cd nexus && go run ./cmd

# sandboxd (in another terminal)
cd sandboxd && go run ./cmd/sandboxd

# gateway (optional, only needed for multi-backend load balancing)
cd sandboxg && go run .
```

`sandboxd` defaults to `mode: none` (direct host execution, local development only). In production switch to `docker` or
`nsjail`; see `sandboxd/config.yaml`.

### 4. Start the frontend

```bash
cd desktop
npm install
npm run dev      # http://localhost:5173
```

The dev server proxies `/nexus` to `http://localhost:27006` (see `desktop/vite.config.js`).

## Repository layout

```
nexus/
  admin/          admin endpoints (platform + tenant)
  service/        business services (agent / flow / capability / market …)
  shared/         config, repositories, auth, logging
  platform/       platform bootstrap and tenant template (including agent definition files)
  docs/           terminology, sandbox design, workspace layout
sandboxd/         isolated execution (docker / nsjail / none) + codehost
sandboxg/         sandbox gateway
browserg/         browser gateway (sticky routing across browser pools)
browserd/         standalone browser pool (Chromium per session)
tools/            shared libraries
desktop/          Vue 3 admin console
```

## MCP protocol version

Endpoints speak **MCP `2026-07-28` only** — the stateless revision: no `initialize` handshake, no protocol-level
session, and every request carries `protocolVersion` / `clientInfo` / `clientCapabilities` in `params._meta`. A client
that defaults to the older protocol is refused at the transport layer; see
[`nexus/docs/mcp-support.md`](nexus/docs/mcp-support.md) for the exact failure modes and for the outbound side.

## RPC protocol

Beside MCP, an endpoint can also be exposed as **a plain JSON-RPC 2.0 surface** (`protocol = rpc`). It is the same
`svc_endpoints` row over the same target with the same `exposed` semantics — only the envelope differs, and a caller
that already speaks MCP recognises the payloads.

**Its unique value is what a third-party protocol structurally cannot offer.** MCP is the interoperability bet on other
people's clients; rpc is the one whose version, error semantics and call context we define ourselves. Three things
follow, and none of them is available to an MCP-only surface:

- **The only in-tenant capability bus.** The `local__<endpoint>` tools an agent can be granted are rpc endpoints
  exclusively; MCP rows stay out of the grant system entirely, because `exposed` is deliberately not checked for a call
  coming from inside the tenant. "Let my own agent call my own sub-flow without exposing it" has no other protocol.
- **The only carrier for the call chain.** Cycle protection needs state that crosses runs — every hop creates a fresh
  `ExecContext`, so a counter restarts. The chain is part of the wire contract (`params._meta.call_chain` across
  processes, `_call_chain` in-process, both stripped before the model sees them), so `f → a → f` is refused at the
  second hop instead of running to the depth limit: one attempt instead of a full budget, and no pool of workers left
  waiting on each other.
- **The only place where a business rejection cannot be reported as a server fault.** Standard codes mean "you sent
  something wrong"; quota exhaustion (`-32000`), call loops (`-32001`) and configuration errors (`-32002`) sit in the
  implementation-defined range, so a client that maps `-32603` to "the server broke" does not page an operator over a
  caller-side quota problem.

What keeps that affordable is the twin discipline: the version rides in the envelope (`version`, major only, absent =
the minimum), results and `tools/list` keep the MCP shapes, and exposure is a **target**-level switch — retracting takes
every protocol of that target down in one statement, so a second protocol costs a row, not a second switch and not a
second grant.

This is still not a replacement for MCP: no third-party ecosystem, tools surface only (no resources / prompts /
sampling). The trade is straightforward — MCP buys reach, rpc buys control, and the endpoint model lets a single target
hold both at once. See [`nexus/docs/design-highlights.md`](nexus/docs/design-highlights.md) for the reasoning.

## Docs

- `nexus/docs/terminology.md` — terminology and verb conventions (read this before changing code)
  ([中文](nexus/docs/terminology.zh.md))
- `nexus/docs/sandbox-design.md` — sandbox isolation design and the three execution channels
  ([中文](nexus/docs/sandbox-design.zh.md))
- `nexus/docs/mcp-support.md` — MCP support: the single protocol version (`2026-07-28`), why it is stateless, and how
  a failed handshake surfaces ([中文](nexus/docs/mcp-support.zh.md))
- `nexus/docs/deployment.md` — the deployment plan: single-host native layout, artifact inventory, the knobs a
  multi-instance deployment needs ([中文](nexus/docs/deployment.zh.md))
- `nexus/docs/deployment-runbook.md` — the operational companion: tiers, configs, first boot, upgrade, backup,
  acceptance checks, troubleshooting ([中文](nexus/docs/deployment-runbook.zh.md))
- `nexus/docs/workspace-layout-and-supervisor-power.md` — tenant workspace layout
  ([中文](nexus/docs/workspace-layout-and-supervisor-power.zh.md))
- `nexus/docs/design-highlights.md` — design highlights: call-chain recursion, multi-tenant quotas, endpoint model
  ([中文](nexus/docs/design-highlights.zh.md))
- `nexus/docs/i18n-plan.md` — the layered bilingual plan, its costs and pitfalls ([中文](nexus/docs/i18n-plan.zh.md))
- `nexus/docs/error-codes.md` — business error-code conventions (a prerequisite for a bilingual UI)
  ([中文](nexus/docs/error-codes.zh.md))
- `nexus/docs/node-audit.md` — the per-node audit: which dimensions each node type is checked on, what a test or gate
  already enforces, and what is still to audit ([中文](nexus/docs/node-audit.zh.md))
- `browserd/README.md` — the standalone browser pool: how nexus reaches it, how to build and deploy it, and the three
  settings that must line up ([中文](browserd/README.zh.md))
- `browserg/README.md` — the browser gateway: sticky routing, the per-tenant cap, and why it is not part of sandboxg
  ([中文](browserg/README.zh.md))
- `AGENTS.md` — module map and cross-domain ground rules

## Security notes

- `nexus/config.yaml` and `desktop/.env` are machine-local configuration and are not committed.
- `nexus/data/` (tenant workspaces) is ignored and never committed.
- Change default credentials before deploying, and configure tokens for `sandbox` / `sandboxg`.

## License

[Apache License 2.0](LICENSE)
