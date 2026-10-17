# Machine Fault Recognition

> Audio-based classification of machine health states across three machine types - a lightweight CNN that hears whether a machine is healthy or faulty.

<p align="center">
  <a href="https://huggingface.co/spaces/antonious28/machine_fault_recognition">
    <img alt="Live Demo" src="https://img.shields.io/badge/%F0%9F%A4%97%20Demo-Hugging%20Face%20Spaces-yellow">
  </a>
  <img alt="Python" src="https://img.shields.io/badge/python-3.13-blue">
  <img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-2.2%2B-ee4c2c">
  <img alt="Test Accuracy" src="https://img.shields.io/badge/test%20acc-91.9%25-brightgreen">
  <img alt="Balanced Accuracy" src="https://img.shields.io/badge/balanced%20acc-82.0%25-green">
  <img alt="Parameters" src="https://img.shields.io/badge/params-0.24M-informational">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-blue">
</p>

**[▶ Try the live demo on Hugging Face Spaces](https://huggingface.co/spaces/antonious28/machine_fault_recognition)** &nbsp;·&nbsp; **[📄 Read the full report (PDF)](docs/Report.pdf)**

---

## Problem & Dataset

**Domain.** Acoustic _machine condition monitoring_ for predictive maintenance - given a short clip recorded near a running machine, decide whether it is operating normally or exhibiting a fault. Acoustic monitoring is attractive because a single non-contact microphone captures the full vibrational signature of the equipment, making it cheap to deploy at scale on factory floors.

**Task.** A supervised **6-way classification** over `{machine type} × {health state}`: three industrial machines (M1, M2, M3), each with a _Normal_ and _Abnormal_ class. This is a closed-set re-framing of the broader _Anomalous Sound Detection_ problem - the same setup popularised by the **DCASE Challenge Task 2** series (DCASE 2020 / 2022 / 2023) and the **MIMII / MIMII-DG** datasets, but here the labels are known at training time.

| Property         | Value                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------------- |
| Files            | **56,236** WAV clips (~54 GB)                                                               |
| Format           | PCM 16-bit mono, **48 kHz**                                                                 |
| Duration         | 11.0 s (M1, M2), 10.0 s (M3)                                                                |
| Class balance    | ≈ **5 : 1** Normal : Abnormal                                                               |
| Hidden structure | Multiple recording **sections** per machine (different mics / units / operating conditions) |

**Why it's hard.** The fault signature lives in _fine spectro-temporal detail_ (transient timing for M2, harmonic smearing for M3, broadband shifts of 1–3 dB for M1), so global summary statistics don't separate Normal from Abnormal. Worse, each machine was recorded across multiple **sections** that look acoustically distinct (cosine similarity as low as **0.27** between M2 sections). A naive random split lets the model memorise section fingerprints - an early version reached F1 ≈ 0.999 purely from leakage. Honest, section-disjoint splits are what made the 91.9% / 82.0% headline numbers meaningful.

**Reference.** Koizumi et al., _“Description and Discussion on DCASE2020 Challenge Task 2: Unsupervised Detection of Anomalous Sounds for Machine Condition Monitoring,”_ DCASE 2020 - the foundational paper for this problem framing (cited in the project report).

---

## Highlights

- **0.24M parameters** - a 4-block CNN small enough for edge deployment, trained from scratch.
- **PCEN features** - Per-Channel Energy Normalisation in front of a log-mel pipeline, robust to gain drift.
- **Frequency-MixStyle** - cross-section domain generalisation; mixes per-(channel,freq) statistics across batch partners drawn from the same class but a different recording section.
- **Hybrid factored head** - a plain 6-way FC head for inference, plus auxiliary factored heads (machine + per-machine health) used _only at training time_ as a regulariser.
- **Reproducible pipeline** - feature cache → cluster-aware split → train → infer, all scripted; Docker image included.

## Classes

| Label | Machine | Health   |
| :---: | :-----: | :------- |
|   0   |   M1    | Normal   |
|   1   |   M1    | Abnormal |
|   2   |   M2    | Normal   |
|   3   |   M2    | Abnormal |
|   4   |   M3    | Normal   |
|   5   |   M3    | Abnormal |

## Results

| Metric            |       Value        |
| ----------------- | :----------------: |
| Test Accuracy     |     **91.9%**      |
| Balanced Accuracy |     **82.0%**      |
| Parameters        |       0.24M        |
| Inference (CPU)   | ~tens of ms / clip |

See `docs/Report.pdf` for ablations (PCEN vs log-mel, FreqMixStyle on/off, plain vs factored head) and full per-class breakdowns.

## Architecture

`SmallCNNFactored` - defined in [`src/models.py`](src/models.py). Inference uses only the plain 6-way FC head; the factored heads are dropped after training.

<p align="center">
  <img src="figures/architecture.svg" alt="Model architecture diagram" width="78%">
  <br>
  <em>Model architecture (SmallCNNFactored).</em>
</p>

## Why this dataset is hard

Each machine is recorded across multiple **sections** (operating conditions / locations / mics). A naive split leaks section identity and overstates accuracy. We cluster log-mel spectra to discover sections, then build a **section-disjoint hybrid split**: train on some sections, evaluate on held-out ones. This is what the model actually generalises to.

<p align="center">
  <img src="figures/cluster_visualization.png" alt="PCA cluster visualization per machine/health" width="78%">
  <br>
  <em>PCA per machine/health - silhouette-validated clusters reveal latent recording sections.</em>
</p>

<p align="center">
  <img src="figures/train_vs_unseen_gap.png" alt="Train vs unseen sections in PCA space" width="78%">
  <br>
  <em>Held-out sections (red) live in different regions of feature space than train sections (blue) - the gap the model must close.</em>
</p>

<p align="center">
  <img src="figures/split_counts.png" alt="Per-machine train/val/test counts" width="78%">
  <br>
  <em>Final per-machine split sizes (Normal stacked, Abnormal on top).</em>
</p>

## Pipeline

```
1. precompute.py    - Cache PCEN + log-mel features from WAV files
2. splits.py        - Discover sections (clustering), assign train/val/test
3. audit_splits.py  - Sanity-check the split (leakage, class balance)
4. train_cnn.py     - Train SmallCNNFactored
5. infer.py         - Run inference on new WAV files
```

<p align="center">
  <img src="figures/pipeline.svg" alt="Processing pipeline diagram" width="78%">
  <br>
  <em>Processing pipeline: feature cache → split → train → infer.</em>
</p>

## Quick Start

### Inference (Docker - easiest)

```bash
./run.sh <wav_folder> <results_folder>
```

The helper builds the image on first run, then mounts your folders. Outputs:

- `results.txt` — one predicted class index (0–5) per file, in filename-numeric order
- `time.txt` — per-file inference time in seconds

### Inference (Python)

```bash
pip install -r requirements.txt
python infer.py --data <wav_folder> --out results/
```

Defaults to `models/final.pt`. Override with `--model <path>`.

### Training

```bash
# 1. Precompute features
python precompute.py

# 2. Generate cluster-aware splits
python splits.py --mode hybrid

# 3. Train
python train_cnn.py --model small_cnn_factored --epochs 25 --variant B \
    --class-weight-cap 1.0 --select-metric val_bal_acc \
    --fms-prob 0.5 --fms-alpha 0.1 \
    --ckpt-path "models/final.pt"
```
