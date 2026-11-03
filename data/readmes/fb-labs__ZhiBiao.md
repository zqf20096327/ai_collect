# 智标（ZhiBiao）

全流程智能招投标平台：把一份招标文件，从**解读**、**投标方案生成**、**合规检查**到**排版导出**串成一条流水线，并内置知识库与平台管理能力。

页面与 API 由同一个 FastAPI 进程在同一个端口提供（纯 B/S，无 Nginx、无反向代理）。

## 功能特性

| 域 | 能力 |
|---|---|
| 招标解读 | 上传招标文件（DOCX / PDF / 图片 OCR），输出 15 维结构化解读、评分矩阵、废标风险项与项目事实库 |
| 投标生成 | 结构模板 → 大纲 → 章节正文（SSE 流式），支持并发控制、篇幅校正、章末断尾修复、全局一致性校核 |
| 合规检查 | 资格性 / 符合性 / 规则 / LLM 语义检查，输出问题清单、检查报告与可定位的修复方案 |
| 排版导出 | DOCX 排版（模板 YAML 驱动）、格式检查与格式差异、DOCX/PDF 转换、Word/PDF 导出 |
| 知识库 | ChromaDB 向量检索，支持 Embedding API 与本地哈希向量回退 |
| 平台管理 | RBAC（24 项权限 / 4 个角色）、API Key、LLM 供应商配置、MinerU OCR 配置、技能管理、AI 配图、统计看板 |

## 技术架构

- **后端**：Python 3.12+ / FastAPI / SQLAlchemy 2.0 异步 ORM / Pydantic v2
- **数据库**：PostgreSQL 16（默认）、MySQL 8（可选）、SQLite + aiosqlite（快速体验）
- **任务**：进程内任务中心，无 Celery / Redis 队列依赖
- **前端**：React 19 / TypeScript 5 / Vite 7 / Tailwind CSS 4 / Zustand / React Router 7
- **文档处理**：python-docx、pdfplumber、mammoth、WeasyPrint
- **检索**：ChromaDB（嵌入式，本地目录持久化）

## 目录结构

```text
backend/               后端实现（与旧 services/core 无任何引用关系）
  api/                 接口层：auth / projects / interpret / generate / check / format / rbac / ...
  checking/            检查域：规则检查、LLM 检查、报告、修复方案、文件解析
  formatting/          交付域：DOCX 排版、格式检查、模板、DOC/PDF 转换
  generation/          生成域：结构模板、大纲、正文、覆盖度、导出
  platform/            平台域：技能、知识库、MinerU、AI 配图、Agent
  models.py            数据模型（18 张表）
  app.py               应用入口（web + API 同端口）
  settings.py          配置（环境变量前缀 ZHIBIAO_）
packages/web/          前端源码与构建配置
db/                    初始化 SQL（PostgreSQL / MySQL）
deploy/seed_admin.py   初始化 RBAC 与管理员账号（幂等）
docker/                镜像、compose 编排、入口脚本
docs/cleanroom/        API 契约快照（OpenAPI / schema）
templates/             DOCX 排版模板（YAML）
tests/                 后端测试
tools/                 契约校验等工具
install.ps1 / install.sh   Windows / Linux 一键安装
start.py               本地启动脚本
```

## 快速开始

### 方式一：Docker（推荐）

前置：Docker Desktop / Docker Engine 可用。

```powershell
# 1. 生成编排环境文件并填入 LLM API Key
copy docker\.env.docker.example docker\.env.docker

# 2. 启动 PostgreSQL + Redis + MinIO + 智标
docker compose -f docker/docker-compose.yml --profile infra up -d --build

# 3. 初始化管理员账号（密码只打印一次）
docker compose -f docker/docker-compose.yml exec -T api python deploy/seed_admin.py
```

访问 `http://127.0.0.1:8000/`。默认管理员邮箱 `admin@zhibiao.pro`。

也可以直接执行一键脚本，自动完成以上步骤：

```powershell
.\install.ps1          # Windows
./install.sh           # Linux
```

### 方式二：本地运行

前置：Python 3.12+、Node.js 20+、PostgreSQL（本机服务或容器）。

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -e ".[dev]"

cp .env.example .env               # 填写 ZHIBIAO_LLM_API_KEY 与数据库连接
npm --prefix packages/web install
npm --prefix packages/web run build

python deploy/seed_admin.py        # 初始化角色与管理员
python -m uvicorn backend.app:app --reload --port 8000
```

### 方式三：SQLite 快速体验

不装 PostgreSQL，仅用于本地试用：

```powershell
$env:ZHIBIAO_DB_TYPE='sqlite'
$env:ZHIBIAO_DATABASE_URL='sqlite+aiosqlite:///./zhibiao.db'
pip install aiosqlite
python -m uvicorn backend.app:app --port 8000
```

## 配置

所有配置均可用 `ZHIBIAO_` 前缀的环境变量或根目录 `.env` 覆盖，字段定义见 [settings.py](backend/settings.py)。

| 变量 | 默认值 | 说明 |
|---|---|---|
| `ZHIBIAO_DB_TYPE` | `postgresql` | `postgresql` / `mysql` / `sqlite` |
| `ZHIBIAO_DATABASE_URL` | `postgresql+asyncpg://...` | PostgreSQL / SQLite 连接串 |
| `ZHIBIAO_MYSQL_*` | `localhost:3306` | MySQL 连接参数（`DB_TYPE=mysql` 时生效） |
| `ZHIBIAO_LLM_API_KEY` | 空 | **必填**，模型类功能依赖 |
| `ZHIBIAO_LLM_API_BASE` | `https://api.deepseek.com` | 需与 Key 同源 |
| `ZHIBIAO_LLM_DEFAULT_MODEL` | `deepseek/deepseek-chat` | 默认模型 |
| `ZHIBIAO_EMBEDDING_*` | 阿里云百炼 | 知识库向量化 |
| `ZHIBIAO_MINERU_*` | `https://mineru.net/api/v4` | 扫描件 OCR |
| `ZHIBIAO_REDIS_URL` | `redis://localhost:6379/0` | 缓存 / 会话扩展 |
| `ZHIBIAO_MINIO_*` | `localhost:9000` | 对象存储 |
| `ZHIBIAO_WEB_DIST` | 自动探测 `./web_dist` | 前端静态产物目录 |
| `ZHIBIAO_PORT` | `8000` | 页面与 API 共用端口 |

> LLM 与 MinerU 也可在「平台设置」页面中配置，数据库中的配置优先于环境变量，并周期热刷新。

> UVicorn worker 必须为 1：登录会话保存在进程内字典，多 worker 会导致随机 401。

> PDF 导出依赖 WeasyPrint，Linux 需 `libpango / libcairo`，Windows 需安装 GTK3 运行时；缺失时 DOCX 导出不受影响。

## API

- 交互式文档：`http://127.0.0.1:8000/docs`
- 健康检查：`http://127.0.0.1:8000/api/health`（返回 `db_ready`）
- 契约规模：133 条路径 / 153 个操作，快照见 [openapi-snapshot.json](docs/cleanroom/openapi-snapshot.json)

## 测试

```bash
pytest -q                          # 后端测试
python tools/check_contract.py     # API 契约覆盖度校验
```

## 许可

本项目以 **GNU Affero General Public License v3.0（AGPL-3.0-only）** 发布，完整条款见 [LICENSE](LICENSE)。

- 上游来源、修改说明与第三方组件许可见 [NOTICE.md](NOTICE.md)。
- 本程序通过网络提供服务，依据 AGPL-3.0 第 13 条，用户有权获取对应源代码；对外部署时请提供指向本仓库的源码链接或书面要约。
