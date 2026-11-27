<p align="center">
  <img src="assets/zhidao.png" width="110" alt="知到自动化学习助手">
</p>

<h1 align="center">知到自动化学习助手</h1>

<p align="center">
  <b>知到（智慧树）共享课的自动化学习工具</b><br>
  扫码登录 · 视频进度 · 弹窗答题 · 作业作答 · 考试答题 · CLI + GUI 双入口
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/python-3.13%2B-3776AB?logo=python&logoColor=white">
  <img alt="License" src="https://img.shields.io/badge/license-GPL--3.0--only-blue">
  <img alt="Tests" src="https://img.shields.io/badge/tests-144%20passed-brightgreen">
  <img alt="Platform" src="https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey">
</p>

<p align="center">
  <a href="#-免责声明">⚠️ 免责声明（使用前必读）</a> ·
  <a href="#-功能特性">功能特性</a> ·
  <a href="#-快速开始">快速开始</a> ·
  <a href="#-图形界面">图形界面</a> ·
  <a href="#-命令行">命令行</a> ·
  <a href="#-配置">配置</a> ·
  <a href="#-开发">开发</a>
</p>

---

## ⚠️ 免责声明

> **本项目仅供技术研究与学习交流，请在使用前完整阅读 [DISCLAIMER.md](DISCLAIMER.md)。**

- 本项目与**智慧树（知到）官方无任何关系**，非官方产品，未获授权、未获背书。
- 使用本项目可能违反你所在院校的**学籍管理规定 / 学术诚信规范**，也可能与平台的《用户协议》冲突。
- **全部使用后果由使用者自行承担。** 作者与贡献者不承担任何责任。
- **请不要用它替代真实学习。** 自动化产生的学时与答题记录不构成知识掌握的证据。
- 本项目**不提供**课程内容、答案代写、代考服务，**不销售**学习成果。
- 仓库内**不含**任何真实账号 Cookie、API Key 或他人答题记录。
- 若你是权利方并认为本项目侵权，请开 Issue 联系处理。

**不接受上述条款者，请立即停止使用并删除本项目全部副本。**

---

## ✨ 功能特性

| 模块 | 能力 |
|------|------|
| **扫码登录** | 二维码落盘 + 终端直接渲染；Cookie 自动持久化，二次启动免扫码 |
| **视频进度** | 1.5x 默认速度（可调至 2.0），V2 心跳上报（30±5 秒），随机暂停，`WatchPoint` 轨迹复现 |
| **弹窗答题** | 到点拉题 → 模拟读题 2 秒 → 提交答案 |
| **作业作答** | `doHomework → 生成答案 → saveStudentAnswer → submit → 错题分析 → 重做循环` |
| **考试答题** | `doExam → 逐题保存 → [--submit] 提交`，含答案锁状态检查 |
| **三级答案策略** | 本地缓存命中 → LLM 生成（带排除错误项 / 历史解析 / 题库参考）→ 随机兜底 |
| **答案缓存** | SQLite 双键（`eid` + `question_id`）自动桥接，支持课程内跨 exam 复用 |
| **外部题库** | 可选接入 `tk.enncy.cn`，查询结果注入 LLM Prompt 作为参考 |
| **双入口** | Typer CLI（`zhidao`）+ Tkinter GUI（`zhidao-gui` / 单文件 exe） |
| **代理** | HTTP / HTTPS / SOCKS5 |
| **日志脱敏** | `api_key` / `token` / `CASLOGC` 自动打码；按天轮转，保留 30 天，gz 压缩 |

## 🧱 技术栈

| 类别 | 选型 |
|------|------|
| 语言 | Python 3.13+ |
| HTTP | httpx（同步） |
| 数据模型 | pydantic v2 |
| CLI | typer |
| 日志 | loguru |
| 加密 | pycryptodome（AES-128-CBC） |
| 配置 | TOML（`tomllib` + `tomli-w`） |
| LLM | openai SDK（OpenAI 兼容接口） |
| 二维码 | qrcode + Pillow |
| HTML 清洗 | beautifulsoup4 |
| GUI | tkinter（标准库） |
| 测试 | pytest（144 用例，全离线） |
| 打包 | PyInstaller（单文件 exe） |

## 📦 快速开始

### 环境要求

- Python **3.13+**
- Windows 10/11、Linux、macOS 均可（exe 打包仅 Windows）

### 安装

```bash
git clone https://github.com/<你的用户名>/zhidao-helper.git
cd zhidao-helper

# 方式一：安装为命令（推荐）
pip install -e .

# 方式二：只装依赖，用 python -m 运行
pip install -r requirements.txt
```

安装后 `zhidao` 命令可用；未安装时用 `python -m zhidao_helper`。

```bash
zhidao --help
zhidao --version
```

> Windows 双击脚本：`run.bat`（自动建 venv + 装依赖 + 启动）、`zhidao.bat`（用当前环境运行）。

### 三步上手

```bash
# 1. 初始化数据目录（~/.zhidao_helper/）
zhidao init

# 2. 扫码登录（二维码输出到 ~/.zhidao_helper/qrcode.png）
zhidao login
#    想在终端直接看二维码：
zhidao login --show-in-terminal

# 3. 拉取课程列表，记住 courseId
zhidao fetch
```

### 刷视频

```bash
zhidao play                      # 全刷所有课程
zhidao play -c 1000008156        # 指定课程
zhidao play -s 1.8 -l 30         # 1.8x 速度，最多跑 30 分钟
zhidao play --url "https://studyvideoh5.zhihuishu.com/stuStudy?recruitAndCourseId=xxxx"
```

### 做作业

```bash
zhidao homework                  # 全刷
zhidao homework -c 1000008156    # 指定课程
zhidao homework --url "https://onlineexamh5new.zhihuishu.com/stuExamWeb.html#/webExamList/dohomework/..."
```

> 作业/考试答案依赖 LLM，**必须先在配置里填 `api_key`**，否则降级为「缓存命中 → 随机」，正确率很低。只刷视频不需要 Key。

### 做考试

```bash
zhidao exam -c 1000008156            # 只保存答案，不提交
zhidao exam -c 1000008156 --submit   # 答题后自动提交
zhidao exam                          # 全刷
```

### 题库缓存

```bash
zhidao cache export -c 1000008156
zhidao cache import ~/.zhidao_helper/cache/zhidao_1000008156.json
```

## 🖥️ 图形界面

不想敲命令就用 GUI：

```bash
python -m zhidao_helper.gui     # 或安装后：zhidao-gui
```

四个标签页：

| 页面 | 用途 |
|------|------|
| ① 登录 | 扫码登录，二维码直接渲染在窗口里；Cookie 自动保存 |
| ② 课程与任务 | 刷新课程列表、刷视频、做作业、做考试、一键全刷、停止 |
| ③ 设置 | API Key / base_url / model、播放速度、完成阈值、时间上限、作业达标分、代理 |
| ④ 运行日志 | 实时输出，出问题先看这里 |

### 打包单文件 exe（Windows）

```bash
python build_exe.py
# 产物：dist/知到自动化学习助手.exe
```

打包后的数据目录是 **exe 同目录\zhidao_data\**（源码运行时是 `~/.zhidao_helper/`）。exe 带参数运行时自动走 CLI 模式：

```bash
.\dist\知到自动化学习助手.exe --help
.\dist\知到自动化学习助手.exe play -c 1000008156 -s 1.8
```

## ⌨️ 命令行

| 命令 | 说明 |
|------|------|
| `zhidao init` | 初始化数据目录与默认配置 |
| `zhidao login` | 扫码登录并保存 Cookie |
| `zhidao fetch` | 获取课程列表（输出 `courseId`） |
| `zhidao play` | 刷视频（`-c` / `--url` / 全刷） |
| `zhidao homework` | 做作业（`-c` / `--url` / 全刷） |
| `zhidao exam` | 做考试（`-c` / 全刷，`--submit` 自动提交） |
| `zhidao cache export` | 导出课程题库缓存 JSON |
| `zhidao cache import` | 导入题库缓存 JSON |

全局参数：`--proxy`、`-d/--debug`、`--console-log`。`play` / `homework` 的 `--url` 与 `-c` 互斥。

## ⚙️ 配置

配置文件：`~/.zhidao_helper/config.toml`（exe 模式：`zhidao_data\config.toml`）。完整示例见 [`config.toml.example`](config.toml.example)。

```toml
save_cookies = true
limit = 0                # 刷课时间限制（分钟，0 = 不限制）
threshold = 0.91         # 视频结束阈值（0.0-1.0）

[video]
zhidao_speed = 1.5       # 播放速度（最高 2.0）

[homework]
threshold = 100          # 作业达标阈值（0-100）
max_submit = 0           # 最大重做次数（0 = 无限）
delay_min = 1.0
delay_max = 2.0
page_size = 100

[exam]
delay_min = 3.0
delay_max = 5.0

[display]
log_level = "INFO"

[proxies]
http = ""
https = ""

[ai]
enabled = true
api_key = ""             # 必填：知到作业/考试没有内置 AI
base_url = "https://api.deepseek.com/v1"
model = "deepseek-chat"
max_token = 27900
timeout = 120.0
max_retries = 3
retry_delay = 1.0

[question_bank]
enabled = false
token = ""
query_url = "https://tk.enncy.cn/query"
info_url = "https://tk.enncy.cn/info"
scopes = ["zhidao_exam", "zhidao_homework"]
```

### 支持的 LLM 服务商（任意 OpenAI 兼容接口）

| 服务商 | `base_url` | `model` |
|--------|-----------|---------|
| DeepSeek | `https://api.deepseek.com/v1` | `deepseek-chat` |
| OpenAI | `https://api.openai.com/v1` | `gpt-4o-mini` |
| 阿里通义（兼容模式） | `https://dashscope.aliyuncs.com/compatible-mode/v1` | `qwen-plus` |
| 月之暗面 Kimi | `https://api.moonshot.cn/v1` | `moonshot-v1-8k` |
| 智谱 GLM | `https://open.bigmodel.cn/api/paas/v4` | `glm-4-flash` |
| 硅基流动 | `https://api.siliconflow.cn/v1` | `deepseek-ai/DeepSeek-V3` |

### 数据目录

| 路径 | 说明 |
|------|------|
| `config.toml` | 配置文件（含 API Key，**已被 .gitignore 排除**） |
| `cookies.json` | 登录 Cookie（**已被 .gitignore 排除**） |
| `execution.json` | `zhidao fetch` 生成的课程列表 |
| `qrcode.png` | 登录二维码 |
| `logs/` | 日志（按天轮转，保留 30 天，gz 压缩） |
| `cache/questions_bank.db` | 答案缓存（SQLite） |

> 换目录（多账号隔离）：设置环境变量 `ZHIDAO_HOME`，例如 `$env:ZHIDAO_HOME="D:\zhidao_account2"`。

## 🔬 实现要点

### 加密策略表

| 策略 | 密钥字段 | `dateFormate` | 校验字段 | 期望值 |
|------|---------|---------------|----------|--------|
| `zhidao` | `video_key` | 是 | `code` | `0` |
| `homework` | `exam_key` | 否 | `status` | `"200"` |
| `zhidao_exam` | `exam_key` | 否 | `status` | `"200"` |

课程列表用 `zhidao` 策略 + `home_key`，期望 `code=200`。

### 视频进度上报（V2）

- `courseId` 必须取 `courseInfo.courseId`（`queryCourse` 返回），取 `videoList` 里的会导致 `code=-1`
- `sdsew` = `encode_ev([recruitId, lessonId, v.id, v.id, chapterId, "0", delta, played, timedelta, uuid+"zhs"])`
- `zwsds` = base64(`studiedLessonDto.id`)
- `ewssw` = `WatchPoint` 轨迹（`time // 5 + 2`，2 秒一个点）
- 同一份 `sdsew` 先发 `saveCacheIntervalTimeV2`（无 `courseId`，失败即本次运行停用），再发 `saveDatabaseIntervalTimeV2`
- `-12` 验证码 → 抛 `CaptchaRequired` 停课；`-9` 时长封顶 → 抛 `TimeLimitExceeded` 停课
- `-8` 时长回退 → 用服务器时间重建 `ev` 重报；`-10` 多窗口 → 刷新 token 重报一次

### 作业流程

1. `state=4` 先 `saveCourseTran` 重置
2. `doHomework` 拿含 `eid` 的题目
3. 逐题生成答案 → `saveStudentAnswer`（`examType=""`，无 `source` 字段）→ 每题 1~2 秒随机延迟
4. `submit` 拿 `score` 算得分率
5. `lookHomework` + `getStuAnswerInfo` 拿每题对错 → 写缓存（正确 / 错误组合）
6. 未达标且还有重做次数 → 回到第 2 步

### 考试流程

1. `getSaveAnswerLockResult` 查锁（`state=1` 跳过）
2. `doExam` 拿题
3. 逐题 `saveStudentAnswer`（`examType=1`，额外明文字段 `source=1`）
4. `--submit` 时调 `submit`（`rt.statu == "1"` 为成功）
5. 无心跳、无对错检查

## 🛠️ 开发

```bash
# 运行测试（144 个用例，全部离线）
python -m pytest tests -q

# 代码检查（需 ruff）
pip install ruff
ruff check zhidao_helper tests
ruff format --check zhidao_helper tests

# 打包 wheel / sdist 到 dist/
python build.py

# 打包单文件 exe
python build_exe.py
```

测试覆盖：AES 加解密、`ev` 编码、配置读写、URL 解析、加密策略表（`MockTransport` 真实解密校验）、缓存双键桥接与跨 exam 检索、作业答案策略与降级、扫描器筛选、视频播放端到端（Mock Session）。

### 目录结构

```
zhidao_helper/
├── __main__.py            CLI 入口（typer）
├── config.py              pydantic 配置 + TOML 读写
├── crypto.py              AES-128-CBC / WatchPoint / encode_ev
├── session.py             HTTP 会话门面
├── login.py               扫码登录
├── logger.py              日志（脱敏 + 轮转）
├── reporter.py            进度报告器
├── question_bank.py       题库客户端
├── gui.py                 Tkinter 图形界面
├── api/
│   ├── http_client.py         httpx 封装、Cookie / UUID
│   ├── encrypted_query.py     加密策略表
│   ├── sso.py                 CAS SSO
│   ├── zhidao_homework_api.py 作业接口
│   ├── zhidao_exam_api.py     考试接口
│   └── ai_analysis_api.py     错题解析（SSE）
├── cache/
│   └── zhidao_cache.py    SQLite 双键缓存
├── llm/
│   ├── base.py            LLM 抽象
│   ├── openai.py          OpenAI 兼容（流式 + 提前终止）
│   └── prompts.py         Prompt 模板与答案解析
├── zhidao/
│   ├── models.py          课程 / 章节 / 弹题模型
│   ├── course.py          课程列表 + 上下文
│   ├── video.py           视频播放器（V2 上报）
│   ├── quiz.py            弹窗答题器
│   ├── homework/          作业扫描 / 分析 / 做题
│   └── exam/              考试扫描 / 做题
├── cli/
│   ├── bootstrap.py       日志 / 代理 / 配置 / 登录 / LLM
│   ├── course_resolver.py courseId -> racId
│   ├── url_parser.py      URL 解析
│   └── services/          play / homework / exam / fetch / cache
└── utils/
    ├── path.py            数据目录
    ├── cookie.py          Cookie 序列化
    ├── html.py            HTML 转文本
    └── display.py         ANSI 颜色 / 进度条 / 二维码
```

## 🔐 安全说明

- 仓库**不含**任何真实凭据；`.gitignore` 已排除 `cookies.json`、`config.toml`、`qrcode.png`、`questions_bank.db`、`logs/`、`zhidao_data/`。
- 提交 PR 前请自查：`git diff --cached | Select-String 'sk-|gho_|CASLOGC'`。
- 日志写入前会脱敏 `api_key` / `token` / `CASLOGC`。
- 发现安全问题请走 [SECURITY.md](SECURITY.md) 的私下渠道，不要开公开 Issue。

## 🤝 贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md)。欢迎 Issue 与 PR，但请勿提交任何真实账号数据、真实答题记录或规避检测的新增逻辑。

## 📄 许可证

[GPL-3.0-only](LICENSE)

本项目参考并受启发于 [pjm314159/zhs](https://github.com/pjm314159/zhs)（GPL-3.0）。按 GPL-3.0 要求，本项目同样以 GPL-3.0-only 发布。

## ⭐ 致谢

- [pjm314159/zhs](https://github.com/pjm314159/zhs) —— 协议链路参考实现
- 所有提交 Issue / PR 的贡献者

---

<p align="center"><sub>如果你觉得这个项目有帮助，欢迎点个 Star ⭐</sub></p>
