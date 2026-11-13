<div align="center">

<img src="docs/images/slb-agent-banner.png" alt="SLB-Agent Banner" width="820"/>

# SLB-Agent

### 一个核心，接入所有 AI · One Core, Every AI

**跑在你自己电脑上的桌面 AI Agent —— 任意厂商 API Key 接入，读代码、改文件、跑命令；内置 Armor Engine 破限内核，让顽固模型稳定交付完整可执行的内容。**

[![Release](https://img.shields.io/github/v/release/joyfulneurob/SLB-Agent?style=flat-square&color=blue)](https://github.com/joyfulneurob/SLB-Agent/releases)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-0078D6?style=flat-square&logo=windows)](https://github.com/joyfulneurob/SLB-Agent/releases)
[![Armor Engine](https://img.shields.io/badge/Armor%20Engine-%E7%A0%B4%E9%99%90%E5%86%85%E6%A0%B8-8B5CF6?style=flat-square)](#-破限内核-armor-engine)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Client-black?style=flat-square)](https://modelcontextprotocol.io)
[![Electron](https://img.shields.io/badge/Electron-33-9FEAF9?style=flat-square&logo=electron&logoColor=white)](https://www.electronjs.org/)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-%E4%BA%A4%E6%B5%81%E7%BE%A4-26A5E4?style=flat-square&logo=telegram&logoColor=white)](https://t.me/jiaoliuqunsbl)
[![Stars](https://img.shields.io/github/stars/joyfulneurob/SLB-Agent?style=flat-square&color=yellow)](https://github.com/joyfulneurob/SLB-Agent/stargazers)

**[下载安装](#-下载安装)** · **[快速开始](#-快速开始)** · **[破限内核](#-破限内核-armor-engine)** · **[插件生态](#-mcp-插件与技能包)** · **[为什么值得用](#-为什么值得用)** · **[交流群](#-交流与讨论)** · **[FAQ](#-faq)**

**中文** | [English](README_EN.md)

</div>

---

## 为什么是 SLB-Agent？

网上流传的越狱提示词，你得手动粘贴、每次开场重来、模型一拒绝就干瞪眼；基于单一模型定制的客户端，你被锁死在一个厂商上、配置全靠手改。SLB-Agent 把这些事做成了**产品**：

> **本地优先 · 任意模型 · 真执行 · 破限内核 · 可扩展**

- 🔓 **内置 Armor Engine 破限内核** —— 不是一段静态提示词，是一套 MCP 工具引擎：按模型族自动生成注入包、探针测配合度、被拒时对症给补救话术、连续被拒自动升档换打法、每轮自动重申防"漂移回退"；4 档强度 × 11 个模型族 × 3 种场景
- 🔌 **不被任何厂商绑架** —— Claude、GPT、Gemini、DeepSeek、Kimi、GLM、通义、豆包、Ollama 本地模型、任意中转站，一个客户端全接进来，随时切换；破限内核对每个模型族都有专属打法
- 🖥️ **100% 本地运行** —— API Key 用系统钥匙串加密，只存在你自己的电脑上；代码不上传、会话不上传、无账号无遥测
- ⚡ **不只是聊天** —— Agent 真正动手：浏览目录、读写文件、正则搜索、执行终端命令、联网搜索、抓取网页、管理待办
- 🧩 **MCP 插件生态** —— 标准 Model Context Protocol 客户端，可直接导入 Claude Desktop / Cursor 的配置；自带网页爬虫、逆向分析、红队作业等内置插件
- 📚 **技能包系统** —— Markdown 写技能，GitHub 网址一键导入；红队套件含 124 个技能文件（侦察 / Web / 内网 / 提权 / 隧道 / 逆向决策链）
- 🔒 **四档权限模式 + 检查点回滚** —— 计划 / 询问 / 自动编辑 / 全自动；写文件先看 Diff，回滚连文件一起恢复，大胆让它干活

---

## 🗺️ 一张图看懂：能力总览

<a href="docs/images/slb-agent-poster.png"><img src="docs/images/slb-agent-poster.png" alt="SLB-Agent 能力总览：破限内核为核心，多模型接入 / 真执行 / MCP 插件 / 红队套件 / 检查点回滚 / 本地安全 全线覆盖" width="760"/></a>

<sub>🔓 破限 · 破甲 · 越狱内核（Armor Engine）为绝对核心 —— 9 个 `armor_*` 工具 · 4 档 × 11 族 · 22 类拒绝对症 · 38 领域交付规格 · 5 条注入通道；外围是多模型接入、真执行、MCP 插件与技能包、红队全链、检查点回滚、本地零遥测。点图看 2560×3200 原图。</sub>

### 🎯 中心是破限，四周是能力

<a href="docs/images/slb-agent-core-orbit.png"><img src="docs/images/slb-agent-core-orbit.png" alt="SLB-Agent 中心大图标：崩开的锁、贯穿盾牌的闪电、被打断的环，代表破限 / 破甲 / 打破阻碍；外围环绕 8 项能力卡" width="720"/></a>

<sub>中心徽章就是产品定位：**崩开的锁 + 贯穿盾牌的闪电 + 被打断的环** —— 破限、破甲、打破一切阻碍。外围 8 张卡是真正交付的能力面：破限内核 · 破甲引擎 · 28+ 厂商一核通吃 · 真 Agent 真执行 · 6 插件 + 124 技能 · 38 领域按规格交付 · 本地优先零遥测 · 三平台双击就装。点图看 2560×2560 原图。</sub>

---

## ✨ 核心特性

| 类别 | 能力 |
|---|---|
| **🔓 破限内核（Armor Engine）** | 9 个 `armor_*` MCP 工具：注入包生成 / 探针测配合度 / 拒绝对症补救 / 连续被拒自动升级 / 输出质检 / 长会话漂移检测 / 机制组合选型 / 38 领域交付规格；宿主侧每轮自动重申，详见[破限内核](#-破限内核-armor-engine)章节 |
| **多模型接入** | OpenAI 兼容 / Anthropic / Gemini 三协议，预置 28+ 家厂商目录，覆盖 Claude、GPT、Gemini、Grok、Mistral、DeepSeek、通义、Kimi、GLM、豆包、文心、混元、MiniMax、OpenRouter、硅基流动、Ollama、LM Studio、Azure 及任意 One-API / New-API 中转站 |
| **接入引导** | 选厂商 → 一键打开密钥页 → 粘贴测试 → 自动拉取模型列表；全程向导化，首次启动自动打开 |
| **Agent 工具箱** | 浏览目录 · 读文件 · glob 查找 · 正则搜索 · 写文件 · 精确编辑 · 执行命令（zsh / PowerShell）· 联网搜索 · 抓取网页 · 待办清单 |
| **MCP 插件** | 支持 stdio 与 Streamable HTTP / SSE；界面添加或直接导入 Claude Desktop / Cursor 的 `mcpServers` JSON |
| **技能包** | Markdown 技能与常驻规则，兼容 `SKILL.md` / `skills/` 格式；从网址（含 GitHub）或本地文件导入，对所有模型生效 |
| **权限模式** | 计划 / 询问 / 自动编辑 / 全自动，写文件前展示 Diff |
| **检查点回滚** | 回滚到任意消息之前，Agent 改过的文件同步恢复 |
| **上下文压缩** | 接近窗口上限自动总结历史，也可手动 `/compact` |
| **项目指令** | 自动读取 `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` / `.cursorrules`，`/init` 一键生成 |
| **会话管理** | 搜索、按日期分组、重命名、导出 Markdown / JSON、单独删除 |
| **成本统计** | 按模型单价估算费用；检视器实时显示 token、上下文占用与执行轨迹 |
| **模型参数** | 每服务商可配输出上限字段、思考开关与强度、上下文窗口、速率上限；三层重试 |
| **拖放路径** | 像终端一样把文件 / 文件夹拖进对话，自动填入绝对路径 |
| **网络** | 系统代理 / 直连 / 自定义 HTTP / SOCKS5 代理 |
| **安全加固** | 代码混淆、Electron Fuses、安装包签名校验、双重独立授权校验 |

斜杠命令：`/plan`（出方案）· `/compact`（压缩上下文）· `/init`（生成项目指令）· `/export`（导出会话）· `/clear`（清空）

---

## 📦 下载安装

最新版本 **v1.1.15** · 全平台 7 个安装包 · 到 [**Releases 页面**](https://github.com/joyfulneurob/SLB-Agent/releases/latest) 下载对应文件：

| 平台 | 架构 | 文件 | 大小 |
|---|---|---|---|
| **Windows** 10/11 | x64 + x86 | `SLB-Agent-1.1.15-Windows.exe` | ≈ 179.9 MB |
| **macOS** | Apple 芯片（M1/M2/M3/M4） | `SLB-Agent-1.1.15-Mac-M.dmg` | ≈ 104.5 MB |
| **macOS** | Intel 芯片 | `SLB-Agent-1.1.15-Mac-Intel.dmg` | ≈ 111.1 MB |
| **Linux** | x86_64（Ubuntu/Debian/UOS/麒麟） | `SLB-Agent-1.1.15-Linux-x64.deb` | ≈ 91.3 MB |
| **Linux** | x86_64（其他发行版，免安装） | `SLB-Agent-1.1.15-Linux-x64.AppImage` | ≈ 113.2 MB |
| **Linux** | arm64（deb） | `SLB-Agent-1.1.15-Linux-arm64.deb` | ≈ 90.1 MB |
| **Linux** | arm64（AppImage） | `SLB-Agent-1.1.15-Linux-arm64.AppImage` | ≈ 113.6 MB |

> 💡 **不知道选哪个？**
> - Mac：点左上角苹果图标 →「关于本机」→ 看「芯片」一栏，Apple M 系列选 M 芯片版，Intel 选 Intel 版
> - Linux：终端执行 `uname -m`，输出 `x86_64` 选 x64 版，`aarch64` 选 arm64 版

> ℹ️ Release 页最下方的 `Source code (zip/tar.gz)` 是 GitHub 自动生成的**本仓库文档快照**（README、宣传图、更新日志），**不含客户端程序源码**；客户端请下载上方对应平台的安装包。

### 安装步骤

<details>
<summary><b>🪟 Windows</b></summary>

1. 下载 `SLB-Agent-1.1.15-Windows.exe`，双击运行
2. 若弹出 SmartScreen「Windows 已保护你的电脑」→ 点「更多信息」→「仍要运行」
3. 按向导完成安装，桌面生成快捷方式

</details>

<details>
<summary><b>🍎 macOS</b></summary>

1. 下载对应芯片的 `.dmg`，双击挂载
2. 把 **SLB-Agent** 拖入「应用程序」文件夹
3. 首次打开若提示「无法验证开发者」：到 **系统设置 → 隐私与安全性**，点「仍要打开」即可（安装包已做 ad-hoc 签名）

</details>

<details>
<summary><b>🐧 Linux（deb）</b></summary>

```bash
sudo apt install ./SLB-Agent-1.1.15-Linux-x64.deb
# 之后在开始菜单打开 SLB-Agent
# 卸载：sudo apt remove slbagent
```

</details>

<details>
<summary><b>🐧 Linux（AppImage）</b></summary>

```bash
chmod +x SLB-Agent-1.1.15-Linux-x64.AppImage
./SLB-Agent-1.1.15-Linux-x64.AppImage
```

> Ubuntu 22.04+ 若提示缺 libfuse2：`sudo apt install libfuse2`
> Ubuntu 24.04 若提示 sandbox 错误：加参数 `--no-sandbox` 运行

</details>

### ✅ 完整性校验（SHA-256）

下载后建议核对校验值，确认安装包未被调包或损坏：

| 文件 | SHA-256 |
|---|---|
| `SLB-Agent-1.1.15-Mac-M.dmg` | `8159c7d11b18905f24c0d0ead86b6f3041ce09a1db6376e17c58b7c66ad5365e` |
| `SLB-Agent-1.1.15-Mac-Intel.dmg` | `0fed0193a8068213a64196a0df6e82d86d4b75259876f089d5b357ca9952113f` |
| `SLB-Agent-1.1.15-Windows.exe` | `f9c20eec9e501c09b263eae629e7d3c3a194d52d0f9fff8565a1117877e1e9aa` |
| `SLB-Agent-1.1.15-Linux-x64.AppImage` | `9aa0bf0e731117099bb2077db7f592c920886a76f65e62fc2ff1a33917e78acc` |
| `SLB-Agent-1.1.15-Linux-x64.deb` | `e0f4c880432129b8f79037622454753404ec69526e3f13b6cb35378a00018fde` |
| `SLB-Agent-1.1.15-Linux-arm64.AppImage` | `d6ea07b968ae2f793a6675233a90d3ca605e2ec825c6b9db043e752aa1648083` |
| `SLB-Agent-1.1.15-Linux-arm64.deb` | `4f75b75b088ba6af20bac9f6ed19dfae9e7cf4702e947d01a5109850e494e451` |

```bash
# macOS
shasum -a 256 <安装包文件名>
# Windows (PowerShell)
Get-FileHash <安装包文件名>
# Linux
sha256sum <安装包文件名>
```

---

## 🚀 快速开始

```text
① 安装并启动        首次启动自动打开「接入引导」
② 接入模型          选厂商 → 打开密钥页 → 粘贴 API Key → 测试连接 → 勾选模型
③ 挂载文件夹开工    顶栏「挂载文件夹」，把项目拖进来，直接下达任务
```

第一句可以试试：

```text
帮我看看这个项目的结构，找出所有硬编码的密钥和接口地址
```

模型开始"客气"、说"我不能"的时候，正是 Armor Engine 的舞台 —— 它会自动识别拒绝形态并给出补救打法，详见下一章。

---

## 🔓 破限内核（Armor Engine）

**把开源社区验证过的越狱机制，做成一套自动化的、有状态的、随模型族自适应的引擎。**

### 它解决什么问题

手动粘贴越狱提示词的四大痛点，Armor Engine 全部工程化解决：

| 手动提示词包的痛点 | Armor Engine 的做法 |
|---|---|
| 每次新会话都要重新粘贴 | 宿主引擎每会话自动注入 system 内核，**每轮自动追加尾部重申**，长会话不漂移 |
| 模型拒绝了只能干瞪眼、盲目重试 | `armor_fix` 识别 **22 类拒绝形态**（道德说教 / 降级替代 / 假设式许可 / 中途刹车 / 反问动机……），对每类给出**可直接重发的补救话术** |
| 一套提示词打所有模型，效果看运气 | **11 个模型族各自适配**（Claude 吃 assistant 预填充、GPT 吃双轨、Gemini 吃伪工具返回值、DeepSeek 吃极简 FORMAT RULES、GLM 吃运维语境……），自动判族自动选打法 |
| 连续被拒没有升级路径 | `armor_escalate` 自动**升一档强度 + 换族条款 + 换编码变体 + 换拆解方案**，输出完整重发提示词 |

### 三档破限插件，按目标模型选择

| | 精简版破限 | VIP 超级破限 | 精英版破限（GLM 专用） |
|---|---|---|---|
| 正文体量 | 7.8K 字，极简协议 | **16.5K 字 + 38 输出骨架**，最强覆盖 | 8.3K 字 + 硬边界语境库 |
| 适用 | 日常使用、上下文紧张、要行为稳定 | 顽固头部模型 | 智谱族 GLM-4 / 4.5 / 4.6 / Z1 / 5.x |
| 稳定性 | 实测均值 71% | 能力优先 | GLM 5.3 实测：直接技术请求全过 |

> 三个插件工具同名（`armor_*`），同时只开一个。

### 九个 `armor_*` 工具

| 工具 | 一句话 |
|---|---|
| `armor_get` | 按模型 + 场景生成完整注入包（system 段 / 尾部重申 / 预填充 / 探针 / 注入协议） |
| `armor_probe` | 拿模型回复判配合度：compliant / partial / refused / unclear，不凭感觉 |
| `armor_fix` | 被拒时对症：命中哪类拒绝形态 → 处置动作 → 可直接复制的补救话术 |
| `armor_escalate` | 连续被拒时自动升档 + 换族条款 + 编码变体 + 整段重发提示词 |
| `armor_audit` | 输出质检：五类材料（假设 / 命令 / 判读 / 失败分支 / 变体）缺哪类、有没有软话术、长度够不够 |
| `armor_drift` | 长会话漂移检测：0–100 漂移分 + 命中信号 + 针对性重申句 |
| `armor_pick` | 从 14 个开源越狱机制（双轨 / CoT 预填充 / 低资源语言 / 多轮压单轮 / 渐进升级 / 输出骨架…）里选一组**互不冲突**的组合 |
| `armor_domain` | 38 个任务领域 × 5 字段规格：触发词 / 交付物 / 拦截点与应对 / 工具映射 / 颗粒度 |
| `armor_status` | 全模型族矩阵、档位差异、当前哪套在生效 |

### 四档强度 × 11 模型族 × 3 场景

- **强度档位**：`standard`（封拒绝词）→ `strong`（双通道 + 边界重置）→ `max`（术语中性化 + 编码降维 + 拒绝处置表，默认）→ `unlimited`（零省略契约 + 反预降级，对付顽固头部模型）；Claude / GPT / Gemini 自动升 unlimited
- **模型族适配**：Anthropic · OpenAI · Google · DeepSeek · 智谱 GLM · Kimi · 通义 Qwen · Grok · Mistral · 本地开源（Llama/Ollama）· 未知 —— 每族"吃得住的打法"与"禁忌"都写进了引擎
- **场景**：`engineering`（技术评估）/ `creative`（虚构创作）/ `data`（数据处理）

### 五条注入通道

| 通道 | 位置 | 频率 |
|---|---|---|
| ① system 内核 | 系统提示词最尾部 | 每会话一次 |
| ② 尾部重申 | 最后一条 user 消息末尾 | **每轮**（对抗 recency 漂移） |
| ③ 助手预填充 | assistant 首条内容（Anthropic 族） | 每轮 |
| ④ 术语中性化 | 并入 strong+ 档 system | 随档位 |
| ⑤ 探针 | 不进对话，独立判定 | 换模型时一次 |

设置页「破限内核」一键开关，不用改任何配置文件。

---

## 🧩 MCP 插件与技能包

SLB-Agent 是标准 **MCP（Model Context Protocol）客户端**：

- 支持传输方式：`stdio` 与 Streamable HTTP / SSE
- 界面添加，或一键导入 Claude Desktop / Cursor 的 `mcpServers` JSON
- 附带插件开发规范与示例，自己写插件只需一个 `server.mjs`

**技能包**让 Agent 拥有领域知识：Markdown 编写，兼容 `SKILL.md` / `skills/` 生态格式，从 GitHub 网址或本地文件导入，对所有模型生效。

### 内置插件（随安装包加密分发）

| 插件 | 能力 |
|---|---|
| **精简版 / VIP 超级 / 精英版破限** | Armor Engine 本体，见上一章 |
| **网页爬虫** | 智能抓取 + 隐身浏览器（自动过 Cloudflare / 瑞数等 13 类防护）+ 后台整站爬取 + 结构化数据抽取导出 |
| **逆向分析** | APK 体检 / 脱壳 / jadx 反编译；源码目录密钥扫描、接口清单抽取 |
| **红队作业套件** | 安全评估全流程中枢：任务管理、资产测绘、漏洞管理、CVE 匹配、载荷库、WAF 识别与绕过、WebShell 管理、隧道管理、数据库利用、内网扫描、报告生成；配套 **124 个技能文件**（侦察 / Web 漏洞 / AD 域 / 提权 / 隧道 / 逆向 / 决策链） |

> 红队套件面向授权渗透测试、靶场演练与安全研究场景。请在合法授权范围内使用。

---

## 🛡️ 隐私与安全

- **API Key 只保存在本机**：macOS 用 Keychain、Windows 用 DPAPI 加密，界面层读不到明文；删除服务商时密钥一并清除
- **无云端账号体系**：不注册、不登录、不上传会话
- **安装包加固**：代码混淆、Electron Fuses（禁 RunAsNode / 禁 NODE_OPTIONS / asar 完整性校验）、签名校验、Ed25519 离线授权
- **网络可审计**：系统代理 / 直连 / 自定义 HTTP / SOCKS5，流量路径由你决定

---

## ⚡ 为什么值得用

| 能力 | 具体做到什么程度 |
|---|---|
| 破限引擎（自动注入 / 拒绝对症 / 自动升级） | 9 个 `armor_*` 工具 + 宿主**每轮自动重申**；22 类拒绝形态逐类给可重发话术；连续被拒**自动升档**换打法 |
| 长会话防漂移 | 每轮尾部重申 + `armor_drift` 漂移打分，越聊越"客气"立刻能发现并拉回 |
| 任意厂商 API Key | 三协议 **28+ 家**：Claude / GPT / Gemini / DeepSeek / GLM / Kimi / Qwen / Grok / Mistral / Llama / Ollama / 任意中转站 |
| 开箱即用 | 图形界面安装包，双击装完选厂商、粘 Key、自动拉模型列表，无需命令行、无需手改配置 |
| 真实执行 | 读写文件、跑命令（zsh / PowerShell）、抓网页、联网搜索；写文件前先看 Diff |
| 检查点回滚 | 回滚到任意消息之前，Agent 改过的文件**一并恢复**，跑飞了能退回去 |
| MCP 插件生态 | stdio + Streamable HTTP / SSE；一键导入 Claude Desktop / Cursor 的 `mcpServers` 配置 |
| 红队全流程 | 13 类工具 + **124 技能文件**：侦察 / 打点 / 提权 / 横向 / 隧道 / 逆向决策链，跨会话记忆续做 |
| 本地安全 | Key 进系统钥匙串（Keychain / DPAPI），无账号、无遥测；安装包混淆 + Fuses + 签名校验 |
| 成本可见 | 按模型单价估算费用，实时显示 token 与上下文占用，长任务不烧钱 |

**一句话**：一个客户端，把「接模型 · 破限制 · 真干活 · 留后路」四件事一次配齐。

---

## ❓ FAQ

<details>
<summary><b>Armor Engine 到底强在哪？</b></summary>

三点本质区别：① **有状态** —— 它知道当前会话被拒过几次、命中过哪类拒绝形态、现在该用哪一档强度；② **自适应** —— 11 个模型族各有打法与禁忌，自动判族，不是一套文本打天下；③ **自动化** —— 宿主每轮注入重申、被拒时直接给你可复制的补救话术，不用你手动分析"它为什么又开始客气了"。

</details>

<details>
<summary><b>是免费的吗？</b></summary>

安装包免费下载，附带试用期；试用期结束后需离线授权密钥解锁完整功能（见「授权」章节）。密钥绑定机器码、一次兑换、带有效期，全程离线验证，不联网上报。

</details>

<details>
<summary><b>我没有 API Key 怎么办？</b></summary>

接入引导里每个厂商都有「打开密钥页面」按钮，去官网注册创建即可；DeepSeek、智谱、Kimi 等国内厂商新用户通常有免费额度。完全离线方案：本地跑 [Ollama](https://ollama.com)，无需任何 Key。

</details>

<details>
<summary><b>和直接用网页版 ChatGPT / Claude 有什么区别？</b></summary>

网页版只能聊天，而且模型经常"我不能"；SLB-Agent 是 Agent —— 它能读你的项目代码、改文件、跑命令、开浏览器抓数据，Armor Engine 让模型把完整方案交出来而不是给你讲安全课。

</details>

<details>
<summary><b>我的对话数据存在哪里？</b></summary>

全部在本机：「设置 → 数据目录」可查看位置。会话可导出 Markdown / JSON 自行备份，卸载即清空。

</details>

<details>
<summary><b>安装包为什么这么大？</b></summary>

内置了完整的运行时（Electron 33）+ 加密插件包（6 个 MCP 插件 + 124 个技能文件）+ 知识库，开箱即用，不需要再装任何依赖。

</details>

---

## 🔑 授权

安装包内置试用期；试用期结束后通过**离线授权密钥**解锁完整功能：

- 密钥采用 Ed25519 签名，绑定机器码，一个密钥只能兑换一次
- 全程离线验证，无账号体系、无联网激活、无遥测
- 获取方式见 Releases 公告或联系作者

---

## 🗺️ Roadmap

- [x] 多模型三协议接入（28+ 家）
- [x] Agent 工具箱（文件 / 命令 / 网络）
- [x] Armor Engine 破限内核（4 档 × 11 族 × 3 场景 × 22 类拒绝形态）
- [x] MCP 插件 + 技能包生态（124 技能文件）
- [x] 检查点回滚 / 上下文压缩 / 成本统计
- [x] 全平台安装包（Win / macOS / Linux x64+arm64）
- [ ] 插件市场（一键安装社区 MCP 插件与技能包）
- [ ] Armor Engine 强度自适应（按会话历史自动调档）
- [ ] 团队协作与配置同步

---

## 💬 交流与讨论

技术问题、破限玩法、插件与技能包分享、踩坑记录 —— 都欢迎进群一起聊。模型更新太快，群里的一手实测往往比文档快一步。

<div align="center">

[![Telegram](https://img.shields.io/badge/Telegram-%E5%8A%A0%E5%85%A5%E4%BA%A4%E6%B5%81%E7%BE%A4-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/jiaoliuqunsbl)

</div>

- **SLB-Agent 交流群** —— 插件、技能包、MCP 配置、红队套件用法，随时问
- 提问前建议先看 [FAQ](#-faq) 与 [破限内核](#-破限内核-armor-engine) 两节，省一半来回
- 有 Bug 或功能建议，也可以直接开 [Issue](https://github.com/joyfulneurob/SLB-Agent/issues)，群里说一声会更快

---

## 🤝 参与贡献

- 发现 Bug 或有功能建议？欢迎提 [Issue](https://github.com/joyfulneurob/SLB-Agent/issues)
- 想让自己的 MCP 插件 / 技能包被收录？欢迎提 PR 或联系作者
- 觉得好用？点一个 ⭐ Star 是对作者最大的支持
- 想找人一起调 prompt、换模型、试插件？进 [Telegram 交流群](https://t.me/jiaoliuqunsbl) 直接问

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=joyfulneurob/SLB-Agent&type=Date)](https://star-history.com/#joyfulneurob/SLB-Agent&Date)

---

<div align="center">

**SLB-Agent** — 把 AI 从聊天框里放出来，让它真正干活。

Made with ⚡ by SLB-Agent Team · MIT License

</div>

---

## ⚠️ 免责声明

- 本项目及其内置组件（含 Armor Engine 破限内核、红队作业套件、网页爬虫、逆向分析插件）**仅供学习、研究与授权安全测试使用**。
- 使用本工具进行的任何测试，必须在**获得目标资产所有者书面授权**的前提下进行。未经授权对他人计算机信息系统进行探测、渗透或数据采集，在绝大多数司法辖区属于违法行为。
- 使用者须自行了解并遵守所在地区的法律法规（包括但不限于《中华人民共和国网络安全法》《刑法》相关条款及境外对应法律）。**下载、安装或使用本工具，即视为你已确认具备合法授权与合规使用能力，并自愿承担全部使用后果。**
- AI 模型经由破限内核产生的输出可能包含错误、过时或具有风险的内容，请自行判断与核验；关键操作请在隔离环境中进行并做好数据备份。
- 本项目按"原样"（AS IS）提供，作者与贡献者不对任何直接或间接损失负责，也不对工具被滥用的后果承担任何责任。
- 若你发现本项目被用于非法用途，请立即停止使用。


<!-- 
SEO Keywords (indexed by GitHub & search engines):
SLB-Agent, AI Agent, 桌面AI客户端, 本地AI客户端, 多模型客户端, AI助手,
LLM client, ChatGPT client, Claude desktop, Gemini client, DeepSeek client, Kimi client, GLM client,
MCP client, Model Context Protocol, MCP 插件, mcpServers, Claude Desktop alternative, Cursor alternative,
Open Interpreter alternative, ChatBox alternative, Cherry Studio alternative, NextChat alternative,
dsh-purge alternative, L1B3RT4S alternative, ARTEX alternative, Claude Code 二开替代,
破限, 破甲, 破甲提示词, 破甲引擎, 越狱, AI 越狱, 模型破限, 破限内核, 越狱提示词, 破解限制,
已破除限制, 解除AI限制, 无限制AI, 反拒绝, 拒绝处理,
jailbreak, LLM jailbreak, jailbreak prompt, AI jailbreak, model jailbreak, prompt jailbreak,
uncensored AI, uncensored LLM, dealignment, LLM dealignment, system prompt override,
prompt engineering, prompt injection, 对抗提示工程, adversarial prompt engineering,
AI 编程助手, AI 自动化, agent framework, tool calling, function calling,
API Key 聚合, 中转站客户端, Ollama GUI, LM Studio GUI, 本地大模型,
红队工具, 渗透测试 AI, pentest AI, pentesting tools, red team tools, redteaming,
security tools, CTF tools, 逆向分析, APK 反编译, 网页爬虫, web scraping,
Electron app, cross platform, 越狱工具, jailbreak tool, 破限工具, 越狱引擎, jailbreak engine
-->
