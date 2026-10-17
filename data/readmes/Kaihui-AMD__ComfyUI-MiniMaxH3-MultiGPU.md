# ComfyUI-MiniMaxH3-MultiGPU

**English** | [中文](README_zh.md)

Clean-room, AMD-focused multi-GPU inference for MiniMax H3 in ComfyUI.

The current release is optimized and validated for **two GPUs**. It accelerates
one video generation job by splitting the H3 transformer sequence and attention
heads across both GPUs. It does not create an extra CFG branch, reduce sampling
steps, skip transformer blocks, or introduce an approximate cache.

The design is inspired by the public
[DeepSpeed Ulysses paper](https://arxiv.org/abs/2309.14509). The implementation
was written against ComfyUI's official MiniMax H3 model and does not copy source
code from another H3 multi-GPU extension.

## Results

Measured on September 8, 2026:

- 2 x AMD Radeon AI PRO R9700 32 GB
- PCIe, two hops between GPUs
- ROCm 7.2.4
- PyTorch 2.10.0
- ComfyUI 0.30.0
- MiniMax H3 INT8 ConvRot
- 864 x 480, 124 frames, 20 steps
- `res_multistep` sampler and `BasicGuider`

| Mode | Denoise | End to end |
| --- | ---: | ---: |
| Single GPU | about 240.6 s | 262.34 s |
| Two GPUs | about 129.0 s | **149.16 s** |
| Speedup | **1.87x** | **1.76x** |

Three consecutive warm two-GPU runs completed in:

```text
150.170 s
148.161 s
149.160 s
```

The median was **149.160 seconds**, a **43.1% latency reduction** from the
same-version single-GPU baseline.

Rank 1 allocates about **15.46 GiB** immediately after loading the sharded and
pruned model. Both GPUs remain below approximately 26 GiB during repeated
124-frame generation.

Cold startup is intentionally excluded. Loading the 32B text encoder and both
DiT ranks can take more than 20 minutes on the test machine.

## Requirements

- Linux
- Two AMD GPUs visible to ROCm
- ROCm with RCCL-enabled PyTorch
- ComfyUI 0.30.0
- MiniMax H3 model files:

```text
ComfyUI/models/
├── diffusion_models/
│   └── minimax_h3_fl2va_pruned_int8_convrot.safetensors
├── text_encoders/
│   └── qwen3vl_32b_minimax_h3_int8_convrot.safetensors
└── vae/
    ├── minimax_h3_video_vae_fp16.safetensors
    └── minimax_h3_audio_vae_fp32.safetensors
```

The repository currently targets exactly two GPUs. Other GPU counts are not
enabled in the public node until they have passed full-model validation.

## Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Kaihui-AMD/ComfyUI-MiniMaxH3-MultiGPU.git
```

No additional Python packages are required beyond a working MiniMax H3
ComfyUI environment.

## Cloud Reproduction

- AMD GPU free cloud platform:
  [Kaihui-AMD/AMD_YES_Cloud](https://github.com/Kaihui-AMD/AMD_YES_Cloud)
- RC cloud reproduction guide:
  [minimax-h3-multigpu.md](https://github.com/Kaihui-AMD/AMD_YES_Cloud/blob/main/bilibili/minimax-h3-amd/minimax-h3-multigpu.md)

## Launch

Use `ROCR_VISIBLE_DEVICES` to expose exactly the two target GPUs. UUIDs are
recommended:

```bash
env -u HIP_VISIBLE_DEVICES -u CUDA_VISIBLE_DEVICES \
ROCR_VISIBLE_DEVICES=GPU-UUID-0,GPU-UUID-1 \
python main.py \
  --listen 0.0.0.0 \
  --port 8188 \
  --highvram
```

Do not set conflicting `HIP_VISIBLE_DEVICES`, `ROCR_VISIBLE_DEVICES`, and
`CUDA_VISIBLE_DEVICES` values. Conflicting visibility masks can map both ranks
to the same physical GPU.

## Usage

1. Import [the GUI workflow](examples/workflow_ui_2gpu.json) into ComfyUI.
2. Select `AMDMinimaxH3SequenceParallelLoader`.
3. Select the MiniMax H3 diffusion checkpoint.
4. Leave `weight_dtype=default`.
5. Leave `devices=auto` when ComfyUI was launched with exactly two visible GPUs.
6. Keep the stock `VAEDecode` and `VAEDecodeAudio` nodes.
7. Queue the workflow once to load both model ranks. Later runs reuse them.

Loader inputs:

| Input | Default | Description |
| --- | --- | --- |
| `unet_name` | required | MiniMax H3 diffusion checkpoint |
| `weight_dtype` | `default` | Same dtype policy as ComfyUI's loader |
| `devices` | `auto` | Two physical IDs/UUIDs, or the visible-device environment |
| `port` | `29541` | Local distributed rendezvous port |

API users can start with
[the API workflow](examples/workflow_api_2gpu.json).

### Video duration

The `length` input is a frame count at 24 FPS. H3 aligns it to `17n + 5`.

| Approximate duration | `length` |
| ---: | ---: |
| 1 second | 22 |
| 3 seconds | 73 |
| 5 seconds | 124 |
| 8 seconds | 192 |
| 10 seconds | 243 |

Keep `CreateVideo.fps=24` to preserve audio synchronization.

## How It Works

MiniMax H3 packs text, visual conditioning, audio, and video tokens into one
sequence processed by a 56-head DiT.

For every transformer block:

1. Each rank processes half of the token rows for token-local operations.
2. QKV weights and per-output-channel INT8 scales are permanently sharded to
   28 heads per GPU.
3. The local QKV projection overlaps the peer token transfer.
4. Each rank computes exact full-sequence attention for its 28 heads.
5. A head-to-sequence exchange sends only the peer-head rows needed by the
   receiving rank.
6. Each rank runs the original full-width `out_proj` on its local sequence rows.
7. MLP and residual operations remain sequence-local.

Rank 0 performs input packing, text refinement, and the final video/audio output
heads. Rank 1 retains only the 50 main transformer blocks.

Keeping the full output projection is important for INT8 ConvRot: splitting it
before activation quantization changes the per-row activation scale. The tested
head-to-sequence path preserves the original quantized projection exactly.

## Memory Management

The loader reserves 8 GiB for sequence-parallel activations so ComfyUI unloads
the text encoder or VAE before denoising:

```bash
AMD_H3_SP_ACTIVATION_RESERVE_GB=8
```

Each new prompt also clears stale allocator cache on rank 1 while retaining its
model weights.

## Verification

Run the CPU mathematical tests:

```bash
python -m pytest -q
```

Run the two-GPU RCCL peer-transfer test:

```bash
torchrun --standalone --nproc_per_node=2 tests/distributed_smoke.py
```

Run parity with a real INT8 ConvRot attention block:

```bash
python tests/quantized_attention_parity.py \
  --comfy-root /path/to/ComfyUI \
  --model /path/to/minimax_h3_fl2va_pruned_int8_convrot.safetensors
```

Measured result:

```text
max_abs=0
mean_abs=0
max_rel=0
```

## Benchmark

With ComfyUI running:

```bash
python scripts/benchmark.py \
  --server http://127.0.0.1:8188 \
  --workflow examples/workflow_api_2gpu.json \
  --length 124 \
  --steps 20 \
  --runs 3
```

The first run includes model loading. Use later runs for steady-state latency.

## Limitations

- Exactly two GPUs are currently supported and validated.
- Native Windows is not supported because the runtime requires NCCL/RCCL.
- Video and audio VAE decode remain on the primary GPU.
- ComfyUI releases newer than 0.30.0 have not yet been validated.

## License

MIT
