# Arena-Agents · AI 狼人杀（Werewolf）多智能体博弈沙盒

[English](README.en.md) | **简体中文**

**Arena-Agents 是一个开源的 AI 狼人杀、社交推理与多智能体博弈沙盒。** 游戏规则写在 Markdown
剧本中；**每一位玩家和主持人都是异步 Agent**（前端 Actor 随时收发消息，后端 Worker 负责思考和
工具调用），由 LLM 主持人按剧本手册推进流程，引擎只提供与游戏无关的频道、发言权、请求与账本。
项目内置一套完整的 12 人狼人杀，也可以用同一引擎运行其他社交推理、剧本杀或桌游规则。

关键词：**AI 狼人杀、狼人杀、多智能体狼人杀、AI 多智能体博弈、社交推理、LLM 智能体、
AI 桌游、AI 剧本杀、social deduction、AI Werewolf、LLM Werewolf**。

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.14.0-blue.svg)](CHANGELOG.md)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg)](https://fastapi.tiangolo.com/)

<img src="docs/images/v014-main-view.png" alt="AI 狼人杀实时对局主界面（上帝视角）：像素头像 + 座位气泡 + 身份标签、状态与视角标签、密封投票请求卡片" width="100%">

## 主要能力

- **玩家是 bot：名字 + 头像 + 四层记忆（v0.14）**：座位只是“这一局坐在哪里”，开局前可以拖动卡片换座，bot 的记忆和模型不受影响。
  每个 bot 有四层记忆——**L0 底层设定**（身份 / 说话方式 / 分析方式，只有你能改）、**L1 架构**（官方契约 + 自己的操作笔记）、
  **L2 规则**（官方剧本 + 自己的规则要点 / 打法 / 待解问题 / 对其他玩家的印象）、**L3 对局**（状态板、硬事实台、可见历史、笔记）。
  编排器（Composer）把各层按固定顺序挂进提示词：系统提示词一局内逐字节不变（供应商的前缀缓存照常命中），自己的记忆写成第一人称
  的段落而不是清单，轮到发言、投票的那一刻再按情境标签提醒一两条相关的打法——同一个模型也能说出明显不同的风格。
  12 个默认 bot（Alice…Leo）随仓库提供，单个 bot 可以导出 / 导入（`.arenabot`）。详见 [docs/bots.md](docs/bots.md)。
- **初始化与复盘（v0.14）**：提示词里不教打法。bot 先**初始化**——读官方契约和规则，用自己的话写下操作笔记、规则要点和打法
  （每个最多 120 秒，全有或全无）；终局后弹窗询问是否**复盘**——每个 bot 最多 60 秒，对照真相修订自己的记忆（写入直接生效，
  到点时已写的保留）。底层设定只有你能改：复盘最多提出建议，由你采纳；真人接管过的座位还可以让 bot 学接管者的说话方式。
  ⚠ 表示契约、剧本或底层设定变了、需要重新初始化；没准备好的 bot 会被**开局检查**拦下，并按玩家列出要做什么。
- **发言只来自 bot 自己（v0.14）**：超过单条字数上限不再被截断，而是以 `TOO_LONG` **退回**（发言权不消耗，真人和 bot 一样）；
  读起来像报告的发言（分条列项、标题、自报座位号）以 `FORMAT` 退回一次，由 bot 用自己的话重写。引擎和编排器没有任何代发、
  改写的路径，提示词也不再要求“思考要简短”。
- **身份开局才发牌（v0.14）**：开局前不存在、也不显示任何身份信息（没有标签，也没有 “?”）；点“开始”并通过开局检查后才发牌。
  「重新发牌」已删除。
- **设置五栏与新的文件格式（v0.14）**：⚙ 设置分为 ① 总存档 ② 底层设定 ③ 官方契约 ④ 规则 ⑤ 对局管理。总存档（`.arenaagents`
  格式 2，仍能导入 v0.13 的）现在包含数据目录里的全部文件，日志不再可选；单个 bot（`.arenabot`）和单局对局（`.arenagame`）
  也能导出 / 导入。API Key 的处理不变：可选导出，只有 Key 用你设的密码加密。
- **座位气泡、状态与视角标签（v0.14）**：卡片左上角的半透明气泡是座位号，名字旁的 ✔ ⚠ ✖ ⏳ ○ 是初始化状态；顶栏第二行是**状态标签**
  （未初始化 / 初始化中 / 对局前 / 对局中 / 已暂停 / 已结束 / 复盘中）和**视角标签**（全局视角 / Alice 视角 / Alice 视角（接管））。
- **基准（v0.14）**：`bench/` 提供可复现的基准套件，量化“发言风格是否不同”和“是否依据硬事实判断”；v0.13.1 的玩家
  （`LegacyBrain`）是基线。详见 [bench/README.md](bench/README.md)。
- **亲自下场：接管一个座位（v0.13）**：对局未开始或已暂停时，在视角标签的菜单里选「接管 X」，就能扮演某个玩家——它的 agent
  暂停、不再产生 token，你看到该座位的视角；退出接管（同样只在不运行时）后座位交还给 agent，它下次醒来会拿到包括
  你的发言在内的完整历史。开局前也可以接管（v0.14：那时还没有发牌，开局后你才看到自己的身份）。你的每个动作都走和 agent
  完全一样的提交闸门：轮次、字数（超长同样以 `TOO_LONG` 退回）、条数、截止时间都不变。
- **接管不停手，agent 可软暂停（v0.13.1）**：接管栏可让 agent 在收完当前回答后停下，时钟同时冻结；
  你仍能慢慢阅读、发言、作答和使用技能，公共频道轮到你时**不限时**，请求仍按原截止时间。还可以给其他座位加
  8 种颜色 / 形状的私人标记，只保存在本浏览器，不赋予颜色任何规则含义。
- **每个频道一个输入框（v0.13）**：像多人聊天软件，切换频道就换成该频道自己的输入框（草稿各自保留，实时显示字数与上限，超限时发送按钮禁用）。
  没轮到你、发言权已结束、频道被关闭 / 冻结 / 只听时，输入框仍可打字，发送按钮变成灰色的「禁言中」（悬停看原因）；
  持有发言权时有「结束发言」；「技能」按钮释放白狼王自爆等主动技能；投票、选择之类的请求卡片先点选、再点「提交」，
  防止误点直接作答，带倒计时。
  质询主持人用和主持人的私聊。
- **一个文件的存档（v0.13）**：总存档是单个 `.arenaagents` 文件——内容（bots、对局、日志、Provider…）不加密，只有 API Key
  可选导出并用你设的强密码加密；导出 / 导入都有进度，导入会校验版本和每个文件的校验值，整体替换前先备份、失败自动回滚。
  附带 v0.12.1 → 存档的转换脚本。
- **历史对局与重放（v0.13）**：列出每一局，可继续、删除（删除不会撤销 bot 已经通过复盘学到的东西）或**重放**——暂停、
  0.5×–8× 倍速、可拖动进度条、跳过空闲，还能切换视角。v0.14 起设置里的「对局管理」还显示每局的状态、复盘进度和文件大小，
  并能导出 / 导入单局（`.arenagame`）。
- **思考记录与错误日志（v0.13.1）**：玩家 / 主持人详情里的「思考记录」用聊天气泡展示每次唤醒的思考与正文，
  不夹工具调用；右上角「日志」列出当前局的 LLM 调用、重试、超时与错误，可按角色筛选、只看错误。
  接管未终局时不能查看其他玩家的思考记录。
- **全员异步 Agent（v0.12）**：每个玩家和主持人都是 Actor + Worker。Actor 永远能收发消息，
  不会被思考或工具执行阻塞；发言、投票、质询和能力随时可以发生，引擎在**提交的那一刻**校验。
- **引擎不替你省钱（v0.12.1）**：每一条投递给 agent 的消息都会立刻唤醒它（没有防抖、没有轮数上限、没有
  “执行深度”），狼人可以随时“拍刀”、白狼王随时自爆；agent 只有三种状态——思考 / 行动 / 休眠，
  `sleep(秒数)` 可以给自己设闹钟。token 靠**编排**管理：每个 agent 一条持久的只追加对话（命中供应商的
  前缀缓存）、运行中到达的消息合并注入、窗口快满时才压缩。
- **预算上限（按局）**：顶栏的 token / 金额统计旁有一个上限按钮，可设 token 和 / 或美元上限，并选择
  “达到上限后强制停止”；80% 变黄，100% 提示或暂停（原因“预算”）。费用按**四类 token**
  （未命中缓存的输入 / 缓存读 / 缓存写 / 输出）和四个价格精确计算。
- **价格源**：Provider 对话框里可从价格表（默认 LiteLLM 的 `model_prices_and_context_window.json`）
  自动填入模型的四个价格和上下文窗口，你仍可手动修改。
- **像素头像**：每个 bot 有一个由程序化素材库随机组合的像素头像（可重新生成全部或单个；主持人也有一个随机头像；
  可复制头像编号、按编号精确重建）。默认 bot 的头像是固定的。
- **自适应界面**：从 1920 宽屏到手机竖屏都能用（按平台与宽度自动切换布局）。
- **LLM 主持人驱动流程**：轮流发言 = 主持人公告 + 发言权管理（`set_floor_queue` 等工具）；
  规则文本与“主持人手册”写在剧本里，引擎本身不含任何游戏词汇。
- **频道与发言权**：可见性只由频道决定；主持人可随时关闭发言权（玩家收到“无发言权”回执），
  发言既有时间限制也有字数限制（超长会被退回重写，不会被截断）；玩家可以私聊质询主持人，主持人可以惩罚骚扰者（关闭其私聊）。
- **只追加的账本**：所有已发生的事都记在账本里，存档、上下文和观战都以它为准；主持人可以改玩家的
  当前状态（出局、复活…），但不能改写历史。
- **可执行 Markdown 剧本（schema v2）**：身份池、模板、能力、检查项和默认限额写在
  `scenarios/*.md` 的 front matter 中，正文是规则说明和只给主持人看的手册。
- **多 Provider / 多模型**：支持 OpenAI Chat Completions、OpenAI Responses、Anthropic
  Messages；主持人及每位玩家可以使用不同模型和思考深度。
- **模型模板**：保存 3 个 Provider/模型/思考深度预设，勾选玩家后一键应用。
- **数据在程序目录下（v0.13）**：只有一个数据目录 `<程序目录>/data/`——不再有“工作文件夹”可选；
  `ARENA_DATA_DIR` 可以覆盖，Docker 里是 `/app/data`；`data/` 已被 `.gitignore` 排除。
  Provider、模板、绑定、bots、官方契约、规则、对局、日志都在里面。
- **安全运行**：对局运行中锁定模型绑定、接管和导入；进程锁保证同一个数据目录只有一个服务在用。
- **只加密 API Key**：Key 单独存放在 `secrets.v1.enc`（AES-256-GCM；Windows 的主密钥由 DPAPI 保护），
  其余数据（bots、契约、规则、对局、日志、设置）都是明文，可直接查看、备份。
- **API 端点预览**：保存 Provider 前显示最终消息地址和模型列表地址；支持自动拼接 `/v1/...`
  或直接填写完整自定义 endpoint。
- **观战界面**：玩家用像素头像 + 名字 + 身份标签（开局后才有）表示，点击玩家卡片看 bot 面板、思考记录和 token 统计；
  信息流只显示发言和请求卡片（整条渲染，不流式），支持“上帝视角”和任意玩家视角。
- **演示模式**：`ARENA_DEMO=1` 用脚本化机器人代替模型，不需要 API Key 就能完整体验一局（12 个 bot 一开始就是 ✔，
  初始化和复盘也由演示机器人用固定回答完成）。

## 界面截图

| 开局检查：没准备好的 bot 会被拦下，弹窗按玩家列出原因（v0.14） | bot 面板：名字与头像、初始化状态、底层设定编辑器（v0.14） |
|---|---|
| <img src="docs/images/v014-start-check.png" alt="开局检查弹窗：按玩家列出没有准备好的 bot（底层设定变了需要重新初始化、上次初始化失败、还没有初始化、底层设定还没有写），每一条都有“去初始化”“去导入底层设定”等按钮；对局没有开始，也没有发牌" width="100%"> | <img src="docs/images/v014-bot-panel.png" alt="bot 面板：名字与头像（初始化后冻结）、已初始化状态与“重新初始化”、思考记录、底层设定的三个必填分区和附加分区、字数计数" width="100%"> |
| **⚙ 设置：五栏——总存档 / 底层设定 / 官方契约 / 规则 / 对局管理** | **终局复盘弹窗：选择让哪些 bot 复盘（每个最多 60 秒）** |
| <img src="docs/images/v014-settings.png" alt="设置对话框：总存档（导出 / 导入）、底层设定、官方契约、规则、对局管理五栏" width="100%"> | <img src="docs/images/v014-review.png" alt="终局弹窗：12 个 bot 默认全选，可以全选 / 全不选，选“暂不”或“复盘”" width="100%"> |
| **玩家视角（接管 Carol）：开局后别人的身份是“?”，只看到该玩家可见的内容** | **深色主题** |
| <img src="docs/images/v014-player-view.png" alt="玩家视角：视角标签显示“Carol视角”，其他玩家的身份标签是“?”" width="100%"> | <img src="docs/images/v014-main-dark.png" alt="深色主题的对局界面：座位气泡、对局状态条、公共频道" width="100%"> |
| **手机竖屏（迷你卡片 + 底部标签栏；这里正在接管 Carol）** | **token / 费用上限（按局，可强制停止）** |
| <img src="docs/images/v014-phone.png" alt="手机竖屏：视角标签与接管栏占前两行，下面是 6×2 迷你卡片、公共频道和底部标签栏" width="60%"> | <img src="docs/images/v014-budget-dialog.png" alt="token / 费用上限对话框：用量进度条、两个上限、强制停止开关、四类 token 明细" width="100%"> |
| **Provider 管理：价格源与四个价格** | **模型模板与绑定** |
| <img src="docs/images/provider-modal.png" alt="Provider 管理：价格源与四个价格" width="100%"> | <img src="docs/images/templates-bindings.png" alt="模型模板与绑定" width="100%"> |

> 截图来自本地**模拟服务**（`tools/mock_ui_server.py`：脚本化的演示数据，不调用任何模型）；Provider 是一个演示用的示例（密钥为占位符），不包含任何真实凭据；图中的路径、名称和数字都是虚构的。

详细操作见 [docs/ui-guide.md](docs/ui-guide.md)。

## 架构：Actor + Worker

引擎的核心只有一个想法：**每个角色（12 名玩家 + 主持人）都是一个异步 agent，由前台的 Actor 和后台的 Worker 两半组成。**

- **Actor 永远在线。** 它是 agent 的信箱：同步、不阻塞、从不调用模型。世界里每提交一条记录，就给每个能看到它的 agent 投递一个 Envelope；休眠的 agent 立刻被唤醒——没有防抖，没有“只唤醒重要消息”的省钱规则。
- **Worker 负责思考。** 一次激活 = 一个 asyncio 任务：打开（或延续）这个 agent 的**那一条持久对话** → 调用模型 → 执行工具 → 合并运行中到达的新消息 → 再调用模型……直到 agent 自己调用 `sleep`。一次激活里没有轮数上限，唯一的刹车是你设的预算。
- **世界只认“提交”。** agent 的每个动作（发言、投票、能力、质询……）都是一个 Intent，在**提交的那一刻**由世界的提交闸门重新校验（发言权、成员、字数、是否过时……）。所以“agent 想的时候世界变了”不会写出错误的东西；取消在途的调用只是为了不浪费 token，不是正确性的保证。

### 整体

<img src="docs/images/arch-overview.zh.svg" alt="Arena-Agents 整体架构：浏览器、FastAPI、GameOrchestrator、Runtime（Actor + Worker）、Brain、World，以及 LLM 适配器、数据目录与剧本" width="100%">

自上而下：浏览器用 REST 控制、用 SSE v2 观战 → FastAPI → **GameOrchestrator** 管理一局的生命周期（创建世界和 13 个 agent、预算、bot 阵容与开局检查、初始化与复盘、加密存档）→ **Runtime** 里每个 agent 是 Actor + Worker，**Supervisor** 把世界的投递泵给它们 → **Brain** 把世界翻译成模型读得懂的提示词和工具，再把工具调用翻译回 Intent → **World** 的提交闸门与只追加的账本。实线是调用与数据，虚线是通知（Envelope 唤醒 agent，UiEvent 推给浏览器）。

### Actor：永远在线的信箱

<img src="docs/images/arch-actor.zh.svg" alt="Actor 的判断树：deliver 把信封放进 pending；休眠就 call_soon 安排一次激活；运行中就合并，或在 interrupt 命中焦点时取消在途调用；另有闹钟、失败重试和停止" width="100%">

- 休眠的 agent 收到信封 → **安排一次激活**（同一次泵里投递的合成一次，没有定时器）。
- 运行中的 agent 收到信封 → **留在 pending，下一轮边界合并**成一条 DELTA，不打断。只有 `interrupt`（发言权被收回、请求被取消……）**并且**命中当前运行读过的频道或请求，才取消在途的模型调用；连续被取消 2 次后改为合并（防饥饿）。
- `gen`（代数）让过期的运行**什么都写不进世界**；`sleep(秒数)` 的闹钟用游戏时钟（暂停时冻结）；失败只影响这个 agent（指数退避重试 2 次后放弃）；停止是同步、幂等的。

### Worker：一次激活

<img src="docs/images/arch-worker.zh.svg" alt="Worker 的循环：打开对话、思考、记账并检查 gen、行动、整理对话、合并运行中到达的信封，直到 sleep；右侧是持久对话、压缩阈值和 Brain 告诉模型的内容" width="100%">

- **持久对话**：每个 agent 一条只追加的对话（`system` 与工具 schema 创建后逐字节不变），所以供应商的前缀缓存能命中；暂停 → 继续沿用同一条对话。
- 一轮的工具在**没有 `await`** 的一段里执行，不可能被取消在半路；assistant 消息和全部工具结果一起追加。
- **三种状态**：💭 思考（LLM 调用在途）· ⚡ 行动（执行工具）· 💤 休眠。
- **按需压缩**：用量达到模型窗口的 60% 提醒 agent 压缩，90% 仍未压缩就裁剪最早的完整轮；没有别的限制。

### 时间线：一条消息怎样唤醒所有人

<img src="docs/images/arch-timeline.zh.svg" alt="三次提交的时间线：休眠的 agent 被唤醒，正在思考的 agent 在下一轮边界合并，出局的玩家不被广播唤醒" width="100%">

每条消息都唤醒（发出者除外）；正在思考的 agent 不被打断，新消息在它下一轮边界并入；出局的玩家不被广播唤醒。

玩家的 Brain 是每个座位一个的 `BotBrain`（v0.14）：编排器（Composer）把这个 bot 的四层记忆按固定顺序挂进系统提示词并控制预算，
轮到发言、投票的那一刻再把相关的一两条打法提到眼前；输出闸门只会把不合格的发言退回，让 bot 自己重写，从不改写。
初始化与复盘是独立的学习循环（`app/learning/`），不是对局里的 agent。说明见 [docs/bots.md](docs/bots.md)
和 [架构](docs/architecture.md) 的“Bot = Brain + 记忆”一节。

引擎本身不理解“狼人”“警长”“第 2 夜”等游戏概念（`tests/v12/test_neutrality.py` 会扫描）。
剧本给出规则和手册，**主持人 Agent** 用工具推进流程；玩家用 `speak` / `respond` / `use_ability` /
`challenge_moderator` 行动。思维链和工具调用只写进明文 trace 日志，前端不展示。逐层的说明见
[docs/architecture.md](docs/architecture.md)（English: [architecture.en.md](docs/architecture.en.md)），
实现契约见 [docs/v0.12-contracts.md](docs/v0.12-contracts.md)。图由 `tools/make_diagrams.py` 生成（SVG，中英文各一份）。

## 快速开始

### 环境要求

- Python 3.12
- Node.js 20（仅前端测试需要）
- 一个 Provider API Key（OpenAI 兼容、OpenAI Responses 或 Anthropic）

### 本机运行

```bash
git clone <repository-url> Arena-Agents
cd Arena-Agents

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt

uvicorn app.main:app --host 127.0.0.1 --port 8000
```

打开 <http://127.0.0.1:8000>。

首次启动会在**程序所在文件夹**（含 `app/` 和 `config.yml` 的那个，与你从哪里启动无关）下创建数据目录
`data/`；Provider、绑定、bots、对局、日志都在里面，不需要选择任何文件夹。Provider 配置在界面中完成，本地使用
不需要 `.env`。第一次启动时，仓库 `bots/` 里的 12 个默认 bot（Alice…Leo）会被复制进去；它们要先**初始化**才能开局
（见下文“配置模型”的第 7 步）。

> **⚠ 数据在程序目录下**：删除或重装程序目录、重新 `git clone`、执行 `git clean -xdf` 都会带走你的对局。
> 请定期在 **⚙ 设置 → 导出存档** 备份（见下文“数据与存档”）。

### 演示模式（无需模型 / API Key）

```bash
ARENA_DEMO=1 uvicorn app.main:app --host 127.0.0.1 --port 8000
```

演示模式用脚本化机器人扮演主持人和 12 名玩家，走真实的引擎、频道、发言权、请求和界面，
但没有任何网络请求和费用；数据放在 `.demo-data/demo/`（不会混进你真实的历史对局）。
演示里 12 个 bot 一开始就是已初始化（✔，用固定回答，不调用模型），可以直接开局；初始化和复盘也由演示机器人完成。
演示里同样可以接管一个座位、使用输入框，并重放已经打完的对局。

### 隔离的开发实例与真实模型冒烟

```bash
# 与你的真实数据完全隔离的实例（数据在 .demo-data/，已被 git 忽略）
python tools/dev_server.py --demo --port 8123
python tools/dev_server.py --copy-providers-from "<程序目录>/data" --port 8124   # 复制 Provider、密钥与绑定，会调用真实模型并产生费用

# 带硬性调用上限的真实模型冒烟（会产生费用）：临时数据目录里先让 bot 初始化，再开局，结束后打印工具使用、被引擎退回的发言
# （TOO_LONG / FORMAT）、缓存命中率和发言权时间线。--init fixed（默认）用固定的初始化、不调模型；--init real 让 bot 真的初始化
python tools/real_smoke.py --from "<程序目录>/data" --scenario scenarios/minimal_test.md --players 4 --max-calls 60
python tools/real_smoke.py --from "<程序目录>/data" --init real --players 4 --max-calls 120

# 给默认 bot 库跑一次真实初始化（发版前做一次；只有加了 --write-library 才会写回 bots/）
python tools/init_default_bots.py --from "<程序目录>/data" --dry-run
python tools/init_default_bots.py --check
```

两个脚本都只**读**你的数据目录（把 Provider 和 Key 复制进一个私有的临时目录里干活），都有硬预算（`--max-calls`），
任何测试和自动流程都不会运行它们。用法、选项、花费的量级和怎么审结果见 [docs/real-model-runs.md](docs/real-model-runs.md)。

### Docker Compose

```bash
cp .env.example .env
# 建议设置 ARENA_API_TOKEN，保护配置写接口
python -c "import base64,secrets; print(base64.urlsafe_b64encode(secrets.token_bytes(32)).decode())" \
  > /secure/arena-master-key

export ARENA_MASTER_KEY_HOST_FILE=/secure/arena-master-key
docker compose up -d --build
```

容器以非 root 用户运行，默认只把 `127.0.0.1:${PORT:-8000}` 映射到宿主机；运行数据位于容器里的
`/app/data`（命名卷 `arena-appdata`，v0.12.1 的 `/data` 卷不会被复用也不会被删除）。API Key 的主密钥通过
Docker Secret 或独立密钥文件提供，缺失时应用拒绝保存 Key，不会回退到明文。从 v0.12.1 升级见
[docs/storage.md](docs/storage.md#upgrading-from-v0121)。

## 配置模型

1. 打开 **Provider → 新增 Provider**。
2. 选择协议：OpenAI Chat Completions / OpenAI Responses / Anthropic Messages。
3. 填写名称、Base URL、API Key。
4. 选择是否自动拼接 API 路径：
   - **开启**：Base URL 视为根地址，最终使用 `/v1/chat/completions`、`/v1/responses` 或
     `/v1/messages`，模型发现使用 `/v1/models`。
   - **关闭**：Base URL 就是完整消息地址，原样发送；模型发现关闭，只能手动填写模型 ID。
5. 获取模型（自动拼接开启时可用），每次选择一个模型。价格是**四个**（美元/1M tokens）：输入（未命中缓存）、
   输出、缓存读、缓存写（后两个留空 = 按输入价计）。对话框里的**价格源**（默认 LiteLLM 的价格表）可以
   自动匹配并填入这四个价格和上下文窗口，你仍可手动修改；没有匹配就不填，不会猜。
6. 在 **模型绑定** 中创建模板 1/2/3，或逐人选择 Provider/模型/思考深度（绑定跟着 bot 走，拖动座位不会改变它）。
7. 点参与者栏的 **⚙ 全局初始化**，让 12 个 bot 各自读一遍官方契约和规则、写下自己的理解（并行，每个最多 120 秒），
   然后才能点“开始”；没准备好的 bot 会被开局检查列出来。

完整说明见 [docs/providers.md](docs/providers.md)。

## 数据与存档

所有数据在一个目录里（默认 `<程序目录>/data/`），**只有 API Key 加密**，其余都是明文，可以直接查看：

```text
data/
├─ settings.json            默认绑定（按 bot）、模板、上次对局、默认预算上限
├─ providers.json           Provider 注册表（不含 API Key）
├─ secrets.v1.enc           API Key（AES-256-GCM；Windows 的主密钥由 DPAPI 包装在 master.v1.dpapi 里）
├─ pricing.json             下载的价格表（公开数据）
├─ contract/                官方契约（contract.md + source.json）
├─ rules/<剧本 id>/         剧本（scenario.md）和学习材料（materials/，默认为空）
├─ bots/                    玩家：lineup.json（12 个座位的顺序）+ <bot id>/（bot.json、core/ 底层设定、arch/、rules/、people.md、record.json…）
├─ games/<id>/game.json     一局（存档格式 v6，仍能读 v5，明文 JSON）+ games/index.json（历史列表的缓存，可重建）
├─ logs/<id>/trace-*.jsonl  思考日志；logs/learning/ 是初始化与复盘的日志
├─ exports/  backups/  tmp/ 导出的存档、导入前的备份（保留 3 份）、上传中的文件
└─ .lock                    进程锁：同一个数据目录只有一个服务在用
```

- **没有“保存”按钮**：对局每次变化后半秒内自动保存，退出前再存一次；重启后上一局以**已暂停**恢复。
- **设置有五栏**：① 总存档 ② 底层设定 ③ 官方契约 ④ 规则 ⑤ 对局管理。① 的**导出存档**与**导入存档**对象是一个
  `.arenaagents` 文件（zip 容器，内容不加密），**包含数据目录里的全部文件**（设置、Provider、价格表、契约、规则、bots、
  对局和全部日志）；导出时会问要不要带 API Key——要的话输入两次强密码（至少 12 位、含大小写 / 数字 / 符号中的三类），Key 用
  `scrypt + AES-256-GCM` 加密，密码不会写进存档；导入时含 Key 的存档需要输入密码，也可以选择“跳过 API Key”
  只导入其余内容。整个过程有进度，完成后会告诉你保存路径（`data/exports/`），也可以下载。
- **导入会校验**格式版本、清单和每个文件的 SHA-256、路径与大小，之后整体替换当前数据：替换前先把旧数据备份到
  `data/backups/<时间>/`，失败自动回滚。对局运行中不能导入。校验能发现损坏，但不是签名——只导入你信任的存档。
  v0.13 的存档（格式 1）也能导入，其中的名册会自动迁移成 bot。
- **单个 bot 与单局对局**：玩家详情里可以导出 / 导入 `.arenabot`（一个 bot 的全部状态，导入时覆盖目标玩家；≤ 20 MiB，
  不含 Key、契约、剧本和对局）；设置 ⑤ 里可以导出 / 导入 `.arenagame`（一局和它的日志；id 冲突时可选覆盖或作为副本导入）。
- **从 v0.12.1 升级**：运行 `python tools/migrate_v0121_to_archive.py`（只读旧工作文件夹，必须用同一个 Windows
  用户，或提供主密钥），再在设置里导入它生成的存档（它是 v0.13 的格式，名册随后自动迁移成 bot）；首次启动发现旧数据时
  页面会提示一次（可以忽略）。
- **从 v0.13 升级是自动的**：第一次启动时，`data/roster/` 被转换成 12 个 bot（名字、头像、性格、印象、经验、战绩和模型绑定
  都带过来，不调用模型，`roster/` 原样保留）；之后先点一次「⚙ 全局初始化」。手写的、没有小标题的性格不丢字：前 300 字进「身份」，
  超出的部分依次进最多 3 个「原有性格（续）」附加分区；它的「说话方式」「分析方式」是空的，要用「✨ 用主持人模型完善」或手写补上才能开局。
- **历史对局**：**📜 历史对局**列出每一局，可以重放、继续、删除（“删除对局不会撤销 bot 通过复盘学到的东西”——记忆属于
  bot，存在 `bots/` 里，不属于某一局）。

完整说明见 [docs/storage.md](docs/storage.md)（数据目录、加密范围、Docker、升级）、
[docs/archive.md](docs/archive.md)（存档格式、校验、密码、转换脚本）和 [docs/bots.md](docs/bots.md)（bot 的文件与记忆）。

## 界面操作

- **参与者栏**：每名玩家（bot）一张卡片——像素头像 + 名字 + 初始化状态（✔ 已初始化 / ⚠ 需重新初始化 / ✖ 失败 / ⏳ 初始化中 / ○ 未初始化）
  + 一个身份标签（开局后才有），头像角上是状态（💭 思考 / ⚡ 行动 / 💤 休眠，休眠到点醒来的悬停提示会写剩余秒数），左上角的半透明
  气泡是座位号。**对局未开始时可以拖动卡片调整座位**（触屏长按后拖动，键盘 Alt+←/→）；bot 的记忆和模型不受影响。点击卡片打开
  **bot 面板**：思考记录入口、LLM 调用、四类 token、缓存命中率和费用，以及它的底层设定、记忆、待确认的提案、初始化与复盘、
  `.arenabot` 导出 / 导入；工具调用只在调用日志的错误详情里保留必要信息。出局者置灰。参与者栏头部有「⚙ 全局初始化」、
  「名册 ▾」（本局是否加载记忆、清除全部学到的记忆、重新生成全部头像）和「复盘全部」。
- **信息流**：只显示发言、公告和**请求卡片**（投票、选择、问答；带进度和结果），整条渲染；没有思维链、
  工具调用和流式输出。
- **状态标签与视角标签**（顶栏第二行最前面）：状态标签显示未初始化 / 初始化中 / 对局前 / 对局中 / 已暂停（附原因）/ 已结束 / 复盘中；
  视角标签显示“全局视角”“Alice 视角”或“Alice 视角（接管）”，点击打开菜单：全局视角、以 X 的视角观看（只显示该玩家有权看到的频道与
  消息）、接管 X（未开始 / 已暂停时可用，有确认窗口）、退出接管。接管期间标签带 🎮 并锁定为你扮演的座位（退出同样有确认窗口，
  只在不运行时可用）。接管只在前端锁定视角：服务端仍向浏览器推送完整的观战数据（已知限制，见方案）。
- **输入框与技能**：信息流底部是当前频道的输入框；投票等请求卡片先点选答案，再点「提交」，提交前可改选，不会在倒计时结束时自动提交；「结束发言」「技能」按钮见上文。
- **频道栏**：显示每个频道的发言权状态（🎤 轮流发言 / 📋 队列 / 💬 自由讨论 / ❄ 已冻结 / 👁 只听 /
  🔇 禁言中）；“质询工单”单独成组；私聊按对方的名字显示；接管时轮到你的频道会有“待你操作”标记。
- **预算**：顶栏 token / 费用统计旁的上限按钮，按局设置 token 和 / 或美元上限，可选“达到上限后强制停止”。
- **对局控制**：开始（先过**开局检查**：12 个 bot 的底层设定完整且都是 ✔、契约和剧本可用、模型绑定齐全，否则按玩家列出问题）/ 暂停 /
  继续；对局结束后仍可点击“继续”恢复（主持人会收到通知）；终局时弹窗询问是否让 bot **复盘**（也可以之后补做）。
- **⚙ 设置 / 📜 历史对局**：设置的五栏（总存档、底层设定、官方契约、规则、对局管理）；重放、继续、删除历史对局
  （重放时有播放条：⏮ ▶/⏸、倍速、进度条、跳过空闲）。
- **自适应布局**：宽屏、窄屏、平板和手机竖屏（迷你卡片 + 底部标签栏）按平台与宽度自动切换。看板可整体折叠，
  分隔条可拖动，双击恢复默认；布局保存在浏览器 `localStorage`。

每个控件的详细行为见 [docs/ui-guide.md](docs/ui-guide.md)。

## 环境变量

| 变量 | 默认值 | 用途 |
|---|---|---|
| `ARENA_DATA_DIR` | `<程序目录>/data`（演示模式：`<程序目录>/.demo-data/demo`） | 数据目录（测试、开发实例、自己的数据盘） |
| `ARENA_MASTER_KEY_FILE` / `ARENA_MASTER_KEY` | 未设置（Windows 用 DPAPI） | Linux/Docker 加密 API Key 的 32 字节主密钥 |
| `ARENA_MAX_ARCHIVE_BYTES` | `2147483648` | 上传的 `.arenaagents` / `.arenagame` 大小上限（2 GiB；`.arenabot` 固定 ≤ 20 MiB） |
| `ARENA_API_TOKEN` | 未设置 | `/api/*` 访问令牌；SSE 也支持 `?token=` |
| `ARENA_ALLOWED_ORIGINS` | 未设置 | 额外允许的跨源来源 |
| `ARENA_ALLOWED_BASE_HOSTS` | 未设置 | Provider 主机白名单（可选） |
| `ARENA_ALLOW_PRIVATE_PROVIDERS` | `false` | 允许本机/内网 Provider（如 Ollama） |
| `ARENA_BIND` | `127.0.0.1` | Docker 宿主机绑定地址 |
| `ARENA_DEMO` | 未设置 | 设为 1 启用演示模式（脚本化机器人，不调用模型） |

v0.13 删除了 `ARENA_WORKSPACE_DIR`、`ARENA_DISABLE_WORKSPACE`、`ARENA_DISABLE_LEGACY_MIGRATION` 和
`ARENA_MAX_IMPORT_BYTES`（程序不再读取它们）。

`config.yml` 只放剧本路径、运行时参数（`runtime:`，见 [实现契约](docs/v0.12-contracts.md) §6）、知识库目录、
座位的默认名字、标签样式、提示词路径和旧版的 LLM 默认值；API Key 加密保存在 `data/secrets.v1.enc`，
不会写进 YAML 或 `.env`。

## 安全

- Provider Key 加密保存，API 永不返回；修改协议、Base URL 或拼接模式必须重新输入 Key。
- 非 GET 请求校验同源 `Origin`；无 token 时配置写接口（含 bot 编辑、初始化与复盘、接管、座位动作、存档导入导出、删除对局）仅允许回环客户端。
- Provider URL 阻止云元数据/链路本地地址；本机/内网 Provider 需要显式开启。
- 导入存档（`.arenaagents`、`.arenabot`、`.arenagame` 用同一套检查）：大小上限、路径白名单（拒绝绝对路径 / `..` / 符号链接）、
  压缩比与条目数上限、每个文件的 SHA-256、对局结构校验；总存档整体替换前先备份，失败自动回滚；运行中不允许导入。导出的 Key 用你的密码加密，
  密码不写入存档、日志或响应。
- 接管：动作者永远由服务端决定（客户端不能替别的座位操作）；视角只在前端锁定，浏览器仍能收到完整的观战数据。
- 默认监听 `127.0.0.1`；对外暴露请配置 TLS 反向代理与 `ARENA_API_TOKEN`。

## 测试

```bash
pip install -r requirements-dev.txt
python -m pytest -q tests
```

测试完全离线，不调用真实 LLM（引擎测试用脚本化的 FakeLLM / 演示机器人；`tests/bench/` 里基准的测试用假模型）。安装 Node.js 后会运行前端
测试，否则自动跳过。CI 覆盖 Ubuntu 与 Windows。`tests/test_docs.py` 检查文档：每个相对链接和图片都存在、
版本号一致、架构图与 `tools/make_diagrams.py` 生成的一致。

**测试从不碰你的真实数据**：`tests/conftest.py` 在整个测试进程里把 `ARENA_DATA_DIR` 指向一次性的临时目录（早于 `app` 的导入），
并在终端摘要里用红字警告 `data/` 在测试期间有变化（`tests/test_real_data_guard.py` 守着这一点）。自己写手工脚本时同样要先设置
`ARENA_DATA_DIR`。会调用真实模型的只有 [docs/real-model-runs.md](docs/real-model-runs.md) 里的两个脚本，而且只在你亲手运行时。

## 目录结构

```text
app/
├─ world/        物理层：提交闸门、账本、频道、发言权、请求、模板、能力、质询（同步、游戏无关）
├─ runtime/      异步运行时：Actor/Worker、Supervisor、LLM 闸门、trace 日志、事件总线、游戏时钟
├─ agents/       Brain：BotBrain + Composer + 输出闸门（v0.14 的 bot）、LegacyBrain（v0.13.1 的玩家）、ArenaBrain（主持人）、学习用的 Brain、
│                工具 schema、上下文构建、笔记与压缩、提示注入防护
├─ bots/         bot 的共用类型与常量：四层记忆、字数上限、哈希、学习端口
├─ learning/     初始化与复盘：独立的学习循环（不是对局里的 agent）、任务与进度、学习用量与日志
├─ game/         编排器、会话容器（存档 v6，仍读 v5）、bot 阵容与开局检查（bots_runtime）、初始化 / 复盘任务（learning_runtime）、预算、
│                绑定、接管（takeover_runtime）、重放投影（replay）、演示机器人
├─ api/          REST + SSE v2、Provider、模板、bots / 契约 / 规则、初始化与复盘、接管与座位动作、历史对局、存档导出 / 导入
├─ archive/      .arenaagents（格式 2，仍读 1）、.arenabot、.arenagame：格式与校验、API Key 的密码加密、导出 / 导入任务、备份与回滚
├─ engine/       LLM 客户端、表达式引擎
├─ llm/          三协议适配器与 API 端点规划
├─ providers/    Provider 注册表（Key 单独加密）、模型的四个价格、价格源
├─ avatars.py    像素头像（素材库 static/avatar/parts.json 由 tools/avatar_lab.py 生成）
└─ storage/      数据目录与进程锁、设置、bots、契约、规则、对局（GameStore）、API Key（SecretStore）、加密（roster.py 只剩 v0.13 名册的迁移读取）
scenarios/       Markdown 剧本（schema v2）
prompts/         主持人提示词、默认官方契约（contract.md）、初始化 / 复盘提示词（learning/）、LegacyBrain 用的玩家提示词
knowledge/       主持人指南与策略资料（只给主持人；玩家的学习材料在数据目录的 rules/ 下，默认为空）
bots/            默认 bot 库：12 个 bot（Alice…Leo），每个一个文件夹（bot.json + core/）
bench/           基准：度量、局面脚本、runner、v0.13.1 基线与验收门槛
static/          单页观战界面（static/js 前端模块、static/avatar 头像素材库）
tools/           开发工具：dev_server（隔离实例）、real_smoke（真实模型冒烟）、init_default_bots（默认 bot 库的真实初始化）、
                 mock_ui_server（模拟服务）、live_replay（事件回放校验）、avatar_lab（头像素材库）、make_diagrams（架构图）、
                 migrate_v0121_to_archive（v0.12.1 → .arenaagents 转换脚本）
tests/           离线回归、API、存储、存档、bots、学习、基准、接管、重放、文档与 UI 测试
docs/            架构、契约、Provider、存储、存档与 UI 文档，docs/images 是截图和架构图
```

## 版本说明

当前版本为 **0.14.0**：玩家从“座位上的名册”变成 **bot**——名字、头像和四层记忆（底层设定 / 架构 / 规则 / 对局），由编排器按层
挂进提示词；bot 在对局之外**初始化**（读契约和规则，写下自己的理解和打法），终局后**复盘**；超长发言以 `TOO_LONG` 退回而不是截断，
发言只来自 bot 自己；身份开局才发牌；设置分五栏，新增 `.arenabot`、`.arenagame`，总存档升到格式 2；仓库带 `bench/` 基准和
12 个默认 bot。决策与测试方案见 [docs/v0.14-plan.md](docs/v0.14-plan.md)（H1–H59），用法见 [docs/bots.md](docs/bots.md)。
**升级要知道的三件事**：
① **不能直接打开的**：v0.12.1 及更早的数据（用 `tools/migrate_v0121_to_archive.py` 转换后在设置里导入，细节见
[docs/storage.md](docs/storage.md#upgrading-from-v0121)）；v0.14 删除了 `/api/roster/**`、「重新发牌」和玩家面板里的性格 / 记忆编辑器
（由 bot 面板取代）。
② **自动迁移**：第一次启动时 `data/roster/` 被转换成 12 个 bot（导入 v0.13 的总存档同样）；迁移不调用模型，所有 bot 都是
“未初始化”，先点一次「⚙ 全局初始化」才能开局。手写的无标题性格一个字都不丢（前 300 字进身份，其余进「原有性格（续）」附加分区），
但说话方式和分析方式要自己补（「✨ 用主持人模型完善」或手写）。
③ **v0.13 的对局**（存档格式 v5）照常能载入、重放、继续——继续时用 v0.13.1 的旧 bot（`LegacyBrain`），不做开局检查，也不能复盘；
新对局的存档是 v6。

上一个版本 0.13.1：接管模式新增 **agent 软暂停**、公共频道不限时、8 色私人标记、思考记录与错误日志；投票等选择请求改为
**先选后提交**。头像编号可以精确重建同款头像。决策与测试方案见 [docs/v0.13.1-plan.md](docs/v0.13.1-plan.md)（G1–G45）。
同一 0.13 系列的 0.13.0 变更引入了座位接管、每频道输入框、数据目录、单个 `.arenaagents` 存档和历史重放。
更早的 [0.12.1](https://github.com/chengyuchen1037/Arena-Agents/releases/tag/v0.12.1) 去掉了引擎里所有“替用户省钱”的
限制，改为持久会话 + 缓存 + 合并 + 压缩的编排，并加入按局预算、四价计费与价格源、角色名册和自适应界面。
各版本的发布页见 [Releases](https://github.com/chengyuchen1037/Arena-Agents/releases)，高层发布说明见
[CHANGELOG.md](CHANGELOG.md)。

## 文档

- [架构（Actor + Worker；Bot = Brain + 记忆）](docs/architecture.md) · [English](docs/architecture.en.md)
- [Bot：底层设定、四层记忆、初始化与复盘](docs/bots.md) · [默认 bot 库](bots/README.md)
- [实现契约](docs/v0.12-contracts.md)（现行；v0.13 增补在 §11，v0.13.1 在 §12，v0.14 在 §13）· [v0.14 方案](docs/v0.14-plan.md)（H1–H59）· [v0.13.1 方案](docs/v0.13.1-plan.md)（G1–G45）· [验收记录](docs/v0.13.1-acceptance.md)· [v0.13 方案](docs/v0.13-plan.md)（F1–F38）· [v0.12.1 方案](docs/v0.12.1-plan.md)（E1–E26）· [v0.12 方案](docs/v0.12-async-agents-plan.md)（历史）
- [基准（bench/）](bench/README.md) · [用真实模型跑：冒烟脚本与默认 bot 库初始化](docs/real-model-runs.md)
- [Provider 与模型](docs/providers.md)
- [数据、存储与加密](docs/storage.md)
- [存档：导出、导入与转换](docs/archive.md)
- [界面操作指南](docs/ui-guide.md)
- [English README](README.en.md)
- [发布说明](CHANGELOG.md)

## 贡献

欢迎提交 Issue 和 Pull Request。提交前请：

1. 游戏规则放在 `scenarios/`，引擎保持游戏无关。
2. 行为变更附带离线测试。
3. 不要提交 `.env`、API Key、数据目录 `data/`、导出的 `.arenaagents` 存档、本地路径或运行数据。
4. 运行 `python -m pytest -q tests` 和 `node --check static/js/*.js`。
5. 改了架构或界面，就同步更新文档；架构图的源头是 `tools/make_diagrams.py`，改完运行
   `python tools/make_diagrams.py` 重新生成（不要手改 SVG）。

## 许可证

MIT，见 [LICENSE](LICENSE)。
