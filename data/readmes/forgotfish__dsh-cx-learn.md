# dsh-cx-learn

> DeepSeek Harness (DSH) 插件：把「超星学习通看课」变成一个**可调度、可观测、可优雅停止**的后台任务。

用 CDP（Chrome DevTools Protocol）驱动一个真实的 Chromium，自动推进课程视频：
恢复播放、关掉防挂机弹窗、自然结束自动切下一节、识别题目后暂停、跳过已完成章节。题目只进入人工审阅队列，不自动回答、填空或提交。

---

## 目录

- [它做什么](#它做什么)
- [特点](#特点)
- [安装](#安装)
- [快速上手](#快速上手)
- [浏览器内核从哪来](#浏览器内核从哪来)
- [旧答题接口](#旧答题接口仅兼容诊断)
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
| P2 题目识别 | 识别视频内随堂题、章节测验或泛化题目，记录后暂停，不自动作答 |
| P3 跳过已完成 | 识别已看完的任务点并跳过 |
| P4 章节模式 | 单章节 / 章节连播，带最大节数上限 |
| 拟人化节奏 | 所有随机延迟集中在 `CONFIG`，可统一调节 |

另有 **扫码登录**：插件设置页直接显示二维码，用手机 App 扫一次即可，登录态长期复用。

---

## 特点

- **零 npm 依赖** —— 引擎只用 Node 内置模块，不引入 puppeteer / playwright
- **内核与插件解耦** —— 换机器只要把浏览器内核丢进共享目录，UI 上直接选
- **多用户隔离** —— 每个用户自己的配置、日志、登录态、浏览器 profile
- **人工审阅队列** —— 分类并展示已识别题目，支持显式投递为对话框草稿
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
5. 确认「只识别题目」模式：遇到视频内随堂题、章节测验或泛化题目时，任务会记录题目并暂停，不会自动选择、填空或提交。
6. 在设置页的「待处理题目」区域，按需逐条点击「投递草稿」；内容只写入当前对话框输入框，是否发送由你自行决定。
7. 点「保存配置」→「开始看课」

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

## 旧答题接口（仅兼容/诊断）

host 中的旧模型目录与答题回调仅为兼容旧配置保留，不属于当前看课流程。设置页不提供模型答题、模型测试或批量探活入口；插件启动时强制题目处理模式为 `skip`。正常流程只识别并记录题目，遇题后暂停，不会请求模型、选择选项、填写答案或提交。

---

## HTTP 接口

所有接口挂在 `/api/cx-learn` 前缀下。

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/health` | **轻量健康快照**（毫秒级，不调 LLM/不读日志）。监测脚本用 |
| GET | `/status` | 完整状态：配置、引擎、内核、模型、近期日志 |
| POST | `/browser/restart` | 只清本插件自己的内核进程 + 重置 `browser.json` |
| GET | `/config` | 读配置 |
| POST | `/config` | 写配置（部分更新） |
| GET | `/models` | 可选模型清单（含来源分类） |
| POST | `/models/health` | 旧兼容接口；正常看课流程不调用 |
| POST | `/ask-test` | 旧兼容接口；正常看课流程不调用 |
| GET | `/browsers` | 可用浏览器内核清单 |
| POST | `/start` | 启动一轮任务 |
| POST | `/stop` | 停止当前任务 |
| POST | `/login` | 启动扫码登录流程 |
| GET | `/qr` | 取登录二维码（base64 data URL） |
| GET | `/courses` | 读取账号下的课程列表 |
| GET | `/log` | 最近日志 |

### `GET /health`

给监测/告警用。**不调宿主 LLM、不读 `run.log`、不 spawn 内核探版本**，稳定在毫秒级，
内部异常也返回 **HTTP 200 + `ok:false`**（监测脚本只看体里的 `ok`，
这样反向代理的 502 才能和业务故障区分开）。

```json
{
  "ok": true,
  "at": "2026-10-30T00:53:57.766Z",
  "engine":   { "ready": true, "path": ".../engine/chaoxing-autolearn.js" },
  "chromium": { "path": ".../chrome-linux64/chrome", "ready": true,
                "version": "Chrome/158.0.8122.0" },
  "browser":  { "alive": false, "port": 34471, "heartbeatAt": null,
                "ageMs": null, "restarts": 0, "lastErrorKind": "",
                "executablePath": "...", "browserVersion": "..." },
  "task":     { "running": false, "pid": null, "startedAt": 1793270064901 },
  "home": ".../cx-learn"
}
```

`browser` 为 `null` 表示浏览器层还没写过中间状态（内核从未启动）。
`alive=false` 且 `heartbeatAt=null` 表示「启动过但心跳未就绪」或「已关闭」——
UI 会显示「—」，不会误报就绪。

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
| `quizMode` | `skip` | 只识别题目并暂停；正常启动入口强制使用 `skip` |
| `quizModel` | `''` | 旧答题接口的兼容字段，正常看课流程不会调用 |

---

## 环境变量

| 变量 | 作用 |
|---|---|
| `DSH_HOME` | DSH 数据根目录，插件的运行期数据落在 `$DSH_HOME/cx-learn/` |
| `CX_BROWSER_ROOT` | 浏览器内核共享目录 |
| `ZHIPU_API_KEY` | 旧兼容答题接口的配置项；正常看课流程不使用 |

引擎侧还支持（独立运行时有用）：

| 变量 | 作用 |
|---|---|
| `CX_CHROMIUM` | 浏览器可执行文件路径 |
| `CX_PROFILE_DIR` | 浏览器 profile 目录（存登录态） |
| `CX_COURSE_URL` | 课程 URL |
| `CX_CDP_PORT` | CDP 端口（默认 9223） |
| `CX_LOGIN_SHOT_DIR` | 登录二维码截图目录 |
| `CX_QUIZ_MODE` | 引擎内部兼容开关；插件启动时强制为 `skip` |
| `CX_LLM_ASK_URL` | 旧答题回调地址，仅兼容/诊断使用 |

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
node engine/chaoxing-autolearn.js --self-test
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
│  设置页：课程 / 内核 / 安全题目识别队列          │
└──────────────────┬──────────────────────────┘
                   │ /api/cx-learn/*
┌──────────────────▼──────────────────────────┐
│  host 半端 (index.js)                        │
│  · 进程生命周期 · HTTP 接口 · 配置持久化        │
│  · 旧 ask server 仅为兼容保留；安全主流程不调用 │
└──────────────────┬──────────────────────────┘
                   │ spawn + 环境变量
┌──────────────────▼──────────────────────────┐
│  引擎 (engine/chaoxing-autolearn.js)          │
│  零依赖 · CDP 适配层 + 业务状态机              │
│  · P0 播放态  P1 切节  P2 识题暂停  P3 跳过  P4 模式 │
└──────────────────┬──────────────────────────┘
                   │ CDP
┌──────────────────▼──────────────────────────┐
│  真实 Chromium（共享内核目录）                 │
└─────────────────────────────────────────────┘
```

**题目处理链路：** 引擎只读识别题目并写入 JSONL 事件，host 将完整事件放入待处理队列；用户显式点击后，设置页生成草稿并调用 composer 的 `setDraft`。草稿与发送严格分离，任何一步都不会选择学习通选项、填写答案或提交。

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
