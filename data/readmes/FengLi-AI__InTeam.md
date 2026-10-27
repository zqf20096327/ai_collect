# InTeam · 企业知识与办公助手

InTeam 是面向中小企业的**企业知识问答与办公任务 Agent**。员工可以在同一个工作空间查阅企业资料、整理准备清单，也可以生成活动方案、报价表和申请单，继续修改、预览并确认下载。

企业问答通过 Dify Chatflow 检索资料并回答；办公助手结合模型工具调用、固定工作流和文件生成程序，将任务要求整理成可编辑的 Word 或 Excel。涉及价格、税率、费用等必要信息时，先核对输入，缺失内容向用户补问。

[![CI](https://github.com/FengLi-AI/InTeam/actions/workflows/ci.yml/badge.svg)](https://github.com/FengLi-AI/InTeam/actions/workflows/ci.yml)

## 可以用它做什么

| 能力 | 示例需求 | 交付内容 |
|---|---|---|
| 企业知识问答 | “报销和权限申请分别用哪个系统？” | 基于企业资料的流式回答、参考来源和追问建议 |
| 自由任务 | “整理项目评审前需要准备的材料。” | 准备清单、资料依据和待核实事项 |
| 活动方案 | “为产品体验活动准备一份策划方案。” | 包含目标、流程、资源安排与预算的可编辑 Word |
| 报价 Excel | “设计服务 2 项，每项 800 元；印刷 100 份，每份 12 元，不计税费。” | 明细、公式与合计完整的可编辑 Excel |
| 加班申请 | “整理一份跨午夜的加班申请。” | 核对起止时间、休息时长和事由后的 Word 申请单 |
| 报销申请 | “把交通和餐饮费用整理成报销单。” | 按项目汇总金额、保留凭证信息的 Word 申请单 |

工作台采用知识导航、对话和任务详情三栏布局，支持调整栏宽；手机和平板通过面板切换查看内容。历史入职记录、候选行动和原有任务保留在历史入口。

## 从需求到文件

1. **说明需求**：输入任务目标，选择自由任务或固定文件类型。
2. **核对资料与字段**：助手按需搜索、阅读已授权资料；缺少必要字段时补问。
3. **生成初稿**：展示执行步骤、资料来源和产物预览，待核实事项集中放在工作台。
4. **继续修改**：在同一任务中追加要求，修改指定字段或正文，保存为新版本。
5. **人工确认与下载**：确认当前文件版本；后续修改会生成新的待确认版本。

活动方案按“检索资料 → 生成大纲 → 产出初稿 → 等待确认 → 输出最终稿”运行。等待确认会保存状态并释放执行名额，刷新页面后可以继续处理。用户可以停止正在执行的任务，再基于已保存的要求继续。

## Agent 与工作流

企业问答和办公任务有各自的执行链路：

- **企业问答**：Dify Chatflow 负责检索与生成，FastAPI 网关负责身份、会话、流式事件和空检索保护。
- **自由任务**：后端 Agent Loop 让模型根据工具结果决定继续检索、阅读全文、澄清需求或交付准备材料。
- **办公文件**：固定工作流管理阶段与人工确认；模型整理结构化内容，程序负责金额、税额、工时计算及 Word / Excel 渲染。

办公 Agent 的资料工具为 `search_knowledge` 和 `read_document`。它们在服务端限定的 Markdown 资料中进行权限过滤和中文词法检索。工具参数、执行预算、停止信号和用户身份由后端控制。

引用核对会检查资料是否实际读取、引文是否来自返回内容，并审查事实、重复内容与建议条件。模型核验仍可能出错，生成内容需要人工审核。

## 文件与版本

- Word 保留可编辑段落和表格；Excel 保留可编辑数据、公式及计算结果。
- 文件按版本保存，预览、下载和确认绑定同一版本与 SHA-256，避免确认后拿到另一份内容。
- 修改指定字段或文本时保留其他内容，已确认文件也可以继续修改成新版本。
- 加班和报销默认使用明确标识的示例模板，也支持上传含受支持占位符的公司 DOCX 模板。
- 模板区提供参考底稿下载；来源元数据标明示例资料及其适用范围。

报价目前支持一单一个税率、含税或未税单价。DOCX 模板限于加班和报销申请，文件需不超过 60 KB，并符合占位符及文件安全检查。任意 Excel 模板填充、分项税率、PPT / PDF 生成和一次生成多种文件尚未支持。

确认表示用户接受当前草稿或文件。助手不会代签、审批、提交申请、发送文件或修改企业业务系统。

## 技术栈

| 层级 | 实现 |
|---|---|
| 前端 | Next.js 16、React 19、TypeScript、TanStack Query |
| 后端 | FastAPI、SQLAlchemy、Alembic、SSE |
| 企业问答 | Dify Chatflow、结构化输出、会话与检索保护 |
| 办公 Agent | OpenAI 兼容工具调用接口、受限工具循环、固定工作流 |
| 文件生成 | python-docx、XlsxWriter、openpyxl、docx-preview |
| 持久化 | SQLite、任务与文件版本、可配置的对象存储备份 |
| 测试 | Pytest、Vitest、Playwright |

## 项目结构

```text
InTeam/
├── backend/
│   ├── app/services/agent/
│   │   ├── runtime.py           自由任务 Agent Loop
│   │   ├── workflows/           固定工作流与确认状态
│   │   └── documents/           文档字段、计算、渲染与下载
│   ├── data/agent-knowledge/    办公示例资料
│   ├── data/agent-templates/    示例模板与参考底稿
│   ├── alembic/                数据库迁移
│   └── tests/                  后端测试
├── frontend/                   问答、任务工作台与文件预览
├── dify/                       Chatflow、企业资料与 RAG 用例
├── eval/                       任务验收用例与结果模板
├── docs/                       产品文档和历史版本记录
└── .env.example                配置模板
```

## 本地运行

需要 Python 3.11 和 Node.js 22 或更高版本。以下命令均从仓库根目录开始。

### 1. 配置后端

```bash
cd backend
python3.11 -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
cp .env.example .env
```

在 `backend/.env` 中填写配置：

```dotenv
APP_ENV=development
SESSION_SECRET=请替换为至少32字符的随机值
INVITE_PEPPER=请替换为另一段至少32字符的随机值

# 企业问答
CHAT_PROVIDER=dify
DIFY_BASE_URL=https://api.dify.ai/v1
DIFY_APP_API_KEY=请填写你的Dify应用APIKey

# 办公助手：模型需要支持OpenAI兼容的工具调用接口
AGENT_ENABLED=true
AGENT_BASE_URL=https://api.deepseek.com
AGENT_API_KEY=请填写你的模型APIKey
AGENT_MODEL=deepseek-flash
```

`AGENT_API_KEY` 留空时会复用 `DEEPSEEK_API_KEY`。模型名称需与你的服务商账户实际可用模型一致。开发环境默认启用办公助手，生产环境需要显式启用。

默认配置中的 `CHAT_PROVIDER=legacy` 保留本地演示与旧检索链路；使用 Dify 企业问答需按上述配置切换。未填写模型密钥不能验证真实生成效果。

### 2. 初始化数据库并启动

仍在 `backend/` 下执行：

```bash
.venv/bin/python migrate.py upgrade head
.venv/bin/python cli_invite.py generate --count 1 --note "local development"
.venv/bin/uvicorn app.main:app --host 127.0.0.1 --port 8000
```

保留命令输出的邀请码，用于本地登录。拉取包含新迁移的版本后，应再次执行迁移命令。`migrate.py` 会过滤外置磁盘生成的 `._` 元数据文件。

### 3. 启动前端

在仓库根目录打开另一个终端：

```bash
cd frontend
npm ci
npm run dev
```

打开 <http://localhost:3000>，输入邀请码进入工作空间。前端默认将 `/api/v1` 转发到 `http://127.0.0.1:8000`；需要修改后端地址时，在 `frontend/.env.local` 中配置 `BACKEND_URL`。

## Dify 与企业资料

1. 导入 [Chatflow DSL](dify/exports/InTeam-Onboarding-Agent-v1.9-published.yml)。
2. 建立公司通识、岗位与协作、项目知识三个知识库。
3. 根据企业实际资料维护 `dify/knowledge-source/`，重新绑定知识库与模型。
4. 发布 Chatflow，将应用 API Key 配置在后端。

办公任务资料位于 `backend/data/agent-knowledge/office/`。仓库自带资料和模板用于演示，实际企业使用前应替换并核实来源、制度和适用范围。

单独部署后端前，可在仓库根目录执行 `python backend/scripts/package_knowledge.py` 打包企业资料。生产环境还需配置资料 ACL、会话密钥、访问域名及数据库备份。后端启动入口为 `python start.py`，负责备份恢复、迁移和服务启动。办公任务运行器采用单进程任务管理，不能直接作为多 worker 调度系统使用。

## 验证

后端离线测试：

```bash
cd backend
.venv/bin/python -m pytest tests -q
```

前端检查：

```bash
cd frontend
npm test
npm run lint
npm run typecheck
npm run build
```

在仓库根目录校验用例：

```bash
python3 eval/validate_cases.py
python3 dify/evaluation/validate_cases.py
```

自动化检查覆盖文件计算与渲染、任务状态、版本确认、权限、迁移及界面交互。用例结构校验、mock 测试与真实模型内容验收分别记录；离线通过不代表任意输入都能得到正确结果。当前版本的完整真实模型验收仍有待完成的项目。

## 文档与许可证

- [任务验收方法与用例](eval/README.md)
- [Dify 资产说明](dify/README.md)
- [Dify Chatflow 说明](dify/chatflow/README.md)
- [历史产品需求](docs/InTeam-PRD-v1.8.md)
- [历史 Agent 版本记录](docs/agent-release-v1.9.md)

历史文档与截图用于追溯，当前入口和能力以本页及源码为准。

项目自有代码采用 [MIT License](LICENSE)。React Bits 衍生组件的许可见 [第三方声明](THIRD_PARTY_NOTICES.md)。MiSans 字体不随仓库分发，可按[字体说明](frontend/public/fonts/README.md)自行安装；未安装时使用系统字体。
