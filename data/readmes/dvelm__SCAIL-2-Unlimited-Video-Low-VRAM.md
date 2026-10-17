<div align="center">

# SCAIL-2 Unlimited Video — Low-VRAM Character Animation

**Create unlimited-length videos on a low-VRAM GPU (8–12 GB)** — animate any reference image with a driving video using SCAIL-2 (Wan 2.1 14B), quantized to GGUF for small cards.

**Animate any reference image using a driving video with [SCAIL-2](https://github.com/zai-org/SCAIL-2) (Wan 2.1 14B backbone), quantized to GGUF so it runs on **8 GB and 12 GB GPUs** — with a clean one-node control panel and automatic multi-segment generation.

> Runs on **8 GB → 12 GB** VRAM. Generates **unlimited-length videos** by chaining segments automatically.

</div>

---

## ✨ What this gives you

- **Character animation / motion transfer**: a reference image (a person, look, or character) is animated using the motion and scene from a driving video. Animation mode keeps **all** subjects from the reference; Replacement mode swaps only the tracked person.
- **Runs on small GPUs**: the diffusion model is a GGUF quant (Q3_K_M ≈ **8.1 GB** for ~8 GB cards, Q4_K_M ≈ **10.9 GB** for ~12 GB cards). No 24 GB monster needed.
- **Unlimited-length videos**: instead of one hard-coded pass (which OOMs low-VRAM cards), the workflow generates in **81-frame segments** (76-frame steps with a 5-frame overlap anchor) and chains them **automatically** until your requested `seconds` are reached. 5 s → 1 segment, 10 s → 2, 30 s → 7, and so on — limited only by your patience, not the card.
- **One config node** controls everything: seconds, fps, resolution, steps, cfg, seed, mode, which subject to track, randomize. Width/height `0` = auto from the driving video.
- **Continuation**: pick up where a previous run ended (anchor the new run to the old output) for effectively endless video.
- Single **Queue click** — no manual per-segment chaining, model loaded once.

---

## 🖼️ What it looks like

| Inputs | Output |
|---|---|
| **Reference image** (who/character to keep) | An animated video (e.g. `SCAIL2_FULL_00001.mp4`) |
| **Driving video** (the motion/scene to copy) | — |

---

## 📦 Repository layout

```
SCAIL-2-GGUF-Easy-Config/
├── workflows/
│   └── SCAIL-2 GGUF 12GB (Easy Config).json   ← the workflow (drag into ComfyUI)
├── custom_nodes/
│   └── scail2-easy-config/                    ← the custom node pack (copy to custom_nodes/)
├── download_models.bat                        ← model downloader (Windows)
├── download_models.sh                         ← model downloader (Linux / macOS)
├── INSTALL.md                                 ← full step-by-step install guide
└── README.md
```

---

## 🚀 Quick start (5 steps)

1. **ComfyUI 0.33.1 or newer** — the SCAIL-2 nodes (`WanSCAILToVideo`, `SCAIL2ColoredMask`, `SAM3_VideoTrack`) are built in from this version. Tested on 0.33.1 (revision 468).
2. **Copy the custom node pack** → `ComfyUI/custom_nodes/scail2-easy-config/` (the whole folder). This pack is fully self-contained — it needs no code changes to run.
3. **Install companion node packs** (ComfyUI-Manager): `ComfyUI-GGUF`, `VideoHelperSuite`, `KJNodes` (optional: `rgthree-comfy`).
4. **Download the models**: run `download_models.bat` (Windows) or `bash download_models.sh` (Linux/macOS) from the repo root, **or** download the files manually — every link is listed in the workflow's built-in guide note and in [INSTALL.md](INSTALL.md). No model downloads happen inside the workflow itself.
5. **Drop your input files** in `ComfyUI/input/` — name the **driving video** `your_driving_video.mp4` and the **reference image** `your_reference_image.png` (or rename the placeholders in the workflow's Load nodes) — then drag `workflows/SCAIL-2 GGUF 12GB (Easy Config).json` into ComfyUI, **Queue**.

> 💡 A fresh install needs **no code modification** — copy the pack + workflow + models and it just works (see [INSTALL.md](INSTALL.md) for the exact list).

---

## 🎛️ The control panel (SCAIL-2 Easy Config node)

| Setting | Meaning |
|---|---|
| `seconds` | Length of the output. `0` = whole driving video. Auto-chained in segments. |
| `fps` | `16` = Wan native. `20/22/24` work (more frames = more VRAM/time). |
| `width` / `height` | `0` = auto from driving video (keeps aspect ratio, multiple of 32). e.g. `832`/`480`. |
| `steps` / `cfg` | `6` / `1.0` = recommended LightX2V distill values. |
| `seed` | Fixed/manual seed (used when `randomize_seed` is OFF). |
| `replace_mode` | **OFF = Animation** (full reference image, ALL subjects animate). **ON = Replacement** (only the tracked person is swapped). |
| `object_indices` | Comma-separated index list of which tracked people to use. **Keep EMPTY** (`""` = all) or `"0"` for the leftmost person. **Never type `True`/`False`** — it's an index list, not a toggle. |
| `randomize_seed` | ON: a fresh random seed every Queue, shared by all segments. OFF: fixed seed (reproducible). |
| `video` | Filename of the driving video (in `input/`). |

---

## 🧠 How "unlimited length" works

SCAIL-2 (like Wan) generates ~81 video frames per pass — a single longer pass needs too much VRAM, especially on low-VRAM cards. This workflow:

1. Generates segment **0** (81 frames).
2. For each next segment, seeds the first 5 latent frames with the previous segment's tail (the **5-frame anchor**) so motion is continuous.
3. **Drops those 5 anchor frames from the output** — so there are **no replayed frames** at segment boundaries (verified).
4. Loops until your `seconds × fps` frames are produced, then trims to exactly that length.

Result: smooth, arbitrarily long video from an 8/12 GB card. For **extra-long** work, use the printed console hint to **continue** a finished run (see below).

---

## 🔁 Continuing a run (endless video)

After each run the console prints the last source frame used. To continue:

1. Set `VHS_LoadVideo` → `skip_first_frames` to the printed `first unused source frame` value.
2. Feed the previous output's **last 5 frames** into the loop node's `anchor_frames` input.
3. Queue — the new run re-renders the 5-frame seam on that anchor instead of jumping.

(Recipe is also in the workflow's built-in guide note and in INSTALL.md.)

---

## ⚠️ Known gotchas (all handled, good to know)

- **`object_indices`**: keep it empty. The pack auto-corrects a stray `True`/`False` and warns, but empty/`"0"` is correct.
- **`max_objects=2`** is set on both SAM3 trackers so the *same* person gets the *same* color in the pose mask and reference mask (identity binding). Don't drop it to 1 on a multi-person scene.
- **Resolution**: the model trains at 512p/704p. `480×256` works but looks soft — prefer `832×480` (12 GB) or `704×512`-class (8 GB).
- The `SHAPE MISMATCH patch_embedding (36 vs 20)` warning is **harmless** (GGUF card confirms).

---

## 📜 Credits & licenses

- **Model**: [zai-org/SCAIL-2](https://github.com/zai-org/SCAIL-2) (Wan 2.1 14B backbone).
- **GGUF quantization**: [realrebelai/SCAIL-2_GGUF](https://huggingface.co/realrebelai/SCAIL-2_GGUF) (MIT).
- **GGUF tooling**: [city96/ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF).
- **Distill LoRA**: LightX2V step/cfg distill.
- This workflow + custom node pack: see [LICENSE](LICENSE).

---

## ❓ Questions / troubleshooting

See [INSTALL.md](INSTALL.md) for the full setup, model list, and troubleshooting. Open a GitHub issue if you hit something not covered.
