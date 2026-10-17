# pocket-browser · 口袋里的浏览器

把手机 app 里已经存在的 `WKWebView`，接成一条受保护的远程调试/自动化通道。

指令从服务器发出，手机里的网页执行打开链接、运行 JS、截图、读取 DOM 等动作，结果原路传回。你的 app 仍然负责 WebView、登录态、数据存储和 UI；pocket-browser 只负责把“控制端”和“手机里的 WebView”连起来。

## 它解决什么问题

用无头浏览器（Playwright/Puppeteer）调试移动端页面、已登录页面或强依赖真实 WebKit 行为的页面时，经常会撞上两堵墙：

- **环境偏差**：数据中心 IP、桌面 UA、无头运行时和真实 iPhone 上的 WebKit 行为不一致。
- **常开成本**：要么养一台一直开着的机器，要么在自己电脑上挂个隧道，电脑一睡，链路就断。

pocket-browser 换了个思路：**执行端就用你随身的手机**。

- 真机、真 Safari 内核（WKWebView）、真移动 UA、真实网络环境。
- 你登录过的站点，cookie 就在这个 WebView 里，不需要在服务器上重新处理登录态。
- 手机本来就随身带、随时在线，不用额外养机器。

## 架构

```
  控制端 ──HTTP──▶  server  ──WebSocket──▶  手机 app 里的 WKWebView
 (脚本/agent)      (本文件)   (你搭的壳)        (真正干活的地方)
        ▲                                            │
        └──────────────── 结果原路返回 ───────────────┘
```

- **server**（`server/server.mjs`）：一个很薄的中转。手机通过 WebSocket 连上来注册（只保留最新一个连接）；控制端通过 HTTP `POST /pocket/cmd` 下指令，server 把指令转发给手机，等结果回来再返回。约 100 行，无状态。
- **手机 app**（`ios/PocketClient.swift`）：把你已有的 `WKWebView` 交给 WebSocket 客户端。收到指令 → 在 WebView 上执行 → 回传结果。参考实现一个类、一行接入。

## 适合接入什么样的 app

pocket-browser 不是一个完整浏览器壳，也不要求你新建 WebView。最适合的场景是：你的 app 里本来就有一个 Browser 页面，只缺一条受控的远程调试通道。

严格说，**任何你能持有引用并在主线程操作的 `WKWebView` 都可以接入**：

- 如果它只是登录页、帮助页、Web 内容页，pocket-browser 也能对当前页面执行 `js/html/screenshot`。
- 如果你想远程打开任意 URL、保留历史、管理 cookies、运行脚本、处理下载和弹窗，那就需要 app 侧本来有一个更完整的 Browser 壳。
- pocket-browser 不负责创建 tabs、地址栏、cookie UI、下载 UI 或指纹配置；这些应该留在你的 app/browser 模块里。

如果你还没有内置浏览器，可以先看这个参考实现：[satyricon-browser](https://github.com/Shitsuten/satyricon-browser) — 一个 iOS SwiftUI app 内 WKWebView 浏览器模块的实现教学，包含持久 cookie、bookmarklets、下载、历史、设置页和基础隐私加固。

接入时建议：

- 复用当前正在显示的 `WKWebView`，不要为了远程控制另起一个隐藏 WebView。
- 如果你希望保留登录态，用 `WKWebsiteDataStore.default()`；如果你希望一次性会话，用 non-persistent data store。
- token 放 Keychain 或你自己的 secret storage，不要写进 Swift 源码。
- 连接动作做成显式开关或调试设置项，不要在页面初始化/render 时自动连。
- 在 SwiftUI app 里，不要从 `body` 或计算属性里隐式创建 WebView；WebView 生命周期最好由 tab/session manager 管。

## 五个指令

一双手拆开来，就是这五件事：

| action | 作用 | 参数 |
|--------|------|------|
| `ping` | 心跳，确认手机在线 | — |
| `goto` | 打开一个 URL | `url` |
| `js` | 执行一段 JavaScript，返回结果 | `js` |
| `html` | 读取当前页面的完整 HTML | — |
| `screenshot` | 截图，返回 base64 PNG | — |

点赞、回复、发帖、翻页、抓取——凡是 `js` 能碰到的 DOM，都是这双手能伸到的地方。

## 快速开始

### 1. 起 server

```bash
npm install
cp .env.example .env      # 填写 POCKET_TOKEN 等
npm start
```

server 默认只监听 `127.0.0.1:3897`，通过 nginx 反代对外（见 `nginx.example.conf`，**注意 WebSocket 的 Upgrade 头**）。

### 2. 先用假手机跑通链路

真机接入前，先让一台「假手机」把 server 侧验证一遍：

```bash
npm run fake-phone
```

它会连上来、把每个指令都答对。这时候另开一个终端：

```bash
TOKEN=你的密钥
# 看手机在不在线
curl -s https://你的域名/pocket/status -H "Authorization: Bearer $TOKEN"
# 下一条 goto 指令
curl -s -X POST https://你的域名/pocket/cmd \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -d '{"action":"goto","url":"https://example.com"}'
```

链路通了，再换真机。

### 3. 接入真机

把 `ios/PocketClient.swift` 拖进你的 app，从 Keychain 或设置页读出 token，然后：

```swift
let pocket = PocketClient(
    webView: 你的WKWebView,
    serverURL: URL(string: "wss://你的域名/pocket/ws")!,
    token: tokenFromKeychain
)
pocket.connect()
```

就这一行。断线会自动指数退避重连。

## 后台保活

iOS 一旦把 app 切到后台，WebView 就被冻结，指令发过去没人执行。有解：

- 让 app 声明 `UIBackgroundModes: audio`，并让 WebView 里的页面**保持音频播放**（放首歌，或者一段静音循环当心跳）。系统认为你在后台放音乐，就不会冻结 app，WebView 跟着一起活着。

也就是说：手机在后台放着音频，这条调试通道就更不容易被系统冻结。这个做法适合自用/开发工具；上架 app 请按 Apple 后台能力规则审慎处理。

## 控制端调用示例

```bash
TOKEN=你的密钥
API=https://你的域名/pocket

# 打开一个页面
curl -s -X POST $API/cmd -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"action":"goto","url":"https://example.com"}'

# 执行 JS：点一个按钮
curl -s -X POST $API/cmd -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"action":"js","js":"document.querySelector(\"button\").click(); \"clicked\""}'

# 截图（截图耗时，把超时放大）
curl -s -X POST $API/cmd -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"action":"screenshot","timeout_ms":60000}'
```

## 安全须知

- **token 是唯一的门禁**。谁拿到 token，谁就能操控你手机里那个已登录的 WebView。别提交进仓库，别放公网明文，定期换。
- server 默认绑 `127.0.0.1`，**请走 nginx/HTTPS 反代**，不要把 3897 端口直接暴露公网。
- 这个 WebView 里是你的真实登录态。它能做的事，就是「一个坐在你手机前、已经登录了所有账号的人」能做的事——权限边界心里要有数。
- 仅用于操控**你自己拥有或已授权**的账号与站点。遵守目标站点的服务条款。
- 对公开部署，建议再加一层保护：IP allowlist、VPN、Basic Auth 或更短有效期的 token。
- 不要把截图 base64、大段 DOM、cookie 或 token 写进日志、issue、README、prompt 或 session summary。

## 更多文档

- [PROTOCOL.md](PROTOCOL.md) — HTTP/WebSocket 协议
- [nginx.example.conf](nginx.example.conf) — nginx 反代示例

## 附赠 skill

- [skills/x-surfing](skills/x-surfing/SKILL.md) — 用这条链路操作 x.com 的完整工艺手册（agent skill 格式）：发推、回复、回关、点赞、删推，以及每一条用翻车换来的"⚠️"。由一只每天在这条链路上冲浪的机器狗持续维护。

## License

GPL-3.0-or-later。见 [LICENSE](LICENSE)。
