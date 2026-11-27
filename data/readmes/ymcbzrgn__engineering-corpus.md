# Engineering Corpus

<!-- mcp-name: com.engineeringcorpus/engineering-corpus -->

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/ymcbzrgn/engineering-corpus/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/engineering-corpus.svg)](https://pypi.org/project/engineering-corpus/)
[![Engineering Corpus MCP server – quality and maintenance score on Glama](https://glama.ai/mcp/servers/ymcbzrgn/engineering-corpus/badges/score.svg)](https://glama.ai/mcp/servers/ymcbzrgn/engineering-corpus)

[![Engineering Corpus: real code your agent can cite. Research agents read the repos you choose, and every report ends with a receipt: a repository at a pinned commit, a file with its lines, and its license.](https://engineeringcorpus.com/og-en.png)](https://engineeringcorpus.com)

Research agents that cite their sources. My agents kept forgetting the repos I told them to learn from and made up sources, so I built agents that study the public GitHub repos you choose, inside the coding agent you already use, and end every report with a receipt: the repository, the commit, the lines and the license of each source. The engine is MIT and runs on your machine, on the CPU.

On one question, the agent's page shows that deer-flow accepts a server's Retry-After of up to 24 hours while tradingagents caps it at 60 seconds, each cited with its lines.

[Docs](https://engineeringcorpus.com/docs/getting-started) ·
[How the benchmark works](https://engineeringcorpus.com/docs/benchmark-method) ·
[Limits](https://engineeringcorpus.com/docs/limits) ·
[Changelog](https://github.com/ymcbzrgn/engineering-corpus/blob/main/CHANGELOG.md)

Try it with one command. It indexes two small repos, runs two searches, needs no account and no key, and the first run downloads an
embedding model of about 600 MB. On a 16 GB Apple M2 Mac it took 112 seconds, about 20 of them for the download. A slower
connection adds to that.

```sh
uvx engineering-corpus demo
```

The [Quickstart](#quickstart) connects it to Claude Code or Codex.

What an agent hands back, from hits to receipts:

<picture>
  <source media="(max-width: 560px) and (prefers-color-scheme: dark)" srcset="https://engineeringcorpus.com/diagrams/rag-return-phone-dark.svg">
  <source media="(max-width: 560px) and (prefers-color-scheme: light)" srcset="https://engineeringcorpus.com/diagrams/rag-return-phone-light.svg">
  <source media="(max-width: 860px) and (prefers-color-scheme: dark)" srcset="https://engineeringcorpus.com/diagrams/rag-return-medium-dark.svg">
  <source media="(max-width: 860px) and (prefers-color-scheme: light)" srcset="https://engineeringcorpus.com/diagrams/rag-return-medium-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="https://engineeringcorpus.com/diagrams/rag-return-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://engineeringcorpus.com/diagrams/rag-return-light.svg">
  <img src="https://engineeringcorpus.com/diagrams/rag-return-medium-light.svg" width="100%" alt="What an agent hands back: from a question to receipts. It asks the corpus tools, reads the lines it will cite, and ends with one receipt line per source.">
</picture>

<details>
<summary>Text version</summary>

1. Research agent (`pack/agents`)
    - You ask one of seven agents, inside the coding agent you already use: `corpus-miner`, `design-explorer`, `precedent-reviewer`, `prior-art-researcher`, `provenance-guard`, `test-scout` and `usage-finder`.
    - The receipt rules are the same block in all seven.
2. Corpus tools (`server.py`)
    - Twelve tools, all read-only: `corpus_search`, `corpus_compare`, `corpus_explore`, `corpus_read`, `corpus_grep`, `corpus_symbols`, `corpus_references`, `corpus_context`, `corpus_package`, `corpus_usage`, `corpus_repos` and `corpus_status`.
    - Corpus text is treated as evidence. Every result that holds corpus text has a notice that says so. With `--agent-files warn`, a hit on a file written to steer agents has a warning.
3. Search, alongside Read and grep, Structure (`server.py`)
    - `corpus_search` returns one hit per file, best first.
    - Each hit has a license class, a permalink pinned to the commit, and a snippet for P, B, W and C. The result lists one verdict for each class.
4. Read and grep, alongside Search, Structure (`read.rs`)
    - `corpus_read`: the file's text at the indexed commit, only for files the secret scan saw. A page is at most 200 lines and 16,000 characters, cut at whole lines.
    - `corpus_grep`: a regex over the same files, at most 100 matches, each line cut at 300 characters.
5. Structure, alongside Search, Read and grep (`symbols.rs`)
    - `corpus_symbols` and `corpus_references` find definitions and references by name. References are inferred.
    - `corpus_context` shows a definition with its callers, tests and docs.
    - `corpus_package` lists which repos use a package, at which version, with lockfile lines.
    - `corpus_usage` shows call sites of an API with their error path.
6. The report (`usage-finder.md`)
    - Every citation is written in full: `owner/repo@commit` and `path:line`.
    - A snippet is pasted only when the user is told to paste lines, and only for classes P, B, W and C. R and U are always pattern only.
7. The receipt block (`usage-finder.md`)
    - `bytedance/deer-flow@35656d6a9fe2ac76ddcf40335ede7361504ddf5b | backend/packages/harness/deerflow/models/claude_provider.py:376-447 | class P (MIT) | pattern only`
    - One line per cited source: the 40 character commit, the lines, the class and its SPDX id (`none` for U).
    - Then `pattern only`, or `copied with notice` and a notice line with the copyright and the license name.
    - No source cited: `No sources cited.`
8. The closing line (`usage-finder.md`)
    - `Licence classes are automated verdicts, not legal advice.`
    - The agents print this line last.

Beside the steps:

- Class verdicts (`server.py`)
    - P: reuse the code if you keep its copyright and license notice.
    - B: reuse the code with its notice. The names and logos are excluded.
    - W: changes to these files stay under the same license; keep the notice.
    - C: reuse puts your derived work under the same license; keep the notice.
    - R and U: location only. Read the file on GitHub and reuse the pattern, without the code.
    - Each verdict says it is automated and is not legal advice.

</details>

## One brief

A developer asks:

> my Python agent calls an LLM API and sometimes gets rate limits and timeouts. How do serious projects retry a failed LLM or HTTP request with exponential backoff, and which approach fits an app that runs as one process? I want no new services, and I can only copy code under permissive licenses.

A model can answer that question from memory. Memory holds the general advice. What each project chose is in its code, and the projects differ. One detail of this
question shows it: how long to wait when a server sends a `Retry-After` header.

- deer-flow accepts a delay of up to 24 hours and falls back to its own backoff above that ([`retry_after.py:7-16`](https://github.com/bytedance/deer-flow/blob/35656d6a9fe2ac76ddcf40335ede7361504ddf5b/backend/packages/harness/deerflow/utils/retry_after.py#L7-L16)).
- tradingagents caps it at 60 seconds ([`reddit.py:151-165`](https://github.com/tauricresearch/tradingagents/blob/c4544913a14ed3df5f1ed7b9e8483270ce20682a/tradingagents/dataflows/vendors/reddit.py#L151-L165)).

Claude Code ran the `prior-art-researcher` agent on that question on 2026-11-13, against an index of 14 public repos, the set the project uses to test comparisons. The page it returned is in [docs/example-brief.md](https://github.com/ymcbzrgn/engineering-corpus/blob/main/docs/example-brief.md), unedited. Its pick, in its words:

> **Pick: B, your own loop, with the SDK's `max_retries=0` whenever an SDK sits underneath.** The deciding constraint is that your client is unknown and the general case is any failed HTTP request. A only exists where an SDK offers the setting. B covers SDK calls and raw httpx/requests/urllib calls with one policy, and adds no dependency or service. Its state stays local, which is all one process needs (inference).

Every source on the page gets a receipt, for example:

```text
bytedance/deer-flow@35656d6a9fe2ac76ddcf40335ede7361504ddf5b | backend/packages/harness/deerflow/models/claude_provider.py:376-447 | class P (MIT) | pattern only
```

The agent made 52 calls to the corpus tools in 862 seconds, on Claude Opus 5.5: 99,224 output tokens and 1,802,609 input tokens, 1,539,847 of them cached context read again on later steps. The run cost $3.68 at list prices.

To get a brief for your own question, ask your agent to run the `prior-art-researcher` agent on it.

## How it works

Indexing builds one index from the repos you choose. Searching reads it. The research agents sit on top of searching and write the receipts. The picture at the top of this page shows what they hand back. [ARCHITECTURE.md](https://github.com/ymcbzrgn/engineering-corpus/blob/main/ARCHITECTURE.md) describes each step.

Indexing, from a slice file to the index:

<picture>
  <source media="(max-width: 560px) and (prefers-color-scheme: dark)" srcset="https://engineeringcorpus.com/diagrams/rag-index-phone-dark.svg">
  <source media="(max-width: 560px) and (prefers-color-scheme: light)" srcset="https://engineeringcorpus.com/diagrams/rag-index-phone-light.svg">
  <source media="(max-width: 860px) and (prefers-color-scheme: dark)" srcset="https://engineeringcorpus.com/diagrams/rag-index-medium-dark.svg">
  <source media="(max-width: 860px) and (prefers-color-scheme: light)" srcset="https://engineeringcorpus.com/diagrams/rag-index-medium-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="https://engineeringcorpus.com/diagrams/rag-index-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://engineeringcorpus.com/diagrams/rag-index-light.svg">
  <img src="https://engineeringcorpus.com/diagrams/rag-index-medium-light.svg" width="100%" alt="Indexing: from a slice file to a searchable index. Each repo is cloned, walked, scanned for secrets, cut into windows, embedded and stored, in nine steps.">
</picture>

<details>
<summary>Text version</summary>

1. Intake (`intake.py`)
    - URLs must be `https://github.com/owner/repo`. A repo marked `private` in the slice file and owners that start with an excluded prefix are dropped. The engine does not check visibility on GitHub: list public repos only (`corpus stars` leaves private stars out).
    - Owner: letters, digits and hyphens, at most 39. Repo name: at most 100.
    - `slice.toml`: `repos` and `exclude_owners`; per repo `url`, `default_branch`, `commit`, `licence`, `licence_overrides`, `private`.
    - No network call. An unknown key stops the run before any work.
2. Clone (`git.rs`)
    - A shallow bare clone of one branch: `git clone --bare --depth 1 --branch`, into a `.partial` folder renamed when complete.
    - An existing clone is updated with `git fetch --depth 1`. A pinned commit is fetched and the branch pointed at it.
    - No shell, and `GIT_TERMINAL_PROMPT=0`. Branch and commit are validated; the URL comes after `--`.
3. Walk (`walk.rs`)
    - The head commit's tree is read with gitoxide, no working tree.
    - Checks run in order. Every skipped file names its rule, one of 15.
    - The rules: `non_utf8_path`, `symlink`, `submodule`, `excluded_dir` (14 folder names), `lockfile` (19 names), `excluded_suffix` (87 endings), `licence_text`, `translation`, `translated_doc`, `generated`, `too_large`, `lfs_pointer`, `binary`, `non_utf8_content`, `minified`.
    - Size caps: 2,000,000 bytes for source code, Markdown and reStructuredText outside test folders, 300,000 for the rest.
    - A file is binary if it has a zero byte (NUL) in its first 8 KiB.
    - A file is minified if it is 2,000 bytes or more. Then either its first line is over 1,000 bytes or its lines average over 300.
4. Licenses (`licence.rs`)
    - Six classes, most to least permissive: P permissive, B permissive with branding terms, W weak copyleft, C copyleft, R restricted, U unknown.
    - Where a file's class comes from, most specific first: an `override` in the slice file, then an `SPDX-License-Identifier:` tag in its first 20 lines.
    - Then comes the nearest folder with a license file, then the repo's declared license.
    - If none applies, the source is `unknown` and the class is U.
    - For a license written as an SPDX expression (`MIT OR Apache-2.0`), OR gives the class that comes first in the order of the six classes.
    - AND gives the one that comes last.
    - Text matching uses the `spdx` crate, from 0.8 confidence.
5. Secret scan (`secrets.rs`)
    - Betterleaks 1.x scans a temporary copy of every kept file, and of the skipped files `corpus_read` can still serve, before any chunk exists. No network.
    - A secret is replaced wherever it appears by `‹secret masked: rule›`. Line numbers stay where they were.
    - No chunk, vector or answer holds the secret. `--allow-unscanned` skips the scan, and the registry records how each repo was checked.
6. Chunk (`chunk.rs`)
    - Windows of 60 lines, one starting every 50 lines, so neighbours overlap by 10.
    - Cut at line boundaries only. Every non blank line lands in at least one chunk, byte for byte.
    - The embed text is a header, a newline and the chunk. The header is `owner/name · path · language`. Over 1,024 tokens, a window splits at line boundaries, taking as many lines as fit.
    - Each chunk has its file's kind tag: `decision`, `changelog`, `agent-instructions` or `plain`.
7. Embed, alongside Terms (`embed.rs`)
    - `granite-embedding-english-r2`, ONNX, CPU only: one vector of 768 numbers, scaled to length 1, per chunk.
    - At most 1,024 tokens per chunk.
    - A model call holds at most 32 chunks, and at most 2,400 tokens counted as the number of chunks times the longest one.
    - `embed_key` is the SHA-256 of the model profile and the embed text. A chunk whose key is unchanged keeps its vector, so a re-index after `git pull` embeds only what changed.
8. Terms, alongside Embed (`terms.rs`)
    - Each word of the embed text is cut into identifier parts, then added whole, lower case. `getUserName` gives `get`, `user`, `name`, `getusername`; `HTTPError` gives `http`, `error`, `httperror`.
    - The header's words, repo, path and language, are terms too. A query goes through the same function.
9. Store (`store.rs`)
    - LanceDB, written per repo: a repo's rows in each table are replaced in one call and the indexes follow.
    - `chunks`, 15 columns: `repo`, `path`, `start_line`, `end_line`, `commit`, `blob_sha`, `language`, license class, SPDX id and source, `text`, `vector` (768 float32), `terms`, `embed_key`, `doc_kind`.
    - Indexes: a bitmap index (a lookup table) on `repo` and `doc_kind`, a full-text index on `terms` (whitespace tokens, no stemming, no stop words). No vector index is built.

Beside the steps:

- Symbols (`symbols.rs`)
    - Definitions and references from tree-sitter, a parser library, using its tags queries, 16 languages. References are matched by name, so they are inferred.
    - A file with syntax errors is flagged.
- Dependencies (`deps.rs`)
    - Four ecosystems: Cargo, npm, PyPI and Go. Lockfiles and manifests are read, each fact with its lockfile path and line.
    - A file in a format or version it does not know gives a `not parsed` receipt with the reason, never a guess.
- Files and registry (`registry.py`)
    - `files`: every file the scan saw, which `corpus_read` and `corpus_grep` serve, with its masked text if it had a finding.
    - `registry.sqlite`: each repo's head commit, license and trust labels (archived, last push, fork). The trust labels come from one GitHub request.

Indexing reaches the network to clone the repos you list, to ask GitHub for public data about each, and to download the embedding model once. A search or a read sends your query to nobody.

Published figures:

- First run, 5 repos, Apple M2, CPU only, timed after clone and model download, 2026-11-13: 1.27 chunks a second and 811 tokens a second. A first run takes longer.
- Peak memory while indexing: up to 1,588 MB.
- Embedding model, first run: about 600 MB download.

</details>

Searching, from a question to a hit:

<picture>
  <source media="(max-width: 560px) and (prefers-color-scheme: dark)" srcset="https://engineeringcorpus.com/diagrams/rag-search-phone-dark.svg">
  <source media="(max-width: 560px) and (prefers-color-scheme: light)" srcset="https://engineeringcorpus.com/diagrams/rag-search-phone-light.svg">
  <source media="(max-width: 860px) and (prefers-color-scheme: dark)" srcset="https://engineeringcorpus.com/diagrams/rag-search-medium-dark.svg">
  <source media="(max-width: 860px) and (prefers-color-scheme: light)" srcset="https://engineeringcorpus.com/diagrams/rag-search-medium-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="https://engineeringcorpus.com/diagrams/rag-search-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://engineeringcorpus.com/diagrams/rag-search-light.svg">
  <img src="https://engineeringcorpus.com/diagrams/rag-search-medium-light.svg" width="100%" alt="Searching: from a question to a hit. Two lists of 400 chunks are merged into one order, cut to one hit per file, and each hit comes back with its license class.">
</picture>

<details>
<summary>Text version</summary>

1. Validate (`server.py`)
    - `query` 1 to 4,000 characters. `k` 1 to 25 hits, 5 by default.
    - `repos`: at most 100 canonical ids, `github.com/owner/name`, lower case. Ids that are not indexed come back in `not_indexed`.
    - Optional: `per_repo`, `uses` (a package), `kind` and `deep`.
2. Dense list, alongside Keyword list (`store.rs`)
    - The query is embedded as it is, with no header or prefix, by `granite-embedding-english-r2`: one 768 dimension vector, on the CPU.
    - The 400 nearest chunks by cosine similarity (how closely two vectors point the same way). A flat scan: the query is compared with every stored vector in scope, and no vector index is built.
3. Keyword list, alongside Dense list (`terms.rs`)
    - The query goes through the same `terms` function as the chunks: `getUserName` gives `get`, `user`, `name` and `getusername`.
    - The 400 best matches by BM25 (a keyword scoring formula; `k1` 1.2, `b` 0.75) on the chunks' `terms`, a full-text index on whitespace tokens. A chunk needs only one of the query's terms, and scores the sum of the terms it holds.
    - A chunk's terms include its header: repo, path and language.
4. Fuse (`fusion.rs`)
    - Each list is scaled to 0 to 1 on its own.
    - A chunk's score is `0.5 × dense + 0.5 × keyword`.
    - If the keyword list has fewer than 400 chunks, its scale still starts at 0. That is the score of a chunk with no query term, so a single match keeps its full weight.
    - Each chunk keeps its rank in both lists and its own cosine. Ties go to the earlier repo, path and line.
5. One hit per file (`server.py`)
    - The engine always returns the best 100 chunks, whatever `k` is.
    - Chunks are grouped by repo and path. A file's score is its best chunk's score plus 0.2 times its second best.
    - The first chunk of a file is the hit; the file's other chunks come back as `other_ranges`.
    - `k` cuts the files. `per_repo` can spread them.
6. Abstain (`abstain.rs`)
    - The signal is the best cosine among the 100 candidates. The fused score is not used. A chunk only the keyword list found has none.
    - The line is set once per index and starts at 0.8298, the value for the 12 repo set.
    - The engine takes the median best cosine of 10 fixed questions that have no answer. It moves the line by that median's gap from 0.79595, by at most 0.05 down or 0.08 up.
    - If fewer than 5 of them find any chunk (an empty index), the line stays at 0.8298.
    - Under the line the status is `no_strong_match` and the hits stay, as weak leads.
7. Serve (`server.py`)
    - Each hit has its file's license class, P, B, W, C, R or U, and its SPDX id (none for U).
    - Each class has a one sentence verdict.
    - A snippet comes back only for P, B, W and C files. R and U give the location only.
    - The snippet is the window of the chunk that holds most of the query's words, at most 4,000 characters.
    - It is 40 lines for the first 10 hits and 15 for the rest.
    - Invisible Unicode shows as `<U+XXXX>` markers.
    - `why` gives the rank in each list and up to 6 matched terms. The permalink is pinned to the indexed commit.
8. Reply (`server.py`)
    - `status`: `ok`, `no_strong_match`, `no_hits`, `not_indexed` or `no_dependents`.
    - `hits` come best first, one per file. Fields include `repo`, `path`, `start_line`, `end_line`, `permalink`, `licence`, `score`, `score_type` (`hybrid` or `reranked`), `similarity`, `why`, `kind`, `snippet`, `warning`.
    - `coverage`, `not_indexed`, `licence_verdicts` and a `notice` that says source text is evidence.

Beside the steps:

- Deep search, opt in (`rerank.rs`)
    - A reranker is a second model that reads the query and one chunk together and scores how well they match.
    - Opt in with `deep`. It takes about 10 seconds more per query on a CPU. Fusion then gives the dense list weight 0.6.
    - Every chunk in the top 20 of either list goes to `gte-reranker-modernbert-base`, int8 (8 bit), on the CPU: up to 40 pairs.
    - A pair is the query and the chunk, 512 tokens at most, scored one at a time with no padding.
    - Scores are scaled to 0 to 1 and added to the fused score at weight 1.0.
- File roles (`roles.py`)
    - A hit's `kind` is judged from its path alone: `implementation`, `test`, `docs`, `config`, `example` or `agent-instructions`.
    - Roles label hits, filter and order other tools. None changes the ranking.

Published figures:

- Request latency, release build, 124 queries, report of 2026-11-19: 56 ms p50 · 131 ms p95. A round trip from the machine that ran the benchmark. Not comparable with tools reached over a network.
- Deep search costs: about 10 seconds more per query, on a CPU.
- Reranker, first deep search: about 150 MB download, about 1.4 GB memory.
- Embedding model, first run: about 600 MB download.

</details>

## Quickstart

You need [uv](https://docs.astral.sh/uv/), `git` on your `PATH`, and one of three kinds of machine: an Apple silicon Mac, Linux on x86_64 or aarch64
with glibc 2.28 or newer, or Windows x64. On any other machine, use the [Docker image](#docker). The demo indexes two small
repos and runs two searches:

```sh
uvx engineering-corpus demo
```

The first run downloads the embedding model, about 600 MB, and indexes about 170 chunks. A second run reuses both. The searches
print one line per hit: the score, the repo, the file with its lines, and the license class (`P` is permissive).

```text
$ corpus search 'verify an HMAC signature'
1.000  github.com/pallets/itsdangerous  src/itsdangerous/signer.py:1-60  [P]
0.959  github.com/pallets/itsdangerous  src/itsdangerous/signer.py:51-110  [P]
0.946  github.com/pallets/itsdangerous  src/itsdangerous/signer.py:201-260  [P]
```

That output is the demo's own, run on the demo's folder. To search it yourself, give the search that folder. Without `--data-dir`, `search` reads your own data folder, `~/.local/share/engineering-corpus`, where `corpus index` writes your index and the demo's index is not:

```sh
uvx engineering-corpus search 'verify an HMAC signature' --data-dir ~/.cache/engineering-corpus/demo
```

It prints eight hits by default. The demo printed the first three.

If the demo stops with an error, see [If the demo stops](#if-the-demo-stops) below.

Then connect your agent. In Claude Code, the plugin brings the seven research agents along with the tools:

```sh
claude plugin marketplace add ymcbzrgn/engineering-corpus
claude plugin install engineering-corpus@engineering-corpus
```

In Codex:

```sh
codex plugin marketplace add ymcbzrgn/engineering-corpus
codex plugin add engineering-corpus@engineering-corpus
```

For the tools alone, with no agents, add the server to Claude Code with
`claude mcp add engineering-corpus -- uvx engineering-corpus serve` (on an older Python, put `--python 3.12` after `uvx`).
The plugins start `uvx` themselves, so no flag can be added to them: on a Python older than 3.11, install a newer one first.
The other clients are under [Connect a client](#connect-a-client).

Then index the repos you would consult for today's task, not all your stars. Indexing needs [Betterleaks](https://github.com/betterleaks/betterleaks) 1.x on your `PATH` (on macOS, `brew install betterleaks`); the demo needs neither it nor a token, and the Docker image carries both git and Betterleaks. Write a slice file with one entry for each, and index it:

```toml
# corpus.toml
[[repos]]
url = "https://github.com/OWNER/NAME"
default_branch = "main"    # the repo's own default branch
```

```sh
uvx engineering-corpus index corpus.toml    # clones, scans and embeds each repo
```

Expect minutes for a small repo and hours for a very large one. On a 16 GB Apple M2 Mac, timed on 2026-11-13 before the embedder thread setting, the engine indexes about 1.27 chunks a second for a repo of more than 500 chunks, so 1,000 chunks take about 13 minutes and 10,000 chunks take about 2.2 hours. That last figure is calculated from the rate; the largest repo timed had 5,448 chunks and took 69 minutes. The [FAQ](https://engineeringcorpus.com/docs/faq#how-long-does-the-first-index-take) has the timed repos and what to expect while a run goes on.

To start from your stars instead, `uvx engineering-corpus stars YOUR_LOGIN --exclude-owner YOUR_EMPLOYER` writes `stars.toml`.
Name every organization you work for with `--exclude-owner`, because the engine calls no organization API, and trim the file to a
few repos before you index, because every repo in it is cloned and embedded. With `uv tool install engineering-corpus` the
commands are `corpus stars` and `corpus index`. The [guide to indexing your stars](https://engineeringcorpus.com/docs/index-your-stars)
covers tokens, rate limits and what is never imported.

### If the demo stops

If the demo stops at once with `has no wheels with a matching platform tag` (uv) or `No matching distribution found for
engineering-corpus` (pip), the machine is not on that list: an Intel Mac, a machine running Alpine Linux (it uses musl, not
glibc) and Windows on Arm get this message. On an Intel Mac and on x86_64 Linux, run the Docker image. It is a linux/amd64
image: a Debian system with the engine in it, and Docker Desktop on an Intel Mac runs it as it is. Windows on Arm and Alpine
Linux on arm64 have neither a wheel nor an arm64 image in v0.1.

If uv stops with `No solution found when resolving tool dependencies` and a hint that it only found `cp311` wheels,
your Python is older than 3.11. Ask uv for a newer one: it uses one it finds and downloads one if it finds none.

```sh
uvx --python 3.12 engineering-corpus demo
```

## Install

Four channels, each running the same engine. Pick the one your tools already use.

| Channel | Install | Update |
|---|---|---|
| uv | `uvx engineering-corpus serve` runs it with no install. `uv tool install engineering-corpus` puts `corpus` on your `PATH`. | `uvx engineering-corpus@latest --version` refreshes uv's copy and ends (`serve` would wait for a client, with nothing printed); restart your client to start the server again. Or `uv tool upgrade engineering-corpus` |
| Claude Code plugin | `claude plugin marketplace add ymcbzrgn/engineering-corpus`, then `claude plugin install engineering-corpus@engineering-corpus` | `claude plugin marketplace update`, then `claude plugin update engineering-corpus`, then restart Claude Code |
| Codex plugin | `codex plugin marketplace add ymcbzrgn/engineering-corpus`, then `codex plugin add engineering-corpus@engineering-corpus` | `codex plugin marketplace upgrade` refreshes the marketplace's snapshot |
| Docker | `docker pull ghcr.io/ymcbzrgn/engineering-corpus` | Pull again |

Wheels are built for Linux x86_64 and aarch64 (glibc 2.28 or newer), macOS on Apple silicon and Windows x64. The package needs
Python 3.11 or newer. To use another copy of ONNX Runtime than the `onnxruntime` package, set `ORT_DYLIB_PATH` to its
`libonnxruntime` library.

### Connect a client

Each client starts the same command, `uvx engineering-corpus serve` (on an older Python, put `--python 3.12` after `uvx`):

- Claude Code: `claude mcp add engineering-corpus -- uvx engineering-corpus serve`
- Cursor: [Add to Cursor](cursor://anysphere.cursor-deeplink/mcp/install?name=engineering-corpus&config=eyJjb21tYW5kIjoidXZ4IiwiYXJncyI6WyJlbmdpbmVlcmluZy1jb3JwdXMiLCJzZXJ2ZSJdfQ%3D%3D), or add the server `uvx engineering-corpus serve` in Cursor's MCP settings
- VS Code: [Install in VS Code](https://vscode.dev/redirect?url=vscode%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522engineering-corpus%2522%252C%2522type%2522%253A%2522stdio%2522%252C%2522command%2522%253A%2522uvx%2522%252C%2522args%2522%253A%255B%2522engineering-corpus%2522%252C%2522serve%2522%255D%257D) or [VS Code Insiders](https://vscode.dev/redirect?url=vscode-insiders%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522engineering-corpus%2522%252C%2522type%2522%253A%2522stdio%2522%252C%2522command%2522%253A%2522uvx%2522%252C%2522args%2522%253A%255B%2522engineering-corpus%2522%252C%2522serve%2522%255D%257D)
- Any client that speaks Streamable HTTP: run `corpus serve --http` and point it at `http://127.0.0.1:8765/mcp`.

On an older Python, edit the entry the Cursor and VS Code links create, and start its `args` with `"--python", "3.12"`.

`python -m engineering_corpus.install_links` prints these links. Each release is published to the official MCP Registry as
`com.engineeringcorpus/engineering-corpus` by the release workflow. The [connect guide](https://engineeringcorpus.com/docs/connect-your-agent) has the
steps for each client, and the [HTTP and Docker guide](https://engineeringcorpus.com/docs/http-and-docker) covers the HTTP
server.

### Docker

```sh
docker run -it --rm -v corpus:/data ghcr.io/ymcbzrgn/engineering-corpus demo --data-dir /data/demo
docker run -i --rm -v corpus:/data ghcr.io/ymcbzrgn/engineering-corpus serve --data-dir /data     # MCP over stdio
docker run --rm -p 127.0.0.1:8765:8765 -v corpus:/data ghcr.io/ymcbzrgn/engineering-corpus        # Streamable HTTP at /mcp
```

To index your own repos in the image, mount the slice file into the working directory and run `index` on it. The index lands
in the `corpus` volume that the `serve` line above reads; the demo keeps its own in `/data/demo`.

```sh
docker run -it --rm -v corpus:/data -v "$PWD/corpus.toml:/data/corpus.toml:ro" ghcr.io/ymcbzrgn/engineering-corpus index corpus.toml
```

The image carries git and a pinned Betterleaks, so `corpus index` scans for secrets inside it. The HTTP server has no
authentication: publish its port on localhost only, as the last line does, or put a proxy with authentication in front.

## The agents

Seven read-only research agents run a method from start to finish. Each ends its report with a receipt block: one line for each
source, with the repo, the commit, the lines, the license class, and `pattern only` or `copied with notice`.

| Agent | What it does |
|---|---|
| `prior-art-researcher` | The whole brief, as one subagent: compares how real projects approach your problem, picks the approach that fits your constraints, finds real call sites of it, and writes one page with the license of every source. When a project keeps decision records, it reports why the maintainers chose their approach. |
| `corpus-miner` | Prior art for a feature: how independent projects solved it, with the counter-examples and the tests that pin the behavior. |
| `design-explorer` | Three to five materially different approaches to one design problem, with their trade-offs and, when a decision record exists, why the maintainers chose an approach. |
| `usage-finder` | How real projects call a library or API, with the error handling and the versions. |
| `provenance-guard` | Where a pasted snippet comes from, under which license, and the notice it needs. |
| `precedent-reviewer` | Compares your diff with how the corpus handles the same thing, and reports gaps, differences and matches, each cited. |
| `test-scout` | How real projects test the same behavior: the techniques, the cases they cover and the cases no test pins down. |

`corpus serve` offers them as MCP prompts, and the plugins add them as subagents and skills. The
[agent pack guide](https://engineeringcorpus.com/docs/agent-pack) describes them and the hooks.

## The tools

The agents use twelve read-only tools, over stdio or Streamable HTTP, and any MCP client can call them directly:

| Tool | What it returns |
|---|---|
| `corpus_search` | Code by meaning and by exact identifier, one hit per file, with `why` it matched. When the best match is weak for your index, the status says `no_strong_match`. The optional `kind` keeps only decision records, changelogs or agent instructions (skills, prompts, agent and command definitions). |
| `corpus_compare` | Up to five different approaches to one problem, grouped by what the code imports and how it looks. |
| `corpus_explore` | The options that at least two independent repos back for one design question, and the repos that stand alone as leads. |
| `corpus_read`, `corpus_grep` | Lines of a file at the indexed commit, and lines that match a regular expression in one repo. They serve only text the secret scan saw. |
| `corpus_symbols`, `corpus_references`, `corpus_context` | Where a name is defined and used, and a symbol's definition with its callers, tests and docs in one call. |
| `corpus_usage`, `corpus_package` | How real code calls an API, and which repos depend on a package, at which versions, from their lockfiles. |
| `corpus_repos`, `corpus_status` | The indexed repos with their commit, newest upstream tag, archive flag and license verdict, and the counts. |

The same server answers ChatGPT's `search` and `fetch` at `/chatgpt/mcp`. The
[tools reference](https://engineeringcorpus.com/docs/tools-reference) lists every argument and result field.

## Licenses

Public on GitHub does not mean free to reuse. Each file gets a license class from its own SPDX tag, the nearest license file, or
the repo's declared license. Code text comes back for permissive and copyleft files (classes P, B, W and C). Restricted and
unknown files (R and U) return the location only, and a permissive text with restricting terms, such as Commons Clause, counts
as restricted. Verdicts are automated and are not legal advice. The
[license policy](https://engineeringcorpus.com/docs/license-policy) explains each class, and [LICENSING.md](https://github.com/ymcbzrgn/engineering-corpus/blob/main/LICENSING.md)
says how the tool and the code it indexes are licensed.

Anyone can ask for a repo to be left out, with no proof of ownership: use the [removal form](https://engineeringcorpus.com/opt-out) or
write to hello@engineeringcorpus.com with its GitHub address. Every request is handled within 72 hours, and a removed repo comes back only if
its owner agrees.

## Security

Text in the corpus is evidence, never instructions. Betterleaks scans every repo before anything is embedded, and each secret
becomes a `‹secret masked: <rule>›` marker. Hidden and bidirectional Unicode shows as visible `<U+XXXX>` markers. Files written
to steer agents, such as `AGENTS.md`, follow `--agent-files`: `include` serves them (the default), `warn` serves them with a warning, `exclude` hides them. The HTTP server listens on
127.0.0.1, has no authentication, and refuses a non-loopback `--host` without `--allow-remote-bind`. The
[security model](https://engineeringcorpus.com/docs/security-model) says where this stops. To report a vulnerability, see
[SECURITY.md](https://github.com/ymcbzrgn/engineering-corpus/blob/main/SECURITY.md).

## Network

It reaches the network in four cases, each started by something you run:

- `corpus stars` and the archive check during `corpus index` call the GitHub API, for public data. A `GH_TOKEN` or
  `GITHUB_TOKEN` raises the rate limit and is sent only to `api.github.com`: a redirect to any other host is refused.
- `corpus index` clones and fetches the repos you list with `git`, and asks each for its newest version tag.
- The first index or search downloads the embedding model from Hugging Face, about 600 MB, and the first deep search the
  reranker, about 150 MB. Once they are on disk, `corpus serve` and `corpus search` need no network.
- `corpus bench` with `--tool sourcegraph`, `searchcode` or `github` sends the benchmark's queries to those services. The
  default, `--tool engineering-corpus`, stays on your machine.

A search or a read sends your query to nobody, and the engine never checks for updates over the network.

## Limits

Queries go in English: the engine is English only, so have your agent translate a question first. The HTTP server has no authentication (see Security), and a hosted version is planned, not built. Every limit, with where it comes from in the code and what to do, is on [the limits page](https://engineeringcorpus.com/docs/limits).

## Your data and updates

The engine keeps its clones, index, registry and models in one folder per user, `~/.local/share/engineering-corpus`
(`$XDG_DATA_HOME/engineering-corpus` when that is set). `ENGINEERING_CORPUS_DATA` or `--data-dir` picks another one. The
[configuration reference](https://engineeringcorpus.com/docs/configuration) lists every setting.

Each data folder records its index format and embedding model in `format.json`. Every command compares it with the running
engine. When the index cannot be read correctly, the command stops and prints the command to run, usually
`corpus index CONFIG --rebuild`, and it never serves vectors it cannot read. A folder with a newer format than the engine knows
is left untouched. The CHANGELOG says in each release whether a re-index is needed. The
engine never checks for updates over the network: you update through your channel.

Indexing again embeds only the chunks whose text changed, so a re-index after `git pull` takes seconds. To drop repos, run
`corpus remove github.com/OWNER/NAME`, or index a trimmed file with `--prune`.

## Why I built it

The longer version is in [the launch post](https://engineeringcorpus.com/docs/launch).

More than 1,000 starred repos on GitHub, and I can no longer keep track of them. They are my library for learning from other people.

I would hand my agents a link and tell them to take inspiration from it. Two days later they had forgotten it. Without search by meaning we spent a lot of tokens, and the agents made up sources. I tried GitHub code search, Sourcegraph, cloning with grep and the agent's own knowledge, and I still needed this tool.

I reach for it when I design a feature or look for ideas: what did other people think, and how did they make it work?

I have been afraid of licenses for as long as I can remember. Nothing has ever happened to me, and I hope it never does. A dispute over a license is not something I could take on. I want to learn from other people's code on the terms their licenses set, so every result carries a verdict. It is automated and it is not legal advice.

Agents do the studying, and every report ends with a receipt for each source: repository, commit, lines, license class. I wanted every claim to be checkable.

Try it and add your own stars. Report errors and send criticism; contribute if you want to. If you insist on paying me, a hosted version is planned. Everything of ours that runs on your machine, the engine, the agents and every tool, stays MIT and free, and no feature moves to a paid tier; the hosted version would charge only for hosting and a ready-made large index. The hosted beta has a [waitlist](https://engineeringcorpus.com/#waitlist).

## Contributing

Pull requests from outside are welcome, and there is no CLA. [CONTRIBUTING.md](https://github.com/ymcbzrgn/engineering-corpus/blob/main/CONTRIBUTING.md) says how to build and test and what a change has to pass, and [CODE_OF_CONDUCT.md](https://github.com/ymcbzrgn/engineering-corpus/blob/main/CODE_OF_CONDUCT.md) says how everyone treats each other. [ARCHITECTURE.md](https://github.com/ymcbzrgn/engineering-corpus/blob/main/ARCHITECTURE.md) maps the code.

If an agent gets a question wrong, [tell us with the failed-question form](https://github.com/ymcbzrgn/engineering-corpus/issues/new?template=question_wrong.yml): the question, the agent, its receipt block and what was wrong.

## License

MIT. Indexed repositories keep their own licenses.

