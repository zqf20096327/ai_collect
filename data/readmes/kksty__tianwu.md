# 天吴 · Tianwu

单用户、单实例、多项目的授权安全测试平台：Go 服务端 + Web 控制台，复用 cyber-harness 的 Hub 与 scan 承载模型会话、工具调用与观测。

> **当前是 0.x 版本。** 接口、账本格式与运行行为在 1.0 之前仍会变；账本格式变化不提供原地迁移，升级时请使用独立数据目录或新建项目（升级前先备份 `data/`）。不要把 0.x 当作稳定版产品，也不要直接用于无人值守的生产环境。

## 功能

- **图谱**：意图的前提、产出、引用与固定上下文是显式关系；事实断言、线索与原始证据分开存放。
- **意图生命周期**：创建、派发、交接、重试、停放与完成；每个 run 留下输入、状态、用量与停止原因。
- **协作**：执行者可以直聊、共享事实与交接。新意图由指挥官或操作员登记；执行者也可以自主决定下一步，需要新意图时提交结构化提议（可选），批准后才生成意图，派发是独立一步。
- **前提与复核**：必要前提须在当前断言版本上通过独立核验；成功意图进入复核阶段。复核默认开启，实例默认与单项目覆盖两级可设。
- **长会话**：笔记保存判断与回执，一个压力周期以有效交接收口后轮换会话；记忆载体是笔记与账本，不是会话本身。
- **操作员监督**：暂停/继续（因控制面重启而暂停的项目在对账后自动恢复；操作员暂停、指挥官停止与完成待命保持）、持续指令（通信页侧栏，可修改与撤销）、授权请求（只登记待办，处理结果唤醒指挥官）、人工接管、待办收件箱、运行停止；暂停原因分类落盘，操作员的盖章与撤销另写 `operator-actions.jsonl`。
- **工具审批**：需要人工决定的工具调用在 guardrail 命名空间挂起，由操作员批准或拒绝；裁判可插拔（`none`/`jev`/`llm`/`hybrid`）。
- **观测与分账**：AOP 采集运行事件、工具调用、命令与 HTTP 流量；token 按指挥官/执行者/裁判分账，只记录不设阈值。
- **模型与容量**：单一模型连接，保存后在线应用（不能在线生效时重启本机宿主）；项目与实例并发上限、单轮墙钟上限、空闲检测。
- **项目迁移**：`.twproj` 带账本快照与证据摘要，导入后以暂停状态落地。

## 环境要求

- Go 1.26 或更高（`go.mod` 声明 `go 1.26.0`）。
- Node.js 24 或更高（前端测试用 `node --test` 直接执行 `.ts`）与 pnpm（锁文件 `pnpm-lock.yaml`）。
- Git。
- Windows 上还需要 Git for Windows 提供的 Bash 与常用 POSIX 工具：宿主的 shell 工具依赖它们。

本地 gate 已在 Go 1.27.3、Node.js 26.9.0 上通过（2026-11-25）；前端检查另需 pnpm。

## 快速开始

控制面内嵌仓库里的前端产物，只改 Go 代码时不需要 Node。界面源码有改动时，先 `pnpm install --frozen-lockfile`、`pnpm build`，再构建 `tw`。

```powershell
pwsh -File scripts/build-harness.ps1 -HarnessDir ../cyber-harness   # -> bin/cyber-harness.exe + bin/cyber-scan.exe
go build -o bin/tw.exe ./cmd/tw
./bin/tw.exe --harness ./bin/cyber-harness.exe --scan ./bin/cyber-scan.exe --data ./data
```

Linux / macOS 用 `scripts/build-harness.sh`，`bin/tw` 不带后缀。启动后做三条最小验证：

1. `GET /healthz` 返回 200。
2. 带控制台令牌请求 `GET /api/projects` 返回 200。
3. `data/console.token` 已生成。

完整启动参数见 `tw --help`。

## 使用流程

1. **配置模型连接。** 启动前设置 `CYBER_BASE_URL`、`CYBER_API_KEY`、`CYBER_MODEL`，或在「设置 → 模型连接」中填写；保存结果会说明已在线应用，还是需要重启宿主。
2. **打开控制台。** 默认 `http://127.0.0.1:8080`，令牌在 `data/console.token`（首次启动生成）。令牌与账本、证据同在实例目录：一起备份、一起收紧权限，代价是执行者的文件工具也能读到（见[安全策略](SECURITY.md)）；需要隔离时用 `--console-token-file` 指到数据目录之外。
3. **建项目。** 写三份文档：起点（范围与已有信息）、终点（验收标准）、内置约束（必须守住的东西）。三份原文就是授权边界，代码不另加规则；边界可随项目推进在控制台更新。
4. **让它跑。** 启动项目后，指挥官按文档与图谱派意图，执行者接意图执行；「图谱」看待办、事实与证据，「项目状态」看谁在跑、为什么停。
5. **随时接管。** 暂停/继续、给指挥官发指令、在待办里处理审批；需要人工决定的工具调用会挂起等操作员。
6. **复盘与带走。** 每个 run 有输入、状态、用量与停止原因；报告预检从结论直达原始证据；整项目可导出为 `.twproj`。

第一次上手建议用本地假模型网关或隔离环境跑一遍，只看流程是否通，不要直接指向真实资产。

## 常用命令

| 用途 | 命令 |
| --- | --- |
| 本地门禁（构建、静态检查、测试、前端检查、文档链接、AOP 漂移、构建清单） | `pwsh -File scripts/gate.ps1`，Linux 为 `./scripts/gate.sh`（等价 `make gate`） |
| Go 测试（串行） | `go test ./cmd/... ./internal/... -p 1 -count=1` |
| 前端检查 | `pnpm --dir web typecheck` 与 `pnpm --dir web test` |
| 收一个 run 供复盘 | `pwsh -File scripts/collect-run.ps1 -Project <项目ID> -Out <out.zip>` |
| 长跑外部看护（默认只观察） | `pwsh -File scripts/watchdog.ps1 -Project <项目ID>` |
| 版本 | `./bin/tw.exe --version` |

## 架构与目录

服务边界、事实与意图的运行模型、复核与交接见[核心架构](docs/01-architecture.md)：[§1.1](docs/01-architecture.md#11-事实与意图的运行模型)是正式架构图，[§9](docs/01-architecture.md#9-兼容与验证边界)是升级与迁移边界。

```text
cmd/        tw（服务端）、tw-gate（本地门禁）、tw-repair（离线修复）、tw-manifest、tw-metrics、
            redact-logs（历史日志脱敏）；ledger、aopspike 是开发用工具
internal/   api（HTTP/路由）、decider（指挥官循环）、store（账本）、host（Hub/scan 监督）、
            project（项目清单）、verifier（复核）、report（报告）、board（态势投影）、aop（生成代码）
web/        src（控制台）、packages/ui 与 packages/theme（组件库，随主仓维护）
scripts/    gate、build-harness、collect-run、watchdog、check-docs 等入口
docs/       01-architecture.md
data/       运行时实例目录（账本、项目、证据、console.token），不随仓库分发
```

## 构建清单

gate 的最后一步写 `.build/build-manifest.json`（步骤清单见 `cmd/tw-gate/main.go:8-25`）：源码身份（仓库根、commit、branch、dirty、工作树补丁 SHA-256）、harness 身份与提交、AOP 生成文件的聚合 fingerprint 与逐文件 SHA-256、协议版本、平台与工具链、模型连接与真实上游 model id、各二进制的 sha256 与 `--version` 输出。清单从不写 API key。

## 离线修复交接游标

历史有效置信度、交接游标的修复都要求项目暂停且 `tw` 已停止，先预览、核对后再提交：

```powershell
./bin/tw-repair.exe --project <项目绝对目录> --confidence            # 预览
./bin/tw-repair.exe --project <项目绝对目录> --confidence --commit   # 先备份账本再写回
./bin/tw-repair.exe --project <项目绝对目录> --intent <精确意图ID>    # 预览该意图的交接游标
```

`--commit` 只写回能保留断言哈希的派生标签或与现存声明一致的游标，并保留修复前的游标、文件摘要与审计记录。

## 免责声明

- **只用于已获授权的目标。** 天吴是安全测试工具，未经目标所有者书面授权对其系统做测试可能构成违法；授权范围由使用者自行取得并负责，本项目不提供任何目标清单或授权。
- **按「现状」提供，不附带担保。** 依 AGPL-3.0 分发，不承诺适销性、特定用途适用性或不侵权；因使用本软件造成的任何直接或间接损失，作者与贡献者不承担责任。
- **测试会改变目标状态。** 扫描、上传、登录尝试都可能留下痕迹或影响业务；请在隔离或可回滚的环境先行验证，风险与后果由使用者承担。
- **数据与合规由使用者负责。** 账本、证据与抓取的流量可能含个人信息或敏感数据，保存、传输与销毁须符合所在地法律与授权约定。
- 本项目与任何被测试的第三方无关；文中出现的产品名仅用于说明。

## 贡献与许可

提交前跑本地门禁；约定见 [CONTRIBUTING.md](CONTRIBUTING.md) 与 [agent.md](agent.md)。测试与演示只使用临时目录、本地假模型或明确授权的隔离环境，不把协议测试表述为真实效果。

天吴以 [AGPL-3.0](LICENSE) 发布；第三方内容的来源和许可见 [NOTICE](NOTICE)。
