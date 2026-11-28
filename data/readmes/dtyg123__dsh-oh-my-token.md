# dsh-oh-my-token

[English](README_EN.md) | 中文

> 让工具输出在 agent 真正需要之前，不进入提示词。

`dsh-oh-my-token` 是 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 插件。它在工具结果**写入日志之前**完成改写，因此模型看到的字节与持久化记录完全一致；它从不改写工具参数、从不触碰磁盘上的会话文件、也不启动任何外部进程。

它把两个工具的理念内建到进程里，而不是捆绑两个二进制：

| 理念 | 来源 | 本插件的做法 |
| --- | --- | --- |
| 按命令与输出形状压缩 | [RTK](https://github.com/rtk-ai/rtk)（Apache-2.0） | 先解析模型已运行的命令，只保留结论和失败细节；命令过滤器没命中时，再按内容形状压缩：git diff/status/log、构建日志、grep/find/ls/tree、重复日志、编号文件与搜索结果。纯 JS，无二进制。 |
| 检索符号而非整文件 | [codegraph](https://github.com/isink17/codegraph) | 把超大且未指定范围的 `read` 变成符号大纲，并限制过大的 `grep` 结果。无 SQLite 图库、无 MCP 服务。 |

外加两项模型根本不需要读取的变换（可分别开关）：对可判定为散文的行，按一张**可自定义的词表**删去或替换「谢谢」「请」「please」「thanks」等词（默认删，也可配成替换成别的词）；以及整理标点——段首的标点删去、挨在一起的两个标点只保留一个（逗号+句号留句号，其余强弱类推）、再删去句末**连续的** `.`、`。`、`,`、`，`（ASCII 省略号 `...` / `…` 除外）。它们作用于工具输出、你亲手输入的消息、助手的回复，以及历史对话——历史部分在组装请求时剥离，因此模型永远不会看到这些内容，而磁盘上的会话文件保持逐字节不变。

还能顺手做的两件事：

- **对话内容编辑**：在设置页直接改写最近的消息（你自己发的或模型回的）。改写只写进下一次请求，不落盘、不改历史日志；点「恢复原内容」即撤销。
- **自动变换记录**：设置页列出最近每次散文步骤实际删掉了哪些词、加上了什么、动了几处标点，改了什么一目了然。

## 它保留了什么

过滤只允许丢弃不承载决策的文本。具体来说：

- `pytest` → `✓ 42 passed in 1.23s`；失败时保留每一条 `FAILED`、`E   `、回溯与摘要行。
- `git status` → `clean`，或前 40 行。
- `git diff` → 文件头加变更行；纯空白 diff 折叠为一行。
- `tsc` → 每条 `error TSxxxx` 加总数；告警丢弃。
- `npm/pnpm/yarn/bun/pip/uv/poetry` 安装 → 成功留摘要行，失败留错误行。
- 其他命令 → 只做 ANSI、回车重绘、重复行与进度条清理。命令字符串永不改写。
- 命令过滤器没命中时（或对历史中的旧工具结果），RTK 结构压缩按形状接管：`git diff/status/log` 保留文件名、计数与 hunk 头；构建日志保留错误、告警与摘要；`cargo build/test` 折叠 Compiling/Checking 进度、保留 `error[E…]`、`test result:` 与 Finished；`go test` 把所有 `ok`/`?` 包折叠成一行结论、失败时保留首个 FAIL 起的细节；`eslint` 紧凑格式按文件分组计数；`grep/find/ls/tree/search-list` 按文件/目录分组并给出计数；重复日志折叠；超长无结构内容保留头尾。它只收缩，不放大。

结果仍超预算时，全文通过 `ctx.spillStore` 保存，标记会告诉模型去哪里取。如果没挂载 spill store，标记会说明如何重跑或重新读取——插件绝不丢弃无法恢复的文本。

## 安装

```sh
dsh plugin --profile web add dsh-oh-my-token
```

本地检出：

```sh
dsh plugin --profile web add file:/path/to/dsh-oh-my-token
```

该命令把包加入配置目录的 `dsh.profile.bundles`，包自带的 `cordis.patch.yml` 负责挂载这一行。可用 `dsh --profile web --dump-config` 查看合成后的配置。

要改预算，在配置目录的 `cordis.patch.yml` 对应行下添加字段；省略的字段沿用 bundle patch 的默认值。开关和散文范围无需改 patch——由设置页面管理。

## 设置页面

**设置 → 省 Token** 是管理面板：

- 每个变换一个开关（5 个命令过滤器、RTK 结构压缩、2 个检索变换、标点整理、词语删除/替换、系统提示词编辑）；
- 压缩力度：省着压 / 默认 / 狠压三档一键设置字符上限与最小改写阈值，展开「高级数字」仍可逐项精调；
- 高级配置：预算、`minChars`/`minGain`、检索阈值、超预算处理（`spill`/`rerun`/`none`）与 `logEvery`，以及插件总开关；
- 散文变换（标点 / 词语）共用的三档范围（`off` / 仅散文输出 / 所有散文）；
- 词语表编辑：每行「词 + 替换」（替换留空即删除），保存后全局生效；
- 对话内容编辑：改写最近消息，只在下次请求发给模型，历史不动，可恢复原内容；
- 自动变换记录：最近每次散文步骤删了哪些词、加上了什么、动了几处标点；
- 节省记录：本次进程与历史累计、移除的 token 与字符、节省比例、按工具明细表，以及消息/回复剥离计数；
- 选择被写入的配置目录，方便确认开关是否真的落盘。

改动在下一次工具调用即生效，无需重启。选择写入配置目录的 `dsh-oh-my-token.state.json`（优先取 `DSH_PROFILE_DIR`，否则从携带本包的配置目录推断），下次启动时覆盖 bundle 配置。统计在同目录的 `dsh-oh-my-token.stats.json`，可在页面清除。

页面由三条精确路由支撑：`/dsh-oh-my-token/state`、`/dsh-oh-my-token/stats` 与 `/dsh-oh-my-token/prompt`（读取当前生效的系统提示词）。

## 系统提示词

在「设置 → 省 Token」底部的「系统提示词」卡片里，打开开关，把你要追加的内容拆成若干个**小段（卡片）**：每张卡片一小段正文，点击「添加一小段」新增，「上移 / 下移」调整顺序，「删除这一段」移除。保存后，所有卡片按从上到下的顺序**拼合成的最终系统提示词**追加到现有 section 之后。保存时旧版 `{ mode, text }` 配置自动迁移为单卡片。

- 每段一个 `interpolate: false` 的 section——已自行替换已知变量，其余 `{{...}}` 保持字面量，不会被当作未知变量而报错；
- 卡片顺序即提示词顺序；
- 运行时上下文快照不受影响；改动在下一次请求生效，无需重启。
- `{{变量}}`：目前 DSH 内置 `{{provider}}`（当前模型供应商）与 `{{model}}`（当前模型名），保存后这两个写法会被替换成当前值；其他写法保持字面量，不报错。
- 「恢复默认提示词」：立即按当前注册实时组装一份系统提示词（首次使用、未发过消息也能读到），按空行**拆成多张卡片**放进编辑器，方便在原默认内容上重新改写；读到的始终是未注入定制文本的原始提示词。

## 配置

| 字段 | 默认值 | 说明 |
| --- | --- | --- |
| `enabled` | `true` | 关闭插件但不移除配置行。 |
| `budgets.default` | `6000` | 没有单独配置的工具的字符上限。 |
| `budgets.read` | `12000` | 文件内容是编辑的基础，因此额度更高。 |
| `budgets.grep` | `6000` | |
| `budgets.bash` | `4000` | |
| `budgets.errorFactor` | `2` | 错误结果允许放大到倍数。 |
| `minChars` | `800` | 小于此值的结果不动（清理不值得冒险）。 |
| `minGain` | `0.05` | 丢弃节省低于此比例的改写；散文句号改写始终保留。 |
| `filters.*` | 全部 `true` | 各过滤器开关：`pytest`、`git`、`tsc`、`packageManager`、`generic`。 |
| `rtk` | `true` | 命令过滤器未命中时，按输出形状再做一层 RTK 结构压缩。也可在设置页面关闭。 |
| `retrieval.readOutlineOverLines` | `400` | 仅当行数超过此值且调用未带 `offset`/`limit` 时才生成大纲。 |
| `retrieval.maxOutlineSymbols` | `60` | |
| `retrieval.maxGrepMatches` | `50` | |
| `prose.stripTrailingPeriod` | `true` | 标点整理：段首标点删去；相邻两个标点只留一个（逗号+句号留句号，同强保留右边）；再删句末**连续的** `.` / `。` / `,` / `，`（省略号除外）。 |
| `prose.stripPoliteness` | `true` | 按 `politenessWords` 词表删去或替换散文行里的词。 |
| `prose.politenessWords` | 内置客套词表 | 每项 `{ word, replace? }`：`replace` 留空或省略 = 删除，填字符串 = 替换。整表未配置时用内置的「谢谢/请/please/thanks…」列表；配置空表 `[]` 则关闭词变换。 |
| `prose.scope` | `filtered` | `filtered` = 仅命令过滤器标记为散文的输出（如 `git log`）；`all`；`off`。 |
| `recovery` | `spill` | `spill` \| `rerun` \| `none`。 |
| `logEvery` | `0` | 每 N 次改写打印一条节省日志；`0` 为静默。 |

未知字段会在激活时报错，而不是静默忽略。以上字段都可以在「设置 → 省 Token」的「高级配置」里修改；`enabled` 是总开关，`filters.*` 对应上方的开关行。

### 为什么句号剥离有防护

删掉文件名、URL、版本号或代码行里的句号，为了省一个 token 而损坏数据，代价太大。因此 `isProseLine` 会拒绝：

- 围栏代码、diff 行、以 `{ [ <` 开头或以 `;{}=` 结尾的行，以及带 `= ( ) ; { } [ ]` 等代码标点又以逗号结尾的行；
- 赋值/声明/语句行（含 `= ; { }` 或以 `const`/`function`/`import` 等开头），客套词删除不会碰它们；
- 含 URL、邮箱、带扩展名路径的行；
- 看起来像版本号（`2.2.0`）或 `host:port` 的内容；
- 列表项（`- `、`*`）、省略号，以及 `e.g.` / `i.e.`。

## 测量

```sh
oh-my-token report [profile-dir | session.jsonl]
```

按事件类型（`user/message`、`assistant/message`、`tool/call`、`tool/result`）统计会话日志，并列出最昂贵的工具结果。这是「改写前」的数字；设置页面显示「改写后」。

```sh
oh-my-token map <file|dir>      # read 会生成的大纲
oh-my-token lint [config.json]  # 校验行配置，不启动 DSH
```

## 还能压什么

把「模型要据此决策的字节」逐个过一遍，结论如下：

- **命令输出**（收益最大）：已有 5 个命令过滤器 + 17 种 RTK 结构压缩器，覆盖 pytest / git / tsc / 包管理器 / eslint / cargo / go test / grep / find / ls / tree 等。剩下的长尾命令（docker、kubectl、make…）按 RTK 的形状识别走 generic + smart-truncate，不再逐个写解析器——每加一个解析器都是一份要维护的回归测试。
- **读文件**：大 `read` 出符号大纲、大 `grep` 截断。再往下压（只给 AST、跳过 import 块）会把「模型能直接引用的文本」换成「模型要再问一次才能拿到的摘要」，省得不多还容易漏关键行，不做。
- **JSON / 图片**：JSON 数组折叠（同结构 N 份只留一份 + 计数）是下一步候选，但 `package-lock` 这类文件删一行就可能让模型拿错版本号，风险不对称，暂缓；图片字节不是文本，属于上游多模态编码的开销，插件层没有安全的压缩点。
- **对话文本**：本轮加了词删除/替换、标点整理、对话编辑。更激进的「语义摘要历史消息」需要额外一次 LLM 调用才能做，违背「不起外部进程」的约束，不做。
- **系统提示词**：只追加/分段改写，不做自动裁剪——提示词里每一个词都是你写来约束模型的，裁掉的代价不可度量。

## 设计约束

- **工具结果只追加。** 替换发生在 `tools/post-execute`，因此被记录的就是替换后的内容。不用 `sessionProjections`、不做追溯修改、不会让前缀缓存失效。聊天文本与旧工具结果则有意不同：历史句号与旧工具结果的 RTK 压缩只在派生请求（`session.deriveMessages()`）中发生，从不写入持久化日志。
- **不改写参数。** DSH 在工具管线里禁止这样做，改写过的命令是另一个可能出错的地方。
- **零新依赖。** `index.js` 只引入自己的文件。
- **过滤器故障不等于工具失败。** 每个分支都有保护；出错时返回原始 decision。
- **与 `dsh-token-frugal` 兼容。** 两者同时挂载时，让 `dsh-token-frugal` 先跑无损编码，再由 `dsh-oh-my-token` 做语义准入。两者在任何变换上都不重叠。

## 刻意不做

- **宿主 CLI 发现。** 告诉 agent 有哪些二进制可用（`PromptContext` 条目、`oh-my-token host-tools`）是独立的可选阶段；注入工具清单会让每个会话都付出提示词字节，包括从不调用 shell 的会话。
- **字符级压缩。** 到处删标点风险很大，只为省一个 token 的零头。只保留上面的散文场景。
- **符号图。** 大纲来自语言感知的正则。LSP 解析器更好，但那也是本插件拒绝引入的构建依赖。
- **输入框下方的小卡片。** 页面放在设置里——人找策略时会去那里；输入框下方的卡片会在每个屏幕重复同样的数字。

## 打赏支持

这个插件在 MIT 许可下完全开源，维护靠个人时间。如果你用起来觉得确实省了 token，欢迎请我喝杯咖啡：

![打赏码](docs/sponsor-qrcode.jpg)

不强制也不承诺什么——代码已经归你用了。

## 致谢

- **[RTK](https://github.com/rtk-ai/rtk)（Apache-2.0）** — 按命令过滤工具输出的思路来自 RTK；本插件的命令过滤器与结构过滤器都是纯 JS 实现。
- **[codegraph](https://github.com/isink17/codegraph)（MCP 服务，FSL-1.1）** — 「先取符号地图，再按范围读取」的检索思路来自 codegraph；本插件用语言感知的正则做了无图库、无 MCP 服务的轻量实现。
- 许可证细节见 [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) 与 [`LICENSES/Apache-2.0.txt`](LICENSES/Apache-2.0.txt)。

## 许可

MIT

RTK 结构过滤器按 Apache-2.0 使用；完整第三方声明（含 Apache-2.0 全文）见 `THIRD_PARTY_NOTICES.md` 与 `LICENSES/Apache-2.0.txt`。
