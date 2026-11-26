<p align="center">
  <img src="assets/logo.png" alt="Justless logo" width="140">
</p>

<h1 align="center">justless</h1>

<p align="center">
  <strong>Up to 171× less for your coding agent to read.</strong><br>
  One local offline Rust binary instead of RTK + graphify + Serena + Headroom + code-review-graph + Repomix. Compact by default, exact on demand.
</p>

<p align="center">
  <a href="#install">Install</a> · <a href="docs/reference.md">Reference</a> · <a href="docs/examples.md">Examples</a> · <a href="docs/benchmarks.md">Benchmarks</a> · <a href="docs/comparison.md">Comparison</a> · <a href="CHANGELOG.md">Changelog</a>
</p>

<p align="center">
  <strong>171×</strong> smaller doc outlines · <strong>154×</strong> smaller code-graph answers · <strong>88×</strong> smaller searches · <strong>23×</strong> less across 18 real workloads · <strong>0</strong> network calls
</p>

**justless** sits between your coding agent and its tools. It turns verbose command output into structured, line-referenced reports, answers code and PR blast-radius questions from a local **code graph** so the agent stops reading whole files, outlines single files and whole directories on demand, and keeps every byte it cuts one command away.

> **🔒 100% local. Zero network calls.** No telemetry, no cloud, no LLM, no account: your code and command output never leave your machine. The one opt-in exception, `justless wrap claude` / `justless proxy`, only relays your client's own API requests.

## How much it saves

Freshly measured offline with the release binary (`scripts/suite_benchmark.py` and the companion benchmark scripts, Linux):

| What your agent does | Without justless | With justless | Cut |
| --- | ---: | ---: | ---: |
| Large Markdown outline: `docs/reference.md` (1,142 lines), outline / + exact 794 B `expand` | 273,594 B | 1,598 B / 2.3 KB | **171×** / **114×** |
| "Where is `X` and what calls it?": search + read vs. `justless query X` (13 unique functions) | 1,095,276 B | 14,930 B | **71×** median, up to **154×** |
| Live checkout search: `rg -n "fn " src` (4,661 matches in 95 files) | 357,380 B | 4,058 B | **88×** |
| CI checks + security audit: `gh pr checks` (61 checks) + `pnpm audit` (13 vulns) | 33.0 KB | 564 B | **60×** |
| Interleaved cluster logs: `kubectl logs` (500 lines) | 45.9 KB | 1.1 KB | **41×** |
| Container build: `docker build` (350-line BuildKit log) | 18.4 KB | 498 B | **38×** |
| Failing Rust test: `cargo test` on [`fixtures/failing`](fixtures/failing) (380 → 9 lines) | 18,038 B | 517 B | **35×** |
| Directory code skeleton: `justless read src/proxy --outline` (7 files, 3,114 lines) | 112.9 KB | 4.1 KB | **28×** (96.4% cut) |
| Failing Python suite: `pytest` (50 parametrized + collection error) | 19.7 KB | 741 B | **27×** |
| Semantic diff + lockfile: `git diff` (whitespace/rename + lockfile folding) | 12.2 KB | 490 B | **26×** |
| **Full 18-workload compactor suite** (`scripts/suite_benchmark.py`) | **1,157.5 KB** | **49.4 KB** | **23.4×** (95.7% cut) |
| Progressive Python outline + 60 B exact `expand` + 88 B verified `edit` | 20,991 B | 1,671 B + 148 B | **12.6×** |
| Kubernetes inventory + pod details: `kubectl get pods` + `kubectl describe pod` | 18.3 KB | 1.6 KB | **12×** |
| Infrastructure plan + deps: `terraform plan` (120 refreshes) / `cargo tree` (400 lines) | 14.6 KB / 15.7 KB | 1.3 KB / 1.5 KB | **11×** / **11×** |
| Lossless structured data: `gh api` JSON (80 objects) / `psql` table (500 rows) | 30.2 KB / 27.5 KB | 3.6 KB / 4.0 KB | **8.3×** / **6.8×** |
| Three-turn repair task, provider input tokens (Claude Haiku, Sonnet, Opus 5.5, Fable 5.2) | 22.4–22.8k | ~2.85k | **8×** |

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/savings-dark.svg">
  <img src="assets/savings-light.svg" alt="Paired horizontal bar chart of bytes an agent received across 18 reproducible workloads: 1,157.5 KB raw versus 49.4 KB with justless (95.7% smaller, 23.4×). Top 14 bars on a linear 0 to 400 KB axis: rg -n &quot;fn &quot; src 349.0 KB to 4.0 KB (88×), read --outline plus expand 267.2 KB to 2.3 KB (114×), query + map + mask 264.9 KB to 22.6 KB (12×), kubectl logs 45.9 KB to 1.1 KB (41×), gh checks + audit 33.0 KB to 564 B (60×), gh api JSON 30.2 KB to 3.6 KB (8×), psql table 27.5 KB to 4.0 KB (7×), pytest 19.7 KB to 741 B (27×), docker build 18.4 KB to 498 B (38×), kubectl pods + describe 18.3 KB to 1.6 KB (12×), cargo test 17.6 KB to 517 B (35×), cargo tree 15.7 KB to 1.5 KB (10×), terraform plan 14.6 KB to 1.3 KB (11×), and git diff 12.2 KB to 490 B (25×)." width="100%">
</picture>

Originals stay recoverable and exit codes matched in every run. Local diagnosis replay dropped from `18,532 B` to `1,541 B` (`12.0×`, `0.060 s`), `justless test --affected` missed `0` failures across 13 mutants (panic and benign), `justless proxy --compact-live` cut oversized newest JSON, logs, tables and tracebacks by `79.8%` to `96.6%` with `0%` prompt-cache invalidation, `mask` retired `38,306 B → 19,952 B`, and cached Tree-sitter queries (`LazyLock`) run 40-file outline batches `>100×` faster (`159 ms` vs `>15 s`).

The three-turn repair task passed in all 24 API runs. Two controlled agent benchmarks on Sonnet 5.5 — 248 runs on small tasks and 96 on tasks built around large output — found no demonstrated difference in cost or success: the model kept its own tool output small, about 5.6 KB and 9 KB per run, so there was little to compact. A saving in long sessions with large output has not yet been shown by a controlled run. The code-question ratio grows with file size, and this repository's files are large. [Methods](docs/benchmarks.md)

### See it

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/query-dark.svg">
  <img src="assets/query-light.svg" alt="Where is would_route defined and what calls it? Without justless, the agent runs rg -n -w would_route src and reads src/agents.rs: 5,232 lines and 207,789 bytes in all. With justless, justless query would_route prints 15 lines (1,560 bytes): definition at src/agents.rs:4382-4405, grouped callers, deduplicated outgoing dependencies with (from :LINE), and related tests. 133× fewer bytes." width="100%">
</picture>

<sub>Where is <code>would_route</code> defined and what calls it? A search plus reading <code>src/agents.rs</code> is 5,232 lines (207,789 bytes); <code>justless query</code> answers in 15 lines (1,560 bytes): 133× against <code>cat</code>, and 71.3× median (up to 153.9×) over 13 unique functions against Claude Code's 2,000-line Read.</sub>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/search-dark.svg">
  <img src="assets/search-light.svg" alt="A search with lots of output. Without justless, rg -n &quot;fn &quot; src prints 4,661 lines (357,380 bytes). With justless run, the agent receives 93 lines (4,058 bytes): grouped by file with match counts, sample lines and archived line ranges. justless log run-O9hfiUbLOlPn --stream stdout --from 3324 --to 3326 then returns those lines verbatim. 88× fewer bytes." width="100%">
</picture>

<sub><code>rg -n "fn " src</code>: 4,661 lines (357,380 bytes) raw, 93 lines (4,058 bytes) grouped by file (88×). Each group names its lines in the archive, and <code>justless log</code> replays lines 3324–3326 byte for byte.</sub>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/outline-dark.svg">
  <img src="assets/outline-light.svg" alt="Reading a big file. Without justless, cat docs/reference.md prints all 1,142 lines (273,594 bytes). With justless, justless read docs/reference.md --outline returns 43 lines (1,598 bytes) using compact h1, h2, h3, table and code anchors. justless expand docs/reference.md '5ed9fdb08d39e4ae9bf0c355#35' then returns the Failures section, lines 781 to 784, byte for byte (794 bytes). The outline is 171× smaller than the file." width="100%">
</picture>

<sub><code>docs/reference.md</code> is 1,142 lines (273,594 bytes); its outline is 43 lines (1,598 bytes, 171×) with compact <code>h1</code>–<code>h3</code>, table and code anchors, and <code>justless expand</code> returns the 794-byte <code>Failures</code> section verbatim (114.4× combined).</sub>

### Watch it in your own sessions

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/statusline-dark.svg">
  <img src="assets/statusline-light.svg" alt="Claude Code's status line in a real session, with justless installed: justless, initially about 2.5 million tokens saved, net about 1.8 million tokens saved (72%) this session, 519 runs, 29 reads." width="100%">
</picture>

```sh
justless init --statusline   # running total and net % in Claude Code's status line
justless stats               # savings by day and command in this project
justless stats --all         # one total across every project on this machine
justless discover --plan     # see unrouted commands in your transcripts and how to cover them
```

The line above is from a real Claude Code session. "Net" subtracts everything the agent later pulled back from the archive. Token figures are estimates from bytes per token measured against Claude's tokenizer; the byte counts are exact.

## One tool instead of a six-tool stack

Context-saving tools each solve one slice of the problem. justless replaces the whole six-tool stack with one local Rust binary, and adds verified edits, budgeted directory skeletons, and cross-compaction handoffs:

| Capability | justless | RTK | graphify | Serena | Headroom | code-review-graph |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| Command hooks & structured compactors | ✅ | ✅ | — | — | — | — |
| Code graph + NL traversal + `explain` | ✅ | — | ✅ | LSP | — | ✅ |
| PR blast-radius review & affected tests | ✅ | — | — | — | — | PR review |
| Surgical outlines (files & dirs) & verified edits | ✅ | File reads | — | ✅ (LSP) | — | — |
| Live-zone cache-safe & history retirement | ✅ | Opt-in proxy | — | — | ✅ | — |
| Built-in secret redaction | ✅ | Paid edition | — | — | — | — |
| 100% local · zero LLM · zero network | ✅ 🔒 | 📡 Partly | 📡 Partly | ✅ | 📡 Partly | ✅ |

<sub>Checked against each project's public documentation on 2026-11-25; "—" means the project does not ship that feature. Each peer has its own strengths: **RTK** covers more shell commands (100+) and agents (18); **graphify** covers ~40 Tree-sitter languages plus PDFs, images, video and an interactive HTML graph viewer; **Serena** connects to live Language Servers for full compiler type-checking and cross-file LSP refactoring; **Headroom** focuses on API-level proxy compression and routing across providers; **code-review-graph** adds interactive visual PR impact graphs; and **Repomix** exports whole repositories into standalone XML/Markdown bundles. [Full comparison](docs/comparison.md)</sub>

## Everything it compacts and navigates

- ⚡ **Command compactors** — Structured, line-referenced reports for tests (`cargo test`/`nextest`, Jest/Vitest/Bun/Playwright/`node --test`, `pytest`/`unittest`, Go races/panics, RSpec, PHPUnit/ParaTest/Pest, `dotnet`, Maven, Gradle, Swift, CTest, `mix`, `deno`), **27+ linters & compilers** (rustc, Clippy, Ruff, mypy, Pyright, ESLint, Biome, Oxlint, `tsc`, ShellCheck, golangci-lint, RuboCop, PHPStan, clang-tidy, cppcheck, yamllint, markdownlint, SQLFluff, ktlint, stylelint, Deno, ansible-lint, actionlint, Credo, MSBuild, Maven, Gradle, gcc/clang/swiftc), Docker/Compose/Podman BuildKit, universal lossless ASCII/`psql`/Unicode/DuckDB/Markdown tables, dependency trees (`cargo tree`, `npm ls`, `pnpm`, `yarn`, `pipdeptree`, `go mod graph`, `mvn`, `gradle`), semantic diffs + **13 lockfiles** + generated/SVG folding, Terraform/OpenTofu/Pulumi plans, Kubernetes/Helm/Docker inventories & `kubectl describe`, `gh`/`glab` checks/runs/views/lists & security audits, lossless `git blame` + compact `git status`/`log`/`branch`/`reflog`, prefix/JSON `logview`, workspace-aware `stacktrace`, and bijective deep-schema `jsonview`.
- 🗺️ **Code graph, review & NL traversal** — **26 indexed code-graph languages** (plus Vue/Svelte/Astro and shebang scripts) refreshed incrementally on every call, weighted PageRank `map` with consolidated communities and cross-community bridges, architectural `map --explain SYMBOL`, natural-language cross-language `lookup --graph`, `justless review [--base REF]` blast-radius PR packs with test coverage-gap detection, `query`, `path`, `pack`, `context --run`, and polyglot `test --affected`.
- 🔬 **Surgical reads & verified edits** — **43 structured outline formats** (code + Markdown `h1`–`h6`/frontmatter/code fences/tables + 13 config/DevOps/IDL/markup formats), budgeted directory Tree-sitter code skeletons (`justless read DIR --outline`), `#A..#B` range and cross-file batch `expand`, session repeat-read delta dedup, and revision-verified parse-checked `edit`.
- 🧹 **Context hygiene & proxy** — `mask`/`recall` with early duplicate and superseded-read retirement plus secret-safe semantic cues, opt-in `justless proxy --compact-live` (live-zone prefix-cache-safe newest-result compaction with exact byte-for-byte recall), server-side clearing via `justless wrap claude`, and cross-compaction `resume` handoffs.
- 🔌 **Agent hooks & MCP** — First-class setup for **7 agents** (Claude Code, Codex, Cursor, Gemini CLI, Copilot CLI, OpenCode with native Read/Grep/Glob + retirement, Antigravity CLI with two-tier hooks and native read outlining), global hooks, monorepo and `cargo +toolchain` routing, and a slim **18-tool** read-only MCP server (`6.1 KB` total schema).
- 🧰 **Scripts, redaction & diagnostics** — `justless exec --intent` for bounded script execution over large data, built-in secret redaction across previews/logs/searches/MCP, `discover --plan`, `stats --all`, `(XX%)` `statusline`, `doctor`, and `learn`.

Details: [Command reference](docs/reference.md) · [Worked examples](docs/examples.md)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/demo-dark.svg">
  <img src="assets/demo-light.svg" alt="Animated terminal. The agent runs cargo test on a copy of fixtures/failing, and the hook routes it through justless run. The agent gets 9 lines instead of 380: the failing assertion with a pointer to stdout lines 365-368, the empty unit test binary folded, ending with [justless run-pHKV4nNjVk9q · 451 B of 17.6 KB shown · exit 101]. The agent then runs justless log run-pHKV4nNjVk9q --stream stdout --from 365 --to 368 and gets back the four exact lines of the assertion failure." width="100%">
</picture>

<sub>The same run step by step: the compact result names the archived lines, and <code>justless log</code> returns them byte for byte (<a href="assets/demo-dark.gif">animated GIF</a>).</sub>

### One failing test

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/before-after-dark.svg">
  <img src="assets/before-after-light.svg" alt="The same failing cargo test run twice. Without justless the agent receives 380 lines (18,038 bytes). With justless, routed by the hook, it receives 9 lines (517 bytes, 97% smaller): the failing test, its assertion, collapsed empty target, exit code 101 and run ID run-pHKV4nNjVk9q. justless log then replays the original assertion lines exactly." width="100%">
</picture>

<sub>The deliberately failing test in <code>fixtures/failing</code>: 380 lines (18,038 bytes) raw vs. 9 lines (517 bytes, 35×) with the empty unit binary folded. The agent types <code>cargo test</code> in both windows; on the right, the hook routes it through <code>justless run</code>. Long lines wrap for display.</sub>

The exit status is still 101, and `justless log RUN_ID --stream stdout --from 365 --to 368` returns the archived lines byte for byte. [Full walkthrough](docs/examples.md#diagnose-and-fix-a-failing-test)

### What it does not do

- **No changed commands.** Same command, directory and exit code. Pipes, redirections, interactive commands and output another program reads pass through untouched.
- **No network, no LLM, no telemetry.** Parsing is local and deterministic, and everything stays in `.justless/`.
- **No hidden failures.** Anything cut is marked with exact archive coordinates and one command away.

## Install

### 1. Run one line in your project folder

```sh
curl -fsSL https://raw.githubusercontent.com/rishadbaniya/justless/main/install.sh | sh -s -- claude
```

Swap `claude` for your agent. The script builds justless from source with Cargo and turns it on for this project. It needs [Rust](https://rustup.rs) 1.91 or newer and a C compiler, and the first build takes a few minutes.

| Your agent | Use | Then |
| --- | --- | --- |
| Claude Code | `claude` | Start a new session |
| Codex | `codex` | Run `/hooks` once and trust them |
| Cursor | `cursor` | Start a new session |
| Gemini CLI | `gemini` | Start a new session |
| Copilot CLI | `copilot` | Start a new session |
| OpenCode | `opencode` | Start a new session |
| Antigravity CLI | `agy` | Start a new session |
| Several at once | `claude codex` | As above, for each |
| Every agent on your PATH | nothing: end the line at `sh` | As above, for each |

### 2. Check it works

```sh
justless doctor              # checks the setup and prints a fix for anything missing
justless run -- git status   # ends with a [justless run-…] line when output is cut
justless stats               # what it saved so far
justless init --statusline   # Claude Code: a running total and net % in the status line
```

### 3. Optional

| To | Run |
| --- | --- |
| Turn it on for every project at once (Claude Code, Codex and Antigravity CLI) | `justless init --global` ([details](docs/reference.md#global-hooks)) |
| Turn it on for one more project | `justless init --hooks --agent claude` in that folder |
| Use it from an editor without hooks, such as VS Code | `justless mcp --install vscode` |
| Run a blast-radius review pack on the current branch | `justless review` |
| Compact newest oversized tool results without breaking prompt cache | `justless proxy --compact-live` ([details](docs/reference.md#request-boundary-context-management)) |
| Pause every hook without uninstalling | Start the agent with `JUSTLESS_DISABLE=1` set |
| Update | See [install options](docs/reference.md#install-and-configure-agents) |
| Remove it from a project | `justless init --remove` |

## How it works

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/how-it-works-dark.svg">
  <img src="assets/how-it-works-light.svg" alt="How Justless works: Claude Code, Codex, Cursor, Gemini CLI, OpenCode, Copilot CLI, and Antigravity connect via hooks, MCP, or CLI to the local offline justless binary, which compacts commands (tests, lint, BuildKit, diffs, logs, tables, JSON), code (26 graph langs, 43 outline formats, map --explain, lookup --graph), and history (duplicates, semantic cues, compaction). Full output is archived locally in .justless/ and replayable byte-for-byte on demand via log, expand, and recall." width="100%">
</picture>

Hooks route commands through `justless run`, a local index answers code and PR review questions, older or superseded tool results retire to an ID, and `log`, `expand` and `recall` return the original bytes whenever a summary is not enough.

[Command reference](docs/reference.md) · [Worked examples](docs/examples.md) · [Benchmarks](docs/benchmarks.md) · [How it compares](docs/comparison.md) · [FAQ](docs/faq.md)

## So how does the author make money from this?

I don't. justless is for people who want to spend less on tokens, not a funnel into spending more somewhere else. There's no paid edition, no cloud version, no account, no telemetry and no "Pro" features held back: everything on this page is in the one free binary, under the [Apache-2.0 license](LICENSE), and it never phones home. If it saves you money, a ⭐ helps the next person find it.

## Contributing

Build, test and commit conventions are in [CONTRIBUTING.md](CONTRIBUTING.md), maintainer notes in [AGENTS.md](AGENTS.md), and changes in the [changelog](CHANGELOG.md).

## License

[Apache-2.0](LICENSE)
