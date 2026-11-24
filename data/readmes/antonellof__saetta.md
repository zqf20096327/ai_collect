<p align="center">
  <img src="docs/assets/saetta-banner.gif" alt="Saetta: local coding agent" width="900">
</p>

<h3 align="center">Saetta: a local coding agent with built-in inference.</h3>
<p align="center">Two families of open coding models, Qwen3.8 and Inkling 2 Mini, run inside the agent on its own inference engine, with no server in between. A 1:1 port of Pi: its tools, sessions and terminal UI. Written in C and hand-written Metal for Apple Silicon Macs, from 32 GB of memory. <a href="https://saetta.dev">saetta.dev</a></p>

<p align="center">
  <a href="#install"><b>Install</b></a> · <a href="#saetta-code"><b>Coding agent</b></a> · <a href="#other-coding-agents">Other agents</a> ·
  <a href="#models">Models</a> · <a href="#server">Server</a> · <a href="#performance">Performance</a> · <a href="#build-from-source">Build from source</a>
</p>

<p align="center">
  <a href="https://saetta.dev"><img src="https://img.shields.io/badge/web-saetta.dev-58a6ff" alt="saetta.dev"></a>
  <a href="https://github.com/antonellof/saetta/releases/latest"><img src="https://img.shields.io/github/v/release/antonellof/saetta?label=download&color=8a3ffc" alt="Download Saetta"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-f28c28" alt="MIT license"></a>
  <img src="https://img.shields.io/badge/Apple%20Silicon-M1%20to%20M5%2C%2032%20GB%2B-111" alt="Apple Silicon M1 to M5, 32 GB or more">
</p>

Saetta puts the strongest open coding models that fit on a Mac inside a coding agent. Its kernels are written for agent work: long prompts that share a prefix (20K to 200K tokens), short answers, tool calls. It picks the model that fits your Mac, downloads it and starts.

| model | from | what it is | SWE-bench |
|---|---|---|---|
| [Qwen3.8-Flash-Next](#models) | 96 GB | Qwen's mixture of experts; the `coder` pack keeps the 256 experts that matter for code. The fastest here | Verified 82.8 (full), 79.2 (Coder) |
| [Qwen3.8-27B](#models) | 32 GB | dense, 4-bit or 8-bit, with LoRA adapters and coding fine-tunes (TURBO, Coder390, Fable-5) | Pro 61.7 |
| [Inkling 2 Mini](#models) | 32 GB | Thinking Machines' 26B mixture of experts with 3.4B active per token: a small model that scores like a large one. First version in Saetta | Verified 79.2 |

Scores are the publishers', for the full-precision models ([sources](#models)).

- On an M5 Max, Flash-Next reads prompts at 1,600 to 1,950 tokens/s and answers at 66 to 85 tokens/s, with speculative decoding.
- Follow-up turns read only what is new: a second turn on a 16K conversation answers in 0.2 s.
- Saetta Code, Claude Code, pi and opencode each start with one command. OpenAI- and Anthropic-compatible APIs serve any other client.
- Every model is checked layer by layer against numpy references built from the same weights. One binary, no Python.
- Tuned and measured on an M5 Max with 128 GB, whose neural accelerators read prompts fastest. M1 to M4 read prompts with half-precision kernels of their own on their GPU cores (not yet measured on those chips: reports welcome).

## Install

```sh
curl -fsSL https://saetta.dev/install.sh | sh    # into ~/.local/bin
saetta start code        # the built-in agent: picks the model that fits this Mac, downloads it and opens it
```

To try Inkling 2 Mini (17 GB, from 32 GB of memory), name it:

```sh
saetta download inkling
saetta start code --pack inkling
```

`saetta` alone (or `saetta auto`) is a guided start: it shows this Mac's chip, memory and free disk, lists the models best first (the ones that do not fit are greyed out), downloads the one you pick, offers the built-in agent or the Claude Code, pi and opencode it finds (with the official installer for a missing one), and starts it. The same by hand:

```sh
saetta download          # the model that fits this Mac, into ~/Models, resumable, hash-checked
saetta start code        # or: saetta start claude, saetta start pi, saetta start opencode
```

`saetta download` picks by memory: `coder` (Flash-Next, 76 GB) with 96 GB or more, `27b-turbo` (Qwen3.8-27B fine-tune, 20 GB, converted from its GGUF: about 40 GB free disk while it runs) with 36 GB, `27b-4bit` (16 GB) with 32 GB. Any pack can be named instead (table below), for example `saetta download inkling` for Inkling 2 Mini (17 GB, from 32 GB) and then `saetta start code --pack inkling`. A pack that cannot run on this Mac is refused, and the context shrinks to what memory holds.

Needs an Apple Silicon Mac (M1 or later) with 32 GB of memory or more, and macOS 26 or later. Update with `saetta update`. `SAETTA_PREFIX` changes the install folder, `SAETTA_VERSION=0.17.1` pins a release, `HF_TOKEN` raises Hugging Face's limits.

The documentation is at [saetta.dev/docs](https://saetta.dev/docs/) (source in [`docs/`](docs)): the agent's commands, sessions, skills and MCP servers, the other agents, the HTTP API and every option.

## Saetta Code

<p align="center">
  <img src="docs/assets/demo-code.gif" width="900" alt="saetta start code: the agent loads the model, writes a one-page site for a coffee roastery, checks and fixes it; the page it wrote at the end">
  <br><sub><code>saetta start code</code> loads the model, writes a landing page for a coffee roastery in one HTML file, checks it and fixes what it finds; then the page as a browser shows it. The typing, the thinking and the waits are cut, the checks play at 8x.</sub>
</p>

Saetta Code is the coding agent inside the `saetta` binary. It is written in C and runs the model in its own process, with no server and no HTTP between the agent and the model. The binary is 2.3 MB and needs neither Node.js nor Python. `saetta start code` picks the model that fits this Mac, downloads it if needed and opens the agent on it.

```sh
saetta start code                       # the model inside the agent (or the running server, if one is up)
saetta code --pack coder                # the same with a chosen pack; Escape stops a turn
saetta code -c                          # continue this folder's last session (pi's too)
saetta code -p "fix the failing test"   # print mode, as pi -p
saetta code --mode json -p "..."        # pi's JSON event stream
saetta code --mode rpc                  # pi's rpc protocol: JSON commands on stdin, events on stdout
saetta code --subagents                 # a subagent tool: up to 3 child agents at once
```

Several Saetta Code sessions share one model: a `saetta start code` in another terminal uses the model the first one loaded, each session in its own conversation. `--subagents` (or `"subagents": true` in `settings.json`) lets the model hand self-contained tasks to child agents that run in parallel; it is off by default, which keeps the prompt pi's. See [Parallel agents](docs/parallel-agents.md).

### Compatible with pi

It is a port of the [pi](https://pi.dev) coding agent 1.5.2 (MIT). It has pi's tools (read, bash, edit, write; grep, find and ls with `--tools`), its system prompt, `AGENTS.md` and `CLAUDE.md` context files, skills (and `/skill:name`), prompt files and session files. It reads and writes pi's `settings.json`, `models.json`, `trust.json` and `mcp.json` in `~/.pi/agent`, so the two share one setup, and each continues the other's sessions, compacted ones included.

Its requests and session files match pi's byte for byte on 63 recorded print and JSON scenarios (tool errors, edits, truncation, sessions, compaction, retries, skills), apart from its own system prompt preamble. Its interactive screens are compared with pi's on 75 recorded scenarios, and its rpc mode with pi's, driven by pi's own rpc client, on 12. pi's TypeScript extensions and packages are not supported, and there is no image input.

### The terminal UI

The interactive view is pi's terminal UI ported to C: differential rendering, an editor with "/" commands and "@" file completion, markdown with highlighted code, tool views with word diffs for edits, bash output shown as it runs, and the model, settings, thinking and session tree selectors. On top of it come a default theme with macOS's colors (`/theme` switches to pi's themes, with a live preview), a footer like a starship prompt (the folder as `~/...`, the git branch and status, the time of the last turn, the model's full name and quantization), and a 3D lightning loader drawn inline while the model loads. The agent checks for a new release at start.

<p align="center"><img src="web/assets/code/tools.png" width="900" alt="An edit of src/duration.ts shown as a diff, node --test with 5 tests passing, and the model's summary"></p>

### Commands

| command | what it does |
|---|---|
| `/model` | switch between downloaded packs in process, download a pack from the list (its size and the free disk shown first), add or edit OpenAI-compatible models |
| `/monitor` | the engine's live stats inside the agent: speed, GPU, memory, prompt-cache reuse, speculation, recent requests |
| `/compact`, `/resume`, `/new` | compact the context, open another session, start a new one |
| `/fork`, `/clone`, `/tree` | branch from an earlier message, duplicate the session, move through its tree |
| `/name`, `/session` | name the session, show its info and stats |
| `/export`, `/import`, `/share`, `/copy` | the session as HTML or JSONL, a JSONL session back in, a secret GitHub gist, the last answer to the clipboard |
| `/settings`, `/theme`, `/thinking`, `/scoped-models`, `/hotkeys` | settings, theme, thinking level, the models Ctrl+P cycles through, keyboard shortcuts |
| `/trust`, `/reload`, `/mcp`, `/changelog` | project trust, reload skills, prompts and context files, MCP servers, release notes |

<p align="center"><img src="web/assets/code/tree.png" width="900" alt="/tree: a session with two branches from the first answer, the current one highlighted"></p>

### MCP

MCP servers come from pi's `mcp.json` (global, or `.pi/mcp.json` in a trusted project), over stdio or Streamable HTTP. Their tools are offered to the model as `mcp__server__tool`, along with tools to read the servers' resources. `/mcp` reconnects, enables or disables a server and changes its exposure; `--no-mcp` turns them all off.

### Which model it uses

By default the model runs inside the agent. It can also use a running Saetta server, or any OpenAI-compatible chat completions server listed in `models.json`; `/model` adds one. LoRA adapters need the server: `saetta start code --lora name=adapter` starts one. Next: sessions kept on disk with the engine's state, and prompts read while tools run.

<p align="center"><img src="web/assets/code/model.png" width="900" alt="/model: a saetta server model, two packs on this Mac, one greyed out as too big for its memory, and the others with their download size"></p>

## Other coding agents

```sh
saetta start claude      # Claude Code
saetta start pi          # pi
saetta start opencode    # opencode
saetta start claude -- -p "fix the failing test"   # anything after -- goes to the agent
```

<p align="center">
  <img src="docs/assets/demo.gif" width="900" alt="saetta start claude: Claude Code on Saetta writes a snake game in Python, checks it, and the game runs">
  <br><sub><code>saetta start claude</code>: Claude Code on the local model writes a snake game and checks it. Real time, no cloud.</sub>
</p>

`saetta start` joins the server on this machine or starts one, waits for the model and runs the agent pointed at it, without touching your agent configuration; the server it started stops with the last session. Several sessions share one server (up to 4 conversations, `SAETTA_CONVERSATIONS`).

| option | effect |
|---|---|
| `--pack <name or dir>` | the model (default: the first downloaded pack that fits this Mac: coder, full, then the 27B packs) |
| `--lora name=adapter` | a LoRA adapter on a 27B pack |
| `--port N`, `--ctx N` | server port (8080) and context (204800 tokens) |
| `--keep` | leave the server running when the agent exits |

<p align="center">
  <img src="docs/assets/demo-pi.gif" width="900" alt="saetta start pi: pi on Saetta writes a Mandelbrot renderer, which then draws the set in color">
  <br><sub><code>saetta start pi</code>: pi writes a Mandelbrot renderer, then it runs.</sub>
</p>

Without `saetta start`, point any agent at `http://127.0.0.1:8080/v1` (OpenAI) or `http://127.0.0.1:8080` (Anthropic), any API key: configs in [`config/`](config) ([Claude Code](docs/claude-code.md), [opencode](docs/opencode.md)).

## Models

`saetta download <name>` fetches a pack at a pinned revision into `~/Models` (or `SAETTA_MODELS`). Commands take a pack by name (`saetta serve coder`) or folder.

| name | model | on disk | Mac memory | SWE-bench | Terminal-Bench 2.1 |
|---|---|---|---|---|---|
| **Inkling 2 Mini** | | | | | |
| **`inkling`** · 3.4B active | [Inkling 2 Mini](https://huggingface.co/mlx-community/Inkling-2-Mini-4bit) (Thinking Machines), 128 experts, 8 active, dense layers 4-bit, experts NVFP4 / MXFP8; first version | 17 GB | 32 GB | Verified 79.2 ⁴ | 71.6 ⁴ |
| **Qwen3.8-Flash-Next** | | | | | |
| **`coder`** · for agents | [Flash-Next](https://huggingface.co/mbrown-uno/Qwen3.8-Flash-Next-GSQ-RCO-Coder-MLX), 256 experts pruned for code, mixed 4/5/6/8-bit | 76 GB | 96 GB | Verified 79.2 ¹ | n/p |
| `full` | [Flash-Next](https://huggingface.co/mlx-community/Qwen3.8-Flash-Next-4bit-mtp), all 512 experts, 4-bit | 105 GB | 128 GB | Pro 62.5 ², Verified 82.8 ¹ | n/p |
| **Qwen3.8-27B** | | | | | |
| `27b-8bit` · with adapters | [Qwen3.8-27B](https://huggingface.co/mlx-community/Qwen3.8-27B-8bit), dense, 8-bit | 29 GB | 48 GB | Pro 61.7 ² | 73.0 ² |
| `27b-4bit` | [Qwen3.8-27B](https://huggingface.co/mlx-community/Qwen3.8-27B-4bit), dense, 4-bit | 16 GB | 32 GB | Pro 61.7 ² | 73.0 ² |
| `27b-pi` | [the pi LoRA adapter](https://huggingface.co/harness-hub/Qwen3.8-27B-pi-adapted) for Qwen3.8-27B | 0.6 GB | | Pro hard-51 64.7 ³ | 55.8 ³ |
| **`27b-turbo`** · with MTP | [TURBO Fable Cold Fusion](https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF), a Qwen3.8-27B fine-tune with shorter thinking, from its Q4_K_M GGUF | 20 GB | 36 GB | n/p | n/p |
| `27b-turbo-8bit` · with MTP | the same, from its Q8_0 GGUF | 30 GB | 48 GB | n/p | n/p |
| `27b-coder390` · with MTP | [Coder390 EfficientThink](https://huggingface.co/nerkyor/Qwen3.8-27B-Coder390-EfficientThink-Opus5.5-GPT6Astra-Grok4.7-DSV4Pro-K3-SFT-RLOO-GGUF-NInfer), a Qwen3.8-27B fine-tune (SFT and RL on code, shorter thinking), from its Q4 LynnStyle GGUF | 23 GB | 48 GB | n/p | n/p |
| `27b-coder390-8bit` · with MTP | the same, from its Q8_0 GGUF | 31 GB | 48 GB | n/p | n/p |
| `27b-fable5` · with MTP | [Fable-5 Coding Distilled](https://huggingface.co/khazarai/Qwen3.8-27B-Fable-5-Coding-Distilled), a Qwen3.8-27B coding distill, from [mradermacher's](https://huggingface.co/mradermacher/Qwen3.8-27B-Fable-5-Coding-Distilled-i1-GGUF) imatrix Q4_K_M GGUF | 20 GB | 36 GB | n/p | n/p |
| `27b-fable5-8bit` · with MTP | the same, from its Q8_0 GGUF | 31 GB | 48 GB | n/p | n/p |

SWE-bench and Terminal-Bench are the publishers' scores for the full-precision model, each with its own harness, not measured by Saetta on these packs: ¹ [ISTA-DASLab](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-Coder-GGUF) (SWE-bench Verified, xhigh reasoning; the Coder against the full model), ² [Qwen](https://huggingface.co/Qwen/Qwen3.8-27B) ([Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next); SWE-bench Pro with Claude Code, Terminal-Bench 2.1 with Terminus), ³ [harness-hub](https://huggingface.co/harness-hub/Qwen3.8-27B-pi-adapted) (the adapter under pi, SWE-bench Pro's hard 51 tasks; the base model scores 39.2 and 39.5 there). ⁴ [Thinking Machines](https://huggingface.co/thinkingmachines/Inkling-2-Mini) (SWE-bench Verified with bash only, Terminal-Bench 2.1 with pi). n/p: not published (Qwen publishes no Terminal-Bench score for Flash-Next; the fine-tunes publish none for either).

With less memory the context is smaller: about 37K tokens with `27b-4bit` on 32 GB. `SAETTA_IGNORE_MEMORY=1` skips the memory checks.

### Inkling 2 Mini

[Inkling 2 Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini) is Thinking Machines' coding model: 26B parameters in a mixture of 128 experts, 8 used per token, so each token costs about as much as a 3.4B dense model while it scores 79.2 on SWE-bench Verified. Its 24 layers run as 48 (a block of 12 is looped three times), with sliding-window attention and its own JSON tool-call format, which Saetta translates to the OpenAI and Anthropic APIs. The MLX pack keeps Thinking Machines' NVFP4 and MXFP8 experts as published. This is a first version: no speculative decoding yet, prompts on the GPU cores rather than the M5's neural accelerators, and a follow-up turn reuses the conversation only when it appends to it.

Licenses: Flash-Next Qwen Community License 1.0; Qwen3.8-27B, the pi adapter, TURBO, Coder390, Fable-5 and Inkling 2 Mini Apache-2.0. No weights are part of this repository.

### GGUF fine-tunes of Qwen3.8-27B

`saetta download 27b-turbo` (or `27b-coder390`, `27b-fable5`) fetches the GGUF, converts it into a Saetta pack and deletes it. `saetta import <file.gguf> <folder>` does the same for any Qwen3.8-27B GGUF (llama.cpp `qwen35`; Q8_0, Q4_K, Q5_K, Q6_K, F16 or BF16 tensors), with the model's `config.json` and tokenizer files in the folder. A GGUF's MTP layer becomes the draft head: Qwen3.8-27B speculates with it as Flash-Next does (`SAETTA_MTP=0` turns it off).

### LoRA adapters

PEFT LoRA adapters run on Qwen3.8-27B at run time, with vLLM's flags. The [pi adapter](https://huggingface.co/harness-hub/Qwen3.8-27B-pi-adapted) is trained to drive the [pi](https://pi.dev) agent (its card: SWE-bench Pro hard 39.2% to 64.7% over the base model).

```sh
saetta download 27b-8bit && saetta download 27b-pi
saetta start pi --pack 27b-8bit --lora qwen3.8-pi=27b-pi                    # pi on it
saetta serve 27b-8bit --lora-modules qwen3.8-pi=27b-pi \
    --default-chat-template-kwargs '{"enable_thinking": false}'            # or any client
```

A request whose `model` is the adapter's name runs with it, any other with the base model. Supported: LoRA on attention and MLP projections, rank a multiple of 8 up to 128, rsLoRA. `SAETTA_LORA=<folder>` applies one to `saetta generate`.

## Server

```sh
SAETTA_CTX=204800 saetta serve coder     # loads in 5 to 10 s, one request at a time, Ctrl-C stops
saetta monitor | status | stop           # live view, state, stop
```

Endpoints: `POST /v1/chat/completions` (streaming, `tool_calls`, `reasoning_content`; `enable_thinking`, `reasoning_effort` in `chat_template_kwargs`), `POST /v1/messages` and `/v1/messages/count_tokens` (Anthropic), `GET /v1/models`, `GET /health`. Model ids: `qwen3.8-flash-next`, `qwen3.8-27b`, `inkling-2-mini`.

| variable | default | effect |
|---|---|---|
| `SAETTA_CTX` | 32768 | context in tokens, 1024 to 262144, rounded down to a multiple of 128 (Flash-Next about 35 KB per token, 27B 64 KB) |
| `SAETTA_SPEC` / `SAETTA_MTP` | 1 / 1 | `0` turns speculative decoding / the MTP head off |
| `SAETTA_KV_F32` | unset | f32 KV cache |
| `SAETTA_IGNORE_MEMORY` | unset | `1` loads or downloads a pack this Mac's memory is too small for, and keeps the asked context |
| `SAETTA_NO_ACCEL` | unset | `1` runs without the tensor-op (neural accelerator) kernels on an M5 (M1 to M4 never use them; `SAETTA_ACCEL=1` forces them there, for testing) |
| `SAETTA_EXPERT_CACHE_GB` | unset | experimental: keep this many GB of experts in memory, read the rest from the SSD (Flash-Next: slower than resident, same output) |

`saetta monitor` shows the server live: model state, speed, GPU load, memory, prompt cache, speculation, sessions and recent requests. `/monitor` shows the same view inside Saetta Code.

<p align="center">
  <img src="docs/assets/monitor.png" width="900" alt="saetta monitor: model state, speed, GPU load, memory, prompt cache, speculation, sessions and recent requests">
</p>

## Performance

Flash-Next on an M5 Max with 128 GB, a six-request coding-agent workload through the HTTP API, seconds (first token / total):

| request | prompt tokens | full | Coder |
|---|---:|---:|---:|
| cold 4K | 3,335 | 2.06 / 3.66 | 2.01 / 3.90 |
| cold 16K | 15,873 | 8.78 / 10.61 | 8.24 / 10.86 |
| cold 64K | 69,923 | 40.23 / 42.16 | 37.31 / 39.87 |
| turn 1 | 15,867 | 8.68 / 9.39 | 8.07 / 8.81 |
| turn 2 (reuses turn 1) | 15,951 | 0.20 / 0.87 | 0.20 / 0.79 |
| edit (tool call, 400 tokens out) | 18,243 | 10.09 / 12.91 | 9.37 / 12.25 |
| sum of totals | | 79.6 | 76.5 |

Prompts at 1,620 to 1,930 tokens/s; answers at 78 to 85 (full) and 66 to 75 (Coder) tokens/s, 142 and 139 tokens/s on the edit with speculation. Qwen3.8-27B: prompts at 940 tokens/s (4K) to 787 (64K); answers at 31 ms/token on the 4-bit pack, 19 ms/token on `27b-turbo` with its MTP head (short prompts; 25 ms/token at 16K).

Inkling 2 Mini, first build, 4K prompt: about 430 tokens/s reading and 58 tokens/s answering, without speculative decoding (not yet re-measured after its last fixes).

M1 to M4 are not measured yet. On the M5 Max forced onto their prompt kernels, the 27B reads a 4K prompt at 256 tokens/s and the Coder at 742, against 961 and 1,538 with the neural accelerators on the same prompt.

## Build from source

Needs full Xcode with the Metal Toolchain (`xcodebuild -downloadComponent MetalToolchain`) and Apple clang 21 or later (C23).

```sh
git clone https://github.com/antonellof/saetta.git && cd saetta
make                                    # ./build/bin/saetta
make test                               # unit tests (SAETTA_PACK=<pack> for real tensors)
make verify GOLDEN=<dir>/golden         # development: against reference outputs (not in this repository)
```

`src/`: `model.c` (Flash-Next), `dense.c` (27B), `inkling.c` (Inkling 2 Mini), `model_api.c` picks one per pack; `kernels/` Metal; `server.c`, `tokenizer.c`, `chat.c`, `toolcall.c`; `code*.c` Saetta Code. `saetta help` lists every command.

## License

[MIT](LICENSE). The engine adapts parts of the MIT-licensed projects sushi, qwental, Strata, ds4, llama.cpp and MLX. Saetta Code is a port of pi (MIT) and adapts parts of the libraries pi builds on (jsdiff, TypeBox, openai-node, highlight.js, marked, OpenTUI). Each adapted file names its source, and every notice is in [LICENSE](LICENSE).
