<div align="center">

<img src="book/assets/cover.png" alt="From First Line to First Paper — Book Cover" width="280" />

# From First Line to First Paper

### *Mastering Python, Statistical Data Science, and Applied Deep Learning*

**Mezanur Rahman Sharukh**  
*M.Sc. Statistician | Public Health & Machine Learning Researcher*  
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24446563.svg)](https://doi.org/10.5281/zenodo.24446563)
[![PyPI](https://img.shields.io/pypi/v/sharukh-tutor?color=0F5C6E&logo=pypi&logoColor=white)](https://pypi.org/project/sharukh-tutor/)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0006--8348--6123-A6CE39?style=flat&logo=orcid&logoColor=white)](https://orcid.org/0009-0006-8348-6123)
[![Release](https://img.shields.io/badge/Edition-1st%20(v1.0.2)-1B3B6F?style=flat)](https://github.com/sharukh01621/first-line-to-first-paper/releases/tag/v1.0.2)
[![Notebooks](https://img.shields.io/badge/Colab%20Notebooks-182%2F182%20PASS-0F5C6E?style=flat&logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/sharukh01621/first-line-to-first-paper/blob/main/colab_drive/00_START_HERE.ipynb)
[![Text License](https://img.shields.io/badge/Text-CC%20BY--NC--SA%204.0-B45309?style=flat)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Code License](https://img.shields.io/badge/Code-MIT-334155?style=flat)](https://opensource.org/licenses/MIT)

<br />

[**Read Web Book Online**](https://sharukh01621.github.io/first-line-to-first-paper/) &nbsp;|&nbsp;
[**Download PDF (860 pp)**](https://github.com/sharukh01621/first-line-to-first-paper/releases/download/v1.0.2/From-First-Line-to-First-Paper.pdf) &nbsp;|&nbsp;
[**Download EPUB 3**](https://github.com/sharukh01621/first-line-to-first-paper/releases/download/v1.0.2/From-First-Line-to-First-Paper.epub) &nbsp;|&nbsp;
[**Launch in Google Colab**](https://colab.research.google.com/github/sharukh01621/first-line-to-first-paper/blob/main/colab_drive/00_START_HERE.ipynb) &nbsp;|&nbsp;
[**Google Drive Mirror**](https://drive.google.com/drive/folders/1pHBCVND-bRsPV4FarRPqOmivYkVmRFBF?usp=drive_link)

</div>

---

## About the Book

***From First Line to First Paper*** is an **860-page, 36-chapter** zero-to-researcher textbook paired **1-to-1** with **182 interactive Google Colab notebooks**, **324 automated diagnostic checks**, and **972 three-tier progressive hints** powered by [`sharukh-tutor`](sharukh_tutor/).

Designed with **zero prior coding prerequisites**, the book guides quantitative students, biostatisticians, public health researchers, and aspiring ML/DL scientists from their very first `print()` statement all the way to leakage-free Scikit-Learn pipelines, PyTorch neural architectures (MLPs, CNNs, GRUs/LSTMs, Multi-Head Self-Attention & LoRA), multi-seed ablation studies, subgroup fairness & calibration audits, Decision Curve Analysis, and cryptographically verified (`SHA-256`) research release artifacts.

### What Makes This Curriculum Different
- **Every Chapter Follows an 8-Stage Mastery Arc:** First-Principles Intuition $\rightarrow$ Visual Mental Model $\rightarrow$ Line-by-Line Walkthrough & "Break It On Purpose" Error Labs $\rightarrow$ 4-Step Problem-Structuring Blueprint $\rightarrow$ Guided To-Dos $\rightarrow$ Paper Trace Test $\rightarrow$ 100-Point Coding Exam $\rightarrow$ Annotated Solutions & Debugging Post-Mortem.
- **Real-World Public Health Spine Datasets:** Every concept is anchored in realistic, programmatically generated public health & epidemiology datasets (`clinic_triage.csv`, `mch_survey_sample.csv`, `epi_surveillance.csv`) with real survey quirks (sentinel `999` values, mixed casing, DHS cluster IDs, and seasonal outbreak dynamics).
- **100% Zero-Drift Verified:** Every walkthrough, guided to-do, coding exam, and annotated solution notebook is executed and verified end-to-end against Python 3.12, NumPy 2.5, Pandas 3.1, SciPy 1.18, Statsmodels 0.15, Scikit-Learn 1.9, and PyTorch 2.15.

---

## Quick Start for Learners (Takes 2 Minutes)

1. **Read Online or Download:** Open the [Interactive Web Companion](https://sharukh01621.github.io/first-line-to-first-paper/), download the [860-Page Print PDF](https://github.com/sharukh01621/first-line-to-first-paper/releases/download/v1.0.2/From-First-Line-to-First-Paper.pdf), or load the [EPUB 3 E-Book](https://github.com/sharukh01621/first-line-to-first-paper/releases/download/v1.0.2/From-First-Line-to-First-Paper.epub) on your tablet/e-reader.
2. **Open the Orientation Lab:** Launch [`00_colab_orientation.ipynb`](https://colab.research.google.com/github/sharukh01621/first-line-to-first-paper/blob/main/colab_drive/00_setup/00_colab_orientation.ipynb) in Google Colab, click **File $\rightarrow$ Save a copy in Drive**, and run its welcome cells.
3. **Learn Interactively with `sharukh-tutor`:** Every chapter has three student notebooks (`01_walkthrough.ipynb`, `02_guided_todos.ipynb`, `03_coding_exam.ipynb`) plus complete annotated solutions under `colab_drive/solutions/`. Stuck on an exercise? Call `tutor.hint("ch01_todo_01", level=1)` (up to level 3) and verify your work with `tutor.check(...)` or `tutor.check_exam(...)`.

---

## Complete 7-Part Curriculum Roadmap (36 Chapters + 5 Appendices)

| Part | Chapters | Core Mastery Milestone | Interactive Labs |
| :--- | :---: | :--- | :---: |
| **Part I** | Ch 1–6 | Computational Thinking & Python from Absolute Zero | 18 student + 12 solution |
| **Part II** | Ch 7–11 | Core Data Structures, File I/O, Testing & Algorithms | 15 student + 10 solution |
| **Part III** | Ch 12–15 | OOP for ML, Jupyter/Colab Engineering, VS Code & Git | 12 student + 8 solution |
| **Part IV** | Ch 16–20 | NumPy, Pandas 3.x, Survey Cleaning, Visualization & Biostatistics | 15 student + 10 solution |
| **Part V** | Ch 21–26 | Classical ML — Leakage, Regularization, Calibration, Trees, PCA & Nested CV | 18 student + 12 solution |
| **Part VI** | Ch 27–32 | Deep Learning — NumPy Backprop, PyTorch, Training Dynamics, CNNs, RNNs & Transformers/LoRA | 18 student + 12 solution |
| **Part VII** | Ch 33–36 | Reproducible Experiments, Ablations, Fairness Audits, Model Cards, TRIPOD+AI & Flagship Paper Capstone | 12 student + 8 solution |
| **Appendices** | A–E | Master Cheat Sheets, Math Refresher, Top-50 Error Decoder, Master Colab Index, Bibliography, 40-Term Glossary & Author Bio | Master Index + Onboarding Hub |

---

## Repository Architecture (Single Source of Truth)

```text
first-line-to-first-paper/
├── book/                    # Quarto Book manuscript (42 .qmd files, cover, XeLaTeX & EPUB themes)
├── master_notebooks/        # Authoring source notebooks (solutions + cell markers)
├── colab_drive/             # Generated student + solution .ipynb notebooks (182 verified) & datasets
├── sharukh_tutor/           # Companion Python tutor package (324 checks, 972 hints, dataset loader)
├── scripts/                 # Zero-drift build, QA verification, QR generator & Google Drive sync
├── config/                  # Book metadata & Colab URL manifest
└── CITATION.cff             # Native GitHub citation metadata
```

---

## Local Build & Verification Pipeline

```bash
# 1. Run full zero-drift notebook build, QR generation & 182-notebook QA verification
python3 scripts/run_pipeline.py

# 2. Render Print PDF (XeLaTeX), EPUB 3, and HTML Web Companion via Quarto
quarto render book/

# 3. Mirror colab_drive/ + compiled PDF & EPUB to Google Drive (rclone)
python3 scripts/sync_drive.py
```

---

## Cite This Book

```bibtex
@book{sharukh2026firstline,
  author    = {Sharukh, Mezanur Rahman},
  title     = {From First Line to First Paper: Mastering Python,
               Statistical Data Science, and Applied Deep Learning},
  edition   = {1st},
  year      = {2026},
  publisher = {Open Scientific Edition / Zenodo},
  doi       = {10.5281/zenodo.24446563},
  url       = {https://doi.org/10.5281/zenodo.24446563}
}
```

## License & Contact

- **Narrative Text & Original Figures:** [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
- **Code, Jupyter Notebooks & `sharukh-tutor`:** [MIT License](https://opensource.org/licenses/MIT)
- **Author:** Mezanur Rahman Sharukh — [ORCID](https://orcid.org/0009-0006-8348-6123) | `shahrukh01621@gmail.com`
