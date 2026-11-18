# 沅楚 YuanChu · AI 短剧生成工作台（开源版）

## 目录

- [特性](#特性)
- [截图](#截图)
- [部署指南](#部署指南)
  - [1. 前置准备](#1-前置准备)
  - [2. 配置](#2-配置)
  - [3. 启动](#3-启动)
  - [4. 首次使用](#4-首次使用)
  - [5. 公网部署要点](#5-公网部署要点)
  - [6. 常见问题](#6-常见问题)
- [自备清单](#自备清单)
- [分层架构与模块门禁](#分层架构与模块门禁)
- [文档](#文档)
- [开源范围说明](#开源范围说明)
- [合规提示](#合规提示)
- [联系作者](#联系作者)
- [License](#license)

**小说 → 分镜 → 关键帧 → 成片的一站式生成流水线。** 上传小说/剧本，系统提取分镜、确认资产与对白，在工作室里生成关键帧、参考图与视频，Agent 与无限画布贯穿全程。FastAPI + Celery + 多供应商生成网关 + React 工作台，基于 Apache-2.0 开源项目 [Jellyfish](https://github.com/Forget-C/Jellyfish) 构建。

## 特性

- **分镜流水线**：章节内容提取分镜 → 编辑页完成资产/对白提取确认（推进到 ready）→ 工作室生成关键帧、参考图与视频，职责边界清晰
- **多供应商生成网关**：文本 / 图像 / 视频 / TTS 全品类，BYO Key（自带凭证），供应商与模型可插拔，按能力路由
- **Agent 编排**：langgraph ReAct 代理 + 按身份闭包的工具集，画布与流水线均可触发
- **无限画布**：节点式工作流编排，图片 / 音频 / 视频任务即建即连，任务去重与并发控制
- **多租户与 RBAC**：租户隔离、自定义角色权限、团队协作与项目可见性、席位与项目配额
- **任务中心**：通用任务状态面板（进度 / 取消 / 回跳），Celery 异步执行 + 任务关联追溯
- **就绪度检查**：视频生成前校验模型 / 资产 / 参数就绪度，缺什么补什么
- **Docker Compose 分组部署**：基础设施 / 应用 / 前端分组编排，自带依赖等待、建库建表与种子数据

## 部署指南

### 1. 前置准备

| 组件 | 说明 |
|---|---|
| Docker + Docker Compose | 部署载体（compose 分组：infra / app / web）|
| MySQL 8.x | 业务库（compose 自带，也可外接），启动时自动建库建表 |
| Redis | Celery 队列 + 限流 + 验证码 |
| S3 兼容对象存储 | 生成产物与文件管理（compose 自带 rustfs，MinIO / OSS 亦可）|
| 模型供应商凭证 | 文本 / 图像 / 视频 / TTS 至少各一家，BYO Key |

### 2. 配置

```bash
git clone https://github.com/hyper-open/yuanchu.git
cd yuanchu/deploy/compose

cp env/common.env.example env/common.env
cp env/infra.env.example env/infra.env
cp env/app.env.example env/app.env
cp env/web.env.example env/web.env
```

必改项（其余变量均有默认值，可渐进覆盖）：

| 变量 | 说明 |
|---|---|
| SETTINGS_SECRET_KEY | 敏感配置加密主密钥（**随机长字符串**）：缺失会静默回退开发密钥，等于库里的模型 Key / SMTP 口令可被解出 |
| MYSQL_PASSWORD | 业务库口令（MYSQL_USER 同步改）|
| RUSTFS_ACCESS_KEY / RUSTFS_SECRET_KEY | 对象存储凭证（外接 S3 时改填 S3_*）|
| S3_BUCKET_NAME | 生成产物桶名（缺失启动报错）|
| COMPLIANCE_MODE | 合规模式声明：internal（自用）/ b2b / public，部署时显式声明 |
| LICENSE_PATH（可选）| 商业版许可文件路径，开源版留空 |

### 3. 启动

```bash
# 基础设施（MySQL / Redis / rustfs）
docker compose --env-file env/common.env --env-file env/infra.env -f parts/infra.yml up -d

# 全量应用（后端 / worker / 前端）
docker compose --env-file env/common.env --env-file env/app.env \
  --env-file env/web.env -f docker-compose.yml up -d
```

首次启动自动完成：等待依赖就绪 → 建库建表（alembic）→ 对象存储建桶 → 风格参考种子导入。健康检查：访问 http://127.0.0.1:28000/api/v1/health 返回 200。

> 前端 http://127.0.0.1:27788；后端 API 28000；管理端服务 28001/28080 仅绑内网，开源版默认不启用。

### 4. 首次使用

1. **注册租户**：前端注册账号，自动创建所属租户
2. **配模型**：「设置 → 模型」填入各品类供应商凭证（BYO Key），配好默认模型与降级链
3. **建项目**：上传小说 / 剧本 → 提取分镜 → 编辑页确认资产与对白 → 工作室生成关键帧与视频
4. **看进度**：任务中心统一跟踪生成任务，画布页可自由编排图片 / 音频 / 视频节点

### 5. 公网部署要点

- 前端端口 27788、后端 28000（可在 compose 改），生产建议前置 Nginx 做 HTTPS 与域名
- 对象存储若用云厂商 OSS，直接改 S3_* 指向外部桶，容器内 rustfs 可停用
- 视频处理依赖 ffmpeg（镜像已内置）；自编译 ffmpeg 需带 libfreetype，否则水印/抽帧走 Pillow 降级档

### 6. 常见问题

| 现象 | 原因与处理 |
|---|---|
| 容器 Up 但许可/审计未生效 | MySQL 未就绪时这些启动步骤会静默跳过——确认 wait_for_infra 通过后再看应用日志 |
| 启动报 S3 HeadBucket 404 | 桶在启动时自动创建；检查 S3_BUCKET_NAME 与存储凭证 |
| 生成任务一直 503 | 对应品类未配置可用模型或凭证失效——「设置 → 模型」补齐 |
| uv sync 报 Distribution not found | backend-kernel/ 必须与 backend/ 同级（path 依赖 ../backend-kernel）|
| 导出报「ffmpeg 缺少 drawtext/overlay」 | 自建 ffmpeg 未编 libfreetype：装依赖，或确认 Pillow 字体可用（自动降级）|
| 商业功能报 501 | 正常：开源版不含增值模块（机审/备案/计费等），见下「开源范围说明」|

### 自备清单

| 项 | 用途 |
|---|---|
| 文本模型 API Key | 分镜提取 / Agent / 剧本处理（OpenAI 兼容接口均可）|
| 图像 / 视频模型 API Key | 关键帧与视频生成（各支持一家即可跑通）|
| TTS API Key（可选）| 对白配音与画布音频 |
| S3 兼容对象存储 | 生成产物与文件管理（compose 自带 rustfs 可免）|

## 截图

### 登录

![登录](docs/images/screenshot-login.png)

### 项目列表

![项目列表](docs/images/screenshot-projects.png)

### 项目工作台（分镜准备流水线）

![项目工作台](docs/images/screenshot-workbench.png)

### 无限画布

![无限画布](docs/images/screenshot-canvas.png)

### 任务中心

![任务中心](docs/images/screenshot-tasks.png)

### 模型管理（BYO Key）

![模型管理](docs/images/screenshot-models.png)

## 分层架构与模块门禁

- **三工程分层**：backend/ 业务端 + backend-kernel/ 共享内核（独立工程，path 依赖）+ front-kernel/ 前端内核——内核不反向依赖任何一端，边界有测试锁定
- **BYO Key 成本模型**：平台不代采模型，真实扣费发生在客户自己的供应商账号；任务配额（并发 / 存储 / 任务数）作为防滥用底线
- **模块门禁**：增值能力（机审 / 合规留痕 / 微短剧备案 / 订阅计费）按 Ed25519 实例许可授权，实现随闭源包装配，开源版对应入口返回 501 引导——见 scripts/opensource-freeze.yaml

## 文档

- [架构文档](site/content/docs/architecture/) —— 当前实现、状态语义、页面职责
- [开发指南](site/content/docs/guide/) —— 环境、流程、接入方式
- [参考资料](site/content/docs/reference/) —— 稳定契约与字典

## 开源范围说明

- 本仓库包含：生成流水线 / Agent / 画布 / 多租户 / 任务系统 / Web 工作台 / 部署编排
- **不在本仓库**：平台管理端（运营后台）、商业增值模块（内容机审、AIGC 合规留痕、微短剧备案辅助、订阅计费）——以闭源包随商业授权分发（部署见 deploy/compose/parts/commercial.yml）
- 测试需完整源码树环境：docker compose --profile test（见 deploy/compose/parts/test.yml）

## 合规提示

- 生成内容已支持 AIGC 显式标识配置（文案 / 档位可配）；若你的产品面向公众提供生成服务，**上线需申请「深度合成」相关服务类目**，并遵守《人工智能生成合成内容标识办法》
- 请遵守《生成式人工智能服务管理暂行办法》：自行面向公众提供生成服务需完成相应算法备案，或与已备案供应商签署合作协议；COMPLIANCE_MODE 需按部署事实如实声明

## 联系作者

- 技术问题 / Bug 反馈：请提 [Issue](../../issues)，方便沉淀给后来人
- 交流 / 商业授权 / 合作：扫码添加微信（备注 GitHub）

<p align="center"><img src="docs/images/wechat-qrcode.png" width="240" alt="作者微信"></p>

## License

[Apache-2.0](LICENSE)。本项目为 [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish)
（Apache-2.0）的衍生作品，保留上游 NOTICE 与归属；上游各语言 README 见 docs/README.*.md。
