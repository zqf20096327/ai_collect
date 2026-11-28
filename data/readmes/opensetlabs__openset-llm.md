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
  <a href="https://github.com/opensetlabs/openset-llm/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/opensetlabs/openset-llm?label=release&color=brightgreen"></a>
  <img alt="Licence: MIT" src="https://img.shields.io/badge/licence-MIT-blue">
  <img alt="Platform: Linux x86-64, AVX-512 or AVX2" src="https://img.shields.io/badge/platform-Linux%20x86--64%20%C2%B7%20AVX--512%20or%20AVX2-lightgrey">
  <img alt="API: OpenAI-compatible" src="https://img.shields.io/badge/API-OpenAI--compatible-brightgreen">
  <img alt="GPU: none" src="https://img.shields.io/badge/GPU-none-black">
  <img alt="RAM: 8 GB" src="https://img.shields.io/badge/RAM-8%20GB-black">
</p>

<p align="center">
  <img src="docs/race.gif" width="820" alt="Three engines answering the same prompt side by side on one 8 vCPU / 8 GB machine; this engine finishes first.">
</p>

```sh
curl -fsSL https://raw.githubusercontent.com/opensetlabs/openset-llm/main/get.sh | bash
openset-llm
```

<p align="center"><sub>Linux (or WSL2), an x86-64 CPU with AVX-512 (fastest) or AVX2, 8 GB of RAM. No clone and no compiler: it installs the engine already built, downloads the model (~7.3 GB), then opens a chat page. <a href="#quick-start">Details, Docker and building from source</a></sub></p>

**New since launch** (0.3.0 to 0.3.4, [release notes](https://github.com/opensetlabs/openset-llm/releases) · [changelog](CHANGELOG.md)):

- **One command to install**, with no clone and no compiler, and `openset-llm update` to move to the next release.
- **A prebuilt engine on every release**, checked against its checksum (`./install.sh --prebuilt` in a clone).
- **A container image on every release:** `ghcr.io/opensetlabs/openset-llm`, see [Run it locally](#run-it-locally).
- **Laptops and desktops without AVX-512** (Intel Core, AMD Zen 1 to 3) run on new 256-bit kernels, 3.5× the old
  path there ([measured](#cpus-without-avx-512)).
- **25 fixes from the community** in the engine, resume from disk, the installer and the benchmark tools, plus a
  [deployment guide](docs/deployment.md) (WSL2 memory, systemd service) and a
  [smoke test](scripts/smoke-test.sh) for a running server.

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
(5.95 GB), on x86 CPUs: fastest with AVX-512, and on our 256-bit kernels where the CPU only has AVX2. It is a set of new kernels and runtime patches on PrismML's llama.cpp fork, and it
serves an OpenAI-compatible API, so the clients and agents you already use work unchanged.

## Quick start

**To chat with it (no code).** You need a Linux PC, or Windows with WSL2, with 8 GB of RAM free for it (16 GB in the
machine is comfortable; on Windows WSL2 must be given 8 GB, see [Run it locally](#run-it-locally)) and an x86-64
processor. The speeds on this page need AVX-512: Intel Xeon Ice Lake or newer, or AMD Zen 4 or newer. A CPU with AVX2
but no AVX-512 (Intel Core 12th gen and newer, older Core, AMD Zen 1 to 3) runs on our 256-bit kernels
([what was measured, and how to run it](#cpus-without-avx-512)).

**Fastest way in: one command, no clone and no compiler.** It installs the latest release with the engine already
built for it, downloads the model, and adds an `openset-llm` command (x86-64 Linux or WSL2 with glibc 2.35 or newer:
Ubuntu 22.04, Debian 12 and later). You can read the script first: [get.sh](get.sh).

```sh
curl -fsSL https://raw.githubusercontent.com/opensetlabs/openset-llm/main/get.sh | bash
openset-llm
```

Or build it from source, which works on older systems too and uses a build tuned to your CPU. This needs git, cmake
and a C++ compiler; on Ubuntu or Debian: `sudo apt install -y build-essential cmake git`.

```sh
git clone https://github.com/opensetlabs/openset-llm && cd openset-llm
./start
```

Want to check your CPU (which kernels it will get) and free RAM before downloading the ~7.3 GB model? Run:

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
or at start-up (`--portable`, one binary for all x86-64). A CPU without AVX-512 runs on the 256-bit kernels (AVX2, with
AVX-VNNI where the CPU has it); one without AVX2 still runs, on the fork's own kernel.

| CPU | ISA | Path | Status |
|---|---|---|---|
| Intel Xeon Ice Lake and newer (Sapphire/Emerald/Granite Rapids) | AVX-512 VNNI + VBMI | full | **Ice Lake measured** (8 vCPU cloud VM) |
| AMD EPYC Zen 4 (9004) | AVX-512 VNNI + VBMI | full | **measured** (EPYC 9354P, cloud container with 8 vCPU / 16 GB, 24 prompts, 2026-11-11): `./serve` 21.1 tok/s = 2.77× ik_llama `-rtr`, 5.46× PrismML; plain decode 1.89× ik |
| AMD EPYC Zen 5 (9005) | AVX-512 VNNI + VBMI | full | **measured** (EPYC 9275F, 8 vCPU / 16 GB, 3 boxes, one prompt, 2026-11-06): `./serve` 35–36 tok/s, 3.0× ik_llama `-rtr`, 4.1× PrismML; plain ~22 tok/s |
| AMD Ryzen 7000 / 9000 | AVX-512 VNNI + VBMI | full | same cores as the EPYC rows |
| Intel Xeon Cascade Lake / Cooper Lake | AVX-512 VNNI, no VBMI | partial | this build decodes at 0.67–0.82× the full path (measured on Ice Lake / Zen 4 boxes) |
| Intel Skylake-SP / Skylake-X | AVX-512, no VNNI | 256-bit kernels | starts and gives the same replies (checked with the build for this class on an Ice Lake box); speed not measured on such a CPU |
| Intel Core 12th gen and newer (Alder / Raptor / Meteor / Arrow Lake) | AVX2 + AVX-VNNI | 256-bit kernels, VNNI dot product | not measured on such a CPU; the kernels were checked bit-exact, and the engine gave the same reply, under an emulated Alder Lake |
| Intel Core before 12th gen without AVX-512, AMD Zen 1 to 3 (Ryzen 1000–5000, EPYC 7001–7003) | AVX2 | 256-bit kernels | **measured on Ice Lake server VMs with AVX-512 disabled** ([table](#cpus-without-avx-512)): 6.1–7.7 tok/s plain decoding, 3.5× the fork's own kernel on the same box, 0.7× of the AVX-512 path |
| ARM64 Linux (Graviton, Ampere, Raspberry Pi 5) | NEON | fallback: fork's kernel | builds; untested |
| Apple Silicon | — | not supported by `install.sh`: use PrismML's Metal build | — |

### CPUs without AVX-512

A CPU with AVX2 but no AVX-512 gets 256-bit kernels for the ternary weights (AVX2, and AVX-VNNI where the CPU has
it) instead of the fork's own kernel. `./install.sh` and `./install.sh --portable` pick them by themselves.

**This release also fixes a start-up bug.** In 0.2.0 and earlier, a `--portable` build could not start on a CPU
without AVX-512, and the Docker image and `--bin-url` binaries are made from that build. Found and checked under
emulated Haswell and Alder Lake CPUs.

Thank you to everyone who told us openset-llm was slow on laptops and desktops without AVX-512. This change is for you.

**How to run it.** The commands are the quick start's; on a machine with AVX2 and no AVX-512 they do this:

```sh
./install.sh --check              # prints "Path: AVX2, no AVX-512: the 256-bit kernels ..."
./install.sh                      # builds for this CPU, downloads and prepares the model
./serve                           # plain decoding: the default without AVX-512
./serve --spec                    # speculative decoding on, drafting 2 tokens ahead
./bench/quick.sh --plain --spec   # measures ./serve, ./serve --no-spec and ./serve --spec on this machine
```

To see which kernels a machine will get before cloning anything:

```sh
f=$(grep -m1 '^flags' /proc/cpuinfo); case "$f" in *avx512vbmi*avx512_vnni*|*avx512_vnni*avx512vbmi*) echo "fast path";; *avx512_vnni*) echo "partial fast path (AVX-512 without VBMI)";; *avx2*) echo "256-bit kernels (AVX2)";; *) echo "generic fallback: slow";; esac
```

**Measured on Ice Lake server VMs with AVX-512 disabled (the binary holds no AVX-512 instruction).** The engine was
built for a Haswell-class CPU and run on 4 cloud VMs with 8 vCPU / 8 GB, 3 rounds each, every engine in every
round, same model file.

| Same box, AVX2-only builds, `llama-bench`, 8 threads | plain decoding tok/s (128 tokens) | prompt reading tok/s (512 tokens) |
|---|---|---|
| **openset-llm, 256-bit kernels** | **6.1–7.7** | **14.5–17.8** |
| openset-llm before this change (the fork's own kernel) | 1.7–1.9 | 2.1–2.7 |
| ik_llama.cpp `-rtr` (`13cffc0`) | 3.9–5.0 | 14–21 |
| PrismML llama.cpp (`prism-b12178`, 2026-11-24) | 2.4–3.0 | 3.9–5.1 |
| for reference: openset-llm with AVX-512 on the same box | 8.0–9.7 | 37–49 |

Medians per box, range over the boxes. Plain decoding is 3.5× the fork's own kernel, 1.5× ik_llama.cpp and
2.2× PrismML's current fork on the same box, and 0.7× of our AVX-512 path; prompt reading is 6.7×
the fork's own kernel, level with ik_llama.cpp (0.93×) and 0.38× of the AVX-512 path.

`./serve` on this path decodes at 5.8–7.2 tok/s on the benchmark prompts (plain decoding: speculation is off by default
without AVX-512), 3.5× the same requests on the fork's own kernel. `./serve --spec` turns speculation on and drafts 2
tokens ahead there: 7.2–8.7 tok/s on the benchmark prompts, 1.27× plain decoding [1.01, 1.78]. On a broader set of 128
prompts it is 1.11× overall: 1.19–1.43× on code, JSON, maths and tool calls, and 0.91–0.99× on prose, translation and
summaries, which is why it is not the default.

Replies: greedy replies equal the AVX-512 path's (plain decoding) on 18 of the 24 benchmark prompts at 128 tokens; the other 6
part at a token where the model's two best candidates are within 0.04 nats of each other. The kernels themselves
give bit-identical results on both paths; the rest of the engine runs at 256 bits there, and near-ties can fall
the other way. WikiText-2 perplexity is 7.5689 on this path against 7.5702 on the AVX-512 path (each ± 0.21).
Memory on 8 GB: at the default 4k context the server holds 5.9 GiB after a ~3k-token prompt with 1.5 GiB still available
(the AVX-512 path with plain decoding: 6.2 and 1.2 GiB); with `--spec` 6.5 GiB and 0.9 GiB (the AVX-512 default: 7.2 and
0.2 GiB); at `--ctx 8192` 6.1 GiB and 1.3 GiB after a ~7k-token prompt. One 8 GB box, one run each.

Not measured: a CPU without AVX-512 (AMD Zen 1 to 3, Intel Core); laptop and desktop memory configurations; CPUs
with performance and efficiency cores; the AVX-VNNI kernels at speed (the test VMs do not have AVX-VNNI, so an
emulator ran them, for correctness). If you run it on such a machine, please post the block that
`./bench/quick.sh --plain --spec` prints as a "Measurement on my machine" issue.

**What is next**

- We are making this path faster.
- Measurements on real AVX2-only desktop and laptop chips come next, and we will publish the numbers here.
- Phones are the next target we are working on.

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

- **New kernels for the ternary weights**, for generating and for reading prompts: AVX-512, and 256-bit (AVX2 /
  AVX-VNNI) for CPUs without it.
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

Requests with an active adapter do not read or write the shared prefix states on disk, which belong to the base model.
Prompt reuse and checkpoints in memory still work.

## Several requests at once (`--multi`)

`./serve --multi N` serves N requests together: every pass over the ~6 GB of weights produces one token for each of
them. Speculation is off in this mode; `--ctx` is per stream. A system prompt (and tool list) that the streams share is
read once, kept on disk, and loaded by every stream that needs it.

| 8 vCPU / 8 GB, Ice Lake Xeon (2026-11-11) | one stream (`--no-spec`) | `--multi 4`, four short prompts together |
|---|---|---|
| tok/s (one stream: server decode rate; `--multi`: wall clock, prompt reading included) | 9.61 | **21.96 total = 2.28×** one stream |
| context | 4,096 | 2,048 per stream (8,192 total) |
| RAM (RssAnon / MemAvailable) | 6.18 GiB / 1.25 GiB | **6.75 GiB / 0.67 GiB** |

- Each stream's greedy output is byte-identical to the same request alone (12/12).
- With ~800-token prompts the total falls to 7–10 tok/s: a newcomer's prompt is read on its own, and the other streams
  pause for those batches (that keeps outputs identical).
- 8 streams leave < 0.3 GB free on an 8 GB machine, so `serve` warns above 6.
- **Agents that share a system prompt** (measured 2026-11-25 on 8 vCPU / 8 GB Ice Lake boxes; every agent sends a
  1.5k–3.9k-token prompt whose ending changes each step, 1.2k–1.8k tokens of it a shared system prompt + tools): the
  server reads 32 % (4 streams) or 46 % (2 streams) of the prompt tokens instead of all of them, and a step of all
  agents takes 58–71 s instead of 157–177 s with 4 streams (2.5–2.8×), 85 s instead of 168–170 s with 2 (2.0×).
  It costs no memory, and the replies are byte-identical to `--no-resume` and to each request alone (every request
  compared). The gain is the shared part: a stream still reads everything after the system prompt again.
- The single-stream server's exact resume point (one checkpoint per stream, ~150 MiB each) is off with `--multi`; it
  can be tried with `./serve --multi N -- --ctx-checkpoints 1` (experimental; 4 streams with it leave < 0.1 GB free on 8 GB).
- Speculation inside `--multi` is not offered: a first look with 2 streams on 8 GB ran at 0.4–0.7× the speed of
  `--multi 2` without it, with replies that no longer matched the request alone; with 4 streams it ran out of memory.
- One user wanting the fastest single reply: plain `./serve`. Several users, agents or best-of-N
  sampling: `--multi`.

## Run it locally

**Which path will I get?** (Linux or WSL; no clone needed)

```sh
f=$(grep -m1 '^flags' /proc/cpuinfo); case "$f" in *avx512vbmi*avx512_vnni*|*avx512_vnni*avx512vbmi*) echo "fast path";; *avx512_vnni*) echo "partial fast path (AVX-512 without VBMI)";; *avx2*) echo "256-bit kernels (AVX2)";; *) echo "generic fallback: slow";; esac
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

From release 0.3.4 on, each release also publishes this image, so you can skip the clone and the build:

```sh
docker run --rm -p 127.0.0.1:8080:8080 -v openset-llm-models:/data/models ghcr.io/opensetlabs/openset-llm
```

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
model through `/mnt/c` is much slower. Most laptop CPUs (Intel 12th gen and newer) have no AVX-512 and get the 256-bit kernels.

**Mac.** Our kernels are x86 only (AVX-512 and AVX2). On Apple Silicon, use PrismML's own build of their fork with Metal
([PrismML-Eng/llama.cpp](https://github.com/PrismML-Eng/llama.cpp)), which is much faster there than any CPU path.
Intel Macs are not supported by `install.sh`.

**Test it** (any of the above):

```sh
curl http://127.0.0.1:8080/v1/chat/completions -H 'Content-Type: application/json' \
  -d '{"messages":[{"role":"user","content":"Write a haiku about cache misses."}]}'
```

Or check the health endpoint, the model list and one reply in one go: `bash scripts/smoke-test.sh`.
To keep the server running in the background as a systemd service, see [docs/deployment.md](docs/deployment.md).

## In the cloud

- **Any Linux VM or container host** with 8 vCPU / 8 GB: the Linux recipe or the Docker image above (AVX-512 for the
  speeds on this page; AVX2-only hosts such as AMD Zen 2 / Zen 3 instances run on the 256-bit kernels).
- **Prebuilt binaries:** `./install.sh --prebuilt` fetches the engine attached to the latest release instead of
  building it (x86-64 Linux with glibc 2.35 or newer, such as Ubuntu 22.04 or Debian 12; no compiler needed). It
  checks the download against the release's `SHA256SUMS` and refuses an engine built from other patches or kernels
  than your checkout, so use it on a checkout of the latest release tag. Releases from 0.3.3 on carry one.
  `./install.sh --bin-url <tarball>` does the same with a tarball of your own (made by `scripts/package.sh`).
  A tarball runs on the Linux distribution it was built on or a newer one, so build it on the oldest one you want to
  support; `install.sh` checks that it starts before it downloads the model.

## Limits

- **Hardware:** the fast path needs x86 with AVX-512 VNNI + VBMI (table above). Measured on Intel Ice Lake, AMD Zen 4
  and Zen 5. The AVX2 path was measured on Ice Lake server VMs with AVX-512 disabled, and its AVX-VNNI variant was
  checked under an emulator ([CPUs without AVX-512](#cpus-without-avx-512)). The 8 vCPU of our Ice Lake test boxes behave like 8 physical cores; a typical cloud 8 vCPU (AWS / GCP / Azure) is 4 cores, so
  expect lower absolute speed there.
- **8 GB is the floor:** on a machine with less, the installer stops, because the model does not fit: the system
  swaps or kills the server, and no smaller model is supported yet. With 8 GB: 4k context by default; above 4k on < 12 GB, `serve` uses plain decoding (above 8k with `--kv8`,
  12k with `--kv6`, 16k with `--kv5`). The compact caches are experimental and were measured on one CPU class.
- **Speculation changes a reply only at near-ties:** greedy replies are byte-identical to plain decoding on 17/24 of
  the benchmark prompts and 75/128 of a broader set; task scores are the same (Numbers).
- **Speed depends on the text and the machine.** Speculative decoding gains most on text the model finds predictable
  (summaries, rewrites, code edits) and less on short open questions; the numbers above are for the benchmark prompts.
- **Resume keeps prompt states on disk.** To continue agent loops quickly, the server saves up to 8 prefix states
  (about 0.3 GB each, built from the start of your prompts) in `~/.openset-llm/state`. Delete that folder to clear
  them, or run `./serve --no-resume`. `--multi` uses the same folder (its states are separate from single-stream ones).
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
