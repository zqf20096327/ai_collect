<div align="center">

<img src="docs/img/banner.png" alt="GAT — Godot Agent Team" width="100%">

# GAT — Godot Agent Team

**A full-cycle game-development agent for Godot: from a one-line idea to a running, verified build — style-consistent, self-evolving, and runnable under both Claude Code and Codex.**

<p>
<img src="https://img.shields.io/badge/Godot-4.x-478CBF?style=for-the-badge&logo=godotengine&logoColor=white" alt="Godot 4.x">
<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
<img src="https://img.shields.io/badge/Claude_Code-ready-D97757?style=for-the-badge&logo=anthropic&logoColor=white" alt="Claude Code">
<img src="https://img.shields.io/badge/Codex-ready-412991?style=for-the-badge&logo=openai&logoColor=white" alt="Codex">
</p>
<p>
<img src="https://img.shields.io/badge/%F0%9F%94%92_style--locked-0b1524?style=for-the-badge" alt="style-locked">
<img src="https://img.shields.io/badge/%E2%99%BB_self--evolving-0b1524?style=for-the-badge" alt="self-evolving">
<img src="https://img.shields.io/badge/license-PolyForm_NC-1f2937?style=for-the-badge" alt="License: PolyForm Noncommercial">
<img src="https://img.shields.io/badge/version-0.2.0-a855f7?style=for-the-badge" alt="v0.2.0">
</p>

**[English](#english) · [中文](#中文)**

</div>

---

## English

GAT is not a single prompt. It is a small **team of role agents** running a **modular,
gated pipeline**, backed by a **game-architecture knowledge base** and a **self-evolving memory**,
that carries a game all the way from *design* to *implementation* inside Godot.

It unifies four projects into one workflow:

- a **document-driven design pipeline** (concept → GDD → art direction → milestones),
- the **game-architect** knowledge base (30+ references on paradigms and per-system design),
- the **game-skill-vfx** pipeline (AI skill-effect VFX → Godot sprite sheets),
- and **live Godot editor control** (build scenes/nodes in a running editor).

```
idea ─► DESIGN ─► STYLE-LOCK ─► REFERENCE ─► IMPLEMENT ─► GODOT GATE ─► VERIFY ─► game
         (docs)   (contract)   (code map)   (Godot)     (runtime)       (evidence)
                          ▲ read / write ▼
                 KNOWLEDGE · architecture refs · self-evolving wiki
```

### Four gates that make it more than a prompt

**⭐ Style-lock — one style, enforced forever.** Generate one hero in a "papercut wuxia" look,
and every icon, VFX, and tileset for the next six months must match it — or the game reads as an
asset-flip. GAT freezes your art direction into an enforceable **Style Contract**
(`design/art/style-contract.yaml`). Every asset skill (1) refuses to run without it, (2) composes
its prompt as `frozen-prefix + your-subject + frozen-suffix` with a locked negative/seed, and
(3) passes an **audit gate** (`tools/art_audit.py`) that rejects off-palette, wrong-resolution,
or off-family output. Changing the style is a deliberate `--relock`, never an accident.
→ [`docs/style-lock.md`](docs/style-lock.md)

<div align="center"><img src="docs/img/style-lock.png" alt="How style-lock works: subject + frozen contract → audit gate → on-style family; off-style is regenerated" width="92%"></div>

**⭐ Self-evolving — the toolkit compounds.** Every skill reads a shared knowledge base *before*
work and writes lessons back *after*. Pitfalls, recipes, patterns, and balance bands accumulate
in `knowledge/wiki/`; game #10 starts far ahead of game #1. GAT can even **propose improvements
to its own skills** — through review, never silently. → [`docs/self-evolving.md`](docs/self-evolving.md)

**⭐ Reference-first — inspect real code before writing new code.** Every substantial feature,
refactor, or fix starts by tracing the current project's owner/call chain/test, then reading a
small licensed upstream implementation. GAT records exact files, pinned revision, license, and the
source→target adaptation in `.gat/evidence/`; `tools/reference_gate.py` rejects vague or incomplete
maps. This prevents disconnected duplicate systems. → [`docs/reference-first.md`](docs/reference-first.md)

**⭐ Godot-gated — engine evidence, not compile optimism.** Runtime writes require MCP
version/project preflight before editing and a final `run → debug output → stop` after the last
edit. UI claims additionally need input/clickthrough and screenshots. Player saves are agent-read-
only; debug runs require project-enforced isolation and a fresh pre-launch snapshot receipt.
→ [`docs/godot-gate.md`](docs/godot-gate.md)

### The pipeline

| Phase | Skills | Output |
|---|---|---|
| **Design** | `gat-brainstorm` · `gat-story` · `gat-design` · `gat-milestone` | `design/` docs + `production/milestone.md` |
| **Style-lock** ⭐ | `gat-style-lock` | frozen `style-contract.yaml` |
| **Assets** | `gat-asset` · `gat-vfx` | style-audited art + Godot VFX (`.tres`) |
| **Reference** ⭐ | `gat-reference-first` | local/upstream code map + revision/license gate |
| **Implement** | `gat-scaffold` · `gat-implement` · `gat-godot-gate` | project + code/scenes + MCP runtime evidence |
| **Verify** | `gat-verify` | provenance + runtime + interaction + sim + art + requirement coverage |
| **Evolve** ⭐ | `gat-evolve` · `gat-learn-from-ref` | knowledge written back; reference lessons |

`/gat-workflow-start` tells you the next step at any point. Full guide:
[`docs/workflow.md`](docs/workflow.md) · architecture: [`docs/architecture.md`](docs/architecture.md).

### Install (Claude Code and/or Codex)

The toolkit is cloned once and shared by all your games. Point a game repo at it:

```bash
git clone https://github.com/chenhangcuisg-code/gat ~/gat
# wire a game project to run GAT under both runtimes:
bash ~/gat/install.sh --runtime both --target /path/to/my-game
#   Windows:  pwsh -File ~/gat/install.ps1 -Runtime both -Target C:\path\to\my-game
cd /path/to/my-game       # then run /gat-workflow-start
```

- **Claude Code** → skills/agents linked into `.claude/`, rules in `CLAUDE.md`.
- **Codex** → `AGENTS.md` + `~/.codex/prompts/gat-*.md` generated from the same source.

One set of SKILL.md files, both runtimes — no fork. → [`docs/dual-runtime.md`](docs/dual-runtime.md)

### Requirements

- **Godot 4.x** (tested 4.6.2 / 4.7) plus a configured **Godot MCP** provider for runtime writes;
  optional **Hastur** plugin for supplementary live editor control.
- **Python 3.10+** with `pillow numpy pyyaml` for the style tools.
- For **skill VFX**: a CUDA GPU (open models, no paid APIs). → [`docs/deployment/vfx-gpu-server.md`](docs/deployment/vfx-gpu-server.md)
- Static art via `gpt-image-2` (no GPU needed).

### Worked example

[`examples/ember-and-ink/`](examples/ember-and-ink/) — a papercut-wuxia idle-RPG taken through
design → style-lock, including a real, runnable Style Contract.

### License

**Source-available, not permissive.** Free for personal, learning, research, and non-commercial
use under [PolyForm Noncommercial 1.0.0](LICENSE). **Commercial use requires prior approval —
contact the author** (see [`LICENSING.md`](LICENSING.md)). The reverse-engineering / reference-
study module is **learning-only**: study games you have the right to inspect, never redistribute
third-party content, and no DRM circumvention.

### Credits

Built on and integrating: the Claude-Code-Game-Studios-derived design workflow, the
`game-architect` knowledge base, [`game-skill-vfx`](https://github.com/chenhangcuisg-code/game-skill-vfx)
(FLUX/AnimateDiff/SDXL VFX), the Hastur Operation Plugin (Godot editor control), and the
`game-unpack` reference-study lessons. v0.2's reference/runtime process also adapts focused patterns
from [`gd-agentic-skills`](https://github.com/thedivergentai/gd-agentic-skills),
[`Coding-Solo/godot-mcp`](https://github.com/Coding-Solo/godot-mcp), and
[`mkdevkit/godot-mcp`](https://github.com/mkdevkit/godot-mcp). See
[`LICENSING.md`](LICENSING.md) and [`provenance/`](provenance/) for exact attributions.

---

## 中文

GAT（Godot 智能体团队）不是一句 prompt，而是一个由**角色智能体组成的小团队**运行一条
**模块化、带强制门禁的流水线**，背后有**游戏架构知识库**与**自进化记忆**支撑，把一款游戏从**设计**
一路推进到 Godot 里的**实现**。

它把四个项目整合进一条工作流：

- **文档驱动的设计流水线**（概念 → GDD → 美术方向 → 里程碑）；
- **game-architect** 知识库（30+ 篇范式与分系统设计参考）；
- **game-skill-vfx** 流水线（AI 技能特效 → Godot 精灵表）；
- 以及**实时 Godot 编辑器操控**（在运行中的编辑器里搭场景/节点）。

```
灵感 ─► 设计 ─► 锁风格 ─► 参考代码 ─► 实现 ─► Godot门禁 ─► 验证 ─► 游戏
        (文档)  (契约)    (映射)    (代码)   (实跑证据)   (逐项证据)
                     ▲ 读 / 写 ▼
              知识库 · 架构参考 · 自进化 wiki
```

### 四道让它超越 prompt 的强制门

**⭐ 锁风格（Style-lock）——一次定风格，永久强约束。** 你用「水墨剪纸武侠」画了一个主角，
之后半年里每一张图标、每一个特效、每一块 tileset 都必须是同一个「画师」的手笔，否则游戏就像
素材拼凑。GAT 把美术方向冻结成可执行的**风格契约** `design/art/style-contract.yaml`：所有出图
技能都会（1）没契约就拒绝生成，（2）把 prompt 组成 `冻结前缀 + 你的主体 + 冻结后缀`（附带锁定
的负面词/种子），（3）过一道**审计门禁** `tools/art_audit.py`，调色板不符、分辨率不对、跟母版
不像的一律打回重生成。改风格必须显式 `--relock`，绝不「顺手」漂移。
→ [`docs/style-lock.md`](docs/style-lock.md)

<div align="center"><img src="docs/img/style-lock.png" alt="风格锁工作原理：主体 + 冻结契约 → 审计门禁 → 同风格素材族；跑偏的自动打回重生成" width="92%"></div>

**⭐ 自进化（Self-evolving）——工具越用越强。** 每个技能干活**前**先读共享知识库，干完**后**把
教训写回去。踩坑、方法、模式、数值区间不断沉淀进 `knowledge/wiki/`，做到第 10 个游戏时的起点
远高于第 1 个。GAT 甚至能**提出对自身技能的改进**——但走评审、绝不悄悄改。
→ [`docs/self-evolving.md`](docs/self-evolving.md)

**⭐ 参考优先（Reference-first）——先读真实代码，再写新代码。** 每个实质功能、重构或修复，
先追踪当前项目的数据归属、调用链、类似实现和测试，再按需读取少量有许可证的上游源码。GAT 会把
具体文件、固定 commit、许可证以及“源 → 目标”的改编写入 `.gat/evidence/`，并由
`tools/reference_gate.py` 机器校验，避免重复造一套与现有系统脱节的实现。
→ [`docs/reference-first.md`](docs/reference-first.md)

**⭐ Godot 实跑门禁——不是能编译就算完成。** 修改运行时代码前必须用 MCP 确认引擎和工程；
最后一次修改后必须完成 `运行 → 读取调试输出 → 停止本次进程`。UI 还要有真实输入/点击链与截图。
玩家手动存档对智能体只读，调试只允许进入项目真正执行的隔离档，并在每次启动前取得新备份凭据。
→ [`docs/godot-gate.md`](docs/godot-gate.md)

### 流水线

| 阶段 | 技能 | 产出 |
|---|---|---|
| **设计** | `gat-brainstorm` · `gat-story` · `gat-design` · `gat-milestone` | `design/` 文档 + `production/milestone.md` |
| **锁风格** ⭐ | `gat-style-lock` | 冻结的 `style-contract.yaml` |
| **出素材** | `gat-asset` · `gat-vfx` | 过审的美术 + Godot 特效（`.tres`） |
| **参考代码** ⭐ | `gat-reference-first` | 本地/上游源码映射 + commit/许可证门禁 |
| **实现** | `gat-scaffold` · `gat-implement` · `gat-godot-gate` | 工程 + 代码/场景 + MCP 实跑证据 |
| **验证** | `gat-verify` | 来源 + 运行 + 交互 + 数值 + 美术 + 逐需求覆盖 |
| **进化** ⭐ | `gat-evolve` · `gat-learn-from-ref` | 教训写回；参考游戏学习 |

随时用 `/gat-workflow-start` 看下一步。完整指南见 [`docs/workflow.md`](docs/workflow.md)，
架构见 [`docs/architecture.md`](docs/architecture.md)。

### 安装（支持 Claude Code 和 Codex）

工具包只克隆一次，供你所有游戏共用。把某个游戏仓库指向它即可：

```bash
git clone https://github.com/chenhangcuisg-code/gat ~/gat
bash ~/gat/install.sh --runtime both --target /path/to/my-game
#   Windows:  pwsh -File ~/gat/install.ps1 -Runtime both -Target C:\path\to\my-game
cd /path/to/my-game       # 然后运行 /gat-workflow-start
```

- **Claude Code** → 技能/智能体链接进 `.claude/`，规则写入 `CLAUDE.md`。
- **Codex** → 由同一份源生成 `AGENTS.md` 与 `~/.codex/prompts/gat-*.md`。

同一套 SKILL.md，双运行时，不分叉。→ [`docs/dual-runtime.md`](docs/dual-runtime.md)

### 环境要求

- **Godot 4.x**（已测 4.6.2 / 4.7）；运行时代码写入需配置 **Godot MCP**，可选 **Hastur**
  仅作为实时编辑器操控补充。
- **Python 3.10+**，风格工具依赖 `pillow numpy pyyaml`。
- **技能特效**需要 CUDA GPU（开源模型，无需付费 API）。→ [`docs/deployment/vfx-gpu-server.md`](docs/deployment/vfx-gpu-server.md)
- 静态美术走 `gpt-image-2`，无需 GPU。

### 示例

[`examples/ember-and-ink/`](examples/ember-and-ink/)——「烬与墨」水墨剪纸放置 RPG，走通了
设计 → 锁风格，含一份真实可运行的风格契约。

### 许可

**源码可见，但非宽松许可。** 个人、学习、研究与非商业用途依 [PolyForm Noncommercial 1.0.0](LICENSE)
免费使用；**商业使用需事先批准协商——请联系作者**（见 [`LICENSING.md`](LICENSING.md)）。逆向 /
参考学习模块**仅供学习**：只研究你有权查看的游戏，绝不二次分发第三方内容，且不含任何破解 DRM 的能力。

### 致谢

整合并基于：源自 Claude-Code-Game-Studios 的设计工作流、`game-architect` 知识库、
[`game-skill-vfx`](https://github.com/chenhangcuisg-code/game-skill-vfx)（FLUX/AnimateDiff/SDXL 特效）、
Hastur Operation Plugin（Godot 编辑器操控）与 `game-unpack` 的参考学习经验。v0.2 还按具体源码
借鉴了 [`gd-agentic-skills`](https://github.com/thedivergentai/gd-agentic-skills)、
[`Coding-Solo/godot-mcp`](https://github.com/Coding-Solo/godot-mcp) 与
[`mkdevkit/godot-mcp`](https://github.com/mkdevkit/godot-mcp) 的聚焦流程。完整 commit、文件和许可证见
[`provenance/`](provenance/) 与 [`LICENSING.md`](LICENSING.md)。

---

<div align="center">
<sub>

**Keywords** — Godot agent · game agent · Godot AI agent · game-making agent · AI game development · autonomous game developer · game-dev automation · multi-agent game studio · GDScript agent · Godot game generator · Claude Code agent · Codex agent · style-locked asset generation · self-evolving agent · text-to-game

**关键词** — 游戏制作智能体 · 游戏开发智能体 · Godot 智能体 · Godot 游戏开发 agent · AI 做游戏 · 自动做游戏 · 一句话生成游戏 · 游戏 AI agent · 多智能体游戏工作室 · GDScript 智能体 · 风格锁定出图 · 自进化 agent

</sub>
</div>
