# AcademiaSD LoRAlab Trainer Studio

<p align="center">
  <img src="assets/launcher_LoRAlab.jpg" alt="AcademiaSD LoRAlab Trainer Studio" width="900">
</p>

## 📅 Changelog

What was added, newest first. Each entry links to its commit.

**2026-11-26**

- <img src="https://img.shields.io/badge/MAJOR%20UPDATE-7c3aed?style=for-the-badge" alt="MAJOR UPDATE" height="22"> **Final XY grid in every image trainer** — when the training ends, the same image (same prompt and seed) is made with several checkpoints (rows) and LoRA strengths (columns), with the face likeness % on each image. It shows which step and strength to use without going to ComfyUI. Turn on **Final XY grid** in 2b. Training Previews ([details](#-final-xy-grid)) [`fe4871f`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/fe4871f)

**2026-11-25**

- <img src="https://img.shields.io/badge/NEW%20TRAINER-ff2d55?style=for-the-badge" alt="NEW TRAINER" height="22"> **Anima 2.9B: anime and illustration LoRAs on the 40-block Anima** — Anima-Base with 12 more blocks (preview v1), trained in NF4 in under 6 GB of VRAM. It has its own card, settings, cache and outputs, and shares the code of the Anima trainer ([details](#anima-29b--anime-and-illustration-loras-on-the-40-block-anima)) [`fedc57b`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/fedc57b)

**2026-11-22**

- **New LR curve on resume**, in every trainer: a checkbox under the LR Scheduler. The LR curve always covered the whole training, so raising Total Steps and resuming continued half-way along the longer curve. With the checkbox, resuming starts a new curve at that step, from the current LR down to its minimum: for example 1000 steps from 4e-4 to 4e-5, then 1000 more from 1e-4 to 1e-5 ([details](#lr-scheduler)) [`dfca123`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/dfca123) ([#88](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/issues/88))
- **Krea 2 from 8 GB of VRAM** — the block swap and **VRAM Profile** of FLUX.1 and Klein 9B. At 1024² Krea 2 peaked at 11.6 GB, enough to spill into Windows shared memory on a 12 GB card and slow down several times; with the 12 GB profile it peaks at 8.0 GB and with the 8 GB one at 4.2 GB, with the same results. A new **Free CUDA cache after each update** checkbox (off by default) hands the unused cached VRAM back to the driver after every optimizer update ([details](#krea-2--image-loras-for-krea-2-raw-and-turbo)) [`c37ae55`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/c37ae55) [`52ea284`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/52ea284) ([#89](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/issues/89))
- **LoKr with block swap** keeps the blocks out of VRAM while the model is built: at small VRAM profiles LoKr uploaded the whole model first (Krea 2 ran out of VRAM, FLUX.1 planned 0 of 57 blocks in VRAM). Applies to FLUX.1, FLUX.2 Klein 9B, Fibo 2.0, Ideogram 4, Ming-Image, Wan 2.2 and Krea 2 [`31435cb`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/31435cb)

**2026-11-19**

- **FLUX.1 Dev, Fibo 2.0, Ideogram 4, Ming-Image, Wan 2.2, LTX-2.3 and Boogu from 8 GB of VRAM** — the block swap and **VRAM Profile** of Klein 9B, with the same results. Wan 2.2 also trains 480p clips on 8 GB and switches experts more than twice as fast ([details](#flux2-klein-9b--image-and-edit-loras)) [`9e4b126`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/9e4b126) [`16b0258`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/16b0258) [`3e06b88`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/3e06b88) [`8d61581`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/8d61581) [`1a95d86`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/1a95d86) [`c48468b`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/c48468b) [`9478139`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/9478139)
- **FLUX.2 Klein 9B from 8 GB of VRAM** — block swap and **VRAM Profile** as in LTX 2.5: edit LoRAs at 1024² peak at 5.8 GB instead of 11.5 GB, with the same results and a few % slower. If a step runs out of VRAM, it moves 2 more blocks to RAM and goes on. In Klein 9B and LTX 2.5 the profile now also counts the VRAM your other apps already use ([details](#flux2-klein-9b--image-and-edit-loras)) [`555de89`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/555de89) [`001624e`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/001624e) [`95c6879`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/95c6879)

**2026-11-18**

- **Up to 4 custom prompts per preview round, in every trainer** — **Custom Prompts (0-4)** next to Caption Mode: each round makes one preview per prompt, or one with a random prompt. Prompts changed while training are encoded on CPU and the trainer switches to them (LTX and MiniMax-H3 encode them in Pre-Cache only). In edit trainers with several reference images, **One image per prompt** makes each prompt edit its own image. The preview viewer shows the prompt of each preview ([details](#-custom-prompts-in-the-previews)) [`589c917`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/589c917) ([#87](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/issues/87))

**2026-11-17**

- **LTX 2.5: half the RAM and Block Swap Storage** — video previews no longer crash the training, and blocks can wait in **RAM**, on **Disk** or in **Auto (RAM + Disk)** with a **RAM Limit**, as in MiniMax-H3 ([details](docs/README_LTX25.md#block-swap-storage-ram-disk-or-auto)) [`429e04f`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/429e04f) [`d4c206a`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/d4c206a) [`dc854e9`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/dc854e9) [`c27a2a7`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/c27a2a7)
- **LTX 2.5: DoRA with any VRAM Profile**, down to 8 GB ([details](docs/README_LTX25.md#dora)) [`b158852`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/b158852) [`42e9f3a`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/42e9f3a)
- <img src="https://img.shields.io/badge/NEW%20TRAINER-ff2d55?style=for-the-badge" alt="NEW TRAINER" height="22"> **LTX 2.5: image, video, video + audio and edit (IC-LoRA) LoRAs, from 8 GB of VRAM** — images, clips and audio in one dataset, video previews with sound, and LoRAs that load in ComfyUI ([details](#ltx-25--image-video-video--audio-and-edit-loras)) [`bb8d867`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/bb8d867) [`b26c7a9`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/b26c7a9) [`79cec3d`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/79cec3d) [`c2b3589`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/c2b3589) [`c5c3a07`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/c5c3a07)
- **Number fields reject meaningless values** — a negative Batch Size or a Grad Accum of 0 made the training fail at the first step. In all trainers, a value below the minimum goes up to it when you leave the field, and an empty one goes back to its initial value. The Pre-Cache and training scripts apply the same limits when they load their settings, so a hand-edited or old json gets them too, with a note in the console [`df7fc19`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/df7fc19)
- New launcher image [`c074d6b`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/c074d6b)

**2026-11-16**

- **LTX 2.3 trains LTX-2.3, not LTX-2.5** — the launcher card, this README and the technical notes said it also worked with LTX-2.5. Its LoRAs usually load in LTX-2.5 (same layers and LoRA key names), but it trains the 2.3 weights: LTX-2.5 retrains the transformer and uses Gemma 4 as text encoder instead of Gemma 3 [`725c0fa`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/725c0fa)
- **Precision selector for older GPUs** — RTX 20, Quadro RTX and GTX 16 cards have no BF16 in hardware and trained several times slower with it. 17 trainers get an **Auto / BF16 / FP16** selector, and **Auto** trains in FP16 on those cards and in BF16 on RTX 30 or newer, with the same loss and previews: Krea 2, Qwen-Image 2.1, FLUX.1 Dev, FLUX.2 Klein 9B, FLUX.3 Image Klein, Ideogram 4, MOSS-Image, Fibo 2.0, ERNIE-Image, Boogu, Wan 2.2, LTX 2.3, Z-Image, Ming-Image, Anima, SDXL and YuE 2 (in Anima, SDXL and YuE 2 it is called **Compute**, since their **Precision** already chooses NF4 or BF16 for the model). With FP16 the loss is scaled so small gradients are not lost, and the model stays in 4 bits. Where a model overflowed in FP16, the trainer rescales its activations right before the norms that read them, so the result is the same: the attention and MLP in Z-Image and Ming-Image (plus their last MLP layer in FP32), and the whole residual stream in ERNIE-Image, Anima and FLUX.3 Image Klein. Qwen-Image 2512 and MiniMax-H3 Image keep training in BF16. Also: LTX 2.3 no longer fails to start without a project name [`a8844b7`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/a8844b7) [`7df3cfb`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/7df3cfb) [`3d64a05`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/3d64a05) [`b082f75`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/b082f75) [`a9387b5`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/a9387b5) [`d5f3e7a`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/d5f3e7a) [`7caa8bb`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/7caa8bb)
- **ERNIE-Image previews at the right size** — Preview Size (area) made previews of about 8000 px that ran out of VRAM, and an explicit width and height came out at half size [`d5f3e7a`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/d5f3e7a)
- **DoRA NormFix** — a **NormFix** checkbox next to DoRA, on by default, in the 17 DoRA trainers. A DoRA trained on the 4-bit model could lose the likeness in ComfyUI even with good previews, because ComfyUI measures the layers on the full model; with NormFix the file is saved with the original model's sizes, and the likeness is the same as in the previews. The trainer downloads the small `dora_norms.safetensors` it needs (5–20 MB) before training if your model folder does not have it ([details](#️-lora-options-rslora-lora-dora-and-lokr)) [`3922b7e`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/3922b7e)

**2026-11-15**

- **A finished job as a template** — in the **History** of the queue page, the ⧉ button opens that job's trainer with the settings it trained with, in a copy of their own: change what you want, give it another Project Name and train again. Your trainer settings are not touched ([how it works](#-job-queue)) [`0b9fd27`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/0b9fd27) ([#84](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/issues/84))
- **DoRA in LTX 2.3 and Boogu** — the **DoRA** checkbox, now in 17 trainers. In LTX 2.3 it goes under rsLoRA / LoRA+; in Boogu under LoKr / Factor, and changing it starts a new training, like the rank or LoKr ([details](#️-lora-options-rslora-lora-dora-and-lokr)) [`7231939`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/7231939)
- **DoRA in 4 more trainers: ERNIE-Image, Fibo 2.0, Ideogram 4 and SDXL** — the same **DoRA** checkbox, now in 15 trainers. In Fibo 2.0 and Ideogram 4 the file follows ComfyUI's fused layers (qkv, to_kv, w13) like their LoRAs do. SDXL also trains DoRA on the resnet convolutions with *All* targets, and its file matches the original weights exactly in ComfyUI ([details](#️-lora-options-rslora-lora-dora-and-lokr)) [`f443b04`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/f443b04)
- <img src="https://img.shields.io/badge/MAJOR%20UPDATE-7c3aed?style=for-the-badge" alt="MAJOR UPDATE" height="22"> **DoRA in 11 trainers** — a **DoRA** checkbox under LoRA Rank / Alpha in Z-Image, FLUX.1 Dev, FLUX.2 Klein 9B, FLUX.3 Image Klein, Krea 2, Qwen-Image 2.1, Qwen-Image 2512, Ming-Image, MOSS-Image, Anima and Wan 2.2. Each layer also learns the size of every output row, apart from the usual LoRA: it often follows the dataset more closely at the same rank, with slower steps. It works with rsLoRA and LoRA+, and the file loads in ComfyUI like any LoRA, with `_dora` in its name. Trained and checked so far in Z-Image, MOSS-Image and FLUX.1 Dev ([details](#️-lora-options-rslora-lora-dora-and-lokr)) [`cf599ab`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/cf599ab)
- **Dataset Manager folds like the Training Chart** in every trainer: click its title to hide or show it (▶ / ▼), and the page remembers it. Closed, only the title with the image and caption counts stays [`64cba83`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/64cba83)

**2026-11-14**

- **Preview Every = 0 stays off** in every trainer: a saved 0 was replaced by the field's default when the trainer opened (50 in Fibo 2.0). The label now reads *Preview Every (0 = off)* and the **2b. Training Previews** header shows *every N steps* or *off*, also while collapsed [`b80d1f5`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/b80d1f5) ([#78](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/issues/78))
- **Start Training checks the pre-cache** in every trainer: with no pre-cache, or with images or captions added, edited, removed or renamed after it, it says so and offers **Pre-cache, then train** (or **Train with the old cache**); the training waits in the queue until its pre-cache finishes well ([how it works](#-job-queue)). MiniMax-H3 and MiniMax-H3 Image now re-encode the samples whose caption or image changed instead of skipping them [`22fbe63`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/22fbe63) ([#79](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/issues/79))
- <img src="https://img.shields.io/badge/MAJOR%20UPDATE-7c3aed?style=for-the-badge" alt="MAJOR UPDATE" height="22"> **MiniMax-H3 Image, edit LoRAs** — pairs `name_before` / `name_after` with the instruction in `name.txt`, packed as the official MiniMax-H3-Image edit pipeline does: the text encoder sees the before image as Picture 1 and the DiT gets it as a reference. Choose **LoRA Type → Edit** in the Pre-Cache panel. The edit pre-cache fits 16 GB by parking the language layers in RAM while the vision tower runs: ~0.7 s per pair instead of 30-46 s ([details](#minimax-h3-image--image-and-edit-loras---experimental)) [`565bfcc`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/565bfcc)
- **MiniMax-H3 Image: new defaults** from the first run with good likeness: LR 4e-4, rank 16 / alpha 32, constant with 50 warmup steps, 1500 steps. On a face dataset the previews averaged 45 % face match over the last 300 steps, with a best of 53.6 % [`4131db8`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/4131db8) [`0e54da5`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/0e54da5)
- **MiniMax-H3 Image: Preview LoRA Strength**, like the LoRA strength in ComfyUI, changeable while training [`a562106`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/a562106)
- **MiniMax-H3 Image: VRAM guard** measured on the step's real peak, so it no longer reports a full card that is not full; after 20 steps the log says how many more resident blocks fit [`f2dfbf4`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/f2dfbf4)
- New launcher image [`fffe716`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/fffe716)

**2026-11-13**

- <img src="https://img.shields.io/badge/NEW%20TRAINER-ff2d55?style=for-the-badge" alt="NEW TRAINER" height="22"> **MiniMax-H3 Image, image LoRAs (experimental)** — for the 6-step distilled MiniMax-H3-Image. The LoRA trains on MiniMax-H3-Image itself with a frozen de-distillation adapter that is not used when generating, downloaded by itself from `AcademiaSD/MiniMax-H3-Image-NF4-for-LoRA-Training`. On a face dataset it reached 40% face likeness at strength 1.0 and 44.5% at 1.3, against 28% when the LoRA is trained on the MiniMax-H3 video model and used on H3-Image. 1500 steps by default; Stop halts at once, and when the VRAM runs short training moves blocks back to RAM instead of slowing down. The LoRAs load in ComfyUI [`b608eeb`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/b608eeb) [`297fedc`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/297fedc) [`db7622b`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/db7622b)
- **MiniMax-H3: sharp previews** — image previews are decoded by the MiniMax-H3-Image VAE (only its 2.2 GB `vae/` folder, downloaded the first time), and the video VAE no longer leaves horizontal stripes, an orange cast or a broken grid on images and clips [`311008c`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/311008c) [`f3ce0e0`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/f3ce0e0)
- Captions in any encoding: `.txt` files saved by Notepad in the Windows code page no longer crash the pre-cache or show up empty (#71), from the Fibo 2.0 fix by [@Synergyart](https://github.com/Synergyart) [`350a410`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/350a410) [`9b9db6e`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/9b9db6e)
- `Install_Triton&SageAtten220.bat` is now `Install_Triton_SageAtten220.bat`: the `&` broke it when started from a terminal (#74) [`40008f5`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/40008f5)
- New cover images for every trainer card [`dbd1870`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/dbd1870)

**2026-11-12**

- Krea 2 LoKr: no more dtype error in the timestep embedding, and previews with the Turbo LoRA hook all 269 layers instead of 34 (also on Wan 2.2), by [@Synergyart](https://github.com/Synergyart) [`616d8d1`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/616d8d1) [`8d8a3bd`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/8d8a3bd)

**2026-11-04**

- <img src="https://img.shields.io/badge/NEW%20TRAINER-ff2d55?style=for-the-badge" alt="NEW TRAINER" height="22"> **FLUX.1 Dev, image LoRAs** — LoRA and LoKr on the transformer and T5-XXL in NF4, downloaded ready from `diffusers/FLUX.1-dev-bnb-4bit` with no token. 800 steps at 512² take about 16 minutes and peak at ~10 GB of VRAM on an RTX 5080 ([details](#flux1-dev--image-loras)) [`21965bb`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/21965bb)

**2026-11-03**

- **Wan 2.2 on 12 GB of VRAM**: the Pre-Cache has 448 x 448 and 480 x 480. At 448 x 448 (rank 8, both experts) training peaks at 10.4 GB, and 1-frame previews stay below that ([details](#wan-22-t2v-a14b--video-and-image-loras-high--low-noise)) [`e95a6ef`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/e95a6ef)
- Launcher: the browser opens once the launcher is ready, without the error page first, and a trainer opens about 1.3 s sooner [`1dcb7f1`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/1dcb7f1)

**2026-11-02**

- **Dataset Forge: a character dataset from a few images, even one** — 🧬 in the Dataset Manager opens it: it captions the references, writes a character sheet, plans outfits, places and framings, and generates them with FLUX.3 Klein (or Fibo 2.0 / Qwen-Image 2.1 / FLUX.2 Klein 9B / Qwen-Image-Edit-2511), keeping only the images that pass the face likeness ([details](#-dataset-forge))
- **Face likeness in the previews**: a % on each preview and on the training chart, how much its face looks like the dataset's. Optional and off by default: the InsightFace models (non-commercial research only) are downloaded only after accepting their terms in a popup ([details](#-face-likeness-in-the-previews)) [`f0a45e2`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/f0a45e2)
- <img src="https://img.shields.io/badge/NEW%20TRAINER-ff2d55?style=for-the-badge" alt="NEW TRAINER" height="22"> **Wan 2.2 T2V-A14B, video and image LoRAs for the high noise and/or low noise expert** — images and clips in the same dataset, the experts in NF4 (downloaded ready from `AcademiaSD/Wan22-T2V-A14B-NF4-for-LoRA-Training`, or converted on your PC shard by shard), image and video previews with both experts and the lightx2v turbo LoRA (12 steps, ~2 min for a 1 s clip), and one LoRA per expert (`_high_noise` / `_low_noise`) for ComfyUI ([details](#wan-22-t2v-a14b--video-and-image-loras-high--low-noise)) [`d2be150`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/d2be150) [`7b2f238`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/7b2f238) [`591152c`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/591152c)

**2026-10-31**

- <img src="https://img.shields.io/badge/MAJOR%20UPDATE-7c3aed?style=for-the-badge" alt="MAJOR UPDATE" height="22"> **Job queue: queue trainings and pre-caches of any trainer, even several of the same model, and they run one after another on the GPU** — a queue page to reorder, pause, resume or remove jobs and jump to the one training; Start asks *Add to queue?* while something trains; *New training for the queue* prepares the next one while the current one trains; *Pause all and exit* in the launcher, also on RunPod and other clouds; a failed job stays in the list saying why; **✎** edits a waiting job ([how it works](#-job-queue)) [`d7bc99e`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/d7bc99e) [`e0089ae`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/e0089ae) [`94ecc4f`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/94ecc4f) [`9bf31bf`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/9bf31bf) [`2468e99`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/2468e99)

**2026-10-25**

- **MOSS-Image edit LoRAs on armV5**: the latest [MOSS-Image-Edit-HQ](https://huggingface.co/akhaliq/MOSS-Image-Edit-HQ) is the default edit base now, with armV4 and chinoll's as options [`ab231b1`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/ab231b1)
- **MOSS-Image edit LoRAs on armV4**: [akhaliq's MOSS-Image-Edit-HQ](https://huggingface.co/akhaliq/MOSS-Image-Edit-HQ) is the new default edit base (it keeps the unedited parts of the image), with chinoll's as an option; the fused export is a normal LoRA ending in `_FUSED`, for ComfyUI's own edit nodes [`4709970`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/4709970)

**2026-10-24**

- **MOSS-Image edit LoRAs**: before → after pairs trained on top of [chinoll's Moss-Image-Edit](https://huggingface.co/chinoll/Moss-Image-Edit), with edit previews, exported alone or fused with Moss-Image-Edit into one patch for ComfyUI [`a2f78ef`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/a2f78ef)
- **Training chart in 3D**: a terrain of the loss, from the loss of each step to the smoothed trend, that you can rotate [`f8d4f9f`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/f8d4f9f)
- Saved LoRAs on the chart at their step: click one to download it or send it to your models folder to test it [`5bad871`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/5bad871)
- **Training chart**: a live loss chart under the console in every trainer, with markers for previews and checkpoints. Closed by default, it costs nothing until opened [`7b665b1`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/7b665b1)
- AMD: VRAM read through ADLX on Windows and AMD GPUs listed in the GPU selector, by [@0xDELUXA](https://github.com/0xDELUXA) [`674447e`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/674447e)

**2026-10-23**

- Upload the trained LoRAs to Hugging Face [`e2abfa8`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/e2abfa8)

**2026-10-22**

- YuE2-3B marked as beta: AR is the default stage (it is the one that clones the voice) and the LoRA files carry their stage, `_AR` / `_NAR` [`77c9825`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/77c9825) [`a8c0699`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/a8c0699)
- MOSS-Image frees the CUDA cache when training fills the VRAM [`f39a4cd`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/f39a4cd)

**2026-10-21**

- <img src="https://img.shields.io/badge/NEW%20TRAINER-ff2d55?style=for-the-badge" alt="NEW TRAINER" height="22"> **YuE2-3B, song LoRAs, with an AR regularizer and fixed NAR conditioning** [`ba65373`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/ba65373) [`f76b32c`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/f76b32c)
- <img src="https://img.shields.io/badge/NEW%20TRAINER-ff2d55?style=for-the-badge" alt="NEW TRAINER" height="22"> **Fibo 2.0 (BRIA), experimental, with the NF4 model downloaded from Hugging Face** [`951f22f`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/951f22f) [`a73d437`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/a73d437)
- Launcher cards laid out evenly and responsively [`5c94e0a`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/5c94e0a)
- Fixes: the Browse folder dialog [`28fc9b5`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/28fc9b5), the Fibo 2.0 pre-cache on large images [`42a08e0`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/42a08e0), training options the interface does not send are kept [`152f270`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/152f270)

**2026-10-20**

- <img src="https://img.shields.io/badge/NEW%20TRAINER-ff2d55?style=for-the-badge" alt="NEW TRAINER" height="22"> **Ming-Image Design, image and edit LoRAs for transparent designs; Save JSON lists the settings changed live** [`678554b`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/678554b) [`aa3a2f0`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/aa3a2f0)

**2026-10-19**

- Models, caches and outputs organized into `Models/`, `Cache_Data/` and `Outputs/`, with automatic migration [`078151d`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/078151d) [`14f942e`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/14f942e)
- LoRAs exported with normal file permissions [`4834fb4`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/4834fb4)

**2026-10-18**

- <img src="https://img.shields.io/badge/NEW%20TRAINER-ff2d55?style=for-the-badge" alt="NEW TRAINER" height="22"> **Qwen-Image 2512 / Edit 2511** [`a24d45d`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/a24d45d)
- <img src="https://img.shields.io/badge/NEW%20TRAINER-ff2d55?style=for-the-badge" alt="NEW TRAINER" height="22"> **Boogu Image Edit 0.1, with live settings and a preview size** [`5e8d055`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/5e8d055) [`7013c61`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/7013c61)
- rsLoRA and LoRA+ in LTX-2.3 and MiniMax-H3 [`2e2a653`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/2e2a653)
- Edit previews with several ordered reference images [`69e3945`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/69e3945) [`f6d9efc`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/f6d9efc)

**2026-10-17**

- <img src="https://img.shields.io/badge/NEW%20TRAINER-ff2d55?style=for-the-badge" alt="NEW TRAINER" height="22"> **MOSS-Image** [`7e485ac`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/7e485ac)
- Tour video in the README [`afdf44c`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/afdf44c)

**2026-10-16**

- <img src="https://img.shields.io/badge/NEW%20TRAINER-ff2d55?style=for-the-badge" alt="NEW TRAINER" height="22"> **FLUX.3 Image Klein, with its NF4 converter and captions in BFL's own formats** [`b860ae5`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/b860ae5) [`1f96b77`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/1f96b77) [`52deaa7`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/52deaa7)
- Before/after datasets train as edit LoRAs even with LoRA Type normal [`a5dbf92`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/a5dbf92)
- The updater reinstalls URL-pinned packages when their URL changes [`ea6c0b5`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/ea6c0b5)

**2026-10-15**

- Launcher: a running training is never cut when switching trainers, and going back works behind a proxy [`43da9a8`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/43da9a8) [`4ea74e2`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/4ea74e2)

<details>
<summary><b>Earlier changes (2026-09-28 to 2026-10-14)</b></summary>

**2026-10-14**

- Trainers open in the launcher tab, with a back button, a glow on the one that is training and trainer switching [`4ed40ad`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/4ed40ad)
- Windows 11 24H2: trainers are detected without `wmic` [`5432f33`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/5432f33)

**2026-10-12**

- LR scheduler selector in every trainer [`f8b2489`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/f8b2489)
- GPU selector in the launcher [`07d2934`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/07d2934)

**2026-10-09**

- Mobile layout for the trainer interfaces and an Upload button for the edit preview image [`59817f3`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/59817f3)
- Failed uploads highlighted with a retry, and LoRA downloads named after the project [`8dd6154`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/8dd6154)
- Visual RefMods keep their source pictures [`8dc926a`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/8dc926a)

**2026-10-08**

- **Experimental AMD (ROCm) support**: installers for Windows and Linux [`b8742cf`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/b8742cf)
- Fix stale or mixed training previews [`4fc1fb6`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/4fc1fb6)

**2026-10-06**

- <img src="https://img.shields.io/badge/NEW%20TRAINER-ff2d55?style=for-the-badge" alt="NEW TRAINER" height="22"> **ERNIE-Image** [`4067e13`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/4067e13)
- rsLoRA, LoRA+ and LoKr in the image trainers, with the option in the LoRA file name [`c46e4ee`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/c46e4ee) [`7e3a800`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/7e3a800)
- Training keeps running when the browser is closed, per-file upload results and non-blocking notifications, by [@Synergyart](https://github.com/Synergyart) [`d350cca`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/d350cca)

**2026-10-05**

- **Translations**: the launcher, the trainers and their consoles in Spanish, German, French, Italian, Portuguese, Japanese and Korean [`c9676f3`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/c9676f3) [`e3b1b51`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/e3b1b51)
- Clear Dataset button in every trainer [`0acfcf5`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/0acfcf5)
- The updater updates the current branch and shows the new commits [`e7aef0d`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/e7aef0d) [`b82291d`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/b82291d)

**2026-10-04**

- <img src="https://img.shields.io/badge/NEW%20TRAINERS-ff2d55?style=for-the-badge" alt="NEW TRAINERS" height="22"> **SDXL (Pony, Illustrious, NoobAI, Juggernaut and RealVis presets) and Ideogram 4 (JSON captions)** [`12822e8`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/12822e8) [`6703a8c`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/6703a8c)
- Password-protected remote access, configured from the launcher [`b786483`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/b786483) [`f12e412`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/f12e412)
- Dataset upload and LoRA download from the browser [`af53a9d`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/af53a9d)
- RunPod: Docker image and Deploy button [`de5bb82`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/de5bb82) [`64f7928`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/64f7928)
- `requirements.txt` and `LORALAB_PYTHON` to use your own Python environment [`a7c232a`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/a7c232a)

**2026-10-03**

- <img src="https://img.shields.io/badge/NEW%20TRAINERS-ff2d55?style=for-the-badge" alt="NEW TRAINERS" height="22"> **Z-Image, Anima (BF16 or NF4) and FLUX.2 Klein 9B** [`385871e`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/385871e) [`0c30cd1`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/0c30cd1) [`6cb669c`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/6cb669c)
- **Linux support**, by [@jonathanhecl](https://github.com/jonathanhecl) [`60ecb9c`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/60ecb9c)

**2026-10-01**

- README rewritten as a self-contained guide for the public release [`21b5ce7`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/21b5ce7)

**2026-09-30**

- Renamed to AcademiaSD LoRAlab Trainer Studio [`c8705f4`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/c8705f4)

**2026-09-29**

- LoRA export folder shared by all the trainers and settings in two columns [`89f68ad`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/89f68ad) [`db773a2`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/db773a2)

**2026-09-28**

- <img src="https://img.shields.io/badge/FIRST%20VERSION-6366f1?style=for-the-badge" alt="FIRST VERSION" height="22"> **Krea 2, LTX-2.3, MiniMax-H3 and Qwen-Image 2.1, one Python environment and a common launcher** [`72189d7`](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio/commit/72189d7)

</details>

---

https://github.com/user-attachments/assets/8f3b6d3f-dbd5-45a4-8ae5-028e241c449a

<p align="center">
  <b>Train LoRAs for the latest image and video models on consumer NVIDIA GPUs (and AMD, experimental) — from 8 GB of VRAM.<br>
  One installation, one Python environment, one launcher. Every trainer in one place.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Windows-10%20%7C%2011-blue.svg" alt="Windows">
  <img src="https://img.shields.io/badge/Linux-supported-yellow.svg" alt="Linux">
  <img src="https://img.shields.io/badge/GPU-NVIDIA%20RTX%2020xx%2B-green.svg" alt="NVIDIA">
  <img src="https://img.shields.io/badge/GPU-AMD%20RX%207000%20%7C%209000%20(experimental)-red.svg" alt="AMD (experimental)">
  <img src="https://img.shields.io/badge/Python-3.13-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/PyTorch-2.14%20cu130-orange.svg" alt="PyTorch">
  <img src="https://img.shields.io/badge/UI-Flask%20%2B%20HTML5-purple.svg" alt="Web UI">
  <img src="https://img.shields.io/badge/Languages-8-teal.svg" alt="8 languages">
  <a href="https://console.runpod.io/deploy?template=lfxvtg5rrb&ref=jbvdshm0"><img src="https://img.shields.io/badge/Deploy%20on-RunPod-673ab7.svg" alt="Deploy on RunPod"></a>
</p>

> 🧪 **Aviso:** se ha añadido soporte a muchos modelos de forma casi simultánea. Es posible que haya bugs, ajustes pendientes o que las configuraciones de entrenamiento y de previsualización por defecto no sean las adecuadas. Por favor, escribe en [Issues](../../issues) contando los problemas que encuentres o los ajustes con los que has conseguido mejores resultados. ¡Gracias!
>
> Las previsualizaciones no tienen por qué tener la calidad del LoRA final: sirven para seguir la evolución del entrenamiento y el parecido del personaje, objeto o estilo. La calidad final del LoRA compruébala en su interfaz (ComfyUI, Forge...), después de ajustar la fuerza del LoRA y con los ajustes de calidad del modelo que uses.
>
> 🧪 **Notice:** support for many models has been added almost at the same time. There may be bugs or rough edges, or the default training and preview settings may not be the right ones. Please open an [issue](../../issues) with the problems you find or the settings that gave you better results. Thank you!
>
> The previews do not have to reach the quality of the final LoRA: they are there to follow the training and the likeness of the character, object or style. Judge the final quality in the matching interface (ComfyUI, Forge...), after adjusting the LoRA strength and with the quality settings of the model you use.

**AcademiaSD LoRAlab Trainer Studio** brings together all the AcademiaSD LoRAlab trainers. Each model is loaded in **4-bit NF4**, the text encoder and the VAE run only once in a **pre-cache** stage, and 100 % of the GPU goes to training. Every trainer has the same web interface: dataset manager with an automatic captioner, live previews, exact-step resume and one-click export to ComfyUI. It also works from another device on your network: upload the dataset and download the LoRA from the browser.

New trainers are added **here**. One `Update_LoRAlab-TrainerStudio.bat` brings them to your existing installation, next to your models and projects — no new repository, no new environment.

| Trainer | Trains | Minimum VRAM |
| :--- | :--- | :--- |
| **Fibo 2.0** *(experimental)* | Image LoRAs (characters, objects, styles) **and edit LoRAs** (before → after) on BRIA Fibo 2.0 Dev | **8 GB** with block swap (5.3 GB peak with image LoRAs at 768², measured) |
| **Qwen-Image 2.1** | Image LoRAs (characters, objects, styles) **and edit LoRAs** (before → after) | 8 GB |
| **Qwen-Image 2512 / Edit 2511** | Image LoRAs on Qwen-Image-2512 **and edit LoRAs** on Qwen-Image-Edit-2511 (before → after); 20B in NF4 with block swap | **~4 GB** (512², measured) / 8 GB (edit at 1024²) |
| **Krea 2** | Image LoRAs (characters, objects, styles) for Krea 2 Raw and Turbo | **8 GB** with block swap (5.2 GB peak with previews at ~640×416, 4.2 GB at 1024², measured) |
| **Boogu Image Edit 0.1** | Edit LoRAs (before → after) and image LoRAs on Boogu-Image-0.1-Edit | **8 GB** with block swap (5.5 GB peak with edit LoRAs at 512², measured) |
| **Z-Image** | Image LoRAs (characters, objects, styles) for Z-Image and Z-Image-Turbo | 8 GB |
| **Ming-Image** *(experimental)* | Image LoRAs for transparent designs and edit LoRAs (before → after) on inclusionAI's Ming-Image 0.1 Design | **8 GB** with block swap (5.8 GB peak at 1024², measured) |
| **Anima** | Anime and illustration LoRAs (characters, styles) | **4 GB** (NF4) / 6 GB (BF16) |
| **Anima 2.9B** *(preview)* | Anime and illustration LoRAs (characters, styles) on Anima-2.9B, the 40-block Anima | **Under 6 GB** (NF4 at 512², measured) |
| **ERNIE-Image** | Image LoRAs (characters, objects, styles); supports rsLoRA, LoRA+ and LoKr | **Under 8 GB** (NF4; verified during training) |
| **FLUX.1 Dev** | Image LoRAs (characters, objects, styles) | **8 GB** with block swap (5.0 GB peak at 512², measured) |
| **FLUX.2 Klein 9B** | Image LoRAs (characters, objects, styles) **and edit LoRAs** (before → after) | **8 GB** with block swap (6.0 GB peak at 768², 5.8 GB with edit LoRAs at 1024², measured) |
| **FLUX.3 Image Klein** | Image LoRAs (characters, objects, styles) **and edit LoRAs** (before → after) | 8 GB |
| **MOSS-Image** | Image LoRAs (characters, objects, styles) on MOSS-Image Base or SFT **and edit LoRAs** (before → after, on top of armV5, armV4 or Moss-Image-Edit); supports rsLoRA, LoRA+ and LoKr | **6 GB** (512²) / 8 GB |
| **Ideogram 4** | Image LoRAs (characters, objects, styles), with JSON captions | **8 GB** with block swap (6.4 GB peak at 1024² with CFG previews, measured) |
| **SDXL** | Image LoRAs for SDXL Base, Pony, Illustrious, NoobAI, Juggernaut, RealVis or your own SDXL checkpoint | **4 GB** (NF4) / 12 GB (BF16) |
| **LTX 2.5** | Image LoRAs, video LoRAs from clips, **video + audio** LoRAs and **edit IC-LoRAs** (before → after), on LTX-2.5; block swap | **8 GB** |
| **LTX-2.3** | Character and style LoRAs for LTX-2.3, trained from images (they usually load in LTX-2.5 too) | **8 GB** with block swap (5.2 GB peak at 768², measured) |
| **MiniMax-H3** | Video LoRAs from images, clips and audio, plus training-free **RefMods** | 8 GB |
| **MiniMax-H3 Image** *(experimental)* | Image LoRAs (characters, objects, styles) **and edit LoRAs** (before → after) on the 6-step distilled MiniMax-H3-Image, trained with a de-distillation adapter; 33B in NF4 with block swap | 8 GB (image LoRAs) / 10 GB (edit LoRAs), estimated from the VRAM plan with Resident Blocks on 0 |
| **Wan 2.2 (T2V-A14B)** | Video and image LoRAs from images and clips, for the **high noise** and/or **low noise** expert | **8 GB** with block swap (5.2 GB peak with images or 17-frame clips at 480p, both experts; 5.7 GB with a video preview, measured) |
| **YuE2-3B** *(experimental / beta)* | Song LoRAs: the AR clones the singer's voice, the NAR learns lyrics and phrasing | ~8 GB (NF4, measured on NAR) |

---

## 🇪🇸 Guía rápida en español

1. **Instalar:** en la carpeta donde quieras instalarlo, escribe `cmd` en la barra de direcciones del explorador y ejecuta
   `git clone https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio.git`
   (o descarga el ZIP desde el botón verde **Code → Download ZIP** y descomprímelo). Después, doble clic en **`Install_LoRAlab-TrainerStudio.bat`**: instala Git si no lo tienes, Python 3.13.1 y un único entorno `venv` para todos los entrenadores. Con GPU AMD usa **`Install_LoRAlab-TrainerStudio_AMD.bat`** (experimental; confirmado con una RX 7800 XT en Windows y MiniMax-H3).
2. **Abrir:** doble clic en **`Start_LoRAlab-TrainerStudio.bat`** y pulsa la tarjeta del entrenador que quieras. Mientras uno entrena, pulsar otra tarjeta la abre en otro puerto para preparar un trabajo de la cola.
3. **Entrenar:** nombre del proyecto → carpeta del dataset → *Crear Captions* (opcional) → *Iniciar Pre-Caché* → *Iniciar / Reanudar* → *Send to Models*. El modelo se descarga solo la primera vez.
4. **Actualizar:** doble clic en **`Update_LoRAlab-TrainerStudio.bat`**. Se conservan tus modelos, proyectos y ajustes, los nuevos entrenadores aparecen en el lanzador y se instalan las librerías nuevas que hagan falta.
5. **Desde otro equipo:** el botón **🌐 Remote access** del lanzador abre el entrenador a tu red con usuario y contraseña. Con **⬆ Subir** (o arrastrando archivos o un `.zip` al Dataset Manager) mandas el dataset desde ese equipo, y con **⬇ Descargar LoRA** te bajas el resultado.
6. **Previsualizaciones nítidas en ComfyUI:** algunos de estos modelos son lentos al generar, y conviene ver el resultado de forma anticipada, mientras se genera, para cancelar si no va bien. Para eso hace falta una buena previsualización. Mi recomendación: al usar tus LoRAs de Qwen-Image 2.1, Krea 2 o FLUX.2 / Klein 9B, pon el nodo **Model Preview Override** de [KJNodes](https://github.com/kijai/ComfyUI-KJNodes) con el TAE de AcademiaSD correspondiente ([Qwen-Image 2.1](https://huggingface.co/AcademiaSD/TAE-Qwen-Image-2.1) · [Krea 2](https://huggingface.co/AcademiaSD/TAE-Krea-2) · [FLUX.2](https://huggingface.co/AcademiaSD/TAE_Flux2_AcademiaSD)) en `ComfyUI/models/vae_approx/`. Detalles en la sección *Sharp previews in ComfyUI*.
7. **Sin GPU potente:** entrena en la nube con **[RunPod](https://console.runpod.io/deploy?template=lfxvtg5rrb&ref=jbvdshm0)**. Es una plantilla ya preparada: eliges una GPU con CUDA 13, entras con el usuario `loralab` y la contraseña que aparece en *Logs → Container*, y al terminar paras y borras el pod. Detalles en la sección *RunPod*.
8. **Requisitos:** Windows 10/11, GPU NVIDIA **RTX 20xx / GTX 16xx o posterior** con driver **580 o superior** (o AMD **RX 7000 / RX 9000** de 16 GB, experimental), 8 GB de VRAM (4 GB para Anima y SDXL en NF4, 12 GB para SDXL en BF16) y 16 GB de RAM (32 GB recomendados).

**Cola de trabajos:** con un entrenamiento en marcha, *Iniciar / Reanudar* o *Iniciar Pre-Caché* en cualquier entrenador pregunta si añadirlo a la cola, con una copia de los ajustes de ese momento. Los trabajos se ejecutan uno tras otro en la GPU. El botón **Cola** del lanzador y de cada entrenador abre la página de la cola: lo que entrena ahora (progreso, tiempo restante y curva de loss) y lo que espera, que puedes reordenar arrastrando, pausar, continuar o quitar. Pausar guarda un checkpoint y deja el trabajo pausado en la cola; continuar sigue desde ese paso. Mientras un entrenador entrena, **➕ Nuevo entrenamiento en cola** abre un borrador del mismo entrenador en otro puerto para preparar el siguiente sin tocar el que entrena (ponle otro nombre de proyecto). Si un trabajo falla, se queda en la lista en rojo diciendo por qué (no se encuentra la pre-caché o el dataset, falta VRAM…); corrígelo y pulsa **↻** para reintentarlo. **✎** en un trabajo de la cola abre su entrenador con sus ajustes para cambiarlos: el botón de empezar pasa a ser **💾 Guardar cambios en la cola**. Mientras se hace la pre-caché, *Iniciar / Reanudar* sigue disponible y manda el entrenamiento a la cola. **⏻ Pausar todo y salir**, abajo en el lanzador, pausa el entrenamiento en curso guardando su checkpoint y cierra todo desde el navegador; al volver a abrir el lanzador la cola sigue sola donde estaba, empezando por ese entrenamiento. En RunPod y otras nubes el lanzador sigue abierto, con la cola pausada.

**Linux:** ya tiene soporte para Linux. Cada `.bat` tiene su `.sh` equivalente; la instalación y el uso están en [docs/Linux.md](docs/Linux.md). Gracias a **[Jonathan Hecl (@jonathanhecl)](https://github.com/jonathanhecl)** por aportarlo.

**LTX 2.5:** nuevo entrenador para **LTX-2.5** de Lightricks con cuatro tipos de LoRA: de imagen (personajes, estilos), de vídeo a partir de clips (movimientos, efectos), de **vídeo + audio** (**Train Audio**) y de **edición IC-LoRA** (pares `nombre_before` / `nombre_after`, de imágenes o clips). Funciona **desde 8 GB de VRAM** con block swap; **VRAM Profile** simula tarjetas menores. Con clips, pulsa primero **Prepare clips** (24 fps y 8n+1 fotogramas sin recortar el final). Las previews de clips salen en `.mp4` con el sonido generado. Descarga `AcademiaSD/LTX25-NF4-for-LoRA-Training` (26,3 GB) la primera vez. Detalles en la sección *LTX 2.5* y en [docs/README_LTX25.md](docs/README_LTX25.md).

**FLUX.1 Dev:** nuevo entrenador de LoRAs de imagen para **FLUX.1 [dev]** de Black Forest Labs (FLUX.1 [dev] Non-Commercial License). Se descarga ya en **NF4** (13,5 GB, sin token) y los dos text encoders solo se usan en el pre-caché. Detalles en la sección *FLUX.1 Dev*.

**MiniMax-H3 Image:** nuevo entrenador (experimental) de LoRAs de imagen y de edición (antes → después) para **MiniMax-H3-Image**, el modelo de imagen destilado a 6 pasos. El LoRA se entrena sobre el propio H3-Image con un adaptador de des-destilación congelado, que no se usa al generar. Para editar, elige **LoRA Type → Edit** en el panel de Pre-Cache y usa pares `nombre_before` / `nombre_after` con la instrucción en `nombre.txt`, por ejemplo `Edit <Picture 1>. Make it TOSTIOK style.`. El pre-caché de edición cabe en 16 GB porque aparca las capas de lenguaje en la RAM mientras corre la torre de visión. Detalles en la sección *MiniMax-H3 Image*.

**FLUX.3 Image Klein:** nuevo entrenador de LoRAs normales y de edición (antes → después) para FLUX.3 Image Klein Base, desde 8 GB de VRAM. El captioner escribe en los formatos propios de FLUX.3 (prosa detallada, y opcionalmente con tabla de cajas `<id>`; en edición, la instrucción con `<ref_image_0>`). Necesita la versión nueva de diffusers: ejecuta **`Update_LoRAlab-TrainerStudio.bat`** antes de abrirlo. Detalles en la sección *FLUX.3 Image Klein*.

**Fibo 2.0:** nuevo entrenador de LoRAs de imagen y de edición (antes → después) para **Fibo 2.0 Dev** de BRIA (8,1 B, CC BY-NC 4.0, uso no comercial). El transformador va en **NF4** (5,2 GB de VRAM) y el text encoder (Qwen3-VL-4B) solo se usa en el pre-caché. Necesita la versión nueva de diffusers (con `BriaFibo2Pipeline`): ejecuta **`Update_LoRAlab-TrainerStudio.bat`** antes de abrirlo. Detalles en la sección *Fibo 2.0*.

**Ming-Image:** nuevo entrenador de LoRAs de imagen y de edición (antes → después) para **Ming-Image 0.1 Design** de inclusionAI, el modelo que genera el canal alfa: los diseños transparentes. El captioner escribe los captions en el JSON estilo Figma del propio modelo. El "text encoder" es un MLLM completo (BailingMoE-V2 + ViT) en NF4. La tarea oficial de edición trabaja a 1024. Detalles en la sección *Ming-Image*.

**MOSS-Image:** nuevo entrenador de LoRAs de imagen para MOSS-Image de OpenMOSS (Apache 2.0), sobre **Base** (el recomendado para LoRAs) o **SFT**, con la misma pre-caché para los dos. Entrena a 512² con menos de 6 GB de VRAM. El text encoder (Qwen3.5-9B) se elige en el pre-caché: BF16 exacto repartido entre GPU y RAM (por defecto), INT8 o NF4. Las previews pueden usar el adaptador turbo de 4 pasos de darask0 (unos 4 s por imagen en vez de 43 s). Detalles en la sección *MOSS-Image*.

**Wan 2.2:** nuevo entrenador de LoRAs de vídeo e imagen para **Wan 2.2 T2V-A14B** (Apache 2.0), con imágenes y clips en el mismo dataset. Wan 2.2 tiene dos expertos de 14B: el de **ruido alto** (composición y movimiento) y el de **ruido bajo** (detalle, caras, estilo). *Experto a entrenar* elige cuál aprende: ruido bajo (basta para personajes y estilos), ruido alto (movimientos nuevos) o los dos (por defecto), con un LoRA para cada uno (`_high_noise` / `_low_noise`); en ComfyUI cada uno va en su modelo. Los expertos se descargan ya en NF4 (~7,6 GB cada uno) de `AcademiaSD/Wan22-T2V-A14B-NF4-for-LoRA-Training`; si ese repo aún no tiene uno, se descarga del original shard a shard (57 GB en FP32), se convierte a NF4 en tu PC y se borra cada shard. Las previews pueden usar el LoRA turbo lightx2v (12 pasos, unos 2 minutos por clip de 1 s). Desde 8 GB de VRAM con block swap: imágenes y clips de 17 fotogramas a 480p, con los dos expertos. Los clips necesitan **ffmpeg** en el PATH. Detalles en la sección *Wan 2.2*.

**Parecido facial:** encima de las previews, **👤 Parecido facial → Activar...** pone en cada preview (y sobre su círculo en la gráfica del entrenamiento) el % de parecido de su cara con la del dataset. En las previews de un LoRA, un 45% o más es mucho parecido (verde) y un 30-45%, parecido parcial (naranja); las fotos reales de la misma persona suelen dar más. También en las previews de vídeo, con su primer fotograma. No se descarga por defecto: los modelos de InsightFace son solo para investigación no comercial, y antes de descargarlos hay que aceptar en una ventana que se usan bajo tu responsabilidad y sin fines comerciales. Funciona en la CPU, también en RunPod. Detalles en la sección *Face likeness in the previews*.

**Prompts propios en las previews:** en **2b. Training Previews**, **Custom Prompts (0-4)** pone hasta 4 prompts tuyos: cada ronda de previews hace una imagen por prompt, o una sola con uno al azar (**One random prompt per preview**). Con 0 se usan las captions del dataset (Caption Mode). Los codifica el Pre-Cache; si los cambias durante el entrenamiento y pulsas **Save JSON**, se codifican en la CPU y el trainer pasa a usarlos (en LTX y MiniMax-H3 solo los codifica el Pre-Cache). En los entrenadores de edición con varias imágenes de referencia, **One image per prompt** hace que cada prompt edite su propia imagen. Al abrir una preview se ve el prompt con el que se hizo. Detalles en la sección *Custom prompts in the previews*.

**Dataset Forge:** con pocas fotos de una persona (desde 1), **🧬 Dataset Forge** en la barra del Dataset Manager crea un dataset de personaje. *Analizar* escribe los captions que falten y una ficha con los rasgos fijos (edad, pelo, ojos). El *plan* combina encuadre, ropa, lugar (mitad interiores, mitad exteriores), luz, ángulo y expresión, y se puede editar línea a línea. *Generar* usa FLUX.3 Klein (FLUX Kommunity License), con las imágenes más naturales: anatomía limpia, poses nuevas y el encuadre pedido. En calidad *Rápida* (por defecto) usa la LoRA turbo PDD de NoiseToNova: 4 u 8 pasos, unos 12 o 25 s por imagen, con más parecido pero un aspecto más maquillado; *Mejor calidad* va de 12 a 50 pasos (16, unos 85 s por imagen), más natural. También se puede elegir Fibo 2.0 (CC BY-NC, el de más parecido, unos 5 min por imagen), Qwen-Image 2.1 (licencia Qwen Research, no comercial; rápido, pero con cuerpos a veces desproporcionados), FLUX.2 Klein 9B o Qwen-Image-Edit-2511 (Apache 2.0). El plan reparte la mitad de las imágenes en primeros planos. Solo guarda las imágenes que pasan el parecido facial mínimo (60% por defecto); las demás van a `_rejected`. El resultado va a una carpeta nueva (la de origen no se toca), con un caption por imagen sin los rasgos fijos, para que el trigger aprenda la identidad. **📂 Usar en el Dataset Manager** la carga en el entrenador. Antes de generar hay que confirmar que tienes derecho o permiso para usar las imágenes de esa persona. Detalles en la sección *Dataset Forge*.

**Curva de LR nueva al reanudar:** la curva del LR cubre siempre todo el entrenamiento, del paso 0 a Total Steps. Si entrenas 1000 pasos con `cosine` de 4e-4 a 4e-5, subes Total Steps a 2000 y reanudas, el paso 1001 está a mitad de la curva de 2000 pasos y el LR vuelve a subir a ~2,3e-4. Con **New LR curve on resume** (debajo del LR Scheduler) la curva empieza de nuevo al reanudar: desde el LR que pongas hasta su mínimo en el último paso, sin warmup; por ejemplo, con LR 1e-4 los 1000 pasos siguientes van de 1e-4 a 1e-5. Detalles en la sección *LR scheduler*.

**LR Scheduler:** debajo del learning rate puedes elegir cómo cambia durante el entrenamiento: `cosine` (por defecto: sube durante el warmup y baja suavemente hasta el 10%), `constant` (el mismo LR de principio a fin, como el entrenador de Civitai), `constant_with_warmup`, `linear` o `cosine_with_restarts` (repite la curva tantas veces como indique *Ciclos*). Si no lo tocas, cada entrenador funciona igual que antes. Detalles en la sección *LR scheduler*.

**Idiomas:** la interfaz y los mensajes de consola están en inglés, español, alemán, francés, portugués, italiano, japonés y coreano. Elige el idioma en el selector **🌍 Language** de la parte inferior del lanzador y pulsa **💾 Save settings**; por defecto está en inglés. Los prompts de los captions siguen siempre en inglés, que es lo que entienden los modelos. Detalles en la sección *Languages*.

> ⚠️ **Sobre los valores por defecto:** las pruebas se han hecho para comprobar que cada entrenamiento funciona, no para buscar el mejor rendimiento ni la mejor calidad. Haz tus propias pruebas con distintas configuraciones (pasos, learning rate, rank, resolución, captions) para mejorar la calidad de tus LoRAs.

---

## 📉 Smaller downloads

Each trainer downloads **only what it uses**, already quantized. The table compares the official full-precision model, what the previous standalone LoRAlab downloaded, and what Trainer Studio downloads now (sizes from the Hugging Face repositories, in GB):

| Trainer | Official model | LoRAlab before | **Trainer Studio now** | What changed |
| :--- | ---: | ---: | ---: | :--- |
| **Krea 2** | 62.0 | 43.2 | **17.0** | The BF16 transformer (26.3 GB) is no longer downloaded or used: the model is built directly from its NF4 weights. |
| **LTX 2.5** | ~70 | — | **26.3** | New trainer: the full transformer (9.6 GB NF4 + 0.85 GB BF16), the Gemma 4 12B text encoder in NF4 (7.2 GB), connectors, VAEs and vocoder, from `AcademiaSD/LTX25-NF4-for-LoRA-Training`. The official Diffusers repo is gated; this one is not. |
| **LTX-2.3** | 101.3 | 111.1 | **32.2** | The BF16 transformer (38.0 GB) and the FP32 Gemma 3 text encoder (48.8 GB) are replaced by NF4 versions (9.8 GB + 7.8 GB). |
| **Qwen-Image 2.1** | ~32 (BF16) | 21.9 | **21.9 / 14.4 / 11.0** | Only the text encoder you pick is downloaded: BF16 (exact, default) / INT8 / NF4. |
| **MiniMax-H3** | 498.5 | 41.4 | **41.4** | The 33B model ships in NF4 from the start. |
| **MiniMax-H3 Image** | 204.0 | — | **38.4** | New trainer: the 33B transformer in NF4 (17.2 GB), its VAE (2.3 GB) and the de-distillation adapter (0.5 GB) from `AcademiaSD/MiniMax-H3-Image-NF4-for-LoRA-Training`, plus the Qwen3-VL text encoder in NF4 (18.4 GB) from the MiniMax-H3 NF4 repo. If MiniMax-H3 is already installed, the text encoder is not downloaded again (~20 GB). |
| **Z-Image** | 20.5 | — | **5.9** | New trainer: the 6B transformer (12.3 GB) and the Qwen3-4B text encoder (8.0 GB) in NF4 (3.4 GB + 2.7 GB). |
| **Anima** | 5.6 | — | **5.6** | New trainer: the official diffusers version of Anima-Base. The 2B model trains in BF16, or in NF4 quantized when loading (nothing extra to download). |
| **Anima 2.9B** | 5.8 (transformer only) | — | **7.3** | New trainer: the diffusers version of Anima-2.9B (`v2ray/Anima-2.9B-preview-v1-diffusers`), with its 40-block transformer (5.6 GB), its own LLM adapter, and the Qwen3-0.6B text encoder and VAE of Anima. It trains in BF16, or in NF4 quantized when loading. |
| **SDXL** | ~7 per model | — | **~7 per model** | New trainer: only the preset you pick is downloaded (one `.safetensors` file); your own checkpoint downloads nothing. |
| **Ideogram 4** | 16.1 (NF4) | — | **16.1** | New trainer: the official NF4 release, which includes the unconditional transformer used only by the previews. It is downloaded from Unsloth's ungated mirror (same weights, no license gate or token needed); the Ideogram license still applies. |
| **FLUX.1 Dev** | 33.7 | — | **13.5** | New trainer: the 12B transformer (23.8 GB) and the T5-XXL text encoder (9.5 GB) in NF4 (6.7 GB + 6.3 GB), from `diffusers/FLUX.1-dev-bnb-4bit`. |
| **FLUX.2 Klein 9B** | 34.7 | — | **8.8** | New trainer: the 9B transformer (18.2 GB) and the Qwen3-8B text encoder (16.4 GB) in NF4 (4.9 GB + 3.8 GB; only the 28 text encoder layers Klein reads). |
| **Qwen-Image 2512 / Edit 2511** | 57.8 each | — | **26.8 / 18.6 / 15.7** | New trainer: the 20B transformer of 2512 or Edit-2511 in NF4 (9.9 GB each; only the one you train on is downloaded) and the Qwen2.5-VL-7B text encoder you pick: BF16 (exact, default) / INT8 / NF4. The optional Lightning turbo LoRA adds 0.85 GB. |
| **MOSS-Image** | 27.2 | — | **20.2 / 13.2 / 9.9** | New trainer: the 5B transformer of Base or SFT in NF4 (3.1 GB each; only the one you train on is downloaded) and the Qwen3.5-9B text encoder you pick: BF16 (exact, default) / INT8 / NF4. The optional turbo preview adapter adds 1.2 GB. |
| **Wan 2.2 T2V-A14B** | 126.2 | — | **~19.5 / ~27** | New trainer: one expert / both, downloaded already in NF4 (~7.6 GB each) from `AcademiaSD/Wan22-T2V-A14B-NF4-for-LoRA-Training`. An expert that repo does not have yet is downloaded from the original shard by shard (57.2 GB in FP32: 69.0 / 126.2 GB in total) and converted to NF4 on your PC, deleting each shard as it goes. On disk it takes **~19.5 GB** with one expert and **~27 GB** with both (UMT5-XXL text encoder and VAE: 11.9 GB). |
| **ERNIE-Image** | 31.6 | — | **~6.7** | New trainer: downloads the prepared NF4 transformer and Ministral 3B text encoder from `AcademiaSD/Ernie-NF4-for-LoRA-Training`. The optional prompt enhancer is not needed for training. |

The automatic captioner adds, only the first time you use it: **nothing** for Krea 2 (it uses Krea 2's own text encoder), **5.5 GB** for Qwen-Image 2.1 when its text encoder is not already the NF4 one and for LTX-2.3, Z-Image, Anima, FLUX.2 Klein 9B and Ideogram 4 (Qwen3-VL-8B NF4, shared by all of them), and **8.9 GB** for MiniMax-H3 (Qwen3-VL-4B).

> **Upgrading from an old standalone LoRAlab?** Copy its model folder into `Models/` instead of downloading it again. Legacy model, cache and output folders in the project root are moved automatically on first start. Then you can delete what is no longer used: `Models/Krea-2-NF4/transformer` (~26 GB) and, in `Models/LTX23-NF4`, the `transformer` (~38 GB) and `text_encoder` (~49 GB) folders.

---

## 🖥️ Requirements

| | Minimum | Recommended |
| :--- | :--- | :--- |
| **OS** | Windows 10 / 11, or 64-bit Linux ([docs/Linux.md](docs/Linux.md)) | Windows 11 |
| **GPU** | NVIDIA **RTX 20xx / GTX 16xx or newer** (compute capability 7.5+) with **8 GB VRAM** (4 GB for Anima and SDXL in NF4, 10 GB for MiniMax-H3 Image edit LoRAs, 12 GB for SDXL in BF16) | 12–24 GB VRAM |
| **AMD GPU** *(experimental)* | Radeon **RX 7000 / RX 9000** or Ryzen AI Max (Strix Halo) with 16 GB of VRAM, using the AMD installer (see *Installation*). Confirmed on an RX 7800 XT 16 GB under Windows with MiniMax-H3 | — |
| **Driver** | NVIDIA **580 or newer** (CUDA 13). AMD: a recent Adrenalin driver on Windows, or `amdgpu` on Linux | Latest |
| **RAM** | 16 GB | 32 GB |
| **Disk** | The model of each trainer you use (table above) plus your datasets and caches | SSD |
| **Other** | Internet the first time each model is used. MiniMax-H3, Wan 2.2 and LTX 2.5 clips and audio files need **`ffmpeg`** in the `PATH`. | |

Python, Git and every library are installed by the installer. GTX 10xx and older cards are **not** supported: PyTorch for CUDA 13 starts at the RTX 20xx generation.

---

## 📦 Installation

**Option A — Git (recommended, makes updating easy).** Open the folder where you want to install it, type `cmd` in the address bar of the Windows Explorer, press Enter and run:

```bash
git clone https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio.git
```

**Option B — ZIP.** Press the green **Code** button → **Download ZIP** and unzip it where you want to install it (the folder is called `AcademiaSD_LoRAlab-TrainerStudio-main`).

Then, inside the folder:

1. Double-click **`Install_LoRAlab-TrainerStudio.bat`**. It installs Git if it is missing (Windows asks for permission), Python 3.13.1 if it is missing, and one `venv` shared by every trainer: PyTorch 2.14 (CUDA 13.0), Diffusers from GitHub, Transformers, PEFT, bitsandbytes, Flask and the rest. It takes a while; at the end it shows the detected GPU and versions.
2. *(Optional)* Double-click **`Install_Triton_SageAtten220.bat`** for Triton and SageAttention 2.2.

Pick a disk with plenty of free space: every model is downloaded into this folder.

**AMD GPUs (experimental).** Use **`Install_LoRAlab-TrainerStudio_AMD.bat`** (Windows) or **`Install_LoRAlab-TrainerStudio_AMD.sh`** (Linux) instead of the normal installer. It asks for your GPU family (RX 7000, RX 9000 or Ryzen AI Max / Strix Halo) and installs PyTorch ROCm from AMD's TheRock nightly builds. It is based on [a user's guide](https://civitai.com/articles/36293/training-krea-2minimax-h3etc-lora-on-low-vram-low-ram-amd-gpu-windows), and the same user [confirmed the installer](../../issues/8) on an **RX 7800 XT 16 GB under Windows**: a full MiniMax-H3 training at about 7 s/step, with no errors. The other trainers are not confirmed yet on AMD; results are welcome in that issue. Attention runs on PyTorch's native kernels (SageAttention is NVIDIA only). Do not run `Install_Triton&SageAtten220`, it is NVIDIA only. On Linux you need the `amdgpu` driver and your user in the `render` and `video` groups.

The **VRAM panel** of the trainers reads the real usage of the whole AMD GPU: on Windows through AMD's [ADLX](https://gpuopen.com/adlx/), which comes with the Adrenalin driver (the AMD installer and the updater install its Python package, `amd-adlx`; older installs with `tools/all-smi/` keep working); on Linux straight from the `amdgpu` driver, with nothing to install. The trainers that fit part of a model in the free VRAM also ask ADLX on Windows, because PyTorch for ROCm there only counts its own process, not the desktop or other programs. With two or more AMD GPUs, the launcher's GPU selector lists them too.

**Linux.** Every `.bat` has a `.sh` equivalent with the same name (`Install_LoRAlab-TrainerStudio.sh`, `Start_LoRAlab-TrainerStudio.sh`, `code/Run_LoRAlab-<Model>.sh`…) and the launcher picks the right one. Install and usage steps are in [docs/Linux.md](docs/Linux.md).

## 🔄 Updating

Double-click **`Update_LoRAlab-TrainerStudio.bat`**. It brings the latest version from GitHub — including any new trainer — and keeps your models, datasets, projects, LoRAs and settings, which are never part of the repository. Then it installs any new or updated library from `requirements.txt`, the single list the installers and the updater share. If the installation was made from the ZIP, the updater turns it into a Git installation the first time. What each update brought is in the [Changelog](#-changelog).

---

## 🚀 Using it

**`Start_LoRAlab-TrainerStudio.bat`** opens the launcher in your browser (`http://127.0.0.1:4990`). Click a trainer: its console window and its web interface (`http://127.0.0.1:5000`) open on their own. The trainer opened from a card uses port 5000. While one is training, clicking another card opens it on the next free port (5001, 5002…) so you can prepare a job for the [job queue](#-job-queue) without stopping the one that trains. Each trainer can also be started directly with its `code\Run_LoRAlab-<Model>.bat`.

Every trainer follows the same five steps:

1. **Project and dataset.** Type a project name, an optional trigger word, and pick the dataset folder with **Browse**. Each image needs a `.txt` caption with the same name. From another device, **⬆ Upload** in the Dataset Manager (or dragging files or a `.zip` onto it) copies them into that folder.
2. **Captions** *(optional)*. **Create Captions** writes a caption for every image with a vision-language model, trigger word first. The prompt is editable and **Overwrite** off only fills the missing ones. Review them in the **Dataset Manager**: click an image to edit its caption, use **Append / Replace / Remove** to change a common text in every caption, delete images, clear all captions, or empty the whole dataset folder with **Clear Dataset** (it asks you to type the number of files; subfolders are kept).
3. **Pre-Cache.** Choose the resolution and press **Start Pre-Cache**. The text encoder and the VAE run once and their output is stored on disk; the first time, the model is downloaded. Running it again skips the images that did not change.
4. **Train.** Set steps, learning rate, rank and alpha, and press **Start / Resume**. Watch the progress, VRAM, RAM and GPU temperature, and the previews (each trainer has its own previews panel). **Stop Training** saves the exact step: press **Start / Resume** again — even days later — to continue without losing a step. To train longer, raise the steps and press it again.
5. **Export.** Type the final name, pick your ComfyUI / Forge / A1111 `models/loras` folder and press **Save Path** — the folder is remembered for **every** trainer — then **🚀 Send to Models**. **⬇ Download LoRA** lists the final LoRA and the step checkpoints and saves the one you pick on the device you are browsing from.

Also in every trainer:

- **Live settings:** while training, change steps, save/preview frequency, preview settings or learning rate and press **Save JSON**; the change applies on the next step.
- **Delete Pre-Cache / Delete Training** empty the current project's folders (the dataset is never touched).
- Exported LoRAs carry kohya-style metadata (trigger word, rank, steps, resolution) that CivitAI and LoRA managers read.
- **Several NVIDIA GPUs?** Pick the one to train with in **🎮 GPU**, next to the language at the bottom of the launcher, and press **💾 Save settings**. It applies to the trainers opened from then on, and the VRAM panel shows that card. *Automatic* keeps CUDA's choice, which puts the card it considers fastest first, not always the one with more VRAM. The selector only appears with two or more NVIDIA cards.
- Optional **Hugging Face token** for faster downloads. Your settings and token are stored in `settings\`, which is never uploaded.
- Models live under `Models/`. Each project uses `Cache_Data/cached_data_<model>_<project>` for the pre-cache and `Outputs/<model>_lora_output_<project>` for checkpoints, previews and LoRAs. Legacy root folders are moved automatically on first start. Migration is skipped while a training or captioning process is running.

---

## 🧾 Job queue

Queue trainings and pre-caches, from one trainer or several, and they run one after another on the GPU.

- **Adding jobs.** While something is training, **Start / Resume** or **Start Pre-Cache** in any trainer asks *Add to queue?* instead of starting. The job keeps a copy of the settings saved at that moment, so you can go on changing that trainer for the next one. With the GPU free, a training starts at once as before, and it shows in the queue too.
- **Missing or outdated pre-cache.** **Start / Resume** checks the project's pre-cache against its dataset. With no pre-cache, or with images or captions added, edited, removed or renamed after it, it lists what changed and offers **Pre-cache, then train**: the pre-cache starts and the training waits in the queue until it finishes well (if it fails, the training keeps waiting until you retry it). **Train with the old cache** trains anyway. Without the launcher the page itself waits for the pre-cache, so keep it open.
- **Training after its pre-cache.** While a trainer runs its pre-cache, its **Start / Resume** stays available: the training goes to the queue and starts as soon as the pre-cache finishes.
- **Editing a waiting job.** **✎** on a job of the queue opens its trainer with that job's settings, and its start button becomes **💾 Save changes to the queue**. The job does not start while you edit it; **Cancel** leaves it as it was.
- **Another trainer while one trains.** Click its card in the launcher: it opens on another port without closing the one that trains.
- **Another training of the same model.** While a trainer trains, **➕ New training for the queue** appears under Start / Stop. It opens a draft of that trainer on another port, starting from the current settings but saving to its own copy: change the project, dataset or anything else without touching the training in progress, and its Start adds it to the queue. Give the draft its own project name, so it does not overwrite the project folder of the one training.
- **The queue page.** The **Queue** button, in the launcher and in every trainer, opens it in the same tab: the job training now, with its progress, time left and loss curve; the jobs waiting, which you drag to change their order, pause, resume or remove; and the history. **Go to the training** opens that job's trainer, with its console, chart and previews, also in the same tab. In the history, **⧉** uses a finished job as a template: it opens its trainer with the settings of that job, in a copy of their own, to change what you want and train again. Give it another Project Name: with the same name, Start / Resume continues the finished training instead of starting a new one.
- **Pause and resume.** Pausing a job, the one training or one waiting, keeps it in the queue as paused: the one training saves a checkpoint and stops, and the next one starts. Resuming it continues from that step. This also works for a training started directly from its trainer. **Pause the queue** lets the current job finish and starts nothing new; **Stop if a job fails** pauses the queue when a job fails.
- **When a job fails** it stays in the list, in red, saying why in plain words (the pre-cache or the dataset was not found, not enough VRAM…) with the console line below. The next job starts meanwhile. Fix the cause and press **↻** to queue it again (at the end, so a Pre-Cache added for it runs first), or add the job again and it replaces the failed one. A job that hangs and does not answer **Remove** or **Pause** is closed after 30 s (3 min when pausing); pressing **Remove** again closes it at once.
- **Each job runs in its own trainer,** opened without a window on a free port (5001, 5002…). What you save in that trainer applies only to that job, never to your trainer settings. If the launcher is closed while a job trains, the job shows as paused (interrupted) and can be resumed.
- **⏻ Pause all and exit,** at the bottom of the launcher, pauses the job training (with its checkpoint), closes every trainer and job and then the launcher itself, all from the browser. Next time you open the launcher, the queue continues on its own where it was, starting with that training from its checkpoint. On RunPod and other clouds, or when used remotely, the launcher stays open so the page keeps working, with the queue paused: turn off **Pause the queue** to carry on.
- Behind a reverse proxy or on RunPod only ports 4990 and 5000 are published: the queue works, but **Go to the training** needs the job's port to be reachable.

---

## 🎯 Custom prompts in the previews

In **2b. Training Previews** of every trainer, **Custom Prompts (0-4)** sets how many prompts of your own the previews use.

- **0** — the previews use the dataset captions, as chosen in **Caption Mode** (First, Random, Rotate 4).
- **1 to 4** — a box appears for each prompt, and each preview round makes one image per prompt: `preview_step_N.png`, `preview_step_N_2.png`… In the gallery they show as *Step N*, *Step N · #2*… Caption Mode is not used meanwhile.
- **One random prompt per preview** — each round makes a single image, with one of your prompts chosen at random. Previews then take as long as with one prompt.
- The trigger word is added in front of each prompt, as in the captions. A settings file from before, with Caption Mode = Custom prompt, opens as 1 prompt.
- **Each preview keeps its prompt.** Click a preview: under its name you see the prompt it was made with, your own or the dataset caption. It is stored inside the PNG (and in a `.txt` next to video and audio previews), so it travels with the file.

**When they are encoded.** Pre-Cache encodes the prompts on the GPU with the rest of the texts. If you change them with **Save JSON**, only the prompts that changed are encoded, in one process: on the GPU when nothing is running, on the CPU while training (it does not touch the training's VRAM; about a minute). The trainer switches to each prompt when it is ready; until then the previews use the ones that are, or the dataset captions. The console lists the prompts and marks with `...` the ones not encoded yet. YuE 2 takes your prompts as lyrics: nothing is encoded, the trainer reads them directly.

**LTX 2.3, LTX 2.5, MiniMax-H3 and MiniMax-H3 Image** encode them in Pre-Cache only: their text encoders (Gemma, MiniMax) are too large to load on the CPU next to a training. After changing a prompt, run Pre-Cache again (it skips the images already cached). If a training is running, the console says which prompts are not encoded and the previews go on with the others. MiniMax-H3 Image uses your prompts for image LoRAs; for edit LoRAs its previews keep using the dataset pairs.

**Edit trainers.** The prompts are the instructions, applied to the preview's reference image(s) (**Edit Preview Image** or **Edit Preview Reference Images**; empty = the "before" of the first pair). Changing the images re-encodes them and every prompt, because Qwen-Image and MOSS-Image show them to the text encoder too.

- In the trainers with a list of reference images (Qwen-Image 2.1, Qwen-Image 2512 / Edit 2511, FLUX.2 Klein 9B, FLUX.3 Image Klein, MOSS-Image), by default all the images are `<image1>`, `<image2>`… of the same edit, for every prompt: the output follows image 1, and image 2 only matters if the prompt names it (*put the jacket of `<image2>` on the person of `<image1>`*).
- **One image per prompt** makes each prompt edit its own image instead: prompt 1 → image 1, prompt 2 → image 2… (with fewer images than prompts they start over). Each image is used at full preview size. Use it to see the effect on several photos in one round, ideally photos that are not in the dataset.

---

## 🎛️ LoRA options: rsLoRA, LoRA+, DoRA and LoKr

Under **LoRA Rank / Alpha**, the trainers have extra checkboxes. They change **how** the LoRA learns, so they are fixed for the whole training (to change them, *Delete Training* and start again; the pre-cache is reused).

| Option | What it does | Trainers |
| :--- | :--- | :--- |
| **rsLoRA** | Scales the LoRA by `alpha/√rank` instead of `alpha/rank`, so high ranks keep learning. Ticking it lowers alpha to keep the same strength. | Z-Image, FLUX.2 Klein 9B, Qwen-Image 2.1, Qwen-Image 2512, Krea 2, Anima, Ideogram 4, ERNIE-Image, MOSS-Image, SDXL, LTX-2.3, MiniMax-H3 |
| **LoRA+** | The `B` matrix of every layer learns 16× faster than `A`: usually the same quality in fewer steps. Lower the LR if it burns early. | same as rsLoRA |
| **DoRA** | Each layer also learns the size (magnitude) of every output row, apart from its direction, which is the usual LoRA. It often follows the dataset more closely at the same rank. Every step is slower and uses some more VRAM, because the 4-bit weight of each layer is unpacked to measure it. Works with rsLoRA and LoRA+. | Z-Image, FLUX.1 Dev, FLUX.2 Klein 9B, FLUX.3 Image Klein, Krea 2, Qwen-Image 2.1, Qwen-Image 2512, Ming-Image, MOSS-Image, Anima, Wan 2.2, ERNIE-Image, Fibo 2.0, Ideogram 4, SDXL, LTX 2.3, LTX 2.5, Boogu |
| **NormFix** (with DoRA, on by default) | Saves the `dora_scale` with the row sizes of the original model instead of those of the 4-bit copy it trains on. ComfyUI measures them on the model it loads, and the 4-bit copy is off by more than what DoRA learns: without NormFix a DoRA can lose the likeness in ComfyUI even when the previews look right. Only the saved file changes, not the training. The sizes come from `dora_norms.safetensors` in the NF4 model folder, downloaded before training when it is missing (SDXL and Anima take them from the original weights when loading). | every DoRA trainer |
| **LoKr** + **Factor** | Replaces LoRA with a Kronecker product (LyCORIS). Much smaller files (~3 MB instead of ~40 MB at rank 8), good for characters with small datasets, more sensitive to the LR. rsLoRA, LoRA+ and DoRA turn off. | Z-Image, FLUX.2 Klein 9B, Qwen-Image 2.1, Krea 2, Anima, ERNIE-Image, MOSS-Image |

- The exported file is a **standard LoRA / LyCORIS file** that ComfyUI and Forge load as usual (with rsLoRA, the alpha is converted so it acts exactly as trained; with DoRA, every layer carries a `dora_scale`, stored the way ComfyUI applies it).
- **Send to Models** and **⬇ Download LoRA** add **`_rs`**, **`_plus`**, **`_dora`** or **`_lokr`** to the name, taken from the file's own metadata, so you always know how it was trained. The *Final LoRA Filename* field shows the suffix as you tick the boxes.
- No extra VRAM with rsLoRA, LoRA+ or LoKr: LoKr never builds the full weight matrix, and the other two only change the scaling and the optimizer. DoRA is the exception: slower steps and some more VRAM.
- **Testing a DoRA in ComfyUI:** use a full caption like the ones in your dataset. A very short prompt with a high CFG and a long negative loses the likeness with a DoRA and with a plain LoRA alike.

**Which one to use.** All of them are optional: with no box ticked the trainer works exactly as before. Train the same dataset with the same steps, seed and LR to compare them; the pre-cache is shared, so only *Delete Training* is needed between runs.

| Mode | Boxes | When it helps | Starting point | Name suffix |
| :--- | :--- | :--- | :--- | :--- |
| **LoRA** (default) | none | Everything: the safe choice | The trainer's defaults | — |
| **rsLoRA** | rsLoRA | Higher ranks (32-64) for styles or many concepts: with plain LoRA, raising the rank adds little | Rank 32; the alpha it sets for you (≈ alpha/√rank) | `_rs` |
| **LoRA+** | LoRA+ | Reaching the same result in fewer steps | Same LR; check the intermediate checkpoints, and lower the LR if it burns early | `_plus` |
| **rsLoRA + LoRA+** | both | The two together: stable high ranks that also learn faster. They do not conflict: one changes the scaling, the other the optimizer | Rank 32, the alpha rsLoRA sets, and an LR about 2× lower than usual, because both make the training stronger | `_rs_plus` |
| **DoRA** | DoRA | Likeness that a plain LoRA does not reach at the same rank, when slower steps are acceptable. Can be combined with rsLoRA and LoRA+ | The trainer's defaults: same rank, alpha and LR as LoRA | `_dora` |
| **LoKr** | LoKr (+ Factor) | Characters and objects with small datasets, or when file size matters | Rank 8, alpha 8, factor 16, same LR as LoRA; factor 8 or a higher LR if it learns too little | `_lokr` |

### LR scheduler

Every trainer has an **LR Scheduler** selector under the learning rate, with **Warmup Steps** (and **Cycles** for restarts). The default keeps each trainer's previous behaviour: `cosine` everywhere, `constant_with_warmup` on MiniMax H3.

| Scheduler | What it does |
| :--- | :--- |
| `cosine` | Rises during the warmup, then eases down to 10% of the LR |
| `constant` | The same LR from the first step to the last (no warmup), like the Civitai trainer |
| `constant_with_warmup` | Rises during the warmup, then stays at the LR |
| `linear` | Rises during the warmup, then goes down in a straight line to 10% |
| `cosine_with_restarts` | Like `cosine`, but climbs back up and repeats the curve *Cycles* times; for long trainings |

With `constant` every checkpoint is trained equally hard, so stopping early gives the same result as a shorter training; the decaying ones usually leave cleaner final checkpoints.

The chosen scheduler is shown in the console summary when training starts and saved in the LoRA metadata (`ss_lr_scheduler`). It is read again on every start, so a resumed training continues with whatever is selected.

**Resuming with more steps.** The curve always covers the whole training, from step 0 to Total Steps. Train 1000 steps with `cosine` from 4e-4 to 4e-5, raise Total Steps to 2000 and resume: step 1001 sits half-way along the 2000-step curve, so the LR jumps back up to ~2.3e-4 and goes down again to 4e-5 at step 2000. To decide yourself where the second part starts, tick **New LR curve on resume** (under the LR Scheduler, off by default): when resuming, the curve starts again at that step, from the current Learning Rate down to its minimum at the last step, without warmup. In the same example, set the LR to 1e-4 and resume: the next 1000 steps go from 1e-4 to 1e-5. The console says it when resuming (`[LR] New LR curve on resume: a new curve starts at step 1000...`). The start step is kept in the project's output folder (`lr_curve.json`): resuming again with the same LR and Total Steps stays on that curve, with others a new one starts, and a new training starts from step 0 as always.

---

## 🌍 Languages

The launcher, every trainer interface and the console messages are available in **English, Español, Deutsch, Français, Português, Italiano, 日本語 and 한국어**. English is the default.

1. At the bottom of the launcher, pick a language in **🌍 Language**: the launcher switches at once, as a preview.
2. Press **💾 Save settings**. The choice is stored in `settings/ui.json` and applies to every trainer.
3. A trainer page that is already open changes after reloading it; the scripts (captioner, pre-cache, training) use the new language on their next run.

What stays in English on purpose:

- **Caption prompts and the captions themselves**, because that is the language the models were trained on.
- Technical names and log tags: settings such as `vram_budget_gb` or `max_seq_len`, markers such as `[NF4-TE]` or `[BACKFILL]`, model names and paths.
- The `.bat` and `.sh` windows of the installer, the updater and the launchers.

**Improving a translation.** Each language is one file, `GUI/locales/<code>.json` (`es`, `de`, `fr`, `pt`, `it`, `ja`, `ko`). The key is the English text and the value is its translation:

```json
{
  "Start Pre-Cache": "Iniciar Pre-Caché",
  "{n} images inside": "{n} imágenes dentro"
}
```

Keep every `{marker}` of the English text, in the same order when it has no name (`{}`). A text with no translation is shown in English, so nothing breaks while a translation is incomplete; edit the file, reload the page, and the change is there. The German, French, Portuguese, Italian, Japanese and Korean translations are first versions: if a term sounds wrong in your language, open an [issue](../../issues) or a pull request with the fix.

---

## 🖼️ Sharp previews in ComfyUI

Some of these models are slow to generate, so it pays to see where an image is going early on, while it is still sampling, and cancel it if it is not working. That needs a good preview, and ComfyUI's default one for Qwen-Image 2.1, Krea 2 and FLUX.2 is Latent2RGB, a blurry, blocky color projection.

My recommendation: **kijai's KJNodes** plus **AcademiaSD's tiny decoders (TAE)**. They show a real image at every step, in milliseconds and without loading the full VAE:

| Model | TAE | File |
| :--- | :--- | :--- |
| Qwen-Image 2.1 | [AcademiaSD/TAE-Qwen-Image-2.1](https://huggingface.co/AcademiaSD/TAE-Qwen-Image-2.1) | `TAEQwenImage21_AcademiaSD.safetensors` |
| Krea 2 | [AcademiaSD/TAE-Krea-2](https://huggingface.co/AcademiaSD/TAE-Krea-2) | `TAE_Krea2_AcademiaSD.safetensors` |
| FLUX.2 and Ideogram4 | [AcademiaSD/TAE_Flux2_AcademiaSD](https://huggingface.co/AcademiaSD/TAE_Flux2_AcademiaSD) | `TAE_Flux2_AcademiaSD.safetensors` |

1. Download the file to `ComfyUI/models/vae_approx/`.
2. Install [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes) by kijai.
3. Add the **Model Preview Override** node between the model (with your LoRA) and the sampler, and pick the TAE in its `tiny_vae` input.

ComfyUI's built-in TAESD preview method does not load these files: use the KJNodes node. They are for previews only; the final image is still decoded with the real VAE.

## 👤 Face likeness in the previews

<p align="center">
  <img src="assets/likeness.jpg" alt="Face likeness on the training previews" width="900">
</p>

For character LoRAs: each preview gets a badge with how much its face looks like the person in the dataset, so you can see from which step the LoRA has learned the face and whether later steps keep it. The same % appears above each preview circle on the training chart, in 2D and 3D.

- **Off by default, nothing is downloaded.** Click **👤 Face likeness → Enable...** above the previews. A popup explains the terms and has two checkboxes: *I accept that I download and use these models under my own responsibility* and *I will not use them for commercial purposes*. **Download** is enabled only with both checked.
- It downloads InsightFace's `buffalo_l` (the SCRFD face detector and the ArcFace recognizer, ~280 MB, only those two files are kept) to `Models/FaceMatch-InsightFace/`, and installs `onnxruntime`. **The InsightFace pretrained models are licensed for non-commercial research purposes only**; the acceptance is saved in `settings/face_match.json`.
- It runs on the CPU of the machine with the trainer, so it uses no VRAM and works the same on Windows, Linux, macOS and RunPod, from any browser or phone.
- **Reference:** the largest face in each dataset image, averaged. **Likeness:** ArcFace cosine similarity of the preview's closest face to that reference, ×100. Real photos of the same person usually score above 50%; a different one, under 20-30%. Generated faces score lower: in the previews of a LoRA, 45% or more is a strong likeness. Green from 45%, amber from 30%, red below; *no face* when none is detected. Video previews are scored on their first frame.
- **Show %** hides or shows the badges in the gallery and the chart. Video previews (Wan 2.2, LTX-2.3) are not scored; YuE2 (audio) does not have it.

## 🧮 Final XY grid

When the training ends, the trainer makes the same image (same prompt and seed) with several checkpoints and LoRA strengths, and joins them into one image per prompt: **checkpoints in rows, strengths in columns**. One look shows when the LoRA learned the character or style, when it starts to overcook, and which strength to use in ComfyUI.

- **Turn it on** in **2b. Training Previews**, under Preview Size: **Final XY grid**, with **Checkpoints** (rows, 4 by default) and **Strengths** (columns, `0.75, 1.0, 1.25` by default, from 0 to 3; 0 is the model without the LoRA). Off by default, because it adds time at the end: one preview per image.
- **Checkpoints** are spread over the training: with 4 and 800 steps, steps 200, 400, 600 and the final one. The trainer keeps a small copy of the LoRA at those steps while it trains (in `xy_grid/snapshots`, about the size of the LoRA), even when they are not multiples of Save Every, so **turn it on before the training ends**. A new training in the same project deletes the copies of the previous one; resuming keeps them.
- **Prompts:** one grid per Custom Prompt or, without them, one with the caption of the first dataset image. Each image uses the same size, steps, CFG and seed as the previews (with Seed = 0, one random seed for the whole grid).
- **Strength works as in ComfyUI:** the weight becomes W + strength × ΔW, also with DoRA and LoKr.
- **Face likeness:** with [Face likeness](#-face-likeness-in-the-previews) installed, each image shows its % in the corner, with the colours of the gallery, and the console says which step and strength are the most alike for each prompt.
- The grids show above the previews (click one to open it full size) and are saved as `xy_grid_step_<N>_<prompt>.png` in the `xy_grid` folder of the output, with the prompt inside the PNG. If the grid fails (for example, out of VRAM), the console says so and the LoRA is already saved.
- **Trainers:** Z-Image, Anima, Anima 2.9B, FLUX.1 Dev, FLUX.2 Klein 9B, FLUX.3 Image Klein, Qwen-Image 2.1, Qwen-Image 2512 / Edit 2511, Krea 2, Fibo 2.0, Ideogram 4, Ming-Image, MOSS-Image, ERNIE-Image, Boogu, SDXL and MiniMax-H3 Image. Not in the video and audio trainers (LTX 2.3, LTX 2.5, MiniMax-H3, Wan 2.2, YuE2).
- **Time:** checkpoints × strengths × prompts previews. With the defaults, 12 per prompt: about 1-2 minutes with a turbo LoRA (Z-Image, ~6 s per image at 4 steps), several minutes with 30-step previews.

---

## 🧬 Dataset Forge

A character dataset from a few images, even just one: new outfits, places and framings that keep the face. Open it with **🧬 Dataset Forge** in the Dataset Manager toolbar of any image or video trainer; it opens in its own tab.

1. **Source and references:** a folder with a few photos of one adult person (it does not touch it). Click the ones to use as reference: up to 4 go into the model, the rest only help the likeness check.
2. **Analyze:** the shared Qwen3-VL-8B captioner writes the captions the references lack and a character sheet: woman / man and the features that do not change (age, hair, eyes, visible marks). Edit it if needed.
3. **Plan:** one line per image combining framing (half close-ups, 30% waist-up, 20% full body: the LoRA learns the face from close-ups), outfit, place (half indoors, half outdoors), light, angle and expression, without repeating outfits or places until they run out. Edit, add or delete lines; **🎲 New plan** makes another one.
4. **Generate:** the model gets the references and each line, with a new pose and expression for every image:
   - **FLUX.3 Klein** (default, NF4). The most natural images: clean anatomy, new poses and the framing of the plan. **Fast** quality (default): NoiseToNova's turbo LoRA (PDD), 4 or 8 steps (about 12 or 25 s per image), with higher likeness but a more made-up, contrasted look. **Best**: 12 to 50 steps with CFG 3.5 (16 steps about 85 s, 28 about 2.5 min), softer and more natural. **Steps** picks the count. **FLUX Kommunity License:** non-commercial use; commercial use of the images only for Qualifying Users (see the license).
   - **Fibo 2.0 Dev** (NF4, 30 steps, CFG 5, about 5 min per image). The highest likeness and clean anatomy, with a slightly more retouched look. **CC BY-NC 4.0: non-commercial use only.**
   - **Qwen-Image 2.1** (NF4, no CFG). High likeness, but bodies can be out of proportion and it tends to copy the pose of the reference. **Best** quality: 20 steps of the base model, clean anatomy, about 40-70 s per image. **Fast**: Viggle's turbo LoRA, 4 steps, about 20-30 s, but more deformed bodies. **Qwen Research License: non-commercial use only.**
   - **FLUX.2 Klein 9B** (NF4 with kalle07's turbo LoRA, 4 steps). Natural anatomy, but the face drifts more and it does not always follow the framing. **FLUX Non-Commercial License.**
   - **Qwen-Image-Edit-2511** (NF4 with lightx2v's Lightning LoRA, 4 steps, Apache 2.0). The only one for commercial use, but it drifts most from the face: expect a lower minimum likeness.

   With two references of the same woman (65% minimum), averages in our test: Fibo 2.0 71%, Qwen-Image 2.1 Best 68%, Fast 64%, FLUX.3 Klein Fast 67% (4 steps) / 64% (8), Best 58-60% (16-28 steps), FLUX.2 Klein 55%, Edit-2511 about 50%. The likeness score is not everything: FLUX.3 Klein's images looked the most natural and were judged closest by eye. For reference, real photos of her scored 61-78% against one reference.

   Every image is checked with the [face likeness](#-face-likeness-in-the-previews): under the minimum (60% by default) it is tried again with another seed, and if it still does not reach it, it goes to `_rejected`. It needs a checkbox confirming you have the right or the person's permission to use their images.
5. **📂 Use in Dataset Manager** sets the new folder as the trainer's dataset: references and generated images, each with its `.txt`.

- **Captions:** the trigger plus the line of the plan (*close-up portrait of a woman, head and shoulders, wearing a black leather jacket, in a coffee shop...*). The fixed features go into the instruction for the model but not into the caption, so the trigger learns the identity.
- **Output:** a new folder (by default `<source>_forge`), never the source. GPU job: it does not start while a training, pre-cache or caption job is running, and they see it as busy.
- **Models:** the same folders as their trainers, downloaded the first time if the trainer has not done it: `Models/FLUX.3-Image-Klein_NF4` (~12 GB, plus the PDD turbo LoRA in `LoRAs`, ~1.2 GB), `Models/Fibo2_Dev-NF4` (`transformer`, `text_encoder_BF16`; ~13 GB), `Models/Qwen-Image21-NF4` (`transformer`, `text_encoder_BF16`, the Viggle turbo LoRA; ~22 GB), `Models/FLUX.2-Klein-9B_NF4` (~9 GB) or `Models/Qwen-Image-2512-NF4` (`transformer_edit`, `text_encoder_BF16`, the Edit-2511 Lightning LoRA; ~27 GB). The BF16 text encoders are split between GPU and RAM; the transformers of FLUX.3 Klein (5.5B), Fibo 2.0, 2.1 (7B) and Klein (9B) fit in the GPU and the 20B of 2511 uses BlockSwap.
- **Two references are better than one:** the likeness check averages them, and the model sees more of the face.
- Without face likeness installed, the images are kept without checking the likeness.

## 🧪 The trainers

> ⚠️ **About the default settings:** the tests were made to check that every training works, not to find the best performance or quality. Run your own tests with different settings (steps, learning rate, rank, resolution, captions) to improve the quality of your LoRAs.

All times were measured on an RTX 5080 16 GB.

### Fibo 2.0 — image and edit LoRAs (BRIA)

> **New and experimental:** full runs (pre-cache, training, previews, edit mode, resume) verified on Fibo 2.0 Dev. It works, but it is young: the defaults will move as more people test it.

- **Normal LoRAs** (characters, objects, styles): one image + one caption each.
- **Edit LoRAs**: pairs named `name_before.png` / `name_after.png` plus the instruction in `name.txt` (for example `replace the jacket with a red leather one`). Choose **LoRA Type → Edit**. The before image goes through the text encoder with the instruction and, as a clean latent, conditions the generation as context tokens; the loss is computed only on the "after".
- **The model:** `briaai/Fibo-2.0-dev`, the full non-distilled base (8.1 B, flow matching on the FLUX.2 VAE, Qwen3-VL-4B as text encoder). Its licence is **CC BY-NC 4.0**: non-commercial use only. The NF4 build is downloaded from `AcademiaSD/Fibo-2.0-NF4-for-LoRA-Training` the first time (the transformer in NF4 and the text encoder in BF16, INT8 or NF4); to build it yourself from the diffusers folder, run `tools/fibo2/5_conversor_Fibo2_NF4.py` once with the folder as `Fibo2_Dev-Raw/`. The conversion needs diffusers with `BriaFibo2Pipeline` (merged upstream): run `Update_LoRAlab-TrainerStudio.bat` first.
- **NF4:** the attention, MLP and cross-attention of the 44 blocks are quantized (342 layers); the perceptor that turns the caption into gist tokens, the modulation of every block and the input/output layers stay in BF16 (73 layers), because quantizing them puts noise in the text path. The transformer is 5.2 GB in VRAM instead of 16 GB.
- **Text encoder for the pre-cache:** Qwen3-VL-4B, the model's own — **NF4 (~2.7 GB, default)**, INT8, BF16 (9 GB+ VRAM) or BF16 with CPU offload (exact, any GPU). The pre-cache runs it once; the training never loads it.
- **Captions:** Fibo 2.0 was trained on structured JSON captions (VGL). A plain `.txt` also works (the pipeline reads it as a short description); for the best results drop a `<name>.json` next to the image with the structured caption — the pre-cache prefers the `.json` over the `.txt`, and the Dataset Manager shows and edits whichever one is there. A `text_render` entry is drawn and shown to the model exactly as in training, so the text of the image comes out right; above the noise level 0.9 the caption goes in without those drawings, as in the official recipe.
- **Recipe:** the one BRIA publishes in `fine_tuning/train_lora.py`: logit-normal noise with 10 % uniform, 10 % text dropout, 20 % context dropout in edit mode, AdamW (weight decay 0.01), gradient clip 1.0.
- **LoRA Targets:** *All* (default) trains all 415 linear layers, exactly the recipe BRIA used; *Blocks* trains only the attention and MLP of the 44 blocks.
- **Previews:** 30 steps / CFG 5, the model's own defaults, and a **Preview Size** (Training / 768 / 1024) to see the result at the size you will use in ComfyUI even if you train at 512. **Fast Previews** cuts the steps and the guidance: Fibo 2.0 Dev has no distilled LoRA (the "Edit Turbo" is another checkpoint), so the preview is about twice as fast but rougher.
- **The LoRA is exported for ComfyUI**, in the format its loader takes (`diffusion_model.<capa>.lora_A/lora_B` + `alpha`). ComfyUI runs its own repack of Fibo 2.0, where the attention, the MLP and the cross-attention are single fused matrices, so the layers that fuse are re-written as one LoRA of several times the rank: the applied change is exactly the same as in diffusers, but the file is about half again as big.
- **To convert a LoRA trained before this change** (with the `transformer.*` keys), without retraining: `python tools/fibo2/7_conversor_lora_comfyui.py <lora.safetensors>`. It rewrites the keys in place and keeps the metadata.
- **Technical notes:** [docs/README_Fibo2.md](docs/README_Fibo2.md).

- **From 8 GB of VRAM:** **VRAM Profile**, **Resident Blocks**, **Block Swap Storage** and **RAM Limit**, as in [FLUX.2 Klein 9B](#flux2-klein-9b--image-and-edit-loras): the blocks that do not fit wait in RAM or on disk and come to the GPU just in time. Measured with the 8 GB profile (rank 16, image LoRAs at 768²): 3.5 s/step and 5.3 GB of peak VRAM, against 3.2 s/step with everything in VRAM; DoRA fits too (5.9 s/step).

| Measured on an RTX 5080 16 GB, **Auto** profile (rank 8, LoRA Targets: all) | s/step | Peak VRAM |
| :--- | :--- | :--- |
| Image 512² | 2.0 | 8.7 GB |
| Image 1024² | 6.2 | 11.2 GB |
| Edit 512² | 3.1 | 9.9 GB |
| Edit 1024² | 14.9 | 15.9 GB |

The edit mode adds the tokens of the before image to the sequence, so edit LoRAs at 1024² need much more memory: on small cards train them at 512².

### Qwen-Image 2.1 — image and edit LoRAs

- **Normal LoRAs** (characters, objects, styles): one image + one caption each.
- **Edit LoRAs**: pairs named `name_before.png` / `name_after.png` plus the instruction in `name.txt` (for example `make it TOSTIOK style`). Choose **LoRA Type → Edit**. The "before" image goes through the text encoder with the instruction, like the ComfyUI `TextEncodeQwenImage21` node, and the loss is computed only on the "after".
- **Captioner:** Qwen3-VL-8B, the model's own text encoder in NF4 (~6 GB VRAM, ~11 s per image), with **Normal** and **Edit** modes. For a style or effect, one common instructio