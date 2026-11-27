# Antigravity Hub

**简体中文** | [English](./README.en.md)

**专为 Google Antigravity 打造的模块化原生控制中心（MCP App）：集上下文监控与累计用量统计、本地代码审查、生态治理与场景预设、本地壁纸引擎、零依赖界面汉化于一体**

[![Version: v1.6.0](https://img.shields.io/badge/Version-v1.6.0-0ea5e9.svg)](https://github.com/Horikita-9-Suzune-Max-Ultrafast/antigravity-hub/releases/tag/v1.6.0)
[![Antigravity 2.35.2 Update Verified](https://img.shields.io/badge/Antigravity%202.35.2-Update%20Verified-10b981.svg)](#实测验证官方更新防破坏实录)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Node.js >= 24](https://img.shields.io/badge/Node.js-%3E%3D24-339933.svg)](https://nodejs.org/)
[![Zero Runtime Deps](https://img.shields.io/badge/Runtime%20Deps-0-brightgreen.svg)](#架构与设计原则)

> **核心承诺**：实时监控与面板交互 **0 模型 Token 消耗** ｜ **绝不向业务代码仓库写入任何缓存文件** ｜ **零第三方运行时依赖（无 `node_modules`）** ｜ **直面 Antigravity 官方更新实测零损通关，支持一键无损还原**

---

## 快速导航

- [五大核心模块一览](#五大核心模块一览)
- [实测验证：官方更新防破坏实录](#实测验证官方更新防破坏实录)
- [v1.6.0 新版亮点](#v160-新版亮点)
- [零门槛快速上手（3 步解压即用）](#快速开始)
- [核心功能详解](#核心特性)
- [架构与安全设计](#架构与设计原则)
- [命令行工具（CLI）](#命令行工具cli)
- [升级、卸载与一键还原](#升级卸载与一键还原)
- [常见问题（FAQ）](#常见问题faq)
- [目录结构](#目录结构)

---

## 五大核心模块一览

**Antigravity Hub** 采用响应式双形态外壳——宽屏（`> 680px`）自动展示 `56px` 左侧图标导航栏，窄屏（`<= 680px`）自动折叠为顶部紧凑 5 模块切换条，支持 **简体中文 / English 免刷新实时切换**。

| 模块 | 解决什么痛点 | 核心能力 |
| :--- | :--- | :--- |
| **1. 上下文监控与记忆库**<br>`Context Cache & Monitor` | 对话变慢、缓存莫名击穿、上下文被什么占满看不清、跨会话累计消耗没总账 | 上下文 6 维构成透视、**跨会话累计用量统计看板（今日/24h/7d/30d/全部 + 人民币/美元）**、已挂载资产点击穿透检视、异常预警一键跳步骤、主/子 Agent 实时纯解码 TPS 与 TTFT、**Win32 原生 120fps 透明悬浮球与共享焦点连续形变迷你条**、统一药丸风格 Gemini KV 倒计时、三源交接胶囊 |
| **2. 本地代码审查**<br>`Local Code Review` | 提交前漏掉硬编码密钥/冲突标记/空异常、手动跑 lint/test 繁琐、AI 审查容易污染主对话上下文 | 零依赖 Git Diff 解析（未提交/已暂存/最近提交/分支对比）、**8 条 L1 毫秒级静态安全与质量预检**（仅扫新增行）、原生工程门禁白名单探测与手动触发（lint/typecheck/test/ruff/mypy/cargo/go）、**L2 隔离 Subagent 深度审查闭环与勾选一键修复**、忽略持久化与 20 份历史报告 |
| **3. 生态治理与场景预设**<br>`Ecosystem & Harness Governance` | 插件/MCP 装多了拖慢每次对话，切场景要手动一个个开关且容易误关核心插件 | Effective Harness 全景栈（P1 工作区 → P4 内置）、**4 支柱连续递减健康评分**（上下文/安全/卫生/完整性）、离线三合一体检与分层修复闭环、多信号智能分类 + 可勾选场景预设、常驻核心保护、不可变快照时间机器 + CLI 回滚 |
| **4. 本地壁纸引擎**<br>`Appearance & Wallpaper` | 默认界面偏素，想要清爽顺眼的个人壁纸且不想重打包破坏客户端 | 零新增 ASAR 侵入点热加载、外置本地壁纸库（15 MiB 熔断）+ 100% 只读本地文件夹扫描、轮播池子集与双缓冲淡入淡出、滑块实时调参（不透明度/模糊/饱和度/遮罩/毛玻璃）、深浅主题独立绑定、一键秒关与 CLI 急救 |
| **5. 零依赖界面汉化**<br>`Antigravity Localization` | 原生界面全英文、高频设置与菜单不直观，担心第三方汉化误翻代码或升级冲突 | 纯 Node.js 流式 ASAR 补丁引擎（维护 4 MiB SHA-256 校验）、739+ 精校内置词条（原生菜单 + 动态界面 + 正则模板）、三层词典外置热加载、代码块/终端/路径物理免疫防误翻、真实 `app.asar` 版本防降级护栏与一键无损还原 |

---

## 实测验证：官方更新防破坏实录

使用客户端增强类插件，大家最担心的往往不是功能够不够多，而是**「下次 Antigravity 官方一更新，会不会把客户端改崩、锁死安装器、丢数据或把旧版备份误还原回去？」**

我们在真实生产环境中，刻意保持 **「ASAR 界面汉化已开启 + 本地壁纸已开启 + 原生悬浮窗运行中」** 的全开实战态，**不卸载插件、不提前还原原版**，连续经历官方原地升级至 **Antigravity `2.35.1` → `2.35.2`**（Electron `44.9.1`），对全链路进行了 6 维实测验收：

| 防破坏验收项 | 实测结果 | 真实链路表现 |
| :--- | :---: | :--- |
| **1. 原地升级防锁死与零孤儿进程** | **PASS** | 官方安装器平滑覆盖 `app.asar` 并以 `--updated` 完成冷启动，无白屏、无文件锁阻塞；升级重启后旧宿主进程自动退出，系统仅保留唯一健康 `language_server` → MCP Server → Win32 原生 WebView2 悬浮窗进程树 |
| **2. 外置真相源 100% 零丢失** | **PASS** | 升级前后逐项核验：Vault 记忆库（217/217）、SQLite 派生调用索引（2840/2840）、个人配置与配额校准、激活词典（1972 条）及本地壁纸库与轮播计划全部无损保留 |
| **3. 新版干净 `.bak` 自动刷新与防降级** | **PASS** | 升级后自动识别 `outdated_after_update` 与真实版本 `2.35.2` 并拦截旧版备份降级；重新应用汉化时先以 `2.35.2` 原版（`current_clean_asar`）刷新 `app.asar.agy-console.bak`，完整注入 `dist/main.js` 与 `dist/preload.js` 且支持一键无损还原 |
| **4. 本地壁纸免重配自动回归** | **PASS** | 壁纸引擎零新增 ASAR 侵入点；重打汉化后原有图库、轮播计划、透明度/模糊/遮罩/毛玻璃参数直接自动恢复，无需重新选图 |
| **5. Hook、Transcript 与原生 DB 兼容** | **PASS** | `SessionStart` 简报、`PreInvocation`/`PostInvocation` 计时、`transcript_full.jsonl` 及原生 `conversations/<id>.db`（纳秒级 TTFT / 纯解码 TPS）开箱即通；`ctx_doctor` 实测 `HEALTHY`、Schema 漂移 `0`、熔断器 `CLOSED (0/3)` |
| **6. 生态治理完整存活与回归全通** | **PASS** | 升级后全部插件、MCP、Skills、Rules 与 Hooks 挂载完好（0 错误 / 0 密钥泄露），21 个测试文件 **86 项自动化测试全部通过** |

> 即使未来 Antigravity 某次大版本改动了内部字段，Hook 也会自动 Fail-Open 返回 `{}`、脱敏录制 `schema-drift.jsonl` 并在连续 3 次异常后熔断，绝不拖慢或卡死主对话；终端运行 `ctx doctor --repair` 即可无损重建索引与复位状态。

---

## v1.6.0 新版亮点

如果你是从旧版本升级或刚了解本项目，以下为 `v1.6.0` 核心大版本升级内容：

- **全新第 5 一级模块：本地代码审查（v1.6.0）**：纯 Node.js 零依赖 Git Diff 解析引擎（支持 `未提交 / 已暂存 / 最近提交 / 分支对比`，自动折叠 lockfile/dist/二进制）；内置 8 条 L1 毫秒级确定性安全与质量规则（仅扫描新增行，杜绝历史旧代码误报）；支持白名单探测并手动执行项目原生门禁（`lint / typecheck / test / ruff / mypy / cargo / go vet`）；提供 L2 隔离 Subagent 深度审查 Prompt 构造、报告落盘导入与勾选发现项一键生成精准修复指令。
- **跨会话累计用量统计看板（v1.6.0）**：在「监控」页新增 **「统计」** 标签（`上下文 / 明细 / 统计 / 记忆库`），基于本地 SQLite 全历史调用库提供 `今天 / 24 小时 / 7 天 / 30 天 / 全部` 时段筛选与模型筛选；一屏呈现累计 Token（含输入/输出/缓存拆分）、请求次数、按时区默认人民币 `¥` 并可一键切换 `¥ / $` 的估算费用、缓存命中率进度条、加权纯解码速度 & 首字平均 TTFT 以及按模型明细。
- **Win32 原生 120fps 透明悬浮球、共享焦点连续形变与编译缓存（v1.6.0）**：悬浮窗宿主升级为本地 `.NET 4 csc.exe` 编译缓存（`floating-host-<hash>.exe`，命中缓存 `< 5ms` 启动），支持原生 60–240Hz DWM 拖拽缩放；最小化收起为 `WS_EX_LAYERED` + `UpdateLayeredWindow` 逐像素抗锯齿 48px 圆形悬浮球（带柔和投影、实时进度环与右键原生菜单）；悬浮球 ↔ 迷你条共享同一焦点锚点，原地完成 **220ms `cubic ease-out` 灵动岛式胶囊连续形变与透明叠化交接**，迷你条与完整窗强制同宽联动且高分屏上下精准居中。
- **生态治理 4 支柱连续评分与核心性能全链路压榨（v1.6.0）**：合并 `ecosystem-inventory.mjs` 统一扫描底座（严格区分 `eager / deferred` MCP 与插件启停态），落地 4 支柱连续健康评分；引擎层完成 Transcript 增量字节累加解析、Git 5×→1× 单子进程收敛、SQLite `WeakMap` 预编译语句缓存、轮询 `rev` 摘要短路与 `ACTIVE_CONV_TTL_MS` 心跳提速。
- **零 Zod 瘦身 33% 与 Radix 12 阶视觉统一（v1.6.0）**：自研轻量 SEP-1865 MCP App 桥接层彻底移除 `zod` 与重型 SDK，单文件 UI 从 `706 KiB` 骤降至 **`475.0 KiB`**；全界面收敛为 Radix UI Colors 12 阶色板与 4 级字号体系，统一 KV 倒计时药丸胶囊与可点击解释气泡，**86 项自动化测试全部通过**。

<details>
<summary><strong>回顾 v1.5.5 核心亮点</strong></summary>

- **GPU 99% 峰值清零与悬浮窗即时同步（v1.5.5）**：彻底清除 CSS `backdrop-filter` 与常驻 60fps 无限动画，移除强制同步 `offsetWidth` 回流与 5s 窗口坐标轮询，按需启停 KV 1s 倒计时并新增低功耗壁纸模式；关闭悬浮窗或 WebView2 宿主退出时 `0ms` 立即切回离线态并释放端口。
- **视口防裁切浮层、标题栏自适应与调用表动态列宽（v1.5.5）**：全部下拉菜单与 KV 帮助气泡升级为视口 `position: fixed` 自动夹紧；调用明细表升级为动态列宽分配与窄宽双行卡片兜底。
- **原生 SQLite 纳秒级 TTFT 与纯解码 TPS 引擎（v1.5.5）**：新增零依赖只读模块 `native-step-metrics.mjs` 提取每步纳秒级首字耗时（TTFT）、纯解码耗时与精确思考/正文 Token 拆分；本地库不可用时自动降级至 Plan A 工具耗时剥离引擎。
- **真实 `app.asar` 版本探测与防降级护栏（v1.5.5）**：汉化状态优先读取 `app.asar` 内部 `package.json` 真实版本并校验 `.bak` 防误降级。
- **SQLite WAL 原子重建与后端安全加固（v1.5.5）**：`rebuildIndex` 事务化原子重建，悬浮窗 HTTP 令牌校验升级为 `crypto.timingSafeEqual`。

</details>

<details>
<summary><strong>回顾 v1.5.4 核心亮点</strong></summary>

- **已挂载资产点击穿透检视（v1.5.4）**：点击任意规则、技能或子代理卡片，直接弹出只读脱敏原文检视窗（支持复制路径 / 打开文件，严格白名单防越权且自动脱敏密钥）；点击任意 MCP 服务，展开全部工具明细表与单工具 Token 占比条，并支持一键跳转生态治理页。
- **异常预警一键精准跳转（v1.5.4）**：预警栏每条异常均可点击——点击缓存击穿/连续低速/子代理异常自动收起预警并定位到对应步骤、展开单步解剖抽屉附脉冲高亮；点击上下文超限直达构成拆解区。
- **三源自动聚合交接胶囊（v1.5.4）**：0 模型 Token 自动聚合「Vault 决策 + 当前会话 `transcript.jsonl`（近期诉求、编辑文件、Artifact 路径）+ 实时 Git 改动与最近 2 条 commit」；支持 **紧凑（500t）/ 标准（1200t）/ 完整（2500t）** 三档预算实时重算，弹窗内可直接编辑当前目标与下一步，并逐项勾选要带走的内容。
- **迷你悬浮条 Radix 语义色框与全界面设计统一（v1.5.3 → v1.5.4）**：Windows 原生无框悬浮窗支持随 Antigravity 启动自动弹出、跟手拖拽排序与 5 级快捷长度；为迷你条 5 模块分配深浅自适应 Radix UI Colors 独立语义色框，清零全界面原生裸按钮与中点分隔符。
- **聚焦本地壁纸库（v1.5.4）**：移除内置氛围渐变预设，界面更干净纯粹；老用户旧配置若指向历史渐变预设 ID 会自动静默回退至首张本地壁纸或关闭态，零报错零白屏。

</details>

> [!NOTE]
> **已知宿主边界说明**
> - **首字延迟（TTFT）与精确思考拆分**：`v1.5.5` 起通过零依赖只读模式（`node:sqlite` `{ readOnly: true }`）从 Antigravity 本地 `conversations/<id>.db` 提取每步纳秒级 TTFT、纯解码速度与精确思考/正文 Token 拆分；若未来宿主变更库结构或本地库不可用，自动 Fail-Open 回退至 Transcript + 工具耗时剥离估算，绝不影响使用。
> - **多对话自动跟随**：只要在任意对话新建或发送消息，Hook 会第一时间记录活跃会话并让侧边栏与独立悬浮窗自动切换（同步对齐对应项目 Git 分支与记忆库）；若仅鼠标点选旧对话浏览（未发消息），在任一面板顶部下拉框点选即可让所有视图同步联动。
> - **额度模块**：由于 Antigravity 暂未提供公开额度查询 API，界面默认隐藏「额度」页（核心代码与 `QuotaProvider` 扩展口仍完整保留在源码中，待官方接口开放后可无痛启用）。

---

## 快速开始

### 环境要求
- **Node.js >= 24.0.0**（使用原生内置 `node:sqlite`，可在终端运行 `node -v` 确认）
- **Git**（用于只读识别仓库指纹与分支，非 Git 目录也可正常使用）
- **Google Antigravity**

### 方式一：下载 Release 免构建插件包（推荐，3 步解压即用，零 `npm install`）

1. 前往 [Releases 页面](https://github.com/Horikita-9-Suzune-Max-Ultrafast/antigravity-hub/releases/latest) 下载 `context-cache-v1.6.0-plugin.zip`（全明文 `.mjs` 源码 + 预编译单文件 UI，零 `node_modules`）。
2. 解压至 Antigravity 本地插件目录，确保目录结构为 `~/.gemini/config/plugins/context-cache/plugin.json`：
   - **Windows PowerShell**：
     ```powershell
     Expand-Archive -Path .\context-cache-v1.6.0-plugin.zip -DestinationPath "$env:USERPROFILE\.gemini\config\plugins" -Force
     ```
   - **macOS / Linux**：
     ```bash
     mkdir -p ~/.gemini/config/plugins
     unzip -o context-cache-v1.6.0-plugin.zip -d ~/.gemini/config/plugins
     ```
3. Antigravity 会自动发现并加载插件（无需重启）：
   - **左侧边栏**：点击 **`Antigravity Hub`** 打开全页控制台（带左侧窄图标导航栏）；
   - **对话右侧边栏**：点击 `+` 菜单打开 **`Antigravity Hub`**（紧凑侧边栏形态）；
   - **独立悬浮窗**：点击监控页顶栏悬浮窗按钮（或开启「随启动自动弹出」），一键呼出桌面原生无框小窗。

### 方式二：从源码克隆、测试并部署

```powershell
# 1. 克隆仓库
git clone https://github.com/Horikita-9-Suzune-Max-Ultrafast/antigravity-hub.git
cd antigravity-hub

# 2. 安装开发期 UI 打包依赖（仅 devDependencies，绝不进入部署产物）
npm install

# 3. 运行全套 21 个自动化测试文件（86 项用例，完全隔离临时目录，零真实数据污染）
npm test

# 4. 构建单文件 MCP App UI 并幂等部署至 ~/.gemini/config/plugins/context-cache
npm run deploy

# 5. 运行健康体检 / 打包便携 Release 压缩包（含 SHA-256 校验文件）
npm run doctor
npm run pack:release
```

---

## 核心特性

### 1. 上下文构成透视与资产检视弹窗（Context Inspector）
- 精确对齐当前会话 `input_tokens + cache_read_tokens` 与模型窗口上限，实时展示占比、剩余空间与切模型水位模拟。
- 自动拆解 `Messages`、`System baseline`、`MCP tools`（区分常驻与 `deferred` 按需懒加载工具）、`Skills`、`Memory & Rules`、`Custom agents` 六大构成。
- **已挂载资产点击穿透检视**：每条规则/技能/子代理均带来源层标签（工作区 / 全局 / 插件 / 内置），点击打开只读脱敏原文弹窗并支持复制路径或直接打开文件；点击 MCP 服务查看全部工具清单与单工具 Token 占比条，一键跳转治理页管理。
- **膨胀归因体检**：自动识别前 3 大上下文占用来源，在占用超过警戒线（默认 `75%`）或单一 MCP Server 过重（`>= 15K` tokens）时给出本地零消耗提示。

### 2. 主 / 子 Agent 实时调用明细、TPS 监控与预警跳转（Live Calls & Telemetry）
- 自动识别主对话 `transcript.jsonl` 中的 `invoke_subagent` 调用并追踪所有子 Agent（编号 `主`、`子1`、`子2`…），支持按步查看、按 Agent / 模型维度汇总、多维筛选，以及顶部汇总看板（步数 / 加权均速 / 累计估算费用 / 当前模型）。
- **1-to-1 双源计时与 Token 加权吞吐**：`PreInvocation` → `PostInvocation` 实测 `hook_ms` 采用 `startMs` 优先一对一消费机制（防同秒错配），缺失时平滑回退至 `hybrid_tool_split` / `transcript_fallback`；均速按总输出 Token / 总耗时加权计算。
- **前缀缓存击穿自动归因与单步解剖**：自动区分 `model_changed`、`idle_ttl_expired`、`context_compacted_or_reset`、`prefix_mutated_unknown` 四类原因；点击任意调用行展开单步解剖抽屉，查看所属会话/子代理、完整模型名、缓存命中比例条与击穿归因。
- **零 Token 异常预警一键跳转**：本地实时检测 4 类异常（上下文超警戒线、缓存击穿、子 Agent 突发高耗、连续 3 步低速 `< 15 tok/s`），点击预警条目自动收起预警栏并定位到对应步骤展开解剖抽屉；可选开启聊天流仅用户可见单行 TPS/Cache 状态条。

### 3. 多对话自动跟随、子代理保留与运行汇总
- **自动跟随活跃对话**：Hook 在 `SessionStart` / `PreInvocation` / `PostInvocation` / `Stop` 实时记录最新活跃会话及其所属工作区，侧边栏与独立悬浮窗均自动切换，连同 Git 分支、Rules 清单与记忆库一并对齐目标项目。
- **运行汇总与子代理保留**：下拉列表保留近 2 小时活跃子代理（带 `子N` 徽章与运行绿点），切回主会话后仍可随时回看；提供顶部 **「汇总：当前运行中的全部对话 (主+子)」** 视图，实时聚合所有并行会话调用流。
- **跨视图同步与按需锁定**：任一面板切换历史对话，其他已打开监控视图同步联动；点击「跟随 / 锁定」按钮随时钉住指定对话。

### 4. Git 感知跨会话记忆库与三源交接胶囊（Context Vault）
- 对目标业务仓库严格**只读探测** Git 指纹、分支与 `HEAD`（绝不在业务仓库写入任何缓存文件），按 `project_id + branch` 隔离存储 `working_state`、`decision`、`architecture`、`pitfall` 与 `Stop` 自动 `checkpoint`。
- 所有记忆写入前自动脱敏（过滤 Bearer Token、API Key、JWT、PEM 私钥等），`SessionStart` 在 `< 500 tokens` 硬预算内注入极简项目索引并提示 `HEAD` 前进标脏。
- **三源自动聚合交接胶囊（0 模型 Token）**：自动合并 Vault 记忆、当前会话 `transcript.jsonl`（近期用户诉求、编辑/新建文件清单、产出 Artifact 路径）与实时 Git 改动（`M`/`A`/`?`）及最近 2 条 commit；支持 **紧凑（500t）/ 标准（1200t）/ 完整（2500t）** 三档预算实时切换、弹窗内直接编辑当前目标与下一步，勾选要带走的条目后一键复制或附着发给新对话。

### 5. 原生无框悬浮窗、Radix 迷你条、Gemini KV 倒计时与 4 分区设置
- **随 Antigravity 启动自动弹出**：MCP Server 握手完成后自动拉起无框悬浮窗（按宿主 `language_server.exe` PID 去重，单次生命周期仅弹一次，退出自动收尾，设置页随时开关）。
- **迷你悬浮条 5 模块独立 Radix 语义色框 & 跟手拖拽排序**：
  - 上下文占比（Indigo 靛蓝）｜ 输出速度 TPS（Violet 柔和紫 / 低速 Amber）｜ KV 倒计时（Cyan 青蓝 → Amber → Red）｜ 模型名（Slate 1px 描边 + 微底色）｜ 缓存命中（Green 翡翠绿），深浅主题自适应。
  - 内置「极简 1 / 紧凑 2 / 标准 3 / 加宽 4 / 完整 5」5 级快捷长度并保留自由拖宽；设置页提供等比预览条，支持跟手拖拽实时让位（FLIP 动画）与点击互换排序。
- **Gemini KV Cache 保鲜倒计时与三态图标**：对话结束后本地 1 秒倒计时（默认 15 分钟参考窗口可自定义，0 模型 Token），悬浮窗与侧栏 Hub 图标随空闲风险平滑切换 **蓝 → 琥珀黄 → 警示红**，配套 `?` 原理提示。
- **Windows 原生无框 WebView2 悬浮窗**：基于 `127.0.0.1` 一次性令牌鉴权拉起原生圆角无框窗口（非 Windows 自动降级至 Edge/Chrome `--app`），支持 Always-on-Top 置顶、收缩迷你条、独立最小化与一键还原、8 方向缩放与高 DPI 位置记忆，关闭即释放端口。
- **顶栏一键安全重启、检查更新与 4 分区设置**：监控顶栏与设置维护区均提供确认保护的「重启 Antigravity」（脱离进程重启，绝不触碰 `app.asar`）；设置维护区支持手动**检查更新与 SHA-256 强校验一键更新**（仅限官方 GitHub Release 白名单、防 Zip-Slip、原子目录切换与失败自动回滚，绝不触碰用户数据）；设置页清晰划分为常规与语言、监控与告警、独立悬浮窗、维护与快捷操作。

### 6. 生态治理与场景预设（Ecosystem & Harness Governance）
- **Effective Harness 全景生效栈与离线三合一体检**：按 `P1 工作区 > P2 全局 > P3 插件 > P4 内置` 扫描全部 Rules、Skills、Hooks 与 MCP Server，纯离线检测 MCP 断路径/过重 Schema、Skill 覆盖冲突/断链（过滤代码块与占位符防误报）以及规则/配置中的明文密钥风险（自动脱敏）。
- **分层修复闭环与单条忽略**：Skill/配置类支持预览/微调预设提示词后一键发送给当前对话 Agent（全页视图自动切为复制提示词）或批量打包修复；重型 MCP 一键跳转停用；隐私告警提供脱敏预览与安全改造提示词；支持单条忽略（实时重算健康分）与底部折叠区随时恢复。
- **多信号智能分类与可勾选场景预设**：综合读取插件 Manifest 描述、`SKILL.md` 描述、MCP 工具名与启动参数做中英双语分类；支持将核心插件标为**常驻保护**、手动覆盖场景分类；内置「极简省流」「全部启用」（确定性）与「专注编码」「办公协作」（推荐模板，未归类项默认保留）；切换前弹出可勾选 Diff 预览并实时重算 Rules/Skills/MCP Token 变化，可一步另存为自定义预设。
- **五重安全护栏与快照时间机器**：系统级保护 `context-cache` 防失联，所有配置写入前自动留存不可变快照（含永久基线），支持界面一键无损回滚与 CLI 逃生舱（`ctx gov rollback`）。

### 7. 本地壁纸引擎（Appearance & Wallpaper）
- **零新增侵入点热加载**：复用现有 Fail-Open 客户端运行时实时推送样式，无需重新打包 `app.asar`；支持秒级总开关与 CLI 急救关闭（`ctx wallpaper off`）。
- **本地壁纸库与只读文件夹**：支持导入本地壁纸库（15 MiB 体积熔断 + Blob 内存自动释放）与 100% 只读本地文件夹扫描（不改动原图）；支持按来源筛选轮播池、自定义壁纸库子集、双缓冲淡入淡出与 1 分钟起自定义轮播间隔。
- **实时参数调节与深浅主题绑定**：滑块拖动即时生效，支持不透明度、模糊、饱和度、全局遮罩、面板不透明度（`scrimOpacity`）与毛玻璃调节，并支持浅色/深色主题独立绑定壁纸。

### 8. Antigravity 零依赖界面汉化（Antigravity Localization）
- **纯 Node.js 流式 ASAR 补丁引擎**：无需 `node_modules` 或解包数千文件，直接流式原位重写 `resources/app.asar` 并完整维护 Electron 4 MiB 分块 SHA-256 `integrity` 校验，无损保留 `unpacked`/`executable`/`link` 元数据。
- **5 态精准感知与纯净原版备份保护**：自动探测客户端路径、版本号与汉化状态；若检测到第三方补丁（如已有 `app.asar.zh-cn.bak`），自动以纯净原版备份为基底，绝不误将已补丁文件存为原版。
- **脱离进程安全重启（Windows WMI Breakaway）**：点击「一键应用汉化」或「一键还原原版」时，通过脱离宿主进程树与 Job Object 的独立后台进程自动关闭客户端、释放文件锁、写入/还原 `app.asar` 并重新拉起 Antigravity。
- **739+ 精校内置词典 + 三层外置热加载**：覆盖 127 条原生菜单 + 612 条 Antigravity 2.0 高频界面 + 34 条动态正则模板，支持 `自定义覆盖 > 社区 MIT 词典 > 内置词典` 合并并热编译至 `%USERPROFILE%\.context-cache\i18n\runtime-bundle.json`，日常改词条/品牌名/免疫区**无需重打 `app.asar`**。
- **防误翻物理免疫区与更新提醒**：一键保护代码块、输入框、终端、文件路径与自定义 CSS 选择器；支持自定义或隐藏左上角品牌显示；官方升级覆盖 `app.asar` 后顶部自动提醒一键重打。

---

## 架构与设计原则

### 双层 Tool Visibility 隔离（0 模型 Token 轮询）

| 层级 | 工具清单 | 可见性 | 对模型上下文的影响 |
| :--- | :--- | :--- | :--- |
| **Model-Visible（5 个精简工具）** | `ctx_open_monitor`、`ctx_brief`、`ctx_save`、`ctx_search`、`ctx_doctor` | `["model", "app"]` | 常驻定义极简（约 `0.6K` tokens） |
| **App-Only（11 个 UI 私有工具）** | `app_get_context_breakdown`、`app_get_calls`、`app_get_quota`、`app_calibrate_quota`、`app_vault_manage`、`app_config_manage`、`app_doctor_action`、`app_i18n_manage`、`app_governance_manage`、`app_appearance_manage`、`app_review_manage` | `["app"]` | **0 tokens**（模型不可见、不触发推理） |

### 五层抗 Antigravity 破坏性更新设计
1. **零运行时依赖**：Core Engine、Hooks、MCP Server、CLI 纯基于 Node.js 24 原生能力（含 `node:sqlite`）；仅开发期使用 `@modelcontextprotocol/ext-apps` + `esbuild` 打包单一零外链静态 HTML，部署产物**零 `node_modules`**。
2. **外置真相源 + 可重建派生索引**：Markdown 与追加式 JSONL 真相源独立存放于 `%USERPROFILE%\.context-cache`（支持 `CONTEXT_CACHE_DATA_DIR` 覆盖），SQLite WAL + FTS5（`index.sqlite`）随时可删并无损重建。
3. **极薄 Fail-Open Hook 层**：仅挂载 `SessionStart`、`PreInvocation`、`PostInvocation`、`Stop`（**不挂载 `PreToolUse`**，绝不干扰原生命令审批）；统一 5s 硬超时、camelCase/snake_case 多版本兼容、脱敏 `schema-drift.jsonl` 录制与 3 次连续异常熔断（任何异常恒定返回 `{}`，退出码 `0`）。
4. **Windows 含空格路径免疫**：`hooks.json` 使用相对路径 + `--no-warnings`，Release 包使用 Antigravity 原生 `${PLUGIN_ROOT}` 变量展开，源码库零本机路径硬编码。
5. **不改宿主敏感配置**：常规运行、监控与自愈绝不修改 Antigravity 程序文件或 `~/.gemini/config/config.json`（仅在用户主动点击汉化/治理写入时留存不可变备份后再执行）。

---

## 命令行工具（CLI）

内置宿主无关 CLI（`bin/ctx.mjs`），可在任意终端直接调用（如果通过 Release 包安装，将路径替换为 `~/.gemini/config/plugins/context-cache/bin/ctx.mjs` 即可）：

```powershell
# 查看当前项目 <500t 极简记忆简报
node --no-warnings bin/ctx.mjs brief

# 写入一条项目决策（自动脱敏）
node --no-warnings bin/ctx.mjs save --kind decision --title "标题" --summary "核心结论" --tags arch,cache

# FTS5 全文检索记忆库
node --no-warnings bin/ctx.mjs search "缓存击穿"

# 查看会话调用明细与 TPS / 额度参考统计
node --no-warnings bin/ctx.mjs calls
node --no-warnings bin/ctx.mjs quota

# 健康体检 / 一键自愈（重建 SQLite FTS5 索引 + 复位熔断器；可选 --resync-telemetry 重算历史 TPS）
node --no-warnings bin/ctx.mjs doctor
node --no-warnings scripts/doctor.mjs --repair
node --no-warnings bin/ctx.mjs doctor --repair --resync-telemetry

# 导出脱敏备份至 ~/.context-cache/exports/
node --no-warnings bin/ctx.mjs export

# 生态治理体检与宿主配置应急回滚逃生舱
node --no-warnings bin/ctx.mjs gov status
node --no-warnings bin/ctx.mjs gov lint
node --no-warnings bin/ctx.mjs gov snapshots
node --no-warnings bin/ctx.mjs gov rollback

# 外观壁纸状态、切图与一键急救关闭
node --no-warnings bin/ctx.mjs wallpaper status
node --no-warnings bin/ctx.mjs wallpaper next
node --no-warnings bin/ctx.mjs wallpaper off

# 界面汉化状态探测、词典热更新、应用与应急还原
node --no-warnings bin/ctx.mjs i18n status
node --no-warnings bin/ctx.mjs i18n refresh
node --no-warnings bin/ctx.mjs i18n apply
node --no-warnings bin/ctx.mjs i18n restore
```

---

## 升级、卸载与一键还原

### 平滑升级到最新版
- **插件内一键更新（v1.5.4+ 推荐）**：进入 **「插件设置 → 维护与操作」** 点击 **「检查更新」**，发现新版后点击 **「一键更新（SHA-256 校验）」** 即可完成强校验下载、原子目录切换与安全重启引导（如遇网络超时或文件占用自动回滚并可跳转 Release 手动下载）。
- **Release 包手动覆盖**：也可直接下载新版 `context-cache-v1.6.0-plugin.zip` 并覆盖解压到 `~/.gemini/config/plugins`。你的记忆库、壁纸库、汉化词典、治理偏好与配置快照全部存放在 `%USERPROFILE%\.context-cache`，**升级零数据丢失**。
- **源码用户**：在仓库目录执行 `git pull && npm run deploy`。

### 完整卸载与无损还原
1. **如曾应用过界面汉化**：先在插件内「界面汉化」页点击 **「一键还原原版」**（或终端运行 `node --no-warnings ~/.gemini/config/plugins/context-cache/bin/ctx.mjs i18n restore`）恢复原版 `app.asar`。
2. **如曾切换过治理场景预设**：可在「生态治理 → 快照」一键回滚至初始基线（或运行 `ctx gov rollback`）。
3. **移除插件本体**：删除 `~/.gemini/config/plugins/context-cache` 目录即可彻底卸载；如需连同个人记忆与本地壁纸缓存一并清理，再删除 `%USERPROFILE%\.context-cache`。

---

## 常见问题（FAQ）

<details>
<summary><strong>1. 会消耗我的模型额度 / 额外 Token 吗？</strong></summary>

不会。监控面板的实时刷新、悬浮窗、资产检视弹窗、交接胶囊生成、生态体检、壁纸热更新和界面汉化全部走私有 `app`-only 工具或本地文件系统，**0 模型 Token 消耗**。模型侧仅暴露 5 个极简工具定义（约 `0.6K` tokens），且不会在后台主动发起任何 LLM 请求。
</details>

<details>
<summary><strong>2. 为什么插件加载失败或报错找不到 <code>node:sqlite</code>？</strong></summary>

请检查本机 Node.js 版本是否 `>= 24.0.0`（运行 `node -v` 查看）。本项目利用 Node.js 24 原生内置的 `node:sqlite` 实现零第三方依赖，低于 Node 24 会无法加载内建 SQLite 模块。升级 Node.js 至 24+ 后重新打开 Antigravity 即可。
</details>

<details>
<summary><strong>3. 汉化或壁纸会不会把 Antigravity 改坏？官方更新后怎么办？</strong></summary>

- **壁纸引擎**：不新增任何 ASAR 侵入点，随时可一键秒关或用 CLI `ctx wallpaper off` 急救关闭；若遇到旧配置冲突自动静默回退。
- **界面汉化**：首次补丁前自动校验并留存纯净原版 `app.asar` 备份，支持一键无损还原；已连续通过 **Antigravity `2.35.1` → `2.35.2`** 全开实战态原地升级实测——官方更新覆盖 `app.asar` 后客户端正常启动不崩溃，Hub 自动提醒「官方更新待重打」，一键重新应用时会自动将 `.bak` 刷新为新版干净原版（杜绝旧版降级），同时原有壁纸与参数直接自动回归。
</details>

<details>
<summary><strong>4. 会在我的代码项目里生成杂乱文件吗？安全吗？</strong></summary>

**绝不会。** 对业务代码仓库仅做只读 Git 探测与只读规则/技能扫描，所有插件状态、索引、快照、壁纸均存放在 `%USERPROFILE%\.context-cache`。同时内置脱敏器自动过滤常见 API Key、Bearer Token、JWT 与 PEM 私钥，资产原文预览额外限制在受控白名单路径并拒绝读取 `.env` 与私钥文件。
</details>

<details>
<summary><strong>5. 找不到悬浮窗或想关掉启动自动弹出？</strong></summary>

点击控制台右上角 / 左下角齿轮图标进入 **「插件设置 → 独立悬浮窗」**，可随时开关「随 Antigravity 启动自动弹出」、调整迷你条快捷长度与跟手拖拽模块顺序；若悬浮窗最小化，在监控页顶栏再次点击悬浮窗图标即可一键唤醒至前台。
</details>

---

## 目录结构

```text
context-cache/
├── bin/ctx.mjs                          # 宿主无关 CLI（记忆 / 监控 / 体检 / 治理 / 壁纸 / 汉化）
├── src/
│   ├── core/                            # Node.js 24 零依赖核心引擎
│   │   ├── paths.mjs                    # 跨平台路径与外置数据目录解析
│   │   ├── config.mjs                   # 配置、模型窗口、价目表、悬浮条偏好与校准
│   │   ├── redact.mjs                   # 敏感凭据脱敏过滤器
│   │   ├── git-context.mjs              # 目标仓库只读 Git 探测（分支/变更文件/近期提交）
│   │   ├── storage.mjs                  # Markdown / JSONL 真相源原子读写
│   │   ├── index-db.mjs                 # node:sqlite WAL + FTS5 派生索引与无损重建
│   │   ├── vault.mjs                    # 跨会话记忆 CRUD、Compact Brief 与三源三档交接胶囊
│   │   ├── context-inspector.mjs        # 上下文构成拆解、资产元数据、安全只读脱敏预览与膨胀归因
│   │   ├── transcript-parser.mjs        # 多版本增量游标解析、子 Agent 发现与流水提取
│   │   ├── native-step-metrics.mjs      # 零依赖只读原生会话库（纳秒级 TTFT、纯解码耗时与精确思考拆分）
│   │   ├── telemetry.mjs                # 多 Agent 调用明细、Decode TPS、工具耗时剥离、缓存击穿与 4 类预警
│   │   ├── session-tracker.mjs          # 活跃对话自动跟随、跨视图联动与工作区对齐
│   │   ├── quota.mjs                    # 5h/7d 滑动窗口、基线校准与 QuotaProvider 扩展口
│   │   ├── popout-server.mjs            # 127.0.0.1 令牌鉴权悬浮小窗服务、握手与自动降级
│   │   ├── win-floating-host.ps1        # Windows 原生无框 WebView2 置顶/迷你条/最小化悬浮窗宿主
│   │   ├── client-restart.mjs           # 脱离进程安全重启 Antigravity（不触碰 app.asar）
│   │   ├── self-update.mjs              # GitHub Release 检查更新、SHA-256 强校验与原子目录切换
│   │   ├── doctor.mjs                   # 体检、漂移报告、备份导出与自愈
│   │   ├── review/                      # 本地代码审查引擎（Git Diff 解析 / L1 静态规则 / 原生门禁 / L2 Subagent 闭环）
│   │   ├── governance/                  # 生态治理（全景扫描/4 支柱评分/多信号分类器/场景预设/离线体检修复闭环/护栏快照）
│   │   ├── appearance/                  # 本地壁纸引擎（外置库/只读扫描/轮播池/旧配置静默回退/热加载）
│   │   └── i18n/                        # 零依赖 Antigravity 汉化引擎（流式 ASAR/词典/脱离重启）
│   ├── adapters/antigravity/            # 极薄 Fail-Open Hook 适配层
│   │   ├── normalize.mjs                # 多版本字段归一化与脱敏漂移录制
│   │   ├── circuit-breaker.mjs          # 3 次异常熔断 5 分钟
│   │   └── hook.mjs                     # 统一 Hook 入口（5s 硬超时）
│   ├── mcp/server.mjs                   # 零依赖 MCP Stdio Server（5 Model + 11 App-Only）
│   └── ui/                              # 单文件自包含模块化控制台前端
│       ├── index.html                   # 控制台壳层与资产检视/交接胶囊/设置弹窗
│       ├── styles.css                   # Radix UI Colors 深浅自适应主题与悬浮条语义色框
│       ├── app.mjs                      # 主监控交互、预警精准跳转与悬浮窗联动
│       ├── i18n-ui.mjs                  # 零依赖中英双语前端词典
│       ├── build-ui.mjs                 # esbuild 单文件零外链打包脚本
│       └── modules/                     # review-module / appearance-module / governance-module / i18n-module
├── plugin/                              # Antigravity 插件清单、Hooks、Rules、Skills 与图标
├── scripts/                             # deploy.mjs、pack-release.mjs 与 doctor.mjs
├── tests/                               # 21 个自动化测试文件（86 项端到端 / 单元 / 韧性用例）
├── LICENSE                              # MIT License
├── README.md                            # 简体中文文档
├── README.en.md                         # English documentation
└── package.json
```

---

## 许可证

本项目基于 [MIT License](./LICENSE) 开源。
