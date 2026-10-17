# ComfyUI-NovelAI-GENYTOOLS

![ComfyUI-NovelAI-GENYTOOLS 项目封面](docs/assets/ComfyUI-NovelAI-GENYTOOLS-cover.png)

一个面向 ComfyUI 的 NovelAI 图像生成与编辑节点包。它把 NovelAI 的模型、提示词、生成参数、角色分区、Vibe、精准参考和采样器拆成可自由连接的模块，并补充批量任务、XY 参数对比、分块放大、图片保存和元数据读取能力。

这是项目的首次公开发布，本文档集中介绍当前可用功能与使用方式。

现已支持 **NovelAI Diffusion V5 Curated / Full**，包括 Standard / Light 质量模式、Anime / Furry 数据集、透明背景、最多 32 个角色与自由定位、自动 `teXt:` 文字块、Max✨ Enhance 和 Opus 免费生成额度显示。V5 当前不支持 Vibe Transfer 与精准参考，插件会在发送请求前明确提示。为获得更好的节点界面显示效果，建议开启 **ComfyUI Node 2.0**。

> 本项目是社区开发的非官方 ComfyUI 扩展，与 NovelAI 官方无隶属关系。调用 NovelAI API 需要用户自己的 Persistent API Token；生成、编码、增强和部分编辑操作可能消耗 Anlas。

## 主要优势

- **ComfyUI 原生模块化设计**：工作流结构接近 `模型加载器 → LoRA/参考 → KSampler`，模型、提示词、参数和参考图均可独立复用。
- **中文节点与参数界面**：常用选项、错误说明、费用统计和节点名称均为中文。
- **覆盖常用 NovelAI 生图能力**：文生图、图生图、局部重绘、角色分区、Vibe Transfer、精准参考、Enhance、Variations 和 Director Tools。
- **角色分区编辑器**：V5 最多添加 32 个角色并支持连续自由坐标；V4/V4.5 最多 6 个角色并使用 5×5 网格。每个角色都可分别设置正负提示词或交给 AI 决定位置。
- **Vibe 完整工作流**：支持图片编码、多个 Vibe 串联、本地 Vibe/Bundle 加载、预览和文件保存。
- **面向大图的分块精修**：先在本地放大，再把画面分块交给 NovelAI 重绘，使用重叠区域、余弦羽化、稳定 Seed 和缓存恢复完成拼接。
- **批量与参数研究工具**：逐条替换提示词生成同风格系列图片，或生成带标签的 XY 参数对比图。
- **费用与隐私保护**：支持 Anlas 上限、缓存续跑和余额显示；Token 不进入工作流 JSON、节点输入、图片元数据或日志。

## 功能总览

### 模型、提示词与生成参数

- `NAI 模型加载器`：选择 V5 Full/Curated、V4.5 Full/Curated、V4 Full/Curated、Anime V3 或 Furry V3，输出可继续串联的 `NAI_PIPE`。节点可显示订阅与 Anlas 余额；选择 V5 时还会显示 Opus 免费额度、估算剩余张数和每日恢复速度。
- `NAI 正面提示词` / `NAI 负面提示词`：使用不同端口类型，避免把正负提示词接反。
- `NAI 正面提示词拼接` / `NAI 负面提示词拼接`：把人物、服装、场景、画风等文本模块组合起来。
- `NAI 正面提示词处理器` / `NAI 负面提示词处理器`：处理随机化、Prompt Chunks、强调和文本片段；V5 会为引号中的文字自动生成官方 `teXt:` 文本块，并避免重复处理已手写的文本块。
- `NAI 核心参数`：设置分辨率、宽高、Steps、Guidance、采样器和噪声调度。
- `NAI 高级参数`：设置 CFG Rescale、CFG Delay、Decrisper、SMEA、动态阈值、质量标签、UC 预设、数据集模式、透明背景、Vibe 归一化和输出格式；V5 支持 Standard / Light / 关闭质量标签以及 Anime / Furry 模式。

### 文生图、图生图与局部重绘

- `NAI 文生图采样器`：使用模块化模型管线、正负提示词和参数卡生成图片。
- `NAI 图生图采样器`：接收 ComfyUI `IMAGE`，通过 Strength 与 Noise 控制保留原图和重新构图的程度。
- `NAI 局部重绘采样器`：接收 `IMAGE + MASK`，使用 NovelAI Inpainting 模型与官方局部重绘请求结构；未遮罩区域在回贴时保留原图。V5 Full 使用原生 V5 Inpainting；V5 Curated 当前按官网行为使用 V4.5 Curated Inpainting，因此该模式最多保留 6 个角色。
- 单次生成张数支持 **1–4 张**，与 NovelAI 单次请求上限一致。
- 采样器返回标准 ComfyUI `IMAGE` 批次、实际 Seed 列表以及费用和调用统计。

```text
NAI 模型加载器 ───────────────────────────────┐
NAI 正面提示词 ───────────────────────────────┤
NAI 负面提示词 ───────────────────────────────┤→ NAI 文生图采样器 → Preview / NAI 图片保存器
NAI 核心参数 ─────────────────────────────────┤
NAI 高级参数 ─────────────────────────────────┘
```

### V5 与 V4/V4.5 角色分区

`NAI 角色分区编辑器`可以直接插入模型管线：

```text
NAI 模型加载器 → NAI 角色分区编辑器 → NAI 文生图/图生图采样器
                         ↑
                    NAI 核心参数
```

- V5 一个节点最多添加 32 个角色；V4/V4.5 最多添加 6 个角色。
- 每个角色拥有独立的正面提示词、负面提示词和启用开关。
- 可以选择“由 AI 决定位置”；V5 手动位置使用连续自由坐标，V4/V4.5 仍使用 5×5 网格中心点。
- 位置编辑器会读取核心参数的宽高，以横图、竖图或方图的真实比例显示。
- 角色顺序、提示词和位置会随工作流保存，但不会保存 Token。
- 角色分区适用于 V5 与 V4/V4.5 模型；V5 Curated 局部重绘因模型回退限制为最多 6 个角色。

### Vibe Transfer 与精准参考

- `NAI 图片 Vibe 编码器`：把输入图片编码为 Vibe，Information Extracted 默认 `0.7`，编码结果可以缓存并加入模型管线。
- `NAI Vibe 文件加载器`：加载 `.naiv4vibe` 或 `.naiv4vibeBundle`，像 LoRA 加载器一样连续串联多个 Vibe。
- `NAI Vibe 文件保存器`：保存当前管线中的 Vibe；单个导出为 `.naiv4vibe`，多个自动导出为 `.naiv4vibeBundle`。
- `NAI 精准参考应用器`：V4.5 可使用角色、风格或角色与风格参考，并设置 Strength 与 Fidelity。
- Vibe 与精准参考遵循 NovelAI 模型能力限制。NovelAI 当前尚未向 V5 开放这两项能力；插件会在发送付费请求前给出中文错误，不会静默忽略参数或自动更换模型。

```text
NAI 模型加载器 → Vibe 文件加载器 → Vibe 文件加载器 → 采样器

NAI 模型加载器 → 图片 Vibe 编码器 → 采样器
                         └────────→ Vibe 文件保存器

NAI 模型加载器 → 精准参考应用器 → 采样器
```

### 分块放大与大图精修

`NAI 模块化分块放大`用于处理已经由本地 ESRGAN、AnimeSharp 等模型放大的图片：按照指定尺寸裁成多个有重叠的图块，逐块执行 NovelAI Img2Img，再通过二维余弦权重融合回完整画布。

![Tile 分块放大效果对比](docs/assets/tile-upscale-comparison.png)

核心能力：

- 图块宽高可自定义，也可跟随原始小图尺寸。
- 横向/纵向重叠与实际融合带宽分别控制。
- 每个图块使用稳定派生 Seed，重复运行能够复现。
- 每块完成后写入缓存；网络中断或手动停止后，重新运行只补缺失图块。
- 支持彩色噪点抑制，降低低 Noise 重绘时出现的零星彩色像素。
- 可连接角色分区、Vibe 或精准参考管线；其中 Vibe 与精准参考仅用于当前支持它们的模型，不能与 V5 组合。

```text
原始小图 ───────────────────────────────────┐
原始小图 → 本地放大模型 → 本地放大图 ───────┤
NAI 模型管线 + 正负提示词 + 参数卡 ─────────┤→ NAI 模块化分块放大 → NAI 图片保存器
```

插件同时保留经典分阶段节点：`NovelAI 分块规划`、`NovelAI V4.5 逐块重绘`、`NovelAI 分块融合`、`NovelAI 二次接缝修复`和`NovelAI 一键分块放大`，适合需要单独观察或调整每个阶段的工作流。

### Enhance、Variations 与 Director Tools

- `NAI Enhance 增强`：按 NovelAI Enhance 逻辑重新处理输入图并增强细节，支持 1×、1.5×、2× 与 V5 Max✨，可选择简化 Magnitude 或高级 Strength/Noise 控制。
- `NAI 图片变体`：基于输入图生成多个可复现的变化版本。
- `NAI 移除背景`：输出背景处理结果。
- `NAI 清理杂物`：清理画面中的杂物，可配置是否保留文字气泡。
- `NAI 提取线稿`：从输入图提取线稿。
- `NAI 转换草图`：将输入图转换成草图。
- `NAI 自动上色`：为线稿或草图自动上色，支持提示词与 Defry。
- `NAI 修改表情`：选择目标表情、强度并附加提示词。
- `NAI 官方放大`：调用 NovelAI 当前固定 2× 的 V5 Curated 放大接口；费用按输入像素分为 1/2/3/4 Anlas，最大输入为 3,145,728 像素。旧工作流中的 4× 选项会明确迁移到当前 2× 行为。
- `NAI 标签建议`：获取提示词标签建议。

### 批量任务与 XY 参数对比

`NAI 批量提示词任务列表`与`NAI 批量文生图任务`可像 for 循环一样逐项生成同一画风的系列图片：

```text
正面提示词模板：{base}, {item}
固定内容：{base}
任务列表中的当前人物/服装/场景：{item}
```

- 每个任务固定 `n_samples=1`，避免使用单次多图请求。
- 支持固定、递增或按任务文本稳定派生 Seed。
- 支持指定起始任务、最大执行数量、请求间隔和总 Anlas 上限。
- 支持逐项缓存，失败重跑时只生成尚未完成的任务。

`NAI XY 轴参数`与`NAI XY 对比图`可比较 Seed、Steps、Guidance、CFG、采样器、噪声调度、模型、分辨率、提示词后缀、Vibe 强度和精准参考参数。横纵轴各支持 1–6 个值，最多形成 6×6 对比矩阵；每个单元格固定生成一张。

### 图片保存与元数据

- `NAI 图片保存器`可以真正保存 PNG 或 WebP，不受 ComfyUI 原生 Save Image 固定 PNG 的限制；V5 透明背景 PNG 会保留 RGBA Alpha 通道。
- PNG 写入 NovelAI 风格的 iTXt 元数据；WebP 写入对应 EXIF/XMP 数据。
- 可保存提示词、UC、模型、Seed、采样器、角色、Vibe 和生成参数。
- `NAI 图片元数据读取`可以读取本节点保存的图片以及兼容的 NovelAI 图片信息。
- 默认不把 ComfyUI 工作流写入图片；如需保留工作流，可在保存器中手动开启。

## 模型能力说明

| 模型 | 角色分区 | Vibe | 精准参考 | 透明背景 | Max✨ Enhance | SMEA / 动态阈值 |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| V5 Full / Curated | ✅（最多 32 个） | — | — | ✅ | ✅ | — |
| V4.5 Full / Curated | ✅（最多 6 个） | ✅ | ✅ | — | — | — |
| V4 Full / Curated | ✅（最多 6 个） | ✅ | — | — | — | — |
| Anime V3 / Furry V3 | — | ✅ | — | — | — | ✅ |

V5 Full 支持原生 V5 局部重绘；V5 Curated 当前使用 V4.5 Curated Inpainting，因此 V5 Curated 局部重绘最多支持 6 个角色。Opus 订阅在普通分辨率、最多 28 Steps 的 V5 生成中可使用会自动恢复的免费额度，额度耗尽后仍可消耗 Anlas 继续生成。

不兼容的模型与参数组合会在 API 调用前停止并给出中文说明，不会自动换模型或静默删除参数。

## 安装

### 方法一：下载 ZIP

1. 从 GitHub Releases 下载压缩包。
2. 解压到 `ComfyUI/custom_nodes/ComfyUI-NovelAI-GENYTOOLS`。
3. 安装依赖：

```powershell
pip install -r ComfyUI/custom_nodes/ComfyUI-NovelAI-GENYTOOLS/requirements.txt
```

4. 通过自己的启动器重启 ComfyUI。

### 方法二：Git 安装

```powershell
cd ComfyUI/custom_nodes
git clone https://github.com/XTOGENY/ComfyUI-NovelAI-GENYTOOLS.git
pip install -r ComfyUI-NovelAI-GENYTOOLS/requirements.txt
```

## 配置 NovelAI Token

1. 在 NovelAI 账户设置中生成 Persistent API Token。
2. 打开 ComfyUI 设置。
3. 找到 `NovelAI 2.0：Persistent API Token`。
4. 填入 Token，并按需选择是否保存在本机 ComfyUI 用户设置中。

Token 只同步到当前 ComfyUI 后端内存，并按照 ComfyUI 设置策略保存在本机。它不会出现在节点字段、工作流 JSON、PNG 元数据、日志或错误消息中。

## 示例工作流

仓库的 `examples/` 目录提供可直接拖入 ComfyUI 的中文工作流：

- 基础文生图与图生图
- Vibe 风格参考文生图/图生图
- 角色分区文生图/图生图
- 精准参考文生图
- 局部重绘
- 分块放大
- Director Tools
- 同风格批量文生图
- XY 参数对比图
- NAI 图片保存器
- 全节点参数说明与按场景分类总工作流

建议先加载对应场景的示例，确认模型、分辨率、图片数量和 Anlas 上限，再执行付费请求。

## 缓存与本地文件

- Vibe 文件默认位于 ComfyUI 输入目录的 `novelai_vibes` 子目录。
- 分块、Vibe 编码、批量任务和 XY 单元格缓存位于 ComfyUI 用户目录下的 `novelai_tiled_upscale`。
- 缓存键包含输入像素、模型、提示词、Seed、坐标和相关采样参数；参数变化后不会错误复用旧结果。
- 可以通过缓存容量参数限制本地占用。

## 使用提醒

- 只有用户主动执行采样器或付费编辑节点时才会请求 NovelAI API。
- 图片 Vibe 首次编码、生成、Enhance、Variations、Director Tools 和官方放大可能产生 Anlas 消耗；符合条件的 Opus V5 生成会优先使用免费额度。
- 批量任务、XY 图和分块放大会产生多次 API 请求，建议开启缓存并设置费用上限。
- NovelAI 接口、模型和费用规则可能调整，请以 NovelAI 当前账户界面与官方说明为准。

## License

[MIT License](LICENSE)

