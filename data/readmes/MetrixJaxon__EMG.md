# Energy-Modulated Gain (EMG): A Sufficient-Statistic Approach to Automatic Modulation Recognition

This repository contains the official PyTorch implementation of the paper

> **Energy-Modulated Gain: A Sufficient-Statistic Approach to Automatic Modulation Recognition**
> *IEEE Transactions on Wireless Communications* (under review).

We revisit automatic modulation recognition (AMR) from the perspective of **sufficient statistics**. Under additive white Gaussian noise, the class-conditional likelihood of a received IQ block factors as a *class-independent* energy term times a class-dependent shape distribution that takes the closed form of a **von Mises–Fisher (vMF) mixture** on the unit hypersphere. The mixture's concentration parameter is **proportional to the signal energy**, which the conventional per-sample IQ normalization step discards. We prove (Theorem 1) that the normalized-IQ vector is therefore *not* a sufficient statistic for the modulation class, and we identify three structural requirements—**non-negativity, monotonicity, multiplicative coupling**—that any energy-injection mechanism must satisfy in order to reintroduce this discarded information consistently with the vMF density.

We translate these requirements into **Energy-Modulated Gain (EMG)**, a lightweight conditional-normalization layer that standardizes intermediate features and reintroduces the standardized log-energy as a learned non-negative multiplicative scale. Integrated into a multi-scale dilated residual backbone (**EMGNet**), EMG achieves **65.70 % / 65.60 % / 80.98 %** overall accuracy on **RML2016.10a / RML2018.01a / HisarMod2019** as reported in the paper, surpassing the strongest reproduced baseline (IQFormer) by **1.36 / 1.40 / 4.67** percentage points. Each baseline is trained with a clean AdamW + cross-entropy recipe so that the reported gap reflects each architecture's intrinsic capacity rather than ancillary training tricks.

---

## 1. What this codebase provides

- **A theory-aligned model.** The implementation in `models/emgnet.py` and `models/blocks.py` instantiates EMG exactly as derived in the paper: a BatchNorm with affine disabled, followed by a non-negative scale `κ(e_c)` (softplus) and an additive shift `μ(e_c)` produced from a shared embedding of the standardized log-energy `q`. Zero-initialization of the conditioning projection guarantees that EMG reduces to plain BN at the first training step (§IV-D of the paper).
- **A unified training pipeline.** A single `main.py` covers all three benchmarks; all dataset-dependent values (IQ length, class count, stem stride, training schedule, model width) live in `config.py`, matching Table II of the paper.
- **All five comparison baselines.** Reference PyTorch implementations of ResNet, MCLDNN, PET-CGDNN, AMC-Net, and IQFormer (Table III of the paper) live in `models/baselines/`, with a dedicated entry point `train_baseline.py` for clean per-baseline training.
- **All ablations needed to reproduce the paper's claims.** The Full / No-energy comparison of Table IV is selectable via a CLI flag; the Concat and Raw-x configurations require small source-level edits noted below. Per-branch κ(q) profiles (Fig. 7) and the EMG modulation analysis (`utils.analyze_modulation`) are produced automatically at the end of every `--mode energy` run.
- **Per-SNR and per-class reporting.** `compute_metrics.py` computes macro/micro/weighted F1, recall, precision, and accuracy overall, per class, and per SNR — directly producing the numbers behind Table III and Figs. 3–5 of the paper.

---

## 2. Repository layout

```
.
├── main.py                   # Unified training + evaluation entry point (EMGNet + baselines under unified protocol)
├── train_baseline.py         # Plain AdamW + CE trainer for the five comparison baselines
├── config.py                 # Per-dataset architecture & training defaults (Table II)
├── load_hisar.py             # HisarMod2019 CSV loader (with .npz cache)
├── compute_metrics.py        # F1 / recall / precision per class and per SNR
├── utils.py                  # DataParallel unwrap; analyze_modulation (κ, |μ| probe)
├── models/
│   ├── emgnet.py             # EMGNet backbone: stem + 4 dilated branches + EMG injections
│   ├── blocks.py             # EMG layer, ResBlock, PlainResBlock, DilatedBranch
│   └── baselines/            # ResNet, MCLDNN, PET-CGDNN, AMC-Net, IQFormer
├── rml_data/
│   ├── loader.py             # RML2016 (pickle) and RML2018 (HDF5) loaders
│   └── dataset.py            # Shared PyTorch Dataset; computes/standardizes log-energy q
└── training/
    ├── augment.py            # GPU augmentation (phase rot., freq. offset, time shift, AWGN) + Mixup
    ├── optimizer.py          # SAM and cosine-with-warmup scheduler
    └── engine.py             # train_epoch, evaluate, evaluate_tta, evaluate_ablation, update_bn
```

---

## 3. Mapping from paper to code

| Paper concept                                                | Where it lives                                           |
|---|---|
| Standardized log-energy `q = (log‖x‖² − μ̂_q)/σ̂_q` (Eq. 12) | `rml_data/loader.py` `_spectral_features` (`log_E` column) and `rml_data/dataset.py` (`feat_mean`/`feat_std`) |
| Shared conditioning embedding `e_c = MLP(q)` (Eq. 17)        | `EMGNet.cond_embed` in `models/emgnet.py`                |
| EMG layer `κ(e_c) ⊙ BN(f) + μ(e_c)` with softplus on κ (Eq. 15, 18, 19) | `EMG` class in `models/blocks.py`                        |
| BN-equivalent zero-init (`Wproj=0`, bias→softplus≈1)         | `EMG.__init__` in `models/blocks.py`                     |
| 4 parallel dilated branches (d ∈ {1,2,4,8}), 2 ResBlocks each, 8 EMG injection points | `EMGNet.branches` + `DilatedBranch` (in `models/blocks.py`) |
| Plain-BN stem with stride 1 (RML2016) or stride 2 (RML2018/HisarMod) | `EMGNet.stem` (stride read from `DATASET_CONFIGS[...]['stem_stride']`) |
| Statistics pooling (channel-wise mean & variance) before MLP head | last lines of `EMGNet.forward`                           |
| Energy-on/off ablation (Table IV "Full" vs "No-energy")      | `--mode energy` vs `--mode baseline`; also `evaluate_ablation` in `training/engine.py` |
| Per-branch learned κ(q), μ(q) profiles (Fig. 7)              | `analyze_modulation` in `utils.py` (printed at end of `--mode energy` runs) |
| Five comparison baselines (Table III)                        | `models/baselines/{resnet,mcldnn,pet_cgdnn,amc_net,iqformer}.py`; trained via `train_baseline.py` |

---

## 4. Environment

- Python ≥ 3.9
- PyTorch ≥ 2.0 (CUDA strongly recommended for RML2018 / HisarMod2019)
- `numpy`, `h5py`, `scikit-learn`

```bash
pip install torch numpy h5py scikit-learn
```

The script automatically wraps the model in `nn.DataParallel` if more than one GPU is visible. The four-GPU setup used for the paper's experiments uses the default per-dataset batch sizes in `config.py`.

---

## 5. Datasets

We evaluate on three standard public benchmarks. Place the original distribution files anywhere and pass the path with `--data_path`. Download links are listed in **Appendix A**.

| Dataset           | Format               | Classes | IQ length | Samples   | SNR range (dB)   |
|-------------------|----------------------|:-------:|:---------:|:---------:|:----------------:|
| RML2016.10a       | pickle (`.pkl`)      | 11      | 128       | 220 K     | −20 … +18        |
| RML2018.01a       | HDF5 (`.hdf5`)       | 24      | 1024      | 2.56 M    | −20 … +30        |
| HisarMod2019.1    | CSV (Train/, Test/)  | 26      | 1024      | 780 K     | −20 … +18        |

**Splits.** RML2016/2018 use a 60/20/20 train/val/test split stratified by `(class, SNR)`. HisarMod2019 uses the official train/test partition with an 85/15 train/val split inside the training portion. Splits are deterministic given `--seed`.

**Caches.** On first use, RML2018 builds a memory-mapped `.cache/` directory next to the HDF5 file (energy-normalized IQ + pre-computed spectral features); subsequent runs load in seconds. HisarMod2019 parses the CSVs once into `hisar_cache.npz` (~3 GB) and remaps the original non-contiguous label IDs to a continuous range `[0, 25]` (full mapping in **Appendix B**).

---

## 6. Quick start

### 6.1 Train the proposed model (Full / EMG)

```bash
# RML2016.10a — 200 epochs, batch 1024, stride-1 stem, 265 K params
python main.py --dataset 2016 \
               --data_path /path/to/RML2016.10a_dict.pkl

# RML2018.01a — 100 epochs, batch 512, stride-2 stem, 1.21 M params
python main.py --dataset 2018 \
               --data_path /path/to/GOLD_XYZ_OSC.0001_1024.hdf5

# HisarMod2019.1 — 100 epochs, batch 512, stride-2 stem, 1.21 M params
python main.py --dataset hisar \
               --data_path /path/to/HisarMod2019.1
```

These three commands reproduce the rows labelled "**Proposed (EMG)**" in **Table III** of the paper. At the end of every run, `main.py` automatically loads the highest-validation checkpoint, evaluates it on the test set, and prints overall accuracy together with per-SNR and per-bin (Low / Mid / High) breakdowns.

### 6.2 Produce paper-style metrics

`compute_metrics.py` reads `.npz` files of the form `{preds, labels, snrs, class_names}` and produces overall, per-class, and per-SNR macro F1 / recall / precision / accuracy. The npz files are written automatically by `train_baseline.py` (see §6.3); for EMGNet runs the easiest way to obtain a npz is to save `(preds, labels, snrs)` from the final test loop in `main.py` (a few lines of `np.savez(...)`).

```bash
python compute_metrics.py \
    --npz_2016 ./results/results_2016_full.npz \
    --npz_2018 ./results/results_2018_full.npz \
    --npz_2019 ./results/results_2019_full.npz \
    --output_json ./metrics_all.json
```

### 6.3 Reproducing the baselines (Table III)

We provide reference implementations of the five baselines compared in Table III: ResNet [3], MCLDNN [4], PET-CGDNN [14], AMC-Net [15], and IQFormer [6]. They live in `models/baselines/` and share the same `(iq, cond, use_energy)` forward signature as EMGNet, with `cond` ignored.

Each baseline is trained with a plain AdamW + cross-entropy recipe via the dedicated entry point `train_baseline.py` (no Mixup, no IQ augmentation, no SAM/SWA), so the reported accuracies reflect each architecture's intrinsic capacity rather than ancillary training tricks:

```bash
python train_baseline.py --dataset 2016 --model resnet     --data_path /path/to/RML2016.10a_dict.pkl
python train_baseline.py --dataset 2016 --model mcldnn     --data_path /path/to/RML2016.10a_dict.pkl
python train_baseline.py --dataset 2016 --model pet_cgdnn  --data_path /path/to/RML2016.10a_dict.pkl
python train_baseline.py --dataset 2016 --model amc_net    --data_path /path/to/RML2016.10a_dict.pkl
python train_baseline.py --dataset 2016 --model iqformer   --data_path /path/to/RML2016.10a_dict.pkl
```

Available `--model` values: `resnet`, `mcldnn`, `pet_cgdnn`, `amc_net`, `iqformer`. Repeat with `--dataset 2018` and `--dataset hisar` for the other two benchmarks. Each run writes a checkpoint and a `results_<model>.npz` file under `./ckpt_v7_{dataset}/baselines/`, which can be fed directly to `compute_metrics.py`.

---

## 7. Reproducing the ablations

### 7.1 Energy utilization ablation (Table IV)

Four configurations sharing the same backbone, differing only in how — or whether — the energy is exposed to the network. The first two are supported as first-class CLI modes; **Concat** and **Raw-x** require small source-level edits (see comments in `models/blocks.py` and `rml_data/loader.py` respectively).

| Configuration                              | Command / change                                     | What it tests                                                |
|---|---|---|
| **Full** (proposed)                        | `--mode energy`                                      | EMG with informative log-energy conditioning                 |
| **No-energy** (parameter-matched control)  | `--mode baseline`                                    | Same architecture, same parameter count, but `cond=0` at every forward (isolates the EMG mechanism at fixed capacity) |
| **Concat** (additive injection)            | replace EMG with a 1×1 conv that concatenates `q` to feature channels | Tests whether multiplicative gating matters (vs additive)    |
| **Raw-x** (no shape/energy split)          | skip the `_normalise_energy` step in `rml_data/loader.py` and feed un-normalized IQ | Tests the value of the shape/energy decomposition itself     |

The Full–vs–No-energy gap (2.01 pp on RML2016, 1.02 pp on RML2018) is the **parameter-aligned measurement of the EMG mechanism itself**, since both configurations carry the same conditioning architecture; the only difference is whether `q` is passed in or zeroed. This is the comparison the paper uses to anchor the "EMG contribution" claim.

### 7.2 Channel sensitivity (Fig. 6)

The synthetic AWGN/Rician/Rayleigh study generates 8 modulations × 20 SNRs × 2000 samples per channel and compares Full vs No-energy on each. The expected ordering of the energy gain is **AWGN > Rician > Rayleigh** (paper reports +20.0 / +6.6 / +4.3 percentage points). A generator script is not included in this repository; the dataset can be produced with any standard MATLAB / GNU-Radio pipeline using a unit-energy transmit constellation and the channel parameters in §V-E2.

### 7.3 EMG behavior probes (Figs. 7, 8)

Running `--mode energy` automatically prints, after the final test, the per-branch κ and `|μ|` of every EMG layer evaluated at `q ∈ {−3, −1.5, 0, 1.5, 3}` for each conditioning feature. This produces the data behind Fig. 7. The t-SNE embeddings of Fig. 8 can be obtained by hooking the penultimate layer (the output of `EMGNet.fc` before `EMGNet.cls`) during evaluation and projecting with any standard t-SNE implementation.

---

## 8. Key CLI flags

The defaults in `config.py` reproduce the paper. The flags below are useful for ablations and analysis.

| Flag             | Default              | Description                                                                 |
|---|---|---|
| `--dataset`      | `2016`               | One of `2016`, `2018`, `hisar`.                                             |
| `--data_path`    | required             | Path to the dataset file/directory.                                         |
| `--mode`         | `energy`             | `energy` = Full EMG; `baseline` = No-energy (parameter-matched).            |
| `--cond_dim`     | `1`                  | Standardized log-energy as a scalar (paper default).                        |
| `--epochs`       | 200 / 100            | RML2016 / RML2018 & HisarMod.                                               |
| `--batch_size`   | 1024 / 512           | Same.                                                                       |
| `--lr`           | `1e-3`               | AdamW initial learning rate.                                                |
| `--sam_rho`      | `0`                  | SAM perturbation radius; `>0` enables SAM (off in paper).                   |
| `--swa_start`    | `-1`                 | Epoch from which SWA averaging starts; `-1` disables SWA (off in paper).    |
| `--tta_n`        | `10`                 | Number of TTA augmentations at test time.                                   |
| `--seed`         | `42`                 | Random seed (results in Tables III–V are averaged over 5 seeds).            |
| `--resume`       | `None`               | Resume from a checkpoint.                                                   |

Checkpoints are written to `./ckpt_v7_{dataset}/`. The script automatically picks the higher-accuracy of `best_*.pt` and `swa_*.pt` for final test evaluation.

---

## 9. Citation

If you use this code or build on the EMG idea, please cite the paper:

```bibtex
@article{zhang2026emg,
  title   = {Energy-Modulated Gain: A Sufficient-Statistic Approach to Automatic Modulation Recognition},
  author  = {Zhang, Xingzong and Zeng, Qin and Chen, Yaqi and Zhang, Hao and Niu, Tong and Qu, Dan},
  journal = {IEEE Transactions on Wireless Communications},
  year    = {2026},
  note    = {Under review}
}
```

Please also cite the original dataset papers (see Appendix A).

---

## Appendix A — Dataset download links

All three benchmarks are publicly available. Files should retain their original names so the loaders recognize them.

### A.1 RML2016.10a

- **DeepSig official site**: <https://www.deepsig.ai/datasets/>
- **Direct download (mirror)**: `https://opendata.deepsig.io/datasets/2016.10/RML2016.10a.tar.bz2`
- **Mirror (Kaggle)**: <https://www.kaggle.com/datasets/nolasthitnotomorrow/radioml2016-deepsigcom>
- **License**: CC BY-NC-SA 4.0
- **Expected file**: `RML2016.10a_dict.pkl`
- **Reference** (also [11] in the paper):
  > T. J. O'Shea and N. West, "Radio Machine Learning Dataset Generation with GNU Radio," in *Proc. GNU Radio Conf.*, 2016.

### A.2 RML2018.01a

- **DeepSig official site**: <https://www.deepsig.ai/datasets/>
- **Direct download (mirror)**: `https://opendata.deepsig.io/datasets/2018.01/2018.01.OSC.0001_1024x2M.h5.tar.gz`
- **License**: CC BY-NC-SA 4.0
- **Expected file**: `GOLD_XYZ_OSC.0001_1024.hdf5`
- **Reference** (also [3] in the paper):
  > T. J. O'Shea, T. Roy, and T. C. Clancy, "Over-the-Air Deep Learning Based Radio Signal Classification," *IEEE J. Sel. Topics Signal Process.*, vol. 12, no. 1, pp. 168–179, 2018.

### A.3 HisarMod2019.1

- **IEEE DataPort (official)**: <https://ieee-dataport.org/open-access/hisarmod-new-challenging-modulated-signals-dataset>
- **DOI**: <https://doi.org/10.21227/8k12-2g70>
- **arXiv preprint**: <https://arxiv.org/abs/1911.04970>
- **License**: Open Access (free IEEE account required)
- **Expected directory layout** (after extracting `HisarMod2019.1.zip`, ~5.13 GB):
  ```
  HisarMod2019.1/
  ├── Train/
  │   ├── train_data.csv      (~8.29 GB)
  │   ├── train_labels.csv
  │   └── train_snr.csv
  └── Test/
      ├── test_data.csv       (~4.15 GB)
      ├── test_labels.csv
      └── test_snr.csv
  ```
- **Reference** (also [35] in the paper):
  > K. Tekbıyık, C. Keçeci, A. R. Ekti, A. Görçin, and G. Karabulut Kurt, "HisarMod: A new challenging modulated signals dataset," *IEEE Dataport*, Oct. 27, 2019, doi: 10.21227/8k12-2g70.

---

## Appendix B — HisarMod2019.1 label remapping

The original HisarMod label IDs are **non-contiguous** (the leading digit encodes the modulation family, the trailing digit the order within the family). `load_hisar.py` automatically remaps them to a continuous `[0, 25]` according to the table below. The remapped index is what the model emits and what the per-class confusion matrix in Fig. 5 of the paper uses.

| Original ID | Remapped | Class       | Family  |
|:-:|:-:|---|---|
| 0  | 0  | BPSK      | PSK    |
| 1  | 1  | 4QAM      | QAM    |
| 2  | 2  | 2FSK      | FSK    |
| 3  | 3  | 4PAM      | PAM    |
| 4  | 4  | AM-DSB    | Analog |
| 10 | 5  | QPSK      | PSK    |
| 11 | 6  | 8QAM      | QAM    |
| 12 | 7  | 4FSK      | FSK    |
| 13 | 8  | 8PAM      | PAM    |
| 14 | 9  | AM-DSB-SC | Analog |
| 20 | 10 | 8PSK      | PSK    |
| 21 | 11 | 16QAM     | QAM    |
| 22 | 12 | 8FSK      | FSK    |
| 23 | 13 | 16PAM     | PAM    |
| 24 | 14 | AM-USB    | Analog |
| 30 | 15 | 16PSK     | PSK    |
| 31 | 16 | 32QAM     | QAM    |
| 32 | 17 | 16FSK     | FSK    |
| 34 | 18 | AM-LSB    | Analog |
| 40 | 19 | 32PSK     | PSK    |
| 41 | 20 | 64QAM     | QAM    |
| 44 | 21 | FM        | Analog |
| 50 | 22 | 64PSK     | PSK    |
| 51 | 23 | 128QAM    | QAM    |
| 54 | 24 | PM        | Analog |
| 61 | 25 | 256QAM    | QAM    |

---

## License

The code in this repository is released under the MIT License. The datasets are governed by their original licenses (CC BY-NC-SA 4.0 for RML2016 and RML2018; IEEE DataPort Open Access for HisarMod2019.1).
