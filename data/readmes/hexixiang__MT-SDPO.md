<div align="center">

# Learn from Whoever Is Right: Answer-Verified Multi-Teacher Distillation for Multi-Domain LLMs

**Xixiang He<sup>1</sup> · Xingming Li<sup>1</sup> · Baiqi Wu<sup>2</sup> · Qiyao Sun<sup>1</sup> · Xuanyu Ji<sup>1</sup> · Ao Cheng<sup>1</sup> · Qingyong Hu<sup>3✉</sup>**

<sup>1</sup>National University of Defense Technology &nbsp; <sup>2</sup>Zhejiang University &nbsp; <sup>3</sup>Intelligent Game and Decision Lab &nbsp; <sup>✉</sup>Corresponding author

[![arXiv](https://img.shields.io/badge/arXiv-2609.02548-b31b1b.svg?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2609.02548)
[![Models](https://img.shields.io/badge/%F0%9F%A4%97%20Models-coming%20soon-lightgrey)](#-news)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

<img src="assets/teaser.png" alt="Domain routing vs. MT-SDPO" width="55%">

</div>

## 📢 News

- **[2026-09-03]** 🔥 Paper released on [arXiv](https://arxiv.org/abs/2609.02548), together with the SciKnowEval-L3 datasets, training code and the frozen evaluation protocol.
- **[TODO]** Release model weights (domain teachers, Multi-Domain initializations and MT-SDPO students) for all five backbones.

## 🔎 Overview

<p align="center"><img src="assets/overview.png" alt="MT-SDPO overview" width="100%"></p>

Routing each training sample to the teacher whose domain label matches assumes that teacher is right. It often is not, while a teacher from another domain is. **MT-SDPO** (Multi-Teacher Self-Distillation Policy Optimization) decides who teaches **per sample, not per domain**:

- **Self-anchor** — a correct rollout from the student's own group supervises its incorrect siblings.
- **Answer-verified eligibility** — a frozen teacher may supervise a sample only if its own private answer passes the verifier.
- **Privileged distillation** — the anchor and all verified feedback form one privileged context that an EMA self-teacher reads and the student does not, so a single policy is deployed with no router, verifier or teacher at inference.

## 📊 Main Results

SciKnowEval-L3 avg@16 accuracy (%) at step 100. **Worst** is the weakest of chemistry / materials / physics; **Gap** is best minus worst. Δ is relative to the shared Multi-Domain Post-Training (PT) initialization.

| Student | Method | Macro ↑ | Worst ↑ | Gap ↓ |
|:--|:--|--:|--:|--:|
| Qwen3-1.7B | Multi-Domain PT | 52.35 | 42.33 | 20.73 |
| | Domain Routing | 48.52 (−3.83) | 44.78 (+2.45) | 10.68 (−10.05) |
| | **MT-SDPO** | 49.79 (−2.56) | **46.20 (+3.87)** | **10.44 (−10.29)** |
| Qwen3-4B | Multi-Domain PT | 62.90 | 48.66 | 22.71 |
| | Domain Routing | 58.94 (−3.96) | 47.78 (−0.88) | 17.48 (−5.23) |
| | **MT-SDPO** | 58.94 (−3.96) | **50.63 (+1.97)** | **13.29 (−9.42)** |
| Qwen3-8B | Multi-Domain PT | 62.47 | 49.29 | 20.96 |
| | Domain Routing | 64.21 (+1.74) | 62.03 (+12.74) | 5.30 (−15.66) |
| | **MT-SDPO** | **67.11 (+4.64)** | **64.08 (+14.79)** | **5.30 (−15.66)** |
| Llama-3.1-8B-Instruct | Multi-Domain PT | 55.78 | 51.42 | 8.15 |
| | Domain Routing | 51.53 (−4.25) | 43.43 (−7.99) | 13.77 (+5.62) |
| | **MT-SDPO** | **52.56 (−3.22)** | **44.62 (−6.80)** | 14.95 (+6.80) |
| OLMo-3-7B-Instruct | Multi-Domain PT | 56.43 | 48.42 | 14.79 |
| | Domain Routing | 59.92 (+3.49) | 51.90 (+3.48) | 12.66 (−2.13) |
| | **MT-SDPO** | **62.02 (+5.59)** | **55.69 (+7.27)** | **10.13 (−4.66)** |

**Ablation on Qwen3-8B** (same teachers, anchor, self-teacher, initialization and budget; only the allocation rule changes):

| Method | Macro ↑ | Worst ↑ | Gap ↓ |
|:--|--:|--:|--:|
| w/o Verification | 60.55 | 55.14 | 10.92 |
| w/o Cross-Domain | 65.08 | 61.79 | **5.14** |
| w/o Aggregation | 66.11 | 62.26 | 7.99 |
| **MT-SDPO** | **67.11** | **64.08** | 5.30 |

Per-domain numbers, SDPO and GRPO references are in the paper (Tables 1, 2 and 6).

## 🚀 Quick Start

### Installation

Python 3.12, `torch==2.8.0`, `vllm==0.11.0`, `transformers==4.57.1`. The trainer is a pinned [verl](https://github.com/volcengine/verl) fork carrying [SDPO](https://github.com/lasgroup/SDPO) and the MT-SDPO extensions; post-training uses [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory).

```bash
git clone https://github.com/hexixiang/MT-SDPO.git && cd MT-SDPO
pip install torch==2.8.0 --index-url https://download.pytorch.org/whl/cu128
pip install -r training/requirements.txt vllm==0.11.0 && pip install -e training
```

```
configs/sft/    LLaMA-Factory recipes (3 domain teachers + Multi-Domain PT) per backbone
data/           SciKnowEval-L3 splits, teacher-generated SFT data, online parquet, private-answer manifests
training/       verl fork with SDPO + MT-SDPO and all ablation controls
evaluation/     frozen avg@16 evaluator with guarded judge fallback
scripts/        one launcher per stage; paths are set in scripts/env.sh
```

### 1. Post-training

Train the three domain teachers and the Multi-Domain policy from the base model. The epoch-2 Multi-Domain checkpoint (`checkpoint-978`) initializes every online method.

```bash
for d in chemistry materials physics combined; do
  CUDA_VISIBLE_DEVICES=0 scripts/run_sft.sh configs/sft/qwen3_8b_full_sft_${d}.yaml
done
```

### 2. Serve teachers and build the private-answer manifest

Manifests for all five students already ship in `data/sciknoweval_l3/expert_manifests/`; rebuild only if you retrain the teachers.

```bash
EXPERT_GPUS=4,5,6 scripts/start_expert_servers.sh
scripts/build_expert_manifest.sh
```

### 3. Online training

```bash
scripts/train_online.sh mt_sdpo                                              # MT-SDPO
scripts/train_online.sh sdpo_sciknoweval_baseline                            # SDPO
scripts/train_online.sh mt_sdpo multi_expert.mode=domain_routed_unverified   # Domain Routing
scripts/train_online.sh mt_sdpo multi_expert.mode=all_unverified             # w/o Verification
scripts/train_online.sh mt_sdpo multi_expert.mode=domain_routed              # w/o Cross-Domain
scripts/train_online.sh single_valid                                         # w/o Aggregation
```

Extra arguments are Hydra overrides (e.g. `trainer.experiment_name=...`). Set `MT_SDPO_STUDENT` / `MT_SDPO_SFT_ROOT` in `scripts/env.sh` to switch backbones.

### 4. Evaluate

```bash
scripts/merge_checkpoint.sh mt-sdpo-qwen3-8b-ckpt978-step100 100
scripts/serve_eval_models.sh outputs/merged/mt-sdpo-qwen3-8b-ckpt978-step100 0 1
scripts/run_eval.sh mt_sdpo_step100 outputs/merged/mt-sdpo-qwen3-8b-ckpt978-step100
```

### Key settings

| | |
|:--|:--|
| Post-training | full-parameter, lr 1e-5, 3 epochs, batch 4, 8,192 context |
| Online | 32 prompts × 8 rollouts per update, 100 updates, lr 1e-5 |
| Distillation | student top-100 + tail, JSD, EMA τ = 0.05, IS clip 2.0 |
| Teacher feedback | incorrect rollouts only, ≤ 256 tokens, leakage-filtered |
| Evaluation | 79 questions / domain, avg@16, temperature 0.6, top-p 0.95 |

## 🙏 Acknowledgements

Built on [SDPO](https://github.com/lasgroup/SDPO), [verl](https://github.com/volcengine/verl), [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory), [vLLM](https://github.com/vllm-project/vllm) and the [SciKnowEval](https://github.com/HICAI-ZJU/SciKnowEval) benchmark.

## 📖 Citation

```bibtex
@article{he2026mtsdpo,
  title   = {Learn from Whoever Is Right: Answer-Verified Multi-Teacher Distillation for Multi-Domain LLMs},
  author  = {He, Xixiang and Li, Xingming and Wu, Baiqi and Sun, Qiyao and Ji, Xuanyu and Cheng, Ao and Hu, Qingyong},
  journal = {arXiv preprint arXiv:2609.02548},
  year    = {2026}
}
```

## 📄 License

[Apache License 2.0](LICENSE).

---

<div align="center">

[![Repo Visits](https://hits.sh/github.com/hexixiang/MT-SDPO.svg?label=Repo%20Visits&color=b31b1b&labelColor=555555)](https://hits.sh/github.com/hexixiang/MT-SDPO/)

</div>
