# ComfyUI NegPiP Prompt

<p align="center">
  <img src="assets/icon.png" alt="NegPiP Prompt icon" width="200">
</p>

[![Tests](https://github.com/cyberdeliaAI/comfyui-negpip-zimage/actions/workflows/tests.yml/badge.svg)](https://github.com/cyberdeliaAI/comfyui-negpip-zimage/actions/workflows/tests.yml)
[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](LICENSE)

A standalone, single-node NegPiP implementation for **Z-Image**, **Z-Image
Turbo**, **Krea 2**, **MOSS-Image / MOSS Turbo**, **SD1**, **SDXL**, and **Anima**. The node patches the
connected model, merges separate positive and negative text strings, and
returns the conditioning required by a normal ComfyUI sampling workflow.

The package keeps its original Registry/repository name,
`comfyui-negpip-zimage`, but version 2.x is no longer limited to Z-Image.

## Installation

Open a terminal in `ComfyUI/custom_nodes` and run:

```bash
git clone https://github.com/cyberdeliaAI/comfyui-negpip-zimage
```

Restart ComfyUI afterwards. No additional Python packages are required beyond
the dependencies included with an up-to-date ComfyUI installation.

Krea 2 support requires a ComfyUI version that includes the native Krea 2
model and `krea2` CLIP loader type.

## Usage

Place **NegPiP Prompt (Multi-Model)** directly after the matching model and
CLIP loaders. It has four inputs:

- `model`: the loaded diffusion model;
- `clip`: the matching text encoder;
- `positive`: a connected positive `STRING`;
- `negative`: a connected negative `STRING`, optionally containing weights.

Both prompt inputs are sockets. They can be connected to a multiline text
node, wildcard node, prompt generator, or any other `STRING` output.

The node converts the negative string to negative NegPiP weights. For example:

```text
positive: a sharp portrait, detailed eyes
negative: blurry background, (text:1.3)
```

is compiled to:

```text
a sharp portrait, detailed eyes, (blurry background:-1), (text:-1.3)
```

The outputs are:

- `patched_model`: the patched `MODEL` that must be connected to the sampler or
  guider;
- positive `CONDITIONING` containing the compiled prompt;
- empty negative `CONDITIONING` for the existing guider/sampler workflow;
- `compiled_prompt` as a `STRING`, showing exactly what was sent to the
  patched text encoder.

Connect `compiled_prompt` to **Preview Any** to inspect the conversion. The
negative conditioning is intentionally empty: NegPiP processes negative
concepts inside the compiled positive conditioning.

The node consumes and encodes the connected CLIP internally, so a CLIP output
is not required. This also applies to Krea 2: its patched CLIP clone is used
immediately for the node's conditioning output.

## Prompt strength and length

You can enter either plain negative text or positive magnitude weights:

```text
blurry, background blur, bokeh
```

```text
(blurry, background blur, bokeh:0.4)
```

The node changes these to weights of `-1` and `-0.4`, respectively. Do not
enter a negative weight in the negative input unless you deliberately want the
same absolute strength; the node always makes negative-input weights negative.

Explicit weights use parentheses, such as `(detail:1.3)`. Bare text such as
`:3`, `16:9`, `12:30`, or `detail:1.3` stays literal in both prompt inputs.

Large negative lists at strength `1.0` can dominate the prompt and produce
unexpected results. Group related concepts and start with lower strengths:

```text
(3D, CGI, render, blender, video game screenshot, illustration:0.25),
(text, writing, subtitle, watermark, logo:0.7),
(blurry, low quality, jpeg artifacts, grainy:0.4)
```

There is no node-level character limit. The effective token/context limit
depends on the connected model and text encoder. The Qwen-based Z-Image and
Krea 2 encoders support a much longer context than CLIP-based SD models, but
long prompts can still use substantially more memory.

Z-Image Turbo normally remains at CFG `1.0`. Use the normal CFG settings for
SD1/SDXL workflows.

For Z-Image, compare prompt changes with the same seed. Broad semantic
categories can react non-linearly, so start with a strength around `0.25` to
`0.5` before trying `1.0`.

## Z-Image troubleshooting

- Connect `patched_model` from this node to the sampler or guider. Do not keep
  that input connected directly to the original model loader.
- Connect the node's positive and negative `CONDITIONING` outputs directly to
  the corresponding sampler/guider inputs.
- Use `compiled_prompt` only for inspection. Do not send it through another
  CLIP Text Encode node; Z-Image's normal tokenizer does not interpret NegPiP
  weights.
- With `Asian` in the negative input, `compiled_prompt` must show
  `(Asian:-1)`. For a weaker test, enter `(Asian:0.4)` in the negative input,
  which compiles to `(Asian:-0.4)`.

## Krea 2 notes

- Load the text encoder with ComfyUI's `CLIPLoader` type `krea2`; a regular
  Qwen, Z-Image, or Flux CLIP is not interchangeable.
- Connect `patched_model` to the sampler and use the node's conditioning
  outputs directly, just as for Z-Image.
- The integrated Krea 2 path applies NegPiP to all 28 main transformer blocks
  and both text-fusion refiner blocks. Enabling the refiners is intentionally
  stronger than the standalone upstream node's default and is intended to
  reduce positive leakage into neighboring text tokens before the main model
  blocks. Start with lower prompt magnitudes if the effect is too strong.
- Prompt magnitudes remain available in the negative input. For example,
  `(blurry:0.4)` compiles to `(blurry:-0.4)`.
- Complex conditioning transforms that normalize or clamp the Krea 2
  conditioning tensor may destroy its embedded NegPiP sidecar. A metadata
  fallback is included, but direct connections from this node remain the
  safest path.

## MOSS-Image / MOSS Turbo notes

MOSS support is new in 2.2.0 and experimental pending generation tests with a
real checkpoint. Use ComfyUI's **native MOSS-Image support** and `CLIPLoader`
type **`moss_image`**, with its **Qwen3.5-9B** text encoder. The older OpenMOSS
custom HF loader is not supported by this NegPiP path.

For an SFT checkpoint with an 8-step SFT DMD LoRA:

1. Load the model, apply your model LoRAs including the DMD adapter, then connect
   the resulting MODEL to **NegPiP Prompt (Multi-Model)**.
2. Connect the MOSS CLIP loader and separate positive/negative STRING inputs.
3. Connect `patched_model` and the node's conditioning outputs directly to the
   sampler. For a second latent-refinement pass, use the same patched model and
   conditioning outputs there as well.
4. Keep the Turbo sampling baseline: **CFG 1**, **8 steps**, **Euler / simple**.
   With CyberMOSS Sampler 0.1.1+, choose `turbo_reference` and verify that
   `schedule_mode` is `simple`. NegPiP does not change the sigma schedule.

Start with a short negative prompt at a low magnitude, for example:

```text
(watermark, text, jpeg artifacts:0.25)
```

The node encodes the positive prompt normally and negative spans separately,
using MOSS's thinking-enabled chat template. It injects the negative embeddings
before the template suffix and applies their signed magnitude to attention
**V** projections in all main blocks and both text-refiner blocks. Both split
Q/K/V and fused QKV projections are handled. The native attention backend,
normalization, rotary positions, model LoRAs and other model patches remain in
the computation. No extra negative diffusion pass is needed at CFG 1; the
separate negative-span text encodes do add prompt-encoding work and memory use.

Negative magnitude `0` removes that span. Empty negatives keep the native
positive-only computation. Positive prompt weighting otherwise follows the
native MOSS tokenizer; this path does not add positive-weight syntax to it.
Custom chat templates, embedding transforms that discard NegPiP metadata,
reference-image editing, compiled-model execution and third-party quantization
backends have not been validated. Reference-image editing is rejected explicitly.

Checks cover signed V projections, token/template alignment, batches, fused and
split QKV, model/CLIP cloning, repeated prompts and CFG-1 tensor predictions.
Passing these checks does not establish image quality or negative-prompt
effectiveness on a particular SFT/DMD combination.

## Compatibility

| Architecture | Status | Patch path |
| --- | --- | --- |
| Z-Image / Z-Image Turbo | Supported | Lumina2 / NextDiT / Qwen3-4B |
| Krea 2 | Supported | SingleStreamDiT / Qwen3-VL-4B / 12-layer text fusion |
| MOSS-Image / MOSS Turbo | Experimental | Native MOSSImage / Qwen3.5-9B / main + text-refiner V projections |
| SD1 | Supported | paired CLIP embeddings + cross-attention patch |
| SDXL / SDXL Refiner | Supported | paired CLIP embeddings + cross-attention patch |
| Anima | Supported | Qwen3-0.6B encoder + internal T5 weight mask + current Cosmos API |
| Flux | Not supported | upstream marks its NegPiP path as unmaintained |

The original workflow node ID, `ZImageNegPipPrompt`, is retained so workflows
made with version 1.x continue to load. The visible node name and category are
now model-neutral.

This package can be installed next to the original ComfyUI-ppm because it has a
unique node ID and internal patch keys. Do not stack two NegPiP nodes on the
same model/CLIP branch. If both connected inputs were already patched by
ComfyUI-ppm's **CLIP NegPip**, this node reuses that patch instead of applying a
second one.

The Anima implementation uses the current ComfyUI rotary-position API and does
not import the removed `apply_rotary_pos_emb` function from
`comfy.ldm.cosmos.predict2`.

## Development checks

With Python 3.11+ and PyTorch installed, run:

```sh
python -B -m unittest discover -s tests -v
```

The MOSS tests use real CPU tensors and small attention models with isolated
ComfyUI boundary doubles. They do not load checkpoint weights.

## Credits and license

This implementation is derived from:

- [ComfyUI-ppm](https://github.com/pamparamm/ComfyUI-ppm) by pamparamm;
- the Z-Image adaptation in
  [BigStationW/ComfyUI-ppm](https://github.com/BigStationW/ComfyUI-ppm);
- [ComfyUI-krea2-negpip](https://github.com/blue-pen5805/ComfyUI-krea2-negpip)
  by blue-pen5805 (adapted from commit
  [`3740add`](https://github.com/blue-pen5805/ComfyUI-krea2-negpip/commit/3740add9dbdc9f254a2befda30e95ba95e3b115d));
- [ComfyUI-NegPipPromptMerge](https://github.com/Deathspike/ComfyUI-NegPipPromptMerge)
  by Deathspike;
- NegPiP by laksjdjf and hako-mikan.

Released under the GNU Affero General Public License v3. See [LICENSE](LICENSE).
