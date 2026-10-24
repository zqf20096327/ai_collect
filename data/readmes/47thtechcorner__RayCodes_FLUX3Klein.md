<div align="center">
  <a href="https://youtu.be/lKaRGGc0LxA">
    <img src="https://img.youtube.com/vi/lKaRGGc0LxA/0.jpg" alt="Flux 3 Klein: The #1 Open AI Image Editor That Runs on 4GB VRAM!">
  </a>
  <h3>📺 <a href="https://youtu.be/lKaRGGc0LxA">Watch the full tutorial on YouTube</a></h3>
</div>

# 🎨 FLUX 3 Klein Layout Controller

> Direct scene layout and subject placement using everyday 2–3 sentence English prompts without manual coordinate typing or ControlNet.

FLUX 3 Klein provides a unified 5.6B flow-map architecture that parses spatial bounding box coordinates embedded directly inside user prompts. This controller automatically converts natural spatial phrasing into normalized 0–1000 coordinate grids, locking character and object positions without external guidance models.

## ⚡ 3-Step Workflow

| Step 1: Plain English Input | Step 2: AI Action | Step 3: Result Deliverable |
| :--- | :--- | :--- |
| Describe your scene in 2–3 natural English sentences (e.g. *"subject on the left, props on the right"*) | Auto-detects spatial zones and maps 0–1000 coordinates into 16-step flow latents | Generates composition-locked PNG images directly in `outputs/` |

## 🌟 Key Features

* **Natural English Spatial Parser**: Describe placements in plain language (*"on the left"*, *"across the top header"*, *"on the right"*); the controller automatically generates the exact 0–1000 coordinates.
* **ControlNet-Free Spatial Layout**: Dictate exact subject locations without training or running separate ControlNet pipelines.
* **Unified Flow-Map Architecture**: Single 5.6B checkpoint handles text-to-image synthesis, character consistency, and targeted edits.
* **Multi-Domain Test Suite**: Built-in pipelines for Studio Product Staging, Cyberpunk Street Scenes, and Swiss Architectural Posters.
* **Direct Image Synthesis**: Generates 3 production-grade 1024x1024 PNG images in `outputs/` without bloated auxiliary files.

## 🛠️ Tech Stack

* **Language**: Python 3.10+
* **AI Model Engine**: FLUX 3 Image Klein (Black Forest Labs)
* **Prompt Processing**: Natural English spatial layout extractor
* **Coordinate Engine**: Normalized 0–1000 grid mapper

## 📋 Installation & Setup

1. **Install Dependencies**
   ```powershell
   pip install rich pydantic
   ```

2. **Model Weights (Hugging Face Hub)**
   Download the official FLUX 3 Image Klein model checkpoint for the Diffusers pipeline:
   ```powershell
   hf download black-forest-labs/flux-3-image-klein --local-dir models/flux-3-klein
   ```

## 🚀 Usage & Execution

Execute the natural prompt parser across all 3 test scenes:

```powershell
python main.py
```

Outputs are automatically saved into the `outputs/` directory:
- `outputs/test1_studio_product.png`
- `outputs/test2_cyberpunk_street.png`
- `outputs/test3_architectural_poster.png`

## 📂 File Structure

```text
FLUX 3 Klein/
├── main.py
├── README.md
```

## 💡 Practical Use Cases

1. **E-Commerce Product Staging**: Describe item placement in plain English to maintain consistent catalog layouts.
2. **Graphic Design & Poster Typography**: Tell the model to place text banners *"across the top"* while keeping subject focus below.
3. **Multi-Character Storyboarding**: Place multiple figures in distinct positions (*"one on the left, one on the right"*) without character blending.
4. **Interior Design Layouts**: Specify precise placement of furniture elements in architectural visualizations.
5. **Brand Marketing Visuals**: Guarantee product prominence while allowing dynamic environmental changes.

## 🔮 Future Enhancements

1. **Interactive Canvas Web UI**: Drag-and-drop bounding box creation interface with instant preview.
2. **Direct ComfyUI WebSocket Link**: Auto-queue generated prompt coordinates directly into active ComfyUI nodes.
3. **Multi-Reference Consistency Stacking**: Anchor multiple reference images to specific bounding boxes.
4. **Automatic Box Extraction**: Auto-generate coordinates from uploaded pencil sketches or wireframes.
5. **Video Keyframe Interpolation**: Animate bounding box coordinates across sequential frames for cinematic camera tracking.

---

## 🏷️ Keywords & Search Tags

`flux 3`, `flux 3 klein`, `flux klein`, `black forest labs`, `flux gguf`, `qwen3 vl`, `qwen image`, `comfyui flux`, `local flux`, `flux 5.6b`, `image klein`, `flux sd`, `midjourney alternative`, `photoshop ai`, `stable diffusion`, `sdxl alternative`, `flux 3 tutorial`, `flux 3 download`, `flux 3 local`, `flux 3 setup`, `flux 3 review`, `flux 3 benchmark`, `flux 3 comfyui`, `flux klein comfyui`, `flux 3 image edit`, `inpainting ai`, `4gb vram`, `rtx 3060`, `rtx 4060`, `low vram`
