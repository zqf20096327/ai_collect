# AI Engine on Small Unified Memory

A streaming inference engine that runs **Qwen3.8-Flash-Next**, a 125B-parameter mixture-of-experts model, on a
**PlayStation 5 running Linux**: 16 GB of unified memory, the console's own GPU through Vulkan compute, and the
model's 24,576 experts streamed from the M.2 SSD into a slot pool the GPU reads in place.

Written from scratch in C++20 and GLSL for this one machine. No llama.cpp, no ROCm (the PS5 GPU, GFX1013, has no
ROCm target).

## Results

Measured on the console (PS5 "Phat", firmware 13.00, WD SN810 512 GB in the M.2 bay), November 2026.

| | |
|---|---|
| decode, served configuration | **49-57 tok/s** (56.2 tok/s on the reference prompt) with cache-aware routing; 45.5 tok/s with exact routing |
| prefill | 320-340 tok/s (each expert is read once per 8,192-token chunk) |
| context | 262,144 tokens; KV cache at 7,696 B per position (4-bit Hadamard-rotated K and V), grown on demand |
| long context | 13.1 tok/s decode at 194k tokens of context |
| conversations on the SSD | a 120,000-token conversation is restored in about 1 s after a restart (418 s to prefill it again) |
| quality | EXL3 3.18 bpw experts: top-1 agreement 0.932 and KL 0.149 nats against an unmodified ~4.5-bit reference (0.935 / 0.135 with exact routing) |
| API | OpenAI- and Anthropic-compatible HTTP API on `:8081` (streaming, tool calls, thinking); dashboard and chat on `:8080` |

How it gets there, in short (details in [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)):

- **Small experts at Q4-class quality.** EXL3 trellis-coded experts (2.68-3.18 bits per weight) are copied
  byte-for-byte into 4 KiB-aligned slots and decoded on the GPU, so each miss reads fewer bytes and more experts fit.
- **Zero-copy streaming.** `io_uring` `READ_FIXED` with `O_DIRECT` lands experts in 2 MiB hugetlb pages that are
  also imported into Vulkan as a dma-buf. About 12 GiB of the 16 GB is expert pool.
- **One command buffer per token.** The GPU waits on per-layer flags in bounded gate kernels while the host binds
  slots; resident experts compute while the missing ones stream.
- **Prediction and speculation.** A trained cross-layer router predictor starts reads one layer early; the model's
  MTP head drafts tokens that are verified in one batched pass; cache-aware routing prefers resident experts when
  the router is uncertain.
- **Layer-major prefill.** Prompts are processed in chunks so each expert is read once per chunk, not once per token.

## Requirements

This project does not include or explain a PS5 jailbreak. You need a console that already boots Linux.

| | |
|---|---|
| console | PS5 "Phat" on firmware 13.00, booting Linux through [ps5-linux](https://github.com/ps5-linux) (`ps5-linux-loader` + the `linux-ps5` kernel, 7.2.x); Arch/CachyOS userland |
| storage | a Gen4 NVMe SSD in the M.2 bay with about 400 GB free for the model files (the SN810 reads 6.4 GB/s) |
| kernel | hugetlbfs, udmabuf, io_uring, amdgpu; check with `bash scripts/console/kconfig-check.sh` |
| console packages | `base-devel cmake ninja shaderc vulkan-headers vulkan-radeon liburing python python-numpy python-tokenizers python-jinja python-huggingface-hub (provides `hf`)` |
| network | a wired LAN is recommended for downloading and copying model files |
| a PC (optional) | Git Bash or Linux, for editing and the sync/build script |

Rules learned the hard way:

- Never connect the console to PSN and never update the firmware: either loses the Linux path.
- Soft reboot only (`systemctl reboot`, which uses kexec). A cold boot returns to the loader's default.
- Never write to USB drives attached to the console unless you know what they are: PS5-formatted storage looks like
  a raw disk, and device names (`sda`, `sdb`) swap between boots. Use `/dev/disk/by-id`.
- Do not pin memory past the pool reserve: pinning to the edge hung the console once.

## Setup

All steps run on the console as the `steam` user unless noted. The layout below is what the systemd units expect:
sources in `~/ps5lm/src`, the build in `~/ps5lm/build14`, model files in `~/ps5lm/model`.

### 1. Kernel parameters and boot modes

```bash
git clone <this repository> ~/ps5lm/src && cd ~/ps5lm/src
bash scripts/console/kconfig-check.sh                 # every line should say ok
sudo bash ps5/appliance/ps5lm-min.sh install          # installs ps5lm-min and the (inert) AI-mode units
sudo ps5lm-min cmdline                                # adds kho=off udmabuf.size_limit_mb=16384 swiotlb=4096 ...
```

`ps5lm-min boot ai` makes the next soft reboot come up as an inference appliance (no gamescope/Steam session,
server started at boot); `ps5lm-min boot game` restores the normal console. See
[`ps5/appliance/README.md`](ps5/appliance/README.md) for every parameter and why it is there.

### 2. Build

```bash
cmake -S runtime -B ~/ps5lm/build14 -G Ninja -DCMAKE_BUILD_TYPE=Release -DPS5LM_BUILD_BENCH=OFF
cmake --build ~/ps5lm/build14 --target flash_decode ps5lm_shaders pack_convert
```

Presets for other layouts are in [`runtime/CMakePresets.json`](runtime/CMakePresets.json) (`ps5`, `ps5-serve`, and
`host` for the portable tests). Never build while the engine is running: the compiler and the pool compete for the
same memory.

### 3. Model files

```bash
M=~/ps5lm/model; mkdir -p $M; cd ~/ps5lm/src/runtime/tools

# tokenizer, chat template and config from the original model
hf download Qwen/Qwen3.8-Flash-Next tokenizer.json tokenizer_config.json chat_template.jinja config.json --local-dir $M

# dense weights (attention, GDN, routers, lm_head, MTP head) and the 102 GB n-gram table, streamed shard by shard
# (resumable; each shard is deleted once converted). Also writes scalar Q4/Q2 expert packs (~110 GB) that only
# --bits 4/2 use: delete experts_q4.pack and experts_q2.pack afterwards if you serve EXL3.
python3 convert_hf.py --out $M --bin ~/ps5lm/build14/pack_convert

# EXL3 experts: the 3.18 bpw branch, repacked byte-for-byte, plus the MTP head's experts as layer 48
hf download turboderp/Qwen3.8-Flash-Next-exl3 --revision 3.18bpw_h6_ng8 --local-dir ~/ps5lm/dl
python3 s15/pack_exl3.py ~/ps5lm/dl $M --delete-shards
python3 s15/pack_exl3_mtp.py $M

# the 2.68 bpw pack (smaller, about 20% faster, used by the smoke test), fetched by HTTP range requests straight
# into the pack format; its MTP layer comes from the 3.18 files written above
python3 s17/fetch_pack_exl3.py 2.68bpw_h6_ng8 $M experts_exl3_268
python3 s15/pack_exl3_mtp.py $M experts_exl3_268 --nonexpert $M/exl3_nonexpert.safetensors
```

The router predictor is optional. Without `$M/pred_s17/` the engine runs without early prefetch; it is fitted
from routing dumps with `runtime/tools/s17/pred_data.sh` and `runtime/tools/s17/fit_pred.py`.

### 4. Check the build

```bash
bash ~/ps5lm/src/scripts/console/smoke.sh
```

One cold 300-token greedy run of a fixed prompt on the 2.68 pack. `PASS` means the generated tokens are identical to
the reference (md5 `18179c0e1f51`). Every change to the engine must keep this at PASS unless it is deliberately
lossy and scored with the quality tools (`scripts/console/score.sh`).

### 5. Serve

```bash
sudo mkdir -p /etc/ps5lm
sudo cp ~/ps5lm/src/ps5/appliance/etc-ps5lm/server.env /etc/ps5lm/server.env   # served flags, each one explained
sudo ps5lm-min boot ai && sudo systemctl reboot
```

After the reboot `ps5lm-server` (API, `:8081`) and `ps5lm-dash` (dashboard and chat, `:8080`) start on their own;
`sudo ps5lm-min status` shows the memory budget and server state.

```bash
curl http://<console-ip>:8081/v1/chat/completions -H 'Content-Type: application/json' \
  -d '{"model":"qwen3.8-flash-next-ps5","messages":[{"role":"user","content":"Hello"}],"stream":true}'
```

Any OpenAI- or Anthropic-compatible client works with `http://<console-ip>:8081`. The API key is not checked, so
keep the console on a trusted network.

### Working from a PC

```bash
cp scripts/console.env.example scripts/console.env    # console address and SSH key path (git-ignored)
scripts/ps5-sync-build.sh --stop-server               # copies the tree to the console and builds there
```

### Tests without a console

```bash
cd runtime && cmake --preset host && cmake --build --preset host && ctest --preset host   # slot cache, quantizer, trace replay
python -m unittest discover -s engine/tests                                             # bandwidth model and gate
```

CI runs these, compiles every shader variant, and compiles the engine with the console's flags.

## Repository layout

| path | contents |
|---|---|
| [`runtime/`](runtime/) | the engine: `include/ps5lm/flash_engine.hpp` (engine), `src/flash_decode.cpp` (CLI and `--serve`), `shaders/` (GLSL compute), `tools/` (HTTP server, dashboard, pack and quality tools) |
| [`ps5/appliance/`](ps5/appliance/) | boot modes, systemd units, served configuration |
| [`scripts/`](scripts/) | PC-side sync/build; `scripts/console/`: smoke test, preflight, benchmarks, hardware probes, the low-memory kernel module |
| [`docs/`](docs/) | design and measurements (start with `ARCHITECTURE.md`) |
| [`engine/`](engine/), [`tools/`](tools/) | the Python bandwidth and hit-rate model and the probe battery that came before the engine |
| [`research/`](research/) | literature studies and design history written before and during the build |
| [`recon/`](recon/) | raw hardware dumps and probe results from the console |

## Documentation

| | |
|---|---|
| how it works and where things are | [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) |
| the engine specification, every number tagged measured / derived / assumed | [`docs/ENGINE-SPEC.md`](docs/ENGINE-SPEC.md) |
| what still limits speed and how it could be fixed | [`docs/OPEN-ITEMS-100B.md`](docs/OPEN-ITEMS-100B.md) |
| cache-aware routing: getting past the SSD's bandwidth | [`docs/CACHE-AWARE-ROUTING.md`](docs/CACHE-AWARE-ROUTING.md) |
| conversations kept on the SSD | [`docs/PERSISTENT-CONTEXT.md`](docs/PERSISTENT-CONTEXT.md) |
| KV cache size, from 19 KB to 7.7 KB per position | [`docs/KV-FOOTPRINT-RESEARCH.md`](docs/KV-FOOTPRINT-RESEARCH.md) |
| long context (194k tokens) | [`docs/S33-LONG-CONTEXT.md`](docs/S33-LONG-CONTEXT.md) |
| every device on the console and what it can add | [`docs/HARDWARE-DECONSTRUCTION.md`](docs/HARDWARE-DECONSTRUCTION.md) |
| the firmware-reserved gigabyte of RAM | [`S26`](docs/S26-GPU-RESERVED-RAM.md), [`S28`](docs/S28-MCE-REGISTER-PROBE.md), [`S29`](docs/S29-IOMMU-AND-APERTURE-PROBE.md), [`S31`](docs/S31-LOWMEM-TIER.md) |
| scaling to 500B-1T models | [`docs/SCALING-500B-1T.md`](docs/SCALING-500B-1T.md) |

Document and tool names carry the development session that produced them (`S15` ... `S35`). Numbers in the
documents cite entries of the project's development ledger as `R1`-`R85`; the ledger itself is not published.

## History

The project started in October 2026 as a course project asking whether a 125B model could run usefully on a 16 GB
console at all. The first answer, from the Python model in `engine/` and the probe battery in `tools/ps5probe/`, was
"6-10 tokens per second". That estimate assumed 4.5-bit scalar experts, a QLC drive and a 2-3 GiB cache; the custom
engine, the EXL3 packs, the SN810 and a 12 GiB pool changed each of those. This repository ends at session S35
(2026-11-13), when the work on Qwen3.8-Flash-Next was finished.

## License and credits

Code is under the [MIT License](LICENSE), except the Linux kernel modules in `scripts/console/s28/` and
`scripts/console/s31/` (GPL-2.0) and the third-party files listed in [`NOTICE`](NOTICE).

Built on the work of others: [Qwen](https://huggingface.co/Qwen) (the model),
[exllamav3](https://github.com/turboderp-org/exllamav3) (the EXL3 format and the quantized packs this engine reads),
[ps5-linux](https://github.com/ps5-linux) (Linux on the PS5), Mesa RADV, and
[Strata](https://github.com/niko1221/strata) (dashboard design).

Not affiliated with or endorsed by Sony Interactive Entertainment, Alibaba/Qwen or any model publisher.
"PlayStation" and "PS5" are trademarks of Sony Interactive Entertainment. Running Linux on a PS5 may void its
warranty and can leave the console unusable; you do so at your own risk.
