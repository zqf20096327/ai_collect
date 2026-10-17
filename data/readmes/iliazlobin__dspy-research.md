# DSPy Research

> Treating prompt engineering as a machine-learning problem — modular, trainable LLM pipelines built and optimized with [DSPy](https://github.com/stanfordnlp/dspy).

[![Python](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![DSPy](https://img.shields.io/badge/DSPy-pipelines-4B0082)](https://github.com/stanfordnlp/dspy)
[![Jupyter](https://img.shields.io/badge/Jupyter-notebooks-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Walkthrough](https://img.shields.io/badge/YouTube-walkthrough-FF0000?logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=NXI2l0wJNBY)

A hands-on exploration of **DSPy**, the Stanford framework that reframes LLM orchestration as a
machine-learning workflow: instead of hand-tuning brittle prompt strings, you declare *signatures*,
compose them into *modules*, and let DSPy's optimizers (teleprompters) compile the pipeline against a
dataset and a metric. This repo collects the notebooks, diagrams, and reference papers used to evaluate
that approach on real tasks — code generation/evaluation, company valuation, and multi-stage market
analysis.

📺 **Video walkthrough:** https://www.youtube.com/watch?v=NXI2l0wJNBY

---

## Why DSPy

Conventional prompt engineering is manual, brittle, and hard to reproduce or scale. DSPy turns the same
goals into an optimization problem:

- **Declarative signatures** — describe *what* a step should do (`question -> valuation, date, raised`),
  not the exact wording of the prompt.
- **Composable modules** — `Predict`, `ChainOfThought`, `ReAct`, retrieval (RAG) and custom modules snap
  together into larger programs.
- **Compilation / optimization** — teleprompters such as `BootstrapFewShot` and
  `BootstrapFewShotWithRandomSearch` automatically bootstrap demonstrations and tune the program against a
  training set and an evaluation metric.
- **Built-in evaluation** — `dspy.Evaluate` runs a program over a dev set and scores it, so improvements
  are measured, not guessed.

The payoff: fewer manual iterations, reproducible pipelines, and measurable score gains before vs. after
compilation.

---

## Notebooks

Each notebook is a self-contained experiment. They share a common setup — an OpenAI LM
(`gpt-3.5-turbo`) plus a [You.com](https://you.com) retriever (`YouRM`) for grounding — and progressively
introduce evaluation, RAG, and compilation.

| Notebook | What it demonstrates |
| --- | --- |
| [`notebooks/code-evaluation.ipynb`](notebooks/code-evaluation.ipynb) | End-to-end code-generation pipeline on the **HumanEval** dataset. Uses a typed `pydantic` signature to emit valid Python, runs generated code through a sandboxed REPL with a timeout, defines a pass/fail metric, evaluates with `dspy.Evaluate`, then **compiles** the program with `BootstrapFewShotWithRandomSearch` and re-scores it. Includes a worked detour through JSON-escaping pitfalls in LM output. |
| [`notebooks/company-valuation.ipynb`](notebooks/company-valuation.ipynb) | A **company-valuation** pipeline that retrieves funding facts and extracts structured fields (valuation, date, amount raised, round, VCs). Builds a custom `AssessValuation` LLM-as-judge metric, contrasts a plain `Predict` baseline against a **RAG** module, then compiles the RAG program with `BootstrapFewShot` to lift the score. |
| [`notebooks/market-analyst.ipynb`](notebooks/market-analyst.ipynb) | A **comparative market-analysis** module that compares two companies across valuation, headcount, founding year, and public perception — the building block for the multi-stage architecture below. |

Supporting code:

- [`notebooks/repl/code.py`](notebooks/repl/code.py) — a small process-isolated Python REPL
  (`execute_code`) with a timeout, used to safely run model-generated solutions.
- [`notebooks/code-samples.py`](notebooks/code-samples.py), [`notebooks/test.py`](notebooks/test.py) —
  scratch task/solution samples and a debug harness used while building the notebooks.

---

## System designs

The diagrams below trace the progression from a naive pipeline to a composed, compiled multi-stage system.

| | |
| --- | --- |
| ![Basic pipeline](images/system-design-1.png) | **1 · Basic company analysis (no compilation).** A straightforward declarative pipeline — inputs in, outputs out — with no automated optimization. The baseline. |
| ![Compiled pipeline](images/system-design-2.png) | **2 · Compiled & optimized company analysis.** The same pipeline after DSPy compilation: demonstrations and module parameters are tuned against a dataset and metric for better accuracy and efficiency. |
| ![Multi-stage pipeline](images/system-design-3.png) | **3 · Composable multi-stage pipeline.** A *Company Researcher* and *Market Analyst* are each compiled into reusable DSPy programs, wired together with fact retrieval, social-media (X) perspective, comparative analysis, and evaluator-based scoring. |

Additional reference diagrams (regular vs. compiled RAG, program composition) live in [`docs/`](docs/).

---

## Tech stack

- **Python 3.10**
- **[DSPy](https://github.com/stanfordnlp/dspy)** — signatures, modules (`Predict`, `ChainOfThought`,
  `ReAct`, RAG), teleprompters (`BootstrapFewShot`, `BootstrapFewShotWithRandomSearch`), and `Evaluate`.
- **OpenAI** (`gpt-3.5-turbo`) as the language model.
- **Retrieval:** [You.com](https://you.com) `YouRM` (Clarifai `ClarifaiRM` also wired up).
- **Datasets:** Hugging Face `datasets` (HumanEval; HotPotQA loader available).
- **`pydantic`** for typed signatures, **Jupyter** for the experiments.

---

## Repository layout

```
dspy-research/
├── notebooks/
│   ├── code-evaluation.ipynb      # HumanEval code-gen + evaluate + compile
│   ├── company-valuation.ipynb    # RAG valuation pipeline + LLM-judge metric + compile
│   ├── market-analyst.ipynb       # comparative two-company analysis module
│   ├── repl/code.py               # sandboxed code-execution REPL (timeout)
│   ├── code-samples.py            # scratch task/solution samples
│   └── test.py                    # debug harness
├── images/                        # system-design diagrams (1–3)
├── docs/                          # RAG / composition reference diagrams
├── papers/                        # the two foundational DSPy papers (PDF)
├── dspy.md                        # environment & install notes
└── .env.example                   # API-key template
```

---

## Getting started

> The notebooks call hosted APIs (OpenAI, You.com), so you'll need the corresponding keys.

```bash
git clone https://github.com/iliazlobin/dspy-research.git
cd dspy-research

# create an environment (conda or venv)
python -m venv .venv && source .venv/bin/activate

# DSPy and the data tooling used by the notebooks
pip install dspy datasets pydantic python-dotenv jupyter

# configure credentials
cp .env.example .env   # then fill in OPENAI_API_KEY, YDC_API_KEY, etc.

jupyter notebook notebooks/code-evaluation.ipynb
```

`.env.example` lists every key the notebooks expect:

```
YDC_API_KEY=          # You.com retriever
OPENAI_API_KEY=       # OpenAI LM
CLARIFAI_USER_ID=     # optional: Clarifai retriever
CLARIFAI_APP_ID=
CLARIFAI_PAT=
```

---

## Related papers

The foundational DSPy papers are mirrored in [`papers/`](papers/):

- [DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines](https://arxiv.org/abs/2310.03714)
- [DSPy Assertions: Computational Constraints for Self-Refining Language Model Pipelines](https://arxiv.org/abs/2312.13382)

---

## Links

- 📺 **Walkthrough:** https://www.youtube.com/watch?v=NXI2l0wJNBY
- 🧩 **DSPy:** https://github.com/stanfordnlp/dspy
- 🌐 **Portfolio:** https://iliazlobin.com/portfolio
- 👤 **Author:** Ilia Zlobin — Principal Software Engineer

## License

Released under the [MIT License](LICENSE).
