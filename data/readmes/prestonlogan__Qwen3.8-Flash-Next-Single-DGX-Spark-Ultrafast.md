<p align="center">
  <img alt="Qwen3.8-Flash-Next on one NVIDIA DGX Spark: 101 tok/s on prose, 2.2× the typical Flash-Next setup on the same box. 133 tok/s on code, 253 tok/s total across 4 requests, about 3,300 tok/s prefill at 8K–32K. Bar chart of decode speed against the typical recipe (TensorFold, NVFP4 + MTP): prose 101.3 vs 46.6, code 133.3 vs 58.3, 4 requests 252.9 vs 97.3." src="media/header.png">
</p>

<p align="center">
  <a href="#quickstart">Quickstart</a> · <a href="#speed">Speed</a> · <a href="#quality-and-limits">Quality</a> · <a href="docs/optimization-notes.md">Optimization notes</a> · <a href="https://github.com/dedene/Hibana-Qwen3.8-Flash-Next-DGX-Spark">Built on dedene's recipe</a>
</p>

<p align="center">
  <a href="https://x.com/iamprestonlogan"><img alt="Follow @iamprestonlogan on X" src="https://img.shields.io/badge/Follow-%40iamprestonlogan-000000?style=for-the-badge&logo=x&logoColor=white"></a>
</p>

Most Qwen3.8-Flash-Next recipes reach ~45–50 tok/s on a Spark (vLLM/SGLang/TensorFold with NVFP4 + MTP). This one runs
[Hibana](https://github.com/sharar-project/hibana), Cornell's GB10 inference engine, in its `fast` profile,
and adds **image input** for Flash-Next, which upstream Hibana does not load. OpenAI- and Anthropic-compatible API on
port 8888, thinking and tool calls included.

> Built on [**dedene/Hibana-Qwen3.8-Flash-Next-DGX-Spark**](https://github.com/dedene/Hibana-Qwen3.8-Flash-Next-DGX-Spark)
> by Peter Dedene, which did the Hibana Docker recipe, the tool-call fix and the speed and agent benchmarks below. This
> repo adds two Hibana patches for images and ships the `fast` profile by default. If you only need text, dedene's
> recipe with `PROFILE=fast` gives the same text speed.

*Real time, no speed-up: this recipe doing an agentic coding task in DeepSeek Harness (reasoning effort Low, thinking expanded). Jump cuts skip pauses while tool calls run. [MP4](media/dsh-agentic-demo.mp4)*

[![This recipe running an agentic coding task in DeepSeek Harness: reasoning, tool calls and code streaming in real time](media/dsh-agentic-demo.gif)](media/dsh-agentic-demo.mp4)

## Speed

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="media/speed-chart-dark.png">
  <img alt="Bar chart: this recipe streams 101.3 tok/s on English prose vs 46.6 for a typical recipe, 133.3 vs 58.3 on code, 101.8 on prose about an image, and 252.9 vs 97.3 total with 4 requests at once" src="media/speed-chart-light.png">
</picture>

<details>
<summary><b>Exact numbers</b></summary>

| tok/s, one DGX Spark | Typical recipe (TensorFold, NVFP4 + MTP) | Hibana `exact` | **This recipe** (Hibana `fast` + images) |
|---|---:|---:|---:|
| English prose, 1 request | 46.6 | 45.2 | **101.3** |
| Code, 1 request | 58.3 | 50.7 | **133.3** |
| Prose about an image, 1 request | no images | no images | **101.8** |
| 4 requests at once, total | 97.3 | 96.6 | **252.9** |
| Prose, sampled (temperature 1.0), 1 request | | | 82.2 |
| Code, sampled (temperature 1.0), 1 request | | | 114.3 |
| Prose about an image, sampled, 1 request | | | 84.5 |
| 4 requests, sampled, total | | | 204.2 |

</details>

Decode speed, timed from the first output token, thinking on (the default). Temperature 0 unless marked, 512 output
tokens (1,024 for sampled rows), median of 3 runs (5 for single sampled rows). This recipe's column was measured
2026-11-20 on its default settings (`PROFILE=fast`, `VISION=1`, `DRAFT_VOCAB=131072`). The TensorFold and `exact`
columns are dedene's measurements from 2026-11-16
([MiaAI-Lab TensorFold recipe](https://github.com/MiaAI-Lab/Qwen3.8-Flash-Next-Single-DGX-Spark-TensorFold) on NVIDIA's
FP4-Local checkpoint), same prompt types and method. dedene measured Hibana `fast` at 102.0 on prose and 123.2 on code
without the draft-vocabulary setting, so the text speed is Hibana's, not this repo's.

Sampled requests are slower because fewer drafted tokens survive verification at temperature 1.0. Prefill is
~3,200–3,500 tok/s at 8K–32K prompts (dedene's numbers).

### Why it is fast

Hibana's `fast` profile serves the 512 experts as calibrated 3-bit copies and the trunk in FP8, so each token reads far
fewer bytes from the Spark's 273 GB/s memory. The checkpoint's MTP head drafts several tokens per step, and the model
verifies them in one pass. In `fast`, sampled requests also accept a drafted token when the model gives it a
probability close to its own choice (`accept_soft` 0.5) instead of only on an exact match.

## Quickstart

**Hardware:** DGX Spark (GB10, sm_121, aarch64), driver 580, CUDA 13, Docker with the NVIDIA Container Toolkit,
Compose v2. About 200 GB of free disk, and the box to itself while it serves (Hibana sizes its KV pools from the free
memory).

```bash
git clone https://github.com/prestonlogan/Qwen3.8-Flash-Next-Single-DGX-Spark-Ultrafast && cd Qwen3.8-Flash-Next-Single-DGX-Spark-Ultrafast
docker compose up -d --wait   # first run: ~15 min image build, 186 GB download, ~3 min kernel builds
tools/check.py                # thinking, tool calls, streaming, image input, speed
docker compose down
```

Text:

```bash
curl -s http://127.0.0.1:8888/v1/chat/completions -H 'Content-Type: application/json' -d '{
  "model": "local-ai", "messages": [{"role": "user", "content": "Say hello."}],
  "chat_template_kwargs": {"enable_thinking": false}}'
```

Image (inline base64 only; the server does not fetch URLs):

```bash
IMG=$(base64 -w0 photo.jpg)   # macOS: base64 -i photo.jpg
curl -s http://127.0.0.1:8888/v1/chat/completions -H 'Content-Type: application/json' -d '{
  "model": "local-ai", "chat_template_kwargs": {"enable_thinking": false},
  "messages": [{"role": "user", "content": [
    {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,'"$IMG"'"}},
    {"type": "text", "text": "What is in this picture?"}]}]}'
```

Thinking is on by default, as on the model card. A request turns it off with
`chat_template_kwargs.enable_thinking: false`. Reasoning comes back in `reasoning_content`. Any `model` id works.
Anthropic-style `image` blocks with a base64 source work too.

## What this repo adds to dedene's recipe

| | dedene's recipe | This recipe |
|---|---|---|
| Default profile | `exact` (lossless, ~47 tok/s) | `fast` (~101 tok/s, slightly lossy) |
| Image input | no (vision tower not loaded) | **yes** (`patches/0002`, `patches/0003`) |
| Image requests use MTP drafting and CUDA graphs | — | yes |
| Draft vocabulary shortlist | off | on (`DRAFT_VOCAB=131072`) |
| Tool-argument fix (`patches/0001`) | yes | yes (dedene's) |

- `patches/0002-flashnext-vision.patch`: loads the checkpoint's Qwen vision tower and projector, expands image
  placeholders, and gives image tokens their multimodal (M-RoPE) positions in attention and the sparse indexer.
- `patches/0003-vision-speculation-graphs.patch`: image requests keep MTP speculative decoding and run the captured
  CUDA graphs instead of one eager pass per token. With patch 0002 alone, image prose decoded at about 36 tok/s in
  our tests (temperature 0, thinking off); with both patches it runs at text speed. Text requests take the same code
  paths as before.

Both patches apply to Hibana `d474b74` (v0.1.0) and are applied during the image build.

## Settings

Put overrides in `.env` (see `.env.example`).

| Variable | Default | Meaning |
|---|---|---|
| `PROFILE` | `fast` | `fast`: 3-bit experts, relaxed acceptance, ~2× faster, slightly lossy. `exact`: the model's own outputs. `throughput`: `fast` tuned for many requests |
| `VISION` | `1` | `1` loads the vision tower (0.84 GiB) and accepts images; `0` serves text only |
| `DRAFT_VOCAB` | `131072` | The drafter picks from the 131,072 most common tokens (+3–10% on English and code in our tests); verification still uses the full vocabulary. Set `0` for mostly non-English text |
| `PROPOSER` | `mtp` | `mtp` (the checkpoint's MTP head) or `dflash2` (incoai's DFlash2 drafter, 1.2 GB more; not tested with images) |
| `SPEC` | profile's | Draft tokens per round; `0` turns speculation off |
| `PARALLEL` | profile's (4) | Most requests decoded together |
| `CONTEXT` | `262144` | Largest prompt plus output per request |
| `SSD` / `SSD_GIB` | `on` / `100` | Prefix cache tier on the NVMe, in `DATA_DIR/ssd` |
| `HOST_FLOOR_GIB` | `12` | Memory left for everything else; Hibana's memory guard stops the server below half of it |
| `HOST` / `PORT` | `0.0.0.0` / `8888` | Listen address |
| `HF_CACHE` | `~/.cache/huggingface` | Shared Hugging Face cache for the checkpoint |
| `DATA_DIR` | `~/.cache/hibana-flashnext` | 3-bit copies, SSD tier, logs |
| `HIBANA_IMAGE` | `hibana-flashnext-vision:d474b74d-v1` | Engine image tag |

## Quality and limits

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="media/quality-chart-dark.png">
  <img alt="Quality panels: GPQA-Diamond 81.8% fast vs 84.8% exact (p 0.51); BFCL 87.2 fast vs 85.8 TensorFold; AgentDojo 77.5 vs 85.5; injection attacks executed 1 of 200 for both" src="media/quality-chart-light.png">
</picture>

- **`fast` is slightly lossy.** Hibana's authors measured GPQA-Diamond with thinking at 81.8% in `fast` against 84.8% in
  `exact` (99 questions, p 0.51), with answers 18% longer. dedene's agent benchmark on `fast`: BFCL single-turn 87.2
  (TensorFold 85.8), AgentDojo tasks done under attack 77.5 (TensorFold 85.5), 1 of 200 injection attacks executed (same
  as TensorFold). Use `PROFILE=exact` when you need the model's exact outputs.
- **Don't raise `HIBANA_ACCEPT_SOFT` above 0.5.** At 1.0–3.0 decoding is 20–60% faster, but in our tests long thinking
  fell into repetition loops and ended with no answer in 1 of 5 to 1 of 3 runs of an agent task. 0.5 had none.
  Hibana's authors use 0.5 for Flash-Next too.
- **Images:** inline base64 only, up to 32 MiB encoded and 100 per request, each resized to at most 1,048,576 pixels.
  No video. One Spark only (no two-Spark tensor parallel with vision). Checked with our own text and image prompts
  (`tools/check.py` and a 22-prompt correctness set); no standard image benchmark (MMMU, ChartQA) has been run yet.
- **Non-English text:** the draft-vocabulary shortlist lowers draft acceptance on scripts outside the common tokens.
  Set `DRAFT_VOCAB=0` if most of your traffic is not English or code. Hibana leaves it off for this reason.
- Port 8888 is shared with other Spark recipes: stop the one that serves it first.
- The API has no key check and listens on the LAN. Keep it there.
- An omitted `temperature` means 1.0 with top_p 0.95 and top_k 20, the model's generation config.

## How it is put together

- `Dockerfile`: Hibana v0.1.0 at commit `d474b74` with its own `uv.lock` environment (torch 2.13 cu130, FlashInfer
  0.6.17, Triton 3.7.1) on `nvidia/cuda:13.0.0-devel`, then patches 0001–0003.
- `compose.yaml`: a one-shot `download` service, then the `hibana` server with host networking.
- `tools/download.sh`: Hibana's own preflight fetches the pinned checkpoint and 3-bit copies for every profile.
- `tools/serve.sh`: maps the settings above to `hibana serve flashnext`.
- `tools/check.py`: standard library only. `--needle 32000 131072` adds long-context retrieval.
- `docs/optimization-notes.md`: every change we measured, what we kept, what we rejected and why, with the numbers.

## Credits

- **[dedene/Hibana-Qwen3.8-Flash-Next-DGX-Spark](https://github.com/dedene/Hibana-Qwen3.8-Flash-Next-DGX-Spark)** by
  Peter Dedene (MIT): the Docker recipe this repo is built from, patch 0001, and the TensorFold, `exact` and agent
  benchmark numbers quoted above.
- **[Hibana](https://github.com/sharar-project/hibana)** by Yahya Emara, Chi-Chih Chang and the Abdelfattah Lab at
  Cornell (Apache-2.0, [paper](https://arxiv.org/abs/2611.10469)): the engine, the 3-bit copies, the `fast` profile and
  MTP drafting. Patches 0002 and 0003 modify Hibana files; see [NOTICE](NOTICE).
- Qwen3.8-Flash-Next by the Qwen team; NVFP4 checkpoint by RadixArk (license on its card).

## License

MIT for this recipe ([LICENSE](LICENSE)). The Hibana patches are Apache-2.0 like the files they change
([NOTICE](NOTICE)). The weights carry their own licenses.
