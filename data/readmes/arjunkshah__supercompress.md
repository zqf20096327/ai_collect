# SuperCompress

Prompt compression for production AI apps.

SuperCompress sits between your application and the LLM. It takes a long context plus the current user query, removes low-value context, keeps query-relevant evidence, and returns a smaller prompt with token-savings metadata.

It is useful when your app sends large retrieved documents, chat history, tool traces, logs, JSON blobs, or agent state into an LLM and you want lower input cost without rewriting the rest of your stack.

[![Repository](https://img.shields.io/badge/repository-GitLab-FC6D26?style=flat&logo=gitlab&logoColor=white)](https://gitlab.com/arjunkshah/supercompress)
[![PyPI](https://img.shields.io/pypi/v/supercompress?style=flat&logo=python&logoColor=white)](https://pypi.org/project/supercompress/)
[![License](https://img.shields.io/badge/license-MIT-3da639?style=flat)](LICENSE)
[![Dashboard](https://img.shields.io/badge/API-dashboard-111827?style=flat)](https://supercompress.dev/dashboard)

## What It Does

Most LLM apps accumulate context faster than they accumulate signal. Retrieval brings back near-duplicates. Agents pass around tool output. Chat history repeats the same facts. Logs and JSON carry a lot of machine noise.

SuperCompress compiles that input before it reaches the model:

- segments text into blocks instead of blindly cutting tokens
- detects content type: text, code, JSON, logs, and traces
- scores blocks against the current query
- keeps entities, definitions, errors, and nearby dependencies
- removes boilerplate, duplicated output, filler, and low-value metadata
- reports what was kept, how many tokens were removed, and the estimated risk

The query is never compressed. Only the context around it is.

## When To Use It

Good fits:

- RAG pipelines with long retrieved chunks
- agent frameworks with growing state or tool traces
- customer support and sales chat history
- code assistants sending repo snippets
- log analysis and incident debugging
- workflows that send structured JSON into an LLM

Bad fits:

- very short prompts
- exact legal/medical/audit text where every token must be preserved
- tasks where formatting is the answer
- small local models that are more sensitive to prompt shape than token count

For loss-sensitive workflows, use CCR markers or a lower compression setting.

## Install

```bash
pip install supercompress
export SUPERCOMPRESS_API_KEY=sc_live_YOUR_KEY
```

Get an API key from [supercompress.dev/dashboard](https://supercompress.dev/dashboard).

## Quick Start

```python
from supercompress.client import SuperCompress

sc = SuperCompress()

result = sc.compress(
    context=long_context,
    query="What failed and how do we fix it?",
)

print(result.compressed_text)
print(f"{result.original_tokens} -> {result.kept_tokens} tokens")
print(f"{result.kv_savings_pct:.1f}% saved")
```

Equivalent HTTP call:

```bash
curl -X POST https://supercompress.dev/api/v1/compress \
  -H "X-API-Key: $SUPERCOMPRESS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "context": "long retrieved context here",
    "query": "What failed and how do we fix it?"
  }'
```

## Response Shape

The API returns compressed text plus enough metadata to decide whether to use it.

```json
{
  "compressed_text": "...",
  "original_tokens": 4200,
  "kept_tokens": 1350,
  "tokens_saved": 2850,
  "kv_savings_pct": 67.8,
  "policy_name": "SuperCompress Compiler",
  "mode": "compiler",
  "compression_risk": "low",
  "preprocessor": "log"
}
```

Use `compressed_text` as the context you send to your LLM. Keep your original user query unchanged.

## Integration Patterns

### OpenAI Python SDK

```python
from openai import OpenAI
from supercompress.client import SuperCompress

openai = OpenAI()
sc = SuperCompress()

compressed = sc.compress(
    context="\n\n".join(retrieved_docs),
    query=user_question,
)

response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Answer using the provided context."},
        {
            "role": "user",
            "content": f"Context:\n{compressed.compressed_text}\n\nQuestion:\n{user_question}",
        },
    ],
)
```

### RAG Pipeline

```python
docs = retriever.search(query, k=12)
context = "\n\n---\n\n".join(doc.text for doc in docs)

compressed = sc.compress(context=context, query=query)

answer = llm.generate(
    system="Use the context. If the answer is missing, say so.",
    user=f"{compressed.compressed_text}\n\nQuestion: {query}",
)
```

### Agent State

```python
history = "\n".join(
    f"[{event.role}] {event.content}"
    for event in agent_events[:-1]
)

latest_task = agent_events[-1].content

compressed = sc.compress(
    context=history,
    query=latest_task,
)

next_prompt = f"{compressed.compressed_text}\n\nCurrent task:\n{latest_task}"
```

### Vercel AI SDK

Use the REST API from a server route or wrap `generateText`/`streamText`.

```ts
const compressed = await fetch("https://supercompress.dev/api/v1/compress", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "X-API-Key": process.env.SUPERCOMPRESS_API_KEY!,
  },
  body: JSON.stringify({
    context: messages.slice(0, -1).map((m) => `[${m.role}] ${m.content}`).join("\n"),
    query: messages.at(-1)?.content ?? "",
  }),
}).then((res) => res.json());

const result = await generateText({
  model: openai("gpt-4o-mini"),
  messages: [
    { role: "system", content: "Use the compressed context." },
    { role: "user", content: compressed.compressed_text },
  ],
});
```

More examples live in [integrations/](integrations/) and [examples/integrations/](examples/integrations/).

## Modes

| Mode | Use When | Behavior |
| --- | --- | --- |
| `compiler` | default production path | query-aware block compiler with content-specific preprocessing |
| `fixed` | you need a predictable budget | keeps approximately `budget_ratio` of the context |
| `precision` | you prefer lower risk over maximum savings | uses verifier-style confidence metadata where available |

Example:

```python
result = sc.compress(
    context=context,
    query=query,
    mode="fixed",
    budget_ratio=0.45,
)
```

## Content-Specific Compression

SuperCompress routes different input types through different preprocessors before scoring blocks.

| Input | What Gets Removed |
| --- | --- |
| JSON | nulls, empty arrays, oversized generated strings, repetitive array bodies |
| Code | docstrings, block comments, low-value comments, oversized literals |
| Logs | duplicate messages, debug noise, collapsed stack traces |
| Text / Markdown | repeated sections, boilerplate, weakly related blocks |

The response includes `preprocessor` so you can inspect which path ran.

## CCR: Reversible Compression

CCR, short for Cache-Compress-Retrieve, is for cases where compression is useful but permanent deletion is not acceptable.

```bash
curl -X POST https://supercompress.dev/api/v1/compress \
  -H "X-API-Key: $SUPERCOMPRESS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "context": "...",
    "query": "What happened?",
    "ccr": true
  }'
```

Removed blocks can be represented with markers like:

```text
[SC-Retrieve: a1b2c3d4]
```

Your app or agent can retrieve the original block later:

```bash
curl "https://supercompress.dev/api/retrieve?hash=a1b2c3d4"
```

Use CCR when auditability matters, when an agent may need to ask for omitted detail, or when you want compression without losing access to the source.

## Performance Notes

The practical value metric is not a single universal recall number. It depends on the corpus, the query, and the risk tolerance.

What we currently track:

- token reduction
- query entity recall
- keyword recall
- important context retained
- compression risk
- latency

On internal synthetic and demo workloads, SuperCompress typically removes a large share of prompt tokens while preserving the named entities and query terms needed for the current question. Exact answer quality should be measured on your own eval set before putting compression in front of critical workflows.

Run your own check by comparing your model outputs with and without compression on saved production prompts.

## Recommended Rollout

1. Log prompt size and cost before adding compression.
2. Add SuperCompress in shadow mode and store `original_tokens`, `kept_tokens`, and `compression_risk`.
3. Run answer-quality evals on your own traffic.
4. Start with `mode="compiler"` or `mode="fixed", budget_ratio=0.45`.
5. Lower the budget only after your evals pass.
6. Enable CCR for high-stakes or audit-sensitive paths.

## Local Development

```bash
git clone https://gitlab.com/arjunkshah/supercompress.git
cd supercompress
npm ci
```

The hosted API and static site are in this repository:

```text
api/                  Vercel serverless API
web/                  static site, playground, dashboard
web/assets/js/        browser compression engine
web/assets/data/      exported model and benchmark artifacts
integrations/         SDK and framework examples
examples/             small runnable examples
docs/                 API and setup docs
```

Useful local checks:

```bash
node --input-type=module --check < web/assets/js/dashboard-api.js
node scripts/benchmark_compiler.js
```

## API Reference

- [docs/API.md](docs/API.md)
- [docs/INTEGRATIONS.md](docs/INTEGRATIONS.md)
- [docs/API_DASHBOARD.md](docs/API_DASHBOARD.md)
- [docs/ENVIRONMENT.md](docs/ENVIRONMENT.md)

## License

MIT. See [LICENSE](LICENSE).
