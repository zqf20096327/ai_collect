# Architecture Canvas · 架构助手

通过 AI 对话生成和修改可编辑架构图。上传需求文档、表格、PDF 或图片，让助手阅读资料，再围绕同一张图持续讨论和调整。

[本机启动](#本机启动) · [无密钥体验](#无密钥体验编辑和导出) · [English](README.en.md) · [设计与源码](ARCHITECTURE.md)

![Architecture Canvas offline workspace](assets/offline-demo.png)

离线示例的真实工作区：无需密钥即可编辑和导出；图中结构为手工示例，不是模型生成效果评测。

自有对话工作区与 Excalidraw 画布，使用 DeepSeek Harness 执行模型调用、工具循环和长会话压缩。模型通过兼容 Chat Completions 的接口配置，不绑定 DeepSeek 模型。

[English](README.en.md) · [接口与嵌入](INTEGRATION.md) · [测试说明](TESTING.md) · [参与开发](CONTRIBUTING.md) · [依赖来源](THIRD_PARTY_NOTICES.md)

采用 [Apache-2.0](LICENSE)。当前为本机运行的 Alpha 版本。

模型生成初稿后，你可以手动整理画布，再用对话继续修改；修改方案先确认，固定组件保留位置。实现取舍与源码入口见 [架构说明](ARCHITECTURE.md)。

## 本机启动

需要 Python 3.10+、Node.js 22.12+、npm。克隆仓库后运行：

```bash
git clone https://github.com/weike-zhang/architecture-canvas.git
cd architecture-canvas
python3 start.py
```

首次运行自动创建虚拟环境、安装锁定的 npm 依赖并构建页面。再次运行复用安装结果。`python3 start.py --check` 检查本机依赖，`--port 5096` 更换端口。

打开 [架构助手](http://127.0.0.1:5093)，点击左下角“模型设置”，填写支持工具调用的模型地址、名称和 API Key。图片阅读需要支持视觉输入的模型，并勾选相应选项。页面输入的密钥只存在服务进程内存；重启后重新填写，或使用不纳入版本管理的 `llm.env`。

```bash
cp llm.env.example llm.env
```

手动编辑和导出可以离线使用。对话、文件语义理解、生成和修改需要可用模型服务。扫描 PDF 的文字识别可选安装 Tesseract；中文扫描件需要 `chi_sim` 语言包。没有 OCR 或读取失败会提示，不会冒充已读。

## 无密钥体验编辑和导出

运行 `python3 demo.py --output demo-session.json`，在页面“上下文 → 导入会话备份”选择生成的文件。拖动模块、改字，再导出 SVG 或 PNG。示例是手工编写的知识助手结构，不会调用模型或搜索；要用对话修改，再填写模型设置。

## 工作区能力

- 多轮讨论；首次生成直接显示，后续修改先列出变更，点击“应用修改”后生效，也可放弃方案。停止请求、失败反馈与重试。
- 上传 TXT/Markdown/CSV/JSON/YAML/XML/HTML/代码文本、DOCX、XLSX、PPTX、PDF，以及常见图片。文档由本机解析、按行读取；图片作为视觉输入发送。
- 每个会话独立保存消息、资料、当前图和最近 12 次生成历史；刷新后继续工作。
- 在上下文面板备份/导入整个会话、删除会话或资料、查看组件来源、预览资料、启停文件、填写需保留的需求摘要，开启新上下文。画布和所选文件保留，旧对话仍可查看。
- 原生画布拖动、改字、撤销、导入，导出 SVG、PNG 和包含图片的可编辑文件。AI 修改时尽量保留已有节点的手动位置和样式；可固定选中组件的位置，并限制只修改选区。手动新建的带文字形状和绑定两端的箭头会同步到语义结构。自由线条、未绑定箭头和纯装饰不会被推断为架构关系。

数据位于 `.workspace/`，可用 `ARCH_DATA_DIR` 改路径。服务重启后，应用用持久消息与需求摘要重新建立模型上下文；不冒充 SDK 原生恢复内部工具日志。运行中的会话复用 Harness，长上下文使用其压缩插件。应用以 12 万字符限制重放正文，达到上限时要求填写摘要并开启新上下文；这是正文预算，不是模型 token 用量。图片在同一运行时仅首次发送，闲置 15 分钟释放运行时，重建后重新附图。

## 统一图标

页面与架构节点统一使用 Lucide 0.468.0。架构引擎内置 32 个常用图标，按组件语义匹配，未知名称回退到通用组件图标。图标 SVG 随图嵌入，导出和离线打开无需请求图标 CDN。中文节点保留图标并预留文字空间。

更新本地图标子集：`python3 sync_icons.py`（需先安装 editor 依赖）。图标来源及许可证见 THIRD_PARTY_NOTICES.md。

## 可插拔边界

无状态 Python SDK：`diagram_sdk.render(ir)` 和 `diagram_sdk.read_document(path)`。MCP stdio 接入：`python3 mcp_server.py --root /明确授权的资料目录`；不传 `--root` 时只提供渲染工具，不读取文件。MCP 使用 2024-11-05 协议，独立于工作区会话，不修改正在编辑的图。详见 [集成说明](INTEGRATION.md)。

`harness/plugin.mjs` 注册 `read_diagram`、`create_diagram`、`update_diagram`、`list_documents`、`read_document`。自有界面和图文档独立于模型运行时，可替换提供方或解析器。

复用 Harness 的 attachment-local、token-meter、compaction-basic、compaction-tool-result-pruner；架构 Agent 仅开放上述工具，不开放 shell。基础插件配置在会话启动时装载；Tavily 搜索模块支持运行中启停、换密钥和卸载，动态注册/注销 `web_search`、`read_webpage`，无需重启当前 Harness 会话。

## 联网搜索模块

在模型设置中填写自己的 Tavily API Key，再勾选“联网搜索”。支持搜索、正文阅读、会话快照和组件来源引用。密钥仅存于服务进程内存，不进入备份或源码包。

搜索能力也可独立运行：无 npm 依赖的本机 HTTP 服务、DeepSeek Harness 插件以及直接 JS 调用，共用同一模块。配置、接入示例和热插拔边界见 [Tavily 模块说明](TAVILY_MODULE.md)。独立打包：`python3 manage.py bundle-search --output /tmp/architecture-tavily-module.zip`。

## 当前边界

服务仅监听本机 `127.0.0.1:5093`，不包含多用户账号、多人协作和生产部署。换端口：`PORT=5096 node harness/workspace.mjs`。

每会话最多 20 份资料，单文件 25 MB；正文最多 30 万字符，PDF 最多 100 页，表格最多 20 个工作表、2000 行和 100 列。达到读取边界会提示。旧版 DOC/XLS/PPT 需转换；Office 内嵌图片、表格公式重算、音视频不在当前支持范围。图片最长边压缩到 2048 像素。

生成以分层架构、业务模块和简单部署总览为主，通常不超过 22 个组件。时序图、ER 图和复杂分支流程不在当前范围。复杂列布局默认展示相邻模块的少量主关系，完整细节保留在结构数据中；简单图保留节点关系。新增节点可能需要手工排版。模型输出需人工检查。

上传内容保存在本机。启用的图片、被工具读取的文件片段、对话及架构结构会发送到你配置的模型服务。移除文件只阻止后续读取；要清除它在已有对话中的影响，需开启新上下文。

## 开发和源码包

```bash
python3 -m unittest discover -s tests -v
npm --prefix editor test
python3 manage.py build
python3 manage.py bundle --output /tmp/architecture-assistant-source.zip
```

源码包包含引擎、前端、Harness 插件、锁文件、示例、测试、文档和 SHA-256 清单；不包含模型密钥、会话资料、Git 历史、依赖或构建产物。

验证记录、平台支持范围和未发布事项见 [发布准备](RELEASE_READINESS.md)。

原 Python `server.py` 保留平台生成 API 兼容性。独立工作区使用 Node 启动命令；知了平台原有权限和会话存储不迁移。平台适配见 [INTEGRATION.md](INTEGRATION.md)。
