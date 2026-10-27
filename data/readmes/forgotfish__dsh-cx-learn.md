# dsh-cx-learn

> DeepSeek Harness (DSH) 插件：把「超星学习通看课」变成一个**可调度、可观测、可优雅停止**的后台任务。

用 CDP（Chrome DevTools Protocol）驱动一个真实的 Chromium，自动推进课程视频：
恢复播放、关掉防挂机弹窗、自然结束自动切下一节、弹题作答（AI 或人工）、跳过已完成章节。

---

## 目录

- [它做什么](#它做什么)
- [特点](#特点)
- [安装](#安装)
- [快速上手](#快速上手)
- [浏览器内核从哪来](#浏览器内核从哪来)
- [答题模型从哪来](#答题模型从哪来)
- [HTTP 接口](#http-接口)
- [配置项](#配置项)
- [环境变量](#环境变量)
- [脱离插件独立运行](#脱离插件独立运行)
- [架构](#架构)
- [免责声明](#免责声明)
- [License](#license)

---

## 它做什么

| 能力 | 说明 |
|---|---|
| P0 播放态检测 | 视频被暂停就恢复播放；关掉防挂机弹窗 |
| P1 自动切节 | 当前节自然结束后自动切到下一节 |
| P2 弹题作答 | 「AI 答题」或「人工答题」两种模式 |
| P3 跳过已完成 | 识别已看完的任务点并跳过 |
| P4 章节模式 | 单章节 / 章节连播，带最大节数上限 |
| 拟人化节奏 | 所有随机延迟集中在 `CONFIG`，可统一调节 |

另有 **扫码登录**：插件设置页直接显示二维码，用手机 App 扫一次即可，登录态长期复用。

---

## 特点

- **零 npm 依赖** —— 引擎只用 Node 内置模块，不引入 puppeteer / playwright
- **内核与插件解耦** —— 换机器只要把浏览器内核丢进共享目录，UI 上直接选
- **多用户隔离** —— 每个用户自己的配置、日志、登录态、浏览器 profile
- **模型来源通用** —— 直接读取你在 DSH 里已配置的所有模型，不是硬编码几个
- **安全停止** —— 检测到人脸识别 / 活体 / 验证码立即停止，绝不尝试绕过
- **不碰后端** —— 不篡改数据、不伪造进度上报、不调用任何进度写接口

---

## 安装

### 方式一：DSH 插件市场

在 DSH 的插件管理页搜索 `dsh-cx-learn`，安装后启用。

### 方式二：手动安装

```bash
# 克隆到 DSH 的插件目录（路径按你的部署调整）
git clone https://github.com/forgotfish/dsh-cx-learn.git

# 让 profile 认识这个 bundle
dsh plugin --profile web add dsh-cx-learn

# 本地开发时指向本地目录
dsh plugin --profile web add link:/绝对路径/dsh-cx-learn
```

安装后在 DSH 的 **设置 → 学习通看课** 里就能看到面板。

### 全局安装（多用户）

在共享插件清单 `access.yaml` 的 `base_bundles` 里加上 `dsh-cx-learn`，所有用户 profile 自动继承：

```yaml
base_bundles:
- '@deepseek-ai/dsh-base'
- '@deepseek-ai/dsh-web-app'
- dsh-cx-learn
```

---

## 快速上手

1. **准备浏览器内核**（见下一节）
2. 打开 DSH → **设置 → 学习通看课**
3. 点「开始登录」→ 等约 10 秒 → 点「刷新二维码」→ 用手机学习通 App 扫码
4. 点「读取我的课程」→ 从下拉里选一门课（会自动带上正确的 `clazzid` / `enc`）
5. 选「答题方式」：
   - **人工答题** —— 遇到弹题就停下等你处理
   - **AI 答题** —— 选一个模型自动作答
6. 点「保存配置」→「开始看课」

---

## 浏览器内核从哪来

内核**不在插件目录里**，而是在一个共享目录里，这样换机器不用改插件。

插件按这个顺序找内核目录：

1. 环境变量 `CX_BROWSER_ROOT`
2. `$DSH_HOME/cx-learn/browsers`
3. `/vol1/@apphome/dsh-shared/browsers`（fnOS / NAS 场景）
4. `/opt/dsh-shared/browsers`
5. 插件目录下的 `.browser/`

**目录结构**：每个子目录 = 一个内核，目录里放可执行文件。

```
browsers/
├── chrome-linux64/
│   └── chrome          ← 可执行文件
├── chromium/
│   └── chromium
└── chrome-headless-shell-linux64/
    └── chrome-headless-shell
```

支持的可执行文件名：`chrome`、`chromium`、`chromium-browser`、`headless_shell`、`chrome-headless-shell`。

设置页的下拉里会列出所有找到的内核（含版本号），也可以直接填自定义绝对路径。

**去哪下载内核**：
- [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/)（推荐，含完整编解码器）
- [npmmirror 镜像](https://registry.npmmirror.com/binary.html?path=chrome-for-testing/)

> 注意：部分精简版 Chromium 缺 H.264/AAC 解码，播放某些课程视频会失败。
> `chrome-headless-shell` 与完整 `chrome` 在这一点上不同。

---

## 答题模型从哪来

下拉里的模型来自**两个来源**，插件启动时自动读取：

### 1. 你在 DSH 里已配置的模型

通过 `ctx.llm.listProviders()` + `listModels()` 读出你配置过的所有服务商及其模型。
装了 `dsh-our-free-model` 之类的插件，它们的模型也会一并出现。

### 2. 插件内置模型

智谱 GLM 系列（走 OpenAI 兼容接口，需要环境变量 `ZHIPU_API_KEY`）。

### 怎么知道哪个模型能用？

设置页有两个按钮：

- **测试模型** —— 用当前选中的模型答一道题（1949 年那道），立刻知道通不通
- **批量体检** —— 依次探测一批模型，列出哪些可用、哪些报什么错

常见失败原因：

| 现象 | 原因 |
|---|---|
| `RATE_LIMIT` / 免费额度用尽 | 上游免费额度耗尽，等配额恢复 |
| `INVALID_CREDENTIAL` | 该模型的凭据没配好 |
| 模型已下线 | 上游把该模型 EOL 了 |
| `余额不足` | 服务商账号欠费 |

---

## HTTP 接口

所有接口挂在 `/api/cx-learn` 前缀下。

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/status` | 完整状态：配置、引擎、内核、模型、近期日志 |
| GET | `/config` | 读配置 |
| POST | `/config` | 写配置（部分更新） |
| GET | `/models` | 可选模型清单（含来源分类） |
| POST | `/models/health` | 批量探活 |
| POST | `/ask-test` | 用指定模型答一道题 |
| GET | `/browsers` | 可用浏览器内核清单 |
| POST | `/start` | 启动一轮任务 |
| POST | `/stop` | 停止当前任务 |
| POST | `/login` | 启动扫码登录流程 |
| GET | `/qr` | 取登录二维码（base64 data URL） |
| GET | `/courses` | 读取账号下的课程列表 |
| GET | `/log` | 最近日志 |

---

## 配置项

存在 `$DSH_HOME/cx-learn/config.json`：

| 字段 | 默认值 | 说明 |
|---|---|---|
| `courseUrl` | `''` | 课程学习页 URL |
| `mode` | `continue_chapters` | `continue_chapters` 连播 / `current_chapter` 只跑当前章 |
| `maxSections` | `5` | 单轮最多看完多少节 |
| `videoDoneAt` | `98.5%` | 判定「看完」的进度阈值 |
| `browserId` | `''` | 选中的内核 id（空 = 自动探测） |
| `chromiumPath` | `''` | 自定义内核绝对路径（非空时优先） |
| `headless` | `true` | 是否无头运行 |
| `quizMode` | `manual` | `ai` 模型代答 / `manual` 暂停等人工 |
| `quizModel` | `''` | 答题模型 id（见 `/models` 返回） |

---

## 环境变量

| 变量 | 作用 |
|---|---|
| `DSH_HOME` | DSH 数据根目录，插件的运行期数据落在 `$DSH_HOME/cx-learn/` |
| `CX_BROWSER_ROOT` | 浏览器内核共享目录 |
| `ZHIPU_API_KEY` | 内置智谱模型用的 API Key |

引擎侧还支持（独立运行时有用）：

| 变量 | 作用 |
|---|---|
| `CX_CHROMIUM` | 浏览器可执行文件路径 |
| `CX_PROFILE_DIR` | 浏览器 profile 目录（存登录态） |
| `CX_COURSE_URL` | 课程 URL |
| `CX_CDP_PORT` | CDP 端口（默认 9223） |
| `CX_LOGIN_SHOT_DIR` | 登录二维码截图目录 |
| `CX_QUIZ_MODE` | `ai` / `manual` |
| `CX_LLM_ASK_URL` | 宿主答题回调地址（插件注入） |

---

## 脱离插件独立运行

引擎是自包含的，不装插件也能跑：

```bash
# 扫码登录
node engine/chaoxing-autolearn.js --login

# 跑一轮
node engine/chaoxing-autolearn.js \
  --mode=continue_chapters \
  --max-sections=5 \
  --course-url='https://mooc1.chaoxing.com/...'

# 自检
node engine/chaoxing-autolearn.js --selftest
```

也可以当 MCP 工具用：

```bash
node engine/chaoxing-autolearn.js --serve-mcp
```

会暴露 `cx_learn`（推进看课）和 `cx_login`（扫码登录）两个工具。

---

## 架构

```
┌─────────────────────────────────────────────┐
│  DSH Web UI (client.js)                      │
│  设置页：课程 / 内核 / 模型 / 答题方式          │
└──────────────────┬──────────────────────────┘
                   │ /api/cx-learn/*
┌──────────────────▼──────────────────────────┐
│  host 半端 (index.js)                        │
│  · 进程生命周期 · HTTP 接口 · 配置持久化        │
│  · ask server：把引擎的答题请求转发给 ctx.llm  │
└──────────────────┬──────────────────────────┘
                   │ spawn + 环境变量
┌──────────────────▼──────────────────────────┐
│  引擎 (engine/chaoxing-autolearn.js)          │
│  零依赖 · CDP 适配层 + 业务状态机              │
│  · P0 播放态  P1 切节  P2 答题  P3 跳过  P4 模式 │
└──────────────────┬──────────────────────────┘
                   │ CDP
┌──────────────────▼──────────────────────────┐
│  真实 Chromium（共享内核目录）                 │
└─────────────────────────────────────────────┘
```

**为什么要绕一圈 host？** 引擎是子进程，拿不到 `ctx.llm`。所以 host 起一个 loopback
`ask` 端点，引擎遇到弹题就回调过来，由 host 用 DSH 的模型服务作答。
这样引擎保持零依赖，同时又能用上你在 DSH 里配好的所有模型。

---

## 免责声明

本项目用于**浏览器自动化技术研究**。

超星学习通等教育平台普遍禁止自动化脚本，使用可能导致**学习进度被退回或账号处罚**。
使用者需自行确认所在平台的服务条款与当地法规，并自行承担全部责任。

本项目**不**篡改后端数据、**不**伪造进度上报、**不**调用任何进度写接口；
所有动作均为模拟页面点击 / 播放行为；一旦检测到人脸识别、活体检测、验证码等
人工验证特征会**立即停止**，不做任何绕过。

---

## License

[MIT](LICENSE)
