# Open Workflow Library

> Open Workflow Library is an open workflow intelligence project for collecting, indexing, validating, repairing, and eventually generating automation workflows across frameworks. It starts with a large n8n workflow collection and is being expanded into a universal workflow knowledge base and tooling layer.

This repository is the working space for that project. It contains the existing n8n workflow collection that seeded the effort, the schemas that define the shared data model, the audit tooling that catalogues the collection, and the early structure of the LLM-usable wiki that the rest of the system will be built on.

---

## Quickstart

Every tool is standard-library Python 3.12+. Nothing is installed globally,
nothing is published, nothing requires n8n on the local machine.

```bash
# Audit the workflow collection (catalog + secret scan, redacts findings).
python tools/audit_workflows.py

# Validate the generated expansion pack (420 templates, structural only).
python tools/validate_generated_pack.py

# Build the unified catalog with deterministic quality scores.
python tools/build_unified_catalog.py

# Keyword + filter search over the unified catalog.
python tools/search_workflows.py --query "lead qualification" --top 5

# Prompt -> IR -> n8n workflow -> static validation (no runtime, no LLM).
python tools/prompt_to_n8n.py "Create a workflow that receives website leads, scores them, saves them to CRM, and alerts Slack."

# Aggregate everything needing human review.
python tools/build_review_queue.py
```

Full demo walkthrough: [`docs/demo.md`](docs/demo.md).

## Honest status

| Capability | Status | Notes |
|---|---|---|
| n8n workflow collection | shipping | ~1,700 source files, plus ~420 generated templates |
| Audit + secret scan | implemented | redacts matches; current run reports 0 findings |
| Catalog + unified search | implemented | deterministic quality score, not a correctness score |
| Schema validation | implemented | jsonschema if available, lightweight required-field check otherwise |
| Duplicate analysis | implemented | exact + title-similarity, surfaces candidates, no auto-dedupe |
| Repair proposals | implemented | emits proposals only; never auto-applied |
| Prompt -> IR | MVP (deterministic, keyword-rule) | not LLM-backed |
| IR -> n8n export | MVP | conservative node whitelist, safe placeholders only |
| Static n8n validation | implemented | structural only; not a behavioural test |
| Learning events | implemented | evidence only; never auto-promoted into curated wiki |
| Human review queue | implemented | nothing is auto-approved |
| Behavioural n8n execution | **not implemented** | no workflow has been imported into n8n by this repo |
| Multi-framework export | **not implemented** | Dify / LangGraph / Make / Zapier are documented, not built |
| LLM-backed prompt-to-workflow | **not implemented** | only the deterministic MVP exists |
| Autonomous self-improvement | **not in scope** | promotion to curated wiki/rules requires human review |
| Production certification | **none** | this is a developer-grade open-source library |

---

## What this is, today

- A collection of ~1,700 n8n workflow files under [`workflows/`](workflows/) and additional automation samples under [`automation/`](automation/), categorised by domain.
- **JSON schemas** for the shared data model:
  - [`schemas/workflow-ir.schema.json`](schemas/workflow-ir.schema.json) — Universal Workflow IR
  - [`schemas/workflow-metadata.schema.json`](schemas/workflow-metadata.schema.json) — catalog metadata
  - [`schemas/repair-proposal.schema.json`](schemas/repair-proposal.schema.json) — human-reviewable repair proposals
  - [`schemas/learning-event.schema.json`](schemas/learning-event.schema.json) — evidence for the self-improvement loop
- A **read-only audit tool**, [`tools/audit_workflows.py`](tools/audit_workflows.py), that catalogues the existing workflows, detects code/webhook usage, redacts secret-like values, and produces both human and machine-readable reports.
- A **catalog** at [`catalog/workflows.index.json`](catalog/workflows.index.json), generated from the audit.
- An **LLM wiki** under [`wiki/`](wiki/) with seed content for patterns, integrations, repair rules, failure cases, and framework guides.
- Documentation under [`docs/`](docs/) describing the architecture, supported-framework status, the planned generator pipeline, the self-improvement loop, and the security model.

## What this is becoming

A universal workflow intelligence layer:

1. **Library** — multi-framework workflow collection in each framework's native format.
2. **Catalog** — structured index across all frameworks.
3. **Universal Workflow IR** — framework-agnostic representation.
4. **Validator + Repair Engine** — schema and behavioural validation, plus *human-reviewed* repair proposals.
5. **Prompt-to-Workflow Generator** — retrieval-grounded generation that uses the catalog and wiki as its knowledge base.
6. **Human-reviewed self-improvement loop** — learning events from validation, generation, and repair flow back into the wiki and repair rules, only via human review.

See [`docs/vision.md`](docs/vision.md) for the longer version and [`docs/architecture.md`](docs/architecture.md) for how the layers fit together.

## How the existing n8n library fits in

n8n is the starting dataset and the first framework with practical tooling support. The audit tool understands n8n workflow files; the catalog currently indexes n8n. None of that locks the project to n8n — the Universal Workflow IR is framework-agnostic by design, and the architecture explicitly accommodates additional importers and exporters.

See [`docs/supported-frameworks.md`](docs/supported-frameworks.md) for the honest, current status of each framework.

## Running the audit

The audit tool is Python and uses the standard library only.

```bash
python tools/audit_workflows.py
```

It produces:

- [`reports/workflow-audit.json`](reports/) — structured audit output
- [`reports/workflow-audit.md`](reports/) — human-readable summary
- [`catalog/workflows.index.json`](catalog/) — indexed catalog conforming to the metadata schema

The tool is **read-only**. It never modifies, moves, or deletes workflow files, and it never prints real secret values — matches against secret-like patterns are replaced with `[REDACTED]` before anything is written to disk. See [`docs/security.md`](docs/security.md) for the details.

## Catalog direction

The catalog is the structured view of the library. For this foundation pass it focuses on detected n8n workflows. Each entry conforms to [`schemas/workflow-metadata.schema.json`](schemas/workflow-metadata.schema.json) and includes detected integrations, trigger type, credential references, code/webhook presence, and a coarse risk level.

Cross-framework catalog coverage will land alongside per-framework importers — see [`docs/supported-frameworks.md`](docs/supported-frameworks.md).

## LLM Wiki direction

The wiki is the **knowledge base** that the rest of the system retrieves from: patterns, integration playbooks, repair rules, failure cases, framework guides. For this pass it ships with hand-written seed entries in each section, structured for both human and LLM consumption. It is not comprehensive — see each section's README for the intended scope.

The wiki is what makes prompt-to-workflow generation grounded rather than hallucinated.

## Generated workflow templates (Expansion Pack V0)

`workflows/generated/open-workflow-library-v0/` contains a deterministic
expansion pack of 420 template workflows across 21 categories. Each template
ships as an n8n `workflow.json`, a Universal IR `workflow.ir.json`, and a
README. The pack is indexed separately in
[`catalog/generated-workflows.index.json`](catalog/generated-workflows.index.json).

These templates are **starting points, not production-tested workflows**. They
contain placeholder credentials and placeholder URLs only — no real keys,
tokens, phone numbers, emails, or private endpoints. Validate with
`tools/validate_generated_pack.py` and review each template before importing.

Details: [`docs/generated-workflows.md`](docs/generated-workflows.md).

## Intelligence Core V1

The repository now ships a small intelligence/tooling layer around the
workflow collection. Every tool is standard-library Python and is documented
under [`docs/ci-and-quality-gates.md`](docs/ci-and-quality-gates.md).

| Tool | What it does |
|---|---|
| `tools/audit_workflows.py` | Read-only audit, secret scan, builds `catalog/workflows.index.json` |
| `tools/validate_generated_pack.py` | Structural validation of the generated expansion pack |
| `tools/build_unified_catalog.py` | Merges the two catalogs into `catalog/unified-workflows.index.json` with a deterministic quality score |
| `tools/search_workflows.py` | CLI search over the unified catalog (keyword + filters) |
| `tools/validate_schemas.py` | Validates schemas + catalogs + sampled IR files (uses `jsonschema` if available, lightweight check otherwise) |
| `tools/analyze_duplicates.py` | Exact-content and title-similarity clusters with `keep` / `review` / `candidate-for-dedupe` recommendations |
| `tools/propose_repairs.py` | Emits human-reviewable repair proposals against `schemas/repair-proposal.schema.json`. Does not modify workflows |
| `tools/prompt_to_ir.py` | Deterministic rule-based **MVP** that turns a prompt into a draft IR. Not an LLM |
| `tools/build_wiki_seed.py` | Writes machine-generated seed notes under `wiki/generated/`. Does not touch the curated wiki |

Honest scope:

- The prompt-to-IR tool is a deterministic keyword-rule MVP. It does not call
  an LLM and does not emit n8n JSON.
- Repair proposals are never applied automatically. Each one carries
  `requiresHumanReview: true` and `status: "proposed"`.
- The generated expansion pack is structurally valid but **not behaviourally
  tested** — no template has been imported and executed.
- Multi-framework export (Dify, LangGraph, Make, Zapier) remains planned. Only
  n8n is implemented.

## Workflow Runtime Proof V1

Workflow Runtime Proof V1 is a deterministic, local proof of the full
intelligence loop:

```
prompt
  -> Universal Workflow IR
  -> n8n workflow.json
  -> static n8n compatibility validation
  -> repair proposal (if needed)
  -> learning event (if useful)
  -> human-reviewable queue
```

It is **static validation only**. No workflow is imported into n8n, no node
is executed, and no external service is called.

| Tool | Role |
|---|---|
| `tools/export_ir_to_n8n.py` | IR JSON → n8n workflow JSON (conservative node whitelist, placeholders only) |
| `tools/validate_n8n_workflow.py` | Static n8n compatibility validator (no runtime) |
| `tools/prompt_to_n8n.py` | Orchestrator: prompt → IR → n8n → validation → proof README |
| `tools/propose_runtime_repair.py` | Emits repair proposals from validation output (no auto-apply) |
| `tools/create_learning_event.py` | Captures learning events from validation/repair (no promotion) |
| `tools/build_review_queue.py` | Aggregates everything needing human review |

Run the proof loop locally:

```bash
python tools/prompt_to_n8n.py "Create a workflow that receives website leads, scores them, saves qualified leads to CRM, and alerts Slack."
python tools/validate_n8n_workflow.py reports/runtime-proof/<slug>/workflow.n8n.json
python tools/build_review_queue.py
```

Honest limitations:

- Static validation only. No runtime execution.
- No external API calls. No real credentials.
- No autonomous self-improvement. Learning events are evidence; promotion
  into the curated wiki or repair rules requires human review.
- Multi-framework export remains planned. Only n8n is implemented.

Details: [`docs/runtime-proof.md`](docs/runtime-proof.md).

## Prompt-to-workflow (roadmap)

The generator pipeline is documented in [`docs/prompt-to-workflow.md`](docs/prompt-to-workflow.md). It is **not implemented** in this pass. The schemas, catalog, and wiki here are the inputs the pipeline will consume.

We will not claim prompt-to-workflow works until it is implemented and validated end-to-end against the catalog.

## Repair engine (roadmap)

The repair engine matches detected failures against the rules in [`wiki/repair-rules/`](wiki/repair-rules/README.md) and emits proposals conforming to [`schemas/repair-proposal.schema.json`](schemas/repair-proposal.schema.json). Proposals are written to `reports/` for review; the engine never mutates workflow files directly.

This is not implemented yet — the schema and rule structure exist so the engine can be built against them.

## Human-reviewed self-improvement (roadmap)

Validation failures and accepted repairs produce learning events ([`schemas/learning-event.schema.json`](schemas/learning-event.schema.json)). Events are *evidence*. They are reviewed by maintainers and may be promoted into wiki entries or repair rules — only after review. See [`docs/self-improvement.md`](docs/self-improvement.md).

There is no autonomous mutation. There will not be.

## Security

Short version: no real credentials in workflow files, redacted secret scanning in the audit tool, idempotent webhooks, careful PII handling, no clinical or regulated-domain claims. Long version: [`docs/security.md`](docs/security.md).

## Repository layout

```
.
├── workflows/             # n8n workflow collection (~1,700 files)
├── automation/            # additional automation samples
├── catalog/               # generated catalog index (workflows.index.json)
├── schemas/               # JSON schemas for IR, metadata, repair, learning
├── wiki/                  # patterns, integrations, repair-rules, failure-cases, framework-guides
├── docs/                  # vision, architecture, supported frameworks, etc.
├── reports/               # generated audit, runtime-proof, and review-queue reports
├── tools/                 # maintainer tooling (audit, catalog, validation, prompt-to-n8n, review queue)
└── scripts/               # legacy helper scripts retained for reference
```

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for workflow contribution standards.

In summary: contributions should pass the audit cleanly (no new entries in `secretFindings`), use credential references rather than embedded values, and — where relevant — add or update a wiki entry that documents *why* the workflow is shaped the way it is. PRs that introduce new framework support should land alongside an importer/exporter under `tools/` and at least one indexed catalog entry.

## Roadmap

Near-term:

- Schema-level validator for IR documents and catalog entries.
- Behavioural validator for n8n workflows (dry-run with mocked integrations).
- First repair-engine implementation, emitting proposals against the rules in [`wiki/repair-rules/`](wiki/repair-rules/README.md).
- Triage of duplicates surfaced by the audit.
- More patterns and integration playbooks in the wiki, extracted from the existing collection.

Medium-term:

- First non-n8n importer (likely Node-RED or Dify) plus an IR round-trip test.
- Prompt-to-workflow MVP for n8n: requirement extraction → catalog/wiki retrieval → IR assembly → validation → export.
- Learning-event capture from validation failures.

Longer-term:

- Additional framework importers/exporters.
- Behavioural validators with realistic mocks for common integrations.
- A reviewable interface for triaging learning events and promoting them into wiki entries.

## License

MIT. See [`LICENSE`](LICENSE).
