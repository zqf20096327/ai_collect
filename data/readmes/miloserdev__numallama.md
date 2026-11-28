<img width="100%" alt="numallama.gif" src="https://raw.githubusercontent.com/miloserdev/numallama/refs/heads/master/docs/numallama.gif" />

# numallama — fast NUMA-aware CPU inference for Llama 3.x, Qwen2.5, Qwen3 / Qwen3-MoE and Qwen3.5 / 3.8

numallama (code name) is a small C inference engine (one translation unit: a thin `src/runq.c`
entry point and topical headers, no dependencies) for Llama 3.x, Qwen2.5,
Qwen3 / Qwen3-MoE and the hybrid Qwen3.5 / Qwen3.8 dense models, tuned for large Arm servers (Ampere Altra / Neoverse N1, NEON + dotprod) and multi-socket
NUMA machines. It started as a fork of [jameswdelancey/llama3.c](https://github.com/jameswdelancey/llama3.c),
itself derived from Andrej Karpathy's [llama2.c](https://github.com/karpathy/llama2.c).

Highlights:

- **Hybrid linear attention (Qwen3.5 / Qwen3.8 dense, e.g. Qwen3.8-27B)**: Gated DeltaNet layers with a
  fixed-size recurrent state (no KV cache, ~150 MB for any context) and every 4th layer gated full attention
  with partial RoPE; the state slices stay in each core's L2. Text only (no vision, MTP head not used yet).
- **Mixture of experts (Qwen3-MoE, e.g. Qwen3-30B-A3B)**: int8 router, top-k routing, every expert
  split evenly between the NUMA nodes; batched prefill groups the tokens by expert so every expert is
  read once per block. Also Qwen3 attention (head_dim != dim / heads, per-head q/k RMSNorm).
- **int8 (Q8) and 4-bit (Q4) weights**, repacked at load into 4-row blocks for NEON `sdot` by lane
  (single token and 4x8 batched kernels). Q4 is asymmetric (groups of 32, fp16 scale + min) and
  quantized with an importance matrix collected by the engine itself: on Llama 3.2 3B its KL to
  full precision is 0.013 (llama.cpp Q4_K_M: 0.015).
- **KV cache int8 by default** (`-K f32` for full precision): int8 K/V and per-head queries with
  per-64 group scales, scored with int8 `sdot`. It quarters the cache (Qwen3.8-27B at 131k:
  16 GB -> 4 GB) and measured +6-28% decode and +5-26% prefill at 8k-30k prompts; the logits move
  by ~0.005 KL against the f32 cache. Session dumps and shared system-prefix slots shrink the
  same way.
- **Quantized embeddings**: the token embedding table is never dequantized as a whole; the row of
  the current token is dequantized on demand. This keeps RSS lower by 1.2 GB (Qwen3-30B) to
  5.1 GB (Qwen3.8-27B) and shortens the load.
- **Multi-socket NUMA**: every weight matrix and the KV cache are split between the sockets
  (`mbind`), each socket's threads compute only its rows, per-node work counters and per-node
  activation buffers keep cross-socket traffic minimal; attention and the MoE router synchronize
  within a socket only. 2 sockets give +50..85% decode speed.
- **Persistent thread pool** with flag-tree barriers in node-local memory (~1 us within a socket,
  ~2 us across), dynamic row distribution, prefetch of the next phase's rows while waiting,
  futex sleep when idle, automatic choice of idle CPUs per NUMA node; sampling runs on the pool.
- **Batched prompt prefill** (matrix x matrix) and a **multi-token decode step**.
- **Speculative decoding**, exact (output distribution unchanged):
  prompt lookup (n-grams from the whole dialog) and an optional small **draft model** (`-d`).
- **OpenAI-compatible server** (`-m server`): `/v1/chat/completions` with streaming, tool calls and
  reasoning, KV-cache reuse of the shared prefix between requests, and **continuous batching**
  (`-J`, dense/MoE models): several sessions decode one token each in one weight-reading pass.
  Works with the official OpenAI clients and anything built on them.
- **Chat** with the native templates (Llama 3, ChatML), context trimming, and **tool calling**
  (`config/tools.json`: sandboxed `ls`/`cat`/`grep`/`find` via fork/execvp, no shell).
- Correct **tiktoken-style tokenizer** (Llama 3 / Qwen2 pre-tokenizer regex + byte-level BPE).
- **SmoothQuant** for Qwen (activation outliers folded into the weights at export time).

See [docs/BENCHMARKS.md](docs/BENCHMARKS.md) for measurements, including a comparison with llama.cpp.
The binary is still called `runq` (the name of the upstream int8 runtime).

## Quick start

Requirements: Linux, gcc or clang, Python 3 with numpy (only for converting models), and RAM for the
model file plus a few GB. Tuned and tested on AArch64 with dotprod (Ampere Altra / Neoverse N1); other
CPUs build with portable C fallbacks, which are not tuned or regularly tested.

For ARMv8.0 boards without SDOT (Cortex-A53/A72, many SBCs) build the portable binary instead of
`make`:

```bash
make portable        # -> ./runq_portable, -march=armv8-a, no SDOT
```

`make` keeps `-mcpu=native` and the SDOT kernels on the build machine; `make portable` also works on
x86-64. The portable kernels are correct but slower; RAM-aware defaults for small boards are still
on the low-end track in `todos.md`.

### Ready-made models

Converted models are published on Hugging Face, so you can skip the conversion:

```bash
make                                   # -> ./runq
pip install huggingface_hub
hf download miloserdev/Qwen3-30B-A3B-Instruct-2507-numallama --local-dir models/qwen3-30b
./runq models/qwen3-30b/qwen3-30b-a3b-instruct-2507-q4.bin -z models/qwen3-30b/tokenizer.bin -m chat
./runq models/qwen3-30b/qwen3-30b-a3b-instruct-2507-q4.bin -z models/qwen3-30b/tokenizer.bin -m server -P 8080
```

Each repository holds the Q4 and/or Q8 file, `tokenizer.bin`, the license of the original model and a
model card with the exact commands and measured speed.

| Repository (`huggingface.co/miloserdev/...`) | Files | License |
|---|---|---|
| [Qwen3-30B-A3B-Instruct-2507-numallama](https://huggingface.co/miloserdev/Qwen3-30B-A3B-Instruct-2507-numallama) | Q4 19 GB, Q8 32 GB | Apache 2.0 |
| [Qwen3.8-27B-numallama](https://huggingface.co/miloserdev/Qwen3.8-27B-numallama) | Q4 18 GB, Q8 29 GB | Apache 2.0 |
| [Qwen2.5-7B-Instruct-numallama](https://huggingface.co/miloserdev/Qwen2.5-7B-Instruct-numallama) | Q8 8 GB | Apache 2.0 |
| [Qwen2.5-3B-Instruct-numallama](https://huggingface.co/miloserdev/Qwen2.5-3B-Instruct-numallama) | Q4 2.1 GB, Q8 3.3 GB | Qwen Research (non-commercial) |
| [Llama-3.1-8B-Instruct-numallama](https://huggingface.co/miloserdev/Llama-3.1-8B-Instruct-numallama) | Q4 5.5 GB, Q8 8.5 GB | Llama 3.1 Community License |
| [Llama-3.2-3B-Instruct-numallama](https://huggingface.co/miloserdev/Llama-3.2-3B-Instruct-numallama) | Q4 2.2 GB, Q8 3.4 GB | Llama 3.2 Community License |
| [Llama-3.2-1B-Instruct-numallama](https://huggingface.co/miloserdev/Llama-3.2-1B-Instruct-numallama) | Q8 1.3 GB | Llama 3.2 Community License |

Abliterated versions (refusals removed by their authors, same license as the original):
[Qwen3-30B-A3B-Instruct-2507](https://huggingface.co/miloserdev/Qwen3-30B-A3B-Instruct-2507-abliterated-numallama),
[Qwen3.8-27B](https://huggingface.co/miloserdev/Qwen3.8-27B-abliterated-numallama),
[Qwen2.5-7B-Instruct](https://huggingface.co/miloserdev/Qwen2.5-7B-Instruct-abliterated-numallama),
[Llama-3.1-8B-Instruct](https://huggingface.co/miloserdev/Llama-3.1-8B-Instruct-abliterated-numallama),
[Llama-3.2-3B-Instruct](https://huggingface.co/miloserdev/Llama-3.2-3B-Instruct-abliterated-numallama).

Llama models: Built with Llama. Their use is subject to the Llama 3.1 / 3.2 Community License and Meta's
Acceptable Use Policy (included in each repository or linked from its card).

The files are numallama's own format, not GGUF: they do not work with llama.cpp, Ollama or transformers.

### Convert a model yourself

```bash
# 1. build
make                                   # -> ./runq

# 2. get a model from Hugging Face (safetensors) and convert it once
pip install numpy huggingface_hub
hf download Qwen/Qwen3-30B-A3B-Instruct-2507 --local-dir hf/qwen3-30b
python3 scripts/export_hf_q8.py   hf/qwen3-30b qwen3_30b_q80.bin       # int8 weights (~32 GB)
python3 scripts/export_tokenizer.py hf/qwen3-30b qwen3_tokenizer.bin    # not needed for Llama 3 (built in)

# 3. optional, 4-bit: importance statistics from the int8 model, then a Q4 export (~19 GB, faster)
./runq qwen3_30b_q80.bin -z qwen3_tokenizer.bin -m imatrix -i data/calibration.txt -o qwen3_30b.imx
python3 scripts/export_hf_q8.py hf/qwen3-30b qwen3_30b_q4.bin --q4 --imatrix qwen3_30b.imx

# 4. chat (type a message, `exit` to quit); -f gives the model sandboxed ls/cat/grep/find
./runq qwen3_30b_q4.bin -z qwen3_tokenizer.bin -m chat -f config/tools.json -t 0.6
```

At start the chat asks for an optional system prompt (Enter skips it). After every reply it prints the
prompt / generation speed and how much of the context window is used. The tools see only the directory
set by `"root"` in `config/tools.json` (by default the repository); commands run without a shell.

Which model (decode speed on 2 x Altra Max, both sockets):

| Model | File | Speed | Notes |
|---|---|---|---|
| Llama 3.2 3B Instruct, Q8 | 3.4 GB | 76 tok/s | small and fast, built-in tokenizer |
| Qwen3-30B-A3B-Instruct-2507, Q4 | 19 GB | 91 tok/s | mixture of experts: fast and good, recommended for chat |
| Qwen3.8-27B, Q4 | 18 GB | 17 tok/s | dense, the strongest answers; `-r 1` enables reasoning |
| Llama 3.1 8B Instruct, Q8 / Q4 | 8.5 / 5.5 GB | 39 / 59 tok/s | |

One socket only: `-N 1` (or run under `numactl`). Fewer threads: `-T <n>`. Longer context: `-c <tokens>`.

### API server

```bash
./runq qwen3_30b_q4.bin -z qwen3_tokenizer.bin -m server -P 8080 -c 32768 -t 0.7
```

```python
from openai import OpenAI
client = OpenAI(base_url="http://127.0.0.1:8080/v1", api_key="none")
r = client.chat.completions.create(model="any", messages=[{"role": "user", "content": "Hi!"}])
print(r.choices[0].message.content)
```

| Endpoint | Supported |
|---|---|
| `POST /v1/chat/completions` | `messages` (system / developer / user / assistant / tool), `stream` (SSE) with `stream_options.include_usage`, `tools` + `tool_calls` (also streamed), `tool_choice: "none"`, `temperature`, `top_p`, `min_p`, `presence_penalty`, `frequency_penalty`, `seed`, `max_tokens` / `max_completion_tokens`, `stop`; Qwen3.5 / 3.8 reasoning with `reasoning_effort` or `chat_template_kwargs.enable_thinking` (returned as `reasoning_content`). Penalties apply when `temperature > 0`; greedy stays penalty-free so speculative verification remains exact. |
| `GET /v1/models` | the loaded model (named after the file) |
| `GET /v1/sessions` | the known sessions (id, tokens, live) plus the state files on disk |
| `GET /metrics` | uptime, requests, prompt/completion/cached tokens, sessions, active/queued (requires the API key when `-A` is set) |
| `GET /health` | `{"status": "ok"}` |

- Listens on `127.0.0.1` by default; `-H 0.0.0.0` exposes it on the network, `-A <key>` then requires
  `Authorization: Bearer <key>`. There is no TLS: put it behind a reverse proxy for public access.
- **Continuous batching** for dense and MoE models (`-J <n>`, default 4): up to `n` sessions decode
  one token each in one weight-reading pass, every session with its own KV cache. Measured on
  Qwen3-30B-A3B (2 sockets, i8 KV): 4 sessions x 128 tokens give 104-109 tok/s aggregate against
  65-73 tok/s with `-J 1` (1.5-1.6x); 2 sessions give 1.24x. Hybrid Qwen3.5/3.8 and GLM keep the
  serial loop. Prefill is blocking in v1: a new long prompt pauses the other streams for its
  duration (the shared system-prefix slots keep agent tails short); speculative decoding is off in
  the batched path. Each session owns a full `-c` cache (i8: ~0.55 GiB at 32k for Qwen3-30B);
  `-J 1` restores the previous one-request-at-a-time behavior.
- **Operations.** SIGINT/SIGTERM stop the accept loop (active work is not drained in v1).
  `/metrics` reports request/token/cache/active/queue counters; use it for health dashboards and
  autoscaling.
- **Scaling on many cores.** Decode is bandwidth/latency-bound: threads stop helping well before
  256 cores, and oversubscription (`-T 240`) is slower. Qwen3-30B-A3B Q4 one process: `-J 16 -T 128`
  ~229 tok/s, `-J 32` ~238. The useful unit is a **NUMA-local replica** with its own queue and KV
  cache. Measured aggregate: 2 replicas x T64/J16 404, 4 x T32/J16 516, **8 x T16/J16 588** tok/s;
  16 x T8/J16 drops to 365 (too many processes), and 2 x T128 is only 172. Start them with
  `scripts/serve_replicas.sh MODEL TOKENIZER 8 16 16 19000
  8192` (pinned with `numactl --cpunodebind/--membind`) and put
  `scripts/replica_router.py 8080 127.0.0.1:19000 ...` in front: new `session_id`s are assigned
  round-robin and stay sticky, so each conversation keeps its KV on one replica; SSE is relayed
  chunk-by-chunk. The router measured 503 tok/s against 516 direct (~3% overhead). Each replica
  loads its own model copy: budget RAM (Qwen3-30B Q4 ~19 GB each) and leave spare cores for prefill
  or another model.
- The KV cache is kept between requests: a conversation that grows turn by turn only processes the
  new messages (`usage.prompt_tokens_details.cached_tokens`). Hybrid models (Qwen3.5 / 3.8, GLM)
  can only resume from the end of the previous prompt (or the start).
- **Sessions survive a restart.** Every conversation is journaled to `<session_dir>/<id>.jsonl`
  (with the full request bodies) and its token history + model state (KV cache / recurrent state +
  the GLM latent / indexer caches) are dumped to `<session_dir>/<id>.bin` (throttled: on growth by
  2048 tokens or 30 s) so a reconnect after a server restart resumes without re-processing the
  history. The dump is head-major and records the KV format: int8 (the default) keeps the cache
  part 4x smaller (a Qwen3.8-27B session at 131k tokens: 16 GB -> 4 GB). Dumps written by an older
  build (format v1) are ignored and rebuilt. The session id comes from the request's `session_id` / `conversation_id` field or the
  `x-opencode-session-id` (also `x-session-id`, `x-conversation-id`) header; without one, a single
  `default` session is used. Sessions also keep an in-memory snapshot: switching between
  conversations (and resuming a dumped one) is a memory copy, not a re-prefill. With continuous
  batching (`-J > 1`) each active session owns its cache and keeps it **resident across turns**, so
  a normal follow-up pays no cache allocation, no disk restore and no dump. The resident set is
  LRU-capped by available RAM (`RUNQ_KV_RESIDENT_MB`; default a quarter of `MemAvailable`, at most
  32 GiB); a cache is dumped every `RUNQ_DUMP_SECS` seconds (default 300) and when it is evicted.
  `-W <dir>` sets the
  session directory (default `workspace/sessions`, `-W none` disables). `GET /v1/sessions` lists
  the known sessions. Clients like opencode send their session header automatically, so an opencode
  conversation can be resumed after restarting the server. Streaming responses send the headers
  immediately and keep-alive comments during prefill, so slow first tokens don't hit client
  timeouts.
- **The system prompt is processed once.** Agent clients send the same fat system prompt (tools +
  instructions, often >10k tokens) in every session. The server captures the model state at the end
  of that prefix (up to 8 distinct prefixes) and restores it for any session sharing it, so the
  first request of a new opencode session processes only its own tail — a ~5-minute prefill of an
  11k-token system prompt becomes a sub-second state load. Only prefixes of at least 2048 tokens
  take a slot, so a short title/side request cannot evict an agent preamble.
- The client runs the tools; the `-f` sandbox is used only by the CLI chat.
- Not supported: `/v1/completions`, `/v1/embeddings`, images and audio, `n` > 1, `logprobs`,
  `response_format` (JSON mode), forcing a call with `tool_choice: "required"`.
- `tests/server_test.py` checks all of this with the official `openai` Python client.

## Layout

| Path | Contents |
|---|---|
| `src/runq.c` + `src/*.h` | the engine as one translation unit: model loading, NUMA placement, thread pool, kernels, forward passes, chat, server (`AGENTS.md` maps the headers) |
| `src/tools.h` | tool calling: minimal JSON parser, `tools.json` loading, sandboxed command execution |
| `src/server.h` | OpenAI-compatible HTTP server (`-m server`) |
| `scripts/export_hf_q8.py` | Hugging Face safetensors → `.bin` (Q8 / Q4, optional SmoothQuant, numpy only) |
| `scripts/export_tokenizer.py` | `tokenizer.json` → `tokenizer.bin` |
| `scripts/export_inkling.py` | Inkling-2-Mini safetensors → `INK2JSON` (Q4 default, `--experts q8`) |
| `scripts/compare_inkling_logits.py` | oracle/candidate logits: top-1, KL, top-10, correlation |
| `scripts/calibrate.py` | fp32 numpy activation statistics (max \|x\| for `--smooth`) |
| `data/calibration.txt` | calibration text for `-m imatrix` (English, Russian, Chinese, code) |
| `config/tools.json` | tools offered to the model in chat mode |
| `data/tokenizer.bin` | Llama 3 tokenizer |
| `tests/` | fp32 numpy reference, tokenizer reference, engine consistency checks |
| `legacy/` | the original upstream fp32 runtime and PyTorch export scripts, for reference |

## Build

```bash
make            # ./runq          (-Ofast -mcpu=native -pthread)
make prof       # ./runq_prof     per-phase timing report at exit
make tests      # tests/*
```

Linux only (pthreads, NUMA syscalls, futex). AArch64 with dotprod gets the NEON kernels; other CPUs
use portable C fallbacks.

## Models

```bash
# Llama 3.x: weights + the bundled tokenizer
python3 scripts/export_hf_q8.py /path/to/Llama-3.1-8B-Instruct llama31_8b_q80.bin
# 4-bit: collect the importance matrix with the Q8 model, then export (wv stays Q8 by default)
./runq llama31_8b_q80.bin -m imatrix -i data/calibration.txt -o llama31_8b.imx
python3 scripts/export_hf_q8.py /path/to/Llama-3.1-8B-Instruct llama31_8b_q4.bin --q4 --imatrix llama31_8b.imx
python3 scripts/export_hf_q8.py /path/to/model model_q4.bin --q4 wq,wk,wo,w1,w3   # explicit kinds (w2 is the most sensitive)

# Qwen3-MoE (e.g. Qwen3-30B-A3B-Instruct-2507): ~32 GB in Q8
python3 scripts/export_hf_q8.py /path/to/Qwen3-30B-A3B-Instruct-2507 qwen3_30b_a3b_q80.bin
python3 scripts/export_tokenizer.py /path/to/Qwen3-30B-A3B-Instruct-2507 qwen3_tokenizer.bin
# ... and in Q4 (~17 GB; per-expert importance; EXPORT_PROCS limits the quantizer processes)
./runq qwen3_30b_a3b_q80.bin -z qwen3_tokenizer.bin -m imatrix -i data/calibration.txt -o qwen3_30b.imx
EXPORT_PROCS=24 python3 scripts/export_hf_q8.py /path/to/Qwen3-30B-A3B-Instruct-2507 qwen3_30b_a3b_q4.bin --q4 --imatrix qwen3_30b.imx

# Qwen3.8 dense (hybrid linear attention), e.g. Qwen3.8-27B: Q8 ~29 GB, Q4 ~17 GB
python3 scripts/export_hf_q8.py /path/to/Qwen3.8-27B qwen38_27b_q80.bin
python3 scripts/export_tokenizer.py /path/to/Qwen3.8-27B qwen38_tokenizer.bin
./runq qwen38_27b_q80.bin -z qwen38_tokenizer.bin -m imatrix -i data/calibration.txt -o qwen38_27b.imx
python3 scripts/export_hf_q8.py /path/to/Qwen3.8-27B qwen38_27b_q4.bin --q4 --imatrix qwen38_27b.imx

# Qwen2.5: calibrate, export with SmoothQuant, export its tokenizer
python3 scripts/calibrate.py /path/to/Qwen2.5-7B-Instruct calib.txt qwen7b.npz
python3 scripts/export_hf_q8.py /path/to/Qwen2.5-7B-Instruct qwen7b_q80.bin --imatrix qwen7b.npz --smooth 0.5
python3 scripts/export_tokenizer.py /path/to/Qwen2.5-7B-Instruct qwen7b_tokenizer.bin
```

**Calibration text.** `-m imatrix` only measures which input channels of each layer carry the most
signal; Q4 rounding then keeps the error small on those channels. It does not train the model or
change the language it answers in. `data/calibration.txt` (~23k tokens) is about one third English,
one third Russian, and the rest Chinese and code (C, Python, shell), so a Q4 model keeps its quality
in all three languages. If you
mostly use another language or domain, append your own text (a few thousand tokens per language is
enough) or pass a different file with `-i`.

`calib.txt` is any natural text of a few thousand words (a mix of the languages you use). Collect
`-m imatrix` statistics on a model exported without `--smooth`. Q4 files of the old symmetric format
are refused: re-export them.

## Run

```bash
# chat (Llama 3 tokenizer is the default: data/tokenizer.bin)
./runq llama31_8b_q80.bin -m chat -t 0.7

# chat with tools, Qwen tokenizer
./runq qwen7b_q80.bin -z qwen7b_tokenizer.bin -m chat -f config/tools.json -t 0.6

# speculative decoding with a draft model (same tokenizer, smaller model)
./runq llama31_8b_q80.bin -m chat -d llama32_1b_q80.bin

# plain generation
./runq llama31_8b_q80.bin -t 0 -n 256 -i "Once upon a time"
```

Inkling-2-Mini uses a separate `INK2JSON` container (text backbone only; see
`scripts/export_inkling.py`). `runq` auto-detects it for raw generation, chat and the HTTP server.
Provenance, container sizes, the quality table and known limitations are in
[`docs/INKLING.md`](docs/INKLING.md); the published Q4/Q8 containers are at
[miloserdev/Inkling-2-Mini-numallama](https://huggingface.co/miloserdev/Inkling-2-Mini-numallama):

```bash
./runq inkling_mini_q4.ink2 -z inkling2_tokenizer.bin -m generate -i "The capital of France is" -n 16 -t 0
./runq inkling_mini_q4.ink2 -z inkling2_tokenizer.bin -m chat -i "What is the capital of France?" -n 128 -t 0
./runq inkling_mini_q4.ink2 -z inkling2_tokenizer.bin -m server -P 8080 -c 8192
```

`scripts/export_inkling.py` defaults to Q4 experts (17.0 GB container); `--experts q8` keeps the
dequantized NVFP4/MXFP8 source at 8 bits (27.7 GB). `tests/check_inkling` writes
`/dev/shm/inkling2/logits_ours.bin`; compare it with the llama.cpp oracle using
`scripts/compare_inkling_logits.py oracle.bin ours.bin`. On the fixed "The capital of France is"
prompt both containers keep top-1 Paris and 10/10 top-10 overlap; Q8 has KL 0.0535 vs 0.0594 for
Q4 against the IQ4_NL oracle, and Q4-vs-Q8 KL is 0.0083 — expert quantization is a small part of
the remaining implementation/format gap.

The Inkling server handles one request at a time and keeps one multi-turn session cache (prompt
tokens + 48-slot state + last logits); a client that sends the previous assistant turn's
`reasoning_content` and `content` reuses it (new `session_id`s reset the cache). Streaming uses SSE
with keep-alives during prefill and reports `reasoning_content` separately from `content`;
`stop`, `min_p`, presence/frequency penalties, seeds and `stream_options.include_usage` are
supported. `/metrics` exposes requests/tokens/cache hits/errors, and SIGINT/SIGTERM trigger a
graceful shutdown. Run several instances behind `scripts/replica_router.py` for concurrency.
`-T` and `-J` do not apply to the Inkling forward yet (it is single-threaded). Because its prefill
is token-by-token, requests longer than `INKLING_MAX_PROMPT` (default 4096) are rejected with a
clear 400 instead of hanging; set `INKLING_MAX_PROMPT=0` to disable the guard. For agent clients
(opencode) use the batched Qwen/dense server.

| Option | Meaning |
|---|---|
| `-T <n>` | threads (default 0 = all idle CPUs of the used NUMA nodes, at most 96 per node) |
| `-N <n>` | NUMA nodes to use (default 0 = all); weights are split between them |
| `-c <n>` | context window (KV cache size), default 8192 |
| `-K i8\|f32` | KV cache format: `int8` (default) with per-64 group scales and int8 dot products, or `f32` (full precision, ~4x more memory) |
| `-k <n>` | max prompt-lookup draft length, default 8, `0` = off (adaptive for MoE models; off for hybrid models: a recurrent state cannot drop rejected drafts) |
| `-m server`, `-H`, `-P`, `-A`, `-W` | OpenAI-compatible API server, listen address (default 127.0.0.1), port (default 8080), API key, sessions directory |
| `-J <n>` | server: concurrent decode sessions for dense/MoE continuous batching, default 4 (`1` = serial) |
| `-r <0\|1>` | Qwen3.5 / 3.8: `1` = reasoning (thinking shown dimmed), default `0` = answer directly |
| `-o <file>` | output of `-m imatrix` (importance statistics for `--q4 --imatrix`) |
| `-d <file>` | draft model for speculative decoding |
| `-f <file>` | tools file, enables tool calling in chat |
| `-t`, `-p`, `-s` | temperature, top-p, seed |
| `-y`, `-i` | system prompt, first user message (chat) / prompt (generate) |

After every reply the chat prints `[prompt N tok X tok/s | reply M tok Y tok/s | context a/b | draft accepted c/d]`
to stderr. Thread placement: `RUNQ_PIN=1` keeps threads pinned, `RUNQ_PIN=0` disables placement.
`RUNQ_BARBENCH=1` prints the latency of the node and cross-node barriers at start-up.
`RUNQ_KV_RESIDENT_MB` and `RUNQ_DUMP_SECS` set the resident session-KV budget and the dump interval
of the continuous-batching server.

For Russian (and other non-English text) with small models keep the temperature around 0.6–0.7.

## Tests

```bash
make tests
# logits vs an independent fp32 numpy reference (KL, top-1 agreement)
tests/dump_logits model.bin data/tokenizer.bin 64 logits.bin "some text" > ids.txt
python3 tests/ref_logits.py /path/to/hf-model ids.txt logits.bin
# tokenizer vs reference BPE built from tokenizer.json (NDIG=1 for Qwen)
tests/encode data/tokenizer.bin 128256 0 < corpus.txt > c.txt
TOKJSON=/path/to/tokenizer.json python3 tests/tok_ref.py < corpus.txt > p.txt && diff c.txt p.txt
# batched prefill / multi-token step / draft-model loop vs plain decoding
tests/check_batch model.bin 64 300
tests/check_multi model.bin
tests/check_draft main.bin draft.bin
# OpenAI-compatible server, with the official client (pip install openai)
./runq model.bin -m server -P 18080 & python3 tests/server_test.py http://127.0.0.1:18080/v1
```

## License

The code is MIT licensed (see `LICENSE`), as the upstream projects
[llama2.c](https://github.com/karpathy/llama2.c) and [llama3.c](https://github.com/jameswdelancey/llama3.c).

`data/tokenizer.bin` is converted from the Meta Llama 3 tokenizer and is subject to the
[Llama 3 Community License](https://www.llama.com/llama3/license/), not to the MIT license.
Model weights are not part of this repository; converted models keep the licenses of their originals.
