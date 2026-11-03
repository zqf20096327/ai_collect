# 若道浏览器 · Ruodao Browser

**简体中文** | [English](README.en.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](#支持平台)
[![Electron](https://img.shields.io/badge/Electron-45-47848F.svg)](https://www.electronjs.org/)
[![React](https://img.shields.io/badge/React-19-61DAFB.svg)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.9-3178C6.svg)](https://www.typescriptlang.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

若道浏览器（Ruodao Browser）是一款**开源、跨平台、基于 Electron 与 Chromium 的 AI 桌面浏览器**，面向「边看边问」的日常浏览场景。

它内置若道 AI 侧边栏：登录 ruodao.com 账号（或填入自己的 API Key）即可调用云端模型，对当前网页做总结、解释、翻译、改写与多轮问答。同时它把主流浏览器该有的能力都做到了可用水平——多标签、书签、历史、下载、无痕窗口、页内查找、缩放、主题切换，以及像 Chrome `--user-data-dir` 一样**无限多开相互隔离的浏览环境**。

界面全部用 React 构建，浏览数据默认只保存在本机，不含任何遥测。

![新标签页](docs/screenshots/01-newtab.png)

---

## 目录

- [功能特性](#功能特性)
- [界面预览](#界面预览)
- [支持平台](#支持平台)
- [快速开始](#快速开始)
- [功能教程](#功能教程)
- [独立多开](#独立多开)
- [快捷键](#快捷键)
- [构建与打包](#构建与打包)
- [测试](#测试)
- [技术架构](#技术架构)
- [数据与隐私](#数据与隐私)
- [已知限制与路线图](#已知限制与路线图)
- [贡献](#贡献)
- [许可证](#许可证)

---

## 功能特性

### 浏览与标签页

- 多标签浏览，支持拖拽排序、固定、静音、复制、关闭其他/右侧标签
- 关闭标签恢复（`Ctrl+Shift+T`）、`Ctrl+Tab` 循环切换、`Ctrl+1…9` 快速跳转
- 前进、后退、刷新、强制刷新、停止加载、主页与全屏
- 每个标签页由独立的 `WebContentsView` 承载，外壳与页面视图分离，切换不丢状态

### 智能地址栏

- 输入网址或关键词直接搜索，支持必应、Google、百度、DuckDuckGo 与自定义搜索引擎
- 基于历史记录与书签的地址建议，可键盘上下选择
- 页面加载状态、站点图标与缩放比例提示
- 以 `?` 或 `ai:` 开头可直接向 AI 提问，不触发搜索

### 书签与历史

- 星标收藏（`Ctrl+D`）、书签栏展示、书签管理页搜索与编辑
- 浏览历史自动记录、搜索、单条删除与一键清空
- 书签、历史、下载与设置均提供独立的内部页面（`ruodao://`）

### 下载

- 下载进度、暂停/继续、取消、打开文件与定位所在文件夹
- 下载记录持久化，支持清理记录
- 下载完成提示与工具栏下载弹层

### 若道 AI

- 右侧 AI 侧边栏（`Ctrl+Shift+A`），登录 ruodao.com 账号或使用 API Key，直接调用若道云端模型
- 自动读取模型列表、余额与 API Key；Key 失效时用账号会话自动重建并重试一次
- **页面上下文问答**：可随时开关「阅读此页」，正文截断 12,000 字，选区截断 6,000 字
- 流式输出、停止生成、重试、复制、清空与新建对话；保留最近 40 条消息
- **网页划词工具条**：选中文字即浮出「询问 / 解释 / 翻译 / 改写 / 总结」
- 地址栏以 `?` 或 `ai:` 开头直接提问；新标签页提供「问 AI」入口
- 右键菜单提供「总结此页、翻译此页、提取页面要点」等快捷动作
- 无痕窗口不保存 AI 对话；凭据只存在主进程，优先使用系统加密存储
- 详细设计与接口约定见 [docs/ai-browser.md](docs/ai-browser.md)

### 阅读与工具

- 页内查找（`Ctrl+F`），显示匹配数量并支持上一个/下一个
- 页面缩放（`Ctrl+=` / `Ctrl+-` / `Ctrl+0`），按站点记忆缩放比例
- 打印当前页面、页面右键菜单、图片/链接快捷操作
- 版本信息与开源许可可在应用菜单中查看

### 隐私与个性化

- 无痕窗口使用独立临时会话，不写入历史与下载记录
- **独立多开**：为工作、测试或家人创建完全隔离的浏览器环境，并可生成独立快捷方式
- 跟随系统 / 浅色 / 深色主题，窗口标题栏同步着色
- 启动时打开新标签页或恢复上次窗口；记住窗口位置与尺寸
- 可清除浏览历史与网页缓存

### 安全基线

- 渲染进程启用 `sandbox` 与 `contextIsolation`，禁用 Node.js 集成
- 主进程对 IPC 调用进行来源窗口校验
- 页面跳转与 `window.open` 使用协议白名单，外部协议交给系统处理
- 默认拒绝摄像头、麦克风、定位、通知等权限，仅允许全屏与剪贴板写入

---

## 界面预览

| 网页浏览 | 应用菜单 |
| --- | --- |
| ![网页浏览](docs/screenshots/02-webpage.png) | ![应用菜单](docs/screenshots/03-menu.png) |
| **历史记录** | **设置（深色）** |
| ![历史记录](docs/screenshots/04-history.png) | ![深色设置](docs/screenshots/05-settings-dark.png) |
| **下载内容** | **书签** |
| ![下载内容](docs/screenshots/06-downloads.png) | ![书签](docs/screenshots/07-bookmarks.png) |
| **独立多开环境** | **无痕窗口** |
| ![独立多开环境](docs/screenshots/09-profile.png) | ![无痕窗口](docs/screenshots/08-private.png) |
| **若道 AI 登录** | **AI 对话与页面上下文** |
| ![若道 AI 登录](docs/screenshots/10-ai-panel.png) | ![AI 对话](docs/screenshots/11-ai-chat.png) |

> 以上截图由端到端验收脚本 `npm run smoke` 在真实 Electron 进程中自动生成，随代码同步更新。

---

## 支持平台

| 平台 | 最低版本 | 产物 |
| --- | --- | --- |
| Windows | Windows 10 1809+ | NSIS 安装包、便携版（x64） |
| macOS | macOS 11+ | DMG、ZIP（arm64 / x64） |
| Linux | 主流发行版 | AppImage、DEB（x64） |

运行环境要求：**Node.js >= 22.12**、**npm >= 10**。

---

## 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/ruodaoai/ruodao-browser.git
cd ruodao-browser

# 2. 安装依赖（.npmrc 已配置 npmmirror 的 Electron 镜像，国内可直连）
npm install

# 3. 启动开发模式（热更新）
npm run dev
```

若道 AI 默认连接 `https://ruodao.com`。联调、私有部署或本地 mock 时，可在启动前覆盖网关地址：

```bash
RUODAO_AI_BASE_URL=http://127.0.0.1:8080 npm run dev
```

Windows PowerShell：

```powershell
$env:RUODAO_AI_BASE_URL = "http://127.0.0.1:8080"
npm run dev
```

首次进入应用后，点击工具栏右侧的星芒按钮（或按 `Ctrl+Shift+A`）打开 AI 侧边栏，用 ruodao.com 账号登录即可开始对话。

---

## 功能教程

完整的图文操作教程见：

- 中文：[docs/GUIDE.zh-CN.md](docs/GUIDE.zh-CN.md)
- English: [docs/GUIDE.en.md](docs/GUIDE.en.md)

下面是最常用的三条路径，先跑通它们就能上手。

### 1. 搜索与浏览

![新标签页](docs/screenshots/01-newtab.png)

1. 启动后进入新标签页，顶部地址栏获得焦点
2. 直接输入关键词回车，使用当前默认搜索引擎（新标签页可切换必应 / Google / 百度 / DuckDuckGo）
3. 输入完整网址或带点的域名（如 `github.com`）则直接导航
4. 输入 `?` 开头的内容回车，会把问题发给若道 AI，而不是搜索

「快速访问」区域会根据你的浏览记录自动更新，点击卡片直达。

### 2. 让 AI 读当前网页

![AI 对话](docs/screenshots/11-ai-chat.png)

1. 打开任意网页，按 `Ctrl+Shift+A` 展开右侧 AI 侧边栏
2. 顶部选择模型（模型列表来自若道云端，随账号权限变化）
3. 确认「阅读此页」处于开启状态——状态条会提示已附上当前页面截取
4. 输入问题，或直接点下方的快捷指令：**总结本页 / 提取要点 / 翻译此页 / 解释选中**
5. 回答会流式输出，可随时「停止」「重试」「复制」，或清空后「新建对话」

不确定本次是否要上传网页正文时，关掉「阅读此页」即可，此时只发送你的问题。

### 3. 划词提问

1. 在网页中选中一段文字
2. 选区下方浮出工具条：询问 AI、解释、翻译、改写、总结
3. 点击「询问 AI」只把选文放进输入框，等你补充问题后再发送；其余按钮直接出结果
4. 输入框、可编辑区域内不会触发工具条

---

## 独立多开

每个独立环境使用自己的存储目录，相当于 Chrome 的 `--user-data-dir`：登录状态、Cookie、网站数据、书签、历史、下载记录与设置互不影响，可同时运行任意多个环境。

![独立多开环境](docs/screenshots/09-profile.png)

**在应用内创建**

1. 打开右上角菜单，选择「新建独立浏览器…」
2. 填写环境名称，选择存储目录（默认位于 `文档/若道浏览器环境/`）
3. 勾选「在桌面创建快捷方式」，按需勾选「创建后立即打开」
4. 创建后双击桌面快捷方式，即可在该环境中独立浏览

独立环境的窗口标题与标签栏会显示环境名称，便于区分。同一目录只允许运行一个实例，重复启动会聚焦已有窗口。

**命令行与快捷方式**

打包后的应用可直接通过参数指定环境目录，行为与 Chrome 一致：

```text
"D:\Program Files\若道浏览器\若道浏览器.exe" --user-data-dir="D:\RuodaoProfiles\工作"
```

开发模式下，快捷方式目标需要先指向 Electron 再传入项目目录：

```text
"...\node_modules\electron\dist\electron.exe" "D:\ai\code\ruodao-browser" --user-data-dir="D:\RuodaoProfiles\工作"
```

也可以使用别名 `--ruodao-profile-dir=<目录>`。环境目录中会写入 `.ruodao-profile.json` 记录环境名称；应用内创建时会拒绝复用已有环境目录或包含浏览器数据的目录，避免数据混用。

---

## 快捷键

| 操作 | 快捷键 |
| --- | --- |
| 新建标签页 / 新建窗口 | `Ctrl+T` / `Ctrl+N` |
| 关闭标签页 / 关闭窗口 | `Ctrl+W` / `Ctrl+Shift+W` |
| 恢复关闭的标签页 | `Ctrl+Shift+T` |
| 聚焦地址栏 | `Ctrl+L` / `Ctrl+K` / `F6` |
| 收藏当前页面 | `Ctrl+D` |
| 页内查找 | `Ctrl+F` |
| 历史记录 / 下载内容 | `Ctrl+H` / `Ctrl+J` |
| 书签管理 / 设置 | `Ctrl+Shift+O` / `Ctrl+,` |
| 刷新 / 强制刷新 | `Ctrl+R` / `Ctrl+Shift+R` |
| 放大 / 缩小 / 重置缩放 | `Ctrl+=` / `Ctrl+-` / `Ctrl+0` |
| 无痕窗口 | `Ctrl+Shift+N` |
| 打印页面 | `Ctrl+P` |
| 打开 / 关闭 AI 助手 | `Ctrl+Shift+A` |
| 切换标签页 | `Ctrl+Tab` / `Ctrl+Shift+Tab` |
| 前进 / 后退 | `Alt+→` / `Alt+←` |
| 全屏 | `F11` |

macOS 上对应的修饰键为 `Cmd`，无痕窗口为 `Cmd+Shift+N`。

---

## 构建与打包

```bash
npm run build        # 类型检查 + 生产构建
npm run pack:dir     # 生成未压缩的应用目录，便于本地验证
npm run dist:win     # Windows: NSIS 安装包 + 便携版
npm run dist:mac     # macOS: DMG + ZIP
npm run dist:linux   # Linux: AppImage + DEB
```

构建产物输出到 `dist/`。应用图标由 `build/icon.png` 提供，可运行 `npm run icon` 从品牌 SVG 重新生成。

---

## 测试

端到端验收脚本会构建应用、启动真实的 Electron 进程，覆盖新标签页、地址栏导航、书签、查找、缩放、菜单、内部页面、下载、标签页与无痕窗口，并输出截图到 `docs/screenshots/`。脚本内置一个本地 mock ruodao.com，同时验证登录、自动创建 API Key、模型列表、SSE 流式回答、页面上下文开关、划词工具条与 401 自动重建重试：

```bash
npm run smoke
```

独立多开专项验收会同时启动多个环境，验证目录与 Cookie 隔离、单实例复用、快捷方式生成及创建后自动启动：

```bash
npm run smoke:profiles
```

单独的静态检查：

```bash
npm run typecheck
```

---

## 技术架构

```
┌────────────────────────────────────────────────────┐
│ 主进程 (Node.js)                                   │
│  BrowserApp · BrowserWindowController             │
│  AiService · RuodaoClient · ProfileStore · IPC     │
└───────────────┬────────────────────┬───────────────┘
                │ IPC (preload)      │ WebContentsView
┌───────────────▼──────────┐  ┌──────▼───────────────┐
│ 浏览器外壳 (React)       │  │ 页面视图 (Chromium)  │
│  标签栏 · 地址栏 · AI 侧栏│  │  普通/无痕分区       │
│  查找栏 · 下载弹层       │  │  内部页面 + 划词工具条│
└──────────────────────────┘  │  设置/历史/书签/下载 │
                              └──────────────────────┘
```

- 浏览器外壳本身是一个 `BrowserWindow`，每个标签页对应一个 `WebContentsView`，主进程根据外壳头部高度统一布局
- `ruodao://` 自定义协议为外壳与内部页面提供静态资源，普通与无痕会话分别注册
- 打开弹出菜单时对外壳下方的页面截图并临时隐藏视图，避免原生视图遮挡浮层
- 数据由 `ProfileStore` 统一持久化到 Electron `userData/profile.json`；无痕会话使用独立内存分区
- `AiService` 在主进程管理凭据、模型列表、页面上下文与 SSE 流；渲染进程只通过受限 IPC 收发事件
- 网页 preload 在 `http/https` 页面注入 Shadow DOM 划词工具条，只上报「动作 + 选区文本 + 页面标题/URL」，不向网页暴露 Node.js 或凭据能力

**技术栈**：Electron 45 · Chromium · React 19 · TypeScript 5.9 · Vite 7 · electron-vite · electron-builder · Playwright · ruodao.com 开放平台 API（SSE）

### 目录结构

```
src/
  main/          主进程：窗口、标签、导航、数据、下载、IPC、协议
  preload/       隔离预加载脚本（外壳 / 内部页面）
  renderer/
    chrome/      浏览器外壳 React 应用
    pages/       新标签页、设置、历史、书签、下载、错误页
    shared/      品牌组件与主题样式
  shared/        共享类型与常量
scripts/         图标生成与端到端验收脚本
build/           打包图标
docs/            截图、设计文档与使用教程
```

---

## 数据与隐私

- 浏览器不包含遥测，浏览数据默认只写入本机 `userData` 目录
- 只有在你主动登录并使用若道 AI 时，浏览器才会把本次提问与所需的页面上下文发送到 ruodao.com；关闭「阅读此页」后不发送网页正文
- ruodao.com 登录会话与 API Key 只保存在主进程，优先使用 Electron `safeStorage` 加密，退出登录即删除
- 每个独立环境的数据分别写入各自的 `--user-data-dir` 目录，环境之间不共享登录状态与浏览记录
- 无痕窗口使用临时会话，关闭窗口后该会话的 Cookie、缓存与记录即被清除
- 应用本身不请求摄像头、麦克风、定位与通知权限，网站权限默认拒绝
- 清除浏览数据可在「设置 → 隐私与数据」中执行

---

## 已知限制与路线图

当前版本为 `0.1.0`，仍处于早期阶段。

**已知限制**

- 若道 AI 需要 ruodao.com 账号或 API Key，模型与额度由若道开放平台管理
- AI 当前只处理文本，暂不支持图片/PDF/附件、跨标签页批量总结与网页自动操作
- 暂不支持浏览器扩展、账号同步、自动更新与内置广告拦截
- 未提供代码签名与公证，正式分发前请按平台要求补充签名流程
- 安全能力沿用 Chromium 默认站点隔离与沙箱模型，未做额外的企业级策略加固
- 独立环境暂不提供管理器页面，删除环境需退出对应实例后手动移除目录与快捷方式

**路线图**

- [ ] 图片 / PDF / 附件理解与截图提问
- [ ] 跨标签页批量总结与对比
- [ ] 页面内自动操作 Agent（填表、点击、结构化提取）
- [ ] 对话历史列表、搜索与导出
- [ ] 独立环境管理器页面
- [ ] 浏览器扩展支持与账号同步
- [ ] 团队策略：模型白名单、额度上限、审计日志

---

## 贡献

欢迎提交 Issue 与 Pull Request。开始之前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，安全问题请按 [SECURITY.md](SECURITY.md) 的方式私下报告。

- 功能建议 / Bug 反馈：请附上系统版本、复现步骤与截图
- 提交代码：从 `main` 拉分支，保持单个 PR 只解决一个问题，并跑通 `npm run typecheck` 与 `npm run smoke`
- 文档与翻译：欢迎补充教程、修正中英文表述

## 许可证

[MIT](LICENSE) © 2026 Ruodao Browser Contributors

若道浏览器是开源软件，可自由用于商业与非商业场景。若道 AI 服务本身由若道开放平台提供，受其服务条款约束。
