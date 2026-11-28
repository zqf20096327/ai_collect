<div align="center">

<img src="desktop/build/icon.png" alt="PaperBridge" width="84" height="84" />

# PaperBridge

**开源、本地优先的一体化科研文献工作台**

保版式双语翻译 · 原/译双层划词与手写 · 类 Zotero 文献库 · 全端加密云同步

[![Release](https://img.shields.io/github/v/release/royhang/PaperBridge?color=2563eb&label=最新版本)](https://github.com/royhang/PaperBridge/releases)
[![Android APK](https://img.shields.io/badge/Android-APK%20直装-3ddc84?logo=android&logoColor=white)](https://github.com/royhang/PaperBridge/releases/latest)
[![CI](https://img.shields.io/github/actions/workflow/status/royhang/PaperBridge/ci.yml?label=CI)](https://github.com/royhang/PaperBridge/actions/workflows/ci.yml)
[![Docker](https://img.shields.io/badge/Docker-一键自托管-0ea5e9?logo=docker&logoColor=white)](#docker-一键自托管推荐)
[![License: MIT](https://img.shields.io/badge/License-MIT-10b981.svg)](LICENSE)

[在线体验](https://royhang.github.io/PaperBridge/) · [客户端 / APK / 插件下载](https://github.com/royhang/PaperBridge/releases/latest) · [界面预览](#界面预览) · [Docker 自托管](#docker-一键自托管推荐) · [本地开发](#本地开发与测试)

</div>

![PaperBridge 总览](docs/screenshots/hero-banner.png)

---

## 为什么选择 PaperBridge？

读论文的痛点往往不在于缺少工具，而在于**工作流被切得太碎**：在 Zotero 管题录、用命令行工具翻版式、导进平板做手写批注、再复制段落去网页问 AI——文件来回倒腾，笔记、译文和笔迹分散在各处。

**PaperBridge 将整条科研阅读链路收进同一个开源工作台**：自带 API Key、零订阅费、全端本地优先，并可随时通过局域网或 Docker 私有云实现毫秒级加密同步。

| 能力维度 | **PaperBridge** | Zotero + 翻译插件 | PDFMathTranslate | GoodNotes / MarginNote |
| --- | :---: | :---: | :---: | :---: |
| **保版式双栏全文翻译（公式 / 图表 / 双栏排版）** | ✅ 原生内置，实时双栏对照 | ⚠️ 仅侧栏纯文本 | ✅ 需命令行或单独转换 | ❌ |
| **原文 / 译文双层划词、高亮与手写笔迹** | ✅ 双层独立、互不串位 | ⚠️ 仅原文批注 | ❌ | ⚠️ 无译文与题录联动 |
| **全端覆盖（Web / Win / Android APK / iPad）** | ✅ 全平台 + 手写笔防误触 | ⚠️ 移动端功能受限 | ❌ | ⚠️ 偏重苹果生态 |
| **类 Zotero 嵌套分类 + 整文件夹导入 + 知网插件** | ✅ 支持 GB/T 7714 & CNKI | ✅ 强项 | ❌ | ❌ |
| **多端同步与隐私** | ✅ 私有云 / 局域网 + E2E 加密 | ⚠️ 免费云空间 300MB | ❌ | ⚠️ 依赖商业云 |
| **护眼纸色（白底 / 羊皮纸 / 柔光 / 暗夜）+ AI 问答** | ✅ 开箱即用 + 长文智能检索 | ⚠️ 需拼装多款插件 | ❌ | ❌ |
| **授权与费用** | **MIT 开源 · 自带 Key · 零订阅** | 云存储收费 | AGPL 开源 | 订阅 / 买断 |

---

## 核心特性

![PaperBridge 核心能力全景](docs/screenshots/features-bento.png)

### 1. 保版式双栏全文翻译
- **自研 TypeScript PDF 版面引擎**：原位重排译文，保留原论文公式（含分数线、根号）、图表、页眉页脚与参考文献结构。
- **双栏论文专项优化**：精准处理 IEEE / ACM 双栏栏缝、`\IEEEPARstart` 首字下沉、跨栏标题与作者信息，避免跨栏粘连或漏译。
- **稳定防漏译与导出**：内置并发限流保护（1–3 路可调）、漏句/丢公式自动重试、全文术语自动提取，支持导出「仅译文 / 左右对照 / 双语交替」PDF。

### 2. 舒适阅读体验与原/译双层批注
- **四档护眼纸色**：阅读器工具栏一键切换 **白底 / 羊皮纸 / 柔光 / 暗夜**，配合全局浅色 / 深色主题联动与「沉浸阅读」全屏模式。
- **原文 & 译文双层划词与高亮**：无论在原文页还是译文页选中文字，都会弹出浮动工具栏（翻译、解释、五色高亮、术语、提问、复制）；高亮与临时选区按原/译图层独立保存，笔记点击可自动定位。
- **跨平台手写批注**：原文页与译文页各自拥有独立手写图层，支持 **Apple Pencil / 三星 S-Pen / 华为 M-Pencil / 小米灵感触控笔** 压感、防手掌误触与橡皮擦除。

### 3. 类 Zotero 文献库与学术一键入库
- **高效整理**：无限级嵌套分类树（支持目录搜索、一键折叠、删除分类时可选保留或移出文献）、**拖入/上传整个文件夹自动仅导入 PDF 并还原目录层级**、右键行内快捷重命名、多条件状态筛选、彩色标签、重复条目检测与回收站。
- **浏览器抓取插件（PaperBridge Connector）**：在 **知网（CNKI）、arXiv、IEEE、Nature、ScienceDirect** 等页面一键选分类、打标签入库，支持桌面端本地直连与云服务器直连。
- **完整引用与题录**：支持 DOI / arXiv 自动补全、知网 GB/T 7714 / NoteExpress / EndNote / RIS 批量解析，一键复制 APA / GB/T 7714 引用与导出 BibTeX。

### 4. 全端加密云同步与省钱 AI 精读
- **毫秒级增量同步**：零依赖自托管同步服务（`sync/server.mjs`），增量 Delta + 双向 Gzip 传输，笔记与手写 ~100ms 同步；PDF 按 SHA-256 去重后台传输并按需优先下载，内置**孤儿 PDF 文件自动垃圾回收**防止服务器磁盘膨胀。
- **端到端加密配置**：所有 API Key 在离开设备前使用 **PBKDF2 + AES-256-GCM** 本地加密，服务端永不保存明文密钥。
- **智能 AI 论文问答**：默认「附带全文上下文」并充分命中 Prompt Cache（Claude 自动加 `cache_control`）；面对 **100 页以上学位论文/教材**自动切换本地 **BM25 智能页检索**，也可一键切换「仅当前引用」节省 Token。

---

## 界面预览

### 1. 保版式双栏译文（公式 / 图表完整保留）+ 译文划词工具栏 + KaTeX AI 问答
> 原位重排中文译文，保留矢量架构图、独立公式与行内数学符号；在**译文页**同样可划词弹出翻译 / 解释 / 五色高亮 / 术语 / 提问工具栏，右侧 AI 问答直接渲染 LaTeX 公式并附带全文上下文。

![保版式双栏译文、译文划词工具栏与 KaTeX AI 问答](docs/screenshots/reader-dual-formula.png)

### 2. 羊皮纸护眼模式 + 原/译双层手写批注 + 双层笔记整理
> 一键切换复古羊皮纸底色与协调暖色桌面背景；原文页与译文页拥有独立手写与高亮图层，右侧笔记自动标记「原文 / 译文」来源，点击即定位跳转。

![羊皮纸护眼模式、原译双层手写批注与笔记整理](docs/screenshots/reader-parchment-ink.png)

### 3. 暗夜护眼模式（深色界面 + 暗夜反色 PDF + 划词流式翻译）
> 切换深色模式时 PDF 自动联动柔和暗夜纸张，高亮标注自动切为高对比度屏幕混合模式，划词翻译在左侧持续锁定高亮原句便于左右对照。

![暗夜护眼模式与划词流式翻译](docs/screenshots/reader-dark-dual.png)

### 4. 类 Zotero 7 三栏文献库（浅色 / 深色模式）
> 左侧支持无限级嵌套分类与目录快筛、Zotero 彩色标签；中间提供状态叠加筛选与右键快捷操作（含行内重命名）；右侧即点即看题录详情与一键引用导出。

| 浅色模式（含右键快捷菜单） | 深色模式 |
| --- | --- |
| ![类 Zotero 三栏文献库浅色模式](docs/screenshots/library-light.png) | ![类 Zotero 三栏文献库深色模式](docs/screenshots/library-dark.png) |

### 5. Android APK / iPadOS 移动端全自适应体验
> 同一套工作台原生适配手机与平板：随时浏览筛选文献库，单栏精读羊皮纸或暗夜译文，并支持触控笔防误触与全端加密云同步。

![Android 与 iPadOS 移动端三屏展示](docs/screenshots/mobile-showcase.png)

---

## 全端获取与使用

| 平台 | 获取方式 | 核心特点 |
| --- | --- | --- |
| **Web 网页版** | [在线体验](https://royhang.github.io/PaperBridge/) 或自托管 | 零安装打开即用，数据存本地 IndexedDB |
| **Windows 桌面版** | [Releases 下载 `win-x64.zip`](https://github.com/royhang/PaperBridge/releases/latest) | 免安装解压即用，内置跨域代理与局域网共享 |
| **Android 平板 / 手机** | [Releases 下载 `android.apk`](https://github.com/royhang/PaperBridge/releases/latest) | 原生直装，内置本地代理，支持 S-Pen / M-Pencil / 小米笔 |
| **iPadOS** | Safari 打开 HTTPS / 局域网地址 → 添加到主屏幕 | 全屏 PWA，支持 Apple Pencil 原生防误触与 120Hz 缩放 |
| **浏览器插件** | [Releases 下载 `Connector.zip`](https://github.com/royhang/PaperBridge/releases/latest) | 知网 / arXiv / IEEE / Nature 一键入库 |
| **Docker 私有云** | `docker compose up -d` | 单端口整合 Web + 跨域代理 + 加密云同步 |

### Windows 免安装版（含免 Docker 局域网直连平板）
1. 在 [Releases](https://github.com/royhang/PaperBridge/releases/latest) 下载 `PaperBridge-<版本>-win-x64.zip`，解压后运行 `PaperBridge.exe`。
2. 内置跨域代理与中文字体，支持 `127.0.0.1:23129` 与浏览器插件本地联动。
3. **无服务器同步到 iPad / 安卓平板**：在「设置 → 云同步」一键开启 **「局域网共享」**（默认端口 `8787`），同一 Wi-Fi 下平板打开显示的 `http://192.168.x.x:8787` 即可满速同步并复用电脑代理。

### Android 原生客户端（APK）与 iPadOS
- **Android / 鸿蒙**：直接安装 `PaperBridge-<版本>-android.apk`（Android 8.0+）。内置本地跨域代理（自动复用本机 VPN/Clash），支持在微信、QQ、文件管理器中点击 PDF 直接「用 PaperBridge 打开」，导出文件自动保存到 `下载/PaperBridge`。
- **iPadOS**：在 Safari 打开部署好的 HTTPS 地址（或 Windows 局域网地址），点击「分享 → 添加到主屏幕」即可全屏运行。

### 浏览器抓取插件（PaperBridge Connector）
1. 下载 `PaperBridge-Connector-<版本>.zip` 并解压（或直接使用仓库内的 `extension/` 目录）。
2. 在 Chrome / Edge 访问 `chrome://extensions`，开启「开发者模式」→ 点击「加载已解压的扩展程序」。
3. 在知网、arXiv、IEEE、Nature 等论文页面点击插件图标即可选分类、打标签一键入库。

---

## Docker 一键自托管（推荐）

在任意 VPS、实验室服务器或 NAS 上，一条命令即可在 **单端口（8080）** 同时启动 **Web 前端 + 跨域代理 + 多端加密云同步服务**：

```bash
git clone https://github.com/royhang/PaperBridge.git
cd PaperBridge
docker compose up -d
```

启动后访问 `http://<服务器IP>:8080`（建议前置 Caddy / Nginx / Cloudflare Tunnel 启用 HTTPS，确保 PWA 与端到端加密完整可用）。

- **数据持久化**：所有同步文献与 PDF 原文件均保存在 `./data`（容器内 `/data`），备份该目录即可完整迁移。
- **自动空间清理**：彻底删除文献或清空回收站后，服务端会自动清理无引用的孤儿 PDF 文件，避免磁盘堆积。
- **常用环境变量**（见 [docker-compose.yml](docker-compose.yml)）：
  - `ALLOW_REGISTER=1`：是否开放注册（个人建完账号后设为 `0` 即可关闭公开注册）
  - `INVITE_CODE=`：可选，设置课题组内部注册邀请码
  - `ALLOWED_HOSTS=*`：内置代理允许转发的 API 主机白名单
  - `PROXY_TOKEN=`：可选，代理令牌（登录云同步后前端自动下发）

---

## 支持的模型与翻译服务

| 类型 | 支持服务 | 浏览器直连 |
| --- | --- | :---: |
| **OpenAI 兼容** | OpenAI、DeepSeek、Kimi、通义千问、智谱 GLM、硅基流动、OpenRouter、高校内网接口、Ollama / vLLM / LM Studio | ✅（受 CORS 限制接口自动走代理） |
| **Anthropic** | Claude | ✅ |
| **Google** | Gemini、Google Cloud Translation | ✅ |
| **机器翻译** | DeepL、百度翻译、有道智云 | 需[跨域代理](proxy/README.md)（桌面端 / APK / Docker 内置） |

---

## 本地开发与测试

```bash
pnpm install
pnpm dev          # 启动本地开发服务器 http://localhost:5173
pnpm build        # 构建生产静态站点到 dist/
pnpm proxy        # 单独启动跨域代理 (127.0.0.1:8787)
pnpm sync         # 单独启动云同步服务 (127.0.0.1:8788)
pnpm desktop:win  # 打包 Windows 便携版 → desktop/release/

pnpm lint         # oxlint 静态检查
pnpm test         # 全量前端与版面引擎单元测试
pnpm test:proxy   # 跨域代理测试
pnpm test:sync    # 增量云同步 / 隔离 / 垃圾回收测试
pnpm test:docker  # All-in-One Docker 服务测试
pnpm test:lan     # 桌面端局域网共享测试
```

---

## 致谢与协议

- 保版式译文 PDF 的思路参考了 [PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate)（AGPL-3.0）；本项目基于 TypeScript（`pdf-lib` + 自研内容流解析与版面引擎）完全独立实现。
- 内置中文字体使用 [Noto Serif SC](https://fonts.google.com/noto/specimen/Noto+Serif+SC)（SIL OFL 1.1），构建时自动下载并通过 [HarfBuzz](https://github.com/harfbuzz/harfbuzz) 子集化嵌入 PDF。
- 本项目基于 [MIT License](LICENSE) 开源。
