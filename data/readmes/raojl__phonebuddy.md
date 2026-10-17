# phoneBuddy

> 会打电话的 AI 客服 —— 让大模型真正拿起电话听、思考、开口说。

phoneBuddy 是一个基于 **Rust + PJSIP + Tauri 2** 的桌面版 AI 智能电话客服。它可以注册到标准 SIP 电话系统（老式 PBX / Asterisk / 公网 SIP 服务商），自动接听来电或主动外呼，实时听懂对方说话，交给大模型思考，再把回复用语音说回去。

- **呼出**：主动拨打 → 被叫方就是客户
- **呼入**：接听来电 → 主叫方就是客户

```
客户说话 ──RTP──▶ PJSIP ──▶ ASR 语音识别 ──▶ 大模型(DeepSeek) ──▶ TTS 语音合成 ──RTP──▶ 客户听到
```

---

## 目录

- [核心能力](#核心能力)
- [技术栈](#技术栈)
- [架构总览](#架构总览)
- [目录结构](#目录结构)
- [快速开始](#快速开始)
- [配置说明](#配置说明)
- [使用说明](#使用说明)
- [扩展新场景](#扩展新场景)
- [踩坑记录](#踩坑记录)
- [文档](#文档)
- [安全说明](#安全说明)
- [许可证](#许可证)

---

## 核心能力

| 能力 | 说明 |
|------|------|
| SIP 软电话 | 标准 SIP 协议注册 / 呼出 / 呼入 / 接听 / 挂断，兼容老式 PBX |
| 实时语音识别 | 通话音频实时转文字，边说边出字幕 |
| AI 智能对话 | 流式对接大模型，带工具调用（Function Calling） |
| 实时语音合成 | AI 回复按句切分，边合成边播放，首句约 1 秒 |
| 语音打断（Barge-in） | 客户开口打断时立即停止播报，切换为倾听 |
| 业务工具 | 查客户、查订单、查菜单、下单、取消、建工单、查知识库 |
| 技能系统 | Markdown 定义场景话术，运行时热加载，加场景不用改代码 |
| 会话持久化 | 通话记录与 Agent 会话落 SQLite / JSONL |

---

## 技术栈

| 层次 | 选型 | 说明 |
|------|------|------|
| 电话协议栈 | **PJSIP 2.17** | 业界最成熟的开源 SIP 协议栈，支持标准 SIP over UDP/TCP |
| 宿主语言 | **Rust** (edition 2021, ≥ 1.77.2) | 承载音频回调、异步任务、并发控制 |
| 桌面框架 | **Tauri 2** | 轻量跨平台壳，前端用系统 WebView2 渲染 |
| 前端 | 原生 HTML/CSS/JS | 单文件 `frontend/index.html`，无构建步骤 |
| 大模型 | **DeepSeek**（OpenAI 兼容） | 可替换为任意 OpenAI 兼容服务 |
| 语音识别 | **腾讯云 ASR** | WebSocket 流式，16k 中文 |
| 语音合成 | **腾讯云 TTS** | WebSocket 流式，边合成边播 |
| 数据存储 | SQLite (`rusqlite`) | 客户、菜单、订单 |
| 异步运行时 | Tokio | 全异步任务编排 |

> **为什么用 PJSIP 而不是纯 Rust 方案？**
> 目标是接入真实的老式 PBX，需要标准 SIP 注册 + 媒体流。Rust 生态目前没有成熟的独立 SIP 客户端 SDK（rsipstack 只有信令、没有媒体；Aria Softphone 的 SIP 实现未独立发布）。PJSIP 是唯一完整的方案，因此采用 Rust 宿主 + C 中间层的 FFI 架构。

---

## 架构总览

```
┌─────────────────────────────────────────────────────────────┐
│  Tauri 2 桌面应用 (WebView2 + 原生 HTML/JS)                  │
│  拨号盘 · 聊天区 · 场景面板 · 实时日志 · TTS 状态            │
└───────────────┬─────────────────────────────────────────────┘
                │ Tauri Commands / Events
┌───────────────▼─────────────────────────────────────────────┐
│  Rust 宿主 (lib.rs / sip.rs / speech_pipeline.rs)            │
│  · 命令调度   · 流式语音管线   · 打断控制   · 会话与技能      │
│                                                              │
│  ┌──────────────┐   ┌──────────────┐   ┌─────────────────┐  │
│  │ agent/       │   │ tts_live.rs  │   │ db.rs           │  │
│  │ 流式对话+工具 │   │ 实时合成      │   │ SQLite          │  │
│  └──────────────┘   └──────────────┘   └─────────────────┘  │
└───────────────┬─────────────────────────────────────────────┘
                │ FFI (extern "C")
┌───────────────▼─────────────────────────────────────────────┐
│  pjsip_bridge.c  —— PJSIP C 中间层                           │
│                                                              │
│        PJSIP 会议桥 (Conf Bridge)                            │
│         ├── 端口 A：put_frame   ← 远端音频 → Rust（听）       │
│         └── 端口 B：get_frame   ← Rust 写入  → 远端（说）     │
└───────────────┬─────────────────────────────────────────────┘
                │ RTP / SIP
         ┌──────▼──────┐
         │  PBX / 客户  │
         └─────────────┘
```

**核心设计：在 PJSIP 会议桥上挂两个方向相反的自定义音频端口，一个用来听、一个用来说。** 其余工程复杂度都围绕如何让这两个端口在真实通话里稳定、低延迟、可打断。

---

## 目录结构

```
phonebuddy/
├── README.md
├── LICENSE
├── .env.example                 # 环境变量模板（复制为 .env）
│
├── docs/                        # 项目文档
│   ├── 01-项目总览.md
│   ├── 02-关键技术路径.md
│   ├── 03-早期架构设想.md
│   └── 04-性能优化设计.md
│
├── frontend/
│   └── index.html               # 全部前端界面（单文件，无构建）
│
├── scripts/                     # 语料生成工具（Python）
│   ├── tencent_tts_demo.py      # 腾讯云 TTS 最小可用 Demo
│   └── generate_tts_corpus.py   # AI 穷举语料 + 批量 TTS 合成
│
├── assets/
│   └── tts/
│       └── index.json           # 预录音语料索引（音频本体需自行生成）
│
└── src-tauri/                   # Rust / Tauri 应用
    ├── Cargo.toml
    ├── build.rs                 # 自动调用 MSBuild 编译 PJSIP 与 C 桥接层
    ├── tauri.conf.json
    ├── sip-config.json          # SIP 服务器配置（已脱敏）
    ├── capabilities/
    ├── icons/
    ├── skills/                  # 场景技能（Markdown，可热插拔）
    │   ├── 订餐服务.md
    │   ├── 产品咨询.md
    │   ├── 技术支持.md
    │   └── 售后投诉.md
    └── src/
        ├── main.rs              # 入口 / 日志 / panic hook
        ├── lib.rs               # Tauri 命令与全局状态
        ├── config.rs            # 统一配置读取（环境变量 / .env）
        ├── sip.rs               # SIP 引擎 + ASR 客户端
        ├── speech_pipeline.rs   # 流式语音管线（ASR→LLM→TTS 编排）
        ├── tts_live.rs          # 腾讯云 TTS 实时流式合成
        ├── tts.rs               # 预录音 TtsBank（离线拼接方案）
        ├── db.rs                # SQLite 客户 / 菜单 / 订单
        ├── system_prompt.txt    # 基础 System Prompt
        ├── pjsip_bridge.c       # PJSIP C 中间层（FFI 边界）
        └── agent/               # Agent 内核
            ├── mod.rs
            ├── agent_loop.rs    # 流式对话循环 + 工具调用
            ├── tools.rs         # 工具定义与实现
            ├── skill.rs         # 技能（Markdown）解析与路由
            ├── session.rs       # 会话持久化
            ├── compaction.rs    # 上下文压缩
            └── events.rs        # 事件定义
```

---

## 快速开始

### 1. 环境要求

| 依赖 | 版本 | 说明 |
|------|------|------|
| Rust | ≥ 1.77.2 | `rustup` 安装，需 MSVC 工具链 |
| Visual Studio Build Tools 2022 | v143 工具集 | 需勾选「使用 C++ 的桌面开发」与 Windows SDK |
| PJSIP | **2.17** | 见下一步，源码放在仓库根目录 `pjproject/` |
| WebView2 Runtime | 任意 | Win10/11 通常已内置 |
| Python | ≥ 3.9 | 仅用于 `scripts/` 下的语料生成工具，可选 |

### 2. 准备 PJSIP 源码

下载 [PJSIP 2.17](https://github.com/pjsip/pjproject/releases/tag/2.17) 源码，解压到**仓库根目录**并重命名为 `pjproject`：

```
phonebuddy/
└── pjproject/          ← 放在这里
    ├── pjproject-vs14.sln
    ├── pjlib/
    ├── pjmedia/
    ├── pjsip/
    └── ...
```

`build.rs` 会自动用 MSBuild 编译它（首次编译约数分钟），产物是 `pjproject/lib/pjproject.lib`。**无需手动编译。**

> 若 PJSIP 未放置，项目仍可编译，但会自动降级为「SIP 功能不可用」模式，便于先调试界面与 Agent。

### 3. 配置密钥

```bash
cp .env.example .env
```

编辑 `.env`，至少填入：

```ini
DEEPSEEK_API_KEY=sk-xxxxxxxx
TENCENT_APP_ID=1234567890
TENCENT_SECRET_ID=AKIDxxxxxxxx
TENCENT_SECRET_KEY=xxxxxxxx
```

### 4. 编译运行

```bash
cd src-tauri
cargo run
```

首次编译会依次完成：编译 PJSIP → 编译 C 桥接层 → 编译 Rust → 启动应用。

### 5. 打包发布

```bash
cd src-tauri
cargo tauri build
```

---

## 配置说明

所有密钥均通过**环境变量或 `.env` 文件**注入，源码中不含任何真实凭据。读取优先级：进程环境变量 > `.env` 文件 > 内置默认值。

| 变量名 | 必填 | 默认值 | 说明 |
|--------|:----:|--------|------|
| `DEEPSEEK_API_KEY` | ✅ | — | DeepSeek API Key |
| `DEEPSEEK_BASE_URL` | | `https://api.deepseek.com/v1` | 任意 OpenAI 兼容地址 |
| `DEEPSEEK_MODEL` | | `deepseek-chat` | 模型名 |
| `TENCENT_APP_ID` | ✅ | — | 腾讯云 AppID（ASR / TTS 共用） |
| `TENCENT_SECRET_ID` | ✅ | — | 腾讯云 SecretId |
| `TENCENT_SECRET_KEY` | ✅ | — | 腾讯云 SecretKey |
| `SIP_SERVER` | | — | 如 `sip:sip.example.com`，留空则用界面输入 |
| `SIP_USER` | | — | SIP 账号 |
| `SIP_PASSWORD` | | — | SIP 密码 |
| `SIP_DISPLAY_NAME` | | — | 显示名 |
| `VS_INSTALL_PATH` | | 自动探测 | 手动指定 VS 安装路径（`build.rs` 用） |
| `PHONEBUDDY_CC` | | 自动探测 | 手动指定 `cl.exe` 路径，用于排查 C 桥接层编译错误 |

`.env` 文件查找顺序：当前工作目录 → 可执行文件同目录 → 项目根目录。

---

## 使用说明

1. **注册 SIP**：左侧「SIP 配置」面板填入服务器 / 用户名 / 密码 → 点「注册」。若 `.env` 已配置 `SIP_*`，启动时会自动注册。
2. **拨打电话**：拨号盘输入号码 → 点拨打。呼出时**被叫方即客户**。
3. **接听来电**：有来电时点「接听」。呼入时**主叫方即客户**。
4. **对话**：接通后直接说话即可。ASR 实时字幕显示在中间聊天区，AI 回复以文字 + 语音同时呈现。
5. **打断**：AI 播报过程中直接开口说话，系统检测到人声会立即停止播报并转入倾听。
6. **查看状态**：底部日志区实时显示 SIP 信令、ASR 事件、Agent 调用等。

### 预录音语料库（可选）

除了实时 TTS，项目还保留了「预录音拼接」方案（`tts.rs` + `assets/tts/`），零延迟、零网络依赖，适合话术固定的垂直场景。

音频本体不随仓库分发，需自行生成：

```bash
cd scripts
pip install httpx websocket-client

DEEPSEEK_API_KEY=sk-xxx \
TENCENT_TTS_APPID=xxx \
TENCENT_TTS_SECRET_ID=xxx \
TENCENT_TTS_SECRET_KEY=xxx \
python generate_tts_corpus.py
```

脚本会：调用大模型穷举场景语料 → 批量调用腾讯云 TTS 合成 PCM → 生成 `assets/tts/index.json` 索引。

单独验证 TTS 通路可用：

```bash
cd scripts
TENCENT_TTS_APPID=xxx TENCENT_TTS_SECRET_ID=xxx TENCENT_TTS_SECRET_KEY=xxx \
python tencent_tts_demo.py "您好，欢迎致电，请问需要点餐吗？"
```

---

## 扩展新场景

在 `src-tauri/skills/` 下新增一个 Markdown 文件即可，无需改代码、无需重新编译（运行时加载）：

```markdown
---
name: 预约服务
trigger: ["预约", "挂号", "订位", "改期"]
---

# 预约服务

## 可用工具
- customer_lookup — 查客户信息
- create_ticket — 创建预约工单

## 工作流程
1. 客户说要预约 → 先确认时间、人数
2. 调用 create_ticket 创建工单
3. 复述预约信息请客户确认
```

Agent 会根据 `trigger` 关键词自动路由到对应技能，`## 可用工具` 段落决定该场景下开放哪些工具。

---

## 踩坑记录

| 现象 | 根因 | 解法 |
|------|------|------|
| 挂断电话即崩溃 (0xC0000005) | PJSIP 2.14 conf bridge 存在 use-after-free | 升级到 PJSIP 2.17 |
| Rust 端读 PJSIP 结构体必段错误 | 手写 struct 定义字段偏移不全 | 引入 C 中间层 `pjsip_bridge.c` 承接所有结构体操作 |
| 注册时 SIGSEGV | 无控制台窗口下 PJSIP 写 stdout | `#![windows_subsystem = "windows"]` + 日志静默 + 落盘 |
| MSBuild 编译报「环境变量名或值太长」 | 多进程模式 + 过长 PATH | `/m:1 /nodeReuse:false` |
| 第二通电话 ASR 不启动 | `on_call_media_state` 早于上一通的 `DISCONNECTED` | 用 call_id 追踪连接归属，不一致则先断后连 |
| 呼入时 ASR 不启动 | `sipCallId` 在 `await` 之后才赋值，事件抢先到达 | 赋值提前到 `await` 之前 |
| ASR 同一个 slice 弹出多个气泡 | 每个 final 片段都触发冻结+清空 | 改为单气泡累积 + 只在满足送 AI 条件时冻结 |
| 叹气/噪音产生 4 个气泡 | ASR 把噪音拆成多个 sliceId | 不按 sliceId 建气泡，统一为单一活跃气泡 |
| TTS 报「无活跃通话」 | `get_last_call_id` 只在呼出时更新 | 新增 `bridge_get_active_call_id`，呼入呼出通用 |
| 音频喂得越快识别越乱 | 分片过碎（40ms/1280B） | 改为 80ms/2560B，并设最小阈值 640B |

---

## 文档

| 文档 | 内容 |
|------|------|
| [01-项目总览](docs/01-项目总览.md) | 产品视角：做什么、能干什么、演进历程 |
| [02-关键技术路径](docs/02-关键技术路径.md) | 技术视角：五条核心链路、关键决策、踩坑根因 |
| [03-早期架构设想](docs/03-早期架构设想.md) | 立项初期的方案设计（与最终落地不同，留作对照） |
| [04-性能优化设计](docs/04-性能优化设计.md) | 延迟与吞吐的优化思路 |

---

## 安全说明

- 仓库内**不含任何真实密钥**，所有凭据通过 `.env` / 环境变量注入，`.env` 已在 `.gitignore` 中忽略。
- `config.rs` 只提供「读取」能力，不会打印任何密钥明文，启动时仅输出「已配置 / 缺失」状态。
- 如你 fork 本仓库，请务必确认 `.env` 未被误提交（`git status` 应看不到它）。
- 曾经泄露的密钥请在对应平台**立即轮换作废**，不要只依赖删除文件。

---

## 许可证

[MIT](LICENSE)

---

**技术栈**：Rust · PJSIP · Tauri 2 · DeepSeek · 腾讯云语音服务
