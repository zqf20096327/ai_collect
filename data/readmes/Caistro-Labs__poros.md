<img src="https://raw.githubusercontent.com/Caistro-Labs/poros/main/docs/assets/poros-banner.png" width="100%" alt="Poros. Fine-tune models bigger than your GPU.">

<p align="center">
<a href="https://github.com/Caistro-Labs/poros/blob/main/LICENSE"><img src="https://raw.githubusercontent.com/Caistro-Labs/poros/main/docs/assets/badge-license.png" height="37" alt="license Apache-2.0"></a><a href="https://github.com/Caistro-Labs/poros/blob/main/docs/index.md"><img src="https://raw.githubusercontent.com/Caistro-Labs/poros/main/docs/assets/chip-docs.png" height="37" alt="docs"></a><a href="https://github.com/Caistro-Labs/poros/blob/main/paper/poros.pdf"><img src="https://raw.githubusercontent.com/Caistro-Labs/poros/main/docs/assets/chip-paper.png" height="37" alt="paper"></a>
</p>

**Poros** is a streaming LoRA fine-tuning engine for models larger than GPU or unified memory. It keeps frozen 4-bit base weights in host RAM or on SSD and streams one block of layers through the GPU at a time while training the adapters. On dense models that fit in VRAM, streamed training matches a standard resident run under `torch.equal`.

Supports SFT, DPO, IPO, KTO, ORPO, and SimPO on Linux (NVIDIA Ampere+) and Apple silicon (macOS 14+).

## Quickstart

```bash
pip install poros-train
```

Installs Poros with `torch`, `transformers`, `peft`, and `bitsandbytes` (macOS skips `bitsandbytes`). Runs on Linux with NVIDIA (compute capability 8.0+, Ampere or newer) and Apple silicon (macOS 14+). [Installation](https://github.com/Caistro-Labs/poros/blob/main/docs/install.md).

```bash
poros machine                                         # checks GPU, driver, RAM, disk and software; prints the next command
poros recipes                                         # the certified runs, and the machine each ran on
poros train qwen2.5-0.5b-instruct --data chats.jsonl  # start small
poros export last --format merged                     # export a merged model for vLLM or TGI
```

In Python, `poros.Run` gives you a plain training loop one step at a time:

```python
import poros

run = poros.Run.create("Qwen/Qwen2.5-7B-Instruct", rank=16, length=512, dataset="chats.jsonl")
data = poros.data.chats("chats.jsonl", run.tokenizer, length=512)
for step in run.steps(200):
    run.forward_backward(data.batch(step))
    run.optim_step()
run.save()   # prints where: ./poros_output/checkpoint-199
```

Chats train with **SFT** and preference pairs train with **DPO** automatically; **IPO, KTO, ORPO, and SimPO** are built in too. See [Quickstart](https://github.com/Caistro-Labs/poros/blob/main/docs/quickstart.md) and [Training](https://github.com/Caistro-Labs/poros/blob/main/docs/training.md).

## Results

<!-- fill:top -->
<table>
  <tr>
    <td width="50%" valign="top">
      <img src="https://raw.githubusercontent.com/Caistro-Labs/poros/main/docs/assets/readme-72b-4090.png" width="100%" alt="Qwen2.5-72B on one 24 GB RTX 4090. All on the GPU: 41.4 of 24 GiB. Poros: 13.5 GiB, at 17.7 s per step.">
      <p><b>RTX 4090 (24 GB):</b> Qwen2.5-72B (41.4 GiB in 4-bit) trains in 13.5 GiB VRAM reserved (9.9 GiB allocated) and 45.1 GiB host RAM at 17.7 s/step (512-token rows, rank 16, 8 rows/step; benchmark run on a 59.6 GiB host).</p>
    </td>
    <td width="50%" valign="top">
      <img src="https://raw.githubusercontent.com/Caistro-Labs/poros/main/docs/assets/readme-mac.png" width="100%" alt="Qwen2.5-72B on a 16 GB Mac, an Apple M4. Peak memory 11.4 GiB. The 4-bit model 38.4 GiB. Step time 41.1 s. 128-token rows.">
      <p><b>M4 Mac (16 GB):</b> Qwen2.5-72B-Instruct (38.4 GiB in 4-bit) streams from an external USB4 SSD at 11.4 GiB peak unified memory and 41.1 s/step on 128-token rows (6-step run). A 144-step run from the internal SSD took loss on 4 held-out rows from 3.01 to 0.68 at 37.9 s/step.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img src="https://raw.githubusercontent.com/Caistro-Labs/poros/main/docs/assets/readme-laptop.png" width="100%" alt="Qwen3-30B-A3B on an 8 GB gaming laptop, an RTX 4060 Laptop GPU. Peak VRAM 6.0 GiB. Step time 13.6 s. LoRA rank 8, 256-token rows (expert store built on the laptop).">
      <p><b>RTX 4060 Laptop (8 GB):</b> Qwen3-30B-A3B trains in 6.0 GiB VRAM and 6.4 GiB host RAM at 13.6 s/step (LoRA rank 8, 256-token rows; expert store built on the laptop; measured run, the recipe is certified on the RTX 4090).</p>
    </td>
    <td width="50%" valign="top">
      <img src="https://raw.githubusercontent.com/Caistro-Labs/poros/main/docs/assets/readme-moe.png" width="100%" alt="Qwen3-30B-A3B on an RTX 4090 with its experts on the SSD, --store ssd. VRAM 21.6 GiB. System RAM 11.2 GiB. 4.3 s per step.">
      <p><b>MoE experts on disk (<code>--store ssd</code>):</b> Qwen3-30B-A3B on an RTX 4090 runs in 21.6 GiB VRAM and 11.2 GiB host RAM at 4.3 s/step (the <code>moe-30b-ssd</code> recipe, <code>fast</code> path). With experts in host RAM it takes 19.9 GiB of RAM and 9.1 GiB of VRAM.</p>
    </td>
  </tr>
</table>

Host RAM is peak process memory excluding droppable checkpoint file pages. Every setting and run is in [Benchmarks](https://github.com/Caistro-Labs/poros/blob/main/docs/bench.md).
<!-- /fill:top -->

The raw benchmark logs behind these figures live in a companion repository,
[Caistro-Labs/poros-benchmarks](https://github.com/Caistro-Labs/poros-benchmarks), at the same
`docs/validation/` paths the docs, the package and the paper cite.

<!-- fill:performance -->
## Performance

Measured on an RTX 4090 (24 GB VRAM, 59.6 GiB RAM) with batch 1, gradient accumulation 8, 512-token rows, and LoRA rank 16. The `efficient` setting is the default and uses less GPU memory; `fast` uses more GPU memory and takes less time per step.

| Model | Setting | Time / step | VRAM reserved | Host RAM (peak) |
|---|---|---:|---:|---:|
| Qwen2.5-72B | efficient (default) | 17.7 s | 13.5 GiB | 45.1 GiB |
| Qwen3-30B-A3B | efficient (default) | 4.6 s | 9.1 GiB | 19.9 GiB |

Each figure is the median of three interleaved runs in one session. VRAM is peak reserved across load and training; host RAM excludes droppable checkpoint file pages. Full protocol and runs: [Benchmarks](https://github.com/Caistro-Labs/poros/blob/main/docs/bench.md) and [Reproducibility](https://github.com/Caistro-Labs/poros/blob/main/docs/training.md#reproducibility).
<!-- /fill:performance -->

## How it works

<img src="https://raw.githubusercontent.com/Caistro-Labs/poros/main/docs/assets/readme-how.png" width="100%" alt="How it works: one block on the GPU at a time. Forward: stream in a block of layers from host RAM, run it and drop it, so the adapters stay. Backward: stream each block in again in reverse order, restore its random state and recompute it to take gradients. The GPU holds the adapters and one block; the base waits in host RAM.">

In QLoRA, the base weights are frozen and never receive gradients, so keeping all 80 layers pinned in VRAM only crowds out everything else. Poros leaves the 4-bit base in host RAM (or on an SSD for MoE experts and Apple silicon), streams one block onto the GPU for the forward pass, keeps activations only at block boundaries, drops the weights, then reloads blocks in reverse to recompute during backward.

Before each block's forward pass, Poros snapshots CPU and CUDA RNG state and restores it during backward recomputation so dropout masks stay identical. On dense models that fit on the card, the adapter matches a fully on-GPU run under `torch.equal` (checked over 200 steps with dropout off), and you can verify it on your own machine with `poros prove`. For MoE models like Qwen3-30B-A3B (128 experts per layer, 8 active per token), `--store ssd` streams only the routed experts into VRAM. See [Streaming and memory](https://github.com/Caistro-Labs/poros/blob/main/docs/streaming.md).

## Supported models and limits

The models below are examples: any model of a listed architecture trains at any size with no extra flags; see [Architectures](https://github.com/Caistro-Labs/poros/blob/main/docs/architectures.md).

| | |
|---|---|
| **Dense** | |
| Qwen2.5 | Qwen2.5-0.5B, 7B, 32B and 72B and their Instruct versions; DeepSeek-R1-Distill-Qwen-1.5B |
| Qwen3 | Qwen3-0.6B, Qwen3-32B |
| Qwen3.5 / 3.6 / 3.8 | Qwen3.5-4B, Qwen3.8-27B |
| Gemma 3 | gemma-3-1b, gemma-3-27b |
| Gemma 4 | gemma-4-31B (not E2B or E4B) |
| **MoE** | |
| Qwen3 MoE | Qwen3-30B-A3B, Qwen3-Coder-30B-A3B |
| Qwen3.5 / 3.6 MoE | Qwen3.6-35B-A3B |
| Gemma 4 MoE | gemma-4-26B-A4B |
| OLMoE | OLMoE-1B-7B |
| Qwen2 MoE | Qwen1.5-MoE-A2.7B |
| DeepSeek-V2 | DeepSeek-V2-Lite |
| **Machines** | |
| NVIDIA | Linux, compute capability 8.0 or newer (Ampere, Ada, Hopper, Blackwell) |
| Mac | Apple silicon, macOS 14 or later |

Run `poros check <model>` to check any model's `config.json` before downloading. Other architectures still train, with no check behind them; see [Models](https://github.com/Caistro-Labs/poros/blob/main/docs/models.md).

**Limits to know upfront:**
- **Single GPU, LoRA only:** multi-GPU and full fine-tuning are not supported yet.
- **Slower when a model already fits:** streaming adds transfer overhead on every step, so train resident whenever a model fits comfortably on your card.
- **Host RAM and disk space:** dense models live in host RAM (the 72B's peak is in [Results](#results)); `--store ssd` builds the [SSD expert store](https://github.com/Caistro-Labs/poros/blob/main/docs/streaming.md#the-ssd-expert-store) from the full download, so disk needs room for both.
- **Platform:** Windows is not supported and WSL2 is untested. Full list in [Limits](https://github.com/Caistro-Labs/poros/blob/main/docs/limitations.md).

[The docs](https://github.com/Caistro-Labs/poros/blob/main/docs/index.md) are also at [caistrolabs.com/docs](https://caistrolabs.com/docs/), and `poros docs` serves them offline. Coding agents read [AGENTS.md](https://github.com/Caistro-Labs/poros/blob/main/AGENTS.md) and `poros agents`. To cite Poros, use [CITATION.cff](https://github.com/Caistro-Labs/poros/blob/main/CITATION.cff).

## License

Poros is [Apache-2.0](https://github.com/Caistro-Labs/poros/blob/main/LICENSE), built by [Caistro Labs](https://caistrolabs.com). Report a bug in [issues](https://github.com/Caistro-Labs/poros/issues) or share an idea in [Discussions](https://github.com/Caistro-Labs/poros/discussions); [CONTRIBUTING.md](https://github.com/Caistro-Labs/poros/blob/main/CONTRIBUTING.md) explains how.

Qwen2.5-72B and its Instruct model use the Qwen license; Poros itself is Apache-2.0.
