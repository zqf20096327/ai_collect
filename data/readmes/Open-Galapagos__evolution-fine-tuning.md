<p align="center">
  <img src="assets/finch_icon.png" width="110" alt="Finch logo">
</p>

<h1 align="center">Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks</h1>

<p align="center">
  A mid-training "practice phase" that teaches small open-source LLMs <b>how to evolve solutions</b>.
</p>

<p align="center">
  <a href="https://arxiv.org/abs/2606.29082"><img src="https://img.shields.io/badge/arXiv-2606.29082-b31b1b.svg" alt="arXiv"></a>
  <a href="https://open-galapagos.github.io/evolution_finetuning/"><img src="https://img.shields.io/badge/Project-Page-1E90FF.svg" alt="Project Page"></a>
  <a href="https://huggingface.co/datasets/minnesotanlp/Finch-Collection"><img src="https://img.shields.io/badge/%F0%9F%A4%97-Finch--Collection-FFD21E.svg" alt="Dataset"></a>
  <a href="https://huggingface.co/collections/minnesotanlp/evolution-fine-tuning"><img src="https://img.shields.io/badge/%F0%9F%A4%97-Finch%20Models-FFD21E.svg" alt="Models"></a>
  <img src="https://img.shields.io/badge/license-Apache--2.0-green.svg" alt="License">
</p>

---

## Table of Contents

- [News](#news)
- [Finch Models](#finch-models)
- [Installation](#installation)
- [Repository Structure](#repository-structure)
- [Quickstart](#quickstart)
- [TL;DR](#tldr)
- [Citation](#citation)
- [License](#license)
- [Acknowledgement](#acknowledgement)

## News

- **Jun 2026 · 📦 Dataset update** — Expanded the Finch Collection with **71 additional optimization tasks** (371 → 442) and **61,049 additional trajectories** (156,731 → 217,780). Teacher trajectories from **GPT-5.4** and **Gemini-3-Flash** are now also available ([GPT-5.4](https://huggingface.co/datasets/minnesotanlp/Finch-Collection-GPT-5.4) · [Gemini-3-Flash](https://huggingface.co/datasets/minnesotanlp/Finch-Collection-Gemini-3-Flash)).
- **Jun 2026 · 🎤 Talk** — Invited talk at the **[AiDDA Conference 2026](https://luma.com/AIDDA2026)** (Virtual), OpenEvolve Team Session.
- **May 2026 · 🏆 Oral** — EFT accepted as an **Oral** at the **[CAIS 2026 Workshop on AI Agents for Discovery in the Wild (AID-Wild)](https://ai-discovery-in-the-wild.github.io/)**, with an invited talk in the OpenEvolve Team Demo Session (San Jose, CA).



## Finch models

| Model | Base | 🤗 Hugging Face |
|---|---|---|
| Finch-2B | Qwen3.5-2B | [minnesotanlp/Finch-2B](https://huggingface.co/minnesotanlp/Finch-2B) |
| Finch-4B | Qwen3.5-4B | [minnesotanlp/Finch-4B](https://huggingface.co/minnesotanlp/Finch-4B) |
| Finch-8B | Qwen3-8B | [minnesotanlp/Finch-8B](https://huggingface.co/minnesotanlp/Finch-8B) |
| Finch-9B | Qwen3.5-9B | [minnesotanlp/Finch-9B](https://huggingface.co/minnesotanlp/Finch-9B) |
| Finch-4B-KTO | Finch-4B | [minnesotanlp/Finch-4B-KTO](https://huggingface.co/minnesotanlp/Finch-4B-KTO) |
| Finch-8B-KTO | Finch-8B | [minnesotanlp/Finch-8B-KTO](https://huggingface.co/minnesotanlp/Finch-8B-KTO) |

## Installation

SkyDiscover uses [`uv`](https://github.com/astral-sh/uv). Install the core
framework plus the benchmark extras you need:

```bash
cd skydiscover
uv sync --extra math --extra adrs --extra frontier-cs --extra external --extra algotune
```

<details>
<summary><b>Task- and benchmark-specific setup</b></summary>

```bash
# Symbolic regression
uv pip install h5py
uv run python data_api.py

# Math (e.g. Erdős minimum-overlap) — JAX on CUDA 12
uv pip install "jax[cuda12]"

# ALE-Bench (AtCoder Heuristic Contest tasks)
git clone https://github.com/SakanaAI/ALE-Bench.git
cd ALE-Bench && uv pip install -e . && uv pip install ".[eval]" && cd ..

# Frontier-CS (competitive programming; requires Docker)
cd benchmarks/frontier-cs-eval
git clone https://github.com/FrontierCS/Frontier-CS.git
cd Frontier-CS/algorithmic && docker compose up -d   # start the judge server
cd ../../../..
uv sync --extra frontier-cs

# Biology (scRNA-seq denoising)
# NOTE: the biology task needs a different numpy version that conflicts with the
# other tasks, so install it separately in its own environment.
git clone https://github.com/openproblems-bio/openproblems.git
cd openproblems && git checkout v1.0.0 && cd ..
uv sync --extra math --extra adrs --extra frontier-cs --extra external \
        --extra prompt-optimization --extra algotune --extra biology
cd openproblems
git apply ../benchmarks/biology/denoising/evaluator/openproblems_api_fix.patch
cd ..
```

</details>

<details>
<summary><b>Training environment (LLaMA-Factory)</b></summary>

```bash
conda create -n train_env -y python==3.12
conda activate train_env
conda install -c conda-forge cuda-nvcc cuda-toolkit -y

git clone --depth 1 https://github.com/hiyouga/LlamaFactory.git
cd LlamaFactory
pip install -e .
pip install -r requirements/metrics.txt -r requirements/deepspeed.txt
pip install wandb
pip install flash-attn --no-build-isolation --no-cache-dir

# Qwen3.5 kernels
pip install "flash-linear-attention>=0.4.1" causal-conv1d --no-build-isolation
pip install tilelang liger-kernel
```

</details>


## Repository structure

```
.
├── dataset_construction/   # Build the Finch Collection: filter & label harvested trajectories
├── train/                  # EFT (SFT) training configs
├── skydiscover/            # Discovery framework + benchmarks
│   ├── scripts/            #   Trajectory collection (Qwen3.5-397B teacher via OpenEvolve)
│   └── eval_scripts/       #   Evaluation: serve & run Finch across the benchmark suite
└── openevolve/             # Vendored OpenEvolve scaffold
```

## Quickstart

Each component is self-contained; see its directory for details.

```bash
# 0) Install SkyDiscover (see Installation above for benchmark extras)
cd skydiscover && uv sync && cd ..

# 1) Collect trajectories with the Qwen3.5-397B teacher (OpenEvolve scaffold)
skydiscover/scripts/run_math_openevolve.sh

# 2) Build the Finch Collection (filter + select trajectories)
bash dataset_construction/scripts/run_pipeline.sh

# 3) Train (example config; uses LLaMA-Factory-style YAML)
#    llamafactory-cli train train/qwen3_5_eft_config.yaml

# 4) Evaluate: serve a Finch checkpoint, then run a benchmark
skydiscover/eval_scripts/run_vllm.sh     # serve a Finch checkpoint
skydiscover/eval_scripts/run_math.sh     # run a benchmark
```

> Set provider API keys via environment variables (e.g. `OPENROUTER_API_KEY`); no keys are committed to this repo.

> [!NOTE]
> **You don't have to use our evaluation code.** Finch is just a mutation operator, so you can drop it into your own evolutionary search scaffold, or clone [SkyDiscover](https://github.com/skydiscover-ai/skydiscover) and run it there. The `skydiscover/eval_scripts/` here are provided only as a convenient reference setup.


## TL;DR

State-of-the-art discovery systems put an LLM inside an evolutionary search *scaffold*, but the discovery know-how lives in the scaffold and every new task starts from zero. **Evolution Fine-Tuning (EFT)** moves that behavior *into the model* by turning evolutionary search **trajectories** into supervision.

<p align="center">
  <img src="assets/eft_concept_teaser.png" width="480" alt="EFT internalizes discovery capability into the model (Finch), usable in both test-time search and test-time RL">
</p>

We build the **[Finch Collection](https://huggingface.co/datasets/minnesotanlp/Finch-Collection)** — 156K trajectories across 10 domains and 371 optimization tasks — and fine-tune open-source LLMs (2B–9B) into the **Finch** family. Across 22 held-out tasks, Finch models beat their base counterparts by **+10.22% on average**.

<p align="center">
  <img src="assets/intro_teaser.png" width="960" alt="EFT as mid-training and cross-discovery transfer via Finch">
</p>

The collection is built in three steps:

1. **Seed task collection.** We source 371 tasks from 10 domains, spanning mathematical discovery, competitive programming, heuristic optimization, numerical algorithm optimization, symbolic regression (physics oscillation, biological population growth, chemical reaction), GPU kernel optimization, constructive search, and biological denoising.
2. **Trajectory collection.** We run the OpenEvolve scaffold with **Qwen3.5-397B-A17B** as the teacher mutation operator under two strategies — diff-based edit (exploitation) and full rewrite (exploration) — at temperature 0.7, top-p 0.95, and a 30K-token generation budget, yielding **172,997** raw trajectories.
3. **Filtering & labeling.** We discard systematic errors, unrecoverable/breakage cases, and overlong inputs (90.6% retained → **156,731**), then label each transition by its score delta.

<p align="center">
  <img src="assets/eft_method.png" width="960" alt="Finch Collection construction pipeline: seed tasks, trajectory collection, filtering">
</p>



## Citation

```bibtex
@misc{lee2026evolutionfinetuninglearningdiscover,
  title         = {Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks},
  author        = {Young-Jun Lee and Seungone Kim and Minki Kang and Alistair Cheong Liang Chuen
                   and Zerui Chen and Seungho Han and Taehee Jung and Dongyeop Kang},
  year          = {2026},
  eprint        = {2606.29082},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/2606.29082}
}
```


## License

The **Finch Collection** is released under the [**CC-BY 4.0**](https://creativecommons.org/licenses/by/4.0/) license and is intended for **non-commercial academic research**. The accompanying **code** and **Finch model weights** are released under the [**Apache 2.0**](https://www.apache.org/licenses/LICENSE-2.0) license; the vendored `openevolve/` and `skydiscover/` components retain their own `LICENSE` files.

## Acknowledgement

This research was supported by the "Advanced GPU Utilization Support Program" funded by the Government of the Republic of Korea (Ministry of Science and ICT). We are grateful to the SkyDiscover team for their valuable feedback on the dataset construction process, the use of the SkyDiscover framework, and the overall direction of this research — in particular, [Shu Liu](https://shulynnliu.com/), [Shubham Agarwal](https://skejriwal44.github.io/), and [Mert Cemri](https://people.eecs.berkeley.edu/~mert_cemri/) for their insightful comments and discussions. We also thank the OpenEvolve team, especially Ritik Vijayvergiya and [Asankhaya Sharma](https://asankhaya.github.io/), for their guidance on using the OpenEvolve framework and for their thoughtful comments on this work. We further thank the authors of ALE-Bench, especially [Yuki Imajuku](https://imajuku.tech/), and the AtCoder team for authorizing the public release of the evolutionary search trajectories derived from their CC BY-ND 4.0-licensed dataset. Finally, we thank [Byung-Kwan Lee](https://byungkwanlee.github.io/ByungKwanLee-CV/) for valuable feedback during the early stages of this project.

