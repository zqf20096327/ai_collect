# VVLA

**VVLA is a high-throughput single-GPU inference and dynamic-batching engine for Vision-Language-Action models.**

<p align="center">
  | <a href="#demo"><b>Demo</b></a>
  | <a href="#benchmarks"><b>Benchmarks</b></a>
  | <a href="#quick-start"><b>Quick Start</b></a>
  | <a href="#supported-models-and-hardware"><b>Support</b></a>
  | <a href="docs/INSTALL.md"><b>Install</b></a>
  | <a href="docs/API.md"><b>API</b></a> |
</p>

**VVLA** is a comprehensive single-GPU inference and serving engine for **π0.5**, **OpenVLA-OFT**, and **LingBot-VLA2** across datacenter and consumer NVIDIA GPUs (**RTX PRO 6000**, **A100**, **RTX 4090**, and **RTX 3090**). It is built to perform across the full deployment spectrum—from low-latency single-arm execution to asynchronous multi-arm fleets and high-concurrency simulation rollouts—without sacrificing closed-loop manipulation accuracy.

Under **asynchronous multi-client and multi-arm workloads**, VVLA scales π0.5 to **111.7 chunks/s** (**2.11×** FlashRT FP8, **2.21×** EmbodiInfer HTTP, **5.06×** compiled LeRobot), sustains **8–9 real-time 20 Hz arms** (**+38%** to **2.56×** fleet task throughput), and accelerates mixed-prompt 6B MoE LingBot-VLA2 by **5.94×** with **zero CUDA Graph rebuilds**. At **single-request (batch 1)** execution, VVLA also lowers median latency against compiled official baselines on **9 of 10** model–GPU pairs (down to **22.55 ms** on π0.5 and **32.48 ms** on OpenVLA-OFT), cuts π0.5 peak VRAM by **35–48%**, and unlocks 6B MoE execution on **24 GB** GPUs where official FP32 runs out of memory.

## Demo

[![VVLA Multi-Arm and Split-Stage Demo](assets/vvla_demo.webp)](assets/vvla_demo.mp4)

**Act 1 (1× real-time):** 9 independent 20 Hz LIBERO arms sharing one RTX PRO 6000 (π0.5) — VVLA completes **18 tasks** vs. **4** for FlashRT FP8 in the same 15 s window (**2.0%** vs. **44.3%** starved ticks). **Act 2 (2× speed):** 4 distinct RoboTwin 2.0 bimanual tasks sharing one RTX PRO 6000 (LingBot-VLA2) — VVLA finishes all 4 tasks with **4.7× less GPU inference time** (**1.72 s** vs. **8.14 s**) and **0 CUDA Graph rebuilds**. [Watch full 1080p video with audio](assets/vvla_demo.mp4).

## VVLA is fast with:

- **Zero-padding dynamic batching**: packs independent, asynchronously arriving clients into exact verified batch widths (`1, 2, 4, 8, 16`) with zero dummy work and immediate per-batch return over binary IPC, HTTP, or WebSocket
- **Split-Stage CUDA Graph reuse**: runs variable-length VLM prefixes outside the graph into paged KV cache and replays one static 10-step MoE suffix graph per batch width, eliminating steady-state graph rebuilds under mixed prompts
- **Calibration-free precision & fused execution**: fuses policy operators across CUDA Graphs, quantizes only high-leverage linear projections on Ada/Blackwell GPUs with zero offline calibration, and preserves FP32 control scalars where low precision breaks manipulation
- **Memory-aware cross-GPU dispatch**: automatically adjusts kernels, weight packing, and batch ceilings to each GPU's architecture and free VRAM—unlocking 6B MoE LingBot-VLA2 and batched OpenVLA-OFT on 24 GB consumer cards

## VVLA is easy to use with:

- **3-line Python API**: `vvla.load("pi05", checkpoint=...).infer_batch([obs], [seed])`
- **One CLI for direct, fixed-batch, and multi-client serving**: switch from dedicated single-arm calls to a shared binary HTTP / WebSocket server with `vvla serve`
- **Process-isolated policy workers**: each model runs in its own isolated Python environment, eliminating `transformers`, `numpy`, and custom CUDA extension conflicts across π0.5, OpenVLA-OFT, and LingBot-VLA2
- **Deadline-aware scheduling on demand**: defaults to low-overhead FIFO and offers optional `cohort-slack-edf` predictive admission for overloaded real-time robot fleets

## Benchmarks

All numbers measure full end-to-end execution from raw CPU observations to independently owned CPU `float32` action chunks on Linux x86_64 (Python 3.12, PyTorch 2.13.0, CUDA 13.0). Full methodology and per-card details live in [Support Matrix](docs/SUPPORT_MATRIX.md) and [Benchmarking](docs/TESTING.md).

### Multi-Client Serving Scaling — π0.5 on RTX PRO 6000

How well one GPU scales when 8, 16, or 32 independent robots or rollout workers submit requests concurrently (throughput in **chunks/s**, higher is better):

| Engine | Precision | 8 Clients | 16 Clients | 32 Clients | P95 Latency (32 Clients) |
|---|---|---:|---:|---:|---:|
| LeRobot (Compiled) | Default | 22.09 | 22.10 | 22.09 | 1,450.5 ms |
| FlashRT | BF16 | 40.81 | 40.81 | 40.79 | 785.4 ms |
| EmbodiInfer (HTTP) | BF16 | 44.13 | 45.87 | 48.80 | 664.1 ms |
| FlashRT | FP8 | 52.91 | 52.89 | 52.89 | 605.3 ms |
| **VVLA (Local)** | **BF16** | 85.73 | 92.18 | **92.27** | **347.1 ms** |
| **VVLA (Binary HTTP)** | **Prefix FP8** | 94.31 | 97.60 | **107.73** | **296.1 ms** |
| **VVLA (Local)** | **Prefix FP8** | **101.96** | **111.47** | **111.73** | **286.6 ms** |

At 32 independent clients, VVLA delivers **2.11×** the throughput of FlashRT FP8 (**2.26×** in BF16), **2.21×** EmbodiInfer HTTP, and **5.06×** compiled LeRobot. Loopback binary HTTP retains **96.4%** of in-process throughput (**107.73 chunks/s**).

### Real-Time Multi-Arm Control at 20 Hz

How many physical-pace 20 Hz robot arms one RTX PRO 6000 can sustain under a 100 ms control deadline, and how many tasks the fleet completes per minute in closed loop:

| Policy | Closed-Loop Workload | Qualified Arms | Fleet Productivity (Baseline → VVLA) | Gain |
|---|---|---:|---|---:|
| **π0.5** | LIBERO Soup-Can (8 arms) | 7 → **8** | 34.0 → **47.0 tasks/min** (vs. FlashRT FP8) | **+38.2%** |
| **π0.5** | LIBERO Soup-Can (9 arms) | 7 → **8** | 20.7 → **53.0 tasks/min** (vs. FlashRT FP8) | **2.56×** |
| **OpenVLA-OFT** | LIBERO Bowl (2 → 3 arms) | 2 → **3** | 22.0 → **33.0 tasks/min** (vs. Official Compiled) | **+50.0%** |

### Cross-GPU Throughput Across Three VLA Models

Concurrent throughput across four NVIDIA GPUs with 8 independent clients sharing one GPU:

#### π0.5

| Hardware | Mode | 8-Client Throughput | vs. FlashRT | vs. EmbodiInfer HTTP |
|---|---|---:|---:|---:|
| RTX PRO 6000 (96 GB) | Prefix FP8 | **101.96 chunks/s** | **1.93×** (FP8) | **2.31×** |
| RTX PRO 6000 (96 GB) | BF16 | **85.73 chunks/s** | **2.10×** (BF16) | **1.94×** |
| A100 (80 GB) | BF16 | **44.33 chunks/s** | **1.55×** (BF16) | **2.16×** |
| RTX 4090 (24 GB) | BF16 | **33.40 chunks/s** | **1.36×** (BF16) | **1.27×** |
| RTX 3090 (24 GB) | BF16 | **18.20 chunks/s** | **1.24×** (BF16) | **1.25×** |

Across all four GPUs, VVLA BF16 also leads FlashRT BF16 in fixed-batch throughput by **6.1–12.6%**, cuts peak VRAM by **35–48%** (down to **8.6–9.3 GiB**), lowers single-request latency by **35–44%** vs. compiled LeRobot (**22.55 ms** Prefix FP8 on PRO 6000), and achieves **100/100** paired LIBERO closed-loop success.

#### OpenVLA-OFT

| Hardware | Mode | Official Compiled | VVLA | Speedup |
|---|---|---:|---:|---:|
| RTX PRO 6000 (96 GB) | Mixed FP8 | 21.44 chunks/s | **42.13 chunks/s** | **1.97×** |
| A100 (80 GB) | BF16 | 12.08 chunks/s | **21.47 chunks/s** | **1.78×** |
| RTX 4090 (24 GB) | Mixed FP8 | 10.22 chunks/s | **17.27 chunks/s** | **1.69×** |
| RTX 3090 (24 GB) | BF16 | 5.52 chunks/s | **6.47 chunks/s** | **1.17×** |

Pure BF16 also beats Official Compiled on every GPU (**1.68×** on PRO 6000, **1.50×** on RTX 4090) and cuts single-request latency by **27–33%** on PRO 6000, A100, and RTX 4090 (**32.48 ms** Mixed FP8 on PRO 6000). Paired LIBERO closed-loop success is **198/200** in BF16 and **196/200** in Mixed FP8 (matching official eager **196/200**).

#### LingBot-VLA2

| Hardware | Mode | Official Baseline | VVLA | Speedup |
|---|---|---:|---:|---:|
| RTX PRO 6000 (96 GB) | Split-Stage | 4.29 chunks/s (Compiled) | **25.47 chunks/s** | **5.94×** |
| A100 (80 GB) | Split-Stage | 0.75 chunks/s (Eager) | **13.87 chunks/s** | **18.5×** |
| RTX 4090 (24 GB) | Mixed | OOM | **8.23 chunks/s** | **Unlocks 24 GB** |
| RTX 3090 (24 GB) | Mixed | OOM | **6.22 chunks/s** | **Unlocks 24 GB** |

Under mixed prompt lengths, Split-Stage runs with **0 steady-state graph rebuilds** and **14.6 GiB** VRAM (vs. 24.4 GiB official FP32, which OOMs on 24 GB cards), lowers single-request latency **2.46×** on PRO 6000 (**92.62 ms**) and **3.62×** on A100 (**140.79 ms**), and matches official FP32 eager at **37/40** on 40 held-out RoboTwin initial states.

## Quick Start

Requires Linux x86_64, Python 3.12, PyTorch 2.13.0 (CUDA 13.0), and a CUDA 13.0-capable NVIDIA driver. Full setup for OpenVLA-OFT, LingBot FlashAttention-2.8.3 wheels, Hub assets, and Docker lives in [docs/INSTALL.md](docs/INSTALL.md).

### Install

```bash
python3.12 -m venv .venv && source .venv/bin/activate
pip install build && python tools/build_release.py
pip install 'dist/vvla-0.1.0b2-py3-none-any.whl[serve,hub]'

python tools/install_backend.py pi05   # or: oft | lingbot
vvla doctor --model pi05
```

### Direct Python SDK

```python
import vvla

with vvla.load("pi05", checkpoint="/models/pi05") as engine:
    action = engine.infer_batch([observation], [17])[0]

with vvla.load("oft", checkpoint="/models/oft", mode="fixed", max_batch=4) as engine:
    actions = engine.infer_batch(observations, seeds)
```

### Multi-Client Server & Client

```bash
# Default binary HTTP / WebSocket server
vvla serve --model pi05 --checkpoint /models/pi05 --host 127.0.0.1 --port 8000

# OpenVLA-OFT Mixed FP8 (PRO 6000 / RTX 4090)
vvla serve --model oft --checkpoint /models/oft --recipe mixed-fp8 --max-batch 4

# LingBot-VLA2 Split-Stage multi-task serving (0 graph rebuilds)
vvla serve --model lingbot --checkpoint /models/lingbot --recipe split-stage --max-batch 4

# Deadline-aware real-time serving with cohort Slack-EDF (PRO 6000)
vvla serve --model pi05 --checkpoint /models/pi05 --recipe prefix-fp8 \
    --max-batch 16 --wait-ms 2 --policy cohort-slack-edf --service-profile pi05-g4-prefix-fp8
```

```python
from vvla import VvlaClient

async with VvlaClient("http://127.0.0.1:8000", transport="ws") as client:
    reply = await client.infer(observation, seed=17, request_id="arm-1-step-8", timeout_s=5)
    action, receipt = reply["result"], reply["scheduler"]
```

## Supported Models and Hardware

Each worker probes GPU compute capability, free VRAM, and installed kernels at startup; validated default routes and opt-in high-throughput recipes (`--recipe mixed-fp8`, `--recipe split-stage`) are listed below:

| Hardware | π0.5 | OpenVLA-OFT | LingBot-VLA2 |
|---|---|---|---|
| RTX PRO 6000 (96 GB, SM120) | Prefix FP8, up to B16 | BF16 / Mixed FP8, B4 | Mixed / Split-Stage, B4 |
| A100-SXM4 (80 GB, SM80) | BF16, B4 | BF16, B4 | Mixed / Split-Stage, B4 |
| RTX 4090 (24 GB, SM89) | BF16, B4 | BF16 / Mixed FP8, B4 | Mixed, B1 |
| RTX 3090 (24 GB, SM86) | BF16, B4 | BF16, B4 | Mixed, B1 |

## Documentation

| Guide | Contents |
|---|---|
| [Installation](docs/INSTALL.md) | Isolated worker setup, OFT/LingBot sources, FlashAttention-2.8.3 wheels, Hub offline caching, Docker |
| [Inference & Service API](docs/API.md) | Observation/action schemas, binary HTTP/WS protocol, FIFO/EDF/Slack-EDF schedulers, `vLLM-Omni` plugin |
| [Support Matrix](docs/SUPPORT_MATRIX.md) | Four-GPU validation scope, full-checkpoint checks, explicit precision and serving recipes |
| [Testing & Benchmarks](docs/TESTING.md) | CPU contract suite, wheel/IPC validation, and `vvla bench` CLI commands |
| [Architecture](docs/ARCHITECTURE.md) | Worker isolation, segmented binary IPC, ownership contracts, and graph metrics |
| [OpenPI Contract](docs/OPENPI_CONTRACT.md) | Input/action and tokenizer contract differences for OpenPI H10 checkpoints |

## Citation

[Technical report (PDF)](report/VVLA_Technical_Report.pdf)

```bibtex
@misc{zhuang2026vvla,
  title  = {VVLA: Single-GPU Inference and Dynamic Batching for Vision-Language-Action Models},
  author = {Shuyang Zhuang},
  year   = {2026},
  url    = {https://github.com/X1Agu/VVLA},
  note   = {Zhejiang University}
}
```

## License

Released under the [Apache-2.0 License](LICENSE). See [NOTICE](NOTICE) and [docs/SOURCE_LINEAGE.json](docs/SOURCE_LINEAGE.json) for third-party notices and upstream attributions. VVLA builds upon and evaluates alongside [LeRobot](https://github.com/huggingface/lerobot), [OpenPI](https://github.com/Physical-Intelligence/openpi), [OpenVLA-OFT](https://github.com/moojink/openvla-oft), [LingBot-VLA2](https://github.com/Robbyant/lingbot-vla-v2), [vLLM / vLLM-Omni](https://github.com/vllm-project/vllm-omni), [FlashAttention](https://github.com/Dao-AILab/flash-attention), [FlashRT](https://github.com/flashrt-project/FlashRT), and [EmbodiInfer](https://github.com/BUAA-CI-LAB/EmbodiInfer).
