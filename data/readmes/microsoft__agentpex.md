# AgentPex — Trace import and evaluation

AgentPex imports agent traces from various formats and evaluates them against specifications extracted from system prompts and tool schemas.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Entrypoints

| Entrypoint | Purpose |
|------------|---------|
| `src/import_traces.py` | Import traces from JSON (standard, tau-sq, or Langfuse) into an artifact directory with specification extraction and augmentation. |
| `src/cli.py` | Run evaluation on existing artifact directories (e.g. after import). |
| `agentpex` + `agentpex.platforms.langfuse` | **Langfuse**: convert client-fetched traces with `import_traces()`, run `evaluate()` |
| `src/integrations/langfuse_eval.py` | **Optional**: standalone script that fetches traces from Langfuse (requires env credentials), runs evaluation, and pushes scores. |
| `src/integrations/langtrace_eval.py` | **Langtrace integration**: fetch traces from Langtrace, run AgentPex evaluation, and push scores back to the Langtrace dashboard. |


## Quick start

**1. Import traces**

```bash
cd src
python import_traces.py /path/to/traces.json [--tau-sq]
```

This creates `artifacts/<name>-<hash>-<timestamp>/` with analysis files (output spec, transition spec, forbidden edges), per-trace `test_run_<id>.json`, and augmentation (plan, init_state, fini_state).

**2. Evaluate**

```bash
python cli.py --skip-sample --gen-eval --input-test-result <artifact_id>
```

Or use the same artifact directory path for `--input-test-result`. Evaluation runs the LLM-judged evaluators and writes `test_eval_*.json` and summary reports.

**3. Smoke test**

Run the end-to-end smoke test to verify your setup. This imports a sample trace, runs all 8 evaluators, and prints scores:

```bash
./scripts/run_smoke_test.sh
```

The script uses `examples/sample_trace.json` (a minimal weather assistant trace) and requires a configured `.env` file. For a quick start with Ollama:

```bash
cp src/.env.ollama .env
./scripts/run_smoke_test.sh
```

## Model configuration (environment variables)

Set LLM provider and model with variables in the form `provider:model` or `provider:model:temperature`. Required for import and evaluation:

| Variable | Purpose | Default |
|----------|---------|---------|
| `DEFAULT_LLM` | Fallback for any unspecified component | Required |
| `PLAN_GEN_LLM` | Plan generation (augmentation) | `DEFAULT_LLM` |
| `OUTPUT_SPEC_*_LLM` | Output spec extraction / validation | `DEFAULT_LLM` |
| `TRANSITION_SPEC_*_LLM` | Transition spec extraction / validation | `DEFAULT_LLM` |
| `*_EVAL_LLM` (e.g. `OUTPUT_SPEC_EVAL_LLM`) | Per-evaluator model overrides | `DEFAULT_LLM` |
| `TRACE_CHECKER_LLM` | Trace-level evaluation / checker | `DEFAULT_LLM` |
| `FINAL_STATE_VALIDATOR_LLM` | Fini state validation | `DEFAULT_LLM` |

Supported providers: `openai:`, `azure:`, `ollama:` (OpenAI-compatible endpoints).

Example:

```bash
export DEFAULT_LLM="openai:gpt-4o"
export PLAN_GEN_LLM="openai:gpt-4o-mini"
```

## Langfuse integration

You can evaluate traces that happen to come from [Langfuse](https://langfuse.com) (or anywhere).

Install and use the package:

```bash
pip install -e .
```

```python
from agentpex import evaluate
from agentpex.platforms.langfuse import import_traces

# 1. Fetch traces yourself (e.g. with Langfuse SDK and your own credentials)
#    traces = langfuse.api.trace.list(limit=50)   # or trace.get(id)

# 2. Convert to AgentPex test_run format (no API call inside import_traces)
test_runs, system_prompt, tools = import_traces(traces)  # optional: langfuse_client=client for traces missing input/output

# 3. Run evaluation; each result includes "scores" with names like AgentPex/plan_eval
results = evaluate(test_runs, score_name_prefix="AgentPex")
for r in results:
    for s in r.get("scores", []):
        print(s["name"], s["value"])  # e.g. AgentPex/plan_eval 85
        # Push to Langfuse from your code if you want (using your Langfuse client)
```


**Expected trace format for `import_traces(traces, ...)`**

`import_traces` does not call the Langfuse API. It expects a list of trace objects you already have. Each trace can be:

- **Langfuse SDK object** — e.g. from `langfuse.api.trace.list()` or `trace.get(id)`, with `id` or `trace_id`, and optionally `input` and `output`.
- **Plain dict** — keys `id` or `trace_id`, and optionally `input`, `output`.

`input` / `output` can be: a string; a list of message dicts (`role`, `content`); or a single message dict. If a trace has no top-level `input`/`output`, you can pass `langfuse_client` so the converter can fetch that trace (or its observations) to derive messages, system prompt, and tools.

**Evaluation behavior**

Traces that are plain input/output (no precomputed plan or output spec) still get scores from techniques that don’t require those (e.g. arg_spec_eval, arg_groundedness_eval, and the gated-min aggregate). For full evaluation with plan/output_spec/fini_state, use traces that include message lists and metadata that map to those fields, or import via `import_traces.py` (e.g. tau-sq) and use the CLI.

### Optional: standalone script (fetches and pushes; needs Langfuse env)

If you prefer a script that fetches from Langfuse and pushes scores back, use `src/integrations/langfuse_eval.py`. **Only this path** needs Langfuse environment variables:

```bash
export LANGFUSE_PUBLIC_KEY="pk-lf-..."
export LANGFUSE_SECRET_KEY="sk-lf-..."
export LANGFUSE_HOST="https://cloud.langfuse.com"   
python src/integrations/langfuse_eval.py --hours-back 24 --limit 100
```

Or programmatically (with `src` on `PYTHONPATH`): `LangfusePexEvaluator().run_evaluation(hours_back=12, limit=50, metric_name_prefix="AgentPex")`. That script fetches traces, runs evaluation, and pushes scores to Langfuse.

## Langtrace integration

You can run the AgentPex evaluator on traces stored in [Langtrace](https://langtrace.ai) and have scores pushed back to the Langtrace dashboard.

**1. Install and set credentials**

```bash
pip install -r requirements.txt   # includes langtrace-python-sdk
export LANGTRACE_API_KEY="<your-api-key>"
export LANGTRACE_PROJECT_ID="<your-project-id>"
export LANGTRACE_API_HOST="https://app.langtrace.ai"   # optional, default
```

**2. Run evaluation on recent traces**

```bash
python src/integrations/langtrace_eval.py --limit 100
```

Or from `src` with `PYTHONPATH=.: python -m integrations.langtrace_eval --limit 100`.

Or programmatically (with `src` on `PYTHONPATH`):

```python
from integrations.langtrace_eval import LangtracePexEvaluator

evaluator = LangtracePexEvaluator()
summary = evaluator.run_evaluation(
    limit=50,
    metric_name_prefix="AgentPex",
)
# Scores are pushed back to Langtrace
```

**Behavior**

- Fetches traces via the Langtrace REST API (`POST /api/traces` with pagination).
- Parses OTEL-format spans to extract prompt/completion messages from events and attributes.
- Runs the same AgentPex evaluation techniques as the CLI.
- Pushes scores back via the Langtrace SDK (`SendUserFeedback`) or REST API fallback.

## Example agents

Ready-to-run example agents are in the `examples/` directory for Langfuse and Langtrace.

**Langfuse example**

The example agent sends traces to Langfuse (your Langfuse credentials are used by the example script, not by the AgentPex API). You can then evaluate with the pip API (fetch traces yourself and call `import_traces` + `evaluate`) or use the example’s `--evaluate` flag, which uses the standalone script that fetches and pushes scores (and thus needs Langfuse env vars).

```bash
# Run the agent (traces go to Langfuse; requires Langfuse env if the agent uses the SDK)
python examples/langfuse_example_agent.py --run-agent

# Evaluate (example script: fetches from Langfuse and pushes scores; needs Langfuse env)
python examples/langfuse_example_agent.py --evaluate --hours-back 1
```

**Langtrace example**

```bash
# Run the agent (creates traced conversations in Langtrace)
python examples/langtrace_example_agent.py --run-agent

# Evaluate the traces with AgentPex
python examples/langtrace_example_agent.py --evaluate --limit 50

# Or both in one go
python examples/langtrace_example_agent.py --run-agent --evaluate
```

Both examples create multi-turn conversations with OpenAI's `gpt-4o-mini`, trace them to the respective platform, then run AgentPex evaluation and push scores back.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos are subject to those third-party's policies.

## Security

Please see our [Security Policy](SECURITY.md) for reporting security vulnerabilities.
