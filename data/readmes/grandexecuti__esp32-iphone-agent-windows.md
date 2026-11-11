# esp32-iphone-agent-windows

**English** — A Windows-native port of [esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent): an ESP32‑S3 USB‑HID bridge plus AirPlay mirroring that lets a single Windows PC see the iPhone screen and drive it like a mouse and keyboard, with a ZCode skill/plugin for hands-on iOS app testing. This repository is a fork with substantial modifications — see [What we changed](#what-we-changed-relative-to-upstream) below.

**中文一句话** — 用一块 ESP32 当"手"（USB 鼠标键盘）、用 AirPlay 投屏当"眼"，在这台 **Windows 电脑上独立承载整套 iPhone 控制栈**：网页上看实时画面、点击即点按；再配一个 ZCode 技能，让 AI 直接"看屏幕 → 点按 → 再截图验证"。

> ## ⚠️ 先说清楚：这是对开源项目的改造，不是原创
>
> 本仓库**基于** [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)（MIT License，© 2026 Henry Yuan）**改造而来**。上游给出了整套架构思路（iOS 辅助触控 + ESP32 USB HID 当"手"，AirPlay/UxPlay 当"眼"，视觉模型当"脑"），我们做的是一件事：**把它的服务端完整移植到 Windows，并把在 Windows 上跑不通的每一层修到能用**，外加 ZCode 集成。
>
> 上游的版权与许可完整保留（见 [LICENSE](LICENSE)，MIT 双版权声明）。**所有改动都列在下面的"我们改了什么"和各处注释里**，文件级清单见 [CHANGES.md](CHANGES.md)。如果这个项目对你有帮助，请也给上游点一个 Star。

---

## 这个项目能做什么

一块插在 iPhone 上的 ESP32 板（模拟 USB 鼠标键盘）+ 一条 AirPlay 投屏流，让电脑能够：

- **看**：实时画面（网页 / HTTP API / AI 模型读图）；
- **动**：点按、长按、滑动、滚动、英中文字输入、系统手势（回主屏/返回）；
- **自动化**：`/api/agent` 接口让视觉模型自己规划并执行任务（需在 `.env` 配模型）；
- **给 AI 工具用**：附带 ZCode 技能，直接在对话里说"看一下我手机 / 帮我点 XX"。

整套东西跑在一台 Windows 10/11 电脑上（Python 3.10+），不需要 Mac、不需要 Linux。

---

## 我们改了什么（相对上游）

> 这一节是重点：以下每一处都是本仓库新增或修改的内容，**上游没有**。

### 1. Windows 原生服务端（从"必须 macOS/Linux"到"Windows 全栈可跑"）

上游的取帧方式依赖 POSIX 管道（`os.pipe`）和 UxPlay 的自定义 GStreamer sink——这在 Windows 上不可行。我们从零重建了取帧链路：

- **`server/hidagent/screen_pipe.py`（新增）** —— 命名管道取帧后端。让接收器把**解码后的原始帧**写进 Windows 命名管道 `\\.\pipe\hidagent-frames`，服务端一侧用 `CreateNamedPipeW` 建管道、读定长 I420 帧、转 JPEG。包含：管道自建、接收器进程监督与重启、断线自愈、接收器配置自动生成（见第 2 点）。
- **`server/hidagent/screen_win.py`（新增）** —— 窗口捕获备选后端（Windows Graphics Capture / `windows-capture`）。这是最初方案：抓 UxPlay 渲染窗口的帧。在本仓库的开发机上因显卡渲染问题被弃用（见第 2 点），保留供其他硬件参考。
- **`server/hidagent/app.py`（修改）** —— 按 `sys.platform` 选择取帧后端（Windows → `screen_pipe`，其他 → 原 `screen.py`）。
- **`server/run-server.ps1`（新增）** —— Windows 一键启动：解析 `.env`、启动服务。
- **为什么不用"窗口截图"而是"管道取帧"**：管道拿到的是**解码后的原始像素**（帧长在 caps 里锁死，数学上确定），没有窗口边框/缩放/遮挡问题，也不需要 GPU 渲染——而显卡渲染恰恰是这台机器上最容易崩的一环。

### 2. 视频管线重造：绕过 Windows 下必崩的 D3D 渲染

上游在 Linux/macOS 上一切正常；在 Windows 上我们遇到的是连续的底层问题，逐层修复如下：

- **"连上秒断"的根因**：UxPlay 引擎的 `autovideosink` 会选中 `d3d12videosink` + `d3d12h264dec`（D3D12 硬解/渲染），在旧显卡/驱动上会导致整条管线报 `Internal data stream error`、会话被拆。
  → 修法：**`-avdec` 强制软件解码**；并用**假渲染器 `fakesink`** 做消费端——由此定位到问题 100% 在 D3D 渲染，与解码、网络无关。
- **为什么最终完全不要窗口**：确认问题在 GPU 渲染后，我们不修显卡，而是把视频出口改成 `filesink` 直写命名管道（见第 1 点）——**彻底绕开 GPU 渲染**。
- **包内 `d3d11` 插件死锁的规避**：该发行包缺少 `gst-plugin-scanner.exe`，插件只能进程内扫描，而 `libgstd3d11.dll` 的插件初始化会**死锁整个进程**（坏结果被写进 GStreamer 注册缓存 `INetCache\gstreamer-1.0\registry*.bin`，删缓存也会在下次扫描时重演）。项目文档记录了处理方式（禁用该插件文件），详见 [docs/TECHNICAL.md](docs/TECHNICAL.md)。
- **包装器的参数限制**：第三方 `uxplay-windows` 包装器会**过滤掉 `arguments.txt` 里的 `-vs`（自定义视频输出）**，并且 `arguments.txt` 不支持引号（带空格的接收器名会把整个参数拆坏，而 UxPlay 引擎遇到未知参数会直接终止进程）。
  → 修法：改用 UxPlay 的 **`-rc` 配置文件通道**（每行一个选项、支持引号），由服务端在每次启动时**自动生成** `uxplayrc.conf` 与 `arguments.txt`——配置永不漂移、可自愈。
- **画面"彩色斜条纹"的修正**：GStreamer 会把每行像素**补齐到 4 字节对齐**。宽度 498 不是 4 的倍数（实际行宽 500），按 498 切片就会每行错 2 字节、整幅画面斜向错位。
  → 修法：把输出帧宽定为 **496（4 的倍数，零补位）**，帧长 = `496 × 1080 × 1.5 = 803,520` 字节，完全确定。

### 3. 指针控制的可靠性（漂移、误判、精度）

iOS 的指针不是桌面鼠标：有**自己的加速曲线**，顶到屏幕边缘会**钳制**（指针不再移动、但服务端的相对记账还在继续），并且**靠近可点控件才显形**。上游的直觉参数在这些行为下会积累误差。我们的修改（`server/hidagent/phone.py`、`vision.py`）：

- `REHOME_EVERY: 10 → 1` —— **每次手势前先"归零"**（把指针顶到左上角锚点），彻底消除边缘钳制造成的累积漂移；
- `TAP_SETTLE = 0.18s`（新增） —— 移动后、按下前留停顿：按得太早，iOS 会把手势判成"拖动"而不是点按；
- `NUDGE: 12 → 48` —— 闭环瞄准时用来"唤醒"指针的微抖幅度：12 单位太小，唤不醒已隐藏的指针；
- `vision.py` 指针识别灰度阈值 `30 → 12` —— 在 496 宽 + JPEG 75 的画面里，指针的对比度只有 15~25，阈值 30 会让它"永远找不到"；
- `_aim()` 改为**多轮闭环收敛**（测量→修正→再测量，最多 3 轮），`/api/tap` 默认启用闭环修正（请求里传 `"aim": false` 可关闭以换取速度）。

### 4. 中文输入通道

上游的 `type` 只覆盖 ASCII。我们梳理并验证了在 iOS 上的可靠中文输入流程（**不改固件**，利用固件已有的命名按键）：

- `type "juhuacha"`（拼音进输入法）→ `key "space"`（空格上屏第一候选"菊花茶"）→ `key "enter"`（提交搜索）；
- 两个实测限制写进了技能文档：**iOS 输入法候选条不响应鼠标点击**（只能触摸/空格上屏）；**协议会吞纯空格参数**（所以空格一律走 `key "space"`，不要试 `type " "`）。

### 5. ZCode 技能 / 插件（`zcode-plugin/`）

- 把"截图 → 读图 → 操作 → 再截图验证"的完整工作流、坐标体系、中文输入流程、故障排查、**已知限制**（每步 10~20 秒延迟、倒计时界面来不及点、视频 App 自动投屏会顶掉镜像等）写成技能（`SKILL.md`），并打包成 ZCode 插件（`.zcode-plugin/plugin.json`）。
- 命令行助手 `scripts/iphone.py`：`status / shot / tap / swipe / scroll / type / key / home / back / calibrate / agent`。

### 6. 运维与自愈

- 服务端每次启动**自动写入**接收器配置（rc + arguments.txt）；
- 管道断开时自动**重建管道并重启接收器**（日志：`pipe closed; starting a fresh session`）；
- 内置 `keep_awake`：空闲时心跳 + 微移指针，防止手机自动锁屏挂起 USB。

### 7. 诊断工具集（`tools/`，本仓库新增）

排查过程中自建的"仪表盘"，也留给你：

| 工具 | 用途 |
|---|---|
| `mdns_probe.py` | 查询局域网里的 AirPlay 接收器（mDNS 组播探针） |
| `mdns_sniff.py` | 监听 mDNS 流量，确认手机的发现请求是否到达本机 |
| `find_click.py` | **扫描定位器**：利用"指针靠近控件才显形"的特性，在目标附近网格探测、命中即点（小按钮的兜底方案） |
| `vision_debug.py` | 指针定位调试：微抖 + 前后帧差分，打印指针位置与像素统计 |
| `run_wrapper_logged.py` | 无控制台启动接收器并捕获其日志（排查包装器/引擎问题的关键工具） |

---

## 上游原有功能（本仓库未改动）

- 整体架构：ESP32-S3 固件（`hardware/hid_bridge`，行协议 `ping/home/move/press/release/click/scroll/type/key`）、Wi-Fi 链路、辅助触控校准、网页控制台、AI agent（planner/actor 两角色视觉模型）、测试用例等；
- 固件、网页 UI、AI agent 逻辑均沿用上游设计（相关文件保留了上游版权声明与注释）。

---

## 快速开始（Windows 10/11）

1. **硬件**：ESP32-S3（建议带 PSRAM，如 N16R8）、一根**能传数据**的 USB-C 线、iPhone（打开 设置 → 辅助功能 → 触控 → 辅助触控）。
2. **刷固件**（Arduino CLI + esp32 core 3.x）：
   ```bash
   cp hardware/hid_bridge/secrets.example.h hardware/hid_bridge/secrets.h
   # 编辑 secrets.h：WiFi 名称/密码、SERVER_HOST=你电脑的局域网 IP
   arduino-cli compile -b esp32:esp32:esp32s3:USBMode=default,CDCOnBoot=cdc,FlashSize=8M hardware/hid_bridge
   arduino-cli upload  -b esp32:esp32:esp32s3:USBMode=default,CDCOnBoot=cdc,FlashSize=8M -p COM3 --input-dir build/hid_bridge hardware/hid_bridge
   ```
   > `USBMode=default` 即 "USB-OTG (TinyUSB)"（可用 `arduino-cli board details -b esp32:esp32:esp32s3` 查证）——HID 需要它。
   > **板子有两个 USB-C 口：数据/HID 用的是"原生口"，另一个（CH343）只用于刷机/供电**，插错口鼠标键盘不会出现。
3. **AirPlay 接收器**：下载 [uxplay-windows](https://github.com/leapbtw/uxplay-windows/releases)（第三方），解压到仓库同级目录 `uxplay-windows/`（或在 `.env` 里设 `UXPLAY_DIR`）。本仓库**不包含**它的二进制。
4. **服务端**：
   ```powershell
   cd server
   python -m venv .venv
   .venv\Scripts\pip install -e .
   Copy-Item .env.example .env   # 按需编辑
   powershell -ExecutionPolicy Bypass -File run-server.ps1
   ```
   首次运行会自建 AirPlay 接收器配置并启动它；服务端在 `http://127.0.0.1:8890`。
5. **手机**：插上板子的原生口 → 控制中心 → 屏幕镜像 → **`iPhone-Agent`** → 浏览器打开 `http://127.0.0.1:8890`。
6. **校准**（首次必做）：网页上按提示校准指针；校准结果保存在 `~/.hidagent/calibration.json`，重启不用重做。

> Windows 防火墙：需要放行 ① 板子→电脑的 TCP `7300`；② `uxplay-windows.exe` 的入站（AirPlay 使用随机高位端口，**程序级规则**才可靠）；③ `mDNSResponder.exe` 的 UDP/TCP（AirPlay 发现依赖 mDNS）。苹果安装 Bonjour 时自带的防火墙规则可能只覆盖"公用"网络配置档，若局域网是"专用"档，需自行补规则（详见 [docs/TECHNICAL.md](docs/TECHNICAL.md)）。

## 配置项（`server/.env`）

| 变量 | 默认 | 说明 |
|---|---|---|
| `LLM_BASE_URL` / `LLM_MODEL` / `LLM_API_KEY` | 空 | OpenAI 兼容的视觉模型（`/api/agent` 用；手动控制不需要） |
| `ACTOR_MODEL` / `PLANNER_MODEL` | 继承 `LLM_MODEL` | 分角色的模型覆盖 |
| `AIRPLAY_NAME` | `iPhone-Agent` | 手机"屏幕镜像"列表里显示的名字（Windows 下不能带空格） |
| `PORT` | `8890` | 网页/HTTP API 端口 |
| `DEVICE_PORT` | `7300` | 板子连接的端口 |
| `HIDAGENT_DEBUG` | `0` | 1 = 详细日志 + 每次 agent 运行的 trace 存到 `~/.hidagent/traces` |
| `UXPLAY_DIR` | 仓库同级 `uxplay-windows` | 接收器目录（Windows） |

## 目录结构

```
server/hidagent/        服务端（FastAPI）
  screen_pipe.py        ★ Windows 命名管道取帧（本仓库新增）
  screen_win.py         ★ WGC 窗口捕获备选后端（本仓库新增）
  screen.py             上游 POSIX 管道取帧（macOS/Linux）
  device.py             TCP/板子协议、心跳、防锁屏
  phone.py              指针控制、校准、闭环瞄准（★ 本仓库有修复）
  vision.py             指针识别（★ 阈值修复）
  app.py                HTTP API + 网页
hardware/hid_bridge/    ESP32 固件（上游）
zcode-plugin/           ★ ZCode 技能/插件（本仓库新增）
tools/                  ★ 诊断工具（本仓库新增）
docs/                   原理深潜（TECHNICAL.md）与上游原始 README
```

## 已知限制

- 每次"看→点"的循环有 10~20 秒的人工/模型延迟（取决于调用方式），**倒计时类界面（开屏广告等）来不及点**；需要快速反应的场景不适合。
- 接收器同时只能接一路流：某些视频 App（如 Bilibili）会自动把视频投屏到 AirPlay 接收器，**会顶掉屏幕镜像**——在 App 设置里关掉"自动投屏"。
- 校准绑定竖屏；手机转横屏会让坐标失效（视频 App 自动全屏横屏还会打断投屏流）。
- DRM 保护的内容投屏为黑屏，无法绕过。
- 手机锁屏会挂起 USB（固件会回 `err phone usb asleep`）：请保持解锁，建议自动锁定设为"永不"。

## 原理深潜

实现原理、每个"坑"的根因与排查过程（mDNS/防火墙、D3D 渲染、命名管道、指针数学、闭环瞄准、时序常量……）都写在 **[docs/TECHNICAL.md](docs/TECHNICAL.md)**。

## 致谢与许可

- 上游项目：[onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)（MIT，© 2026 Henry Yuan）——本仓库的架构、固件与大部分服务端代码来自它；
- AirPlay 接收：[leapbtw/uxplay-windows](https://github.com/leapbtw/uxplay-windows)（第三方打包）与 [FDH2/UxPlay](https://github.com/FDH2/UxPlay)（引擎）；
- Apple Bonjour（mDNS 发现）、iOS 辅助触控（指针）；
- 本仓库新增/修改部分：© 2026 grandexecuti，MIT License（见 [LICENSE](LICENSE)）。
