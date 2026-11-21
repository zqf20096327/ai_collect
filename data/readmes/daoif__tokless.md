<p align="left">
  <img src="./assets/logo.svg" width="60" height="60" alt="Tokless Logo" />
</p>

# Tokless

[![License: MIT](https://img.shields.io/badge/License-MIT-18181B.svg)](./LICENSE)
[![Node.js >= 18](https://img.shields.io/badge/Node.js-%3E%3D18.0.0-10B981.svg)](./package.json)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-18181B.svg)](./package.json)

简体中文 | [English](./README.en.md)

> **核心初心：在不损失一行代码排查与修复质量的前提下，把 AI 编程工具里无意义的盲读膨胀与滚雪球 Token 消耗砍到最低。**

**面向主流 AI 编程 Agent（原生支持 Google Antigravity、Claude Code、Codex CLI，开放 `targets/` 插件架构扩展更多工具）的纯 Node.js 零依赖省流套件——毫秒级 `[L起-L止]` 语法骨架导航、原生 `PreToolUse` 防盲读硬刹车、剥离 MCP 空载税的净身角色与 0 Token 本地账单/缓存断层体检。**

在真实跨语言生产工程（Tauri + Rust + React）的严格 A/B 盲测中，启用 `tokless` 后单次任务减少 **34.4% 模型往返轮次**、砍掉 **53.2% 总 Token 吞吐（净省 1,138 万 Token）**、滚雪球 Cache Read 净省 **53.8%（少烧 1,123 万 Token）**，7 个真实深层 Bug 检出与修复质量零折损（*注：该组盲测数据完成于早期 `v0.1.0` 版本，当时仅含基础语法骨架与无行号盲读拦截，尚未针对后续新增净身角色与优化行号放行机制的新版本重跑完整长任务对照，当前版本理论综合省流表现更强*）。

---

## 一行命令极速启用（零界面 · 纯 Node.js `>=18` 零外部依赖）

### 方式一：终端一键挂载（推荐）

自动检测并挂载本机已安装的 Antigravity、Claude Code（`~/.claude`）与 Codex CLI（`~/.codex`），从 `npx` 临时目录运行时会自动切换为实体文件拷贝，杜绝缓存清理后软链悬空：

```bash
npx tokless install
```

按需指定单个或全部目标宿主 / 一键干净卸载：

```bash
npx tokless install --target agy       # 仅挂载 Google Antigravity
npx tokless install --target claude    # 仅无损合并 Claude Code ~/.claude/settings.json 钩子与技能
npx tokless install --target codex     # 仅安装 Codex CLI ~/.codex/skills/code-skeleton
npx tokless install --target all       # 挂载全部已支持宿主
npx tokless uninstall --target all     # 一键卸载并还原原有宿主配置
```

### 方式二：复制一句话直接交给你的 AI 编程助手

不想自己切终端，直接把下面这句话发给 Antigravity 或 Claude Code 对话框即可：

```text
请运行 npx tokless install 帮我安装启用 tokless 省流套件（若网络受限可克隆 https://github.com/daoif/tokless 后运行 node install.js），装好后帮我确认钩子与技能已生效。
```

### 方式三：源码克隆本地安装（适合二次开发或离线环境）

```bash
git clone https://github.com/daoif/tokless.git
cd tokless
node install.js
```

---

## 为什么你的周额度掉得这么快？有了 `@Codebase` 或 `repomix` 为什么还是拦不住？

很多重度 AI 编程玩家都有同一个困惑：**“IDE 明明自带了 `@Codebase` 语义索引，我也试过 `repomix`，为什么跑几个复杂需求，5 小时窗口和周额度还是见底了？”**

通过对数十份底层会话账单日志（`transcript_full.jsonl`）的逐帧解剖，吃光额度的元凶非常清晰：

### 1. `@Codebase` 是找线索的「搜索引擎」，`tokless` 是防偷懒的「省流刹车系统」

| 工具类型 | 代表工具 | 核心职责 | 为什么单靠它省不了 Agent 循环里的额度？ |
| :--- | :--- | :--- | :--- |
| **语义搜索引擎** | IDE 自带 `@Codebase` | 向量/关键词检索，帮 AI 找到“大概在哪个文件” | **只管找路，不管怎么读**。AI 拿到文件名后，下一步依然习惯性调用无行号的 `read_file` / `Read`，顺手把整份一两千行源码全量塞进上下文。 |
| **全仓打包器** | `repomix` / `gitingest` | 把整个仓库压成单文件喂给网页聊天框 | 适合无本地工具权限的网页问答；若塞进本地 Agent 会话，相当于第 1 步直接背上几万 Token 包袱。 |
| **省流导航与硬刹车** | **`tokless`** | **80ms 零索引出 `[L起-L止]` 骨架 + `PreToolUse` 硬拦盲读** | 当 AI 偷懒盲读 >200 行代码文件（或传 `1~文件末尾` 假切片）时，底层钩子当场拦截并直接甩回该文件的函数/类 `[L起-L止]` 行号骨架，逼它按行号精准切片读取。 |

`tokless` 与 `@Codebase` 完全不冲突，而是天然互补：`@Codebase` 负责回答“去哪几个文件找”，`tokless` 负责在读取那一刻踩住刹车，只让真正要改的那几十行代码进入上下文。

### 2. 「Cache Read 滚雪球效应」与上下文自动压缩水位

在多步 Agent 循环中，真正烧光额度的往往不是单次 `Input`，而是每一步反复重读历史上下文的 **`Cache Read`**：

$$\text{累计 Cache Read} \approx \text{平均上下文水位} \times \text{模型调用轮数}$$

- **早一步塞进废话，步步交复利税**：如果第 3 步盲读塞进 3 万 Token 无关代码，整个任务跑了 50 轮，这 3 万 Token 就会在后续每一步被重复计费 47 次，单这一步就白烧 **140 万+ Cache Read Token**。
- **远离隐式压缩失忆线**：在 Antigravity 等宿主中，三代模型常见在约 **256K** 上下文水位触发底层强制摘要压缩（`CHECKPOINT: # Resuming from a compaction`，将数十万上下文压成几千字摘要导致细节丢失与反复重读）；四代模型实测跑上 440K 未触发压缩（社区普遍推测阈值约 **512K**）。但无论压缩上限在哪，**压低每步水位 + 减少探索轮数**都是同时保住代码记忆精度与周额度的核心解法。

---

## 真实工程 A/B 实测账单（Tauri + Rust + React 全仓找 Bug 与修复）

在同一个生产级桌面工程（Rust 后端 + TypeScript/React 前端）上，基于同一 Git Commit (`3908815`) 切出两个独立 Worktree，由同一模型（`Gemini 4 Hydrogen High`）执行完全相同的全仓深层 Bug 排查、修复与编译验证任务：

| 对比维度 | 对照组 (原生常规模式) | 实验组 (启用 `tokless`) | 真实节省 / 提升 |
| :--- | :--- | :--- | :--- |
| **总 Token 吞吐 (`input + cache_read + output`)** | 21,410,381 (2,141 万) | **10,029,592 (1,003 万)** | **净省 53.2% (-1,138 万 Tokens)** |
| **累计 Cache Read（滚雪球缓存消耗）** | 20,858,589 (2,086 万) | **9,627,700 (963 万)** | **净省 53.8% (-1,123 万 Tokens)** |
| **累计 Input Tokens（新增输入）** | 494,886 | **352,020** | **省 28.9%** |
| **模型调用轮数（Planner Invocations）** | 64 次 | **42 次** | **少跑 34.4% 轮次** |
| **总执行步数（Steps）** | 220 步 | **150 步** | **少走 31.8% 弯路** |
| **`read_file` 调用次数（全量盲读次数）** | 79 次（含 3 次全量盲读） | **51 次（0 次盲读）** | **文件读取减少 35.4%** |
| **峰值上下文水位（Peak Context）** | 439,830 Tokens | **323,344 Tokens** | **峰值降低 26.5%** |
| **定位首个 Bug 开始改代码耗时** | 227 秒（第 115 步） | **196 秒（第 81 步）** | **提速 31 秒 / 少花 34 步** |
| **检出并修复的真实硬核 Bug 数** | 7 个（全部编译通过） | **7 个（全部编译通过）** | **0 质量损耗（并发细节更深）** |

> **实测版本与模型说明**：
> 1. **测试版本背景（`v0.1.0` 基线）**：上表 A/B 盲测数据完成于早期的 `v0.1.0` 版本（当时仅包含基础语法骨架提取与无行号盲读拦截），目前尚未针对新版本重跑完整长任务对照；随着后续版本加入剥离外部 MCP 空载税的净身角色（`inheritMcp: false`）与优化后的行号切片放行机制，当前版本的理论综合省流表现更强。
> 2. **压缩阈值参考**：本轮实测基于四代模型，对照组峰值达 439,830 Tokens 未触发自动压缩（若换作 256K 阈值的三代模型早已触发强制压缩失忆）。完整逐项对比见 [benchmarks/real-world-bugfix-case.md](./benchmarks/real-world-bugfix-case.md) 与静态骨架基准测试 [benchmarks/static-skeleton-benchmark.md](./benchmarks/static-skeleton-benchmark.md)。

---

## 四大核心能力与全平台支持边界（v0.4.1）

`tokless` 把「跨所有 AI 编程工具通用的省流内核」与「特定客户端的深度钩子/日志解析」拆得清清楚楚，绝不混为一谈：

| 宿主工具 | 1. `tokless skeleton` 语法骨架 + `AGENTS.md` 规范 | 2. `PreToolUse` 防盲读硬刹车 | 3. 净身子角色 (`inheritMcp: false`) | 4. `tokless audit` 体检仪 |
| :--- | :---: | :---: | :---: | :---: |
| **能力通用边界** | **100% 所有 AI 编程工具通用** | **可扩展钩子机制（已打通 Antigravity / Claude Code）** | **Antigravity 插件专用** | **`audit project` 跨端通用；`session / compare` 属 Antigravity 专用** |
| **Google Antigravity** | 原生 Skill + CLI + `rules/AGENTS.md` | 原生 `hooks.json` (`read_file` / `view_file`) | `tokless-coder` / `tokless-reviewer` | 全功能支持（`project` + `session` / `compare`） |
| **Claude Code** | `~/.claude/skills` + CLI | 无损合并 `~/.claude/settings.json` (`Read`) | — | 支持 `audit project` 规则与 MCP 税体检 |
| **Codex CLI** | `~/.codex/skills` + CLI + `AGENTS.md` | — | — | 支持 `audit project` 规则体检 |
| **其他工具**（Cursor / Windsurf / Cline / Roo Code / Trae / OpenCode 等） | `npm i -g tokless` + 项目根 `AGENTS.md` 立即可用 | 欢迎参考 `targets/claude-code.js` 共创适配 PR | — | 支持 `audit project` 规则体检 |

### 1. `tokless skeleton`（兼容 `repo-skeleton`）+ `rules/AGENTS.md` 省流规范 —【100% 所有 AI 编程工具通用】

无需预建索引数据库，纯 Node.js 标准库毫秒级提取 `.js/.ts/.tsx/.py/.go/.rs/.java/.c/.cpp/.md` 等文件的类名、函数签名、接口与精确 **`[L起-L止]` 行号范围**，配合 [`rules/AGENTS.md`](./rules/AGENTS.md) 中的两步精准读取规范，探索期单文件省流 **85%~97%**：

```bash
# 扫描整个源码目录（自动排除 node_modules/.git/dist/target 等），一步生成全局行号地图
npx tokless skeleton ./src --depth 3

# 提取单个大文件的函数签名与 [L起-L止] 行号（支持 --json 输出结构化数据）
npx tokless skeleton ./src/App.tsx
```

### 2. `PreToolUse` 防盲读硬刹车（`scripts/read-guard-hook.js`）—【可扩展钩子机制，目前已原生打通 Google Antigravity 与 Claude Code】

精准防盲读，绝不设死板跨度锁死：当 AI 不传起止行号盲读超过 200 行（可通过环境变量 `TOKLESS_READ_MAX_LINES` 调整）的代码文件，或传入 `1~文件末尾` 假切片糊弄时，钩子自动拦截并当场返回该文件的 `[L起-L止]` 语法骨架；一旦拿到明确行号，无论目标函数是 50 行还是 500 行均一次完整放行，避免拆成多轮碎片读取倒贴 Cache Read。

### 3. 剥离外部 MCP 空载底座税的净身子角色（`agents/`）—【Antigravity 插件专用】

内置 [`tokless-coder`](./agents/tokless-coder.md) 与只读 [`tokless-reviewer`](./agents/tokless-reviewer.md)，默认声明 `inheritMcp: false` 卸除纯写代码/审代码时用不上的外部 MCP Schema，消除每一步固定背负的数千至数万空载底座税。

### 4. `tokless audit`（兼容 `agy-audit`）体检仪 —【`audit project` 跨端通用；`audit session / compare` 属 Antigravity 专用】

直接离线解析本地项目规则配置与 Antigravity 会话日志，不花 1 个模型 Token：

```bash
# [跨端通用] 诊断项目的 AGENTS.md / SKILL.md 肥胖度与全局/工作区 MCP 空载底座税
npx tokless audit project <项目目录路径>

# [Antigravity 专用] 解剖单个会话（支持短 ID 前缀）：查 Top 5 烧钱步骤、Prefix Cache 断层与压缩节点
npx tokless audit session <会话ID前缀>

# [Antigravity 专用] 优化前后两个会话的 A/B 量化账单对比
npx tokless audit compare <优化前ID> <优化后ID>
```

---

## 各工具安装位置与日常使用方法

### 1. 已内置一键挂载的三大工具（运行 `npx tokless install` 后分别装到了哪里、怎么触发）

- **Google Antigravity**（`--target agy`）：
  - **安装位置**：`~/.gemini/config/plugins/agy-tokless/`（挂载 `plugin.json`、`hooks.json`、`rules/AGENTS.md`、`skills/` 与 `agents/`）。
  - **日常触发**：装好后新开对话即自动生效——探索大文件时自动触发 `code-skeleton` 技能与 `PreToolUse` 防盲读拦截；派发纯编码或审查子任务时可指定 `tokless-coder` / `tokless-reviewer` 卸除 MCP 税；需要查账单时直接让 AI 调用 `token-audit` 技能或手动运行 `npx tokless audit session <ID>`。
- **Claude Code**（`--target claude`）：
  - **安装位置**：核心脚本存入 `~/.claude/tokless/`，技能写入 `~/.claude/skills/code-skeleton/SKILL.md`，并将 `Read` 防盲读钩子无损合并进 `~/.claude/settings.json`（保留你原有的权限与自定义钩子，卸载时精准剥离还原）。
  - **日常触发**：在任意项目启动 `claude` 后自动生效——当 Claude 试图不带 `offset/limit` 盲读超过 200 行的代码文件时，`PreToolUse` 钩子会自动拦下并把 `[L起-L止]` 骨架直接喂回给它，引导它按行号精读。
- **Codex CLI**（`--target codex`）：
  - **安装位置**：`~/.codex/skills/code-skeleton/`（含 `SKILL.md` 与零依赖 `tools/repo-skeleton` 脚本）。
  - **日常触发**：Codex 会自动发现并按需调用 `code-skeleton` 技能先看行号骨架再精读源码；建议同时将 [`rules/AGENTS.md`](./rules/AGENTS.md) 中的省流规范合入项目根目录的 `AGENTS.md` 以强化主动触发。

### 2. 其他 AI 编程工具（Cursor、Windsurf、Cline、Roo Code、Trae、OpenCode 等）怎么用？

- **当下立即可用法（1 分钟接入核心省流能力）**：
  1. 在终端运行 `npm i -g tokless` 安装全局 CLI（获得全局 `tokless skeleton` 与 `tokless audit project` 命令）；
  2. 将仓库内 [`rules/AGENTS.md`](./rules/AGENTS.md) 的省流读取规范复制到你项目根目录的 `AGENTS.md`（或对应编辑器的 `.cursor/rules/`、`.windsurfrules`、`.clinerules` 等规则文件）中。配置完成后，你的 AI 助手就会在读大文件前主动调用 `tokless skeleton <路径>` 拿 `[L起-L止]` 行号地图并按需精读，也能随时用 `tokless audit project .` 检查规则体积。
- **关于官方一键挂载与共创适配的坦诚说明**：
  由于作者近期精力有限，暂时还没法逐一去折腾十几个编辑器各自的专属全局目录与钩子格式。**如果你日常主力使用其他工具，非常欢迎直接让你的 AI 参考 [`targets/claude-code.js`](./targets/claude-code.js) 写一个对应的挂载适配并提交 PR——我们审核代码确认干净无误后会第一时间合并发版；后续作者空下来也会逐步跟进补充更多主流工具的官方一键支持。**

---

## Node.js 编程接口（Programmatic API）

`tokless` 同时导出零依赖标准 CommonJS 接口（支持 `tokless`、`tokless/skeleton`、`tokless/read-guard`、`tokless/audit` 子路径按需引入），方便其他 Agent 编排器或评测脚本在进程内直接调用，零子进程开销：

```js
const {
  generateSkeleton,        // 自动识别文件或目录生成 [L起-L止] 骨架
  evaluateReadGuard,       // 纯函数评估 Antigravity / Claude Code 读取请求是否盲读
  analyzeSession,          // 解析单次会话账单、缓存断层与峰值水位
  auditProject,            // 审计项目常驻规则体积与 MCP Schema 底座税
} = require('tokless');

// 1. 提取目录或单文件骨架
const skel = generateSkeleton('./src', { maxDepth: 2 });
console.log(skel.formatted);

// 2. 进程内调用防盲读判定（支持 Antigravity 与 Claude Code 载荷格式）
const verdict = evaluateReadGuard({
  tool_name: 'Read',
  tool_input: { file_path: './src/large-module.ts' },
});
// verdict => { decision: 'deny' | 'allow', reason?: string, host: 'claude' | 'antigravity' }
```

---

## 社区共建：欢迎扩展更多 AI 编程工具（Contributing）

`tokless` 将各宿主的安装与卸载逻辑完全解耦在 [`targets/`](./targets/) 目录下，每个宿主只需一个独立的百行级适配器文件：

- [`targets/antigravity.js`](./targets/antigravity.js) — Google Antigravity 插件、钩子与净身角色挂载
- [`targets/claude-code.js`](./targets/claude-code.js) — Claude Code `~/.claude/settings.json` 无损合并与技能挂载（推荐新增适配时优先参考）
- [`targets/codex.js`](./targets/codex.js) — OpenAI Codex CLI 技能挂载

因作者近期精力有限，暂未逐一折腾十几个编辑器的专属全局配置与钩子格式。非常欢迎使用 **Cursor、Windsurf、Cline、Roo Code、Trae、OpenCode、GitHub Copilot** 等工具的开发者，直接让自己的 AI 参考 [`targets/claude-code.js`](./targets/claude-code.js) 完成适配并在 [`targets/index.js`](./targets/index.js) 中注册后提交 Pull Request（或为 `tools/repo-skeleton` 补充更多语言的语法签名识别）——我们审核无误后会立即合并发版；后续作者空下来也会逐步补充更多工具的官方一键支持。

提交 PR 前请在本地运行全套自检（包含跨平台路径测试与 100% 零私人路径泄漏门禁）：

```bash
npm test
```

---

## 开源致谢（Acknowledgments）

`tokless` 全部代码基于 Node.js 标准库从零独立实现，核心设计思路受益于以下优秀开源探索与社区贡献者，特此致谢：

- **社区贡献者**：感谢 [@PXY000](https://github.com/PXY000) 在跨平台 PowerShell 技能文档、钩子 Node 绝对路径解析、路径穿越防护与沙箱安全审计查找上的扎实修复与单测贡献。
- **灵感致敬**：
  - [HoangP8/tokless](https://github.com/HoangP8/tokless)：启发了项目命名及“指令规范 + 生命周期钩子”组合拦截上下文膨胀的思路；
  - [ILoveMyJay/repocontext](https://github.com/ILoveMyJay/repocontext) 与 [pdavis68/RepoMapper](https://github.com/pdavis68/RepoMapper)：启发了“先拿带行号的紧凑语法骨架地图，再按行号精准切片读取”的探索期降耗策略；
  - [ooples/token-optimizer-mcp](https://github.com/ooples/token-optimizer-mcp)：启发了针对工具返回体积与会话级 Token 账单做量化透视的思路。

如果 `tokless` 切实帮你省下了宝贵的周额度，欢迎在右上角点一颗 **Star** 支持，或关注作者技术手记公众号 **【织歌AI笔记】** 交流实战经验。

---

## License

[MIT](./LICENSE)
