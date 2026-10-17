# MiniMax H3 on multiple V100s

**Makes MiniMax H3 video generation practical on multi-GPU NVIDIA V100 machines.**

H3 produces video with synchronised sound, but it was built for modern datacenter
GPUs. On a V100 it is painfully slow, and ComfyUI will only ever use one of your GPUs
for it. This plugin splits each generation across all of them.

On our 8×V100 machine, the same clip went from **19 minutes to about 7**.

---

## Is this for you?

**Yes, if** you have two or more NVIDIA V100s (or another older multi-GPU box) and
H3 is too slow to be usable.

**No, if** you have a single GPU — this plugin does nothing for you. If you are on a
single V100 and hitting NaN or black frames, you want
[ComfyUI-MiniMaxH3-FP16Safe](https://github.com/aaalll12322/ComfyUI-MiniMaxH3-FP16Safe)
instead, which solves a different problem.

**Probably not, if** you have modern GPUs (A100, H100, RTX 40/50 series). H3 already
runs well there and this plugin is tuned for Volta's quirks.

---

## Before you install

- **No warranty.** Provided as-is, with no warranty of any kind. See LICENSE.
- **Installing changes nothing on your system.** No ComfyUI files are modified, and
  the plugin never touches your GPU settings. There is an optional tuning step later
  that does, but only if you choose to run it yourself.
- **Every number in this README comes from one machine** — 8× Tesla V100-SXM2-32GB on
  a DGX-1, one model, one resolution. That is what we measured, not what you should
  expect.
- **Tested on**, in case something misbehaves and you want to compare notes:

  | | |
  |---|---|
  | GPUs | 8× Tesla V100-SXM2-32GB (sm_70), NVLink, DGX-1 topology |
  | OS | Ubuntu 26.04, NVIDIA driver 580.x |
  | ComfyUI | 0.31.x, frontend package 1.48.x |
  | Python / PyTorch | 3.14 / 2.12 built against **CUDA 12.6** |
  | CUDA toolkit | 12.9 installed alongside (only needed for profiling tools) |
  | quantisation backends | `comfy-kitchen` 0.2.28, `comfy-aimdo` 0.4.13 |
  | other usual suspects | `safetensors` 0.7, `numpy` 2.4, `av` 17.0, `transformers` 5.8, `einops` 0.8, `triton` 3.7 |

  The two that actually caused us trouble were **`comfy-kitchen` and `comfy-aimdo`** —
  H3 will not load at all on older versions of either. If the plugin misbehaves in a
  way this README does not describe, check those two first.

  A note specific to Volta: we run PyTorch built against **CUDA 12.x**. CUDA 13 dropped
  *official* support for these GPUs — it may still work, but NVIDIA no longer verifies
  it and it is expected to degrade in later 13.x releases. We have not tested it. If
  you reinstall PyTorch, a cu12x build is the safe choice.

---

## Install

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/dg1kjd/comfyui-v100-sxm2-minimax-h3
```

Restart ComfyUI. No files in your ComfyUI installation are modified.

Requires a ComfyUI build that includes MiniMax H3 support (PR #15224).

---

## Use

**The quickest start** is to load one of the ready-made workflows in `examples/` —
drag the `.json` onto the ComfyUI canvas:

| file | what it does |
|---|---|
| `minimax-h3-text-to-video.json` | text prompt → video with sound |
| `minimax-h3-image-to-video.json` | still image → video with sound |
| `minimax-h3-reference-to-video.json` | reference image → video with sound |

They come wired with everything below already set up. You will need the H3 models in
your `models/` folders under their standard names, and you may want to lower
`num_gpus` on the Sequence Parallel and Parallel VAE Decode nodes to match your
machine.

### Things worth knowing about the example workflows

The node titles are kept short. The details that used to be crammed into them:

- **Sizes are constrained.** Width and height must be multiples of 32, with the total
  area no larger than 1344×768. Length must be one of 5, 22, 39, 56 … 124 frames.
- **The negative prompt node must match the positive one.** Same width, height and
  length — and for image-to-video and reference-to-video, the *same image wired in*.
  The start frame and reference ride along in the conditioning, so if the negative
  side does not carry them too, CFG cancels them out and you lose the reference.
- **Reference-to-video needs the `ref2va` checkpoint**, not `fl2va`, and you must
  address references by ordinal in the prompt — `<Picture 1>`, `<Video 1>`, `<Audio 1>`.
- **Do not drop below 16 steps.** 12 brings visible striping back on our test scene.
- **Reference-to-video wants a stronger oversaturation setting** — the example ships
  0.85 rather than the 0.7 used elsewhere. Copying 0.7 into it stripes badly.

### Or add it to a workflow you already have

Add **MiniMax H3 Sequence Parallel** to your H3 workflow, between the model loader
and the sampler, and set `num_gpus` to how many GPUs you want to use. That is the
whole setup.

```
UNET Loader → (sigma shift, etc.) → MiniMax H3 Sequence Parallel → KSampler
```

Set `num_gpus` to 1 and the node does nothing, so it is safe to leave in a workflow
you share with single-GPU users.

### The other three nodes

| node | what it does | when to use it |
|---|---|---|
| **MiniMax H3 Parallel VAE Decode** | Decodes the finished video across your GPUs instead of one | Always — turns a ~2.5 minute decode into a few seconds |
| **MiniMax H3 RescaleCFG** | Reduces oversaturation at high CFG | If you see neon-bright patches or banding on strongly coloured areas. Try 0.7. ComfyUI's built-in RescaleCFG crashes on H3, hence this one |
| **MiniMax H3 CFG Interval** | Applies CFG only during the early part of generation | Free speed. Try 0.0 to 0.6 — roughly 25% faster with no quality loss in our tests |

### Suggested starting point

What we use for final renders at 1344×768, 124 frames:

- 16 steps, `euler` / `simple`, CFG 6
- **Sequence Parallel** with all your GPUs
- **Parallel VAE Decode** with all your GPUs
- **RescaleCFG** at 0.7, video only
- **CFG Interval** 0.0 to 0.6

---

## What kind of speedup to expect

Measured on 8×V100-SXM2-32GB, 1344×768, 124 frames (about 5 seconds of video):

| | time |
|---|---|
| Before any of this work | ~19 min |
| Sequence parallelism + tuning | ~12 min |
| Plus CFG Interval and 16 steps | **~7 min** |

Your mileage will vary with GPU count, model size and resolution. **Short clips at
low resolution benefit much less** — there isn't enough work to spread across GPUs,
and the coordination overhead can outweigh the gain. This plugin is aimed at the
big, slow renders where you actually feel the wait.

---

## Tuning

One of these is already on by default (keeping the model resident). The rest are
opt-in, and the plugin works fine without any of them.

### Lock your GPU clocks (worth ~13% for us)

This is the single biggest gain after the parallelism itself, and the only step that
**changes your machine rather than just ComfyUI**: it needs root, it stays in effect
after ComfyUI exits until you undo it with `sudo nvidia-smi -rgc`, and it does not
survive a reboot.

It sounds backwards, because the clock you want is *lower* than the GPUs' maximum.
When several GPUs wait for each other hundreds of times per image, the slowest one at
any instant sets the pace — and GPUs left to manage their own clocks constantly speed
up and slow down out of step with one another. A steady, sustainable clock beats a
jittery higher one.

⚠️ **Locking too high is worse than not locking at all.** On our machine, locking to
the 1530 MHz maximum pushed the cards past their power limit, made them throttle a
third of the time, and ended up *slower than leaving them alone*.

There is no universal value — ours was 1290 MHz on V100-SXM2-32GB and yours will
differ. Pick the highest clock your cards sustain without ever throttling:

```bash
nvidia-smi --query-supported-clocks=graphics --format=csv,noheader -i 0   # candidates
sudo nvidia-smi -lgc <mhz>,<mhz>                                          # try one
# then, DURING a render, check it holds and never throttles:
nvidia-smi --query-gpu=index,clocks.sm,power.draw,clocks_throttle_reasons.active \
           --format=csv -lms 500
```

The reported clock should sit exactly at your chosen value and the throttle reasons
should stay `0x0...0` for the whole render. If it dips or throttles, step down. Sample
*during* a render — clocks read between renders tell you nothing.

### Keeping the model fully resident (on by default)

The **Sequence Parallel** node has a `keep_weights_resident` checkbox, **on by
default**. It was worth about **7%** on our machine and made render times noticeably
more consistent run to run.

ComfyUI decides how much of the model to keep in VRAM based on the size of the whole
sequence, without knowing this plugin splits that sequence across GPUs — so it holds
back more memory than needed and pages weights that could have stayed resident. This
tells it to load the model fully.

⚠️ **If you run out of memory, untick it.** With it on, every GPU must hold a complete
copy of the model with nothing paged out. That is the trade: faster, but no VRAM
headroom.

### Choosing which GPUs to use

`CUDA_VISIBLE_DEVICES` works, but **only if you are not passing `--default-device`** —
that flag makes ComfyUI overwrite the variable with every device on the system,
silently discarding your setting. Use ComfyUI's `--cuda-device` instead, or drop
`--default-device`. Either way the nodes clamp to whatever is actually visible, so a
workflow saved asking for 8 GPUs runs fine on 2.

### Interconnect layout

The multi-GPU communication is tuned for an NVIDIA DGX-1 style layout, where GPUs are
connected by NVLink in two groups of four. On a different topology it still works
correctly, but may be slower than it could be. `nvidia-smi topo -m` shows yours.

---

## Troubleshooting

**Nothing got faster.** Check that `num_gpus` is above 1 and that ComfyUI can see all
your GPUs. The log should show one "loaded completely" line per GPU at the start of a
render.

**Out of memory partway through a session, in the video decode.** Parallel decode
holds a VAE copy per GPU on top of everything else, so it can be the straw that breaks
a long session. Just re-queue — ComfyUI unloads and the retry usually succeeds. If it
keeps happening, lower `num_gpus` on that node or swap in ComfyUI's stock VAE Decode.

**Out of memory.** First, untick `keep_weights_resident` on the Sequence Parallel
node — it is on by default and trades VRAM headroom for speed. If that is not
enough: each GPU holds a full copy of the model, so lower `num_gpus` or use a
smaller H3 checkpoint.

**Speeds vary a lot between runs.** Your GPUs are probably changing clock speed on
their own. See the clock locking note above.

**It works but the video looks oversaturated.** Add the RescaleCFG node at 0.7, or
lower your CFG.

---

## How it works, briefly

H3 processes a long sequence of tokens carrying both video and audio. Most of that
work is per-token, so it splits across GPUs cleanly. Attention is the exception — it
needs every token at once — so just before each attention step the data is
redistributed so that each GPU holds the whole sequence for a few attention heads
instead of part of the sequence for all of them, and afterwards it is redistributed
back. This is known as Ulysses sequence parallelism.

The redistribution runs over NVLink where available, routing around the slower PCIe
connections between GPU groups. It runs in a single process with one thread per GPU —
no NCCL, no `torchrun`, nothing to configure.

**On exactness.** The sequence split itself is exact — with the two speed options
below turned off, the sharded result is bit-identical to single-GPU output
(`cos=1.00000000`, `max_abs=0`, verifiable on your own machine by setting
`COMFY_MINIMAX_SP_SELFTEST=1`, which runs the single-GPU loop alongside and compares).

By default two further optimisations are enabled, and they are *numerically
equivalent* rather than bit-identical — attention is computed in fp16, and the data
exchanged between GPUs is sent as fp16. Output quality is unaffected in our testing,
but a fixed seed will not reproduce a single-GPU render exactly. If you need
bit-for-bit reproducibility against single-GPU output, set both
`COMFY_MINIMAX_SP_FP16_ATTN=0` and `COMFY_MINIMAX_SP_FP16_COMM=0` — at a significant
speed cost.

Both fp16 paths watch for values too large to represent. That check is made once per
denoising step rather than on every one of the 400 transfers within it, because reading
it more often stalls all eight GPUs — worth about 3%. In the unlikely event it ever
triggers, the plugin logs it clearly and switches fp16 transfers off for the rest of the
session; `COMFY_MINIMAX_SP_SYNCFREE=0` restores the older per-transfer check instead.

---

## Credit and licence

Sequence parallelism, the NVLink routing, the multi-GPU VAE decode and the H3-specific
nodes here are our own work. The parallel VAE decode mirrors the structure of
ComfyUI's own `decode_temporal`, and the plugin links against ComfyUI internals
throughout — thanks to the ComfyUI authors.

Separately, [aaalll12322's ComfyUI-MiniMaxH3-FP16Safe](https://github.com/aaalll12322/ComfyUI-MiniMaxH3-FP16Safe)
solves the single-GPU numerical problem on V100 and is worth reading if you are on one
GPU. None of its code is included here.

Licensed **GPL-3.0**, matching ComfyUI.
