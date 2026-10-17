# SS-Agent

SS-Agent 是面向科研写作、数学建模竞赛和长流程知识工作的桌面 Agent 工作台。它把资料检索、选题、建模、代码实现、实验、绘图、写作、审稿和导出组织成可暂停、可检查、可继续的工作流。

当前仓库是 SS-Agent `1.7.0` 的 MIT 开源源码版。前端提供经过清理、可读且可运行的生产 bundle；由于原始 React/Vite 工程和 source map 不存在，本仓库不将其声明为原始组件源码。

## 支持的工作

### 数学建模竞赛

内置赛题分析、建模求解、编程实现、统计分析、图表生成、逻辑复核、论文写作、格式检查和 PDF/DOCX 导出流程。下表只列出仓库中已有对应模板的竞赛：

| 竞赛 | 常用搜索名称 | 工作流 |
| --- | --- | --- |
| 全国大学生数学建模竞赛 | CUMCM、国赛、全国赛 | 中文论文与国赛模板 |
| 美国大学生数学建模竞赛 | MCM、ICM、COMAP、美赛 | 英文论文与美赛模板 |
| 中国研究生数学建模竞赛 | 华为杯、研究生数学建模 | 中文论文与华为杯模板 |
| 亚太地区大学生数学建模竞赛 | APMCM、亚太杯、亚太赛 | 中文及英文赛项 |
| MathorCup 高校数学建模挑战赛 | MathorCup | 中文论文与 MathorCup 模板 |
| 全国大学生统计建模大赛 | 统计建模大赛、统计建模国赛 | 统计建模论文模板 |
| 华中地区大学生数学建模邀请赛 | 华中杯 | 中文建模论文 |
| 五一数学建模竞赛 | 五一杯、51MCM | 中文建模论文与五一杯模板 |
| 数维杯大学生数学建模挑战赛 | 数维杯 | 中文赛项与数维杯模板 |
| 长三角高校数学建模竞赛 | 长三角数学建模、长三角杯 | 中文论文与长三角模板 |
| 全国大学生电工数学建模竞赛 | 电工杯、电工数学建模 | 中文论文与电工杯模板 |
| 华数杯全国大学生数学建模竞赛 | 华数杯 | 中文论文与华数杯模板 |
| 东三省数学建模联赛 | 东三省数学建模 | 中文论文与东三省模板 |

其他采用常见数学建模论文结构的校赛、省赛和国际赛，也可以使用通用中文或英文模板。

### 科研与论文写作

- 中文和英文科研论文：大纲、实验、图表、LaTeX/DOCX 写作、编译与迭代改进
- Nature 风格论文：数据分析、组合图、写作、审稿和编译
- 文献综述、开题报告、课程论文、课程报告和人文社科论文
- 从已有代码、数据、图片和实验资产整理成论文
- Idea 发现、文献调研、新颖性检查、实验规划和自动审稿循环
- 论文插图、Nature 风格图、Mermaid/Draw.io 架构图、海报和答辩幻灯片
- 审稿意见回复（rebuttal）、质量检查、结果到论点的证据整理
- 基金申请材料、专利交底书和软件著作权申请资料
- 软件项目需求、设计、前后端开发、测试和项目报告

所有内容均应由使用者复核。文献、数据、公式、实验结果和竞赛规则仍需以原始来源与主办方要求为准。

## 快速部署

### 运行要求

| 环境 | 要求 | 用途 |
| --- | --- | --- |
| Windows | Windows 10/11 x64 | 当前桌面端支持平台 |
| Node.js | 20 或更高版本 | Electron、Mermaid、KaTeX、DOCX 工具 |
| Python | 3.11 或更高版本 | FastAPI 后端、工作流和数据工具 |
| 模型 | OpenAI 兼容 API 或 Claude CLI | Agent 推理与生成 |
| Git | 可选 | 代码与实验版本管理 |
| Pandoc | 可选 | 文档格式转换 |
| Draw.io | 可选 | 流程图与架构图 |
| MiKTeX/TeX Live | 可选 | LaTeX 和中文 PDF 编译 |

### Windows PowerShell

下面的命令不激活虚拟环境，因此不受 PowerShell 脚本执行策略影响：

```powershell
git clone https://github.com/SUSU0409/SS-Agent.git
Set-Location SS-Agent

npm install
python -m venv .venv
& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -r apps\backend\requirements.txt

npm start
```

首次启动后，在“设置”中创建模型预设，填写模型服务地址、API Key 和模型名称，再分配给执行、审稿或编辑角色。API Key 和工作流数据保存在本机用户数据目录，不应提交到 Git。

需要数据分析、机器学习、图像处理和竞赛科学计算环境时，再安装可选依赖：

```powershell
& .\.venv\Scripts\python.exe -m pip install -r apps\backend\requirements-science.in
```

如果 `npm start` 没有使用虚拟环境中的 Python，可在当前终端显式指定：

```powershell
$env:SS_AGENT_PYTHON = (Resolve-Path .\.venv\Scripts\python.exe).Path
npm start
```

## 配置与数据

| 环境变量 | 必需 | 说明 |
| --- | --- | --- |
| `SS_AGENT_PYTHON` | 否 | 指定 Python 解释器 |
| `SS_AGENT_RUNTIME_DIR` | 否 | 指定自备的离线运行时目录 |
| `SS_AGENT_DATA_DIR` | 否 | 指定隔离或自定义数据目录 |
| `CLAUDE_BIN` | 否 | 指定 Claude CLI 路径 |
| `AMINER_API_KEY` | 否 | 启用 AMiner 文献检索 |

默认数据目录为 `%APPDATA%\SS-Agent`，数据库名为 `ss-agent.db`。源码仓库不包含 API Key、用户数据库、验证服务、签名私钥或便携运行时。

## 开发与检查

```powershell
npm run check
& .\.venv\Scripts\python.exe -m compileall -q apps\backend
& .\.venv\Scripts\python.exe -m pytest tests
```

也可以单独启动后端：

```powershell
& .\.venv\Scripts\python.exe -m uvicorn main:app --app-dir apps\backend --host 127.0.0.1 --port 8000
```

## 项目结构

```text
apps/desktop        Electron 主进程、预加载脚本和环境检测
apps/backend        FastAPI 后端、路由、工作流引擎和状态存储
apps/frontend/dist  清理后的可运行前端 bundle
resources/skills    竞赛、科研、写作、审稿和开发 Skills
resources/tools     文献、绘图、DOCX、检查和导出工具
resources/templates 工作流输入模板
resources/branding  SS-Agent 图标与品牌资源
tests               静态检查和接口回归测试
```

开发模式优先使用当前系统的 Python、Node、Claude CLI、Pandoc、Draw.io 和 TeX。只有明确设置 `SS_AGENT_RUNTIME_DIR` 且目标文件存在时，应用才使用离线运行时。Mermaid、KaTeX、DOCX 和 MathML 工具从 `npm install` 安装的精确版本解析。

## 常见问题

- PowerShell 提示禁止运行脚本：无需激活 `.venv`，直接使用本文的 `& .\.venv\Scripts\python.exe` 命令。
- 后端无法启动：确认 Python 版本正确，并重新安装 `apps/backend/requirements.txt`。
- 模型列表或生成失败：检查模型服务地址、API Key、模型名称和网络代理。
- Claude 工作流失败：确认 `claude --version` 可执行，或通过 `CLAUDE_BIN` 指定路径。
- Mermaid 或 DOCX 失败：重新执行 `npm install`，确认 Node.js 可用。
- 中文 LaTeX 缺字：安装 MiKTeX/TeX Live 及 Fandol 或 Noto CJK 字体。

## 许可

SS-Agent 首方代码以 [MIT License](LICENSE) 开源。第三方组件、字体和模板继续遵循各自原始许可，详见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
