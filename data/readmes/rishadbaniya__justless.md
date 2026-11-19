<p align="center">
  <img src="assets/logo.png" alt="Justless logo" width="140">
</p>

<h1 align="center">justless</h1>

<p align="center">
  <strong>Up to 148× less for your coding agent to read.</strong><br>
  One local tool instead of RTK + graphify + context pruning. Compact by default, exact on demand.
</p>

<p align="center">
  <a href="#install">Install</a> · <a href="docs/reference.md">Reference</a> · <a href="docs/examples.md">Examples</a> · <a href="docs/benchmarks.md">Benchmarks</a> · <a href="CHANGELOG.md">Changelog</a>
</p>

<p align="center">
  <strong>148×</strong> smaller answer to a code question · <strong>85×</strong> smaller reads of old revisions · <strong>28×</strong> smaller <code>find .</code> · <strong>10×</strong> less command output · <strong>8×</strong> fewer input tokens on a repair task · <strong>0</strong> network calls
</p>

**justless** sits between your coding agent and its tools. It turns command output into compact reports, answers code questions from a local **code graph** so the agent stops reading whole files, and keeps every byte it cuts one command away.

> **🔒 100% local. Zero network calls.** No telemetry, no cloud, no LLM, no account: your code and command output never leave your machine. The one opt-in exception, `justless wrap claude`, only relays Claude Code's own API requests.

## How much it saves

| What your agent does | Without justless | With justless | Cut |
| --- | ---: | ---: | ---: |
| A file at an old revision, `git show HEAD:CHANGELOG.md` | 29.2 KB | 345 B | **85×** |
| "Where is `X` and what calls it?": search and read the file, or `justless query X` (14 functions) | 1.14 MB | 19 KB | **57×** median, up to 148× |
| `find .` | 267 KB | 9.4 KB | **28×** |
| `cargo test` with one failing test ([`fixtures/failing`](fixtures/failing)) | 18,038 B | 700 B | **26×** |
| `cargo clippy -- -W clippy::pedantic` on this repository, 142 warnings | 79,563 B | 3,916 B | **20×** |
| `git diff` against older revisions | 274 KB | 13.5 KB | **20×** |
| 77 real commands across four Rust and Python repositories | 1,171 KB | 115 KB | **10×** |
| One function from a 21 KB source file: read the file, or its outline and then that function (`expand`) | 21 KB | 2.1 KB + 60 B | **10×** |
| Claude Code `Read` calls of more than 150 lines (167 windows) | 2.80 MB | 305 KB | **9×** |
| A three-turn repair task, input tokens as the API counted them, on Claude Haiku, Sonnet, Opus 5.5 and Fable 5.2 | 22.4–22.8k | ~2.85k | **8×** |

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/savings-dark.svg">
  <img src="assets/savings-light.svg" alt="Bar chart of the bytes an agent received from 77 real commands: 1,171 KB raw versus 115 KB with justless, 90% smaller. git diff against older revisions 274.3 KB to 13.5 KB, find . 267.4 KB to 9.4 KB, grep -rn 200.1 KB to 16.4 KB, git log 143.1 KB to 24.9 KB." width="100%">
</picture>

Originals stay recoverable and exit codes matched in every run. The repair task passed in all 24 runs. On small tasks that read little output (about 5.6 KB per run), a 248-run benchmark found no difference in cost or success: justless pays off on large output and long sessions, which is what it compacts. The code-question ratio grows with file size, and this repository's files are large. [Methods](docs/benchmarks.md)

### See it

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/query-dark.svg">
  <img src="assets/query-light.svg" alt="Where is would_route defined and what calls it? Without justless, the agent runs rg -n -w would_route src, which prints 4 matching lines, then reads the defining file src/agents.rs: 2,498 lines and 102,590 bytes in all, with the 15-line definition at lines 2110 to 2124. With justless, justless query would_route prints 8 lines (665 bytes): the definition at src/agents.rs:2110-2124, its two callers in src/discover.rs at lines 275 and 292, the functions and types it uses, and a note that no related tests were found." width="100%">
</picture>

<sub>Where is <code>would_route</code> defined and what calls it? A search plus the file that defines it is 102,590 bytes; <code>justless query</code> answers in 665: 154× against <code>cat</code>, 148× against Claude Code's Read, which stops at 2,000 lines, and 57× median over 14 functions.</sub>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/search-dark.svg">
  <img src="assets/search-light.svg" alt="A search with lots of output. Without justless, rg -n &quot;fn &quot; src prints 2,512 lines (185,877 bytes), one per match. With justless run, the agent receives 64 lines (2,837 bytes): the match count, 15 files ordered by match count, each with two sample lines and the range of its lines in the archived output, one line summarizing the other 64 files, and a footer with the run ID; the picture leaves out 48 of those lines. justless log then returns lines 245 to 247 of the original output exactly, including a match the report did not show." width="100%">
</picture>

<sub><code>rg -n "fn " src</code>: 185,877 bytes raw, 2,837 grouped by file (66×). Each group names its lines in the archive, and <code>justless log</code> replays them byte for byte.</sub>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/outline-dark.svg">
  <img src="assets/outline-light.svg" alt="Reading a big file. Without justless, cat docs/reference.md prints all 1,099 lines (228,160 bytes). With justless, justless read docs/reference.md --outline returns 36 lines (2,367 bytes): one row per heading with its line range, 34 headings on this first page, and a command for the next page; the picture leaves out 18 of those rows. justless expand then returns the Failures section, lines 738 to 741, exactly as in the file (794 bytes)." width="100%">
</picture>

<sub><code>docs/reference.md</code> is 228,160 bytes; its outline is 2,367 (96×), and <code>justless expand</code> returns one 794-byte section exactly as written.</sub>

### Watch it in your own sessions

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/statusline-dark.svg">
  <img src="assets/statusline-light.svg" alt="Claude Code's status line in a real session with justless: justless · initially ≈2.5M tokens saved · net ≈1.8M tokens saved this session · 519 runs · 29 reads." width="100%">
</picture>

```sh
justless init --statusline   # running total in Claude Code's status line
justless stats               # savings by day and command in this project
justless stats --all         # one total across every project on this machine
```

The line above is from a real Claude Code session. "Net" subtracts everything the agent later pulled back from the archive. Token figures are estimates from bytes per token measured against Claude's tokenizer; the byte counts are exact.

## One tool instead of three

Token-saving tools each take one slice of the context window. RTK compresses command output, graphify answers code questions from a graph, and context pruning clears old tool results. justless does all three in one local binary, and adds file reads, edits and test selection:

| | justless | RTK | graphify |
| --- | :---: | :---: | :---: |
| Compresses command output through agent hooks | ✅ | ✅ | — |
| Code graph: symbols, calls, imports, `query` and `path` | ✅ | — | ✅ |
| Outlines big files and returns one symbol's exact bytes | ✅ | — | — |
| Exact recall of anything it cut | ✅ | ✅ | — |
| Retires old tool results from the context | ✅ | — | — |
| Runs only the tests a change reaches | ✅ | — | — |
| Edits that check the file has not changed | ✅ | — | — |
| Secret redaction | ✅ | Paid edition | — |
| Token estimates calibrated to Claude's tokenizer, built in, nothing sent | ✅ | Bytes ÷ 4 | — |
| No network calls | ✅ 🔒 your code stays yours | 📡 Partly | 📡 Partly |

<sub>RTK and graphify columns from each project's README on 2026-11-19; "—" means the README does not mention it. "Partly": RTK pipelines and its proxy can send content to models, and graphify's pass over docs and media can call a model backend. RTK supports more commands (100+) and agents (18); graphify more languages (about 40) and also reads docs, PDFs and images. [Full comparison](docs/comparison.md)</sub>

## How it cuts tokens

| | What it does |
| --- | --- |
| ⚡ **Compact output** | Test failures, lint findings, searches, diffs, listings and JSON become grouped reports. Anything else gets a 4 KB head, tail and error-line preview. |
| 🎯 **Exact recall** | Every byte is archived with a SHA-256 digest. `justless log RUN --from A --to B` replays the exact lines. |
| 🔬 **Surgical reads** | Outlines in 26 languages. `expand` returns one symbol's exact bytes, and `edit` writes it back only if the file has not changed. |
| 🗺️ **Code graph** | Symbols, calls, imports, HTTP routes and SQL tables. `query`, `path`, `pack`, `lookup` and `affected` answer in one call. |
| 🧪 **Affected tests** | `justless test --affected` runs only the tests a change reaches, and the full suite when it can't be sure. |
| 🔁 **Changed since last read** | Re-reading code with `context` or `pack` shows only what changed since the agent last saw it. |
| 🔐 **Secret redaction** | Keys, tokens and private keys are masked everywhere the agent sees output. |
| 🧹 **Context hygiene** | Run IDs survive compaction, and opt-in `justless wrap claude` clears old tool results server-side. |
| 🧰 **Scripts and lessons** | `exec` runs a script over big data; `learn` turns mistakes agents repeat into project rules. |

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/demo-dark.svg">
  <img src="assets/demo-light.svg" alt="Animated terminal. The agent runs cargo test on a crate with a failing test, and the hook routes it through justless run. The agent gets 9 lines instead of 380: the failing assertion with a pointer to stdout lines 365-368, ending with [justless run-5JrBaF3zTLSD · 634 B of 17.6 KB shown · exit 101]. One long line is wrapped for display. The agent then runs justless log run-5JrBaF3zTLSD --stream stdout --from 365 --to 368 and gets back the four exact lines of the assertion failure." width="100%">
</picture>

<sub>The same run step by step: the compact result names the archived lines, and <code>justless log</code> returns them byte for byte. One long line is wrapped for display.</sub>

### One failing test

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/before-after-dark.svg">
  <img src="assets/before-after-light.svg" alt="The same failing cargo test shown side by side. Without justless the agent receives 380 lines (18,038 bytes), 351 of them trace lines the test prints. With justless, which the hook routes the command through, it receives 9 lines (700 bytes): the failing test with its assertion and location, exit code 101 and a run ID. justless log then replays the original assertion lines exactly." width="100%">
</picture>

<sub>The deliberately failing test in <code>fixtures/failing</code>. The agent types <code>cargo test</code> in both windows; on the right, the hook routes it through <code>justless run</code>. Long lines are wrapped for display.</sub>

The exit status is still 101, and `justless log RUN_ID --stream stdout --from 365 --to 368` returns the archived lines byte for byte. [Full walkthrough](docs/examples.md#diagnose-and-fix-a-failing-test)

### What it does not do

- **No changed commands.** Same command, directory and exit code. Pipes, redirections, interactive commands and output another program reads pass through untouched.
- **No network, no LLM, no telemetry.** Parsing is local and deterministic, and everything stays in `.justless/`.
- **No hidden failures.** Anything cut is marked and one command away.

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
justless run -- git status   # ends with a [justless run-…] line
justless stats               # what it saved so far
justless init --statusline   # Claude Code: a running total in the status line
```

### 3. Optional

| To | Run |
| --- | --- |
| Turn it on for every project at once (Claude Code and Codex) | `justless init --global` ([details](docs/reference.md#global-hooks)) |
| Turn it on for one more project | `justless init --hooks --agent claude` in that folder |
| Use it from an editor without hooks, such as VS Code | `justless mcp --install vscode` |
| Pause every hook without uninstalling | Start the agent with `JUSTLESS_DISABLE=1` set |
| Update | See [install options](docs/reference.md#install-and-configure-agents) |
| Remove it from a project | `justless init --remove` |

## How it works

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/how-it-works-dark.svg">
  <img src="assets/how-it-works-light.svg" alt="Your agent reaches Justless through hooks, MCP or the CLI. Justless turns commands, code lookups and old tool results into compact answers for the context window, archives the full output in .justless, and returns exact bytes on demand with log, expand and recall." width="100%">
</picture>

Hooks route commands through `justless run`, a local index answers code questions, older tool results retire to an ID, and `log`, `expand` and `recall` return the original bytes whenever a summary is not enough.

[Command reference](docs/reference.md) · [Worked examples](docs/examples.md) · [Benchmarks](docs/benchmarks.md) · [How it compares](docs/comparison.md) · [FAQ](docs/faq.md)

## So how does the author make money from this?

I don't. justless is for people who want to spend less on tokens, not a funnel into spending more somewhere else. There's no paid edition, no cloud version, no account, no telemetry and no "Pro" features held back: everything on this page is in the one free binary, under the [Apache-2.0 license](LICENSE), and it never phones home. If it saves you money, a ⭐ helps the next person find it.

## Contributing

Build, test and commit conventions are in [CONTRIBUTING.md](CONTRIBUTING.md), maintainer notes in [AGENTS.md](AGENTS.md), and changes in the [changelog](CHANGELOG.md).

## License

[Apache-2.0](LICENSE)
