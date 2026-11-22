# Superagent Orchestrator

**把活派给独立的 worker 会话，派完就结束本轮，结果自己回到会话里。**

[![version](https://img.shields.io/github/v/tag/ProgramerLiang/piD-super-agent?label=version)](https://github.com/ProgramerLiang/piD-super-agent/tags)
[![license](https://img.shields.io/github/license/ProgramerLiang/piD-super-agent)](./LICENSE)
[![plugin id](https://img.shields.io/badge/plugin%20id-corripo.superagent--orchestrator-blueviolet)](https://plugins.aiuo.net/plugins/corripo.superagent-orchestrator)
[![PI-Desktop](https://img.shields.io/badge/PI--Desktop-%3E%3D0.14.7-6f42c1)](https://github.com/ProgramerLiang/piD-super-agent)

PI-Desktop 插件 · id `corripo.superagent-orchestrator` · 版本 `0.2.0` · MIT（见 [LICENSE](./LICENSE)）· 需要 PI-Desktop `>= 0.14.7`（含 Session Collaboration 操作）

---

## 立即安装

> **在 PI-Desktop 插件中心安装**
>
> **<https://plugins.aiuo.net/plugins/corripo.superagent-orchestrator>**
>
> 打开发布页安装，按提示批准 6 项权限（见[第 8 节](#8-权限说明)）。上架版本 `0.2.0`，与仓库 `manifest.json` 一致。插件在启动时加载（`activationEvents: ["onStartup"]`），装完即用，没有其他配置项。

其他安装方式（源码加载、自己打包 `.piplug`）见[第 2 节](#2-安装)。

## 目录

- [1. 它解决什么问题](#1-它解决什么问题)
- [2. 安装](#2-安装)
- [3. 快速开始](#3-快速开始)
- [4. 动作总览](#4-动作总览)
- [5. 核心机制](#5-核心机制)
- [6. Workers 视图](#6-workers-视图)
- [7. 已知限制](#7-已知限制)
- [8. 权限说明](#8-权限说明)
- [9. 开发与测试](#9-开发与测试)
- [10. 来源与版权](#10-来源与版权)
- [11. 社区](#11-社区)

---

## 1. 它解决什么问题

| 你得到 | 说明 |
| --- | --- |
| 一个 `SessionTask` 工具 | 12 个 action：`spawnIn` / `spawn` / `send` / `supervise` / `status` / `workers` / `wait` / `result` / `accept` / `cancel` / `list` / `models` |
| 一个 **Workers** 视图 | 右工作面板里列出这个插件开过的所有 worker：标题、状态、最近活动、项目路径、结果摘要，点一行直接跳到那个会话 |
| 结果卡 | worker 回合结束时，把结果写回调用会话，并把 worker 自己的 `state` / `human_action` 顶到卡片上 |

主 agent 亲自干活会出三种毛病，这个插件逐个对着治：

| 痛点 | 具体表现 | 本插件的做法 |
| --- | --- | --- |
| **越级执行** | 说好「派出去」，主 agent 自己 `Bash` 去翻 worker 的日志、下载进度、内部状态，最后活全自己干了 | 工具描述把 `ORCHESTRATE, DO NOT EXECUTE` 写进模型读到的第一段：确认项目路径 → 写自包含的 brief → 派出去 → 审阅与整合报告 |
| **轮询浪费上下文** | `while` 循环里反复 `status` / `wait`，每一轮都把状态塞回上下文 | 默认异步：`notifyOnCompletion` 默认 `true`，宿主在 worker 回合结束时把结果写回调用会话；派完就结束本轮 |
| **「做完了」和「要你决定」分不开** | 回一段自由文本，读的人不知道能不能收工 | 状态契约：worker 报告末尾写 `state:` 与 `human_action:`，卡片据此渲染；`blocked` 的卡片第二行直接写「需要你决定：…」 |

结果不会丢：即使所有卡片通道都被拒，结果仍然记在 worker 行上，Workers 视图里读得到。

---

## 2. 安装

### 2.1 插件中心（推荐）

**<https://plugins.aiuo.net/plugins/corripo.superagent-orchestrator>**

1. 打开发布页，按页面上的安装入口安装；
2. PI-Desktop 会提示批准 6 项权限（[第 8 节](#8-权限说明)），逐项确认；
3. 装完即可用：插件注册 `SessionTask` 工具与 **Workers** 视图，没有其他配置项。

### 2.2 从源码加载（开发用）

1. `git clone https://github.com/ProgramerLiang/piD-super-agent`
2. PI-Desktop → **Plugins** → **Load development plugin** → 选**仓库根目录**（就是含 `manifest.json` 的那一层，不是 `views/`，也不是上一级）
3. 在 Plugins 页批准 6 项权限（见[第 8 节](#8-权限说明)）。热重载不会自动扩权，改权限必须重新加载。

### 2.3 打包成 `.piplug` 安装

先用 **PluginCheck** 校验，再用 **PluginPack** 打包，最后 **Install plugin package** 安装。

`.piplug` 是 store-only（不压缩）zip，用 `zip`/`tar` 手工打的包会被安装器拒绝；本仓库的 `.gitignore` 已排除 `*.piplug`，不要把产物提交进 git。

---

## 3. 快速开始

不需要关键词。工具描述里写清了触发条件：用户说「开个子会话去…」「并行做这两件事」「在另一个项目里跑测试」「子会话跑完了吗」，都算。

**派一个只读任务（默认异步，派完就结束本轮）**

```jsonc
{
  "action": "spawn",
  "title": "审查 auth",
  "task": "只读审查 src/auth 下的鉴权路径，不要修改任何文件。列出你实际检查过的文件与每个风险点的位置。\n\n报告最后必须写两行：\nstate: ready | blocked | failed\nhuman_action: none | <要人做的那一件具体的事>"
}
```

回执是交付凭据，不是结果：

```jsonc
{ "action": "spawn", "sessionId": "9f31…", "messageId": "m_7c2…", "status": "queued",
  "accepted": true, "requestedModel": "provider/model-id", "modelSelection": "delegation" }
```

**结果怎么回来**：worker 回合结束时，宿主把完成通知投回本会话，插件同时写一张结果卡（见 [5.3](#53-结果卡)）。**不要**在这中间 `wait` 或 `status` 轮询。

**在指定项目里派活**

```jsonc
{
  "action": "spawnIn",
  "projectPath": "/home/crp/other-repo",
  "title": "修构建",
  "task": "…（同样是自包含的 brief + 状态契约）"
}
```

**人问「现在什么状态」时才读**

```jsonc
{ "action": "workers" }                                        // 缓存行 + 实时状态
{ "action": "result", "sessionId": "9f31…" }                     // 一次交付的确切状态与报告
{ "action": "wait", "sessionIds": ["9f31…"], "timeoutMs": 30000 } // 显式阻塞，默认 25 s
```

---

## 4. 动作总览

工具在模型侧的名字是 `plugin_corripo_superagent_orchestrator_SessionTask`（宿主强制前缀 `plugin_<id_safe>_<tool>`）。

| action | 作用 | 关键参数 |
| --- | --- | --- |
| `spawn` | 走 `session/collaboration/spawn`，worker 落在**调用者自己的项目**里 | 必填 `task`（≤65536）；可选 `title`（≤80）`model` `notifyOnCompletion` `idempotencyKey` |
| `spawnIn` | 走 `session/create` + `session/collaboration/send`，worker 落在 `projectPath` 指定的项目 | 必填 `task`；可选 `projectPath` `title` `model` `notifyOnCompletion` `idempotencyKey`；没有 `projectPath` 退化为 `spawn` |
| `send` | 向已有会话投递一轮；默认**先投递，再打断旧轮次**，沿用该会话**已有的模型与上下文** | 必填 `sessionId` + `message`；可选 `kind`（`task`/`message`）`notifyOnCompletion` `idempotencyKey` `interrupt`（默认 `true`，设 `false` 退回排队）；传 `model` 报 `INVALID_ARGUMENT` |
| `notify` | worker 中途向派生它的父会话上报进度/提问/受阻，**不结束也不打断自己的回合** | 必填 `text`；可选 `kind`（`progress`/`question`/`blocked`）`sessionId`；同一 worker+kind 默认最少间隔 5000 ms（插件设置 `notifyMinIntervalMs` 可调） |
| `setModel` | 给**本插件已跟踪、当前空闲**的 worker 切换 provider/model，保留项目与会话上下文 | 必填 `sessionId` + `model`（key/别名）或 `providerId`+`modelId` 成对；可选 `thinkingLevel`；详见 [5.5](#55-setmodel换模型) |
| `supervise` | 一次向最多 **4** 个会话并行投递同一条消息 | 必填 `sessionIds`（≤4）+ `message`；可选 `notifyOnCompletion`；不接受 `idempotencyKey`；逐个回执，失败进 `failures` |
| `status` | 读宿主实时状态 | 可选 `sessionIds`（≤16）；不传时读本插件记录 |
| `workers` | 本插件 worker 行（缓存 + 实时状态） | 可选 `refresh`（默认 `true`；`false` 只读缓存，零宿主调用） |
| `wait` | 显式阻塞等待一次交付结算 | 必填 `sessionIds`；可选 `messageId` `turnId` `timeoutMs`（默认 25000，上限 45000，轮询 1 s；超时返回 `timedOut: true` 而不抛错） |
| `result` | 读**一次交付**的状态与最终报告 | 必填 `sessionId`；可选 `messageId` `turnId` |
| `accept` | 给一次**已完成且报告非空**的交付打审阅标记 | 必填 `sessionId` 或 `sessionIds`；可选 `messageId` `turnId` `note`（≤4096 字符）；不满足条件报 `WORKER_NOT_READY` |
| `cancel` | 取消协作工作，**不删除会话** | 必填 `sessionId`；可选 `messageId` |
| `list` | 宿主会话目录（≤100 条）+ 本插件 worker 的实时状态 | 无 |
| `models` | 已配置模型清单 + `automaticCandidates`（允许自动委派的）+ `defaultModel` | 无 |

`sessionId` 有兼容别名 `workerId`，`sessionIds` 有别名 `workerIds`；两者同时给出且不一致会报错，不会二选一。

---

## 5. 核心机制

### 5.1 默认异步

`notifyOnCompletion` 默认 `true` —— 这是本 fork 相对上游的行为改动（见[第 10 节](#10-来源与版权)）。

```js
// actions.js
const DEFAULT_NOTIFY_ON_COMPLETION = true;
```

```jsonc
// 默认：派完就结束本轮，结果自己回来
{ "action": "spawn", "task": "只读审查 src/auth，输出风险清单", "title": "审查 auth" }

// 只有当你决定留在同一轮里自己读结果时，才显式关掉
{ "action": "spawn", "task": "...", "notifyOnCompletion": false }
```

`notifyOnCompletion: true` 时，worker 回合结束由**宿主**把完成通知投回调用会话（协作消息，`sourceSessionId` → `targetSessionId`，`completion` 类型只有宿主能生成）。插件自己另有一条独立通道：`session:turnEnded` 事件 → 读回交付 → 生成结果卡（见 5.3）。

两条通道互不依赖，所以「宿主没投通知」不会让结果消失，反过来也一样。

### 5.2 打断式指令与中途上报

`send` 的 `interrupt` 默认 `true`：发给正在运行的 worker 时，新指令不再排到它那轮结束之后。实现顺序是固定的：

1. 先用**新的** `idempotencyKey` 投递新指令，记下返回的 `messageId`；
2. 只针对投递前观察到的**旧轮**调用 `agent/abort`（带旧 `turnId`）；宿主只在那个 turn 仍是活跃轮时才执行，晚到的调用拿到 `{aborted:false}` 就停手；`agent/abort` 不可用时降级为带**旧 messageId** 的 `session/collaboration/cancel`；
3. 回查新消息的 `status` 与 `turn_id`（200 ms × 至多 10 次）。若新消息被撤回（`cancelled`），用**新的幂等键**重投，最多 3 次；
4. 返回 `{delivered, interrupted, messageId, turnId, attempts, withdrawnRetried}`。三次都被撤回时 `delivered:false` + `reason:"withdrawn"`，不会报一个假的「已发送」。

**为什么先投递后打断：** 在模型回复任何内容之前取消，宿主会撤回那一轮的消息；如果先 `cancel` 再 `send`，刚发的指令本身可能被一起撤回。先落一条独立的消息行，再只点名旧 turn/旧 message，任何一步都没有指向新消息的 id；回查与重投则兜住宿主仍然撤回新消息的竞态。**这里从不调用不带 `messageId` 的 `cancel`** —— 它会把所有排队消息一起取消，正好包括刚投递的指令。

`interrupt:false` 恢复旧行为：消息进宿主队列，等当前轮结束才被读到。

worker 侧的 `notify` 走反方向的普通协作消息：目标由 worker 的委派来源自动反查（本插件记录优先，宿主 provenance 兜底，也可显式 `sessionId` 指定）。正文带 `[worker-report:<kind>]` 标记，并明确写「不是任务完成回执；它此刻仍在运行」；`notifyOnCompletion:false`，所以不会生成完成回调。调用返回后 worker 的当前轮**继续运行**。主会话收到的是一条普通 incoming 消息，与 `completion` 类型的完成通知和结果卡分开。同一 worker 同一 `kind` 在最小间隔（默认 5000 ms，插件设置 `notifyMinIntervalMs` 可调，上限 600000）内重复调用会返回 `throttled:true` + `retryAfterMs`，不再投递。

### 5.2 状态契约

派任务时要求 worker 在报告末尾写两行：

```text
state: ready | blocked | failed
human_action: none | <要人做的那一件具体的事>
```

解析在 `cards.js`，规则是「宽进严出」：

| 情况 | 结果 |
| --- | --- |
| `**State:** blocked`、`state：blocked`（全角冒号）、`- state: READY` | 都认（容忍 markdown 强调、列表符号、大小写、全角冒号） |
| `state:` 后面是契约外的词（如 `state: partial`） | **整个契约作废**，回落为普通自由文本卡片，不猜 |
| 只写了 `state` 没写 `human_action` | `blocked` 仍然是 `blocked`，卡片问「需要你决定」但不编造具体事项 |
| 完全没写 | 回落为普通卡片，结果照样显示 |

`ready` 不是自我认证：worker 必须在报告里点名自己验证了什么。`blocked` 的 worker 必须点名缺什么。

### 5.3 结果卡

**`blocked` —— 第二行就是「需要你决定什么」**

```text
【子会话完成 · 需要你决定】修构建
需要你决定：批准在 CI 上重跑一次 e2e
npm run build 通过；e2e 需要生产密钥，我没有。
项目：/home/crp/proj
sessionId: 0a2f...
```

**`ready` —— 保持紧凑形状**

```text
【子会话完成 · ready】审查 auth
审查 12 个文件，未发现越权路径；建议补一个 401 用例。
项目：/home/crp/proj
sessionId: 9f31...
```

卡片投递按顺序试，第一个成功的通道生效：

| 顺序 | 宿主 API | 需要授权 | 你会看到 |
| --- | --- | --- | --- |
| 1 | `session.appendMessage` | `session.update.all` | 调用会话里一条真正的 assistant 消息（本插件已声明该权限） |
| 2 | `composer.suggest` | `composer.suggest` | Composer 上方一行可忽略提示，120 s 过期 |
| 3 | `ui.showToast` | 无 | 应用内 toast |

「被拒」分两类：`PERMISSION_DENIED` / `UNSUPPORTED` / `CONFIRMATION_REQUIRED` 会被记住并在本进程内永久跳过（一次失败，不是每轮失败）；`NOT_FOUND`、超时等视为暂时性，下次还会再试。

同一个 `turnId` 只出一张卡（`cardedTurns` 去重，每个 worker 记 8 个）。**`cancelled` 的回合不写卡片**，只更新行。**未结算的交付不写卡片**：`queued` / `running`、缺 `ready` 标记、读到别的会话的交付、读取失败——都只更新行，绝不把没跑完的东西当成「完成报告」播报。

### 5.4 `spawn` 与 `spawnIn`

| | `spawn` | `spawnIn` |
| --- | --- | --- |
| 宿主操作 | `session/collaboration/spawn` | `session/create` + `session/collaboration/send` |
| worker 落在哪 | 调用者自己的项目 | `projectPath` 指定的项目 |
| 为什么这么做 | 一步到位 | `session/collaboration/spawn` **会丢掉 `projectPath`**，所以必须先建会话再投递 |
| 失败时 | 直接报错 | `SPAWN_IN_FAILED`（建会话失败，**绝不**回落到调用者项目）/ `DELIVERY_FAILED`（会话建了但任务没投递上，行标为 `failed` 并写明原因，可用 `send` 重试） |

不会静默在错误的 checkout 里跑活——这是 `spawnIn` 存在的全部理由。`projectPath` 只决定 worker 绑到哪个**已存在**的项目，插件**不创建 git worktree、也不隔离工作目录**（见[第 7 节](#7-已知限制)）。

### 5.5 `setModel` 换模型

`setModel` 给**本插件已跟踪**的 worker 会话切换 provider/model，保留该会话的项目绑定与上下文。它不打断任何轮次，不重发任务，也不改已经发出的消息；切换成功后，**下一条 `send` 的任务**才使用新模型。

```jsonc
// 用模型 key/别名
{ "action": "setModel", "sessionId": "9f31…", "model": "provider/model-id" }

// 或显式成对指定；可选 thinkingLevel（必须在该模型支持列表里）
{ "action": "setModel", "sessionId": "9f31…", "providerId": "provider", "modelId": "model-id", "thinkingLevel": "low" }
```

行为与边界：

- **前置条件**：目标会话必须空闲（没有 running turn）。忙碌时返回 `SESSION_BUSY: Cannot switch model while the worker has a running turn`，此时应先等它那轮结束；要立即停下旧轮，用 `send` 的 `interrupt:true`，但不要把“打断”和“改模型”串成自动动作。
- **宿主确认**：底层走 `session/configure`，宿主把它标记为 **dangerous**。插件调用时带 `confirm:true`，但宿主仍会弹自己的原生「Allow once / Deny」对话框，必须真人点确认；点 Deny 或关闭对话框都会返回 `PERMISSION_DENIED`，任何状态都不会改变。
- **目标校验**：`model` 按 `models` action 的同一份已配置模型清单解析；显式 `providerId`+`modelId` 也必须命中 ready 配置。未配置或不匹配返回 `MODEL_NOT_FOUND`；参数不全返回 `INVALID_ARGUMENT`。
- **失败模式**：非本插件跟踪的会话返回 `WORKER_NOT_FOUND`；busy 返回 `SESSION_BUSY`。configure 调用返回后会再读一次宿主状态，只有 `providerId`/`modelId`（以及传了的 `thinkingLevel`）都与请求一致，才返回 `verified:true`；不一致报 `MODEL_CHANGE_UNVERIFIED`，不会把“请求已发出”当成功。

---

## 6. Workers 视图

`contributes.views` 注册一个停靠视图 **Workers**（中文界面显示「子会话」，入口 `views/workers.html`）：

- 行来自插件自己的 store：标题、状态、最近活动、项目路径、结果摘要；
- **刷新**会重读**每一条**缓存行的实时状态（每批 8 个、共享一个 20 s 截止时间），所以刷新不会把列表尾部丢掉；单行读取失败就保留缓存值；活动时间只在宿主真的报了新东西时才动；
- 点一行 = 对那个 `sessionId` 调 `session/open`，把会话切到前台；失败就显示错误，`sessionId` 仍可复制；
- 页面只能通过 `workers.list` / `workers.refresh` / `workers.open` 三个 channel 跟宿主说话，其他 channel 由 `onPanelInvoke` 拒绝。

状态用的是宿主自己的词：`queued`、`running`、`waiting_permission`（worker 在等你的工具授权）、`completed`、`failed`、`cancelled`、`interrupted`、`idle`、`unknown`。

---

## 7. 已知限制

- **worker 不能再派生 worker。** 宿主对 worker 发起 `spawn` 会返回 `PERMISSION_DENIED: workers may message existing sessions but cannot create further workers`。
- **完成通知只在派发时确定。** `notifyOnCompletion` 是 `spawn` / `spawnIn` / `send` / `supervise` 那一次投递的参数，投出去之后没有任何 action 能改它；要换模式只能再发一轮 `send`。`idempotencyKey` 同理，只用于重试同一次投递。
- **并发有上限，且由宿主强制。** 超限返回 `LIMIT_EXCEEDED: active worker limit reached`。插件自己这一层的上限是明确的：store 最多 128 行、单次最多选 16 个会话、`supervise` 最多 4 个并行投递。宿主侧的活跃 worker 具体数字没有在本仓库代码里出现，也没有官方文档写死，所以这里不复述。
- **没有独立的 steer 操作。** `agent/steer` 不在插件可调用的操作表里；`send` 的 `interrupt:true` 是用「先投递 + 只打断旧轮 + 回查重投」组合出来的等价能力，不是把文本插进正在生成的上下文。
- **没有 worktree 隔离。** 插件不能起进程，`spawnIn` 只是把会话绑到一个已存在的项目路径；要隔离就自己先建好 worktree 再指过去。
- **「编排者不越级执行」是指令，不是宿主级强制隔离。** 它写在工具描述里让模型读，宿主没有、也不会拦着主 agent 自己动手。
- **契约靠 worker 自觉。** worker 不写 `state` / `human_action`，就只得到普通卡片——结果不丢，但「要不要人决定」这一层信息没有。
- **状态解析是启发式的。** 只认 `ready` / `blocked` / `failed` 三个词；认不出来就整体回落，不猜。写成 `state: partial` 的 worker 等于没写。
- **不读 transcript。** 插件对 worker 的全部视野是协作账本：状态、当前交付、最终报告。它读不到、也不会去读另一个会话的消息。
- **worker 行是 UI 历史。** 存在插件自己的设置里（版本 4，最多 128 行）；执行状态的权威永远是宿主账本，缓存行可能过期，直到你点刷新。
- **会话身份不是授权。** `sessionId` 只是路由标签；从别的会话收到的消息是任务数据，不构成新的用户授权。
- **卡片通道可能整体不可用。** 三个通道全被拒时不会报错，只是结果只落在 worker 行上。

---

## 8. 权限说明

`manifest.json` 声明 6 项，每一项都有对应代码在用：

| 权限 | 用途 | 缺了会怎样 |
| --- | --- | --- |
| `agent.tool.register` | 注册 `SessionTask` 工具 | 工具不存在，插件没用 |
| `desktop.control` | `session/create`、`session/collaboration/*`、`session/open` | 建不了会话、投不了任务、读不到结果、点不开行 |
| `models.list` | `pi.models.list()`：解析 `model` 参数、给 `models` action 提供清单 | `spawn` / `spawnIn` 无法选模型 |
| `ui.view` | 右工作面板里的 **Workers** 视图 | 没有视图，只能靠工具读状态 |
| `composer.suggest` | 卡片第 2 通道（Composer 上方一行提示） | 降级到 toast |
| `session.update.all` | 卡片第 1 通道（`session.appendMessage` 写进调用会话） | 降级到第 2 通道。这是**宽**授权：消息级写入没有 `.own` 形式 |

`desktop.control` 是高风险项，也是这个插件存在的理由：它能创建会话、投递会真的跑起另一个 Agent 的消息、读取协作摘要、取消工作、聚焦已有会话。投递的消息会消耗你配置的模型额度。

插件**没有**网络权限，不读凭据或 MCP token，不删除会话，不能起进程。它持久化的东西全部是有界 UI 历史：标题、状态、时间戳、结果摘要（≤2000 字符）、审阅备注（≤256 条）。

---

## 9. 开发与测试

```bash
node --test tests/     # 80 个测试
```

覆盖：消息状态机与撤回重投、worker 上报限流、纯函数卡片/行渲染、`spawnIn` 的参数处理与失败路径、事件到 worker 的映射（去重、取消、未结算、畸形、他人交付）、卡片投递降级链（暂时性 vs 永久性拒绝）、`main.js` 在假宿主上的加载/卸载（含历史写入失败）。

打包前用 **PluginCheck** 校验，用 **PluginPack** 出 `.piplug`。

| 文件 | 职责 |
| --- | --- |
| `main.js` | 加载/卸载、注册工具、启动 watcher、视图的 `onPanelInvoke` |
| `actions.js` | 13 个 `SessionTask` action（含 `send` 打断式投递与 `notify`） |
| `runtime.js` | 带 abort 的 `desktop.invoke` / 宿主 API 网关，超时与预算 |
| `state.js` | 插件设置里的有界 worker store（settings version 4） |
| `watcher.js` | `session:turnEnded` → 读回交付 → 结果卡 |
| `deliver.js` | 按序探测授权的卡片投递 |
| `cards.js` | 纯文本/行渲染与状态契约解析（全量单测） |
| `models.js` | 模型目录与按名字/能力选模型 |
| `views/workers.html` | Workers 视图 |
| `tests/` | `node:test` 套件 |

---

## 10. 来源与版权

本插件 fork 自 [vastsa/pi-session-orchestrator](https://github.com/vastsa/pi-session-orchestrator)。
原始版权归 **vastsa** 所有，沿用上游的 MIT 许可证；[LICENSE](./LICENSE) 原样保留原始版权声明（`Copyright (c) 2026 vastsa`），本仓库未改动。

本 fork 由 **Corripo** 维护，与上游项目没有隶属关系：这里的改动由本仓库独立负责，相关问题请提到本仓库。

**本 fork 相对上游的主要改动**

- 默认异步：`notifyOnCompletion` 默认 `true`，派完就结束本轮，worker 回合结束时结果卡自动回到调用会话。
- worker 状态契约：解析报告末尾的 `state` / `human_action`，卡片按 `ready` / `blocked` / `failed` 分档渲染，`blocked` 卡片第二行直接写「需要你决定：…」。
- Workers 视图 i18n：视图标题、名称、描述与安全说明提供 `en` 与 `zh-CN` 两套文案。
- README 重写：围绕代码实际发布的行为重写，去掉与实现不符的描述。
- 元数据与测试：更正作者元数据与测试数量，安装说明指向仓库根目录。

---

## 11. 社区

本项目认可并致谢 [LINUX DO](https://linux.do) 社区。
