<p align="right"><sub><b>简体中文</b> · <a href="README.zh-Hant.md">繁體中文</a> · <a href="README.en.md">English</a></sub></p>

<a href="https://slashsci.com/"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/img/readme/zh/hero-dark.jpg">
  <img src="docs/img/readme/zh/hero-light.jpg" alt="SlashSci — 科研 不止一面" width="100%">
</picture></a>

<h1 align="center">SlashSci Library</h1>

<p align="center"><b>为 AI 时代重构的文献管理</b><br>
块级解构 · 沉浸译读 · 本地优先 · Agent 就绪</p>

<p align="center">
<a href="../../releases/latest"><img alt="Release" src="https://img.shields.io/github/v/release/SlashSci/slashsci?style=flat-square&label=beta&color=2D5A67"></a>
<img alt="macOS" src="https://img.shields.io/badge/macOS-Apple_silicon-2D5A67?style=flat-square&logo=apple&logoColor=white">
<img alt="Windows" src="https://img.shields.io/badge/Windows-64--bit-2D5A67?style=flat-square&logo=windows&logoColor=white">
<img alt="MCP" src="https://img.shields.io/badge/MCP-built--in-2D5A67?style=flat-square">
<a href="https://discord.com/invite/ewNMAHvWsp"><img alt="Discord" src="https://img.shields.io/badge/Discord-join-5865F2?style=flat-square&logo=discord&logoColor=white"></a>
</p>

<p align="center">
<a href="https://slashsci.com/"><b>官网</b></a> ·
<a href="https://slashsci.com/#demo"><b>在线试用</b></a> ·
<a href="#下载与安装"><b>下载</b></a> ·
<a href="#内测社区"><b>内测社区</b></a> ·
<a href="../../issues"><b>问题反馈</b></a>
</p>

> [!NOTE]
> **内测阶段 · macOS 与 Windows**：SlashSci Library 目前处于小范围内测，macOS（Apple 芯片）与 Windows（64 位）版本均已开放。加入内测社区，即可获取安装包、安装指引与更新通知，并直接向开发者反馈。

## 核心能力

从读懂一篇论文，到沉淀成自己的知识库。

<table>
<tr>
<td width="56%"><img src="docs/img/readme/zh/01-read.jpg" alt="结构化精读"></td>
<td width="44%">
<sub>01 / 结构化精读</sub>
<h3>读懂</h3>
<p>回到论文本身，而非 PDF 的版面。</p>
<ul>
<li><b>块级全文解析</b>：章节、公式、图表与参考文献按结构完整保留；公式以 KaTeX 渲染，引文就地展开并可一键收录</li>
<li><b>沉浸式逐句译读</b>：译文与语境词汇释义随光标浮现于句侧，原文、译文、对照三种视图即时切换</li>
<li><b>出版级图像</b>：目录、引文与图表就地展开，插图可一键替换为出版商高清原图</li>
</ul>
</td>
</tr>
<tr>
<td width="44%">
<sub>02 / 锚定式批注</sub>
<h3>沉淀</h3>
<p>每一处思考，都锚定在原文之上。</p>
<ul>
<li><b>浮动锚定批注</b>：批注沿页边实时排布，以曲线连回原文位置；观点、方法、数据、疑问四色分类</li>
<li><b>双向溯源</b>：点击批注即定位原文，笔记支持 Markdown 与 LaTeX，引用后一键回到出处</li>
<li><b>语料与术语库</b>：收录佳句与重点术语，自动附译文、出处与写法解读</li>
</ul>
</td>
<td width="56%"><img src="docs/img/readme/zh/02-annotate.jpg" alt="锚定式批注"></td>
</tr>
<tr>
<td width="56%"><img src="docs/img/readme/zh/03-library.jpg" alt="本地文献库"></td>
<td width="44%">
<sub>03 / 本地文献库</sub>
<h3>掌控</h3>
<p>数据留在本地，检索尽在指尖。</p>
<ul>
<li><b>多源收录</b>：DOI、arXiv、PMCID 或网址一步导入；PDF 优先联网匹配结构化全文；浏览器插件支持需登录的页面</li>
<li><b>期刊指标与智能分类</b>：中科院分区、JCR、影响因子与被引次数一览；AI 按学科自动归类，中英文全文检索与查重</li>
<li><b>本地优先，为 Agent 而生</b>：全库以开放格式存于本机，一键导出迁移；内置 MCP 服务，Claude Code 等 Agent 可直接检索</li>
</ul>
</td>
</tr>
</table>

## 真实界面

下图是 Library 的阅读页：沉浸模式、页边批注与文献信息。官网的演示窗里运行的就是这个应用，无需安装即可试用。

<a href="https://slashsci.com/#demo"><img src="docs/img/readme/zh/app-reader.jpg" alt="SlashSci Library 演示" width="100%"></a>

<p align="center"><a href="https://slashsci.com/#demo"><b>在浏览器里试试 →</b></a></p>

## 数据与隐私

**你的文献，只在你的电脑上。**

- **本机存储**：文献以 JSON、Markdown 和 XML 等开放格式保存在本机文件夹，不上传服务器，也不被任何平台锁定。SQLite 只做可重建的索引。
- **密钥自己保管**：翻译与 AI 服务的密钥只保存在你的电脑里，用哪一家由你决定；接 Ollama 可以完全离线。
- **随时带走**：整库一键导出，换电脑、做存档，都不依赖我们。原文不可变，你的批注、译文和修改分开存放。

文献库里的文件都是开放格式：

```text
paper.json              原文块树
annotations.json        批注
translations/zh.json    译文，按句对齐
notes.md                笔记
source/                 原始 PDF / XML
index.sqlite            可重建
```

## 下载与安装

| 平台 | 系统要求 | 状态 |
| --- | --- | --- |
| **macOS** | Apple 芯片 · macOS 13 及以上 | 内测中 · [下载最新版](../../releases/latest) |
| **Windows** | 64 位 · Windows 10 及以上 | 内测中 · [下载最新版](../../releases/latest) |

安装包通过内测社区发放；已加入的成员也可以直接在 [Releases](../../releases/latest) 下载最新版本。

**安装说明（内测版）**

1. **macOS**：下载 `SlashSci-<版本>-arm64.dmg`，打开后把 SlashSci 拖进「应用程序」。
2. **Windows**：下载 `SlashSci-<版本>-x64.exe`，双击安装。
3. 第一次打开时如果被系统拦截，见下方说明。
4. 新版本发布后，应用左侧会出现「新版本」按钮，点一下即可下载。

<details>
<summary>第一次打开时被系统拦截？</summary>

内测版尚未签名，这是系统对未签名应用的默认提示，只需操作一次。

- **macOS**（提示「无法验证开发者」）：到「系统设置 → 隐私与安全性」，在页面下方点「仍要打开」。
- **macOS**（提示「已损坏，无法打开」或「应该推出磁盘映像」）：这是下载时系统加上的隔离标记，文件本身没有损坏。先把 SlashSci 拖进「应用程序」，再打开「终端」运行下面这行，然后重新打开：

  ```
  xattr -cr /Applications/SlashSci.app
  ```
- **Windows**（蓝色的「Windows 已保护你的电脑」）：点「更多信息」，再点「仍要运行」。

</details>

> [!TIP]
> 你的文献保存在本机的 `SlashSci-Library` 文件夹里。建议隔一段时间在「设置 → 文献库 → 导出整个文献库」备份一次。

## 内测社区

**加入内测，一起打磨 Library**。第一时间获取新版本，直接向开发者反馈问题与建议。

<table>
<tr>
<td align="center" width="33%">
<img src="docs/img/readme/qr-discord.png" width="148" alt="Discord"><br>
<b>Discord</b><br>
<sub>扫码或通过链接加入 Discord 社区</sub><br>
<a href="https://discord.com/invite/ewNMAHvWsp">加入 Discord →</a>
</td>
<td align="center" width="33%">
<img src="docs/img/readme/qr-wechat.png" width="148" alt="微信"><br>
<b>微信</b><br>
<sub>用微信扫码加入内测群</sub><br>
&nbsp;
</td>
<td align="center" width="33%">
<img src="docs/img/readme/qr-xhs.png" width="148" alt="小红书"><br>
<b>小红书</b><br>
<sub>扫码或通过链接加入小红书群</sub><br>
<a href="http://xhslink.com/m/MAL0EEu5FS">加入小红书群 →</a>
</td>
</tr>
</table>

## 斜杠科研系列

| 产品 | 状态 | 简介 |
| --- | --- | --- |
| **Library** | 内测中 | 文献管理与沉浸式阅读：导入、阅读、翻译、批注、语料、检索。 |
| **Studio** | 开发中 | 科研构思与可视化工作流编排：从文献到假设，从假设到实验设计。 |
| **Bot** | 开发中 | 个人科研助手与任务自动化：盯文献、跑流程、写草稿，都基于你自己的库。 |

## 问题反馈

遇到问题或有建议，请在 [Issues](../../issues) 里提出，并附上版本号（「设置 → 关于」）和系统信息。也欢迎直接在内测群里找我们。

---

<p align="center"><sub><a href="https://slashsci.com/">slashsci.com</a> · © 2026 SlashSci. All rights reserved.</sub></p>
