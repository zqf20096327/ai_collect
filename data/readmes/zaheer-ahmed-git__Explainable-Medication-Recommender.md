# Explainable Conversational Medication Recommender

Research software for a clinician-facing medication recommender that combines
conversational clinical understanding, hybrid Transformer-GNN ranking, and
grounded explanations.

> Research question: how can a medical conversational recommender produce
> medication rankings that are accurate, faithful, grounded, and clinically
> understandable?

This is research software. It is not a medical device, does not prescribe
medication, and must not replace professional clinical judgment.

## Status

- Data foundation and experimental models are implemented. Protected-data
  results are summarised in the reports listed in the documentation below.
- The paired-OOF late-fusion gate passed on aggregate evaluation. This does
  not authorise clinical use.
- Explainability: a CPU numerical core (fused pairwise margins, bounded grouped
  attribution) is implemented with synthetic tests. Clinical input adapters and
  graph interventions are still planned. See the
  [explainability plan](Documentation/ResearchFinal/ExplainabilityImplementationPlan.md).

## Architecture

The target system has four layers:

1. **Conversational understanding:** an LLM extracts a structured patient profile.
2. **Hybrid recommendation:** a Transformer models patient-context and temporal
   interactions; a heterogeneous GNN models patient, diagnosis, medication, and
   lab relations.
3. **Grounded explainability:** attribution, graph evidence, clinical rules,
   uncertainty, and provenance are assembled before any text is generated.
4. **Clinician review:** ranked candidates with rationale, warnings, and an
   audit trail.

## Data

- MIMIC-IV v3.1 (development), MIMIC-IV-Note v2.2 (text), eICU-CRD v2.0 (external validation).
- Raw PhysioNet data is licensed and is never committed or redistributed.
- Data lives on protected storage, referenced by `DATASET_ROOT`.

## Repository guide

| Path | Contents |
|---|---|
| `pipeline/` | Cohort, extraction, harmonisation, features, baselines, graph and neural training code |
| `scripts/calculco/` | OAR job submission scripts |
| `tests/` | Synthetic-fixture tests |
| `visualization/` | Aggregate-only figure-pack generator |
| `Documentation/` | Research framing, milestones, and protocols (see below) |
| `FinalPosterCDS.pdf` | Research poster |

Key documents:
- [ResearchDetail.md](Documentation/ResearchDetail.md): research framing.
- [DataFoundationRoadmap.md](Documentation/DataFoundationRoadmap.md): implementation sequence.
- [Milestone8B.md](Documentation/Milestone8B.md): graph-aware ablation contract.
- [PairedOOFLateFusionProtocol.md](Documentation/PairedOOFLateFusionProtocol.md): paired five-fold evidence and gate.
- [HybridModelResultReview.md](Documentation/HybridModelResultReview.md): ranking and calibration comparison.
- [ConditionNormalization.md](Documentation/ConditionNormalization.md): condition contract.
- [CalculcoStudentGuide.md](Documentation/CalculcoStudentGuide.md): cluster access and job submission.

## Setup

Development runs on the ULCO Calculco cluster. Python 3.13 with `uv` only.

```bash
uv sync
uv run ruff check .
uv run pytest
```

Machine-specific paths go in a gitignored `.env.calculco` (copy from
`.env.example`). Variables: `PROJECT_HOME`, `DATASET_ROOT`, `DATA_PROTECTED`,
`REPORTS_ROOT`, `WORK_SCRATCH`.

Pipeline commands read protected data. Run small scopes interactively and submit
full runs through OAR (`scripts/calculco/`). Examples:

```bash
uv run python -m pipeline.cohort
uv run python -m pipeline.harmonize
uv run python -m pipeline.evaluate_baselines
```

PyTorch is an optional dependency group. Install it only for the neural branch:

```bash
uv sync --group neural
```

## License

Proprietary. All rights reserved. See [LICENSE](LICENSE). No permission to reuse
or redistribute the code is granted without written consent.
