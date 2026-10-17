---
layout: doc
permalink: /guide/
---
<div align="center">

<img src="https://guide.rtxk.us/wp-content/uploads/2026/07/f00720e065c237e.jpg" alt="Orca 使用完全指南：一个窗口指挥多个 AI 编程 Agent" width="720"/>

# Orca 使用完全指南 2026 · 一个窗口指挥你的 AI Agent 团队

讲清 **Orca** 到底是什么——它不是又一个 IDE，而是一个把 **Claude、Codex、Antigravity 等多个 AI 编程 Agent** 并排装进同一个窗口的「Agent 指挥舱」：给每个任务开独立 git worktree、无限分屏盯进度、编排层自动分派再合并，最终决策留给你。

![类型](https://img.shields.io/badge/类型-完全指南-1f6feb)
![适用](https://img.shields.io/badge/适用-Orca-0969da)
![更新](https://img.shields.io/badge/更新-2026--07-2ea44f)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

[![完整图文版·含截图](https://img.shields.io/badge/📖_完整图文版·含截图-1f6feb?style=for-the-badge)](https://guide.rtxk.us/tutorial/orca-guide.html)

</div>

---

**🦁 合作推荐 · Leonis AI 中转站 —— 一个端点，抵达所有模型**

[![Leonis AI · 一个端点，抵达所有模型](https://img.shields.io/badge/🦁_Leonis_AI-一个端点，抵达所有模型-F7B441?style=for-the-badge&labelColor=9C5606)](https://i.rtxk.us/i/r37kbkg)
[![免费注册领体验额度](https://img.shields.io/badge/免费注册-领体验额度-9C5606?style=for-the-badge)](https://i.rtxk.us/i/r37kbkg)

**把各家大模型的订阅额度，统一成同一个 API 端点。** 不改代码、不换客户端，只替换一行 Base URL——Claude、GPT、Gemini、Grok、Antigravity 等 **6+ 模型共用一把 `sk-` 密钥**。官方 CLI 原生直连、全程流式不缓冲、后端多账号池调度；邮箱注册几十秒完成，**注册即送体验额度**。

```bash
export ANTHROPIC_BASE_URL=https://你的专属端点
export ANTHROPIC_AUTH_TOKEN=sk-你的密钥
claude
```

OpenAI 兼容客户端（Codex CLI / Cherry Studio / NextChat / OpenAI SDK）Base URL 用 `https://你的专属端点/v1`。

👉 [Leonis AI · 免费注册领体验额度 ↗](https://i.rtxk.us/i/r37kbkg) · [cc-switch 接入教程 ↗](https://guide.rtxk.us/tutorial/ai-coding/leonis-ai-cc-switch-guide.html)

---

> 这份笔记讲清「定位 + 核心机制 + 上手路径」；带高清截图、按界面一步步点的**完整图文版**在[主站教程](https://guide.rtxk.us/tutorial/orca-guide.html)，遇到新版本会在那里持续更新。
>
> ⚠️ **先辨清对象**：本系列说的 Orca，是 **Stably AI 开源**的并行 Agent 开发环境（`github.com/stablyai/orca`）。它**不是** Orca Security（云安全公司）、不是微软的 Orca 小模型、也不是 Orca AI（海事/航运）——这些只是同名，彼此毫无关系。

---

## 目录

- [一、Orca 是什么：不是 IDE，是「Agent 指挥舱」](#一orca-是什么不是-ide是agent-指挥舱)
- [二、为什么多 Agent 玩家离不开它](#二为什么多-agent-玩家离不开它)
- [三、支持哪些 Agent：30+ 一键启动](#三支持哪些-agent30-一键启动)
- [四、三平台安装（mac / Windows / Linux）](#四三平台安装mac--windows--linux)
- [五、首次启动：导入 ~/.claude 与 ~/.codex](#五首次启动导入-claude-与-codex)
- [六、5 分钟跑起你的第一个 Agent](#六5-分钟跑起你的第一个-agent)
- [七、本仓文档导航（Orca 系列）](#七本仓文档导航orca-系列)
- [参考与免责声明](#参考与免责声明)

---

## 一、Orca 是什么：不是 IDE，是「Agent 指挥舱」

很多人第一眼把 Orca 当成「能多开几个代码窗口的编辑器」，其实定位完全不同。

> **Orca 把自己定义为 ADE（Agent Development Environment，智能体开发环境），标语是「Ship 100x With The Agent IDE」。** 它同时服务两类使用者：**你**负责拆任务、观察、拍板，**多个 AI Agent** 在各自隔离的工作区里并行执行。你不是在写每一行代码，而是在**指挥一支 Agent 团队**。

几个关键事实（社区整理，以官方为准）：

| 维度 | 说明 |
| :-- | :-- |
| 定位 | Agent 开发环境（ADE），不是传统 IDE |
| 开源 / 许可 | 开源，**MIT** 许可证 |
| 背景 | 由 Y Combinator 支持，关联公司 Lovecast Inc. / Stably |
| 平台 | **免费**支持 macOS、Windows、Linux |
| 仓库 | `github.com/stablyai/orca`（约 **26.5k** stars） |
| 官网 | `onorca.dev` |

除了「多 Agent 并行」，它还内置了一批贴近实战的能力：**内置浏览器 Design Mode**（在预览里点选 UI 元素，把改动需求直接送给 Agent）、**diff 行上批注**（在某一行 diff 上写要求）、应用内浏览 **GitHub / Linear**、文件可拖给 Agent、内置 **Monaco 编辑器**自动保存。

> 一句话记住它的哲学：**「把任务隔离开，把进度摆到眼前，把最终决策留给你。」**

---

## 二、为什么多 Agent 玩家离不开它

如果你只跑一个 Agent，普通终端也够用。可一旦你想**同时让三五个 Agent 干活**，痛点立刻爆发：分支互相覆盖、终端刷屏找不到北、账号额度打架。Orca 就是冲着这些来的。

- **每个任务一个独立 git worktree**：任务之间物理隔离，谁也别想改乱谁的文件；配上**可无限分屏**的终端并排展示，终端重启还能**保留滚动历史**。
- **Claude 与 Codex 深度集成**：内置**用量与 rate-limit 重置追踪**，账号**热切换无需重新登录**——多号轮换时这一条极省事。
- **完成通知 + 未读状态 + 移动伴侣 App**：Agent 干完会提醒你，离开电脑也能在手机上盯着。
- **SSH Worktree**：Agent 可跑在**远端**机器上，支持自动重连与端口转发，还能预览 Markdown、图片、PDF。

> 换句话说，Orca 解决的不是「怎么写代码」，而是**「怎么同时管好一堆正在写代码的 Agent」**——仓库、分支、终端、账号、进度，全都收拢到一个窗口里。worktree 隔离的原理与实操，见 [worktree 隔离与分屏](docs/worktree-isolation.md)。

---

## 三、支持哪些 Agent：30+ 一键启动

Orca 本身是「指挥舱」，真正干活的是你接进来的各家 Agent。它的 **Agent Picker** 支持 **30 多种** CLI Agent：

| 集成程度 | Agent |
| :-- | :-- |
| **深度集成** | Claude Code、Codex、Cursor CLI；**Antigravity**（可自动配置 hooks 与状态） |
| **可直接接入** | Grok、GitHub Copilot CLI、OpenCode、Gemini、Aider、Goose、Amp、Cline、Kimi、Qwen Code、Devin…… |
| **兜底** | 任何 CLI Agent 都能接 |

> 它的价值在于**统一启动入口 + 转发订阅凭证**：你不用再为每个 Agent 单独配一套环境，选中即用。接入各家 Agent 的登录、权限与账号热切换细节，见 [接入你的 Agent](docs/agents-setup.md)。

---

## 四、三平台安装（mac / Windows / Linux）

| 平台 | 方式 |
| :-- | :-- |
| **macOS** | Homebrew，或按处理器下载 DMG（Apple Silicon / Intel）；安装包已签名公证 |
| **Windows** | 安装程序 `orca-windows-setup.exe`；内置终端可选 PowerShell 或 CMD（多数人用 PowerShell） |
| **Linux** | AppImage 或 deb 包 |

macOS 用 Homebrew 最省事：

```bash
# 安装
brew install --cask stablyai/orca/orca

# 升级
brew upgrade --cask orca
```

非 Homebrew 用户，官方下载入口是 `onorca.dev/download`（历史版本走 GitHub Releases），手机端在 App Store 搜 **Orca IDE**。默认自动跟随 **stable** 通道更新；回退旧版本**不会强制降级** worktree 数据。

---

## 五、首次启动：导入 ~/.claude 与 ~/.codex

第一次打开 Orca，它会请求主目录访问权限，并**主动提议导入** `~/.claude`、`~/.codex` 以及 Ghostty 终端设置——这样你原有的 Agent 配置能平滑迁进来。

> **没有独立账号激活流程**。官方一句话很实在：**「不要把时间浪费在寻找『激活码』上。」** 进入空登录页，直接添加第一个仓库即可开工。

---

## 六、5 分钟跑起你的第一个 Agent

| 步骤 | 操作 | 要点 |
| :-- | :-- | :-- |
| ① **Add** | 侧边栏 → Add Repo | Orca 读取 git 状态，默认分支作为 base ref |
| ② **Worktree** | 点仓库名旁「+」，填任务名、选 start-from ref | 通常用 `origin/main`；名称留空会用**海洋生物**自动命名 |
| ③ **Agent** | 新 worktree 终端下拉框选 Agent | Claude Code / Codex / Antigravity… |
| ④ **Prompt** | 发送**边界清楚、可验收**的任务 | 随时打开 diff 检查 |

进阶玩法：**复制**动作可建立多个 worktree，把**同一句提示词交给多个 Agent 赛马**；拖 worktree 标签到右侧 / 下侧即可分屏；最后**提交并推送胜者，删掉其余**。

权限方面，在 **Settings → Agents → Agent Permissions** 里，全局模式可在 **Yolo**（自动放行）与 **Manual**（逐步确认）之间切换；已配置自定义启动参数的 Agent 不受全局开关影响。

> 三路 Agent 从 add 到 ship 的完整协作链，见 [三 Agent 并行实战](docs/three-agents-parallel.md)；让编排层自动分派再合并，见 [编排 Orchestration](docs/orchestration.md)。

---

## 七、本仓文档导航（Orca 系列）

本仓库把主站 Orca 系列整理成独立、交叉链接的中文文档；每篇都附主站高清图文版：

**入门认知**
- 📖 本页：Orca 使用完全指南 · 主站图文 <https://guide.rtxk.us/tutorial/orca-guide.html>
- 👥 [三 Agent 并行实战：Claude 设计 + Codex 干活 + Antigravity 润色](docs/three-agents-parallel.md)

**核心机制**
- 🌊 [worktree 隔离与分屏：让多个 Agent 互不打架](docs/worktree-isolation.md)
- 🎼 [编排 Orchestration：一句话 fan-out 再自动合并](docs/orchestration.md)
- ⌨️ [CLI 命令全集：让 Agent 自己驱动 Orca](docs/cli-commands.md)

**进阶用法**
- 🎯 [Design Mode 设计模式：点一下页面，UI 改动直达 Agent](docs/design-mode.md)
- 📱 [移动端协作：在手机上盯着上百个 Agent 干活](docs/mobile-companion.md)
- 🔌 [接入你的 Agent：Claude / Codex / Antigravity 登录与热切换](docs/agents-setup.md)

**国内落地**
- 🧭 [国内使用避坑：Agent 访问海外 API、线路选型与账号安全](docs/china-access.md)

> 全部文档索引见 [`docs/`](docs/README.md)。

---

## 参考与免责声明

本仓库是社区整理的 **Orca 中文使用笔记**，与 Orca / Stably AI 官方**无隶属关系**；「Orca」「Claude」「Codex」「Antigravity」「Google」等名称与商标归各自权利人所有。

再次提醒**辨清同名产品**：本文所述 Orca 特指 `github.com/stablyai/orca` 这款开源并行 Agent 开发环境，与 Orca Security（云安全）、微软 Orca 语言模型、Orca AI（海事/航运）等同名主体无关。

文中涉及的功能、star 数、平台支持、安装方式等会随官方版本变动，**凡标注「社区整理 / 以官方为准」处请以官方页面与你的实际版本为准**。使用各家 Agent 涉及账号、订阅与网络，相关操作请在**遵守各平台服务条款**的前提下**自行判断、注意账号安全与信息备份，风险自负**。

图文出处与持续更新：<https://guide.rtxk.us>

<sub>最后更新 2026-07 · MIT License · 文档内容可自由转载，保留出处即可</sub>
