<div align="center">

<img src="desktop/assets/icon.png" alt="哲启明思 Logo" width="96" height="96" />

# 哲启明思 · PHILO FM

**离线哲学典藏阅读器 & 微软神经网络电台 & AI 哲思伴读翻译（Windows 桌面端 + Android 移动端）**

*把一座彻底离线、随时可听、可译可问的哲学图书馆，装进电脑与口袋。*

[![License: MIT](https://img.shields.io/badge/License-MIT-1F6F52.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/dadafeiGeorge/zheqimingsi?color=1F6F52&label=Release)](https://github.com/dadafeiGeorge/zheqimingsi/releases/latest)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Android-DF9B48.svg)](#双端特性一览)
[![Library](https://img.shields.io/badge/Books-94%20部原典%20%C2%B7%202920%20万字-B4512A.svg)](#离线哲学典藏书库)
[![AI & Translate](https://img.shields.io/badge/New-AI%20伴读%20%2B%207引擎双语翻译-6F52C8.svg)](#ai-哲思助手与多引擎翻译全新上线)

</div>

---

## 快速下载（开箱即用）

前往 **[GitHub Releases 最新版本](https://github.com/dadafeiGeorge/zheqimingsi/releases/latest)** 直接下载双端安装包，无需配置任何环境：

| 平台 | 文件名 | 大小 | 说明 |
| :--- | :--- | :---: | :--- |
| **Windows x64** | `哲启明思-Windows便携版-新.exe` | ~96.8 MB | 单文件绿色便携，免安装双击即开，全量典籍、字体、AI 伴读与多引擎翻译内置 |
| **Android 7.0+** | `哲启明思-Android.apk` | ~41.5 MB | 轻量单包离线内置，原生前台电台息屏连播 + 原生网络桥接 AI 伴读与双语翻译 |

---

## 项目简介

**哲启明思（PHILO FM）** 是一款离线优先、面向哲学深度研读与沉浸听书体验的跨端开源应用，同时提供 **Windows 单文件便携桌面端**（Electron）与 **Android 原生增强移动端**（Kotlin + WebView + 原生前台媒体服务）。

它内置 **94 部** 精校哲学原典与学术全书（总计 **2,920 万字**）、**383 条**核心哲学术语词典与高压缩离线宋体/楷体字库，零广告、零云端强依赖、开箱即读；并融合 **9 大主题 FM 哲学电台**、**AI 哲思伴读助手** 与 **7 引擎划词/全文双语平行翻译**，配合深夜雨声、壁炉微火、书房棕噪、黑胶底噪等环境白噪音，让思考在桌面精研与移动通勤之间自然延续。

---

## AI 哲思助手与多引擎翻译（全新上线）

### 🤖 AI 哲思伴读与辅助批注
- **多协议模型全覆盖**：内置 **DeepSeek、OpenAI、硅基流动 SiliconFlow、Google Gemini、Anthropic Claude、OpenRouter、本地离线 Ollama** 及任意 OpenAI 兼容接口（OneAPI / NewAPI / 阿里云百炼 / 智谱 / Kimi 等）。
- **原生无跨域流式对话（SSE）**：Windows 端走 Electron 主进程原生流式代理，Android 端走 Kotlin OkHttp 原生流式桥接，彻底规避 CORS 跨域限制，响应实时逐字吐出。
- **阅读上下文深度联动**：阅读中划选任意段落即可呼出 **AI 伴读抽屉**，内置「深度解读」「翻译并解析」「提炼论点」「批判追问」快捷提示词，支持多会话历史与 Markdown 渲染，回答可一键存为书房笔记。
- **AI 一键批注草稿**：在划线批注框中点击 AI 辅助，即可基于所选原典段落自动生成学术批注草稿，编辑后直接保存。

### 🌐 7 引擎划词翻译 & 全文双语平行翻译
- **双模式无缝翻译**：阅读页支持 **划词悬浮即译** 与 **全文双语平行对照翻译**（渐进式小并发翻译、结果自动缓存、切章自动取消，防限流不卡顿）。
- **7 大引擎自由切换**：
  - **在线免密钥即用**：Bing 网页翻译（国内通常直连）、Google 网页翻译
  - **专业官方 API**：Microsoft Azure API、Google Cloud Translation v2 API、DeepL API（Free / Pro，德/法/英学术翻译品质出色）
  - **AI 哲学学术翻译**：调用已配置的大模型进行上下文感知哲学精译
  - **内置零依赖离线翻译引擎**：融合 383+ 跨书德/法/英/希/拉哲学术语辞典 + 高频人文短语与形态还原，断网/飞行模式照常即译，并可选接本地 LibreTranslate 等自建服务自动回退。
- **11 种语言互译**：支持自动检测及简/繁中文、英、法、德、日、韩、俄、西、意、希腊语，设置面板提供延迟测速与一键联调测试。

---

## 界面预览

### Windows 桌面端（学术精读 & 双栏演播室）

| 典藏哲学书馆（宣纸暖白） | 沉浸阅读 · 黑格尔《小逻辑》 |
| :---: | :---: |
| ![桌面端书馆](docs/screenshots/desktop-library.jpg) | ![桌面端精读](docs/screenshots/desktop-reader-paper.jpg) |

| 全屏双栏学术排版（羊皮古卷） | 哲思电台双栏演播室（松烟深墨） |
| :---: | :---: |
| ![桌面端双栏](docs/screenshots/desktop-reader-spread.jpg) | ![桌面端电台](docs/screenshots/desktop-radio-studio.jpg) |

<details>
<summary>点击展开：笔记足迹与 7 日阅读听书统计截图</summary>

![桌面端笔记足迹](docs/screenshots/desktop-notes.jpg)

</details>

### Android 移动端（随身书房 & 息屏连播舞台）

| 移动端典藏书馆 | 松烟深墨夜间阅读 | 黑胶唱盘主舞台 | 随声同步字幕舞台 |
| :---: | :---: | :---: | :---: |
| ![安卓书馆](docs/screenshots/android-library.jpg) | ![安卓夜间阅读](docs/screenshots/android-reader-night.jpg) | ![安卓黑胶电台](docs/screenshots/android-radio-vinyl.jpg) | ![安卓随声字幕](docs/screenshots/android-radio-lyrics.jpg) |

---

## 离线哲学典藏书库

全部文本结构化封装于 [`library-data/`](library-data/)，覆盖 **7 大思想学派**，支持跨全库全文深度检索与本地 `.md` / `.txt` 文稿自由导入：

| 学派分类 | 藏书量 | 代表典籍 / 哲学家 |
| :--- | :---: | :--- |
| **德国古典原典** | 31 部 | 康德《纯粹理性批判》、费希特、谢林、黑格尔《小逻辑》《精神现象学》全系原著与评注 |
| **马克思与批判理论** | 20 部 | 马克思、列宁、卢卡奇、阿尔都塞《读〈资本论〉》、法兰克福学派与批判理论 |
| **张世英哲学全书** | 15 部 | 张世英先生文集全十卷精粹、《哲学导论》、黑格尔专题绎注与述评 |
| **精神分析与后现代** | 12 部 | 拉康、鲍德里亚、巴迪欧、齐泽克等精神分析与当代思想原著 |
| **古希腊与近代哲思** | 8 部 | 笛卡尔《第一哲学沉思集》、莱布尼茨《单子论》、洛克、斯退士希腊哲学批评史等 |
| **现象学与存在哲学** | 5 部 | 海德格尔《德国观念论》、张汝伦《〈存在与时间〉释义》与现代西方哲学 |
| **辞典与术语工具** | 3 部 | 哲学核心术语工具书 + **383 条**即划即查内置词条 |

---

## 双端特性一览

### 核心共通能力
- **四套书房美学主题**：宣纸暖白 / 羊皮古卷 / 青苔护眼 / 松烟深墨，窗口、状态栏与排版一体联动。
- **内置离线精排字体**：内嵌 `LumenSerif`（宋体正/粗）与 `LumenKai`（楷体）精简字库子集，无需系统字体即可呈现纸书排版。
- **跨段落四色划线与批注**：琥珀、茱萸、翠竹、靛青四色标注，选区即可弹出悬浮哲学词典释义（含德/法/希腊原词）。
- **9 大主题哲思电台（FM 88.5 – FM 106.8）**：随书跟读台、古希腊与近代、德国古典原典、马克思与批判、现象学与存在、精神分析后现代、张世英全书台、深夜哲思盲盒、私人节目单；支持微软神经网络主播试听、倍速调节与 5 种环境音混音（纯粹人声 / 深夜雨声 / 壁炉微火 / 书房棕噪 / 黑胶底噪）。
- **笔记足迹 & 金句藏书票**：7 日阅读与听书趋势统计；一键生成**纸本宣纸 / 玄墨黑金 / 博物黛绿**三套典藏金句书票 PNG；支持 **Markdown 笔记导出** 与 **全量 JSON 学习档案备份/恢复**，双端自由迁移。

### Windows 桌面端专属亮点（`desktop/`）
- **单文件绿色便携封装**：免安装双击即开，所有典籍与离线字体完整内置。
- **无边框毛玻璃沉浸视窗**：双重首帧门控彻底消除冷启动白屏闪烁，内置单实例锁防止重复多开。
- **大屏学术精读**：支持精读窄栏 / 经典书页 / 舒展宽栏 / **全屏双栏** 四档排版，`Ctrl+F` 书内秒级全文检索。
- **双栏演播室 & 后台硬件控播**：左黑胶右提词器布局，内置系统托盘菜单、`MediaPlayPause` / `MediaNextTrack` / `MediaPreviousTrack` 全局硬件媒体键控制，并集成 `powerSaveBlocker` 防休眠断播与本地 TTS 音频缓存。

### Android 移动端专属亮点（`android/`）
- **约 41.5 MB 轻量全内置 APK**：地铁通勤、飞行途中彻底零流量畅读。
- **原生沉浸交互**：状态栏与导航栏跟随主题自动变色、冷启动零白屏、实体**音量键翻页**、屏幕常亮、`Haptic Tick` 触感微震反馈与全面屏分级防误触侧滑返回栈。
- **原生 Kotlin 前台媒体服务（`RadioForegroundService`）**：持有 `PARTIAL_WAKE_LOCK` + `WifiLock` + 单一 `AudioFocusRequest` + `MediaSessionCompat`，彻底攻克息屏停播与 WebView 休眠断链；支持锁屏通知栏控制、息屏跨章自动连播、睡眠定时淡出、断点持久化，断网时自动降级系统离线语音兜底。
- **黑胶 ↔ 随声字幕舞台**：轻点一键切换，金句藏书票一键直存系统相册。

---

## 项目架构

```text
.
├── web/                # 前端核心应用（React 18 + TypeScript + Vite + Tailwind CSS）
│   └── src/
│       ├── components/ # LibraryView / ReaderView / RadioStudioView / NotesHubView / AiAssistantPanel / SettingsModals
│       ├── services/   # libraryApi / radioEngine / ambientAudio / aiService / translateService / offlineTranslator
│       └── assets/     # 内置离线字体 LumenSerif & LumenKai (.woff2)
├── desktop/            # Windows 桌面端（Electron 32 无边框窗口 + 本地静态服务 + TTS/AI 原生流式代理 + 托盘/媒体键）
├── android/            # Android 客户端（Kotlin + WebViewAssetLoader + OkHttp 原生流式桥接 + RadioForegroundService）
├── library-data/       # 结构化离线哲学典藏书库（catalog / glossary-index / search-index / 94 部书籍分片）
├── scripts/            # 书库构建、校对、脚注折叠与图标生成脚本
└── docs/screenshots/   # 项目展示截图
```

---

## 本地开发与构建

### 环境要求
- **Node.js** `>= 18`
- **JDK 17 + Android SDK (API 34)**（如需构建 Android APK）
- **Python 3.10+**（如需运行书库处理脚本）

### 1. 启动 Web 开发与构建前端

```bash
cd web
npm install
npm run dev      # 本地开发预览
npm run build    # 构建生产静态资源到 web/dist
```

### 2. 运行与打包 Windows 桌面端

```bash
cd desktop
npm install
npm start            # 本地启动 Electron 桌面端
npm run build:win    # 构建 Windows 便携版（输出到 dist-releases/）
```

### 3. 构建 Android APK

将 `web/dist/` 与 `library-data/` 同步到 `android/app/src/main/assets/web/`（含 `library/` 子目录），随后执行 Gradle 构建：

```bash
cd android
./gradlew assembleRelease
```

---

## 版权与免责声明

- 本项目源代码采用 **[MIT License](LICENSE)** 开源。
- `library-data/` 中的哲学文献整理仅供个人学习、学术研究与技术交流使用。部分近现代译本或著作版权归原著者、译者及出版社所有，请支持正版图书；如涉及版权问题，请通过 Issue 联系，我们将第一时间配合处理。

---

<div align="center">

**桌面沉心精研 · 移动随行聆听**

如果「哲启明思」对你的阅读与思考有所帮助，欢迎点一颗 ⭐ Star！

</div>
