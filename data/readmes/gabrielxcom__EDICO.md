# EDICO | Eliz & Delia's Image Captioner and Organizer

![Project Image](https://gabrielx.com/wp-content/uploads/2026/09/EDICO-1.jpg)

**A local, browser-based tool for building character LoRA training datasets with AI-generated captions.**

EDICO turns a folder of character images into a clean, captioned training dataset — no command-line juggling, no manual caption typing. A single PowerShell script launches a polished web app where you:

1. Set up a project (vision model, trigger word, character identity)
2. Drop in your images
3. Define a structured caption vocabulary
4. Run an AI captioning pipeline with live progress
5. Review, edit, rearrange, and export in a visual organizer

Everything runs **locally on your machine**. Your images never leave your computer.

For more documentation, guides and more software go to:
**[gabrielx.com/open-source-mit-ai-tools](https://gabrielx.com/open-source-mit-ai-tools/)**

---

## ✨ Features

- **Unified web experience** — the entire workflow lives in one browser app (no terminal wizards)
- **Ollama-powered captioning** — works with any vision model (Llava, Qwen-VL, Gemma, etc.)
- **Structured captions** — consistent, tag-based captions instead of messy free text
- **Custom vocabulary** — define exactly what the AI describes (pose, expression, framing, lighting...)
- **Live pipeline progress** — thumbnail grid with per-image status, resume & retry
- **Visual organizer** — filter by any attribute, multi-select or single-select modes
- **Structured image editor** — pick terms per category (no raw text editing)
- **Rearrange & auto-arrange** — drag to order, or auto-sort by priorities before re-sequencing
- **Duplicate & resolution badges** — spot potential duplicates and non-standard image sizes instantly
- **Dark/light theme** — follows your system preference
- **100% local & offline** — after model download, no internet needed

---

## 📋 Requirements

| Requirement | Notes |
|-------------|-------|
| **Windows** | PowerShell 5.1+ (Windows PowerShell or PowerShell 7+) |
| **[Ollama](https://ollama.com/download)** | Must be installed and running |
| **A vision model** | Pull one first: `ollama pull huihui_ai/qwen3-vl-abliterated:8b-instruct` (recommended) |
| **Images** | `.png`, `.jpg`, `.jpeg`, or `.webp` |

> ⚠️ **No Python, no Node, no pip installs.** Just PowerShell + Ollama.

---

## 🚀 Quick Start

1. **Download** this repository (or just `dataset_tool.ps1` + `start.bat`)
2. **Install Ollama** from [ollama.com](https://ollama.com/download) and start it
3. **Pull a vision model** (see below)
4. **Double-click `start.bat`**
5. Your browser opens EDICO — create a project and follow the steps

---

### Recommended vision models

```bash
# Qwen3 VL (recommended — excellent captioning quality)
ollama pull huihui_ai/qwen3-vl-abliterated:8b-instruct

# Alternative: Qwen2.5 VL
ollama pull huihui_ai/qwen2.5-vl-abliterated:7b

# Alternative: LLaVA
ollama pull llava

```

--- 

### Want to support more Open-Source projects? 🤖
*All you need to do is:*
## 🎵 Listen to our songs!
### Visit [I am Eliz Ai .com](https://www.iamelizai.com) 🎵 
We are on YouTube Music, Spotify and Apple Music
