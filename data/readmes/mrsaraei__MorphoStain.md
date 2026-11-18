# MorphoStain

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![PyTorch 2.0+](https://img.shields.io/badge/PyTorch-2.0%2B-ee4c2c.svg)](https://pytorch.org/)

**MorphoStain: Physics-Guided Latent Diffusion and Morphological Distillation for Multiplex Stain Decomposition in Alzheimer's Neuropathology**

https://github.com/user-attachments/assets/413a3bd9-4f64-4955-af1e-22ba5e63453c

MorphoStain is an unsupervised, physics-guided deep learning framework designed to resolve the mathematically ill-posed problem of unmixing co-localized biomarkers that share identical chromogenic spectra—specifically dual-DAB staining of Amyloid-β (6E10) plaques and phosphorylated Tau (AT8) tangles in Alzheimer's disease whole-slide images (WSIs).

---

## ✨ Key Highlights

- **Physics-Guided Latent Diffusion Teacher:** Couples an analytical Beer–Lambert optical density (OD) projection (*S*<sub>AD</sub> ∈ ℝ<sup>3×2</sup>) with a conditional Latent UNet guided by frozen self-supervised pathology embeddings from the **Phikon** Vision Transformer.
- **Monte Carlo Epistemic Uncertainty:** Synthesizes multi-realization concentration ensembles via 5-step deterministic reverse diffusion to quantify pixel-wise decomposition ambiguity (*u*<sub>var</sub>).
- **Ultra-Fast Student Distillation (>1,400× Compression):** Compresses the 169.67M-parameter teacher pipeline into a lightweight **0.12M-parameter `FastStudentUNet`** utilizing parallel multi-scale dilated convolutions (*d* ∈ {1, 2, 4, 8}) for gridding-free, real-time clinical inference (**140.1 FPS**).
- **Symmetric Morphological Routing (*M*<sub>attn</sub>):** Dynamically disentangles shared brown DAB absorption into pure Amyloid-β and Tau channels using chromatic selectivity gates and spatial Gaussian smoothing (15 × 15, σ = 3.5) without requiring pixel-level annotations.
- **Clinical-Grade Desktop GUI:** Includes a standalone `PyQt6` interactive visual suite with asynchronous GPU/MPS/CPU execution and live uncertainty dynamic range calibration.

---

## 📂 Repository Structure

    MorphoStain/
    ├── dataDownloader.py            # Phase 0A: Streams SEA-AD WSIs from public AWS S3 bucket & runs QC
    ├── dataPatchifier.py            # Phase 0B: Level-0 512x512 tiling & flat-field background calibration
    ├── dataSplitter.py              # Phase 0C: Strict donor-isolated Train / Val / Test splitting
    ├── cacheLatent.py               # Phase 1: Extracts & caches SD-VAE latents and Phikon ViT features (.h5)
    ├── teacherDiffusion.py          # Phase 2: Trains physics-guided Latent Diffusion Teacher (M1-M4 variants)
    ├── monteCarlo.py                # Phase 3: Generates 5-step Monte Carlo pseudo-label & uncertainty targets
    ├── studentDistillation.py       # Phase 4: Trains FastStudentUNet with symmetric morphological routing
    ├── trainInverseAE.py            # SOTA Baseline: Trains unsupervised InverseAE (MIDL) model
    ├── evaluateBaselines.py         # Phase 5A: Full benchmark across 9,908 test patches (8 methods)
    ├── evaluateAblation.py          # Phase 5C: Architectural ablation study (M1-M4 Teachers vs. Student)
    ├── generateFigures.py           # Phase 6A: Generates qualitative unmixing, PSNR KDE, & convergence plots
    ├── visualizeChannels.py         # Phase 6B: Multi-patch morphological routing & stain split visualizer
    ├── compareDisentanglement.py    # Phase 6D: Biomarker disentanglement teaser (MorphoStain vs. InverseAE)
    ├── subgroupFailuresAnalysis.py  # Phase 7: Pathological burden subgroup metrics & failure mode diagnostics
    ├── categoryAnalysis.py          # Balanced Cohort Evaluation (Equal Amyloid-Beta vs. Tau AT8 analysis)
    ├── generateWSIPlot.py           # Phase 8A: Macro-scale gigapixel WSI stitching & uncertainty mapping
    ├── generateErrorMap.py          # Phase 8D: High-resolution pixel-wise MSE reconstruction heatmaps
    ├── robustnessAnalysis.py        # Phase 8E: Additive Gaussian sensor noise perturbation benchmark
    ├── zeroShotEvaluation.py        # Phase 8F-1: Multi-seed zero-shot OOD evaluation & Pareto frontier
    ├── HER2externalValidation.py    # Phase 8F-2: Cross-tissue zero-shot transfer on breast cancer HER2 IHC
    ├── multiDomainShift.py          # Phase 8G: Scanner illumination & gamma domain shift benchmark
    ├── benchmarkStats.py            # Phase 8H: Paired t-test, Wilcoxon, Mann-Whitney U, & Cohen's d suite
    ├── generateReliabilityPlot.py   # Phase 9: Empirical uncertainty calibration & ECE reliability diagram
    ├── hyperparameterSensitivity.py # Supplementary sensitivity analysis for overlap weight (lambda_ov)
    ├── MorphoStain.py               # Interactive PyQt6 Clinical Demonstration GUI
    └── results/                     # Output directory for checkpoints (.pth), metrics (.csv), & figures (.pdf)

---

## ⚙️ Installation & Requirements

1. **Clone the repository:**

       git clone [https://github.com/mrsaraei/MorphoStain.git](https://github.com/mrsaraei/MorphoStain.git)
       cd MorphoStain

2. **Create a Conda environment and install dependencies:**

       conda create -n morphostain python=3.10 -y
       conda activate morphostain

       # Install PyTorch (adjust CUDA version as needed for your system)
       pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

       # Install core scientific, pathology, and deep learning packages
       pip install numpy pandas scipy scikit-image opencv-python-headless matplotlib seaborn
       pip install h5py tqdm pillow openslide-python boto3
       pip install diffusers transformers lpips PyQt6

*(Note: Ensure the system-level `openslide` library is installed on your OS, e.g., `apt-get install openslide-tools` on Ubuntu or `brew install openslide` on macOS).*

---

## 🚀 End-to-End Pipeline Execution

### Step 1: Data Ingestion, Tiling, and Donor-Level Splitting
Download paired Amyloid-β (6E10) and Tau (AT8) middle temporal gyrus (MTG) whole-slide images from the public SEA-AD S3 bucket, extract 512 × 512 Level-0 patches, and isolate donors into training (`H20.33.001`, `H20.33.002`, `H20.33.005`), validation (`H19.33.004`), and testing (`H20.33.004`) splits:

    python dataDownloader.py
    python dataPatchifier.py
    python dataSplitter.py

### Step 2: Dual Latent & Foundation Feature Caching (Phase 1)
Pre-extract frozen `stabilityai/sd-vae-ft-mse` latents and `owkin/phikon` ViT semantic conditioning vectors into high-speed HDF5 containers (`latent_train.h5`, `latent_val.h5`, `latent_test.h5`):

    python cacheLatent.py

### Step 3: Physics-Guided Teacher Diffusion & Monte Carlo Sampling (Phases 2 & 3)
Train the conditional Latent UNet teacher model (*M*<sub>1</sub>) and ablation variants (*M*<sub>2</sub>–*M*<sub>4</sub>), then synthesize 5-step reverse diffusion pseudo-labels (`pseudo_labels_train.h5`):

    # Train primary MorphoStain Teacher (M1)
    python teacherDiffusion.py --run_name M1_MorphoStain --lambda_inv 0.5 --lambda_ov 0.1

    # Optional: Train Ablation Variants (M2-M4)
    python teacherDiffusion.py --run_name M2_NoPhikon --disable_phikon
    python teacherDiffusion.py --run_name M3_NoPhysics --lambda_inv 0.0 --lambda_ov 0.0
    python teacherDiffusion.py --run_name M4_NoOverlap --lambda_ov 0.0

    # Generate Monte Carlo mean concentration & epistemic variance targets
    python monteCarlo.py

### Step 4: Fast Student Knowledge Distillation (Phase 4)
Train the lightweight `FastStudentUNet` with Beer–Lambert physical reconstruction, empirical MSE uncertainty calibration, and symmetric morphological routing:

    python studentDistillation.py

The trained weights are saved to `/workspace/results/best_student.pth`.

### Step 5: Quantitative Benchmarking & Statistical Verification (Phases 5–9)
Train the SOTA baseline (`InverseAE`) and run the complete evaluation suite:

    # 1. Train SOTA Deep Baseline (InverseAE)
    python trainInverseAE.py

    # 2. Main Test Set Benchmark (N = 9,908 patches, 8 unmixing methods)
    python evaluateBaselines.py

    # 3. Parametric & Non-Parametric Hypothesis Testing (Paired t-test, Wilcoxon, Cohen's d)
    python benchmarkStats.py

    # 4. Architectural Ablation Study (Table II)
    python evaluateAblation.py

    # 5. Balanced Cohort & Pathological Subgroup Evaluations
    python categoryAnalysis.py
    python subgroupFailuresAnalysis.py

    # 6. Out-of-Distribution (OOD) Zero-Shot & Cross-Tissue Generalization (HER2)
    python zeroShotEvaluation.py
    python HER2externalValidation.py

    # 7. Illumination Domain Shift & Sensor Noise Perturbation Benchmarks
    python multiDomainShift.py
    python robustnessAnalysis.py

---

## 🖥️ Interactive Clinical GUI (`MorphoStain.py`)

Launch the real-time `PyQt6` desktop visualization suite to inspect and unmix specimen patches interactively:

    python MorphoStain.py

- **Hardware Acceleration:** Automatically detects and toggles between `CUDA (GPU)`, `MPS (Apple Silicon GPU)`, and `CPU (Optimized SIMD)`.
- **Multi-Patch Queue & Batch Execution:** Upload single or multiple histopathology patches simultaneously, navigate seamlessly with instant result caching (`◀ Prev` / `Next ▶`), or trigger automated sequential batch processing (`Run All Queue Sequentially`).
- **Automated Regimen & Burden Profiling:** Dynamically computes the quantitative DAB biomarker split (`Aβ % / Tau %`) and automatically classifies the specimen's staining regimen (`Amyloid-β (6E10) + HTX`, `Tau (AT8) + HTX`, or `Co-Localized`).
- **Live Reconstruction Diagnostics:** Computes real-time full-reference fidelity and throughput metrics, including PSNR, SSIM, MSE, RMSE, Cosine Similarity, LPIPS, and FPS.
- **Calibrated Epistemic Uncertainty Viewport:** Renders background-suppressed, tissue-gated uncertainty maps (*u*<sub>var</sub>) paired with an aligned scientific-notation colorbar and an interactive percentile slider (default: 100.0%) to highlight localized optical defocus and boundary artifacts.

---

## 📊 Summary of Quantitative Results

Evaluated across ***N* = 9,908 held-out test patches** from the SEA-AD cohort (Batch Size *B* = 1 on a single NVIDIA RTX 6000 Ada GPU):

| Method | PSNR (dB) ↑ | SSIM ↑ | MSE ↓ | RMSE ↓ | Cosine Sim ↑ | LPIPS ↓ | Throughput (FPS) ↑ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **MorphoStain (Ours)** | **40.56** | **0.9961** | **9.092 × 10⁻⁵** | **0.0095** | **0.9999** | 0.0141 | 140.1 |
| InverseAE (SOTA) | 38.84 | 0.9934 | 1.349 × 10⁻⁴ | 0.0115 | 0.9999 | 0.0150 | **197.2** |
| NMF | 35.39 | 0.9927 | 2.904 × 10⁻⁴ | 0.0170 | 0.9999 | **0.0140** | 16.9 |
| Ruifrok & Johnston | 34.06 | 0.9896 | 4.079 × 10⁻⁴ | 0.0200 | 0.9997 | 0.0499 | 18.8 |
| Macenko *et al.* | 32.37 | 0.9880 | 5.821 × 10⁻⁴ | 0.0241 | 0.9999 | 0.0165 | 17.4 |
| Sparse NMF | 25.64 | 0.9448 | 2.736 × 10⁻³ | 0.0523 | 0.9995 | 0.0743 | 16.1 |
| Vahadane *et al.* | 21.40 | 0.8153 | 7.260 × 10⁻³ | 0.0851 | 0.9987 | 0.1485 | 14.5 |
| LassoReg | 18.37 | 0.5425 | 1.466 × 10⁻² | 0.1209 | 0.9971 | 0.2971 | 16.7 |

- **Statistical Significance:** Paired *t*-test and Wilcoxon signed-rank test confirm *p* < 10<sup>−16</sup> across all baselines, with Cohen's *d* = 3.52 vs. InverseAE and *d* = 7.02 vs. NMF.
- **Uncertainty Calibration:** Expected Calibration Error (**ECE**) of **0.0125**.

---
## 📖 Citation

If you find MorphoStain useful in your research, please cite our paper:

```bibtex
@article{saraei2026morphostain,
  author       = {Saraei, Mohammadreza and Zand, Maryam and Rahmani, Saba},
  title        = {MorphoStain: Physics-Guided Latent Diffusion and Morphological Distillation for Multiplex Stain Decomposition in Alzheimer's Neuropathology},
  journal      = {medRxiv},
  year         = {2026},
  elocation-id = {2026.11.15.26368147},
  doi          = {10.64898/2026.11.15.26368147},
  url          = {https://doi.org/10.64898/2026.11.15.26368147}
}

---


## 🙏 Acknowledgments & Data Availability

Whole-slide neuropathological imaging data were provided by the **Seattle Alzheimer's Disease Brain Cell Atlas (SEA-AD)** consortium (accessible via the [SEA-AD Data Portal](https://portal.brain-map.org/explore/seattle-alzheimers-disease) and the AWS Open Data Registry at `s3://sea-ad-quantitative-neuropathology/`; Gabitto et al., 2024). We obtained external breast cancer HER2 IHC validation data from the **Breast Cancer Immunohistochemical Image Generation (BCI) Challenge** benchmark dataset (available at [bci.grand-challenge.org](http://bci.grand-challenge.org/); Liu et al., 2022).

## 📝 License

This project is licensed under the MIT License — see the `LICENSE` file for details.
