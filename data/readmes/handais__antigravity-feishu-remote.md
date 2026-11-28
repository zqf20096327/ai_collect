<div align="center">

<img src="./assets/hero-banner.svg" alt="Feishu Remote Banner" width="100%" />

<br />

[![CI](https://github.com/handais/antigravity-feishu-remote/actions/workflows/ci.yml/badge.svg)](https://github.com/handais/antigravity-feishu-remote/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/handais/antigravity-feishu-remote)](https://github.com/handais/antigravity-feishu-remote/releases)
[![Node](https://img.shields.io/badge/node-%3E%3D22.5.0-brightgreen)](https://nodejs.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)

**简体中文** · [English Documentation](./README_EN.md) · [更新日志](./CHANGELOG.md)

[🎬 发布会演示](#-发布会演示keynote-preview) · [✨ 核心亮点](#-核心亮点feature-bento-grid) · [🏗️ 架构与安全](#-架构与零泄密安全模型) · [🤖 AI 一键部署](#-交给-ai-一键自动部署agent-quickstart) · [📋 飞书配置清单](#二飞书开放平台-3-分钟配置清单) · [📦 分享打包](#四如何打包分享给朋友)

</div>

> **免公网 IP · 免内网穿透 · 零泄密隔离**  
> 通过飞书 **WebSocket 长连接**，让你在手机（安卓 / iOS）或桌面飞书里随时指挥本机 **Antigravity (`agy`)**——实时看 **CardKit 2.0 打字机流式卡片**、多话题并发执行、拦截高危 Shell 命令、**电脑 ⇄ 手机双向会话接力**，甚至**在手机上直接修改并双检热更新本插件自身（支持快照一键回滚）**。  
> 个人 `App Secret` 与白名单严格保存在 `~/.config/antigravity-feishu/`（Windows 为 `%USERPROFILE%\.config\antigravity-feishu\`，`0600` 权限），插件目录零密钥，打包即可安全分享给朋友。

---

## 🎬 发布会演示（Keynote Preview）

<div align="center">
  <img src="./assets/keynote-demo.gif" alt="Feishu Remote Keynote Demo" width="100%" />
  <br />
  <sub>01 核心亮点 → 02 CardKit 2.0 实时流式编码 → 03 多话题并发 &amp; 控制面板 → 04 <code>/guard</code> 高危命令飞书审批 → 05 双向会话接力 &amp; 手机自迭代</sub>
</div>

---

## ✨ 核心亮点（Feature Bento Grid）

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>⚡ CardKit 2.0 打字机流式卡片</h3>
      实时原地刷新工具步骤、耗时与 Token 用量，失败自动无缝降级 <code>patchCard</code>；超长输出智能分片且不截断代码块，完成后自动在原消息贴上 <code>DONE</code> 表情并附带改动 Diff 按钮。
    </td>
    <td width="50%" valign="top">
      <h3>🧵 单群多话题并发隔离</h3>
      在飞书「话题群」内按 <code>chatId#threadRootId</code> 自动隔离上下文与工作目录。开几个话题就并发几路任务（默认上限 4），流式输出、分片与文件回传全部锁回原话题楼。
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>💻 电脑 ⇄ 手机双向无缝接力</h3>
      离开电脑自动感应（<code>--notify-mode away</code>）并把桌面端完成结果推到飞书，支持「🧵 新开话题接管」或回流原楼；随时用 <code>/handoff</code> + <code>feishu_read_mobile_session</code> 同步回桌面端继续。
    </td>
    <td width="50%" valign="top">
      <h3>🚀 手机远程自迭代插件（防变砖）</h3>
      出门在外也能直接在飞书里让 AI 修改 <code>feishu-remote</code> 源码：<code>/reload</code> 先自动跑语法与冒烟双检，通过后零中断热重启；每次启动自动留存健康快照，异常支持 <code>/rollback</code> 一键回滚。
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>🛡️ <code>/guard</code> 高危命令飞书审批</h3>
      内置 <code>PreToolUse</code> 安全钩子：当远程任务尝试执行 <code>rm -rf</code>、<code>git push --force</code>、<code>sudo</code> 等高危命令时，自动向手机推送审批卡片，超时 Fail-Closed 自动拒绝。
    </td>
    <td width="50%" valign="top">
      <h3>🎛️ 控制面板 · 云文档与技能生态</h3>
      支持动态置顶高频操作（<code>⭐ 常用操作</code>）、<code>⚡ 30m全权</code> 倒计时自动降权与 <code>🛠️ 设置</code> 二级页；消息贴飞书云文档链接自动读取正文与批注，支持 Task v2 待办及 <code>/</code> 技能清单。
    </td>
  </tr>
</table>

---

## 🏗️ 架构与零泄密安全模型

<div align="center">
  <img src="./assets/architecture-flow.svg" alt="Feishu Remote Architecture and Security Model" width="100%" />
</div>

> [!NOTE]
> **平台实测说明**
> - **macOS（主力验证）**：作者日常开发环境，已完整实机跑通长连接、`launchd` 开机常驻、`/desktop` 接管与离开感应。
> - **Linux / 原生 Windows（实验性支持）**：已完成跨平台代码适配并通过 GitHub Actions 三平台 CI（`ubuntu-latest` / `windows-latest` / `macos-latest`）自动化冒烟测试，但**作者暂未在真实 Linux / Windows 机器上做过完整端到端实测**；遇到平台兼容问题欢迎附上 `cli.mjs status` / `cli.mjs logs` 提 Issue 或 PR。

---

## 🤖 交给 AI 一键自动部署（Agent Quickstart）

如果你正在使用 **Antigravity / Claude Code / OpenClaw** 等具备终端能力的 AI 助手，**不需要自己手动敲命令**，直接把仓库链接交给它即可完成本地部署（提示：部署代理可以是 Claude Code / OpenClaw 等任意终端 AI，但运行时远程控制依赖本机已安装并登录 **Antigravity CLI (`agy`)**）。

### 1. 给用户：复制这句话发给你的 AI 助手

```text
请帮我按这个仓库的 README 自动部署飞书远程控制插件：
https://github.com/handais/antigravity-feishu-remote
安装到本机 Antigravity 全局插件目录（macOS/Linux 为 ~/.gemini/config/plugins/feishu-remote，Windows 为 %USERPROFILE%\.gemini\config\plugins\feishu-remote）。如果当前环境支持浏览器操作，也请直接打开飞书开放平台（https://open.feishu.cn/app）帮我完成应用创建、权限导入、长连接事件/回调配置与版本发布，只在需要我扫码登录、二次确认或最后在飞书发“你好”配对时提醒我。
```

### 2. 给 AI 助手（Antigravity / Coding Agent）的部署 SOP

> [!IMPORTANT]
> 请严格按以下步骤依次执行并校验输出；每步失败立即停止并报告原因，不要跳过检查。

#### Step 1 — 前置环境检查
1. 检查系统平台与支持边界：
   - **macOS**：已实机完整验证（`launchd` 常驻）。
   - **Linux / 原生 Windows**：实验性支持（代码已适配并通过三平台 CI，作者未做真实实机端到端验证）。Windows 使用 PowerShell 语法，Linux/WSL2 走 `systemd --user` 或后台进程；若遇到平台特定报错，先完整记录 `cli.mjs status` / `cli.mjs logs` 方便定位或向仓库反馈。
2. 检查 Node 版本与 `agy` CLI：
   - **macOS / Linux (bash/zsh)**：
     ```bash
     node -v && which agy
     ```
   - **Windows (PowerShell)**（勿用 `which` 或 `&&`，PowerShell 5.1 不支持 `&&`）：
     ```powershell
     node -v; Get-Command agy
     ```
     *(若使用 CMD 可运行 `node -v && where agy`。)*
   - 要求 **`Node.js >= 22.5.0`**（`/desktop` 只读索引与 `Stop` Hook 子代理过滤依赖内置 `node:sqlite`）。若版本过低，请先协助用户升级 Node 或提示安装。
   - 若找不到 `agy`，提醒用户先安装并完成 `agy` 登录验证。

#### Step 2 — 下载插件并安装依赖与体检
> [!CAUTION]
> 插件目录在 macOS/Linux 为 `~/.gemini/config/plugins/feishu-remote`，在 Windows 为 `$HOME\.gemini\config\plugins\feishu-remote`（即 `%USERPROFILE%\.gemini\config\plugins\feishu-remote`）。**在 Windows PowerShell/CMD 下严禁直接执行 `mkdir -p` 或向外部命令传未展开的 `~` 路径。**

1. 若插件目录尚不存在，安装或克隆仓库并安装生产依赖（也可用跨平台的 `agy plugin install https://github.com/handais/antigravity-feishu-remote` 替代克隆）：
   - **macOS / Linux (bash/zsh)**：
     ```bash
     mkdir -p ~/.gemini/config/plugins
     git clone https://github.com/handais/antigravity-feishu-remote.git ~/.gemini/config/plugins/feishu-remote
     cd ~/.gemini/config/plugins/feishu-remote && npm install --omit=dev
     ```
   - **Windows (PowerShell)**：
     ```powershell
     New-Item -ItemType Directory -Force "$HOME\.gemini\config\plugins" | Out-Null
     git clone https://github.com/handais/antigravity-feishu-remote.git "$HOME\.gemini\config\plugins\feishu-remote"
     Set-Location "$HOME\.gemini\config\plugins\feishu-remote"; npm install --omit=dev
     ```
   *(若已通过 zip 解压到此目录，进入对应目录执行 `npm install --omit=dev` 即可。)*
2. 运行代码体检与隔离冒烟测试，确认本地环境完全兼容：
   - **macOS / Linux**：
     ```bash
     node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs check
     node ~/.gemini/config/plugins/feishu-remote/scripts/smoke-test.mjs
     ```
   - **Windows (PowerShell)**：
     ```powershell
     node "$HOME\.gemini\config\plugins\feishu-remote\scripts\cli.mjs" check
     node "$HOME\.gemini\config\plugins\feishu-remote\scripts\smoke-test.mjs"
     ```
   - 期望：`cli.mjs check` 输出 `"ok": true` 且 `"errors": []`；`smoke-test.mjs` 输出 `ALL SMOKE TESTS PASSED`。

#### Step 3 — 飞书开放平台配置（支持 Antigravity IDE 浏览器半自动代办）

- **路径 A（推荐，当前 Agent 具备浏览器操作工具 / Antigravity IDE `/browser`）**：
  1. 打开 `https://open.feishu.cn/app`；如果未登录，先**暂停并提示用户扫码登录飞书开放平台**，待用户确认登录后再继续后续点击。
  2. 新建一个企业自建应用（或进入用户指定的已有应用），开启 **应用能力 → 机器人（Bot）**。
  3. 进入 **权限管理 → 批量导入/导出权限**，粘贴下方 **[二、飞书开放平台 3 分钟配置清单](#二飞书开放平台-3-分钟配置清单)** 中的 JSON 一键开通权限（若用户计划建个人话题群免 `@` 使用，顺带确认开通 `im:message.group_msg`）。
  4. 进入 **凭证与基础信息** 获取 `App ID` 与 `App Secret`（若点击查看需要验证码/人工复制，请让用户粘贴或仅在本机运行 `cli.mjs setup`，**绝不在对话回复里明文回显 `App Secret`**）。
  5. **先跑 Step 4 的 `setup` 与 `start` 启动本地守护进程，再保存长连接**：因为飞书后台开启「使用长连接接收事件/回调」时可能会校验当前应用是否已有在线长连接，请先完成 Step 4 写入凭证并启动守护进程（注意：此时应用尚未发布版本，`cli.mjs scopes` 里的权限显示 `pending` 属正常现象，**发布后再跑 `scopes` 验收**）。
  6. 回到网页 **事件与回调**：将「事件配置」和「回调配置」的订阅方式均设为 **使用长连接接收**，添加事件 `im.message.receive_v1`、`application.bot.menu_v6` 与回调 `card.action.trigger`。
  7. （可选）进入 **机器人自定义菜单** 配置 `menu_panel` / `menu_commands` / `menu_new` / `menu_stop`（响应动作选「推送事件」）。
  8. 进入 **版本管理与发布** → 创建版本（可用范围保持仅自己或指定成员）并提交发布（遇到需人工确认/审核提示时由用户确认）。
  9. **发布后权限验收**：运行 `cli.mjs scopes` 确认基础 `im:message`、`im:resource`、`cardkit:*` 等权限均已变为 `granted`（若仍有 `pending`，确认版本已正式生效并等待数十秒再复查）。

- **路径 B（纯命令行环境、无浏览器工具）**：
  - 引导用户按下方 **[二、飞书开放平台 3 分钟配置清单](#二飞书开放平台-3-分钟配置清单)** 操作并发布，向用户索取且**仅索取**两项信息：**`App ID`** 与 **`App Secret`**，再执行 Step 4（并在确认版本已发布后运行 `cli.mjs scopes` 验收）。

#### Step 4 — 写入配置、启动守护进程与验收
拿到 `App ID` 和 `App Secret` 后执行（`cli.mjs` 内部会自动把 `--cwd ~` 跨平台展开为当前用户主目录，并把配置保存到 `~/.config/antigravity-feishu/` / `%USERPROFILE%\.config\antigravity-feishu\`）：

- **macOS / Linux (bash/zsh)**：
  ```bash
  node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs setup \
    --app-id "<APP_ID>" \
    --app-secret "<APP_SECRET>" \
    --cwd ~ \
    --mode accept-edits \
    --notify-mode away

  node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs start
  node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs status
  ```
- **Windows (PowerShell)**（勿使用 `\` 续行）：
  ```powershell
  node "$HOME\.gemini\config\plugins\feishu-remote\scripts\cli.mjs" setup --app-id "<APP_ID>" --app-secret "<APP_SECRET>" --cwd ~ --mode accept-edits --notify-mode away
  node "$HOME\.gemini\config\plugins\feishu-remote\scripts\cli.mjs" start
  node "$HOME\.gemini\config\plugins\feishu-remote\scripts\cli.mjs" status
  ```
- 阶段验收标准：
  - `cli.mjs status` 中 `configured: true` 且 `daemon.running: true`；
  - 若是路径 B（应用已发布版本）或已完成 Step 3 第 8 步发布，继续执行 `cli.mjs scopes`（Windows 为 `node "$HOME\.gemini\config\plugins\feishu-remote\scripts\cli.mjs" scopes`）确认基础 `im:message`、`im:resource`、`cardkit:*` 等权限处于 `granted` 状态。
- **Windows 重启后提醒**：原生 Windows 下 `cli.mjs start` 采用分离后台 PID 模式，**系统重启后不会像 macOS `launchd` / Linux `systemd` 那样自动开机启动**；部署完成时请提醒用户：重启电脑后需重新运行一次 `cli.mjs start`（或自行配置 Windows 任务计划程序 / WSL2）。

#### Step 5 — 首轮配对验活
1. 提示用户在手机/电脑飞书里找到该机器人，**私聊发送一句 `你好`**，触发自动白名单绑定与欢迎卡片。
2. 绑定完成后，可选执行 `cli.mjs test-send --panel` 验证控制面板卡片可正常送达。

#### AI 必守红线与排错速查
- **凭证隔离红线**：严禁将 `appSecret`、`open_id` 写入插件仓库目录内（`~/.gemini/config/plugins/feishu-remote/` 或 `%USERPROFILE%\.gemini\config\plugins\feishu-remote\`），也严禁在回复或日志中明文回显 `appSecret`（所有凭证与状态统一由 `cli.mjs setup` 保存在 `~/.config/antigravity-feishu/` / `%USERPROFILE%\.config\antigravity-feishu\`，POSIX 权限 `0600`）。
- **子进程重启禁令**：如果当前任务本身是由飞书桥接拉起的子会话（`FEISHU_REMOTE_BRIDGE_CHILD=1`），禁止自行运行 `cli.mjs restart` 杀掉父守护进程；应提示用户在飞书发 `/reload` 安全重启。
- **常见快速调整**：
  - 话题群免 `@` 触发：确保飞书后台已开通并发布 `im:message.group_msg`，再执行 `cli.mjs setup --group-policy all`（白名单依然仅放行授权 `open_id`）。
  - 调整全局并行任务上限（默认 `4`）：`cli.mjs setup --max-concurrent 2`（16 GB 内存日常推荐 2–4）。
  - 详细维护与排错规则另见仓库内的 `skills/feishu-remote/SKILL.md` 与 `rules/AGENTS.md`。

---

## 一、全部功能与指令速查

插件涵盖 **飞书 WebSocket 守护进程**、**25+ 飞书斜杠指令与交互卡片**、**`feishu-remote-tools` MCP 工具集** 以及 **`Stop` / `PreToolUse` 双生命周期 Hook**。

<details>
<summary><b>📖 展开查看完整功能清单、飞书指令集、MCP 工具与 Hook 说明</b></summary>

1. **飞书长连接桥接守护进程（Daemon）**：
   - 开机后台常驻（macOS `launchd` / Linux `systemd --user`）。
   - **CardKit 2.0 打字机流式更新**（失败自动降级 `patchCard`），工具步骤原地刷新状态与耗时，页脚展示耗时 / 工具次数 / Token 用量；超长结果自动智能分片且不截断代码块。
   - **消息表情状态反馈**：任务完成后自动在原消息贴上 `DONE` 表情。
   - **任务自动排队 & 失败重试**：上一条任务尚未完成时，后续发送的消息自动排队接力执行（支持一键中止当前立刻执行或取消排队）；中止/异常卡片自带 `🔄 重试` 按钮。
   - **引用回复 & 云文档上下文**：在飞书长按「回复」历史消息、卡片或截图时自动带入上下文；在消息里直接贴 `feishu.cn/docx/...` 或 `/wiki/...` 链接会自动拉取正文给 Antigravity。
   - 每个飞书会话独立记忆工作目录、权限模式（含**临时全权限到期自动降权**）、模型与最近历史会话（支持跨窗口/跨话题聚合）。
   - **单群多话题并行（话题群模式）**：在飞书「话题群」中按 `chatId#threadRootId` 自动隔离会话，群内每开一个话题即一个独立并行会话（默认全局最多同时执行 4 个并发任务，可通过 `--max-concurrent` 调整），消息、流式卡片、分片与文件回传全部锁回原话题楼。
   - **安全白名单**：默认首次私聊发消息的账号自动绑定为唯一主人（`autoBindFirstUser`），其他陌生私聊直接拦截并提示其 `open_id`。
2. **飞书常用指令与快捷方式**：
   - **多页可视化控制面板 + 卡片交互按钮**：可在飞书开放平台开启「机器人自定义菜单」与 `card.action.trigger` 长连接回调，不用记命令直接点按钮操作；支持在主控制面板、目录浏览、命令与技能、最近会话、模型切换和 `🛠️ 设置` 之间**原地翻页切换**（子页面均带 `⬅️ 返回面板`）。消息回复卡片内也自带「🆕 新对话」「⚙️ 控制面板」「🗂️ 最近会话」及执行中的「🛑 立即中止」按钮。
   - `/panel`（或 `/menu`）：打开带按钮的控制面板（一键切换常用目录/模式/模型、**⚡ 30m全权**、**🌿 Git**、**🔐 权限**、目录浏览器、收藏目录、开新对话、**♻️ 安全重启** / **⏪ 快照回滚**）
   - `/` 或 `/skills`：查看 `agy` 内置命令与本机已安装 Skills 清单（支持一键 `/compact` 及 `/agy <原始命令>` 强制透传）
   - `/git`：零延迟查看当前工作目录 Git 分支、工作区改动及最近 5 条提交（不经大模型）
   - `/scopes`（或 `/perms`）：自检飞书应用各项能力权限授权状态，有待审权限时支持一键向管理员重发审批申请
   - `/queue`：查看和管理当前对话的排队任务列表（支持单条取消或清空）
   - `/doc`：读取或生成飞书云文档（`/doc <链接|ID>`、`/doc create 标题 | Markdown`、`/doc write 链接 | Markdown`）
   - `/tasks`（或 `/todo`）：查看、新建（`/tasks add 标题 | 说明`）、勾选完成或一键交给 Antigravity 执行飞书任务中心待办（需先配置 OAuth 回调并运行一次 `cli.mjs auth`）
   - `/ops`（或 `/backups`）：打开**运维与自迭代面板**（查看运行版本 vs 磁盘版本、触发代码体检、保存快照、安全重启、二次确认回滚历史快照）
   - `/reload`：执行语法 + ESM 导入双阶段预检，通过后安全重启守护进程并推送上线确认卡片
   - `/check`：仅执行插件脚本代码体检（`node --check` + 导入导出检查），不重启
   - `/snapshot` / `/rollback [快照ID]`：手动保存当前可用快照，或回滚到上一版快照（带确认按钮）
   - `/dirs`：打开交互式**目录浏览卡片**（支持进入子目录、返回上一级、`🏠 ~`、一键 `📌 收藏/取消收藏此目录`、以及点击 `🙈 显示隐藏` 或 `/dirs -a` 切换显示 `.` 开头隐藏目录）
   - `/help`：查看全部命令
   - `/status`：查看当前工作目录、模式（含临时全权倒计时）、模型、队列条数、会话 ID 与运行状态
   - `/new`：开启新对话（清空当前上下文绑定）
   - `/sessions [all|here]` / `/use <序号|ID>`：查看并切回全部飞书窗口或当前话题的最近会话（跨窗口切换自动同步工作目录 `cwd`，顶部支持一键切换到 **`💻 电脑对话`**）
   - `/desktop [关键词]`（别名 `/pc`）：只读扫描与全文检索本机 CLI / 桌面端历史对话，预览最近上下文并支持**双轨接管**（可选 **`🧵 新开话题接管`** 在话题群独立开楼隔离上下文，或 **`📱 当前对话接管`** / **`👀 接管并总结`**）
   - `/topic [set|clear]` / `/unlink`：查看或绑定「🧵 新开话题接管」的默认话题群；`/unlink` 可结束当前话题楼与电脑端的自动回流追踪
   - `/handoff [cli|desktop]`（别名 `/back`）：生成手机端回流电脑端的终端 `agy --conversation` 恢复命令与桌面交接提示词（自动写入系统剪贴板与交接快照，并支持桌面端通过 `feishu_read_mobile_session` 无感同步手机进度、自动检测原桌面端分叉）
   - `/guard [on|off]`（别名 `/approval`）：开关 `PreToolUse` 高危命令飞书审批拦截（默认开启，对 `rm -rf`、`git push --force`、`git reset --hard`、`sudo` 等高危命令弹窗确认，超时 Fail-Closed 拒绝）
   - `/cd <路径或关键词>`（或 `/cwd`）：切换执行目录；支持模糊关键词匹配常用目录并弹出候选按钮
   - `/send <文件路径>`（或 `/sendfile <路径>`）：把本机图片或文件直接发回飞书（加 `--file` 强制按文件发送）
   - `/pin`：收藏 / 取消收藏当前目录到控制面板快捷目录
   - `/mode [accept-edits|plan|auto|full|default|full 30m]`：查看或切换执行权限模式（支持 `/mode full 30m` 临时全权限并在到期后自动切回安全模式）
   - `/timeout [分钟|0]`：查看或设置单轮任务超时时间（默认 60 分钟；`/timeout 0` 不限时，CardKit 超过 10 分钟流式窗口会自动无缝切为全卡刷新）
   - `/effort [low|medium|high|xhigh|max|default]`：查看或切换推理强度（控制面板也可直接点 `🎛️ 强度`）
   - `/notify [on|away [分钟]|off]`（别名 `/mute` / `/unmute`）：切换桌面端完成提醒（始终 / 仅离开电脑时通过键鼠空闲检测提醒 / 关闭）
   - `/model [模型名|default]` / `/models`：查看可用模型或切换模型（支持点击按钮切换）
   - `/stop`（或 `/cancel`）：立即中止当前正在执行的任务
   - **多模态收发**：手机直接发送图片/截图、文件（PDF/代码/文档）、语音或图文混排，自动下载至 `~/.config/antigravity-feishu/inbox/`（7 天自动清理）并由 Antigravity 原生读取分析。
   - **基础存储与性能治理**：`mcp-server.mjs` 按需懒加载飞书 SDK；守护进程默认 `warn` 级静音并带本地时间戳，启动及每 24 小时自动原地截断超 5 MB 的日志文件，并限制 `inbox/` 附件 7 天过期与 200 MB 总上限。
3. **MCP 主动推送与文档/任务工具（`feishu-remote-tools`）**：
   - `feishu_send_message` / `feishu_send_card` / `feishu_send_file`：让桌面端 Antigravity 主动向你手机发汇报或回传本地图片/文件。
   - `feishu_read_doc` / `feishu_write_doc`：读取飞书云文档/Wiki（含正文及划词/全文批注），或将 Markdown 分析报告直接新建/追加写入飞书云文档。
   - `feishu_list_tasks` / `feishu_create_task` / `feishu_complete_task`：查询个人/清单待办、创建或完成飞书 Task v2 任务（需先在飞书后台配置 `http://127.0.0.1:18923/callback` 并运行一次 `cli.mjs auth`）。
   - `feishu_list_mobile_sessions` / `feishu_read_mobile_session`：在桌面端直接读取你在手机飞书上聊过的 CLI 会话记录、改动文件与最新结论，无需手动翻日志路径。
   - `feishu_bridge_status` / `feishu_manage_bridge`：直接查询或启停桥接后台服务。
4. **任务完成提醒 & 电脑→手机接力 Hook（`Stop`） & 高危命令审批（`PreToolUse`）**：
   - 当你在电脑端发起的任务执行结束时，若该对话已绑定过未关闭的话题楼，通知会自动**静默回流到原话题楼**（附带 `🔄 同步电脑最新进展` 与 `🔓 结束本楼追踪`）；否则发往私聊总收件箱，提供 **`🧵 新开话题接管`** 与 **`📱 当前私聊接管`** 双选项及**最新回复结果预览**。
   - 当飞书桥接拉起的子任务尝试执行高危 Shell 命令时，`PreToolUse` Hook 自动向飞书推送审批卡片，确认后才放行。
   - 飞书每轮任务结束后，若修改了本地文件，完成卡片会自动附带 **`🔍 看改动 Diff`**、**`📄 查看改动文件`** 与 **`📥 发到聊天`** 快捷按钮。

</details>

---

## 二、飞书开放平台 3 分钟配置清单

1. 登录 [飞书开放平台](https://open.feishu.cn/app) → 进入你的 **企业自建应用**。
2. **添加应用能力**：开启 **机器人（Bot）**。
3. **权限管理**（也支持在飞书开放平台「权限管理 → 批量导入/导出权限」直接粘贴下方 JSON 一键导入）：
```json
{
  "scopes": {
    "tenant": [
      "im:message",
      "im:message:send_as_bot",
      "im:message.p2p_msg:readonly",
      "im:message.group_at_msg:readonly",
      "im:message:readonly",
      "im:resource",
      "im:message.reactions:write_only",
      "im:message.reactions:read",
      "cardkit:card:write",
      "cardkit:card:read",
      "docx:document",
      "docs:permission.member:create",
      "docx:document:readonly",
      "docx:document:write_only",
      "docx:document.block:convert",
      "wiki:node:read"
    ]
  }
}
```
<details>
<summary>查看各项权限用途说明</summary>

   - **基础必需**：
     - `im:message`（获取与发送单聊、群组消息）
     - `im:message:send_as_bot`（以应用身份发消息）
     - `im:message.p2p_msg:readonly`（读取用户发给机器人的单聊消息）
     - `im:resource`（获取与上传图片或文件资源 — 手机端发图片/文件/语音及 `/send` 回传必需）
   - **增强交互 & 云文档（强烈推荐）**：
     - `cardkit:card:write` / `cardkit:card:read`（CardKit 2.0 打字机流式更新）
     - `im:message.reactions:write_only` / `im:message.reactions:read`（消息表情状态反馈）
     - `im:message:readonly`（读取引用回复的历史消息与卡片内容）
     - `docx:document` / `docs:permission.member:create` / `docx:document:readonly` / `docx:document:write_only` / `docx:document.block:convert` / `wiki:node:read`（飞书云文档与 Wiki 读取/创建/写入及自动给主人开协作者权限）
     - `im:message.group_at_msg:readonly`（可选，如需在群里 `@机器人` 使用）
     - `im:message.group_msg`（可选，仅在配合 `--group-policy all` 实现单人话题群免 `@` 直接打字触发时需要）

</details>

4. **事件与回调**：
   - **事件配置**：订阅方式选择 **「使用长连接接收事件」**，添加事件 **`im.message.receive_v1`**（接收消息 v2.0）和 **`application.bot.menu_v6`**（机器人自定义菜单事件，用于响应底部菜单点击）。
   - **回调配置**：订阅方式选择 **「使用长连接接收回调」**，添加回调 **`card.action.trigger`**（用于响应控制面板、目录浏览、队列、权限、Git、重试等卡片按钮点击）。
5. **机器人自定义菜单（推荐，不用打字直接点）**：
   - 在 **应用能力 → 机器人 → 机器人自定义菜单** 中开启（推荐「悬浮菜单」或底部菜单）。
   - 每个菜单项推荐把「响应动作」设为 **「推送事件」**，Event Key 可设为：`menu_panel`（控制面板）、`menu_commands`（命令与 Skills）、`menu_new`（新对话）、`menu_stop`（中止任务）；也支持 `menu_dirs`、`menu_effort`、`menu_git`、`menu_scopes`、`menu_queue`、`menu_mode_temp_full`、`menu_ops`、`menu_reload`、`menu_sessions`、`menu_models`、`menu_mode_full`、`menu_help`（或直接发送 `/panel`、`/`、`/new`、`/stop`）。
6. **版本管理与发布**：创建版本并发布（如果只给自己用，可发布为仅自己/指定测试人员可见）。
7. 在 **凭证与基础信息** 页面复制 **`App ID`** 和 **`App Secret`**。

---

## 三、本机安装与启动

> **环境要求**：`Node.js 22.5+`（`/desktop` 只读索引扫描依赖内置 `node:sqlite`）及已登录的 `agy` CLI。守护进程托管支持 **macOS (`launchd`)**、**Linux (`systemd --user`)** 与 **原生 Windows**（PowerShell/CMD 下自动走分离后台 `pid` 模式，支持 `where agy`、系统代理读取与 `GetLastInputInfo` 离开感应；Windows 如需开机自启可配合计划任务或使用 WSL2）。
>
> **目录与平台说明**：Windows 用户的全局插件目录为 `%USERPROFILE%\.gemini\config\plugins\feishu-remote`（PowerShell 为 `$HOME\.gemini\config\plugins\feishu-remote`），凭证配置目录为 `%USERPROFILE%\.config\antigravity-feishu\`。目前作者主力在 **macOS** 实机验证，**Linux / Windows 属于通过三平台 CI 测试的实验性支持**。

### 1. 安装插件与依赖

**方式 A（推荐，Antigravity CLI 一键安装）**：
```bash
agy plugin install https://github.com/handais/antigravity-feishu-remote
# 然后在插件安装目录安装生产依赖（全局目录默认如下，若安装在工作区请进入对应路径）：
cd ~/.gemini/config/plugins/feishu-remote && npm install --omit=dev
```

**方式 B（Git 克隆安装）**：
```bash
git clone https://github.com/handais/antigravity-feishu-remote.git ~/.gemini/config/plugins/feishu-remote
cd ~/.gemini/config/plugins/feishu-remote && npm install --omit=dev
```

### 2. 写入配置
```bash
node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs setup \
  --app-id "你的_APP_ID" \
  --app-secret "你的_APP_SECRET" \
  --cwd "$HOME" \
  --mode accept-edits
```
> 国内代理说明：本插件默认会隔离代理环境——飞书长连接与 REST API **直连**（避免本地 `socks5://` 环境变量导致断连），同时自动检测本机 HTTP 代理并仅注入给底层 `agy` 子进程。如需手动指定，可传 `--proxy http://127.0.0.1:7897`。

### 3. 启动守护进程
```bash
node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs start
node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs status
```

### 4. 在手机飞书里配对
打开手机飞书，搜你的机器人名字，在**私聊**里给它发一句 `你好`（或 `/help`）。  
机器人会自动绑定你的飞书 `open_id` 为白名单主人并回复欢迎卡片，随后即可直接发任务使用！

<details>
<summary><b>🛠️ 展开查看常用 CLI 运维命令（状态、日志、体检、文档与重启）</b></summary>

```bash
# 查看状态
node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs status

# 查看最近 50 行日志
node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs logs --lines 50

# 发送测试卡片 / 直接推送控制面板 / 发送本机文件回飞书
node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs test-send
node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs test-send --panel
node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs test-send --dirs
node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs send-file ~/Desktop/screenshot.png

# 代码体检 / 安全重启 / 快照与回滚
node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs check
node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs safe-restart
node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs backups
node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs snapshot
node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs rollback

# 飞书应用权限自检 & 云文档读写 & 电脑端会话扫描
node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs scopes
node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs read-doc "https://xxx.feishu.cn/docx/..."
node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs write-doc --title "分析报告" --file ./report.md
node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs desktop --limit 5
node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs desktop --query "关键词" --limit 5

# 重启 / 停止
node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs restart
node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs stop
```

</details>

---

## 四、如何打包分享给朋友？

直接运行打包命令（会自动排除 `node_modules` 和任何个人敏感配置）：

```bash
node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs pack --out ~/Desktop/feishu-remote-plugin.zip
```

### 朋友收到 zip 后的安装步骤（4 步）
1. 确保朋友电脑上已安装 `Node.js`（22.5+）和 `agy` CLI（并已登录）。
2. 把 zip 解压到他自己电脑的 `~/.gemini/config/plugins/`（最终路径为 `~/.gemini/config/plugins/feishu-remote/plugin.json`，注意不要套娃）。
3. 安装依赖并写入他自己的飞书应用凭证：
   ```bash
   cd ~/.gemini/config/plugins/feishu-remote && npm install --omit=dev
   node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs setup --app-id "他的AppID" --app-secret "他的AppSecret"
   node ~/.gemini/config/plugins/feishu-remote/scripts/cli.mjs start
   ```
4. 他自己在手机飞书私聊自己的机器人发一条消息，即可自动绑定并开始使用。

---

## 五、致谢

感谢 [LINUX DO](https://linux.do) 社区的支持与交流。
