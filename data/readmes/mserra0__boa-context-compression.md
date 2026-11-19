# Boa: Linear-Time Context Compression with State-Space Encoding

Boa is a plug-and-play online context compressor built on a Mamba state-space model (SSM). It encodes arbitrary-length text context in a single linear-time $\mathcal{O}(L)$ pass into a compact sequence of continuous representations or Key-Value (KV) caches, conditioning a frozen target LLM without fine-tuning or modifying the LLM.

<p align="center">
  <a href="https://arxiv.org/abs/2610.33006">
    <img src="https://img.shields.io/badge/arXiv-2610.33006-B31B1B?style=for-the-badge&logo=arxiv&logoColor=white" alt="Paper on arXiv: 2610.33006">
  </a>
  <a href="https://www.alphaxiv.org/abs/2610.33006">
    <img src="https://img.shields.io/badge/alphaXiv-Discussion-9A2036?style=for-the-badge&logo=alphaxiv&logoColor=white" alt="Discussion on alphaXiv">
  </a>
  <a href="https://mserra0.github.io/boa-context-compression/">
    <img src="https://img.shields.io/badge/Project%20Page-Live-1F6FEB?style=for-the-badge&logo=githubpages&logoColor=white" alt="Project page">
  </a>
</p>

<p align="center">
  <a href="#quick-start">
    <img src="https://img.shields.io/badge/Quick%20Start-18181B?style=flat-square" alt="Quick Start">
  </a>
  <a href="#documentation">
    <img src="https://img.shields.io/badge/Documentation-18181B?style=flat-square" alt="Documentation">
  </a>
  <a href="#citation">
    <img src="https://img.shields.io/badge/Citation-18181B?style=flat-square" alt="Citation">
  </a>
</p>

<p align="center">
  <img src="figures/Method.png" alt="Boa Compressor Overview" width="100%">
</p>

## Quick Start

Prerequisites: Linux, an NVIDIA GPU, the CUDA toolkit (`nvcc`, needed to build `mamba-ssm` and `causal-conv1d`) and [uv](https://github.com/astral-sh/uv); details in [docs/setup.md](docs/setup.md).

```bash
# 1. Install
uv sync

# 2. Download MRQA (about 1.5 GB; layout and details: docs/data/datasets.md)
bash scripts/download_mrqa.sh data/MRQA

# 3. Train a small compressor (Mamba2-130M compressing for a frozen Qwen2.5-0.5B-Instruct)
#    on 200 MRQA samples. WANDB_MODE=disabled runs without a Weights & Biases account.
export WANDB_MODE=disabled
uv run torchrun --standalone --nproc_per_node=1 main.py --config configs/quickstart.yaml

# 4. Compare the frozen LLM (full context) with the compressed student on a short context
CKPT=$(ls -dt checkpoints/quickstart_*/ | head -1)best_model.pt
cat > context.txt <<'CTX'
Hamlet is a tragedy written by William Shakespeare, probably between 1599 and 1601. It is set in Denmark and follows Prince Hamlet as he seeks revenge on his uncle Claudius, who murdered Hamlet's father, the king, and then married the king's widow, Queen Gertrude.
CTX
printf 'Who wrote the play Hamlet?\nexit\n' | \
  uv run python src/inference.py --config configs/quickstart.yaml --checkpoint "$CKPT" --context-file context.txt
```

`configs/quickstart.yaml` only uses public Hugging Face models (downloaded on first use) and is meant to verify the installation and data layout, not to produce a useful compressor: after a few steps the student's answers are not meaningful. The first run builds a dataset cache from the MRQA files, which takes a few minutes. For interactive use, run `src/inference.py` without piping input; `--context-file` sets the context that the teacher reads in full and the student reads compressed.

Paper experiments (8x compression, Mamba2 1.3B compressor, fine-tuned Qwen3-1.7B as frozen LLM, see [docs/training/teacher.md](docs/training/teacher.md)):

```bash
# Stage 1: LM pretraining on FineWeb-Edu (needs the sample/100BT subset, see docs/data/datasets.md)
uv run torchrun --standalone --nproc_per_node=<num_gpus> main.py \
  --config configs/pretrain/mn5/qwen3_1-7b/pretrain_mamba2_kv_qwen3_8x.yaml

# Stage 2: MRQA fine-tuning (set training.start_from to the stage-1 run directory first)
uv run torchrun --standalone --nproc_per_node=<num_gpus> main.py \
  --config configs/train/mn5/qwen3_1-7b/mambaL2_pathB_kv_8x_from_pretrain.yaml

# Evaluation (official MRQA F1/EM; the out-of-domain sets need: bash scripts/download_mrqa.sh data/MRQA --ood)
CUDA_VISIBLE_DEVICES=0 uv run python -m src.evaluation \
  --config configs/eval/config_eval_MRQA.yaml \
  --experiment-dir checkpoints/<run_dir> \
  --device cuda
```

These configs are sized for multi-node runs (see [docs/cluster.md](docs/cluster.md)); adjust the batch settings when using fewer GPUs. Placeholder paths are listed in [docs/setup.md](docs/setup.md). The other configs under `configs/train`, `configs/pretrain` and `configs/ablations` cover the compression-ratio, decoder-scaling and ablation runs ([docs/benchmarks/ablations.md](docs/benchmarks/ablations.md)).

## Branches

| Branch | Contents | Branch documentation |
|---|---|---|
| `main` | Boa compressor, training, evaluation, latency benchmark | this repository |
| `baseline/activation-beacon` | Activation Beacon baseline | [`docs/baselines/activation-beacon.md`](https://github.com/mserra0/boa-context-compression/blob/baseline/activation-beacon/docs/baselines/activation-beacon.md) |
| `baseline/sac` | SAC baseline | [`docs/baselines/sac.md`](https://github.com/mserra0/boa-context-compression/blob/baseline/sac/docs/baselines/sac.md) |
| `baseline/icae` | ICAE baseline | [`docs/baselines/icae.md`](https://github.com/mserra0/boa-context-compression/blob/baseline/icae/docs/baselines/icae.md) |
| `baseline/qwen3-fullft` | full fine-tuning of the Qwen3 frozen LLM / teacher used by the configs on `main` | [`docs/baselines/qwen3-fullft.md`](https://github.com/mserra0/boa-context-compression/blob/baseline/qwen3-fullft/docs/baselines/qwen3-fullft.md) |
| `ablation/sft-finetune` | supervised fine-tuning objective (8x ablation arms) | [`docs/ablations/sft-finetune.md`](https://github.com/mserra0/boa-context-compression/blob/ablation/sft-finetune/docs/ablations/sft-finetune.md) |
| `ablation/kd-pretrain` | off-policy KD pretraining objective (KD ablation arm) | [`docs/ablations/kd-pretrain.md`](https://github.com/mserra0/boa-context-compression/blob/ablation/kd-pretrain/docs/ablations/kd-pretrain.md) |

## Documentation

Getting started:

- [Setup](docs/setup.md): prerequisites, installation, placeholders and environment variables
- [Datasets](docs/data/datasets.md): MRQA and FineWeb-Edu download and directory layout
- [Frozen LLM / teacher checkpoints](docs/training/teacher.md): how the fine-tuned Qwen3 models are produced
- [Cluster scripts](docs/cluster.md): example Slurm scripts and what to adapt
- [Pinned model revisions](docs/pinned-revisions.md): Hub revisions used for the experiments

Method and implementation:

- [Architecture Overview](docs/architecture/overview.md): forward pass, model classes, prompt injection geometries
- [Compressors (Mamba1 vs Mamba2)](docs/architecture/compressors.md): stride anchoring, left-padding, sequence packing
- [Student Layout Templates](docs/architecture/student-templates.md): bare, B-qc and B-ctx student formats
- [Attention Geometry](docs/architecture/attention.md): 2D padding mask expansion and bounded (FIFO) mask caching
- [KV Injection Mechanics](docs/architecture/kv-injection.md): key-value cache projections and anchor embeddings
- [Knowledge Distillation Loss](docs/training/knowledge-distillation.md): KL divergence, temperature scaling, position masking
- [Training Loop](docs/training/loop.md): DDP training, AMP precision, gradient accumulation, W&B logging
- [Language Model Pretraining](docs/training/pretraining.md): pretraining pipeline, token budget packing, FineWeb-Edu
- [Data Loading & Packing](docs/data/dataloading.md) and [Dataset Schema](docs/data/dataset.md)

Evaluation and benchmarks:

- [MRQA Evaluation Suite](docs/evaluation/mrqa-metrics.md): official span-overlap F1/EM package and batch scripts
- [Ablation Benchmark Matrix](docs/benchmarks/ablations.md): 8x compression, model scaling and ablation runs
- [Latency Benchmark](docs/benchmarks/latency.md): latency / memory sweeps against ICAE, SAC, Activation Beacon and full context (`benchmarks/latency/`)

Project page:

- [Project page](https://mserra0.github.io/boa-context-compression/): source in `site/`; the latency curves in `site/data/latency.json` are regenerated with `node site/tools/build-latency.mjs <outputs-directory> > site/data/latency.json`

Engineering notes:

- [Correctness Notes](docs/engineering/correctness-notes.md)

## Citation

```bibtex
@misc{serraortega2026lineartime,
  title={Linear-Time Context Compression with State-Space Encoding},
  author={Marc Serra Ortega and Andrey Barsky and Carlos Boned Riera and Tom{\'a}s Ockier and Dimosthenis Karatzas},
  year={2026},
  eprint={2610.33006},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2610.33006}
}
```

Third-party code and attributions: [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). A machine-readable citation is in [CITATION.cff](CITATION.cff).

## License

Released under the MIT License, see [LICENSE](LICENSE). Third-party components keep their own licenses, see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
