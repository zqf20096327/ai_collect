<p align="center">
    <br>
    <img src="asset/banner.png" width="50%"/>
    <br>
    <h1>OneDayAgent: Towards a Long-Horizon Harness for Autonomous Agents</h1>
<p>

<p align="center">
  <a href="https://arxiv.org/abs/2608.05013"><img src="https://img.shields.io/badge/Paper-arXiv-000000?style=for-the-badge&logo=arxiv&logoColor=white" alt="Paper" /></a>
  <a href="https://huggingface.co/papers/2608.05013"><img src="https://img.shields.io/badge/🤗%20Paper-HF-FFD21E?style=for-the-badge&logoColor=black" alt="HuggingFace Paper" /></a>
  <a href="https://huggingface.co/datasets/zjunlp/onedayagent_traj"><img src="https://img.shields.io/badge/🤗%20Data-TRAJ-FF9D00?style=for-the-badge&logoColor=black" alt="Trajectory Dataset" /></a>
  <a href="https://x.com/zxlzr/status/2085193376304107574"><img src="https://img.shields.io/badge/𝕏-Follow-000000?style=for-the-badge&logoColor=white" alt="Follow on X" /></a>
  <a href="https://xhslink.cn/o/7H0C8AVSsYE"><img src="https://img.shields.io/badge/小红书-Follow-FF2442?style=for-the-badge&logoColor=white" alt="小红书" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-3DA639?style=for-the-badge" alt="License MIT" /></a>
</p>

**OneDayAgent** is a long-horizon agent harness that turns open-ended everyday requests into a managed execution process. Unlike rigid workflow-based agents, it decomposes multi-hour tasks into bounded subtasks, verifies deliverables against the original goal, and compresses execution state into reusable memory — producing reliable outputs even under sustained context pressure.

🏆 **OneDayAgent** was evaluated on the AgentIF-OneDay benchmark (104 tasks) across 5 backend LLMs from 3 model families, achieving state-of-the-art performance with an overall score of **0.821**. See [Main Results](#main-results) for details.

<p align="center">
  <img src="asset/intro.png" width="100%"/>
</p>

<p align="center">
  <em style="font-size: 0.85em; color: #6b7280;">
    Long-horizon everyday tasks. <b>(a)</b> Everyday requests are long-horizon, cross-environment, and multimodal — causing goal drift, context accumulation, and state transfer failures. OneDayAgent addresses them through task decomposition, verification & repair, and execution memory. <b>(b)</b> OneDayAgent achieves state-of-the-art performance on AgentIF-OneDay with an overall score of 0.821.
  </em>
</p>

## 🔔 News

- <strong>[2026-08-15]</strong> We open-source the code for OneDayAgent. Thanks to all contributors for their great efforts!

- <strong>[2026-08-04]</strong> We release our paper [OneDayAgent: Towards a Long-Horizon Harness for Autonomous Agents](https://arxiv.org/abs/2608.05013).

- <strong>[2026-07-21]</strong> Uploaded the trajectory dataset to 🤗Hugging Face: <a href="https://huggingface.co/datasets/zjunlp/onedayagent_traj" target="_blank">zjunlp/onedayagent_traj</a>.

## Table of Contents

- 🌟 [Overview](#overview)
- 📈 [Main Results](#main-results)
- 🔧 [Environment Setup](#environment-setup)
- ⏩ [Running](#running)
- 🌻 [Acknowledgement](#acknowledgement)
- 🚩 [Citation](#citation)
- 🤝 [Contributors](#contributors)

## Overview

Everyday requests — such as *"research a topic, build a deck, and deliver a report"* — are long-horizon, cross-environment, and multimodal. As tasks stretch from minutes to hours, agents face sustained context pressure: goals drift from accumulated constraints, intermediate state fails to transfer across environments, and observations pile up until the context window overflows. Existing approaches fix individual failure modes, but these failures interact and compound over long trajectories.

**OneDayAgent** addresses these challenges through three core capabilities:

1. **Task Decomposition** — breaks an overloaded request into bounded subtasks, each with a shorter local objective while preserving the global intent. This reduces per-step context load and enables focused, verifiable progress.

2. **Global Verification & Repair** — after subtask execution, an LLM-based verifier checks whether the deliverable satisfies the original request. If defects are found, a targeted repair loop patches them — re-aligning the final output with the user's actual goal.

3. **Execution Memory** — compresses high-volume tool observations (e.g., web pages, search results, code output) into reusable evidence through immediate summarization. Subtask state is checkpointed so that context compression never loses critical information needed by later steps.

<p align="center">
  <img src="asset/method.png" width="100%"/>
</p>

<p align="center">
  <em style="font-size: 0.85em; color: #6b7280;">
    OneDayAgent uses a long-horizon harness that decomposes an everyday task, executes subtasks through environment-grounded tools, maintains execution memory, and performs global verification and repair before producingthe final deliverable.
  </em>
</p>

OneDayAgent runs on any OpenAI-compatible LLM backend. The same harness — without prompt engineering or architecture changes — achieves stable performance across 5 models from 3 families (GLM, Gemini, DeepSeek), demonstrating that the harness, not the model, drives long-horizon reliability.

## Main Results

Main benchmark results (AgentIF-OneDay, all variants).

<p align="center">
  <img src="asset/main_results.png" width="100%"/>
</p>

<p align="center">
  <em style="font-size: 0.85em; color: #6b7280;">
    We compare OneDayAgent with general-purpose agents across task types, domains, rubric dimensions, input-attachment settings, latency, and overall score [0, 1]. OWE, LII, and IR denote Open Workflow Execution, Latent Instruction Inference, and Iterative Refinement, while Inst., Fact., and Logic denote Instruction Following, Factuality, and Logic/Functionality. The w/ and w/o columns report scores with and without input attachments. † marks official AgentIF-OneDay results evaluated with Gemini-3-Pro-Preview as the LLM-as-judge and validated against human annotations. With the GLM-5.2 backend, OneDayAgent achieves the strongest overall score of 0.821 and leads all score dimensions.
  </em>
</p>

## Environment Setup

> [!IMPORTANT]
> We strongly recommend using the pre-built [Docker](https://docs.docker.com/engine/install/) image. Manual environment setup is error-prone due to the large number of system dependencies (Playwright, LibreOffice, ffmpeg, etc.).

### Option A: Pull Pre-Built Image (Recommended)

<a href="https://hub.docker.com/repository/docker/johnsonzheng03/onedayagent/general"><img src="https://img.shields.io/badge/onedayagent-dev-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="onedayagent on Docker Hub" /></a>

```bash
docker pull johnsonzheng03/onedayagent:dev
docker tag johnsonzheng03/onedayagent:dev onedayagent:dev
```

### Option B: Build From Source

If you need to modify the image (e.g., customize `entrypoint.sh`):

<a href="https://hub.docker.com/repository/docker/johnsonzheng03/onedayagent-base/general"><img src="https://img.shields.io/badge/onedayagent--base-clean-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="onedayagent-base on Docker Hub" /></a>

```bash
docker pull johnsonzheng03/onedayagent-base:clean
docker tag johnsonzheng03/onedayagent-base:clean onedayagent-base:clean
docker build -t onedayagent:dev .
```

### Option C: Local Environment (Not Recommended)

If [Docker](https://docs.docker.com/engine/install/) is unavailable, install dependencies manually. The full requirements are in [`requirements.txt`](requirements.txt) — see the file header for platform-specific system packages and install order.

```bash
# 1. Install system packages (Ubuntu/Debian example — see requirements.txt for other platforms)
apt-get update && apt-get install -y \
    poppler-utils libreoffice-core-nogui libreoffice-impress libreoffice-calc \
    ffmpeg git

# 2. Install Python packages (follow the 4-part order in requirements.txt)
pip install -r requirements.txt

# 3. Install Playwright browser
python -m playwright install --with-deps chromium

# 4. Install OneDayAgent
pip install -e . --no-deps
```

### Configuration

Copy `.env.example` to `.env` and fill in your API keys:

```bash
cp .env.example .env
# Edit .env with your BASE_URL, API_KEY, MODEL, and tool keys (SERPER_AK, JINA_AK, etc.)
```

Key configuration groups (see [`.env.example`](.env.example) for full details):

| Section | Variables | Purpose |
|---|---|---|
| Main Model | `BASE_URL`, `API_KEY`, `MODEL` | Primary reasoning model (OpenAI-compatible) |
| VLM | `VLM_URL`, `VLM_AK`, `VLM_MODEL` | Image analysis (defaults to Main) |
| Summary | `SUMMARY_URL`, `SUMMARY_AK`, `SUMMARY_MODEL` | Context compression (defaults to Main) |
| Image Gen | `IMAGE_GEN_URL`, `IMAGE_GEN_MODEL`, `IMAGE_GEN_AK` | Image generation tool |
| Tools | `SERPER_AK`, `JINA_AK` | Web search and visit |
| Judge & Eval | `EVALUATE_URL`, `EVALUATE_AK`, `EVALUATE_MODEL` | LLM-as-judge scoring and benchmark evaluation (any OpenAI-compatible backend) |

## Running

### Quick Start

```bash
# Run all 104 tasks (uses .env DR_DATASET_FILE_PATH)
bash run.sh

# Run a specific dataset subset
bash run.sh --dataset questions_10.txt
```

### Dataset Selection

Datasets are located in `tasks/agentif_oneday/datasets/`. A `.txt` file contains question IDs (one per line), which are matched against the full JSONL (`questions_all.jsonl`) to select tasks. Pass the filename via `--dataset`:

```bash
bash run.sh --dataset questions_80.txt    # run 80 tasks
bash run.sh --dataset questions_all.txt    # run all 104 tasks (default)
```

### Experiment ID

Each run creates an output directory named `<MODEL>_<timestamp>`. Use `--exp` to set a custom ID:

```bash
bash run.sh --exp my_experiment
```

### Resume

If a run is interrupted, resume it by passing the same experiment ID. The agent will skip completed tasks and re-run only the missing ones:

```bash
bash run.sh --exp 20260814_135234
```

Tasks are considered completed if they have both a rollout record and a valid score in `rollout1.jsonl`. Tasks with `percentage=0` (failed evaluation) are also skipped; to re-evaluate them, delete their records from `rollout1.jsonl` before resuming, or set `DR_FORCE_REEVAL=true` in `.env`.

### Output Structure

All outputs are written to `./runs/` (mapped to `/data` inside Docker):

```
runs/
├── output/<model>_<exp_id>/          # Experiment output
│   ├── rollout1.jsonl                # Full trajectory + judge scores (one line per task)
│   ├── sft_data1.jsonl               # SFT training data (full trajectory)
│   ├── sft_data2.jsonl               # SFT training data (split by stage)
│   ├── sft_stats1.json               # SFT conversion statistics
│   └── token_usage.json              # Token usage summary
├── result_attachments/<model>_<exp_id>/  # Agent-generated files
│   ├── auto_score_<timestamp>.jsonl  # Judge criteria-level results
│   ├── auto_score_<timestamp>.txt    # Judge summary
│   ├── env_snapshot.txt              # Sanitized env config snapshot
│   ├── run_<timestamp>.log           # Run log
│   ├── taskif_<id>_<ts>/             # Per-task output files
│   └── trajectory_stats/             # SFT statistics charts
├── judge_results/                    # Judge output files
├── judge_logs/                       # Judge LLM logs
├── logs/
│   ├── run_<timestamp>.log           # Python FileHandler log
│   └── console_<timestamp>.log       # Full stdout/stderr capture
├── camel_working_dir/                # Camel toolkit temp files
└── token_usage/                      # Token usage tracking
```

## Acknowledgement

This work was completed during the authors' time at [Ant Group](https://www.antgroup.com/). We thank [xBench](https://xbench.org/) for providing the AgentIF-OneDay benchmark.

## Citation

Please cite our paper if you find OneDayAgent is useful in your work. Thanks!

```bibtex
@misc{zheng2026onedayagentlonghorizonharnessautonomous,
      title={OneDayAgent: Towards a Long-Horizon Harness for Autonomous Agents}, 
      author={Jingsheng Zheng and Xinyuan Fang and Jintian Zhang and Zhengke Gui and Huajun Chen and Ningyu Zhang},
      year={2026},
      eprint={2608.05013},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2608.05013}, 
}
```

## Contributors

<a href="https://github.com/zjunlp/OneDayAgent/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=zjunlp/OneDayAgent" /></a>

We will offer long-term maintenance to fix bug for the project. Welcome for issues and PRs!
