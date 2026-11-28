<p align="center">
  <img src="docs/assets/saetta-banner.gif" alt="Saetta: local coding agent" width="900">
</p>

<h3 align="center">Saetta: a local coding agent with built-in inference.</h3>
<p align="center">A coding agent for Apple Silicon Macs with the model inside it: a C port of pi that runs Qwen3.8 and Inkling 2 Mini in its own process, on its own Metal inference engine, without Python, Node or a server. <a href="https://saetta.dev">saetta.dev</a></p>

<p align="center">
  <a href="#performance"><b>Performance</b></a> · <a href="#start"><b>Start</b></a> · <a href="#models"><b>Models</b></a> · <a href="#the-agent"><b>The agent</b></a> ·
  <a href="#other-agents-and-clients">Other agents</a> · <a href="#build-from-source">Build from source</a>
</p>

<p align="center">
  <a href="https://saetta.dev"><img src="https://img.shields.io/badge/web-saetta.dev-58a6ff" alt="saetta.dev"></a>
  <a href="https://github.com/antonellof/saetta/releases/latest"><img src="https://img.shields.io/github/v/release/antonellof/saetta?label=download&color=8a3ffc" alt="Download Saetta"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-f28c28" alt="MIT license"></a>
  <img src="https://img.shields.io/badge/Apple%20Silicon-M1%20to%20M5%2C%2032%20GB%2B-111" alt="Apple Silicon M1 to M5, 32 GB or more">
</p>

Saetta Code is a C port of the [pi](https://pi.dev) coding agent with the model running in the same process: one 2.3 MB binary, no Python, no Node, no server. Its inference engine (C and hand-written Metal) is built for agent work: long shared-prefix prompts, short answers, tool calls. Any Apple Silicon Mac with 32 GB of memory or more; it picks the model that fits.

<p align="center">
  <img src="docs/assets/demo-code.gif" width="900" alt="saetta start code: the agent loads the model, writes a one-page site for a coffee roastery, checks and fixes it; the page it wrote at the end">
  <br><sub><code>saetta start code</code> writes a landing page in one HTML file, checks it and fixes what it finds (waits cut, checks at 8x).</sub>
</p>

## Performance

All on an M5 Max with 128 GB; every number is a measured run.

<p align="center"><img src="web/assets/perf/qwen.svg" width="900" alt="Qwen3.8 on an M5 Max: prompt reading Coder 1,656 to 1,927 tokens/s, full 1,738 to 1,808, 27B 940 to 787; answering full 142 and Coder 139 tokens/s on a code edit, full 85 and Coder 66 at 16K, 27B TURBO 52, 27B 4-bit 32"></p>

<p align="center"><img src="web/assets/perf/resume.svg" width="900" alt="Time to the first token with the Coder pack: 37.31 s on a cold 64K prompt, 8.24 s on a cold 16K prompt, 0.20 s on a follow-up turn"></p>

<p align="center"><img src="web/assets/perf/inkling.svg" width="900" alt="Inkling 2 Mini on an M5 Max, 4K prompt: answering at 71.5 tokens/s in Saetta with prompt lookup and 58.7 without, Strata 54.2, llama.cpp 47.3, Strata with DSpark 36.7; prompt reading Strata 2,963, Saetta 2,396, llama.cpp 685 tokens/s"></p>

<p align="center"><img src="web/assets/perf/m14.svg" width="900" alt="Prompt reading at 4K on the M1 to M4 kernels, measured on the M5 Max: 27B 152 before 0.18, 256 now, 961 with the M5's accelerators; Coder 487, 742 and 1,538"></p>

Since 0.22 Saetta reads Inkling prompts on the M5's tensor ops too, 5 times faster than before; Strata is still 19% ahead there. M1 to M4 are not measured on real hardware yet (reports welcome). Details: [Performance](docs/performance.md).

## Start

```sh
curl -fsSL https://saetta.dev/install.sh | sh    # into ~/.local/bin; later: saetta update
cd ~/src/my-project && saetta start code          # downloads the model that fits this Mac, then opens the agent
saetta download inkling && saetta start code --pack inkling     # or name a pack
```

By memory it picks `coder` (Qwen3.8-Flash-Next, 76 GB) from 96 GB, `27b-turbo` (20 GB) from 36 GB, `27b-4bit` (16 GB) from 32 GB. Inside the agent, `/model` downloads and switches packs. Needs macOS 26 or later. Docs: [saetta.dev/docs](https://saetta.dev/docs/).

## Models

| family | Mac memory | good for | packs | published scores |
|---|---|---|---|---|
| **Qwen3.8-Flash-Next** | 96 GB (`coder`), 128 GB (`full`) | the fastest here and the highest published scores; `coder` keeps the 256 of 512 experts that matter for code | `coder`, `full` | SWE-bench Verified 82.8 (full), 79.2 (Coder) |
| **Qwen3.8-27B** | 32 GB (4-bit), 48 GB (8-bit) | dense, fits a 32 GB Mac; LoRA adapters on the 8-bit pack; coding fine-tunes with a draft head that answers faster | `27b-4bit`, `27b-8bit`, fine-tunes | SWE-bench Pro 61.7, Terminal-Bench 2.1 73.0 |
| **Inkling 2 Mini** | 32 GB | Thinking Machines' 26B mixture of experts, 3.4B active per token; context up to 1M tokens where memory allows | `inkling` | SWE-bench Verified 79.2, Terminal-Bench 2.1 71.6 |

| name | weights | on disk | Mac memory | options | SWE-bench | Terminal-Bench 2.1 |
|---|---|---|---|---|---|---|
| **Qwen3.8-Flash-Next** | | | | | | |
| **`coder`** | [Flash-Next Coder](https://huggingface.co/mbrown-uno/Qwen3.8-Flash-Next-GSQ-RCO-Coder-MLX), 256 experts, mixed 4/5/6/8-bit | 76 GB | 96 GB | draft head (MTP) | Verified 79.2 ¹ | n/p |
| `full` | [Flash-Next](https://huggingface.co/mlx-community/Qwen3.8-Flash-Next-4bit-mtp), 512 experts, 4-bit | 105 GB | 128 GB | draft head (MTP) | Pro 62.5 ², Verified 82.8 ¹ | n/p |
| **Qwen3.8-27B** | | | | | | |
| **`27b-4bit`** | [Qwen3.8-27B](https://huggingface.co/mlx-community/Qwen3.8-27B-4bit), 4-bit | 16 GB | 32 GB | | Pro 61.7 ² | 73.0 ² |
| `27b-8bit` | [Qwen3.8-27B](https://huggingface.co/mlx-community/Qwen3.8-27B-8bit), 8-bit | 29 GB | 48 GB | LoRA adapters | Pro 61.7 ² | 73.0 ² |
| `27b-pi` | [pi adapter](https://huggingface.co/harness-hub/Qwen3.8-27B-pi-adapted) (LoRA, for `27b-8bit`) | 0.6 GB | | trained to drive pi | Pro hard-51 64.7 ³ | 55.8 ³ |
| **`27b-turbo`** | [TURBO Fable Cold Fusion](https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF), shorter thinking, from Q4_K_M | 20 GB | 36 GB | draft head (MTP) | n/p | n/p |
| `27b-turbo-8bit` | the same, from Q8_0 | 30 GB | 48 GB | draft head (MTP) | n/p | n/p |
| `27b-coder390` | [Coder390 EfficientThink](https://huggingface.co/nerkyor/Qwen3.8-27B-Coder390-EfficientThink-Opus5.5-GPT6Astra-Grok4.7-DSV4Pro-K3-SFT-RLOO-GGUF-NInfer), SFT and RL on code, from Q4 | 23 GB | 48 GB | draft head (MTP) | n/p | n/p |
| `27b-coder390-8bit` | the same, from Q8_0 | 31 GB | 48 GB | draft head (MTP) | n/p | n/p |
| `27b-fable5` | [Fable-5 Coding Distilled](https://huggingface.co/khazarai/Qwen3.8-27B-Fable-5-Coding-Distilled), from [imatrix Q4_K_M](https://huggingface.co/mradermacher/Qwen3.8-27B-Fable-5-Coding-Distilled-i1-GGUF) | 20 GB | 36 GB | draft head (MTP) | n/p | n/p |
| `27b-fable5-8bit` | the same, from Q8_0 | 31 GB | 48 GB | draft head (MTP) | n/p | n/p |
| `27b-qwopus` | [Qwopus3.8-27B Coder-Flash](https://huggingface.co/mlx-community/Qwopus3.8-27B-Coder-Flash-4bit), distilled from Qwen3.8-Flash-Max, 4-bit | 16 GB | 32 GB | | n/p ⁵ | n/p ⁵ |
| `27b-qwopus-8bit` | [the same](https://huggingface.co/mlx-community/Qwopus3.8-27B-Coder-Flash-8bit), 8-bit | 29 GB | 48 GB | | n/p ⁵ | n/p ⁵ |
| **Inkling 2 Mini** | | | | | | |
| `inkling` | [Inkling 2 Mini](https://huggingface.co/mlx-community/Inkling-2-Mini-4bit), dense 4-bit, experts NVFP4 / MXFP8 | 17 GB | 32 GB | prompt lookup; 1M context | Verified 79.2 ⁴ | 71.6 ⁴ |
| `inkling-dspark` | [DSpark drafter](https://huggingface.co/thinkingmachines/Inkling-2-Mini) for `inkling` | 0.6 GB | | opt-in, `SAETTA_DSPARK=1` | | |

How to run each one:

```sh
# Qwen3.8-Flash-Next (96 GB+) and Qwen3.8-27B (32 GB+)
saetta download coder && saetta start code --pack coder
saetta download 27b-4bit && saetta start code --pack 27b-4bit

# Qwen3.8-27B coding fine-tunes (converted from their GGUF on download, with a draft head)
saetta download 27b-turbo && saetta start code --pack 27b-turbo
saetta download 27b-qwopus && saetta start code --pack 27b-qwopus

# LoRA adapters on the 27B 8-bit, in the agent's own process
saetta download 27b-8bit && saetta download 27b-pi
saetta start code --pack 27b-8bit --lora-modules qwen3.8-pi=27b-pi

# Inkling 2 Mini (32 GB+), optionally with its DSpark drafter
saetta download inkling && saetta start code --pack inkling
saetta download inkling-dspark && SAETTA_DSPARK=1 saetta start code --pack inkling

# Any Qwen3.8-27B GGUF, imported into a pack (the folder holds the model's config.json and tokenizer)
saetta import my-finetune.gguf ~/Models/my-finetune && saetta start code --pack ~/Models/my-finetune

# A remote OpenAI-compatible model: add it in /model, or in ~/.pi/agent/models.json, then
saetta code --model myprovider/my-model
```

**Bold**: what `saetta download` picks by memory. The GGUF fine-tunes are converted on download ([GGUF import](docs/gguf-import.md)); LoRA adapters run in process ([LoRA](docs/lora.md)); Inkling's DSpark drafter is opt-in ([Choosing a model](docs/choosing-a-model.md)). A pack too big for this Mac is refused and the context is sized to the memory left (about 37K tokens with `27b-4bit` on 32 GB). Every model is checked layer by layer against a numpy reference built from the same weights.

<sub>SWE-bench and Terminal-Bench are the publishers' scores for the full-precision model, each with its own harness, not measured by Saetta on these packs: ¹ [ISTA-DASLab](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-Coder-GGUF) (SWE-bench Verified, xhigh reasoning; the Coder against the full model), ² [Qwen](https://huggingface.co/Qwen/Qwen3.8-27B) ([Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next); SWE-bench Pro with Claude Code, Terminal-Bench 2.1 with Terminus), ³ [harness-hub](https://huggingface.co/harness-hub/Qwen3.8-27B-pi-adapted) (the adapter under pi, SWE-bench Pro's hard 51 tasks; the base model scores 39.2 and 39.5 there). ⁴ [Thinking Machines](https://huggingface.co/thinkingmachines/Inkling-2-Mini) (SWE-bench Verified with bash only, Terminal-Bench 2.1 with pi). ⁵ [Jackrong](https://huggingface.co/Jackrong/Qwopus3.8-27B-Coder-Flash) publishes only its own local tests (an MMLU-Pro subset of 1,500 questions, 93.87; 9 of 9 runs of a 3-task coding-agent test). n/p: not published (Qwen publishes no Terminal-Bench score for Flash-Next; the fine-tunes publish none for either). Licenses: Flash-Next Qwen Community License 1.0; the others Apache-2.0. No weights are part of this repository.</sub>

## The agent

pi 1.5.2's tools, system prompt, `AGENTS.md`/`CLAUDE.md`, skills, prompt files, sessions and terminal UI, sharing pi's `~/.pi/agent` setup: each continues the other's sessions. Requests and session files match pi's byte for byte on 63 recorded scenarios, the interactive screens on 82, rpc mode on 12. Not supported: pi's TypeScript extensions, image input.

```sh
saetta code -c                          # continue this folder's last session
saetta code -p "fix the failing test"   # print mode (--mode json, --mode rpc as pi)
saetta code --subagents                 # up to 3 child agents at once
```

- **Sessions resume instantly**: the engine's state is saved with each session, so `-c`, `/resume` and `/fork` read only what is new ([Sessions](docs/sessions.md)).
- **Tool output is read while the tool runs**: a command's output goes into the conversation as it streams, so the answer starts sooner when the command ends ([Sessions](docs/sessions.md)).
- **Edits draft from the files**: the files the agent read or changed feed the engine's speculation, so an edit that copies a block of a file is written several tokens per step ([Sessions](docs/sessions.md)).
- **Interrupted runs come back**: after a crash, a kill or a closed terminal, the next start offers to resume; commands and edits that were running are never re-run without asking.
- **Parallel agents** share one loaded model ([Parallel agents](docs/parallel-agents.md)); **MCP** servers over stdio or HTTP with OAuth ([MCP](docs/mcp.md)).
- **The terminal UI** is pi's, in C, with a footer showing the branch, the last turn's time and tok/s, and the model; `/monitor` shows the engine live. All commands: [Commands](docs/commands.md).

<p align="center"><img src="web/assets/code/tools.png" width="900" alt="An edit of src/duration.ts shown as a diff, node --test with 5 tests passing, and the model's summary"></p>

Coming next: commands confined to the project by macOS's Seatbelt.

## Other agents and clients

The same engine serves Claude Code, pi and opencode over OpenAI- and Anthropic-compatible APIs:

```sh
saetta start claude                      # or: saetta start pi, saetta start opencode
saetta serve coder                       # any client: http://127.0.0.1:8080/v1 (OpenAI) or :8080 (Anthropic)
```

<p align="center">
  <img src="docs/assets/demo.gif" width="900" alt="saetta start claude: Claude Code on Saetta writes a snake game in Python, checks it, and the game runs">
  <br><sub><code>saetta start claude</code>: Claude Code on the local model writes a snake game and checks it. Real time, no cloud.</sub>
</p>

Options, endpoints and environment variables: [Server](docs/server.md), [HTTP API](docs/http-api.md), [Environment](docs/environment.md).

## Build from source

Needs full Xcode with the Metal Toolchain and Apple clang 21 or later (C23): `make`, then `make test`. See [Build from source](docs/build-from-source.md). `src/`: `code*.c` Saetta Code; `model.c` (Flash-Next), `dense.c` (27B), `inkling.c` (Inkling 2 Mini); `kernels/` Metal; `server.c`.

## License

[MIT](LICENSE). The engine adapts parts of the MIT-licensed sushi, qwental, Strata, ds4, llama.cpp and MLX; Saetta Code is a port of pi (MIT) and adapts the libraries pi builds on. Each adapted file names its source; every notice is in [LICENSE](LICENSE).
