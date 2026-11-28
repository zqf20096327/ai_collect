# LDST · Log-Driven Semantic Tuning for MIP Solvers

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Repository checks](https://github.com/Zhengzhong-You/LDST/actions/workflows/repository-checks.yml/badge.svg)](https://github.com/Zhengzhong-You/LDST/actions/workflows/repository-checks.yml)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB.svg)](pyproject.toml)
[![SCIP 9.2.4](https://img.shields.io/badge/SCIP-9.2.4-476A6F.svg)](#requirements)
[![Benchmark: 215 instances](https://img.shields.io/badge/Benchmark-215_instances-476A6F.svg)](PROVENANCE.md)

Research code and benchmark data for tuning the SCIP mixed-integer programming solver with a large language model that reads solver logs.

**[Quick start](#quick-smoke-test)** · **[Experiments](docs/experiment_recipes.md)** · **[Benchmark data](#benchmark-data)** · **[Provenance](PROVENANCE.md)** · **[Contributing](CONTRIBUTING.md)** · **[Citation](#citation)**

This repository accompanies the paper

> Zhengzhong You, Kaizhao Sun, Zeping Min, Wotao Yin, and Xinshang Wang. *Log-Driven Semantic Tuning for Mixed Integer Programming Solvers.* Working paper, 2026.

## What LDST is

Black-box configurators observe one scalar outcome per solver run. LDST instead reads the run itself: after each SCIP run, a fixed-schema parser turns the log into compact diagnostics on presolve, the root LP and cuts, branching, heuristics, and bound progress. An LLM receives these diagnostics, a memory of earlier trials centered on the current best configuration, and the meaning, type, and domain of each parameter in a curated 45-parameter whitelist. It proposes a sparse edit to the current best configuration. Each proposal passes schema, domain, and novelty checks, must load as a SCIP settings file, and is then evaluated by an actual solver run.

The tuning objective depends on what the default configuration achieves within the 600-second limit. For instances that the default run solves (Case 1), LDST uses an estimate of completion time, T̂∞, obtained by fitting a branch-and-bound tree-growth surrogate to snapshots from the ordinary SCIP progress table. Intermediate instances with a feasible but unproved solution (Case 2) use the primal–dual integral, and hard instances with dual progress only (Case 3) use the normalized improvement of the final dual bound. Each loss is normalized by its value under the default configuration.

The repository contains the LDST implementation, the scalar-feedback baselines (SMAC3, RBFOpt, and Random), and the entry points and analysis scripts for the paper's experiments: single-instance tuning (Exp. A), prompt-information ablations (Exp. B), within-family transfer (Exp. C), and the appendix validation of the completion-time signal. It also contains the 215-instance benchmark: the 156 generated CVRP, GAP, JSP, and UFL instances are bundled; the 59 MIPLIB 2017 instances are downloaded from the official MIPLIB site by script and verified by SHA-256. Experiment logs and raw LLM responses are not included.

## Repository layout

| Path | Contents |
|---|---|
| `src/ldst/` | Prompt construction, SCIP-log feature extraction, OpenAI client (`models/gpt/`), and benchmark builders (`benchmarks/`) |
| `src/two_stage/` | `oracle` (one SCIP run and its log), `prompt_step` (history, loss, validation, next edit), and `sim_loop` (both steps on one host) |
| `src/utilities/` | SCIP CLI runner and version check, log parser, completion-time estimator (`est_time.py`), typed whitelist, formulations, and the baseline CLI (`optimizer_cli.py`) |
| `src/random_tune/`, `src/smac_tune/`, `src/rbfopt_tune/` | Scalar-feedback baselines |
| `scripts/` | Experiment entry points (`run_expA_single.py`, `run_expC_multi.py`, `preview_prompt_modes.py`), benchmark tools (`benchmarks/`), and the paper's analysis, figure, and planning scripts (`analysis/`, `figures/`, `plans/`) |
| `manifests/`, `splits/` | The 215-instance manifest with regime labels, and the Exp. C train/test splits |
| `benchmarks/` | Generated instances (`derived/`), raw-source records and checksums (`source/`), and the XML100 configuration files and checksum manifest (`validation/`) |
| `assets/metadata/` | The typed curated whitelist of 45 SCIP parameters |
| `examples/` | Small manifests, diagnostic snapshots, and prompt previews for the four prompt variants |
| `docs/` | [Experiment recipes](docs/experiment_recipes.md), [code map](docs/repo_map.md), and [results layout](docs/results_layout.md) |
| `tests/` | No-LLM smoke tests, offline unit tests, and the [validation record](tests/TESTED.md) |
| `results/` | Per-instance results behind the paper (`paper/`) and the location for locally generated logs and summaries |

## Requirements

- Python 3.10 or later. The paper used Python 3.12.4 on Ubuntu Linux (x86_64).
- The SCIP 9.2.4 command-line binary, on `PATH` or given by `SCIP_BIN=/absolute/path/to/scip`. The runner checks the version and refuses any other release. The completion-time fit also solves a small model through this binary's AMPL `.nl` reader, which standard SCIP builds include. `conda install -c conda-forge scip=9.2.4` installs this binary on Linux, macOS, and Windows. Homebrew's `scip` formula now installs SCIP 10, so on macOS use conda-forge or a 9.2.4 build from [scipopt.org](https://scipopt.org).
- The Python dependencies in [`pyproject.toml`](pyproject.toml) (OpenAI SDK, PyYAML, Pyomo, NumPy, SciPy, Matplotlib, Requests, PySCIPOpt). PySCIPOpt is used only to build benchmark instances; all solver runs go through the SCIP binary.
- Optional: SMAC3, RBFOpt, and ConfigSpace for the SMAC3 and RBFOpt baselines (the paper used SMAC3 2.3.1). Depending on its settings, RBFOpt can also require the Bonmin and Ipopt executables; see the RBFOpt documentation.
- For LLM runs only: an OpenAI API key with access to the model (GPT-5.2 in the paper). The smoke tests make no LLM calls.

## Installation

```sh
git clone https://github.com/Zhengzhong-You/LDST.git
cd LDST
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .                  # LDST, Random baseline, analysis code
python -m pip install -e ".[baselines]"     # optional: SMAC3 and RBFOpt baselines
scip --version                              # must report 9.2.4, or export SCIP_BIN
```

`bash scripts/bootstrap_env.sh` creates `.venv/` and installs the package in editable mode. Run all commands below from the repository root.

## Quick smoke test

```sh
./tests/run_smoke_tests.sh                                       # needs SCIP 9.2.4; no LLM calls
python -m unittest discover -s tests -v                          # offline; no SCIP binary or API key needed
python scripts/benchmarks/verify_derived_instances.py --check_sha256
```

The smoke script compiles all Python files and runs, in `--no_llm` mode, one single-instance trial, the prompt-preview generator for the four prompt variants, one `two_stage.sim_loop` trial, and one multi-instance trial on small CVRP instances. It takes about one minute and writes its logs under `out/`. Like every LDST run, it also writes a CSV snapshot of the prompt memory, `<instance>.csv`, to the working directory; root-level CSV files are ignored by git. A scalar-feedback baseline can be checked the same way:

```sh
python -m utilities.optimizer_cli random --whitelist curated \
  --instance benchmarks/derived/cvrp_P-n16-k8.mps.gz --case 1 --tau 60 --n_trials 1
```

## Reproducing the paper

All solver runs use SCIP 9.2.4 with one thread, a 600-second limit, and `randomization/randomseedshift = 42`; stochastic baselines also use seed 42. [docs/experiment_recipes.md](docs/experiment_recipes.md) gives the full commands, output folders, and analysis scripts.

| Experiment | Entry point | Budget and inputs |
|---|---|---|
| Exp. A: single-instance tuning against SMAC3, RBFOpt, and Random | `scripts/run_expA_single.py --prompt_mode ldst`; `python -m utilities.optimizer_cli {smac,rbfopt,random}` | 51 evaluations (default run plus 50 proposals) per method and instance; all 215 instances in `manifests/cleaned_case_assignments.csv` |
| Exp. B: prompt-information ablations | `scripts/run_expA_single.py --prompt_mode {outcome_only,static_context,index_only}` | 31 evaluations per method and instance on the 76 Case 1 instances |
| Exp. C: within-family transfer and multi-instance tuning | `scripts/run_expC_multi.py`, `scripts/plans/`, `splits/` | Same per-run budget as single-instance tuning; fixed train/test splits for CVRP, GAP, JSP, and UFL |
| Appendix: completion-time signal on XML100 | `python -m utilities.est_time --retro`, `scripts/analysis/analyze_rank_corr.py` | 100 XML100 CVRP instances and 10 fixed configurations in `benchmarks/validation/` |

LLM runs are not deterministic even with fixed solver seeds, so reruns reproduce the protocol rather than identical trajectories.

### Paper results

[`results/paper/`](results/paper/) contains the per-instance results behind the main results, the mechanism study, the single-anchor transfer study, and the appendix validation of the completion signal. The following command recomputes every reported number from these files with the Python standard library and checks it against the paper:

```sh
python scripts/analysis/verify_paper_tables.py
```

## Benchmark data

| Family | Instances | In this repository |
|---|---:|---|
| CVRP (CVRPLIB sets A, B, E, F, P; SYMPHONY archive) | 90 | Generated `.mps.gz` files in `benchmarks/derived/` |
| GAP (OR-Library types C and D) | 12 | Generated `.mps.gz` files in `benchmarks/derived/` |
| JSP (OR-Library job shop) | 24 | Generated `.mps.gz` files in `benchmarks/derived/` |
| UFL (UflLib Uniform) | 30 | Generated `.mps.gz` files in `benchmarks/derived/` |
| MIPLIB 2017 (`benchmark-v2` draw) | 59 | Names and SHA-256 digests only; download with the command below |
| XML100 validation set (appendix) | 100 | Names and SHA-256 digests in `benchmarks/validation/xml100_manifest.csv`; instance files not included |

The raw upstream files used to generate CVRP, GAP, JSP, and UFL are not redistributed. [PROVENANCE.md](PROVENANCE.md) explains each decision and its evidence, and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) gives attribution and citations.

```sh
# Check that the 156 bundled instances match their recorded SHA-256 digests
python scripts/benchmarks/verify_derived_instances.py --check_sha256

# Download the 59 MIPLIB 2017 instances (about 75 MB) into benchmarks/derived/ and verify them
python scripts/benchmarks/build_derived_instances.py --families MIPLIB --verify_sha256
python scripts/benchmarks/verify_derived_instances.py --check_sha256 --require_miplib

# Fetch the raw CVRP/GAP/JSP/UFL sources (SHA-256 checked) and rebuild the generated families byte for byte
python scripts/benchmarks/download_benchmark_sources.py
python scripts/benchmarks/build_derived_instances.py --families CVRP GAP JSP UFL \
  --outdir out/rebuilt_generated --verify_against benchmarks/derived --exact_bytes
```

Downloaded files are stored under `benchmarks/source/upstream/` and `benchmarks/derived/miplib_*.mps.gz`, which are ignored by git. When the UflLib site is unreachable, place a copy of `Uniform.tgz` at `benchmarks/source/upstream/ufllib/Uniform.tgz`; the downloader then verifies its checksum.

## LLM and API configuration

LDST calls the OpenAI Responses API through `src/ldst/models/gpt/call_gpt.py`. Credentials and endpoints are read only from environment variables; no command-line option accepts them, and the code does not write them to its outputs.

| Variable | Purpose |
|---|---|
| `OPENAI_API_KEY` | API key; required for LLM runs |
| `OPENAI_BASE_URL` | Optional OpenAI-compatible endpoint; `OPENAI_API_BASE` is accepted as a legacy alias |
| `OPENAI_MODEL` | Model used when `--model` is not given (default `gpt-5.2`); `MODEL` is read as a fallback |
| `LDST_REASONING_EFFORT` | Reasoning effort sent with each request (default `medium`) |
| `LDST_TELEMETRY_FILE` | Optional JSONL file with one record per API call (model, latency, token usage, and any error message); prompts are not recorded |
| `LDST_CALL_CONTEXT` | Optional JSON object copied into each telemetry record |
| `SCIP_BIN` | Path to the SCIP 9.2.4 binary when `scip` is not on `PATH` |

Requests use JSON output and at most 20,000 output tokens; an invalid response is re-queried up to three times. Only the OpenAI provider is implemented; the other modules under `src/ldst/models/` are stubs.

**Cost.** API usage is billed to your account. For the main Exp. A bank with seed 42, LDST made 10,964 GPT-5.2 calls using 62,958,576 tokens, about USD 320 at uncached list prices, or roughly 51 calls per instance. Solver time dominates wall-clock time: each method–instance pair in Exp. A can use up to 51 × 600 s, about 8.5 hours. Start with `--trials 2` on a few instances to check cost and setup.

## Tests and validation

[tests/TESTED.md](tests/TESTED.md) lists the checks and what was verified for this release. The smoke and unit tests exercise the code paths; `scripts/analysis/verify_paper_tables.py` checks the reported numbers against the released per-instance results.

## Questions and contributions

Use [GitHub Issues](https://github.com/Zhengzhong-You/LDST/issues) for reproducible bugs, questions, and proposed improvements. Include the commit, operating system, SCIP and Python versions, the exact command, and the instance. The [contribution guide](CONTRIBUTING.md) describes how to keep benchmark evidence reproducible.

## License

Copyright (c) 2026 Alibaba Group. The code and documentation are released under the [MIT License](LICENSE). Benchmark instances derived from third-party collections remain subject to their upstream terms; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). SCIP, the OpenAI API, and the Python dependencies are not distributed here and are governed by their own licenses and terms.

## Citation

Please cite the paper and record the repository commit used in your experiments. [CITATION.cff](CITATION.cff) supplies GitHub's **Cite this repository** metadata.

```bibtex
@misc{you2026ldst,
  title  = {Log-Driven Semantic Tuning for Mixed Integer Programming Solvers},
  author = {You, Zhengzhong and Sun, Kaizhao and Min, Zeping and Yin, Wotao and Wang, Xinshang},
  year   = {2026},
  note   = {Working paper}
}
```

When you use the benchmark, please also cite the upstream collections listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
