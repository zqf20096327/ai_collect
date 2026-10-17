# LM Studio on two PCs — split a model over LAN with LM Studio's own engine

> **In one sentence:** run a model that is too big for one GPU in **LM Studio across two computers** (distributed inference over LAN, multi-PC / multi-GPU) using llama.cpp's **RPC backend** — no LM Studio source changes, just two DLLs and one environment variable (`GGML_RPC_SERVERS`). Tested on Windows + Vulkan with AMD cards (RX 9070 XT + RX 6800 over 2.5 GbE); the same approach should work with NVIDIA / CUDA runtimes if you rebuild the registry DLL for them. If you searched for *"LM Studio multiple PCs"*, *"LM Studio RPC"*, *"LM Studio distributed inference"*, *"LM Studio two GPUs on different computers"* or *"llama.cpp rpc-server with LM Studio"* — this is that.

**Who made this.** The idea is Robert's ("can't we trick LM Studio into offloading to the second GPU instead of the CPU?").
The code, the builds and this README were written by **Kod, an AI (Claude Opus 5 running in Claude Code)**, working with Robert
on his two-PC setup on 15 Sep 2026. We say this up front because it matters: this is a working hack from a home lab, not a
reviewed upstream feature. Use at your own risk; read the caveats.

**Status:** works, measured, not submitted upstream (see `UPSTREAM.md` for why and how you could).

**What this is.** Two small files that let LM Studio's bundled `llama-server.exe` see a GPU in
*another computer* through llama.cpp's RPC backend, so a model that does not fit your card can be
split across two machines — without touching a line of LM Studio.

**What it is not.** Not a speed trick. Splitting a model that *fits* on one card makes it slower
(a 9B went from 90 to 57 t/s). It pays when the model *does not fit*: a 35B MoE went from 31 t/s
(experts in RAM) to 57–82 t/s split over two cards.

## How LM Studio's engine is built (why a plug-in alone doesn't work)

LM Studio ships upstream llama.cpp (2.37.0 = commit `8172e65`). Its registry
(`ggml_llamacpp.dll`, a renamed `ggml.dll`) is built **without** `GGML_BACKEND_DL`: the CPU and
Vulkan backends are linked in and registered statically, and its argument parser has no `--rpc`.
Dropping a `ggml-rpc.dll` next to it does nothing at serve time — the registry never looks for
plug-ins. `--list-devices` *does* (it goes through `common`), which is why that test lies.

## The two files

1. **`ggml-rpc.dll`** — llama.cpp's RPC backend at the same commit, with one addition: at
   registration it reads `GGML_RPC_SERVERS=host:port[,host:port...]`, adds those servers and
   exposes their devices. (Patch `0001`, 45 lines. See `UPSTREAM.md`.)
2. **`ggml_llamacpp.dll`** — the registry rebuilt the way LM Studio builds it (static CPU + Vulkan)
   **plus** static RPC, linked against import libraries generated from LM Studio's *own*
   `ggml-cpu.dll` / `ggml-vulkan.dll` (`.def` files included). This is the only piece that is
   LM-Studio-specific and must be rebuilt per LM Studio runtime version.

## Install (Windows host, Vulkan runtime 2.37.0)

1. On the second PC: run `ggml-rpc-server -H 0.0.0.0 -p 50052 -d <device>` from a llama.cpp build
   with the **same RPC protocol version** (b10951 works with 8172e65; check `git log` of
   `ggml/src/ggml-rpc/ggml-rpc.cpp` between the two commits — no changes = compatible).
2. On the LM Studio PC: back up and replace in
   `%USERPROFILE%\.lmstudio\extensions\backends\llama.cpp-win-x86_64-vulkan-avx2-2.37.0\`:
   `ggml_llamacpp.dll` (ours), and add `ggml-rpc.dll` (ours).
3. Set the user environment variable `GGML_RPC_SERVERS=<ip>:50052`
   (optionally `LLAMA_ARG_TENSOR_SPLIT=0.58,0.42` — first number = the RPC device).
4. Start LM Studio, select the **Vulkan** runtime, load a model. The remote card fills.

Safety: without the variable everything is stock. With the variable and no worker reachable,
the plug-in logs "could not add RPC server" and LM Studio runs single-GPU. An LM Studio runtime
update overwrites both files → automatic fallback to stock.

## Build recipe (what we did)

- Worktree at `8172e65`, ROCm clang 23 + lld-link + llvm-dlltool, Windows Kits `rc.exe`.
- `ggml-rpc.dll`: cmake `-DBUILD_SHARED_LIBS=ON -DGGML_BACKEND_DL=ON -DGGML_RPC=ON`
  (Vulkan/HIP off), target `ggml-rpc`.
- `ggml_llamacpp.dll`: compile `ggml-backend-reg.cpp` + `ggml-backend-dl.cpp` with
  `-DGGML_USE_CPU -DGGML_USE_VULKAN -DGGML_USE_RPC -DGGML_BUILD -DGGML_SHARED`, link against
  `ggml-base.lib`, `vk.lib`, `cpu.lib` (from LM Studio's DLLs via `llvm-dlltool -d *.def`) and
  our `rpc.lib`. See `build-lms/` in the worktree.

## Measured (same flags, same prompts)

| model | LM Studio + this | plain llama.cpp b10951 |
|---|---|---|
| Qwen3.5-9B Q4_K_M, solo on RX 9070 XT | 89–91 t/s, prefill 2352 | 91 t/s, prefill 2685 |
| Ornith-1.5-35B-A3B Q4_K_M, split 0.58/0.42, MTP | 59–62 | 56–57 |
| Qwen3.6-35B-A3B Q4_K_XL, split 0.55/0.45, MTP | 75–80 | 81–83 |
| Qwen3.8-27B Q4_K_M dense, split 0.58/0.42, MTP | 32 | 32 |

Hardware: i7-9700K / 32 GB / RX 9070 XT (Windows, Vulkan) ↔ i7-2600K / RX 6800 (Ubuntu, Vulkan),
2.5 GbE direct cable. LM Studio has no secret kernels — it is upstream llama.cpp with a nice face.

## Caveats

- Both sides must share the RPC protocol version; a mismatch connects silently and computes on
  the CPU (we learned that the hard way — check the worker's VRAM after load).
- The worker serves one client at a time (upstream PR #28916 changes that).
- Rebuild `ggml_llamacpp.dll` for each LM Studio runtime version; `ggml-rpc.dll` only needs the
  same protocol version.
- Prior art: none found upstream; LM Studio tracker issue #321 (Jan 2025, open) asks for exactly this.

## License

Patches and build files: MIT, same as llama.cpp (see `LICENSE-llama.cpp`; the DLLs are built from llama.cpp @ 8172e65
plus our two patches). The `.def` files only list exported symbol names of LM Studio's own DLLs; none of LM Studio's
files are redistributed here.
