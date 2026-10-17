<div align="center">

```
███╗   ███╗ █████╗ ████████╗██╗  ██╗    ███╗   ███╗ ██████╗ ██████╗ ███████╗██╗         ██████╗ ██████╗  ██████╗
████╗ ████║██╔══██╗╚══██╔══╝██║  ██║    ████╗ ████║██╔═══██╗██╔══██╗██╔════╝██║         ██╔══██╗██╔══██╗██╔═══██╗
██╔████╔██║███████║   ██║   ███████║    ██╔████╔██║██║   ██║██║  ██║█████╗  ██║         ██████╔╝██████╔╝██║   ██║
██║╚██╔╝██║██╔══██║   ██║   ██╔══██║    ██║╚██╔╝██║██║   ██║██║  ██║██╔══╝  ██║         ██╔═══╝ ██╔══██╗██║   ██║
██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║    ██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗███████╗    ██║     ██║  ██║╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝
```

# 数学建模Pro · MathModel Pro

**数学建模竞赛全流程 AI 工作流 Skill —— 从读题到交稿，国赛标准，开箱即用**

**A full-pipeline AI workflow skill for mathematical modeling contests — from problem reading to submission-ready paper, national-contest grade, out of the box.**

[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)](https://github.com/ll2010650-coder/mathmodel-pro)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Language](https://img.shields.io/badge/lang-中文%20%7C%20English-orange.svg)]()
[![MATLAB](https://img.shields.io/badge/MATLAB-R2024b-red.svg)]()
[![Word](https://img.shields.io/badge/Word-MathType-purple.svg)]()
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)]()

[中文介绍](#-中文介绍) · [English](#-english-introduction) · [快速开始](#-快速开始--quick-start) · [工作流](#-六阶段工作流--six-stage-workflow) · [验收标准](#-验收标准--acceptance-criteria)

</div>

---

## 🇨🇳 中文介绍

**数学建模Pro** 是一个为数学建模竞赛（国赛 CUMCM / 美赛 MCM/ICM / 各类邀请赛）打造的 AI Agent 全流程工作流 Skill。它把一次完整的建模比赛拆解为 **审题 → 建模 → 编程 → 图表 → 论文 → 验收** 六个阶段，每个阶段都有可照做的操作手册、量化验收标准和血泪教训清单。

它不是模板，而是一套**被实战验证过的方法论**：内置 9 份国赛获奖论文的范式提炼、4 篇训练论文的评审扣分点、2000/2001 年经典赛题的算法速查，以及一条可生成合规 Word 论文的自动化生产线（pandoc + 样式模板 + MathType + 视觉检查）。

### ✨ 核心特性

- 🎯 **六阶段操作手册**：每个阶段按 `输入 → 编号步骤 → 公式/算法 → 产出物 → 验收标准` 组织，可直接照做
- 📐 **分题型方法论**：优化 / 预测 / 评价 / 机理 / 网络 五大题型的选型决策树与防错速查
- 📊 **国赛级图表规范**：泳道式技术路线图、Nature 配色、图证三段式、图内文字≈正文大小
- 📝 **Word 论文生产线**：Markdown → pandoc → 三线表（1.5/0.5 磅）→ 公式居中编号 → MathType 一键转换 → 页码 → 逐页视觉检查
- 🔍 **两级验收门禁**：硬错误（FAIL 必修）/ 警告（WARN 尽量修），占位符零容忍、数值唯一事实源
- 🧠 **教学双模式**：自动识别"我在想…"（引导教学）与"帮我做…"（直接执行）
- 📚 **知识沉淀**：每次解题自动写入 Obsidian 笔记与记忆库

### 📦 仓库结构

```
mathmodel-pro/
├── SKILL.md                              # 主文件:六阶段操作手册
├── references/                           # 方法论与案例库
│   ├── teaching-golden-rules.md          #   教学黄金规则(模式检测/禁忌/五步流程)
│   ├── modeling-norms.md                 #   建模规范(题型决策树/防错速查/验收门禁)
│   ├── word-paper-pipeline.md            #   Word 论文生产线(含血泪教训)
│   ├── document-handling.md              #   文档处理规范
│   ├── case-vessel-3d-reconstruction.md  #   案例:血管三维重建(2001 B题)
│   ├── case-pipe-optimization.md         #   案例:钢管订购运输(2000 B题)
│   ├── training-papers-lessons.md        #   训练论文+评审扣分点提炼
│   └── award-winning-papers.md           #   9份国赛获奖论文范式
└── assets/                               # 自动化生产线资产
    ├── ref_custom.docx                   #   论文样式模板(宋体小四/行距/段前段后)
    ├── make_ref.py                       #   样式模板生成脚本
    ├── fix_equations.py                  #   公式居中+右编号后处理
    └── fix_tables.py                     #   三线表+表格宽度后处理
```

---

## 🇬🇧 English Introduction

**MathModel Pro** is a full-pipeline AI-agent workflow skill for mathematical modeling contests (CUMCM, MCM/ICM, and beyond). It decomposes a complete contest into six stages — **Problem Analysis → Modeling → Coding → Visualization → Paper Writing → Verification** — each shipped with an actionable manual, quantitative acceptance criteria, and hard-won lessons.

It is not a template but **battle-tested methodology**: distilled patterns from 9 national-award-winning papers, review deductions from 4 training papers, algorithm quick-references for classic problems (2000/2001 CUMCM B), and an automated pipeline that produces submission-grade Word papers (pandoc + style template + MathType + visual inspection).

### ✨ Key Features

- 🎯 **Six-stage operating manual**: every stage organized as `input → numbered steps → formulas/algorithms → deliverables → acceptance criteria`
- 📐 **Problem-type methodology**: selection decision trees and pitfall guides for optimization / prediction / evaluation / mechanistic / network problems
- 📊 **Contest-grade figure standards**: swim-lane roadmaps, Nature-style palettes, figure-evidence triads, in-figure text ≈ body text size
- 📝 **Word paper pipeline**: Markdown → pandoc → three-line tables (1.5/0.5 pt) → centered numbered equations → one-click MathType conversion → page numbers → page-by-page visual check
- 🔍 **Two-tier verification gates**: hard errors (must-fix FAIL) vs warnings (WARN), zero tolerance for placeholders, single source of truth for all numbers
- 🧠 **Dual interaction modes**: auto-detects "I'm thinking…" (Socratic guidance) vs "do it for me…" (direct execution)
- 📚 **Knowledge sedimentation**: auto-writes Obsidian notes and a growing memory bank after every problem

---

## 🚀 快速开始 · Quick Start

### 中文

1. 将本仓库的 `SKILL.md`、`references/`、`assets/` 复制到你的 AI Agent 的 skills 目录（如 `.claude/skills/mathmodel-pro/`）
2. 对 Agent 说："用 mathmodel-pro 做这道建模题"，并提供题面文件（.doc/.docx/PDF）
3. 按六阶段推进，每阶段结束对照验收标准自查
4. 论文产出后，在 Word 的 MathType 选项卡执行一次 `Convert Equations` 完成公式格式收尾

### English

1. Copy `SKILL.md`, `references/`, and `assets/` into your AI agent's skills directory (e.g., `.claude/skills/mathmodel-pro/`)
2. Tell the agent: "Solve this modeling problem with mathmodel-pro", and provide the problem statement (.doc/.docx/PDF)
3. Progress through the six stages, self-checking against the acceptance criteria after each
4. Finish by running `Convert Equations` once in Word's MathType tab

---

## 🔄 六阶段工作流 · Six-Stage Workflow

| 阶段 Stage | 内容 Content | 验收标准 Acceptance |
|:---|:---|:---|
| 1️⃣ 审题与数据理解 | 读题面、实际查看数据（禁止预判形状）、子问题六要素 | 每个子问题输入/输出/约束齐全 |
| 2️⃣ 建模设计 | 题型归类、变量定义、假设检验、目标函数+约束逐条 | 三要素齐全，假设可被引用 |
| 3️⃣ 编程实现 | MATLAB/LINGO/Python，最小步骤+运行确认，约束回代 | 不信求解器 success，数值可追溯 |
| 4️⃣ 图表生成 | 数据图（Origin/MATLAB)+ 泳道路线图 + 思维导图 | 每图过三问：含义/价值/作用 |
| 5️⃣ 论文撰写 | Word+MathType，分题型写作格式，摘要公式化，创新显性化 | 格式 12 项清单全过 |
| 6️⃣ 验证验收 | 数值三处一致、合理性对比、可复现性、两级门禁 | 硬错误为零方可交付 |

---

## ✅ 验收标准 · Acceptance Criteria

| 指标 Metric | 标准 Standard |
|:---|:---|
| 正文字数 Body length | ≥ 10,000 字 characters |
| 正文页数 Body pages | ≥ 25 页 pages |
| 图表数量 Figures | ≥ 10 张，双面板图编 (a)(b) |
| 表格样式 Tables | 三线表：上下 1.5 磅黑、表头下 0.5 磅细线 |
| 公式 Equations | MathType 插入、居中、右侧编号 |
| 灵敏度分析 Sensitivity | 必须含数学表达式 λ = ΔZ/Δp |
| 参考文献 References | ≥ 5 条，全部真实存在 |
| 可复现性 Reproducibility | 附录代码参数与正文一致，一键重跑 |

---

## 🧪 实战验证 · Battle-Tested

本 Skill 经 5 轮自测迭代与真实赛题实战验证（模拟评分 76 → 90+）：

- ✅ 2001 CUMCM B 题（血管三维重建）：R = 30.08 ± 0.14，亚像素定位，32 页论文
- ✅ 运输优化 / 供应商评价 / 灰色预测 三类题型全流程演练
- ✅ 骨架法对比、噪声稳健性、平滑参数敏感性等方法间互验实验

*Validated through 5 self-test iterations and a real contest problem (simulated score 76 → 90+).*

---

## 📄 许可证 · License

MIT License — 自由使用、修改与分发，注明出处即可。

---

<div align="center">

**数学建模Pro · MathModel Pro** — 让每一次建模都有章可循 · *Making every modeling endeavor methodical.*

关键词 Keywords: 数学建模 | 数学建模竞赛 | 国赛 | 美赛 | CUMCM | MCM | ICM | mathematical modeling | contest workflow | AI agent skill | MATLAB | MathType | 论文写作

</div>
