<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/iishong0w0/Axiom-AI-Aimbot?style=social)](https://github.com/iishong0w0/Axiom-AI-Aimbot/stargazers)
![Version](https://img.shields.io/badge/Version-6.2-green.svg)
![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![License](https://img.shields.io/badge/License-PolyForm--Noncommercial%201.0.0-blueviolet.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/iishong0w0/Axiom-AI-Aimbot)
![Repo Size](https://img.shields.io/github/repo-size/iishong0w0/Axiom-AI-Aimbot)

<img src="src/gui/assets/logo.png" alt="Axiom logo" width="120">

<h1>Axiom AI</h1>
<p>Windows computer-vision aim assistance built with Python, PyQt6, ONNX Runtime, and native acceleration.</p>

## <a href="https://github.com/iishong0w0/Axiom-AI-Aimbot/releases/latest"><strong>Download Latest Release</strong></a>
## <a href="https://discord.gg/h4dEh3b8Bt">Discord</a>

<p><strong>If this project helps you, please give us a Star.</strong></p>

</div>

## Overview

Axiom AI is a real-time computer-vision desktop application for screen capture, object detection, overlay rendering, and configurable input automation. The app uses a PyQt6 + QFluentWidgets interface, ONNX Runtime inference, optional Rust acceleration for hot paths, and Windows input backends for mouse, hardware controllers, and virtual gamepad workflows.

Before using Axiom, read [Disclaimer.md](Disclaimer.md). This software can violate game, platform, or competition rules depending on where and how it is used. You are responsible for complying with local law and third-party terms.

## Current Capabilities

- **Aim control**
  - PID tuning with separate X/Y axis parameters.
  - Optional Y-axis reduction delay.
  - Bezier curve smoothing.
  - Smart tracker prediction with smoothing, prediction time, stop threshold, and prediction overlay.
  - Single-target mode.
  - Adjustable FOV, independent detection range, confidence threshold, and capture/detection intervals.
  - Aim target selection: head, body, or both in the UI.

- **Auto fire**
  - Key-activated or always-on auto fire.
  - Adjustable scope delay and fire interval.
  - Head/body/both hit-zone checks.
  - Separate primary and secondary auto-fire bindings.

- **Capture and display**
  - `dxcam` and `mss` capture backends.
  - Transparent overlay mode for FOV, boxes, confidence, and status panel.
  - Window display mode for a framed visual preview.
  - Configurable status-panel rows and visual scale.

- **Compute backends**
  - ONNX Runtime backend selection for DirectML, CUDA, TensorRT, and ROCm.
  - Setup Wizard can install or remove the matching ONNX Runtime wheel.
  - GPU device selection is exposed in the UI where supported.
  - CPU fallback is intentionally not automatic; the selected provider must be installed and available.

- **Input methods**
  - `mouse_event`
  - `sendinput`
  - `ddxoft`
  - Arduino HID mouse
  - Arduino controller bridge
  - MAKCU
  - Virtual Xbox controller

- **Configuration and localization**
  - Root `config.json` stores the active application settings.
  - Named presets are managed through the Configs page and stored under `src/config/`.
  - Language packs live in `src/language_data/`.
  - Supported UI languages include English, Chinese, Japanese, Korean, German, French, Spanish, Portuguese, Russian, and Hindi.

## Models

Axiom loads ONNX detection models from the runtime `models/` directory at the project root. The first-run wizard and Model page can fetch available `.onnx` files from the configured GitLab model catalog:

```text
iis20160512/axiom-ai-aimbot-models
```

You can also add your own `.onnx` model through the Model page. The active model path is saved in `config.json`.

## System Requirements

### Minimum

- Windows 10/11 64-bit
- Python 3.11 runtime, or the bundled `src/python/python.exe` release runtime
- Microsoft Visual C++ Redistributable for native dependencies
- A GPU/runtime combination supported by one of the installed ONNX Runtime providers

### Recommended

- Windows 11 64-bit
- NVIDIA GPU for CUDA or TensorRT, or any suitable DirectX 12 GPU for DirectML
- 16 GB RAM or more
- A downloaded ONNX model in `models/`

## Quick Start

1. Run `啟動Launcher.bat`.
   - The launcher requests administrator privileges.
   - It checks for the Visual C++ Redistributable and starts `src\python\python.exe src\main.py`.

2. Accept the disclaimer.

3. Complete the Setup Wizard.
   - Choose language, theme, acrylic settings, compute backend, and starter model.
   - If the wizard installs a compute runtime, Axiom saves the config and restarts so the new runtime can be loaded cleanly.

4. Open the settings window.
   - **Aim**: FOV, detection range, intervals, confidence, PID, Bezier, tracker, and screenshot method.
   - **Trigger**: auto-fire mode, target part, delay, interval, and hit-zone ratios.
   - **Keys**: aim keys, toggle key, and auto-fire keys.
   - **Input Actions**: mouse movement/click backend, COM ports, hardware tools, and Xbox settings.
   - **Model**: select, add, delete, download, or open the model folder.
   - **Visuals**: overlay/window display, FOV/box/status visibility, console visibility, and acrylic opacity.
   - **Configs**: create, save, load, rename, import, export, or delete named presets.
   - **Other**: compute backend, GPU device, installed runtimes, update check, language, and reset.

5. Use the configured keys.
   - Default aim keys include mouse left, mouse X2, and mouse right.
   - Default toggle key is `Insert`.
   - Detection starts automatically when a model is configured and runtime initialization succeeds.

## Running Without the Launcher

Release bundle:

```powershell
src\python\python.exe src\main.py
```

Development environment:

```powershell
python src\main.py
```

The development command requires equivalent Python packages and native dependencies to be installed in your environment.

## Project Structure

```text
Axiom/
├── 啟動Launcher.bat              # Windows launcher
├── config.json                   # Runtime-created active settings file
├── models/                       # Runtime-created/downloaded ONNX model folder
├── src/
│   ├── main.py                   # Current application entry point
│   ├── launch_fluent.py          # Legacy startup path
│   ├── version.py                # Version constant
│   ├── bootstrap/                # Runtime preparation and onboarding
│   ├── core/                     # Detection, config, runtime, model, and backend logic
│   ├── gui/                      # Overlay, status panel, visual window, and Fluent UI
│   ├── language_data/            # Translation JSON files
│   ├── python/                   # Bundled Python runtime in release bundles
│   ├── rust/axiom_rust_accel/    # Rust native acceleration module
│   ├── vendor/                   # Native/vendor binaries
│   └── win_utils/                # Windows input, controller, and admin helpers
└── src/docs/
    ├── README.md
    ├── Disclaimer.md
    └── LICENSE.txt
```

## Notes for Maintainers

- `src/main.py` is the current startup path. Prefer it over `src/launch_fluent.py`.
- The selected ONNX provider is explicit. Do not document automatic CPU fallback unless the runtime logic changes.
- The `models/` and root `config.json` paths are runtime data paths and may not exist in a clean source tree.
- Named presets are stored separately from the active config and should be treated as user data.
- The bundled Python runtime, Rust target files, and downloaded models are release/runtime artifacts rather than source modules.

## License

This project is licensed under the **PolyForm Noncommercial License 1.0.0**.

- **No commercial use**: commercial use is prohibited.
- **Personal, educational, and research use**: allowed within the license terms.
- **Modification and distribution**: allowed only as permitted by the license.
- **Attribution and notices**: keep the original license and copyright notices.

For details, see [LICENSE.txt](LICENSE.txt) and [Disclaimer.md](Disclaimer.md).

## Contact

- Discord: [Join the community](https://discord.gg/h4dEh3b8Bt)
- GitHub: [iishong0w0](https://github.com/iishong0w0)
- Email: iis20160512@gmail.com

---

**Disclaimer**: This software is provided "as is" without warranty. Use it at your own risk. See [Disclaimer.md](Disclaimer.md) for the full terms and risk disclosure.

**Copyright © 2025-2026 iisHong0w0. All rights reserved.**
