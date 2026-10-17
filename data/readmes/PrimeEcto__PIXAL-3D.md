<p align="center">
  <img src="banner.png" alt="Pixal3D Studio — one-click image to 3D for Pinokio" width="880">
</p>

# Pixal3D Studio — one-click image → 3D for Pinokio

Turn a single reference image into a fully textured 3D model (GLB) and orbit it right in your browser. A [Pinokio](https://pinokio.computer) launcher that wraps [Pixal3D](https://github.com/TencentARC/Pixal3D) (Tencent ARC, SIGGRAPH 2026) in a clean, focused studio UI — **no node graphs, no clutter**. Drop an image, pick a quality, press Generate.

Built on:

- **[Pixal3D](https://github.com/TencentARC/Pixal3D)** — pixel-aligned image-to-3D generation with detailed geometry and PBR textures
- **[ComfyUI](https://github.com/comfy-org/comfyui)** — the API backend
- **[Pixal3D-ComfyUI](https://github.com/Saganaki22/Pixal3D-ComfyUI)** — community ComfyUI integration that carries the model loader and low-VRAM machinery

## Install (Pinokio, 1 click)

1. Open Pinokio → **Discover** / paste this URL, or from any Pinokio terminal:
   ```
   pterm download https://github.com/PrimeEcto/PIXAL-3D
   ```
   (or drop the cloned folder into `PINOKIO_HOME/api/PIXAL-3D`)
2. Click **Install** — clones both repos, builds the venv, compiles the CUDA extensions, and verifies the stack (~30–60 min first time; install never `git pull`s an existing checkout — use **Update** for that)
3. Click **Start** — the Studio opens at the server root. Selecting the app does **not** auto-start it.
4. Upload an image → choose **Draft / High / Ultra** → **Generate 3D model** → download the GLB

First launch downloads ~43 GB of weights (Pixal3D cascade + DINOv3 encoder + MoGe camera estimator + BiRefNet background remover); every launch after that is local. The weights load lazily on your first Generate (~2 min).

## Hardware profile

Designed and tested on an **RTX 4070 SUPER (12 GB VRAM / 32 GB RAM)**:

- **VRAM mode: `native_low_vram`** — every model stage stays in system RAM and streams to the GPU one stage at a time
- Measured peak during generation: **~6.8 GB VRAM** (draft preset)
- Full three-stage cascade (sparse structure → shape → PBR texture) in ~6–8 minutes at high/draft presets
- Requirements: **NVIDIA GPU (8–12 GB VRAM), 32 GB+ RAM, ~60 GB free disk.** Linux builds the CUDA extensions from source; for Windows see the prebuilt-wheel notes under `comfyui/custom_nodes/Pixal3D-ComfyUI/docs/` after install.

| Tier (auto-detected) | Hardware | Behavior |
|---|---|---|
| `enthusiast` | ≥24 GB VRAM | max detail, upstream NAF |
| `mainstream` | 10–24 GB VRAM | fast path, texture upsampler capped to avoid OOM |
| `compact` | 6–10 GB VRAM | textures ≤2048, low-VRAM staging |
| `minimal` | <6 GB VRAM | textures ≤1024, most frugal path |
| `cpu` | no CUDA | generation unsupported |

## Smooth 3D viewport (GPU)

The viewport is browser-rendered WebGL — it's fast only if the browser window has GPU access. Pinokio's in-app webview runs with GPU compositing disabled, so the viewport may software-render there (the top bar shows a red `SOFTWARE RENDER` badge when it detects this). For full-speed orbiting:

- Click **View in Browser (GPU viewport)** in the sidebar — same studio, opened in your system browser, which uses the real GPU
- Or click the badge's **retry** button first; if it stays red, restart the app window

Generation itself always runs on CUDA — the System panel shows the detected GPU, live GPU/VRAM meters, and the active tier.

## The UI

| Setting | What it does |
|---|---|
| **Reference image** | The input photo/render. Background is removed automatically (BiRefNet) |
| **Quality** | Draft (1024-cascade, 2K textures, fastest) · High (1024-cascade, 4K) · Ultra (1536-cascade, 4K) |
| **Seed** | Reproducibility. Same seed + same image = same model. Leave empty (or `0`) for automatic — the used seed is shown in the result bar |
| **Render modes** | Wire / Clay / Shaded / Rendered — Blender-style viewport views |

Everything else — camera estimation (MoGe), FOV, mesh decimation, remeshing, PBR texture baking — is handled automatically.

## REST API

The studio exposes a small purpose-built API on the ComfyUI server (Pinokio assigns the port automatically; substitute your app's URL).

| Method | Route | Purpose |
|---|---|---|
| `GET` | `/pixal_studio/config` | Server info: VRAM mode, GPU name, quality presets, `model_loaded` flag |
| `GET` | `/pixal_studio/metrics` | Live telemetry: CPU, RAM, GPU util, VRAM |
| `POST` | `/pixal_studio/upload` | Multipart image upload → `{image_id, preview}` |
| `POST` | `/pixal_studio/generate` | Start a job: `{image_id, quality, seed}` → `{job_id}` |
| `GET` | `/pixal_studio/status` | `{stage, progress, eta, done, error, cancelled, model_loaded, model_url}` |
| `POST` | `/pixal_studio/cancel` | Abort the running job (weights stay resident for the next run) |
| `GET` | `/pixal_studio/model/{id}.glb` | Download the generated GLB |

### Curl

```bash
BASE=http://127.0.0.1:<PORT>

# 1. upload a reference image
IMAGE_ID=$(curl -s -F "image=@my_figure.png" $BASE/pixal_studio/upload | jq -r .image_id)

# 2. start generation (quality: draft | high | ultra)
curl -s -X POST $BASE/pixal_studio/generate \
  -H "Content-Type: application/json" \
  -d "{\"image_id\":\"$IMAGE_ID\",\"quality\":\"high\",\"seed\":42}"

# 3. poll until done:true
curl -s $BASE/pixal_studio/status

# 4. download the GLB
curl -s -O $BASE/pixal_studio/model/<id>.glb
```

### Python

```python
import time, requests

BASE = "http://127.0.0.1:<PORT>"

def image_to_3d(image_path, quality="high", seed=42):
    image_id = requests.post(
        f"{BASE}/pixal_studio/upload",
        files={"image": open(image_path, "rb")},
    ).json()["image_id"]

    requests.post(
        f"{BASE}/pixal_studio/generate",
        json={"image_id": image_id, "quality": quality, "seed": seed},
    )

    while True:
        s = requests.get(f"{BASE}/pixal_studio/status").json()
        print(f"{s['stage']}  {s['progress']:.0%}")
        if s["done"]:
            if s.get("error"):
                raise RuntimeError(s["error"])
            return requests.get(BASE + s["model_url"]).content  # GLB bytes

glb = image_to_3d("my_figure.png")
open("model.glb", "wb").write(glb)
```

### JavaScript (Node)

```js
import { readFileSync, writeFileSync } from "node:fs";

const BASE = "http://127.0.0.1:<PORT>";

async function imageTo3D(imagePath, quality = "high", seed = 42) {
  const form = new FormData();
  form.append("image", new Blob([readFileSync(imagePath)]));
  const { image_id } = await (await fetch(`${BASE}/pixal_studio/upload`, { method: "POST", body: form })).json();

  await fetch(`${BASE}/pixal_studio/generate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ image_id, quality, seed }),
  });

  for (;;) {
    const s = await (await fetch(`${BASE}/pixal_studio/status`)).json();
    console.log(`${s.stage}  ${(s.progress * 100).toFixed(0)}%`);
    if (s.done) {
      if (s.error) throw new Error(s.error);
      const buf = Buffer.from(await (await fetch(BASE + s.model_url)).arrayBuffer());
      writeFileSync("model.glb", buf);
      return;
    }
    await new Promise((r) => setTimeout(r, 1500));
  }
}
```

The same generation is also exposed as a standard ComfyUI node — `PixalStudioGenerate` (category *Pixal Studio*) — for use inside the full ComfyUI editor or via `POST /prompt`.

## Environment overrides

Set via the `env` block in `start.js`:

| Variable | Default | Purpose |
|---|---|---|
| `PIXAL_STUDIO_VRAM_MODE` | auto | `dynamic_vram` (needs torch 2.8+) · `native_low_vram` · `hybrid_low_vram` · `full_gpu` |
| `PIXAL_STUDIO_MODEL_REPO` | `TencentARC/Pixal3D` | HF repo or local snapshot path |
| `PIXAL_STUDIO_DOWNLOAD` | `1` | Auto-download missing model weights |
| `PIXAL_STUDIO_IDLE_UNLOAD` | `120` | Seconds to keep weights resident after a generation before releasing RAM (0 disables) |
| `PIXAL_STUDIO_UV_MAX_COST` | `8` | xatlas chart-growth cost during UV unwrap — higher = fewer, larger charts = much faster export with no visible quality change (`0`/`off` = upstream default) |

## Project structure

```
PIXAL-3D/
├── app/                     # TencentARC/Pixal3D (cloned by install.js)
├── comfyui/                 # comfy-org/comfyui (cloned by install.js)
│   ├── custom_nodes/
│   │   ├── Pixal3D-ComfyUI/ # community integration (cloned by install.js)
│   │   └── pixal_studio/    # studio bridge, copied here by install.js
│   ├── env/                 # shared Python venv (created by install.js)
│   └── models/              # downloaded weights (~43 GB, first launch)
├── studio/                  # THE STUDIO WEB UI — served by ComfyUI at the
│                            # server root via --front-end-root. Fully
│                            # self-contained (vendored model-viewer).
├── pixal_studio/            # canonical source of the studio bridge
│   └── web/                 # fallback UI copy (route /pixal_studio/app)
├── build/                   # CUDA extension sources (cloned by install.js)
├── gen/                     # uploads + generated GLB outputs at runtime
├── install.js               # 1-click install
├── start.js                 # 1-click launch (captures the server URL)
├── reset.js                 # wipes env + build artifacts, re-runs install
├── update.js                # git-pulls this repo + deps, refreshes bridge
├── torch.js                 # PyTorch cu128 installer helper
├── pinokio.js               # sidebar menu
└── pinokio.json             # metadata
```

## Troubleshooting

- **Check the logs first** (Pinokio convention): `logs/api/`, `logs/shell/` — the terminal view in the Pinokio sidebar shows the live server output
- **Choppy viewport / CPU spike while orbiting**: the browser window is software-rendering WebGL. Open the studio via **View in Browser (GPU viewport)**, or restart the app window (see *Smooth 3D viewport* above)
- **Environment check**: `comfyui/env/bin/python comfyui/custom_nodes/Pixal3D-ComfyUI/install.py --check --skip-requirements` prints a full import report (torch/CUDA/flash-attn/flex_gemm/cumesh/o_voxel/drtk/natten)
- **403 downloading the background model**: the model's `pipeline.json` originally points at the gated `briaai/RMBG-2.0`; the installer patches it to the open `ZhengPeng7/BiRefNet`
- **OOM during `ultra`**: use `high` — the 1536-cascade needs more than 12 GB even with offloading
- **First generation is slow**: weights load from disk into RAM on first use (~2 min); subsequent generations reuse the resident handle
- **Update refused (`Not possible to fast-forward`)**: a repo has local changes or diverged. Resolve it manually, or delete the folder and re-install
- **Reset**: wipes the Python env + build artifacts and re-runs the full install automatically (downloaded weights are kept)

## Credits

- [Pixal3D](https://github.com/TencentARC/Pixal3D) — Tencent ARC / Tsinghua (MIT)
- [ComfyUI](https://github.com/comfy-org/comfyui)
- [Pixal3D-ComfyUI](https://github.com/Saganaki22/Pixal3D-ComfyUI) — Saganaki22
- [Hunyuan3D-2GP](https://github.com/deepbeepmeep/Hunyuan3D-2GP) / Wan2GP by DeepBeepMeep — inspiration for the low-VRAM profile approach

Issues and pull requests welcome at [github.com/PrimeEcto/PIXAL-3D](https://github.com/PrimeEcto/PIXAL-3D).
