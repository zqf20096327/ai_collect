# skill-create-debug-dsh

一个给 **DeepSeek Harness (DSH)** 用的 skill：面向写 skill 的人，负责创建、修改、体检，以及回答那个最难自测的问题：**这个 skill 到底会不会被触发。**

`DSH skill` · `SKILL.md 363 行` · `2 个脚本（464 + 414 行）` · `4 篇 references` · `Python 3.8+` · `audit.py 零第三方依赖` · `MIT`

---

## 它解决什么问题

写 skill 的门槛看起来很低：一个 Markdown 文件，加一段 frontmatter，放进目录就能用。

难点在于，DSH 的失败方式**几乎全是静默的**：

- `name` 写成大写或中文，整个 skill 被丢弃，屏幕上没有任何报错；
- 字段名写了 DSH 不认识的（`triggers`、`version`、`author`），一律忽略，文件看上去一切正常；
- 触发场景写进了 `whenToUse`，而这个字段根本不进会话目录，对触发毫无作用；
- `description` 超过 500 字符，尾部被截断，模型永远读不到你精心写的那几条；
- `SKILL.md` 放在嵌套目录里，而扫描深度刻意只有一层，找不到；
- 正文写了 500 行领域知识，每次触发都把这 500 行重新塞进上下文。

这些都不会崩、不报错、不提示。所以「写个 Markdown」并不够，你需要的是一套能**静态体检**加**实测触发率**的工具。本 skill 就是这套工具，外加一份把机制讲清楚的规格速查。

---

## 核心概念速览

### 6 条硬约束

| # | 约束 | 违反后果 |
|---|---|---|
| 1 | `name` 必须匹配 `^[a-z0-9]+(-[a-z0-9]+)*$`（全小写 ASCII） | **整个 skill 被静默丢弃** |
| 2 | `description` 必填、非空 | 同上 |
| 3 | 发现深度**只有一层**：`<root>/<name>/SKILL.md` | 嵌套目录里的 skill 找不到 |
| 4 | 会话目录里**只渲染 `name` + `description`** | `whenToUse` 对触发**毫无作用** |
| 5 | `description` 在目录中被截断到 **500 字符** | 超出部分模型看不到 |
| 6 | 目录是**持久消息**，正文是**工具结果** | 两者都常驻消耗 token |

第 4、5 条最容易踩：`whenToUse` 合法但不参与触发，`description` 超长的部分彻底消失。**把最重要的触发场景放最前面。**

### 只有这 6 个字段被识别

| 字段 | 必填 | 作用 |
|---|:--:|---|
| `name` | 是 | skill 的身份，跨来源合并的唯一键 |
| `description` | 是 | **模型自动触发的唯一依据** |
| `whenToUse` | 否 | 合法，但不进会话目录，写了等于没写 |
| `metadata` | 否 | 提供方元数据，不渲染 |
| `disable-model-invocation` | 否 | `true` 时模型看不到，只能用户手敲 |
| `user-invocable` | 否 | `false` 时用户不能 `/name` 调用 |

其余字段一律静默忽略。**真实案例**：某 skill 写了 592 字符的 `triggers:` 关键词表，一个字都没生效，而真正起作用的 `description` 反而写得敷衍。

两个开关键都是可选，**省略即允许**，这也是绝大多数 skill 该有的状态。值写错（例如 `是`、`true-ish`）会**丢弃整个 skill**，而不是退回默认值。

### 没有触发词机制

DSH **没有关键词表、没有正则、没有匹配打分**。触发是模型读完 `description` 之后的**语义判断**。

所以「触发词」只是写作技巧，不是注册机制：往 `description` 里写用户真会说的原话，本质是给模型的判断多提供一点线索。

### 两条独立触发路径

| 路径 | 谁发起 | 依据什么 | 关闭它的开关 |
|---|---|---|---|
| 模型自动 | 模型判断 | 会话目录里的 `description` | `disable-model-invocation: true` |
| 用户显式 | 用户敲 `/name` | `/` 菜单里的 skill 名 | `user-invocable: false` |

同一份 frontmatter 服务两个表面。**改 `description` 只影响第一条路径**，第二条路径看的是名字。

还有一个反直觉的事实：模型只对**自己搞不定的复杂多步任务**才去查 skill。简单单步请求（「读一下这个 PDF」）即使 description 完美匹配也不会触发。显而易见的流程写成 skill 是浪费，它永远不会被触发。

---

## 安装

安装本身就是「把目录拷进去」，但有两个前提必须满足，否则装了也不生效。

**前提一：必须在 skills 根目录的下一层。** 发现深度只有一层，`<root>/<name>/SKILL.md` 是唯一合法形态，多套一层目录就找不到。

**前提二：放对根目录。** DSH 按 rank 由小到大扫描，rank 小者胜：

| Rank | 来源 | 路径 |
|---:|---|---|
| 100 | `project-dsh` | `<项目根>/.dsh/skills` |
| 200 | `project-agents` | `<项目根>/.agents/skills` |
| 300 | `custom` | 配置项 `customSkillDirs` |
| 400 | `user-dsh` | `$DSH_HOME/skills`（默认 `~/.dsh/skills`） |
| 500 | `user-agents` | `$DSH_AGENTS_HOME/skills`（默认 `~/.agents/skills`） |
| 600 | `bundled` | `bundledSkillDir` 配置项 |

项目根 = 含 `.git` 的最近祖先目录，没有则用当前工作目录。低 rank 会遮蔽高 rank 的同名 skill，被遮蔽者只记日志，没有 API 能枚举出来。

Windows 上用户级 agents 目录即 `C:\Users\<用户名>\.agents\skills`。

安装（Windows PowerShell）：

```powershell
# 用户级安装：对所有项目生效
Copy-Item -Recurse .\skill-create-debug-dsh "$env:USERPROFILE\.agents\skills\"
```

```bash
# Linux / macOS 用户级安装
cp -r ./skill-create-debug-dsh ~/.agents/skills/
```

项目级安装则把同一份目录放到 `<项目根>/.agents/skills/` 或 `<项目根>/.dsh/skills/` 下。

**无需重启。** 改 frontmatter 后模型侧目录会热重载，下一个模型步骤即可见。但 Web UI 的 `/` 菜单不会自动刷新，**需要按 F5**。另外，`references/`、`scripts/`、`assets/` 里的编辑不触发目录刷新，改这些文件不需要做任何操作。

验证是否装上：在 DSH 会话里输入 `/sk`，`skill-create-debug-dsh` 应该出现在候选里（`/` 菜单是不区分大小写的有序子序列匹配，前缀命中排最前）。如果模型侧目录里有它、菜单里没有，先刷新页面，不要急着改 frontmatter。

---

## 脚本用法

两个脚本都在 `scripts/` 下。

### audit.py：静态体检

```bash
python scripts/audit.py                    # 体检全部 skill
python scripts/audit.py --skill <name>     # 体检单个 skill
python scripts/audit.py --json             # 机器可读输出
```

检查项：frontmatter 合规性、命名合法性、行数、正文与 `description` 的 token 成本估算、`description` 质量（长度 / 触发场景 / 边界）、未知字段（死字段）、结构合理性（该不该拆 `references/`）、跨 skill 触发词重叠。

真实输出（本仓库自身，实测）：

```
$ python scripts/audit.py --skill skill-create-debug-dsh

skill-create-debug-dsh    OK
    正文 357 行 | description 319 字符 | 目录常驻约 182 tok | 正文约 5592 tok | 子目录: scripts,references

汇总: 1 个 skill | 0 错误 | 0 警告
每次会话的 skill 目录常驻成本约 182 tokens（仅 description）
```

注意 `正文 357 行` 这个数字与文件总行数（363 行）略有差别：前者统计的是计入上下文成本的正文部分。

拿到报告后按「错误 → 警告 → 建议」的顺序处理。**错误必须先清零**，警告可以判断后再决定。

### eval_trigger.py：触发准确率评估

```bash
python scripts/eval_trigger.py --check                            # 环境就绪性检查
python scripts/eval_trigger.py --skill <name> --gen               # 生成 cases.json 用例模板
python scripts/eval_trigger.py --skill <name> --cases cases.json
python scripts/eval_trigger.py --skill <name> --cases c.json --repeat 3 --probe 60
python scripts/eval_trigger.py --skill <name> --cases c.json --json
```

`--gen` 生成的模板只是骨架（含 3 条示例），**必须人工补足后再跑**：应触发 8 到 10 条，不应触发 8 到 10 条。应触发用例要覆盖正式、口语、不点名但明显需要等不同写法；不应触发用例里最该放的是「近似误触发」，也就是共享关键词但实际需要别的东西的请求。

示例输出（**数字为示意，非实测**）：

```
$ python scripts/eval_trigger.py --skill <name> --cases cases.json --repeat 3 --probe 60

  ✓ #1   期望:应触发   实际:已触发  帮我写个 skill 抓取网页公告
  ✗ #2   期望:应触发   实际:未触发  这个 skill 为什么没触发
  ✓ #8   期望:不应触发 实际:未触发  帮我读一下这个 PDF

  应触发命中率  : 7/8 = 88%
  误触发率      : 0/8 = 0%
  注: 6/48 次运行在探测超时后被掐断 —— 触发决策取自已落盘日志，判定有效
```

**命中率低是欠触发**，去 `description` 里补触发场景。**误触发率高是边界不清**，加「不适用」段。每次只改一个变量再重跑，否则无法归因。

---

## 触发准确率是怎么测的

原理很短：跑一次**真实的无头任务**，然后去读那一次的 session 日志。

```
dsh --profile headless "<查询>"  →  读 session 日志  →  查是否调用了 skill 工具
```

判定依据是日志里 `tool/call` 事件的 `data.name == "skill"`，且 `data.arguments` 里 `name` 等于目标 skill。**这是真实的调用记录，不需要模型自述**，模型说自己「用了 skill」或「没用」都不参与判定。

脚本在 `--probe` 秒后**主动掐断进程**（默认 120 秒）。原因是触发决策发生在任务最开始，之后模型会真的去执行整个工作流（可能数分钟），这部分对判定毫无价值。掐断把单条用例从数分钟压到 1 到 2 分钟。

### 局限（请先读这段再解读数字）

- **headless 是单轮的**，测不出多轮对话里的触发行为；
- 它只回答「有没有被加载」，**测不出加载后模型有没有正确执行正文指令**，那需要人工看轨迹；
- 模型采样有随机性，`--repeat` 少了得到的只是噪声，建议至少 3 次；
- 判定依赖 DSH 的 session 日志格式与 `tool/call` 事件结构。DSH 若改了日志格式，解析可能失效，此时脚本会报「未产生新的 session」或解析不到事件，而不是悄悄给出错误的 0%；
- 用例集的质量决定结论的价值。用显而易见无关的请求凑数，会得到一份好看但无用的 100%。

---

## ⚠️ 副作用与隔离：先把 `DSH_HOME` 指向临时目录

**跑每一条评估用例，都会真实启动一次 headless DSH 会话**，因而会在 `$DSH_HOME/sessions/` 下产生**真实的 session 记录**。

如果直接用默认的 `~/.dsh`，这些 session 会出现在你的会话列表里（在 DSH Web 界面中显示为「未分组」），看起来就像凭空多出来的一堆垃圾会话。跑 12 条用例乘 3 次重复，就是 36 条。

**推荐做法：把 `DSH_HOME` 指向一个临时目录，再跑评估。** 这样评估产生的会话完全隔离，不污染主环境。脚本原生支持这个环境变量：

```python
DSH_HOME = os.environ.get("DSH_HOME") or os.path.join(os.path.expanduser("~"), ".dsh")
```

```powershell
# Windows
$env:DSH_HOME = "F:\tmp\dsh-eval"
python scripts/eval_trigger.py --check
python scripts/eval_trigger.py --skill <name> --cases cases.json
```

```bash
# Linux / macOS
export DSH_HOME=/tmp/dsh-eval
python scripts/eval_trigger.py --skill <name> --cases cases.json
```

另外，脚本会自动创建 `headless` profile（位于 `$DSH_HOME/profiles/headless/`），这也是它写在 `DSH_HOME` 下的内容之一。用临时目录时，评估结束后整个目录可以直接删掉。

---

## 仓库结构

```
skill-create-debug-dsh/
├── SKILL.md                        363 行，主指令
├── scripts/
│   ├── audit.py                    464 行，静态体检，仅用标准库
│   └── eval_trigger.py             414 行，触发率评估，依赖 zstandard
├── references/
│   ├── dsh-spec.md                 198 行，frontmatter 字段语义、发现规则、rank 优先级
│   ├── dsh-behavior.md             183 行，运行期行为、目录与正文生命周期、token 成本模型
│   ├── authoring.md                233 行，写法方法、description 打磨、渐进式披露
│   └── eval-methodology.md         187 行，用例设计、结果解读、A/B 对比
├── LICENSE                         MIT
└── .gitignore
```

合计 2042 行，约 90 KB。`references/` 是按需加载的长文档，正文只在需要精确细节时指向它们，这样触发成本才可控。

---

## 兼容性

| 项目 | 要求 |
|---|---|
| Python | 3.8+（开发环境为 3.13） |
| 第三方包 | `audit.py` 无；`eval_trigger.py` 需要 `zstandard`，用于读取 DSH 的 zstd 压缩 session 日志 |
| DSH CLI | 仅 `eval_trigger.py` 需要，且 `dsh` 必须在 PATH 中 |
| 平台 | 在 Windows 上开发，含 Windows 专属处理；代码有跨平台分支 |

`zstandard` 是评估脚本的**硬依赖**，缺少时 session 日志解不开：

```bash
pip install zstandard
```

Windows 专属处理包括：任务栏弹窗抑制（防止掐断进程树时弹出「应用程序无法正常启动」对话框）、用 `taskkill /T` 结束整棵无头进程树、解析 npm 的 `.CMD` shim 以定位 `dsh`。其余路径有跨平台分支（用 `os.killpg` 结束进程组），但**非 Windows 平台的实测覆盖较少**，在 Linux 或 macOS 上遇到问题请提 issue。

关于 DSH 版本：本 skill 记录的约束（500 字符截断、rank 表、日志事件结构）均以写作时的 DSH 行为为准。DSH 若调整这些默认值，`references/` 里的规格与 `audit.py` 的检查项可能随之漂移。

---

## 许可证

本项目采用 **MIT License**，Copyright (c) 2026 ChengYK (https://github.com/Murphy2000-cyk)，全文见 `LICENSE`。

你可以自由使用、修改、再分发，包括商用，保留版权声明即可。
