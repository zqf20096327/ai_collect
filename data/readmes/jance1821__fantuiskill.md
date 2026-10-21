# FantuiDB · 电商视频爆款分镜逆向复刻专家

> 把一条爆款电商视频**拆成 6/9/12 宫格分镜骨架**，再把其中的**产品 / 人物 / 场景**换成你自己的，
> 最终产出一张同规格的新故事板图——原有爆款框架不被破坏，替换部分精准可控。

[![version](https://img.shields.io/badge/version-0.3.0-blue)](./SKILL.md)
[![python](https://img.shields.io/badge/python-3.9%2B-3776ab)](https://www.python.org/)
[![license](https://img.shields.io/badge/license-MIT-green)](./LICENSE)
[![agent](https://img.shields.io/badge/agent-SKILL.md%20compatible-8b5cf6)](#三支持的主流-agent)
[![model](https://img.shields.io/badge/model-厂商无关-0ea5e9)](#六模型接入理解层与出图层)

---

## 一、它解决什么问题

电商投流的核心成本不在剪辑，而在**验证哪条创意能跑量**。一条跑出来的爆款视频，其价值不只是画面本身，而是它已经验证过的四件事：

1. **镜头顺序** —— 什么景别、什么角度、按什么节奏切。
2. **商品展示逻辑** —— 产品何时出现、怎么拿、怎么演示。
3. **转化脚本结构** —— 钩子 → 痛点 → 卖点 → 演示 → 信任 → 收口。
4. **视觉真实感** —— UGC 感、色温、光质、手持感、生活化背景。

传统做法是"照着拍一条"，成本高、周期长、还原度靠人。本 Skill 把这条链路工程化为**可复现的流水线**：先把参考视频压成结构化的分镜骨架，再把骨架套到你的产品上，由图像模型出图。

**定位说明（重要）**：本 Skill 是**分镜打样系统**，不是最终成片系统。它输出的是可继续接图生视频模型的故事板图与逐格 Prompt。

| 它做 | 它不做 |
|---|---|
| 逆向拆解参考视频的分镜结构、销售链路、视觉 DNA | ❌ 承诺逐像素复制原视频 |
| 输出结构化分镜 JSON + Excel 可录入表格 | ❌ 编造产品不存在的功能 |
| 把产品 / 人物 / 场景自然替换进原骨架 | ❌ 把新产品改成其他品类 |
| 输出整张宫格 Prompt + 每格独立 Prompt | ❌ 直接产出可投放级成片 |
| 出图后自动质检，未通过则自动修正重绘 | ❌ 复刻他人商标 / 真人身份做商用冒充 |

---

## 二、技术原理

![FantuiDB 流水线架构](docs/assets/pipeline.svg)

整套流程建立在一条判断上：**分镜结构是可迁移的，画面像素不是。** 因此流水线拆成三段——拆解、替换、质检——每段都以结构化 JSON 作为交接物，而不是让模型"看着办"。

### 1. 拆解层：从视频到分镜骨架

**关键设计是"双路抽帧 + AI 选帧"两步走，而不是平均抽帧。**

- **ffprobe** 先读取时长、分辨率、帧率、码率，作为后续抽帧密度的决策依据。
- **FFmpeg 双路抽帧**：
  - 均匀路径 `fps=...` —— 保证全时段覆盖，密度约为目标帧数的 2 倍；
  - 场景切变路径 `select='gt(scene,0.28)'` —— 抓真正的镜头切换点（阈值 0.2–0.35 可调）。
- 两路结果按时间戳重新排序合并，再用 `pick_evenly` 压缩到 24–48 张候选帧，同时计算每帧的**边缘方差**作为清晰度代理指标，用于后续剔除模糊帧。
- **多模态大模型选帧**：候选帧先被 Pillow 拼成每页 12 图的 contact sheet 再送模型（降低 token 与请求数）。模型不是"选好看的图"，而是按 **9 类销售节点**筛选：

  `hook` · `pain` · `product_show` · `demo` · `closeup` · `result` · `reaction` · `trust` · `cta`

- 选帧结果会经过**程序化校验**：帧数是否等于宫格数、frame_id 是否在候选清单内、是否重复、时间戳是否单调、是否覆盖钩子与转化节点。校验失败自动追加 issue 让模型重选一次；仍失败则降级为**规则兜底选帧**（均匀取帧），并在 `quality_check.needs_second_pass` 中标记。
- **Pillow 本地拼图**：`cover` 居中裁剪填满格子（不拉伸变形），格间距与外边距 4px，浅灰底。默认不加任何文字水印——宫格是分析板，不是海报。

### 2. 反推断层：从宫格图到分镜脚本

**这里没有独立 ASR 环节**，这是本 Skill 与常见方案的核心差异。

只要理解层接入的是**支持图片输入的多模态大模型**，它就能直接读取宫格图，同时提取：

- 画面信息：景别、镜头角度、镜头运动、主体、产品位置与露出方式、左右手动作、产品交互动作、表情、背景、光线、转场；
- 画面文字：屏幕字幕、贴纸、标题；
- **口播与字幕节奏**（从画面文字 + 分镜顺序反推脚本结构）。

输出 `reference_analysis.json`，包含完整的视觉 DNA 分析：

```text
video_basic_info   → 视频类型、预估时长、平台风格、整体风格
visual_dna         → 拍摄手法、画幅、光线、色温、构图、UGC 程度、背景复杂度、剪辑节奏
script_table[]     → 逐格分镜（26 个字段）
conversion_logic   → 钩子/痛点/信任/演示/利益叠加/收口 六段链路拆解
copywriting_extraction → 逐句文案功能标注（钩子/痛点/卖点/证明/促单/互动）
replication_notes  → 必须保留 / 可调整 / 不可偏离
confidence_report  → 视觉置信度与音频对齐置信度
```

再由 `export_excel_csv.py` 转成 **26 列 UTF-8-BOM 的 CSV**，可直接用 Excel / WPS 打开录入。

### 3. 替换层：从骨架到新产品故事板

- **产品画像提取**：产品图交理解层模型，提取品类、形状、主辅色、材质视觉感、表面细节、识别点，并输出三组约束：
  - `must_keep` —— 必须保持的颜色/形状/logo/比例/结构；
  - `can_adapt` —— 可随场景自然变化的摆放角度、光线、手持方式；
  - `must_avoid` —— 不可变成其他品类、不可凭空增加功能、**不可把白底图的白底背景带进场景**。
- **Prompt 融合**：把原分镜 JSON + 产品画像 + 参考宫格图一起交给理解层模型，输出整张宫格 Prompt 与逐格 Prompt，并强制带上一致性规则（产品一致、人物一致、场景一致、光线一致、叙事连续）。
- **出图**：由可插拔的 Image Provider 完成（见下文第六节）。

### 4. 三种任务模式

| 模式 | 行为 | 适用 |
|---|---|---|
| `strict_replace` | 场景、镜头、构图、动作全部锁定，只换产品/人物/局部元素 | "原爆款形态不变，只换我的产品" |
| `storyboard_transfer` **（默认）** | 保留结构、节奏、分镜顺序、卖点推进逻辑，允许换产品/人物/场景 | "保留爆款逻辑，不要求逐帧一致" |
| `hybrid_creative` | 保留骨架与销售逻辑，允许适度创意变化 | 仅在用户明确要求时使用 |

### 5. 质检与自愈闭环

生成完成后，理解层模型以**原参考宫格图 vs 新生成宫格图**做对照质检，质检项为硬门槛：

```text
key_frames_valid             关键帧有效
grid_order_correct           宫格顺序正确
product_consistent           产品一致（外观/颜色/结构/logo 不漂移）
product_naturally_integrated 产品自然融合（不悬浮、比例正确、接触面正确）
hands_perspective_contact_valid  手部透视与遮挡合理
scene_drift         = false  无场景漂移
text_pollution      = false  无字幕/水印/贴纸污染
poster_style        = false  无海报棚拍感
sales_structure_preserved    销售结构完整
```

任一项不通过 → 生成 `repair_prompt.txt` → 带原宫格 + 上轮结果 + 产品图重新出图 → 再质检，最多重试 `repair_attempts` 次（默认 2）。**未通过则直接抛错，不允许把不合格结果当成功交付。**

---

## 三、支持的主流 Agent

本 Skill 遵循 `SKILL.md` 约定，能力需求是「**能执行本地 shell / Python 命令**」。按执行能力分三档：

### Tier 1 · 完整能力（推荐）

可以直接跑通全流程（含 FFmpeg 抽帧与本地拼图）。

| Agent | 接入方式 |
|---|---|
| **Trae** | 项目内放置 `SKILL.md`，Agent 自动识别；上传视频后按提示推进 |
| **Claude Code** | 仓库根目录即工作区，直接对话触发；脚本由其 Bash 工具执行 |
| **Cursor / Windsurf** | 作为项目打开，用 Agent 模式对话触发 |
| **Codex CLI / Gemini CLI** | 在仓库目录内运行，允许执行本地命令 |
| **WorkBuddy** | 作为本地项目打开，Skill 自动加载 |
| **Cline / Roo Code** 等 VS Code Agent | 授予终端执行权限后可用 |

**建议的对话触发语**（任一句即可）：

```text
分析这个爆款视频，我要拆 9 宫格
帮我拆解这个带货视频，再把产品换成我的
把这个视频的产品替换成我的产品，保留原分镜结构
参考爆款视频生成我产品的新故事板
```

### Tier 2 · 工作流编排

把各步骤封装为节点，适合团队化 / 批量化生产。

| 平台 | 用法 |
|---|---|
| **n8n** | 见 [`docs/n8n_nodes.md`](docs/n8n_nodes.md)，完整节点蓝图 + 理解层 / 出图 API 节点配置；建议拆成 `/upload-reference-video` 与 `/replace-product-storyboard` 两个 Webhook，**一条爆款拆一次，可复用到 N 个产品** |
| **Dify / Coze / 阿里云百炼** | 把 Shell 节点 + HTTP 节点按同样顺序串起来 |

### Tier 3 · 仅对话（降级路径）

无法执行本地脚本的纯网页对话环境（如 Claude.ai 网页版、ChatGPT GPTs）：

- 抽帧与拼图改由**用户手动完成**（上传关键帧截图）；
- 其余分析、替换、Prompt 生成环节不受影响，但**会丢失准确时间戳，动作时间线变弱**；
- 无音频文本时口播分析降级为纯画面推断。

> 降级策略的完整对照表见 [`SKILL.md` 第 9 节](./SKILL.md)。

---

## 四、快速开始

### 1. 环境准备

```bash
# 1) FFmpeg（必须为完整版，含 ffprobe）
#    Windows:  winget install Gyan.FFmpeg
#    macOS:    brew install ffmpeg
#    Ubuntu:   sudo apt install ffmpeg

# 2) Python 依赖
pip install -r requirements.txt

# 3) 校验
ffmpeg -version && ffprobe -version
```

> FFmpeg 不在 PATH 时，可通过环境变量 `FFMPEG_PATH` / `FFPROBE_PATH` 指定可执行文件或所在目录。

### 2. 配置模型

```bash
cp .env.example .env
```

**理解层**——填任意一个兼容 OpenAI `chat/completions` 且支持图片输入的大模型（厂商不限）：

```env
LLM_API_KEY=你的密钥
LLM_BASE_URL=https://<你的服务地址>/v1
LLM_MODEL=<模型名或接入点 ID>
```

**出图层**——填任意一个能"吃 Prompt + 参考图、吐图片"的模型，下面以内置参考实现为例：

```env
IMAGE2_API_KEY=你的密钥
IMAGE2_BASE_URL=https://api.yijiarj.cn/v1/chat/completions
IMAGE2_MODEL=image2-4k
```

> ⚠️ `.env` 已在 `.gitignore` 中，**绝不要提交或外发**。

### 3. 准备输入

仓库已自带一个空的 `input/` 目录（目录内的素材文件被 `.gitignore` 忽略，不会入库），把你的素材直接放进去即可：

```text
input/
├── reference_video.mp4     # 15–30 秒或 50 秒左右的爆款/电商视频
└── product_main.jpg        # 你的产品图（建议 4 张：主图 + 45° + 侧面 + 细节）
```

> 如果你想用别的目录，改 `config.json` 的 `reference_video` 字段即可（支持相对路径与绝对路径）。

### 4. 运行

```bash
# 一次跑完 阶段 A + 阶段 B
python scripts/run.py \
  --config config.json \
  --product-images input/product_main.jpg input/product_45.jpg

# 只跑阶段 A（先看拆解结果，再决定要不要替换）
python scripts/run.py --config config.json --phase a

# 换出图模型
python scripts/run.py --config config.json --provider nano_banana \
  --product-images input/product_main.jpg
```

`config.json` 关键字段：

```json
{
  "job_id": "user_demo_001",
  "reference_video": "input/reference_video.mp4",
  "grid_count": 9,
  "candidate_count": 24,
  "scene_threshold": 0.28,
  "image_provider": "image2",
  "repair_attempts": 2
}
```

### 5. 分阶段使用的理由

先视频、后产品图，是**避免模型过早进入"创作模式"**：

```text
阶段 A：参考视频 → 分镜结构 → 镜头节奏 → 产品出镜逻辑 → 转化链路
阶段 B：产品图  → 产品画像 → 替换规则 → 新故事板
```

一次拆解、多次复用：`reference_analysis.json` 与宫格图存下来后，换不同产品可反复跑阶段 B，无需重新拆视频。

### 6. 查看产物

```text
runs/{job_id}/
├── grid_images/reference_grid_9.jpg       # 原视频分镜骨架
├── analysis/reference_analysis.json       # 结构化分镜脚本
├── analysis/shot_table.csv                # Excel 可直接打开
├── prompts/new_storyboard_prompt.json     # 每格独立 Prompt
├── storyboard_output/new_product_storyboard.png  # ★ 最终故事板图
└── quality_check/final_quality_check.json # 质检报告
```

导出交付：

```bash
python copy_results.py --run-dir runs/user_demo_001 --out-dir "D:/交付/某产品故事板"
```

清理中间产物（仅移入回收站，可恢复）：

```powershell
powershell -ExecutionPolicy Bypass -File cleanup_preview.ps1
```

---

## 五、宫格规格怎么选

| 规格 | 布局 | 适用视频 | 说明 |
|---|---|---|---|
| **6 宫格** | 3 列 × 2 行 | 8–10 秒、镜头少、动作简单 | 结构简单时宁可降到 6 格，也不要硬塞低价值帧 |
| **9 宫格** | 3 列 × 3 行 | **15–30 秒，大多数电商带货视频** | **默认推荐**，也是典型抖音/千川视频的最佳匹配 |
| **12 宫格** | 3 列 × 4 行 | 30 秒以上、镜头多、卖点多、动作复杂 | 信息密度高时宁可升到 12 格，也不用重复帧凑数 |

**单张图上限为 12 格**。若镜头数超过 12 个，请拆成多轮 run（每轮 ≤12 格）后再二次拼接，不要靠重复帧凑数。

每格为 9:16 竖屏，适配抖音 / TikTok / 千川等短视频平台；总画布比例由布局自然决定，不强制 16:9。

---

## 六、模型接入：理解层与出图层

**两层都不绑定模型厂商，本仓库也不限定可选范围。**

### 6.1 理解层 —— 任意大模型，推荐多模态

只要同时满足两点，任何自建或云端模型都能直接使用：

1. 兼容 OpenAI 协议：`POST {LLM_BASE_URL}/chat/completions`，请求 / 响应结构一致；
2. **支持图片输入（多模态）**——流水线要靠它读宫格图与产品图；纯文本模型无法完成反推断。

配置三个环境变量即可，代码里没有任何厂商默认值：

```env
LLM_API_KEY=你的密钥
LLM_BASE_URL=https://<你的服务地址>/v1
LLM_MODEL=<模型名或接入点 ID>
```

支持中途换模型：改这三个变量即可，无需改动任何代码。（若你此前已配置过旧的变量名，程序会自动回落兼容。）

### 6.2 出图层 —— 任何生图模型都能接入

出图层是一套**开放契约**，统一在 `scripts/providers/base.py` 的 `ImageProvider`：只要你的模型能"接收 Prompt + 参考图、返回图片"，就能接进来。

仓库内置了三个**参考实现**（开箱可用，方便快速上手），但它们**只是示例，不是可选范围的上限**：

| 规范名 | 默认模型 | 接入协议 | 适合场景 |
|---|---|---|---|
| `image2` | `image2-4k` | OpenAI 兼容 chat/completions | 国内直连友好，4K 出图 |
| `gpt_image` | `gpt-image-1` | OpenAI Images API（generations / edits） | 指令遵循与文字渲染强；支持多参考图 edits |
| `nano_banana` | `gemini-2.5-flash-image` | Gemini 原生 `generateContent` | 多图输入 + 一致性保持突出，最贴合本任务 |

除了这三个，**其他生图模型同样支持**，接入方式有三条路：

1. **零代码**：若目标模型提供 OpenAI 兼容的 `chat/completions`，直接复用内置实现，只把 `base_url` / `model` / `api_key` 换成对方的——**无需写代码**。
2. **加一个 provider**：继承 `ImageProvider` 实现 `generate()`，在注册表登记（约 40 行）。见 [image_models.md 第 4 节](docs/image_models.md)。
3. **手工出图**：把 `prompts/image2_storyboard_prompt.txt` 的 Prompt 与参考图拿到网页端生成，走降级路径。

```bash
# 列出已内置的参考实现
python -c "from providers import list_providers; print(list_providers())"

# 选择用哪个
python scripts/run.py --config config.json --provider nano_banana --product-images input/product_main.jpg
```

各模型在**本任务**（整张宫格 + 多参考图 + 强一致性约束）下的具体表现、参数与踩坑，见
👉 [`docs/image_models.md`](docs/image_models.md)

---

## 七、插件与环境依赖

### 必需

| 依赖 | 版本 | 用途 |
|---|---|---|
| **FFmpeg**（完整版，含 **ffprobe**） | 5.0+ | 读取视频元信息、抽帧、场景切变检测 |
| **Python** | 3.9+（推荐 3.10+；已在 3.13 验证） | 流水线脚本 |
| **Pillow** | ≥10.0.0 | 拼宫格、裁剪、缩放、清晰度计算 |
| **requests** | ≥2.31.0 | 调用理解层与出图 API |

### API

| 服务 | 必需性 | 用途 |
|---|---|---|
| **理解层大模型**（任意厂商，需支持图片输入） | **必需** | 选帧、视频反推断、产品画像、Prompt 生成、自动质检 |
| **出图模型**（任意，仓库内置 3 个参考实现） | **必需**（阶段 B） | 生成新故事板图 |

### 可选

| 项 | 说明 |
|---|---|
| **n8n** | 工作流编排（Tier 2） |
| **openpyxl** | 不需要。CSV 用 UTF-8-BOM 输出，Excel/WPS 直接双击无乱码 |
| **独立 ASR 服务** | 不需要。口播由理解层多模态模型从宫格图直接提取 |

完整的依赖清单、环境变量、故障排查，见 👉 [`docs/dependencies.md`](docs/dependencies.md)

---

## 八、注意事项与已知限制

### 使用前必读

1. **FFmpeg 必须是完整版**，仅装 `ffmpeg` 而无 `ffprobe` 会在第一步就失败。
2. **理解层必须选支持图片输入的多模态模型**，纯文本模型无法完成反推断。
3. **`.env` 含真实密钥**，已在 `.gitignore` 中，切勿提交。
4. **产品图建议 4 张**（主图 / 45° / 侧面 / 细节）。单图也能跑，但产品一致性与避免"脑补背面"的能力会明显下降。
5. **产品白底图只作为产品本体参考**，白底背景不会被带入场景（提示词中已强制约束）。
6. **不要用本 Skill 复刻他人商标、真人身份或受版权保护的画面做商用冒充**。
7. **图像模型无法保证 100% 不变形**。产品 logo、细小文字、复杂结构仍是风险点——这是模型能力边界，不是流程缺陷。

### 已知限制

| 限制 | 影响 | 缓解 |
|---|---|---|
| 单张宫格上限 12 格 | 镜头数 >12 时无法一次出图 | 拆多轮 run 后二次拼接 |
| 无音频时口播推断降级 | 字幕节奏变弱 | 提供带字幕的参考视频 |
| 场景切变阈值需按素材调 | 快剪视频可能漏帧 | 调低 `scene_threshold`（0.2–0.35） |
| 出图模型逐格一致性 | 产品/人物可能轻微漂移 | 优先选一致性强的模型；配合自动质检修正 |
| 质检依赖多模态模型判断 | 属主观项，非像素级判定 | `final_quality_check.json` 保留人工复核入口 |
| 理解层模型能力差异 | 弱模型的 JSON 遵从度不稳 | 已内置 2 次重试 + 校验 + 规则兜底；建议选指令遵循强的多模态模型 |

---

## 九、目录结构

```text
FantuiDB/
├── SKILL.md                  # Agent 技能定义（核心契约）
├── README.md                 # 本文件
├── config.json               # 运行配置
├── .env.example              # 环境变量模板（复制为 .env）
├── requirements.txt
├── copy_results.py           # 产物导出
├── cleanup_preview.ps1       # 中间产物清理（仅移回收站）
├── scripts/
│   ├── run.py                        # 主流水线（阶段 A / B / all）
│   ├── extract_candidate_frames.py   # 双路抽帧
│   ├── stitch_grid.py                # 6/9/12 宫格拼接
│   ├── export_excel_csv.py           # 分镜 → CSV
│   ├── extract_image2_prompt.py      # 提取最终出图 Prompt
│   ├── workflow_helpers.py           # 选帧校验、兜底、contact sheet
│   ├── utils.py                      # FFmpeg 定位、视频探测、通用工具
│   └── providers/
│       ├── base.py                   # ★ ImageProvider 出图契约
│       ├── llm_client.py             # ★ 理解层：通用大模型客户端（厂商无关）
│       ├── __init__.py               # provider 注册表与工厂
│       ├── doubao_client.py          # 兼容模块（历史文件名，等价于 llm_client）
│       ├── image2_client.py          # 出图参考实现 · Image2
│       ├── gpt_image_client.py       # 出图参考实现 · GPT-Image
│       └── nano_banana_client.py     # 出图参考实现 · 香蕉 Nano Banana
├── prompts/                  # 5 个核心提示词（反推断/选帧/产品/替换/表格）
├── schemas/                  # 4 个 JSON Schema
├── docs/
│   ├── principles.md         # 技术原理详解
│   ├── usage.md              # 使用方法与 Agent 适配
│   ├── image_models.md       # 主流生图模式注意事项
│   ├── dependencies.md       # 插件与环境依赖
│   ├── api_integration.md    # API 接入说明
│   ├── workflow_steps.md     # 步骤清单
│   ├── local_run_commands.md # 本机运行命令
│   ├── n8n_nodes.md          # n8n 节点蓝图
│   └── quality_checklist.md  # 质检清单
├── templates/                # 交互回复模板
├── examples/                 # 输入/输出样例
└── n8n/                      # 工作流蓝图
```

---

## 十、文档索引

| 文档 | 内容 |
|---|---|
| [技术原理](docs/principles.md) | 第一性原理、四层拆解、双路抽帧、反推断、质检闭环、数据结构 |
| [使用方法](docs/usage.md) | 各主流 Agent 接入、三种运行模式、参数调优、故障排查 |
| [主流生图模式注意事项](docs/image_models.md) | 内置参考实现对比、其他模型接入方式、参数、踩坑、Prompt 技巧 |
| [插件与环境依赖](docs/dependencies.md) | 依赖清单、环境变量全表、安装步骤、常见报错 |
| [API 接入说明](docs/api_integration.md) | 理解层与出图层的请求/响应结构与调试方式 |
| [n8n 节点蓝图](docs/n8n_nodes.md) | 节点工作流与 Webhook 拆分方案 |

---

## 免责声明

本项目仅用于**电商创意分镜的结构分析与自有产品素材生成**。使用者须自行确保：

- 对上传的参考视频拥有合法使用权；
- 不将输出用于复刻他人商标、真人身份或受版权保护的画面做商业冒充；
- 遵守所在地区关于 AI 生成内容标识的法律法规，并按投放平台要求标注 AI 生成内容。

---

## License

[MIT](LICENSE)
