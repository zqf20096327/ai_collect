<div align="center">

# NextUnit-Bench

### Moving Generality from Model to Modeler:<br>LLM Agents for PHM on a Deployment-Style Benchmark

**[Zhenling Chen](https://github.com/JialingRichard)**

Laboratoire Génie Industriel, CentraleSupélec, Université Paris-Saclay

[![arXiv](https://img.shields.io/badge/arXiv-2611.25252-b31b1b.svg)](https://arxiv.org/abs/2611.25252)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

</div>

**Tell your coding agent one sentence:**

```text
Read https://raw.githubusercontent.com/JialingRichard/nextunit-bench/v1.0/FIELD_MANUAL.md and follow it to set up NextUnit-Bench on this machine.
```

> [!NOTE]
> **Version 1.0**, identical to the paper. The agent you tell this sets the
> benchmark up and verifies it; it downloads the hidden units, so it must
> never be the agent under evaluation ([Rule 0](FIELD_MANUAL.md#rule-0-you-are-the-builder-not-the-subject)).

<p align="center">
  <img src="assets/teaser.png" width="60%" alt="NextUnit-Bench deployment-style evaluation">
</p>

<p align="center"><em>
Deployment-style evaluation. The agent sees the task description and the development units, works for two hours in a sandbox, and delivers a sealed, executable predictor. The evaluator runs it offline on each hidden unit; the hidden units, their labels, the scoring code, and the score itself remain invisible to the agent.
</em></p>

## Abstract

Coding agents built on large language models (LLMs) now help develop many models published as general solutions. Should generality instead reside in the agent that builds a model for each new task? We examine this question in prognostics and health management (PHM), where every model must work on unseen equipment. Our deployment-style benchmark, NextUnit-Bench, covers 24 public datasets split into 58 folds that hold out units or operating conditions; each agent has two hours to deliver an executable predictor, then run on the hidden units. First, frontier agents outperform AutoML, which reaches less than half the best agent's score, and faithful implementations of published methods on four datasets, of which only 6 of 30 beat the strongest agent's own design; published accuracies, where reproducible, rest on the papers' own conventions, and a single convention, capping the remaining life of test engines, can halve the reported error. Second, the agents' advantage is a design made on each machine's data; once made, a plain-text plan of a few hundred words carries most of the gap between two frontier agents, and given a weaker agent's plan, the strongest agent falls to that agent's level, often to identical predictions. Before touching the data, however, the gap between the two shrinks to about a third, and domain toolkits appear to help neither: what sets the strongest apart is how much it learns from the data. Third, such designs reach only implementers that can execute them: given the strongest agent's designs, a locally deployable open-weight model delivers half as often, even when they are lightened, and scores no higher than without them. Generality, we argue, is not disappearing but moving, from the model to the modeler.

## At a glance

- **24 public PHM datasets, 58 folds** that hold out units or operating conditions: bearings, batteries, turbofan engines, wind turbines, process plants, and more.
- **Deployment-style protocol:** the subject works for two hours on development units only, then delivers an executable predictor that is sealed and re-run offline on the hidden units.
- **Any modeler:** LLM agents, AutoML, published methods, or your own pipeline are scored by the same evaluator.
- **Agent-facing:** the benchmark is set up by an agent following a field manual; datasets are not redistributed but fetched from their original sources and verified by checksums.

## Main result

<p align="center">
  <img src="assets/fig2_scores_github.png" width="75%" alt="Score S over the 24 datasets for each method">
</p>

Score *S* over the 24 datasets: the share of the baseline's error that a
method removes, in %, with 95% intervals from a bootstrap over datasets
(Fig. 2 of the paper, with full model names). Frontier LLM agents (GPT-6
Astra, Kimi K3, DeepSeek V4.1-Flash, GPT-6 Luna) remove a third to nearly
half of the baseline's error; local open-weight agents (Gemma 4 26B-A4B,
Qwen3.6-35B-A3B), AutoML (even with generic features) and time-series
foundation models fine-tuned on each fold (MOMENT-1-base, Chronos-2) remain
below 20.

## The short version

The sentence at the top is all you need to type. The manual is written for
agents. It has them clone this repository (the `v1.0` tag), check the
machine and ask you before large downloads, then download, convert and
verify the data, and run the fixed evaluator. There is no setup wizard for
humans on purpose. If you have already cloned the repository, point your
agent to the local [`FIELD_MANUAL.md`](FIELD_MANUAL.md) instead. To evaluate
something afterwards, add: "then evaluate <your method or agent> with it".

> **Important.** The agent that sets up the benchmark downloads the hidden
> units and their labels. It must never be the agent under evaluation. Agents
> under evaluation run only inside the runner's sandbox, which shows them
> development data only. See FIELD_MANUAL.md, Rule 0.

## What the benchmark is

- 24 public PHM datasets in four task families (condition classification,
  remaining useful life, degradation and health estimation, anomaly detection
  and failure prediction).
- 58 folds that hold out units or operating conditions: whole units are held
  out, except in CWRU, SEU and HSF15 (UCI hydraulic), which have no
  independent units and hold out whole operating conditions; official splits
  are kept where they exist.
- An agent gets two hours of effective wall-clock time per fold and must
  deliver `artifact.py` with `predict(input_directory, output_file)`.
- The evaluator runs the sealed predictor offline, one fresh process per hidden
  unit, and compares predictions with labels outside the sandbox.
- Score per fold: `S = 100 * max(0, 1 - E/B)`, where `E` is the method's loss
  and `B` the loss of a fixed baseline (mean of a random forest and a 1-D CNN,
  published as a frozen 58-row table). Averaged over folds within a dataset,
  then equally over datasets.
- Two headline aggregates: **S24** over all 24 datasets, and **S_noshortcut**
  over the 21 datasets left after removing the three whose collection or
  preparation left a shortcut (AHU21, THREEW, CARE; see
  [`KNOWN_ISSUES.md`](KNOWN_ISSUES.md)).
  S_noshortcut is *not* the paper's "21 unit sets" column, which drops CWRU,
  SEU and HSF15 instead.

## What this repository contains, and what it does not

- Contains: the frozen benchmark definition (task descriptions, splits,
  hidden-unit lists, baseline table, checksums, reference scores), data
  acquisition and conversion scripts, the evaluator and scoring, the artifact
  specification, a self-check, a minimal agent runner, and the data and
  scripts behind the paper's figures.
- Does **not** contain any dataset. Each dataset is downloaded from its
  original source (or a documented mirror) and checked against SHA-256 hashes.
  Datasets keep their own licences; see [`docs/datasets.md`](docs/datasets.md).

## Requirements (summary)

- Linux x86_64 with unprivileged user namespaces (for `bwrap`) and, to run
  agents, `systemd-run --user`.
- Disk: about 90 GB of downloads, 85 GB of unpacked raw files and 89 GB of
  prepared data for all 24 datasets; about 8 GB for the two Python
  environments. Memory: 20 GB available (TEP's conversion).
- The pinned environments (`runtime/`: lock files and a container recipe).
  A GPU is optional.

## Results from the paper

Main runs of the paper (one run per agent, 58 folds), re-scored from their
stored predictions with this repository's evaluator; 95% intervals from a
bootstrap over datasets. Agents: GPT-6 Astra, Kimi K3, DeepSeek V4.1-Flash and
GPT-6 Luna through the Codex command-line agent; Qwen3.6-35B-A3B and Gemma 4
through OpenCode.

| Agent | S24 | S_noshortcut |
|---|---|---|
| Astra | 43.0 [32.4, 53.8] | 40.4 [29.4, 52.0] |
| Kimi | 39.7 [29.2, 51.0] | 38.4 [26.6, 50.7] |
| DeepSeek | 36.1 [25.7, 46.9] | 34.7 [24.2, 46.0] |
| Luna | 30.8 [19.4, 43.1] | 29.2 [17.5, 41.9] |
| Qwen3.6 | 14.3 [5.9, 24.8] | 14.4 [5.4, 25.7] |
| Gemma 4 | 16.5 [9.2, 25.4] | 16.7 [9.3, 25.5] |

`paper/tables/make_tables.py` regenerates this and the paper's other tables
from `paper/data/`; `paper/make_figures.py` the figures.

## Version

v1.0 is identical to the paper, including its known issues (documented, with
evidence, in `KNOWN_ISSUES.md`). Planned v1.1: corrected request construction
for THREEW. Scores from different versions are not comparable.

## Paper

Zhenling Chen, Zhiguo Zeng, and Anne Barros.
[*Moving Generality from Model to Modeler: LLM Agents for PHM on a Deployment-Style Benchmark.*](https://arxiv.org/abs/2611.25252)
arXiv:2611.25252 [cs.LG], 2026.

## Citation

If you use NextUnit-Bench, please cite the paper (also in
[`CITATION.cff`](CITATION.cff)), and the original publications of the
datasets you use ([`docs/datasets.md`](docs/datasets.md#citations)):

```bibtex
@misc{chen2026nextunit,
  title         = {Moving Generality from Model to Modeler: {LLM} Agents for {PHM} on a Deployment-Style Benchmark},
  author        = {Chen, Zhenling and Zeng, Zhiguo and Barros, Anne},
  year          = {2026},
  eprint        = {2611.25252},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url           = {https://arxiv.org/abs/2611.25252}
}
```

## Contact

Questions and issues: please open a GitHub issue or contact Zhenling Chen.

## License

- **Code** (Python, shell, container and configuration files, including the
  scripts in `paper/`): MIT ([`LICENSE`](LICENSE)).
- **Benchmark definition, documentation and figures**: everything under
  `nextunit/benchmark/` (task descriptions, splits, hidden-unit lists,
  baseline table, checksums, reference scores), everything under `docs/` and
  `assets/`, the Markdown files in the repository root, and the figures,
  tables and text in `paper/`: CC BY 4.0 ([`LICENSE-docs`](LICENSE-docs)).
- **Datasets**: not in this repository. Each keeps its original licence; two
  of them (Paderborn, MIMII DUE) are non-commercial. See
  [`docs/datasets.md`](docs/datasets.md).

## Known issues

See [`KNOWN_ISSUES.md`](KNOWN_ISSUES.md).
