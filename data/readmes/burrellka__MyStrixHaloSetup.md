# Getting a Strix Halo box actually working for local LLMs

**This is a Linux guide.** The first thing I did with this machine was wipe Windows and install Linux Mint. Everything below assumes an Ubuntu 24.04 (Noble) base — Mint on Noble works identically. If you plan to stay on Windows, this guide will not help you.

A working setup for AMD Ryzen AI Max+ 395 ("Strix Halo") mini PCs, written by someone who is not an ML engineer and got it working anyway.

**~120GB of usable memory for models. NPU running alongside the GPU, costing under 4% of GPU throughput instead of 69%. Both engines serving from one API.**

---

## Who this is for

You bought (or are considering) a Strix Halo mini PC — 128GB unified memory, roughly $2000-2800 depending on vendor — because you wanted to run large models locally. You are technically competent and comfortable in a terminal. You are **not** a machine learning engineer, and you don't want to lose a week to kernel mailing lists figuring out why your NPU doesn't exist.

You've probably already found the forum posts. Slow inference. Phantom memory ceilings. Half your RAM missing. The NPU that never shows up. Version-matrix hell where fixing one thing breaks another.

That was me. It took nine days. This is the two-day version.

## Who this is NOT for

If you build ROCm from source for fun, if you have opinions about quantization schemes, if you knew what `gfx1151` meant before reading this — you already know more than this guide contains. Some choices below are "the thing that worked," not "the optimal thing." You will find better. Please open an issue and tell me; I'll fold it in.

This guide is deliberately conservative. It prefers the boring path that works over the clever path that might.

---

## What you get at the end

All numbers below are measured on my box (128GB Strix Halo), not projected. Your mileage varies with model, quantization, and context length.

- **The full memory pool actually usable** (~120GB), instead of the ~62GB the box ships with or the phantom ~80GB some apps report.
- **A ~4x GPU inference speedup just from fixing the backend.** My daily-driver 26B MoE went from **~58 tok/s on Vulkan to ~230 tok/s on ROCm** — same model, same box, same quantization. The memory fixes and the ROCm backend are the whole difference. (Prefill on that model runs ~1,250 tok/s, but decode is the number that reflects what using it actually feels like.)
- **NPU inference via FastFlowLM, running genuinely in parallel.** A 1B model on the NPU sustains **~61 tok/s with the GPU at 0% utilization** — proof the two engines are independent. And running that NPU workload alongside GPU work costs the GPU about **3%** throughput; the *same* workload placed on the GPU costs **69%**. That ~20x difference is the whole reason to bother with the NPU.
- **One OpenAI-compatible endpoint** serving both engines, so anything speaking the OpenAI API just works.

> **The MoE caveat, because it matters for that 230 number:** my daily driver is a *Mixture-of-Experts* model (Gemma-4-26B-A4B — ~26B total parameters but only ~4B active per token). MoE is *why* it's this fast: each token only pulls a fraction of the weights through the box's ~256 GB/s memory bandwidth. A **dense** 27B model on the same hardware would be dramatically slower, because every token drags all 27B of weights through that same bandwidth. **On unified-memory hardware like this, decode speed is bound by memory bandwidth, not compute.** If you want speed, run MoE models. If you load a dense 70B expecting these numbers, you'll be disappointed — and that's physics, not a setup mistake.

---

## Before you start

Three read-only checks, two minutes:

```bash
# 1. Kernel version — you want 6.14, 6.17, or 6.18
uname -r

# 2. How much RAM does the OS actually see?
free -h

# 3. Is IOMMU enabled? (#1 silent killer of NPU support)
dmesg | grep -i -E "AMD-Vi|IOMMU" | head
```

**If `free -h` shows ~62GB on a 128GB box, that is not a fault — it's the factory default, and Step 0 fixes it.**

If IOMMU is disabled, enable it in BIOS before anything else. Nothing NPU-related works without it and the failure modes are confusing.

---

## The sequence

Eight steps. Order matters — Step 0 must come first (nothing in Linux can fix it), and Step 3 must come before Step 5. Both explained in the traps section.

### Step 0 — Fix the BIOS memory carve-out (do this first, biggest single win)

**Symptom:** `free -h` shows ~62Gi on a 128GB machine. Half your RAM is gone.

These boxes ship with the BIOS hard-reserving a large fixed block as dedicated VRAM. Mine arrived with **64GB** locked away at firmware level. Visible in the kernel log:

```bash
dmesg | grep -i "amdgpu: VRAM\|GTT memory ready"
```

Factory default looks like:
```
amdgpu: VRAM: 65536M (65536M used)     ← 64GB walled off by BIOS
```

**No amount of Linux configuration fixes this.** It's a firmware-level reservation, invisible to the OS.

**The fix:** reboot into BIOS (usually `Del` on these boards) and find the UMA / VRAM allocation setting. The label varies by vendor — look for **UMA Frame Buffer Size**, **iGPU Memory Allocation**, or **Dedicated Graphics Memory**, often under *Advanced → GFX Configuration*.

**Set it to the minimum** (typically 512MB, or "UMA Auto" / "Minimum").

This is counterintuitive. Instinct says a bigger GPU allocation must be better. It is not. On Linux the GPU reaches system memory dynamically through GTT, so a small carve-out plus a large dynamic ceiling beats a big fixed partition in every scenario. A fixed 64GB block sits reserved whether a model is using it or not.

After the change, the same command should show:
```
amdgpu: VRAM: 512M (512M used)
amdgpu: 63968M of GTT memory ready
```
and `free -h` should show ~124Gi.

> Some stripped-down mini-PC BIOSes don't expose this setting at all. If yours doesn't, that's a real limitation — worth checking reviews before buying.

### Step 1 — Raise the kernel's dynamic memory ceiling (GRUB)

Step 0 freed the RAM. This step lets the GPU actually *claim* it when a big model loads.

After the BIOS fix the kernel defaults to roughly a 62GB GTT ceiling. Check yours:

```bash
cat /sys/module/ttm/parameters/pages_limit
```

That's in 4KB pages. `16376050` ≈ 62.5GB. Any model needing more will fail to load.

Raise it to ~120GB (120 × 1024³ ÷ 4096 = **31457280** pages):

```bash
sudo cp /etc/default/grub /etc/default/grub.bak
sudo nano /etc/default/grub
```

Append to the existing `GRUB_CMDLINE_LINUX_DEFAULT` — don't retype the line, just add to it:

```
ttm.pages_limit=31457280 ttm.page_pool_size=31457280
```

Result should be a single line:

```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash ttm.pages_limit=31457280 ttm.page_pool_size=31457280"
```

Verify before committing, then apply:

```bash
grep GRUB_CMDLINE_LINUX_DEFAULT /etc/default/grub    # one line, quotes at each end
sudo update-grub
sudo reboot
```

Confirm after reboot:

```bash
cat /sys/module/ttm/parameters/pages_limit    # want: 31457280
free -h                                        # still ~124Gi
dmesg | grep "GTT memory ready"                # now ~120GB
```

**This is a ceiling, not a reservation.** The GPU grows into it when a large model loads and releases the memory when the model unloads. Setting it high costs nothing at idle — which is exactly why the BIOS fix had to come first. Before Step 0, "120GB" would have meant permanently walled off. After it, 120GB is a max the OS can reclaim.

> `page_pool_size` must match `pages_limit`, or the allocator caps you at the smaller pool. On some driver versions an oversized pool slightly increases idle bookkeeping — if `free -h` looks odd at idle, drop `page_pool_size` back to default and keep only `pages_limit`.

### Step 2 — Raise the memlock limit

The NPU runtime needs to lock far more memory than the default (~16MB) allows.

```bash
sudo tee -a /etc/security/limits.conf > /dev/null <<'EOF'
*    soft    memlock    unlimited
*    hard    memlock    unlimited
EOF
```

Log out and back in, confirm with `ulimit -l`. Root sessions may still show the old value — expected, and the Lemonade service handles it itself via `LimitMEMLOCK=infinity`.

### Step 3 — Fix the NPU firmware (read Trap 1 before doing anything)

```bash
cat /sys/bus/pci/drivers/amdxdna/*/fw_version
```

If it shows **1.0.0.166** (what stock `linux-firmware` ships), you're below FastFlowLM's minimum of 1.1.0.0 and the NPU will not work.

**Do not fix this by downloading newer firmware manually. That bricks the NPU.** See Trap 1.

The correct fix installs a *matched* driver+firmware pair:

```bash
sudo apt install linux-headers-$(uname -r) dkms

sudo add-apt-repository ppa:lemonade-team/stable
sudo apt update

sudo apt install amdxdna-dkms
sudo reboot
```

Verify all four after reboot:

```bash
# 1. Driver must be the DKMS one — path MUST contain "updates/dkms"
modinfo amdxdna | grep filename

# 2. Firmware clears the minimum
cat /sys/bus/pci/drivers/amdxdna/*/fw_version    # want 1.1.x+

# 3. No protocol mismatch
dmesg | grep -i amdxdna

# 4. Built for your running kernel
dkms status
```

Healthy result: firmware `1.1.2.65`, a `filename` under `updates/dkms`, driver initialized cleanly. You'll see two "tainting kernel" lines — **normal** for any out-of-tree DKMS module, not errors.

Rollback is clean: `sudo apt remove amdxdna-dkms` and reboot.

### Step 4 — Install the NPU userspace runtime

```bash
sudo apt install libxrt-npu2
```

AMD XRT runtime plus the XDNA plugin. Pure userspace, touches nothing in the kernel or GPU stack.

### Step 5 — Install Lemonade

```bash
sudo apt install lemonade-server
```

A headless local LLM server exposing an OpenAI-compatible API and driving both engines. Auto-installs the FastFlowLM binary if it isn't on your PATH, and its systemd unit sets `LimitMEMLOCK=infinity`.

(There's also `lemonade-desktop`, a GUI web app. Skip it on a headless box.)

### Step 6 — Configure it (do not skip — see Trap 2)

```bash
sudo find /etc/lemonade /var/lib/lemonade -name '*.json' -o -name '*.conf' 2>/dev/null
```

| Setting | Value | Why |
|---|---|---|
| `enable_dgpu_gtt` | `true` | **The single most important flag here.** Without it the app can't use the GTT pool and you get the phantom ~80GB ceiling — even after Steps 0 and 1. |
| `host` | `0.0.0.0` | Only if reaching it from other machines on your LAN. Leave `localhost` otherwise. |
| `extra_models_dir` | your GGUF path | Point at existing models so you don't re-download. |

Restart and verify:

```bash
sudo systemctl restart lemonade-server
journalctl -u lemonade-server -n 50 | grep -i "memory pool\|System RAM"
```

You want the large pool (~120GB). If it says 0.5GB, that's the tiny VRAM carve-out and GTT is still off.

### Step 7 — Install backends and pull a model

```bash
lemonade backends install llamacpp:rocm
```

**You do not need to build ROCm from source.** Lemonade ships a prebuilt llama.cpp+ROCm binary explicitly targeting `gfx1150/gfx1151/gfx1152` — which is what Strix Halo is. One command instead of a multi-hour version-matrix fight.

Prove the NPU works with the smallest model:

```bash
lemonade pull llama3.2-1b-FLM

curl -s -X POST http://localhost:13305/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"llama3.2-1b-FLM","messages":[{"role":"user","content":"Write 200 words about the ocean."}],"max_tokens":300}' \
  | python3 -m json.tool
```

Two things confirm success: the response `id` contains `fastflowlm` (only FLM runs on the NPU), and decode speed lands around **60+ tok/s**. Confirm the GPU is genuinely idle:

```bash
cat /sys/class/drm/card*/device/gpu_busy_percent    # 0 during NPU inference
```

---

## The traps

Symptom first, because that's what you'll search at 2am.

### Trap 0 — "My 128GB box only has 62GB of RAM"

**Symptom:** `free -h` shows ~62Gi. `dmesg` shows `amdgpu: VRAM: 65536M (65536M used)`.

Not a fault, not a Linux problem, not fixable in Linux. The BIOS ships with a large fixed VRAM carve-out. See Step 0. Highest-value fix in this guide, takes five minutes.

**The counterintuitive part:** set the GPU's BIOS memory allocation to the *minimum*, not the maximum. On Linux, dynamic GTT allocation plus a high kernel ceiling beats a fixed partition in every scenario.

### Trap 1 — "My NPU firmware is too old, so I'll just update the firmware"

**Symptom:** firmware reads `1.0.0.166`; FastFlowLM requires ≥1.1.0.0.

**The obvious fix that destroys your NPU:** manually dropping in newer firmware (e.g. `npu.sbin` 1.1.2.65). The stock in-tree driver can't speak the newer protocol:

```
aie2_check_protocol: Incompatible firmware protocol major 7 minor 2
firmware is not alive
```

and the NPU **disappears entirely**. FastFlowLM's docs confirm: forcing 1.1 firmware "can make the NPU disappear because the in-tree driver expects the older firmware protocol."

**The actual fix:** `amdxdna-dkms`, which installs a matched pair — a driver speaking protocol 7 alongside protocol-7 firmware. Both halves move together. Documented in AMD's own `xdna-driver` issue #1219, describing this exact hardware and version mismatch.

**How to know you fixed it right:** `modinfo amdxdna | grep filename` must show a path containing `updates/dkms`. A stock in-tree path means the DKMS driver isn't active and you'll hit the protocol error.

### Trap 2 — The phantom memory ceiling (app-layer)

**Symptom:** your inference app reports ~80GB usable and refuses to allocate more — *even after* fixing BIOS and GRUB.

**What it is not:** a hardware limit.

**What it is:** an application-layer detection bug. Some servers misread the GTT pool. I confirmed this by running two apps side by side on the same box in the same minute: one reported 80.3GB, the other 120.5GB. Same hardware, same drivers. The app was the broken layer.

**The fix:** in Lemonade, `enable_dgpu_gtt: true`, then confirm the logs show the large pool. If your server reports the small number and has no equivalent flag, that's an argument for changing servers, not for buying RAM.

Note there are **three independent memory limits** on this hardware: the BIOS carve-out (Trap 0), the kernel GTT ceiling (Step 1), and the app's detection (this one). All three have to be right.

### Trap 3 — Doing things in the wrong order

Firmware updates touch the GPU stack *and* the NPU stack simultaneously. If you build and validate your GPU setup first, then update firmware, you've invalidated your own validation.

**Firmware first, then GPU.** Confirm existing GPU inference still works after the firmware change (your canary), *then* build the new GPU stack on settled firmware. One validation pass instead of two ambiguous ones.

### Trap 4 — Version-matrix fragility

Genuinely fragile, and the source of many horror stories:

- At least one `linux-firmware` release has broken ROCm outright.
- At least one ROCm release (7.0.2) has a memory-detection bug reporting ~62GB.
- The community-verified line at time of writing was ROCm 6.4.x.

**Practical advice:** use the prebuilt backend rather than assembling your own. Once you have a working combination, **pin it**:

```bash
sudo apt-mark hold lemonade-server
```

Then upgrade deliberately, with a config backup and a known-good version to roll back to. Don't let a routine `apt upgrade` silently rearrange your inference stack.

### Trap 5 — Assuming generic AMD advice applies to your chip

Much of what you'll find online is for Strix Point, discrete Radeon cards, or older XDNA. Strix Halo (`gfx1151`, PCI ID `17f0:11`) is specific enough that generic advice frequently doesn't apply. Include the chip identifier when searching, and check what silicon someone is on before taking their fix.

### Trap 6 — Trusting a utilization gauge over actual evidence

**Symptom:** you run a model on the NPU and NPU utilization reads 0%.

That may be a broken gauge, not a broken engine. Verify with evidence: does the response ID name the NPU runtime? Is throughput in the range that runtime produces? Is GPU busy percentage zero during the call? Those three together beat a utilization number that may simply not be wired up.

---

## What I'd do differently

**Check `free -h` on day one.** I ran for a while before noticing half the RAM was missing to a BIOS default. Five-minute fix, and everything downstream depends on it.

**Read the firmware trap before touching firmware.** Research turned up issue #1219 *before* I did the obvious thing. Moving faster would have bricked the NPU and cost a day recovering.

**Check the app's memory detection before blaming hardware.** I lost time believing an 80GB ceiling was real. One cross-check against a second app would have shown it was software in minutes.

**Look for the packaged path first.** I scoped a whole project around building ROCm from source. It was one command.

**Write things down as you go.** I kept a running document of every verified fact, every working command, every dead end. When something broke a week later, that document was worth more than my memory. It's also why this guide exists.

**Don't do the risky step tired.** The firmware update is the one action here that can take your NPU offline. Do it with time to verify and roll back.

---

## Full verification

```bash
# Memory: all three layers correct?
free -h                                              # ~124Gi
cat /sys/module/ttm/parameters/pages_limit           # 31457280
curl -s http://localhost:13305/api/v1/system-info | python3 -m json.tool

# NPU test — expect ~60 tok/s
curl -s -X POST http://localhost:13305/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"llama3.2-1b-FLM","messages":[{"role":"user","content":"hello"}],"max_tokens":50}'

# GPU idle during NPU work?
cat /sys/class/drm/card*/device/gpu_busy_percent
```

---

## After it's working — seeing and managing the fleet

Once the box is serving, the day-to-day question stops being "how do I get it running" and becomes "*what's actually loaded, is it healthy, and is the context I set the context that's really running?*" I built **[HELM](https://github.com/burrellka/HELM)** for exactly that — a self-hosted web control plane over Lemonade: an honest dashboard (the real memory pool, derived per-slot context, live throughput, crash detection), safe load / unload / pin controls, and a grounded model advisor. Same spirit as this guide — *show me it's true, don't guess* — and it runs fully read-only if you just want to look before you touch. Entirely optional; the setup above stands on its own.

---

## Corrections welcome

I am not an expert. Some of this is certainly suboptimal, and parts will go stale as Lemonade, ROCm, and the kernel drivers move. Please open an issue if:

- A version recommended here has been superseded
- A trap has been fixed upstream
- You have measurements from a different Strix Halo box (different vendor, RAM config, or BIOS)

The goal is that the next person loses an afternoon instead of a week.

---

## References

- [FastFlowLM](https://github.com/FastFlowLM/FastFlowLM) — the NPU runtime
- [Lemonade](https://github.com/lemonade-sdk/lemonade) — the server driving both engines
- [AMD xdna-driver issue #1219](https://github.com/amd/xdna-driver/issues/1219) — the firmware/protocol trap, documented
- Lemonade PPA: `ppa:lemonade-team/stable`

---

*Written from a nine-day setup log. Every command here was run on real hardware — these are what actually worked, not reconstructions.*
