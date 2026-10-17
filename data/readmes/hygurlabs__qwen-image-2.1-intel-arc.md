# Qwen-Image-2.1 on an Intel Arc Pro B70

Qwen-Image-2.1 generates, edits and cuts out images on an **Intel Arc Pro B70**
through PyTorch XPU. One 1024x1024 image in **52 seconds**, native 2K in two
minutes, instruction editing in 63 seconds, and real alpha-channel output.

An RTX 5080 16 GB is about twice as fast at 1024 and three times at 2K. Both
columns are in the table below, measured the same way, so you can decide which
trade you want.

## What was actually uncertain

ComfyUI lists Intel Arc as natively supported through `torch.xpu`, so the
platform was never in question. What no public source covered is whether the
**INT8 ConvRot** repacked weights — the ones the official ComfyUI templates
use for both the diffusion model and the Qwen3-VL text encoder — run outside
CUDA at all. The model card states no hardware requirement and its examples
are written for CUDA; the installation guide this work started from pins
`cu130` wheels and warns that GGUF support says nothing about the INT8 encoder.

They run. The images below were checked by eye, not by exit code.

## Measurements

`server_seconds` is ComfyUI's own timing for a completed job, end to end:
load, encode, sample, decode, save. Euler / simple, CFG 1, denoise 1, batch 1.

| Task | Resolution | Steps | RTX 5080 16 GB | Arc Pro B70 32 GiB |
|---|---|---:|---:|---:|
| INT8 text-to-image | 1024x1024 | 40 | 27.0 s | 52.0 s |
| INT8 text-to-image | 2048x1152 | 50 | 42.4 s | 125.2 s |
| INT8 transparent (RGBA) | 1024x1024 | 40 | 27.1 s | 52.8 s |
| INT8 instruction edit | 1024x1024 | 40 | 57.2 s | 63.3 s |
| GGUF Q4_K_M, CPU text encoder | 1024x1024 | 40 | 48.4 s | 78.0 s |
| GGUF Q4_K_M, GPU text encoder | 1024x1024 | 40 | not measured | 56.1 s |

The edit row is the interesting one. On the 16 GB card, editing an image cost
**twice** what generating one cost, because the time went into swapping weights
in and out under `--lowvram`. On the B70 the gap falls to 20%. The bottleneck
changed kind: the machine stopped waiting on memory and started computing.

`--lowvram` is pointless on the B70 — 51.97 s against 52.13 s at 1024, 125.17
against 125.69 at 2K. 32 GiB hold the 16.6 GB of INT8 weights with nothing
offloaded, so the launcher here does not pass it.

Full conditions, versions and caveats: [results/results.md](results/results.md).

## Examples

| INT8 on the B70 | Transparent (real alpha) | Instruction edit |
|---|---|---|
| ![teapot](examples/b70-int8-1024-teapot.png) | ![fox](examples/b70-int8-1024-transparent-fox.png) | ![sunflowers](examples/rtx5080-int8-edit-sunflowers.png) |

The transparent PNG carries 566,583 fully transparent pixels and an alpha range
of 0-255. A checkerboard in a viewer proves nothing; `scripts/check-alpha.py`
reads the channel.

## Install on Intel (Linux)

Needs a working Intel GPU driver — check `xpu-smi discovery` or `clinfo -l`
first — plus git and Python 3.10-3.13. The script installs nothing system-wide.

```bash
./install/install-xpu.sh ~/ComfyUI-Qwen21-XPU
```

It clones ComfyUI at a pinned commit, builds a venv with `torch==2.13.0+xpu`
from PyTorch's XPU index, adds the GGUF loader node at its validated commit,
and stops. Weights are a separate step, so you choose which set you want.

Model files go under `<install>/models/`:

| File | Size | Into |
|---|---:|---|
| `qwen_image_2.1_int8_convrot.safetensors` | 7.26 GB | `diffusion_models/` |
| `qwen3vl_8b_int8_convrot.safetensors` | 9.35 GB | `text_encoders/` |
| `qwen_image_2.1_vae_bf16.safetensors` | 0.68 GB | `vae/` |

They are the [official ComfyUI repack](https://huggingface.co/Comfy-Org/Qwen-Image-2.1)
at revision `b8abad0`. The GGUF variant swaps only the diffusion file for
`qwen-image-2.1-Q4_K_M.gguf` (4.60 GB) and reuses the same encoder and VAE.

## Serve it on the LAN

```bash
./scripts/serve.sh ~/ComfyUI-Qwen21-XPU            # loopback, port 8188
./scripts/serve.sh ~/ComfyUI-Qwen21-XPU --lan      # every interface
./scripts/serve.sh ~/ComfyUI-Qwen21-XPU --lan --port 8189
```

`--lan` binds `0.0.0.0` and prints the address to hand to another machine.
**ComfyUI has no authentication**: only do this on a network you trust, and
never expose it to the internet. Without `--lan` it stays on loopback and an
SSH tunnel (`ssh -N -L 8188:127.0.0.1:8188 user@host`) is the safe way in.

The script auto-detects XPU, CUDA or CPU and says which one it picked, so it
works on the NVIDIA side of this comparison too.

## Reproduce the numbers

```bash
./scripts/bench.sh ~/ComfyUI-Qwen21-XPU http://127.0.0.1:8188
```

Two traps it handles for you, both of which cost real time here. **Never reuse
a seed**: ComfyUI serves the cached graph and reports `0.001 s`, which looks
like a triumph and means nothing. And **throw away the first job after a
launch** — it pays for loading the weights (70.6 s against 52.1 s afterwards).

## What this does not tell you

Throughput says nothing about quality. INT8 ConvRot and Q4_K_M are not the same
degradation and nothing here measures the difference. The timings come from one
prompt family, run once each, on one machine per vendor. The RTX 5080 has since
been removed from that machine, so its column is frozen and cannot be extended.

## Credits and licence

The installation recipe, the workflow structure and the benchmark modes are
derived from [alesha-pro/tools](https://github.com/alesha-pro/tools/tree/main/qwen-image-2.1)
(MIT), which documents the CUDA path in detail and is the right place to start
on NVIDIA. This repository adds the Intel XPU path and its measurements.

See [NOTICE.md](NOTICE.md) for upstream attribution and the model licence.
Scripts are [MIT](LICENSE); documentation and measurements are
[CC BY 4.0](LICENSE-DOCS). The weights carry the Qwen Research License.
