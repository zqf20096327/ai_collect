# Project AEGIS — Core

[![CI](https://github.com/gravion-ux/aegis/actions/workflows/ci.yml/badge.svg)](https://github.com/gravion-ux/aegis/actions/workflows/ci.yml)

![Demo](docs/demo.png)

*The AEGIS multi-agent core in action.*

Project AEGIS is a multi-agent AI system built around a rule that most
agent frameworks treat as an afterthought: **the system must be safe and
correct before it is clever.** Every capability an agent can reach is
declared, scoped, limited, audited, and recoverable.

This repository is the working core. It runs on Node.js 18+ with **zero
runtime dependencies**.

> **Status: Experimental.** Phase 0–3 complete. **315 automated tests**, and CI runs
> the suite on Node 18, 20 and 22. The HTTP provider is proven against a
> local mock server; it has **not** been pointed at a paid model, because no
> credential is available in this environment. See
> [Known limitations](#known-limitations).

## Features

### What Phase 2 added

Phase 0–1 proved the machinery: task lifecycle, persistent storage, an
append-only audit log, structured logs, redaction, and a CLI. Phase 2 adds
the parts that make it an agent system rather than a task tracker.

| area | what it does | where |
| --- | --- | --- |
| **Persistent memory** | schema-validated records, project/task scoping, dedup with merge, TTL retention, checkpoints, and context assembly that keeps verified facts separate from assumptions and open questions | `aegis/memory.js` |
| **Provider abstraction** | a deterministic offline provider and a generic HTTP provider behind one interface, with a router that refuses to silently substitute a paid model for a free one | `aegis/providers/` |
| **Permission-controlled tools** | default-deny registry: per-task allowlist, risk ceiling, timeout, output cap, audit events | `aegis/tools/registry.js` |
| **Resource manager** | per-task and global budgets, preflight cost check, pricing reported as `unknown` rather than invented | `aegis/usage.js` |
| **Specialist agents** | `review`, `memory`, `research`, `router` — deterministic, offline, explainable | `aegis/specialists.js` |
| **Orchestrator** | runs an agent under its declared limits, validates its output, retries only on a retryable provider error, and logs every step | `aegis/orchestrator.js` |
| **Cancellation & recovery** | cooperative cancellation between steps, checkpoints, idempotency, and resume that survives a real process restart | `aegis/recovery.js` |
| **Typed config** | validated config with credential-shaped fields stripped on read | `aegis/config.js` |

### What Phase 3 added — the Chief

Phase 2's Orchestrator runs one task. Phase 3 adds the layer above it:
a **chief** that takes a whole goal, splits it into a dependency graph
of subtasks, delegates each one to a specialist, and refuses to call
the mission done until a separate verification pass agrees.

| area | what it does | where |
| --- | --- | --- |
| **Specialist cards** | one JSON data file per specialist: role, purpose, the actions it may perform, the tools it may touch, and the boundary tags it may work inside. A card may narrow the orchestrator manifest, never widen it — the chief checks this at startup | `aegis/cards/`, `aegis/cards.js` |
| **Decomposition** | a mission (goal + granted scopes + work items) is routed item-by-item to specialists and built into a task graph; dependencies are explicit (`needs`), data flow is explicit (`inputFrom`), cycles and unknown dependencies refuse the mission before anything runs | `aegis/chief.js` |
| **Scope enforcement in code** | every subtask is checked twice — at decomposition and again at dispatch: the action must be on the specialist's card, the boundary tag must be on the card, and the tag must be inside the mission's granted scopes. A violation refuses the mission (or the subtask) with `OUT_OF_SCOPE` / `ACTION_NOT_ALLOWED`, and the refusal is audited | `aegis/chief.js` (`Scope`, `Chief._enforce`) |
| **Dispatch** | subtasks run in topological order through the existing Orchestrator, so manifest allowlists, budgets, output-schema validation and audit apply unchanged; a subtask whose dependencies did not all succeed is SKIPPED, never run on partial inputs | `aegis/chief.js` |
| **Verification pass** | the mission is `DONE` only when an independent pass confirms every subtask is accounted for, succeeded, carries evidence and a non-null output, and stayed inside the granted scopes. Anything else is `NEEDS_REVIEW` | `aegis/chief.js` (`Chief.verify`) |
| **Summariser specialist** | a sixth card-carrying specialist: digests the labelled outputs of earlier subtasks (first line + word count per section), deterministically | `aegis/specialists.js` |

Run the demo — four subtasks, four specialists, one verified report,
plus the refusal path with a scope grant removed:

```bash
npm run demo:chief
```

Decomposition is deterministic and rule-based, like the Phase 1/2
agents: the same mission always produces the same graph. There is no
LLM call in the chief layer, and no specialist gains a capability from
being asked nicely — capability comes only from its card and the
manifest under it.
## Requirements

- **Node.js 18 or newer** (`engines: "node": ">=18.0.0"` in
  `package.json`; CI runs the suite on Node 18, 20 and 22).
- **Zero runtime dependencies** — there is nothing to install beyond
  cloning the repository; the test suite uses Node's built-in
  `node --test` runner (`npm test`).
- **No credentials needed.** The default provider is deterministic and
  offline. An HTTP provider is optional and configured only through
  the `AEGIS_LLM_URL` and `AEGIS_LLM_AUTH_HEADER` environment
  variables.

## Quick start

```bash
# run the full suite (315 tests)
npm test

# explore the CLI
node aegis/cli.js --help

# create and run a task
node aegis/cli.js tasks create --title "audit headers" --role classifier \
  --goal "Check HSTS and CSP on the staging host"
node aegis/cli.js tasks run <id-from-previous>
node aegis/cli.js tasks show <id>

# Phase 2 surface
node aegis/cli.js agents list        # the 10 registered agents
node aegis/cli.js tools list          # the default-deny toolset
node aegis/cli.js providers smoke     # offline provider, no credentials needed
node aegis/cli.js usage               # budget summary
node aegis/cli.js security scope      # the active scope boundaries
```

## How it fits together

```
task  ──▶ orchestrator ──▶ manifest lookup ──▶ agent handler
             │                   │                    │
             │                   │                    ├─▶ tool registry (default-deny)
             │                   │                    └─▶ memory (redacted on write)
             │                   │
             │                   └── declared limits: iterations, wall clock, depth
             │
             ├─▶ budget (preflight cost check)
             ├─▶ audit log (append-only, every step)
             └─▶ checkpoint (resume after a crash)
```

An agent role has to be declared in **both** the manifest and the runtime
registry. The manifest is derived from the registry, so a role can never be
declared without an implementation, or registered without a declaration.
Any role without an explicit manifest entry gets a deliberately
*restrictive* fallback: no tools, one iteration, no delegation.

## Task lifecycle

```
QUEUED ──▶ READY ──▶ RUNNING ──▶ SUCCEEDED
             │          │   │
             │          │   ├─▶ FAILED ──▶ RETRYING ──▶ RUNNING
             │          │   ├─▶ CANCELLED
             │          │   └─▶ BLOCKED
             │          └─▶ WAITING_FOR_APPROVAL
             ├─▶ CANCELLED
             └─▶ BLOCKED
```

Every transition is validated against the canonical state machine in
`aegis/states.js`. `RETRYING` is reachable only from `FAILED` — a task
cannot spin without ever failing — and terminal states are sinks.

## Security boundaries

These are design constraints, not aspirations. Each one has a test.

- **Tools are default-deny.** An unregistered tool throws. A call outside
  the task's `allowedTools` is denied and audited. Every tool declares a
  risk level (`read` < `mutate` < `external` < `destructive`), and a task
  may only reach as far as its own `maxRiskLevel`.
- **No unrestricted shell.** There is no shell tool in the registry.
- **The filesystem tool is rooted.** `fs.read` refuses any path outside an
  explicit `allowedRoots` list.
- **The HTTP tool is loopback-only.** `http.get` rejects any non-loopback
  host, so it cannot be pointed at a third party.
- **Paid providers are opt-in.** A model whose name looks paid is refused
  with a `ProviderError` unless `provider.allowPaid` is explicitly turned
  on. It is never silently replaced with the offline provider, because a
  silent substitution produces output that looks like a model answer and
  is not one.
- **No credentials in code, config, logs, or commits.** The provider
  endpoint comes from `AEGIS_LLM_URL`; an optional auth header comes from
  `AEGIS_LLM_AUTH_HEADER`. `stripSecrets()` removes credential-shaped
  config fields on read, `aegis.config.json` is gitignored, and CI runs
  `scripts/scan-secrets.js` over the tree.
- **Memory is redacted on write.** A secret in a memory record is scrubbed
  before it reaches disk, not after.
- **The audit log is append-only** and HMAC-chained; the runtime exposes
  `append` and `read` only.
- **Failure is isolated.** A corrupt memory file or storage index is
  recovered cleanly and cannot take down a working task.
- **The resume path is tested across a process boundary.** Two real Node
  child processes run against the same state directory; the test asserts
  that no step runs twice.

## Tests

```bash
npm test              # 315 tests, the full suite
npm run test:phase1   # the Phase 1 compatibility suite
npm run scan:secrets  # credential-shaped string scan
```

The suite covers the state machine, storage round-trip, audit chain,
redaction patterns, deterministic and specialist agents, the memory
schema, provider routing and paid-provider refusal, tool permissions,
budgets, the orchestrator, cancellation, checkpoint/resume, the chief (decomposition, dependency ordering, scope refusal, audit trail, verification), the CLI, the
Phase 1 compatibility surface, and adversarial cases — invalid
transitions, corrupted index, oversized inputs, a missing memory key, and
a manifest that has drifted from the registry.

## Configuration

Copy `aegis.config.example.json` to `aegis.config.json` and edit it. The
example states in a comment that it must never contain a key.

```bash
cp aegis.config.example.json aegis.config.json
```

The default configuration uses the offline provider and enables no paid
provider. Budgets, runtime limits, and memory retention are all optional
and all `null` by default, which means "no limit".

## Known limitations

- **No real LLM has been verified.** The HTTP provider is exercised against
  a local mock server only. Point `AEGIS_LLM_URL` at a local Ollama or
  LM Studio endpoint and run `npm run smoke` to change that.
- **The provider adapter is generic** (HTTP + JSON). Provider-specific
  quirks — Anthropic's `system` block, OpenAI's function-calling format —
  are not encoded.
- **`research` cannot reach the public internet.** It uses the
  loopback-only `http.get` tool by design; a real web-search tool would be
  a separate, explicitly-permissioned capability.
- **The specialists are deterministic rule engines**, not model-backed
  agents. That is what makes Phase 2 testable without a credential, and
  it is not a substitute for model-backed behaviour.

## Design

See [`docs/DESIGN.md`](./docs/DESIGN.md) for the architecture and the list
of items deferred to later phases.
[`PHASE2_IMPLEMENTATION_REPORT.md`](./PHASE2_IMPLEMENTATION_REPORT.md) is
the verified ledger of Phase 2 — what was implemented, what the tests
actually prove, and which defects were found and fixed.

## License

MIT — see [`LICENSE`](./LICENSE).
