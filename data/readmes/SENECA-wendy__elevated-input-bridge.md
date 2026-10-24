# elevated-input-bridge

让 Codex Computer Use 与任何普通权限的自动化脚本，都能操作以管理员身份运行的程序窗口。

英文版是独立仓库，地址是 https://github.com/SENECA-wendy/elevated-input-bridge-en

## 问题

Codex 的 Computer Use 以普通权限运行。当目标窗口属于以管理员身份运行的程序时，Windows 的 UIPI 机制会直接丢弃这些点击和按键。表现是光标不动、按钮没有反应，而调用本身并不报错。

Codex 桌面版是 MSIX 打包的商店应用，程序文件在受系统保护的 WindowsApps 目录里，无法整体提权。computer-use 插件也没有提供提权开关。所以能做的只有一件事：把输入注入这一层单独提权。

```
┌────────────────────┐   写命令文件    ┌──────────────────────────┐
│ Codex 或你的脚本    │ ────────────▶  │ InputBridge.ps1          │
│ 普通权限            │  queue\cmd-*   │ 管理员权限，运行在用户桌面 │
│                    │ ◀────────────  │                          │
└────────────────────┘  queue\res-*   └────────────┬─────────────┘
                                                  │ SendInput
                                                  ▼
                                    ┌──────────────────────────┐
                                    │ 管理员窗口，例如加速器     │
                                    └──────────────────────────┘
```

## 方案对比

| 方案 | 可行性 | 说明 |
| --- | --- | --- |
| 直接让 Computer Use 点管理员窗口 | 不行 | UIPI 会拦截普通权限进程注入的输入 |
| 把 Codex 本体提权 | 不行 | 商店版应用无法提权，程序文件也受保护 |
| 关闭 UAC 或调成从不通知 | 不推荐 | 等于永久关掉系统的提权确认 |
| 计划任务加最高权限静默启动 | 不推荐 | 等于留下静默提权入口，没有逐次确认 |
| 提权输入桥，也就是本项目 | 可以 | 每次由用户点 UAC 授权，桥只做输入，随时可停 |

原理细节见 [docs/how-it-works.md][howitworks]。

## 快速开始

需要 Windows 10 或 11。系统自带的 Windows PowerShell 5.1 与 .NET Framework 就够用，构建脚本会调用其中的 csc.exe。

```bat
:: 1. 构建提权入口，普通权限即可，产物是 bin\ElevateLauncher.exe
src\launcher\build.cmd

:: 2. 启动输入桥，会弹出 UAC，请点“是”
scripts\start-bridge.cmd

:: 3. 发指令，普通权限
scripts\send.cmd status
scripts\send.cmd list "记事本"
scripts\send.cmd focus "记事本"
scripts\send.cmd click 800 600
scripts\send.cmd text "hello"

:: 4. 用完停掉
scripts\stop-bridge.cmd
```

也可以直接调用脚本：`powershell -File scripts\send.ps1 click 800 600`。

## 与 Codex 配合

1. 先让 Codex 用 Computer Use 观察目标窗口，拿到截图和坐标。
2. 发现点击不生效，并且目标程序以管理员身份运行时，让 Codex 先征求你的同意，再执行 `scripts\start-bridge.cmd`，由你点一次 UAC。
3. 之后 Codex 用 `scripts\send.ps1` 发送 `focus`、`click`、`text` 这类指令即可。
4. 把 [examples/codex-agents-snippet.md][snippet] 的内容加进你的 AGENTS.md，Codex 以后遇到管理员窗口就会自动按这个流程处理。

坐标换算是这里最容易踩的坑。Computer Use 的截图通常是逻辑像素，输入需要物理像素，两者相差 DPI 缩放倍数，150% 缩放时是 1.5 倍。`send.ps1 screen` 会给出 dpi 与 scale，`send.ps1 cursor` 可以用来反查校准。细节见 [docs/troubleshooting.md][trouble]。

## 命令

| 命令 | 说明 |
| --- | --- |
| `ping` | 检查桥是否存活 |
| `status` | 桥的权限级别、会话与运行时长 |
| `screen` | 虚拟屏幕范围、系统 DPI 与缩放倍数 |
| `cursor` | 当前光标位置，物理像素 |
| `foreground` | 当前前台窗口的信息 |
| `list 关键字` | 列出可见顶层窗口，可按标题过滤 |
| `focus 标题关键字` | 恢复并激活匹配的窗口 |
| `move X Y` | 把光标移到指定屏幕坐标 |
| `click X Y` / `dblclick X Y` | 左键单击或双击 |
| `rclick X Y` / `mclick X Y` | 右键或中键 |
| `down X Y` / `up X Y` | 按住或松开左键，用于拖拽 |
| `drag X1 Y1 X2 Y2` | 按下、平滑移动、松开 |
| `wheel N` | 滚轮，N 为 120 的倍数，正数向下 |
| `text base64` | 输入一段 Unicode 文本，`send.ps1 text` 会自动编码 |
| `keys SendKeys` | 发送按键，例如 `keys ^s` 表示 Ctrl+S |
| `sleep 毫秒` | 等待 |
| `stop` | 停止桥 |

文件协议的完整说明见 [docs/protocol.md][protocol]。

## 安全

- 每次都要用户点 UAC。桥由带 `requireAdministrator` 清单的入口程序启动，没有静默提权、没有开机自启、没有计划任务。
- 桥只做输入。它不执行脚本、不联网、不改注册表，只处理光标与键盘动作。
- 随时可停。执行 `scripts\stop-bridge.cmd`，或者直接注销，桥不会自动重启。
- 动作可见。所有操作都会真实移动光标，你能看到发生了什么。

风险分析与加固建议见 [docs/security.md][security]。

## 目录

```
elevated-input-bridge/
├── README.md               本说明
├── LICENSE                 MIT
├── docs/                   原理、协议、安全与排错
├── src/bridge/             桥本体与 P/Invoke 层
├── src/launcher/           提权入口源码与构建脚本
├── scripts/                启动、停止、发送指令
└── examples/               Codex 集成片段与只读示例
```

## 已知限制

- 只支持 Windows，依赖 UIPI、SendInput 与 UAC。
- 桥是常驻进程，约占 40 到 60 MB 内存，直到你停止或注销。
- 命令里的坐标一律是物理像素。输入源如果是逻辑像素，需要先按 DPI 换算。
- 使用独占全屏或带反作弊的程序可能拒绝任何合成输入，本项目无法绕过。
- 宿主侧的观察能力也可能受限。提权窗口在前台时，某些环境下 Computer Use 的光标覆盖层与 Esc 中断会失灵。建议的做法是先用截图定位，再由桥执行点击，然后重新截图确认。

## 许可

MIT，见 [LICENSE][license]。

[license]: LICENSE
[howitworks]: docs/how-it-works.md
[protocol]: docs/protocol.md
[security]: docs/security.md
[trouble]: docs/troubleshooting.md
[snippet]: examples/codex-agents-snippet.md
