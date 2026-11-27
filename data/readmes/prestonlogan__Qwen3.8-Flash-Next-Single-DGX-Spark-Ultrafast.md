<p align="center">
  <img alt="Qwen3.8 Flash Next on one NVIDIA DGX Spark, v1.1.0: 132 tok/s on prose, 2.8× faster than the baseline recipe (typical NVFP4 + MTP recipe 46.6 tok/s, this recipe 132.4 tok/s). 109 tok/s on agent-session replays (30-run replay, temperature 1.0), 154 tok/s on code, 296 tok/s total across 4 concurrent requests." src="media/header.jpg">
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

> **v1.2.0:** target-guided long-context draft attention and automatic QSA prefill. On one Spark, same day and harness, realistic decode at 100K rose from 89.9 to 101.0 tok/s (four runs each) and at 250K from 74.4 to 100.4 tok/s. Fixed exact 100K copy rose from 149.0 to 179.3 tok/s with byte-identical output. Short context is unchanged within the measured run spread. It also removes invalid programmatic dependent launch instructions from the HyperConnection kernels, fixing an intermittent batch 4 startup freeze, and fixes [#10](https://github.com/prestonlogan/Qwen3.8-Flash-Next-Single-DGX-Spark-Ultrafast/issues/10): quoting or explaining `</think>` inside the model's reasoning no longer ends the turn with an empty answer. Upgrade with `git pull && docker compose up -d --build --wait`.
>
> **v1.1.0:** a distilled draft head, a repetition guard and GB10 kernels, in two modes. The default
> (`TUNING=v1.1`) is 28% faster on prose and 23% faster on code than v1.0.0 at temperature 0, and 12% faster across 30
> sampled agent sessions with no looping run (v1.0.0: 2 of 30). `TUNING=v1.1-exact` keeps drafting from changing what
> the model says and scores higher on tool-eval-bench (93 against 89), at about v1.0.0's sampled speed. See
> [v1.0.0 vs v1.1.0](#v100-vs-v110).
>
> **v1.1.1:** fixes an engine crash in v1.1.0. A sampled request (temperature above 0) whose round was checked without
> CUDA graphs, such as one with an image, could stop the engine with `NameError: name 'batch' is not defined`; after
> that, chat requests returned 503. Thanks to dengfa.cheng for the report. Upgrade with
> `git pull && docker compose up -d --build --wait`. Serving mostly non-English text? Set `DRAFT_VOCAB=0`; see
> [Quality and limits](#quality-and-limits).

> Built on [**dedene/Hibana-Qwen3.8-Flash-Next-DGX-Spark**](https://github.com/dedene/Hibana-Qwen3.8-Flash-Next-DGX-Spark)
> by Peter Dedene, which did the Hibana Docker recipe, the tool-call fix and the speed and agent benchmarks below. This
> repo adds two Hibana patches for images and ships the `fast` profile by default. If you only need text, dedene's
> recipe with `PROFILE=fast` gives the same text speed.

*Real time, no speed-up: v1.1.0 default (`TUNING=v1.1`) in DeepSeek Harness at reasoning effort Xhigh, building a small Python inventory CLI (6 files, 3 unit tests). The whole task took 34 s; this clip is the middle 14.6 s, with the harness's decode speed (`tok/s`) under the composer. [Prompt and how it was made](media/demo/README.md) · [MP4](media/dsh-agentic-demo.mp4)*

[![This recipe running an agentic coding task in DeepSeek Harness: reasoning, tool calls and code streaming in real time](media/dsh-agentic-demo.gif)](media/dsh-agentic-demo.mp4)

## Speed

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="media/speed-chart-dark.png">
  <img alt="Bar chart: this recipe (v1.1.0) streams 132.4 tok/s on English prose vs 46.6 for a typical recipe, 153.6 vs 58.3 on code, 114.0 on prose about an image, and 296.3 vs 97.3 total with 4 requests at once" src="media/speed-chart-light.png">
</picture>

<details>
<summary><b>Exact numbers</b></summary>

| tok/s, one DGX Spark | Typical recipe (TensorFold, NVFP4 + MTP) | Hibana `exact` | **This recipe** (v1.1.0, Hibana `fast` + images) |
|---|---:|---:|---:|
| English prose, 1 request | 46.6 | 45.2 | **132.4** |
| Code, 1 request | 58.3 | 50.7 | **153.6** |
| Prose about an image, 1 request | no images | no images | **114.0** |
| 4 requests at once, total | 97.3 | 96.6 | **296.3** |
| Prose, sampled (temperature 1.0), 1 request | | | 110.7 |
| Code, sampled (temperature 1.0), 1 request | | | 122.7 |
| Prose about an image, sampled, 1 request | | | 90.1 |
| 4 requests, sampled, total | | | 205.0 |

</details>

Decode speed, timed from the first output token, thinking on (the default). Temperature 0 unless marked, 512 output
tokens (1,024 for sampled rows), median of 3 runs (5 for single sampled rows). This recipe's column was measured
2026-11-24 on its default settings (`PROFILE=fast`, `TUNING=v1.1`, `VISION=1`). The TensorFold and `exact` columns are
dedene's measurements from 2026-11-16
([MiaAI-Lab TensorFold recipe](https://github.com/MiaAI-Lab/Qwen3.8-Flash-Next-Single-DGX-Spark-TensorFold) on NVIDIA's
FP4-Local checkpoint), same prompt types and method. dedene measured Hibana's stock `fast` at 102.0 on prose and 123.2
on code; the rest of the gain comes from this repo's v1.1.0 draft head and kernels.

Sampled requests are slower because fewer drafted tokens survive verification at temperature 1.0. Prefill is
about 3,400 tok/s at 2K tokens in v1.1.0, slower than v1.0.0 (see [limits](#quality-and-limits)).

### v1.0.0 vs v1.1.0

Same Spark, same day (2026-11-24), each from a fresh boot, `bench/bench.py` medians in tok/s. Full results, method
and raw files: [bench/ab-20261124](bench/ab-20261124/README.md).

| | v1.0.0 | **v1.1.0** (default, `TUNING=v1.1`) | v1.1.0 exact (`TUNING=v1.1-exact`) |
|---|---:|---:|---:|
| Prose, temperature 0 | 103.5 | **132.4** | 107.4 |
| Code, temperature 0 | 124.6 | **153.6** | 92.6 |
| Prose about an image, temperature 0 | 106.1 | **114.0** | 81.6 |
| 4 requests, temperature 0, total | 255.6 | **296.3** | 222.1 |
| Prose, temperature 1.0 | **114.5** | 110.7 | 98.2 |
| Code, temperature 1.0 | 106.1 | **122.7** | 106.6 |
| Prose about an image, temperature 1.0 | 87.6 | **90.1** | 79.2 |
| 4 requests, temperature 1.0, total | 195.8 | **205.0** | 197.1 |
| 30 agent-session replays, temperature 1.0: mean tok/s | 97.2 | **109.2** | 99.8 |
| ... runs that looped | 2 of 30 | **0 of 30** (guard stopped 1) | **0 of 30** |
| tool-eval-bench (hard mode on) / hard mode | 89 / 62 of 70 | 89 / 59 of 70 | **93 / 65 of 70** |
| GSM8K / MBPP / tool calls / AIME (each of 20) | 18 / 20 / 19 / 20 | 19 / 19 / 20 / 20 | 18 / 19 / 20 / 20 |
| Prefill, 2,048-token prompt, tok/s | **3,786** | 3,434 | 2,907 |
| Needle in a haystack to ~254K tokens | 20/20 | | 20/20 |

Long-context results for v1.1.0 (decode at depth, RULER, a compaction agent test) are under [Long context](#long-context).

**Which mode to use.** The default is the fast choice for chat, coding and agents: faster than v1.0.0 on every
temperature-0 row and on sampled code and images, even on sampled prose (110.7 against 114.5, within the ±25%
run-to-run spread). `TUNING=v1.1-exact` is for when output must follow the served model exactly (evaluations,
reproducible runs) or when tool-call safety matters most: it scored 4 points higher on tool-eval-bench, and the
default had one more safety warning than v1.0.0 (it disclosed a token under a multi-hop prompt injection).

What the modes change: speculative decoding drafts several tokens and the model checks them. Exact acceptance keeps a
draft only when it is what the model would have produced. The default relaxes that a little: at temperature 0 it
keeps a draft that is in the model's top 3 and close in score (as v1.0.0 does), and at temperature 1.0 it accepts
near-misses with `accept_soft` 0.35 (v1.0.0: 0.5). In one of the default's 30 agent replays the repetition guard
stopped a loop at about 5,500 thinking tokens; the run ended early instead of looping. `TUNING=stock` serves the
v1.0.0 behavior.

### Why it is fast

Hibana's `fast` profile serves the 512 experts as calibrated 3-bit copies and the trunk in FP8, so each token reads far
fewer bytes from the Spark's 273 GB/s memory. The checkpoint's MTP head drafts several tokens per step, and the model
verifies them in one pass. v1.1.0 replaces that head with one distilled to match the model's own choices more often
(so more drafts survive verification), keeps the head's 512 experts in 3-bit form, and adds GB10 kernels for the
HyperConnection mix, split-K sparse attention and the 3-bit matrix multiply. The default then accepts slightly more
drafts than exact verification would (see above).

## Quickstart

**Hardware:** DGX Spark (GB10, sm_121, aarch64), driver 580, CUDA 13, Docker with the NVIDIA Container Toolkit,
Compose v2. About 200 GB of free disk, and the box to itself while it serves (Hibana sizes its KV pools from the free
memory).

```bash
git clone https://github.com/prestonlogan/Qwen3.8-Flash-Next-Single-DGX-Spark-Ultrafast && cd Qwen3.8-Flash-Next-Single-DGX-Spark-Ultrafast
docker compose up -d --wait   # first run: ~15 min image build, 187 GB download, ~3 min kernel builds
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
| Default profile | `exact` (lossless, ~47 tok/s) | `fast` with the v1.1.0 stack (`TUNING=v1.1`; `v1.1-exact` for exact acceptance) |
| Image input | no (vision tower not loaded) | **yes** (`patches/0002`, `patches/0003`) |
| Image requests use MTP drafting and CUDA graphs | — | yes |
| Draft vocabulary shortlist | off | on (98,304 rows) |
| Distilled MTP draft head, 3-bit experts | no | **yes** (`patches/0004`, 1.2 GB download) |
| Target-guided long-context draft attention | no | **yes** (`patches/0005`) |
| Quoting `</think>` in reasoning does not end the turn | no | **yes** (`patches/0006`) |
| Repetition guard and late `</think>` ramp | no | **yes** (`patches/0004`) |
| GB10 kernels: HyperConnection mix, split-K sparse attention, 3-bit GEMM | no | **yes** (`patches/0004`) |
| Tool-argument fix (`patches/0001`) | yes | yes (dedene's) |

- `patches/0002-flashnext-vision.patch`: loads the checkpoint's Qwen vision tower and projector, expands image
  placeholders, and gives image tokens their multimodal (M-RoPE) positions in attention and the sparse indexer.
- `patches/0003-vision-speculation-graphs.patch`: image requests keep MTP speculative decoding and run the captured
  CUDA graphs instead of one eager pass per token. With patch 0002 alone, image prose decoded at about 36 tok/s in
  our tests (temperature 0, thinking off); with both patches it runs at text speed. Text requests take the same code
  paths as before.

- `patches/0004-v1.1-exact-speed-stack.patch` (v1.1.0): loads the distilled draft head and its 3-bit experts; adds a
  repetition guard that stops a generation only on a real loop (periodic repeats over at least 64 tokens, or very
  low n-gram novelty over a long window), aware of code fences and tool calls; a `</think>` bias that starts at 40% of
  `max_tokens` and grows firm by 70%, so long reasoning still ends with an answer; the GB10 kernels above; routing
  renormalization; and a 2K/4K-token prefill warmup at startup. The patch header lists which parts are always on
  (kernels, warmup) and which `TUNING=v1.1` and `v1.1-exact` switch on.

- `patches/0005-qsa-guided-draft-attention.patch` (v1.2.0): for text contexts over 65,536 tokens,
  the draft keeps the most recent 14,336 KV pages plus 2,048 distant pages selected by the target model's own
  verify-time sparse attention at layer 43. This shortens long-context draft attention without changing the target
  model or exact verification. Image requests and budget speculation are excluded. In the controlled release test,
  realistic 100K decode rose from 89.9 to 101.0 tok/s and 250K from 74.4 to 100.4; fixed exact 100K copy rose from
  149.0 to 179.3 tok/s with byte-identical fixed prompts.

- `patches/0006-think-close-token.patch` (v1.2.0): `</think>` is one ordinary token (id 248069), so a model that
  quotes the tag in its reasoning used to close thinking there. Inside thinking the engine now masks that token unless
  the previous token ends in a newline outside an open code fence, inline code span or quote, and masks the
  end-of-turn tokens. The reasoning parser ends reasoning on the token id instead of the text. Exact-mode outputs are
  unchanged.

All six patches apply to Hibana `d474b74` (v0.1.0), in order, during the image build.

## Settings

Put overrides in `.env` (see `.env.example`).

| Variable | Default | Meaning |
|---|---|---|
| `PROFILE` | `fast` | `fast`: 3-bit experts, ~2× faster than `exact`. `exact`: NVFP4 experts, the checkpoint's own outputs. `throughput`: `fast` tuned for many requests |
| `TUNING` | `v1.1` | With `PROFILE=fast`: `v1.1` turns on the distilled draft head, the repetition guard and the patch 0004 settings, with lightly relaxed acceptance (top-3 at temperature 0, `accept_soft` 0.35). `v1.1-exact` is the same with exact acceptance. `stock` serves Hibana's own `fast`, as in v1.0.0 |
| `VISION` | `1` | `1` loads the vision tower (0.84 GiB) and accepts images; `0` serves text only |
| `DRAFT_VOCAB` | 98,304 (`v1.1*`), 131,072 (`stock`) | The drafter picks from the most common tokens (+3–10% on English and code in our tests); verification still uses the full vocabulary. Set `0` for mostly non-English text |
| `DRAFT_HEAD_REPO` | `prestonlogan/Qwen3.8-Flash-Next-MTP-Draft-Head` | Hugging Face repo the download service fetches the distilled draft head from (SHA-256 checked) |
| `MTP_QSA_GUIDE` | `1` (`v1.1*`) | Target-guided long-context draft attention. Set `0` to disable it |
| `QSA_GUIDE_LAYER` | `43` | Target attention layer whose verify-time page selection guides the draft |
| `MTP_QSA_GUIDE_LOCAL` | `14336` | Recent draft KV pages always kept |
| `MTP_QSA_GUIDE_WIDTH` | `2048` | Selected distant draft KV pages kept, at most 2048 |
| `MTP_QSA_GUIDE_MIN_CONTEXT` | `65536` | Context length where guided drafting starts |
| `QSA_PREFILL_BACKEND` | `auto` (`v1.1*`) | Sparse attention prefill backend. `auto`: the optimized kernel where it applies, the original otherwise, per request. `optimized` is strict: any prefill the optimized kernel can't run (over 32,768 tokens, or sparse eager prefill such as a highly repetitive prompt) fails that request with a 503. Use `optimized` only to benchmark the kernel |
| `PROPOSER` | `mtp` | `mtp` (the checkpoint's MTP head) or `dflash2` (incoai's DFlash2 drafter, 1.2 GB more; not tested with images) |
| `SPEC` | profile's | Draft tokens per round; `0` turns speculation off |
| `PARALLEL` | profile's (4) | Most requests decoded together |
| `CONTEXT` | `262144` | Largest prompt plus output per request |
| `SSD` / `SSD_GIB` | `on` / `100` | Prefix cache tier on the NVMe, in `DATA_DIR/ssd` |
| `HOST_FLOOR_GIB` | `12` | Memory left for everything else; Hibana's memory guard stops the server below half of it |
| `HOST` / `PORT` | `0.0.0.0` / `8888` | Listen address |
| `RESTART` | `no` | Docker restart policy. Set `unless-stopped` for a server that runs unattended: it restarts after a reboot and after an engine failure (see below) |
| `HF_CACHE` | `~/.cache/huggingface` | Shared Hugging Face cache for the checkpoint |
| `DATA_DIR` | `~/.cache/hibana-flashnext` | 3-bit copies, SSD tier, logs |
| `HIBANA_IMAGE` | `hibana-flashnext-vision:d474b74d-v7` | Engine image tag |

## Quality and limits

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="media/quality-chart-dark.png">
  <img alt="Quality panels. v1.1.0 on this build: tool-eval-bench 89 v1.0.0, 89 v1.1.0 default, 93 v1.1.0 exact; hard mode 62, 59, 65 of 70; GSM8K/MBPP/tool calls/AIME 77, 78, 77 of 80; agent replays that looped 2, 0, 0 of 30. Stock fast, measured by others: GPQA-Diamond 81.8% fast vs 84.8% exact (p 0.51); BFCL 87.2 fast vs 85.8 TensorFold; AgentDojo 77.5 vs 85.5; injection attacks executed 1 of 200 for both" src="media/quality-chart-light.png">
</picture>

- **v1.1.0 against v1.0.0 on the same day** (details in [bench/ab-20261124](bench/ab-20261124/README.md)):
  tool-eval-bench 89 for the default and 93 for `v1.1-exact` against 89 (hard mode 59 and 65 against 62 of 70). The
  default had safety warnings on TC-51, TC-74 and TC-98 (v1.0.0: TC-51, TC-85; exact: TC-51). GSM8K, MBPP, tool calls
  and AIME (20 each, temperature 0) are within one question across all three. In 30 replays of an agent session at
  temperature 1.0, v1.0.0 fell into a repetition loop twice and neither v1.1.0 mode did. On one long reasoning prompt
  `v1.1-exact` thought for 7,626 tokens before answering against 26,112 for v1.0.0.
- **Exact acceptance is not the `exact` profile.** `TUNING=v1.1-exact` makes drafting lossless, but the target model
  is still `fast`'s 3-bit experts with a routing budget, so outputs differ slightly from `PROFILE=exact`. The numbers
  below are for Hibana's stock `fast` (`TUNING=stock`).
- **Stock `fast` is slightly lossy.** Hibana's authors measured GPQA-Diamond with thinking at 81.8% in `fast` against 84.8% in
  `exact` (99 questions, p 0.51), with answers 18% longer. dedene's agent benchmark on `fast`: BFCL single-turn 87.2
  (TensorFold 85.8), AgentDojo tasks done under attack 77.5 (TensorFold 85.5), 1 of 200 injection attacks executed (same
  as TensorFold). Use `PROFILE=exact` when you need the model's exact outputs.
- **Thinking quoted the closing tag.** Before v1.2.0 ([#10](https://github.com/prestonlogan/Qwen3.8-Flash-Next-Single-DGX-Spark-Ultrafast/issues/10)), a model that wrote or explained the literal
  `</think>` tag inside its reasoning ended the turn there: an empty answer or thinking cut in two. The engine now
  masks that token inside thinking unless the previous token ends in a newline outside an open code fence, inline
  code span, or quote, and the parser ends reasoning on the token id, not the text. Forced closes (think guard,
  thinking budget) are unchanged. Answers that must contain the literal tag can still drop or change it
  ([#13](https://github.com/prestonlogan/Qwen3.8-Flash-Next-Single-DGX-Spark-Ultrafast/issues/13)); insert it on the client side if you need it exactly.
- **v1.1.0 prefills more slowly.** At 2,048 tokens it prefilled at 3,434 (default) and 2,907 (exact) tok/s against
  3,786 for v1.0.0. Time to first token on a 17.9K-token uncached prompt was 7.9 s against 6.4 s (about 10-35% longer
  across our runs); prompts already in the prefix cache are unaffected (0.18 s).
- **v1.2.0 prefill:** median 2,048-token prefill was 3,004 tok/s against 2,985 for the v1.1.1-equivalent baseline,
  effectively flat. A unique 32K prompt prefilled at 3,435 against 3,151 tok/s, 9.0 percent faster. At 63K it was
  3,147 against 3,225 tok/s, 2.4 percent slower.
- **The repetition guard ends a generation that is looping** (finish reason `stop`) instead of letting it run to
  `max_tokens`. Set `HIBANA_THINK_GUARD=0` to turn it off.
- **Don't raise `HIBANA_ACCEPT_SOFT` above the default.** At 1.0–3.0 decoding is 20–60% faster, but in our tests long
  thinking fell into repetition loops and ended with no answer in 1 of 5 to 1 of 3 runs of an agent task. v1.1.0 uses
  0.35; Hibana's own `fast` and v1.0.0 use 0.5.
- **Images:** inline base64 only, up to 32 MiB encoded and 100 per request, each resized to at most 1,048,576 pixels.
  No video. One Spark only (no two-Spark tensor parallel with vision). Checked with our own text and image prompts
  (`tools/check.py` and a 22-prompt correctness set); no standard image benchmark (MMMU, ChartQA) has been run yet.
- **Non-English text:** the draft-vocabulary shortlist lowers draft acceptance on scripts outside the common tokens.
  Set `DRAFT_VOCAB=0` if most of your traffic is not English or code. Hibana leaves it off for this reason. A user's
  measurement on one Spark with `TUNING=v1.1`: Slovak decode 70.1 tok/s with the shortlist against 86.5 with
  `DRAFT_VOCAB=0`, while English went 130.5 against 115.0.
- Port 8888 is shared with other Spark recipes: stop the one that serves it first.
- The API has no key check and listens on the LAN. Keep it there.
- An omitted `temperature` means 1.0 with top_p 0.95 and top_k 20, the model's generation config.

### Long context

v1.1.0 default on one Spark, 2026-11-24. Scripts, raw results and method: [bench/longctx-20261124](bench/longctx-20261124/README.md).
The v1.2.0 rows come from the 2026-11-25 release validation ([bench/v120-20261125](bench/v120-20261125/README.md)),
which measured only 100K and 250K. They ran on a different day from the v1.1.0 rows; the same-day A/B is in the
first bullet below.

| Context already filled | 0 | 32K | 64K | 100K | 150K | 200K | 250K |
|---|---:|---:|---:|---:|---:|---:|---:|
| Decode tok/s | 124.2 | 104.2 | 101.4 | 94.1 | 86.0 | 72.1 | 69.4 |
| Time to first token, uncached | 1.0 s | 11.1 s | 22.5 s | 35.2 s | 53.5 s | 74.7 s | 86.6 s |
| v1.2.0 decode tok/s | n/a | n/a | n/a | 101.0 | n/a | n/a | 100.4 |
| v1.2.0 time to first token, uncached | n/a | n/a | n/a | 30.6 s | n/a | n/a | 80.0 s |

- **v1.2.0:** patch 0005 improves decode after 65K tokens. In the same-day controlled A/B, realistic 100K decode rose
  from 89.9 to 101.0 tok/s and 250K from 74.4 to 100.4. Fixed exact 100K copy rose from 149.0 to 179.3 tok/s with
  byte-identical fixed prompts. Batch 2 rose from 202.1 to 229.3 and 244.3 tok/s after a first-request warmup cost.
  At 131K, the five-task RULER subset averaged 90.5 against 90.1, and variable tracking over 10 samples averaged 86.0
  against 84.0.
- **Decode holds up; prefill is the cost.** Decode was near 70 tok/s with 250K tokens in context in v1.1.0 and about
  100 tok/s in v1.2.0, but an uncached 250K prompt still waits 80 to 87 s for its first token. Prompts already in the prefix cache skip that.
- **RULER** (NVIDIA's 13 synthetic tasks, thinking off, temperature 0): average **96.3** at 32K, **94.0** at 64K and
  **96.4** at 128K. The 8 retrieval tasks scored 100 at every length; the misses are in variable tracking, common-word
  counting and HotpotQA. Samples are small (5 per task at 32K, 3 at 64K and 128K), and 192K was not run. Common-word
  counting needed 1,024 output tokens instead of RULER's usual ~128, or the model is still counting when it stops.
- **An agent task 6 times the context window.** The agent read about 900K tokens of RFCs a page at a time, found 12
  planted requirements and built a tool from them, through 6 compactions where its history was replaced by its own
  summary. It passed 24 of 25 hidden checks and finished on its own in 41 minutes. The one failure: during a
  compaction it wrote down a requirement that is not in the documents, as if quoted, and built it in. Under long
  agent runs, check what the agent claims it read, not only what it remembers.

## How it is put together

- `Dockerfile`: Hibana v0.1.0 at commit `d474b74` with its own `uv.lock` environment (torch 2.13 cu130, FlashInfer
  0.6.17, Triton 3.7.1) on `nvidia/cuda:13.0.0-devel`, then patches 0001–0005.
- `compose.yaml`: a one-shot `download` service, then the `hibana` server with host networking.
- `tools/download.sh`: Hibana's own preflight fetches the pinned checkpoint and 3-bit copies for every profile, then
  the distilled draft head (with `TUNING=v1.1`), checked against pinned SHA-256 hashes.
- `tools/serve.sh`: maps the settings above to `hibana serve flashnext`.
- `tools/health.sh`: the healthcheck. If Hibana's engine fails (it then answers 503 while the web server stays up), it
  stops the server so the container exits and `RESTART=unless-stopped` restarts it, about 70 s to serving again.
- `tools/check.py`: standard library only. `--needle 32000 131072` adds long-context retrieval.
- `docs/optimization-notes.md`: every change we measured, what we kept, what we rejected and why, with the numbers.

## Credits

- **[dedene/Hibana-Qwen3.8-Flash-Next-DGX-Spark](https://github.com/dedene/Hibana-Qwen3.8-Flash-Next-DGX-Spark)** by
  Peter Dedene (MIT): the Docker recipe this repo is built from, patch 0001, and the TensorFold, `exact` and agent
  benchmark numbers quoted above.
- **[Hibana](https://github.com/sharar-project/hibana)** by Yahya Emara, Chi-Chih Chang and the Abdelfattah Lab at
  Cornell (Apache-2.0, [paper](https://arxiv.org/abs/2611.10469)): the engine, the 3-bit copies, the `fast` profile and
  MTP drafting. Patches 0002–0005 modify Hibana files; see [NOTICE](NOTICE).
- Qwen3.8-Flash-Next by the Qwen team; NVFP4 checkpoint by RadixArk (license on its card). The distilled draft head
  is derived from Qwen3.8-Flash-Next and carries the Qwen Community License 1.0 ([card](hf/draft-head/README.md)).

## License

MIT for this recipe ([LICENSE](LICENSE)). The Hibana patches are Apache-2.0 like the files they change
([NOTICE](NOTICE)). The weights carry their own licenses; the draft head is under the Qwen Community License 1.0.
