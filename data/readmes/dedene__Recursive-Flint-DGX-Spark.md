# Recursive Flint on a single DGX Spark (llama.cpp, Docker Compose)

Serve [Recursive Flint](https://huggingface.co/RecursiveSI/flint) on one NVIDIA DGX Spark with stock llama.cpp, from the official [NVFP4 GGUF](https://huggingface.co/RecursiveSI/flint-nvfp4-gguf). One command downloads the pinned file and starts an OpenAI-compatible API with reasoning and tool calls.

Flint is Recursive's mixture-of-experts model for coding agents: 39.8B parameters, about 2.5B active per token, 262K context, text only. 35 of its 49 layers use a 513-token sliding window, so the KV cache stays small: the full window costs about 7.5 GB. The NVFP4 GGUF is 22.9 GB.

**Hardware:** DGX Spark (GB10, sm_121, aarch64), driver 580, CUDA 13, Docker with the NVIDIA Container Toolkit and Compose v2. About 25 GB free disk. The server takes about 33 GB, so it fits next to another model on a different port.

## Quickstart

```bash
git clone https://github.com/dedene/Recursive-Flint-DGX-Spark.git
cd Recursive-Flint-DGX-Spark
docker compose up -d --wait     # download 22.9 GB (first run only), load, wait until healthy
tools/check.py                  # model id, answers, reasoning split, tool call, streaming, Dutch
docker compose down
```

The download checks the file's sha256; `up --wait` returns once `/health` answers.

The API is at `http://<spark-ip>:8888/v1`, model `flint`. llama-server answers whatever model id a client sends, so clients set up for `local-ai` work too.

```bash
curl http://<spark-ip>:8888/v1/chat/completions -H 'Content-Type: application/json' -d '{
  "model": "flint",
  "messages": [{"role": "user", "content": "Write a Python function that merges overlapping intervals."}],
  "max_tokens": 32768
}'
```

Flint decides on each turn whether to reason. There is no switch: `enable_thinking` and `reasoning_effort` do nothing. The reasoning comes back in `message.reasoning_content` and counts toward `max_tokens`, so give hard problems at least 32K tokens. Send `reasoning_content` back with the assistant message when you continue a conversation. The server samples with the card's settings (temperature 1.0, top_p 0.95, top_k 20, min_p 0) unless the request sets its own.

## How it is put together

- **`compose.yaml`:** the `download` service fetches the pinned GGUF and checks it, then `flint` serves it. A healthcheck hits `/health`.
- **`tools/download.sh`:** curl of the pinned Hugging Face revision, resumable, sha256 checked. A complete file without a stamp is checked rather than fetched again.
- **`tools/serve.sh`:** `llama-server` with the card's flags: all layers on the GPU, flash attention, f16 KV, the compact sliding-window cache, `--jinja`, plus a 2048-token prefill batch.
- **`tools/check.py`:** functional checks, plus `--needle N` for a long-context recall test.
- The image is the official arm64 CUDA 13 build of llama.cpp (b11804), pinned by digest. Flint support landed one day earlier. There is no Dockerfile.

## Configuration

Copy `.env.example` to `.env` and uncomment what you want to change, then `docker compose up -d --wait` again.

| Variable | Default | |
|---|---|---|
| `CONTEXT` | 262144 | Context llama-server allocates. Slots share it. |
| `PARALLEL` | 1 | Server slots, for concurrent requests. |
| `UBATCH` | 2048 | Prefill micro-batch. |
| `SPEC` | `none` | `ngram` drafts text the reply repeats from the prompt. |
| `TEMP`, `TOP_P`, `TOP_K`, `MIN_P` | 1.0, 0.95, 20, 0 | Server defaults; a request can override them. |
| `PORT`, `HOST`, `SERVED_NAME` | 8888, 0.0.0.0, flint | |
| `API_KEY` | empty | Bearer token, when set. |
| `LLAMA_CPP_IMAGE`, `MODEL_REVISION` | pinned | Re-run `tools/check.py` after a bump. |

## Speed tuning

Four slots, the kit's speed suite, 2 repetitions. Decode is weighted over code, prose and tool calls.

| Setting | Decode, tok/s | Prefill at 27K, tok/s | 4 requests at once, tok/s |
|---|---:|---:|---:|
| llama.cpp defaults (micro-batch 512) | 91.5 | 1,851 | 213 |
| Micro-batch 2048 (**default**) | 91.9 | **2,490** | 212 |
| n-gram drafting | 87.4 | 1,849 | 204 |

A larger micro-batch makes prefill 35% faster and leaves decode alone. n-gram drafting costs 5% on this mix. Flint has no MTP head and no published drafter, so there is nothing else to try for decode.

## Notes

- **Memory.** About 33 GB with one slot and the full 262K window.
- **Long context works.** `check.py --needle 131072` found its key at 110,615 tokens in 58 s.
- **Greedy decoding is not validated by Recursive.** The benchmark below runs at temperature 0, like the other models on this Spark.
- **The API is open on the LAN** unless you set `API_KEY`.

## As an agent: benchmark results

I ran this stack through the same agent benchmark as the other models on this Spark, on 22 and 23 October 2026. Same box, same samples, temperature 0, four requests in flight. The other models ran with thinking off and 4,096 output tokens. Flint can't turn its reasoning off, so it got 32,768 tokens. The suites are the standard [Inspect](https://inspect.aisi.org.uk/) tasks from inspect_evals 0.24.0. Brackets are the 95% interval. The run used llama.cpp's default micro-batch of 512; with the new default of 2048, prefill is about 35% faster.

| | Recursive Flint (NVFP4 GGUF, llama.cpp) | Qwen3.8 Flash Next (NVIDIA FP4-Local, vLLM + MTP) | Ornith-1.5-122B (NVFP4, vLLM + MTP) | Nemotron 3.5 Super VL (NVFP4, vLLM + LiLiCorr) | MiniCPM-V 4.7 (Q8_0, llama.cpp) | Underdog Saluki 27B (IQ2, llama.cpp + DFlash) |
|---|---:|---:|---:|---:|---:|---:|
| BFCL single-turn, n=500 | 80.0 (76–83) | 82.4 | 86.0 | 85.6 | **89.0** | 86.8 |
| BFCL multi-turn, n=200 | 32.0 (26–39) | 54.5 | 51.5 | 49.2 | **63.0** | 48.2 |
| AgentDojo, tasks done without an attack, n=96 | 75.0 (65–83) | 84.4 | 81.2 | 77.1 | **85.4** | 75.0 |
| AgentDojo, attacks resisted, n=200 | 94.5 (90–97) | **99.0** | 87.0 | 81.5 | 64.5 | 88.0 |
| AgentDojo, tasks done under attack, n=200 | 70.5 (64–76) | **82.0** | 71.5 | 64.0 | 64.5 | 64.5 |
| IFEval, prompt strict, n=541 | **94.6** (92–96) | 85.8 | 80.2 | 85.6 | 88.5 | 79.3 |
| Global-MMLU Dutch, n=300 | 79.3 (74–84) | **87.0** | 85.7 | 86.7 | 86.7 | 81.3 |
| GPQA-Diamond, n=198 | 68.7 (62–75) | 64.6 | **72.7** | 56.1 | 69.7 | 49.0 |
| Agent loop, steps per minute (8 tool steps) | **24.8** | 13.8 | 8.4 | 19.2 | 18.3 | 10.1 |
| Decode, tok/s weighted over code, prose and tool calls | **92.7** | 43.6 | 37.0 | 34.6 | 55.7 | 44.9 |
| Decode, Dutch prose, tok/s | **96.1** | 31.7 | 33.1 | 23.6 | 57.3 | 27.3 |
| Prefill at ~32k tokens, tok/s | 1,835 | 2,274 | 2,082 | **2,373** | 1,854 | 704 |
| 4 requests at once, tok/s | **211** | 113 | 82 | 93 | 108 | 88 |
| Memory for the whole server | ~33 GB | ~97 GB | ~101 GB | ~91 GB | ~44 GB | **27.5 GB** |

Flint is the fastest model we've run on this Spark, by a wide margin. Decode runs at 93 tok/s, more than twice Qwen FP4-Local, and it barely slows down in Dutch. In the agent loop it does 24.8 steps per minute, against 13.8 for Qwen, and the wait for the first token stays at 1.5-1.7 s as the conversation grows. It also needs a third of the memory.

It follows instructions better than anything else here: IFEval 94.6, nine points above Qwen. Prompt injection holds up well too. 11 of 200 attacks got through, 4 in banking and 7 in Slack, none in travel or the mail and calendar suite. Qwen let 2 through.

The weak spot is longer tool work. Multi-turn BFCL is 32.0, against 54.5 for Qwen and the lowest score in the table. Flint makes fewer calls before it stops: a median of 6.5 per task, against 9 for Qwen, and 14 turns ran into the 32K-token limit. AgentDojo without an attack lands at 75.0, also at the bottom. Dutch knowledge is weak at 79.3. Asked for the capital of West Flanders, it answered Kortrijk.

So for a Dutch-speaking agent that does long multi-step work, Qwen FP4-Local stays the better choice. For short, fast steps, or next to another model on the same box, Flint is the obvious candidate.

## Credits

- [Recursive](https://huggingface.co/RecursiveSI) for Flint and the NVFP4 GGUF (Apache 2.0). The weights are not in this repository.
- The shape of this repository follows [Kolibri-1-DGX-Spark](https://github.com/dedene/Kolibri-1-DGX-Spark): one Compose project, a pinned download, and a small check.

## License

MIT, see [LICENSE](LICENSE). The model weights are Apache 2.0 by their authors.
