# Memory Recall Rerank

A reproducible benchmark and reference pipeline for long-term memory retrieval.

The core idea is simple:

```text
deterministic gate
→ recent-context reference resolution
→ broad retrieval
→ rerank
→ deterministic state rules
→ confidence routing
→ optional LLM arbitration
→ top-k context injection
```

Vector search retrieves broadly. A reranker judges query–candidate relevance. Deterministic rules protect temporal truth. An LLM handles only ambiguous references and version conflicts.

## Internal benchmark

The included dataset contains 18 synthetic Chinese memory-recall cases. It covers location collisions, superseded preferences, cancelled plans, meal slots, generic questions, pure emotion, explicit recall and all-irrelevant candidates. Public fixtures are de-identified semantic equivalents of the internal set, so fresh API scores may vary slightly from the recorded run.

| Evaluated system | Strict accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| DeepSeek V4 Flash | 16/18 | 0.846 | 1.000 | 0.917 |
| DeepSeek V4 Pro | 16/18 | 0.909 | 0.909 | 0.909 |
| GPT-4o | 17/18 | 0.917 | 1.000 | 0.957 |
| Voyage rerank-2.5, Top-1, threshold 0.50 | 18/18 | 1.000 | 1.000 | 1.000 |
| Cohere Rerank 4 Pro + deterministic rules | 18/18 | 1.000 | 1.000 | 1.000 |

These are project-internal results recorded on 2026-08-17, not a universal leaderboard. Voyage's lowest positive and highest negative scores were 0.508 and 0.439; the threshold is dataset-specific. Cohere's 18/18 is a pipeline result, not a raw-model claim. Re-run the public fixtures before adopting any threshold.

## Quick start

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e .

export COHERE_API_KEY=...
memory-recall-benchmark --provider cohere --model rerank-v4.0-pro

export VOYAGE_API_KEY=...
memory-recall-benchmark --provider voyage --model rerank-2.5 --low 0.44 --high 0.50 --top-k 1
```

Run deterministic tests without any API key:

```bash
python -m unittest discover -s tests -v
```

## Integrating the pipeline

Implement a retriever that returns `Candidate` objects, choose a `Reranker`, and call `RecallPipeline.recall()`. If the current turn contains a context-local reference, pass a bounded `recent_context` separately. The gate can then avoid long-term retrieval when the live conversation already resolves the reference. Do not concatenate recent dialogue into every retrieval query: words merely mentioned by the current discussion can become false long-term targets.

The optional ambiguity callback receives only grey-zone or conflicting candidates. It must return candidate IDs, never rewritten memory text.

A reranker answers “which candidate is most relevant?” It does not decide whether long-term memory should be searched at all. Keep recall intent and local reference resolution ahead of retrieval, and report their quality separately from rerank accuracy. The 18-case table above remains a candidate-ranking benchmark; gate regressions are not added to its denominator.

Scores are not portable between providers. Calibrate thresholds for every model and dataset. Keep timestamps and state metadata outside free-form summaries whenever possible.

## Privacy and failure behavior

Only the query and bounded synthetic/reference candidate fields are sent to a rerank API. Keys are loaded from environment variables. Logs should contain IDs, scores, latency and routing decisions—not full private memories.

If reranking fails, the reference pipeline returns a typed failure. A production integration may explicitly fall back to an existing verifier; if both fail, fail closed rather than injecting unaudited vector neighbours.

## License

AGPL-3.0-only. Network deployments that modify this project must make the corresponding source available under the license terms.
