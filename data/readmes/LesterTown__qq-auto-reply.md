# dsh-qq-local

**让你的 DeepSeek Harness（DSH）用你自己已登录的 QQ 账号，跟好友自动聊天。**

不接协议、不注入客户端，只用 **屏幕 OCR + CGEvent 模拟键鼠**——把「人手操作 QQ」这件事自动化。

> 零协议 · 零注入 · 不触发风控封号 · 天然可迁移到微信 / 飞书 / 钉钉

---

## 为什么是「操控界面」而不是「接协议」

现成的 QQ 机器人方案（OneBot / NapCat / Lagrange / 官方机器人）要么**只能用小号**、要么有真实的**封号风险**，微信侧（iLink / WeChatFerry / UIA）也全是逆向注入、README 普遍写着「当一次性号用」。

这个插件换了个思路：

| | 协议 / 注入方案 | 本插件 |
|---|---|---|
| 用谁的号 | 小号（主号有风控风险） | **你自己的主号** |
| 依赖 | NapCat / 注入 DLL / 逆向协议 | 无，只要 QQ 窗口在你屏幕上 |
| 封号风险 | 有（实测有掉线/冻结案例） | 无（对 QQ 来说就是人在点鼠标） |
| 跨平台 | Windows 优先 | macOS（其它系统换掉 swift 小工具即可） |
| 跨 IM | 一平台一套 | 同一套逻辑可复用到微信等 |

代价是：它只能和你**屏幕上看得见**的东西打交道，所以必须有一块不被遮挡的 QQ 窗口。

## 工作原理

```
每 5s 心跳 → 读开关（enabled）
   └─ 开了 → 距上轮 ≥ intervalSec ?
        └─ tick:
           1. 激活 QQ（轮询 frontmost，确保真的到前台）
           2. 读窗口位置 → 按分数偏移算出「聊天区 / 输入框」坐标（窗口随便拖都自适应）
           3. 在左栏按备注名点开好友聊天
           4. 截整个窗口 → Vision OCR → 过滤出聊天区 → 取底部最新一条消息
           5. 与 watermark（上一条已知消息）比对：相同 = 没有新消息，跳过
           6. 不同 → 调 LLM 生成一两句回复 → 点输入框 → ⌘A → 粘贴 → 回车发送
           7. 更新 watermark，写入 state.json
```

首次运行只记录基线、不回复，避免一开机把历史消息全「回」一遍。

## 安装

前提：DSH 桌面端、macOS、已登录且窗口可见的 QQ（新版 NT）。

```bash
git clone <this repo> ~/dsh-qq-local
dsh plugin --profile desktop add ~/dsh-qq-local
```

然后用 **⌘Q** 完全退出 DeepSeek Harness 再打开（或在设置里改一次配置文件触发热重载），
到「设置 → QQ 本地自动回复」面板里填好友备注名、打开总开关即可。

> `link:` 安装是符号链接，Node 会从插件**真实路径**解析依赖，而不是从 profile 的
> `node_modules`。若报 `ERR_MODULE_NOT_FOUND: @deepseek-ai/schemastery`，跑一次：
>
> ```bash
> bash scripts/link-peers.sh      # 读取 DSH_PROFILE_DIR，默认 ~/.dsh/profiles/desktop
> ```

## 配置（设置面板）

| 键 | 默认 | 说明 |
|---|---|---|
| `enabled` | `false` | **总开关**，改了立即生效（volatile 热更新，不用重启） |
| `target` | 空 | 要自动回复的好友**备注名**，随时改、下一轮生效；空则跳过 |
| `intervalSec` | `60` | 检查间隔（秒），最小 5 |
| `model` | `deepseek-v4-pro` | 用哪个模型回复（换便宜的能省钱） |
| `persona` | 通用朋友口吻 | 回复用的 system prompt，随便写人设 |
| `regionXFrac` 等 6 项 | 见代码 | 聊天区 / 输入框相对窗口的分数偏移，一般不用动 |

另外插件注册了一个 `qq_send` 工具：可以让 agent 主动给**任意**好友发一条消息（临时指定 `target`），
不影响自动回复目标。

> 配置项必须标 `.volatile()` 才会出现在设置页，且 volatile 改动**不会重挂插件**——
> 所以轮询是「常驻心跳 + 每轮现读开关」，不是启动时判断一次。

## 需要的系统权限

在「系统设置 → 隐私与安全性」里给 **DeepSeek Harness** 打开：

- **屏幕录制** —— 截图 + OCR
- **辅助功能** —— CGEvent 模拟鼠标 / 键盘
- **自动化 → System Events** —— 回车发送、⌘A/⌘V（macOS 偶尔会自己重置，表现为 `-10004 权限违例`）

## 调试

```bash
DSH_QQ_LOCAL_DEBUG=1   # 打开后会把每轮 tick 的窗口/OCR/LLM 详情写进 <dataDir>/trace.log
```

数据目录：`$DSH_QQ_LOCAL_DATA` → `<baseDir>/dsh-qq-local` → `~/.dsh/dsh-qq-local`。

## 已知限制

- **别在自动回复开着的时候手动操作 QQ**：插件靠点击和截图驱动真实窗口，人机抢焦点会点错人/截到空白（每轮已做「重新激活 + 重读窗口 + 重试」缓解）。
- watermark 只比「底部消息」，不区分左右归属：你自己手动发的消息可能被当成新消息回一次。
- 表情包 / 图片读不到文字，只能收到「[动画表情]」这类占位。
- 只支持 macOS（Windows 需要把 `scripts/*.swift` 换成等价的 Win32 自动化）。
- QQ 窗口被最小化/隐藏时本轮跳过。

## Roadmap

- [ ] 消息左右归属判定（区分「对方发的」和「自己手打的」）
- [ ] 图片消息：OCR 兜底 / 多模态识别
- [ ] **跨 IM 统一底座**：QQ + 微信同一套人设、记忆、会话
- [ ] 可选：把 swift 小工具换成内置 Node 原生调用，减少外部依赖

## English

`dsh-qq-local` is a [DeepSeek Harness](https://github.com/deepseek-ai) plugin that lets your own logged-in
QQ desktop client auto-reply to a friend. It drives the real UI (screen capture + OCR + CGEvent) instead of
speaking the QQ protocol, so there is no injection and no account-ban risk. A single toggle in the DSH
settings page turns it on; it then polls every `intervalSec`, detects the newest message via OCR, asks an LLM
for a short reply, and types it back with a synthetic paste + Enter.

## License

MIT
