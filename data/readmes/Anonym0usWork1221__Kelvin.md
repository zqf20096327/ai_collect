<p align="center">
  <img src="docs/assets/kelvin-banner.png" alt="Kelvin — AI-aware thermal governor and gaming performance engine for rooted Android" width="840">
</p>

<h1 align="center">Kelvin</h1>

<p align="center">
  <b>AI-aware thermal governor + gaming engine + on-device AI studio for rooted Android.</b><br>
  A tiny root daemon that sustains on-device LLM inference and maximizes game FPS — safely —
  plus a private, offline <b>AI studio</b> (local chat + image generation) and a RAM manager,
  wrapped in a neo-brutalist app with a floating performance HUD.
</p>

<p align="center">
  <a href="https://github.com/Anonym0usWork1221/Kelvin/releases/latest"><img src="https://img.shields.io/github/v/release/Anonym0usWork1221/Kelvin?display_name=tag&color=F5A623&label=release" alt="Latest release"></a>
  <img src="https://img.shields.io/badge/license-MIT-22D3EE" alt="MIT License">
  <img src="https://img.shields.io/badge/platform-Android%2014%2B-A3E635" alt="Android 14+">
  <img src="https://img.shields.io/badge/root-Magisk%20·%20KernelSU%20·%20APatch-F5A623" alt="Magisk / KernelSU / APatch">
  <img src="https://img.shields.io/badge/SoC-Snapdragon%208%20Gen%202%20/%208%20Elite-FF3B30" alt="Snapdragon 8 Gen 2 / 8 Elite">
  <img src="https://img.shields.io/badge/app-Kotlin%20·%20Compose-8B98A9" alt="Kotlin + Jetpack Compose">
</p>

<p align="center">
  <a href="#-install">Install</a> ·
  <a href="#-on-device-ai-studio">AI studio</a> ·
  <a href="#-using-the-kelvin-app">Using the app</a> ·
  <a href="#%EF%B8%8F-how-it-works">How it works</a> ·
  <a href="#-build">Build</a> ·
  <a href="docs/architecture.md">Architecture</a> ·
  <a href="docs/safety.md">Safety</a>
</p>

---

On-device AI is throttled by thermals: run a local **LLM** (`llama.cpp`, MediaPipe, ONNX
Runtime, QNN Genie) for a minute and GPU/CPU clocks collapse (680 → 300 MHz) as the phone
protects itself. Gaming thermal mods exist, but they chase **short FPS bursts**, not
**sustained** AI workloads — and nobody ships a governor that reshapes thermal behaviour
specifically for NPU/CPU-heavy inference.

**Kelvin does both.** It loads the right frequency curve for what you're actually doing:

> **How each one gets picked, honestly.** Inference is **auto-detected** — the daemon scans for
> engine processes and Kelvin's own AI studio announces itself, so AI-Sustained loads on its own.
> Games are **not** auto-detected: you assign a profile to a package once in the Apps tab and it
> loads whenever that game comes to the foreground. I'd rather you set one rule than have a
> heuristic guess wrong and pin your clocks during a video call.

- 🎮 **Game** — burst: raise the GPU + big-core floors for frame stability.
- 🧠 **AI-Sustained** — soak: hold clocks flat at a raised-but-bounded ceiling so inference
  throughput doesn't cliff after a few runs. *(The genuinely new part.)*
- ⚖️ **Balanced** / 🔋 **Battery** — stock-ish / efficiency.

All behind a **hard temperature ceiling**, a **stock-config backup**, and a **bootloop
watchdog** — Kelvin *reshapes* the thermal curve, it never removes the safety net.

<p align="center">
  <img src="docs/assets/kelvin-hero.png" alt="Kelvin — sustained on-device AI inference on one side, mobile gaming burst performance on the other" width="820">
</p>

## 📱 The app

A neo-brutalist Kotlin + Compose companion: live telemetry, one-tap profiles, per-app rules,
a safety panel, a draggable floating **HUD** you can pin over any game or LLM front-end, plus a
full **[on-device AI studio](#-on-device-ai-studio)** (local chat + image generation) and a **RAM
manager**. Smallest-possible APK — no analytics, offline-first.

<p align="center">
  <img src="docs/assets/screenshots/dashboard.png" width="200" alt="Kelvin dashboard — live skin/SoC/GPU temperature, thermal headroom, and one-tap Game / AI-Sustained / Balanced / Battery profiles">
  &nbsp;
  <img src="docs/assets/screenshots/telemetry.png" width="200" alt="Kelvin live telemetry — per-cluster CPU clocks, GPU frequency and busy percent, RAM, and engine detection toggles">
  &nbsp;
  <img src="docs/assets/screenshots/safety.png" width="200" alt="Kelvin safety panel — bootloop watchdog status, editable skin-temperature ceiling, hard thermal limits, and restore-stock">
  &nbsp;
</p>
<p align="center"><sub>Dashboard · Live sensors · Safety · Per-app profiles — all streaming from the root daemon over a local socket.</sub></p>

## 🧠 On-device AI studio

Kelvin isn't just a governor — it ships a **fully local, private AI studio** that runs entirely
on your phone. No cloud, no account, no data leaves the device. And because Kelvin *is* the
thermal governor, it flips itself into **AI-Sustained** the moment inference starts, so your
tokens/sec and image steps don't thermally cliff.

<p align="center">
  <img src="docs/assets/screenshots/ai-hub.png" width="200" alt="Kelvin AI hub — installed on-device models, one-tap chat and image generation, model manager, device RAM and NPU readout">
  &nbsp;
  <img src="docs/assets/screenshots/ai-chat.png" width="200" alt="Kelvin local LLM chat — streaming tokens from a llama.cpp GGUF model with load, stop, offload and AI-Sustained controls">
  &nbsp;
  <img src="docs/assets/screenshots/image-studio.png" width="200" alt="Kelvin image studio — on-device Stable Diffusion with a per-device CPU/GPU backend selector and explicit load-then-generate flow">
  &nbsp;
</p>
<p align="center"><sub>AI hub · Local chat (llama.cpp) · Image studio (Stable Diffusion) — 100% offline, on-device.</sub></p>

- 💬 **Local LLM chat (`llama.cpp` / GGUF).** Real streaming chat with any GGUF model, token by
  token, over a bundled `llama-server`. Multi-turn history that **persists to disk**, a searchable
  **History** screen (rename / delete), a **Stop** button, and **Offload** to free RAM. Tool-calling
  is wired so the model can ask the image engine to *draw* a picture mid-conversation.
- 🎨 **On-device image generation (Stable Diffusion 1.5 / stable-diffusion.cpp).** Type a prompt,
  get a real image — no gradient placeholders. A **persistent server** loads the model **once**
  (device-specific compute compiled at load, like a warmed-up LLM), then generations run instantly
  after. A **per-device backend picker (Auto / GPU / CPU)** is discovered from your actual hardware,
  with **load → generate**, **Reload / Offload**, **Stop**, and one-tap **Save to Photos**. Private
  gallery — nothing touches your camera roll until you export it.
- ⚡ **Chat on the Hexagon NPU.** llama.cpp has an upstream Hexagon backend, and Kelvin ships it. On a
  Snapdragon **8 Gen 2 or newer** with a **Q4_0** model, flip the accelerator to NPU in Runtime and the
  work moves off the CPU. The catch is real and Kelvin says so up front: only Q4_0 (and Q8_0/MXFP4)
  can be repacked for the DSP, so a Q4_K_M model stays on the cores. The toggle stays greyed out —
  with the reason — unless your build, your chip and your model all line up. Details, numbers and the
  parts that *don't* work: [docs/npu.md](docs/npu.md).
- 🔁 **Convert a model on your own GitHub Actions minutes.** Most of HuggingFace is raw safetensors,
  which no phone runtime loads. Your phone can't convert it either — no Python, no RAM, no disk. So
  fork Kelvin, paste a token, and the app dispatches a conversion job **in your fork**, watches it,
  and downloads the finished GGUF straight back. Q4_0 output is what makes a model NPU-ready, which
  closes the loop.
- 📦 **Model manager that recognises more than GGUF.** Paste any **HuggingFace** repo and Kelvin
  classifies it: GGUF, diffusion checkpoints, **QNN context binaries** (with a Hexagon version check
  before you spend a gigabyte), Nexa, LiteRT, `.task`, ExecuTorch, MNN, SNPE. Whole-folder models
  install with their directory layout intact. Downloads are **resumable, cancellable, foregrounded**,
  with an optional **token for gated models**. Anything it can't run says why, and offers conversion
  when that's the answer.
- 🧮 **RAM manager (root).** Real per-process **PSS/USS** from `smaps_rollup`, safe **force-stop** of a
  heavy app behind a server-side deny-list (system-critical processes are protected), and a genuine
  **Clear cached RAM** (`drop_caches` + compact) — the honest "free RAM", not a fake booster.

> **Why root helps AI:** Android's phantom-process killer SIGKILLs a CPU-heavy inference child the
> instant it spikes; Kelvin launches its engines as a **root-owned process** that survives, and holds
> **AI-Sustained** clocks so throughput stays flat. Everything degrades gracefully without root —
> chat and images still run, you just lose the governor + full RAM manager.

## 🧩 Two planes, one product

A root module can't draw a UI; an app can't write `/sys`. So Kelvin is split, and the two
halves talk over a **root-owned abstract `AF_UNIX` socket** (`@kelvin`, line-delimited JSON):

- **`kelvind`** — a tiny (~31 KB) native **C** daemon in a Magisk/KernelSU/APatch module: the
  workload detector, profile engine, safety layer, and per-SoC path providers.
- **Kelvin app** — a **Kotlin + Compose** companion: floating HUD (FPS, clocks, temps,
  tokens/sec, RAM), one-tap profiles, per-app rules, a safety panel, and launcher-icon
  hide/show. It renders what the daemon reports and sends it commands — it never touches `/sys`.

See [docs/architecture.md](docs/architecture.md) and the socket contract in
[protocol/README.md](protocol/README.md).

## 📦 Repository layout

```
kelvin/
├── daemon/     native C governor (kelvind) + RAM manager + per-SoC providers   ← the core
├── module/     Magisk/KernelSU/APatch packaging
├── app/        Kotlin + Compose companion — HUD, dashboard, per-app profiles, safety,
│               AI studio (local chat + image gen), RAM manager
├── protocol/   daemon↔app control-socket contract
├── docs/       architecture · safety · SoC matrix · AI studio · NPU · tooling
├── scripts/    build-daemon.sh · build-sd.sh (NDK cross-compile)
└── .github/    CI: daemon build · app build · tag → signed release
```

## ⚙️ How it works

Each ~5 Hz tick, the daemon: reads sensors → detects the workload (foreground app + a `/proc`
scan for inference-engine signatures) → runs the **safety interlock** → resolves a profile
(with hysteresis to avoid clock thrash) → applies **only safe, reversible knobs** (cpufreq
`scaling_min/max`, GPU devfreq `min/max`) → publishes stats to the app. Full write-safety
rules: [docs/safety.md](docs/safety.md).

> **On-device finding:** the vendor thermal-engine continuously rewrites `scaling_max`, so
> max-caps are best-effort — **raising the floor (`scaling_min`) is the authoritative lever**,
> which is exactly why the AI-Sustained curve holds.

## 📲 Install

1. Download **`kelvin.zip`** from [Releases](https://github.com/Anonym0usWork1221/Kelvin/releases/latest).
2. Flash it in **Magisk / KernelSU / APatch** Manager.
3. **Reboot.**
4. *(Recommended)* install the companion app: grab **`Kelvin-<version>.apk`** from the same
   release and open it. It's signed and offline — no Play Store, no internet permission.

Requires root (Magisk 20.4+, KernelSU, or APatch). Fully systemless and reversible —
disable or remove the module to restore stock.

## 🚀 Using the Kelvin app

1. **Onboarding.** On first launch Kelvin checks that the root daemon is reachable
   (`kelvind detected — you're linked`), then walks you through granting the **display-over-
   other-apps** permission (for the HUD) and the notification permission.
2. **Dashboard.** See live **skin / SoC / GPU** temperature, thermal **headroom** against the
   ceiling, and per-cluster clocks. Leave **Auto-Switch** on to let the daemon pick the profile
   from the detected workload, or tap **Game / AI-Sustained / Balanced / Battery** to pin one.
3. **Floating HUD.** From the **HUD** tab, launch the overlay: a draggable, snap-to-edge strip
   of FPS · clocks · temps · tokens/sec · RAM. Tap it to toggle compact/expanded; tune opacity,
   corner, refresh rate, and which stats show.
4. **Per-app profiles.** In **Apps**, assign a profile to any package — it auto-loads whenever
   that game or your llama.cpp front-end comes to the foreground.
5. **Safety.** View the bootloop-watchdog / interlock status, **lower** the skin-temp ceiling
   within the daemon's hard limit, and one-tap **Restore stock**.
6. **AI studio** *(AI tab)*. Tap **Add model** to download a GGUF chat model or a Stable Diffusion
   image model (or paste a HuggingFace link). Open a model to **chat** (streaming, saved history),
   or the **Image** studio to pick a compute **backend (Auto / GPU / CPU)**, **Load** the model once,
   then **Generate** — save to Photos when you like it. **RAM** tab: stop a heavy app or **clear
   cached RAM**.
7. **Hide the icon** *(Settings)*. Kelvin can drop its launcher icon; reopen it with the
   **Quick Settings tile** or the dialer secret code **`*#*#5358#*#*`**.

## 🔨 Build

Toolchain setup (Ubuntu): [docs/tooling.md](docs/tooling.md).

**Daemon** (module):

```bash
export ANDROID_NDK_HOME=/path/to/ndk
bash scripts/build-daemon.sh          # → module/bin/{arm64-v8a,armeabi-v7a}/kelvind
cd module && zip -r ../kelvin.zip .   # package (CI does this on a v* tag)
```

Host sanity build (no NDK): `gcc -std=c11 -D_GNU_SOURCE -Wall -Wextra -Idaemon/include daemon/src/*.c daemon/soc/*.c -o kelvind`.

**App:**

```bash
cd app && ./gradlew assembleDebug     # or assembleRelease (signed when a keystore is present)
```

**AI engine binaries** (bundled in the APK, **git-ignored + CI-built** like `kelvind`): the chat
engine is llama.cpp's `llama-server` and the image engine is stable-diffusion.cpp's `sd-server`.
Reproduce the image one with `scripts/build-sd.sh [cpu|vulkan]` → `app/src/main/jniLibs/arm64-v8a/
libstable-diffusion-server.so`.

Tag a version (`git tag v0.6.0 && git push --tags`) and CI cross-compiles both ABIs, packages
`kelvin.zip`, builds a **signed** `Kelvin-<version>.apk`, and publishes the GitHub Release.

## 🖥️ Supported hardware

Kelvin used to be Snapdragon-or-nothing. It isn't any more — there are four providers now, and the
last one catches everything with a cpufreq policy, which is every Android phone made this decade.

| Provider | Chips | What you get |
|---|---|---|
| `qcom` | Snapdragon (8 Gen 2 SM8550 is my test bench; 8 Gen 3, 8 Elite, 8 Elite Gen 5) | CPU clocks, governor, Adreno GPU + busy%, gaming-phone fans |
| `mediatek` | Dimensity / Helio | CPU clocks, governor, Mali GPU, PPM user limits so MediaTek's power manager cooperates |
| `exynos-tensor` | Exynos 2100→2600, Google Tensor G1→G5 | CPU clocks, governor, Mali GPU via devfreq or `/sys/kernel/gpu` |
| `generic` | anything else | CPU clocks, governor, GPU if it uses devfreq, temperatures, a fan if it's a cooling device |

You lose the vendor extras on `generic`, not the product. Full detail, including every path and every
node I refuse to touch: [docs/soc-matrix.md](docs/soc-matrix.md).

**Changing the CPU governor** is new too — `schedutil`, `performance`, `powersave` and friends, from
the Tuning screen, behind a daemon-side allow-list. `userspace` isn't on it, and
[docs/safety.md](docs/safety.md) explains why.

## 🛡️ Safety

Kelvin runs as root and writes `/sys`. It enforces an absolute skin (48 °C) and SoC junction
(95 °C) ceiling in a path no profile can override, backs up your stock config before the first
write, restores it on exit or thermal interlock, and holds stock for a whole boot if the previous
one looked unstable. It **never** writes `emul_temp`, **never** disables a critical thermal zone,
and **never** touches thermal trip points at all.

[docs/safety.md](docs/safety.md) is the full contract — every node it writes, every node it refuses
to, and why. Worth reading before you trust any root thermal tool on your daily driver.

## 📚 Documentation

| | |
|---|---|
| [docs/ai-studio.md](docs/ai-studio.md) | Using the on-device AI: models, chat, images, the fit gate, the RAM manager |
| [docs/npu.md](docs/npu.md) | Running models on the Hexagon NPU, and converting the ones that won't |
| [docs/soc-matrix.md](docs/soc-matrix.md) | Which chips are supported, every sysfs path, governor control |
| [docs/safety.md](docs/safety.md) | The write contract and the four rules behind it |
| [docs/architecture.md](docs/architecture.md) | How the two planes fit together |
| [docs/tooling.md](docs/tooling.md) | Building everything from scratch on Ubuntu |
| [protocol/README.md](protocol/README.md) | The daemon socket, if you want to drive it yourself |

## 🤝 Contributing

Confirm or request your chipset via the
[device-support template](.github/ISSUE_TEMPLATE/device-support.md) (include the sysfs probe).
A new SoC is one file in `daemon/soc/` plus one line in the registry — most of the work is already
done by the shared layer. See [docs/soc-matrix.md](docs/soc-matrix.md).

## 📄 License

MIT © 2026 **Abdul Moez** ([@Anonym0usWork1221](https://github.com/Anonym0usWork1221)). See [LICENSE](LICENSE).

Some components Kelvin builds against or downloads are under other licences — notably Qualcomm's QNN
runtime, which the app fetches from Maven Central and which the MIT text does not cover. See
[NOTICE.md](NOTICE.md).

> ⚠️ Kelvin changes CPU/GPU/thermal behaviour on rooted devices. It ships extensive
> safeguards, but you run it at your own risk.

<p align="center"><sub>
<b>Keywords:</b> on-device AI · local LLM · offline AI chat · llama.cpp · GGUF · on-device Stable
Diffusion · stable-diffusion.cpp · local image generation · Magisk module · KernelSU · APatch ·
AI thermal governor · CPU/GPU frequency scaling · sustained inference · gaming performance · FPS
boost · tokens/sec · Snapdragon 8 Gen 2 / 8 Elite · Adreno · Hexagon NPU · QNN · rooted Android ·
Android RAM manager · drop_caches · floating performance HUD · Kotlin Jetpack Compose.
</sub></p>
