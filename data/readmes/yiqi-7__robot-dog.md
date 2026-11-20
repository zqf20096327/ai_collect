# Robot Dog

在 Gazebo 的虚拟厂区里运行四足巡检机器人，用浏览器看板派发任务、查看地图、遥测和告警。项目目前只在仿真环境中验证。

[快速开始](#快速开始体验巡检看板) · [完整仿真](#继续使用) · [English](README.en.md)

## 快速开始：体验巡检看板

准备 Git 和 Node.js 22.12 或更新版本（含 npm）。这条路径使用内置模拟数据，不需要 ROS 2、机器人或 MQTT Broker。

```bash
git clone https://github.com/yiqi-7/robot-dog.git
cd robot-dog/dashboard
npm ci
```

在当前 `dashboard` 目录打开 [public/qbot-config.js](dashboard/public/qbot-config.js)，把 `mqtt.mode` 从 `"real"` 改成 `"mock"`。在同一目录运行：

```bash
npm run dev
```

打开终端打印的本地地址（默认 <http://localhost:3000>）。确认页脚显示「内置模拟」，再在「机器人队列」点选另一台机器人。右侧「选中机器人」卡片应切换到对应编号，并显示它的电量等遥测数据。按 `Ctrl+C` 停止。

## 继续使用

- [完整仿真](deploy/README-DEPLOY.md#模式-1本地全栈单机)：在 Ubuntu 26.04 上运行 ROS 2 Lyrical、Gazebo Sim 10、CHAMP 和 Nav2，体验建图、定位与航点巡逻。
- [云端中转部署](deploy/README-DEPLOY.md#模式-2云端分离生产--远程控制)：分开运行仿真主机和远端服务。MQTT 与视频的示例配置允许匿名访问，仅在受信网络内使用。
- [看板配置](dashboard/README.md) · [MQTT 接口](dashboard/MQTT-INTERFACE.md) · [语音接口](dashboard/VOICE-INTERFACE.md) · [视频链路](dashboard/VIDEO-LINK.md)

<details>
<summary>完整仿真：准备环境和启动</summary>

先按照 [ROS 2 Lyrical 文档](https://docs.ros.org/en/lyrical/Get-Started/Installation/Ubuntu-Install-Debs.html)配置软件源。在 Ubuntu 上从仓库根目录运行：

```bash
sudo apt install ros-lyrical-desktop ros-lyrical-navigation2 \
  ros-lyrical-slam-toolbox ros-lyrical-ros-gz ros-dev-tools \
  libmosquitto-dev mosquitto mosquitto-clients nlohmann-json3-dev \
  libopencv-dev libx11-dev ffmpeg
source /opt/ros/lyrical/setup.bash
colcon build --symlink-install
source install/setup.bash
```

按[部署指南](deploy/README-DEPLOY.md#模式-1本地全栈单机)准备 `quadruped-ops/` 看板运行副本，并启用 Mosquitto 的 TCP 和 WebSocket 监听。然后在仓库根目录运行：

```bash
./deploy/switch_config.sh local
./deploy/mode1_local_all.sh
```

打开 <http://127.0.0.1:8080>，按[验证清单](deploy/README-DEPLOY.md#验证清单)检查 MQTT 遥测与视频。运行 `./deploy/stop_all.sh local` 停止。Nav2 的避障只覆盖导航链路，独立的近距离急停区域未启用，巡逻和恢复仍可能失败。

</details>

[问题反馈](https://github.com/yiqi-7/robot-dog/issues) · [MIT 许可证](LICENSE) · [第三方许可（含 CHAMP）](NOTICE)
