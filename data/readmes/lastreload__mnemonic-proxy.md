<p align="center">
  <img src="https://raw.githubusercontent.com/lastreload/mnemonic-proxy/main/docs/assets/logo.png" alt="Mnemonic Proxy logo" width="120">
</p>

<h1 align="center">Mnemonic Proxy</h1>

<p align="center"><em>Like Johnny, your agent carries more than its head can hold — and keeps working for hours.</em></p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
  <img alt="Python ≥ 3.10" src="https://img.shields.io/badge/python-%E2%89%A53.10-blue.svg">
  <a href="https://lastreload.github.io/mnemonic-proxy/"><img alt="Project page" src="https://img.shields.io/badge/page-lastreload.github.io-ff2bd6.svg"></a>
</p>

**Keep a coding agent's history without keeping it all in the model's context.** Mnemonic Proxy sits between
an agent and an OpenAI-compatible backend: the agent sends its history as usual; the proxy manages what the model reads.

- **Archive verbatim.** Older tool outputs leave the prompt, not the archive: their original text stays available through recall.
- **Recall on demand.** A tool-calling model can search and retrieve archived text through `recall`. Exact storage does not
  guarantee that the model finds the right evidence or answers correctly.
- **Resume without a full re-read.** Save and restore engine state on supported backends; other backends use
  masking and recall without saved state.

**Try it in one minute — no model or GPU needed** (Python ≥ 3.10, [uv](https://docs.astral.sh/uv/)):

<!-- readme-test: ci -->
```sh
uvx mnemonic-proxy demo
```

No `uv` yet? `pip install uv` (or `curl -LsSf https://astral.sh/uv/install.sh | sh`), or skip `uv` entirely and
use the three `pip` lines of [T0](#t0--see-it-work-1-minute-no-model).

Expected result: **`PASS`**.

The demo uses the real proxy with a **scripted fake model** to check archive, masking and byte-for-byte recall.
It does not test a real model's tool use or saved engine state. [Without uv / demo details](#t0--see-it-work-1-minute-no-model)
· [Connect your agent and engine](#install).

**Measured, not guaranteed** — single runs on our hardware; setup and limitations at each link:

| Experiment | Result |
|---|---|
| [Long coding session, one 12 GB GPU](#one-session-measured) | 3 h 15 min; 448K tokens of history, at most 105K in the prompt. Archived history is not all in context. |
| [AgentLongBench subset, clarified questions](#benchmark-agentlongbench-with-a-32k-window) | 86/100 right with the proxy at 32K, vs 47 with an LLM summary and 69 with full history in a larger window; a repeat run gave 85 / 57 / 75. |
| [Saved engine state](#saved-state-measured) | A 110K-token conversation resumed in 1.4 s instead of ≈50 s; requires a backend with save/restore support. |

[What we have not proven](#what-we-have-not-proven) · [Project page](https://lastreload.github.io/mnemonic-proxy/)

OpenAI Chat Completions, Anthropic Messages and OpenAI Responses; Python ≥ 3.10, standard library only.
Developed and benchmarked primarily with [Strata](https://github.com/Niko1221/Strata), by Niko1221 and contributors.
This independently maintained project also supports llama-server, ds4-server, Ollama, LM Studio and other
OpenAI-compatible backends; capabilities and test coverage vary ([Engines](#engines)).

<details>
<summary>Johnny's payload</summary>

<p align="center">
  <img src="https://raw.githubusercontent.com/lastreload/mnemonic-proxy/main/docs/assets/hero.jpg" alt="Mnemonic Proxy" width="100%">
</p>

</details>

## Install

The first time: install, watch it work with no model, check your engine, start. No configuration file is needed
to begin — these four lines are the whole first run.

<!-- readme-test: ci -->
```sh
python3 -m venv mnemonic-venv && . mnemonic-venv/bin/activate
pip install mnemonic-proxy
mnemonic-proxy demo      # 1 minute, no model: archive, masking, recall -> PASS
mnemonic-proxy check --upstream http://127.0.0.1:8095 --port 8096 --data ./data
mnemonic-proxy --upstream http://127.0.0.1:8095 --port 8096 --data ./data
```

`check` ends with one of three outcomes: **`READY` (exit 0)**, **`READY with warnings` (exit 2)** — it works, but
something optional is off (typically saved state) — or **`NOT READY` (exit 1)**, and then it says, line by line,
what to change; `--live` adds a real generation, a tool call and a save/restore. `--upstream` is the engine's
address. Then point the agent at the proxy (port 8096) instead of the engine. The engine window must be at least
16K tokens, 32K or more recommended ([Requirements](#requirements)). Step by step with a small model on CPU:
[Quick start](#quick-start).

**No engine running yet?** The package ships the fake engine the test suite uses, so `check` and the proxy can be
tried with nothing installed but this package:

<!-- readme-test: ci -->
```sh
python3 -m ctxproxy.fake_engine --flavor llama --n-ctx 32768 --port 8095 &
mnemonic-proxy check --upstream http://127.0.0.1:8095 --port 8096 --data ./data
```

**A configuration file, when you want one** (saved state, or an engine that needs explicit thresholds). It is a
separate, explicit step — the proxy runs on its defaults without it:

<!-- readme-test: ci -->
```sh
mnemonic-proxy init-config --engine strata        # or llama-server, ds4, openai-32k
mnemonic-proxy check --upstream http://127.0.0.1:8095 --port 8096 --data ./data --config config.json
```

`init-config` writes a **minimal** `config.json` (0.3.24): only what the proxy cannot work out by itself, so the
[automatic configuration](#automatic-configuration) keeps deciding the rest. For Strata, llama-server and
ds4-server that is *nothing at all* (`{}`) — the window comes from the engine, and the saved-state options, the
exact token count and the window-sized budgets are chosen from the engine and the machine. The exceptions are the
only two things nobody can discover: `--slot-dir DIR` (the engine's own `--slot-save-path`, for saved state) and,
for a plain OpenAI-compatible engine that reports no context, `window`.

<!-- readme-test: illustrative -->
```sh
mnemonic-proxy init-config --engine strata --slot-dir /path/to/sessions   # {"slot_dir": "/path/to/sessions"}
mnemonic-proxy init-config --engine strata --full                         # every field, documented
mnemonic-proxy init-config --engine strata --launcher                     # + the one-click starter, below
```

`--full` writes the complete documented example from the copy inside the package (no network, no clone) — every
field explicit, which is also what *switches the automatic configuration off*, so use it as a reference and delete
the lines you do not mean to pin. `init-config` prints which file it used and never overwrites a file you have
already edited (`--force` does). It never writes `"auto_config"`: it is already the default, and writing it would
remove a protection — on a data folder that already holds conversations the automatic choices are only *applied*
when `auto_config` is explicit, so that an upgrade cannot change how a running setup behaves. The complete
examples are browsable at [`examples/`](https://github.com/lastreload/mnemonic-proxy/tree/main/examples); `check`
prints the full `raw.githubusercontent.com` URL of the one for *your* version whenever it suggests one. Fields:
[Configuration](#configuration).

**One click** (`--launcher`, 0.3.24; asked for by the first Windows user). Writes `start-mnemonic-proxy.bat` on
Windows and `start-mnemonic-proxy.sh` elsewhere, next to the config and with the values you passed baked in:

<!-- readme-test: ci -->
```sh
mnemonic-proxy init-config --engine strata --launcher --dir ./one-click \
  --upstream http://127.0.0.1:8095 --port 8096 --data ./data
```

It starts **only the proxy** — your engine's own command line stays yours — and in this order: it refuses to go on
if the engine does not answer, runs `check` once (a port already taken is reported there, with the fix), then runs
the proxy. Every value is a variable at the top of the file (`UPSTREAM`, `PORT`, `DATA`, `CONFIG`, `VENV`, and a
commented-out `TOKENIZER` unless `--tokenizer` was given), so it can be edited or overridden from the environment;
on Windows it ends with `pause`, so a console opened by a double-click does not vanish with the error in it. For
llama-server *and* its engine in one file, see
[`examples\start-windows.bat`](https://github.com/lastreload/mnemonic-proxy/blob/main/examples/start-windows.bat)
([Platforms](#platforms)).


### Strata in two commands

Strata already running? Then there is nothing to prepare: no folder to create, no extra engine flag, no
configuration file.

<!-- readme-test: ci -->
```sh
pip install mnemonic-proxy
mnemonic-proxy --upstream http://127.0.0.1:8095 --port 8096 --data ./data
```

The proxy creates `./data` itself and reads the window from Strata's `/v1/status`. Point your agent at
`http://127.0.0.1:8096/v1` instead of 8095 and turn off its own auto-compaction (table below). Everything but
one feature is already working: masking, the verbatim archive, `recall`, segments with handoff notes, 📌/🗑 and
tools on demand. Run `mnemonic-proxy check --upstream http://127.0.0.1:8095 --data ./data` first if you want the
setup verified line by line; the startup log says in one line what is on and what is off.

**Saved state (optional, and only later).** Saved state buys back one thing: the *fast resume* of a long
session (1.4 s instead of ≈50 s on a 110K-token conversation, [measured](#saved-state-measured)). It needs
Strata ≥ 0.1.40 restarted with one extra flag — this exact line, added to the Strata start command you already
use:

<!-- readme-test: real-engine -->
```sh
strata --slot-save-path /path/to/sessions        # plus your usual Strata options
```

and the same folder named in the proxy's config (the proxy creates it if it does not exist, so there is no
`mkdir` step) — one command writes exactly that file and nothing else:

<!-- readme-test: ci -->
```sh
mnemonic-proxy init-config --engine strata --slot-dir /path/to/sessions --dir ./saved-state
```

<!-- readme-test: illustrative; config: partial -->
```json
{
  "slot_dir": "/path/to/sessions"
}
```

Then start the proxy with `--config config.json`. `slot_save`, `mask_anchor` and `autosave` are **not** written:
the proxy switches them on by itself once `slot_dir` is there and the engine, the RAM and the disk allow it, and
it says so in one line at startup and in `check` ([Automatic configuration](#automatic-configuration)); writing
them by hand only matters to force them, or to keep them off. `check` reports `saved state: supported by the
engine, configured in the proxy`, and `check --live` verifies that `slot_dir` really is Strata's
`--slot-save-path` (same folder, same host) by saving and restoring a real state file. Nothing else changes.

**Your engine.** Start it as below. The `config` column is what `init-config` writes for that engine: minimal by
default, the complete example with `--full`.
[`examples/`](https://github.com/lastreload/mnemonic-proxy/tree/main/examples) holds the complete ones. `slot_dir`
and the engine's `--slot-save-path` are only for saved state: skip both to run in base mode, add them later (the
shortest Strata path is [above](#strata-in-two-commands)).

| engine | engine command (minimum) | config | saved state |
|---|---|---|---|
| Strata, any version | Strata's own start | none; base mode on an engine that *could* save state: `--engine official-strata` | no (base mode) |
| Strata ≥ 0.1.40, with saved state | Strata's own start, plus `--slot-save-path DIR` | `--engine strata --slot-dir DIR` (one field; `--full` = `config.example.json`) | yes |
| llama-server | `llama-server -m model.gguf -c 32768 --parallel 1 --jinja --port 8095` (add `--slot-save-path ./slots` for saved state) | `--engine llama-server --slot-dir ./slots` (`--full` = `config.llama-server.json`) | yes with `--slot-save-path` |
| llama-server, router mode (several models) | `llama-server --models-preset preset.ini --models-max 1 --port 8095`; preset: `[*]` with `slot-save-path` and `parallel = 1`, a `ctx-size` (`c`) ≥ 16384 per model | `--engine llama-server-router --slot-dir ./slots` + `preset.router.example.ini` | yes, per model |
| ds4-server | `ds4-server -m MODEL.gguf --ctx 65536 --kv-disk-dir ./kv --port 8110` | none (`--full` = `config.ds4.json`) | kept by ds4 itself |
| Ollama, LM Studio | engine context set to 32768 (see below); `--tokenizer` recommended | none: the window is read from the engine | no (base mode) |
| any OpenAI-compatible (vLLM, online APIs) | — | `--engine openai-32k` at 32K (just `{"window": 32768}`); at 131072 none is needed | no (base mode) |

The proxy reads the window from Strata, llama-server (`n_ctx`, per model in router mode), ds4-server (`--ctx`),
Ollama and LM Studio (the context of the loaded model, 0.3.8), and scales its thresholds to it, unless `window` is
written in the config. From any other engine it cannot: write the engine's real context in `window`, and since
0.3.24 the thresholds scale from it exactly as they would from an engine-reported one (so
`{"window": 32768}` is a complete 32K configuration — `config.openai-32k.json` spells the same numbers out).
Details per engine: [Engines](#engines).

**Ollama and LM Studio** (tested on Linux, small model, details in [Tested combinations](#tested-combinations)). Both
serve an OpenAI-compatible API (Ollama `http://127.0.0.1:11434/v1`, LM Studio `http://127.0.0.1:1234/v1`;
`--upstream` is the same address without `/v1`) and the proxy runs in base mode: masking, archive, `recall`, segment
switches, tool calls, streaming, `/v1/messages` and `/v1/responses` worked, no saved state. What to know:
- **Give the engine a context of 32768 (at least 16384).** With their defaults on our machine (Ollama 4096 on CPU;
  LM Studio 8192) both answer HTTP 200 to longer prompts after dropping part of them, without telling the client:
  Ollama drops the oldest messages, LM Studio keeps the beginning and the end and drops the middle.
  Ollama: `OLLAMA_CONTEXT_LENGTH=32768 ollama serve`; `ollama ps` shows the context in use (column `CONTEXT`).
  LM Studio: `lms load <model> --context-length 32768`, then `lms server start`; `lms ps` shows it.
- **The proxy reads that context** (0.3.8): Ollama `GET /api/ps` (`context_length` of the loaded model: the context
  it runs with, not the training context of `POST /api/show`), LM Studio `GET /api/v0/models`
  (`loaded_context_length`). Ollama is recognised only when `GET /api/version` **and** a coherent `/api/ps` models
  array both answer (0.3.24): a gateway such as llama-swap that exposes the version but not `/api/ps` runs as a
  generic engine, and its `/v1/models` catalog is reported as model availability with the loaded state and the
  window unverified. It reads it again before every request (one cheap GET; a model that is not loaded is
  loaded first with a 1-token request), so the window follows the engine and a prompt never goes over it. Below
  16384 the proxy refuses to start; a `window` in the config bigger than the engine context also refuses the start
  and fails `check`, with the command that fixes it. You can leave `window` out of the config.
- **`--tokenizer` is still recommended** (the model's `tokenizer.json`, `pip install 'mnemonic-proxy[exact]'`).
  Without it the proxy estimates chars/3.5, which was up to ~10% low on code with many digits; on generic engines
  the estimate now gets a 15% margin by default (`window_estimate_slack` 0.15) and `check` warns. With 0.3.7 the
  notes request at a segment switch was estimated at 31.3K tokens but was 33.4K real tokens and both engines cut it;
  with 0.3.8 and no tokenizer it was 27.7K real tokens on Ollama and nothing was cut (numbers in Tested
  combinations).
- **A cut prompt is reported**: when the engine says (`usage.prompt_tokens`) it read less than 0.8× what the proxy
  counted, the journal gets `engine_truncated` and the log one warning per conversation; `check --live` sends a
  prompt of 0.9× the window and fails with "engine context smaller than window" if it does not come back whole.
- Ollama ignores an integrated GPU by default and runs on the CPU (much slower); `OLLAMA_IGPU_ENABLE=1` makes it use
  it. With it, Ollama chose a default context of 262144 from the shared memory: set `OLLAMA_CONTEXT_LENGTH` anyway.

**Your agent.** Turn off the agent's own auto-compaction, otherwise two context managers fight over the same history:

| agent | point it at | turn off | setup |
|---|---|---|---|
| pi, omp | `http://127.0.0.1:8096/v1` (`openai-completions`) | `"compaction": {"enabled": false}` | [T1 step 6](#t1--a-real-model-on-cpu), [omp](#pi-hermes-continue--chat-completions) |
| opencode | `http://127.0.0.1:8096/v1` (`openai-compatible` provider) | `"compaction": {"auto": false}` | [opencode](#opencode-chat-completions) |
| Hermes Agent | `http://127.0.0.1:8096/v1` (custom provider) | `compression.enabled: false` | [Hermes setup and test notes](docs/hermes-agent.md) |
| Continue, other Chat Completions clients | `http://127.0.0.1:8096/v1` | the client's own context compaction | [Chat Completions](#pi-hermes-continue--chat-completions) |
| Claude Code | `ANTHROPIC_BASE_URL=http://127.0.0.1:8096` (no `/v1`) | `DISABLE_AUTO_COMPACT=1` | [Claude Code](#claude-code-anthropic-messages) |
| Codex | `base_url = "http://127.0.0.1:8096/v1"`, `wire_api = "responses"` | no switch: `model_auto_compact_token_limit = 100000000` | [Codex](#codex-openai-responses) |
| any MCP client (Claude Code, Codex, Hermes) | `mnemonic-mcp --db ./data/archive.sqlite` (read-only search of the archive) | — | [MCP](#mcp-recall-server-claude-code-codex-hermes) |

**Your OS.**
- **Linux**: the reference; the commands on this page, and all the measured sessions.
- **Windows, native**: PowerShell commands and a one-click `examples\start-windows.bat` in [Platforms](#platforms)
  (tested on the CI runner, not yet on a desktop). **WSL 2**: the Linux commands, with engine, proxy and `slots` all
  inside WSL.
- **macOS**: not tested yet; follow the Linux commands (llama.cpp from Homebrew or built with Metal), see
  [Platforms](#platforms).
- **Android (Termux)**: `pkg install python git`, then `pip install git+https://github.com/lastreload/mnemonic-proxy`;
  tested in Waydroid (Android 13, x86_64) in front of an online API, not yet on an ARM phone, see
  [Platforms](#platforms).

## How it works

Archived content stays verbatim; the model writes handoff notes at segment switches. No vector database is required.

1. **Hide — mask, don't summarize.** Old tool outputs and reasoning leave the prompt in stable blocks and become
   one-line receipts with an id. The prefix stays byte-identical between blocks, so the engine's KV cache keeps
   working. A receipt says what the call did and how it ended, how big the output was (lines and bytes), the exit
   code when there is one, the error type and the **first** error line — everything read off the archived bytes, no
   model involved, so the same output always produces the same receipt:
   `⟪ctx-archive id=t1a2b… · output of bash "pytest -q" · this agent · hidden to save space (3120 tokens)⟫ Receipt: test: exit code 1, 412 lines/38.2 KB, passed 86, failed 1 (tests/test_a.py::test_adds). Error type: AssertionError. First error line: «E AssertionError: assert 3 == 4». Exact text: recall id=t1a2b…`
2. **Recall — structured, exact.** A `recall` tool searches the verbatim archive: first write of a file, its full
   edit timeline, command → output, the reasoning behind an edit — every hit tagged with message number and segment.
   The proxy runs these calls itself; the client never sees them, even when streaming.
3. **Segment — handoff notes.** When even the masked window fills up, the model writes its own notes, the segment is
   sealed and a fresh one starts. Pinned lines (`!!` or `📌`) survive every switch; lines starting with `🗑` (or `~`)
   mark a message as disposable once answered.
   *A copy is labelled a copy.* Several of these blocks — handoff notes, the verbatim first request, the 📌 block,
   an automatic-recall insertion — are themselves `role:"user"` messages, so a client's own control frame carried
   inside them would read as a fresh delivery. Clients mark out-of-band messages with frames the model is told to
   trust (Hermes: `[OUT-OF-BAND USER MESSAGE … delivered once at this position] … [/OUT-OF-BAND USER MESSAGE]`);
   in every copy the proxy writes, such a frame is relabelled `[quoted OUT-OF-BAND USER MESSAGE …]` — same words,
   whole text, visibly a quotation. The message the client actually delivered stays byte for byte as it was, in its
   own place (issue #61).
4. **Save — engine state on disk.** On engines that support it (llama-server, Strata with session files) the KV
   state is saved to disk: resuming after a pause, a restart or another client takes 1–3 s instead of a full
   re-read.
5. **Archive — deduplicated cold storage.** Old state files are rebuilt bit-for-bit from content-addressed zstd
   blocks: −36% disk on our sessions, sha256-verified before every restore.
6. **Lean — tools on demand.** Agents ship tens of thousands of tokens of tool definitions. The proxy keeps the core
   ones and loads the rest by name: 25.6K → 6.2K tokens on every request.

> "In the courier business you don't read the payload. You carry it, and you give it back exactly as it was." — the
> design rule. Hidden content is never paraphrased; it is either in the prompt or retrievable verbatim.

## Requirements

- **Engine window: at least 16K tokens (16384), 32K or more (32768) recommended.** Below 16K the proxy refuses to
  start, and `mnemonic-proxy check` reports NOT READY, with the command to restart the engine (`llama-server -c
  32768`, `ds4-server --ctx 32768`). Why: at 32K the recall trap of the ds4 runs (an error line removed from the
  prompt, asked for later) was answered right with both ds4 builds; at 8K it passed **once**, after the 0.3.0 recall
  fix, and failed before it. Small windows stay excluded until they are proven on more runs. Reports (Italian):
  [DS4-QWEN-COMPARE-RESULT.md](https://github.com/lastreload/mnemonic-proxy/blob/main/docs/dev-notes/DS4-QWEN-COMPARE-RESULT.md),
  [RECALL-8K-030-RESULT.md](https://github.com/lastreload/mnemonic-proxy/blob/main/docs/dev-notes/RECALL-8K-030-RESULT.md).
- Python ≥ 3.10 (`kv_archive`: ≥ 3.14). An OpenAI-compatible engine. **Saved state is optional**: without it the
  proxy still masks, archives, recalls and switches segments, and only the fast resume of a long session is lost.
  With it: llama-server with `--slot-save-path`, or Strata ≥ 0.1.40 with `--slot-save-path` (see
  [Engines](#engines)). The proxy creates that folder itself when it is missing and the engine is on this host.

## Quick start

Three levels. Each one stands on its own.

| | what you see | needs | time |
|---|---|---|---|
| **T0 — see it work** | archive, masking, exact recall, with a scripted fake model | Python ≥ 3.10 | 1 minute |
| **T1 — real model on CPU** | a real agent (pi) writing code through the proxy, masking, a recall probe (the tested 4B model did not call `recall`), resume after an engine restart | + cmake, a C++ compiler, Node.js ≥ 22.19, ~9 GB RAM (the engine at `-c 32768`), 3.5 GB disk | ~45 minutes |
| **T2 — real use (GPU)** | your own model and agent, long sessions | a GPU engine | — |

Commands are for Linux; see [Platforms](#platforms) for macOS and Windows (native or WSL).

### T0 — see it work (1 minute, no model)

<!-- readme-test: ci -->
```sh
python3 -m venv mnemonic-venv && . mnemonic-venv/bin/activate
pip install mnemonic-proxy
mnemonic-proxy demo
```

With [uv](https://docs.astral.sh/uv/), no venv to create: `uvx mnemonic-proxy demo`. `uvx` runs the command from a
temporary environment and installs nothing, so keep the prefix for the next commands (`uvx mnemonic-proxy check ...`)
or install the command once with `uv tool install mnemonic-proxy`. The development version (the
`main` branch, newer than the last PyPI release): `pip install git+https://github.com/lastreload/mnemonic-proxy`
(needs `git` on PATH: `sudo apt install git`). Its `--version` ends in `.dev0` — a `main` build is not the next
release, and the examples it points at are the ones on `main`.

The demo starts the real proxy in a temporary folder, in front of a scripted fake model. An agent reads a long
`build.log` that contains one build id; the session grows until the proxy hides the log; the demo prints what the
engine receives in its place (a one-line receipt); then the user asks for the build id, the model calls `recall`,
the proxy answers it internally and the archived text is compared byte for byte with the original. It ends with
`PASS` (exit 0) or `FAIL` (exit 1).

It proves the proxy's own logic: archive, masking, recall. It does not prove anything about a real model, its tool
calling, or saved engine state — T1 exercises those with a real model and reports its limitations.

### T1 — a real model on CPU

Tested end to end in a clean Ubuntu 24.04 container (see [Tested combinations](#tested-combinations)). A 4B model on
CPU is slow (seconds per answer) and limited: the point is to exercise the proxy with a real model, not to do real
work. A successful recall is not guaranteed; see the measured [Tested combinations](#tested-combinations).

**0. Prerequisites** (Ubuntu/Debian; other systems: [Platforms](#platforms)):

<!-- readme-test: real-engine -->
```sh
sudo apt install git cmake build-essential python3-venv curl
```

and Node.js ≥ 22.19 for pi (<https://nodejs.org/en/download>, or your package manager).

**1. Folder, proxy, example config.**

<!-- readme-test: real-engine -->
```sh
mkdir mnemonic-trial && cd mnemonic-trial
git clone --depth 1 https://github.com/lastreload/mnemonic-proxy
python3 -m venv .venv && . .venv/bin/activate
pip install ./mnemonic-proxy
cp mnemonic-proxy/examples/config.llama-server-32k.json .
mkdir -p slots
```

**2. llama.cpp, the tested release (CPU build, ~2 minutes on 12 cores).**

<!-- readme-test: real-engine -->
```sh
git clone --depth 1 --branch b11430 https://github.com/ggml-org/llama.cpp
cmake -S llama.cpp -B llama.cpp/build -DCMAKE_BUILD_TYPE=Release
cmake --build llama.cpp/build --config Release -j 8 --target llama-server
```

**3. The model**: Qwen3-4B-Instruct-2507, Q4_K_M (2.5 GB). Qwen publishes no GGUF for this model
([model card](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507)); this is the
[Unsloth conversion](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF), pinned to the tested revision:

<!-- readme-test: real-engine -->
```sh
mkdir -p models
curl -L -o models/Qwen3-4B-Instruct-2507-Q4_K_M.gguf \
  https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF/resolve/a06e946bb6b655725eafa393f4a9745d460374c9/Qwen3-4B-Instruct-2507-Q4_K_M.gguf
sha256sum models/Qwen3-4B-Instruct-2507-Q4_K_M.gguf
# 3605803b982cb64aead44f6c1b2ae36e3acdb41d8e46c8a94c6533bc4c67e597
```

**4. The engine** (terminal 1, inside `mnemonic-trial`):

<!-- readme-test: real-engine -->
```sh
llama.cpp/build/bin/llama-server -m models/Qwen3-4B-Instruct-2507-Q4_K_M.gguf \
  -c 32768 --parallel 1 --jinja --slot-save-path ./slots --port 8095
```

Wait for the line `listening on http://127.0.0.1:8095` (about 2 s once the model file is cached; `curl -s
localhost:8095/health` answers `{"status":"ok"}`). `--slot-save-path ./slots` is what makes saved state
possible, and it must be the same folder as `slot_dir` in the config (`./slots`). `--jinja` is already the default in
this build; it is written out because tool calling depends on it. `-c 32768` is the recommended window (the minimum
is 16384, see [Requirements](#requirements)); the example config starts masking at 14K tokens, so the proxy is at
work after a few long tool outputs.

**5. Check, then start the proxy** (terminal 2, inside `mnemonic-trial`, venv active: `. .venv/bin/activate`):

<!-- readme-test: real-engine -->
```sh
mnemonic-proxy check --live --upstream http://127.0.0.1:8095 --port 8096 --data ./data --config config.llama-server-32k.json
mnemonic-proxy --upstream http://127.0.0.1:8095 --port 8096 --data ./data --config config.llama-server-32k.json
```

`check` must end with `READY` (exit 0): engine recognised as llama.cpp, model loaded, window taken from `n_ctx`
(32768) with the thresholds scaled to it, saved state supported and configured, and — because of `--live` — one
real generation, one tool call, one save/restore whose file appeared in `./slots`. Each failing line says how to fix
it; see also [Troubleshooting](#troubleshooting). The proxy then prints
`[mnemonic-proxy] 127.0.0.1:8096 -> http://127.0.0.1:8095 (engine llama.cpp, saved state yes) ... window=32768`.

**6. pi, the coding agent** (terminal 3). Install the tested version:

<!-- readme-test: real-engine -->
```sh
npm install -g --ignore-scripts @earendil-works/pi-coding-agent@1.0.3
```

Create `~/.pi/agent/models.json` (if it exists, add the `mnemonic` entry to its `providers`):

<!-- readme-test: illustrative; config: client -->
```json
{
  "providers": {
    "mnemonic": {
      "baseUrl": "http://127.0.0.1:8096/v1",
      "api": "openai-completions",
      "apiKey": "local",
      "compat": { "supportsDeveloperRole": false, "supportsReasoningEffort": false },
      "models": [
        { "id": "local-model", "name": "local model via mnemonic-proxy", "reasoning": false,
          "contextWindow": 131072, "maxTokens": 2048 }
      ]
    }
  }
}
```

and `~/.pi/agent/settings.json` (if it exists, add these three keys):

<!-- readme-test: illustrative; config: client -->
```json
{
  "defaultProvider": "mnemonic",
  "defaultModel": "local-model",
  "compaction": { "enabled": false }
}
```

`compaction.enabled: false` matters: pi's own auto-compaction would summarise the history the proxy is managing.
`contextWindow` is the *virtual* window the client sees (131072), not the engine's 32768: pi subtracts the prompt size
from it to choose `max_tokens`, and with the engine's real window it would ask for fewer and fewer tokens as the
history grows, down to 1. Fitting the history
into the engine's real window is the proxy's job. `apiKey` is a placeholder (the proxy does not check it); the model
id is any name, llama-server serves its loaded model.

**7. The exercise.** In terminal 3, a folder with a log whose one interesting line is buried in the middle:

<!-- readme-test: real-engine -->
```sh
mkdir -p ~/mnemonic-exercise && cd ~/mnemonic-exercise
python3 -c "for i in range(650): print('[%04d] compiling module_%03d.c ... ok (%d ms)' % (i, i, 80 + i * 7 % 61) if i != 397 else '[0397] build id: BUILD-7f3a9c-ORCHID-42')" > build.log
pi
```

Type these requests one at a time and wait for each answer (or non-interactively, same session:
`pi -p "<request 1>"`, then `pi -c -p "<request 2>"`, …):

1. `Run python3 -c "import uuid; print(uuid.uuid4())" and tell me the value.` — a `bash` tool call; pi repeats the
   value.
2. `Run cat build.log and tell me whether every module compiled.` — a long output (≈13K tokens; on CPU the 4B model
   needs a few minutes to read it).
3. `Write primes.py with a function first_primes(n) that returns the first n prime numbers, and test_primes.py with
   three unittest tests. Run the tests.` — `write` calls, then `bash`. The prompt is now past the masking threshold
   (14K tokens with the 32K config): as soon as enough newer messages follow the log, the proxy hides it behind a
   receipt (here during step 4). Nothing is printed; check with
   `grep -c '"event": "mask"' ~/mnemonic-trial/data/journal.jsonl` (≥ 1).
4. `Add a function is_prime(n) to primes.py and a test for it in test_primes.py, then run the tests.`
5. `What build id is written in build.log? Do not run commands and do not read files.` — the log is no longer in the
   prompt, only its receipt; the expected path is a `recall` call answered by the proxy itself (pi never sees it):
   `grep -c '"event": "recall"' ~/mnemonic-trial/data/journal.jsonl`. Small models often skip it: see the results
   below.

Wait one minute (the proxy saves the engine state after 60 s idle: `"event": "autosave"`), then restart the engine:
Ctrl+C in terminal 1, start it again with the same command, and ask `Which files did you write in this session?`.
The proxy restores the conversation from `./slots` instead of re-reading it:
`grep '"event": "autorestore"' ~/mnemonic-trial/data/journal.jsonl` shows the restored tokens and milliseconds.

What this proves and what it does not, for this model: see [Tested combinations](#tested-combinations).

### T2 — real use (GPU)

Use the engine and model you already have; the only requirements are an OpenAI-compatible endpoint and, for saved
state, an engine that can save its KV state to disk:

<!-- readme-test: real-engine -->
```sh
llama-server -m your-model.gguf -c 131072 --parallel 1 --jinja --slot-save-path /path/to/slots --port 8095
mnemonic-proxy check --upstream http://127.0.0.1:8095 --port 8096 --data ./data --config config.json
mnemonic-proxy --upstream http://127.0.0.1:8095 --port 8096 --data ./data --config config.json
```

with `config.json` = `examples/config.llama-server.json` and `slot_dir` = the same `/path/to/slots` (see
[Configuration](#configuration) for the recommended fields). With an engine that has no saved state (vLLM, online
APIs) the proxy runs in base mode (window: see [Install](#install)). The measurements in
[One session, measured](#one-session-measured) (Qwen3.8 Flash Next IQ3_XXS, 128K window) come from
Strata (our session-files build, 0.1.38 + PR #668) on a 12 GB RTX 4070 Ti — see [Engines](#engines); they say nothing about
other hardware.

The proxy recognises the engine at startup and turns off, with a warning, whatever the engine cannot do
(`--engine auto|strata|llama.cpp|ds4|openai` forces it). `ctxproxy` is kept as an alias of `mnemonic-proxy`.
Optional: `--tokenizer` (a Hugging Face `tokenizer.json`, or a Strata pack `tokenizer/` folder; needs
`pip install 'mnemonic-proxy[exact]'`) for exact token counts.
If `--tokenizer` is explicitly supplied but cannot be loaded (missing `tokenizers`, bad path or invalid format),
startup fails before contacting the engine; it never silently switches that run to estimated counting. Install
`mnemonic-proxy[exact]` in the same environment as the proxy and check the path. Omit the option only when an
estimated guard is intended. Without a tokenizer, the proxy uses a chars/3.5 estimate;
with llama-server, `"engine_tokenize": true` counts through its `/tokenize`. A
systemd user unit is in [examples/mnemonic-proxy.service](https://github.com/lastreload/mnemonic-proxy/blob/main/examples/mnemonic-proxy.service).

**Window guard.** Before every call (answer, recall rounds, handoff notes, seal, anchor and retries), the proxy
checks `counted_prompt + max_tokens + window_margin ≤ window`. If it does not fit, it lowers `max_tokens`, removes
what the recall loop added (by value per token: results become one-line receipts, old reasoning becomes its
conclusion line, recallable by id) or returns HTTP 400 instead of sending. Both output-limit aliases are kept in
sync. A prompt that cannot be counted with a loaded tokenizer is refused rather than silently estimated.

With `--tokenizer`, the final guard and planning total now load an adjacent `chat_template.jinja`
(from the pack directory, or beside a supplied HF tokenizer file). This matters for fine-tunes such as Tiel:
its Sharp template adds instructions and tool-error warnings that the built-in Qwen renderer does not write.
Install/update `mnemonic-proxy[exact]` for both the tokenizer and sandboxed Jinja renderer. A discovered template
that cannot load or render is never silently replaced by the built-in one. Pictures are forwarded to the engine and
budgeted, not refused: the template writes one vision marker per picture (never its bytes), and the guard counts each
marker as `image_tokens` tokens. That number is an **upper bound**, and it has to be: no engine reports the real
patch count before the request (Strata has no `/tokenize`, and its `/v1/messages/count_tokens` counts the marker
alone). The rule is **`image_tokens >= vision.max_tokens + 2`**: the reader clamps one picture's expansion to
`vision.max_tokens` (Strata's `vision.max_tokens`, 1024 on GPU and 300 on CPU by default; without it a picture once
became 93,700 tokens), while the marker itself is three special tokens of which two - `<|vision_start|>` and
`<|vision_end|>` - stay in the prompt around the expansion the allowance replaces. So a pack clamped to 300 needs
**302**, and Strata's GPU default clamp of 1024 needs **1026** - which is the shipped default; a round 1120 is the
same rule with a little free headroom. An over-reservation costs a little context, an under-reservation would send a
prompt over the window.
`image_tokens` has to be a non-negative integer (config load rejects anything else), and a request that carries a
picture while the bound is `0` is refused with `image_tokens=0` in its message: a picture cannot be priced at
nothing, and the startup line says the same before the first request.

Everything else about pictures is fail-closed, because a counted prompt that is not the prompt the engine builds is
a window nobody can guarantee. The markers the template wrote must be exactly the pictures being priced - a template
without a vision branch (a fine-tune that prints `content` as text) cannot serve pictures and is refused, never
tolerated. A picture in a `system` message is refused: Strata hands that message its text parts and the pack template
raises on its images, so its bytes would never reach the model. A picture with no readable source (a `file_id`, an
empty url) is refused instead of turning into an empty image, and a picture carried under a content type the adapter
does not read is refused instead of disappearing from the prompt. Video and audio parts stay refused: no supported
engine reads them, so their marker would have no honest budget. `window_guard` events for a prompt with pictures
carry `guarantee=image_bounded` with `images` and `image_allowance`, text-only prompts keep `guarantee=exact` and
their journal lines are byte-identical to before, and a refusal carries the reason in its 400 message. The structural
part of that holds on the estimated path too: without a tokenizer the count is only `guarantee=estimated`, but a
picture the adapter would not read is still a lost turn, so it is refused there as well.

A marker **quoted in text** is not a picture. Someone pasting `<|vision_start|><|image_pad|><|vision_end|>` into a
message - asking about the template, or pasting a log - puts the real spelling of the marker in the prompt, and
Strata shields such spellings instead of reading a picture (#28). The guard subtracts quoted spellings before it
checks markers against pictures and before it prices them (their characters stay reserved as literal slack), and the
saved-state stamp counts only pictures, so a quote cannot steal a picture's identity. The quote still changes the
prompt's identity: it is part of the prompt.

Picture bytes never reach disk. `live_dump` and the KV sidecar name a picture by hash the way the journal does, and
they fold a `data:` URI or a long base64 run found inside *text* too - a tool result that prints a screenshot used to
write megabytes of base64 into `live/last_request.json`. The prompt forwarded to the engine is not folded: the
picture gets there whole.

Engine state (autosave checkpoints, masking anchors) is keyed by the prompt's hash, so a picture joins that identity
only where the proxy can name its bytes: a `data:` URI is hashed by content and stamped at the marker the template
wrote, so the same text with another picture is a different state and can never be restored under the previous
image's embeddings. A picture referenced from *outside* the prompt - an `http(s)` url or a file path - can hold
different bytes on the next turn under the same name, so a prompt carrying one records no state, restores none and
seals no anchor (`anchor_skip reason=volatile_picture`); its tokens are budgeted the same way. Send `data:` URIs
(OpenCode does) when a conversation should keep its state reuse. The proxy cannot make the *engine's* own prefix
cache safe for a url whose content changed under the same pad count - a second reason to prefer `data:`.
Without that file, the historical built-in Qwen rendering remains (`template=builtin-qwen` at startup);
use it only with a matching server template. Per-message planning costs remain Qwen approximations; the full
pack-rendered total and final guard are what enforce the window.

A matching tokenizer/template still does not validate hidden server settings. Recent Strata/PolyStrata encode special-token spellings
quoted inside content (for example `</think>`) as ordinary text, not single special tokens. The guard reserves an
additional conservative byte-BPE bound for these literals, including tool schemas and decoded call arguments;
`window_guard` events carry `guarantee=tokenizer_bound` and `literal_slack` when this reserve is nonzero
(`guarantee=exact` otherwise). This may lower the output ceiling slightly more than necessary. Arbitrary templates,
a tokenizer for another model, and server-side prompt additions are not covered by a local exact-count claim.

Without a tokenizer the count is the calibrated chars/3.5 estimate (`guarantee=estimated`): on text with many digits
or symbols the real count can be well above it, so use the correct `--tokenizer` (or raise `window_estimate_slack`,
e.g. `0.3`) when the window is small. On generic engines (Ollama, LM Studio, any OpenAI-compatible) without
`--tokenizer` the slack is 0.15 by default (0.3.8); Strata, llama.cpp and ds4 keep 0. This 15% is not an extra reserve
on top of a loaded tokenizer. `"window_guard": false` explicitly disables the protection.

The calibration factor is learned from the `usage.prompt_tokens` the engine reports, with guards against a
single misleading sample: samples under 1,000 estimated tokens are ignored, a sample whose real/estimated ratio
falls outside 0.25–4.0 is rejected and journalled (`calibration_rejected`), and until 5 samples have been accepted
the factor may only grow, never shrink — overestimating costs a little window, underestimating masks too late. A
prompt the engine cut is already excluded (0.3.8). The clamp stays 0.5–2.0: chars/3.5 is a deliberately pessimistic
baseline for prose, so a factor below 1.0 is a legitimate correction, and `window_estimate_slack` is the knob for
extra prudence. Exact counting with a tokenizer is never calibrated.

**Context diagnostics.** The CLI prints startup/version/window/template and concise runtime events to **stderr**:
`window_guard` (including every checked call, clamp, count failure, local refusal and engine-count mismatch),
`response_clamped`, `mask`, `switch`, `switch_skipped`, and `client_disconnected`. No prompt/notes/error-body text
is printed by this summary. Capture it with `2> proxy-events.log` (or use your service manager's journal).
The full structured log stays at `<--data>/journal.jsonl`; recent events are also available at
`GET /v1/strata/journal`. The optional [dashboard](#dashboard-optional-needs-the-git-clone-ui-in-italian) reads the data directory; do not confuse its
port with the proxy's. `where=answer|recall_round|final|notes|seal|anchor|answerfix` identifies the upstream phase;
a client continuation is a new answer request, not a distinct server-side phase. `seal` and `anchor` deliberately
request one token to establish saved state; this differs from a client answer clamped to one token.

**The prompt head is measured, not guessed (`tool_heads`, 0.3.24).** The head — the template scaffolding, the tool
definitions and the system prompt — is the largest single occupant of an interactive prompt, and until 0.3.24 it was
recorded nowhere: the `request` event carries aggregate counters only, and the archive holds messages, not tools.
`journal_tool_heads` (on by default) writes **one** `tool_heads` line **per conversation and per change of the tool
list** — not per request — with the list's fingerprint, the number of tools, for every tool its **name**, the tokens
of the full definition and the tokens of its `description` alone, the counted head total (`head_tokens` =
`defs_tokens` + `system_tokens` + `frame_tokens`), and, when `tools_paging` is on, which tools stayed in the head
(`base`) and which went to the loadable catalog (`catalog`). `counting` says whether the numbers are `exact` (pack
tokenizer + real template) or `estimated` (the chars/`chars_per_token` fallback); the counter is the one the proxy
already uses for the window. **Names and numbers only: no definition text, no `description` text and no system
prompt ever enter the journal** — the record is built from names and integers, so it cannot carry text, and
`tests/test_tool_heads.py` proves it (`toolheads.leaks`, `toolheads.unknown_strings`). One line is about 450 bytes
and its size does not grow with the length of the definitions. This makes `tooldefs_desc_max`, `tooldefs_param_max`
and `tools_paging` measurable after the fact. Note that the pager itself journals nothing: `tools_search` and
`tool_not_loaded` only appear when the **model** calls `tools` or an unloaded tool, so before this event a journal
without them could not tell "paging never ran" from "paging ran and the model never touched the catalog" — this line
tells them apart. `tool_heads` is a measurement, not a decision: the prompt sent to the engine is byte-identical
with it on or off.

If PolyStrata rejects a request *before generation* with its explicit context/count error, the proxy records
both counts and retries **once**, unchanged except for lower output/reasoning limits derived from that engine
count. An engine-counted prompt with no answer room becomes a local `window_guard` error without a retry.
Unrelated 400s, transport errors and errors after streaming starts are not retried. This is a safety net, not
proof that the first request always fits arbitrary server-side modifications (for example restored hidden
reasoning or an effort instruction moved by the server). `fit_max_tokens=true` is an additional engine-side
output safety net, but cannot make an already oversized prompt fit. `window_margin` applies in tokenizer mode;
`window_estimate_slack` does not. Increasing the margin is not a substitute for the correct template.

Disable the agent's own auto-compaction in every client below, otherwise two context managers fight over the same
history.

### pi, Hermes, Continue, … (Chat Completions)

Point the client's OpenAI base URL at `http://127.0.0.1:8096/v1`. For pi, the two files of T1 step 6 (with your real
`contextWindow`/`maxTokens`). For other clients: their OpenAI-compatible provider setting, plus their own way to turn
off context compaction.

**omp ([oh-my-pi](https://github.com/can1357/oh-my-pi))** — tested with 18.10.1 on Strata. omp reads YAML from
`~/.omp/agent/` (or `$PI_CODING_AGENT_DIR`). Add the proxy as a provider in `models.yml`:

```yaml
providers:
  mnemonic:
    baseUrl: http://127.0.0.1:8096/v1
    api: openai-completions
    apiKey: none
    auth: apiKey
    compat:
      supportsDeveloperRole: false
      supportsReasoningEffort: false
      maxTokensField: max_tokens
      thinkingFormat: qwen-chat-template   # for Qwen models; drop it for others
    models:
      - id: qwen3.8-flash-next-iq3_xxs     # the id your engine reports at /v1/models
        name: Flash Next via mnemonic-proxy
        reasoning: true
        input: [text]
        contextWindow: 131072              # the engine's real window
        maxTokens: 16384                   # leave room for reasoning (see the ds4 note below)
        cost: {input: 0, output: 0, cacheRead: 0, cacheWrite: 0}
```

and turn omp's own compaction off in `config.yml`, so the proxy manages the window:

```yaml
compaction:
  enabled: false
```

Then `omp --model mnemonic/qwen3.8-flash-next-iq3_xxs`. If you use extensions that also shorten tool output (for
example SoL-Pi's ObservationPack), we have not tested them together with the proxy.

### opencode (Chat Completions)

Tested with opencode **1.19.5** on Strata: one 1 h 32 min session, 554 requests, 51 masks, 44 `recall` calls of
which 19 returned archived text, numbers [below](#opencode-on-strata-measured). Put this in
`$XDG_CONFIG_HOME/opencode/opencode.json`
(global; `$XDG_CONFIG_HOME` defaults to `~/.config`, so that is usually `~/.config/opencode/opencode.json`)
or `opencode.json` in the project:

<!-- readme-test: real-engine; config: client -->
```json
{
  "$schema": "https://opencode.ai/config.json",
  "compaction": { "auto": false },
  "autoupdate": false,
  "provider": {
    "mnemonic": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "mnemonic-proxy",
      "options": {
        "baseURL": "http://127.0.0.1:8096/v1",
        "apiKey": "local",
        "timeout": false,
        "headerTimeout": false,
        "chunkTimeout": false
      },
      "models": {
        "qwen3.8-flash-next-iq3_xxs": {
          "name": "Flash Next via mnemonic-proxy",
          "tool_call": true,
          "reasoning": true,
          "limit": { "context": 131072, "output": 16384 },
          "cost": { "input": 0, "output": 0, "cache_read": 0, "cache_write": 0 }
        }
      }
    }
  },
  "model": "mnemonic/qwen3.8-flash-next-iq3_xxs"
}
```

The model key is the id your engine reports at `/v1/models`; `limit.context` is the engine's real window. Then
`opencode` (TUI) or, non-interactively, `opencode run --model mnemonic/qwen3.8-flash-next-iq3_xxs --auto "…"` and
`opencode run -c --model … --auto "…"` to continue the same session.

**Auto-compaction off**: `"compaction": {"auto": false}` is the real option (`Enable automatic compaction when
context is full`, default `true`, in opencode's own `config.json` schema). With it off, a 537-message session
produced no summary message and no compaction event in opencode's database. Note that opencode counts tokens from
the `usage` the proxy returns — the **physical** prompt (max 108K here), not the real history (1.17 M tokens at the
end) — so it would rarely trigger compaction anyway; turn it off regardless, so only one context manager is at work.

Limits found:

- Use the **`provider`** key with **`npm`**, not the newer plural `providers` + `package`: with `providers` the
  model does not appear in `opencode models` and `opencode run` fails with
  `UnknownError … Unexpected server error`.
- If npm blocks install scripts, `opencode-ai`'s `postinstall` does not fetch the binary: run
  `cd node_modules/opencode-ai && node postinstall.mjs` once.
- `opencode run` needs `--auto`, otherwise it waits for permission approvals that never come.
- Tool calls go through unchanged (669 calls: `read`, `bash`, `edit`, `write`, `grep`; no empty results, no HTTP
  errors). The only failures were 5 `edit` calls rejected **by opencode** with `Could not find oldString in the
  file`: the model rebuilt the old text from memory after its own earlier tool arguments had been masked. It
  recovered with `write`.
- `recall` never appears in opencode's tool list: the proxy injects it and answers it in its own internal rounds.
- The model re-reads a lot (415 `reread` events, often `read … limit=60`); in one turn that became a ~20 minute
  read loop before it wrote the file. That is the model, not the proxy.

### Claude Code (Anthropic Messages)

Checked against Claude Code 2.1.287; a 1 h 41 min session with 2.1.284 on Strata is measured
[below](#claude-code-and-codex-live-on-strata). Claude Code may print `unrecognized_model local-model`: it works
anyway.

<!-- readme-test: real-engine -->
```sh
export ANTHROPIC_BASE_URL=http://127.0.0.1:8096      # no /v1
export ANTHROPIC_AUTH_TOKEN=local                    # any value; the proxy does not check it
export ANTHROPIC_MODEL=local-model                   # any name; the engine serves its loaded model
export ANTHROPIC_DEFAULT_HAIKU_MODEL=local-model     # background tasks (replaces ANTHROPIC_SMALL_FAST_MODEL)
export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1    # fewer side requests competing for the engine
export DISABLE_AUTO_COMPACT=1                        # turns off auto-compaction; /compact still works
claude
```

`ANTHROPIC_SMALL_FAST_MODEL` is still read by 2.1.287 (it takes precedence), but the documented name is
`ANTHROPIC_DEFAULT_HAIKU_MODEL`. `DISABLE_COMPACT=1` would also turn off the manual `/compact`.
`POST /v1/messages` (streaming and not) and `POST /v1/messages/count_tokens` are supported. Thinking blocks get a
local placeholder signature: a session started through the proxy cannot be continued on Anthropic's API.

### Codex (OpenAI Responses)

Codex 0.160 speaks only the Responses API (`wire_api = "chat"` is rejected). In `~/.codex/config.toml` (or a separate
`CODEX_HOME`):

```toml
model = "local-model"
model_provider = "local"
model_context_window = 131072              # the proxy's window; Codex compacts relative to this
model_auto_compact_token_limit = 100000000 # compaction threshold far above any real session

[model_providers.local]
name = "local engine via mnemonic-proxy"
base_url = "http://127.0.0.1:8096/v1"
wire_api = "responses"
env_key = "LOCAL_API_KEY"          # export LOCAL_API_KEY=local (any value)
requires_openai_auth = false
supports_websockets = false
```

Codex 0.160 has no setting that turns auto-compaction off: `model_auto_compact_token_limit` only moves the
threshold. Set it far above any session, as above, so that in practice the proxy is the only context manager.
Codex's `prompt_cache_key` is used as the conversation key. Stateless only (`store=false`, no
`previous_response_id`), which is what Codex sends.

### MCP recall server (Claude Code, Codex, Hermes)

The archive can also be searched from any MCP client, read-only (sqlite `mode=ro`; the proxy can keep writing). Three
tools: `recall` (same search as the proxy's tool), `conversations`, `journal`.

<!-- readme-test: ci -->
```sh
mnemonic-mcp --db ./data/archive.sqlite                 # stdio
mnemonic-mcp --db ./data/archive.sqlite --http 8133     # streamable HTTP on 127.0.0.1:8133/mcp
```

<!-- readme-test: real-engine -->
```sh
claude mcp add mnemonic -- mnemonic-mcp --db /path/to/data/archive.sqlite
codex mcp add mnemonic -- mnemonic-mcp --db /path/to/data/archive.sqlite
hermes mcp add mnemonic --command mnemonic-mcp --args --db /path/to/data/archive.sqlite
```

`python3 -m ctxproxy.mcp_server` is the same program. Hermes `config.yaml` equivalent:

```yaml
mcp_servers:
  mnemonic:
    command: mnemonic-mcp
    args: [--db, /path/to/data/archive.sqlite]
    enabled: true
```

### Dashboard (optional; needs the git clone; UI in Italian)

The dashboard is not part of the pip package: it runs from a clone of this repository, and its interface is in
Italian.

<!-- readme-test: real-engine -->
```sh
python3 mnemonic-proxy/dashboard/ctxdash.py --data ./data --strata http://127.0.0.1:8095 --proxy http://127.0.0.1:8096 --port 8097
```

Read-only, on `127.0.0.1:8097`: engine status, physical vs. virtual context over time, masking/segment/recall events,
and the live physical prompt (with `live_dump: true`).

### Proxy endpoints

Besides the client APIs (`/v1/chat/completions`, `/v1/messages`, `/v1/responses`), all other paths are passed to the
engine. The proxy's own:

| endpoint | what |
|---|---|
| `GET /health` | proxy + engine health: `{"status": "ok" \| "loading" \| "engine_unreachable", "engine", "version", "upstream"}`; HTTP 200 only when the engine is ready |
| `GET /v1/engine` | what was detected: `kind`, `slot_save` (saved state supported and on), `n_ctx`, `model`, `notes`. `GET /v1/strata/engine` is the same (0.1 name, kept) |
| `GET /v1/strata/conversations/<id>` | one conversation: archived messages, masks, segments |
| `GET /v1/strata/archive/<id>` | one archived block, verbatim |
| `GET /v1/strata/journal` | the last 200 journal events |

## Tested combinations

### opencode on Strata, measured

**0.3.21, opencode 1.19.5 on Strata** (2026-11-01): PC4070TI, Strata 0.2.6 / engine 0.1.50 with Qwen3.8 Flash Next
GSQ-RCO IQ3_XXS, `--max-context 131072 --kv int8 --kv-resident 32768`, proxy window 131072 (mask trigger ~80K,
target ~40K), `--tokenizer` from the pack. opencode installed in an isolated prefix with its own `XDG_*` dirs,
auto-compaction off, one session, eight consecutive turns driven with `opencode run` / `run -c` on a throwaway copy
of 29 Python modules (13,911 lines): write one markdown document per group of modules, then write and test a new
module, then answer questions about the session from memory.

| | |
|---|---|
| session | 1 h 32 min 30 s, 554 requests, 235,380 tokens generated |
| history vs prompt | real history up to **1,171,531** tokens; physical prompt median 77,027, max **108,332** |
| prefill | 1,866,843 tokens actually read, 40,031,102 reused from saved state (**97.8 % reuse**) |
| TTFT (proxy-side prefill), all requests | median **1,902 ms**, max 30,279 ms |
| TTFT on the 51 requests where masking happens | median **7,023 ms**, max 19,574 ms |
| TTFT on the 51 requests right after a mask | median **1,930 ms**, max 17,188 ms |
| generation | median 49.5 tok/s, max 90.5 tok/s |
| masking | 51 masks, from `93,470 → 57,659` (3 pieces) down to 1-piece emergency batches |
| segments | 3 switches; `seal` 1.8–2.8 s, `save` 0.80–0.84 s per file |
| anchor | 39 `anchor_save`, 36 `anchor_restore`, 2 `anchor_skip` |
| `recall` | **44 calls by the model; 19 returned archived text** (8 by `query`, 11 by arguments id as 700-char excerpts), 25 returned none (21 output ids with `mode=output`, which by design answers only with a pointer to the arguments id; 4 `path` calls empty because of the filter fixed in 0.3.24). All 32 id calls asked for blocks masked inside the current turn: `mode=output` served them without that filter, but a plain `recall(id=…)` of the same blocks would have been refused by 0.3.23 (see CHANGELOG). `recall_use` marks 35 of 44 as used |
| tool calls | 669 (`read` 434, `bash` 190, `edit` 33, `write` 10, `grep` 2); 0 empty results |
| errors | 0 `proxy_error`, 0 `upstream_error`, 0 `client_disconnect`, 0 non-200; 5 `edit` calls rejected by opencode (stale `oldString`), 1 turn with no final answer (`final_answer_missing`) |

What it shows: masking costs about **5 s of extra prefill on the request where it happens** (7.0 s against a 1.9 s
median) and **nothing on the next one** (1.93 s against 1.886 s for requests far from a mask), because the anchor is
saved and restored instead of re-prefilling the shortened prompt. The model asked for `recall` on its own whenever
it needed a masked tool result, and the three memory questions at the end of the session were answered correctly
after seven `recall` calls. What it does NOT show, and what a re-reading of this journal found later: the id calls
of this session all pointed at blocks masked inside the *current* turn. They all used `mode=output`, which in
0.3.23 skipped the archive filter: each output id got only a pointer to its arguments id, and the arguments id gave
700-char excerpts, never the verbatim text. A plain `recall(id=…)` of those blocks would have been refused
(`idx < max_idx`), and the 4 `path` calls came back empty for that reason. The filter is fixed in 0.3.24; these
numbers are the 0.3.23 behaviour. Also not shown: the
interactive TUI, `opencode serve`/`web`/`attach`, MCP servers
or sub-agents, opencode's own compaction running *together* with the proxy, and the client-side TTFT (we measured
the proxy's `prompt_ms`). One turn out of eight ended with no final answer: the model spent the whole turn reading.

**0.3.8, Ollama and LM Studio: window read from the engine** (2026-10-19): same machine, engines and model as the
0.3.7 run below (Ollama with the integrated GPU, `OLLAMA_IGPU_ENABLE=1`, context set with `OLLAMA_CONTEXT_LENGTH`;
LM Studio `lms load … [--context-length 32768]`), no `--tokenizer`. Report: `docs/dev-notes/ENGINE-WINDOW-038-RESULT.md`.

| test | Ollama | LM Studio |
|---|---|---|
| context read by the proxy (`/api/ps`, `/api/v0/models`) | 4096, 32768 | 8192, 32768 |
| small context, `check` without config / with `window` 32768; proxy start | NOT READY: 4096 < 16384 / also "config window=32768 > Ollama context 4096"; start refused | same with 8192 |
| small context, proxy allowed below the minimum (development switch), prompts of 5.4K and 10.8K estimated | window 4096: segment switches, 0.97K / 0.93K sent, codeword right, nothing cut | window 8192: 6.0K and 1.1K sent, notes 6.5K, codeword right, nothing cut |
| forced cut: engine hidden behind a plain `/v1` forwarder, config `window` 32768 | `engine_truncated` ×2 (11.2K counted → 3.7K read; 22.0K → 3.2K), 1 warning; `check --live` fails ("request (29473 tokens) exceeds … 4096") | ×2 (11.2K → 3.8K; 22.0K → 3.2K), 1 warning; `check --live` fails (… 8192) |
| context 32768: `check --live` full-window probe | 29,473 tokens sent, 29,473 read | 29,473 / 29,473 |
| context 32768: the notes request that 0.3.7 cut (prompt ≈ 35.7K real) | 21 of 28 messages kept, notes request 27.7K real tokens, not cut; codeword right | 27.7K, not cut; codeword right |
| context 32768, no `window` in the config: tool conversation (12 files) | — | 21 requests all 200, 19/19 valid tool calls, 1 mask (21.8K → 7.3K), 1 `recall` served, 0 `engine_truncated` |

**0.3.7, Ollama and LM Studio** (2026-10-19): Linux, Ryzen AI Max+ 395 (Radeon 8060S integrated GPU, Vulkan), both
engines installed in user space (Ollama 0.40.6 official tarball; LM Studio headless `llmster` 0.0.25 with its
llama.cpp Vulkan runtime 2.41.0), same model in both: Qwen3-4B-Instruct-2507 Q4_K_M. Proxy from `main` with
`config.openai-32k.json`, one request at a time from a small Python client (no agent).

| test | Ollama | LM Studio |
|---|---|---|
| `check` | `READY` (exit 0); without a config `READY with warnings`: window unknown, 131072 | `READY` (exit 0) |
| engine context by default | 4096 (CPU; with `OLLAMA_IGPU_ENABLE=1`: 262144) | 8192 |
| longer prompts at the default context (Ollama ≈ 6–36K real tokens, LM Studio ≈ 8.6–21K), straight to the engine and through the proxy | HTTP 200, prompt cut to 2.7–3.7K tokens, a codeword from the first message lost | HTTP 200, prompt cut to 2.7–3.8K tokens, beginning and end kept |
| engine context 32768: tool conversation over 12 files (`list_files`, `read_file`, `calc`) | 23 requests, all 200; 21 tool calls, all valid; 1 mask (prompt 19.4K → 7.4K); largest prompt 19.4K; nothing cut | 23 requests, all 200; 21 tool calls, all valid; 1 mask (19.3K → 7.3K); largest prompt 21.3K; nothing cut |
| engine context 32768: one prompt of ≈ 35.7K real tokens | straight: cut to 29.8K, codeword lost; proxy: segment switch, 6.3K sent, codeword right | straight: cut to 14.8K; proxy: segment switch, 6.2K sent, codeword right |
| the proxy's own notes request at that switch (no `--tokenizer`) | estimated 31.3K, cut by the engine to 30.5K | estimated 31.3K, real 33.4K, cut to 15.1K; with `--tokenizer`: 30.8K, not cut |
| streaming, `/v1/messages`, `/v1/responses` | streamed (11 chunks), 200, 200 | streamed (11 chunks), 200, 200 |

The model stopped before reading every file (10 of 12 on Ollama, 11 of 12 on LM Studio; the sums it made were right
for the files it read) and, asked about a file that was still in view, called `recall` for the wrong piece and said
it could not quote it: the proxy served the piece the model asked for. These are limits of the 4B model, not of the
engines.

**0.3.0, engine `-c 32768`** (2026-10-06): T1 run as written above, on the CPU of a Ryzen 7 5700G (16 threads, no
GPU, llama-server at `nice 19`), in a fresh folder with its own `HOME`: llama.cpp `b11430` CPU build, pi 1.0.3,
Node 24.14, Python 3.14, `config.llama-server-32k.json`. Requests sent with `pi -p` / `pi -c -p`, one at a time.

| model | `check --live` | tool calls | masking | recall (step 5) | engine restart |
|---|---|---|---|---|---|
| Qwen3-4B-Instruct-2507 Q4_K_M (Unsloth) | READY (exit 0) | yes; steps 1–4 done, 4/4 tests pass | yes: 1 mask (the 13.4K-token log, prompt 17.3K → 4.0K) | **no**: answered "cannot determine" instead of calling `recall` | autorestore 4112 tokens in 349 ms; next prompt 4157/4176 reused |

Times on this CPU: steps 2–4 took 7, 5 and 10 minutes (reading 13K tokens of log, then generating at a 16K prompt);
the whole exercise about 25 minutes. Memory: llama-server RSS 8.9 GB at `-c 32768`; one saved state of 4.1K tokens
is 600 MB in `./slots`. A first run with a 150-line log (≈3K tokens, the 0.2.1 exercise) never reached
the masking threshold at 32K (largest prompt 10K): step 5 was answered right from the prompt, not tested. Hence the
650-line log above.

**0.2.1, engine `-c 8192`** (windows below 16K are refused since 0.3.0): run literally as written in T1 at the time,
in a clean `ubuntu:24.04` container (12 CPU cores, no GPU, user without sudo), llama.cpp `b11430` CPU build, pi
1.0.3, Node 22.23.3, Python 3.12, the 8K example config of 0.2.1 (2026-10-06).

| model | `check --live` | tool calls | masking | recall (step 5) | engine restart |
|---|---|---|---|---|---|
| Qwen3-4B-Instruct-2507 Q4_K_M (Unsloth) | READY | yes | yes: 5 masks, 4 segment switches | **no**: answered "cannot determine" instead of calling `recall` | autorestore 2450 tokens in 42 ms; next prompt 2486/2505 reused |
| Qwen2.5-Coder-7B-Instruct Q4_K_M (Qwen) | READY with warnings (no tool call) | **no**: writes the call as JSON text, same straight to llama-server | — | — | autorestore 3698 tokens in 17 ms |

What T1 proves: the proxy in front of a real llama-server — window read from the engine, thresholds scaled to it,
masking under a real agent (and, at 8K, segment switches), state saved when idle and restored after an engine
restart without re-reading. What it does not prove: that a 4B model uses `recall` reliably (it did not, at 8K or at
32K), or that the agent always finishes the task — at 8K, in step 4 the 4B model looped on read/edit until the
timeout. Those depend on the model; use T2 for real work.

Found while testing, fixed in 0.2.1: with the extended recall tool (`recall_struct`, `recall_multi`) in the tool
list, Qwen3-4B made 0/6 tool calls (4–6/6 without): the example configs keep the short `recall` tool.

## Troubleshooting

Start with `mnemonic-proxy check` (add `--live` to exercise the engine): every failing line says what to change.

| symptom | cause | fix |
|---|---|---|
| `check`: port … is in use | another proxy (or another program) on that port | stop it, or pass a different `--port` (and change the client's base URL) |
| `check`: engine answers 503 / `GET /health` says `loading` | llama-server is still loading the model | wait for `listening on …` in its log |
| `check`: engine not reachable | wrong `--upstream`, or the engine is not running | start the engine; `curl http://127.0.0.1:8095/health` must answer |
| proxy exits at startup: `refusing to start, the context window is too small` / `check`: context window … minimum is 16384 | engine started with a window below 16K (`-c 8192`), or `"window"` below 16384 in the config | restart the engine with `-c 32768` (ds4-server: `--ctx 32768`); remove `"window"` from the config (it is read from the engine). See [Requirements](#requirements) |
| llama-server: `failed to allocate` / killed | not enough memory for model + context | a smaller quantisation or a smaller model; the window can go down to 16384 (`-c 16384`), not below |
| HTTP 400 `exceeds the available context size` | the client asked for more than the window | proxy started with a config whose `window` is larger than the engine's `-c`? The proxy reads `n_ctx` from llama-server at startup: restart the proxy after changing `-c` |
| the model describes the command instead of calling a tool, or says it "cannot run commands" | chat template without tools, or a model weak at tool calling | llama-server with `--jinja`; `check --live` shows whether a tool call works; try a stronger model (see [Tested combinations](#tested-combinations)) |
| `check`: saved state supported by the engine, not enabled in the proxy | config without `slot_save` | nothing to fix unless you want the fast resume: it is optional, and the line says how to add it later |
| `check --live`: the state file is not in `slot_dir` | `slot_dir` ≠ llama-server `--slot-save-path`, or the engine runs on another host / in a container with another path | the same folder, as seen from the proxy's host |
| `check`: engine detected as `openai` | llama-server too old, or another engine | saved state needs llama-server with `--slot-save-path`, or Strata ≥ 0.1.40 with `--slot-save-path`; everything else works |
| Strata has no saved state | Strata older than 0.1.40, or started without `--slot-save-path` | optional: base mode keeps working. For the fast resume, update to Strata ≥ 0.1.40 and start it with `--slot-save-path DIR` |
| `check`: `slot_dir … does not exist and the proxy could not create it` | the path is not writable by the user running the proxy | run the `mkdir` command the message prints, or point `slot_dir` at a writable folder (the engine's `--slot-save-path`) |
| answers get shorter and shorter / summaries appear in the history | the client's own compaction is on as well | turn it off: pi `"compaction": {"enabled": false}`, opencode `"compaction": {"auto": false}`, Claude Code `DISABLE_AUTO_COMPACT=1`, Hermes `compression.enabled: false`, Codex: [threshold](#codex-openai-responses) |
| Windows: `\u27ea` in the output of `demo` / `check`, or `?` where `·` `—` `«»` should be | before 0.3.24 a non-UTF-8 console got `errors="backslashreplace"` | fixed in 0.3.24: on a console that is not UTF-8 the proxy prints ASCII stand-ins (`<<`, `>>`, `--`). Nothing sent to the engine or written to disk changes; `chcp 65001` (UTF-8) brings the real characters back |
| Codex: `wire_api = "chat"` rejected | Codex ≥ 0.160 only speaks the Responses API | `wire_api = "responses"` |
| `kv_archive` refused | needs Python ≥ 3.14 (`compression.zstd`) | Python 3.14, or leave `kv_archive` off (default) |

## Platforms

- **Linux**: the reference. Every tested combination below ran on Linux.
- **macOS**: the proxy is plain Python and should work as on Linux (not yet tested). Build llama.cpp the same way
  (Metal is on by default on Apple Silicon) or install it with Homebrew (`brew install llama.cpp`), then use the same
  `llama-server` command; `sha256sum` is `shasum -a 256`.
- **Windows, native** (since 0.3.2; tested on the `windows-latest` CI runner, not yet on a desktop): Python ≥ 3.10
  from python.org, the official llama.cpp Windows build (`llama-b11430-bin-win-cpu-x64.zip` or a GPU one). In
  PowerShell:

  <!-- readme-test: windows -->
  ```powershell
  py -m venv mnemonic-venv; .\mnemonic-venv\Scripts\Activate.ps1
  pip install mnemonic-proxy
  mnemonic-proxy demo
  mkdir slots
  llama-server.exe -m model.gguf -c 32768 --jinja --slot-save-path .\slots --port 8095   # in a second window
  mnemonic-proxy check --live --upstream http://127.0.0.1:8095 --data .\data --config config.llama-server.json
  mnemonic-proxy --upstream http://127.0.0.1:8095 --port 8096 --data .\data --config config.llama-server.json
  ```

  `config.llama-server.json` is in `examples\` (`"slot_dir": "./slots"`: relative paths are resolved from the folder
  you start the proxy in, so start the engine and the proxy from the same folder), and
  `mnemonic-proxy init-config --engine llama-server --slot-dir .\slots` writes the minimal version of it.
  **One click, any engine** (0.3.24): `mnemonic-proxy init-config --engine strata --launcher` writes
  `start-mnemonic-proxy.bat` next to the config, with your `--upstream`, `--port`, `--data`, `--config` and
  (optional) `--tokenizer` already in it — start Strata yourself, then double-click the `.bat`. It checks that the
  engine answers, runs `check` once (a taken port is reported there), starts the proxy and ends with `pause`.
  [`examples\start-windows.bat`](https://github.com/lastreload/mnemonic-proxy/blob/main/examples/start-windows.bat)
  is the llama-server variant that also *starts the engine*: it runs
  `llama-server.exe` in its own window with `--slot-save-path .\slots`, waits for it, runs `check`, then the proxy on
  port 8096 (edit the four paths at the top: `LLAMA`, `MODEL`, `CONFIG`, `VENV`). What CI proves on Windows: unit
  tests, demo on a cp1252 console, `check --live` READY, chat through the proxy, `start-windows.bat`, the generated
  `start-mnemonic-proxy.bat` against a fake engine, autosave and
  autorestore after an engine restart (3.2K tokens restored in 95 ms; the turn takes 2.3 s instead of 35.7 s),
  `kv_archive` round trip.
  Not tested: real agents (pi, Claude Code, Codex) on Windows, GPU builds, the dashboard. `sha256sum` is
  `Get-FileHash -Algorithm SHA256`.
  **Console**: a PowerShell window whose code page is not UTF-8 cannot carry the characters the proxy prints
  (`⟪ ⟫ · — «»`). Since 0.3.24 the commands detect it and print ASCII stand-ins instead (`<<ctx-archive id=… -
  output of bash …>>`, `--`, `"…"`), so the report stays readable and nothing arrives mangled; accents in paths are
  folded (`Projet par défaut` -> `Projet par defaut`). `chcp 65001` before running the command brings the real
  characters back. This is the console view only: the text sent to the engine, the archive, the journal and
  `last_request.json` are byte for byte the same on every platform.
- **Windows, WSL 2**: follow the Linux commands inside WSL. Keep the engine, the proxy and the `slots` folder all
  inside WSL, so that `slot_dir` and `--slot-save-path` are the same path. Not yet tested.
- **Android (Termux)** (0.3.8; tested in Waydroid 1.6.2 on Linux — Android 13, x86_64 — with Termux 0.118.3 and its
  Python 3.14.8; not yet on an ARM phone). The proxy is plain Python, nothing is compiled:

  <!-- readme-test: real-engine -->
  ```sh
  pkg update -y && pkg upgrade -y
  pkg install -y python git
  pip install git+https://github.com/lastreload/mnemonic-proxy    # 0.3.8 (about 25 s)
  mnemonic-proxy demo                                              # PASS
  ```

  Use case: an agent on the phone in front of an online API (no model on the phone), base mode:

  <!-- readme-test: real-engine -->
  ```sh
  curl -LO https://raw.githubusercontent.com/lastreload/mnemonic-proxy/main/examples/config.openai-32k.json
  mnemonic-proxy --upstream https://openrouter.ai/api --api-key "$OPENROUTER_API_KEY" \
    --port 8096 --data ./data --config config.openai-32k.json
  ```

  then point the agent at `http://127.0.0.1:8096/v1`. Measured run (OpenRouter, `meta/muse-spark-1.3-contributor`, a
  small stdlib client with 3 tools reading ten ~5K-token logs, 15 turns, history 55K tokens at the end): the proxy
  never sent more than 24K tokens; prompt tokens 353K with the proxy (all rounds, the 9 `recall` rounds included) vs
  447K for the same 15 requests sent directly (−21%; −56% counting only the 15 client turns); 12 valid tool calls,
  0 errors; the final question about the first log (masked by then) was answered right through `recall`. Prefix
  caching on the API side made the direct requests cheap, so in dollars the two were close (about 0.03–0.04 USD each).
  Limits: no saved state (online API); `--api-key` is visible in the process list of the Termux user; `check --live`
  tries the first model the API lists, so do not use `--live` against a catalogue like OpenRouter; online APIs can
  answer HTTP 429 (rate limit), which the proxy passes to the client unchanged (the client must retry). A proxy on a
  computer can also be reached from Termux with `adb reverse tcp:8096 tcp:8096` (tested with a fake engine).

## Uninstall

<!-- readme-test: illustrative -->
```sh
pip uninstall mnemonic-proxy        # inside the venv you installed it in, or delete the venv
rm -rf ./data                       # the archive, the journal: your conversations in plaintext
rm -rf ./slots                      # saved engine state (large files), and kv-archive/ if you used kv_archive
```

`./data` and `./slots` are separate on purpose: deleting the state files keeps the archive (recall still works, only
resuming without re-reading is lost); deleting `./data` loses the archive and the conversations' state becomes
unreachable. Undo the client changes as well (pi `models.json`/`settings.json`, the Claude Code variables, the Codex
provider).

## One session, measured

A real coding session — a canvas tower-defense game built from scratch by Qwen3.8 Flash Next (IQ3_XXS) on a single 12 GB
RTX 4070 Ti — with the proxy in between.

<p align="center">
  <img src="https://raw.githubusercontent.com/lastreload/mnemonic-proxy/main/docs/assets/replay.gif" alt="Replay: a question answered from three hours earlier via one recall call" width="100%">
</p>

<p align="center"><sub>Replay of a real exchange (animated GIF; <a href="https://raw.githubusercontent.com/lastreload/mnemonic-proxy/main/docs/assets/replay.mp4">MP4</a>).
Three hours and two segment switches into the session, one <code>recall</code> call — resolved inside the proxy in
61 ms — brings back the verbatim first version of the boss block, message 20. The recalled block is returned verbatim.</sub></p>

| | |
|---|---|
| **448K** | tokens of history archived and recallable |
| **105K** | peak tokens actually in the prompt (window: 128K) |
| **3h15** | continuous agent work · 430 requests · 0 errors |
| **1.4 s** | to resume a 110K-token conversation from disk (≈50 s re-reading it) |

<p align="center">
  <img src="https://raw.githubusercontent.com/lastreload/mnemonic-proxy/main/docs/assets/session-chart.svg" alt="Full history vs. prompt actually read, per request" width="100%">
</p>

Magenta: the full history of the session. Cyan: what the model actually reads on each request. Dashed lines: the two
segment switches (≈2 minutes each, written handoff notes). Data from the proxy journal, 5 Oct 2026.

## Benchmark: AgentLongBench with a 32K window

[AgentLongBench](https://github.com/euReKa025/AgentLongBench) (kf-c, tool_response, Count Frequency and Find
Duplicates), 25 questions per type at 64k (~74K-token history) and 128k (~150K): 100 questions, official scorer.
Qwen3.8 Flash Next IQ3_XXS on Strata 0.1.40, one RTX 4070 Ti 12 GB, seed 1. Four methods: the full history in an
81,920 / 163,840-token window, and three ways to fit it into 32,768 tokens — this proxy (0.3.5, commit
[`b8d4920`](https://github.com/lastreload/mnemonic-proxy/commit/b8d4920)), an LLM summary of at most 2,048 tokens
written by the same model, and truncation. Preregistered test: proxy vs summary, exact McNemar. With the question
clarified (one sentence saying which tool output "round N" means; answers and scorer unchanged):

| correct | full window | proxy | summary | truncation |
|---|---|---|---|---|
| 64k (/50) | 38 | **41** | 27 | 23 |
| 128k (/50) | 31 | **45** | 20 | 26 |
| both (/100) | 69 | **86** | 47 | 49 |
| repeat, both (/100) | 75 | **85** | 57 | 62 |

Proxy vs summary: 44 questions right only with the proxy, 5 only with the summary (p = 7.6e-9).
**Repeat run** (31 Oct 2026, proxy 0.3.19, same engine, model, questions, scorer and methods; 64k / 128k: full window
40 / 35, proxy 42 / 43, summary 32 / 25, truncation 32 / 30): proxy vs summary 35 / 7 (+28 points, p = 1.5e-5), vs
truncation 30 / 7 (+23, p = 0.0002), vs full window 22 / 12 (+10, p = 0.12, not significant). The proxy stayed at
85-86 while the other three methods scored 6-13 points higher than in the first run: a single run can be off by that
much, and questions from the same history are not independent. With the original,
ambiguous question every method was near chance (51 / 52 / 56 / 44; answering "0 / no" every time scores 50).
Limits: one model, one engine, one seed, 100 questions; the clarified run exists because of the first one; end to
end the proxy took a median 136 s / 286 s per question (64k / 128k) vs 70 s / 102 s for the full window, mostly
replaying the whole history through the proxy before the question.
Per-question results, logs, scripts and analysis: [mverde73/mnemonic-proxy-agentlongbench](https://huggingface.co/datasets/mverde73/mnemonic-proxy-agentlongbench).

## Recall, benchmarked

71 questions about past sessions, each with the known location of the evidence (including 8 with no answer in the
archive). Held-out split:

| | keyword search | structured recall |
|---|---|---|
| evidence found within 5 calls | 90% | 100% |
| tokens returned per question | 5,940 | 2,737 |
| "not in the archive" recognised | 1 / 4 | 4 / 4 |

The benchmark guided development, so read it as a regression suite, not an independent score. Its archives are real
private sessions and are not in this repository: `bench/` runs against your own archives (`bench/data/<name>.sqlite`)
with questions written for them. Details: [docs/dev-notes/RECALL-RESULT.md](https://github.com/lastreload/mnemonic-proxy/blob/main/docs/dev-notes/RECALL-RESULT.md)
(Italian).

## Saved state, measured

Resuming a conversation instead of re-reading it:

| case | saved | re-read |
|---|---|---|
| Strata (session-files branch), 110K tokens, RTX 4070 Ti | 1.4 s | ≈50 s |
| Strata (session-files branch), 69K tokens, after restart | 2.9 s | 33 s |
| llama-server, 8.2K tokens, CPU, Qwen3-0.6B | 1.9 s | 28.6 s |
| llama-server.exe, native Windows (CI runner), 3.2K tokens, CPU, Qwen3-0.6B | 2.3 s | 35.7 s |

Times are for restoring the conversation's context; loading the model is separate.

### Why saved state matters

A long agent conversation is expensive to rebuild: every token of it has to be processed again (prefill) before the
model can answer. Without saved state that cost is paid again each time the engine loses the conversation — after a
restart, when another client or conversation used the engine in between, and when the proxy returns to a sealed
segment. On a single 12 GB GPU that is close to a minute for 100K tokens; restoring the saved state takes a second or
two, and the state lives on disk, not in VRAM.

This is not specific to the proxy: any client that keeps long conversations on a local engine benefits.
llama-server already offers it through `--slot-save-path`. Strata has it since
[v0.1.40](https://github.com/Niko1221/Strata/releases/tag/v0.1.40) ([PR #668](https://github.com/Niko1221/Strata/pull/668)),
opt-in with `--slot-save-path`. The Strata numbers on this page were measured on our session-files build
(0.1.38 + PR #668, `8d8f664`), before the release. The proxy has since run on Strata 0.1.40 in the
[AgentLongBench benchmark](#benchmark-agentlongbench-with-a-32k-window) and the
[recall tests](#does-the-model-recall-on-its-own), but the restore times in the table above have not been
re-measured on 0.1.40; a contributor measured restore on Strata 0.1.41
([Tools](#tools-audit-the-archive-and-measure-restore)).

## Claude Code and Codex, live on Strata

0.2.0 in front of Strata (Qwen3.8 Flash Next IQ3_XXS, RTX 4070 Ti 12 GB, 128K window), with the real clients:

| | Claude Code 2.1.284 (Anthropic Messages) | Codex 0.160 (Responses) |
|---|---|---|
| session | 1 h 41 min, 9 steps, 339 requests, **0 proxy errors** | 3 steps, 20 requests |
| prompt tokens served from the engine cache | **92.6%** of 11.36M | **93.9%** of 351K |
| context | 328K virtual, at most 46K in the prompt; 14 segment switches | — |
| `recall` | 22 calls | exact: 36 tests and 8/8 error messages, word for word |

Claude Code ran on a test config with low thresholds (window 64K, masking at 36K) so that segments would switch
within the session. Found live and fixed in 0.3.0: in 3 writes out of 140 the model copied the shortened form of an
old tool argument into a file (see [What we have not proven](#what-we-have-not-proven)). Report:
[docs/dev-notes/LIVE020-RESULT.md](https://github.com/lastreload/mnemonic-proxy/blob/main/docs/dev-notes/LIVE020-RESULT.md) (Italian).

### Does the model recall on its own?

Recall only helps if the model uses it without being told. We built short scripted tasks where a value the model
needs at the end exists **only** in an old, masked tool output — not on disk, not reproducible — and the final request
never says "remember" or "earlier":

- **A** random output of a setup script (build id, p95, skipped migrations); re-running it gives different values;
- **B** a file read once, then deleted;
- **C** the old version of an overwritten config, no git, no backup;
- **D** an error from a test service that is then shut down;
- **L** a long session: the value appears in turn 0, followed by 12 heavy turns and several segment switches.

Qwen3.8 Flash Next IQ3_XXS on Strata 0.1.40, RTX 4070 Ti 12 GB, proxy 0.3.1 as released (no extra hints):

| client | episodes | right values | via `recall` the model chose to call |
|---|---|---|---|
| Claude Code 2.1.284 | A, B, C, D × 2 | 8 / 8 | 8 / 8 |
| Claude Code 2.1.284 | L: 127K virtual, 3 segment switches | 1 / 1 | yes |
| pi 0.87.1 | A, B, D | 3 / 3 | 3 / 3 |
| pi 0.87.1 | L: 231K virtual, 6 segment switches | 1 / 1 | yes (5 keyword searches) |
| omp 18.10.1 (oh-my-pi) | A, B, C, D | 4 / 4 | 4 / 4 ¹ |
| omp 18.10.1 (oh-my-pi) | L: 82K virtual, 2 segment switches | 1 / 1 | yes (6 calls) |

¹ With omp the model repeated the values in its own one-line answer in B (all three) and D (two of three), so they
stayed visible: there recall was strictly needed only for D's third value. A and C are clean.

A control with the full history in the prompt (no masking) was right in every short episode. In the long one it
re-ran the setup script and wrote the new, wrong values — the proxy run did better. Each episode was checked for the
true values in the final prompt (none were there, except the omp cases in ¹); one file per configuration was also
checked by hand.

Across 8 real sessions (4 pi, 3 Claude Code, 1 Codex; 18 journals counting 10 replays) the need is rare: 5 spontaneous
recalls against 108 after a question about the past; 30 re-reads of a masked, unchanged file (≈37K tokens; ≈46K
counting the replays); 4 edits out of 505 failed because the model
misremembered a masked file. When a file can be re-read, the model re-reads it — which is right when it has changed.

Limits: one model, one run of each long session, scaled-down thresholds (32K window) for the long sessions; Cline
not measured (it cannot resume a session headless without a Cline account). Report:
[docs/dev-notes/RECALL-NEED-RESULT.md](https://github.com/lastreload/mnemonic-proxy/blob/main/docs/dev-notes/RECALL-NEED-RESULT.md)
(Italian).

### Long context on Strata, without the proxy

16 `name=number` facts scattered in a generated Italian story, question at the end, temperature 0, two seeds, from
16K to 122K tokens of prompt: **151/160 exact, 0 wrong** — every miss is an omitted line, all at 64K and above.
Prefill stays at ~2.5K tok/s up to 122K, VRAM flat at 11.6 GB. Same report, section 4.

## User reports

Numbers measured by users on their own hardware and shared with permission. Not reproduced by us.

| | [u/Swimming-Farmer7815](https://www.reddit.com/r/Qwen_AI/comments/1x26aj9/comment/pfb7uu7/) |
|---|---|
| hardware | RTX 5060 Ti 16 GB, Xeon E5-2699 v3, 64 GB DDR4 ECC |
| engine / model | Strata, Swift-Qwen3.8-Flash-Next IQ3_XXS, 128K window |
| client | Cline, with its automatic context compaction disabled |
| session | 13 h; ~280K tokens of total history, ~77K in the last request |
| saved state | ~58K tokens restored in under 4 s (about 1 min 15 s to re-read at the measured prefill rate) |
| `recall` | 8 calls, all 8 results used by the model |

The user reports no compaction pauses during the session. All 8 recalls happened in the last two minutes of the
session, when the user asked for a summary of the day: during normal work the model never called `recall` on its
own. In our tests with Claude Code, pi and omp the model did call `recall` by itself when the value could not be re-read
from disk ([Does the model recall on its own?](#does-the-model-recall-on-its-own)); with Cline we could not test it.

**Share your numbers.** If you run the proxy on your own hardware, a report helps — especially with clients and models
we have not tested (Cline, other models). Useful: GPU/RAM, engine and model, client, session length (total
history and tokens in the last request), restore time, how many `recall` calls and whether the model made them on its
own. `data/journal.jsonl` holds most of it; check it before sharing, it contains your recall queries. Open an issue
with the [user report](https://github.com/lastreload/mnemonic-proxy/issues/new?template=user-report.md) template.

## Written about it

- [Radyz.cz](https://radyz.cz/nazory/mnemonic-proxy-agenticka-pamet-kontextove-okno/) (Czech, 25 Oct 2026):
  *"AI si nepamatuje. Jen si vede spis."* ("AI doesn't remember. It just keeps a file."). An independent review of how
  the proxy works, the session and benchmark numbers with their limits, and the privacy side. It points out that there
  is no command yet to delete a conversation; that is tracked in [#19](https://github.com/lastreload/mnemonic-proxy/issues/19).

## Engines

| client \ engine | Strata | llama-server | ds4-server | any OpenAI-compatible |
|---|---|---|---|---|
| Chat Completions (pi, omp, Hermes, Continue…) | tested · full | tested on CPU · full | tested with pi (GLM 5.3, Qwen3.8) · engine keeps its own state | base (no saved state) |
| opencode (Chat Completions) | **tested** (1 h 32 min live session, 554 requests) | experimental | experimental | experimental |
| Claude Code (Anthropic Messages) | **tested** (1 h 41 min live session) | experimental | experimental | experimental |
| Codex (Responses) | **tested** (live, exact recall) | experimental | experimental | experimental |
| MCP recall server (Claude Code, Codex, Hermes) | tested read-only on a real archive | | | |

"Tested": real client, real engine, measured; reports in `docs/dev-notes/`. "Experimental": tested end to end
against a mock engine and with short real client runs, not yet on long real sessions.

- **llama.cpp** — start `llama-server` with `--slot-save-path DIR` for saved state (masking anchor, segment saved
  before a switch, autosave/autorestore, `kv_archive`). The window comes from the server's `n_ctx` unless `window` is
  set; with `--parallel N` the proxy pins one slot (`slot_id`, default 0). Without `--slot-save-path` the proxy runs
  in base mode.
- **llama.cpp in router mode** (0.3.7, llama-server started without `-m`, models from `--models-preset` or
  `--models-dir`, loaded on demand) — detected automatically. The client's `model` picks the model; the proxy reads
  that model's n_ctx (its slot, `GET /slots?model=…`, loading the model if needed) **before** building the prompt, so
  the window always fits the model that will run it (thresholds scale with it). If the n_ctx cannot be read the
  request is refused with a clear error; it is never sent with the config window. Saved files are bound to the model
  that wrote them: a file is never restored into another model. Start every model with `--slot-save-path` (put it
  in the `[*]` section of the preset) and `parallel = 1`, and give each model a `ctx-size` of at least 16K.
  **Loading takes time** (on AI395 a 35B-A3B Q4 model took ~73 s from a USB disk, 12 s from the page cache): with
  `stream: true` the proxy sends an SSE comment (`: loading model <id>`; Anthropic API: a `ping` event) every
  `router_keepalive_s` (10 s) until the model is loaded and its n_ctx read, so a client with a read timeout does not
  give up; if the client has gone away the request is dropped before anything is generated (journal
  `router_client_gone`). **Non-stream requests get nothing until the answer: the client's timeout must be longer
  than the model's load time** (plus the answer). `router_load_timeout_s` (600) bounds the wait on the proxy side.
  **One history per conversation**: when a smaller model needs masking to fit, the masked history is what the bigger
  model gets afterwards too (it can read the masked results again with its tools; its earlier saved file no longer
  matches). The disk check before an autosave uses the bytes/token measured on the last save of the same model
  (×1.25; 20000 until the model has saved once). Tested on CPU with tiny models and on AI395 (Radeon 8060S,
  Vulkan) with Qwen3.6-35B-A3B and Gemma 4 E2B (`docs/dev-notes/ROUTER-MODE-RESULT.md`). Ready to copy:
  `examples/preset.router.example.ini` (start with `llama-server --models-preset preset.router.example.ini
  --models-max 1 --port 8095`) and `examples/config.llama-server-router.json`.
- **Strata** — works in base mode on any version. **Saved state: Strata ≥ 0.1.40**
  ([PR #668](https://github.com/Niko1221/Strata/pull/668), released in
  [v0.1.40](https://github.com/Niko1221/Strata/releases/tag/v0.1.40)), started with `--slot-save-path DIR`. Session files
  must be trusted: the hashes detect corruption, not tampering. Our measurements are from the session-files build
  (0.1.38 + PR #668, `8d8f664`); on 0.1.40 the proxy ran the AgentLongBench benchmark and the recall tests, but
  restore times were not re-measured there (see [Saved state, measured](#saved-state-measured)).
**Saved state that the engine does not support.** After a reply that means "not supported", the proxy stops
saved-state work for that model only (anchors and their one-token calls, segment seal/save, SAVE/RESTORE,
autosave/autorestore, kv_archive). Masking, the text archive, `recall` and notes keep working.

| Reply to a slot call | What the proxy does |
|---|---|
| HTTP 500 "the engine answered a session … the server ended the engine" (PolyStrata `strata-poly`) | suspended until restart or reset |
| HTTP 501 with a documented permanent text (no `--slot-save-path`, parallel requests, strata-poly on PolyStrata v0.1.45-poly.7 or later) | suspended until restart or reset |
| any other HTTP 501 | paused for 15 minutes, then one call retries |
| 404, 400, 409, 503, 507, generic 500, timeouts | not a refusal |

`GET /v1/strata/saved-state` lists the suspended models. `POST /v1/strata/saved-state/reset` with `{}` (all models)
or `{"model": "<exact id>"}` clears them; it answers `{"cleared": [...]}`, 400 for a bad body, and **403 unless the
request comes from this machine** (the proxy has no client authentication). The check looks at the direct TCP
peer: a local reverse proxy can make remote requests look local, so block this endpoint at that proxy if remote
access must be denied. After a reset the next save is sent again, so on a strata-poly model with a PolyStrata
release older than v0.1.45-poly.7 it ends the engine once more.

The proxy warns once per suspension: after a reset or a successful retry, a new refusal is reported again. The
retry after the 15-minute pause happens only when the proxy next needs saved state, so `GET` may show
`retry_after_s: 0` until then. The suspension adds no new requests to the engine's status endpoint.

**PolyStrata v0.1.45-poly.7 and later** answer a save or restore on a `strata-poly` model with HTTP 501 and keep the
engine running (VecSzn/PolyStrata#114): update with `UPDATE.bat` / `./update.sh` and restart PolyStrata. The proxy
recognises that 501 as permanent and suspends saved state for that model on the first reply. On **older PolyStrata
releases** the first SAVE to a `strata-poly` model still ends the engine (the proxy then suspends saved state for
that model); to avoid even that, set `mask_anchor`, `slot_save`, `autosave`, `autorestore`, `seal_experimental` and
`kv_archive` to `false` for that model.
  `setup.sh` and `run-strata-proxy.sh` in the repository root (a venv, then the proxy in front of a running
  Strata, `slot_dir` read from the Strata config) were contributed and are covered by unit tests; they are not yet
  tested by the maintainer on a real Strata install.

  `examples/config.example.json` is the configuration used with session files;
  `examples/config.official-strata.json` the one for Strata without `--slot-save-path` (or older than 0.1.40).
- **Generic OpenAI-compatible** (vLLM, online APIs, …) — base mode: masking, archive + `recall`, segments with
  handoff notes, 📌/🗑, streaming. No engine state, no saved files. Not tested on vLLM itself.
- **ds4-server** ([antirez/ds4](https://github.com/antirez/ds4)) — automatic detection, tool-call ids untouched, no
  duplicate saving (ds4 has `--kv-disk-dir`). Tested with pi, see below.

### ds4-server

ds4-server keeps its own state: with `--kv-disk-dir DIR` it checkpoints the KV cache to disk by text prefix and
resumes a conversation after a tool call by recognising the tool-call id (exact replay of the sampled call). So the
proxy does less than with other engines:

<!-- readme-test: real-engine -->
```sh
./ds4-server -m MODEL.gguf --ctx 65536 --port 8110 --kv-disk-dir ./kv
mnemonic-proxy --upstream http://127.0.0.1:8110 --port 8096 --data ./data --config examples/config.ds4.json
```

- Detection: `GET /v1/models` with `owned_by: "ds4.c"`; the window is taken from `context_length` (= `--ctx`).
  `engine: "ds4"` forces it.
- The proxy does not save, restore or archive engine state (`slot_save`, `mask_anchor`, `autosave`, `kv_archive`
  are turned off): ds4 does it itself.
- `mask_tool_args` is turned off: ds4 re-inserts the sampled call text by id, so shortened arguments would not
  reach the model. Set `ds4_exact_tool_replay: false` only if ds4-server runs with
  `--disable-exact-dsml-tool-replay`.
- Tool-call ids pass through unchanged in all three protocols (the id the engine generated reaches the client and
  comes back identical); internal `recall` calls keep the engine's id and are re-inserted identically next turn.
- Old reasoning is masked as usual; the last turn with tool calls keeps its reasoning.
- `checkpoint_align_tokens` (off by default): when set to ds4's checkpoint interval (by default 10240 tokens,
  `--kv-cache-continued-interval-tokens` rounded to `--kv-cache-boundary-align-tokens`), a masking block starts just
  after a multiple of it, so fewer tokens are re-read after the last disk checkpoint. Needs an exact `--tokenizer`
  to be meaningful. In one long session at 32K (below) it changed no masking decision.
- Not proven: Claude Code and Codex in front of ds4; parallel sessions (`--batched-session N`) — the proxy still
  serialises requests.

mnemonic-proxy is a separate tool, compatible with ds4-server and tested with it; it is not part of the ds4 project.

**Measured with pi** (4 tasks in one session on a 140-line `server.log`; the last one asks, without re-running
anything, for the request id and shard of the *third* error, whose output the proxy had already removed from the
prompt). Hardware: Ryzen AI Max+ 395 "Strix Halo", 128 GB unified memory, ROCm gfx1151.

| model, engine | window | tasks 1–3 | third error (rq-2290, shard 3) | `recall` | time |
|---|---|---|---|---|---|
| GLM 5.3 Flash Q2, ds4 `0aaea5a`, SSD streaming, MTP | 8K | ok | **right**, plus an invented timestamp | 5, by id + offset | 10 min 34 s |
| Qwen3.8 Flash Next Q2, ds4 local ROCm port | 8K | ok | not found; said so, invented nothing (0.2 recall budget: fixed in 0.3.0) | 5 | 6 min 05 s |
| Qwen3.8 Flash Next Q2, ds4 local ROCm port | 32K | ok | **right** (still in the prompt, no masking) | 0 | 3 min 30 s |
| same, **proxy 0.3.0**, first prompt forcing a plain `cat server.log` | 8K | ok | **right**, exact line (no invented detail) | 1 (id + query) | 7 min 07 s |

The 8K rows were measured to stress recall; since 0.3.0 the proxy refuses windows below 16K (see
[Requirements](#requirements)).
- GLM: after each `recall` ds4 read only the new tokens (614–634), never the whole prompt again: it resumes by
  tool-call id. Prompt reading 24–29 tok/s, generation ~6 tok/s — enough to verify the mechanism, too slow for work.
- Qwen3.8 at 8K: the model used `recall` correctly (by id, then by offset), but 0.2's proxy cut the 2nd–4th results
  to almost nothing (`room` < 0) and the third error, at character 6,183 of 9,282, never arrived. 0.3.0 fixes the
  two causes (see the changelog). With 0.3.0 one `recall` by id + query brought the line back (360 tokens). One
  successful live run, with a stricter first prompt: in two runs with the original prompt the model ran
  `cat server.log | grep -c ERROR` instead, never saw the lines, and said so.
- Qwen3.8 runs on a local ROCm port of ds4's Qwen path (not the ds4 release, which supports Qwen3.8 on Metal/CUDA
  only); prompt reading ~81 tok/s and generation 16–19 tok/s at 1.6K–7.8K tokens without MTP.

Reports (Italian): [DS4-GLM-RESULT.md](https://github.com/lastreload/mnemonic-proxy/blob/main/docs/dev-notes/DS4-GLM-RESULT.md),
[DS4-QWEN-COMPARE-RESULT.md](https://github.com/lastreload/mnemonic-proxy/blob/main/docs/dev-notes/DS4-QWEN-COMPARE-RESULT.md) (also Qwen3.8 quality on ds4 vs Strata),
[RECALL-8K-030-RESULT.md](https://github.com/lastreload/mnemonic-proxy/blob/main/docs/dev-notes/RECALL-8K-030-RESULT.md) (the 0.3.0 run),
[DS4-RESULT.md](https://github.com/lastreload/mnemonic-proxy/blob/main/docs/dev-notes/DS4-RESULT.md) (the adapter).

#### Long sessions on ds4: proxy vs pi's own compaction

Same hardware, ds4 `fc80bd6` (+ the local ROCm port for Qwen3.8), proxy 0.3.2, pi 1.0.3, window 32K, one run per
side. Without the proxy pi compacts by itself (`reserveTokens 8192`, `keepRecentTokens 8000`: our choice for 32K).
Every answer below is graded by tests and regexes written before the runs.

| task, model | | with proxy | pi alone |
|---|---|---|---|
| 16 steps (`farmastock`), Qwen3.8 Flash Next Q2 | steps done (2 h limit) | **16/16** in 85 min | 14/16 |
| | re-reads from token 0 | **0** | 23 |
| | tokens read by the engine | **167K** | 267K (with fewer steps) |
| | early facts recalled at the end | **5/5** | 4/5, one "I don't know" (asked after the limit) |
| 29 steps (`salepren`), same model | steps done (4 h limit) | 29/29 | 10/29 |
| | re-reads from token 0 | **1** | 38 |
| | tokens read / prefill time | **362K / 4,447 s** | 511K / 6,368 s |
| | memory probes at steps 8, 14, 20 | 17/18 | 5/6 (only st