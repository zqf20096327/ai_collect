# VulnDog

[![CI](https://github.com/Keutonim/VulnDog/actions/workflows/ci.yml/badge.svg)](https://github.com/Keutonim/VulnDog/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/runtime%20deps-0-orange)]()

<p align="center">
  <img src="assets/vulndog.png" alt="VulnDog — passive proxy companion for active vulnerability hunting" width="720">
</p>

**VulnDog is a companion for active vulnerability hunting: you send the requests, it tells you which of them look like something worth chasing.**

It runs as a local proxy on your machine, watches the traffic *you* route through
it, and scores each request against an offline knowledge base of 456k CVE/CWE/exploit
records. Everything it surfaces is an advisory candidate, never a finding — it flags
a request as matching a known pattern, and confirming whether that matters is still
your job. It never issues requests of its own.

Zero dependencies, stdlib Python, local Ollama embeddings for semantic matching,
no cloud by default, MIT licensed.

> **Status: the capture → analysis pipeline, config v2, scope/SSRF rail,
> MCP server, AI-provider layer, and the `db` store-management surface are
> shipped** (`src/vulndog/`), unified behind the `vulndog` console entry
> (M2.5): the observing proxy, timestamped run folders, redaction-before-persist,
> the offline matching engine, and `vulndog db build / info / verify` (M3.1)
> all work today via `vulndog …` (or `python -m vulndog …`). The CI/release
> workflow scaffolding is in place (M3.3), the docs are finalized (M3.2), and
> the independent-extension validation is shipped (M3.4 — stranger
> walkthroughs, re-proven by permanent offline tests): **all milestones
> M1.1–M3.4 are delivered**. Still planned (see PLAN.md for the milestone
> table): the first public release — **no store ships in the tree yet** and
> there are no releases (store distribution awaits the GAP-1 decision).

---

## Why VulnDog

When you are hunting, you fire hundreds of requests at a target and most of them
are noise — a handful might match something known, and those are the ones you want
in front of you early rather than on page nine of a proxy history. VulnDog exists
to close that gap: it watches the traffic you route through its local proxy and
flags the requests that match patterns in its offline knowledge base of 456k
CVE/CWE/exploit records, so you can focus on the promising directions instead of
reading every line by hand.

The tool is strictly an observer. It never sends requests of its own, every test
stays in your hands, and everything it raises is an advisory candidate — a match
against a known pattern, not a confirmed vulnerability. The knowledge base,
matching, and the optional embeddings (local Ollama) all run on your machine;
stdlib Python, zero runtime dependencies.

**MCP bonus for agent-driven testing:** if you run an AI agent through tool-calling
loops (browser automation, scanner batteries), it can query VulnDog over MCP
(`vuln_query`, `highlights`, `run_status`) to ask which of its own requests matched
known patterns — a feedback loop that helps the agent lean into promising directions
instead of fuzzing blind. But the tool is for hunters first; MCP is one interface,
not the identity.

## How the engine works (hybrid: rules + local embeddings, zero cloud LLM)

VulnDog's engine is a fully reused, production-proven core (690 tests green at the
2026-10-28 state) with a deterministic pipeline plus one local ML step:

```
proxied request
  → tap (pure observer, bounded queue)          # redaction happens BEFORE persist
  → events.jsonl (redacted spool, per-run dir)
  → event text shaping                          # deterministic
  → query embedding via local Ollama            # the one ML step
  → FTS5 BM25 prefilter (top-500)               # deterministic SQL
  → cosine re-rank vs pre-embedded KB vectors   # pure Python
  → score floor (0.49, calibrated) + top_k      # deterministic
  → regex "exact-id pins" for literal CVE-/CWE- tokens
  → highlights (highlights.jsonl + highlights.md)
```

- **No cloud LLM calls, ever.** The only model service is a local Ollama
  *embedding* endpoint (`/api/embed`, model `embeddinggemma:300m`, 768-d vectors).
  There is no chat completion, no prompt, no per-request LLM verdict anywhere in
  the pipeline. See docs/AI-INTEGRATION.md.
- **The embedder is required for matching** (including exact-id pins): with the
  embedding backend down, matching enters a buffer-and-retry down-mode and no
  highlights are produced until it recovers. There is no fts-only fallback in v1 —
  see docs/AI-INTEGRATION.md ("When the embedder is down").
- **Redaction before persist.** Query values are length-masked (`<len-N>`), secret
  look-alikes are replaced (`<redacted>`), and anything that fails redaction is
  dropped fail-closed. See docs/RUNS-AND-LOGS.md.

## Features

| # | Feature | Notes |
|---|---|---|
| 1 | **CLI-only interface** | shipped entry: `vulndog run / status / version / mcp / db` (console script after `pip install .`; `python -m vulndog …` is the equivalent module form); English product language |
| 2 | **Configurable proxy** | local observing forward proxy, loopback by default (`--host` / `--port`); Mode A only — absolute-form HTTP + CONNECT tunnel. A non-loopback bind requires `--allow-remote-bind` **plus** a client credential (`--client-token` / `--client-allow`), otherwise the proxy refuses to start |
| 3 | **Per-run timestamped folders** | every run creates `runs/<YYYYMMDD-HHMMSS>[-<tag>]/` inside the project, containing the flagged-request log (`highlights.jsonl` / `highlights.md`) |
| 4 | **Scope + SSRF rail** | in/out host patterns (exact or `*.suffix`; out wins) — out-of-scope requests get HTTP 403 and never leave the machine; under that, an SSRF rail **default-denies private/loopback/link-local/metadata targets** (`--allow-private` to opt in) |
| 5 | **Built-in vulnerability DB** | offline SQLite knowledge base built from CVE (cvelistV5), ExploitDB, CWE, OWASP Top 10 archives — 456,460 records / 437,782 chunks in the full corpus |
| 6 | **Optional AI hook** | semantic matching via local Ollama embeddings (default) or a custom provider config; reacts to requests and searches vulnerability matches |
| 7 | **MCP server** | first-class consumers are AI agents: stdio JSON-RPC MCP server exposing `vuln_query`, `highlights`, `run_status` — shipped, run it with `vulndog mcp` (docs/MCP.md) |
| 8 | **Proven engine, fully reused** | the `vuln_watchdog` core is vendored unchanged (module names identical); no redesign of what works |
| 9 | **Advisory-only semantics** | output is "candidate / never a finding"; no auto-promotion; the engine issues zero target-bound requests |

**Explicit non-features** (so nobody expects them): no GUI (CLI only), no
MITM/TLS decryption (owner-rejected permanently), no LLM verdicts or prompt-driven
reasoning (embeddings only).

## Safety posture (shipped)

The proxy is network-facing code, so its safety floors are explicit:

- **SSRF rail (default-deny).** Requests to loopback, RFC1918, link-local
  (including the cloud-metadata address `169.254.169.254`), CGNAT
  `100.64.0.0/10`, IPv6 ULA/link-local, `localhost` and `*.internal` names are
  refused with 403 (`denial_reason:"proxy_private"`) before any upstream socket —
  on both the HTTP and CONNECT legs, under any scope. Numeric IP spellings
  (decimal/hex/octal shorthand) are normalized before classification, and other
  names are classified at connect time against their **resolved** address: a
  public name that resolves to a private address (DNS rebinding) is denied, and
  the connection uses that classified address — one resolution per request, no
  re-resolution at connect. Honest residual: a DNS record flipping between
  separate resolutions across requests (the rebinding TOCTOU) is a narrow known
  race — the socket never re-resolves the name, but there is no resolver-level
  pinning; treat the rail as a floor, not a full SSRF defense. `--allow-private`
  is the explicit opt-in for testing private targets (it skips the rail but
  keeps the single-resolution pinning).
- **No accidental open relay.** `--allow-remote-bind` (a non-loopback listen
  address) **refuses to start** unless you also pass `--client-token <secret>`
  (per-request `Proxy-Authorization: Bearer <token>` check, constant-time
  compared) or `--client-allow <cidr>`. The credential is hop-by-hop: it is
  never forwarded to the origin and never written to disk. Loopback binds (the
  default) need no credential.
- **Resource brakes.** Concurrent connections are capped — excess connections
  are answered 503 before a handler thread spawns; the event queue drops oldest
  at 1000 and reports the delta as a `drop_counter` meta line; the per-run
  spool freezes at 100 000 events behind a visible `spool_cap` marker. Every
  drop/refusal class is counted in the run state (`watchdog-run.json`).
- **Redaction before persist.** One fail-closed redaction door: the spool and
  the flagged-request log both derive from redacted data, and anything that
  fails redaction is dropped and counted, never persisted raw. The limits of
  that guarantee are documented honestly in docs/RUNS-AND-LOGS.md.

## What the proxy can and cannot see (visibility matrix)

| Traffic | What VulnDog inspects | Why |
|---|---|---|
| Plain HTTP (absolute-form requests) | full request: method, URL incl. path, params (names kept, values length-masked), status, content type, redacted body | leg is not encrypted |
| HTTPS (CONNECT) | tunnel-level metadata only: host:port, timing, tunnel events (no path, no body) | the tunnel is relayed opaque; MITM/TLS interception is **rejected by design** |

Most real-world traffic is HTTPS — plan your expectations accordingly. If you need
request-level inspection of an HTTPS target, front it with plain HTTP in your own
test rig or use a target that speaks HTTP.

## Quick start

Prerequisites: Python >= 3.11; a local Ollama with the embed model
(`ollama pull embeddinggemma:300m`) for analysis; and a vulnerability store —
**no store ships in the tree yet**, so build one (see docs/VULNERABILITY-DB.md)
or pass `--store <path to vulnkb.sqlite>`.

```text
# install (zero runtime dependencies)
pip install .

# capture + analyze — proxy on 127.0.0.1:8080, Ctrl-C to stop
vulndog run
vulndog run --store /path/vulnkb.sqlite --duration 300

# point your tool / test rig at the proxy (default 127.0.0.1:8080)
# read flagged candidates when the run stops:
#   runs/<YYYYMMDD-HHMMSS>/highlights.md       (human)
#   runs/<YYYYMMDD-HHMMSS>/highlights.jsonl    (machine)

# show the latest run (pid liveness, counters, stop state)
vulndog status                      # add --json for machine-readable output

# AI agents: start the MCP server over stdio (setup: docs/MCP.md)
vulndog mcp --project .

# build / inspect / verify the vulnerability store (needs a local Ollama;
# full surface: docs/VULNERABILITY-DB.md)
vulndog db build --raw-dir <dir-with-4-archives>
vulndog db info
vulndog db verify
```

Every command above also works as `python -m vulndog <subcommand>` without
the console script. `vulndog db` (store management — `build` / `info` /
`verify`, plus a release-asset dry-run) is shipped (M3.1); see
docs/VULNERABILITY-DB.md.

A run without a reachable store still captures and preserves every event.
When captured events meet a down or disabled match path (missing store,
embedder outage, analysis failure), the run exits 4 with an actionable message
("build one … or pass --store") — an unanalyzed run is never reported as a
clean "no vulnerabilities" result. Exit 4 means analysis was skipped or
failed, never "no vulnerabilities found"; a run that captured zero events
exits 0 (empty-spool semantics).
Full flag surface: docs/CONFIGURATION.md. Run-folder layout and formats:
docs/RUNS-AND-LOGS.md.

## Using VulnDog responsibly

VulnDog is a passive monitoring tool for traffic **you are authorized to test**.
It never sends requests to targets and never modifies traffic. You are responsible
for complying with the laws and scopes that apply to what you point through the
proxy. Run directories contain real target hostnames from your traffic — treat
them as sensitive and never redistribute them.

## Documentation index

| Doc | Contents |
|---|---|
| [PLAN.md](PLAN.md) | phased implementation plan: milestones, acceptance criteria, deltas, risks |
| [docs/CONFIGURATION.md](docs/CONFIGURATION.md) | CLI flags, config file + 3-layer merge, scope, proxy settings, thresholds, mutes |
| [docs/RUNS-AND-LOGS.md](docs/RUNS-AND-LOGS.md) | run folder layout, flagged-request log formats with real examples, redaction guarantees and limits |
| [docs/MCP.md](docs/MCP.md) | MCP server for AI agents: transport, tools, agent setup |
| [docs/VULNERABILITY-DB.md](docs/VULNERABILITY-DB.md) | built-in vuln DB: sources, schema, build pipeline, seed/full/subset options, how to populate and extend it yourself |
| [docs/AI-INTEGRATION.md](docs/AI-INTEGRATION.md) | the AI hook: Ollama setup, custom provider config, outage behavior |
| [CONTRIBUTING.md](CONTRIBUTING.md) | dev setup, running the tests, adding a KB recipe, extending docs, commit style |
| [SECURITY.md](SECURITY.md) | supported versions, reporting a vulnerability in VulnDog itself, the tool's safety model |

## License

VulnDog ships a **MIT** license: the `LICENSE` file at the repository root plus
the `license` declaration in `pyproject.toml`. The choice is **provisional** —
it stands in until the owner's final licensing decision (PLAN.md GAP-1, which
also covers the per-source data-terms review for the redistributable
vulnerability store).

> Decision pending: license choice — a provisional **MIT** `LICENSE` ships
> today (recommended default, owner to confirm; alternatives considered:
> Apache-2.0).
