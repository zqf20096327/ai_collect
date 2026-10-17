<div align="center">

<img width="172" height="203" alt="HOMR GUI" src="figures/gui-screenshot.png" />

# HOMR GUI

**Music Score to MIDI · 乐谱转 MIDI**

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![GUI: PyQt6](https://img.shields.io/badge/GUI-PyQt6-41CD52?logo=qt&logoColor=white)](https://www.qt.io/)
[![Based on HOMR](https://img.shields.io/badge/Based_on-HOMR-8A2BE2)](https://github.com/liebharc/homr)

[English](#english) · [中文](#中文)

</div>

---

<a id="english"></a>

## Overview

**HOMR GUI** is a desktop graphical front-end for [liebharc/homr](https://github.com/liebharc/homr), an end-to-end Optical Music Recognition (OMR) system built on vision transformers. Screenshot or drag in an image of a music score, and it converts it into **MusicXML** and **MIDI** in a single click — no command line required.

## Features

- **Graphical Interface** — a minimalist PyQt6 desktop app; no more command line.
- **One-click conversion** — grab a score region with `Win + Shift + S` or drag & drop an image; the score is recognized automatically and exported as `.musicxml` and `.mid`.
- **CPU / GPU mode switch** — run on CPU (`onnxruntime`) or GPU (`onnxruntime-gpu` + CUDA).
- **China-friendly downloads** — model downloads are proxied through a mirror for faster speeds in mainland China.
- **Drop straight into your DAW** — once converted, simply drag the generated MIDI file into your DAW.

## Installation

HOMR GUI requires **Python 3.11–3.15**.

1. Clone the repository:

   ```bash
   git clone https://github.com/Quackone/homr_gui.git
   cd homr_gui
   ```

2. Install dependencies:

   ```bash
   # CPU mode (recommended for most users)
   pip install -r requirements.txt
   ```

   For GPU acceleration, you also need CUDA, and install `onnxruntime-gpu` in place of `onnxruntime`:

   ```bash
   pip uninstall onnxruntime
   pip install onnxruntime-gpu
   ```

   Alternatively, using Poetry:

   ```bash
   poetry install            # CPU
   poetry install --with gpu # GPU
   ```

## Usage

Launch in GPU mode:

```bash
python homr_gui.py
```

Or in CPU compatibility mode:

```bash
python homr_gui_cpu.py
```

On Windows you can also use the bundled launchers:

- `启动.bat` — normal (GPU) launch
- `CPU兼容模式.bat` — CPU-safe mode for maximum compatibility
- `调试启动.bat` — debug launch with console output

**How to use:**

1. Press `Win + Shift + S` and select the score region, or drag & drop an image onto the window.
2. The AI engine recognizes the score automatically.
3. The results (`.musicxml` and `.mid`) are saved next to the source image.
4. Drag the `.mid` file into your DAW and start editing.

## Acknowledgments

- [liebharc/homr](https://github.com/liebharc/homr) — the upstream OMR engine by [Christian Liebhardt](https://github.com/liebharc).
- GUI by Quackone.

## License

This project is licensed under the [GNU AGPL v3](https://www.gnu.org/licenses/agpl-3.0) license.

---

<a id="中文"></a>

## 简介

**HOMR GUI** 是基于 [liebharc/homr](https://github.com/liebharc/homr) 的桌面图形界面封装与增强版。HOMR 是一个基于视觉 Transformer 的端到端光学乐谱识别（OMR）系统。截图或拖入一张乐谱图片，即可一键转换成 **MusicXML** 和 **MIDI**，无需命令行。

## 功能特性

- **图形界面** —— 基于 PyQt6 的极简桌面应用，告别命令行。
- **一键转换** —— 用 `Win + Shift + S` 框选乐谱区域，或直接拖入图片，自动识别并导出 `.musicxml` 和 `.mid`。
- **CPU / GPU 模式切换** —— 支持 CPU（`onnxruntime`）与 GPU（`onnxruntime-gpu` + CUDA）两种模式。
- **国内下载优化** —— 模型下载走镜像代理，国内下载速度更快。
- **直接拖入 DAW** —— 转换完成后，把生成的 MIDI 文件直接拖进 DAW 即可。

## 安装

HOMR GUI 需要 **Python 3.11–3.15**。

1. 克隆仓库：

   ```bash
   git clone https://github.com/Quackone/homr_gui.git
   cd homr_gui
   ```

2. 安装依赖：

   ```bash
   # CPU 模式（推荐大多数用户使用）
   pip install -r requirements.txt
   ```

   如需 GPU 加速，还需要 CUDA，并用 `onnxruntime-gpu` 替换 `onnxruntime`：

   ```bash
   pip uninstall onnxruntime
   pip install onnxruntime-gpu
   ```

   或使用 Poetry：

   ```bash
   poetry install            # CPU
   poetry install --with gpu # GPU
   ```

## 使用

以 GPU 模式启动：

```bash
python homr_gui.py
```

或以 CPU 兼容模式启动：

```bash
python homr_gui_cpu.py
```

在 Windows 上也可以直接双击自带的启动脚本：

- `启动.bat` —— 常规（GPU）启动
- `CPU兼容模式.bat` —— CPU 安全模式，兼容性最好
- `调试启动.bat` —— 调试启动，带控制台输出

**使用方法：**

1. 按 `Win + Shift + S` 框选乐谱区域，或将图片拖入窗口。
2. AI 引擎自动识别乐谱。
3. 识别结果（`.musicxml` 和 `.mid`）会保存在原图片旁边。
4. 把 `.mid` 文件拖进 DAW 即可开始编辑。

## 致谢

- [liebharc/homr](https://github.com/liebharc/homr) —— 上游 OMR 引擎，作者 [Christian Liebhardt](https://github.com/liebharc)。
- GUI 作者：Quackone。

## 开源协议

本项目遵循 [GNU AGPL v3](https://www.gnu.org/licenses/agpl-3.0) 协议。
