# Inkling 2 Mini on Apple Silicon (MLX)

MLX-VLM with support for [Thinking Machines' Inkling 2 Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini), the
looped mixture-of-experts model (26.4B parameters, about 3.4B active per token; the middle 12 of its 24 layers run three
times per token). Text and image input, its DSpark speculative-decoding draft, tool calls, and the released NVFP4 / MXFP8
weights loaded as they are.

Since 21 November 2026, Inkling 2 Mini is supported in MLX-VLM itself (pull request #2778, merged into
[Neywa-Labs/mlx-vlm](https://github.com/Neywa-Labs/mlx-vlm) main; not yet in a PyPI release). From v0.2.0 this repository is
that upstream MLX-VLM, pinned at commit `fd6404f`, plus one addition: `mlx_vlm/tools/parsers/inkling.py`, Inkling's tool-call
format, so `mlx_vlm.server` returns OpenAI `tool_calls`.

Our Hugging Face builds (below) use the upstream tensor names since 21 November 2026, so they load both with this repository
and with stock MLX-VLM from main. If you downloaded one of them before that, download it again. v0.1.0 of this repository
(our own looped-model code) only loads the earlier files.

Published by [NetProjects](https://netprojects.com) (Internet Projects Ltd). Not affiliated with Thinking Machines.

## Install

Python 3.10 or newer on an Apple Silicon Mac:

```bash
pip install "git+https://github.com/internet-projects/inkling2-mlx@v0.2.8" torch torchvision
```

This installs `mlx-vlm` version `0.8.0+inkling2mini.10`. Without the tool-call parser, stock MLX-VLM from main works too:
`pip install "git+https://github.com/Neywa-Labs/mlx-vlm" torch torchvision`. PyTorch and torchvision are only used on the CPU by the image
processor.

## Models

| Model | Size | Notes |
|---|---|---|
| [netprojects/Inkling-2-Mini-MLX-4-8bit](https://huggingface.co/netprojects/Inkling-2-Mini-MLX-4-8bit) | 19.5 GB + 0.64 GB draft | 4-bit NVFP4 + 8-bit MXFP8 experts as released (lossless), recommended |
| [netprojects/Inkling-2-Mini-MLX-4bit](https://huggingface.co/netprojects/Inkling-2-Mini-MLX-4bit) | 16.5 GB + 0.64 GB draft | plain affine 4-bit |
| [netprojects/Inkling-2-Mini-MLX-3bit](https://huggingface.co/netprojects/Inkling-2-Mini-MLX-3bit) | 14.1 GB + 0.64 GB draft | 3/4-bit experts, for 24 GB Macs (`prefill_step_size=256`) |
| [netprojects/Inkling-2-Mini-MLX-2.5bit](https://huggingface.co/netprojects/Inkling-2-Mini-MLX-2.5bit) | 10.8 GB + 0.64 GB draft | per-layer mixed 2/3-bit experts (new files 22 November 2026); 16 GB Macs with a raised GPU limit (see its card) |
| [netprojects/Inkling-2-Mini-MLX-2bit-mixed](https://huggingface.co/netprojects/Inkling-2-Mini-MLX-2bit-mixed) | 9.5 GB + 0.64 GB draft | per-layer mixed, mostly 2-bit experts, smallest; for 16 GB Macs (see its card) |


## Use

```python
from mlx_vlm import load, generate
from mlx_vlm.prompt_utils import apply_chat_template

model, processor = load("netprojects/Inkling-2-Mini-MLX-4-8bit")
prompt = apply_chat_template(processor, model.config, "Explain in two sentences why the sky is blue.", reasoning_effort="low")
print(generate(model, processor, prompt, max_tokens=2048, temperature=0.0).text)
```

`reasoning_effort` is part of Inkling's chat template: `none`, `minimal`, `low`, `medium`, `high` (default), `xhigh`, `max`,
or a number from 0.0 to 0.99. The model can think at length even at `none`, so always set `max_tokens`.

Images: pass `num_images=1` to `apply_chat_template` and `image=["picture.png"]` to `generate`.

DSpark speculative decoding, with the draft bundled in the model repository:

```python
from mlx_vlm.speculative.drafters import load_drafter
draft, kind = load_drafter("netprojects/Inkling-2-Mini-MLX-4-8bit")
print(generate(model, processor, prompt, max_tokens=2048, draft_model=draft, draft_kind=kind, draft_block_size=4).text)
```

Since v0.2.5, plain decode is fast enough that drafting pays off mainly on text that repeats what came before (code edits,
rewrites, structured output). Since v0.2.8, drafting switches itself off while plain decode is faster and back on when drafting
pays again (auto-off, greedy and seeded runs). Without a block size, DSpark uses block 4.
Server: add `--draft-model <same repo> --draft-kind dflash --draft-block-size 4`.

DFlash2 draft (v0.2.8): the separate [incoai/Inkling-2-Mini-DFlash2](https://huggingface.co/incoai/Inkling-2-Mini-DFlash2)
draft (about 1 GB) also loads, with `load_drafter("incoai/Inkling-2-Mini-DFlash2")` or `--draft-model incoai/Inkling-2-Mini-DFlash2`.

Greedy tok/s on an M5 Max, 4-bit build, block 4, 256 new tokens (plain decode 83-87):

| Draft | chat | chat 2 | code | rewrite |
|---|---|---|---|---|
| DSpark (bundled), auto-off off | 60 | 59 | 93 | 94 |
| DSpark (bundled), auto-off | 86 | 82 | 96 | 92 |
| DFlash2, auto-off off | 67 | 66 | 98 | 87 |
| DFlash2, auto-off | 85 | 82 | 90 | 94 |

`MLX_VLM_DSPARK_AUTO_OFF=0` keeps drafting on for every round.

Variable-loop checkpoints (v0.2.8): [thinkingmachines/TML-d24-varloop-research](https://huggingface.co/thinkingmachines/TML-d24-varloop-research)
loads like Inkling 2 Mini and runs its looped layers 1 to 5 times. Set the pass count with `INKLING2_LOOP_PASSES=N` (or
`loop_num_passes` in the text config); the checkpoint's default is 3. The bundled DSpark draft works only at 3 passes.

Faster one-token decode (v0.2.3, on by default): the attention no longer copies its key/value history at every step.
On an M5 Max with the 4-bit build, plain decode went from 41.0 to 44.6 tok/s at a 1K prompt and from 36.4 to 41.7 at 16K,
and DSpark (block 4) from 85.4 to 90.9 tok/s at 16K. The output matches the old code up to bf16 rounding (same greedy
tokens in our checks; drafted check rows are bit-identical). `INKLING2_FAST_DECODE=0` switches back to the old code.

v0.2.4 adds compiled per-layer glue and controllers and three small Metal kernels (attention residuals and the
loop's cross-pass messages, the q/k/r clip with the value norm, and the banded mask), all on by default and switched off
by the same `INKLING2_FAST_DECODE=0`. On the same Mac and build, plain decode went from 44.6 to 59.7 tok/s at 1K and from
41.6 to 55.1 at 16K; DSpark (block 4) from 102.6 to 118.0 at 1K and from 90.3 to 100.5 at 16K (KL max 0.008 against
v0.2.3, same top token at every checked position). On CPU the plain MLX code runs instead of the kernels.

v0.2.5 adds ten more decode changes (compiled one-row MoE and attention visits, launch trims, a top-k kernel for check
rows, and overlapping the GPU with Python every 8 layer visits). Same Mac, 4-bit build, 23 November 2026, greedy, median
of 3, against the original MLX-VLM (Neywa-Labs `f1618d6d`) and v0.2.4:

| tok/s | MLX-VLM | v0.2.4 | v0.2.5 |
|---|---|---|---|
| Plain, 1K prompt | 40.7 | 59.5 | 84.1 (×2.07) |
| Plain, 8K prompt | 38.5 | 57.2 | 79.7 (×2.07) |
| DSpark block 4, 1K (repeated text) | 101.8 | 115.0 | 125.0 (×1.23) |
| DSpark block 4, 8K (repeated text) | 95.9 | 107.0 | 114.9 (×1.20) |
| Chat answer, 256 tokens, plain | 36.7 | 59.8 | 86.4 (×2.35) |
| Chat answer, 256 tokens, DSpark block 4 | 50.0 | 59.7 | 64.3 |

Against the original MLX-VLM: KL max 0.014, same top token at all 97 checked positions, same greedy text; peak memory
26.4 GB (MLX-VLM 26.2). `INKLING2_FAST_DECODE=0` still switches all of it off.

v0.2.6 speeds up prompt reading (prefill): the depth reads of a whole prompt chunk go through the attention-residual
kernel, the loop's message controller runs as one compiled graph, and the banded mask kernel writes the sink logit as
its last column (no second copy of the heads x rows x keys mask). Same Mac and build, 24 November 2026:

| Prefill tok/s | v0.2.5 | v0.2.6 |
|---|---|---|
| 8.7K prompt | 1467 | 1642 (+12%) |
| 16K prompt | 1382 | 1608 (+16%) |

KL max 0.0025 against v0.2.5, same 64 greedy tokens. Decode is unchanged. `INKLING2_FAST_DECODE=0` switches these off too.

v0.2.7 makes sampled DSpark faster. The target now checks the draft with speculative (rejection) sampling: a drafted
token is kept with probability min(1, p/q), and the first rejected position is drawn from the leftover of the target
distribution. The output follows the same temperature, top-p and top-k law as plain decode; before, a drafted token was
kept only when the target's own random draw happened to match it. Same Mac, 4-bit build, 256 new tokens, thinking off,
DSpark block 4, 25 November 2026:

| tok/s | plain | DSpark v0.2.6 | DSpark v0.2.7 |
|---|---|---|---|
| Rewrite, temperature 1.0 | 83.3 | 92.9 | 97.4 |
| Rewrite, temperature 1.0, top-p 0.95 | 82.0 | 76.6 | 96.6 |
| Chat, temperature 1.0 | 86.2 | 54.6 | 58.2 |

So DSpark is now the faster choice for sampled code edits and rewrites too; for chat, plain decode stays faster.
With a seed, v0.2.7 DSpark output follows the same law as plain decode but is not token-identical to it;
`MLX_VLM_DSPARK_REJECTION=0` restores the old check, which is.

OpenAI-compatible server (tool calls returned as `tool_calls`, thinking as `reasoning_content`):

```bash
mlx_vlm.server --model netprojects/Inkling-2-Mini-MLX-4-8bit --port 8000
```

### Other Inkling 2 Mini MLX builds

From v0.2.8, `load` also reads Inkling 2 Mini builds made for other runtimes: builds converted with mlx-lm's Inkling
support (pull request #2086, for example mlx-community/Inkling-2-Mini-4bit), oMLX (oQ) builds such as
mlx-community/Inkling-2-Mini-oQ4e-mtp, and nativ-community/Inkling-2-Mini-nvfp4. The loader renames their tensors and
reads each layer's format (affine, NVFP4, MXFP8) from the tensor shapes, because some of their configs list only one
format. Our DSpark draft works with them too. Same Mac, 256 new tokens, greedy, thinking off, 26 November 2026:

| Build | Chat tok/s (plain / DSpark) | Code tok/s (plain / DSpark) | Same first token as our 4-bit |
|---|---|---|---|
| netprojects/Inkling-2-Mini-MLX-4bit | 87 / 60 | 87 / 93 | (reference) |
| mlx-community/Inkling-2-Mini-oQ3e-mtp | 83 / 53 | 83 / 95 | 84% |
| mlx-community/Inkling-2-Mini-4bit | 71 / 42 | 70 / 61 | 92% |
| mlx-community/Inkling-2-Mini-oQ4e-mtp | 67 / 36 | 64 / 53 | 92% |
| pipenetwork/Inkling-2-Mini-MLX-8bit | 65 / 39 | 64 / 57 | 92% |
| nativ-community/Inkling-2-Mini-nvfp4 | 52 / 36 | 52 / 50 | 91% |

Builds that keep the released NVFP4/MXFP8 experts are slower on the Mac than plain affine experts.

## Checks

On a MacBook Pro M5 Max (128 GB), 21 November 2026, with this repository's MLX-VLM (`fd6404f`), against Thinking Machines' Transformers implementation (pull request
#51050) running on the CPU with the released weights, 12 short chat texts (488 answer positions):

| Build | Same next token | Mean KL | GSM8K (50, reasoning `none`) |
|---|---|---|---|
| 4-8bit (the release, lossless) | 98.4% | 0.0018 | 47/50 |
| 4bit | 95.9% | 0.029 | 47/50 |
| 3bit | 95.5% | 0.042 | 48/50 |
| 2.5bit (22 November files) | 91.0% | 0.066 | 46/50 |
| 2bit-mixed | 90.2% | 0.107 | 47/50 |

The 4-8bit build's greedy answers to 3 prompts match Thinking Machines' code token for token (24 tokens each).
The 2.5bit and 2bit-mixed rows were measured on 22 November 2026 with the same code and texts, and repeated with v0.2.4 (same results).
Tool calls, coding tasks and thinking pass on every build. Image prompts pass on the 3-bit and larger builds; the 2.5bit and
2bit-mixed builds (2-bit vision encoder) get the colours and positions of the test image right but call its circle an oval.

Known limitation: when the model calls a tool through `mlx_vlm.server`, `content` can also carry a short sentence of its
reasoning.

## License

MLX-VLM is under the MIT License (`LICENSE`). The Inkling tool-call parser is under the Apache License 2.0
(`LICENSE-APACHE-2.0`); `NOTICE` describes it and the history of this repository. Inkling 2 Mini itself is Apache-2.0 with Thinking Machines'
[Model Acceptable Use Policy](https://thinkingmachines.ai/model-acceptable-use-policy/).

MLX-VLM's own documentation: [github.com/Neywa-Labs/mlx-vlm](https://github.com/Neywa-Labs/mlx-vlm) (MIT License, see `LICENSE`).
