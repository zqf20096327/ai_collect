# CardboardBox Defect Detection via Synthetic Data Generation

> **From 44 real labels to deployment-grade accuracy** — Blender SDG + Two-Stage YOLO + Sim-to-Real Transfer  
> Independently replicating NVIDIA's SDG methodology with one non-obvious finding that changes deployability

[![mAP50](https://img.shields.io/badge/mAP50-0.89-brightgreen)](.)
[![Defect Hit Rate](https://img.shields.io/badge/Defect%20Hit-93%25-brightgreen)](.)
[![False Positive](https://img.shields.io/badge/Clean%20Box%20FP-0%25-brightgreen)](.)
[![Real Data](https://img.shields.io/badge/Real%20Labels-44%20images-blue)](.)
[![Synthetic Data](https://img.shields.io/badge/Synthetic-4000%20images-blue)](.)

---

## Demo Video

[![Watch the full demo on YouTube](https://img.youtube.com/vi/2sVSZpJezgQ/maxresdefault.jpg)](https://www.youtube.com/watch?v=2sVSZpJezgQ)

*Click to watch on YouTube — full pipeline walkthrough: Blender SDG → YOLO training → real-time webcam inference*

---

## Live Demo — Two-Stage Inference on Real Footage

> Green = Box (YOLO1) · Blue = Stain · Yellow = Puncture (YOLO2)

<table>
<tr>
<td align="center">
<img src="08_records/charts/conclusion_assets/gif/IMG_9132_annotated.gif" width="320"/>
<br><sub><b>IMG_9132</b> — Stain detection</sub>
</td>
<td align="center">
<img src="08_records/charts/conclusion_assets/gif/IMG_9133_annotated.gif" width="320"/>
<br><sub><b>IMG_9133</b> — Puncture detection</sub>
</td>
</tr>
<tr>
<td align="center">
<img src="08_records/charts/conclusion_assets/gif/IMG_9134_annotated.gif" width="320"/>
<br><sub><b>IMG_9134</b> — Clean box (zero false positive)</sub>
</td>
<td align="center">
<img src="08_records/charts/conclusion_assets/gif/IMG_9135_annotated.gif" width="320"/>
<br><sub><b>IMG_9135</b> — Dual-defect scenario</sub>
</td>
</tr>
</table>

---

## Dataset — Synthetic Data Pipeline at a Glance

The pipeline generates three synchronized data streams from a single Blender scene.  
Each GIF below cycles through **60 sampled frames** from the full 6,000+ image dataset.

| Blender Render | Mask Pass | YOLO Annotation Overlay |
|:-:|:-:|:-:|
| ![Render images](08_records/charts/conclusion_assets/gif/render_images.gif) | ![Mask passes](08_records/charts/conclusion_assets/gif/mask_passes.gif) | ![Annotated](08_records/charts/conclusion_assets/gif/annotated.gif) |
| *Cycles render — domain-randomized lighting, ground PBR, HDRI* | *Object mask pass — used for auto-labeling bounding boxes* | *Auto-generated YOLO label overlay via OpenCV contour* |

---

## TL;DR

| | Real-Only (44 imgs) | + 4,000 Synthetic | Gain |
|---|---|---|---|
| Val mAP50 | 0.69 | **0.89** | +0.20 |
| Defect Hit Rate | 71% | **93%** | +22 pp |
| Clean Box FP | 23% | **0%** | −23 pp |
| Stain Recall | 40% | **80%** | ×2 |

The core insight is **not** "synthetic data is magic" — it's that synthetic data turns 50 prototyping images into deployment-grade performance, provided the negative anchor distribution is correct.

![SDG Value](08_records/charts/figures/H3_sdg_value.png)

---

## Four Non-Obvious Engineering Findings

### Finding 1 — Real Negative Anchor Is the Deployability Switch (Not Sample Count)

Standard SDG tutorials explain "synthetic pre-train + small real fine-tune." None explain **which real samples** matter. This project isolates the effect:

| Config | Train Composition | Clean Box FP |
|---|---|---|
| Hybrid v1 (failed) | 4,000 synthetic + 12 real positive | **76%** ❌ |
| **Hybrid v2 🏆** | 4,000 synthetic + 12 positive + **20 real clean negative anchor** | **0%** ✅ |

**The delta is 20 real clean-box crops.** Without them, the model's decision threshold collapses: it flags printing text and fold creases as defects. Adding positives without negatives makes this worse, not better.

> **Engineering rule:** In hybrid SDG training, source your negatives before sourcing your positives.

![Anchor Decides Hybrid](08_records/charts/figures/H1_anchor_decides_hybrid.png)

---

### Finding 2 — P001 Epoch-Early Lock: Distribution Shape > Dataset Scale

Ultralytics YOLOv8's fitness function (`0.1×mAP50 + 0.9×mAP50-95`) combined with a small val set (30 images) and default patience logic can lock `best.pt` at epoch 1–2 — silently shipping a COCO-pretrained model with no domain learning.

| Scale | No HN backgrounds | + 22 HN empty backgrounds |
|---|---|---|
| 500-image train | best = epoch 1 🔒 | best = epoch 30 ✅ |
| 6,427-image train | best = epoch 2 🔒 | **best = epoch 10 ✅** |

**13× more data does not solve it. 22 hard-negative backgrounds (0.34% of dataset) do.** Training distribution shape controls optimizer behavior more than volume.

![P001 2×2 Ablation](08_records/charts/figures/H2_p001_2x2.png)
![YOLO1 Test Results](08_records/charts/figures/Y1_yolo1_test_results.png)

---

### Finding 3 — Double Augmentation Destroys Fine-Grained Features

When the SDG pipeline already applies Sim-to-Real augmentation (color shift, blur, JPEG compression, noise), stacking Ultralytics default augmentation (mosaic, HSV, random erasing) on top creates destructive over-perturbation for small defects like Puncture (circular holes < 30px):

| Aug Configuration | Val Puncture mAP50 | Multiplier |
|---|---|---|
| Both aug layers on (baseline) | 0.10 | 1.0× |
| Pipeline aug off (noaug) | 0.385 | 3.8× |
| **Ultralytics aug off (noultaug)** | **0.76** | **7.6×** |

Most SDG tutorials omit this — but it determines whether your model escapes synthetic-only val overfitting.

![Double Aug 2×2](08_records/charts/figures/G3_double_aug_2x2.png)

---

### Finding 4 — Sim-to-Real Gap is Feature-Dependent, Not Task-Dependent

The same Blender pipeline produces radically different sim-to-real transfer outcomes depending on the defect's visual signature:

| Target | Synthetic-Only Performance | Explanation |
|---|---|---|
| YOLO1 — Box localization | mAP50 ≈ 0.95+, test recall 94% | Large-scale geometry + flat texture; PBR shader closely matches reality |
| YOLO2 — Puncture (circular hole) | 100% hit rate | Sharp edge, concentrated feature; easy to express in shader |
| YOLO2 — Stain (translucent gradient) | Real-only 40%, synth-only **0%**, hybrid **80%** | Subtle translucency and diffuse gradients exceed PBR fidelity |

**"Is synthetic data enough?"** has no universal answer. It depends on whether the defect's visual feature is expressible by your shader. Audit your defect types before choosing pure-synthetic vs. hybrid strategy.

![Cross-Task SDG](08_records/charts/figures/Y2_cross_task_sdg.png)

---

## Apple-to-Apple Ablation — 5 Configs, 40 Shared Test Images

Held-out test set: 40 images (5 stain + 5 puncture + 4 both + 26 clean) — never seen in any training run.

| Experiment | Train Composition | Defect Hit | Clean FP | Verdict |
|---|---|---|---|---|
| realonly_fair | 0 synthetic + 44 real | 71% | 23% | Prototype-viable, high FP |
| noaug | 4,000 synth (no pipeline aug) | 0% | 0% | Double aug → val overfit |
| **noultaug** | 4,000 synth (no YOLO aug) | **86%** | 8% | ✅ Best pure-synthetic baseline |
| hybrid v1 | 4,000 + 12 real positive | 100% | 62% | ❌ FP explosion; undeployable |
| **hybrid_v2** 🏆 | 4,000 + 12 positive + 20 anchor | **93%** | **0%** | ✅ Only deployment-ready config |

![5-Way Apple-to-Apple](08_records/charts/figures/G1_yolo2_apple_to_apple.png)

> **Note on Confusion Matrix vs. deployment conf:** Ultralytics confusion matrix uses conf ≈ 0.001 for PR/F1 curve coverage; it does not reflect deployed FP rate. The "Clean FP" column above is empirical: `11_predict_yolo2.py --conf 0.40` on the 40-image test set.

### Training Dynamics

![Loss Curves](08_records/charts/figures/C1_loss_curves.png)
![Confusion Matrix — Pure Baselines](08_records/charts/figures/CM1a_pure_baselines.png)
![Confusion Matrix — Hybrid Anchor Effect](08_records/charts/figures/CM1b_hybrid_anchor_effect.png)

---

## System Architecture

| Pipeline Overview | Blender SDG Workflow | ComfyUI Stain Shader |
|:-:|:-:|:-:|
| ![Pipeline](08_records/charts/figures/pipeline_architecture.png) | ![Blender](08_records/charts/figures/Blender_workflow@2x.png) | ![ComfyUI](08_records/charts/figures/ComfyUI@2x.png) |

```
Webcam frame (640×480)
    │
    ▼
YOLO1  (production_v2_HN/best.pt)
  └─ Locates box BBox  [class 0, conf ≥ 0.50]
    │
    ▼  tight crop (0% padding) → resize 640×640
YOLO2  (production_v1_hybrid_v2/best.pt)
  └─ Detects Stain / Puncture  [conf ≥ 0.40]
    │
    ▼
Overlay: Green = Box · Blue = Stain · Yellow = Puncture
```

**Critical design:** training ROI and inference ROI are strictly mirrored (same crop padding, same resize) — eliminating train/inference domain gap.

---

## Quickstart

> **Note — This repository is a research showcase for Synthetic Data Generation (SDG).**
> The Blender scene file (`03_Blender_Project/*.blend`, ~158 MB) is not version-controlled.
> Running the full pipeline from scratch requires you to supply your own Blender scene and
> update the object names, material slot references, and file paths in `02_blender_render.py`
> to match your scene setup.
> The inference scripts (09–12) and pre-trained weights work independently without Blender.

### Environment

- Python 3.11 / Windows 11
- NVIDIA RTX 4050 Laptop (6 GB VRAM) / CUDA 12.1
- Blender 4.x / Ultralytics 8.4.38

### Run the full pipeline from scratch

```powershell
# 1. Activate venv
.\venv\Scripts\Activate.ps1

# 2. Generate synthetic data  (~5,900 Blender renders, ~6 hours)
python 02_Scripts\03_render_operator.py

# 3. Generate YOLO1 / YOLO2 labels
python 02_Scripts\04_annotator_yolo1.py
python 02_Scripts\05_cropper_yolo2.py

# 4. Train  (YOLO1: ~30 min / YOLO2: ~10 min)
python 02_Scripts\08_train.py --target yolo1 --patience 20
python 02_Scripts\08_train.py --target yolo2 --patience 20 --no-yolo-aug

# 5. Real-time webcam demo
python 02_Scripts\11_realtime_demo.py
```

### Run demo directly with pre-trained weights

```powershell
python 02_Scripts\11_realtime_demo.py
# Auto-loads:
#   YOLO1 = production_v2_HN/best.pt         (94% test recall)
#   YOLO2 = production_v1_hybrid_v2/best.pt  (93% defect hit, 0% FP)
# Q to quit · S to screenshot
```

### Run annotated video inference on a file

```powershell
python 02_Scripts\11b_predict_video.py --input path/to/video.mp4
```

---

## Repository Structure

```
CardboardBox_detect/
├── 01_Assets/              # PBR ground materials / HDRI / decals / real reference photos
├── 02_Scripts/             # Pipeline + training / inference scripts (00–12)
├── 03_Blender_Project/     # Blender master scene  (not version-controlled; .blend excluded)
├── 04_Dataset_YOLO1/       # Box-detection dataset  ← generated by pipeline, not on GitHub
├── 05_Dataset_YOLO2/       # Defect-detection dataset ← generated by pipeline, not on GitHub
├── 06_Raw_Output/          # Blender renders + QA / predict results ← generated, not on GitHub
├── 07_Models/              # Trained weights (3 best.pt published; others gitignored)
└── 08_records/             # Charts / logs
    └── charts/             # Publication-ready figures + GIFs
```

> **Note:** `04_`, `05_`, `06_` are pipeline outputs and are `.gitignore`d.
> Run scripts `03 → 04 → 05` in order to regenerate them (requires Blender scene — see Quickstart).

Full experiment log: [CLAUDE.md](CLAUDE.md) — 10 ablation groups + P001–P014 engineering incident records.

---

## Alignment with NVIDIA SDG Methodology

| Dimension | NVIDIA Reference | This Project |
|---|---|---|
| Synthetic images | 1,500 | 4,000 |
| Real images | 50 | 44 |
| Real data ratio | 3.3% | **1.1%** |
| Strategy | Two-stage fine-tune (pretrain → freeze + low-LR FT) | Single-stage hybrid + ablation-controlled fine-tune |
| Key result | Synthetic pre-training rescues pure-real failure | Same conclusion + **real negative anchor** as secondary deployability switch |

This project independently replicates NVIDIA's methodology and adds the negative-anchor finding not covered in NVIDIA's published guidance.

> **Reference:** Dataset numbers (1,500 synthetic / 50 real) and methodology sourced from Docca & Torculas (2023) — *NVIDIA Developer Blog* — and the companion [YouTube demo](https://www.youtube.com/watch?v=cuoZAYoewE0). See Citations section for full references.

---

## ⚠️ Limitations

This is a **3-month solo side project** with AI coding assistance. The findings are point estimates from a single hardware setup, and the pipeline is currently designed around cardboard boxes specifically.

| # | Limitation | Impact |
|---|---|---|
| L1 | Val set = 30 images; statistically unstable | mAP is sensitive to individual image changes |
| L2 | Test set size varies across experiments (72 / 84 / 40) | Mitigated via 40-image intersection for apple-to-apple comparison |
| L3 | No cross-camera / cross-box-type domain validation | Performance on a different webcam is unknown |
| L4 | Single architecture (YOLOv8n); v8s / v8m not tested | Conclusions may be model-scale-sensitive |
| L5 | Augmentation parameters are heuristic; no grid search | 0.89 mAP50 is likely not the ceiling |
| L6 | **Low object replicability** — switching to a different object (screws, teddy bears, shoes, etc.) requires redesigning the physical and mathematical rendering rules in scripts 01–03 | Pipeline is not plug-and-play for new products |

---

## Future Work

**Immediate: YOLO1 Production Tuning**  
The current YOLO1 model (94% test recall) is near production-ready. Next step is extended real-world stress testing across varied lighting and camera angles before combining with YOLO2 for end-to-end field deployment.

**Generative AI for Sim-to-Real Gap Closure**  
Blender-based SDG was chosen for its full geometric controllability — every coordinate, camera angle, and defect position is programmatically determined, enabling automated annotation at scale. However, Blender's PBR shader has a ceiling: subtle optical effects like translucent stain gradients create a sim-to-real gap that purely physics-based rendering cannot bridge (see Finding 4).

The next research phase will explore using **generative AI (diffusion models / image-to-image translation)** to post-process Blender outputs and reduce the visual domain gap — treating the synthetic dataset as a structured starting point for generative augmentation rather than a final output. The goal is to preserve the geometric labeling accuracy of SDG while gaining the photorealistic texture fidelity of learned priors.

**Scaling to NVIDIA Omniverse Replicator + Cosmos**  
This project deliberately reimplemented NVIDIA's SDG methodology in Blender to understand the pipeline from first principles (see *Alignment with NVIDIA SDG Methodology*). The natural production-grade upgrade path is NVIDIA's own two-stage stack, which maps almost one-to-one onto the structured-render → generative-augment direction above:

| Current (Blender) | NVIDIA Upgrade Path | What It Buys |
|---|---|---|
| Custom orchestrator + Cycles render | **[Omniverse Replicator](https://developer.nvidia.com/omniverse/replicator)** | Native domain randomization API, USD-based scenes, ground-truth annotation at scale, RTX-accelerated throughput |
| Diffusion post-processing (planned) | **[NVIDIA Cosmos](https://www.nvidia.com/en-us/ai/cosmos/)** (Cosmos Transfer world foundation models) | Conditions on the structured render's segmentation / depth / edge maps to synthesize photorealistic, physically-grounded variations — **closing the sim-to-real gap while preserving the exact labels** |

Concretely, the target workflow is: **Omniverse Replicator** generates the controllable, perfectly-labeled 3D ground truth → **Cosmos Transfer** amplifies each frame into diverse, photoreal samples conditioned on those structured maps. This is precisely NVIDIA's recommended physical-AI data flywheel, and it directly addresses Finding 4 — the translucent-stain shader ceiling — by replacing hand-tuned PBR fidelity with a learned world prior, without sacrificing the automated annotation that makes SDG viable. Replicator also removes the current pipeline's biggest limitation (L6, low object replicability): swapping in a new product becomes a USD asset change rather than a rewrite of the geometric rendering rules.

**Structured Sim-to-Real Evaluation**  
Formally measure domain gap per defect class under controlled lighting and camera changes, to build a transferability map for future SDG pipeline decisions.

---

## Tech Stack

| Category | Tools |
|---|---|
| 3D Rendering | Blender 4.x (Cycles, OptiX) |
| Scene Randomization | Custom orchestrator + render operator |
| Domain Randomization | 20 HDRI environments + 29 PBR ground materials + projected decal variation |
| Sim-to-Real Augmentation | OpenCV (cool color shift + contrast + blur + JPEG + noise) |
| Model | YOLOv8n (Ultralytics 8.4.38) |
| Deployment | OpenCV webcam + dual-model real-time inference |

---

## Citations

- Docca, A., & Torculas, M. (2023, April 19). [How to Train a Defect Detection Model Using Synthetic Data with NVIDIA Omniverse Replicator.](https://developer.nvidia.com/blog/how-to-train-a-defect-detection-model-using-synthetic-data-with-nvidia-omniverse-replicator/) *NVIDIA Developer Blog.* ← primary reference for the NVIDIA SDG methodology comparison
- NVIDIA Omniverse. (2023). [Defect Detection Model Trained on Synthetic Data w/ Omniverse Code, Adobe Substance 3D, and Roboflow](https://www.youtube.com/watch?v=cuoZAYoewE0) [Video]. *YouTube.* ← companion demo video; dataset numbers (1,500 synthetic / 50 real) cited from here
- NVIDIA. (2025). [Cosmos World Foundation Models for Physical AI.](https://www.nvidia.com/en-us/ai/cosmos/) ← referenced in Future Work as the generative-augmentation upgrade path
- NVIDIA. [Omniverse Replicator — Synthetic Data Generation.](https://developer.nvidia.com/omniverse/replicator) ← referenced in Future Work as the production-grade SDG upgrade path
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- Tobin, J., Fong, R., Ray, A., Schneider, J., Zaremba, W., & Abbeel, P. (2017). "Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World." *IROS 2017*
- Ghiasi, G., Cui, Y., Srinivas, A., Qian, R., Lin, T.Y., Cubuk, E.D., Le, Q.V., & Zoph, B. (2021). "Simple Copy-Paste is a Strong Data Augmentation Method for Instance Segmentation." *CVPR 2021*
- Boikov, A., Payor, V., Savelev, R., & Kolesnikov, A. (2021). ["Synthetic Data Generation for Steel Defect Detection and Classification Using Deep Learning."](https://www.mdpi.com/2073-8994/13/7/1176) *Symmetry*, 13(7), 1176

---

## Author

**bbKurt11** — Sim-to-Real Computer Vision Research (2026)

This project demonstrates a complete engineering pipeline from synthetic data generation → domain randomization → sim-to-real transfer, validated across 9 YOLO2 ablations × 4 YOLO1 ablations, yielding four non-obvious engineering findings.

📬 [xinhong0127@gmail.com](mailto:xinhong0127@gmail.com)

💼 [LinkedIn]https://www.linkedin.com/in/kurt-du-708145401

---

## Disclaimer

The cardboard box used in this project belongs to a commercial diaper brand. **This project is a personal, non-commercial research side project. It is not affiliated with, endorsed by, or associated with any brand or company in any way.** The box was used solely as a physical object for computer vision research purposes. No brand identity, trademark, or proprietary information is intentionally reproduced or exploited.

