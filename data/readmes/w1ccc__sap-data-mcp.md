<div align="center">

<img src="docs/images/promo-zh.webp" width="760" alt="SAP Data MCP 宣传片片头：PO 4500000417 的货款怎么还没到？为了查清楚，在 SAP GUI 里一个接一个地敲事务码">

# SAP Data MCP

**一句话，读懂你的 S/4HANA。**

让 Claude 等 AI 助手只读查询 SAP S/4HANA 的 MCP 服务，RFC/BAPI、私有云 OData、公有云 API 都能接

[English](README.en.md) · [3 步上手](#3-步上手) · [完整宣传片](https://github.com/wangyichuan0609-tech/sap-data-mcp/releases/latest) · [MIT 许可](LICENSE)

</div>

**一句话理解**：如果把 AI 助手看成一位新同事，SAP Data MCP 就是给它开的一个**只读账号，外加一本操作手册**：订单、发票、库存、供应商未清项，它都能自己去 SAP 里查，再用一句话把结论告诉你；但它改不了任何数据，碰不到你的密码，查过什么也都有记录。

![AI 助手用 4 次只读调用回答「PO 4500000417 的货款怎么还没到？」：发票比订单多 500 AUD，价格差异触发了付款冻结](docs/images/answer.jpg)

## 3 步上手

需要 Python 3.12，以及一个支持 MCP 的 AI 工具，例如 Claude Desktop、Claude Code 或 Cursor。下面以公有云 API 为例（Windows PowerShell）：

```powershell
git clone https://github.com/wangyichuan0609-tech/sap-data-mcp.git
cd sap-data-mcp
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example public_cloud\api\.env
```

1. 打开 `public_cloud\api\.env`，填写系统地址 `SAP_API_BASE_URL`，再选 Basic 认证（`SAP_API_USERNAME`、`SAP_API_PASSWORD`）或 OAuth 客户端凭证（`SAP_API_AUTH=oauth`、`SAP_API_TOKEN_URL`、`SAP_API_CLIENT_ID`、`SAP_API_CLIENT_SECRET`）。私有云 OData 的做法一样，把目录换成 `private_cloud\odata`。
2. 把服务注册到 AI 工具，路径换成你的实际位置：

   ```json
   {
     "mcpServers": {
       "sap_public_api": {
         "command": "C:\\sap-data-mcp\\.venv\\Scripts\\python.exe",
         "args": ["C:\\sap-data-mcp\\public_cloud\\api\\server.py"]
       }
     }
   }
   ```

   Claude Code 里一行就行：`claude mcp add sap_public_api -- C:\sap-data-mcp\.venv\Scripts\python.exe C:\sap-data-mcp\public_cloud\api\server.py`
3. 让 AI 先调用 `health_check` 和 `test_sap_api_connection(service="material")` 确认连通，然后直接用中文提问，比如「PO 4500000417 的货款怎么还没到？」

> 本地部署和私有云如果走 RFC/BAPI，还需要 SAP NW RFC SDK 和 PyRFC，按 [GOLDEN_PATH.md](private_cloud/rfc/docs/GOLDEN_PATH.md) 配置。每个服务都从自己 `server.py` 所在的目录读取 `.env`、`config/` 和 `logs/`，所以 AI 工具里只要写绝对路径。

## 和其他做法有什么不同

| 你可能用过的做法 | 麻烦在哪里 | SAP Data MCP 的不同 |
|---|---|---|
| **在 SAP GUI 里手工查**（ME23N、MIR4、FBL1N…） | 一个问题要开好几个事务码，单号来回复制，还会被「填写所有必填字段」拦下 | 用中文提问，AI 自己调用对应的标准读取接口，一次给出结论 |
| **自己写脚本调 RFC 或 OData** | 每个新问题都要写代码、处理认证和分页，脚本里还常常带着密码 | 三个服务共 412 个现成的只读 Tool，认证和分页都处理好了，凭证只放在本机 `.env` |
| **给 AI 一个能写入的账号或接口** | AI 理解错了就可能改到数据，事后也说不清它做过什么 | 只读白名单写在代码里，没有任何写入能力，每次调用都进审计日志 |
| **直接读底层数据库表** | 要懂表结构和字段含义，读出来的是原始数据，容易漏掉业务规则 | 优先走 SAP 标准业务接口（BAPI、标准 OData 服务、Released API），结果带着业务含义；RFC 服务里的查表 Tool 只作只读补充 |

### 用大白话说，它的好处是

- **不用记事务码**：直接问「这张 PO 为什么还没付款」，AI 会自己查订单、发票和供应商未清项。
- **只读，改不了数据**：RFC 调用必须通过 98 个标准读取函数的白名单，HTTP 只发固定的 GET 请求（唯一的 POST 是获取 OAuth token），没有任何创建、修改或过账的能力。
- **密码不经过 AI**：密码、client secret 和 token 只放在本机的 `.env` 里，在错误信息和日志中显示为 `[REDACTED]`；Tool 不接受凭证、任意 URL 或原始 OData 查询，TLS 校验始终开启。
- **查过什么都有记录**：每次调用都会写进 `logs/tool_calls_YYYY-MM-DD.jsonl`，包括参数、状态、耗时和用到的函数或 API 路径，用 `get_tool_call_log` 就能回看。
- **查不到就说查不到**：每个结果都带 `ok`、`not_found`、`partial` 或 `error` 状态。空列表不等于余额为零，缺权限不等于没有数据，清账参考不等于实际付款。
- **三种部署都能接**：本地部署和私有云走 RFC/BAPI 或 OData，公有云走 Released API；三个服务的配置、凭证和日志互相独立。
- **用你已经在用的 AI 工具**：Claude Desktop、Claude Code、Cursor 等支持 MCP 的客户端都能直接连，不需要另外搭平台或写 Agent。

### 它不做什么

为了说清楚边界：SAP Data MCP **只读**，不创建、不修改、不过账、不审批任何单据；它调用 SAP 标准接口，**不会**去操作 SAP GUI 或 Fiori 页面；它返回 SAP 给出的数据，**不替你下结论**，比如不会把清账参考当成付款记录。它也不是 SAP 官方产品，能查到哪些数据，取决于目标系统激活了哪些服务、登录用户有哪些权限。

## 包含什么

| 服务和客户端标签 | 适用系统 | 接入方式 | 只读 Tool |
|---|---|---|---|
| [`private_cloud/rfc`](private_cloud/rfc/)<br>`sap_private_rfc` | 开放 RFC 的 S/4HANA Private Edition、On-Premise；ECC / NetWeaver | RFC/BAPI，PyRFC + SAP NW RFC SDK | 95 个，基于 98 项 RFC 函数白名单 |
| [`private_cloud/odata`](private_cloud/odata/)<br>`sap_private_odata` | 开放标准 OData 服务的 Private Edition、On-Premise | OData V2/V4 over HTTPS | 159 个（155 业务 + 4 基础） |
| [`public_cloud/api`](public_cloud/api/)<br>`sap_public_api` | S/4HANA Cloud Public Edition | Released OData V4/V2 API over HTTPS | 158 个（154 业务 + 4 基础） |

三个服务合计注册 412 个只读 Tool（不同服务之间有不少同名 Tool），覆盖 8 大标准模块：MM/IM、PP、SD、WM/EWM、FI、CO、主数据 / MDG、QM。RFC 服务另有 Basis 和接口监控（ST22、SM21、SLG1、SM37、IDoc、qRFC/tRFC/bgRFC 队列、Gateway 服务注册），以及只读查表、只读查看源码和运行已审核的只显示报表。各模块的详细覆盖、接口来源和已知缺口见 [docs/COVERAGE.md](docs/COVERAGE.md)（英文）。

## 可以这样问

- 「PO 4500000417 的货款怎么还没到？」：订单、订单历史、供应商发票、供应商未清项。
- 「今天系统里有哪些短转储？」：`list_short_dumps`（RFC）。
- 「今天早上以来有没有被取消的后台作业？」：`list_background_jobs`（RFC）。
- 「列出最近三天出错的入站 IDoc。」：`list_idocs`（RFC）。
- 「物料 4000123 在 1010 工厂各库存地点、各批次有多少库存？」：RFC 用 `search_material_stock`，HTTP 服务用 `get_material_stock`。
- 「供应商 100318 在公司代码 1710 下有哪些未清项？」：`search_supplier_account_items`。

结果保留 SAP 原始的字段名、键、金额、单位和币种，零值和 false 也照样返回。列表用 `max_results` 和 `offset` 分页。监控类时间是 SAP 应用服务器本地时间，与 SAP GUI 显示一致。

## 目录结构

```text
sap-data-mcp/
├── private_cloud/
│   ├── rfc/          RFC/BAPI 服务（PyRFC + SAP NW RFC SDK）
│   └── odata/        私有云 OData 服务
├── public_cloud/
│   └── api/          公有云 Released API 服务
├── shared/           两个 HTTP 服务共用的 OData 客户端和业务 Tool
├── tests/            基于 SAP 形态样例数据的离线回归测试，不登录 SAP
├── docs/             覆盖范围说明和宣传素材
├── requirements.txt  HTTP / MCP 共用依赖；RFC 服务另加 PyRFC
└── .env.example      HTTP 服务的配置模板
```

## 文档

- [docs/COVERAGE.md](docs/COVERAGE.md)：按模块列出的覆盖范围、接口选择及 SAP 官方出处、已知边界（英文）。
- [private_cloud/rfc/README.md](private_cloud/rfc/README.md)：RFC Tool 及对应的 SAP 函数、所需权限、审计日志字段。
- [private_cloud/rfc/docs/GOLDEN_PATH.md](private_cloud/rfc/docs/GOLDEN_PATH.md)：RFC 从安装 Python 到第一次调用的完整步骤。
- [private_cloud/odata/README.md](private_cloud/odata/README.md) 和 [public_cloud/api/README.md](public_cloud/api/README.md)：两个 HTTP 服务的服务映射。

## 测试

`tests/` 里的离线回归测试使用 SAP 形态的样例数据，不登录 SAP。RFC 部分的测试会导入 PyRFC，请在装好 RFC 依赖的环境里运行：

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests
```

新增 RFC 函数时，先确认它是标准只读函数，再加入 `READ_ONLY_FUNCTIONS`；不在名单上的函数会被 Connector 直接拒绝。

## 声明

独立开源项目，与 SAP SE 无隶属关系，也未获其认可。SAP、S/4HANA 及其他 SAP 产品名称是 SAP SE 的商标。宣传片中的业务数据为演示虚构。

## License

[MIT](LICENSE)
