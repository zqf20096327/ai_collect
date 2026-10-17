# ST-AutoPulse 2.3.0

[English](README_EN.md) · [零基础图解指引](docs/QUICKSTART_CN.md) · [2.2.0 历史审计记录](docs/AUDIT_REPORT_CN.md)

让 SillyTavern 里的角色在私聊中主动联系你。2.2.0 引入了**每个角色独立的开关、间隔和提示词**；2.2.1 修复了从聊天主页面进入真实扩展设置的首次引导；2.2.2 加入待处理队列的付费调用确认并让嫉妒正文卡保留到用户点击 `×`；2.3.0 再把用户界面改成更准确的“离线待处理触发”，并提供一次调用的普通自动联系聚合回归。

## 先看结论

- 打开 Alice 设置的 10 分钟，只影响 Alice；切到 Bob 可以另设 30 分钟；再切回 Alice 会恢复 10 分钟。
- 2.3.0 的 8 步导览覆盖从 SillyTavern 主页面进入设置的完整路径。首次导览且抽屉关闭时，前两步会要求真实点击 `Extensions / 扩展设置` 入口和 `ST-AutoPulse` 标题栏；第 3 步介绍连接状态与离线待处理触发。
- **绿灯（服务端模式）**：多个私聊角色可各自在后台计时，关闭浏览器后仍可排队；重开时先显示数量和类型，只有你明确选择后才会合并生成、逐条生成、忽略或清空。
- **黄灯（前端模式）**：无需 Server Plugin，但只为当前打开的私聊计时；关闭或休眠页面后不能保证继续。
- 当前页面保持打开期间，嫉妒正文浮窗不会定时消失，也不会在第 4 条出现时淘汰旧消息；只有点击对应的 `×` 才关闭。
- 新角色默认关闭，必须由用户主动开启。
- 角色只改名称时，2.2.0 会沿用稳定角色身份，并分阶段迁移该角色的独立设置、timer、已排队事件、定时任务/outbox 和嫉妒独立 API 配置。服务端只迁移精确匹配的旧稳定 key，写盘失败可幂等重试；不会根据旧数字 ID 猜角色。删除后重建角色、重新导入成另一张卡或同时更换身份字段时，仍可能被视为新角色。
- 当前仓库**只负责私聊主动消息**。AutoPulse 的私聊计时、立即触发与经用户确认生成的待处理触发不会写入群聊；微信式群聊、群成员主动消息和群嫉妒由独立项目 [ChatPulseGroupLogic](https://github.com/NANA3333333/ChatPulseGroupLogic) 负责。

## 安装

### 1. 安装前端扩展

在 SillyTavern 打开 `Extensions（扩展） → Install Extension（安装扩展）`，粘贴：

```text
https://github.com/NANA3333333/ST-AutoPulse
```

也可以把仓库文件复制到：

```text
SillyTavern/public/scripts/extensions/third-party/ST-AutoPulse/
```

### 2. 安装 Server Plugin（推荐）

内置安装器只安装前端。若要绿灯后台模式，还要：

> **仅限可信单用户实例：** 多个访问者会共享插件数据与嫉妒独立 API 配置。多人共用的 SillyTavern 不要安装或启用 Server Plugin。

1. 建立 `SillyTavern/plugins/autopulse/`。
2. 把本仓库的 `server-plugin/index.js` 复制到该目录。
3. 在 SillyTavern 的 `config.yaml` 中设置 `enableServerPlugins: true`。
4. **重启 SillyTavern 的 Node.js 进程**，只刷新网页不够。

最终结构：

```text
SillyTavern/
├── public/scripts/extensions/third-party/ST-AutoPulse/
│   ├── index.js
│   ├── poll-worker.js
│   ├── settings.html
│   ├── style.css
│   └── manifest.json
└── plugins/autopulse/
    └── index.js
```

## 第一次使用

1. 打开一个**角色私聊**，先由你发送一条消息。
2. 回到 SillyTavern 主页面顶部或侧栏，**真实点击** `Extensions / 扩展设置` 入口（通常是方块/积木图标；手机端可能收在折叠菜单里）。
3. 在扩展设置列表中找到 `ST-AutoPulse`，再**真实点击**标题栏或右侧箭头展开。聊天输入区本身不会直接显示 AutoPulse 设置。
4. 看状态灯：绿色表示 Server Plugin 已连接；黄色表示当前页面前端计时。若绿色模式发现离线待处理触发，会先暂停生成并分开显示普通自动联系与定时任务数量；可选择合并、逐条生成、忽略当前角色、清空全部或稍后处理。
5. 在“当前角色的独立计时”中确认角色名无误，再打开“启用自动消息”。
6. 把间隔设为 1–180 分钟；第一次建议 5 分钟测试。
7. 可修改提示词，然后点击“立即触发”验证模型连接与角色语气。
8. 切换到第二个角色，重新进入 `Extensions / 扩展设置 → ST-AutoPulse` 并单独配置；两个角色的设置互不覆盖。

首次出现的 8 步箭头导览也遵循这条路径。抽屉关闭时，第 1、2 步会等待你点击高亮的真实入口，不会用“下一步”代替打开设置；第 3 步会指向连接与离线待处理触发卡。若设置已经打开，导览会自动跳到第一个尚未完成的步骤，避免再次点击把抽屉关掉。详细说明和手机端位置见 [零基础图解指引](docs/QUICKSTART_CN.md)。

## 功能

- 每角色独立自动消息计时与旧设置迁移
- 每天、每周和一次性定时任务（服务端模式）
- 离线待处理触发分类计数、一次调用的普通自动联系聚合回归、逐条生成与零 Token 忽略/清空（服务端模式）
- 情绪压力与回归反应
- 角色切换后的嫉妒浮窗（当前页面会话内由用户点击 `×` 关闭）
- 自定义提示词、桌面通知和 Slash 命令
- `/autopulse on|off|trigger|status|<分钟>`

## 常见问题

### 怎么选择 user？

AutoPulse 不另设 user 选择器。它使用 SillyTavern 当前选中的 Persona/User。请先在 SillyTavern 的 Persona 管理页选择身份，再开始聊天。

### 需要自己连接模型 API 吗？

普通主动消息使用 SillyTavern 当前已配置且能够正常回复的主模型连接，不需要在 AutoPulse 中再填一次主聊天 API Key。只有你主动为某个角色配置“嫉妒独立 API”时，Server Plugin 才会把该配置（包括 API Key）保存到 `SillyTavern/plugins/autopulse/jealousy-configs/`。这些文件是本地明文 JSON，并非加密保险库。把“嫉妒上下文深度”设为 `0` 时不会读取或发送私聊消息，但角色设定和本次嫉妒指令仍会发送。

嫉妒独立 API 的服务商会收到该角色的名称、描述、性格、场景、你选择深度内的最近私聊，以及嫉妒提示词。只填写你信任的 Endpoint；远程服务建议只用 HTTPS（本机 `localhost` 除外）。请限制插件目录和备份文件的读取权限，不要把它、API Key、配置页截图、生成正文或日志上传到 README、Issue 或群聊；Key 一旦公开，请立即到服务商后台轮换。“测试嫉妒弹窗”会真实调用一次独立 API 或 SillyTavern 主模型，并可能计费，不是零 Token 的界面预览。

### 世界书必须挂吗？

不必须。角色卡本身足够时可以不用；若你的设定依赖世界书，就按 SillyTavern 原本的方式绑定。AutoPulse 会沿用当前私聊上下文和 SillyTavern 已有绑定。

### 每次打开都有很多“离线待处理触发”，该选哪一个？

2.3.0 把原来的“离线消息”改名为**离线待处理触发**：它们只是普通自动联系计时器或定时任务留下的待办，还不是已经生成好的消息。Server Plugin 发现这些触发时会暂停消费；在你明确选择前，不会因它们调用模型，也不会自动补发。打开：

```text
Extensions / 扩展设置 → ST-AutoPulse → 离线待处理触发
```

点击“查看并决定如何处理”。弹窗会分别显示当前角色的“普通自动联系”和“定时任务”数量，然后选择：

- **合并为 1 条回归消息（1 次模型调用，推荐）**：只把当前角色积压的普通自动联系（timer）合成一次自然的“回来联系你”消息。无论有几条普通自动联系，都只调用一次模型；**定时任务不会被合并或删除**，仍留待你单独决定。
- **生成当前角色全部 N 条（可能 N 次调用）**：逐条处理当前角色的普通自动联系和定时任务，最多可能调用 N 次模型。其他角色仍保持待确认。
- **忽略当前角色 N 条（0 Token）**：删除当前角色的全部待处理触发，不调用模型，不影响其他角色。
- **清空全部，不生成（0 Token）**：删除所有私聊角色的待处理触发及尚待入队的定时任务 outbox，不调用模型；无需先打开某个角色。
- **稍后处理 / ×**：只隐藏弹窗；待处理触发和暂停状态都保留，不会在后台自行生成。

没有打开角色私聊时，合并、逐条生成和“忽略当前角色”会禁用；全局“清空全部”和“稍后处理”仍可使用。忽略或清空只删除尚未生成的触发，不会删除已经写进聊天记录的消息，**也不会关闭**各角色的自动消息计时器或定时任务。只要这些功能仍开启，之后还会产生新的待处理触发；若不想继续积压，请进入每个角色私聊关闭“启用自动消息”，并停用不再需要的定时任务。

若确认后数量或目标发生变化，本次生成会取消并要求按最新状态再次确认。点击角色级生成动作后若切到 Bob、群聊或 Alice 的另一个聊天窗口，插件会在下一次模型调用前停止，不能把 Alice 的触发生成到错误聊天。

电脑休眠、页面恢复显示、网络重连或切换到另一个聊天后，插件会先重新检查持久队列，再决定是否读取实时事件。因此 Alice 在你停留 Bob/群聊期间积压的触发，也会先进入确认。若普通 `/pending` 事件生成或聊天保存失败，自动消费闸门会立即关闭，并重新显示确认弹窗；在用户重新审查并明确选择前，不会直接重试下一次付费调用。因为失败前模型可能已经被调用，再次点击生成动作仍可能再次消耗 Token，也可以选择忽略或清空。

### 嫉妒消息为什么不会自己消失？

这是 2.2.2 的预期行为。当前页面保持打开期间，主版和 Lite 都会保留嫉妒正文卡，只有点击该消息右上角的 `×` 才关闭；刷新或关闭页面会清空这些仅存在于当前页面的通知。触发时另有一条 5 秒后淡出的短提示，它不是正文卡。通知很多时可以在右下角通知区域滚动查看。

### 能让不同角色卡在群聊里分别主动说话吗？

本仓库不能。2.2.0 起的“多角色独立”指**多个角色私聊分别计时**，不是群聊自动发言。AutoPulse 遇到群聊会明确拒绝写入，避免串角色；需要群成员分别主动发言、群嫉妒或角色群聊 API 时，请安装独立的 [ChatPulseGroupLogic](https://github.com/NANA3333333/ChatPulseGroupLogic)。

## 已知限制与安全边界

- AutoPulse 本身只处理私聊，不会向 SillyTavern 原生群聊写入自动消息；需要微信式群聊、群成员主动消息与群嫉妒时安装 [ChatPulseGroupLogic](https://github.com/NANA3333333/ChatPulseGroupLogic)。两个扩展可同时安装，但私聊和群聊的计时、嫉妒及 API 设置保持独立。
- **Server Plugin 仅支持可信的单用户部署。** 同一个 SillyTavern 进程中的所有访问者会共享 AutoPulse 的 timer、定时任务、离线队列和嫉妒独立 API 配置；这些数据没有按 SillyTavern 账号或用户隔离。`data.json`、`queue.json` 和 `jealousy-configs/` 会以本地明文 JSON 保存角色标识、提示词/任务等队列元数据及独立 API 配置，并非加密保险库。不要在多人共用实例上启用它，并限制整个插件目录及备份的读取权限。多人使用时，请为每个人运行拥有独立目录的 SillyTavern 实例，或只使用不带共享服务端状态的前端模式。
- Server Plugin 的队列有持久化与事件去重，但服务端尚未提供跨窗口原子 claim；**两个 SillyTavern 窗口仍可能同时抢同一条待处理触发**。这是低频多窗口场景的已知限制，建议同一时刻只让一个窗口处理 AutoPulse 队列。
- 为防止角色列表重排后串角色，升级时只带旧数字 `characterId`、没有稳定 `characterKey` 的定时任务和队列事件不会被猜测性绑定；它们会被隔离或清理。请在正确角色私聊中重新创建这类旧定时任务。普通角色重命名使用服务端精确 key 迁移：新嫉妒配置已存在时以新配置为准；旧配置存在时，只有确认新 key 已有配置或新副本写入成功后才会删除旧副本。
- 新建定时任务使用仅含字母、数字、`_`、`-` 的安全 ID。升级前已存在的特殊 ID 仍可查看、修改和删除；前端会把角色名、正则、任务内容与旧 ID 当作纯文本/属性值处理，不拼接为 HTML。
- `ST-AutoPulse-Lite/` 已在本仓库修复；独立的 `ST-AutoPulse-Lite` GitHub 仓库尚未由本次工作同步。
- 本仓库采用 **CC BY-NC-ND 4.0**。它允许署名、非商业地分享未修改副本，但禁止分发修改版或衍生版；因此它不符合通常允许修改与再分发的“开源软件许可证”定义。

## 测试状态

### 2.3.0 当前源码与实机验证

当前导览路径固定为：

```text
SillyTavern 主页面
    ↓ 第 1 步：用户真实点击
Extensions / 扩展设置
    ↓ 第 2 步：用户真实点击
展开 ST-AutoPulse
    ↓ 第 3–8 步
连接与离线待处理触发 → 当前角色 → 启用 → 间隔 → 提示词 → 立即触发
```

首次自动导览且抽屉关闭时，第 1、2 步不能靠“下一步”跳过真实操作；只有对应抽屉确实展开后，导览才进入插件设置控件。手动重播时，如果某层设置已经打开，导览会识别其状态并从第一个尚未完成的步骤继续。第 3 步和全局决策弹窗使用“离线待处理触发”名称。

最终执行 `npm run verify` 的结果：

| 验收层 | 结果 |
|---|---:|
| 自动化测试 | **188/188 PASS**：主客户端 123、Server Plugin 46、Lite 19 |
| 嫉妒通知 | **PASS**：主版/Lite 创建 0 个自动关闭计时器，不限制 3 条；只删除被点击 `×` 的目标通知 |
| 普通计时器处理 | **PASS**：可把当前角色多次普通联系合并为一次模型调用，也可选择逐条生成 |
| 定时任务边界 | **PASS**：计划任务不会进入普通计时器聚合；聚合后继续保留，等待单独决定 |
| 零 Token 动作 | **PASS**：“忽略当前角色”和“清空全部”都不会调用模型或写入聊天 |
| `/pending` 故障门禁 | **PASS**：普通 `/pending` 事件生成或保存失败后会关闭自动消费，必须先重新审查，不能直接重试付费调用 |
| 桌面端/手机端实机界面 | **PASS**：SillyTavern 1.18.0 中正确显示总数、角色分类计数、调用成本和五种决定 |

当前无 Key 的机器可读结果：

- [`docs/test-data/autopulse-2.3.0-validation.json`](docs/test-data/autopulse-2.3.0-validation.json)：188/188 自动化与安全边界汇总。
- [`docs/test-data/autopulse-2.3.0-browser.json`](docs/test-data/autopulse-2.3.0-browser.json)：桌面端、手机端弹窗状态、按钮标签与截图记录。
- [`docs/test-data/autopulse-2.3.0-live-ui-replay.json`](docs/test-data/autopulse-2.3.0-live-ui-replay.json)：当前 2.3.0 源码的 14 张私聊、任务、压力、回归、嫉妒、Slash 与群聊边界截图，含路由和卡片计数证据。
- [`docs/test-data/autopulse-2.2.2-validation.json`](docs/test-data/autopulse-2.2.2-validation.json)：上一版付费调用门禁的历史报告。

#### 2.3.0 当前源码全功能实机图册

以下 `20–33` 截图在 SillyTavern `1.18.0` 中安装本仓库当前 `2.3.0` 前端与 Server Plugin 后实际点击拍摄。两名角色、计时器、一次性任务、压力、回归、嫉妒通知、Slash 命令和群聊拒绝都走当前源码路径。

本轮运行环境无法稳定连出到 DeepSeek 官方接口，所以生成请求由本地 OpenAI-compatible 测试端点接住，并回放仓库中已经保存的真实 DeepSeek AIRP 输出。报告明确标记 `fixtureReplay: true`、`providerCallThisRun: false`，不把这次界面回放冒充成新的外部 API 成功。历史真实输出来源、原 Run ID、当前源码哈希、每次触发类型和截图 SHA-256 均写入机器报告。

| 沈砚秋：独立 5 分钟设置 | 沈砚秋：主动私聊写入当前聊天 |
|---|---|
| ![当前 2.3.0 中沈砚秋启用独立五分钟计时与角色提示词](docs/screenshots/20-v230-shen-private-settings.png) | ![当前 2.3.0 中沈砚秋主动私聊消息与成功通知](docs/screenshots/21-v230-shen-private-message.png) |

| 弥拉·周：独立 20 分钟设置 | 弥拉·周：主动私聊写入当前聊天 |
|---|---|
| ![当前 2.3.0 中弥拉周启用独立二十分钟计时与角色提示词](docs/screenshots/22-v230-mira-private-settings.png) | ![当前 2.3.0 中弥拉周主动私聊消息与成功通知](docs/screenshots/23-v230-mira-private-message.png) |

机器报告同时保存沈砚秋 `5` 分钟、弥拉·周 `20` 分钟且二者均启用，证明第二个角色不是共用一个默认计时器。截图中的两段回放输出也分别保留旧书店主与深空机械师的角色口吻。

| 一次性“巡夜提醒”任务 | 任务到点后单独发出 |
|---|---|
| ![当前 2.3.0 中创建并启用一次性巡夜提醒定时任务](docs/screenshots/24-v230-scheduled-task-settings.png) | ![一次性定时任务到点后在私聊中实际写入消息](docs/screenshots/25-v230-scheduled-task-fired.png) |

该任务触发后状态变为停用并记录最后触发分钟；它走 `scheduledTask` 路径，不会混入普通计时器的离线聚合。

| 压力等级 3 设置与测试 | 压力联动消息 |
|---|---|
| ![当前 2.3.0 压力系统设置到等级三并依次测试](docs/screenshots/26-v230-pressure-level3-settings.png) | ![压力等级联动后实际写入的角色私聊消息](docs/screenshots/27-v230-pressure-message.png) |

![用户回归反应测试与实际私聊消息](docs/screenshots/28-v230-return-reaction.png)

压力与用户回归是私聊内的两条独立触发路径；报告分别记录 `pressure: true` 和回归测试动作，不与群聊主动消息共享状态。

| 每角色嫉妒独立 API | `/autopulse status` 实际输出 |
|---|---|
| ![沈砚秋嫉妒独立 API 配置窗口，Key 内容已清空](docs/screenshots/29-v230-jealousy-independent-api.png) | ![当前 2.3.0 Slash status 命令的状态提示](docs/screenshots/32-v230-slash-status.png) |

嫉妒独立 API 按角色配置。当前界面实际命中所配置的独立兼容端点 4 次；这证明专属路由选择和请求处理，但本轮端点是本地回放端点，不代表新的 DeepSeek 直连成功。截图中没有可用 Key，清理检查也确认 SillyTavern Secrets 和 `jealousy-configs/` 均无测试凭据残留。

| 等待 15 秒后 4 条正文卡仍保留 | 点击一条 `×` 后只剩 3 条 |
|---|---|
| ![四条嫉妒正文通知等待十五秒后仍全部保留](docs/screenshots/30-v230-jealousy-four-persistent.png) | ![点击其中一条嫉妒通知关闭按钮后只删除该条](docs/screenshots/31-v230-jealousy-after-close.png) |

这两张图专门验证用户提出的通知行为：嫉妒正文卡不会按时间自动消失，也不会因为出现第 4 条而淘汰旧卡；只有点击对应 `×` 才关闭该条。

![AutoPulse 在原生群聊拒绝角色计时，同时 ChatPulse Group Logic 已安装](docs/screenshots/33-v230-native-group-refusal-with-cpgl.png)

上图是两个项目的共存边界：SillyTavern 原生群聊中，AutoPulse 显示“群聊（不支持角色计时）”并拒绝把私聊自动消息写入群聊；同一扩展页可见 `ChatPulse Group Logic`。真正的微信式群成员主动消息和群嫉妒由后者处理。两者可以同装，但**私聊主动/私聊嫉妒**与**群主动/群嫉妒**的计时器、API 配置和触发链彼此独立；群嫉妒只并入 ChatPulse Group Logic 自己的那一条群主动消息，不会调用 AutoPulse 的私聊嫉妒。

#### 2.3.0 离线待处理触发实机弹窗

实机队列共 5 条：当前角色 Seraphina 有 3 条普通自动联系和 1 条定时任务，其他角色 1 条。下面是**用户决定如何处理离线触发**的真实弹窗；它不是角色已经自动生成或自动补发了 5 条消息。

| 桌面端 `1366×768` | 手机端 `390×844` |
|---|---|
| ![桌面端离线待处理触发决策弹窗，显示普通自动联系与定时任务分类以及五种处理动作](docs/screenshots/18-desktop-offline-pending-decision.png) | ![手机端离线待处理触发决策弹窗，操作按钮纵向排列](docs/screenshots/19-mobile-offline-pending-decision.png) |

两端都显示：合并只处理 3 条普通自动联系并生成 1 条回归消息；“生成全部 4 条”可能调用 4 次；定时任务不会被普通聚合消费；忽略当前角色和清空全部是零 Token 动作。

### 2.2.1 历史实机导览

2.2.1 源码曾在 SillyTavern 1.18.0 桌面端和手机端各完成 **8/8** 步定位：首次 Persona 弹窗结束后才显示导览；前两个入口中心命中真实控件；抽屉动画结束后才推进；“上一步”和“完成”不会关闭设置面板。五个前端文件与安装副本的 SHA-256 全部一致。机器可读记录见 [`docs/test-data/onboarding-2.2.1-browser.json`](docs/test-data/onboarding-2.2.1-browser.json)。

### 2.2.0 功能实现的历史实机验收

2026-07-27 已把 2.2.0 功能实现逐文件复制到 SillyTavern 1.18.0，并在每张截图前核对源码、安装目录与锁定 SHA-256。下面的 32/32、9/9、模型探索与 `01–12` 截图都属于这次历史验收；它们继续证明私聊计时、跨窗口读取、隔离和群聊拒绝边界，但不用于证明 2.2.1 新增的前两步入口交互。

| 验收层 | 结果 | 说明 |
|---|---:|---|
| 自动化测试 | **137/137 PASS** | 主客户端 77、Server Plugin 43、Lite 17 |
| SillyTavern + DeepSeek 实机记录 | **32/32 PASS** | 功能实现快照；保留 10 张私聊/边界真实浏览器截图 |
| Server Plugin v3 HTTP 集成 | **9/9 PASS** | 真实启动 SillyTavern 进程，两个角色计时器互不重置 |
| 额外模型随机性探索 | **35 次调用** | 31 个严格启发式检查通过 26 个；详见下方说明 |

机器可读原始结果见 [`docs/test-data/`](docs/test-data/)；其中不包含 API Key。

实机环境：SillyTavern `1.18.0`（`8172dcd0ee67…`）、DeepSeek 官方 API、`deepseek-v4-flash`。Run ID 为 `71106c21-9479-4564-a421-c4d1fa618e54`；该次运行的前端 `index.js` SHA-256 为 `fa2dacc93b4b57850a9d6c54e2772f1603091a0e42d626b4e663afca04d10677`，Server Plugin 为 `68c357ba5676a2033fb800ffd574bb3e8200629d6c0feec009c96c35f49d2c17`。

本轮实际验证了：

- 沈砚秋 `5` 分钟 → 弥拉·周 `20` 分钟 → 切回沈砚秋仍为 `5` 分钟，服务端同时存在两个独立 v3 timer。
- 第二个独立浏览器窗口能看到已保存的消息、保持 5 分钟设置，并从真实聊天记录准确召回测试暗号“松针-27”。
- 弥拉私聊不知道沈砚秋私聊中的暗号；新聊天不会凭空继承旧聊天秘密。
- 群聊页面明确禁用 AutoPulse；尝试前后私聊消息数、两个 timer 与离线队列均未变化。
- 测试结束后已恢复原 SillyTavern 设置并删除临时 API Key；仓库、截图、报告和测试数据残留扫描为 0。

### 2.2.1 历史实机导览截图

| 第 1 步：桌面端 Extensions 入口 | 第 2 步：桌面端展开 ST-AutoPulse |
|---|---|
| ![桌面端高亮 Extensions 扩展设置入口](docs/screenshots/13-desktop-tour-extensions-entry.png) | ![桌面端高亮 ST-AutoPulse 标题栏](docs/screenshots/14-desktop-tour-autopulse-entry.png) |

| 第 3 步：桌面端连接状态 | 手机端第 1 步：Extensions 入口 |
|---|---|
| ![桌面端高亮连接状态](docs/screenshots/15-desktop-tour-connection.png) | ![手机端高亮 Extensions 扩展设置入口](docs/screenshots/16-mobile-tour-extensions-entry.png) |

![手机端高亮 ST-AutoPulse 标题栏](docs/screenshots/17-mobile-tour-autopulse-entry.png)

### 2.2.0 历史功能验收截图

> `01–03` 是旧版 10 步新手引导截图，画面中的 `/10` 计数属于 2.2.0 历史界面。2.2.1 的 8 步导览请看上面的 `13–17`；2.3.0 第 3 步使用“离线待处理触发”说明。

| 历史桌面引导：连接状态 | 历史桌面引导：每角色间隔 |
|---|---|
| ![桌面新手引导高亮连接状态](docs/screenshots/01-desktop-tour-connection.png) | ![桌面新手引导高亮消息间隔](docs/screenshots/02-desktop-tour-interval.png) |

| 历史手机竖屏引导 | 沈砚秋手动 AIRP |
|---|---|
| ![手机端新手引导高亮当前角色](docs/screenshots/03-mobile-tour-character.png) | ![沈砚秋真实角色扮演对话](docs/screenshots/04-shen-manual-roleplay.png) |

| 沈砚秋独立 5 分钟 | 弥拉·周独立 20 分钟 |
|---|---|
| ![沈砚秋五分钟主动消息计时](docs/screenshots/05-shen-autopulse-5min.png) | ![弥拉二十分钟主动消息计时](docs/screenshots/06-mira-autopulse-20min.png) |

| 切回沈砚秋恢复 5 分钟 | 第二窗口持久化与记忆 |
|---|---|
| ![切回沈砚秋恢复五分钟](docs/screenshots/07-shen-restored-5min.png) | ![第二窗口读取聊天并召回暗号](docs/screenshots/08-cross-window-persistence.png) |

| 弥拉私聊隔离 | 群聊 AutoPulse 明确拒绝 |
|---|---|
| ![弥拉不知道另一私聊的秘密](docs/screenshots/09-mira-private-isolation.png) | ![群聊页面禁用AutoPulse](docs/screenshots/11-group-autopulse-rejected.png) |

![修改后源码测试数据总览](docs/screenshots/12-test-summary.png)

### 如何看待 26/31 的模型探索结果

这 31 项是插件验收之外的多次模型随机采样，不是“产品通过率”。其中沈砚秋的**逐字、逐位置**回忆为 1/5，另外 4 次仍记得赤铜钥匙与“玻璃海”，但书名或藏放位置发生偏差；弥拉的严格回忆为 5/5。与本仓库直接相关的结果包括双向私聊隔离 6/6、新聊天无凭空记忆 3/3、两角色主动消息人设 6/6。

这说明普通上下文记忆会受模型随机性和提示词影响，不能把“跨窗口打开同一聊天”误写成长期记忆插件。正式的修改版 UI 验收另行执行并为 **32/32 PASS**，其中同一聊天跨窗口的实际暗号召回通过。

本地验证：

```bash
npm run verify
```

## License

Copyright © 2026 NANA3333333。原始源码、文档与资产采用 [CC BY-NC-ND 4.0](LICENSE)，第三方材料仍受各自许可约束。
