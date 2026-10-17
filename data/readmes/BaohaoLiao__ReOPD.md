<div align="center">

## Multi-Turn On-Policy Distillation with Prefix Replay

ReOPD distills a teacher agent into a student **without environment interaction during student training**: the student acts on prefixes replayed from pre-collected teacher trajectories, while the teacher supplies dense per-step supervision. It matches or improves online OPD accuracy with **zero tool calls** and **4–9× faster rollouts**.

<p align="center">
  <a href="https://arxiv.org/abs/2607.04763"><img src="https://img.shields.io/badge/arXiv-2607.04763-b31b1b?style=flat&labelColor=555" alt="arXiv"></a>
  <a href="https://baohaoliao.github.io/ReOPD/"><img src="https://img.shields.io/badge/🌐 Project-Page-blue?style=flat&labelColor=555" alt="Project Page"></a>
  <a href="https://github.com/BaohaoLiao/ReOPD"><img src="https://img.shields.io/badge/github-ReOPD-181717?style=flat&labelColor=555&logo=github&logoColor=white" alt="GitHub"></a>
  <a href="https://huggingface.co/collections/baohao/reopd"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Collection-blue" alt="Hugging Face collection"></a>
</p>

</div>

## 🔥 News

- **[07/2026]** ReOPD reproduction code is released!

## 🌟 Overview

<div align="center">
<img alt="OPD vs ReOPD" src="assets/reopd_overview.png" width="800">
</div>

Fully online OPD (top) re-rolls the student through a live environment every update and queries the teacher at each visited history. ReOPD (bottom) replays a **teacher-forced prefix** from an offline pool — collected for free during the teacher's RL — and lets the student act only at the supervised step. Multi-turn OPD suffers a **two-sided distribution shift** (student occupancy vs. teacher reliability), so ReOPD samples positions with `p_t ∝ κ^t` (κ = 0.6) at data-processing time, favoring early, low-shift prefixes and leaving the loss unchanged.

<div align="center">
<img alt="Accuracy, rollout time, and tool calls" src="assets/accuracy_time_toolcall.png" width="800">
<img alt="Multi-environment distillation" src="assets/multi_env.png" width="800">
</div>

The offline pool also decouples environments from training: trajectories from heterogeneous environments are collected separately by domain-specific teachers and merged into one pool, so a single student is distilled jointly without keeping all environments online.

## 📂 Repository Layout

```text
ReOPD/
  data/          # Prefix-pool construction, prompt mixing
  train/         # Training code (src/) + env-var reference (README.md)
  eval/          # math/ (AIME24/25, AMC23, Minerva, Olympiad, MATH500), search/ (7 QA sets)
  scripts/
    models/      # Megatron model-arg configs
    train/       # convert, cold start, GRPO, distillation
    eval/        # math.sh, search.sh
  tools/         # HF <-> Megatron torch_dist converters
  docs/          # search.md, multi_env.md
  third_party/slime   # Training framework (submodule)
```

This README covers **math** (ReTool). See [`docs/search.md`](docs/search.md) and [`docs/multi_env.md`](docs/multi_env.md) for the other environments.

## 📦 Installation

Set up the base environment following slime's [quick-start guide](https://github.com/THUDM/slime/blob/main/docs/en/get_started/quick_start.md) (PyTorch/CUDA, Ray, SGLang, Megatron-LM, Docker image), then:

```bash
git clone https://github.com/BaohaoLiao/ReOPD.git && cd ReOPD
git submodule update --init --recursive
pip install -r requirements.txt
pip install -e third_party/slime --no-deps
```

- **A100 (SM80):** slime's default images target H100/H800. Use the A100 patch set in [THUDM/slime#1832](https://github.com/THUDM/slime/pull/1832).
- **Megatron elsewhere than `/root/Megatron-LM`:** `export MEGATRON_ROOT=/path/to/Megatron-LM`.
- **Math (ReTool):** no extra install — the Python sandbox deps are in `requirements.txt`.
- **Search (Search-R1):** extra deps + a retriever conda env — see [`docs/search.md`](docs/search.md#-installation).

## 🚀 Quickstart

**Evaluate a released model:**

```bash
hf download baohao/ReOPD_Math_Qwen3-8B_SFT-RL_to_Math_Qwen3-4B-Instruct-2507_SFT --local-dir /ckpt/model
DP_SIZE=8 bash scripts/eval/math.sh /ckpt/model
```

**Run one ReOPD distillation** from released artifacts, skipping stages 1, 2 and 3a (8 GPUs: teacher 4–7, student 0–3):

```bash
hf download baohao/Math_Qwen3-4B-Instruct-2507_SFT --local-dir /ckpt/student_hf
hf download baohao/Math_Qwen3-8B_SFT-RL           --local-dir /ckpt/teacher_hf
hf download baohao/Math_Qwen3-8B_SFT-RL_Prefix --repo-type dataset --local-dir /data/pool

# slime trains from torch_dist; the teacher is served by SGLang and stays HF
HF_CHECKPOINT=/ckpt/student_hf SAVE=/ckpt/student_torch_dist \
    bash scripts/train/convert_hf_to_torch_dist.sh

TEACHER=qwen3-8b STUDENT=qwen3-4b \
TEACHER_MODEL_PATH=/ckpt/teacher_hf \
HF_CHECKPOINT=/ckpt/student_hf \
REF_LOAD=/ckpt/student_torch_dist \
PROMPT_DATA=/data/pool/train.jsonl \
SAVE_DIR=/runs/reopd_8b_to_4b \
    bash scripts/train/reopd_math.sh

RUN_DIR=/runs/reopd_8b_to_4b ORIGIN_HF_DIR=/ckpt/student_hf \
    bash scripts/eval/math.sh iter_0000199
```

> Any released checkpoint used as a **student** needs that one-time torch_dist conversion for `REF_LOAD` (add `MODEL_CONFIG=scripts/models/<model>.sh` for 8B/30B). Teachers stay in HF format.

## ⚡ Training

Four stages per environment. Every script validates its inputs on startup and names what's missing.

| Stage | Script | Purpose |
| --- | --- | --- |
| 1 | `cold_start.sh` | SFT the base model on tool-use traces |
| 2 | `teacher_grpo_math.sh` | RL the teacher; its rollouts become the prefix pool for free |
| **3** | **`reopd_math.sh`** | **ReOPD (ours)** — replay prefixes, one turn, zero tool calls |
| 4 | `opd_math.sh` | OPD baseline — student rolls out live, queries the teacher every step |

> **Start from any stage.** All `_SFT` (cold start) and `_SFT-RL` (teacher) checkpoints are released — see [Trained Models](#-trained-models) and the [Quickstart](#-quickstart) conversion note.

### 1. Cold start (SFT)

Download a base model and convert it to torch_dist (written to `<hf_dir>/torch_dist`):

```bash
hf download Qwen/Qwen3-4B-Instruct-2507 --local-dir /path/to/Qwen3-4B-Instruct-2507
# also available: Qwen/Qwen3-8B-Base , Qwen/Qwen3-30B-A3B-Instruct-2507

QWEN3_4B_HF=/path/to/Qwen3-4B-Instruct-2507 \
    bash scripts/train/convert_all_to_torch_dist.sh
```

Set `QWEN3_8B_HF` and/or `QWEN3_30B_HF` in the same call to convert those too. Then SFT:

```bash
hf download baohao/math-cold-start --repo-type dataset --local-dir /path/to/data

MODEL=qwen3-4b \
HF_CHECKPOINT=/path/to/Qwen3-4B-Instruct-2507 \
REF_LOAD=/path/to/Qwen3-4B-Instruct-2507/torch_dist \
PROMPT_DATA=/path/to/data/train.parquet \
SAVE_DIR=/path/to/output \
    bash scripts/train/cold_start.sh
```

`MODEL` sets config, parallelism and optimizer offload; 3 epochs, LR 5e-5 cosine:

| `MODEL` | Config | TP | EP | Offload |
| --- | --- | --- | --- | --- |
| `qwen3-4b` (default) | qwen3-4B-Instruct-2507.sh | 2 | 1 | off |
| `qwen3-8b` | qwen3-8B.sh (Qwen3-8B-Base) | 2 | 1 | off |
| `qwen3-30b` | qwen3-30B-A3B-Instruct-2507.sh | 4 | 8 | on |

> **Qwen3-8B-Base** ships without a chat template. `convert_all_to_torch_dist.sh` copies `tokenizer_config.json` from Qwen3-4B-Instruct-2507 whenever both `QWEN3_8B_HF` and `QWEN3_4B_HF` are set, keeping everything in non-thinking mode (`COPY_NONTHINKING_TOKENIZER=0` disables).

### 2. Teacher GRPO

slime saves cold start as a *training* checkpoint (optimizer state included), so re-materialize clean weights first — torch_dist → HF → torch_dist:

```bash
COLD_START_RUN=/path/to/output          # SAVE_DIR from stage 1
ITER=$(cat $COLD_START_RUN/latest_checkpointed_iteration.txt)

INPUT_DIR=$COLD_START_RUN/iter_$(printf '%07d' $ITER) \
OUTPUT_DIR=/path/to/sft_hf \
ORIGIN_HF_DIR=/path/to/Qwen3-4B-Instruct-2507 \
    bash scripts/train/convert_torch_dist_to_hf.sh

HF_CHECKPOINT=/path/to/sft_hf SAVE=/path/to/sft_torch_dist \
    bash scripts/train/convert_hf_to_torch_dist.sh
```

Then RL the teacher:

```bash
hf download baohao/math-train --repo-type dataset --local-dir /path/to/rl_data

MODEL=qwen3-4b \
HF_CHECKPOINT=/path/to/sft_hf \
REF_LOAD=/path/to/sft_torch_dist \
PROMPT_DATA=/path/to/rl_data/train.jsonl \
SAVE_DIR=/path/to/teacher_run \
    bash scripts/train/teacher_grpo_math.sh
```

`MODEL` also sets the RL rollout-engine and memory settings. Rollouts land in `SAVE_DIR/rollout_debug/` — that **is** the prefix pool for stage 3. No in-training eval; measure with `scripts/eval/math.sh`.

### 3. ReOPD (ours)

**a. Build the prefix pool** (`ω(t; κ) = κ^t`, κ = 0.6):

```bash
python data/build_prefix_pool_math.py \
    --rollout-dir /path/to/teacher_run/rollout_debug \
    --prompt-data /path/to/rl_data/train.jsonl \
    --output /path/to/math_prefix_pool.jsonl
```

Filtering rules and flags: [`data/README.md`](data/README.md).

> **Or download it.** One pool per teacher:
>
> | Teacher | Pool | Rows |
> | --- | --- | --- |
> | Qwen3-4B-Instruct-2507 | [`Math_Qwen3-4B-Instruct-2507_SFT-RL_Prefix`](https://huggingface.co/datasets/baohao/Math_Qwen3-4B-Instruct-2507_SFT-RL_Prefix) | 81,936 |
> | Qwen3-8B | [`Math_Qwen3-8B_SFT-RL_Prefix`](https://huggingface.co/datasets/baohao/Math_Qwen3-8B_SFT-RL_Prefix) | 53,762 |
> | Qwen3-30B-A3B-Instruct-2507 | [`Math_Qwen3-30B-A3B-Instruct-2507_SFT-RL_Prefix`](https://huggingface.co/datasets/baohao/Math_Qwen3-30B-A3B-Instruct-2507_SFT-RL_Prefix) | 54,706 |

**b. Distill:**

```bash
TEACHER=qwen3-30b STUDENT=qwen3-4b \
TEACHER_MODEL_PATH=/path/to/teacher_sft_rl_hf \
HF_CHECKPOINT=/path/to/student_sft_hf \
REF_LOAD=/path/to/student_sft_torch_dist \
PROMPT_DATA=/path/to/math_prefix_pool.jsonl \
SAVE_DIR=/path/to/student_run \
    bash scripts/train/reopd_math.sh
```

Same presets as stage 4; what differs:

| | ReOPD (3) | OPD (4) |
| --- | --- | --- |
| Student turns / sample | **1** | up to 16 |
| Tool calls | **0** | up to 16 |
| Response / context cap | 4096 / 8192 | 8192 / — |
| Teacher serving | mem 0.8, 256 in-flight, 32k KV | mem 0.85, 128 in-flight, uncapped |

One turn and zero tool calls is what makes rollouts 4–9× faster.

### 4. OPD (online baseline)

Same command with `opd_math.sh` and the **RL prompts** instead of the pool:

```bash
TEACHER=qwen3-30b STUDENT=qwen3-4b \
TEACHER_MODEL_PATH=/path/to/teacher_sft_rl_hf \
HF_CHECKPOINT=/path/to/student_sft_hf \
REF_LOAD=/path/to/student_sft_torch_dist \
PROMPT_DATA=/path/to/rl_data/train.jsonl \
SAVE_DIR=/path/to/student_run \
    bash scripts/train/opd_math.sh
```

`TEACHER` and `STUDENT` are independent. The paper's pairs:

| Pair | `TEACHER` | `STUDENT` | Teacher served | Student offload |
| --- | --- | --- | --- | --- |
| 4B → 4B | `qwen3-4b` | `qwen3-4b` | TP1 × DP4 | off |
| 8B → 4B | `qwen3-8b` | `qwen3-4b` | TP1 × DP4 | off |
| 30B → 4B | `qwen3-30b` | `qwen3-4b` | TP2 × DP2 | off |
| 30B → 8B | `qwen3-30b` | `qwen3-8b` | TP2 × DP2 | on |

Teacher on `TEACHER_GPUS` (default 4–7), student on `STUDENT_GPUS` (0–3). Every variable: [`train/README.md`](train/README.md).

## 🎓 Evaluation

```bash
# HF checkpoint:
DP_SIZE=8 bash scripts/eval/math.sh /path/to/hf_model

# torch_dist checkpoints from a run (converted automatically):
RUN_DIR=/path/to/run ORIGIN_HF_DIR=/path/to/base_hf \
    bash scripts/eval/math.sh iter_0000199 iter_0000219
```

One pipeline: convert if needed → serve → evaluate → tear down. Key settings are grouped at the top of the script and env-overridable, e.g. `DATASETS="aime24" NUM_SAMPLES_HARD=16 TP_SIZE=2`. Search eval: [`docs/search.md`](docs/search.md#-evaluation).

## 🤗 Trained Models

All in the [Hugging Face collection](https://huggingface.co/collections/baohao/reopd). Names encode role, environment (`Math` / `Search` / `Both`), and base model. Multi-env runs reuse the single-env teachers — only the student is trained on both.

| Role | Pattern |
| --- | --- |
| Cold start (stage 1) | `<Env>_<Base>_SFT` |
| Teacher (stage 2) | `<Env>_<Base>_SFT-RL` |
| **ReOPD student (ours)** | `ReOPD_<Teacher>_to_<Student>` |
| OPD student (baseline) | `OPD_<Teacher>_to_<Student>` |
| SFT student (off-policy baseline) | `SFT_<Student>_on_<Teacher>_trace` |
| Multi-env cold start | `Both_<Base>_SFT` |
| Multi-env student | `<Method>_Math-Search_<Teacher>_to_Both_<Student>` |
| Prefix pools (stage-3 data) | `<Env>_<Teacher>_SFT-RL_Prefix` |

Example: [`baohao/ReOPD_Math_Qwen3-30B-A3B-Instruct-2507_SFT-RL_to_Math_Qwen3-8B_SFT`](https://huggingface.co/baohao/ReOPD_Math_Qwen3-30B-A3B-Instruct-2507_SFT-RL_to_Math_Qwen3-8B_SFT).

## 📝 Citation

```bibtex
@misc{liao2026reopd,
      title={Multi-Turn On-Policy Distillation with Prefix Replay},
      author={Baohao Liao and Hanze Dong and Christof Monz and Xinxing Xu and Li Dong and Furu Wei},
      year={2026},
      eprint={2607.04763},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2607.04763},
}
```

## 🙏 Acknowledgments

Built on [slime](https://github.com/THUDM/slime) for training and [SGLang](https://github.com/sgl-project/sglang) for rollout and teacher serving. The math and search environments are adapted from [ReTool](https://arxiv.org/abs/2504.11536) and [Search-R1](https://github.com/PeterGriffinJin/Search-R1). We really appreciate their contributions to the community.
