<h1 align="center">openset-llm</h1>

<p align="center"><b>Fast LLM inference on the hardware you already own. No GPU. 8 GB of RAM.</b></p>

<p align="center">First model: a 27B LLM at 17–20 tokens per second on a CPU-only machine with 8 cores and 8 GB of RAM, about 4× the next-fastest engine we tested.</p>

<p align="center">
  <a href="https://github.com/opensetlabs"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/open-set-labs-dark.svg">
    <img src="docs/open-set-labs.svg" height="44" alt="Open Set Labs">
  </picture></a>
</p>

<p align="center">
  <img alt="Licence: MIT" src="https://img.shields.io/badge/licence-MIT-blue">
  <img alt="Platform: Linux x86-64, AVX-512" src="https://img.shields.io/badge/platform-Linux%20x86--64%20%C2%B7%20AVX--512-lightgrey">
  <img alt="API: OpenAI-compatible" src="https://img.shields.io/badge/API-OpenAI--compatible-brightgreen">
  <img alt="GPU: none" src="https://img.shields.io/badge/GPU-none-black">
  <img alt="RAM: 8 GB" src="https://img.shields.io/badge/RAM-8%20GB-black">
</p>

<p align="center">
  <img src="docs/race.gif" width="820" alt="Three engines answering the same prompt side by side on one 8 vCPU / 8 GB machine; this engine finishes first.">
</p>

```sh
git clone https://github.com/opensetlabs/openset-llm && cd openset-llm && ./start
```

<p align="center"><sub>Linux (or WSL2), a CPU with AVX-512, 8 GB of RAM. The first run builds the engine and downloads the model (~7.3 GB), then opens a chat page. <a href="#quick-start">Details</a></sub></p>

An LLM is not a sealed box. It is a stack of parts you can rewrite: matmul kernels, decoding, attention, caches. People
already rewire single neurons to change what a model does; we rewired the machinery underneath to change where it runs.
Do that, and a 27B model runs on the hardware the world already owns, ordinary CPUs, not just GPUs. Search,
extraction, agents and speech then run locally with no per-token fee, and products that never paid off at API prices do.

| **17–20 tok/s** | **4.2–4.3× / 5.9–6.1×** | **5.8×** | **no loss from the speed-ups** |
|---|---|---|---|
| one user, 8 vCPU / 8 GB Ice Lake Xeon | ik_llama.cpp / PrismML's llama.cpp fork, each in its fastest setting, on the same CPU | faster agent steps than ik_llama.cpp at 16k context (paired median; 55 s vs 314 s per step) | GSM8K 39/40 and 83.1 % coding pass@1: statistically the same with and without our latest speed-ups (the ternary model itself is PrismML's) |

**It fits where a 27B model usually does not.** Everything here runs in 8 GB of system memory with no GPU at all: no
video memory, no unified memory, nothing offloaded. A standard 4-bit build of the same Qwen3.8-27B is a 16–19 GB file,
which is why models of this size are normally run on a GPU or a 24–32 GB machine. (Another 26B model can be squeezed
into 8 GB at 1 bit per weight; we measured it on the same box: [Numbers](#numbers).) Mainline llama.cpp's own packing of
this ternary model is 7.63 GB and pages from disk on the same 8 GB machine ([measured](#numbers)); the file this engine
runs is 5.95 GB.

The race above in full: [▶ 45 s video](demo/race.mp4).

**Contents:** [Quick start](#quick-start) · [Numbers](#numbers) · [Which CPUs](#which-cpus-get-the-fast-path) ·
[Memory](#memory-budget-8-gb-machine) · [What is inside](#what-is-inside) · [Several requests at once](#several-requests-at-once---multi) ·
[Run it locally](#run-it-locally) · [In the cloud](#in-the-cloud) · [Limits](#limits) · [Reproduce](#reproduce) ·
[Contributing](#contributing) · [Licence](#licence)

openset-llm is an inference engine for ordinary CPUs; more models and more hardware will follow. Today it runs
Qwen3.8-27B, as PrismML's ternary [Bonsai-2-27B](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)
(5.95 GB), on x86 CPUs with AVX-512. It is a set of new kernels and runtime patches on PrismML's llama.cpp fork, and it
serves an OpenAI-compatible API, so the clients and agents you already use work unchanged.
Its sibling, [openset-tts](https://github.com/opensetlabs/openset-tts), does the same for speech: Qwen3-TTS faster than real time on the same kind of box.

## Quick start

**To chat with it (no code).** You need a Linux PC, or Windows with WSL2, with 8 GB of RAM free for it (16 GB in the
machine is comfortable; on Windows WSL2 must be given 8 GB, see [Run it locally](#run-it-locally)) and a processor with
AVX-512: Intel Xeon Ice Lake or newer, or AMD Zen 4 or newer. Intel Core 12th gen and later do not have it and get a
much slower fallback ([check yours](#which-cpus-get-the-fast-path)). It builds from source, so it needs git, cmake and
a C++ compiler; on Ubuntu or Debian: `sudo apt install -y build-essential cmake git`.

```sh
git clone https://github.com/opensetlabs/openset-llm && cd openset-llm
./start
```

Want to check your CPU (AVX-512 fast path) and free RAM before downloading the ~7.3 GB model? Run:

```sh
./install.sh --check
```

The first run checks your machine, builds the engine and downloads the model (~7.3 GB), then opens a chat page at
http://127.0.0.1:8080. Later runs go straight to the page. Ctrl+C stops it.

The chat page is experimental, and its very first reply takes several seconds to begin. Results may vary,
and they often vary upward: a newer processor or faster memory beats the box we measured on (see the
[CPU table](#which-cpus-get-the-fast-path)).

![The chat page](docs/chat-page.png)

**For developers.** The same server speaks the OpenAI API, so existing clients and agents work unchanged.

```sh
./install.sh        # checks your CPU and RAM, builds, downloads the model from Hugging Face (~7.3 GB)
./serve             # chat at http://127.0.0.1:8080, API at /v1  (one user, fastest replies)
./serve --multi 4   # or: 4 requests at once, 2.3× the total tokens/s on short prompts
./serve --no-webui  # API only
```

```python
from openai import OpenAI   # pip install openai
client = OpenAI(base_url="http://127.0.0.1:8080/v1", api_key="unused")
print(client.chat.completions.create(model="openset-llm",
      messages=[{"role": "user", "content": "Write a haiku about cache misses."}]).choices[0].message.content)
```

## Numbers

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/speed-dark.svg">
  <img src="docs/speed.svg" width="860" alt="Bar chart of generation speed on an 8 vCPU / 8 GB Ice Lake box: this engine 17 to 19.7 tokens per second, this engine with plain decoding 9 to 10, ik_llama.cpp 4 to 4.6, PrismML's llama.cpp fork 2.7 to 3.2.">
</picture>

**17–20 tok/s decode for one user on an 8 vCPU / 8 GB Ice Lake box: 4.2–4.3× ik_llama.cpp and 5.9–6.1× PrismML's
llama.cpp fork on the same CPU**, each engine in its fastest setting: our release default (`./serve`, with speculative
decoding) against ik_llama.cpp with run-time repack (`-rtr`) and PrismML's fork, all as llama-server, same model file,
same prompts, thinking off in every engine. 24 prompts × 256 tokens on each of 2 fresh cloud boxes, greedy, ratios paired
per prompt on the same box, pooled median [95 % bootstrap CI]. We ran it twice, on different boxes: the absolute speed
moves with the box (cloud hosts differ), the ratios do not.

| 8 vCPU / 8 GB, Ice Lake Xeon (cloud VM), 48 paired prompts, run of 2026-11-11 | decode tok/s, median [95% CI] | openset-llm default ÷ this row |
|---|---|---|
| **openset-llm `./serve`** (default: speculative decoding on) | **19.67 [18.53, 20.96]** | — |
| openset-llm `./serve --no-spec` (plain decoding) | 10.01 [9.76, 10.65] | 1.92× [1.82, 2.07] |
| ik_llama.cpp `-rtr --jinja` (HEAD `c260cbd`) | 4.58 [4.56, 4.63] | **4.33× [4.10, 4.60]** |
| PrismML llama.cpp `--jinja` (HEAD `6447906`) | 3.16 [2.57, 3.77] | **6.10× [5.82, 6.51]** |

| Same benchmark, two other boxes, run of 2026-11-12 | decode tok/s, median [95% CI] | openset-llm default ÷ this row |
|---|---|---|
| **openset-llm `./serve`** | **16.99 [16.31, 18.39]** | — |
| openset-llm `./serve --no-spec` | 9.03 [8.44, 9.73] | 1.94× [1.80, 2.06] |
| ik_llama.cpp `-rtr --jinja` | 4.01 [3.90, 4.36] | **4.17× [3.76, 4.53]** |
| PrismML llama.cpp `--jinja` | 2.72 [2.49, 3.10] | **5.85× [5.51, 6.73]** |

| AMD EPYC 9354P (Zen 4), cloud container with 8 vCPU / 16 GB, 24 paired prompts, one box | decode tok/s | openset-llm default ÷ this row |
|---|---|---|
| **openset-llm `./serve`** | **21.10 [19.40, 23.14]** | — |
| ik_llama.cpp `-rtr --jinja` | 7.74 [7.59, 7.96] | **2.77× [2.56, 3.11]** |
| PrismML llama.cpp `--jinja` | 3.83 [3.73, 3.88] | **5.46× [5.06, 6.23]** |

**Long context** (one WikiText document per length, 128-token answer, same text for every engine; decode tok/s after
the prompt, median over rounds). "Earlier build" in the tables below is this engine before its attention kernel and
agent-loop resume were added; it was never published and is shown only to isolate what those two parts add:

| context | openset-llm `./serve` | earlier build `./serve` | ik_llama.cpp `-rtr` | PrismML | prompt reading, openset-llm / ik |
|---|---|---|---|---|---|
| 4k, Ice Lake 8 GB (3 rounds) | **15.8** | 10.2 | 4.37 | 2.55 | 47.8 / 22.9 tok/s |
| 16k, Ice Lake 8 GB (3 rounds; speculation off on < 12 GB) | **7.98** | 7.24 (`--no-spec`) | 3.65 | – | 41.6 / 20.3 |
| 4k, Zen 4 16 GB (3 rounds) | **16.5** | 13.2 | 7.14 | 3.70 | 40.9 / 26.2 |
| 16k, Zen 4 (3 rounds; 2 for ik_llama.cpp) | **13.4** | 2.80 (10.3 with `--no-spec`) | 5.16 | – | 34.5 / 22.6 |
| 32k, Zen 4 (1 round) | **11.3** | 1.68 | 3.88 | – | 30.0 / 22.4 |

Every engine found all 5 facts planted in the document at every length it ran.

**Agent loops:** seconds per agent step on a recorded 11-request coding-agent session (the client rewrites the end of
its prompt every step), 16k context, 64-token answers; steps 0–5 paired on the same box (earlier build on Ice Lake: `--no-spec`; PrismML on Zen 4: steps 0–1):

| per step, wall clock | openset-llm `./serve` | earlier build | ik_llama.cpp `-rtr` | PrismML |
|---|---|---|---|---|
| Ice Lake 8 GB | **55 s** | 155 s (2.8×) | 314 s (**5.8×**) | 1,230 s (23×) |
| Zen 4 16 GB | **63 s** | 184 s (2.9×) | 274 s (**4.4×**) | 716 s (9.0×) |

Over the whole session openset-llm averages 58–59 s per step against 228–261 s with `--no-resume` (3.9–4.5×), with the same
replies (11/11). It re-reads 19,101 prompt tokens over steps 1–10 instead of 96,386.

**Quality.** No measurable loss from the speed-ups: GSM8K-40 39/40 and coding pass@1 83.1 % (160 HumanEval + MBPP problems),
against 39/40 and 83.8 % for the earlier build (p = 1.0). WikiText-2 perplexity: 7.5702 vs 7.5699 (each ± 0.21, the estimate's own uncertainty).
How the ternary model compares with the full-precision one is on [PrismML's model card](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf).
Both rivals were run without speculative decoding, which is how they ship for this model: its file has no draft head
until one is grafted on, as our installer does. The tables compare what a user of each engine gets.

**Mainline llama.cpp v1.0.0** (`b1b770d`), which has speculative decoding built in, was spot-checked on the same
8 vCPU / 8 GB Ice Lake box class on 2026-11-15 (one box, one or two prompts per setting: a "does it run" check, not the
benchmark above). It reads a different packing of this model, 7.63 GB against the 5.95 GB file this engine runs, and that
does not fit comfortably in 8 GB:

| llama.cpp v1.0.0, 8 vCPU / 8 GB, `-c 2048 -np 1` | decode tok/s |
|---|---|
| plain decoding, short prompt | 3.06 |
| plain decoding, long prompt (1,355 tokens) or the default 4 slots | pages from disk; did not finish within minutes |
| its speculative decoding (`--spec-type draft-mtp`, 1.37 GB draft head) | 0.17 (76 % of drafts accepted; model + head exceed RAM) |

With more memory it will do better; we have not measured that.

**A different model in the same 8 GB: Inkling 2 Mini.** Thinking Machines' 26.4B model, in Unsloth's 1-bit GGUF
(`UD-IQ1_S`, 7.76 GB) on Unsloth's llama.cpp build (`b12588`), CPU only, on the same 8 vCPU / 8 GB Ice Lake box, back to
back with this engine (2026-11-21; one box, the 24 prompts above, 256 tokens, greedy). This compares two models as
well as two engines:

| same box, 24 prompts | decode tok/s, median [min–max] | GSM8K-40 | coding pass@1 (160 problems) | tokens per coding answer, median |
|---|---|---|---|---|
| **openset-llm `./serve`** | **20.07 [13.19–23.25]** | 39/40 | 83.1 % | 176 |
| Inkling 2 Mini `UD-IQ1_S`, the fastest CPU setting we found | 7.40 [6.42–8.59] | 39/40 | 80.0 % | 1,054 |

openset-llm decodes **2.8×** faster per prompt (2.80× [1.60–3.56]). Answer quality on these two small sets is level:
the coding difference is not statistically significant (p = 0.38). Inkling always reasons before it answers (we found
no way to switch that off), so its quality row is with its guide's sampling and a 3,072-token cap, one sample per
problem, and it spends about six times the tokens per answer. Its fastest setting needs `-t 8 --cache-ram 0
--ctx-checkpoints 1`; as its guide's command runs on a CPU it does 4.1 tok/s. The 1-bit file only just fits (it reads
about 0.5 MB from disk per token); its larger files page on 8 GB (the recommended 4-bit file: 1.2 tok/s), and with
enough memory for them it will do better: we have not measured that.

<details><summary>Plain decoding and prompt reading, every engine without speculation (same boxes)</summary>

| ratios | openset-llm `--no-spec` / ik_llama `-rtr` | openset-llm / PrismML |
|---|---|---|
| decode, llama-server, the prompts above, Ice Lake (48 paired) | 2.20× [2.15, 2.30] | — |
| decode, llama-server, Zen 4 (24 paired) | 1.89× [1.86, 1.97] | — |
| decode, llama-bench tg128, Ice Lake (3 rounds × 2 boxes) | 2.25× [2.15, 2.35] | 3.30× [2.85, 3.80] |
| prompt, llama-bench pp512, Ice Lake | 2.16× [1.87, 2.19] | 8.40× [7.49, 9.09] |
| decode tg128 / prompt pp512, Zen 4 (3 rounds) | 1.81× / 1.36× | 3.69× / 7.01× |

tg128 box medians, Ice Lake: openset-llm 9.6–10.8, ik_llama `-rtr 1` 4.4–4.7, PrismML 2.6–3.8 tok/s; pp512: 44–49, 22.5–23.4,
5.4–5.8. Draft acceptance on these prompts: 0.75.
</details>

- ik's greedy outputs differ from ours (different arithmetic after its repack), but its WikiText-2 perplexity is 7.5681 vs
  our 7.5702: both are correct (2026-10-27, earlier HEADs).
- `--multi 4`: each stream's greedy output is byte-identical to the same request alone.

## Which CPUs get the fast path

`./install.sh --check` prints the path your machine will get. The build picks it at compile time (default, `-march=native`)
or at start-up (`--portable`, one binary for all x86-64). A CPU without the fast path still runs, on the fork's own kernel.

| CPU | ISA | Path | Status |
|---|---|---|---|
| Intel Xeon Ice Lake and newer (Sapphire/Emerald/Granite Rapids) | AVX-512 VNNI + VBMI | full | **Ice Lake measured** (8 vCPU cloud VM) |
| AMD EPYC Zen 4 (9004) | AVX-512 VNNI + VBMI | full | **measured** (EPYC 9354P, cloud container with 8 vCPU / 16 GB, 24 prompts, 2026-11-11): `./serve` 21.1 tok/s = 2.77× ik_llama `-rtr`, 5.46× PrismML; plain decode 1.89× ik |
| AMD EPYC Zen 5 (9005) | AVX-512 VNNI + VBMI | full | **measured** (EPYC 9275F, 8 vCPU / 16 GB, 3 boxes, one prompt, 2026-11-06): `./serve` 35–36 tok/s, 3.0× ik_llama `-rtr`, 4.1× PrismML; plain ~22 tok/s |
| AMD Ryzen 7000 / 9000 | AVX-512 VNNI + VBMI | full | same cores as the EPYC rows |
| Intel Xeon Cascade Lake / Cooper Lake | AVX-512 VNNI, no VBMI | partial | this build decodes at 0.67–0.82× the full path (measured on Ice Lake / Zen 4 boxes) |
| Intel Skylake-SP / Skylake-X | AVX-512, no VNNI | fallback: fork's kernel | untested |
| Intel Core 12th gen and newer, most laptops | AVX2 only | fallback: fork's kernel | this build decodes 4.8–5.7× slower than the full path (measured on Ice Lake boxes) |
| ARM64 Linux (Graviton, Ampere, Raspberry Pi 5) | NEON | fallback: fork's kernel | builds; untested |
| Apple Silicon | — | not supported by `install.sh`: use PrismML's Metal build | — |

## Memory budget (8 GB machine)

| What | Size |
|---|---|
| Model file (Bonsai-2-27B PTQ1_0 + grafted MTP head) | ~6.2 GB on disk, mmapped |
| Repacked weights (built once per start, while the server loads) | ~6 GB of anonymous memory; the mmapped originals become reclaimable page cache |
| Server resident set, default settings, **4k context** | RssAnon 6.99 GiB idle, **7.22 GiB after a ~4k-token prompt**; MemAvailable **≥ 0.19 GiB** (2026-11-11) |
| `--ctx 8192` (`serve` switches to plain decoding there on < 12 GB) | RssAnon **6.45 GiB** after an 8k-token prompt; MemAvailable **0.96 GiB** (2026-11-10) |
| Peak RSS during a 512-token prefill | 7.89 GB |

- **Context: 4,096 tokens by default** on purpose: a full 4k context with speculation leaves ~0.2 GB free on an 8 GB
  machine. With `--ctx` above 4096 on a machine (or container limit) under 12 GB, `serve` turns speculation off by
  itself (above 8192 with `--kv8`): there the draft state does not fit next to the KV cache and plain decoding is faster.
  `--ctx 16384` then runs plain decoding with ~0.45 GB free (measured). With 16 GB, speculation stays on to 32k.
- **Longer context on 8 GB (experimental, opt-in):** a smaller attention cache leaves room for more context and
  keeps speculation on further. Pick one flag; none of them is exact, and `--kv6` / `--kv5` need AVX-512.

  | `./serve` flag | attention cache vs default | speculation stays on to | plain decoding to | WikiText PPL (default 7.5702) | GSM8K-40 / coding pass@1 (default 39 / 83.1 %) |
  |---|---|---|---|---|---|
  | `--kv8` (int8) | 57 % | 8k | 32k | 7.5678 | – |
  | `--kv6` (6-bit) | 38 % | 12k (10.5–11.0 tok/s at full 12k–14k prompts) | 32k (5.7 tok/s, 0.7 GB free) | 7.5713 | 39 / 83.8 % |
  | `--kv5` (5-bit) | 32 % | 16k (9.0–11.1 tok/s at a full 16k prompt, ~0.1 GB free) | 64k (3.9–4.5 tok/s, ~0.1 GB free) | 7.5729 | 39 / 83.1 % |

  Measured 2026-11-21 on 8 vCPU / 8 GB Ice Lake boxes (the only CPU class tested). A planted-facts recall test scored
  8/8 at 16k, 32k and 64k with both new formats; `--multi` and agent-loop resume give the same replies with them as
  without. `serve` refuses contexts past these limits on machines under 12 GB. At 64k expect about 50 minutes to read
  a full prompt the first time.
- `./serve` turns off llama-server's host prompt cache (`--cache-ram 0`, default 8 GiB) and keeps one context
  checkpoint (`--ctx-checkpoints 1`); the defaults OOM an 8 GB box.
- `install.sh` refuses to run below 8 GB of RAM (or a container memory limit below that), and needs ~15 GB of free disk
  while it prepares the model (6.2 GB after).

## What is inside

A patch set on PrismML's llama.cpp fork (pinned at `e3de715`), applied by `install.sh`:

- **New AVX-512 kernels for the ternary weights**, for generating and for reading prompts.
- **Speculative decoding with the model's own multi-token-prediction head** (published by unsloth, grafted on at
  install): the engine drafts a few tokens ahead and the full model checks every one.
- **A fused attention kernel** that keeps long contexts fast.
- **Several requests in one pass** (`./serve --multi N`); every stream's output is byte-identical to the same request
  served alone.
- **Agent loops resume:** when a client resends a long prompt with a changed ending, the server continues from where
  the two diverge instead of reading it all again. Replies are byte-identical.

Defaults are the fastest settings. Switches: `./serve --no-spec` (plain decoding), `--no-resume`, `--multi N`,
`--think`, `--ctx N`, and `--kv8` (experimental, opt-in: a smaller, int8 attention cache; 43 % less cache memory, which is what lets
speculation stay on at `--ctx 8192` on an 8 GB machine; not exact: WikiText PPL 7.5678 vs 7.5702) or its smaller
siblings `--kv6` / `--kv5` (6- and 5-bit; [Memory budget](#memory-budget-8-gb-machine) has the limits and numbers).

## LoRA adapters (experimental)

GGUF LoRA adapters made for Qwen3.8-27B load through llama-server's own flag, passed after `--`:

    ./serve -- --lora Qwen3.8-27B-opencode-lora-F16.gguf

The adapter is applied at run time next to the ternary weights, which stay as they are. Tested with the OpenCode
adapter ([harness-hub/Qwen3.8-27B-opencode-adapted-GGUF](https://huggingface.co/harness-hub/Qwen3.8-27B-opencode-adapted-GGUF),
319 MB) on one 8 vCPU / 8 GB Ice Lake box, 6 prompts × 128 tokens:

| | decode tok/s, median | free memory |
|---|---|---|
| `./serve` | 14.7 | 0.24 GB |
| `./serve` + adapter | 8.4 | none left (the box was out of memory) |
| `./serve --no-spec` | 8.0 | 1.25 GB |
| `./serve --no-spec` + adapter | 6.5 | 0.93 GB |

The adapter loads, changes the output and tool calls stay well-formed; speculative decoding still accepts drafts at the
same rate. On 8 GB use `--no-spec` with an adapter, or a machine with more memory. Not measured: whether an adapter
trained on the full-precision model improves this ternary build on any task.

## Several requests at once (`--multi`)

`./serve --multi N` serves N requests together: every pass over the ~6 GB of weights produces one token for each of
them. Speculation and agent-loop resume are off in this mode (speculation with it is untested); `--ctx` is per stream.

| 8 vCPU / 8 GB, Ice Lake Xeon (2026-11-11) | one stream (`--no-spec`) | `--multi 4`, four short prompts together |
|---|---|---|
| tok/s (one stream: server decode rate; `--multi`: wall clock, prompt reading included) | 9.61 | **21.96 total = 2.28×** one stream |
| context | 4,096 | 2,048 per stream (8,192 total) |
| RAM (RssAnon / MemAvailable) | 6.18 GiB / 1.25 GiB | **6.75 GiB / 0.67 GiB** |

- Each stream's greedy output is byte-identical to the same request alone (12/12).
- With ~800-token prompts the total falls to 7–10 tok/s: a newcomer's prompt is read on its own, and the other streams
  pause for those batches (that keeps outputs identical).
- 8 streams leave < 0.3 GB free on an 8 GB machine, so `serve` warns above 6.
- One user wanting the fastest single reply: plain `./serve`. Several users, agents or best-of-N
  sampling: `--multi`.

## Run it locally

**Which path will I get?** (Linux or WSL; no clone needed)

```sh
f=$(grep -m1 '^flags' /proc/cpuinfo); case "$f" in *avx512vbmi*avx512_vnni*|*avx512_vnni*avx512vbmi*) echo "fast path";; *avx512_vnni*) echo "partial fast path (AVX-512 without VBMI)";; *avx2*) echo "fallback: AVX2, runs ~5x slower";; *) echo "generic fallback: slow";; esac
```

Inside a clone, `./install.sh --check` says the same and checks your RAM.

**Linux (native build, fastest).** Needs 8 GB RAM, ~15 GB free disk while installing, and git. `install.sh` installs
cmake/ninja/compiler through apt when it can.

```sh
git clone https://github.com/opensetlabs/openset-llm && cd openset-llm && ./install.sh && ./serve
```

**Docker** (portable build: picks the best kernel for whatever CPU it lands on). Give Docker at least 8 GB of memory.

```sh
git clone https://github.com/opensetlabs/openset-llm && cd openset-llm && docker build -t openset-llm .
docker run --rm -p 127.0.0.1:8080:8080 -v openset-llm-models:/data/models openset-llm   # no authentication: this machine only
```

The first `docker run` downloads the model (~7.3 GB) into the `openset-llm-models` volume; later runs start in ~40 s.

**Windows (WSL2).** WSL2 gets half of your RAM by default, so on a 16 GB PC raise it first. In PowerShell:

```powershell
wsl --install -d Ubuntu-24.04
notepad "$env:USERPROFILE\.wslconfig"     # add the two lines below, save, then run: wsl --shutdown
```

```ini
[wsl2]
memory=10GB
```

Then, in the Ubuntu shell, run the Linux one-liner above. Clone into your Linux home (`~`), not `/mnt/c`: reading the
model through `/mnt/c` is much slower. Most laptop CPUs (Intel 12th gen and newer) get the AVX2 fallback.

**Mac.** Our fast path is x86 AVX-512 only. On Apple Silicon, use PrismML's own build of their fork with Metal
([PrismML-Eng/llama.cpp](https://github.com/PrismML-Eng/llama.cpp)), which is much faster there than any CPU path.
Intel Macs are not supported by `install.sh`.

**Test it** (any of the above):

```sh
curl http://127.0.0.1:8080/v1/chat/completions -H 'Content-Type: application/json' \
  -d '{"messages":[{"role":"user","content":"Write a haiku about cache misses."}]}'
```

## In the cloud

- **Any Linux VM or container host** with 8 vCPU / 8 GB and AVX-512: the Linux recipe or the Docker image above.
- **Prebuilt binaries:** `./install.sh --bin-url <tarball>` skips the build (tarballs come from `scripts/package.sh`).
  A tarball runs on the Linux distribution it was built on or a newer one, so build it on the oldest one you want to
  support; `install.sh` checks that it starts before it downloads the model.

## Limits

- **Hardware:** the fast path needs x86 with AVX-512 VNNI + VBMI (table above). Measured on Intel Ice Lake, AMD Zen 4
  and Zen 5. The 8 vCPU of our Ice Lake test boxes behave like 8 physical cores; a typical cloud 8 vCPU (AWS / GCP / Azure) is 4 cores, so
  expect lower absolute speed there.
- **8 GB is the floor:** 4k context by default; above 4k on < 12 GB, `serve` uses plain decoding (above 8k with `--kv8`,
  12k with `--kv6`, 16k with `--kv5`). The compact caches are experimental and were measured on one CPU class.
- **Speculation changes a reply only at near-ties:** greedy replies are byte-identical to plain decoding on 17/24 of
  the benchmark prompts and 75/128 of a broader set; task scores are the same (Numbers).
- **Speed depends on the text and the machine.** Speculative decoding gains most on text the model finds predictable
  (summaries, rewrites, code edits) and less on short open questions; the numbers above are for the benchmark prompts.
- **Resume keeps prompt states on disk.** To continue agent loops quickly, the server saves up to 8 prefix states
  (about 0.3 GB each, built from the start of your prompts) in `~/.openset-llm/state`. Delete that folder to clear
  them, or run `./serve --no-resume`.
- **The model is PrismML's ternary Bonsai-2-27B**, with thinking off by default (`./serve --think`). The server
  repacks the weights every time it starts, before it accepts requests (20–45 s on the box we measured).

## Reproduce

Most tables above come from `bench/`: box setup, both rivals built at pinned commits with the flags shown, every arm
interleaved on the same box, and one script that prints the tables. How to run it, and the few inputs we cannot
publish (the recorded agent session, the broader prompt set, the earlier build): `bench/README.md`.

## Contributing

Bug reports, measurements on other CPUs and patches are welcome: see [CONTRIBUTING.md](CONTRIBUTING.md). A report is
most useful with the output of `./install.sh --check` and the line `./serve` prints at start. For speed on your CPU,
`./bench/quick.sh --plain` prints a ready-to-paste block in about five minutes. Security issues:
[SECURITY.md](SECURITY.md). Changes per release: [CHANGELOG.md](CHANGELOG.md).

## Licence

MIT (see `LICENSE`; the ggml authors' copyright is kept). Credits and model licences in `NOTICE`: ggml/llama.cpp,
PrismML (PTQ1_0 and Bonsai-2), unsloth (MTP sidecar), Qwen (Qwen3.8-27B). The weights are Apache 2.0 and are downloaded
from Hugging Face, not redistributed here.