# 科研鼠鼠 · Skills 导航站

**面向大学生和研究生，按专业找到适合自己的科研 Skills。**

**科研鼠鼠 · Skills 导航站**（`shushu-research-skills`）由 RiceAI88 整理维护，汇集 GitHub 上用于文献检索、论文阅读、写作、绘图、数据分析和科研计算的 Agent Skills。支持按专业、科研任务和适用平台筛选，并提供安装入口、使用条件与维护信息。科研相关工具、工作流与资料单独标注。

### [打开科研 Skills 导航 →](https://riceai985.cc/)

[![Skills](https://img.shields.io/badge/Skills-348-0d9f6e)](#skills-榜单)
[![Updated](https://img.shields.io/badge/updated-2026--11--21-64748b)](#收录与更新)
[![CI](https://github.com/RiceAI88/shushu-research-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/RiceAI88/shushu-research-skills/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-64748b)](LICENSE)

[按专业找](#按专业找-skills) · [按任务找](#按科研任务找-skills) · [新手入门](#网站怎么用) · [今日新增](#今日新增-skills) · [Skills 榜单](#skills-榜单) · [科研相关项目](#科研相关项目) · [收录与更新](#收录与更新) · [推荐项目](CONTRIBUTING.md) · [English](#english)

[![科研 Skills 导航：专业分类、科研任务与项目安装入口](assets/readme-dashboard.png)](https://riceai985.cc/)

*专业筛选界面示例；图片中的数量仅代表截图时的数据，最新结果以网站为准。*

觉得有帮助，欢迎点一个 Star 🌟；有好用的 Skills，也欢迎[提交推荐](https://github.com/RiceAI88/shushu-research-skills/issues/new?template=recommend-repo.yml)。

## 按专业找 Skills

先选择学科门类，再选择具体专业和你想完成的科研任务：

[理学](https://riceai985.cc/#discipline=science) · [工学](https://riceai985.cc/#discipline=engineering) · [医学](https://riceai985.cc/#discipline=medicine) · [农学](https://riceai985.cc/#discipline=agriculture) · [经济学](https://riceai985.cc/#discipline=economics) · [管理学](https://riceai985.cc/#discipline=management)

[法学](https://riceai985.cc/#discipline=law) · [文学](https://riceai985.cc/#discipline=literature) · [历史学](https://riceai985.cc/#discipline=history) · [哲学](https://riceai985.cc/#discipline=philosophy) · [教育学](https://riceai985.cc/#discipline=education) · [艺术学](https://riceai985.cc/#discipline=arts)

专业归属依据官方文档，当前仍在补充；尚未核验专业归属的项目可在“全部”中浏览。选择专业后，可在“收录范围”中决定是否包含跨专业通用 Skills，以及科研相关项目。

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

一个项目可以用于多个场景。网站默认只展示有 `SKILL.md` 文件证据的 Skills；需要科研工具或资料时，可在“收录范围”中打开“含科研相关项目”。

## 网站怎么用

- **第一次接触 Skill**：先点网站首屏的“30 秒看懂 Skill”，了解 Skill 是什么、需要哪些宿主工具，以及账号、费用与依赖要求。
- **按专业和任务查找**：选择学科门类、具体专业与科研任务，再按平台、Stars、上升最快或最新收录筛选排序；“专业适用优先”是独立的排序选项。
- **沿专业路径上手**：工具栏的“专业路径”按已核对项目串联任务步骤，列出每一步的工具、环境、依赖与安装来源，不必全部安装。
- **发现新项目**：查看“今日新增”，也可按近 7 日增长、趋势或最近更新排序。
- **找到适合的平台**：搜索关键词，按 Claude Code、Codex、Antigravity、Cursor、MCP 等适用平台筛选；不同项目支持的平台不同，安装前以官方文档为准。
- **查看使用条件**：点击卡片打开详情，查看安装入口、适用任务、必要依赖与维护信息；已核对项目提供文档来源与核对记录，文档核对不等于已执行安装或运行实测。
- **收藏与对比**：收藏感兴趣的项目，加入对比后比较任务、安装方式、依赖和维护状态；收藏保存在当前浏览器。
- **观察趋势**：切换到“数据洞察”，查看专业分布、专业与场景覆盖及内容缺口；展开更多图表可看 Stars 增长与规模比较，筛选条件与榜单联动。
- **分享与订阅**：复制当前筛选链接，或使用 [RSS](feed.xml)、[月报](reports/)、[JSON](data/rankings.json) 和 [CSV](data/rankings.csv)。

## 今日新增 Skills

新增 Skills **4** · 按本次更新时间所在的北京时间自然日统计 · “新增”指本站首次收录，不是仓库刚创建。

- **[jordan-gibbs/hyperresearch](https://github.com/jordan-gibbs/hyperresearch)** — Convert Claude Code or Codex into the most intelligent Deep Research Agent. Collect, sear…
- **[Paper2Poster/Paper2Poster](https://github.com/Paper2Poster/Paper2Poster)** — [NeurIPS 2025] Open-source Multi-agent Poster Generation from Papers
- **[peacefulj/SSCI-SCI-skills](https://github.com/peacefulj/SSCI-SCI-skills)** — 100+学术book-to-skills：400+ 条可判定规则审查 + 一键成稿，支持 Windows 安装包与本地化部署
- **[scitex-ai/scitex-python](https://github.com/scitex-ai/scitex-python)** — A Python toolkit — AI for Science

[查看网站今日新增](https://riceai985.cc/#today=skill) · 本节最多展示 5 个，完整列表见网站。初始导入的基线项目不计为今日新增。

## Skills 榜单

Skills **348** · 科研相关项目 **206** · 类型待核验 **3**

更新时间：**2026-11-21 18:15 UTC+8**。以下为 Skills 前 20 名，按 Stars 降序排列；同 Stars 时依次按趋势分和仓库名排序，筛选项目类型后重新编号。Stars 与增长反映关注度，不代表科研质量、安装兼容性或推荐保证。

| # | 仓库 | Stars | 近 7 日 | 适用平台 | 作者原文简介 |
|---:|---|---:|---:|---|---|
| 1 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 57,977 | +887 | Claude Code/Codex/Cursor/Antigravity | Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by… |
| 2 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 57,930 | +1,105 | Claude Code | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 3 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | 54,400 | +922 | Codex | 符合nature论文学术表达和科研绘图的Skill |
| 4 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 19,547 | +385 | Claude Code/Codex/MCP | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML res… |
| 5 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 14,913 | — | Claude Code/Codex/OpenCode/Gemini | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| 6 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | 14,858 | +329 | Codex | Codex-native Academic Research Skills suite for human-in-the-loop academic research workf… |
| 7 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | 14,715 | +189 | Claude Code/Codex/Gemini | Comprehensive open-source library of AI research and engineering skills for any AI model.… |
| 8 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | 13,124 | +654 | Claude Code/Cursor/Codex | 将博导十年科研经验炼化为可直接调用的 AI 技能。从 Idea 构思到论文投稿，你的 AI 科研副导师。 |
| 9 | [ChenLiu-1996/figures4papers](https://github.com/ChenLiu-1996/figures4papers) | 12,340 | +1,098 | Cursor/Claude Code/Codex | My Python scripts to make high-quality figures for publications in top AI conferences and… |
| 10 | [Companion-Inc/feynman](https://github.com/Companion-Inc/feynman) | 10,143 | — | Codex/OpenCode/MCP | The open source AI research agent. |
| 11 | [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab) | 8,693 | — | 平台见说明 | Unified framework for robot learning with multi-physics/renderer support |
| 12 | [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills) | 8,469 | +137 | Claude Code/Codex/Gemini | Skill package for ML/CV/NLP paper writing, curated and adapted from Prof. Peng Sida's ope… |
| 13 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | 8,078 | — | Claude Code/Codex | GPT-Image-2 PPT Generator Skill for Creating Image-Based PowerPoint Presentations in Code… |
| 14 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | 7,675 | +39 | Gemini | PaperBanana: Automating Academic Illustration For AI Scientists |
| 15 | [larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts) | 6,951 | — | Claude Code/Codex | Data visualization Skill for AI Agents, turning data into polished, interactive HTML char… |
| 16 | [Adkid-Zephyr/anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill) | 6,938 | +746 | Claude Code/Cursor | 极致轻量｜阻止论文的防御性写作 \| Anti-defensive writing for academic papers — 学术写作原则 Skill + prompt pack… |
| 17 | [ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills) | 6,882 | +454 | Claude Code/Codex/Cursor/Gemini/Windsurf/MCP | AI agent skills for social media research. Outlier posts, comment mining, competitor tear… |
| 18 | [jihe520/MathModelAgent](https://github.com/jihe520/MathModelAgent) | 6,392 | +67 | Claude Code/Codex | 🤖📐专为数学建模设计的 Agent & skills ,自动完成数学建模，生成一份完整的可以直接提交的论文。 An Agent Designed for Mathematical… |
| 19 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | 6,369 | +75 | Codex | Open-source AI for Science Skill for research agents. Review literature, run analyses, ma… |
| 20 | [zLanqing/codex-claude-academic-skills](https://github.com/zLanqing/codex-claude-academic-skills) | 6,145 | +195 | Claude Code/Codex | 本仓库包含三个面向学术科研人员的Skills，覆盖从文献阅读、论文写作到科学计算的完整研究工作流。office-academic-skill 负责论文阅读报告与学术 PPT/Wo… |

[浏览完整 Skills 榜单](https://riceai985.cc/) · 简介保留仓库作者原文，仅截短展示；“—”表示零增量或暂缺可比较的历史记录，计算方式见[排名方法](docs/methodology.md)。

## 科研相关项目

以下为科研工具、工作流和资料等相关项目的前 10 名，独立按 Stars 顺序展示，不混入上方 Skills 排名。

| # | 仓库 | Stars | 近 7 日 | 适用平台 | 作者原文简介 |
|---:|---|---:|---:|---|---|
| 1 | [binary-husky/gpt_academic](https://github.com/binary-husky/gpt_academic) | 71,707 | +50 | 平台见说明 | 为GPT/GLM等LLM大语言模型提供实用化交互接口，特别优化论文阅读/润色/写作体验，模块化设计，支持自定义快捷按钮&函数插件，支持Python和C++等项目剖析&自译解功能，… |
| 2 | [scutan90/DeepLearning-500-questions](https://github.com/scutan90/DeepLearning-500-questions) | 57,727 | — | 平台见说明 | 深度学习500问，以问答形式对常用的概率知识、线性代数、机器学习、深度学习、计算机视觉等热点问题进行阐述，以帮助自己及有需要的读者。 全书分为18个章节，50余万字。由于水平有限… |
| 3 | [PDFMathTranslate/PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate) | 38,572 | — | MCP | [EMNLP 2025 Demo] PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的… |
| 4 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | 36,211 | — | 平台见说明 | Elevate your AI research writing, no more tedious polishing ✨ |
| 5 | [mli/paper-reading](https://github.com/mli/paper-reading) | 34,139 | +26 | 平台见说明 | 深度学习经典、新论文逐段精读 |
| 6 | [AccumulateMore/CV](https://github.com/AccumulateMore/CV) | 24,324 | +40 | 平台见说明 | ✅（已完结）超级全面的 深度学习 笔记【土堆 Pytorch】【李沐 动手学深度学习】【吴恩达 深度学习】【大飞 大模型Agent】 |
| 7 | [amusi/CVPR2026-Papers-with-Code](https://github.com/amusi/CVPR2026-Papers-with-Code) | 22,968 | +11 | 平台见说明 | CVPR 2026 论文和开源项目合集 |
| 8 | [kaixindelele/ChatPaper](https://github.com/kaixindelele/ChatPaper) | 20,018 | — | 平台见说明 | Use ChatGPT to summarize the arXiv papers. 全流程加速科研，利用chatgpt进行论文全文总结+专业翻译+润色+审稿+审稿回复 |
| 9 | [immersive-translate/immersive-translate](https://github.com/immersive-translate/immersive-translate) | 19,860 | — | 平台见说明 | 沉浸式双语网页翻译扩展 , 支持输入框翻译， 鼠标悬停翻译， PDF, Epub, 字幕文件, TXT 文件翻译 - Immersive Dual Web Page Transl… |
| 10 | [ZJU-LLMs/Foundations-of-LLMs](https://github.com/ZJU-LLMs/Foundations-of-LLMs) | 18,631 | — | 平台见说明 | A book for Learning the Foundations of LLMs |

[浏览科研相关项目](https://riceai985.cc/#related=1)（打开后与 Skills 合并展示）。类型待核验项目不计入两张表，待文件证据确认后再归类；有 `SKILL.md` 也不等同于已通过安装测试。

## 收录与更新

**数据从哪里来？** 使用 GitHub API 获取仓库公开信息，通过热门搜索、最近更新搜索、Stars 区间搜索和维护者推荐发现候选；新候选读取 README 核验其自身科研用途，已有项目独立复查。搜索与核验有预算和覆盖限制，不保证收齐 GitHub 上所有科研 Skills。

**哪些项目会收录？** 当前 Stars 门槛为 **30**，排除 fork、归档和明确无关项目。Skills／科研工作流与科研相关工具／指南采用分轨准入；检测默认分支的 `SKILL.md` 文件后标注类型。暂时请求失败时保留此前合格项目的缓存并标记待核验，不因跌出搜索结果就直接移除。

**怎样排名？** 主榜按 Stars 排序，增长来自历史快照；趋势分仅作辅助，也可在网站切换排序。完整规则、字段含义和历史数据说明见[排名方法](docs/methodology.md)，采集过程见[采集报告](data/collection-report.json)与[变更记录](data/collection-events.json)。

**什么时候更新？** [Update rankings](https://github.com/RiceAI88/shushu-research-skills/actions/workflows/update-rankings.yml) 计划每日 **北京时间 10:20（02:20 UTC）**运行。GitHub Actions 定时任务可能排队或延迟，计划时间不等于数据发布时间，也不保证每天都有新增。运行结果见 Actions；有仓库维护权限时，可在该工作流选择 **Run workflow** 手动触发。

README 会由采集脚本自动生成，静态介绍需修改 [`render_readme`](scripts/update_rankings.py)，再用已有数据重新生成；不要只改 README 后等待下一次采集覆盖。采集会同步维护榜单、首次收录记录、近 60 天历史快照和订阅资产。

## 推荐项目与参与维护

发现遗漏或分类错误，可[提交推荐 Issue](https://github.com/RiceAI88/shushu-research-skills/issues/new?template=recommend-repo.yml)，附仓库链接、具体科研用途和 Skill／安装文档入口。也欢迎修正文档、核对安装信息、改进搜索和页面体验，详见[贡献指南](CONTRIBUTING.md)。

开发者从[前端开发文档](docs/frontend-development.md)开始；安装记录与精选维护分别见[安装核验](docs/installation-audit.md)和[精选维护说明](docs/editorial-maintenance.md)。

## English

**Research Hamster · Skills Directory** (`shushu-research-skills`) helps undergraduate and postgraduate students find GitHub research Skills by discipline, task and supported platform, from literature search and writing to figures, data analysis and scientific computing.

[Open the dashboard](https://riceai985.cc/en/) to choose a discipline and task, read the starter guide, explore discipline research paths, inspect installation requirements, save favorites, compare repositories and explore data insights. Descriptions stay in the repository author's original language.

Discipline labels are based on official documentation; coverage is still being expanded. General research Skills and related projects can be included through the scope control. The default ranking contains repositories with detected `SKILL.md` files. Research-related tools, workflows and guides are separately labelled and can be included with a toggle; unverified types are excluded from both previews. File detection does not certify quality or successful installation.

Candidates are discovered through popular, recently updated and star-banded searches, then reviewed against README evidence. The main ranking uses Stars; daily arrivals mean first inclusion on this site, measured by the Beijing calendar day. The scheduled daily refresh may be delayed and does not guarantee new entries every day. Search coverage is bounded.

[Methodology](docs/methodology.md) · [Contributing](CONTRIBUTING.md) · [JSON](data/rankings.json) · [CSV](data/rankings.csv) · [RSS](feed.xml)

## 来源与致谢

本项目基于 [kael-odin/awesome-academic-research-skills](https://github.com/kael-odin/awesome-academic-research-skills) 导入并进行后续改版，感谢原作者 [kael-odin](https://github.com/kael-odin) 的开源贡献。

本仓库由 RiceAI88 独立维护，已将首页迁移至 React，并增加专业分类、科研任务筛选、入门指南与专业路径、项目类型区分、今日新增、项目对比、数据洞察与采集核验机制。保留原项目的 MIT 许可证和版权声明；不代表原作者或与原作者存在隶属关系。早期导入的历史快照不代表本站当时已运行。

## License

[MIT](LICENSE)
