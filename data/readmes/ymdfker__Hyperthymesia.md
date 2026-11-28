# Hyperthymesia

[English user guide](#english-user-guide) · [GitHub](https://github.com/ymdfker/Hyperthymesia) · [AtomGit](https://atomgit.com/ynndfker/Hyperthymesia)

给 AI agent 用的长期记忆。接入后，你在 Claude Code、Codex、WorkBuddy、Qoder、DeepSeek Harness 里说过的事实、做过的决定、
代码里定下的约定，新开会话时 agent 依然记得，不用再交代一遍。

- 记忆库存在你电脑上（`~/.hyperthymesia/`）；后台整理时，相关材料会发送给宿主使用的模型，密码、密钥先做遮盖。
- 后台自动整理，用你 agent 自己最便宜且通过能力检查的模型和额度；额外花费取决于对话和宿主，可通过日志查看实际用量。
- 个人的事所有项目通用；每个项目的约定只在该项目里可见。

## 接入步骤

找到你用的 agent，只按那一节一步步做。用多个 agent 就每一节各做一遍。

以下一键命令安装最新正式版本；升级后请完全退出并重新打开你的agent。

- [Claude Code](#claude-code)
- [Codex](#codex)
- [WorkBuddy](#workbuddy)
- [Qoder](#qoder)
- [DeepSeek Harness（dsh）](#deepseek-harnessdsh)

使用打包程序不需要安装Python；宿主所需的CLI或Node.js按下面对应步骤配置。

### Claude Code

**1. 安装并接入**

- **Mac / Linux**：打开“终端”（Mac：按 `Command + 空格`，输入“终端”回车），复制下面整行，粘贴进去，按回车：

  ```bash
  curl -fsSL https://github.com/ymdfker/Hyperthymesia/releases/latest/download/install.sh | sh -s -- claude
  ```

- **Windows**：在开始菜单搜索“PowerShell”并打开，复制下面整行，粘贴进去，按回车：

  ```powershell
  $env:HY_AGENTS="claude"; irm https://github.com/ymdfker/Hyperthymesia/releases/latest/download/install.ps1 | iex
  ```

看到“完成”或“Complete”字样即可。

**2. 重启 Claude Code**

完全退出 Claude Code（关掉所有窗口或终端里的 claude），再重新打开。

**3. 检查（可选）**

新开一个终端（或 PowerShell），执行：

```bash
hyperthymesia doctor --agent claude
```

“写入提供方”应显示 `claude`。这只确认整理提供方；还需要确认 MCP 已连接、钩子实际触发。完整检查步骤见[兼容核查清单](docs/desktop-compat.md)。

### Codex

**1. 安装并接入**

- **Mac / Linux**：打开“终端”（Mac：按 `Command + 空格`，输入“终端”回车），复制下面整行，粘贴进去，按回车：

  ```bash
  curl -fsSL https://github.com/ymdfker/Hyperthymesia/releases/latest/download/install.sh | sh -s -- codex
  ```

- **Windows**：在开始菜单搜索“PowerShell”并打开，复制下面整行，粘贴进去，按回车：

  ```powershell
  $env:HY_AGENTS="codex"; irm https://github.com/ymdfker/Hyperthymesia/releases/latest/download/install.ps1 | iex
  ```

看到“完成”或“Complete”字样即可。

**2. 重启 Codex**

完全退出 Codex，再重新打开。

**3. 批准钩子**

在 Codex 输入框里输入 `/hooks` 回车，在列表里找到 hyperthymesia，选择批准（信任）。
不批准的话 Codex 不会运行它，记忆不会生效。

安装会在 Codex 配置里加入 `[features.code_mode]` 的 `direct_only_tool_namespaces = ["mcp__hyperthymesia"]`，并把全局 `tool_output_token_limit` 和记忆读取工具的 `output_token_limit` 设为 262144（你已自设全局上限则不改），让记忆读取结果完整交给模型，不被截断。如果你的配置里已有 `features.code_mode` 设置，安装不会改动，只会提示你手动把这一项加进去。

**4. 检查（可选）**

新开一个终端（或 PowerShell），执行：

```bash
hyperthymesia doctor --agent codex
```

“写入提供方”应显示 `codex`。这只确认整理提供方；还需要确认 MCP 已连接、钩子实际触发。完整检查步骤见[兼容核查清单](docs/desktop-compat.md)。

### WorkBuddy

**Windows lite 构建写入报“宿主CLI鉴权失败”时**：这类构建的内置 CLI 不能复用桌面登录，只能让后台整理走你自己的 OpenAI 兼容 API。
1. 新建 `%USERPROFILE%\.hyperthymesia\config.toml`（Mac 为 `~/.hyperthymesia/config.toml`），按下文“用 API key 整理记忆”的示例写 `[writer]` 四个字段（provider、model、base_url、api_key_env），换成你的服务商。
2. 在 PowerShell 执行 `setx DEEPSEEK_API_KEY "你的key"`（变量名与 `api_key_env` 一致；文件里不写 key），然后完全退出并重开 WorkBuddy 和终端。
3. 执行 `hyperthymesia doctor`：应显示“写入提供方：openai”和“key：已从环境变量 … 读到”。再执行 `hyperthymesia write` 确认写入。

**WorkBuddy 5.3.14退出注意事项**：退出时结束钩子不能可靠送达，未达到批量阈值的尾部可能要等下次进入会话、触发启动钩子后才自动补写。仅打开应用停在首页不保证触发；补写完成前，新会话可能答不出尾部信息。已入库记忆的读取不受此问题直接影响。停用接入请执行卸载命令并重启宿主。

**1. 安装并接入**

- **Mac / Linux**：打开“终端”（Mac：按 `Command + 空格`，输入“终端”回车），复制下面整行，粘贴进去，按回车：

  ```bash
  curl -fsSL https://github.com/ymdfker/Hyperthymesia/releases/latest/download/install.sh | sh -s -- workbuddy
  ```

- **Windows**：在开始菜单搜索“PowerShell”并打开，复制下面整行，粘贴进去，按回车：

  ```powershell
  $env:HY_AGENTS="workbuddy"; irm https://github.com/ymdfker/Hyperthymesia/releases/latest/download/install.ps1 | iex
  ```

看到“完成”或“Complete”字样即可。

**2. 重启 WorkBuddy**

完全退出 WorkBuddy（Mac：菜单栏 WorkBuddy → 退出；Windows：右下角托盘图标右键 → 退出），再重新打开。

**3. 检查（可选）**

新开一个终端（或 PowerShell），执行：

```bash
hyperthymesia doctor --agent workbuddy
```

“写入提供方”应显示 `codebuddy`（WorkBuddy 内置的就是 CodeBuddy）。这只检查整理配置；还要在 WorkBuddy 的 MCP 设置里确认 `hyperthymesia` 连接成功。

桌面版配置写入 `~/.workbuddy/settings.json` 和 `~/.workbuddy/mcp.json`，原文件会先备份；已有 CodeBuddy CLI 配置保留。若要单独给 CLI 接入，执行 `hyperthymesia install codebuddy`。

上述桌面路径从v0.2.5起生效；v0.2.4旧版使用的是CLI入口。已安装旧版的用户请重新执行第1步升级，再重启WorkBuddy。

### Qoder

**1. 安装并接入**

- **Mac / Linux**：打开“终端”（Mac：按 `Command + 空格`，输入“终端”回车），复制下面整行，粘贴进去，按回车：

  ```bash
  curl -fsSL https://github.com/ymdfker/Hyperthymesia/releases/latest/download/install.sh | sh -s -- qoder
  ```

- **Windows**：在开始菜单搜索“PowerShell”并打开，复制下面整行，粘贴进去，按回车：

  ```powershell
  $env:HY_AGENTS="qoder"; irm https://github.com/ymdfker/Hyperthymesia/releases/latest/download/install.ps1 | iex
  ```

看到“完成”或“Complete”字样即可。

**2. 登录 qodercli**

安装时会自动装好 Qoder 官方命令行 qodercli（整理记忆要用它，用的是你自己的 Qoder 额度）。
在终端里执行下面一行，浏览器会打开 Qoder 登录页，登录并授权即可：

```bash
qodercli login
```

如果安装时提示“需要 npm”：先到 <https://nodejs.org> 下载安装 Node.js（选 LTS 版），然后重新执行第 1 步。

**3. 重启 Qoder**

完全退出 Qoder，再重新打开。

**4. 检查（可选）**

新开一个终端（或 PowerShell），执行：

```bash
hyperthymesia doctor --agent qoder
```

“写入提供方”应显示 `qoder`。这只确认整理提供方；还需要确认 MCP 已连接、钩子实际触发。完整检查步骤见[兼容核查清单](docs/desktop-compat.md)。

### DeepSeek Harness（dsh）

**1. 安装并接入**

- **Mac / Linux**：打开“终端”（Mac：按 `Command + 空格`，输入“终端”回车），复制下面整行，粘贴进去，按回车：

  ```bash
  curl -fsSL https://github.com/ymdfker/Hyperthymesia/releases/latest/download/install.sh | sh -s -- dsh
  ```

- **Windows**：在开始菜单搜索“PowerShell”并打开，复制下面整行，粘贴进去，按回车：

  ```powershell
  $env:HY_AGENTS="dsh"; irm https://github.com/ymdfker/Hyperthymesia/releases/latest/download/install.ps1 | iex
  ```

看到“完成”或“Complete”字样即可。

**2. 确认 dsh 已填 DeepSeek API key**

整理记忆用的是你在 dsh 里配置的 DeepSeek key（自动选最便宜的模型）。如果还没填过：
在终端执行 `dsh web`，在打开的页面里进入 设置 → 模型，在 DeepSeek 一栏填入你的 API key（在 <https://platform.deepseek.com> 申请）并保存。

**3. 重启 DeepSeek Harness（dsh）**

在运行 `dsh web` 的终端里按 `Ctrl + C` 关掉它，再重新执行 `dsh web`。

**4. 检查（可选）**

新开一个终端（或 PowerShell），执行：

```bash
hyperthymesia doctor --agent dsh
```

“写入提供方”应显示 `dsh`。这只确认整理提供方；还需要确认 MCP 已连接、钩子实际触发。完整检查步骤见[兼容核查清单](docs/desktop-compat.md)。

### Windows配置与排错

- Qoder用户级MCP与钩子均使用`~/.qoder/settings.json`；升级接入会先备份，只迁移本服务在旧`mcp.json`中的条目。
- WorkBuddy支持发现注册安装位置和lite构建。非标准位置仍无法发现时，可在启动宿主前设置`HYPERTHYMESIA_CODEBUDDY_CLI`为实际`cli/bin/codebuddy`或JavaScript入口；它不是登录凭据。
- `hyperthymesia doctor --agent workbuddy --check-cli`可无模型检查启动；`doctor --agent qoder --check-cli`同理。启动通过不代表模型鉴权通过；若lite构建没有独立登录入口且桌面认证不能复用，需要明确配置自己的兼容API，不会自动切换账号或收费渠道。
- 数据目录可用`HYPERTHYMESIA_HOME`指定，例如PowerShell中`$env:HYPERTHYMESIA_HOME="F:\Hyperthymesia-data"`。它不改变exe解包目录；系统盘满时还需将标准`TEMP`和`TMP`设为可写、有空间的目录，再重启宿主。搬迁旧库前请退出宿主并备份。
- 失败保留原材料，`write`会返回失败状态；查看数据目录内的`logs/writer.log`与`logs/hooks.log`。新锁由操作系统释放。缺失Stop的轮次只在原会话记录明确完成且唯一匹配时恢复，否则继续保留，`doctor`会显示未完成数量。

### 遇到问题

- **提示找不到 hyperthymesia 命令**：关掉终端重新打开再试；还不行就用完整路径：Mac/Linux 为 `~/.local/bin/hyperthymesia`，
  Windows 为 `%USERPROFILE%\.hyperthymesia\bin\hyperthymesia.exe`。
- **Mac 提示“无法验证开发者”**：系统设置 → 隐私与安全性 → 点“仍要打开”。
- **想看记下了什么**：正常聊几轮后执行 `hyperthymesia context 项目目录`。记忆在后台整理，聊得够多或会话结束时才写入，不会马上出现。

## 可选操作

**让 agent 记得接入之前的聊天**：

```bash
hyperthymesia import --list
hyperthymesia import --agent 你的agent --session 会话编号
```

（`--all --days 7` 导入最近 7 天全部会话；只能补回对话，补不回当时的代码改动。）

**只在某个项目里试用**：`hyperthymesia install 你的agent --project 项目目录`（支持 claude、codex、codebuddy、workbuddy、qoder）。dsh 按 profile 接入，不提供项目级安装隔离。

**用 API key 整理记忆**（一般不需要：会自动沿用 agent 里已配的 key；只有想让整理走另一个 API 时才配）：
新建 `~/.hyperthymesia/config.toml`，写入：

```toml
[writer]
provider = "openai"                      # 任意 OpenAI 兼容接口
model = "deepseek-chat"
base_url = "https://api.deepseek.com/v1"
api_key_env = "DEEPSEEK_API_KEY"         # 只写环境变量名，key 本身放在环境变量里，本工具不保存
```

**后台模型选择**：自动选择分别检查质量、速度和可获得的用量；宿主没有上报token时标为“未知”，不会仅因此拒绝模型，也不能把未知用量当成已证实低开销。准入题允许把同一方案的两个步骤分条保存；多存一句“帮你写通知”这类客套话只记警告，不判模型不可用。无可用验收时最多试探4个最便宜的候选；评分标准更新后，已保存的准入回复会在本地重判，不重复花额度。原始回复和判定原因脱敏记录在`logs/models.log`。`doctor --check-cli`只运行版本检查，不调用模型或刷新准入缓存。

如果你已确认某个模型在本机可用，可在`config.toml`显式设置`[writer]`下的`model = "你的宿主实际支持的模型ID"`。这会跳过自动准入，**不代表质量已验收**，也不会自动改用别家宿主或付费API。显式指定只控制模型，提供方仍遵循宿主或你自己的配置。自动选择失败会保留积压并给出日志和配置路径。

**写入结果说明**：`write` 显示“写入 0 轮”时括号里会说明原因（没有待写轮次、此前已写过、或还有未完成轮次）。个别条目的引用在原文里找不到时，只挂起这几条到 `~/.hyperthymesia/held_entries.jsonl`（不入库），其余照常写入。同一宿主命令行同一时刻只给一个写入进程用，其余排队，避免本地端口冲突。

**升级**：重新执行你那一节第 1 步的命令即可（会覆盖程序并重新接入，记忆保留）。如果你下载的是带版本号的文件（如`hyperthymesia-v0.2.8.exe`）并直接执行`install`，程序会先把自己复制到`~/.hyperthymesia/bin/`下的固定文件名，宿主配置只引用这个固定路径；以后替换它即可升级。

**写入显示“批次被另一个写入进程占用”**：说明有别的写入进程（常见于升级前的旧版本）持有该项目的锁，提示里会给出pid；结束该进程后再执行`hyperthymesia write`。

**卸载**：`hyperthymesia uninstall 你的agent`（移除本工具配置，保留其他条目；备份用于需要时手动恢复）。删除 `~/.hyperthymesia/` 即清空全部记忆。

## 常用命令

| 命令 | 作用 |
|---|---|
| `install <agent> [--project 目录]` | 接入 agent（原配置先备份） |
| `uninstall <agent> [--project 目录]` | 移除本工具配置，保留其他条目 |
| `doctor [--agent X]` | 查看整理提供方和模型；不证明钩子、MCP、召回全链路通过 |
| `context [目录]` | 查看该目录下会注入给 agent 的记忆 |
| `write` | 立即整理积压对话（平时后台自动） |
| `import --list` / `import --agent X --session 编号` | 导入接入前的会话 |

### 写入失败后继续

引用修正请求会附上原始材料，只修引用。仍找不到来源的条目保留为待处理，不会被当作已完成。写入进度保存在`state.db`，已保存的对象与事实不会因重复执行同一步而重复插入；下次执行`write`沿用原批次并从未完成阶段续接，不必重导全部历史。只有阶段全部完成才确认该批处理完成，完成计数不代表事实完整率。

历史事实按来源时间判断新旧，而不是按导入先后。来源时间不清楚、引用含义不足、哪些内容值得保存，仍需要模型判断，程序不能保证语义全对。格式有歧义时保留原回复并报错，不要求模型重写正确内容；请保留`state.db`和`logs/writer.log`用于排查，不要清库重导。日志包含已脱敏的模型回复。排查后可执行`hyperthymesia write`继续处理待完成步骤。

## 它是怎么工作的

每轮开始，钩子把相关记忆注入给 agent（记忆多时只注入目录，agent 通过 MCP 工具按需读取）；每轮结束，记下你的原话、
agent 的最终回复和本轮代码改动；积压够多或会话结束时，后台用该 agent 最便宜的模型整理进 `~/.hyperthymesia/`，
旧值被新值取代时自动失效。代码改动通过独立的影子仓库记录，不碰你的 git 历史；`.env`、私钥等凭据文件不读取。

**后台整理分两步**：先把一批对话（默认积压约 28000 token 触发，单批上限约 40000 token，约 20 轮）分成最多 3 段逐轮抽取，材料按轮编号，模型只给出处编号，原文由程序复制；没抽到任何内容的轮次会单独补问。再整理一次：带上相关旧记录，判断哪些已存在、哪些更正旧值、哪些应合并或拆分，以及新事项是否并入已有对象（只能并入它看过旧记录的对象，否则新建）。做不了的个别项挂起到 `held_entries.jsonl`，不让整批失败。阈值可用环境变量 `HYPERTHYMESIA_BACKLOG_TOKENS`、`HYPERTHYMESIA_BATCH_TOKENS` 调整；`HYPERTHYMESIA_WRITER_MODE=single` 改回旧的一次调用写法。

**读取**：记忆多时只注入目录；agent 用 `memory_read_objects` 按对象读取，可加 `full=true` 看助手建议全文，加 `include_history=true` 看已失效的旧值。目录自上次读取后没变时不重复返回。

## English user guide

Hyperthymesia gives AI agents long-term memory across chats. It captures facts, decisions, project conventions and code changes, then makes relevant memories available in later conversations.

- Memories are stored locally in `~/.hyperthymesia/`. Background extraction sends relevant conversation material to the model used by your agent, after masking detected credentials. This is not fully offline processing.
- Background writing uses your agent's own model access and quota. Automatic selection considers available acceptance results, speed, token usage and price. Extra usage varies; there is no guaranteed overhead percentage.
- Personal memories are shared across projects; project memories belong to their project.

Source repositories: [GitHub](https://github.com/ymdfker/Hyperthymesia) · [AtomGit](https://atomgit.com/ynndfker/Hyperthymesia). The installation commands below download published **GitHub Release** assets. The commands always install the latest published version.

### 1. Install and connect your agent

Choose the identifier for your agent:

| Agent | Identifier |
|---|---|
| Claude Code | `claude` |
| Codex | `codex` |
| WorkBuddy desktop | `workbuddy` |
| Qoder | `qoder` |
| DeepSeek Harness | `dsh` |

**macOS / Linux:** open Terminal and run the following. Replace `claude` with your agent's identifier from the table.

```bash
AGENT=claude
curl -fsSL https://github.com/ymdfker/Hyperthymesia/releases/latest/download/install.sh | sh -s -- "$AGENT"
```

**Windows:** open PowerShell and run the following. Replace `claude` with your agent's identifier.

```powershell
$env:HY_AGENTS="claude"
irm https://github.com/ymdfker/Hyperthymesia/releases/latest/download/install.ps1 | iex
```

No Python installation is required for the packaged executable. Wait for the installer to report completion. Repeat for each agent you use.

### 2. Complete your agent's setup

- **Claude Code:** fully quit all Claude Code windows or terminal sessions, then reopen it.
- **Codex:** fully quit and reopen Codex. Enter `/hooks` and approve/trust the Hyperthymesia hooks. Without approval, the hooks will not run.
- **WorkBuddy:** fully quit and reopen the app. In its MCP settings, ensure `hyperthymesia` is enabled and connected. Desktop settings use `~/.workbuddy/settings.json` and `~/.workbuddy/mcp.json`; existing files are backed up and CodeBuddy CLI settings are preserved. Use `hyperthymesia install codebuddy` for the separate CLI.
- **Qoder:** the installer sets up the official `qodercli` used for background writing. Run `qodercli login`, complete browser authorization, then fully restart Qoder. If the installer requires npm, install Node.js LTS from [nodejs.org](https://nodejs.org/) and rerun installation.
- **DeepSeek Harness:** use the DeepSeek API key already configured in dsh. If needed, run `dsh web`, open Settings → Models, configure DeepSeek and save. Obtain a key from [DeepSeek Platform](https://platform.deepseek.com/). Restart dsh by stopping `dsh web` with Ctrl+C and launching it again. Hyperthymesia does not require you to copy the key into its own configuration.

### 3. Check the connection and use it normally

In a new Terminal or PowerShell window, run the command for your agent:

```bash
hyperthymesia doctor --agent claude
hyperthymesia doctor --agent codex
hyperthymesia doctor --agent workbuddy
hyperthymesia doctor --agent qoder
hyperthymesia doctor --agent dsh
```

Run only the relevant line. The writer provider should match your agent; WorkBuddy reports `codebuddy`, its underlying runtime. `doctor` checks configuration, not the complete capture/write/recall chain. Also check the MCP connection and actual hook activity. See the [compatibility notes](docs/desktop-compat.md), currently maintained in Chinese.

Chat and work normally. Hooks record completed turns and code changes; background writing runs when enough material has accumulated or a supported lifecycle event triggers it. Memory is not necessarily saved immediately after each reply. To inspect what a project would receive:

```bash
hyperthymesia context /path/to/project
```

### WorkBuddy desktop usage notes

WorkBuddy 5.3.14 may not deliver the session-end event reliably on quit. Conversation material below the batch threshold may remain pending until you enter a chat again and session-start triggers background writing. Opening the home screen alone is insufficient; a question asked before writing finishes may miss that pending material. Already stored memories remain readable.

That version also ignores `disableAllHooks`. To disconnect Hyperthymesia, use its uninstall command and restart WorkBuddy.

### Optional operations

**Import earlier chats:**

```bash
hyperthymesia import --list
hyperthymesia import --agent claude --session SESSION_ID
```

Replace `claude` and `SESSION_ID` as needed. `--all --days 7` imports chats from the last seven days. Historical code changes cannot be reconstructed by this import.

**Try a single project:**

```bash
hyperthymesia install claude --project /path/to/project
```

Project installation supports `claude`, `codex`, `codebuddy`, `workbuddy` and `qoder`. dsh integration is profile-based and does not provide project-level installation isolation.

**Use a separate OpenAI-compatible API for background writing:** create `~/.hyperthymesia/config.toml` only if you want to override your agent's normal model access:

```toml
[writer]
provider = "openai"
model = "deepseek-chat"
base_url = "https://api.deepseek.com/v1"
api_key_env = "DEEPSEEK_API_KEY"
```

Put the actual key in the named environment variable, not in this file.

**Upgrade:** rerun the installation command for your agent. This replaces the executable and refreshes integration while retaining memories. It installs the latest published release, not unreleased source changes.

**Uninstall:** run `hyperthymesia uninstall claude`, substituting your agent's identifier. It removes Hyperthymesia's integration entries and preserves other settings. Memories remain on disk; deleting `~/.hyperthymesia/` permanently removes them.

### Windows configuration and troubleshooting

Qoder's user MCP configuration now shares `~/.qoder/settings.json` with hooks. Integration backs up files and migrates only Hyperthymesia's obsolete MCP entry. Windows CLI launches use the actual Node/JavaScript entrypoint, preserving multiline arguments; inherited Qoder SDK transport markers are removed without deleting authentication locations. Newer CLI versions are not automatically downgraded.

For a nonstandard WorkBuddy location, use `HYPERTHYMESIA_CODEBUDDY_CLI` to specify the actual bundled script before starting the host. `doctor --agent workbuddy --check-cli` (or `qoder`) checks startup without a model request, not account/quota availability. A lite bundle with no usable login path may still require your explicitly configured API; no automatic credential or paid-provider fallback is performed.

Use `HYPERTHYMESIA_HOME` for the memory directory. Executable extraction still uses `TEMP`/`TMP`; disk-full bootloader failures happen before Python code can run. Failed writes retain their input, OS locks release on process death, and interrupted turns are recovered only from unique, explicitly completed transcript records. Ambiguous turns remain pending and visible in `doctor`.

### Troubleshooting

- **Command not found:** reopen Terminal/PowerShell. If necessary, use `~/.local/bin/hyperthymesia` on macOS/Linux or `%USERPROFILE%\.hyperthymesia\bin\hyperthymesia.exe` on Windows (the latter is a Command Prompt path; in PowerShell use `$env:USERPROFILE`).
- **macOS blocks the executable:** open System Settings → Privacy & Security and choose Open Anyway if offered.
- **New information is missing:** inspect the capture/write logs and allow background writing to finish; a connected MCP server alone does not prove that hooks captured or saved the conversation.

### Command reference

| Command | Purpose |
|---|---|
| `install <agent> [--project PATH]` | Connect an agent; existing configuration is backed up |
| `uninstall <agent> [--project PATH]` | Remove integration while preserving unrelated settings |
| `doctor [--agent AGENT]` | Inspect the writer configuration and model |
| `context [PATH]` | Show the memory context for a directory |
| `write` | Manually process pending completed turns; normally automatic |
| `import --list` / `import --agent AGENT --session ID` | Import earlier chats |

### Resuming failed writes

Keep `state.db` and `logs/writer.log` when a write fails. After fixing the reported configuration or connection problem, run `hyperthymesia write` to resume the unfinished stage. Correct objects and facts are retained; the whole chat need not be imported again. An entry with unresolved source references remains pending. Processing completion does not certify that every useful fact was extracted correctly; inspect the saved context and correct mistakes in normal conversation.

### How background writing works

Writing runs in two steps. A batch (triggered at about 28,000 backlog tokens, capped at about 40,000 tokens, roughly 20 turns) is first extracted in up to three windows; turns are numbered, the model cites positions only, and the program copies the original text. Turns with nothing extracted are asked again individually. One organize step then compares candidates with related existing records: duplicates, corrections, merges, splits, and whether a new subject belongs to an existing object (only an object whose records the model was shown; otherwise a new object is created). Items that cannot be applied are held in `held_entries.jsonl` instead of failing the batch. Tune with `HYPERTHYMESIA_BACKLOG_TOKENS` and `HYPERTHYMESIA_BATCH_TOKENS`; `HYPERTHYMESIA_WRITER_MODE=single` restores the older single-call writer.

Reading: with many memories only a directory is injected; the agent calls `memory_read_objects`, optionally with `full=true` (full assistant suggestions) or `include_history=true` (superseded values). An unchanged directory is not resent.

For Codex, installation adds `direct_only_tool_namespaces = ["mcp__hyperthymesia"]` under `[features.code_mode]` and sets the global `tool_output_token_limit` and the memory tool's `output_token_limit` to 262144 (an existing global limit is kept), so memory reads reach the model untruncated. If your config already sets `features.code_mode`, it is left untouched and you are told to add the entry yourself.

### Writer model selection

Automatic selection checks quality, latency and available token statistics. Missing telemetry is marked unknown; it does not by itself reject a model or prove low cost. A saved courtesy offer (such as "I can draft the notice") is only a warning, not a rejection. Without usable acceptance data, at most four cheapest candidates are probed; when scoring rules change, saved probe replies are rescored locally without new requests. Redacted probe replies and reasons are in `logs/models.log`. `doctor --check-cli` checks the CLI version without model requests or cache refresh.

To select a model yourself, set `[writer] model = "YOUR_SUPPORTED_MODEL_ID"` in `config.toml`. Explicit selection bypasses automatic screening; it does not certify quality or change the provider. No automatic switch to another host or paid API is performed. Automatic CLI discovery skips unusable wrappers and continues searching; supported npm wrappers resolve to their actual JavaScript entrypoint.
