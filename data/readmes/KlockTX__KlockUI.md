# KlockUI

**零门槛开箱即用的 ComfyUI 本地 WebUI。**

换底模不用重学一遍参数：采样器、步数、CFG、该挂哪支 LoRA，都跟着模型走。

[![License: GPL-3.0](https://img.shields.io/badge/license-GPL--3.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()
[![No build step](https://img.shields.io/badge/build-none-brightgreen.svg)]()
[![Local first](https://img.shields.io/badge/data-stays%20local-success.svg)]()

针对低显存与低内存深度优化。多架构预设、LoRA 按架构隔离、参数配方可存可分享。

![KlockUI 主界面](docs/shot-main.jpg)

> **不含推理引擎，也不含任何模型权重。**
> 引擎（ComfyUI）与底模由 [`install.md`](install.md) 指导安装——把仓库链接交给你的 agent 即可。

---

## 目录

- [为什么需要它](#为什么需要它)
- [功能](#功能)
- [支持的架构](#支持的架构)
- [快速开始](#快速开始)
- [运行结构](#运行结构)
- [参数配方](#参数配方)
- [配置](#配置)
- [常见问题](#常见问题)
- [项目结构](#项目结构)
- [参与贡献](#参与贡献)
- [许可](#许可)

---

## 为什么需要它

ComfyUI 本身很强，但有个日常成本：**每换一个底模，就要重来一遍。**

换 Anima 要 Euler + sgm-uniform、28 步、CFG 4；
换 Krea 2 要 Euler + Simple、8 步、CFG 1，而且 shift 是烤死在模型里的；
换 Z-Image 要 Res Multistep + Simple、9 步，编码器还得换成 `lumina2` 类型。
走错一步不会报错，只会给你一张糊图——然后你要花十分钟才意识到是采样器选错了。

KlockUI 不重写引擎，只在外面包一层——把这些参数**固化成代码里的架构知识**，
换模型时自动跟着换：

```python
# comfy_bridge.py 里的一小段
zimage: {
    "sampler": "Res Multistep", "scheduler": "Simple",
    "steps": 9, "cfg": 1.0, "shift": 3,
    "clip_type": "lumina2",            # 不是 stable_diffusion
    "te": "qwen_3_4b_fp8_mixed.safetensors",
    "vae": "ae.safetensors",
}
```

换模型时它自动套用，你只关心画面。

---

## 功能

### 按架构自动配参数

选定底模，采样器、调度器、步数、CFG、shift、文本编码器类型、VAE 全部自动就位。
架构靠**权重张量名**判断，不看文件名——文件可以随便改名，权重不会说谎。

### LoRA 按架构隔离

一支 Krea 2 的画风 LoRA 只会在 Krea 2 下出现，切到 Anima 就自动隐藏。
每支可单独拖权重，未启用的会显示建议默认值。

### 中文直接出图

用中文写就行。点「转写」，本地模型把它变成英文提示词，**先给你一版预览**，
改到满意再生成。

输出格式跟着架构走：Anima / SDXL 给「一句描述 + Tags 行」；
Krea 2 和 MOSS 给完整段落——这两家的编码器读长文本，塞成标签反而丢细节。
翻译时还会保证你说的每个细节都活下来，不被"氛围词"顶掉。

模型跑在 **CPU**（llama.cpp），不占显卡显存；只在点转写时才启动，
空闲十分钟自动退出。可选装，不装也能用，自己写英文提示词即可。

### 预设可分享，LoRA 清单也给了

`presets/` 里 27 个配方各自挂了自己的 LoRA。这些 LoRA 的名字、体积、用途
整理在 [`loras.manifest.json`](loras.manifest.json)——想跑哪个预设，照着清单装就行。
装不下全套也没关系：不装 LoRA 一样能出图，只是配方里挂的那几支会提示缺件。

### 参数配方可分享

界面上调好的整套设置导出成一个 `.json`，拖回界面即还原：

```
模型 + 画质档 + 尺寸 + 步数 + CFG + 采样器 + 调度器 + shift + 种子 + LoRA 及其权重
```

### 其余

| | |
|---|---|
| **仓库配方一键导入** | 「参数预设」里直接列出 `presets/` 的示例，点导入即可，不用翻文件 |
| **配方编辑器** | 界面里直接改 JSON，实时校验语法，保存写回 `presets/`（覆盖前自动 `.bak`） |
| **LoRA 搜索** | 按名称、触发词、说明即时过滤，几百支也不难找 |
| **A/B 对比** | 两张图并排看，滚轮同步缩放，下方只列参数差异 |
| **提示词历史** | 最近 30 条提交过的提示词，可搜索、一键回填（含步数与底模） |
| **本地图库** | 生成的图带参数存档，可回填到界面重出 |
| **局部重绘** | 画蒙版只重画那一块，其余不动 |
| **高清二采** | latent / 像素放大 + 低噪重绘，一处开关 |
| **图反推标签** | WD14，拖张图进来出标签（需 `onnxruntime`，可选） |
| **控制图** | LLLite 等条件图，按架构显示 |
| **中文界面** | 界面全中文，内置角色与画师词库 |

---

## 支持的架构

| 架构 | 参数 | 默认配方 | 许可 |
|---|---|---|---|
| **Anima 2.9B** | 2.9B | Euler + sgm-uniform，28–50 步，CFG 3.5–5 | 非商用 |
| **Z-Image Turbo** | 6B | Res Multistep + Simple，9 步，CFG 1 | Apache-2.0 |
| **Krea 2 Turbo** | 12.9B | Euler + Simple，8 步起，CFG 1 | 社区（年收 <100 万美元免费） |
| **MOSS-Image** | 5B | Euler + Simple，50 步，CFG 3 | Apache-2.0 |
| **SDXL / Pony / Illustrious** | 6–7B | DPM++ 2M SDE + Karras，20–30 步 | 见各模型 |
| **更多 / 新出的架构** | 任意 | 交给 agent：模型和官方工作流一起给它，按 [`skill.md`](skill.md) 第六节加进来 | 见各模型 |

上面这几行不是白名单。新模型出来不用等更新——把它和官方 ComfyUI 工作流一起发给 agent，
它会按 `skill.md` 第六节的清单改八处（后端四处、前端四处），
再照官方工作流反推采样器、步数、CFG、shift 和各画质档，装完直接能用。

白名单那处最容易漏：漏了不报错，而是把架构静默换成上一个用过的，
拿错编码器去编码，最后报一个和真实原因无关的维度错。

---

## 快速开始

**方式 A · 仓库链接**（agent 自己 clone）

把下面这句话发给你的 agent（Claude Code / Cursor / WorkBuddy 等都可以）：

> 安装 https://github.com/KlockTX/KlockUI ，按仓库里的 `install.md` 执行。

**方式 B · 安装包（推荐 · 不用 git）**

从 [Releases](https://github.com/KlockTX/KlockUI/releases) 下载 `KlockUI-x.y.z.zip`，
把**压缩包文件本身**发给 agent，并说：

> 安装这个压缩包：`<拖入 KlockUI-x.y.z.zip>`，按包里的 `install.md` 执行安装配置。

包里自带 `AGENT-INSTALL.md`，agent 解压后会按同一套流程装。**不需要 agent 会 git clone**，
也不需要它访问 GitHub。

两种方式拿到代码后，**剩下的交给 agent**：`install.md` 和 `skill.md` 会引导它
先探测本机已有的 ComfyUI（有就复用，不重复装）、建 Python 环境、按显卡选量化档、
**问你要装哪些模型**、逐个文件校验下载、装好 `skill.md`，最后跑一张测试图验收。

仓库和包里都不含模型权重——**但不需要你自己下载**：agent 会按你的选择逐个装并校验。

手动装也可以，[`install.md`](install.md) 里每一步都带断言，照着走即可。

装完后启动：

```bat
start.bat      :: Windows：拉起引擎 + 界面，然后打开浏览器
stop.bat       :: 只停界面，引擎保留
```

```bash
# 任意平台
../ComfyUI/venv/bin/python server.py
```

打开 <http://127.0.0.1:7861> 。

---

## 运行结构

![运行结构](docs/architecture.svg)

三个进程都在本机：浏览器只是界面，KlockUI 负责把表单翻译成节点图，ComfyUI 执行，GPU 出图。
**没有任何云端调用**，图片和提示词不出本机。

---

## 参数配方

导出的 JSON 长这样：

```json
{
  "klockui": 1,
  "name": "雨夜霓虹 · 回眸",
  "model": "krea2_turbo_int8_convrot.safetensors",
  "arch": "krea",
  "prompt": "anime illustration, cel shading, clean lineart, ...",
  "quality": "standard",
  "size": { "ratio": "2:3", "width": 1024, "height": 1536 },
  "steps": 12,
  "cfg": 1,
  "sampler": "Euler",
  "scheduler": "Simple",
  "loras": [
    { "name": "krea2_yoneyama_mai", "weight": 0.75 },
    { "name": "krea2_cyberpunk_anime", "weight": 0.6 }
  ]
}
```

字段优先级：`model` → `quality` → 显式字段 → `loras`。

`quality` 是档位名（`gacha`/`draft`/`standard`/`fine`/`hires`），会一次性写入步数、CFG、二采；
JSON 里再写 `steps` 则以显式值为准。

`presets/` 里有 26 个可直接使用的例子，字段说明见 [`presets/README.md`](presets/README.md)。

二次元向的画师 LoRA 串、触发词与提示词模板整理在 [`docs/anime-recipes.md`](docs/anime-recipes.md)；
生成耗时的实测拆解见 [`docs/performance.md`](docs/performance.md)。

---

## 配置

所有路径都有默认值，也可用环境变量覆盖：

| 变量 | 默认 | 说明 |
|---|---|---|
| `KLOCK_COMFY_URL` | `http://127.0.0.1:8188` | 引擎地址 |
| `KLOCKUI_PORT` | `7861` | 本服务端口 |
| `KLOCK_MODELS_ROOT` | 自动探测 | 模型根目录 |
| `KLOCK_DIFFUSION_DIR` | `<root>/diffusion_models` | DiT 族底模 |
| `KLOCK_CHECKPOINT_DIR` | `<root>/checkpoints` | SDXL 系整模型 |
| `KLOCK_VAE_DIR` | `<root>/vae` | VAE |
| `KLOCK_LORA_DIR` | `<root>/loras` | LoRA |

模型根目录探测顺序：`KLOCK_MODELS_ROOT` → `<repo>/../models` → `<repo>/models` → `<repo>/../ComfyUI/models`。

---

## 常见问题

**为什么不用 ComfyUI 原生界面？**

原生界面是给"搭工作流"用的，KlockUI 是给"今天出 50 张图"用的。
它是包在 ComfyUI 外面的壳，不是替代品——引擎还是那个引擎，
只是换底模时不用再重新接一遍线。

**需要多少显存？**

| 显存 | 能跑 |
|---|---|
| 6GB | Anima（int8）+ 较低分辨率 |
| 8GB | Anima / Z-Image 舒服，Krea 2 需 `--lowvram` 且较慢 |
| 12GB+ | 全部架构可用 |
| 16GB+ | 全部架构 + 更高分辨率与二采 |

**模型从哪来？**

`models.manifest.json` 里每个文件都有地址、精确字节数、许可。
安装时 agent 会问你要哪几个架构，只下你选的。**仓库本身不含任何权重。**

**能商用吗？**

代码 GPL-3.0。模型各自授权：Z-Image / MOSS 是 Apache-2.0，Krea 2 有营收门槛，
**Anima 系是非商用**。拿它接单前请先看清楚 `license` 字段。

**图片会被上传吗？**

不会。没有账号、没有遥测、没有外部请求，除非你自己去下载模型。

**支持 macOS / AMD 吗？**

代码是纯 Python + 原生前端，理论上都能跑。但**只在 Windows + NVIDIA 上验证过**，
MPS / ROCm 下出问题不奇怪；提 issue 我会看，但不保证能修。

---

## 项目结构

```
KlockUI/
├─ server.py            # HTTP 服务、任务队列、图库、鉴权
├─ comfy_bridge.py      # 参数 → ComfyUI 工作流；所有架构知识都在这
├─ interrogate.py       # WD14 图反推（可选）
├─ index.html           # 单页前端
├─ assets/
│  ├─ app.js            # 前端逻辑：面板、预设、拖拽
│  ├─ artists.js        # 画师词库
│  └─ characters*.js    # 角色词库
├─ vendor/              # mdui + 图标字体（离线，无构建步骤）
├─ presets/             # 26 个示例配方
├─ docs/                # 架构图 · 二次元配方 · 前端约定
├─ install.md           # 安装说明（写给 agent）
├─ AGENT-INSTALL.md     # 仅发行包内有：告诉 agent「这是压缩包，照 install.md 装」
├─ scripts/
│  └─ make_release.py   # 生成发行包（只打 git 受控文件）
├─ skill.md             # 配置知识与排错（写给 agent）
└─ models.manifest.json # 模型清单
```

**没有构建步骤**：前端是原生 JS + CSS，`vendor/` 里的依赖直接引用。
clone 下来就能跑，不需要 `npm install`。

---

## 参与贡献

欢迎 issue 和 PR。几个让合并更顺畅的约定：

1. **架构相关改动**：先在 issue 里说明依据（官方文档 / 实测数据），不要凭印象调参数
2. **新增架构**：四处一起改，别只改 `_classify`
3. **提交前自检**：`python -c "import server, comfy_bridge"` 与 `node --check assets/app.js` 都要过
4. **别提交模型文件**：`.gitignore` 已挡，但 PR 里塞大文件会被拒
5. **commit 标题**：功能变更写清做了什么（如「配方编辑改为卡片内联展开」）；
   纯文档、文案类写「对 X 进行修改」；改动理由写正文，标题不铺开讲

排错思路和已知坑写在 [`skill.md`](skill.md) 里，改代码前建议先扫一眼。

---

## 致谢

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) —— 推理引擎，本项目是它的前端
- [mdui](https://www.mdui.org/) —— Material Design 组件库
- [Anima](https://huggingface.co/circlestone-labs/Anima) · [Z-Image](https://huggingface.co/Comfy-Org/Z-Image-Turbo) · [Krea 2](https://huggingface.co/Comfy-Org/Krea-2) · [MOSS-Image](https://huggingface.co/Comfy-Org/MOSS-Image) —— 开源权重

---

## 许可

代码：[**GPL-3.0**](LICENSE)。

模型权重不适用本许可。各架构授权见 `models.manifest.json` 的 `license` 字段，
其中 Anima 系为**非商用**，商用前请自行替换。
