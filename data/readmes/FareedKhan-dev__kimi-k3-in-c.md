<div align="center">

<h1>kimi-k3-in-c</h1>

<h3>A 2.78-trillion-parameter model. One CPU. 8 GB of RAM.</h3>

<p>Kimi K3 inference in portable C99.<br>No BLAS. No framework. No GPU.</p>

<p>
<a href="https://github.com/FareedKhan-dev/kimi-k3-in-c/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/FareedKhan-dev/kimi-k3-in-c/ci.yml?branch=main&style=flat-square&label=CI" alt="CI"></a>
<a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-blue?style=flat-square" alt="License"></a>
<a href="Makefile"><img src="https://img.shields.io/badge/C99-portable-lightgrey?style=flat-square" alt="C99"></a>
<a href="#requirements"><img src="https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey?style=flat-square" alt="Platform"></a>
<a href="CHANGELOG.md"><img src="https://img.shields.io/badge/version-1.1.0-brightgreen?style=flat-square" alt="Version"></a>
</p>

<table>
<tr>
<td align="center"><b>2.78T</b><br><sub>parameters</sub></td>
<td align="center"><b>1.56 TB</b><br><sub>checkpoint on disk</sub></td>
<td align="center"><b>8.24 GB</b><br><sub>peak RSS, measured</sub></td>
<td align="center"><b>176 KB</b><br><sub>the whole engine</sub></td>
<td align="center"><b>0</b><br><sub>GPUs</sub></td>
</tr>
</table>

<p><b>The same 2.78-trillion-parameter model, the same answer, on whatever machine you own.</b><br>More memory only buys speed:</p>

<table>
<tr>
<th align="left">the machine you have</th>
<th align="right">RAM</th>
<th align="right">time per token</th>
<th align="left">what is going on</th>
</tr>
<tr>
<td align="left">an ordinary laptop</td>
<td align="right">8 GB</td>
<td align="right"><b>26.5 s</b></td>
<td>the whole model streams off the disk on every step</td>
</tr>
<tr>
<td align="left">a high-end laptop</td>
<td align="right">32 GB</td>
<td align="right"><b>24.2 s</b></td>
<td>some of the model now sits in memory</td>
</tr>
<tr>
<td align="left">a desktop</td>
<td align="right">64 GB</td>
<td align="right"><b>19.8 s</b></td>
<td>more of it sits in memory</td>
</tr>
<tr>
<td align="left">a heavy workstation</td>
<td align="right">128 GB+</td>
<td align="right"><b>5.6 s</b></td>
<td>the model fits entirely in memory, the disk wait is gone</td>
</tr>
</table>

<sub>Same short prompt at every size, and the output is <b>byte-identical</b> from the smallest machine to the largest; only the clock changes. One machine, 124 cores, fast NVMe drive: the first three rows still read the model from disk each step, so a slower drive is slower there, while the 128 GB+ row keeps everything in memory and no longer waits on the disk. On that same machine v1.0.0 made the math per token about <b>8&times;</b> lighter, a follow-up question in a chat <b>3.9&times;</b> faster, and long prompts about <b>half</b> as costly. (A token is roughly a short word-piece; the two runnable demos below are the original captures on a slower drive, so their clock reads a little higher.) Full data in <a href="docs/data/">docs/data/</a>.</sub>

<hr>

<p>
  <img src="docs/images/patrick_pray.png" height="44" align="middle" alt="">
  <i>I am open to AI research roles and PhD positions. <a href="https://drive.google.com/file/d/1yW5xHDS6Mr9ByrkCgVve85OqF4UOPv9K/view?usp=sharing">CV</a>.</i>
</p>

<hr>

<sub>The macOS, Windows and NEON ports, chat mode, the <code>ultra</code> preset, the faster MXFP4 kernels and a long list of parser fixes came from the people below. <a href="CONTRIBUTORS.md">Who did what</a>.</sub>

<p>
<a href="https://github.com/douglasmun"><img src="https://avatars.githubusercontent.com/u/12515041?v=4&s=96" width="48" height="48" alt="douglasmun" title="douglasmun"></a>
<a href="https://github.com/cwwjacobs"><img src="https://avatars.githubusercontent.com/u/251295277?v=4&s=96" width="48" height="48" alt="cwwjacobs" title="cwwjacobs"></a>
<a href="https://github.com/mahavak"><img src="https://avatars.githubusercontent.com/u/38126162?v=4&s=96" width="48" height="48" alt="mahavak" title="mahavak"></a>
<a href="https://github.com/sulfierry"><img src="https://avatars.githubusercontent.com/u/22729945?v=4&s=96" width="48" height="48" alt="sulfierry" title="sulfierry"></a>
<a href="https://github.com/Barba2k2"><img src="https://avatars.githubusercontent.com/u/67913962?v=4&s=96" width="48" height="48" alt="Barba2k2" title="Barba2k2"></a>
<a href="https://github.com/ShaalanMarwan"><img src="https://avatars.githubusercontent.com/u/26276966?v=4&s=96" width="48" height="48" alt="ShaalanMarwan" title="ShaalanMarwan"></a>
<a href="https://github.com/TROY665"><img src="https://avatars.githubusercontent.com/u/84645104?v=4&s=96" width="48" height="48" alt="TROY665" title="TROY665"></a>
<a href="https://github.com/ysgao"><img src="https://avatars.githubusercontent.com/u/1692765?v=4&s=96" width="48" height="48" alt="ysgao" title="ysgao"></a>
<a href="https://github.com/openchat-ai"><img src="https://avatars.githubusercontent.com/u/274358245?v=4&s=96" width="48" height="48" alt="openchat-ai" title="openchat-ai"></a>
<a href="https://github.com/arafatsolok"><img src="https://avatars.githubusercontent.com/u/58647359?v=4&s=96" width="48" height="48" alt="arafatsolok" title="arafatsolok"></a>
<br>
<a href="https://github.com/genesisrevelationinc-debug"><img src="https://avatars.githubusercontent.com/u/243808510?v=4&s=96" width="48" height="48" alt="genesisrevelationinc-debug" title="genesisrevelationinc-debug"></a>
<a href="https://github.com/AuricTW"><img src="https://avatars.githubusercontent.com/u/108772778?v=4&s=96" width="48" height="48" alt="AuricTW" title="AuricTW"></a>
<a href="https://github.com/biokraft"><img src="https://avatars.githubusercontent.com/u/35855749?v=4&s=96" width="48" height="48" alt="biokraft" title="biokraft"></a>
<a href="https://github.com/cablepull"><img src="https://avatars.githubusercontent.com/u/135179737?v=4&s=96" width="48" height="48" alt="cablepull" title="cablepull"></a>
<a href="https://github.com/Avicennasis"><img src="https://avatars.githubusercontent.com/u/913872?v=4&s=96" width="48" height="48" alt="Avicennasis" title="Avicennasis"></a>
<a href="https://github.com/Deobot2"><img src="https://avatars.githubusercontent.com/u/131834087?v=4&s=96" width="48" height="48" alt="Deobot2" title="Deobot2"></a>
<a href="https://github.com/BlakeEvans22"><img src="https://avatars.githubusercontent.com/u/32441662?v=4&s=96" width="48" height="48" alt="BlakeEvans22" title="BlakeEvans22"></a>
<a href="https://github.com/FermiHart"><img src="https://avatars.githubusercontent.com/u/100219585?v=4&s=96" width="48" height="48" alt="FermiHart" title="FermiHart"></a>
<a href="https://github.com/santhoshsathish94"><img src="https://avatars.githubusercontent.com/u/11693712?v=4&s=96" width="48" height="48" alt="santhoshsathish94" title="santhoshsathish94"></a>
<a href="https://github.com/Irfanwani"><img src="https://avatars.githubusercontent.com/u/62456735?v=4&s=96" width="48" height="48" alt="Irfanwani" title="Irfanwani"></a>
</p>

</div>

<br>

```console
$ ./bin/k3 ~/k3model --trunk ~/k3trunk --preset laptop \
           --tok ~/k3model --prompt "The capital of France is" --gen 8 --incremental

--- generated text ---
 Paris.",
+            "The Eiffel
----------------------
8 tokens in 261.5 s, 32.69 s/token average
PEAK RSS for the whole run: 8.24 GB
```

Slow, and answering correctly, in 8.24 GB, from a checkpoint of 1.56 TB. This particular
batch command deliberately asks for a raw continuation. The official Kimi K3 checkpoint
is also chat-capable; use the XTML REPL below when you want answers and multi-turn history.
Give the same batch request more memory and the answer does not change, only the clock:

```console
$ ./bin/k3 ~/k3model --trunk ~/k3trunk --preset server \
           --tok ~/k3model --prompt "def fibonacci(n):" --gen 28 --incremental

--- generated text ---
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci
----------------------
28 tokens in 299.3 s, 10.69 s/token average
PEAK RSS for the whole run: 127.92 GB
```

Every figure in this document comes from the measurement output in
[`docs/data/`](docs/data/).

![A small resident working set on top, the model itself on NVMe underneath, and a few labelled pipes between them](docs/images/main_architecture_with_spongbob.png)

The dense trunk stays in memory to whatever depth you choose and streams the rest; the
1.45 TB of routed experts are never resident, and are multiplied straight out of their
packed 4-bit form. The consequence is that **the same model runs in 8 GB and in 224 GB and
produces byte-identical output at every budget between.**

Four decisions about where bytes live take it from a cluster to a laptop, and the answer
at the bottom is the same as the answer at the top:

![Four steps from a server cluster down to an ordinary laptop, with the same output at both ends](docs/images/fit_cascade.png)

[Part II](#part-ii-how-it-works) builds every box in both diagrams from scratch, one
component at a time.

---

## Contents

**[Part I: Getting started](#part-i-getting-started)**

- [Requirements](#requirements)
- [Quick start](#quick-start): clone, build and verify in about a minute, with no model
- [Full setup](#full-setup): the whole path to generated text
- [Usage](#usage)
  - [Synopsis](#synopsis)
  - [Prompt options](#prompt-options)
  - [Memory options](#memory-options)
  - [Generation options](#generation-options)
  - [Diagnostic options](#diagnostic-options)
  - [Exit codes](#exit-codes)
  - [Environment variables](#environment-variables)
  - [Worked examples](#worked-examples)
- [Choosing a preset](#choosing-a-preset)
- [Reading the run report](#reading-the-run-report)
- [Common questions](#common-questions)

**[Part II: How it works](#part-ii-how-it-works)**

- [The problem: a model that does not fit](#the-problem-a-model-that-does-not-fit)
- [The four reductions](#the-four-reductions)
- [The machine, and what it assumes](#the-machine-and-what-it-assumes)
- [The codebase](#the-codebase)
- [Three invariants](#three-invariants)
- [1. Reading a 1.56 TB checkpoint from its headers](#1-reading-a-156-tb-checkpoint-from-its-headers)
- [2. The config reader that refuses to guess](#2-the-config-reader-that-refuses-to-guess)
- [3. The tokenizer, byte for byte](#3-the-tokenizer-byte-for-byte)
- [4. Reduction one: the experts already ship at half a byte](#4-reduction-one-the-experts-already-ship-at-half-a-byte)
- [5. Kernels with a floating point contract](#5-kernels-with-a-floating-point-contract)
- [6. Reduction two: KDA, attention with a memory that never grows](#6-reduction-two-kda-attention-with-a-memory-that-never-grows)
- [7. Reduction three: MLA, one latent instead of ninety-six heads](#7-reduction-three-mla-one-latent-instead-of-ninety-six-heads)
- [8. Attention residuals: layers that look back](#8-attention-residuals-layers-that-look-back)
- [9. Picking 16 experts of 896](#9-picking-16-experts-of-896)
- [10. Packing the trunk: 93 layers, one read each](#10-packing-the-trunk-93-layers-one-read-each)
- [11. Reduction four: streaming the trunk turns a floor into a dial](#11-reduction-four-streaming-the-trunk-turns-a-floor-into-a-dial)
- [12. An LRU cache for the experts](#12-an-lru-cache-for-the-experts)
- [13. How big should that cache be? Ask the trace](#13-how-big-should-that-cache-be-ask-the-trace)

**[Part III: Validation](#part-iii-validation)**

- [The gate ladder](#the-gate-ladder)
- [A tiny oracle first](#a-tiny-oracle-first)
- [Proving it on the full checkpoint](#proving-it-on-the-full-checkpoint)
- [The first tokens](#the-first-tokens)
- [Sustained generation: text in, text out](#sustained-generation-text-in-text-out)

**[Part IV: Measurements](#part-iv-measurements)**

- [The memory ladder: 8 GB to 224 GB](#the-memory-ladder-8-gb-to-224-gb)
- [The cache that was not participating](#the-cache-that-was-not-participating)
- [Allocation beats capacity](#allocation-beats-capacity)
- [Measuring the measurement](#measuring-the-measurement)
- [Storage is the whole game](#storage-is-the-whole-game)
- [Why the trunk is not quantised](#why-the-trunk-is-not-quantised)

**[Part V: Reference](#part-v-reference)**

- [Scope](#scope)
- [Closing the ledger](#closing-the-ledger)
- [Documentation](#documentation)
- [Development](#development)
- [Star history](#star-history)
- [License](#license)

---

# Part I: Getting started

## Requirements

The gate is storage: **the checkpoint is 1.56 TB.** Everything else is ordinary.

| | | |
|---|---|---|
| **OS** | Linux, x86-64 (reference); macOS/arm64 and Windows/x86-64 also build and pass every gate | uses `O_DIRECT`, `posix_memalign`, `getrusage` -- ported for Windows via MSYS2's MinGW-w64 (see `src/io/k3_portable_io.h`) |
| **CPU** | AVX2 + FMA on x86-64, NEON on arm64 | AVX-512 unnecessary. `make portable` targets generic AVX2 on x86-64 |
| **RAM** | 8 GB and up | every preset works; more memory is faster, never different |
| **Storage** | ~1.7 TB free | 1.56 TB checkpoint + 109 GB packed trunk, ideally on fast local disk |
| **Toolchain** | GCC ≥ 9 or Clang ≥ 10 | GNU make, or CMake |
| **Python** | 3.9+ | for the download, pack and analysis tools; not for `make test` |

The tokenizer and config reader are portable C99 and build anywhere. Without a checkpoint
you can still do everything in [Quick start](#quick-start).

## Quick start

Clone, build and run the entire test suite. **No checkpoint, no network, no Python**. The
whole thing takes about a minute.

```bash
git clone https://github.com/FareedKhan-dev/kimi-k3-in-c.git
cd kimi-k3-in-c

make -j            # seconds. Seven C files, a compiler and OpenMP
make test          # under a minute
```

It ends like this, or it failed:

```
GATE 1  teacher forcing : 32/32 positions match tf_pred
        generated span  : 20/20  <- must be exact
GATE 2  greedy decode   : 20/20 generated tokens match full_ids
GATE 3  incremental    : 20/20 generated tokens match full_ids  <- KV cache + carried KDA state

VERDICT: ENGINE MATCHES THE REFERENCE EXACTLY

ALL WEIGHTLESS TESTS PASSED
```

That is the whole engine: every kernel, the streaming cache, the safetensors reader, the
config reader, the tokenizer, and an end-to-end oracle over a 13-layer model built with the
same tensor graph as the released one, checked against a PyTorch reference from fixtures
committed to the repository.

One published measurement also replays on the spot, from a trace recorded during a full
93-layer run (this one needs Python 3.9+ and numpy):

```bash
python3 tools/sim_cache.py tests/fixtures/expert_trace.bin
```

100,096 expert requests, reprinting the capacity table in
[`expert-cache-capacity.txt`](docs/data/expert-cache-capacity.txt).

## Full setup

Six steps from an empty directory to generated text. Only step 4 is slow.

`./scripts/k3-doctor.sh` can be run at any point. It checks the toolchain, sizes your RAM
to a preset, measures your storage, and prints the exact command to run next.

### Step 0. clone

```bash
git clone https://github.com/FareedKhan-dev/kimi-k3-in-c.git
cd kimi-k3-in-c
```

About 45 MB, most of it the diagrams and the test fixtures.

### Step 1. check the machine

```bash
./scripts/k3-doctor.sh
```

Takes about a minute, because it measures your disk the way the engine reads it. It exits
non-zero if the machine cannot run the model at all.

### Step 2. build

```bash
make -j
```

Seconds. The only dependencies are a C99 compiler, libm and OpenMP. CMake works too:

```bash
cmake -B build && cmake --build build -j && ctest --test-dir build
```

### Step 3. verify before downloading anything

```bash
make test
```

This is worth doing before committing to a 1.56 TB download: it proves the engine matches
its reference on a model with the same tensor graph, and it needs nothing but the
repository.

### Step 4. fetch the checkpoint

**1.56 TB, so hours rather than minutes.** Get a token from
[huggingface.co/settings/tokens](https://huggingface.co/settings/tokens):

```bash
export HF_TOKEN=hf_your_token_here          # read from the environment, never echoed
./scripts/download-model.sh ~/k3model       # resumable, re-run to continue
```

The script finishes by verifying the shard count, the exact byte total, and then every
individual per-shard size against the published figures:

```text
verifying…
  shards : 96 (expect 96)
  bytes  : 1560936091448 (expect 1560936091448)
  shards : all 96 match their published sizes individually
  RESULT : byte-exact match
```

A partial download does not fail loudly; it produces wrong tokens. Treat a `FAIL` here as
a stop. Checking per shard also turns "re-download 1.56 terabytes" into "re-download this
one 17 gigabyte file", and it catches the one case a total cannot: two shards wrong in
opposite directions by the same amount.

### Step 5. pack the trunk

```bash
./scripts/pack-trunk.sh ~/k3model ~/k3trunk
```

About four minutes, once. It rewrites the 93 dense layers into one 109 GB file where layer
*L* lives at a known offset and can be read in a single call. **This is what turns the
memory requirement into a dial.** Put the output on the fastest disk you have.

### Step 6. run

```bash
./bin/k3 ~/k3model --trunk ~/k3trunk --preset workstation \
         --tok ~/k3model --prompt "The capital of France is" --gen 8 --incremental
```

The tokenizer ships with the checkpoint, which is why `--tok` points at the model
directory.

### Where everything ends up

```
kimi-k3-in-c/    ~45 MB   source, docs, images, and bin/k3
~/k3model/      1.56 TB   96 shards · config.json · tiktoken.model · tokenizer_config.json
~/k3trunk/       109 GB   trunk.bin · trunk.json, on the fastest disk you have
```

The first token of any run loads every pinned layer from disk, about 108 GB at the
`server` preset, so it takes far longer than the steady rate. That cost is paid once per
run, not once per token.

## Usage

### Synopsis

```
k3 <model_dir> [prompt] [memory] [generation] [diagnostics]
```

`<model_dir>` is the directory holding the `.safetensors` shards. It is required for any
run, but `--help`, `--version` and `--list-presets` work without it:

```bash
./bin/k3 --help
./bin/k3 --version
./bin/k3 --list-presets
```

### Prompt options

Outside `--chat`, exactly one of these is required. Passing none, or more than one, is a
usage error (exit 2).

| flag | argument | |
|---|---|---|
| `--prompt` | `TEXT` | tokenize TEXT and run it. **Requires `--tok`.** |
| `--prompt-file` | `PATH` | tokenize the file's bytes. **Requires `--tok`.** Preferred for anything non-ASCII: the shell re-encodes `argv`, whereas a file is read verbatim |
| `--ids` | `1,2,3` | token ids directly. No tokenizer is loaded at all, so this works on a machine with no tokenizer files. The reproducible channel the tests use |

```bash
# text in
./bin/k3 ~/k3model --tok ~/k3model --prompt "The capital of France is" ...

# text in, from a file. Use this for CJK, emoji, accents
printf 'La capitale de la France est' > /tmp/p.txt
./bin/k3 ~/k3model --tok ~/k3model --prompt-file /tmp/p.txt ...

# ids in, ids out, no tokenizer needed
./bin/k3 ~/k3model --ids 1008,10484,318,15383,387 ...
```

### Memory options

| flag | argument | default | |
|---|---|---|---|
| `--preset` | `NAME` | none | `laptop` · `desktop` · `workstation` · `server` · `max`. Sets both budgets below |
| `--trunk` | `DIR` | off | the packed trunk directory from step 5. **This is what enables streaming.** Without it the trunk loads fully resident, around 113.5 GB |
| `--trunk-gb` | `X` | 16 | budget for pinned layers plus the streaming ring |
| `--cache-gb` | `X` | 64 | budget for the routed-expert LRU cache |
| `--trunk-ring` | `N` | 2 | streaming ring slots: one layer being computed on, the rest reads in flight. Each extra slot costs one slot of RAM, and the budget still wins if it does not fit |
| `--threads` | `N` | physical cores | OpenMP threads. On Linux the default is the physical core count rather than OpenMP's one thread per logical CPU, which is slower here on SMT parts. `OMP_NUM_THREADS`, if set, is respected |
| `--ultra-low-memory` | none | off | stream exact embedding rows and lm_head chunks; full recompute also reuses one recurrent-state slot. Requires `--trunk` |

The `ultra` preset selects `--ultra-low-memory` with a 2.5 GB trunk ring and a
0.31 GB expert cache. It is a proof-of-life path for 8 GB-class machines, not an
interactive-speed preset; model precision, Top-K routing and all 93 layers are unchanged.

`--preset` and the two `-gb` flags set the same two numbers, so a preset is just a
shorthand. Order matters if you mix them: a later flag wins, so
`--preset server --cache-gb 40` gives you the server trunk budget with a 40 GB cache.

> **`--preset` without `--trunk` does nothing useful.** Every preset assumes the trunk is
> streamed. Omit `--trunk` and the engine loads all 113.5 GB resident regardless of the
> budget you asked for.

### Generation options

| flag | argument | default | |
|---|---|---|---|
| `--gen` | `N` | 8 | tokens to generate. Ceiling 4096; prompts may be up to 32768 tokens. `--gen 0 --incremental --save-state PATH` runs only the prefill and saves its exact state, to warm a prefix once and resume it many times |
| `--stop-id` | `N` | off | stop as soon as the model emits id `N`; repeatable, up to 8. The released checkpoint declares two end ids that disagree (163586 in `config.json`, 163585 in `tokenizer_config.json`) and emits both, so pass both |
| `--incremental` | none | off | carry the KV cache and the recurrent state between tokens instead of re-running the whole prefix |
| `--tok` | `DIR` | none | directory holding `tiktoken.model` and `tokenizer_config.json` |

**Pass `--incremental` for any generation of length.** Without it every step re-runs the
entire prefix, which is *O(T²)*; with it, step 0 pays for the prompt and every later step
costs the same fixed amount. Both paths are gated on producing identical tokens, so this
is a pure speed choice.

### Text chat (official Kimi K3 XTML)

K3 is chat-capable. `--chat` uses the official XTML segments and tokenizer control tokens;
it does not fall back to ChatML or a handwritten generic prompt. Version one is text-only:
there are no tools, images, server, or context compaction.

```bash
./bin/k3 ~/k3model --trunk ~/k3trunk --preset desktop --tok ~/k3model \
  --chat --system "You are a helpful assistant." \
  --history my-session.jsonl --incremental
```

The REPL accepts ordinary text plus `/help`, `/reset`, and `/exit`. It prints the complete
canonical record, including `<think>…</think>` and `<response>…</response>`. When
`--history` is supplied, it writes a portable, human-readable JSONL file such as:

```json
{"role":"system","content":"You are a helpful assistant."}
{"role":"user","content":"Explain cache locality."}
{"role":"assistant","content":"…","reasoning_content":"…"}
```

Treat that file as sensitive: it can contain every user message and the complete assistant
reasoning record, which K3 requires to continue a conversation faithfully. On restart the
engine validates, re-renders, and re-prefills the transcript; it deliberately does not
serialize opaque KV, MLA, or KDA state. Within one session under `--incremental` the
state a turn built is kept, and the next turn prefills only its new tail when the
rendered transcript begins with exactly the ids that state was fed (the REPL prints how
many positions were reused); `/reset` or any other divergence starts over. A supplied `--system` must exactly match an existing
initial system record. Literal control-marker text in user messages is encoded as ordinary
text, never as an XTML control token.

Chat defaults to `--gen 4096` and, like batch generation, to greedy decoding. Passing any
of `--temperature`, `--top-p` or `--seed` turns sampling on (temperature `1.0`, top-p
`0.95` unless given); `--greedy` forces argmax even then. Sampling uses
PCG32; `--seed N` deterministically derives one stream per assistant turn, so replaying the
same transcript with the same seed is reproducible. The 32K prompt / 4096 generation limits
are existing engine limits, not new chat limits; chat fails clearly and retains the history
when either context or safe KV allocation is reached.

Thinking is on by default with `thinking_effort=max`, which is exactly what the checkpoint's
own tokenizer does when `apply_chat_template` is given nothing; `--thinking-effort low` or
`high` changes only that setting. `--no-think` is the encoder's `thinking=False`: no
thinking-effort system message, prior assistant turns rendered without a think channel, and
a generation prompt that opens the response channel directly, so the model answers at once
and the REPL prints no `<think>` block. On a streamed trunk this is the largest speed lever
there is: in a real-checkpoint run, 119 of the 150 tokens of a five-word answer were the
think block. Reasoning already stored in the transcript is left in place and is rendered
again the next time the conversation runs with thinking on. Both flags are byte- and
id-exact against the official tokenizer in `tests/unit/test_chat.c`.

Chat uses the same CPU-only streamed trunk and routed-expert cache as batch mode. `--preset`,
`--trunk-gb`, and `--cache-gb` keep exactly their existing meanings: no experts are preloaded
and the trunk remains disk-streamed unless those existing memory flags ask otherwise.

### Diagnostic options

| flag | argument | |
|---|---|---|
| `--config` | `PATH` | model config; defaults to `<model_dir>/config.json` |
| `--layers` | `N` | bind only the first N layers, for partial shard sets |
| `--out` | `FILE` | JSON results (default `k3_run.json`) |
| `--dump-logits` | `PATH` | float32 logits for the first step, for elementwise comparison |
| `--dump-cache-trace` | `DIR` | writes `expert_hist.json` and `expert_trace.bin`, which `tools/sim_cache.py` replays |

### Exit codes

Scripts can rely on these.

| | |
|---:|---|
| `0` | success |
| `1` | a tensor failed to bind, or a forward pass failed |
| `2` | usage error, or a config that could not be read with confidence; the engine declines to guess |
| `3` | the run finished but the `--out` file could not be written, so the results a harness reads are missing |
| `4` | the run finished, but at least one routed expert failed to load, so the emitted ids are unsound. Distinct from `1` because the process otherwise succeeded, and it is the code that catches silent numerical corruption |
| `5` | stopped early by Ctrl-C. The step in flight finished, and the state file, `--out` and the reports were all written, but the token list is shorter than asked for. A second Ctrl-C kills the process instead |

### Environment variables

| variable | used by | |
|---|---|---|
| `HF_TOKEN` | `download-model.sh` | HuggingFace token, read from the environment and never echoed |
| `OMP_NUM_THREADS` | the engine | thread count. When neither this nor `--threads` is given, Linux defaults to the physical core count |
| `K3_TOK_FILES` | tokenizer tools and CI | directory holding `tiktoken.model`, when it is not in a default location |
| `K3_MODEL_DIR` | `tools/budget.py` | checkpoint directory, when not given as an argument |

### Worked examples

```bash
# Full-model, one-token proof of life on an 8 GB-class ARM64 machine.
./bin/k3 ~/k3model --trunk ~/k3trunk --preset ultra \
         --tok ~/k3model --prompt "The capital of France is" --gen 1

# Smallest possible run, the 8 GB floor.
./bin/k3 ~/k3model --trunk ~/k3trunk --preset laptop \
         --tok ~/k3model --prompt "Hello! My name is" --gen 16 --incremental

# Fastest per gigabyte. Pins 90 of 93 trunk layers.
./bin/k3 ~/k3model --trunk ~/k3trunk --preset server \
         --tok ~/k3model --prompt "def fibonacci(n):" --gen 28 --incremental

# Hand-tuned split instead of a preset: everything to the trunk.
./bin/k3 ~/k3model --trunk ~/k3trunk --trunk-gb 110 --cache-gb 13 \
         --tok ~/k3model --prompt-file prompt.txt --gen 32 --incremental

# Reproducible: ids in, ids out, no tokenizer, JSON results.
./bin/k3 ~/k3model --trunk ~/k3trunk --preset desktop \
         --ids 1008,10484,318,15383,387 --gen 8 --incremental --out run.json

# Capture a cache trace, then replay it offline at any capacity.
./bin/k3 ~/k3model --trunk ~/k3trunk --preset workstation \
         --ids 1008,10484,318,15383,387 --gen 8 --incremental \
         --dump-cache-trace /tmp/trace
python3 tools/sim_cache.py /tmp/trace/expert_trace.bin

# Elementwise logit comparison against the PyTorch reference.
./bin/k3 ~/k3model --trunk ~/k3trunk --preset server \
         --ids 3,4,5,6,7 --gen 1 --dump-logits /tmp/c_logits.bin
python3 tools/cmp_logits.py /tmp/c_logits.bin ref_logits.json

# Partial shard set: bind only the first 8 layers.
./bin/k3 ~/k3model --trunk ~/k3trunk --layers 8 \
         --ids 1,2,3 --gen 1

# Under a hard memory ceiling, which is how the ladder was measured.
systemd-run --scope --user -q -p MemoryMax=8G -p MemorySwapMax=0 \
  ./bin/k3 ~/k3model --trunk ~/k3trunk --trunk-gb 2.5 --cache-gb 0.5 \
           --ids 1008,10484,318,15383,387 --gen 8 --incremental
```

## Choosing a preset

```console
$ ./bin/k3 --list-presets
presets (trunk / expert-cache, in GB):
  ultra          2.50 / 0.31    ~3 GB planned: streamed model tables, one state slot. Slow.
  laptop         3.00 / 1.00    8.2 GB peak RSS. The ordinary-path floor.
  desktop       16.00 / 10.00   31.9 GB peak RSS.
  workstation   60.00 / 30.00   95.5 GB peak RSS; the expert cache starts to matter here.
  server       110.00 / 13.00   ~128 GB peak RSS; 90 of 93 trunk layers pinned. Fastest.
  max          110.00 / 109.00  ~224 GB peak RSS; trunk pinned and a large expert cache.

All presets stream the trunk, so they need --trunk <packed_dir>.
Run scripts/k3-doctor.sh to see which one this machine fits.
```

![What each preset actually costs in memory](docs/images/preset_ladder.png)

The boundaries come from the measured ladder, and the doctor keys on `MemAvailable` rather
than `MemTotal`:

```bash
if   [ "$AVAIL_GB" -ge 192 ]; then PRESET=server;      EXPECT="~6 s/token"
elif [ "$AVAIL_GB" -ge  96 ]; then PRESET=workstation; EXPECT="~6-20 s/token"
elif [ "$AVAIL_GB" -ge  32 ]; then PRESET=desktop;     EXPECT="~24 s/token"
elif [ "$AVAIL_GB" -ge  10 ]; then PRESET=laptop;      EXPECT="~27 s/token"
else PRESET=""; fi
```

Two things worth knowing before you pick:

- **`max` is not faster than `server`** in these measurements. The extra 96 GB buys nothing
  outside the noise floor.
- **A preset needs a little more free memory than its peak RSS.** The engine refuses any
  plan above 95% of available memory, to leave room for everything outside the plan, so
  `server` at about 128 GB needs roughly 135 GB available, not 128.
- **Give the trunk memory before the expert cache.** At a fixed 128 GB budget that was
  worth 1.69×. [Allocation beats capacity](#allocation-beats-capacity) has the data.

## Reading the run report

The engine prints a memory plan, then a line per generated token, then a summary. Abridged
from a `workstation` run:

```
cache [final step]
  requests     : 1472  hits 1472 (100.00%)  misses 0  evictions 729
                 TRUE resident hit rate 50.48%
I/O share of wall clock: 71.1%  (trunk 62.4 s + experts 34.2 s of 135.8 s)
trunk [final]
  pinned 48/93 layers, ring 1 slots
  read 368.65 GB in 62.40 s (5908 MB/s)
PEAK RSS for the whole run: 94.74 GB   <- quote this, not the plan
```

Three numbers carry the meaning:

- **`TRUE resident hit rate`**: experts served from RAM. The raw `hits` counter also
  counts experts the prefetcher pulled off disk moments earlier, so it reads 100% at every
  cache size; the resident figure is printed beneath it.
- **`I/O share of wall clock`**: whole-run disk time against total, measured between 41%
  and 61% across the ladder.
- **`PEAK RSS`**: from `getrusage`, after the run. This is the memory figure; the up-front
  plan runs slightly above it.

## Common questions

**Memory sits near 113 GB even at a small preset.** `--trunk` was omitted. Without a packed
trunk directory the whole trunk is loaded resident; every preset assumes streaming.

**A non-ASCII prompt tokenizes oddly.** The shell re-encodes `argv`, so the engine receives
different bytes than you typed. Put the prompt in a file and use `--prompt-file`, which is
read verbatim.

**`--prompt/--prompt-file need --tok DIR`.** The tokenizer ships with the checkpoint, so
add `--tok ~/k3model`. The engine exits rather than guessing where the vocabulary lives. To
skip the tokenizer entirely, pass token ids with `--ids`.

**Throughput is well below the table.** Almost always storage. `python3 tools/devbw.py
<file-on-that-disk>` measures the disk the way the engine reads it, using large random
`O_DIRECT` reads at queue depth 1 and 16, which `dd` does not. Network volumes run several
times slower than local NVMe; keep `~/k3trunk` local.

**The run refused to start over the KV cache.** Context costs about 2.37 MB per position
regardless of budget, and the engine computes that up front rather than discovering it an
hour in. Shorten the request, or drop `--incremental`, which carries no KV cache at all.

**Is the whole 1.56 TB needed?** For generation, yes. For development, no: `make test`
needs nothing at all, and `--layers N` runs against partial shard sets.
`scripts/download-model.sh <dest> --layers N` fetches only the shards those layers need,
about 7 GB for `N=1` and 125 GB for `N=8`. That is for exercising the pipeline on a small
disk; a layer prefix is not the model and does not produce its output.

**Why no BLAS?** Because every matmul here has to give the same bits on every machine.
The test suite checks the engine against a PyTorch reference exactly, not to a tolerance,
and that only works if the order in which each dot product is summed is fixed and known.
A BLAS library chooses its own blocking and reduction order, which can differ between
versions, between vendors (OpenBLAS, MKL, Accelerate), and between thread counts on the
same machine. Each of those answers is numerically correct and none of them matches the
others bit for bit. The kernels in `src/core/k3_ops.c` exist to pin that order: the AVX2
and NEON paths reproduce the scalar reduction exactly, and `test_ops` checks they do.
It also keeps the build free of a dependency that installs differently on each
platform, for kernels that are not the bottleneck anyway. A run is limited by how fast
the trunk and the experts come off disk, not by arithmetic.

**macOS, Windows, WSL?** Linux is the reference platform. macOS/arm64 builds with plain
`make` (see the Makefile's platform block). Windows builds natively too, via MSYS2's
MinGW-w64 GCC (`pacman -S mingw-w64-x86_64-gcc`, then open the "MSYS2 MinGW x64" shell
specifically -- `make`, `make test`, and `make test-all` all pass every gate unmodified,
including the full-model oracle and tokenizer parity against real Kimi K3 weights.
Four Linux-only calls needed porting -- `O_DIRECT`, `pread`, `posix_memalign`, and
`getrusage` -- documented in `src/io/k3_portable_io.h`. One real bug surfaced during the
port and is worth knowing if you extend this code on Windows: `_aligned_malloc`, which
backs the `posix_memalign` shim, must be freed with `_aligned_free`, not plain `free`;
POSIX's `posix_memalign` carries no such restriction, so this is easy to get wrong
silently -- it compiles, and Windows terminates the process with `STATUS_HEAP_CORRUPTION`
only once the corrupted allocator metadata is actually used. `make asan`/`make ubsan`
switch to Clang on Windows (`pacman -S mingw-w64-clang-x86_64-clang
mingw-w64-clang-x86_64-compiler-rt`): MinGW-w64's GCC package ships no sanitizer runtime
at all, confirmed directly rather than assumed. WSL works too, unmodified, since it is
just Linux -- the tokenizer and config reader are portable C99 either way and build
anywhere, in CI included.

---

# Part II: How it works

## The problem: a model that does not fit

[Kimi K3](https://huggingface.co/moonshotai/Kimi-K3) has **2.78 trillion parameters** and
is **1.56 terabytes** as shipped. No consumer machine can hold it, and waiting for better
hardware does not help, because the wall is not speed, it is capacity.

But it is a [mixture of experts](https://huggingface.co/blog/moe), so only 16 of its 896
experts per layer fire for any given token and the rest sit asleep on disk. Keep the
always-on part in memory, stream the sleeping experts, and it fits in **8.24 gigabytes**
on one CPU with no GPU.

The naive requirement is the one every parameter count implies.

![The naive requirement: every parameter resident at bf16](docs/images/eq_naive_memory.png)

So 5.56 terabytes is the number to beat.

![One token wakes 16 experts and leaves 880 asleep](docs/images/moe-sparsity.png)

Kimi K3 has 93 layers. Layer 0 is a plain dense feed-forward layer, so the other 92
layers route, and each of those picks the top 16 experts out of 896.

![Only 16 of 896 experts fire per layer, so most of the model sleeps](docs/images/eq_sparsity_ratio.png)

About 104 billion parameters are active for any given token, out of 2.78 trillion, which is 3.7
percent. The other 96.3 percent still has to exist somewhere reachable, but it does not
have to be in RAM.

Counting the actual bytes on disk rather than guessing:

```text
=== shard census: what the 1.56 TB actually is ===
shards            : 96
total bytes       : 1560936091448  (1.56 TB)

--- routed experts (the part that is streamed, never resident) ---
  experts total     : 82,432   (896 routed x 92 MoE layers)
  bytes per expert  : 17,547,264  exactly
                      = 33,030,144 params x 0.53125 bytes
                      = 0.5 bytes/nibble + 1/32 byte for the shared E8M0 scale
  routed expert set : 82,432 x 17,547,264 = 1.447 TB
```

There are **82,432 routed experts**, each occupying exactly **17,547,264 bytes**. Together
they are **1.447 terabytes**, which is 93 percent of the entire checkpoint. Everything
else (attention projections, routers, norms, embeddings) is the remaining 7 percent.

![Where the 1.56 TB lives: 93% of it is experts that never load](docs/images/bytes_census.png)

That census is the whole strategy in one picture. If those 1.447 terabytes can be
reachable but never resident, the memory problem shrinks by more than an order of
magnitude before a single kernel is written.

![The always-active set: 113.49 GB at bf16, everything else is streamable](docs/images/eq_resident_set.png)

What is left is **56,743,648,000 parameters**, or 113.49 gigabytes at bfloat16. Of that,
108.81 GB is the per-layer dense trunk and 4.70 GB is the embedding table plus the output
head.

## The four reductions

- **5,560 GB**: every parameter at bfloat16, where we start.
- **1,560 GB**: the checkpoint as shipped, because the experts already arrive at half a
  byte per weight.
- **113.49 GB**: what has to be resident once routing means the experts never load.
- **8.24 GB**: what is measured, once the trunk is streamed instead of held.

![Four reductions, and the output is identical at both ends](docs/images/eq_fit_ledger.png)

End to end that is a **675× reduction** from the bfloat16 model and **189×** from the
shipped checkpoint. Nothing is approximated and no weight is dropped: the output at the
bottom of that ladder is byte for byte the output at the top. The chart at the top of
this document is that ledger drawn to scale.

## The machine, and what it assumes

Every measurement here comes from one workstation: a two-socket AMD EPYC 7763 with 124
cores and no SMT, 228 GB of RAM, and 3.2 TB of NVMe. It also has four NVIDIA L40 GPUs,
which sat completely idle for the entire campaign, because this engine has no GPU path.

```text
--- ISA (note: AVX2 present, AVX-512 ABSENT) ---
avx avx2 fma sse4_2

--- memory ---
Mem:           228Gi       5.1Gi       207Gi       3.1Mi        18Gi       223Gi
MemTotal:       239308464 kB
MemAvailable:   233961008 kB
Hugepagesize:       2048 kB
```

There is **no AVX-512**. The engine needs AVX2 and FMA and nothing more, the instruction
set on any desktop CPU from the last decade.

The storage numbers matter more than the CPU numbers, and one runs against expectation.

```text
--- storage bandwidth, measured ---
O_DIRECT cold : 3.2 GB/s     (dd bs=4M iflag=direct after drop_caches)
buffered warm : 2.3 GB/s
engine, trunk : 5373-6064 MB/s sustained during runs
NOTE O_DIRECT is FASTER than buffered here. That is the opposite of the usual
expectation, and it is why the engine opens the trunk O_DIRECT.
```

Reading with `O_DIRECT`, bypassing the page cache entirely, is **faster** here than
reading through it. That single measurement decided the whole I/O design.

![One binary, four kinds of machine, and one identical answer](docs/images/machine-model.png)

One piece of hygiene, because a loaded machine is easy to measure badly:

```text
--- measurement hygiene ---
unattended-upgrades: STOPPED and DISABLED before measurement (was using ~63% of a
  core during the smoke run).
apt-daily.timer and apt-daily-upgrade.timer: DISABLED
```

A background package updater eating most of a core moves a timing by more than most
optimisations do, so it goes off before anything is measured.

How much memory does the engine actually need? Multiplying config values by hand gives the
wrong answer in an instructive way, which is why `tools/budget.py` exists:

```python
# Streamable only if ROUTED. The 2 SHARED experts sit in the same namespace and
# are NOT streamable, which is where hand arithmetic goes wrong.
def classify(name: str) -> str:
    if ".block_sparse_moe.experts." in name:
        return "routed_expert"          # streamable: only 16 of 896 per token
    if ".block_sparse_moe.shared_expert" in name:
        return "shared_expert"          # RESIDENT: runs on every token
    if ".self_attn." in name:
        return "attention"              # resident
    if "embed_tokens" in name or "lm_head" in name:
        return "embedding"              # resident
    return "other"                      # norms, router gates, biases: resident
```

The two shared experts run on every token, so they belong in the resident set even though
their tensor names sit next to the routed experts. Getting that wrong makes the floor look
smaller than it is, which is the worst direction to be wrong in.

---

## The codebase

Six C files compiled into one binary. No BLAS, no PyTorch, no ONNX runtime, no GPU
library. The only dependencies are libm and OpenMP.

```
include/k3/
  k3.h              # the public header: config, weights, every kernel prototype
  k3_cfg.h          # config reader, header-only, refuses to substitute defaults
src/
  core/k3_ops.c     # every numeric kernel: RMSNorm, KDA, MLA, MoE, MXFP4 matmul
  io/k3_st.c        # safetensors reader, hand-written JSON scan, O_DIRECT reads
  io/k3_load.c      # locating one expert's bytes inside a shard
  io/k3_trunk.c     # streaming the dense trunk, pinned prefix plus a ring slot
  cache/k3_cache.c  # the routed-expert LRU cache and its batch prefetch
  model/k3_bind.c   # binding checkpoint tensor names to kernel arguments
  tokenizer/k3_tok.h# byte-level BPE loaded from tiktoken.model
  cli/k3_run.c      # the k3 binary: memory plan, decode loop, reporting
tools/              # python: pack the trunk, replay the cache, verify against torch
benchmarks/         # the cgroup memory ladder and the split sweep
tests/              # fixtures, the tiny oracle, the 93-layer conformance run
```

```bash
CFLAGS = -O3 -std=gnu99 -Wall -Wextra -Wpointer-arith -Wshadow -Wvla \
         -march=native -fopenmp -ffp-contract=off
LDFLAGS = -lm -fopenmp
```

The flag that looks unusual is `-ffp-contract=off`. By default a compiler may fuse a
multiply and an add into a single FMA, which changes the rounding. That is normally good.
Here it is a problem, because the scalar path, the OpenMP path and the AVX2 path must
produce **bit-identical** results, so that a performance change can never quietly become
an accuracy change.

![One C file plus small headers becomes a tiny static binary](docs/images/build-flow.png)

```text
1. build, warnings are failures
  -> clean build, no diagnostics
  test_ops          97784 bytes
  k3_model          89392 bytes
  k3_run           179736 bytes
```

The whole inference engine is **179,736 bytes**, a 176 kilobyte binary whose job is to
run a 1.56 terabyte model.

![A 176 KB binary that runs a 1.56 TB model](docs/images/binary_sizes.png)

One check crosses machines. The tokenizer was run on the same input file under Windows and
under Linux:

```text
=== cross-platform tokenizer determinism ===
  Linux   gcc 13.3.0  x86_64
  Windows gcc 16.1.0  x86_64
  input   src/k3.h (24,499 bytes) -> 6,862 ids
  result  IDENTICAL id streams

  (a naive md5 of stdout DIFFERS by one byte: Windows text-mode stdout writes the
   trailing newline as CRLF. That is the pipe, not the tokenizer.)
```

Two compilers on two operating systems produce the same 6,862 token ids from the same
24,499 bytes. The md5 sums differ by exactly one byte, and the reason is the line ending
the shell added, not anything the tokenizer did.

## Three invariants

The public header opens with three invariants that must hold. Each one is a place where a
plausible-looking implementation produces a model that runs, emits fluent text, and is
wrong, with no crash and no NaN to warn you.

1. **`A_log` is indexed per head, not per channel.** The checkpoint ships `head_dim`
   floats but only the first `num_heads` are meaningful; the rest are padding.
2. **MLA uses NoPE, yet the 64 rope dimensions still exist and are still cached.** Only
   the rotation is absent; dropping the slots changes the head width.
3. **The MoE routing bias steers selection only.** The combining weights come from the
   unbiased sigmoid scores.

Each is ticked off below as its component arrives, and each is gated by a fixture chosen
so that getting it wrong changes the output: `A_log` by a linspace that a per-channel
misindex scrambles, NoPE by asserting the softmax scale is over the full head width, and
the routing bias by a fixture whose bias reorders the top-k on five of its six rows.

This list used to have five entries. The other two, that the UT-transform inverse is
`(I + Akk)^-1` and that `Aqk` keeps its diagonal while `Akk` does not, describe the
chunked parallel form of the delta rule. This engine does not use it. `k3_kda_step` runs
the naive sequential recurrence one position at a time, and so does the PyTorch reference
it is checked against, so neither matrix is ever formed. They were claims about an
algorithm rather than about this code, nothing implemented them, and no test could have
caught getting them wrong. They now live in [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
with the rest of the algorithm description. Restoring a chunked KDA path means restoring
them, with the fixtures that gate them.

## 1. Reading a 1.56 TB checkpoint from its headers

The checkpoint is 96 safetensors files. The format is deliberately simple, which is what
makes it possible to treat 1.56 terabytes as an index rather than as data.

![safetensors: one length, one header, then raw bytes at known offsets](docs/images/eq_st_layout.png)

Every file starts with an 8-byte little-endian length, then that many bytes of JSON
describing every tensor, then the raw tensor bytes back to back. Nothing is compressed and
nothing is interleaved.

![Index the shard, read the exact bytes on demand, then drop the pages](docs/images/st-load.png)

No JSON library is used. The header can be tens of megabytes and only four fields per
tensor are wanted, so the reader scans it directly.

```c
/* Walk the header once, copy nothing we do not need. `p` sits just past the
 * opening quote of the tensor name. */
static const char *st_scan_entry(const char *p, const char *end, K3Tensor *t)
{
    const char *q = memchr(p, '"', (size_t)(end - p));
    if (!q || (size_t)(q - p) >= sizeof t->name) return NULL;
    memcpy(t->name, p, (size_t)(q - p));
    t->name[q - p] = '\0';

    const char *d = st_find_key(q, end, "dtype");
    if (!d) return NULL;
    t->dtype = st_dtype_code(d);

    const char *s = st_find_key(q, end, "shape");
    if (!s) return NULL;
    t->rank = 0;
    t->nelem = 1;
    for (const char *c = s; c < end && *c != ']'; c++) {
        if (*c >= '0' && *c <= '9') {
            long v = strtol(c, (char **)&c, 10);
            if (t->rank >= K3_ST_MAXRANK) return NULL;
            t->shape[t->rank++] = v;
            t->nelem *= (size_t)v;
        }
    }

    /* offsets are RELATIVE to the start of the data section */
    const char *o = st_find_key(q, end, "data_offsets");
    if (!o) return NULL;
    t->off  = (size_t)strtoull(o, (char **)&o, 10);
    while (o < end && (*o < '0' || *o > '9')) o++;
    t->nbytes = (size_t)strtoull(o, (char **)&o, 10) - t->off;
    return o;
}
```

Every tensor goes into a hash table keyed by a hash of its name. The choice of hash is not
arbitrary.

```c
/* Names are long and share deep prefixes
 * ("language_model.model.layers.N.block_sparse_moe.experts.M...."), so the hash must
 * mix every byte; a prefix-only or length-only hash would pile every expert of a
 * layer into one bucket. */
static uint64_t fnv1a(const char *s)
{
    uint64_t h = 1469598103934665603ull;
    while (*s) { h ^= (unsigned char)*s++; h *= 1099511628211ull; }
    return h;
}
```

Half a million tensor names that all begin with the same forty characters is a genuinely
hostile input for a hash function. FNV-1a mixes on every byte, so the expert index at the
end of the name still moves the result.

Reading a tensor afterwards has one wrinkle: `O_DIRECT` requires the offset and the length
to be multiples of the block size, and a tensor starts wherever the previous one ended.

```c
int64_t k3_st_read_aligned(const K3St *s, int shard, int64_t off, int64_t nbytes,
                           void *buf, int64_t bufcap, int64_t *payload_off)
{
    /* widen outward to the enclosing aligned window */
    const int64_t lo  = off & ~(int64_t)(K3_ST_ALIGN - 1);
    const int64_t hi  = (off + nbytes + K3_ST_ALIGN - 1) & ~(int64_t)(K3_ST_ALIGN - 1);
    const int64_t len = hi - lo;
    const int64_t pad = off - lo;
    if (len > bufcap) return 0;
    if (payload_off) *payload_off = pad;

    int64_t got = 0;
    while (got < len) {
        ssize_t r = pread(dfd, (char *)buf + got, (size_t)(len - got), (off_t)(lo + got));
        if (r <= 0) break;      /* the last window may run past EOF */
        got += r;
    }
    return got >= pad + nbytes ? nbytes : (got > pad ? got - pad : 0);
}
```

Note the `break` rather than a failure on a short read: the final aligned window of a shard
extends past the end of the file, which is expected, so the return value checks that the
payload was covered rather than that the whole window was.

```text
indexed 497220 tensors from 96 shards in 0.27 s
```

**Half a million tensors indexed in about a quarter of a second.** This is what makes
everything afterwards possible: the engine never reads a shard it does not need, so the
1.56 terabytes on disk is a catalogue, not a working set.

A parser that agrees with itself proves nothing, so the index is dumped and re-parsed
independently in Python, comparing dtype, shape, offsets, and the widened float bit
patterns.

```python
# Bit patterns, not tolerances: widening bf16 to f32 is lossless.
c_bits = np.asarray(c_values[name], dtype=np.float32).view(np.uint32)
p_bits = ref.astype(np.float32).view(np.uint32)
if not np.array_equal(c_bits, p_bits):
    bad = int(np.count_nonzero(c_bits != p_bits))
    fail(f"{name}: {bad} of {c_bits.size} float32 bit patterns differ")
```

```text
=== shard verification ===
shards: 96
bytes:  1560936091448
expected: 1560936091448
RESULT: EXACT MATCH
```

![96 shards, 1,560,936,091,448 bytes, verified one file at a time](docs/images/shard_sizes.png)

## 2. The config reader that refuses to guess

The model's dimensions come from the checkpoint's own `config.json`, and this is the first
place **invariant four** can silently bite.

![One-based layer indices, and 92 and 93 are both MLA by design](docs/images/eq_layer_map.png)

Kimi K3 alternates two attention mechanisms. Most layers use one, every fourth uses the
other, and the last two are both the second kind so the final layer always does global
attention. The config lists those layers explicitly, and the list is **one-based**.

```text
--- every value below is READ from the checkpoint, not assumed ---
config: config.json (nested shape) | hidden=7168 layers=93 vocab=163840
        | 24 MLA + 69 KDA | experts 896 top16 shared2 | latent=3584

--- KDA/MLA layer map (ONE-based, from full_attn_layers) ---
full_attn_layers (24, all MLA): 4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,93
  note 92 AND 93 are both MLA - the report (2.1) places an extra Gated MLA layer
  at the end of the backbone so the final layer always does global attention.
kda_layers (69): every other layer.
```

Every one of those numbers is read from the file; none is compiled in. They land in one
struct, which is the entire model on one screen:

```c
typedef struct {
    int hidden;            /* 7168  */
    int n_layers;          /* 93    */
    int vocab;             /* 163840 */
    float rms_eps;         /* 1e-5  */

    /* Kimi Delta Attention. 69 of the 93 layers. */
    int kda_heads;         /* 96    */
    int kda_head_dim;      /* 128, and d_k == d_v */
    int conv_k;            /* 4, depthwise, causal, SiLU fused */
    float gate_lb;         /* -5.0, the decay lower bound */

    /* Gated MLA. 24 of the 93 layers. */
    int n_heads;           /* 96    */
    int q_lora;            /* 1536  */
    int kv_lora;           /* 512   */
    int qk_nope;           /* 128   */
    int qk_rope;           /* 64, PRESENT BUT NEVER ROTATED */
    int v_head;            /* 128   */
    int mla_out_gate;      /* 1     */

    /* Stable LatentMoE. 92 of the 93 layers. */
    int n_experts;         /* 896   */
    int topk;              /* 16    */
    int n_shared;          /* 2, full width, added UNWEIGHTED */
    int latent;            /* 3584, the routed-expert width */
    int moe_inter;         /* 3072  */
    float routed_scale;    /* 1.0   */
    int moe_renorm;        /* 1     */
    int latent_norm;       /* 1, RMSNorm on the AGGREGATE, not per expert */

    /* the single dense layer, layer 0 */
    int first_dense;       /* 1     */
    int dense_inter;       /* 33792 */

    int attn_res_block;    /* 12. Boundaries fire when layer_idx % this == 0. */
    float situ_b1;         /* 4.0   */
    float situ_b2;         /* 25.0  */

    int  n_full_attn;      /* 24 */
    int *full_attn;        /* ONE-BASED layer indices */
} K3Cfg;
```

That struct is the contract between the checkpoint and every kernel. If it is right, the
model is Kimi K3. If any field is wrong, the model is something else that still speaks
English.

![Refuse rather than guess, because a guessed field gives you a different model](docs/images/config-guard.png)

Consider what a permissive reader would do. The released config nests its fields one level
deeper than a fixture does, so a reader that only knows the flat shape finds nothing it
recognises. If it then fills in defaults, two things happen: the SiTU betas get 4.0 and
25.0, which are the **correct** values, so nothing looks wrong, and `full_attn_layers`
comes back empty, so all 93 layers run as KDA and the 24 global-attention layers vanish.
The model loads, streams, decodes, and produces grammatical English from an architecture
that is not Kimi K3.

```c
/* An absent field is an ERROR, never a default. Missing names are accumulated so
 * the message lists all of them at once. */
static int cfg_req_int(jval root, const char *key, int *out,
                       const char **missing, int *nmissing)
{
    jval v = json_get(root, key);
    if (v.type != JSON_NUM) {                 /* absent OR the wrong type */
        if (*nmissing < K3_CFG_MAXMISS) missing[(*nmissing)++] = key;
        return 0;
    }
    *out = (int)v.num;
    return 1;
}
```

```text
  [no_layermap]
    k3_cfg: no_layermap.json is missing 1 required field(s):
        full_attn_layers
      refusing to substitute defaults: a config this reader cannot
      fully understand would silently produce a DIFFERENT model.
      ok    correctly rejected no_layermap.json

  [bad_layer_index]
    k3_cfg: bad_layer_index.json full_attn_layers[2] = 999 is outside 1..93
        (the list is ONE-based)
      ok    correctly rejected bad_layer_index.json
```

A config reader is about a hundred and fifty lines of the most boring code in the project,
and it is one of exactly two places that can hand you a different model without telling
you.

## 3. The tokenizer, byte for byte

The other one is the tokenizer. Kimi K3 uses a byte-level BPE with 163,584 ranks plus 256
special tokens, shipped as a `tiktoken.model` file.

![Every case goes through a file, never through argv](docs/images/tok-flow.png)

The loader reads that file straight into the vendored BPE structures. It rests on three
assumptions, each of which produces a tokenizer working perfectly on ASCII and diverging
on everything else:

- **The merge keys are bytes, not code points.** A key that happens to decode as valid
  UTF-8 must still be treated as its raw bytes.
- **Ranks come from the file.** They are not derived from frequency at load time.
- **The added-token block is appended after the ranks**, so an added token's id is 163,584
  plus its index, not its position in a merged table.

The test compares the C tokenizer against the Python `tiktoken` library case by case,
through files rather than command-line arguments:

```text
oracle   : tiktoken 0.13.0
method   : token-for-token comparison; every case passed through a FILE, never argv
           (argv is re-encoded to the active code page on Windows and would compare
            different bytes on every non-ASCII case)

  PASS  han only                 2 ids
  PASS  japanese                 6 ids
  PASS  korean                   5 ids
  PASS  cyrillic                 4 ids
  PASS  arabic                   7 ids
  PASS  emoji zwj                5 ids
  PASS  code python             11 ids
  PASS  json                    19 ids

tokenizer parity: 45/45 cases match
```

Then whole files are pushed through and decoded back:

```text
roundtrip: 48353 bytes -> 14797 ids -> 48353 bytes : PASS   <- k3_ops.c
roundtrip: 24499 bytes -> 6862 ids -> 24499 bytes : PASS   <- k3.h
roundtrip: 201775 bytes -> 52671 ids -> 201775 bytes : PASS   <- REPORT.md
roundtrip: 53444 bytes -> 12145 ids -> 53444 bytes : PASS   <- modeling_kimi_k3.py
```

![Four files in, byte-identical files back out](docs/images/roundtrip_sizes.png)

Two hundred kilobytes of markdown becomes 52,671 token ids and comes back as exactly the
same two hundred kilobytes. Every later claim about identical output rests on the
tokenizer being deterministic.

```c
/* Greedily merge the lowest-rank adjacent pair. Everything here is BYTES. */
static int tok_encode_piece(const Tok *t, const unsigned char *p, int n, int *out)
{
    int parts[K3_TOK_MAXPIECE + 1], np = n + 1;
    for (int i = 0; i <= n; i++) parts[i] = i;          /* byte boundaries */

    for (;;) {
        int best = -1, bestrank = INT_MAX;
        for (int i = 0; i + 2 < np; i++) {
            const int r = tok_rank(t, p + parts[i], parts[i + 2] - parts[i]);
            if (r >= 0 && r < bestrank) { bestrank = r; best = i; }
        }
        if (best < 0) break;                            /* no mergeable pair left */
        memmove(&parts[best + 1], &parts[best + 2],
                (size_t)(np - best - 2) * sizeof(int));
        np--;
    }

    for (int i = 0; i + 1 < np; i++)
        out[i] = tok_rank(t, p + parts[i], parts[i + 1] - parts[i]);
    return np - 1;
}
```

The loop keeps a list of slice boundaries and repeatedly joins whichever adjacent pair has
the lowest rank, which is what makes the result independent of any tie-breaking order.

## 4. Reduction one: the experts already ship at half a byte

The first of the four reductions, and the largest single one.

The routed experts do not ship at bfloat16. They ship in **MXFP4**, a microscaling 4-bit
float format. Each weight is a 4-bit nibble indexing a 16-entry table, and every group of
32 consecutive weights shares one 8-bit exponent.

![MXFP4: a 4-bit nibble scaled by one 8-bit exponent per 32 weights](docs/images/eq_mxfp4.png)

![One byte carries two weights, and the low nibble is the even one](docs/images/mxfp4-decode.png)

![Half a byte per weight plus the shared scale gives one expert exactly](docs/images/eq_bytes_per_weight.png)

Half a byte plus one thirty-second of a byte is 0.53125 bytes per weight, and one expert
has 33,030,144 parameters, so one expert is exactly 17,547,264 bytes. That matches the
census to the byte.

The format is checked against the released checkpoint rather than against documentation:

```json
{
  "note": "Kimi K3 MXFP4 bytes from the released checkpoint. w = E2M1[nibble] * 2^(scale - 127), one scale per 32 elements.",
  "source": "language_model.model.layers.1.block_sparse_moe.experts.0.w1",
  "rows": 64, "packed_cols": 1792, "scale_cols": 112,
  "logical_width": 3584, "group_size": 32,
  "e2m1_lut": [0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0,
              -0.0, -0.5, -1.0, -1.5, -2.0, -3.0, -4.0, -6.0]
}
```

Both halves of the decode are lookup tables, and building them is the only setup the
format needs.

```c
/* E2M1: sign, two exponent bits, one mantissa bit. Sixteen values in total. */
static const float K3_E2M1[16] = {
    0.0f,  0.5f,  1.0f,  1.5f,  2.0f,  3.0f,  4.0f,  6.0f,
   -0.0f, -0.5f, -1.0f, -1.5f, -2.0f, -3.0f, -4.0f, -6.0f
};

/* Byte -> its two weights, so the inner loop does one lookup, not two shifts. */
static void k3_pair_init(void)
{
    for (int b = 0; b < 256; b++) {
        K3_E2M1_PAIR[b][0] = K3_E2M1[b & 0x0F];   /* low nibble  = EVEN element */
        K3_E2M1_PAIR[b][1] = K3_E2M1[b >> 4];     /* high nibble = ODD  element */
    }
}

/* Scale byte -> power of two. 255 is NaN by spec, mapped to 0 to contain damage. */
static void k3_e8m0_init(void)
{
    for (int b = 0; b < 256; b++)
        K3_E8M0[b] = (b == 255) ? 0.0f : ldexpf(1.0f, b - 127);
}
```

Now the nibble order, which is a convention no statistic can check.

![The low nibble is the EVEN element, and reversing it is silently wrong](docs/images/eq_nibble_pack.png)

```text
"expected_swapped_nibbles": {
  "note": "what you get if the low nibble is treated as the ODD element.
           Statistics are identical; positions are wrong."
}
```

Every mean, every standard deviation, every histogram of the swapped version is identical
to the correct one, because it is the same multiset of numbers. Only the positions differ.
A verification that checks distributions would pass a matrix with every adjacent pair of
weights transposed.

The obvious way to use these weights is to decode them into floats and then do a normal
matrix multiply. Pricing that:

![What dequantizing would cost, which is why we multiply from the nibbles](docs/images/eq_dequant_cost.png)

One expert at 17.55 MB becomes 132 MB once expanded to float32. Each token touches 16
experts across 92 layers (1,472 experts), so decoding them all would mean writing out
**194 gigabytes per token** of pure format conversion, before a single multiply-accumulate.

![Half a byte per weight saves 4 TB, and never dequantizing saves 194 GB a token](docs/images/mxfp4_savings.png)

So nothing is ever dequantised. The matrix multiply reads packed nibbles directly.

```c
/* y[rows] = x[in] . W[rows][in], W stored as MXFP4. Nothing is dequantized. */
void k3_matmul_mxfp4(float *y, const float *x, const unsigned char *packed,
                     const unsigned char *scales, int in, int rows, int group)
{
    const int ngroup = (in + group - 1) / group;
    const int rowbytes = (in + 1) / 2;              /* two nibbles per byte */

#pragma omp parallel for schedule(static)
    for (int o = 0; o < rows; o++) {
        const unsigned char *pb = packed + (size_t)o * rowbytes;
        const unsigned char *sb = scales + (size_t)o * ngroup;
        double acc = 0.0;                            /* double, always */

        for (int g = 0; g < ngroup; g++) {
            const float s = K3_E8M0[sb[g]];
            if (s == 0.0f) continue;                 /* a NaN scale zeroes the group */

            const int i0 = g * group;
            const int n = (i0 + group <= in) ? group : (in - i0);
            float wf[64];

            /* low nibble is the EVEN weight, high nibble the ODD one */
            const int half = n / 2;
            for (int k = 0; k < half; k++) {
                const unsigned char b = pb[(i0 / 2) + k];
                wf[2 * k]     = K3_E2M1_PAIR[b][0];  /* low  nibble -> even index */
                wf[2 * k + 1] = K3_E2M1_PAIR[b][1];  /* high nibble -> odd index  */
            }
            if (n & 1) wf[n - 1] = K3_E2M1_PAIR[pb[(i0 / 2) + half]][0];

            double part = 0.0;
            for (int k = 0; k < n; k++) part += (double)x[i0 + k] * (double)wf[k];
            acc += part * (double)s;
        }
        y[o] = (float)acc;
    }
}
```

Two details are worth pausing on. `if (s == 0.0f) continue` handles a scale byte of 255,
which the MXFP4 specification defines as NaN; mapping it to zero means one corrupt byte
kills one group of 32 weights instead of turning an entire row into NaN and poisoning
every downstream layer. And `if (n & 1)` handles a group with an odd number of elements.
with a group size of 32 that can never happen on this checkpoint, and it is written
anyway. That is the difference between code that works and code that is correct, and it
costs one line.

```text
  PASS  mxfp4          64 rows x 3584 elems, EXACT on released checkpoint bytes
```

Not "within tolerance", but **exact**. Both sides read identical bytes off identical weights,
so there is nothing that could legitimately differ, and the test is written with zero
tolerance to say so.

That is reduction one. The experts arrive at 0.53125 bytes per weight instead of 2, which
takes 5.45 TB of expert weights down to 1.447 TB, and never expanding them saves another
194 GB of memory traffic per token.

## 5. Kernels with a floating point contract

Every code path must produce the same bits. RMSNorm is the most used kernel in the model.

![RMSNorm with epsilon inside the square root, accumulated in double](docs/images/eq_rmsnorm.png)

```c
void k3_rmsnorm(float *out, const float *x, const float *w, int n, float eps)
{
    double ss = 0.0;                                   /* double, not float */
    for (int i = 0; i < n; i++) ss += (double)x[i] * (double)x[i];
    const float inv = (float)(1.0 / sqrt(ss / (double)n + (double)eps));
    for (int i = 0; i < n; i++) out[i] = x[i] * inv * (w ? w[i] : 1.0f);
}
```

Two details are load-bearing: the accumulator is a **double** even though every input and
output is a float, and epsilon goes **inside** the square root rather than outside.

![A fixed reduction order, so scalar and AVX2 agree bit for bit](docs/images/eq_accum_order.png)

```c
/* Four accumulators partitioned by i % 4. This pins the summation order, so a
 * 4-wide vector loop adds the same numbers in the same sequence. */
static float k3_dot4(const float *x, const float *w, int n)
{
    double a0 = 0.0, a1 = 0.0, a2 = 0.0, a3 = 0.0;
    int i = 0;
    for (; i + 3 < n; i += 4) {
        a0 += (double)x[i]     * (double)w[i];
        a1 += (double)x[i + 1] * (double)w[i + 1];
        a2 += (double)x[i + 2] * (double)w[i + 2];
        a3 += (double)x[i + 3] * (double)w[i + 3];
    }
    for (; i < n; i++) a0 += (double)x[i] * (double)w[i];
    return (float)((a0 + a1) + (a2 + a3));       /* the parentheses are the contract */
}
```

![bf16 to fp32 is a shift, not a conversion, so widening is lossless](docs/images/eq_bf16_widen.png)

A bfloat16 value is the top 16 bits of a float32 with the bottom 16 dropped, so widening
is a shift left by 16 and it is exact. That is why the trunk can be streamed in its
shipped precision with no accuracy question at all, a point that becomes important much
later.

```c
void k3_matmul_bf16(float *y, const float *x, const uint16_t *W, int in, int out)
{
#pragma omp parallel for schedule(static) if (out > 64)
    for (int o = 0; o < out; o++) {
        const uint16_t *row = W + (size_t)o * in;
        int i = 0;
        double acc;
#if defined(__AVX2__)
        {
            __m256d v = _mm256_setzero_pd();
            for (; i + 3 < in; i += 4) {
                /* bf16 -> f32 is a 16-bit shift: no table, no rounding */
                const __m128i h   = _mm_loadl_epi64((const __m128i *)(row + i));
                const __m128i b32 = _mm_slli_epi32(_mm_cvtepu16_epi32(h), 16);
                const __m256d wd  = _mm256_cvtps_pd(_mm_castsi128_ps(b32));
                const __m256d xd  = _mm256_cvtps_pd(_mm_loadu_ps(x + i));
                v = _mm256_add_pd(v, _mm256_mul_pd(wd, xd));   /* NOT fmadd */
            }
            double a[4];
            _mm256_storeu_pd(a, v);
            acc = (a[0] + a[1]) + (a[2] + a[3]);
        }
#else
        {
            double a0 = 0.0, a1 = 0.0, a2 = 0.0, a3 = 0.0;
            for (; i + 3 < in; i += 4) {
                a0 += (double)k3_bf16f(row[i    ]) * (double)x[i    ];
                a1 += (double)k3_bf16f(row[i + 1]) * (double)x[i + 1];
                a2 += (double)k3_bf16f(row[i + 2]) * (double)x[i + 2];
                a3 += (double)k3_bf16f(row[i + 3]) * (double)x[i + 3];
            }
            acc = (a0 + a1) + (a2 + a3);
        }
#endif
        for (; i < in; i++) acc += (double)k3_bf16f(row[i]) * (double)x[i];
        y[o] = (float)acc;
    }
}
```

Both branches accumulate into four doubles, both partition by `i % 4`, and both reduce as
`(a0 + a1) + (a2 + a3)`. The vector path is the scalar path with the same additions
performed in the same order, four at a time.

Note the multiply-add. `_mm256_add_pd` of an `_mm256_mul_pd` is deliberately not
`_mm256_fmadd_pd`. A fused multiply-add rounds once instead of twice and is therefore
**more** accurate, which is exactly the problem: it would give a different answer from
the scalar loop, and a hardware capability must never change the output.

![Same weights, three code paths, one hash](docs/images/kernel-contract.png)

Proving the AVX2 and scalar paths agree cannot be done with a tolerance check, because a
tolerance check happily passes a kernel that quietly reassociated its sum. So the
benchmark hashes the output instead: FNV-1a over the exact bit pattern of every float in
the result, built twice, once with AVX2 and once without, then diff the digests.

```text
tolerance: atol=1.0e-05 rtol=1.0e-04  (from MANIFEST.json)
  PASS  rmsnorm        n=384    worst=0.01x tol
  PASS  situ_glu       n=48     worst=0.00x tol
        bound check |out|=100.000 must be <= b1*b2=100.0 : ok
  PASS  kda_decay      H=4 D=16 tok=4  max|dg|=4.768e-07 max|dalpha|=1.788e-07
  PASS  mla            n=768    worst=0.08x tol
        H=4 qh=32 (nope 24 + rope 8) v=16 kv_lora=32 scale=0.176777
  PASS  mxfp4          64 rows x 3584 elems, EXACT on released checkpoint bytes
  PASS  matmul_bf16   n=129    bit-identical to k3_matmul
22 passed, 0 failed, 0 skipped
```

The worst case across all 22 kernels is 8 percent of the allowed tolerance, and two are
exact rather than merely close.

![Where one token goes on the floor configuration: 80% of it is waiting on disk](docs/images/token_time_split.png)

Benchmarked at the model's own dimensions on the smallest configuration, the split is
about 36 seconds of trunk reading, 11 seconds of expert reading and 10 seconds of
arithmetic. **Eighty percent of a token is waiting for a disk**, which is why the second
half of this document is about I/O and not about kernels.

## 6. Reduction two: KDA, attention with a memory that never grows

Sixty-nine of the 93 layers use Kimi Delta Attention, and its property that matters here
is easy to state: its memory does not grow with context length.

A standard attention layer stores a key and a value for every token it has seen, so its
cache grows linearly forever. KDA instead keeps one fixed-size matrix per head and updates
it in place as tokens arrive.

![The recurrent state is the same size at 10 tokens and at 100,000](docs/images/eq_kda_state.png)

Ninety-six heads times a 128×128 matrix per head is the entire memory of a KDA layer, at
any sequence length. Across all 93 layers that is **626.25 megabytes**, whether you feed
it ten tokens or a million.

![Every token folds into the same fixed-size state](docs/images/kda-state.png)

![Why 69 layers are KDA: its state does not grow with context](docs/images/context_scaling.png)

That plot is the argument for the whole design. The flat line is KDA. The rising line is
what the other 24 layers cost, and it crosses this machine's memory somewhere around
100,000 tokens. If all 93 layers behaved like it, the model would not fit at any context
length worth having.

![Decay the state, read from it, write the delta, then read the updated state](docs/images/kda-flow.png)

First, the projections go through a short depthwise causal convolution of width four with
SiLU fused in.

![A depthwise causal convolution of width 4 with the activation fused in](docs/images/eq_shortconv.png)

```c
/* Causal depthwise conv with SiLU fused. State is carried across calls. */
void k3_shortconv(float *y, const float *x, const float *w, float *state,
                  int channels, int k, int T)
{
    const int hist = k - 1;                  /* guard on hist, not on buf */
    float *buf = hist ? (float *)malloc((size_t)hist * sizeof(float)) : NULL;
    if (hist && !buf) k3_fatal_oom("ShortConv history", (size_t)hist * sizeof(float));

    for (int c = 0; c < channels; c++) {
        if (hist) {
            if (state) memcpy(buf, state + (size_t)c * hist, (size_t)hist * sizeof(float));
            else       memset(buf, 0, (size_t)hist * sizeof(float));
        }

        for (int t = 0; t < T; t++) {
            const float cur = x[(size_t)t * channels + c];
            float acc = w[(size_t)c * k + hist] * cur;   /* taps run oldest to newest */
            for (int j = 0; j < hist; j++)
                acc += w[(size_t)c * k + j] * buf[j];

            for (int j = 0; j + 1 < hist; j++) buf[j] = buf[j + 1];
            if (hist > 0) buf[hist - 1] = cur;

            y[(size_t)t * channels + c] = acc * sigmoidf_(acc);   /* SiLU, fused */
        }
        if (state && hist) memcpy(state + (size_t)c * hist, buf, (size_t)hist * sizeof(float));
    }
    free(buf);
}
```

Note the guard on `hist` rather than on `buf`: with a kernel width of one there is no
history at all, `malloc(0)` is allowed to return NULL, and a check on the pointer would
silently skip the entire convolution and leave the output untouched.

Then the queries and keys are L2-normalised, a sum of squares, not a mean of squares,
which is a different function that looks nearly identical in code.

![A sum of squares, not a mean, and applied to q and k only](docs/images/eq_l2norm.png)

Then the decay gate, which is **invariant one**.

![The decay gate, with A indexed per head and not per channel](docs/images/eq_kda_decay.png)

```c
void k3_kda_decay(float *g, float *alpha, const float *z, const float *A_log,
                  const float *dt_bias, int H, int D, float lb)
{
    for (int h = 0; h < H; h++) {
        const float a = expf(A_log[h]);      /* PER HEAD, not per channel */
        for (int d = 0; d < D; d++) {
            const int i = h * D + d;
            const float u  = a * (z[i] + dt_bias[i]);
            const float gi = lb * sigmoidf_(u);   /* in (lb, 0] */
            g[i] = gi;
            alpha[i] = expf(gi);                  /* in (e^lb, 1] */
        }
    }
}
```

The gate lower bound is −5, so `alpha` lands between `e^-5` and 1. Near one means this key
channel keeps almost all of its history; near `e^-5` means it forgets almost everything,
per channel and per token.

![The delta rule: decay, read, write the difference, then read again](docs/images/eq_kda_recurrence.png)

```c
void k3_kda_step(float *S, float *o, const float *q, const float *k,
                 const float *v, const float *alpha, float beta, int dk, int dv)
{
    /* 1. decay: scale ROW i of S by alpha[i], per key channel */
    for (int i = 0; i < dk; i++) {
        float *row = S + (size_t)i * dv;
        const float a = alpha[i];
        for (int j = 0; j < dv; j++) row[j] *= a;
    }

    /* 2. read the state along k: u = S^T k */
    float *u = (float *)calloc((size_t)dv, sizeof(float));
    if (!u) k3_fatal_oom("KDA recurrence temporary", (size_t)dv * sizeof(float));
    for (int i = 0; i < dk; i++) {
        const float ki = k[i];
        if (ki == 0.0f) continue;
        const float *row = S + (size_t)i * dv;
        for (int j = 0; j < dv; j++) u[j] += ki * row[j];
    }

    /* 3. rank-one delta write: (v - u) is the prediction error */
    for (int i = 0; i < dk; i++) {
        const float ki = k[i];
        if (ki == 0.0f) continue;
        float *row = S + (size_t)i * dv;
        for (int j = 0; j < dv; j++) row[j] += ki * beta * (v[j] - u[j]);
    }

    /* 4. output from the ALREADY UPDATED state: o = S^T q */
    for (int j = 0; j < dv; j++) o[j] = 0.0f;
    for (int i = 0; i < dk; i++) {
        const float qi = q[i];
        if (qi == 0.0f) continue;
        const float *row = S + (size_t)i * dv;
        for (int j = 0; j < dv; j++) o[j] += qi * row[j];
    }
    free(u);
}
```

That `calloc` happens **after** step one has already scaled the state, so an early return
on allocation failure would leave the recurrent matrix permanently decayed but never
updated. Every subsequent token would then be computed from a state that is quietly wrong,
with nothing to indicate it. That is why the failure path aborts instead of returning.

![Nine ordered steps, and the numbering is not decoration](docs/images/kda-nine-steps.png)

```c
void k3_kda_layer(float *out, const float *x, const K3KdaW *w, const K3Cfg *c,
                  int T, float *state, float *scratch)
{
    const int E = c->hidden, H = c->kda_heads, D = c->kda_head_dim;
    const int P = H * D, K = c->conv_k, hist = K - 1;

    float *q  = scratch;                 float *k  = q + (size_t)T * P;
    float *v  = k + (size_t)T * P;       float *z  = v + (size_t)T * P;
    float *al = z + (size_t)T * P;       float *bt = al + (size_t)T * P;
    float *o  = bt + (size_t)T * H;      float *gb = o + (size_t)T * P;
    float *wr = gb + P;                  float *fa = wr + P;

    /* 1. projections */
    for (int t = 0; t < T; t++) {
        const float *xt = x + (size_t)t * E;
        k3_mmw(q + (size_t)t * P, xt, w->q, w->wdt, E, P);
        k3_mmw(k + (size_t)t * P, xt, w->k, w->wdt, E, P);
        k3_mmw(v + (size_t)t * P, xt, w->v, w->wdt, E, P);
        k3_mmw(bt + (size_t)t * H, xt, w->b, w->wdt, E, H);
        k3_mmw(fa, xt, w->f_a, w->wdt, E, D);        /* one low-rank pair, all heads */
        k3_mmw(z + (size_t)t * P, fa, w->f_b, w->wdt, D, P);
    }

    /* 2. ShortConv with fused SiLU, carrying state across calls */
    float *cs = state ? state + (size_t)H * D * D : NULL;
    k3_shortconv(q, q, w->q_conv, cs ? cs : NULL, P, K, T);
    k3_shortconv(k, k, w->k_conv, cs ? cs + (size_t)P * hist : NULL, P, K, T);
    k3_shortconv(v, v, w->v_conv, cs ? cs + (size_t)2 * P * hist : NULL, P, K, T);

    /* 3. L2Norm on q and k ONLY, per head. v is deliberately left alone. */
    for (int t = 0; t < T; t++)
        for (int h = 0; h < H; h++) {
            l2norm_(q + (size_t)t * P + (size_t)h * D, D, 1e-6f);
            l2norm_(k + (size_t)t * P + (size_t)h * D, D, 1e-6f);
        }

    /* 4/5. beta and the decay chain */
    for (int t = 0; t < T; t++) {
        for (int h = 0; h < H; h++) bt[(size_t)t * H + h] = sigmoidf_(bt[(size_t)t * H + h]);
        k3_kda_decay(z + (size_t)t * P, al + (size_t)t * P, z + (size_t)t * P,
                     w->A_log, w->dt_bias, H, D, c->gate_lb);
    }

    /* 6. recurrence, per head, with q pre-scaled by d_k^-0.5 */
    float *S = state;
    float *Sown = NULL;
    if (!S) {
        Sown = (float *)calloc((size_t)H * D * D, sizeof(float));
        if (!Sown) k3_fatal_oom("KDA recurrent state", (size_t)H * D * D * sizeof(float));
        S = Sown;
    }
    const float qscale = 1.0f / sqrtf((float)D);
    for (int t = 0; t < T; t++)
        for (int h = 0; h < H; h++) {
            const size_t off = (size_t)t * P + (size_t)h * D;
            for (int i = 0; i < D; i++) wr[i] = q[off + i] * qscale;
            k3_kda_step(S + (size_t)h * D * D, o + off, wr, k + off, v + off,
                        al + off, bt[(size_t)t * H + h], D, D);
        }

    /* 7/8/9. head-wise RMSNorm, THEN the gate, THEN the output projection */
    for (int t = 0; t < T; t++) {
        const float *xt = x + (size_t)t * E;
        float *ot = o + (size_t)t * P;
        for (int h = 0; h < H; h++)
            k3_rmsnorm(ot + (size_t)h * D, ot + (size_t)h * D, w->o_norm, D, c->rms_eps);
        k3_mmw(gb, xt, w->g, w->wdt, E, P);
        for (int i = 0; i < P; i++) ot[i] *= sigmoidf_(gb[i]);
        k3_mmw(out + (size_t)t * E, ot, w->o, w->wdt, P, E);
    }
    free(Sown);
}
```

Nine numbered steps, and the numbering is not decoration. Step 3 normalises `q` and `k`
and deliberately leaves `v` alone. Step 6 pre-scales the query by one over the square root
of the head dimension **before** the recurrence rather than after it.

![Norm first, then gate, then project, and that order is not interchangeable](docs/images/eq_kda_gate.png)

Steps 7, 8 and 9 carry an ordering constraint of their own. The released model ends the
layer with a fused kernel from the `fla` library called `FusedRMSNormGated`, which takes
the raw gate and applies the sigmoid internally. The reference implementation instead does
an explicit RMSNorm followed by a multiply by the sigmoid of the gate. Those are the same
function **only** if the fused kernel is norm-first and gate-second, so
`tools/verify_kda.py` proves it rather than assuming it:

> The plausible alternatives, gating before norming or norming the gate, both run cleanly
> and produce a different model.

No test catches that except comparing against the released code, which is exactly what
that script does.

```text
one KDA layer  : 443740384 params  (887.48 MB at bf16)
69 KDA layers  : 61.24 GB at bf16   (KDA attention ONLY, not the whole trunk)
full trunk     : 113.49 GB at bf16, 56,743,648,000 always-active params
one expert     : 33030144 params  (17.55 MB at MXFP4)
all 82432 experts: 1.45 TB at MXFP4  <- streamed from NVMe

per-sequence state, FIXED regardless of context:
  KDA recurrent : 217.06 MB at bf16
  ShortConv     : 15.26 MB at bf16
  MLA KV        : 2.37 MB per position (24 MLA layers, EXPANDED k and v, fp32)
                  19.38 GB at 8192 context
                  310.04 GB at 131072 context

allocating and running ONE full-width KDA layer (fp32)...
  weights: 1.77 GB
  ran 4 tokens in 0.17 s (44 ms/token)
  output all finite: YES, max |y| = 0.000003
  state non-zero   : yes
```

The two lines under "FIXED regardless of context" are the payoff. The KDA state is 217 MB
and the convolution history is 15 MB, and neither number moves no matter how long the
sequence gets, against 310 GB for the other attention mechanism at 131,072 positions.

That is reduction two: 69 of 93 layers have a memory cost completely independent of how
much text you feed them.

## 7. Reduction three: MLA, one latent instead of ninety-six heads

The other 24 layers do global attention, because a purely recurrent stack cannot look back
at an arbitrary earlier token with full precision. They use Gated Multi-head Latent
Attention, and they are the ones that cost memory per position.

A normal attention layer with 96 heads would store, for every position, a key and a value
for each head. MLA instead projects the token down into one small shared latent, caches
only that, and rebuilds the per-head keys and values from it when they are needed.

![One latent per position is cached, and k and v are rebuilt on use](docs/images/eq_mla_latent.png)

![The query and the token both pass through a small shared latent](docs/images/mla-latent.png)

The latent is 512 dimensions for the key and value content plus 64 more, and those 64 are
where **invariant four** lives.

```c
/* NoPE: the 64 rope dimensions are projected and cached, but never rotated. */
static void k3_mla_project(float *q, float *kv, const float *x, const K3MlaW *w,
                           const K3Cfg *c)
{
    float qa[K3_MAX_QLORA];                  /* down to 1536, norm, back up */
    k3_mmw(qa, x, &w->q_a_proj, c->q_lora, c->hidden);
    k3_rmsnorm(qa, qa, w->q_a_norm, c->q_lora, c->rms_eps);
    k3_mmw(q, qa, &w->q_b_proj, c->n_heads * (c->qk_nope + c->qk_rope), c->q_lora);

    /* one 576-wide projection: the entire per-position cache for this layer */
    k3_mmw(kv, x, &w->kv_a_proj, c->kv_lora + c->qk_rope, c->hidden);
    k3_rmsnorm(kv, kv, w->kv_a_norm, c->kv_lora, c->rms_eps);
    /* the trailing qk_rope floats are left unnormalised and unrotated */
}
```

The head width is 192 (128 content dimensions plus those 64 carried-but-unrotated
ones), so the softmax scale is the inverse square root of 192 rather than of 128. Getting that
wrong is a change of about 22 percent in every attention score, and it produces perfectly
readable output.

```c
    for (int t = 0; t < T; t++) {
        const int p = cached + t;
        for (int h = 0; h < H; h++) {
            const float *qt = q + ((size_t)t * H + h) * qh;
            float m = -INFINITY;
            for (int s = 0; s <= p; s++) {                 /* causal: s <= p */
                const float *ks = K3_KV_AT(s) + (size_t)h * kvd;
                const float *kr = K3_ROPE_AT(s);           /* shared slot */
                double d = 0.0;
                for (int i = 0; i < qn; i++) d += (double)qt[i] * (double)ks[i];
                /* the rope slot is UNROTATED but still scored, and the SAME 64
                 * values serve every head */
                for (int i = 0; i < qr; i++) d += (double)qt[qn + i] * (double)kr[i];
                sc[s] = (float)d * scale;
                if (sc[s] > m) m = sc[s];
            }
            double z = 0.0;
            for (int s = 0; s <= p; s++) { sc[s] = expf(sc[s] - m); z += sc[s]; }
```

The score is two dot products added together. The first runs over the 128 content
dimensions, which are per head. The second runs over the 64 rope dimensions, which are
**shared**: `K3_ROPE_AT(s)` takes no head index, so all 96 heads score against the same 64
numbers. That is what makes the cache 576 wide instead of 96 × 320, and skipping the
second term is the quiet way to get a model that still speaks.

![Twenty-four MLA layers, expanded k and v in fp32, per position](docs/images/eq_mla_kv.png)

![What MLA caches per position, per layer](docs/images/kv_layout.png)

![The released code caches expanded heads, the latent is 53x smaller](docs/images/eq_kv_compression.png)

Ninety-six heads times 320 floats is 30,720 floats per position per layer. The latent is
576. That is **53 times smaller for mathematically identical output**, and it is the difference
between a context length you can use and one you cannot.

Because the KV cache is the one thing that grows, the engine refuses to start rather than
discovering the problem an hour in:

```c
/* The context limit is the MLA KV cache, not any array size. */
if (incremental) {
    const double kv_need = (double)(np + gen + 1) * K3_KV_BYTES_PER_POS;
    const double avail   = mem_available_bytes();
    if (avail > 0.0 && kv_need > avail * 0.9) {
        fprintf(stderr,
            "\nREFUSING: the KV cache for %d positions needs %s but only %s is\n"
            "available. This is a MEMORY limit, not an engine ceiling: MLA caches\n"
            "expanded k and v in fp32 across 24 layers, so context costs ~2.37 MB per\n"
            "position regardless of budget. Shorten the request, or use full\n"
            "recompute (drop --incremental), which carries no KV cache at all.\n",
            np + gen + 1, kb, ab);
        return 2;
    }
}
```

"This is a MEMORY limit, not an engine ceiling" saves somebody an afternoon of looking for
a hardcoded constant that does not exist.

That is reduction three. Context costs 2.37 MB per position instead of 125.

## 8. Attention residuals: layers that look back

One more structural piece, unusual enough to be worth a section even though it costs no
memory.

In a normal transformer each layer adds its output to a running residual stream. Kimi K3
does something different: each layer attends over the outputs of every preceding **block**,
where a block is twelve layers, and learns how much of each to mix in.

![Each layer attends over the outputs of every preceding block](docs/images/eq_attn_res.png)

![Blocks of twelve, so the residual stack never exceeds nine sources](docs/images/eq_block_count.png)

![Every twelve layers the running prefix is snapshotted and cleared](docs/images/attn-res.png)

```c
void k3_attn_res(float *out, const float *src, const float *fold,
                 int nsrc, int n, float eps)
{
    float *score = (float *)malloc((size_t)nsrc * sizeof(float));
    if (!score) k3_fatal_oom("AttnRes scores", (size_t)nsrc * sizeof(float));

    for (int s = 0; s < nsrc; s++) {
        const float *v = src + (size_t)s * n;
        double ss = 0.0;
        for (int i = 0; i < n; i++) ss += (double)v[i] * (double)v[i];
        const float inv = (float)(1.0 / sqrt(ss / (double)n + (double)eps));
        double acc = 0.0;                            /* key: the NORMALISED source */
        for (int i = 0; i < n; i++) acc += (double)(v[i] * inv) * (double)fold[i];
        score[s] = (float)acc;
    }

    float m = score[0];
    for (int s = 1; s < nsrc; s++) if (score[s] > m) m = score[s];
    double z = 0.0;
    for (int s = 0; s < nsrc; s++) { score[s] = expf(score[s] - m); z += score[s]; }

    for (int i = 0; i < n; i++) out[i] = 0.0f;
    for (int s = 0; s < nsrc; s++) {
        const float p = (float)(score[s] / z);
        const float *v = src + (size_t)s * n;   /* the RAW source, not the key */
        for (int i = 0; i < n; i++) out[i] += p * v[i];
    }
    free(score);
}
```

The keys are normalised before scoring and the values are the **raw** sources. Norming the
values as well is the obvious-looking mistake, and it quietly rescales the residual stream.

![One layer: aggregate, attend, aggregate again, then route](docs/images/decoder-layer.png)

```c
void k3_decoder_layer_inc(float *h, float *block_residual, int *n_blocks,
                          const K3LayerW *w, const K3Cfg *c, int layer_idx,
                          int T, float *state, float *scratch,
                          float *kvc, float *ropec, int cached, int cap)
{
    const int E = c->hidden;
    const int maxb = c->n_layers / c->attn_res_block + 2;

    float *pref   = scratch;                    /* [T][E] the running residual   */
    float *tmp    = pref + (size_t)T * E;       /* [T][E] module output          */
    float *hin    = tmp  + (size_t)T * E;       /* [T][E] normalised layer input */
    float *foldA  = hin  + (size_t)T * E;       /* [E] attention aggregator      */
    float *foldM  = foldA + E;                  /* [E] mlp aggregator            */
    float *src    = foldM + E;                  /* [maxb+1][E] source stack      */
    float *dgu    = src + (size_t)(maxb) * E;   /* [2*dense_inter]               */
    float *sub    = dgu + (size_t)2 * c->dense_inter;   /* scratch for the module */

    /* norm gain and scoring projection collapse into one vector */
    for (int i = 0; i < E; i++) {
        foldA[i] = w->attn_res_norm[i] * w->attn_res_proj[i];
        foldM[i] = w->mlp_res_norm[i]  * w->mlp_res_proj[i];
    }

    memcpy(pref, h, (size_t)T * E * sizeof(float));
    int have_prefix = 1;                        /* mirrors "prefix_sum is not None" */

    /* aggregation before attention, only when snapshots already exist */
    if (*n_blocks > 0) {
        for (int t = 0; t < T; t++) {
            for (int b = 0; b < *n_blocks; b++)
                memcpy(src + (size_t)b * E,
                       block_residual + ((size_t)t * maxb + b) * E,
                       (size_t)E * sizeof(float));
            memcpy(src + (size_t)(*n_blocks) * E, pref + (size_t)t * E,
                   (size_t)E * sizeof(float));
            k3_attn_res(h + (size_t)t * E, src, foldA, *n_blocks + 1, E, c->rms_eps);
        }
    }

    /* block boundary: snapshot the running residual, then CLEAR it */
    if (layer_idx % c->attn_res_block == 0) {
        for (int t = 0; t < T; t++)
            memcpy(block_residual + ((size_t)t * maxb + *n_blocks) * E,
                   pref + (size_t)t * E, (size_t)E * sizeof(float));
        (*n_blocks)++;
        have_prefix = 0;
    }

    /* whichever attention was bound for this layer */
    for (int t = 0; t < T; t++)
        k3_rmsnorm(hin + (size_t)t * E, h + (size_t)t * E, w->in_norm, E, c->rms_eps);
    if (w->kda) k3_kda_layer(tmp, hin, w->kda, c, T, state, sub);
    else        k3_mla_cached(tmp, hin, w->mla, c, T, sub, kvc, ropec, cached, cap);

    if (have_prefix) for (size_t i = 0; i < (size_t)T * E; i++) pref[i] += tmp[i];
    else             { memcpy(pref, tmp, (size_t)T * E * sizeof(float)); have_prefix = 1; }

    /* aggregation before the MLP, with no emptiness guard */
    for (int t = 0; t < T; t++) {
        for (int b = 0; b < *n_blocks; b++)
            memcpy(src + (size_t)b * E,
                   block_residual + ((size_t)t * maxb + b) * E,
                   (size_t)E * sizeof(float));
        memcpy(src + (size_t)(*n_blocks) * E, pref + (size_t)t * E,
               (size_t)E * sizeof(float));
        k3_attn_res(h + (size_t)t * E, src, foldM, *n_blocks + 1, E, c->rms_eps);
    }

    for (int t = 0; t < T; t++)
        k3_rmsnorm(hin + (size_t)t * E, h + (size_t)t * E, w->post_norm, E, c->rms_eps);

    if (w->moe) {
        int   idx[K3_MAX_TOPK]; float wt[K3_MAX_TOPK];
        k3_moe(tmp, hin, w->moe, c, T, idx, wt, sub);
    }
}
```

The layer never asks which kind it is; it checks whether `w->kda` was bound, so the layer
map from `config.json` is the only thing that decides. The two aggregations are not
symmetric: the one before attention is skipped when no snapshots exist yet, and the one
before the MLP has no such guard, because the reference has none either.

Does that do anything observable? The reference forward pass draws it. Printing the
maximum absolute activation after every layer:

```text
  L45  KDA MoE      41.2 s   |h| max 47.714829
  L46  KDA MoE      38.9 s   |h| max 62.183392
  L47  MLA MoE      44.3 s   |h| max 76.281532
  L48  KDA MoE      36.1 s   |h| max 2.902113
  L49  KDA MoE      39.5 s   |h| max 4.353188
```

Layer 47 to layer 48: the activation magnitude goes from **76.28 to 2.90**, a factor of
26, in one layer. That is a block boundary: the running prefix was snapshotted and
cleared, so the next layer starts from a fresh small residual.

![Attention residuals drawn by the data: activations climb, then collapse every 12 layers](docs/images/activation_spikes.png)

Seven sawteeth, one per block, each climbing for twelve layers and then collapsing. Nobody
drew that shape; the model did. The biggest peak is 136.7 at layer 59, dropping to 1.78 at
layer 60. When a measured curve has exactly the period the code says it should, that is a
decent sign the code matches the model.

## 9. Picking 16 experts of 896

The router scores every one of the 896 experts and picks sixteen. This is **invariant
five**, the subtlest of the lot.

![The bias steers selection only, the weights come from unbiased scores](docs/images/eq_router.png)

```c
/* Score all n_experts, pick the top-k, weight them. The bias steers SELECTION only. */
void k3_router(int *idx, float *w, const float *x, const float *W, const float *bias,
               int hidden, int n_experts, int topk, int renorm, float routed_scale)
{
    float sc[K3_MAX_EXPERTS], ch[K3_MAX_EXPERTS];

#pragma omp parallel for schedule(static)
    for (int e = 0; e < n_experts; e++) {
        double acc = 0.0;
        for (int i = 0; i < hidden; i++)
            acc += (double)x[i] * (double)W[(size_t)e * hidden + i];
        sc[e] = 1.0f / (1.0f + expf(-(float)acc));      /* the UNBIASED score */
        ch[e] = sc[e] + (bias ? bias[e] : 0.0f);        /* the SELECTION score */
    }

    char taken[K3_MAX_EXPERTS] = {0};        /* top-k by repeated max */
    for (int j = 0; j < topk; j++) {
        int best = -1;
        for (int e = 0; e < n_experts; e++)
            if (!taken[e] && (best < 0 || ch[e] > ch[best])) best = e;
        taken[best] = 1;
        idx[j] = best;
        w[j] = sc[best];                                 /* the UNBIASED score again */
    }

    if (renorm) {
        float s = 0.0f;
        for (int j = 0; j < topk; j++) s += w[j];
        if (s > 0.0f) for (int j = 0; j < topk; j++) w[j] /= s;
    }
    for (int j = 0; j < topk; j++) w[j] *= routed_scale;
}
```

`sc[e]` and `ch[e]` are both computed and used for different things. The biased score picks
the winners; the unbiased score weights them. Collapsing those two into one variable is a
two-character edit that changes the model.

![Experts run in a narrow latent, and the norm is on the aggregate](docs/images/eq_moe_latent.png)

![Route, run 16 experts in a 3584-wide latent, then project back up](docs/images/moe-dispatch.png)

```c
/* Stable LatentMoE for one token.
 *
 * Six steps, and step 4 is the one people get wrong: the RMSNorm is applied to the
 * AGGREGATE of the weighted expert outputs, not to each expert individually. Norming
 * per expert and then summing is a different function.
 *
 * The two shared experts run on the ORIGINAL full-width input, not the latent, and
 * their output is added UNWEIGHTED. They are not part of the top-k sum. */
void k3_moe(float *out, const float *x, const K3MoeW *w, const K3Cfg *c,
            int T, int *idx, float *wt, float *scratch)
{
    const int E = c->hidden, L = c->latent, I = c->moe_inter;
    float *z = scratch, *accL = z + L, *gu = accL + L, *act = gu + 2 * I;
    float *edn = act + I;

    for (int t = 0; t < T; t++) {
        const float *xt = x + (size_t)t * E;

        /* 1. route on the FULL width, not the latent */
        k3_router(idx, wt, xt, w->gate, w->gate_bias, E,
                  c->n_experts, c->topk, c->moe_renorm, c->routed_scale);

        /* 2. down-project into the expert latent */
        k3_mmw(z, xt, w->down, w->wdt, E, L);

        /* 3. run the chosen experts, accumulating in the latent */
        for (int i = 0; i < L; i++) accL[i] = 0.0f;
        if (w->src && w->src->getmany) w->src->getmany(w->src, w->layer, idx, c->topk);

        for (int j = 0; j < c->topk; j++) {
            K3ExpertQ q;
            if (w->src->get(w->src, w->layer, idx[j], &q) != 0) {
                k3_expert_drops++;          /* counted, never silent */
                continue;
            }
            k3_matmul_mxfp4(gu,     z, q.p1, q.s1, L, I, K3_MXFP4_GROUP);
            k3_matmul_mxfp4(gu + I, z, q.p3, q.s3, L, I, K3_MXFP4_GROUP);
            k3_situ_glu(act, gu, I, c->situ_b1, c->situ_b2);
            k3_matmul_mxfp4(edn, act, q.p2, q.s2, I, L, K3_MXFP4_GROUP);
            for (int i = 0; i < L; i++) accL[i] += wt[j] * edn[i];
        }

        /* 4. norm the AGGREGATE, not each expert */
        if (c->latent_norm) k3_rmsnorm(accL, accL, w->latent_norm, L, c->rms_eps);

        /* 5. back up to full width */
        float *ot = out + (size_t)t * E;
        k3_mmw(ot, accL, w->up, w->wdt, L, E);

        /* 6. shared experts, on the ORIGINAL input, added UNWEIGHTED */
        const int SI = I * c->n_shared;
        k3_mmw(gu,      xt, w->sh1, w->wdt, E, SI);
        k3_mmw(gu + SI, xt, w->sh3, w->wdt, E, SI);
        k3_situ_glu(act, gu, SI, c->situ_b1, c->situ_b2);
        k3_mmw(edn, act, w->sh2, w->wdt, SI, E);
        for (int i = 0; i < E; i++) ot[i] += edn[i];
    }
}
```

The activation inside each expert is SiTU-GLU, a gated unit with both halves passed
through bounded tanh functions.

![SiTU-GLU with beta1 = 4 and beta2 = 25, so the product is bounded](docs/images/eq_situ_glu.png)

```c
void k3_situ_glu(float *y, const float *x, int n, float b1, float b2)
{
    const float *gate = x;
    const float *up   = x + n;
    for (int i = 0; i < n; i++) {
        const float g = gate[i];
        /* the sigmoid takes the UNCAPPED gate */
        const float a = b1 * tanhf(g / b1) * sigmoidf_(g);
        const float u = b2 * tanhf(up[i] / b2);
        y[i] = a * u;
    }
}
```

The sigmoid reads the **uncapped** gate `g`, not the capped `b1 * tanh(g / b1)`. Feeding it
the capped value gives a function that is still smooth, still bounded, still produces
fluent output, and is a different activation.

Because both factors are bounded, the product can never exceed 4 × 25 = 100, and the
fixture drives it deliberately to that exact analytic cap:

```text
  PASS  situ_glu       n=48     worst=0.00x tol
        bound check |out|=100.000 must be <= b1*b2=100.0 : ok
```

A fixture that only tested the near-linear region would pass an implementation with the
caps left out entirely, because for small inputs the tanh is almost the identity.

Now the thing to remember for later. The Kimi K3 technical report describes a training
technique called **Quantile Balancing** whose entire purpose is to flatten expert usage
across the pool, so that no small set of experts dominates.

![The hottest experts, out of 10,010 distinct ones touched](docs/images/expert_reuse.png)

That is good for the model, and it is going to be very bad for the cache. Hold that
thought.

One last thing about the `continue` in the expert loop. A dropped expert means one token
was computed with f