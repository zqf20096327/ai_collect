# PreMoE: Proactive Inference for Efficient Mixture-of-Experts

[arXiv](https://arxiv.org/abs/2505.17639)
[License](LICENSE)

Official implementation of **PreMoE: Proactive Inference for Efficient Mixture-of-Experts**.

## News

- **[2026-07]** 🎉 PreMoE has been accepted to **COLM 2026**!

## Overview

PreMoE is a **training-free** framework that proactively compiles sparse MoE variants for targeted deployment scenarios. At its core is **Predicted Expert Utility (PEU)**, a robust metric for estimating expert importance from router logits through high-confidence threshold filtering and logit transformation. Using PEU scores computed on a small calibration set, PreMoE produces domain-aware expert rankings that can be used to compile either **domain-specific specialists** or **high-efficiency multi-domain generalists** -- without any retraining.

Across MoE models ranging from 30B to 718B parameters, PreMoE achieves up to **50% sparsity** with nearly no performance loss.

## Supported Models


| Model               | Parameters | Routed Experts | Active Experts | Framework                        |
| ------------------- | ---------- | -------------- | -------------- | -------------------------------- |
| DeepSeek-R1         | 671B       | 256            | 8              | vLLM 0.13.0 (GPU / Ascend NPU)  |
| openPangu-Ultra-MoE | 718B       | 256            | 8              | vLLM 0.13.0 (GPU / Ascend NPU)  |
| Qwen3-30B-A3B       | 30B        | 128            | 8              | vLLM 0.13.0 (GPU / Ascend NPU)  |


## Pipeline

PreMoE operates through three stages:

```
                         ┌─────────────────┐
                         │  Stage 1: Normal │
                         │   Full-model     │
                         │   inference      │
                         └────────┬─────────┘
                                  │  model outputs
                                  ▼
                         ┌─────────────────┐
                         │ Stage 2: Analyze │
                         │  Collect router  │
                         │  logits → PEU    │
                         │  → expert ranking│
                         └────────┬─────────┘
                                  │  expert_ranking.pth
                                  ▼
                         ┌─────────────────┐
                         │Stage 3: Retrieve │
                         │  Pruned-expert   │
                         │  inference       │
                         └─────────────────┘
```

### Stage 1: Normal Inference

Run the original model to generate outputs on the calibration dataset.

```bash
export STAGE=normal
# Launch vLLM server and run inference as usual
```

### Stage 2: Analyze (Logit Collection + PEU Scoring)

Concatenate each prompt with its Stage-1 output and run a single prefill pass with `max_tokens=1`. Router logits are automatically captured and saved to disk.

```bash
export STAGE=analyze
export PTH_SAVE_PATH="/path/to/save/logits"

# Run inference (eager mode, sequential, max_tokens=1)
# After collection, merge and analyze:
python -m premoe.merge_logits \
    --logits-dir "${PTH_SAVE_PATH}" \
    --output record_all_logits.pth

python -m premoe.analyze \
    --input record_all_logits.pth \
    --output expert_ranking.pth \
    --topk 8 \
    --num-experts 256   # 128 for Qwen3-30B
```

### Stage 3: Retrieve (Pruned Inference)

Load the expert ranking and run inference with only the top-M experts per layer.

```bash
export STAGE=retrieve
export RESERVE_EXPERTS_NUM=128          # experts to keep per layer
export LOAD_EXPERTS_PATH="expert_ranking.pth"

# Launch vLLM server -- same configuration as Stage 1
```

## Installation

### Prerequisites

- Python >= 3.10
- [vLLM](https://github.com/vllm-project/vllm) == 0.13.0
- PyTorch >= 2.0
- For Ascend NPU: [vllm-ascend](https://github.com/vllm-project/vllm-ascend)
- For CUDA GPU: standard vLLM CUDA installation

### Setup

```bash
git clone https://github.com/JarvisPei/PreMoE.git
cd PreMoE

pip install -r requirements.txt
```

### Apply vLLM Patches

PreMoE supports both **CUDA GPU** and **Ascend NPU** deployments.
See [`vllm_patches/README.md`](vllm_patches/README.md) for detailed instructions.

#### Option A: Ascend NPU

```bash
# vllm-ascend patches (worker + expert selector)
cp vllm_patches/vllm_ascend/worker/worker_v1.py \
   $(python -c "import vllm_ascend; print(vllm_ascend.__path__[0])")/worker/worker_v1.py
cp vllm_patches/vllm_ascend/ops/fused_moe/experts_selector.py \
   $(python -c "import vllm_ascend; print(vllm_ascend.__path__[0])")/ops/fused_moe/experts_selector.py

# vLLM model patches (choose the model you need)
cp vllm_patches/vllm/model_executor/models/deepseek_v2.py \
   $(python -c "import vllm; print(vllm.__path__[0])")/model_executor/models/deepseek_v2.py
cp vllm_patches/vllm/model_executor/models/qwen3_moe.py \
   $(python -c "import vllm; print(vllm.__path__[0])")/model_executor/models/qwen3_moe.py
```

#### Option B: CUDA GPU

```bash
# vLLM model patches (same files, hardware-agnostic)
cp vllm_patches/vllm/model_executor/models/deepseek_v2.py \
   $(python -c "import vllm; print(vllm.__path__[0])")/model_executor/models/deepseek_v2.py
cp vllm_patches/vllm/model_executor/models/qwen3_moe.py \
   $(python -c "import vllm; print(vllm.__path__[0])")/model_executor/models/qwen3_moe.py
```

Then add the PreMoE stage hook to the GPU worker. In
`vllm/v1/worker/gpu_worker.py`, add the following **after**
`self.model_runner.profile_run()` inside `determine_available_memory()`:

```python
from premoe.worker_hooks import premoe_init_stage
premoe_init_stage(self.model_runner.model)
```

For models with grouped top-k routing (e.g. DeepSeek-R1), see the
GPU expert selector instructions in [`vllm_patches/README.md`](vllm_patches/README.md).

## Environment Variables


| Variable              | Stage    | Description                                        |
| --------------------- | -------- | -------------------------------------------------- |
| `STAGE`               | all      | Pipeline stage: `normal`, `analyze`, or `retrieve` |
| `PTH_SAVE_PATH`       | analyze  | Directory for saving collected router logits       |
| `LOAD_EXPERTS_PATH`   | retrieve | Path to the expert ranking `.pth` file             |
| `RESERVE_EXPERTS_NUM` | retrieve | Number of experts to keep per layer                |


## Repository Structure

```
PreMoE/
├── README.md                           # This file
├── LICENSE                             # MIT License
├── requirements.txt                    # Python dependencies
├── premoe/                             # Core PreMoE analysis tools
│   ├── __init__.py
│   ├── analyze.py                      # PEU scoring (CLI)
│   ├── merge_logits.py                 # Merge per-rank/layer logits
│   ├── worker_hooks.py                 # Hardware-agnostic worker hooks
│   └── gpu_expert_selector.py          # GPU-compatible expert selector
├── vllm_patches/                       # Modified vLLM source files
│   ├── README.md                       # Patch application guide
│   ├── vllm/
│   │   └── model_executor/models/
│   │       ├── deepseek_v2.py          # DeepSeek-R1/V3 model
│   │       └── qwen3_moe.py           # Qwen3-30B-A3B model
│   └── vllm_ascend/
│       ├── worker/worker_v1.py         # NPU worker with PreMoE hooks
│       └── ops/fused_moe/
│           └── experts_selector.py     # Expert selection with pruning
├── data/
│   └── calibration/                    # Calibration datasets
│       ├── nv_math_800.jsonl
│       ├── nv_stem_200_random.jsonl
│       ├── am_code_600_python.jsonl
│       └── chat_lmsys_600_random.jsonl
└── scripts/                            # Example pipeline scripts
    ├── run_normal.sh
    ├── run_analyze.sh
    └── run_retrieve.sh
```

## Calibration Data

The `data/calibration/` directory contains sample calibration datasets:


| File                          | Domain        | Samples | Source    |
| ----------------------------- | ------------- | ------- | --------- |
| `nv_math_800.jsonl`           | Mathematics   | 800     | Nemotron  |
| `nv_stem_200_random.jsonl`    | STEM          | 200     | Nemotron  |
| `am_code_600_python.jsonl`    | Code (Python) | 600     | OpenCoder |
| `chat_lmsys_600_random.jsonl` | General chat  | 600     | LMSYS     |


As few as **5--10 calibration samples** are sufficient for effective PEU computation.

## Citation

If you find PreMoE useful in your research, please cite our paper:

```bibtex
@article{pei2026premoe,
  title={PreMoE: Proactive Inference for Efficient Mixture-of-Experts},
  author={Pei, Zehua and Zhang, Ying and Zhen, Hui-Ling and Yuan, Tao and Yu, Xianzhi and Dong, Zhenhua and Pan, Sinno Jialin and Yuan, Mingxuan and Yu, Bei},
  journal={arXiv preprint arXiv:2505.17639},
  year={2026}
}
```

## License

This project is licensed under the MIT License -- see the [LICENSE](LICENSE) file for details.
