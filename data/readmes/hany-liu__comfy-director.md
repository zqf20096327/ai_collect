# ComfyDirector

> ComfyUI 本地长视频导演台 —— 把一句话故事，炼成一支电影级 AI 长视频。

ComfyDirector 是本机运行的 **MiniMax H3 长视频导演台**：你在浏览器里输入一段故事，它会自动拆分剧本、维护角色一致性、逐段生成并审核视频，最后拼接成一支完整成片。真正的图生视频由你本机已有的 ComfyUI 工作流执行——ComfyDirector 负责导演、调度与质检。

## 🔒 为什么选本地

- **数据不出门**：故事剧本、角色脸图、生成视频全部留在本机磁盘，不调用任何云端视频 API，无内容审查与隐私顾虑
- **零 API 成本**：生成消耗的是你自己的显卡，没有按分钟/按张计费
- **断网可用**：除模型下载外，整个创作流程不需要互联网

## 💻 本机实测配置

以下数据来自开发机实测（RTX 4070 12GB，Windows）：

| 场景 | 实测数据 |
|---|---|
| 原生 H3 画布上限 | 992×1792（峰值显存 11.5 GiB，约 7 分钟/段）；1024×1856 起显存颠簸，不推荐 |
| 标准档 480×864 | 约 2~3 分钟/段 |
| 人脸修复（CodeFormer） | 约 2.1 秒/帧，峰值显存 ~2.3 GB，可与生成共存 |
| RTX 2× 超分 | 已验证最高 4×（竖屏 1920×3456），生产默认 2× |

显存 12GB 及以上即可流畅跑全部规格；8GB 显卡建议只用 480×864 标准档并关闭超分。

## ✨ 功能亮点

**剧本与规划**
- 一句话故事 → 自动拆分为可编辑的 5 秒分段剧本
- 支持 5 秒 ~ 10 分钟（600 秒）总时长，按 5 秒倍数自由设定
- 可选接入本地 OpenAI-compatible 规划器（如 Qwen）自动生成分段剧情
- 可选镜头风格（缓推 / 缓拉 / 左摇 / 右摇 / 手持跟拍），生成时自动把运镜提示注入每段 H3 提示词，项目内可随时修改

**角色一致性**
- 唯一必须的人工素材：一张脸部参考照片
- 脸图 → 四视图角色表（2×2 拼版）→ 首图，三级素材链路逐级选用
- 每段视频用 `frame_idx=0` 严格锚定开头，续段以上一段已接受的第 119 帧续写

**逐段生成与审核**
- 每段 5 秒 / 24fps / 120 帧，逐段生成、逐段预览、逐段接受，不批量霸占 GPU
- 每个候选版本进入历史候选库，随时回退改选，不覆盖原始素材
- 首帧、四视图、首图均支持「上传」或「AI 生成」双来源
- **一键自动审批全片**：素材就绪后在时间线点「一键生成全片」，按顺序生成并自动接受全部片段，跑完自动拼接成片；可随时停止、可断点续跑
- **砍掉重做**：跑完全片后哪一段不满意，点该段的「砍掉这一段」撤销当前选择（历史候选保留），改好剧情后从该段一键续跑或逐段重试

**后处理**
- **人脸修复**：可选 CodeFormer 逐段修复脸部细节（显存与耗时显著增加）
- **RTX 2× 超分**：每个候选独立超分到项目尺寸的 2 倍（960×1728 / 1728×960），拼接时全高清或全原片，绝不混用分辨率
- 成片自动拼接，时长与规格与项目严格一致
- **SRT 软字幕**：拼接时按各段剧情自动生成同名 `.srt` 字幕文件（5 秒/段对齐），播放器自动挂载，可从成片卡片下载
- **整片旁白配音（可选）**：独立「配音工作间」按钮导引，非必选、不影响主流程。提供旁白文字 + 参考音视频，调用本机 CosyVoice3 zero-shot 生成整片旁白；多版候选经审核后可在成片时选择其一，第二道 FFmpeg 混为 AAC 音轨（短补静音、长截断对齐视频时长）。新建项目表单另有「旁白先导」块：临时生成测长 → 按 5 秒倍数推荐总长并自动填入

**工程能力**
- 成片规格四档：480×864 / 864×480 / **992×1792** / 1792×992（大尺寸为原生 H3 画布实测工程上限）
- 生成前自动 `POST /free` 释放显存，低显存机器可关闭
- Windows 一键启动 / 状态 / 停止脚本；全程中文界面与错误提示

## 🖼 界面预览

**新建项目** —— 一句话故事 + 四档成片规格 + 可选人脸修复：

![新建项目表单](docs/screenshots/01-create-form.png)

**多项目管理** —— 所有项目保存在本机 `projects/` 目录：

![项目列表](docs/screenshots/02-project-list.png)

**准备素材** —— 脸图 → 四视图角色表 → 首图，三级素材逐级选用，候选库随时回退：

![准备素材](docs/screenshots/03-preparation.png)

**时间线** —— 逐段生成、逐段审核，每个候选可切换历史版本、独立 2× 超分：

![时间线](docs/screenshots/04-timeline.png)

**成片** —— 全部片段接受后一键拼接：

![成片拼接](docs/screenshots/05-final-card.png)

## 📦 依赖前提

| 依赖 | 要求 | 说明 |
|---|---|---|
| Node.js | 20+ | 运行导演台服务 |
| FFmpeg | 在 PATH 中 | 视频规范化与拼接（或用 `DIRECTOR_FFMPEG` 指定路径） |
| ComfyUI | 运行于 `http://127.0.0.1:8000` | 导演台不代管它的启停；需已装好 MiniMax H3 图生视频工作流所需模型，以及 Krea2（角色素材生成）、ReActor/CodeFormer（人脸修复，可选） |
| GPU | NVIDIA，建议 12GB+ 显存 | 8GB 可跑标准档；详见上方实测配置 |

## 🚀 快速开始

**方式一：一键脚本（推荐）**

1. 先启动 ComfyUI
2. 双击根目录 `start-director.bat`（后台启动并打开浏览器，重复执行不会重复启动）
3. 用 `status-director.bat` 查看导演台 / ComfyUI / GPU 状态，用 `stop-director.bat` 关闭

**方式二：npm**

```bash
npm install
npm start            # 前台启动，浏览器打开 http://127.0.0.1:8790
npm run status       # 查看导演台、ComfyUI 与 NVIDIA GPU 状态
npm stop             # 只关闭导演台，不关闭 ComfyUI
```

启动后输入故事与时长即可开始创作。项目默认保存在 `projects/`，可用 `DIRECTOR_PROJECTS_DIR` 改到更大磁盘。

## 🤖 模型清单

导演台工作流实际引用的模型（需放入 ComfyUI `models/` 对应子目录）：

**MiniMax H3 视频生成**（`models/diffusion_models`、`models/text_encoders`、`models/vae`、`models/loras`）

| 文件 | 角色 |
|---|---|
| `minimax_h3_ref2va_pruned_int8_convrot.safetensors` | 主模型（图生视频 DiT，int8） |
| `qwen3vl_32b_minimax_h3_int8_convrot.safetensors` | 文本编码器（Qwen3-VL 32B） |
| `minimax_h3_fl2v_lightx2v_turbo_4step_v0.1_comfy.safetensors` | LoRA（首帧驱动 4 步加速） |
| `minimax_h3_video_vae_fp16.safetensors` / `minimax_h3_audio_vae_fp32.safetensors` | 视频 / 音频 VAE |

**Krea2 角色素材生成**（四视图角色表与首图，`models/diffusion_models`、`models/text_encoders`、`models/vae`、`models/loras`）

| 文件 | 角色 |
|---|---|
| `krea2_turbo_fp8_scaled.safetensors` | 主模型（图像生成） |
| `qwen3vl_4b_fp8_scaled.safetensors` | 文本编码器（Qwen3-VL 4B） |
| `qwen_image_vae.safetensors` | VAE |
| `Krea2-四视图QuadView_krea2_v1.safetensors` | LoRA（2×2 四视图拼版） |
| `krea2_identity_edit_v1_2_r128.safetensors` | LoRA（身份保持编辑 / 首图） |

**人脸修复（可选，`models/insightface`、`models/facerestore_models`）**

| 文件 | 角色 |
|---|---|
| `GFPGANv1.4.pth`（默认）或 CodeFormer | 人脸修复模型 |
| `retinaface_resnet50`（insightface） | 人脸检测 |

RTX 2× 超分使用 `RTXVideoSuperResolution` 节点内置模型，无需额外下载。

## 🎬 工作流程

```
输入故事与时长 → 上传脸部参考 → 生成/上传四视图角色表 → 生成/上传首图
      → 逐段生成视频 → 逐段预览与接受 → 拼接最终成片
      → 或 一键自动审批全片（全段生成并自动接受）→ 不满意的段砍掉重做 → 自动拼接成片
```

- 只有「脸图 → 已选四视图 → 已选首图」全部完成，才能生成第 1 段
- 改选上游素材会清除下游当前选择，但保留全部历史候选，可随时回退
- 每段满意后点「选用这个版本」；全部接受后点「拼接最终成片」
- 想省去逐段点选时，可在时间线「一键生成全片」自动审批；成片后不满意哪一段，就「砍掉这一段」并让它从该段续跑重做

## 📐 成片规格

| 档位 | 尺寸 | 比例 |
|---|---|---|
| portrait | 480×864 | 竖屏 9:16 |
| landscape | 864×480 | 横屏 16:9 |
| portraitLarge | 992×1792 | 竖屏 9:16 大尺寸（约 12GB 显存，7 分钟/段） |
| landscapeLarge | 1792×992 | 横屏 16:9 大尺寸 |

创建项目时选定规格，之后固定不变。四视图角色表固定 1024×1536 不随项目变化。

## 🧩 素材要求

| 素材 | 要求 | 来源 |
|---|---|---|
| 脸部参考 | 清晰正面/三分之二脸部或半身照，**唯一必须上传** | 用户上传 |
| 四视图角色表 | 1024×1536 的 2×2 拼版（front / three-quarter / side / back） | 上传或 AI 生成 |
| 首图 | 按项目规格（如 480×864） | 上传或 AI 生成 |

所有素材仅作身份与服装参考，不会作为分屏画面。凭据字段不写入 URL、localStorage 或 project JSON。

## ⚙️ 环境变量

| 变量 | 默认 | 说明 |
|---|---|---|
| `DIRECTOR_PROJECTS_DIR` | `projects/` | 项目保存目录 |
| `DIRECTOR_COMFY_URL` | `http://127.0.0.1:8000` | ComfyUI 地址 |
| `DIRECTOR_COMFY_AUTO_FREE` | `1` | 生成前自动释放显存，低显存机器设 `0` 关闭 |
| `DIRECTOR_FFMPEG` / `DIRECTOR_FFPROBE` | PATH | FFmpeg 可执行文件路径 |
| `DIRECTOR_PLANNER_MODE` | `deterministic` | 规划器模式：`deterministic` / `openai` |
| `DIRECTOR_PLANNER_URL` / `_MODEL` / `_API_KEY` | — | 本地 OpenAI-compatible 规划器配置（key 仅存于服务端环境变量） |
| `H3_ATTENTION_PROFILE` | `sage` | H3 注意力实现：`sage`（默认，快 27%）或 `baseline` |
| `DIRECTOR_COSYVOICE_DIR` | `D:\experiment\copow_workspace\default\CosyVoice` | CosyVoice3 仓库目录（配音功能） |
| `DIRECTOR_COSYVOICE_PY` | 自动探测 `videolingo` conda 环境 Python | 执行 TTS 的 Python 解释器 |
| `DIRECTOR_COSYVOICE_MODEL_DIR` | 仓库下 `pretrained_models/Fun-CosyVoice3-0.5B` | CosyVoice3 模型目录 |
| `DIRECTOR_TTS_TIMEOUT_MS` | `180000` | 单次配音生成超时（毫秒） |

完整示例见 [`.env.example`](.env.example)。项目不会自动加载 `.env` 文件，变量需在服务进程环境中设置。

## 🗂 目录结构

```
templates/     # 首段/续段 ComfyUI 工作流模板（独立副本，Sage/Baseline 两套）
src/           # 服务端：存储、剧本规划、素材生成、视频工作流、人脸修复、成片拼接
public/        # 浏览器端：导演台 UI
scripts/       # 工具脚本（模板校验、分辨率探测等）
projects/      # 项目数据（已 gitignore）
test/          # 状态机、存储、工作流解析、FFmpeg 参数、HTTP 流程测试
docs/          # 决策记录（Sage 默认、分辨率上限探测等）
```

## 🧪 测试与证据边界

`npm test`（58 项）只证明状态机、文件存储、ComfyUI 响应解析、FFmpeg 参数与 HTTP 流程；`npm run validate:workflows` 做模板结构校验。除非主动连接本机 ComfyUI 并成功产出媒体，否则这些检查不代表真实 GPU 生成已通过。

## 🛠 技术栈

Node.js（ESM）· ComfyUI API · MiniMax H3（图生视频）· Krea2（角色素材）· FFmpeg · CodeFormer（人脸修复）· RTXVideoSuperResolution（2× 超分）· 原生 HTML/CSS/JS 前端
