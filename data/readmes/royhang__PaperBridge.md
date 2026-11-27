<div align="center">

<img src="desktop/build/icon.png" alt="PaperBridge" width="88" height="88" />

# PaperBridge

**专为研究生与科研人员打造的一体化开源文献工作台**
<br/>
**保版式双栏译文 · Apple Pencil 原/译双层手写 · 类 Zotero 文献库 · 知网一键插件 · 毫秒级加密云同步**

[![Release](https://img.shields.io/github/v/release/royhang/PaperBridge?color=2563eb&label=最新版本)](https://github.com/royhang/PaperBridge/releases)
[![CI](https://img.shields.io/github/actions/workflow/status/royhang/PaperBridge/ci.yml?label=CI)](https://github.com/royhang/PaperBridge/actions/workflows/ci.yml)
[![Docker](https://img.shields.io/badge/Docker-一键自托管-0ea5e9?logo=docker&logoColor=white)](#一键-docker-自托管部署推荐)
[![License: MIT](https://img.shields.io/badge/License-MIT-10b981.svg)](LICENSE)

[在线体验](https://royhang.github.io/PaperBridge/) · [Windows 免安装版 & 浏览器插件](https://github.com/royhang/PaperBridge/releases) · [一键 Docker 部署](#一键-docker-自托管部署推荐) · [iPadOS 使用指南](#3-ipados-沉浸阅读与-apple-pencil-双层手写)

</div>

![PaperBridge 多端保版式翻译与 Apple Pencil 双层手写总览](docs/screenshots/hero-banner.png)

---

## 为什么选择 PaperBridge？

研究生读论文最痛的点，往往不是缺工具，而是**工具太割裂**：在 **Zotero** 里管文献，导出到 **PDFMathTranslate** 翻排版，再传到 **iPad GoodNotes** 上手写批注，最后复制段落去 **ChatGPT / DeepSeek** 提问——文件来回倒腾，笔记、笔迹、译文散落四处。

**PaperBridge 把这整条科研阅读链路合而为一，而且完全开源、自带 API 零订阅费、本地优先且支持 Docker 一键私有云同步：**

| 能力维度 | **PaperBridge** | Zotero + 翻译插件 | PDFMathTranslate | GoodNotes / MarginNote |
| --- | :---: | :---: | :---: | :---: |
| **保版式双栏全文翻译（保留公式/图表/IEEE 双栏）** | ✅ 原生内置，双栏实时对照 | ⚠️ 仅侧栏纯文本翻译 | ✅ 需命令行/单独转换 | ❌ 无 |
| **iPadOS + Apple Pencil 原文/译文双层独立手写** | ✅ 原/译双层互不串位 + 防误触 | ⚠️ 仅原文批注 | ❌ 无阅读器 | ⚠️ 无法同步译文与题录 |
| **类 Zotero 嵌套分类 + 彩色标签 + 引用导出** | ✅ 三栏工作台 + GB/T 7714 | ✅ 强项 | ❌ 无文献库 | ❌ 无题录管理 |
| **知网（CNKI）/ arXiv 浏览器一键抓取插件** | ✅ 配套 Connector 扩展 | ✅ Zotero Connector | ❌ 无 | ❌ 无 |
| **Web / Windows / iPad 毫秒级增量云同步** | ✅ Docker 自托管 + E2E 加密 | ⚠️ 免费云空间仅 300MB | ❌ 无同步 | ⚠️ 限苹果生态 |
| **暗夜护眼 PDF 阅读 + AI 论文问答 + 自动术语表** | ✅ 暗夜/柔光纸张 + 省 Token 模式 | ⚠️ 需多款第三方插件拼装 | ❌ 无问答 | ❌ 无 AI 问答 |
| **隐私与费用** | **MIT 开源 · 自带 Key · 零订阅** | 云存储付费 | AGPL 开源 | 订阅/买断 |

---

## 核心能力全景

![PaperBridge 核心功能全景图](docs/screenshots/features-bento.png)

### 五大差异化优势

1. **科研级保版式双栏译文引擎（自研 TypeScript PDF 内容流解析）**
   - 原位替换译文、保留原论文排版、图表、行内公式原字形（含分数线/根号）与参考文献。
   - **专项攻克 IEEE / ACM 双栏论文难题**：精准识别跨栏标题/页脚下的 12pt 栏缝（不跨栏粘连）、自动折叠 `\IEEEPARstart` 首字下沉（不漏译第二行）、保护居中小型大写罗马数字标题与作者栏。
   - 内置并发安全上限（1–3 路可调，默认 3 避免触发 429 限流）、漏句/丢数字/丢公式自动重试、领域术语表自动提取，以及导出「仅译文 / 左右对照 / 双语交替」PDF。
2. **真·iPadOS 生产力：Apple Pencil 原文 & 译文双层手写 + 暗夜护眼**
   - 原文页与译文页拥有**各自独立的手写图层**，双栏对照批注互不串位；压感钢笔、荧光笔、橡皮一应俱全。
   - 针对 Safari 深度实现 **Apple Pencil 原生防手掌误触**（仅 `stylus` 落笔书写，手掌与手指自由滚动、双指捏合缩放），搭配「沉浸阅读」一键隐藏顶栏。
   - **暗夜模式 PDF 护眼纸张**：黑夜模式下 PDF 自动切换柔和暗夜纸张（不再刺眼纯白），并支持阅读器工具栏一键在「自动暗夜 / 柔光暖纸（保留原图色彩）/ 始终暗夜 / 原始白底」间切换，荧光笔在暗底上自动切为高亮混合模式。
3. **贴合国内研究生的类 Zotero 7 文献库 + 知网一键抓取**
   - 无限级嵌套分类树、顶部可叠加状态筛选条（未读 / 在读 / 已读 / 星标 / 有笔记 / 无 PDF）、Zotero 彩色标签、未分类 / 重复条目 / 回收站。
   - 配套 Chrome / Edge 扩展 **PaperBridge Connector**（`extension/`）：在**知网（CNKI）、arXiv、IEEE、Nature** 页面点击图标，选分类、打标签一键入库（同时支持桌面端本地直连与云服务器直连）；支持知网 GB/T 7714 / NoteExpress / EndNote / RIS 批量解析与 `标题_作者.pdf` 自动匹配。
4. **毫秒级增量多端云同步 + 端到端加密**
   - 零依赖自托管同步服务（`sync/server.mjs`）：**增量同步（Delta）+ 双向 Gzip**，画一笔手写/记一条笔记 ~100ms 完成；大体积 PDF 按 **SHA-256 去重**在后台独立队列传输，点开未下载文献时按需优先秒下。
   - API Key 在离开浏览器前即用你的账号密码做 **PBKDF2 + AES-256-GCM 本地端到端加密**，服务器永远不存明文 Key。
5. **灵活省钱的 AI 精读问答与全接口兼容**
   - 划词流式翻译/解释并持续高亮原句；论文问答默认 **「附带全文上下文」**（常规论文全量命中 Prompt Cache，Claude 自动附加 `cache_control`；遇到 **100 页以上博硕论文/教材**自动切换零依赖本地 **BM25 智能页检索**，结合目录/当前页/显式页码引用与高相关页防截断），也可按需一键切换 **「仅当前引用（省 Token）」**。
   - 支持 OpenAI / DeepSeek / Claude / Gemini / 通义 / 智谱 / Kimi / 高校内网接口 / 本地 Ollama / DeepL / 百度 / 有道；Windows 桌面端内置 Chromium Happy-Eyeballs 跨域代理，校园接口零配置直连。

---

## 实拍界面预览

### 保版式双栏全文翻译 + 多文献标签页 + 逐段对照
![保版式双栏全文翻译与多文献标签页](docs/screenshots/reader-dual.png)

### 划词翻译与左侧持续高亮对照
![划词翻译与左侧选区持续高亮](docs/screenshots/reader-select-pin.png)

### 类 Zotero 7 三栏文献库（浅色 / 深色模式）
| 浅色模式 | 深色模式 |
| --- | --- |
| ![类 Zotero 7 三栏文献库浅色模式](docs/screenshots/library-zotero.png) | ![类 Zotero 7 三栏文献库深色模式](docs/screenshots/library-dark.png) |

---

## 一键 Docker 自托管部署（推荐）

只需要一台普通 VPS / 实验室服务器 / NAS，一条命令即可在 **单端口（8080）** 同时启动 **PaperBridge 网页端 + 内置跨域代理 + 多端加密云同步服务**：

```bash
git clone https://github.com/royhang/PaperBridge.git
cd PaperBridge
docker compose up -d
```

启动后访问 `http://<你的服务器IP>:8080`（建议前端套 Caddy / Nginx / Cloudflare Tunnel 开启 HTTPS，以便 iPadOS PWA 与端到端加密正常工作）：

- **数据持久化**：所有同步的 PDF 原文件与用户数据均保存在 `./data` 目录（容器内 `/data`），备份该目录即可完整迁移。
- **常用环境变量**（在 [docker-compose.yml](docker-compose.yml) 中配置）：
  - `ALLOW_REGISTER=1`：是否开放注册（个人注册完账号后可设为 `0` 关闭注册）
  - `INVITE_CODE=`：可选，设置团队/课题组内部注册邀请码
  - `ALLOWED_HOSTS=*`：内置代理允许转发的模型 API 主机白名单
  - `PROXY_TOKEN=`：可选，代理令牌（登录云同步后前端自动下发，无需手填）

---

## 全端使用指南

### 1. Windows 桌面客户端（免安装便携版）
- 在 [GitHub Releases](https://github.com/royhang/PaperBridge/releases) 下载 `PaperBridge-<版本>-win-x64.zip`，解压运行 `PaperBridge.exe`。
- 内置跨域代理（自动兼容系统代理与 IPv4/IPv6，学校接口 / DeepL / 百度 / 有道直连免配置）、内置中文字体、支持本地端口 `127.0.0.1:23129` 与浏览器插件秒级联动。

### 2. 知网 / 学术站一键入库扩展（PaperBridge Connector）
1. 在 [GitHub Releases](https://github.com/royhang/PaperBridge/releases) 下载 `PaperBridge-Connector-<版本>.zip` 并解压（或直接加载仓库 `extension/` 目录）。
2. 在 Chrome / Edge 打开 `chrome://extensions` 开启「开发者模式」→「加载已解压的扩展程序」。
3. 在知网、arXiv、IEEE 页面点击插件图标，选分类打标签一键入库。

### 3. iPadOS 沉浸阅读与 Apple Pencil 双层手写
1. 在 iPad Safari 打开你的 PaperBridge HTTPS 地址，点击「分享 → 添加到主屏幕」。
2. 点击右上角 **「云同步」** 登录同一账号，自动同步全部文献、PDF、笔记、双层笔迹与加密 API 配置。
3. 阅读器工具栏可一键开启 **手写模式**（默认仅 Pencil 防误触）、切换 **暗夜/柔光 PDF 纸张** 与开启 **沉浸阅读模式**。

---

## 支持的 API 服务

| 类型 | 服务 | 浏览器直连 |
| --- | --- | --- |
| OpenAI 兼容 | OpenAI、DeepSeek、Kimi、通义千问、智谱 GLM、硅基流动、OpenRouter、高校接口、Ollama / vLLM / LM Studio 本地模型… | ✅（跨域受限接口可走内置/自建代理） |
| Anthropic | Claude | ✅ |
| Google | Gemini | ✅ |
| 机器翻译 | Google Cloud Translation | ✅ |
| 机器翻译 | DeepL、百度翻译、有道智云 | ❌ 需[跨域代理](proxy/README.md)（桌面端 & Docker 内置免配置） |

---

## 本地开发与测试

```bash
pnpm install
pnpm dev          # 本地开发 http://localhost:5173
pnpm build        # 构建静态站点到 dist/
pnpm proxy        # 单独启动跨域代理（127.0.0.1:8787）
pnpm sync         # 单独启动云同步服务（127.0.0.1:8788）
pnpm desktop:win  # 打包 Windows 免安装版 → desktop/release/

pnpm test         # 全量单元测试
pnpm test:proxy   # 跨域代理测试
pnpm test:sync    # 增量云同步 + Gzip + 隔离测试
pnpm test:docker  # All-in-One Docker 服务冒烟测试
pnpm lint         # oxlint 静态检查
```

## License

MIT

### 致谢

- 「保版式译文 PDF」的思路参考了 [PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate)（AGPL-3.0）；本项目使用 TypeScript（`pdf-lib` + 自研内容流解析与版面引擎）完全独立实现。
- 中文字体：[Noto Serif SC](https://fonts.google.com/noto/specimen/Noto+Serif+SC)（SIL Open Font License 1.1），构建时由 `scripts/fetch-fonts.mjs` 下载并通过 [HarfBuzz](https://github.com/harfbuzz/harfbuzz) 子集化后嵌入 PDF。
