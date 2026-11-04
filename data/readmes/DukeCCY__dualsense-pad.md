# dualsense-pad

> 给住在电脑里的角色加一层触觉：把 PS5 手柄的触摸板变成一块 250 Hz 的二维输入，
> 手势识别、震动、灯条全走本地 HTTP。零依赖，不联网，只做协议翻译。
>
> *A sense of touch for the character that lives in your computer: turn a DualSense
> touchpad into a 250 Hz input surface — gestures, haptics and lightbar over a local HTTP API.*

<p align="center">
  <img src="docs/demo.png" width="500" alt="状态面板：实时坐标、分区、速度、手势与事件列表">
  <img src="docs/zones.png" width="228" alt="分区视图：把人形剪影按身高切成若干部位">
</p>

把 **PS5 DualSense 手柄的触摸板**当成一块 1920×1080 的二维输入设备来用：
读取手指位置与轨迹、把手势和震动/灯条写回手柄，并通过一个本地 HTTP 服务
把状态暴露给任意前端（网页、桌面挂件、游戏、脚本都行）。

零依赖 —— 只用 Python 标准库（`ctypes` 调系统 DLL），不需要 hidapi，
不需要装驱动，不需要管理员权限。

```
pip install 不需要
python -m dualsense_pad list      # 先看有没有认出设备
python -m dualsense_pad serve     # 起服务，然后浏览器打开 examples/web_demo.html
```

---

## 为什么做这个

现在挺流行在自己电脑上"养"一个角色：接进 QQ 或微信当机器人、做成桌面挂件常驻在角落、
或者挂一个随时喊得出来的语音助手 —— 也有人干脆养一只住在电脑里的大肥鱼。

入口不一样，底下是同一件事：用 DeepSeek Harness 这类本地 agent 运行时搭一个角色，
让它常驻、有记忆、能自己主动说话。"听"和"说"这条路已经通了，
唯独缺一件事：**被碰到**。

麦克风听得见声音，但听不出"手在背上慢慢往下滑"。于是永远隔着一层屏幕 ——
你看得见它，它看不见你。

DualSense 的触摸板正好补这一段：一块 40 × 25 mm 的连续输入面，有位置、有速度、
有轨迹、有停留，全是原始信号，不需要任何识别模型。手指的动作翻译成一条事件推给角色，
角色的反应再用震动和灯条回到手上，这一圈就闭合了。

所以这里的定位不是"手柄工具"，而是：

> **给住在电脑里的角色，加一层触觉。**

一条典型链路：

```
DualSense 触摸板
   ↓   250 Hz 坐标 / 手势
dualsense_pad serve          ← 本项目：只做翻译
   ↓   HTTP /state，或 webhook 事件
你的 agent / 角色运行时       ← 决定要不要回应、怎么回应
   ↓
震动 + 灯条  ←── 回手
```

本项目只负责中间那一段：把手指的动作翻译成结构化事件。它不判断"这是谁"，
也不决定"该不该有反应"。回手的方向留了两个出口（`/pulse`、`/light`），
给什么反馈由上层自己定。

分层的好处很实际：协议解析、重复帧、坐标系这些烦人的东西只写一次，
上面换角色、换模型、换玩法都不用再碰底层。

超出"通用工具"的部分一个没留：**没有角色数据、不做身份判断、不联网**，
出口只有一个本地 HTTP 端口（见 [它不做什么](#它不做什么)）。

---

## 它能做什么

| 能力 | 说明 |
|---|---|
| 触摸位置 | 250Hz 读原始坐标（1920×1080），单指 / 双指 |
| 手势识别 | 点 / 拍 / 划 / 抚摸 / 画圈 / 双指捏 / 双指撑 |
| 坐标映射 | 横向或竖向，可翻转，可缩放到任意子矩形，可自定义分区 |
| 震动 | 两路马达（高频 / 低频），支持"跟随手速"的节奏反馈 |
| 灯条 | 任意 RGB，带待机色 |
| 按键 | 15 个键位，含 L2 / R2 的 0–255 模拟量 |
| 接管开关 | 一条 URL 把设备完全放开给其他程序（进游戏前用） |
| 事件外推 | 一段触摸结束后 POST 到你的 webhook，默认关闭 |

## 它不做什么

* **不是驱动**，不装虚拟手柄，不拦截其他程序的输入。
* **不跨平台** —— 目前只有 Windows 后端（`setupapi` / `hid.dll`）。
  报文解析、手势、输出报文、坐标映射都是纯 Python，换平台只需重写 `hid.py`。
* **不做识别** —— 它只告诉你"手指在做什么"，不判断"这是谁"。

---

## 环境要求

| 项 | 要求 |
|---|---|
| 系统 | **Windows 10 / 11**（只有 Windows 后端） |
| Python | **3.9+**（只用标准库，不用装任何包） |
| 硬件 | 一个 **DualSense**（PS5 手柄），USB 线或 USB 无线转发方案 |
| 连接 | **必须是 USB 形态**（见下），蓝牙直连不支持 |

没有手柄也能跑单元测试（不碰硬件）：

```bash
python -m unittest discover -s tests
```

### 连接方式：只支持 USB 报文

程序只认 **USB 输入报文**（report id `0x01`，64 字节，触摸起点第 33 字节）。

| 接法 | 支持 | 说明 |
|---|---|---|
| USB 线直连 | ✅ 应当可用（**未实测**） | 系统里出现 `mi_03` 接口 |
| USB 无线接收方案 | ✅ **已实测其中一种** | 自制板子转发、市售 dongle 都算，见下 |
| 蓝牙直连（配对到主板蓝牙） | ❌ **不支持** | 蓝牙是 report id `0x31`，所有字段偏移整体后移，本程序没有对应解析 |

**关于「接收器」**：无线接收的做法不止一种 —— 用板子（例如树莓派）把蓝牙转成 USB HID、
买现成的 dongle，都能走通。**本程序不认具体型号，只认两件事：**

1. 系统里出现 `054C:0CE6`（DualSense Edge 是 `0DF2`）
2. 带 `mi_03` 接口，且 `touch` 能读出坐标

两条满足就能用，否则不行。所以别去对型号，按这两条自己验一遍最快。
本项目只在**其中一种**转发方案上实测过；换别的方案理论等价，但没有逐一验证。

**怎么判断自己是哪种**：`python -m dualsense_pad list`，看到 `mi_03` 就是 USB 形态。
蓝牙直连时可能只有 `mi_05` 之类，此时 `serve` 会打印一条警告，读到的坐标是无效的。

另外，程序按 **VID `054C` + PID `0CE6`（或 Edge 的 `0DF2`）** 找设备。
如果你的转发方案把设备重新枚举成了别的 VID/PID，会「找不到手柄」——
那是转发方案的问题，不是代码的问题。

---

## 哪些跑过、哪些没跑过

写清楚是为了不让人踩空。**已实测**是在 Windows 11 + DualSense 经一种 USB 无线转发方案下做的：

| 能力 | 状态 |
|---|---|
| `list` 设备识别 | ✅ 实测 |
| 250Hz 读坐标、单指 / 双指 | ✅ 实测 |
| 8 类手势（点/拍/划/蹭/圈/捏/撑/双指） | ✅ 实测，逐个人工验证 |
| 15 个键位（含 L2/R2 模拟量） | ✅ 实测 |
| 震动（跟随手速 + 脉冲） | ✅ 实测 |
| 灯条（任意 RGB + 待机色） | ✅ 实测 |
| `serve` 全部端点 + webhook 投递 | ✅ 实测 |
| 自定义分区 JSON、配置 JSON | ✅ 实测 |
| 单元测试 23 条 | ✅ 全过 |
| **USB 线直连** | ⚠️ 未实测（预计与转发方案相同） |
| **蓝牙直连** | ❌ 不支持（报文格式不同） |
| **`--horizontal` 横向模式** | ⚠️ 未实测 |
| **`--no-flip-u` / `--flip-v` 翻转** | ⚠️ 未实测 |
| **`examples/web_demo.html` 页面** | ⚠️ 未在浏览器里跑过（背后的 API 与跨域头已验） |
| **`touch` / `buttons` 子命令** | ⚠️ 未实测（只跑过 `list`） |
| **Linux / macOS** | ❌ 没有后端 |

---

## 快速开始

### 1. 确认设备

```bash
python -m dualsense_pad list
```

```
找到 2 个 Sony HID 接口：
  054C:0CE6  DualSense       \\?\hid#vid_054c&pid_0ce6&mi_03#...  ← 触摸板
  054C:0CE6  DualSense       \\?\hid#vid_054c&pid_0ce6&mi_05#...
```

一个 DualSense 会暴露多个 HID 接口。**触摸板和传感器在 `mi_03` 上**，
程序会自动挑这一个。

### 2. 单独验触摸

```bash
python -m dualsense_pad touch
```

```
触点1 按 ( 480,  120)
触点1 按 ( 512,  160)
```

如果坐标全乱、位置对不上，先读 [PROTOCOL.md](PROTOCOL.md) 里
"触摸数据从第 33 字节开始"那一节。

### 3. 起服务

```bash
python -m dualsense_pad serve --settle 1.5 --gain 1.0
```

然后打开 `examples/web_demo.html`（直接双击即可，它 `fetch` 本地 7778）。

### 4. 接你自己的程序

前端轮询 `/state`：

```js
const s = await (await fetch('http://127.0.0.1:7778/state')).json();
// s = { active, nx, ny, two, gap, sp, amp, duty, gesture, btn, ... }
```

或者让服务把"一段操作结束了"推给你：

```bash
python -m dualsense_pad serve --webhook http://127.0.0.1:9000/on-pad
```

```json
{
  "type": "touch",
  "gesture": "stroke",
  "zone": "chest",
  "nx": 0.18,
  "ny": 0.42,
  "dur": 3.21,
  "path": 96.4,
  "span": 71.2,
  "speed": 30.0,
  "at": 1730000000.0
}
```

---

## HTTP 端点

| 端点 | 作用 |
|---|---|
| `GET /state` | 当前状态快照，建议 30–60ms 轮询一次 |
| `GET /events` | 最近 40 条已落定事件 |
| `GET /health` | 设备名、回手是否可用、接管状态、分区表 |
| `GET /takeover?on=0` | 放开设备（进游戏前）；`on=1` 收回 |
| `GET /gain?n=1.5` | 震动总强度倍率 0–2.5 |
| `GET /light?r=255&g=0&b=0` | 直接设灯条 |
| `GET /pulse?w=120&s=80&ms=120` | 来一记震动 |

只监听 `127.0.0.1`，不对外。

## 命令行参数

```
serve
  --config FILE        JSON 配置。不给时，当前目录有 config.json 就自动用它
  --port 7778          端口
  --settle 1.5         停手多久算一段结束（秒）。调大减少碎片事件，代价是反应变慢
  --gain 1.0           震动总强度倍率
  --webhook URL        事件落定时 POST 过去
  --zones FILE         分区配置（见 examples/zones_humanoid.json）
  --horizontal         横向使用（默认竖向）
  --vertical           竖向使用（覆盖配置里的 vertical=false）
  --no-flip-u          不翻转横向
  --flip-u             翻转横向（覆盖配置里的 flip_u=false）
  --flip-v             翻转纵向
```

**优先级：命令行 > 配置文件 > 内置默认值。** 配置文件只写你想改的字段就行，
不用抄全；完整字段见 `examples/config.example.json`。

```bash
cp examples/config.example.json config.json   # 改完直接 serve，会自动读到
python -m dualsense_pad serve
```

---

## 三个容易卡住的地方

### 灯条不亮，但震动正常

输出报文的**第 2 字节**（使能位 2）决定了这一帧要不要动灯条：

* `0x04` = 允许改灯条颜色
* `0x08` = **重置灯条**（灯灭）

写成 `0x08` 时，后面 RGB 填什么都没用，灯永远是灭的。而震动看的是第 1 字节，
所以会出现"震动好使、灯死活不亮"的现象。

### 灯亮了一下就灭

刷新震动时发的那一帧如果没带当前颜色（RGB 全 0），就会把刚点亮的灯刷黑。
每一帧输出都必须同时带上马达值和当前颜色，两边共用同一份状态。

### 震感不跟手速走

先确认速度算对了：`/state` 里的 `sp` 会显示当前速度（mm/s）。
如果手指慢慢划 `sp` 也顶到几百，那是速度窗口太短 —— 250Hz 下"最后两三帧"
只有 10 毫秒，抖动就能算出高速。用 100–150ms 的滑动窗口做平均。

如果 `sp` 会变、手上感觉不变，那是振幅的问题：这类马达在低段几乎没有区分度，
把数字从 12 调到 50 手感差不多。改用**时间域** —— 同样振幅，靠"通电占比"
表达快慢（慢 = 断续轻颤，快 = 连续），差别会明显得多。

---

## 目录结构

```
dualsense_pad/
  hid.py        设备枚举、打开、读报文（Windows）
  report.py     输入报文解析（纯函数，可跨平台单测）
  output.py     输出报文 / 马达 / 灯条
  gestures.py   手势分类
  mapping.py    坐标映射与分区
  server.py     本地 HTTP 服务
  cli.py        命令行
examples/
  web_demo.html         状态面板
  config.example.json   配置样例
  zones_humanoid.json   按身高分段的样例
docs/
  demo.png              状态面板截图
  zones.png             分区视图截图
```

## 协议细节

报文的全部偏移、使能位含义、以及每条结论是怎么验证出来的，见
[PROTOCOL.md](PROTOCOL.md)。改解析代码之前建议先读一遍。

## 许可

MIT。见 [LICENSE](LICENSE)。
