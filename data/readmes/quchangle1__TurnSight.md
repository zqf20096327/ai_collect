<h1 align="center">🛠️👀 TurnSight: Turn-Level Hindsight Self-Distillation for 
<br>Tool-Integrated Reasoning

</h1>

<div align="center"> 

[![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg?logo=arxiv)](https://arxiv.org/pdf/2608.04007)
[![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-yellow?logo=huggingface)](https://huggingface.co/collections/ChangleQu/turnsight)
[![Model](https://img.shields.io/badge/Model-HuggingFace-yellow?logo=huggingface)](https://huggingface.co/collections/ChangleQu/turnsight)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-390/) 
</div>

<h5 align="center"> If you like our project, please give us a star ⭐ on GitHub for the latest update.</h5>

## 📣 Latest News
- **[Aug 5, 2026]**: 📄 Our paper is now available on **[arXiv](https://arxiv.org/pdf/2608.04007)**.
- **[Aug 5, 2026]**: 🔥 We released all our **TurnSight model checkpoints** and **datasets**. Checkout **[🤗 TurnSight](https://huggingface.co/collections/ChangleQu/turnsight)** here.
- **[Aug 5, 2026]**: 🚀 Full codebase of **TurnSight** released.

## 📦 Model Zoo

| Model | Download |
| --- | --- |
| Qwen3-8B-TurnSight | [🤗 HuggingFace](https://huggingface.co/ChangleQu/Qwen3-8B-TurnSight) |
| Qwen3-4B-TurnSight | [🤗 HuggingFace](https://huggingface.co/ChangleQu/Qwen3-4B-TurnSight) |

## 💡 Overview

TurnSight improves multi-turn tool-integrated reasoning with four components:

1. **Multi-turn TIR:** collect complete tool-interaction trajectories and compute turn-level base advantages.
2. **Execution hindsight:** expose the executed tool results to a teacher view and estimate the teacher-student log-probability gap for each turn.
3. **Multi-lookahead teacher selection:** compare teachers with 1-, 2-, and 3-step lookahead contexts and select the direction-consistent, strongest signal.
4. **Group-normalized weighting:** normalize teacher evidence within each group, apply bounded sign-aware modulation, and integrate the result with the base advantage.

![TurnSight framework](images/framework.png)

## 📊 Overall Performance

TurnSight is evaluated on FTRL, BFCL, and ToolHop-style tool-integrated reasoning tasks. The table below reports the current results for Qwen3-4B and Qwen3-8B.

![TurnSight experiments](images/experiment.png)

## 🛠️ Setup

### 💻 Environment

Create a Python 3.10 environment and install the pinned dependencies:

```bash
conda create -n TurnSight python=3.10 -y
conda activate TurnSight
pip install -r requirements.txt
```

The training code expects the repository root to contain the following directories:

```text
TurnSight/
├── Code/                 # VeRL extensions and TurnSight training code
├── Data/                 # train.parquet and test.parquet
├── Scripts/              # training entry points
├── images/               # README figures
└── requirements.txt
```

### 🤖 Base Model

Download a base Qwen3 checkpoint from Hugging Face and set its local path through `MODEL_PATH`. The default value in `Scripts/run.sh` is `./models/Qwen3-8B`.

- [Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B)
- [Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B)

### 📊 Data

The default training script reads:

- `Data/train.parquet` for training
- `Data/test.parquet` for validation

Each example uses the `messages` field as the prompt and is configured for Qwen3-style thinking and multi-turn tool interaction.

## ⚙️ Training Configuration

The main configuration is in [`Scripts/run.sh`](Scripts/run.sh). 
The default experiment uses lookahead depths `[1, 2, 3]`, tool-only teacher context, group normalization, and bounded `tanh` modulation. Make sure a Ray Jobs server is available at `http://localhost:8265` before launching training, or override `RAY_ADDRESS`.

## 🚀 Quick Start

### 🔥 Training

```bash
export MODEL_PATH=/path/to/Qwen3-8B
bash Scripts/run.sh
```

Training checkpoints, rollouts, and validation outputs are written below `outputs/` by default. The script runs validation before training and periodically evaluates according to the configured `trainer.test_freq`.

### 🤖 Model Merge

- Run the command to merge the trained model into SAFETENSORS format.
  ```bash
  python3 Code/merge/merge_model.py merge --local_dir ${dir} --target_dir ${dir}
  ```

### 🚀 Evaluation

We evaluate **TurnSight** on three benchmark datasets to assess its effectiveness and generalization ability across different tool-interaction scenarios.

#### 📊 Benchmark 1: FTRL
  - Run evaluation on FTRL with:
  ```bash
  export MODEL_PATH=/path/to/Qwen3-8B-TurnSight
  bash Scripts/eval_ftrl.sh
  ```

#### 📊 Benchmark 2: BFCL
  - We use the official code provided by BFCL to perform evaluation. You can find the official code in the [BFCL](https://github.com/ShishirPatil/gorilla/blob/main/berkeley-function-call-leaderboard/README.md) repo. 

#### 📊 Benchmark 3: ToolHop
 - Run evaluation on ToolHop with:
  ```bash
  bash Scripts/eval_toolhop.sh
  ```

## 📄 Citation
```bibtex
@article{qu2026turnsight,
    title={TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated Reasoning},
    author={Qu, Changle and Dai, Sunhao and Cai, Hengyi and Zhou, Yuqi and Chen, Xinran and Simon and Xu, Jun},
    journal={arXiv preprint arXiv:2608.04007},
    year={2026}
  }
```

## 👏 Acknowledgement

This project uses the [VeRL](https://github.com/volcengine/verl) framework for distributed reinforcement learning and tool-integrated reasoning.

