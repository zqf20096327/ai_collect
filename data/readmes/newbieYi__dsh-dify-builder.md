# dsh-dify-builder

在 DeepSeek Harness 中通过对话实时构建本地 Dify 工作流。右侧直接显示 Dify 画布，节点和连线原地更新，不反复刷新页面。

## 效果演示

[![对话实时生成 Dify 工作流演示](https://raw.githubusercontent.com/newbieYi/dsh-dify-builder/main/docs/assets/dsh-dify-builder-preview.gif)](https://newbieyi.github.io/dsh-dify-builder/demo.html)

左侧通过对话描述需求，右侧 Dify 画布会同步创建和修改节点。点击上方动画可播放完整演示视频（约 1 分 51 秒，默认静音，可在播放器中开启声音）。

## 安装前检查

### 1. Node.js 20+

检查：

```bash
node --version
npx --version
```

如果命令不存在，先从 [Node.js 官网](https://nodejs.org/en/download) 安装 LTS 版本，再重新打开终端。版本低于 20 时也需要先升级。

### 2. DeepSeek Harness

检查：

```bash
dsh --version
```

如果命令不存在，执行：

```bash
npm install -g @deepseek-ai/dsh@latest
dsh --version
```

首次使用可运行 `dsh web`，浏览器会打开 DSH。请先确认 DSH 可以正常对话。若 DSH 已配置 DeepSeek API Key，安装器会尝试将其同步到 Dify；密钥不会写入仓库或打印到日志。没有 DeepSeek Key 也可以完成安装并使用非模型工作流。更多信息见 [DeepSeek Harness 官方项目](https://github.com/deepseek-ai/deepseek-harness)。

### 3. Docker

检查：

```bash
docker --version
```

如果命令不存在，请先安装 [Docker Desktop](https://docs.docker.com/desktop/)。macOS 上安装后无需提前启动，安装器会自动打开并等待 Docker 就绪；Linux 需要确保 Docker Engine 可以正常运行。

## 快速安装

无需克隆仓库，直接从 GitHub Release 安装：

```bash
npx --yes "https://github.com/newbieYi/dsh-dify-builder/archive/refs/tags/v0.2.4.tar.gz" install
```

该命令固定使用经过验证的 `v0.2.4`，只需要 `npx`，不要求本机安装 Git。项目源码、版本记录和问题反馈位于 [newbieYi/dsh-dify-builder](https://github.com/newbieYi/dsh-dify-builder)。

看到“安装完成”后，重新打开 DSH Web，新建会话并选择「Dify 工作流构建」。不需要手动下载 Dify、编写 Docker 配置、安装 Sidebar 或创建管理员账号。

安装器会在下载 Dify 前检查 DSH CLI 和 Docker。前置条件不满足时会停止并显示对应安装命令，不会执行到一半才提示。

## 安装器会做什么

安装器自动完成并逐项验收：

1. 检查 DSH CLI 和 Docker；macOS 上 Docker 未启动时自动打开 Docker Desktop。
2. 下载经过验证的固定版本 Dify。
3. 配置 iframe 和 Dify 原生协作通道。
4. 启动并检查 Dify 容器，初始化本地管理员。
5. 尝试安装 Dify 官方 DeepSeek 模型插件；存在 DSH DeepSeek Key 时同步凭据并选择可用模型。
6. 安装 DSH runtime、内置 Sidebar、右侧 panel 和 Agent preset。
7. 检查插件冲突、Dify setup 和实时协作端点；默认模型缺失只显示警告，不会阻断安装。

首次安装会使用 `admin@dify.local`，密码随机生成并仅保存在本机私有配置中。重复执行安装命令是安全的，不会重建管理员或更换已有 Dify 密钥。

## 日常使用

1. 在空白新会话中选择「Dify 工作流构建」。
2. 如果 Docker 或 Dify 没有运行，插件会自动检查并拉起。
3. 在左侧描述要创建或修改的工作流，右侧 Dify 画布会实时更新。
4. 空白会话切换到其他模式时，Dify 标签和右侧栏会自动关闭。

## 遇到问题

运行只读诊断：

```bash
npx --yes "https://github.com/newbieYi/dsh-dify-builder/archive/refs/tags/v0.2.4.tar.gz" doctor
```

诊断会检查 DSH CLI、Docker、三个插件、Sidebar 冲突、Dify setup 和 Socket.IO 协作通道，不会修改配置或重启服务。默认模型缺失会显示 `WARN`，但诊断仍可通过。

常见情况：

| 现象 | 处理方式 |
|---|---|
| 提示找不到 Docker | 先安装 Docker Desktop，再重新执行安装命令 |
| 安装完成但看不到新模式 | 重新启动 DSH Web 后再新建会话 |
| 提示默认模型未配置 | 非模型工作流仍可使用；需要大模型节点时，在 Dify 中配置并选择模型 |
| 大模型节点不可选 | 在 Dify 的模型供应商设置中配置可用模型，再为节点选择该模型 |
| 已有 Dify，管理员登录验证失败 | 使用下方高级参数提供现有账号和密码 |
| 安装在管理员初始化后中断 | 直接再次执行安装命令，安装器会恢复默认管理员凭据并继续 |

<details>
<summary>高级安装参数</summary>

使用已有账号或指定访问地址：

```bash
npx --yes "https://github.com/newbieYi/dsh-dify-builder/archive/refs/tags/v0.2.4.tar.gz" install \
  --email owner@example.com \
  --password 'YourStrongPassword123!' \
  --name Owner \
  --base-url http://127.0.0.1:8080
```

默认数据目录：

| 内容 | 默认位置 |
|---|---|
| Dify 源码和数据入口 | `~/.dsh/dify-builder/dify` |
| 私有配置 | `~/.dsh/dify-builder/config.json` |
| 打包后的 DSH 插件 | `~/.dsh/dify-builder/packages` |
| Agent preset | `~/.dsh/.agent-presets/dify-builder` |

可用 `DSH_HOME` 修改 DSH 根目录，用 `DSH_DIFY_HOME` 单独修改 Dify 部署目录。

</details>

<details>
<summary>从源码开发和验证</summary>

仅项目开发者需要使用：

```bash
node ./bin/dsh-dify-builder.js install
npm test
```

普通用户不需要进入 `packages/`，也不需要单独安装或阅读 Sidebar 子项目。

</details>

## 技术说明

- Dify 固定在经过验证的上游 commit；本项目不修改 Dify 源码。
- 草稿保存使用 Dify 原生 collaboration 模式和 Socket.IO `workflow_update`。
- 创建应用后右侧只导航一次，普通节点修改不会刷新 iframe。
- `dsh-dify-sidebar` 随安装器发行，安装时会移除冲突的原版 Sidebar。
- 私密账号和密码只写入权限为 owner-only 的本地配置，不进入 preset 或公开仓库。

## 平台与许可

当前完成 macOS 和 Linux 支持；Windows 尚未完成端到端验证。

主项目使用 MIT License。`packages/dsh-dify-sidebar` 派生自 MIT 许可的 [DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar)，原始 LICENSE 已保留，归属信息见 `NOTICE`。
