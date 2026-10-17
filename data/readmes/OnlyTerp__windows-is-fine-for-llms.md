<p align="center">
  <img src="assets/hero.png" alt="Windows is fine for local LLMs — now. Run 20 GB+ models on the GPU that also drives your display: no desktop crashes, no second machine, no dual-boot." width="880">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Windows%2011-0078D4?style=flat-square&logo=windows11&logoColor=white" alt="Windows 11">
  <img src="https://img.shields.io/badge/NVIDIA%20CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white" alt="NVIDIA CUDA">
  <img src="https://img.shields.io/badge/WSL2-4D4D4D?style=flat-square&logo=linux&logoColor=white" alt="WSL2">
  <img src="https://img.shields.io/badge/llama.cpp-ready-7C5CFF?style=flat-square" alt="llama.cpp ready">
  <img src="https://img.shields.io/badge/License-MIT-5EE7FF?style=flat-square" alt="License: MIT">
  <img src="https://img.shields.io/badge/PRs-welcome-9BE15D?style=flat-square" alt="PRs welcome">
</p>

<h1 align="center">Windows Is Actually Fine for Local LLMs (Now)</h1>

> **The short version:** The old advice — *"don't run local LLMs on Windows, use Mac or Linux"* — had real reasons behind it. But the two things that actually made Windows painful (desktop crashes when loading big models on your display GPU, and WSL2 running out of memory on a model that should fit) are **both solvable**, and the fixes are small and reversible. This is the playbook we wish existed when we started.

We run a 32 GB RTX 5090 that **also drives the monitor**, on Windows 11 + WSL2, serving 20+ GB models daily. After the fixes below: no desktop crashes, terminals stay alive, full-speed inference. No dual-boot, no second machine.

This guide tries hard to be **accurate, not just confident** — claims are cited, and where something is community knowledge rather than official documentation, it says so.

---

## Contents

- [Who this is for](#who-this-is-for)
- [The two real problems](#the-two-real-problems)
- [Fix 1: Display-GPU stability (stop the crashes)](#fix-1-display-gpu-stability-stop-the-crashes)
- [Fix 2: Where to run the model (WSL vs native Windows)](#fix-2-where-to-run-the-model-wsl-vs-native-windows)
- [How to actually serve a model](#how-to-actually-serve-a-model)
- [VRAM sizing: how much to leave for the desktop](#vram-sizing-how-much-to-leave-for-the-desktop)
- [Troubleshooting table](#troubleshooting-table)
- [FAQ](#faq)
- [Bonus gotcha: HuggingFace downloads stall in WSL](#bonus-gotcha-huggingface-downloads-stall-in-wsl)
- [TL;DR checklist](#tldr-checklist)
- [Sources](#sources)

---

## Who this is for

- You have an NVIDIA GPU on **Windows 11** (especially RTX 40/50-series).
- That GPU **also drives your display** — you don't have a spare headless card.
- You want to run local LLMs (llama.cpp, Ollama, LM Studio, vLLM, ComfyUI, …) without your desktop crashing or your tooling falling over.
- You've heard "just use Linux" and want to know whether you actually have to. (You don't — but Linux is genuinely great too; this guide isn't anti-anything.)

---

## The two real problems

When people say "Windows is unstable for LLMs," they're almost always hitting one of two specific issues. Neither is fundamental to Windows.

<p align="center">
  <img src="assets/problems-fixes.png" alt="The two real problems and their cheap, reversible fixes: (1) big-model load crashes the desktop because WDDM TDR resets the GPU after 2s — fix by raising TdrDelay to 20; (2) WSL2 OOMs on a model that fits because of Blackwell's ~16 GiB hidden CUDA-context overhead — fix by serving on native Windows." width="880">
</p>

### Problem 1 — Loading a big model crashes your desktop

**Symptom:** You load a large model; the screen goes black for a few seconds (or the machine hard-crashes/reboots). Event Viewer shows `nvlddmkm` **Event ID 153**, or you get a `VIDEO_TDR_FAILURE (0x116)` bugcheck.

**The intuitive (but usually wrong) diagnosis:** "My GPU can't handle a model this big while also running the desktop / it's out of VRAM."

**The actual cause: WDDM TDR — Timeout Detection and Recovery.** Windows watches the GPU, and by default if a single GPU operation occupies the GPU longer than **2 seconds** without yielding, Windows assumes the driver hung and forcibly resets it ([Microsoft Learn — TDR Registry Keys](https://learn.microsoft.com/en-us/windows-hardware/drivers/display/tdr-registry-keys), default `TdrDelay = 2`). Loading and warming a 20 GB model can run large kernels well past that window — so Windows resets the driver mid-load, which looks like a crash. With 32 GB of VRAM and a 20 GB model you have ~10 GB free; this is a *timeout*, not a memory shortage.

**Honest scope:** This is most commonly reported on **WSL2, on Blackwell (RTX 50-series), or under heavy/long context** rather than every Windows machine. On a stable, well-cooled RTX 30/40 running llama.cpp natively with a recent driver, you may never hit it. But when it does happen, this is the cause — and the fix is cheap and harmless, so it's worth doing preemptively on a display GPU. (Real-world report: [ollama/ollama #15024](https://github.com/ollama/ollama/issues/15024) — `nvlddmkm` Event ID 153 from context population on an RTX 3090 via WSL2.)

→ [Fix 1](#fix-1-display-gpu-stability-stop-the-crashes)

### Problem 2 — WSL2 runs out of memory loading a model that should fit

**Symptom:** Inside WSL2, llama.cpp/vLLM fails with `cudaMalloc failed: out of memory` allocating ~17 GB — **even though `nvidia-smi` shows tens of GB of VRAM free.**

**The actual cause:** WSL2 is a VM. CUDA inside that VM is brokered through the Windows host's WDDM/Hyper-V layer, and large allocations end up bounded by the VM's resources, not just raw VRAM. On **Blackwell specifically**, there's a documented **~16 GiB CUDA-context overhead inside WSL2** that doesn't exist on native Linux, and — critically — it's **invisible to `torch.cuda.mem_get_info()`**, so frameworks plan KV-cache sizes against a wrong "free memory" number and OOM at allocation ([microsoft/WSL #40401](https://github.com/microsoft/WSL/issues/40401), tested on drivers 596.36 and 581.80; the same drivers show only 1–2 GiB overhead on native Linux). On Ampere/Ada (RTX 30/40) the overhead is much smaller (a few hundred MB), so this bites Blackwell users hardest.

**The fix:** Don't fight WSL for big-model serving — **serve from native Windows**, which uses the full host RAM and the most direct GPU path. Keep your Linux workflow in WSL and just talk to the Windows server over HTTP.

→ [Fix 2](#fix-2-where-to-run-the-model-wsl-vs-native-windows)

---

## Fix 1: Display-GPU stability (stop the crashes)

Two parts: raise the TDR timeout (registry, needs Admin + reboot) and turn off a couple of overlay/power behaviors that destabilize a busy display GPU. **Everything here is reversible.**

### 1a. Raise the TDR timeout (registry, Admin)

This is the single highest-value change. Run in an **Administrator** PowerShell — it backs up the key first:

```powershell
$key = 'HKLM:\SYSTEM\CurrentControlSet\Control\GraphicsDrivers'

# Back up the whole GraphicsDrivers key so you can fully revert
reg.exe export "HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers" "$env:USERPROFILE\graphicsdrivers-backup.reg" /y

# Raise the GPU watchdog so long model-load/warmup kernels aren't killed.
# Default TdrDelay is 2s. We use 20s — enough for model loads, still recovers
# reasonably fast if the GPU ever *genuinely* hangs.
New-ItemProperty -Path $key -Name 'TdrDelay'      -Value 20 -PropertyType DWord -Force
New-ItemProperty -Path $key -Name 'TdrDdiDelay'   -Value 20 -PropertyType DWord -Force
```

> **What these do** ([Microsoft Learn](https://learn.microsoft.com/en-us/windows-hardware/drivers/display/tdr-registry-keys)): `TdrDelay` (default **2s**) is the timeout threshold — how long the GPU can hold off the scheduler before Windows declares a hang. `TdrDdiDelay` (default **5s**) is how long the OS waits for driver threads before issuing the `VIDEO_TDR_FAILURE (0x116)` bugcheck. Both in `HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`.

> **Pick your value honestly.** The GPU-rendering community typically uses **8–30 seconds** (not 60–120). Higher is safer for long kernels but has a real downside: if the GPU *truly* hangs, your desktop is frozen for the **entire** `TdrDelay` before Windows recovers it. **20s** is a good default for a display GPU that loads big models. Use 30–60s only if you still see timeouts on load; avoid very large values on a daily-driver desktop.

**Reboot** — TDR changes only take effect after a restart.

**Verify** (after reboot; `0x14` = 20):
```powershell
reg query "HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers" /v TdrDelay
```

**Revert everything:** `reg.exe import "$env:USERPROFILE\graphicsdrivers-backup.reg"` then reboot.

### 1b. Two NVIDIA settings (NVIDIA app GUI)

The old "NVIDIA Control Panel" was folded into the **NVIDIA app**. Open it → **Graphics → Global Settings** (a long scrollable list — same options as the old Control Panel):

- **Power management mode → "Prefer maximum performance."**
  Keeps the GPU out of deep idle clock states. A cold GPU ramping from idle on the first model-load kernels can itself contribute to a timeout.
- **CUDA - Sysmem Fallback Policy → "Prefer No Sysmem Fallback."**
  By default, when VRAM gets tight CUDA silently spills into system RAM — which tanks performance and can stutter the compositor. "No fallback" gives you a clean out-of-memory error instead of a creeping hang, which is what you want on a display GPU. (Note: WSL2 ignores this setting entirely — it only affects native-Windows CUDA — see [microsoft/WSL #11050](https://github.com/microsoft/WSL/issues/11050).)

### 1c. (Optional) Disable MPO if you see flicker/black flashes

**Multi-Plane Overlay (MPO)** is widely reported by the community to cause momentary black flashes / flicker on RTX 40/50 desktops under GPU load. If you experience that specifically, disabling MPO is a common fix.

> ⚠️ **Honesty note:** The MPO-disable registry keys are **community/undocumented** — they are *not* in official Microsoft or NVIDIA documentation, and the MPO→flicker link is community-reported, not vendor-confirmed. They're widely used and reversible, but treat them as a community workaround, not an official setting. Only apply this if you actually see flickering.

The common community method (works on current Windows 11 builds):
```powershell
# Community/undocumented. Reversible (delete the value to re-enable MPO).
New-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\GraphicsDrivers' -Name 'DisableOverlays' -Value 1 -PropertyType DWord -Force
```
The older method (`HKLM\SOFTWARE\Microsoft\Windows\Dwm` → `OverlayTestMode = 5`) is widely reported to have stopped working on newer Windows 11 builds. See community tools like `RedDot-3ND7355/MPO-GPU-FIX` for the current approach. Reboot after changing. (`dxdiag` → Display tab will show MPO status.)

### 1d. Driver hygiene (RTX 50-series)

- Use a recent stable/Studio driver. Early Blackwell launch drivers had real stability problems; newer drivers are better. We can't responsibly name a specific "fixed in version X" hotfix — NVIDIA's release notes don't cite one we could verify — so just stay reasonably current and avoid the launch-window driver.
- **PCIe link stability:** Blackwell + some motherboards have had PCIe-link issues that present as instability/black screens. A documented case ([NVIDIA/open-gpu-kernel-modules #1010](https://github.com/NVIDIA/open-gpu-kernel-modules/issues/1010)) was Linux-specific (open kernel module dropping to PCIe Gen1), with the Windows driver behaving correctly. If you get unexplained hard GPU hangs on a PCIe 5.0 board, forcing the GPU slot to **Gen4** in BIOS is a low-risk thing to try.

### Does it work? (our result)

We loaded a **22 GB model on the display-attached RTX 5090** — the exact scenario that used to crash the desktop — and after these fixes: **no crash, no flicker**, model loaded to ~24.5 GB VRAM, inference at 150–200+ tok/s, desktop fully responsive throughout.

---

## Fix 2: Where to run the model (WSL vs native Windows)

This is the decision that trips everyone up.

<p align="center">
  <img src="assets/architecture.png" alt="Recommended setup: keep your workflow in WSL2 (agents, scripts, tooling) and call a native-Windows llama-server.exe over HTTP on port 8080. The server uses full host RAM and the most direct GPU path to the RTX 5090, which serves the model and drives the display at the same time." width="880">
</p>

| | Native Windows | Inside WSL2 |
|---|---|---|
| **RAM available to CUDA** | Full host RAM (e.g. 64 GB) | Bounded by the WSL VM |
| **Load a model near/over the VM's resources?** | Yes | Often **fails** — `cudaMalloc` OOM even with free VRAM |
| **Blackwell (RTX 50xx) overhead** | Normal | **~16 GiB hidden** CUDA-context overhead ([WSL #40401](https://github.com/microsoft/WSL/issues/40401)) |
| **Display stability** | Most direct WDDM path | Extra Hyper-V GPU-paravirt layer = more failure modes |
| **Setup friction** | Download a release `.exe`, run it | Build/install in WSL, handle networking |

**Recommendation: serve big models from native Windows.** Download the Windows CUDA `llama-server.exe` (or use Ollama / LM Studio for Windows), point it at your GGUF, done. Full host RAM, most stable GPU path.

**You keep your WSL workflow.** Your scripts, agents, and tooling can live in WSL and just call the Windows server over HTTP — Linux ergonomics, native-Windows GPU muscle.

> ### ⚠️ Critical warning if a long-running process lives *inside* WSL
> If you run an agent, server, or your main terminal workflow inside WSL, **do not "fix" the memory problem by raising the WSL RAM cap / running `wsl --shutdown`.** Editing `.wslconfig` requires `wsl --shutdown`, which **kills everything inside WSL — including the thing making the change.** And if the new value is too high for your host, **the WSL VM can fail to launch at all**, stranding you.
>
> We learned this the expensive way: `memory=40GB` on a 64 GB host made the VM refuse to boot — ~30 minutes lost and a full reboot to recover. The native-Windows serving path sidesteps this completely: you never touch `.wslconfig`.

---

## How to actually serve a model

Grab a prebuilt Windows CUDA build of `llama-server.exe` from the [llama.cpp releases](https://github.com/ggml-org/llama.cpp/releases) (the win-cuda `bin` + `cudart` zips), then from **Windows PowerShell** (not WSL):

```powershell
.\llama-server.exe -m C:\models\your-model.gguf `
  -ngl 99 `              # offload all layers to the GPU
  -c 32768 `            # context length
  -fa on `             # flash attention
  --host 0.0.0.0 --port 8080
```

`-ngl 99` puts the weights in VRAM; `--host 0.0.0.0` makes it reachable from WSL and your LAN. Prefer a GUI? **LM Studio** or **Ollama for Windows** both expose an OpenAI-compatible endpoint with zero command line.

### Reaching it from WSL (this trips people up)

It depends on your WSL networking mode ([Microsoft WSL networking docs](https://learn.microsoft.com/en-us/windows/wsl/networking)):

- **Mirrored mode** (`networkingMode=mirrored` in `.wslconfig`, Windows 11 22H2+): `http://127.0.0.1:8080` reaches the Windows host directly. (Mirrored mode also fixes the IPv6 download issue below.)
- **NAT mode** (the default): `127.0.0.1` refers to **WSL itself, not Windows.** Use the Windows host IP — the default gateway:

```bash
# From WSL — works in both modes (tries localhost, then the NAT gateway):
curl -s http://127.0.0.1:8080/health || \
curl -s "http://$(ip route | awk '/^default/ {print $3}'):8080/health"
```

---

## VRAM sizing: how much to leave for the desktop

On a display GPU, leave room for **DWM** (the Windows compositor), which keeps every window's content in off-screen VRAM surfaces.

<p align="center">
  <img src="assets/vram-budget.png" alt="VRAM budget on a display GPU: leave roughly 2–3 GB of headroom for the Windows compositor (DWM). A 24 GB card fits about 21 GB of model plus KV cache; a 32 GB card fits about 28–29 GB. DWM figures are community estimates and vary with resolution, monitor count, HDR and open windows." width="880">
</p>

> ⚠️ **No official numbers exist** for DWM VRAM use — vendors don't publish them. The figures below are **community estimates** (Task Manager / GPU-Z observations), and they vary a lot with resolution, monitor count, HDR, and how many windows are open.

Rough budget:
- DWM idle, single 1440p: a few hundred MB. 4K / multi-monitor / HDR / lots of windows: up to ~1–2 GB.
- **Leave ~2–3 GB free** as a safe margin on a display GPU.

So target roughly:
- **24 GB card →** ~21 GB max for model + KV cache
- **32 GB card →** ~28–29 GB max

A model's VRAM ≈ (quantized file size) + (KV cache, which grows with context length). A Q4_K_M of a ~30B model is ~18–22 GB; choose context length so model + KV cache + ~2–3 GB headroom stays under your card's VRAM. If you set `-ngl 99` and hit OOM, lower the context length first, then the quant.

---

## Troubleshooting table

| Symptom | Most likely cause | Fix |
|---|---|---|
| Screen blacks out a few seconds during model load, then recovers | WDDM TDR killing the long load kernel | Raise `TdrDelay` (Fix 1a) + reboot |
| Hard crash / reboot / `VIDEO_TDR_FAILURE (0x116)` on load | TDR, sometimes plus an early Blackwell driver | Fix 1a; update to a current driver |
| Momentary black flashes / flicker during use | MPO conflict (community-reported) | Disable MPO (Fix 1c) + reboot |
| `cudaMalloc failed: out of memory` in WSL, but `nvidia-smi` shows free VRAM | WSL2 VM bound (esp. Blackwell's ~16 GiB hidden overhead) | Serve on native Windows (Fix 2) |
| Inference slows to a crawl as context grows | CUDA sysmem fallback spilling VRAM→RAM | NVIDIA app → Prefer No Sysmem Fallback (Fix 1b) |
| First tokens after idle are slow / occasional load timeout | GPU sitting in a deep idle power state | NVIDIA app → Prefer maximum performance (Fix 1b) |
| Random hard GPU hang on a PCIe 5.0 board | PCIe link instability | Try forcing PCIe Gen4 in BIOS (Fix 1d) |
| HF download stuck at 0 bytes in WSL | IPv6 routing black-hole | `curl -4` (see below) |
| Model loaded but WSL can't reach the server | WSL networking mode | `127.0.0.1` (mirrored) or host gateway IP (NAT) |

---

## FAQ

**Do I need two GPUs or a headless card?**
No. A single display GPU works after the TDR fix. We run one 5090 that drives the monitor and serves models at the same time.

**Will this hurt gaming or normal GPU use?**
No. A higher `TdrDelay` and disabling MPO are standard tweaks in the 3D-rendering community; they don't reduce performance. The only `TdrDelay` tradeoff is a longer freeze *if* the GPU ever genuinely hangs.

**Is a high `TdrDelay` dangerous?**
Only in this sense: a genuine GPU hang freezes the desktop for the full `TdrDelay` before Windows recovers it (vs 2s default). That's why we suggest **20s**, not 60–120s, for a daily-driver display GPU.

**Why not just use Linux / dual-boot?**
You can — bare-metal Linux is genuinely the cleanest path for GPU compute (no WDDM, no VM). The point of this guide is that you don't *have* to abandon Windows if it's your daily driver.

**Does this apply to AMD GPUs?**
TDR is a Windows feature, not NVIDIA's, so the TDR and MPO fixes apply to AMD too. The CUDA-specific and NVIDIA-app steps don't — AMD uses ROCm/Vulkan.

**Is this anti-Mac?**
Not at all. Apple Silicon's unified memory is excellent for local LLMs. This guide is "you don't have to switch away from your Windows box," not "Windows is best."

**Does the WSL memory problem mean WSL is useless for LLMs?**
No — small/medium models that fit comfortably inside the WSL VM run fine. It's specifically *large* models (and Blackwell's hidden overhead) where native Windows wins. And you can always drive a native-Windows server from WSL.

---

## Bonus gotcha: HuggingFace downloads stall in WSL

If `curl`/`wget`/`huggingface-cli` hangs at 0 bytes downloading from HuggingFace **inside WSL2**, it's usually an **IPv6 routing** problem — HF resolves to IPv6 and the connection black-holes. Force IPv4:

```bash
curl -4 -L -C - --noproxy '*' -o model.gguf \
  "https://huggingface.co/<repo>/resolve/main/<file>.gguf?download=true"
```

`-4` forces IPv4, `-C -` resumes a partial download. If you run a local MITM/proxy, also unset `SSL_CERT_FILE` / `*_proxy` for the download. (Mirrored WSL networking can also resolve this by fixing IPv6 handling.)

---

## TL;DR checklist

1. **Admin PowerShell:** set `TdrDelay=20`, `TdrDdiDelay=20` → **reboot.** (Verify with `reg query`.)
2. **NVIDIA app → Global Settings:** Power management → *Prefer maximum performance*; CUDA - Sysmem Fallback Policy → *Prefer No Sysmem Fallback*.
3. **Seeing flicker?** Disable MPO (community fix) + reboot.
4. **Serve big models from native Windows** (full host RAM, most stable GPU path). Drive them from WSL over HTTP.
5. **Never** raise the WSL RAM cap / `wsl --shutdown` if a live process runs inside WSL.
6. **HF downloads stalling in WSL?** `curl -4`.

That's the whole game. Windows is fine now — we use it every day.

---

## Sources

Official documentation:
- Microsoft — [TDR Registry Keys](https://learn.microsoft.com/en-us/windows-hardware/drivers/display/tdr-registry-keys) and [Timeout Detection and Recovery](https://learn.microsoft.com/en-us/windows-hardware/drivers/display/timeout-detection-and-recovery)
- Microsoft — [WSL networking (mirrored vs NAT)](https://learn.microsoft.com/en-us/windows/wsl/networking)
- NVIDIA — [CUDA on WSL User Guide](https://docs.nvidia.com/cuda/wsl-user-guide/index.html)

Verified GitHub issues:
- [microsoft/WSL #40401](https://github.com/microsoft/WSL/issues/40401) — Blackwell sm_120 ~16 GiB CUDA-context overhead in WSL2 (invisible to `mem_get_info`)
- [microsoft/WSL #11050](https://github.com/microsoft/WSL/issues/11050) — WSL2 ignores the CUDA Sysmem Fallback Policy
- [ollama/ollama #15024](https://github.com/ollama/ollama/issues/15024) — `nvlddmkm` Event ID 153 driver crash from context load (RTX 3090, WSL2)
- [NVIDIA/open-gpu-kernel-modules #1010](https://github.com/NVIDIA/open-gpu-kernel-modules/issues/1010) — Blackwell PCIe link / GSP-timeout instability (Linux)

Community (clearly marked as such above): MPO-disable registry tweaks (`DisableOverlays`, `OverlayTestMode`) and DWM VRAM-usage figures are community knowledge, not vendor-documented.

> **Found another Windows/WSL LLM gotcha and its fix?** Open a PR. The goal is to replace the "Windows can't do local LLMs" myth with concrete, tested, *honestly-sourced* fixes.

---

*Written by people who run this setup daily — after hitting every one of these walls ourselves.*
