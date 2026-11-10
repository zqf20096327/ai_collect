# 🎬 MiniMax-H3 & Qwen-Image 2.1 全能工作台 · All-in-One ComfyUI Colab Studio

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/joker124zx/minimax-h3-qwen-comfyui-colab/blob/main/MiniMax_H3_Qwen2.1_ComfyUI_Colab.ipynb)
![ComfyUI](https://img.shields.io/badge/ComfyUI-latest-blue)
![MiniMax-H3](https://img.shields.io/badge/MiniMax--H3-Video%20%2B%20Audio-purple)
![Qwen-Image 2.1](https://img.shields.io/badge/Qwen--Image-2.1-orange)
![GPU](https://img.shields.io/badge/GPU-96GB%20Blackwell%20(G4)-green)

**中文** | [English](#-english)

---

## 📖 简介

一个 **单文件 Google Colab 笔记本**，一键在云端 GPU（默认推荐 **G4 / RTX PRO 6000 Blackwell 96GB**，支持随时手动切换 A100 / H100 / L4）上部署 **ComfyUI**，并按需加载：

- **MiniMax-H3**：文生视频、首尾帧图生视频、1:1 九宫格多图/视频/音频全能参考视频（Ref2VA）、Pika 6步 2K 超清放大、二阶段一采成型二采修脸、无限时长数字人（像素幻想Lab双采版）、PrefixStream 素材箱长视频无限续写、人物替换导演台、YCNodes 分块二采、360° 单/双图环绕运镜等，**原生音画同步**。
- **FastH3-Omni**（UCSD × NVIDIA）：原生 8 步极速全参考视频，含 Blackwell NVFP4 加速版。
- **C 站 MiniMax-H3 Remix & PRISM**：社区二合一微调底模（64G BF16 / 31G INT8）及 `PRISM×10Eros×PikaFlex`（19.2G INT8）三合一破限极速底模。
- **千问 Qwen-Image 2.1**：2K 文生图、单图精准编辑（支持挂载 LoRA）、多图合成编辑（8步极速）、双图换装、角色三视图、360° 多角度相机、3D 角色姿势画廊、8MP 分块超清修复、万物转动漫与夜曲破限动漫专版。

### ✨ 最新升级亮点

- 🖼️ **1:1 整齐九宫格全参工作流（双版本）**：
  - `🔥H3九宫格全参防崩工作流_1比1整齐复刻版.json`：原生 720p/1080p 满血直出，彻底剔除一阶段降采样导致的肢体粘连与崩坏。
  - `🔥H3九宫格全参_Pika6步2K超清放大工作流.json`：集成 **Pika H3 Flex 6步极速加速 LoRA** + `SelfLiftH3Sampler`（一阶段 4 步 720p 成型 + 二阶段 2 步 3D 潜空间真 2K `1088×1920` 超清放大）。
- 🛡️ **G4 Blackwell (`sm_120`) 深度防崩调优**：全系主力工作流默认旁路不兼容的 `SageAttention` 与多人场景易粘连的 `BlockSparseAttention`，多人互动画面手脚清晰稳定。
- 💓 **三重防休眠保活 + 崩溃 3 秒自动复活守护**：
  - 单元格尾部内置前台 `Busy` 守护循环（防止 Colab 因内核空闲 15 分钟自动掐断回收）+ 每 45 秒双向 RPC 心跳。
  - 每 15 秒巡检 `ComfyUI (8188)` 与 `cloudflared` 隧道：若因显存峰值闪退，**3 秒内自动原地重启恢复，原 Cloudflare 网址保持不变**。
- 🚀 **全内存 Gzip 静态资源缓存 (`_FILE_MEM_CACHE`)**：对前端脚本、样式、扩展与 `object_info` 进行内存级预压缩缓存，大幅提升 Cloudflare 隧道首次打开网页的速度。
- 🧩 **按需切换架构 & LoRA/工作流池隔离**：H3 视频池（11 套精调工作流）与千问图像池（13 套专属工作流）完全隔离，下拉菜单清爽不混杂。

---

## 🚀 快速开始

1. 点击上方 **Open in Colab** 徽章打开笔记本（建议 `文件 → 在云端硬盘中保存一份副本`）。
2. 默认已配置为 **G4 (96GB Blackwell)** 显卡；如需更换可在 `代码执行程序 → 更改运行时类型` 中自由切换。
3. （可选）在 **单元格 1** 和 **单元格 6** 的 `C站_API_Token` 中填入你自己的 [Civitai API Key](https://civitai.com/user/account)，用于下载 C 站 LoRA。
4. **每次开机先运行 单元格 1**（安装底座环境、自定义节点、公共 VAE / 放大器与加速 LoRA 池）。
5. 根据需求 **运行 2～6 中的任意一个** 单元格，运行后会输出 Cloudflare 公网访问链接并进入后台防断连守护状态（如需切换其他模型单元格，点击左上角 ⏹️ 停止当前格即可）。
6. 网页断开或需要刷新隧道时，运行 **单元格 7** 秒级重启，不会重新下载模型。

> [!IMPORTANT]
> 本仓库公开版本已将私人 Civitai Token **清空为占位符 `""`**。不填写 Token 时，Hugging Face 上的所有底模、CLIP、VAE、Pika 6步 LoRA 等均可正常下载。

---

## 🧭 单元格说明

| 单元格 | 名称 | 核心底模与配置 | 专属池（LoRA + 工作流） | 适用场景 |
| :--- | :--- | :--- | :--- | :--- |
| **1️⃣** | 🛠️ 必备基础框架 | ComfyUI 核心 + 全部高阶自定义节点 + 3款核心 VAE / 潜空间放大器 | 初始化运行底座与加速 LoRA 池 | **每次新开机必点一次** |
| **2️⃣** | 🎬 文生 + 首尾帧视频 | 官方 `64G` FL2VA 底模 + 自选 CLIP | H3 视频池（11 套精调工作流） | 文生音视频、首尾帧图生视频 |
| **3️⃣** | 🖼️ 全参视频 | 官方 `64G` Ref2VA 全参底模 + 自选 CLIP | H3 视频池（11 套精调工作流） | 九宫格多图/视频/音频参考、换人换脸、数字人 |
| **4️⃣** | ⚡ FastH3-Omni 极速版 | `41G` 原生 8 步 BF16 + `13G` Blackwell NVFP4 | H3 视频池（11 套精调工作流） | 极速多参生成、低步数高帧率预览 |
| **5️⃣** | 🌟 C 站 H3 Remix / PRISM | `64G/31G` Remix 或 `19.2G` PRISM 三合一破限底模 + 未删减 CLIP | H3 视频池 + C 站增强池 | 社区微调、6步极速融合、分块二采、360° 环绕 |
| **6️⃣** | 🎨 千问 Qwen-Image 2.1 | `13.6G` 标准 / 8 步 Turbo / 夜曲动漫底模 + 专用双 CLIP & VAE | 千问专属池（19 款 LoRA + 13 套工作流） | 2K 文生图、单图LoRA编辑、多图合成、姿势画廊 |
| **7️⃣** | 🚀 单独重启 ComfyUI | 不删模型、不重下，10 秒重开后端与免 403 隧道 | 保持当前已选模型池不变 | 网页断连恢复、刷新获取新隧道链接 |

---

## 📦 内置工作流清单

### 🎬 H3 视频工作流（11 套主力精调版）

| 文件名 | 核心用途与特点 |
| :--- | :--- |
| `🔥H3九宫格全参防崩工作流_1比1整齐复刻版.json` | **主力推荐**：1:1 整齐九宫格布局（支持 1～9 图 + 3 音 + 3 视 + 左侧独立忽略开关），原生 720p/1080p 零缩放直出防崩版 |
| `🔥H3九宫格全参_Pika6步2K超清放大工作流.json` | **2K 极速推荐**：同上 1:1 九宫格布局，搭载 Pika 6步 LoRA + `SelfLift`（4步 720p 成型 + 2步真 2K `1088×1920` 潜空间放大） |
| `🔥H3全参文生视频_20步原生防崩直出工作流.json` | 用全参底模跑 20 步高遵循度原生文生音视频，解决普通文生人物肢体扭曲问题 |
| `🔥H3全参二阶段2K精修_一采成型二采修脸工作流.json` | 双阶段采样：一阶段构图成型 + 二阶段 2K 潜空间放大修脸与细节重绘 |
| `首尾帧工作流.json` | 首尾帧图生视频 + 多 LoRA 串联控制 |
| `MiniMaxH3无限时长数字人工作流_像素幻想Lab双采版.json` | 音频驱动无限时长数字人说话/唱歌（双采样高清锁脸版） |
| `H3长视频无限续写_PrefixStream素材箱接力工作流.json` | 基于 PrefixStream 素材箱接力的多段长视频无限续写工作流 |
| `人物替换导演台工作流.json` | 视频换人 / 角色替换 / 动作迁移导演台 |
| `H3高阶_YCNodes分块二采工作流.json` | YCNodes 高阶分块二次采样超清精修工作流 |
| `12_360环绕_单图.json` | 单图输入 360° 子弹时间环绕运镜（配 `360-Orbit-LoRA`） |
| `13_360环绕_双图.json` | 双图输入 360° 环绕运镜过渡 |

### 🎨 千问 Qwen-Image 2.1 工作流（13 套专属版）

| 文件名 | 核心用途 |
| :--- | :--- |
| `qwen21文生图.json` | 标准 2K 文生图（内置亚洲人像美学、画质修复、写实真人、佳能质感等多款 LoRA 串联） |
| `qwen21单图精准编辑_支持LoRA.json` | 单图指令精准改图（支持挂载任意千问 LoRA） |
| `qwen21多图合成编辑_极速8步.json` | 多张参考图融合编辑（8 步 Turbo 极速出图） |
| `qwen21极速生图改图扩写放大一体.json` | 生图 + 改图 + 扩图 + 放大全合一工作台 |
| `qwen21双图换装编辑.json` | 角色固定 + 服装参考图一键换装 |
| `qwen21角色三视图.json` | 单张角色图生成正/侧/背标准角色三视图 |
| `qwen21多角度.json` | 360° 多角度相机视角自由旋转生成 |
| `qwen21姿势迁移.json` | 3D 角色姿势画廊 + SDPose 骨骼姿势迁移 |
| `qwen21涂鸦编辑.json` | 画板局部涂鸦重绘编辑 |
| `qwen21分块高清修复放大8MP.json` | 8MP 超高清分块放大修复 |
| `qwen21万物转动漫.json` | 真人/实景照片一键转二次元动漫风格 |
| `qwen21图片放大.json` | 图像超清细节重绘放大 |
| `qwen21夜曲破限动漫专版.json` | NoctQA 夜曲破限动漫底模专属生图工作流 |

---

## 🇬🇧 English

### Overview

A **single-file Google Colab notebook** that deploys **ComfyUI** on a cloud GPU (defaults to **G4 / RTX PRO 6000 Blackwell 96GB**, freely switchable to A100 / H100 / L4) and loads on demand:

- **MiniMax-H3** — text-to-video, first/last-frame I2V, 1:1 9-Grid full-parameter reference-to-video (up to 9 images + 3 videos + 3 audios), Pika 6-Step 2K latent upscale, 2-stage face refinement, infinite talking avatar, PrefixStream long-video continuation, character swap director, YCNodes tiled 2-pass, and 360° single/dual-image orbit camera, with **native audio-video generation**.
- **FastH3-Omni** (UCSD × NVIDIA) — native 8-step fast reference-to-video, including a Blackwell NVFP4 build.
- **Civitai MiniMax-H3 Remix & PRISM** — community fine-tuned models (`64G` BF16 / `31G` INT8 / `19.2G` PRISM×10Eros×PikaFlex 3-in-1).
- **Qwen-Image 2.1** — 13 workflows covering 2K T2I, LoRA-enabled single-image editing, 8-step multi-image composition, outfit swap, character turnaround sheets, 360° multi-angle camera, 3D pose gallery, and 8MP tiled upscaling.

### Key Upgrades
- **1:1 9-Grid Full-Parameter Workflows**: Both native 720p/1080p zero-downscale anti-crash direct output and Pika 6-step 2K (`1088×1920`) progressive upscale.
- **G4 Blackwell (`sm_120`) Stability Fixes**: Bypasses incompatible `SageAttention` / `BlockSparseAttention` nodes to prevent multi-character limb distortion.
- **Triple Keep-Alive & 3-Second Auto-Resurrection Guardian**: Keeps the Colab kernel `Busy` to prevent 15-minute idle disconnects, sends periodic RPC heartbeats, and automatically restarts `ComfyUI` or `cloudflared` within 3 seconds if a crash occurs.

---

⭐ If this helps you, please give it a star! / 如果对你有帮助，欢迎点个 Star！
