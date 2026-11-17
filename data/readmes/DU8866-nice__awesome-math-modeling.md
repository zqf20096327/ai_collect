<!-- 本文件由 scripts/build_readme.py 生成，请勿直接修改。要改内容请编辑 data/tools.yaml 后重新生成。 -->

# Awesome Math Modeling · 数学建模 AI 工具与资源大全

[![Stars](https://img.shields.io/github/stars/DU8866-nice/awesome-math-modeling?style=flat-square)](https://github.com/DU8866-nice/awesome-math-modeling) [![Last commit](https://img.shields.io/github/last-commit/DU8866-nice/awesome-math-modeling?style=flat-square)](https://github.com/DU8866-nice/awesome-math-modeling/commits) [![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-lightgrey?style=flat-square)](LICENSE) [![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)

**简体中文** | [English](README.en.md)

> 数学建模竞赛（国赛 CUMCM、美赛 MCM/ICM、华为杯研赛等）的 AI Agent、Skill、论文模板、算法代码、获奖论文和求解器精选。每个项目都标注星标数和最近更新时间，数据每周自动刷新。

AI 正在改变数学建模比赛。过去半年，GitHub 上名称或描述含“数学建模”的新仓库就有 1600 多个，从一键出论文的 Agent，到只管选题的小 skill，质量参差不齐。同时，美赛、国赛、华为杯都出台了 AI 使用规定：可以用，但必须如实声明。

这份清单把能用、仍在维护的项目按用途整理好，并把各赛事的 AI 规定放在最前面，用之前先弄清楚边界。

收录 120 个项目 · 数据更新于 2026-11-16

**2027 美赛（MCM/ICM）：2027 年 1 月 28 日至 2 月 1 日（美东时间），距开赛还有 73 天。** 赛期以 [COMAP 官网](https://www.contest.comap.com/undergraduate/contests/mcm/) 为准。

## 目录

- [先看规则：比赛允许怎么用 AI](#rules)
- [怎么挑](#pick)
- [全流程 Agent 应用](#cat-agents)（7）
- [全流程 Skill（Claude Code / Codex 等）](#cat-skills)（24）
- [专项 Skill：选题、选模型、单题型、摘要](#cat-focused)（11）
- [研究生赛（华为杯）专用](#cat-gmcm)（3）
- [论文评审、自查与 AI 使用说明](#cat-review)（4）
- [论文模板（LaTeX / Typst）](#cat-templates)（9）
- [教程与资料合集](#cat-learning)（9）
- [算法与代码库](#cat-algorithms)（9）
- [真题与获奖论文](#cat-papers)（14）
- [求解器与常用库](#cat-solvers)（22）
- [研究：大模型做数学建模和运筹优化](#cat-research)（8）
- [常见问题](#faq)
- [让 Agent 帮你挑](#finder)
- [相关合集](#related)
- [参与贡献](#contributing)

<a id="rules"></a>
## 先看规则：比赛允许怎么用 AI

| 赛事 | 能不能用 | 必须交什么 | 不合规会怎样 |
|---|---|---|---|
| 美赛 MCM/ICM（[COMAP 政策](https://www.contest.comap.com/undergraduate/contests/mcm/flyer/Contest_AI_Policy.pdf)，2025 版） | 允许负责任地使用，解题不要求用 AI | 正文中标注、参考文献列出；25 页正文之后附 **Report on Use of AI Tools**（不计入页数），生成式 AI 要写出提问和完整回答 | COMAP 发现未披露的使用会采取相应处理 |
| 国赛 CUMCM（[2025 年试行规定](https://github.com/EmpyreanHYR/CUMCM-AI-Usage-Report/blob/main/%E5%85%A8%E5%9B%BD%E5%A4%A7%E5%AD%A6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8%E8%A7%84%E5%AE%9A%20.pdf)） | 可以用，但核心建模与分析必须由参赛队独立完成 | 正文相应位置标注；参考文献列出工具名称、版本、开发机构和使用日期；支撑材料附 **《AI 工具使用详情》PDF**（工具、用途和环节、关键交互记录、采纳与修改情况）。没用 AI 也要在参考文献后声明“本参赛队未使用任何 AI 工具” | 取消评奖资格 |
| 华为杯研赛（[2025 年规定](https://yjsb.zjnu.edu.cn/_upload/article/files/75/fc/43236cdd4cbfa29c3ed8006080e8/359fe3e7-2758-402c-b25d-b5a6868c5437.pdf)） | 可作辅助手段，不能替代独立思考和核心创新 | 最终文字用参赛队自己的语言表述；来源无法确认的 AI“模型”“公式”不予认可；AI 参与的数据分析结果和程序要注明工具名称、版本、开发机构和日期 | 取消评奖资格 |

> [!IMPORTANT]
> 规定每年可能调整，赛前以当届官方通知为准。国赛规定链接到的是参赛者整理仓库里收录的原文，华为杯规定链接的是高校研究生院转发的原文。

2026 年 11 月，国赛组委会发布了[部分参赛作品相似度较高的通报](https://www.mcm.edu.cn/html_cn/node/74c9193dcdfd44d026d2c3bf5f93695c.html)，具体情况见通报附件。很多队伍用同一个热门 skill 或同一套提示词时，思路和行文容易趋同，这也是本清单把“人机协作”类工具标出来的原因：关键判断留给自己。

<a id="pick"></a>
## 怎么挑

| 你的情况 | 可以先看 |
|---|---|
| 第一次参赛，想真正学会建模 | [shumo-expert](https://github.com/XiucuiGuan/shumo-expert)（只引导、不代写）、[intro-mathmodel](https://github.com/datawhalechina/intro-mathmodel)、[MathModel](https://github.com/zhanwen/MathModel) |
| 国赛队伍，想让 AI 当助手、自己拿主意 | [mathmodel-skill](https://github.com/handsomeZR-netizen/mathmodel-skill)、[modeling-workbench](https://github.com/Lucasuiii/modeling-workbench)、[cumcm-step-review](https://github.com/yuanchen-home/cumcm-step-review) |
| 美赛，要写英文论文 | [LLM-MM-Agent](https://github.com/usail-hkust/LLM-MM-Agent) 的技能包、[mathodology](https://github.com/sweetcornna/mathodology)、[LaTeX-in-ICM-MCM](https://github.com/QTH1225/LaTeX-in-ICM-MCM) 模板 |
| 不想配环境，要装好就能用的软件 | [MathModelAgent](https://github.com/jihe520/MathModelAgent) 桌面版、[HaJiMi](https://github.com/yjz211/HaJiMi-Math-Model-Agent)、[Remit](https://github.com/zhou2030109-glitch/Remit) |
| 华为杯研赛 | [Huaweibei-cool](https://github.com/siyunhao2025-beep/Huaweibei-cool)、[hwb-math-modeling-skills](https://github.com/xieyouxixi/hwb-math-modeling-skills)、[GMCMthesis](https://github.com/latexstudio/GMCMthesis) |
| 卡在选题或选模型 | [route-selection](https://github.com/y3519712124-ui/math-modeling-contest-route-selection)、[cumcm-taste](https://github.com/bydtesla1609/cumcm-taste) |
| 交卷前查漏 | [bzd-math-modeling-skills](https://github.com/BZDmathclub/bzd-math-modeling-skills)、[mathematical-modeling-review](https://github.com/landawang-star/mathematical-modeling-review)，再用 [CUMCM-AI-Usage-Report](https://github.com/EmpyreanHYR/CUMCM-AI-Usage-Report) 写 AI 使用详情 |
| 赛后想发论文 | [math-modeling-to-sci-skill](https://github.com/siyunhao2025-beep/math-modeling-to-sci-skill) |

这张表依据各项目 README 整理，没有逐个实测。

**图例**：🚀 全自动 · 🤝 人机协作（关键决策由你确认）· 🎓 引导式（不代写）· 📝 提示词合集（非标准 skill）· 🆕 近 60 天新建 · 💤 超过一年未更新（工具、模板和研究类）· 📦 已归档

> [!NOTE]
> 工作方式标签依据各项目 README 的自述，只在 README 写明时才标。“收录”指核对过仓库说明和目录结构，不等于实测过效果。skill 可能附带脚本，安装前先读一遍它的 SKILL.md。

<a id="cat-agents"></a>
## 全流程 Agent 应用

装好就能用的桌面或网页应用，把读题、建模、写代码、出图、写论文串成一条流水线。大多需要自己填大模型 API Key。

- **[MathModelAgent](https://github.com/jihe520/MathModelAgent)** · ★ 6.3k · 🚀<br>数学建模专用 Agent，自动分析问题、建模、写代码、纠错并撰写论文；桌面版内置 Claude Code 和全套 skill，填一个 API Key 即可开始。<br><sub>更新于 2026-11 · 11 个 skill</sub>
- **[LLM-MM-Agent](https://github.com/usail-hkust/LLM-MM-Agent)** · ★ 698 · 🚀<br>港科大 MM-Agent（NeurIPS 2025），把真实建模问题拆成分析、建模、求解、写作的智能体流程；新版另提供可装进 Codex、Claude Code、Cursor 的「数学建模专家」技能包。<br><sub>更新于 2026-09 · 美赛 · GPL-3.0</sub>
- **[AutoMM](https://github.com/sghwr/AutoMM)** · ★ 219 · 🚀<br>基于 DeepSeek Harness 的全自动研究流程，按小问推进理解、文献、假设、公式、计算和校验，附实时仪表盘；当前版本不写论文。<br><sub>更新于 2026-08 · 12 个 skill</sub>
- **[Beacon](https://github.com/123-qw-as/Beacon)** · ★ 174 · 🤝<br>基于 LangGraph 的多智能体流水线，面向美赛和研赛：读题、建模、写代码、出图、成文并编译 PDF，关键节点人工审核；有网页界面和命令行。<br><sub>更新于 2026-08 · 美赛 · 华为杯</sub>
- **[Remit](https://github.com/zhou2030109-glitch/Remit)** · ★ 88 · 🤝<br>Remit 数模小助手：协调、建模、代码、论文四个 Agent 像一支队伍协作，题意、方案和最终成果由你确认；本地运行，可断点恢复。<br><sub>更新于 2026-11 · MIT</sub>
- **[HaJiMi-Math-Model-Agent](https://github.com/yjz211/HaJiMi-Math-Model-Agent)** · ★ 59 · 🤝<br>本地桌面智能体，0–9 阶段的有状态工作流：冻结题目和数据、逐问建模求解、出图、LaTeX 论文，人工验收后生成代码附录、AI 使用说明和提交包。<br><sub>更新于 2026-09 · MIT</sub>
- **[MathAgent](https://github.com/zxuexingzhijie/MathAgent)** · ★ 42 · 🚀<br>基于 Spring AI Alibaba Graph 和 Vue 的建模研究系统，多智能体加代码解释器，自动构建、求解模型并输出报告。<br><sub>更新于 2025-11</sub>

<a id="cat-skills"></a>
## 全流程 Skill（Claude Code / Codex 等）

装进编程 Agent 的技能包，从读题一直覆盖到论文和提交检查。多数是标准 SKILL.md 格式，Claude Code、Codex、Trae、WorkBuddy 等支持 skill 的工具都能装。

- **[XiaoMaColtAI/math-modeling-skill](https://github.com/XiaoMaColtAI/math-modeling-skill)** · ★ 1.9k<br>建模分析 → 代码实现 → 论文撰写三阶段，可以只跑其中一段；Python 和 MATLAB 双语言，附优化、预测、评价、图论等算法资源库，产出 Word 论文。<br><sub>更新于 2026-11 · 国赛 · 美赛 · 14 个 skill</sub>
- **[MathModeling-skills](https://github.com/zhnnky329/MathModeling-skills)** · ★ 1.1k · 🤝<br>新版从“自动驾驶”改为“助手”：两道硬门由你决定，三个审计角色把关能否提交；支持 Python 与 MATLAB / 北太天元，旧的全自动版保留在 legacy 分支。<br><sub>更新于 2026-11 · 28 个 skill · MIT</sub>
- **[yushui2022/MathModel-Skill](https://github.com/yushui2022/MathModel-Skill)** · ★ 459<br>分 Lite / Flash / Standard / Pro 四档，Agent 真正运行代码、整理图表和证据后再写论文并检查，支持原生 Word 公式和 PDF 渲染检查；适配 Trae、Claude Code、Codex。<br><sub>更新于 2026-10 · 12 个 skill · MIT</sub>
- **[Lupynow/math-modeling-skills](https://github.com/Lupynow/math-modeling-skills)** · ★ 440<br>解题和写论文两个 skill，规则提炼自 150 多篇国赛一等、美赛 O/F 奖论文，含 95+ 场景的模型决策矩阵、8 本算法手册和 22 个 Python 模板。<br><sub>更新于 2026-07 · 国赛 · 美赛 · 2 个 skill · MIT</sub>
- **[mathodology](https://github.com/sweetcornna/mathodology)** · ★ 329<br>9 个技能、8 个角色加一个桌面工作台：记录实验、核对论文里的数字和图表、核验引用，附 46 类图表模板和敏感性、蒙特卡罗等 18 个实验组件。<br><sub>更新于 2026-11 · 美赛 · 国赛 · 其他赛事 · 9 个 skill · MIT</sub>
- **[handsomeZR-netizen/mathmodel-skill](https://github.com/handsomeZR-netizen/mathmodel-skill)** · ★ 305 · 🤝<br>把比赛拆成 10 个阶段和一份共享决策日志，团队只回答编号问题，随时说“看进度”；提交前检查匿名、页数和 AI 披露。<br><sub>更新于 2026-09 · 国赛 · 美赛 · 其他赛事 · 2 个 skill · MIT</sub>
- **[AutoMCM-Pro](https://github.com/RealSeaberry/AutoMCM-Pro)** · ★ 262 · 🚀<br>让 Claude Code 当“自动驾驶”、人当副驾驶的实验：读题、文献、推导、自证代码到 LaTeX 论文自动推进，人在关键节点审阅；也支持 Codex、opencode、DeepSeek Harness。<br><sub>更新于 2026-09 · 7 个 skill · MIT</sub>
- **[xuec699-sudo/math-modeling-skills](https://github.com/xuec699-sudo/math-modeling-skills)** · ★ 246 · 🚀<br>全自动和人工把关两种模式，六维选题评估、模型依赖图、五人评审团和学术诚信检查，论文里每个数字都能追溯到脚本输出。<br><sub>更新于 2026-06 · 国赛 · 美赛 · 其他赛事</sub><br><sub>💡 可切换为人工检查点模式</sub>
- **[modeling-workbench](https://github.com/Lucasuiii/modeling-workbench)** · ★ 178 · 🤝<br>七阶段工作流：候选模型先试算再定，论文数值关联代码和数据，代码改了能发现旧证据失效；三个关键节点由你审阅，交付中英文 LaTeX/PDF。<br><sub>更新于 2026-09 · 3 个 skill · MIT</sub>
- **[MathModelRun](https://github.com/chengyike20110519-create/MathModelRun)** · ★ 115<br>证据驱动的十阶段执行系统：复现实验、冻结结果、渲染论文、独立审计，适用国赛、美赛和 HiMCM。<br><sub>更新于 2026-10 · 国赛 · 美赛 · 其他赛事 · 3 个 skill · MIT</sub>
- **[Enhanced-mathmodel-Codex-skills](https://github.com/xzwwwwww/Enhanced-mathmodel-Codex-skills)** · ★ 113 · 🚀<br>Codex 全局 skill 套件，从题面推进到模型路线、实验模板、论文分块、Word 文档和最终质量报告。<br><sub>更新于 2026-05 · 9 个 skill</sub>
- **[Math-model-skills](https://github.com/WuXinbo-bo/Math-model-skills)** · ★ 112<br>Meta-model-agent：数据审计、建模、真实计算、验证、可视化、论文到提交验收的可恢复工作流，强调结果可复现、证据一致。<br><sub>更新于 2026-09 · 国赛 · 美赛 · 其他赛事 · 9 个 skill · MIT</sub>
- **[rootkiller6788/mathmodel-skill](https://github.com/rootkiller6788/mathmodel-skill)** · ★ 72 · 🤝<br>国赛、美赛、电工杯统一工作流：10 个阶段、共享决策日志、确定性脚本和独立检查，Codex 和 Claude Code 可以在同一个目录里接力。<br><sub>更新于 2026-10 · 国赛 · 美赛 · 其他赛事 · 8 个 skill · MIT</sub>
- **[MathModel-Copilot](https://github.com/Odyphus/MathModel-Copilot)** · ★ 67 · 🆕<br>面向国赛、美赛的建模助手和 skill：审题、模型比较、运行 Python、结果核验、论文辅助和团队协作。<br><sub>更新于 2026-10 · 国赛 · 美赛 · 3 个 skill · MIT</sub>
- **[math-modelCN](https://github.com/jsChen-biostat/math-modelCN)** · ★ 63<br>六步工作流、26 个 skill：赛题分析、建模、编码、科研绘图、论文和查重验收，附绘图模板画廊和算法资料库。<br><sub>更新于 2026-09 · 国赛 · 26 个 skill · MIT</sub>
- **[anticipate218/math-modeling-skill](https://github.com/anticipate218/math-modeling-skill)** · ★ 59 · 🤝<br>定位是“懂规则、懂评阅的教练”而不是自动写论文：审题选题、选模型、做检验、按规范写，提交前逐项检查会直接出局的红线。<br><sub>更新于 2026-10 · 国赛 · 华为杯 · 美赛 · MIT</sub>
- **[My-MathModeling-skills](https://github.com/capwitf/My-MathModeling-skills)** · ★ 59 · 🤝<br>14 个按需触发的 skill，需要题面、建模、代码、图表、审查或排版时再介入，整理好证据和风险后把判断交还给人。<br><sub>更新于 2026-07 · 国赛 · 14 个 skill · MIT</sub>
- **[mathmodel-studio](https://github.com/yan315598-design/mathmodel-studio)** · ★ 47<br>数模工坊：审题、建模、求解、验证和论文整理，可以从整道题开始，也可以只处理手上已有的代码或草稿；支持 Codex、Claude Code、ZCode。<br><sub>更新于 2026-09 · 4 个 skill · MIT</sub>
- **[EZ_math_model](https://github.com/woodfishhhh/EZ_math_model)** · ★ 42 · 🚀<br>固定七阶段：题目解析、建模、Python 求解、论文、质量审查和打包，一次运行输出 Markdown / Word / PDF 论文和代码包。<br><sub>更新于 2026-07 · 国赛 · 美赛 · 华为杯 · 29 个 skill · MIT</sub>
- **[dsh-ultramath](https://github.com/Andiii208/dsh-ultramath)** · ★ 42 · 🚀<br>DeepSeek Harness 插件：带工具编排的多 Agent 预设，一个预设跑通读题到审稿，附 33 篇模型库和论文模板。<br><sub>更新于 2026-08 · MIT</sub>
- **[cumcm-math-modeling-codex-skill](https://github.com/usst-yk/cumcm-math-modeling-codex-skill)** · ★ 38<br>国赛 Codex skill：拆题、查数据、建模、求解、出图、验证，最后写进 LaTeX 论文；在 Codex 里一句话就能安装。<br><sub>更新于 2026-05 · 国赛</sub>
- **[Math-Modeling-Agent-Flow](https://github.com/mantou6666/Math-Modeling-Agent-Flow)** · ★ 28<br>Solver → Paper → Finalizer → Growth 四个 skill，覆盖建模、论文、提交前检查和赛后复盘。<br><sub>更新于 2026-08 · 国赛 · 美赛 · MIT</sub>
- **[cumcm-modeling-analyst](https://github.com/zhu-hailin/cumcm-modeling-analyst)** · ★ 27 · 🤝<br>在国赛里实际用过的协作 skill，逐问确认，把题目、模型和证据整理成队友看得懂的论文和交付物。<br><sub>更新于 2026-09 · 国赛</sub>
- **[LEEHAHAHAHA/math-modeling-skill](https://github.com/LEEHAHAHAHA/math-modeling-skill)** · ★ 25<br>七阶段从读题到交付，机理模型优先，每问给 2–3 个不同方案，机器学习只做稳健性检验；附国赛 LaTeX 模板，可用于 Claude Code、Codex、WorkBuddy。<br><sub>更新于 2026-09 · 国赛 · 美赛 · 2 个 skill</sub>

<a id="cat-focused"></a>
## 专项 Skill：选题、选模型、单题型、摘要

只管一个环节的小工具，可以和上面的全流程 skill 搭配使用。

- **[cumcm-paper-hand-skill](https://github.com/Mr-potato-123/cumcm-paper-hand-skill)** · ★ 214<br>论文手：在已整理好建模和求解材料的参赛文件夹里写论文，内置获奖论文参考库和 LaTeX 模板。<br><sub>更新于 2026-08 · 国赛 · 美赛 · MIT</sub>
- **[cumcm-live-workflow-skill](https://github.com/haoxilin/cumcm-live-workflow-skill)** · ★ 185<br>经过真实国赛检验的实战手册：读题自查、出图、LaTeX、交叉审阅、填结果模板，含 2026 版 AI 使用规定和 26 条终审自查表。<br><sub>更新于 2026-09 · 国赛 · MIT</sub>
- **[cumcm-c-problem-lfs](https://github.com/liufanshan11/cumcm-c-problem-lfs)** · ★ 146<br>只做国赛 C 题：依据 2018–2025 年 C 题优秀论文和评阅规范，统计、预测、评价和优化方法优先，沿用 cumcmthesis 模板。<br><sub>更新于 2026-08 · 国赛</sub>
- **[cumcm-b-problem-lfs](https://github.com/liufanshan11/cumcm-b-problem-lfs)** · ★ 117<br>只做国赛 B 题：机理、几何、统计优先，内置摘要、总括方程组、图表设计和 25–29 页的论文节奏。<br><sub>更新于 2026-08 · 国赛</sub>
- **[math-modeling-contest-route-selection](https://github.com/y3519712124-ui/math-modeling-contest-route-selection)** · ★ 92<br>选题和路线选择：逐题比较建模路线、可行性、验证方式和推翻条件，避免一上来就套 TOPSIS、熵权法、LSTM 的同质化方案。<br><sub>更新于 2026-06 · 国赛 · 美赛 · MIT</sub>
- **[-MCM-ICM-CUMCM-100-AI-Prompts-](https://github.com/yugwl/-MCM-ICM-CUMCM-100-AI-Prompts-)** · ★ 41 · 📝<br>100 条数学建模提示词，按比赛流程分成 8 个阶段，任何聊天机器人都能用。<br><sub>更新于 2025-11 · 美赛 · 国赛</sub>
- **[math-modeling-to-sci-skill](https://github.com/siyunhao2025-beep/math-modeling-to-sci-skill)** · ★ 40<br>赛后把建模报告或竞赛论文改造成可投稿的 SCI 论文：重新界定研究问题，补基线和稳健性，核对引用和期刊匹配。<br><sub>更新于 2026-11</sub>
- **[cumcm-taste](https://github.com/bydtesla1609/cumcm-taste)** · ★ 35<br>选模型之前先做事实审查：哪些现实因素会改变结果、哪些能省略、有没有阈值或滞后效应，先出“方法准入报告”再选模型。<br><sub>更新于 2026-08 · 国赛</sub>
- **[zhengdabei-survey-report-skill](https://github.com/DDXYY189/zhengdabei-survey-report-skill)** · ★ 29 · 🆕<br>正大杯市场调查与分析大赛报告 skill：调查设计、统计方法、结论建议和提交前审查，含 AI 使用说明。<br><sub>更新于 2026-09 · 其他赛事 · MIT</sub>
- **[cumcm-abstract-writing-skill](https://github.com/jjh666888/cumcm-abstract-writing-skill)** · ★ 28<br>国赛摘要专用：写、改、评摘要，起草后再以评委视角复核事实和质量。<br><sub>更新于 2026-08 · 国赛</sub>
- **[shumo-expert](https://github.com/XiucuiGuan/shumo-expert)** · ★ 26 · 🎓<br>引导式学习：布鲁姆分层提问、苏格拉底追问、四阶段建模引导，只讲方法，不代求解、不代写代码，适合赛前训练和教学。<br><sub>更新于 2026-09 · 华为杯 · MIT</sub>

<a id="cat-gmcm"></a>
## 研究生赛（华为杯）专用

中国研究生数学建模竞赛的专用 skill，多数蒸馏了历年获奖论文。

- **[hwb-math-modeling-skills](https://github.com/xieyouxixi/hwb-math-modeling-skills)** · ★ 193<br>围绕华为杯训练场景的读题、方案设计、模型适配、章节检查和全文评审 skill；作者说明适合赛前训练、自查和复盘。<br><sub>更新于 2026-10 · 华为杯</sub><br><sub>💡 赛中能否使用以当届规则为准</sub>
- **[Huaweibei-cool](https://github.com/siyunhao2025-beep/Huaweibei-cool)** · ★ 86 · 🆕<br>以 2004–2024 年 729 篇华为杯获奖论文为底座：8 大题型原型、51 张方法卡、2022–2025 年 24 道题的赛道档案，LaTeX 和 Word 双链路。<br><sub>更新于 2026-09 · 华为杯 · 2 个 skill</sub>
- **[Auto-Modeling-Skill](https://github.com/weibu123/Auto-Modeling-Skill)** · ★ 53<br>拆题、数据审计、建模、代码、验证到 LaTeX 交付的可复现工作流，内置 338 篇优秀论文索引和 67 篇深度蒸馏的知识库。<br><sub>更新于 2026-09 · 华为杯 · MIT</sub>

<a id="cat-review"></a>
## 论文评审、自查与 AI 使用说明

交卷前用来查漏补缺。评分和获奖预测都是非官方参考。

- **[bzd-math-modeling-skills](https://github.com/BZDmathclub/bzd-math-modeling-skills)** · ★ 435<br>依据 2020–2025 年国赛评分细则和评阅流程：逐句读题、建模思路、分章节自查、格式检查、评委式评审、位次预估和高校国奖数据查询。<br><sub>更新于 2026-09 · 国赛</sub>
- **[cumcm-step-review](https://github.com/yuanchen-home/cumcm-step-review)** · ★ 316 · 🤝<br>国赛逐步审核版：问题重述、逐问建模、检验、摘要等每一部分先给方案，经你审核才写代码和正文，最后生成 AI 工具使用报告。<br><sub>更新于 2026-09 · 国赛 · 8 个 skill</sub>
- **[mathematical-modeling-review](https://github.com/landawang-star/mathematical-modeling-review)** · ★ 105<br>把赛题和论文交给它，得到逐问诊断、五维评分、修改优先级和非官方的奖项区间预测。<br><sub>更新于 2026-11 · 国赛</sub><br><sub>💡 作者限定个人非商业使用</sub>
- **[CUMCM-AI-Usage-Report](https://github.com/EmpyreanHYR/CUMCM-AI-Usage-Report)** · ★ 35 · 💤<br>国赛“AI 工具使用详情”LaTeX 模板：工具与版本、提问、回答、采纳和修改情况分框排版，附 Markdown 转 LaTeX 小工具。<br><sub>更新于 2025-09 · 国赛 · MIT</sub>

<a id="cat-templates"></a>
## 论文模板（LaTeX / Typst）

格式以当届官方通知为准，用之前先核对页数、封面和匿名要求。

- **[CUMCMThesis](https://github.com/latexstudio/CUMCMThesis)** · ★ 1.4k<br>国赛 LaTeX 论文模板，已适配 2026 年格式。<br><sub>更新于 2026-08 · 国赛</sub>
- **[GMCMthesis](https://github.com/latexstudio/GMCMthesis)** · ★ 331 · 💤<br>研究生数学建模竞赛（华为杯）LaTeX 模板（2024 版）。<br><sub>更新于 2024-09 · 华为杯</sub>
- **[LaTeX-in-ICM-MCM](https://github.com/QTH1225/LaTeX-in-ICM-MCM)** · ★ 290<br>基于 EasyMCM 的美赛 LaTeX 模板，支持多种排版样式。<br><sub>更新于 2026-10 · 美赛 · LPPL-1.3c</sub>
- **[mcmthesis](https://github.com/latexstudio-org/mcmthesis)** · ★ 194 · 💤<br>美赛 LaTeX 模板 mcmthesis。<br><sub>更新于 2024-01 · 美赛</sub>
- **[cumcm-latex-template](https://github.com/yifengchen07/cumcm-latex-template)** · ★ 115<br>针对 2026 年国赛的 LaTeX 模板。<br><sub>更新于 2026-08 · 国赛 · MIT</sub>
- **[Huawei_Cup_2026_Mathematical_Modeling_latex](https://github.com/1SPECOO/Huawei_Cup_2026_Mathematical_Modeling_latex)** · ★ 71 · 🆕<br>2026 年华为杯 LaTeX 模板，与官网 Word 要求一致。<br><sub>更新于 2026-09 · 华为杯</sub>
- **[cumcm](https://github.com/jayxin/cumcm)** · ★ 37<br>国赛 LaTeX 模板。<br><sub>更新于 2026-08 · 国赛 · LPPL-1.3c</sub>
- **[CUMCM-typst-template](https://github.com/a-kkiri/CUMCM-typst-template)** · ★ 34 · 💤<br>国赛 Typst 模板。<br><sub>更新于 2025-07 · 国赛 · Apache-2.0</sub>
- **[GMCM2026-LaTeX](https://github.com/jirouvan/GMCM2026-LaTeX)** · ★ 33 · 🆕<br>2026 年华为杯 LaTeX 模板，带完整字体和版式配置。<br><sub>更新于 2026-09 · 华为杯</sub>

<a id="cat-learning"></a>
## 教程与资料合集

入门和系统学习用。

- **[MathModel](https://github.com/zhanwen/MathModel)** · ★ 12.5k<br>星标最多的数模资料库：优秀论文、算法、LaTeX 模板、算法思维导图、参考书和 MATLAB 教程，本科和研究生赛都有。<br><sub>更新于 2025-09 · 国赛 · 美赛 · 华为杯</sub>
- **[personqianduixue/Math_Model](https://github.com/personqianduixue/Math_Model)** · ★ 5.3k<br>国赛、美赛、华为杯、MathorCup、电工杯等十多个比赛的资料和 LaTeX 模板。<br><sub>更新于 2023-12 · 国赛 · 美赛 · 华为杯 · 其他赛事</sub>
- **[intro-mathmodel](https://github.com/datawhalechina/intro-mathmodel)** · ★ 961<br>Datawhale《数学建模导论》，覆盖常用模型与算法的系统教程。<br><sub>更新于 2026-01</sub>
- **[Math-Model-and-Machine-Learning](https://github.com/QInzhengk/Math-Model-and-Machine-Learning)** · ★ 661<br>数学建模和机器学习、深度学习、大模型的笔记和资料，持续更新。<br><sub>更新于 2026-11</sub>
- **[COMAP-MCM-2026](https://github.com/GuangLun2000/COMAP-MCM-2026)** · ★ 395<br>一支美赛队开源的全套材料：论文、MATLAB/Python 代码、作图 PPT 模板、写作与协作笔记和 Word 模板。<br><sub>更新于 2026-01 · 美赛 · BSD-2-Clause</sub>
- **[math-model](https://github.com/HBdingdang/math-model)** · ★ 275<br>美赛、国赛、研赛论文和各类模型方法整理，适合入门和进阶。<br><sub>更新于 2023-09 · 国赛 · 美赛 · 华为杯</sub>
- **[WHUT_CUMCM20](https://github.com/zichuan-liu/WHUT_CUMCM20)** · ★ 172<br>武汉理工大学参赛资料：国赛、美赛、数维杯、亚太赛的论文和校内集训材料。<br><sub>更新于 2022-05 · 国赛 · 美赛 · 其他赛事 · MIT</sub>
- **[zsy0x/math_model](https://github.com/zsy0x/math_model)** · ★ 90<br>各大比赛历年优秀论文和题目，附 19 个数模比赛的时间表和学习笔记。<br><sub>更新于 2026-08 · 国赛 · 美赛 · 其他赛事</sub>
- **[MCM-ICM_Study_Resources](https://github.com/CQULeaf/MCM-ICM_Study_Resources)** · ★ 57<br>美赛备赛和比赛中用到的全部资料：论文模板、数据处理、绘图技巧和常见模型。<br><sub>更新于 2025-03 · 美赛</sub>

<a id="cat-algorithms"></a>
## 算法与代码库

常用模型的现成实现，拿来改比从零写快。

- **[Algorithms_MathModels](https://github.com/HuangCongQing/Algorithms_MathModels)** · ★ 2.5k<br>国赛、美赛常用算法的 MATLAB 实现。<br><sub>更新于 2022-12 · 国赛 · 美赛 · MIT</sub>
- **[Mathematical-Modeling](https://github.com/Lanrzip/Mathematical-Modeling)** · ★ 562<br>数学建模常见模型的 Python 实现。<br><sub>更新于 2020-07</sub>
- **[PMMAA](https://github.com/hacheyz/PMMAA)** · ★ 428<br>《Python 数学建模算法与应用》的笔记和代码，按章节整理。<br><sub>更新于 2024-08 · GPL-3.0</sub>
- **[Mathematical-Modeling-In-Python](https://github.com/RabbitWhite1/Mathematical-Modeling-In-Python)** · ★ 223<br>用 Python 重写《数学建模算法与应用》第二版的部分示例（原书用 MATLAB）。<br><sub>更新于 2020-09 · MIT</sub>
- **[Mathematical-modeling-model](https://github.com/leost123456/Mathematical-modeling-model)** · ★ 201<br>数学建模常用算法大全。<br><sub>更新于 2024-07 · GPL-3.0</sub>
- **[mathematical_modeling_python](https://github.com/ShituoMa/mathematical_modeling_python)** · ★ 174<br>数学建模导论的 Python 版本。<br><sub>更新于 2024-05</sub>
- **[mathmodeling](https://github.com/Koorye/mathmodeling)** · ★ 92<br>回归、分类、差分、聚类、时间序列、因子分析等方法的 Python 代码。<br><sub>更新于 2024-04 · GPL-2.0</sub>
- **[Mathematical-modeling-algorithm-and-Application](https://github.com/STL-CC/Mathematical-modeling-algorithm-and-Application)** · ★ 49<br>司守奎《数学建模算法与应用》案例的 Python 实现。<br><sub>更新于 2026-02</sub>
- **[FelixYuan-YF/MCM-ICM](https://github.com/FelixYuan-YF/MCM-ICM)** · ★ 34<br>美赛常用模型的 Python 实现，附历年 Outstanding 论文。<br><sub>更新于 2025-02 · 美赛 · MIT</sub>

<a id="cat-papers"></a>
## 真题与获奖论文

看获奖论文是最快的学习方法之一。引用时注明出处，不要照抄。

- **[dick20/MCM-ICM](https://github.com/dick20/MCM-ICM)** · ★ 2.3k<br>2004–2020 年美赛 O 奖论文合集。<br><sub>更新于 2025-07 · 美赛</sub>
- **[Postgraduate-Mathematical-Contest-in-Modelling2](https://github.com/zhenhua-chen1/Postgraduate-Mathematical-Contest-in-Modelling2)** · ★ 229<br>华为杯历年数据分析类题目的代码，作者曾获一等奖。<br><sub>更新于 2026-09 · 华为杯</sub>
- **[2025-MCM-ICM-Problem-C](https://github.com/Nahuyiur/2025-MCM-ICM-Problem-C)** · ★ 148<br>2025 年美赛 C 题 Outstanding 队伍的代码和论文。<br><sub>更新于 2026-09 · 美赛 · MIT</sub>
- **[MCM-ICM-2025-E-Nitrogen-Cycling-Model](https://github.com/LUKEQ420/MCM-ICM-2025-E-Nitrogen-Cycling-Model)** · ★ 109<br>2025 年美赛 E 题 Finalist：基于 Lotka-Volterra 的氮循环模型。<br><sub>更新于 2026-01 · 美赛 · MIT</sub>
- **[Mathematical_Contest_in_Modeling](https://github.com/JiahaoLiu2005/Mathematical_Contest_in_Modeling)** · ★ 104<br>国赛和美赛大数据方向赛题的代码、论文模板和比赛经验。<br><sub>更新于 2026-09 · 国赛 · 美赛</sub>
- **[cumcm-problems](https://github.com/CosmicLinks/cumcm-problems)** · ★ 97<br>1992–2025 年国赛真题汇总。<br><sub>更新于 2026-06 · 国赛</sub>
- **[2021-ICM-D-Outstanding](https://github.com/liujiyaoFDU/2021-ICM-D-Outstanding)** · ★ 97<br>2021 年美赛 D 题 O 奖论文和代码。<br><sub>更新于 2022-02 · 美赛</sub>
- **[24ICM_E_O_Award_Paper_code](https://github.com/ydchen0806/24ICM_E_O_Award_Paper_code)** · ★ 89<br>2024 年美赛 E 题 O 奖（INFORMS 冠名奖）论文和代码。<br><sub>更新于 2024-07 · 美赛</sub>
- **[CUMCM2020-Desert-Game](https://github.com/seanys/CUMCM2020-Desert-Game)** · ★ 76<br>2020 年国赛 B 题“沙漠游戏”全国一等奖论文、源码和 LaTeX。<br><sub>更新于 2020-12 · 国赛</sub>
- **[CUMCM-Paper-And-SourceCode](https://github.com/yan-fanyu/CUMCM-Paper-And-SourceCode)** · ★ 71<br>2010–2024 年国赛论文和源代码。<br><sub>更新于 2025-06 · 国赛</sub>
- **[2023_CUMCM_National-First-Prize](https://github.com/linggm3/2023_CUMCM_National-First-Prize)** · ★ 64<br>2023 年国赛 A 题定日镜场优化，全国一等奖代码、论文和答辩 PPT。<br><sub>更新于 2025-08 · 国赛 · MIT</sub>
- **[CUMCM-2024A-Bench-Dragon](https://github.com/cny123222/CUMCM-2024A-Bench-Dragon)** · ★ 62<br>2024 年国赛 A 题“板凳龙”，全国一等奖。<br><sub>更新于 2025-06 · 国赛 · MIT</sub>
- **[2019GMCM](https://github.com/qssxbhxy/2019GMCM)** · ★ 62<br>2019 年华为杯 F 题第一名论文和代码。<br><sub>更新于 2019-12 · 华为杯 · MPL-2.0</sub>
- **[2026MCM-ICM_C](https://github.com/alectimison-maker/2026MCM-ICM_C)** · ★ 25<br>2026 年美赛 C 题 Finalist 的代码和论文，附三天备赛攻略。<br><sub>更新于 2026-05 · 美赛 · MIT</sub>

<a id="cat-solvers"></a>
## 求解器与常用库

比赛里最常用的开源库，按用途分：优化、智能算法、预测、评价、仿真、绘图。

- **[prophet](https://github.com/meta/prophet)** · ★ 20.5k<br>带季节和节假日效应的时间序列预测。<br><sub>更新于 2026-11 · MIT</sub>
- **[networkx](https://github.com/networkx/networkx)** · ★ 17.4k<br>图与网络分析，最短路、最大流、中心性。<br><sub>更新于 2026-11</sub>
- **[sympy](https://github.com/sympy/sympy)** · ★ 15.1k<br>符号计算：推公式、解微分方程。<br><sub>更新于 2026-11</sub>
- **[or-tools](https://github.com/google/or-tools)** · ★ 14.4k<br>Google 运筹工具箱：线性和整数规划、约束规划、车辆路径、排班。<br><sub>更新于 2026-11 · Apache-2.0</sub>
- **[statsmodels](https://github.com/statsmodels/statsmodels)** · ★ 11.8k<br>回归、时间序列（ARIMA 等）、假设检验。<br><sub>更新于 2026-11 · BSD-3-Clause</sub>
- **[sktime](https://github.com/sktime/sktime)** · ★ 10.1k<br>统一接口的时间序列机器学习框架。<br><sub>更新于 2026-11 · BSD-3-Clause</sub>
- **[SciencePlots](https://github.com/garrettj403/SciencePlots)** · ★ 9.4k<br>Matplotlib 的论文风格配色和样式。<br><sub>更新于 2026-06 · MIT</sub>
- **[scikit-opt](https://github.com/guofei9987/scikit-opt)** · ★ 6.7k<br>遗传、粒子群、模拟退火、蚁群等智能算法，几行代码就能调用。<br><sub>更新于 2026-03 · MIT</sub>
- **[deap](https://github.com/DEAP/deap)** · ★ 6.5k<br>灵活的进化算法框架。<br><sub>更新于 2026-04 · LGPL-3.0</sub>
- **[cvxpy](https://github.com/cvxpy/cvxpy)** · ★ 6.4k<br>用 Python 写凸优化问题的建模语言。<br><sub>更新于 2026-11 · Apache-2.0</sub>
- **[statsforecast](https://github.com/Nixtla/statsforecast)** · ★ 5.0k<br>快速的统计预测模型合集。<br><sub>更新于 2026-11 · Apache-2.0</sub>
- **[mesa](https://github.com/mesa/mesa)** · ★ 4.0k<br>基于智能体（agent-based）的仿真建模。<br><sub>更新于 2026-11 · Apache-2.0</sub>
- **[pymoo](https://github.com/the-dual-space/pymoo)** · ★ 3.0k<br>多目标优化库：NSGA-II、NSGA-III、MOEA/D 等。<br><sub>更新于 2026-11 · Apache-2.0</sub>
- **[pyomo](https://github.com/Pyomo/pyomo)** · ★ 2.6k<br>面向对象的代数建模语言，可接各种求解器。<br><sub>更新于 2026-11</sub>
- **[pulp](https://github.com/coin-or/pulp)** · ★ 2.5k<br>简单易用的 Python 线性规划库。<br><sub>更新于 2026-11</sub>
- **[JuMP.jl](https://github.com/jump-dev/JuMP.jl)** · ★ 2.5k<br>Julia 的数学优化建模语言。<br><sub>更新于 2026-11</sub>
- **[geatpy](https://github.com/geatpy-dev/geatpy)** · ★ 2.1k<br>高性能进化算法工具箱和框架。<br><sub>更新于 2026-02 · LGPL-3.0</sub>
- **[HiGHS](https://github.com/ERGO-Code/HiGHS)** · ★ 1.9k<br>高性能开源线性 / 混合整数规划求解器。<br><sub>更新于 2026-11 · MIT</sub>
- **[SALib](https://github.com/SALib/SALib)** · ★ 1.0k<br>敏感性分析：Sobol、Morris、FAST 等，论文里的“模型检验”常用。<br><sub>更新于 2026-11 · MIT</sub>
- **[PySCIPOpt](https://github.com/scipopt/PySCIPOpt)** · ★ 1.0k<br>SCIP 求解器的 Python 接口。<br><sub>更新于 2026-11 · MIT</sub>
- **[pysd](https://github.com/SDXorg/pysd)** · ★ 467<br>Python 系统动力学建模，可读 Vensim 模型。<br><sub>更新于 2026-10 · MIT</sub>
- **[pyDecision](https://github.com/Valdecy/pyDecision)** · ★ 375<br>多准则决策：AHP、TOPSIS、熵权法、VIKOR 等评价类方法。<br><sub>更新于 2026-10</sub>

<a id="cat-research"></a>
## 研究：大模型做数学建模和运筹优化

论文配套代码和评测基准，想了解 AI 建模能力边界的可以看。

- **[OptiMUS](https://github.com/teshnizi/OptiMUS)** · ★ 308 · 💤<br>OptiMUS：大模型加 MIP 求解器自动完成优化建模。<br><sub>更新于 2025-11 · MIT</sub>
- **[ORLM](https://github.com/Cardinal-Operations/ORLM)** · ★ 284 · 💤<br>ORLM：训练专门做优化建模的大模型。<br><sub>更新于 2025-09 · Apache-2.0</sub>
- **[OR-License](https://github.com/NineAbyss/OR-License)** · ★ 205 · 🆕<br>评测大模型 Agent 能否在没有专家预先改写问题的情况下完成运筹优化工作。<br><sub>更新于 2026-11 · Apache-2.0</sub>
- **[or_llm_agent](https://github.com/bwz96sco/or_llm_agent)** · ★ 108<br>OR-LLM-Agent：自动完成运筹优化问题的建模和求解。<br><sub>更新于 2026-09</sub>
- **[OptiChat](https://github.com/li-group/OptiChat)** · ★ 74<br>用大模型解释优化模型的结果。<br><sub>更新于 2026-09 · MIT</sub>
- **[SIRL](https://github.com/Cardinal-Operations/SIRL)** · ★ 69<br>用可验证奖励强化学习提升大模型的优化建模能力。<br><sub>更新于 2026-04</sub>
- **[ORQA](https://github.com/nl4opt/ORQA)** · ★ 51 · 💤<br>ORQA（AAAI 2025）：评测大模型运筹推理能力的问答基准。<br><sub>更新于 2025-06</sub>
- **[Mamo](https://github.com/FreedomIntelligence/Mamo)** · ★ 16 · 💤<br>Mamo：带求解器验证的数学建模评测基准。<br><sub>更新于 2024-06 · CC-BY-SA-4.0</sub>

<a id="faq"></a>
## 常见问题

**skill 怎么装？**
多数项目是标准 SKILL.md 格式。Claude Code 放进 `~/.claude/skills/`（全局）或项目里的 `.claude/skills/`，Codex 放进 `~/.codex/skills/`，也可以用 `npx skills add 作者/仓库名`。各工具路径不同，以项目 README 的安装说明为准。

**用了 AI 要声明吗？**
要。三个赛事都要求写明用了什么工具、用在哪里，见上方[规则](#rules)。

**全自动 skill 跑出来的论文能直接交吗？**
不建议。国赛要求核心建模与分析由参赛队独立完成，华为杯要求最终文字用参赛队自己的语言表述。全自动工具更适合赛前练习和对照思路，比赛里把关键判断留给自己。

**会收录“降 AI 率”工具吗？**
不收录以降 AI 率、躲避 AIGC 检测为主要卖点的项目。比赛要求的是如实披露。

**星标数多久更新一次？**
每周一由 GitHub Actions 自动刷新并重新排序，链接每周检查一次。

<a id="finder"></a>
## 让 Agent 帮你挑

这份清单也是一个 skill。把仓库里的 [`skills/math-modeling-finder`](skills/math-modeling-finder) 文件夹装进你的 agent（或运行 `npx skills add DU8866-nice/awesome-math-modeling`），然后问它：

> 我们是国赛三人队，用 Codex，想要人机协作的 skill，装哪个？

它会按你的赛事、所用工具和想要的 AI 参与程度，从清单里挑两三个并说明理由，同时提醒当届的 AI 使用规定。

<a id="related"></a>
## 相关合集

| 项目 | 说明 | ⭐ | 最近更新 |
|---|---|---:|---|
| [Awesome-Vibe-Research](https://github.com/modelscope/Awesome-Vibe-Research) | AI 辅助科研资源合集。 | 478 | 2026-11 |
| [awesome-academic-research-skills](https://github.com/kael-odin/awesome-academic-research-skills) | 学术论文与科研 Agent Skill 每日排行榜。 | 213 | 2026-11 |
| [Awesome-LLMs-for-Mathematical-Modeling](https://github.com/DataArcTech/Awesome-LLMs-for-Mathematical-Modeling) | 大模型做数学建模的论文合集。 | 18 | 2026-11 |

<a id="contributing"></a>
## 参与贡献

欢迎推荐项目或纠错：[提交 Issue](https://github.com/DU8866-nice/awesome-math-modeling/issues/new/choose)，或者修改 [`data/tools.yaml`](data/tools.yaml) 后提 PR，详见[贡献指南](CONTRIBUTING.md)。README 由脚本生成，请不要直接改它。

## Star 趋势

[![Star History Chart](https://api.star-history.com/svg?repos=DU8866-nice/awesome-math-modeling&type=Date)](https://star-history.com/#DU8866-nice/awesome-math-modeling&Date)
