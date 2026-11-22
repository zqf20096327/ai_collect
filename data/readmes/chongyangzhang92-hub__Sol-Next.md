<div align="center">

<img src="docs/media/hero-banner.png" alt="Sol Next v6.3 Public Edition — 致敬并深度重构自 Mika 的新一代极速安卓 AI 助理" width="100%" />

# Sol Next — Android AI Phone Agent（开源极速安卓 AI 手机助理 · 致敬并重构自 Mika）

**简体中文** · [English](README.en.md) · [🌐 产品发布官网（含高清演示视频）](https://chongyangzhang92-hub.github.io/Sol-Next/) · [🤖 Agent 索引 (`llms.txt`)](llms.txt) · [🛠 `AGENTS.md`](AGENTS.md) · [📊 与 Mika 对比](docs/guides/COMPARISON_WITH_MIKA.md) · [🔑 BYOK 配置](docs/guides/BYOK_SETUP.md)

<br/>

> **English Summary (for Global Developers & AI Search)**: **Sol Next (`ai.sol.next`)** is an open-source, **zero-built-in-key (BYOK)** Android 10–16 AI phone agent built upon and paying tribute to [`wangzan101/Mika`](https://github.com/wangzan101/Mika) (Apache-2.0). Designed as a high-speed, anti-pause mobile GUI agent and Mika evolution/alternative, Sol Next combines a **Rust v3.10 native JNI kernel** (`17–45 µs` UI tree pruning, `-74% to -97%` tokens), **1:1 physical Display 0 background VirtualDisplay cloning** (`0.0px` drift), **Android 14–16 HTTP/3 QUIC 0-RTT with smart circuit breaker**, **64-round Xiaomi HyperOS anti-pause recovery**, **carrier-grade AI phone calls** (Volcengine Seeduplex 3.0 / OpenAI Realtime BYOK + 3×4 DTMF), and **zero-dependency CLI (`--json`) + MCP Server** integration.

<br/>

<a href="https://github.com/chongyangzhang92-hub/Sol-Next/releases/latest"><img src="https://img.shields.io/badge/下载公开版%20APK-v6.3.0%20(零内置%20Key)-10b981?style=for-the-badge&logo=android&logoColor=white" alt="下载公开版 APK" /></a>
<a href="https://chongyangzhang92-hub.github.io/Sol-Next/"><img src="https://img.shields.io/badge/在线产品官网-高清视频演示-0284c7?style=for-the-badge&logo=googlechrome&logoColor=white" alt="在线产品官网" /></a>
<a href="https://github.com/wangzan101/Mika"><img src="https://img.shields.io/badge/致敬原作者-wangzan101%2FMika-6366f1?style=for-the-badge&logo=github&logoColor=white" alt="致敬 Mika" /></a>

<br/>

![Android 10-16](https://img.shields.io/badge/Android-10%20~%2016%20(API%2029--36)-3DDC84?logo=android&logoColor=white)
![Rust Kernel](https://img.shields.io/badge/Rust%20Native%20Kernel-v3.10%20JNI-DEA584?logo=rust&logoColor=white)
![Zero API Keys](https://img.shields.io/badge/Public%20BYOK-0%20内置%20API%20Key-f59e0b)
![License](https://img.shields.io/badge/License-Apache--2.0-blue)

<br/>

### 🎬 实机效果抢先看（Android 16 · 1:1 原生后台虚拟屏 + 全脑中枢 + AI 电话）

<img src="docs/media/sol-next-hero-demo.gif" alt="Sol Next Android 16 实机演示：1:1 后台虚拟屏、全脑中枢与 AI 接打电话" width="840" />

<sub>▲ Android 16 实机录屏：后台 1:1 原生虚拟屏（1080×2400 @ 420dpi）自主执行多步任务、展开浮窗零漂移触控、全脑中枢遥测与 AI 电话驾驶舱</sub>

> 🎥 **观看完整 1080p 高清演示视频**：直接访问 [**Sol Next 交互式产品发布官网**](https://chongyangzhang92-hub.github.io/Sol-Next/#demo-video)，或下载仓库内的 [`docs/media/sol-next-demo.mp4`](docs/media/sol-next-demo.mp4)（1.4 MB，H.264 通用编码）。

</div>

---

## 🙏 致敬 Mika 原作者（`@wangzan101`）

> **饮水思源，坦诚开源。**
>
> **Sol Next** 是在杰出的开源项目 [**Mika (`github.com/wangzan101/Mika`)**](https://github.com/wangzan101/Mika)（Apache-2.0 协议，Trendshift GitHub Kotlin 日榜 & 周榜 #1）的设计理念与架构基础上改造、重构和演进而来的公开产品。
>
> `@wangzan101` 开创性地将 **Android 独立后台虚拟屏（VirtualDisplay）**、**无线调试免电脑开启** 以及 **保留原生拨号器的 Telecom Companion 伴侣通话思路** 带到了手机端 AI 助理领域，为整个安卓 Agent 社区树立了极高的标杆。
>
> 在此基础上，**Sol Next** 围绕真机长期高频使用中遇到的核心痛点——**响应速度极限、虚拟屏坐标偏移、小米 HyperOS 等国产 ROM 长任务莫名暂停中断、AI 电话实战可用性与主动个人感知**——进行了从 **Rust 原生内核** 到 **网络协议栈、虚拟屏驱动与交互体验** 的全栈深度改造。
>
> 我们由衷敬佩并感谢 `@wangzan101` 与 Mika 社区的贡献！欢迎大家同时给原仓库 [**wangzan101/Mika**](https://github.com/wangzan101/Mika) 点亮 Star。

---

## ✨ 什么是 Sol Next 公开版？

**Sol Next** 是一款面向 Android 10–16 的**极速端云协同 AI 手机助理**：

- **🔓 100% 零内置模型 API Key（纯公开 BYOK 版）**：本仓库发布的公开版安装包（包名 `ai.sol.next`）**不包含任何内置密钥、不连任何私有服务器、不推送私人渠道更新**；安装后 30 秒填入你自己的 DeepSeek / OpenAI / OpenRouter / 硅基流动 / 通义千问 Key 即可直连官方服务商使用，Key 与个人记忆 100% 留存本机。
- **🦀 Rust v3.10 原生内核加速**：将 UI 控件树极限剪枝（`-74%~-97%`，耗时仅 `17–45 µs`）、System-0 BM25+同义词语义路由（`51 µs` · 0 Token）、SSE 流式增量步骤解析（`80 µs`）全部下沉至 Rust JNI 原生代码。
- **📱 1:1 复刻原生手机屏（0.0px 零误差）**：直读物理主屏 Display 0 的真实分辨率、DPI 与刷新率，完整 1:1 克隆后台虚拟屏（`scale=1.0`），通过 `injectTapPx` 与亚像素浮点直投彻底消除缩放与量化漂移。
- **🛡️ 64 轮防暂停防中断自愈体系**：彻底根治超时伪取消、小米 HyperOS 设置页误拦、5G/Wi-Fi 切网 UDP/QUIC 黑洞、后台确认无声卡死与无线调试瞬断问题，支持断点自动续跑。
- **📞 完整运营商级 AI 接打电话驾驶舱**：不抢占系统默认拨号器，支持豆包 Seeduplex 3.0 与 OpenAI Realtime 实时语音（BYOK）、3×4 IVR DTMF 拨号盘、免提切换、多路通话隔离、随时一键人工接管与通话纪要总结。
- **✨ 全维感知个人助理**：基于 Android KeyStore 端侧加密记忆，主动感知低电量、重要日程与通知并推送贴心提醒，后台代办顺序入队绝不打断主任务。

---

## 📊 Sol Next vs Mika：全方位对比与演进图解

为了帮助开发者和用户清晰了解我们在 Mika 基础上做了哪些深度改造，以下通过 **4 组架构与实测对比图 + 全量功能对照表** 呈现客观透明的对比结果。

### 1. 六层系统架构演进对比（Mika 原版底座 → Sol Next 深度重构）

<img src="docs/media/compare-architecture.png" alt="Mika 原版 vs Sol Next 六层架构演进对比图" width="100%" />

### 2. 核心性能、Token 压缩与延迟实测基准

<img src="docs/media/compare-benchmark.png" alt="Sol Next vs Mika 核心性能与延迟实测对比图" width="100%" />

### 3. 1:1 原生手机屏克隆 vs 传统缩放虚拟屏（坐标精度对比）

<img src="docs/media/compare-vdisplay-precision.png" alt="1:1 复刻原生手机屏 vs 传统缩放虚拟屏坐标精度对比图" width="100%" />

### 4. 八维工程能力雷达图（透明呈现双方各自优势）

<img src="docs/media/compare-radar-matrix.png" alt="Sol Next vs Mika 八维工程能力雷达图与客观对比" width="100%" />

### 5. 完整功能全景对比表（Comparison / Alternatives）

| 对比维度 | Mika 原版 (`wangzan101/Mika`) | **Sol Next 公开版 (`v6.3.0-public`)** |
|---|---|---|
| **开源协议与渊源** | Apache-2.0 原创开源标杆 | Apache-2.0 · 致敬并基于 Mika 深度重构演进 |
| **模型接入与隐私** | BYOK 自带 Key / 账号登录，无中转服务器 | **纯公开零内置 Key（BYOK）**，直连用户所选服务商，支持 DeepSeek / OpenAI / OpenRouter / 硅基流动 / 通义千问一键预设 + 实时握手测速 |
| **端侧原生内核** | Kotlin / JVM 控件处理 | **Rust v3.10 原生 JNI 内核**：UI 树极限剪枝 `-74%~-97%`（17–45 µs）、BM25 路由 `51 µs`、SSE 流式步骤提取 `80 µs` |
| **网络传输协议** | 标准 HTTP/2 请求 | **Android 14–16 原生 Chromium HTTP/3 (QUIC 0-RTT + 连接迁移)** + 12s 首包看门狗 + 连续 2 次失败自动熔断切 HTTP/2 + KV 前缀预热 |
| **后台虚拟屏规格** | 独立后台 VirtualDisplay（开创者） | **Display 0 物理参数 1:1 完全复刻**（`1080×2400 @ 420dpi · 60Hz · scale=1.0`，支持至 4K / 840dpi），展开浮窗支持 720p 高清实时触控 |
| **点击与滑动精度** | 缩放换算与通用坐标映射 | **`injectTapPx` 原始像素直击（0.0px 误差）** + 悬浮 PiP / OCR 亚像素浮点直投 + 全量标准 `TOOL_TYPE_FINGER` 硬件注入 |
| **无障碍解耦能力** | 依赖系统无障碍或辅助通道 | 支持 **零无障碍 `UiAutomationConnection` 直通读树** + `InputManagerGlobal` 定屏注入（关闭系统全部无障碍开关依然可执行跨页任务） |
| **跨页执行提速** | 逐轮等待完整响应与系统默认动画 | **Layer-0 原生 System API 直达（<15 ms）** + `uid=2000` 零动画加速（关闭自动恢复）+ 10 步批量编译 + **SSE 边吐边执行抢跑** |
| **长任务防暂停/防中断** | 常规重试与单轮中断恢复 | **64 轮长任务护航**：根治 `TimeoutCancellationException` 伪取消、6 轮阶梯重试、进程内 `WakeLock+WifiLock` 双保活、瞬断自动断点续跑、无线调试掉线静默自愈 |
| **小米 HyperOS 深度适配** | 通用 Android 适配 | **专项根治 HyperOS 痛点**：区分「密码与安全/清理缓存」常规设置避免误拦、三级返回兜底（`KEYCODE_BACK` → 左上角像素返回键 → 左边缘手势）、后台高风险确认自动弹高优通知 |
| **AI 接打电话模块** | 开创非默认拨号器 Telecom Companion 架构 | **完整运营商级 AI 电话驾驶舱**：兼容 `uid=2000`/`uid=0`、智能自动/Direct/Redirect 音频模式、多路来电隔离防串音、联系人解析、5–15 位短号（严禁紧急号）、**3×4 交互式 DTMF 拨号盘**、免提切换、实时计时与通话纪要失败重试 |
| **个人助理与主动感知** | 偏好记忆 + 定时任务 + 技能总结 | **独立「个人助理」空间**：Android KeyStore AES-GCM 本地加密记忆、低电量/重要通知/日程主动弹窗提醒、后台代办自动顺序排队绝不打断当前主任务 |
| **内置桌面浏览器 & Linux 沙箱** | ✅ **Mika 原版强项**：完整内置桌面级浏览器、每对话独立 Linux 沙箱（Python/Node）、丰富社区 App/网站知识库与 MCP 电脑联动 | 聚焦手机原生 App 极速直操与零冗余轻量化设计（若重度依赖内置浏览器与 Linux 沙箱，推荐同时使用原版 [Mika](https://github.com/wangzan101/Mika)！） |

### 6. 主流安卓 AI Agent 路线横向对比（适用场景与平替指南）

| 方案类型 | 代表项目 | 是否需要连电脑 | 是否抢占主屏 | 核心特点与适用人群 |
|---|---|---|---|---|
| **手机原生极速后台屏（Rust + 1:1 屏 + AI 电话）** | **Sol Next (`ai.sol.next`)** | ❌ 无线调试一次配对即可独立运行 | ❌ **1:1 独立后台虚拟屏** | 追求极致速度、0 漂移精准点击、小米/HyperOS 64 轮长任务零暂停、运营商级 AI 接打电话与纯 BYOK 隐私 |
| **手机原生全能沙箱助理** | **[Mika](https://github.com/wangzan101/Mika)** | ❌ 独立运行 | ❌ 后台虚拟屏 | 追求内置桌面级浏览器、每对话独立 Linux 沙箱（Python/Node）与社区 App/网站知识库 |
| **PC 端 ADB 视觉 Agent** | AppAgent / Mobile-Agent / Open-AutoGLM | ✅ 需持续连电脑运行 Python | ✅ 直接接管主屏 | 适合学术实验与桌面脚本联调，不适合日常脱离电脑随身使用 |
| **传统无障碍脚本工具** | Auto.js / Tasker 宏脚本 | ❌ 独立运行 | ✅ 抢占主屏 | 适合固定流程硬编码，不具备跨 App 自然语言理解与异常处理能力 |

---

## 📱 真实界面实拍画廊（Android 16 实机截图）

<table>
<tr>
<td align="center" width="33%">
<img src="docs/media/screen-public-welcome.png" width="250" alt="公开版零内置 Key 首页引导" /><br/>
<b>公开版纯净首页（零内置 Key）</b><br/>
<sub>清晰提示不内置任何 API Key，30 秒直达 BYOK 配置</sub>
</td>
<td align="center" width="33%">
<img src="docs/media/screen-public-byok.png" width="250" alt="BYOK 模型 API 配置页" /><br/>
<b>BYOK 自带模型配置</b><br/>
<sub>一键预设 DeepSeek / OpenAI / OpenRouter / 硅基流动 / 通义千问，支持实时测速</sub>
</td>
<td align="center" width="33%">
<img src="docs/media/screen-vdisplay-1to1.png" width="250" alt="1:1 原生后台虚拟屏展开" /><br/>
<b>1:1 物理屏克隆悬浮窗</b><br/>
<sub>实测 1080×2400 @ 420dpi 零缩放，随时展开零漂移触控</sub>
</td>
</tr>
<tr>
<td align="center" width="33%">
<img src="docs/media/screen-26step-task.png" width="250" alt="26 步连续任务零中断完成" /><br/>
<b>26 步长任务一气呵成</b><br/>
<sub>后台 1:1 虚拟屏连续 26 步翻页读取并结构化汇报，全程 0 暂停</sub>
</td>
<td align="center" width="33%">
<img src="docs/media/screen-ai-call-active.png" width="250" alt="AI 接打电话实时驾驶舱与 DTMF 拨号盘" /><br/>
<b>AI 电话驾驶舱 + 3×4 DTMF</b><br/>
<sub>保留原生拨号器，实时计时、静音托管、一键人工接管</sub>
</td>
<td align="center" width="33%">
<img src="docs/media/screen-brain-cockpit.png" width="250" alt="全脑中枢与 Rust QUIC 性能遥测" /><br/>
<b>全脑中枢 · Rust/QUIC 遥测</b><br/>
<sub>实时监控 HTTP/3 QUIC、Rust 剪枝率、零动画与端侧状态</sub>
</td>
</tr>
</table>

---

## 🚀 30 秒快速开始（零内置 Key · 三步开用）

### 第 1 步：下载安装公开版 APK
前往 [**Releases 页面**](https://github.com/chongyangzhang92-hub/Sol-Next/releases/latest) 下载：
- **`Sol-Next-v6.3.0-public-arm64.apk`**（推荐绝大多数现代安卓手机，85 MB，包名 `ai.sol.next`）
- **`Sol-Next-v6.3.0-public-universal.apk`**（全架构通用包，含 `arm64-v8a` + `x86_64`，106 MB）

> 公开版使用独立包名 `ai.sol.next`，与任何其他应用互不冲突，且**不包含任何内置密钥、不连接任何私有服务器**。

### 第 2 步：填入你的模型 API Key（BYOK）
1. 打开 Sol Next，点击首页提示条或进入底部 **「后台手机」** 标签页顶部的 **「模型 API 配置（公开版 · 自带 Key / BYOK）」**。
2. 点击一键预设（**DeepSeek** / **OpenAI** / **OpenRouter** / **硅基流动** / **通义千问**）或自定义任意 OpenAI 兼容接口。
3. 粘贴你自己的 `sk-...` API Key，点击 **「保存并测速」**，看到 `✓ 连接成功` 即可立即开始对话与执行任务（无需重启 App）。

详细服务商配置与 AI 电话实时语音配置请阅读 👉 [**BYOK 模型与语音完整配置指南**](docs/guides/BYOK_SETUP.md)。

### 第 3 步：免电脑开启 1:1 后台虚拟手机（可选）
仅聊天或查询无需此步骤；如需在后台独立虚拟屏操作第三方 App：
1. 在「后台手机」页点击 **「一键全自动配对」**，按引导在系统「开发者选项 → 无线调试 → 使用配对码配对设备」中点开配对码。
2. 在弹出的通知栏直接输入 6 位配对码即可自动连接 `uid=2000` 后台助手，立即解锁 **1:1 原生后台虚拟屏、零动画跨页加速、零无障碍节点直通与 AI 电话伴侣权限**。

---

## 🤖 Agent-Ready：让 AI 编程助手零幻觉部署 & MCP 直连手机

本仓库完整支持 **Agent-Ready 标准**，内置 [`llms.txt`](llms.txt)、[`llms-full.txt`](llms-full.txt)、[`AGENTS.md`](AGENTS.md)、[`CLAUDE.md`](CLAUDE.md)、[`.env.example`](.env.example)、零依赖 CLI 与原生 MCP Server：

### 1. 一句话让 AI 助手帮你安装到手机（Claude Code / Cursor / Codex / Antigravity）
> 💡 电脑连上安卓手机（USB 或无线 ADB），直接把下面这句话发给你的 AI 助手：
>
> `请按 https://github.com/chongyangzhang92-hub/Sol-Next/blob/main/docs/guides/INSTALL_WITH_AGENT.md 的步骤，下载校验 SHA-256 并把零内置 Key 公开版 Sol Next (ai.sol.next) 安装到当前 ADB 连接的安卓手机上，并启动 1:1 后台虚拟屏助手。`

### 2. 零依赖非交互式 CLI（支持 `--json` 结构化输出）
```bash
python3 scripts/sol-cli.py status --json
python3 scripts/sol-cli.py install --verify-sha256 --grant-permissions --json
python3 scripts/sol-cli.py start-helper --json
python3 scripts/sol-cli.py run --intent "打开系统设置并查看电池电量" --json
```

### 3. 原生 MCP Server（零外部依赖，直接接入 Claude Desktop / Cursor / Claude Code）
```json
{
  "mcpServers": {
    "sol-next": {
      "command": "python3",
      "args": ["/path/to/Sol-Next/mcp/sol_mcp_server.py"]
    }
  }
}
```
提供 4 个标准 MCP 工具：`sol_device_status`、`sol_install_public_apk`、`sol_start_virtual_display_helper`、`sol_run_phone_task`。

---

## ❓ 常见问题（FAQ）

- **Q1：有没有类似 Mika、但速度更快、在小米 HyperOS 上不容易暂停中断的开源安卓 AI 助理？**
  **Sol Next** 正是在 Mika 基础上针对「端侧速度（Rust v3.10 剪枝 + QUIC + 零动画）」「1:1 虚拟屏零漂移」「小米 HyperOS 防误拦与 64 轮断点自愈」进行全栈深度重构的开源项目。
- **Q2：Sol Next 公开版免费吗？需要注册账号或经过第三方中转服务器吗？**
  完全免费（Apache-2.0），无需注册账号、无任何私有中转服务器。采用纯 BYOK 模式，你在手机上填入自己的 DeepSeek / OpenAI / OpenRouter / 硅基流动 / 通义千问 Key 即可直连官方接口。
- **Q3：支持 AI 自动接听和拨打运营商电话吗？会替换我的系统拨号器吗？**
  支持。沿用并完善了 Mika 的非默认拨号器 Telecom Companion 架构，**保留你的系统原生拨号器**，支持豆包 Seeduplex 3.0 与 OpenAI Realtime（BYOK）、3×4 DTMF 语音菜单按键、免提与随时一键人工接管。
- **Q4：能和原版 Mika 同时装在同一台手机上吗？**
  可以。Sol Next 公开版包名为 `ai.sol.next`，与原版 Mika 互不冲突，方便你按场景自由切换。

---

## 🔒 公开版安全与隐私承诺

- **零内置密钥审计**：公开版在构建期通过硬性安全门禁禁止打包任何模型凭据文件（`assets/sol-models.properties` 不存在），可随时用 `unzip -l` 校验。
- **零私有中转服务器**：对话请求由你的手机直接发往你在 BYOK 页面填写的模型服务商（如 `api.deepseek.com`、`api.openai.com` 等）。
- **高风险操作显式门控**：涉及付款、转账、下单、删除、卸载、拨打/接听/挂断电话等敏感操作前自动拦截并请求你手动确认；切后台时自动弹出高优先级系统通知，绝不暗中放行或无声卡死。
- **独立发布渠道**：本公开版仅面向社区公开发布，绝不向任何私人测试机推送覆盖更新。

---

## 📄 开源协议与版权声明

- 本项目遵循 **Apache License 2.0** 协议（详见 [LICENSE](LICENSE) 与 [NOTICE](NOTICE)）。
- 再次向原作者 **[@wangzan101](https://github.com/wangzan101)** 及其开创性项目 **[Mika](https://github.com/wangzan101/Mika)** 致以最诚挚的敬意！
