# 论文伴侣 · Paper Companion

[![Build](https://github.com/zhaoy6859-svg/PaperCompanion/actions/workflows/build.yml/badge.svg)](https://github.com/zhaoy6859-svg/PaperCompanion/actions/workflows/build.yml)
[![Release](https://img.shields.io/github/v/release/zhaoy6859-svg/PaperCompanion)](https://github.com/zhaoy6859-svg/PaperCompanion/releases/latest)
[![License](https://img.shields.io/github/license/zhaoy6859-svg/PaperCompanion)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Windows-black)](#安装)
[![Windows](https://github.com/zhaoy6859-svg/PaperCompanion/actions/workflows/windows.yml/badge.svg)](https://github.com/zhaoy6859-svg/PaperCompanion/actions/workflows/windows.yml)

**论文精读 App（macOS 原生版 + Windows 桌面预览版）**：左边读 PDF，右边是聊天式的 AI 伴侣。macOS 上论文留在原处，收进书房，可以按书架、标题、笔记和提问检索。阅读时有可收起的目录、缩略图和正文查找。提问条贴在论文正下方，是一条细胶囊：加附件、写问题、选推理强度，再发送。问完右侧弹出带头像和时间的对话。还没打开论文也可以先聊，并让伴侣按标题或缩写从书房里打开某一篇。译文用 XeLaTeX 排版，保留纸张尺寸和边距；宽表格跨栏换行，不按坐标重排原图。回答篇幅可以选精简或详细，推理强度另外选择。问答支持 Markdown / 公式 / 表格，可接任意 OpenAI 兼容模型（默认 DeepSeek）。

## Windows 桌面预览版

**[下载 Windows 版 2.5.1](https://github.com/zhaoy6859-svg/PaperCompanion/releases/tag/v2.5.1-windows-beta.1)** · Windows 10/11 x64 · **已在实机演示通过**

- `.exe` 安装程序；`.zip` 解压后运行 `PaperCompanion.exe`
- 同一只伴侣：PDF 阅读、熟悉度、右侧问答、长对话记忆、多语言精翻、LaTeX 学习报告
- 已移植**划线笔记**（页面上高亮、点开写笔记、右侧「笔记」页）和**框选识别**（截图交给视觉模型转写，需开启页面图片，不是离线 OCR）
- 自带 Tectonic 排版引擎与中文字体；首次生成 PDF 需联网下载 TeX 排版资源
- 阅读区与对话区之间可拖动调宽，宽度自动记住
- 修复 `\top` 等常见公式命令导致的「不支持的 LaTeX 命令」；回答结构对齐网页版助手
- API Key 按服务地址隔离；支持只读工具 `get_paper_page`；429/5xx 未输出正文前有限重试并遵守 `Retry-After`，401 不重试，断流保留已生成内容
- 安装包未签名：SmartScreen 提示时选「更多信息 → 仍要运行」，可用 [SHA256SUMS.txt](https://github.com/zhaoy6859-svg/PaperCompanion/releases/download/v2.5.1-windows-beta.1/SHA256SUMS.txt) 校验
- 跨平台数据迁移尚未移植；细节见 [desktop/README.md](desktop/README.md)

## ⬇️ macOS 下载安装

**[下载 论文伴侣 2.3.2（macOS 13+）](https://github.com/zhaoy6859-svg/PaperCompanion/releases/tag/v2.3.2)** · DMG 5.9 MB

1. 打开上面的 Release 页面，下载 `PaperCompanion-2.3.2.dmg`
2. 把「论文伴侣」拖进「应用程序」
3. 首次打开若被 Gatekeeper 拦下：右键 →「打开」，或执行
   `xattr -dr com.apple.quarantine "/Applications/论文伴侣.app"`

> 只阅读和问答不需要额外依赖；要让「译文 / 学习报告」排版跑通，需要本机安装 MacTeX 或 TeX Live（`xelatex`）。

> 上面的 DMG 是 **2.3.2**。书房、可收起的目录和缩略图、正文查找、论文下方的提问胶囊、聊天式对话，以及精简或详细回答都在当前源码里，还没有打进这个安装包。要使用这些功能，克隆仓库后执行 `./build.sh` 和 `./install.sh`。

2.3.1：伴侣回答改为网页版结构（结论 → 原文引用 → 逐符号解释 → 类比/边界，数学强制 LaTeX）；阅读区与对话区可拖动调宽并记住宽度。
2.3.2：API Key 按服务地址绑定，切换 Base URL 不会复用旧服务的 Key（[测试](https://github.com/zhaoy6859-svg/PaperCompanion/blob/main/tests/KeyIsolationTests.swift)）。

觉得有用的话，点右上角 ⭐ **Star** 支持一下，也欢迎邮件交流：**zhaoy6859@gmail.com**

<sub>**English** — Paper Companion is a paper reading app with a native macOS edition and a Windows desktop preview. On macOS, papers stay where they are and collect in a study you can search. The reader has a collapsible outline, thumbnails, and in-document find. The question bar sits under the page: a thin capsule for an attachment, the question, reasoning effort, and send. The answer opens in a chat sidebar with avatars and the clock time. You can talk before a paper is open, and ask the companion to open one from the study by title or acronym. XeLaTeX translations keep the page size and margins, and wide tables span the page and wrap inside their cells. Answer length is concise or detailed, separate from reasoning effort. Works with DeepSeek (default) and any OpenAI-compatible API. The macOS DMG is still 2.3.2; the study and the controls below are on `main`. [Download the latest release](https://github.com/zhaoy6859-svg/PaperCompanion/releases/latest).</sub>

## 界面

下面用三篇示例短文演示，不是真实论文。

**书房。** 论文留在原来的位置。底部的胶囊可以先跟伴侣聊。也可以搜索标题、笔记和提问，或按书架筛选。

![书房：搜索把列表收成一篇，底部是聊天胶囊](docs/study.gif)

**阅读。** 目录和缩略图可以收起。`⌘F` 在正文里查找，并标出每一处。提问条贴在论文下方。

![阅读：收起目录，查找，再看缩略图](docs/reader.gif)

**伴侣。** 右侧是对话：头像、时间和气泡。胶囊上方的「精简 / 详细」决定下一次回答写多长，默认精简。胶囊里的「高」选择推理强度。

![伴侣：论文下方提问，右侧聊天](docs/companion.gif)

## 阅读流程

1. 第一次打开是大肥鱼欢迎页。之后进入书房：拖入论文或文件夹、从 Zotero 导入，或继续上次阅读。论文文件留在原处，书房只记住位置、书架和笔记。
2. 伴侣询问你对论文的熟悉程度：完全陌生、了解基础、比较熟悉。解释深度随选择调整，每篇论文独立保存，可随时修改。
3. 阅读时左侧是目录和缩略图，用 `⇧⌘D` 或目录栏上的箭头收起。`⌘F` 查找正文；在书房里 `⌘F` 则是搜索论文。
4. **默认不自动翻译**：设置目标语言后点「开始翻译」才会发起请求；翻译中可停止、继续或重新翻译。半透明进度浮层显示已完成页数；排版阶段显示独立等待状态。浮层不接收鼠标事件，不阻挡滚动、选字和提问。
5. 完整译文成功编译后进入主阅读区；可导出本地 PDF。排版失败时保留原文，并可导出 TeX 源码。
6. 提问条在论文正下方。右侧对话支持 Markdown、数学公式、表格、代码高亮、复制回答/代码，并显示头像和时间。阅读旧回答时新内容不会强制拉回底部。胶囊上方选择「精简」或「详细」：精简先给结论，大约 400 字；详细把推理、符号和证据边界写完。胶囊里的推理强度默认是「高」，只用于这一次提问。这些选择决定下一次回答，不会改写已经显示的内容。在书房或对话里说「打开某一篇」，伴侣会按标题或缩写在书房里匹配，唯一对上就直接打开。
7. 一键整理交流生成学习笔记，或导出由 LaTeX 编译的学习报告。

## 2.3 的变化

- 不再只接 DeepSeek：设置里可选 DeepSeek（默认）、OpenAI、Anthropic Claude、Google Gemini、通义千问、Moonshot Kimi、智谱 GLM、OpenRouter、硅基流动、本地 Ollama，或任意 OpenAI 兼容服务。
- Base URL 和模型名都可改；每个服务单独保存 Key，切回来不用重填。视觉能力按服务自动开关。
- 伴侣换成同一只「大肥鱼」的九张表情：欢迎、熟悉度、聊天头像、进度、设置和 App 图标分别使用不同姿态。

## 2.2 的变化

- 伴侣形象换成原创的大肥鱼插画，欢迎页、熟悉程度提问、聊天头像与 App 图标统一使用。
- 翻译改为手动触发：打开论文不会产生任何模型请求，点「开始翻译」后才翻译。
- 修好表格排版，并支持模型输出的 `\(...\)` 行内公式与 Markdown 表格。宽表格跨栏，并在单元格里换行。

## 排版与界面

- 原创大肥鱼插画用于欢迎页、熟悉程度提问页、聊天头像、进度、设置和 App 图标。
- 译文连续排版，不再插入“原文第几页”标题或人为逐页换页；通过不可见书签保留原文定位。
- 保留源 PDF 的纸张尺寸和边距，以及模型输出的标题层级、表格与公式编号。只有多数页面都明确分成两栏时才用双栏；拿不准就保持单栏。
- 宽表格跨栏，单元格内换行，不再把整张表缩进栏宽。
- 图不按坐标搬回原位。模型写成 `![图注](figure)` 的图会变成图注，说明原图仍在源 PDF。
- 多个原文页落在同一译文页时，页级定位取该译文页的第一个来源锚点。
- 聊天渲染器随 App 本地打包，不从 CDN 加载。正文经过 HTML 清理，支持浅色和深色外观。

## 公式和长问答

翻译请求可附带该页上下半页高清图；需要支持图片输入的模型才能利用图片核对公式。正文转义，数学经安全检查后交给 XeLaTeX。编译成功并不代表公式识别完全准确，难辨认公式仍需对照原文。

保存全部问答记录。每次请求使用近期完整对话（最多 24 轮、约 24,000 字符预算）和持久化的早期交流摘要；早期历史分批合并摘要。摘要不是逐字记忆，会额外调用模型；摘要失败保留原始记录并提示。

## 模型服务

默认 DeepSeek，开箱即用。设置里可以换成任意 OpenAI 兼容服务：

| 服务 | Base URL | 说明 |
| --- | --- | --- |
| DeepSeek | `https://api.deepseek.com` | 默认，支持图片 |
| OpenAI | `https://api.openai.com/v1` | GPT 系列 |
| Anthropic Claude | `https://api.anthropic.com/v1` | 官方 OpenAI 兼容层 |
| Google Gemini | `https://generativelanguage.googleapis.com/v1beta/openai` | — |
| 通义千问 | `https://dashscope.aliyuncs.com/compatible-mode/v1` | 阿里云百炼 |
| Moonshot Kimi | `https://api.moonshot.cn/v1` | — |
| 智谱 GLM | `https://open.bigmodel.cn/api/paas/v4` | — |
| OpenRouter | `https://openrouter.ai/api/v1` | 一个 Key 用多家模型 |
| 硅基流动 | `https://api.siliconflow.cn/v1` | — |
| 本地 Ollama | `http://localhost:11434/v1` | 无需 Key |

每个服务的 Key 分开保存在本机 `credentials.json`（0600）；换服务不会覆盖原来的 Key。

## 安装与设置

```sh
./build.sh
./install.sh
```

构建需要 macOS、Swift Command Line Tools；PDF 编译需要 XeLaTeX（MacTeX / TeX Live）。安装到 `~/Applications/论文伴侣.app`。当前使用 ad-hoc 签名。

菜单「论文伴侣 → 设置…」配置模型接口和 API Key，支持 OpenAI 兼容服务。Key 保存在本机 `~/Library/Application Support/PaperCompanion/credentials.json`（权限 0600）；旧钥匙串配置会迁移。论文、交流、笔记及译文缓存也保存在本机，不改动原 PDF。

常用快捷键：`⌘O` 打开、`⌘F` 查找正文、`⇧⌘D` 显示或收起目录、`⇧⌘R` 框选、`⇧⌘T` 原文/译文、`⇧⌘S` 收起助手、`⌘,` 设置。目录栏右上角也能收起。论文下方的胶囊可以选择推理强度，上方可以选择「精简」或「详细」回答。

扫描版的问答依赖 OCR/视觉能力；超长论文超过全文预算时会提示截断。翻译可停止、继续或重试，缓存按目标语言、提示词和排版版本区分。

## 回归验证

```sh
./scripts/test.sh
swiftc Sources/Models.swift Sources/ConversationMemory.swift Sources/ChatEngine.swift tests/ConversationMemoryTests.swift -o /tmp/pc-memory-tests
/tmp/pc-memory-tests
swiftc -framework AppKit -framework PDFKit Sources/Models.swift Sources/ConversationMemory.swift Sources/PaperLayout.swift Sources/TranslationTeX.swift Sources/LearningReport.swift tests/ReadingPDFTests.swift -o /tmp/pc-pdf-tests
/tmp/pc-pdf-tests
swiftc -parse-as-library -framework AppKit -framework WebKit tests/RichTranscriptTests.swift -o /tmp/pc-rich-tests
/tmp/pc-rich-tests
```

`tests/ReaderSwitchTests.swift` 与除 main.swift 外全部源码一起编译，验证译文替换、原文位置恢复和进度层鼠标穿透。UI 测试需可用 macOS 图形会话。可用环境变量 `PAPER_COMPANION_HOME` / `PAPER_COMPANION_PREFS_SUITE` 隔离测试数据，显式设置 `DEEPSEEK_API_KEY=''` 禁用真实模型请求。

资源来源和完整插画提示词见 `Resources/Companion/PROVENANCE.md`；本地网页依赖版本和许可见 `Resources/Chat/THIRD_PARTY.md`。


## 学习：这个 App 是怎么搭出来的

从窗口、PDF、流式请求、Markdown/KaTeX 渲染、LaTeX 排版到打包与 CI 的完整拆解，包含 8 个里程碑和 5 个练手改动：[docs/BUILDING.md](docs/BUILDING.md)

## 可靠性与工具调用（Windows 桌面版）

- **Key 按地址绑定**：切换 Base URL 不会复用旧服务的 Key；新地址没有 Key 时直接提示，localhost / Ollama 例外。两个本地模拟服务的端到端验证见 [keys.spec.cjs](https://github.com/zhaoy6859-svg/PaperCompanion/blob/main/desktop/test/keys.spec.cjs)。
- **只读工具 `get_paper_page`**：模型决定是否调用，App 校验页码（整数、1..N）、读取当前论文该页正文并回传，模型再据此回答。测试覆盖正常调用、越界、参数分片和取消：[tool.test.cjs](https://github.com/zhaoy6859-svg/PaperCompanion/blob/main/desktop/test/tool.test.cjs)。
- **失败恢复**：429/5xx/网络错误在尚未输出正文时最多重试 3 次，遵守 `Retry-After` 并做指数退避；401/403 不重试；已经显示正文的断流不自动重放，保留现场并提供「重新生成」。测试见 [reliability.test.cjs](https://github.com/zhaoy6859-svg/PaperCompanion/blob/main/desktop/test/reliability.test.cjs) 与 [desktop.spec.cjs](https://github.com/zhaoy6859-svg/PaperCompanion/blob/main/desktop/test/desktop.spec.cjs)。

以上行为在 Windows/Electron 桌面版实现并随 CI 跑。macOS 原生版已完成 Key 按地址绑定（[KeyIsolationTests.swift](https://github.com/zhaoy6859-svg/PaperCompanion/blob/main/tests/KeyIsolationTests.swift)）；工具调用与重试的移植在计划中。

## 交流

有任何问题、建议，或者想聊聊论文阅读，都欢迎邮件找我：

**zhaoy6859@gmail.com**

也欢迎直接在 GitHub 上提 Issue。

## 开源协议

MIT License © 2026 [zhaoy6859-svg](https://github.com/zhaoy6859-svg)

欢迎提 Issue 和 PR。文字和插画版权归作者所有，代码可自由使用、修改和分发。

如果这个项目帮到了你，点个 ⭐ Star 就是最大的鼓励。
