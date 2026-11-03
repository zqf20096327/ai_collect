![GreenBoost Windows](assets/header.png)

# GreenBoost for Windows

**Keep selected model experts in VRAM and load the rest from RAM or a GGUF file when CUDA needs them.**

GreenBoost's experimental MoE backend gives expert weights stable GPU addresses
while reusing a bounded pool of physical VRAM. The model's own router chooses
which experts run. GreenBoost loads their original bytes before the existing
llama.cpp CUDA kernels use them. Model calculations stay on the GPU.

**Native Windows throughout:** the launcher and library are Windows C/C++
binaries built with MSVC. File reads use Win32 APIs, and NVIDIA's Windows CUDA
driver runs the GPU kernels. Building and running the Windows product requires
no WSL, Linux installation or Linux service. Host integration runs in user
mode; the separately retained KMDF driver is legacy and optional.

**The latest offloading changes are source only and have not been run or
benchmarked.** They add CUDA hot-expert tracking, upcoming file reads and
optional greedy speculative decoding. No throughput improvement is claimed.
The [older beta 3 ZIP](https://github.com/denoflore/greenboost-windows/releases/download/v2.4.0-beta.3/GreenBoost-Windows-2.4.0-beta.3-x64.zip)
does not contain this backend.

## Pick the path you need

| Your situation | Use | What it does |
| --- | --- | --- |
| A supported quantised MoE model needs more expert storage than you want to keep in VRAM | **Experimental MoE backend**, below | Loads selected expert weights through a pinned RAM cache into a fixed VRAM pool. |
| Your model fits normally, or you want to launch another CUDA application | **Portable allocation shim** | Uses ordinary CUDA allocations first, with an optional managed-memory fallback and reported capacity allowance. |

You choose the path before launch. The portable shim does not automatically
turn an existing llama.cpp, Ollama or LM Studio installation into the MoE backend.
Dense weights, KV cache and temporary CUDA buffers still need memory outside
the expert pool. A configured allowance is not reserved RAM or extra physical VRAM.

## Build and run MoE offloading

You need Windows x64, an NVIDIA GPU and driver, Visual Studio C++ Build Tools,
CMake, Ninja, a CUDA Toolkit, and your own supported quantised MoE GGUF.
Use a single GGUF file. The build uses pinned official **llama.cpp b12019**.

From this repository's root, build for an RTX 3090 or 3090 Ti:

```powershell
.\windows-port\tools\build_moe.ps1 `
    -CudaRoot 'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.3' `
    -Architectures 86
```

Use architecture `75` for RTX 2000, `86` for RTX 3000, `89` for RTX 4000,
or `120` for RTX 5000, with a Toolkit that supports that architecture.
RTX 2000 hardware execution remains unverified. Building requires the Toolkit;
running the resulting directory uses the copied CUDA runtime libraries.

For a machine with **24 GiB VRAM and 128 GiB RAM**, this is an illustrative
starting configuration. It gives experts 12 GiB of VRAM and a 64 GiB pinned RAM
cache. The remaining memory must cover everything else the model and Windows need.

```powershell
.\windows-port\tools\run_moe.ps1 `
    -LlamaDirectory '.\windows-port\tools\backends\greenboost-moe-b12019\build\bin' `
    -Model 'D:\models\your-moe.gguf' -Gpu 0 `
    -ExpertVramMiB 12288 -ExpertRamMiB 65536 `
    -HotExperts 8 -PrefetchMiB 16 `
    -Context 4096 -MicroBatch 8 -Tokens 128 `
    -Prompt 'Explain how a heat pump works.'
```

This does not promise that a particular model fits or runs quickly. Use the
CUDA GPU number from `llama-completion.exe --list-devices`; NVIDIA tools can
number the same cards differently. The launcher exposes that card as CUDA0,
runs one completion and restores its environment settings afterward.

**Sizing rule:** leave room for dense weights, KV cache, temporary buffers,
Windows and other applications. Increase the expert VRAM pool when those have
room; a tiny pool can force repeated transfers. The
[full offloading guide](windows-port/integrations/llama/README.md) explains
budgets, every switch, draft models, MTP, errors and disabling individual features.

## What the new loading controls do

- **Hot experts:** CUDA tracks recent use and selects experts whose pages should
  be retained when possible. Required pages always take precedence.
- **Prefetch:** Windows starts bounded file reads for later projections and
  likely experts in the following layer while CUDA executes current work.
  These reads fill RAM; GPU residency still follows the actual router.
- **Speculative decoding:** a compatible draft model or MTP head proposes several
  tokens. The target model verifies them together using greedy CUDA sampling.
  Accepted proposals can share one target pass and its expert loads.

Speculation is optional. Add a compatible ordinary draft GGUF to the command:

```powershell
    -DraftModel 'D:\models\compatible-small-draft.gguf' -DraftTokens 4
```

Use `-Speculation Mtp` only with a model and optional sidecar supported by the
pinned backend. These modes have not been exercised in this revision. Unsupported
CUDA computation or sampling fails explicitly. Routing biases, expert pruning,
CPU expert execution, Xolotl-specific weight formats and a Linux GPU unlock are
not part of this implementation.

## Use the portable allocation shim

The separate portable launcher remains available for ordinary CUDA applications.
Build current source using the [portable build instructions](windows-port/BUILDING.md),
or use the older beta 3 ZIP with its earlier allocation policy. Keep
`greenboost.exe` and `greenboost_cuda.dll` together.

```powershell
.\greenboost.exe 'C:\application\app.exe' arguments
```

For the included ordinary llama.cpp workflow, from the extracted portable package:

```powershell
.\install_llama.ps1 -Cuda 13.4
.\run_llama.ps1 -ListDevices
.\run_llama.ps1 -Model 'D:\models\model.gguf' -Gpu 0
```

Use the documented CUDA 12.4 backend option for RTX 2000 or suitable older
runtime combinations. The current source tries ordinary device allocations
first and managed memory after an eligible out-of-memory result. Windows and
the NVIDIA driver determine whether and where that allocation succeeds.
`-ExtraMiB 0` disables the reported extra-capacity allowance.
See [portable settings](windows-port/README.md) and [CUDA compatibility](windows-port/RTX_KERNELS.md).

## What the evidence establishes

The [November 1 receipts](windows-port/STREAMING_RESULTS_20261101.json) cover the
**earlier demand-paging implementation**. Granite 3.1 1B A400M Q4_K_M produced
matching resident and paged text for two short prompts on an RTX 3060. That
exercise deliberately used a **32 MiB expert pool**. Its final paged run was
about 5.92 tokens/s; the corresponding resident run was about 125.11 tokens/s.
The model already fit in VRAM. This was a bounded-residency check, not a tuned
large-model throughput result.

Those measurements do not validate the new cache, prefetch or speculation code.
The new revision has no inference or performance receipt. The
[earlier allocation report](windows-port/EXPERIMENTAL.md) separately records
CUDA allocation and storage checks across five RTX cards. Larger-than-VRAM
model throughput, long sessions and the configurations in the shared Xolotl
post remain unverified here.

## What "one memory" means

Expert data retains its logical address as physical VRAM is reused. RAM and
files provide backing storage. Their transfer speeds still matter. The
inference backend explicitly arranges residency before CUDA reads a weight;
there is no transparent GPU fault handler or direct SSD-to-GPU transfer.

## Documentation and credits

- [November 2 issue revisions, build evidence and pending checks](windows-port/ISSUE_REVISIONS.md)
- [Complete MoE configuration and offloading guide](windows-port/integrations/llama/README.md)
- [Portable launcher](windows-port/README.md) and [building it](windows-port/BUILDING.md)
- [Implementation notes and evidence boundaries](docs/greenboost-revisions/STREAMING.md)
- [Troubleshooting](windows-port/TROUBLESHOOTING.md)

Original GreenBoost by [Ferran Duarri](https://gitlab.com/IsolatedOctopi/greenboost).
Windows port and maintenance by [Chris Zuger / denoflore](https://github.com/denoflore).
[GPL v2](LICENSE). The inference kernels and speculative decoder come from
[llama.cpp](https://github.com/ggml-org/llama.cpp/tree/b12019) under its MIT licence.
Microsoft Detours is MIT licensed. Linux sources remain as upstream reference.
