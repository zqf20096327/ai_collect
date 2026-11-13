# 🎬 MiniMax-H3 · HyperFlow 14B · H3-Image 33.1B & Qwen-Image 2.1 全能工作台 · All-in-One ComfyUI Colab Studio

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/joker124zx/minimax-h3-qwen-comfyui-colab/blob/main/MiniMax_H3_Qwen2.1_ComfyUI_Colab.ipynb)
![ComfyUI](https://img.shields.io/badge/ComfyUI-latest-blue)
![MiniMax-H3](https://img.shields.io/badge/MiniMax--H3-Video%20%2B%20Audio-purple)
![HyperFlow 14B](https://img.shields.io/badge/HyperFlow-14B%206--Step-ff6b35)
![H3-Image 33.1B](https://img.shields.io/badge/H3--Image-33.1B%204MP%2F16MP-10b981)
![Qwen-Image 2.1](https://img.shields.io/badge/Qwen--Image-2.1-orange)
![GPU](https://img.shields.io/badge/GPU-96GB%20Blackwell%20(G4)-green)

**中文** | [English](#-english)

---

## 📖 简介

一个 **单文件 Google Colab 笔记本**，一键在云端 GPU（默认推荐 **G4 / RTX PRO 6000 Blackwell 96GB**，支持随时手动切换 A100 / H100 / L4）上部署 **ComfyUI**，并按需加载：

- **MiniMax-H3 (31B)**：文生视频、首尾帧图生视频、1:1 九宫格多图/视频/音频全能参考视频（Ref2VA）、Pika 6步 2K 超清放大、二阶段一采成型二采修脸、无限时长数字人（像素幻想Lab双采版）、PrefixStream 素材箱长视频无限续写、人物替换导演台、YCNodes 分块二采、360° 单/双图环绕运镜等，**原生音画同步**。
- **FastH3-Omni**（UCSD × NVIDIA）：原生 8 步极速全参考视频，含 Blackwell NVFP4 加速版。
- **C 站 MiniMax-H3 Remix & PRISM**：社区二合一微调底模（64G BF16 / 31G INT8）及 `PRISM×10Eros×PikaFlex`（19.2G INT8）三合一破限极速底模。
- **⚡💋🖼️ HyperFlow 14B + H3 Eros Max 31B + H3-Image 33.1B 三合一王牌组合（新增第 6 格）**：
  - **HyperFlow Flash 14B**：6 步极速文生 / 首尾帧 / 多图全参有声视频（`fl2va 14.9G + ref2va 15.3G` INT8 ConvRot 或 GGUF 可选）；
  - **H3 Eros Max 31B (beta7 INT8 HQ)**：`21.3G` 社区预融合 8 步 Turbo 高清有声视频底模；
  - **MiniMax H3-Image Full INT8 (33.1B)**：`31.7G` 6 步 PDD 原生直出 4MP/16MP 超清大图 & 16 图参考改图；
  - 三套底模**共用同一个 25G 未删减 CLIP** 与音视频 VAE，并内置「**33.1B 满血生图直连 HyperFlow 6 步有声视频一条龙**」工作流！
- **千问 Qwen-Image 2.1**：2K 文生图、单图精准编辑（支持挂载 LoRA）、多图合成编辑（8步极速）、双图换装、角色三视图、360° 多角度相机、3D 角色姿势画廊、8MP 分块超清修复、万物转动漫与夜曲破限动漫专版。

### ✨ 最新升级亮点

- ⚡💋🖼️ **第 6 格「HyperFlow 14B + Eros Max 31B + H3-Image 33.1B」三合一生态（12 套专属工作流）**：不用切格、不用重复加载 CLIP，一格同时畅玩 4MP/16MP 满血超清生图改图、14B 6步极速视频、31B 8步高清视频，以及生图无缝直转有声视频一条龙。
- 🛡️ **容器页缓存防爆 + 抗代理闪断 + 冷启动零崩溃加固**：
  - 每下完大权重自动执行 `os.sync() + POSIX_FADV_DONTNEED` 主动释放 Linux 页缓存 + `--cache-ram 32` 封顶，138GB 高速落盘系统 RAM 稳定保持在 `4～5 GB`，彻底杜绝 G4 容器内存被页缓存顶爆重置；
  - 静默后台下载进度监控（零 `iopub` 日志风暴、零双向 `eval_js` 死锁），即使家宽代理短暂抖动也不会卡死在“正在恢复执行”；
  - 全本 Colab 主内核零 C 扩展库加载（子进程隔离生成占位图 + 纯标准库 PNG 兜底），新开机从第 1 格到第 6 格一次直通不崩内核。
- 🖼️ **1:1 整齐九宫格全参工作流（双版本）**：
  - `🔥H3九宫格全参防崩工作流_1比1整齐复刻版.json`：原生 720p/1080p 满血直出，彻底剔除一阶段降采样导致的肢体粘连与崩坏。
  - `🔥H3九宫格全参_Pika6步2K超清放大工作流.json`：集成 **Pika H3 Flex 6步极速加速 LoRA** + `SelfLiftH3Sampler`（一阶段 4 步 720p 成型 + 二阶段 2 步 3D 潜空间真 2K `1088×1920` 超清放大）。
- 💓 **防休眠保活 + 崩溃 3 秒自动复活守护**：每 15 秒巡检 `ComfyUI (8188)` 与 `cloudflared` 隧道，若因显存峰值闪退，**3 秒内自动原地重启恢复，原 Cloudflare 网址保持不变**。
- 🚀 **全内存 Gzip 静态资源缓存 (`_FILE_MEM_CACHE`)**：对前端脚本、样式、扩展与 `object_info` 进行内存级预压缩缓存，大幅提升 Cloudflare 隧道首次打开网页的速度。
- 🧩 **按需切换架构 & 三池完全隔离**：经典 H3 视频池（11 套）、HyperFlow+ErosMax+H3-Image 三合一池（12 套）、千问图像池（13 套）共 **36 套精调工作流**完全隔离，合法 RFC-4122 UUID 零报错。

---

## 🚀 快速开始

1. 点击上方 **Open in Colab** 徽章打开笔记本（建议 `文件 → 在云端硬盘中保存一份副本`）。
2. 默认已配置为 **G4 (96GB Blackwell)** 显卡；如需更换可在 `代码执行程序 → 更改运行时类型` 中自由切换。
3. （可选）在 **单元格 1 / 6 / 7** 的 `C站_API_Token` 中填入你自己的 [Civitai API Key](https://civitai.com/user/account)，用于下载 C 站底模与 LoRA。
4. **每次开机先运行 单元格 1**（安装底座环境、31 个高阶自定义节点、公共 VAE / 放大器与加速 LoRA 池）。
5. 根据需求 **运行 2～7 中的任意一个** 单元格，运行后会输出 Cloudflare 公网访问链接并进入后台防断连守护状态（如需切换其他模型单元格，点击左上角 ⏹️ 停止当前格即可）。
6. 网页断开或需要刷新隧道时，运行 **单元格 8** 秒级重启，不会重新下载模型。

> [!IMPORTANT]
> 本仓库公开版本已将私人 Civitai Token **全部清空为占位符 `""`**。不填写 Token 时，Hugging Face 上的所有底模、CLIP、VAE、Pika 6步 LoRA 等均可正常下载（第 6 格 H3-Image 未填 Token 无法直连 C 站时也会自动回退至 Hugging Face 官方 INT8 生图底模）。

---

## 🧭 单元格说明（1～8）

| 单元格 | 名称 | 核心底模与配置 | 专属池（LoRA + 工作流） | 适用场景 |
| :--- | :--- | :--- | :--- | :--- |
| **1️⃣** | 🛠️ 必备基础框架 | ComfyUI 核心 + 31 个高阶自定义节点 + 核心 VAE / 潜空间放大器 | 初始化运行底座与加速 LoRA 池 | **每次新开机必点一次** |
| **2️⃣** | 🎬 文生 + 首尾帧视频 | 官方 `64G` FL2VA 底模 + 自选 CLIP | H3 视频池（11 套精调工作流） | 原版满血文生音视频、首尾帧 |
| **3️⃣** | 🖼️ 全参视频 | 官方 `64G` Ref2VA 底模 + 自选 CLIP | H3 视频池（11 套精调工作流） | 1:1 九宫格多图/音/视全参、数字人 |
| **4️⃣** | ⚡ FastH3-Omni 实时全参 | `41G` 原生 8 步 BF16 / `13G` Blackwell NVFP4 | H3 视频池（11 套精调工作流） | 极速全能参考视频、低步数预览 |
| **5️⃣** | 🌟 C 站 Remix / PRISM | `64G/31G` Remix 或 `19G` PRISM 三合一微调底模 + 未删减 CLIP | H3 视频池 + C 站增强池 | 31B 社区写实微调、分块二采 |
| **6️⃣** | ⚡💋🖼️ **HyperFlow 14B + Eros Max 31B + H3-Image 33.1B 三合一** | `30.2G` HyperFlow(6步) + `21.3G` Eros Max 31B(8步) + `31.7G` H3-Image 33.1B(6步) + 共用 25G CLIP | **三合一专属池（12 套专属工作流 + 36 款增强 LoRA）** | **开一格同时畅玩 4MP/16MP 满血生图改图 + 14B/31B 双视频 + 一条龙直转** |
| **7️⃣** | 🎨 千问 Qwen-Image 2.1 | `13.6G` 标准 / 8 步 Turbo / 夜曲动漫底模 + 专用双 CLIP & VAE | 千问图像池（13 套专属工作流 + 19 款 LoRA） | 2K 文生图、双图换装、姿势画廊、8MP 修复 |
| **8️⃣** | 🚀 单独重启 ComfyUI | 不删模型、不重下，10 秒重开后端与免 403 隧道 | 保持当前已选模型池不变 | 网页断连恢复、刷新获取新隧道链接 |

---

## 📦 内置工作流清单（共 36 套）

### ⚡💋🖼️ 第 6 格：HyperFlow + Eros Max + H3-Image 33.1B 三合一专属工作流（12 套）

| 文件名 | 核心用途与特点 |
| :--- | :--- |
| `⚡1_HyperFlow官方_文生音视频_6步极速.json` | HyperFlow Flash 14B 原生 6 步极速文生音画同步视频 |
| `⚡2_HyperFlow官方_首帧图生音视频_6步极速.json` | 单首帧图生 6 步极速有声视频 |
| `⚡3_HyperFlow官方_首尾帧音视频_6步极速.json` | 首尾帧丝滑过渡 6 步有声视频 |
| `⚡4_HyperFlow官方_多图全参音视频_6步极速.json` | 多图全能参考（Ref2VA）6 步有声视频 |
| `🔥5_HyperFlow破限NSFW_文生音视频+C站大人LoRA版.json` | HyperFlow 6 步文生有声视频 + 社区增强 LoRA 串联 |
| `🔥6_HyperFlow破限NSFW_首尾帧图生+C站大人LoRA版.json` | HyperFlow 6 步首尾帧图生 + 社区增强 LoRA 串联 |
| `🔥7_HyperFlow破限NSFW_多图全参+C站大人LoRA版.json` | HyperFlow 6 步多图全参 + 社区增强 LoRA 串联 |
| `🖼️8_H3Image满血33B_6步4MP超清破限文生图.json` | MiniMax H3-Image Full INT8 (33.1B) 6 步 PDD 原生 4MP/16MP 超清文生图 |
| `🖼️9_H3Image满血33B_6步4MP破限改图与16图参考.json` | MiniMax H3-Image 33.1B 6 步精准指令改图与最高 16 图参考融合 |
| `🚀10_H3Image满血生图直连HyperFlow_一条龙破限生图转有声视频.json` | **一条龙推荐**：33.1B 满血生出超清首帧后直接喂入 HyperFlow 14B 生成有声视频 |
| `💋11_ErosMax破限融合31B_首尾帧与文生音视频_8步极速.json` | H3 Eros Max 31B（beta7 INT8 HQ）8 步 Turbo 首尾帧 / 文生有声视频 |
| `💋12_ErosMax破限融合31B_多图全参音视频_8步九宫格版.json` | H3 Eros Max 31B 8 步多图全参九宫格有声视频 |

### 🎬 第 2～5 格：经典 31B H3 视频工作流（11 套主力精调版）

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

### 🎨 第 7 格：千问 Qwen-Image 2.1 工作流（13 套专属版）

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

- **MiniMax-H3 (31B)** — text-to-video, first/last-frame I2V, 1:1 9-Grid full-parameter reference-to-video (up to 9 images + 3 videos + 3 audios), Pika 6-Step 2K latent upscale, 2-stage face refinement, infinite talking avatar, PrefixStream long-video continuation, character swap director, YCNodes tiled 2-pass, and 360° single/dual-image orbit camera, with **native audio-video generation**.
- **FastH3-Omni** (UCSD × NVIDIA) — native 8-step fast reference-to-video, including a Blackwell NVFP4 build.
- **Civitai MiniMax-H3 Remix & PRISM** — community fine-tuned models (`64G` BF16 / `31G` INT8 / `19.2G` PRISM×10Eros×PikaFlex 3-in-1).
- **⚡💋🖼️ HyperFlow 14B + H3 Eros Max 31B + H3-Image 33.1B 3-in-1 Suite (Cell 6 — NEW)** — combines 6-step **HyperFlow Flash 14B** (`fl2va` + `ref2va`), 8-step **H3 Eros Max 31B (beta7 INT8 HQ)**, and 6-step **MiniMax H3-Image Full INT8 (33.1B)** native 4MP/16MP T2I & 16-image editing, sharing a single **25G uncensored CLIP** with 12 dedicated workflows (including a one-click **H3-Image → HyperFlow Video** pipeline).
- **Qwen-Image 2.1 (Cell 7)** — 13 workflows covering 2K T2I, LoRA-enabled single-image editing, 8-step multi-image composition, outfit swap, character turnaround sheets, 360° multi-angle camera, 3D pose gallery, and 8MP tiled upscaling.

### Key Upgrades
- **Cell 6 All-Star 3-in-1 Suite**: Native 4MP/16MP image generation + 14B 6-step & 31B 8-step audio-video generation in a single workspace without reloading CLIP.
- **Container Page-Cache Eviction & Crash Hardening**: Automatic `os.sync() + POSIX_FADV_DONTNEED` keeps container RAM around `4–5 GB` across 138 GB of model downloads; zero blocking `eval_js` calls, silent `aria2c` progress monitoring, and subprocess-isolated image helpers ensure rock-solid cold starts even over unstable proxies.
- **1:1 9-Grid Full-Parameter Workflows & G4 Blackwell (`sm_120`) Stability Fixes**: Native 720p/1080p zero-downscale direct output + Pika 6-step 2K (`1088×1920`) progressive upscale, with 3-second auto-resurrection guardian.

> [!IMPORTANT]
> All private Civitai API tokens have been **stripped to empty placeholders (`""`)** in this repository. Paste your own [Civitai API key](https://civitai.com/user/account) into `C站_API_Token` in Cell 1 / 6 / 7 if you wish to download login-gated Civitai models and LoRAs.

---

⭐ If this helps you, please give it a star! / 如果对你有帮助，欢迎点个 Star！
