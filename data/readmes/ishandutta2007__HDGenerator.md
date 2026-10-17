# HD Video Generator 🚀 — AI Video Upscaler & Super-Resolution CLI

<p align="center">
  <img src="assets/banner.svg" alt="HD Video Generator Banner" width="100%" />
</p>

<p align="center">
  <a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a>
  <a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" /></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg" alt="Python Version" /></a>
  <a href="https://onnxruntime.ai/"><img src="https://img.shields.io/badge/Inference-ONNX%20Runtime-green.svg" alt="ONNX Runtime" /></a>
  <a href="https://github.com/xinntao/Real-ESRGAN"><img src="https://img.shields.io/badge/AI%20Model-Real--ESRGAN-orange.svg" alt="Model" /></a>
  <a href="https://github.com/ishandutta2007/HDGenerator/pulls"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome" /></a>
  <a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>
</p>

> 🌟 **HD Video Generator** is an open-source, lightweight, and high-performance command-line (CLI) tool to upscale Standard Definition (SD) videos to High Definition (HD/4K) using state-of-the-art **Real-ESRGAN** deep learning super-resolution models with **ONNX Runtime** and **OpenCV**.

---

## 📌 Table of Contents 📑

- [📖 Overview](#-overview-)
- [✨ Key Features](#-key-features-)
- [🏷️ Keywords & Tags](#️-keywords--tags-)
- [📋 Prerequisites](#-prerequisites-)
- [⚙️ Setup & Installation](#️-setup--installation-)
- [🧠 Model Download](#-model-download-)
- [📁 Project Structure](#-project-structure-)
- [🚀 Usage & CLI Examples](#-usage--cli-examples-)
- [🎬 Supported Formats & Capabilities](#-supported-formats--capabilities-)
- [❓ Troubleshooting & FAQ](#-troubleshooting--faq-)
- [🤝 Contributing](#-contributing-)
- [⭐ Star History](#-star-history-)
- [📄 License](#-license-)

---

## 📖 Overview 🔍

Are your vintage home videos, old animations, or low-resolution clips blurry and pixelated? 📽️ **HD Video Generator** uses cutting-edge artificial intelligence and computer vision to restore, enhance, and upscale video frames to crystal-clear high definition. Powered by the optimized `RealESR_Gx4_fp16` ONNX model, it delivers 4x spatial resolution improvements with sharp edges, rich colors, and reduced compression artifacts. 🎨✨

---

## ✨ Key Features 💡

* 🤖 **AI-Powered 4x Video Upscaling:** Harnesses the deep learning power of Real-ESRGAN (`RealESR_Gx4_fp16`) to reconstruct fine textures and realistic details.
* ⚡ **High-Performance ONNX Inference:** Utilizes `onnxruntime` for blazing-fast, cross-platform, hardware-accelerated model execution.
* 🎥 **Robust Frame Processing:** Leverages `opencv-python` for accurate frame-by-frame decoding, high-quality transformation, and seamless re-encoding.
* 💻 **Intuitive CLI Interface:** Simple, developer-friendly command-line options with smart default output handling.
* 🔒 **100% Local & Privacy-Friendly:** All video processing runs locally on your machine—no cloud uploads, subscriptions, or API rate limits! 🛡️
* 📦 **Lightweight & Extensible:** Minimal dependencies and modular code structure for easy customization and pipeline integration. 🧩

---

## 🏷️ Keywords / Tags 🔖

`video-upscaling` · `real-esrgan` · `super-resolution` · `ai-video-enhancer` · `onnxruntime` · `opencv` · `python` · `sd-to-hd` · `video-enhancement` · `deep-learning` · `computer-vision` · `image-restoration` · `video-processing`

---

## 📋 Prerequisites 🛠️

* 🐍 **Python:** Version 3.8 or higher
* 🐙 **Git:** For cloning the repository
* 💻 **OS:** Windows, macOS, or Linux

---

## ⚙️ Setup & Installation 🚀

### 1. 📥 Clone the Repository
```bash
git clone https://github.com/ishandutta2007/HDGenerator.git
cd HDGenerator
```

### 2. 🌐 Create and Activate a Virtual Environment

* **Windows (PowerShell / Command Prompt):** 🪟
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  ```

* **macOS / Linux:** 🍎🐧
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🧠 Model Download 💾

This project requires the **Real-ESRGAN ONNX** model weights (`RealESR_Gx4_fp16.onnx`):

1. 📥 Download `RealESR_Gx4_fp16.onnx` directly from the [ONNX Model Zoo on Hugging Face (ai-forever/Real-ESRGAN)](https://huggingface.co/ai-forever/Real-ESRGAN/tree/main/weights).
2. 📁 Create a `models/` directory in the project root (if not already present):
   ```bash
   mkdir models
   ```
3. 💾 Place `RealESR_Gx4_fp16.onnx` inside the `models/` folder.

---

## 📁 Project Structure 🗂️

```text
HDGenerator/
├── assets/
│   ├── banner.svg              # Dynamic SVG header banner
│   └── social-preview.gif      # Social preview animated GIF (640x320)
├── models/
│   └── RealESR_Gx4_fp16.onnx   # ONNX super-resolution model weights
├── src/
│   ├── main.py                 # CLI entry point & argument parser
│   └── upscaler.py             # Video decoding, inference, & encoding pipeline
├── videos/
│   └── sample.mp4              # Sample input / demo video
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🚀 Usage & CLI Examples 🎬

Run the pipeline from the project root directory using Python:

### 🌟 Basic Upscaling
Upscale a video using default output naming (`<original_name>_upscaled.mp4`):
```bash
python src/main.py --input "videos/sample.mp4"
```

### 🎯 Custom Output Destination
Specify an exact path for the enhanced video output:
```bash
python src/main.py --input "videos/sample.mp4" --output "videos/sample_4k_enhanced.mp4"
```

### 🧠 Custom Model Path
Specify a different ONNX model variant if needed:
```bash
python src/main.py --input "videos/sample.mp4" --model_path "models/RealESR_Gx4_fp16.onnx"
```

### 🎛️ CLI Command Options

| Argument | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `--input` | `str` | *(Required)* | Filepath to the input SD video to upscale. |
| `--output` | `str` | `<input_dir>/<name>_upscaled.mp4` | Destination filepath for the upscaled HD video. |
| `--model_path` | `str` | `models/RealESR_Gx4_fp16.onnx` | Filepath to the `.onnx` super-resolution model. |

---

## 🎬 Supported Formats & Capabilities 🎞️

- 📹 **Input Formats:** MP4, AVI, MOV, MKV, and other standard formats supported by OpenCV.
- 📐 **Upscaling Factor:** 4x spatial scaling (e.g., 480p SD $\rightarrow$ 1080p/4K HD).
- 🚀 **Execution Providers:** CPU and GPU (CUDA/DirectML) inference via `onnxruntime` / `onnxruntime-gpu`.

---

## ❓ Troubleshooting & FAQ 💡

<details>
<summary><b>⚡ Q: How do I enable GPU acceleration with ONNX Runtime?</b></summary>
<br/>
To use NVIDIA CUDA acceleration, install <code>onnxruntime-gpu</code> instead of standard <code>onnxruntime</code>:

```bash
pip uninstall onnxruntime
pip install onnxruntime-gpu
```
Ensure compatible CUDA and cuDNN libraries are configured on your system.
</details>

<details>
<summary><b>📦 Q: Where can I find more Real-ESRGAN ONNX weights?</b></summary>
<br/>
Alternative checkpoints and specialized anime/photo enhancement models can be downloaded from Hugging Face or converted from PyTorch weights to ONNX format.
</details>

---

## 🤝 Contributing 🌟

Contributions, issues, and feature requests are welcome! 💖

1. 🍴 Fork the repository
2. 🌿 Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'feat: Add AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🚀 Open a Pull Request

---

## ⭐ Star History

[![Star History Chart](https://star-history.dera.page/svg?repos=ishandutta2007/HDGenerator&type=date&legend=top-left)](https://star-history.dera.page/#ishandutta2007/HDGenerator&type=date&legend=top-left)

---

## 📄 License 📜

Distributed under the **MIT License**. See `LICENSE` for more information. ⚖️