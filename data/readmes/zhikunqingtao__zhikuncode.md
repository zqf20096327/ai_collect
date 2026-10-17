[🌐 English](docs/README_EN.md)

<div align="center">
  <img src="docs/assets/logo.svg" alt="ZhikunCode" width="120" />
  <h1>ZhikunCode</h1>
  <p><strong>开源 AI 编程助手 — 部署一次，浏览器全流程操控</strong></p>
  <p>Agent 委派与后台任务 · Docker 自托管 · 国产大模型直连 · 深度安全架构</p>

  <p>
    <a href="#-快速开始">快速开始</a> ·
    <a href="#-特性亮点">核心特性</a> ·
    <a href="https://zhikunqingtao.github.io/zhikuncode/#case-study">案例展示</a> ·
    <a href="#-公开工程案例">公开工程案例</a> ·
    <a href="#-swe-bench-lite-评测">SWE-bench 评测</a> ·
    <a href="#-cli-工具">CLI 工具</a> ·
    <a href="#-skill技能系统">skill技能系统</a> ·
    <a href="#-插件系统">插件系统</a> ·
    <a href="#-可视化">可视化</a> ·
    <a href="#-记忆系统">记忆系统</a> ·
    <a href="#-竞品对比">竞品对比</a> ·
    <a href="docs/README_EN.md">English</a>
  </p>

  <p>
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" /></a>
    <a href="https://github.com/zhikunqingtao/zhikuncode"><img src="https://img.shields.io/badge/Docker-Ready-blue?logo=docker" alt="Docker" /></a>
    <a href="https://github.com/zhikunqingtao/zhikuncode/stargazers"><img src="https://img.shields.io/github/stars/zhikunqingtao/zhikuncode?style=social" alt="GitHub Stars" /></a>
    <a href="https://github.com/zhikunqingtao/zhikuncode"><img src="https://img.shields.io/github/last-commit/zhikunqingtao/zhikuncode" alt="Last Commit" /></a>
    <a href="https://github.com/zhikunqingtao/zhikuncode"><img src="https://img.shields.io/github/languages/code-size/zhikunqingtao/zhikuncode" alt="Code Size" /></a>
    <a href="https://github.com/zhikunqingtao/zhikuncode/actions/workflows/ci.yml"><img src="https://github.com/zhikunqingtao/zhikuncode/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
    <a href="https://zhikunqingtao.github.io/zhikuncode/swe-bench-report.html"><img src="https://img.shields.io/badge/SWE--bench%20Lite-56.0%25%20(168%2F300)-7a2410?logo=python&logoColor=white" alt="SWE-bench Lite 56.0% (168/300)" /></a>
  </p>
</div>

---

> **部署到服务器，打开浏览器就能用，手机上也行**

> 🏗️ **[查看完整系统架构图 →](https://zhikunqingtao.github.io/zhikuncode/ZhikunCode-Architecture.html)**  
> Java Agent Runtime · React 浏览器操作面 · Python Capability Service · 全景可视化

> 🧭 **[查看完整能力总览 →](https://zhikunqingtao.github.io/zhikuncode/ZhikunCode-Capability-Overview.html)**
> 交互入口 · Agent / Run · 权限安全 · 工具与 Skill · 验证产物 · 观测恢复

> **历史代码规模快照（非当前版本统计）：** `ea0170c` · 2026-08-09 · Git 跟踪的产品源代码 134,826 行 / 863 文件（Java 93,118 / 622、React 33,642 / 209、Python 服务与 CLI 8,066 / 32；不统计本地忽略文件）

> 🔎 **[实时黄金监控：ZhikunCode vs Codex 同题 PK →](https://zhikunqingtao.github.io/zhikuncode/case-studies/zhikuncode-codex-gold-monitor-audit.html)**
> ZhikunCode × Codex · 同一需求两套实现，14 维评分、过程截图与完整执行记录

> 🚄 **[12306 候补全链路可视化：单文件零依赖交付 →](https://zhikunqingtao.github.io/zhikuncode/case-studies/zhikuncode-codex-12306-audit.html)**
> ZhikunCode/KimiK3 × Codex/GPT-5.6 Sol · 7 维对比评估，双方产物可直接在线试玩

> 🎮 **[5小时 AI 从零写出可玩的《王者荣耀》网页版 →](https://zhikunqingtao.github.io/zhikuncode/case-studies/zhikuncode%E5%BC%80%E5%8F%91%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80.html)**
> Kimi K3 · 一次连续开发 5 小时 29 分 · 19 个文件 / 7,979 行纯静态 Three.js · 打开浏览器即可试玩

> 📊 **[AI 办公工具对比测评（宇树科技 · 截至 2026-08-30）→](https://zhikunqingtao.github.io/aireport/case-studies/AI%E5%8A%9E%E5%85%AC%E5%B7%A5%E5%85%B7%E5%AF%B9%E6%AF%94%E6%B5%8B%E8%AF%84_%E5%AE%87%E6%A0%91%E7%A7%91%E6%8A%80_%E6%88%AA%E8%87%B32026-08-30.html)**
> 五款工具 × 六任务连续链路 · 30 件固定终稿证据复核 · 同一报告阿里云 OSS 镜像：[oss.zhikun.xin](https://oss.zhikun.xin/zhikuncode/aireport/case-studies/AI%E5%8A%9E%E5%85%AC%E5%B7%A5%E5%85%B7%E5%AF%B9%E6%AF%94%E6%B5%8B%E8%AF%84_%E5%AE%87%E6%A0%91%E7%A7%91%E6%8A%80_%E6%88%AA%E8%87%B32026-08-30.html)

> 🔍 **AI Coding 代码审查对比：17 份报告**
> [Claude Opus5.5：排名分析、方法与证据 →](https://github.com/zhikunqingtao/zhikuncode/blob/aicoding-eval-0923/docs/case-studies/assets/aicoding%E8%AF%84%E6%B5%8B/Claude%20Opus5.5-17%E4%BB%BD%E5%AE%A1%E6%9F%A5%E6%8A%A5%E5%91%8A%E6%8E%92%E5%90%8D%E5%88%86%E6%9E%90%E6%96%B9%E6%B3%95%E8%BF%87%E7%A8%8B%E8%AF%81%E6%8D%AE%E4%B8%8E%E7%BB%93%E8%AE%BA.md) · [GPT-6 Astra Ultra：公平排名与可复核证据 →](https://github.com/zhikunqingtao/zhikuncode/blob/aicoding-eval-0923/docs/case-studies/assets/aicoding%E8%AF%84%E6%B5%8B/GPT-6%20Astra%20Ultra-17%E4%BB%BD%E5%AE%A1%E6%9F%A5%E6%8A%A5%E5%91%8A%E5%85%AC%E5%B9%B3%E6%8E%92%E5%90%8D%E4%B8%8E%E5%8F%AF%E5%A4%8D%E6%A0%B8%E8%AF%81%E6%8D%AE.md)

> 🔬 **[八款 AI Coding 同题代码审查（2026-09-25） →](docs/case-studies/assets/AICoding%E8%AF%84%E6%B5%8B0925/README.md)**
> 八份原报告 · 六维评分 · 可复核证据与约1小时57分钟过程录屏

> 🏆 **[SWE-bench Lite 技术报告 →](https://zhikunqingtao.github.io/zhikuncode/swe-bench-report.html)**  
> 提交命名空间 `20260525_zhikuncode` · 官方 harness 评测 Resolve **168 / 300 (56.0%)** · Patch 生成率 284 / 300 (94.7%)

---

## 🔎 公开工程案例

### 实时黄金监控：ZhikunCode vs Codex 同题 PK

同一个实时黄金监控需求，分别交给 ZhikunCode 与 Codex 从零完成，再按需求理解、开发交互、数据准确性、架构、代码质量、用户体验等 14 个维度打分。报告同时保留双方的优点与缺陷。

- ZhikunCode：Kimi K3 遇到 HTTP 429 后，由用户切换至 GLM-5.2 并在同一逻辑会话中继续。
- Codex：GPT-5.6 Sol，推理强度 High。
- 最终评分 ZhikunCode 68.3、Codex 68.4 —— 两者几乎打成平手。

**[查看对比报告 →](https://zhikunqingtao.github.io/zhikuncode/case-studies/zhikuncode-codex-gold-monitor-audit.html)** ·
**[下载原始数据 →](docs/case-studies/zhikuncode-codex-gold-monitor-evidence.json)** ·
**[了解评测方法 →](docs/case-studies/README.md)**

### 12306 候补全链路可视化：单文件零依赖交付

同一个"12306 候补成功后台全链路"动态可视化需求，分别交给 ZhikunCode 与 Codex 完成，从任务理解、代码质量、动态可视化、架构与数学、用户体验、开发效率、技术实现 7 个维度评估。报告同时保留双方的优点与缺陷。

- ZhikunCode：kimi-k3 交付单文件 HTML，1,061 行、零外部网络依赖，打开就能跑。
- Codex：GPT-5.6 Sol（高推理模式）交付 Next.js 工程，会话截图显示总耗时 27m52s。
- 最终加权评分 ZhikunCode 8.68、Codex 8.45 —— 差距很小，产物风格截然不同。

**[查看对比报告 →](https://zhikunqingtao.github.io/zhikuncode/case-studies/zhikuncode-codex-12306-audit.html)** ·
**[产物在线 Demo →](https://zhikunqingtao.github.io/zhikuncode/case-studies/assets/12306-comparison/artifacts/zhikuncode/12306-houbu.html)** ·
**[下载原始数据 →](docs/case-studies/zhikuncode-codex-12306-evidence.json)** ·
**[了解评测方法 →](docs/case-studies/README.md)**

### 5小时，AI 从零写出可玩的《王者荣耀》网页版

ZhikunCode 使用 Kimi K3 在 2026-08-09 凌晨一次性完成了一个纯静态 Three.js 5v5 MOBA 游戏：选将、对局、AI 队友与敌人全部可玩，打开浏览器就能进。

- 一次连续开发 5 小时 29 分，产出 19 个第一方文件、7,979 行代码。
- 10 个子 Agent 协作分工，覆盖玩法、渲染、AI 行为与关卡资源。
- 纯静态交付，无后端、无外部网络依赖，浏览器直接运行。
- 全过程留痕：43 张截图与 5 段原始录屏，可跟着报告一路下钻。

**[查看详细案例 →](https://zhikunqingtao.github.io/zhikuncode/case-studies/zhikuncode%E5%BC%80%E5%8F%91%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80.html)** ·
**[在线试玩（5英雄选将）→](https://king.zhikun.xin/)** ·
**[自动演示（直接进入对局）→](https://king.zhikun.xin/?demo=1)** ·
**[了解评测方法 →](docs/case-studies/README.md)**

### AI 办公工具对比测评（宇树科技 · 截至 2026-08-30）

五款 AI 办公工具——千问办公、Qoder、豆包办公、WorkBuddy 与 ZhikunCode——依次执行同一组六条连续指令，围绕宇树科技完成从 Excel 分析底稿、Word 研究报告、PPT 到信息图与交互 HTML 的完整办公链路，共产出 30 件固定终稿并逐件复核证据。

正式排名双榜列示：六任务等权榜 ZhikunCode 以 93.8 分列第 1（千问 93.6 分第 2）；均衡投研实务榜千问 93.3 分第 1、ZhikunCode 92.7 分第 2。30 件终稿的交付闸门分布为 G0 3 件 / G1 20 件 / G2 7 件。本报告为单次固定样本任务链实测，不外推为各工具的总体能力。

**[查看完整报告（GitHub Pages）→](https://zhikunqingtao.github.io/aireport/case-studies/AI%E5%8A%9E%E5%85%AC%E5%B7%A5%E5%85%B7%E5%AF%B9%E6%AF%94%E6%B5%8B%E8%AF%84_%E5%AE%87%E6%A0%91%E7%A7%91%E6%8A%80_%E6%88%AA%E8%87%B32026-08-30.html)** ·
**[阿里云 OSS 镜像 →](https://oss.zhikun.xin/zhikuncode/aireport/case-studies/AI%E5%8A%9E%E5%85%AC%E5%B7%A5%E5%85%B7%E5%AF%B9%E6%AF%94%E6%B5%8B%E8%AF%84_%E5%AE%87%E6%A0%91%E7%A7%91%E6%8A%80_%E6%88%AA%E8%87%B32026-08-30.html)**

### AI Coding 代码审查对比：17 份报告

**[Claude Opus5.5：排名分析方法、过程、证据与结论 →](https://github.com/zhikunqingtao/zhikuncode/blob/aicoding-eval-0923/docs/case-studies/assets/aicoding%E8%AF%84%E6%B5%8B/Claude%20Opus5.5-17%E4%BB%BD%E5%AE%A1%E6%9F%A5%E6%8A%A5%E5%91%8A%E6%8E%92%E5%90%8D%E5%88%86%E6%9E%90%E6%96%B9%E6%B3%95%E8%BF%87%E7%A8%8B%E8%AF%81%E6%8D%AE%E4%B8%8E%E7%BB%93%E8%AE%BA.md)** ·
**[GPT-6 Astra Ultra：公平排名与可复核证据 →](https://github.com/zhikunqingtao/zhikuncode/blob/aicoding-eval-0923/docs/case-studies/assets/aicoding%E8%AF%84%E6%B5%8B/GPT-6%20Astra%20Ultra-17%E4%BB%BD%E5%AE%A1%E6%9F%A5%E6%8A%A5%E5%91%8A%E5%85%AC%E5%B9%B3%E6%8E%92%E5%90%8D%E4%B8%8E%E5%8F%AF%E5%A4%8D%E6%A0%B8%E8%AF%81%E6%8D%AE.md)**

### 八款 AI Coding 同题代码审查（2026-09-25）

八款 AI Coding 工具审查同一代码提交，从有效发现、准确性、归因、证据、工程覆盖及建议交付六个维度比较最终报告。公开八份原报告、逐项评分、独立复核证据、重算脚本与约1小时57分钟的过程录屏。本次为单任务产物评测，不代表产品总体能力排名。

**[评测首页 →](docs/case-studies/assets/AICoding%E8%AF%84%E6%B5%8B0925/README.md)** ·
**[证据与复算 →](docs/case-studies/assets/AICoding%E8%AF%84%E6%B5%8B0925/%E8%AF%81%E6%8D%AE%E9%99%84%E4%BB%B6/README.md)** ·
**[过程录屏与时间索引 →](docs/case-studies/assets/AICoding%E8%AF%84%E6%B5%8B0925/%E8%AF%81%E6%8D%AE%E9%99%84%E4%BB%B6/%E5%AE%8C%E6%95%B4%E6%B5%81%E7%A8%8B%E5%BD%95%E5%B1%8F/%E5%BD%95%E5%B1%8F%E6%97%B6%E9%97%B4%E7%B4%A2%E5%BC%95%E4%B8%8E%E8%BF%87%E7%A8%8B%E6%A0%B8%E9%AA%8C.md)**

> 以上案例均为单次任务实测记录，详细方法与数据见各案例报告页。

---

## ✨ 特性亮点

| | 特性 | 说明 |
|---|---|---|
| 🌐 | **浏览器全流程操控** | 部署一次，任何设备的浏览器即可完成全流程操作 —— 权限审批、方案协商、任务管控，手机上也能用，无需安装客户端 |
| 🧭 | **双视图任务工作台** | 同一 Session 可在简洁工作台与开发工作台之间自由切换。简洁工作台集中展示当前要求、执行状态、主要成果、待处理事项和验收结果；开发工作台保留完整对话、工具、文件、Git、终端、浏览器与 Agent 信息。切换只改变信息组织，不改变后台执行方式 |
| 📦 | **当前交付投影** | 按当前 Root Run 及其递归子 Run 关联本轮要求、最终回复、交付物、待处理 Interaction、活动与 Evidence，避免把不同执行轮次的数据拼接成一次交付；无法精确关联的旧 Session 会明确采用兼容回退 |
| 🔀 | **会话资料合并** | 将 2～5 个空闲会话的摘要、已持久化过程文本和可确认归属的临时产物整理到一个新会话，保留来源会话；新会话等待下一条指令，不自动合并工程代码 |
| 📁 | **Project 与 Run 控制** | 直连本机可选用原生目录选择器，远程部署只浏览配置的 allowed roots；Project 经真实路径规范化并持久授权，Session 拒绝客户端任意 `workingDirectory`。运行中输入按 Session 投递并返回 queued/applied/rejected，支持取消、包含 INTERRUPTED 的 CAS 单一终态与 WebSocket 恢复 |
| 🔗 | **引用本地文件** | 直连本机通过系统选择器把 canonical 路径加入提示词（不上传内容）；ECS、远程或代理访问通过浏览器选择文件，立即上传为 OSS 永久公开对象，再把地址加入提示词。远程上传需要先配置 OSS |
| 🤖 | **Agent 委派与后台任务** | 五种子 Agent 角色、独立上下文与并行执行；同步结果回传、当前 Run 后台结果汇总，以及可查询、可请求取消的后台任务 |
| 🔒 | **统一授权安全架构** | 所有核心工具统一经过 Tool Gateway：规范化输入冻结 → Operation Analyzer 风险与资源分析 → 系统不变量检查 → RUN/SESSION/WORKSPACE Grant 匹配或持久权限交互 → 执行前动态复检 → 结构化结果审计。高风险操作只允许单次授权；专用 Network/MCP Analyzer 对 SAFE/GUARDED 操作支持按工具记住 RUN/SESSION 授权，未知 MCP/动态工具默认只能单次审批 |
| 🇨🇳 | **国产大模型直连** | 千问 / DeepSeek / Moonshot / 智谱GLM / MiniMax 开箱即用，国内网络直连，无需科学上网 |
| 🐳 | **Docker 一键部署** | `docker compose up -d` 默认启动 Java 后端和内置静态前端；镜像同时包含可选的受管 Python 服务，数据存本地 |
| 📤 | **OSS 发布与截图粘贴（可选）** | `/publish-oss` 仍只按明确指令发布已验证产物；粘贴截图支持双路径——OSS 已配置时走后端快速上传，OSS 未配置时自动降级为 Base64 直传，无需额外配置即可使用图片分析能力 |
| 🌍 | **秒悟应用发布（可选）** | 通过 `/publish-meoo` 将已验证的静态网站或全栈应用发布为独立新站点，获取可分享的网站链接；默认关闭，完全访问模式外每次发布需单独确认 |
| 🎙️ | **语音交互（ASR / TTS）** | 对话输入支持麦克风语音识别（qwen3-asr-flash），AI 回复支持一键朗读（qwen3-tts-flash）；接入阿里云百炼 DashScope，配置 API Key 即用，未配置时自动隐藏 |
| ⚡ | **智能上下文管理** | 六层压缩级联（Snip / MicroCompact / ContextCollapse / AutoCompact / CollapseDrain / ReactiveCompact）+ 增量折叠（每10轮自动压缩）+ 413 两级上下文压缩（CollapseDrain 激进压缩 → ReactiveCompact 反应式压缩）+ 精确 Token 计数（tiktoken 多模型支持）+ 自纠错循环（SelfCorrectionLoop，编译/测试失败自动诊断修复，最多3次）+ Token三级告警 + 图片上下文治理（大图外置化 → 按需注入 → 预算守卫三层防护），无缝应对超长对话。核心引擎为 ContextCascade 与 QueryEngine |
| 📷 | **多模态图片对话** | 支持图片上传输入，模型自动识别图片内容并分析；**智能视觉模型路由**——当前模型不支持图片时，自动切换至同厂商视觉模型处理，处理完成后无缝切回原模型；DeepSeek V4.1 Flash（`deepseek-flash`）原生支持视觉，并作为 DeepSeek 系列图片理解兜底。**图片预算守卫**——大图片（>50KB）自动外置化为轻量 JSON 引用，API 调用前按需注入，两阶段 Token 预算守卫确保多图对话不累积超限（单张≤1.5MB，总量≤2MB，单次最多注入 8 张）。ZenMux 图片模型包括 Fable 5.1、Opus 5.5、Sonnet 5.5、Haiku 5.5、GPT-5.6 Sol、GPT-6 Astra、Gemini 3.8 Flash 与 Grok 4.6（各模型数量上限见模型目录） |
| 🖼️ | **浏览器语义快照** | `/snap` 命令智能捕获网页完整状态（DOM 结构 + 交互元素），支持富交互页面语义提取，生成结构化 JSON 供 Agent 解析和回放验证 |
| 💬 | **轮次与任务过程视图** | 显示方式三档：精简档默认折叠问题、过程与回复，可分别展开；标准、完整过程档保留完整问题与回复，按档展示过程，运行中同样生效。移动端常驻输入卡片提供附件、语音和显示方式切换，首页模板可直接填入草稿。 |
| 📊 | **实时活动追踪与审批** | Activity Panel 实时记录 AI 工具执行全流程，L1/L2/L3 三层展示体系，Signal 智能标记（auto_approve/review_recommended/needs_review），一键批量审批决策，SQLite 后端持久化，支持会话恢复 |
| 🧪 | **运行时验证框架（Runtime Verification）** | VerifierFactory 三模态分发（browser/http_api/auto）+ 8 种 HTTP action handler + JSONPath 断言 + 证据链 SQLite 存储 + Feature Flag 双重门控 + 前端实时进度面板 |
| 🔍 | **RV-4 证据包可视化** | 验证产物 7 类证据（screenshot / command / console / test / video / har / diff）Tab 分栏展示，移动端订阅 STOMP `verify_attention` 通知一键审批/驳回，REST API `/api/evidence/*` 提供查询与 Blob 下载 |
| 🏆 | **SWE-bench Lite 历史实测（2026-05）** | 历史评测模型 `qwen3.7-max`（保留原记录）+ 6 工具闭集（Read/Edit/Write/Bash/Grep/Glob），无网络、无 sub-agent；官方 harness 评测 **Resolve 56.0% (168/300)**、Patch 生成率 **94.7% (284/300)**，[技术报告 →](https://zhikunqingtao.github.io/zhikuncode/swe-bench-report.html) |
| 🚀 | **极致性能** | REST API p50 1.5ms · WS STOMP 握手 2.22ms · 490次真实请求采样验证，核心引擎零外部依赖纯 Java 实现 |
| 🏭 | **运行时可靠性** | Run 状态 CAS 原子管理 · 完整 Session 快照、Run event sequence 与待处理持久交互重放 · 进程硬超时+梯度终止 · 作用域 Grant 与子 Agent 受控继承 · Artifact declare→seal→hash 验证及显式发布 · 结构化工具结果生成工具卡片与权威下载链接 · `sid/rid/prid/agent/turn/tool/llm` 日志关联 · BestEffortObservabilityRecorder 补充事件失败隔离 · Provider 本地预算守卫 |

---

### 外观主题

支持浅色、深色、液态玻璃、星舰、花果晨、灵霄夜、果冻、蜘蛛爬虫和璀璨银河九套主题。桌面端通过顶栏「外观设置」切换，手机布局通过输入区「更多操作」中的「外观」切换；设置即时生效并保存在本地。

蜘蛛爬虫（`spider`）采用深黑底与青色／洋红／紫色霓虹蛛网，八足蜘蛛在空闲时探索、抓取文字副本，并随真实任务状态变化调整动作。选中即启用完整动效，不提供独立动效档位；原始文字仍可选择和复制。

该主题优先适配 PC，平板和手机按可用空间减少同时抓取数量。三维动效需要 WebGL 2，不可用时保留主题配色与聊天功能，页面隐藏时暂停三维绘制。相比普通主题会增加 GPU 开销；动画本身不额外调用模型。

璀璨银河（`galaxy`）以持续旋转的蓝／紫／玫红银河铺满页面，真实任务通过文件星点、工具光轨和回复星尘联动；工具详情折叠时，光效可落在执行摘要上。选中即启用完整效果，不提供独立效果开关，也不增加星图侧栏；原始文字和操作保持原位。动效需要 WebGL 2，不可用时保留静态配色与聊天功能，页面隐藏时暂停绘制。相比普通主题会增加 GPU 与电量消耗；动画本身不额外调用模型，历史消息不会重播任务动画。

果冻提供浓郁／克制样式及完整、精简、关闭三档动效，并遵循系统「减少动态效果」偏好。

花果晨与灵霄夜采用大闹天宫重彩戏曲风，分别提供暖色绢纸与深色夜景配色；使用专属强调色，不开放强调色预设切换。两套主题均提供：

- **浓郁／克制**：开启「浓郁模式」展示描金纹样、牌匾和实色消息气泡，关闭后使用克制样式；动效可独立选择完整、精简或关闭。
- **闭关**：收起装饰层，专注书写。
- **装裱分享**：将会话题名与可编辑的题跋制作成立轴、手卷或册页样式的单张 PNG 图片并导出。

### 对话工作台与修改验收

新建会话默认使用**开发工作台、标准显示方式**，简洁／开发工作台共享会话，显示方式可选精简、标准、完整过程。助手回复末尾的“本轮修改”可展开文件清单，查看本轮原生 `Edit`／`Write` 的逐次修改（仅含成功且路径可核实的操作）。

### 会话资料合并（2～5 个来源）

在会话列表选择 2～5 个已停止执行的空闲会话（可来自不同文件夹）合并为新会话，需确认主会话、新标题和模型；新会话接收交接摘要、过程文本与可确认归属的临时产物副本，工程代码不自动合并。合并期间来源会话可查看但不能执行或删除；新会话使用**“完全访问权限”（`AUTO_APPROVE`）**模式，创建后等待你的下一条指令。

### 语音识别热词配置

语音识别需配置 `LLM_PROVIDER_DASHSCOPE_API_KEY`（不能用 Token Plan Key），热词纠正在根目录 `.env` 设置 `ASR_CORRECTIONS` 后重启后端生效。格式为 `标准写法:变体1,变体2;标准写法2:变体3`，例如 `zhikuncode:zhi kun code,zkun code,智坤code;PostgreSQL:post gre sql`。配置项见 [`.env.example`](.env.example)。

## ⚡ 快速开始

### 前置准备：获取 LLM API Key

本项目需要 LLM（大语言模型）API Key 才能运行。默认使用**阿里云千问（DashScope）**，国内网络直连。

**获取千问 API Key：**
1. 访问 [阿里云百炼平台 API Key 管理](https://bailian.console.aliyun.com/cn-beijing/?tab=model#/api-key)
2. 注册或登录阿里云账号
3. 创建 API Key，复制完整密钥（以 `sk-` 开头）

> 千问提供免费额度，足够个人开发使用。也可以使用 [DeepSeek](https://platform.deepseek.com/)、[Moonshot/Kimi](https://platform.moonshot.cn/) 等国内服务商，详见下方"支持的 LLM 服务商"。

### 方式一：Docker 部署（推荐）

只需 3 步，从零到可用：

```bash
# 1. 克隆仓库
git clone https://github.com/zhikunqingtao/zhikuncode.git
cd zhikuncode

# 2. 配置 API Key
cp .env.example .env
# 编辑 .env，填入你的 LLM API Key（默认使用千问/DashScope，国内直连）

# 3. 启动
docker compose up -d
```

> **首次构建说明：** 第一次运行会自动构建 Docker 镜像，需要下载依赖并编译，预计耗时 **15-30 分钟**（取决于网络速度）。后续启动只需几秒。可通过 `docker compose logs -f` 查看构建进度。

启动完成后，打开浏览器访问 **http://localhost:8080** 即可使用。

> 基础 `docker-compose.yml` 默认只启动 Java 后端（由它提供内置静态前端）。Docker 镜像已包含 Python 运行时与服务代码，但不会默认启动；需要容器内 Python 服务时，请通过自己的 Compose override 显式传入 `PYTHON_SERVICE_AUTO_START=true`、`PYTHON_SERVICE_PATH=/app/python-service`、`PYTHON_SERVICE_EXECUTABLE=/app/python-service/.venv/bin/python` 和 `WORKSPACE_ROOT=/app/workspace`，然后使用两个 Compose 文件重新创建容器。若还要让浏览器使用直连 Python 的界面能力，override 必须额外把 Python 绑定到容器接口、仅映射到宿主机 loopback，并通过反向代理开放所需的精确路由；不要把 `8000` 端口直接暴露到公网。

> **系统要求：** Docker 20.10+，Docker Compose V2，建议 4GB+ 内存。

### 方式二：本地开发

**前置条件：** JDK 21、Node.js 22+、Python 3.11~3.12（不支持 3.13+）

```bash
git clone https://github.com/zhikunqingtao/zhikuncode.git
cd zhikuncode

# 配置环境变量
cp .env.example .env
# 编辑 .env，填入你的 LLM API Key

# 停止旧进程后启动三端服务
./stop.sh
./start.sh
```

三端服务会同时启动：

| 服务 | 地址 | 说明 |
|------|------|------|
| **Backend** | `http://localhost:8080` | Java Spring Boot 后端，核心 API |
| **Python Service** | `http://localhost:8000` | FastAPI 服务，代码分析 |
| **Frontend** | `http://localhost:5173` | React 开发服务器 |

> `./start.sh` 默认把仓库根目录设为 workspace；仅当 allowed roots 和本地 picker 开关都没有非空配置时，才自动启用直连本机目录浏览。

#### 本地工作台使用说明

- 首次使用默认采用**开发工作台**，未选择会话时显示欢迎页；可通过页面顶部随时切换到**简洁工作台**。
- 简洁工作台面向结果，展示当前 Root Run 对应的要求、最终回复、主要成果、待处理事项、近期活动和验收状态，不把旧执行结果混入本轮交付。
- 开发工作台保留完整对话、工具调用、文件、Diff、Git、终端、浏览器、Agent 和证据视图。
- 视图选择保存在当前浏览器中，并支持按 Session 记住选择；切换视图不会中断任务或改变运行状态。
- PDF、图片、文本和 Markdown 等支持在工作台内安全预览；其他文件可切换到开发工作台文件区处理。
- “在文件夹中显示”仅适用于从本机浏览器直连本地 ZhikunCode 的场景。

<details>
<summary><b>手动分别启动各服务</b></summary>

```bash
# 后端（从仓库根目录启动，仅适用于直连本机开发）
export ZHIKUN_DEFAULT_WORKSPACE="$PWD"
export ZHIKUN_LOCAL_PICKER_ENABLED=true
cd backend && ./mvnw spring-boot:run -DskipTests

# Python 服务（另开终端，从仓库根目录启动）
cd python-service
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
export WORKSPACE_ROOT="$(cd .. && pwd)"
export ZHIKUN_LOCAL_PICKER_ENABLED=true
export PYTHONPATH="$PWD/src"
uvicorn src.main:app --host 127.0.0.1 --port 8000

# 前端（另开终端，从仓库根目录启动）
cd frontend && npm install && npm run dev
```

</details>

> **RV-1 运行时验证依赖**：`jsonpath-ng`（JSONPath 断言引擎）、`httpx`（异步 HTTP 客户端），已包含在 `python-service/requirements.txt` 中。

> **权限数据说明：** 当前授权架构以 V015 持久交互和 V019 受约束 Grant 为数据库权威，不读取旧权限表。开发环境升级时直接重建项目数据库，并在新版本中重新授权。

### 可选：OSS 产物发布、截图粘贴与远程文件引用

ZhikunCode 提供内置 `/publish-oss` Skill，可从同一持久化根 Session 内的根 Run 与通过 `parent_run_id` 建立的后代 Run 中选择一个已验证产物条目，发布为 OSS 永久公开链接。底层 OSS 发布能力**默认关闭且绝不自动上传**，需单独配置启用；Skill 管理页中的开关不替代部署配置。生成文件、完成 Run、预览或打开文件都不会触发上传；每次发布都必须由用户明确提出，并通过一次高风险权限确认。

启用同一套 OSS 配置后，浏览器还能感知从其他应用复制并粘贴到对话框的 PNG/JPEG/WebP 截图（单张不超过 5 MiB），通过固定后端通道立即上传，并将服务端验证过的 OSS 图片地址直接交给视觉模型。这个路径不调用 `/publish-oss` Skill，也不额外调用 LLM；OSS 未配置时自动降级为 Base64 直传，无需额外配置即可使用图片分析能力。

“引用本地文件”会按实际访问能力选择路径：只有直接 loopback、无代理转发且原生选择器安全门禁全部满足时，才只发送 canonical 路径；ECS、远程和代理访问则使用浏览器文件选择器，选中后立即上传到 `${ZHIKUN_OSS_PREFIX}/local-files/`，并把文件名与 OSS 地址加入提示词。远程文件默认沿用 `ZHIKUN_OSS_MAX_FILE_BYTES`（100 MiB）上限，OSS 未配置时该入口不可用且不会降级为 Base64。该通道接受任意文件类型，不执行敏感文件名或内容扫描；对象发布为永久 `public-read`，移除标签、切换 Session 或放弃消息都不会删除它，使用前请确认文件可以公开。

凭证模式默认为 `auto`：本机存在完整的标准 `ALIBABA_CLOUD_ACCESS_KEY_ID`/`ALIBABA_CLOUD_ACCESS_KEY_SECRET` 时优先使用阿里云默认凭证链；否则，配置了 `ZHIKUN_OSS_ECS_ROLE_NAME` 时使用 **ECS RAM Role + IMDSv2**；两者都没有时仍尝试默认凭证链（例如阿里云 CLI 默认 Profile）。因此同一套非密钥配置可同时支持本地一键启动和 ECS。每个部署者都必须使用自己的 Bucket 与最小权限身份；仓库不包含维护者的 OSS 凭证。

在 `.env` 中配置：

```bash
ZHIKUN_OSS_ENABLED=true
ZHIKUN_OSS_ENDPOINT=https://oss-cn-your-region.aliyuncs.com
ZHIKUN_OSS_REGION=cn-your-region
ZHIKUN_OSS_BUCKET=your-bucket
ZHIKUN_OSS_PUBLIC_BASE_URL=
ZHIKUN_OSS_PREVIEW_ENABLED=false
ZHIKUN_OSS_PREFIX=zhikuncode-artifacts
ZHIKUN_OSS_ECS_ROLE_NAME=your-ecs-ram-role
ZHIKUN_OSS_CREDENTIAL_MODE=auto
ZHIKUN_OSS_MAX_FILE_BYTES=104857600
ZHIKUN_OSS_CONNECT_TIMEOUT_MS=10000
ZHIKUN_OSS_REQUEST_TIMEOUT_MS=120000
```

可选自定义域名与预览：先自行完成目标 Bucket 的域名绑定、DNS 和 HTTPS 配置，再将 `ZHIKUN_OSS_PUBLIC_BASE_URL` 设为自己的 HTTPS 域名根地址（例如 `https://files.example.com`，不带端口、路径前缀、查询参数或片段）。产物发布、截图粘贴和远程文件引用会统一使用该域名，上传 Endpoint 不变。设置 `ZHIKUN_OSS_PREVIEW_ENABLED=true` 后，仅新上传的 HTML、纯文本、PDF、PNG/JPEG/GIF/WebP 使用 `inline`，其他类型仍作为附件；开启预览必须配置自定义域名，不能使用 OSS 默认域名。默认留空且关闭时保持原下载行为。

OSS 关闭时，无效的自定义域／预览配置会产生警告并从 CSP 省略，不阻断启动；开启时仍会阻止启动。合法自定义域在 OSS 关闭时仍保留在 CSP 中，以支持历史图片。发布入口始终保留严格配置校验。剪贴板 API 会规范化 HEAD 返回的具体图片 MIME（统一大小写、去除参数），保留有效 CDN 转码类型；其他类型回退到文件字节检测结果。客户端声明的图片类型仍须匹配上传内容。

本地部署可先配置阿里云 CLI 默认 Profile；也可将受限 RAM 用户或临时 STS 的 `ALIBABA_CLOUD_ACCESS_KEY_ID`、`ALIBABA_CLOUD_ACCESS_KEY_SECRET` 与可选 `ALIBABA_CLOUD_SECURITY_TOKEN` 写入本机 `.env`。不要提交真实值。旧式 `OSS_ACCESS_KEY_ID`、`OSS_ACCESS_KEY_SECRET`、`OSS_SESSION_TOKEN` 会被拒绝。

> 身份只应具有目标 Bucket/前缀所需的最小 `PutObject`、`GetObject/HeadObject`、`PutObjectAcl` 和失败清理 `DeleteObject` 权限；Bucket 必须允许目标对象设置 `public-read`，否则上传会失败并尝试清理私有对象。

使用流程：

1. 在当前持久化根 Session 中生成产物；Manifest 完成 declare → seal/hash → verify 后，状态可以是 `verified`，也可以是包含目标已验证条目的 `partial`。
2. 明确输入 `/publish-oss <文件路径>`，或说明“上传刚生成的产物到 OSS”。
3. 核对确认卡片中的文件名、大小、公开范围和“永久公开”警告后，批准本次操作。
4. 上传成功后使用发布成功卡片打开预览或下载；以浏览器实际响应为准，不让模型重新拼接链接。

安全边界与当前限制：

- 只允许同一持久化根 Session 内根 Run 或授权后代 Run 所声明、目标条目已验证且仍匹配 Manifest 哈希的 workspace 内**单个普通文件**，默认不超过 100 MiB。
- 拒绝目录、批量上传、符号链接、workspace 外路径、`.env`、私钥、数据库、凭证配置及检测到敏感内容的文件。
- 对象先私有上传，远端校验成功后才切换为 `public-read`；失败时清理本次新建的私有对象。
- 返回地址为**永久公开链接**。卡片依据公开地址的响应判断预览或下载；检查失败时保守显示“下载”，不会撤销已成功的发布。OSS 默认域名通常会下载 HTML。
- 旧对象的内容、元数据及历史消息链接不会迁移；重复发布旧对象可返回当前配置域名，但原附件仍可能下载。关闭预览也不会恢复已上传对象的元数据。
- HTML 预览会执行页面脚本。分享域不得共享应用登录 Cookie 或加入应用认证接口的跨域白名单；同站子域名不等于完整安全隔离。注意 HTTPS 证书续签，不承诺所有浏览器均可预览所有格式。
- 当前精简版不提供批量发布、发布历史或撤销入口；删除公开对象需要运维人员在 OSS 侧显式执行。
- 本地与 ECS 都支持真实上传；本地使用默认凭证链，ECS 建议使用自动轮换的 RAM Role 临时凭证。
- 远程文件引用使用原始请求体流式上传，不扩大 Spring 的全局 multipart 限制；若 ECS 前还有反向代理，代理的请求体上限也必须不低于 `ZHIKUN_OSS_MAX_FILE_BYTES`。

### 支持的 LLM 服务商

ZhikunCode 支持**多 Provider 同时配置**（推荐）和单 Provider 两种模式。多 Provider 模式下可在前端自由切换模型：

**方式一：多 Provider 配置（推荐）**

在 `.env` 中为每个服务商配置独立的 API Key，前端可自由切换：

```bash
# DashScope（千问系列）
LLM_PROVIDER_DASHSCOPE_API_KEY=your-dashscope-key

# DashScope Token Plan（百炼订阅专属 sk-sp- Key，与按量计费 Key 分离）
LLM_PROVIDER_DASHSCOPE_TOKEN_PLAN_API_KEY=your-token-plan-key

# DeepSeek
LLM_PROVIDER_DEEPSEEK_API_KEY=your-deepseek-key

# Moonshot (Kimi)
LLM_PROVIDER_MOONSHOT_API_KEY=your-moonshot-key

# Kimi Code 订阅：K3 + K2.8 Preview（与 Moonshot 按量渠道独立）
LLM_PROVIDER_KIMI_CODE_API_KEY=your-kimi-code-key
# LLM_PROVIDER_KIMI_CODE_MODELS=k3,kimi-for-coding

# Zhipu (智谱 GLM)
LLM_PROVIDER_ZHIPU_API_KEY=your-zhipu-api-key-here

# MiniMax
LLM_PROVIDER_MINIMAX_API_KEY=your-minimax-api-key-here

# ZenMux（默认目录：Fable 5.1 / Opus 5.5 / Sonnet 5.5 / Haiku 5.5 / GPT-5.6 Sol / GPT-6 Astra / Gemini 3.8 Flash / Grok 4.6）
# 支持逗号分隔多 Key：订阅 Key（sk-ss-v1- 前缀）放前优先、按量 Key（sk-ai-v1- 前缀）兜底；
# 402 quote_exceeded / 404 model_not_available 时自动冷却 15 分钟切换到下一把 Key。
LLM_PROVIDER_ZENMUX_API_KEY=your-zenmux-api-key-here
```

**Kimi Code 订阅：** 配置 `LLM_PROVIDER_KIMI_CODE_API_KEY` 并重启后，可选择 **Kimi K3（订阅）**（`k3`）或 **Kimi K2.8 Preview（订阅）**（`kimi-for-coding`）。两者走 `https://api.kimi.com/coding/v1`，流式与非流式调用均固定 `thinking.type=enabled`、`reasoning_effort=max`，上下文配置为 **1,048,576 tokens**，单次输出预算为 131,072 tokens（应用上限，非官方最大输出声明）。K3 的 1M 权限要求 Pro / Allegretto 及以上套餐；K2.8 Preview 对具备 coding 权益的会员开放 1M。订阅模型 ID、密钥和路由独立于按量 `kimi-k3`，不自动跨渠道切换；本地启动与 Docker Compose 均支持。订阅用量不折算为 Moonshot 按量价格，界面估算为 0 不代表免费。模型 ID 与规格核对日期：2026-09-20，见 [官方模型配置](https://www.kimi.com/code/docs/kimi-code/models.html)。

**GLM-5.3（百炼）：** 复用 `LLM_PROVIDER_DASHSCOPE_TOKEN_PLAN_API_KEY`，默认模型列表已包含 `bailian/glm-5.3`；若 `.env` 自定义了 `LLM_PROVIDER_DASHSCOPE_TOKEN_PLAN_MODELS`，请将该 ID 加入列表并重启。内部模型 ID 为 `bailian/glm-5.3`，仅发往百炼 Token Plan 的请求使用上游 ID `glm-5.3`，现有 `glm-5.3` 仍走智谱直连。百炼配置中填写裸 `glm-5.3` 也会自动规范化并去重，避免注册顺序影响路由。流式与非流式均固定 `enable_thinking=true`、`reasoning_effort=max`、`clear_thinking=false`，配置最大 **1,000,000 tokens** 上下文和 65,536 tokens 单次输出预算（已实测接受的应用预算，非官方最大输出声明）；支持工具调用与历史思考回传，文本模型不开放图片输入。订阅 Credits 以百炼账单为准，界面 0 单价不代表免费。2026-09-21 核对：[Token Plan 支持模型](https://help.aliyun.com/zh/model-studio/token-plan-personal-overview)、[GLM 参数](https://help.aliyun.com/zh/model-studio/glm)、[官方上下文配置](https://help.aliyun.com/zh/model-studio/openclaw)。

**方式二：单 Provider 配置（向后兼容）**

如未配置多 Provider，系统自动回退到单 Provider 模式。在 `.env` 中配置 `LLM_BASE_URL` 和 `LLM_API_KEY` 即可切换：

| 服务商 | Base URL | 推荐模型 | 备注 |
|--------|----------|----------|------|
| **千问/DashScope** | `https://dashscope.aliyuncs.com/compatible-mode/v1` | qwen3.8-max-0902 | 按量计费 Provider，国内直连 |
| **阿里云百炼 Token Plan** | `https://token-plan.cn-beijing.maas.aliyuncs.com/compatible-mode/v1` | qwen3.8-max / qwen3.8-flash / deepseek-v4-pro-0813 / deepseek-v4-flash-0731 / deepseek-v4.1-flash | 使用独立 `sk-sp-` Key；模型均标注“百炼”。V4.1 Flash 为服务端 `app.model.default`、快速查询及图片兜底的默认值；前端初始模型偏好仍为 `qwen3.8-max-0902`，用户配置／会话选择优先 |
| **DeepSeek** | `https://api.deepseek.com/v1` | deepseek-flash | 国内直连；DeepSeek V4.1 Flash，支持思考、工具调用与原生视觉 |
| **Moonshot（Kimi）** | `https://api.moonshot.cn/v1` | kimi-k3 | 国内直连；kimi-k3 支持 1M 上下文和原生视觉 |
| **Zhipu（智谱 GLM）** | `https://open.bigmodel.cn/api/paas/v4/chat/completions` | glm-5.3, glm-5.3-flash | 国内直连 |
| **MiniMax** | `https://api.minimax.chat/v1` | MiniMax-M3 | 百万上下文 |
| **ZenMux（多模型中转）** | `https://zenmux.ai/api/v1` | anthropic/claude-fable-5.1 / anthropic/claude-opus-5.5 / anthropic/claude-sonnet-5.5 / anthropic/claude-haiku-5.5 / openai/gpt-5.6-sol / openai/gpt-6-astra / google/gemini-3.8-flash / x-ai/grok-4.6 | OpenAI/Google/xAI 模型使用 Responses 推理与工具续轮；支持图片 |
| **OpenAI** | `https://api.openai.com/v1` | gpt-5.6-sol / gpt-5.4-mini | 需要外网访问 |
| **本地 Ollama** | `http://localhost:11434/v1` | 支持所有 Ollama 模型（ollama/*） | 完全离线 |

> 任何兼容 OpenAI API 格式的服务商都可以接入，只需配置对应的 Base URL 和 API Key。

### 可选：启用 DashScope 托管 MCP 服务

ZhikunCode 当前预置了 17 个阿里云百炼 MCP 服务、共 83 个白名单工具。运行时采用服务级最小化默认策略：智谱联网搜索、高德地图、千问图像和万相视频默认开启；新闻、法律、企业信息、文本审核、金融、学术、采购、物流、行情和行业洞察等 13 个低频或高风险服务默认关闭。没有配置百炼 Key 时会跳过远端连接，不影响核心对话、代码编辑和本地工具使用。

默认关闭或被用户关闭的 MCP 不建立连接、不注册工具，也不会向模型上下文注入工具描述；直接调用会被拒绝。点击页面顶部的 **MCP** 徽章可打开 **MCP 管理**，按服务即时启用或关闭，选择保存在本机且无需重启。

| MCP 服务 | 传输 | 能力 | 工具数 |
|---------|------|------|-------|
| 高德地图 | SSE | 地理编码、IP 定位、天气、搜索、距离与四类路线规划等 | 13 |
| 千问-图像生成（QwenImage） | HTTP | 文生图、单图编辑、多图融合 | 3 |
| 万相-视频生成（WanVideo） | HTTP | 文生视频、图生视频、数字人、首尾帧视频及结果查询 | 8 |
| OneKey 新闻查询 | HTTP | 频道、热榜、按频道或标题检索新闻 | 3 |
| OneKey 得理法律数据 | HTTP | 法规与类案检索 | 2 |
| OneKey 上奇企业工商 | HTTP | 企业匹配、工商、股东、人员、投资、分支、联系方式 | 7 |
| OneKey 文本内容审核 | HTTP | 违规、推广、辱骂、低质和广告法风险审核 | 1 |
| `zhipu-websearch` | SSE | 智谱联网搜索 Pro | 1 |
| 东方财富妙想 | HTTP | 股票行情、公告、研报、财务、资金与市场数据查询 | 11 |
| 企业知识产权 | HTTP | 企业知识产权信息查询 | 1 |
| 万方文献 | HTTP | 学术文献检索与详情查询 | 2 |
| arXiv 论文 | SSE | 论文搜索、详情、作者与分类查询 | 4 |
| 1688 选品 | HTTP | 商品选品与货源查询 | 1 |
| 物流快递 | SSE | 快递物流查询与轨迹跟踪 | 2 |
| 贵金属行情 | HTTP | 黄金、白银等贵金属行情与市场数据 | 6 |
| 连锁商业 / 茶饮洞察 | HTTP | 连锁品牌、门店、商圈与茶饮市场洞察 | 8 |
| 旅游洞察 | HTTP | 景区、客流、酒店与旅游市场数据分析 | 10 |

**如需使用**（需要阿里云百炼 API Key，并在控制台开通相应 MCP 能力；部分服务调用可能产生费用，具体以百炼控制台为准）：

1. 在 `.env` 中配置 DashScope Key：
   ```bash
   LLM_PROVIDER_DASHSCOPE_API_KEY=sk-xxxxxxxx
   ```
2. 首次修改 `.env` 后，通过 `./stop.sh && ./start.sh` 完整重启三端。
3. 在页面顶部打开 **MCP 管理**，仅启用当前任务需要的服务；后续开关即时生效，无需重启。

> 注册表中的 `"enabled": true` 表示该工具进入管理员白名单，不等于服务在运行时默认开启。工具必须同时通过注册表白名单、服务开关和凭证可用性三层检查。

---

## 🏆 SWE-bench Lite 评测

ZhikunCode 已完成 SWE-bench Lite（300 实例，pass@1）官方 harness 评测，**Resolve Rate 56.0% (168/300)**。所有评测产物（`all_preds.jsonl`、`results.json`、`metadata.yaml`、轨迹）已开源在 [`docs/swe-bench/20260525/`](docs/swe-bench/20260525/)，可第三方复现。

### 关键指标

| 指标 | 数值 | 出处 |
|---|---|---|
| Resolved Instances | **168 / 300 (56.0%)** | `docs/swe-bench/20260525/results.json` `resolved=168` |
| Patch 生成率 | **284 / 300 (94.7%)** | `all_preds.jsonl`（其中 16 条空 patch） |
| 历史主干模型（保留原记录） | `qwen3.7-max` | `docs/swe-bench/20260525/metadata.yaml` |
| 工具闭集 | Read / Edit / Write / Bash / Grep / Glob | [`swe-bench/swe_bench.py`](swe-bench/swe_bench.py) `ALLOWED_TOOLS` |
| 单实例预算 | 60 轮 / 900 秒 | [`swe_bench.py`](swe-bench/swe_bench.py) `solve_instance(max_turns=60, timeout=900)` |
| 并发 worker | 1 | `--workers` 默认值 |
| 网络 / Sub-agent | 均禁用 | 系统提示显式声明 |
| 提交命名空间 | `20260525_zhikuncode` | `metadata.yaml` |

### 仓库级表现（`results/resolved_by_repo.json`）

| Repository | Resolved / Total | Resolve Rate |
|---|---|---|
| mwaskom/seaborn | 3 / 4 | **75.0%** |
| django/django | 82 / 114 | **71.9%** |
| astropy/astropy | 4 / 6 | **66.7%** |
| sympy/sympy | 42 / 77 | 54.5% |
| scikit-learn/scikit-learn | 12 / 23 | 52.2% |
| pytest-dev/pytest | 8 / 17 | 47.1% |
| pydata/xarray | 2 / 5 | 40.0% |
| matplotlib/matplotlib | 8 / 23 | 34.8% |
| psf/requests | 2 / 6 | 33.3% |
| sphinx-doc/sphinx | 4 / 16 | 25.0% |
| pylint-dev/pylint | 1 / 6 | 16.7% |
| pallets/flask | 0 / 3 | 0.0% |
| **Total** | **168 / 300** | **56.0%** |

### 工程亮点（每一项均可在源码定位）

- **Agent-Loop 显式四相位** ANALYZE→LOCATE→FIX→VERIFY，相位边界由系统提示硬约束（[swe_bench.py](swe-bench/swe_bench.py)）
- **六层上下文压缩级联** Snip / MicroCompact / ContextCollapse / AutoCompact / CollapseDrain / ReactiveCompact（[ContextCascade.java](backend/src/main/java/com/aicodeassistant/engine/ContextCascade.java)，源码注释中 Level 1.5 ContextCollapse 为渐进折叠中间层）
- **413 两阶段恢复** CollapseDrain → ReactiveCompact，保障 60 轮会话收敛于上下文窗口内
- **自纠错循环（SelfCorrectionLoop）** 编译/测试失败结构化再提示，默认 MAX_ATTEMPTS=3，SWE-bench 模式提升至 7 次（[SelfCorrectionLoop.java](backend/src/main/java/com/aicodeassistant/engine/correction/SelfCorrectionLoop.java)）

📄 完整方法学与可复现命令见技术报告：<https://zhikunqingtao.github.io/zhikuncode/swe-bench-report.html>

---

## 📊 竞品对比

### 功能对比

| 特性 | ZhikunCode | Aider | Cline | Cursor | Claude Code | Copilot |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| 开源免费 | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Web UI | ✅ 全功能 | ⚠️ 实验浏览器 UI | ❌ | ⚠️ Web版 | ✅ | ⚠️ GitHub.com |
| Docker 一键自托管 | ✅ 完整 Web 服务 | ⚠️ CLI 容器化 | ❌ | ⚠️ 企业付费 | ❌ | ❌ |
| 国产大模型直连 | ✅ 原生支持 | ⚠️ 需配置兼容 API | ⚠️ 需配置兼容 API | ❌ | ❌ | ❌ |
| 多 Agent 协作 | ✅ Agent 委派 + 后台任务 | ❌ | ✅ Kanban + CLI 并行 | ✅ Multi-Agents | ✅ Sub-Agents | ✅ /fleet + Agent Mode |
| 浏览器全流程操控¹ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 安全沙箱 | ✅ 8层 | ❌ | ❌ | ⚠️ 企业级 | ✅ OS级 | ⚠️ GitHub 权限策略 |
| MCP 工具扩展 | ✅ | ⚠️ 第三方 | ✅ | ✅ | ✅ | ✅ |
| CLI 终端工具 | ✅ aica + 35+ 斜杠命令 | ✅ CLI-first | ✅ CLI 2.0 | ✅ Cursor CLI | ✅ CLI-only | ✅ Copilot CLI |
| 可扩展skill技能系统 | ✅ Markdown 驱动 + 内置/项目/用户技能 | ❌ | ❌ | ✅ Rules | ✅ Hooks | ❌ |
| 插件系统 | ✅ Java SPI 插件 + 沙箱隔离 + 热重载 | ❌ | ❌ | ✅ Plugins | ✅ Skills/Hooks | ✅ Plugins |
| 跨会话记忆 | ✅ 三层记忆 + BM25 搜索 | ❌ | ❌ | ✅ Rules | ✅ Memory | ❌ |
| 活动追踪与审批 | ✅ L1/L2/L3 三层 | ❌ | ❌ | ❌ | ✅ 权限管理 | ❌ |
| Activity 持久化 | ✅ SQLite + STOMP | ❌ | ❌ | ❌ | ⚠️ 内存级 | ❌ |
| 无需安装客户端 | ✅ | ❌ | ❌ | ⚠️ | ✅ | ❌ |

> ¹ **浏览器全流程操控**：部署后任意设备浏览器（包括手机）即可完整操控编码全流程——权限审批、方案协商、任务管控。这与 Cline/Cursor 的"AI 控制浏览器做自动化测试"是不同的概念。

### 安全特性对比

| 安全特性 | ZhikunCode | Aider | Cline | Claude Code |
|---------|:---:|:---:|:---:|:---:|
| 命令执行沙箱 | 8 层检查 | ❌ 用户审批 | ❌ 用户审批 | ✅ gVisor/Firecracker |
| 工具授权 | 统一 Tool Gateway + 执行前动态复检 | ❌ | 简单确认 | 权限管理系统 |
| 安全测试覆盖 | 权限/Bash/路径/并发专项测试 | 未公开 | 未公开 | 未公开 |
| 敏感路径拦截 | ✅ | ❌ | ❌ | ❌ |
| 危险命令阻断 | ✅ | ❌ | ❌ | ✅ 部分 |
| 环境变量白名单 | ✅ | ❌ | ❌ | ❌ |

> **说明：** 以上对比基于各项目公开文档（截至 2026 年 4 月），AI 编程工具迭代迅速，如有不准确之处欢迎提 [Issue](https://github.com/zhikunqingtao/zhikuncode/issues) 指正。Cline CLI 2.0、Cursor 2.0+、Claude Code Desktop、GitHub Copilot /fleet 等均在快速迭代中。
>
> **最新动态（2026 年 4 月）：** Claude Code Desktop App 已发布（支持本地+云端混合执行）；Cursor 3.1 新增 Canvas 特性（交互式仪表盘+自定义 UI 组件）；各竞品最新版本号：Aider v0.86+、Cline v1.0.35+、Cursor 3.1+、Claude Code 2.1.119+、GitHub Copilot CLI 1.0.35+。

#### ZhikunCode 差异化能力展示

| 能力维度 | ZhikunCode 实现 | 技术亮点 |
|---------|----------------|----------|
| 上下文压缩 | ✅ 6层级联压缩 + 413两级上下文压缩 | ContextCascade 支持从 L0 Snip 到 L4 ReactiveCompact 渐进式压缩 |
| 运行时验证（Runtime Verification） | ✅ 三模态运行时验证 + 7类证据链 | VerifierFactory 分发（browser/http_api/auto），Feature Flag 控制 |
| MCP 传输协议 | ✅ 4种传输方式(StdIO/SSE/WebSocket/HTTP) | Client+Server 双向模式，覆盖本地与远程全场景 |
| SWE-bench 实测 | ✅ 56.0% 通过率（开源可复现） | 完整评测流程开源，支持独立验证 |

---

## 🏗️ 架构概览

ZhikunCode 采用三端分离架构，Java 后端负责核心编排，React 前端提供交互界面，Python 服务处理代码分析：

```
┌──────────────────┐      WebSocket / HTTP      ┌──────────────────────┐
│    Frontend       │ ◄────────────────────────► │      Backend          │
│  React 18 + TS    │                            │  Java 21 + Spring    │
│  Vite + Tailwind  │                            │  Boot 3.4            │
│  :5173 (dev)      │                            │  :8080               │
└──────────────────┘                            └──────────┬───────────┘
                                                           │ HTTP
                                                           ▼
                                                ┌──────────────────────┐
                                                │   Python Service      │
                                                │   FastAPI + Uvicorn   │
                                                │   :8000               │
                                                └──────────────────────┘
```

### 各层职责

| 层 | 技术栈 | 职责 |
|----|--------|------|
| **后端** | Java 21, Spring Boot 3.4.x, WebSocket, SQLite | 核心编排引擎、LLM API 路由、Agent 管理、内置工具与 MCP 动态扩展、统一授权网关、会话持久化 |
| **前端** | React 18, TypeScript 5.6, Vite 5, TailwindCSS, Monaco Editor, xterm.js, Zustand | 对话式交互 UI、代码编辑器、内置终端、文件浏览器、设置面板、实时流式输出、委派结果查看 |
| **Python 服务** | FastAPI, Uvicorn, Python 3.11+ | 代码分析、AST 解析、MCP 工具桥接 |

### Docker 部署架构

生产环境通过 Docker 单容器部署。镜像包含 Java 后端、内置静态前端和 Python 运行时；基础 Compose 默认只启动 Java 进程，受管 Python 服务需通过显式的环境变量/override 启用：

```
┌─────────────────────────────────────────────────┐
│                Docker Container                  │
│  ┌───────────┐  ┌───────────┐  ┌──────────────┐ │
│  │  Backend   │  │  Python*  │  │   Frontend   │ │
│  │  :8080     │  │  :8000    │  │  (静态文件)   │ │
│  └───────────┘  └───────────┘  └──────────────┘ │
│                                                  │
│  Volume: zhikun-data (SQLite + 会话数据)          │
│  Volume: workspace (用户项目代码)                  │
├──────────────────────────────────────────────────┤
│  Port: 8080 → 宿主机                              │
└──────────────────────────────────────────────────┘
```

`*` Python 服务为可选的容器内受管进程，不对外暴露端口，也不由基础 Compose 默认启动。

### 核心引擎（Core Engines）

ZhikunCode 的智能决策由以下核心引擎协同驱动：

| 引擎 | 职责 | 关键特性 |
|------|------|----------|
| **查询引擎（QueryEngine）** | Agent 决策与工具执行编排 | 多步迭代循环，驱动完整 Agent Loop |
| **授权服务（AuthorizationService）** | 统一策略与授权裁决 | 系统不变量、权限模式、Grant 匹配、持久交互 |
| **操作分析器（OperationAnalyzerRegistry）** | 工具语义与风险分析 | 文件、Bash、网络、MCP/动态工具分类 |
| **工具授权网关（ToolExecutionGateway）** | 工具执行唯一入口 | 执行槽、最终授权复检、结构化执行结果 |
| **权限 Grant 仓库（PermissionGrantRepository）** | 授权保存、匹配和撤销 | RUN/SESSION/WORKSPACE 作用域与父子 Agent 继承 |
| **上下文级联（ContextCascade）** | 上下文压缩与恢复 | 6层级联 + 413两级上下文压缩 |
| **图片注入器（ImageRefInjector）** | 图片引用安全注入与预算管理 | 候选选取、动态预算、完整性校验和去重 |
| **Token预算守卫（TokenBudgetGuard）** | 两阶段 Token 预算控制 | 历史 Base64 预清理 + 最终 payload 梯度降级 |
| **工具执行管线（ToolExecutionPipeline）** | 工具执行全生命周期 | 校验、输入冻结、授权、执行和结果归一化 |
| **自纠错循环（SelfCorrectionLoop）** | 错误诊断与自动修复 | MAX_ATTEMPTS=3(默认)/7(SWE-bench) |
| **RunControlService** | Run 生命周期 CAS | 状态原子更新，COMPLETED/FAILED/CANCELLED/INTERRUPTED 单一终态权威 |
| **RunExecutionRegistry** | 活跃 Run 执行注册 | 以 Session 映射内存活跃 Run、输入队列与取消上下文；不承担 checkpoint 持久化 |
| **DurableInteractionService** | 持久交互 | Inbox、ACK、服务端 deadline、CAS 终态与重连恢复 |
| **Project 工作空间服务** | Project 选择与信任边界 | 持久授权、真实路径规范化、Session 工作目录固定、符号链接/别名/重绑定及越界复检 |
| **Artifact Manifest 与发布策略** | 验证产物归属和显式发布 | 从同一根 Session 的 `verified` 或 `partial` Manifest 中选择已验证条目，发布前复核哈希 |
| **BestEffortObservabilityRecorder** | 补充观测故障隔离 | 有界异步事件队列、丢弃/写失败指标；记录失败不反向破坏主执行链 |
| **日志关联与恢复投影** | 诊断关联和断线恢复 | MDC 提供 `sid/rid/prid/agent/turn/tool/llm`；完整 Session 快照、Run event sequence、活跃工具状态及持久交互重放恢复前端 |

### Agent Loop 查询循环

ZhikunCode 的 QueryEngine 通过多步迭代循环驱动 Agent 决策与工具执行：

```
压缩级联（ContextCascade）→ 流式会话创建 → API 调用（含熔断、自适应重试和降级保护）→ 响应收集 → 工具结果消费（ToolExecutionPipeline）→ 终止评估 → 工具摘要注入 → 状态更新
```

**关键子系统：**

| 组件 | 职责 | 配置项 |
|------|------|--------|
| IncrementalCollapseManager | 每10轮触发一次增量上下文折叠 | `context.cascade.incremental-collapse.enabled` |
| ContextCascade | 六层压缩级联（Snip→MicroCompact→ContextCollapse→AutoCompact→CollapseDrain→ReactiveCompact） | `context.cascade.*` |
| MicroCompactService | 清除旧工具结果内容，降低上下文体积 | `features.flags.CACHED_MICROCOMPACT` |
| ModelTierService | 模型降级链管理，30分钟冷却期自动恢复 | `app.model.tier-chain` |

**413 恢复**：由 [QueryEngine.java](backend/src/main/java/com/aicodeassistant/engine/QueryEngine.java) 编排，先尝试两级上下文压缩：
1. **Level 3** — CollapseDrain 激进压缩（contextWindow × 0.5 目标）
2. **Level 4** — ReactiveCompact 反应式压缩（仅保留 1 轮 + 极度压缩）

若仍失败且错误与媒体相关，再尝试移除媒体块；恢复耗尽后释放错误并终止，不继续落入普通模型降级。两级压缩不等同于完整错误恢复链路。

<details>
<summary><b>六层压缩级联（ContextCascade）详解</b></summary>

| 层级 | 名称 | 语义 | 触发条件 |
|------|------|------|----------|
| L0 | Snip（首选裁剪） | 优先裁剪工具输出中的冗余内容 | 上下文接近阈值 |
| L1 | MicroCompact（微压缩） | 清除旧工具结果，降低上下文体积 | L0 不足 |
| L1.5 | ContextCollapse（渐进折叠） | 增量折叠中间层，每10轮触发 | 配置启用 |
| L2 | AutoCompact（自动压缩） | 系统自动压缩全局上下文 | 常规阈值突破 |
| L3 | CollapseDrain（激进压缩） | contextWindow × 0.5 目标，413恢复Phase1 | 413错误第一阶段 |
| L4 | ReactiveCompact（反应式压缩） | 仅保留1轮 + 极度压缩，413恢复Phase2 | 413错误第二阶段 |

源码：`ContextCascade.java`

</details>

---

## 🔒 安全架构

安全是 ZhikunCode 的核心设计原则。每一条命令执行前，都要经过多层安全检查。

### 8 层 Bash 安全沙箱

所有 Shell 命令执行前，必须通过以下 8 层检查：

| 层级 | 检查内容 | 说明 |
|------|---------|------|
| **第 1 层** | 命令解析 | 解析命令结构，识别管道、重定向、子命令 |
| **第 2 层** | 黑名单过滤 | 三级拦截体系（ABSOLUTE_DENY/HIGH_RISK_ASK/AUDIT_LOG），阻断已知危险命令（`rm -rf /`、`mkfs`、`dd`、`format` 等），含 ReDoS 正则防护 |
| **第 3 层** | 路径遍历检测 | 防止 `../` 路径穿越攻击，阻断设备路径、UNC 路径 |
| **第 4 层** | 权限验证 | 统一授权网关裁决，敏感操作需用户审批 |
| **第 5 层** | 沙箱执行 | 破坏性命令强制在 Docker 沙箱中执行（只读文件系统 + 内存限制 + 网络隔离） |
| **第 6 层** | 参数净化 | 环境变量白名单、命令注入防护 |
| **第 7 层** | 输出校验 | 检测异常输出，敏感信息脱敏 |
| **第 8 层** | 审计日志 | 完整记录每次命令执行，可追溯 |

### 统一工具授权流程

所有核心工具执行都经过同一条不可绕过的授权链：

```text
Schema/Tool 校验
→ 规范化输入冻结
→ Operation Analyzer
→ 系统安全不变量
→ Grant / 权限模式 / 用户交互裁决
→ 获取执行并发槽
→ 路径、符号链接、环境和授权状态最终复检
→ Tool Gateway 执行
→ 结构化 Effect / Result / 审计事件
```

- 工具使用已冻结的规范输入执行，授权后修改原始参数不会改变实际执行内容。
- 高风险操作只能选择 ONCE，不生成可复用 Grant。
- 可证明安全的 Bash 命令只支持 RUN/SESSION 精确授权，不支持 WORKSPACE 宽授权。
- 受约束的文件读取和编辑可以选择 SESSION/WORKSPACE。
- 未知 MCP 和动态工具默认只能 ONCE；只有专用 Analyzer 才能产生可复用授权。
- `network-v1` 和 `mcp-v1` 的 SAFE/GUARDED 操作可选择 RUN/SESSION：保存的 Grant 仅匹配同一工具，输入值可变化；不支持 WORKSPACE，HIGH 风险仍只能 ONCE。
- Grant 不能覆盖保护路径、符号链接逃逸、敏感环境变量和执行前动态变化。
- 用户决策以 SQLite 中的 Interaction CAS 终态为唯一权威。

### 文件夹选择与持久授权

Web 新会话必须先选择一个已授权目录。远程和 Docker 部署的目录浏览只展示服务端配置允许的根目录及其子目录；启用本地 picker 的直连本机部署中，内置目录浏览器从默认 workspace 起始，可浏览本机服务进程可读的目录。macOS 和 Windows 还会在系统能力可用时显示原生文件夹选择按钮，系统对话框通常从桌面目录开始；Linux 继续使用内置目录浏览器。Docker 中宿主机的 `WORKSPACE_PATH` 对应容器内的 `/app/workspace`。浏览器不能把客户端本地路径直接当作远程服务端路径。

- Project 是一个全局、持久、可撤销的信任范围和默认相对路径根，并不是通用的操作系统文件沙箱；专用文件工具以 Session 的规范化工作目录解析相对路径，范围外路径另行授权并复检。
- DEFAULT 模式下，Project 内的普通文件操作免于重复确认；Project 外的普通请求进入常规授权流程，并可在策略允许时记住授权；敏感文件和高风险操作仍需逐次批准。
- 撤销 Project 会停止后续普通写入的持久自动授权。已有 Session 仍以原目录作为默认相对路径根；安全读取仍按 Session 策略执行，其他受控操作重新进入正常授权流程。
- Session、Query 和文件搜索使用 `projectId` 或 `sessionId`；客户端提交任意 `workingDirectory` 会被拒绝。
- 普通目录和 Git 子目录都可授权；只有所选目录本身就是 Git worktree 根目录时，才提供内置仓库上下文和 Git slash 命令。Bash 不是目录沙箱，但始终走独立的命令授权，不会因 Project 选择而自动获准。
- 后端的 `ZHIKUN_LOCAL_PICKER_ENABLED` 安全默认值为 `false`。使用 `./start.sh` 本地快速启动时，如果 `ZHIKUN_WORKSPACE_ALLOWED_ROOTS` 和该变量均无非空配置，脚本会为直连本机桌面场景启用 picker；显式设置 `false` 或配置 allowed roots 时不会被覆盖或隐式启用。远程、反向代理和生产部署应显式保持关闭并配置 allowed roots。
- Python 的 `WORKSPACE_ROOT` 是相对路径的默认锚点。配置 `ZHIKUN_WORKSPACE_ALLOWED_ROOTS` 后，Python 路由同样严格限制在这些根目录内；只有未配置 allowed roots 且显式启用本机 picker 的 loopback 开发模式，才允许分析用户选择的其他绝对路径。

### 授权范围与子 Agent 继承

| 范围 | 生命周期 | 子 Agent 行为 |
|------|----------|---------------|
| ONCE | 当前一次操作 | 不持久化 |
| RUN | 当前直接执行 Run | DIRECT_ONLY，不被兄弟或后代继承 |
| SESSION | 当前根会话 | 根 Agent 及其后代可在相同约束下复用 |
| WORKSPACE | 当前规范化工作区 | 根会话及后代可复用受约束的文件能力 |

`ONCE` 是不写入 Grant 仓库的一次性授权决策；`RUN`、`SESSION`、`WORKSPACE` 才是三种持久 Grant 范围。

子 Agent 使用 root session、root run 和 actor ancestry 构成的授权主体匹配父会话 Grant。继承只复用相同工具语义和约束，不能扩大路径、命令、风险等级或资源范围。

### 权限模式

| 模式 | 实际行为 |
|------|----------|
| DEFAULT | 已授权 Project 内的普通文件编辑自动允许；其他无可复用 Grant 的受控操作请求用户确认 |
| PLAN | 只允许安全工作区读取，其他 Effect 拒绝 |
| ACCEPT_EDITS | 自动允许工作区内非高风险文件编辑，其他受控操作仍需确认 |
| DONT_ASK | 不创建交互；安全读取、已有 Grant 和已授权 Project 内普通文件操作可执行，其他需要交互的操作直接拒绝 |
| AUTO_APPROVE | 自动批准到达人工授权阶段的工具操作，包括工作区外文件、公共互联网请求和秒悟发布；秒悟发布仍强制验证证据绑定、快照一致性与内容安全检查；硬拒绝、安全 Hook、SSRF 防护和部署沙箱仍然生效 |

新建 Web、REST 和合并会话默认使用完全访问（`AUTO_APPROVE`），创建接口显式传入其他合法权限模式时使用该模式。已有会话的 REST 查询沿用保存的权限；若显式传入的 `permissionMode` 与会话不同，三个查询接口（包括 SSE）在开始执行前返回 HTTP 409，错误码 `PERMISSION_MODE_MISMATCH`，请先在页面修改会话权限。页面收到保存确认后更新显示；修改影响后续工具授权，已经获准或执行中的操作不会被终止。

`AUTO_APPROVE` 会取消工具权限确认（包括秒悟发布）；远程部署使用时应确认运行账户、文件系统和网络边界符合预期。它不会赋予操作系统之外的新权限，也不会绕过系统安全与部署限制。

### 受保护路径

以下路径始终受系统安全不变量保护，权限模式和已保存 Grant 都不能绕过：

- `.git` — Git 仓库数据
- `.env` — 环境变量和密钥
- `.ssh` — SSH 密钥
- `.gnupg` — GPG 密钥
- `.aws` — AWS 凭证

### 安全测试

- 权限、Bash、路径、符号链接、WebSocket、并发和数据库 CAS 均有专项测试覆盖
- 包含命令注入、路径穿越、权限绕过等攻击场景
- **v9.3 深度防御新增**：
  - **CWE-22 路径穿越**：`CoordinatorService.getScratchpadDir` sessionId 白名单（11 单测），即使上游 URI 拦截被绕过，白名单仍为最终落盘防线
  - **跨用户访问隔离（P2-A）**：`BrowserReplayController` 双层闸门 —— sessionId 格式校验返回 400 + principal 归属校验返回 403，MVP 匿名会话兼容

  **v9.3 安全防御摘录：**

  | 防御层级 | 位置 | 防护机制 | 单测数 |
  |---------|------|---------|-------|
  | P1-2 | `CoordinatorService.getScratchpadDir` | sessionId 白名单 `^[A-Za-z0-9_-]{1,128}$` | 11 |
  | P2-A | `BrowserReplayController` | sessionId 格式校验 (400) + principal 归属校验 (403) | — |

- 上述场景均有专项测试覆盖；完整安全套件通过本地回归或专项工作流执行。

### 🧪 质量验证

完整功能测试报告见 [ZhikunCode v9.3 全链路测试报告](docs/test-results/v9.3/ZhikunCode全链路测试报告.md)（2026-05-16）

**持续集成：**
- **GitHub Actions 自动化流水线**：主 CI 执行后端与 Python 测试、前端检查和构建；Docker 镜像验证仅在 `main` push 时执行。

**前端专项验证快照（2026-10-04，历史记录）：**

- **Vitest 全量单元测试**：127 个测试文件通过，1220 PASS / 16 skipped（1236 total）；包含通知替换、旧计时回调竞态、卸载重挂和语法色板对比度回归。
- **主题浏览器回归**：1440px／390px 视口下共 16 个主题与浓度组合场景、8360 项颜色与隔离断言通过；覆盖正文、链接悬停、行内代码、表格、99／100 行代码与手动高亮、消息操作、Mermaid、图片和图文混合消息。
- **历史跳过项**：当时星舰主题在两个视口下的图片浮层交互因 `clip-path` 裁剪问题跳过；2026-10-06 已修复并恢复回归，当前不再跳过。
- **静态与构建验证**：TypeScript、改动源码 ESLint、Vite 生产构建和差异检查通过；构建仍提示部分分包超过 1000 kB。

此快照仅记录前端验证，不代表重新执行了后端、Python 或全栈会话链路测试。主题脚本使用真实消息组件和完整样式，在独立 Chromium 上下文中阻断网络请求；不启动业务服务、不读取现有会话，也不使用系统剪贴板。

**历史本地验证快照（2026-09-02）：**

- **后端单元/集成测试**：1258 tests / 0 failure / 0 error / 62 skipped
- **Python pytest**：107 PASS
- **前端 vitest**：207 PASS / 16 skipped（223 total）
- **简洁工作台 Playwright E2E**：7 / 7 PASS
- **静态与构建验证**：TypeScript 与 Vite 生产构建通过

**历史专项与 E2E 基线：**
- **36 模块 REST/WS/LLM/Session 冒烟**：45/45 PASS（42 REST + 1 WS STOMP + 1 LLM 真推理 + 1 Session 持久化）
- **E2E 差异化链路**：Task 7 可视化自动路由（`/visualize` mermaid/json/text）· Task 8 浏览器语义快照 MVP（`/snap`）全链路 PASS
- **APOS Phase 1 E2E**：62 用例（9 模块，含 28 原始功能 + 34 支撑链路）100% PASS，覆盖 Activity 基础 UI / 数据流转 / 三层展示 / Signal 标记 / Feature Flag / 后端 API / 响应式 / 持久化，含 4 Bug 修复回归
- **APOS Phase 2 E2E**：5 模块 50 用例（变更影响全景 / Pipeline 视图与 DAG / 异常检测与告警 / 移动端响应式 / Phase 2 集成功能）48 PASS / 2 SKIP，通过率 96%
- **APOS 风险修复专项**：11 用例 100% PASS（工具调用 / 批量操作 / 并发竞态 / API 降级）
- **AI Coding 功能增强专项**：6 大模块（SelfCorrectionLoop / 精确Tokenizer / Skill预算安全 / BashTool动态超时 / GitDiffTracker / SearchStrategyRouter）33 用例 + 238 单元测试 + 7 集成测试 + Feature Flag 双向验证，100% PASS
- **功能完整性验证**：100% 覆盖 v1.0 规划功能

**测试框架详情（2026-09-02 历史记录）：**

| 框架 | 层级 | 覆盖范围 | 数量 |
|------|------|---------|------|
| JUnit 5 + Mockito | 后端单元/集成测试 | 上下文/授权网关/技能/插件/LLM/MCP/记忆/并发/SSE/持久化/工具/工作台投影等（覆盖范围摘录） | 1258 tests / 0 failure / 0 error / 62 skipped |
| Vitest | 前端单元测试 | Store 生命周期/跨 Tab 同步/流式渲染/权限交互/重连恢复/工作台与路由边界 | 207 PASS / 16 skipped |
| Playwright + 节点脚本 | 端到端 E2E | 简洁工作台 / 可视化 3 种 viewType / 浏览器快照 MVP / APOS Phase 1 全栈 / APOS Phase 2 全栈 | 简洁工作台 7/7 PASS；Task 7/8/APOS 历史基线全绿 |
| Pytest | Python 服务测试 | Token 估算/文件处理/浏览器自动化/语义快照/代码分析器/CLI | 107 PASS |

**性能基线摘录（v9.3，原报告共 490 次真实请求采样）：**

| 指标 | p50 | p95 | p99 |
|-----|-----|-----|-----|
| REST API（14 端点混合） | 1.5ms | 2.3ms | 4.3ms |
| WS STOMP 握手 | 2.22ms | 4.58ms | 6.22ms |
| 浏览器语义快照（热路径） | 9.23ms | 12.20ms | 12.26ms |

**详细测试数据与证据：**
- v9.3 完整报告：[docs/test-results/v9.3/](docs/test-results/v9.3/)
- 分模块测试结果：[docs/test-results/](docs/test-results/)
- 前端 E2E 脚本：[frontend/e2e/](frontend/e2e/)
- 隔离主题回归脚本：[frontend/tests/browser/theme-regression.mjs](frontend/tests/browser/theme-regression.mjs)
- E2E 截图证据：[docs/test-results/screenshots/](docs/test-results/screenshots/)（42 项）

从仓库根目录运行主题回归（首次运行先安装前端依赖与 Playwright Chromium；已安装时可直接执行测试命令）：

```bash
cd frontend
npm ci
npx playwright install chromium
npm run test:theme-regression
```

该测试无需启动后端或前端开发服务器，失败截图写入系统临时目录。

<details>
<summary>📋 历史测试模块摘录（原报告共 36 个模块，保留原编号，点击展开）</summary>

| # | 模块 | 用例数 | 通过率 | 备注 |
|---|------|--------|--------|------|
| 1 | 环境准备与三端启动 | 7 | 100% | — |
| 2 | REST API 基础功能 | 33 | 100% | 逐端点验证 |
| 3 | WebSocket STOMP 通信 | 8 | 100% | — |
| 4 | Agent Loop 核心循环 | 9 | 100% | — |
| 5 | 工具系统与安全 | 10 | 100% | — |
| 6 | 权限治理与安全 | 6 | 100% | — |
| 7 | System Prompt 与 LLM | 7 | 100% | — |
| 8 | 记忆系统 | 7 | 86% | ★ 首次覆盖 |
| 9 | 技能系统 | 7 | 100% | ★ 首次覆盖 |
| 10 | 插件系统与 MCP | 11 | 100% | ★ 首次覆盖 |
| 12 | Python 服务 | 15 | 100% | 1 BUG 已修复 |
| 13 | 前端 E2E 与 UI | 7 | 86% | 1 PARTIAL |
| 14 | 文件历史与补充 API | 11 | 100% | ★ 首次覆盖 |
| 15 | CLI 命令行工具 aica | 11 | 91% | 2 BUG 已修复 |
| 16 | 可视化功能 E2E | 19 | 100% | ★ 首次覆盖 |
| 17 | F3 代码复杂度分析 | 6 | 100% | ★ v1.0 新增 |
| 18 | F33 变更影响链路分析 | 6 | 100% | ★ v1.0 新增 |
| 19 | F25 API 契约可视化 | 6 | 100% | ★ v1.0 新增 |
| 20 | F35 代码→图表自动生成 | 25 | 100% | ★ v1.0 新增 |
| 21 | F40 代码路径追踪可视化 | 25 | 100% | ★ v1.0 新增 |
| 22 | 单元测试体系（v9.3 扩展） | 84 | 100% | E2E 模块级测试用例数（后端 JUnit 1500+ 已在别处统计） |
| 23 | APOS 基础 UI | 4 | 100% | ★ 首次覆盖 |
| 24 | APOS 数据流转 | 4 | 100% | ★ 首次覆盖 |
| 25 | APOS 三层展示 | 4 | 100% | ★ 首次覆盖 |
| 26 | APOS Signal与筛选 | 2 | 100% | ★ 首次覆盖 |
| 27 | APOS Feature Flag | 2 | 100% | ★ 首次覆盖 |
| 28 | APOS 后端API验证 | 1 | 100% | ★ 首次覆盖 |
| 29 | APOS 响应式+健康 | 3 | 100% | ★ 首次覆盖 |
| 30 | APOS Activity持久化 | 8 | 100% | ★ 首次覆盖 + 4 Bug 修复 |
| 31 | APOS 变更影响全景 | 6 | 100% | ★ Phase 2 新增 |
| 32 | APOS Pipeline视图与DAG | 12 | 92% | ★ Phase 2 新增 |
| 33 | APOS 异常检测与告警 | 10 | 100% | ★ Phase 2 新增，2 SKIP |
| 34 | APOS 移动端响应式 | 9 | 89% | ★ Phase 2 新增 |
| 35 | APOS Phase 2集成功能 | 13 | 100% | ★ Phase 2 新增 |
| 36 | AI Coding 功能增强 | 33 | 100% | ★ v9.4 新增（6子模块 + 238单元 + Feature Flag验证） |

</details>

---

## 🎯 skill技能系统

ZhikunCode 的skill技能系统（Skill System）是一个 **Markdown 驱动的可扩展工作流引擎**。每个技能就是一个 `.md` 文件，用 YAML frontmatter 定义元数据，用 Markdown 正文定义执行指令。

### 管理与启停

PC 和平板通过顶部 **Skill** 入口、手机通过 **更多 → Skill 管理** 打开管理页，可搜索技能、查看来源与正文，并分别开启或关闭。现有与新增技能默认开启。设置由同一后端的所有设备和会话共享，默认保存到 `~/.zhikun/skill-states.json`；可通过 `SKILL_STATE_PATH` 指定位置，Docker 使用持久化目录中的 `/app/data/skill-states.json`。

开关按技能内部名称保存，同名覆盖、文件热加载或删除后重建同名技能都会保留原有选择。

保存后立即拦截新的技能调用，下一条用户消息使用更新后的配置，无需重启。关闭的技能不出现在可用列表或技能建议中，不再自动加入其描述、正文和对应 token 开销；全部关闭时移除 `Skill` 工具。页面可见时每 5 秒同步一次其他设备的设置，也可手动刷新。

如果技能设置文件损坏或无法读取，后端仍会启动，但所有 Skill 暂时关闭。管理页会显示错误并禁止保存，原文件不会被覆盖；修复提示中的配置文件后，重启后端恢复正常管理。

当前回答与已经开始的技能执行继续运行；旧聊天历史中的技能内容仍可能影响模型，新聊天可获得干净上下文。开关管理的是技能加载与调用，不会隔离磁盘文件。技能对应的独立命令、底层工具及部署配置仍有各自的启用规则，例如关闭 `review` Skill 不会关闭独立的 `/review` 命令。

### 13 个内置技能

在 Web 输入框输入 `/skill <技能名>` 打开技能弹窗，再填写参数并执行；发布使用表中的专用命令。技能提供工作流指引，同名直接命令（如 `/review`）有独立实现。

| 技能 | 命令 | 功能 |
|------|------|------|
| **智能提交** | `/skill commit` | 分析暂存区变更，按 Conventional Commits 格式生成 commit message |
| **代码审查** | `/skill review` | 审查未提交变更，按 P0/P1/P2/P3 严重程度分类问题 |
| **智能测试** | `/skill test` | 为指定代码或近期变更生成/运行测试，覆盖边界情况 |
| **PR 助手** | `/skill pr` | 分析分支差异，生成结构化 PR 描述和审查说明 |
| **调试诊断** | `/skill debug` | 按需求进行根因诊断、最小修复或脱困分析 |
| **代码验证** | `/skill verify` | 按项目技术栈和改动风险选择构建、测试及静态检查 |
| **项目笔记** | `/skill remember` | 显式保存、检索和更新项目共享笔记；不保证新会话自动读取 |
| **架构分析** | `/skill software-architecture` | Clean Architecture + SOLID + 设计模式评估 |
| **数据摘要** | `/skill csv-data-summarizer` | CSV统计分析+可视化图表+Markdown报告 |
| **Prompt工程** | `/skill prompt-engineering` | 优化prompt结构、清晰度和有效性 |
| **测试驱动开发** | `/skill test-driven-development` | TDD红→绿→重构循环方法论指导 |
| **OSS 产物发布** | `/publish-oss` | 经单次高风险授权，从同一持久化根 Session 的根 Run 或授权后代 Run 中发布目标条目已验证且哈希仍匹配的产物；底层发布能力默认关闭且不会自动上传 |
| **秒悟应用发布** | `/publish-meoo` | 每次创建新站点、保留旧站点并占用平台额度；结果卡显示匿名访问验证状态。[配置与使用说明](docs/deployment/meoo.md) |

### 技能加载来源

当前启动时依次加载内置、项目和用户技能，同名定义由后加载者覆盖；这不是支持删除后自动回退的分层注册表：

```
bundled → project → user
```

| 来源 | 目录 | 说明 | 状态 |
|------|------|------|------|
| **managed** | 策略管理目录 | 企业统一下发的技能 | 预留 |
| **user** | `~/.zhikun/skills/` | 用户全局自定义技能 | ✅ 已实现 |
| **project** | `.zhikun/skills/` | 项目级技能；是否纳入版本控制取决于 Git 忽略规则 | ✅ 已实现 |
| **plugin** | 插件提供 | JAR 插件内嵌的技能 | 预留 |
| **bundled** | 内置 | 13 个开箱即用技能 | ✅ 已实现 |
| **mcp** | MCP 构建 | 通过 MCP 协议注册的技能 | 预留 |

### 自定义技能

在 `~/.zhikun/skills/` 或项目根目录 `.zhikun/skills/` 下创建 `.md` 文件：

```markdown
---
description: "将代码翻译为指定语言"
arguments:
  - language
---

# 翻译任务

将用户选中的代码翻译为 {{language}}，保持原有逻辑和注释风格。
```

Web 调用方式：输入 `/skill translate`，在弹窗参数栏填写 `language=python` 或 `python`，再执行。

**可解析的 frontmatter 字段：**

模型调用 `Skill` 工具时，渲染正文通过工具结果返回；Web `/skill` 通过命令路径将渲染提示送入当前对话。

| 字段 | 类型 | 说明 |
|------|------|------|
| `description` | string | 技能描述 |
| `name` | string | 显示名称（覆盖文件名） |
| `arguments` | list | 参数定义列表 |
| `argument_hint` | string | 参数提示文本 |
| `when_to_use` | string | 使用条件描述元数据 |
| `allowed_tools` | list | 技能声明的工具列表；不能替代实际工具权限控制 |
| `context` | string | `inline`（默认）将渲染正文作为工具结果返回；`fork` 返回正文和执行元数据，当前入口不自动创建子代理 |
| `model` | string | 模型声明（`inherit` 表示不指定覆盖）；当前执行器返回此元数据，不自动切换模型 |
| `version` | string | 技能版本号 |
| `disable_model_invocation` | boolean | 模型调用偏好声明（默认 false）；当前工具入口未据此禁止模型调用 |
| `user_invocable` | boolean | 手动调用偏好声明（默认 true）；当前入口未据此限制调用 |
| `hooks` | object | 钩子配置（预留） |
| `effort` | string | 推理强度声明；fork 结果携带此元数据，当前不自动调整模型请求 |
| `agent` | string | 关联代理名称声明；fork 结果携带此元数据，当前不自动创建对应代理 |
| `paths` | list | 文件路径 glob 模式声明（元数据） |
| `shell` | string | Shell 类型声明（默认 bash）；当前不据此启动或切换 Shell |

> 已监听目录中的技能文件支持热更新（500ms 防抖）。删除同名覆盖文件不会自动恢复内置定义；修改内置资源或清理覆盖文件后，应重新构建并重启后端，再刷新前端菜单。

**安全与运行控制：**
- **技能加载与上下文**：不设置单技能或会话累计的 token 加载额度；模型上下文容量、运行轮次和输出限制仍然适用，重复加载仍会增加实际输入 token 消耗。
- **工具声明**：`allowed_tools` 描述预期工具；当前不保证运行时强制执行这份列表，实际工具权限仍然适用
- **参数检查**：`Skill` 工具入口对每个已解析参数检查 2000 字符上限，并匹配六类危险正则模式：`$(...)`、反引号、`; command`、管道命令、`&& rm`、`${...}`；后续工具调用仍经过实际授权与执行检查。
- **Fork 深度检查**：fork 模式检查调用时的当前上下文深度，深度 ≥3 时拒绝；该入口仍只返回渲染正文与元数据。

---

## 🧩 插件系统

ZhikunCode 的插件系统通过标准 **Java SPI（ServiceLoader）** 机制发现和加载第三方 JAR 插件，提供四大桥接能力：命令注册、工具注册、钩子拦截、MCP 服务器集成。通过 `plugin.enabled` Feature Flag 控制启停。

### 四大桥接能力

| 桥接类型 | 说明 | 示例 |
|---------|------|------|
| **命令注册** | 插件可注册自定义斜杠命令，自动添加插件前缀 | `/myplugin:hello` |
| **工具注册** | 插件可提供自定义工具供 AI Agent 调用 | 自定义代码分析工具 |
| **钩子拦截** | 插件可在关键事件前后执行自定义逻辑 | 工具执行前安全审计 |
| **MCP 服务器** | 插件可注册 MCP 服务器扩展 AI 能力 | 连接外部数据源 |

### 安全特性

- **PluginClassLoader 沙箱隔离** — 插件通过包白名单访问宿主 API：核心 API 包（`com.aicodeassistant.plugin.*`、`tool.*`、`command.*`、`mcp.*`）、标准库（`java.*`、`javax.*`、`jdk.*`、`sun.*`、`org.slf4j.*`）、基础框架（`org.springframework.*`、`com.fasterxml.jackson.*`、`jakarta.*`）。未在白名单中的宿主类访问会抛出 `ClassNotFoundException`
- **钩子执行超时保护** — Virtual Thread + `CompletableFuture.orTimeout(5s)`，超时自动放行，防止插件阻塞主流程
- **JAR 文件验证** — 加载前校验文件存在性、JAR 格式合法性、大小限制（默认 50MB）、SPI 配置文件（`META-INF/services/`）完整性
- **API 版本兼容检查** — 插件声明 `minApiVersion` / `maxApiVersion`，宿主自动校验兼容性

### 热重载机制

支持运行时重新加载所有插件，无需重启服务：

- 使用 `ReentrantReadWriteLock` 保证热重载期间的并发安全
- 重载流程：卸载所有插件（注销命令/工具/钩子/MCP + 关闭 ClassLoader）→ 重新扫描加载
- 触发方式：`/reload-plugins` 斜杠命令 或 REST API

### 8 种钩子事件类型

插件可注册以下事件钩子，在关键节点执行自定义逻辑：

| 事件类型 | 触发时机 |
|---------|----------|
| `PreToolExecution` | 工具执行前 |
| `PostToolExecution` | 工具执行后 |
| `UserPromptSubmit` | 提示词提交时 |
| `SessionStart` | 会话开始 |
| `SessionEnd` | 会话结束 |
| `TaskCompleted` | 任务完成 |
| `Notification` | 通知事件 |
| `Stop` | 停止事件 |

### 插件开发指南

开发一个 ZhikunCode 插件只需四步：

**1. 实现 `PluginExtension` SPI 接口**

```java
public class MyPlugin implements PluginExtension {
    @Override public String name() { return "my-plugin"; }
    @Override public String version() { return "1.0.0"; }

    @Override
    public List<Command> getCommands() {
        return List.of(/* 自定义命令 */);
    }

    @Override
    public void onLoad(PluginContext ctx) {
        ctx.getLogger().info("Plugin loaded!");
    }
}
```

**2. 在 `META-INF/services/` 中注册 SPI**

```
# META-INF/services/com.aicodeassistant.plugin.PluginExtension
com.example.MyPlugin
```

**3. 将 JAR 放入 `~/.zhikun/plugins/` 目录**

**4. 重启服务或执行 `/reload-plugins` 热重载**

> `PluginExtension` 接口采用默认方法设计 — 最小实现仅需 `name()` 和 `version()`，其余能力（命令/工具/钩子/MCP）按需覆写。

---

## 🧠 记忆系统

ZhikunCode 内置三层记忆架构，让 AI 助手能够 **跨会话记住你的偏好、项目约定和工作流程**。

### 三层记忆架构

| 层级 | 文件 | 作用域 | 说明 |
|------|------|--------|------|
| **个人记忆** | `~/.ai-code-assistant/MEMORY.md` | 全局跨项目 | AI 自动记录用户偏好、常用模式、错误解决方案 |
| **项目记忆** | `zhikun.md` / `zhikun.local.md` | 当前项目 | 项目级编码约定、架构决策、构建流程 |
| **团队记忆** | `.zhikun/team-memories/*.md` | 团队共享 | 随代码库分发的团队规范和共享知识 |

### 记忆分类

基于认知心理学模型的设计分类（实现层面通过文件路径和元数据标签区分），记忆自动归类为四种类型：

| 分类 | 说明 | 示例 |
|------|------|------|
| **语义记忆**（semantic） | 项目知识、用户偏好、技术约定 | 「这个项目使用 JUnit 5 + AssertJ」 |
| **事件记忆**（episodic） | 具体操作历史、调试经过 | 「上次部署时端口冲突的解决方法」 |
| **程序记忆**（procedural） | 常用工作流、部署流程 | 「每次提交前先跑 `mvn test`」 |
| **团队记忆**（team） | 团队级共享知识和规范 | 「API 返回统一使用 Result 包装」 |

### 自动记忆与搜索

AI 在交互过程中通过内置的 MemoryTool 自动记录和检索记忆：

- **自动写入** — AI 发现重要信息时主动记录（用户偏好、项目规范等）
- **自动加载** — 每次会话启动时自动注入系统提示，无需手动操作
- **BM25 搜索** — 纯 Java 实现的 BM25 搜索引擎，支持中英文混合检索（Unigram + Bigram 中文分词）
- **来源追踪** — 支持记忆来源追踪（source 字段），区分 REST API 创建与 LLM 工具创建的记忆
- **LLM 重排** — 可选的 LLM 精排服务，BM25 粗筛后由大模型进行相关性精排

### 页面管理记忆

点击页面顶部的 **记忆** 徽章，即可在页面中查看和编辑个人记忆（`MEMORY.md`）：

- **卡片模式** — 逐条查看、编辑、删除记忆条目，支持手动新增
- **整篇模式** — 以 Markdown 编辑器整体修改，支持实时预览
- **安全保护** — 保存时自动规范化条目格式、生成 `.bak` 备份，并在内容被并发修改时进行冲突检测；PC / 平板 / 手机响应式布局

### 项目记忆文件

在项目根目录创建记忆文件，AI 会自动读取并遵循：

```markdown
# zhikun.md — 项目约定（随代码库提交）

## 编码规范
- Java 方法命名使用 camelCase
- 测试类以 Test 结尾

## 构建流程
- 提交前必须跑 `./mvnw test`
- Commit 采用 Conventional Commits 格式
```

```markdown
# zhikun.local.md — 本地配置（不提交，加入 .gitignore）

## 本地环境
- 我的 API Key 在 .env 文件中
- 本地数据库端口: 5432
```

> 项目记忆仅从所选 Project 根目录加载 `zhikun.md` 和 `zhikun.local.md`，不向父目录搜索；单文件上限 100KB。`zhikun.md` 随代码库提交用于团队共享，`zhikun.local.md` 用于个人本地配置。

### 安全保护

- 截断保护：个人记忆最多 200 行 / 25KB，防止系统提示 Token 爆炸
- 自动压缩：超出 50,000 字符时自动压缩，保留最新 70%
- 自动过期：90 天未访问的记忆自动清理
- 路径穿越防护：项目记忆写入时校验绝对路径和符号链接

---

## 💻 CLI 工具

除了 Web UI，ZhikunCode 还提供完整的命令行能力，覆盖三种场景：

### Python CLI（aica）— 终端 AI 编程

`aica` 是 ZhikunCode 的命令行客户端，设计为 UNIX 管道一等公民：

```bash
# 安装
cd python-service
pip install -e ".[cli]"

# 基础使用
aica "帮我重构这个函数"

# 显式授权当前目录（仅 localhost 后端）
aica --working-dir "$PWD" "帮我重构这个函数"

# 远程后端使用已有 Project
aica --server https://example.com --project-id PROJECT_ID "检查项目"

# 管道输入 — 像 grep/sed 一样组合
cat src/main.py | aica "review this code"

# 结构化输出 + jq 处理
aica -f json "list all API endpoints" | jq '.result'

# 流式输出
aica -f stream-json "refactor this module"

# 继续上次对话
aica --continue "fix the bug we just discussed"
```

未提供 `--working-dir`、`--project-id`，且没有通过 `--session-id`、`--continue` 或 `--resume` 选择 Session 时，CLI 使用后端默认 workspace。`--working-dir` 只适用于 localhost，远程后端应使用 `--project-id`；两者不能同时使用。

**核心特性：**

| 特性 | 说明 |
|------|------|
| 三种输出格式 | `text`（终端 Markdown 渲染）/ `json`（结构化）/ `stream-json`（SSE 流式） |
| 管道支持 | 自动读取 stdin，与 shell 管道无缝组合 |
| 权限模式 | `--permission-mode default/plan/accept_edits/dont_ask/auto_approve` 控制授权策略（CLI 未指定时新建默认完全访问、续接沿用会话权限；`auto_approve` 取消人工确认，含秒悟发布；不能绕过硬拒绝、安全 Hook、SSRF 或部署沙箱） |
| 会话管理 | `--continue` 继续上次会话，`--resume <id>` 恢复指定会话 |
| 模型选择 | `--model` 指定模型，`--effort` 控制推理深度 |
| 工具控制 | `--allowed-tools` / `--disallowed-tools` 白名单/黑名单 |
| 退出码 | 0=成功，1=通用错误，2=参数错误，3=连接错误，4=认证错误，130=Ctrl+C 中断 |

> `aica` 通过 HTTP/SSE 连接 ZhikunCode 后端，共享同一套 Agent 引擎、工具集和安全架构。适合 CI/CD 集成和脚本自动化场景。

### 35+ 斜杠命令 — Web UI 快捷操作

> 以下斜杠命令在 Web UI 中使用，`aica` CLI 通过自然语言 prompt 访问后端 Agent 引擎实现相同能力。

在 Web UI 中输入 `/` 或按 `Ctrl+K` 打开命令面板，支持模糊搜索和键盘导航：

| 类别 | 命令 | 说明 |
|------|------|------|
| **核心** | `/help` `/clear` `/exit` | 帮助、清除对话、退出 |
| **模型** | `/model` | 查看可用模型；切换请使用输入栏的模型选择器 |
| **诊断** | `/doctor` | 9 项系统诊断（Java/LLM/Git/JVM/Python/磁盘） |
| **压缩** | `/compact` | 手动触发上下文压缩，可附带指令（如 `/compact focus on API`） |
| **Git** | `/diff` `/commit` `/review` | 代码差异（`/diff [unstaged\|staged\|--staged]`；`--cached` 不再被接受，请用 `staged`）、暂存预览/直接提交、代码审查 |
| **配置** | `/config` `/permissions` | 查看配置、权限模式管理 |
| **会话** | `/session` `/resume` | 会话信息、恢复历史会话 |
| **成本** | `/cost` `/usage` | Token 用量、费用统计 |
| **MCP** | `/mcp-servers` `/mcp-tools` | MCP 服务管理 |
| **深度分析** | `/ultrareview` | AI 深度审查（架构+安全+性能+并发） |
| **浏览器** | `/snap` | 语义快照 —— 捕获当前页面 DOM 结构与交互元素，生成 JSON 格式快照 |
| **可视化** | `/visualize mermaid\|json\|text` | 自动路由推送 —— 流式渲染 Mermaid 图表、JSON 数据或纯文本可视化结果 |

> 命令输入错误时，系统会基于 Levenshtein 距离自动建议相似命令。

---

## 📱 浏览器全流程操控

这是 ZhikunCode 的核心差异化特性。与 Cursor、Cline 等需要安装桌面客户端或 IDE 插件的工具不同，ZhikunCode 是一个独立的 Web 应用 —— 部署一次，任何设备的浏览器都能用。

### 为什么这很重要？

| 场景 | 传统 AI 编程工具 | ZhikunCode |
|------|-----------------|------------|
| 通勤路上想审批一个权限请求 | ❌ 必须打开电脑 | ✅ 手机浏览器直接操作 |
| 同事想试用你的 AI 编程助手 | ❌ 需要安装 VS Code + 插件 | ✅ 发一个链接就行 |
| 部署到团队服务器多人共用 | ❌ 每人都要装客户端 | ✅ 浏览器打开就用 |
| iPad 上改代码 | ❌ 没有原生客户端 | ✅ Safari/Chrome 直接用 |

### 完整的浏览器操控能力

通过浏览器，你可以完成 AI 编程的全部流程：

- **对话式编程** — 输入自然语言需求，Agent 自动生成代码，实时流式输出
- **权限审批** — 每个敏感操作都会弹出审批请求，你可以 允许/拒绝/修改
- **方案协商** — Agent 提出方案后可以在浏览器中讨论、修改、确认
- **任务管控** — 查看任务状态与结果，按任务 ID 请求取消并查询停止确认
- **文件浏览** — 在浏览器中直接查看和导航项目文件树
- **委派结果查看** — 通过对话中的工具结果查看子任务结果

### 实时通信

前后端通过 **STOMP over SockJS** 保持实时连接（自动协商 WebSocket → xhr-streaming → xhr-polling 降级）：

- **流式输出** — LLM 响应逐字输出，无需等待完成
- **持久权限交互** — 权限请求先写入 SQLite，再投递到浏览器；刷新或断线重连后可恢复未完成请求
- **服务端终态裁决** — 浏览器只提交服务端下发的选项，允许、拒绝、过期和取消通过数据库 CAS 互斥裁决
- **服务端倒计时** — 权限决策窗口为 300 秒，前端只展示服务端 deadline，不在本地自动伪造拒绝
- **子 Agent 授权复用** — 后代 Agent 在严格约束下复用根会话 SESSION/WORKSPACE Grant，避免重复弹窗
- **状态同步** — Agent 工作状态变化即时反映在 UI 上
- **心跳保活** — 双向 10s 心跳检测，断线自动重连（指数退避 1s→10s）
- **消息保障** — 128KB 消息大小限制，1MB 发送缓冲，30s 发送超时

### 🌉 Bridge 跨端桥接

ZhikunCode 通过 Bridge 模块提供跨端桥接（Cross-Platform Bridge）能力：

| 组件 | 职责 |
|------|------|
| **BridgeServer** | 桥接服务端，管理设备连接和消息路由 |
| **BridgeApiClient** | 客户端 API 封装，支持远程调用 |
| **TrustedDeviceManager** | 可信设备管理，设备注册与认证 |

---

## 🤖 Agent 委派与后台任务

把独立调查、实现或验证交给子 Agent，让主 Agent 保持对整体目标的掌握；把需要持续查询的执行交给后台 Task，用任务 ID 跟踪状态与结果。两者都能让耗时工作与主对话配合推进，各自承担明确的职责。

### 五种内置 Agent 角色

`Agent` 工具通过 `subagent_type` 选择角色，`SubAgentExecutor` 为每次调用创建独立子会话与上下文，由角色提示和当前可用工具共同约束执行：

| 角色 | 适合的任务 | 工具范围 |
|------|-----------|---------|
| **探索（explore）** | 搜索代码、梳理调用链、定位实现与风险 | 当前启用工具中排除直接编辑工具与角色禁用项 |
| **验证（verification）** | 复现问题、执行测试、寻找反例并给出证据 | 当前启用工具中排除直接编辑工具与角色禁用项；遵守验证角色的文件保护约束 |
| **规划（plan）** | 分析需求、比较方案、拆解实施步骤 | 当前启用工具中排除直接编辑工具与角色禁用项 |
| **通用（general-purpose）** | 实现功能、修复问题、完成完整子任务 | 当前启用工具，受公共禁用项与授权约束 |
| **引导（guide）** | 查阅文档、解释配置与用法 | 仅 Glob、Grep、Read、WebFetch、WebSearch |

工具池从当前启用的内置工具、插件和 MCP 工具组装，再应用公共禁用项及角色 allow/deny 规则。子 Agent 不提供 `Agent`、`TaskCreate`、`VerifyPlanExecution` 等嵌套委派或验证编排入口。探索、验证和规划角色排除 `Edit`、`Write`、`NotebookEdit` 等直接编辑工具；仍可用的 Shell、浏览器或 MCP 操作继续受授权约束，工具过滤本身不是完整只读沙箱。

**验证以证据为准。** `verification` 的角色提示要求保护源码、现有测试、配置、依赖与锁文件，在授权范围内执行测试并允许生成可复现的验证产物、缓存和临时脚本；不得为验证而安装依赖或进行 Git 写入。动态验证结论须引用实际命令和工具输出，静态分析须明确标注。报告需针对主要风险进行反例检查，并区分 **PASS**（验收范围已验证且无重大缺口）、**FAIL**（已确认失败）与 **PARTIAL**（尚未确认失败，但关键验证未完成）。这些是角色执行与报告规范，最终应结合实际证据审阅结论。

### 独立上下文、并行执行与结果回收

每次委派都需要在 `prompt` 中交代目标、已知结论、文件路径、授权边界与预期交付；子 Agent 从独立上下文开始。多个相互独立的 `Agent` 调用可在同一轮通过 Virtual Thread 并行执行，适合分别调查不同模块，或并行完成互不冲突的子任务。共享目录中的文件修改仍需避免重叠；上下文独立不等于文件隔离。

| 入口 | 调用与结果链路 | 适合场景 |
|---------|---------------|---------|
| **Agent（同步）** | 子会话执行 → 返回状态与结果 → 主 Agent 继续 | 下一步依赖该子任务结论 |
| **Agent（后台）** | `run_in_background=true` → 返回代理 ID 与输出文件路径 → 后台执行 → 当前 Run 收集结果 → 主 Agent 汇总 | 主 Agent 还有其他独立工作可推进 |
| **TaskCreate** | 提交后台执行 → 返回任务 ID → TaskList／TaskGet 查询状态与输出 | 需要单独查询、更新输出或请求取消的执行 |
| **TodoWrite** | 更新计划与进度清单 | 记录步骤与完成情况，不启动执行 |

后台 Agent 由 `BackgroundAgentTracker` 按父会话和父 Run 登记，WebSocket 推送启动、完成和失败事件。默认启用 `BACKGROUND_AGENT_WAIT`：主 Run 准备结束时，`QueryEngine` 等待**当前 Run** 尚未交付的后台 Agent 结果，将其作为任务数据回填上下文，再由主 Agent 生成汇总。结果不会成为新的授权或执行指令。

常规执行会对超过 **100,000 字符**的答案正文截断并附标记；Worktree 路径对包含交付、恢复信息的合成内容作同样处理。异常恢复及附加信息另有处理，因此这不是所有最终响应的统一硬上限。后台输出文件保存处理后的结果，父 Run 自动回填每个文件的前 **4,000 字符**，超长时附截断标记，并保留文件路径；可按路径读取更多已保存内容，文件本身也可能已被截断。

子 Agent 执行等待的基础预算默认 **30 分钟**，默认配置上限也为 **30 分钟**；执行等待超时后默认再等待 **30 秒**供退出。子会话初始化与 Worktree 准备、交付不计入这段执行等待计时，因此它不是调用总耗时上限。

父 Run 每批后台结果等待另设默认 **31 分钟**预算，与子执行等待分别计时；新一批等待独立获得预算，同一批唤醒不会刷新截止时间。可通过 `FEATURE_BACKGROUND_AGENT_WAIT=false` 关闭等待，或用 `AGENT_TIMEOUT_MAX_WAIT_MINUTES` 调整预算；提高子代理超时上限时应同步调整。等待超时会明确报告 `BACKGROUND_AGENT_WAIT_TIMEOUT`；取消、等待中断或主 Run 轮次耗尽也可能使结果收集未完成。此结果回收链路属于后台 `Agent`；`TaskCreate` 的执行结果通过任务工具查询。

### 模型选择、授权与真实执行状态

子 Agent 的模型解析顺序为 **显式 `model` 参数 → 父查询模型 → `premium` 别名**，五种角色遵循同一规则。`model` 可选择可用的实际模型名或 `light`、`standard`、`premium` 别名；别名在 `application.yml` 的 `agent.model-aliases` 中配置，当前三者默认均为 `qwen3.8-max-0902`。

子 Agent 使用关联的根会话、根 Run 与代理祖先链进行权限裁决。符合工具语义和约束的 SESSION／WORKSPACE Grant 可按规则复用；继承不会扩大路径、命令、风险或资源范围。需要人工授权的操作通过根会话的持久交互流程处理。

执行结果区分 `completed`、`failed`、`timeout`、`interrupted` 和 `max_turns`，后台结果保留实际结束原因。执行等待超时会发出中止信号并等待退出窗口，能够恢复时附带部分进展；执行等待超时或取消请求本身不等于所有受管执行已经停止，应结合停止确认与恢复信息判断后续处理。

`AgentConcurrencyController` 提供全局 **30** 个、每会话 **10** 个并发准入名额，并设 **3 层**执行深度上限。超限请求会被拒绝；名额按执行路径释放，名额释放不构成底层执行已停止的确认。

### 工作目录与安全交付

`Agent` 的 `isolation` 提供两种选择：

| 隔离方式 | 行为 | 适合场景 |
|---------|------|---------|
| **none**（默认） | 使用父工作目录，子会话上下文独立 | 代码调查、验证、文件范围清晰的子任务 |
| **worktree** | 从项目已提交 HEAD 创建独立 Git Worktree，通过安全检查后自动合回 | 需要隔离文件修改的实现或实验 |

WORKTREE 不包含父工作区未提交的修改，也不会自动 stash 或提交父目录；实际执行目录与提示一致，原 Project 授权边界不扩大。授权根必须是有效仓库根；其内部子目录可映射到新树执行，无初始提交或 detached HEAD 不支持自动交付。

只有执行正常完成、受管工作已停止且目标分支、历史与工作区状态通过核验时才自动合回。已交付但清理失败仍为完成并附警告；未交付、冲突、超时或停止未确认会保留工作区与分支，并返回实际恢复位置。Git 自然退出后不会为清理终止 hook 后台进程。Linux 和 macOS 对仍在受管进程组内的普通后台后代保留目录；主动脱离该组的守护进程不在此保证内。其他平台沿用原有尽力跟踪能力，不承诺同等级的后代停止证明。停止服务也不删除 worktree 或代理分支。 自动交付遵守 Git 忽略规则：ignored 文件不会强制加入提交，正常清理时可能随目录删除；需要保留的交付文件应放在非忽略路径。子模