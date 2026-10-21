<div align="center" style="font-size: 5em;">
  <strong>CardioState-JEPA: Delay-Aware Cross-Modal Learning<br/>of a Shared Cardiac Representation</strong>
  <br><br>
</div>

<div align="center">
<a href="https://hamzashafiq28.github.io/projects/cardiostate-jepa/"><img src="https://img.shields.io/badge/Project-Page-blue?style=for-the-badge"></a>
<a href="https://arxiv.org/abs/2608.12944"><img src="https://img.shields.io/badge/arXiv-Paper-red?style=for-the-badge"></a>
<a href="https://huggingface.co/hamzashafiq/CardioState-JEPA"><img src="https://img.shields.io/badge/Checkpoint-%F0%9F%A4%97%20Hugging%20Face-yellow?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/Manhph2211/PulseLM"><img src="https://img.shields.io/badge/PPG%20Data-%F0%9F%A4%97%20PulseLM-orange?style=for-the-badge"></a>
</div>

<!-- Project-page and arXiv badges are placeholders until those links go live. -->
<br>

<div align="center">
    <img src="Fig/CardioState_Fig.png" width="100%" alt="Overview of CardioState-JEPA: two-stage delay-aware cross-modal JEPA over ECG, PPG, and PCG"/>
</div>

## :rocket: Introduction

**What if one cardiac foundation model could read ECG, PPG, *and* PCG?**

Electrocardiography (ECG), photoplethysmography (PPG), and phonocardiography (PCG) are
three different observations of the **same** cardiac cycle — electrical activation,
peripheral pulse, and heart sounds — yet cardiac foundation models are almost always
trained for a single sensor, leaving the shared physiology across sensors unexploited.

**CardioState-JEPA** is a cardiac foundation model that learns **one shared representation
jointly across ECG, PPG, and PCG**, built on a physiology-aware joint-embedding predictive
architecture (JEPA). It maps heterogeneous waveforms into a common token space, processes
them with a **single shared Transformer encoder**, and learns by **predicting masked latent
cardiac states** rather than reconstructing raw waveforms — placing the pretraining target
on shared physiology instead of sensor-specific appearance.

Because the three modalities observe the same beat at *different physiological times* (PCG
follows electromechanical coupling, PPG arrives later via pulse transit), cross-modal
prediction uses a **learned delay aligner** that matches signals at the corresponding
cardiac time. And because synchronized multi-sensor recordings are scarce, training follows
a two-stage curriculum: **Stage&nbsp;I** learns within-modality structure from abundant
unimodal data, then **Stage&nbsp;II** uses paired data to align modalities in latent cardiac
time.

Evaluated as a **frozen encoder** across **25 downstream tasks** spanning ECG, PPG, and PCG,
a single shared encoder improves average **PPG** classification by **+8.2** AUROC, **PCG**
murmur detection by **+18.8** AUROC, and **ECG** classification by **+15.5** AUROC over the
best self-supervised signal baseline, and matches or exceeds cardiac models trained with
privileged clinical text or supervised labels on several ECG benchmarks.

This repository releases the **pretrained shared encoder** and a **linear-probe evaluation
harness**, so you can extract cardiac codes from any of the three modalities and reproduce
the frozen-encoder downstream results.

## :bar_chart: Key Results (frozen encoder, linear probe)

| Modality | Metric | Best signal baseline | **CardioState-JEPA** |
|---|---|---|---|
| PPG (6 classification tasks) | macro-AUROC ↑ | 72.2 | **80.4** |
| PPG (11 regression tasks) | MAE ↓ | 10.9 | **9.1** |
| ECG (6 datasets × 3 label fractions) | macro-AUROC ↑ | 68.5 | **84.1** |
| PCG — CirCor murmur | macro-AUROC ↑ | 79.1 | **97.9** |
| PCG — CinC2016 abnormal | macro-AUROC ↑ | 62.4 | **66.8** |

All downstream evaluations use **patient-disjoint** splits and a frozen encoder → trainable
`nn.Linear` head. See the paper for full per-task tables and ablations.

## :file_folder: Repository Structure

```
.
├── cardiostate_jepa
│   ├── models          # shared encoder, tokenizers/stems, JEPA model
│   ├── losses          # intra/cross JEPA, delay supervision, VICReg state, phase
│   ├── data            # modality datasets + paired loaders (VitalDB, EPHNOGRAM, ...)
│   ├── evaluation      # linear-probe evaluation harness (ECG / PPG / PCG runners)
│   ├── scripts         # feature extraction, linear probe, figures
│   └── configs/model   # encoder architecture configs
├── cardio_state_weights
│   └── cardiostate_encoder.pt      # released shared encoder (or download from HF)
├── requirements.txt
└── README.md
```

## :hammer_and_wrench: Installation

```bash
git clone https://github.com/hamzashafiq28/CardioState-JEPA.git && cd CardioState-JEPA
conda create -n cstate python=3.10 && conda activate cstate
pip install -r requirements.txt
pip install -e .          # installs the `cardiostate_jepa` package
```

## :floppy_disk: Model Weights (Hugging Face)

The released model is a **single encoder checkpoint** (`cardiostate_encoder.pt`, ~360 MB) —
the frozen ViT-B shared encoder used for all downstream results. It is a **pure weights file**
(a `state_dict` with no optimizer state, no config, and no data/paths embedded), so you load
it together with the matching architecture config shipped in this repo:
`cardiostate_jepa/configs/model/cardiostate.yaml`.

**Download from the Hub:**

```bash
huggingface-cli download hamzashafiq/CardioState-JEPA \
    cardiostate_encoder.pt --local-dir cardio_state_weights/
```

or in Python:

```python
from huggingface_hub import hf_hub_download
ckpt = hf_hub_download("hamzashafiq/CardioState-JEPA", "cardiostate_encoder.pt")
```

**Load the encoder and extract cardiac codes:**

```python
import torch
from cardiostate_jepa.evaluation.checkpoint_model import load_model_for_eval

model = load_model_for_eval(
    "cardio_state_weights/cardiostate_encoder.pt",
    "cardiostate_jepa/configs/model/cardiostate.yaml",
).eval()

# tokenize -> shared encoder -> projector; pooled mean gives the cardiac code
ppg = torch.randn(2, 1, 1250)        # [batch, 1 channel, 10 s @ 125 Hz]
with torch.no_grad():
    tokens, _ = model.core.tokenize(ppg, "ppg", 125.0)
    code = model.core.encode(tokens).mean(1)   # [2, 768] cardiac code
print(code.shape)
```

The same encoder accepts `"ecg"` (12-lead, 500 Hz) and `"pcg"` (1-channel, 4000 Hz) — pass
the modality name and its sampling rate to `tokenize`.

### Load with `transformers` (`AutoModel.from_pretrained`)

The encoder is also published as a `transformers`-compatible model, so it loads with the
standard `AutoModel.from_pretrained(..., trust_remote_code=True)` interface:

```python
from transformers import AutoModel
import torch

model = AutoModel.from_pretrained("hamzashafiq/CardioState-JEPA",
                                  trust_remote_code=True).eval()

ppg = torch.randn(2, 1, 1250)            # [batch, 1 ch, 10 s @ 125 Hz]
with torch.no_grad():
    out = model(ppg, modality="ppg", fs=125.0)
print(out.pooler_output.shape)           # (2, 768) cardiac code
```

`modality` is `"ecg"` (12 leads @ 500 Hz), `"ppg"` (1 ch @ 125 Hz), or `"pcg"` (1 ch @ 4000 Hz);
pass the matching `fs`. This path requires the package to be installed (`pip install -e .`),
since the encoder architecture lives here. The `transformers` wrapper (`CardioStateConfig` /
`CardioStateModel`) and the script that assembles the Hugging Face repo are in [`hf/`](hf/).

## :book: Usage — PPG Evaluation with Hugging Face Weights

The PPG downstream data is the public **[PulseLM](https://huggingface.co/datasets/Manhph2211/PulseLM)**
benchmark and is **auto-downloaded from Hugging Face** on first run. To evaluate the released
encoder, point the runner at the checkpoint via `CSTATE_CKPT` and select `--model cardiostate`:

```bash
# 1) get the weights (once)
huggingface-cli download hamzashafiq/CardioState-JEPA \
    cardiostate_encoder.pt --local-dir cardio_state_weights/

# 2) point the runner at the weights + the matching architecture config
export CSTATE_CKPT=cardio_state_weights/cardiostate_encoder.pt
export CSTATE_CONFIG=cardiostate_jepa/configs/model/cardiostate.yaml

# 3) run a PPG task — PulseLM is fetched from the Hub automatically
python -m cardiostate_jepa.evaluation.baselines.ppg.run \
    --model cardiostate --dataset pulselm --task wesad \
    --epochs 100 --lr 1e-3 --batch-size 16 --device cuda
```

This freezes the encoder, extracts features, trains a linear head under the MERL protocol
(Adam, `lr=1e-3`, 100 epochs, `MultiStepLR` milestone 40), and reports
macro-AUROC (classification) or MAE (regression) with a 95% subject-level bootstrap CI to
`runs/ppg/cardiostate_pulselm_<task>/metrics.json`.

**Available PPG task keys** (`--task`):

| Type | Tasks |
|---|---|
| Classification (macro-AUROC ↑) | `wesad`, `dalia_activity`, `ppgarrhythmia`, `mimicperform_af`, `sdb`, `bidmc_rr`, `uqvitalsigns_rr` |
| Regression (MAE ↓) | `dalia_hr`, `earset_hr`, `wildppg_hr`, `wildppg_rmssd`, `bcg_sbp`, `bcg_dbp`, `ppgbp_sbp`, `ppgbp_dbp`, `sensors_sbp`, `sensors_dbp`, `uci_sbp`, `uci_dbp`, `uqvitalsigns_spo2` |

Sweep every task with three seeds:

```bash
for task in wesad dalia_activity ppgarrhythmia mimicperform_af sdb bidmc_rr uqvitalsigns_rr \
            dalia_hr earset_hr wildppg_hr wildppg_rmssd bcg_sbp bcg_dbp ppgbp_sbp ppgbp_dbp \
            sensors_sbp sensors_dbp uci_sbp uci_dbp uqvitalsigns_spo2; do
  for seed in 0 1 2; do
    python -m cardiostate_jepa.evaluation.baselines.ppg.run \
        --model cardiostate --dataset pulselm --task "$task" \
        --seed "$seed" --epochs 100 --lr 1e-3 --batch-size 16 --device cuda
  done
done
```

> **Env vars:** `CSTATE_CKPT` (required, path to the weights) and `CSTATE_CONFIG` (the
> architecture config above). Optional: `CSTATE_FEATURE` (`encoder`, default),
> `CSTATE_POOLING` (`mean`, default), `CSTATE_PPG_FS` (`125`, default).

The ECG and PCG probes work the same way — `cardiostate_jepa.evaluation.baselines.ecg.run`
(`--dataset ptbxl --task super`, etc.) and `cardiostate_jepa.scripts.probe_pcg_baselines`
(`--dataset circor --task murmur`) — all with `--model cardiostate` and the same `CSTATE_*`
environment variables.

## :page_facing_up: Citation

```bibtex
@misc{shafiq2026cardiostatejepadelayawarecrossmodallearning,
      title={CardioState-JEPA: Delay-Aware Cross-Modal Learning of a Shared Cardiac Representation}, 
      author={Hamza Shafiq and Hung Manh Pham and Bin Zhu and Pan Zhou and Jun Hu and Aaqib Saeed},
      year={2026},
      eprint={2608.12944},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2608.12944}, 
}
```
