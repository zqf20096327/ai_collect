# artex-ld

当前版本：**0.2.0**（合并版）；Git Tag：**v0.2.0**。

基于 [ARTEX](https://github.com/Autumn-27/ARTEX) v0.3.15 的二次开发版本：AI 自主渗透测试平台。

在原有「planner-worker 自主推进」双图架构上，本版本整合了三个来源的能力：

| 来源 | 带来什么 |
|---|---|
| **artex-ld 自身** | 四个可控点：**场景可配**（任务分类/模板/种子意图）、**意图可审**（AI 预审 + 人工批准/驳回）、**执行者可指定**（自定义 agent 执行意图）、**finding 可编排**（触发器自动派生子任务/写报告/复测） |
| **[RuoJi6/ARTEX](https://github.com/RuoJi6/ARTEX) v0.3.27** | 计划任务（日历调度）、Finding 案例化（分组/合并/人工否决）、任务情报与凭据整理、代理池与出口探测、worker 池、审批裁判重试与静态脚本沙箱、HTTP 请求重放 |
| **[AntiFox-AI/antifox](https://github.com/AntiFox-AI/antifox) v2.0** | **证据驱动交付**：复现过程就地落库、漏洞富化、证据截图、交付级三语报告（docx）、知识库两层 RAG |

> ⚠️ 仅限合法授权、自有系统与隔离靶场。审核、拦截和人工确认只是辅助控制，不能替代授权边界、目标隔离与操作者判断。

---

## 目录

- [快速开始](#快速开始)
- [安装](#安装)
- [功能地图](#功能地图)
- [配套 MCP（可选增强）](#配套-mcp可选增强)
- [文档](#文档)
- [致谢与许可](#致谢与许可)

---

## 快速开始

### 方式一：Release 部署包（推荐，自带 PostgreSQL 自动初始化）

```bash
# 1. 新建目录并下载 Release 部署包
mkdir artex && cd artex
wget https://github.com/steveopen1/artex-ld/releases/download/v0.2.0/artex-0.2.0-linux-amd64.deploy.tar.gz

# 2. 解压并一键安装（自动注册 systemd 服务、初始化数据库）
tar xzf artex-0.2.0-linux-amd64.deploy.tar.gz
chmod +x install.sh
sudo bash install.sh --server artex-0.2.0-linux-amd64.deploy.tar.gz
```

### 方式二：Docker Compose（从源码构建）

```bash
git clone https://github.com/steveopen1/artex-ld.git
cd artex-ld
chmod +x deploy.sh && ./deploy.sh
# 已有镜像无需重新构建时：./deploy.sh --no-build
```

首次运行自动生成权限 `0600` 的 `.env`（含随机 PostgreSQL 密码），已有 `.env` 不会被覆盖。

### 方式三：源码构建

```bash
git clone https://github.com/steveopen1/artex-ld.git
cd artex-ld
chmod +x build.sh
./build.sh        # 需要 Go 1.26+、Node.js 20+
export ARTEX_PG_DSN='postgres://artex:密码@127.0.0.1:5432/artex?sslmode=disable'
./dist/artex-linux-amd64/artex
```

### 方式四：下载预编译二进制（Releases）

到本仓库的 [Releases](https://github.com/steveopen1/artex-ld/releases) 下载对应平台的 zip，解压后得到 `artex` + `start.sh`（Windows 为 `start.bat`）+ `skills/` + `config.example.json`。Linux ARM64（包括 ARM64 Kali）选择 `linux-arm64`，x86_64 选择 `linux-amd64`：

```bash
cp config.example.json config.json   # 填好 database 连接
./start.sh                           # → http://localhost:8787
```

### 装后管理

| 事项 | 命令 |
| --- | --- |
| 启动/停止（二进制安装） | `cd /opt/artex && ./start.sh` |
| 升级（Docker） | `./update.sh` |
| 升级（二进制） | 重跑 `install.sh --server <新包>`（自动备份数据库与旧二进制） |
| 忘记管理员密码 | `./reset-password.sh` |
| 页面一键更新 | **系统 → 系统配置 → 版本与更新**（SHA256 校验 / 原子换装 / 失败回滚，数据不受影响） |

### 首次使用

1. 浏览器访问 `http://<服务器IP>:8787/setup`，设置管理员密码。
2. 在 **系统 → LLM** 配置模型（Anthropic / OpenAI / 兼容 OpenAI 的私有网关均可）。
3. **任务 → 新建任务**：选择场景分类与 planner 模板，填写目标开跑。

### 可选运行时依赖

| 依赖 | 用途 | 缺失时的行为 |
|---|---|---|
| `python3` + `python-docx` | 渲染交付级 `.docx` 报告 | 报告生成会明确报错并说明缺什么；Markdown 交付包不受影响（纯 Go） |
| PostgreSQL **pgvector** 扩展 | 知识库语义检索 | **自动降级为关键词检索**，不阻塞启动（`settings` 记 `knowledge.vector_available`） |

启用 pgvector（需超级用户执行一次）：

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

---

## 功能地图

### 一、自主推进（上游 ARTEX 继承）

- **双图架构**：全局资产图 + 每任务探索图（goal / intent / fact / finding 血缘链），anchor 锚点相连。
- **planner-worker**：1 个 planner + N 个 worker goroutine 事件驱动推进，自主派生意图、记录事实、确认漏洞。
- **MITM 流量录制**：`:8788` 记录代理，全量留痕，可检索/回看/作为漏洞证据。
- **人在环路**：拦截规则 allow / deny / **ask** + LLM 兜底审批。

### 二、四个可控点（artex-ld 自身）

- **场景可配**：任务分类 + planner/worker 提示词模板 + 种子意图预设；建任务时快照，改模板不影响在建任务。
- **意图可审**：LLM 预审 → 人工批准/驳回/修订（乐观锁），任务级开关 `review_enabled` / `review_auto`。
- **执行者可指定**：按 `executor_key` 把意图路由给自定义 agent 执行（内网渗透 / 代码审计 / 提权）。
- **finding 可编排**：触发器按 finding 自动派生子任务、撰写报告、发起复测。

### 三、运行与调度（RuoJi6 侧）

- **计划任务**：日历窗口（一次性 / 按周，北京或系统时区）自动启停任务，支持运行历史、立即运行、批量操作。
- **任务级 worker 池**：按 LLM profile 绑定 worker 槽位；任务级 `worker_count` 覆盖全局并发（上限 50）。
- **出口与代理**：全局出口代理、代理池（导入/轮换/健康阈值/故障自愈）、出口 IP 探测与顶栏展示。
- **任务并发上限**：超限任务排队，空位自动启动。
- **任务备注**：任务与计划任务的备注（≤2000 字）。
- **真实运行时长**：只累计实际执行时长，排除暂停/排队/终态。

### 四、漏洞治理（RuoJi6 侧）

- **Finding 案例化**：把同一缺陷的重复上报归并为案例（分组 / 合并建议 / 人工否决），统一报告随案例维护。
- **任务情报与凭据整理**：agent 记录凭据 / 线索 / 敏感数据（带证据与置信度），可由凭据处理 agent 统一整理。
- **漏洞复测**：对确认漏洞发起独立复测会话，结论与原处置状态分开保存。
- **同一漏洞归并**：相似漏洞合并为一条，保留全部原始记录。
- **审批记录检索**：审批历史全文检索 + 日期/来源筛选。

### 五、证据驱动交付（AntiFox 侧）

- **复现过程就地落库**：agent 挖洞时把「入口点 / 前置条件 / 有序步骤 / 来源」写进 `findings.reproduction`；
  每步的请求与响应**逐字取自真实执行**，杜绝「复现步骤拼不全、靠编造」。
- **自动关联真实流量包**：登记时把每一步解析到当次真实录制的 MITM 报文（method+path 定位，query/body/响应特征逐级收窄），
  报告与发现页可一键跳到原始报文。
- **确认即富化**：漏洞被确认后自动生成结构化富化（描述 / 风险 / 修复建议 / CVSS 3.1），可人工编辑。
- **证据截图**：按复现步骤序号挂载截图，图注可编辑。
- **交付级报告**：`.docx`（封面 / 目录 / 页码 / 漏洞属性表）+ Markdown 交付包，**简体中文 / 繁体中文 / 英文**三语。
- **知识库两层 RAG**：全局通用知识（漏洞库 / 0day / 技巧 / 方法论）+ 本任务专属资料（授权书 / 评分规则 / 范围 / 检查项），
  agent 执行前主动检索以指导方法选择与判定标准。

---

## 配套 MCP（可选增强）

场景预设中的部分能力依赖以下 MCP，按需安装后在 **系统 → MCP** 配置并授权可见：

| MCP | 用途 | GitHub | 安装 / 启动 |
|---|---|---|---|
| **GodzillaSuper** | webshell 管理 + 立足点实连验证（`shell_list` / `shell_test`），trace_cleaner 依赖 | [Xaaaa-bip/GodzillaSuper](https://github.com/Xaaaa-bip/GodzillaSuper) | 需 Java 17+，从其 Releases 下载 `gsl5.jar`：`java -jar gsl5.jar mcp 9123 127.0.0.1`，SSE 地址 `http://127.0.0.1:9123/sse` |
| **Playwright MCP** | 浏览器操作（资产探测、截图取证） | [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | `npx @playwright/mcp --headless` |
| **ScopeSentry** | 资产测绘同步 | [DoubleShark/ScopeSentry](https://github.com/DoubleShark/ScopeSentry) | 见其 README（Docker 部署），HTTP 方式接入，API Key 在 ScopeSentry 侧生成 |

远程 MCP 可在系统设置中选择 `http`（Streamable HTTP）或 `sse`（旧版 SSE）。
旧版 SSE 服务通常使用 `GET /sse` 建立事件流，再通过服务返回的
`/message?sessionId=...` 接收 JSON-RPC 请求；配置时将 URL 填为 `/sse`，请求头按
`Authorization=Bearer <token>` 填写。

---

## 文档

| 内容 | 链接 |
| --- | --- |
| 功能详解（agent / 工具 / 审核流 / 案例） | [docs/ARTEX-功能详解.md](docs/ARTEX-功能详解.md) |
| 部署手册（依赖 / 离线构建 / 升级 / 反代） | [docs/ARTEX-部署手册.md](docs/ARTEX-部署手册.md) |
| 换环境迁移方案 | [docs/ARTEX-换环境迁移方案.md](docs/ARTEX-换环境迁移方案.md) |
| 全流程代码链 | [docs/ARTEX-二开-全流程代码链文档.md](docs/ARTEX-二开-全流程代码链文档.md) |
| 漏洞流量证据 | [docs/漏洞流量证据.md](docs/漏洞流量证据.md) |
| 更新日志 | [CHANGELOG.md](CHANGELOG.md) |

---

## 致谢与许可

致谢米斯特安全团队。

本仓库整合了三个开源项目的成果，向原作者致谢：

- [Autumn-27/ARTEX](https://github.com/Autumn-27/ARTEX) —— 原始 ARTEX 架构与代码基础
- [RuoJi6/ARTEX](https://github.com/RuoJi6/ARTEX) —— 调度、治理与运行能力
- [AntiFox-AI/antifox](https://github.com/AntiFox-AI/antifox) —— 证据驱动交付与知识库

许可：[AGPL v3](LICENSE)，遵循上游许可。二次开发组件与上游第三方组件的版权及许可义务不因修改而消失。
