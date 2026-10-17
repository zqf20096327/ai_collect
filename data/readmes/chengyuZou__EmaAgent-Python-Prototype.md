# EmaAgent 

![Version](https://img.shields.io/badge/version-v0.4-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)


始于 EmaAgent，但不止于只有 Ema 的 Agent。

目前即将进行一次彻底重构，主开发语言将更换为TypeScript，建议Contributors们去提Issue

换上其他角色的 `人设 Prompt` `Live2D` `参考音频`，并调整少量配置与素材，就可以扩展成任何角色的 Agent。

当魔裁全角色智能体补齐后，就能开 `线上魔女审判`。

<img src="./images/others/multi-agent.jpg" alt="multi-agent" width="300" />

---

EmaAgent 是一个多模式智能助手系统，也是我的第一个智能体项目。当前版本核心包含：

- `chat` 普通对话模式
- `agent` 工具调用模式(ReAct)
- `narrative` 叙事检索模式（Router + LightRAG），支持不含 BE 的全剧情检索
- WebSocket 流式输出 + 分段 TTS + 合并回放
- 会话持久化 + 压缩 + 记忆 ChunkRAG
- 附件检索与会话记忆检索统一预处理（支持判定日志与事件回传）
- Live2D 状态联动

![mode](./images/chat/image2.png)

---

## AI使用情况
### 后端
`api`文件夹的全部文件

其余文件夹均进行内容扩写, 约 `60%`

### 前端
全部 前端是梅露露教的 

<img src="./images/others/ema.jpg" alt="ema" width="400" />
<img src="./images/others/mll.jpg" alt="mll" width="300" />

---

## 更新计划 
- [x] 详细的使用教程
- [x] 一键部署
- [ ] 日文语音输出
- [ ] 拓展 `Tool` 功能 实现更强大的 Agent 模式
- [ ] UI美化 自选主题
- [ ] Live2D 优化(Live2D没做好)
- [ ] 架构优化
- [ ] 增加更多`LLM` `EBD` `TTS` 模型接口
  
总之有很多要更新 看你们想更新哪一块

能做EmaAgent 肯定能做其他角色的智能体

魔裁所有角色智能体 `subAgent` 都做完后 可以集成到一个大的智能体中 `MainAgent`

可以开线上魔女审判`agent to agent` 让她们自主聊天

就是 `Token` 消耗要上天了

---

## 更新日志

<details>

## v0.4.1 - 2026-04-05 

- 修复前端步骤状态闭环问题（`step_update` 完整支持 `running -> success/failed`）。
- 修复“仅检索历史附件时”追踪面板不显示附件检索步骤的问题。
- Narrative 模式新增检索链路裁剪：跳过无关附件检索，减少额外开销。
- Agent 编排层新增运行时结构化模块：`runtime_types.py`、`input_pipeline.py`、`execution_tracker.py`。
- 深度思考过程面板与多周目剧情展示完成一轮 UI 升级。

### UI 更新截图

![UI 更新 1](./images/chat/uiupdate1.png)
![UI 更新 2](./images/chat/uiupdate2.png)
![UI 更新 3](./images/chat/uiupdate3.png)

---

### v0.4 - 2026-03-23
- 会话记忆升级为 Chunk + RAG 检索链路（向量优先，关键词回退，最多一跳扩展）
- 记忆模块文档与代码注释规范化（统一 Args/Returns/Raises/Examples）
- API 目录补全文档（接口、IO 类型、示例、Mermaid 数据流）
- MCP、Agent、Memory、Live2D、Audio 等目录文档持续完善

### v0.3 - 2026-03-06
- 前端新增 MCP 配置与管理页面能力

### v0.3 - 2026-03-02
- 增加 MCP 模块 `ema_mcp`，已集成：
  - 高德地图导航（需配置 Key）
  - Howtocook（无需 Key）
- 支持通过 `config/mcp.json` 快速导入 MCP 配置

### v0.2 - 2026-02-22
- 修复 `start.ps1` 中 Node 环境 PATH 仅在临时会话生效的问题
- 感谢 B 站用户 [Jason1044](https://space.bilibili.com/668402457?spm_id_from=333.40164.0.0) 提供反馈

问题示例：
```shell
Command not found: npm. Install Node.js (managed by nvm-windows in .\setup.ps1).
所在位置 E:\EmaAgent-main\start.ps1:27 字符: 9
+         throw "Command not found: $Name. $Hint"
+         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         + CategoryInfo          : OperationStopped: (Command not fou...n .\setup.ps1).:String) [], RuntimeException
          + FullyQualifiedErrorId : Command not found: npm. Install Node.js (managed by nvm-windows in .\setup.ps1).
```

### v0.2 - 2026-02-21
- TTS 模块改为 Factory 模式（感谢 [CodeCCsky](https://github.com/CodeCCsky)）
- 修复 narrative 周目剧情查询异常问题

### v0.2 - 2026-02-16
- 使用 `uv` 进行快速部署
- 新增 `react.py` 中同类错误连续出现检测

### v0.2 - 2026-02-15
- 项目开源

### v0.1 - 2026-01-14
- 实现 `narrative` 功能
- 仅支持终端运行

### 2025-12-09
- 准备开发

### 2025-11
- 刚学 Agent
  
</details>

---

## 架构总览

当前版本采用“前端协议层 - API 服务层 - Agent 编排层 - 智能能力层 - 数据持久层”的分层结构，核心目标是：

1. 路由层尽量薄，业务逻辑集中在 service 与 agent。
2. 会话、附件、记忆走统一持久化与检索通道，支持流式输出与可中断控制。
3. 配置改动可热重载（LLM/TTS/MCP/路径等）。

```mermaid
flowchart TB
    %% ===== Client =====
    subgraph C["Client Layer"]
        FE["Frontend (React + Vite)\nfrontend/src/*"]
        L2D["Live2D Viewer\nfrontend/public/live2d/*"]
    end

    %% ===== API =====
    subgraph B["Backend API Layer (FastAPI)"]
      API["api/main.py\nApp Entry + Lifecycle + Static Mount"]
      RT["api/routes/*\nchat sessions settings news music game live2d"]
      SV["api/services/*\nChat Session Settings News Music Game Live2D"]
    end

    %% ===== Core =====
    subgraph A["Agent Orchestration Layer"]
      EMA["agent/EmaAgent.py\n统一调度 chat agent narrative"]
        RE["agent/react.py\nReAct Tool Loop"]
      MCP["ema_mcp/*\nMCP Client Bridge Manager"]
      TOOLS["tools/*\nBuiltin and Extensible Tools"]
      ATT["attachments/*\nIngest Chunk Retrieve"]
    end

    %% ===== Intelligence =====
    subgraph I["Intelligence Layer"]
      LLM["llm/client.py + llm/clients/*\nOpenAI DeepSeek Qwen"]
        NAR["narrative/core.py\nRouter + RAGManager + LightRAG"]
      MEM["memory/*\nSession Manager + Compressor + ChunkRAG"]
    end

    %% ===== Data =====
    subgraph D["Data & Assets Layer"]
        CFG["config/*\nYAML ENV Paths"]
        DATA["data/*\nsessions uploads audio music puzzle theme font"]
        NDATA["narrative/memory/*\nLightRAG Persistent Data"]
        PAR["Parser/*\n剧情清洗 重排 入库前处理"]
    end

    FE --> API
    L2D --> FE
    API --> RT
    RT --> SV
    RT --> EMA

    EMA --> RE
      EMA --> MCP
      EMA --> ATT
    RE --> TOOLS
    EMA --> LLM
    EMA --> NAR
    EMA --> MEM

    SV --> DATA
      ATT --> DATA
    NAR --> NDATA
    MEM --> DATA
    EMA --> CFG
      SV --> CFG
    PAR --> NAR

    classDef client fill:#E3F2FD,stroke:#1E88E5,color:#0D47A1,stroke-width:1.5px;
    classDef api fill:#E8F5E9,stroke:#2E7D32,color:#1B5E20,stroke-width:1.5px;
    classDef agent fill:#FFF8E1,stroke:#F9A825,color:#E65100,stroke-width:1.5px;
    classDef intel fill:#F3E5F5,stroke:#8E24AA,color:#4A148C,stroke-width:1.5px;
    classDef data fill:#FBE9E7,stroke:#D84315,color:#BF360C,stroke-width:1.5px;

    class FE,L2D client;
    class API,RT,SV api;
    class EMA,RE,TOOLS agent;
    class LLM,NAR,MEM intel;
    class CFG,DATA,NDATA,PAR data;

```

  ### 架构描述（v0.4）

  1. 启动阶段
  - `api/main.py` 在 startup 预热 Agent 运行时组件，减少首包延迟。
  - shutdown 统一回收 MCP/Narrative/Live2D 等资源。

  2. 聊天主链路
  - HTTP：`routes/chat.py -> ChatService.chat -> EmaAgent.run`。
  - WebSocket：`routes/chat.py -> ChatService.websocket_chat -> EmaAgent.run_stream`。
  - 流式模式支持 `token/audio/tool_call/runtime_preprocess/done/error` 事件与 `stop` 中断。

  3. 记忆与附件链路
  - 会话数据由 `SessionManager` 统一持久化。
  - 附件在发送时回填字节并进入附件检索链路。
  - 记忆检索使用 ChunkRAG，负责相关历史片段召回。
  - `EmaAgent` 在 `run/run_stream` 先做压缩与统一预处理，再分发到 `chat/agent/narrative/finish`。

  4. 配置与热重载
  - `SettingsService` 统一管理 `config.yaml`、`ui.yaml`、`mcp.yaml`。
  - 更新设置后按需触发 Agent/TTS/MCP 热重载。

  5. 服务分层原则
  - `routes` 负责参数与协议。
  - `services` 负责业务编排。
  - `agent/memory/llm/tools` 负责核心推理与能力执行。

---

## 文档导航

| 文档 | 说明 |
|---|---|
| [`agent/README.md`](./agent/README.md) | Agent 编排层与 ReAct 执行流 |
| [`attachments/README.md`](./attachments/README.md) | 附件入库、分块、索引与检索链路 |
| [`api/README.md`](./api/README.md) | API 分层与入口说明 |
| [`api/routes/README.md`](./api/routes/README.md) | 全部 REST/WS 路由说明 |
| [`api/services/README.md`](./api/services/README.md) | 业务服务层说明 |
| [`audio/README.md`](./audio/README.md) | TTS 说明 |
| [`config/README.md`](./config/README.md) | 路径 配置与环境变量体系 |
| [`ema_mcp/README.md`](./ema_mcp/README.md) | MCP客户端 |
| [`frontend/README.md`](./frontend/README.md) | 前端交互层与页面说明 |
| [`llm/README.md`](./llm/README.md) | LLM 配置与统一客户端 |
| [`memory/README.md`](./memory/README.md) | 会话模型 持久化与压缩 |
| [`narrative/README.md`](./narrative/README.md) | 叙事路由与 LightRAG 管理 |
| [`Parser/README.md`](./Parser/README.md) | 剧情脚本清洗 重排与入库前处理 |
| [`tools/README.md`](./tools/README.md) | 工具系统与可扩展能力 |

---

## 配置API Key && MCP
### API Key
基础LLM模型可选`DeepSeek` `Qwen` `OpenAI` 三类接入 三选一即可
- `DeepSeek` [API](https://platform.deepseek.com/api_keys)
- `Qwen` [API](https://bailian.console.aliyun.com/cn-beijing?tab=model&utm_content=se_1023046479#/api-key)
- `OpenAI` [API](https://platform.openai.com/settings/organization/api-keys)

Embedding向量编码模型与TTS文本转语音模型目前使用`siliconflow`

后续更新会增加更多接入模型
- `siliconflow`[API](https://cloud.siliconflow.cn/me/account/ak)

获取 Key 后 直接在 `config/config.yaml` 里修改对应 provider 的 `api_key` 字段即可

示例（节选）：
```yaml
runtime:
  llm_model: deepseek/deepseek-chat
  ebd_model: siliconflow/bge-m3
  tts_model: siliconflow/cosyvoice2-0.5b

llm:
  providers:
    deepseek:
      deepseek-chat:
        api_key: your_deepseek_key_here
    qwen:
      qwen3-max:
        api_key: your_qwen_key_here
    openai:
      gpt-4o:
        api_key: your_openai_key_here

ebd:
  providers:
    siliconflow:
      bge-m3:
        api_key: your_ebd_key_here

tts:
  providers:
    siliconflow:
      cosyvoice2-0.5b:
        api_key: your_siliconflow_key_here
```

---

### MCP
可在 [MCP.so](https://mcp.so/) 复制你喜欢的 MCP Server Config，然后写入 `config/mcp.yaml`，示例如下：
```yaml
mcp_servers:
  amap:
    enabled: true
    command: "npx"
    args:
      - "-y"
      - "@amap/amap-maps-mcp-server"
    env:
      AMAP_MAPS_API_KEY: "your_key"
    description: "高德地图 MCP 服务：地理编码、路线规划、天气、POI 搜索等"
    transport: "stdio"
    url: ""

  howtocook-mcp:
    enabled: true
    command: "npx"
    args:
      - "-y"
      - "howtocook-mcp"
    env: {}
    transport: "stdio"
    url: ""
```

---

目前加载的MCP如下 若使用需要事先配置高德的Key
| MCP Key URL | 是否需要 |
| - | - |
| [高德导航](https://console.amap.com/dev/key/app) | ✅️ |
| [Howtocook MCP](https://mcp.so/server/howtocook-mcp/worryzyy) | ❌️ |

---

## 一键启动
默认使用 [uv 启动](#uv-启动)

目前只测试了 Windows 环境 Linux 环境还没测试

### Windows 系统

进入根目录下

点击 `install.bat` 执行安装命令 会自动执行[uv 启动](#uv-启动)的 `setup.ps1` 命令

安装完毕后 再点击 `start.bat` 一键启动 会自动执行[uv 启动](#uv-启动)的 `start.ps1` 命令

---

## uv 启动
目前只测试了 Windows 环境 Linux 环境还没测试

### Windows系统
进入到根目录下

先安装环境
```shell
# 一键环境安装（uv + Python + nvm + Node + 前端依赖）
powershell -ExecutionPolicy Bypass -File .\setup.ps1
```

再一键启动
```shell
# 一键启动（后端8000 + 前端5173）
powershell -ExecutionPolicy Bypass -File .\start.ps1
```

---

## 正常启动

### 1. 环境准备

- Python 3.12+
- Node.js 18+
- AnaConda(可选)

### 2. 下载并安装依赖包

你可以二选一：

方式 A：直接使用系统 Python 环境

```bash
python -m pip install -r requirements.txt
```

方式 B：使用 Conda 新建独立环境

需要你下载AnaConda

```bash
conda create -n Ema python=3.12 -y
conda activate Ema
python -m pip install -r requirements.txt
```

后端:

```bash
python -m pip install -r requirements.txt
```

前端:

```bash
cd frontend
npm install
cd ..
```

---

### 3. 启动
进入文件根目录

后端:

```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

前端:

```bash
cd frontend
npm install
npm run dev
```

---

### 4. 访问地址

- 前端: `http://localhost:5173`
- 后端: `http://localhost:8000`

---

## 演示

### Chat
可选择三个模式 
- `agent`智能体模式 目前工具较为单一
- `chat`日常聊天模式 
- `narrative`剧情模式 支持不含BE的三个周目剧情问答

目前支持 `DeepSeek` `Qwen` `OpenAI` 三类模型接入
![llm](./images/chat/image.png)

由衷感谢B站UP主[露姆娅](https://space.bilibili.com/1384755?spm_id_from=333.788.upinfo.head.click)提供的艾玛Live2D

--- 

### News
从`B站` `百度` `Google`三个网站进行内容爬取

方法为事先写入`魔法少女的魔女审判`作为默认关键字再进行爬取

目前爬取Google的代码似乎有小Bug

![news](./images/news/news.png)

---

### Music
音乐播放

上传自己的音乐文件进行播放

支持`收藏` `文件格式转换` `更改歌手 封面`功能

![music](./images/music/music.png)

---

### Game
拼图游戏 玩到一半nnk会来开你盒

上传你自己的图片就可以玩

可选`3x3` `4x4` `10x10` `20x20`等模式

![nnk](./images/game/puzzle.jpg)

![Puzzle Game](./images/game/game.png)

---

### Setting

配置你的`API Key` 修改配色 

更改文件路径(这个不建议)

![api](./images/setting/image.png)

在`EmaAgent`的`data`文件夹下
- `audio`存放`chat`页面中TTS合成的音频
- `font`存放`setting`页面中的字体样式
- `music`存放`music`页面下的音乐
- `puzzle_images`存放`game`页面下的拼图图片
- `sessions`存放`chat`侧栏的会话数据
- `theme`存放`setting`页面中的主题设置

---


## 项目结构

```text
EmaAgent/
├─ README.md # 项目总览、启动说明、架构图、模块说明与演示文档
├─ requirements.txt # 后端 Python 依赖清单
├─ config/config.yaml # LLM EBD TTS 运行时与密钥配置
├─ config/mcp.yaml # MCP 服务配置
├─ config/ui.yaml # 主题与字体配置
├─ main.py # 旧版 CLI 启动入口（v0.2 已迁移到 api/main.py）
│
├─ agent/ # EmaAgent 核心逻辑与 ReAct 循环
│ ├─ react.py # ReAct 思考-行动-观察循环
│ └─ EmaAgent.py # 主代理类，集成工具与 LLM
|
├─ attachments/ # 附件处理逻辑
|
├─ api/ # FastAPI 后端服务
│ ├─ routes/ # API 路由定义
│ │ ├─ schemas/ # 请求/响应数据模型
│ │ └─ services/ # 业务逻辑服务层
│ └─ main.py # API 应用入口
|
├─ audio/ # TTS 音频生成与管理
│ └─ clients/ # TTS 客户端实现
|
├─ config/ # 配置文件与路径管理
|
├─ data/ # 用户数据存储
│ ├─ audio/ # 音频文件
│ ├─ font/ # 字体资源
│ ├─ music/ # 音乐文件
│ ├─ puzzle_images/ # 谜题图片
│ ├─ sessions/ # 会话数据
│ ├─ theme/ # 主题配置
│ └─ uploads/ # 用户上传文件
|
├─ ema_mcp/ # MCP 协议集成模块
|
├─ frontend/ # React + Vite 前端应用
│ ├─ public/ # 静态资源
│ └─ src/ # 源代码
|
├─ images/ # 图片资源
│ ├─ chat/ # 聊天相关图片
│ ├─ game/ # 游戏相关图片
│ ├─ music/ # 音乐相关图片
│ ├─ news/ # 新闻相关图片
│ ├─ others/ # 其他图片
│ └─ setting/ # 设置相关图片
|
├─ llm/ # LLM 模型配置与客户端
│ └─ clients/ # 不同 LLM 提供商客户端
|
├─ logs/ # 运行日志目录
├─ memory/ # 会话记忆管理与压缩
|
├─ narrative/ # 叙事检索与多周目 RAG
│ └─ memory/ # LightRAG 持久化数据
|
├─ Parser/ # Naninovel 脚本解析工具
|
├─ prompts/ # 系统提示词模板
|
├─ tools/ # 工具集合与基础类
│ ├─ builtin/ # 内置工具实现
│ ├─ file_analysis/ # 文件分析工具
│ └─ search/ # 搜索工具
└─ utils/ # 通用工具函数
```

---

## 补充说明
### 1. 剧情数据清洗与重排（Parser）

原始脚本数据来自 Naninovel，单条记录通常是这种格式：

```text
# 0101Adv01_Narrative002
; <ruby="さくらば">桜羽</ruby>エマは周囲の悪意に<br>耳を塞ぎたかった。
樱羽艾玛只想捂紧耳朵，<br>
抵挡身边涌现的恶意。
```

这类数据直接用于 RAG 会遇到三个核心问题：

1. 周目顺序问题：理论上是 `1周目(5章) -> 2周目(4章) -> 3周目(2章)`，但原始数据里第三周目的两章常被接在第二周目后面。  
2. 场景切分问题：剧情由 `Adv` 与 `Trial` 组成，正确顺序里 `Trial` 通常插在章节内 `Adv` 的倒数第二或第三段附近，但原始数据里二者经常被完全分离。  
3. 目录分散问题：第三周目有部分数据在另一个文件夹，需要额外映射与合并。  

为了解决这些问题，项目使用 `Parser/` 的分步流程：

1. `build_dataset.py`：全量提取脚本，做角色识别与文本清洗，标注 `timeline/chapter/type(Adv|Trial)`。  
2. `merger.py`：用滑动窗口合并为可检索 chunk，保留章节边界与剧情位置信号。  
3. `new.py`：把被放错位置的第三周目章节重映射回 `Act03`，统一周目结构。  

最终产物（如 `norm_merged_cleaned.json`）才会送入 narrative 记忆库使用。

### 2. Narrative RAG 设计与演进

剧情检索模块是本项目和通用聊天助手最大的差异点之一。

- 当前实现：三个周目分别由三个 LightRAG 实例维护（`1st_Loop`、`2nd_Loop`、`3rd_Loop`）。  
- 路由策略：`narrative/router.py` 先把用户问题拆分并路由到对应周目，再由 `narrative/rag_manager.py` 并发查询并聚合结果。  
- 架构入口：`narrative/core.py`（`NarrativeMemory`）统一封装 `Router + RAGManager`。  

演进说明：

- 在 `2026年1月` 的方案中，曾尝试对清洗后数据增加 `progress_score`，并在用户问“开始/结束/中途”等关键词时做进度过滤。  
- 该方案在实际对话中效果不稳定（召回与语义匹配不够理想）。  
- 后续切换到 LightRAG 后，实际效果更好，因此当前版本以 LightRAG 路由检索为主。  

### 3. Session 管理服务化改造

为贴近网页端大模型产品的会话体验（新建、列表、重命名、删除、历史回放），会话管理从 Agent 内部能力拆分为独立服务：

- 服务层：`api/services/session_service.py`  
- 路由层：`api/routes/sessions.py`  
- 底层存储：`memory/manager.py` + `memory/schema.py`  

现有会话接口包括：

- `GET /api/sessions`：会话列表  
- `POST /api/sessions/new`：新建会话  
- `GET /api/sessions/{session_id}/messages`：读取消息历史  
- `POST /api/sessions/{session_id}/rename`：重命名会话  
- `DELETE /api/sessions/{session_id}`：删除会话  

### 4. `memory/schema.py` 数据类说明

`memory/schema.py` 是会话与 Agent 运行态的核心数据契约，主要类如下：

- `Message`：通用消息基类，统一 `role/content/timestamp` 以及工具调用字段序列化逻辑。  
- `SystemMessage` / `UserMessage` / `AssistantMessage` / `ToolMessage`：四类标准消息子类，对应 LLM 聊天与工具调用链。  
- `CompressionRecord`：单次压缩记录（压缩时间、范围、摘要、压缩前后消息数）。  
- `CompressionHistory`：压缩历史聚合（当前摘要、最近压缩时间、累计压缩次数）。  
- `Session`：完整会话对象（消息列表、压缩游标、上下文裁剪参数、统计字段），并提供：
  - `get_context_for_llm()`：构造模型输入上下文（含摘要注入、tool 消息过滤）
  - `compress_if_needed()`：按阈值触发上下文压缩
  - `to_dict()/from_dict()`：会话元信息持久化
- `AgentStatus`：运行状态枚举（`idle/thinking/acting/finished/error`）。  
- `AgentRuntimeState`：单次 ReAct 运行时状态容器（步骤计数、工具结果、最终答案、时长与错误信息）。  

### 5. API 与 Service 分层

项目后端采用典型的 Route-Service 分层：
(注):这部分代码AI写的,我尽量把注释写全

- `api/routes/*`：参数校验、HTTP 协议层、响应模型。  
- `api/services/*`：业务逻辑与文件系统操作。  

主要模块分工如下：

| 模块 | 作用 |
|---|---|
| `chat` | `chat/agent/narrative` 三模式统一入口，含 WS 流式返回与 TTS 片段合成 |
| `sessions` | 会话生命周期管理（列表/新建/重命名/删除/历史） |
| `music` | 音乐上传、播放列表、收藏、转换、封面、重命名、删除 |
| `game` | 拼图图片上传、列表、单删、批量删除 |
| `news` | 多来源资讯抓取与聚合 |
| `settings` | 模型配置、主题字体、路径与系统状态 |
| `audio/live2d` | 音频静态访问与 Live2D 状态联动 |

### 6. Tools 与 Agent 关系（简述）

`tools/` 的整体组织方式参考了 OpenManus 的工具集合思路：统一抽象、统一调度、统一错误包装。  
在本项目里：

- `agent/react.py` 负责 ReAct 的 `think -> act` 循环与工具调用。  
- `agent/EmaAgent.py` 在 ReAct 之外再做一层业务封装：统一接入日常聊天、剧情问答、基础工具调用、会话保存与流式回传。  

这也是为什么前端只需选择 `chat / agent / narrative` 模式，而不需要关心底层工具与检索细节。

---

## 共犯名单 (Contributors Stargazers Forks)
感谢所有卷入这场 `审判` 的人员 排名不分先后


### Contributor
<a href="https://github.com/chengyuZou/EmaAgent/graphs/contributors">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://contrib.rocks/image?repo=chengyuZou/EmaAgent&antml=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://contrib.rocks/image?repo=chengyuZou/EmaAgent" />
    <img alt="Contributors" src="https://contrib.rocks/image?repo=chengyuZou/EmaAgent" />
  </picture>
</a>

---

[⭐ Stargazers](https://github.com/chengyuZou/EmaAgent/stargazers) 
[🔀 Forks](https://github.com/chengyuZou/EmaAgent/network/members)

---

## 致谢名单

注:排名不分先后顺序
| name | describe |
| - | - |
| [柏斯阔落](https://space.bilibili.com/266938091?spm_id_from=333.1387.follow.user_card.click)| [NagaAgent](https://github.com/RTGS2017/NagaAgent) |
| [无头鬼艾伦](https://space.bilibili.com/352089037?spm_id_from=333.1387.follow.user_card.click) | [MikuChat](https://www.bilibili.com/video/BV1DkzABZEoe/?spm_id_from=333.1387.homepage.video_card.click&vd_source=3151b98d67ade6395736508def783435) |
| [露姆娅](https://space.bilibili.com/1384755?spm_id_from=333.788.upinfo.head.click) | [艾玛Live2D](https://www.bilibili.com/video/BV1rF6QB1EqW/?spm_id_from=333.337.search-card.all.click) |
| [貳階堂希罗](https://space.bilibili.com/434748403?spm_id_from=333.788.upinfo.head.click) | [魔法少女的魔女审判 CG/PV/美术/音声资源提取解包](https://www.bilibili.com/video/BV1Zu4czJENM/?spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=3151b98d67ade6395736508def783435) |
| [OpenManus](https://github.com/FoundationAgents/OpenManus) | 参考Tool架构 |
| [LightRAG](https://github.com/HKUDS/LightRAG) | Simple and Fast Retrieval-Augmented Generation |
| [Acacia](https://acacia-create.com/) | - |
| [Serism_official](https://space.bilibili.com/1050531840?spm_id_from=333.788.upinfo.detail.click) | 孩子们 猜猜艾玛的[参考音频](https://www.bilibili.com/video/BV1NCqqBuE9M/?buvid=XXC3D36CA77C347443C8E1BE9ABDA72C8EE56&from_spmid=search.search-result.0.0&is_story_h5=false&mid=SCkMrA1jFnwwFjYh6jhhHg%3D%3D&plat_id=116&share_from=ugc&share_medium=android&share_plat=android&share_session_id=73cd231c-acfa-4a3c-a6d0-2e3e162b4b12&share_source=WEIXIN&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1771042359&unique_k=LuTRc12&up_id=1050531840&vd_source=3151b98d67ade6395736508def783435)哪来的? |

## 免责声明
仅供个人、爱好者之间的学习、研究与技术交流用

不适用于任何商业或盈利性活动

本项目中展示的部分图像、声音、模型、脚本等素材

其著作权及相关权利均归原始权利人所有

本次开源目的在于探讨智能体开发、游戏开发、美术、音频设计、技术实现原理

以促进教育与创作交流 不构成对任何原作、商标或品牌的商业使用、再分发或暗示性授权

若项目中包含的素材被认定涉嫌侵犯他人版权或违反相关使用条款请及时联系

我会在接收到正式通知后立即移除相关内容 避免后续再次使用

---



---

## 2026-04-05 技术日报（前后端全链路优化与 UI 升级）

### 一、核心问题修复（Bug Fixes）

1. 修复前端“无限转圈（Infinite Spinner）”状态流转异常
   - 在 `frontend/src/components/ChatInterface.tsx` 补齐 `step_update` 事件状态闭环。
   - 解决步骤结束后仍停留在执行中的问题。

2. 修复“已有附件检索不回显步骤”
   - 在 `agent/input_pipeline.py` 增加历史附件存在判断。
   - 即使当前轮未新上传附件，也能正确渲染“附件检索”追踪步骤。

### 二、UI / UX 升级

1. 深度思考模块视觉优化
   - 外层容器与内部 `thought/think` 展示块增加分层背景与过渡效果。

2. Narrative 多周目可视化增强
   - 对 `narrative_route` 结果增加分支渲染。
   - 命中多个 Loop 时自动渲染多个子折叠块，便于观察抽取进度。

3. 记忆压缩字段展示修正
   - 前端显示字段对齐 `before_compressions`。
   - 保持压缩前后统计信息的一致性。

### 三、架构与性能优化

1. Narrative 模式检索裁剪
   - 当 `mode == "narrative"` 时，跳过无关附件向量检索。
   - 降低检索开销与上下文长度，缩短响应路径。

2. 运行时输入解耦
   - 将原始用户 query 与检索证据上下文分离。
   - 由 `agent/runtime_types.py` 与 `agent/input_pipeline.py` 统一管理运行时注入结构。

### 四、技术答疑（Q&A）

1. RAG 证据如何进入最终请求
   - 证据在 `input_pipeline.py` 汇总为运行时系统提示。
   - 在请求构建阶段与主 Persona 提示词拼接后送入模型。
   - 用户消息正文保留原始 query，避免被检索模板污染。

### 五、稳定性结论

- 已完成从“后端步骤状态流”到“前端可视化追踪”的闭环修复。
- Narrative 指定工作流已具备可观察、可裁剪、可扩展的检索链路。
- 现阶段主链路可用性与可视化反馈均达到稳定状态。
