<div align="center">

<img src="adm/assets/app_icon.png" width="130" alt="AI Dialog Manager">

# AI Dialog Manager

**一个窗口,管住所有 AI 编程工具的聊天记录。**

统一浏览 / 搜索 / 编辑 **9 种 AI 工具**的会话,还能把任意一段对话<br>
**「转生」**到另一种 AI 工具里继续 —— 换工具、换目录,上下文一行不丢。

[![Release](https://img.shields.io/github/v/release/haczen/ai-dialog-manage?style=flat-square&color=blue)](https://github.com/haczen/ai-dialog-manage/releases)
[![CI](https://img.shields.io/github/actions/workflow/status/haczen/ai-dialog-manage/ci.yml?style=flat-square&label=CI)](https://github.com/haczen/ai-dialog-manage/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows-blue.svg?style=flat-square)]()
[![Python](https://img.shields.io/badge/python-3.12%2B-3776ab.svg?style=flat-square)](https://www.python.org/)

**中文** | [English](docs/README.en.md) *(coming soon)*

</div>

---

## 📦 安装

**方式一:下载即用(推荐,Windows 免安装)**

到 [Releases](https://github.com/haczen/ai-dialog-manage/releases) 下载最新的
`AI-Dialog-Manager-vX.X.X.exe`,双击运行,无需 Python。

**方式二:源码运行**

```powershell
git clone https://github.com/haczen/ai-dialog-manage.git
cd ai-dialog-manage
uv sync          # 安装依赖(需要 uv,https://docs.astral.sh/uv/)
uv run adm       # 启动
```

**自行打包**

```powershell
uv run pyinstaller --noconfirm AI-Dialog-Manager.spec
# 产物在 dist\AI-Dialog-Manager.exe
```

## 🚀 快速上手教程

### 第 1 步 · 启动与扫描

双击 exe(或 `uv run adm`)。启动后自动扫描本机全部 9 种来源的会话,
按最近更新排序。状态栏显示 `129 个会话 · Claude 109 · Codex 13 · …`。

> 第一次扫描约 1 秒;之后启动有缓存,秒开。
> 只要你机器上装过对应工具、产生过对话,就会自动出现在列表里。

### 第 2 步 · 找到想看的会话

| 操作 | 方法 |
|---|---|
| 按关键词找 | 左上搜索框:标题 / 项目 / id 模糊匹配(`Ctrl+F`) |
| 只看某个工具 | 「来源」下拉:9 个来源独立筛选 |
| 只看某项目 | 「项目」下拉(自动收集全部项目) |
| 排序 | 「排序」下拉 + `↓↑` 切换方向;表头点击也可以 |
| 项目全景 | 「📁 按项目分组」切换树视图:项目节点带会话数/消息数/总大小 |
| 快捷收藏 | 点 ☆,配合「★ 收藏」只看收藏 |

### 第 3 步 · 查看对话

**双击任意会话**,右侧打开聊天视图:

- 用户 / 助手气泡,thinking 与工具调用/结果默认折叠,点开看细节
- 会话内还有一排工具:只看用户/助手、隐藏工具噪音、**会话内搜索**、
  **倒序阅读**(最新消息在前)
- 大会话自动分页,「加载更多」翻看历史
- 每条消息显示行号、时间戳、模型名

### 第 4 步 · 编辑对话

**双击任意消息**打开编辑器:

- 「文本」标签:直接改文字(工具参数以 JSON 编辑)
- 「Raw JSON」标签:直接改原始记录,高手用法
- **删除消息**:自动连带其 tool_use / tool_result 配对;
  Claude 会话还会自动修复 parentUuid 链,不会改坏
- 「+ 追加消息」:往会话末尾加一条用户消息,resume 后 CLI 立即可见
- 删除后自动跳回原位置,不用重新翻页

> 每次写入前自动备份到 `%APPDATA%\ai-dialog-manager\backups\`,
> 保留最近 8 份;CLI 在你编辑期间追加的内容会被自动保留合并。

### 第 5 步 · 一键恢复继续聊

选中会话 →「▶ 恢复会话」:自动在项目目录打开新终端,执行
`claude --resume <id>` / `codex resume <id>` / `opencode --session <id>` 等。

### 第 6 步 · 转生到另一个 AI 工具

这是本工具的特色功能。选中会话 →「⤴ 适配其它 AI」:

1. 选目标工具(Claude / Codex / OpenCode / Gemini / Qwen / Goose / Cline / Roo / JSON)
2. 选**新的工作目录**(可以和原目录完全不同,如 `E:\test` → `D:\hello`)
3. 可选新标题、是否带上工具记录/思考/子代理
4. 确认 → 新工具的会话库里出现一个**全新 id** 的会话,原会话不动

工具调用会转成可读文本,避免目标工具不认识源工具的 schema 而报错。
也支持命令行:

```powershell
uv run adm --transplant 4f2a1c --to codex --cwd D:\hello
```

### 第 7 步 · 意识上传(把会话打包带走)

选中会话 →「⤴ 意识上传」导出一个自包含文件夹,
拿到**没装 Python、没装本工具**的机器上:

```bat
install.bat "D:\新目录"        :: 同工具恢复(新 id、cwd 改写)
restore-codex.bat "D:\hello"   :: 换工具:转换 + 直接打开继续
restore-gemini.bat "D:\hello"  :: 或 Gemini / Qwen / Goose / Cline / Roo / JSON
```

### 第 8 步 · 全局搜索与批处理

- `Ctrl+Shift+F` 全局搜索:**所有来源的全文**(含工具参数和输出),
  双击结果直接跳到那条消息
- `Ctrl`/`Shift` 多选会话 →「⋯ 批处理」:批量收藏/归档/导出 Markdown/删除/上传/转生

### 快捷键速查

| 按键 | 作用 |
|---|---|
| `Ctrl+F` | 会话列表过滤框 |
| `Ctrl+Shift+F` | 全局搜索 |
| `F5` | 重新扫描 |
| `Delete` | 删除选中会话(先备份) |
| `Enter` | 打开选中会话 |
| 双击列表行 | 打开会话 |
| 双击消息 | 编辑该消息 |

## 🗂 支持的 9 个会话来源

| 来源 | 会话存储位置 | 编辑 | 一键恢复 |
|---|---|---|---|
| **Claude Code** | `~/.claude/projects/<路径>/<id>.jsonl` | ✅ | `claude --resume <id>` |
| **Codex** | `~/.codex/sessions/…/rollout-*.jsonl` + `state_5.sqlite` | ✅ | `codex resume <id>` |
| **OpenCode 2.x** | `~/.local/share/opencode/opencode.db`(sqlite) | ✅ | `opencode --session <id>` |
| **Gemini CLI** | `~/.gemini/tmp/<sha256(cwd)>/chats/session-*.json` | ✅ | `gemini --resume <id>` |
| **Qwen Code** | `~/.qwen/tmp/<sha256(cwd)>/chats/session-*.json` | ✅ | `qwen --resume <id>` |
| **Goose** | `%APPDATA%\Block\goose\data\sessions\<id>.json` | ✅ | `goose session --resume --name <id>` |
| **Cline**(VS Code) | `globalStorage/saoudrizwan.claude-dev/tasks/<id>/` | ✅ | VS Code → Cline → 历史 |
| **Roo Code**(VS Code) | `globalStorage/rooveterinaryinc.roo-cline/tasks/<id>/` | ✅ | VS Code → Roo → 历史 |
| **Kiro**(AWS AI IDE) | `%APPDATA%\Kiro\User\workspaceStorage\*` 会话 JSON(探测式) | ✅ | Kiro 内 History 继续 |

每个来源的标题、项目、消息数、大小、tokens、运行状态、归档状态统一提取;
Gemini / Qwen 的会话目录是单向哈希,扫描时用其它来源的 cwd 反查还原项目名。

## 🛡 数据安全

- **只读优先**:列表扫描不写任何原始文件
- **写前自动备份**:`%APPDATA%\ai-dialog-manager\backups\<来源>\<会话>\`,
  保留最近 8 份;OpenCode 用 sqlite backup API 保证 WAL 一致性
- **外部修改检测**:保存时校验加载快照——CLI 期间追加的内容自动保留合并,
  已被外部改动的旧内容**拒绝覆盖**并提示
- **原子写入**:临时文件 + `os.replace`,断电不留半个文件
- Codex 编辑后自动清理投影缓存,强制从 rollout 重新投影

## ⚡ 性能

| 指标 | 数值 |
|---|---|
| 首次全量扫描(311MB / 129 会话) | ~1.0s |
| 热启动扫描(缓存命中) | **0.03s** |
| 列表加载策略 | 只扫元数据,点击才解析正文(后台线程) |
| 连续点击切换会话 | 立即切换,旧加载自动作废 |

## ⌨️ 命令行

```powershell
uv run adm --selftest      # 无界面自检:全源扫描/解析/编辑回环/缓存校验
uv run adm --repair        # 修复 Claude 会话断链(parentUuid/leafUuid)
uv run adm --transplant <id|path> --to claude|codex|opencode|gemini|qwen|goose|cline|roo|json
                           [--cwd DIR] [--title T] [--out DIR] [--no-tools] [--reasoning]
```

`--transplant` 的源可以是任意已扫描来源的会话 id(前缀也可),
或 Claude/Codex 转录文件、OpenCode 导出的 JSON。

## 🏗 架构 & 二次开发

```
adm/
├── sources.py         源注册表:scan/load/编辑能力/resume 命令的单一分派点
├── models.py          SessionMeta / Message / Part + 来源徽章/颜色注册表
├── config.py          全部来源的路径常量
├── claude_store.py    Claude 扫描/解析/编辑
├── codex_store.py     Codex sqlite + rollout
├── opencode_store.py  OpenCode sqlite(读+写,seq 分配器/backup API)
├── gemini_store.py    Gemini CLI / Qwen Code(同构参数化)
├── goose_store.py     Goose
├── cline_store.py     Cline / Roo Code(同构参数化)
├── kiro_store.py      Kiro IDE(探测式解析 workspaceStorage)
├── jsonlio.py         jsonl 行级编辑器(备份+外部修改检测+原子写)
├── record_io.py       JSON 文档记录级编辑器(同保真)
├── meta_cache.py      持久化扫描缓存
├── scanner.py / searcher.py / launcher.py
├── transfer.py        意识上传:可恢复包 + 无依赖安装器
├── transplant.py      跨工具转换:中立会话 + 9 个目标写入器
├── i18n.py            中英文案
└── ui/                主题 / 表格 / 聊天视图 / 对话框 / 主窗口
```

**新增一种来源 = 写一个 store 模块 + 在 `sources.py` 注册一行**;
列表、搜索、编辑、转生、上传、统计全部自动生效。

开发自查:

```powershell
uv run adm --selftest           # 全源夹具 + 编辑回环 + 缓存断言
$env:ADM_AUTOTEST='1'; uv run adm --smoke   # GUI 自动化冒烟
```

## 🤝 贡献

欢迎 issue / PR:

- 新来源适配(最需要:各工具新版本的存储格式变化)
- 各来源在真实环境下的验证报告(路径/字段与实现是否一致)
- UI/UX 改进、英文翻译完善

## 📄 许可与免责

[MIT License](LICENSE)。

- 本项目按「现状」提供,不附带任何担保;作者不对使用造成的损失负责,
  建议批量操作前自行备份
- 使用者应遵守所在地法律及各 AI 工具的服务条款;违规使用责任自负
- 独立个人项目,与 Anthropic / OpenAI / Google / Alibaba / Block / AWS 等
  任何公司无关联;各工具名称与商标归其所有者
- 不收集、不上传任何数据,所有操作本机完成

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=haczen/ai-dialog-manage&type=Date)](https://star-history.com/#haczen/ai-dialog-manage&Date)

---

## 社区 / 友链

本开源项目已链接认可 [LINUX DO 社区](https://linux.do/) 🐧

> [LINUX DO](https://linux.do/) - 新的理想型社区

欢迎在 LINUX DO 讨论、反馈与交流本工具的使用心得。
