# Animon

**具有角色、长期记忆与关系状态的 AI 陪伴对话原型。**  
**An AI companion prototype with distinct characters, persistent memory, and evolving relationship states.**

[简体中文](#简体中文) · [English](#english)

**作者 / Authors**  
Z. Y. Wang, Z. L. Qin, H. T. Lu, B. S. Yu, L. W. Jiang, Z. P. Chen

---

## 简体中文

### 项目概述

Animon 是一个基于 Python 的模块化 AI 陪伴对话原型。它将角色设定、长期记忆、情绪状态、表达倾向和关系档案连接起来，使持续对话能够参考以往互动，而不局限于单次问答。

项目提供命令行文字交互和可选的语音输入 / 输出，默认通过 DeepSeek API 生成回复。本项目中的“成长”由本地持久化状态、记忆和提示词上下文实现，不涉及在线更新大模型权重。

当前版本面向学习、原型验证与二次开发，未包含玩偶硬件、Web 服务或模型权重。运行对话需要自行配置模型服务及 API key，可能产生服务费用。

### 功能概览

| 功能 | 实现方式 |
| --- | --- |
| 双角色交互 | 绵绵与砰砰采用不同的人设、语气和回应策略 |
| 长期记忆 | 从对话中抽取关键事实，使用关键词检索为后续回复提供上下文 |
| 六轴状态 | 亲密度、情绪、活力、勇气、共情与好奇心随互动及间隔时间更新 |
| 表达倾向演化 | 周期性抽取、强化、衰减与整合关系中特有的表达倾向 |
| 关系档案 | 在交互里程碑记录关系反思，支持即时查看 |
| 轻量任务 | 建议任务，记录进度，支持完成与放弃 |
| 安全约束 | 关键词分级、年龄规则、回复校验与模板回退 |
| 可选语音 | FunASR 识别，CosyVoice 本地合成或 edge-tts 在线合成 |

这些机制不保证记忆始终正确、角色始终一致或固定时间内形成特定效果。

### 认识两个角色

| 角色 ID | 名称 | 设计方向 |
| --- | --- | --- |
| `mianmian` | 绵绵 | 慢节奏、共情优先、柔和表达 |
| `pengpeng` | 砰砰 | 行动优先、轻量挑战、游戏化表达 |

运行人设定义在 `character_layer.py`。`personas/` 提供设计说明，不会被程序自动加载。对话与关系数据按“用户 ID × 角色”分组，两个角色不会自动共享长期记忆。

### 快速开始

需要 **Python 3.10 或以上**。文字模式的离线验证使用 Python 3.12；语音环境需单独配置。下载或克隆项目后，在包含 `animon.py` 的仓库根目录运行以下命令。

#### Windows PowerShell

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
notepad .env
```

在本机 `.env` 中填写 `DEEPSEEK_API_KEY`，保存后运行：

```powershell
.\.venv\Scripts\python.exe seed_users.py
.\.venv\Scripts\python.exe animon.py -c mianmian -u alice
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

用文本编辑器打开本机 `.env`，填写 `DEEPSEEK_API_KEY` 并保存，再运行：

```bash
python seed_users.py
python animon.py -c mianmian -u alice
```

种子脚本提供 `alice`、`leo`、`ben` 三个演示档案，重复运行会更新同名 ID 的档案字段。首次运行会创建 `data/animon.db`。输入 `/quit` 退出，输入 `/switch pengpeng` 切换角色。

其他用户 ID 也可以开始对话。未登记或未设置年龄的用户按儿童安全规则处理；`-u` 只用于选择本地数据，不是登录认证。

### 配置

配置可写入仓库根目录的本机 `.env`，也可设置为系统环境变量；已有系统环境变量优先。**真实 key 只填写在本机 `.env`，公开的 `.env.example` 保持空密钥。**

| 环境变量 | 默认值 | 说明 |
| --- | --- | --- |
| `DEEPSEEK_API_KEY` | 空，聊天时必填 | 所配置模型服务的凭据 |
| `DEEPSEEK_BASE_URL` | `https://api.deepseek.com` | OpenAI 兼容的 Chat Completions 接口地址 |
| `DEEPSEEK_MODEL` | `deepseek-flash` | 代码默认模型，可按服务商可用模型覆盖 |
| `DEEPSEEK_THINKING` | `disabled` | 支持 `disabled`、`enabled`；`omit` 或空值不发送该扩展参数 |
| `DEEPSEEK_BETA_BASE_URL` | 从主地址生成 `/beta` 地址 | 严格工具调用入口；普通 CLI 聊天不使用 |
| `COSYVOICE_HOME` | 空 | CosyVoice 源码根目录，仅对应语音模式需要 |

更换兼容服务通常需要同时修改凭据、接口地址和模型名。若服务不接受 `thinking` 参数，设置 `DEEPSEEK_THINKING=omit`；具体兼容性需自行验证。

数据库路径、上下文窗口和原始对话保留策略等设置位于 `core.py` 的 `Config`，没有对应的环境变量或命令行开关。

### 常用命令与参数

| 对话命令 | 作用 |
| --- | --- |
| `/state`、`/facts`、`/turns` | 查看状态、关键事实与近期对话 |
| `/profile`、`/users` | 查看当前档案与已登记档案 |
| `/tasks`、`/done`、`/abandon` | 查看、完成或放弃任务 |
| `/traits`、`/observe`、`/consolidate` | 查看、抽取或整合表达倾向 |
| `/我们`、`/relationship` | 查看关系档案并生成即时反思，会请求模型 |
| `/switch mianmian`、`/switch pengpeng` | 切换角色 |
| `/reset` | 确认 `yes` 后重置当前用户与角色的关系 |
| `/debug`、`/quit` | 查看调试信息或退出 |

| 启动参数 | 作用 |
| --- | --- |
| `-c` / `--character` | 选择 `mianmian` 或 `pengpeng` |
| `-u` / `--user` | 指定用户 ID，默认 `default` |
| `--no-memory` | 停用新事实抽取，仍保存原始对话，其他记忆与倾向机制仍可使用 |
| `--no-state-delta` | 隐藏状态变化输出，状态仍更新 |
| `--sync-log data/outbox.jsonl` | 将变更另写本地日志，可能包含原始对话；默认关闭 |

运行 `python animon.py --help` 查看全部参数。

### 可选语音

| 启动参数 | 语音识别 | 语音合成 |
| --- | --- | --- |
| `--voice-stub` | 模拟输入 | 模拟输出 |
| `--voice-edge` | FunASR 整句 | edge-tts 在线 |
| `--voice-stream-edge` | FunASR 流式 | edge-tts 在线 |
| `--voice` | FunASR 整句 | CosyVoice 本地 |
| `--voice-stream` | FunASR 流式 | CosyVoice 本地 |

一次只选择一个模式。`--voice-stub` 不加载语音模型，但仍需配置对话模型。即使识别与合成在本地完成，对话生成默认仍依赖 API。

依赖、模型路径、设备配置及 `/auto` 连续听说说明见[语音配置](docs/VOICE_SETUP.md)。`requirements-lock.txt` 是原环境的版本快照，不是适用于所有平台的带哈希锁文件。

### 项目结构

| 模块 | 职责 |
| --- | --- |
| `animon.py` | 主循环、命令处理与模块编排 |
| `core.py` | 配置、共享数据类型、SQLite 存储与模型客户端 |
| `input_layer.py`、`character_layer.py` | 输入处理与角色定义 |
| `state_layer.py`、`memory_layer.py` | 状态更新与长期记忆 |
| `task_layer.py`、`decision_layer.py` | 任务管理与本轮决策 |
| `expression_layer.py`、`output_layer.py` | 提示词组织、模型生成与输出 |
| `user_layer.py`、`trait_layer.py` | 用户档案与表达倾向 |
| `relationship_layer.py` | 关系反思与里程碑档案 |
| `safety_policy.py` | 安全分级、年龄规则、校验与回退 |
| `voice_layer.py`、`sync_layer.py` | 可选语音与同步接口 |

详细数据流与扩展入口见[架构说明](docs/ARCHITECTURE.md)。HTTP 同步后端尚未实现；当前可选 JSONL 后端只写本地文件。

### 数据、隐私与使用边界

- 原始对话、档案和派生数据默认保存在本机 SQLite 中，未加密，原始对话默认持续保留。
- 生成回复时，当前输入、近期对话及所选档案、记忆、倾向等上下文会发送给配置的模型服务；派生分析可能产生额外请求。
- edge-tts 会将待朗读文本发送给在线语音服务。第三方服务按各自政策处理请求。
- `/reset` 删除当前关系的对话、事实、心情、任务、倾向、状态、轮次与历史反思；保留用户档案、安全事件及其他关系，不清理旧日志、录音、备份或第三方记录。
- 用户 ID 不提供访问控制，程序不适合直接作为公网多人服务。
- 安全规则可能误判或漏检，不能替代监护、专业支持或应急服务。未成年人使用需要监护参与与场景验证。

详见[隐私说明](docs/PRIVACY.md)和[安全说明](SECURITY.md)。`.gitignore` 不会过滤网页上传、手动 ZIP 或已有 Git 历史。

### 开发与验证

安装文字依赖后，在仓库根目录运行：

```bash
python -m unittest discover -s tests -v
python tools/check_release.py
```

离线测试使用临时数据库和模拟模型，无需真实 key，不调用付费 API。发布检查面向干净的候选目录；准备 Git 提交时，先暂存拟提交文件，再用 `python tools/check_release.py --staged` 检查实际暂存内容。

真实 API、音频设备和 GPU 语音环境需要另行验证。贡献流程见 [CONTRIBUTING.md](CONTRIBUTING.md)，问题反馈请使用仓库 Issues；安全漏洞按 [SECURITY.md](SECURITY.md) 私密报告。

### 文档与许可证

| 文档 | 内容 |
| --- | --- |
| [使用说明](docs/USER_MANUAL.md) | 日常操作、角色和任务 |
| [架构说明](docs/ARCHITECTURE.md) | 模块、数据流与扩展 |
| [语音配置](docs/VOICE_SETUP.md) | 语音环境与模型 |
| [隐私说明](docs/PRIVACY.md) | 保存、发送与删除范围 |
| [第三方说明](THIRD_PARTY_NOTICES.md) | 依赖来源与使用约定 |
| [GitHub 发布指南](docs/GITHUB_RELEASE.md) | 首次发布与后续更新 |

Animon 代码采用 [Apache License 2.0](LICENSE)。第三方依赖、模型、在线服务及声音素材各自的条款分别适用。本项目保留 edge-tts 接入仅作个人演示、不用于商业部署的约定，这与该 Python 库本身的许可证分别说明。

---

## English

### Overview

Animon is a modular Python prototype for AI companionship. It combines character definitions, persistent memory, emotional state variables, expression tendencies, and relationship archives so that conversations can draw on previous interactions.

The project provides a text-based command-line interface and optional speech input/output. Replies use the DeepSeek API by default. Character development is implemented through locally stored state, memory, and prompt context; it does not update the language model's weights online.

This release is intended for learning, prototyping, and further development. It does not include toy hardware, a web service, or model weights. You must configure your own model service and API key; usage may incur provider charges.

### Features

| Feature | Implementation |
| --- | --- |
| Two distinct characters | Different personas, tones, and response strategies for Mianmian and Pengpeng |
| Persistent memory | Model-assisted fact extraction and keyword-based retrieval for later conversations |
| Six state variables | Intimacy, mood, energy, courage, empathy, and curiosity change with interaction and inactivity |
| Evolving expression tendencies | Periodic extraction, reinforcement, decay, and consolidation of relationship-specific tendencies |
| Relationship archives | Milestone reflections and on-demand relationship summaries |
| Lightweight tasks | Suggestions, progress tracking, completion, and abandonment |
| Safety constraints | Keyword-based risk levels, age rules, reply validation, and fallback templates |
| Optional speech | FunASR recognition with local CosyVoice synthesis or online edge-tts synthesis |

These mechanisms do not guarantee accurate recall, consistent characterization, or a particular outcome within a fixed period.

### Characters

| Character ID | Name | Design direction |
| --- | --- | --- |
| `mianmian` | 绵绵 / Mianmian | A slower pace, empathy first, and gentle expression |
| `pengpeng` | 砰砰 / Pengpeng | Action first, small challenges, and playful interaction |

Runtime personas are defined in `character_layer.py`. The `personas/` directory contains design notes and is not loaded automatically. Conversation and relationship data are grouped by user ID and character; the two characters do not automatically share long-term memory.

### Quick start

Requires **Python 3.10 or newer**. Offline text-mode validation used Python 3.12; speech requires separate setup. After downloading or cloning the project, run these commands from the repository root containing `animon.py`.

#### Windows PowerShell

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
notepad .env
```

Set `DEEPSEEK_API_KEY` in your local `.env`, save it, then run:

```powershell
.\.venv\Scripts\python.exe seed_users.py
.\.venv\Scripts\python.exe animon.py -c mianmian -u alice
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

Open your local `.env` in a text editor, set `DEEPSEEK_API_KEY`, save it, then run:

```bash
python seed_users.py
python animon.py -c mianmian -u alice
```

The seed script supplies three demonstration profiles: `alice`, `leo`, and `ben`. Running it again updates profile fields for the same IDs. The application creates `data/animon.db` on first use. Enter `/quit` to exit or `/switch pengpeng` to change characters.

Other user IDs can also start conversations. Unknown or unset ages receive the child-oriented safety rules. The `-u` option selects a local data group; it is not authentication.

### Configuration

Use a local `.env` in the repository root or system environment variables. Existing system variables take precedence. **Put real keys only in your local `.env`; leave the public `.env.example` credential field empty.**

| Variable | Default | Purpose |
| --- | --- | --- |
| `DEEPSEEK_API_KEY` | Empty; required for chat | Credential for the configured model service |
| `DEEPSEEK_BASE_URL` | `https://api.deepseek.com` | OpenAI-compatible Chat Completions endpoint |
| `DEEPSEEK_MODEL` | `deepseek-flash` | Default in the code; override with a model available from your provider |
| `DEEPSEEK_THINKING` | `disabled` | `disabled` or `enabled`; `omit` or an empty value leaves out this extension |
| `DEEPSEEK_BETA_BASE_URL` | A `/beta` URL derived from the base URL | Strict tool-call endpoint; not used for ordinary CLI chat |
| `COSYVOICE_HOME` | Empty | CosyVoice source root, needed only for the corresponding speech modes |

Switching compatible providers usually requires changing the credential, endpoint, and model together. Set `DEEPSEEK_THINKING=omit` if the provider rejects the `thinking` extension. Provider compatibility requires separate verification.

Other settings, including the database path, context window, and raw-conversation retention policy, are defined in `Config` in `core.py`. They do not have corresponding environment variables or CLI switches.

### Commands and options

| Chat command | Action |
| --- | --- |
| `/state`, `/facts`, `/turns` | Inspect state, extracted facts, and recent conversation |
| `/profile`, `/users` | Inspect the current profile and registered profiles |
| `/tasks`, `/done`, `/abandon` | Inspect, complete, or abandon tasks |
| `/traits`, `/observe`, `/consolidate` | Inspect, extract, or consolidate expression tendencies |
| `/我们`, `/relationship` | View the relationship archive and generate a current reflection; calls the model |
| `/switch mianmian`, `/switch pengpeng` | Change characters |
| `/reset` | Reset the current user-character relationship after confirming `yes` |
| `/debug`, `/quit` | Inspect debug information or exit |

The Chinese `/我们` command and its English alias `/relationship` perform the same action.

| CLI option | Action |
| --- | --- |
| `-c` / `--character` | Select `mianmian` or `pengpeng` |
| `-u` / `--user` | Set the user ID; default: `default` |
| `--no-memory` | Disable new fact extraction; raw turns are still saved, and other memory/tendency mechanisms remain available |
| `--no-state-delta` | Hide state-change output without disabling state updates |
| `--sync-log data/outbox.jsonl` | Write local change events, potentially including raw conversations; disabled by default |

Run `python animon.py --help` for all options.

### Optional speech

| CLI option | Recognition | Synthesis |
| --- | --- | --- |
| `--voice-stub` | Simulated input | Simulated output |
| `--voice-edge` | FunASR utterance-based | Online edge-tts |
| `--voice-stream-edge` | Streaming FunASR | Online edge-tts |
| `--voice` | FunASR utterance-based | Local CosyVoice |
| `--voice-stream` | Streaming FunASR | Local CosyVoice |

Select one mode at a time. `--voice-stub` skips speech models but still requires the conversation model configuration. Local recognition and synthesis do not make the default conversation pipeline fully offline.

See [speech setup](docs/VOICE_SETUP.md) for dependencies, model paths, devices, and the `/auto` continuous-listening mode. `requirements-lock.txt` is a snapshot of an earlier environment, not a universal hash-locked installation specification.

### Project structure

| Module | Responsibility |
| --- | --- |
| `animon.py` | Main loop, commands, and orchestration |
| `core.py` | Configuration, shared types, SQLite storage, and model client |
| `input_layer.py`, `character_layer.py` | Input handling and character definitions |
| `state_layer.py`, `memory_layer.py` | State updates and persistent memory |
| `task_layer.py`, `decision_layer.py` | Task management and per-turn decisions |
| `expression_layer.py`, `output_layer.py` | Prompt construction, generation, and output |
| `user_layer.py`, `trait_layer.py` | User profiles and expression tendencies |
| `relationship_layer.py` | Reflections and milestone archives |
| `safety_policy.py` | Risk levels, age rules, validation, and fallbacks |
| `voice_layer.py`, `sync_layer.py` | Optional speech and synchronization interfaces |

See the [architecture guide](docs/ARCHITECTURE.md) for data flow and extension points. The HTTP synchronization backend is not implemented; the optional JSONL backend only writes local files.

### Data, privacy, and limitations

- Raw conversations, profiles, and derived data are stored in unencrypted local SQLite. Raw conversations are retained by default.
- The current message, recent turns, and selected profile, memory, and tendency context are sent to the configured model provider. Derived analysis can trigger additional requests.
- edge-tts sends text to an online speech service. Each provider applies its own data policies.
- `/reset` removes the current relationship's turns, facts, moods, tasks, tendencies, state, counters, and historical reflections. It retains profiles, safety events, and other relationships, and does not erase old logs, recordings, backups, or provider-held data.
- User IDs do not provide access control. The prototype is not ready to serve as a public multi-user service.
- Safety rules can produce false positives and miss risks. They do not replace supervision, professional support, or emergency services. Use with minors requires guardian involvement and scenario-specific validation.

See [privacy details](docs/PRIVACY.md) and the [security policy](SECURITY.md). `.gitignore` does not filter browser uploads, manually created archives, or existing Git history.

### Development and validation

After installing the text dependencies, run from the repository root:

```bash
python -m unittest discover -s tests -v
python tools/check_release.py
```

Offline tests use temporary databases and mocked models. They require no real key and make no paid API calls. The release checker targets a clean candidate directory. For a Git commit, stage the intended files first, then use `python tools/check_release.py --staged` to inspect the actual index contents.

Live API access, audio hardware, and GPU speech environments require separate validation. See [CONTRIBUTING.md](CONTRIBUTING.md) for contributions, use repository Issues for general feedback, and follow [SECURITY.md](SECURITY.md) for private vulnerability reports.

### Documentation and license

The supporting documents below are currently in Chinese.

| Document | Contents |
| --- | --- |
| [User manual](docs/USER_MANUAL.md) | Everyday operation, characters, and tasks |
| [Architecture](docs/ARCHITECTURE.md) | Modules, data flow, and extension points |
| [Speech setup](docs/VOICE_SETUP.md) | Speech environments and models |
| [Privacy](docs/PRIVACY.md) | Storage, transmission, and deletion scope |
| [Third-party notices](THIRD_PARTY_NOTICES.md) | Dependency sources and usage conventions |
| [GitHub release guide](docs/GITHUB_RELEASE.md) | Initial publication and later updates |

Animon's code is licensed under the [Apache License 2.0](LICENSE). Third-party dependencies, models, online services, and voice materials remain subject to their own terms. This project retains its personal-demonstration-only, non-commercial-deployment convention for the edge-tts integration; that convention is distinct from the Python library's own license.
