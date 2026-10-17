<div align="center">

# 🧪 PromptLab

**CI-first prompt & LLM regression testing — YAML suites, zero local setup**

[![License: MIT](https://img.shields.io/badge/License-MIT-7C3AED?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](pyproject.toml)
[![Tests](https://img.shields.io/badge/Tests-offline%20%2B%20echo-00C853?style=for-the-badge&logo=pytest&logoColor=white)](tests)
[![CI](https://img.shields.io/badge/Runs%20on-GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)](.github/workflows)

**Describe your prompt tests in YAML. GitHub Actions runs them on every PR — free, deterministic, no API keys.**

</div>

## Why PromptLab

Every AI app ships prompts, and almost nobody tests them. A "small" model swap or
tweak silently breaks behavior. promptfoo owns the JS world; Python devs get
PromptLab: **a lightweight, local-first, CI-native eval tool**.

- 🧪 **YAML suites** — prompts, variables, providers, assertions in one readable file
- 🔌 **Providers** — `echo` (offline/deterministic), `ollama`, any OpenAI-compatible API
- ✅ **12 built-in assertions** + `@register_assertion` plugin API (one-file PRs!)
- 📊 **Reports** — Markdown (PR comments), JSON, JUnit XML (GitHub checks UI)
- 🧮 **Baselines** — save a run, compare later, fail the build on regressions
- 🤖 **CI-first** — `promptlab init` writes the GitHub Actions workflow for you
- ⚖️ **Semantic judging** — an optional judge model grades free-form outputs

## Architecture

```
promptlab.yaml ──► Loader (pydantic validation)
                      │
                      ▼
                Runner ──► Provider (echo | ollama | openai_compat)
                 │            │  renders {{vars}}, caches completions
                 │            ▼
                 │         output ──► Assertions (builtin + plugins)
                 │
                 ├──► SuiteResult ──► Reports: markdown / json / junit
                 └──► BaselineStore ──► compare runs, fail on regressions

Interfaces: CLI (init · validate · run)
            GitHub Actions: ci.yml · eval.yml · nightly.yml · action.yml
```

Server/API keys are only needed for real models — and even those can run on
GitHub's machines (see **Nightly** below). Your laptop is optional.

## Quick Start

```bash
pip install -e .

# Scaffold a suite + the GitHub Actions workflow
promptlab init

# Check the suite is valid (fast, CI-safe)
promptlab validate promptlab.yaml

# Run it locally to see reports
promptlab run promptlab.yaml --format markdown
```

### Suite format

```yaml
providers:
  - id: echo
    type: echo

prompts:
  - "Translate to French: {{text}}"

defaults:
  vars:
    text: "Hello, world!"

tests:
  - description: translation behaves
    assert:
      - contains: "Bonjour"
      - not_contains: ["Hello"]
      - regex: "^Bonjour"
      - length: [1, 400]
      - latency_ms: 3000
      - json_schema: { type: object }
      - semantic: "the reply is a polite French greeting"   # needs a judge model
```

## Running in GitHub Actions

**That's the default.** `promptlab init` drops `.github/workflows/promptlab.yml`
into your repo; on every PR it validates the suite, runs the tests, uploads a
JUnit report, and fails the PR on regressions. With the `echo` provider it needs
**no keys and no model**.

Use this repo from any other repository via the reusable Action:

```yaml
- uses: kamalesh404/promptlab@v0
  with:
    suite: promptlab.yaml
    compare-baseline: baseline   # optional regression gate
```

### Nightly real-model evals (still zero laptop time)

`.github/workflows/nightly.yml` installs **Ollama on the GitHub runner**, pulls
`qwen2.5:0.5b`, runs the suite against a real model, compares against the
committed baseline, and archives the report as an artifact:

```yaml
on:
  schedule:
    - cron: "0 3 * * *"
```

Prefer hosted APIs? Add `openai_compat` with an `api_key` from repo secrets —
still runs on GitHub.

### Baselines

```bash
promptlab run promptlab.yaml --save-baseline baseline
git add .promptlab/baseline.json && git commit -m "update prompt baseline"

# Later / in CI:
promptlab run promptlab.yaml --compare-baseline baseline
# exit 1 if any test that passed before now fails; fixes & new tests are listed too
```

## CLI Reference

| Command | Purpose |
|---|---|
| `promptlab init [path]` | Scaffold a starter suite + CI workflow |
| `promptlab validate <suite>` | Schema-validate a suite (use in CI) |
| `promptlab run <suite>` | Execute the suite, print a report, exit 1 on failure |
| `--format markdown\|json\|junit` | Choose the report format |
| `--output <file>` | Write the report to a file |
| `--save-baseline <name>` | Persist the run for future comparison |
| `--compare-baseline <name>` | Diff against a saved baseline; fail on regressions |

## Providers

| Provider | Cost | Notes |
|---|---|---|
| `echo` | Free | Deterministic; ideal for CI and examples |
| `ollama` | Free | Any local model; used by the nightly workflow |
| `openai_compat` | API key | OpenAI, DeepSeek, Groq, Together, LM Studio |

## Built-in Assertions

| Assertion | Args | Checks |
|---|---|---|
| `contains` | str or list | output contains every string |
| `not_contains` | str or list | output contains none of them |
| `equals` | str | exact (trimmed) match |
| `starts_with` / `ends_with` | str | prefix / suffix |
| `regex` | str | `re.search` match |
| `length` | int or [min, max] | output length bounds |
| `not_empty` | true | non-blank output |
| `is_valid_json` | true | parses as JSON |
| `json_schema` | dict | minimal JSON-schema subset (type/properties/required/items) |
| `semantic` | str | LLM-graded criterion (configure `defaults.judge`) |
| `latency_ms` | int | completion time budget |

## Testing

```bash
pytest   # 105 offline tests — echo provider, no network, no keys
```

## Contributing

PromptLab is built for tiny, focused PRs:

- **New assertion** = one function + `@register_assertion("name")` — see `src/promptlab/asserts/builtin.py`
- **New provider** = one class + `@register_provider("name")` — see `src/promptlab/providers/`
- Ideas welcome: HTML report, cost assertions, CSV dataset import, pytest plugin

See [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

## License

MIT — see [LICENSE](LICENSE)

<div align="center">
<b>Built by <a href="https://github.com/kamalesh404">Kamalesh</a></b>
</div>
