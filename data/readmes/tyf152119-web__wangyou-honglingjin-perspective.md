# 网友红领巾视角 Codex Skill

一个面向公考做题、备考复盘、选岗决策与账号来源核验的人物视角 Skill。

基于网友红领巾的 B 站公开视频、官方微博、严格清洗字幕、原创专栏和选择性 ASR，提炼出 5 个心智模型、9 条决策启发式与可运行的表达规则。

## 能做什么

- 复盘模考中的调度、读题、方法、执行和恢复故障
- 根据候选差距决定估算、精算或核验深度
- 为卡题预设换入口、基础法和跳过路径
- 结合资格、地域、家庭和长期成本分析选岗
- 核验官方账号、假号、搬运与资料授权状态

## 安装

在 Codex 中直接说：

```text
安装这个 Skill：https://github.com/tyf152119-web/wangyou-honglingjin-perspective/tree/main/skills/wangyou-honglingjin-perspective
```

也可以使用 Codex 自带的 Skill Installer：

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo tyf152119-web/wangyou-honglingjin-perspective \
  --path skills/wangyou-honglingjin-perspective
```

Windows PowerShell：

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" `
  --repo tyf152119-web/wangyou-honglingjin-perspective `
  --path skills/wangyou-honglingjin-perspective
```

安装后在下一轮对话中使用。

## 使用示例

```text
用网友红领巾的方法帮我复盘这次模考。
```

```text
红领巾会怎么看我这两个岗位的取舍？
```

```text
这个“网友红领巾”账号是本人吗？
```

一般公考知识问题不会自动触发人物视角；需要明确说“网友红领巾视角”“红领巾会怎么看”或类似指令。身份、假号和授权问题会进入中性的事实核验模式，不扮演本人。

## 研究与验证

- 336 个视频/分 P 记录，315 个唯一 BVID
- 249 条有字幕，87 条无字幕
- 4 条关键决策视频 ASR，2 条代表性模考/录屏抽样
- 12 个关键决策案例
- Nuwa 质量检查 6/6 PASS
- Skill Creator 验证通过
- 已知立场、边缘风格、触发路由与域外防漂移测试通过

详细审计见 [`docs/validation/`](docs/validation/)。

## 来源边界

确认的本人公开账号只有：

- [B 站 UID 21969231](https://space.bilibili.com/21969231/)
- [微博 UID 1187051904](https://weibo.com/u/1187051904)

微博内容主要与 B 站重复，不重复计入方法证据。抖音同名或近似名账号不属于本人。未核实授权的站外资料只标为“非本人聚合/授权状态未核实”。

仓库不包含原视频、音频、整包字幕、ASR 全文或临时下载地址。详细说明见 [`SOURCE_DATA.md`](skills/wangyou-honglingjin-perspective/references/SOURCE_DATA.md)。

## 免责声明

这是根据公开资料制作的独立研究型 Skill，不是网友红领巾本人或其授权分身，也不能代表本人对新问题的真实意见。涉及当年政策、岗位资格和招录规则时，必须核验最新官方文件和招录单位答复。

## License

本仓库自行创作的代码、Skill 指令和研究文本采用 [MIT License](LICENSE)。第三方名称、平台内容和原始材料不因此获得重新许可，详见 [NOTICE](NOTICE.md)。
