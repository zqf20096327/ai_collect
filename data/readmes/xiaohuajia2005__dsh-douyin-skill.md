# DSH 抖音助手

**带证据约束的拟人化抖音社交代理。**

它在本机 Microsoft Edge 里真实操作抖音网页版，把「看视频」和「回私信」拆成两条互不阻塞的常驻服务，中间用**人格卡 + 长期记忆 + 梗库 + 平台证据**四层约束模型输出。设计目标不是「回得快」，而是**回得像这个人，并且不会编造自己没做过的事**。

> v1.4.13 ｜ 383 项单元测试 ｜ MIT ｜ 第三方适配，非 DeepSeek 官方发行版

---

## 特性

| 能力 | 说明 |
| --- | --- |
| **自主观看** | 在允许时段与每日额度内挑片、停留、换片或停止；采样真实画面交给模型决策，同时保留手动启动／暂停 |
| **私信回复** | 仅回复本人勾选的许可会话；按正文、附件、引用分别处理，图文混合不漏附件 |
| **补答** | 已读但一直没回的尾消息，在时间窗内补一次（默认 12 小时、最多 2 次）；本人正在输入时自动让路 |
| **评论防重** | 公开评论独立开关，默认关闭；同作品不重复评论，靠**发送收据**而非内存标记判断 |
| **人格与记忆** | 人格卡手写区由人维护、生成区按月更新；长期记忆只在允许范围内共享，看到主题不等于喜欢 |
| **好友互动与分享** | 一个总开关管理许可会话的回复与自主分享；按平台稳定身份绑定收件人，同作品同会话去重 |
| **群聊回复** | 仅回复已许可群聊中被 @ 或叫到设定昵称的消息 |
| **静默观看** | 持续静音，核实窗口归属后尝试最小化；仍是**有窗口** Edge，不保证最小化后持续播放 |
| **自检与用量** | 一键诊断 + 限定修复建议；含「评论控件可识别性」，抖音改版当天就能看出来 |
| **观看日报** | 从本机观看记录生成 Markdown，不额外调用模型 |
| **可选音频** | 本地 Whisper 转写对白，视频音频可选 MiMo / MiniMax 云端后端（自带 Key） |

**明确不做**：不读文件正文、网页正文、直播音轨；不代付款、转账、赴约；**发送结果不明时不自动重发**。

---

## 架构

```
┌ 宿主接入层 ───────────────────────────────────────────────┐
│ dsh-plugin（注册/生命周期）  tool-definitions（工具 schema） │
│ native-settings*（设置页与 IPC）  settings-sections         │
├ 执行层（浏览器）───────────────────────────────────────────┤
│ browser-launcher / host / pages / pause  playwright-runtime│
│ chat-browser（私信 DOM）  comment-browser（评论区）          │
│ video-storyboard（分镜拼图）  video-forward（视频转发）      │
├ 编排层（业务状态机）───────────────────────────────────────┤
│ core（观看主循环）  chat-service（私信编排）                 │
│ autonomous-watch / comments / share  scheduled-watch       │
│ friend-interactions(+guard)  receipt-baseline  task-limits │
├ 模型交互层 ───────────────────────────────────────────────┤
│ api-agent（请求/用量/脱敏）  chat-agent（提示词组装）         │
│ chat-output（表情与指令协议）  persona-memory  memory        │
│ meme-wiki（梗库，只读外部词库）  native-watch-decision       │
└ 数据层（仓库外）───────────────────────────────────────────┘
  ~/.dsh/douyin-browser/
    control/   页面与文件锁
    memory/    人格卡、shared.sqlite、日报
    state/     策略、已读水位、收据、风格样本等 JSON
```

观看是长事务、聊天是低延迟事务。两者共用一套人格与许可名单，但运行时互不阻塞——这是整个架构最关键的一次拆分。

### 关键模块

| 文件 | 行数 | 职责 |
| --- | --- | --- |
| `chat-browser.mjs` | 1971 | 私信页全部 DOM 操作：会话列表、发送、未读、正在输入 |
| `chat-service.mjs` | 1523 | 私信编排：许可、水位、补答、记忆注入、发送回读 |
| `core.mjs` | 1207 | 观看主循环：挑片、播放、采样、决策、额度 |
| `comment-browser.mjs` | 578 | 评论区：定位输入框、发布、命中核对 |
| `diagnostics.mjs` | 216 | 一键自检与报告映射（纯映射函数可单测） |
| `chat-agent.mjs` | 326 | 提示词组装：人格／记忆／风格／热梗／梗库／证据边界 |

---

## 工程亮点

### 383 项单元测试护栏

`node --test` 起跑，零第三方断言库，38 个测试文件覆盖浏览器层以上的全部纯逻辑：状态锁自愈、收据裁剪、可见性判定、梗库边界、补答让路规则、诊断映射、打包白名单、隐私红线。

```powershell
npm test
# # tests 383
# # pass 383
# # fail 0
```

### 评论链路已完成解耦重构

重构前的 `comment-browser.mjs` 是「治理孤岛」——零测试引用、4 份重复的可见性实现、400+ 字符的单行守卫链。现在：

- **单一定义**：`visible` / `privateArea` / 身份判定收敛到 `comment/scope.mjs`；页内函数用 `new Function` + 源码注入组合，不再复制粘贴，并且能被 oracle 测试逐项比对。
- **锁按证据决定能否接管**：控制锁（短临界区）pid 死亡即接管；收据锁（可能已点过）**绝不自动接管**。规则抽成纯函数 `commentPostLockDecision`。
- **收据有界**：`clicking` / `uncertain` 永不删除，已确认只留最近 200 条 + 1MB 预算——否则累积到 4MB 硬上限后，评论会**永久失败**。
- **时序常量单点**：轮询节拍与门禁窗口收进 `comment/timing.mjs`（`Object.freeze` + 测试锁定）。折算每秒 CDP 往返从约 400 降到约 102。

### 诊断自检系统

一键自检覆盖浏览器安装、Node 版本、目录读写、锁状态、模型配置、静默窗口，以及**评论控件可识别性**：`editorCount` / `submitFound` / `nativeIcon` / `enabled` 四项，全程只读（不输入、不点击、不导航）。认不得发布控件时明确提示「疑似抖音改版」；出现多个发布控件则直接 fail——那是会点错场景。

### 隐私红线有测试兜底

`tests/privacy-guard.test.mjs` 扫描源码与文档，禁止本机绝对路径与明文 Key／Token，并断言 `.gitignore` 覆盖 `state/`、`memory/`、`control/`、`*.sqlite`、`*.db` 等运行时产物。

---

## 环境依赖

| 项 | 要求 |
| --- | --- |
| 操作系统 | Windows 10 / 11（依赖本机 Edge 与窗口控制） |
| 浏览器 | Microsoft Edge（本人登录的专用 profile，**有窗口**运行） |
| Node.js | **>= 22.13**（使用 `node:sqlite`、`node --test`） |
| DSH 宿主 | 见 `package.json` 的 `engines.dsh`（已核对 0.2.0-rc.2 / 0.2.1-rc.2 两代 SDK） |
| 模型 | 插件版复用宿主已配置的、**支持图片**的模型 |
| 可选 | 本地 Whisper（Python）、ffmpeg（音频转写） |

---

## 快速开始

### 1. 安装

**插件版（推荐）**——DSH Desktop 打开「应用 → 桌面插件」，填写包名：

```
dsh-douyin-browser-local@1.4.13
```

装完**完全退出并重新打开**同一份 DSH。Web profile 也可用命令行：

```powershell
dsh plugin --profile web add dsh-douyin-browser-local@1.4.13
```

**源码版**——在仓库根目录：

```powershell
pnpm install --frozen-lockfile
$dshInstallDirectory = 'C:\Apps\DSH Desktop'   # 换成实际安装目录
.\install-native.ps1 -DshRoot $dshInstallDirectory             # 只检查，不改配置
.\install-native.ps1 -DshRoot $dshInstallDirectory -Install    # 确认无误后再装
```

安装器保留原 profile 副本，不删除登录、记忆或收据。

### 2. 首次配置

1. DSH「模型」页先配好提供商 → 本插件里选一个**支持图片**的模型（插件不重复填写主模型 Key）。
2. 打开「设置 → 刷抖音」→「打开抖音」，**由本人**在专用 Edge 里登录并完成验证码。
3. 填写人格正文（称呼、情绪、表达习惯）——它决定说话方式，不改许可与现实承诺。
4. 在「好友互动」里勾选允许回复的好友／群聊；**默认不会自行添加任何会话**。
5. 按需开启「允许自动观看」「公开评论」（后者默认关闭）。

> 详细行为约定（时段、额度、静默观看、分镜、群分享等）见 [docs/usage.md](docs/usage.md)。

### 3. 跑测试

```powershell
npm test
```

---

## 数据与隐私

- 全部运行时数据在 **`~/.dsh/douyin-browser/`**，与源码仓库完全分离，已在 `.gitignore` 中排除。
- 仓库内不含登录态、Cookie、聊天记录或数据库文件；`.env` 与 `*.local.json` 不入库。唯一例外是 `media/settings.local.json`——只有 `enabled` / `backend` 两个字段的默认值，无隐私。
- 主模型 Key 由宿主或设置页管理，不写入源码、不回显。
- 梗词库来自同级的 `dsh-memewiki` 包，路径经 `DSH_MEMEWIKI_DB` 环境变量或包解析得到，**源码中不写死任何绝对路径**；词库缺失时自动降级为「无梗库」，不影响回复。

---

## 文档

| 文档 | 内容 |
| --- | --- |
| [docs/usage.md](docs/usage.md) | 逐项行为约定（时段、额度、静默、分镜、群分享、多对象分享） |
| [docs/plugin.md](docs/plugin.md) | 插件版安装、分类设置与自动保存 |
| [docs/details.md](docs/details.md) | 详细说明与验收记录 |
| [docs/standalone-api.md](docs/standalone-api.md) | 独立软件版本机 API |
| [docs/versioning.md](docs/versioning.md) | 版本与兼容策略 |
| [CHANGELOG.md](CHANGELOG.md) | 版本变更记录 |

---

## 免责声明

本项目是**第三方 MIT 开源适配**，与抖音、字节跳动、DeepSeek 均无隶属或背书关系。

- 仅供**学习交流与技术研究**，请遵守抖音用户协议、社区规则及所在地法律法规。
- 自动化操作存在账号风险（限流、验证、封禁），请自行评估并控制频率；默认配置偏保守，不建议为「效率」调高。
- 模型输出可能出错。使用者对账号发布的一切内容负责；涉及金钱、承诺、隐私的话题请勿交由自动化处理。
- 作者不对因使用本项目造成的账号处罚、数据丢失或其它损失承担责任。

---

## 许可证

[MIT](LICENSE)。第三方组件与素材的来源及许可见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
