# Plasma Flux Explorer

**Explore the magnetic architecture of fusion.**

Plasma Flux Explorer is a local-first scientific workstation for exploring released tokamak equilibrium records from the [Sophelio Fusion Equilibrium Challenge](https://huggingface.co/datasets/Sophelio/fusion-equilibrium-challenge). It provides researchers and engineers with interactive 2D poloidal field visualization, 3D axisymmetric surface reconstruction, cross-machine comparison, and model prediction validation while strictly preserving experimental data provenance.

![Plasma Flux Explorer Workspace](docs/screenshots/overview.png)

---

## The Problem It Solves

Tokamak fusion experiments (such as DIII-D and MAST) generate multi-dimensional plasma equilibria and diagnostic signals:

- **Poloidal Magnetic Flux $\psi(R, Z)$:** Reconstructed 2D flux grids from EFIT (Equilibrium and Fitting code) describing magnetic surfaces and confinement.
- **Asynchronous Diagnostic Signals:** Fast magnetic coil currents and spatial Thomson scattering electron temperature/density profiles ($T_e$, $n_e$) sampled on distinct, non-uniform time bases.
- **Machine Learning Benchmarking:** Predictive models for plasma equilibrium need rigorous validation against experimental reconstructions without accidentally computing metrics against withheld evaluation targets.

Plasma Flux Explorer unifies these datasets into an interactive, zero-configuration local workstation that maintains strict scientific provenance between ground-truth EFIT reconstructions, raw diagnostic measurements, imported model predictions, and educational analytical models.

---

## Key Capabilities

- **Interactive 2D Poloidal Field Viewer:** Real-time marching-squares contour extraction, perceptual colormaps (Viridis, Plasma, Cividis, Inferno), equal-scale geometry ($R$-$Z$ in meters), pan/zoom, coordinate probe, and toggleable layers (flux surfaces, LCFS boundary, magnetic axis, X-point candidates).
- **Temporal Discharge Scrubbing & Playback:** High-performance timeline scrub bar with variable playback rates ($0.5\times$, $1\times$, $2\times$), frame stepping, and synchronized diagnostic readouts.
- **Diagnostic Signal Alignment:** Correlated time-series displays for magnetic coil inputs and plasma current ($I_p$), alongside nearest-neighbor Thomson scattering profiles ($T_e$, $n_e$) mapped to independent diagnostic time bases.
- **3D Axisymmetric Magnetic Surface:** Hardware-accelerated 3D surface revolved from the experimental Last Closed Flux Surface (LCFS) with interactive orbit controls and wireframe mode.
- **Cross-Machine Comparative Analysis:** Side-by-side DIII-D vs. MAST comparison rendered on a shared physical scale with nearest-frame temporal alignment, shape parameter deltas ($\Delta$), and symmetric boundary distance metrics (mean symmetric and Hausdorff distances).
- **Plasma Boundary Geometry:** Quantitative shape extraction computing major radius ($R_0$), minor radius ($a$), aspect ratio ($A$), elongation ($\kappa$), upper/lower triangularity ($\delta$), cross-sectional area (shoelace integration), and axisymmetric volume (Pappus' centroid theorem).
- **Model Prediction Laboratory:** Session-only JSON prediction import with structural validation (grid dimensions, coordinate vectors, timestamp alignment, unit checks) and residual visualization ($|\Delta\psi|$).
- **Zero-Cloud Architecture:** Works completely offline using local Parquet archives and JSON catalog caches, with optional deployment to Cloudflare Workers via OpenNext.

---

## Visual Showcase

### Research Workspace Overview

Centralized dashboard tracking local catalog status, indexed equilibrium frames, machine coverage (DIII-D / MAST), and data source provenance.

![Research Workspace Overview](docs/screenshots/dashboard.png)

### 3D Axisymmetric Surface Reconstruction

Revolves the experimental Last Closed Flux Surface (LCFS) around the tokamak's major axis ($R=0$), providing an intuitive 3D representation of the magnetic boundary.

![3D Axisymmetric Geometry](docs/screenshots/feature-01-3d-geometry.png)

### Cross-Machine Equilibrium Comparison

Compares DIII-D (conventional aspect ratio, $A \approx 2.9$) and MAST (spherical tokamak, $A \approx 1.5$) on a shared physical $R$-$Z$ scale, computing geometric differences and symmetric boundary distances.

![Cross-Machine Comparison](docs/screenshots/feature-02-machine-comparison.png)

### Plasma Geometry & Boundary Parameter Construction

Renders the extracted LCFS boundary contour alongside the magnetic axis, geometric center, and 18 SI derived parameters (elongation, triangularity, volume, and EFIT scalar parameters $\beta_N$, $l_i$, $q_{95}$).

![Plasma Geometry](docs/screenshots/feature-03-plasma-geometry.png)

### Model Prediction Import & Validation

Inspect and validate external machine-learning model predictions against reference EFIT reconstructions without code execution or server-side persistence.

![Prediction Laboratory](docs/screenshots/feature-04-prediction-lab.png)

---

## Quick Start

### Prerequisites

- **Node.js:** 20.9.0 or higher
- **pnpm:** 10.0.0 or higher (or `npm`)
- **Python:** 3.11 or higher
- **uv:** For Python dependency management

### Installation

```bash
# Clone the repository
git clone https://github.com/ranajahanzaib/plasma-flux-explorer.git
cd plasma-flux-explorer

# Install JavaScript and Python dependencies
pnpm install
uv sync
```

### Bootstrap Starter Data

Fetch the official starter-kit demo records for DIII-D (shot 203702, 166 frames) and MAST (shot 28348, 36 frames):

```bash
pnpm data:bootstrap
pnpm data:validate
```

The bootstrap command stores raw data in `data/raw/` and compiles the index to `data/processed/catalog.json`.

### Run the Application

```bash
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser. The application runs locally with no external API keys or cloud credentials required.

---

## Data Ingestion & Configuration

The bootstrap tool supports downloading official starter demos or fetching challenge splits from Hugging Face:

```bash
# Default: Downloads official starter demos for DIII-D and MAST
pnpm data:bootstrap

# Challenge mode: Fetch bounded rows from the challenge corpus
pnpm data:bootstrap -- --source challenge --config diii_d_train --config mast_public_test --max-shots 2
```

### Supported Configurations

- `diii_d_train`: Training records containing full EFIT reference flux grids and scalar parameters.
- `diii_d_public_test`: Challenge evaluation records with withheld reference flux (diagnostic signals only).
- `mast_public_test`: Spherical tokamak challenge test split with withheld reference flux.
- `starter_demo`: Official starter-kit demo files providing complete reference reconstructions for both DIII-D and MAST.

---

## Project Architecture

```text
plasma-flux-explorer/
├── app/                      # Next.js App Router (pages and API routes)
│   ├── api/                  # REST endpoints (/catalog, /discharges, /geometry, /topology)
│   ├── layout.tsx            # Root HTML layout and metadata
│   ├── page.tsx              # Application shell and module navigation
│   └── workspace.css         # Responsive scientific workstation stylesheet
├── public/
│   └── app.js                # Client-side workstation engine (marching squares, 3D canvas, state)
├── scientific/
│   └── equilibrium.py        # Numerical routines (flux normalization, geometry, Pappus volume)
├── scripts/
│   ├── bootstrap_data.py     # Parquet ingestion, validation, and catalog builder
│   ├── validate_data.py      # Catalog schema and numerical integrity validator
│   └── publish-catalog.mjs   # Cloudflare R2 catalog synchronization tool
├── tests/
│   └── test_equilibrium.py   # Unit test suite for scientific algorithms and ingestion
├── docs/
│   ├── screenshots/          # Showcase captures referenced in documentation
│   ├── architecture.md       # Technical design and data flow
│   ├── data-schema.md        # JSON schema definitions
│   ├── data-sources.md       # Upstream data sources and attribution
│   ├── deployment.md         # Local and Cloudflare Worker deployment
│   ├── equilibrium-processing.md # Marching squares and geometric derivations
│   └── limitations.md        # Scientific and technical boundaries
└── wrangler.jsonc            # Cloudflare Workers / OpenNext configuration
```

---

## Engineering Commands

| Command               | Description                                                      |
| --------------------- | ---------------------------------------------------------------- |
| `pnpm dev`            | Starts the Next.js development server on `http://localhost:3000` |
| `pnpm build`          | Compiles optimized Next.js assets and compiles Python modules    |
| `pnpm start`          | Runs the production Next.js server locally                       |
| `pnpm test`           | Executes the unit test suite (`uv run python -m unittest`)       |
| `pnpm typecheck`      | Validates TypeScript types and checks client JavaScript syntax   |
| `pnpm lint`           | Runs ESLint across the codebase                                  |
| `pnpm data:bootstrap` | Ingests and indexes tokamak equilibrium records                  |
| `pnpm data:validate`  | Validates local catalog integrity and numeric boundaries         |
| `pnpm cf:build`       | Builds the Cloudflare Worker bundle with OpenNext                |
| `pnpm cf:preview`     | Previews the Cloudflare Worker locally                           |

---

## Scientific Methods & Boundaries

- **Flux Coordinate Normalization:** Normalized poloidal flux is computed via:
  $$\psi_N = \frac{\psi - \psi_{\text{axis}}}{\psi_{\text{boundary}} - \psi_{\text{axis}}}$$
  Normalization is only evaluated when axis and boundary flux values are supplied and non-degenerate.
- **Boundary Integration:** Cross-sectional area is determined by the discrete Green's theorem (shoelace formula). Axisymmetric volume is calculated via Pappus' centroid theorem using the true polygon area centroid, avoiding circular approximations.
- **Topology Candidates:** Stationary points ($\nabla \psi = 0$) are resolved at grid resolution using bilinear cell saddle analysis. The workstation clearly labels these as candidates rather than refined separatrix extractions.
- **Separation of Time Bases:** Diagnostic sample rates and EFIT equilibrium reconstruction times are maintained on their independent native time grids without artificial interpolation.
- **Withheld Ground Truth:** The workstation strictly respects dataset splits: withheld test targets are flagged as unavailable, and reference errors are never calculated for unlabeled splits.

For detailed documentation, see [Scientific Methodology](docs/equilibrium-processing.md), [Data Sources](docs/data-sources.md), and [Limitations](docs/limitations.md).

---

## License & Custom Work

[![Hire me](https://img.shields.io/badge/Open%20to%20work-work%40withrana.com-brightgreen)](mailto:work@withrana.com) [![LinkedIn](https://img.shields.io/badge/LinkedIn-workwithrana-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/workwithrana)
[![Upwork](https://img.shields.io/badge/Upwork-Hire%20Me-14A800?style=flat&logo=upwork&logoColor=white)](https://www.upwork.com/freelancers/~01bbcf6edb91a8df5f)
[![Contra](https://img.shields.io/badge/Contra-Hire%20Me-000000?style=flat)](https://contra.com/ranajahanzaib/)

**License:** MIT, see [LICENSE](LICENSE). Free for personal and commercial use. Source datasets retain their respective terms and attribution requirements.

**Author:** Rana Jahanzaib

**Need scientific tooling or custom visualization built for your stack?** Get in touch: [work@withrana.com](mailto:work@withrana.com)
