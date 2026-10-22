<p align="center"><img src="assets/cover.svg" alt="Fintech Data Engineering Roadmap: from sources to explainable money" width="100%"></p>

# Fintech Data Engineering Roadmap

**From your first SQL query to an explainable fintech warehouse: 100 lessons, 40 foundation exercises, 8 scenario labs, and runnable payment examples.**

[Five-minute experiment](docs/FIRST_WIN.md) · [Start learning](docs/START_HERE.md) · [100-step roadmap](roadmap/README.md) · [Practice](practice/README.md) · [Scenario labs](challenges/README.md) · [Videos](resources/VIDEOS.md) · [Articles](resources/ARTICLES.md)

An open learning path for data engineering, DWH, and financial data. Learn what to study, why it matters, how to implement a principle, and how to detect mistakes. Core themes include exact amounts, change history, repeated delivery, late events, reconciliation, and recovery. A dedicated module covers AI assistants, RAG, Text-to-SQL, and ML features. All repository content is in English.

## Find a missing dollar in five minutes

**A balanced journal can still disagree with the processor. Can you explain why?**

Requires Git and Python 3.12+ with `sqlite3`. No package installation, paid cloud,
or API key is needed.

```bash
git clone https://github.com/antony502189-max/fintech-data-engineering-roadmap.git
cd fintech-data-engineering-roadmap
python -m fintech_lab.quickstart
```

You will see six events inserted, zero inserted on replay, and six duplicates.
The journal balances, but p3 is short by $1.00 and p9 has no internal payment.
Every run starts fresh in memory and writes no files. On Windows, use `py -3`
instead of `python` if needed.

Follow the [first-win walkthrough](docs/FIRST_WIN.md) to explain the amounts and
change one input. If it helps, star the repository to bookmark the learning path.

## Save the full demo and start practicing

Requires Git and Python 3.12+ with `sqlite3`. The lab and all 40 exercises use the standard library. Run from the repository root in PowerShell, Bash, or macOS Terminal.

```bash
python -m fintech_lab --out work/demo
python -m unittest discover -s tests -v
python practice/run.py init E01
python practice/run.py grade E01
```

The final command initially fails because the personal starter contains `TODO`. Implement `solve(data)` in `work/answers/E01.py`, then grade again. On Windows, use `py -3` instead of `python` if needed. No paid cloud or API key is required.

The first clean demo writes `work/demo/warehouse.db` and `report.json` with:

- Six accepted events; replay inserts zero events and reports six duplicates.
- January 1 net cash: USD 12200 and EUR 4900 minor units; January 2: USD −2000.
- Two matches, a p3 discrepancy of −100 USD minor units, and an unexpected external p9.
- A late p3 feature equal to zero before receipt and 2500 afterward.

Reusing the output directory retains the database, so even the first ingestion step then reports duplicates. Choose a new `--out` for a clean experiment. Reconciliation exceptions are intentional.

## What you will build

| Section | Outcome |
|---|---|
| [100 lessons](roadmap/README.md) | Concepts, fintech examples, implementation steps, tasks, failure modes, acceptance checks, and primary sources |
| [40 exercises](practice/README.md) | Forty starters, forty references, ninety verification cases, and a grading CLI |
| [8 scenario labs](challenges/README.md) | Multi-batch rollback, temporal joins, payout allocation, schema migration, bitemporal reports, real backup recovery, a SQL bug hunt, and leakage-safe training data |
| [Payments lab](labs/README.md) | SQLite, synthetic events, exact money, idempotency, journal checks, reconciliation, SCD2, and point-in-time features |
| [Architecture](docs/ARCHITECTURE.md) | Data flow, transaction boundaries, and teaching-model limitations |
| [Resources](resources/README.md) | YouTube, official documentation, and engineering articles from Stripe, Monzo, and Uber |
| [Capstone projects](projects/README.md) | Four project specifications and an acceptance rubric |
| [AI workflow](docs/AI_WORKFLOW.md) | SQL verification, RAG permissions, injection, evaluation, and synthetic inputs |
| [Operations](docs/INCIDENT_RUNBOOKS.md) | Investigation of missing, late, and incorrect monetary events |

## Learning sequence

| Module | Focus | Practice |
|---|---|---|
| 01. Foundations | Python, Git, tests, APIs, containers, time, and money | E01–E04 |
| 02. SQL | Grain, joins, NULL, windows, transactions, indexes, incremental models | E05–E08 |
| 03. Modeling | Layers, facts, dimensions, SCD2, bitemporal history, Vault, metrics | E09–E12 |
| 04. Ingestion | Batch, webhooks, CDC, schema evolution, outbox, replay | E13–E16 |
| 05. Storage | Parquet, partitions, Iceberg, warehouses, Spark, Kafka, event time | E17–E20 |
| 06. Transformation | dbt, DAGs, retries, backfill, publication, CI, migrations | E21–E24 |
| 07. Fintech | Lifecycle, ledger, reconciliation, refunds, FX, credit, fraud | E25–E28 |
| 08. Reliability | Quality, latency, observation, incidents, backups, drills | E29–E32 |
| 09. Platform | IAM, personal data, secrets, encryption, retention, IaC, FinOps | E33–E36 |
| 10. AI and growth | Assistants, RAG, injection, evals, features, portfolio | E37–E40 |

Choose a [learning path](docs/LEARNING_PATHS.md) for beginners, analysts, backend engineers, or experienced data engineers. A first pass may take 200–400 hours; deeper tool integrations and capstones take additional time. Progress is measured by verifiable artifacts, not video hours.

## Verify the repository

```bash
python -m unittest discover -s tests -v
python practice/run.py verify
python challenges/run.py verify
python scripts/check_docs.py
python scripts/check_sql.py
python scripts/check_english.py
```

CI checks Windows and Ubuntu with Python 3.12 and 3.14. `verify` validates references; `grade` checks your solution. Starters intentionally fail before implementation. See [verification evidence](docs/VALIDATION.md) and [GitHub Actions](https://github.com/antony502189-max/fintech-data-engineering-roadmap/actions).

## After the foundation exercises

Work through the [eight scenario labs](challenges/README.md) before your capstone. They include 28 independently specified cases and observable multi-stage results. C07 begins with runnable incorrect SQL: find the monetary bug and repair it. Other starters require an implementation. Initialize with `python challenges/run.py init C01` and test with `python challenges/run.py grade C01`.

## Scope and provenance

All payment data is synthetic. The lab uses simplified signed accounting and does not implement real bank settlement, production Kafka, cloud IAM, or regulatory certification. Platform and AI exercises simulate principles locally; [stack extensions](labs/STACK_EXTENSIONS.md) describe further integration work. Retention examples do not establish legal requirements.

The first edition was authored with AI assistance, with executable examples checked and external resources attributed. [Provenance](docs/PROVENANCE.md) explains the substantive construction steps and maintainer-requested January–October 2026 commit schedule. Scheduled timestamps do not establish when the work actually occurred.

## Help improve the project

Star the repository if it helps you learn or teach. Useful contributions include reproducible bugs, additional edge cases, clearer explanations, and updated sources. Read [CONTRIBUTING](CONTRIBUTING.md). For sharing, use the [post and demo guide](community/SHARING.md).

MIT license. External materials retain their own licenses. [Research and related projects](resources/RESEARCH_NOTES.md).
