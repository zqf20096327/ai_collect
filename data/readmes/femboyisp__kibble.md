<div align="center">

<img src="assets/kibble.png" alt="kibble" width="180">

# kibble

**A fast Rust mass-knowledge & data platform — chew through any source into clean datasets.**

[![crates.io](https://img.shields.io/crates/v/kibble?color=FF9CCB&logo=rust&label=crates.io)](https://crates.io/crates/kibble)
[![docs.rs](https://img.shields.io/docsrs/kibble?color=FF9CCB&label=docs.rs)](https://docs.rs/kibble)
[![downloads](https://img.shields.io/crates/d/kibble?color=FF9CCB&label=downloads)](https://crates.io/crates/kibble)
[![license](https://img.shields.io/crates/l/kibble?color=FF9CCB)](https://github.com/femboyisp/kibble#license)
![tests](https://img.shields.io/badge/tests-386%20passing-FF9CCB)
![made with](https://img.shields.io/badge/powered%20by-chewing%20%F0%9F%A6%B4-FF9CCB)

<img src="assets/kibble-demo.gif" alt="kibble demo — clean, index, search, and grounded cited RAG" width="720">

</div>

`kibble` acquires knowledge and data at scale from almost anywhere (local files, git repos,
websites, HuggingFace datasets, file hosts, archives), extracts and cleans it, classifies and
catalogs it, and builds chat-format JSONL datasets — the raw material for training and retrieval.
It can also run as an HTTP service so bots/automation can submit links for ingestion, and ingest
agent **capabilities** (skills) the same way it ingests data.

The heavy lifting (model training, OCR, embeddings) lives in external backends; `kibble` is the
fast, dependency-light orchestrator that routes to them and turns messy sources into clean,
deterministic, structured datasets and knowledge bases — at volume.

## Install

```bash
# from crates.io (needs a Rust toolchain)
cargo install kibble

# prebuilt binary (Linux / macOS)
curl -fsSL https://github.com/femboyisp/kibble/releases/latest/download/kibble-installer.sh | sh

# prebuilt binary (Windows, PowerShell)
powershell -c "irm https://github.com/femboyisp/kibble/releases/latest/download/kibble-installer.ps1 | iex"

# from source
git clone https://github.com/femboyisp/kibble && cd kibble && cargo build --release
```

Prebuilt targets: Linux x86_64/arm64, macOS Intel/Apple Silicon, Windows x86_64 — see [Releases](https://github.com/femboyisp/kibble/releases).

## Quickstart (30 seconds, no setup)

```bash
cargo build --release
./target/release/kibble index examples/          # BM25 index — no backend needed
./target/release/kibble search "ownership"        # ranked results in ~1s
```

`kibble init` scaffolds this (a `kibble.toml` + sample docs) in any directory.

**What needs a backend?** The core pipeline runs fully offline:

| Works offline (no backend) | Needs an LLM/embed endpoint |
|----------------------------|-----------------------------|
| `clean` · `index` · `search` · `build` · `eval` · `pack` · `crawl` | `ask` · `bench` · `cluster` · `extract` (OCR/ASR) |

(`index`/`search`/`classify` fail soft to lexical-only BM25 when no embed backend is set — they still work, just without semantic ranking.)

## Commands

```
kibble clean                 # apply the text-cleaning rules to stdin → stdout
kibble ingest <source>       # pull a local source (twitter archive, textfiles) into data/raw/local/
kibble fetch <url> [--name]  # download/resolve a URL into data/ingest/<slug>/ (see Handlers)
kibble crawl <url>           # BFS-crawl a site (same-host, robots-safe) → markdown in the ingest tree
kibble extract <path|dir>    # turn artifacts → text (OCR / transcription / PDF / video / office) into data/extracted/
kibble build                 # raw docs + configured sources → train/valid/test JSONL + catalog + stats
kibble tune                  # group the built dataset into phased curriculum + config.yaml (reads [tune])
kibble train                 # run the configured trainer against the tune package (reads [train]; --dry-run; see docs/TRAIN.md)
kibble pack                  # package the build output into a Kaggle dataset bundle (reads [pack])
kibble eval [--strict]       # grade dataset quality (SFT readiness, dedup, leakage, balance); gate CI
kibble index [path]          # build the retrieval index (chunks + embeddings + BM25)
kibble search "<q>" [--k N]  # hybrid semantic + BM25 search over the index
kibble ask "<q>" [--k N] [--web]  # grounded, cited RAG answer over the index (agentic search; --web adds live web search)
kibble cluster [--k N] [--json]  # topic-cluster the dataset rows (embeddings) → data/clusters.json
kibble serve                 # run the ingest HTTP API (POST /ingest, GET /jobs/{id}); needs KIBBLE_API_TOKEN
kibble caps install <path|url>  # pull a source's skills into the capability registry (also: scan/list/remove)
kibble bench [--strict] [--stream]  # benchmark a served model (OpenAI-compatible endpoint); score + latency; gate CI (--stream: live research output to stderr)
kibble soul build            # compile soul.toml → serving artifacts (chat template, gen config, tools, manifest)
kibble mcp                   # stdio MCP server — expose build/eval/bench/soul/caps as tools for an agent/harness
```

The full loop: **fetch/ingest → build → tune → pack → train (Kaggle/Unsloth) → eval.**

### Commands at a glance

Every command does one focused job — point it at a source and it does its thing:

| Command | Label | What it does |
|---------|-------|--------------|
| `fetch` / `serve` | 💨 **Fetch** | pulls in whatever you point it at (URLs, repos, datasets, file hosts) |
| `crawl` | 🕸️ **Crawl** | BFS-crawls a whole site → clean markdown (robots-safe, polite, SSRF-guarded) |
| `extract` | ⭐ **Extract** | turns the artifact into text — OCR / transcription / PDF / video / office |
| `clean` | 🌬️ **Clean** | strips out the junk (mentions, URLs, hashtags, zero-width) |
| `build` | 🍳 **Build** | combines everything → a chat-format dataset (**dedups + leakage-safe split**) |
| `tune` | 🎓 **Tune** | groups the dataset into phased curriculum by source + trainer config (**sprint/** layout) |
| `pack` | 🎁 **Pack** | bundles the dataset for Kaggle/Unsloth training |
| `eval` | 📊 **Grade** | grades dataset quality (readiness, dedup, leakage, balance, diversity) + gates CI |
| `caps` | ✨ **Copy skills** | pulls in a repo's **skills** and keeps them in your registry |
| `bench` | 🥊 **Bench** | benchmark a served model (quality + speed) against your suite; gate CI |
| `soul` | 👻 **Soul** | compile `soul.toml` → serving artifacts (system prompt, sampling, tools, chat template) |
| `mcp` | 🌐 **Serve tools** | expose the whole toolkit as MCP tools an agent/harness can drive (stdio JSON-RPC) |

## Capabilities (`kibble caps`)

Skill installation applied to the agent itself: consume a source and **gain its skills**. Point
`caps` at a local path or URL (URL sources reuse the `fetch` handlers — git/archive/http), and any
`SKILL.md` skills are installed into a managed registry:

```bash
kibble caps install https://github.com/you/skills-repo   # detect + install skills (--force, --project)
kibble caps scan <path|url>     # dry-run: list what would install
kibble caps list                # installed skills
kibble caps remove <name>       # uninstall
```

Skills land under `<root>/skills/<name>/` with an index at `<root>/registry.json` (`[caps].root`,
default `~/.kibble/caps`; `--project` for a repo-local `.kibble/caps`). Install is **copy + register
only** — skill scripts are never executed; names are sanitized, dests confined under the skills
root, symlinks skipped, inputs size-capped. This is the foundation of the agentic-harness layer
(exposing the registry over MCP, assembling agent configs, and an autonomous build/tune loop are
next).

## Sources (`kibble.toml`)

`build` ingests the local raw tree **plus** any `[[source]]` declared in `kibble.toml`. Source
types are auto-detected from the path (with an explicit `type` override):

```toml
[[source]]
path = "https://github.com/you/repo"   # codebase (cloned, scanned)
[[source]]
path = "data/external/chat.jsonl"      # dataset (folded into the splits)
system_prompt = "Answer concisely and accurately."  # optional per-source prompt injection
[[source]]
path = "https://blog.example.com/post" # web (fetched → main text extracted)
[[source]]
path = "notes/"                        # files dir (.txt/.md → prose rows)

[network]
proxy = "socks5://127.0.0.1:9050"      # all outbound traffic is proxy-aware (else *_PROXY env)

[paths]
data_root   = "data"                   # raw/catalog/mirror base
dataset_dir = "data/datasets/unsloth"  # where build writes splits + stats
```

Auto-detection covers: **dataset** (`.jsonl`), **codebase** (git URL or code dir), **web** (URL),
**blog** (`.html`), **files** (`.txt`/`.md` dir). Code content bypasses the prose cleaner
(`$VAR`/URLs/paths preserved); prose is cleaned.

**Curation (`[curate]`):** before writing, `build` drops malformed / degenerate / too-short rows,
deduplicates identical answers, and splits **by answer content** (`SHA256(answer) %100` → 78/12/10)
so identical answers can never land in two splits — making exact train↔valid/test leakage
impossible by construction. An **opt-in MinHash near-dup pass** (`near_dedup`) additionally collapses
near-paraphrase/boilerplate answers. Deterministic; `stats.json` reports `dropped_duplicates`,
`dropped_filtered`, and `dropped_near_duplicates`.

## Handlers (`kibble fetch` / the serve API)

`fetch` and `/ingest` route a URL to the right downloader, staging the result into the ingest
tree for `build` to consume — point kibble at a link and it pulls it in:

- **git** — shallow clone (proxy-aware, argv-guarded)
- **HuggingFace dataset** — list + download via the hub API
- **open HTTP directory** — crawl `<a href>` links; **direct HTTP file** — stream download
- **archives** — `.zip` / `.tar.gz` extracted (zip-slip & symlink safe)
- **Dropbox / Google Drive / MediaFire / gofile** — share-link resolvers
- **mega.nz** — public file & folder links, downloaded and **decrypted** (hand-rolled AES-128)

Every download is size-capped and writes traversal-safe filenames.

## Serve API

A job queue — point automation at it and jobs come riding in:

```bash
KIBBLE_API_TOKEN=… kibble serve     # fail-closed: refuses to start without a token
```

> **Secrets / `.env`:** kibble auto-loads the nearest `.env` (working dir upward)
> at startup, so `OCR_API_KEY`, `KIBBLE_API_TOKEN`, `OPENAI_API_KEY`, etc. don't
> need `source`-ing. Real env vars always win. Copy `.env.example` → `.env`
> (gitignored). No `.env` present → nothing happens.

- `GET /health` (open) · `POST /ingest {url,name?}` → `{job_id}` · `GET /jobs/{id}` → status
- Bearer-token auth on ingest/jobs; an **SSRF guard** rejects loopback/private/link-local IPs
  (incl. IPv4-mapped IPv6 and userinfo tricks) with an `allow_hosts` bypass; in-memory job
  registry. Default bind is `127.0.0.1`; front with a reverse proxy to expose it.

## Eval

`kibble eval` grades a built dataset's **training-readiness and quality** (SFT) — valid-row /
malformed check, exact+normalized **duplicate** rate, train↔valid/test **leakage**, length
distribution, source **balance** (from `stats.json`), **degenerate** rows, and answer **diversity**
(distinct-2). It writes `report.{json,md}` with a 0–100 score and per-metric thresholds; **overall
PASS iff every gated metric passes**. An **opt-in** near-dup pass (`[eval].near_dup`) adds
`near_duplicate_rate` + `near_leakage_rate` (MinHash) so the gate also certifies fuzzy/paraphrase
duplication and leakage. When `clusters.json` is present, the `max_topic_share` metric gates on
topic balance (default threshold `0.60`), with fail-soft skipping if the embed backend is unavailable.

```bash
kibble eval            # report only
kibble eval --strict   # exit 1 if the dataset fails the gate (block CI / a build)
```

Thresholds live under `[eval.thresholds]` (see `docs/EVAL.md`). On a real 59k-row corpus it caught
14% train/valid leakage and 8.5% duplicates — exactly the issues that silently wreck a fine-tune.
Active curation that *fixes* a failing dataset (dedup/filter/rebalance in `build`) and DPO/
pretraining formats are the next steps.

## Understand layer (embeddings)

A dense-embedding backend (any OpenAI-compatible `/embeddings` endpoint) with a content-hash
**vector store/cache** (`data/embeddings/`, reused across `build` → `eval`), plus a hand-rolled
**SimHash LSH** for cosine near-duplicate search. No new crate dep. Two consumers, both **opt-in**
and fail-soft (unconfigured/unreachable endpoint → skipped with a warning, `build`/`eval`
unaffected):

```toml
[understand.embed]
base_url = "http://localhost:8090/v1"  # empty (default) = disabled
model    = "nomic"
```

- `[curate].semantic_dedup` (default off) — collapses near-paraphrase answers, keeping the
  longest; reported as `dropped_semantic_duplicates`.
- `[eval].semantic` (default off) — adds `semantic_near_duplicate_rate` + `semantic_leakage_rate`,
  gated into the score and `--strict`.

Keys come from `EMBED_API_KEY` / `OPENAI_API_KEY` (env only, optional on a trusted LAN). See
`docs/UNDERSTAND.md` for the full config, store format, and the recommended rollout (enable
`[eval].semantic` first — read-only — then `[curate].semantic_dedup` once the numbers look right).

## Cluster

`kibble cluster` groups the built dataset's answers into topics using **deterministic spherical k-means**
(k-means++ seeding, fixed PRNG seed, up to 50 iterations) on their embeddings. Each topic is labeled
by its most **distinctive terms** (high TF-IDF in-cluster, rare across clusters; no LLM). Centroids
are stored in `clusters.json` and feed the `eval` dataset-balance gate (`max_topic_share`, #25)
and build-time topic rebalancing.

```toml
[cluster]
k               = 12                   # default: target number of topics
enabled         = true                 # default
out             = "data/clusters.json" # default
rebalance       = false                # default: cap over-represented topics in build
max_topic_share = 0.35                 # default: cap topics at 35% of train (build-side)
llm_labels      = false                # default: opt-in for LLM-named labels

[understand.embed]
base_url = "http://localhost:8090/v1"  # reused from understand layer
model    = "nomic"
```

Cluster is **opt-in and fail-soft**: if the embed backend is unconfigured or unreachable, clustering
is skipped with a warning — `kibble build` completes unaffected and `kibble cluster` still succeeds.

```bash
kibble cluster           # cluster with [cluster].k (default 12)
kibble cluster --k 8    # cluster into exactly 8 topics
kibble cluster --json   # emit JSON (see docs/CLUSTER.md)
```

When `[cluster].rebalance = true`, `kibble build` clusters the curated train in-memory, caps over-represented topics by dropping their fringe rows, and writes the resulting `clusters.json` — so `eval` reads the same centroids and converges in one build. When rebalance is off and `[cluster].enabled = true`, clustering runs on all splits at the end of build (unchanged path). Set `[cluster].llm_labels = true` to replace distinctive-term labels with LLM-generated topic names (reuses the `[ask]` endpoint; fail-soft if unavailable). See `docs/CLUSTER.md` for full details.

## Retrieve / search

`kibble index` chunks the corpus, embeds each chunk via the shared `[understand.embed]` cache, and
builds a hand-rolled **BM25** inverted index; `kibble search` ranks passages by **Reciprocal Rank
Fusion** of BM25 + semantic cosine. Both fail soft to lexical-only (BM25) when no embed backend is
configured, the endpoint is unreachable, or the index was built with a different model:

```toml
[index]
dir         = "data/index"                                     # default
sources     = ["data/raw", "data/ingest", "data/extracted"]     # default
chunk_chars = 800                                                # default
rrf_k       = 60                                                 # default
```

```bash
kibble index                          # build/rebuild the index from [index].sources
kibble search "how does X work" --k 5 --json   # hybrid search → table or JSON hits
```

Writes `data/index/{chunks.jsonl,bm25.json,meta.json}`; a missing/empty index errors with
`run kibble index first`. No new crate dep; deterministic offline tests. See `docs/RETRIEVE.md` for
the full behavior, output shapes, and fail-soft details.

## Ask / RAG

`kibble ask "<question>"` answers questions **grounded in the indexed corpus**: it seeds a
`search`, then lets a served LLM call a `search_corpus` tool up to `[ask].max_rounds` times to dig
further before answering with `[n]` citations — or, when the corpus doesn't cover it, an
interactive not-found flow (provide a source & retry / add detail & retry / `--chance`
general-knowledge fallback, flagged ungrounded). **Always shows grounding:** cited sources, or the
retrieved passages that fed an uncited answer, or a `⚠` when it's general knowledge. Reuses the
`retrieve` index and a shared OpenAI-compatible chat helper (also used by `bench`); retrieval stays
fail-soft, but `ask` needs a served LLM (`[ask].base_url`) — that part is a hard dependency, unlike
`search`.

```toml
[ask]
base_url    = "http://localhost:8000/v1"       # served LLM (empty → hard error)
model       = "kibble-style"
temperature = 0.2
max_tokens  = 1024
k           = 6            # passages per search_corpus call
max_rounds  = 3            # agentic search iterations

[web]
base_url    = "https://localhost:8888"   # SearXNG instance; empty → DuckDuckGo scrape fallback
default     = false                          # web tools off unless --web overrides
max_results = 5
allow_hosts = []
fetch_bytes = 2000000
fetch_chars = 4000
```

**Point `ask` at any OpenAI-compatible server** (Ollama, LM Studio, vLLM, llama.cpp):

```toml
# kibble.toml
[understand.embed]
base_url = "http://localhost:11434/v1"   # e.g. `ollama pull nomic-embed-text`
[ask]
base_url = "http://localhost:11434/v1"   # e.g. `ollama pull llama3.2`
model    = "llama3.2"
```

Or copy the fully-annotated template: `cp kibble.toml.example kibble.toml`.

```bash
kibble ask "how does the retry backoff work"
kibble ask "what's the SSRF guard policy" --k 8 --json
kibble ask "who wrote the original BASIC interpreter" --chance
kibble ask "what changed in the latest Rust release" --web
```

`--web` (or `[web].default = true`) additionally gives the model `web_search`/`fetch_page` tools —
it prefers the corpus and only reaches the web when needed; `--no-web` forces corpus-only for one
query. Citations are tagged **`[local]`** vs **`[web]`** in the `Sources:` list (`--json` gets a
`"kind"` field); fetched pages are cited for that answer only, never added to `data/index`.

Answers **stream token-by-token** in a terminal as the model generates them (`[ask].stream`,
default on; `--no-stream` to disable, `--stream` to force it) — piped output buffers instead, and
`--json` buffers into a single object unless paired with `--stream`. **`--json --stream` streams
NDJSON events** for programmatic consumers (search/token events → terminal answer/notfound event;
no TTY required).

Key comes from `ASK_API_KEY` / `OPENAI_API_KEY` (env only). No new crate dep; deterministic
offline tests via a scripted-chat seam and localhost mocks for web mode. See `docs/ASK.md` for the
agentic loop, the not-found flow, web-augmented answers, streaming, and output examples (found /
not-found / `--chance`).

## Library usage

kibble is also a **library**, not just a CLI — link it directly instead of shelling out to the
binary and parsing stdout. A search/ask-only consumer takes the lean **`retrieval`** feature,
which drops the heavy ingest/build/crawl/serve tree (`parquet`, `axum`, `pdf-extract`,
`tar`/`zip`/`aes`); the default **`full`** feature is everything (what the `kibble` binary uses).

```toml
# lean consumer — just search + ask (+ web):
kibble = { git = "https://github.com/femboyisp/kibble", default-features = false, features = ["retrieval"] }
```

The API is async (tokio) and returns typed results. Errors are clean `Err`s, never panics
(e.g. an unset `[ask].base_url` surfaces as an `io::Error`, not a crash):

```rust
use std::path::Path;
use kibble::ask::{AskOptions, AskEvent, Outcome};

let root = Path::new(".");                       // dir holding kibble.toml + data/index

// hybrid BM25 + semantic search → typed hits (runs the blocking read on the blocking pool)
let hits = kibble::retrieve::search(root, "how does the retry backoff work", 5).await?;

// buffered grounded RAG → the whole Outcome at once
let out: Outcome = kibble::ask::query(
    root, "what's the SSRF guard policy",
    AskOptions { web: true, ..Default::default() },   // { k: Option<usize>, web: bool, chance: bool }
).await?;

// streaming grounded RAG → search progress + answer tokens + final cited result, as they happen
use tokio_stream::StreamExt;
let mut stream = kibble::ask::query_stream(root, "explain the ask loop", AskOptions::default())?;
while let Some(ev) = stream.next().await {
    match ev {
        AskEvent::Search { query, kind } => { /* "⋯ searching corpus" — SearchKind::{Corpus,Web,Fetch} */ }
        AskEvent::Token(t)               => print!("{t}"),           // one answer-text delta
        AskEvent::Done(outcome)          => { /* terminal: Outcome::{Answered{answer,sources,..},NotFound} */ }
    }
}
```

`query`/`query_stream`/`search` futures are `Send`, so they compose with `tokio::spawn`,
`select!`, and `Send`-bound async traits. `query_stream` returns `io::Result<impl Stream<Item =
AskEvent> + Send>` — setup errors are a typed `Err` *before* streaming; the final result rides as
the terminal `AskEvent::Done`.

## Bench (model benchmarks)

Where `eval` grades the *dataset*, `kibble bench` grades the *model*. Point it at any
OpenAI-compatible endpoint (your vLLM / MLX server), run an **extensible** benchmark suite, score
quality **and speed**, and gate:

```toml
[bench.model]
base_url = "http://localhost:8000/v1"
model    = "style-lora"
[[bench.benchmark]]
name = "knowledge"
path = "benchmarks/knowledge.jsonl"
method = "contains"      # contains | mcq | judge
threshold = 0.7
```

```bash
kibble bench            # score + latency report → bench/report/{report.json,report.md}
kibble bench --strict   # exit 1 if the model fails the gate (CI)
```

A benchmark = a `[[bench.benchmark]]` entry + a `cases.jsonl`; **add a file → add a benchmark**
(see `docs/BENCH.md`). This is the loop's "did the model get better / is it fast enough?" signal.
A **web-research / tool-execution** method (`method = "research"`) runs an agentic loop — the model
calls `web_search` / `fetch_page` (SearXNG or DuckDuckGo + KIBBLE's page fetch), the harness executes
them, and the final answer is scored + timed end-to-end (the measurable "beat-Perplexity"). `fetch_page`
is SSRF-guarded + byte-capped. Add `--stream` to watch the model's research output live on stderr
(research-only; scoring and stdout are unchanged). See `docs/BENCH.md`.

## Extract

`kibble extract <path|dir>` turns artifacts into clean text (the extraction layer),
staged under `data/extracted/` for `build` to consume (`fetch → extract → build`):

- **image → OCR** and **audio → transcription** via a configured OpenAI-compatible endpoint
  (e.g. an Unlimited-OCR / Whisper server), with a local-CLI fallback (`tesseract`, `whisper`)
- **PDF** — text-layer via `pdf-extract`; scanned/sparse PDFs render with `pdftoppm` → OCR
- **video** — `ffmpeg` pulls the audio track → transcription
- **office** (docx/odt/…) — `pandoc` → plain text
- **html/text** — main-text extraction / passthrough

Each backend tries the endpoint, then a CLI, then errors clearly. Keys come from env only;
CLIs are invoked via arg-vectors with canonicalized paths (no shell, no flag injection); inputs
are size-capped. Configure under `[extract]` / `[extract.ocr]` / `[extract.transcribe]` /
`[extract.pdf]` / `[extract.video]` / `[extract.office]`.

## Cleaning rules

`clean` strips, in order: zero-width/replacement chars; `@mentions` (emails preserved);
`http(s)://` URLs; `#hashtags`, `$TICKERS`, `r/subreddits`; Discord invites; brackets left empty
after stripping — then normalizes whitespace.

## Roadmap

`kibble` is a **consume-anything** ingestion & dataset platform built as a layered stack
(discover → acquire → extract → understand → curate → retrieve → **answer** → tune). **Shipped:**
acquisition (`fetch`/`serve` + handlers incl. git/HuggingFace/Dropbox/Drive/MediaFire/gofile/mega),
the full extractor (`extract`: OCR / transcription / PDF / video / office), `build`/`pack`/`eval`,
the `understand` layer (embeddings + semantic dedup/leakage), the `retrieve` layer (`index`/`search`
— BM25 + semantic hybrid, RRF-fused), and the `ask` layer (`kibble ask` — agentic, cited RAG).
**Next:** web-augmented `ask` (SearXNG-backed research beyond the corpus), embedding-based
auto-classify/clustering, a tunable training mix, and an auto-tune harness with observability. See
`CHANGELOG.md` and the design specs for the layered roadmap.

## Development

**386 tests**, all offline (localhost mocks + stub binaries, no real network/tools), clippy clean:

```bash
cargo test       # offline tests (no network/external tools — localhost mocks + stub binaries)
cargo clippy
```

## License

Licensed under either of [MIT](LICENSE-MIT) or [Apache-2.0](LICENSE-APACHE) at your option.
Contributions are welcome — pre-1.0, so expect sharp edges 🦴
