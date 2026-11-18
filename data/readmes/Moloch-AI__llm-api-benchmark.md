# LLM API Benchmark: Compare Latency, Throughput & Cost

*Open-source benchmarking toolkit for OpenAI-compatible LLM APIs.*

[![CI](https://github.com/Moloch-AI/llm-api-benchmark/actions/workflows/ci.yml/badge.svg)](https://github.com/Moloch-AI/llm-api-benchmark/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

![llm-api-benchmark: compare latency, throughput, reliability and cost of OpenAI-compatible LLM APIs](assets/banner.svg)

`llm-bench` measures what your application would experience when it calls an LLM API. It reports
time to first token, end-to-end latency, output tokens per second, error rates by type, cost
from the prices you supply, and whether tool (function) calls come back well formed. A
conformance suite checks which OpenAI parameters and behaviors an endpoint supports, and which it
accepts but silently ignores. Each workload is reported separately, with sample sizes, from a fixed
and versioned set of prompts. Runs are bounded before they start: a request cap, an optional USD
budget, a dry run, and confirmation for larger runs.

It works with any endpoint that speaks the OpenAI Chat Completions format: hosted APIs, gateways,
and local servers. It is a measurement tool for comparing endpoints from the client's side. It is
not a load generator.

- [Features](#features)
- [Installation](#installation)
- [Quickstart](#quickstart)
- [Example configuration](#example-configuration)
- [Sample output](#sample-output)
- [Test tool calling](#test-tool-calling)
- [OpenAI-compatible API test suite](#openai-compatible-api-test-suite)
- [Supported providers](#supported-providers)
- [Metrics](#metrics)
- [Methodology](#methodology)
- [Configuration](#configuration)
- [Commands](#commands)
- [Security](#security)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## Features

- **Streaming and non-streaming.** In stream mode, TTFT (first text, reasoning included) and TTFC
  (first answer text) are measured separately, so reasoning models are not misread.
- **Distributions with sample sizes.** Each workload gets min, median, P90, P95 and max, with
  `n`. Tail percentiles from fewer than 20 samples are flagged.
- **Throughput from the provider's `usage`.** When a provider reports no usage, token counts are
  estimated and marked `~`. No substitute tokenizer is used.
- **Typed reliability.** Failures are recorded as `http_429`, `http_503`, `timeout`,
  `connection_error`, `invalid_response` or `stream_error:<type>` (errors sent inside a stream
  that opened with HTTP 200), with an error rate per endpoint.
- **Bounded runs.** `max_requests`, an optional budget, `--dry-run`, and confirmation above 20
  requests. Concurrency is 1 by default and at most 8, and requests are spaced to each provider's
  `rate_limit_rpm`.
- **Polite under errors.** `Retry-After` is honored, failures back off, and an endpoint stops after
  a permanent error (401, 402, 403, 404, or a 429 with `X-Should-Retry: false`) or repeated
  failures. Nothing is retried, because each attempt is one sample.
- **Cost from your prices.** Enter per-token prices with their source and date. The tool ships no
  prices.
- **Versioned datasets.** `core-v1` has eight workloads, from one-word answers to 700-word
  tutorials, and `tools-v1` four tool-calling workloads. Each run records the dataset's version
  and SHA-256. You can add your own datasets.
- **Optional deterministic checks.** Does the JSON parse, does the code compile, is the number on
  the last line correct. They are mechanical checks, not a quality score.
- **Tool calling.** `tools-v1` has four workloads: picking the right function or none, filling
  typed arguments, several calls in one reply, and following `tool_choice`. Checks cover the
  function chosen, the expected argument values and JSON Schema validity. Agreement across
  repetitions is reported too. Streamed calls are rebuilt from their fragments.
- **Reports.** A terminal table, JSON, CSV (per request and per group), Markdown, and a
  self-contained HTML page with local SVG charts that loads nothing from the network.
- **Conformance suite.** `llm-bench conformance` runs 22 tests (21 small requests) for model
  listing, streaming, usage, parameter handling, tool calls and error bodies. It reports PASS,
  WARN or FAIL per test, as a terminal table, JSON, Markdown and JUnit XML.
- **Comparisons.** `llm-bench compare` gives the difference of medians with a 95% bootstrap
  interval, and says "no clear difference" when the interval includes zero.
- **Credentials stay out.** Keys are read only from environment variables, and terminal output,
  logs and result files are redacted.
- **Ctrl+C keeps what was measured.** In-flight requests are cancelled and partial results are
  written.

## Installation

Requires Python 3.11 or newer. The package is **not on PyPI yet**, so install it from GitHub:

```bash
pipx install "git+https://github.com/Moloch-AI/llm-api-benchmark"
# or, in a virtual environment:
pip install "git+https://github.com/Moloch-AI/llm-api-benchmark"
```

This installs the `llm-bench` command; `python -m llm_api_benchmark` works too. A different
project already uses the PyPI name `llm-bench` (it installs a `llm_bench` command). Do not install
that one by mistake.

## Quickstart

**Try it offline first.** The synthetic demo simulates two endpoints in-process, with no key and
no network. Every report it produces is labeled as synthetic data.

```bash
llm-bench init synthetic-demo
llm-bench run --config synthetic-demo.yaml --yes --formats json,csv,md,html
```

**Then point it at a real endpoint.** Start with a dry run, which prints the plan and sends
nothing:

```bash
llm-bench init molochai            # or: llm-bench init openai-compatible
export MOLOCHAI_API_KEY=your-api-key
llm-bench run --config molochai.yaml --dry-run
llm-bench run --config molochai.yaml
```

Results go to `results/`: JSON always, plus CSV, Markdown and HTML with `--formats`. To render
them again later:

```bash
llm-bench report results/molochai-<timestamp>.json --format html -o report.html
llm-bench compare results/run-a.json results/run-b.json
```

## Example configuration

Two endpoints in one file, so they are interleaved over the same time window:

```yaml
version: 1
name: two-endpoints
dataset: core-v1
workloads: [short-answer, code-explain, json-generation]
modes: [stream]
repetitions: 5            # each prompt, per endpoint
warmup: 1                 # per endpoint, excluded from statistics
concurrency: 1
timeout_s: 120
max_requests: 100         # the run refuses larger plans
temperature: 0.2          # omit to use each provider's default
providers:
  - name: molochai-llama-70b
    preset: molochai                 # base URL, key variable, rate limit, notes
    model: llama-3.3-70b-instruct-abliterated
  - name: other-provider
    preset: openai-compatible
    base_url: https://api.example.com/v1
    api_key_env: OTHER_PROVIDER_API_KEY
    model: ${OTHER_MODEL}            # expanded from the environment
    rate_limit_rpm: 60
    pricing:                         # optional; enables cost and --budget
      input_per_mtok: 0.50
      output_per_mtok: 1.50
      currency: USD
      source: https://example.com/pricing
      checked_on: 2026-11-17
```

Ready-made files are in [benchmarks/](benchmarks/):

- [molochai.yaml](benchmarks/molochai.yaml)
- [openai-compatible.yaml](benchmarks/openai-compatible.yaml): OpenAI's API as the example
- [synthetic-demo.yaml](benchmarks/synthetic-demo.yaml)

`llm-bench init` writes the same three files.

## Sample output

> The output below is **synthetic fixture data** from `benchmarks/synthetic-demo.yaml`: two
> simulated endpoints, one with injected errors. It shows the report format and is not the
> performance of any real API. The full set of files is in
> [examples/synthetic-demo/](examples/synthetic-demo/): the
> [Markdown report](examples/synthetic-demo/report.md), the HTML report (`report.html`; GitHub
> shows HTML as source, so download it and open it in a browser), the JSON and both CSV files.

```text
SYNTHETIC FIXTURE DATA - not the performance of any real API.

synthetic-demo  |  2026-11-17T11:08:42+00:00  |  dataset core@1.0.0  |  15.58 s

short-answer  (max_tokens 32, 3 prompts)
Provider      Mode    n  Errors  TTFT p50  TTFT p95  TTFC p50  Latency p50  Latency p95  Out tok/s  Decode tok/s  Checks
------------  ------  -  ------  --------  --------  --------  -----------  -----------  ---------  ------------  ------
sim-steady    stream  9    0.0%     0.079    0.088*     0.079        0.232       0.246*      142.6         202.5       -
sim-steady    plain   9    0.0%         -         -         -        0.185       0.207*      189.6             -       -
sim-variable  stream  9    0.0%     0.125    0.234*     0.125        0.269       0.353*      112.6         206.1       -
sim-variable  plain   9    0.0%         -         -         -        0.235       0.298*      134.7             -       -

Reliability (all requests, warm-up included)
Provider      Model               Sent  OK  Error rate  Errors       Skipped  Cost
------------  ------------------  ----  --  ----------  -----------  -------  ----
sim-steady    synthetic-steady      55  55        0.0%  -                  0     -
sim-variable  synthetic-variable    55  52        5.5%  http_503 x3        0     -
```

`*` marks tail percentiles from fewer than 20 samples. A comparison of the two simulated
endpoints ([compare.txt](examples/synthetic-demo/compare.txt)) reports "no clear difference"
wherever the bootstrap interval includes zero.

## Test tool calling

Does an endpoint pass `tools` through, return calls in the standard shape, fill the arguments your
schema asks for, and respect `tool_choice`? The `tools-v1` dataset asks small, harmless questions
with tools attached. The tools are never executed; only the calls are checked.

```bash
llm-bench run --config synthetic-tools.yaml --yes          # offline, simulated
llm-bench run --config my-endpoint.yaml --dataset tools-v1 --dry-run
```

| Workload | What it asks | Checks |
|---|---|---|
| `tool-select` | Pick one of four functions, or answer without a tool | `tool_call` (name and arguments), `no_tool_call`, `tool_args_valid`, `tool_call_count` |
| `tool-args` | Dates, times, integers in a range, enums and lists | expected values, schema validity |
| `tool-parallel` | Two or three calls in one reply | `tool_call_count` with `min`, each expected call |
| `tool-choice` | A named function, `"required"`, `"none"` | the forced call, or no call |

The report adds a table per tool workload:

```text
Provider      Mode    Called a tool       Same calls  tool_args_valid  tool_call
------------  ------  -------------  ---------------  ---------------  ---------
sim-steady    stream          77.8%  44% (3 prompts)              4/9        0/9
```

That example comes from the simulator, which does not read prompts, so its argument checks fail
by design. Use your own tools in a dataset file (see [docs/configuration.md](docs/configuration.md#tool-workloads))
to test the calls your application makes. These checks show whether calls are well formed and as
expected on small tasks; they are not an agent benchmark.

## OpenAI-compatible API test suite

"OpenAI-compatible" usually means "some of it". `llm-bench conformance` finds out which parts. Its
most useful finding is a parameter that is accepted and then ignored: a `max_tokens`, `stop`,
`n`, `response_format` or `logprobs` that returns HTTP 200 without taking effect.

```bash
llm-bench conformance -c synthetic-conformance.yaml       # offline: a reference endpoint and a quirky one
llm-bench conformance -c my-endpoint.yaml --formats json,md,junit
```

```text
Test                                reference  quirky
----------------------------------  ---------  ------
stream.usage                        PASS       FAIL
params.max_tokens                   PASS       FAIL
params.n                            PASS       FAIL
params.response_format.json_object  PASS       WARN
params.response_format.json_schema  PASS       FAIL
errors.invalid_key                  PASS       WARN
errors.unknown_model                PASS       FAIL
```

That excerpt is the in-process reference endpoint, once as documented and once with quirks
switched on. It is synthetic data, not any provider's results.

- **What WARN and FAIL mean.** An explicit 400 for an unsupported parameter is a WARN; silently
  ignoring it is a FAIL.
- **CI.** The exit code is 1 on any FAIL, so the suite works as a gate for your own server or
  gateway.

[docs/conformance.md](docs/conformance.md) lists every test, what passes, and how to read the
results.

## Supported providers

| Preset | What it is | How it was checked |
|---|---|---|
| `openai-compatible` | Any endpoint with `POST {base_url}/chat/completions` in the OpenAI format | In CI, against in-process fixtures, a real local HTTP server and the MolochAI mock server |
| `molochai` | [MolochAI](https://molochai.dev/?utm_source=github&utm_medium=oss&utm_campaign=llm-api-benchmark), with its documented behaviors built in | Against the public docs and the official mock server in CI (reasoning, keep-alive and queue comments, usage chunk, in-stream errors, error shapes), and an unauthenticated request to the live API. A keyed live run is the manual [live workflow](.github/workflows/live.yml). |
| `synthetic` | A simulated endpoint for demos and tests | Not a provider. Its results are always labeled synthetic. |

Other providers work through `openai-compatible` with their own `base_url`. The maintainers have
not verified them. [docs/providers.md](docs/providers.md) covers the settings that differ between
"compatible" APIs, such as `max_completion_tokens`, header-based keys, `api-version` query
parameters and local servers without auth. It also explains how to add an adapter for a
different wire format.

## Metrics

| Metric | Meaning |
|---|---|
| **TTFT** | Request sent → first streamed chunk with text (reasoning or answer). Stream mode only. |
| **TTFC** | Request sent → first chunk with answer text. It differs from TTFT for reasoning models. |
| **Latency** | Request sent → last byte. Includes DNS, TLS on new connections, queueing and generation. |
| **Out tok/s** | `completion_tokens / latency`: end-to-end output speed. |
| **Decode tok/s** | `(completion_tokens - 1) / (last text chunk - first text chunk)`: speed once text flows. |
| **Error rate** | Failed / sent, by type. Skipped requests are listed with the reason. |
| **Cost** | From the provider's token counts and your prices. Shown only when both are known. |
| **Checks** | Share of replies that pass the prompt's deterministic checks. |
| **Called a tool** | Tool workloads: share of successful replies with at least one tool call. |
| **Same calls** | Tool workloads: for each prompt, the share of repetitions that make the most common set of calls (same functions, same parsed arguments), averaged over prompts. |

APIs stream chunks, not individual tokens, so TTFT is "first chunk with output". A tool-call
fragment counts as output and as the start of the answer. Token counts
come from the provider's `usage`; when it is missing they are estimated at 4 characters per token
and marked `~`.

## Methodology

In short:

- The plan is fixed before the first request.
- Each repetition is shuffled with a fixed seed, so endpoints share the same time window.
- Warm-up requests are excluded from statistics.
- Connections are kept alive.
- Nothing is retried.
- Workloads are never pooled into a single "speed" number.
- Comparisons show uncertainty instead of declaring a winner.

The full definitions, stopping rules, budget algorithm, statistics and known limitations are in
[docs/methodology.md](docs/methodology.md). How this compares with llmperf, AIPerf, GuideLLM and
others is in [docs/related-tools.md](docs/related-tools.md).

To keep a comparison fair:

- Run both endpoints from one config file, on one machine, at one time.
- Use the same temperature and the same dataset version.
- Get enough samples: 10 or more per group for medians, 20 or more for P95.
- Check `completion_tokens` before you compare latency. Some providers ignore `max_tokens`.

## Configuration

The most used keys are below. The complete reference is
[docs/configuration.md](docs/configuration.md).

| Key | Default | |
|---|---|---|
| `dataset` | `core-v1` | Built-in name or a path to your own YAML |
| `workloads` | all | Subset, e.g. `[short-answer, long-response]` |
| `modes` | `[stream]` | `stream`, `plain` or both |
| `repetitions` / `warmup` | 3 / 1 | Per prompt / per endpoint |
| `concurrency` | 1 | Up to 8 |
| `timeout_s` | 120 | Total per request |
| `max_requests` | 100 | Hard cap on the plan |
| `budget` | none | USD (or `{limit, currency}`); needs `pricing` on every endpoint |
| `temperature` | not sent | Set it explicitly for comparisons |
| `providers[].preset` | `openai-compatible` | `molochai`, `synthetic` |
| `providers[].base_url`, `model` | | `${VAR}` and `${VAR:-default}` are expanded |
| `providers[].api_key_env` | | Name of the environment variable with the key |
| `providers[].rate_limit_rpm` | none | The provider's published limit |
| `providers[].pricing` | none | `input_per_mtok`, `output_per_mtok`, `currency`, `source`, `checked_on` |

## Commands

| Command | What it does |
|---|---|
| `llm-bench conformance -c FILE` | Run the OpenAI compatibility tests against each endpoint. Options: `--list`, `--only`, `--skip`, `--providers`, `--dry-run`, `--yes`, `--formats json,md,junit`, `--fail-on fail\|warn\|never`. |
| `llm-bench run -c FILE` | Run a benchmark. Options: `--dry-run`, `--yes`, `--out-dir`, `--formats`, `--dataset`, `--providers`, `--workloads`, `--modes`, `--repetitions`, `--warmup`, `--concurrency`, `--max-requests`, `--budget`, `--stop-at-budget`, `--quiet`. |
| `llm-bench providers` | List presets, how each was checked, and their notes. |
| `llm-bench datasets [NAME] [--prompts]` | List datasets, or show workloads, prompts and checks. |
| `llm-bench models --preset P` / `--base-url URL --api-key-env VAR` | List model ids (one `GET /models`). |
| `llm-bench report FILE --format table\|markdown\|html\|csv\|requests-csv\|json` | Render a results file. |
| `llm-bench compare A B [--provider-a X --provider-b Y]` | Compare two runs, or two endpoints of one run. |
| `llm-bench init [synthetic-demo\|molochai\|openai-compatible]` | Write a starter config. |

Exit codes:

- `0`: the run finished. Failed requests are measurements, not tool errors.
- `1`: a request needed by `models` failed.
- `2`: invalid configuration or refused plan.
- `130`: interrupted.

The result files are described in [docs/results.md](docs/results.md).

## Security

- Keys are read only from the environment variable that each endpoint names (`api_key_env`).
  Credential headers in a config file are rejected; use `headers_env` for extra secret headers.
- Terminal output shows at most the last four characters of a key.
- Result files contain only the variable name. URL credentials, key-like query values,
  bearer-token patterns and the registered keys themselves are redacted from every message, and
  error bodies are redacted too, in case a provider echoes the key back.
- Results can still reveal which endpoints and models you use, and when. Review them before you
  publish them.
- Report vulnerabilities privately ([SECURITY.md](SECURITY.md)).

## Troubleshooting

| Symptom | Likely cause and fix |
|---|---|
| `environment variable X is not set` | Export the key named by `api_key_env`. `--dry-run` shows which keys are set. |
| `The plan has N requests, more than max_requests` | Lower `repetitions`, `workloads` or `modes`, or raise `max_requests`. |
| `http_401` then `skipped: stopped after HTTP 401` | Wrong or revoked key. The endpoint is stopped on purpose. |
| `http_404` or `http_301` | Wrong `base_url`: it should end before `/chat/completions`, usually with `/v1`. |
| `http_400` / `http_422` on every request | A parameter the provider rejects. See [docs/providers.md](docs/providers.md#any-other-openai-compatible-endpoint). |
| `invalid_response: expected text/event-stream` | The endpoint does not stream. Use `modes: [plain]`. |
| Throughput marked `~` | The provider sent no `usage`. Try `stream_usage: true`, or accept the estimate. |
| `http_524` in plain mode | A proxy (for example Cloudflare) cut a long request. Use stream mode. |
| Replies much longer than `max_tokens` | The provider ignores it. Set `max_tokens_honored: false` and `assumed_max_output_tokens`. |
| `This run sends N requests. Add --yes` | Larger runs need confirmation. Check the plan with `--dry-run` first. |

## Contributing

Bug reports, provider configurations you have verified, and dataset proposals are welcome. See
[CONTRIBUTING.md](CONTRIBUTING.md) for the development setup. Tests run offline against fixtures
and the mock server. Do not submit benchmark results as claims about providers.

## About

This tool is maintained by MolochAI, which runs an
[OpenAI-compatible API for open-weight models](https://molochai.dev/?utm_source=github&utm_medium=oss&utm_campaign=llm-api-benchmark).
It is designed to be useful on its own, with any provider. It ships no performance numbers for
MolochAI or anyone else, and the `molochai` preset gets no special treatment in measurement or
reporting.

## License

[MIT](LICENSE)
