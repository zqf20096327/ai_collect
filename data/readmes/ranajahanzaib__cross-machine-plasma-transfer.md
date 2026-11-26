# Cross-Machine Plasma Transfer Analysis

An open-source scientific research workbench for investigating domain shift, transfer learning, uncertainty, and cross-machine generalization in magnetic equilibrium reconstruction between the **DIII-D** (conventional aspect ratio) and **MAST** (spherical) tokamaks.

The platform addresses a foundational problem in computational plasma physics: **why a model trained on one tokamak fails on another, and how we can systematically quantify, visualize, and reduce that transfer discrepancy without target-label leakage.**

![Cross-Machine Plasma Transfer Dashboard Overview](docs/screenshots/overview.png)

---

## Key Highlights

- **Rigorous Protocol Enforcement (`ProtocolGuard`):** Programmatically prevents target-label and scaffolding-channel leakage across Protocol A (Strict source-only), Protocol B (Challenge label-free adaptation), and Protocol C (FAIR-MAST independent research).
- **Physical Tokamak Geometry Engine:** Computes exact 2D $(R, Z)$ conductor polygons for DIII-D's 18 shaping/field-shaping coils (including skewed F-coils) and MAST's 10 poloidal P-coils in verified $\text{kA}\cdot\text{turn}$.
- **Invariant Feature Engineering:** Translates disparate diagnostic chords, Thomson-scattering electron temperatures/densities ($T_e, n_e$), and magnetics into geometry-weighted current moments and gap-aware harmonized profiles.
- **Statistical Domain Shift Diagnostics:** Quantifies distribution discrepancies via univariate Wasserstein earth-mover distances, Kolmogorov-Smirnov statistics, kernel Maximum Mean Discrepancy (MMD), and shot-stratified domain classifiers.
- **Unsupervised Domain Adaptation:** Benchmarks Correlation Alignment (CORAL) covariance whitening/recoloring and Optimal Transport (Sinkhorn divergence) against unadapted baselines.
- **2D Poloidal Flux Reconstruction ($\psi(R, Z)$):** Reconstructs $65 \times 65$ magnetic flux surfaces, edge safety factor $q_{95}$, and normalized beta $\beta_N$, coupled with a $k$-NN source-support Out-of-Distribution (OOD) risk detector.
- **Full-Stack Scientific Workbench:** Next.js 14 App Router dashboard with D3.js and HTML5 Canvas visualizations backed by a high-throughput FastAPI analytical service.

---

## Visual Showcase & Feature Tour

### 1. Shared Feature-Space Manifold

Projecting high-dimensional tokamak operating states into shared 2D manifolds (UMAP and PCA) reveals the fundamental domain gap separating conventional and spherical configurations.

![Shared Feature-Space Explorer](docs/screenshots/feature-space.png)

### 2. Tokamak Physical Geometry Comparison

Direct physical cross-section comparison illustrating vessel boundaries, Thomson-scattering diagnostic chords, and poloidal field coils for DIII-D ($R_0 = 1.67\,\text{m}, a = 0.67\,\text{m}$, aspect ratio $2.5$) versus MAST ($R_0 = 0.85\,\text{m}, a = 0.65\,\text{m}$, aspect ratio $1.3$).

![Machine Geometry Comparison](docs/screenshots/machine-geometry.png)

### 3. Quantitative Domain Shift Analysis

Statistical evaluation of cross-machine covariate shift showing a multivariate MMD of `0.593` and domain classifier separability ($\text{ROC-AUC} = 1.00$), isolating the primary physical drivers of domain divergence (`coil_current_abs_sum`, $T_e$ edge quantiles, and core diagnostic coverage).

![Quantitative Domain Shift Analysis](docs/screenshots/domain-shift.png)

### 4. Equilibrium Reconstruction Prediction Explorer

Synchronized $65 \times 65$ 2D poloidal magnetic flux $\psi(R, Z)$ maps displaying the EFIT reference, baseline model prediction, and absolute error for DIII-D, alongside zero-shot target reconstruction on MAST with Protocol B leakage protection.

![Equilibrium Reconstruction Predictions](docs/screenshots/equilibrium-reconstruction.png)

### 5. Domain Adaptation Laboratory

Interactive comparison between unadapted baseline representations and Correlation Alignment (CORAL), demonstrating covariance-aligned target projection onto source manifold support without requiring target labels.

![Domain Adaptation Laboratory](docs/screenshots/domain-adaptation.png)

### 6. Experimental Dataset Inventory

Live inventory of real tokamak discharges from the [Sophelio Fusion Equilibrium Challenge dataset](https://huggingface.co/datasets/Sophelio/fusion-equilibrium-challenge) at pinned revision `1e280905b85f2a6fdde7e06fca8cf3a1edf447cb`.

![Dataset Inventory](docs/screenshots/dataset-inventory.png)

---

## Architecture Overview

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        Next.js 14 Scientific UI                        │
│   D3.js Cross-Sections · Canvas Flux Heatmaps · UMAP Manifold Explorer │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ HTTP / Rewrites (:3000 -> :8000)
┌───────────────────────────────────▼────────────────────────────────────┐
│                        FastAPI Analytical Service                      │
│      /api/overview  ·  /api/machines  ·  /api/domain-shift  ·  ...     │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│                   Scientific Core (plasma_transfer)                    │
│ ┌──────────────────────┐ ┌──────────────────────┐ ┌──────────────────┐ │
│ │    ProtocolGuard     │ │    MachineGeometry   │ │ SignalHarmonizer │ │
│ └──────────────────────┘ └──────────────────────┘ └──────────────────┘ │
│ ┌──────────────────────┐ ┌──────────────────────┐ ┌──────────────────┐ │
│ │ DomainShiftAnalyzer  │ │    CORAL / Sinkhorn  │ │  PCARegression   │ │
│ └──────────────────────┘ └──────────────────────┘ └──────────────────┘ │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│                  Hugging Face Fusion Equilibrium Data                  │
│       DIII-D Discharges (Labelled)  ·  MAST Discharges (Label-Free)    │
└────────────────────────────────────────────────────────────────────────┘
```

---

## Local Setup & Quick Start

### Prerequisites

- **Python:** 3.11 or 3.12 with [`uv`](https://docs.astral.sh/uv/) installed
- **Node.js:** v18+ or v20+ with [`pnpm`](https://pnpm.io/) (v9+)

### 1. Clone & Install Dependencies

```bash
git clone https://github.com/ranajahanzaib/cross-machine-plasma-transfer.git
cd cross-machine-plasma-transfer

# Install Python scientific dependencies
uv sync --extra dev

# Install frontend JavaScript dependencies
pnpm install
```

### 2. Start Local Research Environment

Launch both the FastAPI backend and Next.js dashboard concurrently:

```bash
pnpm dev
```

- **Frontend Dashboard:** [http://localhost:3000](http://localhost:3000)
- **FastAPI Backend:** [http://localhost:8000](http://localhost:8000)
- **Interactive OpenAPI Documentation:** [http://localhost:8000/docs](http://localhost:8000/docs)

Custom ports can be configured via environment variables:

```bash
API_PORT=8080 PORT=3001 pnpm dev
```

The repository includes a precomputed, deterministic analysis artifact (`artifacts/quickstart_analysis.json`) so the dashboard is immediately populated upon first launch.

---

## CLI & Pipeline Operations

The project includes the `plasma-transfer` command-line utility for inspection and pipeline execution:

```bash
# Display platform configuration and active scientific protocol
uv run plasma-transfer info

# Ingest raw experimental shot files from Hugging Face
uv run plasma-transfer ingest --profile quickstart

# Execute end-to-end scientific pipeline and regenerate analytical artifacts
uv run plasma-transfer run-pipeline
```

### CLI Output Example

```text
$ uv run plasma-transfer info
Cross-Machine Plasma Transfer Analysis
Investigating domain shift and transfer learning between DIII-D and MAST tokamaks.
Active Protocol: Protocol B (Challenge-Compatible Label-Free Adaptation)
```

---

## Automated Verification & Test Suite

The project includes comprehensive test coverage spanning the scientific core, mathematical geometry, protocol guards, and REST API endpoints.

```bash
# Run complete Python test suite (16 tests)
uv run pytest

# Run TypeScript typecheck across Next.js application
pnpm typecheck

# Run production build of frontend dashboard
pnpm build
```

### Test Suite Summary

- `test_protocol_guard_leakage_prevention`: Enforces zero target-label and scaffolding feature admission.
- `test_split_integrity_guard`: Verifies shot-stratified splitting prevents contamination between folds.
- `test_machine_geometry_polygon_computation`: Validates conductor polygon math and skewed coil coordinates.
- `test_signal_harmonizer_alignment`: Asserts gap-aware interpolation and missing-data masking.
- `test_profile_statistics_handle_all_missing_rows`: Verifies robust handling of empty profile rows without runtime warnings.
- `test_domain_shift_metrics`: Tests Wasserstein, KS, and distribution overlap calculations.
- `test_pca_regression_baseline`: Tests low-dimensional flux surface regression fitting and shape assertions.
- `test_ood_detector`: Asserts $k$-NN distance scoring and out-of-distribution classification.
- `test_api_*`: Validates all FastAPI endpoints (`/health`, `/overview`, `/machines`, `/geometry`, `/embeddings`, `/domain-shift`, `/shots`, `/predictions/sample`, `/reports/markdown`).

---

## Repository Structure

```text
├── apps/
│   └── web/                     # Next.js 14 dashboard (Tailwind, D3.js, Canvas)
│       ├── src/app/             # 17 analytical routes (overview, machines, predictions, etc.)
│       └── next.config.js       # Dynamic API proxying and rewrite configuration
├── artifacts/
│   └── quickstart_analysis.json # Precomputed scientific analysis snapshot (762 observations)
├── docs/
│   └── screenshots/             # High-resolution visual showcase images
├── python/
│   └── plasma_transfer/         # Scientific core package
│       ├── adaptation/          # CORAL and Optimal Transport (POT/Sinkhorn)
│       ├── cli/                 # Typer-based CLI implementation
│       ├── domain_shift/        # MMD, KS, Wasserstein, and domain classifier
│       ├── features/            # Geometry-aware feature extraction
│       ├── geometry/            # Conductor polygon and machine specifications
│       ├── models/              # PCA regression and reference baselines
│       ├── ood/                 # k-NN out-of-distribution detector
│       ├── preprocessing/       # Gap-aware signal harmonizer
│       └── protocols/           # ProtocolGuard and lineage tracker
├── scripts/
│   └── dev.sh                   # Concurrent local development runner
├── services/
│   └── api/plasma_api/          # FastAPI backend application
└── tests/                       # Pytest automated test suite
```

---

## Scientific Scope & Limitations

- **Experimental Dataset:** Evaluates real tokamak discharges from the [Fusion Equilibrium Challenge](https://huggingface.co/datasets/Sophelio/fusion-equilibrium-challenge). Running `plasma-transfer run-pipeline` downloads remote dataset shards into local cache.
- **Protocol B Leakage Protection:** Target reference flux labels ($\psi$) for MAST are strictly withheld. Any baseline predictions on MAST are exploratory zero-shot transfers.
- **In-Sample Baseline Evaluation:** The baseline model MAE ($\psi = 0.0472\,\text{V}\cdot\text{s/rad}$) reported on DIII-D is in-sample training performance and should not be construed as held-out generalization error.
- **Hardware Acceleration:** Computations default to CPU and automatically utilize Apple Silicon Metal Performance Shaders (MPS) or NVIDIA CUDA when available.

---

## Contributing

Contributions from plasma physicists, computational researchers, and ML engineers are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) and review the [Code of Conduct](CODE_OF_CONDUCT.md).

## License & Custom Work

[![Hire me](https://img.shields.io/badge/Open%20to%20work-work%40withrana.com-brightgreen)](mailto:work@withrana.com) [![LinkedIn](https://img.shields.io/badge/LinkedIn-workwithrana-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/workwithrana)
[![Upwork](https://img.shields.io/badge/Upwork-Hire%20Me-14A800?style=flat&logo=upwork&logoColor=white)](https://www.upwork.com/freelancers/~01bbcf6edb91a8df5f)
[![Contra](https://img.shields.io/badge/Contra-Hire%20Me-000000?style=flat)](https://contra.com/ranajahanzaib/)

**License:** MIT, see [LICENSE](LICENSE). Free for personal and commercial use.

**Author:** Rana Jahanzaib

**Need this built for your stack?** Email me what you're working on: work@withrana.com
