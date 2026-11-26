<div align="center">

# ARTEX-redev

**ARTEX 的二次开发版（fork）** · 授权范围内的 AI 安全作业台

从「一条指令打到穿」走向「有硬边界的作业台 + 离线分析域」：在线授权测试、二进制逆向、
源码审计、恶意样本分析、蓝队检测，共用一套策略执行层与证据链。

[![ci](https://github.com/br0ny4/artex-redev/actions/workflows/ci.yml/badge.svg)](https://github.com/br0ny4/artex-redev/actions/workflows/ci.yml)
[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](LICENSE)
[![Go](https://img.shields.io/badge/Go-1.26-00ADD8.svg)](go.mod)
[![Status](https://img.shields.io/badge/status-alpha-orange.svg)](docs/redev/05-decisions.md)

</div>

---

## 这是什么

本仓库是开源项目 **ARTEX v0.3.15**（作者 [Autumn-27](https://github.com/AUTUMN-27)）的
**二次开发（fork）版本**，依 **AGPL-3.0** 继续开源。

- **上游已于 2026-10-08 闭源并删除仓库**，本仓库基于其最后一个开源版本（v0.3.15，2026-10-07）；
- 本仓库与原作者、版权方**无关**，不代表其立场，也不提供任何商业版本；
- 上游 README 原文存档在 [`README.upstream.md`](README.upstream.md)，改动说明见 [`NOTICE`](NOTICE)。

> ⚠️ **不要使用任何第三方预构建镜像。** 上游下线后已出现带 root 后门的镜像
> （`tomicdd/artex`，9000+ 次拉取），详见 [`docs/redev/01-abuse-and-status.md`](docs/redev/01-abuse-and-status.md)。
> 本仓库的镜像只从本仓库源码构建，并走 GHCR。

## 为什么做这个 fork

ARTEX 自 2026-08 起被多个威胁行为者当作攻击基础设施使用：FBI 于 2026-11-13 发布
FLASH 通报，全球金融/政府/科技/国防等行业受影响；公网上有 1400+ 台无鉴权控制台可被接管。
这件事本身说明两件事：

1. **自主 Agent 的能力是真的**（正因如此才需要它）；
2. **上游的安全边界是假的**——授权范围校验已被移除、无规则命中即放行、LLM 裁判失败即允许、
   默认监听所有网卡、未认证即可抢占实例。

所以这个 fork 不做"更强的攻击工具"，而是把**边界做成真的**，并把能力从"在线打点"扩展到
安全从业者真正的工作面（挖洞、逆向、审计、样本、蓝队）。

## 与上游的差异

| 方面 | 上游 v0.3.15 | 本仓库 |
|---|---|---|
| 模块路径 | `github.com/Autumn-27/artex` | `github.com/br0ny4/artex-redev` |
| 授权范围（RoE） | **已移除**，无范围校验 | `engagement` 数据模型 + 网络层强制（L2）+ 代理层语义判定（L3） |
| 默认放行 | 无规则命中 → 放行；裁判失败 → allow | 启用策略后**默认拒绝**；判不清 → 挂起问询 |
| 监听地址 | `:8787` 全网卡 | **`127.0.0.1:8787`**（compose 同样只绑回环） |
| 登录爆破 | 无限制 | 同 IP 10 分钟失败 5 次 → 锁 15 分钟 |
| 流量录制 | 可关闭（关掉即绕过一切代理层判定） | 启用策略后**强制开启且不可关闭**；无代理则拒绝启动 |
| 响应内容 | 原样交给模型 | 命中源码/配置/密钥 → **截断，原文不进上下文** |
| 审计 | 工具调用审计环 | 判定全量落 `policy_decisions`（hash chain），可校验完整性 |
| 文档 | — | `docs/redev/`：滥用态势、代码地图、工具选型、策略引擎设计、决策记录 |

更细的差异见 [`docs/redev/09-diff-from-upstream.md`](docs/redev/09-diff-from-upstream.md)（逐项对照）
与 [`docs/redev/05-decisions.md`](docs/redev/05-decisions.md)（决策记录）。

## 定位与守则

上游的骨架（多角色编排、探索图、全量流量录制、findings 与流量快照绑定）我们**一行没改**——
那是它真正的价值，也是"结论可回放到具体请求"的前提。这个 fork 只在两根轴上收紧：

1. **边界为真**：没有授权记录就发不出包，判不清就全量停止，录制不可关闭；
2. **证据机器化**：0day 结论必须过三道门（PoC 可复现 + ≥5 条反例 + ≥3 次跨源撞车比对），
   其中 PoC 可由平台经录制代理重放、撞车检索可由平台代查 NVD / CISA KEV。

为什么这样切、守什么/改什么、以及诚实的风险登记，见
[`docs/redev/10-positioning.md`](docs/redev/10-positioning.md)。该文档里的代码坐标、接口与
测试锚点由 `internal/docscheck` 在 CI 里校验——改代码不改文档会红，避免"定位"变成过时叙事。

## 进展与计划

> 本节**每次提交都更新**：记录"现在到哪、下一步做什么"。最近更新：2026-11-24（`bounty-recon` 在线侦察域包）。
> 状态：✅ 已完成 · 🚧 进行中 · 📋 计划中

### 当前状态

- **版本线**：Fork-0.3.0 已发布（5 平台二进制 + GHCR 多架构镜像）；`main` 持续迭代，发布按需打 tag。
- **域包（5 个）**：`web-pentest`（在线测试）、`bounty-recon`（在线侦察，只看不动）、
  `binary-re`（离线逆向）、`source-audit`（源码审计）、`malware-triage`（样本分诊）。
- **执行层**：L1 命令出口（含宿主机边界）、L2 出网收口、L3 请求/响应判定、预算与 Stop-All、
  哈希链判定审计；未配置 engagement 时保持上游行为。
- **证据链**：三道准入门（PoC 可复现 ≥2 次 / 反例 ≥5 条 / 跨源撞车 ≥3 次且复核留痕）；
  候选与逐跳可达性工件（证据由平台核对，不采信自称）。
- **前端**：`/system/policy` 规范执行操作台、仪表盘停止横幅与拦截统计、漏洞详情「准入」页、
  任务详情「候选」页。

### 里程碑

| 阶段 | 内容 | 状态 |
|---|---|---|
| P0 | 安全硬化：默认回环、登录限速、fail-closed 开关、镜像自建 | ✅ |
| P1 | 内核：engagement 数据模型、**域包（domain pack）抽象**、产物模型扩展 | ✅ 域包抽象已落地（[07](docs/redev/07-domain-packs.md)） |
| P1.5 | **规范执行层**：L1 命令/工具、L3 请求与响应、L2 出网强制、判定审计链 | ✅ |
| P1.6 | hold 生命周期（全量停止 → 操作员答复 → 恢复 → 任务暂停/续跑）、操作台 | ✅ |
| P1.7 | `/api/auth/init` 一次性 setup token + 前端配合 | ✅ |
| P2 | 离线域包：`binary_re`、`source_audit`、`malware_triage`；离线域只守宿主机边界 | ✅ |
| P2.5 | 0day 流水线：候选 → 可达性 → 触发验证 → **三道准入门**（PoC 可复现 + ≥5 条反例 + ≥3 次跨源撞车比对） | ✅ 门与候选均落地（[08](docs/redev/08-0day-pipeline.md)） |
| P3 | 在线域包：`web_pentest` ✅、`bounty_recon`（侦察，只看不动）✅、CDP 浏览器分析 | 🚧 CDP 未开始 |
| P4 | 蓝队域包（检测工程 + agentic 攻击者检测规则）、多域报告、测评台（XBOW 104） | 📋 |

### 下一步（按优先级）

1. **CDP 浏览器分析**：`chrome-devtools-mcp` + `playwright-mcp` 组合，覆盖登录态、前端 API
   挖掘、JS 去混淆；WebSocket 帧捕获缺工具，需要小 CDP shim。
2. **预算余量进仪表盘**：值班要能一眼看出"这个任务还剩多少次请求"。
3. **合规矩阵端到端**：越界/停止/清理/报告脱敏的完整链路用例。
4. **L2 netns 自动化**：把 `deploy/egress-lockdown` 从"建议"变成 compose 默认。

已落地的实现与"为什么这么定"记录在 [`docs/redev/05-decisions.md`](docs/redev/05-decisions.md)；
设计细节见 [`docs/redev/04-policy-engine.md`](docs/redev/04-policy-engine.md)。

## 快速开始

### 1. 源码运行

```bash
git clone https://github.com/br0ny4/artex-redev.git
cd artex-redev
go build -o artex ./cmd/artex        # 需要 Go 1.26+
./artex                              # 默认只监听 127.0.0.1:8787
```

需要 PostgreSQL（`ARTEX_PG_DSN` 或 `config.json`）；首次打开 `/setup` 设置管理员密码。

启动日志会打印一行初始化口令，`/setup` 要求填入——没有它任何人都能在设密码前抢占实例
（公网裸奔控制台最常见的失陷路径）。也可用 `ARTEX_SETUP_TOKEN` 固定。

### 2. Docker Compose

```bash
cp .env.example .env                 # 填 POSTGRES_PASSWORD
docker compose up -d                 # 镜像来自 ghcr.io/br0ny4/artex-redev
```

镜像按 tag 发布（`ghcr.io/br0ny4/artex-redev:v0.3.0`，`latest` 指向最新版本）；
v0.2.0 / v0.3.0 均已实测可拉取（linux/amd64 + linux/arm64 多架构 manifest）。
需要自己改工具链时用源码构建：

```bash
./build-image.sh                     # 内部走 Dockerfile.local，构建后启动
```

### 3. 启用规范执行层（在线测试必做）

只填一个部署上下文文件，平台就会在三个出口强制判定：

```bash
cp policy/web-pentest/deployment-context.example.yaml policy/web-pentest/deployment-context.yaml
# 填写：授权范围、测试账号、允许工具、报告出口、产物目录、授权时间窗
export ARTEX_ENGAGEMENT_FILE=./policy/web-pentest/deployment-context.yaml
./artex
```

启用后：

| 出口 | 行为 |
|---|---|
| **L1** 命令/工具 | 扫描器未审批、内联解释器、RCE 只读白名单、敏感文件读取、命令目标越界 → 拦截 |
| **L3** 请求 | 范围外 / 删除类 / 覆盖类 / 资金类 / 未标注测试账号 → **不发包**，回平台管控 403 |
| **L3** 响应 | 源码、配置、密钥、超限响应 → 截断，原文不进模型上下文 |

查看判定与证据链：`GET /api/policy/status`、`/api/policy/decisions`、`/api/policy/chain`。

**需要人确认时全量停止**（规范 7.3）：范围归属不明 / 接口语义判不清 / 预算耗尽时，平台会挂起整个
engagement，把问题原样转给操作员；未获明确答复前所有请求与命令都被挡下。挂起时平台还会**暂停正在运
行的任务**（等待答复可能几小时，不暂停就是空烧 token），答复并恢复后自动续跑——只续跑因挂起被暂停的
任务，操作员自己暂停的不动。

页面入口：**系统 → 规范执行**（`/system/policy`），可直接答复挂起、看判定流水、校验审计链；
总览页顶部会在全量停止时亮红，系统状态卡显示执行层状态与当前域包。

```bash
curl /api/policy/holds                        # 看当前挂起与问题
curl -X POST /api/policy/holds/{id}/answer \
     -d '{"answer":"已确认在授权范围内","resume":true}'   # 明确答复后才恢复
```

### 3.5 接入逆向 / 审计工具（MCP 工具模板）

**系统 → MCP → 工具模板** 里预置了 9 个常用服务器，点"使用"会预填命令与参数，保存前可改：

| 类别 | 模板 | 说明 |
|---|---|---|
| 逆向 | radare2 MCP（MIT）、IDA MCP（idalib 无头）、IDA MCP（Hex-Rays 官方）、Ghidra MCP（无头）、ReVa | 只读反汇编/反编译、函数与 xref、结构体重命名；IDA 两个模板需商业授权（IDA 8.3+/9.4+） |
| 浏览器 | Playwright MCP、Chrome DevTools MCP | 前端挖掘（隐藏接口、鉴权绕过、客户端原型污染）与网络/性能取证；两者都不是安全边界，工具调用仍走 guard 审批 |
| 审计 | Semgrep MCP | 规则化 SAST、变体搜索 |
| 情报 | VirusTotal MCP（托管 http） | 样本/域名/IP 情报；哈希会外发，客户内部样本先确认授权 |

模板只做预填，**不替你决定命令**：这些工具自身在快速演进（IDA 的 GUI 插件路径已被官方弃用、
Ghidra/ReVa 的启动方式随版本变），每条模板都带安装方式与注意事项，接不通时按提示核对命令即可。
工具接进来后仍受 L1 判定约束（内联解释器、敏感文件读取、目标越界等），不是绕开策略的旁路。

### 3.6 离线分析：样本 / 固件 / 恶意代码（binary-re 域包）

逆向与病毒分析不做 HTTP 测试，红线也不同（不能把样本送外网、不能在业务主机上跑样本），
所以它是一套独立域包，而不是在线策略的参数微调：

```bash
cp policy/binary-re/deployment-context.example.yaml policy/binary-re/deployment-context.yaml
# 填：产物目录、情报源（VT/MB/OTX）、沙箱声明、授权时间窗
export ARTEX_ENGAGEMENT_FILE=./policy/binary-re/deployment-context.yaml
./artex                                # 启动日志会打印 pack=binary-re
```

与在线域的差异：出网只允许情报回源（其余全禁）；`wine`/`qemu` 等能在宿主机跑样本的工具默认禁用；
情报查询 200 次/任务、1 rps；送检（upload/submit/detonate）归 D 类需显式授权，未声明即拒绝。
`GET /api/policy/status` 的 `pack` 字段与 `/system/policy` 页面会显示当前用的是哪套域策略。
离线域包不需要录制代理即可启动（在线域没有代理直接拒绝启动）：录制默认关、可随时开，
`GET /api/policy/status` 的 `traffic_capture_required` 会说明当前域包的要求。

离线/本地域只守**宿主机边界**，不按在线作业边界高频拦截：

- **始终拒绝**：`rm -rf /`、`dd of=/dev/sda`、`mkfs`、`shutdown`、`chmod -R 777 /`（含藏在
  `python -c` 载荷里的同类动作）；直接执行 `scope.local_paths` 内的样本/被审计脚本；
  读 `~/.ssh/id_rsa`、`/etc/shadow` 这类宿主机凭据。
- **离线域放行**（`runtime.host_boundary`）：`python -c` 做一次性计算、样本里出现 `shadow`/`.env`
  字样（敏感判定只认路径形态）、命令连 `127.0.0.1` 本地辅助服务。
- 仍有边界在人工侧：经脚本/编码把产物外传，依赖 L2 出网白名单阻挡目的地。

详见 [`docs/redev/07-domain-packs.md`](docs/redev/07-domain-packs.md) §2.2。

### 3.7 源码审计与 0day 挖掘（source-audit 域包）

审计客户源码时用独立域包，授权范围是**目录清单**而不是域名：

```bash
cp policy/source-audit/deployment-context.example.yaml policy/source-audit/deployment-context.yaml
# 填：local_paths（只读副本目录）、产物目录、报告出口、授权时间窗
export ARTEX_ENGAGEMENT_FILE=./policy/source-audit/deployment-context.yaml
./artex                                # 启动日志会打印 pack=source-audit
```

- 默认**零出网**：审计工具（semgrep / Joern / ast-grep / rg / tree-sitter）本地跑，
  只有报告通道可用；需要拉规则/查 CVE 要显式加白名单。
- 被审计源码只读：原地改源码命中红线，补丁与 PoC 只能写进产物目录。
- `ssh`/`scp`/`rsync`/`nc`/`curl`/`wget` 等外传类命令默认禁用；`git push` 归 D 类需显式授权。
- 接 `semgrep mcp` / 本地 MCP 审计服务器见 3.5，工具调用仍走 guard 判定。
- **提交 0day 前必须过三道门**（漏洞详情 → 「准入」页录入，或直接调接口）：一份可复现的 PoC
  （≥2 次连续复现）、≥5 条反例、≥3 次跨 ≥2 类信息源的撞车比对；未过门的 finding 导出报告
  会被 409 拦下。规则见 [08](docs/redev/08-0day-pipeline.md)。
- **结论从哪来可回溯**：Worker 发现可疑点先用 `add_candidate` 登记候选（位置 + 入口→sink 的路径），
  平台逐跳核对——在线域每跳必须是真实抓到的流量 id，离线域必须是授权目录清单内的源码位置（行号有效）——
  再算可达性；核对不过只降级显示、不阻断。之后 `report_finding` 带 `candidate_id` 转为结论，
  任务页「候选」Tab 能看到每条结论的证据链。
- **撞车比对可以让平台代检（命中条目落库后仍需人工复核并留下复核人/依据，未复核会阻断导出）**：「准入」页可一次填最多 5 条查询，平台真的请求 NVD 与 CISA KEV，
  把命中的公开条目（编号 + 标题 + 链接）落库并标注「平台代检」；是否同一个漏洞仍由人复核后勾选。
  检索失败不会记成"没撞车"（查不动 ≠ 没重复）。
- **PoC 可以让平台代跑**：「准入」页填入 `expect_status`（可选 `expect_body_contains`）后点「平台重放」，
  平台会经录制代理真实发包——仍受范围/语义/预算判定，判不过的请求不会到达目标——并把复现次数按
  机器实测抬高、用真实流量 id 回填证据。`command`/`file`/`sample` 涉及在宿主机执行代码，平台不代跑。

### 3.8 样本分诊（malware-triage 域包）

批量钓鱼/勒索样本的第一小时：不执行样本，只做"是什么、什么家族、什么能力、IOC 清单"。

```bash
cp policy/malware-triage/deployment-context.example.yaml policy/malware-triage/deployment-context.yaml
export ARTEX_ENGAGEMENT_FILE=./policy/malware-triage/deployment-context.yaml
./artex                                # 启动日志会打印 pack=malware-triage
```

- **一律不执行样本**（`R13 execute_sample_at_all`）：需要动态行为请换 `binary-re` 并走沙箱审批。
- 出网只允许情报回源；样本本体不得上传未声明的第三方服务（`R12`）。
- 分诊工具（file/hash/strings/exiftool/olevbа/capa/YARA/FLOSS/diec）默认可用；
  `wine`/`qemu`/`gdb`/`strace` 默认禁用。
- 预算更紧：情报查询 100 次/任务（批量分诊时每个样本都要省着查）。

### 3.9 在线侦察：赏金项目只看不动（bounty-recon 域包）

赏金/众测的日常是"先测绘、后打点"：子域、JS、接口、变化监控。侦察域把这段工作从
`web-pentest` 里分出来，用更紧的读写比与更低的速率，避免"探一探"变成扫描。

```bash
cp policy/bounty-recon/deployment-context.example.yaml policy/bounty-recon/deployment-context.yaml
# 填 program scope（domains 支持 *.example.com 通配）、授权窗口、报告通道
export ARTEX_ENGAGEMENT_FILE=./policy/bounty-recon/deployment-context.yaml
./artex                                # 启动日志会打印 pack=bounty-recon
```

- **只看不动**：不申请测试账号，C/D/E 类（写）动作在语义层没有合法通道，直接拒；
  预算里 `vuln_samples`、`send_actions` 都是 0。
- **公开情报源只读**：`crt.sh` / `urlscan.io` / `otx.alienvault.com` 在 egress 白名单里，
  只放行 GET/HEAD/OPTIONS（判定规则 `R8_intel_read`）；向其 POST/写入直接拒（`R8_egress_write`）。
- **更慢的读**：默认 4000 次/任务、3 rps、并发 2；扫描器（nuclei/nmap/masscan/zmap…）默认禁用。
- **通配授权**：`*.example.com` 按 scope 规则匹配，归属不明仍按范围外、必要时全量停止。

### 4. 锁定出网（L2，强烈建议）

只靠代理挡不住 `nmap`/裸 TCP。把容器出口收口到唯一代理：

```bash
docker compose -f docker-compose.yml -f deploy/egress-lockdown/docker-compose.egress.yml up -d
```

验收命令与原理见 [`deploy/egress-lockdown/README.md`](deploy/egress-lockdown/README.md)。

## 目录结构

```
agent/       Agent 运行时：目标拆解 → 规划 → 执行 → 复测
policy/      规范执行层：范围/语义分级/预算/命令/响应检查/审计（纯 Go，可单测）
             web-pentest/  在线测试域包（授权范围/测试账号/扫描器审批）
             binary-re/    离线二进制分析域包（情报回源白名单/禁宿主模拟器/送检审批）
             source-audit/ 源码审计域包（目录清单授权/零出网/禁外传命令）
             malware-triage/ 样本分诊域包（一律不执行样本/情报回源/批量分诊预算）
             patterns/secret.txt   敏感特征（RE2）
traffic/     录制代理（mitmproxy）+ L3 判定出口
guard/       工具调用前置钩子（L1）
intercept/   可配置拦截规则 + 人工审批
db/          PostgreSQL（schema.sql 幂等迁移）
server/      HTTP API / 任务引擎 / MCP 编排 / 通知 / 策略 API
web/         Next.js 前端
deploy/      部署补充（egress-lockdown = L2 出网强制）
docs/redev/  设计与决策文档（必读）
skills/      内置 skill
```

## 合规与边界

- **许可证**：AGPL-3.0（见 [`LICENSE`](LICENSE)）。修改后分发、或通过网络提供服务，须按 §5/§13
  提供完整对应源码并保留版权声明；本仓库不提供闭源商用授权。
- **允许用途**：**仅限获得明确书面授权的资产**，或本地隔离环境中的研究与样本分析。
- **明确不做**：免杀/规避检测、反取证、无人工确认的自动化利用、"输入目标列表即自动出洞"、
  大规模凭据窃取与数据外传。这些既是上游被滥用的核心机制，也会让项目无法辩护。
- **不提供担保**：按现状提供，使用者自负全部法律责任。
- **上游附加条款**：上游 README 声明"禁止任何实际测试（含授权资产）"，与本 fork 的授权测试定位
  存在张力；AGPL 本身不限制用途，但请在动手前自行完成法律评估。

## 维护

- 分支：`main` 保持可构建、可测试；功能在 `feat/*` 分支开发后合入。
- 提交规范：`type(scope): summary`（feat/fix/refactor/docs/test/chore/security）。
- 每个安全相关改动**必须带回归测试**；策略层改动还要补合规矩阵用例。
- **每次提交都要更新 README「进展与计划」**（当前状态 / 里程碑 / 下一步），保证文档不是过时叙事。
- 提交前跑：`go build ./... && go vet ./... && go test ./...`（需要 PostgreSQL；CI 的串行策略与
  已知 flake 清单见 [`docs/redev/06-ci.md`](docs/redev/06-ci.md)）。
- 安全问题请走私密渠道（见 [`SECURITY.md`](SECURITY.md)），不要公开提 issue。

## 致谢

上游 [ARTEX](https://github.com/Autumn-27/ARTEX) 作者 Autumn-27，以及 ScopeSentry、norma 等
上游组件；设计参考了 AIxCC 参赛系统、Strix、Google Big Sleep / Naptime 等公开工作（见
[`docs/redev/02-tooling-survey.md`](docs/redev/02-tooling-survey.md)）。
