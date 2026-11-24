<div align="center">

<img src="docs/assets/icon.svg" width="84" alt="agent browser panel" />

# DSH-Agent 侧边自动化操作浏览器

**在 DeepSeek Harness 的右侧栏里，让 Agent 用你的真浏览器干活：它看得见、点得动，你随时可以接管。**

`dsh-plugin-agent-browser` · DSH 桌面端插件

<p>
  <img alt="version 1.4.24" src="https://img.shields.io/badge/version-1.4.24-2563eb?style=flat-square" />
  <img alt="DSH 0.2.2 - 0.3.0" src="https://img.shields.io/badge/DSH-0.2.2%20~%200.3.0-1d4ed8?style=flat-square" />
  <img alt="11 tools" src="https://img.shields.io/badge/tools-11-0f766e?style=flat-square" />
  <img alt="196 tests passed" src="https://img.shields.io/badge/tests-196%20passed-16a34a?style=flat-square" />
  <img alt="platform Windows and macOS" src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS-475569?style=flat-square" />
  <img alt="license MIT" src="https://img.shields.io/badge/license-MIT-0284c7?style=flat-square" />
</p>

[什么时候用](#什么时候会用到它) · [快速开始](#快速开始) · [它能做什么](#它能做什么) · [十一个工具](#十一个工具) · [接管](#人机验证与接管) · [安全](#安全与隐私) · [设置页](#设置页) · [配置](#配置) · [文档地图](#文档地图)

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

浏览器本身不缺，缺的是**给 Agent 用的那一层**：可寻址的元素（`ref`）、可回放的错误（13 个稳定错误码）、可交还的控制权（顶部那条接管按钮）。这三样才是这个插件的正文。

判据、计费与边界讨论见 [`docs/design/web-tools-and-agent-browser.md`](docs/design/web-tools-and-agent-browser.md)。

## 它能做什么

| 能力 | 具体是什么 |
|---|---|
| **侧栏里的真浏览器** | Electron `<webview>`，不是截图流、也不是无头浏览器。登录态、Cookie、JS 渲染、跨域 iframe 都是真的，页面就在你眼前 |
| **快照带 `ref`** | `browser_snapshot` 把无障碍树 + 一张截图一起给模型，可交互元素都带 `[ref=eN]`；点击、输入、悬停直接用 ref，不用猜坐标 |
| **十一个工具** | 打开 / 快照 / 点击 / 滚动 / 悬停 / 缩放 / 截图 / 输入 / 按键 / 求值 / 下载，覆盖一个正常人会用浏览器做的事 |
| **验证墙不硬闯** | 检测到 Cloudflare、reCAPTCHA、滑块这类验证页就停下，把控制权交给你；你过完再交还，Agent 会收到一段「你不在时发生了什么」的摘要 |
| **证据落盘** | 截图默认拼接整页，下载件落盘，两者都带尺寸 / 字节数 / sha256，能直接当报告附件 |
| **失败不毁现场** | 导航失败自动退回上一页，错误里带 `nav_dns` / `nav_cert` / `nav_blocked` 等具体原因；错误页上不会返回空树假成功 |
| **过程看得见** | Web 端为截图 / 打开 / 下载各出一张工具卡片，模型调了什么、页面长什么样，一眼可查 |
| **设置就在 DSH 里** | 装好后「设置」左侧多一页 **浏览器面板**：行为、预算、下载、搜索兜底、会话白名单、本地文件服务六组表单，改完保存即可，不用手改 YAML |
| **工程化底座** | 动态端口 + 每进程令牌、13 个稳定错误码、取消、策略接缝、196 个单测 |

## 快速开始

### 1. 确认环境

| 项 | 要求 |
|---|---|
| 宿主 | **仅 DSH Desktop（Electron）**。面板依赖 `<webview>` 与 `globalThis.dshDesktop.browser` 租约，Web 版没有这两样 |
| DSH 版本 | `>=0.2.2-rc.3 <0.3.0`（本机实测 `0.2.2-rc.5`） |
| 操作系统 | Windows / macOS 桌面端 |
| 网络 | 通道只监听 `127.0.0.1`；页面访问走面板自己的网络栈，带你的登录态 |

### 2. 装包

在对话里让 Agent 安装仓库里的 tgz（装完**不需要重启** DSH）：

```text
plugin_manager action: install_bundle
                target: dist/dsh-plugin-agent-browser/dsh-plugin-agent-browser-1.4.24.tgz
```

### 3. 打开面板

点右侧栏上的 **+**，在引导页里选 **「浏览器（Agent）」**。首次打开会让你自己登录目标站点，登录态留在面板里，同一进程内后续页面与 Agent 直接复用。

### 4. 让它干活

不用记工具名，直接说你想让它做什么：

> 打开 <你的目标站点>，登录进去，按「近一周 / 关键词 / 你的筛选条件」跑一遍，把前几条整理成表格，再截一张整页图。

Agent 会自己走完 `browser_open` → `browser_snapshot` → 按 `ref` 点搜索框、点搜索、翻页 → `browser_screenshot`。你可以在面板里看着它一步步动，卡住了随时接管。

### 5. 想自己接手

点面板顶部的 **「我来接管」**。此时 Agent 的 `open` / `click` / `type` / `press` / `eval` 全部被拒绝，但 `browser_snapshot` 仍然可用——它得能看见你做了什么。点「交还 Agent」时，面板会先截一张图，把交接摘要交给它。

## 十一个工具

| 工具 | 作用 |
|---|---|
| `browser_open` | 打开 http(s) 地址；或传 `path` 打开工作区里的 HTML（自动起只读本地服务） |
| `browser_snapshot` | 读当前页面的无障碍树（带 `[ref=eN]`）+ 一张截图；`includeImage:false` 可省掉截图 |
| `browser_click` | 点某个 `ref`；没有 ref 时传 CSS `selector`（失败会分型报告 `not_found` / `multiple` / `occluded` / `disabled`） |
| `browser_scroll` | 滚动页面或某个容器，返回位置与 `atBottom`；懒加载列表靠它触发 |
| `browser_hover` | 把指针移到元素上但不按，返回落点与 `grew`；叠卡、悬浮菜单要先 hover 再点 |
| `browser_zoom` | 缩放页面 25%–300%；缩小会给页面更宽的排版视口，桌面站才塞得进窄侧栏 |
| `browser_screenshot` | 存 PNG 到工作区 `screenshots/`，返回路径、尺寸、sha256；默认长页拼接成整页图 |
| `browser_type` | 往输入框写文字，`submit:true` 顺带回车；**密码框一律拒绝**，交给人来输 |
| `browser_press` | 按一个键或组合键；`Alt+Left` / `Alt+Right` / `F5` 会走面板的导航动作 |
| `browser_eval` | 在页面里求值（不够用时才用，永远不要用它绕过登录或验证）；可整体关闭 |
| `browser_download` | 把附件下到工作区 `downloads/`，返回路径、字节数、sha256；可执行类扩展名会被拒 |

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

顶部那行现况（桥 `http://127.0.0.1:6549` · 工具 11 个 · 面板 client 1 个）就是排查入口：数字不对，先看插件有没有加载，再看是不是有别的后端在抢面板。

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

## 已知限制

- **仅桌面端**。Web 版 profile 没有 `<webview>` 与浏览器租约，启用后面板不出现、工具返回明确的 `unavailable` / `panel_not_open`，不会静默超时。
- **一个 profile 只能启用一个浏览器后端**。两套插件都注册 `browser_*` 工具，宿主会拒绝第二次注册；启用前先停掉另一个。
- **DSH 窗口在后台或最小化时不绘制**，也不接收合成输入：点击会"没反应"、截图会超时。把窗口切到前台即可，这不是插件 bug。
- **跨域 iframe 只能给占位**，里面的元素必须用坐标点；canvas 同理。
- **验证墙可能漏报**。检测器按 URL / 标题 / DOM / 文案判断，真实 Cloudflare 挑战页有漏报记录（[`docs/tickets/033`](docs/tickets/033-challenge-detection-gap.md)）；上线按"检测可能不触发，请人工接管"使用。
- **`browser_download` 走宿主侧 `fetch`，不带页面 Cookie**：需要登录态才能下载的链接会拿到登录页而不是文件。
- **`target=_blank` 的附件是黑洞**：点了既不导航也不落盘，附件一律用 `browser_download({ url })`。
- **取消只保证"不再等、不再下发新命令"**，已经发到页面里的动作不会撤销。
- **整页拼接有上限**：默认 10000 CSS 像素、最多 16000 设备像素行，超了会停下并在结果里标 `truncated`。

更多已知问题与处置见[用户手册 · 故障排查](dist/dsh-plugin-agent-browser/README.md#故障排查)。

## 仓库结构

```
plugin/         插件源码 —— 11 个工具、快照引擎、桥、守卫、注入脚本，以及 20 余个单测
dist/           打包产物 —— 可安装的 tgz、装机版 README、cordis.patch.yml
demo/           本地测试夹具 —— V2/V3/V4 直接跑的那几个文件
tools/          工程工具 —— pack（打包）、check-docs（文档一致性）、testsite（本地测试站）、case-run（案例探针与夹具）
docs/           全部文档 —— design / spec / decisions / cases / tickets / release / assets
screenshots/    运行截图 —— 案例证据与复跑留档
```

## 文档地图

| 文档 | 内容 |
|---|---|
| [用户手册](dist/dsh-plugin-agent-browser/README.md) | 安装 / 升级 / 卸载、全部配置字段、11 个工具、故障排查 |
| [与内置联网工具的分工](docs/design/web-tools-and-agent-browser.md) | 三层能力对比、`search → fetch → open` 判据、计费风险 |
| [为什么不复用官方浏览器工具](docs/design/browser-use-contract.md) | 48 行互斥锁、MCP provider、三条路线对比 |
| [技术规格](docs/spec/001-agent-browser-plugin-spec.md) | 工具契约、状态机、快照格式、安全边界 |
| [官方对齐规格](docs/spec/002-official-alignment-spec.md) | B1–B11 / M1–M5 / U1–U7 与版本线 1.1.0–1.4.3 |
| [决策记录](docs/decisions/README.md) | 9 篇：通道选型、为什么不用 CDP、动态端口与令牌…… |
| [取证与验收](docs/cases) | 探针结果、快照引擎、接管、打包、spec 审计、四套案例集 |
| [ticket 列表](docs/tickets) | 34 张，含失败模式与验收证据 |
| [发布说明](docs/release/release-notes-1.4.md) | 1.4.3 产物、行为变化、未验证项、回滚 |
| [工作区日志](PROGRESS.md) | 开发期进度、踩坑、下一步 |

## 开发

仓库是纯 JS，**没有构建步骤**；插件源码在 `plugin/`，发布产物在 `dist/`。

```bash
# 单测（196 例）
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
