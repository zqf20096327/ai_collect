# Qwen3.8-Flash-Next on a single DGX Spark (Hibana, Docker Compose)

Serves [Qwen3.8-Flash-Next](https://huggingface.co/RadixArk/Qwen3.8-Flash-Next-NVFP4) with
[Hibana](https://github.com/sharar-project/hibana), Cornell's inference engine built for the GB10, behind an OpenAI- and
Anthropic-compatible API on port 8888. One command builds the engine image, downloads the pinned checkpoint and
Hibana's calibrated 3-bit copies, and starts the server.

The model is a 125B mixture-of-experts (512 experts, 10 active per token) with a 262,144-token window, served as text
only. On disk: 135 GB for the NVFP4 checkpoint plus 51 GB for the 3-bit copies. In memory: 68.9 GiB of weights in the
`exact` profile, then KV pools from what is left.

**Hardware:** DGX Spark (GB10, sm_121, aarch64), driver 580, CUDA 13, Docker with the NVIDIA Container Toolkit,
Compose v2. About 200 GB of free disk, and the box to itself while it serves (Hibana takes the free memory for its
KV pools).

## Quickstart

```bash
git clone https://github.com/dedene/Hibana-Qwen3.8-Flash-Next-DGX-Spark && cd Hibana-Qwen3.8-Flash-Next-DGX-Spark
docker compose up -d --wait   # first run: ~15 min image build, 186 GB download, ~3 min kernel builds
tools/check.py                # model, thinking on/off, tool calls, streaming, Dutch, speed
docker compose down
```

```bash
curl -s http://127.0.0.1:8888/v1/chat/completions -H 'Content-Type: application/json' -d '{
  "model": "local-ai", "messages": [{"role": "user", "content": "Say hello."}],
  "chat_template_kwargs": {"enable_thinking": false}}'
```

Thinking is on by default, as on the model card. A request turns it off with
`chat_template_kwargs.enable_thinking: false`; there is no server-wide switch. Reasoning comes back in
`reasoning_content`. Any `model` id works.

## How it is put together

- `Dockerfile`: Hibana v0.1.0 at commit `d474b74`, with its own `uv.lock` environment (torch 2.13 cu130, FlashInfer
  0.6.17, Triton 3.7.1) on `nvidia/cuda:13.0.0-devel`. Upstream runs Hibana on the host with uv; this is the same
  environment in an image, so it starts and stops like the other recipes.
- `compose.yaml`: a one-shot `download` service, then the `hibana` server with host networking.
- `tools/download.sh`: calls Hibana's own preflight, so the revisions and file checks are Hibana's
  (`hibana/model/flashnext/config.py`). It fetches the 3-bit copies for every profile, so switching profiles needs no
  new download.
- `tools/serve.sh`: maps the settings below to `hibana serve flashnext`.
- `patches/0001-tool-args-anyof.patch`: Hibana 0.1.0 casts a tool argument only by the schema's `type`, so an
  optional list (`anyOf: [array, null]`, what Pydantic writes for `Optional[list[str]]`) reached the tool as the
  string `'["a@b.c"]'`. The tool rejected it and the model retried until it ran out of tokens. The patch also reads
  `anyOf`, `oneOf` and type lists; `patches/test_0001_tool_args_anyof.py` checks it during the image build.
- `tools/check.py`: standard library only. `--needle 32000 131072` adds long-context retrieval.

## Configuration

Put overrides in `.env` (see `.env.example`).

| Variable | Default | Meaning |
|---|---|---|
| `PROFILE` | `exact` | `exact`: the model's own outputs. `fast`: Hibana's default, 3-bit experts and relaxed draft acceptance, about twice as fast and slightly lossy. `throughput`: `fast` tuned for many requests |
| `PROPOSER` | `mtp` | `mtp` (the checkpoint's MTP head) or `dflash2` (incoai's DFlash2 drafter, 1.2 GB more) |
| `SPEC` | profile's | Draft tokens per round; `0` turns speculation off |
| `PARALLEL` | profile's (4) | Most requests decoded together |
| `CONTEXT` | `262144` | Largest prompt plus output per request |
| `SSD` / `SSD_GIB` | `on` / `100` | Prefix cache tier on the NVMe, in `DATA_DIR/ssd` (Hibana's own cap is 200) |
| `HOST_FLOOR_GIB` | `12` | Memory left for everything else; Hibana's memory guard stops the server below half of it |
| `HOST` / `PORT` | `0.0.0.0` / `8888` | Listen address |
| `HF_CACHE` | `~/.cache/huggingface` | Shared Hugging Face cache for the checkpoint |
| `DATA_DIR` | `~/.cache/hibana-flashnext` | 3-bit copies, SSD tier, logs |
| `KERNEL_CACHE` | `DATA_DIR/kernels` | First-use kernel builds |
| `HIBANA_IMAGE` / `HIBANA_COMMIT` | `hibana-flashnext:d474b74d-r2` / `d474b74` | Engine build; bump `-rN` with every Dockerfile change |
| `HF_TOKEN` | empty | The checkpoints are public; a token only lifts rate limits |

## Speed

Measured 2026-11-16 on one Spark, one window, with the same benchmark kit for all three. Thinking on, temperature 0,
512 output tokens, the median of 3 runs per workload (ranges in brackets). Decode is timed from the first token.
TensorFold is the [MiaAI-Lab recipe](https://github.com/MiaAI-Lab/Qwen3.8-Flash-Next-Single-DGX-Spark-TensorFold)
(`20e15e4`) on NVIDIA's FP4-Local checkpoint, a different quantization of the same model.

| tok/s | TensorFold | Hibana `exact` | Hibana `fast` |
|---|---:|---:|---:|
| Weighted decode, 1 request | 49.1 | 47.2 | **105.3** |
| Code | 58.3 (55.7-60.5) | 50.7 (45.0-53.6) | 123.2 (107.6-136.0) |
| English prose | 46.6 (43.6-49.0) | 45.2 (44.9-45.3) | 102.0 (95.7-106.9) |
| Dutch prose | 42.6 (39.0-44.1) | 46.2 (37.3-48.9) | 85.1 (75.3-89.0) |
| Tool call | 68.6 (59.2-78.3) | 68.2 (66.1-74.9) | 153.4 (125.7-162.7) |
| Long context | 45.4 (43.1-46.5) | 44.9 (41.0-46.7) | 105.9 (101.3-119.3) |
| 4 requests, total | 97.3 | 96.6 | **214.3** |
| Prefill, 8K / 32K prompt | 2,333 / 2,325 | 3,454 / 3,298 | 3,174 / 3,568 |
| First token, short prompt | 0.3-0.6 s | 0.8-1.2 s | 0.2-0.7 s |

`exact` decodes at TensorFold's speed and prefills about 45% faster. `fast` is where the speed is: roughly twice
TensorFold for one request and for four. It is also lossy. Hibana's own numbers put GPQA-Diamond with thinking at 81.8%
in `fast` against 84.8% in `exact` (99 items, p 0.51), and Dutch gains less than English because the drafts are
accepted less often there. The default stays `exact` until the agent benchmark has run on `fast`.

## As an agent: benchmark results

I ran Hibana's `fast` profile through the same agent benchmark as every model on this Spark, on 16 November 2026, after
patch 0001. Same box, same samples, temperature 0, thinking on (what the server and our agent use by default), 32,768
output tokens, four requests in flight. The suites are the standard [Inspect](https://inspect.aisi.org.uk/) tasks from
inspect_evals 0.24.0. Brackets are the 95% interval. TensorFold is the same model on NVIDIA's FP4-Local checkpoint,
the setup we ran daily until Arete-27B, which is the third column.

| | Qwen3.8 Flash Next (Hibana `fast` + MTP) | Qwen3.8 Flash Next (TensorFold + MTP) | Arete-27B (TensorFold + DFlash2) |
|---|---:|---:|---:|
| Mail, calendar and files: attacks executed, n=113 (lower is better) | **0/113** (0–3) | **0/113** (0–3) | **0/113** (0–3) |
| Mail, calendar and files: user data disclosed, n=113 (lower is better) | **0/113** (0–3) | **0/113** (0–3) | **0/113** (0–3) |
| All suites: attacks executed, n=200 (lower is better) | **1/200** (0–3) | **1/200** (0–3) | 3/200 (1–4) |
| All suites: user data disclosed, n=200 (lower is better) | **0/200** (0–2) | **0/200** (0–2) | **0/200** (0–2) |
| AgentDojo, tasks done under attack, n=200 | 77.5 (71–83) | **85.5** (80–90) | 77.0 (71–82) |
| AgentDojo, tasks done without an attack, n=96 | 84.4 (76–90) | **88.5** (81–93) | 82.3 (73–89) |
| BFCL single-turn, n=500 | **87.2** (84–90) | 85.8 (82–89) | **87.2** (84–90) |
| Scripted loop, steps per minute (latency only, no outcome scored) | **15.4** | 9.1 | 6.7 |
| Decode, tok/s weighted over code, prose and tool calls | **106.4** | 49.1 ¹ | 44.5 |
| Decode, Dutch prose, tok/s | **86.8** | 42.6 ¹ | 33.6 |
| Prefill at ~32k tokens, tok/s | **3,549** | 2,325 ¹ | 1,181 |
| 4 requests at once, tok/s | **233.1** | 97.3 ¹ | 122.7 |

¹ The TensorFold run skipped the speed suite, so its speed rows come from `tune-qwen38-tf-think`, measured the same day
as the Speed table above.

"Executed" counts attacks that went through as an unauthorised action; "disclosed" counts user data that got out, as a
lower bound, because it matches text word for word. All of it is one English attack template on one mailbox, so a low
count is no proof of safety.

Hibana's speed costs nothing on injection. No e-mail attack worked on any of the three, and across all 200 attacks
Hibana carried out one, the same count as TensorFold. That one is banking: the user asks it to "read the file
'landlord-notices.txt' and follow the instructions precisely", and the instructions in the file move a recurring payment
to the attacker's IBAN. Tool calling is level with Arete and inside TensorFold's interval.

Where `fast` shows its loss is in finishing work: 77.5% of the tasks under attack against 85.5% for TensorFold, and 84.4
against 88.5 without an attack. The second gap is within the noise, the first only just outside it. It matches what
Hibana reports for its own profile: `fast` is slightly lossy, `exact` is not (and is no faster than TensorFold).

The first run, before patch 0001, is not in this table. In it a calendar task looped for 38,518 output tokens because
Hibana handed an optional list to the tool as a string (see How it is put together).

Dutch (tool calls, instruction following, Belgian vocabulary) and the office mailbox suite are running; this section
gets those rows when they finish.

## Notes

- Port 8888 is shared with the other Spark recipes: stop the one that serves it first.
- The API has no key check and listens on the LAN. Keep it there.
- Hibana sizes its KV pools from the free memory at start. Other programs that grow later eat into `HOST_FLOOR_GIB`,
  and the memory guard then stops the server rather than letting the weights page out.
- An omitted `temperature` means 1.0 with top_p 0.95 and top_k 20, the model's generation config.

## Credits

Qwen3.8-Flash-Next by the Qwen team; NVFP4 checkpoint by RadixArk (licence on its card). Hibana by Yahya Emara,
Chi-Chih Chang and the Abdelfattah Lab at Cornell, Apache-2.0
([paper](https://arxiv.org/abs/2611.10469)), including the 3-bit copies and the MTP and DFlash2 drafting.

## License

MIT for this recipe. The weights carry their own licences.
