<div align="center">

<img src="assets/AppIcon.png" width="120" height="120" alt="Colab Tools App Icon" />

# Colab Tools

**One-click H3 video model deployment, polite GPU queueing, and auto-shutdown money saver for Google Colab on macOS.**

No manual scripts or terminal juggling · Pick **H3 Original** or **H3 Flash** (or any custom weight) and click Start · Smart Google Drive copy & real-time output backup · No babysitting: live queue progress in the menu bar, plus sound & popup notifications when allocated, ready, or stopped · Also switches cleanly to LLM proxy mode for coding tools.

[English](README.md) · [简体中文](README.zh-CN.md) · [Download Latest](https://github.com/LJMStark/Colab-Tools/releases/latest) · [Changelog](CHANGELOG.md) · [Security](SECURITY.md)

[![CI](https://github.com/LJMStark/Colab-Tools/actions/workflows/ci.yml/badge.svg)](https://github.com/LJMStark/Colab-Tools/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/LJMStark/Colab-Tools?color=f59e0b&logo=github)](https://github.com/LJMStark/Colab-Tools/releases/latest)
[![Platform](https://img.shields.io/badge/macOS-arm64-111827?logo=apple&logoColor=white)](https://github.com/LJMStark/Colab-Tools/releases/latest)
[![Go](https://img.shields.io/badge/Go-1.27%20%2B%20MyGo-00ADD8?logo=go&logoColor=white)](https://github.com/egoist/mygo)
[![Colab CLI](https://img.shields.io/badge/google--colab--cli-0.8.x-4285F4)](https://github.com/googlecolab/google-colab-cli)
[![License](https://img.shields.io/badge/License-MIT-10b981)](LICENSE)

<br />

<table>
  <tr>
    <td align="center" colspan="2">
      <img src="docs/images/preview-main-status.png" alt="Colab Tools Desktop Console Status (H3 Live Queue)" width="840" /><br />
      <sub><b>Desktop Console</b> · Live Compute Units, VRAM, GPU load, ComfyUI running/pending queue, saved clip count & one-click ComfyUI launch</sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="50%">
      <img src="docs/images/preview-deploy-h3.png" alt="Zero-Config Beginner Home Launchpad" width="420" /><br />
      <sub><b>One-Click Zero-Config Home</b> · Pre-configured with <b>H3 Flash</b>, smart GPU auto-fallback, Drive backup & 10m post-queue auto-shutdown</sub>
    </td>
    <td align="center" width="50%">
      <img src="docs/images/preview-settings-queue.png" alt="Optional Custom GPU Priority & Morning Schedule" width="420" /><br />
      <sub><b>Optional Power-User Controls</b> · Quietly collapsed by default; expand anytime for eco mode, custom GPU order, fallback & morning schedule</sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="50%">
      <img src="docs/images/preview-onboarding.png" alt="First-Launch Environment Doctor" width="420" /><br />
      <sub><b>Guided Setup</b> · Checks and installs official <code>google-colab-cli</code> in one click</sub>
    </td>
    <td align="center" width="50%">
      <img src="docs/images/preview-dashboard.png" alt="Quiet System-Tray Companion HUD" width="320" /><br />
      <sub><b>Quiet System-Tray Companion</b> · Close the big window and keep live cost, ComfyUI launch & instant stop one click away</sub>
    </td>
  </tr>
</table>

</div>

---

## Why Use Colab Tools? (In Plain Words)

Renting A100 / G4 / H100 GPUs through Google Colab is great value for running video models, until four daily annoyances burn your credits or your evening:

1. **Forgetting to stop an idle GPU burns more credits than actually rendering**
   - Real bill from an 18-clip H3 run: rendering all 18 clips cost only **17 Compute Units**, while accidentally leaving the machine sitting overnight burned **54 Compute Units**.
   - **How Colab Tools helps**: It watches your ComfyUI queue plus GPU+CPU load (so 30 GB model downloads or FFmpeg muxing are never killed early). Once your video queue finishes and sits idle (default 10 min), it **stops the runtime automatically and re-checks Colab servers to confirm billing truly stopped**.
2. **Re-installing ComfyUI and uploading bash scripts on every fresh VM gets old fast**
   - **How Colab Tools helps**: Deployment scripts are built straight into the app and sent to the cloud VM automatically. Pick **H3 Original (31B)** or **H3 Flash (13.7B fast)** out of the box — or expand **More Versions** for 24GB-friendly GGUF, any HuggingFace repo, or models already in your Drive. All variants share the exact same 21.5 GB base weights (text encoder + audio/video VAE).
3. **Symlinking 20GB+ weights straight from Google Drive FUSE causes stalls and disconnects**
   - **How Colab Tools helps**: When Google Drive is enabled, Colab Tools sequentially copies existing base weights and prebuilt acceleration `.whl` wheels onto the VM's fast local NVMe SSD (`rsync -ahW`) before running, downloads missing weights at datacenter speed (`hf_xet` / `hf_transfer`, with optional base backup back to Drive), and **writes every finished video clip straight to Drive `outputs/`** so a 24h timeout or disconnect never wipes your work. You can also turn Drive off for quick cloud-only trials.
4. **Colab tabs drop connections and native port proxy breaks ComfyUI WebSockets**
   - **How Colab Tools helps**: Once ComfyUI starts, Colab Tools opens it in your browser through a **local encrypted SSH tunnel (`127.0.0.1:8188`)** using official `colab ssh --proxy-mode` — no public URL exposed and no WebSocket black screens (an optional `cloudflared` link toggle is included if you want to monitor from another device). Built in pure Go with GPU-rendered UI (`~9 MB` zipped, zero Electron), fast and lightweight on **macOS**.

---

## Also Works Great for Self-Hosted LLM Proxies

Need a cloud GPU to power your local AI coding tools? Switch the recipe to **大模型代理 (LLM Proxy)** in the Deploy tab:
- Auto-detects and safely writes standby configs with backups for **[CC Switch](https://github.com/farion1231/cc-switch)**, **OpenCode** (`opencode.json`), and **Codex CLI** (`config.toml`) without touching your active official subscription or storing plaintext keys;
- One-click terminal launcher for **Claude Code**, plus safe-by-default **OpenAI (`/v1`) & Anthropic** copy templates for Cherry Studio, Cline, Roo Code, and Cursor.

---

## Download & Install

> **Platform focus:** Colab Tools currently focuses on **macOS**. Windows builds have been temporarily unlisted until the macOS experience is fully polished.

### Prerequisites
- **macOS 14.0+** (`arm64` Apple Silicon prebuilt; Intel Mac builds from source)
- **Official Google Colab CLI** (`uv tool install google-colab-cli`, **checked & installable right inside the first-launch wizard**)

### Option 1: Download Prebuilt App (Recommended)
1. Download `Colab-Tools-v0.3.17-macOS-arm64.zip` from [GitHub Releases](https://github.com/LJMStark/Colab-Tools/releases/latest), unzip it, and drag **`Colab Tools.app`** to `/Applications`.
2. Finish the 3-step setup wizard, then on the **Home** tab simply click the top-center **Power button** (pre-configured out of the box with **H3 Flash**, smart GPU auto-fallback, Drive backup, and auto-shutdown).

> **Signature note:** Community builds are self-signed. On first launch, right-click → **Open** (or run `xattr -cr "/Applications/Colab Tools.app"`).

### Option 2: Build from Source (Pure Go, Zero CGO)
```bash
git clone https://github.com/LJMStark/Colab-Tools.git
cd Colab-Tools
GOTOOLCHAIN=auto go test -race ./...
chmod +x scripts/package.sh
./scripts/package.sh --mac --zip --install
```

---

## Security & Official Policy Compliance

- **Strictly Official CLI Execution**: Runtime start/stop, quota checks, SSH tunnels (`colab ssh --proxy-mode`), and browser links all call official `google-colab-cli` commands.
- **System Credential Vault**: Multi-account OAuth2 credentials and keys stay encrypted in macOS Keychain, using `0600` shredded ephemeral files during execution.
- **Polite Queue Guardrails**: Low-frequency Equal Jitter retries (max 5 rounds / 40 min) with immediate 15-minute cooldown on `429` rate limits or `412` assignment caps. Please follow the [Google Colab FAQ & Terms of Service](https://research.google.com/colaboratory/faq.html). See [SECURITY.md](SECURITY.md) for full details.

---

## Community & Contact

If **Colab Tools** saves your Compute Units or streamlines your workflow, consider leaving a ⭐ Star!

- **X (Twitter)**: [@starkljm](https://x.com/starkljm)
- **Contact**: DM [@starkljm](https://x.com/starkljm) on X *(if the WeChat QR expires, DM for a fresh invite)*
- **WeChat Community Group (`Colab Tools 交流群`)**:

<p align="left">
  <img src="assets/wechat-qr.png" width="220" alt="Colab Tools WeChat Group QR Code" />
</p>

---

## License

Released under the [MIT License](LICENSE). Copyright © 2026 [LJMStark](https://github.com/LJMStark).
