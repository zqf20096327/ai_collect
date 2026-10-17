# TrustPlane

**Has your agent earned the right to do this work?**

TrustPlane is the authority layer above AI coding agents.
It classifies risk, authorizes runtimes, scores trust and
produces a tamper-evident audit trail for every governed
task across every runtime.

Agent runtimes answer: can the agent do the work?
TrustPlane answers: has the agent earned authority to do it?

---

## Try it in 60 seconds

Requires Node.js 18+ and PostgreSQL.

```bash
git clone https://github.com/rayyagari2-create/agentic-workforce-framework
cd agentic-workforce-framework
cp .env.example .env
npm install
npm run demo:setup
npm run demo
```

The demo classifies 5 tasks by risk, fires an approval gate
on high-risk items, scores agent performance on D1-D4
dimensions and writes a hash-chained audit log.

---

## Runtime authorization demo

TrustPlane blocks, authorizes or supervises a runtime based
on earned trust, not capability.

The Sprint 3 authorization demo is deterministic and
example-driven. Production runtime authorization uses
the same schemas and audit shape.

```bash
npm run authorize:blocked
npm run authorize:authorized
npm run authorize:supervised
```

Example output:

```
Decision:          BLOCKED
Runtime:           codex
Task class:        db_migration
Risk lane:         critical
Required tier:     HIGH
Current tier:      PROVISIONAL

Reason:
Codex has not earned sufficient trust for critical lane
database migrations in this workspace.

Recommended:       claude_code
```

---

## How it works

Every task goes through five stages:

1. Classify: task class and risk lane from five dimensions
2. Authorize: check runtime trust tier against required tier
3. Execute: runtime runs under approved scope and controls
4. Score: D1-D4 trust scoring from real artifacts
5. Verify: hash-chained audit trail verified end to end

Trust tiers: PROVISIONAL, RESTRICTED, STANDARD, HIGH
Scoring dimensions: D1 Correctness, D2 Observability,
                    D3 Policy, D4 Recurrence

---

## Sprint 3: Trust-Based Runtime Authorization

Sprint 3 introduces the named capability: **Trust-Based Runtime Authorization.**

Not routing. Authorization.

AWF evaluates agent and runtime behavior across D1-D4 scoring dimensions,
then assigns a task-specific trust tier that determines whether the runtime
is authorized, supervised or blocked.

| Runtime | UI refactor | DB migration | Security fix |
|---|---|---|---|
| Cursor | HIGH | PROVISIONAL | PROVISIONAL |
| Codex | STANDARD | PROVISIONAL | RESTRICTED |
| Claude Code | STANDARD | STANDARD | HIGH |

Sprint 3 public deliverables: four new schemas, nine worked examples,
four architecture docs, and the authorize-task CLI demo above.

Sprint 2 proved cross-runtime governance across Claude Code and Codex
from one control plane. Sanitized replay in
[examples/cross-runtime/](examples/cross-runtime/).

---

## What is in this repo

```
schemas/v1/              JSON schemas for all governance artifacts
examples/                Worked examples for authorization decisions,
                         trust profiles and risk profiles
docs/                    Architecture, D1-D4 scoring, task risk
                         profiling, execution substrates
agents/                  Reference agent instruction files
calibration/             D1-D4 rubric and scoring anchors
hooks/                   OS-level hook enforcement examples
database/migrations/     Postgres governance schema and audit log
services/                Audit service, scorer, governance engine
```

---

## What TrustPlane is not

TrustPlane does not spawn agents, generate code, route
subagents or capture tool-call telemetry. Those belong to
execution substrates like Claude Code, Codex, Cursor, Devin
and Maggy.

TrustPlane sits above them and decides who is authorized
to run what and under which controls.

See [docs/execution-substrates.md](docs/execution-substrates.md)
for the full three-layer architecture.

---

## Evidence

From the private reference implementation:

- 120+ governed sessions scored
- Zero successful hook bypasses
- Claude Code and Codex adapters proven at Gate 3
- Cross-runtime demo verified. One audit chain, two runtimes

Metrics are self-reported and not independently audited.

---

## Schemas

```
AgentTaskManifest              Task contract before dispatch
QAVerdict                      Structured verdict with per-criterion evidence
FailureRecord                  17-class failure taxonomy with recurrence
TrustScore                     D1-D4 session score and trust tier
TrustSubject                   Accountable identity AWF scores
TaskRiskProfile                5-dimension risk scoring
TrustCapabilityProfile         Earned trust per runtime per task class
RuntimeAuthorizationDecision   Authorization output with audit event
AuditEvent                     Canonical per-event audit shape with user_id
```

All schemas in [schemas/v1/](schemas/v1/) are AJV Draft 2020-12 compatible.

---

## Install

```bash
npx agentic-workforce-framework@latest init
```

Scaffolds AWF governance into any repo.

---

## Contributing

Schema extensions, case studies and documentation
corrections welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

MIT. See [LICENSE](LICENSE).

*Originated by Ramesh Ayyagari, 2026*