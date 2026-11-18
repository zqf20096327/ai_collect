# Robot Dog 🐕 — 厂区四足巡检机器人

**中文** | [English](README.en.md)

基于 **ROS 2 (Lyrical) + Gazebo (gz sim 10)** 的四足机器狗仿真与运维项目：
在仿真厂区里完成建图、导航、巡逻，并通过 MQTT 对接浏览器运维看板与语音指令网关，
端侧经 **腾讯云中转** 实现远程控制。

![ROS2](https://img.shields.io/badge/ROS%202-Lyrical-blue)
![Gazebo](https://img.shields.io/badge/gz%20sim-10-orange)
![Platform](https://img.shields.io/badge/平台-Ubuntu%2026.04-green)
![MQTT](https://img.shields.io/badge/MQTT-mosquitto-purple)
![WebRTC](https://img.shields.io/badge/视频-WebRTC%2FWHEP-ff69b4)

---

## 这个项目做了什么

| 能力 | 实现 |
|---|---|
| 四足步态 | CHAMP 通用控制器 + 自研 `gait_controller`，trot 步态实测 0.35 m/s |
| 建图与导航 | SLAM Toolbox 在线建图 / 预建图定位 + Nav2 规划控制 |
| 上云桥接 | 4 个职责单一节点：`mqtt_bridge`(遥测/告警/遗嘱) `task_runner`(派单执行) `voice_link`(语音上行+TTS) `deadman_guard`(心跳看门狗) |
| 视觉 | `image_sender`：JPEG 快照(MQTT 兜底) + H.264 推流(RTSP→WebRTC 主通道) |
| 语音 | 端侧录音 → **Opus 压缩（实测 12.9:1 ~ 16:1）** → MQTT 上行 → 云端 ASR(SenseVoice) → LLM/规则决策 → 任务下发 + TTS 播报 |
| 运维看板 | React + Vite 单页应用，实时遥测、地图、任务派单、语音指令、视频监控 |
| 安全 | 心跳看门狗 + 输入超时归零 + 碰撞监控，三级速度链 (`cmd_vel_in → cmd_vel → 底盘`) |

---

## 两种部署模式

项目支持两种形态，**先单机跑通再上云**：

| | 模式 1：本地全栈 | 模式 2：云端分离 |
|---|---|---|
| 场景 | 本地读代码 / 单机演示 | 生产部署 / 远程控制 |
| ROS2 | TITAN_V | TITAN_V |
| MQTT + 视频中转 + 语音网关 + 看板 | TITAN_V 全在本机 | 腾讯云 `43.172.91.67` |

> ### ⚠️ 部署到你自己的环境前必读：文中 IP 是作者的测试服务器
>
> 本文档里出现的 `43.172.91.67` 是**作者自己的腾讯云测试机**，不是公共服务。
> 直接照抄会在你的环境里连到别人的服务器（机器人画面也会推过去）。
> **部署到你自己的环境时，请把这些地址全部替换成你自己的服务器 IP / 域名。**
>
> 替换点清单（下文用 `<你的IP>` 表示你自己的服务器地址）：
>
> | 位置 | 变量 / 参数 | 怎么换 |
> |---|---|---|
> | `deploy/switch_config.sh` | `CLOUD_HOST`（默认 `43.172.91.67`） | 改脚本内默认值，或临时覆盖：`CLOUD_HOST=<你的IP> ./switch_config.sh cloud` |
> | `dashboard/public/qbot-config.js` | `mqtt.brokerUrl`、`streaming.whepBase` | 看板**运行时**配置，改完刷新浏览器即生效（无需重新构建） |
> | `deploy/mediamtx.yml` | `webrtcAdditionalHosts` | 必须填你的公网 IP，否则浏览器 WHEP 建连失败 |
> | `deploy/mode2_robot_side.sh` | `--host <你的IP>` | 端侧启动参数（脚本内默认值也要改） |
> | `deploy/mode2_cloud_side.sh`、`deploy/push_cloud_app.sh` | 云端地址 / ssh 目标 | 脚本内默认值 |
> | `src/quadruped_sim/launch/quadruped_gz.launch.py` | `broker_host`、`rtsp_server` | 可用 launch 参数覆盖 `broker_host:=<你的IP>`；`rtsp_server` 目前写死在文件里，需直接改 |
> | `src/quadruped_mqtt_bridge/src/image_sender.cpp` | RTSP 推流地址默认值 | 直接改源码里的默认值 |
> | 各文档（`README*.md`、`deploy/*.md`、`dashboard/VIDEO-LINK.md`） | 示例命令里的 IP | 只是示例，替换即可 |
>
> 只跑**模式 1（单机）**时不需要任何公网地址：`./deploy/switch_config.sh local` 会把看板指向 `127.0.0.1`。

```bash
# 在仓库根目录执行（脚本会自己推导工作区路径，不需要先 cd deploy）

# 模式 1：单机起全部（ROS2 + broker + 语音网关 + 看板）
./deploy/switch_config.sh local && ./deploy/mode1_local_all.sh

# 模式 2：云端
./deploy/mode2_cloud_side.sh                       # 在 43.172.91.67 上（换成你的云端）
./deploy/mode2_robot_side.sh --host 43.172.91.67   # 在 TITAN_V 上（换成你的云端）

# 停止：四选一（local / cloud / robot / all）。
# 注意别照抄 `local|cloud|robot|all` —— 在 shell 里 `|` 是管道，会被当成命令执行
./deploy/stop_all.sh local
```

详细说明见 **[deploy/README-DEPLOY.md](deploy/README-DEPLOY.md)**。

> **语音功能需要额外下载 ASR 模型**（229MB，不入库）。官方发布包：
> ```bash
> wget https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/\
> sherpa-onnx-sense-voice-zh-en-ja-ko-yue-int8-2024-07-17.tar.bz2
> tar xvf sherpa-onnx-sense-voice-zh-en-ja-ko-yue-int8-2024-07-17.tar.bz2
> # 把 model.int8.onnx 与 tokens.txt 放进 dashboard/models/sensevoice/
> ```
> 不放模型也能跑：网关会打印"语音通道关闭，仅文本注入可用"，其余功能不受影响。

---

## 环境要求

最小可用配置（数字取自 [deploy/README-DEPLOY.md](deploy/README-DEPLOY.md) 的「云端资源实测」表）：

| 项 | 要求 | 依据 / 说明 |
|---|---|---|
| 系统 | **Ubuntu 26.04 LTS**（ROS 2 **Lyrical** 对应的发行版） | 本项目在 26.04 + `/opt/ros/lyrical` 上实测 |
| ROS 2 | Lyrical + Gazebo `gz sim 10` | 见下方「依赖」 |
| 内存 | 建议 **8 GB+** | 云端只跑中转（无 Gazebo）时实测 **1967 MB** 可运行：ASR 加载后 `voice-gateway` RSS 约 400 MB，系统余量约 800 MB；本机再跑仿真需要更多 |
| 磁盘 | 建议 **10 GB+ 可用** | 云端一侧实测 `/opt/qbot` 约 280 MB（模型 229 MB + `node_modules` 45 MB + `dist` 6 MB）；本机还要放 ROS 2 / Gazebo、`build/`、`install/`、`quadruped-ops/` 等构建与运行产物 |
| ASR 模型 | 约 **290 MB**（不入库，需自行下载） | `model.int8.onnx` 约 229 MB + `tokens.txt` 约 309 KB；模型目录含示例音频共约 290 MB。缺失只会关闭语音通道 |
| 网络 | 模式 1 无需外网；模式 2 需放行 TCP `1883/8083/8554/8889/8080` + UDP `8189` | 端口清单见 [deploy/README-DEPLOY.md](deploy/README-DEPLOY.md) |

---

## 快速开始

### 依赖

```bash
# ROS 2 Lyrical + Gazebo (gz sim 10)
sudo apt install ros-lyrical-desktop ros-lyrical-navigation2 \
     ros-lyrical-slam-toolbox ros-lyrical-ros-gz
# MQTT 依赖
sudo apt install libmosquitto-dev mosquitto mosquitto-clients nlohmann-json3-dev
# 视觉 / 语音
sudo apt install libopencv-dev ffmpeg
```

### 编译

```bash
source /opt/ros/lyrical/setup.bash   # 全新机器必须先 source，否则 colcon 找不到 ROS 2 依赖
cd <本项目根目录>              # 后面命令用 $(pwd)，所以在根目录执行
colcon build --symlink-install
source install/setup.bash
```

### 启动（模式 2，连云端）

```bash
ros2 launch quadruped_sim quadruped_gz.launch.py \
  gui:=false rviz:=false nav:=true gait:=champ teleop:=false patrol:=false \
  map:=$(pwd)/maps/factory_full.yaml \
  broker_host:=43.172.91.67 broker_port:=1883
```

### 看板

```bash
# 浏览器打开
http://43.172.91.67:8080          # 模式 2
http://127.0.0.1:8080             # 模式 1
```

---

## 项目结构

```
robot-dog/
├── src/
│   ├── champ/                     # CHAMP 四足步态控制器（vendored + 本项目补丁）
│   ├── quadruped_champ_config/    # CHAMP 适配本机的参数包
│   ├── quadruped_sim/             # 仿真包：模型、步态、传感器、Nav2 参数
│   ├── quadruped_mqtt_bridge/     # 上云桥接：4 节点 + 视觉 + 语音采集
│   └── quadruped_explorer/        # 自主导航：航点巡逻、卡死重试
├── dashboard/                     # 运维看板（React + Vite）+ 语音网关
├── deploy/                        # 两种模式的部署脚本与 MediaMTX/Mosquitto 配置
├── tools/weaknet/                 # 弱网注入与矩阵测试脚本
├── maps/                          # 预建地图（factory_full.yaml 等）
└── README.md / README.en.md
```

> `quadruped-ops/` 是 `dashboard/` 的运行副本（含 node_modules 与 290MB 模型），
> **不入库**，按需在本地保留即可。

---

## 关键设计

### 节点拆分：单一职责 + 松耦合

早期是一个大 `mqtt_bridge` 节点包办遥测、派单、语音、安全。问题很实际：
任何一处出问题都要重启全部功能，语音大帧会顶掉遥测的 keepalive。

拆成 4 个独立节点后，各自持有独立 MQTT 连接、独立失败域：

| 节点 | 职责 | 订阅 |
|---|---|---|
| `mqtt_bridge` | 遥测 1Hz、告警、LWT 遗嘱 | 无 |
| `task_runner` | 接收 `cmd` 派单、执行导航、回写任务状态 | `robots/+/cmd` |
| `voice_link` | 语音上行、TTS 播报、piper 合成 | `robots/+/tts` |
| `deadman_guard` | 心跳监控、速度旁路与归零 | `safety/heartbeat` |

### 语音压缩：为什么必须做

课程接口约定 `pcm_s16le` + base64，并注明"局域网可直传"。但实际部署是**公网弱网**：

| 方案 | 3.6 秒语音体积 | 512kbit 上行耗时 |
|---|---|---|
| 原始 PCM（112 KB 裸流）→ base64 | 150 KB | 约 2.3 s（理想）/ 数十秒（15% 丢包） |
| **Ogg/Opus（实测 5 KB ≈ 11 kbps）→ base64** | **7 KB** | **约 0.1 s** |

> 口径说明：112 KB 是裸 PCM，150 KB 是它 base64 编码后（×4/3）的实际上行体积。
> Opus 同理：5 KB 裸流、7 KB base64。压缩比按裸流算 ≈22:1，按上行字节算 ≈21:1；
> 若只算「PCM ↔ 上行」则是 112:7 ≈ 16:1，文档取保守区间 12.9:1 ~ 16:1。

端侧用 ffmpeg 编码 Opus（失败自动回退 PCM），云端网关解码后送 ASR。
压缩比实测 **12.9:1 ~ 16:1**，ASR 识别结果不受影响。

### 视频：双通道

- **主通道**：`image_sender` → ffmpeg(H.264, 禁 B 帧) → `rtsp://<中转>:8554/cam/<id>` → MediaMTX → 浏览器 WHEP
- **兜底通道**：MQTT 二进制 JPEG 快照（640×360 / q90 / 1fps，实测约 17.7 KB/帧）
- 主通道挂了看板自动降级到快照，快照也断了才显示静态占位图

细节见 **[dashboard/VIDEO-LINK.md](dashboard/VIDEO-LINK.md)**。

### 安全：三层防护

1. `collision_monitor` — 激光雷达碰撞检测
2. `deadman_guard` — 心跳 >3s 切断、速度输入 >0.5s 归零（底盘层最后手段）
3. 端侧 LWT 遗嘱 — 掉线时 broker 代发离线状态

---

## 实测数据

| 指标 | 结果 |
|---|---|
| Trot 步态速度 | 0.35 m/s（`/odom` 真值） |
| 遥测频率 | **1 Hz**（`mqtt_bridge` 的 `publish_hz` 默认 `1.0`，见 `src/quadruped_mqtt_bridge/src/node_core.cpp`），单帧约 0.2 KB |
| 摄像头兜底帧 | 640×360，q90，约 17.7 KB/帧，1 fps |
| 语音压缩 | 3.6s：112 KB PCM → 5 KB Opus → 7 KB base64 |
| 云端中转 RTT | 851 ~ 1590 ms（均值 1192 ms，抖动 ±304 ms） |
| MQTT 断线恢复 | 10 ~ 16 s（`mosquitto_reconnect_delay_set(2, 10)`） |
| 弱网矩阵测试 | 41 项检查中 28 项通过（六档 W1~W6：延迟/抖动/丢包/乱序/断网/组合） |

**弱网失败的构成**（13 项失败，逐条核对原始结果后）：

- **W5/W6 断网档是真失败**：链路断开后客户端未及时检测到 keepalive 超时，
  恢复后 `state` 与三节点重连都超出 25 s 窗口，遥测停止。
- **4 项「派单执行」是检查脚本的假阴性**：W2/W3/W4 的位移分别是 4.90 / 1.74 / 5.44 m，
  机器人实际走到了，但脚本的「是否启动」判定写成了 `False`（它只看首个速度帧，
  弱网下丢包导致首帧错过）。真实结论应以位移为准。
- **W1 派单确实未执行**（位移 0.00 m）。
- **看门狗与节点存活 12/12 全通过**：六档弱网下 `deadman_guard` 从未误触发，
  四个节点始终在线——这是安全链路的正面证据。

---

## 巡逻与建图实测

### 长时间巡逻统计

以 `/tmp/sim_v6.log`（一次连续运行 81.8 分钟）统计：

| 指标 | 数值 |
| --- | --- |
| 发送航点 | 220 次 |
| 到达 | 76 次 |
| 重试耗尽跳过 | 42 次 |
| 整体到达率 | 34.5% |
| 最近 120 条日志区间到达率 | 57% |

**结论：巡逻不是"零失败"**。失败集中在机器人停在货架/墙面前 1.6 m 无法起步时，
Nav2 下发速度但步态推不动（关节速度打满限幅），最终以 `code=6` 中止。
改进方向见 [已知限制](#已知限制)。

### 加脱困后的回归（静态合并图）

`patrol_node` 现在会在重试前先做一次**脱困**（后退 1.3 s + 原地转 1.6 s），
再重发目标。同一台机上实测：

| 指标 | 数值 |
| --- | --- |
| 环线 1 | **4/5 到达**（北走廊 / 墙洞东 / 缝北口 / 货架南 全部一次到达） |
| 唯一失败 | 出生点 `code=6` × 3 次，脱困后仍未能起步，跳过 |
| 后续环 | 机器人连卡在货架南侧后多点失败，需要人工干预 |

结论：脱困把一部分 `code=6` 变成到达（补扫驱动里也验证过同样的效果），
但 Champ 步态在货架/墙角顶住时仍可能连续卡死，这是步态本身的局限，
不是导航参数问题。彻底解决需要换步态或加专门的"蹬地-收回"恢复动作。

### 地图补扫（仓库东侧）

旧图 `factory_full` 有 18.7% 未知区，集中在仓库东侧，当时 (5.0,-6.0)、
(7.0,-5.5)、(8.0,-5.5) 三处"全规划失败"。补扫按下面的流程做完：

1. **临时切 SLAM 模式**（启动不带 `map:=`），跑"逐点规划 + 跟踪"的自动环线
   （34 点，路线由 `tools/make_rescan_route.py` 生成——它直接读 `maps/factory_full.pgm`
   找出未知区边缘）；每点先 `ComputePathToPose` 预验证，失败/中止就先脱困再重试一次，
   仍不行跳过。绕开 `bt_navigator` 直接对接 planner/controller，避免行为树在负载高时激活失败。
   说明：跑环线的驱动脚本是一次性临时脚本（历史上放在 `/tmp/rescan_driver.py`，
   **不在仓库内**，机器重启就没了）；仓库里保留的是可复现的路线生成器
   `tools/make_rescan_route.py`。
2. **保守合并**新图与旧图：旧图已知处**全部保留**，旧图未知处只吸收
   新图"确认自由"的格——**不吸收新图的障碍格**。原因：新会话的占据
   像素里有步态抖动噪声，窄通道里多 1% 障碍就会把 0.35 m 内切膨胀
   连成墙（实测激进合并后 costmap 57% 格子是 253/254，走廊全断，
   机器人被困在 1.2 m 的小口袋里）。
3. 合并时两图帧都锚在出生点、偏航一致，只按世界坐标平移；最后裁回
   旧图 404×289 的画面尺寸与原 origin，保证巡逻航点、AMCL 初值全部沿用。

| 指标 | 旧图 | 补扫合并后 |
| --- | --- | --- |
| 分辨率 / 尺寸 | 0.05 m / 404×289 | 0.05 m / 404×289（帧不变）|
| 自由 | 75.7% | **85.0%** |
| 占据 | 5.6% | 5.6%（不引入新障碍）|
| 未知 | 18.7% | **9.4%** |
| 仓库东区未知 | 39.4% | **24.5%** |
| (8.0,-5.5) 1 m² 未知 | 76.2% | **13.8%** |
| (7.0,-5.5) 1 m² 未知 | 45.1% | **17.7%** |

**补扫的意外结论**：(7.0,-5.5) 和 (8.0,-5.5) 这两处补扫后确认**是货架实体
本身**——旧图那里是未知，`track_unknown_space: false` 把未知当自由，
规划器才"假可达"。所以它们本来就不该当驻留点；挨着的通道
(5.0,-5.4) 规划正常（已验证 ✅）。这比"补出一块能站的地"更有价值：
新图让规划器不再从货架里穿过去。

> 早期记录曾写"40 分钟 6 轮 30/30 全到达、零失败"，该结论来自单次未含异常
> 状态的观测，与长时间运行统计不符，此处按实测数据更正。

## 文档索引

| 文档 | 内容 |
|---|---|
| [deploy/README-DEPLOY.md](deploy/README-DEPLOY.md) | 两种部署模式的完整操作手册 |
| [dashboard/VIDEO-LINK.md](dashboard/VIDEO-LINK.md) | 视频链路拓扑、配置要点、实测与排障 |
| [dashboard/MQTT-INTERFACE.md](dashboard/MQTT-INTERFACE.md) | MQTT 主题与报文契约 |
| [dashboard/VOICE-INTERFACE.md](dashboard/VOICE-INTERFACE.md) | 语音链路契约（上行/下行/确认策略） |
| [tools/weaknet/README.md](tools/weaknet/README.md) | 弱网注入与矩阵测试方法 |
| [deploy/mediamtx-install.md](deploy/mediamtx-install.md) | MediaMTX 安装与配置 |
| [LICENSE](LICENSE) / [NOTICE](NOTICE) | 许可（MIT）与第三方组件归属 |

---

## 已知限制

- 仿真环境，未在真实四足硬件上验证
- 看板任务 ID 由前端 `max(existing)+1` 分配，多操作员并发时有碰撞风险
- MediaMTX 与 MQTT 目前允许匿名访问，公网部署需补认证
- 语音上行依赖端侧 ffmpeg + libopus
- 模式 1 默认无 MediaMTX，视频降级为 MQTT-JPEG 快照

---

## 许可与致谢

- **本项目**（本仓库自有的代码与文档，含 `dashboard/`、`deploy/`、`src/quadruped_*`）以
  **MIT** 许可发布，全文见 [LICENSE](LICENSE)（年份 2026，署名 `yiqi-7`）。
  > 如与课程 / 竞赛的许可要求冲突，**以课程 / 竞赛要求为准**。
- **`src/champ/`** 是 vendored 的上游项目 **CHAMP**，遵循其 **BSD-3-Clause** 许可
  （原文见 [src/champ/champ/include/champ/LICENSE](src/champ/champ/include/champ/LICENSE)）。
  本项目只在其上做适配补丁（参数包 `quadruped_champ_config`、接口对接），未改变上游许可条款。
- **第三方组件**（均为运行时依赖，未修改其源码）：

  | 组件 | 用途 | 许可 |
  |---|---|---|
  | [CHAMP](https://github.com/chvmp/champ) | 四足步态控制器（`src/champ/`，vendored） | BSD-3-Clause |
  | [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) + SenseVoice 模型 | 语音识别（ASR） | Apache-2.0 |
  | [MediaMTX](https://github.com/bluenviron/mediamtx) | RTSP → WebRTC 视频中转 | MIT |
  | [Eclipse Mosquitto](https://mosquitto.org/) | MQTT Broker | EPL-2.0 |
  | [Gazebo / gz-sim](https://gazebosim.org/) | 仿真环境 | Apache-2.0 |
  | [ROS 2](https://docs.ros.org/) / [Nav2](https://nav2.ros.org/) / [SLAM Toolbox](https://github.com/SteveMacenski/slam_toolbox) | 中间件、导航、建图 | Apache-2.0 / 见各自上游仓库 |
  | [React](https://react.dev/) / [Vite](https://vite.dev/) / [mqtt.js](https://github.com/mqttjs/MQTT.js) / [Recharts](https://recharts.org/) | 看板前端 | MIT |

  各组件版权归其原作者所有；模型权重（SenseVoice、piper）遵循各自发布许可，且**不入库**
  （见 `.gitignore`）。更细的归属说明见 [NOTICE](NOTICE)。
