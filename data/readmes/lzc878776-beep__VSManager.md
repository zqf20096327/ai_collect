# VSManager · 多 VS 管理工具

VSManager 是一个 Windows 桌面工具（WinForms / .NET Framework 4.8），用于同时管理本机上多个 Visual Studio 实例及其中的 GitHub Copilot 对话。

## 功能

- **VS 实例总览**：自动发现正在运行的 Visual Studio，显示解决方案、调试状态与 Copilot 忙碌 / 空闲状态；一键布局到多块屏幕。
- **应用内 Copilot 对话**：VS 线程页实时查看回复（Markdown 渲染），保留停止 Copilot、打开对话和调试控制；不再显示底部输入栏，文字与附件从 AI 总控助手「直发」发布。
  发送后自动切回：发送（或关闭文档等操作）结束时，若目标 VS 抢到了前台，VSManager 会切回你原来所在的窗口（原窗口已关闭，例如临时弹窗，就切回 VSManager），并在之后约 6 秒内继续守护，处理 VS 延迟激活自己的情况；期间你一按键或点击鼠标就停止，最多切回 3 次，切回记录在发送日志中。
  Return after sending: when a send (or an operation such as closing documents) finishes and the target VS has taken the foreground, VSManager switches back to the window you were using (VSManager itself if that window is gone, e.g. a transient popup), and keeps guarding for about 6 seconds in case VS activates itself late; it stops as soon as you press a key or click, switches back at most 3 times, and records each switch in the send log.
  发送诊断：右键 VS →「发送诊断 / Send diagnostics」打开面板，逐条列出最近的发送，并按「排队 → 定位输入框 → 填入 → 提交 → 确认送达 → 恢复焦点」六步显示每一步是完成、等待、失败还是送达不确定，高亮出错的步骤并给出处理建议，可复制诊断或打开发送日志；发送日志每次发送也会多写一行「阶段 / Stages」。送达不确定（已提交但未确认、提交后异常等）时禁止盲目重发：AI 总控助手的 `retry_task` / `retry_task_with_info` 会被拒绝，需先用 `read_vs_chat` 核实目标对话、用 `read_send_diagnostics` 查看出错步骤；用户在任务清单手动重新排队时会弹出默认「否」的强提醒。诊断记录只保存在内存中（本次运行最近 100 次发送）。
  Send diagnostics: right-click a VS → "发送诊断 / Send diagnostics" to open a panel listing recent sends. Each send shows six steps, queue → locate input → fill → submit → confirm delivery → restore focus, marked done, waiting, failed or delivery uncertain; the failing step is highlighted with advice, and you can copy the diagnosis or open the send log, which also gets a "阶段 / Stages" line per send. When delivery is uncertain (submitted but unconfirmed, an error after submission, etc.) blind resending is forbidden: the AI assistant's `retry_task` / `retry_task_with_info` are refused until it checks the target chat with `read_vs_chat` and the failing step with `read_send_diagnostics`, and a manual requeue from the task list shows a strong warning whose default is "No". Diagnoses are kept in memory only (the latest 100 sends of the current run).
- **调试控制**：开始 / 停止 / 中断 / 重新启动调试，生成 / 重新生成，读取错误列表。
- **AI 总控助手**：接入任意 OpenAI 兼容接口（默认 DeepSeek），通过函数调用查看各 VS 状态、分派任务、等待结果。快捷按钮「🗂 关闭 .cs 标签页 / Close .cs tabs」一键关闭各 VS 中已打开的 .cs 标签页，有未保存修改的文件保留不关闭、不保存并列出。
  The "Close .cs tabs" quick button closes the open .cs tabs in every VS; files with unsaved changes stay open, are not saved, and are listed.
  工具按需加载（「属性 → AI 助手 → 按需加载工具组」，默认开启）：每轮只向模型提供核心工具（VS 状态、发布 / 等待任务、任务清单与重试接续、测试清单、解决方案开关等），屏幕布局、VSManager 自测与界面探针、代码 / 文件检查与截图、worktree、笔记、CAD 验证、MCP 管理等工具组只在本轮文字相关（关键词或提到工具名）、近 8 轮用过，或 AI 调用 `load_tools` 时才加入；未列出的工具仍可按名调用。普通一轮的工具定义约减少三分之二，请求更小、模型更专注；关闭后每轮提供全部工具。
  On-demand tools ("Properties → AI assistant → Load tool groups on demand", on by default): each round gives the model only the core tools (VS status, publishing / waiting for tasks, task list with retry and continuation, test checklists, opening / closing solutions…); the groups for screen layout, VSManager self-test and UI probes, code / file inspection and screenshots, worktrees, notes, CAD verification and MCP management join only when the round's text is related (keywords or a tool name), they were used in the last 8 rounds, or the AI calls `load_tools`. Unlisted tools can still be called by name. A plain round sends about two-thirds less tool definition text, so requests are smaller and the model stays focused; turning it off offers every tool each round.
- **MCP 外部工具**：可选挂载 MCP（Model Context Protocol）服务器（本地命令或 Streamable HTTP 地址），把其工具注册给 AI 总控助手；默认关闭，不预装任何服务器。
- **CAD 动作执行器**：独立的 ai.exe 按动作序列驱动调试启动的 CAD（打开图纸、执行命令、截图、抓日志等），结果回传给 AI 总控助手用于执行「待验证」项；每个项目一份适配包。目标项目也可嵌入 `sdk\VsmVerify.cs` 提供验证接口，由 ai.exe 经本机命名管道调用。
  Target projects can also embed `sdk\VsmVerify.cs` to expose a verification interface that ai.exe calls over a local named pipe.
  向 CAD 测试环境项目（CAD 插件项目）发布任务时，AI 总控助手会在任务文字中注明「不需要启动 CAD 自行测试，测试由 ai.agent 后续完成」，目标 VS 只负责编码、编译与单元测试。
  When publishing to a CAD test-environment (CAD plug-in) project, the AI assistant states in the task that the VS need not start CAD to test; ai.agent runs the CAD tests afterwards, and the VS only codes, builds and runs unit tests.
  用户不在场、无法回答提问时（通知驱动的轮次、自验证 / 自迭代循环、用户说过自己离开），AI 总控助手不停下来等待，而是根据上下文自己决策并把任务推进到完成，在回复中写明所做的决定；只有确实无法继续（缺少只有用户才有的信息、需要授权的不可逆操作、工具反复失败）时才停下，并在最终回复中说明需要用户提供什么。
  When the user is away and cannot answer (notice-driven rounds, self-verify / self-iteration loops, or the user said they are away), the AI assistant does not stop to wait; it decides from the context, drives the task to completion and states its decisions in the reply. It stops only when it truly cannot continue (information only the user has, an irreversible action needing authorization, tools failing repeatedly) and then says in the final reply what the user needs to provide.
- **执行计划缓存**：流程复杂（多步骤、跨重启、步骤间有依赖）时，AI 总控助手先用 `create_plan` 建立执行计划并持久化到 `%APPDATA%\VSManager\agent-plans.json`，每完成一步用 `update_plan_step` 更新，全部完成才 `complete_plan` 释放；进行中的计划常驻系统提示词。VSManager 重启（含自测重启）后新进程自动读回计划，发出「[执行计划恢复]」通知让 AI 从下一步接着做；自测重启时并入重启完成通知。简单请求不建计划。
  Execution plan cache: for complex flows (multi-step, across restarts, dependent steps) the AI assistant first creates a plan with `create_plan`, persisted in `%APPDATA%\VSManager\agent-plans.json`, updates each finished step with `update_plan_step` and releases it with `complete_plan` only when all are done; active plans stay in the system prompt. After a VSManager restart (including self-test restarts) the new process reads the plans back and sends a "[Plan resumed]" notice so the AI continues from the next step; for self-test restarts it joins the restart notice. Simple requests get no plan.
- **任务清单**：默认新发布 AI 任务保存后自动按编号调度；手动与恢复任务仍等待「开始流程 / Start」，可在属性改为全部自动。同时显示各 VS 中手动进行的 Copilot 对话。
- **任务归属与项目摘要**：任务题目自动补全为「项目名 · 事项」（项目名取解决方案名），在任务清单与通知中显示；任务通知、失败反馈与 send_task 结果末尾自动附上「[项目上下文]」（项目名、职责描述、该 VS 最近 3 条任务结果），多项目并行时 AI 总控助手不必从长对话中翻找归属。不改变排队与调度规则。在此基础上的会话层隔离（`AgentSessionIsolation`，默认开启）让 AI 总控助手的模型上下文按项目分开：某项目的通知与对话不会出现在其他项目的轮次中，避免结论、文件路径与错误信息互相串扰。
  Session-level isolation on top of this (`AgentSessionIsolation`, on by default) splits the AI assistant's model context per project: one project's notices and conversation never appear in another project's rounds, so conclusions, file paths and errors do not leak across projects.
- **解决方案登记与 VS 开关**：按常用名称（别名 / 同义词，支持模糊匹配）登记解决方案，AI 助手可据此打开 / 关闭 VS；目标 VS 未打开时任务自动暂存，获得自动启动资格或本次会话手动开始后，打开目标才会自动推送。
- **VS 会话记录与一键打开**：侧边栏 VS 列表上方「📌 记录 VS」记录当前打开的解决方案及主窗口与浮动窗格位置，「▶ 一键打开 VS」打开其中尚未打开的解决方案，就绪后按记录恢复布局（右键 / 托盘菜单与 AI 工具 `record_vs_session` / `open_vs_session` 同样可用）。
- **Agent 自循环反馈**：侧边栏「Agent 自循环 / Agent loop」区读取外部 Agent 评测脚本的运行目录（每次运行一个子目录，含 `result.json`、`cases.json`、`transcript.md`、`logs\`），以柱状条显示最近各次运行的通过率（绿＝全部通过、红＝有失败、灰＝无结果、黄＝运行中）；点击后主界面切换到问题汇总页（与 VS 对话、AI 总控助手、笔记本同一区域，点击左侧其他项即切回），顶部可切换两种视图：「汇总（不重复问题）」（默认）把不重复的问题汇总到一张大表，每个问题一行（编号 + 问题概述 + 简短结果（绿色「✓ 通过」/ 红色「✗ 失败」，曾有相反结果时附「· 曾失败 / · 曾通过」）+ 历次测试（按旧→新以 ✓ / ✗ 排列，并显示通过数 / 总数，如「✗✓✓✓ 3/4」）+ 首次 / 最近测试时间）；「按批次」列出测试过的全部问题，一个批次（一次评测运行）一条分割行并记录时间，批次按时间新→旧、批次内按问题编号排列（每行：编号 + 问题概述 + 本次结果 + 总体结果 + 时间 + 耗时；同一问题先失败、之后的测试通过即算通过；选中分割行显示该批次概况），选中某个问题即在下方显示它的全部测试记录（每次的具体提问、回答与未通过原因）。只读，有新结果时自动刷新；评测目录由 AI 技能读取代码自动选择：在已打开 / 已登记解决方案所在仓库中查找写出 `result.json` / `cases.json` 的评测脚本与代码，解析其中由环境变量拼出的运行目录，选择最近有运行的文件夹（启动或首次打开时未设置会自动查找，找不到时再手动选择文件夹），保存在 `AgentEvalDir`（以 `%LOCALAPPDATA%` 等环境变量形式保存）。读取全部运行，问题汇总不省略任何一条；AI 总控助手可用 `find_agent_eval_folder` 选择目录、`list_agent_eval_issues` 查看全部问题（可按 仍失败 / 未再运行 / 已恢复 筛选）。
- **语音**：可选接入豆包语音，任务完成后播报摘要（中文 / English 可选，AI 助手回复语言随之切换）；原 VS 输入栏的按住说话入口已移除。
- **Web 远程控制与 AI Skill**：在局域网内用手机浏览器操作（需访问令牌）；可把控制 API 安装为 Copilot CLI / Claude Code 等的 Skill（含 VS 截图）。
- **历史归档**：任务流水、助手对话、各 VS 对话与发送日志按天写入 JSONL，默认永久保留。
- **发布到 GitHub**：一键 git init / 提交 / 创建或关联远程仓库 / 推送，发布前自动做敏感信息自检。
- **内存监控**：按 VSManager / 各 VS 实例（含子进程）/ 共享组件分组显示工作集与私有字节，支持温和清理与超阈值提醒。
- **自动重启**：AI 助手出现异常、请求连续失败或长时间无响应时自动重建；可选进程看门狗在 VSManager 异常退出后自动拉起，并有防重启风暴限制。

## 输入栏 @ 指定 VS / Mention a target VS

- 在 AI 总控输入框输入 `@`：立即列出当前实例的 **编号、名称、职责摘要**，继续输入编号（可带 `#`）、名称或职责关键词筛选；↑/↓ 选择，Enter 确认，鼠标单击也可确认。候选列表打开时 Enter **只选择、不发送**；Esc 只关闭候选，不停止 AI。离开输入框、切换面板或调整窗口会关闭列表。VS 线程页不再提供输入栏。
  The manager assistant input shows current instances with **number, name and responsibility** immediately after `@`. Filter by number (optional `#`), name or responsibility; use ↑/↓ and Enter, or click. While suggestions are open, Enter **selects without sending** and Esc only dismisses suggestions without stopping AI. Leaving the input, switching panels or resizing dismisses the list. VS thread pages no longer have a composer.
- 确认后出现 `@[#编号 名称|会话标识]`，例如选择目标后再输入「修复编译错误」。保留完整标记，再按 Enter / 发送即可直接加入该实例的任务队列；标记本身不会发给 VS。**显式目标覆盖 AI 自动匹配**，总控不调用模型来重新选目标，即使没有配置模型或模型正在运行也能入队。普通输入没有提及时仍走原流程。
  Selection inserts `@[#number name|session-id]`. Keep the complete marker, add the task and press Enter / Send to enqueue directly; the marker is removed from the task body. **Explicit targeting overrides AI matching** without calling a model, even if no model is configured or it is busy. Inputs without mentions retain their previous flow.
- AI 总控输入栏的发送按钮旁还有 **「⚡ 直发 / Direct」**（快捷键 Ctrl+Enter，仅在输入中包含 @ 目标时可用）：按 @ 指定的目标直接发布任务，AI 只做简单润色让语句通顺，不补充内容、不提问；未配置模型或模型正在运行时按原文直接入队。
  The AI assistant input also has a **"⚡ 直发 / Direct"** button beside Send (Ctrl+Enter, enabled only when the input contains an @ target): it publishes straight to the @ target, and the AI only smooths the wording without adding content or asking questions; without a configured or idle model the text is enqueued as typed.
- **@小维**：候选列表末尾固定有「AI @小维」（AI 总控助手），选择后插入 `@[小维|标识]`，也可以直接输入 `@小维`。含 @小维 的消息明确交给 AI 总控助手按常规规则处理（回答问题或调用工具），即使同时 @ 了某个 VS 也不会直接入队，VS 提及只作为上下文；「⚡ 直发」仍以 VS 目标为准。需要已配置模型，AI 正在运行时保留草稿并提示。
  **@小维**: the candidate list always ends with "AI @小维" (the AI assistant); choosing it inserts `@[小维|id]`, or just type `@小维`. Messages containing @小维 go explicitly to the AI assistant under its normal rules (answer or use tools); even with a VS mention nothing is enqueued directly and the VS only serves as context. "⚡ Direct" still targets the VS. A configured model is required; while the AI is busy the draft is kept with a notice.
- 一条消息只能指定 **一个不同的 VS**。重复提及同一实例会去重；多个不同实例、未确认的 `@查询`、未知/修改过的标记或无正文（且无附件）都整条拒绝，不部分发布。无匹配时显示中英提示，保留草稿与附件。只有持久化成功才清空输入；重复提交相同目标、正文和附件复用活动任务。
  A message allows **one distinct VS**. Repeated mentions of that instance are deduplicated. Multiple distinct targets, unconfirmed queries, unknown/edited markers, or no body without attachments reject the whole message. No-match and save failures retain text and attachments. Input clears only after persistence; identical active tasks are reused.
- 编号只是显示，目标实际绑定 **进程 ID、启动时间和解决方案/项目**。切换左侧选中项、实例重排或重名不会改目标；同一解决方案的两个 VS 也不会互相替代。实例关闭、重启或切换解决方案后拒绝发送，已排队任务在调度时失败并说明原因，请重新选择后发布。发送边界还核验真实进程和 DTE；无法核验时不会强行发送。
  Numbers are labels; routing pins **process ID, start time and solution/project**. Sidebar selection, reordering and duplicate names cannot retarget a task, including two VS processes opening the same solution. Closed/restarted/changed targets are rejected; queued tasks fail at dispatch with an explanation. Select again and resubmit. The send boundary also verifies the live process and DTE; unverifiable targets are not force-sent.
- 标记在本次应用会话内可复制；会话标识不要手改。应用重启后，旧输入标记需重新选择（已保存任务仍保留精确目标元数据）。图片与总控附件随提及任务一起持久化、排队；采用现有发布、状态、完成通知和手动对话保护，来源记为「用户」。默认仍需任务清单 **Start**，不会伪装为自动 AI 任务；用户已启用「全部自动」时沿用该设置。
  Markers can be copied within this application session. Do not edit their identifiers; after restarting the app, select input mentions again. Persisted tasks retain exact target metadata. Images and agent attachments join the normal persisted queue, dispatch, status, completion notification and manual-chat protection flow as **user** tasks. The default still requires **Start**; mentions do not masquerade as AI tasks. Explicit all-automatic settings remain respected.
- 语法边界：行首、空白/标点后及中文句内的 `@` 可提及；拉丁单词中的 `@`、邮箱、`@scope/package`、反引号代码以及常见 C# 声明（例如 `var @class`）保留为普通文字。其他含 `@` 的代码请放在反引号中，或用 `@@` 防止识别；普通文字路径不删改字符（包括 `@@`）。筛选词不含空格；名称有空格时可输入其中一段再选择。此功能仅在 AI 总控输入框启用，Web 远程接口不解析提及。
  Syntax: `@` at a line start, after whitespace/punctuation, or within Chinese text can start a mention. Latin-word `@`, emails, `@scope/package`, backtick code and common C# declarations (such as `var @class`) stay literal. Put other `@` code in backticks or use `@@` to prevent recognition; literal input is not rewritten, including `@@`. Queries cannot contain spaces; filter a fragment of a spaced name. Only the manager assistant input interprets mentions, not Web remote requests.

## Worktree 工作线 / Worktree lanes

- 默认新发布 AI 开发任务自动启动，本会话自动任务完成新产生的合并屏障继承资格；旧恢复合并仍需 Start（或显式全部自动），不会因收到完成回调而擅自合并。已有 VS 中的 Copilot 不会被停止或重发。
  Newly submitted AI development tasks auto-start by default; barriers newly generated by their completion inherit eligibility. Restored integrations still require **Start** (or explicit all-automatic mode); callbacks alone never authorize them. Existing Copilot work is not stopped or resent.
- 显式告诉 AI 助手「为已登记项目创建 worktree 工作线，名字为 feature1」，使用 `create_worktree(project, name)`；`list_worktrees` 查询工作线，之后将返回的**精确别名**用于 `send_task`。普通项目任务不受影响。
  Explicitly request a worktree lane with `create_worktree(project, name)`, inspect it with `list_worktrees`, then use its **exact returned alias** with `send_task`. Ordinary project tasks are unchanged.
- 需要标准安装位置的 Git for Windows（`Program Files\Git` 或 `%LOCALAPPDATA%\Programs\Git`）、已提交且干净的主仓库，以及在「属性 → AI 文件授权」授权仓库及其共同父目录。不会从仓库或 PATH 查找可执行程序。工作目录命名为 `项目目录.worktree.名字`，分支为 `task/名字`，从创建时捕获的主项目当前分支建立；自动登记、打开对应 VS，未就绪的任务暂存后发送到该工作树，不发送到同名主项目。
  Requires Git for Windows in a standard install location (`Program Files\Git` or `%LOCALAPPDATA%\Programs\Git`), a clean committed main checkout, and existing file grants for the repository and its parent. Repository/PATH executables are not used. The sibling `Project.worktree.name` uses `task/name` based on the captured current main branch. It is registered and opened in its own VS; queued tasks wait for that exact solution, not a similarly named main project.
- 每个开发任务开始及成功回执后检查工作树干净；Copilot 只提交本任务修改，不自动提交用户的未提交文件。每 **5 个成功开发任务**持久化插入一个可见「本地推送/合并」任务，优先于该工作线后续开发任务；合并任务不计数。失败、取消和重复回执不增加计数，重启不重复生成批次。
  Development starts and finishes clean; Copilot commits only its own task changes, never unrelated user edits. Every **five successful development tasks** inserts a durable visible local-integration task ahead of subsequent lane work. Integration tasks do not count; failures, cancellations, duplicate receipts and restarts do not inflate batches.
- 合并先在工作树吸收主分支，冲突交给该工作树的 Copilot；验证冲突解决、提交、干净状态和祖先关系后，主项目仅 `--ff-only` 快进，不切换分支、不远程 push、不强推、不 reset/clean。主项目脏、分支切换、权限撤销、保存失败或 Git 错误都会失败并保留屏障；处理后在任务清单**重试原合并任务**。取消合并也不会放行后续任务。工作线历史保留作计数账本，不可删除或按历史上限裁剪（可用界面隐藏）。
  Merge main into the worktree first; Copilot resolves conflicts there. Only after clean committed resolution and ancestry checks does the main checkout fast-forward (`--ff-only`), with no branch switching, remote push, force push, reset or clean. Dirty main, switched branches, revoked grants, persistence failures and Git errors retain the barrier; resolve the cause and **retry the original integration task**. Cancelling does not release the lane. Workflow history is retained as the durable ledger, exempt from removal/trimming (UI hiding is available).
- 同一主仓库的自动合并串行执行；不要同时在外部 Git/VS 中修改主仓库。暂不支持子模块、符号链接、配置 include、自定义 filter/merge driver 或 worktreeConfig；Git hooks 不运行。少于 5 个成功任务时不会自动合并；当前不提供自动删除工作树或远程推送功能。
  Automatic integrations sharing a main checkout are serialized; do not modify that checkout concurrently through external Git/VS. Submodules, symlinks, config includes, custom filters/merge drivers and worktreeConfig are unsupported; Git hooks are disabled. Fewer than five successes do not auto-integrate. Automatic worktree removal and remote pushing are not provided.

## 运行环境

- Windows 10 / 11
- Visual Studio 2022 或更高版本，并安装 GitHub Copilot
- .NET Framework 4.8
- [Microsoft Edge WebView2 Runtime](https://developer.microsoft.com/microsoft-edge/webview2/)（Windows 11 已自带）

## 构建与运行

```powershell
git clone https://github.com/<owner>/VSManager.git
cd VSManager
dotnet build VSManager.slnx -c Release
.\src\VSManager\bin\Release\net48\VSManager.exe
```

`<owner>` 替换为仓库所有者；默认分支为 `main`，开发中的内容在 `develop`（见[分支策略](#分支策略)）。

也可以直接用 Visual Studio 打开根目录的 `VSManager.slnx`（项目文件位于 `src\VSManager\VSManager.csproj`）生成并运行。

运行单元测试（MSTest，测试数据全部写入系统临时目录，不会读写 %APPDATA%\VSManager 中的真实数据）：

```powershell
dotnet test VSManager.slnx
```

测试分为三类（见 `tests\VSManager.Tests\TestKind.cs`），`dotnet test` 默认只运行「完全不弹窗」类，不会显示窗口、抢占焦点、使用剪贴板或启动命令行进程，运行期间可以正常在其他窗口输入：

| 范围 `TestScope` | 内容 | 运行方式 |
|---|---|---|
| `NoPopup`（默认） | 完全不弹窗的测试（约 960 个），日常修改后运行这一类即可 | `.\tests\run-tests.ps1` 或 `dotnet test VSManager.slnx` |
| `UI` | 显示窗口 / 抢焦点 / 使用剪贴板的界面测试，运行期间请勿在其他窗口输入 | `.\tests\run-tests.ps1 -Scope UI` |
| `Console` | 启动 git、cmd、PowerShell 等命令行进程的测试（需要 git 在 PATH 中） | `.\tests\run-tests.ps1 -Scope Console` |
| `All` | 全部测试（发布前或改动界面 / 命令行相关代码时） | `.\tests\run-tests.ps1 -Scope All` 或 `dotnet test VSManager.slnx -p:TestScope=All` |

脚本还支持 `-Filter`（与分类条件同时生效）与 `-NoBuild`；输出目录默认在测试项目 `bin\run-tests\` 下，避免与正在运行的 VSManager 争用文件。直接使用 `dotnet test --filter` 时以该筛选条件为准，不再附加分类条件。新增测试若会弹窗 / 抢焦点 / 使用剪贴板，请标注 `[TestCategory(TestKind.Ui)]`；若启动命令行进程，请标注 `[TestCategory(TestKind.Console)]`。

若本机 NuGet 配置中有不可用的源导致还原失败，可先执行 `dotnet restore VSManager.slnx --source https://api.nuget.org/v3/index.json`。

## 目录结构

```text
VSManager/
├─ VSManager.slnx              解决方案
├─ README.md / LICENSE / .gitignore / .gitattributes
├─ CONTRIBUTING.md             贡献指南（分支策略、提交规范、自检）
├─ CHANGELOG.md                更新日志
├─ settings.example.json       配置示例（真实配置在 %APPDATA%\VSManager\，不入库）
├─ src/
│  └─ VSManager/               主程序项目（WinForms，.NET Framework 4.8）
│     ├─ VSManager.csproj
│     ├─ Program.cs / app.manifest
│     ├─ Assets/               图标与嵌入资源（Web 页面、Copilot Skill）
│     │  ├─ app.ico
│     │  ├─ Web/               remote.html、transcript.html
│     │  └─ Skill/             SKILL.md、vsm.ps1
│     ├─ Core/                 领域层：不依赖界面与 Win32
│     │  ├─ Models/            数据模型（外部对话、图片附件、Copilot 状态）
│     │  ├─ Tasks/             任务模型、任务状态机、发送重试判定、任务清单
│     │  └─ TextUtil.cs        通用文本工具
│     ├─ Infrastructure/       基础设施层
│     │  ├─ Config/            配置读写（AppSettings）、数据目录（AppPaths）
│     │  ├─ Http/              AI 接口客户端工厂、请求体策略
│     │  ├─ IO/                文件系统抽象、原子写入
│     │  ├─ Logging/           统一日志入口（AppLog）、发送日志
│     │  ├─ Storage/           tasks.json 存储
│     │  ├─ Win32/             Win32 互操作、内存裁剪
│     │  └─ QrCode.cs          二维码
│     ├─ Services/             服务层
│     │  ├─ Abstractions/      外部依赖接口（VS 操作、Copilot 通道、语音）
│     │  ├─ Agent/             AI 总控助手、提示词、对话记录
│     │  ├─ Publish/           发布到 GitHub
│     │  ├─ Remote/            局域网网页遥控、Skill 安装
│     │  ├─ Storage/           历史归档
│     │  ├─ Tasks/             任务调度器（发布、重试、完成、失败）
│     │  ├─ VisualStudio/      VS 实例、Copilot 对话 / 监控、代码扫描、内存监控
│     │  └─ Voice/             豆包语音合成与识别
│     └─ UI/                   界面层：主窗口、主题、通用控件
│        ├─ Forms/             设置、发布、对话记录、内存等窗口
│        └─ Panels/            Copilot 对话、AI 助手、任务清单面板
└─ tests/
   └─ VSManager.Tests/         单元测试（MSTest）
```

所有源码仍使用同一个命名空间 `VSManager`，目录只用于按职责组织文件。构建输出（`bin/`、`obj/`）与测试结果（`TestResults/`）已被 `.gitignore` 排除。

### 分层架构

- **Core（领域层）**：任务模型 `QueuedTask`、状态机 `TaskStateMachine`（排队 → 发送中 → 执行中 → 已完成 / 待验证 / 失败 / 已取消；「待验证」`unverified` 表示改动已完成，但尚未在运行中的程序里实际验证，或需要用户手动测试、运行或确认（旧版「已完成（待用户验证）」记录读取时自动迁移为待验证），在接续等级中按「待确认」处理（「已完成」「待确认」两挡会暂停后续），可右键「标记为已验证」或在任务清单旁的「测试清单」勾选（`TaskTestChecklist`，每个任务一个测试条目，列出需实测的内容，勾选即完成；与主对话栏之间可拖动分隔条调整宽度并自动保存）转为已完成；旧版本读取到该状态会视为无法识别并暂停）、发送重试判定 `SendRetryPolicy`、任务清单 `TaskQueue`（编号分配、历史裁剪、归档流水）。只依赖接口 `ITaskStore`、`ITaskArchiveSink` 与可替换时钟，可直接单元测试。
- **Services（服务层）**：VS 管理、Copilot 消息发送、AI 助手、语音、归档、发布。`TaskDispatcher` 负责任务调度，通过 `ITaskDispatchHost` 与主窗口交互；外部依赖通过 `IVsOperations`、`ICopilotChannel`、`IVoiceService`、`IAiClientFactory` 抽象。
- **Infrastructure（基础设施层）**：Win32 封装、配置与数据目录、文件系统抽象 `IFileSystem` 与原子写入 `AtomicFile`、统一日志 `AppLog`（含未处理异常记录到 crash.log）、HTTP 客户端创建。
- **UI（界面层）**：窗体与控件，只负责展示与交互，业务动作委托给服务层。

## 配置

首次运行时会自动生成配置文件 `%APPDATA%\VSManager\settings.json`，所有选项都可以在主窗口「⚙ 属性」中修改。配置缺失、字段不全或已损坏时会使用默认值（损坏的文件会另存为 `settings.json.corrupt-*`），不会导致程序崩溃。

各字段及默认值见 [`settings.example.json`](settings.example.json)。常用的有：

| 配置项 | 说明 | 默认值 |
|---|---|---|
| `AgentEndpoint` / `AgentModel` | AI 助手接口地址与模型（OpenAI 兼容，需支持函数调用） | DeepSeek |
| `AgentKeyProtected` | AI 助手 API Key（DPAPI 加密，仅本机当前用户可解密） | 空 |
| `VoiceKeyProtected` | 豆包语音 API Key（DPAPI 加密） | 空 |
| `VoiceLanguage` | 语音语言：`zh` 中文 / `en` English；同时决定播报提示词、音色与 AI 总控助手的回复语言，切换后立即生效 | `zh` |
| `VoiceSpeakerEn` | 英文播报的音色 ID（seed-tts-*）或声音描述（seed-audio-*）；不可用时自动回退到默认音色 `zh_female_vv_uranus_bigtts` 并提示 | 英文声音描述 |
| `AgentMax*` | AI 额度：工具返回、单条消息、任务文本、历史消息等的单次上限 | 见示例 |
| `WebEnabled` / `WebPort` / `WebToken` | Web 远程控制开关、端口、访问令牌（为空时自动生成） | 关闭 / 8765 |
| `ArchiveEnabled` / `ArchiveRoot` / `ArchiveRetentionDays` | 历史归档开关、根目录（支持 `%环境变量%`）、保留天数（0 表示永久保留） | 开启 / 见下 / 0 |
| `PublishRepoPath` / `PublishOwner` / `PublishRepoName` / `PublishVisibility` / `PublishBranch` | 发布到 GitHub：本地目录（空＝自动查找）、所有者（空＝Token 用户）、仓库名、可见性、默认分支 | 空 / 空 / VSManager / public / main |
| `PublishAuthorName` / `PublishAuthorEmail` | 提交作者与邮箱（邮箱为空时使用 GitHub noreply 地址） | VSManager contributors / 空 |
| `GitHubTokenProtected` | GitHub Token（DPAPI 加密） | 空 |

<details>
<summary>全部配置项与默认值（点击展开）</summary>

| 分组 | 配置项 | 默认值 | 说明 |
|---|---|---|---|
| 窗口与布局 | `MainScreen` / `ToolScreen` | 空 | 主界面 / 工具窗口所在屏幕（空＝自动） |
| | `Layout` | `上下` | 工具窗口布局方式 |
| | `ActivateMoveMain` / `ActivateMoveTools` | true / false | 激活 VS 时是否移动主界面 / 工具窗口 |
| | `TopMost` / `MinimizeToTray` / `Hotkeys` | false / true / true | 置顶、关闭到托盘（最小化保留任务栏图标）、全局热键 |
| | `ClickToActivate` | false | 单击列表即激活 VS |
| | `SidebarWidth` / `AgentHeight` / `TaskPanelCollapsed` | 0 / 0 / false | 界面尺寸记忆（0＝默认） |
| | `AgentEvalDir` / `AgentEvalCollapsed` | 空 / false | Agent 自循环反馈读取的评测运行目录（可含环境变量）与侧边栏区是否折叠 / Agent self-loop run folder and collapsed state |
| | `TaskListGroupByVs` / `TaskListGroupSort` / `TaskListCollapsedGroups` | true / `activity` / 空 | 任务清单分组、组排序（`activity` / `number` / `manual`）、折叠状态，见[任务清单分组](#任务清单分组) / Task grouping, group ordering and collapsed state |
| | `AutoStartAiTasks` / `AutoStartAllTasks` | true / false | 默认新发布 AI 自动；全部模式优先且包含恢复任务。关闭只影响后续入队 / Newly submitted AI automatic by default; all mode overrides and includes restored tasks. Disabling affects later admissions |
| | `TaskListManualOrder` / `TaskListItemOrder` / `TaskListGroupOrder` | false / 空 / 空 | 手动条目显示排序开关、条目及分组顺序；不影响调度 / Manual entry display ordering and saved entry/group order; dispatch unchanged |
| Copilot 监听与发送 | `MonitorCopilot` / `PollMs` | true / 1500 | 监听 Copilot 状态及轮询间隔（毫秒） |
| | `WaitForManualChat` / `ManualChatWaitTimeoutSeconds` | true / 300 | 礼让目标手动对话；10–86400 秒，超时只提醒并继续等待 / Yield to target manual chat; 10–86400 seconds, timeout warns and keeps waiting |
| | `Sound` / `Popup` | true / true | 完成时提示音、托盘气泡 |
| | `TaskPopups` / `PopupMutedUntil` | true / 无 | 任务与完成弹窗总开关；弹窗上的 🔕 可静音 30 分钟、2 小时、今天，或直接关闭（在「属性 → Copilot 对话」中恢复）；同时最多显示 3 个弹窗 |
| | `CopilotPaneKeyword` / `BusyButtonIds` | `Copilot` / `CancelButton` | 识别 Copilot 窗格与「忙碌」按钮 |
| | `BackgroundSend` / `BackgroundSync` / `AutoOpenChat` | true / true / true | 后台发送、后台同步对话、自动打开对话窗格 |
| | `RestoreCopilotPane` / `ShowChatSteps` | true / true | 窗格被切走时自动切回、显示对话步骤 |
| | `AutoOpenCopilotPane` | true | 发送前 / 手动打开时，若对话窗格缺失、被隐藏或停留在历史记录，自动打开到当前会话 |
| | `SendConfirmTimeoutSeconds` / `SendAutoRetry` / `SendRetryCount` | 10 / true / 1 | 写入 Copilot 输入框后的确认超时（秒，2–120）、粘贴未确认或未找到输入框时是否自动重试及粘贴重试次数（0–5） |
| | `SendLocateTimeoutSeconds` / `SendLocateRetryCount` | 6 / 1 | 每轮定位 Copilot 输入框的轮询超时（秒，1–60）、未找到时重新打开窗格并重试的次数（0–5，`SendAutoRetry=false` 时不重试） |
| | `CloseVsDocumentsBeforeSend` / `CloseVsDocumentsThreshold` | false / 10 | 显式开启后，仅在文档标签数量严格超过阈值（0–1000）时清理已保存文档；未保存、未知状态与调试会话跳过 |
| | `RecordCompletedTasksInNotebook` | true | 任务成功完成后写入笔记本：按完成日期自动建立「yyyy.M.d 任务记录」页面，页面正文即当天清单，逐条列出时间与题目（检测到的手动对话也会记录并标注「手动对话」），点击进入详情子页面（任务内容或提问、VS、时间、完整回复）；仅保存在本地笔记数据库 `%APPDATA%\VSManager\Notebooks\notebook.db`（SQLite；文件夹与笔记合并为可含子页面的页面，旧 `.md` 首次启动时一次性导入并保留作备份，可「导出 Markdown」） |
| | `SaveAndCloseDocumentsAfterTask` | true | 兼容旧字段名；现在仅在 AI 任务已完成或待验证后、同目标下一任务发布前关闭已保存的 `.cs` 标签页，绝不自动保存；未保存文件保留并提示文件名，其他类型不动，调试或状态未知时跳过并提示；手动任务与失败任务不触发 |
| 解决方案登记 | `SolutionCloseConfirm` | true | AI 关闭 VS 前总是弹窗确认（关闭时仍会检查未保存修改） |
| | `SolutionOpenWaitSeconds` | 90 | AI 打开解决方案后等待 VS 出现的最长时间（秒，10–600） |
| | `PendingVsSettleSeconds` | 20 | 暂存任务在目标 VS 出现后再等待的秒数，让解决方案与 Copilot 加载完成（0–300） |
| | `PendingVsNotify` | true | 任务暂存 / 自动推送、自动启动与完成提示（语音需另行开启）/ Parked, pushed, automatic start and completion notices; voice requires separate opt-in |
| | `WatchConversations` / `ExternalRestoreLimit` / `ExternalRestoreHours` | true / 50 / 24 | 监听各 VS 中的手动对话及启动时恢复的数量与时间范围 |
| | `Aliases` / `VsNotes` | [] / [] | VS 别名与职责描述 |
| AI 总控助手 | `AgentEnabled` | true | 启用 AI 助手 |
| | `AgentEndpoint` / `AgentModel` | `https://api.deepseek.com` / `deepseek-flash` | OpenAI 兼容接口与模型 |
| | `AgentKeyProtected` | 空 | API Key（DPAPI 加密；也可用 `VSMANAGER_AGENT_API_KEY`） |
| | `AgentInstructions` / `AgentConfirm` / `AgentAutoFollowUp` | 空 / false / true | 自定义要求、执行前确认、任务完成后自动跟进；也可在笔记本根目录的「AI 助手补充提示词」页面中写补充要求，每次开始新对话时读取（点「新对话」使修改生效） |
| | `AgentSessionIsolation` | true | 会话层隔离：AI 总控助手的模型上下文按项目（解决方案名）分开。任务通知归属其项目；用户消息恰好提到一个项目（项目名、VS 名或登记别名）时归属该项目，否则为全局。项目轮只看到全局对话与本项目对话，全局轮只看到全局对话和各项目最近结论摘要；归属随对话记录保存，重开后接续。界面对话仍是一条，「新对话」一并清空 |
| | `NoteAgentDock` / `NoteAgentPercent` / `NoteAgentFloatBounds` | right / 50 / 空 | 笔记本界面的「笔记 AI 助手」：默认与笔记本各占半屏；拖动其标题栏可停靠到右侧 / 左侧（侧边栏停靠）或底部，拖到中间变为浮动窗口（浮动窗口拖回边缘可重新停靠，关闭则回到上次停靠位置），也可点标题栏按钮 ◧ ◨ ⬓ ⧉ 切换；位置、比例与浮动窗口大小自动保存。它有独立对话，与总控助手共用同一套笔记本技能（`read_current_note` / `list_notes` / `read_note` / `create_note` / `append_to_note` / `update_note` / `format_note_card` / `add_note_card` / `add_note_card_styles`，写入遵守「操作前确认」），不操作 VS；点「📥 插入到笔记」把最新回复写入当前笔记（光标处或末尾）。关闭 `AgentEnabled` 时一并隐藏 |
| | `AgentIncludeSolutionRoots` / `AgentFileRoots` | true / [] | 默认仅授权已登记解决方案目录；额外根目录必须在「AI 文件授权」中应用确认，或由用户编辑本机配置；两者都为空时拒绝全部访问 |
| | `McpEnabled` / `McpServersJson` | false / "" | 是否为 AI 总控助手挂载 MCP 服务器及其配置 JSON；只在「属性 → MCP 服务器」中由用户修改，AI 不能更改 |
| | `AgentPowerShellEnabled` | false | 兼容保留字段；AI 任意脚本入口停用，旧配置设为 true 也不能绕过文件白名单 |
| | `AgentMaxToolText` / `AgentMaxMessageText` / `AgentMaxTaskText` | 120000 / 30000 / 12000 | 单次文本上限（字符） |
| | `AgentMaxOutputTokens` / `AgentMaxHistory` / `AgentMaxIterations` | 0 / 800 / 320 | 输出上限（0＝模型默认）、历史条数、单轮工具调用次数 |
| | `AgentMaxFileLines` / `AgentMaxReadCount` | 4000 / 400 | 读取文件行数、读取对话条数上限 |
| | `AgentChatKeepDays` / `AgentChatMaxRecords` | 30 / 2000 | 对话记录保留天数与条数（0＝不限） |
| 自动重启 | `AgentAutoRestart` / `AgentHangTimeoutSeconds` / `AgentFailureThreshold` | true / 120 / 3 | 见[自动重启](#自动重启) |
| | `ProcessWatchdogEnabled` | false | 进程看门狗 |
| | `AutoRestartMaxCount` / `AutoRestartWindowMinutes` | 3 / 5 | 防重启风暴 |
| 任务清单 | `TaskHistoryLimit` / `TaskNextId` | 0 / 自动 | 历史条数上限（0＝全部保留）、下一个任务编号 |
| | `AutoHideResentFailedTasks` / `AutoHideResentFailedNotify` | true / true | 同一任务重新发布（重新排队）时只在界面隐藏原失败条目、隐藏时是否弹出通知并播报；隐藏记录在 `HiddenResentTasks`（默认 []，最多 2000 条），`tasks.json` 与归档不变 |
| 语音 | `VoiceAnnounce` / `VoiceAiSummary` / `VoiceTranslate` / `VoiceIncludeName` | true / true / true / true | 完成播报、AI 摘要、按语言翻译、播报 VS 名称 |
| | `VoiceLanguage` / `VoiceResource` | `zh` / `seed-audio-1.0` | 语音语言与资源 |
| | `VoiceSpeaker` / `VoiceSpeakerEn` | 内置中文 / 英文声音描述 | 音色 |
| | `AsrEnabled` / `AsrResource` | true / `volc.seedasr.sauc.duration` | 旧语音输入配置，仅保留兼容；输入入口及设置控件已移除 |
| | `VoiceKeyProtected` | 空 | 豆包语音 API Key（DPAPI 加密；也可用 `VSMANAGER_DOUBAO_API_KEY`） |
| Web 远程 | `WebEnabled` / `WebPort` / `WebToken` | false / 8765 / 空（自动生成） | 局域网远程控制 |
| 归档 | `ArchiveEnabled` / `ArchiveRoot` / `ArchiveRetentionDays` | true / 空 / 0 | 历史归档 |
| 内存 | `VsMemoryAutoEnabled` / `VsMemoryThresholdMB` / `VsMemoryAutoClean` | false / 6144 / false | 见[内存监控](#内存监控) |
| 定期内存清理 | `AutoTrimVsMemory` / `AutoTrimIntervalMinutes` / `AutoTrimThresholdMB` | false / 30（5–1440）/ 0（不限制） | 见[内存监控](#内存监控) |
| AI 助手附件 | `AttachmentMaxFileMB` / `AttachmentMaxCount` | 10（1–100）/ 5（1–20） | 单个附件大小上限、每条消息附件数量上限 |
| | `AttachmentKeepDays` / `AttachmentInlineMaxChars` | 30（0 = 不限制）/ 20000 | 附件保留天数；文本附件内联到任务正文的字数上限，见[AI 助手附件](#ai-助手附件) |
| 发布 | `PublishRepoPath` / `PublishOwner` / `PublishRepoName` | 空 / 空 / `VSManager` | 本地目录、所有者、仓库名 |
| | `PublishVisibility` / `PublishBranch` | `public` / `main` | 可见性、默认分支 |
| | `PublishAuthorName` / `PublishAuthorEmail` | `VSManager contributors` / 空（noreply） | 提交作者 |
| | `GitHubTokenProtected` | 空 | GitHub Token（DPAPI 加密；也可用 `VSMANAGER_GITHUB_TOKEN`） |

</details>

### 环境变量

API Key 不要写进任何需要提交的文件。可以在「属性」中填写（加密保存在本机），也可以用环境变量提供：

| 环境变量 | 作用 |
|---|---|
| `VSMANAGER_AGENT_API_KEY` | 「属性」中未填写时使用的 AI 助手 API Key |
| `VSMANAGER_DOUBAO_API_KEY` | 「属性」中未填写时使用的豆包语音 API Key |
| `VSMANAGER_ARCHIVE_ROOT` | `ArchiveRoot` 为空时使用的归档根目录 |
| `VSMANAGER_GITHUB_TOKEN` | 「发布到 GitHub」中未填写 Token 时使用 |

未设置 `ArchiveRoot` 与 `VSMANAGER_ARCHIVE_ROOT` 时，归档写入 `%APPDATA%\VSManager\archive`。配置的目录不可用（磁盘不存在、无写入权限）时会自动回退到该目录，并在界面上提示。

如需把本机归档放到自定义目录（例如容量更大的数据盘），设置用户级环境变量后重启 VSManager 即可（也可以直接在「属性 → 归档」中修改）：

```powershell
setx VSMANAGER_ARCHIVE_ROOT "%USERPROFILE%\Documents\VSManagerArchive"
```

### 本地数据位置

| 路径 | 内容 |
|---|---|
| `%APPDATA%\VSManager\settings.json` | 配置（含加密的 Key 与 Web 令牌） |
| `%APPDATA%\VSManager\tasks.json` | 任务清单 |
| `%APPDATA%\VSManager\solutions.json` | 解决方案登记表（含本机路径，仅存本机） |
| `%APPDATA%\VSManager\vs-session.json` | 「📌 记录 VS」的 VS 会话记录（解决方案路径与窗口位置，仅存本机） |
| `%APPDATA%\VSManager\agent-chat.jsonl` | AI 助手对话记录（每行一条 JSON，仅存本机；每条记有写入它的 VSManager 进程 PID 与启动时间，AI 助手面板与「对话记录」窗口可用进程下拉框只看某个进程或「全部进程」，助手消息的「AI 助手」标题后显示进程名称，如「AI 助手 · VSManager · PID 1234」） |
| `%APPDATA%\VSManager\logs\` | 程序日志 |
| `%APPDATA%\VSManager\publish-scan-terms.txt` | 发布自检的自定义词表 |
| `<ArchiveRoot>\tasks\`、`chat\`、`logs\` | 历史归档 |

以上文件都已写入 `.gitignore`，请勿提交；发布自检也会拦下这些本机数据文件。

### AI 助手对话记录

点击主窗口顶部的「📜 对话记录」打开历史窗口，可按关键词（或「#任务编号」）搜索、按日期筛选、切换正序 / 倒序，并可显示工具调用步骤。重开 VSManager 时，主界面的 AI 对话区与模型上下文会自动接续上次对话（从最近一次「＋ 新对话」之后的记录恢复；工具调用细节只显示、不再发给模型，仅本机展示的通知不进上下文），只有点「＋ 新对话」才重新开始；完整历史在该窗口中查看。每条记录包含时间、角色（user / assistant / notice）、文本以及关联的任务编号；写入时逐条追加并立即刷盘。容量由「属性 → AI 总控助手 → 对话记录」中的 `AgentChatKeepDays`（默认 30 天）与 `AgentChatMaxRecords`（默认 2000 条）控制，超出时只裁剪该文件中最旧的记录，不影响任务清单与归档。

### AI 授权文件工具

在「属性 → AI 文件授权」配置根目录白名单。默认只纳入已登记解决方案的父目录，不因某个 VS 正在运行而自动授权；额外目录每行一条，支持环境变量，必须点击「应用授权目录」并确认后生效。也可编辑本机 `settings.json` 的 `AgentIncludeSolutionRoots` 与 `AgentFileRoots`。禁用登记目录且额外列表为空时拒绝全部文件访问；模型不能自行更改授权。允许读取的内容可能发送给配置的 AI 服务。

| 工具 | 参数与默认值 | 返回内容 |
|---|---|---|
| `find_files` | `directory`；`pattern="*"`、`recursive=true`、`maxDepth=3`、`maxResults=100` | 文件名通配符（`*`、`?`）匹配及元数据 |
| `search_file_contents` | `directory`、`keyword`；`filePattern="*"`、`recursive=true`、`maxDepth=3`、`maxResults=100`、`maxFileBytes=1048576` | 忽略大小写的字面关键词匹配，含相对路径、行号与打码片段；先脱敏再匹配，不支持正则 |
| `read_file` | `path`；`startLine=1`、`maxLines=200` | 带行号的打码文本与 `nextStartLine`；0 表示没有后续行 |
| `list_directory` | `directory`；`maxResults=200` | 直接子项的类型、文件字节数和 UTC 修改时间；目录大小不递归计算 |

共同硬限制：只接受不超过 240 字符的完整本机路径；深度最多 8（根目录为 0）、最多 200 条结果、5,000 个遍历条目、5 秒协作式预算和 16,000 个输出字符。读取单文件最多 1 MiB、单次最多 500 行，且服从用户设置的更低行数/字符额度。只解码 UTF-8 或带 BOM 的 UTF-16；读取时单行最多 2,048 字符，搜索片段单行最多 1,024 字符，更低字符额度可能进一步缩短。超长行会明确标记截断，但其省略部分不能通过下一行续读。系统 I/O 调用本身不能强制中止。

目录遍历跳过 `bin`、`obj`、`node_modules`、`.git`、`packages`、`.vs`、`.svn`、`.hg`。禁止越界、设备/UNC 路径、备用数据流、目录跳转、重解析点及硬链接；通过原生句柄验证最终路径并固定祖先目录。系统/安装目录、凭据目录、浏览器资料目录、`.ssh`、`.aws`、`.azure`、`.kube`、私钥、`.env`、凭据相关名称、`settings.json` 及副本始终拒绝。AppData 默认禁止，只有额外获得授权且符合临时目录规则的 LocalAppData 临时目录例外。二进制可以列元数据，但不读取或内容搜索。

文本在分页或搜索前整文件打码：已配置的服务密钥，以及中英文密码/密钥/令牌赋值、连接字符串、私钥块、Bearer/Basic、常见服务 Token、JWT 和带凭据的 URL。规则不能识别所有未知编码或混淆秘密，不应据此授权敏感资料目录。旧 `read_vs_file`、`scan_vs_code` 共用相同边界；扫描改为安全元数据列表，关键源码按需通过文件工具读取。任意 `run_powershell` 已从 AI 工具中移除，旧开关不能重新开放；截图工具见下方「AI 读取 VS 截图」，文件与截图中的文字均不构成操作授权。

**AI 读取 VS 截图**：需要看界面才能理解你说的位置（例如「右上角那个按钮」「这个弹窗」）时，总控助手会调用 `read_vs_screenshot`：短暂切换到目标 VS（或其前台弹窗）截图，截图后切回原窗口，不经预览直接交给当前模型分析，返回前台窗口 / 弹窗、各窗格位置、按钮与菜单文字等描述；开启「操作前确认」（`AgentConfirm`）时先弹窗确认。截图不保存到磁盘。需要支持图片的模型（如 DeepSeek `deepseek-flash`、通义千问 `qwen-vl-plus`、火山方舟 `doubao-seed-1-6-250615`、OpenAI `gpt-4o-mini`、本地 Ollama `qwen2.5vl`）；`deepseek-v4-pro` 等纯文字模型会直接提示「不支持图片」而不截图，接口拒绝图片时也会明确提示切换模型。`AgentScreenshotEnabled`（默认开启）关闭时两个截图工具都停用；`AgentScreenshotRequirePreview`（默认关闭，设置中的「截图需逐张预览批准」）开启后只能用需要逐张预览批准的 `capture_vs_screenshot`。

**笔记本技能**：总控助手与笔记 AI 助手共用同一套笔记本技能（工具与提示词相同），可以读写本地笔记本（`%APPDATA%\VSManager\Notebooks\notebook.db`）。`read_current_note` 读取笔记本中当前打开的页面（含未保存的编辑），`list_notes` 查找页面、`read_note` 读取正文；说「把这些结论记到笔记里」「新建一篇会议记录」时用 `create_note` 新建页面（可放在指定父页面下，同级不能重名），`append_to_note` 在已有笔记末尾追加且不改动原文；只有明确要求改写整篇时才用 `update_note` 覆盖正文。写入遵守「操作前确认」（`AgentConfirm`），单次最多 100000 字；写入后笔记本界面自动刷新，若你正在编辑同一页面，未保存的草稿会按原有规则另存为「标题-draft-时间」页面，不会丢失。笔记内容对 AI 而言是不可信数据，不构成操作授权。据笔记发布任务时，笔记页面中的图片可以一起发给目标 VS 的 Copilot：`read_note` 会列出页面引用的图片，`send_task` 的 `attachments` 填 `note:页面编号`（全部图片）或 `note:页面编号/资源名`（指定图片），图片复制到本机附件目录（`%APPDATA%\VSManager\attachments`）后随任务粘贴，受单个任务附件数量与大小上限约束；只能引用该页面正文实际引用的图片。

**拖拽排序**：在笔记本左侧目录中按住页面拖动即可调整顺序，拖动时以一条带圆点的强调色分割线标出放下后的位置（指向行的上半部放在该页之前、下半部放在其后；拖到已展开父页的下半部放入其子页最前，拖到「笔记本」根节点放到最前）。靠近上下边缘会自动滚动，在折叠的父页上停留片刻会自动展开；不能拖到自身或其子页面下，目标位置有同名页面时会提示。排序保存在本地笔记数据库中，重启后保持；搜索时不能拖动排序。

**笔记卡片**：在笔记中写 ```card 代码块，阅读视图会把它渲染成与任务清单一致的卡片（状态胶囊、编号、时间、标题、正文、附注）。每行一个「键: 值」，不带键的行接在上一个键后面：`status`（done / needs_user / unverified / running / waiting / failed / cancelled / info，决定颜色与默认胶囊文字）、`label`（自定义胶囊文字）、`duration`（用时）、`meta`（胶囊右侧说明）、`time`（右上角时间）、`title`、`text`、`note`（以 ↳ 开头的附注）。内容全部转义，不执行 HTML。总控助手可用 `add_note_card` 把卡片追加到指定笔记（遵守「操作前确认」），或用 `format_note_card` 生成卡片后配合 `update_note` 修改已有卡片；笔记助手用 `format_note_card` 生成卡片，点「📥 插入到笔记」写入。

**在页面上直接编辑笔记**：打开笔记后直接在渲染后的页面上输入和修改，无需切换到 Markdown；改动按原有规则自动保存，未改动的段落保持原始 Markdown 不变。支持 Markdown 快捷输入：行首输入 `#`～`######`、`-`、`1.`、`>`、`- [ ]` 后按空格转为标题、列表、引用、任务项，输入 ```` ```语言 ```` 后按回车新建代码块；Tab / Shift+Tab 调整列表缩进，单击复选框切换完成状态，Ctrl+V 可粘贴文字或截图。单击页面链接直接跳转，网页链接需 Ctrl+单击打开。右上角「Markdown 源码 / Source」切换到源码编辑，点「返回页面编辑 / Back to page」或按 Esc 返回；任务记录页面保持只读。
可选的 `style` 行决定卡片样式（不写即标准型，已有卡片不受影响）：`compact` 紧凑型（标题并入首行、正文一行）、`numbered` 编号左列型（`meta` 作为左侧大号编号）、`noted` 带附注型（附注完整显示为引用块）、`accent` 左色条型（按状态着色的左边框），也接受「紧凑型」「编号左列型」等中文写法。想先比较再选定时，让总控助手调用 `add_note_card_styles`，它会把同一组内容按每种样式各生成一张卡片写入笔记；`format_note_card` 与 `add_note_card` 也都支持 `style` 参数。

```card
status: done
duration: 16m57s
meta: #108 · AI
time: 09:48
title: → Demo
text: 实现导出功能
note: 构建与测试通过
```

**修改任务结果**：对总控助手说「把任务 #12 的测试清单改成中文」等，它先用 `list_tasks` 查看原结果与测试清单（待验证任务会列出各项及勾选状态），再调用 `edit_task_result(id, text)` 用完整的新结果文字替换原结果并保存到 `%APPDATA%\VSManager\tasks.json`。只改结果文字与测试清单，不改变任务状态、编号、排队与调度；执行中的任务不能修改；项数不变时保留已勾选状态；新文字里没有清单时保留原清单。遵守「操作前确认」（`AgentConfirm`），单次最多 4000 字，修改会写入任务日志与流水归档。

审计保存在 `%APPDATA%\VSManager\logs\file-audit.log`：记录操作、关联编号、脱敏路径及路径标识、开始/结果状态、数量和耗时，不记录搜索词或文件内容。读取前和返回前均须成功写入审计，否则不返回内容；无法读取的条目会汇总提示，不静默伪装为完整结果。审计及白名单仅保留本机，不提交到仓库。

### MCP 服务器（外部工具）

在「属性 → MCP 服务器」打开开关，填写配置后点击「应用并连接」（校验通过并确认后生效）。格式与常见 MCP 客户端相同，支持 `mcpServers` / `servers` 两种顶层键；每个服务器只能填写 `command`（本地 stdio，可带 `args`、`env`、`cwd`）或 `url`（Streamable HTTP，可带 `headers`）之一，`"disabled": true` 可暂时停用。值中可使用 `%变量%` 引用环境变量，建议令牌写成 `%变量%` 而不要直接写入配置。第一版不预装任何服务器，示例（可点「插入示例」）：

```json
{
  "mcpServers": {
	"example": { "command": "npx", "args": ["-y", "<mcp-server-package>"], "env": { "TOKEN_NAME": "%TOKEN_NAME%" } },
	"remote": { "url": "https://example.com/mcp", "headers": { "Authorization": "Bearer %TOKEN_NAME%" } }
  }
}
```

- 连接在后台完成：握手 `initialize`（协议版本 2025-06-18）→ `tools/list`（自动翻页）；卡片显示每个服务器的状态、工具数量或错误，可随时「重新连接」。服务器通知工具列表变化时自动刷新。
- 工具以 `mcp_服务器_工具` 的名称注册给 AI 总控助手（笔记助手不挂载），说明与参数 Schema 来自服务器；新增 `list_mcp_servers` 查看状态、`reconnect_mcp_servers` 重连（需确认）。
- 开启「操作前确认」时，调用未声明只读（`readOnlyHint`）的 MCP 工具前会弹窗显示参数；工具在后台线程执行，默认超时 180 秒，结果中的图片等二进制只给出摘要。
- `.cmd` / `.bat` 命令（如 `npx`）经 `cmd.exe` 启动；本地服务器进程放入作业对象，VSManager 退出时一并结束。诊断日志写入日志目录的 `mcp.log`（不记录环境变量与请求头的值）。
- 安全边界：MCP 服务器是独立进程，以当前用户权限运行，**不受「AI 文件授权」限制**，也不会因此扩大 VSManager 内置文件工具的授权；只添加可信服务器。系统提示要求助手把 MCP 返回内容视为不可信数据，未经用户要求不把授权文件内容发送给 MCP 工具。AI 不能增删服务器或修改配置。

### 发送前文档清理

在「属性 → 发送确认」显式开启 `CloseVsDocumentsBeforeSend`（默认 false）。仅在目标 VS 的文档标签页数严格大于 `CloseVsDocumentsThreshold`（默认 10）时，才在实际发送之前清理已保存文档；多个视图按文档窗口计数。调试中、调试状态未知、未保存或无法确认状态的文档一律跳过；工具窗口、Copilot 窗格和 VS 进程不关闭，也不会自动保存或丢弃修改。

先使用 DTE 文档窗口 `Close(0)`（保留保存提示，避免竞态丢失修改）；每步重新确认保存状态、窗口身份和调试状态。失败时只有唯一文档标题、路径、窗口句柄和 UIA 文档标签身份均可证明时，才点击该标签内的关闭按钮；身份不明或有模态窗口则拒绝后备操作。不发送全局“关闭全部”命令。清理串行执行，有枚举上限和 8 秒协作式预算；已进入的 COM/UIA 调用不能强制中止，不会遗留超时后继续关闭窗口的后台操作。

清理及通知失败单独记录，不改写任务文本、发送返回值或任务状态。诊断写入现有发送日志（右键 VS →「查看发送日志」），包含初始标签数、标题、保存状态、关闭方式和失败信息；清理结果及跳过的未保存文件名仅在本机 AI 助手界面显示，不加入模型上下文、不触发自动跟进，另按现有弹窗与语音设置播报数量。关闭标签页不保证 VS 的工作集立即下降。

### 打开对话助手

找到 Copilot 窗格不等于可以输入：窗格可能自动隐藏、被覆盖，或停留在「查看聊天历史记录」列表（此时「返回」按钮可见，对话列表与输入框不可见）。AI 工具 `open_copilot`（参数 `vs`：VS 编号或名称）按以下顺序降级：

1. DTE 执行 `View.GitHub.Copilot.Chat`，工具窗口自动隐藏时固定显示、不可见时设为可见（不改变停靠方式）；
2. 仍不可见时用 UI Automation 聚焦窗格；
3. 停留在历史记录时点击「返回」（`backToChat`）切回当前会话；
4. 校验输入框可见且可编辑，再把 VS 切到前台并聚焦输入框。

每步的窗格状态、候选数量、是否自动隐藏与耗时写入发送日志；结果按现有弹窗与语音设置播报「已打开对话助手」或「未能打开对话助手，请手动打开」。`AutoOpenCopilotPane`（默认 true）开启时，发送任务前也会先按同样的步骤打开窗格（不抢前台），定位输入框重试时同样会退出历史记录。历史列表视图中没有对话列表，窗格搜索靠「返回」按钮识别它。自动修复后窗格仍未就绪时，任务不会被当成「等待手动对话」原样重发：发送结果以「等待对话窗格就绪 / Chat pane not ready」开头并写明诊断原因与处理建议（未找到窗格、不可见、停留在历史列表、无输入框、定位不到输入框），任务清单每轮先诊断并修复，再间隔 10 秒、30 秒重试，最多 3 轮；仍失败就停止自动重发并以该原因失败（未提交任何内容），AI 总控助手会先调用 `open_copilot` 修复成功后再重试，否则把原因转告用户。

### AI 助手附件

- 输入：AI 助手输入框支持粘贴截图（Ctrl+V）、拖拽文件和「＋ 附件」按钮。支持图片（png/jpg/jpeg/gif/bmp/webp）、文本与代码（txt/log/cs/xaml/json/xml/md/csv 等）以及常见文档（pdf/docx/xlsx 等，只发送路径引用）。默认单个 10 MB、每条 5 个，超限时明确提示。
- 存储：附件复制到 `%APPDATA%\VSManager\attachments\yyyy-MM-dd\`，文件名为「时间戳-6 位随机后缀.扩展名」；对话记录、任务清单（tasks.json）与归档只保存引用（编号、原始文件名、大小、类型、SHA-256、相对路径），不内嵌二进制内容。对话中的附件显示为可点击链接（在资源管理器中定位），保存与清理记入 `logs\attachments.log`。该目录已加入 `.gitignore` 与发布自检，不会被提交。
- 随任务发送：AI 调用 `send_task` 时用 `attachments` 参数（编号或 `last`）指定附件，只能引用用户在本次对话中提供的文件。发送时图片复用现有的图片发送流程粘贴到 VS Copilot（单条最多 4 张，webp 与超出的图片改为路径引用）；文本文件以带文件名的代码块内联到正文（超长截断并注明）；二进制与文档只发送路径。图片在提交前失败时改为只发送文字（附图片路径），记为「文字已送达、图片未送达」并提示，不判为任务失败。当前模型支持看图时（如 `deepseek-flash`、`gpt-4o-mini`、`qwen-vl-plus`），图片（png / jpg / gif / webp，每条最多 4 张）会同时随消息发给 AI 模型直接查看，只保留最近一条带图消息的图片以免重复上传；已知纯文字模型（如 `deepseek-v4-pro`）只收到附件清单，接口拒绝图片时本会话自动改为只发文字并提示重发。
- 任务清单显示 `📎 N`，右键「查看附件」可打开或定位文件。设置窗口可调整上限与保留天数（`AttachmentKeepDays` 默认 30，0 表示不限制），并提供「立即清理过期附件」；仍被未结束任务引用的附件不会被清理。

### 手动对话优先 / Manual chat takes priority

`WaitForManualChat=true`（默认）让队列在目标 VS 有手动 Copilot 活动时等待；`ManualChatWaitTimeoutSeconds=300`（默认，范围 10–86400 秒；非正数恢复默认）。在「属性 → Copilot 对话」开关提前让行，在「发送确认」调整秒数；保存到 `%APPDATA%\VSManager\settings.json`。示例见 `settings.example.json`。超时只提醒一次并继续等待，不强制发送、不覆盖草稿、不增加尝试次数，也不把任务改为失败。用户可处理目标草稿，右键任务「重新检查并推送 / Recheck and send」重新探测，或取消任务。

- **空输入判定 / Empty-input rules**：文字、图片和发送边界共用 NFKC 规范化；只有 Unicode 空白（含换行、制表符、NBSP、全角空格）及零宽格式字符（如 U+200B/C/D、U+2060、U+FEFF、双向格式符）时视为空。标点、文字、数字、emoji、组合符、变体选择符及非空白控制字符仍保护；读取失败不等于空。空文字仍有附件、输入法合成、忙碌或未知状态时继续等待。/ Text, image and write-boundary guards share NFKC normalization. Unicode whitespace and zero-width format characters alone are empty; punctuation, letters, digits, emoji, combining marks, variation selectors and non-whitespace controls remain protected. Unreadable input is not empty. Attachments, IME composition, busy or unknown state still block.
- **失败与恢复 / Failure and recovery**：真正发送失败第一次就终止并保存为失败，不再每 30 秒重发。只有明确尚未提交的手动对话 / 弹窗保护继续等待且不消耗次数；写入或提交后不确定的结果立即失败，保留输入，禁止自动补发或切换发送方式重发。失败 / 取消任务可右键「手动重新排队 / Requeue manually」，先核实历史送达及草稿后确认；等待任务可「重新检查并推送」。操作仅授权当前任务、清除该目标探测缓存，仍需两次新空闲观察并保留保存、前序、目标身份、忙碌、附件和草稿保护，不开启全局 Start，也不宣称已送达。/ Real send failures stop on the first attempt and persist as failed. Only explicit pre-submission manual-chat/dialog protection waits without consuming attempts. Post-write/submission uncertainty fails, preserves input and forbids automatic resend/fallback. Manually requeue failed/cancelled tasks after reviewing prior delivery and drafts, or recheck waiting tasks. Only the selected task is authorized; its target cache is invalidated and two fresh idle samples plus all existing safety gates are required. Global Start is unchanged; a recheck is not delivery.
- **推送核实 / Push verification**：入队后核实任务确在清单中且已保存，并跟踪最多 30 秒；只有确认送达 Copilot 才提示「✅ 推送成功」，失败提示「❌ 推送失败」及原因，暂未发送提示「⏳ 已加入任务清单，尚未推送」及原因（等待开始、暂停、前序、目标忙碌 / 未打开等）。/ After enqueueing, the task is verified as listed and saved and tracked for up to 30 s; only a confirmed delivery to Copilot reports "✅ 推送成功 (pushed)", failures report "❌ 推送失败 (push failed)" with the reason, and tasks not yet sent report "⏳ queued, not yet pushed" with the reason (awaiting Start, paused, predecessor, target busy / closed, etc.).
- **诊断 / Diagnostics**：等待进入、超时、手动重查及失败终止记录在 `%APPDATA%\VSManager\logs\tasks.log`；输入探测变化记录在同目录 `send-diagnostics.log`，仅含目标身份哈希、原始 / 规范化长度、可读性、附件数量、合成 / 焦点状态及异常类别，不含草稿正文。发送步骤仍在归档目录 `logs\send-YYYYMMDD.log`（未归档时位于应用日志目录）；最终结果区分送达与待核实。/ Wait entry, timeout, manual recheck and terminal failure go to `tasks.log`; changed input observations go to `send-diagnostics.log` with identity hashes, lengths, readability, attachment counts, IME/focus flags and exception types only, never draft text. Existing send traces retain stage evidence and distinguish delivery from uncertainty.

- **依据与边界**：只在准确目标实例的 Copilot 窗格查找已配置的可见停止按钮，以及既有分层定位器识别的输入框。生成中、未发送草稿（失焦后仍保护）、未发送附件、可检测的输入法合成、无法读取输入或 UIA 异常均等待。只打开窗格或空框保留焦点不等于输入中。独立后台 STA 探测不切换焦点、不打开窗格，最多四个未结束探测；每目标约两秒采样，连续两次空闲才放行。无窗格可进入原自动打开流程，但打开后、写入剪贴板 / 输入前再次检查；读取失败绝不按空白处理。
- **调度与清单**：保护不依赖 `MonitorCopilot`、`WatchConversations` 或归档，也不从历史手动对话推断当前忙碌。等待只是会话内说明，任务仍为原排队状态；任务行、悬停提示和 AI / 网页任务清单共享原因。仅已获启动资格且前序放行的队首探测；同目标后续不插队，其他目标独立继续。立即发布、重试、附件、暂存恢复和工作树合并仍走相同保护。管理器自身在途任务不是新的手动等待，完成跟踪不受草稿保护阻挡；重启重新探测。
- **通知**：开始等待、超时、真正送达后自动继续各通知一次；就绪不等于送达。完成通知注明曾礼让手动对话，与原自动完成通知合并，避免重复。沿用 `PendingVsNotify`、弹窗 / 提示音及 `VoiceAnnounce`、语音语言设置。等待不会触发 AI 完成回执；已写入 / 已提交但无法确认的队列发送需要用户核实，禁止自动重发。
- **关闭与隐私**：关闭只撤销提前让行，写入边界仍保护草稿、附件及未知输入，不绕过原 Busy、构建、等待回复、前序或启动授权。检测仅记录类别和长度等诊断，不存储或记录目标草稿、按键或输入法合成文本，不安装全局键盘钩子。该观察不是对用户意图的判断；未向 UIA / Windows IME 接口暴露的编辑或合成状态无法保证可识别，实际 VS / Copilot / 输入法版本仍需现场验证。检查与写入并非跨进程原子操作，但在写入边界再次校验目标、任务资格与输入。

With **Wait for manual chat** enabled (default), generation, unsent drafts (even without focus), attachments, detectable IME composition and unreadable/unknown input hold the target queue. Empty input focus or an open pane alone does not. Set `ManualChatWaitTimeoutSeconds` in Settings (default 300; range 10–86400; nonpositive values restore the default). The timeout warns once and **keeps waiting**, never forcing a send, overwriting drafts, failing the task or consuming retries. Settings persist in `%APPDATA%\VSManager\settings.json`.

Read-only STA probing is independent of monitoring, conversation display and archives, uses the exact target and existing input locator, caps outstanding probes at four, samples each target roughly every two seconds and requires two idle samples. Missing panes may use existing auto-open, followed by checks before clipboard/input mutation. Eligibility, full-list predecessors, per-target ordering, attachments, parked tasks and worktree barriers remain intact; other targets continue independently. Running manager tasks are not manual chats; completion tracking is not input-gated. Wait reasons are session-only and shared by task rows, tooltips and AI/web list results. Explicit manual requeue/recheck grants only the selected task, never global Start or a protection bypass.

One notice each covers waiting, timeout and confirmed resumed delivery; completion adds a short yield note without duplicating automatic-completion announcements. Existing `PendingVsNotify`, popup/sound, voice enablement and language choices apply. Uncertain post-write/submission results require manual verification, not automatic resend. Disabling advance yielding never bypasses write-boundary input protection or existing Busy/build/reply/predecessor gates. Detection records only categories and diagnostic lengths, not drafts, keys or IME text, and installs no global hook. Unexposed UIA/IME states cannot be guaranteed detectable; real VS/Copilot/IME versions need validation. Cross-process observation and writing are not atomic, so safety is rechecked at the write boundary.

### 自动启动与手动开始 / Automatic and manual workflow start

- **默认仅 AI 自动**：`AutoStartAiTasks=true`、`AutoStartAllTasks=false`。AI 的 `send_task`（含附件与暂存）保存入队成功后，本会话该任务自动获得调度资格，无需另点 Start；不调用全局 Start。手动 / 网页用户任务以及从 tasks.json 恢复的旧 AI 任务不会被顺带放行。相同目标的手动前序仍阻塞后续 AI，其他目标可独立调度；仍由同一个调度器检查完整清单的编号、前序和工作树屏障，不直发、不插队，拖拽只影响显示。
- **属性可配置**：开启 `AutoStartAllTasks` 优先于仅 AI，显式授权现有未完成任务（含恢复的执行中任务与合并）和后续入队任务；持久化后下次启动也按全部自动处理。两者关闭时，后续入队任务回到手动 Start。配置改变只影响后续入队（启用全部模式同时授权已有活动任务），既有会话授权不撤销、在途工作正常完成；不是暂停开关。需停止排队任务可用取消。失败任务仍需用户明确重新排队；手动重查 / 重新排队只授权当前任务，不改变来源、不授权其他任务。
- **按钮与恢复**：Start 只表示用户手动开启本会话的完整流程，AI 自动启动时按钮仍可点击；每个条目显示自己的启动资格和等待前序。默认重启丢弃会话授权，旧任务仍等 Start；显式重复 `send_task` 可重新授权仍活动的 AI 条目，但只复用一次，不改变手动重复条目的来源，不授权旧合并。恢复的运行中任务先核验而非重发；崩溃中断发送保留失败保护。
- **AI 启动流程**：AI 总控助手可调用 `start_task_workflow` 将本会话切换为已启动，效果等同点击「开始流程 / Start」（开启「操作前确认」时会先询问）；无论由用户还是 AI 启动，按钮都会同步显示「✓ 已启动 / Started」并置灰。
- **保存、暂存与通知**：保存失败不自动授权，提示用户待保存恢复后重发或 Start；目标未打开则暂存，打开后仍等待 `PendingVsSettleSeconds`。每条获授权任务仅一次自动启动通知 / 播报，自动完成文案说明 AI / 全部模式；通过 `PendingVsNotify` 控制，语音仍尊重原语音开关和中英文语言选择。入队响应只说明资格与等待条件，不宣称已执行完成。
- **工作树维护**：每五个成功开发任务的新合并屏障，仅在由本会话自动任务完成所产生时继承资格；未获资格的手动任务、旧合并不会因此获授权。合并失败 / 取消仍阻塞工作线，处理后重试原合并，保持原有归档、状态与失败跳过策略。

With `AutoStartAiTasks=true` and `AutoStartAllTasks=false` (defaults), persisted AI submissions, including attachments and parked tasks, receive session-only eligibility without global Start. Manual/web tasks and restored AI tasks still await Start; earlier manual tasks block the same target while independent targets can run. ID ordering, complete-list predecessor checks, failure policy, worktree barriers and display-only dragging are unchanged.

Enable **Auto-start all tasks** in Settings to include existing unfinished/restored tasks (including running work and integrations) and future admissions; this persisted mode also applies after restart. Disable both for manual future admissions. Changes do not revoke existing session grants or interrupt in-flight work; use cancellation for queued work. Explicit manual requeue/recheck authorizes only the selected task without changing its source or granting other tasks. The Start button remains available until the full workflow is started. The AI assistant can also start it with `start_task_workflow` (same as clicking Start; asks first when "Confirm before acting" is on); whether the user or the AI starts it, the button syncs to "✓ 已启动 / Started" and is disabled.

Default restarts discard grants; an explicit duplicate AI submission may reauthorize the same active AI entry, never convert a manual entry or authorize an old integration. Failed saves withhold eligibility until an explicit resubmission or Start after save recovery. Closed targets still await readiness and the configured settle delay. One bilingual start notice per granted task and automatic-completion notices identify AI/all mode, obey `PendingVsNotify` and existing voice/language settings. Admission is not proof of execution. Only new barriers generated by this session's automatically completed development work inherit eligibility; old barriers do not. Integration failure/cancellation and crash-interrupted sends retain their existing explicit-retry protections.

### 暂停任务队列

任务清单标题行的「⏸ 暂停」可暂停整个队列：暂停期间不再发布新任务、不推送暂存任务，排队任务全部保留；有执行中的任务时会询问让它执行完（完成结果照常记录），还是中断它（停止该 VS 的 Copilot，任务重新排队，继续后重新发送并附上「在已有改动基础上接着做」的说明）。点「▶ 继续」恢复并按编号发布。暂停状态保存在 `settings.json`（`TaskQueuePaused`），重开 VSManager 后仍保持暂停；AI 助手也可用 `pause_task_queue` 暂停 / 继续（中断执行中的任务需用户确认），`list_tasks` 会显示暂停状态。

任务清单每次变更都立即写入 `tasks.json`（上一版本保存在 `tasks.json.bak`），重开后排队、等待目标 VS、执行中的任务以及「已放行」「已中断」标记都会恢复；上次正在发送的任务恢复为排队（异常退出时改为失败待确认，避免重复发布）。

### 任务清单分组

右侧任务清单默认按目标 VS 分组（`TaskListGroupByVs` 默认 true），每组一个标题行：已打开的 VS 显示「@编号 名称」（编号与左侧列表一致），未打开的显示「名称（未打开）」，并统计任务数、执行中、排队、待打开与失败数量。组内沿用原排序（执行中 / 排队按编号在前，已结束的按完成时间倒序）；组间默认「有执行中的优先，再按最近活动倒序」（`TaskListGroupSort = activity`），也可选按 VS 编号（`number`）。「等待目标 VS」的任务在目标已打开时归入该 VS 分组，否则归入单独的「等待打开」分组。点击标题折叠 / 展开（折叠状态保存在本机 settings.json 的 `TaskListCollapsedGroups`），右键标题可全部折叠 / 展开、切换排序或改为平铺列表；标题栏的 ▤ / ≡ 按钮在分组与平铺之间切换。分组只影响显示，标题行不可选中；排队、发布与清除 / 历史等操作不变。

任务清单标题栏的「移除无效」按钮一次移除所有失败、已取消的任务与已停止 / 已中断的手动对话（确认后执行）：任务从 `tasks.json` 删除，历史归档仍保留记录；发送中的任务与 Worktree 记录不会被删除。没有无效条目时按钮不可用。

#### 拖拽显示排序 / Drag-to-reorder display

- **仅显示，不改变执行顺序 / Display only; execution order unchanged**。本功能选择显示排序方案：实际调度始终遵守原编号、前序、启动资格和工作树合并屏障规则，不提供拖拽切换执行顺序的开关；不会更改任务编号、目标 VS、状态、发布、完成通知、语音或归档。/ This feature changes display order only. Dispatch still follows IDs, predecessors, start eligibility and worktree barriers; dragging cannot change execution order or task business state.
- 左键拖动任务或手动对话：平铺时可放任意位置；分组时仅允许同组，跨组显示拒绝提示（需全局显示排序时切换平铺）。拖动 VS 标题移动整组，落在组内时吸附该组前 / 后边界，折叠组也可移动，列表尾部空白可追加到末尾。插入线标明落点；接近上下边缘自动滚动；Esc 或拖出列表松开取消。标题单击在松开时折叠 / 展开，不会因拖拽而折叠。/ Drag tasks or manual chats anywhere in flat view, or within their VS group. Drag headers to move whole groups; targets snap to group boundaries. Collapsed groups and blank list tails are supported, with insertion lines, edge scrolling and Esc/outside-drop cancellation. Header clicks toggle only on release.
- 右键菜单仅保留关键操作（推送 / 重新排队 / 取消、查看对话、复制、附件、删除）；清除与历史改用标题栏按钮。首次有效拖动自动启用手动显示顺序，右键「恢复默认排序」删除已保存顺序；悬停列表或 ▤ / ≡ 显示当前模式与执行隔离说明。/ The context menu keeps only key actions (send / requeue / cancel, view chat, copy, attachments, remove); clearing and history use the header buttons. A successful drag enables manual display order, and right-click "Reset order" removes saved ranks. Hover the list or view button for current modes and the dispatch distinction.
- `settings.json` 保存上述开关与排序键，重启恢复。任务按稳定编号识别；对话使用归档可恢复的 VS、开始时间及问题身份，不使用重启会重建的对话编号。新条目 / 新分组在已有手动项之后按默认规则显示。切换平铺保留组顺序，清除已完成、历史开关、撤销清除、失败隐藏、重新排队及折叠不会丢失已有排名；删除或暂不显示的键保留到显式重置，避免历史恢复错位。保存键去重并过滤无效值，不静默截断条数。/ Settings persist modes and stable identity keys across restarts. New entries/groups follow ranked ones in default order. Flat view, history filtering, undo-clear, hidden failures, retries and collapse preserve ranks. Deleted/absent keys remain until explicit Reset, without silent count truncation.

### 截图器

点击主窗口顶部的「✂ 截图」（截图时暂时隐藏本窗口），或在任何程序中按全局快捷键 `Ctrl+Alt+Shift+S`（不隐藏本窗口；托盘菜单也有「截图」）：各屏幕画面被冻结并调暗，按住左键拖动框选区域，松开即完成，选区旁显示像素尺寸；Esc 或右键取消（框选中右键只放弃当前选区）。截图复制到剪贴板（不保存文件），可直接粘贴到 AI 助手、VS 对话输入框或笔记中；结果与取消记录在 `%APPDATA%\VSManager\logs\snip.log`。窗口较窄放不下按钮时按钮自动隐藏，快捷键与托盘菜单仍可用；快捷键被其他程序占用时只记录日志，按钮不受影响。

### 内存监控

点击主窗口顶部的「🧠 内存」打开内存面板：按 VSManager 本体、各 VS 实例（devenv 及其全部子进程，如 ServiceHub、WebView2、MSBuild、Copilot 语言服务）和无归属的共享组件（如 VBCSCompiler）分组，显示每个进程的 PID、所属 VS、工作集、私有字节与占比，默认在每个任务完成后自动刷新（打开窗口时及按 F5 也会立即测量）。

日常同步只为本次请求的消息读取 UI Automation 子树，不再缓存整段长对话的历史子树；已关闭 VS 的窗格、消息与监听缓存会自动释放（隐藏窗口时也会清理）。对话记录容量裁剪使用两遍流式读取，避免把整个日志加载到内存；原有保留天数、条数与追加顺序不变，不删除额外历史或任务。

对话浏览器首次可见时才初始化；隐藏或最小化后停止渲染并尝试挂起，重新显示时同步最新内容。对话更新只传输变化的消息，进度提示变化不再发送整段历史；不再重复保留整份 HTML 缓存。不会缩减完整对话、改变 AI 上下文额度或清除用户的 WebView2 数据。

- 「清理 VSManager」：完整 GC 并修剪 VSManager 及其 WebView2 的工作集。
- 「温和清理」（单个 VS 或全部）：若 VS 提供 `Tools.ForceGC` 命令则先触发 VS 内部 GC，再修剪标为「可安全清理」的进程的工作集。修剪只是把不常用的内存页移出物理内存，需要时自动换回；不会结束任何进程、不会丢失未保存内容，私有字节通常不变。
- 调试器组件、测试宿主、终端 / Copilot 代理命令、被调试的程序等标为「不建议」，只展示不清理。
- 每次清理的前后数值显示在面板底部，并写入 `%APPDATA%\VSManager\logs\memory.log`。
- 超阈值自动策略（默认关闭）：`VsMemoryAutoEnabled`（默认 false）、`VsMemoryThresholdMB`（默认 6144）、`VsMemoryAutoClean`（默认 false = 只提示）。每分钟检查一次，同一 VS 30 分钟内最多处理一次；VS 正在调试 / 生成 / Copilot 运行中时只提示。
- 定期自动清理（默认关闭，在内存面板底部配置）：`AutoTrimVsMemory`（默认 false）、`AutoTrimIntervalMinutes`（默认 30，范围 5–1440）、`AutoTrimThresholdMB`（默认 0 = 不限制；大于 0 时只清理工作集超过该值的 VS）。后台定时器每 30 秒检查是否到期（不占用界面线程），到期后复用上面的温和清理，清理范围完全相同。正在调试、生成、Copilot 运行、有发送中 / 执行中任务，或自动化接口不可用（无法确认状态）的 VS 一律跳过并在 `memory.log` 记录原因。面板显示上次结果与下次预计时间，并提供「立即执行一次」。实际释放内存时通知并播报「已自动清理 N 个 VS 实例内存，释放 X MB」；无效果或全部跳过时只记日志。

### 自动重启

- **AI 助手自动重启**（默认开启，`AgentAutoRestart`）：AI 助手内部出现未处理异常、请求连续失败 `AgentFailureThreshold` 次（默认 3，仅统计网络错误 / 超时 / 5xx 等临时故障）或运行中 `AgentHangTimeoutSeconds` 秒没有任何进展（默认 120；等待用户确认时不计）时，自动取消当前一轮、重建 AI 客户端并恢复可用，对话中与状态栏会显示「AI 助手已自动重启」。任务清单不受影响。
- **进程看门狗**（默认关闭，`ProcessWatchdogEnabled`）：开启后会启动一个独立的看门狗进程；VSManager 异常退出（崩溃、被结束）后约 2 秒自动重新拉起。任务清单每次变更都会写盘，崩溃时还会再尽力保存一次；重启后默认恢复任务队列但等待手动「开始流程」（显式全部自动模式除外），获资格后执行中的任务继续跟踪；退出时「发送中」的任务可能已送达，因此标为失败并提示手动重新排队，避免重复发布。正常退出不会被拉起。
- **防重启风暴**：`AutoRestartWindowMinutes` 分钟内最多自动重启 `AutoRestartMaxCount` 次（默认 5 分钟 3 次，AI 助手与进程分别计数），超过后停止自动重启并提示查看日志。
- **手动入口**：主窗口顶部「⟳ 重启」菜单与托盘菜单提供「重启 AI 助手」「重启 VSManager…」（需确认；正在发送时拒绝，任务清单与配置先保存），菜单内还可切换上述两个开关、打开日志目录。
- **测试清单分类与自验证循环**：任务回执规则要求 Copilot 在每个测试项开头标注「[AI]」（AI 总控助手可用工具验证：编译 / 单元测试、日志、文件或配置、命令与接口返回、验证接口等）或「[人工]」（需要操作界面或观察画面、声音）；未标注的项按文字保守推断，涉及界面、点击、观察或无法判断时一律归为人工。测试清单中 AI 项显示青绿色「AI」标签，人工项显示琥珀色「人工」标签，顶部统计两类剩余项数。「🤖 AI 验证 / AI verify」让助手立即用工具验证所有未勾选的 AI 项；「🔁 自验证」开关（需开启「任务完成自动跟进」，保存为 `AgentSelfVerify`）开启后，任务进入待验证且含 AI 项时自动通知助手验证、用 `mark_test_item` 勾选（写明依据），未通过则用 `retry_task_with_info` 带证据重试，再次待验证时自动进入下一轮，受 AI 自主补充上限（3 次）约束。`mark_test_item` 拒绝勾选人工项；人工项始终留给用户。VSManager 自身的任务仍通过自测重启测试。
  **Checklist split and self-verify loop**: the receipt rules ask Copilot to tag each checklist item "[AI]" (the AI assistant can verify it with tools: build / unit tests, logs, files or settings, command and API output, verification checks) or "[人工]" (manual: needs UI interaction or watching / listening); untagged items are inferred conservatively and anything about UI, clicks, observation or unclear is manual. The test checklist shows AI items with a teal "AI" tag and manual items with an amber "人工" tag, with counts of both at the top. "🤖 AI verify" asks the assistant to verify every unchecked AI item now; the "🔁 Loop" switch (needs task auto follow-up; saved as `AgentSelfVerify`) makes tasks awaiting verification with AI items notify the assistant to verify them and check them via `mark_test_item` with evidence, retrying with `retry_task_with_info` and the evidence on failure; the next pending result re-enters the loop, bounded by the AI retry cap (3). `mark_test_item` refuses manual items, which always stay with the user. VSManager's own tasks are still tested through the self-test restart.
- **自测重启技能**（AI 总控助手）：VSManager 自身的编程任务完成后，对助手说「重启 VSManager 测试新功能」，它先用 `list_tasks` 读取测试清单写成测试计划，再调用 `restart_vsmanager_for_testing`。要求 VSManager 正在某个 VS 的调试器中运行（F5 启动）；工具先用该 VS 自带的 MSBuild 把 VSManager 项目生成到临时目录确认能编译（失败则不重启，正在运行的程序不受影响），本轮回复结束且没有发送中的任务后保存任务清单、配置、笔记与本会话的启动授权，写入 `%APPDATA%\VSManager\restart-handoff.json`，再让该 VS 执行 Debug.Restart。等待期间暂停发布新任务；其他 VS 中执行的任务照常进行，重启后继续跟踪、不会重发。新进程读取交接单（只用一次，30 分钟内有效）后恢复启动授权，对话自动接续，并向助手发送「[重启完成通知]」（含新旧进程、程序文件时间以判断是否加载了新程序）；助手按计划逐项执行能用工具完成的测试，用 `mark_test_item` 勾选有工具依据的通过项，需要用户操作或观察的项列为「需用户测试」。VS 未能重启时自动撤销并告知助手。
  **Self-test restart skill** (AI assistant): after a VSManager coding task, ask the assistant to restart VSManager and test; it builds a test plan from the checklist via `list_tasks` and calls `restart_vsmanager_for_testing`. VSManager must run under a VS debugger (F5). The tool pre-builds the project into a temp folder with that VS's MSBuild (no restart on failure; the running app is untouched); after the round ends and no send is in flight it saves tasks, settings, notes and session start grants to `%APPDATA%\VSManager\restart-handoff.json`, then has that VS run Debug.Restart. New sends pause meanwhile; tasks running in other VS instances continue and are tracked again after the restart, never resent. The new process consumes the handoff once (valid 30 minutes), restores grants, resumes the conversation and sends the assistant a "[重启完成通知 / Restart completed]" notice (old/new process and exe times show whether the new build loaded); the assistant runs the tool-verifiable items, checks passed items with evidence via `mark_test_item` and lists the rest as needing user testing. If VS does not restart, the attempt is withdrawn and the assistant is told.
- **无感重启（不等待其他 VS）**：自测重启只等 AI 本轮回复结束、发送中的消息与正在进行的收尾合并，以及调试 VSManager 的那个 VS 中的任务；其他 VS 中正在执行的任务一律忽略，不必等它们完成，它们照常执行。等待期间其他 VS 的完成事件暂缓处理，排队的助手通知不再在旧进程里开新一轮，而是写入 `%APPDATA%\VSManager\restart-notices.json` 带到新进程（只读一次，12 小时内有效），在「[重启完成通知]」之后补发；暂缓完成的任务由新进程的执行中跟踪重新读取结果，不会重发。手动「重启 VSManager」同样带走未处理的通知。提示词已同步：只有调试 VSManager 的 VS 中有执行中任务时才不重启。
  **Seamless restart (no waiting on other VS)**: a self-test restart waits only for the assistant's current round, in-flight sends, ongoing finishing / merging and tasks in the VS debugging VSManager; tasks running in other VS instances are ignored, never waited for, and keep running. Meanwhile their completion events are deferred and queued assistant notices no longer start new rounds in the old process; they are written to `%APPDATA%\VSManager\restart-notices.json`, carried to the new process (read once, valid 12 hours) and re-delivered after the "[重启完成通知 / Restart completed]" notice. Deferred tasks are picked up by the new process's running-task tracking, which reads their results without resending. The manual "Restart VSManager" also carries unprocessed notices. The prompt now says only a running task in the VS debugging VSManager blocks a restart.
- **界面状态探测工具**：AI 总控助手新增 `get_window_state`、`get_foreground_window`、`list_tray_icons`、`read_restart_handoff`，可自己验证重启后窗口位置 / 页面 / 草稿是否恢复、是否抢焦点、是否留下托盘残影、交接文件是否被消费，支撑自迭代。提示词、重启完成通知与测试清单标注规则已同步说明；写明使用这些工具的测试项归为 [AI]，已标 [人工] 的项仍不能由 AI 勾选。
  **UI state probe tools**: the AI assistant gains `get_window_state`, `get_foreground_window`, `list_tray_icons` and `read_restart_handoff` to verify by itself whether window position / page / draft were restored after a restart, whether focus was stolen, whether a ghost tray icon remains and whether the handoff files were consumed, enabling self-iteration. The prompt, the restart-completed notice and the checklist tag rule describe them; items naming these tools count as [AI], while items tagged [人工] (manual) still cannot be checked by the AI.
- **可验证性重判与自动验证**：任务进入待验证时按测试项文字重判 [AI] / [人工]（已有清单在启动与读取时同样重判，只改未勾选项）：窗口位置、大小、最大化 / 最小化、所在屏幕、当前页面、选中的 VS、输入框草稿、托盘图标与残影、前台焦点、交接文件消费状态归为 [AI]；画面观感、动画、颜色、需要用户点击按钮、需要人为制造故障的项保持 [人工]。核对清单工具返回或其他项标注的元测试项（提到 `list_test_checklists` / `list_tasks` / `mark_test_item`，或写明某类项「显示为 / 标为 [AI] / [人工]」）单独判定：引号（『』「」“”、反引号等）里引用的是其他项，不参与判定，去掉后本项仍需点击按钮等人工动作才判 [人工]，否则判 [AI]。AI 发布的任务即使未开「🔁 自验证」循环，完成通知也附「[自动验证]」说明，让助手先用 `get_window_state` 等工具验证并勾选 [AI] 项（写明依据），验证不了的如实转告、不得勾选；需要重启才能验证的项只在用户要求或循环 / 自迭代进行中才重启。需要特定前置场景（某个 VS 对话页、最大化 / 副屏、草稿、先切到其他应用）时，助手用 `prepare_restart_scenario` 自己造出场景再触发自测重启。
  **Verifiability re-judging and auto-verification**: when a task becomes awaiting verification its items are re-judged [AI] / [人工] from their text (existing checklists too, at startup and when read; unchecked items only): window position, size, maximized / minimized, screen, current page, selected VS, input draft, tray icons and ghosts, foreground focus and handoff-file consumption become [AI]; looks, animation, colors, clicking buttons and deliberately causing failures stay [人工]. Meta items that check a checklist tool's output or other items' tags (mentioning `list_test_checklists` / `list_tasks` / `mark_test_item`, or stating that some items "show as / are tagged [AI] / [人工]") are judged separately: quoted text (corner brackets, quotes, backticks) cites other items and is ignored; only a human action left in the item itself (e.g. clicking a button) makes it [人工], otherwise it is [AI]. Even without the "🔁 Loop", completion notices of AI-published tasks carry an "[自动验证 / Auto-verify]" block so the assistant first verifies and checks the [AI] items with `get_window_state` and the other tools (citing evidence) and honestly relays what it cannot verify, never checking it; items that need a restart are restarted only when the user asks or a loop / self-iteration is running. For items that need a precondition (a VS chat page, maximized / second screen, a draft, another app in front) the assistant builds it with `prepare_restart_scenario` before triggering the self-test restart.
- **补 skill 闭环**：AI 总控助手验证测试项时，若某项用现有工具验证不了、但要看的是机器可读状态（窗口 / 控件 / 托盘 / 文件 / 日志 / 进程等），它自己判断需要什么 skill 并调用 `start_skill_gap_loop`，无需用户提醒地完成「发布实现任务 → 重启加载 → 用新 skill 验证 → 通过勾选 / 未通过带证据修复」，直到通过或达到轮次上限（默认 3）。它是自迭代的特例：复用自迭代的状态、轮次上限、重启完成通知与 `stop_self_iteration`，同一时间只能有一个；区别是由 AI 自动发起、授权只覆盖实现与修复该 skill，目标固定为让该测试项可自动验证。必须人眼 / 人手的项不发起，每项只发起一次；skill 正常但被测项本身不符时交回原任务流程处理。
  **Skill-gap loop**: when an item cannot be verified with existing tools but concerns machine-readable state (window / control / tray / file / log / process), the AI assistant decides which skill is needed and calls `start_skill_gap_loop`, then runs "publish the implementation → restart to load it → verify with the new skill → check on success / fix with evidence on failure" without user reminders until it passes or the round limit (default 3). It is a special self-iteration reusing the same state, round limit, restart notice and `stop_self_iteration`, and only one can run at a time; unlike a user-started one it is started by the AI, authorizes only tasks implementing or fixing that skill, and its goal is fixed to making that item automatically verifiable. Never for items needing human eyes or hands, one loop per item; if the skill works but the item itself fails, the original task's flow takes over.
- **查看全部测试清单**：AI 总控助手用 `list_test_checklists` 查看全部待验证任务的完整测试清单（不再只看到最近的两三条），`list_tasks` 也会列出所有待验证任务并为测试项编号；旧任务的清单从已保存的回复补齐。提示词说明这是只读查询、不能为此发布任务：清单保存在 VSManager 自身，各 VS 中的 Copilot 看不到，发布只会产生无效任务；工具不足时也须先说明原因、经用户确认才可请求完善能力。
  **View every checklist**: the AI assistant uses `list_test_checklists` to see the full checklist of every task awaiting verification (not just the two or three most recent), and `list_tasks` now includes every such task with numbered items; older tasks are filled from the saved reply. The prompt explains this is a read-only query that must not become a published task: the checklist lives in VSManager and the Copilot in each VS cannot see it, so publishing would only create a useless task; when tools fall short it must explain why and ask for an improvement only after the user confirms.
- **更无感的重启**：自测重启与「重启」按钮保存窗口位置、大小、最大化 / 隐藏状态、页面、选中的 VS 与 AI 草稿到 `%APPDATA%\VSManager\restart-ui.json`（只用一次，15 分钟内有效）。新窗口在显示前准备位置、页面与草稿；屏幕失效不妨碍恢复隐藏 / 最大化状态。恢复不主动激活窗口，避免从重启期间切换到的应用抢焦点；需要时可用托盘或热键激活。自测重启在主窗口处于前台时，先异步准备位于旧窗口后方的截图并等待就绪（最多八秒），不激活、不置顶、不占任务栏；准备失败则清理辅助进程并降级为普通重启。旧进程退出后超过 1.5 秒才显示「截图暂不可交互」提示，可点击关闭。新窗口同步绘制恢复的控件、选中 VS 后释放截图；缺失 VS 最多额外等三秒，WebView 内容可能继续加载。用户导航、启动异常或关闭也会释放截图，辅助进程另有四分钟超时。界面状态保存失败会取消自测重启、恢复通知与托盘，不再带着不完整状态退出。接续对话每 200 毫秒检查实例刷新与助手空闲，实例列表最多等八秒，不再固定等两秒。页面与选中的 VS 仍在二十秒内保持，用户手动切换立即让步。
  **Smoother restart**: self-test and manual restarts save bounds, maximized/hidden state, page, selected VS and AI draft to `%APPDATA%\VSManager\restart-ui.json` (consumed once, valid 15 minutes). Placement, page and draft are prepared before showing; a missing monitor no longer prevents hidden/maximized restoration. Restore never requests activation, preserving an app switched to during restart; tray and hotkey activation remain available. A foreground self-test asynchronously prepares a snapshot behind the old main window and waits up to eight seconds for readiness, without activation, topmost status or a taskbar entry. Preparation failure cleans up the helper and falls back to an ordinary restart. A dismissible snapshot-only notice appears only after the old process has been gone for 1.5 seconds. Restored controls are synchronously painted and the selected VS is restored before releasing the snapshot; a missing VS adds at most three seconds, and WebView content can still load afterward. Navigation, startup errors or exit also release it; the helper has a four-minute timeout. UI-state save failure aborts the self-test restart and restores notices and the tray. Continuation checks discovery and assistant idleness every 200 ms, waiting at most eight seconds for instances instead of imposing a two-second minimum. Page and VS selection are still preserved for twenty seconds, yielding immediately to user navigation.
- **无感边界与测试清单**：这是减少中断，而非零中断承诺。截图不是可交互界面；重新编译、WebView 初始化、网络重连及 VS 自身切前台仍可能可感知。旧托盘图标先移除以减少残影，新图标和任务栏窗口由新进程建立，因此仍可能短暂消失 / 重排；永久稳定的图标身份需要独立常驻宿主，本次不引入。当前模型回复仍等完成后才自测重启，其他 VS 任务与待处理通知保持原有交接规则。
  **Limits and checklist**: this reduces disruption rather than promising zero interruption. The snapshot is not interactive; rebuilding, WebView initialization, reconnection and VS itself taking foreground may remain visible. Removing the old tray icon reduces ghosts, but the new process creates a new tray icon and taskbar window, so gaps/reordering remain possible. A permanently stable identity requires a separate resident host, not introduced here. Self-test still waits for the current model reply; other VS tasks and pending notices retain the existing handoff rules.
  **自测重启页面例外**：自测重启固定进入 AI 总控助手页，不再恢复原 VS 对话页，也不等待原 VS 选择恢复；上述页面保持机制使用 AI 总控页作为目标，用户之后手动切页仍立即让步。窗口位置、大小、最大化 / 隐藏、焦点与草稿恢复不变。普通「重启」仍恢复原页面；AI 功能关闭时不自动启用它。
  **Self-test page exception**: self-test restarts always open the AI assistant page rather than the previous VS chat, without waiting to restore that VS selection. The settling mechanism targets the AI page and still yields to subsequent user navigation. Bounds, maximized/hidden state, focus and draft restoration are unchanged. Ordinary restarts keep the saved page; a disabled AI feature is not enabled automatically.
  - [ ] [AI] 从 VS 对话页自测重启，确认进入 AI 总控页且窗口状态、草稿与交接消费不变；普通重启仍恢复原页面 / Self-test restart from VS chat: verify the AI page, unchanged window state/draft and consumed handoff; ordinary restarts retain the saved page (`get_window_state`, `read_restart_handoff`).
  - [ ] [人工] 前台快速 / 慢速重启，观察空白、提示延迟、截图点击关闭与内容加载；不要把截图当作实时界面 / Observe fast/slow foreground restarts, blank frames, delayed notice, click dismissal and content loading; do not treat the snapshot as live UI.
  - [ ] [人工] 重启准备及重建期间切到其他应用、输入文字；确认不中断输入、不被截图遮挡，用户改选页面后不被拉回 / Switch apps and type during preparation and rebuilding; check uninterrupted input, no cover obstruction and no navigation being undone.
  - [ ] [人工] 最小化 / 托盘隐藏、最大化、副屏及断开原屏幕场景，确认无普通窗口闪现或启动气泡 / Check minimized/tray-hidden, maximized, secondary and disconnected-monitor cases for normal-window flashes or startup balloons.
  - [ ] [人工] 隔离环境模拟辅助进程失败、状态写入失败、VS 不重启与缺失目标 VS；确认降级 / 取消、截图清理、托盘恢复和有界等待 / In an isolated environment simulate helper failure, state-save failure, no VS restart and a missing selected VS; verify fallback/abort, cleanup, tray recovery and bounded waits.
  - [ ] [AI] 在获准的真实重启后核对其他 VS 任务不重发、授权和通知接续；先采样前台，再检查托盘残影 / After an authorized real restart verify no task resend, restored grants and notice continuation; sample foreground before probing tray ghosts (`get_foreground_window`, `list_tray_icons`). 单次采样不能证明整个过程无抢焦点 / A single sample cannot prove uninterrupted focus throughout.
- **自迭代循环**（AI 总控助手，需用户明确要求）：在 F5 调试 VSManager 且开启「任务完成自动跟进」时，对助手说「自己迭代改进 XX，最多 N 轮」，它调用 `start_self_iteration` 记下目标与轮次上限（默认 3，最多 10，状态存于 `%APPDATA%\VSManager\self-iteration.json`，24 小时过期），然后循环：向调试 VSManager 的 VS 发布开发任务 → 任务完成后读测试清单并自测重启 → 重启通知附带本轮说明，按工具测试结果 `mark_test_item`，全部通过即 `stop_self_iteration`，否则按失败证据发布修复任务再重启。每次成功预编译算一轮，达到上限后拒绝再重启；该 VS 中仍有执行中的任务时不会重启；需要用户观察的项仍列为「需用户测试」。随时可说「停止迭代」。
  **Self-iteration loop** (AI assistant, only on explicit request): with VSManager under F5 and "auto follow-up" enabled, ask the assistant to iterate on a goal for up to N rounds; it calls `start_self_iteration` (default 3, max 10 rounds; state in `%APPDATA%\VSManager\self-iteration.json`, expires after 24 hours) and loops: publish a task to the VS debugging VSManager → after completion restart for testing → the restart notice carries the round guidance; mark evidence-backed items, call `stop_self_iteration` when all pass, otherwise publish a fix based on the failures and restart. Each successful pre-build counts as a round and restarts are refused at the limit; no restart while that VS still runs a task; items needing observation remain for the user. Say "stop iterating" anytime.
- 日志：`%APPDATA%\VSManager\logs\agent.log`（AI 助手故障与重启）、`watchdog.log`（看门狗）、`crash.log`（未处理异常）。

### 解决方案登记与 VS 开关

**登记表**保存在 `%APPDATA%\VSManager\solutions.json`（独立于 settings.json，写入时保留 `.bak` 备份，主文件损坏时自动回退到备份并另存 `.corrupt-时间` 副本）。格式：

```json
{
  "_comment": "…",
  "Solutions": [
    {
      "Alias": "订单项目",
      "Path": "%USERPROFILE%\\source\\repos\\OrderSystem\\OrderSystem.sln",
      "Synonyms": [ "订单", "下单", "order" ],
      "Description": "可选说明",
      "DefaultVs": 0
    }
  ]
}
```

> 示例中的路径仅为示意，请配置 `.sln` / `.slnx` 完整路径；匹配、扫描及打开时支持展开环境变量。`DefaultVs` 为可选的 VS 编号（0 = 未设置），仅在该 VS 的当前解决方案路径与启动路径均未知时作为识别后备；不能覆盖已知路径。

**界面入口**：「属性 → 解决方案登记」卡片的「管理登记表…」、实例列表右键菜单「登记此解决方案」（一键登记已打开的 VS）与「解决方案登记…」。登记窗口支持新增 / 修改 / 删除、浏览选择解决方案、「从已打开的 VS 登记」、直接打开所选解决方案，并显示每条是否已打开及对应 VS 编号；新增「从目录扫描并登记」与「重新读取配置」入口。直接编辑配置文件后可重新读取，放弃未保存的界面修改前会确认。

**多路径与扫描**：`Solutions` 数组可保存多条记录，没有登记数量上限。扫描目录由用户指定，深度为 0–3，默认 3（根目录为 0）；跳过 `bin`、`obj`、`node_modules`、`.git`、`packages`、`.vs`、`TestResults`、`artifacts`、`dist` 及链接。扫描在后台执行，可取消；单次预算为 20 秒、5,000 个目录、50,000 个条目、2,000 个结果，达到任一限制会明确提示结果不完整。取消和时间限制不能强制中止正在进行的单次文件系统调用。候选默认不勾选，确认后才批量登记；以文件名为默认别名，同名自动加编号，重复路径跳过，已有说明与同义词不被覆盖。扫描上限不限制登记表的总容量。

**本机隐私**：登记表不会自动填入任何真实目录。文件及其备份、临时副本仅留在本机；忽略规则覆盖大小写变体。发布自检检查当前文件、索引及 HEAD 历史；发现登记表文件会直接阻止发布，不能通过普通的“确认继续”绕过。

**别名匹配规则**

1. 完整路径一致、别名完全一致 → 命中；同义词完全一致、文件名（不含扩展名）一致次之；
2. 去掉「解决方案 / 项目 / 工程 / 方案 / 代码 / solution / project / repo / 仓库」等通用后缀后一致（如「下单项目」→「下单」）；
3. 互相包含（至少 2 个字符）、按顺序出现的字符、说明中包含、二元组相似度等模糊规则得分较低；
4. 精确类匹配取并列最高分，模糊匹配取与最高分相差不足 10 分的候选；只有一条候选才直接使用，多条则列出供选择；无匹配时明确报错并列出全部已登记别名。

显式目录路径未命中时不回退到模糊别名；同路径的多条登记也返回候选。识别已打开 VS 时优先使用实际路径，其次是当前路径未知时的启动路径；仅凭标题识别要求实例唯一且登记文件名没有歧义。

**AI 工具**

| 工具 | 参数 | 说明 |
|---|---|---|
| `list_solutions` | 无 | 列出登记的别名、同义词、路径，以及是否已打开、对应 VS 编号 |
| `open_solution` | `solution`：别名或完整路径 | 已打开则只激活该 VS 窗口；否则确认后启动 VS 打开，并等待其出现（`SolutionOpenWaitSeconds`） |
| `close_vs` | `target`：VS 编号 / 名称或登记别名 | 先检查：Copilot 忙、有执行中任务、正在生成 / 调试、存在未保存修改或无法检查时拒绝并说明原因；通过后确认，再发送普通关闭请求（等同点击关闭按钮），绝不强制结束进程 |
| `list_vs` | 无 | 列出已打开的 VS、其解决方案及对应的登记别名 |
| `send_task` | `vs` 可填登记别名 | 目标 VS 未打开时任务进入「等待目标 VS」并暂存 |

**暂存与自动推送**：以下调度需要任务获得自动启动资格或本次会话手动 Start；默认新发布 AI 任务自动，恢复任务仍等待 Start，不能仅因打开 VS 而被放行。`send_task` 的目标是登记别名且对应 VS 未打开时，任务以 `waiting_vs`（等待目标 VS）状态写入 tasks.json（重启后仍保留），任务清单显示「⏳ 「别名」打开后自动推送」，并弹出通知 / 播报「任务已暂存，等待打开订单项目 / Task parked, waiting for 订单项目 to open」。调度器每 2 秒检查一次；无论 VS 由 `open_solution` 还是用户手动打开，只要检测到对应解决方案，就把任务转为排队（`waiting`），再等待 `PendingVsSettleSeconds` 秒后按正常流程发布。状态流转：`waiting_vs → waiting → sending → running → done`；`waiting_vs` 也可直接取消（`cancelled`）。

> 兼容性：旧版本 VSManager 读取到 `waiting_vs` 状态会把该任务视为已取消。

### 一键布局：集中查看 Copilot 对话

把各 VS 的 Copilot 对话窗格切换为浮动窗口，在指定屏幕（默认第二屏幕）按工作区宽度横向均布并置顶显示，同时最小化 VS 主窗口，只留下纯净的对话内容；还原布局时取消置顶。

- **入口**：实例列表右键菜单「一键布局：Copilot 对话 → 副屏横向均布（最小化 VS）」与「还原 Copilot 对话布局」；或对 AI 助手说“最小化所有 VS，把对话框排到副屏”。
- **排列规则**：每格宽度不小于 360 像素（按系统 DPI 缩放），一行放不下时自动换行并平均分配到各行；也可选网格排列。只有一块屏幕时排在该屏幕。
- **降级处理**：未连接自动化接口（DTE）、找不到或无法浮动对话窗格的 VS 会跳过并说明原因，不会被最小化；窗格未打开时会先自动打开。
- **还原**：执行前记录主窗口位置 / 最大化状态与窗格的停靠状态（仅保存在内存中，重启 VSManager 后不再可还原）；还原时先恢复主窗口，再把原本停靠的窗格放回原位。
- **说明**：浮动工具窗口归 VS 主窗口所有，主窗口最小化时 Windows 会一并隐藏它们，VSManager 会在最小化后以不激活的方式重新显示窗格。前台粘贴发送消息时可能会把对应 VS 恢复到前台。

| 工具 | 参数 | 说明 |
|---|---|---|
| `arrange_copilot_panes` | `screen`（屏幕编号，0 = 自动）、`layout`（`horizontal` / `grid`）、`minimizeVs`（默认 true）、`vs`（可选，如 `"1,3"`） | 一键布局；遵守「AI 操作需要确认」（`AgentConfirm`） |
| `restore_copilot_layout` | 无 | 还原一键布局之前的窗口布局；同样遵守 `AgentConfirm` |

### 显示器感知的 VS 工作区布局

点击总控助手「屏幕布局 / Layout」，或输入「先看看有几块屏幕，再自动安排所有 VS、Copilot 和输出栏」。助手先读取真实显示器信息，再布局，不需要用户先提供屏幕编号。也可以说「只布局 1、3 号 VS，主窗口放屏幕 1，Copilot、输出和错误列表放屏幕 2」。

| 工具 | 参数 | 说明 |
|---|---|---|
| `get_displays` | 无 | 只读返回屏幕数量、编号、分辨率、横竖屏、桌面位置、工作区、屏幕之间的相对位置（左 / 右 / 上 / 下）、主屏、当前前台窗口屏幕、VSManager 与各 VS 所在屏幕及当前窗口矩形；编号与属性一致 |
| `place_workspace_windows` | `layout`（JSON 数组，每项 `{"vs":"1","main":{"screen":1,"x":0,"y":0,"w":65,"h":100},"copilot":…,"output":…,"errorList":…,"solutionExplorer":…}`，矩形也可写 `[screen,x,y,w,h]`；x/y/w/h 为该屏工作区百分比） | AI 根据 `get_displays` 自行设计并摆放主窗口与窗格；`main` 必填，省略的窗格不移动；重叠或过小只警告；某个 VS 的自动化接口不可用（如文档未加载完时 `IVsPersistDocData` 返回 E_NOINTERFACE）时只把该 VS 或该窗格记为跳过并写明原因，其他 VS 照常摆放；遵守 `AgentConfirm`，可用 `restore_workspace_layout` 还原 |
| `arrange_workspace_layout` | `vs`（逗号分隔编号/名称，空为全部）、`mainScreen` / `paneScreen`（0 自动）、`includeOutput`（true）、`includeErrorList`（true）、`includeSolutionExplorer`（true） | 按内置规则自动布局 VS 主窗口、Copilot 和所选附属窗格（用户明确要求默认布局时使用）；遵守 `AgentConfirm` |
| `restore_workspace_layout` | 无 | 还原这套工作区布局；遵守 `AgentConfirm`，失败项保留供重试 |

「屏幕布局 / Layout」快捷按钮让 AI 先读取全部屏幕的尺寸与相对位置，再自行设计布局并用 `place_workspace_windows` 摆放，每个 VS 的 Copilot、输出、错误列表与解决方案资源管理器一并安排（尚未创建的内置窗格会被创建，还原时恢复隐藏）。布局优先级：按各屏实际尺寸、方向与主屏属性（不是屏幕编号）判断用途，`get_displays` 会给出「建议用途」并标注过小的屏幕。主屏留给 VSManager，VS 主界面可以放入主屏；所有 AI 助手（Copilot 对话）尽量集中在一块尺寸足够大的非主屏，不放到尺寸过小的屏幕（工作区不足约 600x900 像素，如 2560x734 的窄条屏）；解决方案资源管理器与所属主窗口同屏相邻；输出与错误列表优先使用第三屏（较小的屏幕也可用于输出）。屏幕不够则 AI 对话在上、输出与错误列表在下共用一屏；只有一屏或空间仍不足，由 AI 根据尺寸、横竖屏与窗口数量自行决定，优先可读性与不重叠，并说明取舍。用户明确指定的位置优先。
The "屏幕布局 / Layout" quick button reads every screen's size and relative position and applies an AI-designed layout with `place_workspace_windows`, including each VS's Copilot, Output, Error List and Solution Explorer (built-in panes not yet created are created and hidden on restore). Priorities: screen roles are judged by actual size, orientation and the primary flag rather than screen numbers; `get_displays` reports suggested roles and marks screens that are too small. The primary screen is kept for VSManager and VS main windows may use it; all AI assistants (Copilot chats) stay together on one sufficiently large non-primary screen and never on a too-small one (work area under about 600x900 pixels, such as a 2560x734 strip); each Solution Explorer sits beside its own main window on the same screen; Output and Error List prefer a third screen (a smaller screen is fine for output). With fewer screens, AI chats stack above Output and Error List on a shared screen. With only one screen or insufficient space, the AI decides based on sizes, orientation and window count, prioritizing readability and avoiding overlaps, and explains the tradeoffs. Explicit user placements take precedence.

`arrange_workspace_layout` 的内置默认布局按尺寸与属性分配屏幕：主窗口使用主屏（与 VSManager 同屏；主屏被显式指定给对话时改用当前前台窗口所在屏或其余最大屏），每个主窗口左侧约 22% 留给资源管理器；Copilot 使用工作区不小于约 600x900 像素的非主窗口屏中最大的一块，没有合适屏幕时与主窗口同屏分区（左侧约 65% 主窗口与资源管理器、右侧对话）；输出与错误列表使用剩余屏幕中最大且高度不低于约 300 像素的一块，没有时放在对话下方（对话占上部约 65%）。显式 `mainScreen` 固定主窗口及资源管理器所在屏，显式 `paneScreen` 固定 Copilot、输出与错误列表所在屏；关闭的可选窗格不占区域。空间不足会警告，AI 可用 `place_workspace_windows` 继续调整，不强制沿用默认比例。坐标使用桌面像素，保留负坐标并避开任务栏；允许最多 2 像素的 DPI 舍入，更大的位置偏差或最小尺寸限制会如实报告。

布局时不会最小化 VS，会恢复原先最小化的主窗口参与布局；还原时恢复原显示状态。不保存或关闭文件，不处理任意其他工具窗格；无法确认目标、存在模态对话框、DTE 不可用或窗格缺失时跳过并报告，不猜测原状态或强制打开缺失窗格。审批后显示器或目标窗口改变时不执行旧计划。布局快照仅在当前 VSManager 会话内有效，精确停靠组位置由 VS 管理；恢复后再切换到旧 Copilot 单独布局模式，避免互相覆盖。已有只排列 Copilot 的工具与入口保留。

### CAD 插件调试自动加载 DLL

点击「▶ 调试」（或由 AI 助手 / Web 远程触发开始调试）且 VS 处于设计模式时，会检查启动项目的调试启动程序：项目调试属性「启动外部程序」或 `launchSettings.json` 当前配置（`commandName: Executable`）的可执行文件为 `acad.exe`（AutoCAD 及其行业版）、`zwcad.exe`、`gcad.exe` 或 `bricscad.exe` 时，判定为 CAD 调试环境。

- 在 `%TEMP%\VSManager\CadDebug\` 生成启动脚本，内容为 `(command "_.NETLOAD" "启动项目输出 DLL")`，并把 CAD 标准启动参数 `/b "脚本"` 临时加到原参数前；CAD 打开后自动加载要调试的 DLL，调试器从启动开始就已附加，断点正常命中。
- **FILEDIA**：系统变量 FILEDIA 为 0 时无法自动加载 DLL。点击调试时，VSManager 先检查启动程序对应的 AutoCAD 配置（注册表 `HKCU\Software\Autodesk\AutoCAD\<版本>\<产品>\FixedProfile\General Configuration` 的 `FileDialog`），为 0 时在启动前改为 1，状态栏会说明；无法确定对应安装时处理全部为 0 的 AutoCAD 配置。启动脚本首行还会执行 `(if (= (getvar "FILEDIA") 0) (setvar "FILEDIA" 1))` 兜底，ZWCAD / GstarCAD / BricsCAD 同样生效。FILEDIA 为 1 时不做任何修改。
- 调试器进入运行 / 中断状态、生成结束后未启动、VS 断开或 15 分钟超时后，恢复原启动参数（`launchSettings.json` 按原字节写回；期间被改动则只去掉本工具加入的参数）；退出 VSManager 时也会恢复。异常残留的参数在下次调试时自动替换，不会叠加。
- 原参数已含 `/b` 脚本、启动项目不输出 DLL、已在调试中（继续运行）或不是 CAD 时保持原样，状态栏说明原因。开关位于「属性」的「发送确认」卡片中的「CAD 调试自动加载 DLL」，默认开启。
- **调试图纸**：把图纸路径或 `.dwg` / `.dxf` 附件发给 AI 总控助手（例如「#2 的调试图纸是 %USERPROFILE%\Documents\测试.dwg」），助手会用 `set_cad_debug_drawing` 按该 VS 的解决方案记录下来（`get_cad_debug_drawing` 查看，发送空路径清除；开启审批时需确认）。之后点击调试时把图纸作为 CAD 启动参数一并传入（`"图纸" /b "脚本"`），CAD 打开该图纸并在其中 NETLOAD；未记录或图纸已不存在时不传图纸，CAD 按默认打开新图，状态栏会说明。原启动参数已指定图纸时以原参数为准。以附件记录时使用附件副本，如需保存回原文件请直接发送路径。
- DLL 不在 CAD 可信位置时，AutoCAD 会弹出安全提示，请选择加载（或自行把输出目录加入 `TRUSTEDPATHS`）；本工具不修改 `SECURELOAD` 等安全设置。

### CAD 动作执行器（ai.exe）

用于让 AI 总控助手自动执行任务清单中的「待验证」项。组成：`src\VSManager.AiHost`（ai.exe，不持有模型的哑调度器）、`src\VSManager.CadAgent`（动作协议与 CAD 侧代理）、`adapters\_template`（项目适配包模板，含中英 SKILL.md）。

- **适配包**：复制 `adapters\_template` 到 `%APPDATA%\VSManager\adapters\<名称>\`，在 `adapter.json` 中填写匹配的解决方案名、命令映射表、日志路径与启动配置（CAD 路径、附加 DLL、启动命令、启动参数、默认图纸）。换项目只需新增适配包，不改 ai.exe 与 VSManager。
- **流程**：开启 Web 远程 → 点击调试启动 CAD（匹配适配包时自动编译并 NETLOAD 引导 DLL，CAD 中的代理经本机 Web API 上线；命令 `VSM_AIAGENT` 查看状态）→ AI 助手调用 `run_cad_actions` 把动作序列交给 ai.exe → 逐条下发、汇总回传 → 助手对照判定依据判定或请用户确认。`list_cad_adapters` 查看适配包与连接状态。
- **动作 v1**：`openDrawing`、`switchDrawing`、`closeAllDrawings`、`runCommand`、`getParam`、`screenshot`、`getLog`、`getEntityCount`；统一入参 `vs / timeoutMs / action / args`，统一返回 `ok / errorCode / message / artifacts / durationMs`。未指定图纸时用已记录的调试图纸，图纸不存在时打开新图并说明。
- **规则与安全**：每条默认超时 60 秒、连接类错误重试 1 次，超时或失败即停止序列（后续标记 SKIPPED）；CAD 崩溃返回 `CAD_GONE`，不自动重启；同一时刻只驱动一个 CAD。`runCommand` 只能执行适配包命令映射表中的命令，`getLog` 只读适配包声明的日志；截图与日志只在内存中回传并在结果窗口展示，不写入用户目录；CAD 接口只接受本机请求；开启「操作前确认」时执行前需确认。
- **项目自带验证接口（本机 IPC）**：目标项目可以把程序目录 `sdk\VsmVerify.cs`（与 `VSManager.CadAgent.dll` 中的 `VSManager.Verify` 相同，只依赖 .NET Framework 4.x，C# 6 语法）加入插件工程，在进程内登记检查项：
  ```csharp
  VerifyEndpoint.Start("示例插件", "Demo.Plugin")          // 第二个参数为解决方案名（不含扩展名）
      .Register("entityCount", "图层上的实体数", ctx =>
          VerifyOutcome.Pass("数量正确").With("count", "12"), "layer=图层名");
  // 需要在 CAD 主线程执行时设置 Invoker，把检查封送到主线程。
  ```
  端点在 `\\.\pipe\VSManager.Verify.<进程ID>` 上监听，仅允许当前用户、拒绝网络登录，不需要 Web 远程与令牌。AI 助手调用 `list_verify_checks` → ai.exe `verify list` 发现端点（归属：该 VS 调试器附加的进程，或端点声明的解决方案名与 VS 解决方案一致），再调用 `run_verify_check` → ai.exe `verify run` 执行检查，返回 `pass / fail / inconclusive / error`、说明、证据与明细；只有 pass 且证据满足判定依据才可勾选测试项。每个检查默认超时 60 秒（1–600 秒），同一端点同一时刻只执行一个检查，超时的检查结束前返回 `BUSY`；ai.exe 会校验管道服务端进程 ID，拒绝冒名管道。目标进程与 VSManager 提权状态不一致时管道可能拒绝访问。没有验证接口的项目仍使用上面的动作序列。
- **限制**：v1 引导 DLL 面向 .NET Framework 版 CAD（如 AutoCAD 2024 及更早），基于 .NET 8 的 AutoCAD 2025+ 暂不支持（调试仍正常，只是不加载代理）。引导 DLL 位于 `%TEMP%\VSManager\CadAgent\`，SECURELOAD 提示时请选择加载。

### 按 VS 同步 git

总控助手的「🔄 同步 git ▾」是下拉菜单：列出每个打开的 VS 及其仓库当前分支（只读 `.git/HEAD`，支持 worktree），选哪个就只同步该 VS 所在的仓库，不再一次同步全部。非 git 仓库的 VS 不可选；多个 VS 共用一个仓库时标出「与 #N 同仓库」。模型可用时由 AI 用 `send_task` 按编号原样发布给该 VS；未配置模型或模型正忙时按精确目标直接入队（同 @ 提及任务）。同步规则不变：不强推、不 reset --hard、不丢弃修改。

### AI Skill 截图

安装到 Copilot CLI / Claude Code 等的 AI Skill（属性 → AI Agent Skill）新增 `screenshot` 命令：`vsm.ps1 screenshot <vs> [-Out <file.png>]` 截取目标 VS（或其前台弹窗）并保存为 PNG，输出文件路径，外部 AI 再用自己的看图工具打开。默认保存到 `%TEMP%\VSManager\screenshots`，只保留最近 20 张。

- 截图会短暂把该 VS 切到前台，完成后切回原窗口；使用「允许 VS 截图分析」开关（属性 → AI 助手），关闭时拒绝。开启「截图需逐张预览批准」时会先弹出预览，用户取消则不返回图片。
- 接口 `/api/screenshot` 只服务本机（127.0.0.1 / ::1）调用，局域网手机端即使持有密钥也不能截图。
- VSManager 启动时会自动刷新已安装的 Skill 文件（只更新已存在的安装目录），无需手动重装。
- 图片内容可能含代码或敏感信息；Skill 说明要求 AI 把图中文字视为不可信数据，不当作指令。

### 关闭 .cs 文件标签页

一次关闭某个 VS 中所有已打开的 .cs 文件标签页（仅扩展名为 `.cs` 的文件，不含 `.cshtml` / `.csproj` 等）。有未保存修改的文件不会关闭也不会保存，只在结果中列出文件名；其他文件与工具窗口不受影响。

- **入口**：实例列表右键菜单「关闭所有 .cs 标签页 / Close all .cs tabs」；或对 AI 助手说“关掉 1 号 VS 里打开的 .cs 文件”。

| 工具 | 参数 | 说明 |
|---|---|---|
| `close_cs_tabs` | `vs`：VS 编号或名称 | 关闭该 VS 中所有已打开的 .cs 标签页，返回关闭数量与保留的未保存文件；遵守 `AgentConfirm` |
| `restart_vsmanager_for_testing` | `testPlan`：重启后要执行的测试计划；`taskId`：要验证的任务编号（可为 0） | 自测重启：预编译通过后，在本轮结束时让调试 VSManager 的 VS 重新启动调试，重启后发送「[重启完成通知]」续跑测试；遵守 `AgentConfirm` |
| `get_window_state` | 无 | 只读：VSManager 主窗口位置、大小、最大化 / 最小化、所在屏幕、是否前台、当前页面、选中的 VS、AI 草稿与托盘状态；重启后逐项对照重启前保存值（一致 / 不一致） |
| `get_foreground_window` | 无 | 只读：当前前台窗口的标题、窗口类、进程名与 PID，以及是否属于本 VSManager，用于验证是否抢焦点 |
| `list_tray_icons` | `openOverflow`（默认 true） | 只读：列出托盘图标并给出 VSManager 托盘残影结论；Windows 10 可得所属进程与失效窗口，Windows 11 经 UI 自动化读取（会短暂展开「显示隐藏的图标」再收起并交还前台） |
| `read_restart_handoff` | 无 | 只读：`restart-ui.json` / `restart-handoff.json` 的内容与消费状态（文件不存在通常表示已被新进程读取删除），以及本进程启动时实际恢复了什么 |
| `read_vsmanager_log` | `name`：日志名（`tasks`、`send`、`watchdog`、`cad`、`mcp`、`memory`、`crash` 等）或文件名；`lines`：末尾行数（默认 200，最多 2000）；`date`：可选 `yyyy-MM-dd`（默认当天） | 只读：读取 VSManager 自身日志，返回日志文件路径（用户目录显示为 `%APPDATA%` 等环境变量）、总行数与末尾 N 行原文，按文件工具的现有规则脱敏。在 `%APPDATA%\VSManager\archive\logs`（`send-日期.log` 等归档日志，多分卷时取最后一卷）与 `%APPDATA%\VSManager\logs`（`tasks.log`、`watchdog.log` 等）中查找；按天分文件的日志取该日文件，不分天的日志给出日期时只取该日记录。只接受文件名与 .log / .txt，`agent.log`、`file-audit.log` 不开放；找不到时列出可用日志名。用于核对「已按测试项文字重判 N 个测试项的可验证性」「【执行方式】请按自动推荐的提示词执行」等记录是否存在 |
| `read_agent_chat` | `lines`：末尾轮数（默认 20，最多 200）；`since`：可选 `yyyy-MM-dd HH:mm`，只返回该时间之后的轮次与启动记录 | 只读：读取 `%APPDATA%\VSManager\agent-chat.jsonl` 与 `plan.log`。第一部分按轮列出轮次序号、时间、用户消息 / 通知摘要（脱敏并截断到 160 字）与该轮实际调用的工具名（如 `create_plan`、`update_plan_step`、`read_plan`、`send_task`，重复调用记为 ×N）；第二部分列出本进程（★）与历次启动读回的执行计划：启动时间、读回计划数、续跑的计划编号与标题、是否发出「执行计划恢复」通知（单独通知或并入重启完成通知）。用于核对某轮是否真的调用过某工具、重启后是否读回计划 |
| `create_plan` | `title`：计划标题；`steps`：步骤列表（2–30 步，按执行顺序）；`goal`：可选，目标与验收标准 | 为复杂流程（多步骤、跨重启、步骤间有依赖，如补 skill 闭环、自迭代、多阶段验证）创建执行计划，写入 `%APPDATA%\VSManager\agent-plans.json`，常驻直到 `complete_plan`；同名进行中的计划不重复创建，最多 5 个进行中的计划；简单请求不要建计划 |
| `update_plan_step` | `step`：第几步（从 1 开始）；`status`：`pending` / `in_progress` / `done` / `failed` / `skipped`（也接受「完成」「进行中」等中文）；`note`：可选说明；`planId`：只有一个进行中的计划时可省略 | 更新某一步的状态与说明并立即写盘，返回计划进度与下一步；全部完成时提示调用 `complete_plan` |
| `read_plan` | `planId`：可选，0 表示全部 | 读回进行中的执行计划：步骤、每步状态与说明、下一步 |
| `complete_plan` | `summary`：结果总结；`planId`：可选；`force`：可选，强制释放 | 流程完成后释放计划（从文件中移除）；有未完成步骤时拒绝，确需放弃时 `force=true` 并写明原因 |
| `prepare_restart_scenario` | `page`、`vs`、`draft`、`window`、`screen`、`foreground`（均可选，至少一项） | 场景补齐：切到 AI 总控页或某个 VS 对话页、写入 AI 输入草稿（已有用户草稿不覆盖）、最大化 / 还原 / 最小化、移到第 N 块屏幕、把前台切给其他应用或 VSManager；保留 10 分钟，`restart_vsmanager_for_testing` 在保存界面状态前再应用一次并写进重启完成通知；多次调用会合并（未填的项沿用上一次），用户发送消息清空的草稿在重启前重新写入 |
| `list_test_checklists` | `taskId`（0 表示全部） | 只读：列出全部「待验证」任务（不限最近几条）的完整测试清单，每项带序号（与 `mark_test_item` 一致）、勾选状态与 [AI] / [人工] 标注；不入队、不发布任务 |
| `mark_test_item` | `taskId`、`item`（从 1 开始）、`passed`、`evidence`（必填依据） | 勾选 / 取消勾选待验证任务的测试项，全部勾选后任务标记为完成；标为「[人工]」的项拒绝勾选；依据写入 tasks.log；遵守 `AgentConfirm` |
| `start_self_iteration` | `goal`（目标与验收标准）、`maxRounds`（默认 3，最多 10） | 用户明确要求时开始自迭代循环，需 F5 调试与「任务完成自动跟进」；返回调试 VSManager 的 VS；遵守 `AgentConfirm` |
| `start_skill_gap_loop` | `taskId`、`item`、`skill`（需要的新 skill）、`reason`（现有工具为何验证不了）、`maxRounds`（默认 3，最多 10） | 补 skill 闭环，由 AI 自动发起、无需用户提醒：某测试项用现有工具验证不了、但新增一个读取机器可读状态的 skill 就能自动验证时，开始一轮专用自迭代——发布实现任务 → 重启加载 → 用新 skill 验证并勾选（即使标为人工），失败带证据修复。拒绝必须人眼 / 人手的项；每项只发起一次；与自迭代互斥 |
| `stop_self_iteration` | `summary`（可选） | 结束自迭代，报告已用轮次 |

### 任务回执

任务清单派发的每条任务都有本轮回执 ID（GUID），Copilot 在最终回复最后一行输出三选一的回执：`SUCCESS`（已完成且已验证）、`UNVERIFIED`（改动已完成，但尚未实际验证或需要用户测试 / 确认，显示为「待验证」；旧回执 `NEEDS_USER` 仍按待验证识别）、`FAILED`（任务本身未完成；无关的遗留问题不算失败）。

回执规则附在每条任务消息的末尾。VS 2026 的 Copilot 代理（内置 Copilot CLI）不会加载 `copilot-instructions.md` 等自定义指令文件，所以规则不能靠指令文件下发，每条任务都会带上完整规则。

回执规则之前还附有一条执行方式「【执行方式】请按自动推荐的提示词执行」：过程中出现自动推荐的提示词（建议的下一步 / 后续操作）时，Copilot 直接按推荐内容继续，把任务推进到完成，不停下来询问或等待确认；只有确实无法继续时才停下并说明需要用户提供什么。所有发布的任务（AI 发布、@ 直发、手动与重试）都会带上这条。
Before the receipt rules every task also carries an execution rule, "follow the automatically suggested prompts": when suggested prompts (recommended next steps / follow-ups) appear, Copilot continues with them and drives the task to completion without stopping to ask or wait for confirmation, and stops only when it truly cannot continue, saying what the user must provide. Every published task (AI-published, @ direct, manual and retries) carries it.

### 接续等级

任务清单顶栏有一个四档滑块（点击、拖动或 ←/→ 键切换，保存在 settings.json 的 `TaskContinueLevel`），决定同一 VS 的前序任务以什么结果结束时自动执行下一项。挡位名表示「哪种结果会阻塞队列、等你处理」，避免需要你处理的内容被后续任务覆盖对话上下文：

| 挡位 | 已完成 | 待确认（待验证） | 失败 |
| --- | --- | --- | --- |
| 「已完成」`completed` | 放行 | 阻塞 | 阻塞 |
| 「待确认」`needs_user` | 放行 | 阻塞 | 放行 |
| 「失败」`failed` | 放行 | 放行 | 阻塞 |
| 「不限」`unlimited`（默认） | 放行 | 放行 | 放行（失败记录保留） |

- 排队中 / 发送中 / 执行中的前序始终阻塞后续；已取消的不阻塞。旧版「跳过失败前序任务」开关仍可用：开启 = 「不限」，关闭 = 「失败」。旧配置（`TaskReleaseLevel` 三档）会按原行为自动迁移：旧「失败」→「不限」，旧「待验证」→「失败」，旧「已完成」不变。
- 待确认与失败的任务会分别记录「待处理内容」与「失败原因」（回执规则要求 Copilot 以「待处理：」「失败原因：」开头单独成段，没有时取回复最后一段；投递、读取失败等按失败类别记录），卡片上直接显示摘要；点击该条目时，任务清单底部会展开详情区显示全文与处理方式，可选中复制，点 × 关闭。AI 助手收到的通知与任务列表中也包含这两项。
- 被暂停时，在任务清单右键失败 / 待验证的条目：「补充信息后重试…」把补充内容连同前次反馈发回原 VS（每个任务最多 3 次）；「放行后续任务」保留该条结果，让后续继续执行。
- AI 助手收到失败通知后自行判断：能从 VS 返回的信息补齐时调用 `retry_task_with_info` 补充重试；需要用户决定或补充时，把失败原因与所需信息告诉你，由你补充、放行（`release_task`）或取消。任务阻塞时，你在对话中给出的补充、修正或验证反馈会通过 `retry_task_with_info`（`from_user=true`，不受 AI 自主重试次数限制，需你确认）发给阻塞任务本身并在原条目重试；AI 向被阻塞的 VS 用 `send_task` 发布新任务时默认不入队，而是提示改为补充阻塞任务（确实无关的新任务可设 `queue_behind_blocked=true` 排在其后）。你在任务清单中手动「补充信息后重试」也不再受次数限制。也可以让它用 `set_release_level` 调整等级。开启「AgentConfirm 审批」时这些工具都需要确认。
- 防止循环消耗用量：同一需求（重发链 + 补充重试）由 AI 自主触发的 Copilot 执行次数有上限，在「设置 → 发送确认 → AI 重试上限」调整（默认 3，范围 1–10）；原样或只加「请再试一次」的重发会被拒绝。投递失败、VS 关闭、读取失败和「Copilot 本轮未执行完」（网络 / 服务错误、被中断）不计入次数，AI 可用 `retry_task` 重试，每个任务最多 5 次。你在任务清单里手动重试不受限制。
- 失败时读取完整回复：任务失败时，VSManager 会保存本轮 Copilot 的完整回复（最后一条任务消息之后的全部回答与过程步骤，不只是最后一行状态），失败通知附上全文（过长时为开头与结尾摘录，AI 可用 `read_task_reply` 分页读取全文）。回复结尾出现返回中断 / 未预期的 EOF、返回体或上下文过大、达到单轮迭代上限、网络 / 服务错误时，即使回复很长也判为「Copilot 本轮未执行完」，不计入执行次数。AI 先阅读全文找原因并补充内容：中断类用 `retry_task` 重试，重试会自动提示 Copilot 在已有进度上继续，需要调整做法（如分步完成、减少输出）时写在 `note` 中；内容类用 `retry_task_with_info` 补充信息重试；确实无法处理时才交给你。完整回复随任务保存在 `tasks.json`，重新排队后清除。失败日志也会读取：Copilot 回复中折叠的过程步骤（如 Autopilot 重试、命令执行等）会被临时展开，读取每段日志最顶层的内容（每步最多 20 行 / 1500 字符，每个文本块 8 行），这里往往是本轮失败的主要原因；同时读取界面上可见的 Copilot 提示（如「此响应被截断，因为它太长了」），读完后恢复折叠，思考过程不展开。
- 重试说明整合而非堆叠：重试时轮次、前次尝试反馈、补充信息与接续说明合并为一段，只给一次处理要求（补充信息与前次反馈冲突时以补充信息为准）。`retry_task_with_info` 的 `replace_previous=true` 表示 info 是主控 AI 按用户意图整合后的完整说明，替换此前累积的补充、前次反馈与接续说明；`fresh_context=true`（`retry_task` 也支持）表示 Copilot 对话已清空或换成新线程，Copilot 会先重新阅读相关代码、文档与 Git 状态了解进度，而不是依赖已不存在的对话。任务菜单「补充信息后重试」对话框也提供这两个开关。
- 补充排队中的任务：任务还在排队（等待发布或等待 VS 打开）时，右键「补充要求（合并到此任务）…」或让 AI 调用 `retry_task_with_info`，补充要求会合并到原任务，发送时以「【补充要求】」附在任务内容之后一并发给 Copilot，不会另起一条内容重复的新任务，也不计入补充次数；任务已开始发送时不再合并，对话框中的内容会复制到剪贴板，待任务完成后可再「补充信息后重试」。
- 任务自动接续（「属性 → AI 助手 → 任务自动接续」，默认开启，需要「任务完成自动跟进」）：任务返回待验证、或已完成但回复提到还有剩余步骤（如「尚未完成」「剩余步骤」「下一步需要」「TODO」）时，通知附「[自动接续]」说明，AI 助手先验证 [AI] 项，再自己判断剩余步骤：目标 VS 能完成的剩余工作用 `continue_task` 向同一 VS 发布接续任务（正文自动附原任务摘要与上一轮结果，只做剩余步骤），形成闭环而不停下来等你；[AI] 项不通过属于本次改动本身的问题时仍用 `retry_task_with_info`；只剩 [人工] 项或需要你提供信息 / 授权时不接续，改为告诉你。每个任务只接续一次，每条接续链最多 3 次；原任务阻塞同一 VS 时自动放行（测试清单保持待验证），接续任务按编号排在该 VS 已排队任务之后。用户直接发布的任务待验证时同样会通知 AI 判断接续。

## 发布到 GitHub

点击主窗口顶部的「🚀 发布」打开发布窗口，流程为：检查 git → 未初始化时 `git init` → 补齐 `.gitignore`（排除 bin/obj/dist、settings.json、tasks.json、日志、归档目录）→ 敏感信息自检 → `git add` → 提交（中英双语提交信息）→ 创建或关联远程仓库 → `git push`。

- **Token**：在发布窗口填写（DPAPI 加密保存），或设置环境变量 `VSMANAGER_GITHUB_TOKEN`。Token 只在内存中通过 HTTP 头传给 git，不会写入远程地址、`.git/config`、日志或界面。
  - fine-grained Token：仓库权限 **Contents：读写**；需要自动创建仓库时再加 **Administration：读写**（组织仓库需组织授权）。
  - classic Token：`repo` 范围（仅公开仓库可用 `public_repo`）；推送 `.github/workflows` 还需要 `workflow`。
- **敏感信息自检**：扫描所有待提交文件以及提交信息、提交作者，规则包括盘符绝对路径、当前用户名与机器名、邮箱（noreply 与 example 域名除外）、常见 Key/Token 格式与疑似密钥赋值、本机已配置的密钥，以及自定义词表 `%APPDATA%\VSManager\publish-scan-terms.txt`（每行一个，适合填写内部项目名、客户名，文件不会提交）。有命中时发布暂停并列出「文件:行号 + 命中内容」（密钥已打码），由你确认继续或取消；「仅自检」只扫描、不修改仓库。
- **日志**：`%APPDATA%\VSManager\logs\publish-yyyyMMdd.log`。失败时界面会给出原因与修复建议；远程已有本地没有的提交时不会强制推送。

## 分支策略

| 分支 | 用途 | 合并方式 |
|---|---|---|
| `main` | 默认主分支，始终可构建、可发布；每个版本打标签（如 `v1.0.0`） | 只接受来自 `develop`（发布）或 `fix/xxx`（紧急修复）的合并 |
| `develop` | 集成分支，汇总已完成的功能与修复 | 接受 `feature/xxx`、`fix/xxx` 的 Pull Request |
| `feature/xxx` | 新功能，从 `develop` 创建 | 完成后向 `develop` 发起 Pull Request |
| `fix/xxx` | 缺陷修复，一般从 `develop` 创建；线上紧急问题从 `main` 创建 | 合并回来源分支；从 `main` 创建的修复还需同步合并到 `develop` |

```powershell
git switch develop; git pull
git switch -c feature/memory-panel
# ……开发、构建、测试 / develop, build, test……
git push -u origin feature/memory-panel   # 然后在 GitHub 上向 develop 发起 Pull Request
```

- 推送前先 `git pull` 拉取远程最新内容；**不要强制推送**（`--force`）到 `main` 与 `develop`。
- 提交信息格式为「类型: 简述」，中英双语，详见 [CONTRIBUTING.md](CONTRIBUTING.md)。
- 发布前使用「🚀 发布 → 仅自检」做敏感信息自检，确认无命中后再提交。

## 常见问题

- **看不到某个 VS 实例？** VSManager 与 VS 需以相同权限运行（都以管理员或都不以管理员运行），并且 VS 已完全加载解决方案。
- **Copilot 状态一直是「未知」？** 确认已安装 GitHub Copilot 并打开过 Copilot 对话窗格；若窗格标题不同，可在「属性」中修改 `CopilotPaneKeyword`。
- **发送失败并提示粘贴未确认？** 右键 VS →「查看发送日志」，每次失败都会记录「粘贴确认诊断」（目标 VS、窗口状态、窗格 / 输入框位置与焦点、读取到的文本片段、剪贴板与耗时）。常见原因：VS 被模态对话框阻挡、剪贴板被同步工具改写、超长消息粘贴较慢（可在「属性 → 发送确认」调大超时）。
- **发送失败并提示「未找到 Copilot 输入框 / 对话窗格 / 输入框不可编辑」？** 输入框按 L1（WpfTextViewHost）→ L2（对话列表外最靠下的 WpfTextView）→ L3（最靠下的可编辑文本元素）→ L4（旧方式，需可编辑）→ L5（位置命中测试）逐级降级定位，每级的候选数量、名称、AutomationId、是否可编辑与耗时都写入发送日志，最终失败时还会记录窗格结构。长时间的 Copilot 回合刚结束时窗格的 UI Automation 树可能暂未刷新，程序会带退避轮询并重新打开窗格重试；仍失败时请切换到该 VS 单击一次输入框，或在「属性 → 发送确认」调大定位超时 / 重试次数。「不可编辑」通常表示 Copilot 正等待你确认操作。
- **AI 助手没有回复 / 提示未配置？** 在「属性 → AI 总控助手」中填写 API Key（或设置 `VSMANAGER_AGENT_API_KEY`），并确认接口支持函数调用。
- **`dotnet restore` 失败？** 本机 NuGet 配置中可能有不可用的源，执行 `dotnet restore VSManager.slnx --source https://api.nuget.org/v3/index.json`。
- **生成时提示 VSManager.exe 被占用？** 程序正在运行时，请先退出（托盘 → 退出），或把输出指定到临时目录：`dotnet build VSManager.slnx "-p:OutputPath=%TEMP%\vsm-build\"`。
- **推送到 GitHub 失败？** 检查 Token 权限（classic：`repo` 或仅公开仓库的 `public_repo`；fine-grained：Contents 读写）与网络；远程有新提交时先 `git pull`，工具不会强制推送。
- **配置或任务丢失？** 配置在 `%APPDATA%\VSManager\settings.json`，损坏时另存为 `settings.json.corrupt-*`；任务清单在 `tasks.json`，历史归档在 `<ArchiveRoot>\tasks\`。
- **重新发布失败任务后，原失败条目不见了？** 这是 `AutoHideResentFailedTasks`（默认开启）的行为：新任务正文规范化（统一换行、去掉每行首尾空白与空行、合并连续空格、去掉零宽字符）后的 SHA-256 指纹与某条更早的失败任务相同、且目标 VS 相同时，原条目只在界面隐藏。正文过短（少于 12 字符）或目标不同时不会隐藏，原因写入任务日志；正文以「重发 #26：」开头或以「（重试 #26）」结尾时去掉标记后比对，不受长度限制。点任务清单顶部「历史」可查看，右键「恢复显示该失败条目」或「撤销清除」可恢复。

## 安全提示

- Web 远程控制默认关闭；开启后会在局域网内监听端口，凭访问令牌控制所有 VS，只应在可信网络中使用。令牌可以在「属性」中重置。
- AI 助手会把 VS 名称、职责描述、对话内容和代码片段发送给你配置的模型服务商；语音功能会把播报文本发送给豆包语音。请根据所在组织的数据政策选择服务商。

## 第三方依赖

| 组件 | 许可证 |
|---|---|
| [Markdig](https://github.com/xoofx/markdig) | BSD-2-Clause |
| [Microsoft.Extensions.AI / Microsoft.Extensions.AI.OpenAI](https://github.com/dotnet/extensions) | MIT |
| [OpenAI .NET SDK](https://github.com/openai/openai-dotnet)（间接依赖） | MIT |
| [Microsoft.Web.WebView2](https://www.nuget.org/packages/Microsoft.Web.WebView2) | Microsoft WebView2 SDK 许可（BSD 风格，允许再分发） |
| [NAudio.WinMM](https://github.com/naudio/NAudio) | MIT |

二维码编码器（`QrCode.cs`）与应用图标（`app.ico`，渐变底色 + 文字）均为本项目自行制作，随本项目按 MIT 许可证发布。使用 DeepSeek、豆包语音等在线服务时，需另行遵守各服务商的服务条款。

## 贡献指南

欢迎提交 Issue 与 Pull Request，完整流程见 [CONTRIBUTING.md](CONTRIBUTING.md)，版本变更见 [CHANGELOG.md](CHANGELOG.md)。要点：

- 本项目是开源项目：README、文档、代码注释、提交信息与发布说明中不要出现个人信息（真实姓名、邮箱、机器名、用户名、本机盘符路径、公司 / 客户信息），示例路径请使用 `%APPDATA%` 等环境变量或通用示例。
- 开源说明文档与代码注释提供中英两份（中文在前、英文在后，或并列呈现）。
- 功能开发使用 `feature/xxx`，修复使用 `fix/xxx`，向 `develop` 发起 Pull Request；提交前构建 0 错误、单元测试全部通过。

## 声明

本项目为独立的开源工具，与 Microsoft、GitHub 及文中提到的各服务商无隶属或背书关系。Visual Studio、GitHub Copilot 等名称为其各自所有者的商标。

## 许可证

本项目以 [MIT 许可证](LICENSE) 发布：可自由使用、修改与再分发，需保留版权与许可声明；软件按「原样」提供，不附带任何担保。第三方组件遵循各自的许可证（见上表）。

---

# VSManager · Multi Visual Studio Manager (English)

VSManager is a Windows desktop tool (WinForms / .NET Framework 4.8) for managing several Visual Studio instances on one machine together with their GitHub Copilot chats.

## Features

- **Instance overview**: discovers running Visual Studio instances and shows the solution, debug state and whether Copilot is busy or idle; one-click layout across monitors.
- **In-app Copilot chat**: VS thread pages display live Markdown replies and retain Stop Copilot, open-chat and debug controls. There is no bottom composer; send text and attachments through the manager assistant's Direct action.
- **Debug control**: start / stop / break / restart debugging, build / rebuild, read the error list.
- **AI assistant**: works with any OpenAI-compatible endpoint (DeepSeek by default) and uses function calling to inspect instances, dispatch tasks and wait for results.
- **MCP external tools**: optionally mount MCP (Model Context Protocol) servers (local command or Streamable HTTP address) and register their tools for the AI assistant; off by default with no server preinstalled.
- **CAD action executor**: a standalone ai.exe drives the CAD started by debugging through an action sequence (open drawing, run command, screenshot, read log, ...) and returns the results to the AI assistant for "pending verification" items; one adapter per project. Target projects can also embed `sdk\VsmVerify.cs` to expose a verification interface that ai.exe calls over a local named pipe.
- **Task list**: newly submitted AI tasks auto-start after saving by default; manual/restored tasks await **Start**, unless Settings explicitly enables all-automatic mode. Dispatch respects IDs and target readiness; manual Copilot chats are listed as well.
- **Task ownership and project summary**: task titles are completed as "Project · item" (the solution name) and shown in the task list and notifications; task notifications, failure feedback and send_task results end with a [项目上下文 / Project context] block (project name, responsibility, latest 3 task outcomes of that VS), so the AI assistant does not have to dig ownership out of a long conversation when several projects run in parallel. Queueing and dispatch rules are unchanged.
- **Solution registry & VS open/close**: register solutions under everyday names (aliases / synonyms with fuzzy matching) so the AI assistant can open and close Visual Studio by name; tasks for a closed solution are parked, and dispatch once it opens with automatic eligibility or manual Start in this session.
- **VS session record & one-click open**: "📌 记录 VS" above the sidebar VS list records the open solutions with their main-window and floating-pane positions; "▶ 一键打开 VS" opens the ones not yet open and restores the recorded layout once ready (also in the context / tray menus and as AI tools `record_vs_session` / `open_vs_session`).
- **Agent self-loop feedback**: the sidebar "Agent 自循环 / Agent loop" section reads the run folder of an external agent evaluation script (one sub-folder per run with `result.json`, `cases.json`, `transcript.md`, `logs\`) and draws pass-rate bars for the recent runs (green all passed, red failures, grey no result, amber running); clicking it switches the main area to the question page (the same area as the VS chat, AI assistant and notebook; click another sidebar item to switch back), with two views switched at the top: "Summary" (default) puts the unique questions in one table, one row per question (number + summary + short result (green "✓ 通过" / red "✗ 失败", with "· 曾失败 / · 曾通过" when an earlier test had the opposite result) + test history oldest → newest as ✓ / ✗ with passes / total, e.g. "✗✓✓✓ 3/4" + first / latest test time); "By batch" lists every tested question with one separator row per batch (evaluation run) showing its time, batches newest first and questions by number within a batch (each row: number + summary + result in this batch + overall result + time + duration; a question that failed first and passed in a later test counts as passed; selecting a separator shows the batch overview), and selecting a question shows all of its test records (the exact prompt, answer and failure reason of each test) below. Read-only; refreshes automatically when new results appear. The evaluation folder is selected automatically by an AI skill that reads code: it searches the repositories of open / registered solutions for evaluation scripts and code writing `result.json` / `cases.json`, resolves the run folders built from environment variables and picks the folder with the latest runs (searched automatically at startup or on first open when unset, with a manual folder picker only when nothing is found), stored in `AgentEvalDir` (with environment variables such as `%LOCALAPPDATA%`). All runs are read and the issue summary omits nothing; the AI assistant can select the folder with `find_agent_eval_folder` and list every issue with `list_agent_eval_issues` (filterable by failing / not rerun / resolved).
- **Voice**: optional Doubao speech service for spoken summaries when tasks finish (Chinese / English selectable; the AI assistant reply language follows it); the old VS composer's push-to-talk control has been removed.
- **Web remote & AI skill**: control everything from a phone browser on the LAN (access token required); the control API can be installed as a skill for Copilot CLI / Claude Code and similar agents (including VS screenshots).
- **History archive**: task history, assistant chats, per-instance chats and send logs are written to daily JSONL files and kept forever by default.
- **Publish to GitHub**: one-click git init / commit / create or link the remote / push, with an automatic sensitive-content scan before publishing.
- **Memory monitor**: working set and private bytes grouped by VSManager / each VS instance (with child processes) / shared components, with gentle cleanup and threshold alerts.
- **Auto restart**: the AI assistant is rebuilt automatically after an error, repeated request failures or a hang; an optional process watchdog relaunches VSManager after an abnormal exit, with a restart-storm limit.

## Requirements

- Windows 10 / 11
- Visual Studio 2022 or later with GitHub Copilot
- .NET Framework 4.8
- [Microsoft Edge WebView2 Runtime](https://developer.microsoft.com/microsoft-edge/webview2/) (included in Windows 11)

## Build and run

```powershell
git clone https://github.com/<owner>/VSManager.git
cd VSManager
dotnet build VSManager.slnx -c Release
.\src\VSManager\bin\Release\net48\VSManager.exe
```

Replace `<owner>` with the repository owner. The default branch is `main`; work in progress lives in `develop` (see [Branching](#branching)).

You can also open `VSManager.slnx` at the repository root in Visual Studio (the project file is `src\VSManager\VSManager.csproj`) and build / run it there.

Run the unit tests (MSTest; all test data goes to the system temp folder, real data under %APPDATA%\VSManager is never read or written):

```powershell
dotnet test VSManager.slnx
```

Tests fall into three categories (see `tests\VSManager.Tests\TestKind.cs`). By default `dotnet test` runs only the "no popup" set, which shows no window, takes no focus, does not touch the clipboard and starts no command-line process, so you can keep typing in other windows:

| Scope `TestScope` | Contents | How to run |
|---|---|---|
| `NoPopup` (default) | Tests that never pop up (about 960); enough after routine changes | `.\tests\run-tests.ps1` or `dotnet test VSManager.slnx` |
| `UI` | UI tests that show windows / take focus / use the clipboard; avoid typing elsewhere while they run | `.\tests\run-tests.ps1 -Scope UI` |
| `Console` | Tests that start command-line processes such as git, cmd or PowerShell (git must be on PATH) | `.\tests\run-tests.ps1 -Scope Console` |
| `All` | Every test (before a release, or after changing UI / command-line code) | `.\tests\run-tests.ps1 -Scope All` or `dotnet test VSManager.slnx -p:TestScope=All` |

The script also accepts `-Filter` (combined with the category filter) and `-NoBuild`; output goes to the test project's `bin\run-tests\` by default so a running VSManager does not lock files. An explicit `dotnet test --filter` takes precedence and no category filter is added. Tag new tests that show windows, take focus or use the clipboard with `[TestCategory(TestKind.Ui)]`, and tests that start command-line processes with `[TestCategory(TestKind.Console)]`.

If restore fails because the local NuGet configuration lists an unavailable source, run `dotnet restore VSManager.slnx --source https://api.nuget.org/v3/index.json` first.

## Directory layout

```text
VSManager/
├─ VSManager.slnx              Solution
├─ README.md / LICENSE / .gitignore / .gitattributes
├─ CONTRIBUTING.md             Contribution guide (branching, commit format, scan)
├─ CHANGELOG.md                Changelog
├─ settings.example.json       Example config (the real one lives in %APPDATA%\VSManager\ and is not committed)
├─ src/
│  └─ VSManager/               Main project (WinForms, .NET Framework 4.8)
│     ├─ VSManager.csproj
│     ├─ Program.cs / app.manifest
│     ├─ Assets/               Icon and embedded resources (web pages, Copilot skill)
│     │  ├─ app.ico
│     │  ├─ Web/               remote.html, transcript.html
│     │  └─ Skill/             SKILL.md, vsm.ps1
│     ├─ Core/                 Domain layer: no UI or Win32 dependencies
│     │  ├─ Models/            Data models (external chats, image attachments, Copilot state)
│     │  ├─ Tasks/             Task model, task state machine, send retry rules, task list
│     │  └─ TextUtil.cs        Shared text helpers
│     ├─ Infrastructure/       Infrastructure layer
│     │  ├─ Config/            Settings load / save (AppSettings), data folder (AppPaths)
│     │  ├─ Http/              AI client factory, request body policy
│     │  ├─ IO/                File-system abstraction, atomic writes
│     │  ├─ Logging/           Unified log entry (AppLog), send log
│     │  ├─ Storage/           tasks.json store
│     │  ├─ Win32/             Win32 interop, memory trimming
│     │  └─ QrCode.cs          QR code
│     ├─ Services/             Service layer
│     │  ├─ Abstractions/      Interfaces for external dependencies (VS operations, Copilot channel, voice)
│     │  ├─ Agent/             AI assistant, prompts, chat history
│     │  ├─ Publish/           Publish to GitHub
│     │  ├─ Remote/            LAN web remote, skill installer
│     │  ├─ Storage/           History archive
│     │  ├─ Tasks/             Task dispatcher (publish, retry, completion, failure)
│     │  ├─ VisualStudio/      VS instances, Copilot chat / monitor, code scanner, memory monitor
│     │  └─ Voice/             Doubao text-to-speech and speech recognition
│     └─ UI/                   UI layer: main window, theme, shared controls
│        ├─ Forms/             Settings, publish, chat history, memory windows
│        └─ Panels/            Copilot chat, AI assistant and task list panels
└─ tests/
   └─ VSManager.Tests/         Unit tests (MSTest)
```

All source files still share the single namespace `VSManager`; folders only group files by responsibility. Build output (`bin/`, `obj/`) and test results (`TestResults/`) are excluded by `.gitignore`.

### Layered architecture

- **Core (domain)**: the task model `QueuedTask`, the state machine `TaskStateMachine` (waiting → sending →