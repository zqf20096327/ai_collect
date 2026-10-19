# ReelAgent

> 一句话：把剧本变成短剧。多 LLM 协同、7 阶段全自动 Pipeline、自由对话式 Agent。

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/tests-60%20passed-brightgreen.svg)](./tests)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 演示（Web 前端）

> 一段视频看懂前端能干什么：新建任务、跑 Pipeline、分镜/视频预览、审核批注、在线剪辑重拼。

https://github.com/user-attachments/assets/36b49224-227f-4453-bbc8-a0ef5994a612

---

## 它能做什么

输入一份剧本（txt/docx）或一张参考图，自动产出分集短剧成片或单图小视频：

- **智能摄取**：解析剧本 → 分集 + 角色注册表 + 场景表
- **角色/场景生图**：多风格底图 + 服装变体 + 场景图
- **逐镜分镜**：每集 shot 级视频 prompt，一次请求闭环
- **AI 视频生成**：Seedance 2.0 图生视频
- **BGM 生成**：MiniMax 音乐按情绪分组
- **ffmpeg 拼装**：视频 + BGM 混音输出 mp4
- **AI 审核**：成片自动挑硬伤，支持 shot 级重生修复
- **Clip Mode**：单张参考图直出带原生对白的短视频片段
- **自由对话 Agent**：`reel` 终端里直接聊，自动识图、自动调用工具

Pipeline 是引擎，Agent 是自动驾驶——前者保证稳定产出，后者负责听懂人话并编排。

---

## 快速开始

```bash
# 1. 安装
pip install -e .

# 2. 配置（可选；AGNES 内置免费 key，可零配置先用）
cp .env.example .env
# 编辑 .env，填入 CLAUDE_API_KEY / KIMI_API_KEY / DEEPSEEK_API_KEY 等

# 3. 启动交互终端
reel
```

首次启动会引导选择默认 LLM：

```text
🎬 ReelAgent
首次使用，请选择 LLM 模型：
  1. AGNES 2.0 Flash（免费，推荐先用）
  2. Claude Opus 4.7
  3. DeepSeek V4
  4. Kimi K2.6
> 1
已选择：agnes
```

---

## Web 前端（可视化操作台）

浏览器里完成新建任务、跑 Pipeline、分镜/视频预览、审核批注、在线剪辑重拼、画风/提示词/密钥管理，全程无需碰命令行。

### 环境要求

- Python 3.10+（后端 FastAPI，已随 `pip install -e .` 装好）
- Node.js 18+ 与 npm（前端构建）

### 一键启动（推荐）

`run.py` 会自动安装前端依赖 + 构建 + 起服务 + 开浏览器，API 和页面同端口：

```bash
python run.py                # 首次自动 npm install + 构建，默认 http://127.0.0.1:7788
python run.py --build        # 强制重新构建前端
python run.py --port 9000    # 自定义端口
```

### 开发模式（前端热更新 HMR）

前后端分离：后端 7788，前端 Vite dev server 5173（自动代理 `/api`、`/media` 到后端）：

```bash
python run.py --dev          # 一条命令同时起后端 + vite HMR，浏览器开 http://localhost:5173
```

### 手动安装 / 启动前端依赖

若想单独操作前端（例如只装依赖或只跑构建）：

```bash
cd web
npm install                  # 安装前端依赖
npm run dev                  # 开发模式（需另起后端：uvicorn server:app --port 7788）
npm run build                # 构建到 web/dist（供 run.py 生产模式托管）
npm run preview              # 本地预览构建产物
```

后端可单独启动：`uvicorn server:app --reload --port 7788`。

### 前端功能一览

| 页面 | 作用 |
|------|------|
| Dashboard | 任务列表、状态总览、新建入口 |
| 新建任务 | 上传/粘贴剧本，选画风、LLM/生图供应商、分辨率/比例 |
| 任务详情 | 7 阶段时间轴 + 逐阶段视图（摄取/生图/分镜/视频/BGM/成片/审核） |
| 在线剪辑 | 逐镜设入出点、单镜重生、非破坏重拼产出 `edited.mp4` |
| 审核批注 | AI 审核清单 + 人工时间轴批注（增删改） |
| 画风库 | 在线编辑 `styleconfig.json`（自动备份 / 一键回退） |
| 提示词 | 在线编辑 `sys-prompt/*.md`（自动备份 / 一键回退） |
| 设置 | 读写 `.env` 密钥（Key 打码显示） |

技术栈：React 18 + Vite + TypeScript + Tailwind + shadcn/Radix UI；后端 FastAPI，用 SSE 推送 Pipeline 进度与 Agent 流式对话。

---

## REPL 自由对话（推荐日常用）

安装后输入 `reel` 进入自然语言控制台：

```text
> 帮我做一个韩漫风格的霸总短剧
> 剧本在 story.docx
> 用 C:\ReelAgent\TEST.png 做一段 16:9 小视频，女人说"老公..."
> 只跑 stage 1 摄取剧本
> 把第 2 集的视频重跑一下
> 审核一下并自动修复
> 看下状态
> /open
> /exit
```

### 当前 Agent 能力

- **自然语言理解**：闲聊、脑暴、跑 Pipeline、查状态、改配置都能听懂。
- **自动识图**：消息里带上图片路径（如 `C:\ReelAgent\TEST.png`），Agent 会自动调用 `analyze_image` 分析并基于结果回复。
- **ReAct 工具调用**：需要操作时自动输出 JSON 调用工具，观察结果后再决定下一步。
- **流式输出**：最终回复逐字实时打印到终端。
- **技能注入**：`sys-prompt/*.md` 会根据对话主题动态注入到系统提示里（如 clip、角色、场景、分镜等）。
- **会话记忆**：`~/.reelagent/session.json` 保存当前任务、模型、风格、最近 50 轮历史，重启后自动续上。

### 内置命令

| 命令 | 作用 |
|------|------|
| `/status` | 查看当前任务状态 |
| `/tasks` | 最近任务列表 |
| `/config style 韩漫` | 修改默认风格 |
| `/config model agnes` | 修改默认模型 |
| `/model` | 快速查看/切换模型 |
| `/open` | 打开当前任务输出目录 |
| `/help` | 帮助 |
| `/exit` | 退出 |

---

## 命令参考

### pipeline.py（专家模式）

```bash
python pipeline.py --scene <任务ID> [选项]
```

| 参数 | 必填 | 默认 | 说明 |
|------|:--:|------|------|
| `--scene` | ✅ | — | 任务 ID，产物落 `output/<id>/` |
| `--script` | * | — | 剧本 .docx / .txt（Stage1 需要） |
| `--style` | | styleconfig 默认 | 画风名，如 `韩漫` `赛博朋克` `吉卜力` |
| `--stages` | | `1,2,3,4,5,6` | 阶段，逗号分隔。7=AI 审核 |
| `--llm-provider` | | `.env` | `claude` / `deepseek` / `kimi` / `agnes` |
| `--image-provider` | | `.env` | `gemini` / `gpt-image-2` |
| `--image-model` | | styleconfig | 覆盖生图模型 |
| `--video-model` | | styleconfig | 覆盖视频模型 |
| `--workers` | | `200` | 生图/视频并发上限 |
| `--force` | | 关 | 强制重做所选阶段 |
| `--polish` | | 关 | Stage1 前润色剧本 |
| `--review` | | 关 | Stage6 后 AI 审核成片 |
| `--auto-fix` | | 关 | 审核后自动重生问题 shot |

> \*Stage1 需要 `--script`，纯跑 Stage4~7 不需要。

### agent.py / `reel`（自然语言 / 交互模式）

```bash
# 非交互自然语言
python agent.py --ask "把我新传的都市爱情剧本做成韩漫风格短剧，跑完审核一下"

# 终端交互（推荐）
reel
```

| 参数 | 必填 | 默认 | 说明 |
|------|:--:|------|------|
| `--ask` | * | — | 自然语言指令 |
| `--task` | * | — | 任务 ID（与 `--ask` 二选一） |
| `--script` | | — | 剧本文件 |
| `--style` | | `韩漫` / 偏好记忆 | 画风名 |
| `--llm-provider` | | `.env` | `claude` / `deepseek` / `kimi` / `agnes` |
| `--image-provider` | | `.env` | `gemini` / `gpt-image-2` |
| `--stages` | | `1,2,3,4,5,6` | 阶段范围 |
| `--workers` | | `50` / 偏好记忆 | 并发数 |
| `--force` | | 关 | 强制重做所选阶段 |
| `--polish` | | 关 | Stage1 前润色剧本 |
| `--review` | | 关 | Stage6 后 AI 审核成片 |
| `--auto-fix` | | 关 | 审核后自动重生问题 shot |
| `--reference-image` | | — | Clip Mode 外部参考图路径 |
| `--video-ratio` | | — | 视频比例 `16:9` / `9:16` / `1:1` |
| `--video-resolution` | | — | 分辨率 `480p` / `720p` / `1080p` |
| `--video-duration` | | — | 视频时长（秒） |
| `--video-prompt` | | — | 片段镜头描述 |
| `--preserve-style` | | 关 | 保持参考图原风格 |
| `--dialogue` | | — | 对白 JSON，如 `[{"speaker":"女人","text":"老公..."}]` |
| `--choices` | | — | 选项列表 JSON 或 `\|` 分隔 |

> \* `--task` 与 `--ask` 至少提供一个。

---

## 7 个 Stage

| # | 名称 | 输入 | 输出 |
|---|------|------|------|
| 1 | 摄取 | 剧本 .docx/.txt | 分集 + 角色 + 场景注册表 |
| 2 | 生图 | 注册表 | 角色底图 + 服装变体 + 场景图 |
| 3 | 分镜 | 注册表 + 图片 | shot 级 video prompt |
| 4 | 视频 | prompt + 参考图 | Seedance 视频片段 |
| 5 | BGM | shot 分组 | MiniMax 背景音乐 |
| 6 | 拼装 | 视频 + BGM | ffmpeg 成片 .mp4 |
| 7 | 审核 | 成片 | AI 硬伤清单 → control.json |

---

## Clip Mode：单图直出小视频

用一张外部参考图直接生成带原生对白的短视频片段，无需完整剧本：

```bash
python agent.py --ask "用 C:\ReelAgent\TEST.png 做一段 16:9 的小视频，保持原图风格，女人说\"老公...\"，男人说\"别走\"，最后弹出选项 A.来吧宝贝 B.我想起来还有工作"
```

- 参考图默认作为角色底图复用
- 对白按 `角色名(音色) {中文台词}` 格式直接写进 Seedance video_prompt，由模型原生生成口型/对白
- 不再默认 ffmpeg 后期烧字幕（`burn_subtitles` 仍作为可选工具保留）

---

## 常用示例

```bash
# 全流程
python pipeline.py --scene my --script story.docx --style 韩漫 --stages 1,2,3,4,5,6

# 只跑视频+拼装+审核
python pipeline.py --scene my --stages 4,5,6,7 --review

# 重跑分镜
python pipeline.py --scene my --stages 3 --force

# 润色粗糙剧本
python pipeline.py --scene my --script rough.txt --polish --style 赛博朋克

# Agent 全自动
python agent.py --task my --script story.docx --style 韩漫

# 自然语言全自动
python agent.py --ask "把我新传的剧本做成韩漫风格短剧"

# 只重跑视频
python agent.py --ask "重跑 my 的视频"

# 审核并自动修复
python agent.py --task my --ask "审核一下，有问题自动修"

# 查看状态
python agent.py --task my --ask "看下状态"

# 终端交互
reel

# Clip Mode
python agent.py --ask "用 C:\\ReelAgent\\TEST.png 做一段 16:9 小视频，保持原图风格，女人说\"老公...\""

# 免费全自动（AGNES 零配置）
python agent.py --task my --script story.docx --llm-provider agnes
```

---

## LLM / 生图 / 视频 / BGM 供应商

| 类型 | Provider | 说明 |
|------|----------|------|
| LLM | **Claude** Opus 4.7 | 原生多模态，长上下文 |
| | **DeepSeek** V4 | 纯文本高性价比，需 AGNES 识图桥 |
| | **Kimi** K2.6 | 原生多模态，OpenAI 兼容 |
| | **AGNES** 2.0 Flash | 内置免费 key，零配置启动 |
| 生图 | **Gemini** 3.1 Flash | Google 官方 |
| | **GPT-image-2** | OpenAI 生图/编辑 |
| 视频 | **Seedance** 2.0 | 火山引擎 Ark |
| BGM | **MiniMax** Music 2.6 | 按情绪分组生成 |

`*_BASE_URL` / `*_MODEL` 均可从 `.env` 覆盖，支持三方代理。

---

## 风格库

配置在 `styleconfig.json`，当前内置：韩漫、美漫、日漫、美式厚涂、维多利亚 2D、3D 皮克斯、爱死机、古风 3D、赛博朋克、吉卜力、2D 像素等，可自行增删。

---

## 项目结构

```
ReelAgent/
├── pipeline.py          # 7 Stage 生产引擎 + LLM/生图/视频客户端封装
├── reelagent/           # 新 Agent 实现
│   ├── agent.py         # ReelAgent 主类（ReAct + 流式 + 识图）
│   ├── intent.py        # 自然语言意图解析器
│   ├── planner.py       # 执行计划器（DAG）
│   ├── executor.py      # ReAct 执行引擎 + Tool Registry 桥接
│   ├── tools.py         # Tool Registry 与本地工具实现
│   ├── skills.py        # sys-prompt/*.md 作为 skill 动态注入
│   ├── review_loop.py   # 审核→重生闭环
│   ├── prefs.py         # 用户偏好记忆
│   ├── report.py        # 结构化报告
│   └── repl.py          # 终端自然语言交互 REPL
├── agent_state.py       # AgentState / Tool / ToolStatus
├── agent_core.py        # 兼容层
├── agent.py             # Agent CLI 入口
├── server.py            # FastAPI 后端（任务/Pipeline/Agent/审核/剪辑 API，SSE）
├── run.py               # Web 一键启动（构建前端 + 起服务 + 开浏览器）
├── web/                 # Web 前端（React + Vite + TS + Tailwind + shadcn）
│   ├── src/pages/       # Dashboard / 新建任务 / 任务详情 / 画风 / 提示词 / 设置
│   ├── src/views/       # 摄取/生图/分镜/视频/BGM/成片/剪辑/审核 视图
│   ├── src/api/         # 后端 API 封装
│   └── dist/            # 构建产物（生产模式由 server.py 托管）
├── ai_review.py         # AI 审核
├── styleconfig.json     # 画风库
├── sys-prompt/          # 提示词工程（skill）
├── tests/               # 单元测试（60 passed）
├── .env.example
├── pyproject.toml
└── requirements.txt
```

---

## 记忆系统

| 位置 | 作用 | 说明 |
|------|------|------|
| `~/.reelagent/prefs.json` | 用户偏好 | 默认风格、模型、并发数、recent_tasks |
| `~/.reelagent/session.json` | REPL 会话 | 当前 task_id、模型、风格、最近 50 轮对话 |
| `output/<task_id>/control.json` | 任务数据 | 剧本、角色、场景、episodes、shots、状态 |
| `reelagent/agent.py` 内 `_image_analysis_cache` | 图片分析缓存 | 同一张图同 mtime 不重复调用 LLM |

---

## 设计要点

- **自研 Agent 框架**：没有使用 LangChain / AutoGen / LlamaIndex，直接基于 ReAct + Tool Registry 实现。
- **脏标记级联**：上游修改自动标记下游阶段失效。
- **多供应商工厂**：LLM / 生图 / 视频 / BGM 统一接口。
- **幂等续写**：中断后从断点恢复。
- **审核闭环**：AI 逐镜审核 + shot 级重生。
- **供应商可观测**：每个 shot 记录 task_id / request_id / errors。
- **Windows 适配**：ffmpeg 路径转义、surrogate 编码清理等针对 Windows 终端做了处理。

---

## Roadmap / TODO

- [x] 开发 Web 前端页面，支持可视化剧本编辑、分镜预览、审核批注、在线剪辑
- [ ] 兼容 Claude Code、Cursor、Windsurf 等主流 Agent 编辑器的调用规范
- [ ] 多角色/多场景一致性与角色锁定优化
- [ ] 视频生成失败自动重试与异地容灾
- [ ] 更细粒度的成本/耗时统计面板

---

## License

MIT
