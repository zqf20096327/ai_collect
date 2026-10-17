# Gimbal-AI-Assistant

[![Platform](https://img.shields.io/badge/Platform-RK3588%20%7C%20STM32-blue)](https://www.rock-chips.com/)
![Language](https://img.shields.io/badge/Language-Python%20%7C%20C-green)
[![License](https://img.shields.io/badge/License-MIT-orange)](LICENSE)

**一个能感知、能交流、能行动的本地桌面智能体。**

项目以二自由度云台为当前物理载体：RK3588 负责视觉、语音、本地语义与对话，STM32 负责实时动作控制，让智能体能够离线感知用户、理解指令并作出物理响应。

**当前版本：v5.1**

## 核心能力

| 模块 | 能力 |
|---|---|
| 视觉 | RetinaFace / Haar 人脸检测、目标跟踪与主动扫描 |
| 语音 | SenseVoice + Silero VAD 离线识别、唤醒词和本地命令解析 |
| 对话 | RKLLM 上运行 Qwen2，Qwen1.5 可兼容回滚 |
| 控制 | STM32 + FreeRTOS 执行 25 Hz PID/PWM 实时控制 |
| 工程 | NPU 调度、TTS 隔离、摄像头/串口重连和安全保持 |

稳定控制链与实验功能彼此隔离：

- 常用语音控制走“离线 ASR → 本地受控规则 → 动作队列”，不依赖 LLM。
- 设备状态回答来自本地运行时快照。
- Qwen2 自由对话和 RKLLM `semantic_only` 属于实验或开发路径。

## 快速开始

目标环境为 Orange Pi 5 Plus / RK3588、STM32F103VET6 和 Python 3.9。首次运行前请完成[硬件接线](docs/hardware_setup.md)、[Orange Pi 部署](docs/deployment_orangepi.md)和[模型准备](docs/model_assets.md)。

```bash
git clone https://github.com/Z-Teddy/Gimbal-AI-Assistant.git
cd Gimbal-AI-Assistant/Software_RK3588

pip install -r requirements.txt
bash scripts/find_devices.sh
bash scripts/run_voice.sh
```

默认入口使用离线语音控制稳定路径。常用运行模式：

| 配置 | 用途 | 发布级别 |
|---|---|---|
| `runtime_tracking.yaml` | 纯视觉跟踪 | 稳定 |
| `runtime_voice.yaml` | 本地语音控制与状态问答 | 稳定、推荐 |
| `runtime_voice_qwen15.yaml` | Qwen1.5 兼容验证 | 回滚验证 |
| `runtime_voice_dialog.yaml` | Qwen2 唤醒对话 + TTS | 实验 |
| `runtime_voice_dialog_qwen15.yaml` | Qwen1.5 对话兼容 | 实验 |
| `runtime_voice_rkllm_dev.yaml` | RKLLM 独立语义调试 | 开发 |

```bash
# 纯视觉
python main.py --gui --config configs/runtime_tracking.yaml

# Qwen2 实验性对话
RUN_CONFIG=configs/runtime_voice_dialog.yaml bash scripts/run_voice.sh

# 无界面运行；也可通过 --config 显式指定配置
RUN_CONFIG=configs/runtime_voice.yaml bash scripts/run_headless.sh
```

GUI 按 `q` 退出，Headless 使用 `Ctrl+C`。

## 系统概览

```text
Camera ─> RetinaFace ─> Main Loop ─> Serial ─> STM32 ─> PID/PWM ─> Servo
Mic ─> VAD/ASR ─> InteractionResolver ─┬─> Local Control ─> Main Loop
                                      └─> Status / RKLLM / TTS
```

RK3588 负责感知、语音和决策；STM32 负责协议解析、状态机与实时运动控制。完整链路和安全边界见[系统架构说明](docs/system_architecture.md)。

## 文档导航

### 开始使用

| 文档 | 内容 |
|---|---|
| [硬件清单与接线](docs/hardware_setup.md) | 硬件选型、引脚、供电注意事项和首次联调顺序 |
| [Orange Pi 部署与运行](docs/deployment_orangepi.md) | 环境、模型目录、配置、启动方式和 systemd |
| [模型资源与校验](docs/model_assets.md) | Qwen 模型来源、转换方式、SHA-256 与许可证边界 |

### 理解系统

| 文档 | 内容 |
|---|---|
| [系统架构说明](docs/system_architecture.md) | 异构职责、视觉/语音/对话链路与关键机制 |
| [通信协议说明](docs/communication_protocol.md) | RK3588 ↔ STM32 帧格式、命令和安全语义 |
| [性能指标与测量](docs/performance.md) | 控制周期、历史基线、指标边界和测量命令 |

### 开发与排障

| 文档 | 内容 |
|---|---|
| [测试与诊断](docs/testing.md) | 单元测试以及视觉、ASR、RKLLM 和 TTS 验证工具 |
| [常见问题](docs/troubleshooting.md) | 摄像头、串口、ASR、RKLLM、TTS 与服务排障 |

### 版本与发布

| 文档 | 内容 |
|---|---|
| [v5.1 发布说明](docs/RELEASE_V5_1.md) | 版本范围、配置变化、升级方式和已知限制 |
| [更新日志](CHANGELOG.md) | 各版本变化记录 |
| [v5.0 历史说明](docs/RELEASE_V5.md) | 上一稳定版本的设计边界 |

## 仓库结构

```text
Gimbal-AI-Assistant/
├── Hardware_STM32/       # STM32F103 + FreeRTOS 固件
├── Software_RK3588/
│   ├── app/              # 视觉、语音、LLM、技能和控制模块
│   ├── configs/          # 场景配置
│   ├── models/           # 本地模型目录；大文件不进入 Git
│   ├── scripts/          # 启动、部署、测试和性能脚本
│   ├── tools/            # 独立诊断工具
│   ├── tests/            # 自动测试
│   └── main.py           # 主程序入口
├── docs/                 # 模块化文档
├── CHANGELOG.md
└── README.md
```

## 第三方资源与许可证

项目使用 RetinaFace、SenseVoice、Silero VAD、Qwen、RKLLM、Piper，并可调用系统安装的 eSpeak NG。模型和第三方运行时二进制不随仓库分发，使用和再分发前请分别确认上游许可证。

项目代码遵循 [MIT License](LICENSE)。

Copyright (c) 2026 Z-Teddy
