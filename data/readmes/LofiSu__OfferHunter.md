# OfferHunter｜用 STAR 法则写求职简历

简体中文 | [English](README.en.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**用真实经历写一份经得起追问的求职简历**

OfferHunter 是一个开源的简历写作技能。把项目笔记或旧简历交给 Claude、ChatGPT、Codex、Grok 等助手，就能从头写一份简历、调整栏目顺序，或按岗位描述改写项目经历。支持中文、英文和双语稿。

- [看项目怎么写](skills/resume-engineering/references/examples.md)：EC-Monica 案例把项目负责人的工作、技术实现和上线数据分别写清。
- [按岗位选经历](skills/resume-engineering/references/ai-roles.md)：对照 100 条 BOSS 直聘岗位样本和按岗位整理的取材指南，找出最相关的项目。
- [看简历模板](#html-简历模板)：页首并列放 GitHub 和可核验的作品链接。可以复制 HTML，也可以使用黑白单栏 LaTeX 模板。

[快速开始](#快速开始) · [STAR 写法](#用-star-写项目经历) · [常见问题](#常见问题)

## 快速开始

在项目目录里克隆仓库，再按客户端选一条安装命令。

```sh
git clone https://github.com/LofiSu/OfferHunter.git
```

```sh
# Claude Code
mkdir -p .claude/skills && cp -R OfferHunter/skills/resume-engineering .claude/skills/
# Codex
mkdir -p .agents/skills && cp -R OfferHunter/skills/resume-engineering .agents/skills/
# Grok CLI
mkdir -p .grok/skills && cp -R OfferHunter/skills/resume-engineering .grok/skills/
```

开启新会话，请助手使用 `resume-engineering`。

**ChatGPT、Claude、Grok 网页端**：上传或粘贴 [SKILL.md](skills/resume-engineering/SKILL.md)，附上简历或项目笔记。有目标 JD 时一并提供。

## 用 STAR 写项目经历

简历里的每个项目都先拆成四部分，再写成正文。

- **S · 背景**：谁遇到了什么问题？
- **T · 我的职责**：你负责并完成了什么？
- **A · 行动**：你具体做了什么？关键方案是怎么实现的？
- **R · 结果**：最后交付了什么？有哪些上线数据、使用反馈或验证结果？

正文里的每个项目都按「背景、我的职责、行动、结果」分四行写，一页简历也采用这个顺序。没有量化指标时，用实际交付、采纳情况或已完成的验证来写结果。有待确认的事实放在稿外。

## 可以这样用

- 「按这份 AI 应用工程 JD 改写我的两段项目经历。每段保留最能体现工程取舍的两个要点。」
- 「把这份项目复盘写成可投递的一页简历。上线效果是团队数据，我个人负责的是流程编排。」
- 「审一遍这份简历。找出说不清归因的数字，给我可以直接替换的写法。」

默认给出可直接复制的简历正文。团队成果注明归属，个人职责写清自己具体做了什么。

查看 [EC-Monica 电商产运 Agent 的完整 STAR 改写](skills/resume-engineering/references/examples.md)。

## 按 BOSS 直聘 JD 投递

把目标职位的 JD、链接或截图和旧简历一起发给助手。它会把最相关的经历往前放，逐个项目按「背景、我的职责、行动、结果」改写，重点项目写清你在哪段工作或实习中负责了什么、技术方案怎么实现、最后交付了什么。打招呼语也会用一段真实经历说明你与岗位的相关性。也可以只改简历或只写打招呼语。[投递写法和示例](skills/resume-engineering/references/boss-application.md)

## 整份简历与 LaTeX

先在页首写求职方向、联系方式和作品链接，再按实际经历安排工作、实习和项目。教育、开源和奖项可按需要放在页首或单独列出。LaTeX 模板采用黑白单栏。

[简历结构](skills/resume-engineering/references/resume-structure.md) · [LaTeX 模板](skills/resume-engineering/templates/resume.tex)

先问自己最希望招聘方记住哪一点，再用一份作品或一项真实交付来证明。把这条亮点放在姓名下方。

在页首加一句自我介绍，把工作或实习经历、可点击的代表作和现在想做的方向写在一起。[中英文示例](skills/resume-engineering/references/resume-structure.md#一句话自我介绍)

**作品和经历怎么核验**：作品优先附可公开打开的演示或代码链接。需要背调时，经对方同意，可私下向招聘方提供前主管的工作邮箱或公司电话。

## HTML 简历模板

![通用中文简历模板，包含求职方向、实习经历和项目经历](assets/resume-preview-highlight-zh.png)

示例从实习经历开始。有正式工作经历时，可复制公司和项目的结构，在实习前加上「工作经历」。

展开源码并保存为 `resume.html`，用浏览器打开。填好内容后，可用打印菜单导出 A4 PDF。

<details>
<summary>展开并复制 HTML 源码</summary>

```html
<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>候选人姓名</title>
  <style>
    @page { size: A4; margin: 11mm; }
    * { box-sizing: border-box; }
    body {
      max-width: 210mm; margin: 0 auto; padding: 11mm;
      background: #fff; color: #161616;
      font: 10.5pt/1.38 Georgia, "Songti SC", "Noto Serif CJK SC", serif;
    }
    h1 { font-size: 21pt; line-height: 1.15; margin: 0 0 .15em; }
    header p { margin: .12em 0; }
    a { color: inherit; overflow-wrap: anywhere; }
    .highlight { color: #193677; }
    .intro { margin: .28em 0; }
    .profile, .open-source { font-weight: 700; }
    .section-title {
      color: #174add; border-bottom: 1.5px solid #315eed;
      font-size: 15pt; margin: .55em 0 .35em; padding-bottom: .16em;
    }
    .employer {
      background: #f0f1f3; border-radius: 4px;
      margin: .45em 0 .3em; padding: .32em .55em; font-size: 11pt;
    }
    .project-title { color: #193677; margin: .55em 0 .15em; font-size: 11pt; }
    .star { margin: 0; padding-inline-start: 1.25em; }
    .star > li { margin: .16em 0; }
    .star ul { list-style: circle; margin: .1em 0 0; padding-inline-start: 1.25em; }
    .responsibility { margin: .2em 0 .18em; }
    .responsibility strong { color: #193677; }
    .star-action li { margin: .12em 0; }
    @media print {
      body { max-width: none; margin: 0; padding: 0; }
      h2, h3, h4 { break-after: avoid; }
      li { break-inside: avoid; }
      .employer { print-color-adjust: exact; }
    }
  </style>
</head>
<body>
  <header>
    <h1>候选人姓名</h1>
    <p class="highlight"><strong>个人亮点</strong> · 我最擅长的工作与一项可核对的成果。</p>
    <p>手机号 ｜ <a href="mailto:hello@example.com">hello@example.com</a></p>
    <p class="profile">求职方向</p>
    <p class="open-source"><a href="https://github.com/username">GitHub</a> ｜ <a href="https://example.com/portfolio">作品链接</a></p>
    <p class="intro">曾在某团队负责某项工作，代表作是 <a href="https://example.com/work">作品名称</a>，目前希望深入某个方向。</p>
    <p>学校专业</p>
  </header>
  <main>
    <section>
      <h2 class="section-title">实习经历</h2>
      <h3 class="employer">公司或团队｜岗位｜起止时间</h3>
      <article class="resume-project">
        <h4 class="project-title">实习项目名称</h4>
        <ul class="star">
          <li><strong>背景</strong> · 服务对象遇到了什么问题？</li>
          <li class="responsibility"><strong>我的职责</strong> · 我负责并完成了什么？</li>
          <li><strong>行动</strong> · 我做了什么，采用了什么方法？</li>
          <li><strong>结果</strong> · 交付了什么，有哪些可核对的成效？</li>
        </ul>
      </article>
    </section>

    <section>
      <h2 class="section-title">项目经历</h2>
      <article class="resume-project">
        <h4 class="project-title">项目名称</h4>
        <ul class="star">
          <li><strong>背景</strong> · 服务对象遇到了什么问题？</li>
          <li class="responsibility"><strong>我的职责</strong> · 我负责并完成了什么？</li>
          <li><strong>行动</strong> · 我做了什么，采用了什么方法？</li>
          <li><strong>结果</strong> · 交付了什么，有哪些可核对的成效？</li>
        </ul>
      </article>
    </section>
  </main>
</body>
</html>
```

</details>

## 常见问题

### 没有目标 JD，能先写一整份 AI 简历吗？

可以。先用旧简历或项目笔记起草，优先写职责和结果最清楚的经历。拿到岗位 JD 后，再按该岗位的实际工作重排和精简。

### STAR 法则怎么用在一页简历里？

每个项目写四行，每行只留最需要读者知道的信息。团队数据写清归属。没有量化数据时，可以写已上线能力、实际采纳或验证发现。

### HTML 或 LaTeX 简历如何导出 PDF？

HTML 可用浏览器的打印菜单导出 A4 PDF。LaTeX 源文件可用 XeLaTeX 编译。两份模板都使用单栏布局，适合突出内容和阅读顺序。

### BOSS 直聘岗位索引是什么？

索引来自公开招聘列表，保留职位名、可见 JD 关键词、STAR 取材提示和来源。采集日期和访问限制见[岗位参考](skills/resume-engineering/references/ai-roles.md)。

## 贡献

欢迎通过 [Issues](https://github.com/LofiSu/OfferHunter/issues) 提交可追溯的公开 JD、脱敏案例或模板改进。如果 OfferHunter 帮你把一段经历写得更清楚，欢迎在 GitHub 点一颗 Star。

## 许可

[MIT](LICENSE)
