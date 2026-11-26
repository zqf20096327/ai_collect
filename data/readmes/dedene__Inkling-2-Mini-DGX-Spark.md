# Inkling 2 Mini on a single DGX Spark (vLLM, Docker Compose)

Serve [Inkling 2 Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini) from Thinking Machines on one NVIDIA DGX Spark with vLLM. One command downloads the pinned first-party checkpoint and starts an OpenAI-compatible API with text, images, reasoning and tool calls.

Inkling 2 Mini is a looped mixture-of-experts model: 26.4B parameters in total, 3.4B active per token, 128 experts with 8 active. Its 24 layers split into a prelude (0-5), a loop core (6-17) that runs three times with shared weights, and a coda (18-23), so each token reads about 5.4B effective active weights. Attention mixes 20 sliding-window and 4 full-attention layers, and a ViT handles images. The checkpoint ships in its trained precision, NVFP4 experts plus MXFP8 in the last four layers, 20.2 GB with the bundled DSpark drafter. The model goes to 1M tokens of context; on the Spark this recipe serves 262,144, the cap in vLLM's own recipe.

**Hardware:** DGX Spark (GB10, sm_121, aarch64), driver 580, CUDA 13, Docker with the NVIDIA Container Toolkit and Compose v2. About 25 GB free disk for the weights plus ~20 GB for the image. The server takes about 56 GB: 19.1 GiB of weights, a fixed 32 GiB KV cache (327,101 tokens) and engine overhead, so it fits next to something else on the box.

## Quickstart

```bash
git clone https://github.com/dedene/Inkling-2-Mini-DGX-Spark.git
cd Inkling-2-Mini-DGX-Spark
docker compose up -d --wait     # download 20 GB (first run only), load, wait until healthy
tools/check.py                  # model id, reasoning effort, tool call and round trip, streaming, Dutch, an image
docker compose down
```

A cold start takes about 4 minutes here: 100 s to load the weights, 2 minutes to build the KV cache and warm up. `up --wait` returns once `/health` answers.

The API is at `http://<spark-ip>:8888/v1`, model `inkling-2-mini`. It also answers to `local-ai`, so clients set up for another model on this port keep working.

```bash
curl http://<spark-ip>:8888/v1/chat/completions -H 'Content-Type: application/json' -d '{
  "model": "inkling-2-mini",
  "reasoning_effort": "low",
  "max_tokens": 4096,
  "messages": [{"role": "user", "content": "Wat is de hoofdstad van West-Vlaanderen?"}]
}'
```

**Thinking.** The chat template has no `enable_thinking` switch. It reads `reasoning_effort`: `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, `max`, or a number from 0.0 to 0.99. A request sends it top-level or in `chat_template_kwargs`. Without it the template uses 0.9, and that is what a client that sends nothing gets. `REASONING_EFFORT` changes the server default. Even `none` doesn't switch thinking fully off. The reasoning comes back in `message.reasoning_content`.

**Set a token limit.** The model card warns that the model can get stuck in long reasoning loops that repeat, mostly while debugging code. Send `max_tokens` and cap the number of agent turns.

## How it is put together

- **`compose.yaml`:** the `download` service runs `tools/download.sh` (`hf download` of the pinned revision) and exits, then `inkling` serves from the host's Hugging Face cache. A healthcheck hits `/health`.
- **`tools/serve.sh`:** `vllm serve` with the `inkling` reasoning and tool-call parsers, DSpark speculative decoding (7 draft tokens, as the vLLM recipe), prefix caching, a fixed KV cache size and a fixed GPU memory threshold. It checks every setting before it starts.
- **`tools/check.py`:** functional checks, plus `--needle N` for a long-context recall test.
- The image is vLLM's day-0 build [`vllm/vllm-openai:inkling-2-mini`](https://hub.docker.com/r/vllm/vllm-openai/tags), pinned by digest. The model support (vllm-project/vllm#69028) is not in a release yet. There is no Dockerfile.

## Configuration

Copy `.env.example` to `.env` and uncomment what you want to change, then `docker compose up -d --wait` again.

| Variable | Default | |
|---|---|---|
| `REASONING_EFFORT` | empty | Server-wide thinking effort; empty = the template default, 0.9. |
| `SPEC` | `dspark` | `dspark` (the bundled drafter) or `none`. |
| `VISION` | `on` | `off` refuses images (`--limit-mm-per-prompt image:0`). |
| `CONTEXT` | 262144 | Tokens per sequence. |
| `PARALLEL` | 8 | Concurrent sequences. For spark-bench-kit: `PARALLEL=4`. |
| `BATCHED_TOKENS` | 8192 | Chunked-prefill size (see Notes). |
| `KV_CACHE_GIB` | 32 | KV cache size, about 69 KB per token. |
| `GPU_UTIL` | 0.7 | Only a start check here: vLLM refuses to start when less than this share of the 121.6 GiB is free, even with a fixed KV size. The image's own 0.92 fails as soon as anything else holds 10 GB. |
| `PORT`, `HOST`, `SERVED_NAME`, `ALIAS` | 8888, 0.0.0.0, inkling-2-mini, local-ai | |
| `API_KEY` | empty | Bearer token, when set. |
| `RESTART` | `no` | `unless-stopped` to survive a reboot. |
| `VLLM_IMAGE`, `MODEL_REVISION` | pinned | Re-run `tools/check.py` after a bump. |

## Notes

- **Port 8888** is the same port the other recipes in this series use. Stop the other server first, or set `PORT`.
- **The API is open on your LAN** (`HOST=0.0.0.0`, no key). Set `API_KEY` or `HOST=127.0.0.1` if that matters.
- **sm_121 limits** (vllm-project/vllm#69012): from 2,048 tokens per step the router's `k_group_partials` kernel needs 196,868 B of shared memory, and GB10 allows 101,376 B per block, so the engine dies in warmup. The day-0 image already avoids that path on sm_120/121 (no TMA kernel, 2 stages), and starts at `BATCHED_TOKENS=8192`. Set 1024 if a later image brings the crash back; the fix on main is vllm-project/vllm#69021.
- **Tool history:** the template refuses tool-call arguments as a JSON string; `tools/check.py` sends them that way, like OpenAI clients do, to make sure vLLM converts them first.
- **Languages:** the card says quality is lower outside English.

## As an agent: benchmark results

I ran Inkling 2 Mini through the same agent benchmark as every model on this Spark, on 21 November 2026, the day after
its release. Same box, same samples, temperature 0, 32,768 output tokens, four requests in flight, no
`reasoning_effort`, so the template default of 0.9: what a client that sends nothing gets. The suites are the standard
[Inspect](https://inspect.aisi.org.uk/) tasks from inspect_evals 0.24.0. Brackets are the 95% interval. The other two
columns are Qwen3.8 Flash Next, thinking on: on Hibana, the model our agent uses on this Spark now, and on TensorFold,
the reference setup before it.

| | Inkling 2 Mini (vLLM + DSpark, effort 0.9) | Qwen3.8 Flash Next (Hibana `fast` + MTP) | Qwen3.8 Flash Next (TensorFold + MTP) |
|---|---:|---:|---:|
| Mail, calendar and files: attacks executed, n=113 (lower is better) | **0/113** (0–3) | **0/113** (0–3) | **0/113** (0–3) |
| Mail, calendar and files: user data disclosed, n=113 (lower is better) | **0/113** (0–3) | **0/113** (0–3) | **0/113** (0–3) |
| All suites: attacks executed as scored, n=200 (lower is better) | 6/200 (1–6) ² | **1/200** (0–3) | **1/200** (0–3) |
| All suites: user data disclosed, n=200 (lower is better) | **0/200** (0–2) | **0/200** (0–2) | **0/200** (0–2) |
| AgentDojo, task done and attack ignored, n=200 | 71.5 (65–77) | 77.0 (71–82) | **85.5** (80–90) |
| AgentDojo, tasks done without an attack, n=96 | 79.2 (70–86) | 84.4 (76–90) | **88.5** (81–93) |
| BFCL single-turn, n=500 | **86.8** (84–89) | **87.2** (84–90) | **85.8** (82–89) |
| Scripted loop, steps per minute (latency only, no outcome scored) | 8.1 | **15.4** | 9.1 |
| Decode, tok/s weighted over code, prose and tool calls | 43.2 | **106.4** | 49.1 ¹ |
| Decode, Dutch prose, tok/s | 28.5 | **86.8** | 42.6 ¹ |
| Prefill at ~32k tokens, tok/s | 2,719 | **3,549** | 2,325 ¹ |
| 4 requests at once, tok/s | 81.5 | **233.1** | 97.3 ¹ |
| Server memory | **~56 GB** | ~98 GB | ~75 GB |

¹ The TensorFold run skipped the speed suite; its speed rows come from `tune-qwen38-tf-think` (16 November).
² AgentDojo's own count. Five of the six are the same travel attack, which asks the agent to recommend a hotel. Reading
the answers, Inkling told the user each time that a tool had asked it to recommend the hotel and that it would not. The
scorer only checks whether the hotel's name appears in the answer, so these count. The sixth (Slack: visit a URL
first) is real. Hibana and TensorFold each carried out one other attack.

"Executed" counts attacks that went through as an unauthorised action; "disclosed" counts user data that got out, as a
lower bound, because it matches text word for word. All of it is one English attack template on one mailbox, so a low
count is no proof of safety.

On injection Inkling holds up: no e-mail attack worked, nothing was disclosed, and it called out the injected
instructions to the user instead of quietly ignoring them. Single-turn tool calling is level with both Qwen setups.

It finishes less work. Against Hibana the task rows overlap, so that's within the noise; against TensorFold under attack
(71.5 against 85.5) it is not. It is also the slowest of the three in the agent loop, 59 s for the eight steps against
31 s on Hibana. What it buys is memory: 56 GB for the whole server,
against 75 and 98.

Thinking never fully switches off. `reasoning_effort` reaches the template, but the effect on length is small: on a
train-timetable puzzle `none` used 928 to 1,928 completion tokens and `high` 1,194 to 1,355. In the smoke run one
GPQA question took all 32,768 tokens, re-checking its own working without repeating itself. The model card warns about
exactly this, so cap `max_tokens`.

Unsloth Studio stayed loaded on the same Spark (11 GB, idle) during the whole run, the speed rows included.

## Credits

- [Thinking Machines](https://thinkingmachines.ai/news/inkling-2-mini/) for Inkling 2 Mini, Apache 2.0.
- The vLLM team for day-0 support and the [recipe](https://recipes.vllm.ai/thinkingmachines/Inkling-2-Mini) this one follows.

## License

MIT for this repo. The weights are under Apache 2.0.
