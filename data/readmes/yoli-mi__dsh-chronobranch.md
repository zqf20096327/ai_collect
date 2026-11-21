<div align="center">

# dsh-chronobranch

[![CI](https://github.com/yoli-mi/dsh-chronobranch/actions/workflows/ci.yml/badge.svg)](https://github.com/yoli-mi/dsh-chronobranch/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![DSH](https://img.shields.io/badge/DeepSeek%20Harness-0.2.x-18181b.svg)](https://github.com/deepseek-ai/dsh)

中文 | [English](README.en.md)

</div>

**ChronoBranch** 是面向 **DeepSeek Harness (DSH)** 的原生横向点线时空分支画布插件。  
它直接以原生视图标签 **`时间线`** 挂载在 DSH 会话顶部的 `对话` / `轨迹` 旁，自动跟随 DSH 浅色与深色主题，将长对话、分叉探索、同工作区多对话关联、Agent 执行轨迹与自由悬浮磁贴统一在一个克制清晰的点线画布中。

---

## 核心特性

### 1. 原生「时间线」视图 & 确定性点线泳道
- **零侵入原生挂载**：通过 `conversation.view` 直接注册为 `时间线` 标签页，自动响应 DSH `data-ds-dark-theme` 浅灰白 / 炭黑主题切换。
- **确定性点线排版**：严格从左向右的时间轴与平行泳道，分叉与回流曲线全部沿列间留白通道拐角走线，绝不遮挡正文；支持 **L1 鸟瞰 / L2 点线 / L3 展开** 三档缩放与全文关键字检索。
- **自由拉伸展开对话**：双击节点或点击「展开」原地打开完整 Markdown 对话卡片（支持代码块一键复制、GFM 表格、任务列表），并支持**直接拖拽右侧 / 底部 / 右下角手柄自由缩放卡片尺寸**，整条时间线实时自适应重排。
- **Agent 选择卡片原位呈现**：完整解析并按真实时间顺序穿插渲染 Agent 的 `ask_user_question` 交互提问与选项状态（待回答 / 已回答 / 自定义输入）。

### 2. 共用底部唯一输入框的分支体验
- **不再引入第二套输入框**：在任意已完成轮次点击「分叉」，立即调用 DSH 原生 `sessions.fork({ sessionId, atSeq, increaseTitle: true })` 并通过 `uiWorkspace.openSession` 将 **DSH 底部唯一的完整输入框** 切换至新分支，完整保留模型选择、图片附件、`@` 文件引用、`/` 斜杠命令与审批流。
- **自动隐藏重复前缀**：通过记录分叉截断点 `forkAtSeq`，新分支泳道从分叉点之后干净起笔，不重复堆砌父线历史轮次。
- **底部轨道切换胶囊**：多轨道并存时，通过 DSH 原生 `conversation.input.dock` 在底部输入框正上方提供与输入框等宽的轨道切换胶囊，一键切换发送目标并保持停留在时间线画布且不重置视角。

### 3. 同工作区任意多段对话时间线关联
- 点击右上角 **「关联对话」**，即可勾选同一工作区下的任意数量对话组成共享时间线组（支持传递合并：关联 A–B 与 B–C 后，点开 A / B / C 中任意一个对话的时间线都能同时看到全部时间线）。
- **分支默认关联**：通过 `fork` 创建的分支默认与原对话关联；关联轨道表头支持一键「断开」。

### 4. 微观执行小轴
- 思考推理（Reasoning）、工具调用、终端命令与文件 Diff 默认收敛在展开卡片左下角的 `微观小轴` 触发按钮中。
- 点击后在对话卡片**正下方**向外展开一条点线微观小轴，不挤压对话阅读高度；点击任意步骤可在右侧抽屉查看完整参数、输出日志与红绿 Unified Diff。

### 5. 屏幕磁贴
- 在展开后的对话卡片底部点击 **「磁贴」**，将任意轮次悬挂为 DSH 原生 `shell.overlay` 悬浮磁贴：
  - 切换 `对话` / `轨迹` / `时间线` 或切换左侧会话均不消失；
  - 支持自由拖拽、屏幕边缘与磁贴间自动磁吸对齐、自由缩放、一键并排、`完整 / 仅AI` 切换与一键 `定位` 跳回源轮次。
- 点击磁贴右上角 **「悬浮桌面」**，在 Windows 下通过本地回环宿主（`127.0.0.1:47392`）弹出 100% 无边框、无任务栏图标（`ShowInTaskbar=False`）、始终置顶的原生 WPF 桌面卡片，**即使最小化 DSH 桌面端也依然停留在桌面上**。

### 6. 原生融合 DSH 快捷键设置 & 分支生命周期闭环
- 通过 `@deepseek-ai/dsh-client-shortcuts`（`ctx.shortcuts`）将全部 7 个时间线快捷键直接注册进 DSH 原生 **设置 → 快捷键**，支持原生按键录制、冲突检测、持久化保存与一键恢复默认。
- 支持废案分支一键折叠为细虚线、随时展开、**Cherry-pick 提炼结论回流父线**，以及 Agent 派生（Subagent）泳道统一呈现。

---

## 快速安装

### 方式一：在 DSH 桌面端内一键安装（最简单，推荐）

1. 打开 DeepSeek Harness Desktop，在左侧边栏点击 **「插件」** → **「添加插件」**。
2. 直接粘贴本仓库地址：
   ```text
   https://github.com/yoli-mi/dsh-chronobranch
   ```
3. 点击 **「安装」**，完成后点击 **「立即启用」** 即可生效（无需手动编译）。

### 方式二：本地源码克隆并挂载到 DSH Desktop（适合二次开发）

环境要求：Node.js `>= 20`、pnpm `>= 9`、[DeepSeek Harness (DSH)](https://github.com/deepseek-ai/dsh) Desktop（推荐 `0.2.2+`）。

```bash
git clone https://github.com/yoli-mi/dsh-chronobranch.git
cd dsh-chronobranch
pnpm install
pnpm run install:desktop
```

安装脚本会自动构建 `lib/index.js` 与 `lib/client.js`，并将 `dsh-chronobranch` 以标准组合包（Bundle）形式软链并注册到 `~/.dsh/profiles/desktop/package.json`，在 DSH 的「插件」和「设置」中完整展示中文名称、简介、图标与详情文档。

> **生效方式**：完全退出（含系统托盘）并重新启动 DeepSeek Harness Desktop，打开任意会话即可在顶部看到 **`时间线`** 标签页。

卸载桌面端插件：

```bash
pnpm run uninstall:desktop
```

### 方式三：使用 `dsh` CLI 安装

```bash
# 直接从 GitHub 安装到 desktop profile（网页版可改为 --profile web）
dsh plugin --profile desktop add https://github.com/yoli-mi/dsh-chronobranch
```

---

## 快捷键说明

全部时间线命令均已接入 DSH 原生 **设置 → 快捷键**，可在 DSH 设置中自由修改、清空或重置（以下为无冲突默认键位）：

| 命令 | 默认键位（Windows / Linux） | 默认键位（macOS） |
| :--- | :--- | :--- |
| 时间线 · 展开 / 收起完整对话 | `Ctrl + Alt + Shift + O` | `⌘ + ⌥ + ⇧ + O` |
| 时间线 · 从选中节点拉出分支 | `Ctrl + Alt + Shift + B` | `⌘ + ⌥ + ⇧ + B` |
| 时间线 · 展开 / 收起微观小轴 | `Ctrl + Alt + Shift + M` | `⌘ + ⌥ + ⇧ + M` |
| 时间线 · 悬挂为屏幕磁贴 | `Ctrl + Alt + Shift + T` | `⌘ + ⌥ + ⇧ + T` |
| 时间线 · 鸟瞰 / 点线 / 展开视图 | `Ctrl + Alt + Shift + 1 / 2 / 3` | `⌘ + ⌥ + ⇧ + 1 / 2 / 3` |
| 节点与泳道导航 | `← / →`、`↑ / ↓` | `← / →`、`↑ / ↓` |
| 快捷贴为磁贴 | `Shift + 点击节点` | `Shift + 点击节点` |
| 关闭弹窗 / 抽屉 | `Esc` | `Esc` |

---

## 项目结构

```text
dsh-chronobranch/
├── src/
│   ├── index.ts                      # Node Host 侧入口 & 本地回环桌面磁贴 HTTP 服务
│   ├── host/
│   │   └── wpf-tile-script.ts        # Windows 无边框置顶 WPF 桌面磁贴宿主脚本
│   ├── core/                         # 平台无关的核心渲染与布局层
│   │   ├── types.ts                  # UCGS 统一时空图协议与类型定义
│   │   ├── layout.ts                 # 确定性点线泳道布局引擎与通道拐角走线算法
│   │   ├── ChronoCanvas.tsx          # 交互式点线时间线画布与工作区关联弹窗
│   │   ├── AssistantContent.tsx      # 穿插式 Markdown + Agent 选择卡片渲染器
│   │   ├── markdown.tsx              # 零依赖 XSS 安全 Markdown 渲染器
│   │   ├── icons.tsx                 # 16×16 / 1.5px 定制单色线性 SVG 图标集
│   │   └── styles.ts                 # .cb-* 作用域浅/深双主题样式注入器
│   └── client/                       # DeepSeek Harness 浏览器侧 Cordis 适配层
│       ├── index.tsx                 # conversation.view / input.dock / shell.overlay / shortcuts 注册
│       ├── dsh-adapter.ts            # DSH 会话快照 & 工作区连通分量 -> UCGS 适配器
│       ├── meta-store.ts             # 分支元数据、工作区关联组、回流边持久化存储
│       ├── composer-dock-store.ts    # 底部轨道切换胶囊 & 分叉提示栏状态桥接
│       ├── shortcut-bridge.ts        # DSH 原生 ctx.shortcuts 桥接器
│       ├── tile-store.ts             # 磁贴状态与磁吸定位管理
│       └── TileOverlay.tsx           # DSH 原生 shell.overlay 悬浮磁贴组件
├── scripts/
│   └── install-desktop.mjs           # DSH Desktop 一键挂载 / 卸载脚本
├── cordis.patch.yml                  # Cordis 插件挂载清单
├── tsdown.config.ts                  # Host (ESM) + Client (CJS ModuleLoader) 双端构建配置
└── package.json
```

---

## 本地开发

```bash
pnpm run dev        # 监听源码并实时重新编译
pnpm run typecheck  # TypeScript 类型检查
pnpm run build      # 生成 lib/index.js 与 lib/client.js
```

更多开发约定请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)，版本变更记录请参阅 [CHANGELOG.md](CHANGELOG.md)。

## 开源协议

[MIT License](LICENSE) © 2026 [yoli-mi](https://github.com/yoli-mi)
