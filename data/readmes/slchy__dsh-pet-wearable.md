# dsh-pet-wearable

<div align="center">

[![Node.js](https://img.shields.io/badge/node-%3E%3D22.18.0-brightgreen.svg)](https://nodejs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.7-blue.svg)](https://www.typescriptlang.org/)
[![Tests](https://img.shields.io/badge/tests-1240%20passing-success.svg)](#开发与验证)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

**面向智能穿戴设备的云端全双工语音伴生 Agent（基于 `dsh` / DeepSeek Harness）**

[架构](#架构) • [快速开始](#快速开始) • [实测延迟](#实测延迟) • [核心配置](#核心配置) • [开发与验证](#开发与验证) • [文档](#核心文档)

</div>

---

智能眼镜、耳机等穿戴设备受限于功耗与算力，端侧只适合透传音视频和传感器事件。本项目将能量门、语义判停、实时对话与工具执行全部收口到云端，提供免唤醒全双工交互、即时打断（Barge-in），以及结合佩戴、电量与静默时长的克制主动开口（`pet` 指行为层的在场感，不做桌面动画或 3D 形象）。

## 核心特性

- **两条互斥语音主管道（`VOICE_PIPELINE=live | cascade`）**：进程启动期显式二选一，会话内绝不混跑。**Pure Live** 以 Omni 为唯一前台嗓子、通过 `BackgroundTaskBus` 异步调度无头 `dsh`；**Pure Cascade** 走 `ASR → 判停 → CascadeAgent（快模型/投机 + dsh）→ CosyVoice 流式`。
- **统一单泵与确定性内核**：`TurnRunner` 仅消费 `FastVoiceEngine.respond()` 事件流；相位、打断与结算唯一归口纯函数 [kernel.ts](./src/kernel.ts)（因果序号 `commitSeq` / `{no, gen}` + 媒体时间尺子），所有副作用经 `KernelRuntime.dispatchAndApply()` 唯一执行。
- **全双工即时打断与话筒仲裁**：能量门 + TurnJudge 判停免唤醒切句；用户开口立刻下发 `audio.stop` 并抢占话筒（`user > reply > announce / pet > reflex`）。
- **硬件无关线协议**：`src/devices/` 仅定义 6 个下行指令与 6 个上行事件，握手期按能力集动态降级，接入新设备（如[雷鸟 X3 Pro](./docs/devices/RAYNEO-X3-PRO.md)）不改核心状态机。
- **零密钥本地闭环与虚拟时间仿真**：内置 `canned / silent / echo` 离线桩、`npm run sim` 纯虚拟时间模拟器、330 转移穷尽状态验证与 1240 项运行时测试（`npm run test:all` 共 1267）。

---

## 架构

```text
端侧（眼镜 / 耳机 / 手机）                     云端（单进程，一条主管道）
  PCM / mSBC · 拍照 · 佩戴 · 电量 ───TLS───► 共享底座
                                              · devices/primitives（v1/v2 能力协商）
                                              · UplinkPipeline（能量门 voiced / silenceMs）
                                              · kernel.ts + causal.ts（纯 step / 因果屏障）
                                              · AppSession · FloorArbiter · pet/brain
                                              · dsh 后端（工具 / subagent / 后台 job / 记忆）
                                                           │
                                        VOICE_PIPELINE = live | cascade
                                           ┌───────────────┴───────────────┐
                                           ▼                               ▼
                                     【Pure Live】                   【Pure Cascade】
                              OmniShadow (20ms seal 抢跑)      ASR (150ms 封段) → UtteranceAssembler
                                           │                               │
                              LiveOrchestrator + LiveEngine    CascadeAgent (FastLlm + 投机 / dsh)
                              唯一前台 · 24 kHz PCM 直出       routeTurn(live:'off') → CascadeEngine
                                           │                               │
                              BackgroundTaskBus 异步派单       CosyVoice 流式 TTS（失败回落整段）
                              (tool_call/early_rule/image/记忆)            │
                                           ▼                               ▼
                                 无头 dsh → FloorArbiter              PCM 下行
                                 安静窗 speakFromText() 同嗓汇报
                                 （精确数字/长文走逐字 TTS + 静默回注）
                                           └───────────────┬───────────────┘
                                                           ▼
                              TurnRunner 单泵（消费 FastVoiceEngine.respond()）
                                  └──► KernelRuntime.dispatchAndApply() → KernelPorts
```

**运行形态**：独立进程 [src/main.ts](./src/main.ts)（生产形态）与 Web 插件 [packages/dsh-voice-web](./packages/dsh-voice-web/README.md)（同步仓根 `src/`）均直接可用；[src/driver.ts](./src/driver.ts) 目前仅为 0.0.1 dsh 插件配置骨架，尚未接语音栈。

---

## 快速开始

环境要求：**Node.js >= 22.18.0**（接入真实硬件 mSBC 上行需安装 `ffmpeg`）。

### 1. 零密钥本地闭环

```bash
npm install

# 终端 1：离线 Mock 服务端
node src/main.ts --listen 8766 --stt canned --tts silent --agent echo

# 终端 2：模拟设备推流
node tools/fake-phone.ts --port 8766 --sbc tmp/voice.sbc
```

### 2. 纯虚拟时间仿真（无网络 / 无密钥）

```bash
npm run sim                          # 40 个预设声明式场景
npm run sim -- --explore --runs 500  # 随机状态探索 + 不变量检查
```

### 3. 生产启动

```bash
cp .env.example .env
npm run install-profile              # 写入 ~/.dsh/profiles/sdk/cordis.patch.yml

# Pure Live（Omni 单前台 + dsh 纯异步后台）
VOICE_PIPELINE=live node src/main.ts --listen 8766 --stt qwen-realtime --tts cosyvoice --agent dsh --dsh-sdk

# Pure Cascade（ASR + 级联快车道/dsh + CosyVoice 流式）
VOICE_PIPELINE=cascade node src/main.ts --listen 8766 --stt qwen-realtime --tts cosyvoice --agent dsh --dsh-sdk
```

---

## 实测延迟

> 本仓裸说 `p50` / `p90` **一律指端到端「闭嘴 → 出声」**（`firstWordMs` = `① 停嘴→定稿` + `② 判停` + `③ 模型与合成首块`）。

| 管道 / 轮次类型 | 真机实测表现 | 说明 |
|:---|:---|:---|
| **Pure Live（Omni 直出）** | p50 **716–776 ms** / p90 **758–932 ms** | 同场较级联省 p50 164–200 ms、p90 527–951 ms（详见 [OMNI-LANE.md](./docs/OMNI-LANE.md)） |
| **Pure Cascade（快车道直答）** | p50 **906–1296 ms** / p90 **1208–2619 ms** | 受晚高峰与 TTS 首包长尾影响（详见 [QOS.md](./docs/QOS.md)） |
| **工具 / 委派轮（dsh）** | Live 同轮垫话 ~650 ms 出声，后台异步汇报 | Cascade 走短回执后接正文；精确数字/端口/长文自动走逐字朗读 |

---

## 核心配置

完整 64 项时间旋钮见 [docs/TIME-KNOBS.md](./docs/TIME-KNOBS.md)，部署与 TLS 运维细节见 [docs/OPERATIONS.md](./docs/OPERATIONS.md)。

| 环境变量 / 参数 | 默认值 | 说明 |
|:---|:---:|:---|
| `VOICE_PIPELINE` | （未设则推断） | `live` 或 `cascade`（显式值优先，非法值启动即拒；未设时 `OMNI_SHADOW=1` 且 `OMNI_ANSWER!=off` 推断为 `live`） |
| `MIAI_STT` / `--stt` | `(空)` | `qwen-realtime`（`live` 必选）/ `aliyun` / `canned` / `noop` |
| `MIAI_TTS` / `--tts` | `(空)` | `cosyvoice`（线上默认）/ `omni`（单音色逐字朗读）/ `silent` |
| `OMNI_API_KEY` / `DASHSCOPE_API_KEY` | - | `live` 必配；`cascade` 下配合 `OMNI_SHADOW=1` + `OMNI_ANSWER=off` 可挂只读测速探针 |
| `FAST_LANE_API_KEY` / `FAST_LANE_MODEL` | - / `qwen-flash` | 仅 `cascade` 生效；`live` 不加载 `FastLlmClient` |
| `FAST_LANE_SPECULATE` / `FAST_LANE_DELEGATE` | `1` / `0` | 仅 `cascade`：快慢双发投机开关 / `[[DELEGATE]]` 委派开关 |
| `MIAI_TOKENS` / `MIAI_TLS_KEY` / `MIAI_TLS_CERT` | - | 绑定非本机地址时强制要求鉴权 Token 与 TLS 证书 |
| `PET_PROACTIVE` | `0` | 设 `1` 开启情境感知主动开口 |

---

## 开发与验证

```bash
npm test                                          # 云端运行时测试（1240），与部署自检 100% 对齐
npm run test:bench                                # bench/eval 与 bench/replay（23）
npm run test:web                                  # packages/dsh-voice-web（4）
npm run test:all                                  # 全仓：1240 根 + 23 bench + 4 web = 1267
npm run typecheck                                 # TypeScript 严格检查
npm run sim                                       # 40 场景虚拟时间仿真
node --experimental-strip-types tests/fsm-verify.ts  # DialogFsm 穷尽状态验证（330 转移）
npm run mutate                                    # 定向变异检查（单独执行，勿与 npm test 并行）
python scripts/time-knobs.py --write              # 修改时间参数后重新生成 TIME-KNOBS.md
node scripts/observe.ts <档案目录>                # 会话综合诊断（分段 / 审计 / dsh 对齐）
node scripts/probe-omni-inject-speak.mjs          # 真 DashScope 后台同嗓汇报协议探针
```

完整工具矩阵与回放脚本见 [docs/TOOLS.md](./docs/TOOLS.md)。

---

## 目录速览

```text
├── src/
│   ├── main.ts · voice-session.ts · pipeline-mode.ts    # 启动装配、连接编排、管道切换
│   ├── kernel.ts · kernel-runtime.ts · causal.ts        # 确定性控制内核（纯 step + 因果时间）
│   ├── turn-runner.ts · turn-router.ts · session-core.ts# 统一单泵、路由、会话决策
│   ├── pipelines/                                       # live-orchestrator.ts / cascade-agent.ts
│   ├── engines/                                         # live / cascade / adapter（FastVoiceEngine）
│   ├── background-task-bus.ts · omni-shadow.ts          # 异步后台总线与实时音频车道
│   ├── app/ · devices/ · pet/                           # 应用层话筒仲裁、v1/v2 协议、宠物脑与仿真
├── packages/dsh-voice-web/                              # 浏览器 Web 插件与前端 demo
├── scripts/ · bench/ · tools/                           # 观测归因、回放探针、设备模拟器；bench/eval/ 为 55 轮离线 TTS 准确率与延迟护栏
├── docs/ · tests/                                       # 架构/QoS/ADR 文档与测试套件
```

---

## 核心文档

| 主题 | 文档 | 内容 |
|:---|:---|:---|
| **架构与决策** | [CLOUD-ARCHITECTURE.md](./docs/CLOUD-ARCHITECTURE.md) | 模块分层、单向依赖图与并发模型 |
| | [ADR-0003](./docs/adr/0003-deterministic-kernel.md) · [ADR-0004](./docs/adr/0004-flattened-pipelines.md) | 确定性内核（三把尺子）与双管道拍扁决策 |
| **状态机** | [state-machines.md](./docs/state-machines.md) | 对话、话筒、后台总线与空窗播报状态转移真值表 |
| **QoS 与实时车道** | [QOS.md](./docs/QOS.md) · [TIME-KNOBS.md](./docs/TIME-KNOBS.md) | 延迟口径、六条原则、四层回归闸门与 64 项时间旋钮 |
| | [OMNI-LANE.md](./docs/OMNI-LANE.md) | Omni 音频车道协议实测、延迟账与排障手册 |
| **协议与运维** | [device-protocol.md](./docs/device-protocol.md) · [OPERATIONS.md](./docs/OPERATIONS.md) | 穿戴端线协议、生产部署与证书轮换 |
| **工具索引** | [TOOLS.md](./docs/TOOLS.md) | 观测、归因、回放与变异检查脚本手册 |

---

## License

基于 [MIT License](./LICENSE) 开源；第三方模型与组件许可见 [THIRD-PARTY-NOTICES.md](./THIRD-PARTY-NOTICES.md)。
