# dsh-pet-wearable

<div align="center">

[![CI](https://github.com/slchy/dsh-pet-wearable/actions/workflows/ci.yml/badge.svg)](https://github.com/slchy/dsh-pet-wearable/actions/workflows/ci.yml)
[![npm: dsh-voice-web](https://img.shields.io/npm/v/dsh-voice-web.svg?label=dsh-voice-web)](https://www.npmjs.com/package/dsh-voice-web)
[![Node.js](https://img.shields.io/badge/node-%3E%3D22.18.0-brightgreen.svg)](https://nodejs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.7-blue.svg)](https://www.typescriptlang.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/slchy/dsh-pet-wearable/blob/main/LICENSE)

**面向智能穿戴设备的云端全双工语音伴生 Agent（基于 `dsh` / DeepSeek Harness）**

[架构](#架构) • [快速开始](#快速开始) • [实测延迟](#实测延迟) • [核心配置](#核心配置) • [开发与验证](#开发与验证) • [文档](#核心文档)

</div>

---

> **选包提示（npm 用户）**：
> - **要在 `dsh web` / Desktop 即插即用语音桌宠**：请直接安装 [`dsh-voice-web`](https://www.npmjs.com/package/dsh-voice-web)（`dsh plugin --profile web add dsh-voice-web`）。
> - **要部署穿戴端云端独立服务**：请从 [GitHub 仓库](https://github.com/slchy/dsh-pet-wearable) 或 [GitHub Releases](https://github.com/slchy/dsh-pet-wearable/releases) 拉取代码与部署包运行；`dsh-pet-wearable` 的 npm 包当前仅作包名保留与开发参考，不作为即插即用插件。

智能眼镜、耳机等穿戴设备受限于功耗与算力，端侧只适合透传音视频和传感器事件。本项目把人声检测、声学判停（TurnJudge：进程内 ONNX 的 Smart Turn v3.2，文本语义补判为可选）、实时对话与工具执行收口到云端，提供免唤醒全双工交互、即时打断（Barge-in），以及结合佩戴、电量与静默时长的克制主动开口。`src/pet/` 是穿戴侧的在场与主动开口；桌面立绘、拖拽和气泡在 Web 插件 [`packages/dsh-voice-web`](https://github.com/slchy/dsh-pet-wearable/blob/main/packages/dsh-voice-web/README.md)，不进穿戴状态机。

## 核心特性

- **两条互斥语音主管道（`VOICE_PIPELINE=live | cascade`）**：进程启动期显式二选一，会话内绝不混跑。**Pure Live** 以 Omni 为唯一前台嗓子，前台轮次与后台事实只经 [`live-session-store.ts`](https://github.com/slchy/dsh-pet-wearable/blob/main/src/pipelines/live-session-store.ts) 投影成单槽 `updateDynamicContext`，再由 `BackgroundTaskBus` 异步调度无头 `dsh`；**Pure Cascade** 走 `ASR → 判停 → CascadeAgent（快模型/投机 + dsh）→ CosyVoice 流式`。
- **统一单泵与确定性内核**：`TurnRunner` 仅消费 `FastVoiceEngine.respond()` 事件流；相位、打断与结算唯一归口纯函数 [kernel.ts](https://github.com/slchy/dsh-pet-wearable/blob/main/src/kernel.ts)（因果序号 `commitSeq` / `{no, gen}` + 媒体时间尺子），所有副作用经 `KernelRuntime.dispatchAndApply()` 唯一执行。
- **全双工即时打断与话筒仲裁**：Silero v5 神经 VAD（缺模型或 `VOICE_VAD=energy|0|off|false` 时自动退回能量门）+ TurnJudge（进程内 ONNX）声学判停免唤醒切句，文本语义补判（END 标签）可选；用户开口立刻下发 `audio.stop` 并抢占话筒（`user > reply > announce / pet > reflex`）。
- **硬件无关线协议**：`src/devices/` 仅定义 6 个下行指令与 6 个上行事件，握手期按能力集动态降级，接入新设备（如[雷鸟 X3 Pro](https://github.com/slchy/dsh-pet-wearable/blob/main/docs/devices/RAYNEO-X3-PRO.md)）不改核心状态机。
- **零密钥本地闭环与虚拟时间仿真**：内置 `canned / silent / echo` 离线桩、`npm run sim` 纯虚拟时间模拟器、330 转移穷尽状态验证。当前 `npm run test:all` 为 **1715**（根 1586 含契约套件 + bench 24 + web 105）。

---

## 架构

```text
端侧（眼镜 / 耳机 / 手机）                     云端（单进程，一条主管道）
  PCM / mSBC · 拍照 · 佩戴 · 电量 ───TLS───► 共享底座
                                              · devices/primitives（v1/v2 能力协商）
                                              · UplinkPipeline（Silero v5 32 ms 帧，或能量门）
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
                              LiveOrchestrator + live-session-store CascadeAgent (FastLlm + 投机 / dsh)
                              唯一前台 · 24 kHz PCM 直出       routeTurn(live:'off') → CascadeEngine
                                           │                               │
                              BackgroundTaskBus 异步派单       CosyVoice 流式 TTS（失败回落整段）
                              (tool_call/early_rule/image/记忆)            │
                                           ▼                               ▼
                                 无头 dsh → FloorArbiter              PCM 下行
                                 安静窗 speakFromText() 同嗓汇报
                                 （精确数字/长文走逐字 TTS，结论进单槽快照）
                                           └───────────────┬───────────────┘
                                                           ▼
                              TurnRunner 单泵（消费 FastVoiceEngine.respond()）
                                  └──► KernelRuntime.dispatchAndApply() → KernelPorts
```

**运行形态**：独立进程 [src/main.ts](https://github.com/slchy/dsh-pet-wearable/blob/main/src/main.ts) 是穿戴/服务端生产入口。Web 插件 [packages/dsh-voice-web](https://github.com/slchy/dsh-pet-wearable/blob/main/packages/dsh-voice-web/README.md) 已作为即插即用包发布至 npm（`dsh plugin --profile web add dsh-voice-web`），其 `src/driver.ts` 把同一套语音栈挂进 dsh 宿主（`/dsh-voice/*` 与 `/dsh-voice/ws`、进程内 `InProcessDshAgent`、前端三档语音配置面板与程序合成动态音效、未设 `MIAI_ARCHIVE_DIR` 时档案落 `~/.voice-agent/archives`）。包内 `src/voice/` 由 `scripts/sync-voice.mjs` 从仓根 `src/` 生成，不进 git。仓根 [src/driver.ts](https://github.com/slchy/dsh-pet-wearable/blob/main/src/driver.ts) 仍是 0.0.1 配置骨架，不建监听。

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
| **Pure Live（Omni 直出）** | p50 **716–776 ms** / p90 **758–932 ms** | 同场较级联省 p50 164–200 ms、p90 527–951 ms（详见 [OMNI-LANE.md](https://github.com/slchy/dsh-pet-wearable/blob/main/docs/OMNI-LANE.md)） |
| **Pure Cascade（快车道直答）** | p50 **906–1296 ms** / p90 **1208–2619 ms** | 受晚高峰与 TTS 首包长尾影响（详见 [QOS.md](https://github.com/slchy/dsh-pet-wearable/blob/main/docs/QOS.md)） |
| **工具 / 委派轮（dsh）** | Live 同轮垫话 ~650 ms 出声，后台异步汇报 | Cascade 走短回执后接正文；精确数字/端口/长文自动走逐字朗读 |

---

## 核心配置

完整 72 项时间旋钮见 [docs/TIME-KNOBS.md](https://github.com/slchy/dsh-pet-wearable/blob/main/docs/TIME-KNOBS.md)（`scripts/time-knobs.py` 守 17 条不变量），部署与 TLS 运维细节见 [docs/OPERATIONS.md](https://github.com/slchy/dsh-pet-wearable/blob/main/docs/OPERATIONS.md)。

> **可选 ONNX 模型放哪**（`silero_vad.onnx` / `smart-turn-v3.2-cpu.onnx`）：
> - 默认查找 `models/` 与 `~/.voice-agent/models/`（可用 `VOICE_MODELS_DIR` / `VOICE_VAD_MODEL` / `TURN_JUDGE_MODEL` 覆盖）；
> - 首次启动未找到时自动从 [GitHub Releases](https://github.com/slchy/dsh-pet-wearable/releases/latest) / 上游镜像下载并校验 SHA-256（设 `VOICE_AUTO_DOWNLOAD_MODELS=0` 关闭）；
> - 离线环境可直接从 [GitHub Releases](https://github.com/slchy/dsh-pet-wearable/releases/latest) 手动下载两个 `.onnx` 附件放入上述目录，缺模型自动降级不阻断启动。

| 环境变量 / 参数 | 默认值 | 说明 |
|:---|:---:|:---|
| `VOICE_PIPELINE` | （未设则推断） | `live` 或 `cascade`（显式值优先，非法值启动即拒；未设时 `OMNI_SHADOW=1` 且 `OMNI_ANSWER!=off` 推断为 `live`） |
| `VOICE_VAD` | `auto` | `energy` / `0` / `off` / `false` 关闭神经 VAD。缺 `models/silero_vad.onnx`、加载失败同样退回能量门，不阻断启动。模型路径用 `VOICE_VAD_MODEL` |
| `TURN_JUDGE` | `auto` | 声学判停（Smart Turn v3.2，**进程内 ONNX**）。`0` / `off` / `false` 关闭；缺 `models/smart-turn-v3.2-cpu.onnx` 或加载失败退回固定合并窗口。模型路径用 `TURN_JUDGE_MODEL`（兼容旧名 `SMART_TURN_MODEL`），**不需要 Python** |
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
npm test                                          # 云端运行时与契约测试（1586，含 tests/contracts/*.test.ts）
npm run test:bench                                # bench/eval 与 bench/replay（24）
npm run test:web                                  # packages/dsh-voice-web（105）
npm run test:all                                  # 全仓：1586 根 + 24 bench + 105 web = 1715
npm run typecheck                                 # TypeScript 严格检查
npm run sim                                       # 40 场景虚拟时间仿真
node --experimental-strip-types tests/fsm-verify.ts  # DialogFsm 穷尽状态验证（330 转移）
npm run verify:formal                             # 形式验证入口：DialogFsm + 回话词穷尽检查
npm run verify:secrets                            # 公开仓防泄漏扫描（禁入路径 + 高置信度密钥/公网 IPv4）
npm run verify:pack                               # 两个包的 npm pack --dry-run（发包内容体检）
npm run verify:release                            # 真实双包构建 + 清单校验 + 净室 npm install 冒烟
npm run version:bump -- <x.y.z>                   # 同步推进根包、web 包与两份 lockfile 版本号
npm run mutate                                    # 定向变异检查（单独执行，勿与 npm test 并行）
python scripts/time-knobs.py --write              # 修改时间参数后重新生成 TIME-KNOBS.md
node scripts/observe.ts <档案目录>                # 会话综合诊断（分段 / 审计 / dsh 对齐）
node scripts/probe-omni-inject-speak.mjs          # 真 DashScope 后台同嗓汇报协议探针
```

完整工具矩阵与回放脚本见 [docs/TOOLS.md](https://github.com/slchy/dsh-pet-wearable/blob/main/docs/TOOLS.md)。

### 持续集成与持续交付（CI / CD）

`.github/workflows/` 下共有四个工作流：

- `ci.yml`：`guards`（防泄漏扫描、两端 typecheck、时间参数不变量、形式验证、变异检查）与 `test-matrix`（Linux Node 22/24 + Windows Node 24 跑 `npm run test:all` 与 `verify:pack`）。
- `model-parity.yml`：只在 VAD / 判停 / 特征相关文件变动时拉取两个 ONNX 模型，按 SHA256 校验后跑真模型单测，并断言 `skipped 0`、`fail 0`（防止静默跳过假绿）。
- `release.yml`：推送 `vX.Y.Z` tag 或手动 `dry_run` 时执行全量闸门、净室打包冒烟、自动以 OIDC Trusted Publishing（或 `NPM_TOKEN`）发布 `dsh-voice-web` 至 npm、创建 GitHub Release 并附双包与 `SHA256SUMS.txt`，随后调用 `deploy.yml`。
- `deploy.yml`：将干净服务端部署包通过严格 `known_hosts` SSH 上传至生产主机，由 `scripts/remote-deploy.sh` 完成 `releases/<id> + shared/ + current` 原子切换、探活与失败自动回滚（完整配置见 [docs/CD.md](https://github.com/slchy/dsh-pet-wearable/blob/main/docs/CD.md)）。

---

## 目录速览

```text
├── src/                                                 # 仓根 *.ts 共 142 个
│   ├── main.ts · pipeline-mode.ts · vad.ts              # CLI 装配、管道切换、共享 SileroVadModel
│   ├── voice-session.ts · omni-shadow.ts · session.ts   # 薄再导出；实现在 voice/ · omni/ · session/
│   ├── kernel.ts · kernel-runtime.ts · causal.ts        # 确定性控制内核（纯 step + 因果时间）
│   ├── turn-runner.ts · turn-router.ts · session-core.ts# 统一单泵、路由、会话决策
│   ├── voice/          (8)                              # VoiceConnection、握手、ASR 前端、开麦相位
│   ├── omni/           (7)                              # protocol / shadow / control-plane / socket / …
│   ├── session/        (9)                              # dsh 传输、轮次机、headless、侧通道
│   ├── pipelines/      (5)                              # live-orchestrator、live-session-store、entity-divergence、cascade
│   ├── engines/        (5)                              # live / cascade / adapter（FastVoiceEngine）
│   ├── runtime/        (8)                              # 装配、provider 工厂、vad / turn-judge bootstrap
│   ├── assembler/      (2) · app/ (4) · devices/ (5)    # 语义闸与音频窗、应用层、v1/v2 协议
│   ├── pet/                                             # 穿戴侧主动开口、brain 与虚拟时间仿真
│   └── background-task-bus.ts · uplink-pipeline.ts      # 后台总线；32 ms 帧对齐的上行
├── packages/dsh-voice-web/                              # 桌宠插件：host-* 安全边界与 WS 桥，browser/pet-* 立绘
│   └── src/voice/                                       # sync-voice.mjs 生成，不进 git
├── scripts/ · bench/ · tools/                           # 观测归因、回放探针、设备模拟器；bench/eval/ 为 55 轮离线护栏
├── docs/ · tests/                                       # 架构/QoS/ADR；根 tests/*.test.ts 共 128 个文件
```

---

## 核心文档

| 主题 | 文档 | 内容 |
|:---|:---|:---|
| **架构与决策** | [CLOUD-ARCHITECTURE.md](https://github.com/slchy/dsh-pet-wearable/blob/main/docs/CLOUD-ARCHITECTURE.md) | 模块分层、单向依赖图与并发模型 |
| | [ADR-0003](https://github.com/slchy/dsh-pet-wearable/blob/main/docs/adr/0003-deterministic-kernel.md) · [ADR-0004](https://github.com/slchy/dsh-pet-wearable/blob/main/docs/adr/0004-flattened-pipelines.md) | 确定性内核（三把尺子）与双管道拍扁决策 |
| **状态机** | [state-machines.md](https://github.com/slchy/dsh-pet-wearable/blob/main/docs/state-machines.md) | 对话、话筒、后台总线与空窗播报状态转移真值表 |
| **QoS 与实时车道** | [QOS.md](https://github.com/slchy/dsh-pet-wearable/blob/main/docs/QOS.md) · [TIME-KNOBS.md](https://github.com/slchy/dsh-pet-wearable/blob/main/docs/TIME-KNOBS.md) | 延迟口径、六条原则、四层回归闸门与 72 项时间旋钮 |
| | [OMNI-LANE.md](https://github.com/slchy/dsh-pet-wearable/blob/main/docs/OMNI-LANE.md) | Omni 音频车道协议实测、延迟账与排障手册 |
| **协议与运维** | [device-protocol.md](https://github.com/slchy/dsh-pet-wearable/blob/main/docs/device-protocol.md) · [OPERATIONS.md](https://github.com/slchy/dsh-pet-wearable/blob/main/docs/OPERATIONS.md) · [CD.md](https://github.com/slchy/dsh-pet-wearable/blob/main/docs/CD.md) | 穿戴端线协议、生产部署、证书轮换与自动发版 CD 手册 |
| **工具索引** | [TOOLS.md](https://github.com/slchy/dsh-pet-wearable/blob/main/docs/TOOLS.md) | 观测、归因、回放与变异检查脚本手册 |

---

## License

基于 [MIT License](https://github.com/slchy/dsh-pet-wearable/blob/main/LICENSE) 开源；第三方模型与组件许可见 [THIRD-PARTY-NOTICES.md](https://github.com/slchy/dsh-pet-wearable/blob/main/THIRD-PARTY-NOTICES.md)。
