# Point-in-Time Feature Store Lab

A compact, reproducible data-engineering project for machine learning and
quantitative research portfolios. It builds leakage-safe historical features in
DuckDB, handles late-arriving events with an explicit availability timestamp,
and proves that incremental replay matches a clean full rebuild.

The data is deterministic and synthetic. No external or private data is used.

## What this demonstrates

- Validated DuckDB schemas with immutable event and example primary keys.
- Idempotent batch ingestion: exact replay is a no-op, while conflicting payloads
  for an existing ID fail closed.
- Point-in-time 1-, 7-, and 30-day aggregates using both event time and the time
  an event became available.
- A future seven-day binary label kept strictly outside the feature window.
- Canonical, engine-independent SHA-256 snapshots for reproducibility checks.
- Incremental-versus-full rebuild equivalence.
- A deliberately invalid full-history join, isolated as an audit artifact, that
  makes temporal leakage visible.
- Boundary, late-data, cross-entity, replay, conflict, and end-to-end tests.

## Temporal contract

All timezone-naive timestamps represent UTC seconds. A decision is made at
`observation_time`. An event can contribute to a feature only when:

```text
observation_time - lookback <= event_time < observation_time
and available_at <= observation_time
```

The target is whether a purchase occurs in the mature, non-overlapping interval:

```text
observation_time <= event_time < observation_time + 7 days
```

Events stamped exactly at the decision belong to the label side, not the feature
side. Counts use zero for no history; recency and average purchase amount remain
null, accompanied by `has_prior_history`. The 30-day window is the maximum feature
lookback.

## Quick start

Requires Python 3.10 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
python -m point_in_time_feature_store_lab \
  --output-dir artifacts \
  --entities 150 \
  --days 90 \
  --seed 20260913
```

The command writes:

- `point_in_time_features.csv`: one audited training row per entity-decision pair.
- `naive_full_history_audit.csv`: intentionally invalid output, never model input.
- `pipeline_summary.json`: source manifest, ingestion deltas, audit counts, and hashes.
- `leakage_audit.png`: valid versus naive affected-example rates.
- `boundary_timeline.png`: one decision's eligible, late, and future events.

## Reproducible result

The checked-in artifacts use the command above. They are an implementation audit
for a known synthetic generator, not a production performance claim.

| Check | Result |
| --- | ---: |
| Generated events | 6,125 |
| Entity-decision feature rows | 600 |
| Target prevalence | 54.3% |
| Event-time cutoff violations | 0 |
| Availability cutoff violations | 0 |
| Rows inserted by exact batch replay | 0 |
| Incremental snapshot matches full rebuild | Yes |
| Examples affected by naive full-history join | 600 / 600 |

The deliberately naive join produced 10,487 leaked event–example pairs because
one future or then-unavailable event can contaminate multiple historical decision
rows. See the complete [pipeline summary](artifacts/pipeline_summary.json) and
[valid feature snapshot](artifacts/point_in_time_features.csv).

![Point-in-time leakage audit](artifacts/leakage_audit.png)

![Feature and label boundary example](artifacts/boundary_timeline.png)

## Why `available_at` matters

An event may have occurred yesterday but arrived in the warehouse tomorrow. A
backfill keyed only on `event_time` would incorrectly make it visible to a model
at today's decision. This project requires `available_at <= observation_time`, so
offline training reconstructs what was actually knowable then.

## Scope and limitations

This is a local, offline feature-store demonstration under append-only, immutable
event semantics. It does not claim distributed exactly-once delivery, concurrent
writes, online/offline consistency, low latency, access controls, or production
scale. Corrections and deletions would require explicit versioning that is outside
this lab. Primary keys and hashes detect certain duplication or drift; they do not
prove semantic correctness. Real validity also depends on trustworthy clocks,
entity identity, source completeness, and a documented late-data policy.

Synthetic outputs illustrate leakage mechanisms and reproducible ingestion. They
do not quantify real-world predictive lift or system reliability.

## Repository layout

```text
src/point_in_time_feature_store_lab/
  simulation.py  # deterministic events, delays, and mature labels
  store.py       # contracts, idempotent ingestion, and SQL features
  audit.py       # temporal checks and canonical hashes
  pipeline.py    # incremental replay versus full rebuild
  reporting.py   # audit charts and JSON output
  cli.py         # reproducible command-line workflow
tests/            # exact boundary, conflict, replay, and pipeline tests
artifacts/        # outputs from the documented run
```

## License

MIT
