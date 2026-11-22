![镜场 Cartoon Studio · 本地短片与 AI 漫剧工作台](docs/images/cover.jpg)

<p align="center">
  <a href="https://github.com/bilzeng/cartoon-studio"><img alt="GitHub 仓库" src="https://img.shields.io/badge/GitHub-24292f?style=flat-square&amp;logo=github&amp;logoColor=white"></a>
  <a href="https://github.com/bilzeng/cartoon-studio/issues"><img alt="GitHub Issues 问题反馈" src="https://img.shields.io/badge/Issues-24292f?style=flat-square&amp;logo=github&amp;logoColor=white"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/License-Apache%202.0-315f5c?style=flat-square"></a>
  <a href="https://nodejs.org/"><img alt="Node.js 24 或更新版本" src="https://img.shields.io/badge/Node.js-24%2B-315f5c?style=flat-square"></a>
  <a href="#连接-comfyui"><img alt="接入 ComfyUI" src="https://img.shields.io/badge/Generation-ComfyUI-315f5c?style=flat-square"></a>
</p>

# 镜场 · Cartoon Studio

镜场是一款运行在本机的开源短片与 AI 漫剧工作台。你可以在节点画布上组织参考素材，按剧本拆分和编排镜头，用自己的 ComfyUI 工作流生成图像、视频与旁白，再从分镜台导出 MP4。

[快速开始](#快速开始) · [制作一集](#制作一集) · [连接 ComfyUI](#连接-comfyui) · [开源项目与致谢](#开源项目与致谢) · [开发与测试](#开发与测试)

## 功能一览

- **自由画布**　拖入图片，组织图像、视频和音频素材，拖动节点端口连线。在提示词中用 `@` 指定参考图。
- **3D 导演台**　在画布底部点「＋ → 导演台」，再点节点上的「打开导演台」。可以摆放演员、设置机位和走位关键帧，把当前取景截图或预演视频接回画布。
- **分镜与版本**　逐镜编辑运镜、对白和时长，跨集复用角色、场景和道具。每个镜头可独立返工，预览后再选用版本。
- **图像与视频**　使用自定义像素尺寸、PoseSwap 姿势换装、RelayVSR 高清修复及 H3 两段续接。
- **素材与成片**　给素材去重、打标签、收藏，从分镜台预览镜头顺序，导出带配乐的 MP4。

![镜场工作流画布，剧本节点连到《潮汐电台》的六个分镜](docs/images/canvas.jpg)

*《潮汐电台》内置示例，启动镜场即可打开。*

## 快速开始

**启动和浏览示例需要 Node.js 24 或更新版本。** MP4 导出和涉及本地音视频预处理的功能需要将 FFmpeg 加入 `PATH`。初次安装依赖需要联网。Windows、macOS 和 Linux 均提供便携启动脚本。

```sh
git clone https://github.com/bilzeng/cartoon-studio.git
cd cartoon-studio
npm ci
npm run build
npm start
```

在浏览器打开终端打印的地址，通常是 [http://127.0.0.1:4317/](http://127.0.0.1:4317/)。首次体验可直接打开「示例画布 → 潮汐电台」。浏览示例、编排项目和使用本地素材均可在 ComfyUI 离线时完成。

也可以在源码目录使用平台启动脚本。首次运行会准备对应平台的运行环境。

| 系统 | 入口 |
| --- | --- |
| Windows | 双击 `Start-Windows.cmd` |
| macOS | 双击 `Start-macOS.command` |
| Linux | 运行 `sh Start-Linux.sh` |

### 一键更新

在工作台左侧点击 **更新并重启**。Git 安装会拉取当前分支所跟踪的远端 `main`，便携包或源码压缩包跟随 GitHub 的公开 `main`，无需另外安装 Git。程序先下载代码、安装依赖并构建，等生成和导出任务完成后，在原地址重启并刷新页面。项目、素材和环境设置继续使用安装目录里的 `data/` 和 `.env`。更新需要联网，并需要安装目录有写入权限。

按钮随新版启动器提供。旧安装首次升级时，源码版在原安装目录执行 `git pull --ff-only`、`npm ci` 和 `npm run build` 后重新启动，便携版用含此按钮的新版程序并沿用原 `data/`。双击启动脚本或运行 `npm start` 时会检查安装版本并重建旧页面。如果旧进程占用原端口，启动器会打开新版地址。开发模式 `npm run dev` 使用 Vite 热更新。

## 制作一集

### 1. 从剧本拆镜

在首页选择「新建画布创作」并粘贴剧本。多段文本按行拆镜，单行中文还可按句末标点拆分。进入「分镜表」设置景别、光影、运镜、对白和时长。从「角色、场景与道具」建立设定卡，再把引用逐镜绑定。

![分镜表展示《潮汐电台》的逐镜描述、设定引用和生成入口](docs/images/shot-table.jpg)

### 2. 生成并比较版本

在分镜表对单镜提交生成，或在画布上把参考图接到图片节点。在「生成设置」中选择画幅和像素预设，也能直接填写宽高。PoseSwap 节点的人物、姿势和服装分别选择。换一张同用途的专用参考图时，画布会复用原参考节点和连线。

预览「生成记录」后选择采用的版本。修复节点里的对比滑杆可以查看该版输出对应的原始输入。

![图片节点的生成设置，提供选定画幅、像素预设和自定义宽高](docs/images/image-settings.jpg)

### 3. 编排与导出

切到「分镜台」检查镜头顺序和总时长。在导出窗口选择画幅及可选全片配乐。横屏、竖屏和方形的默认成片尺寸分别为 1280 × 720、720 × 1280 和 720 × 720，输出帧率为 24 fps。制作下一集时，可从「剧集设定」沿用本集设定卡创建独立项目。

![分镜台以缩略图和时长显示已编排的镜头](docs/images/storyboard.jpg)

## 连接 ComfyUI

从首页或画布右上角打开「ComfyUI 环境」，填写服务地址和可选的 Bearer 令牌，然后点「测试并切换」。同机服务通常使用 `http://127.0.0.1:8188`。支持保存多个环境，运行中的任务仍会从提交时选定的服务取回结果。

视频节点的「H3 · 多参考图一采预览」先生成带声音的原生预览，横版为 1344 × 768，竖版为 768 × 1344。选用满意的版本后，点「高清修复」，选择 2K 或 4K 并开始放大。

[工作流模型下载与安装清单](docs/workflow-model-install.pdf)按功能列出模型、下载地址和安装目录。[RelayVSR 单图原流程](docs/workflows/relayvsr-single-image.json)可以拖入 ComfyUI 编辑器，选一张图后运行。

在节点的「模型与工作流」查看内置预设，包括「角色卡 · 含姓名三栏 2K」。Gitee 和 GitHub 提供相同的内置工作流。模型权重、自定义节点、字体和文件映射由连接的 ComfyUI 环境管理。

| 工作流 | 所需环境 |
| --- | --- |
| 常规生图与参考图编辑 | 支持对应模型加载与采样的 ComfyUI 环境。镜场可以发现 Krea2、Qwen Image 2.1、Z-Image Turbo 和兼容的 SD checkpoint。 |
| PoseSwap 姿势与换装 | Qwen Image 2.1、配套的 Qwen3-VL 编码器和 VAE，以及 `TextEncodeQwenImage21` 等节点。环境同时提供 Qwen Image 2.1 BF16 和 PoseStudio V1.1 时，可使用姿态 LoRA。图片可上传，也可从画布选取。 |
| RelayVSR 高清修复与 2K / 4K 视频二采 | 配置 RelayVSR 相关节点、×2 模型及配套 VAE。预设使用 `relayvsr_x2_lightx2v_int8_convrot.safetensors` 和 `relayvsr_flash_vae_x2_fp32.safetensors`。 |
| MiniMax H3 与两段续接 | H3 模型、匹配的文本编码器、视频和音频 VAE。对应预设还需要 Pika Flex LoRA。两段续接使用 `AICG3D_H3*` 节点。 |

预设缺少依赖时，打开该工作流的配置，核对当前环境已安装的节点和权重，并映射兼容的文件。大尺寸生成受模型和硬件限制。若 Apple Silicon 上的 MPS 在 VAE 解码阶段报张量尺寸错误，可先用较小尺寸生成，再使用超分流程；环境和预设支持时也可使用分块解码。

### 导入自己的工作流

1. 先在 ComfyUI 中验证工作流，再导出 JSON。镜场支持导入编辑器格式和 API 格式。依赖扩展前端序列化的工作流可优先使用 API 格式。
2. 在镜场节点的「模型与工作流 → 导入工作流 JSON」中指定成品输出、参考素材输入、提示词及需要开放的参数。
3. 逐个检查模型文件映射，再从画布发起生成。准确的节点类型及默认文件名可查阅 [内置工作流定义](server/presets)。

PoseSwap 外部图库需要联网，来源和授权范围见 [第三方来源](THIRD_PARTY_NOTICES.md)。

## 开源项目与致谢

感谢以下项目。镜场通过 ComfyUI API 调用生成能力，所需插件由使用者按工作流安装。

| 项目 | 镜场中的用途 |
| --- | --- |
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 提交生成工作流、读取节点和模型列表、跟踪任务并回收成品。 |
| [AICG3D](https://github.com/JGRFW/comfyui-AICG3D) | MiniMax H3 分段续接与 Spark-TTS 旁白的节点来源。 |
| [AICG3D PoseSwap](https://github.com/JGRFW/comfyui-aicg3d-PoseSwap) | 人物、姿势和服装参考图库的来源。镜场从固定版本在线读取三套图库。 |
| [VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite) | 内置 Wan 2.1 视频工作流通过 `VHS_VideoCombine` 输出 MP4。 |
| [RelayVSR](https://github.com/kopperx/RelayVSR) · [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) | 高清修复和超分工作流对应的上游项目。 |
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | 在本机拼接镜头、处理音视频、导出成片。 |
| [React](https://github.com/facebook/react) · [React Flow](https://github.com/xyflow/xyflow) · [CodeMirror](https://codemirror.net/) · [Lucide](https://github.com/lucide-icons/lucide) | 应用界面、节点与连线、提示词编辑和图标。 |
| [Node.js](https://github.com/nodejs/node) · [Express](https://github.com/expressjs/express) · [Vite](https://github.com/vitejs/vite) · [Playwright](https://github.com/microsoft/playwright) | 本地运行时和 API、前端构建、浏览器回归测试。 |

模型、LoRA 的发布页、节点标识、完整直接依赖和图库使用条款均列在 [第三方来源与许可说明](THIRD_PARTY_NOTICES.md)。README 的封面与导航编排参考了 [Toonflow 的项目文档](https://github.com/HBAI-Ltd/Toonflow-app)。

## 项目数据

项目文件、个人素材、生成记录、环境设置和导出成片保存在本机的 `data/`。迁移时先退出镜场，再备份整个 `data/` 目录。画布 JSON 可单独导出和导入，用于迁移画布结构及素材引用。引用对应的原始媒体需随数据目录一并迁移。

`data/`、`.env`、运行时目录和发行产物由 Git 忽略。ComfyUI 服务地址及令牌在应用中配置，也可通过本地 `COMFYUI_URL` 和 `COMFYUI_TOKEN` 环境变量设置。

## 开发与测试

前端使用 React、React Flow 和 Vite。Express 负责本地项目、媒体和 ComfyUI API，FFmpeg 负责导出与必要的音视频处理。

| 目录 | 职责 |
| --- | --- |
| `src/` | 应用界面、节点画布、分镜编辑与素材选择 |
| `shared/` | 项目结构、画布连接和工作流共享逻辑 |
| `server/` | 本地存储、生成任务、预设工作流及导出 |
| `tests/` | 服务端与 Playwright 浏览器回归 |

```sh
npm ci
npm run dev

npm test
npx playwright install chromium
npm run test:canvas
npm run build
npm run test:sites
```

遇到问题可在 [GitHub Issues](https://github.com/bilzeng/cartoon-studio/issues) 提交复现步骤、系统与运行时版本、所用预设和脱敏错误信息。欢迎提交问题修复和可复用的工作流改进。

## 许可证

镜场源码采用 [Apache License 2.0](LICENSE)。第三方工具、模型、插件和外部图库适用各自条款。详见 [第三方来源与许可说明](THIRD_PARTY_NOTICES.md)。
