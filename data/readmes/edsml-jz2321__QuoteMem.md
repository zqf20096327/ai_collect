# QuoteMem

QuoteMem is an auditable long-term memory service for conversational agents.
Each memory is a short statement tied to the exact words it came from. When a
fact changes, the old version is kept and marked as replaced. When a user asks
the agent to forget something, it is removed from reads and is not learned
again later.

**What it does**

- **Quoted evidence.** Every memory points to the original message by exact
  UTF-8 byte ranges, so any answer can be traced back to the words that
  support it.
- **Versioned supersession.** An update or correction writes a new version and
  closes the old one. History stays readable through `/memory/history`.
- **Forgetting with tombstones.** Forgetting is a two-step prepare/confirm
  call. A forgotten fact leaves a tombstone that the review step checks, so
  a later restatement of it is not stored again.
- **Recorded review decisions.** Before a new memory is written, a review step
  compares it with the existing memories it may update. Each decision is
  stored with the snapshot of neighbours it was made against, so it can be
  audited and replayed.
- **Review modes.** `lean-local` (the default) reviews with deterministic
  local rules. `full` sends every candidate to a judge model. A selective
  `targeted-v1` judge mode sends only flagged candidates to the model; it is
  used by research configurations, not by a command-line flag.

**How it differs.** Many memory layers store free-text summaries or embeddings
only. QuoteMem stores each memory together with its source quote, its version
history and its review decision, so every stored fact can be checked against
the conversation.

**Result.** In the Agent Memory Leaderboard (AMLB) Cycle 2 official results,
QuoteMem scored **59.83** overall and ranked **23rd of 125** entries in
*Textual Memory · Closed-source Methods*, where it is listed as "QuoteMem"
with a link to this repository:
<https://agentmemoryleaderboard.ai/results/cycle-2/#industry-textual>.

A paper describing the system is in preparation.

## Status

This is the first public snapshot of the code. Please note:

- **No tests are included yet.** The test suite depends on benchmark fixtures
  whose licences need review first.
- The Python package and command are named `aml`.
- Section references in code comments (for example `plan.md §9`) point to an
  internal design document that is not published.

## Install

Requirements: Python 3.12 and [uv](https://docs.astral.sh/uv/) 0.11.21 or later.

```bash
uv sync                  # core service
uv sync --extra bench    # also the benchmark tools (pyarrow, tiktoken)
```

QuoteMem stores its data with [HeavenBase](https://pypi.org/project/heavenbase/)
0.1.2.3 (MIT), which is installed from PyPI with the other dependencies.

## Run the HTTP service

```bash
export DASHSCOPE_API_KEY=...        # embeddings (Alibaba Cloud Model Studio)
export OPENAI_API_KEY=...           # chat model, through an OpenAI-compatible gateway
export OPENAI_BASE_URL=https://<your-gateway>/v1
export AML_HTTP_AUTH_SECRET=...     # clients send "Authorization: Bearer <secret>"
export AML_JOB_ID=local-1           # any non-empty identifier for this deployment

uv run aml serve --workspace ./qm-workspace --host 127.0.0.1 --port 8000
```

`serve` creates and initializes the workspace on first start. Stop it with
Ctrl-C; it drains in-flight requests before it exits.

Write a conversation turn, then search it:

```bash
curl -s http://127.0.0.1:8000/add \
  -H "Authorization: Bearer $AML_HTTP_AUTH_SECRET" -H "Content-Type: application/json" \
  -d '{"user_id": "u1", "session_id": "s1", "request_id": "r1",
       "messages": [{"role": "user", "speaker": "Rowan",
                     "content": "I moved to Lisbon last spring."}]}'

curl -s http://127.0.0.1:8000/search \
  -H "Authorization: Bearer $AML_HTTP_AUTH_SECRET" -H "Content-Type: application/json" \
  -d '{"user_id": "u1", "query": "Where does Rowan live?", "top_k": 10}'
```

`/add` returns after the new memories are stored and searchable.

Other routes:

| Route | Purpose |
|---|---|
| `GET /health` | Liveness |
| `POST /memory/history` | Version history of a memory |
| `POST /memory/why` | The evidence behind a memory |
| `POST /memory/add-items` | Memories written by one Add |
| `POST /memory/forget/prepare`, `POST /memory/forget` | Two-step forget by memory |
| `POST /memory/forget/statement/prepare`, `POST /memory/forget/statement` | Two-step forget by a natural-language statement |

`aml route --shard http://127.0.0.1:8001 --shard ...` spreads users over
several `serve` processes by `user_id`. Run `uv run aml serve --help` for the
remaining flags.

## Configuration

Secrets are read only from environment variables. Command-line flags and the
optional `--provider-config` JSON file hold non-secret settings only.

| Variable | Needed for | Notes |
|---|---|---|
| `DASHSCOPE_API_KEY` | Embeddings | Model `qwen3.7-text-embedding` through the Model Studio OpenAI-compatible endpoint |
| `OPENAI_API_KEY` | Extraction and review | Chat model `deepseek-v4.1-flash` |
| `OPENAI_BASE_URL` | Extraction and review | HTTPS root of an OpenAI-compatible gateway that serves that model. `api.openai.com` is refused for it. |
| `AML_HTTP_AUTH_SECRET` | `serve` | Non-empty printable ASCII |
| `AML_HTTP_AUTH_MODE` | `serve` | `bearer` (default), `token` or `x-api-key` |
| `AML_JOB_ID` | `serve` | Non-empty identifier |

Useful flags:

- `--add-mode {lean-local,full}` sets the review mode of a new workspace. The
  mode is frozen when the workspace is created; reopening it with a different
  mode is refused.
- `--embedding-dimensions {1024,2048}` sets the vector size of a new workspace.

## Benchmark tools

`python -m aml.bench.cli` downloads public benchmark files, replays them over
HTTP and computes local diagnostic scores. Benchmark data is not included in
this repository. [`benchmarks/`](benchmarks) lists each source by URL, pinned
revision, SHA-256 and licence, and the tool downloads it from its publisher:

```bash
uv run --extra bench python -m aml.bench.cli \
  --sources benchmarks/sources.json --dataset ./data/longmemeval_oracle.json --variant oracle download
```

Each dataset keeps its own licence (see [NOTICE](NOTICE)). LoCoMo-Refined is
CC BY-NC 4.0 (non-commercial) and BEAM data is CC BY-SA 4.0.

## Contact

Please open a GitHub issue for questions, bug reports and suggestions.

## License

MIT, see [LICENSE](LICENSE). Third-party components and their licences are
listed in [NOTICE](NOTICE).
