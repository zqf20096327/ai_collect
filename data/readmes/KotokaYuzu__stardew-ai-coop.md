# 星露谷物语 AI 队友（Stardew Valley AI Coop Companion）

给《星露谷物语》添加一个会聊天、能干活的 AI 队友。她在第二个游戏窗口中，通过原生局域网联机进入你的农场，可以理解中文指令、帮忙干农活、钓鱼下矿，也可以在游戏里聊天。

- 浏览器面板控制，默认地址为 `http://127.0.0.1:8765`，仅绑定本机回环地址；端口冲突时会自动选择其他端口。
- Python 大脑使用标准库，游戏侧使用 C# SMAPI 模组 **CoopLink**。
- 发布包自带便携 Python 和预编译模组，无需另装 Python 或 .NET SDK 即可正常使用。
- 可自行配置兼容 Chat Completions 的模型接口和 API Key。

> **本项目不包含游戏本体或 SMAPI 安装器。** 请自行准备正版《Stardew Valley》并安装 SMAPI。详见 [DISCLAIMER.md](DISCLAIMER.md)。

## v0.5.0 更新

- AI 可以按需读取双方的可见任务、共同订单、角色状态、菜单和当前地图分页数据。
- AI 可以选择已接入的游戏行动接口，并根据真实回执继续判断和调整。
- 改进修改失败或回执超时后的反馈；未确认的修改不会自动重复提交。
- 矿洞指定坐标传送增加入口连通性检查，并在回执中记录实际落点。

当前开放的是**已接入的游戏接口**，不是全部游戏 API，也不是 MCP 服务器。新查询、模型自主操作和矿洞落点仍需进一步实机验证。

## 兼容版本

| 组件 | 版本 |
| --- | --- |
| 游戏 | Stardew Valley 1.6.15（build 24356），开发与实机测试基线 |
| SMAPI | 4.5.2；模组声明的最低版本为 4.0.0 |
| 运行时 | .NET 6；发布包内含便携 Python 3.13.16 |
| 项目版本 | CoopLink **0.5.0** / 面板 **0.5.0** / 协议 **6** |
| 系统 | Windows 10 / 11 x64 |

- 其他 1.6.x 版本未逐一验证；1.5.x 及更早版本不兼容。
- 当前设计为「1 位真人 + 1 位 AI」，更多真人玩家参与尚未适配。
- 0.5.0 发布副本通过 **320 项离线测试**；离线测试不等于本版新增功能已完成实机验收。

## 安装

1. 自备正版《Stardew Valley》，并安装 [SMAPI](https://smapi.io/)。
2. 从 Releases 下载本项目发布包，完整解压到可写目录。
3. 双击 `星露谷物语AI启动面板.exe`，也可以使用 `启动面板.cmd`。
4. 程序会尝试查找游戏；如果未找到，请选择包含 `StardewModdingAPI.exe` 的游戏目录。
5. 如需更换游戏目录，可使用 `重新选择游戏目录.cmd`。

发布包不需要放进游戏的 `Mods` 文件夹。源码构建和维护说明见 [SETUP-FOR-AI.md](SETUP-FOR-AI.md)。

## 使用

1. 在面板「高级设置」中填写自己的模型接口地址、模型名和 API Key，保存后测试连接。
2. 点击「一键开始」，启动主人和 AI 队友两个游戏窗口。
3. 在主人窗口选择「合作 → 主持」并进入存档；农场需要有可用的联机小屋。
4. 等待队友连接，在 AI 窗口手动选择农场帮手。
5. 两边进入同一存档后，在面板选择「自动读取」和「启动模型大脑」。
6. 在游戏内按 `T` 聊天，例如「帮我浇水」「跟着我」「看看任务日志」。

模型服务需要兼容 Chat Completions，并能按照项目要求返回规划 JSON。连接测试通过不代表所有中转站或模型都能可靠完成游戏操作。

可选的 **JEV / AgentJev** 不随包提供权重和依赖，默认关闭；接入说明见 [AI必读.md](AI必读.md)。

## 隐私与注意事项

- API Key 使用 Windows DPAPI 加密，保存在本机 `stardew-coop/runtime/agent/settings.json` 中。
- 游戏聊天、筛选后的记忆和模型按需读取的游戏数据会发送给你配置的模型服务。
- AI 可能误解自然语言指令。使用游戏数据修改功能前，请先备份重要存档。
- 如不需要直接修改游戏数据，可在 `stardew-coop/config/companion.json` 中关闭 `gameEdits.enabled`。
- 发布或分享文件时，不要包含 `runtime/`、`memory/`、个人配置、令牌或存档。

## 目录

- `stardew-coop/agent/`：面板、Python 大脑和测试。
- `stardew-coop/config/`：人格、游戏常识和行为配置。
- `stardew-coop/mod/`：CoopLink 源码与预编译 DLL。
- `stardew-coop/profiles/`：主人和 AI 的独立模组档案。
- `stardew-coop/python/`：便携 Python 和相关许可证。
- `launcher-source/`：启动器源码。
- `packaging/`：发布构建脚本和便携覆盖说明。

## 文档

- [用户必读.txt](用户必读.txt)：玩家安装与使用教程。
- [AI必读.md](AI必读.md)：项目架构与维护说明。
- [SETUP-FOR-AI.md](SETUP-FOR-AI.md)：安装、验证与排障说明。
- [RELEASE-VALIDATION.md](RELEASE-VALIDATION.md)：本版测试结果和未覆盖范围。
- [DISCLAIMER.md](DISCLAIMER.md)：兼容性、版权与免责声明。
- [OPEN_SOURCE_REFERENCES.md](OPEN_SOURCE_REFERENCES.md)：参考项目、作者和许可证说明。

## 版权与致谢

本项目自有代码以 MIT 许可发布，详见 [LICENSE](LICENSE)。

感谢《Stardew Valley》作者 ConcernedApe、SMAPI 作者 Pathoschild 和所有相关贡献者。开源项目的参考来源、作者及许可边界见 [OPEN_SOURCE_REFERENCES.md](OPEN_SOURCE_REFERENCES.md)。

公开包使用自绘通用像素素材，不包含原版游戏图集、角色肖像或 Zpix 字体。便携 Python 及其组件遵循随附许可证。
- 界面素材取自 `ffffhx/stardew-valley-assets`，见 `stardew-coop/agent/assets/README.md`。

本仓库自有代码以 MIT 许可发布，见 [LICENSE](LICENSE)。
