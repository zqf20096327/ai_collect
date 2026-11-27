# ComfyShop

**简体中文** · [English](README.en.md)

<p>
  <img src="packages/tokens/src/brand/comfyshop-logo.svg" alt="ComfyShop 图标" width="64" />
  <img src="packages/tokens/src/brand/comfyshop-wordmark.svg" alt="ComfyShop 字标" width="192" />
</p>

**RunningHub 的开源自托管替代方案，面向使用 ComfyUI 的团队。**

把调好的 ComfyUI 工作流发布成同事可以直接使用的生成表单。在同一个网页提交图片或视频生成任务、跟踪每次执行、找到原始成品，再用已有参数发起下一轮。个人和团队空间均可使用本空间的 ComfyUI 工作机、RunningHub 连接和平台的公开官方工作流。数据库与媒体存放在你部署的平台环境中。

简体中文、台湾繁体中文、英文、日文和韩文共用页面地址、公开目录和同一账号下的个人记录。页头的语言选择会保存在浏览器中，切换时仍停留在当前页面。首次访问按浏览器语言偏好匹配，再回退到部署默认语言。官方内容随界面语言显示，作者内容保留原文。

[Docker 快速启动](#docker-快速启动) · [界面截图](#界面截图) · [工作机接入](integrations/comfyui/README.md) · [RunningHub 连接](integrations/runninghub-worker/README.md) · [GitHub Issues](https://github.com/ComfyShop-ORG/ComfyShop/issues)

[![GitHub Actions CI](https://github.com/ComfyShop-ORG/ComfyShop/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/ComfyShop-ORG/ComfyShop/actions/workflows/ci.yml) · [MIT 许可证](LICENSE)

![ComfyShop 桌面端公开工作流库](docs/screenshots/desktop-catalog.jpg)

## 从工作流到成品

1. **让流程可以复用。** 在 ComfyUI 调好节点并导出 API JSON。在 ComfyShop 导入后，作者可以整理表单字段、提示和默认值。工作流版本完成一次真实执行后即可发布，新草稿可以继续调试。
2. **从网页提交生成。** 选择工作流，填写提示词、参考素材和其他参数。ComfyUI 工作流使用自己的在线工作机，RunningHub 工作流使用自己在相应站点的连接，官方模型由平台分配工作机。提交后可以跟踪排队和执行进度。
3. **追溯每一次执行。** 一次提交可以执行多次。每次执行都保留工作流版本、实际参数和原始输出，包含种子的流程会保留实际使用的种子。在「我的 → 结果」里，即使同一批次后续失败，也能查看先前成功的结果，并从历史执行载入参数重跑。
4. **按需共享作品。** 从一次成功执行中选择成品和封面。网页默认选中「公开完整输入（含素材）」，访客可查看参数并下载列出的参考文件。选择「公开参数」或「仅公开成品」可让参考文件保持私有。

工作流、任务和成品的详细规则见 [功能与使用](docs/requirements.md)。

## 运行

### Docker 快速启动

在安装了 Docker 和 Docker Compose 的机器上启动平台。

```sh
git clone https://github.com/ComfyShop-ORG/ComfyShop.git
cd ComfyShop
docker compose up -d --build --wait
```

1. 打开平台地址，在登录弹框创建账号。平台和工作机同机运行时，可在该机器上打开 `http://localhost:8688`。工作机在另一台机器上时，使用工作机能访问的服务器 IP 或域名打开网页。
2. 在「工作机」页下载启动包。包内 `worker.json` 默认记录下载时访问的平台地址，也可用 `COMFYSHOP_PUBLIC_URL` 指定对外地址。在已运行 ComfyUI 的 GPU 机器上解压并启动，再到网页确认接入。
3. 在「我的 → 工作流」导入一份 **ComfyUI API JSON**，选择工作机并提交生成。完成后可在「我的 → 结果」查看和下载原文件。

全新部署从空库开始。基础版默认将 SQLite 和媒体保存在挂载到 `/data` 的数据卷中，也可使用外部 S3 兼容存储。团队版使用 PostgreSQL，可选本地文件、本地 RustFS 或外部 S3，拥有独立的配置示例。公开工作流和作品可由任何能访问该实例的访客浏览。用于团队内部时，将实例放在团队可访问的网络或访问控制之后。端口、HTTPS 和备份见 [Docker 部署](docs/deployment.md)。

### 本地开发

使用 Node.js 22.13+（22.x）或 24+、pnpm 12.21.0、uv，以及 `.python-version` 指定的 Python 3.12。本地 API 处理视频或运行视频相关测试时，需要 `ffmpeg` 和 `ffprobe`。

```sh
pnpm install --frozen-lockfile
uv sync --all-packages --locked
pnpm dev
```

默认开发网页为 `http://127.0.0.1:5173`，API 文档为 `http://127.0.0.1:8688/docs`。使用 `pnpm build` 和 `pnpm start` 可在本机启动同源的生产构建。

## 界面截图

### 桌面端工作流与公开作品

![桌面端工作流详情与公开作品](docs/screenshots/desktop-workflow.jpg)

### 手机端

|                                      公开工作流库                                      |                                       登录                                       |
| :------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------: |
| <img src="docs/screenshots/mobile-catalog.jpg" alt="手机端公开工作流库" width="280" /> | <img src="docs/screenshots/mobile-login.jpg" alt="手机端登录弹框" width="280" /> |

## 连接工作机

从「工作机」下载启动包。工作机可独立运行，也可作为 ComfyUI 插件接入。模型和自定义节点安装在执行该流程的 ComfyUI 环境中。每个账号可以绑定多台工作机，并选择本次任务由哪一台执行。安装方式、手动接入和连接恢复见 [工作机文档](integrations/comfyui/README.md)。

## 安装并使用 Skill

在部署实例打开「账户 → 安装 Skill」或访问安装页 `/skill`，配置 Codex 或 Claude Code。Skill 使用自己的登录会话，沿用对应账号权限，可以查询工作流、准备多组参数、提交生成任务及取回成品。每组不同输入会作为独立任务入队。 [Skill 用法](integrations/skills/comfyshop/SKILL.md) · [平台操作](integrations/skills/comfyshop/references/operations.md)

## 数据与迁移

通过 `.env.example` 可查看平台的环境变量和数据位置。数据库与媒体随部署持久化。生产启动时执行 Alembic 迁移。需要保留数据时，按部署方式备份数据库和媒体。 [部署和备份](docs/deployment.md) · [环境变量示例](.env.example)

## 目录与检查

| 目录           | 内容                                               |
| -------------- | -------------------------------------------------- |
| `apps/web`     | React 界面                                         |
| `apps/api`     | FastAPI、任务与权限规则、Alembic 迁移              |
| `packages`     | 类型化 API 客户端、组件和设计 tokens               |
| `integrations` | ComfyUI、官方、RunningHub 工作机和外部客户端 Skill |
| `libs`         | 工作机共用协议、平台媒体处理库                     |

```sh
uv run --all-packages playwright install --only-shell chromium
pnpm check
pnpm format:check
pnpm test
pnpm build
```

GitHub Actions 还会核对 OpenAPI 生成结果和数据库模型是否与迁移一致。 [架构](docs/architecture.md) · [设计规则](docs/design-system.md) · [验证说明](docs/verification.md) · [CI 工作流](https://github.com/ComfyShop-ORG/ComfyShop/actions/workflows/ci.yml)

## 许可证

ComfyShop 使用 MIT 许可证。 [LICENSE](LICENSE)
