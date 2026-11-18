# PACE: Parity-Aware Compute Evaluation

**More Agents, More Samples, or More Thinking? Untangling Coordination, Ensembling, and Test-Time Compute in Multi-Agent LLMs**

**Author:** Seyed Mahmoud Sajjadi Mohammadabadi  
**Affiliation:** Department of Computer Science and Engineering, University of Nevada, Reno  
**Correspondence:** `mahmoud.sajjadi@unr.edu`  
**Repository:** [https://github.com/mahmoudsajjadi/pace](https://github.com/mahmoudsajjadi/pace)  
**arXiv Preprint:** [arXiv:2611.17610](https://arxiv.org/abs/2611.17610) ([HTML version](https://arxiv.org/html/2611.17610v1))  
**Paper PDF:** Preprint: [`manuscript/main.pdf`](manuscript/main.pdf) | Visual Cheatsheet: [`docs/assets/pace_cheatsheet.pdf`](docs/assets/pace_cheatsheet.pdf) | Interactive Studio: [`dist/hf_space_pace_studio/`](dist/hf_space_pace_studio/)

[![arXiv:2611.17610](https://img.shields.io/badge/arXiv-2611.17610-b31b1b.svg)](https://arxiv.org/abs/2611.17610)
[![Upvote on Hugging Face](https://img.shields.io/badge/🤗_Upvote_Paper-Hugging_Face_Daily_Papers-ffd21e.svg)](https://huggingface.co/papers/2611.17610)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Data: CC BY 4.0](https://img.shields.io/badge/Data-CC%20BY%204.0-lightgrey.svg)](zenodo_datasets.json)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://www.python.org/downloads/)
[![Test Suite: 1143 Passing](https://img.shields.io/badge/Tests-1143%20Passing-success.svg)](tests/)
[![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24286397.svg)](https://doi.org/10.5281/zenodo.24286397)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mahmoudsajjadi/pace/blob/main/notebooks/audit_your_log.ipynb)

**Reproducible on one consumer GPU.** The controlled experiments (`llama3.1:8b` served by Ollama, about 4.9 GB) run on a single 12 GB card (developed on an RTX 4070): `bash scripts/reproduce_12gb_gpu.sh` runs the tests, the hidden-profile file check and a 170-call smoke run, and records its own wall time (the expected runtimes in the script header are derived from a measured batch rate, not from a timed run of the script).

Official replication repository, audited contrast ledger (`9` primary studies, `516` unique multi-agent configurations from `531` raw extracted rows, `834` contrast records), `pace` CLI and evaluation toolkit (legacy aliases: `cme`, `mae-eval`), and zero-dependency browser workbench (**PACE Studio**) for Parity-Aware Compute Evaluation.

**Licences.** Code (`code/`, `analysis/`, `scripts/`, `tests/`): Apache-2.0 (`LICENSE`). Dataset files (extracted contrast tables and the hidden-profile task, staged in `zenodo_datasets.json`): CC-BY-4.0.

![PACE 60-second explainer](docs/assets/pace_explainer.gif)

---

## Abstract & Canonical Findings

Multi-agent language model evaluations often compare communicating systems against a single greedy pass, confounding inter-agent coordination with independent sampling and expanded test-time compute. We introduce **Parity-Aware Compute Evaluation (PACE)**, which classifies single-agent baselines on a four-category ladder (**Category A**: single greedy pass $k=1$; **Category B**: noncommunicating sampled baseline; **Category C**: resource-matched or shared-ceiling baseline; **Category D**: compute-cost Pareto frontier), audits a **resource vector with six dimensions**

$$\mathbf{R} = \langle R_{\text{reason}}, R_{\text{token}}, R_{\text{cost}}, R_{\text{lat}}, R_{\text{sample}}, R_{\text{sys}} \rangle,$$

enforces directional resource feasibility, and measures the frontier gap relative to single-agent self-consistency at parity in tokens.

### Extracted Corpus & Empirical Synthesis

- **Canonical Denominators:** From `12` studies considered across two stages (`5` initial studies and `7` screened candidates: `4` included, `3` excluded), the included corpus comprises **`9` primary studies**, **`516` unique multi-agent configurations** (`531` raw extracted rows minus `15` baseline-only rows), and **`834` baseline-specific contrast records** (`358` Category A, `360` Category B, `114` Category C, and `2` Category D Pareto contrasts; **`474` combined Category B/C contrasts** across `8` studies; **`156` shared-ceiling contrasts**; **`318` paired Category A/B contrasts** across **`72` unique baseline cells**).
- **Single-Pass vs. Compute-Controlled Categories:** Mean accuracy differences are **`-0.032`** against Category A (`358` contrasts; `-0.005` omitting Zhang et al., who supply `180` configurations), **`-0.051`** against Category B (`360` contrasts), and **`-0.012`** against Category C (`114` contrasts). Across combined Category B/C (`474` contrasts, `8` studies), the unweighted contrast mean is **`-0.042`**, with exploratory three-level REML log odds $\hat\beta = \mathbf{-0.195}$ (CR2 95% CI `[-0.323, -0.067]`; 95% study-mean prediction interval `[-0.515, +0.125]`).
- **Consistency Across Studies:** Multi-agent systems fail to lead in **`74%`** (`352` of `474`) of Category B/C contrasts, feasible baselines match or beat them in **`36%`** (`171` of `474` directionally feasible; `56` below `-1.96 SE`; `69%` or `356` of `516` unique configurations across Categories A/B/C), and **`8 of 9`** study means are nonpositive (sole positive exception: Wunderlich et al. at **`+0.020`** at stated configurations on MMLU-Pro, compute not matched).
- **Sampling Gap ($\Delta_{\text{gap}}$):** Across `5` dual-baseline studies (`318` pairs spanning `72` unique baseline cells, `64 of 72` negative), switching from greedy to sampled baselines lowers accuracy differences by **`-0.038`** weighted equally by study (**`-0.028`** across pairs; **`-0.036`** across the `72` unique cells; cell-level REML $\hat\beta = \mathbf{-0.178}$, CR2 95% CI `[-0.347, -0.009]`).
- **Controlled Open-Weight Experiment (`llama3.1:8b` via Ollama):**
  - **Shared-evidence MMLU-Pro (`n=250`):** Vanilla debate (`−0.015` frontier gap, `0.567` vs. `0.581` frontier) and Mixture-of-Agents (`−0.072` frontier gap) do not clear the equal-token self-consistency frontier under Holm correction.
  - **Complementary Hidden Profile split-view control (`n=200`):** Split-view debate exceeds the split-view independent-voting frontier (`+0.073` frontier gap, `0.182` vs. `0.109`, Holm-adjusted `p = 0.007`), while trailing content-mismatched placebo debate (`0.248`) and four-choice chance (`0.250`).

---

## Repository Structure

```text
├── .github/                   # CI workflows & study-contrast issue template (add_study_contrast.yml)
├── analysis/                  # Synthesis, REML pooling, plotting, and LaTeX build gates
│   ├── assemble_paper.py      # Assembles & compiles manuscript/main.pdf
│   ├── run_baseline_tiers.py  # Descriptive corpus synthesis, dual-baseline pairing & numbers.tex
│   └── run_k9_reml.py         # Three-level REML + CR2 inference (including 72-cell Model D)
├── code/
│   ├── pace/                  # Standalone PACE CLI, importers (incl. Inspect AI), & browser Studio
│   ├── cme/                   # Legacy CLI/API aliases preserved for backwards compatibility
│   └── mae_eval/              # Legacy resource tracker/auditor package aliases
├── dist/
│   ├── assets/                # Explainer GIF & cheatsheet (PNG/PDF)
│   ├── github_release_staging/# Offline-verified GitHub release staging tree
│   └── hf_space_pace_studio/  # Hugging Face Space workbench + corpus_contrasts.json (832 rows)
├── docs/                      # Project landing page (index.html), community playbook & visual assets
├── evidence/                  # Verified extracted CSVs, screening ledger & audit reports
│   ├── contrasts_anchor5_core.csv
│   ├── contrasts_dual_baseline.csv
│   ├── extension_contrasts.csv
│   └── verification_worksheet.csv
├── figures/                   # Publication vector PDF figures and PNG previews
├── manuscript/                # Modular LaTeX source of truth and generated macro files
├── notebooks/                 # Interactive Colab/Jupyter log-auditing notebook (audit_your_log.ipynb)
├── outputs/                   # Baseline contrast tables, REML JSON & experimental logs
├── paper/                     # Synchronized manuscript build targets and figure/table mirrors
├── pyproject.toml             # PEP 621 package metadata (`pace-eval`) & CLI entry points
├── review/                    # Programmatic concordance ledgers & claim-verification tables
├── scripts/                   # Reproducibility runner (12 GB GPU), corpus builders & exporters
├── supplement/                # Moderator synthesis, empirical trace harvest & author templates
└── tests/                     # Automated unit, regression, and concordance test suite
```

---

## Quickstart: the `pace` CLI & PACE Studio

Install `pace-eval` from the repository root (`pyproject.toml`) or from `code/`:

```bash
pip install -e .               # installs `pace` (plus legacy `cme` and `mae-eval` console aliases)
```

Core auditing, reporting, log import (including Inspect AI via `--format inspect`), and local GUI commands:

```bash
pace studio                    # launches the zero-dependency browser UI (PACE Studio)
pace classify --config sas.json
pace audit run_trace.jsonl
pace import-logs --format inspect --input eval_log.json --output trace.jsonl && pace audit trace.jsonl
pace report --pool pool.jsonl --logs run.jsonl --system debate --export-latex card.tex
pace dynamics debate_log.jsonl --null null.jsonl --json
pace inflate --samples pool.jsonl --k 1,3,5,9,16,24 --wrong-options auto   # beta-binomial sampling inflation (auto needs an answer label per row)
pace card run_trace.jsonl --latex --output pace-card.tex
```

Constructive planning, simulation, meta-analysis, frontier, and rebuttal commands:

```bash
pace pool-size --agents 5 --rounds 3 --prompt-tokens 100 --msg-tokens 20 --json
pace simulate --mode debate --items 100 --agents 5 --rounds 3 --out debate.jsonl
pace meta --contrasts outputs/baseline_tier_contrasts.csv --scale log_or --json
pace power --p-base .55 --delta .10 --n-items 40 --json
pace benchmark-gen --route clue_grid --out clues.jsonl
pace aggregate-open --input candidates.jsonl --metric token_jaccard --out centroids.jsonl
pace plot --kind phase --out phase.svg
pace hidden-profile --n 100 --out hp.jsonl
pace frontier --samples pool.jsonl --logs run.jsonl --out frontier.pdf
pace rebuttal --contrasts data/baseline_tier_contrasts.csv --export-markdown rebuttal.md
```

End-to-end synthetic walkthrough, interactive Colab notebook, GitHub Action CI workflow template, and community study-submission playbook live in:
- [`notebooks/audit_your_log.ipynb`](notebooks/audit_your_log.ipynb)
- [`code/examples/end_to_end_walkthrough.py`](code/examples/end_to_end_walkthrough.py)
- [`code/examples/github_action_pace_audit.yml`](code/examples/github_action_pace_audit.yml)
- [`docs/index.html`](docs/index.html), [`docs/COMMUNITY_AND_PR_PLAYBOOK.md`](docs/COMMUNITY_AND_PR_PLAYBOOK.md), and [`.github/ISSUE_TEMPLATE/add_study_contrast.yml`](.github/ISSUE_TEMPLATE/add_study_contrast.yml)
- Visual assets: [`docs/assets/pace_explainer.gif`](docs/assets/pace_explainer.gif), [`docs/assets/pace_cheatsheet.png`](docs/assets/pace_cheatsheet.png), and [`dist/assets/`](dist/assets/)

Legacy imports (`from cme ...` and `from mae_eval ...`) remain supported alongside `pace`.

---

## Reporting Standard: Evaluation Card & Progressive Levels

Every completed comparison should report:
1. **The seven-field PACE Evaluation Card:** Baseline rung (`A`–`D`), resource vector $\mathbf{R}$, token accounting (prompt, completion, cached vs. uncached tokens), MAS/SAS resource ratios, frontier gap with 95% paired bootstrap CI, evidence/route structure (`shared` vs. `split`, verifier availability, model heterogeneity), and per-item resource distribution and stopping rules.
2. **Three progressive reporting levels:**
<!-- README_SPEC:BEGIN -->

**Placebo condition (S7).** Each peer message is replaced by a sample from a different item, truncated or repeated to match the character length of the message it replaces; it is not token-matched (realized token ratios of S7: 0.978 against S4 on MMLU-Pro, prompt 0.906 and completion 1.130; 1.475 against S4v on Hidden Profile, prompt 1.389 and completion 1.674). The placebo is content-mismatched, not content-free.

**Reporting levels.**
- **`PACE-Minimum`:** Category B/C baseline (for example nested initial-round self-consistency voting), full token and call counts, and paired bootstrap accuracy intervals.
- **`PACE-Recommended`:** Equal-token self-consistency frontier curve, directional feasibility across all six dimensions of the resource vector, and placebo control or split-view checks.
- **`PACE-Extended`:** Per-item budget matching, cache-weighted billing accounting, adaptive stopping distributions, hybrid call-graph edge counts, and peer-influence transition dynamics.

**Release manifest.** 113 files listed in `RELEASE_MANIFEST.json` (mode: local-only-staging).

<!-- README_SPEC:END -->

---

## Verification & Manuscript Compilation

Run the full automated verification suite (`1058 passed, 0 failed`):

```bash
pytest -q tests/
```

Assemble and verify all PDF targets (`manuscript/main.pdf`, `paper/main.pdf`) with Build Gates 1 and 2:

```bash
python -I analysis/assemble_paper.py
```

---

## Citation

```bibtex
@article{sajjadi2026more,
  title   = {More Agents, More Samples, or More Thinking? Untangling Coordination, Ensembling, and Test-Time Compute in Multi-Agent LLMs},
  author  = {Sajjadi Mohammadabadi, Seyed Mahmoud},
  journal = {arXiv preprint arXiv:2611.17610},
  year    = {2026},
  eprint  = {2611.17610},
  archivePrefix = {arXiv},
  primaryClass  = {cs.AI},
  doi     = {10.48550/arXiv.2611.17610},
  url     = {https://arxiv.org/abs/2611.17610},
  note    = {Replication repository at https://github.com/mahmoudsajjadi/pace}
}
```
