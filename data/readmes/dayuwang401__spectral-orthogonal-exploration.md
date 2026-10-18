# Student Guides Teacher: Weak-to-Strong Inference via Spectral Orthogonal Exploration (SOE)

<p align="center">
  <a href="https://2026.aclweb.org/"><img src="https://img.shields.io/badge/ACL%202026-Oral-b31b1b.svg" alt="ACL 2026 Oral"></a>
  <a href="https://aclanthology.org/2026.acl-long.761.pdf"><img src="https://img.shields.io/badge/Paper-ACL%20Anthology-blue.svg" alt="Paper"></a>
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue.svg" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/PyTorch-2.0%2B-ee4c2c.svg" alt="PyTorch 2.0+">
  <img src="https://img.shields.io/badge/vLLM-enabled-4b8bbe.svg" alt="vLLM">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT">
</p>

> **Official implementation of the ACL 2026 (Oral) paper:**
> **"Student Guides Teacher: Weak-to-Strong Inference via Spectral Orthogonal Exploration"**
> Dayu Wang, Jiaye Yang, Weikang Li, Jiahui Liang, Yang Li, Deguo Xia, Jizhou Huang — *Baidu Inc. & Nanyang Technological University*
>
> 📄 **Paper:** [ACL 2026, Long Papers, pp. 16716–16733](https://aclanthology.org/2026.acl-long.761.pdf)

**Spectral Orthogonal Exploration (SOE)** is a **training-free, inference-time (test-time scaling)** framework that mitigates **Reasoning Collapse** in Large Language Model (LLM) mathematical reasoning. Under a **"Student Guides Teacher" (weak-to-strong)** paradigm, a *weaker* Student model acts as an **orthogonal probe** that ejects a *stronger* Teacher model out of its low-rank **bias manifold**, restoring genuine semantic exploration and dramatically improving both accuracy and sampling efficiency.

<p align="center">
  <img src="assets/motivation.png" width="88%" alt="Reasoning Collapse vs. Spectral Orthogonal Exploration">
  <br>
  <em>Baseline sampling collapses into a narrow, repetitive region of the action space (top). SOE injects an orthogonal probe to re-diversify the search space and recover high-quality solutions (bottom).</em>
</p>

---

## 🔎 Keywords / Topics

`Large Language Models` · `LLM reasoning` · `test-time scaling` · `inference-time scaling` · `reasoning collapse` · `mathematical reasoning` · `chain-of-thought` · `weak-to-strong generalization` · `self-consistency` · `best-of-N` · `spectral methods` · `orthogonal exploration` · `null space` · `SVD` · `exploration-exploitation` · `decoding strategies` · `AIME` · `MATH-500` · `OlympiadBench` · `Omni-Math` · `Qwen3` · `Gemma-3` · `vLLM`

> If you found this work through an LLM/literature search for **test-time scaling**, **reasoning collapse**, or **weak-to-strong inference**, this is the official code for **SOE (Wang et al., ACL 2026)**. See [Citation](#-citation).

---

## 🚀 Overview

LLMs exhibit a paradox on hard reasoning tasks: repeated stochastic sampling tends to produce **lexical variations of the same erroneous logic** rather than genuinely new reasoning — a phenomenon we call **Reasoning Collapse**. We show that failed traces are associated with a **low-rank bias manifold** in the model's hidden-state geometry, which suppresses exploration toward corrective solution directions.

**SOE** addresses this with a geometric intervention:
- Instead of using a weak auxiliary model for *imitation*, SOE uses it as an **orthogonal probe**.
- The probe injects **semantically heterogeneous** reasoning signals into the **orthogonal complement** (null space) of the Teacher's dominant subspace.
- This steers the Teacher toward diverse trajectories and improves exploration far beyond standard sampling.

**Results (Pass@16, difficult subset):** SOE improves **average accuracy by +62.4%** and **average sampling efficiency by +113.7%** over strong baselines, with consistent gains on logic and code generation as well.

---

## 🧩 Method: The SOE Pipeline

<p align="center">
  <img src="assets/pipeline.png" width="92%" alt="SOE Pipeline">
  <br>
  <em>The three phases of Spectral Orthogonal Exploration.</em>
</p>

SOE operates in three phases at inference time:

1. **Phase I — Greedy Trace & Monitoring.** The Teacher (π<sub>θ</sub>) generates a greedy reasoning trace; candidate *collapse points* are monitored and the trace is truncated at critical reasoning steps.
2. **Phase II — Micro-SVD & Probe Selection (core mechanism).** At each truncation point, Monte-Carlo look-ahead samples from the Teacher estimate the local **bias manifold** via **Micro-SVD**. The weaker **Student (π<sub>φ</sub>)** generates `L` candidate probes; we compute the **Orthogonal Projection Residual** of each probe against the Teacher's dominant subspace and select the most orthogonal probe `s*`.
3. **Phase III — Ejection & Resumption.** The chosen orthogonal probe is *stitched* into the context, and the Teacher resumes reasoning on fresh, geometrically diverse paths.

**Efficient spectral estimation.** Computing eigenvectors of the covariance `Ĉ ∈ ℝ^{d×d}` directly is prohibitive. We exploit SVD duality by forming the Gram matrix `G = HᵀH ∈ ℝ^{N×N}` over `N` Monte-Carlo samples and solving the smaller eigenproblem `G vₖ = λₖ vₖ` to recover the principal components (see `utils.py::get_subspace_basis` and `compute_orthogonality_score`).

---

## 📊 Main Results

**Pass@16 accuracy on the Difficult Subset** (problems where the Teacher's greedy decoding failed). Teacher: **Qwen3-4B-Instruct-2507**; Student: **Gemma-3-4B-IT**.

- **AIME 2024:** Baseline 38.5% → **SOE 76.9%** (**+99.7%**)
- **AIME 2025:** Baseline 35.3% → **SOE 70.6%** (**+100.0%**)
- **MATH-500:** Baseline 33.7% → **SOE 45.9%** (**+36.2%**)
- **OlympiadBench:** Baseline 11.7% → **SOE 15.5%** (**+32.5%**)
- **Omni-Math (Hard):** Baseline 14.5% → **SOE 20.8%** (**+43.4%**)
- **Average:** Baseline 26.7% → **SOE 45.9%** (**+62.4%**)

<p align="center">
  <img src="assets/efficiency.png" width="92%" alt="Sampling efficiency across benchmarks">
  <br>
  <em>Distinct correct solutions vs. compute budget (tokens). SOE (red) reaches more distinct correct solutions far faster than the baseline (blue), for an average <b>+113.7%</b> sampling-efficiency gain.</em>
</p>

---

## 🛠️ Installation

**Requirements:** Python 3.10+, PyTorch 2.0+, and a CUDA-capable GPU (multi-GPU supported for Step 3).

```bash
git clone https://github.com/dayuwang401/spectral-orthogonal-exploration.git
cd spectral-orthogonal-exploration
pip install -r requirements.txt
```

Dependencies (`requirements.txt`): `torch`, `vllm`, `transformers`, `numpy`, `tqdm`, `accelerate`, `ray`.
Step 3 additionally benefits from `flash-attention-2` (`attn_implementation="flash_attention_2"`).

### Models & Data

- **Models:** download the **Teacher** (e.g., `Qwen3-4B-Instruct-2507`) and **Student** (e.g., `Gemma-3-4B-IT`) from Hugging Face. The Student's *different architecture / training data* is important — it ensures its bias manifold is not aligned with the Teacher's.
- **Data:** place evaluation datasets (e.g., AIME, MATH-500, OlympiadBench, Omni-Math) as `.jsonl`, one problem per line, with `problem` and `answer` fields.

---

## ⚡ Quick Start

The pipeline runs as four sequential steps.

### Step 1 — Baseline Generation (Greedy)
Generate greedy reasoning traces from the Teacher to identify failure cases.
```bash
python step1_baseline_gen.py \
    --model_path /path/to/teacher-model \
    --data_path ./data/test_data.jsonl \
    --output_path ./results/step1_baseline.jsonl \
    --max_tokens 1024 \
    --tensor_parallel_size 1
```

### Step 2 — Filter Failures
Extract the trajectories where the Teacher was incorrect (`is_correct == false`) to target for intervention.
```bash
python step2_filter_error.py \
    --input_file ./results/step1_baseline.jsonl \
    --output_file ./results/step2_failures.jsonl
```

### Step 3 — Spectral Orthogonal Exploration (Intervention)
Core mechanism: estimate the Teacher's bias manifold (Micro-SVD), generate Student probes, and stitch the most orthogonal probe into the context. Runs data-parallel across all visible GPUs.
```bash
python step3_soe_intervention.py \
    --teacher_path /path/to/teacher-model \
    --student_path /path/to/student-model \
    --input_file ./results/step2_failures.jsonl \
    --output_file ./results/step3_intervened.jsonl \
    --num_samples 8 \
    --max_new_tokens 8 \
    --batch_size 32
```

### Step 4 — Final Evaluation
The Teacher resumes reasoning from the stitched context; we evaluate final accuracy.
```bash
python step4_evaluate.py \
    --model_path /path/to/teacher-model \
    --data_path ./results/step3_intervened.jsonl \
    --output_path ./results/step4_final_results.jsonl \
    --n_samples 1 \
    --temperature 0.7
```

---

## 📁 Repository Structure

```
spectral-orthogonal-exploration/
├── step1_baseline_gen.py      # Step 1: Teacher greedy baseline generation (vLLM)
├── step2_filter_error.py      # Step 2: filter incorrect traces
├── step3_soe_intervention.py  # Step 3: Micro-SVD + orthogonal probe selection (core)
├── step4_evaluate.py          # Step 4: final evaluation of stitched trajectories
├── utils.py                   # Math answer normalization, boxed extraction, SVD utilities
├── requirements.txt
└── assets/                    # Figures used in this README
```

---

## 📝 Citation

If you use SOE or find this work useful, please cite:

```bibtex
@inproceedings{wang2026student,
  title={Student Guides Teacher: Weak-to-Strong Inference via Spectral Orthogonal Exploration},
  author={Wang, Dayu and Yang, Jiaye and Li, Weigang and Liang, Jiahui and Li, Yang and Xia, Deguo and Huang, Jizhou},
  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages={16716--16733},
  year={2026}
}
```

## 📬 Contact

For questions about the paper or code, please open an issue or contact the corresponding authors (Baidu Inc. / Nanyang Technological University).

## 📄 License

Released under the [MIT License](LICENSE).
