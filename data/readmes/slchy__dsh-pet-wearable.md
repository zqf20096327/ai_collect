# dsh-pet-wearable

<div align="center">

[![Node.js](https://img.shields.io/badge/node-%3E%3D22.18.0-brightgreen.svg)](https://nodejs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.7-blue.svg)](https://www.typescriptlang.org/)
[![Tests](https://img.shields.io/badge/tests-684%20passing-success.svg)](#开发与测试)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Status: Active](https://img.shields.io/badge/status-active%20development-orange.svg)](#)

**面向智能穿戴设备的云端全双工语音伴生 Agent（基于 `dsh` / DeepSeek Harness）**

薄端侧接入 · 快慢双轨推理 · 即时打断 · 克制的主动开口 · 硬件无关协议

[核心特性](#核心特性) • [系统架构](#系统架构) • [快速开始](#快速开始) • [性能与延迟](#性能与端到端延迟) • [配置说明](#配置说明) • [文档导航](#详细文档导航)

</div>

---

## 为什么做 dsh-pet-wearable

智能眼镜、耳机、手表受限于电池与散热，无法在端侧长期运行高算力模型；而传统语音助手依赖唤醒词和半双工轮候，打断笨重、延迟高，交互割裂。本项目将音频流处理、语义判停、快慢路由与工具调用全部收口到云端，端侧只负责透传音频与传感器帧：

| 维度 | 传统语音助手（如智能音箱 / 手机助手） | `dsh-pet-wearable` |
|:---|:---|:---|
| **交互模式** | 半双工：喊唤醒词 → 等提示音 → 说话 → 等播完 | 全双工免唤醒：能量门 + 语义判停自适应切句 |
| **打断机制** | 需等播完或重新喊唤醒词 | 即时 Barge-in：开口即下发 `audio.stop`，同步取消在途推理 |
| **响应结构** | 串行等待 2–4 s，复杂任务长时间静默 | 快慢双轨：闲聊直达（实测 p50 906–1296 ms，随时段波动）；复杂任务先播回执再给正文 |
| **存在形态** | 纯工具：不唤醒不响应 | 伴生（Pet）：结合佩戴、电量、时段与静默时长，有节制地主动开口 |
| **硬件耦合** | 深度绑定特定芯片或厂商 SDK | 线协议解耦：端侧仅搬运音视频与状态帧，接入新硬件不改核心代码 |

> [!NOTE]
> **关于命名中的 `pet`**：
> 这里的 `pet` 指的不是桌面像素动画或 3D 虚拟形象，而是行为层的**在场感与适度主动性**——全天候佩戴的设备需要低打扰、知进退，而不是随时抢戏。

---

## 核心特性

- **快慢双轨推理（Fast Lane + `dsh`）**
  - **快车道直答**：日常短句走轻量模型直接响应，真机实测端到端首字 **p50 906–1296 ms**（七场配对，n=14–39；差值与时段、台词相关，见下文基准表）。
  - **按语义而非词表委派**：本地仅拦截三类固定形态（空文本、超过 `FAST_LANE_MAX_CHARS`、含阿拉伯数字），其余统一先走快模型，可选由模型在输出流中发出 `[[DELEGATE]]` 触发转交（见 `FAST_LANE_DELEGATE`）。早期基于关键词表判路由时，「你看过吗」「为什么」这类闲聊常被误判为任务，真机 92 轮里有 25 轮白走了 `dsh`。默认 `FAST_LANE_KEEP_TURNS=0`，不按轮数强制转交（该策略曾导致每 4 轮出现 1 轮 6–8 秒长等）。
  - **深度推理与工具调用**：多步推理、事实检索与多模态任务交由 `dsh` 及子代理执行。
  - **投机并发与委派回执**：快慢双轨支持并行起跑；快车道超时或判定转交时，先下发短回执（如「我看看。」）填补静默，正文就绪后立即顶掉回执并清空下行缓冲。
- **全双工与即时打断（Full-Duplex & Barge-in）**
  - 基于上行能量门（-40 dBFS）与语义判停（TurnJudge）完成免唤醒切句。
  - 流式 ASR 捕获用户新发言（过滤纯语气词）后，立即下发 `audio.stop` 截断下行音频，同时中止在途上游推理与排队轮次。
- **情境感知的主动开口**
  - 依据佩戴状态、剩余电量、深夜时段、环境静默时长与发言间隔构建确定性时机状态机。
  - 低电量或深夜自动静默，所有触发条件均可追溯、可复现。
- **硬件无关的能力协商**
  - `src/devices/` 仅定义 6 个标准下行指令与 6 个上行事件，在 `Hello` 握手阶段动态协商能力集。
  - 缺失能力自动降级（如无摄像头则不触发视觉链路），接入新设备（如[雷鸟 X3 Pro](./docs/devices/RAYNEO-X3-PRO.md)）无需改动核心状态机。
- **零密钥本地闭环与虚拟时间仿真**
  - 内置 `canned` STT、`silent` TTS 与 `echo` Agent，无需 API Key 与真机即可跑通全链路。
  - 内置纯虚拟时间模拟器（`npm run sim`），支持随机状态空间探索与因果不变式校验，全仓 684 个测试用例覆盖核心时序路径。

---

## 系统架构

### 1. 数据流与模块分层

```text
端侧（智能眼镜 / 耳机 / 手机）              云端服务（src/）
  AudioRecord / AudioTrack  ────────►  TLS 长连接（帧协议 · 鉴权 · 心跳）
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
                           短句闲聊直答                  复杂推理 · 检索 · 多模态
                                 └─────────────┬─────────────┘
                                               ▼
                                    TTS（CosyVoice）→ PCM 流式下发
```

### 2. 双轨时序路径

```text
[用户停嘴] ──────────────┬────────────────────────────────────────►
                         ▼
               [① 停嘴→定稿 ~300ms | ② 判停收敛 ~2–26ms]
                         │
        ┌────────────────┴────────────────┐
        ▼ (快车道直达)                     ▼ (转交 dsh)
  [模型首字 ~184ms]                 [超时或委派触发]
        │                                 │
  [TTS 首包裁静音 ~350ms]            [先播短回执："我看看。"]
        │                                 │
  端侧出声（p50 ~0.9–1.05s）        [Subagent / 工具执行完成]
                                          │
                                    顶掉回执，播发正文
```

### 3. 抢占式话筒仲裁（Floor Arbiter）

话筒归属由 `AppSession.floor` 统一管理，遵循确定的抢占优先级：

| 当前占用者 | 可被谁抢占 | 说明 |
|:---|:---|:---|
| `user` | **无** | 用户优先级最高，任何状态下开口均立即抢占话筒 |
| `reply` | `user` | 正在播报正文回复，可被用户随时打断 |
| `announce` | `user`、`reflex` | 后台作业播报，不抢占正文，待正文结束且环境安静后播报 |
| `pet` | `user`、`reflex` | 主动开口，不与正文冲突，仅在静默窗口内受控触发 |
| `reflex` | **任意占用者** | 过渡性垫音或短回执，可被用户发言或正文回复随时顶掉 |

---

## 快速开始

### 环境要求

- **Node.js** >= 22.18.0
- （可选）接入真实硬件需安装 `ffmpeg`（用于 mSBC 解码）

### 1. 零密钥本地闭环

使用内置离线 Mock 跑通握手、轮次流转与音频下行：

```bash
# 安装依赖
npm install

# 启动服务端（监听 8766，离线 Mock）
node src/main.ts --listen 8766 --stt canned --tts silent --agent echo
```

在另一终端启动模拟设备推流：

```bash
node tools/fake-phone.ts --port 8766 --sbc tmp/voice.sbc
```

预期输出示例：

```text
[Main] listening on 127.0.0.1:8766 (plain)
[Device] handshake completed: protocol=v2 capabilities=[audio, wear, battery]
[Floor] turn started: #1 speaker=user
[FastLane] hit: "你好呀" -> "你好！我在呢。" (TTFT: 240ms)
[TTS] audio chunk dispatched: 3200 bytes
[Floor] turn settled: #1 duration=1080ms
```

### 2. 虚拟时间逻辑仿真

无网络、无密钥、无音频设备依赖，用于验证主动开口策略与状态机不变式：

```bash
npm run sim                          # 运行预设声明式场景
npm run sim -- --explore --runs 500  # 随机探索 500 轮，检查不变式违规
npm run sim -- --trace out/          # 导出完整时序日志（JSONL）
```

### 3. 接入真实设备与云端模型

```bash
# 1. 配置云端服务密钥（Aliyun STT / CosyVoice / LLM）
cp .env.example .env

# 2. 安装 dsh 人设 Profile 补丁（启用 dsh 时必做，自动写入 ~/.dsh/profiles/sdk/cordis.patch.yml）
npm run install-profile

# 3. 启动生产服务
node src/main.ts --listen 8766
```

---

## 性能与端到端延迟

### 延迟口径

> [!IMPORTANT]
> 本项目提及的 `p50` / `p90` **无特殊说明时均指端到端「闭嘴 → 出声」延迟**（`firstWordMs`）：从用户停嘴（能量门关闭）到穿戴端播放首个有效字音频的完整耗时。
> 拆解为三段：`① 停嘴→定稿`（ASR 收敛）+ `② 定稿→开轮`（语义判停等待）+ `③ 开轮→首块`（模型 TTFT + TTS 首包合成与下发）。

### 真机基准实测

以下为真机快车道直答（委派轮已按 `turn.end.path` 排除）实测结果。各场台词不同，**单场绝对值不可横向硬比**，仅作配置改动前后观察；`p50` 为**逐轮总耗时**的中位数，不等于三段中位数直接相加：

| 场次 | 有效轮 | **p50 (ms)** | ① 停嘴→定稿 | ② 定稿→开轮 | ③ 开轮→首块 | 判停配置 |
|:---|:---:|:---:|:---:|:---:|:---:|:---|
| `20261119-153754` | 39 | 1054 | 300 | 8 | 597 | 每拍 400 / 预算 400 |
| `20261119-160012` | 21 | 1257 | 324 | 4 | 817 | 每拍 400 / 预算 400 |
| `20261119-160921` | 21 | **920** | 295 | 25 | 567 | 每拍 **200** / 预算 **400** |
| `20261120-031505` | 17 | 991 | 300 | 26 | 643 | 每拍 200 / 预算 **200** |
| `20261121-111055` | 14 | 1283 | 344 | 3 | 874 | 每拍 200 / 预算 200 |
| `20261121-113439` | 26 | 1296 | 347 | 4 | 671 | 每拍 200 / 预算 200 |
| `20261121-145934` | 14 | **906** | 303 | 30 | 564 | 每拍 200 / 预算 200 |

> 场次名是 **UTC**；换算成北京时间要 **+8**（`20261121-113439` = 19:34 CST）。
> 时间是当前解释力最强的单变量：同一套配置下 **11:15 CST 991 / 19:10 1283 /
> 19:34 1296 / 22:59 906**。跨时段的差值不能当噪声用。

**数据解读与边界说明：**
- **配置差异**：七场配置并不统一，不能将差值直接归因为跨场抖动或台词差异。唯一同配置的一对是 `15:37` 与 `16:00`（差 203 ms）；判停总预算 `400 → 200` 从 `03:15` 起生效（`920 ms` 那场预算仍为 `400`）。
- **主要收益来源**：HTTP 连接保活每轮省去 130–190 ms 握手开销，将模型段压至 ~184 ms；判停每拍从 400 ms 收至 200 ms（`TURN_JUDGE_EXTEND_MS`），缩短了「再等一下」轮次的放行时间。
- **回放的适用边界**：同向量 7 轮回放中 `fast` 命中 5/7，但因音量链不同，回放与真机 ASR 逐字一致仅 1/7（同为 `qwen-realtime`）。回放只用来看路由分支与相对变化，绝对延迟一律以真机档案为准。
- **残余瓶颈**：
  - `①` 约 300 ms 里，**停嘴→封段（①a）实测 66–82 ms**（由上行包长量化：75 ms 包付 ~70 ms，包内尾静音不参与计时，所以 `VOICE_COMMIT_MS=20` 实际受包长约束），**封段→定稿（①b）211–293 ms** 在 ASR 那侧（见 [docs/QOS.md](./docs/QOS.md) §2.5）。
  - `③` 里模型段约 184 ms、TTS 正常首包 320–400 ms；偶发长尾集中在 TTS 侧 —— 首包 >900 ms 的轮次旧四场 **8/112**、11-21 三场 **9/60**，`tts.done` 显示文本均在 100 ms 内送完，耗时卡在 `finish-task` 后的合成阶段。
  - 另有**尚未解释**的两段瞬态：`setup_ms`（run-task→task-started）的 **65 / 335 双峰**，以及 ①b 在一场里**跳档**到 0.68–1.33 s 后自恢复。两者时间窗重叠、判据与进展见 [docs/QOS.md](./docs/QOS.md) §2.6–§2.7。

### 已落地的延迟优化

- **HTTP 连接保活拉长至 50 s**：Node `fetch` 默认 `keepAliveTimeout` 为 4 s，而真机轮间间隔 p50 达 5–7 s，导致几乎每轮重做 TLS 握手（复用 146–296 ms vs 新建 375–434 ms）。全局 dispatcher 拉长至 50 s 后，模型段从 ~300 ms 降至 ~184 ms（`MIAI_HTTP_KEEPALIVE_MS`，见 `src/http-agent.ts`）。
- **判停前预跑（Prefetch）**：ASR 定稿到达即提前发模型请求，不再干等判停静默期结束，开轮至模型首字缩减 ~220 ms。
- **中间结果投机（Partial Speculation）**：能量门关闭瞬间取最新 partial 提前请求；定稿后校验**去全部标点后完全一致**才认领，未命中则无缝回退定稿。
- **取消按轮数强制转交**：`FAST_LANE_KEEP_TURNS=0` 消除周期性 6–8 s 强制委派；`pending` 队列设硬上限，超限丢弃最旧轮次并记录 `agent.trim`。
- **TTS 首包静音裁剪**：对 CosyVoice 首包音频按 5 ms 窗口做能量裁切，首部无效静音从 146 ms 压至 11 ms。
- **判停输入按句裁剪 + 尾部静音对齐**：仅向判停器送入单句音频并保留 20 ms 尾静音以对齐训练分布，正常轮次 `②` 从 1.9 s 降至 ~2 ms；同时为中文短句引入 `TURN_JUDGE_THRESHOLD_CJK=0.35` 降低保守等待。
- **判停等待设总预算**：模型变快后，`②` 的等待不再被模型耗时完全遮蔽；`TURN_JUDGE_WAIT_BUDGET_MS=200`（单拍 `200 ms`）将等待上限锁在模型段量级。
- **宿主侧自控 ASR 端点（实验中）**：关闭云端 200 ms 服务端 VAD 窗，改为本地静音到点发 `commit`，配合开轮静音门槛防换气误切；同 13 轮向量上 `①` 从 400 ms 降至 254–302 ms，有声拆句从 1 降为 0（见 [docs/QWEN-REALTIME-ASR-PROBED.md](./docs/QWEN-REALTIME-ASR-PROBED.md)）。
- **EoT 公开基准对账（实验中）**：在 [livekit/eot-bench](https://github.com/livekit/eot-bench) 中文子集上，本判停器 AUC 0.754，5% 误切预算下平均等待 0.918 s（纯静音等待为 1.100 s，省 182 ms；跨模型榜单口径不一，本文不作横向排名）。更关键的结论是**线上瓶颈在调度策略而非模型本身**（重复询问、宽限与预算绕过问题已于 2026-11-18 修复，详见 [docs/EOT-BENCH-RESULTS.md](./docs/EOT-BENCH-RESULTS.md) §0）。

<details>
<summary><b>展开查看：真机 13 轮同向量回放原始标定记录与状态审计</b></summary>

```text
源档案 20261117-221010-<设备 IP>_46019   来源=真机 mSBC
回放命令：python bench/replay/run.py --archive 20261117-221010-<设备 IP>_46019 --turns 13

【回放标定】13 轮实测（单位：ms）
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

## 配置说明

支持**独立进程模式**（`src/main.ts`）与 **`dsh` / Cordis 插件模式**（`src/driver.ts`）。

### 1. 独立进程模式（`src/main.ts`）

| 分类 | 环境变量 / CLI 参数 | 默认值 | 说明与调优经验 |
|:---|:---|:---:|:---|
| **网络与鉴权** | `--listen` / `PORT` | `8766` | 服务监听端口 |
| | `MIAI_TOKENS` | - | 设备鉴权 Token（逗号分隔，公网部署必配） |
| | `MIAI_TLS_KEY` / `_CERT` | - | TLS 私钥与证书路径（绑定非本机地址时必配） |
| | `MIAI_HTTP_KEEPALIVE_MS` | `50000` | 出站 HTTP 保活上限（ms）。默认 `fetch` 仅 4 s，真机间隔 5–7 s 会导致每轮重做 TLS 握手（+130–190 ms）。**必须短于服务端空闲超时**，否则复用瞬间遇对端断连会直接失败 |
| **语音链路** | `MIAI_STT` / `--stt` | (空) | STT 实现：`aliyun`（现网 NLS）、`qwen-realtime`（实验）、`canned` / `noop` / `<path>`；留空不启用 |
| | `MIAI_TTS` / `--tts` | (空) | TTS 实现：`cosyvoice`、`mimo`、`silent`、`<path>` |
| | `VOICE_PAUSE_DETECT_MS` | `200` | 静音达到该时长即预跑判停侧车（不触发提交，仅提前计算） |
| | `VOICE_COMMIT_MS` | `20` | **仅 `qwen-realtime`**（其它 STT 为 `0` 关闭）：静音达标即发 `commit` 封段（只切段不开轮）。因包内尾静音不参与计时，**实际下限受上行包长量化约束**，20 与 40 仅在包边界有差异 |
| | `VOICE_OPEN_QUIET_MS` | `300` | **仅 `qwen-realtime`**：定稿到达时要求的连续静音门槛，不足则继续等待以防换气误切 |
| | `VOICE_OPEN_QUIET_SHORT_MS` | `200` | **仅 `qwen-realtime`**：判停置信度 $p \ge 0.8$（当前硬编码）时启用的短静音门槛 |
| **快车道** | `FAST_LANE_MODEL` | - | 轻量闲聊模型名（如 `qwen-flash`） |
| | `FAST_LANE_TIMEOUT_MS` | `1200` | 快车道首字超时（ms），超时后转交 `dsh` |
| | `FAST_LANE_MAX_CHARS` | `14` | 纯形态字数上限，超长直接整句交由 `dsh` |
| | `FAST_LANE_WINDOW_CHARS` | `800` | 快车道历史窗口字符预算；实测 800 → 1600 首字差异小于 10 ms，默认维持 800 |
| | `FAST_LANE_PREFETCH` | `1` | 判停前预跑开关（`1` 开 / `0` 关） |
| | `FAST_LANE_SPECULATE` | `1` | 快车道与 `dsh` 双轨投机开关 |
| | `FAST_LANE_PARTIAL_SPECULATE` | `1` | 使用 ASR 中间结果提前发起推理（去标点与定稿完全一致才认领） |
| | `FAST_LANE_SPEC_MIN_CHARS` | `6` | 中间结果起跑最小字数（仅控制是否发请求，认领仍受去标点完全一致硬约束）。曾试验降至 2 字，请求量涨 2.5 倍而 p50 无改善，已回退 |
| | `FAST_LANE_HEDGE` | `2` | 并发发出的相同请求份数，抢首个响应头（方差集中在服务端排队，响应头→首 token 实测差 ~1 ms）；落败请求在响应头前 `abort` |
| | `FAST_LANE_KEEP_TURNS` | `0` | 每攒满 N 轮整句交 `dsh` 同步上下文。`0` 表示永不按计数转交；`pending` 另有硬上限，超限裁剪最旧轮次并记 `agent.trim` |
| | `FAST_LANE_DELEGATE` | `0` | 是否识别模型输出的 `[[DELEGATE]]` 委派标记。为 `0` 时关闭标记检测闸门，首字无需等待第二个字符 |
| **语义判停** | `TURN_JUDGE_THRESHOLD` | `0.5` | 语义结束置信度阈值 |
| | `TURN_JUDGE_THRESHOLD_CJK` | `0.35` | 中文短句判停阈值（缓解中文判停偏保守） |
| | `TURN_JUDGE_QUIET_MS` | `0` | 定稿后额外静默时长（ms） |
| | `TURN_JUDGE_EXTEND_MS` | `200` | 判停未决时单拍延长时长（ms）；越小越早开轮，但留给用户续说的窗口越短 |
| | `TURN_JUDGE_MAX_UNSURE` | `1` | 判停未决最大延拍次数（与 `MAX_EXT` 取较小值） |
| | `TURN_JUDGE_MAX_EXT` | `2` | 延拍次数硬上限 |
| | `TURN_JUDGE_TRIM_MS` | `20` | 送入判停器的音频尾部保留静音上限（ms） |
| | `TURN_JUDGE_WAIT_BUDGET_MS` | `200` | **QoS 预算**：`②` 定稿→开轮总等待上限（`0` 不限）。200 ms 接近模型段耗时（~184 ms），可将等待基本藏入模型耗时 |
| | `TURN_JUDGE_SEQUENCE_BUDGET_MS` | `1200` | **QoS 预算**：句尾疑似未完序列（数字 / 字母 / 「然后」等）时的扩展总预算（`0` 关闭） |
| | `TURN_JUDGE_MAX_OPEN_SILENCE_MS` | `650` | **QoS 统一天花板**：开轮连续静音硬上限，任何分支不可绕过（`0` 不限） |
| **TTS（CosyVoice）** | `COSYVOICE_PREWARM` | `1` | 定稿即预开 task（将 `run-task → task-started` ~66 ms 移入空窗）。`instruction` 模式下因语气在建 task 时锁定，自动禁用预热 |
| | `COSYVOICE_FIRST_BATCH_CHARS` | `1` | 首批送字数。实测仅送 1 字时服务端不会起算，需等后续文本到达（间隔 2 s 首包 2328 ms，间隔 50 ms 为 371 ms），因此该项只省「等第 2 个 token」的时间 |
| | `COSYVOICE_EMOTION_MODE` | `instruction` | 情绪表达模式；设为 `prosody`（仅调 rate/pitch）时可在定稿前预开 task |
| **主动开口** | `PET_PROACTIVE` | `0` | 主动开口总开关（`1` 开启） |
| | `VOICE_HOLD_MS` | `2000` | 能量门从判定静音到完全关门的保持时间（ms） |

### 2. `dsh` 插件模式（`src/driver.ts`）

| 配置项 | 默认值 | 说明 |
|:---|:---:|:---|
| `port` | `8766` | 设备接入端口 |
| `host` | `127.0.0.1` | 监听地址；绑定非本机时强制校验 TLS 与 Auth 配置 |
| `tls.keyPath` / `certPath` | `''` | TLS 证书与私钥路径 |
| `auth.tokenFile` | `''` | 设备鉴权 Token 文件路径（可用 `npm run pair -- new` 生成） |
| `turnThreshold` | `0.5` | 语义判停置信度阈值 |
| `proactive.*` | 见源码 | 主动开口策略参数（静默阈值、低电量红线、深夜免打扰时段等） |

---

## 开发与测试

```bash
# 1. 运行全量单元测试（684 个用例）
npm test

# 2. TypeScript 静态类型检查
npm run typecheck

# 3. 会话归档综合诊断报告
node --experimental-strip-types scripts/observe.ts <档案目录>

# 4. 状态机转移与话筒抢占合规审计
node --experimental-strip-types scripts/fsm-trace-check.ts <档案目录>

# 5. 逐轮内容审计：用户原话 → 模型输入 → 模型输出 → 端侧实听
node --experimental-strip-types scripts/said-audit.ts <档案目录>

# 6. 标准延迟报告：按车道 / 判停是否等待 / 台词类别分组（口径见 docs/QOS.md）
node --experimental-strip-types scripts/latency-report.ts <档案目录> --standard

# 7. 重新生成时间参数总表（改动任何时间旋钮后必须执行，否则测试报错）
python scripts/time-knobs.py --write

# 8. 生成或管理设备配对凭证
npm run pair -- new

# 9. partial 时序分析：投机提前量统计（三口径覆盖 + 按句长分组）
python scripts/partial-timeline.py <档案目录>

# 10. 封段统计：句内静音分布及 20/40/60 ms 门槛下的误封次数
python scripts/silence-runs.py <档案目录>

# 11. TTS 首包分批送达探针（测试首字/标点与后续文本间隔对首包的影响）
MODE=live ROUNDS=80 IDLE_MS=5000 node bench/latency/probe-cosyvoice-feed.mjs

# 12. 真机向量回放（独立拉起隔离实例，不影响线上端口）
python bench/replay/run.py --archive <会话名> --turns 16
```

> [!TIP]
> 完整脚本路由表、延迟口径唯一定义及归档字段说明，参见 [docs/TOOLS.md](./docs/TOOLS.md)。

---

## 目录结构

```text
dsh-pet-wearable/
├── src/
│   ├── main.ts                # 独立进程入口
│   ├── driver.ts              # Cordis / dsh 插件入口
│   ├── fronted-agent.ts       # 快车道轻量推理引擎
│   ├── utterance-assembler.ts # 语音分段与语义判停协调
│   ├── dialog-fsm.ts          # 全双工对话状态机
│   ├── providers.ts           # STT / TTS / Agent 契约与工厂注入
│   ├── app/session.ts         # 话筒抢占仲裁（Floor Arbiter）
│   └── pet/                   # 主动开口状态机与仿真调度
├── docs/                      # 状态机规范、实测记录、协议与运维文档
├── bench/                     # 真机向量回放、延迟探针与 EoT 基准适配
├── tools/                     # 设备模拟器（fake-phone / fake-v2-device）
└── tests/                     # 单元测试套件
```

---

## 详细文档导航

| 主题 | 文档 | 说明 |
|:---|:---|:---|
| **QoS 规范（推荐首读）** | [QOS.md](./docs/QOS.md) | 指标口径、六条原则、改动五问、测量核查表及在用/否决/待定清单 |
| | [TIME-KNOBS.md](./docs/TIME-KNOBS.md) | 时间参数总表（脚本生成）：默认值、时钟源、持有者、遮蔽关系与上限 |
| **状态机** | [state-machines.md](./docs/state-machines.md) | 六大核心状态机（DialogFsm、FloorArbiter 等）时序与真值表 |
| **工具与度量** | [TOOLS.md](./docs/TOOLS.md) | 观测脚本矩阵、延迟口径唯一定义与排障路由 |
| **判停基准** | [EOT-BENCH-RESULTS.md](./docs/EOT-BENCH-RESULTS.md) | 中文 EoT 基准数据、口径与修订记录（含撤回顾因）；核心结论：瓶颈在策略不在模型 |
| **ASR / TTS 实测** | [QWEN-REALTIME-ASR-PROBED.md](./docs/QWEN-REALTIME-ASR-PROBED.md) | DashScope realtime 端点与静音窗实测（含「回执会骗人」现象） |
| | [ALIYUN-ASR-PROBED.md](./docs/ALIYUN-ASR-PROBED.md) | 阿里云 NLS（现网）协议与延迟实测 |
| | [MIMO-API-PROBED.md](./docs/MIMO-API-PROBED.md) | MiMo 淘汰记录（不支持上行流式） |
| | [STT-TTS-REALTIME-QUESTIONS.md](./docs/STT-TTS-REALTIME-QUESTIONS.md) | 选型前调研清单（已结案） |
| **系统与协议** | [CLOUD-ARCHITECTURE.md](./docs/CLOUD-ARCHITECTURE.md) | 云端模块分层、并发模型与接口契约 |
| | [device-protocol.md](./docs/device-protocol.md) | 穿戴端线协议（帧结构、控制指令与状态帧） |
| **运维** | [OPERATIONS.md](./docs/OPERATIONS.md) | 生产部署、TLS 配置与证书轮换 |
| | [OPS-RECORD.md](./docs/OPS-RECORD.md) | 运维排障手记与双仓实操记录 |
| **架构决策（ADR）** | [ADR-0001: App Layer & Pet](./docs/adr/0001-app-layer-and-pet.md) | 应用层分层、话筒仲裁与主动开口演进 |
| | [ADR-0002: Simulator](./docs/adr/0002-virtual-time-simulator.md) | 虚拟时间模拟器与因果不变式测试设计 |
| **实现与草稿** | [fsm-align-report.md](./docs/fsm-align-report.md) | 状态机对齐第 0–4 步推进记录与卡点 |
| | [shared-conversation-log.md](./docs/design/shared-conversation-log.md) | 单一对话日志设计草稿（暂缓实现） |
| **硬件适配** | [RAYNEO-X3-PRO.md](./docs/devices/RAYNEO-X3-PRO.md) | 雷鸟 X3 Pro 真机接入参考 |

---

## 边界说明（Out of Scope）

以下方向明确不在本项目范围内：

1. **不做视觉 / 动画形象**：不开发桌面宠物 UI、3D 建模或虚拟主播渲染，专注底层语音链路与交互状态机。
2. **不支持单会话多设备并发**：严格维持「单副穿戴设备 ↔ 独立会话」的一对一模型。
3. **不建主观拟人评分体系**：交互质感以真实场景盲测为准，不做脱离语境的形式化打分。

---

## 开源许可与第三方致谢

本项目采用 [MIT License](./LICENSE) 开源。第三方代码与模型权重沿用各自原许可，详见 [THIRD-PARTY-NOTICES.md](./THIRD-PARTY-NOTICES.md)：

- `turn_judge/whisper_features.py`：BSD 2-Clause (Daily) / Apache 2.0 (Hugging Face)
- 判停模型权重：BSD 2-Clause (Pipecat / Smart Turn)
- VAD 模型：MIT License (Silero VAD)——可选依赖，`--stt aliyun` 路径不启用