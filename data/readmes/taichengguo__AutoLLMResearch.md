# AutoLLMResearch


https://github.com/user-attachments/assets/54df8a14-c055-41ef-969b-ef0733916a18



AutoLLMResearch is an RL-trained LLM agent that proposes configurations (hyperparameters, data mixtures, model architectures, RL hyperparameters) for language-model training tasks. The agent is trained through a three-stage pipeline — **LMConfigGym** (environment), **Policy Distillation** (SFT warm-up), and **Multi-Turn RL** (GRPO on top of the [verl](https://github.com/volcengine/verl) framework with the SGLang rollout backend) — and evaluated on offline benchmark data drawn from HW-GPT-Bench, StepLaw, ADMIRE-BayesOpt, and RegMix.

## Core Pipeline

```
 ┌──────────────────────┐   ┌───────────────────────┐   ┌──────────────────────┐
 │  1. LMConfigGym      │   │  2. Policy            │   │  3. Multi-Turn RL    │
 │  (offline simulator) │ → │     Distillation      │ → │     (GRPO + tool)    │
 │                      │   │     (SFT warm-up)     │   │                      │
 │  HW-GPT-Bench        │   │  LlamaFactory on      │   │  verl + SGLang       │
 │  StepLaw             │   │  best trajectories    │   │  `exec_config` tool  │
 │  ADMIRE-BayesOpt     │   │  → config_coder_*B    │   │  multi-turn dialogue │
 │  RegMix / RL sweeps  │   │                       │   │  against the Gym     │
 └──────────────────────┘   └───────────────────────┘   └──────────────────────┘
```

### 1. LMConfigGym — the environment

`verl/configcoder_data/HW_GPT/lmconfig_gym.py` defines `LMConfigGym`, a gym-like simulator backed by offline benchmark data. It exposes four tasks:


| Task                        | Optimization target  | Backing data                                                 |
| --------------------------- | -------------------- | ------------------------------------------------------------ |
| `rl_grpo_tuning`            | reward / accuracy    | `configcoder_data/rl_summary_all_filtered.csv`               |
| `model_architecture_tuning` | perplexity + Latency | `HW_GPT/hwgpt_sampled_results.pkl`                           |
| `data_mixture_tuning`       | `metric_avg_id+ood`  | `regmix-data/`                                               |
| `instruction_tuning`        | smooth loss          | `steplaw-main/`, `admire_ift_runs/`, `ADMIRE-BayesOpt-main/` |


Minimal usage:

```python
from verl.configcoder_data.HW_GPT.lmconfig_gym import LMConfigGym

gym = LMConfigGym()
gym.set_task("rl_grpo_tuning")
gym.set_env(task="gsm8k", model="qwen2.5-1.5B-Instruct", subject=256, epoch=15)

result = gym.query({"lr": 1e-6, "mb": 16, "kl": 0.001})
print(result["score"], result.get("additional_info"))
```

During RL training the gym is invoked from `verl/tools/configcoder_tool.py` (the `exec_config` tool): the model emits a config between `<config>...</config>` tags and the tool returns a score plus training info back into the dialogue.

### 2. Policy Distillation — SFT warm-up

Best-of-N trajectories collected against the Gym are converted into an SFT corpus (`LlamaFactory/data/config_coder.json`) and used to warm-start the policy before RL. This stage runs under `LlamaFactory/`:

```bash
cd LlamaFactory
bash run_train.sh            # full-parameter SFT for Qwen3-1.7B and Qwen3-4B
```

Key files:

- `LlamaFactory/run_train.sh` — entrypoint that drives SFT for the 1.7B and 4B variants.
- `LlamaFactory/mytrain/sql_qwen_train_toollongcot.yaml` — Hydra/YAML config (Qwen3 template, full-parameter SFT, DeepSpeed ZeRO-3, cutoff 23k).
- `LlamaFactory/data/config_coder.json` — distilled trajectories (tool-call long-CoT format) used for SFT.
- Outputs land under `LlamaFactory/saves/config_coder_{1.7B,4B}/checkpoint-*`, which are later plugged into the RL stage via `MODEL_PATH`.

Trajectories that feed this stage are produced by the trajectory-synthesis rollout described below (§ *Trajectory-synthesis rollout*).

### 3. Multi-Turn RL — GRPO on top of verl

The final stage is multi-turn GRPO with the `exec_config` tool, driven by verl + SGLang. The policy converses with the Gym turn-by-turn: propose a config → receive a score → refine.

```bash
bash run_train_configcoder.sh
```

- **Algorithm:** GRPO, multi-turn, tool-augmented (`exec_config`).
- **Rollout backend:** SGLang.
- **Config:** `examples/sglang_multiturn/config/configcoder_multiturn_grpo.yaml`.
- **Tool schema:** `examples/sglang_multiturn/config/tool_config/configcoder_tool_config.yaml`.
- **Reward:** `verl/utils/reward_score/configcoder.py` (train) and `configcoder_eval.py` (eval), wired via `custom_reward_function.path`.

## Repository Layout

```
.
├── README.md                                            # this file
├── run_train_configcoder.sh                             # stage-3: main GRPO training entrypoint
├── run_train_configcoder_eval.sh                        # stage-3: evaluation on held-out test splits
├── run_train_configcoder_eval_for_trainset.sh           # stage-3: evaluation over the train split
├── run_train_configcoder_gen_traj_syn_best.sh           # trajectory-synthesis (feeds stage-2)
│
├── data/lmconfig/                                       # parquet datasets (train_*/test_* for each task)
│
├── examples/sglang_multiturn/config/
│   ├── configcoder_multiturn_grpo.yaml                  # main multi-turn GRPO config
│   └── tool_config/configcoder_tool_config.yaml         # tool-call schema for `exec_config`
│
├── verl/                                                # verl framework (trainer/workers/...)
│   ├── tools/configcoder_tool.py                        # tool bridging model outputs → LMConfigGym.query
│   ├── utils/reward_score/
│   │   ├── configcoder.py                               # reward for training
│   │   └── configcoder_eval.py                          # reward for evaluation
│   └── configcoder_data/
│       ├── HW_GPT/
│       │   ├── lmconfig_gym.py                          # ★ LMConfigGym — the environment
│       │   ├── hwgpt_sampled_results.pkl                # HW-GPT-Bench sampled results
│       │   ├── data_mixing_random_selections_dict.pkl
│       │   ├── LICENSE
│       │   └── README.md
│       ├── steplaw-main/                                # StepLaw benchmark (instruction-tuning env)
│       ├── ADMIRE-BayesOpt-main/                        # ADMIRE-BayesOpt (instruction-tuning env)
│       ├── regmix-data/                                 # RegMix (data-mixture env)
│       ├── admire_ift_runs/
│       ├── rl_summary_all_filtered.csv                  # filtered RL sweep (GRPO env)
│       ├── rl_summary_all.csv / rl_summary1.csv
│       └── Performance_Law.xlsx
│
└── LlamaFactory/                                        # stage-2: Policy Distillation (SFT warm-up)
    ├── run_train.sh                                     # SFT entrypoint for Qwen3-1.7B / 4B
    ├── mytrain/                                         # project-specific SFT YAMLs
    │   └── sql_qwen_train_toollongcot.yaml              # full-parameter tool-long-CoT SFT config
    ├── data/config_coder.json                           # distilled trajectories for SFT
    └── src/                                             # upstream LlamaFactory source
```

## Installation

```bash
# conda env (Python 3.10+ recommended)
conda create -n autollmresearch python=3.10 -y
conda activate autollmresearch

# RL stack (verl + SGLang rollout backend)
pip install -e .                        # installs verl from this repo
pip install sglang
pip install transformers accelerate ray pandas pyarrow tqdm wandb

# SFT stack (Policy Distillation)
cd LlamaFactory && pip install -e ".[torch,metrics]" && cd ..

# (optional) log in to W&B if you use the wandb logger
wandb login
```

Hardware: RL configs assume ≥4× GPUs (80GB class; adjust `trainer.n_gpus_per_node`, `*.ppo_micro_batch_size_per_gpu`, `*.max_token_len_per_gpu` for your setup). SFT also runs on 4× 80GB with DeepSpeed ZeRO-3.

## How to Run

All RL scripts are launched from the repo root and resolve paths via `PROJECT_DIR="$(pwd)"`.

### Stage 1 — Probe the Gym (optional sanity check)

Import `LMConfigGym` in a Python shell (see the snippet under *LMConfigGym* above) to confirm the backing data files are in place before training.

### Stage 2 — Policy Distillation (SFT)

```bash
cd LlamaFactory
bash run_train.sh
```

This produces `LlamaFactory/saves/config_coder_{1.7B,4B}/checkpoint-*`, which you then plug into the RL stage by setting `MODEL_PATH` inside `run_train_configcoder.sh`.

### Stage 3 — Multi-Turn RL (GRPO)

```bash
bash run_train_configcoder.sh
```

Key knobs inside the script:

- `MODEL_PATH` — base model (default `Qwen/Qwen3-4B`; also tested with 1.7B / 8B / 14B, or an SFT checkpoint path from stage 2)
- `Compare_OR_VALUE` — dataset variant: `VALUE` (default), `COMPARE`, or `ABLATION`. This picks `data/lmconfig/train${data_suffix}.parquet` / `test${data_suffix}.parquet`
- `TOTAL_EPOCHS` — number of GRPO epochs
- `trainer.n_gpus_per_node=4` / `CUDA_VISIBLE_DEVICES=0,1,2,3` — GPU count

Artifacts:

- logs: `train_configcoder_<model>.log`
- rollouts: `./<data>${data_suffix}_<model>_rollouts_configcoder_train/`
- W&B project: `verl_grpo_configcoder`

### Evaluation (validation only)

```bash
bash run_train_configcoder_eval.sh
```

Sets `TOTAL_EPOCHS=0` with `trainer.val_before_train=True`, so it runs the rollout/validation pass without updating weights. Edit `MODEL_PATHS` inside the script to point at the checkpoints you want to score.

### Evaluation over the train split

```bash
bash run_train_configcoder_eval_for_trainset.sh
```

Same idea as above, but uses a train-split parquet as `data.val_files` — useful for diagnosing RL-memorization vs. generalization.

### Trajectory-synthesis rollout (produces data for stage 2)

```bash
bash run_train_configcoder_gen_traj_syn_best.sh
```

Runs validation against `data/lmconfig/added_gen_traj_data.parquet` to generate best-of-N trajectories (`actor_rollout_ref.rollout.n=5`, `do_sample=True`). The resulting trajectories are post-processed into `LlamaFactory/data/config_coder.json` to feed the next round of Policy Distillation.

## Data

`data/lmconfig/` contains per-task parquet splits used directly by the scripts:

- `train_VALUE*.parquet`, `test_VALUE*.parquet` — main value-regression splits (aggregate + per-task, plus `_low_fidelity` / `_medium_fidelity` / `_progress` / `_budget_1_2` variants)
- `train_COMPARE.parquet` / `train_ABLATION.parquet` and `_WO_Text_Info`, `_WO_Elite` variants — ablations
- `added_gen_traj_data.parquet` — trajectory-synthesis eval set

The four per-task splits correspond to the `LMConfigGym` tasks listed above.

## Placeholders in the scripts

Some paths in the shell scripts are intentionally left as placeholders — fill them in before running:

- `<PATH_TO_SFT_CKPT>/config_coder_{1.7B,4B}/checkpoint-*` — the SFT checkpoints produced in stage 2
- `<PATH_TO_INDEX>` / `<PATH_TO_CORPUS>` in `examples/sglang_multiturn/search_r1_like/local_dense_retriever/retrieval_server.py` — only relevant if you use that (unrelated) retrieval example

