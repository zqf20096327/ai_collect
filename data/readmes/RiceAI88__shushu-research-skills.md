# 科研鼠鼠 · Skills 导航站

**简体中文** · **[English (README_EN.md)](README_EN.md)**

**面向大学生和研究生，按专业找到适合自己的科研 Skills。**

**科研鼠鼠 · Skills 导航站**（`shushu-research-skills`）由 RiceAI88 整理维护，汇集 GitHub 上用于文献检索、论文阅读、写作、绘图、实验复现、投稿审稿、数据分析和研究计算的 Agent Skills。支持按 12 个学科门类与具体专业、8 类科研任务和适用 AI Agent 筛选，提供中文一句话导读、3 步快速上手指引（标注终端或 AI Agent 对话框执行位置、一键复制安装与双语提示词案例）、10 条专业科研路径与维护状态参考。科研相关工具、工作流与学习资料单独标注。

### [打开科研 Skills 导航 →](https://riceai985.cc/)

[![Skills](https://img.shields.io/badge/Skills-502-0d9f6e)](#skills-榜单)
[![Updated](https://img.shields.io/badge/updated-2026--11--27-64748b)](#收录与更新)
[![CI](https://github.com/RiceAI88/shushu-research-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/RiceAI88/shushu-research-skills/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-64748b)](LICENSE)

[按专业找](#按专业找-skills) · [按任务找](#按科研任务找-skills) · [新手入门](#网站怎么用) · [今日新增](#今日新增-skills) · [Skills 榜单](#skills-榜单) · [科研相关项目](#科研相关项目) · [收录与更新](#收录与更新) · [推荐项目](CONTRIBUTING.md) · [English](README_EN.md)

[![科研 Skills 导航：专业分类、科研任务与项目安装入口](assets/readme-dashboard.png)](https://riceai985.cc/)

*专业筛选界面示例；图片中的数量仅代表截图时的数据，最新结果以网站为准。*

觉得有帮助，欢迎点一个 Star 🌟；有好用的 Skills，也欢迎[提交推荐](https://github.com/RiceAI88/shushu-research-skills/issues/new?template=recommend-repo.yml)。

## 按专业找 Skills

先选择学科门类，再选择具体专业和你想完成的科研任务：

[理学](https://riceai985.cc/#discipline=science) · [工学](https://riceai985.cc/#discipline=engineering) · [医学](https://riceai985.cc/#discipline=medicine) · [农学](https://riceai985.cc/#discipline=agriculture) · [经济学](https://riceai985.cc/#discipline=economics) · [管理学](https://riceai985.cc/#discipline=management)

[法学](https://riceai985.cc/#discipline=law) · [文学](https://riceai985.cc/#discipline=literature) · [历史学](https://riceai985.cc/#discipline=history) · [哲学](https://riceai985.cc/#discipline=philosophy) · [教育学](https://riceai985.cc/#discipline=education) · [艺术学](https://riceai985.cc/#discipline=arts)

专业归属依据官方文档（目前已覆盖 160+ 个项目的专业档案，全站 Skills 100% 配备中文导读，持续补充中）；尚未核验专业归属的项目可在“全部”中浏览。选择学科门类后可直观查看各门类数量，并通过栏内“包含通用”开关或工具栏“收录范围”决定是否合并展示跨专业通用 Skills 及科研相关项目。

## 按科研任务找 Skills

| 你想做什么 | 从这里开始 |
|---|---|
| 查找论文、检索参考文献 | [找文献](https://riceai985.cc/#task=find) |
| 阅读、总结或翻译论文 | [读论文](https://riceai985.cc/#task=read) |
| 整理写作思路、修改表达、处理 LaTeX | [写论文](https://riceai985.cc/#task=write) |
| 制作论文配图、图表和科研示意图 | [科研绘图](https://riceai985.cc/#task=figures) |
| 复现实验、运行评估与基准测试 | [实验复现](https://riceai985.cc/#task=reproduce) |
| 准备投稿、审稿与返修回复 | [投稿审稿](https://riceai985.cc/#task=review) |
| 数据处理、统计分析与计量研究 | [数据分析](https://riceai985.cc/#task=analyze) |
| 数值计算、仿真与数学建模 | [研究计算](https://riceai985.cc/#task=compute) |

一个项目可以用于多个场景。网站默认只展示有 `SKILL.md` 文件证据的 Skills；需要科研工具或学习资料时，可在“收录范围”中打开“含科研相关项目”。

## 网站怎么用

- **第一次接触 Skill**：先点网站首屏的“30 秒看懂 Skill”，了解 Skill 是什么、需要搭配哪些 AI Agent（如 Claude Code、Codex、Cursor、Antigravity 等）；没装命令行工具的同学也可查看“在网页版 DeepSeek / Kimi / ChatGPT 直接用”的零门槛方法。
- **论文阶段急救速配**：支持一键切换“本科毕设起步 / 开题文献综述 / 顶刊配图流程图 / 问卷与实证计量 / 组会 PPT 与海报 / 润色改写与返修” 6 大高频场景，解决多项目选择困难。
- **按专业和任务查找**：选择学科门类、具体专业与科研任务，支持中文意图词搜索（如“润色”“降重”“画流程图”“跑实验”“计量”），并可按专业适用优先、Stars、上升最快或最新收录排序。
- **沿专业路径上手**：首屏“专业科研路径”或工具栏“专业路径”提供覆盖理工农医、经管法、人文社科的 10 条串联科研路径，列出每一步的工具、环境、依赖与安装来源，按需选用不必全部安装。
- **3 步快速上手与门槛提示**：点击卡片打开详情，顶部直观标出环境门槛小标签（如纯规则文档、需本地 Python、需 GPU、自备外部 API Key），并按“准备环境 → 安装 Skill（区分终端与对话框执行，附‘让 AI 帮你装’与网页版 AI 引导词）→ 复制双语科研提示词开用”三步上手；已核对项目提供官方文档来源与核对记录，文档核对不等于已执行安装或运行实测。
- **筛选适用 AI Agent**：按 Claude Code、Codex、Antigravity、Cursor、OpenClaw、MCP 等适用 AI Agent 筛选；不同项目支持的客户端不同，安装前以官方文档为准。
- **发现新项目**：查看“今日新增”，也可按近 7 日增长、趋势或最近更新排序。
- **收藏、对比与同门分享**：收藏感兴趣的项目后，可一键生成“课题组专属收藏清单（`#pack=...`）”或单项目微信群/小红书安利文案发给同门，对方打开即可一键收入收藏；收藏保存在当前浏览器。
- **观察趋势**：切换到“数据洞察”，查看专业分布、专业与场景覆盖及内容缺口；展开更多图表可看 Stars 增长与规模比较，筛选条件与榜单联动。
- **分享与订阅**：复制当前筛选链接，或使用 [RSS](feed.xml)、[月报](reports/)、[JSON](data/rankings.json) 和 [CSV](data/rankings.csv)。

## 今日新增 Skills

新增 Skills **14** · 按本次更新时间所在的北京时间自然日统计 · “新增”指本站首次收录，不是仓库刚创建。

- **[zhou2030109-glitch/Remit](https://github.com/zhou2030109-glitch/Remit)** — 数模Agent（数模 Agent）/ 数学建模 AI 助手：多智能体协作完成题意分析、文献检索、建模、代码执行与论文写作，支持人工审核和断点恢复。Local-first mult…
- **[optpku/ReasBook](https://github.com/optpku/ReasBook)** — Formalized mathematics from textbooks and research papers in Lean 4.
- **[CacinieP/TeXada-Studio-with-agentskills](https://github.com/CacinieP/TeXada-Studio-with-agentskills)** — 本地 LaTeX 工作台：源码/PDF 双栏、图片识别、保真语法修复、AgentSkills 与人工审阅 · AGPL-3.0-only
- **[nanless/audio-research-workbench](https://github.com/nanless/audio-research-workbench)** — 仓库未提供简介
- **[rspace-os/rspace-web](https://github.com/rspace-os/rspace-web)** — This the main repository for RSpace: rspace-web. Check https://github.com/rspace-os/rspac…

[查看网站今日新增](https://riceai985.cc/#today=skill) · 本节最多展示 5 个，完整列表见网站。初始导入的基线项目不计为今日新增。

## Skills 榜单

Skills **502** · 科研相关项目 **291** · 类型待核验 **2**

更新时间：**2026-11-27 14:39 UTC+8**。以下为 Skills 前 20 名，按 Stars 降序排列；同 Stars 时依次按趋势分和仓库名排序，筛选项目类型后重新编号。Stars 与增长反映关注度，不代表科研质量、安装兼容性或推荐保证。

| # | 仓库 | Stars | 近 7 日 | 适用 AI Agent | 作者原文简介 |
|---:|---|---:|---:|---|---|
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 58,734 | +950 | Claude Code | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 2 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 58,610 | +743 | Claude Code/Codex/Cursor/Antigravity | Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by… |
| 3 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | 55,232 | +986 | Codex | 符合nature论文学术表达和科研绘图的Skill |
| 4 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 19,979 | +492 | Claude Code/Codex/MCP | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML res… |
| 5 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | 15,149 | +340 | Codex | Codex-native Academic Research Skills suite for human-in-the-loop academic research workf… |
| 6 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 14,958 | +2 | Claude Code/Codex/OpenCode/Gemini | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| 7 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | 14,852 | +161 | Claude Code/Codex/Gemini | Comprehensive open-source library of AI research and engineering skills for any AI model.… |
| 8 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | 13,719 | +705 | Claude Code/Cursor/Codex | 将博导十年科研经验炼化为可直接调用的 AI 技能。从 Idea 构思到论文投稿，你的 AI 科研副导师。 |
| 9 | [ChenLiu-1996/figures4papers](https://github.com/ChenLiu-1996/figures4papers) | 12,578 | +276 | Cursor/Claude Code/Codex | My Python scripts to make high-quality figures for publications in top AI conferences and… |
| 10 | [Companion-Inc/feynman](https://github.com/Companion-Inc/feynman) | 10,156 | — | Codex/OpenCode/MCP | The open source AI research agent. |
| 11 | [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab) | 8,732 | +44 | 平台见说明 | Unified framework for robot learning with multi-physics/renderer support |
| 12 | [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills) | 8,617 | +170 | Claude Code/Codex/Gemini | Skill package for ML/CV/NLP paper writing, curated and adapted from Prof. Peng Sida's ope… |
| 13 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | 8,209 | +148 | Claude Code/Codex | GPT-Image-2 PPT Generator Skill for Creating Image-Based PowerPoint Presentations in Code… |
| 14 | [ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills) | 8,104 | +1,315 | Claude Code/Codex/Cursor/Gemini/Windsurf/MCP | AI agent skills for social media research. Outlier posts, comment mining, competitor tear… |
| 15 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | 7,696 | +22 | Gemini | PaperBanana: Automating Academic Illustration For AI Scientists |
| 16 | [Adkid-Zephyr/anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill) | 7,360 | +537 | Claude Code/Cursor | 极致轻量｜阻止论文的防御性写作 \| Anti-defensive writing for academic papers — 学术写作原则 Skill + prompt pack… |
| 17 | [larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts) | 7,010 | +70 | Claude Code/Codex | Data visualization Skill for AI Agents, turning data into polished, interactive HTML char… |
| 18 | [jihe520/MathModelAgent](https://github.com/jihe520/MathModelAgent) | 6,445 | +67 | Claude Code/Codex | 🤖📐专为数学建模设计的 Agent & skills ,自动完成数学建模，生成一份完整的可以直接提交的论文。 An Agent Designed for Mathematical… |
| 19 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | 6,435 | +78 | Codex | Open-source AI for Science Skill for research agents. Review literature, run analyses, ma… |
| 20 | [AIScientists-Dev/academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer) | 6,388 | +748 | Claude Code/Codex | Strip AI-writing tells from papers and grant proposals (NSF/NIH), while keeping scholarly… |

[浏览完整 Skills 榜单](https://riceai985.cc/) · 简介保留仓库作者原文，仅截短展示；“—”表示零增量或暂缺可比较的历史记录，计算方式见[排名方法](docs/methodology.md)。

## 科研相关项目

以下为科研工具、工作流和学习资料等相关项目的前 10 名，独立按 Stars 顺序展示，不混入上方 Skills 排名。

| # | 仓库 | Stars | 近 7 日 | 适用 AI Agent | 作者原文简介 |
|---:|---|---:|---:|---|---|
| 1 | [binary-husky/gpt_academic](https://github.com/binary-husky/gpt_academic) | 71,725 | +27 | 平台见说明 | 为GPT/GLM等LLM大语言模型提供实用化交互接口，特别优化论文阅读/润色/写作体验，模块化设计，支持自定义快捷按钮&函数插件，支持Python和C++等项目剖析&自译解功能，… |
| 2 | [scutan90/DeepLearning-500-questions](https://github.com/scutan90/DeepLearning-500-questions) | 57,732 | — | 平台见说明 | 深度学习500问，以问答形式对常用的概率知识、线性代数、机器学习、深度学习、计算机视觉等热点问题进行阐述，以帮助自己及有需要的读者。 全书分为18个章节，50余万字。由于水平有限… |
| 3 | [PDFMathTranslate/PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate) | 38,701 | +160 | MCP | [EMNLP 2025 Demo] PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的… |
| 4 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | 36,370 | +29 | 平台见说明 | Elevate your AI research writing, no more tedious polishing ✨ |
| 5 | [mli/paper-reading](https://github.com/mli/paper-reading) | 34,153 | +22 | 平台见说明 | 深度学习经典、新论文逐段精读 |
| 6 | [AccumulateMore/CV](https://github.com/AccumulateMore/CV) | 24,360 | +43 | 平台见说明 | ✅（已完结）超级全面的 深度学习 笔记【土堆 Pytorch】【李沐 动手学深度学习】【吴恩达 深度学习】【大飞 大模型Agent】 |
| 7 | [amusi/CVPR2026-Papers-with-Code](https://github.com/amusi/CVPR2026-Papers-with-Code) | 22,971 | +8 | 平台见说明 | CVPR 2026 论文和开源项目合集 |
| 8 | [kaixindelele/ChatPaper](https://github.com/kaixindelele/ChatPaper) | 20,034 | +16 | 平台见说明 | Use ChatGPT to summarize the arXiv papers. 全流程加速科研，利用chatgpt进行论文全文总结+专业翻译+润色+审稿+审稿回复 |
| 9 | [immersive-translate/immersive-translate](https://github.com/immersive-translate/immersive-translate) | 19,896 | +50 | 平台见说明 | 沉浸式双语网页翻译扩展 , 支持输入框翻译， 鼠标悬停翻译， PDF, Epub, 字幕文件, TXT 文件翻译 - Immersive Dual Web Page Transl… |
| 10 | [ZJU-LLMs/Foundations-of-LLMs](https://github.com/ZJU-LLMs/Foundations-of-LLMs) | 18,651 | +24 | 平台见说明 | A book for Learning the Foundations of LLMs |

[浏览科研相关项目](https://riceai985.cc/#related=1)（打开后与 Skills 合并展示）。类型待核验项目不计入两张表，待文件证据确认后再归类；有 `SKILL.md` 也不等同于已通过安装测试。

## 收录与更新

**数据从哪里来？** 使用 GitHub API 获取仓库公开信息，通过热门搜索、最近更新搜索、Stars 区间搜索和维护者推荐发现候选；新候选读取 README 核验其自身科研用途，已有项目独立复查。搜索与核验有预算和覆盖限制，不保证收齐 GitHub 上所有科研 Skills。

**哪些项目会收录？** 当前 Stars 门槛为 **30**，排除 fork、归档、自动搬运镜像及与学术研究无关的通用开发／营销工具。Skills／科研工作流与科研相关工具／学习资料采用分轨准入，读取仓库文档核验学术研究证据，并检测默认分支的 `SKILL.md` 文件后标注类型。暂时请求失败时保留此前合格项目的缓存并标记待核验，不因跌出搜索结果就直接移除。

**怎样排名？** 主榜按 Stars 排序，增长来自历史快照；趋势分仅作辅助，也可在网站切换排序。完整规则、字段含义和历史数据说明见[排名方法](docs/methodology.md)，采集过程见[采集报告](data/collection-report.json)与[变更记录](data/collection-events.json)。

**什么时候更新？** [Update rankings](https://github.com/RiceAI88/shushu-research-skills/actions/workflows/update-rankings.yml) 计划每日 **北京时间 10:00（02:00 UTC）**运行。GitHub Actions 定时任务可能排队或延迟，计划时间不等于数据发布时间，也不保证每天都有新增。运行结果见 Actions；有仓库维护权限时，可在该工作流选择 **Run workflow** 手动触发。

README 会由采集脚本自动生成，静态介绍需修改 [`render_readme`](scripts/update_rankings.py)，再用已有数据重新生成；不要只改 README 后等待下一次采集覆盖。采集会同步维护榜单、首次收录记录、近 60 天历史快照和订阅资产。

## 推荐项目与参与维护

发现遗漏或分类错误，可[提交推荐 Issue](https://github.com/RiceAI88/shushu-research-skills/issues/new?template=recommend-repo.yml)，附仓库链接、具体科研用途和 Skill／安装文档入口。也欢迎修正文档、核对安装信息、改进搜索和页面体验，详见[贡献指南](CONTRIBUTING.md)。

开发者从[前端开发文档](docs/frontend-development.md)开始；安装记录与精选维护分别见[安装核验](docs/installation-audit.md)和[精选维护说明](docs/editorial-maintenance.md)。

## English

**[Read Full English README (README_EN.md) →](README_EN.md)** · **[Open English Dashboard →](https://riceai985.cc/en/)**

**Research Hamster · Skills Directory** (`shushu-research-skills`) helps undergraduate and postgraduate students find GitHub research Skills by discipline, task and supported AI Agent, from literature search and writing to figures, data analysis and scientific computing.

[Open the dashboard](https://riceai985.cc/en/) to choose a discipline and task, read the starter guide, follow 10 discipline research paths, use the 3-step quick-start with copyable prompt examples, inspect installation requirements, save favorites, compare repositories and explore data insights. Curated summaries are paired with the repository author's original description.

Discipline labels are based on official documentation; coverage is still being expanded. General research Skills and related projects can be included through the inline toggle or scope control. The default ranking contains repositories with detected `SKILL.md` files. Research-related tools, workflows and learning materials are separately labelled and can be included with a toggle; unverified types are excluded from both previews. File detection does not certify quality or successful installation.

Candidates are discovered through popular, recently updated and star-banded searches, then reviewed against README evidence while filtering out mirrors and non-academic noise. The main ranking uses Stars; daily arrivals mean first inclusion on this site, measured by the Beijing calendar day. The scheduled daily refresh runs at 10:00 UTC+8 (02:00 UTC), may be delayed, and does not guarantee new entries every day. Search coverage is bounded.

[English README](README_EN.md) · [Methodology](docs/methodology.md) · [Contributing](CONTRIBUTING.md) · [JSON](data/rankings.json) · [CSV](data/rankings.csv) · [RSS](feed.xml)

## 来源与致谢

本项目基于 [kael-odin/awesome-academic-research-skills](https://github.com/kael-odin/awesome-academic-research-skills) 导入并进行后续改版，感谢原作者 [kael-odin](https://github.com/kael-odin) 的开源贡献。

本仓库由 RiceAI88 独立维护，已将首页迁移至 React，并增加专业分类、科研任务筛选、3 步上手指引与 10 条专业路径、项目类型区分、今日新增、项目对比、数据洞察与分轨采集核验机制。保留原项目的 MIT 许可证和版权声明；不代表原作者或与原作者存在隶属关系。早期导入的历史快照不代表本站当时已运行。

## License

[MIT](LICENSE)
