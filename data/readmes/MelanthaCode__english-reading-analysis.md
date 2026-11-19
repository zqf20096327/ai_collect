# 英语阅读 → 中文 · English Reading to Chinese

[![Stars](https://img.shields.io/github/stars/MelanthaCode/english-reading-analysis?style=social)](https://github.com/MelanthaCode/english-reading-analysis/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-SKILL.md-8A2BE2)](https://skills.sh/melanthacode/english-reading-analysis/english-reading-analysis)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-plugin-d97757)](#安装)
[![npm](https://img.shields.io/npm/v/dsh-skill-english-reading?logo=npm&label=npm)](https://www.npmjs.com/package/dsh-skill-english-reading)
[![npm downloads](https://img.shields.io/npm/dm/dsh-skill-english-reading)](https://www.npmjs.com/package/dsh-skill-english-reading)
[![cross-platform](https://github.com/MelanthaCode/english-reading-analysis/actions/workflows/cross-platform.yml/badge.svg)](https://github.com/MelanthaCode/english-reading-analysis/actions/workflows/cross-platform.yml)

> **把英语试卷丢给 AI，输出可打印的中文解析。**

![输出示例：英语文章的逐段中文翻译与长难句拆解](assets/screenshots/01-article.png)

一个给 AI Agent 用的技能：把**英语阅读材料转成中文**——文章逐段翻译，试卷题目与选项翻译并给出答案，复杂长难句做句法拆解，最后输出一份可打印的 A4 文档。

核心是**英译中**：长难句分析是其中一环，不是全部。

**输入**：一篇英语文章、一份英语试卷（文字版 / 扫描件 / 手机照片）
**输出**：中文分析文档 + 可选 A4 打印 PDF

## 快速开始

```bash
# DeepSeek Harness：插件市场搜索「英语阅读分析」，或
dsh plugin add dsh-skill-english-reading

# 任意支持 Agent Skills 的工具（Codex / Cursor / Copilot / Cline / OpenCode …20+）
npx skills add MelanthaCode/english-reading-analysis

# Claude Code 插件市场
claude plugin marketplace add MelanthaCode/english-reading-analysis
claude plugin install english-reading-analysis@melantha-skills
```

不用装依赖、不用配 API Key。不要命令行的话，可以下[离线包](https://github.com/MelanthaCode/english-reading-analysis/releases/latest)直接解压到技能目录。

## 安装

同一个仓库同时是三种形态，按你用的工具选一个：

| 你的工具 | 安装方式 |
|---|---|
| **DeepSeek Harness** | 插件市场搜索「英语阅读分析」，或 `dsh plugin add dsh-skill-english-reading`（[npm](https://www.npmjs.com/package/dsh-skill-english-reading)）|
| **Claude Code** | `claude plugin marketplace add MelanthaCode/english-reading-analysis` → `claude plugin install english-reading-analysis@melantha-skills` |
| **Codex / Cursor / Copilot / Cline / OpenCode / Amp / Windsurf / Gemini CLI 等 20+** | `npx skills add MelanthaCode/english-reading-analysis` |

`npx skills add` 是覆盖面最广的一条：它把技能装到 `.agents/skills/english-reading-analysis/`，再为各工具建软链，一次覆盖 20 多个 Agent。

手动安装（任意工具）：

```bash
git clone https://github.com/MelanthaCode/english-reading-analysis.git \
  ~/.claude/skills/english-reading-analysis      # Claude Code
# 或
  ~/.codex/skills/english-reading-analysis       # Codex
# 或
  ~/.dsh/skills/english-reading-analysis         # DeepSeek Harness
```

Windows 上的写法（PowerShell）：

```powershell
git clone https://github.com/MelanthaCode/english-reading-analysis.git `
  "$env:USERPROFILE\.claude\skills\english-reading-analysis"
```

### 三种形态的关系

- **技能**（`SKILL.md`）：内容本体，所有 Agent 通用
- **DSH 插件**（`dsh-plugin/`）：把技能注册进 Harness 技能目录，并在侧栏提供面板
- **Claude Code 插件**（`.claude-plugin/`）：Claude Code 的插件市场入口

三者共用同一份 `SKILL.md` 与同一套打印样式，改一处三处同步。

## 支持平台

**Windows、macOS、Linux 三个系统都必须能完整跑通**，包括最后的 A4 PDF 渲染。这不是口头承诺：仓库里有一条 CI 在三个系统的真实机器上跑同一份冒烟测试（[cross-platform.yml](.github/workflows/cross-platform.yml)），任何平台坏掉，徽章就会变红。

| 系统 | 支持 | 浏览器 | 扫描件所需（可选） | 自检 |
|---|---|---|---|---|
| Windows 10 / 11 | ✅ CI 实测 | Chrome、Edge、Brave（默认安装即可，**不需要加进 PATH**） | TeXLive/MiKTeX 自带，或 `scoop install poppler` | `python scripts\render_pdf.py --check` |
| macOS 12+ | ✅ CI 实测 | Chrome、Chromium、Edge | `brew install poppler` | `python3 scripts/render_pdf.py --check` |
| Linux（x64/arm64） | ✅ CI 实测 | `google-chrome`、`chromium`、`microsoft-edge`、`brave-browser` | `apt install poppler-utils` | `python3 scripts/render_pdf.py --check` |

自检通过时输出类似：

```
platform:    win32
python:      3.11.9
browser:     C:\Program Files\Google\Chrome\Application\chrome.exe
weasyprint:  MISSING (fallback engine)
wkhtmltopdf: MISSING (fallback engine)
pdftoppm:    C:\texlive\2024\bin\windows\pdftoppm.exe
pdfinfo:     C:\texlive\2024\bin\windows\pdfinfo.exe
engine:      chrome -> C:\Program Files\Google\Chrome\Application\chrome.exe
status:      ready for PDF rendering
```

看 `status` 一行即可：

- `ready for PDF rendering` → 引擎是 Chrome 系，版式完全符合规范
- `ready, but DEGRADED` → 只有 weasyprint / wkhtmltopdf，能出 PDF 但分页会有差异
- `NO RENDERER` → 本机一个引擎都没有

## 超出三个系统怎么办

WSL、Alpine、FreeBSD、Termux、只有 Safari 的 Mac、锁权限的公司电脑——这些环境不做保证，但**不会让任务卡死**。脚本内置四级降级：

| 层级 | 手段 | 结果 |
|---|---|---|
| 1 | `--chrome "路径"` 或 `RENDER_PDF_BROWSER` 环境变量 | 用已有浏览器，质量不变 |
| 2 | 装一个：`apk add chromium`、`pip install weasyprint`、`npx playwright install chromium` | 质量不变或接近 |
| 3 | `--engine weasyprint` / `--engine wkhtmltopdf` | 能出 PDF，分页有差异 |
| 4 | 交付 HTML | 浏览器里 `Ctrl+P` 另存为 PDF，页面已按 A4 排版 |

关键是第 4 层：**PDF 是包装，不是内容。** 渲染完全不可用时任务依然完成——Agent 按 [references/platform-fallback.md](references/platform-fallback.md) 的决策链执行，并在回复里说明走的是哪一层。脚本退出码也是机读的：`3` 表示无引擎、`4` 超时、`5` 未产出，方便 Agent 分支处理。

## 兼容性

| 工具 | 接入方式 |
|---|---|
| Claude Code | `npx skills add` 自动软链 / 插件市场 / `~/.claude/skills/` |
| Codex CLI | `npx skills add` 写入 `.agents/skills/` |
| GitHub Copilot、OpenCode、Amp、Cline、Cursor、Windsurf、Gemini CLI 等 | 同上，走 Agent Skills 通用目录约定 |
| DeepSeek Harness | 放入 `~/.dsh/skills/` 或项目内 `.agents/skills/` |

只要工具支持 **Agent Skills** 约定（`SKILL.md` + 同目录资源），把它放进技能目录即可，无需为每家厂商改代码。

## 预览

**① 文章：逐段原文 + 中文译文，复杂长难句高亮编号**

![文章页：原文与中文译文](assets/screenshots/01-article.png)

**② 题目 · 选项 · 答案：题干与选项中英对照，答案附原文定位解析**

![题目页：题干、选项、答案与解析](assets/screenshots/02-questions.png)

**③ 长难句拆解：左栏为句子/从句级框架，右栏为原词（词序不变），词下彩色下划线标成分**

![长难句页：句法框架与成分标注](assets/screenshots/03-long-sentences.png)

## 用法示例

> 把这篇英语文章翻成中文，复杂长难句高亮，文末单独拆解。

> 这份英语试卷（扫描件）：逐篇翻成中文，题目和选项都要中英对照，给出答案和解析，再按每篇做长难句分析。

> 这是我批改过的卷子，帮我把错题分析一下，错因归类，再针对每篇的难句做拆解。

## 输出结构

每篇文章独立成块，块内顺序固定：

```
文章 1：<主题>
  1. 原文 + 译文          英译中，逐段对照
  2. 题目 · 选项 · 答案    题干与选项中英对照、答案、原文定位解析
  3. 作答对错分析          仅在提供作答时：逐题对错、错因归类、纠正提示
  4. 长难句拆解            左栏句法框架 / 右栏原词，彩色下划线标成分
```

多篇文章按同样结构逐篇重复；没有的环节直接省略。

## 特点

- **以译为主**：原文照录不改写，译文准确优先于文采，保留因果、对比、程度与挂接关系。
- **长难句单次呈现**：一个句子只出现一次，左侧标句子/从句级框架，右侧保留原词序，不重复三遍同一句话。
- **题目可核对**：题干、选项都翻译，答案指回原文句子，并说明干扰项错在哪。
- **可直接打印**：HTML + headless Chrome 渲染 A4 PDF，卡片与题块不跨页，标题不孤行。
- **无身份噪声**：标题、页脚、文件名只写文章主题，不带学校名、考试名、原卷页码。

## 依赖

| 用途 | 需要 |
|---|---|
| 渲染 PDF | Google Chrome / Chromium / Edge（任一，装在默认位置即可） |
| 读取扫描件 | `pdftoppm`（poppler） |
| 运行脚本 | Python 3.9+ |

**Windows 用户**：Chrome 和 Edge 默认不在 `PATH` 里，脚本会自己到注册表 `App Paths` 和 `Program Files`、`Program Files (x86)`、`%LOCALAPPDATA%` 下找。装完先自检：

```bash
python3 scripts/render_pdf.py --check
# browser: C:\Program Files\Google\Chrome\Application\chrome.exe
```

如果装在非默认位置，显式指定即可：

```bash
python3 scripts/render_pdf.py 输入.html 输出.pdf --chrome "D:\你的路径\chrome.exe"
```

扫描件依赖 `pdftoppm`：macOS 用 `brew install poppler`，Windows 可装 TeXLive/MiKTeX（自带）、或 `scoop install poppler`。它缺失只影响"扫描件转图"这一步，文字版材料不受影响。

```bash
brew install poppler            # macOS 读扫描件用
python3 scripts/render_pdf.py 输入.html 输出.pdf
```

## 隐私与安全

- **不联网**：`scripts/render_pdf.py` 只调用本地 Chrome，无任何 HTTP 请求、无遥测、不上传任何内容。
- **只读你的材料**：文章、试卷、照片在你的机器上读取与渲染，产物写在本地。
- **可审计**：全部逻辑都在本仓库的 Markdown 与一个约 300 行的纯标准库 Python 脚本里，没有构建步骤、没有依赖包、没有二进制。
- **MIT 许可**：可自由修改、二次分发。

## 目录

```
english-reading-analysis/
├── SKILL.md                       # 入口：结构、流程、验收清单
├── AGENTS.md                      # 给 AI 读的自述：能力、安装、验证、改动红线
├── CHANGELOG.md                   # 版本变更
├── .claude-plugin/
│   ├── plugin.json                # Claude Code 插件清单
│   └── marketplace.json           # 插件市场条目
├── references/
│   ├── sentence-analysis.md       # 长难句：分析顺序、从句分类、展示规则、范例
│   ├── paper-workflow.md          # 试卷：题块字段、题型解法、干扰项、错因分类
│   ├── layout-pdf.md              # 版式：CSS、分页、渲染命令、排错
│   └── platform-fallback.md       # 引擎缺失时的四级降级决策链
├── assets/
│   ├── template.html              # 可直接套用的 HTML 模板
│   └── screenshots/               # README 用效果图
├── scripts/
│   └── render_pdf.py              # HTML → A4 PDF（macOS / Linux / Windows）
├── tests/
│   ├── smoke.html                 # 跨平台冒烟页，CI 在三系统上渲染它
│   └── test_engines.py            # 引擎探测单测（CI 三系统都跑）
└── .github/workflows/
    └── cross-platform.yml         # Windows / macOS / Linux 三系统 CI
```

## 设计取舍

- **为什么不用 Word**：高亮、词下彩色下划线、卡片级分页控制在 Word 里很难稳定，HTML + 打印更可控。
- **为什么段落不跨页**：英文原文与中文译文必须挨着看，拆到两页会打断对照阅读。
- **为什么句法框架只到句子/从句级**：把名词短语内部也拆成层级会让左栏膨胀，反而看不清主干。

## English

An Agent Skill that turns English reading passages and exam papers into a Chinese study document: paragraph-by-paragraph translation, question and option translation with answers and source-line explanations, error analysis, long-sentence syntax breakdown, and a print-ready A4 PDF.

Install once, use in 20 agents:

```bash
npx skills add MelanthaCode/english-reading-analysis
```

[Full English README →](README.en.md)

## 字体

英文标题用 [Jost](https://fonts.google.com/specimen/Jost)、正文用 [Zilla Slab](https://fonts.google.com/specimen/Zilla+Slab)（均为 SIL Open Font License 1.1），以 base64 内嵌在 `assets/template.html` 里，所以离线渲染 PDF 也能保持同样字形；中文回落到系统宋体 / PingFang。

## 图标

侧栏与市场图标使用 [Lucide](https://lucide.dev) 的 `languages` 字形（ISC 许可），以路径内联方式实现，不引入运行时依赖。

## 作者

Melantha · [github.com/MelanthaCode](https://github.com/MelanthaCode)

## 配色

界面与打印样式共用一套颜色变量，取自 [Searching for Birds](https://searchingforbirds.visualcinnamon.com/)（Nadieh Bremer 的观鸟数据可视化项目）：`--primary #f9564e`、`--secondary #ffcc2d`、`--accent #23abab`、`--background #f4efe5`，另附它的"鸟种色"（northern cardinal 红、common raven 靛、sandhill crane 绿、american robin 橙、blue jay 蓝、mallard 粉、barred owl 沙、cooper's hawk 青绿）。配色以数据形式存放在 `dsh-plugin/client.js` 的 `PALETTES` 里（同一份镜像到 `assets/palette.json`），面板通过 `ACTIVE_PALETTE` 选用其中一套；打印样式用 `assets/template.html` 的 CSS 变量，取值与之一致。换配色只需改 `ACTIVE_PALETTE` 一行，其余代码不用动。

## License

MIT

---

如果这个技能帮你省了时间，点个 ⭐ 会让更多需要它的人搜到它 —— [Star](https://github.com/MelanthaCode/english-reading-analysis)。
