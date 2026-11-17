# 拉卡拉 CS80 客显屏 → Agent 状态副屏

一台 ¥39 的「拉卡拉客显屏 CS80」，**不改硬件**（原屏、原主板、原 Type-C/12V 供电，只刷固件），
改造成 800×1280 的副屏：多画布 + 组件拖拽编辑器 + 自定义页面 + 视频屏保，全部本地、无云依赖。

![参考效果](docs/assets/dashboard.jpg)

![架构](docs/assets/architecture.png)

一份 canvas 渲染代码同时是编辑器、预览和设备像素源：`host.py` 把浏览器算出来的像素
按 32×16 tile 差分推给 `qdc1`（独占 USB 的 C sidecar），后者 LZ4 压缩后走 QDC1 协议送到屏上；
数据源、屏保、音频都在 host 侧，整条链路本地闭环，不依赖任何云服务。

## 能做什么

| 能力 | 说明 |
|---|---|
| 画布 | 5×8 网格（每格 160 px），组件拖拽/缩放/复制，多画布 tab 切换 |
| 组件 | 时钟、时钟（表盘/LCD 数码管）、股票（A 股/美股/期货按时段自动切）、K 线、加密、GitHub、天气、电脑指标、Agent、RunCat、RunCat 条、音乐、倒计时、便签、资讯、假期倒计时、Home Assistant 概览 |
| 自定义页面 | 写一个 ES 模块直接画整屏（示例：自选股 + 分时图，见 `panel/web/pages/stock.js`） |
| Agent 状态 | 自动扫描本机 Pi / Claude Code / Codex / DeepSeek Harness 的会话，列表按「运行中 → 等待 → 结束」排序，可逐条隐藏 |
| 屏保 | 选视频（内置 `wallpaper.mp4`，也可用 `panel/add-screensaver.sh` 转自己的），手动播或锁屏自动播 |
| 控屏 | 亮度（5–100）、待机/唤醒、设备状态回读 |
| 喇叭 | 独立「音频播放」面板：任意格式（WAV / FLAC / M4A / OGG / 视频音轨…）→ ffmpeg 转 128 kbps MP3 再上传（≤4 MiB），音量 / 停止 / 播放自愈；固件只解 MP3，转码在主机侧，PLAY 撞到 BAD_STATE 会自动修音频路由后重试 |
| 自检 | 每帧用 `VERIFY` 回读设备 framebuffer 哈希，patch 链哈希必须对上才算成功 |
| Home Assistant | 5×2 全屋概览：室内温度/湿度、室外天气、空调、开关/插座、功率、音箱；走本机 HA REST API，token 只留在 host，组件只传 entity_id |

## 一键刷机（新买设备 / 给别人用）

不用看文档、不用装 Python：**把设备插好，双击仓库根目录的 `一键刷机.cmd`**。

前置就三样：**Windows 10/11 x64** + **能传数据的 Type-C 线** + **DC 12V/2A 电源**。
（缺 Quectel USB 驱动时脚本会自己解压 `quectel-usb-driver.zip` 并弹一次 UAC 代装；
便携 Python 首次运行会自动解压到 `win-flash/flash/py/`，已经随仓库带着。）

它会先探设备，再按实际情况选路：

| 设备当前状态 | 脚本动作 | 耗时 |
|---|---|---|
| 已经是 QDisplay（QDC1 应答） | 只报 `block` / `features`，不动它 | 5 s |
| R03 基带（`…03A04M08_OCPU_QPY`） | 只写 APP 分区 | ~30 s |
| R05 / 拉卡拉 1.6 出厂（`…05A01M08_OPU_BETA1215`） | 整片 8 MiB 备份 → 刷 `fw.pac` 降到 R03 → 再写 APP | ~15 min |
| 完全没设备 / Error 43 | 打印「线 / 供电 / 驱动 / HUB」四步排查，缺驱动可代装 | — |

命令行等价写法（不想双击时用）：

```bat
cd win-flash\flash
py\python.exe flash_oneclick.py --dry-run   :: 只看诊断和计划，不动设备
py\python.exe flash_oneclick.py             :: 刷（刷前确认一次）
py\python.exe flash_oneclick.py --yes       :: 全自动
```

刷完看画面：`panel\run-windows.cmd`，或直接双击打包好的 `cs80-panel.exe`。
日志与原厂备份都在 `win-flash/dumps/`（备份的才是刷机前那一份，别删）。
细节见 [`docs/firmware.md`](docs/firmware.md) §0.6；为什么要先降级见 §0.5。

## 买第二台设备怎么接（10 步）

> 只想把设备刷成副屏：直接用上面的 `一键刷机.cmd`，下面 10 步是手工版/排障用。
> 全流程只在 **Windows + macOS** 走通过；刷机只有 Windows 能做（macOS 上 BootROM 口被拒）。

1. **确认是同款**：主板丝印 `CS80 MB V10`，屏 FPC `H.101.001B02`，模组 `EC600UCNLBR03A04M08`。
   细节见 [`docs/hardware.md`](docs/hardware.md)。
   **还要看固件代次**：`ATI` 回 `EC600UCNLBR03A04M08_OCPU_QPY`、设备管理器里有 `MI_20`（if32）才是可直接刷的那代；
   若是 `EC600UCNLBR05A01M08_OCPU_BETA1215`（拉卡拉 1.6，8 个接口、无 `MI_20`），直接刷会黑屏，
   要先 `flash_at.py` 降级到 R03（先 `dump_flash.py` 整片备份）——见 [`docs/firmware.md`](docs/firmware.md) §0.5。
2. **Windows 上刷 QDisplay 固件**（只写 APP 分区，不动 NV）：
   `cd win-flash/flash && py\python.exe qdisplay_app.py ..\..\win-display\qdisplay\qdisplay_native.bin --auto`
   完整前置/流程/坑：[`docs/firmware.md`](docs/firmware.md)。
3. **验证固件**：屏上应该显示内置的「等待连接」页；客户端连上后会报 `block=520192`、特性位 `0x23f`。
4. **拷贝 `panel/` 到目标机器**，编译 sidecar：
   - macOS：`clang -O2 -o panel/qdc1 panel/qdc1.c panel/lz4.c -framework IOKit -framework CoreFoundation`
   - Windows：`cl qdc1.c lz4.c /Fe:qdc1.exe`（详见 [`docs/windows.md`](docs/windows.md)）
5. **确认数据通道**：
   - macOS：固定走 **USB 接口 32**（IOKit，免 root），不用做任何事
   - Windows：`qdc1.exe --probe` 找哪个 COM 口回 QDC1 HELLO，然后 `set CS80_COM=COMxx`
6. **起 host**：`python3 panel/host.py`（或直接跑打包好的桌面壳，它会自己拉起 host）。
7. **确认在线**：`curl 127.0.0.1:8787/api/status` → `device=up`、`ready.block=520192`。
8. **打包桌面壳**（可选）：`cd panel/shell && npm i && npx tauri build` → `.app` / `.msi`。
   新增 `panel/web/**` 文件时记得同步 `src-tauri/tauri.conf.json` 的 `bundle.resources`。
9. **校屏**：亮度想完全不闪就设 100（`<100` 时固件用 1 kHz 软件 PWM 调光，中间灰会轻微抖）；
   host 会**记住你设的亮度**（`~/.cs80_panel/config.json`，断电重连后自动恢复），不再自己刷成 100。
   要强制锁死某个值就 `set CS80_BRIGHTNESS=100`。再检查 `VERIFY` 是否一致（不一致说明像素格式或字节序错）。
   屏自身在闪：按 [`docs/troubleshooting.md`](docs/troubleshooting.md#屏闪) 的四步定位；
   如果是 0.3.1 固件等待页每秒一下，用 `win-flash/flash/patch_waiting_page.py` 打补丁。
10. **长期运行**：桌面壳带托盘 + 关窗不退出 + host 监督线程（host 死了自动重启）；
    开机自启用系统登录项。

## Linux（无桌面 / usbfs）

Linux 上没有 IOKit，`libusb` 又因为内部 32 位接口位图**打不开接口 32**（`LIBUSB_ERROR_INVALID_PARAM`），
所以 sidecar 直接用 usbfs ioctl。`qdc1.c` 已带 `__linux__` 分支：自动按 VID:PID 找 `/dev/bus/usb/BBB/DDD`，
用 `USBDEVFS_DISCONNECT_CLAIM` 踢掉 `option` 驱动并 claim 接口 32，再走 `USBDEVFS_BULK`。

```bash
cd panel
gcc -O2 -o qdc1 qdc1.c lz4.c
./qdc1 --hello                     # {"qdc1":true,"block":520192}
```

无桌面常驻：编辑器只负责改布局，后台 kiosk 负责持续推帧（关掉浏览器也不影响屏）。

```bash
sudo install -m 644 deploy/99-cs80.rules /etc/udev/rules.d/
sudo install -m 644 deploy/cs80-panel.service deploy/cs80-kiosk.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now cs80-panel cs80-kiosk
```

- `cs80-panel`：`host.py --host 0.0.0.0 --port 8787`，局域网编辑器入口。
- `cs80-kiosk`：`panel/kiosk-guard.sh` 拉起 Chromium headless 打开 `http://127.0.0.1:8787/?kiosk=1` 持续渲染推帧。
  - 用 Playwright 的 **chrome-headless-shell**（不是完整 Chrome）：它没有窗口/遮挡，不会把页面当后台节流。
  - unit 里仍带 `--disable-background-timer-throttling` 等参数，双保险。
  - 页面每 5 秒 POST `/api/heartbeat`；guard 查 `/api/health` 的 `beat_age`，连续两次 >30 s 就重启 Chromium
    （进程活着但页面被冻结时，systemd 的 `Restart=` 是发现不了的）。
  - 编辑器改完布局后 kiosk **原地重建画布**（`reloadLayout()`），不再整页 reload，省掉 2~5 秒空档。
  - Chromium 路径按本机 Playwright 安装位置写在脚本里，换机器改 `CS80_CHROME` 或脚本默认值。
- Linux 上不带 `?kiosk=1` 的页面默认只编辑、不推帧（按钮显示“后台推送中”），避免和 kiosk 抢帧。
- 需要 root，或给 `2c7c:0901` 加 udev 规则；首次 claim 会把接口 32 从 `option` 驱动摘下来（`ttyUSB6` 消失），属正常。
- 界面无鉴权，`--host 0.0.0.0` 仅限可信内网；外网用 `ssh -L 8787:127.0.0.1:8787`。
- Linux 下锁屏/显示器休眠联动不可用，其余功能（帧、patch、屏保、音频）一致。
- **USB 速率**：`/api/status` 的 `usb.speed` 是 480 才是高速；如果是 12（全速），整帧 2 MB 要 1.5~2.5 s，
  屏幕每次重连都会顿一下。优先直插主机 USB 口、换好线，别挂两层 HUB；本机就是重插一次后从 12 恢复到 480 的。
- **推帧卡死**：host 的发送队列只有 4 条 + sidecar 每 patch 后 50 ms 限速，设备慢时宁可返回 `ok:false`
  让前端下一轮合并重试，不会把几十条 patch 一口气灌给固件。连续 6 次推帧失败会在 UI 标
  `needs_replug`：固件接收状态机卡死只能拔插 Type-C 重新枚举（不要用软件 USB reset，可能把固件 USB 功能复位死）。

## 已验证的现状

| 项 | 值 |
|---|---|
| 设备 | CS80 + EC600U-CN（UIS8910），QDisplay native 固件写在 `0x60260000` |
| 主机 | macOS（arm64，本仓主力）、Windows（见 `docs/windows.md`，需你实机确认 COM 映射） |
| 传输 | macOS IOKit 接口 32 / Windows 厂商虚拟串口，QDC1 协议 |
| 带宽 | 实测 **10.5 MB/s**（整帧裸 2 MB → 195 ms；LZ4 后 ~50 KB → 20 ms） |
| 常态刷新 | 局部 patch **64 B / 1–2 ms**；屏保视频 12 fps（250 KB/帧、59 ms/帧） |
| Linux 实测 | 重插后 480 Mbps：整帧 2 MB ≈ 0.2 s；曾枚举成 12 Mbps（全速，整帧 ≈ 1.7 s，`usb.speed` 可见） |
| 已知固件坑 | 个别整帧/局部包 LZ4 解不动（3 s 接收超时，`status=8`）：patch 自动原地重试 3 次；整帧在全速链路上直接走裸块 |
| 恢复 | `win-flash/flash/fw.pac` 可整包刷回 QuecPython |
| 新批次（R05） | 出厂是拉卡拉 1.6 固件（8 接口、APP 区非 `2PPA`），QDisplay 刷不进去 → 用 `dump_flash.py` 备份后 `flash_at.py` 降级到 R03，再刷 QDisplay。2026-11 同款新机实测通过 |

## 目录

```
docs/                文档（硬件 / 固件 / 协议 / 排障 / 走过的死路 / Windows）
  assets/            文档用图（架构图 .drawio 源 + PNG、默认看板、引脚图、界面截图）
panel/               客户端：host.py（常驻）+ web/（画布编辑器）+ qdc1.c（USB sidecar）+ shell/（Tauri 壳）
  run.sh             macOS 启动脚本（host + Chrome 应用窗口）
  run-windows.cmd    Windows 启动脚本（host + Edge/Chrome 应用窗口，无需 Rust）
  qdc1_ping.py       QDC1 探活/状态查询（刷机后验证固件跑起来没有）
  flicker_probe.py   屏闪探针：整屏纯色 + 可调重复提交频率
  kiosk-guard.sh     Linux 无桌面：拉起/守护 headless Chromium 持续推帧
win-flash/           刷机与恢复工具 + 官方 QuecPython 固件包（新设备必需）
  flash_oneclick.py         一键刷机（判代次 + 备份 + 降级 + 刷 APP + 验证）
  flash/appimg.py            APP2 容器 CRC32（手改固件字节后必须重算）
  flash/make_waiting_page.py 生成等待页（纯黑白，不闪）
  flash/patch_waiting_page_image.py  把生成的页面换进固件 BIN
  flash/patch_waiting_page.py        0.3.1 等待页倒计时重绘补丁
  flash/reset_download.py    卡在下载模式时用 BSL 复位（不用拔插）
  flash/flash_at.py          R05 新批次（拉卡拉 1.6）降级到 R03 的基带刷写
  flash/dump_flash.py        整片 8 MiB 备份 / 裸写回滚（降级基带前必做）
  dumps/                     刷机前备份的固件 + 刷机日志（.gitignore，不进仓库）
一键刷机.cmd       双击即刷（自动解压便携 Python → flash_oneclick.py）
win-display/         官方 Windows 上位机安装包 + 固件 bin（0.3.0 / 0.3.1）+ 摄像头验证脚本
deploy/              Linux 部署：udev 规则 + systemd（host / kiosk）
archive/quecpython/  QuecPython 时代的工具（历史留档，见 docs/dead-ends.md）
```

## 文档索引

| 文档 | 什么时候看 |
|---|---|
| [`docs/hardware.md`](docs/hardware.md) | 换设备/查引脚/要写自己的固件时 |
| [`docs/firmware.md`](docs/firmware.md) | 刷固件、恢复 QuecPython |
| [`docs/protocol.md`](docs/protocol.md) | 要写别的客户端（Linux/手机/单片机） |
| [`docs/troubleshooting.md`](docs/troubleshooting.md) | 屏不亮/掉线/画面不更新 |
| [`docs/windows.md`](docs/windows.md) | Windows 上编译 sidecar、找 COM 口、验收清单 |
| [`docs/dead-ends.md`](docs/dead-ends.md) | 别重复踩的坑（含为什么放弃 QuecPython） |
| [`panel/README.md`](panel/README.md) | 客户端架构、组件、页面、配置项 |

## 素材与许可

- 猫素材：[runcat-dev/RunCat365](https://github.com/runcat-dev/RunCat365) 的 `cat_running_*.png`（Apache-2.0）
- Agent logo：Pi / Claude / OpenAI 取自 [warp](https://github.com/warpdotdev/warp)（其仓库内资源），DeepSeek 取自 [simple-icons](https://github.com/simple-icons/simple-icons)
- 农历表：[solarlunar](https://www.npmjs.com/package/solarlunar)（ISC）
- 网格交互：[gridstack.js](https://github.com/gridstack/gridstack.js)（MIT）
- 设计语言参考：[glanceapp/glance](https://github.com/glanceapp/glance)
- 固件与协议逆向：[StevenLang233/lakala-display-re](https://github.com/StevenLang233/lakala-display-re)

屏保视频 `panel/web/media/wallpaper.mp4` 为用户自带素材，未包含在上述开源许可内。
