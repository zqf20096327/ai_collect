<p align="center">
  <img src="assets/matryoshka_compressm.png" width="600" alt="CompreSSM">
</p>

<h1 align="center">CompreSSM</h1>

<p align="center">
  <b>The Curious Case of In-Training Compression of State Space Models</b><br>
  <a href="https://arxiv.org/abs/2510.02823">Paper</a> • ICLR 2026 • <a href="https://github.com/phnazari/compreSSMamba">Mamba Experiments</a>
</p>

<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python 3.10+"></a>
  <a href="https://github.com/google/jax"><img src="https://img.shields.io/badge/JAX-0.4+-green.svg" alt="JAX"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
</p>

---

This is the main repository accompanying the ICLR 2026 paper [The Curious Case of In-Training Compression of State Space Models](https://arxiv.org/abs/2510.02823). It contains the LRU experiments. The Mamba experiments are available in the [CompreSSMamba](https://github.com/phnazari/compreSSMamba) repository.

<p align="center">
    <small><i>Note: This code has undergone heavy refactoring for public release. If you encounter any issues, please help us clean up by raising them.</i></small>
</p>

---

State Space Models (SSMs) offer parallelizable training and fast inference for long sequence modeling. At their core are recurrent dynamical systems with update costs scaling with state dimension. **CompreSSM** applies balanced truncation (a classical control-theoretic technique) *during training* to identify and remove low-influence states based on their Hankel singular values. Models that begin large and shrink during training achieve computational efficiency while maintaining higher performance than models trained directly at smaller dimension.

---

## Installation

```bash
git clone https://github.com/camail-official/compressm.git
cd compressm
conda env create -f environment.yaml
conda activate compressm
```


## Data Preparation

MNIST and CIFAR-10 auto-download into `data/` on first run. The four LRA datasets (ListOps, IMDB, AAN, Pathfinder) must be manually downloaded from the [Long Range Arena repository](https://github.com/google-research/long-range-arena) and placed under `data/lra_release/`:
```
data/lra_release/
  listops/          # basic_train.tsv, basic_val.tsv, basic_test.tsv
  aan/               # new_aan_pairs.{train,eval,test}.tsv
  pathfinder/
    pathfinder32/    # curv_baseline/ with metadata .npy files
```

IMDB is downloaded and cached automatically via the `datasets` library on first run.

**Note on Pathfinder:** For faster loading, you can preprocess Pathfinder into a single `.npz` file:
```bash
python scripts/preprocess_pathfinder.py --data-dir data/lra_release/pathfinder/pathfinder32 --resolution 32
```

## Quick Start

```bash
# Train baseline (no compression)
python scripts/train.py --config configs/smnist/default.yaml --seed 42

# Train with in-training compression (tol=0.01)
python scripts/train.py --config configs/smnist/default.yaml \
    --mode tolerance --tol 0.01 --seed 42
```

## Experiment Configurations

All configurations needed to reproduce the paper experiments live under `configs/`:

```
configs/
├── smnist/
│   ├── default.yaml              # sMNIST baseline (mode: none)
│   ├── pragmatic.yaml            # Pragmatic variant (Appendix C.4)
│   └── ablations/
│       ├── selection_largest.yaml    # BT sanity check (Appendix D.1)
│       ├── selection_random.yaml
│       ├── selection_smallest.yaml
│       ├── num_reductions_1.yaml     # Num. reductions ablation (Appendix D.2)
│       ├── num_reductions_2.yaml
│       ├── num_reductions_4.yaml
│       ├── num_reductions_8.yaml
│       ├── num_reductions_16.yaml
│       ├── window_0k.yaml            # Reduction window ablation (Appendix D.3)
│       ├── window_25k.yaml
│       ├── window_50k.yaml
│       ├── window_100k.yaml
│       └── window_150k.yaml
├── scifar/
│   ├── default.yaml              # sCIFAR baseline
│   └── pragmatic.yaml            # Pragmatic variant
├── listops/
│   └── default.yaml              # ListOps baseline
├── imdb/
│   └── default.yaml              # IMDB baseline
├── aan/
│   └── default.yaml              # AAN baseline
└── pathfinder/
    └── default.yaml              # Pathfinder baseline
```

## Running Experiments

### Baselines (no reduction)

```bash
python scripts/train.py --config configs/smnist/default.yaml --seed 42
python scripts/train.py --config configs/scifar/default.yaml --seed 42
python scripts/train.py --config configs/listops/default.yaml --seed 42
python scripts/train.py --config configs/imdb/default.yaml --seed 42
python scripts/train.py --config configs/aan/default.yaml --seed 42
python scripts/train.py --config configs/pathfinder/default.yaml --seed 42
```

### Tolerance-Based Reduction (Table 1)

Use the default config as a base and override `--mode tolerance --tol <value>`:

**sMNIST** tolerance values: {0.04, 0.02, 0.01, 0.005, 0.002, 0.001}



```bash
# Example: sMNIST with tol=0.01
python scripts/train.py --config configs/smnist/default.yaml \
    --mode tolerance --tol 0.01 --seed 42
```

**LRA tasks** (sCIFAR, ListOps, IMDB, AAN, Pathfinder) tolerance values: {0.15,  0.10, 0.07, 0.05, 0.03, 0.02}

```bash
# Example: sCIFAR with tol=0.05
python scripts/train.py --config configs/scifar/default.yaml \
    --mode tolerance --tol 0.05 --seed 42
```

### Pragmatic Variant (Appendix C.4)

The pragmatic approach uses fixed 10% reduction with automatic rollback:

```bash
python scripts/train.py --config configs/smnist/pragmatic.yaml --seed 42
python scripts/train.py --config configs/scifar/pragmatic.yaml --seed 42
```

### Ablations (Appendix D)

All ablations are on sMNIST (256 → 32 states, 200k steps):

```bash
# D.1 — HSV selection scheme
python scripts/train.py --config configs/smnist/ablations/selection_largest.yaml --seed 42
python scripts/train.py --config configs/smnist/ablations/selection_random.yaml --seed 42
python scripts/train.py --config configs/smnist/ablations/selection_smallest.yaml --seed 42

# D.2 — Number of reduction steps (R = 1, 2, 4, 8, 16)
python scripts/train.py --config configs/smnist/ablations/num_reductions_4.yaml --seed 42

# D.3 — Reduction window timing
python scripts/train.py --config configs/smnist/ablations/window_0k.yaml --seed 42
python scripts/train.py --config configs/smnist/ablations/window_150k.yaml --seed 42
```

### Full Paper Reproduction

Use `reproduce.py` for multi-seed sweeps:

```bash
# Single experiment, multiple seeds
python scripts/reproduce.py configs/smnist/default.yaml \
    --seeds 8 42 123 456 789 101 202 303 404 505 --gpu 0

# Tolerance sweep
python scripts/reproduce.py configs/scifar/default.yaml \
    --seeds 8 42 123 456 789 --gpu 0 \
    -- --mode tolerance --tol 0.05

# Dry run (preview commands)
python scripts/reproduce.py configs/smnist/default.yaml \
    --seeds 42 --dry-run

# List all canonical paper experiments
python scripts/reproduce.py --list
```

### Seed Conventions

| Dataset    | Seeds |
|------------|-------|
| sMNIST     | 10 seeds: 8, 42, 123, 456, 789, 101, 202, 303, 404, 505 |
| LRA tasks  | 5 seeds: 8, 42, 123, 456, 789 |

### Expected Results (Table 1)

Top-3 mean accuracy across seeds:

### Main Datasets (CIFAR10, ListOps, AAN, IMDB, Pathfinder)

| Dataset | Metric | tol = 0.15 | tol = 0.10 | tol = 0.07 | tol = 0.05 | tol = 0.03 | tol = 0.02 | tol = 0 (Baseline) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **CIFAR10** | State dim | 57.4 ± 1.5 | 92.6 ± 4.2 | 126.0 ± 4.0 | 160.8 ± 5.4 | 213.6 ± 6.1 | 327.2 ± 16.0 | 384 |
| | CompreSSM | **84.4 ± 0.2** | **85.7 ± 0.1** | **86.0 ± 0.1** | **85.8 ± 0.1** | **86.0 ± 0.2** | **86.1 ± 0.2** | - |
| | Baseline | 78.2 ± 0.7 | 81.8 ± 0.3 | 83.7 ± 0.2 | 84.2 ± 0.5 | 84.9 ± 0.0 | 86.0 ± 0.1 | 86.5 ± 0.3 |
| **ListOps** | State dim | 56.8 ± 3.4 | 81.8 ± 4.9 | 109.8 ± 3.9 | 135.4 ± 6.8 | 167.6 ± 5.7 | 213.8 ± 28.0 | 256 |
| | CompreSSM | **48.3 ± 0.7** | **51.8 ± 0.9** | 48.2 ± 1.1 | 47.5 ± 1.6 | **49.2 ± 0.3** | 47.1 ± 1.4 | - |
| | Baseline | 43.4 ± 0.4 | 46.3 ± 0.5 | **49.4 ± 1.8** | **49.2 ± 0.7** | 48.2 ± 2.1 | **47.6 ± 1.7** | 49.7 ± 0.8 |
| **AAN** | State dim | 53.6 ± 1.9 | 84.4 ± 1.4 | 111.0 ± 2.0 | 136.6 ± 2.9 | 170.0 ± 2.4 | 203.2 ± 13.7 | 256 |
| | CompreSSM | 87.2 ± 0.3 | 87.5 ± 0.1 | 87.4 ± 0.3 | 87.2 ± 0.0 | 87.6 ± 0.3 | 87.9 ± 0.2 | - |
| | Baseline | **87.5 ± 0.3** | **87.9 ± 0.3** | **87.8 ± 0.2** | **87.8 ± 0.5** | **87.3 ± 0.4** | 87.4 ± 0.5 | **87.3 ± 0.3** |
| **IMDB** | State dim | 95.0 ± 2.3 | 119.6 ± 2.2 | 136.8 ± 1.9 | 150.4 ± 1.2 | 165.0 ± 1.3 | 192.0 ± 0.0 | 192.0 |
| | CompreSSM | 82.2 ± 0.2 | 82.8 ± 0.1 | 83.7 ± 0.4 | 83.8 ± 0.3 | 84.1 ± 0.4 | 84.4 ± 0.2 | - |
| | Baseline | **82.7 ± 0.1** | **83.5 ± 0.1** | **83.7 ± 0.0** | **84.0 ± 0.4** | **84.3 ± 0.0** | **84.5 ± 0.1** | 84.7 ± 0.1 |
| **Pathfinder** | State dim | 34.6 ± 1.9 | 51.2 ± 1.7 | 65.6 ± 2.3 | 81.2 ± 1.6 | 105.0 ± 2.1 | 129.8 ± 5.2 | 256 |
| | CompreSSM | 96.6 ± 1.3 | **97.9 ± 0.1** | 97.6 ± 0.5 | 97.8 ± 0.4 | 98.0 ± 0.0 | 98.0 ± 0.1 | - |
| | Baseline | **97.3 ± 0.2** | **97.9 ± 0.1** | **98.0 ± 0.1** | **98.1 ± 0.0** | **98.2 ± 0.0** | **98.1 ± 0.1** | 98.3 ± 0.1 |

---

### sMNIST Performance

| Dataset | Metric | tol = 0.04 | tol = 0.02 | tol = 0.01 | tol = 0.005 | tol = 0.002 | tol = 0.001 | tol = 0 (Baseline) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **sMNIST** | State dim | 12.7 ± 3.0 | 27.6 ± 1.8 | 46.8 ± 3.2 | 76.3 ± 7.5 | 148.1 ± 9.8 | 191.4 ± 4.7 | 256 |
| | CompreSSM | **95.9 ± 0.2** | **96.9 ± 0.0** | **96.9 ± 0.1** | **96.9 ± 0.1** | 97.0 ± 0.1 | **97.2 ± 0.3** | - |
| | Baseline | 92.6 ± 0.5 | 96.0 ± 0.2 | 95.9 ± 0.1 | 96.4 ± 0.2 | **97.3 ± 0.2** | **97.3 ± 0.1** | 97.3 ± 0.1 |tba

## Code Structure

```
compressm/
├── models/lru.py                  # LRU model with in-training reduction support
├── reduction/
│   ├── hsv.py                     # Hankel singular value computation
│   └── balanced_truncation.py     # Balanced truncation algorithm
├── training/
│   ├── trainer.py                 # Training loop with compression modes
│   └── utils.py                   # Training utilities
└── data/
    ├── datasets.py                # sMNIST, sCIFAR, ListOps, IMDB, AAN, Pathfinder
    └── dataloaders.py             # Data loading and batching

configs/
├── {smnist,scifar,listops,imdb,aan,pathfinder}/
│   └── default.yaml               # Paper hyperparameters per dataset
├── {smnist,scifar}/pragmatic.yaml  # Pragmatic variant configs
└── smnist/ablations/               # 13 ablation configs (Appendix D)

scripts/
├── train.py                       # Training CLI
├── reproduce.py                   # Multi-seed reproduction (--list for all experiments)
├── analyse_results.py             # Results aggregation
├── preprocess_pathfinder.py       # Pathfinder .npz preprocessing
└── smoke_test.py                  # Quick validation of all datasets
```

## Config Key Reference

| Key | Description |
|-----|-------------|
| `model.state_dim` | State space dimension (n) — what gets reduced |
| `model.hidden_dim` | Hidden/embedding dimension (h) |
| `reduction.mode` | `none` / `tolerance` / `fixed` / `pragmatic` |
| `reduction.tol` | Fraction of Hankel energy to discard (tolerance mode) |
| `reduction.selection` | `largest` (default) / `smallest` / `random` |
| `reduction.red_start` | Step to begin reductions |
| `reduction.red_end` | Step to stop reductions |
| `reduction.red_interval` | Steps between reduction checks |
| `reduction.reduction_fraction` | Fraction to remove per step (fixed/pragmatic) |
| `reduction.performance_tolerance` | Max accuracy drop for rollback (pragmatic) |

## Citation

We kindly invite you to cite our work if you enjoy this repo:

```bibtex
@misc{chahine2026curiouscaseintrainingcompression,
      title={The Curious Case of In-Training Compression of State Space Models}, 
      author={Makram Chahine and Philipp Nazari and Daniela Rus and T. Konstantin Rusch},
      year={2026},
      eprint={2510.02823},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2510.02823}, 
}
```

## License

MIT License - see [LICENSE](LICENSE) for details.
