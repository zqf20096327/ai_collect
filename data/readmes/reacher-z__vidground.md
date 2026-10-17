# VidGround

> **Watch Before You Answer: Learning from Visually Grounded Post-Training**

[![arXiv](https://img.shields.io/badge/arXiv-2604.05117-b31b1b.svg)](https://arxiv.org/abs/2604.05117)
[![HF Paper](https://img.shields.io/badge/%F0%9F%A4%97-Paper-yellow)](https://huggingface.co/papers/2604.05117)
[![Project Page](https://img.shields.io/badge/Project-Page-blue)](https://vidground.etuagi.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview

Many video benchmarks and post-training datasets contain questions that can
be answered without watching the video. VidGround identifies those examples
with a text-only probe and keeps the examples that require visual evidence.

The released package is a deterministic curation component. It does not
download a model, call an API, or claim that a heuristic reproduces the
paper's probe. Users run their text-only model separately, save its
predictions, and pass the complete probe log to the filter.

## What's Included

- A validated JSONL filter for audited text-only probe outputs.
- Exact, Unicode-aware answer matching with explicit probe coverage checks.
- A machine-readable audit summary for every curation run.
- Framework-independent evaluation helpers.
- Release metadata, citation metadata, and build checks.

The training launcher and paper evaluation runners are not included. The
launcher exits with a non-zero status instead of pretending to run training.

## Repository Structure

```text
vidground/
├── README.md
├── CHANGELOG.md
├── CITATION.cff
├── LICENSE
├── citation.bib
├── pyproject.toml
├── data/                          # input and curation instructions
├── eval/                          # evaluation boundary and paper references
├── scripts/
│   ├── filter_visually_grounded.py
│   ├── release_pypi.sh
│   └── run_rl_posttrain.sh
├── tests/
└── src/vidground/
    ├── __init__.py
    ├── cli.py                     # JSONL command-line interface
    ├── eval.py                    # evaluation helpers
    └── filter.py                  # curation data model and logic
```

## Installation

For local development:

```bash
git clone https://github.com/reacher-z/vidground.git
cd vidground
python -m pip install -e '.[dev]'
```

For a reproducible source installation (Python 3.9+ and Git required):

```bash
python -m pip install "git+https://github.com/reacher-z/vidground.git@7ae3b2fec65eb7d5d2a6a0c20b5b6b255d4efdc3"
```

This pinned revision declares version 0.1.1 and was installed successfully in a
fresh environment. On September 15, 2026, the PyPI project endpoint returned
404 and `pip install vidground==0.1.1` was unavailable. Use the source command
above; the GitHub version tag does not by itself establish PyPI availability.

For a small runnable introduction, see the
[probe-log mini-lab](https://yuxuan.world/research/papers/vid-filter/probe-lab/).
It includes four handwritten fixtures, answer-format and Unicode checks, and
a missing-coverage failure check. It does not run a model, process video, or
reproduce the paper's metrics.

## Quick Start

### 1. Prepare the input data

Each input line must be a JSON object with `id`, `question`, and `answer`.
`options` is optional in the library but should be included for
multiple-choice data. Extra fields, such as `video`, are retained in the
filtered output.

```json
{
  "id": "example-001",
  "video": "path/to/video.mp4",
  "question": "What happens next?",
  "options": ["A", "B", "C", "D"],
  "answer": "B"
}
```

### 2. Save a text-only probe log

Run the probe with the question and options only. It must not receive video
or image content. Save exactly one record for every input ID:

```json
{"id": "example-001", "predictions": ["B"]}
```

Predictions must already use the same answer representation as the input
answer. The filter compares normalized strings and does not extract answers
from free-form model responses.

### 3. Filter and write an audit record

```bash
vidground-filter \
  --input data/raw/your_dataset.jsonl \
  --text-only-probes data/raw/your_text_only_probes.jsonl \
  --output data/filtered/your_dataset.vidground.jsonl \
  --audit-output data/filtered/your_dataset.vidground.audit.json
```

The command rejects malformed records, duplicate IDs, missing probe coverage,
and probes that do not correspond to an input. It writes output files
atomically, so a failed run does not replace an existing result.

For a local summary only, use the library:

```python
from vidground import TextOnlyProbe, curate_dataset

retained, summary = curate_dataset(examples, probes)
print(summary.as_dict())
```

The old 0.1.0 `--probe` flag and compatibility classes remain available for
small smoke tests. They are not a substitute for a recorded model probe.

### 4. Verify the package

```bash
python -m pytest
python -m build
python -m twine check dist/*
```

To build and validate the exact release flow without uploading:

```bash
DRY_RUN=1 bash scripts/release_pypi.sh
```

When the package is ready for PyPI, provide a token through the environment:

```bash
TWINE_TOKEN=... bash scripts/release_pypi.sh
```

## Data and Evaluation

The repository does not redistribute the datasets used in the paper or claim
artifact-level reproduction of its reported metrics. See
[`data/README.md`](data/README.md) for input and probe contracts and
[`eval/README.md`](eval/README.md) for the evaluation boundary.

## Paper-Reported Results

The following values are reported in the
[public preprint](https://arxiv.org/abs/2604.05117), not regenerated by this
repository. The paper reports a single GPT-5-mini text-only pass retaining
181,710 of 263,071 Video-R1-260K samples, or 69.1%.

| Frames | VideoMME | VideoMMMU | MMVU | Avg. Full | Avg. VG |
|---:|---:|---:|---:|---:|---:|
| 16 | 58.7 | 47.4 | 64.2 | 56.8 | 45.2 |
| 32 | 61.5 | 48.3 | 65.8 | 58.5 | 47.6 |
| 64 | 63.4 | 49.4 | 65.6 | 59.5 | 47.9 |

## Citation

If you use VidGround or the accompanying materials, cite the public preprint.
GitHub also renders the preferred citation from
[`CITATION.cff`](CITATION.cff).

```bibtex
@article{zhang2026vidground,
  title   = {Watch Before You Answer: Learning from Visually Grounded Post-Training},
  author  = {Zhang, Yuxuan and Hwang, EunJeong and Zhang, Huaisong and Du, Penghui
             and Jia, Yiming and Jiang, Dongfu and He, Xuan and Zhang, Shenhui
             and Nie, Ping and West, Peter and Allen, Kelsey R.},
  journal = {arXiv preprint arXiv:2604.05117},
  year    = {2026},
  url     = {https://arxiv.org/abs/2604.05117}
}
```

## Acknowledgements

We thank our collaborators at UBC, Vector Institute, Etude AI, Kuaishou
(Kolors Team), University of Toronto, University of Waterloo, and UIUC.

## License

Released under the [MIT License](LICENSE).
