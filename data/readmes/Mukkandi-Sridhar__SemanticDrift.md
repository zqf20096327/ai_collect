# SemanticDrift

**Does rewording an agent's tool descriptions change which model looks best?**
A pre-registered study on the MCP tools of [IBM AssetOpsBench](https://github.com/IBM/AssetOpsBench),
using wording changes that the benchmark's own developers made during 2026.

[![Tests](https://github.com/Mukkandi-Sridhar/SemanticDrift/actions/workflows/tests.yml/badge.svg)](https://github.com/Mukkandi-Sridhar/SemanticDrift/actions/workflows/tests.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)

![Model rank under each description catalog](figures/fig1_rankings.png)

## Key findings

We gave 10 models from 6 providers the same 36 AssetOpsBench tools and 152 requests, and changed
only the tool descriptions. That makes 38,304 tool-selection decisions in total.

- **Aggregate accuracy hardly moves.** No accuracy difference between the original catalog and any
  rewritten catalog survives correction for multiple comparisons.
- **The leaderboard does move.** Under an identical copy of the catalog (our placebo), the top
  model stays the same. Under 6 of the 7 rewritten catalogs, the top model changes or becomes tied
  (mostly between Claude Sonnet 5.5 and GPT-6.1 Terra, which differ by 3 of 152 tasks on the
  original catalog).
- **Individual decisions move beyond run-to-run noise.** For 24 of 70 model × catalog pairs, more
  decisions change than under the placebo (95% CI above zero), mostly for four smaller models
  (Claude Haiku 5.5, Gemini 3.1 Flash-Lite, GPT-6 Luna, Mistral Small 4) and by a few points.
  Every kind of edit does this: paraphrases, scope changes and the real AssetOpsBench revisions.
  On the 55 tasks whose tools have a history, the paraphrases move decisions about as much as the
  developers' own edits.
- **Whether an edit is harmless is hard to tell in advance.** Two LLM judges agree that 29 of the
  32 real edits change meaning, but they split on about half of the paraphrases, and the
  paraphrases they both accept move decisions about as much as the rest.
- **Some small models act when they should ask.** On 24 requests that need a human decision,
  GPT-6 Luna chose a write tool (create, close or cancel a work order) 18–25% of the time; frontier
  models stayed near 0–4%.

The full results, with sources for every number, are in [`research/FINDINGS.md`](research/FINDINGS.md).
For a concrete case, see [one request under all nine catalogs](docs/example.md).

## What's in this repository

| Path | Contents |
|---|---|
| `datasets/tools/` | The 36 tools (29 read, 7 write) and the 9 description catalogs |
| `datasets/history/` | 42 earlier, developer-written descriptions recovered from AssetOpsBench's git history |
| `datasets/tasks/` | 152 requests with gold labels (103 single-tool, 49 that need no tool) |
| `src/semdrift/` | Extraction, request building, the experiment runner, scoring, analysis and figures |
| `configs/` | Models, prices, reasoning settings and run configuration |
| `results/` | Processed scores and analysis (raw responses are archived separately) |
| `research/` | Pre-registration, design, findings notebook, decision log |
| `docs/` | A worked example, and the original June 2026 proposal in `docs/history/` |

## Quick start

Requires Python 3.11 or newer. The harness uses only the standard library.

```bash
git clone https://github.com/Mukkandi-Sridhar/SemanticDrift && cd SemanticDrift
git clone https://github.com/IBM/AssetOpsBench vendor/AssetOpsBench
git -C vendor/AssetOpsBench checkout 0d044061ab3ffd4b213ddf6a0868c360d7e9667c

make check     # validate the dataset and run the tests
make figures   # redraw the figures (needs matplotlib: pip install -r requirements.txt)
```

## The dataset

**Tools.** Names, descriptions and input schemas are extracted statically from four AssetOpsBench
MCP servers (`iot`, `utilities`, `fmsr`, `wo`) at commit `0d04406`. Nothing from upstream is
imported or executed.

**Catalogs.** Every catalog keeps the same tool names, order and schemas; only description text
differs.

| ID | Catalog | How it was made |
|---|---|---|
| V0 | Original | Upstream, verbatim |
| V0R | Placebo | Byte-identical copy of V0 (measures run-to-run noise) |
| P1–P3 | Paraphrases | Meaning-preserving rewrites; the 15 riskiest were checked by hand |
| MG | Vaguer | Scope widened, parameter docs unchanged |
| MS | Narrower | One plausible narrowing per tool |
| H1 | Historical, earliest | Each tool's oldest description in the git history with an identical schema |
| H3 | Historical, previous | Each tool's last description before V0 |

**Tasks.** 103 requests have exactly one correct tool; 49 should get a text reply instead
(20 easy, 24 "tempting" requests that resemble a write action but need a human decision, and
5 out of scope). Provenance and checks are described in `datasets/tasks/SOURCES.md` and
`research/03-dataset/`.

## How the study was run

The hypotheses, metrics and analysis were fixed before any data was collected
([`research/PREREG.md`](research/PREREG.md)). Every later change is listed there with its date and
reason.

- Each request goes to each model once per catalog and repeat. The first action counts: a tool
  call or a text reply. No tool is ever executed.
- Models use their lowest available reasoning setting, the provider's default temperature, and a
  fixed system prompt. Each OpenRouter model is pinned to one host.
- Tool order is shuffled per repeat and shared by all models and catalogs.
- Nine models ran three repeats; Gemini 4 Argon ran one (budget).

| | |
|---|---|
| Models | GPT-6 Luna, GPT-6.1 Terra, GPT-6.2 Sol, Claude Haiku 5.5, Claude Sonnet 5.5, Gemini 3.1 Flash-Lite, Gemini 4 Argon, DeepSeek V4.1 Flash, Qwen 3.8 27B, Mistral Small 4 |
| Decisions | 38,304, run on 2026-11-25 |
| API cost | ≈ $36 (OpenRouter $29.93, OpenAI ≈ $6.25) |

To rerun the experiment you need OpenAI and OpenRouter API keys in a `.env` file
(see `.env.example`) and the steps in [`research/RUNBOOK.md`](research/RUNBOOK.md).

## Limitations

- Each trial is a single first action, not a full multi-step agent run.
- The tools come from one benchmark and one domain (industrial maintenance).
- The paraphrases were written by a language model. Two LLM judges agree that 15–19 of 36 per
  catalog are fully equivalent; the rest are borderline or, rarely, changed. The historical
  catalogs are human-written.
- The effects are small per decision. Their importance lies in how they change rankings and
  safety-relevant actions, not in average accuracy.
- Several ranking changes involve models whose accuracy differs by only a few tasks.

## Citation

If you use this work, please cite it as described in [`CITATION.cff`](CITATION.cff).

## Acknowledgements

The tools, descriptions and historical versions come from
[IBM AssetOpsBench](https://github.com/IBM/AssetOpsBench) (Apache-2.0); see
`datasets/tools/LICENSE.AssetOpsBench` and `datasets/tools/SOURCE.md`.

## License

[CC BY 4.0](LICENSE). Material derived from AssetOpsBench keeps its Apache-2.0 license.
