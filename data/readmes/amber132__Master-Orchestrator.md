<div align="center">

# Master Orchestrator

**一条命令把"重构这 15 个文件"分解成 DAG，让多个 Claude / Codex 并发跑，按阶段路由不同模型，Simple 模式自动检测越权改动并回滚。**

[![CI](https://github.com/amber132/Master-Orchestrator/actions/workflows/ci.yml/badge.svg)](https://github.com/amber132/Master-Orchestrator/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Stars](https://img.shields.io/github/stars/amber132/Master-Orchestrator.svg)](https://github.com/amber132/Master-Orchestrator/stargazers)

[English](./README_EN.md) | [快速开始](#快速开始) | [工作原理](#工作原理) | [示例](./examples) | [文档](#文档)

</div>

---

## 它解决什么问题

单个 `claude` 或 `codex` 跑大任务时常见的痛点：

- 改 15 个文件 → 上下文溢出，最后几个文件和前面不一致
- 100+ 个 lint 错误要修 → 串行慢，失败靠手工重跑
- 复杂功能（中间件 + 路由 + 测试 + 文档）→ 一个 agent 同时做规划和执行，规划深度不够
- Simple 批量模式下一个 worker 偷偷改了不该改的文件 → 校验阶段识别并自动 git revert

Master Orchestrator 把目标自动拆成 DAG，按阶段路由给最合适的模型（Claude 规划 / Codex 写代码 / Claude 审查），并发跑。Simple 模式额外内置越权改动检测和自动回滚；DAG 模式由评审引擎在收敛阶段输出回滚计划（人工或后续 simple run 执行）。

## 方案

Master Orchestrator 把一个自然语言目标转换成**有向无环图（DAG）**任务，再按阶段选择最合适的 AI Agent 执行：

```bash
mo do "给 Express 应用添加 JWT 鉴权，包括中间件、路由、测试和 API 文档"
```

它会自动完成：

1. **任务分解**：把目标拆成有依赖关系的子任务，规划阶段默认交给 Claude
2. **阶段路由**：按任务类型选择 provider，例如 Claude 负责推理，Codex 负责执行
3. **并行执行**：没有依赖冲突的任务并行跑，DAG 模式默认 `max_parallel=4`，Simple 批量模式默认 16 个 worker，均可在 `config.toml` 中放大
4. **交叉审查**：用另一个 Agent 做结果验证和质量门禁
5. **失败重试**：按错误类型分类，使用指数退避重试
6. **结果收敛**：合并输出、跑测试、确认最终交付一致；Simple 模式下校验阶段会对越权改动自动 `git checkout` 回滚

## 为什么需要 Master Orchestrator

| 场景 | 单 Agent | Master Orchestrator |
| --- | --- | --- |
| 5 个文件的重构 | 容易上下文溢出，改动不一致 | DAG 分解，并行执行 |
| 100+ 文件批量修复 | 串行、慢、失败后靠手工重跑 | Simple 模式：16 并发、自动重试 |
| 复杂功能开发 | 人工协调多个会话 | 自动阶段路由，检测收敛状态 |
| 混合型任务 | 同一个模型同时负责规划和写代码 | Claude 做规划，Codex 做执行 |

## 快速开始

### 安装

```bash
git clone https://github.com/amber132/Master-Orchestrator.git
cd Master-Orchestrator
pip install -e ".[dev]"
```

需要 Python 3.11+，并且本机 PATH 中至少能使用 `claude` 或 `codex` 其中之一。

### 第一个编排任务

```bash
# 让编排器自动选择 provider
mo do "给 src/routes/ 下所有 POST 接口补充输入校验"

# 强制使用指定 provider
mo do --provider codex "给 UserService 类生成单元测试"

# 按阶段混用 provider：Claude 规划，Codex 执行，Claude 审查
mo do \
  --phase-provider decompose=claude \
  --phase-provider execute=codex \
  --phase-provider review=claude \
  "重构支付模块，让它支持多币种"
```

### 用 Simple 模式处理批量任务

适合几百个独立工作项，例如 lint 修复、格式化、规则化小改动：

```bash
# 从任务清单扫描并执行
mo simple run --manifest tasks.jsonl

# 中断后继续
mo simple resume

# 只重试失败项
mo simple retry
```

Simple 模式默认最多运行 **16 个并发 worker**，内置自动重试、语法验证和崩溃恢复。

## 工作原理

```
                    ┌─────────────────────────────────────────────┐
                    │            你的目标（自然语言）              │
                    └────────────────────┬────────────────────────┘
                                         │
                    ┌────────────────────▼────────────────────────┐
                    │            分解（Claude）                    │
                    │       目标 → 有依赖关系的 DAG 子任务          │
                    └────────────────────┬────────────────────────┘
                                         │
              ┌──────────────────────────┼──────────────────────────┐
              │                          │                          │
    ┌─────────▼─────────┐    ┌──────────▼──────────┐    ┌─────────▼─────────┐
    │  任务 A (Claude)   │    │  任务 B (Codex)      │    │  任务 C (Codex)    │
    │  "写中间件"        │    │  "写路由"            │    │  "写测试"          │
    └─────────┬─────────┘    └──────────┬──────────┘    └─────────┬─────────┘
              │                          │                          │
              └──────────────────────────┼──────────────────────────┘
                                         │
                    ┌────────────────────▼────────────────────────┐
                    │            审查（Claude）                    │
                    │       跨 Agent 验证与质量门禁                 │
                    └────────────────────┬────────────────────────┘
                                         │
                    ┌────────────────────▼────────────────────────┐
                    │            收敛                              │
                    │       合并结果、运行测试、验证输出            │
                    └─────────────────────────────────────────────┘
```

### Provider 路由

流水线的每个阶段都可以使用不同 AI Agent：

| 阶段 | 默认 Provider | 原因 |
| --- | --- | --- |
| `decompose` | Claude | 更适合规划和依赖分析 |
| `execute` | Codex | 更适合高吞吐代码生成 |
| `review` | Claude | 更适合推理正确性和发现问题 |
| `discover` | Claude | 更适合调研和探索 |
| `simple` | Codex | 面向批量任务做了吞吐优化 |

可以在不同层级覆盖默认路由：

```bash
# 全局指定
mo do --provider claude "..."

# 按阶段指定
mo do --phase-provider execute=codex --phase-provider review=claude "..."

# 配置文件 config.toml
[routing.phase_defaults]
execute = "codex"
review = "claude"
```

### 错误恢复

编排器会识别错误类型，并选择对应策略：

- **限流**：指数退避并加入抖动
- **上下文溢出**：自动压缩上下文后重试
- **临时失败**：最多重试 10 次，默认 30 秒基础退避
- **Provider 不可用**：在 auto 模式下切换到备用 provider
- **任务失败**：向依赖任务传播状态，跳过不可达任务

### 收敛检测

系统会持续检查：

- **停滞**：多轮没有进展时升级或切换策略
- **劣化**：质量下降时回滚到上一个可用状态
- **回归**：原本通过的测试失败时暂停并提示

## 架构

```
master_orchestrator/
├── cli/                  # 统一 CLI 入口（mo do / runs / improve / dashboard）
├── config.py             # TOML 配置加载
├── model.py              # 核心数据模型
├── scheduler.py          # 感知 DAG 依赖的任务调度
├── convergence.py        # 质量收敛检测（含 ConvergenceDetector）
├── convergence_deterioration.py  # 恶化趋势检测
├── review_engine.py      # 审查引擎主入口
├── review_engine_parser.py       # 审查 JSON 解析与评分校验
│
├── cli/                  # do/simple/improve/dashboard 子命令
├── orchestrator/         # DAG 执行核心：主循环 / 任务调度 / 收尾
├── autonomous/           # 目标驱动的自治控制器
├── simple/               # 高吞吐批量执行模式
│   └── _conflict_detection.py / _metrics.py / _slot_planning.py  # 拆出的纯函数
├── self_improve/         # 自我改进循环（discover / phases / rollback / workspace）
├── architecture/         # 架构层会审（contract / council / execution / trigger）
├── observability/        # 监控/告警/日志/心跳/网络健康/诊断
├── pool/                 # provider 池/路由/故障切换/双池
├── runtime/              # 进程/资源/优雅停机/平台特定 worker
├── errors/               # 错误分类/恢复策略
├── claude_cli/ codex_cli/  # provider 适配（subprocess + 输出解析）
├── store/                # SQLite 状态持久化（_dag_ops / _simple_ops / _aux_ops / 迁移）
├── task/                 # 任务建模（intake / classifier / contract / templates / cache）
├── context/              # 上下文管理（compactor / quarantine / summarizer / store）
├── auto_model/           # 自治模式数据模型
├── discover/ external_source/  # 自我改进的代码发现与外部信号
├── web/                  # dashboard 服务端
└── ...（其余 ~65 个单职责顶层模块，完整清单见 docs/MODULES.md）
```

完整模块清单（自动生成）：[docs/MODULES.md](./docs/MODULES.md)。

子包之外，顶层另有用于错误分类、限流、监控、预算追踪、provider 路由等单一职责模块。完整模块清单见 [docs/MODULES.md](./docs/MODULES.md)（由 `python scripts/gen_architecture_docs.py` 自动生成）。

## 配置

```toml
# config.toml
[orchestrator]
max_parallel = 4          # DAG 模式默认；autonomous 模式可放大到 200

[simple]
max_running_processes = 16                 # Simple 批量模式默认并发
auto_recover_unauthorized_changes = true   # 越权改动自动 git revert

[claude]
default_model = "sonnet"
default_timeout = 1800
max_budget_usd = 1000.0

[codex]
default_model = "gpt-5.4"
default_timeout = 1800
execution_security_mode = "restricted"

[routing]
default_provider = "auto"
auto_fallback = true

[routing.phase_defaults]
decompose = "claude"
execute = "codex"
review = "claude"
```

完整示例见 [config.toml](./config.toml)。

## 文档

| 文档 | 说明 |
| --- | --- |
| [USAGE.md](./USAGE.md) | 使用指南和示例 |
| [CLI 参考](./docs/CLI_REFERENCE.md) | 全部命令和参数 |
| [Provider 与路由](./docs/providers-and-routing.md) | Provider 配置与路由机制 |
| [Simple 模式](./docs/simple-mode.md) | 高吞吐批量执行模式 |
| [Simple 验证](./docs/simple-validation.md) | Simple 模式验证管线配置 |

## 使用场景

**功能开发**

```bash
mo do "用 WebSocket 添加实时通知，包括服务端、客户端、断线重连逻辑和测试"
```

**代码迁移**

```bash
mo do --phase-provider execute=codex "把 src/components/ 下所有 class component 迁移为 hooks 写法"
```

**批量修复**

```bash
mo simple run --manifest lint-fixes.jsonl
```

**自我改进**

```bash
mo improve -d ./my-project --discover
```

## 参与贡献

贡献指南见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

## 许可证

[MIT](LICENSE)

---

<div align="center">

**如果 Master Orchestrator 帮你更快交付，欢迎点一个星标。**

[![Star History Chart](https://api.star-history.com/svg?repos=amber132/Master-Orchestrator&type=Date)](https://star-history.com/#amber132/Master-Orchestrator&Date)

</div>
