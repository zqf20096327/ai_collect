<p align="center">
  <img src="assets/esgenius-logo.png" alt="ESGenius logo" width="132">
</p>

<h1 align="center">ESGenius</h1>

<p align="center">
  <strong>Benchmarking LLMs on Environmental, Social, and Governance (ESG) and Sustainability Knowledge</strong>
</p>

<p align="center">
  <strong>EMNLP 2025 Main Conference Oral</strong> |
  Resource and Theme Paper Award nominations, Top 1%
</p>

<p align="center">
  <a href="https://angel-ntu.github.io/ESGenius/">Project Site</a> |
  <a href="https://angel-ntu.github.io/ESGenius/heatmap.html">Interactive Heatmap</a> |
  <a href="https://huggingface.co/datasets/cy0307/ESGenius">Hugging Face Dataset</a> |
  <a href="https://aclanthology.org/2025.emnlp-main.739/">ACL Anthology</a> |
  <a href="https://aclanthology.org/2025.emnlp-main.739.pdf">PDF</a> |
  <a href="data/README.md">Dataset Card</a> |
  <a href="docs/evaluation.md">Evaluation Guide</a>
</p>

<p align="center">
  <a href="https://aclanthology.org/2025.emnlp-main.739/"><img alt="EMNLP 2025 Main Oral" src="https://img.shields.io/badge/EMNLP%202025-Main%20Oral-2f7d58"></a>
  <a href="https://angel-ntu.github.io/ESGenius/"><img alt="Project website" src="https://img.shields.io/badge/Website-GitHub%20Pages-366f8a"></a>
  <a href="https://huggingface.co/datasets/cy0307/ESGenius"><img alt="Hugging Face dataset" src="https://img.shields.io/badge/Hugging%20Face-Dataset-c78a2e"></a>
  <a href="https://angel-ntu.github.io/ESGenius/heatmap.html"><img alt="Model results" src="https://img.shields.io/badge/Models-50%20evaluated-12372f"></a>
  <a href="LICENSE"><img alt="License Apache 2.0" src="https://img.shields.io/badge/License-Apache--2.0-blue"></a>
</p>

---

ESGenius is an expert multiple-choice benchmark for evaluating whether large language models understand ESG and sustainability knowledge in standards-aware settings. It includes 1,136 source-grounded questions, plain and reference-aware dataset files, evaluation scripts, published result figures, and an interactive 50-model heatmap for question-level diagnosis.

## Quick Links

| Goal | Start here |
| --- | --- |
| Read the paper | [ACL Anthology](https://aclanthology.org/2025.emnlp-main.739/) or [PDF](https://aclanthology.org/2025.emnlp-main.739.pdf) |
| Open the project page | [angel-ntu.github.io/ESGenius](https://angel-ntu.github.io/ESGenius/) |
| Inspect model-question outcomes | [Interactive heatmap](https://angel-ntu.github.io/ESGenius/heatmap.html) |
| Use the Hugging Face release | [cy0307/ESGenius](https://huggingface.co/datasets/cy0307/ESGenius) |
| Download the plain benchmark | [`data/ESGenius_1136q.csv`](data/ESGenius_1136q.csv) or [`data/ESGenius_1136q.json`](data/ESGenius_1136q.json) |
| Use source-grounded references | [`data/ESGenius_w_ref_1136q.csv`](data/ESGenius_w_ref_1136q.csv) |
| Reproduce evaluations | [Evaluation guide](docs/evaluation.md) |
| Cite ESGenius | [BibTeX](#citation) or [CITATION.cff](CITATION.cff) |

## At a Glance

| Item | Details |
| --- | --- |
| Paper | ESGenius: Benchmarking LLMs on Environmental, Social, and Governance (ESG) and Sustainability Knowledge |
| Venue | EMNLP 2025 Main Conference Oral |
| Recognition | Resource and Theme Paper Award nominations, Top 1% |
| Questions | 1,136 multiple-choice ESG and sustainability questions |
| Answer protocol | `A`, `B`, `C`, `D`, plus `Z` for "Not sure" |
| Evaluated models | 50 models with aggregate rankings and question-level heatmap results |
| Reference support | Source document names, page references, and supporting excerpts |
| Hugging Face release | [`cy0307/ESGenius`](https://huggingface.co/datasets/cy0307/ESGenius) |
| License | Apache 2.0 |

## Why ESGenius?

General factual benchmarks do not fully capture the domain-specific demands of ESG work. Sustainability reporting, climate disclosure, and governance analysis require specialized terminology, source-dependent concepts, and knowledge of reporting frameworks. ESGenius targets this gap directly.

- Covers environmental, social, governance, and sustainability knowledge across major standards and disclosure contexts.
- Draws from IPCC, GRI, SASB, ISO, IFRS/ISSB, TCFD, CDP, and related ESG sources.
- Uses a controlled A-D multiple-choice format with `Z` for abstention or uncertainty.
- Provides source-grounded reference fields for audit, retrieval, and citation-aware evaluation.
- Includes reproducible evaluation scripts and published result artifacts.

## What Is Included

| Component | Purpose |
| --- | --- |
| Dataset | Plain CSV/JSON benchmark files and a reference-aware CSV |
| Evaluation code | Local Hugging Face, reference-aware prompting, and Dashscope-compatible Qwen API paths |
| Utilities | Shared prompt formatting, prediction parsing, metrics, and Excel export helpers |
| Results | Ranking figure, paper figures, and generated evaluation outputs |
| Webpage | Paper project site plus an interactive Plotly heatmap |
| Citation metadata | `CITATION.cff` and EMNLP 2025 BibTeX |

## Repository Layout

| Path | Purpose |
| --- | --- |
| [`index.html`](index.html) | GitHub Pages paper project site |
| [`heatmap.html`](heatmap.html) | Interactive 50-model model-question heatmap |
| [`assets/`](assets) | Site styles, JavaScript, and ESGenius logo |
| [`data/ESGenius_1136q.csv`](data/ESGenius_1136q.csv) | Plain benchmark in CSV format |
| [`data/ESGenius_1136q.json`](data/ESGenius_1136q.json) | Plain benchmark in JSON format |
| [`data/ESGenius_w_ref_1136q.csv`](data/ESGenius_w_ref_1136q.csv) | Reference-aware benchmark with source metadata |
| [`data/README.md`](data/README.md) | Dataset schema and usage notes |
| [`docs/evaluation.md`](docs/evaluation.md) | Detailed evaluation workflow guide |
| [`docs/huggingface_dataset_card.md`](docs/huggingface_dataset_card.md) | Source dataset card used for the Hugging Face release |
| [`evaluation_utils.py`](evaluation_utils.py) | Shared loading, prompting, parsing, metrics, and export utilities |
| [`eval_opensource.py`](eval_opensource.py) | Local Hugging Face model evaluation |
| [`eval_opensource_rag.py`](eval_opensource_rag.py) | Reference-aware prompting evaluation |
| [`eval_qwen_api.py`](eval_qwen_api.py) | Dashscope-compatible Qwen API evaluation |
| [`figures/`](figures) | Paper and website figures |
| [`results/`](results) | Published result images and evaluation outputs |
| [`CITATION.cff`](CITATION.cff) | Citation metadata |

## Hugging Face Release

The canonical public benchmark bundle is hosted at [cy0307/ESGenius](https://huggingface.co/datasets/cy0307/ESGenius). It contains the dataset files, dataset documentation, citation metadata, license, and lightweight evaluation scripts so users can download the benchmark from the Hugging Face Hub while using GitHub for source development and the project site.

```bash
hf download cy0307/ESGenius \
  --type dataset \
  --local-dir ESGenius-HF
```

## Dataset

The public dataset lives in [`data/`](data) and is mirrored on [Hugging Face](https://huggingface.co/datasets/cy0307/ESGenius). Use the plain files for standard model evaluation and the reference-aware file for audit or retrieval experiments.

| File | Use |
| --- | --- |
| [`ESGenius_1136q.csv`](data/ESGenius_1136q.csv) | Main CSV benchmark for standard evaluation |
| [`ESGenius_1136q.json`](data/ESGenius_1136q.json) | JSON mirror of the plain benchmark |
| [`ESGenius_w_ref_1136q.csv`](data/ESGenius_w_ref_1136q.csv) | Reference-aware version with `ref_page`, `ref_doc`, and `source_text` |

Core fields:

| Column | Description |
| --- | --- |
| `query_id` | Stable question identifier |
| `new_id` | Sequential question index |
| `query` | Multiple-choice question stem |
| `A`, `B`, `C`, `D` | Candidate answer options |
| `Z` | "Not sure" option |
| `answer` | Gold option label |
| `ref_page`, `ref_doc`, `source_text` | Reference metadata and excerpt in the reference CSV |

See [`data/README.md`](data/README.md) for schema notes and usage guidance.

## Quick Start

Create an environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Copy the environment template:

```bash
cp .env.example .env
```

Run a small local smoke test:

```bash
python eval_opensource.py \
  --dataset ESGenius_1136q.csv \
  --models Qwen/Qwen2.5-0.5B-Instruct \
  --limit 10
```

Results are written to `results/` as Excel workbooks with `summary` and `details` sheets.

## Evaluation Paths

All evaluation paths share normalization, option extraction, metric computation, and workbook export through [`evaluation_utils.py`](evaluation_utils.py).

| Path | Script | Typical use |
| --- | --- | --- |
| Local open-source models | [`eval_opensource.py`](eval_opensource.py) | Run Hugging Face causal language models locally |
| Reference-aware prompting | [`eval_opensource_rag.py`](eval_opensource_rag.py) | Prepend source snippets from the reference CSV |
| Qwen API | [`eval_qwen_api.py`](eval_qwen_api.py) | Evaluate Dashscope-compatible Qwen models with retry handling |

Reference-aware smoke test:

```bash
python eval_opensource_rag.py \
  --dataset ESGenius_w_ref_1136q.csv \
  --models Qwen/Qwen2.5-0.5B-Instruct \
  --limit 10
```

Qwen API smoke test:

```bash
python eval_qwen_api.py \
  --dataset ESGenius_1136q.csv \
  --models Qwen2.5-Max \
  --limit 10
```

For all options, output structure, and reproducibility notes, see [`docs/evaluation.md`](docs/evaluation.md).

## Results and Project Site

The project site follows a paper-project format and keeps the homepage lightweight. The full diagnostic view lives in the interactive heatmap.

- [Project homepage](https://angel-ntu.github.io/ESGenius/)
- [Interactive heatmap](https://angel-ntu.github.io/ESGenius/heatmap.html)
- [Hugging Face dataset](https://huggingface.co/datasets/cy0307/ESGenius)
- [ACL Anthology record](https://aclanthology.org/2025.emnlp-main.739/)

<p align="center">
  <img src="figures/main_results.png" alt="Main ESGenius benchmark results" width="760">
</p>

<p align="center">
  <em>Main ESGenius benchmark results. Additional figures are available in <code>figures/</code>, <code>results/</code>, and on the project site.</em>
</p>

Validate the static site locally:

```bash
python scripts/check_static_site.py
python -m http.server 8000
```

Then open `http://127.0.0.1:8000/`.

## Reproducibility Checklist

- Keep `query_id` as a string when loading datasets.
- Keep the `Z` option in prompts; it is part of the benchmark protocol.
- Use deterministic generation settings from [`evaluation_utils.py`](evaluation_utils.py).
- Existing result workbooks are skipped by default to avoid accidental overwrites.
- Use `--force` only when intentionally regenerating outputs.
- Report both accuracy and invalid or abstention behavior when comparing models.
- Use the reference-aware CSV when an experiment depends on source snippets.

## Citation

If you use ESGenius, please cite the EMNLP 2025 paper and repository metadata in [`CITATION.cff`](CITATION.cff).

```bibtex
@inproceedings{he-etal-2025-esgenius,
  title = "{ESG}enius: Benchmarking {LLM}s on Environmental, Social, and Governance ({ESG}) and Sustainability Knowledge",
  author = "He, Chaoyue and Zhou, Xin and Wu, Yi and Yu, Xinjia and Zhang, Yan and Zhang, Lei and Wang, Di and Lyu, Shengfei and Xu, Hong and Xiaoqiao, Wang and Liu, Wei and Miao, Chunyan",
  editor = "Christodoulopoulos, Christos and Chakraborty, Tanmoy and Rose, Carolyn and Peng, Violet",
  booktitle = "Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing",
  month = nov,
  year = "2025",
  address = "Suzhou, China",
  publisher = "Association for Computational Linguistics",
  url = "https://aclanthology.org/2025.emnlp-main.739/",
  doi = "10.18653/v1/2025.emnlp-main.739",
  pages = "14612--14653",
  ISBN = "979-8-89176-332-6"
}
```

## Contributing

Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for contribution guidance. For vulnerability reporting, see [`SECURITY.md`](SECURITY.md).

## License

This project is released under the [Apache 2.0 License](LICENSE).
