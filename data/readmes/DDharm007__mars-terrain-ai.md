# MANGAL DRISHTI (मंगल दृष्टि)

**Decoding the Red Planet Through Artificial Intelligence.**

[![License: MIT](https://img.shields.io/badge/License-MIT-C87951.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB.svg)](requirements.txt)
[![PyTorch](https://img.shields.io/badge/PyTorch-CUDA%20%2F%20CPU-EE4C2C.svg)](requirements.txt)
[![Frontend](https://img.shields.io/badge/React%2019%20%2B%20TypeScript-Vite-61DAFB.svg)](frontend/package.json)

> **Creator & Maintainer:** Dharm Patel ([@DDharm007](https://github.com/DDharm007))  
> **Repository:** [https://github.com/DDharm007/Mangal-Drishti](https://github.com/DDharm007/Mangal-Drishti)  
> **Final Integrity Report:** [MANGAL_DRISHTI_FINAL_INTEGRITY_REPORT.pdf](docs/release/MANGAL_DRISHTI_FINAL_INTEGRITY_REPORT.pdf)

---

## Scientific & Operational Limitation Notice

> **Important:** MANGAL DRISHTI is a **2D semantic perception and terrain intelligence research platform** trained on NASA/JPL AI4MARS imagery (`512 × 512` single monocular rover frames).  
> Semantic terrain classes (`Soil`, `Bedrock`, `Sand`, `Big Rock`) and the experimental visual concern index **do NOT verify physical rover safety or terrain traversability**. Real planetary rover path planning requires 3D stereo range/elevation geometry, local slope gradients, obstacle clearance relative to chassis kinematics, and wheel-soil terramechanics. Always verify `physical_safety_verified: false` in exported reports.

---

## Overview

MANGAL DRISHTI (**Mars Autonomous Navigation, Geospatial Analysis & Learning**) is an end-to-end computer vision, quantitative benchmarking, and mission-control software suite for Martian surface terrain segmentation.

### Core Capabilities

1. **Leakage-Free Data Engineering (AI4MARS v0.6)**:
   - Processes `2,326` raw rover image-mask pairs (`2,296` valid; `30` all-`255` unlabeled frames rejected) from NASA/JPL AI4MARS (Zenodo Record `15995036`).
   - Enforces temporal drive cluster isolation using MSL SCLK timestamps (`43,200 s` gap threshold across `189` clusters -> `153` train / `36` val clusters; zero frame overlap).
   - Preserves mask integrity strictly via nearest-neighbor resizing (`ignore_index=255` for MXY rover hardware masks, `>30 m` stereo range masks, and unlabeled regions).
2. **Semantic Segmentation Models (PyTorch + AMP)**:
   - **DeepLabV3+ + ResNet50 (Default)** (`40,347,812` params) — ASPP multi-scale context + low-level decoder fusion.
   - **U-Net + ResNet34** (`24,521,796` params) — Symmetric encoder-decoder with skip connections.
   - **Optimized Variants** trained with balanced Hybrid Cross-Entropy + Dice loss (`deeplabv3plus_optimized`, `unet_optimized`).
3. **Rigorous Held-Out Expert Test & Domain Shift Evaluation**:
   - Benchmarked untouched against all **526 JPL expert consensus frames**: **322 MSL (Curiosity)** + **204 MER (141 Opportunity + 63 Spirit)** across combined, per-rover, confidence, confusion-matrix, and GPU/CPU latency profiles.
4. **Terrain Intelligence Engine (`src/intelligence/`)**:
   - Computes class composition percentages/pixels, OpenCV connected terrain components (`REG_*`), 2D Big Rock candidate bounding boxes, softmax mean confidence, Shannon entropy (nats + normalized), boundary complexity density, experimental 2D visual concern assessment, 9-panel diagnostic visual artifacts, and structured JSON reports.
5. **FastAPI + React Mission Control Web Application**:
   - Dark, scientific 6-route console (`Overview`, `Terrain Analysis`, `Intelligence Reports`, `Model Performance`, `Dataset & Research`, `System Status`) with interactive segmentation inspection, 9 visualization modes, zoom/opacity controls, row-normalized confusion matrix heatmaps, filterable archives, and rendered research markdown.

---

## Application Demonstrations

### Live Terrain Analysis Workflow (`Upload -> GPU Inference -> 9 Visualization Modes -> Region Highlighting`)

![MANGAL DRISHTI Live Analysis Workflow](docs/media/demos/mangal_drishti_analysis_workflow.gif)

### Full Mission Control Workspace Tour (`Overview -> Reports -> Confusion Matrices -> Research -> Diagnostics`)

![MANGAL DRISHTI Mission Control Tour](docs/media/demos/mangal_drishti_mission_tour.gif)

---

## Interface Gallery

| Mission Overview Dashboard | Terrain Analysis Workspace |
|---|---|
| ![Overview Dashboard](docs/media/screenshots/01_overview_dashboard.png) | ![Terrain Analysis](docs/media/screenshots/02_terrain_analysis.png) |
| **Intelligence Reports Archive** | **Model Benchmarks & Confusion Heatmaps** |
| ![Intelligence Reports](docs/media/screenshots/03_intelligence_reports.png) | ![Model Performance](docs/media/screenshots/04_model_performance.png) |
| **Dataset & Scientific Research** | **System Diagnostics & Runtime Cache** |
| ![Dataset Research](docs/media/screenshots/05_dataset_research.png) | ![System Diagnostics](docs/media/screenshots/06_system_diagnostics.png) |

---

## Dataset Taxonomy & Verification Splits

| Class ID | Class Label | Step 2 RGB Visualization | Train Pixel Share | Median-Frequency Weight |
|---:|---|---|---:|---:|
| `0` | **Soil** | `(166, 97, 26)` | `47.5450%` | `0.545153` |
| `1` | **Bedrock** | `(55, 126, 184)` | `46.2734%` | `0.560134` |
| `2` | **Sand** | `(245, 194, 66)` | `5.5653%` | `4.657246` |
| `3` | **Big Rock** | `(228, 26, 28)` | `0.6163%` | `12.000000` (capped) |
| `255` | **Unlabeled / Ignore** | `(40, 44, 52)` | Excluded from loss/metrics | Ignored |

- **Training Split:** `1,407` pairs (MSL SCLK clusters)
- **Validation Split:** `363` pairs (MSL SCLK clusters)
- **Held-Out Expert Test Split:** `526` pairs (`322` MSL Curiosity + `141` MER-1 Opportunity + `63` MER-2 Spirit; `0.3868%` valid `Big Rock` pixels)

---

## Quantitative Model Benchmarks & Ground-Truth Results

All evaluation metrics below strictly exclude `ignore_index=255` pixels and were measured on the **untouched 526-image JPL Expert Test Set** unless labeled `Validation (363)`.

### 1. Held-Out JPL Expert Test & Validation Summary

| Model & Split | mIoU | Mean Dice | Pixel Acc | Soil IoU | Bedrock IoU | Sand IoU | Big Rock IoU | Big Rock P / R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **DeepLabV3+ Baseline** (Val 363, Ep 10) | `0.7659` | — | — | — | — | — | — | — |
| **U-Net Baseline** (Val 363, Ep 6) | `0.7466` | — | — | — | — | — | — | — |
| **DeepLabV3+ Baseline** (Test Combined 526) | `0.6900` | `0.7765` | `0.9196` | `0.8777` | `0.8331` | `0.8363` | `0.2130` | `0.343 / 0.360` |
| **U-Net Baseline** (Test Combined 526) | `0.6819` | `0.7646` | `0.9213` | `0.8948` | `0.8135` | `0.8405` | `0.1790` | `0.247 / 0.393` |
| **DeepLabV3+ Optimized** (Test Combined 526) | `0.6897` | `0.7605` | `0.9344` | `0.9017` | `0.8387` | `0.8780` | `0.1406` | `0.449 / 0.170` |
| **U-Net Optimized** (Test Combined 526) | `0.6932` | `0.7756` | `0.9268` | `0.8940` | `0.8193` | `0.8598` | `0.1999` | `0.411 / 0.280` |
| **DeepLabV3+ Optimized** (Val 363 / Test MSL 322) | `0.8051 / 0.7811` | `— / —` | `— / —` | `— / —` | `— / —` | `— / —` | `0.5656 / —` | — |

### 2. Cross-Rover Domain Shift (MSL In-Distribution vs. MER Out-of-Distribution)

| Model | MSL Test (322) mIoU | MER Test (204) mIoU | MER-1 Opportunity (141) | MER-2 Spirit (63) |
|---|---:|---:|---:|---:|
| **DeepLabV3+ Baseline** | `0.7311` | `0.6265` | `0.6574` | `0.4634` |
| **U-Net Baseline** | `0.7144` | `0.6276` | — | — |
| **DeepLabV3+ Optimized** | `0.7811` | `0.6165` | — | — |

### 3. Hardware Runtime & Throughput (`NVIDIA GeForce RTX 3050 A Laptop GPU`, 4 GB VRAM)

| Architecture | Parameters | State Dict / Full Checkpoint | GPU FP16 bs=1 Avg / FPS | CPU Avg Latency |
|---|---:|---:|---:|---:|
| **DeepLabV3+ + ResNet50** | `40,347,812` | `154.13 MB` / `462.24 MB` | `23.968 ms` / `41.722 FPS` | `672.681 ms` |
| **U-Net + ResNet34** | `24,521,796` | `93.62 MB` / `280.91 MB` | `22.882 ms` / `43.703 FPS` | `447.258 ms` |

---

## Independent Validation on Previously Unseen NASA Mars Imagery

To test real-world qualitative behavior outside the AI4MARS corpus, **4 newly acquired raw Mars surface frames** (downloaded on `2026-11-23 UTC` from public NASA Perseverance and Curiosity feeds) were verified against all **`2,326`** known IDs in `split_manifest.json` (`0` overlap / `dataset_leakage_checked: true`) and analyzed across all **4 trained models** (`16` inference runs).

> **Important Scientific Separation:** Ground-truth segmentation masks do **NOT** exist for these public NASA feeds (`ground_truth_available: false`). Quantitative accuracy, IoU, Dice, precision, and recall are **NOT** computed or mixed with the JPL benchmark above. Detailed machine-readable results live in [`unseen_manifest.json`](docs/validation/unseen_mars_imagery/metadata/unseen_manifest.json) and [`unseen_validation_notes.md`](docs/validation/unseen_mars_imagery/research_notes/unseen_validation_notes.md).

| NASA Image ID | Mission · Camera · Sol | DeepLabV3+ Baseline | U-Net Baseline | DeepLabV3+ Optimized | U-Net Optimized |
|---|---|---|---|---|---|
| `ZL0_2024_0846622583_145EBY_N0930000ZCAM10058_1100LMJ` | **Mars 2020 (Perseverance)** · `MCZ_LEFT` · Sol `2024` (`1200×874`) | Dom: `big_rock` (`45.3%`), Sand `38.1%`, Conf `0.598`, H `0.943` | Dom: `sand` (`65.4%`), Bedrock `28.2%`, Rock `1.2%` | Dom: `sand` (`46.8%`), Rock `34.1%`, Conf `0.658` | Dom: `sand` (`78.3%`), Bedrock `16.2%`, Conf `0.709` |
| `NLF_2023_0846549056_005ECM_N0930000NCAM00709_09_095J` | **Mars 2020 (Perseverance)** · `NAVCAM_LEFT` · Sol `2023` (`1200×904`) | Dom: `big_rock` (`66.4%`), Soil `20.5%`, Conf `0.674`, H `0.814` | Dom: `sand` (`83.1%`), Soil `11.4%`, Conf `0.621` | Dom: `big_rock` (`59.3%`), Soil `29.7%`, Conf `0.715` | Dom: `sand` (`83.7%`), Soil `9.0%`, Conf `0.703` |
| `NLB_848553598EDR_F1260000CCAM01081M_` | **MSL (Curiosity)** · `NAV_LEFT_B` · Sol `5081` (`1024×1024`) | Dom: `sand` (`41.4%`), Rock `31.9%`, Bedrock `23.6%`, Conf `0.764` | Dom: `bedrock` (`66.8%`), Sand `24.0%`, Conf `0.633` | Dom: `bedrock` (`42.9%`), Sand `38.6%`, Conf `0.818` | Dom: `bedrock` (`52.6%`), Sand `29.9%`, Conf `0.645` |
| `NRB_848386706EDR_F1260000CCAM05077M_` | **MSL (Curiosity)** · `NAV_RIGHT_B` · Sol `5079` (`1024×1024`) | Dom: `bedrock` (`43.5%`), Sand `40.0%`, Rock `16.0%`, Conf `0.796` | Dom: `bedrock` (`59.7%`), Sand `28.1%`, Conf `0.629` | Dom: `bedrock` (`45.4%`), Sand `31.8%`, Conf `0.836` | Dom: `bedrock` (`45.9%`), Sand `38.3%`, Conf `0.653` |

### Visual Comparisons on Unseen NASA Frames

| Perseverance `MCZ_LEFT` (Sol 2024) — Side-by-Side | Curiosity `NAV_RIGHT_B` (Sol 5079) — Side-by-Side |
|---|---|
| ![Perseverance MCZ_LEFT Side-by-Side](docs/validation/unseen_mars_imagery/comparisons/ZL0_2024_0846622583_145EBY_N0930000ZCAM10058_1100LMJ_side_by_side.png) | ![Curiosity NAV_RIGHT_B Side-by-Side](docs/validation/unseen_mars_imagery/comparisons/NRB_848386706EDR_F1260000CCAM05077M__side_by_side.png) |

**Cross-Model 4-Way Comparison — Curiosity `NAV_LEFT_B` (Sol 5081):**
![Curiosity All 4 Models](docs/validation/unseen_mars_imagery/comparisons/NLB_848553598EDR_F1260000CCAM01081M__all_4_models.png)

*Image Credit: NASA / JPL-Caltech / MSSS / ASU (public domain Martian raw imagery feeds).*

---

## Architecture & Project Structure

```text
MANGAL DRISHTI/
├── START_MANGAL_DRISHTI.bat          # Windows one-click dependency check, launcher & shutdown
├── LICENSE                           # MIT License (original code & docs)
├── THIRD_PARTY_NOTICES.md            # Attributions for AI4MARS, NASA, PyTorch, React, Font Awesome, etc.
├── configs/
│   └── data_config.yaml              # Pipeline, split, weighting & model configuration
├── src/
│   ├── data/                         # Dataset preprocessing, SCLK split verification & DataLoader
│   ├── models/                       # U-Net (ResNet34) & DeepLabV3+ (ResNet50)
│   ├── training/                     # AMP training loops, weighted CE/Dice loss & checkpointing
│   ├── evaluation/                   # Held-out 526-image evaluator, OOD MER analysis & benchmarks
│   ├── intelligence/                 # TerrainIntelligenceEngine, regions, candidates & PNG panels
│   └── api/main.py                   # FastAPI REST API + static artifact server (Port 8000)
├── frontend/                         # React 19 + TypeScript + Vite 8 + Tailwind CSS 4 + Anime.js v4 UI (Port 5173)
├── scripts/                          # Audit, PDF generator & NASA unseen imagery validation scripts
├── tests/                            # Pytest suites covering Step 2, Step 5 & Step 6 API
└── docs/
    ├── media/                        # High-resolution screenshots & animated GIF demonstrations
    ├── validation/unseen_mars_imagery/ # Leakage-checked unseen NASA frames, reports & comparisons
    └── release/                      # Audit JSON & MANGAL_DRISHTI_FINAL_INTEGRITY_REPORT.pdf
```

---

## Quick Start (Windows One-Click Launcher)

> **Prerequisites:** Windows 10/11, **Python 3.10+** (`python` in PATH or `.venv`), **Node.js 18+ / npm**.  
> **Checkpoints:** Trained `.pth` files (`experiments/deeplabv3plus/best_model.pth`, `experiments/unet/best_model.pth`, `experiments/evaluation/optimization/.../best_model.pth`) are excluded from Git tracking due to size. Historical reports, benchmarks, and UI remain browsable without them, while live inference requires local trained checkpoints under `experiments/`.

1. **Double-click** `START_MANGAL_DRISHTI.bat` (or run from Command Prompt / PowerShell):
   ```powershell
   cmd /c START_MANGAL_DRISHTI.bat
   ```
2. To run **preflight prerequisite & port diagnostics only** without launching servers:
   ```powershell
   cmd /c START_MANGAL_DRISHTI.bat --check
   ```
3. The launcher automatically verifies Python, Node/npm, `.venv`, Python packages, CUDA vs. CPU fallback, local checkpoints, `frontend/node_modules`, and ports `8000`/`5173`, then opens **`http://127.0.0.1:5173`**.
4. Press any key inside the launcher window when finished to cleanly terminate both background processes (`logs/` captures `launcher.log`, `backend.log`, and `frontend.log`).

---

## Manual Setup & Developer Commands

```powershell
# 1. Create and activate Python virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Install Python dependencies (PyTorch, FastAPI, Uvicorn, OpenCV, Pillow, ReportLab)
pip install -r requirements.txt fastapi uvicorn python-multipart reportlab playwright

# 3. Install frontend packages
cd frontend
npm install
cd ..

# 4. Run Backend API (http://127.0.0.1:8000)
.\.venv\Scripts\python.exe -m uvicorn src.api.main:app --host 127.0.0.1 --port 8000

# 5. In a second terminal, run Frontend UI (http://127.0.0.1:5173)
cd frontend
npm run dev -- --host 127.0.0.1 --port 5173
```

### Verification Commands

```powershell
# Run Pytest Unit & API Integration Suite (18 tests)
.\.venv\Scripts\python.exe -m pytest tests/test_step2_preprocessing.py tests/test_step5_intelligence.py tests/test_step6_api.py -v

# Verify Frontend Production TypeScript & Vite Bundle
cd frontend ; npm run build ; cd ..
```

---

## FastAPI REST Endpoints (`src/api/main.py`)

| Method & Route | Description |
|---|---|
| `GET /api/health` | Liveness check (`{"status": "ok"}`) |
| `GET /api/system/status` | Live device (`CUDA` / `CPU`), GPU VRAM, host RAM, loaded models & checkpoint inventory |
| `GET /api/models` | Ground-truth Combined, MSL, MER, Validation & Optimization benchmark metrics |
| `GET /api/reports` | List persisted Terrain Intelligence reports with summary & visual concern metadata |
| `GET /api/reports/{report_id}` | Retrieve full structured JSON analysis, regions, 2D candidates & artifact URLs |
| `GET /api/reports/{report_id}/download` | Download downloadable `intelligence_report.json` attachment |
| `POST /api/analyze` | Multipart rover image upload + selected model inference (`deeplabv3plus`, `unet`, `deeplabv3plus_optimized`, `unet_optimized`) |
| `GET /api/research` | Dataset taxonomy (`class_mapping`, `class_weights`, splits) & rendered research markdown docs |

---

## Troubleshooting

- **Port `8000` or `5173` conflict:** Stop conflicting Python/Node listeners (`Get-NetTCPConnection -LocalPort 8000,5173`) before running `START_MANGAL_DRISHTI.bat`.
- **CUDA unavailable / running on CPU:** Inference falls back cleanly to CPU without code changes (single-image DeepLabV3+ takes ~`673 ms` on CPU vs. ~`24 ms` GPU FP16). Ensure CUDA-enabled PyTorch matches your NVIDIA driver if GPU acceleration is desired.
- **`matplotlib` Smart App Control block on Windows:** Keep `matplotlib>=3.9.0,<3.11.0` as pinned in `requirements.txt`.
- **Missing `.pth` checkpoints:** Only historical evaluation metrics, benchmarks, and existing intelligence reports display until checkpoints are restored locally under `experiments/`.

---

## License & Third-Party Notices

- **Original Code & Documentation:** Released under the [MIT License](LICENSE) — Copyright © 2026 **Dharm Patel (DDharm007)**.
- **Datasets, Pretrained Weights & Third-Party Libraries:** Governed by their respective licenses and NASA open data policies; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for complete attributions.
