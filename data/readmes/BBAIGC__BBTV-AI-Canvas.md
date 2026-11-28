<div align="center">

# BBTV 无限画布

### 图片、视频与声音，在一张画布中创作

[![版本 v0.1.561](https://img.shields.io/badge/版本-v0.1.561-2563eb)](https://github.com/BBAIGC/BBTV-AI-Canvas/releases/latest)
[![Windows 10 / 11](https://img.shields.io/badge/Windows-10%20%2F%2011-0078d4)](https://bbtv.ainivox.cn)
[![本地永久免费](https://img.shields.io/badge/本地功能-永久免费-16a34a)](#开始使用下载与安装)
[![无需购买 API](https://img.shields.io/badge/API-无需购买-0891b2)](#开始使用下载与安装)
[![MCP Agent 控制](https://img.shields.io/badge/MCP-Agent%E6%8E%A7%E5%88%B6-3b82f6)](#agent-control)

**支持的本地模型**

[![Qwen Image](https://img.shields.io/badge/Qwen-Image-615ced)](https://huggingface.co/Qwen/Qwen-Image)
[![MOSS Image](https://img.shields.io/badge/MOSS-Image-18877d)](https://huggingface.co/Comfy-Org/MOSS-Image)
[![FLUX Krea](https://img.shields.io/badge/FLUX-Krea-444444)](https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev)
[![Z Image](https://img.shields.io/badge/Z-Image-e27132)](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)
<br>
[![MiniMax H3](https://img.shields.io/badge/MiniMax-H3-3959c8)](https://huggingface.co/Comfy-Org/MiniMax-H3)
[![MiniMax H3 Image](https://img.shields.io/badge/MiniMax-H3_Image-7754be)](https://huggingface.co/Comfy-Org/MiniMax-H3-Image)
[![SeedVR2](https://img.shields.io/badge/SeedVR2-放大-278a6a)](https://huggingface.co/numz/SeedVR2_comfyUI)
[![Qwen 视觉](https://img.shields.io/badge/Qwen-视觉反推-615ced)](https://huggingface.co/Qwen)

[使用说明](#从参考素材到完整创作) · [下载安装](#开始使用下载与安装) · [模型下载](MODELS.md) · [智能体部署](#让智能体协助部署) · [版本清单](release-notes/0.1.561.md) · [Agent 控制](#agent-control)

</div>

<!-- BBTV_MCP_ANNOUNCEMENT_START -->
**v0.1.561 · 2026年11月27日发布**，已接入 MCP，可让智能体直接操作画布。[查看 Agent 控制与接入方式](#agent-control)。
<!-- BBTV_MCP_ANNOUNCEMENT_END -->

<!-- BBTV_BRAND_START -->
**BBTV AI Canvas（BBTV 无限画布）** 是 Windows 本地 AI 无限画布创作软件，支持 ComfyUI 图片与视频生成、智能分镜、高清放大及 MCP 智能体控制。本地功能永久免费，使用本地模型无需购买 API；可选云端服务按服务商规则计费。

BBTV AI Canvas is a free Windows local AI infinite canvas for ComfyUI image and video creation, storyboarding, upscaling and MCP agent control.

[官网](https://bbtv.ainivox.cn/) · [功能介绍](https://bbtv.ainivox.cn/features/) · [下载中心](https://bbtv.ainivox.cn/download/) · [模型教程](https://bbtv.ainivox.cn/models/) · [使用指南](https://bbtv.ainivox.cn/guides/) · [English](https://bbtv.ainivox.cn/en/)
<!-- BBTV_BRAND_END -->

<!-- BBTV_KREA2_FEATURE_START -->
## Krea2 风格与连续双采

Krea2 的影视柔光、风格滤镜可逐项调节；支持连续双采、MOSS → Krea2 和成图二采，原图保留。缺少配套时按文件下载并校验。

| 银发云宫 · 柔光与滤镜双采 | 紫藤金饰 · 柔光双采 |
|---|---|
| ![银发云宫](docs/images/krea2/silver-selected-dual.jpg) | ![紫藤金饰](docs/images/krea2/wisteria-selected-dual-soft.jpg) |

[查看采样参数、真实4K验证与来源说明](docs/Krea2采样与风格对照.md)。双采可能改变细节，不承诺逐像素保内容；三款固定 LoRA 通过独立资源库下载，安装包不捆绑权重。
<!-- BBTV_KREA2_FEATURE_END -->

## 开始使用：下载与安装

### [官网下载 Windows 安装包](https://bbtv.ainivox.cn) · [GitHub 直接下载](https://github.com/BBAIGC/BBTV-AI-Canvas/releases/latest)

1. **安装 BBTV。** 下载 Windows 安装包并完成安装，已有版本可在“关于 BBTV”检查更新。
2. **准备引擎与模型。** 打开[统一资源库](https://pan.baidu.com/s/1DNzXSlrRB0bNPPT78RdrRQ?pwd=rpmx)，提取码 **rpmx**；已有 ComfyUI 和匹配模型可直接复用。
3. **连接本地引擎。** 在设置中选择引擎目录，并参考 [MODELS.md](MODELS.md) 核对所选模型的编码器、VAE 和其他依赖。
4. **开始第一次创作。** 新建项目，导入参考图片，选择模型，输入要求并生成。

[v0.1.561 更新内容](release-notes/0.1.561.md)



**把想法、参考图、分镜和生成结果放进一张无限画布，接着创作。** BBTV 将常用的本地图片、视频与放大流程做成可以直接使用的操作：选择模型、提供参考、写下要求，无需手动搭建 ComfyUI 节点工作流。

**无需购买 API。本地功能永久免费，也没有按次生成费用。** 本地模型在自己的电脑运行，需要适合的硬件、推理引擎和相应模型。

![MiniMax H3 视频生成：画布中的生成耗时与实际画面](docs/assets/video-generation-speed.png)

从参考图、剧本到多镜头视频，生成耗时和结果直接显示在画布上。图中两条 15 秒、384 × 672 视频的本机生成记录约为 **6 分 38 秒**和 **7 分 16 秒**；速度会随模型、参数、缓存和硬件变化。

MiniMax H3 在远景、小脸画面中可能出现面部细节失真。可在视频节点的更多菜单中使用**修复人脸**；模型细节恢复和严格身份一致性需按实际结果核对。

### MiniMax H3 Image 细节增强

从低清原图继续恢复毛发、牙齿、布料和食品细节。MiniMax H3 Image 使用原生图生图，既能围绕参考图编辑，也能生成更清晰的画面。下面是作者提供的完整实机截图。

![MiniMax H3 Image 原生图生图与狗狗细节增强的完整实机截图](docs/assets/prd4/h3-image-detail.png)

在 BBTV 导入 628 × 628 原图，选择 **MiniMax H3 Image · 图生图**，输入「高清放大图像，增加画面细节，消除噪点」，生成 2048 × 2048 结果，再用对比节点检查。该次真实记录为 **6 步、CFG 1、denoise 1、seed 859403524、euler_ancestral / sgm_uniform，259.933 秒**；完整模型输入见[提示词与参数](docs/assets/prd4/parameters.json)。

<table align="center">
<tr><th align="center">原始低清图片</th><th align="center">H3 Image 细节增强</th></tr>
<tr><td><a href="https://bbtv.ainivox.cn/review/prd4/#image"><img src="docs/assets/prd4/photo-original.png" width="420" alt="628×628 原始低清图片" /></a></td><td><a href="https://bbtv.ainivox.cn/review/prd4/#image"><img src="docs/assets/prd4/photo-detail.png" width="420" alt="2048×2048 H3 Image 细节增强结果" /></a></td></tr>
</table>

<p align="center"><a href="https://bbtv.ainivox.cn/review/prd4/#image"><strong>打开滑动对比 · 拖动查看原图与增强结果</strong></a> · <a href="https://bbtv.ainivox.cn/review/prd4/parameters.json">完整提示词与参数</a></p>

生成式细节增强可能局部重绘手机、手部或食品；需要逐像素保留原图时，可选择专用高清放大模型。

![从剧本、镜头提示词到 MiniMax H3 视频的画布创作](docs/assets/story-to-video.png)

从故事构思出发，把剧本、角色、场景、图片提示词和视频结果放在同一张画布上。右侧助手整理创作内容，左侧节点承接素材与结果，创作脉络始终可见。

### MiniMax H3 视频人物替换

让参考照中的人物跟随原片动作。下面的真实样本截取公开舞蹈视频的 3 秒片段，保留紫色光线、镜头以及手、肩和头部动作，换成参考人物的面容、卷发和菱形衬衫。点击原片或结果画面即可播放。

<table align="center">
<tr><th align="center">舞蹈原片</th><th align="center">人物参考照</th><th align="center">替换结果</th></tr>
<tr><td><a href="https://bbtv.ainivox.cn/review/prd4/dance-source.mp4"><img src="docs/assets/prd4/dance-source.jpg" width="260" alt="3秒舞蹈原片" /></a></td><td><a href="docs/assets/prd4/reference-woman.jpg"><img src="docs/assets/prd4/reference-woman.jpg" width="260" alt="成年女性参考照" /></a></td><td><a href="https://bbtv.ainivox.cn/review/prd4/dance-result.mp4"><img src="docs/assets/prd4/dance-result.jpg" width="260" alt="H3 人物替换视频结果" /></a></td></tr>
<tr><td align="center"><a href="docs/assets/prd4/dance-source.mp4">下载原片</a></td><td align="center"><a href="docs/assets/prd4/reference-woman.jpg">下载参考照</a></td><td align="center"><a href="docs/assets/prd4/dance-result.mp4">下载结果</a></td></tr>
</table>

**384 × 672 · 3 秒 · 24 FPS · 原生 20 步 · CFG 1 · seed 912611 · 生成 369.003 秒。** 局部五官仍有变化；这次单人短片未覆盖全身快动作或多人遮挡。[同步播放与完整参数](https://bbtv.ainivox.cn/review/prd4/#dance) · [素材来源与说明](docs/H3图片与视频示例.md)

狗对白的[原 15 秒完整六段稿实测](https://bbtv.ainivox.cn/review/prd4/#dialogue)保留用户原稿、实际原图与原参数，仅固定测试种子。两句台词均完整识别，但「黄果」被识别为同音的「黄国」，部分笑的画面两狗同时张嘴，严格逐字与口型验收仍有限制。[完整提示词与参数](docs/assets/prd4/dialogue-original15.json) · [可复现工作流](docs/assets/prd4/dialogue-original15-graph.json)。此前 6 秒和本轮 8 秒短句样本分别保留，参考图、时长及稿件不同，不作为单变量对照。

以下展示均为作者提供的软件实机截图。

## 从参考素材到完整创作

| 想做什么 | 在 BBTV 中怎么做 |
|---|---|
| 图片生成与编辑 | 使用 Qwen Image、MOSS、Krea、Z-Image 等本地路线，围绕参考图继续创作 |
| 反推与提示词 | 手动开始反推，选择目标模型风格、语言、详细程度与长度；前置提示词可调整和重置 |
| 多图创作 | 多选图片，直接输入共同创作要求，保留素材之间的联系 |
| 视频与分镜 | 整理剧本、角色、场景与镜头，再使用本地 MiniMax H3 生成视频 |
| 图片放大 | 选择 VOSR2、SeedVR2 等路线，逐张或整组处理 |
| 宫格与批量处理 | 切分宫格、选择倍率、排队生成，让结果按组整齐排列 |
| 整理与交付 | 节点分组、复制到其他画布、保存项目、批量导出图片或 ZIP |

支持的具体能力取决于已安装的模型和依赖。各条路线按需配置，可先完成一个功能，再逐步扩展。

### 多角度参考，接着生成视频

围绕同一张人物或产品参考图继续创作，生成多角度视图、切分九宫格，再把选定图片作为视频参考。MiniMax H3 的视频节点可直接播放和逐帧查看，首帧、提示词与生成参数集中在当前节点下方。

![多角度视图、九宫格拆分与 MiniMax H3 视频节点](docs/assets/multi-angle-video.png)

### 从反推提示词到放大与对比

参考图可以连出文本节点，保留反推内容后继续调整、复用。图片生成、高清放大和 A/B 对比沿连线展开，方便把同一思路的不同结果并排检查。

![提示词反推、图片生成、高清放大与对比节点](docs/assets/prompt-upscale-compare.png)

### 图片工具，就在选中素材旁

图片节点提供编辑、反推提示词、高清放大、多角度、角度分离、宫格切分与图层分离入口；更多菜单集中收纳去除背景、灯光、裁剪和对比等工具。具体处理需要相应模型与依赖，可按自己的创作需求安装。

![图片节点工具栏与更多菜单](docs/assets/image-tools.png)

### 画布按自己的习惯整理

批量生成与多图导入可分别选择堆叠、多变体或铺开，也可把结果自动打组。导出水印支持位置与大小设置，水印作用于下载和复制，画布中的原图继续保留。

![画布的图片排列与导出水印设置](docs/assets/canvas-preferences.png)

### 引擎与模型，统一准备

环境页集中显示当前硬件、引擎连接和本地模型资源，支持导入引擎、导入模型、在线下载与刷新检测。已经存在的 ComfyUI 与模型可以复用；下载前先选需要的功能，再按公开清单检查配套依赖。

![本地创作环境、模型列表与资源准备](docs/assets/engine-models.png)

<!-- BBTV_MCP_README_START -->
<a id="agent-control"></a>

## 让 AI 通过 MCP 操作画布

BBTV 提供标准 MCP，让智能体直接操作**正在打开的真实画布**。创建节点、填写提示词、连接素材、选择模型、加入生成队列，都会即时显示在软件里；生成结果也保存在同一画布中。

顶部蓝色控制条显示正在操作的智能体名称，发光光标跟随操作。九档速度从极速到逐步演示，可随时调整或停止后续操作。模型任务是否完成，以节点和队列的实际状态为准。

智能体可先用 `bbtv_live_actions` 发现图片/视频工具栏、画布与节点右键、设置和生成历史，再用 `bbtv_live_invoke` 调用原功能，或在原面板中操作真实控件。高清使用用户选择的实际放大模型和参数，保留原图；不会用普通图片生成代替放大。视频复刻、重拍、图层分离、裁剪、字幕等功能也通过各自原入口执行。

**[下载通用 BBTV MCP Skill](https://bbtv.ainivox.cn/download/bbtv-canvas-mcp-skill.zip)** · [GitHub 备用下载](https://github.com/BBAIGC/BBTV-AI-Canvas/releases/download/v0.1.561/bbtv-canvas-mcp-skill.zip)，交给支持 Skill 的智能体安装。它包含真实画布操作、素材保护、模型选择与任务恢复规则，不含密钥或模型权重；不支持持久 Skill 的产品可在当前对话读取使用。

### 连接 Codex、Claude Code 或其他智能体

1. 启动 BBTV，进入**设置 → MCP**，开启连接。
2. 复制软件提供的 HTTP 或 stdio 配置，添加到智能体的 MCP 设置。
3. 打开目标画布，让智能体先读取状态，再执行创作任务。

Codex、Claude Code 及其他支持标准 MCP 的客户端可接入。豆包需要所用版本提供 MCP 服务连接能力；未提供 MCP 接口的版本无法直接连接。各客户端配置格式可能不同，以软件复制的服务地址、启动命令和连接令牌为准。

**HTTP：** 使用软件给出的本机 `/api/mcp` 地址和连接令牌，支持 Streamable HTTP。服务默认只在本机开放，令牌不要放进提示词、截图或公共仓库。地址示意：

```text
http://127.0.0.1:3210/api/mcp
Authorization: Bearer <软件内复制的连接令牌>
```

**stdio：** 安装包已包含轻量桥接脚本，可使用 BBTV 自带的运行时，无需另外安装 Node.js。配置结构示意如下，路径请使用软件复制的实际值：

```json
{
  "mcpServers": {
    "bbtv": {
      "command": "<BBTV安装目录>/BBTV.exe",
      "args": [
        "--max-old-space-size=128",
        "<BBTV安装目录>/resources/mcp/bbtv-canvas-mcp.cjs",
        "--base-url",
        "http://127.0.0.1:3210"
      ],
      "env": {
        "ELECTRON_RUN_AS_NODE": "1",
        "NODE_OPTIONS": "",
        "BBTV_MCP_TOKEN": "<软件内复制的连接令牌>"
      }
    }
  }
}
```

### 从读取到生成

| 步骤 | MCP 操作 |
|---|---|
| 查看真实窗口与画布 | `bbtv_live_status`、`bbtv_live_read` |
| 查看已配置模型 | `bbtv_live_batch` 中的 `models` 动作 |
| 准备节点与连线 | `bbtv_live_batch`，支持节点别名、编辑、连接、选择和保存 |
| 导入本机素材 | `bbtv_live_import`；指定真实文件，可按目录筛选后逐项导入 |
| 配置云端 API | `bbtv_configure_api`；保存用户提供的连接并读取实际模型目录 |
| 开始生成 | `generate` 先加入可见队列，再用 `queue/start` 开始 |
| 查看图片与其他功能 | `bbtv_live_image` 返回当前节点图片；`bbtv_live_ui` 操作可见控件 |

可以这样交代任务：

> 先读取当前画布和可用模型，把我指定目录中的参考图片导入画布。保留原图，整理角色、场景和分镜，连接好参考后加入生成队列；先让我在画布里查看准备结果。

模型与接口沿用这台电脑的软件配置。需要设置云端 API 时，使用软件提供的专用配置工具输入密钥；工具只返回连接状态与模型信息，不回显已有密钥。不要把密钥写进节点提示词、普通文本动作或公开文档。

`bbtv_configure_api` 的参数包括唯一 `requestId`、连接名称 `name`、接口地址 `baseUrl` 和用户明确提供的 `apiKey`；`purpose` 可选图片、文字、音频或全部，`discover` 控制是否读取接口模型目录。需要更新现有连接时，先确认其 `connectionId` 再指定；手动模型可通过 `models` 保留准确名称与类型。保存由可见软件窗口确认，回执不包含密钥，也不会启动生成。

目录导入由智能体先筛选目录中的真实媒体文件，再逐文件调用 `bbtv_live_import`，为每个文件使用独立 `requestId`。该工具接收普通媒体文件，不把目录路径当成图片，不执行文件，也不会偷偷替换成示例素材。

批量调用可用 `requestId` 防止同一操作重复提交。页面断线或超时后，先检查实际画布，避免重复生成。停止 MCP 会中止后续画布操作；已经提交的模型任务仍应在生成队列中检查或取消。
<!-- BBTV_MCP_README_END -->

## 让智能体协助部署

选择适合自己的方案，复制完整提示词，发给 [Codex](https://chatgpt.com/codex)、[Claude Code](https://claude.com/product/claude-code)、[豆包工作](https://www.doubao.com/work)、[WorkBuddy](https://www.workbuddy.cn/)、[字节 TRAE](https://www.trae.cn/download)、[MiniMax Code](https://code.minimax.cn/about) 等智能体。三套提示词与软件、官网使用同一份内容，都会先核对本机配置并复用已有模型。下方提示词默认展开，也可收起后快速浏览其他内容。

### 1. 按电脑配置推荐

先检测硬件与已有资源，再选择适合本机的图片、视频或放大能力。

<details open>
<summary>完整部署提示词</summary>

```text
请协助我在这台 Windows 电脑上配置 BBTV 本地推理引擎与模型。按下列目标执行实际检查和部署，保留现有 ComfyUI、模型、画布与用户设置。
方案：按电脑配置推荐
1. 优先根据这台电脑的实际显存、内存和磁盘空间推荐组合；先完成可运行的最小闭环，再按我的用途逐项增加功能。
2. 如果显存或存储不足，说明具体不满足的模型与替代方案，不因为作者电脑能运行就承诺本机也能运行。

共同执行要求：
1. 先按“01-软件包 → 02-推理引擎 → 03-基础模型”准备常用本地能力；其他模型按软件提示下载“04-可选扩展”内对应真实权重文件夹并直接拖入 BBTV。共享组件位于各功能的“00-共享配套”，已匹配文件只需一份，不重复下载。再检测本机 Windows、CPU、内存、GPU、可用显存、驱动和目标磁盘空间，不用作者配置代替实际硬件。
2. 如果尚未安装 BBTV，只从官网或官方 GitHub Releases 获取 Windows 二进制安装器，核对版本和校验值后安装；GitHub 是安装包与使用文档入口，不要求克隆源码或在本机编译。
3. 定位已有 ComfyUI（包括便携版、整合包和独立 Python 环境）、extra_model_paths.yaml、BBTV 引擎与模型目录。先检查常见安装位置和用户指定目录，再按实际证据扩大查找；不要全盘读取无关文件。
4. “01-软件包”“02-推理引擎”分别提供程序与引擎；“03-基础模型”包含 Krea 2、H3 视频、VOSR2 等常用配套，需满足实际硬件条件。“04-可选扩展”按功能和模型存放权重，所选模型还可能依赖基础包或其他功能的共享组件。根据软件缺项提示与对应文件夹配套清单补齐，仅下载缺失文件；基础资源不等于所有扩展模型配套已完整。
5. 复用已存在且匹配的模型文件，按公开清单核对大小与 SHA256，不能只凭名称判断；名称不同但哈希一致的文件也是可复用资源。检查并使用 extra_model_paths.yaml；如果 BBTV 需要清单指定的模型名称，可采用文件联接或额外路径配置满足别名，保留原权重原位，不搬移、不重复下载。仅下载缺失且适合本机的资源，图片、视频、文本编码器、VAE、LoRA 和放大模型必须按依赖配套，不把包名当作已完整可用的证据。 用户主动拖入下载的模型包时，按清单校验后归位：同盘移动，跨盘校验复制成功再移除该下载源；已有 ComfyUI 或 Ollama 模型仍可原位复用，不搬移既有环境。
6. 按资源清单的 installRoot 和 installRelativePath 分流安装，不将基础/可选、功能分类或旧“模型库”目录整层嵌入 models。新旧包目录都支持识别；Ollama 必须保留 manifest、所有 blob 与图像投影器完整引用。导入模型后刷新检测，无需重启应用；导入引擎时依界面提示重启。遵守每个模型各自许可。
7. 先给出本机适合的功能组合、所需磁盘空间与缺失资源，再部署已选择的组合。不要覆盖同名模型或删除现有环境；修改配置前保留可恢复备份，不强制迁移已有模型。
8. 网盘分享页不是文件直链。使用已公开的真实下载链接；若资源链接尚未开放，或百度网盘需要我完成登录、转存或下载，请明确说明并使用我提供的本地压缩包，不编造链接或校验值。
9. 部署后检查核心依赖、模型文件与本地推理服务。启动 BBTV，在设置的本地引擎中选择正确目录，保存配置并按需重启；分别验证引擎连通、模型列表和对应功能是否可用。未经我选择，不调用收费云端接口。
10. 最后列出实际使用的路径、复用与新增文件、验证结果和仍缺少的资源；失败时保留成功部分，说明下一步，不把未验证的功能标为成功。

官方网站：https://bbtv.ainivox.cn
安装包与使用文档：https://github.com/BBAIGC/BBTV-AI-Canvas
模型清单：https://github.com/BBAIGC/BBTV-AI-Canvas/blob/main/docs/model-distribution-inventory.json
推理引擎：https://pan.baidu.com/s/1DNzXSlrRB0bNPPT78RdrRQ?pwd=rpmx（提取码：rpmx）
模型资源：https://pan.baidu.com/s/1DNzXSlrRB0bNPPT78RdrRQ?pwd=rpmx（提取码：rpmx）
作者电脑：i7-12700KF · 64 GB 内存 · RTX 5060 Ti 16 GB
```

</details>

### 2. 轻量部署

按常用功能减少下载；轻量指资源组合更少，不代表适合低显存。

<details open>
<summary>完整部署提示词</summary>

```text
请协助我在这台 Windows 电脑上配置 BBTV 本地推理引擎与模型。按下列目标执行实际检查和部署，保留现有 ComfyUI、模型、画布与用户设置。
方案：轻量部署
1. 先询问我主要需要图片生成、视频生成还是图片放大，只部署选定功能和必须的配套依赖，不把作者完整模型库全部下载。
2. 轻量是相对作者全套减少资源，并不是低显存保证。特别核对视频模型、编码器、VAE 和默认加速 LoRA 的总大小，以及本机可用显存与内存。

共同执行要求：
1. 先按“01-软件包 → 02-推理引擎 → 03-基础模型”准备常用本地能力；其他模型按软件提示下载“04-可选扩展”内对应真实权重文件夹并直接拖入 BBTV。共享组件位于各功能的“00-共享配套”，已匹配文件只需一份，不重复下载。再检测本机 Windows、CPU、内存、GPU、可用显存、驱动和目标磁盘空间，不用作者配置代替实际硬件。
2. 如果尚未安装 BBTV，只从官网或官方 GitHub Releases 获取 Windows 二进制安装器，核对版本和校验值后安装；GitHub 是安装包与使用文档入口，不要求克隆源码或在本机编译。
3. 定位已有 ComfyUI（包括便携版、整合包和独立 Python 环境）、extra_model_paths.yaml、BBTV 引擎与模型目录。先检查常见安装位置和用户指定目录，再按实际证据扩大查找；不要全盘读取无关文件。
4. “01-软件包”“02-推理引擎”分别提供程序与引擎；“03-基础模型”包含 Krea 2、H3 视频、VOSR2 等常用配套，需满足实际硬件条件。“04-可选扩展”按功能和模型存放权重，所选模型还可能依赖基础包或其他功能的共享组件。根据软件缺项提示与对应文件夹配套清单补齐，仅下载缺失文件；基础资源不等于所有扩展模型配套已完整。
5. 复用已存在且匹配的模型文件，按公开清单核对大小与 SHA256，不能只凭名称判断；名称不同但哈希一致的文件也是可复用资源。检查并使用 extra_model_paths.yaml；如果 BBTV 需要清单指定的模型名称，可采用文件联接或额外路径配置满足别名，保留原权重原位，不搬移、不重复下载。仅下载缺失且适合本机的资源，图片、视频、文本编码器、VAE、LoRA 和放大模型必须按依赖配套，不把包名当作已完整可用的证据。 用户主动拖入下载的模型包时，按清单校验后归位：同盘移动，跨盘校验复制成功再移除该下载源；已有 ComfyUI 或 Ollama 模型仍可原位复用，不搬移既有环境。
6. 按资源清单的 installRoot 和 installRelativePath 分流安装，不将基础/可选、功能分类或旧“模型库”目录整层嵌入 models。新旧包目录都支持识别；Ollama 必须保留 manifest、所有 blob 与图像投影器完整引用。导入模型后刷新检测，无需重启应用；导入引擎时依界面提示重启。遵守每个模型各自许可。
7. 先给出本机适合的功能组合、所需磁盘空间与缺失资源，再部署已选择的组合。不要覆盖同名模型或删除现有环境；修改配置前保留可恢复备份，不强制迁移已有模型。
8. 网盘分享页不是文件直链。使用已公开的真实下载链接；若资源链接尚未开放，或百度网盘需要我完成登录、转存或下载，请明确说明并使用我提供的本地压缩包，不编造链接或校验值。
9. 部署后检查核心依赖、模型文件与本地推理服务。启动 BBTV，在设置的本地引擎中选择正确目录，保存配置并按需重启；分别验证引擎连通、模型列表和对应功能是否可用。未经我选择，不调用收费云端接口。
10. 最后列出实际使用的路径、复用与新增文件、验证结果和仍缺少的资源；失败时保留成功部分，说明下一步，不把未验证的功能标为成功。

官方网站：https://bbtv.ainivox.cn
安装包与使用文档：https://github.com/BBAIGC/BBTV-AI-Canvas
模型清单：https://github.com/BBAIGC/BBTV-AI-Canvas/blob/main/docs/model-distribution-inventory.json
推理引擎：https://pan.baidu.com/s/1DNzXSlrRB0bNPPT78RdrRQ?pwd=rpmx（提取码：rpmx）
模型资源：https://pan.baidu.com/s/1DNzXSlrRB0bNPPT78RdrRQ?pwd=rpmx（提取码：rpmx）
作者电脑：i7-12700KF · 64 GB 内存 · RTX 5060 Ti 16 GB
```

</details>

### 3. 作者全量配置

按作者资源清单准备完整功能，先核对本机空间与硬件差异。

<details open>
<summary>完整部署提示词</summary>

```text
请协助我在这台 Windows 电脑上配置 BBTV 本地推理引擎与模型。按下列目标执行实际检查和部署，保留现有 ComfyUI、模型、画布与用户设置。
方案：作者全量配置
1. 以作者公开清单为目标逐项核对图片、视频、编辑、放大与配套资源；先统计整套下载和解压空间，列明现有文件可复用的部分。
2. 完整资源数量不等于本机能同时加载。按我的硬件选择精度、分辨率和资源释放策略；作者硬件仅作参考，不把所有模型强行常驻显存。

共同执行要求：
1. 先按“01-软件包 → 02-推理引擎 → 03-基础模型”准备常用本地能力；其他模型按软件提示下载“04-可选扩展”内对应真实权重文件夹并直接拖入 BBTV。共享组件位于各功能的“00-共享配套”，已匹配文件只需一份，不重复下载。再检测本机 Windows、CPU、内存、GPU、可用显存、驱动和目标磁盘空间，不用作者配置代替实际硬件。
2. 如果尚未安装 BBTV，只从官网或官方 GitHub Releases 获取 Windows 二进制安装器，核对版本和校验值后安装；GitHub 是安装包与使用文档入口，不要求克隆源码或在本机编译。
3. 定位已有 ComfyUI（包括便携版、整合包和独立 Python 环境）、extra_model_paths.yaml、BBTV 引擎与模型目录。先检查常见安装位置和用户指定目录，再按实际证据扩大查找；不要全盘读取无关文件。
4. “01-软件包”“02-推理引擎”分别提供程序与引擎；“03-基础模型”包含 Krea 2、H3 视频、VOSR2 等常用配套，需满足实际硬件条件。“04-可选扩展”按功能和模型存放权重，所选模型还可能依赖基础包或其他功能的共享组件。根据软件缺项提示与对应文件夹配套清单补齐，仅下载缺失文件；基础资源不等于所有扩展模型配套已完整。
5. 复用已存在且匹配的模型文件，按公开清单核对大小与 SHA256，不能只凭名称判断；名称不同但哈希一致的文件也是可复用资源。检查并使用 extra_model_paths.yaml；如果 BBTV 需要清单指定的模型名称，可采用文件联接或额外路径配置满足别名，保留原权重原位，不搬移、不重复下载。仅下载缺失且适合本机的资源，图片、视频、文本编码器、VAE、LoRA 和放大模型必须按依赖配套，不把包名当作已完整可用的证据。 用户主动拖入下载的模型包时，按清单校验后归位：同盘移动，跨盘校验复制成功再移除该下载源；已有 ComfyUI 或 Ollama 模型仍可原位复用，不搬移既有环境。
6. 按资源清单的 installRoot 和 installRelativePath 分流安装，不将基础/可选、功能分类或旧“模型库”目录整层嵌入 models。新旧包目录都支持识别；Ollama 必须保留 manifest、所有 blob 与图像投影器完整引用。导入模型后刷新检测，无需重启应用；导入引擎时依界面提示重启。遵守每个模型各自许可。
7. 先给出本机适合的功能组合、所需磁盘空间与缺失资源，再部署已选择的组合。不要覆盖同名模型或删除现有环境；修改配置前保留可恢复备份，不强制迁移已有模型。
8. 网盘分享页不是文件直链。使用已公开的真实下载链接；若资源链接尚未开放，或百度网盘需要我完成登录、转存或下载，请明确说明并使用我提供的本地压缩包，不编造链接或校验值。
9. 部署后检查核心依赖、模型文件与本地推理服务。启动 BBTV，在设置的本地引擎中选择正确目录，保存配置并按需重启；分别验证引擎连通、模型列表和对应功能是否可用。未经我选择，不调用收费云端接口。
10. 最后列出实际使用的路径、复用与新增文件、验证结果和仍缺少的资源；失败时保留成功部分，说明下一步，不把未验证的功能标为成功。

官方网站：https://bbtv.ainivox.cn
安装包与使用文档：https://github.com/BBAIGC/BBTV-AI-Canvas
模型清单：https://github.com/BBAIGC/BBTV-AI-Canvas/blob/main/docs/model-distribution-inventory.json
推理引擎：https://pan.baidu.com/s/1DNzXSlrRB0bNPPT78RdrRQ?pwd=rpmx（提取码：rpmx）
模型资源：https://pan.baidu.com/s/1DNzXSlrRB0bNPPT78RdrRQ?pwd=rpmx（提取码：rpmx）
作者电脑：i7-12700KF · 64 GB 内存 · RTX 5060 Ti 16 GB
```

</details>

“轻量”指只下载需要的功能和依赖，并不意味着所有低显存电脑都能运行。


## 作者设备与速度参考

作者电脑：i7-12700KF · 64 GB 内存 · RTX 5060 Ti 16 GB。以下是这台设备已有成功任务的记录，模型加载、步数与缓存状态没有统一，不能作为同条件性能比较。

| 功能与模型 | 输出与条件 | 历史记录耗时 |
|---|---|---|
| 图片 · Qwen Image 2.1 Turbo | 1024 × 1824，8 步；20 次记录 | 约 10.5～19.4 秒 |
| 视频 · MiniMax H3 | 15 秒视频，480 × 640 或 480 × 864；7 次记录 | 约 7.9～18.4 分钟 |
| 放大 · VOSR2 | 约 683 方图放大 4 倍，输出约 2732 × 2732；9 次记录 | 约 20.0～49.3 秒 |
| 放大 · VOSR2 | 最长边 4048，输出 4048 × 2699；1 次记录 | 约 32.5 秒 |

作者日常口述参考为 H3 的 15 秒视频约 10 分钟、VOSR2 到 4K 约 20～30 秒、近 1K 图片十多秒；这些口述没有固定全部参数，实际运行可能更慢。普通 Qwen Image 2.1 与 Turbo 的耗时不能混用。公开的精选记录见 [性能记录](docs/performance-reference.json)。

## 模型下载与空间

[统一资源库](https://pan.baidu.com/s/1DNzXSlrRB0bNPPT78RdrRQ?pwd=rpmx) · 提取码 **rpmx**

| 资源层 | 文件数 | 文件合计 |
|---|---:|---:|
| 基础必需组合 | 20 | 76.30 GB |
| 可选扩展 | 120 | 275.09 GB |
| 当前资源清单合计 | 144 | 356.26 GB |

这是作者资源库的分层，并非安装 BBTV 必须一次下载全部文件。按功能计算所需资源，预留下载、解压和运行缓存空间；共用权重只保存一份。

## 自己选择云端服务

需要云端模型时，可以在接口设置里填写自己的服务地址、API Key 和模型，按服务支持的兼容协议自行接入。图片与文字模型可分别配置，服务由自己选择，没有平台绑定。本地路线继续独立使用；云端费用与可用能力由所选服务决定。

## 更新与交流

软件启动时检查新版本，发现更新后可在“关于 BBTV”查看更新内容并下载安装；运行期间每小时继续检查。正在输入或操作弹窗时，启动更新提示会稍后显示。

“关于 BBTV”集中显示应用版本、推理环境、更新入口与最近更新记录，便于检查当前安装状态。

![关于 BBTV、推理环境与版本更新](docs/assets/about-updates.png)

GitHub 从 **0.1.53** 起保留最近 **8 个稳定版本**的安装包及其校验配套文件。发布第 9 个稳定版后才清理最旧安装包，历史 Release 页面、标签和更新说明继续保留；预发布、草稿、引擎与模型资源不在清理范围内。

内测反馈与使用交流：

<img src="docs/assets/bbtv-qq-group.jpg" width="320" alt="BBTV 内测交流群二维码" />

## 致谢与第三方声明

感谢抖音创作者 [@🌈](https://www.douyin.com/user/MS4wLjABAAAAAhuYCbGqwDkhJg0Ar_oPMn6KehdmEI6-IS_Mqq0Flpo) 分享原版室内提示词生成器，BBTV 的室内提示词功能参考了其参数设计与生成逻辑。

本地推理使用 ComfyUI 及相应模型生态，感谢相关项目与模型作者。

本仓库提供安装包索引、使用文档和版本说明，程序源码未在此仓库发布。第三方组件的许可证与声明保留在 [NOTICE.md](NOTICE.md) 及 [LICENSES](LICENSES/open-canvas-MIT.txt)。模型与第三方组件各自适用其原许可证。

BBTV剪辑向所有用户免费开放，永不收费。我们会在原作基础上持续优化、更新功能，后续版本同样免费。

BBTV剪辑 0.2.6 基于 [Concat](https://github.com/jub0t/Concat) 完整原生源码开发，原作者为 Jareer Abdullah 与 Concat 贡献者，遵循 AGPL-3.0-or-later。[下载本版完整对应源码 ZIP](https://bbtv.ainivox.cn/editor/source/BBTV-Editor-0.2.6-source.zip?build=20261121-final)，或查看[来源、许可与构建材料说明](docs/BBTV剪辑-开源来源与源码.md)。保留原版权与第三方归属，其他独立组件遵循各自许可。
