# qwensese

[![CI](https://github.com/maokexuehu/qwensese/actions/workflows/ci.yml/badge.svg)](https://github.com/maokexuehu/qwensese/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Zero dependencies](https://img.shields.io/badge/runtime%20deps-0-success.svg)](requirements.txt)

**基于 Python 标准库 HTTP 服务与本地 Ollama 模型、利用 Markdown 角色卡与每轮现场拼装的系统提示词，
实现的零第三方依赖本机角色扮演对话台。**

A local-first, zero-dependency character roleplay console for Ollama. A pure Python
standard-library HTTP server serves a single-page web UI, assembles the system prompt
fresh on every request, and streams tokens straight from your local model — no cloud,
no account, no API key, no third-party Python packages. A built-in hardware advisor
detects your GPU/VRAM and recommends which Qwen GGUF quantization actually fits.

中文说明见下方；文档索引在文末。

![界面预览](docs/assets/preview.png)

## 中文说明

### 这个项目解决什么问题

- **对话不出本机**：模型权重跑在你自己的机器上，前端、服务端、Ollama 全部在本机回环地址，不需要联网也不需要账号。
- **角色卡就是 Markdown**：`personas/*.md` 用 `## 字段名` 分段，页面里改完保存立刻写回文件；SYSTEM 每轮现场拼装，所以换角色、改尺度、改文风都是下一条消息就生效，不用重建模型。
- **自带系统提示层与文风层**：`prompts/system-core.md` 负责维持角色一致性、抑制出戏与思考链输出，`prompts/style-guide.md` 负责文风与节奏（可关）。
- **零第三方依赖**：只用 Python 标准库，`pip install` 都不需要；Windows 有双击即用的 PowerShell 脚本，Linux/macOS 用 `scripts/start.sh` 或直接 `python web/app.py`。
- **先量显卡再选模型**：`scripts/model_advisor.py` 检测显卡/显存/内存，按档位推荐 Qwen GGUF 量化，网页里点「硬件选型」也能看下载/导入命令；不再"先下 13 GB 再发现跑不动"。
- **手机/局域网可用**：`--lan` 后同一 Wi-Fi 内的手机浏览器可访问（强制要求先设置 `access_key`）；还给 Chatbox 等客户端准备了 `/v1` OpenAI 兼容层。
- **日常功能齐全**：对话存档、上下文压缩摘要、重新生成/撤回、叙事者模式、"帮我想"下一步建议、从旧对话或一段描述生成角色卡。

### 特性

- 纯标准库后端：Python `ThreadingHTTPServer`，无框架、无构建步骤、无第三方包。
- 原生单页前端：`web/index.html` + `web/app.js` + `web/style.css`，不依赖前端框架。
- 每轮现拼 SYSTEM：角色卡字段、尺度档位、用户（"我"）设定、前情摘要、本轮额外指令、文风规则在请求时组合。
- 流式输出：以 NDJSON 逐行转发 Ollama 的流；内置思考链过滤（开头 `think` 块、零宽字符、残缺标记）与开头垃圾清理。
- 角色卡编辑：页面内编辑 13 个标准字段，支持额外自定义字段，保存即合并写回 `personas/*.md`；可新建、删除。
- "我的角色卡"：`config/user_personas/` 下可放多张"我"的设定，页面随时切换。
- 对话存档：`saves/*.json` 自动/手动保存，列表按更新时间排序，点开即接着聊。
- 上下文管理：token 估算、超出预算自动丢弃最早对话；一键把前段对话压成摘要，可撤销。
- 帮我想：结合最近对话与角色设定，生成 3～5 条可立刻接上的台词/动作建议。
- 角色卡生成：支持"从对话提取"与"从描述生成"两条路径，先预览、确认后才落盘。
- 叙事者模式：不扮演单一角色，以第三人称推进剧情，可多人物同场。
- 模型与参数：模型下拉、上下文长度、回复长度预设、温度 / top_p / 复读惩罚可调。
- **硬件选型**：`GET /api/hardware` + 网页「🖥️ 硬件选型」按钮，按显存给推荐与可复制的下载/导入命令。
- **模型工具链（跨平台）**：检测选型、断点续传下载（自动 SHA256 校验）、生成 Modelfile 并 `ollama create`，全部是纯 Python 脚本。
- 访问口令：`access_key` 非空时校验全部页面与 API；默认只监听 `127.0.0.1`。
- OpenAI 兼容层：`/v1/models`、`/v1/chat/completions`；用虚拟模型名 `qwensese/<角色>/<尺度>` 切换角色与尺度。
- 一键脚本：启动、下载 GGUF、导入 Ollama 模型（Windows PowerShell；Linux/macOS 有 `start.sh` 与纯 Python 工具链）。

### 环境要求（说清楚硬件账单）

| 项目 | 要求 |
| --- | --- |
| Python | 3.10+（只用标准库；开发环境为 3.12） |
| Ollama | 建议最新版（需要支持 `/api/chat` 的 `think` 参数） |
| 操作系统 | Windows 10/11（一键脚本需要 PowerShell 5.1+）；Linux/macOS 可用 `scripts/start.sh` + 纯 Python 工具链 |
| 显卡 | **没有硬性门槛**，但默认 27B 模型需要 **16 GB 级显存**才能全速；8 GB 卡建议改 8B、12 GB 建议 14B，用 `model_advisor.py` 选型 |
| 磁盘 | 模型权重 2.5～20 GB（默认 27B `UD-IQ4_XS` 约 13.4 GB）；请给 `models/` 预留 20 GB+（下载临时文件 + Ollama blobs 各一份） |
| 内存 | 建议 ≥16 GB；显存不足时 Ollama 会把部分层卸载到内存，速度骤降 |
| 网络 | 仅首次下载模型需要联网；之后完全离线 |
| 浏览器 | 任意现代浏览器 |

> 首次开始 = 一次性下载十几 GB 权重。这是本地大模型的固有成本，不是本项目的额外开销；
> 想先低成本试流程可以用 4B/8B（2.5～5 GB）。

### 快速开始（4 步）

1. **准备环境**：装好 Python 3.10+ 与 Ollama，确认 `python --version`、`ollama --version` 都能执行。

2. **按显卡选模型**：

   ```bash
   python scripts/model_advisor.py            # 检测显存并给出推荐（Windows/Linux/macOS 通用）
   ```

   按输出里的「下载」命令下载。默认组合（16 GB 级显存）是 27B `UD-IQ4_XS`：

   ```bash
   python scripts/model_advisor.py --download huihui-27b --quant UD-IQ4_XS
   ```

   老用户也可以继续用 PowerShell 脚本（curl 版，无 SHA256 校验）：

   ```powershell
   powershell -ExecutionPolicy Bypass -File scripts/download-model.ps1
   ```

3. **导入 Ollama**（需要 Ollama 服务在运行）：

   ```bash
   python scripts/import_model.py --gguf models/gguf/Huihui-Qwen3.8-27B-abliterated-UD-IQ4_XS.gguf --name qwensese-27b --num-ctx 12288
   ```

   Windows 也可以：`powershell -ExecutionPolicy Bypass -File scripts/import-model.ps1 -Name qwensese-27b`。
   如果提示 Ollama 不可达，先跑 `scripts/start.ps1` / `OLLAMA_MODELS="$PWD/models" ollama serve`。

4. **启动页面**：

   ```powershell
   # Windows
   powershell -ExecutionPolicy Bypass -File scripts/start.ps1
   ```

   ```bash
   # Linux / macOS
   ./scripts/start.sh
   ```

   或双击 `scripts/start.bat`。启动后浏览器打开 <http://127.0.0.1:8717/>。首次启动会自动把
   `web/config.example.json` 复制成 `web/config.json`。

已经导入过模型、只想手工启动时：`python web/app.py`。

更细的步骤见 [docs/quickstart.md](docs/quickstart.md)，选型细节见
[docs/model-selection.md](docs/model-selection.md)，全部配置项见
[docs/configuration.md](docs/configuration.md)。

### 获取模型

**先选型再下载**：不同显存能跑的量化差别很大。

| 显存 | 建议 | 文件大小 |
| --- | --- | --- |
| 无独显 / 核显 | Qwen3 4B `Q4_K_M` | 约 2.5 GB |
| 8 GB | Qwen3 8B / 8B abliterated `Q4_K_M` | 约 5 GB |
| 12 GB | Qwen3 14B / 14B abliterated `Q4_K_M` | 约 9 GB |
| **16 GB** | **27B abliterated `UD-IQ4_XS`（本仓库默认，作者实测）** | 约 13.4 GB |
| 24 GB | 27B `UD-Q4_K_XL` 或 32B `Q4_K_M` | 16.5～20 GB |
| 32 GB+ | 32B `Q5_K_M` / 27B `UD-Q5_K_XL` | 19.5～24 GB |

默认模型仓库与量化：

| 项目 | 值 |
| --- | --- |
| 模型仓库 | `huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF` |
| 默认量化 | `UD-IQ4_XS`（约 13.4 GB） |
| 导入后的 Ollama 模型名 | `qwensese-27b` |
| 其他可选量化 | `UD-Q3_K_XL`（约 12.4 GB）、`UD-DW-Q4_K_M`（约 15.4 GB）、`UD-Q4_K_XL`、`UD-Q5_K_XL` |

完整候选表、14B/8B 的安装路径、SHA256 校验说明、Linux/macOS 命令见
[docs/model-selection.md](docs/model-selection.md)。

模型权重由发布方按自己的许可证分发，不在本仓库的 MIT 许可范围内；使用前请阅读上游仓库的许可与使用条款。

### 目录结构

```text
qwensese/
├── README.md                   # 本文件
├── CHANGELOG.md                # 版本变更记录
├── CONTRIBUTING.md             # 贡献指南
├── CODE_OF_CONDUCT.md          # 行为准则
├── SECURITY.md                 # 安全策略与威胁模型
├── LICENSE                     # MIT
├── NOTICE.md                   # 模型权重与第三方内容说明
├── requirements.txt            # 零第三方依赖说明
├── .gitignore                  # 忽略模型权重/存档/本机配置
├── .gitattributes              # 换行策略（文本 LF，脚本按系统）
├── .github/                    # CI / Release 工作流、issue/PR 模板
├── web/                        # HTTP 服务与前端
│   ├── app.py                  # 入口：标准库 HTTP 服务 + API + SYSTEM 拼装
│   ├── importer.py             # 从对话/描述生成角色卡的分析器（被 app.py 调用）
│   ├── index.html              # 单页界面
│   ├── app.js                  # 前端逻辑（无构建）
│   ├── extra.js                # 18+ 确认与「硬件选型」面板（独立小文件）
│   ├── style.css               # 样式
│   └── config.example.json     # 配置模板（复制为 config.json 使用）
├── personas/                   # 角色卡（AI 扮演的人）
│   ├── persona.md              # 示例角色：林晚，书店店主
│   ├── example-mentor.md       # 示例角色：周屿，研究生
│   ├── template.md             # 空白角色卡模板
│   └── README.md               # 字段说明
├── prompts/
│   ├── system-core.md          # 系统提示词（每轮注入 SYSTEM）
│   └── style-guide.md          # 文风规则（可关闭）
├── config/
│   ├── mode.txt                # 思考模式偏好记录
│   ├── template-thinking.txt   # Ollama TEMPLATE 片段（thinking 版）
│   ├── template-nothink.txt    # Ollama TEMPLATE 片段（nothink 版）
│   ├── user_personas/default.md # "我"的角色卡（可放多张）
│   └── current_user_persona.txt # 当前选中的"我"（运行时写入，不入库）
├── ollama/
│   └── Modelfile.echo          # 手工建模型用的 Modelfile 示例
├── docs/
│   ├── quickstart.md           # 从零到能对话
│   ├── model-selection.md      # 按显卡选模型（选型/下载/校验/导入）
│   ├── security-model.md       # 安全模型与威胁矩阵
│   ├── configuration.md        # 配置参考
│   ├── API.md                  # HTTP API 参考
│   ├── architecture.md         # 架构说明
│   ├── roadmap.md              # 已知短板与计划
│   └── assets/preview.png      # README 截图
├── scripts/                    # 一键脚本 + 纯 Python 工具链
│   ├── start.ps1 / start.bat / start.sh
│   ├── model_advisor.py        # 硬件检测 + 选型推荐（跨平台）
│   ├── download_model.py       # 断点续传 + SHA256 校验下载器（跨平台）
│   ├── import_model.py         # 生成 Modelfile + ollama create（跨平台）
│   ├── model-advisor.ps1       # Windows 薄包装
│   ├── model_catalog.json      # 候选模型目录（可直接编辑）
│   ├── download-model.ps1 / import-model.ps1
│   └── README.md
├── tests/                      # 自动化测试（纯标准库）
│   ├── run_all.py
│   ├── test_layout.py
│   ├── test_advisor.py
│   ├── test_api.py
│   └── README.md
├── saves/                      # 运行时生成：对话存档 JSON（不入库）
├── models/                     # 运行时生成：模型与 GGUF（不入库）
└── logs/                       # 运行时生成：Ollama/服务日志（不入库）
```

> `saves/`、`models/`、`logs/`、`web/config.json`、`__pycache__/` 都是运行时产物，已被 `.gitignore` 忽略，发布仓库里不会包含。

### API 一览

本服务共 20 个 `/api/*` 路径（22 个方法-路径组合）+ `/v1` 兼容层 2 个端点，全部返回 UTF-8 JSON（流式接口为 NDJSON / SSE）。完整字段、示例与错误码见 [docs/API.md](docs/API.md)。

| 方法 | 路径 | 用途 |
| --- | --- | --- |
| GET | `/api/health`（别名 `/health`） | 存活探针：`ok`、Ollama 是否可达、角色卡数量 |
| GET | `/api/state` | 角色卡列表、当前模型名、Ollama 状态、尺度档位文案、版本、前端开关 |
| GET | `/api/persona?id=<文件名>` | 读取单张角色卡的字段字典 |
| GET | `/api/models` | Ollama 已安装模型列表 + `ollama_ok` |
| GET | `/api/hardware` | 显卡/显存/内存检测 + 推荐模型量化 + 下载/导入命令（缓存 5 分钟） |
| GET | `/api/ctx?persona_id=&level=&mode=` | 当前 SYSTEM 的字符数与估算 token 数 |
| GET | `/api/me?file=` | 当前"我"的角色卡字段 + 全部"我"的列表 |
| GET | `/api/me/list` | "我"的角色卡列表（精简版） |
| GET | `/api/saves[?id=]` | 存档列表；带 `id` 时返回该存档的完整内容 |
| GET | `/v1/models`（别名 `/models`） | OpenAI 兼容：虚拟模型名列表 |
| POST | `/api/persona/save` | 新建/保存角色卡（只提交部分字段时与旧卡合并） |
| POST | `/api/persona/delete` | 删除角色卡 |
| POST | `/api/me` | 新建/保存"我"的角色卡，可同时设为当前 |
| POST | `/api/me/delete` | 删除"我"的角色卡 |
| POST | `/api/chat` | 主对话接口，NDJSON 流式返回 |
| POST | `/api/compress` | 把最近的对话压成前情摘要 |
| POST | `/api/suggest` | 结合最近对话生成"下一步可以说什么"建议 |
| POST | `/api/card/gen` | 从一段描述生成角色卡 / "我"的卡（只返回草稿，不落盘） |
| POST | `/api/import` | 从一段现成对话导入角色卡（NDJSON 进度流） |
| POST | `/api/me/import` | 从一段对话提取"我"的设定 |
| POST | `/api/saves` | 保存/更新一份对话存档 |
| POST | `/api/saves/delete` | 删除对话存档 |
| POST | `/api/ollama/start` | 尝试拉起项目自带的 Ollama（`ollama/ollama.exe`） |
| POST | `/v1/chat/completions`（别名 `/chat/completions`） | OpenAI 兼容：对话，支持 SSE 流 |

另外两个路径不是本服务提供的，而是本服务用来探活/列模型的 **Ollama 上游接口**：

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| GET | `http://127.0.0.1:11434/api/tags` | Ollama 已安装模型列表（上游） |
| GET | `http://127.0.0.1:11434/api/version` | Ollama 版本探活（上游） |

想要等价的探活结果，直接调用本服务的 `/api/health` 或 `/api/models` 即可。

### 安全说明

0.2.0 起，写接口不再"默认裸奔"；完整威胁矩阵见 [docs/security-model.md](docs/security-model.md)。

- **默认只监听本机**：`host` 默认 `127.0.0.1`，页面与 API 只有本机可访问。
- **访问口令 `access_key`**：设置后所有页面与 API 都要求携带口令（`?k=`、cookie `qk`、请求头 `X-Access-Key`，常量时间比较）；留空则不校验（纯本机场景）。
- **Host / Origin / Content-Type 校验**：Host 头必须是本机/配置的地址（防 DNS rebinding）；跨站 `Origin` 的 POST 直接 403（防恶意网页删卡/烧显卡）；写接口必须 `application/json`（防表单 CSRF）。
- **安全响应头**：CSP、`nosniff`、`X-Frame-Options: DENY`、`Referrer-Policy: no-referrer` 等全部响应都带。
- **cookie `SameSite=Strict; HttpOnly`**；写盘读-改-写加锁，避免并发丢更新。
- **`--lan` 强制口令**：监听 `0.0.0.0` 且未设置 `access_key` 时拒绝启动（除非显式 `--insecure-lan`）。开放公网仍应加 HTTPS 反向代理与防火墙/来源 IP 限制。
- **Ollama 自身没有鉴权**：默认只绑 `127.0.0.1:11434`，不要直接暴露到公网。
- **提示词注入/越狱不是漏洞**：本项目的用途是自定义人设并在本地生成虚构内容，模型被诱导产出什么由使用者自行负责；仍然不要用它生成违法或伤害真实人物的内容。
- **没有内容护栏**：默认底座是消融拒答方向的 abliterated 模型，服务端没有输出过滤或年龄验证；前端 18+ 确认只是本地提示。

完整威胁模型与漏洞上报方式见 [SECURITY.md](SECURITY.md)。

### 内容免责声明

- **仅限成年人**：本项目面向成年人，用于虚构角色扮演；首次打开页面会显示 18+ 提示（本地记录确认，可被清掉，服务端无法验证年龄）。
- **BYO 内容（自带内容）**：仓库自带的 `personas/persona.md`（林晚）与 `personas/example-mentor.md`（周屿）是虚构的成年角色示例，只用于演示格式；你添加的任何角色卡、提示词、存档都由你自己负责。
- **不附带模型**：本仓库只包含源码、脚本、示例文本与文档，不包含任何模型权重；模型输出取决于你选择的模型、量化与提示词。
- **年龄底线**：所有角色必须是 **18 岁及以上的虚构角色**；禁止用于未成年人、真实可识别的个人、真实伤害或任何违法内容。
- **无强制过滤**：默认模型是权重层面消融拒答方向的衍生模型，提示词里的底线只是软约束；请自行评估所在司法辖区与平台规则的合规风险。
- 本项目按 MIT 许可**不作任何担保**，使用风险自负。

### 常见问题

- **下载模型太慢 / 中断**：`download_model.py` 支持断点续传，重跑同一条命令即可；也可以分多次下载。
- **显存不够 / 速度很慢**：先跑 `python scripts/model_advisor.py`；16 GB 以下建议换 14B/8B，并把 `num_ctx` 调小。
- **网页上没显示模型**：Ollama 服务没起，或模型导入到了别的 `OLLAMA_MODELS` 目录；用 `scripts/start.ps1` / `scripts/start.sh` 启动 Ollama。
- **`--lan` 启动被拒绝**：这是有意的安全限制；先在 `web/config.json` 设置长随机 `access_key`。
- **想自己加模型**：编辑 `scripts/model_catalog.json` 或直接用 `scripts/download_model.py --repo ... --file ...`。

更多见 [docs/quickstart.md](docs/quickstart.md) 与 [docs/model-selection.md](docs/model-selection.md)。

### 文档索引

| 文档 | 内容 |
| --- | --- |
| [docs/quickstart.md](docs/quickstart.md) | 从零安装到第一次对话的完整步骤 |
| [docs/model-selection.md](docs/model-selection.md) | 按显卡选模型、下载校验、导入、Linux/macOS 命令 |
| [docs/security-model.md](docs/security-model.md) | 安全模型、威胁矩阵、残余风险与加固建议 |
| [docs/configuration.md](docs/configuration.md) | `web/config.json`、`config/` 目录、环境变量与采样参数参考 |
| [docs/API.md](docs/API.md) | 每个 HTTP 接口的方法、参数、响应示例与错误码 |
| [docs/architecture.md](docs/architecture.md) | 三层架构、无状态对话、流式转发、角色卡解析、存档结构、鉴权门禁 |
| [docs/roadmap.md](docs/roadmap.md) | 已知短板、拆分计划与路线图 |
| [CONTRIBUTING.md](CONTRIBUTING.md) | 开发环境、代码风格、PR 流程、如何跑测试 |
| [CHANGELOG.md](CHANGELOG.md) | 版本变更记录 |
| [SECURITY.md](SECURITY.md) | 安全策略、威胁模型、漏洞上报 |
| [scripts/README.md](scripts/README.md) | 一键脚本与工具链用法 |
| [tests/README.md](tests/README.md) | 测试怎么跑 |

### 许可

本项目以 [MIT License](LICENSE) 发布。模型权重、第三方模型与第三方内容由各自的发布方按其许可证提供，不在本仓库的 MIT 许可范围内；`personas/`、`config/` 中你自己添加的内容由你自行负责。详见 [NOTICE.md](NOTICE.md)。
