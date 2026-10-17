# RepoProbe

**Can an LLM explain how a codebase actually works — not just patch it?**

[![arXiv](https://img.shields.io/badge/arXiv-2608.04783-b31b1b.svg)](https://arxiv.org/abs/2608.04783)
[![Paper](https://img.shields.io/badge/venue-ASE%202026-4b5563.svg)](https://conf.researchr.org/home/ase-2026)
[![License](https://img.shields.io/badge/code-Apache--2.0-blue.svg)](./LICENSE)
[![Data License](https://img.shields.io/badge/data-CC%20BY%204.0-lightgrey.svg)](./dataset/LICENSE)
[![Python](https://img.shields.io/badge/python-3.11%2B-3776ab.svg)](https://www.python.org/)

Evaluation code and benchmark data for the paper:

> **RepoProbe: Benchmarking Architecture-Aware Repository Comprehension with Checklists**
> *41st IEEE/ACM International Conference on Automated Software Engineering (ASE 2026)*
> Munich, Germany, October 12–16, 2026
> [arXiv:2608.04783](https://arxiv.org/abs/2608.04783)

RepoProbe is a discussion-based benchmark for repository-level code understanding. Unlike
defect-centric benchmarks that supply strong localisation cues (stack traces, error logs,
filenames) and thereby let models shortcut genuine comprehension, RepoProbe draws its
questions from real **GitHub Discussions** — open-ended architectural inquiries about how a
codebase actually works.

Answers are graded by a **Checklist-Based Verification Protocol** that decomposes each
open-ended response into atomic, weighted, verifiable technical facts, replacing opaque
scalar LLM-as-a-Judge ratings with objective item-level verification.

## At a Glance

| | |
|---|---|
| Repositories | 50 |
| Questions | 500 (3–30 per repository, median 8) |
| Programming languages | 15 |
| Question categories | Project Architecture / Business Logic / Implementation Details |
| Grading | Weighted checklist items with tiered rubrics, scored by an LLM judge |
| Agent scaffolding | Docker-isolated, identical for every model under test |
| Models evaluated in the paper | 20 (13 closed-weight, 7 open-weight) |

## Key Results

Each answer is worth 10 points: 9 for **knowledge** items (factual and technical correctness)
and 1 for a **clarity** item (explanation quality). *Overall Performance* is the mean of the
total over 10, *Perfect Solve Rate* the fraction of questions scoring a full 10/10. All values
are percentages; the full table of 20 models is in the paper.

| Model | Overall | Knowledge | Clarity | Perfect Solve |
|---|---|---|---|---|
| GPT-5.2 | **62.7** | **60.3** | 84.7 | 26.0 |
| Claude Opus 4.6 | 62.1 | 60.2 | 79.0 | **27.5** |
| GPT-5.4 | 60.4 | 57.6 | **85.6** | 24.2 |
| Claude Sonnet 4.6 | 60.2 | 58.3 | 78.2 | 27.2 |
| GLM-5 *(best open-weight)* | 54.8 | 52.9 | 72.2 | 21.3 |

Two findings drive the benchmark's design:

- **Fluency outruns correctness.** Every model scores far higher on clarity than on knowledge
  — GPT-5.2 reaches 84.7 clarity against 60.3 knowledge. Answers read as authoritative while
  the technical substance lags, which is precisely what scalar LLM-as-a-Judge scoring tends to
  reward.
- **Full credit is rare.** The best Perfect Solve Rate is 27.5%, so roughly three out of four
  questions leave at least one checklist item unmet even for frontier models. Repository-level
  comprehension is far from saturated.

## Repository Structure

```
.
├── README.md                            # This file
├── LICENSE                              # Apache-2.0, applies to source code
├── NOTICE                               # Copyright and licensing summary
├── CITATION.cff                         # Citation metadata
├── repos_info.json                      # Metadata and snapshot info for all 50 repositories
├── requirements.txt                     # Python dependencies
├── dataset/                             # Benchmark Q&A data (one CSV per repository)
│   ├── LICENSE                          # CC BY 4.0, applies to benchmark data
│   ├── NOTICE                           # Scope of the data licence and provenance
│   ├── adk-python.csv
│   ├── ...                              # 50 CSV files
│   └── yasb.csv
├── docs/
│   └── AGENT_INTEGRATION.md             # How to plug your own agent scaffolding in
├── candidate_repos/                     # (Runtime, git-ignored) Cloned repositories
├── scripts_agent/                       # Shell entrypoints
│   ├── fetch_repos.sh                   # Clone/update repos and generate repomix summaries
│   └── eval_models_multi_repo.sh        # Run agent-based evaluation across all repos
├── evaluator.py                         # Main evaluation orchestrator (Docker-based agent runner)
├── scorer.py                            # Checklist-based scoring via LLM judge
├── cache.py                             # Caching layer for agent answers and scores
├── dataset_loader.py                    # CSV dataset loader
├── fetch_repos.py                       # Repository cloning and repomix generation
├── prompt_templates_en.py               # Scoring prompt templates
└── agent_configs/                       # Docker container and agent runtime configuration
    ├── Dockerfile.base                  # Base image (Python, Node.js)
    ├── Dockerfile                       # Per-repo image (copies repo + configs)
    ├── build_base_image.sh              # Script to build the base Docker image
    ├── agent.json                       # Declares how to launch the agent under evaluation
    ├── example_agent.py                 # Reference agent scaffolding, replaceable
    ├── gateway.py                       # In-container OpenAI-compatible model gateway
    ├── gateway.sh                       # Gateway startup script
    └── model_client.py                  # OpenAI-compatible API client
```

## Dataset Format

Each CSV file in `dataset/` corresponds to one repository. Columns:

| Column | Description |
|---|---|
| `repo_name` | Short name of the source repository (matches the CSV filename) |
| `question_id` | Stable identifier, formatted as `<repo>-<index>` |
| `discussion_id` | GitHub Discussion node ID, for tracing back to the original thread |
| `taxonomy` | Code-understanding category: Project Architecture / Business Logic / Implementation Details |
| `difficulty` | Difficulty level |
| `question` | The question, derived from a GitHub Discussion |
| `answer` | Reference answer from the discussion maintainer |
| `checklist` | Weighted checklist items with tiered scoring rubrics |

A `checklist` entry looks like this — each item carries a point value and tiered criteria,
so partial credit is awarded explicitly rather than inferred by the judge:

```
(3 points) Bug Fix Confirmation and Commit Identification
- 3 points: Correctly confirms the fix is present in 8.0.2 and identifies the commit hash
- 1 point: Confirms the fix exists but does not provide the correct commit
- 0 points: Fails to confirm, or asserts the bug is unfixed
```

## Prerequisites

- Python 3.11+
- Docker
- Node.js 20+ (for `repomix`)
- An OpenAI-compatible API endpoint and key

## Agent Scaffolding

RepoProbe evaluates agents rather than raw model APIs: each question is answered by an agent
that explores the repository before responding. The harness is scaffolding-agnostic — it
defines a container contract (repository at `/app/repo`, question at `/tmp/prompt/prompt.txt`,
answer on stdout) and launches whatever `agent_configs/agent.json` declares. Bring your own
loop, an open-source framework or a vendor CLI without modifying the harness.

A minimal reference agent, `agent_configs/example_agent.py`, is wired up by default so the
benchmark runs out of the box. See [`docs/AGENT_INTEGRATION.md`](./docs/AGENT_INTEGRATION.md)
for the full contract.

Scores are comparable only across models evaluated under the *same* scaffolding, since tool
availability and turn budget change how much of a repository a model actually inspects. The
experiments in the paper used the scaffolding described there, which is not redistributed
here.

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Build the base Docker image

```bash
cd agent_configs && bash build_base_image.sh
```

### 3. Fetch the evaluation repositories

This clones the 50 upstream repositories, checks each one out at the snapshot commit recorded
in `repos_info.json`, and generates a `repomix` summary. The repositories are **not** shipped
with this benchmark; they are fetched from their original sources.

Pinning matters: the questions and checklists were written against those snapshots, so
evaluating against current upstream `HEAD` would score models on code the dataset never
described. A repository whose snapshot commit has disappeared upstream is reported at the end
of the run and should be excluded rather than evaluated at a different commit.

```bash
export DATASET_DIR=./dataset
bash scripts_agent/fetch_repos.sh
```

### 4. Run the evaluation

```bash
export OPENAI_API_KEY=<your-api-key>
export OPENAI_BASE_URL=<your-api-base-url>   # optional
export MODELS=gpt-5.2
bash scripts_agent/eval_models_multi_repo.sh
```

## Environment Variables

| Variable | Required | Default | Description |
|---|---|---|---|
| `OPENAI_API_KEY` | Yes | — | API key for the OpenAI-compatible endpoint |
| `OPENAI_BASE_URL` | No | `https://api.openai.com/v1` | Base URL of the endpoint |
| `OPENAI_SCORING_API_KEY` | No | falls back to `OPENAI_API_KEY` | Separate key for the scoring judge |
| `OPENAI_SCORING_BASE_URL` | No | falls back to `OPENAI_BASE_URL` | Separate base URL for the scoring judge |
| `MODELS` | No | `gpt-5.2` | Comma-separated models under test |
| `SCORING_MODEL` | No | `gpt-5.2` | Judge model used for checklist verification |
| `MAX_WORKERS` | No | `5` | Concurrent evaluation containers |
| `SCORING_WORKERS` | No | `10` | Concurrent scoring requests |
| `NUM_ITERATIONS` | No | `1` | Repeated runs per question, for variance analysis |
| `AGENT_CONFIG` | No | `agent_configs/agent.json` | Declares the agent scaffolding to evaluate |
| `AGENT_TIMEOUT` | No | `3600` | Per-question container timeout, in seconds |
| `OPENAI_TIMEOUT` | No | `3600` | Per-request timeout for model and judge calls, in seconds |
| `DATASET_DIR` | No | `./dataset` | Dataset directory, or a single CSV to evaluate one repository |
| `CANDIDATE_REPO_DIR` | No | `./candidate_repos` | Where upstream repositories are cloned |
| `REPO_JSON_PATH` | No | `./repos_info.json` | Repository metadata and snapshot commits |
| `CACHE_DIR` | No | `cache_experiments` | Cache of agent answers and judge scores |
| `OUTPUT_DIR` | No | `agent_results` | Where result files are written |
| `GIT_DEPTH` | No | `0` | Clone depth for `fetch_repos.sh`; `0` is a full clone |

The same defaults apply whether you go through `scripts_agent/` or call `evaluator.py` directly.

Inside the container the harness sets `REPOPROBE_MODEL` to the model under test and
`REPOPROBE_MAX_TURNS` from `agent.json`. The bundled gateway honours `REPOPROBE_GATEWAY_HOST`,
`REPOPROBE_GATEWAY_PORT` and `MAX_ROUNDS`; the reference agent reads `REPOPROBE_GATEWAY_URL`.

## Licensing

| Scope | Licence |
|---|---|
| Source code | [Apache-2.0](./LICENSE) |
| Benchmark data (`dataset/`, `repos_info.json`) | [CC BY 4.0](./dataset/LICENSE) |

The `question` and `answer` fields derive from publicly visible GitHub Discussions; copyright
in that text remains with the original authors. Each record keeps its `discussion_id` so the
original thread can be traced and attributed. Authors who wish to have their content removed
may open an issue.

Records whose original discussion referenced external links were rewritten by an LLM to fold
in a summary of the linked material, making each task answerable without network access;
records without external links retain their original wording. The `taxonomy` labels and
`checklist` rubrics were also LLM-generated and then verified by human expert annotators.

Personal data was removed before release: mentions of individual GitHub accounts were replaced
with `@user`, e-mail addresses with `contact@example.com`, and account names appearing in home
directory paths (in pasted stack traces and shell output) with `user`. Code-level uses of `@`
(annotations, decorators, npm scopes) and system accounts such as `root` were left intact,
since changing them would alter the technical meaning of the text.

The scope of the data licence is set out in [`dataset/NOTICE`](./dataset/NOTICE).
`repos_info.json` records the owner, name and pinned commit of every upstream repository, so
each question can be traced back to the exact snapshot it was written against.

## Citation

```bibtex
@inproceedings{repoprobe2026,
  author    = {Yang, Yuexi and Wu, Alyssa and Luo, Ji and Xuan, Richeng and
               Hu, Zhichao and Liu, Yuhong and Qin, Zhen},
  title     = {RepoProbe: Benchmarking Architecture-Aware Repository Comprehension with Checklists},
  booktitle = {Proceedings of the 41st IEEE/ACM International Conference on
               Automated Software Engineering (ASE '26)},
  year      = {2026},
  publisher = {ACM},
  address   = {New York, NY, USA}
}
```
