# Rollout Diff

Rollout Diff finds changes in generated code and prose across RL training steps. It reads a TRL or verl dump locally, ranks events for inspection, and links each event to examples in the original data. Ordinary analysis needs no GPU, model API, or trainer installation.

## Install

Use Python 3.11 or newer. The local investigation app and watch workflows require macOS or Linux. The wheel includes the web interface.

Install from the directory containing the wheel.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install ./rolloutdiff-0.1.0-py3-none-any.whl
rollout --help
```

The distribution and import name are `rolloutdiff`. The executable is `rollout`. For an index that carries 0.1.0, use `python -m pip install rolloutdiff==0.1.0`. From an unpacked source distribution, use `python -m pip install .`.

## Analyze a dump

```sh
rollout analyze /path/to/completions --format trl --run experiment-1 \
  --reward-column training_passed --output report.json
rollout render report.json --output report.html
```

Open `report.html` locally. The report shows how many series could be screened, which features changed, when they alerted, and which events ranked highest. If there is an event, inspect its selected responses using the same dump, run, and reward column.

```sh
rollout inspect /path/to/completions --format trl --run experiment-1 \
  --reward-column training_passed --report report.json --event-rank 1
```

Add `--with-absent` to inspect completions from the same run, step, and prompt where a binary feature is absent. This needs complete prompt groups. Reports store evidence and references. Raw response text stays in the source dump. Choose fresh output paths for reports.

| Format | Input | Required source columns |
| --- | --- | --- |
| `trl` | Trainer output, completions directory, or `completions_<step>.parquet` | `step`, `prompt`, `completion`, and `reward` or a named `--reward-column` |
| `verl` | Directory or `<step>.jsonl` / `step_<step>.jsonl`, optionally gzipped | `step`, `input`, `output`, `score` |

For verl use `--format verl` and omit `--reward-column`. Each file's step must agree with its name. Interpret the reward according to the producer's scoring function.

### Read the evidence

At each step, analysis averages completions within each exact prompt and weights prompts equally. Estimating a standard error needs at least two sampling units. Related prompt variants can share a sampling unit through the Python API. Sequential alerts use a 15-step baseline and three consecutive qualifying observations. Event rank is a heuristic for choosing what to inspect.

New analyses run sequential detection by default. Add `--retrospective` to `rollout analyze` or `rollout watch run`, or pass `retrospective=True` to `analyze_rollouts()`, to enable the experimental detector. It estimates a mean-shift boundary from the available series. Its original null-alert benchmark failed at 16/768 (2.08%) against a 0.5% ceiling.

Version-3 analysis reports record the detector policy and distinguish disabled analysis from a completed scan with zero changes. They require a current reader. Historical version-1 and version-2 reports retain their recorded evidence. The bundled benchmark describes historical trials and does not calibrate a new run.

The source distribution includes benchmark results, a data manifest, and offline reproduction instructions. Open `bench/README.md` inside `rolloutdiff-0.1.0.tar.gz`. To download that archive from an index, use `python -m pip download --no-deps --no-binary=rolloutdiff rolloutdiff==0.1.0`.

`--sensitivity lenient` selects an experimental profile for smaller increases in retained structural binary features. Its report shows default and experimental counts for the same cohort. Retrospective detection is a separate choice. Full-run vocabulary selection limits alert dates to offline analysis.

## Compare windows or trajectories

```sh
rollout diff /path/to/completions --format trl --run experiment-1 \
  --reward-column training_passed --a 80:100 --b 140:160 \
  --output diff.json --html diff.html
```

Ranges are inclusive and can overlap or appear in either order. To compare whole dumps, pass two paths. Differences are B minus A, with completions pooled within each exact prompt per side. The report shows prompt overlap, uncertainty, and citations for each side. Comparison inspection verifies source and response fingerprints.

For recorded conversations, use `--format openhands` for SWE-rebench, `--format swe-smith`, or `--format inspect`. Two unstepped dumps can be compared in full. SWE-smith files containing multiple models need an explicit `--model` for side A and `--other-model` for side B. OpenHands and SWE-smith accept JSON lists, JSONL, or Parquet. Inspect accepts one completed, text-only schema-v2 log per side. Rewards and scores require explicit selection. Missing steps and rewards stay unavailable.

```sh
rollout diff a.json b.json --format inspect --run run-a --other-run run-b \
  --tool-calls --output calls.json
rollout inspect a.json --format inspect --run run-a --report calls.json \
  --side a --feature tool_calls_count
```

`--tool-calls` compares recorded assistant requests by count, adjacent tool names, argument shape, path category, and command class. Citations resolve to original calls. A request's outcome needs separate evidence, and differences across models can reflect different tasks. Measuring change through agent training requires stepped data. Missing steps or rewards and tool-call comparisons use the version-2 comparison format.

Inspect JSON works with the base installation. To read native `.eval` files, install the optional `inspect-ai==0.3.290` reader in a fresh environment.

```sh
python3 -m venv .venv-inspect
.venv-inspect/bin/python -m pip install './rolloutdiff-0.1.0-py3-none-any.whl[inspect]'
.venv-inspect/bin/rollout diff --help
```

The equivalent index requirement is `'rolloutdiff[inspect]==0.1.0'`. The adapters read recorded logs without running tools or rescoring samples.

## Python adapters and extractors

`load_trl` and `load_verl` return canonical rows. To adapt a different stepped table, map canonical names to the columns of your pandas DataFrame, `frame`, with `from_table`. Preserve the exact prompt and response, a nonnegative integer step, finite reward, and a unique `(run, sample_id)`. Supply stable sample IDs if rows may be reordered. Prompt identity includes chat roles and metadata.

```python
from rolloutdiff import analyze_rollouts, extract, featurize, from_table

rows = from_table(frame, run="trial", columns={
    "step": "iteration", "prompt": "question", "response": "answer",
    "reward": "score", "sample_id": "completion_id",
})
sample = extract(rows.iloc[0].response)
print(sample.dense["n_code_blocks"], sorted(sample.sparse))
tables = featurize(rows)
print(tables.catalog[["feature", "tier", "kind"]])
analysis = analyze_rollouts(rows)
print(analysis.event_ranking)
```

`extract` reads Python syntax and prose from one response. `featurize` produces per-completion dense values, retained sparse features, and a catalog. `build_report(analysis)` and `render_report(report)` export an analysis. For unstepped inputs use `load_trajectories` or `load_inspect` and `compare_rollouts(a, b, include_tool_calls=True)`. Use `extract_tool_calls(tool_calls, response_messages)` to inspect one record's structured call features.

## Other workflows

- **Investigate locally.** `rollout investigate --root /path/to/data` opens the loopback app. Choose a TRL or verl dump to inspect ranked events or compare windows. Keep the session URL private. `--no-browser` prints the URL. Saved replay and intervention evidence can be viewed read-only.
- **Watch completed steps.** `rollout watch seal` checks a closed file against independently planned prompt-group counts. `rollout watch run` consumes marked files in order, waits for gaps, and resumes with the detector policy recorded in its private state. A supported legacy session continues with both detectors and needs the newer writer after it appends a step. Start a new state to change policy. `--once` processes one finite inventory. Inspect a saved commit against its own source snapshot. Event issuance is the first durable snapshot containing the event. Membership, representative, and rank can change in later snapshots. The timing check used recorded Aria steps. Full-prefix statistics are recomputed.
- **Connect a producer.** `AsyncRolloutProducer.submit` accepts complete, planned groups into a bounded queue. A receipt's `acknowledge()` waits for durable storage. `make_trl_callback` supports TRL 1.18.0 GRPO with Transformers 4.56.2, one writer on world rank zero, and a restricted full-generation logging configuration. `VerlCompletionLogger.bind(trainer)` replaces the verl 0.9.1 training dump writer with one designated publisher. `FixedProbeHook` needs a separate run, fixed prompts, and a caller-owned sampler. See `rollout watch --help` for configuration, rank, and recovery requirements. Playback checks used authored inputs. Live trainer overhead and distributed execution remain unmeasured.
- **Send a notification.** `rollout watch notify` sends a bounded summary of a durable snapshot to an explicitly supplied endpoint and records the attempt locally. Delivery has no automatic retry.
- **Review Aria replay evidence.** `rollout replay-aria --help` describes replay of one selected completion. `rollout investigate-aria --help` covers controlled interventions against frozen evidence. Replay needs the supported Docker setup, pinned artifacts and explicit authorization. Interventions require single-use approval.

## Development

Run the development checks from the source root in an activated Python virtual environment.

```sh
python -m pip install -c .github/ci-constraints.txt -e '.[test]' ruff
ruff format --check src bench tests scripts .github/*.py
ruff check src bench tests scripts .github/*.py
python -m pytest -q -m 'not local_data'
```

Frontend development uses Node 22.23.1. Run `npm ci --prefix frontend`, then `npm run --prefix frontend lint`, `npm run --prefix frontend typecheck`, `npm test --prefix frontend`, and `npm run --prefix frontend build`. The build updates the assets in the wheel. Browser tests use `npm run --prefix frontend test:e2e` with Playwright Chromium installed. Contributor instructions are in `CONTRIBUTING.md` in the source distribution.
