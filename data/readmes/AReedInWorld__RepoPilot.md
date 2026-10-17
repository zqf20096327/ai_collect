# RepoPilot

基于 **Deep Agents 0.7.19** 的代码修复 CLI。输入一个固定 Python 项目的 bug 任务，Agent 在 Docker 中调查、改代码和运行开发测试；系统冻结候选，由独立验收器评分。失败时有限重试，并支持候选保存后的跨进程恢复。

本项目用于展示 Agent 应用工程：执行边界、测试判定、预算、可追溯记录和恢复机制。只支持一个预置仓库、三个独立 `seeded_bug`，不是任意仓库修复平台。

## 安装

需要 Git、uv、Python 3.12 和运行 Linux 容器的 Docker Desktop。本项目在 Windows 11 + WSL 2 上开发；运行时通过 Docker CLI，不向容器暴露 Docker socket。

使用 PowerShell 克隆项目并安装依赖：

```powershell
git clone https://github.com/AReedInWorld/RepoPilot.git
cd RepoPilot
uv python install 3.12
uv sync --frozen
if (-not (Test-Path -LiteralPath '.env')) {
    Copy-Item -LiteralPath '.env.example' -Destination '.env'
}
```

编辑本机 `.env`，填入真实 `LLM_API_KEY`，保留以下配置：

```dotenv
LLM_BASE_URL=https://api.deepseek.com
LLM_MODEL_ID=deepseek-flash
LLM_API_KEY=在本机填写
REPOPILOT_IMAGE=repopilot-eval:0.1
```

`.env` 不提交。模型使用 Chat Completions、thinking disabled、temperature 0、最大输出 4096 tokens；提供方 SDK 重试关闭。框架摘要重试仍会发生，计入同一 run 的请求预算。

启动 Docker Desktop 并确认 Linux 引擎就绪，然后构建固定镜像：

```powershell
uv run python -m repopilot env build
uv run python -m repopilot doctor
uv run python -m repopilot doctor --probe-model
```

`doctor` 默认不会请求模型。`--probe-model` 最多进行两次小型付费请求，验证连接和工具调用。未配置、连接失败、环境未准备均有独立状态。

构建使用 `docker/base-image.json` 固定的基础镜像 digest，离线运行前预装锁定的 pytest、pytz 及测试依赖。Docker 镜像 ID 随 run 保存；重建为不同 ID 后不能用于恢复旧 run。

若已有 uv Python 3.12 链接损坏，可在项目内安装后再同步：

```powershell
$env:UV_PYTHON_INSTALL_DIR = Join-Path (Get-Location) '.repopilot\python'
uv python install 3.12
uv sync --frozen --python 3.12
```

## 一次完整修复

```powershell
uv run python -m repopilot tasks list
uv run python -m repopilot tasks validate --all
uv run python -m repopilot run --task bug-01 --mode harness
uv run python -m repopilot report --run-id <上一条输出的run_id>
```

任务基于 MIT 许可的 `dbader/schedule` 1.2.2，固定 commit `82a43db1b938d8fdf60103bd41f329e06c8d3651`。三题分别为假值标签误清理、取消实例失效和返回列表污染内部队列。每题从独立故障基线开始，只允许提交 `schedule/__init__.py`；它们不是上游真实 issue。

`tasks validate --all` 使用已知补丁，分别验证原版、故障版和参考修复，**不是模型成绩**。每次保存新证据目录，不覆盖旧记录。正常候选需通过 81 项上游回归和 18 项外部业务断言；外部断言与 JUnit 由不导入候选源码的可信宿主 pytest 进程生成。

## 候选阶段恢复

```powershell
uv run python -m repopilot run --task bug-01 --mode harness --stop-after-ready
uv run python -m repopilot resume --run-id <输出中的run_id>
```

两条命令启动不同进程。恢复直接验收保存的候选，不重新调用模型；失败后若预算仍允许，才开启下一轮修复。只能恢复 `READY_FOR_VERIFY`，不恢复生成中的回答或工具进程。30 分钟绝对时限包含暂停时间，请及时恢复。

## 对照实验与证据

```powershell
uv run python -m repopilot compare --all
```

六次运行串行执行，每次使用新工作区。baseline 只允许一次 Agent 修复调用；harness 最多三轮，并获得外部失败反馈。两者总预算相同：30 次模型请求、1800 秒；单次请求 90 秒、工具命令 60 秒、完整验收 120 秒。摘要、失败及框架重试均计数；token 使用量未知时不填零，调用预算不是严格费用上限。

运行产物位于 `.repopilot/runs/<run_id>/`：

- `report.json` / `report.md`：状态、候选、测试、预算和失败原因。
- `events.jsonl`、`budget.json`：阶段、调用事件和持久化预算。
- `candidates/<轮数>/`：完整允许源码、可应用补丁及恢复清单。
- `verification/<轮数>/`：结构化结果、可信 JUnit 和回归日志。
- `logs/tools/`：有大小上限且脱敏的工具输出。

`compare` 将脱敏结果归档到 `evidence/runs/`，并输出 `evidence/comparison.json`。真实结果见 [docs/results.md](docs/results.md)，实施清单见 [TODO.md](TODO.md)。六次对照不证明行业成功率，也不保证 harness 比 baseline 更好。

## 测试与限制

```powershell
uv run python -m pytest -q
```

Docker 集成测试会检查镜像可用性；环境不满足时明确 skip。模型相关机制测试使用模拟 HTTP，不计作真实模型修复。完整测试包含预算失败、摘要重试、超时后子进程终止、补丁重放、恶意或缺失测试结果拒绝、跨进程恢复与损坏清单拒绝。

若 Windows 测试临时目录存在权限问题，使用新的项目内临时路径：

```powershell
uv run python -m pytest -q --basetemp .repopilot/test-temp-new -p no:cacheprovider
```

CLI 非成功退出码为 2，命令行参数错误也为 2；中断为 130。`READY_FOR_VERIFY` 是演示暂停成功，不代表代码已经通过验收。已完成 run 的重复恢复不执行模型或测试。

本项目仅支持受控固定样例；Docker 隔离与外部业务断言不构成对任意恶意 Python 行为的完整证明。原项目回归在候选容器内运行，其 JUnit 不能单独授予成功。符号链接、路径穿越、二进制和修改范围外文件不被接受。候选缓存不属于交付源码。

架构与能力分工见 [docs/architecture.md](docs/architecture.md)，可执行演示见 [docs/demo.md](docs/demo.md)。许可证与来源见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
