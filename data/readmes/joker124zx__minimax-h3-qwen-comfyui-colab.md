# 🎬 MiniMax-H3 & Qwen-Image 2.1 全能工作台 · All-in-One ComfyUI Colab Studio

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/joker124zx/minimax-h3-qwen-comfyui-colab/blob/main/MiniMax_H3_Qwen2.1_ComfyUI_Colab.ipynb)
![ComfyUI](https://img.shields.io/badge/ComfyUI-latest-blue)
![MiniMax-H3](https://img.shields.io/badge/MiniMax--H3-Video%20%2B%20Audio-purple)
![Qwen-Image 2.1](https://img.shields.io/badge/Qwen--Image-2.1-orange)
![GPU](https://img.shields.io/badge/GPU-96GB%20Blackwell%20(G4)-green)

**中文** | [English](#-english)

---

## 📖 简介

一个 **单文件 Google Colab 笔记本**，一键在云端 GPU 上部署 **ComfyUI**，并按需加载：

- **MiniMax-H3**：文生视频、首尾帧图生视频、多图/视频/音频全能参考视频（Ref2V）、数字人对口型、360° 环绕运镜、无限长视频时间线导演等，**原生音画同步**。
- **FastH3-Omni**（UCSD × NVIDIA）：原生 8 步极速全参考视频，含 Blackwell NVFP4 加速版。
- **C 站 MiniMax-H3 Remix**：社区二合一微调底模。
- **千问 Qwen-Image 2.1**：2K 文生图、多图改图、换装/一致性、超清修复、动漫转真人等。

特点：

- 🧩 **按需切换架构**：用哪套模型就只下载哪套，切换时**自动清理未选底模**，节省磁盘。
- 🗂️ **LoRA 池 / 工作流池完全隔离**：H3 视频池与千问图像池互不干扰。
- 📦 **18 套 H3 工作流 + 12 套千问工作流内置**（压缩嵌入笔记本中，开机自动写入 ComfyUI，**0 缺失节点**）。
- ⚡ **多线程并发下载** 节点、VAE、放大器、LoRA。
- 🌐 **Cloudflare 隧道** 自动生成公网访问链接（免 403），并支持**秒级重启**，无需重下模型。
- 📝 全部单元格为 Colab **表单模式**，下拉框选模型，点 ▶️ 即可，无需改代码。

---

## 🚀 快速开始

1. 点击上方 **Open in Colab** 徽章打开笔记本（建议 `文件 → 在云端硬盘中保存一份副本`）。
2. `代码执行程序 → 更改运行时类型`，选择 **大显存 GPU**（推荐 **G4 / RTX PRO 6000 Blackwell 96GB**，或 A100 80G / H100）。
3. （可选）在 **单元格 1** 和 **单元格 6** 的 `C站_API_Token` 中填入你自己的 [Civitai API Key](https://civitai.com/user/account)，用于下载 C 站 LoRA。
4. **每次开机先运行 单元格 1**（安装底座环境）。
5. 根据需求 **只运行 2～6 中的一个** 单元格，在表单里选好底模 / CLIP，运行后会输出 ComfyUI 访问链接。
6. 网页断开或链接失效时，运行 **单元格 7** 秒级重启，不会重新下载模型。
7. 用完记得 `代码执行程序 → 断开连接并删除运行时`，避免浪费算力额度。

> [!IMPORTANT]
> 本仓库版本已将作者私人 Civitai Token **清空为占位符**。不填写 Token 时，Hugging Face 上的模型均可正常下载，仅需要登录才能下载的 C 站 LoRA 会跳过/失败。

---

## 🧭 单元格说明

| 单元格 | 名称 | 核心底模与配置 | 专属池（LoRA + 工作流） | 适用场景 |
| :--- | :--- | :--- | :--- | :--- |
| **1️⃣** | 🛠️ 必备基础框架 | ComfyUI 核心 + 全部自定义节点 + 公共 VAE / 潜空间放大器 / 加速 LoRA | 初始化运行底座 | **每次新开机必点一次** |
| **2️⃣** | 🎬 文生 + 首尾帧视频 | 官方 `64G` FL2VA 底模 + 自选 CLIP | H3 视频池 | 文生音视频、首尾帧图生视频 |
| **3️⃣** | 🖼️ 全参视频 | 官方 `64G` Ref2VA 底模 + 自选 CLIP | H3 视频池 | 多图 / 视频 / 音频全能参考、运镜控制 |
| **4️⃣** | ⚡ FastH3-Omni 实时全参 | `41G` 原生 8 步 BF16 / `13G` Blackwell NVFP4 | H3 视频池 | 极速全能参考视频、视频改视频 |
| **5️⃣** | 🌟 C 站 H3 Remix | `64G` BF16 / `31G` INT8 社区二合一底模 + 未删减 CLIP | H3 视频池 + C 站增强池 | 社区微调效果、360° 环绕运镜 |
| **6️⃣** | 🎨 千问 Qwen-Image 2.1 | `13.6G` 标准 / 8 步 Turbo / 夜曲动漫底模 + 专用 CLIP & VAE | 千问专属池（19 款 LoRA + 12 套工作流） | 2K 文生图、多图改图、超清修复 |
| **7️⃣** | 🚀 独立重启 ComfyUI | 不删模型、不重下 | 保持当前模型池 | 网页断连、刷新获取新隧道链接 |

### 🔤 CLIP（文本编码器）可选项

| 选项 | 大小 | 说明 |
| :--- | :--- | :--- |
| `qwen3vl_32b_minimax_h3_int8_convrot` | 25G | 官方 INT8 均衡版（默认推荐） |
| `qwen3vl_32b_minimax_h3_nvfp4_awq` | 15G | 官方 NVFP4 极速版（Blackwell 加速） |
| `qwen3vl_32b_heretic_minimax_h3_nvfp4` | 15G | 社区未删减极速版 |
| `qwen3vl_32b_minimax_h3_int8_convrot_uncensored` | 25G | 社区未删减均衡版 |
| `minimaxH3Remix_int8ConvrotV06Fixed_txt` | 25G | C 站 Remix 配套 CLIP |

---

## 📦 内置 H3 工作流（18 套）

| 文件 | 用途 |
| :--- | :--- |
| `00_Omni官方原版.json` | Comfy-Org 官方 FastH3-Omni 参考视频工作流 |
| `01_文生与首尾帧.json` | 文生视频 / 首尾帧图生视频 |
| `02_文生与首尾帧_二采放大.json` | 同上 + 二次采样潜空间放大 |
| `03_全能参考_直出.json` | 1～9 张参考图 + 视频 + 音频，单采直出 |
| `04_全能参考_二采放大.json` | 全能参考 + 二采放大精修 |
| `05_舞蹈数字人.json` | 人物图 + 音乐，卡点舞蹈 |
| `06_视频动作迁移.json` | 人物图 + 参考视频，1:1 复刻动作 |
| `07_外部视频3D放大.json` | 对已有视频做 3D 潜空间放大 |
| `08_全能一体_单采极速.json` | 全能一体，单次采样极速版 |
| `09_全能一体_二采精修.json` | 全能一体，二采精修版 |
| `10_全能一体_3D放大锁脸.json` | 全能一体 + 3D 放大 + 人脸锁定 |
| `11_H3数字人V4.json` | 音频驱动数字人说话 / 唱歌 |
| `12_360环绕_单图.json` | 单图 360° 环绕运镜 |
| `13_360环绕_双图.json` | 双图 360° 环绕运镜 |
| `14_全能工作流.json` | 文武双全综合工作流（100+ 节点） |
| `15_时间线导演_无限长视频.json` | 时间线导演台：无限长视频 + 原音锁定 + 二采 |
| `16_时间线导演_低显存版.json` | 时间线导演台低显存 / 低内存版 |
| `17_Omni改视频_二采精品.json` | FastH3-Omni 视频改视频 + 二采放大精品版 |

> `MiniMaxH3ReferenceToVideo` 节点最多支持 **9 张参考图**、**3 段参考视频**、**3 段参考音频**。

---

## 🧱 主要自定义节点

ComfyUI-Manager · VideoHelperSuite · KJNodes · Impact-Pack · Easy-Use · rgthree · LayerStyle · essentials · comfyui_controlnet_aux · LTXVideo · SeedVR2 VideoUpscaler · Inpaint-CropAndStitch · SelfLift · FeiHou-Easy-H3 / Toolbox · MiniMaxH3-Easy · MiniMaxH3-TimelineDirector · H3-Motion-Context · H3-Context-Noise · Minimax_h3_latent_Upscaler · SDPose-OOD · qwenmultiangle · ZenID · AdvancedRefluxControl 等。

## 🧠 模型来源

- [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) · [Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1)
- [FastVideo/FastH3-Omni-Comfy](https://huggingface.co/FastVideo/FastH3-Omni-Comfy) · [FastVideo/FastH3-Omni-NVFP4-QAD-Comfy](https://huggingface.co/FastVideo/FastH3-Omni-NVFP4-QAD-Comfy)
- [FX-FeiHou/MiniMax-H3-Remix](https://huggingface.co/FX-FeiHou/MiniMax-H3-Remix)
- [LBH-123-AI/Minimax_h3_latent_Upscaler](https://huggingface.co/LBH-123-AI/Minimax_h3_latent_Upscaler) 及各社区 LoRA 作者（详见笔记本内下载列表）

---

## ⚠️ 注意事项

- 底模体积很大（单个 13G～64G），请使用 **大显存 + 大磁盘** 的运行时。
- 切换 2～6 号单元格时会自动删除未选中的底模以释放空间。
- 部分社区 LoRA / 底模为未删减（NSFW）版本，请遵守当地法律法规及各模型许可协议，**仅限成年人合法使用**。
- 所有模型版权归原作者所有，本仓库仅提供部署脚本。

---

## 🇬🇧 English

### Overview

A **single-file Google Colab notebook** that deploys **ComfyUI** on a cloud GPU in one click and loads, on demand:

- **MiniMax-H3** — text-to-video, first/last-frame image-to-video, all-in-one reference-to-video (multiple images / videos / audios), talking avatars with lip-sync, 360° orbit camera, and an infinite-length timeline director, all with **native audio-video generation**.
- **FastH3-Omni** (UCSD × NVIDIA) — native 8-step fast reference-to-video, including a Blackwell NVFP4 build.
- **Civitai MiniMax-H3 Remix** — a community 2-in-1 fine-tuned base model.
- **Qwen-Image 2.1** — 2K text-to-image, multi-image editing, outfit swap / consistency, restoration, anime-to-real and more.

Highlights:

- 🧩 **On-demand switching** — only the selected base model is downloaded; unselected ones are **auto-removed** to save disk space.
- 🗂️ **Isolated LoRA & workflow pools** — the H3 video pool and the Qwen image pool never collide.
- 📦 **18 H3 workflows + 12 Qwen workflows built in** (compressed inside the notebook, auto-installed into ComfyUI, **zero missing nodes**).
- ⚡ **Parallel multi-threaded downloads** for nodes, VAEs, upscalers and LoRAs.
- 🌐 **Cloudflare tunnel** public URL (no 403), with **instant restart** that never re-downloads models.
- 📝 Every cell uses Colab **form view** — pick models from dropdowns and press ▶️, no code editing required.

### Quick Start

1. Click the **Open in Colab** badge above (recommended: `File → Save a copy in Drive`).
2. `Runtime → Change runtime type` and pick a **high-VRAM GPU** (recommended **G4 / RTX PRO 6000 Blackwell 96GB**, or A100 80G / H100).
3. (Optional) Paste your own [Civitai API key](https://civitai.com/user/account) into `C站_API_Token` in **cell 1** and **cell 6** to enable Civitai LoRA downloads.
4. **Run cell 1 first on every new session** (installs the base environment).
5. Run **exactly one** of cells 2–6, choose the base model / CLIP in the form; a ComfyUI URL will be printed when ready.
6. If the page disconnects or the link expires, run **cell 7** to restart in seconds without re-downloading.
7. When finished, use `Runtime → Disconnect and delete runtime` to stop consuming compute units.

> [!IMPORTANT]
> The author's private Civitai token has been **replaced with an empty placeholder** in this repository. Without a token, all Hugging Face models still download normally; only login-gated Civitai LoRAs will be skipped.

### Cells

| Cell | Name | Base model & config | Dedicated pool | Use case |
| :--- | :--- | :--- | :--- | :--- |
| **1** | 🛠️ Base framework | ComfyUI core + all custom nodes + shared VAEs / latent upscalers / turbo LoRAs | Runtime foundation | **Run once per session** |
| **2** | 🎬 T2V + First/Last-frame | Official `64G` FL2VA + selectable CLIP | H3 video pool | Text-to-AV, first/last-frame I2V |
| **3** | 🖼️ Reference-to-Video | Official `64G` Ref2VA + selectable CLIP | H3 video pool | Multi-image/video/audio reference, camera control |
| **4** | ⚡ FastH3-Omni | `41G` native 8-step BF16 / `13G` Blackwell NVFP4 | H3 video pool | Fast reference video, video-to-video |
| **5** | 🌟 Civitai H3 Remix | `64G` BF16 / `31G` INT8 community model + uncensored CLIP | H3 pool + Civitai pool | Community fine-tune, 360° orbit |
| **6** | 🎨 Qwen-Image 2.1 | `13.6G` standard / 8-step Turbo / Noct anime model + dedicated CLIP & VAE | Qwen pool (19 LoRAs + 12 workflows) | 2K T2I, multi-image edit, restoration |
| **7** | 🚀 Restart ComfyUI | Keeps all models | Current pool unchanged | Reconnect, fresh tunnel URL |

### Built-in H3 Workflows (18)

| File | Purpose |
| :--- | :--- |
| `00_Omni官方原版.json` | Official Comfy-Org FastH3-Omni reference workflow |
| `01_文生与首尾帧.json` | Text-to-video / first-last-frame I2V |
| `02_文生与首尾帧_二采放大.json` | Same + 2-pass latent upscale |
| `03_全能参考_直出.json` | 1–9 reference images + video + audio, single pass |
| `04_全能参考_二采放大.json` | Reference-to-video + 2-pass refine |
| `05_舞蹈数字人.json` | Character image + music → beat-synced dance |
| `06_视频动作迁移.json` | Character image + reference video → 1:1 motion transfer |
| `07_外部视频3D放大.json` | 3D latent upscale for existing videos |
| `08_全能一体_单采极速.json` | All-in-one, single-pass fast |
| `09_全能一体_二采精修.json` | All-in-one, 2-pass refined |
| `10_全能一体_3D放大锁脸.json` | All-in-one + 3D upscale + face lock |
| `11_H3数字人V4.json` | Audio-driven talking / singing avatar |
| `12_360环绕_单图.json` | Single-image 360° orbit |
| `13_360环绕_双图.json` | Dual-image 360° orbit |
| `14_全能工作流.json` | Comprehensive combat + drama workflow (100+ nodes) |
| `15_时间线导演_无限长视频.json` | Timeline director: infinite length + audio lock + 2-pass |
| `16_时间线导演_低显存版.json` | Timeline director, low VRAM / RAM |
| `17_Omni改视频_二采精品.json` | FastH3-Omni video-to-video + 2-pass upscale |

> The `MiniMaxH3ReferenceToVideo` node accepts up to **9 reference images**, **3 reference videos** and **3 reference audios**.

### Notes

- Base models are large (13G–64G each) — use a runtime with **plenty of VRAM and disk**.
- Switching between cells 2–6 automatically deletes unselected base models to free space.
- Some community LoRAs / models are uncensored (NSFW). Please comply with local laws and each model's license — **adults only, lawful use only**.
- All models belong to their original authors; this repository only provides deployment scripts.

---

⭐ If this helps you, please give it a star! / 如果对你有帮助，欢迎点个 Star！
