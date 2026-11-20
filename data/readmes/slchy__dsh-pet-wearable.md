# dsh-pet-wearable

<div align="center">

[![Node.js](https://img.shields.io/badge/node-%3E%3D22.18.0-brightgreen.svg)](https://nodejs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.7-blue.svg)](https://www.typescriptlang.org/)
[![Tests](https://img.shields.io/badge/tests-638%20passing-success.svg)](#-开发与测试)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Status: Experimental](https://img.shields.io/badge/status-active%20development-orange.svg)](#)

**面向智能穿戴设备的云端全双工语音伴生 Agent（基于 `dsh` / DeepSeek Harness）**

低功耗端侧接入 · 快慢双轨投机推理 · 毫秒级打断 · 伴生在场感 · 硬件无关能力协商

[💡 核心特性](#-核心特性) • [🏛️ 架构设计](#️-系统架构) • [🚀 快速开始](#-快速开始) • [📊 性能与延迟](#-性能表现与端到端延迟) • [⚙️ 配置说明](#️-配置说明) • [📚 详细文档](#-详细文档导航)

</div>

---

## 🌟 为什么需要 dsh-pet-wearable？

智能穿戴设备（如智能眼镜、耳机、手表）受限于**电池容量**与**散热空间**，无法在端侧运行高算力大模型。传统语音助手往往依赖机械唤醒与半双工轮候，交互割裂且反应迟缓：

| 维度 | 传统智能语音助手（如 Siri / 智能音箱） | `dsh-pet-wearable` 云端伴生 Agent |
|:---|:---|:---|
| **交互模式** | **半双工**：喊唤醒词 ➔ 等待提示音 ➔ 用户说话 ➔ 静候播报 | **全双工免唤醒**：端侧能量门 + 语义判停，随心自然切句 |
| **打断能力** | 必须等待一整段播完，或强行再喊唤醒词中断 | **毫秒级 Barge-in**：用户一开口即刻止声，同步取消在途推理 |
| **响应延迟** | 串行等待 2–4 秒，复杂任务长时间尴尬留白 | **双轨投机并发**：短句闲聊 ~1.1s 直答；深思任务回执自然垫音 |
| **存在形态** | **工具型**：被动等待召唤，无唤醒则如同死物 | **伴生型（Pet）**：感知佩戴、电量与时段，在适宜时机克制搭话 |
| **硬件侵入** | 深度绑定特定芯片或专属硬件 SDK | **轻量标准化**：端侧仅搬运音频与传感器帧，接入新硬件 0 改动 |

> [!NOTE]
> **关于命名中的 "pet"（伴生理念）**：
> 这里的 `pet` 并非桌面像素动画、固定 3D 模型或虚拟化身，而是行为层面的**自然在场感与适度主动性**。全天候穿戴设备需要低存在感的贴身形态——不吵闹、知时务、懂进退，在用户开口时随时倾听。

---

## 💡 核心特性

- ⚡ **快慢双轨投机推理（Fast Lane + dsh）**
  - **快车道直达**：日常闲聊与短句通过快模型直接响应，真机实测端到端首字 **p50 920–1054 ms**（四场配对，n=17–39；单场受台词影响，见下文基准表）。
  - **委派判据是语义，不是字面**：本地只挡三种形态（空、超 `FAST_LANE_MAX_CHARS`、含阿拉伯数字），**其余一律先问快模型**，由它在流里输出 `[[DELEGATE]]` 决定转交。词表判过的时代，「你看过吗」「为什么」这类闲聊因为含「看」「为什么」被一票判成任务，真机 92 轮里 25 轮白走 `dsh`。默认 `FAST_LANE_KEEP_TURNS=0`：**不按轮数强制转交**（曾让每 4 轮里有 1 轮等 6–8 秒）。
  - **深度思考与工具调度**：复杂逻辑、事实检索与图文问答交由 `dsh` 进行多步推理与 Subagent 任务派发。
  - **投机并发与委派回执**：双轨并行起跑，若快车道超时或判定需转交，立即垫一句自然回执（如「我看看。」）填补空白，答案就绪后即刻顶掉回执并清空下行缓冲。
- 🎙️ **真正的全双工与自然打断（Full-Duplex & Barge-In）**
  - 基于上行能量门（-40 dBFS）+ 语义判停（TurnJudge），自适应停顿切句，无需唤醒词。
  - 用户开口即打断：流式 ASR 一旦捕捉到新发言（语气词除外），立即下发 `audio.stop` 终止下行音频，并取消正在执行的上游推理与排队轮次。
- 🐾 **情境感知与有节制的主动开口**
  - 基于佩戴状态、剩余电量、深夜时段、环境静默时长以及发言间隔构建多维时机状态机。
  - 在合适时机受控地主动搭话；低电量或深夜时段自动抑制，保持行为的可解释性。
- 🔌 **硬件解耦与能力协商（Hardware Agnostic）**
  - `src/devices/` 仅定义 6 个标准下行操作与 6 个上行事件，在 `Hello` 握手阶段动态协商设备能力。
  - 能力缺失时平滑降级（如设备不支持拍照则不触发视觉推理），接入新型号硬件（如[雷鸟 X3 Pro](./docs/devices/RAYNEO-X3-PRO.md)）无需改动核心代码。
- 🧪 **零密钥本地闭环与可测性**
  - 内置 `canned` 识别、`silent` 合成与 `echo` 代理，单机零配置秒级跑通全链路。
  - 提供纯虚拟时间模拟器（`npm run sim`），支持状态空间探索与因果回溯，全仓 638 个测试用例保障时序稳定性。

---

## 🏛️ 系统架构

### 1. 数据流与双轨架构

```
端侧（智能眼镜 / 耳机 / 手机）              云端服务（本仓 src/）
  AudioRecord / AudioTrack  ────────►  TLS 连接（帧协议 · 鉴权 · 心跳保活）
  Camera / 佩戴 / 电量 / 触摸  ─────►          │
                                               ▼
                               能量门 → ASR → 语义判停（UtteranceAssembler / TurnJudge）
                                               │ 整句 / 定稿
                                               ▼
                               DialogFsm（话筒票据 · 轮次生命周期仲裁）
                                               │
                                 ┌─────────────┴─────────────┐
                                 ▼                           ▼
                         快车道 FrontedAgent          dsh（工具 / 后台 Job / 子代理）
                           短句闲聊极速响应              复杂推理、事实检索、多模态
                                 └─────────────┬─────────────┘
                                               ▼
                                    TTS（CosyVoice）→ PCM 流式下发
```

### 2. 双轨投机时序瀑布流（Latency Waterfall）

```text
[用户停嘴] ───────────────┬───────────────────────────────────►
                           ▼
                  [TurnJudge 语义判停收敛 ~2ms]
                           │
      ┌────────────────────┴────────────────────┐
      ▼ (快车道直跑)                            ▼ (转交 dsh 多步推理)
  [轻量模型 TTFT ~260ms]                    [投机超时 / 暗号触发]
      │                                         │
  [TTS 句首裁静音下发 ~350ms]               [下发自然回执: "我看看..."]
      │                                         │
  📢 穿戴端出声 (端到端 ~1.1s)              [Subagent / MCP 执行完毕]
                                                │
                                            📢 顶掉回执，平滑播发正文 (~1.5s)
```

### 3. 严格的抢占式话筒仲裁（Floor Arbiter）

话筒状态由 `AppSession.floor` 统一管理，遵循确定性抢占规则：

| 占用者 | 可被谁抢占 | 说明 |
|:---|:---|:---|
| `user` | **无** | **用户永远最高优先**：任何状态下开口立即抢下话筒 |
| `reply` | `user` | 正在播发正题回答，可被用户随时插话打断 |
| `announce` | `user`、`reflex` | 后台作业播报：**抢不动正题**，等正题说完且安静后才播 |
| `pet` | `user`、`reflex` | 主动开口：不与正题冲突，安静后受控触发 |
| `reflex` | 任何人（除 `user`） | 垫音反馈（如回执提示音），可被正文随时顶掉 |

---

## 🚀 快速开始

### 前提条件

- **Node.js** >= 22.18.0
- （可选）接入真实硬件需安装 `ffmpeg`（用于 mSBC 解码）

### 1. 零密钥本地跑通（5 秒闭环验证）

使用内置离线 Mock 组件，无需真实硬件或 API Key 即可跑通完整会话链路：

```bash
# 1. 安装依赖
npm install

# 2. 启动服务（监听 8766 端口，使用离线 Mock）
node src/main.ts --listen 8766 --stt canned --tts silent --agent echo
```

在另一终端运行测试客户端模拟穿戴设备推流：

```bash
node tools/fake-phone.ts --port 8766 --sbc tmp/voice.sbc
```

运行后控制台将打印正常的会话握手与轮次日志：
```text
[Main] listening on 127.0.0.1:8766 (plain)
[Device] handshake completed: protocol=v2 capabilities=[audio, wear, battery]
[Floor] turn started: #1 speaker=user
[FastLane] hit: "你好呀" -> "你好！我在呢。" (TTFT: 240ms)
[TTS] audio chunk dispatched: 3200 bytes
[Floor] turn settled: #1 duration=1080ms
```

### 2. 虚拟时间逻辑仿真（主动开口探索）

纯虚拟时间运行，无需网络、API 密钥与音频驱动，快速验证主动开口策略与状态机因果不变式：

```bash
npm run sim                          # 运行预设声明式场景
npm run sim -- --explore --runs 500  # 随机探索 500 次，检测不变量违规
npm run sim -- --trace out/          # 导出完整时序时间线（JSONL 格式）
```

### 3. 连接真实穿戴设备与云端模型

1. 配置环境变量：
   ```bash
   cp .env.example .env
   # 编辑 .env 配置各云厂商 API Key（Aliyun STT / CosyVoice / LLM）
   ```
2. 安装 `dsh` 人设 Profile 补丁（使用 `dsh` 时必选）：
   ```bash
   npm run install-profile      # 自动拷入 ~/.dsh/profiles/sdk/cordis.patch.yml
   ```
3. 启动全功能生产服务：
   ```bash
   node src/main.ts --listen 8766
   ```

---

## 📊 性能表现与端到端延迟

### 延迟衡量口径

> [!IMPORTANT]
> 本项目提及的 `p50` / `p90` **不加限定时一律指「闭嘴 → 出声」**（端到端完整链路）：
> 即 **用户停嘴（能量门关闭时刻）➔ 穿戴设备听到首个有效字声音**。
> 计算公式：`firstWordMs` = ① ASR 识别 + ② 语义判停收敛 + ③ 模型 TTFT + ④ TTS 首包解码。
> （下面回放表里的「③ →首块」一列 = 上式 **③+④**：模型首字到设备听到首块音频。）

### 基准实测数据

**真机**（快车道直答、0 次委派，线上 `qwen-realtime` + `cosyvoice`）。
四场台词不同，**单场绝对值不可比**，只做前后配对；`①+②+③` 按**逐轮合计**取中位，不是各段中位相加：

| 场次 | 有效轮 | **p50** | ① 停嘴→定稿 | ② 定稿→开轮 | ③ 开轮→首块 | 配置差异 |
|:---|:---:|:---:|:---:|:---:|:---:|:---|
| `20261119-153754` | 39 | 1054 | 300 | 8 | 597 | ② 预算 400 |
| `20261119-160012` | 22 | 1257 | 324 | 4 | 817 | ② 预算 400 |
| `20261119-160921` | 21 | **920** | 295 | 25 | 567 | ② 预算 200 |
| `20261120-031505` | 17 | 991 | 300 | 26 | 643 | ② 预算 200 |

> **p50 的波动主要来自两次改动**：连接保活（每轮省 130–190 ms，见下）把 `③` 压到
> 模型段 ~184 ms；`②` 的等待预算从 400 收到 200 后，那三成「等了一下」的轮次不再
> 每轮多付 200 ms。两场 200 预算的差（920 / 991）来自台词与 `③` 的服务端抖动。

> **同一份向量回放**（7 轮）：路径分布 `fast` 5/7。
> 但回放的 ASR 与真机**逐字一致只有 1/7**（同一 `qwen-realtime`，音量链不同），
> 所以回放只看**走哪条腿**，绝对延迟一律以真机档案为准。

> **残余的大头**：
> `①` 已到 300 ms 上下，其中约 68 ms 是封段等的「一整个上行包」——静音帧在同一包里
> 不参与计时，配置的 `VOICE_COMMIT_MS=20` 实际从未生效（见 [docs/TOOLS.md](./docs/TOOLS.md) 的 `silence-runs.py`）。
> `③` 里模型段约 184 ms、TTS 首包约 320–400 ms；**偶发长尾在 TTS 侧**，
> 真机 112 轮里 8 次超过 900 ms，`tts.done` 显示文本都在 100 ms 内送完，
> 慢在 `finish-task` 之后的合成。

### 核心延迟优化技术

- 🔌 **HTTP 连接保活 50 s**：`fetch` 默认的 `keepAliveTimeout` 是 **4 s**，而真机上两轮间隔 p50 就有 5–7 s —— 等于**每轮重做一次 TLS 握手**（复用 146–296 ms vs 新建 375–434 ms）。全局 dispatcher 把它拉到 50 s 后，模型段从 ~300 ms 回到 ~184 ms（`MIAI_HTTP_KEEPALIVE_MS`，见 `src/http-agent.ts`）。
- 🏎️ **判停前起跑（Prefetch）**：ASR 识别定稿瞬间即预先发起推理请求，不再等待判停静默期结束，开轮至模型首字缩减 ~220ms。
- 🔮 **中间结果投机（Partial Speculation）**：能量门静音瞬间抓取最新 partial 提前请求；认领要求**去全部标点后完全一致**，坏情况下退回定稿不影响正确性。
- 🚫 **不按期强制转交**：攒满 N 轮就整句交给 `dsh` 曾让**每 4 轮就有 1 轮**（用户只是想聊两句）等 6–8 秒。改成 `FAST_LANE_KEEP_TURNS=0`（永不因计数转交）后，这类轮次归零；`pending` 有硬上限，丢最老的轮次会落 `agent.trim`。
- ✂️ **TTS 首包静音裁剪**：对 CosyVoice 合成音频首包执行 5ms 窗口能量裁切，下行开头无效静音从 146ms 压缩至 11ms。
- 🎯 **判停窗口按句裁剪 + 尾部静音削减**：判停输入仅喂单句音频，尾部静音保留 20ms，与训练特征对齐；`出句→开轮` 从 1.9s 骤降至 2ms。
- 🌏 **中文字符判停阈值优化**：针对中文判停偏保守的特点，引入 `TURN_JUDGE_THRESHOLD_CJK=0.35`，防止短句误判未完成。
- ⏱️ **判停的等待有预算**：`②` 的等待藏在模型段后面时是免费的，模型快了以后就变成纯空等。`TURN_JUDGE_WAIT_BUDGET_MS=200`（一拍 `TURN_JUDGE_EXTEND_MS=200`）把上限封死在模型段附近。
- ⚡ **ASR 端点自控（实验中，尚未全量验证）**：支持关掉云端服务端 200ms VAD 窗，改由宿主本地在静音到点发 `commit`，再由「开轮静音门槛」挡住换气；同一份 13 轮向量上 `① 停嘴→出句` **400 → 254–302 ms**、有声拆句 1 → 0（见 [docs/QWEN-REALTIME-ASR-PROBED.md](./docs/QWEN-REALTIME-ASR-PROBED.md)）。
- 🧪 **判停器有公开基准可对账（实验中）**：在 [livekit/eot-bench](https://github.com/livekit/eot-bench) 中文子集上，本项目的判停器 AUC 0.754 / 5% 误切预算下等待 0.918 s，比「纯静音死等」的 1.100 s 省 **182 ms**（这个增量列已不作判断，见文档）。榜单的**跨模型排名待核实**（其余行是上游公开结果、口径未必一致），本文不据此排序。**真正的结论是：瓶颈不在模型而在策略**（重复询问/宽限/预算可绕过，2026-11-18 已修），详见 [docs/EOT-BENCH-RESULTS.md](./docs/EOT-BENCH-RESULTS.md) §0。

<details>
<summary><b>🔍 点击展开：真机 13 轮同向量回放原始标定记录与时序审计</b></summary>

```text
源档案 20261117-221010-<设备 IP>_46019   来源=真机 mSBC
回放命令：python bench/replay/run.py --archive 20261117-221010-<设备 IP>_46019 --turns 13

【回放标定】13 轮测试实测（单位：ms）
    轮     ① 停嘴→ASR     ② →开轮    ③ →首块      合计   ASR 识别文本
    1          386         6      726    1118   你好。
    2          358         4     1050    1412   界面呢。
    3          404         4     1267    1675   我们随便来闲聊一下。
    4          383         2     1053    1438   你看过星球大战吗？你知道吗？
    5          316         1     1373    1690   嗯，七四的复仇。
    6          377         2     1210    1589   对呀，你说说你的看法呢？
    7            —      1020      337       —   对嘛，那句。（判停正确等待后半句）
    8          397         4      573     974   台词的经典是台词是什么来着？
    9          357         2      825    1184   不对，不是那个我我占据个高地了吗？
   10          274       475      371    1120   嗯，对。
   11          352         3      656    1011   嗯，对。
   12          303         2     1195    1500   后面发生了什么？
   13          352         2      420     774   嗯，那先聊到这里吧，你挂一下。

=== 时序 / 状态审计 ===
✓ 轮次配对完整，状态转移符合白名单
✓ 插话下发 audio.stop 及时，无违规残留
```

</details>

---

## ⚙️ 配置说明

系统支持两种部署形态：**独立进程模式**与 **`dsh` (Cordis) 插件模式**。

### 1. 独立进程模式（`src/main.ts`）

| 配置分类 | 环境变量 / CLI 参数 | 默认值 | 说明与调优建议 |
|:---|:---|:---:|:---|
| **网络与鉴权** | `--listen` / `PORT` | `8766` | 监听端口 |
| | `MIAI_TOKENS` | - | 设备鉴权 Token 列表（逗号分隔；外网必配） |
| | `MIAI_TLS_KEY` / `_CERT` | - | TLS 私钥与证书路径（监听非本机时必配） |
| | `MIAI_HTTP_KEEPALIVE_MS` | `50000` | 出站 HTTP 连接的**保活上限**。`fetch` 默认 4 s，而真机两轮间隔常有 5–7 s，等于每轮重做 TLS 握手（多 130–190 ms）。**必须短于服务端的空闲超时**——服务端先关、我们恰好复用时那一次会直接失败 |
| **语音链路** | `MIAI_STT` / `--stt` | (空) | 流式识别选型：`aliyun`（现网 NLS）、`qwen-realtime`（实验）、`canned` / `noop` / `<path>`；不给则不启用流式识别 |
| | `MIAI_TTS` / `--tts` | (空) | 合成选型：`cosyvoice`、`mimo`、`silent`、`<path>` |
| | `VOICE_PAUSE_DETECT_MS` | `200` | 静音到这么久先预跑判停侧车（不等提交，纯提速） |
| | `VOICE_COMMIT_MS` | `20` | **仅 `qwen-realtime`**（其它 STT 为 `0`=关）：静音到点即发 `commit` 封段。这是「切段」不是「开轮」，可以激进。**注意实际门槛是一整个上行包**（包内尾部静音不参与计时），所以 20 与 40 的差别只在包边界上 |
| | `VOICE_OPEN_QUIET_MS` | `300` | **仅 `qwen-realtime`**：定稿到达时要求的连续静音门槛，不够就再等（防换气被当句尾） |
| | `VOICE_OPEN_QUIET_SHORT_MS` | `200` | **仅 `qwen-realtime`**：判停 p ≥ `0.8`（目前写死）时改用的短门槛 |
| **快车道** | `FAST_LANE_MODEL` | - | 轻量闲聊模型名称（如 `qwen-flash`） |
| | `FAST_LANE_TIMEOUT_MS` | `1200` | 快车道首字超时时间，超时自动转交 `dsh` |
| | `FAST_LANE_MAX_CHARS` | `14` | **形态**上限：超过就整句交给 `dsh`（这一条不看语义，只看长度） |
| | `FAST_LANE_WINDOW_CHARS` | `800` | 对话窗口的**字符**预算。每多一轮 system+history 就多几十上百 token，窗口越小首字越快；实测 800→1600 只差 <10 ms，所以默认不动 |
| | `FAST_LANE_PREFETCH` | `1` | 判停前预跑开关（`1` 开启，`0` 关闭） |
| | `FAST_LANE_SPECULATE` | `1` | 快车道与 dsh 双轨投机开关 |
| | `FAST_LANE_PARTIAL_SPECULATE` | `1` | 拿 ASR **中间结果**先起跑（定稿确认是前缀才认领） |
| | `FAST_LANE_SPEC_MIN_CHARS` | `6` | 中间结果至少几个字才起跑。只控制「发不发请求」，认领另有一条硬闸：**去全部标点后必须与定稿完全一致**。降到 2 试过，请求涨 2.5 倍、端到端 p50 没动，已退回 |
| | `FAST_LANE_HEDGE` | `2` | 并发发几份**完全相同**的请求抢首个响应头（方差全在服务端排队，实测「响应头→首 token」只差 ~1 ms）；落败的在拿到响应头前就 abort |
| | `FAST_LANE_KEEP_TURNS` | `0` | 攒满几轮就**整句交给 `dsh`**（顺便刷它的上下文）。`0`（默认）= 永不因计数转交——这条曾让每 4 轮就有 1 轮等 6–8 秒。`pending` 另有硬上限，丢最老的会落 `agent.trim` |
| | `FAST_LANE_DELEGATE` | `0` | 是否认模型自己写的 `[[DELEGATE]]` 暗号。`0` 时判暗号的闸门也一起关掉，首字不必等第二个字符 |
| **语义判停** | `TURN_JUDGE_THRESHOLD` | `0.5` | 语义说完置信度阈值 |
| | `TURN_JUDGE_THRESHOLD_CJK` | `0.35` | 针对中文短句的判停阈值（防止过早等待） |
| | `TURN_JUDGE_QUIET_MS` | `0` | 定稿后额外静默期（ms） |
| | `TURN_JUDGE_EXTEND_MS` | `200` | 判停未决时**每一拍**等多久。改小 = 更早开轮，但留给「用户接着说」的窗口更短 |
| | `TURN_JUDGE_MAX_UNSURE` | `1` | 判停未决时最多延几拍（`MAX_EXT` 是另一条上限，两条取小） |
| | `TURN_JUDGE_MAX_EXT` | `2` | 延拍次数的硬上限 |
| | `TURN_JUDGE_TRIM_MS` | `20` | 判停快照尾部保留的最大静音（ms） |
| | `TURN_JUDGE_WAIT_BUDGET_MS` | `200` | **QoS**：`②` 定稿→开轮的总等待预算，用完就收下。0 = 不设。200 约等于模型段时长（~184 ms），于是等待基本藏在模型后面 |
| | `TURN_JUDGE_SEQUENCE_BUDGET_MS` | `1200` | **QoS**：句尾像未完成的序列（数字/字母/「然后」）时的**更大预算**（不再给更多拍数）。0 = 不启用 |
| | `TURN_JUDGE_MAX_OPEN_SILENCE_MS` | `650` | **QoS 统一上限**：开轮时连续静音的天花板，任何分支都不许绕过。0 = 不设 |
| **TTS（CosyVoice）** | `COSYVOICE_PREWARM` | `1` | 定稿那一刻就把 task 开好（`run-task` → `task-started` 约 66 ms 挪进空窗）。`instruction` 模式下自动不预热——语气是开 task 时定死的 |
| | `COSYVOICE_FIRST_BATCH_CHARS` | `1` | 首批送几个字。**实测只送 1 个字时服务端不开始合成**，要等后续文本到齐才动（等 2 s 送其余 → 首包 2328 ms，等 50 ms → 371 ms），所以这一项省的只是「等第 2 个 token」 |
| | `COSYVOICE_EMOTION_MODE` | `instruction` | `prosody` 表示只用 rate/pitch 表达情绪，可以在定稿前预开 task |
| **主动开口** | `PET_PROACTIVE` | `0` | 是否开启主动开口（`1` 开启） |
| | `VOICE_HOLD_MS` | `2000` | 能量门判定静音至关门的维持时间（ms） |

### 2. `dsh` 插件模式（`driver.ts`）

作为 Cordis 插件运行时的配置项：

| 配置项 | 默认值 | 说明 |
|:---|:---:|:---|
| `port` | `8766` | 设备接入监听端口 |
| `host` | `127.0.0.1` | 绑定地址；监听非本机时强制检查 TLS 与 Auth 配置 |
| `tls.keyPath` / `certPath` | `''` | TLS 证书路径 |
| `auth.tokenFile` | `''` | 设备鉴权 Token 文件路径（通过 `npm run pair -- new` 生成） |
| `turnThreshold` | `0.5` | 语义判停置信度阈值 |
| `proactive.*` | 详见代码 | 伴生主动开口参数（闲置阈值、电量红线、深夜静音时段等） |

---

## 🛠️ 开发与测试

```bash
# 1. 运行完整单元测试套件（638 个测试）
npm test

# 2. 静态 TypeScript 类型检查
npm run typecheck

# 3. 诊断并生成会话归档分析报告
node --experimental-strip-types scripts/observe.ts <档案目录>

# 4. 状态机时序与抢占合规审计
node --experimental-strip-types scripts/fsm-trace-check.ts <档案目录>

# 5. 逐轮审计模型行为：用户说了什么 → 被问了什么 → 答了什么 → 听到多少
node --experimental-strip-types scripts/said-audit.ts <档案目录>

# 6. 标准报告：按车道 / 按判停是否等待 / 按台词类别 三张表（口径见 docs/QOS.md）
node --experimental-strip-types scripts/latency-report.ts <档案目录> --standard

# 7. 时间参数总表：从源码生成，改了旋钮要重新生成（测试会红）
python scripts/time-knobs.py --write

# 8. 生成或管理设备配对凭证
npm run pair -- new

# 9. partial 时序：投机到底能提前多少（三个覆盖口径 + 按句长分组）
python scripts/partial-timeline.py <档案目录>

# 10. 封段统计：句内静音段分布，以及 20/40/60 ms 门槛各会误封多少次
python scripts/silence-runs.py <档案目录>

# 11. TTS 首包探针：分批送达（首字/标点在不在、后续文本隔多久）对首包的影响
MODE=live ROUNDS=80 IDLE_MS=5000 node bench/latency/probe-cosyvoice-feed.mjs

# 12. 真机向量回放（自己起隔离实例，不打生产端口）
python bench/replay/run.py --archive <会话名> --turns 16
```

> [!TIP]
> 全量脚本路由表、**延迟口径归属**与档案字段的逐项定义，见 [docs/TOOLS.md](./docs/TOOLS.md)。

---

## 📁 核心目录结构

```text
dsh-pet-wearable/
├── src/
│   ├── main.ts                # 独立进程启动入口
│   ├── driver.ts              # Cordis / dsh 插件接入入口
│   ├── fronted-agent.ts       # 快车道轻量推理引擎
│   ├── utterance-assembler.ts # 语音组装与语义判停协调
│   ├── dialog-fsm.ts          # 全双工对话状态机
│   ├── providers.ts           # STT / TTS / Agent 工厂契约注入
│   ├── app/session.ts         # 话筒抢占仲裁 (Floor Arbiter)
│   └── pet/                   # 主动开口时机状态机与仿真调度
├── docs/                      # 状态机时序、架构设计、硬件协议与运维文档
├── bench/                     # 真实向量回放、延迟评测、判停基准（eot-bench 适配器、微调准备）
├── tools/                     # 设备模拟器 (fake-phone, fake-v2-device)
└── tests/                     # 覆盖完整的单元测试用例
```

---

## 📚 详细文档导航

| 领域 | 核心文档 | 内容概览 |
|:---|:---|:---|
| **QoS（先看这份）** | [QOS.md](./docs/QOS.md) | 指标定义与口径规则、六条原则、改动流程五问、测量方法检查项、在用/已否决/待定三张清单 |
| | [TIME-KNOBS.md](./docs/TIME-KNOBS.md) | 时间参数总表（**生成物**）：默认值 / 时钟 / 持有者 / 被谁遮住 / 上限 |
| **状态机与流转** | [state-machines.md](./docs/state-machines.md) | 六大核心状态机（DialogFsm、FloorArbiter 等）时序与真相表 |
| **工具与度量** | [TOOLS.md](./docs/TOOLS.md) | 观测工具矩阵、延迟口径唯一定义与排障路由表 |
| **判停基准** | [EOT-BENCH-RESULTS.md](./docs/EOT-BENCH-RESULTS.md) | 公开中文 EoT 基准上的数字、口径与**修订记录**（含被撤回的归因）；结论：瓶颈在策略不在模型 |
| **ASR / TTS 实测** | [QWEN-REALTIME-ASR-PROBED.md](./docs/QWEN-REALTIME-ASR-PROBED.md) | DashScope realtime 的端点/静音窗实测与「回执会骗人」 |
| | [ALIYUN-ASR-PROBED.md](./docs/ALIYUN-ASR-PROBED.md) | 阿里云 NLS（现网）协议与延迟实测 |
| | [MIMO-API-PROBED.md](./docs/MIMO-API-PROBED.md) | MiMo 为何出局：不支持上行流式 |
| | [STT-TTS-REALTIME-QUESTIONS.md](./docs/STT-TTS-REALTIME-QUESTIONS.md) | 选型前的调研清单（已结案） |
| **云端架构** | [CLOUD-ARCHITECTURE.md](./docs/CLOUD-ARCHITECTURE.md) | 云端核心模块分层、并发模型与接口契约 |
| **硬件协议** | [device-protocol.md](./docs/device-protocol.md) | 穿戴端线协议规范（帧结构、控制指令、上行状态帧） |
| **运维实践** | [OPERATIONS.md](./docs/OPERATIONS.md) | 生产部署指南、TLS 配置与证书轮换 |
| | [OPS-RECORD.md](./docs/OPS-RECORD.md) | 运维踩坑记录、双仓事实与排障手记 |
| **架构决策 (ADR)** | [ADR-0001: App Layer & Pet](./docs/adr/0001-app-layer-and-pet.md) | 应用层架构、话筒仲裁与主动开口机制演进 |
| | [ADR-0002: Simulator](./docs/adr/0002-virtual-time-simulator.md) | 虚拟时间模拟器设计与因果测试理念 |
| **实现报告** | [fsm-align-report.md](./docs/fsm-align-report.md) | 状态机对齐第 0–4 步逐步做了什么、卡在哪 |
| | [shared-conversation-log.md](./docs/design/shared-conversation-log.md) | 单一对话日志的设计草稿（暂不实现） |
| **设备适配** | [RAYNEO-X3-PRO.md](./docs/devices/RAYNEO-X3-PRO.md) | 雷鸟 X3 Pro 智能眼镜真机接入实践参考 |

---

## 🚫 明确边界（Out of Scope）

为了保持项目的专注度与高性能，以下内容明确**不属于**本项目的开发范畴：

1. **不做视觉/动画形象**：不开发桌面像素风组件、3D 形象或虚拟主播动画；专注底层语音、交互与意图响应。
2. **不支持单会话多设备并发**：严格遵循「一副穿戴设备绑定一个独立会话」的模型。
3. **不构建主观拟人评分体系**：拟人感以真实用户盲测体验为准，拒绝脱离场景的形式化指标。

---

## 📄 开源许可与第三方致谢

本项目采用 [MIT License](./LICENSE) 开源。

项目中引用的第三方代码及算法模型遵循其原有开源许可，详见 [THIRD-PARTY-NOTICES.md](./THIRD-PARTY-NOTICES.md)：
- `turn_judge/whisper_features.py`：BSD 2-Clause (Daily) / Apache 2.0 (Hugging Face)
- 判停模型权重：BSD 2-Clause (Pipecat / Smart Turn)
- VAD 模型：MIT License (Silero VAD)—— **可选**，`--stt aliyun` 这条路径不使用
