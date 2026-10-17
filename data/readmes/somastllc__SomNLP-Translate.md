<h1 align="center">SomNLP-Translate</h1>

<p align="center">
  <b>Reproducible, quality-controlled English–Somali parallel data for machine translation.</b><br>
  <i>Xog isbarbar-socota oo Ingiriisi iyo Soomaali ah, looguna talagalay turjumaadda mashiinka.</i>
</p>

<p align="center">
  <b>Rust-first</b> data pipeline · streaming · config-driven · full provenance
</p>

## Status

SomNLP-Translate has completed **M1 — Foundation**. The data contracts and architecture
are defined; public-source downloaders and processing stages are planned next.

| Milestone | Scope | Status |
|-----------|-------|--------|
| M1 | Workspace, schema, documentation | Done |
| M2 | OPUS and MT560 parallel downloaders | Planned |
| M3 | Cleaning, dual LID, filtering, deduplication | Planned |
| M4 | Leakage-resistant splits and evaluation | Planned |
| M5 | Extended and synthetic sources | Planned |
| M6 | Hugging Face release | Planned |

See [PLAN.md](PLAN.md) and [ROADMAP.md](ROADMAP.md).

## Scope

The canonical dataset stores each aligned English–Somali pair once. Language tags make
the record direction-neutral; exporters can create either English→Somali or
Somali→English training views without duplicating source data.

SomNLP-Translate complements
[SomNLP-Corpus](https://github.com/dugsiiye-labs/SomNLP-Corpus):

```text
SomNLP-Corpus     monolingual Somali documents  → language modeling and Somali NLP
SomNLP-Translate  aligned English–Somali pairs  → translation training and evaluation
```

The repositories follow compatible conventions but remain independent Rust workspaces.

## Planned pipeline

```text
download → merge + exact dedup → clean both sides → dual LID → quality filter
         → near dedup + leakage control → train/dev/test split → final
```

Every stage will stream JSONL, emit statistics, and preserve rejected records with
machine-readable reasons.

## Record format

```json
{
  "id": "mt560:sha256-prefix",
  "source": {"text": "Peace is important.", "lang": "en"},
  "target": {"text": "Nabaddu waa muhiim.", "lang": "so"},
  "provenance": {
    "source": "mt560",
    "collected_at": "2026-07-22T00:00:00Z"
  },
  "license": "CC-BY-4.0",
  "hashes": {
    "source": "sha256:...",
    "target": "sha256:...",
    "pair": "sha256:..."
  },
  "quality": {"disposition": "kept", "flags": []},
  "schema_version": 1
}
```

`source` and `target` preserve the upstream alignment order. Training direction is an
export option, not a second stored record. See
[docs/METADATA_SCHEMA.md](docs/METADATA_SCHEMA.md).

## Project layout

```text
SomNLP-Translate/
├── configs/                 # future pipeline configuration
├── crates/
│   ├── common/              # pair schema and shared contracts
│   ├── translate-tools/     # planned download and merge tools
│   └── translate-pipeline/  # planned processing and split stages
├── docs/                    # architecture and data specifications
├── reports/                 # generated stage reports (gitignored)
└── data/                    # generated dataset artifacts (gitignored)
```

## Development

**Requirements:** Rust 1.75+

```bash
cargo test
cargo clippy --all-targets -- -D warnings
cargo fmt --check
```

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Source registry](docs/SOURCES.md)
- [Metadata schema](docs/METADATA_SCHEMA.md)
- [ID strategy](docs/ID_STRATEGY.md)
- [Quality metadata](docs/QUALITY_METADATA.md)
- [Merge semantics](docs/MERGE_SEMANTICS.md)
- [Cleaning plan](docs/CLEANING_PLAN.md)
- [Data pipeline](docs/DATA_PIPELINE.md)
- [Contributing](CONTRIBUTING.md)