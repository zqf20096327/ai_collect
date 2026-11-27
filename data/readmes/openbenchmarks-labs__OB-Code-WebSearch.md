# OB-Code-Websearch

Open, independent benchmark of web search APIs for developers and coding agents: which search API helps a coding agent write working API calls for enterprise products (Workday, SAP, UKG, Veeva, Genesys and ServiceNow). The model, tickets, search budget and run day stay fixed; only the search tool changes. Version 2 measures six search APIs, the ones its validation runs used: Firecrawl, Keenable, Nimble, Parallel, TinyFish and You.com.

**Live leaderboard (version 1):** [openbenchmarks.com/web-search-for-coding-agents](https://openbenchmarks.com/web-search-for-coding-agents) · **Public dataset:** [`openbenchmarks/OB-Code-Websearch`](https://huggingface.co/datasets/openbenchmarks/OB-Code-Websearch)

Published and maintained by **[OpenBenchmarks Labs](https://openbenchmarks.com)**.

## Methodology

Each task gives a coding agent a realistic integration ticket against an enterprise product API (such as Workday, SAP SuccessFactors, UKG, Veeva, Genesys Cloud, or ServiceNow) and the request the existing code sends today. The agent searches the web using the configured search API and produces a final API call.

- **Two boards:** **Search only** and **Search & fetch** are ranked separately.
- **Fixed protocol:** Every tool runs with the same coding model, turn limit and search budget (`harness/config.yaml`), and every setup of a run starts within one `window_hours` window (`benchmark.yaml`).
- **Scoring:** `judge/` grades each final answer against ground truth; [`judge/README.md`](judge/README.md#what-the-answer-grader-checks) says what the answer grader in this repo checks and what it does not. The `scoring` block in [`benchmark.yaml`](benchmark.yaml) sets how a board sums the grades: on the private set, ranked questions (an answer page open to crawlers) run three times and score the share of their scored runs that pass; validation runs each question once; the original and reserve groups are weighted; questions with no open answer page run once and are reported beside the ranking; each score has a 95% confidence range, and no setup is called better than another when the ranges overlap.
- **Failures:** an answer stopped by our own failure (the model service, our network, key, credit or rate limit) is asked again, up to three attempts, and is never scored; a board is refused when more than `not_measured_max` of a setup's planned runs went unscored. An answer stopped by the search API's own failure (a 5xx, a search that times out or is reset, or another mode than the one sent) is asked again the same way, and if it still fails on its last attempt it counts as the vendor's miss. A page that the fetch API fails to serve, for its own outage too, is shown to the model as an error, and the model goes on.

## Tools

The version 2 private run uses the 8 setups in [`STATUS.md`](STATUS.md): `firecrawl`, `keenable_pro`, `keenable_realtime`, `nimble_standard`, `parallel_advanced_tool`, `parallel_fast_tool`, `tinyfish` and `you_highlights_core`.

[`tools/`](tools/README.md) configures 13 search tools, the six above plus `brave`, `exa`, `linkup`, `perplexity`, `serp`, `tako` and `tavily`, which version 2 does not run.

## Dataset

- **Public split:** 30 enterprise API tickets are committed in [`data/questions.jsonl`](data/questions.jsonl). The Hugging Face dataset [`openbenchmarks/OB-Code-Websearch`](https://huggingface.co/datasets/openbenchmarks/OB-Code-Websearch) still holds the version 1 file; the version 2 questions are in review there.
- **Held-out split:** The validation and private sets are kept out of this repository to prevent contamination and training on test items; `benchmark.yaml` names each by its sha256.

See [`data/README.md`](data/README.md) for the full file format and field definitions.

## Repository structure

- [`data/`](data/README.md): 30 public benchmark questions and schema documentation.
- [`harness/`](harness/README.md): Agent loop, search API adapters, and the obkit entry points (`harness/obkit.py`).
- [`tools/`](tools/README.md): One `<tool>.yaml` config per search API (13 tools).
- [`judge/`](judge/README.md): The question the agent gets, the answer grader, and the LLM verifier.
- [`benchmark.yaml`](benchmark.yaml): Benchmark contract, scope, and refresh cadence.
- [`AGENTS.md`](AGENTS.md): Entry guide for coding agents.

## Quick start

Run the offline verification check (no API keys required):

```sh
uv venv && uv pip install -r requirements.txt
.venv/bin/python -B -m harness.obkit data/questions.jsonl
```

Live runs go through [obkit](AGENTS.md), which reads API keys from `.env` (copy `.env.example`) or the environment.

## Adding or updating a tool

1. Add or edit `tools/<tool>.yaml` (and update `harness/search.py` and `.env.example` if adding a new search API).
2. Run the offline `selftest` command above.
3. Open a pull request.

## Links

- [Live leaderboard](https://openbenchmarks.com/web-search-for-coding-agents)
- [Most accurate](https://openbenchmarks.com/web-search-for-coding-agents/most-accurate-search-api), [fastest](https://openbenchmarks.com/web-search-for-coding-agents/fastest-search-api) and [most token-efficient](https://openbenchmarks.com/web-search-for-coding-agents/most-token-efficient-search-api) search APIs for coding agents
- [Hugging Face dataset](https://huggingface.co/datasets/openbenchmarks/OB-Code-Websearch)
- [`llms.txt`](https://openbenchmarks.com/llms.txt)

## Related benchmarks

- [OB-Company-News](https://github.com/openbenchmarks-labs/OB-Company-News): Company news search and news-index APIs ([leaderboard](https://openbenchmarks.com/company-news))
- [OB-Company-Search-Multi-Turn](https://github.com/openbenchmarks-labs/OB-Company-Search-Multi-Turn): Multi-hop company research agents ([leaderboard](https://openbenchmarks.com/multi-turn-company-search))
- [OB-FinSearch](https://github.com/openbenchmarks-labs/OB-FinSearch): Financial research search APIs
- [All OpenBenchmarks leaderboards](https://openbenchmarks.com)

## License

MIT. See [LICENSE](LICENSE).
