# 🎯 Async Issue Manager

**上班前丢任务，下班后看结果。**

**async-issue-manager 是一个纯本地、基于文件的 AI Agent 异步任务管理系统（本地 Issue 管理）：用 `.issues/` 目录里的 Markdown 文件 + Git 记录任务，给在用 OpenClaw 等 Agent 框架、白天不在电脑前的人用，解决「人必须盯着 Agent 一问一答」的问题——上班前丢任务，Agent 按标签分派执行，下班后看结果。**

A local-first, file-based issue tracker and async task queue for AI agents: tasks are Markdown files in `.issues/`, tracked by Git, matched to agents by label. Python standard library only, no GitHub Issues/Jira/Notion required.

纯 Python 3.8+ 标准库 · 零外部依赖 · 可作为 OpenClaw Skill 使用 · MIT

## 为什么需要这个？（AI Agent 异步任务）

大多数人用 AI Agent 的方式是"坐在电脑前，一问一答"。但如果你是上班族呢？

```
❌ 传统方式：人盯着 Agent 干活，效率 = 你在线的时间
✅ 异步方式：丢任务就走，Agent 自己调度、执行、归档
```

这个系统让你的 Agent 像一个**自动运转的小团队**——你自己配置有哪些 Agent、各自擅长什么，系统按标签匹配任务。

## 工作流

```
    你随口说一句 → 建 Issue（排优先级、打标签）
         ↓
    每小时 cron 触发 → 巡查 + 广播，把 open Issue 按标签匹配给各 Agent
         ↓
    主 Agent 读取广播结果 → 派活给子 Agent 执行
         ↓
    子 Agent 完成 → 关单（Issue 移入 closed/）
         ↓
    你下班看 closed/ → 今天的成果
```

旁路：
- **🔍 巡查系统**：发现问题自动建 Issue，交给 Agent 处理
- **📦 纯本地**：不依赖外部服务；`.issues/` 是纯文本，可纳入 Git

## 特性

- **纯本地** — `.issues/` 目录 + Git，不依赖 GitHub Issues / Jira / Notion
- **自动巡查** — 检查 stub、`TOOLS.md` 引用的脚本、闲置 Skill、`MEMORY.md` 大小（见下文）
- **按标签 / 优先级匹配** — `broadcast.py` 把 open Issue 匹配给订阅的 Agent，最终派活由你的主 Agent 判断
- **巡查建单去重** — 巡查建单按标题去重，相同标题不会重复建 Issue
- **Git 可追溯** — `.issues/` 是纯文本，可纳入 Git 追踪完整历史（需自行 commit，见 [SKILL.md](SKILL.md) 示例）
- **自愈** — `manager.py sync` 修复 `index.json` 与目录文件不一致

## 快速开始（本地 Issue 管理）

### 0. 获取代码

```bash
git clone https://github.com/ythx-101/async-issue-manager.git
```

需要 Python 3.8+，无需 `pip install`。

### 30 秒体验

```bash
mkdir /tmp/aim-demo && cd /tmp/aim-demo
bash <repo>/examples/quickstart.sh     # <repo> 换成上一步 clone 的路径
```

### 1. 安装

```bash
# 方式 A: 作为 Skill 安装（推荐）
cp -r async-issue-manager/ <your-workspace>/skills/

# 方式 B: 直接复制脚本到工作区
mkdir -p <your-workspace>/scripts/issues
cp -r async-issue-manager/scripts/* <your-workspace>/scripts/issues/
```

`.issues/open|in-progress|closed` 目录在首次运行 `manager.py` 时自动创建。

### 2. 创建第一个 Issue

```bash
python3 scripts/manager.py create \
  --title "测试异步任务系统" \
  --body "验证 Issue 创建 → 分配 → 关闭的完整流程" \
  --priority P2 \
  --labels test
```

### 3. 配置 Cron 自动调度

在 OpenClaw 中配置 cron：

```json
{
  "schedule": { "kind": "cron", "expr": "0 * * * *" },
  "payload": { "kind": "systemEvent", "text": "issue-hourly-dispatch" },
  "sessionTarget": "main"
}
```

或使用系统 crontab：

```
0 * * * * cd /workspace && bash scripts/auto-dispatch.sh
```

`auto-dispatch.sh` 只做「巡查 → 广播 → 写日志（`logs/issue-dispatch.log`）」，派活由你的主 Agent 读取结果后决定。

### 4. 查看结果

```bash
python3 scripts/manager.py list --status open
python3 scripts/manager.py list --status closed
python3 scripts/manager.py show 1
```

### 运行测试

```bash
python3 -m unittest discover -s tests -v
```

## 命令一览

| 命令 | 说明 |
|------|------|
| `manager.py create --title T [--body B] [--priority P2] [--labels a b]` | 创建 Issue |
| `manager.py list [--status open\|in-progress\|closed] [--labels a b] [--priority P] [--assignee A]` | 列出 Issue（`--status` 默认 `open`） |
| `manager.py show <id>` | 显示 Issue 全文 |
| `manager.py assign <id> <agent>` | 分配给某个 Agent，移入 `in-progress/` |
| `manager.py close <id> [--resolution TEXT]` | 关闭 Issue，移入 `closed/` 并追加解决方案 |
| `manager.py stats` | 统计概览 |
| `manager.py sync` | 修复 `index.json` 与目录文件的不一致（含孤儿文件） |
| `broadcast.py [--json]` | 按 `AGENT_SUBSCRIPTIONS` 把 open Issue 匹配给 Agent |
| `inspector.py [--dry-run] [--json]` | 运行巡查；发现问题时退出码为 1 |
| `auto-dispatch.sh` | 巡查 + 广播 + 写日志，供 cron 调用 |

### 工作区定位规则

与 `find_workspace()` 一致，按顺序：

1. 环境变量 `WORKSPACE` 或 `OPENCLAW_WORKSPACE`（目录存在时）
2. 从脚本所在目录向上查找含 `.issues/` 的目录
3. 当前目录

### Issue 文件格式

```markdown
---
id: 35
title: 研究 xxx 方案
priority: P1
labels: research, analysis
status: open
assignee: unassigned
created_at: 2026-02-21T10:00:00
updated_at: 2026-02-21T10:00:00
---

具体描述任务内容...
```

## 目录结构

```
.issues/                          # Issue 存储
├── open/                         # 待处理
├── in-progress/                  # 进行中
├── closed/                       # 已完成
└── index.json                    # 索引

scripts/
├── manager.py              # Issue CRUD 核心
├── broadcast.py            # Agent 订阅 & 广播
├── inspector.py            # 巡查系统
└── auto-dispatch.sh        # 自动调度入口
```

4 个脚本，纯 Python 标准库 + Bash，零外部依赖。

## Issue 生命周期

```
创建 → open/ → 分配 → in-progress/ → 完成 → closed/
                                        ↑
                            巡查系统自动创建
```

每次状态变更：
1. 文件从一个目录移动到另一个目录
2. YAML front matter 自动更新
3. `index.json` 同步更新
4. （可选）由你的 cron 执行 `git add .issues && git commit`

## 自定义

### 修改 Agent 订阅

编辑 `scripts/broadcast.py` 中的 `AGENT_SUBSCRIPTIONS`（标签或优先级任一匹配即推送）：

```python
AGENT_SUBSCRIPTIONS = {
    "your_agent": {
        "labels": ["your-label"],
        "priority": ["P1", "P2"],
        "description": "擅长什么"
    }
}
```

### 添加巡查规则

在 `scripts/inspector.py` 的 `Inspector` 类中添加新方法：

```python
def check_your_custom_rule(self):
    """你的自定义检查"""
    # 检查逻辑...
    if problem_found:
        self.issues.append({
            "priority": "P2",
            "title": "发现问题",
            "body": "问题描述",
            "labels": ["your-label"]
        })
```

然后在 `run()` 方法中调用它。

## 巡查系统（自动发现问题并建 Issue）

**Agent 不只执行任务，还能自己发现问题。** `inspector.py` 内置 4 项检查，发现问题后按标题去重建 Issue（`--dry-run` 只报告不建单）：

| 检查项 | 检查对象 | 发现后 |
|--------|----------|--------|
| 未实现 stub / TODO | 工作区脚本中的 `not_implemented` / `TODO:` 标记 | 建 Issue |
| `TOOLS.md` 引用 | `TOOLS.md` 中引用的脚本路径是否存在 | 建 Issue |
| 闲置 Skill | `skills/our/` 下 30 天未修改的目录 | 建 Issue |
| 记忆膨胀 | `MEMORY.md` 超过 10KB | 建 Issue |

巡查只负责建 Issue，不会自动修复；修复交给 Agent 处理。其他检查（例如 Agent 的日常产出检查）需要自行按上文方式实现。

## 适用场景 / 和其他方案比

### 适用场景

| 场景 | 做法 |
|------|------|
| 上班族 | 早上丢任务 → 白天 Agent 自动跑 → 晚上看结果 |
| 开发者 | 巡查系统发现问题 → 建 Issue → Agent 处理 |
| 内容创作 | 建"写教程"Issue → 写手 Agent 生成草稿 → 人工审核 |
| 研究 | 建"研究 xxx"Issue → 探索者收集资料 → 分析师出报告 |

### 定性对比

| | 本项目 | GitHub Issues | Jira / Linear / Notion | 单个 TODO.md |
|---|---|---|---|---|
| 需要联网 / 账号 | 否 | 是 | 是 | 否 |
| 数据格式 | Markdown 文件 + `index.json` | 云端托管 | 云端托管 | 单个 Markdown |
| Agent 读写难度 | 低（读写本地文件 / 调 CLI） | 需 API 与认证 | 需 API 与认证 | 低，但无结构 |
| 多人协作 | 不适合 | 适合 | 适合 | 不适合 |
| 可视化看板 | 无 | 有 | 有 | 无 |

短板：没有 Web 界面；不适合多人团队协作；派活依赖你自己的 Agent。

### 不适合的场景

- 需要多人同时协作、评论、权限管理的团队项目
- 需要图形化看板或报表
- 希望系统自己调用 Agent 执行任务（本项目只负责记录、匹配与广播）

## 常见问题 FAQ

**不用 OpenClaw 能用吗？（without OpenClaw）**
能。CLI 是普通 Python 脚本，任何能执行 shell 的 Agent 或 crontab 都可以调用。

**和 GitHub Issues / Jira / Notion 有什么区别？**
本项目是纯本地文件，不需要账号和网络，Agent 直接读写 Markdown；代价是没有 Web 界面、不适合多人协作。

**需要联网或数据库吗？（offline / no database）**
不需要。数据是 `.issues/` 下的 Markdown 文件加一个 `index.json`。

**怎么让 Agent 每小时自动处理任务？（cron）**
用 cron 每小时运行 `auto-dispatch.sh`，它会巡查并广播，结果写入 `logs/issue-dispatch.log`；派活由你的主 Agent 读取结果后决定。

**怎么配置哪个 Agent 接哪类任务？（agent routing）**
编辑 `broadcast.py` 里的 `AGENT_SUBSCRIPTIONS`，Issue 的标签或优先级任一匹配即推送给该 Agent。

**手动挪了文件，index.json 和目录对不上怎么办？（sync）**
运行 `python3 scripts/manager.py sync`，它会按文件所在目录修正状态，并把没有索引的孤儿文件纳入 `index.json`。

**多台设备怎么同步？**
把 `.issues/` 放进 Git，用 push / pull 同步。

**怎么加自定义巡查规则？**
在 `inspector.py` 的 `Inspector` 类里加一个检查方法，并在 `run()` 中调用，见上文「添加巡查规则」。

## 作者的使用情况

以下是作者自述的数据，这个系统在作者的 OpenClaw 实例上运行了 2 周的成果：

- **35 个 Issue** 被创建（自动 + 手动）
- **30+ 个已关闭**（完成率 > 85%）
- **巡查系统**自动发现了文档过期、代码 stub、资源闲置等问题并建 Issue，由 Agent 处理
- **零外部依赖** — 纯文件系统 + Git

## 灵感来源

- OpenClaw 的 `sessions_spawn` 机制（子 Agent 自动执行）
- steipete 的"人才是瓶颈"哲学（不搞复杂编排，指挥官直接判断）
- GitHub Issues（文件格式借鉴，但不依赖 GitHub 平台）

## License

MIT，见 [LICENSE](LICENSE)。

## Authors

**林月 (@YuLin807)** — [x.com/YuLin807](https://x.com/YuLin807)  
**小灵 🦞** — AI Partner

---

*人在工位，龙虾在家干活。这才是人机协作该有的样子。*
