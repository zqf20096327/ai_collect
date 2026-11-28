<div align="center">

<img src=".github/assets/readme-hero.webp" width="100%" alt="ChalkLee：让每一道题，都有更多可能。黑板风的 ChalkLee 品牌横幅，右侧是用粉笔画的勾股定理。">

<p><strong>开源的本地题库与备课工具</strong>——把电脑里的 PDF 和 Word 变成可编辑、可搜题、可交给 AI 直接修改的试卷与讲义。</p>

<a href="https://github.com/seven0x16/chalklee/releases/latest"><img src="https://img.shields.io/github/v/release/seven0x16/chalklee?label=Release&amp;color=114837&amp;style=flat-square" alt="Latest release"></a>
<a href="LICENSE"><img src="https://img.shields.io/badge/License-AGPL_3.0-114837?style=flat-square" alt="License: AGPL 3.0"></a>
<a href="#下载安装"><img src="https://img.shields.io/badge/Platform-macOS_%7C_Windows-114837?style=flat-square" alt="Platform: macOS and Windows"></a>
<a href="#交流与反馈"><img src="https://img.shields.io/badge/QQ%E7%BE%A4-1135963910-114837?style=flat-square" alt="QQ 群 1135963910"></a>

<p>
  <a href="#下载安装"><strong>下载安装</strong></a>
  &nbsp;|&nbsp;
  <a href="#使用方式">使用方式</a>
  &nbsp;|&nbsp;
  <a href="#接入-ai">接入 AI</a>
  &nbsp;|&nbsp;
  <a href="#从源码运行">从源码运行</a>
  &nbsp;|&nbsp;
  <a href="#参与贡献">参与贡献</a>
</p>

</div>

## ChalkLee 是什么

老师的电脑里通常存着多年积累的 PDF 和 Word，其中不少 PDF 是扫描件。它们能看、能打印，却很难再利用：想改一道题得重新打字，想从十几份资料里找同类题只能一份份翻，交给 AI 处理也要来回复制，再重新调公式和排版。

ChalkLee 把这些资料转换成结构化的可编辑文档，每道题的题干、选项、答案、解析和知识点都分开保存。这样一来：

- **直接编辑与排版**：文字、公式像在 Word 里一样改，增删题目后题号自动重排；
- **文件夹即题库**：一个文件夹里的所有文档都能一起搜索、筛选、挑进选题篮组卷；
- **AI 改得准**：ChalkLee AI 能准确找到“第 3 题”“这道题的解析”，改动直接写进卷面。

新的试卷和讲义也可以直接在 ChalkLee 里编写。教材、知识清单、出过的题和出题要求放在同一个文件夹里，ChalkLee AI 出题时都用得上。

<img src=".github/assets/app-interface.webp" width="100%" alt="ChalkLee 应用界面：左侧是资料目录，中间是可编辑的试卷，右侧 ChalkLee AI 正在补全答案与解析。">

## 使用方式

### 1. 打开资料文件夹

ChalkLee 直接打开电脑上的普通文件夹，不用导入，也不建数据库。文件都留在原处，照样可以用其他软件打开。

### 2. 转换旧资料

打开 PDF（包括扫描件）、Word 或 LaTeX（.tex），点“用 ChalkLee AI 转换”；也可以右键文件夹，整批转换。

转换会把整页内容拆成一道道题：公式、化学式和 Word 里的 MathType 变成可编辑公式，卷末答案按题号归到对应的题下，每道题标上知识点。结果另存为 `.chalklee` 文档，放在原稿旁边；拿不准的地方标出“[待核对]”，并在转换记录里列出提醒，方便对照原稿检查。

### 3. 编辑和排版

文档按纸张排版，支持 A4 单栏、A3 双栏以及页边距和页眉页脚，编辑时看到的就是打印出来的样子。题目像在 Word 里一样直接修改，增删后题号自动重排，删选项时后面的字母和正确选项也会跟着更新；选项、答案和解析用题目旁边的按钮添加，整份粘贴进来的内容可以一键识别成题目。

答案和解析可以随时隐藏，学生版和教师版不用各存一份。导出 Word、PDF 或打印时，可以选择是否带上答案与解析，以及放在每道题后还是文档末尾。

笔记、提纲和计划可以用 Markdown 写，ChalkLee 直接编辑原文件，边写边显示排版效果。要整理成试卷或讲义发给学生时，点“转换为 ChalkLee”。

### 4. 搜题和组卷

文件夹里所有文档的题都能一起搜，可以按年级、年份、题型、难度和知识点筛选。挑中的题放进选题篮，再插入正在编辑的文档，或者组成一份新文档，题号自动排好。

### 5. 让 AI 直接修改文档

在 ChalkLee AI 面板里用平常的话提要求，改动直接写进文档。比如：

- 给第 3 题出 2 道相似题，插在原题后面
- 把截图里的题加到练习里
- 把第 4 题改成选择题
- 把这份压缩到 3 页
- 做一个能拖动的勾股定理演示，上课投屏用

### 6. 按教材和技能出题

- **教材与知识清单**：教材的电子版或扫描件直接放进文件夹，打开后点“不需要转换”，整批转换时会跳过它。ChalkLee AI 能读教材，把学过的章节整理成**知识清单**；老师核对后，出题就按清单确定范围。
- **把出题习惯存成技能**：出过一份满意的练习后，对 ChalkLee AI 说“把刚才的要求存成技能”，题型、分值和出题要求会整理成一页 Markdown，放进资料文件夹根目录的“技能”文件夹，随时可以修改。以后说“出 16.3 的巩固练习”，ChalkLee AI 会先读对应的**技能**，再照着出。
- **跨工具通用**：技能采用通用的 `SKILL.md` 格式，通过命令行工具或其他 AI 应用使用 ChalkLee 时同样有效。

### 7. 在插件中心添加小工具

插件中心放待办、日历这类独立的小工具，这两个已经内置。想要点名、细目表这样的工具，点“用 ChalkLee AI 做插件”说出需求，ChalkLee AI 做好后先试用，满意再安装。从 [chalklee-plugins](https://github.com/seven0x16/chalklee-plugins) 下载或同事分享的插件文件，拖进插件中心就能安装；自己的插件也能导出分享给别人。

## 接入 AI

ChalkLee 不绑定某一家 AI，也不用注册账号。转换和对话用的是你自己的模型服务，或者你已经在用的 AI 应用：

| 方式 | 可用于 | 支持 |
| --- | --- | --- |
| **接入模型服务** | 原稿转换、ChalkLee AI 对话 | DeepSeek、Kimi、智谱、阿里云百炼、火山方舟、MiniMax、硅基流动、OpenRouter、OpenAI、Anthropic、Gemini、Ollama 及兼容接口 |
| **使用本机已登录的命令行工具** | ChalkLee AI 对话 | Claude Code、Codex、CodeBuddy、OpenCode、Cursor、Qoder |
| **在 AI 应用里使用 ChalkLee（MCP）** | 原稿转换、改题、组卷等 | WorkBuddy、豆包工作、千问办公、Codex，以及 Cursor、Cherry Studio、Trae 等支持 MCP 的应用 |

原稿转换需要支持图片输入的模型。连接 AI 应用的方法见 [外部 AI 应用连接](docs/external-agent-mcp.md)。

## 数据安全

- 打开、编辑、搜题和组卷都在本机完成，不需要联网。只有转换和对话时，需要处理的内容才会发给你选择的服务，不经过 ChalkLee 的服务器。
- 原稿不会被改动；转换结果另存一份，遇到重名再另存，不覆盖已有文件。
- 编辑时自动保存版本，可以随时恢复；ChalkLee AI 的每次修改和目录整理都能撤销。
- 插件在沙箱里运行，不能联网，也不能直接读写工作区里的文件；需要读取文档、搜索题库等权限时，安装前会列出来请老师确认。
- 版本记录、题库分组、插件数据等应用数据保存在文件夹里的 `.chalklee/` 目录。

## 下载安装

- **GitHub Releases**：[前往下载最新版本](https://github.com/seven0x16/chalklee/releases/latest)
- **百度网盘**：[点此下载（v0.2.0）](https://pan.baidu.com/s/1uoAg-R05FS7C_bR6zi5XqA?pwd=ivvc)，提取码 `ivvc`
- **QQ 群文件**：加入交流群 **1135963910**（[扫码进群](#交流与反馈)），在群文件里下载

| 电脑 | 安装包 |
| --- | --- |
| Mac（Apple 芯片，M1 及以后，macOS 13+） | `…-mac-arm64.dmg` |
| Mac（Intel 芯片，macOS 13+） | `…-mac-x64.dmg` |
| Windows（64 位，Windows 10+） | `…-win-x64.exe` |

不确定 Mac 是哪种芯片时，打开苹果菜单 › 关于本机查看。

安装包暂未在 Apple 和微软登记开发者身份，系统认不出发布者，所以第一次打开时会提示无法验证，并不是查出了问题。按下面的步骤允许一次，以后就能直接打开。

<details>
<summary><strong>第一次打开时提示无法验证</strong></summary>

**macOS**

1. 把 ChalkLee 拖进“应用程序”后打开。弹窗提示“未打开‘ChalkLee’”时点“完成”，不要点“移到废纸篓”。
2. 打开“系统设置 › 隐私与安全”，往下翻到“安全性”，在“已阻止‘ChalkLee’以保护 Mac”这一行点“仍要打开”。没看到这一行时，先再打开一次 ChalkLee。

**Windows**：出现“Windows 已保护你的电脑”时，点“更多信息”，再点“仍要运行”。

</details>

安装后打开资料文件夹就能开始编辑和搜题；转换原稿和使用 ChalkLee AI 前，先在设置里[接入 AI](#接入-ai)。

## 常见问题

<details>
<summary><strong>ChalkLee 收费吗？</strong></summary>

ChalkLee 本身开源免费，不用注册账号，也不收会员费。只有转换原稿和使用 AI 时，会调用你自己的模型服务或 AI 应用，相关费用由对应平台收取。

</details>

<details>
<summary><strong>支持哪些学科？</strong></summary>

从小学到高中，各科的试卷和讲义都能转换和编辑。数学公式、化学方程式、几何配图、英语阅读和语文材料题都支持，不同学科的题型与排版都能自然呈现。

</details>

<details>
<summary><strong>支持哪些文件，能导出 Word 吗？</strong></summary>

支持转换 PDF（包括扫描件）、Word（.docx 和 .doc）、LaTeX（.tex）和 Markdown。做好的文档能打印或导出 Word、PDF；导出 Word 保留内容和基础样式，要完整保留版面请导出 PDF。

</details>

## 交流与反馈

使用中遇到问题，或想分享教学场景、提出建议，欢迎加入 QQ 群 **1135963910**（群文件同步提供安装包），也可以在 [Issues](https://github.com/seven0x16/chalklee/issues) 里反馈。

<p align="left">
  <img src=".github/assets/qq-group.webp" width="168" alt="ChalkLee 交流群的 QQ 二维码，群号 1135963910">
</p>

如果 ChalkLee 对你的备课有帮助，欢迎在页面右上角点一颗 Star，让更多老师看到它。

## 从源码运行

ChalkLee 基于 Electron、React 和 Tiptap，需要 **Node.js 22.19（22.x）或 24 及以上版本**。

```bash
git clone https://github.com/seven0x16/chalklee.git
cd chalklee
npm ci
npm run dev
```

测试与提交代码见[参与贡献](CONTRIBUTING.md)，打包与代码结构见[桌面开发说明](apps/desktop/README.md)。

| 想了解 | 看这里 |
| --- | --- |
| `.chalklee` 文件里有什么（ZIP 包，内含 JSON 文档与资源） | [ChalkLee 文档格式](docs/chalklee-format.md) |
| 让其他 AI 应用连接 ChalkLee | [外部 AI 应用连接](docs/external-agent-mcp.md) |
| 写一个点名、细目表这样的小工具 | [ChalkLee 插件](docs/plugin-api.md)，模板和示范插件见 [chalklee-plugins](https://github.com/seven0x16/chalklee-plugins) |

## 参与贡献

欢迎提交代码改进 ChalkLee。提交前请阅读 [贡献说明](CONTRIBUTING.md)，按改动范围完成相应的测试与验证；外部贡献在合并前需要签署贡献者许可协议（CLA）。

## 许可证

ChalkLee 采用 [GNU AGPL-3.0-only](LICENSE) 开源。如需在闭源软件或服务中使用，可联系 seven0x16@163.com 获取商业授权。

- 只通过插件接口与 ChalkLee 交互的插件可以自选许可证，不受 AGPL 约束。
- 内置的待办、日历和插件模板另以 MIT 发布在 [chalklee-plugins](https://github.com/seven0x16/chalklee-plugins)。
- ChalkLee 的名称和标识不随许可证授权。
- 第三方组件保留各自的许可证与声明。

完整条款见 [NOTICE](NOTICE)。

<br>

<div align="center">

<sub>Made for Ms. Lee. Here for Every Teacher.</sub>

</div>
