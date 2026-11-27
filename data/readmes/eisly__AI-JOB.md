# AI-JOB

AI-JOB 是一个面向求职场景的应用，涵盖求职画像、简历管理与分析、岗位搜索与匹配、专项训练、项目实战和模拟面试。项目由 Vue 前端、Java 业务后端和 Python Agent 组成；具体功能和运行方式以当前代码为准。

本文以 Windows PowerShell 本地开发为例，命令默认从项目根目录执行。

## 项目结构

```text
project/frontend/   Vue 3 + Vite 前端
project/backend/    Spring Boot 业务后端和 Flyway 数据库迁移
project/agent/      Python AI Agent
requirements.txt    Python 依赖
docker-compose.yml  MySQL、Redis、Mailpit
docs/功能资料/       功能设计和开发过程记录
```

## 环境准备

- JDK 21、Maven、Node.js 和 npm。
- Python 3.11（以下示例使用 Conda）。
- Docker Desktop 和 Docker Compose。
- 可选：安装 Tesseract 及中文、英文语言包，用于图片型 PDF OCR；岗位网页渲染需要 Playwright Chromium。

```powershell
conda create -n ai-job python=3.11 -y
conda env config vars set -n ai-job PYTHONNOUSERSITE=1
conda activate ai-job
python -m pip install -r requirements.txt
python -m pip check
# 需要网页渲染时执行
python -m playwright install chromium
```

已有 `ai-job` 环境可跳过创建；在已激活的环境中设置 Conda 环境变量后，需重新激活环境。

## 本地配置与密钥

首次运行时复制模板；如果已有 `.env`，请保留原文件：

```powershell
if (-not (Test-Path .env)) { Copy-Item .env.example .env }
```

编辑项目根目录的 `.env`，自行设置 `MYSQL_PASSWORD`、`MYSQL_ROOT_PASSWORD`、`REDIS_PASSWORD` 和至少 32 字节的随机 `APP_JWT_SECRET`。数据库首次初始化后，单独修改 `.env` 不会自动修改现有 MySQL 数据卷中的密码。

按需在同一文件中添加以下变量。模板中没有的变量可以自行添加；密钥和令牌请从对应平台创建，**不要写进 README、前端代码或提交到 Git**。

| 变量 | 用途及未配置时的影响 | 官方获取入口 |
| --- | --- | --- |
| `DEEPSEEK_API_KEY` | 真实 AI 模型调用；默认 `auto` 模式下未配置会使用模拟模型。 | [DeepSeek 开放平台](https://platform.deepseek.com/)（登录后创建 API Key） |
| `TAVILY_API_KEY` | 可选，岗位网页搜索来源。 | [Tavily 控制台](https://app.tavily.com/) |
| `BRAVE_SEARCH_API_KEY` | 可选，岗位网页搜索补充来源。 | [Brave Search API 申请指南](https://api-dashboard.search.brave.com/documentation/guides/authentication) |
| `SPEECH_API_KEY` | 可选，阿里云百炼语音识别与合成。 | [百炼 API Key 获取指南](https://help.aliyun.com/zh/model-studio/get-api-key) |
| `GITHUB_TOKEN` | 可选，GitHub 公开仓库搜索；匿名访问有频率限制。 | [GitHub 个人访问令牌指南](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) |
| `GITEE_TOKEN` | 可选，Gitee 公开仓库搜索；未配置可能无法使用该来源。 | [Gitee 私人令牌指南](https://help.gitee.com/repository/settings/sync-between-gitee-github) |
| `GITCODE_TOKEN` | 可选，GitCode 公开仓库搜索；未配置可能无法使用该来源。 | [GitCode 访问令牌指南](https://docs.gitcode.com/docs/help/home/user_center/security_management/user_pat/) |

供应商可能要求开通服务、授权模型或充值，具体以其官方页面为准。仓库令牌按需授予最小权限。语音配置还需要按实际百炼业务空间设置 `SPEECH_BASE_URL`，并设置 `AGENT_SPEECH_ASR_PROVIDER=qwen`；模板默认使用 fake ASR，设置 Key 本身不会启用真实语音。语音 Key 使用 `SPEECH_API_KEY` 一种名称，避免与旧别名冲突。

`.env` 已被 Git 忽略，但忽略规则不会移除已被跟踪的文件，也不能撤销已泄露的凭据。如果密钥曾被提交或公开，应到供应商处撤销或轮换；不要在日志、截图或聊天中分享密钥。生产环境还应设置独立的服务间签名密钥、文件签名密钥等安全配置，本地默认配置不适合直接用于生产。

## 启动

### 1. MySQL、Redis 和本地邮件服务

```powershell
docker compose up -d --wait mysql redis mailpit
docker compose ps
```

默认 MySQL 为 `127.0.0.1:3307`，数据库名 `career_business`；Redis 为 `127.0.0.1:6379`。端口、用户和密码以 `.env` 为准。Mailpit 收件箱为 [http://localhost:8025](http://localhost:8025)，用于本地捕获邮件，并不代表真实邮件已发送。

MySQL 和 Redis 使用 Docker 数据卷。普通停止容器不会清空数据；`docker compose down -v` 会删除持久化卷，请勿在需要保留数据时使用。

### 2. Java 后端

另开 PowerShell，在项目根目录执行：

```powershell
cd project\backend
mvn spring-boot:run
```

默认地址为 `http://localhost:8080`。首次启动时 Flyway 创建业务表，后续按版本执行未应用的迁移；不要修改已执行的迁移，应新增迁移文件。

### 3. Python Agent

另开 PowerShell，在项目根目录执行：

```powershell
conda activate ai-job
python project/agent/run.py
```

默认监听 `127.0.0.1:8100`。Agent 读取项目根目录及 `project/agent/.env` 的配置；修改配置后需重启对应进程。真实模型和搜索服务需要网络、有效凭据及相应权限。

### 4. 前端

另开 PowerShell，在项目根目录执行：

```powershell
cd project\frontend
npm ci
npm run dev
```

浏览器访问 Vite 输出的地址，默认 [http://localhost:5173](http://localhost:5173)。默认开发代理将 `/api` 转发到 `localhost:8080`；如果端口调整，需同步检查前端代理和后端跨域配置。

## 演示数据与测试

如需演示数据，可在**空的开发库**手动导入 `project/backend/src/main/resources/db/demo/demo_data.sql`。脚本不会自动运行，也不保证重复导入；不要用于生产库。演示账号已禁用，岗位和公司为虚构数据。

```powershell
cd project\backend
mvn test
```

部分集成测试需要独立测试数据库、Redis 或 SMTP；测试可能写入数据，请勿连接共享或生产服务。更多启动及功能说明见 [服务启动过程记录](docs/功能资料/服务启动_process.md) 和 [功能资料目录](docs/功能资料/README.md)。
