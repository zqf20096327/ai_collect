# GaMMA: Towards Joint Global-Temporal Music Understanding in Large Multimodal Models

<a href='http://arxiv.org/abs/2605.00371'><img src='https://img.shields.io/badge/ArXiv-Paper-red' /></a> <a href='https://geshang777.github.io/GaMMA/'><img src='https://img.shields.io/badge/Project-Page-Green'></a> <a href='https://huggingface.co/spaces/geshang/GaMMA'><img src='https://img.shields.io/badge/Web-Demo-blue'></a> <a href='https://huggingface.co/collections/geshang/gamma-8b'><img src='https://img.shields.io/badge/HuggingFace-Model-yellow' /></a>

## Overview

Introducing GaMMA, a large multimodal model designed to jointly handle both global music understanding and temporal music reasoning within a unified parameter space. Built on a streamlined encoder-decoder paradigm, GaMMA combines language modeling with dual audio experts and a gated fusion mechanism to model both non-temporal musical semantics and time-dependent musical structure, while a progressive training pipeline based on pretraining, supervised fine-tuning, and reinforcement learning further strengthens instruction-following, full-song understanding, and temporal reasoning.

<p align="center">
  <img src="assets/gamma_teaser.png" width="100%" alt="GaMMA demo" />
</p>

<!-- <p align="center">
  <img src="assets/gamma_framework.jpg" width="100%" alt="GaMMA framework" />
</p> -->

## News

- `[2026-5-1]`:🔥 GaMMA is released! Check out our [project page](https://geshang777.github.io/GaMMA/) and [paper](http://arxiv.org/abs/2605.00371).

## Installation

- We use python 3.12 and CUDA 12.4 for implementation.
- The inference code runs on NVIDIA A100 GPUs with 80 GB of memory. Please ensure your available VRAM is sufficient to avoid potential out-of-memory (OOM) issues.

### PyTorch Inference

```bash
conda create -n gamma python=3.12 -y
conda activate gamma

pip install --extra-index-url https://download.pytorch.org/whl/cu121 torch==2.5.1 torchaudio==2.5.1
pip install -r requirements.txt

export CUDA_HOME=/usr/local/cuda
export PATH=$CUDA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH

# flash-attn build can take a long time in a fresh environment.
pip install --no-build-isolation --no-cache-dir flash-attn==2.8.0.post2
```

### Optional: vLLM Inference

```bash
conda create -n gamma_vllm python=3.12 -y
conda activate gamma_vllm

export CUDA_HOME=/usr/local/cuda
export PATH=$CUDA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH

pip install torch==2.10.0+cu128 torchaudio==2.10.0+cu128 --index-url https://download.pytorch.org/whl/cu128
pip install torchvision==0.25.0+cu128 --index-url https://download.pytorch.org/whl/cu128
pip install numpy==2.2.6
pip install -r requirements-vllm.txt
pip install transformers==4.57.6
pip install --no-build-isolation --no-cache-dir flash-attn==2.8.0.post2 causal-conv1d==1.6.0
pip install setuptools-scm "cmake>=3.26.1" uv
cd vllm
mkdir -p vllm/vllm_flash_attn
export SETUPTOOLS_SCM_PRETEND_VERSION=0.17.1
export UV_LINK_MODE=copy
export UV_CACHE_DIR=/tmp/build_tmp/uv-cache
export TMPDIR=/tmp/build_tmp
python use_existing_torch.py --prefix
uv pip install -r requirements/build.txt
uv pip install --no-build-isolation -e .
cd ..
```

## Quick Start

### PyTorch CLI

```bash
python demo/web_demo_mmaudio.py \
  --mode cli \
  --model-path /absolute/path/to/your/checkpoint \
  --audio-file /absolute/path/to/your/audio.mp3 \
  --question "Please briefly describe the style, mood and main vocal characteristics of this song."
```

### PyTorch Web Demo

```bash
python demo/web_demo_mmaudio.py \
  --mode web \
  --model-path /absolute/path/to/your/checkpoint
```

### vLLM CLI

```bash
python demo/web_demo_mmaudio_vllm.py \
  --gpu-memory-utilization 0.9 \
  --max-num-seqs 2 \
  --max-model-len 32768 \
  --model-path /absolute/path/to/your/checkpoint \
  --audio-file /absolute/path/to/your/audio.mp3 \
  --question "Please briefly describe the style, mood and main vocal characteristics of this song."
```

## Acknowledgments

GaMMA is built upon [LLaVA-NeXT](https://github.com/LLaVA-VL/LLaVA-NeXT), [Qwen](https://qwen.ai/home) and [vLLM](https://github.com/vllm-project/vllm). We express our gratitude to the authors for their remarkable work.

## Citation

```bibtex
@article{gamma2026you,
  title={GaMMA: Towards Joint Global-Temporal Music Understanding in Large Multimodal Models},
  author={You, Zuyao and Yu, Zhesong and Liu, Mingyu and Zhu, Bilei and Wan, Yuan and Wu, Zuxuan},
  journal={arXiv},
  year={2026}
}
```

