# Beetle

常驻系统托盘的桌面客户端：把飞书群里 @ 机器人的问题，交给本机的 Claude Code / Codex 处理，内置「查 bug」流程。

> 截图待补：`docs/images/screenshot-home.png`、`docs/images/screenshot-run-log.png`、`docs/images/screenshot-skills.png`

## 功能

- **飞书长连接机器人**：支持多个机器人，随客户端启动，断线自动重连。
- **Claude Code / Codex 双引擎**：每个机器人可单独选择由哪个本机 CLI 处理问题。
- **查 bug 流程**：读取群聊上下文 → 同步最新 release 代码 → 只读查询项目关联的数据源 → 给出根因与修复建议。
- **数据源自己管**：直连 MySQL / PostgreSQL / MongoDB（可走 SSH 跳板，密码只存系统凭据库，客户端强制只读），或指定一个自己的技能去查库。
- **代码审查机器人**：群里发 PR 链接自动审查，用 [open-code-review](https://github.com/alibaba/open-code-review)（`ocr`）按语言规则审查，输出带覆盖率的审查卡片。
- **记录方式多选**：可在 Gitee / GitHub 建 issue，也可写入飞书文档。
- **运行日志**：实时步骤流 + 原始日志，便于回溯 Agent 做了什么。
- **环境检查与一键安装**：检测 Claude Code / Codex、Python、Git、lark-cli 等依赖，缺什么装什么。
- **技能中心**：把产品自带的技能一键安装到 Claude Code 或 Codex。
- **首次启动引导、配置导入导出**。
- **深色 / 浅色主题**，多种主题色可选。

## macOS 首次打开

安装包暂未经过 Apple 公证。从浏览器下载后第一次打开时：

- 提示「无法验证开发者」：打开「系统设置 → 隐私与安全性」，在页面下方点「仍要打开」。
- 提示「已损坏，无法打开」（v0.1.7 及更早的版本）：把 Beetle 拖进「应用程序」后，在终端执行
  `xattr -cr /Applications/Beetle.app`，再双击打开。

之后通过客户端自动更新不会再出现这个提示。

## 安装与开发

开发环境依赖：

- Node.js 18+，pnpm
- Rust stable
- Windows 需要 WebView2 运行时（macOS 适配进行中）

```bash
pnpm install
pnpm tauri dev      # 开发模式
pnpm tauri build    # 打包安装程序
```

运行时依赖：

- Claude Code 或 Codex CLI（至少一个）
- Python 3.10+
- Git
- open-code-review（`npm i -g @alibaba-group/open-code-review`，代码审查用）
- lark-cli，并已完成**用户身份**登录

## 配置

1. **飞书应用**：创建飞书企业自建应用（客户端内可扫码创建，也可手填 App ID / App Secret）。注意同一个应用只能在一台电脑上建立长连接。
2. **lark-cli 登录**：用 `lark-cli auth login` 以用户身份登录，机器人读群聊、发消息、写文档都依赖它。
3. **数据源**：在「数据源」页添加。直连方式填地址、账号（建议只读账号），可配置 SSH 跳板；或者选「自定义技能」，指定本机已安装的某个技能来查这个库。再在项目里勾选关联的数据源。
4. **issue 令牌**：需要建 issue 时，设置环境变量 `GITEE_TOKEN` 或 `GITHUB_TOKEN`。使用仓库级令牌即可，需具备 issue 权限。

## 安全说明

- **直连查询由客户端强制只读**：Agent 通过 `beetle --db-query` 查询，看不到密码；只允许单条 `SELECT`（拦截 `INTO`、加锁、`@` 变量、读文件 / 休眠等危险函数），自动补 `LIMIT` 且有上限，会话设为只读并有超时，必须填写成本说明，每次查询记审计。用「自定义技能」查询的库，只读由该技能自己保证。
- **Agent 禁止清单是尽力而为，不是沙箱**：它通过提示词与规则约束 Agent 行为，不能替代操作系统级隔离。请在可信环境、最小权限账号下运行。
- **读私聊仅限机器人主人触发**，其他人 @ 机器人不会读取私聊内容。
- **密钥只存系统凭据库**（Windows 凭据管理器 / macOS 钥匙串），不写入配置文件。

## 目录结构

```
src/                              前端（界面）
src-tauri/                        后端（Rust / Tauri）
src-tauri/resources/skills/       机器人内置技能（chat-context、code-sync、issue-record、feishu-doc-record、db-query、pr-review 等）
src-tauri/resources/catalog/      技能中心里的技能（可安装到 Claude Code / Codex）
src-tauri/resources/templates/    流程模板（如 bug-hunt、qa）
```

## 参与贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

[AGPL-3.0-only](LICENSE)

---

## English

**Beetle** is a tray-resident desktop client that hands questions @-mentioned in Feishu (Lark) group chats to your local Claude Code or Codex, with a built-in "bug hunt" workflow: read chat context, sync the latest release code, run read-only production queries through an approval group, and propose a root cause and fix. Results can be recorded as Gitee / GitHub issues or Feishu docs. Built with Tauri (Rust) and a web frontend; Windows is supported, macOS is in progress. Dev: `pnpm install && pnpm tauri dev`. Licensed under AGPL-3.0-only.
