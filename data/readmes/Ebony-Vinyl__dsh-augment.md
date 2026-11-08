<p align="center">
  <img src="assets/logo.svg" width="88" alt="dsh augment logo">
</p>

<h1 align="center">dsh augment</h1>

<p align="center">
  <a href="https://github.com/Ebony-Vinyl/dsh-augment/blob/main/LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-263146?style=flat-square"></a>
  <img alt="Status" src="https://img.shields.io/badge/status-0.0.1%20preview-7da1de?style=flat-square">
  <img alt="DSH" src="https://img.shields.io/badge/DSH-0.2.x-4b6fff?style=flat-square">
  <a href="https://github.com/Ebony-Vinyl/dsh-augment/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/Ebony-Vinyl/dsh-augment?style=flat-square&color=4b6fff"></a>
</p>

<p align="center">
  <strong>自适应驾驭层：Token 压缩 + 证据驱动的自我进化，为 DeepSeek Harness 桌面端设计。</strong>
</p>

> 0.0.1 预览版：在不改模型权重的前提下，把工具输出压小、把重复读取折叠、把省下的 token 摊开给你看；同时让提示词、记忆、技能、工具指导、子代理、脚本和模型路由持续进化。
>
> 所有数据只保存在本机 `~/.dsh/dsh-augment`，没有遥测；实时进化只调用你在 DSH 中配置的模型 provider。

## Preview

<p align="center">
  <img src="docs/preview-context.png" alt="dsh augment 上下文优化面板" width="760">
</p>

## Highlights

- **Token 账本** — 按请求对比“原本输入 vs 实际输入”，叠加缓存加权等效节省。
- **输出压缩** — 10+ 纯函数过滤器，`never_worse` 守卫，read 默认保护。
- **CCR 取回** — 省略的原文落盘 7 天，footer 带 id，`augment_retrieve` 分页取回。
- **read 同名替换** — 作用域覆盖官方 read，保留沙箱与 `fs/observed`，重复读取折叠。
- **上下文增强** — 项目地图、环境经验、循环防护；只注入高信号内容。
- **工具 schema 开销** — 每个请求 7.7K–18K tokens 的工具定义成本（取决于 preset），按工具 + 使用次数展示，未使用标红。
- **自我进化** — 8 个可进化组件、Propose–Probe–Compose、证据门、审计与一键回滚。
- **零原生依赖** — 纯 JS 运行时，不打包 bash/MSYS，不隐藏官方工具，不发网络请求。

## Quick Start

```bash
git clone https://github.com/Ebony-Vinyl/dsh-augment.git
cd dsh-augment
node scripts/install.mjs
```

重启 DeepSeek Harness，打开 **设置 → dsh augment**。

- 需要 `pnpm` 在 PATH 中；或设置 `DSH_PNPM` 指向 `pnpm.mjs`。
- 如果使用桌面端自带 pnpm：设置 `DSH_APP_ROOT` 为 DeepSeek Harness 安装目录。
- 卸载：`node scripts/uninstall.mjs`；急救：创建 `~/.dsh/dsh-augment/DISABLED`。

## 0.0.1 预览版：自我进化

- **双层递归**：任务级 Propose–Probe–Compose + 改进级算子 bandit / improver 元进化。
- **候选算子**：GEPA 反思编辑、PPC 通用/领域候选、ACE lesson、OPRO、APE、AWM、SkillOpt、TRACE、routing。
- **Capability Gym**：12 个确定性任务模板 × 24 个 held-out 变体，覆盖工具选择、上下文检索、错误恢复、指令遵循、记忆召回、规划、代码修复与 token 效率。
- **证据优先**：四臂对比（baseline / equal-compute / full-rsi / reuse-only）、配对 bootstrap、Bonferroni、回归门；没有正向 CI 下界不采纳。
- **持续学习**：带证据、作用域、置信度和版本谱系的 lesson / skill / memory / subagent / routing；按 token 预算排序注入。
- **任务内自修复**：工具失败时注入有界修复提示，不注入停止/完成指令。
- **可视化工作区**：总览、工作台、经验库、评测中心、组件、记忆、设置 7 个页签；SSE 实时更新；手写 SVG 图表。
- **安全**：生成代码只在 worker+vm 沙箱运行、默认不自动执行；secrets/注入检测；审计与一键回滚。

详见 [EVOLUTION.md](EVOLUTION.md)、[EVOLUTION-REPORT.md](EVOLUTION-REPORT.md) 和 [ATTRIBUTION.md](ATTRIBUTION.md)。

**实时模型**：默认使用 DSH 已配置的 `agnes / agnes-3.0-flash`（OpenAI 兼容，`https://api.agnes-ai.cn/v1`，免费）。可在“自我进化 → 设置 → 模型路由”中修改 executor / improver / selector / judge。

---

## 功能

### 1. 输出压缩

对 `bash` / `pwsh` / `grep` / `glob` 等工具输出应用纯函数压缩：

- ANSI / OSC 清理、进度行折叠；
- 连续重复行折叠（≥3 行 → `[xN]`）；
- grep 结果按文件分组；
- JSON 精简 / 大 JSON 骨架化；
- git diff 压缩（去掉 `index` 行、折叠长上下文）；
- HTML → 文本（去脚本 / 样式 / 标签）；
- base64 / 长 hex 省略；
- 按形状（日志 / 代码 / 散文 / JSON）做头尾窗口裁剪；
- `never_worse` 守卫：压缩后不更小就返回原文；
- 小于 512 字符不处理；输入上限 2MB；单行上限 2000 字符；
- **read 默认不做有损压缩**（回读成本高于节省）；
- 每个有损输出都带机器可读 footer，例如：

```text
[dsh augment: tech=cap 5000→220 lines, ~7800→~3629 tokens, saved 4171, id="c-0c3ed7e1d3da"]
```

### 2. 大结果外置（CCR）+ 取回

被裁剪的原文按内容 hash 存到 `~/.dsh/dsh-augment/store`（gzip，7 天，200MB 上限，LRU 清理）。footer 里的 `id` 可用 `augment_retrieve` 工具分页取回：

```text
augment_retrieve({ id: "c-0c3ed7e1d3da", offset: 0, limit: 8192 })
```

检测到私钥、密码、API key 形态的内容不会落盘；这类内容只做无损压缩。

### 3. read 工具替换

在 agent 作用域注册同名 `read`，利用 DSH 的 “scoped tools shadow globals” 覆盖官方 read：

- 参数与官方一致：`file_path`、`offset`、`limit`；
- 走 `ctx.fs`，保留宿主沙箱、工作区边界和 `fs/observed`（read-before-edit 依赖它）；
- 输出更紧凑：`<path>…</path> lines a-b/n` + `N|text`；
- 同一文件、同一范围、同一 `version` 重复读取时返回引用，不返回全文；
- 单次输出 200KB 上限，超出提示下一个 `offset`；
- 注册失败或 `ctx.fs` 不可用时自动跳过，官方 read 原样保留。

`glob` / `grep` 保留官方实现：它们已经是 ripgrep + 上限 + 落盘，直接替换没有净 token 收益，还会绕过宿主的 subprocess 沙箱；它们的输出由压缩流水线处理。

### 4. 仓库地图

`agent/created` 后台扫描 session cwd：项目类型、包管理器、脚本、框架、两层目录树、import 入度最高的文件、入口文件、测试命令、`.env.example` 变量名（只读变量名）。

- 渲染为 ≤700 tokens 的紧凑 Markdown；
- 按 repo 路径 + git HEAD + package.json mtime 缓存；
- 注入 agent 作用域的 system prompt section（order 3300），每个 session 首次请求后锁定文本，避免中途改动破坏 KV cache；
- `augment_map` 工具按 `summary|tree|hot|entry|tests|env|all` 或关键词取细节。

### 5. 环境经验

按 repo 记录“已验证命令”和“命令修复”：

- 成功执行的测试 / 构建 / lint 命令，≥2 次才成为事实；
- `pytest` 失败、`python -m pytest` 成功这类修复，≥2 次成功且无近期反证；
- 最多 4 条、150 tokens，注入系统提示；
- 存储 `~/.dsh/dsh-augment/facts`，设置页可查看 / 清空。

### 6. 循环防护

按 agent 记录最近工具调用（名称、参数 hash、错误签名）。同一工具 + 同一错误签名在最近 10 次调用中出现 ≥3 次，且 10 次内未提示过，就通过 `additionalContexts` 注入一次约 60 tokens 的纠偏提示。绝不注入停止 / 完成类指令。

### 7. Token 账本

**测量口径：**

- 实际输入：provider `usage.inputTokens + cacheReadTokens + cacheWriteTokens`；
- 原本输入：实际输入 + 当前请求消息里所有 footer 的 `saved` 之和 − 注入成本；
- 注入成本：系统提示上下文段 + `augment_retrieve` / `augment_map` schema + 循环防护提示；
- 净节省 = 原本 − 实际；
- 压缩结果会留在历史里，后续每个请求都会重复计入节省，所以这是真实的累计效果；
- 输出 tokens 单独展示，不冒充节省；缓存命中率单独展示；
- 缓存加权等效：按 input 1× / cache-read 0.1× / cache-write 1.25× / output 5× 折算，并且**对原本输入使用与实际输入相同的缓存比例**，避免把 provider 的缓存折扣全部算成插件的功劳；
- 没有 provider usage 时回退本地估算，并标注“估算”。

### 8. 设置页

注册到 `settings.section`（id `dsh-augment`，order 72，label `dsh augment`）：

- **总览**：累计净节省、节省率、实际输入、缓存命中；最近 30 次请求双柱图；节省来源；按工具；**工具 schema 开销**；健康状态；最近压缩事件；
- **设置**：总开关、压缩阈值、CCR、重复折叠、read 替换、项目地图、环境经验、循环防护；
- **压缩实验室**：粘贴一段工具输出，立即看到 before / after / 节省率，不落盘、不影响真实会话。

“工具 schema 开销”是本预览版新增的透明面板：它把每个请求都要付的工具定义成本按工具列出来（本机实测 **7.7K–18K tokens / 请求，取决于 preset**），并标注每个工具在本机账本里的使用次数；未使用的工具会标红。它**不隐藏任何工具**，你可以据此关闭不需要的插件或工具，而不是让插件替你猜。

---

## 自我进化工作区

设置页顶部有“上下文优化 / 自我进化”双模式。自我进化包含 7 个页签：

1. **总览**：能力指数、相对基线、经验库、累计净节省；能力趋势（含 95% CI 带）、Pareto 前沿、组件雷达、最近运行、实时活动；没有运行时显示“第一次使用”引导。
2. **工作台**：模拟/实时、k、开发集/held-out 任务数、自动采纳；阶段时间线（base → inv/dom → compose → select → reflect → validate）；候选盲评、diff、采纳/回滚；运行历史。
3. **经验库**：搜索/类型/状态过滤；证据、置信度、复用次数、作用域、版本谱系；采纳/验证/冻结/归档/解冻；知识图谱。
4. **评测中心**：Capability Gym 套件、四臂对比、任务×臂热力图、CI、Pareto、回归、协议指纹；导出 JSON。
5. **组件**：8 个 harness 组件卡片、预览、编辑器、diff、版本时间线、采纳/回滚。
6. **记忆**：注入预览、预算、学习策略、经验构成、模型路由表。
7. **设置**：触发器、预算、验证门、学习、模型路由、安全/保留、导入导出/清理。

HTTP/SSE：

- `GET /plugins/dsh-augment/evolution/snapshot?light=1`
- `GET /plugins/dsh-augment/evolution/runs/:id`
- `GET /plugins/dsh-augment/evolution/versions/:id`
- `POST /plugins/dsh-augment/evolution/actions`
- `POST /plugins/dsh-augment/evolution/benchmark`
- `GET /plugins/dsh-augment/evolution/events?token=...`（SSE）
- `GET /plugins/dsh-augment/evolution/export`
- `GET /plugins/dsh-augment/evolution/library|evaluations|gym`

工具：`augment_evolve`、`augment_recall`、`augment_skill`。命令：`/evolve`、`/recall`、`/benchmark`。

数据目录：`~/.dsh/dsh-augment/evolution/`（runs、versions、experiences.json、evaluations、reports、audit.jsonl）。

### 评测协议

- **四臂**：`baseline`、`equal-compute`、`full-rsi`、`reuse-only`。
- **评分**：0–1；失败/未评分不按 0 插补。
- **统计**：按任务配对，任务级 percentile bootstrap（默认 10,000 次，seed 42），95% CI；两个主比较用 Bonferroni 校正。
- **采纳门**：CI 下界 > 0、无任务回归超过 5%、无安全违规、证据完整；否则状态为 `no-gain` / `incomplete`，不采纳。
- **防脆性**：held-out 与 dev 分离；评测集不进入反思上下文；编辑预算；多次重复；选择器盲评。

### 安全与回滚

- 生成代码只在 `worker_threads + vm` 沙箱运行：无 `require`、无 `process`、无 fs/网络、1s 超时、输出 ≤1MB；默认关闭自动执行，需 UI 批准。
- 所有反思/经验文本过 secret 检测、控制字符/双向覆盖检测、prompt injection 检测；失败则拒绝。
- 不把评测集/隐藏 grader 放进反思上下文。
- 破坏性命令在 probe 中默认阻断；需要显式批准。
- 所有采纳/回滚/冻结写 `audit.jsonl`；任何版本可一键回滚。
- 数据保留：默认 30 天，按大小/条数 LRU；一键导出/重置。

---

## 安装

要求：DeepSeek Harness 桌面端 0.2.1-rc.2 ~ 0.2.1-rc.5（`engines.dsh: >=0.2.0-rc.2 <0.3.0-0`；本版本在 0.2.1-rc.5 上实测），Windows / macOS / Linux。

1. 关闭 DeepSeek Harness。
2. 在本目录运行：

```bash
node scripts/install.mjs
```

脚本会：

- 备份 `~/.dsh/profiles/desktop/package.json`、`cordis.patch.yml`、`pnpm-lock.yaml` 到 `~/.dsh/dsh-augment/backup/<时间>/`；
- 添加 `"dsh-augment": "link:<插件目录>"`；
- 把 `dsh-augment` 加入 `dsh.profile.bundles`；
- 用 pnpm 安装（可用 `DSH_PNPM` / `DSH_APP_ROOT` 指定桌面端自带 pnpm）。

3. 启动 DeepSeek Harness，打开 **设置 → dsh augment**。

卸载：

```bash
node scripts/uninstall.mjs
# 或从最近一次备份恢复：
node scripts/uninstall.mjs --restore
```

启动故障急救：创建 `%USERPROFILE%\.dsh\dsh-augment\DISABLED`（或 `~/.dsh/dsh-augment/DISABLED`），插件会直接跳过加载。删除该文件即可恢复。

---

## CLI

不需要启动桌面端也能查看账本、压缩文件和生成仓库地图：

```bash
node scripts/augment.mjs stats
node scripts/augment.mjs config
node scripts/augment.mjs compress <file> [--out <file>]
node scripts/augment.mjs map [root]
node scripts/augment.mjs reset --yes
node scripts/augment.mjs export [file]
```

`compress` 使用与插件完全相同的压缩流水线；`stats` 读取同一份 `~/.dsh/dsh-augment/stats.json`。

## 性能

dsh augment 不在模型请求前做重活；唯一的 CPU 路径是工具结果返回后的压缩，且有上限和快速路径。

| 场景 | 实测 |
|---|---|
| 100KB 日志 | 9.5–11 ms |
| 1MB 日志 | ~10 ms（先裁剪再处理） |
| 2MB 日志（输入上限） | 19–21 ms |
| 100KB git diff | 5.2–5.7 ms |
| 100KB HTML | 15.5–16.1 ms |
| 154KB JSON | 2.8–2.9 ms |
| 2MB token 估算 | 3.1 ms/次 |
| CCR 异步写入 2MB | 39–48 ms（事件循环不被阻塞） |
| CCR 取回一页 | 15 ms |
| 仓库地图 500 文件 | 50–130 ms（后台，3s 预算） |

设计保证：

- 压缩在 `tools/post-execute` 里、工具结果之后运行；输入上限 2MB；大日志先 cap 再处理，避免全量多遍扫描。
- CCR 的 gzip / 写盘 / 读盘全部异步，不阻塞宿主事件循环。
- `llm/stream` 只观察 chunk，账本在流结束后才计算；普通消息用 `includes` 快速跳过，不做正则/估算。
- 仓库地图后台构建，walk 3s / hot files 1.5s / env 1s 预算；不阻塞会话创建。
- 所有状态按 agent/session 隔离，无全局锁、无跨会话串行链。
- 账本只保留 200 条请求 / 2000 条事件的紧凑行；`/stats` 只返回最近 60 条请求 + 80 条事件，不把每条请求的 schema 数组重复发给前端。
- 不增加模型调用、不改写流、不包 fetch、不发网络请求。
- 系统提示注入段是稳定的，命中 KV cache；账本把它作为注入成本扣除，净节省仍为正。

## 隐私与存储

| 数据 | 位置 | 说明 |
|---|---|---|
| 配置 | `~/.dsh/dsh-augment/config.json` | 原子写 |
| 账本 | `~/.dsh/dsh-augment/stats.json` | 最近 200 请求 / 2000 事件 |
| CCR 原文 | `~/.dsh/dsh-augment/store/*.gz` | 7 天，200MB 上限，敏感内容不落盘 |
| 仓库地图 | `~/.dsh/dsh-augment/repos/` | 按 repo + HEAD 缓存 |
| 环境经验 | `~/.dsh/dsh-augment/facts/` | 每 repo 最多 50 条 |
| 进化运行 | `~/.dsh/dsh-augment/evolution/runs/` | 运行记录、阶段、候选 |
| 版本 | `~/.dsh/dsh-augment/evolution/versions/` | 采纳/回滚的 harness 版本 |
| 经验库 | `~/.dsh/dsh-augment/evolution/experiences.json` | 带证据/作用域/谱系 |
| 评测 | `~/.dsh/dsh-augment/evolution/evaluations/` | 四臂报告、CI、热力图数据 |
| 审计 | `~/.dsh/dsh-augment/evolution/audit.jsonl` | 采纳/回滚/冻结 |

v1 的压缩/账本功能没有任何网络请求。v2 的实时进化会通过宿主 `ctx.llm` 调用你在 DSH 中配置的模型 provider（默认 `agnes-3.0-flash`）；不会向其他服务发送数据，也不会自动上传经验或轨迹。

---

## 设计取舍

- **不隐藏官方工具**：`read` 用同名作用域覆盖，注册失败自动回退；`glob` / `grep` 保留官方 ripgrep 实现，只压缩输出。
- **不做全量 system prompt assemble 探测**，不引入原生二进制，不打包 bash/MSYS。
- **工具 schema 成本只展示不隐藏**：你能看到每个请求 7.7K–18K tokens 的工具定义开销和使用次数，再决定关掉哪些插件/工具。
- **所有有损输出都可取回**：footer 带 id，CCR 原文本机保留 7 天。

## 已知限制

- token 数是本地估算（CJK 感知）；只有 provider 上报的 `usage` 是计费真值。
- read 替换只在 `ctx.fs` 可用时注册；不可用时官方 read 保留。
- 设置里的 read 替换开关对**新会话**生效；已有会话的 scoped 注册会保留到 agent 销毁。
- `glob` / `grep` 保留官方实现，只压缩输出。
- 环境经验和 shell 输出压缩依赖可用的 workspace 沙箱；如果宿主报 `grantWrite(...)` / ACL 错误，属于宿主 sandbox 问题，不是本插件。
- 宿主 API 在 0.2.x 内仍可能漂移；插件对可选服务做了 `ctx.get` 探测和 try/catch 降级。
- 如果输入框底部出现红色的“选择未能同步，请重试或重新加载插件”，那是 **EAC design world** 的本地模板服务（`127.0.0.1:4173`）未启动，与本插件无关；启动 EAC 模板服务或禁用 EAC 插件即可消失。

---

## 开发

```bash
npm test                          # node --test，59 个用例（含 7 页签 SSR、HTTP/SSE、host 注入）
npm run build:client              # esbuild 打包 lib/client/ → lib/client.js
node scripts/evolution-smoke.mjs  # 模拟进化 + held-out 验证，写出 docs/evolution-simulated.*
```

目录：

```
lib/index.js              Host 半：压缩 hook / 账本 / 进化服务接线
lib/evolution/            自我进化：config / store / harness / engine / evaluate /
                          learning / policy / meta / bridge / sandbox / routes / gym
lib/client/               Browser 半源码：shell / context / evolution 7 页签 / charts / ui
lib/client.js             构建产物（发布包已包含）
lib/pipeline.js           压缩流水线
lib/filters.js            纯函数过滤器
lib/ledger.js             请求级账本
lib/ccr.js                大结果外置
lib/read-tool.js          read 同名覆盖
lib/repo-map.js           仓库地图
lib/env-facts.js          环境经验
lib/loop-guard.js         循环防护
lib/http.js               /plugins/dsh-augment/*
scripts/install.mjs       / uninstall.mjs
scripts/augment.mjs       CLI：stats / config / compress / map / reset / export
scripts/build-client.mjs  客户端构建
scripts/evolution-smoke.mjs 模拟进化验证
scripts/save-simulated-harness.mjs 把模拟 harness 保存为候选版本
test/*.test.mjs           59 个用例
docs/evolution-simulated.md 模拟验证报告
```

## Acknowledgments

自我进化层的思想来源见 [ATTRIBUTION.md](ATTRIBUTION.md)。

## License

MIT
