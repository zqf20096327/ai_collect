# Luth-2: Pushing the French Capabilities of SLMs with MOPD

![Luth-2 banner](media/luth-2-banner.png)

**Luth-2** is the second iteration of our French post-training work, built on Qwen3.5 with a 3B-token multi-domain SFT mixture, reinforcement learning, and multi-domain on-policy distillation (MOPD). It targets stronger **French reasoning, instruction following, knowledge, code, tool use, and dialogue** and is competitive with much larger models. This repository contains the training, evaluation, and data-processing code used to build and reproduce the Luth-2 models.

- 📄 **Blog**: [Luth-2: Pushing the French Capabilities of SLMs with MOPD](https://huggingface.co/blog/MaxLSB/luth-2)
- 🤗 **Models**: [Luth-2-0.8B](https://huggingface.co/kurakurai/Luth-2-0.8B) · [Luth-2-2B](https://huggingface.co/kurakurai/Luth-2-2B)
- 📊 **Datasets**: [SFT](https://huggingface.co/datasets/kurakurai/Luth-2-Post-Training-SFT) · [RL](https://huggingface.co/datasets/kurakurai/Luth-2-Post-Training-RL)
- 💻 **Code**: [GitHub](https://github.com/kurakurai/Luth-2)
- 🏆 **Leaderboard**: [French LLM Leaderboard](https://huggingface.co/spaces/kurakurai/llm_leaderboard_fr)

![Luth-2 leaderboard](media/luth-2-leaderboard.png)

## Setup

Requires [uv](https://docs.astral.sh/uv/) and a CUDA-capable GPU. Each stage has its own
environment, because their dependencies conflict.

## SFT

Supervised fine-tuning with [TRL](https://github.com/huggingface/trl)'s `SFTTrainer`,
sharded across GPUs with [Accelerate](https://github.com/huggingface/accelerate) +
[DeepSpeed](https://github.com/deepspeedai/DeepSpeed) ZeRO-3.

```bash
# Install the SFT venv
make install
# SFT with the default config on 1 GPU
make train
# SFT with your own config
make train TRAIN_CONFIG=configs/training/custom.yaml
```

Trains [`configs/training/default.yaml`](configs/training/default.yaml) — model, datasets,
LoRA, batch size, sequence length. Add `TRAIN_GPUS=0,1,2,3` to shard across GPUs with
DeepSpeed ZeRO-3.

## RL

Reinforcement learning with [prime-rl](https://github.com/PrimeIntellect-ai/prime-rl)
(vLLM inference + orchestrator + FSDP2 trainer). Rewards come from our own
[verifiers](https://github.com/PrimeIntellect-ai/verifiers) environments in
[`tools/rl/envs/`](tools/rl/envs/).

```bash
# Install prime-rl and the Luth reward environments
make rl-install
# RL with the default config (math)
make rl
# RL with another recipe
make rl RL_CONFIG=configs/rl/code.toml
# RL writing its rollouts and checkpoints somewhere else
make rl RL_OUTPUT=/scratch/luth-rl-math
```

Each run writes to `outputs/rl-<config name>` unless `RL_OUTPUT` says otherwise.

- **`math.toml`** — GRPO, boxed answer checked with math-verify
- **`code.toml`** — GRPO, binary reward from unit tests
- **`if.toml`** — GRPO, French IFEval constraints blended with a judge score
- **`mopd.toml`** — multi-teacher on-policy distillation of the three specialists

```bash
# if.toml needs the judge
make rl-judge RL_JUDGE_GPUS=0
make rl RL_CONFIG=configs/rl/if.toml RL_GPUS=1,2,3,4 RL_INFER_GPUS=2 RL_TRAIN_GPUS=2
make rl-judge-stop

# mopd.toml needs the three teachers
make rl-teachers RL_TEACHER_GPUS=5,6,7
make rl RL_CONFIG=configs/rl/mopd.toml RL_GPUS=0,1,2,3,4 RL_INFER_GPUS=3 RL_TRAIN_GPUS=2
make rl-teachers-stop
```

## Eval

French benchmarks with our fork of
[lm-evaluation-harness](https://github.com/kurakurai/lm-evaluation-harness), which adds the
French task set: **MGSM-rev2, GPQA-Diamond, Global-MMLU-Lite, MATH-500, AIME 24, AIME 25,
HumanEval+, MBPP+, IFEval, MMLU-ProX-Lite** and **Multi-IF**.

```bash
# Install our lm-evaluation-harness fork
make eval-install
# Run the French benchmark suite with the default config
make eval
# Run it with your own config
make eval EVAL_CONFIG=configs/eval/custom.yaml
```

Multi-IF is multi-turn — each turn feeds the model its own previous answer, which the
harness's batched request flow cannot express — so it ships as a dedicated runner instead of
an `lm_eval --tasks` entry, and is run from the eval env directly:

```bash
cd third_party/lm-evaluation-harness
CUDA_VISIBLE_DEVICES=0,1 .venv/bin/python -m lm_eval.tasks.multi_if_fr \
    --model vllm \
    --model_args "pretrained=kurakurai/Luth-2-2B,dtype=bfloat16,tensor_parallel_size=2,gpu_memory_utilization=0.7,max_model_len=16384,enable_thinking=False" \
    --gen_kwargs do_sample=True,temperature=0.6,top_p=0.95,max_gen_toks=1024 \
    --output_path ../../outputs/eval --log_samples --n_runs 10
```

## Merge

Model merging with [mergekit](https://github.com/arcee-ai/mergekit), plus a custom Qwen3.5
architecture definition and a wrapper that keeps the merged model vLLM-loadable
([`tools/mergekit/`](tools/mergekit/)).

```bash
# Install mergekit and the Qwen3.5 architecture
make merge-install
# Merge with the default config, into outputs/merged
make merge
# Merge with your own config
make merge MERGE_CONFIG=configs/merge/slerp.yaml
```

## Data curation

Cleans an SFT/RL mixture before training: decontamination drops samples overlapping the eval
benchmarks (token n-gram overlap, the Tülu 3 / OLMo 3 method) and deduplication drops repeats
(exact, or near-duplicate via MinHash-LSH). Both read a dataset from the Hub and push the
cleaned version back.

```bash
# Install the SFT venv, shared with data curation
make install
# Drop training samples that overlap eval benchmarks
make decontam
# Drop duplicate samples
make dedup
```

## Citation

```bibtex
@misc{luth2,
  title  = {Luth-2: Pushing the French Capabilities of SLMs with MOPD},
  author = {Maxence Lasbordes and Guillaume Pradel},
  year   = {2026},
  url    = {https://huggingface.co/blog/MaxLSB/luth-2}
}
```
