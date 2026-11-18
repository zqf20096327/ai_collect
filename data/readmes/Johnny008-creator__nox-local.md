<div align="center">

# N Ø X · Local

**A coding agent that runs only on your machine.**

Own terminal UI · llama.cpp on Vulkan · no API keys · works offline

[![CI](https://github.com/Johnny008-creator/nox-local/actions/workflows/ci.yml/badge.svg)](https://github.com/Johnny008-creator/nox-local/actions/workflows/ci.yml)
![version](https://img.shields.io/badge/version-1.0.0--rc1-14b8a6)
![go](https://img.shields.io/badge/Go-1.27-00ADD8?logo=go&logoColor=white)
![llama.cpp](https://img.shields.io/badge/llama.cpp-Vulkan-8b5cf6)
![platform](https://img.shields.io/badge/platform-Linux%20%C2%B7%20AMD%2FIntel%2FNVIDIA-f59e0b)
![license](https://img.shields.io/badge/license-MIT-22c55e)

</div>

![The NØX-Local terminal UI: a prompt, tool calls, an inline diff and the answer](docs/assets/demo.gif)

NØX-Local is a coding agent for people who want the work to stay on their own computer. It drives llama.cpp directly, so there is no API key, no account, no per-token bill and nothing sent to a server. The whole agent loop is built around one constraint most agents ignore: **a 4B model has to be able to use it.**

---

## Why

Cloud agents stop when your quota runs out, and they see every file they read. A local model is free and private, but the agent loops written for frontier models fall apart on it: too many tools, prompts that fill the window, and tool calls the small model formats slightly wrong.

NØX-Local is that loop, rewritten for small models:

- **A short menu.** Ten built-in tools with short descriptions (Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch, Artifact, TodoWrite), so a 4B model picks the right one.
- **A context that lasts.** Files are read 300 lines at a time, tool output is trimmed and old results are dropped first. A 32K window goes a long way.
- **Forgiving parsing.** When the model writes a tool call as plain text instead of making one, the call is recovered and run.
- **No runaway loops.** A third identical call is blocked and the model is told to try something else.
- **MCP is opt-in.** You switch on the servers you need; the model never sees forty tools it cannot handle.

The numbers on the reference machine (RX 6500 XT 8 GB, Ryzen 5 5600GT, 16 GB DDR4) are in [docs/BENCHMARKS.md](docs/BENCHMARKS.md).

## Features

| | |
|---|---|
| **Terminal UI** | Sidebar with models, context and the plan; inline diff cards; full-screen `/diff`; command palette; mouse selection; vim keys |
| **Offline** | Runs entirely on this machine. Only WebSearch and WebFetch reach the network; `/web off` removes them |
| **Approvals** | `manual` asks before every change, `plan` is read-only, `auto` asks only for risky commands, `yolo` never asks. Each approval shows the diff |
| **Undo** | A Git checkpoint before every turn. `/rewind` restores files, `/redo` puts them back, `/revert` fixes one file |
| **Context** | A meter in the sidebar. At 70 % it suggests `/compact`, which summarises the thread and continues in a fresh context |
| **Sessions** | Saved automatically, `/resume` or `-c`, `/fork` to branch a thread, `/search` across all of them |
| **Project memory** | `NOX.md` written by `/init`, loaded into every prompt |
| **MCP** | Servers from `~/.nox-local/config.toml` or a project `.mcp.json`, switched on one by one with `/mcp` |
| **Skills** | `SKILL.md` folders from `.nox/skills`, `~/.nox-local/skills` and `~/.claude/skills`. Ships with `find-skills`, `create-skill` and `visualize` |
| **Hooks** | Shell commands on prompt, after a tool, and at the end of a turn; optional auto-commit |
| **Background work** | The model can start a dev server, get the URL back, and keep working |
| **Headless** | `nox-local -p "…"` for scripts and CI, `--output json` for event streams |

## Quick start

### Requirements

- Linux with a Vulkan-capable GPU. 8 GB of VRAM is the tested target; smaller models run on less.
- Go 1.27+ if you build from source.
- About 3 GB of disk for the first model.

> No GPU? `llama-server` falls back to the CPU and NØX-Local runs, but expect a few tokens per second. The smallest model is the one to try.

### 1. Build llama.cpp with Vulkan

```sh
sudo pacman -S --needed cmake ninja vulkan-headers spirv-headers shaderc   # Arch
# Debian/Ubuntu: sudo apt install build-essential cmake ninja-build libvulkan-dev glslc

git clone --depth 1 https://github.com/ggml-org/llama.cpp ~/.nox-local/llama.cpp
cmake -S ~/.nox-local/llama.cpp -B ~/.nox-local/llama.cpp/build -G Ninja \
  -DGGML_VULKAN=ON -DCMAKE_BUILD_TYPE=Release -DLLAMA_CURL=OFF
cmake --build ~/.nox-local/llama.cpp/build --target llama-server --parallel
```

NØX-Local looks for `llama-server` in `$NOX_LLAMA_SERVER`, then `PATH`, then `~/.nox-local/llama.cpp`, then `~/.nox/llama.cpp`. If your build is somewhere else, set the variable:

```sh
export NOX_LLAMA_SERVER=/path/to/llama-server
```

### 2. Install NØX-Local

```sh
git clone https://github.com/Johnny008-creator/nox-local && cd nox-local
sh scripts/install.sh            # builds and installs to ~/.local/bin
```

Or grab the binary from [Releases](../../releases):

```sh
curl -L -o nox-local https://github.com/Johnny008-creator/nox-local/releases/latest/download/nox-local-linux-amd64
chmod +x nox-local && mv nox-local ~/.local/bin/
```

With Go 1.27+ installed, one command is enough:

```sh
go install github.com/Johnny008-creator/nox-local/cmd/nox-local@v1.0.0-rc1
```

### 3. Get a model

```sh
nox-local models                 # catalog with sizes, and what you already have
nox-local pull qwen3.5-4b        # 3.0 GB, resumes if the download is interrupted
```

Models are stored as plain GGUF files in `~/models` (change it with `NOX_MODELS`). Any llama.cpp-compatible GGUF works; the catalog only lists the ones measured here.

### 4. Run

```sh
cd ~/code/my-project
nox-local
```

Type a request. In `auto` mode the agent edits files and runs commands, and asks before anything risky. **Shift+Tab** cycles the mode, **Ctrl+O** picks another model, **Ctrl+C** twice quits.

### Check that it works

```sh
nox-local -p "which files are in this directory? use the Glob tool"
```

The answer should mention real files, and the output should include a tool call. If it answers from memory instead, the model is too small for tools — try the 9B.

## Models

Five models, measured on the reference machine: **AMD Radeon RX 6500 XT 8 GB** (Vulkan, RADV), Ryzen 5 5600GT, 16 GB DDR4, running **Omarchy 4.5** (Arch Linux). Settings are the ones NØX-Local uses: `--fit` placement, KV cache q8_0, flash attention.

| Model | File | Context | Generation | Prompt | Notes |
|---|---|---|---|---|---|
| **Qwen3.5 4B** | 3.0 GB | 64K | **32 tok/s** | 590 t/s | The default: whole model in VRAM, follows tools well, answers fast |
| **Qwen3.5 9B** | 6.1 GB | 32K | 9 tok/s | 380 t/s | Better Czech and longer reasoning; the one for real work if you can wait |
| **Ornith 1.5 9B** | 5.2 GB | 32K | **22 tok/s** | 425 t/s | A Qwen3.5 fine-tune at IQ4_XS; nearly the 9B's quality, twice the speed |
| **Nemotron 3.5 Bolt E4B** | 5.1 GB | 32K | 8 tok/s | 655 t/s | NVIDIA on a Gemma 4 base; fastest at reading long context, slow to write |
| **Underdog Saluki 27B** | 7.9 GB | 16K | 3 tok/s | ~5 t/s | 27B at IQ2: the smartest model that fits, and it feels like it. Way too slow for agent work on this GPU unless the prompts stay short |

All five run on an 8 GB card. Pick with `/model`; the conversation carries over and the model reloads on your next message. `-m <id>` starts on a specific one.

### Which one?

- **Default / small edits:** Qwen3.5 4B. It is the only one here that feels instant.
- **Real work, Czech, longer plans:** Ornith 1.5 9B — the best speed-to-quality ratio on this hardware.
- **Long files to read, short answer:** Nemotron Bolt E4B. Its prompt processing is the fastest of the five; generation is not.
- **A hard question where you can wait:** Saluki 27B. On this GPU it is a batch job, not a chat partner.

The numbers come from `llama-bench` (`-p 512 -n 128`, q8_0 KV, flash attention) on that machine, except Saluki, which does not fit on the GPU alone and was measured through `llama-server --fit`. Other GPUs work; expect different numbers. Method and older measurements: [docs/BENCHMARKS.md](docs/BENCHMARKS.md).

## Using it

Type `/` for the list, or `Ctrl+K` for the palette.

| Command | |
|---|---|
| `/model` · `/effort` | pick a model · how much it may think (`low`, `medium`, `high`) |
| `/mode` | `manual`, `plan`, `auto`, `yolo` |
| `/plan` · `/go` | plan-first: the agent plans read-only, `/go` executes the approved plan |
| `/research` | deep research: rounds of searching and reading, ending in a sourced report |
| `/btw` | side question about the work in flight; the running turn is not touched |
| `/compact` · `/handoff` | summarise into a fresh context · start a new thread from a summary |
| `/diff` · `/rewind` · `/redo` · `/revert` | see every change, undo a turn, undo the undo, fix one file |
| `/todos` · `/artifacts` | the agent's task list · documents, pages, charts and diagrams it made |
| `/web` | switch WebSearch and WebFetch off so nothing leaves the machine |
| `/mcp` · `/skills` · `/memory` · `/init` | servers · skills · which `NOX.md` files are loaded · write one |
| `/resume` · `/search` · `/export` · `/fork` | sessions |
| `/doctor` | check llama-server, models and MCP |
| `/theme` · `/plain` · `/vim` · `/keys` | looks and keys |
| `/config` · `/trust` · `/hooks` | settings, project settings, hooks |

Keys worth knowing: **Shift+Tab** mode, **Ctrl+T** effort, **Ctrl+O** model, **Esc** interrupt, **Alt+Enter** queue a message for the running turn, **Ctrl+K** palette.

### Approvals

Every change that is not a plain read asks first in `manual`, and risky commands ask in `auto`. The card shows the diff or the command, and `a` allows that tool or command for the rest of the session. Protected files (`.env`, keys, `.git/`) always ask, except in `yolo`.

## How it works

A turn is a loop: the model gets a short system prompt, the project's `NOX.md`, a compact tool menu and a trimmed tool history. It answers with text and tool calls; the tools run; the results go back in.

What makes it work on small models:

- **Ten tools, short descriptions.** A 4B model follows a menu it can read in one screen.
- **Trimming over summarising.** Tool output keeps its head and tail, files are read in 300-line chunks, and old tool results are dropped before the conversation itself.
- **Plain-text recovery.** If the model prints a tool call instead of calling it, NØX-Local parses it and runs it anyway.
- **A loop guard.** A third identical call is blocked with "try a different approach" instead of burning the context.
- **Thinking budget.** `medium` and `high` effort cap the reasoning tokens (2K and 6K), so a model cannot think for eleven thousand tokens on a one-line answer.

## MCP

Small models handle a few tools well, not forty. Servers are configured but stay off until you switch them on:

```toml
# ~/.nox-local/config.toml
[mcp.filesystem]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-filesystem", "."]
```

`/mcp` lists what is configured and toggles each server. A project's `.mcp.json` (Claude Code format) is read too, and asks for `/trust` first because it can start processes.

## Skills

A skill is a folder with a `SKILL.md` the model can read when it decides it is relevant. NØX-Local looks in `.nox/skills`, `~/.nox-local/skills` and `~/.claude/skills`, so skills you already use elsewhere show up here.

Built in: **find-skills** (search GitHub, review a skill, install it), **create-skill** (write a new one in the format small models follow), **visualize** (charts, animations, diagrams).

## Memory

`NOX.md` in the project is loaded into every prompt. `/init` writes one by reading the repository. `~/.nox-local/NOX.md` applies everywhere. `/memory` shows what is loaded.

## Configuration

`~/.nox-local/config.toml` is created with comments on first run; a project can override it in `.nox/config.toml`.

```toml
model  = "qwen3.5-4b"      # default model
mode   = "auto"            # manual | plan | auto | yolo
effort = "low"             # low | medium | high
# auto_commit = true

[[hooks]]
event   = "stop"           # prompt | post_tool | stop
command = "go build ./..."
```

| Variable | |
|---|---|
| `NOX_LLAMA_SERVER` | path to your `llama-server` |
| `NOX_MODELS` | where GGUF files live (default `~/models`) |
| `NOX_PLAIN` | set to anything for no animation |
| `NOX_SPEC` | speculative decoding for one run: `ngram-mod`, `draft-mtp`, `ngram-simple`… Off by default, see below |

## Headless

```sh
nox-local -p "summarise this repository"                 # prints the answer
nox-local -p "add a --json flag to export" --output json # event stream
nox-local -c -p "and now run the tests"                  # continue the last session
nox-local -m qwen3.5-9b --mode plan -p "how would you …"  # pick model and mode
```

Headless never blocks on a question: `auto` and `yolo` allow tool calls, `manual` and `plan` deny them. Exit code is non-zero when the turn fails, so it works in scripts and CI.

## Troubleshooting

**`llama-server not found`**
Build llama.cpp with `-DGGML_VULKAN=ON` (step 1) or point `NOX_LLAMA_SERVER` at an existing `llama-server`.

**`no model downloaded yet`**
`nox-local pull qwen3.5-4b`. If the download was interrupted, run it again; it resumes.

**The first message takes 10–20 seconds**
That is the model loading into VRAM. Later turns start immediately. `/model` reloads it.

**Generation is very slow**
Check that the model is not spilling into system RAM: `radeontop`, `nvtop` or `nvidia-smi` show the footprint. A smaller model or `/compact` fixes most cases. `RADV_PERFTEST=nogttspill` is set for you; if you use a different Vulkan driver, look for the equivalent.

**The GPU resets or the screen flickers**
VRAM ran out, usually with a browser open. Use the 4B, or lower the context.

**The model answers but never calls a tool**
Tool calls need a model with tool support. All five models in the catalog are tested with them; very small or older GGUFs are not. In `plan` mode the model also cannot run anything, by design.

**Czech output is garbled**
A 4B limitation, not a parser problem. The 9B and Ornith write Czech well; Nemotron is happiest in English.

**It keeps repeating the same call**
The loop guard blocks a third identical call and tells the model to try another approach. If it still spins, tell it what it did wrong, or give it a smaller task.

## FAQ

**Is anything sent to a server?**
No, unless the model uses `WebSearch` or `WebFetch`. Those two tools run without an approval prompt, because they are read-only. If you want a hard guarantee, `/web off` leaves them out of every turn; the model then has no network at all.

**Is there telemetry?**
No.

**Can I use Ollama or LM Studio instead of llama.cpp?**
Not directly: NØX-Local manages `llama-server` because it needs the flags, the context size and the speed settings per model. An OpenAI-compatible endpoint would need a separate provider.

**Does it work on macOS or Windows?**
The Go code builds there and the TUI is portable, but llama.cpp setup and the process handling are only tested on Linux. Treat it as Linux-first.

**NVIDIA or Intel GPU?**
Vulkan handles all three vendors. The measured profiles are for an 8 GB AMD card; other GPUs work but the numbers will differ.

**How do I uninstall it?**
Remove `~/.local/bin/nox-local`, `~/.nox-local` and the models you downloaded. Nothing else is installed.

## Status

`1.0.0-rc1`. Feature-complete and measured; it needs real-world use before 1.0.0. Bugs and rough edges go in [Issues](../../issues).

Next: **Windows** (the code already cross-compiles for it; it is untested), **NVIDIA and Intel measurements** (Vulkan covers all three vendors, but only an AMD card sits here), macOS testing, and a better first-run experience for people without a model.

## Contributing

Issues and pull requests are welcome. The one rule is the design constraint: the agent loop must stay usable by a 4B model. If a change adds a tool, a prompt section or a round trip, say what it costs a small model.

Run `go test ./...` before opening a PR.

## License

MIT © 2026 Jan Raszka. See [LICENSE](LICENSE).

---

If this saves you an API bill, or finally makes a small model usable, **a star helps other people find it**. Issues and ideas are just as welcome: [open one](https://github.com/Johnny008-creator/nox-local/issues).
