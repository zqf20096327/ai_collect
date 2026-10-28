<div align="center">

<img src="docs/assets/overview.png" alt="LexBench Web Search — Measure what search finds." width="100%">

**English** · [简体中文](docs/README.zh-CN.md)

[![CI](https://github.com/lexmount/lexbench-websearch/actions/workflows/check.yml/badge.svg)](https://github.com/lexmount/lexbench-websearch/actions/workflows/check.yml)
[![License: Apache 2.0](https://img.shields.io/badge/code-Apache--2.0-51735b)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-356a91)](pyproject.toml)

[Features](#features) · [Tasks](#task-suites) · [Quickstart](#quickstart) · [Scoring](#scoring) · [Versions](#versions) · [Related projects](#related-repositories) · [Contributing](CONTRIBUTING.md)

</div>

Evaluate what a search system finds: ranked results, known sources and evidence for factual answers.

## Features

| Feature | What you get |
| --- | --- |
| Graded ranking metrics | Compute nDCG, precision and direct-result success from supplied relevance grades. [Evaluation protocol](docs/evaluation.md) |
| Retrieval diagnostics | Check known-page hits, source URLs and lexical answer evidence alongside ranking relevance. |
| Traceable tasks | Inspect query origins, adaptations, attribution and source licenses. [Data and sources](docs/data.md) |
| Qualified references | Keep reference-page checks and supported URL equivalences with the task definitions. |
| Offline CLI and Python API | Validate, export and score locally, without API calls or third-party runtime packages. |
| Verified definitions | Load and export hash-checked tasks; one bench release fixes the data, references and scoring code. |
| Runner integration | Use exported tasks with your own runner or [Browser Eval](https://github.com/lexmount/browser-eval) for provider calls, timing, evidence and reports. |

## Task suites

| Dataset | Tasks | Scope |
| --- | ---: | --- |
| `scenarios` | 149 | General web, named-site and vertical-search queries, with qualified references and URL equivalences |
| `factual` | 831 | SimpleQA Verified retrieval probes within the shared input limit, retaining publisher answers and source URLs |

The two suites contain 980 tasks. The selected bench release fixes their data,
references and scoring tools together; there is no separate dataset release to select.

Each query retains origin and derivation records. See [data and sources](docs/data.md) and [third-party notices](THIRD_PARTY.md).

The factual set adapts SimpleQA Verified for retrieval diagnostics. It does not reproduce the official closed-book answer evaluation. Report its metrics separately from scenario relevance.

## Quickstart

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then:

```sh
git clone https://github.com/lexmount/lexbench-websearch.git
cd lexbench-websearch
uv sync --frozen
uv run --frozen lexbench-websearch list
uv run --frozen lexbench-websearch validate scenarios
uv run --frozen lexbench-websearch validate factual
uv run --frozen lexbench-websearch export scenarios > /tmp/scenarios.json
```

These commands inspect and export the bundled definitions offline, without a browser or API key. A pinned integration needs no sibling checkout:

```sh
uv add 'lexbench-websearch @ git+https://github.com/lexmount/lexbench-websearch.git@<commit>'
```

## Scoring

Try a ranking that contains the useful result and one that misses it:

```sh
uv run --frozen lexbench-websearch score examples/relevant.json
uv run --frozen lexbench-websearch score examples/missing.json
```

The examples use supplied relevance labels: the first returns `success=1`, the second `success=0`. This CLI scores saved rankings; it does not fetch results or generate labels.

Relevance grades range from 0 (irrelevant) through 1 (related but insufficient) and 2 (useful support) to 3 (directly satisfies the request). The [evaluation protocol](docs/evaluation.md) defines nDCG, precision, success and aggregation across queries. Source-URL hits and lexical answer matches are separate diagnostics. Historical model labels are not distributed as human ground truth.

The Python API supports the same deterministic metrics:

```python
from lexbench_websearch.inputs import load_dataset, registry
from lexbench_websearch.relevance import query_metrics

cases = load_dataset(registry()["current"]["scenarios"])["cases"]
metrics = query_metrics(["useful", "unrelated"], {"useful": 3, "unrelated": 0}, cutoff=5)
assert metrics["ndcg"] == 1.0
assert metrics["precision"] == 0.2
```

## Run providers and build reports

Follow the [Browser Eval Search guide](https://github.com/lexmount/browser-eval/blob/main/harness/web_search/README.md) to run providers and build reports. Provider credentials, retries, latency, billing and measured outputs belong to the harness. The [integration guide](docs/integration.md) defines normalized responses, reference bindings and annotation inputs.

## Versions

Use the [release history](https://github.com/lexmount/lexbench-websearch/releases) to choose a frozen benchmark. Run `uv run --frozen lexbench-websearch version` to inspect the installed catalog and scoring state. See [version rules](docs/versions.md) for result comparisons.

## Related repositories

| Repository | Role |
| --- | --- |
| [Browser Eval](https://github.com/lexmount/browser-eval) | Provider execution, saved evidence and comparison reports |
| [LexBench Web Fetch](https://github.com/lexmount/lexbench-webfetch) | Web Fetch tasks, frozen references and acceptance scoring |
| [Moli](https://github.com/lexmount/moli) | Browser used in the companion evaluation harness |
| [WebFetch CLI](https://github.com/lexmount/webfetch-cli) | CLI client for the Lexmount WebFetch service |
| Artifact Site ([Mainland China](https://yours.lexmount.cn/artifact-site) · [Global](https://yours.lexmount.com/artifact-site)) | Report sharing and access controls |
| [Lexbench-Headless-Browser](https://github.com/lexmount/Lexbench-Headless-Browser) | Protocol, automation-driver and web-platform benchmarks |

[Third-party notices](THIRD_PARTY.md) retain the terms for Microck/websearch-bench, SimpleQA Verified, OpenAI SimpleQA and community material. Code, tools and guides use English; dataset text keeps its original language.

## Contribute

Read [CONTRIBUTING](CONTRIBUTING.md) before changing task definitions, references or scoring.

```sh
make check
make package-check
```

[Security](SECURITY.md) · [Third-party content](THIRD_PARTY.md) · [Apache 2.0](LICENSE)

## License

Project-owned code and contributions use [Apache 2.0](LICENSE). Bundled datasets retain their original licenses and copyright notices; see [THIRD_PARTY](THIRD_PARTY.md).

## Cite LexBench Web Search

Project citation: [CITATION.cff](CITATION.cff).

```bibtex
@software{lexbench_websearch_2026,
  author = {{LexBench Web Search contributors}},
  title = {Browser Eval: Benchmarking Browsers and Web Tools for AI Agents},
  note = {Web Search benchmark component},
  year = {2026},
  url = {https://github.com/lexmount/lexbench-websearch}
}
```
