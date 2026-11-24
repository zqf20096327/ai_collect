# ComfyUI 工作流合集 · ComfyUI Workflow Collection

> **584** 个精选 ComfyUI 工作流，覆盖 AI 生图、换脸、动画、修复、电商、室内设计等主流场景。
>
> **584** curated ComfyUI workflows covering image generation, face swap, animation, upscaling, e-commerce, interior design, and more.
>
> 📋 **[查看完整工作流索引 INDEX.md](./INDEX.md)** — 每个工作流均含作用描述与所需模型清单

---

## 目录结构

```
comfyUI-workflow/
├── templates/          # 所有工作流 JSON（584 个，扁平结构）
│   └── index.json      # 机器可读目录（自动生成，供 ComfyUI 模板浏览器使用）
├── scripts/
│   ├── gen_index.py              # 生成 INDEX.md（按内容自动分类）
│   └── gen_templates_index.py    # 生成 templates/index.json
├── INDEX.md            # 人类可读工作流索引（自动生成）
├── README.md
└── LICENSE
```

---

## 工作流分类 · Workflow Categories

工作流按内容自动分类（由 `scripts/gen_index.py` 在生成 INDEX.md 时推断）：

| 分类 | 说明 |
|------|------|
| 🎬 AI动画视频 | AnimateDiff · SVD图生视频 · DragNUWA · DynamiCrafter |
| 🧑 AI换脸人像 | ReActor · InstantID · PhotoMaker · Roop |
| 👗 AI电商换装 | OOTDiffusion 虚拟换装 · 服装设计 |
| ✂️ AI换背景抠图 | RemBG · BiRefNet · SAM · LayeredDiffusion |
| 🔧 AI画质修复 | SUPIR · CCSR · UltimateSD · 局部重绘 · BrushNet |
| 🎲 AI 2D→3D | Zero123 · SV3D · TripoSR |
| 🏠 AI室内设计 | 室内渲染 · 毛坯房效果图 · 建筑风格替换 |
| 📷 AI摄影写真 | 人像写真 · 虚拟摄影 |
| ✍️ AI文字艺术 | 艺术字 · 光影字 · Logo · 线稿绘画 |
| 🎨 AI创意趣玩 | 漫画风格 · 卡通 · 壁纸 · 创意特效 |
| 📖 入门基础 | ComfyUI 官方示例 · 文生图 · ControlNet · IPAdapter |

---

## 工作流索引 · Workflow Index

所有工作流的**作用描述**和**所需模型**汇总在 [INDEX.md](./INDEX.md)，按内容自动分类，方便快速定位目标工作流。

> 重新生成索引：`python scripts/gen_index.py`
> 重新生成模板目录：`python scripts/gen_templates_index.py`

---

## 常用自定义节点 · Common Custom Nodes

以下节点包被本仓库 **50 个以上**工作流使用，建议优先安装：

| 节点包 | 工作流数 | 主要功能 |
|--------|---------|---------|
| [ComfyUI-IPAdapter-plus](https://github.com/cubiq/ComfyUI_IPAdapter_plus) | 189 | 图像风格/人脸参考（IPAdapter） |
| [ComfyUI-ComfyRoll](https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes) | 139 | 工具节点集合（CR 系列） |
| [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite) | 120 | 视频加载/输出（VHS） |
| [ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack) | 108 | FaceDetailer · SAM 分割 · 检测器 |
| [UltimateSDUpscale](https://github.com/ssitu/ComfyUI_UltimateSDUpscale) | 94 | 终极 SD 放大 |
| [ComfyUI-AnimateDiff-Evolved](https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved) | 78 | AnimateDiff 动画生成 |
| [comfyui-wd14-tagger](https://github.com/pythongosssss/ComfyUI-WD14-Tagger) | 66 | WD14 自动打标 |
| [ComfyUI-ReActor](https://github.com/Gourieff/comfyui-reactor-node) | 62 | ReActor 换脸 |
| [comfyui_segment_anything](https://github.com/storyicon/comfyui_segment_anything) | 51 | Grounding DINO + SAM 分割 |

> 使用 [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager) → `Install Missing Custom Nodes` 可一键安装。

---

## 快速上手 · Quick Start

### 前提条件

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 已安装
- [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager) 推荐安装（可一键安装缺失节点）

### 使用步骤

1. **克隆仓库**
   ```bash
   git clone https://github.com/leolu/comfyUI-workflow.git
   ```

2. **选择工作流**  
   在 `templates/` 目录中找到对应的 `.json` 文件，或参考 [INDEX.md](./INDEX.md)。

3. **加载工作流**  
   打开 ComfyUI → 右上角菜单 → `Load` → 选择 `.json` 文件。

4. **安装缺失节点**  
   ComfyUI-Manager → `Install Missing Custom Nodes` 一键安装。

5. **下载模型**  
   参考下方模型下载表，将模型放到 ComfyUI 对应目录。

6. **运行**  
   点击 `Queue Prompt` 开始生成。

---

## 模型下载 · Model Downloads

> 模型文件体积较大（数百 MB 至数 GB），不含在本仓库中，需单独下载。

| 模型 | 用途 | 下载地址 |
|------|------|---------|
| SDXL Base 1.0 | 文生图基础模型 | [Hugging Face](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) |
| SD 1.5 | 经典基础模型 | [Hugging Face](https://huggingface.co/runwayml/stable-diffusion-v1-5) |
| AnimateDiff V2 | 动画生成 | [Hugging Face](https://huggingface.co/guoyww/animatediff) |
| InstantID | 人像一致性换脸 | [Hugging Face](https://huggingface.co/InstantX/InstantID) |
| IP-Adapter | 图像风格参考 | [Hugging Face](https://huggingface.co/h94/IP-Adapter) |
| SUPIR | 超分辨率图像修复 | [Hugging Face](https://huggingface.co/Kijai/SUPIR_pruned) |
| SVD XT | 图生视频 | [Hugging Face](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) |
| LCM LoRA | 实时/加速采样 | [Hugging Face](https://huggingface.co/latent-consistency) |
| SAM | 图像分割 | [Meta](https://github.com/facebookresearch/segment-anything#model-checkpoints) |
| Stable Zero123 | 多视角 3D 生成 | [Hugging Face](https://huggingface.co/stabilityai/stable-zero123) |

**Civitai 精选模型：** [civitai.com](https://civitai.com)

---

---

## 贡献 · Contributing

欢迎提交 PR 贡献新工作流！

1. 将 `.json` 文件放入 `templates/` 目录
2. 文件名清晰描述用途
3. PR 描述中注明所需模型和自定义节点
4. 确保工作流在 ComfyUI 最新版本可正常运行

---

## License

[MIT](./LICENSE) © 2025

> 部分工作流来源于社区分享，版权归原作者所有，本仓库仅供学习整理使用。

### ⚠️ 受限文件说明

`templates/` 中包含少量原作者声明「禁止商用 / 仅限学习交流」的工作流（文件名含「不可用于商业用途」字样），**不在本仓库 MIT 许可证的覆盖范围内**，请使用前自行确认。
