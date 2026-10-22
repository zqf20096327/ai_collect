# 🧬 GenomixAI — AI-Powered DNA Variant Analysis

GenomixAI is an applied AI research project exploring how **genomic foundation models can assist with DNA variant analysis**.

The system combines **Evo2-based inference**, clinical variant data, genome references, and a full-stack application to make genomic variant exploration more accessible.

> **Important:** This is a research/prototype system and is **not a clinical diagnostic tool**. Predictions should not be used for medical decisions.

## Why GenomixAI?

Interpreting genomic variants requires combining sequence context with biological and clinical evidence. GenomixAI explores a practical workflow for bringing these signals together:

1. Accept a genomic variant or gene of interest.
2. Run model-based sequence analysis with **Evo2**.
3. Retrieve relevant clinical classifications from **NCBI ClinVar**.
4. Retrieve reference/genome context from **UCSC Genome Browser APIs**.
5. Present the results through an interactive web application.

## Architecture

```
                    ┌─────────────────────┐
                    │     Next.js UI      │
                    │  React + TypeScript  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    FastAPI API      │
                    │   Python 3.12       │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┼─────────────┐
                 ▼             ▼             ▼
          ┌───────────┐  ┌───────────┐  ┌───────────┐
          │   Evo2    │  │  ClinVar  │  │    UCSC   │
          │  Inference│  │   API     │  │ Genome API│
          └─────┬─────┘  └───────────┘  └───────────┘
                │
                ▼
          ┌─────────────┐
          │ Modal GPU   │
          │ H100 / GPU  │
          └─────────────┘
```

## Key Features

- 🧬 DNA variant analysis with Evo2
- ⚖️ Comparison with ClinVar clinical classifications
- 🔎 Gene and chromosome exploration
- 🌍 Reference genome support
- 📊 Model confidence information
- ⚡ GPU-accelerated inference
- 🚀 Serverless GPU deployment through Modal
- 📱 Responsive web interface

## Technical Stack

### AI / Backend
- Python 3.12
- FastAPI
- Evo2
- Modal serverless GPUs
- NCBI ClinVar API
- UCSC Genome API

### Frontend
- Next.js
- React
- TypeScript
- Tailwind CSS
- shadcn/ui

## Evaluation & Research

The project is intended as an **applied research and engineering prototype** rather than a clinically validated predictor.

A reproducible evaluation should:

1. **Define the prediction target first.** Specify the variant classes, label source, genome build, and intended interpretation before choosing metrics.
2. **Prevent data leakage.** Keep duplicate records and variants from the same locus or related samples in the same split where appropriate. Prefer chromosome-, gene-, or locus-aware holdouts when they match the intended generalization claim.
3. **Record provenance.** Store dataset versions, ClinVar review status and access date, genome build, model/checkpoint identifier, inference settings, and preprocessing version.
4. **Compare against baselines.** Include simple sequence or annotation-based baselines alongside Evo2, and compare against ClinVar labels only with clear acknowledgement that ClinVar is an evidence database, not an infallible ground truth.
5. **Report discrimination and calibration.** Use AUROC and AUPRC for suitable binary tasks, class-wise precision/recall/F1 for imbalanced labels, and calibration metrics or reliability plots when output probabilities are interpreted as confidence.
6. **Measure operational cost.** Track latency, GPU type, memory use, throughput, and cost per evaluated variant.
7. **Publish error analysis.** Report performance by variant class and data subgroup, confidence intervals where feasible, and representative failure cases.

Suggested experiment artifacts include a versioned dataset manifest, fixed split definitions, model configuration, machine-readable metrics, and a short report describing limitations. Do not tune on the final held-out test set.

**No clinical performance claims are made by this repository.** Any future results should be independently validated before consideration for clinical use.

## Getting Started

### Clone

```bash
git clone https://github.com/GeneralSubhra/variant-analysis-evo2
cd variant-analysis-evo2
```

### Backend

```bash
cd backend

uv venv --python 3.12
source .venv/bin/activate
# Windows:
# .venv\\Scripts\\activate

uv pip install -r requirements.txt

modal setup
modal run main.py
```

For production deployment:

```bash
modal deploy main.py
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend runs at:

```
http://localhost:3000
```

## References

- Evo2 paper: https://www.science.org/doi/10.1126/science.ado9336
- Evo2 implementation: https://github.com/ArcInstitute/evo2
- ClinVar: https://www.ncbi.nlm.nih.gov/clinvar/
- UCSC Genome Browser: https://genome.ucsc.edu/

## Roadmap

- [ ] Add reproducible benchmark suite
- [ ] Add baseline model comparisons
- [ ] Add automated evaluation pipeline
- [ ] Add latency / cost benchmarks
- [ ] Expand variant classes and genomic regions
- [ ] Improve uncertainty and calibration analysis
