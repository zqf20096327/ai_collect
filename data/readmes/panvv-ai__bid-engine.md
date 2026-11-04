<p align="center">
  <img src="./bid-engine-frontend/public/bid-engine-mark.png" width="88" alt="标擎 BidEngine Logo">
</p>

<h1 align="center">标擎 BidEngine</h1>

<p align="center">面向招投标全流程的 AI 工作台</p>

<p align="center"><strong>找标 · 读标 · 写标 · 审标 · 沉淀</strong></p>

<p align="center">
  <a href="./README.md"><strong>简体中文</strong></a> ·
  <a href="./README.en.md">English</a>
</p>

<p align="center">
  <a href="#快速开始">快速开始</a> ·
  <a href="#功能概览">功能概览</a> ·
  <a href="#技术架构">技术架构</a> ·
  <a href="./CONTRIBUTING.md">参与贡献</a> ·
  <a href="./SECURITY.md">安全报告</a>
</p>

<p align="center">
  <a href="https://go.dev/"><img src="https://img.shields.io/badge/Go-%E2%89%A51.23-blue?logo=go" alt="Go 1.23+"></a>
  <a href="https://nextjs.org/"><img src="https://img.shields.io/badge/Next.js-14.2-black?logo=next.js" alt="Next.js 14.2"></a>
  <a href="https://chakra-ui.com/"><img src="https://img.shields.io/badge/Chakra%20UI-v2.8-teal?logo=chakraui" alt="Chakra UI v2.8"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-PolyForm%20Noncommercial%201.0.0-blue" alt="PolyForm Noncommercial 1.0.0"></a>
</p>

![标擎个人工作台](./images/readme/hero-workbench.png)

标擎把分散在多个工具中的招投标工作组织成一条可追溯、可协作的链路：先持续发现值得跟进的项目，再把招标文件拆成可核验的字段、条款和风险，随后完成标书大纲、正文生成与逐项审核，并将企业素材和审核规则沉淀下来。

这是一个可本地私有部署、模型可自行配置的专业工作台，而不是只负责生成一段文本的聊天工具。

> 仓库采用源码公开模式，许可证限制商业使用范围；这不等同于 OSI 定义的开源许可。详见[许可与使用范围](#许可与使用范围)。

---

## 为什么是标擎

- **全链路衔接**：情报、解析、生成、审核和素材之间的数据可以连续流转，避免反复上传、复制和手工整理。
- **结论可核验**：字段、条款、风险与审核问题都保留原文证据，可定位到 PDF 页码和区域。
- **经验可复用**：企业资质、业绩、模板、图片、素材标签和审核规则沉淀为团队资产。
- **部署与模型可控**：数据服务本地部署，LLM 支持 OpenAI 兼容接口，可按业务模块分别配置模型。

---

## 功能概览

| 模块 | 解决的问题 | 主要结果 |
|---|---|---|
| 招标情报站 | 公告分散，人工筛选成本高 | 多源采集、规则筛选、订阅提醒 |
| 招标解析 | 长文档难读，关键要求容易遗漏 | 字段、条款、风险、评分与大纲 |
| 投标文件生成 | 从零写标书耗时，素材难复用 | 大纲评审、流式写作、在线编辑与导出 |
| 投标文件审核 | 人工逐条比对容易漏项 | 清单审核、原文定位、整改闭环 |
| 素材库 | 企业材料散落，难以稳定复用 | 资质、业绩、模板、图片和知识沉淀 |
| 运营与协作 | 模型、账号、情报源和反馈难管理 | 模型配置、权限、采集运维与系统管理 |

截图用于功能说明，业务内容已脱敏或来自公开招标公告。

### 招标情报站

从人工浏览招标网站，变成按关注范围持续发现机会。

- 多源采集公开招标公告，支持关键词、地区、行业、金额和发布时间筛选。
- 用自然语言描述关注条件，命中订阅后生成站内提醒，并可同步到飞书。
- 在公告详情中直接发起招标解析，把发现机会接到后续工作流。
- 管理员可维护采集源、查看批次结果、重试失败任务并手工触发采集。

![招标情报站：公告筛选与订阅提醒](./images/readme/feature-intel.png)

### 招标解析

上传 PDF、DOC 或 DOCX，将长文档拆成可核验、可溯源的结构化结果。

- 流水线覆盖文档规范化、章节识别、字段提取、条款抽取、风险评估、标书蓝图和智能摘要。
- 字段与条款保留原文页码、坐标和多处证据，适合人工复核。
- 支持多值字段、跨页表格、告警处理、自定义关注点、暂停和按阶段重跑。
- 确认标书蓝图后，可以直接创建标书生成项目。

![招标解析：字段结论与 PDF 原文证据联动](./images/readme/feature-analysis.png)

![招标解析交互演示：从字段结论查看原文证据](./images/readme/demo-analysis-evidence.gif)

查看字段时可直接打开原文证据，结论与招标文件之间的对应关系无需人工再找。

### 投标文件生成

让标书从大纲开始组织，在统一编辑器中复用解析结果与企业素材。

- 支持空白标书、从招标文件创建和从模板创建。
- 大纲支持增删改、层级调整、排序和评审确认，可从文档标题反向同步。
- 支持整篇或单章 SSE 流式生成、中断、选区 AI 重写和自动保存。
- DOCX 与 PDF 导出支持章节页码回读，便于生成带页码的目录和溯源索引。

![投标文件生成：大纲、编辑器和章节素材联动](./images/readme/feature-file-gen.png)

### 投标文件审核

在交付前把招标要求、投标响应、风险与整改状态放在同一条检查链路上。

- 支持上传招标和投标文件，也支持关联已有解析项目或从生成项目直接发起审核。
- 按合规性、完整性和竞争力生成结构化清单，支持人工确认、驳回、备注与复检。
- 差异项可定位到投标文件原文，整改状态和责任人在同一页面闭环。
- 企业审核规则可沉淀复用，审核报告可导出为多工作表 Excel。

![投标文件审核：审核清单与投标原文对照](./images/readme/feature-audit.png)

### 素材库

把分散的企业材料整理成可检索、可复用、可持续积累的投标资产。

- 分类管理企业资质、企业业绩、文档模板和图片。
- 支持上传、预览、下载、排序、移动和编辑。
- 自动打标、图片智能描述和 OCR 解析结果可查看、确认或重试。
- 解析后的素材可供标书生成匹配，也可作为审核证据。

![素材库：企业资质与解析结果](./images/readme/feature-material.png)

### 系统管理与协作

- 按业务模块配置 OpenAI 兼容模型的 Base URL、API Key、模型 ID 和响应类型，并支持连通性测试。
- 平台级候选模型供无用户上下文的后台任务使用，支持排序和失败自动降级。
- 支持公司、用户、系统角色、招标情报源、采集批次和订阅匹配任务管理。
- 支持飞书扫码、账号绑定和招标情报提醒，以及带截图的问题反馈。
- 开放接口使用独立令牌鉴权，未配置令牌时默认关闭。

![模型配置：按业务模块独立配置 LLM](./images/readme/feature-system.png)

---

## 快速开始

以下流程适用于首次从 GitHub 克隆后，在单机上完成本地开发部署。默认使用：

- 前端：`http://localhost:3000`
- 后端：`http://localhost:1022`
- MySQL：`127.0.0.1:3306`，本地默认账号 `root`，密码 `root`，数据库 `smart-bid`

### 1. 准备环境

| 依赖 | 要求 | 用途 |
|---|---|---|
| Git | 任意近期版本 | 拉取仓库 |
| Go | `>= 1.23` | 本地运行后端 |
| Node.js | 推荐 `>= 22`，同时安装 npm | 本地运行前端 |
| MySQL | `8.0+` | 业务数据库 |
| `mysql` 客户端 | 必须存在于 `PATH` | 导入表结构，并被 `start.sh` 用于环境预检 |
| Docker Desktop | 支持 `docker compose` | Redis、MinIO、Docling、转换与采集服务 |

建议至少预留 8 GB 内存和 10 GB 磁盘空间。首次构建 `tender-intel-collector` 与 `doc-converter` 镜像时需要下载依赖并等待较长时间。

验证命令：

```bash
go version
node --version
npm --version
mysql --version
docker --version
docker compose version
```

### 2. 克隆仓库

```bash
git clone https://github.com/panviviplus/bid-engine.git
cd bid-engine
```

### 3. 创建并初始化数据库

仓库不包含业务数据和默认账号，只提供完整表结构。新建数据库后必须导入
[`docs/sql/smart-bid.sql`](./docs/sql/smart-bid.sql)。

如果你已经有满足上述连接信息的本地 MySQL：

```bash
mysql -h 127.0.0.1 -P 3306 -u root -proot \
  -e "CREATE DATABASE IF NOT EXISTS \`smart-bid\` CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;"

mysql -h 127.0.0.1 -P 3306 -u root -proot \
  smart-bid < docs/sql/smart-bid.sql
```

如果本机还没有 MySQL，可以用 Docker 启动一个仅供本地使用的实例：

```bash
docker run -d \
  --name bid-engine-mysql \
  --restart unless-stopped \
  -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=root \
  -e MYSQL_DATABASE=smart-bid \
  -e TZ=Asia/Shanghai \
  mysql:8.0 \
  --character-set-server=utf8mb4 \
  --collation-server=utf8mb4_general_ci
```

等待 MySQL 就绪后导入表结构：

```bash
until docker exec bid-engine-mysql \
  mysqladmin ping -h 127.0.0.1 -uroot -proot --silent; do
  sleep 2
done

docker exec -i bid-engine-mysql \
  mysql -uroot -proot smart-bid < docs/sql/smart-bid.sql
```

验证数据库：

```bash
mysql -h 127.0.0.1 -P 3306 -u root -proot \
  -N -e "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='smart-bid';"
```

当前完整表结构应导入 102 张表。若使用其他 MySQL 地址、账号或密码，请创建
`bid-engine-backend/conf/conf-local.override.yml` 覆盖 DSN：

```yaml
mysql:
  dsn: user:password@tcp(127.0.0.1:3306)/smart-bid?charset=utf8mb4&parseTime=true&loc=Asia%2FShanghai
```

密码中的特殊字符需要按 MySQL DSN 规则进行 URL 编码。覆盖文件已加入 `.gitignore`，不要提交真实凭据。

### 4. 启动基础服务

在项目根目录执行：

```bash
docker compose up -d --build
docker compose ps
```

该命令启动以下服务：

| 服务 | 端口 | 作用 |
|---|---|---|
| Redis | 6379 | 任务队列、任务租约与进度事件 |
| MinIO | 9000 / 9001 | 上传文件与对象存储 |
| Docling | 5002 | PDF、DOC、DOCX 结构化解析 |
| Doc-Converter | 5010 | 老旧 DOC/DOCX 转 PDF |
| Tender Collector | 5011 | 招标公告采集 |

MySQL 由部署方独立管理，不包含在 `docker-compose.yml` 中。当前 compose 文件中的 Redis 与 MinIO 数据目录是维护者本机路径；迁移到其他机器时，请先把 `volumes` 改为本机可写目录。

### 5. 启动前后端

```bash
bash start.sh
```

脚本会执行环境预检、写入前端本地代理配置、释放 `3000` 与 `1022` 端口，然后启动 Go 后端和 Next.js 前端。注意：`start.sh` 会结束占用这两个端口的现有进程。

看到前端地址后访问：

```text
http://localhost:3000/signin
```

### 6. 完成首次登录

1. 打开注册页，填写公司、姓名、手机号和密码。
2. 本地环境不接短信网关，验证码会直接显示在页面提示或接口响应的 `debugCode` 字段中。
3. 注册时填写的新公司会自动创建，注册者会成为该公司负责人。
4. 仓库没有内置演示账号；任何类似测试账号的信息都只对生成它的本地数据库有效。

### 7. 配置 LLM

登录后进入“系统管理 > 模型配置”，至少配置一个可用的 OpenAI 兼容服务：

| 字段 | 说明 |
|---|---|
| Base URL | 模型服务的 OpenAI 兼容地址，例如服务商提供的 `/v1` 地址 |
| API Key | 仅保存在本地数据库，页面默认脱敏展示 |
| 模型 ID | 例如服务商控制台中的模型标识 |
| 响应类型 | 通常选择 `Chat Completions` |

点击“测试连接”，确认成功后再保存。招标解析、标书生成、审核和素材 OCR 都依赖模型配置；后台招标情报任务还需要超管在“系统模型配置”中提供可用模型。

### 8. 可选集成

飞书登录与提醒为可选能力。需要启用时：

```bash
cp .env.example .env.local
```

然后在 `.env.local` 中填写 `FEISHU_APP_ID`、`FEISHU_APP_SECRET`，并按需设置外网可访问的 `FEISHU_PUBLIC_BASE_URL`。私有 PDF 服务、跨域白名单等部署参数使用
`bid-engine-backend/conf/conf-local.override.yml` 覆盖。完整配置模板见
[`conf-local.yml`](./bid-engine-backend/conf/conf-local.yml)。

### 9. 停止服务

- 在 `start.sh` 所在终端按 `Ctrl+C`，会停止前后端进程。
- 基础容器保持运行；需要停止时执行 `docker compose stop`。
- 首次部署创建的 Docker MySQL 需要另行执行 `docker stop bid-engine-mysql`。

### 常见问题

| 现象 | 处理方式 |
|---|---|
| `start.sh` 报 MySQL 不可达 | 确认服务监听 `127.0.0.1:3306`、账号为 `root/root`，并且系统能执行 `mysql` 命令 |
| 数据库表不存在或接口 500 | 确认已创建 `smart-bid` 并完整导入 `docs/sql/smart-bid.sql` |
| 文档解析不可用 | 执行 `docker compose ps`，确认 `docling` 和 `doc-converter` 为 running/healthy |
| 情报采集不可用 | 确认 `tender-intel-collector` 已启动，并可访问 `http://localhost:5011/healthz` |
| AI 任务持续失败 | 在“模型配置”中测试连通性，检查 Base URL、模型 ID、响应类型和账户额度 |
| 页面无法调用后端 | 从项目根目录运行 `bash start.sh`，不要绕过项目配置单独启动 Next.js |
| 端口被占用 | `start.sh` 会终止占用 3000/1022 的进程，请先保存其他项目的工作 |
| Docker 数据目录报错 | 修改 `docker-compose.yml` 中 Redis、MinIO 的 `volumes` 为本机可写路径 |

### 可选：容器方式运行前后端

完成数据库和基础服务准备后，也可以把前后端作为容器运行：

```bash
docker build -t bid-engine-backend:local -f bid-engine-backend/Dockerfile bid-engine-backend/
docker build -t bid-engine-frontend:local -f bid-engine-frontend/Dockerfile bid-engine-frontend/
bash docker-start.sh local
```

访问 `http://localhost:8080`。容器模式下前端为 `8080`、后端为 `8081`，后端通过
`host.docker.internal` 连接宿主机的 MySQL、Redis、MinIO 和解析服务。

`start.sh` 与 `docker-start.sh` 共享同一套 MySQL、Redis 和 MinIO，不要同时运行两套前后端，否则任务队列可能被重复消费。

---

## 技术架构

![标擎技术架构图](./images/ArchitectureDiagram.png)

| 层级 | 技术 |
|---|---|
| 前端 | Next.js 14 App Router、TypeScript、Chakra UI v2.8、TipTap v3 |
| 后端 | Go 1.23+、Gin v1.9、GORM v1.24、gorm.io/gen |
| 数据与队列 | MySQL 8.0+、Redis 7、MinIO |
| 文档处理 | Docling、doc-converter |
| 招标情报采集 | Python、FastAPI、Playwright、trafilatura |
| 身份与集成 | JWT Cookie、飞书扫码/IAM 回调、OpenAPI Token |
| 大模型 | OpenAI 兼容 API，用户级与系统级模型配置 |

### 典型数据流

```text
招标公告
  → 招标解析：规范化、章节、字段、条款、风险、蓝图、摘要
  → 标书生成：大纲确认、素材匹配、流式写作、在线编辑
  → 标书审核：清单生成、证据定位、人工复核、整改闭环
  → 导出交付与知识沉淀
```

---

## 项目结构

```text
bid-engine/
├── README.md                  # 中文说明（默认）
├── README.en.md               # English documentation
├── bid-engine-frontend/       # Next.js 前端
├── bid-engine-backend/        # Go 后端
├── tender-collection/         # 招标公告采集服务
├── docs/sql/                  # 数据库表结构与迁移 SQL
├── images/                    # README 截图与架构图
├── start.sh                   # 本地前后端一键启动
├── docker-compose.yml         # 基础服务
└── docker-compose-*.yaml      # 前后端容器编排
```

---

## 开发与验证

```bash
# 后端
cd bid-engine-backend
go build ./...

# 前端
cd ../bid-engine-frontend
npm install --legacy-peer-deps
npx tsc --noEmit
```

- 分支与提交约定见 [CONTRIBUTING.md](./CONTRIBUTING.md)。
- 安全问题请通过 [SECURITY.md](./SECURITY.md) 描述的私密渠道报告。
- 修改前端页面布局、UI 渲染效果或组件交互逻辑时，需要按项目规范进行设计审查并至少完成一次编译检查。
- 修改 GORM 数据模型后，应确认是否需要重新生成 `gorm.io/gen` 查询代码。

---

## 项目状态与已知边界

- 当前定位为本地研发与测试环境；公网生产部署还需要自行配置 HTTPS、反向代理、备份、监控和密钥管理。
- 本仓库只提供表结构，不附带演示账号或业务数据。
- 素材产品库等能力仍在持续完善，界面中标记为“规划中”或“开发中”的功能不代表已交付。
- AI 生成的招标解析、合规审核、风险评估和标书内容仅供参考，提交前必须由专业人员核验。
- 招标情报来自公开网站，实际投标前应以招标公告和招标文件的官方原文为准。

---

## 许可与使用范围

本项目采用 **PolyForm Noncommercial License 1.0.0**，属于源码公开（source-available），不是 OSI 定义的开源许可。

| 场景 | 是否允许 |
|---|---|
| 个人学习、研究、实验、私有部署、非商业二次开发 | 允许 |
| 慈善、教育、公共研究、公共安全或健康、环保、政府机构的非商业使用 | 允许 |
| 在 `main` 基础上 Fork、修改并提交 PR | 允许 |
| 对外提供收费服务、集成进商业产品、企业内部经营性使用 | 禁止；需取得另行书面授权 |

完整条款见 [LICENSE](./LICENSE)，名称与 Logo 授权见 [NOTICE](./NOTICE)。

**免责声明**：本软件按“现状”提供，不附带任何明示或默示担保。AI 结果不构成法律、合规或专业建议。
