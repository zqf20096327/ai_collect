<div align="center">

# H3 Face Fix for ComfyUI (PixelAI Labs)

### Fix melted, blurry far faces in MiniMax H3 videos. No re-render, original audio kept.

MiniMax H3 smudges faces that are far from the camera. This workflow finds the face, redraws it big with your
character's photo and pastes it back into the clip you already made. Our **H3 Face Size Fade** node keeps close-ups exactly as H3 made them.

[![Premium ComfyUI courses](https://img.shields.io/badge/Premium%20ComfyUI%20courses-pixelailabs.com-96FF3D?style=for-the-badge&labelColor=050505)](https://pixelailabs.com)
[![Support on Ko-fi](https://img.shields.io/badge/Support%20on-Ko--fi-FF6433?style=for-the-badge&logo=kofi&logoColor=white&labelColor=050505)](https://ko-fi.com/pixelailabs)

![The same MiniMax H3 frame: melted face on the left, fixed face on the right](docs/hero.jpg)

</div>

---

## Examples

Left: the clip as H3 made it. Right: the same clip after one run. Click a GIF for the full video with sound.

<table>
<tr>
<td width="50%" valign="top"><a href="docs/example_boutique.mp4"><img src="docs/example_boutique.gif" alt="Try-on video, face 47 px" width="100%"></a><br><b>Try-on walk:</b> her face starts at 47 px with melted eyes</td>
<td width="50%" valign="top"><a href="docs/example_street.mp4"><img src="docs/example_street.gif" alt="Street walk, face 30 to 85 px" width="100%"></a><br><b>Street walk:</b> filmed from across the road, face 30 to 85 px</td>
</tr>
<tr>
<td width="50%" valign="top"><a href="docs/example_farmer.mp4"><img src="docs/example_farmer.gif" alt="Farmer push-in" width="100%"></a><br><b>Push-in:</b> why the fade matters. Full fix while he is far away, the close-up stays untouched (no extra wrinkles)</td>
<td width="50%" valign="top"><a href="docs/example_cart.mp4"><img src="docs/example_cart.gif" alt="Speeding cart" width="100%"></a><br><b>Tracking shot at speed:</b> the new face stays locked on, no wobble</td>
</tr>
</table>

---

## Installation

### 1. Install the node

**ComfyUI Manager:** *Custom Nodes Manager* → *Install via Git URL* →
`https://github.com/Pixelailabs/ComfyUI-H3-FaceFix-PixelAILabs` → restart ComfyUI.

**Manual:**

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Pixelailabs/ComfyUI-H3-FaceFix-PixelAILabs
```

The node needs no extra Python packages. You need ComfyUI 0.45.0 or newer (H3 and SAM 3.1 are built in).

### 2. The node packs the workflow uses

All in the Manager (search the name), or *Install via Git URL*:

| Pack | Used for |
|---|---|
| [ComfyUI-H3-FaceRefine](https://github.com/Carasibana/ComfyUI-H3-FaceRefine) by Carasibana | Face tracking, crop and paste back |
| [MaskVidExperiments](https://github.com/drozbay/MaskVidExperiments) by drozbay | Cleans the face mask |
| [ComfyUI-VOSR2](https://github.com/ylchen333/ComfyUI-VOSR2) by ylchen333 | Final polish. Downloads its model (about 7 GB) on the first run |
| [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes) | Sage attention patch for H3 |
| [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite) | Loads and saves the video with its audio |
| [ComfyUI-Impact-Subpack](https://github.com/ltdrdata/ComfyUI-Impact-Subpack) | Registers the `ultralytics` folder for the face detector |

### 3. Models

| Model | Folder | Size |
|---|---|---|
| [Minimax-h3_Singularity_ref2va_v2_int8](https://huggingface.co/WarmBloodAban/Minimax-h3_Singularity/blob/main/Minimax-h3_Singularity_ref2va_v2_int8.safetensors) | `models/diffusion_models` | 34 GB |
| [pika_h3_flex_turbo_8step_hd_ref2va](https://huggingface.co/Pika-Labs/Pika-H3-Flex-Turbo-LoRA/blob/main/pika_h3_flex_turbo_8step_hd_ref2va.safetensors) | `models/loras` | 3.9 GB |
| [qwen3vl_32b_minimax_h3_int8_convrot](https://huggingface.co/Comfy-Org/MiniMax-H3/blob/main/text_encoders/qwen3vl_32b_minimax_h3_int8_convrot.safetensors) (RTX 50: the [nvfp4_awq](https://huggingface.co/Comfy-Org/MiniMax-H3/blob/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) one, 15.7 GB) | `models/text_encoders` | 27 GB |
| [minimax_h3_video_vae_int8_convrot](https://huggingface.co/Comfy-Org/MiniMax-H3/blob/main/vae/minimax_h3_video_vae_int8_convrot.safetensors) | `models/vae` | 2.8 GB |
| [minimax_h3_audio_vae_fp32](https://huggingface.co/Comfy-Org/MiniMax-H3/blob/main/vae/minimax_h3_audio_vae_fp32.safetensors) | `models/vae` | 0.6 GB |
| [sam3.1_multiplex_fp16](https://huggingface.co/Comfy-Org/sam3.1/blob/main/checkpoints/sam3.1_multiplex_fp16.safetensors) | `models/checkpoints` | 1.75 GB |
| [face_yolov8n.pt](https://huggingface.co/Bingsu/adetailer/blob/main/face_yolov8n.pt) | `models/ultralytics/segm` | 6 MB |
| VOSR2 *(automatic)* | `models/VOSR2` | about 7 GB |

Already making H3 videos? Then you have most of these.

### 4. Load the workflow

[`example_workflows/PixelAI_H3_FaceFix.json`](example_workflows/PixelAI_H3_FaceFix.json): drag it into ComfyUI, or find
it in *Workflow → Browse Templates*.

![The H3 Face Fix workflow: 8 coloured groups, left to right](example_workflows/PixelAI_H3_FaceFix.jpg)

---

## Quick start

1. **1. Inputs:** load your finished H3 clip (its audio is kept) and a clear photo or character sheet of the face.
2. **Which face?** `largest_face` (default) or `smallest_face`, and **Face number** 0, 1, 2... when there are several people.
3. Press **Run**.
4. The fixed clip, with the original sound, is saved in `ComfyUI/output/` as `H3_FaceFix_*.mp4`.

---

## How it works

| Group | What happens |
|---|---|
| **3. Find the face** | Tracks the face through every frame and cuts a big square around it |
| **Fade on close faces** | Our node: decides how much of the fix each frame gets, from the face size |
| **4. Face mask** | SAM 3.1 masks only the face, so the background stays as it was |
| **5 + 6. Prepare, re-render** | H3 redraws the face at 768 px from your photo. No prompt |
| **7. Polish + paste back** | VOSR2 cleans it up, then only the face is stitched back into your clip |

---

## The node

**H3 Face Size Fade (PixelAI Labs)** sits between *H3 Face Track Crop* and *H3 Face Stitch*. Faces at or under 110 px
get the full fix, faces at 180 px and up stay untouched, with a smooth ramp in between. The sizes are for 1080p and
scale with your video's height.

| Setting | Default | Notes |
|---|---|---|
| `full_fix_below_px` | 110 | Face height that gets the full fix |
| `no_fix_above_px` | 180 | Face height from which the original face is kept |
| `crop_factor` | 2.5 | Same value as on H3 Face Track Crop |
| `reference_height` | 1080 | The px values above are for this video height. 0 = use them as they are |

The rest of the workflow, as shipped:

| Setting | Value |
|---|---|
| Sampler / scheduler | euler / beta, 8 steps, denoise 0.5 |
| Turbo LoRA | Pika Flex Turbo 8-step, strength 1.0 |
| Face crop | 768 x 768, crop_factor 2.5 |
| Stitch | face_only, dilation 24, feather 24, colour match 1 |
| Prompt | none: the face photo does the work |

---

## Speed

About **4 minutes per 10 s of 1080p video** on an RTX 5090 (32 GB). The first run is slower while VOSR2 downloads
its model.

---

## Tips

- **One face per run.** More people? Run once per person with Face number 0, 1, 2 and feed each result into the next run.
  For `smallest_face` or a face number above 0, turn `identity_track` off on the Track Crop node.
- **The small face in the back is the broken one?** Switch *Which face?* to `smallest_face`.
- **Scan your old clips.** In one 121-clip episode, 57 clips had a face small enough to need this.
- **Close-ups are left alone on purpose.** Turning the fix on for big faces adds wrinkles and age. Keep the fade on.

---

## Learn more and support

<table>
<tr>
<td width="50%" valign="top">

### 🎓 Premium ComfyUI courses
Build one consistent AI influencer and make ultra-realistic photos and H3 talking videos with her: the
**[AI Influencer Pro](https://pixelailabs.com/comfyui-workflows/krea2-minimax-h3-ultrarealistic-ai-influencer-pro)**
course and more on **[pixelailabs.com](https://pixelailabs.com)**. The full video tutorial for this workflow is on our
YouTube channel, Bonnie AI Lab.

</td>
<td width="50%" valign="top">

### ☕ Support this project
This node and workflow are free. If they save your clips, you can buy me a coffee:

<a href="https://ko-fi.com/pixelailabs"><img src="https://cdn.prod.website-files.com/5c14e387dab576fe667689cf/670f5a02fcf48af59c591185_support_me_on_kofi_dark.avif" alt="Support me on Ko-fi" height="48"></a>

</td>
</tr>
</table>

---

## Credits

- [ComfyUI-H3-FaceRefine](https://github.com/Carasibana/ComfyUI-H3-FaceRefine) by Carasibana: the face track, crop and stitch nodes
- [MaskVidExperiments](https://github.com/drozbay/MaskVidExperiments) by drozbay, [ComfyUI-VOSR2](https://github.com/ylchen333/ComfyUI-VOSR2) by ylchen333
- [Pika H3 Flex Turbo LoRA](https://huggingface.co/Pika-Labs/Pika-H3-Flex-Turbo-LoRA) by Pika Labs, [MiniMax H3](https://huggingface.co/MiniMaxAI/MiniMax-H3) by MiniMax
- The idea of adding the SAM mask and VOSR2: [sunbaolong_2001 on X](https://x.com/sunbaolong_2001/status/2122877265960903146)

Made by **[PixelAI Labs](https://pixelailabs.com)**. MIT licensed.
