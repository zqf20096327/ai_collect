<img src="icon.png" alt="Open Malicious-Code Benchmark icon"> 

# Open Malicious-Code Benchmark

[![Support](https://img.shields.io/badge/Support-26A5E4?logo=telegram&logoColor=white)](https://t.me/falseposi)
[![Website](https://img.shields.io/badge/website-falseposi.com-1F6FEB?logo=googlechrome&logoColor=white)](https://falseposi.com/en)
[![Whitepaper](https://img.shields.io/badge/whitepaper-arXiv%3A2606.07792-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.07792)
[![License](https://img.shields.io/badge/license-BSD--2--Clause-blue.svg)](LICENSE)

> [!NOTE]
> **News:** The [MOLOT System Card whitepaper](https://arxiv.org/abs/2606.07792)
> is now available on arXiv.

**OMCBench** is a benchmark suite for evaluating malicious-code detection
capabilities. The benchmark consists of a labeled set of 800 Python and
JavaScript packages: 400 benign and 400 malicious packages for each language.

We also publish the [**MOLOT System Card**](https://arxiv.org/abs/2606.07792), which describes our progress on
malicious-code detection using machine learning. We cannot release the model
publicly because it is part of the PT Application Inspector product, but we can
provide its metrics on OMCBench.

MOLOT is compared against three open-source tools:

- **OSSGadget BackdoorRules** — run via Microsoft Application Inspector. This is
  the same rule engine as OSSGadget's `oss-detect-backdoor`.
- **bandit4mal** — a fork of [bandit](https://github.com/PyCQA/bandit) with
  rules tuned for malicious Python packages (Python only).
- **Semgrep** — run with [Apiiro's `malicious-code-ruleset`](https://github.com/apiiro/malicious-code-ruleset).

| Tool | Ecosystem | Code | Precision | Recall | F1 | Support |
|---|---|---|---:|---:|---:|---:|
| **MOLOT (ours)** | py | Commercial Use | 0.896 | 0.865 | **0.880** | 400 |
| ossgadget | py | Open Source | 0.554 | 0.770 | 0.644 | 400 |
| bandit4mal | py | Open Source | 0.519 | 0.885 | 0.654 | 400 |
| semgrep | py | Open Source | 0.557 | 0.685 | 0.614 | 400 |
| **MOLOT (ours)** | js | Commercial Use | 0.912 | 0.885 | **0.898** | 400 |
| ossgadget | js | Open Source | 0.671 | 0.805 | 0.732 | 400 |
| semgrep | js | Open Source | 0.746 | 0.645 | 0.692 | 400 |

Each tool is run as a subprocess over every package; its findings are parsed
into a common per-file / per-package prediction format and scored against
ground-truth labels.

## Repository layout

| Path | Contents |
|---|---|
| `benchmark/` | Benchmark code: tool runners, output parsers, metrics, CLI |
| `data/` | Bundled reference data (`file_labels.parquet` — file-level ground truth) |
| `results/` | Published benchmark results (see [Results](#results)) |
| `packages/` | The 800 package archives the benchmark was run on |
| `tests/` | Unit tests for the parsers, runners, metrics, and sampler |

## Installation

Requires Python `>=3.11` (tested on 3.12).

```bash
pip install -e .
```

This installs the Python dependencies (`pandas`, `numpy`, `scikit-learn`,
`click`, `loguru`, `tqdm`, `pyarrow`) and the `external-benchmark` console
script. The CLI is also runnable as `python -m benchmark`.

### External tools

The scanners themselves are **not** Python packages and must be installed
separately — the benchmark only calls them as subprocesses.

#### Tool versions used for the published results

To reproduce the numbers in `results/`, install these exact versions:

| Tool | Version | Notes |
|---|---|---|
| Application Inspector CLI | `1.9.55` | `dotnet tool install … --version 1.9.55` |
| OSSGadget BackdoorRules | repo commit `a41b2dad` (2026-04-08) | dir `src/Shared.CLI/Resources/BackdoorRules` |
| bandit4mal (`lyvd/bandit4mal`) | commit `03ba95f3` | fork has no released tag; pin by commit |
| Semgrep | `1.162.0` | `pipx install semgrep==1.162.0` |
| Apiiro `malicious-code-ruleset` | repo commit `a21246b6` (2025-02-24) | |

#### Install commands (pinned)

- **Application Inspector CLI** (for OSSGadget BackdoorRules):

  ```bash
  dotnet tool install -g Microsoft.CST.ApplicationInspector.CLI --version 1.9.55
  ```

  The binary is `appinspector`; pass its path via `--appinspector-bin`.

- **OSSGadget BackdoorRules** — directory of JSON rules from the
  [`microsoft/OSSGadget`](https://github.com/microsoft/OSSGadget) repository:

  ```bash
  git clone https://github.com/microsoft/OSSGadget
  git -C OSSGadget checkout a41b2dad
  ```

  Pass `OSSGadget/src/Shared.CLI/Resources/BackdoorRules` via
  `--appinspector-rules-path`.

- **bandit4mal** — installed via pipx at the pinned commit, plus the missing
  `pbr` dependency:

  ```bash
  pipx install "git+https://github.com/lyvd/bandit4mal.git@03ba95f388c006da1ebb053650f663ff2efc8eb5"
  pipx inject bandit pbr
  ```

  The binary is named `bandit` (e.g. `~/.local/bin/bandit`); pass its path via
  `--bandit4mal-bin`.

- **Semgrep**:

  ```bash
  pipx install semgrep==1.162.0
  ```

- **Apiiro `malicious-code-ruleset`** — clone the repository at the pinned
  commit into a directory of your choice:

  ```bash
  git clone https://github.com/apiiro/malicious-code-ruleset.git
  git -C malicious-code-ruleset checkout a21246b6
  ```

  Then pass that directory via `--semgrep-rules-path`.

## Usage

### `run` — run the benchmark

Runs every selected tool over the packages in a manifest, saves the raw tool
outputs, and computes metrics.

```bash
python -m benchmark run \
    --manifest results/manifest.csv \
    --packages-dir packages \
    --appinspector-rules-path OSSGadget/src/Shared.CLI/Resources/BackdoorRules \
    --bandit4mal-bin ~/.local/bin/bandit \
    --semgrep-rules-path .deps/malicious-code-ruleset \
    --output-dir runs
```

Key options:

- `--packages-dir` *(required)* — directory of package archives; filenames must
  match `folder_name` in the manifest.
- `--manifest` — CSV with columns `folder_name,ecosystem,label_true` listing the
  packages to run. Use `results/manifest.csv` to reproduce the published set.
  When omitted, the built-in stratified sampler is used instead and
  `--datasets-root` is required.
- `--datasets-root` — root containing `python/` and `js/` subdirs with
  `validation*.csv` files; required only when `--manifest` is not given.
- `--appinspector-rules-path` *(required)* — OSSGadget BackdoorRules directory.
- `--output-dir` — where to write results (default `runs/`). A `<run-id>/`
  subdirectory is created inside it.
- `--ecosystems` — comma-separated, `py`, `js`, or both (default `py,js`).
- `--tools` — which tools to run: `ossgadget`, `bandit4mal`, `semgrep`
  (default: all three).
- `--appinspector-bin` / `--bandit4mal-bin` / `--semgrep-bin` — tool binary
  paths (defaults: `appinspector`, `bandit`, `semgrep`).
- `--semgrep-rules-path` — local `apiiro/malicious-code-ruleset` checkout;
  required when `semgrep` is in `--tools`.
- `--timeout-sec` — per-package timeout in seconds (default 600).
- `--workers` — worker processes for the per-package loop (default 1).
- `--n-per-class` / `--seed` / `--smoke` — control the built-in sampler; ignored
  when `--manifest` is given.
- `--run-id` — run identifier; defaults to a UTC timestamp (`YYYYMMDD-HHMMSS`).

Outputs (in `<output-dir>/<run-id>/`):

| File | Contents |
|---|---|
| `manifest.csv` | The packages run: `folder_name`, `ecosystem`, `label_true` |
| `raw/<tool>/<pkg>.*` | Verbatim per-tool outputs (`.json` / `.sarif`) |
| `predictions.parquet` | Long-form predictions across all tools and packages |
| `metrics.csv` | Precision / Recall / F1 / ROC-AUC per `(tool, ecosystem, level)` |
| `runtime.csv` | Wallclock per `(tool, package)` |
| `config.json` | Run parameters |
| `inventory/<pkg>.json` | Per-package file list (used by `recalculate`) |
| `run.log` | Run log |

### `recalculate` — recompute metrics from saved raw outputs

Re-parses the saved `raw/` outputs and recomputes `predictions.parquet`,
`metrics.csv`, and `runtime.csv` without re-running the tools. Useful after
fixing parser logic. Requires a run directory produced by `run` (with `raw/`).

```bash
python -m benchmark recalculate --run-dir runs/20240501-120000
```

### `recompute-ci` — bootstrap confidence intervals

Computes nonparametric bootstrap confidence intervals from a saved
`predictions.parquet`. This works directly on the shipped results:

```bash
python -m benchmark recompute-ci --run-dir results
```

Options:

- `--run-dir` *(required)* — run directory containing `predictions.parquet`.
- `--n-resamples` — bootstrap resamples per `(tool, ecosystem, level,
  error_handling)` (default 1000).
- `--ci-level` — confidence level (default 0.95).
- `--seed` — RNG seed (default 42).
- `--out` — output path; defaults to `<run-dir>/metrics_ci.csv`.

## Results

The `results/` directory contains the published benchmark output:

| File | Contents |
|---|---|
| `manifest.csv` | The 800 benchmarked packages (`folder_name`, `ecosystem`, `label_true`) |
| `predictions.parquet` | Long-form per-tool predictions at package and file level |
| `metrics.csv` | Precision / Recall / F1 / ROC-AUC per `(tool, ecosystem, level)` |
| `metrics_ci.csv` | The same metrics with bootstrap confidence intervals (produced by `recompute-ci`, not by `run`) |

Package-level scores (`error_handling = as_benign`, 400 packages per
ecosystem, 50/50 benign/malicious):

| Tool | Ecosystem | Precision | Recall | F1 |
|---|---|--:|--:|--:|
| ossgadget | js | 0.671 | 0.805 | 0.732 |
| ossgadget | py | 0.554 | 0.770 | 0.644 |
| semgrep | js | 0.746 | 0.645 | 0.692 |
| semgrep | py | 0.557 | 0.685 | 0.614 |
| bandit4mal | py | 0.519 | 0.885 | 0.654 |

File-level scores (`error_handling = as_benign`; support varies per tool —
each tool's file row count depends on which files it scans, e.g. ossgadget
processes `.ts` files that semgrep does not). File-level ground truth comes
from the bundled `data/file_labels.parquet` (`file_label` ∈ {benign,
malicious, unknown}); only files with a confirmed `benign`/`malicious`
label participate. The expanded benign-file coverage from the unified label
source is why support is much larger than the per-package numbers:

| Tool | Ecosystem | Support | Precision | Recall | F1 |
|---|---|--:|--:|--:|--:|
| ossgadget | js | 15,305 | 0.197 | 0.632 | 0.300 |
| ossgadget | py | 10,203 | 0.183 | 0.566 | 0.277 |
| bandit4mal | py | 10,203 | 0.160 | 0.742 | 0.263 |
| semgrep | js | 14,913 | 0.567 | 0.418 | 0.481 |
| semgrep | py | 10,167 | 0.252 | 0.513 | 0.338 |

(bandit4mal is Python-only and is skipped for JavaScript packages.
`metrics_ci.csv` carries the same numbers with 1000-resample nonparametric
bootstrap 95% confidence intervals; file-level CIs use a clustered
bootstrap by package to account for within-package dependence.)

### Tool notes

- **bandit4mal** only analyses Python packages; JavaScript packages are skipped
  automatically.
- **ossgadget**, **bandit4mal**, and **semgrep** only report files they find
  suspicious. The benchmark pads each result with `score=0` / `benign` rows for
  every other source file in the package so that file-level metrics are correct.
- Two error-handling modes are reported in `metrics.csv`: `as_benign` treats a
  tool error as a benign prediction; `exclude` drops errored packages.
- **ROC-AUC** is omitted above because the three tools emit coarse severity
  scores (ossgadget effectively binary, bandit4mal 3 levels, semgrep 4) — a
  ROC curve is not meaningful for them; they are binary classifiers at a
  fixed threshold. The raw `roc_auc` column is still in `metrics.csv` for
  completeness.

### Caveats

- **Semgrep timeouts.** Semgrep times out (default 600 s) on ~10 large
  benign packages (`clearml`, `memray`, `regex`, `Faker`, `biopython`,
  `vue-template-compiler`, `chai`, `chevrotain`, `babel-parser`,
  `datadog-browser-rum`). Under `as_benign` these are counted as benign
  predictions, which mildly inflates semgrep's published precision. Re-run
  with `--timeout-sec 3600` and semgrep precision drops ~0.5–2 pp because
  it completes those packages and flags some of them as false positives.
- **Bandit4mal timeouts.** Bandit4mal historically left a 0-byte raw output
  file on timeout, which earlier benchmark versions parsed as "no
  findings" (silent false-benign). The current parser records timeouts as
  `error` (`Faker-30.8.2` is the only py package that hits this even at
  3600 s).
- **One package only hits a single tool.** `theremontada12@99.10.9.zip`
  carries the malicious label via a `preinstall: node README.md` hook
  (executes the README at install time); the bundled `.js` code itself is
  benign and no tool's code scanner flags it. It's intentionally kept in
  the malicious set because the hook is the malicious vector. A small
  number of other packages in the malicious set use the same pattern —
  the malicious vector lives in `package.json` install hooks rather than
  in scannable code.

## Dataset construction

The benchmark contains 800 packages — 200 benign + 200 malicious per
ecosystem (Python and JavaScript). Benign packages are sampled from the
top-downloaded set on PyPI and npm, restricted to permissive licenses
(MIT, BSD-2/3-Clause, Apache-2.0, ISC, PSF, Unlicense, ZPL-2.1) so the
bundle can be redistributed. Malicious packages are sampled from public
malware feeds. Per-file labels combine expert annotation and LLM
labeling. The full selection methodology — including near-duplicate
collapse and manual review swaps — is described in the parent (private)
benchmark; this repository ships only the final manifest
(`results/manifest.csv`) and the per-file labels for the 800 bundled
packages (`data/file_labels.parquet`).

## A note on scope

This is the open subset of a larger internal benchmark. The original benchmark
also compared an in-house detector; that tool and its results are intentionally
excluded here. The published results in `results/` therefore cover only the
three public tools above.

> ⚠️ The `packages/` directory contains real malicious package archives,
> included for benchmarking. Handle them in an isolated environment and do not
> install or execute them.

## Citation

If you use OMCBench or refer to the MOLOT results, please cite the whitepaper:

Lopatkin Daniil, Maksim Mitrofanov, Stanislav Rakovsky, and Aleksandr
Khalikov. 2026. "MOLOT System Card: Malicious Operational Logic Observation
Transformer." arXiv:2606.07792. https://doi.org/10.48550/arXiv.2606.07792

```bibtex
@misc{falseposi2026molot,
  title = {MOLOT System Card: Malicious Operational Logic Observation Transformer},
  author = {Lopatkin, Daniil and Mitrofanov, Maksim and Rakovsky, Stanislav and Khalikov, Aleksandr},
  year = {2026},
  eprint = {2606.07792},
  archivePrefix = {arXiv},
  primaryClass = {cs.CR},
  doi = {10.48550/arXiv.2606.07792},
  url = {https://arxiv.org/abs/2606.07792}
}
```
