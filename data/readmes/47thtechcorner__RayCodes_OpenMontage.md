<div align="center">
  <a href="https://youtu.be/FyM-0sJYIR8">
    <img src="https://img.youtube.com/vi/FyM-0sJYIR8/0.jpg" alt="OpenMontage: The World's First 100% Free Local AI Video Production System">
  </a>
  <h3>📺 <a href="https://youtu.be/FyM-0sJYIR8">Watch the full tutorial on YouTube</a></h3>
</div>

# OpenMontage: The World's First 100% Free Local AI Video Production System

**Automated Local Video Editing and Generation Pipeline powered by Ollama and FFmpeg.**

---

## ⚡ Overview

OpenMontage is a professional, open-source local video production system. It combines local LLM reasoning with advanced timeline rendering to automate the video creation process. By integrating local multimodal AI models (such as `gemma4:e2b`) and the advanced web-based **HyperFrames** timeline engine, OpenMontage can script, edit, grade, and overlay cinematic visual elements on raw video footage without external API dependencies.

---

## 🧠 Technical Highlights

- **🧠 Local Multi-Modal Intelligence**: Auto-detects and leverages Ollama models (`gemma4:e2b`) to build production plans and scene layouts directly on your machine.
- **🎨 Advanced HyperFrames Composition**: Uses standard HTML, CSS, and GSAP (GreenSock Animation Platform) to render cinematic text cards, subtitles, and interactive graphic overlays (like lane vectors and object-tracking boxes).
- **⚙️ Cinematic FFmpeg Grading**: Automatically trims, rescales, color-grades, and applies professional vignette and contrast filters to input footage.
- **🔌 Minimalist Clean Codebase**: Designed with a simple interface separating the core orchestration engine into clean modules under `< 100 lines` of code.

---

## 🚀 Quick Start Installation

Follow these steps to set up and run OpenMontage locally.

### 1️⃣ Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/RayCodes/RayCodes_OpenMontage.git
cd RayCodes_OpenMontage
```

### 2️⃣ Prerequisites
Ensure your system has the following core runtimes installed:
- **🐍 Python 3.10+** (verify with `python --version`)
- **🟢 Node.js >= 22** (required for HyperFrames local composition rendering)
- **🎬 FFmpeg** (must be accessible from your system PATH)
- **🦙 Ollama** (local LLM runner)

### 3️⃣ Setup Reference Video
Since large video files are excluded from git, you must provide your own raw reference video file:
- Place any sample `.mp4` video (e.g. 5 to 15 seconds) in the root directory.
- Rename the file to `reference_video.mp4`.

### 4️⃣ Download Local Model
Open your terminal and pull the default multimodal model:
```bash
ollama pull gemma4:e2b
```

### 5️⃣ Install Python Packages
From the root directory, install all required Python libraries:
```bash
pip install -r requirements.txt
```

### 6️⃣ Ensure Browser Shell
The HyperFrames composition engine requires Chrome Headless Shell to capture and render HTML timelines into video frames. Install it by running:
```bash
npx hyperframes browser ensure
```

---

## 🛠️ Running the Video Generation Pipeline

OpenMontage includes a built-in user dashboard for interactive creation.

### 1️⃣ Launch the Dashboard
Run the Streamlit web application:
```bash
streamlit run app.py
```

### 2️⃣ Generate Your Video
1. Open the browser to the local URL (usually `http://localhost:8501`).
2. Select your local Ollama model in the sidebar.
3. Enter your video concept or prompt (e.g., `Neural Navigator`).
4. Click **Generate Video**.

The pipeline will:
- Parse your prompt and generate/load the structured `production_plan.json`.
- Automatically stage the reference video and create a dedicated workspace under `projects/`.
- Inject a custom kinetic HTML composition with animated lane vectors and car detection boxes.
- Call the HyperFrames compiler to render the final composition to `sample_output/concept_demo.mp4`.

---

## 📂 Workspace Directory Structure

```text
├── openmontage_engine/   # Complete core engine containing tools, schemas, and templates
├── sample_output/        # Stores generated production plans and final MP4 renders
│   └── production_plan.json
├── app.py                # Dashboard user interface (Streamlit)
├── pipeline.py           # Core orchestration pipeline
├── requirements.txt      # Python dependencies
├── .gitignore            # Git ignore file
└── README.md             # Project documentation
```

---

## 🏷️ Keywords & SEO Metadata

`Ollama` `FFmpeg` `Local AI Video` `AI Video Editor` `HyperFrames` `GSAP Video Rendering` `Python Video Pipeline` `Streamlit Video Generator` `Autonomous Video Production` `Local Multimodal AI` `Gemma 4` `Chrome Headless Shell Rendering`
