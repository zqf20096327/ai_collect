# 阿杭 Skills

阿杭的公开 Skills 合集，围绕 AI 应用、自媒体创作和思考决策，把实际工作中的方法整理成可复用的 Agent 工作流。

阿杭是产品经理出身的商人，也从事 AI 内容创作。这里既有帮助表达需求、梳理思路的方法类 Skill，也有写作、素材处理和视频制作工具。每个 Skill 的适用平台、依赖和成熟度分别说明，按需要选择安装。

## 从你的需求开始

| 方向 | 想完成什么 | Skill | 形态与边界 |
|---|---|---|---|
| AI 应用 | 把模糊需求说清楚，形成可直接使用的提示词 | [ah-clarify-task-intent](skills/ah-clarify-task-intent/README.md) | 纯文本工作流；提供导入包 |
| 自媒体创作 | 让 Gemini 润色中文口播，保留事实和原意 | [ah-gemini-script-polisher](skills/ah-gemini-script-polisher/README.md) | 试用；依赖 Codex 与 Gemini 官网操作能力 |
| 自媒体创作 | 获取自有或已获授权的抖音视频素材 | [ah-douyin-clean-downloader](https://github.com/ahang008/ah-douyin-clean-downloader) | 独立仓库；环境与使用边界见该仓库 |
| 自媒体创作 | 按不同观众问题重组长口播，形成切片候选 | [ah-longform-clip-matrix](https://github.com/ahang008/ah-longform-clip-matrix) | 独立仓库；保留来源时间映射与验收状态 |
| 自媒体创作 | 从视频、时间戳逐字稿和审核区间生成剪辑产物 | [ah-talking-head-edit](skills/ah-talking-head-edit/SKILL.md) | 试用；自有 JSON 工程、MP4 和 SRT，不支持剪映原生工程 |
| 自媒体创作 | 编排 AI 博主系列的剪辑、字幕与封面流程 | [ah-ai-blogger-video](skills/ah-ai-blogger-video/README.md) | 系列入口；剪辑与封面依赖另装 |
| 自媒体创作 | 编排减肥系列的口播视频制作流程 | [ah-weightloss-video](skills/ah-weightloss-video/README.md) | 系列入口；剪辑引擎与模板另行准备 |
| 思考与决策 | 澄清目标、权衡取舍、检查条件与反馈 | [ah-think](https://github.com/ahang008/ah-think) | 独立仓库；试用 MVP |

需求表达问题从 `ah-clarify-task-intent` 开始；目标与取舍问题从 `ah-think` 开始。两者分别帮助你把任务说明白、把选择想清楚。

## 选择安装方式

### Codex

将具体 Skill 的地址交给 Codex，例如：

```text
请安装 https://github.com/ahang008/ah-skills/tree/main/skills/ah-clarify-task-intent 中的 Skill，连同 references 一起保留。只安装这个 Skill，遇到已有同名版本先说明差异。
```

安装后在新对话中调用 `ah-clarify-task-intent`。也可以将完整目录放入 Codex 的用户 Skills 目录；具体安装方式和依赖以对应 Skill 的说明为准。

### Claude Desktop

意图澄清 Skill 提供 [ZIP 导入包](packages/ah-clarify-task-intent.zip)。下载后，在 Claude Desktop 的“自定义 / Skills / 添加 Skill / 上传 Skill”中导入，检查启用状态。若已安装原名 `clarify-task-intent`，请选择一个版本启用，避免重复匹配。

该导入路径已用原名版本验证；公开版的名称和打包内容见 [使用说明](skills/ah-clarify-task-intent/README.md)。其他 Skill 含有不同的平台依赖，不能仅凭文本格式相同就判断可在 Claude Desktop 运行。

## 收录与维护

- 本仓库是统一目录，普通 Skill 默认放在 `skills/<skill-name>/`；已有独立仓库保留，由本页链接到各自的维护入口。
- 需要独立版本管理、较多运行依赖或独立维护周期时，再考虑拆分仓库，不要求每个新 Skill 单独建库。
- 新发布的自有 Skill 使用 `ah-` 前缀。只收录明确选择公开且有权分发的内容，不自动同步本机安装目录或私人素材。
- 方法类 Skill 可以只有指令和参考材料；工具类 Skill 按实际需要提供脚本及验证。系列入口需明确哪些能力由外部依赖提供。
- “试用”表示仍需结合具体场景验证；格式检查通过、导入成功和任务效果验证是不同状态。

贡献方式见 [CONTRIBUTING.md](CONTRIBUTING.md)，来源与依赖见 [PROVENANCE.md](PROVENANCE.md) 和 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

## 使用许可

本仓库采用 [AH Source Available Non-Commercial License 1.0](LICENSE)，属于源码可见的非商业许可。个人、教育和研究等非商业用途按许可使用；商业用途需要事先获得书面授权。独立仓库和第三方依赖分别遵循各自的许可，合集中的链接不改变其授权范围。

## 关于与联系

阿杭分享 AI 应用和自媒体实践，也接受相关产品合作与商业授权咨询。

- [X](https://x.com/Astronaut_1216)
- [个人网站](https://zephyr8.asia)
- 合作联系：微信 zephyr136；邮箱 a1165094791@gmail.com。

功能问题可提交 [Issue](https://github.com/ahang008/ah-skills/issues)。涉及隐私或漏洞的问题，先阅读 [安全说明](SECURITY.md)，不要公开提交敏感内容。
