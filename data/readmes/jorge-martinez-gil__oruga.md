<div align="center">

# ORUGA

### Optimizing Readability Using Genetic Algorithms

**Measurable, inspectable, and reproducible text simplification.**

[![CI](https://github.com/jorge-martinez-gil/oruga/actions/workflows/ci.yml/badge.svg)](https://github.com/jorge-martinez-gil/oruga/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-2EA44F.svg)](LICENSE)
[![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.knosys.2023.111273-5965E0.svg)](https://doi.org/10.1016/j.knosys.2023.111273)
[![Journal](https://img.shields.io/badge/Knowledge--Based_Systems-2024-F58220.svg)](https://www.sciencedirect.com/journal/knowledge-based-systems)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jorge-martinez-gil/oruga/blob/main/examples/oruga_colab_demo.ipynb)

[**Read the paper**](https://doi.org/10.1016/j.knosys.2023.111273)
· [**Explore examples**](examples/)
· [**Contribute**](CONTRIBUTING.md)

</div>

---

ORUGA is a citable Python framework for **semantics-preserving readability
optimization** and **text-simplification benchmarking**. It searches for word
replacements that lower a text's reading level while minimizing changes to its
meaning.

Use it as an inspectable simplification tool, a reproducible evolutionary NLP
baseline, or a shared evaluation harness for rule-based, transformer, and LLM
outputs.

> **No installation needed:** open the
> [interactive Colab notebook](https://colab.research.google.com/github/jorge-martinez-gil/oruga/blob/main/examples/oruga_colab_demo.ipynb)
> and run the demo in your browser.

## Why ORUGA?

| | What you get |
| :--- | :--- |
| **Measure** | Six readability metrics, including FKGL, SMOG, Coleman-Liau, ARI, Flesch, and Gunning Fog |
| **Optimize** | Genetic, swarm, and multi-objective algorithms with Pareto-front support |
| **Inspect** | Explicit synonym substitutions and measurable objective values |
| **Compare** | One evaluation layer for ORUGA and outputs from other simplification systems |
| **Reproduce** | Seeded runs, preserved paper scripts, tests, and scholarly metadata |
| **Start light** | A NumPy-only core; NLP and optimization backends are optional extras |

## Quickstart

### 1. Install

```bash
git clone https://github.com/jorge-martinez-gil/oruga.git
cd oruga
pip install -e ".[wordnet]"
python -m nltk.downloader wordnet omw-1.4
```

### 2. Optimize a passage

```python
from oruga import optimize

report = optimize(
    "The committee deliberated extensively regarding the ramifications "
    "of the proposed legislation.",
    provider="wordnet",
    optimizer="ga",
    metric="fkgl",
    modification=True,
    seed=0,
)

print(report.optimized_text)
print("FKGL:", report.metrics_before["fkgl"], "→", report.metrics_after["fkgl"])
```

### 3. Explore the result

Each run returns an `OptimizationReport` containing the original and optimized
text, before-and-after readability metrics, objective values, and—when using a
multi-objective optimizer—the candidate Pareto front.

For a zero-heavy-dependency example using the built-in dictionary and genetic
algorithm:

```bash
pip install -e .
python examples/quickstart.py
```

## How it works

```text
Input text
    │
    ▼
Synonym provider ──► Candidate representation
                           │
                           ▼
                  Readability objectives
                           │
                           ▼
                   Evolutionary search
                           │
                           ▼
             Optimized text + metrics + Pareto front
```

ORUGA models simplification as a combinatorial search problem. A provider
proposes valid substitutions, the objective layer scores each candidate, and an
optimizer searches for the best trade-off between readability, modification
rate, and semantic distance.

| Layer | Built-in choices |
| :--- | :--- |
| Synonym provider | `dictionary`, `wordnet`, `word2vec`, `web` |
| Readability metric | `fkgl`, `flesch`, `smog`, `coleman_liau`, `ari`, `gunning_fog` |
| Objective | Readability, modification rate, Jaccard distance, or Word Mover's Distance |
| Optimizer | `random`, `ga`, `jaya`, `cuckoo`, `tlbo`, `pygad`, `nsga2`, `gde3`, `smpso` |

## Command-line interface

```bash
# Optimize text directly
oruga optimize \
  --text "The committee deliberated extensively." \
  --provider wordnet \
  --optimizer ga \
  --metric fkgl \
  --modification \
  --seed 0

# Optimize a file using a reusable configuration
oruga optimize --config examples/config.example.yaml --file mydoc.txt --json

# Score a passage or inspect available components
oruga metrics --text "Score this passage."
oruga list
```

## Find your workflow

### Optimize a collection of documents

```python
from oruga import OrugaConfig, optimize_corpus

config = OrugaConfig(
    provider="wordnet",
    optimizer="nsga2",
    modification=True,
    seed=0,
)

with open("documents.txt") as stream:
    documents = [line.strip() for line in stream if line.strip()]

for report in optimize_corpus(documents, config=config):
    print(report.improvement("fkgl"), report.optimized_text)
```

### Benchmark another simplification method

Already have a rule-based system, transformer, LLM, or custom optimizer? Score
its output with the same metrics ORUGA uses:

```python
from oruga import readability

original = "The committee deliberated extensively regarding the ramifications."
simplified = my_method(original)

for metric in ("fkgl", "smog", "flesch"):
    before = readability.score(original, metric)
    after = readability.score(simplified, metric)
    print(f"{metric}: {before:.2f} → {after:.2f}")
```

To add a new search method to ORUGA itself, subclass
`oruga.optimizers.base.Optimizer` and register it. The optimizer will then work
with every provider, metric, and objective.

### Choose ORUGA or generative rewriting

| | ORUGA | Generative rewriting |
| :--- | :--- | :--- |
| Search space | Supplied synonym candidates | Open-ended generation |
| Training data | None required | Model-dependent |
| Target metric | Optimized directly | Usually controlled through prompting |
| Output | One solution or a Pareto front | Usually one rewrite |
| Changes | Every replacement is traceable | Changes may span the whole passage |
| Compute | CPU-friendly | Model-dependent |

The approaches are complementary: ORUGA can provide a controlled baseline and a
consistent metric layer for evaluating generative systems.

## Optional capabilities

The core installation requires only NumPy. Install extras only for the features
you need.

<details>
<summary><strong>Show optional dependency groups</strong></summary>

```bash
pip install -e ".[wordnet]"   # WordNet synonyms via NLTK
pip install -e ".[word2vec]"  # Word2Vec synonyms + Word Mover's Distance
pip install -e ".[web]"       # Web-thesaurus synonyms
pip install -e ".[jmetal]"    # NSGA-II, GDE3, and SMPSO
pip install -e ".[pygad]"     # Paper-faithful single-objective GA
pip install -e ".[grammar]"   # LanguageTool post-correction; requires Java
pip install -e ".[dev]"       # Tests and metric cross-validation
pip install -e ".[all]"       # Every optional capability
```

WordNet also requires a one-time corpus download:

```bash
python -m nltk.downloader wordnet omw-1.4
```

</details>

## Research and reproducibility

This repository is the official implementation of:

> Jorge Martinez-Gil. *Optimizing readability using genetic algorithms.*<br>
> Knowledge-Based Systems, 284:111273, 2024.
> [doi:10.1016/j.knosys.2023.111273](https://doi.org/10.1016/j.knosys.2023.111273)

The original experimental scripts remain available in [`legacy/`](legacy/README.md).
The modern engine expresses the same ideas through composable providers,
metrics, objectives, and optimizers.

<p align="center">
  <img src="example.png" width="620" alt="ORUGA research example showing an original passage, a Pareto front, and optimized text">
</p>

<details>
<summary><strong>Reproduce and validate the experiments</strong></summary>

Run the lightweight test suite and smoke checks:

```bash
pip install -e ".[dev]"
pytest -q
python examples/quickstart.py
oruga list
```

Run the paper-oriented workflow with the relevant backends:

```bash
pip install -e ".[wordnet,pygad,jmetal,word2vec]"
python -m nltk.downloader wordnet omw-1.4
python examples/reproduce_paper.py
```

Reproducibility metadata is provided through [`CITATION.cff`](CITATION.cff),
[`.zenodo.json`](.zenodo.json), and [`codemeta.json`](codemeta.json). Readability
metrics are implemented in pure Python and cross-validated against an
independent library in [`tests/test_readability.py`](tests/test_readability.py).

</details>

## Citation

If ORUGA supports your research, use GitHub's **Cite this repository** button or
copy the BibTeX below:

```bibtex
@article{martinez2024oruga,
  author  = {Jorge Martinez-Gil},
  title   = {Optimizing readability using genetic algorithms},
  journal = {Knowledge-Based Systems},
  volume  = {284},
  pages   = {111273},
  year    = {2024},
  issn    = {0950-7051},
  doi     = {10.1016/j.knosys.2023.111273}
}
```

## Contributing

Contributions are welcome—especially new synonym providers, optimizers,
metrics, datasets, and benchmarks. See the [contribution guide](CONTRIBUTING.md)
to get started.

## License

ORUGA is released under the [MIT License](LICENSE).

---

<div align="center">

**Make complex text easier to read—without making the process harder to trust.**

</div>
