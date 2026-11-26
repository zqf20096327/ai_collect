<div align="center">

<img src="assets/AppIcon.png" width="120" height="120" alt="Colab Tools App Icon" />

# Colab Tools

**One-click H3 video model deployment, polite GPU queueing, and auto-shutdown money saver for Google Colab (macOS & Windows).**

No manual scripts or terminal juggling · Pick **H3 Original** or **H3 Flash** (or any custom weight) and click Start · Smart Google Drive copy & real-time output backup · Also switches cleanly to LLM proxy mode for coding tools.

[English](README.md) · [简体中文](README.zh-CN.md) · [Download Latest](https://github.com/LJMStark/Colab-Tools/releases/latest) · [Changelog](CHANGELOG.md) · [Security](SECURITY.md)

[![CI](https://github.com/LJMStark/Colab-Tools/actions/workflows/ci.yml/badge.svg)](https://github.com/LJMStark/Colab-Tools/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/LJMStark/Colab-Tools?color=f59e0b&logo=github)](https://github.com/LJMStark/Colab-Tools/releases/latest)
[![Platforms](https://img.shields.io/badge/macOS%20%7C%20Windows-arm64%20%2F%20amd64-111827)](https://github.com/LJMStark/Colab-Tools/releases/latest)
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
      <img src="docs/images/preview-deploy-h3.png" alt="One-Click H3 Original & Flash Deployment" width="420" /><br />
      <sub><b>Zero-Hands H3 Deployment</b> · Choose <b>H3 Original (31B)</b>, <b>H3 Flash (13.7B)</b>, GGUF, or custom HuggingFace / Drive weights — all sharing one 21.5 GB base</sub>
    </td>
    <td align="center" width="50%">
      <img src="docs/images/preview-settings-queue.png" alt="Polite GPU Queue & Off-Peak Schedule" width="420" /><br />
      <sub><b>Polite GPU Queue & Morning Schedule</b> · Pick your priority GPUs, set a fallback card, or wake up to an already-grabbed A100/G4</sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="50%">
      <img src="docs/images/preview-onboarding.png" alt="First-Launch Environment Doctor" width="420" /><br />
      <sub><b>Guided Setup</b> · Checks and installs official <code>google-colab-cli</code> in one click; automatically bridges WSL2 on Windows</sub>
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
4. **Colab tabs drop connections, native port proxy breaks ComfyUI WebSockets, and Windows lacks native CLI support**
   - **How Colab Tools helps**: Once ComfyUI starts, Colab Tools opens it in your browser through a **local encrypted SSH tunnel (`127.0.0.1:8188`)** using official `colab ssh --proxy-mode` — no public URL exposed and no WebSocket black screens (an optional `cloudflared` link toggle is included if you want to monitor from another device). Built in pure Go with GPU-rendered UI (`~8.5 MB` zipped, zero Electron), it runs natively on **macOS** and **Windows** (automatically bridging WSL2 on Windows until native Windows CLI lands).

---

## Also Works Great for Self-Hosted LLM Proxies

Need a cloud GPU to power your local AI coding tools? Switch the recipe to **大模型代理 (LLM Proxy)** in the Deploy tab:
- Auto-detects and safely writes standby configs with backups for **[CC Switch](https://github.com/farion1231/cc-switch)**, **OpenCode** (`opencode.json`), and **Codex CLI** (`config.toml`) without touching your active official subscription or storing plaintext keys;
- One-click terminal launcher for **Claude Code**, plus safe-by-default **OpenAI (`/v1`) & Anthropic** copy templates for Cherry Studio, Cline, Roo Code, and Cursor.

---

## Download & Install

### Prerequisites
- **macOS 14.0+** (`arm64` prebuilt; Intel builds from source) or **Windows 10/11 (`x64`)**
- **Official Google Colab CLI** (**checked & installable right inside the first-launch wizard**):
  - **macOS**: `uv tool install google-colab-cli`
  - **Windows**: Colab Tools prefers native `colab.exe` if present and automatically bridges `google-colab-cli` inside **WSL2** otherwise.

### Option 1: Download Prebuilt App (Recommended)
1. Grab the archive for your OS from [GitHub Releases](https://github.com/LJMStark/Colab-Tools/releases/latest):
   - **macOS (Apple Silicon)**: `Colab-Tools-v0.3.8-macOS-arm64.zip` → unzip and drag **`Colab Tools.app`** to `/Applications`.
   - **Windows (x64)**: `Colab-Tools-v0.3.8-Windows-amd64.zip` → unzip and run **`Colab Tools.exe`**.
2. Finish the 3-step setup wizard, open the **Deploy** tab, pick **H3 Original** or **H3 Flash**, and click **Start & Deploy**.

> **Signature notes:** Community builds are self-signed. On macOS, right-click → **Open** (or `xattr -cr "/Applications/Colab Tools.app"`). On Windows SmartScreen, click **More info → Run anyway**.

### Option 2: Build from Source (Pure Go, Zero CGO)
```bash
git clone https://github.com/LJMStark/Colab-Tools.git
cd Colab-Tools
GOTOOLCHAIN=auto go test -race ./...
chmod +x scripts/package.sh
./scripts/package.sh --all --zip --install
```

Windows PowerShell:
```powershell
$env:GOTOOLCHAIN = "auto"
$env:CGO_ENABLED = "0"
$env:GOFLAGS = "-trimpath"
go test ./...
go tool mygo build -platform windows/amd64 -skip-installer -o build/win .
```

---

## Security & Official Policy Compliance

- **Strictly Official CLI Execution**: Runtime start/stop, quota checks, SSH tunnels (`colab ssh --proxy-mode`), and browser links all call official `google-colab-cli` commands.
- **System Credential Vault**: Multi-account OAuth2 credentials and keys stay encrypted in macOS Keychain / Windows Credential Manager, using `0600` shredded ephemeral files during execution.
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
