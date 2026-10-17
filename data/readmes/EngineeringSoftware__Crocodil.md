# <img src="logo.svg" alt="crocodile" height="30"> CROCODIL

## About

This repo hosts the code and data for the following EMNLP 2026 Findings paper:

[CROCODIL: Cross-Model Code Editing with LLMs](https://arxiv.org/abs/2609.03894)

Authors: Linghan Zhong, Aditya Thimmaiah, Jayanth Srinivasa, Milos Gligoric, Junyi Jessy Li

```bibtex
@inproceedings{ZhongETAL26CROCODIL,
  author = {Zhong, Linghan and Thimmaiah, Aditya and Srinivasa, Jayanth and Gligoric, Milos and Li, Junyi Jessy},
  title = {{CROCODIL}: Cross-Model Code Editing with {LLMs}},
  booktitle = {Findings of the Conference on Empirical Methods in Natural Language Processing},
  pages = {To appear},
  year = {2026},
}
```

## Setup

Needs `direnv`, `uv`, Python 3.12, `cargo` + `rustfmt`, `rust-analyzer`,
`cargo-llvm-cov`. Local inference needs a GPU host. Data collection needs
`GITHUB_TOKEN`. Claude Haiku runs on AWS Bedrock, so it needs
`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.

```bash
direnv allow    # exports REPO_DIR, SCRIPT_DIR, PYTHON_DIR, WORK_DIR, PAPER_DIR, PYTHONPATH
```

alternatively manually loading the necessary environment variables are also possible with

``` bash
source .envrc
```

Torch arrives transitively (`trl`, `peft`) and PyPI serves a CUDA build on
every platform, so pick a backend explicitly when the default is wrong:

```bash
uv sync --extra cuda    # NVIDIA, CUDA 12.8
uv sync --extra rocm    # AMD, ROCm 6.4
uv sync --extra cpu     # no GPU, drops ~3.5GB of unusable nvidia wheels
```

## Tests

```bash
uv run pytest python/tests
```

## Docker

The image carries the code and the toolchain (Python venv, llama.cpp, Rust);
data is mounted. Copy `.env.example` to `.env` first if you need
`GITHUB_TOKEN`, `HF_TOKEN`, AWS credentials, or a `_work` outside the repo.

```bash
docker compose up -d --build                                                    # CPU, works on Apple Silicon
docker compose -f docker-compose.yml -f docker-compose.cuda.yml up -d --build   # NVIDIA
docker compose exec app bash
```

```bash
bash scripts/pipeline/pr_rewrite_edit_pipeline.sh --download-gguf
pytest python/tests
```

## Data

Every artifact the paper reports is released as one Hugging Face
dataset:

<https://huggingface.co/datasets/EngineeringSoftware/Crocodil-data>

Unpack it into `$WORK_DIR` and every stage below finds its inputs
already there, so any stage can be re-run without repeating the ones
before it.

```bash
uv run hf download EngineeringSoftware/Crocodil-data \
    --repo-type=dataset --local-dir="$WORK_DIR"
```

## Collecting a corpus
Only needed to rebuild the corpus from scratch. The released data above
already contains it.

```bash
export GITHUB_TOKEN=...
C=scripts/pipeline/data_collection_pipeline.sh

COLLECTION_NAME=big_rust_repos bash $C --collect_repos   # crates.io -> big_rust_repos.txt
bash $C --split_repos            # big_rust_repos -> eval_rust_repos + training_rust_repos

for N in eval_rust_repos training_rust_repos; do
  export COLLECTION_NAME=$N
  bash $C --collect_prs
  bash $C --extract_functions
  bash $C --collect_readmes      # PRs whose repo has no README are dropped downstream
  bash $C --pr_inference         # GPU host
  bash $C --extract_tests        # cargo host, needs cargo-llvm-cov
  bash $C --after_only_tests     # cargo host; a function needs a test that fails on its pre-edit body
  bash $C --extract_call_info    # needs rust-analyzer
  bash $C --extract_use_stmts
done
```

## Downloading model weights
```bash
ALL="qwen3.5-thinking:35b-a3b-q4_k_m gpt-oss:20b-q4_k_m \
     olmo3-thinking:7b.think-q4_k_m olmo3.1-thinking:32b.think-q4_k_m"
export REWRITE_MODELS_LIST="$ALL" EDIT_MODELS_LIST="$ALL"

bash scripts/pipeline/pr_rewrite_edit_pipeline.sh --download-gguf
```

The two `*_MODELS_LIST` vars override the model arrays in
`scripts/pipeline/pr_pipeline_common.sh` for one run.

## Claude Haiku (AWS Bedrock)

```bash
export AWS_ACCESS_KEY_ID=... AWS_SECRET_ACCESS_KEY=...
export AWS_REGION=us-east-1      # only region with the model enabled, and the default
```

## Reproducing Tables 2 and 3

```bash
ALL="qwen3.5-thinking:35b-a3b-q4_k_m gpt-oss:20b-q4_k_m \
     olmo3-thinking:7b.think-q4_k_m olmo3.1-thinking:32b.think-q4_k_m claude-haiku-4-5"
export rewrite_models_list="$ALL" EDIT_MODELS_LIST="$ALL"

P=scripts/pipeline/pr_rewrite_edit_pipeline.sh

bash $P --download-gguf                  # GPU host
bash $P --desc                           # GPU host
bash $P --rewrite                        # GPU host + AWS creds
bash $P --eval-rewrite                   # cargo host, required before --rewrite-repair
bash $P --rewrite-repair                 # GPU host + AWS creds
bash $P --rewrite-overlap                # writes the overlap gate file
bash $P --eval-rewrite-after-postrepair  # cargo host, required before --edit
bash $P --edit                           # GPU host + AWS creds
bash $P --overlap-edit                   # laptop
bash $P --overlap-edit-rustfmt           # laptop, needs rustfmt only

bash scripts/pipeline/paper_pipeline.sh --crossedit-tables
```

## Training CROCODIL

GRPO through verl. `verl` is not in `pyproject.toml`. The paper ran verl 0.7.1 on vllm 0.11.2 (image `rocm/vllm:rocm7.0.0_vllm_0.11.2_20251210`). Install both into the venv;
without vllm the pipeline falls back to the `hf` rollout, which is slower.

Training data is the Qwen reimplementation of `training_rust_repos`
after 10 repair rounds, restricted to functions whose reimplementation
still fails the post-PR tests. Build it with the corpus recipe above,
then:

```bash
P=scripts/pipeline/pr_rewrite_edit_pipeline.sh
export REWRITE_MODELS_LIST="qwen3.5-thinking:35b-a3b-q4_k_m"
export REPAIR_NUM_ROUNDS=10
D=--pr-dataset-name=training_rust_repos

bash $P $D --download-gguf --desc --rewrite    # GPU host
bash $P $D --eval-rewrite                      # cargo host
bash $P $D --rewrite-repair                    # GPU + cargo host
```

The preset keeps every reimplementation (`overlap_max: null`), so
`--rewrite-overlap` is not needed here.

```bash
V=scripts/pipeline/verl/verl_pipeline.sh
CFG=--config=olmo3-7b-think/training_rust_repos

bash $V $CFG --eval-rewrite-after          # cargo host, writes the -after.jsonl --prepare-run reads
bash $V $CFG --prepare-run --train         # GPU host
```

Post-train evaluation converts the LoRA to GGUF and runs it as the editor
through llama.cpp. It needs a llama.cpp checkout with its own venv at
`$LLAMA_CPP_PATH` (default `/root/llama.cpp`) for `convert_lora_to_gguf.py`,
and the base GGUF the adapter loads onto:

```bash
EDIT_MODELS_LIST="olmo3:7b.think-q4_k_m" bash $P --download-gguf
```

Then run the RL rows in the next section with `--output-dir=<run dir>`.

## Reproducing Tables 4 to 7

Run after the Tables 2 and 3 chain. The checkpoint is the run dir from the
training section, or any directory under `_model/` in verl's own layout.

```
_model/<run dir>/
  global_step_<N>/actor/lora_adapter/
    adapter_config.json
    adapter_model.safetensors
```

`<run dir>` is any nesting you like under `_model/`. In the commands
below it becomes `--output-dir=_model/<run dir>`, with the step
directory as `--resume global_step_<N>`. Drop `--resume` to take the
step named in `<run dir>/latest_checkpointed_iteration.txt`. The tuned
model name is `<run dir>/global_step_<N>/actor/lora_adapter` with `/`
replaced by `-`, so it changes if the checkpoint moves.

```bash
P=scripts/pipeline/pr_rewrite_edit_pipeline.sh
V=scripts/pipeline/verl/verl_pipeline.sh

OPEN="qwen3.5-thinking:35b-a3b-q4_k_m gpt-oss:20b-q4_k_m \
      olmo3-thinking:7b.think-q4_k_m olmo3.1-thinking:32b.think-q4_k_m"
export REWRITE_MODELS_LIST="$OPEN"
export EDIT_MODELS_LIST="olmo3-thinking:7b.think-q4_k_m"

# base rows
bash $P --edit                                       # GPU host
bash $P --eval-edit                                  # cargo host
bash $P --overlap-edit --overlap-edit-rustfmt        # laptop, needs rustfmt only

# prompt-only baseline rows
bash $P --edit-limit                                 # GPU host
for R in $OPEN; do                                   # cargo host
  bash $P --overlap-edit-limit --eval-edit-limit --pr-dataset-name=eval_rust_repos@$R
done

# RL rows
bash $V --gguf-edit-train --infer-edit-train --overlap-edit-train --eval-edit-train \
     --config=olmo3-7b-think/training_rust_repos \
     --output-dir=_model/<run dir> --resume global_step_<N>

bash scripts/pipeline/paper_pipeline.sh --verl-tables
```
