# Composable Soft-Prompt Distillation of RL Experts

<p align="center">
  <a href="https://arxiv.org/abs/2611.27376"><img src="https://img.shields.io/badge/arXiv-2611.27376-b31b1b.svg" alt="arXiv"></a>
  <a href="https://huggingface.co/datasets/ucsbai/cspd"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-prompts%20%26%20data-ffd21e.svg" alt="Hugging Face"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg" alt="License: CC BY-NC 4.0"></a>
</p>

Code for [**Composable Soft-Prompt Distillation of RL Experts: Toward Continual Post-Training**](https://arxiv.org/abs/2611.27376).

RL post-training produces domain experts that must then be consolidated into one model. Weight merging and multi-teacher on-policy distillation (MOPD) re-consolidate the whole model whenever an expert is added, and can erode capabilities outside the target domains. **CSPD** keeps the pre-RL model frozen, distills each RL expert independently into a **soft prompt** (256 trainable input vectors), and composes experts by **concatenating their prompts** at inference, without any joint training.

<p align="center"><img src="docs/figures/cspd_mopd_comparison.png" width="90%"></p>

- **One prompt per expert.** A single soft prompt recovers at least 90% of the teacher's gain in 22 of 23 math, code and agent settings (7B–35B, dense and MoE).
- **Plug-in composition.** Four independently trained prompts (math, code, science, instruction following) on M2RL-SFT reach 67.83 on the in-domain average, on par with MOPD (67.79), and the average rises with every expert added.
- **Generalization.** The composition has the best mean (56.6) on six held-out benchmarks, while MOPD loses 3.6 points on TruthfulQA.
- **Cheap serving.** Per-request soft prompts keep throughput within 1.5% of the unadapted backbone and reach 2.40× the throughput of rank-4 LoRA on one B200.

<p align="center"><img src="docs/figures/cspd_overview.png" width="100%"></p>

## Reproduce with a coding agent

Paste this prompt into a coding agent (Claude Code, Codex, Cursor and similar) running on a GPU machine. The agent reads [AGENTS.md](AGENTS.md) for the environments, commands and paper numbers. It then downloads the four released soft prompts, composes them and reports Table 2 next to the paper. Each benchmark takes one GPU, a few hours each on a B200.

```text
Clone https://github.com/UCSB-AI/CSPD and read AGENTS.md. Reproduce Table 2
(task A): compose the four released soft prompts in the MCSI order, then generate and score AIME24,
LiveCodeBench v5, GPQA-Diamond and IFBench. Ask me for an HF token if GPQA needs one, run code
scoring in a sandbox, and do not change any grader, prompt or decoding setting. Report your scores,
the paper's scores and the differences in one table.
```

For the reverse order, replace `MCSI` with `ISCM` in the prompt.

## Method

For each expert, the teacher (the post-RL checkpoint) generates responses offline. Only the prompt vectors are trained, with the response-only language-modeling loss, on the frozen pre-RL student. The prompt is inserted right after the system header. **Prefix-robust training** inserts 128–256 tokens of other examples from the same domain in front of the prompt on half of the training examples, so each prompt learns to work behind other prompts. At inference, prompts are concatenated in a chosen order (`MCSI` = math, code, science, instruction following; the last module sits next to the question).

## Results

### Distilling individual RL experts (Table 1)

Recovery = 100 × (Student+SP − Student) / (Teacher − Student). All scores are percentages.

| Domain | Pre-RL checkpoint → RL expert | Student | Teacher | Student+SP | Recovery |
| --- | --- | ---: | ---: | ---: | ---: |
| Math | MiMo-7B-SFT → MiMo-7B-RL | 63.77 | 73.18 | 72.25 | 90.15 |
| Math | GPT-OSS-Swallow-20B SFT → RL | 76.53 | 90.21 | 89.67 | 96.06 |
| Math | Qwen3-Swallow-8B SFT → RL | 63.68 | 83.01 | 82.28 | 96.22 |
| Math | OLMo-3-7B-Instruct-DPO → Instruct | 42.97 | 60.72 | 60.13 | 96.70 |
| Math | Nemotron-Cascade-8B SFT → MathRL | 85.25 | 89.34 | 89.30 | 99.18 |
| Math | Qwen3-Swallow-30B-A3B SFT → RL | 72.91 | 86.25 | 86.23 | 99.79 |
| Math | Eurus-2-7B-SFT → PRIME | 36.06 | 49.63 | 49.91 | 102.07 |
| Math | INTELLECT-MATH SFT → RL | 45.47 | 54.11 | 54.62 | 105.89 |
| Math | Poro-2-8B-Long-Math SFT → RL | 68.34 | 72.43 | 73.88 | 135.47 |
| Math | Klear-Reasoner-8B SFT → RL | 62.15 | 65.00 | 66.11 | 139.02 |
| Code | MiMo-7B-SFT → MiMo-7B-RL | 50.17 | 52.87 | 52.55 | 88.08 |
| Code | Nemotron-Cascade-8B SFT → CodeRL | 55.73 | 69.39 | 69.56 | 101.21 |
| Code | Klear-Reasoner-8B SFT → RL | 53.44 | 57.27 | 57.34 | 101.83 |
| Code | Qwen3-14B → AReaL-boba-2-14B-Open | 64.86 | 68.06 | 68.14 | 102.38 |
| Code | Mellum2-12B-A2.5B SFT → Instruct | 36.30 | 39.05 | 39.34 | 110.34 |
| Code | Qwen3-8B → AReaL-boba-2-8B-Open | 58.54 | 62.20 | 62.96 | 120.83 |
| Code | OLMo-3-7B-Instruct-DPO → Instruct | 28.50 | 34.10 | 36.54 | 143.44 |
| SWE-bench Verified | Nemotron-Cascade-8B SFT → final | 23.60 | 34.60 | 33.75† | 92.27† |
| SWE-bench Verified | Qwen3-32B → DeepSWE-Preview | 24.90 | 44.05 | 45.65 | 108.36 |
| SWE-bench Verified | Qwen3.5-35B-A3B → Lego-RL-35B-A3B | 64.00 | 70.40 | 72.25 | 128.91 |
| SWE-bench Verified | SWE-Gym-OpenHands-7B → SkyRL-Agent-7B-v0 | 11.40 | 12.80 | 13.60 | 157.14 |
| Terminal-Bench 2.1 | Qwen3.5-9B → TMax-9B | 20.22 | 28.09 | 29.96 | 123.81 |
| Terminal-Bench 2.1 | Qwen3.6-27B → TMax-27B | 43.45 | 46.07 | 48.69 | 200.00 |

† The prompted student receives the teacher's predicted bug locations. Benchmark mixes per row are listed in the paper (Table 1).

### Composing experts (Table 2)

Student: M2RL-SFT (Qwen3-4B). Teachers: the four M2RL RL experts. avg@K with K = 64/8/16/8.

| Method | AIME24 | LCB v5 | GPQA-D | IFBench | Avg. | Recovery |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Student (no prompt) | 55.94 | 58.61 | 44.38 | 42.71 | 50.41 | 0.0 |
| Individual experts (oracle routing) | 81.77 | 66.92 | 50.44 | 67.33 | 66.61 | 100.0 |
| Expert merge (TA, λ = 1.0) | 78.85 | 64.52 | 54.14 | 71.58 | 67.27 | 104.1 |
| Expert merge (TIES) | 81.25 | 65.42 | 57.07 | 66.12 | 67.47 | 105.2 |
| MOPD | 83.28 | 66.24 | 55.21 | 66.42 | 67.79 | 107.2 |
| LoRA distill + TA (λ = 0.5) | 80.21 | 63.10 | 56.22 | 62.46 | 65.50 | 93.1 |
| LoRA distill + TIES | 81.41 | 64.00 | 56.66 | 62.67 | 66.19 | 97.3 |
| Single-domain SP | 80.89 | 64.67 | 49.24 | 66.71 | 65.38 | 92.4 |
| CSPD w/o prefix-robust training (AdamW) | 76.98 | 64.15 | 51.89 | 65.00 | 64.50 | 87.0 |
| CSPD (ISCM) | 79.90 | 65.72 | 57.92 | 67.33 | 67.72 | 106.8 |
| **CSPD (MCSI)** | 80.47 | 64.67 | 57.77 | 68.42 | **67.83** | **107.5** |

<p align="center"><img src="docs/figures/composition_dynamics.png" width="85%"></p>

Adding experts one at a time (I → S → C → M) raises the average at every step; removing one prompt mostly costs its own domain (Figure 3). Independent training beats progressive training at every stage:

<p align="center"><img src="docs/figures/progressive_domain_comparison.png" width="100%"></p>

### Out-of-domain generalization (Table 3)

| Method | XSTest | TruthfulQA | BFCL | TriviaQA | BBEH | FinQA | Mean |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Student (no prompt) | 80.4 | **64.6** | 47.6 | 31.5 | 11.1 | 66.3 | 50.3 |
| Expert merge (TIES) | 82.4 | 63.7 | 48.5 | **33.6** | 25.6 | 70.9 | 54.1 |
| MOPD | 84.2 | 61.0 | 49.4 | 31.9 | 23.9 | 70.8 | 53.5 |
| LoRA distill + TA (λ = 0.5) | 85.1 | 63.8 | 47.5 | 32.7 | 23.0 | 70.9 | 53.8 |
| **CSPD (MCSI)** | **88.2** | 64.2 | **55.6** | 33.5 | **25.8** | **72.5** | **56.6** |

### Serving (Figure 5) and mechanism (Figure 6)

GPT-OSS-20B (BF16) on one B200, 20,480 input and 512 output tokens per request, a distinct adapter per request. At 32 concurrent requests, soft prompts serve 715.4 output tokens/s (backbone 721.3, rank-4 LoRA 298.5) and cut P95 time to first token from 39.21 s (LoRA) to 17.26 s.

<p align="center"><img src="docs/figures/serving_b200.png" width="80%"></p>

<p align="center"><img src="docs/figures/sp_interp_main.png" width="85%"></p>

## Released artifacts

[ucsbai/cspd](https://huggingface.co/datasets/ucsbai/cspd) holds the four M2RL domain prompts (step 200), the packed teacher responses used to train them (math 11,508, code 7,968, science 12,642, instruction following 14,179 responses), single-expert prompts for seventeen Table 1 settings (math: MiMo-7B, Poro-2-8B, Qwen3-Swallow-8B and 30B-A3B, Eurus-2-7B, Klear-Reasoner-8B; code: MiMo-7B, Nemotron-Cascade-8B, Klear-Reasoner-8B, AReaL-boba-2-14B and 8B, Mellum2-12B-A2.5B, OLMo-3-7B; agent: Nemotron-Cascade-8B SWE, SkyRL-Agent-7B, TMax-9B and 27B), and the prompt checkpoints every 20 updates for six pairs used in the mechanism analysis (`trajectories/`). `compose.py --paper-order` downloads the M2RL prompts and checks their SHA-256.

## Repository layout

```
src/soft_prompt_distillation/   core library: sampling, frozen-backbone prompt training, task adapters, graders
configs/
  math/, code/                  one config per Table 1 setting (math and code)
  ablations/                    GPT-OSS prompt-length sweep and training curve
  smoke.yaml                    small end-to-end check
scripts/run_pipeline.sh         sample -> train -> evaluate for one single-expert config
experiments/
  m2rl/                         multi-expert composition (Table 2, Figure 3, Table 3)
    teacher/                    teacher data: RL-blend questions, teacher sampling, M2RL reward verification
    pack_data.py                pack verified responses for training
    train_sp.py                 train one domain prompt (prefix-robust, Muon, cosine)
    compose.py                  concatenate prompts in any order
    eval/                       generation (SGLang or vLLM) and official graders; benchmark inputs
    baselines/                  Task Arithmetic / TIES merging and LoRA distillation
    ood/                        out-of-domain inputs and scorers
  agents/                       SWE-bench and Terminal-Bench prompt training (Nemotron, SkyRL, TMax)
  serving/                      B200 multi-adapter benchmark (Figure 5) and SGLang patch
  speculative-decoding/         EAGLE-3 / DFlash acceptance with soft prompts
  interp/                       GPT-OSS mechanism analysis (Figure 6, Appendix G)
  paper-figures/                scripts that redraw the paper figures
tests/                          CPU test suite
```

## Installation

```bash
python3.11 -m venv .venv && source .venv/bin/activate
pip install -e '.[train,data,test]'
pytest                                  # CPU tests
```

The single-expert pipeline generates with SGLang (`pip install -e '.[sglang]'`, see `scripts/setup_runtime.sh`). For the multi-expert experiments, generation (`teacher/sample_teacher.py`, `eval/generate.py`, `ood/bfcl/run.py`) runs in the SGLang 0.5.18 environment from `scripts/setup_blackwell_runtime.sh`. Training, baselines and scoring run in the environment pinned in [`experiments/m2rl/requirements.txt`](experiments/m2rl/requirements.txt), which also provides vLLM 0.11 for `--engine vllm` and the XSTest judge.

## Reproducing the experiments

### Multi-expert composition (Table 2, Figure 3)

Released prompts can be composed and evaluated directly. Each step below runs on one GPU.

```bash
# 1. compose the released step-200 prompts (downloads and checks their SHA-256)
python experiments/m2rl/compose.py --paper-order MCSI --output artifacts/MCSI.safetensors

# 2. generate (K defaults to the paper's 64/8/16/8) and score with the official graders
python experiments/m2rl/eval/build_gpqa.py          # GPQA prompts, needs access to Idavidrein/gpqa
for bench in aime24 lcb_v5 gpqa_diamond ifbench; do
  python experiments/m2rl/eval/generate.py --bench $bench --prompt artifacts/MCSI.safetensors \
      --output runs/MCSI/$bench.jsonl
  python experiments/m2rl/eval/score.py --bench $bench --responses runs/MCSI/$bench.jsonl
done
```

Omit `--prompt` for the student, use `--paper-order ISCM` for the reverse order, `I`, `SI`, `CSI` for the continual-addition stages, and drop one letter for leave-one-out. LiveCodeBench scoring executes generated code; run it in a sandbox.

To train the prompts from scratch, download the packed teacher responses from [ucsbai/cspd](https://huggingface.co/datasets/ucsbai/cspd), or regenerate them from the RL experts:

```bash
# regenerate one domain's teacher data (math | code | science | if); code grading runs generated programs, use a sandbox
python experiments/m2rl/teacher/build_questions.py --domain math --output runs/teacher/math/questions.jsonl
python experiments/m2rl/teacher/sample_teacher.py --domain math --questions runs/teacher/math/questions.jsonl --output runs/teacher/math
python experiments/m2rl/pack_data.py runs/teacher/math data/m2rl/math     # --max-per-question 2 for code
```

Then train each domain prompt:

```bash
hf download ucsbai/cspd --repo-type dataset --include 'data/*' --local-dir .   # or use the regenerated data
torchrun --nproc-per-node 4 experiments/m2rl/train_sp.py --data data/m2rl/math --output runs/m2rl/math
# the 'w/o prefix-robust training' row of Table 2 also uses AdamW (Table 5)
torchrun --nproc-per-node 4 experiments/m2rl/train_sp.py --data data/m2rl/if --output runs/m2rl/if-no-prefix --no-prefix-robust --optimizer adamw
python experiments/m2rl/compose.py --module M=runs/m2rl/math/checkpoints/update-0200/state.pt ... --output artifacts/mine.safetensors
```

Progressive training (Figure 4) passes the earlier prompts with `--frozen-prompts`. Baselines: `baselines/merge_models.py` (TA and TIES over the four RL experts or the merged LoRA students) and `baselines/lora_distill.py` (rank 16 on the same data and batches). MOPD is the released `Jackwang111/M2RL-MT_OPD` checkpoint; all model revisions are listed in [experiments/m2rl](experiments/m2rl/README.md).

### Out-of-domain evaluation (Table 3)

```bash
python experiments/m2rl/ood/build_inputs.py         # TriviaQA, TruthfulQA, XSTest, BBEH, FinQA
python experiments/m2rl/eval/generate.py --bench finqa --inputs experiments/m2rl/ood/inputs \
    --prompt artifacts/MCSI.safetensors --output runs/MCSI/finqa.jsonl
python experiments/m2rl/ood/score.py --bench finqa --responses runs/MCSI/finqa.jsonl
```

XSTest is judged by Qwen3Guard-Gen-8B (`ood/score.py` loads it with vLLM). BFCL runs with `experiments/m2rl/ood/bfcl/run.py` (official BFCL handler and checker at a pinned commit, generation through SGLang); see the [benchmark versions](experiments/m2rl/BENCHMARKS.md), which pin every dataset and grader revision used in Tables 2 and 3.

### Single-expert distillation (Table 1)

Each config holds the model revisions, data, template and evaluation settings for one row.

```bash
bash scripts/run_pipeline.sh configs/math/qwen3-swallow-8b.yaml runs/qwen3-swallow-8b
```

The pipeline evaluates student and teacher, samples teacher responses, trains the prompt, and evaluates checkpoints; `soft-prompt-distill {sample,train,evaluate} --help` runs the stages separately. Start with `configs/smoke.yaml`. GPT-OSS-Swallow-20B uses `configs/math/gpt-oss-swallow-20b.yaml` (correct-only supervision; the same config builds the mixed-supervision arm of Table 4), and `configs/ablations/` holds the prompt-length sweep and training curve. Where the original RL data are not public, the configs use the proxy data named in the paper (DeepScaleR for MiMo math, AReaL code data for MiMo code, Klear code data for Mellum2 and Nemotron CodeRL). See [docs/single-expert.md](docs/single-expert.md) and [docs/CODE_VERIFICATION.md](docs/CODE_VERIFICATION.md) for the code grader.

Agent prompt training is in [experiments/agents](experiments/agents/README.md).

### Serving, speculative decoding and analysis

- [experiments/serving](experiments/serving/README.md): upstream SGLang plus [engine.patch](experiments/serving/engine.patch), workload generator and the B200 benchmark launcher.
- [experiments/speculative-decoding](experiments/speculative-decoding/spec/README.md): EAGLE-3 and DFlash acceptance length with and without a prompt.
- [experiments/interp](experiments/interp/README.md): trace generation, teacher-forced KL, nearest-neighbor tokens and attention-pathway interventions.
- `python experiments/paper-figures/scripts/plot_*.py` redraws the paper figures from the reported numbers.

## Citation

```bibtex
@article{zhang2026cspd,
  title  = {Composable Soft-Prompt Distillation of RL Experts: Toward Continual Post-Training},
  author = {Zhang, Zhen and Yang, Changyi and He, Xuehai and Liu, Chengzhi and Yin, Yutong and Liu, Ziyue and Yin, Zhuoran and Li, Yangmin and Liu, Zhihan and Li, Jisen and Jin, Mingyu and Li, Chuhan and Weng, Zhaotian and He, Ruoyu and Gao, Wenyao and Deng, Jiaxin and Wu, Chenwei and Shen, Hui and Chai, Wenhao and Zhao, Chenyang and Ying, Zhuofan and Liu, Kieran and Chen, Andrew and Ma, Pony and Wang, Zhaoran and Patel, Alkesh and Gan, Zhe and Wang, Xin Eric},
  journal = {arXiv preprint arXiv:2611.27376},
  year   = {2026}
}
```

## License

Code is released under [CC BY-NC 4.0](LICENSE) (non-commercial use, with attribution). Vendored third-party files keep their original licenses; see [NOTICE](NOTICE) and [licenses/](licenses/). Models, datasets and benchmarks follow their own licenses.
