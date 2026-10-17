# AnalogAgent: Self-Improving Analog Circuit Design Automation with LLM Agents

[![arXiv](https://img.shields.io/badge/arXiv-2603.23910-b31b1b.svg)](https://arxiv.org/abs/2603.23910)

This repository contains the implementation of AnalogAgent, an agentic framework for automated analog circuit design.

> 🎉 **Accepted at KDD 2026 (AI4Science Track), selected for Oral presentation.**
>
> 📄 Paper: [AnalogAgent: Self-Improving Analog Circuit Design Automation with LLM Agents](https://arxiv.org/abs/2603.23910)


## Overview
AnalogAgent integrates:
- Multi-Agent Systems for execution-driven refinement
- Self-Evolving Memory for cross-task knowledge reuse
- Adaptive Design Playbook for structured generation guidance

## 🚀 Reproducibility & Artifacts

To support the verification of our methodology and results, we have released the **AnalogAgent-Artifact** repository. This includes the multi-agent system(MAS), the Self-Evolving Memory (SEM), and the complete evaluation suite.

### 📦 Repository Structure
The current repository contains the following key components for the refinement loop:

- **`main_run.py`**: The central entry script that orchestrates the **end-to-end refinement loop** (Generate → Execute/Check → Optimize → Curate Rules).
- **`agents.py`**: Defines multi-agent roles, including the *Code Generator* and *Design Optimizer*.
- **`curator.py` + `playbook.py` + `playbook.json`**: Implements the **Self-Evolving Memory (SEM)**. Handles rule filtering, conflict checking, deduplication, and persistent storage of design heuristics.
- **`problem_set.tsv`**: Benchmark task metadata containing standardized analog circuit design specifications.

### 🛠️ Execution Environment

All experiments were conducted and verified under the following settings to ensure consistency and performance:

* **Operating System**: Ubuntu 20.04.6 LTS
* **Python Version**: 3.10 (A dedicated **Conda environment** is highly recommended)
* **Circuit Simulators**: 
    * **ngspice**: Must be installed and accessible in your `$PATH`.
    * **PySpice**: Required for Python-SPICE interfacing.
* **ML Runtime Stack**: 
    * **Local Inference**: Supports vLLM-based serving (optimized for NVIDIA RTX A6000 / CUDA 12.4).
    * **Cloud Inference**: Supports Gemini, GPT, and Qwen API integrations.
* **Hardware**: Experiments were executed on a dual-GPU workstation with **NVIDIA RTX A6000** (Driver 550.54).

### 💻 Quick Start: How to Reproduce
You can verify the AnalogAgent methodology by running the following command to initiate an automated design task:

```bash
# 1. Clone the repository
git clone https://github.com/TheWind-upBird/Analogagent.git
cd Analogagent

# 2. Install dependencies (Requires Python 3.10)
pip install openai google-generativeai PySpice optuna pandas python-dotenv matplotlib numpy
# Also requires ngspice installed and available in your $PATH (see Execution Environment).

# 3. Run the end-to-end refinement loop (Example: Task ID 1)
python main_run.py \
  --model gpt-5 \
  --api_key YOUR_API_KEY \
  --task_id 1 \
  --num_per_task 1 \
  --num_of_retry 1
```
## Status
> **Note:** This is a **minimum viable product (MVP)** . A more comprehensive and detailed version of the code  will be uploaded subsequently.
