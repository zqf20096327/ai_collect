# STS2 LLM Player Agent

一个面向《Slay the Spire 2》的 GitHub Copilot 玩家代理定制包：让 Copilot CLI / VS Code 通过 STS2MCP 读取游戏状态、做当前 run 决策、复盘失败与胜利，并把经验沉淀成可复用的长期记忆。

> 当前目标不是做“攻略问答机器人”，而是做一个会接管对局、会复盘、会修正打法的长期玩家代理。

## 亮点

- **真实接管游戏**：通过 STS2MCP 的 MCP 工具读取状态、打牌、选奖励、走地图、进商店、火堆与事件。
- **自带玩家入口**：`.github/agents/player.agent.md` 是主入口，负责在 piloting / review / research / runtime prep 之间切换。
- **四层记忆系统**：当前 run playbook、近期 run timeline、完整复盘 archive、跨局 lesson ledger。
- **战斗安全协议**：默认 `读状态 -> 验证一张牌 -> 执行动作 -> 重新读状态`，避免手牌索引漂移。
- **复盘驱动学习**：关键失败、Boss、精英、成型节点后，把经验压缩成未来可召回的 heuristic。
- **策略不确定时会研究**：需要外部信息时，用研究 skill 搜集资料，再结合当前牌组、遗物、血量、地图落地。

## 项目当前情况

这个仓库已经具备一个可运行的 Copilot customization pack 骨架：

| 模块 | 状态 | 说明 |
|---|---:|---|
| `player` custom agent | 可用 | 作为长期玩家代理入口，负责任务编排 |
| `sts2-prepare-runtime` skill | 可用 | 检查 MCP 工具、游戏/mod 状态与 CLI 持久配置 |
| `sts2-pilot-run` skill | 可用 | 处理战斗、奖励、路线、商店、休息、事件等当前 run 决策 |
| `sts2-review-run` skill | 可用 | 处理死亡/胜利/关键 swing 复盘与 lesson 更新 |
| `sts2-research-strategy` skill | 可用 | 面向不确定策略问题做外部研究 |
| `.github/sts2-memory/` | 持续积累中 | 保存 run 记忆、复盘与跨局经验 |
| `.vscode/mcp.json` | 已提供 | VS Code 风格 MCP 配置参考 |
| Copilot CLI 持久 MCP | 需本机配置 | 需要写入 `~/.copilot/mcp-config.json` 或用 `/mcp add` |

仍然需要注意：STS2 仍在变化，STS2MCP 工具覆盖也会变化；这里的打法记忆来自实际 run 复盘，但不是“最优解证明”。

## 用到的项目与技术

- [Slay the Spire 2](https://store.steampowered.com/app/2868840/Slay_the_Spire_2/)：目标游戏。
- [STS2MCP](https://github.com/Gennadiyev/STS2MCP)：核心 MCP/mod 依赖。本仓库的 submodule 暂时指向 [`ttxttx1111/STS2MCP`](https://github.com/ttxttx1111/STS2MCP) 的 `copilot-agent-tools` 分支，用于保留当前 player agent 依赖的菜单、profile、选择界面等 MCP 工具增强。
- GitHub Copilot custom instructions / custom agents / skills：本仓库的主要交互层。
- GitHub Copilot CLI：推荐的本地命令行玩家入口。
- VS Code MCP 配置：`.vscode\mcp.json` 提供共享参考配置。
- `uv` + Python：用于启动 STS2MCP 的 MCP server。

## 环境要求

推荐环境：

- Windows
- 已安装 Steam 版 Slay the Spire 2
- 游戏内已安装并启用 STS2MCP mod
- 本地 STS2MCP HTTP 服务可访问 `localhost:15526`
- 已安装 `uv`
- 已安装 GitHub Copilot CLI 或使用支持 custom agents / skills / MCP 的 VS Code

本仓库默认参考的本机游戏路径是：

```text
D:\program\steam\steamapps\common\Slay the Spire 2\
```

如果你的安装路径不同，只要 STS2MCP mod 能正常启动并监听 `localhost:15526` 即可。

## 快速开始

1. 克隆仓库并拉取 submodule：

```powershell
git clone --recurse-submodules https://github.com/ttxttx1111/sts2-llm.git
Set-Location .\sts2-llm
```

如果已经克隆但没有 submodule：

```powershell
git submodule update --init --recursive
```

2. 按 STS2MCP 上游说明安装 mod，并确认本地服务可访问：

```powershell
curl http://localhost:15526/
```

3. 确认 MCP server 目录存在：

```powershell
Test-Path .\vendor\STS2MCP\mcp\server.py
```

4. VS Code 用户可以参考 `.vscode\mcp.json`。该配置使用 workspace 相对路径：

```json
{
  "servers": {
    "sts2": {
      "type": "stdio",
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "${workspaceFolder}\\vendor\\STS2MCP\\mcp",
        "python",
        "server.py",
        "--no-trust-env"
      ]
    }
  }
}
```

5. Copilot CLI 用户可以把等价配置放到 `~\.copilot\mcp-config.json`，注意把路径替换成你本机仓库的绝对路径：

```json
{
  "mcpServers": {
    "sts2": {
      "type": "stdio",
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "D:\\path\\to\\sts2-llm\\vendor\\STS2MCP\\mcp",
        "python",
        "server.py",
        "--no-trust-env"
      ]
    }
  }
}
```

6. 打开 Copilot CLI 或 VS Code，进入 `player` agent，然后用自然语言开始：

```text
接管当前这把
帮我复盘刚才输的这局
研究一下这套铁甲前期该不该走精英
```

## 仓库结构

```text
.github\
  agents\
    player.agent.md              # 长期玩家代理入口
  skills\
    sts2-prepare-runtime\        # MCP / 运行时准备
    sts2-pilot-run\              # 当前 run 操作与决策
    sts2-review-run\             # 复盘与经验沉淀
    sts2-research-strategy\      # 外部策略研究
  sts2-memory\
    current-playbook.md          # 当前 run 战术记忆
    run-history.md               # 近期 run 索引
    runs\                        # 活跃/历史 run 时间线
    reviews\                     # 完整复盘 archive
    lesson-ledger.md             # 跨局经验 ledger
  design\                        # 架构与工作流设计
  changelog\                     # 每次工作流变化的记录
.vscode\
  mcp.json                       # VS Code MCP server 参考配置
vendor\
  STS2MCP\                       # 上游 STS2MCP submodule
deprecated\                      # 早期废弃版本快照（详见下方"废弃的历史版本"）
```

## 废弃的历史版本

`deprecated/` 下保存了几组早期探索版本的代码快照，已不在当前主路径上，仅作历史与演进脉络参考。这些快照以普通目录形式内嵌在本仓库中（不含嵌套的 git 历史），不需要额外 clone 或 submodule 拉取。

- **`deprecated/1/` — 早期组件组合**
  - `STS2-MenuControl/`：基于 .NET / Harmony 的 STS2 主菜单 HTTP 控制 mod，提供 REST 接口来导航菜单、选角、开 run、处理多人房间和模态弹窗（端口 8081）。
  - `llm-slay-the-spire/`：一个 STS2 MCP server 加自动 runner 包（`slay_the_spire_sts2`），对接本地 15526 游戏态 API 与 8081 菜单控制 API，对外暴露 MCP 工具与资源用于状态查询、推荐和受控动作，并内置一条菜单流 / 战斗推进 / 奖励 / 路线 / 主菜单恢复的 runner 循环。
- **`deprecated/2/ai play slay the spire 2/` — LLM-led 双 agent 工作区**
  - 围绕“让 agent 稳步学会打通 STS2”的长期目标搭建的工作区，区分 `player`（实时对局执行）和 `developer`（开 run、失败恢复、工具与记忆维护）两个 agent。
  - 强调持久化的 run / lesson / playbook 记忆，主玩法路径后来切到 LLM-only：默认经 GitHub Copilot CLI 用 `gpt-5.4-chat`，并支持 `copilot-sdk` 暖会话桥接、`github-models` 直连以及 `openai-compatible` 端点等可切换 provider。
- **`deprecated/3/ai-play-slts2-2/` — 从厚多智能体到 player 直连的演进**
  - 最初想做完整的 `player / runtime / reviewer` 多智能体体系，但在实战中发现 coordinator 包装过厚反而更易出错、更慢、更脆，于是收敛成“player 直连游戏、skill 负责教 player 怎么想、组织者只通过与 player 对话求证来诊断”的更薄主链路。仓库本身保留了一次明显的架构演进痕迹（厚 runtime -> 保留角色分工但主路径 native 化），并坚持证据优先的学习回路：先落 live 事件与 summary，reviewer 再基于证据复盘，最后才更新 lessons / playbook。

这些目录里的 README / AGENTS / 内嵌说明都是各版本当时的写法，不再代表当前仓库的主路径与结论。要看当前打法与工作流，请回到本 README 顶部以及 `.github/design/`。

## 工作流设计

更多细节见：

- [设计总览](.github/design/README.md)
- [系统细节](.github/design/system-details.md)
- [变更记录](.github/changelog/README.md)

核心循环是：

```text
play -> timeline -> review -> archive -> compress -> recall -> revise
```

也就是说：先实战推进，再记录时间线；关键节点做复盘；完整复盘保存在 archive；少量稳定结论压缩到 lesson ledger；当前 run 真需要的提醒写回 playbook。

## 使用边界

- 这是一个本地玩家代理定制包，不是 STS2 官方项目。
- MCP 控制依赖本机游戏、mod 和 `localhost:15526`，不适合暴露到公网。
- 运行记忆是经验材料，不是不可推翻的规则；新证据应该能降级、改写或退休旧 heuristic。
- 战斗中不要连续复用旧手牌索引；每个实际动作前都要重新确认最新状态。
- 如果你公开 fork，请检查 `.github\sts2-memory\` 中是否包含你不想公开的个人 run 记录。

## 贡献

欢迎围绕以下方向改进：

- 更稳的 runtime/MCP 准备流程
- 更清晰的 agent / skill 边界
- 更好的复盘模板与 lesson 分类
- 角色、牌组、遗物、Boss 的可复用打法经验
- STS2MCP 工具变化后的同步更新

贡献前建议阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 致谢

本项目建立在 [Gennadiyev/STS2MCP](https://github.com/Gennadiyev/STS2MCP) 之上。没有这个 mod 和 MCP server，就无法让 Copilot 可靠读取并操作 STS2 当前局面。

## License

本项目使用 [MIT License](LICENSE)。
