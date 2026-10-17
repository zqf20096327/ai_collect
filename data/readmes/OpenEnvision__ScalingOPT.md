<p align="center">
  <div align="center">
  <img width="243.5" height="186.7" alt="2a0ff7d09549aec917655f98551eaa32" src="https://github.com/user-attachments/assets/d0a7d40e-1be4-4a34-a943-e19caef400d4" />
</div>
  <h1 align="center">ScalingOPT (LLM)</h1>
  <p align="center">
    <b>Optimizer-centric scaling studies for large language model</b>
    <br/>
    <a href="https://tianshijing.github.io/ScalingOpt/">Project Page</a> · <a href="#quick-start">Quick Start</a> · <a href="#optimizers">30+ Optimizers</a> · <a href="#datasets-and-data-pipelines">Datasets</a> · <a href="#training-recipes">Training Recipes</a> · <a href="#evaluation">Evaluation</a>
  </p>
</p>

---

ScalingOPT is a research-oriented PyTorch codebase for **optimizer-centric scaling studies** in large language model (LLM) training. It is part of the broader [ScalingOpt](https://tianshijing.github.io/ScalingOpt/) community effort and is designed to make optimizer comparisons **reproducible**, **fair**, and **ergonomically extensible**.

## Highlights

- **Single entrypoint, 30+ optimizers** — switch optimizers with `--optimizer <name>`, no loop rewriting needed.
- **17 model configs** — LLaMA (9M–13B), GPT-2 (124M), Qwen3 (0.6B–1.7B) with full architecture details.
- **3 dataset pipelines** — C4 (HF streaming), The Pile (local JSONL), OpenWebText (nanoGPT binary).
- **Multi-GPU DDP** — native `torchrun` distributed training out of the box.
- **Single-GPU & low-memory** — quantized weight training and per-layer optimizer variants for ≤12 GB VRAM.
- **Post-training** — SFT, DPO, GRPO via TRL integration; PPO/REINFORCE++ via OpenRLHF.
- **Evaluation** — one-command eval on 14+ benchmarks via lm-evaluation-harness.
- **Logging** — Weights & Biases + JSONL; tracks loss, perplexity, LR, throughput, and more.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Repository Structure](#repository-structure)
- [Optimizers](#optimizers)
- [Datasets and Data Pipelines](#datasets-and-data-pipelines)
- [Model Configurations](#model-configurations)
- [Training Recipes](#training-recipes)
  - [Recipe 1: C4 Pretraining (LLaMA)](#recipe-1-c4-pretraining-llama)
  - [Recipe 2: The Pile Pretraining (Qwen3)](#recipe-2-the-pile-pretraining-qwen3)
  - [Recipe 3: OpenWebText Pretraining (GPT-2)](#recipe-3-openwebtext-pretraining-gpt-2)
  - [Recipe 4: Single-GPU Low-Memory Training](#recipe-4-single-gpu-low-memory-training)
- [SFT / DPO / GRPO Training](#sft--dpo--grpo-training-trl-integration)
- [Evaluation](#evaluation)
- [Full CLI Reference](#full-cli-reference)
- [Checkpointing and Resuming](#checkpointing-and-resuming)
- [Logging](#logging)
- [License](#license)
- [Citation and Attribution](#citation-and-attribution)

---

## Prerequisites

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| Python | 3.7+ | 3.10+ |
| PyTorch | 2.0+ | 2.2+ (with BF16 support) |
| GPU | 1× (single-GPU mode) | 4–8× NVIDIA A100/H100 |
| CUDA | 11.8+ | 12.1+ |
| OS | Linux | Ubuntu 22.04+ |

> **Note**: macOS/CPU can be used for code development and debugging, but GPU is required for actual training.

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/OpenEnvision-Lab/ScalingOPT.git
cd ScalingOPT
```

### Step 2: Create a virtual environment (recommended)

```bash
conda create -n scalingopt python=3.10 -y
conda activate scalingopt
```

Or with `venv`:

```bash
python -m venv venv
source venv/bin/activate
```

### Step 3: Install PyTorch

Install PyTorch with CUDA support matching your driver version. Visit [pytorch.org](https://pytorch.org/get-started/locally/) for the latest command, for example:

```bash
pip install torch --index-url https://download.pytorch.org/whl/cu121
```

### Step 4: Install all dependencies

```bash
pip install -r requirements.txt
```

This installs the full dependency stack: `transformers`, `datasets`, `wandb`, `tiktoken`, `loguru`, `bitsandbytes`, `evaluate`, `tqdm`, `schedulefree`, and more.

### Step 5: Install the optimizer library

```bash
pip install -e .
```

This installs `scalingopt-torch` in editable mode, making all optimizers in `scalingopt_torch/` importable.

### Verify installation

```bash
python -c "import scalingopt_torch; print('scalingopt_torch version:', scalingopt_torch.__version__)"
python -c "import torch; print('PyTorch:', torch.__version__); print('CUDA available:', torch.cuda.is_available())"
```

---

## Quick Start

Train a LLaMA-60M model on C4 with AdamW (single node, 4 GPUs):

```bash
torchrun --standalone --nproc_per_node 4 main_pretrain.py \
  --model_config configs/llama_60m.json \
  --dataset allenai/c4 --dataset_config en \
  --tokenizer t5-base \
  --batch_size 32 --total_batch_size 512 \
  --max_length 256 \
  --lr 1e-3 --warmup_steps 1000 --num_training_steps 10000 \
  --weight_decay 0.1 --grad_clipping 1.0 \
  --optimizer adamw \
  --eval_every 1000 --save_every 5000 \
  --dtype bfloat16
```

Want to try a different optimizer? Just change `--optimizer`:

```bash
# APOLLO
--optimizer apollo_adamw --rank 256 --scale_type channel --proj random --update_proj_gap 200 --apollo_scale 1

# Muon
--optimizer muon

# Adam-Mini
--optimizer adam_mini
```

---

## Repository Structure

```
ScalingOPT/
├── main_pretrain.py                 # Pretraining entrypoint (DDP via torchrun)
├── main_sft.py                      # SFT entrypoint (TRL SFTTrainer, full + LoRA)
├── main_dpo.py                      # DPO entrypoint (TRL DPOTrainer, full + LoRA)
├── main_grpo.py                     # GRPO entrypoint (TRL GRPOTrainer, full + LoRA)
├── main_eval.py                     # Evaluation on popular benchmarks (lm-eval-harness)
├── setup.py                         # Package setup for scalingopt-torch
├── requirements.txt                 # All dependencies (merged, deduplicated)
│
├── configs/                         # Model architecture configs (JSON)
│   ├── llama_9m.json ... llama_13b.json    # LLaMA: 9M to 13B params
│   ├── gpt2_124m.json                      # GPT-2: 124M params
│   └── qwen3_0.6b.json, qwen3_1.7b.json   # Qwen3: 0.6B to 1.7B params
│
├── scalingopt_torch/                # Optimizer library (pip install -e .)
│   ├── __init__.py                  #   Exports all optimizer classes (v1.0.3)
│   ├── adamw.py, adamw8bit.py       #   GaLore AdamW / 8-bit variants
│   ├── adafactor.py, adam_mini.py   #   Adafactor / Adam-Mini
│   ├── apollo.py, q_apollo.py       #   APOLLO / Quantized APOLLO
│   ├── muon.py, moonlight.py, mano.py  # Muon / Moonlight / Mano
│   ├── soap.py, shampoo.py, sso.py  #   Second-order methods
│   ├── mars.py, mars_m.py           #   MARS / MARS-Muon
│   ├── spam.py, stable_spam.py      #   Sparse momentum methods
│   ├── lamb.py, lars.py             #   Large-batch optimizers
│   ├── lomo.py, adalomo.py          #   Low-memory optimizers
│   ├── conda.py, conda_projector.py #   Compressed gradient projection
│   ├── prodigy.py, sophia.py, ...   #   Adaptive LR methods
│   └── *_projector.py               #   SVD / random projection utilities
│
├── utils/                           # Training infrastructure
│   ├── optimizer_factory.py         #   Standalone optimizer factory (any framework)
│   ├── argparse.py                  #   CLI argument parsing
│   ├── dataloader.py                #   Dataset loading & tokenization
│   ├── setup.py                     #   Model & optimizer construction
│   ├── eval.py                      #   Evaluation utilities
│   ├── training_utils.py            #   Schedulers & helpers
│   ├── modeling_llama.py            #   Local LLaMA implementation
│   ├── quantization.py              #   Int8 weight quantization
│   └── fake_quantization.py         #   Simulated quantization
│
├── data/
│   └── openwebtext/
│       └── prepare.py               # OpenWebText → train.bin / val.bin
│
├── scripts/                         # Ready-to-run experiment scripts
│   ├── pretrain_c4/                 #   C4 pretraining (LLaMA configs)
│   ├── pretrain_pile/               #   Pile pretraining (Qwen configs)
│   ├── pretrain_openwebtext/        #   OpenWebText pretraining (GPT-2)
│   ├── single_gpu/                  #   Single-GPU / low-memory runs
│   ├── sft_trl/                     #   SFT scripts (full + LoRA)
│   ├── dpo_trl/                     #   DPO scripts (full + LoRA)
│   ├── grpo_trl/                    #   GRPO scripts (full + LoRA)
│   ├── ppo_openrlhf/               #   OpenRLHF PPO / GRPO / REINFORCE++
│   ├── eval/                        #   Evaluation scripts (lm-eval-harness)
│   └── example.sh                   #   Checkpoint resume example
│
├── LICENSE                          # CC BY-NC 4.0
├── NOTICE
└── THIRD_PARTY_NOTICES.md           # Upstream sources & licenses
```

---

## Optimizers

All optimizers are selected via `--optimizer <name>` in `main_pretrain.py`. The authoritative list is in `utils/setup.py`.

### Supported Optimizers

| Category | Optimizer Name(s) | Description |
|----------|-------------------|-------------|
| **Baselines** | `adam`, `adamw`, `sgd`, `adafactor`, `adam8bit` | Standard first-order methods |
| **GaLore Family** | `galore_adamw`, `galore_adafactor`, `galore_adamw8bit` | Gradient Low-Rank Projection |
| **GaLore Per-Layer** | `galore_adamw8bit_per_layer` | Layer-wise GaLore (saves memory) |
| **APOLLO Family** | `apollo_adamw`, `q_apollo`, `q_apollo_per_layer` | Approximate Gradient Scaling |
| **Muon-based** | `muon`, `moonlight`, `mano` | Orthogonal / matrix optimization |
| **Second-order** | `soap`, `shampoo`, `sso`, `root` | Preconditioned methods |
| **Variance-reduced** | `mars`, `mars_m` | MARS / MARS-Muon hybrid |
| **Adaptive** | `adam_mini`, `ademamix`, `came`, `sophia`, `prodigy` | Advanced adaptive LR methods |
| **Large-batch** | `adan`, `lamb`, `lars` | Designed for large-batch training |
| **Low-memory** | `lomo`, `adalomo` | Low-Memory Optimization |
| **Sparse** | `spam`, `stable_spam` | Sparse momentum methods |
| **Projected** | `conda` | Compressed gradient with projector |
| **Schedule-Free** | `adamw_schedulefree`, `sgd_schedulefree`, `radam_schedulefree` | No external LR schedule needed |

### Optimizer-specific parameters

Common parameters shared by most optimizers:

```bash
--lr 1e-4           # Learning rate
--beta1 0.9         # First moment coefficient
--beta2 0.999       # Second moment coefficient
--weight_decay 0.0  # Weight decay
--grad_clipping 0.0 # Gradient clipping (0 = disabled)
```

GaLore / APOLLO / Conda-specific parameters:

```bash
--rank 128              # Projection rank
--update_proj_gap 50    # Steps between projection updates
--proj_type std         # GaLore projection type: "std", "reverse_std", "left", "right", "full"
--galore_scale 1.0      # GaLore gradient scaling factor
--galore_dim 2          # Tensor dimension threshold: 2 = SVD projector (default), >2 = Tucker decomposition
--proj random           # APOLLO projection type: "random" or "svd"
--scale_type tensor     # APOLLO scale granularity: "tensor" or "channel"
--apollo_scale 1.0      # APOLLO gradient scaling factor
--conda_scale 1.0       # Conda gradient scaling factor
```

Quantization parameters (for `q_apollo`, `q_galore_adamw8bit`, etc.):

```bash
--weight_quant           # Enable int8 weight quantization
--weight_bits 8          # Weight quantization bits
--weight_group_size 256  # Weight quantization group size
--stochastic_round       # Enable stochastic rounding
--proj_quant             # Enable projection quantization
--proj_bits 8            # Projection quantization bits
--proj_group_size 256    # Projection quantization group size
```

> **Schedule-Free optimizers** require `pip install schedulefree` and use a constant LR schedule internally. ScalingOPT automatically handles the required `optimizer.train()` / `optimizer.eval()` mode switches.

---

## Datasets and Data Pipelines

ScalingOPT supports two data interfaces. The correct one is selected automatically based on `--dataset`.

### Interface 1: Hugging Face Datasets (Streaming)

For large-scale datasets served via the Hugging Face Hub or local directories compatible with `datasets.load_dataset()`.

```bash
--dataset allenai/c4 --dataset_config en    # C4 English (streaming)
--dataset ../datasets/pile                   # Local Pile directory
```

**Token packing** (recommended for document corpora to eliminate padding waste):

```bash
--packing --add_eos
```

This concatenates documents into a continuous token stream separated by EOS tokens, then slices fixed-length blocks of `--max_length`.

### Interface 2: nanoGPT-style Binary Corpora

If `--dataset` points to a directory containing `train.bin`, the dataloader switches to a memory-mapped random block sampler (no padding, fixed-length contiguous blocks).

```bash
--dataset data/openwebtext    # Directory containing train.bin and val.bin
```

### Dataset Summary

| Dataset | HF ID | Format | Preparation | Download Size | Used By |
|---------|-------|--------|-------------|---------------|---------|
| **C4** | [`allenai/c4`](https://huggingface.co/datasets/allenai/c4) | HF streaming | None (streams on-the-fly) | HF cache only (~few GB) | [Recipe 1](#recipe-1-c4-pretraining-llama) |
| **The Pile** | [`monology/pile-uncopyrighted`](https://huggingface.co/datasets/monology/pile-uncopyrighted) | JSONL.zst (local) | Download to local disk | ~335 GB compressed | [Recipe 2](#recipe-2-the-pile-pretraining-qwen3) |
| **OpenWebText** | [`Skylion007/openwebtext`](https://huggingface.co/datasets/Skylion007/openwebtext) | nanoGPT binary | `prepare.py` → `train.bin`/`val.bin` | ~13.5 GB download → ~17 GB bin | [Recipe 3](#recipe-3-openwebtext-pretraining-gpt-2) |

### Tokenizer Summary

| Tokenizer | HF ID | Vocab Size | Used By |
|-----------|-------|------------|---------|
| T5-base (SentencePiece) | [`t5-base`](https://huggingface.co/t5-base) | 32,000 | Recipe 1 (LLaMA on C4) |
| Qwen3-0.6B | [`Qwen/Qwen3-0.6B-Base`](https://huggingface.co/Qwen/Qwen3-0.6B-Base) | 151,669 | Recipe 2 (Qwen3-0.6B on Pile) |
| Qwen3-1.7B | [`Qwen/Qwen3-1.7B-Base`](https://huggingface.co/Qwen/Qwen3-1.7B-Base) | 151,669 | Recipe 2 (Qwen3-1.7B on Pile) |
| GPT-2 (BPE) | [`gpt2`](https://huggingface.co/gpt2) | 50,257 | Recipe 3 (GPT-2 on OpenWebText) |

All tokenizers are auto-downloaded from Hugging Face on first use. To pre-download for offline clusters:

```bash
python -c "
from transformers import AutoTokenizer
for name in ['t5-base', 'Qwen/Qwen3-0.6B-Base', 'Qwen/Qwen3-1.7B-Base', 'gpt2']:
    AutoTokenizer.from_pretrained(name)
    print(f'Downloaded: {name}')
"
```

> **About model weights**: ScalingOPT trains all models **from scratch**. No pretrained model weights are downloaded — only tokenizer files. Model architectures are randomly initialized from the local JSON configs in `configs/`.

See each [Training Recipe](#training-recipes) for detailed per-recipe download instructions.

---

## Model Configurations

All model architectures are defined as JSON configs in `configs/`. ScalingOPT auto-selects the appropriate model class:

- **LLaMA configs** → local `LlamaForCausalLM` (in `utils/modeling_llama.py`)
- **GPT-2 / Qwen3 configs** → `transformers.AutoModelForCausalLM` (add `--use_hf_model` for Qwen)

### Available Configs

| Config File | Architecture | Parameters | Hidden Size | Layers | Heads | FFN Size |
|-------------|-------------|------------|-------------|--------|-------|----------|
| `llama_9m.json` | LLaMA | 9M | 128 | 4 | 4 | 352 |
| `llama_20m.json` | LLaMA | 20M | 256 | 4 | 4 | 688 |
| `llama_35m.json` | LLaMA | 35M | 384 | 6 | 8 | 1024 |
| `llama_40m.json` | LLaMA | 40M | 416 | 8 | 8 | 1024 |
| `llama_60m.json` | LLaMA | 60M | 512 | 8 | 8 | 1376 |
| `llama_71m.json` | LLaMA | 71M | 512 | 12 | 8 | 1368 |
| `llama_100m.json` | LLaMA | 100M | 640 | 12 | 10 | 1708 |
| `llama_130m.json` | LLaMA | 130M | 768 | 12 | 12 | 2048 |
| `llama_250m.json` | LLaMA | 250M | 768 | 24 | 16 | 2560 |
| `llama_350m.json` | LLaMA | 350M | 1024 | 24 | 16 | 2736 |
| `llama_1b.json` | LLaMA | 1B | 2048 | 24 | 32 | 5461 |
| `llama_3b.json` | LLaMA | 3B | 2560 | 32 | 32 | 6848 |
| `llama_7b.json` | LLaMA | 7B | 4096 | 32 | 32 | 11008 |
| `llama_13b.json` | LLaMA | 13B | 5120 | 40 | 40 | 13824 |
| `gpt2_124m.json` | GPT-2 | 124M | 768 | 12 | 12 | 3072 |
| `qwen3_0.6b.json` | Qwen3 | 0.6B | 1024 | 28 | 16 (GQA 8) | 3072 |
| `qwen3_1.7b.json` | Qwen3 | 1.7B | 2048 | 28 | 16 (GQA 8) | 6144 |

> **Notes**: All LLaMA configs use SiLU activation, RoPE embeddings, and vocab size 32,000 (except llama_100m: 32,100). Qwen3 configs use Grouped-Query Attention with 8 KV heads and vocab size 151,669. GPT-2 uses GELU activation and vocab size 50,257.

---

## Training Recipes

All training is launched through a single entrypoint with `torchrun`:

```bash
torchrun --standalone --nproc_per_node <NUM_GPUS> main_pretrain.py [ARGUMENTS]
```

> **All models are trained from scratch.** ScalingOPT never downloads pretrained model weights — only tokenizer files. Model architectures are randomly initialized from the local JSON configs in `configs/`.

### Recipe 1: C4 Pretraining (LLaMA)

**Scripts**: `scripts/pretrain_c4/`
**Configs**: `configs/llama_*.json` (9M – 13B)

#### Step 1: Download the dataset

C4 (Colossal Clean Crawled Corpus) is streamed directly from the Hugging Face Hub — **no manual download needed**. Data flows on-the-fly during training; only HF's local cache is used for buffering.

| Item | Value |
|------|-------|
| HF Dataset ID | [`allenai/c4`](https://huggingface.co/datasets/allenai/c4) |
| Config | `en` (English subset, ~305 GB total, auto-set by ScalingOPT) |
| Format | Compressed JSON (`.json.gz`), 1024 shards |
| Access | Public, no authentication required |
| License | [ODC-BY](https://opendatacommons.org/licenses/by/1-0/) |
| Local disk | Only HF cache (~few GB streaming buffer) |

The default mode is **streaming**, which requires no pre-download — training begins immediately and data is fetched on-the-fly. To verify streaming works:

```bash
python -c "
from datasets import load_dataset
ds = load_dataset('allenai/c4', 'en', split='train', streaming=True)
sample = next(iter(ds))
print('Keys:', list(sample.keys()))
print('Text preview:', sample['text'][:200])
print('C4 streaming OK')
"
```

> **Offline / air-gapped clusters**: if your training nodes cannot access the internet, pre-download C4 to a local directory using one of the methods below, then point `--dataset` to it.
>
> **Method A — Python `datasets` library** (saves as HF Arrow format):
>
> ```bash
> # Download C4 English to local disk (~305 GB download, ~350 GB on disk as Arrow)
> python -c "
> from datasets import load_dataset
> ds = load_dataset('allenai/c4', 'en', split='train')
> ds.save_to_disk('./datasets/c4-en-train')
> "
> # Then use --dataset ./datasets/c4-en-train in training
> ```
>
> **Method B — `huggingface-cli`** (keeps raw `.json.gz` shards):
>
> ```bash
> pip install -U huggingface_hub
> # Download only the English subset (~305 GB)
> huggingface-cli download allenai/c4 --repo-type dataset --include "en/*" --local-dir ./datasets/c4
> # Then use --dataset ./datasets/c4 in training
> ```
>
> **Method C — Git LFS** (selective shard download):
>
> ```bash
> GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://huggingface.co/datasets/allenai/c4
> cd c4
> git lfs pull --include "en/*"   # ~305 GB
> ```

#### Step 2: Download the tokenizer

The T5-base tokenizer is automatically downloaded from Hugging Face on first use (~2 MB). To pre-download for offline clusters:

```bash
python -c "from transformers import AutoTokenizer; AutoTokenizer.from_pretrained('t5-base')"
```

| Item | Value |
|------|-------|
| Tokenizer | [`t5-base`](https://huggingface.co/t5-base) (SentencePiece, vocab size 32,000) |
| Download size | ~2 MB |

Verify the tokenizer is working:

```bash
python -c "
from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained('t5-base')
print('Vocab size:', tok.vocab_size)
ids = tok('Hello world', return_tensors='pt')
print('Token IDs:', ids['input_ids'])
print('T5-base tokenizer OK')
"
```

#### Step 3: Launch training

**LLaMA-350M with AdamW (4 GPUs):**

```bash
torchrun --standalone --nproc_per_node 4 main_pretrain.py \
  --model_config configs/llama_350m.json \
  --dataset allenai/c4 --dataset_config en \
  --tokenizer t5-base \
  --max_length 1024 \
  --batch_size 16 --total_batch_size 512 \
  --num_training_steps 10000 --warmup_steps 1000 \
  --lr 6e-4 --weight_decay 0.1 --grad_clipping 1.0 \
  --scheduler cosine --min_lr_ratio 0.1 \
  --dtype bfloat16 \
  --eval_every 1000 --save_every 5000 \
  --optimizer adamw
```

**LLaMA-350M with APOLLO (4 GPUs):**

```bash
torchrun --standalone --nproc_per_node 4 main_pretrain.py \
  --model_config configs/llama_350m.json \
  --dataset allenai/c4 --dataset_config en \
  --tokenizer t5-base \
  --max_length 1024 \
  --batch_size 128 --total_batch_size 512 \
  --num_training_steps 60000 --warmup_steps 6000 \
  --lr 0.01 --weight_decay 0 \
  --dtype bfloat16 \
  --eval_every 1000 \
  --optimizer apollo_adamw \
  --rank 256 --scale_type channel --proj random \
  --update_proj_gap 200 --apollo_scale 1
```

**Use a pre-built script:**

```bash
bash scripts/pretrain_c4/llama_60m.sh
bash scripts/pretrain_c4/llama_130m.sh
bash scripts/pretrain_c4/llama_350m.sh
bash scripts/pretrain_c4/llama_1b.sh
bash scripts/pretrain_c4/llama_7b.sh
bash scripts/pretrain_c4/llama_13b.sh
```

Each script contains multiple optimizer configurations — uncomment the one you want to use.

### Recipe 2: The Pile Pretraining (Qwen3)

**Scripts**: `scripts/pretrain_pile/`
**Configs**: `configs/qwen3_0.6b.json`, `configs/qwen3_1.7b.json`

#### Step 1: Download the dataset

The Pile is loaded from a **local copy** — it is not streamed from HF during training. You need to download it to disk first.

| Item | Value |
|------|-------|
| HF Dataset ID | [`monology/pile-uncopyrighted`](https://huggingface.co/datasets/monology/pile-uncopyrighted) |
| Access | Public, no authentication required |
| File format | Zstandard-compressed JSONL (`.jsonl.zst`) |
| Train shards | 30 files (`train/00.jsonl.zst` – `train/29.jsonl.zst`), ~11.1 GB each |
| Download size | **~335 GB** (compressed) |
| Rows | ~176M documents |
| Splits | `train`, `val` (~338 MB), `test` (~338 MB) |
| License | Derived from [The Pile](https://arxiv.org/abs/2101.00027) (MIT); copyrighted subsets removed |

> **What was removed**: Books3, BookCorpus2, OpenSubtitles, YTSubtitles, and OWT2 — the only Pile subsets not explicitly permitted for AI training.

Choose one of the following download methods:

**Option A: `huggingface-cli download` (recommended)**

The fastest and most robust method. Supports resumable downloads and parallel transfers:

```bash
pip install -U huggingface_hub

# Download the full dataset (~335 GB) to a local directory
huggingface-cli download monology/pile-uncopyrighted \
  --repo-type dataset \
  --local-dir ../datasets/pile
```

The downloaded directory structure will be:

```
../datasets/pile/
├── train/
│   ├── 00.jsonl.zst   # ~11.1 GB
│   ├── 01.jsonl.zst
│   ├── ...
│   └── 29.jsonl.zst
├── val.jsonl.zst      # ~338 MB
├── test.jsonl.zst     # ~338 MB
└── README.md
```

**Option B: Python `datasets` library**

```bash
# Download and convert to HF Arrow format (~335 GB download + ~800 GB Arrow on disk)
python -c "
from datasets import load_dataset
ds = load_dataset('monology/pile-uncopyrighted', split='train')
ds.save_to_disk('../datasets/pile')
"
```

> **Note**: This method downloads the raw files **and** converts them to Arrow format, which roughly doubles the disk usage (~335 GB download + ~800 GB Arrow). Use Option A if disk space is limited.

**Option C: Use the original EleutherAI Pile**

```bash
# Requires access approval on Hugging Face
python -c "
from datasets import load_dataset
ds = load_dataset('EleutherAI/pile', split='train')
ds.save_to_disk('../datasets/pile')
"
```

> **Note**: The original [EleutherAI/pile](https://huggingface.co/datasets/EleutherAI/pile) may require access approval. The `monology/pile-uncopyrighted` variant is openly available.

**Option D: Use an existing local copy**

If you already have The Pile in any HF-compatible format (Arrow / Parquet / JSONL), simply point `--dataset` to that directory:

```bash
--dataset /path/to/your/pile
```

**Verify the download:**

```bash
python -c "
from datasets import load_dataset
ds = load_dataset('../datasets/pile', split='train', streaming=True)
sample = next(iter(ds))
print('Keys:', list(sample.keys()))
print('Text preview:', sample['text'][:200])
print('Pile download OK')
"
```

#### Step 2: Download the tokenizer

The Qwen3 tokenizer is automatically downloaded from Hugging Face on first use (~11 MB). To pre-download for offline clusters:

```bash
# For Qwen3-0.6B
python -c "from transformers import AutoTokenizer; AutoTokenizer.from_pretrained('Qwen/Qwen3-0.6B-Base')"

# For Qwen3-1.7B
python -c "from transformers import AutoTokenizer; AutoTokenizer.from_pretrained('Qwen/Qwen3-1.7B-Base')"
```

| Model | Tokenizer HF ID | Vocab Size | Download |
|-------|------------------|------------|----------|
| Qwen3-0.6B | [`Qwen/Qwen3-0.6B-Base`](https://huggingface.co/Qwen/Qwen3-0.6B-Base) | 151,669 | ~11 MB |
| Qwen3-1.7B | [`Qwen/Qwen3-1.7B-Base`](https://huggingface.co/Qwen/Qwen3-1.7B-Base) | 151,669 | ~11 MB |

Verify the tokenizer is working:

```bash
python -c "
from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained('Qwen/Qwen3-0.6B-Base')
print('Vocab size:', tok.vocab_size)
ids = tok('Hello world', return_tensors='pt')
print('Token IDs:', ids['input_ids'])
print('Qwen3 tokenizer OK')
"
```

#### Step 3: Launch training

> **Note**: Qwen3 requires `--use_hf_model` so that `transformers` constructs the correct architecture via `AutoModelForCausalLM.from_config()`.

**Qwen3-0.6B with AdamW (4 GPUs):**

```bash
export TOKENIZERS_PARALLELISM=true

torchrun --standalone --nproc_per_node 4 main_pretrain.py \
  --use_hf_model \
  --model_config configs/qwen3_0.6b.json \
  --dataset ../datasets/pile \
  --tokenizer "Qwen/Qwen3-0.6B-Base" \
  --max_length 1024 \
  --batch_size 16 --total_batch_size 512 \
  --num_training_steps 10000 --warmup_steps 1000 \
  --lr 6e-4 --min_lr_ratio 0.1 \
  --scheduler cosine \
  --weight_decay 0.1 --grad_clipping 1.0 \
  --dtype bfloat16 \
  --eval_every 100 --save_every 1000 \
  --optimizer adamw
```

**Qwen3-1.7B with Muon (4 GPUs):**

```bash
export TOKENIZERS_PARALLELISM=true

torchrun --standalone --nproc_per_node 4 main_pretrain.py \
  --use_hf_model \
  --model_config configs/qwen3_1.7b.json \
  --dataset ../datasets/pile \
  --tokenizer "Qwen/Qwen3-1.7B-Base" \
  --max_length 1024 \
  --batch_size 8 --total_batch_size 512 \
  --num_training_steps 10000 --warmup_steps 1000 \
  --lr 3e-4 --min_lr_ratio 0.1 \
  --scheduler cosine \
  --weight_decay 0.1 --grad_clipping 1.0 \
  --dtype bfloat16 \
  --eval_every 100 --save_every 1000 \
  --optimizer muon
```

**Use a pre-built script:**

```bash
bash scripts/pretrain_pile/qwen3_0.6b_pile.sh
bash scripts/pretrain_pile/qwen3_1.7b_pile.sh
```

### Recipe 3: OpenWebText Pretraining (GPT-2)

**Scripts**: `scripts/pretrain_openwebtext/`
**Config**: `configs/gpt2_124m.json`

This pipeline is derived from [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT).

#### Step 1: Download and preprocess the dataset

OpenWebText requires a **one-time preprocessing step** that downloads the raw corpus from HF and converts it into nanoGPT-style binary files (`train.bin` / `val.bin`).

| Item | Value |
|------|-------|
| HF Dataset ID | [`Skylion007/openwebtext`](https://huggingface.co/datasets/Skylion007/openwebtext) (aliased as `openwebtext`) |
| Access | Public, no authentication required |
| Documents | 8,013,769 |
| License | [CC0](https://creativecommons.org/share-your-work/public-domain/cc0/) (public domain) |

**Disk space requirements:**

| Phase | Size | Description |
|-------|------|-------------|
| HF download | ~13.5 GB | Compressed dataset files |
| HF cache | ~54 GB | Decompressed + cached by HF `datasets` |
| Output: `train.bin` | ~17 GB | ~9B tokens as uint16 |
| Output: `val.bin` | ~8.5 MB | ~4.4M tokens as uint16 |
| **Total needed** | **~85 GB** | During preparation (HF cache can be cleaned afterwards) |

**Step 1a: Install `tiktoken` (recommended, optional)**

The preparation script prefers `tiktoken` for GPT-2 BPE tokenization (2–3× faster than the HF tokenizer). It falls back to `GPT2TokenizerFast` if `tiktoken` is not installed:

```bash
pip install tiktoken
```

**Step 1b: Run the preparation script**

```bash
python data/openwebtext/prepare.py --output_dir data/openwebtext
```

This script performs the following steps automatically:
1. Downloads the OpenWebText corpus from [`Skylion007/openwebtext`](https://huggingface.co/datasets/Skylion007/openwebtext) on Hugging Face
2. Splits into train (99.95%) and validation (0.05%) sets
3. Tokenizes all documents using GPT-2 BPE (via `tiktoken` or `GPT2TokenizerFast` as fallback)
4. Concatenates all token IDs and writes binary files: `train.bin`, `val.bin` (uint16), and `meta.pkl`

**Advanced preparation options:**

```bash
python data/openwebtext/prepare.py \
  --output_dir data/openwebtext \
  --num_proc 16 \
  --val_ratio 0.0005 \
  --seed 2357
```

| Argument | Default | Description |
|----------|---------|-------------|
| `--output_dir` | `data/openwebtext/` | Output directory for binary files |
| `--num_proc` | 8 | Parallel workers for tokenization (more = faster) |
| `--val_ratio` | 0.0005 | Fraction reserved for validation |
| `--seed` | 2357 | Random seed for train/val split |

> **Tip**: On machines with many cores, increasing `--num_proc` (e.g. 32 or 64) significantly speeds up tokenization. The download step itself is single-threaded and takes the most time.

**Step 1c: Verify the output**

After preparation completes, verify the binary files were created correctly:

```bash
python -c "
import os, numpy as np

for name in ['train.bin', 'val.bin']:
    path = os.path.join('data/openwebtext', name)
    data = np.memmap(path, dtype=np.uint16, mode='r')
    print(f'{name}: {len(data):,} tokens ({os.path.getsize(path) / 1e9:.2f} GB)')
    print(f'  First 10 tokens: {data[:10].tolist()}')
    print(f'  Max token ID: {data.max()} (should be < 50257)')
print('OpenWebText preparation OK')
"
```

Expected output:

```
train.bin: ~9,035,582,198 tokens (17.07 GB)
val.bin:   ~4,434,897 tokens (0.01 GB)
```

#### Step 2: Download the tokenizer

The GPT-2 tokenizer is automatically downloaded on first use (~2 MB). To pre-download for offline clusters:

```bash
python -c "from transformers import AutoTokenizer; AutoTokenizer.from_pretrained('gpt2')"
```

| Item | Value |
|------|-------|
| Tokenizer | [`gpt2`](https://huggingface.co/gpt2) (BPE, vocab size 50,257) |
| Download size | ~2 MB |

> **Note**: The `prepare.py` script uses `tiktoken` (if installed) for tokenization, which produces identical token IDs to the HF tokenizer but runs faster. The training script itself uses `AutoTokenizer.from_pretrained("gpt2")` for the dataloader.

Verify the tokenizer is working:

```bash
python -c "
from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained('gpt2')
print('Vocab size:', tok.vocab_size)
ids = tok('Hello world', return_tensors='pt')
print('Token IDs:', ids['input_ids'])
print('GPT-2 tokenizer OK')
"
```

#### Step 3: Launch training

**Train with the default script (8 GPUs):**

```bash
bash scripts/pretrain_openwebtext/gpt2_124m.sh data/openwebtext
```

Default configuration: 8 GPUs, micro-batch 12, total batch 480, seq length 1024, 600K steps, AdamW.

**Customize via environment variables or extra flags:**

```bash
# Change GPU count and optimizer
NPROC=4 OPTIMIZER=apollo_adamw bash scripts/pretrain_openwebtext/gpt2_124m.sh data/openwebtext

# Or pass extra arguments after the data directory
bash scripts/pretrain_openwebtext/gpt2_124m.sh data/openwebtext \
  --optimizer apollo_adamw --rank 128 --update_proj_gap 50
```

**Available environment overrides:**

| Variable | Default | Description |
|----------|---------|-------------|
| `NPROC` | 8 | Number of GPUs |
| `MICRO_BATCH_SIZE` | 12 | Per-GPU micro-batch size |
| `TOTAL_BATCH_SIZE` | 480 | Global batch size |
| `SEQ_LEN` | 1024 | Sequence length |
| `NUM_STEPS` | 600000 | Training steps |
| `WARMUP_STEPS` | 2000 | Warmup steps |
| `LR` | 6e-4 | Learning rate |
| `OPTIMIZER` | adamw | Optimizer name |

> **Note**: When `--dataset` points to a directory containing `train.bin`, the dataloader auto-detects nanoGPT-style binaries. Loss masking uses `attention_mask` to avoid edge cases where `eos_token_id == pad_token_id` (common in GPT-2 tokenizers).

### Recipe 4: Single-GPU Low-Memory Training

**Scripts**: `scripts/single_gpu/`

These configurations are designed for research on a single GPU (as low as 12 GB VRAM) using quantized weights and per-layer optimizer variants.

#### Example: LLaMA-7B with Q-APOLLO per-layer (single GPU, ~12 GB)

```bash
torchrun --standalone --nproc_per_node 1 main_pretrain.py \
  --model_config configs/llama_7b.json \
  --batch_size 1 --total_batch_size 1 \
  --lr 0.01 --warmup_steps 15000 --num_training_steps 150000 \
  --dtype bfloat16 \
  --eval_every 1000 \
  --optimizer q_apollo_per_layer \
  --weight_quant --weight_group_size 128 --stochastic_round \
  --rank 1 --scale_type tensor --proj random \
  --update_proj_gap 200 --apollo_scale 128 \
  --weight_decay 0 \
  --single_gpu
```

**Use a pre-built script:**

```bash
bash scripts/single_gpu/llama_7b_q_apollo_mini_per_layer.sh
```

---

## SFT / DPO / GRPO Training (TRL Integration)

ScalingOPT integrates with [TRL (Transformer Reinforcement Learning)](https://huggingface.co/docs/trl) to provide **SFT**, **DPO**, and **GRPO** training with **all 30+ optimizers**.

### Prerequisites

```bash
pip install trl peft accelerate
```

### Entry Points

| Script | Framework | Training Paradigm |
|--------|-----------|-------------------|
| `main_sft.py` | TRL SFTTrainer | Supervised Fine-Tuning (full + LoRA) |
| `main_dpo.py` | TRL DPOTrainer | Direct Preference Optimization (full + LoRA) |
| `main_grpo.py` | TRL GRPOTrainer | Group Relative Policy Optimization (full + LoRA) |

### SFT Examples

**Full SFT with Muon optimizer:**

```bash
accelerate launch --num_processes 4 main_sft.py \
  --model_name_or_path meta-llama/Llama-2-7b-hf \
  --dataset_name tatsu-lab/alpaca \
  --optimizer muon --lr 2e-5 \
  --per_device_train_batch_size 4 --gradient_accumulation_steps 4 \
  --gradient_checkpointing --bf16 --num_train_epochs 3
```

**LoRA SFT with APOLLO:**

```bash
accelerate launch --num_processes 4 main_sft.py \
  --model_name_or_path meta-llama/Llama-2-7b-hf \
  --dataset_name tatsu-lab/alpaca \
  --use_lora --lora_r 16 --lora_alpha 32 \
  --optimizer apollo_adamw --lr 1e-4 \
  --rank 256 --scale_type channel --proj random \
  --update_proj_gap 200 --apollo_scale 1.0 \
  --per_device_train_batch_size 8 --gradient_accumulation_steps 2 \
  --gradient_checkpointing --bf16 --num_train_epochs 3
```

**QLoRA SFT (4-bit base model + LoRA) with AdamW:**

```bash
accelerate launch main_sft.py \
  --model_name_or_path meta-llama/Llama-2-7b-hf \
  --dataset_name tatsu-lab/alpaca \
  --use_qlora --lora_r 16 --lora_alpha 32 \
  --optimizer adamw --lr 2e-4 --weight_decay 0.1 \
  --per_device_train_batch_size 4 --gradient_accumulation_steps 4 \
  --gradient_checkpointing --bf16 --num_train_epochs 3
```

### DPO Examples

**Full DPO with SOAP:**

```bash
accelerate launch --num_processes 4 main_dpo.py \
  --model_name_or_path meta-llama/Llama-2-7b-hf \
  --dataset_name trl-lib/ultrafeedback_binarized \
  --optimizer soap --lr 5e-7 \
  --beta 0.1 --loss_type sigmoid \
  --per_device_train_batch_size 2 --gradient_accumulation_steps 8 \
  --gradient_checkpointing --bf16
```

**LoRA DPO with AdamW:**

```bash
accelerate launch --num_processes 4 main_dpo.py \
  --model_name_or_path meta-llama/Llama-2-7b-hf \
  --dataset_name trl-lib/ultrafeedback_binarized \
  --use_lora --lora_r 16 \
  --optimizer adamw --lr 5e-6 --weight_decay 0.1 \
  --beta 0.1 --loss_type sigmoid \
  --per_device_train_batch_size 4 --gradient_accumulation_steps 4 \
  --gradient_checkpointing --bf16
```

### GRPO Examples

**Full GRPO with Adam-Mini (math reasoning):**

```bash
accelerate launch --num_processes 4 main_grpo.py \
  --model_name_or_path Qwen/Qwen2-0.5B-Instruct \
  --dataset_name trl-lib/DeepMath-103K \
  --optimizer adam_mini --lr 5e-6 \
  --beta 0.04 --num_generations 4 --reward_funcs accuracy \
  --per_device_train_batch_size 2 --gradient_accumulation_steps 8 \
  --gradient_checkpointing --bf16
```

**LoRA GRPO with Schedule-Free AdamW:**

```bash
accelerate launch --num_processes 4 main_grpo.py \
  --model_name_or_path Qwen/Qwen2-0.5B-Instruct \
  --dataset_name trl-lib/DeepMath-103K \
  --use_lora --lora_r 16 \
  --optimizer adamw_schedulefree --lr 5e-5 \
  --beta 0.04 --num_generations 4 --reward_funcs accuracy \
  --per_device_train_batch_size 4 --gradient_accumulation_steps 4 \
  --gradient_checkpointing --bf16
```

### Ready-to-Run Scripts

All scripts follow the same optimizer-agnostic pattern — uncomment one `OPTIMIZER_ARGS` block and run:

| Script | Paradigm |
|--------|----------|
| `scripts/sft_trl/sft_full.sh` | Full SFT |
| `scripts/sft_trl/sft_lora.sh` | SFT + LoRA |
| `scripts/dpo_trl/dpo_full.sh` | Full DPO |
| `scripts/dpo_trl/dpo_lora.sh` | DPO + LoRA |
| `scripts/grpo_trl/grpo_full.sh` | Full GRPO |
| `scripts/grpo_trl/grpo_lora.sh` | GRPO + LoRA |
| `scripts/ppo_openrlhf/ppo.sh` | OpenRLHF PPO / GRPO / REINFORCE++ |

### Optimizer Factory (for custom integrations)

The standalone optimizer factory can be used with **any** training framework:

```python
from utils.optimizer_factory import create_optimizer

optimizer = create_optimizer(
    model,
    "apollo_adamw",
    lr=1e-4,
    rank=256,
    scale_type="channel",
    proj="random",
    update_proj_gap=200,
    apollo_scale=1.0,
)

# Pass to any TRL trainer:
trainer = SFTTrainer(model=model, ..., optimizers=(optimizer, None))

# Or use in a custom training loop:
for batch in dataloader:
    loss = model(**batch).loss
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()
```

### OpenRLHF Integration

[OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) is recommended for large-scale distributed RL training (PPO, GRPO, REINFORCE++, RLOO). See `scripts/ppo_openrlhf/ppo.sh` for setup instructions and integration examples.

---

## Evaluation

ScalingOPT wraps [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) to provide one-command evaluation on all popular benchmarks.

### Prerequisites

```bash
pip install "lm_eval[hf]"
# For vLLM backend (faster for large models):
pip install "lm_eval[vllm]"
```

### Preset Benchmark Suites

| Suite | Benchmarks | Best For |
|-------|-----------|----------|
| `quick` | HellaSwag, ARC-C, Winogrande, TruthfulQA | Fast sanity check |
| `pretrain` | LAMBADA, WikiText | Pretraining quality (perplexity) |
| `knowledge` | MMLU, ARC-C/E, HellaSwag, Winogrande, TruthfulQA, PIQA, BoolQ, OpenBookQA | Knowledge & understanding |
| `reasoning` | GSM8K, MATH, BBH | Math & reasoning |
| `code` | HumanEval | Code generation |
| `instruction` | IFEval | Instruction following |
| `leaderboard` | MMLU-Pro, GPQA, MuSR, MATH-Hard, IFEval, BBH | HuggingFace Open LLM Leaderboard v2 |
| `full` | All of the above (14 benchmarks) | Comprehensive evaluation |

### Quick Examples

**Evaluate a pretrained checkpoint:**

```bash
python main_eval.py \
  --model_name_or_path ./ckpts/llama_350m \
  --suite pretrain
```

**Evaluate after SFT (with LoRA adapter):**

```bash
python main_eval.py \
  --model_name_or_path meta-llama/Llama-2-7b-hf \
  --lora_path ./outputs/sft_lora/checkpoint-500 \
  --suite knowledge
```

**Run Open LLM Leaderboard v2 benchmarks:**

```bash
python main_eval.py \
  --model_name_or_path meta-llama/Llama-2-7b-hf \
  --suite leaderboard
```

**Custom task selection:**

```bash
python main_eval.py \
  --model_name_or_path meta-llama/Llama-2-7b-hf \
  --tasks mmlu gsm8k arc_challenge hellaswag
```

**Use vLLM backend (faster for 7B+ models):**

```bash
python main_eval.py \
  --model_name_or_path meta-llama/Llama-2-7b-hf \
  --backend vllm --tensor_parallel_size 4 \
  --suite full
```

**Quick test with sample limit (for debugging):**

```bash
python main_eval.py \
  --model_name_or_path meta-llama/Llama-2-7b-hf \
  --suite quick --limit 100
```

### Ready-to-Run Eval Scripts

| Script | Description |
|--------|-------------|
| `scripts/eval/eval_pretrain.sh` | Evaluate pretrained models (perplexity) |
| `scripts/eval/eval_sft.sh` | Evaluate SFT / instruction models (knowledge + reasoning) |
| `scripts/eval/eval_reasoning.sh` | Math & reasoning focused (GSM8K, MATH, BBH) |
| `scripts/eval/eval_leaderboard.sh` | Official HF Open LLM Leaderboard v2 suite |
| `scripts/eval/eval_full.sh` | Full comprehensive evaluation (14 benchmarks) |
| `scripts/eval/eval_custom.sh` | Template for custom task selection |

Results are saved as JSON to `--output_dir` (default: `./eval_results/`) and printed as a table to stdout.

---

## Full CLI Reference

### Experiment Setup

| Argument | Default | Description |
|----------|---------|-------------|
| `--model_config` | **required** | Path to model config JSON |
| `--use_hf_model` | `False` | Use `AutoModelForCausalLM` instead of local LLaMA |
| `--single_gpu` | `False` | Single-GPU mode (no DDP) |
| `--dtype` | `bfloat16` | Data type: `bfloat16` or `float32` |
| `--seed` | `0` | Random seed |
| `--workers` | `8` | DataLoader workers |
| `--activation_checkpointing` | `False` | Enable gradient checkpointing |

### Dataset & Tokenizer

| Argument | Default | Description |
|----------|---------|-------------|
| `--dataset` | `allenai/c4` | HF dataset name or local directory |
| `--dataset_config` | `None` | Dataset config (auto-set to `"en"` for C4) |
| `--train_split` | `train` | Training split name |
| `--eval_split` | `validation` | Evaluation split name |
| `--dataset_text_field` | `text` | Text field name in dataset |
| `--tokenizer` | `t5-base` | Tokenizer name or path |
| `--packing` | `False` | Enable token packing |
| `--add_eos` | `False` | Add EOS between packed documents |
| `--shuffle_seed` | `42` | Shuffle seed for dataset |

### Training Hyperparameters

| Argument | Default | Description |
|----------|---------|-------------|
| `--batch_size` | **required** | Per-GPU micro-batch size |
| `--total_batch_size` | `None` | Global batch size (auto-derives gradient accumulation) |
| `--gradient_accumulation` | `None` | Manual gradient accumulation steps |
| `--lr` | `1e-4` | Learning rate |
| `--warmup_steps` | `1000` | Linear warmup steps |
| `--num_training_steps` | `10000` | Total update steps |
| `--max_train_tokens` | `None` | Token budget (e.g. `100M`, `1B`); overrides `--num_training_steps` |
| `--optimizer` | `Adam` | Optimizer name (see [Optimizers](#optimizers)) |
| `--max_length` | `256` | Sequence length |
| `--scheduler` | `cosine` | LR schedule: `linear`, `cosine`, `cosine_restarts` |
| `--min_lr_ratio` | `0.1` | Minimum LR ratio for cosine decay |
| `--weight_decay` | `0.0` | Weight decay |
| `--grad_clipping` | `0.0` | Gradient clipping (0 = disabled) |

### Evaluation & Saving

| Argument | Default | Description |
|----------|---------|-------------|
| `--eval_every` | `5000` | Evaluate every N update steps |
| `--save_every` | `10000` | Save checkpoint every N steps |
| `--save_dir` | auto | Checkpoint directory (auto-generated from config + timestamp) |

### Wandb

| Argument | Default | Description |
|----------|---------|-------------|
| `--project` | `test` | W&B project name |
| `--name` | `test` | W&B run name |
| `--entity` | `None` | W&B entity |
| `--tags` | `None` | Comma-separated W&B tags |
| `--unset_wandb` | `False` | Disable W&B logging |

### JSONL Logging

| Argument | Default | Description |
|----------|---------|-------------|
| `--jsonl_log_path` | `None` | JSONL log file path (`"auto"` → `<save_dir>/metrics.jsonl`) |
| `--jsonl_log_every` | `1` | Log training metrics every N steps |

---

## Checkpointing and Resuming

Checkpoints are saved to `--save_dir` (auto-generated if not specified). Each checkpoint contains model weights, optimizer state, and scheduler state.

### Resume training

```bash
# Resume from latest checkpoint (weights only)
torchrun --standalone --nproc_per_node 4 main_pretrain.py \
  --model_config configs/llama_350m.json \
  --continue_from ./checkpoints/llama_350m-2025-01-15-10-30-00 \
  ... # other arguments

# Resume with optimizer and scheduler state
torchrun --standalone --nproc_per_node 4 main_pretrain.py \
  --model_config configs/llama_350m.json \
  --continue_from ./checkpoints/llama_350m-2025-01-15-10-30-00 \
  --restore_optimizer \
  ... # other arguments

# Resume from a specific step
torchrun --standalone --nproc_per_node 4 main_pretrain.py \
  --model_config configs/llama_350m.json \
  --continue_from ./checkpoints/llama_350m-2025-01-15-10-30-00 \
  --restore_optimizer \
  --resume_step 5000 \
  ... # other arguments
```

See `scripts/example.sh` for a complete resume pattern.

---

## Logging

### Weights & Biases

Enabled by default on rank 0. Configure with:

```bash
--project my_project --name my_run --entity my_team --tags "llama,apollo"
```

Disable with `--unset_wandb`.

### JSONL Logging

Append-only JSON Lines logging for offline analysis and reproducibility:

```bash
--jsonl_log_path auto            # Writes to <save_dir>/metrics.jsonl
--jsonl_log_path logs/run1.jsonl # Custom path
--jsonl_log_every 10             # Log every 10 steps
```

Each line is a JSON object with a `type` field:
- `"config"` — full run configuration snapshot
- `"train"` — per-update training metrics (loss, ppl, LR, throughput, etc.)
- `"eval"` / `"final_eval"` — evaluation metrics (loss, ppl, tokens)

### Tracked Metrics

| Metric | Logged To | Description |
|--------|-----------|-------------|
| `loss` | wandb, JSONL, console | Cross-entropy loss |
| `ppl` | wandb, JSONL, console | Perplexity (exp(loss)) |
| `lr` | wandb, JSONL | Current learning rate |
| `tokens_seen` | wandb, JSONL | Cumulative tokens processed |
| `throughput_tokens` | wandb, JSONL | Tokens per second |
| `throughput_examples` | wandb, JSONL | Examples per second |
| `total_svd_count` | wandb, JSONL | SVD projection count (for GaLore/APOLLO) |
| `eval_loss` / `eval_ppl` | wandb, JSONL, console | Evaluation loss and perplexity |

---

## License

This repository is licensed under **CC BY-NC 4.0** (Creative Commons Attribution-NonCommercial 4.0 International). See `LICENSE` for details.

**Important notes:**
- CC BY-NC 4.0 is a **non-commercial license** and is **not** an OSI-approved open-source software license.
- Third-party files retain their original licenses where specified in file headers; consult `THIRD_PARTY_NOTICES.md` and upstream projects before redistribution.

## Citation and Attribution

If you use ScalingOPT in academic work, please cite the relevant optimizer papers and credit upstream sources listed in `THIRD_PARTY_NOTICES.md`. For community context and related resources, see the [ScalingOpt Community](https://tianshijing.github.io/ScalingOpt/).
