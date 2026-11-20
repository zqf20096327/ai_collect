<div align="center">

<img src="docs/assets/banner.svg" alt="Bridge-Agents — visual AI workflows grounded in your documentation" width="100%" />

# Bridge-Agents

**Visual AI workflows for customer support, grounded in your documentation.**

<sub>Design the conversation flow on a drag-and-drop canvas, ground every answer in your own knowledge base with citations,<br />and connect the workflow to the enterprise systems you already run.</sub>

<img src="https://img.shields.io/badge/license-Apache--2.0-blue?style=for-the-badge" alt="Apache-2.0" />
<img src="https://img.shields.io/badge/self--hosted-yes-2ea043?style=for-the-badge" alt="Self-hosted" />
<img src="https://img.shields.io/badge/python-3.11%2B-3776ab?style=for-the-badge" alt="Python 3.11+" />
<img src="https://img.shields.io/badge/status-0.1.0%20in%20progress-f59e0b?style=for-the-badge" alt="0.1.0 in progress" />

<sub><a href="README.zh-CN.md">简体中文</a> · English</sub>

<br /><br />

[Design](#design-in-one-page) · [Architecture](#architecture) · [Workflow](#pillar-1--design-the-workflow-visually) · [RAG](#pillar-2--ground-answers-in-your-documentation) · [Integrate](#pillar-3--connect-enterprise-systems-through-tools) · [Quick start](#quick-start) · [Deploy](#configuration-and-deployment) · [FAQ](#faq) · [Roadmap](#status-and-roadmap)

</div>

## The problem

Enterprises do not lack AI models. They lack a way to **shape the customer
conversation without writing code** and to **ground answers in their own
documentation**. Three groups of people need to work together:

- **Operations staff** need to design and change the workflow — routing, knowledge,
  tone, escalation — without filing a software ticket.
- **Support teams** need answers that cite the company's own documentation instead
  of inventing policy or relying on a generic model.
- **IT and platform teams** need the workflow to sit next to the systems they
  already run (identity provider, CRM, order system, ticketing, documentation)
  instead of replacing them.

Bridge-Agents is built around two product pillars — a visual workflow editor and
first-class retrieval — plus the integrations that put them to work.

## Design in one page

| 🧩 **Visual workflows** | 📚 **RAG by default** | 🔌 **It integrates, not replaces** |
|---|---|---|
| The conversation flow is saved data, not code. Operators drag nodes onto a canvas, connect them, and configure them in plain-language forms; a flow that cannot compile is rejected before it goes live. Saving hot-swaps the new workflow into the runtime — no redeploy. | Documentation is a first-class part of the product: upload support articles or point at an existing docs folder, retrieve heading-aware chunks with hybrid search, and let the agent answer with `[1]`, `[2]` citations. The demo ships 10 indexed articles so it works offline. | Identity comes from your IdP, actions go through typed **tools** bound in the workflow, data lives in your database, and the GUI is static files behind your nginx. Self-hosted, SQLite by default, no vendor lock-in. |

## Architecture

<img src="docs/assets/architecture.svg" alt="Bridge-Agents architecture: channels connect to the runtime, whose visual flow, knowledge base and tools connect to existing enterprise systems" width="100%" />

The product is deliberately split into four planes:

- **Control plane** — the visual graph, node settings and the support prompt,
  owned by operators, validated on save and hot-swapped into the runtime.
- **Knowledge plane** — document ingestion, heading-aware chunking, the hybrid
  index, the retrieval node and citation rendering.
- **Delivery plane** — model calls, tool execution, channels and the support desk
  ([`packages/bridge_agents`](packages/bridge_agents)).
- **Integration plane** — typed tools that adapt enterprise APIs, identity, database
  and static GUI deployment, so the product fits an existing stack.

## Pillar 1 — Design the workflow visually

The starting point is that **a flow is configuration, not a deploy**. Operators
work in the Studio (`/admin/studio`), not in the codebase.

### The flow is a validated graph

A conversation is a graph of nodes; the canvas edits the same JSON configuration
the runtime compiles.

| Node | What an operator uses it for |
|---|---|
| `system` | Set the assistant's role prompt |
| `retrieval` | Ground answers in the knowledge base (top-k, score threshold) |
| `agent` | Generate the customer-facing reply |
| `tools` | Let the agent call registered system tools |
| `custom` | Add an extra model step (translation, classification, rewrite) |
| `sanitize` | Optional guardrail: mask banned words or run provider moderation |
| `review` | Optional guardrail: review, retry or rewrite before delivery |
| `start` / `end` | Entry and exit |

Operators add nodes from a palette, connect them (including condition handles
such as `respond`, `tool_call`, `pass`, `block`), drag/auto-layout them and edit
fields in a plain-language inspector. Advanced users get a JSON editor for the
same configuration.

**Validated by construction:** the graph is compiled before it is saved. A broken
reference, missing agent role or unroutable edge is rejected — the previous flow
keeps running. Saving hot-swaps the new graph; no redeploy, no restart.

### Studio covers the rest of the operator job

- **Knowledge** — upload documents, reindex, search-preview the retrieval index;
  point `DOCS_DIR` at an existing documentation folder.
- **Model** — pick a provider preset (OpenAI, Azure OpenAI and 13 more) and an
  endpoint; the available models are fetched from the provider and shown as a
  dropdown (Azure lists deployments). Preset endpoints are verified against the
  vendors' docs in [docs/providers.md](docs/providers.md). Save several validated
  API profiles and choose which one the whole system uses from the list on the
  right; API keys are stored encrypted and never returned.
- **Support prompt** — the support prompt is the flow's `system` node, edited in the
  flow editor (not in Settings); the Settings page only manages model APIs.
- **Roles and language** — support staff and admins edit; customers only chat.
  The whole Studio and customer UI ship in English and 简体中文, light/dark, and
  responsive layouts.

Optional `sanitize` / `review` guardrail nodes are available on the canvas when a
deployment wants extra checks; they are not required by the default flow.

### What still needs a developer (today)

New *system capabilities* — a new CRM connector, a custom node kind, a new
channel — are Python extensions registered in the server. Operators then bind and
configure them in the flow. Making those integrations declarative
(OpenAPI/HTTP tool definitions, custom nodes as plugins) is on the roadmap, so
more of the integration work can move from IT to operations.

## Pillar 2 — Ground answers in your documentation

Retrieval is a first-class part of the product, not an add-on. Upload support
articles, point `DOCS_DIR` at an existing documentation folder, and the
`retrieval` node feeds cited passages into the agent.

<img src="docs/assets/rag-flow.svg" alt="RAG pipeline: documentation is split into heading-aware chunks, indexed with vectors and keywords, retrieved by the retrieval node and passed to the agent with citations" width="100%" />

### Knowledge in the Studio

- **Upload and edit** — add Markdown/text files, reindex, search-preview the index,
  open any document's full text and delete stale articles.
- **Heading-aware chunks** — 900-character chunks with 120-character overlap;
  headings stay with their section so citations are readable.
- **Hybrid retrieval** — vector similarity (60%) plus lexical matching (40%);
  `RAG_TOP_K` and `RAG_MIN_SCORE` are configurable per deployment and per
  `retrieval` node.
- **Citations** — retrieved passages are passed with citation markers; the shipped
  prompt asks the agent to cite `[1]`, `[2]` and to say when the docs do not cover
  a question.
- **Embeddings** — deterministic offline hash embedder by default; set
  `RAG_EMBEDDER=openai` to use any `/v1/embeddings` endpoint.

### Retrieval in the workflow

- Drag the `retrieval` node before the `agent` node (or wherever it makes sense)
  and configure top-k / score threshold in the inspector.
- The node retrieves passages for the latest customer message and injects them
  into the model context; citations survive into the reply.
- Prefer a tool? The bundled `search_docs` tool exposes the same index to the
  agent.

### Demo knowledge base

The demo ships with 10 fictional support articles (accounts, billing, refunds,
desktop sync, sign-in/SSO, API/webhooks, security, SLAs) — 64 indexed chunks — so
the retrieval path works offline without uploading anything.

## Pillar 3 — Connect enterprise systems through tools

Bridge-Agents is a layer *next to* the systems an enterprise already runs, not a
replacement for them. The integration design is **tool-based**: every enterprise
capability is wrapped as a typed tool, the workflow's `tools` node binds the tools
that are allowed in that flow, and the agent calls them when a conversation needs
real system data or an action.

<img src="docs/assets/tools-integration.svg" alt="Integration through tools: enterprise systems are exposed as typed tool adapters, bound by the workflow's tools node and called by the agent; results return to the model and transcript" width="100%" />

### How a tool integration works

1. **Register the tool** — a bundled adapter or a small Python extension exposes
   one enterprise capability with a name, a description for the model, typed
   arguments, credentials from the environment and a read/write scope.
2. **Bind it in the flow** — the operator opens the `tools` node inspector and
   selects which registered tools this workflow may use. The graph must route
   `tool_call` for the agent to be able to call them.
3. **Call it during the conversation** — the agent sees only the bound tools and
   decides when to call one; arguments are validated against the tool schema.
4. **Return the result** — the tool result goes back into the model context and is
   streamed to the transcript, so the final answer can combine live system data
   with retrieved documentation.

### Tool design principles

- **Narrow and typed** — one tool per business operation (`order_status`,
  `create_ticket`, `customer_lookup`) with a JSON schema the model must follow.
- **Read-only by default** — read tools are the normal starting point; write tools
  are explicit and only exposed where the flow allows them.
- **The system stays the source of truth** — tools call the existing API; the
  runtime does not copy or rewrite enterprise data unless a write tool is invoked.
- **Credentials stay server-side** — tool secrets live in the environment, never
  in the flow JSON or the browser.
- **Visible calls** — tool calls and results are streamed and stored in the
  transcript, so support staff can see what the agent actually did.

### What ships today

Bundled tools: `get_current_time`, `calculate` and `search_docs` (the RAG tool).
The admin API lists the tool catalog, the flow inspector binds tools per node, and
tool calls/results stream to the transcript. New enterprise APIs are currently
added as small Python tools; **declarative HTTP/OpenAPI tools** are the next step so
simple read/write endpoints can be registered without writing Python.

| Surface | How it connects | Status |
|---|---|---|
| Identity | Reuse an existing IdP: HS256 (local), RS256 PEM or external OIDC JWKS; three roles (customer, support, admin) | Shipped; browser OIDC login flow next |
| Knowledge | Point `DOCS_DIR` at an existing docs folder or upload in Studio; hash embedder offline or any `/v1/embeddings` endpoint | Shipped |
| System APIs / tools | The workflow's `tools` node binds registered tools; each tool wraps one enterprise API with typed arguments, and results return to the model and transcript | Shipped for Python-registered tools; declarative HTTP/OpenAPI tools next |
| Tool catalog | Bundled `get_current_time` / `calculate` / `search_docs` plus Python-registered adapters; the admin API lists them for the flow inspector | Shipped |
| Channels | Same-origin web chat (static GUI behind your nginx) and a signed Lark channel with two-way human replies | Shipped; Slack and a generic webhook API next |
| Storage | SQLite by default; PostgreSQL / MySQL extras; uploads on disk or a mounted volume | Shipped |
| Deployment | pip/uv packages (`bridge-agents`, `bridge-agents-server`), systemd unit, nginx reverse proxy, Docker Compose; the GUI is a static artifact | Shipped |
| API contract | REST + WebSocket under `/api/v1` and `/ws`; `/api/v1/meta` version handshake; `/health` | Shipped |
| Configuration | TOML + environment variables with standard precedence; secrets only in env or encrypted runtime settings | Shipped |
| Extensibility | Protocols for token verifiers, chat models (OpenAI-compatible), moderation adapters, channels; `create_app()` and `AgentRuntime` | Shipped |

### Non-invasive by design

- **Your systems stay the source of truth.** The runtime reads through tools and
  never rewrites enterprise data unless an operator's tool explicitly does so.
  Read-only connectors are the normal starting point.
- **No data leaves your infrastructure in demo/offline mode.** The default model,
  embedder and channels run locally; external providers are opt-in.
- **No new gateway required.** Deploy the static GUI into the existing nginx and
  proxy `/api`/`/ws` to the Python service on a private port. Same origin, no CORS.
- **Version compatibility is explicit.** The GUI reads `/api/v1/meta`; server and
  GUI can be released independently as long as `min_web_version` is respected.
- **Secrets stay out of the UI and the database by default.** Keys live in the
  environment, or encrypted at rest when saved through Studio → Settings.

## One story, three pillars

1. An operator opens Studio, drags a `retrieval` node before the agent, uploads
   the support docs and saves. The graph is validated and hot-swapped — no deploy.
   *(Workflow)*
2. A customer asks *"How do I activate Widget Pro?"* Retrieval returns the
   activation passage and the agent answers with a `[1]` citation. *(RAG)*
3. The customer asks for order status. The `tools` node calls the existing order
   system and the answer combines the tool result with the policy citation.
   *(Workflow + integration)*
4. Identity comes from the company IdP, conversations are stored in the company
   database, and the GUI is served by the company nginx. *(Integrate)*

## Quick start

### One command (local, no Docker)

Requirements: Python 3.11, [uv](https://github.com/astral-sh/uv) and Node.js for
the first web build only.

```bash
git clone <repository-url> bridge-agents
cd bridge-agents
uv sync
uv run bridge-agents demo
```

The first run creates `.env` from `.env.example`, builds the GUI and starts the
deterministic mock model plus the API. One process serves both:

- **http://localhost:8000/** — customer chat
- **http://localhost:8000/admin** — support desk; Studio at `/admin/studio`
- **http://localhost:8000/health** — health check

`bridge-agents demo --port 18000 --mock-port 8002`, `--no-build`, `make demo`,
`make help` and `bridge-agents doctor` cover the common variations.

### One command (Docker)

```bash
docker compose up --build
```

Customer UI at **http://localhost/**, staff portal at **http://localhost/admin**,
API health at **http://localhost:8000/health**. The stack runs offline with a mock
model and stores conversations on a named volume.

### Manual development

```bash
uv sync
cp .env.example .env          # ALLOW_DEV_LOGIN=true for the demo login
uv run bridge-agents init-db
uv run bridge-agents serve --reload       # API + built UI on :8000
npm --prefix web install && npm --prefix web run dev   # Vite on :5173
```

## Configuration and deployment

Configuration precedence is **CLI arguments > environment variables > `.env` >
`bridge-agents.toml` > defaults**. `bridge-agents init` generates a starter TOML
file and a secrets-only `.env`; `bridge-agents config check` validates the
effective configuration (it fails on production-unsafe defaults).
See [.env.example](.env.example), [bridge-agents.toml.example](bridge-agents.toml.example)
and [docs/architecture.md](docs/architecture.md) for every setting.

Deployment keeps the GUI and Python separate:

| Artifact | Contents |
|---|---|
| `bridge-agents` | core runtime (no server dependencies) |
| `bridge-agents-server` | FastAPI server, database models, CLI; pins the matching core version |
| `bridge-agents-web-<version>.tar.gz` | built static GUI for nginx/CDN (never inside the wheel) |

```bash
pip install --find-links dist "bridge-agents-server[postgres]"
bridge-agents init --config /etc/bridge-agents/bridge-agents.toml \
    --env-file /etc/bridge-agents/bridge-agents.env
bridge-agents init-db --config /etc/bridge-agents/bridge-agents.toml
bridge-agents config check --config /etc/bridge-agents/bridge-agents.toml
bridge-agents serve --config /etc/bridge-agents/bridge-agents.toml
```

Copy [deploy/bridge-agents.service](deploy/bridge-agents.service) and
[deploy/nginx.conf](deploy/nginx.conf) and follow the production checklist in
[deploy/README.md](deploy/README.md). `make release` builds both wheels and the
versioned web archive.

## Packages and embedding

Two Python distributions plus the static GUI:

- **`bridge-agents`** — workflow pipeline, graph validation, retrieval, tool
  registry, auth verifiers, moderation adapters, injection guard, rate limiter,
  embeddable `AgentRuntime` and testing fakes.
- **`bridge-agents-server`** — FastAPI app, database models and CLI. Extras:
  `[postgres]`, `[mysql]`.
- **Web UI** — React/Vite in `web/`, released as a static archive.

```python
from bridge_agents.runtime import AgentRuntime

async with AgentRuntime(llm=my_chat_model) as runtime:
    answer = await runtime.reply("How do I activate Widget Pro?")
    async for event in runtime.stream("Can I get a refund?"):
        ...
```

Mount the server into an existing FastAPI service if you already own the HTTP
layer:

```python
from app.main import create_app

app.mount("/bridge-agents", create_app())
```

`bridge_agents.testing` ships deterministic `FakeChatModel` / `FakeModerator`
doubles. Details: [packages/bridge_agents/README.md](packages/bridge_agents/README.md).

## Where it fits

| | Bridge-Agents | Typical low-code bot builders |
|---|---|---|
| Visual workflow editing | ✅ validated drag-and-drop graph, hot-swapped | yes, but often closed and code-bound |
| Grounded answers with citations | ✅ built-in RAG with upload/reindex and citations | usually an add-on or prompt-only |
| Fits an enterprise stack | ✅ typed tools for CRM/orders/tickets, IdP, existing docs, database, own nginx | often a closed SaaS platform |
| Human handoff stops the AI | ✅ takeover cancels the pending reply | depends on the product |
| Self-hosted and embeddable | ✅ pip packages + static GUI + one-command demo | usually not |

Low-code platforms are great for prototypes. Bridge-Agents is for teams whose
customer replies carry commercial or legal weight — where "the bot said it" is
not an acceptable answer.

## Status and roadmap

**0.1.0 is in progress.** What is real today:

| Shipped | Next |
|---|---|
| Visual flow editor with validation, node inspector, auto layout and JSON fallback | Flow version history and approvals |
| RAG: heading-aware chunks, hybrid retrieval, citations, upload/reindex and full-text preview | Reranking and per-tenant knowledge bases |
| Studio: knowledge panel, 15 model provider presets, saved and validated API profiles | Browser OIDC login flow (JWKS/RS256 verification already works) |
| Tool-based enterprise integration: tool catalog, `tools` node binding, tool-call streaming | Declarative HTTP/OpenAPI tools for new enterprise APIs |
| Customer demo with nickname entry, conversation history, attachments and streaming | PyPI publishing, container images and release automation |
| Support desk with takeover, AI/human labels and image transcript | Slack adapter, generic webhook API and an embeddable widget |
| Support desk with takeover, AI/human labels and image transcript | Database migrations (Alembic) and a `db upgrade` command |
| Customer demo with nickname entry, conversation history and attachments | Kubernetes/Helm deployment option |
| Lark channel, bilingual/responsive UI, light/dark themes | — |
| Packaging, CLI, TOML configuration, static GUI release, systemd/nginx templates | — |
| 336 offline tests, 91% coverage, ruff and sanitisation gates | — |

## FAQ

**Can a non-programmer really change the AI flow?**
Yes for the conversation behaviour: routing, prompt, knowledge, tools, model
APIs and escalation are editable in Studio, validated on save and applied without
redeploying. New *integrations* (a new system API connector, a custom node kind)
currently need a small Python extension; declarative HTTP tools are next.

**How are answers grounded in my documentation?**
Upload Markdown/text files in Studio or point `DOCS_DIR` at an existing folder.
The `retrieval` node uses heading-aware chunks and hybrid search, and the answer
cites the passages it used as `[1]`, `[2]`. Reindex from Studio after changing the
documents; the demo works offline with 10 seeded articles.

**Can I add guardrails?**
Yes, optionally: the canvas includes `sanitize` and `review` nodes for banned
words, provider moderation or an LLM policy check. They are not required by the
default flow.

**Does it need a specific model vendor?**
No. Any OpenAI-compatible endpoint works; Azure OpenAI has a native client and 13
more provider presets ship in Studio. Anthropic is supported through a compatible
gateway.

**Does it replace my CRM / order system / IdP?**
No. Existing systems are exposed as typed **tools**; the workflow binds the tools it
allows, the agent calls them when needed, and results return to the conversation.
Your IdP, documentation, database and web server are reused. Read-only tools are
the normal starting point.

**Do I need Docker or an API key to try it?**
No. `uv sync && uv run bridge-agents demo` runs offline with a deterministic mock
model; Docker Compose is an alternative.

**Is it production-ready?**
0.1.0 is the first release. The runtime and deployment path are usable; the
roadmap above lists the audit/approval, OIDC, migration and publishing work that a
regulated production rollout should wait for. See
[deploy/README.md](deploy/README.md).

**Where are the entry points?**
`/` is the customer chat (no staff navigation); `/admin` is the staff portal with
the support desk, and `/admin/studio` is the control plane (flow, knowledge,
settings).

## Security and privacy

No credentials or customer data are shipped with the repository. The demo login
is disabled in production, roles are separated, provider keys stay in the
environment (or encrypted runtime settings), workflow changes are validated before
activation, and provider URLs can be restricted with an allow-list. See
[SECURITY.md](SECURITY.md) for reporting.

## Documentation

- [docs/architecture.md](docs/architecture.md) — API, runtime nodes, configuration, quality gates
- [docs/design-decisions.md](docs/design-decisions.md) — why the product works this way
- [deploy/README.md](deploy/README.md) — production topology and checklist
- [packages/bridge_agents/README.md](packages/bridge_agents/README.md) — library usage
- [CHANGELOG.md](CHANGELOG.md) — recent changes
- [docs/releasing.md](docs/releasing.md) — release checklist, PyPI/GHCR publishing and rollback
- [docs/providers.md](docs/providers.md) — verified provider endpoints and model-discovery notes

## License

Apache-2.0. See [LICENSE](LICENSE).

## Provenance

Bridge-Agents is an independent, sanitized rewrite of a customer-conversation
runtime the author built for an internal production system. It is published with
written permission. No proprietary code, data, credentials or customer
information is included.
