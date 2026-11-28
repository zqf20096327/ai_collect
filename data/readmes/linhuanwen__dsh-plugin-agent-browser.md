<div align="center">

<img src="docs/assets/icon.svg" width="84" alt="agent browser panel" />

# DSH-Agent 侧边自动化操作浏览器

**在 DeepSeek Harness 的右侧栏里，让 Agent 用你的真浏览器干活：它看得见、点得动，你随时可以接管。**

`dsh-plugin-agent-browser` · DSH 桌面端插件

<p>
  <img alt="version 1.5.24" src="https://img.shields.io/badge/version-1.5.24-2563eb?style=flat-square" />
  <img alt="DSH 0.2.2 - 0.3.0" src="https://img.shields.io/badge/DSH-0.2.2%20~%200.3.0-1d4ed8?style=flat-square" />
  <img alt="17 tools" src="https://img.shields.io/badge/tools-17-0f766e?style=flat-square" />
  <img alt="421 tests passed" src="https://img.shields.io/badge/tests-421%20passed-16a34a?style=flat-square" />
  <img alt="platform Windows and macOS" src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS-475569?style=flat-square" />
  <img alt="license MIT" src="https://img.shields.io/badge/license-MIT-0284c7?style=flat-square" />
</p>

[什么时候用](#什么时候会用到它) · [快速开始](#快速开始) · [它能做什么](#它能做什么) · [十八个工具](#十八个工具) · [接管](#人机验证与接管) · [安全](#安全与隐私) · [设置页](#设置页) · [配置](#配置) · [文档地图](#文档地图)

</div>

<p align="center"><img src="docs/assets/hero.svg" width="760" alt="示意图：左边是对话，右边是侧栏里的真浏览器面板；顶部徽章显示检测到验证、等你处理，面板底部有我来接管按钮" /></p>

DSH 桌面端本来就能开网页：你点开、你操作。这个插件补的不是"又一个浏览器"，而是**让 Agent 能用同一块面板**——它看得到带 `ref` 的元素、点得动、填得进、能把文件带回来，中间还能把鼠标交还给你。

内置的 `web_search` / `web_fetch` 负责「匿名、快速、只读」地取网页文字；这里负责「用你的登录身份、看得见、能动手」的那一半。

## 什么时候会用到它

先问一句：**我需要的只是这几段文字，还是这个页面本身？**

只要命中下面任意一条，就该开面板；一条都不命中，就别开——浏览器比抓网页慢，也更贵。

| 触发条件 | 具体长什么样 |
|---|---|
| **内容在登录之后** | 订单、账单、后台、邮箱、内部系统、会员价——`web_fetch` 只能拿到登录页 |
| **内容要跑完 JS 才出现** | 单页应用、无限滚动、点「加载更多」、切换标签页才有的表格 |
| **必须动手才走得下去** | 点按钮、填表单、选日期、翻页、hover 出菜单、在 canvas 或地图上缩放拖动 |
| **要把文件带回来** | 附件、报表、导出的表格——下载落到工作区，带字节数与 sha256（文件内容指纹，用来核对下回来的东西没被改过） |
| **要留下「当时页面长这样」的证据** | 整页拼接截图 + 尺寸 + sha256（同一张图永远算出同一个值，能证明报告里那张图就是当时截的那张） |
| **中途必须有人** | 验证码、滑块、要你判断的歧义——它停下，你处理，处理完再续跑 |

反过来，这三种情况**不要**用它：

- 只是读一篇公开文章、一份静态文档 → `web_fetch`，最便宜；
- 只是想找到网址、找到资料在哪 → `web_search`；
- 要做的是你本人的主观决定（选哪个方案、这笔钱要不要付）→ 你来点，别交给 Agent。

还有一层是「什么时候该把面板亮出来」，那是设置里的三档（自动 / 每次调用都打开 / 从不自动打开），跟上面这六条不是一回事，见下文[「面板自动打开」到底管什么](#面板自动打开到底管什么)。

### 它补的是哪一层

| 你要做的事 | `web_search` | `web_fetch` | DSH 自带浏览器（你手动） | 本插件（Agent 动手） |
|---|:---:|:---:|:---:|:---:|
| 找网址、找资料在哪 | ✅ | | | |
| 读公开的静态文章、文档 | | ✅ 最便宜 | | |
| 打开 JS 渲染 / 登录后才有的页面 | | ✗ | ✅ | ✅ |
| 用你的登录态（Cookie、扫码、账号） | | ✗ | ✅ | ✅ |
| 点按钮、填表、翻页、悬停、缩放 | | ✗ | ✅ 手动 | ✅ 自动 |
| 留下整页证据、把附件下载回来 | | | ✅ 手动 | ✅ 带 sha256 |
| 遇到人机验证 | | | ✅ | 检测到就交给你 |

浏览器本身不缺，缺的是**给 Agent 用的那一层**：可寻址的元素（`ref`）、可回放的错误（21 个稳定错误码）、可交还的控制权（顶部那条接管按钮）。这三样才是这个插件的正文。

判据、计费与边界讨论见 [`docs/design/web-tools-and-agent-browser.md`](docs/design/web-tools-and-agent-browser.md)。

## 它能做什么

| 能力 | 具体是什么 |
|---|---|
| **侧栏里的真浏览器** | Electron `<webview>`，不是截图流、也不是无头浏览器。登录态、Cookie、JS 渲染、跨域 iframe 都是真的，页面就在你眼前 |
| **快照带 `ref`** | `browser_snapshot` 把无障碍树 + 一张截图一起给模型，可交互元素都带 `[ref=eN]`，能算出稳定路径时还带 `[loc="css:…"]`；点击、输入、悬停直接用 ref/loc，不用猜坐标。树被预算截断时返回 `cursor`，下次带 `cursor` 续读下一段；页面在两次快照之间打印的 console 与未捕获错误会附在末尾（最多 10 条），页面自己发出的 fetch/XHR 失败也会附上（写清失败数与请求总数） |
| **十八个工具** | 打开 / 快照 / 阅读 / 点选 / 标签页 / 等待 / 点击 / 拖拽 / 滚动 / 悬停 / 缩放 / 截图 / 输入 / 按键 / 上传 / 求值 / 下载 / 时间线，覆盖一个正常人会用浏览器做的事 |
| **看得见的动作** | 每个动作后页面里补画一笔落点痕迹（点击涟漪、悬停光标点、元素高亮、拖拽连线），独立覆盖层、页面收不到事件；`feedback.enabled` 可关闭 |
| **验证墙不硬闯** | 检测到 Cloudflare、reCAPTCHA、滑块这类验证页就停下，把控制权交给你；你过完再交还，Agent 会收到一段「你不在时发生了什么」的摘要 |
| **证据落盘** | 截图默认拼接整页，下载件落盘，两者都带尺寸 / 字节数 / sha256，能直接当报告附件 |
| **失败不毁现场** | 导航失败自动退回上一页，错误里带 `nav_dns` / `nav_cert` / `nav_blocked` 等具体原因；错误页上不会返回空树假成功 |
| **过程看得见** | Web 端为截图 / 打开 / 下载各出一张工具卡片，模型调了什么、页面长什么样，一眼可查 |
| **设置就在 DSH 里** | 装好后「设置」左侧多一页 **浏览器面板**：行为、预算、下载、搜索兜底、会话白名单、本地文件服务六组表单，改完保存即可，不用手改 YAML |
| **工程化底座** | 动态端口 + 每进程令牌、21 个稳定错误码、取消、策略接缝、421 个单测 |

## 快速开始

### 1. 确认环境

| 项 | 要求 |
|---|---|
| 宿主 | **仅 DSH Desktop（Electron）**。面板依赖 `<webview>` 与 `globalThis.dshDesktop.browser` 租约，Web 版没有这两样 |
| DSH 版本 | `>=0.2.2-rc.3 <0.3.0`（本机实测 `0.2.2-rc.5`） |
| 操作系统 | Windows / macOS 桌面端 |
| 网络 | 通道只监听 `127.0.0.1`；页面访问走面板自己的网络栈，带你的登录态 |

### 2. 装包

在对话里让 Agent 安装仓库里的 tgz（装完通常无需重启；若面板行为还是旧的，说明客户端 bundle 被缓存了，完整重启一次 DSH 即可）：

```text
plugin_manager action: install_bundle
                target: dist/dsh-plugin-agent-browser/dsh-plugin-agent-browser-1.5.24.tgz
```

### 3. 打开面板

点右侧栏上的 **+**，在引导页里选 **「浏览器（Agent）」**。首次打开会让你自己登录目标站点，登录态留在面板里，同一进程内后续页面与 Agent 直接复用。

### 4. 让它干活

不用记工具名，直接说你想让它做什么：

> 打开 <你的目标站点>，登录进去，按「近一周 / 关键词 / 你的筛选条件」跑一遍，把前几条整理成表格，再截一张整页图。

Agent 会自己走完 `browser_open` → `browser_snapshot` → 按 `ref` 点搜索框、点搜索、翻页 → `browser_screenshot`。你可以在面板里看着它一步步动，卡住了随时接管。

### 5. 想自己接手

点面板顶部的 **「我来接管」**。此时 Agent 的 `open` / `click` / `type` / `press` / `eval` 全部被拒绝，但 `browser_snapshot` 仍然可用——它得能看见你做了什么。点「交还 Agent」时，面板会先截一张图，把交接摘要交给它。

## 十八个工具

| 工具 | 作用 |
|---|---|
| `browser_open` | 打开 http(s) 地址；或传 `path` 打开工作区里的 HTML（自动起只读本地服务）；`newTab:true` 时在面板里另开一个标签，当前页留在后面不丢 |
| `browser_pick` | 请人直接在页面上指路：`mode:"element"`（默认）点一个元素，`mode:"box"` 拉一个框拿走框里每个元素，都变成结构化引用（`loc` + 可读名 + `rect` + 落点坐标；框选还带框的坐标、`total` 与 `truncated`），之后用 `browser_click {loc}` 等既有工具逐个操作。点选/框选期间页面**收不到**按下、拖动和松手（捕获后吞掉，不派发输入），不需要确认条；`timeoutMs` 默认 60000（夹 3000–120000）、`limit` 默认 20（夹 1–100），超时或 Esc 是正常回执不是错误；图标按钮、重复行、一组复选框、canvas 控件这些快照读不出的目标最适合先 pick |
| `browser_tabs` | 列出、切换、关闭面板里的标签页（`action: "list"` / `"switch"` / `"close"`，`tab` 传标签 id）；切换保留每个标签的页面状态，关最后一个会先开一张空白页 |
| `browser_snapshot` | 读当前页面的无障碍树（带 `[ref=eN]`；能算出稳定路径时紧跟 `[loc="css:…"]`）+ 一张截图；`includeImage:false` 可省掉截图；被字符预算截断时返回 `cursor`，带 `cursor` 再调用可续读下一段（页面变了会返回 `stale_cursor`）；页面自己打印的 console/未捕获错误也会附在末尾（最多 10 条，每次快照清空），页面自己发出的 fetch/XHR 失败同样附在末尾（最多 10 条，带状态/耗时/错误与请求总数） |
| `browser_read` | 读页面**渲染出来的文字或表格**，不靠无障碍树：`mode: "text"`（默认）返回可见文字并截断到 `maxChars`（默认 8000，最大 40000），`mode: "table"` 返回每张表的 caption、表头与行（`maxTables` 默认 10、`maxRows` 默认 100）；用 `loc`/`selector`/`ref` 指定根元素，不传则是整页 body；纯读、零审批，人工相位下也可用 |
| `browser_wait` | 等某个 CSS 选择器或页面文字出现（`gone:true` 等它消失），超时返回 `timedOut`；纯读、无需确认，异步加载先等再快照 |
| `browser_click` | 点某个 `ref`；ref 过期时改用快照里的 `loc="css:…"`（跨快照有效），或直接传 CSS `selector`（失败会分型报告 `not_found` / `multiple` / `occluded` / `disabled`） |
| `browser_drag` | 拖拽：`from` 按住、`to` 松开（各传一个 `ref` / `loc` / `selector`；`to` 也可传视口坐标 `toX`+`toY` 或相对源中心的 `dx`/`dy`），`steps` 2–30 默认 8；适合滑块、可排序列表、看板、canvas 手柄；写动作、站点首次确认；原生 HTML5 drag-and-drop 不覆盖 |
| `browser_scroll` | 滚动页面/容器（`dy` / `to` / `container`），或按 `ref` / `loc` / `selector` 把某个元素滚进视口，返回位置、`atBottom`、元素 `rect` 与 `visible` / `fullyVisible` |
| `browser_hover` | 把指针移到元素上但不按，返回落点与 `grew`；叠卡、悬浮菜单要先 hover 再点 |
| `browser_zoom` | 缩放页面 25%–300%；缩小会给页面更宽的排版视口，桌面站才塞得进窄侧栏 |
| `browser_screenshot` | 存 PNG 到工作区 `screenshots/`，返回路径、尺寸、sha256；默认长页拼接成整页图 |
| `browser_type` | 往输入框写文字（`ref` 或 `loc` 定位），`submit:true` 顺带回车；**密码框一律拒绝**，交给人来输 |
| `browser_press` | 按一个键或组合键；`Alt+Left` / `Alt+Right` / `F5` 会走面板的导航动作 |
| `browser_upload` | 把工作区里的文件放进页面的 `<input type=file>`：写动作、站点首次确认；单文件 2 MiB / 合计 4 MiB / 最多 5 个，路径不许出工作区 |
| `browser_eval` | 在页面里求值（不够用时才用，永远不要用它绕过登录或验证）；可整体关闭 |
| `browser_download` | 把附件下到工作区 `downloads/`，返回路径、字节数、sha256；可执行类扩展名会被拒 |
| `browser_timeline` | 回读这台宿主上最近执行过的动作：工具、成败、错误码、参数摘要、截图/下载的文件路径；纯读、零审批，面板关着也能查 |

> `browser_snapshot` 默认每次附图。截图对视觉 token 不便宜，这是刻意的取舍：Agent 看不到页面就只能猜。需要省 token 时传 `includeImage:false`。

## 它是怎么工作的

```text
Agent（对话）
   │  browser_* 工具调用
   ▼
host 半 · 注册工具 / 策略 / 下载 / 静态服务
   │  长轮询：127.0.0.1 动态端口 + 每进程令牌
   ▼
client 半 · 侧栏 tab / 四态徽章 / 三张工具卡片 / <webview>
   │  executeJavaScript
   ▼
页面注入层 · snapshot / actions / detect / guards
```

- **为什么要三层**：工具跑在宿主侧，才有文件与网络权限；`<webview>` 只能活在渲染器里；页面内的遍历与命中必须进页面执行。三层之间只有一条本机回环通道。
- **为什么不用 CDP / Playwright**：桌面端已经把浏览器租约给了渲染器，再拉一个外部 Chrome 就不是"侧栏里那一个"。取舍见 [`docs/decisions/005`](docs/decisions/005-loopback-bridge-over-cdp.md)。
- **为什么长轮询**：面板侧只能发起请求，宿主拿不到渲染器的主动推送。长轮询 + 队列是这个约束下最省事的一条路。

## 人机验证与接管

面板顶部有一条徽章，四种状态：

| 状态 | 含义 |
|---|---|
| `Agent 正在操作（mm:ss）` | Agent 在用 |
| `等待你处理（人机验证）` | 检测到验证页，输入类工具被拦下 |
| `你已接管（mm:ss）` | 你在面板里自己动手 |
| `空闲` | 没人动 |

- **只检测，不绕过**。遇到 Cloudflare / reCAPTCHA / 滑块，页面内画一圈红框提示你，Agent 的调用拿到 `needs_human`，它应当把控制权交给你而不是硬试。
- **密码永不进入对话**。`browser_type` 对密码框一律拒绝，密码由你在面板里输入。
- **交接有摘要**。交还时截一张图 + 一段文字摘要，Agent 下一次快照就能读到「你不在时页面变成了什么样」。

## 安全与隐私

- 通道**只监听 `127.0.0.1`**，动态端口 + 每进程 43 字符令牌 + Host 校验；令牌只经宿主发现路由下发给面板。
- 本地静态服务**只读、仅当前工作区**、随机端口 + 路径令牌 + 双重路径校验，拒绝目录穿越与符号链接。
- **密码框内容永不进入模型上下文**；`browser_eval` 可整体关闭（`evalEnabled: false`）。
- 下载默认拦截 24 类可执行扩展名，单文件 50 MiB 上限，重名不覆盖。
- `sessions.allowlist` 可以限定只有哪些会话能驱动浏览器（子代理默认拿不到）。
- 截图与下载只落在工作区的 `screenshots/`、`downloads/`。

## 设置页

装好之后，**「设置」左侧会多一页「浏览器面板」**（插件启用时出现，禁用即消失）。不用去翻 `cordis.patch.yml`，参数都在这里改：

![设置 → 浏览器面板：顶部是桥的状态行，下面是行为、预算、下载、搜索兜底、会话白名单、本地文件服务六组字段](docs/assets/settings-page.png)

顶部那行现况（桥 `http://127.0.0.1:6549` · 工具 14 个 · 面板 client 1 个）就是排查入口：数字不对，先看插件有没有加载，再看是不是有别的后端在抢面板。

| 分组 | 能改什么 | 保存后 |
|---|---|---|
| 行为 | 面板自动打开（`activation`）/ 系统提示词路由段（`routing`）/ 导航后缩到面板宽度 / 占用 browserUse 槽 / 允许 `browser_eval` | 立即生效，下一次工具调用就按新值走 |
| 预算 | 导航超时、快照默认字符上限、`eval` 上限 | 插件重载约 1–2 秒，面板自动重连 |
| 下载 | 下载目录、单文件上限、额外禁用的扩展名 | 同上 |
| 搜索兜底 | 导航失败时是否附同站候选、候选条数 | 同上 |
| 会话白名单 | 只允许哪些会话驱动浏览器（留空 = 全部，子代理默认拿不到） | 同上 |
| 本地文件服务 | 工作区页面的单文件上限 | 同上 |

页面顶部是一行现况：桥的端口、已注册的工具数、当前几个会话持有浏览器——排查问题时先看这一行，能立刻分清"插件没加载"和"页面在跟别的后端抢"。

### 「面板自动打开」到底管什么

它只管**浏览器面板本身**：`browser_open` / `snapshot` / `click` / `type` / `scroll` / `hover` / `zoom` / `screenshot` / `press` / `eval` 这十个工具被调用时，要不要把右侧栏展开、把面板带到前台。它**不影响** `web_search` / `web_fetch`——那两个是 DSH 内置的联网工具，跑在宿主里，永远不碰面板。

| 选项 | 实际行为 |
|---|---|
| **自动（需要时）** `auto` | 只有当这个会话还没有活着的面板时，才打开并展开右侧栏；之后不再动布局。你手动收起侧栏后，它会保持收起 |
| **每次调用都打开** `always` | 每条浏览器命令都把面板带到前台（即使你已经切到别的视图）；适合"想盯着它操作"的场景，代价是每次操作都会抢一次焦点 |
| **从不自动打开** `manual` | 从不打开。当前没有面板时，命令立即失败并返回 `panel_not_open`，提示你自己开页签或改成 `auto` |

两个例外要知道：

- `browser_download` 永远不受这三档影响——它在宿主侧用 `fetch` 跑，既不开面板也不需要面板。
- `auto` / `always` 只能打开面板页签并展开右栏，**不能把你切换到别的会话**。如果那条命令所属的会话不在屏幕上，面板拿不到页面，5 秒后仍会返回"panel is not on screen"，此时切回那个会话再重试即可。

保存只提交你改动过的字段；写配置走的是 DSH 自己的 config editor，所以**本插件永远不会去改你的 `cordis.patch.yml`**。需要重载的那几组，页面会等插件重新连上、读回新值之后再提示成功。

> 如果页面提示「这个 profile 不能保存插件配置」，说明宿主没给它 config editor（常见于只读 profile）——此时表单只读，配置只能按下一节写 YAML。

## 配置

日常改配置优先用上一节的设置页。只有在没有界面、或要把配置写进版本库时，才需要手写 YAML：

在 `cordis.patch.yml` 里给插件写 `config` 时，**这一行是整行替换，不是深合并**：只写一个字段，其余字段会全部回到默认值。正确写法是把整份配置抄全、只改你要改的那几行。完整模板与全部字段的说明见[用户手册](dist/dsh-plugin-agent-browser/README.md#配置)。

最常改的三个旋钮：

| 字段 | 默认 | 说明 |
|---|---|---|
| `activation` | `auto` | `auto` 只有需要页面的动作才展开面板；`always` 每次都亮；`manual` 要你自己先开 |
| `evalEnabled` | `true` | 是否允许 `browser_eval` 在页面里跑任意 JS；不可信页面建议关 |
| `searchFallback.enabled` | `false` | 导航失败时附上同站候选（按次计费，默认关，绝不自动打开） |
| `approvals.mode` | `first-touch` | 写动作（输入、提交、下载、脚本）在同站点第一次出现时问一次；`off` 回到 1.4.x 的直接执行 |
| `approvals.timeoutMs` | `30000` | 确认条等待时长，超时按「拒绝」处理，不执行 |
| `approvals.sensitiveSites` | `[]` | 这些站点每次都问，即使选过「本会话允许本站」 |
| `dialogs.mode` | `record` | 页面 `alert/confirm/prompt` 默认被拦截并记录（`confirm` 答否、`prompt` 答取消），页面不冻结；`off` 恢复原生弹窗（会冻结到人点掉） |
| `feedback.enabled` | `true` | 每个动作后在页面上画一笔落点痕迹（点击涟漪、元素高亮、拖拽连线），纯展示层、页面收不到事件，关掉即静默 |

## 写动作确认（`approvals`，默认开启）

读动作从不打扰：`open`、`snapshot`、`scroll`、`hover`、`screenshot`、普通链接近导航都直接执行。六类写动作会在一处**站点 × 会话**粒度上问一次：输入文字（type）、会提交表单的点击/Enter（submit）、下载（download）、页面脚本（eval）、上传文件（upload）、拖拽（drag，无法从元素判断是否改状态，一律按写处理）。确认条长在面板顶部，三个按钮「允许一次 / 本会话允许本站 / 拒绝」，Enter 等于拒绝；面板不可见时立即失败而不是干等 30 秒；你点「我来接管」的那一瞬，待确认的写动作自动作废。

页面里的 JS 弹窗（`alert` / `confirm` / `prompt`）默认由注入守卫拦截并记录，不会冻结页面、也不会擅自点「确定」；内容会出现在随后那次操作的结果里（`blocked dialogs`），可用 `dialogs.mode` 切回原生行为（[`docs/tickets/041`](docs/tickets/041-js-dialogs.md)）。

写动作的结果带三态 `effect`：成功是 `committed`；在命令离开宿主前失败（参数、审批、策略、人工相位）是 `none`，重试是安全的；面板已经把命令拉走却丢了回执（超时、取消、被接管、插件停止）是 `unknown`，此时工具报 `action_unknown`（不可重试），hint 会要求先 `browser_snapshot` 核对页面再决定——**不要重发同一动作**。这条规则对 `submit` / `download` / `eval` 尤其重要（[`docs/spec/004`](docs/spec/004-capability-admission-spec.md) §4 B4、[`docs/tickets/042`](docs/tickets/042-action-effect-tri-state.md)）。

## 已知限制

- **阅读的边界**：`browser_read` 只读 `innerText`/`<table>`，不读几何、样式与 HTML 源码；只认真表格；跨域 iframe 文本不可读；截断时会给 `truncated` 与 `totalChars`。

- **仅桌面端**。Web 版 profile 没有 `<webview>` 与浏览器租约，启用后面板不出现、工具返回明确的 `unavailable` / `panel_not_open`，不会静默超时。
- **一个 profile 只能启用一个浏览器后端**。两套插件都注册 `browser_*` 工具，宿主会拒绝第二次注册；启用前先停掉另一个。
- **DSH 窗口在后台或最小化时不绘制**，也不接收合成输入：点击会"没反应"、截图会超时。把窗口切到前台即可，这不是插件 bug。
- **跨域 iframe 只能给占位**，里面的元素必须用坐标点；canvas 同理。
- **验证墙可能漏报**。检测器按 URL / 标题 / DOM / 文案判断；1.5.x 补上了「正在进行安全验证 / 验证您是人类」这类文案、`challenge-platform` iframe 与打开后 2 秒内的二次复检，并已在 `nopecha.com/demo/cloudflare` 真站回归通过（`needs_human` → 脚本被拒 → 人工过墙后恢复，[`docs/tickets/033`](docs/tickets/033-challenge-detection-gap.md)）；其他厂商的墙尚未取样，上线仍按「检测可能不触发，请人工接管」使用。
- **写动作确认按站点判断，不按登录态**：面板读不到 HttpOnly Cookie，所以无法区分「登录后的页面」；只好用「站点首次写动作」这个可观测信号代替（[`docs/spec/003`](docs/spec/003-first-touch-approval-spec.md)）。
- **只覆盖六类写动作**：输入、会提交表单的点击/Enter、下载、脚本、上传、拖拽。非表单按钮的副作用（比如「删除」按钮发 `fetch`）按读处理，不会被拦。
- **`browser_download` 走宿主侧 `fetch`，不带页面 Cookie**：需要登录态才能下载的链接会拿到登录页而不是文件。
- **`target=_blank` 的附件是黑洞**：点了既不导航也不落盘，附件一律用 `browser_download({ url })`。
- **动作时间线活在当前宿主进程**：最多 200 条，DSH 退出/插件重载即清空、不落盘；只记工具调用（不记页面内部事件或其他插件）；`browser_timeline` 自身读取不记录。
- **取消只保证"不再等、不再下发新命令"**，已经发到页面里的动作不会撤销；写动作若已被面板拉走，取消后返回 `action_unknown`（可能已执行，先 snapshot 核对）。
- **整页拼接有上限**：默认 10000 CSS 像素、最多 16000 设备像素行，超了会停下并在结果里标 `truncated`。
- **JS 弹窗只覆盖页面脚本期**：守卫在 `dom-ready` 后注入，内联脚本在解析期弹的窗、以及 `beforeunload` 的「页面留人」仍未处理（前者需 preload 探针，后者需宿主 `will-prevent-unload`）；普通 `alert/confirm/prompt` 已拦截并记录。

更多已知问题与处置见[用户手册 · 故障排查](dist/dsh-plugin-agent-browser/README.md#故障排查)。

## 仓库结构

```
plugin/         插件源码 —— 18 个工具、快照引擎、桥、守卫、注入脚本，以及 20 余个单测
dist/           打包产物 —— 可安装的 tgz、装机版 README、cordis.patch.yml
demo/           本地测试夹具 —— V2/V3/V4 直接跑的那几个文件
tools/          工程工具 —— pack（打包）、check-docs（文档一致性）、testsite（本地测试站）、case-run（案例探针与夹具）
docs/           全部文档 —— design / spec / decisions / cases / tickets / release / assets
screenshots/    运行截图 —— 案例证据与复跑留档
```

## 文档地图

| 文档 | 内容 |
|---|---|
| [用户手册](dist/dsh-plugin-agent-browser/README.md) | 安装 / 升级 / 卸载、全部配置字段、16 个工具、故障排查 |
| [与内置联网工具的分工](docs/design/web-tools-and-agent-browser.md) | 三层能力对比、`search → fetch → open` 判据、计费风险 |
| [为什么不复用官方浏览器工具](docs/design/browser-use-contract.md) | 48 行互斥锁、MCP provider、三条路线对比 |
| [技术规格](docs/spec/001-agent-browser-plugin-spec.md) | 工具契约、状态机、快照格式、安全边界 |
| [官方对齐规格](docs/spec/002-official-alignment-spec.md) | B1–B11 / M1–M5 / U1–U7 与版本线 1.1.0–1.4.3 |
| [决策记录](docs/decisions/README.md) | 10 篇：通道选型、为什么不用 CDP、动态端口与令牌、首次写动作确认…… |
| [取证与验收](docs/cases) | 探针结果、快照引擎、接管、打包、spec 审计、五套案例集（含首写确认 F1–F12） |
| [ticket 列表](docs/tickets) | 47 张，含失败模式与验收证据 |
| [发布说明](docs/release/release-notes-1.5.md) | 1.5.x 产物、行为变化、未验证项、回滚 |
| [工作区日志](PROGRESS.md) | 开发期进度、踩坑、下一步 |

## 开发

仓库是纯 JS，**没有构建步骤**；插件源码在 `plugin/`，发布产物在 `dist/`。

```bash
# 单测（421 例）
node --test --test-timeout=60000 plugin/test/*.test.mjs

# 打包 tgz
node tools/pack.mjs

# 文档 ↔ 代码一致性（配置字段 / 工具名 / 示例 YAML / 决策索引 / B11 引用）
node tools/check-docs.mjs
```

`docs/assets/hero.svg` 是手写的示意图；`docs/assets/` 里另有几张真实运行截图，`python tools/make-readme-assets.py` 可以从截图重新生成（Pillow，可选）。

开发循环是「改 `plugin/` → `node tools/pack.mjs` → `plugin_manager install_bundle <tgz>`」，约 10 秒。改 `client.js` 要 bump `CLIENT_REV` 才会重新执行 client 半。更多约定（哪些字段能热改、重装后第一条命令为什么超时、link 安装的坑）写在 [`PROGRESS.md`](PROGRESS.md) 末尾。

## 反馈

若发现有问题或有修改建议，可以直接开 [issue](https://github.com/linhuanwen/dsh-plugin-agent-browser/issues) 描述问题或建议。

## 友链

本项目已链接认可 [LINUX DO](https://linux.do) 社区。

## License

[MIT](LICENSE) © 2026 linhuanwen
