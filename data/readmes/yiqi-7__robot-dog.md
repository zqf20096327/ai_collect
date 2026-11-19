# Robot Dog：ROS 2 四足巡检机器人仿真

**中文** | [English](README.en.md)

基于 **ROS 2 Lyrical、Gazebo Sim 10、CHAMP 和 Nav2** 的四足巡检机器人仿真项目。项目包含机器人模型与仿真、建图/定位/导航、航点巡逻、MQTT 遥测与任务接口、语音链路、视频流，以及浏览器运维看板。

> 项目目前以仿真验证为主，尚未在真实四足硬件上完成验证。这里的“避障”指 Nav2 导航过程中的激光雷达 costmap 避障，不代表任何运动场景都有独立的安全急停保护。

## 能力概览

| 子系统 | 当前实现 |
|---|---|
| 步态与运动 | 使用 CHAMP；不包含自研步态控制器 |
| 建图与导航 | SLAM Toolbox、预建图定位、Nav2；运行时 `/scan` 更新障碍层 |
| 任务与巡逻 | MQTT 派单、Nav2 航点巡逻、失败重试与脱困动作 |
| 遥测与安全 | MQTT 状态/告警、心跳看门狗、速度输入超时归零 |
| 语音 | 端侧录音与 Opus 上行、语音网关 ASR/TTS；模型需单独获取 |
| 视频 | MQTT-JPEG 快照兜底；可选 RTSP / MediaMTX / WebRTC(WHEP) 主通道 |
| 看板 | React + Vite 单页应用，显示遥测、地图、任务、告警和视频 |

### 避障与安全边界

Nav2 的局部和全局 costmap 都订阅 `/scan` 并启用 obstacle layer，导航控制器可据此绕开已观测到的障碍。`collision_monitor` 节点虽然在配置中，但当前 `polygon_stop` 区域是禁用状态；因此不要把它描述为已启用的近距离碰撞急停。遥控或其他节点绕过 Nav2 直接发速度时，也不能依赖 Nav2 costmap 保护机器人。真实硬件部署仍需独立急停和安全验证。

## 部署方式

| 模式 | 用途 | 组成 |
|---|---|---|
| 模式 1：本地全栈 | 开发、仿真和单机演示 | ROS 2/Gazebo、MQTT、看板和语音网关均在本机；没有 MediaMTX 时视频使用 JPEG 快照 |
| 模式 2：云端分离 | 远程访问演示/部署 | 机器人侧运行仿真与 ROS 2 节点；中转服务器运行 MQTT、看板、语音网关和可选 MediaMTX |

真实地址不写在仓库。模式 2 在相应主机的仓库副本中配置：

```bash
cp deploy/qbot.env.example deploy/qbot.env
# 编辑 deploy/qbot.env，至少设置 CLOUD_HOST；NAT 场景还需设置 PUBLIC_IP
```

`deploy/qbot.env` 已被 gitignore 排除。模式 2 详细前置条件、服务安装、端口和排障步骤见 [部署指南](deploy/README-DEPLOY.md)。公网 MQTT/视频服务当前没有认证配置，**不要直接暴露到不可信公网**。

## 快速开始：模式 1

目标环境为 Ubuntu 26.04、ROS 2 Lyrical 与 Gazebo Sim 10。先安装项目依赖，并确保已 source ROS 环境：

```bash
sudo apt install ros-lyrical-desktop ros-lyrical-navigation2 \
  ros-lyrical-slam-toolbox ros-lyrical-ros-gz \
  libmosquitto-dev mosquitto mosquitto-clients nlohmann-json3-dev \
  libopencv-dev ffmpeg
source /opt/ros/lyrical/setup.bash
```

构建 ROS 工作区：

```bash
colcon build --symlink-install
source install/setup.bash
```

模式 1 脚本还需要仓库忽略的 `quadruped-ops/` 运行副本（看板依赖、构建产物及可选模型）：

```bash
cp -a dashboard quadruped-ops
cd quadruped-ops
npm install
npm run build
cd ..
```

Mosquitto 需要同时监听 TCP `1883` 和 WebSocket `8083`。可安装仓库配置并重启服务：

```bash
sudo cp deploy/mosquitto-websockets.conf /etc/mosquitto/conf.d/websockets.conf
sudo systemctl restart mosquitto
```

启动和停止：

```bash
./deploy/switch_config.sh local
./deploy/mode1_local_all.sh
# 停止本地模式
./deploy/stop_all.sh local
```

默认启动 Nav2、CHAMP、巡逻和 `voice_source`。需要无麦克风运行时，可将 `voice:=false` 传给 launch；模式脚本的完整选项和准备步骤见 [部署指南](deploy/README-DEPLOY.md)。启动后打开 `http://127.0.0.1:8080`。

## 主要目录

```text
src/champ/                     CHAMP 上游控制器
src/quadruped_champ_config/    本项目的 CHAMP 参数与模型适配
src/quadruped_sim/             Gazebo 模型、launch、Nav2 配置
src/quadruped_explorer/        航点巡逻与恢复逻辑
src/quadruped_mqtt_bridge/  MQTT、任务、语音、视频与安全节点
dashboard/                     看板源码、语音网关与接口文档
deploy/                        本地/云端脚本及服务配置
maps/                          示例地图
tools/weaknet/                 弱网测试工具
```

## 测试与状态

在 ROS 2 环境中构建和测试：

```bash
colcon build --symlink-install
colcon test
colcon test-result --verbose
```

看板测试：

```bash
cd dashboard
npm install
npm test
npm run build
```

已有仿真验证覆盖 8 个 ROS 包、29 项 C++ 测试，以及看板测试；这些结果不等于真实硬件验收。巡逻在长时间仿真中仍会出现 Nav2 规划/执行失败和步态卡滞，不能视作可靠的无人值守系统。

## 文档

- [完整部署指南](deploy/README-DEPLOY.md)
- [看板说明](dashboard/README.md)
- [MQTT 接口](dashboard/MQTT-INTERFACE.md)
- [语音接口](dashboard/VOICE-INTERFACE.md)
- [视频链路](dashboard/VIDEO-LINK.md)
- [CHAMP 配置包](src/quadruped_champ_config/README.md)
- [MQTT 桥接包](src/quadruped_mqtt_bridge/README.md)
- [弱网测试](tools/weaknet/README.md)
- [许可证与第三方归属](LICENSE) / [NOTICE](NOTICE)

## 已知限制

- 仅完成仿真验证，真实四足硬件、地面接触和传感器可靠性尚未验证。
- Nav2 的 costmap 避障只适用于导航控制链路；当前 `collision_monitor` 的停止多边形未启用。
- 巡逻和脱困仍可能失败或卡滞；长时间无人值守运行不可靠。
- MQTT/MediaMTX 示例为匿名配置；公网使用前必须自行配置认证、访问控制和 TLS。
- 语音 ASR 模型及部分运行模型不随仓库分发，需按对应文档获取并遵守上游许可。
- 模式 1 的默认视频通道是 MQTT-JPEG；流畅 WebRTC 视频需单独部署 MediaMTX。

## 许可

本仓库自有代码按 [MIT](LICENSE) 发布。`src/champ/` 保留 CHAMP 上游的 BSD-3-Clause 许可；第三方归属见 [NOTICE](NOTICE)。
