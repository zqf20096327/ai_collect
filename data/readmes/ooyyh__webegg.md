# WebEgg
<p align="center"><img src="docs/images/icon.png" width="96" height="96" alt="WebEgg icon" /></p>

[![CI](https://github.com/ooyyh/webegg/actions/workflows/ci.yml/badge.svg)](https://github.com/ooyyh/webegg/actions/workflows/ci.yml)
[![Release](https://github.com/ooyyh/webegg/actions/workflows/release.yml/badge.svg)](https://github.com/ooyyh/webegg/actions/workflows/release.yml)
[![Latest Release](https://img.shields.io/github/v/release/ooyyh/webegg)](https://github.com/ooyyh/webegg/releases)
[![Stars](https://img.shields.io/github/stars/ooyyh/webegg?style=flat)](https://github.com/ooyyh/webegg/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/ooyyh/webegg)](https://github.com/ooyyh/webegg/commits/main)
<a href="https://linux.do"><img src="https://img.shields.io/badge/LINUX%20DO-%E7%A4%BE%E5%8C%BA-FFB003?style=flat-square" alt="LINUX DO 社区" /></a>
WebEgg 是一个 **Wails + Go + React + Manifest V3** 的本地 AI 控制面。它通过浏览器插件驱动 Gemini 网页端，在本地执行真实的文件、目录、搜索、Git、Shell 和后台进程工具，并把对话与工具结果全部渲染在桌面端。

当前版本：`0.9.8`

> 不注入 Gemini 页面 UI，不依赖第三方 API Key。浏览器只是网页 AI 传输适配器，聊天与项目数据留在本机。

![WebEgg 本地对话工作区](docs/images/chat.png)

## 工作方式

```text
Wails 本地聊天
      │ 任务入队
      ▼
Go 本地 Bridge ──► Chrome 扩展 ──► Gemini 网页对话
      ▲                                  │
      │ 事件/工具结果                     │ 工具块
      └──────── MCP 工具执行 ◄────────────┘
             文件 / 目录 / Git / Shell / 进程
```

## 核心特性

- **本地 AI 聊天工作区**：每个项目独立会话，支持多会话、归档、复活和本地历史。
- **自动浏览器控制**：新建会话后自动创建 Gemini 网页对话并注入工具优先协议。
- **26 项真实编程工具**：文件、目录、搜索、Git、Shell、后台进程和项目脚本。
- **全自动 / 需批准**：读取自动，写入、删除、Shell 和进程可按策略请求本地批准。
- **结构化工具结果**：Markdown、代码块、文件内容、目录表格、终端输出和 Git diff。
- **真实数据可视化**：最近 7 天消息/工具调用趋势与工具能力分布。
- **可靠重连**：扩展 alarms 保活、标签页唤醒、内容脚本自动重注入和任务租约恢复。
- **极简黑白主题**：桌面、插件设置弹窗共享日间/夜间主题。

---

## 5 分钟快速开始

### 前置要求

- Windows 10/11 x64
- Chrome、Edge 或其他 Chromium 浏览器
- 一个可以正常登录的 Gemini 网页账号

> 建议保持 Gemini 标签页打开。可以切到后台或最小化浏览器，但不要关闭网页。

### 第 1 步：下载并运行桌面端

从 [Releases](https://github.com/ooyyh/webegg/releases/latest) 下载：

- 推荐：`WebEgg-windows-amd64.zip`
- 或单文件：`WebEgg.exe`

解压后运行 `WebEgg.exe`。如果 Windows SmartScreen 提示未知发布者，请确认文件来自本仓库 Release 后选择继续运行。

首次启动后保留桌面端窗口或让它正常运行。

### 第 2 步：加载浏览器扩展

1. 打开 `chrome://extensions/`（Edge 为 `edge://extensions/`）。
2. 开启右上角「开发者模式」。
3. 点击「加载已解压的扩展程序」。
4. 选择 Release 包中的 `extension` 目录，或源码仓库的 `extension/` 目录。
5. 将 **WebEgg Monochrome** 固定到浏览器工具栏。

当前没有 Chrome Web Store 版本，必须通过开发者模式加载。

### 第 3 步：授权项目

1. 在 WebEgg 桌面端打开「项目」。
2. 点击「添加项目」，选择一个本地代码目录。
3. 项目会以目录授权方式登记，不会自动修改文件。
4. 根据信任程度选择：
   - **需批准**：写入、删除、Shell、后台进程需桌面确认。
   - **全自动**：工具自动执行，适合完全信任的项目。

### 第 4 步：生成并配置连接令牌

1. 打开「连接」。
2. 点击「生成令牌」。
3. 立即复制 `we_...` 令牌。明文只显示一次。
4. 打开浏览器中的 WebEgg 扩展弹窗。
5. 填写：
   - MCP 地址：`http://127.0.0.1:8787/mcp`
   - 连接令牌：刚才生成的 `we_...`
6. 点击「保存并检测连接」。
7. 打开 Gemini 页面并刷新一次。

插件令牌只保存在扩展私有存储中，不会传入 Gemini 页面。

### 第 5 步：新建会话并开始任务

1. 回到桌面端默认的「对话」工作区。
2. 在顶部选择项目和会话。
3. 点击 `+` 新建会话。
4. WebEgg 会自动：
   - 新建本地会话
   - 驱动 Gemini 新建网页对话
   - 注入工具协议
   - 执行项目环境初始化
5. 看到「适配器在线」后，在底部输入任务。

可以尝试：

```text
先浏览项目结构，告诉我这个项目是做什么的。
```

```text
找到项目的测试入口，运行测试并修复失败。
```

```text
检查当前 Git 差异，找出潜在的 bug 并修复，完成后重新验证。
```

```text
启动开发服务器，确认监听地址后告诉我访问链接。
```

### 第 6 步：查看工具执行

工具调用会显示为可折叠卡片：

- 参数和结果默认收束。
- 点击卡片标题展开。
- 文件读取显示路径、行数和哈希。
- 命令显示退出码、stdout、stderr 和耗时。
- 目录显示条目表格。
- 可使用「渲染 / 原文」切换结构化展示与原始 JSON。

长驻开发服务器应使用后台进程工具，而不是 60 秒超时命令。模型需要检查进程日志后，才能报告服务器真正启动成功。

### 第 7 步：更新版本

1. 关闭旧 WebEgg 进程。
2. 下载并解压最新 Release。
3. 启动新 `WebEgg.exe`。
4. 在扩展管理页点击「重新加载」。
5. 刷新 Gemini 页面。

扩展权限或后台脚本更新后，必须重新加载扩展并刷新网页。

---

## 常见问题

| 现象 | 处理 |
|---|---|
| 一直显示“等待插件” | 确认 Gemini 标签页打开；重新加载扩展；刷新 Gemini；检查扩展是否启用了新版本 |
| 扩展显示已连接但适配器离线 | 插件后台可达，但 Gemini 内容脚本未运行；刷新 Gemini 页面 |
| 新建会话后没有自动初始化 | 确认至少有一个 Gemini 标签页；查看扩展是否有 alarms/scripting 权限 |
| 任务停在排队/运行中 | 重启 WebEgg 会标记中断；任务租约允许另一个在线 Gemini 标签页重新领取 |
| 开发服务器启动后消失 | 使用 `webegg_shell_start`，再用 `webegg_process_logs` 验证监听地址 |
| 文件写入提示冲突 | 重新读取文件获取最新 hash，再带 `expectedHash` 写入 |
| UI 还是旧版 | 确认加载的是本仓库 `extension/` 或最新 Release，而不是旧目录；重新加载并刷新页面 |
| 插件领不到任务 | 检查扩展设置中的地址和令牌；在「连接」页重新生成令牌后同步更新插件 |

更多排查见 [开发与测试](docs/DEVELOPMENT.md)。

## 工具与权限

当前注册 **26 项工具**：

| 分类 | 工具 |
|---|---|
| 项目与目录 | `project_list`、`project_info`、`directory_list/create/delete` |
| 文件读取 | `file_stat`、`file_read` |
| 文件编辑 | `file_create/write/patch/delete/move/copy` |
| 搜索 | `glob`、`grep` |
| Git | `git_status/diff/log/branches/show` |
| 执行 | `shell_run`、`shell_start`、`process_list/logs/stop`、`project_script` |

所有工具名均带 `webegg_` 前缀。完整参数、错误码和长驻服务器规则见 [工具参考](docs/TOOLS.md)。

- **读取工具**：自动执行。
- **写入/删除/Shell/进程**：根据执行策略自动执行或等待本地批准。
- 审批与工具名和完整参数哈希绑定，5 分钟过期，只能消费一次。
- Shell、项目脚本和后台进程不是操作系统沙箱。

## 安全边界

- 本地服务只监听 `127.0.0.1:8787`。
- MCP 使用 Bearer Token，桌面配置只保存 SHA-256 哈希。
- 文件路径经过规范化和项目根包含性检查。
- 拦截 `..`、绝对路径、盘符、UNC、符号链接逃逸和敏感文件。
- `.env*`、私钥、`.ssh`、`.aws`、credentials 等默认禁止访问。
- 文件覆盖/补丁/删除要求最新 SHA-256，修改前保存隔离备份。
- Git 只读，不提供 commit、push、reset 或 rebase。
- 不自动安装依赖。

## 开发与构建

```powershell
git clone https://github.com/ooyyh/webegg.git
cd webegg

cd frontend
npm ci
cd ..

wails dev
```

运行测试：

```powershell
go test ./...
go vet ./...

cd extension
npm test
cd ..

cd frontend
npm run build
cd ..
```

Windows 构建：

```powershell
wails build -clean
```

详细说明见 [开发、测试、构建与发布](docs/DEVELOPMENT.md)。

## 自动构建与发布

- `.github/workflows/ci.yml`：push/PR 自动测试、构建前端和 Windows Wails 校验。
- `.github/workflows/release.yml`：推送 `v*` tag 自动构建并发布 GitHub Release。
- Release 自动包含桌面程序、插件包、文档和 `SHA256SUMS.txt`。

```powershell
git tag v0.9.8
git push origin v0.9.8
```

## 文档

- [架构与数据流](docs/ARCHITECTURE.md)
- [26 项工具参考](docs/TOOLS.md)
- [开发、测试、构建与发布](docs/DEVELOPMENT.md)
- [贡献指南](CONTRIBUTING.md)
- [安全说明](SECURITY.md)
- [版本变更](CHANGELOG.md)

## 项目结构

```text
webegg/
├── app.go, main.go          # Wails、桌面 API、执行模式和审批
├── internal/
│   ├── approval/            # 参数绑定的一次性审批
│   ├── auth/                # 随机令牌与哈希校验
│   ├── bridge/              # 网页命令队列、租约与会话上下文
│   ├── chat/                # 项目会话、消息、工具历史与归档恢复
│   ├── config/              # 项目、配置、执行模式和状态目录
│   ├── server/              # loopback HTTP、MCP 与桥接端点
│   └── tools/               # 文件、搜索、Git、Shell、后台进程
├── frontend/                # React 桌面控制中心
├── extension/               # 无 UI 注入的 Gemini 后台传输适配器
├── docs/                    # 架构、工具和开发文档
└── .github/workflows/       # CI 与自动 Release
```

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=ooyyh/webegg&type=Date)](https://star-history.com/#ooyyh/webegg&Date)

## 致谢

WebEgg 由 [ooyyh](https://github.com/ooyyh) 维护。欢迎提交 Issue、Pull Request 或 Star 支持项目。
