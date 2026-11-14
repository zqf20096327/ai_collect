# 论文伴侣 · Paper Companion

[![Build](https://github.com/zhaoy6859-svg/PaperCompanion/actions/workflows/build.yml/badge.svg)](https://github.com/zhaoy6859-svg/PaperCompanion/actions/workflows/build.yml)
[![Release](https://img.shields.io/github/v/release/zhaoy6859-svg/PaperCompanion)](https://github.com/zhaoy6859-svg/PaperCompanion/releases/latest)
[![License](https://img.shields.io/github/license/zhaoy6859-svg/PaperCompanion)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS%2013%2B-black)](#安装)

**macOS 原生论文精读 App**：左边读 PDF，右边是 AI 伴侣。译文由 XeLaTeX 按原文版式重排，问答支持 Markdown / 公式 / 表格，可接任意 OpenAI 兼容模型（默认 DeepSeek）。

## ⬇️ 直接下载安装

**[下载 论文伴侣 2.3.0（macOS 13+）](https://github.com/zhaoy6859-svg/PaperCompanion/releases/latest)** · DMG 5.9 MB

1. 打开上面的 Release 页面，下载 `PaperCompanion-2.3.0.dmg`
2. 把「论文伴侣」拖进「应用程序」
3. 首次打开若被 Gatekeeper 拦下：右键 →「打开」，或执行
   `xattr -dr com.apple.quarantine "/Applications/论文伴侣.app"`

> 只阅读和问答不需要额外依赖；要让「译文 / 学习报告」排版跑通，需要本机安装 MacTeX 或 TeX Live（`xelatex`）。

觉得有用的话，点右上角 ⭐ **Star** 支持一下，也欢迎邮件交流：**zhaoy6859@gmail.com**

![论文伴侣：大肥鱼欢迎页](docs/welcome.png)

<sub>**English** — Paper Companion is a native macOS app for reading papers: a PDF reader with an AI companion, Markdown/KaTeX chat, and on-demand XeLaTeX typeset translations that keep the paper's page size, margins and columns. Works with DeepSeek (default) and any OpenAI-compatible API. [Download the latest release](https://github.com/zhaoy6859-svg/PaperCompanion/releases/latest).</sub>

## 界面

| 熟悉程度 | 译文（与原文同版式） |
| --- | --- |
| ![熟悉程度](docs/level.png) | ![译文](docs/translation.png) |

| 问答（Markdown / 公式 / 表格） | 模型设置（可接任意大模型） |
| --- | --- |
| ![问答](docs/chat.png) | ![设置](docs/settings.png) |

## 阅读流程

1. 启动后由大肥鱼「论文伴侣」欢迎你；选择 PDF、拖入文件，或继续上次阅读。
2. 伴侣询问你对论文的熟悉程度：完全陌生、了解基础、比较熟悉。解释深度随选择调整，每篇论文独立保存，可随时修改。
3. **默认不自动翻译**：设置目标语言后点「开始翻译」才会发起请求；翻译中可停止、继续或重新翻译。半透明进度浮层显示已完成页数；排版阶段显示独立等待状态。浮层不接收鼠标事件，不阻挡滚动、选字和提问。
4. 完整译文成功编译后进入主阅读区；可导出本地 PDF。排版失败时保留原文，并可导出 TeX 源码。
5. 右侧问答支持 Markdown、数学公式、表格、代码高亮、复制回答/代码。阅读旧回答时新内容不会强制拉回底部。
6. 一键整理交流生成学习笔记，或导出由 LaTeX 编译的学习报告。

## 2.3 的变化

- 不再只接 DeepSeek：设置里可选 DeepSeek（默认）、OpenAI、Anthropic Claude、Google Gemini、通义千问、Moonshot Kimi、智谱 GLM、OpenRouter、硅基流动、本地 Ollama，或任意 OpenAI 兼容服务。
- Base URL 和模型名都可改；每个服务单独保存 Key，切回来不用重填。视觉能力按服务自动开关。
- 伴侣换成同一只「大肥鱼」的九张表情：欢迎、熟悉度、聊天头像、进度、设置和 App 图标分别使用不同姿态。

## 2.2 的变化

- 伴侣形象换成原创的大肥鱼插画，欢迎页、熟悉程度提问、聊天头像与 App 图标统一使用。
- 翻译改为手动触发：打开论文不会产生任何模型请求，点「开始翻译」后才翻译。
- 修好表格排版：宽表格自动缩放到栏宽（两栏模式下不再挤压重叠），并支持模型输出的 `\(...\)` 行内公式与 Markdown 表格。

## 排版与界面

- 原创大肥鱼插画用于欢迎页、熟悉程度提问页、聊天头像、进度、设置和 App 图标。
- 译文连续排版，不再插入“原文第几页”标题或人为逐页换页；通过不可见书签保留原文定位信息。
- 读取源 PDF 的纸张尺寸、估计边距、主要字号、单双栏布局，保留模型输出的标题层级、表格与公式编号。
- 翻译后的文字长度不同，不能逐行逐页复刻原版。单双栏识别为启发式；混合跨栏布局、复杂图表和原图的位置目前不会完整重建。多个原文页合并到一个译文页时，页级定位只取该译文页的第一个来源锚点。
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

常用快捷键：`⌘O` 打开、`⇧⌘R` 框选、`⇧⌘T` 原文/译文、`⇧⌘S` 收起助手、`⌘,` 设置。

扫描版的问答依赖 OCR/视觉能力；超长论文超过全文预算时会提示截断。翻译可停止、继续或重试，缓存按目标语言、提示词和排版版本区分。

## 回归验证

```sh
swiftc Sources/Models.swift Sources/ConversationMemory.swift Sources/ChatEngine.swift tests/ConversationMemoryTests.swift -o /tmp/pc-memory-tests
/tmp/pc-memory-tests
swiftc -framework AppKit -framework PDFKit Sources/Models.swift Sources/ConversationMemory.swift Sources/PaperLayout.swift Sources/TranslationTeX.swift Sources/LearningReport.swift tests/ReadingPDFTests.swift -o /tmp/pc-pdf-tests
/tmp/pc-pdf-tests
swiftc -parse-as-library -framework AppKit -framework WebKit tests/RichTranscriptTests.swift -o /tmp/pc-rich-tests
/tmp/pc-rich-tests
```

`tests/ReaderSwitchTests.swift` 与除 main.swift 外全部源码一起编译，验证译文替换、原文位置恢复和进度层鼠标穿透。UI 测试需可用 macOS 图形会话。可用环境变量 `PAPER_COMPANION_HOME` / `PAPER_COMPANION_PREFS_SUITE` 隔离测试数据，显式设置 `DEEPSEEK_API_KEY=''` 禁用真实模型请求。

资源来源和完整插画提示词见 `Resources/Companion/PROVENANCE.md`；本地网页依赖版本和许可见 `Resources/Chat/THIRD_PARTY.md`。


## 交流

有任何问题、建议，或者想聊聊论文阅读，都欢迎邮件找我：

**zhaoy6859@gmail.com**

也欢迎直接在 GitHub 上提 Issue。

## 开源协议

MIT License © 2026 [zhaoy6859-svg](https://github.com/zhaoy6859-svg)

欢迎提 Issue 和 PR。文字和插画版权归作者所有，代码可自由使用、修改和分发。

如果这个项目帮到了你，点个 ⭐ Star 就是最大的鼓励。
