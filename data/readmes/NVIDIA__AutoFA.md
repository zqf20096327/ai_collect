<div align="center">

<h1>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/NVIDIA/AutoFA/main/img/autofa-logo-dark.svg">
    <img src="https://raw.githubusercontent.com/NVIDIA/AutoFA/main/img/autofa-logo.svg" alt="NVIDIA AutoFA" width="420">
  </picture>
</h1>

**Automated failure analysis for models and agent harnesses.**

[![NVIDIA](https://img.shields.io/badge/NVIDIA-76B900?logo=nvidia&logoColor=white)](https://www.nvidia.com/)
[![License](https://img.shields.io/badge/license-Apache--2.0%20%7C%20CC--BY--4.0-blue)](https://github.com/NVIDIA/AutoFA/blob/main/LICENSE)
[![Agents](https://img.shields.io/badge/runs%20with-Claude%20Code%20%7C%20Codex-76B900)](#quick-start)

[Quick start](#quick-start) · [Workflows](#workflows) · [Documentation](#documentation) · [Tutorial](https://github.com/NVIDIA/AutoFA/blob/main/eval_data/README.md) · [Contributing](https://github.com/NVIDIA/AutoFA/blob/main/CONTRIBUTING.md)

</div>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/NVIDIA/AutoFA/main/img/welcome_screen-dark.png">
    <img src="https://raw.githubusercontent.com/NVIDIA/AutoFA/main/img/welcome_screen.png" alt="AutoFA home menu in the terminal" width="900">
  </picture>
</p>

A reward tells you *that* an agent failed, not *why*. AutoFA is a toolkit for
reading completed evaluation runs (local **NeMo Gym** and **Harbor** folders or remote
**EvalRDL** runs) and explaining their failures from complementary angles: bottom-up
discovery and top-down taxonomy classification run in parallel on the same data.
It lets you:

- **Screen first:** run preflight checks that flag rollouts where the agent gamed the evaluation.
- **Discover (bottom-up):** let Claude Code or Codex mine the traces for recurring failure
  mechanisms, write reusable Python detectors, and measure their coverage and supporting evidence.
- **Classify (top-down):** label every failed rollout with one mode from a fixed taxonomy using
  an LLM or agentic judge, separating model faults from harness faults.
- **Measure:** alongside or after discovery, compare tokens, context, turns, tool use and cost
  between correct and incorrect rollouts.
- **Explore and share:** browse failure cards, source traces and highlighted evidence in a local
  library, then publish detectors and reuse them on new runs.
- **Delegate:** describe the goal to your coding agent and let the bundled
  [driver skill](https://github.com/NVIDIA/AutoFA/blob/main/agent-skills/autofa-driver/SKILL.md) set up, launch, monitor and explain the work.

### Two lenses, one picture

Discovery and taxonomy classification answer different questions and work best together.

| | Failure discovery | Taxonomy classification |
|---|---|---|
| **Direction** | Bottom-up: patterns emerge from the data | Top-down: failures are mapped onto known categories |
| **Question** | *What keeps going wrong in this run?* | *How are failures distributed across known modes?* |
| **Output** | Reusable Python detectors with coverage and evidence | One failure mode per rollout, with cited events |
| **Best for** | New benchmarks, unknown mechanisms, regression detectors | Comparable breakdowns across models, harnesses and runs |

Use a taxonomy bucket as the starting cohort for
[discovery](https://github.com/NVIDIA/AutoFA/blob/main/docs/taxonomy-classification.md#continue-with-failure-discovery) to dig into one
category, and let discovery surface mechanisms that no taxonomy anticipated.

## Quick start

Want to try AutoFA but do not have evaluation logs? The repository includes three example
LiveCodeBench runs for `thinkingmachines/Inkling-Small`, `zai-org/GLM-5.3-Flash` and
`nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16`. Follow the
[example reports and bundled-data tutorial](https://github.com/NVIDIA/AutoFA/blob/main/eval_data/README.md) to browse their
ready-made analyses without running AutoFA, or run AutoFA yourself on the included
rollout archives.

You need [`uv`](https://docs.astral.sh/uv/getting-started/installation/) and a signed-in
[Claude Code](https://code.claude.com/docs/en/quickstart) or
[Codex CLI](https://developers.openai.com/codex/cli/). Clone the repository:

```bash
git clone https://github.com/NVIDIA/AutoFA.git
cd AutoFA
```

Then choose **one** of the following ways to use it.

### Option A: ask your coding agent (recommended)

Open the checkout in Claude Code or Codex and describe what you want:

```text
Read AGENTS.md, set up AutoFA, and analyze these runs: <links or paths>.
Aim for eight supported failure modes with high combined recall by end of day.
```

The agent installs AutoFA, asks before installing optional readers such as LibreOffice or
audio and video support, registers the `autofa-driver` skill and continues as your
analysis driver: it helps choose models and effort, picks the right workflow, monitors
progress, and summarizes findings with suggested next steps. Leave out the analysis goal
to set up only. Later, invoke the skill directly with `/autofa-driver` in Claude Code or
`$autofa-driver` in Codex. See [agent setup](https://github.com/NVIDIA/AutoFA/blob/main/docs/agent-setup.md) and
[operating AutoFA through the driver](https://github.com/NVIDIA/AutoFA/blob/main/docs/driver-supervision.md) for monitoring, stopping
and cost reporting.

### Option B: run it yourself

Install the environment and open the interactive home menu:

```bash
uv sync --python 3.12 --inexact
uv run --no-sync autofa
```

Choose **New analysis** for discovery (with optional efficiency metrics and preflight
checks), **Classify failures by taxonomy** for top-down labelling, or
**Explore failure library** to browse saved results. For unattended or reproducible runs,
describe the whole job in a YAML file and use
[batch mode](https://github.com/NVIDIA/AutoFA/blob/main/docs/workflows.md#batch-runs):

```bash
uv run --no-sync autofa run --config examples/run-configs/frontier-23859c40d27a4c84.yaml
```

LLM judges and LLM detectors use an OpenAI-compatible endpoint that you configure
under **Settings > LLM endpoints**; if it needs a key, store it as `LLM_API_KEY` in the project `.env`.
See [LLM endpoints](https://github.com/NVIDIA/AutoFA/blob/main/docs/llm-endpoints.md) and [configuration](https://github.com/NVIDIA/AutoFA/blob/main/docs/configuration.md).

### See the results

AutoFA starts a local dashboard automatically. Open the **Library** link it prints
(default <http://127.0.0.1:8765>) to browse failure cards, source traces and reports.
See the [failure library guide](https://github.com/NVIDIA/AutoFA/blob/main/docs/library.md) for saving, publishing and reusing results.
Results persist under `~/.autofa/`.

## Workflows

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/NVIDIA/AutoFA/main/img/autofa-overview-dark.svg">
    <img src="https://raw.githubusercontent.com/NVIDIA/AutoFA/main/img/autofa-overview.svg" alt="AutoFA overview: NeMo Gym, Harbor and EvalRDL runs pass optional preflight cheating checks, then two complementary workflows run in parallel: top-down taxonomy classification and bottom-up failure discovery (with optional efficiency metrics); optionally, one taxonomy category can be explored further with failure discovery. Results land in a browsable failure library, and a coding agent can drive every workflow." width="900">
  </picture>
</p>

| Workflow | What it answers | Start it with | Guide |
|---|---|---|---|
| **Preflight check: cheating** (runs first) | Did the agent look up the answer or tamper with the grader? | `autofa preflight cheating` | [Preflight cheating checks](https://github.com/NVIDIA/AutoFA/blob/main/docs/cheating-check.md) |
| **Failure discovery** | Which recurring mechanisms cause failures, and how many rollouts does each explain? | **New analysis**, `autofa run` | [Running an analysis](https://github.com/NVIDIA/AutoFA/blob/main/docs/workflows.md) · [Detectors](https://github.com/NVIDIA/AutoFA/blob/main/docs/detectors.md) |
| **Efficiency metrics** (alongside or after discovery) | How do correct and incorrect rollouts differ in tokens, context, turns, tools and cost? | **Analysis settings > Analyses to run** | [Efficiency metrics](https://github.com/NVIDIA/AutoFA/blob/main/docs/efficiency.md) |
| **Taxonomy classification** | Which known failure mode does each failed rollout belong to? | **Classify failures by taxonomy**, `autofa classify` | [Taxonomy classification](https://github.com/NVIDIA/AutoFA/blob/main/docs/taxonomy-classification.md) |

## Documentation

| Topic | Guide |
|---|---|
| Terms used throughout AutoFA | [Glossary](https://github.com/NVIDIA/AutoFA/blob/main/docs/glossary.md) |
| Agent-driven setup and operation | [Agent setup](https://github.com/NVIDIA/AutoFA/blob/main/docs/agent-setup.md) · [Driver supervision](https://github.com/NVIDIA/AutoFA/blob/main/docs/driver-supervision.md) · [Driver skill](https://github.com/NVIDIA/AutoFA/blob/main/agent-skills/autofa-driver/SKILL.md) |
| Sessions, resume, batch runs and unattended discovery | [Running an analysis](https://github.com/NVIDIA/AutoFA/blob/main/docs/workflows.md) |
| Inputs: local NeMo Gym / Harbor and remote EvalRDL | [Datasets and rollout selection](https://github.com/NVIDIA/AutoFA/blob/main/docs/datasets.md) · [Local imports and traces](https://github.com/NVIDIA/AutoFA/blob/main/docs/local-traces.md) |
| Models, endpoints, analysis settings and skills | [Configuration](https://github.com/NVIDIA/AutoFA/blob/main/docs/configuration.md) · [LLM endpoints](https://github.com/NVIDIA/AutoFA/blob/main/docs/llm-endpoints.md) |
| Writing, validating and scoring detectors | [Detectors](https://github.com/NVIDIA/AutoFA/blob/main/docs/detectors.md) · [Metrics and feedback](https://github.com/NVIDIA/AutoFA/blob/main/docs/metrics.md) |
| Office rendering, audio, video and speech readers | [Artifact inspection dependencies](https://github.com/NVIDIA/AutoFA/blob/main/docs/artifact-dependencies.md) |
| Reports, saved libraries, publishing and storage | [Failure library and saved results](https://github.com/NVIDIA/AutoFA/blob/main/docs/library.md) |
| Token usage, spend and projections | [Usage and cost accounting](https://github.com/NVIDIA/AutoFA/blob/main/docs/usage-accounting.md) |

## Known limitations

> [!IMPORTANT]
> **Research preview**
>
> AutoFA is in research preview and is not yet ready for production use. Its code,
> configuration and output formats may change without backward compatibility.
> Findings are produced by AI agents and may be incomplete or inaccurate; review them
> before acting on them.

- Discovery and model-based judging need your own model access, and the selected trace
  content is sent to the providers you configure.
- The Library server uses a shared profile: anyone holding its token can read and modify
  that profile's libraries. Detector execution is not an operating-system sandbox.
  See [SECURITY.md](https://github.com/NVIDIA/AutoFA/blob/main/SECURITY.md).
- Initial reading of local runs holds the run in memory, so very large rollouts or expanded
  request histories can exceed the hydration batch budget. Supplying missing metadata
  labels currently rereads the original logs.
- AutoFA installs no audio or video codecs, FFmpeg, PyAV or LibreOffice. Its dependencies
  do include image codecs: Pillow and pypdfium2 read formats such as JPEG, PNG, GIF, TIFF,
  WebP, AVIF and JPEG 2000. Office rendering and audio and video inspection need readers
  that you install as described in
  [artifact inspection dependencies](https://github.com/NVIDIA/AutoFA/blob/main/docs/artifact-dependencies.md); a setup agent asks
  before installing them. Without them, Office page images and audio and video content are
  reported unavailable.

## Support and contributing

Report bugs, feature requests and documentation questions through
[GitHub Issues](https://github.com/NVIDIA/AutoFA/issues), with a minimal reproduction using
synthetic or otherwise authorized data. Release notes are published on
[GitHub Releases](https://github.com/NVIDIA/AutoFA/releases).

Bug fixes, documentation corrections and tests are welcome; for anything else, open an issue
and agree the approach with a maintainer first. Read [CONTRIBUTING.md](https://github.com/NVIDIA/AutoFA/blob/main/CONTRIBUTING.md) for the
[contribution scope](https://github.com/NVIDIA/AutoFA/blob/main/CONTRIBUTING.md#contribution-scope),
[DCO sign-off](https://github.com/NVIDIA/AutoFA/blob/main/CONTRIBUTING.md#developer-certificate-of-origin) and
[maintainers](https://github.com/NVIDIA/AutoFA/blob/main/CONTRIBUTING.md#maintainers-and-code-ownership). Participation follows the
[Code of Conduct](https://github.com/NVIDIA/AutoFA/blob/main/CODE_OF_CONDUCT.md).

## Security

Report vulnerabilities privately through the channels in [SECURITY.md](https://github.com/NVIDIA/AutoFA/blob/main/SECURITY.md). Keep
credentials, private traces and personal information out of public issues and pull requests.

## License

AutoFA is released under **CC-BY-4.0 AND Apache-2.0**: code-only files are Apache-2.0, while
documentation, prompts, skills and assets follow the dual-license terms in [LICENSE](https://github.com/NVIDIA/AutoFA/blob/main/LICENSE).
Third-party material keeps its own terms, recorded in
[THIRD_PARTY_NOTICES.md](https://github.com/NVIDIA/AutoFA/blob/main/THIRD_PARTY_NOTICES.md).
