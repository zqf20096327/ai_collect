<!-- 本文件由 scripts/build.py 生成，请勿手改。要改内容请编辑 data/ 或 templates/ 后重新生成。 -->

# Awesome Story Skills · 让大模型讲好故事

**中文** · [English](README.en.md)

> 能直接装、直接用的大模型讲故事开源工具，不是论文清单：skill、agent 框架、应用，以及放出了代码的研究。小说、网文、短篇、剧本、互动叙事、同人仿写，以及把真实事件写得像小说一样好看的非虚构叙事，都收。
>
> Ready-to-use open-source tools for LLM storytelling, not a paper list: agent skills, harnesses, apps and research with released code, for novels, short stories, scripts, interactive fiction, fan fiction and narrative nonfiction.

这里只收一类项目：故事主要由大模型写出来，项目本身提供的是讲故事的方法或原则，比如怎么先规划再写、怎么让长篇不吃书、怎么让多个 agent 分工审稿、怎么学一部作品的写法、怎么把一条新闻写成有悬念又不编造事实的故事。下载、发布、翻译、通用润色、标题模板这些周边工具不收。

每个项目都按故事类型归类，并标出它用了哪些方法。[方法指南](METHODS.md)把这些方法逐一讲清楚：解决什么问题、常见做法、取舍和坑、从哪里开始。

**让 agent 帮你挑**：`npx skills add UnderleveledBuilder/awesome-story-skills` 装上 storytelling-methods skill，然后直接说「我要写 300 章修仙，帮我挑方法」。机器可读的完整索引在 [catalog.json](catalog.json)。

收录 819 个项目：335 个 skill 和提示词、462 个框架和应用、22 个研究代码 · 元数据更新于 2026-10-26

**图例**：🌟 精选 · 📝 提示词 · ⚙️ 框架 · 🧩 应用 · 🎓 研究代码 · 💤 超过 180 天未更新 · 📦 已归档 · ⚠️ 仓库失效

> [!NOTE]
> 「人工核对」指核对过仓库说明、目录结构和分类，不等于实测过写作效果。skill 和应用可能附带脚本，安装前请先读一遍说明。

## 目录

- [本周新增](#new)（0）
- [精选：从这里开始](#featured)（26）
- [按故事类型](#by-group)
  - [长篇小说 · 网文](#group-novel)（357）
  - [短篇 · 故事](#group-short)（41）
  - [剧本 · 短剧 · 影视](#group-script)（84）
  - [互动叙事 · 游戏 · 角色扮演](#group-interactive)（199）
  - [仿写 · 同人 · 风格迁移](#group-imitation)（28）
  - [非虚构叙事](#group-nonfiction)（65）
  - [通用叙事方法](#group-general)（45）
- [按创作方法查找](#by-method)
- [相关资源](#resources)
- [收录徽章](#badge)

<a id="new"></a>
## 本周新增

本周暂无新增。发现好项目欢迎[推荐](../../issues/new?template=submit-skill.yml)。

<a id="featured"></a>
## 精选：从这里开始

每种故事类型里方法最扎实、最有代表性的项目，第一次来可以先看这些。

- [inkos](https://github.com/Narcooo/inkos) ★10.8k · 长篇小说 · 网文：统一 harness 管长短篇、剧本、同人仿写、互动影游；长篇用 truth files 记设定、伏笔和角色状态，每章写后审计→修订→状态回写
- [zenstory-ai/oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode) ★8k · 长篇小说 · 网文：扫榜找题材、拆爆款提节奏与素材，再按细纲逐章写；设定、大纲、追踪分文件落盘，状态卡分开作者真相与读者已知，写后脚本查 AI 句式
- [webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) ★7.7k · 长篇小说 · 网文：Claude Code 长篇网文插件：分阶段初始化设定与总纲、拆卷纲章纲，写章后多维审查并把事实提交进状态库与 RAG，可查伏笔角色，附只读面板
- [AI_NovelGenerator](https://github.com/YILING0013/AI_NovelGenerator) ★6.3k · 长篇小说 · 网文：本地部署的长篇小说生成应用：用雪花法从核心创意逐级展开卷、弧、场景、章纲到正文，管理角色/势力/物品/伏笔状态，AI 流程可在画布上改
- [NousResearch/autonovel](https://github.com/NousResearch/autonovel) ★1.6k · 长篇小说 · 网文：仿 autoresearch 的改—评—留弃循环：设定、人物、大纲、文风、canon 打分过阈值，逐章起草评分重写，再经对抗删改、读者评审团和 Opus 审稿
- [RecurrentGPT](https://github.com/aiwaves-cn/RecurrentGPT) ★1k · 长篇小说 · 网文：用自然语言模拟 LSTM：每步写一段正文和下一段计划，改写短期记忆，段落摘要存入可语义检索的长期记忆；人可选改计划共写任意长度小说
- [neuro-book](https://github.com/notnotype/neuro-book) ★753 · 长篇小说 · 网文：长篇写作 IDE：时间线切面事件溯源推算世界状态，伏笔承诺账本，leader/writer 等多 agent 分工写章，llmlint 规则查 AI 味
- [lengdu](https://github.com/asass-11/lengdu) ★43 · 短篇 · 故事：中文短篇创作与冷读：先写完正文，再由独立校准 Agent 和全新读者 Agent 首读，检验看懂、流畅、好看
- [screenwriting-skills](https://github.com/jtydhr88/screenwriting-skills) ★1.8k · 剧本 · 短剧 · 影视：从 47 本编剧书与 23 卷剧本蒸馏 26 个 skill：结构、Truby、场景、对白、剧集圣经、编剧室与改编，附中美日韩法剧作和戏曲案例
- [short-drama](https://github.com/0xsline/short-drama) ★1.5k · 剧本 · 短剧 · 影视：短剧编剧 skill：选题立项→故事骨架→角色与四层反派→分集目录（钩子、付费卡点）→逐集写剧本→五维评分审查→合规审核
- [dramatron](https://github.com/google-deepmind/dramatron) ★1.1k · 剧本 · 短剧 · 影视：从一句 logline 层级展开：先生成标题、人物、情节节拍和地点描述，再逐场生成对白，作者可在每一层编辑重写
- [Marinara-Engine](https://github.com/Pasta-Devs/Marinara-Engine) ★739 · 互动叙事 · 游戏 · 角色扮演：角色扮演与游戏引擎：AI 游戏主持带队伍/任务/战斗，可按需安装叙事导演、连续性检查、世界状态与关系追踪、长期记忆、Lorebook 维护等代理
- [OpenStory](https://github.com/ZJU-LLMs/OpenStory) ★434 · 互动叙事 · 游戏 · 角色扮演：多智能体故事世界推演框架：角色按感知→计划→执行→反思插件自主行动演出剧情，玩家可下指令、回溯分支；WorldKernel 一句话生成角色、地点与规则
- [AI4VisualNovel](https://github.com/ttsmallHot/AI4VisualNovel) ★101 · 互动叙事 · 游戏 · 角色扮演：视觉小说多 agent 框架：制片、编剧、演员、美术分工，先出大纲再生成拓扑排序的 DAG 分支剧情图，演员 agent 按人设演对白并审立绘，导出可玩游戏
- [Sonder_Engine](https://github.com/N0819/Sonder_Engine) ★59 · 互动叙事 · 游戏 · 角色扮演：互动小说引擎：导演裁定客观因果，感知层决定每个角色能知道什么，角色代理只凭私有记忆行动，叙述者只写玩家可见部分，再统一提交状态
- [harnessNovel](https://github.com/XTmingyue/harnessNovel) ★198 · 仿写 · 同人 · 风格迁移：先对参考小说分三阶段拆书（结构、世界观、情节单元、文风），把情节抽象成叙事模式，再按核心玩法→舞台路线→章纲→正文仿写，章节级去 AI 味
- [longzu.skillls](https://github.com/zuoyou12/longzu.skillls) ★11 · 仿写 · 同人 · 风格迁移：江南、烽火戏诸侯文风蒸馏 skill：全文统计 1465 万字语料加等距精读，得出共享叙事骨架和可替换语言皮肤，支持风格杂交，附审计脚本和盲测
- [director](https://github.com/s1dashu/director) ★826 · 非虚构叙事：动画解说模式先定中心问题，按钩子、背景、矛盾、概念、误读、回答组织讲稿，区分事实与解读、不编造动机和对白，再做人物、分镜和视频生成
- [data2story-skill](https://github.com/QinghongLin/data2story-skill) ★158 · 非虚构叙事：数据新闻 agent：侦探查背景、分析师跑代码出发现、编辑定故事主线与钩子–证据–转折结构，再出图写 HTML，每句话标注并校验到数据或出处
- [good-story](https://github.com/Rimagination/good-story) ★141 · 非虚构叙事：科研叙事 skill：从结果、图表和草稿里找出张力和主线，按证据链重排图序，输出故事卡和证据地图，按领域校准证据强度，查因果和普遍性有没有说过头，模拟审稿人
- [Writingbook-AgenticWorkflow](https://github.com/idoforgod/Writingbook-AgenticWorkflow) ★29 · 非虚构叙事：AI 自传流水线：McAdams/Kvale 式 12 轮访谈→故事圣经（情感弧+起承转合）→逐章写并混合作家文风→对抗审稿+CoVe 事实核查→跨章一致性审计
- [aletheia](https://github.com/mycyg/aletheia) ★8 · 非虚构叙事：文章、论文转纪录片：先建证据账本把主张和引文绑定出处，提 2–3 个叙事方向，按「张力→证据→解释→后果」因果链写旁白与逐镜分镜，确认后才生成素材
- [sepia](https://github.com/Nanako0129/sepia) ★3.5k · 通用叙事方法：按 StoryScope 论文测出的 AI 小说结构特征分三遍修：先改叙事架构（不点题、松因果链、后置揭示），再改段落流和表层措辞
- [WriteHERE](https://github.com/principia-ai/WriteHERE) ★974 · 通用叙事方法：异构递归规划：把写作任务动态拆成检索、推理、撰写三类子任务，边分解边执行并按上下文调整，小说与长报告共用一套引擎
- [creative-writing-skills](https://github.com/haowjy/creative-writing-skills) ★541 · 通用叙事方法：muse 主代理调度头脑风暴、角色模拟、大纲、写手、批评、编辑和读者模拟等子代理，从已有文字提炼文风文件，写后批评修订并同步知识库
- [doc-story-generation](https://github.com/yangkevin2/doc-story-generation) ★161 · 通用叙事方法：DOC：先生成前提和多层细纲（重排器挑大纲顺序、检测人物），再按细纲逐段写正文并用控制器保持贴合大纲，产出 3500+ 词长故事

<a id="by-group"></a>
## 按故事类型

<a id="group-novel"></a>
### 长篇小说 · 网文

长篇连载的写作系统：开书、大纲、分章写作、长篇记忆、审稿。

#### skill · 提示词（138）

- 🌟 **[zenstory-ai/oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode)** · ★ 8k<br>扫榜找题材、拆爆款提节奏与素材，再按细纲逐章写；设定、大纲、追踪分文件落盘，状态卡分开作者真相与读者已知，写后脚本查 AI 句式<br><sub>方法：规划 · 记忆 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-10-23 · 中文 · 13 个 skill · MIT</sub><br><sub>💡 同团队另有 DeepSeek Harness 版 oh-story-dsh</sub>

- 🌟 **[webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer)** · ★ 7.7k<br>Claude Code 长篇网文插件：分阶段初始化设定与总纲、拆卷纲章纲，写章后多维审查并把事实提交进状态库与 RAG，可查伏笔角色，附只读面板<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-10-24 · 中文 · 8 个 skill · GPL-3.0</sub><br><sub>💡 master 为 Claude Code 版，新功能在 v8 分支（DeepSeek Harness）</sub>

- **[PenglongHuang/chinese-novelist-skill](https://github.com/PenglongHuang/chinese-novelist-skill)** · ★ 4.3k<br>从零生成 10–50 章中文小说：三层问答、创作记忆、每章悬念钩子、自动校验<br><sub>方法：规划 · 理论 · 修订</sub><br><sub>更新于 2026-10-20 · 中文 · MIT</sub>

- **[Chinese-WebNovel-Skill](https://github.com/Tomsawyerhu/Chinese-WebNovel-Skill)** · ★ 924<br>网文写作 skill：主路由分派到开头、转场、对白、章末、剧情逻辑、人物一致性、卷纲、去 AI 味等 10 个模块，写前检索本地语料范例<br><sub>方法：规划 · 修订 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-08-28 · 中文</sub><br><sub>💡 README 未写安装方式：SKILL.md 在仓库根目录，把整个仓库放进 skills 目录即可；附 166 篇短篇语料约 11MB，检索脚本需 Python 3</sub>

- **[Openwrite](https://github.com/LiPu-jpg/Openwrite)** · ★ 883<br>DeepSeek Harness 长篇小说插件：统一创作 Agent 加 90 个小说工具，人物、设定、大纲、伏笔存本地，章节走标准审稿 DAG 与去 AI 味<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-23 · 中文 · 25 个 skill · Apache-2.0</sub><br><sub>💡 需 DeepSeek Harness（dsh）宿主；preset 内含 oh-story-deslop / long-write / review 等 skill，疑似取自 zenstory-ai/oh-story-claudecode</sub>

- **[awesome-novel-agent](https://github.com/modoojunko/awesome-novel-agent)** · ★ 839<br>总控 agent 按状态文件逐个派 8 个子 agent：卷纲→章纲场景卡→提示词组装→正文→Gate A-F 去 AI 味（不过就重写）→归档更新设定<br><sub>方法：规划 · 记忆 · 多智能体 · 去 AI 味</sub><br><sub>更新于 2026-09-25 · 中文 · AGPL-3.0</sub><br><sub>💡 名字带 awesome，但它是创作 agent，不是列表；README 写明个人免费、商用需联系作者授权（仓库许可证为 AGPL-3.0）</sub>

- **[novel-creator-skill](https://github.com/leenbj/novel-creator-skill)** · ★ 697<br>每章强制五步门禁（记忆同步→一致性→风格校准→校稿→脚本），配 RAG 回读、知识图谱、进度配额、跨 agent 交叉审稿与事件冷却，两遍去 AI 味<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-03-10 💤 · 中文</sub><br><sub>💡 最后更新 2026-03-10，因 682★ 收录；去 AI 味润色基于 blader/humanizer 方法论</sub>

- **[oh-story-dsh](https://github.com/zenstory-ai/oh-story-dsh)** · ★ 612<br>把 Oh Story 小说技能装进 DeepSeek Harness：加了文件树、编辑器、Chat 三栏的小说工作台，另带短剧、小说改游戏、视频解说工作台<br><sub>方法：规划 · 记忆 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-10-19 · 中文 · 38 个 skill · MIT</sub><br><sub>💡 基于同团队的 zenstory-ai/oh-story-claudecode（打包的 Oh Story 0.8.5，小说技能文件与原版相同）和 novel-to-game，另加 DSH Web 工作台界面和短剧、视频解说技能。只能在 DeepSeek Harness 里用，需要 Node.js 24+；Claude Code 用户用原版</sub>

- **[Novel-Control-Station-Skill](https://github.com/jingtai123/Novel-Control-Station-Skill)** · ★ 432<br>开书访谈后先出完整大纲与人物档案，按真值文档逐章生成控制卡再写，章后回写人物/关系/伏笔/情绪债务等动态状态，按需加载风格模块并三步去 AI 味<br><sub>方法：规划 · 记忆 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-03-29 💤 · 中文 · MIT</sub><br><sub>💡 最后更新 2026-03-29，因 424★ 收录；附 Codex 连续创作（马拉松）PowerShell runner 模板；作者称已用其写起点连载</sub>

- **[story-skills](https://github.com/danjdewhurst/story-skills)** · ★ 352<br>人物、伏笔、连续性状态都写成带 frontmatter 的 Markdown，CLI 像编译器查死人复出、兑现早于铺垫等矛盾；24 个 skill 从构思到投稿<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-10-20 · 英文 · 24 个 skill · MIT</sub>

- **[wordflowlab/novel-writer-skills](https://github.com/wordflowlab/novel-writer-skills)** · ★ 268<br>Claude Code 斜杠命令加 Skills：宪法→规格→澄清→计划→任务→写作→分析七步写小说，类型知识和一致性检查自动激活，追踪情节、时间线和关系<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2025-10-20 💤 · 中文 · 13 个 skill · MIT</sub><br><sub>💡 跨平台版是 wordflowlab/novel-writer；2025-10 后没再更新，按 265★ 且被多个派生项目沿用收录</sub>

- **[novel-writing-framework](https://github.com/LAY-lgtm/novel-writing-framework)** · ★ 266<br>五份网文写作方法论：通用长篇流程、番茄快节奏、起点慢热、智斗权谋专项、完稿改良诊断，含三章一轮自检和 AI 指纹量化指标<br><sub>方法：规划 · 理论 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-05-31 · 📝 提示词 · 中文 · MIT</sub><br><sub>💡 每份是单独的 .md，需自己放进 skills 目录或手动加载</sub>

- **[Lorn.NovelWriteSkills](https://github.com/lornshrimp/Lorn.NovelWriteSkills)** · ★ 244<br>先把作者文风、作品蓝本、题材研究蒸馏成模板，再走大纲→章节控制卡→正文→审阅去 AI 味闭环；母稿再改写成 13 个平台版本，跑字数和相似度门禁<br><sub>方法：规划 · 修订 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-09-04 · 中文 · 350 个 skill</sub><br><sub>💡 README 只写了 VS Code + GitHub Copilot 用法（.github/skills、.github/prompts 结构）；约 350 个 SKILL.md 也可单独复制到其他 agent；仓库约 22MB，大部分是写作研究资料</sub>

- **[webnovel-writer-opencode](https://github.com/lujih/webnovel-writer-opencode)** · ★ 223<br>webnovel-writer 的 OpenCode 增强版：三层 RAG 组上下文，故事合约约束设定，伏笔债务追踪，6 维审查，借鉴 inkOS 做事件溯源<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-10-21 · 中文 · 16 个 skill · GPL-3.0</sub><br><sub>💡 基于 lingfengQAQ/webnovel-writer，另加 8 个 skill：批量写章、重写、修复、删除、导出（EPUB/DOCX/PDF 等）、番茄风和七猫风写作约束、自动发布到番茄；v2.8 起借鉴 inkos 的事件溯源设计。用 npx @cszx/webnovel-writer-opencode init 安装，Claude Code 用户直接用原版</sub>

- **[sumeru](https://github.com/xindoo/sumeru)** · ★ 216<br>网文全流程 7 个 skill：选题（含榜单分析）→世界观大纲→章节批量撰写→时间线/OOC 审查→润色→多平台导出，可断点续写<br><sub>方法：规划 · 设定 · 修订</sub><br><sub>更新于 2026-08-23 · 中文 · 7 个 skill</sub>

- **[Distilled-Novel-Toolbox](https://github.com/dama-cyber/Distilled-Novel-Toolbox)** · ★ 192<br>网文写作知识库 13 个 skill：题材、人设、世界观、节奏、爽点、情绪、文风、商业化、合规、润色去 AI 味与 AIGC 检测应对<br><sub>方法：理论 · 设定 · 人物 · 去 AI 味</sub><br><sub>更新于 2026-06-09 · 中文 · 13 个 skill</sub><br><sub>💡 README 未写安装方式：把各 novel-* 目录复制到 agent 的 skills 目录即可；每个模块附 test-prompts.json</sub>

- **[novel-kit](https://github.com/t59688/novel-kit)** · ★ 162<br>规范驱动的 40+ 条 /novel 斜杠命令：先建「小说宪法」与 Writer 风格配置，管理角色/地点/势力/伏笔，章节按规划→撰写→审查→润色→确认推进<br><sub>方法：规划 · 设定 · 记忆 · 修订</sub><br><sub>更新于 2025-12-22 💤 · 中文</sub><br><sub>💡 最后更新 2025-12-22，因 162★ 收录；需配合 novel-kit CLI 初始化项目</sub>

- **[awesome-novel-studio](https://github.com/MJbae/awesome-novel-studio)** · ★ 159<br>先出 3 份提案，再做世界观、带语气表的角色卡和 25 集节拍设计；写每集前汇总前两集时间线与伏笔，写后 6 个代理并行做 16 轴润色<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-04-14 💤 · 英文 · 10 个 skill · Apache-2.0</sub>

- **[tianming-skill](https://github.com/zy-zmc/tianming-skill)** · ★ 157<br>长篇协同创作指令系统：用五份知识库约束世界观与人物，按「天命：大纲/目录/正文/体检/存档」逐步推进<br><sub>方法：规划 · 设定 · 记忆 · 风格</sub><br><sub>更新于 2026-06-06 · 中文</sub><br><sub>💡 CC BY-NC-SA 4.0 非商用许可；README 同时推广作者的同名桌面软件</sub>

- **[book-genesis-studio](https://github.com/felipelobomotta-blip/book-genesis-studio)** · ★ 151<br>整本书写作 skill：立项简报→人物、章节计划与事实账本→逐章起草，盲读模拟读者评首章、每 5 章查连续性，审计加十项量表限次修订<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-10-09 · 英文 · 4 个 skill · MIT</sub><br><sub>💡 按用户所用语言写作；附 32 章葡语样书，评分为自评</sub>

- **[novel-harness](https://github.com/manhai934/novel-harness)** · ★ 131<br>网文陪写 harness：开书规划，把章节拆成作者自己填的写作块，审稿去 AI 味，维护角色状态、伏笔和章节摘要<br><sub>方法：规划 · 记忆 · 去 AI 味 · 共创</sub><br><sub>更新于 2026-08-06 · 中文 · 6 个 skill</sub><br><sub>💡 附本地 Studio Dashboard（需 Python + Node）；可选知识包从作者服务器（阿里云 OSS）下载 zip</sub>

- **[Claude-Book](https://github.com/ThomasHoussin/Claude-Book)** · ★ 126<br>多 agent 写小说：只读 bible 加按章版本化 state，规划→写作→文风/人物/连续性三审循环≤3 轮，用本地小模型困惑度改写降 AI 痕迹<br><sub>方法：记忆 · 多智能体 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-01-22 💤 · 英文 · 4 个 skill · MIT</sub><br><sub>💡 perplexity-improver 需约 16GB 显存跑 Ministral-3-8B；book-analyzer 可从源书拆出 bible</sub>

- **[Jieice/ai-novel-writer](https://github.com/Jieice/ai-novel-writer)** · ★ 120<br>网文 skill 套装：开书建项目出大纲人设，拆参考书学文风，毒点检测与冲突设计，写完同步降重并更新项目文件，另有 90 年代乡土、港综专用写作器<br><sub>方法：规划 · 理论 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-04-22 💤 · 中文 · 17 个 skill</sub><br><sub>💡 整理自 Linux.do 用户 user2609 分享的流程，README 写安装到 Trae；仓库是作者工作目录，混有具体作品、参考小说原文、网页存档、BypassAIGC 降重和番茄自动发布脚本</sub>

- **[ani-book-skill](https://github.com/ExplosiveCoderflome/ani-book-skill)** · ★ 107<br>故事发动机→卷/章计划→单章正文→修订审查→连续性回灌，事实和伏笔验收后才进长期状态；拆书笔记可按章接入上下文，支持同人续写与跨书设定复用<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-10-15 · 中文 · Apache-2.0</sub>

- **[novel2agent-jp](https://github.com/kgmkm/novel2agent-jp)** · ★ 107<br>日语小说 skill：企划、世界观、角色、情节写进 TOML 并用脚本校验，编辑和作家分工执笔，再让多个 LLM 从逻辑、文体、考据、读者视角交叉推敲<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-09-25 · 日文 · MIT</sub><br><sub>💡 旧名 novel2hermes_jp；也支持 Hermes、goose；附 40 多项的角色表、插图提示词和 pixiv/カクヨム 投稿格式转换</sub>

- **[akira399/dsh-novel-writer](https://github.com/akira399/dsh-novel-writer)** · ★ 103<br>九阶段门禁（选题→设定→人设→大纲→分卷→细纲→正文→修订→完本），世界书关键词注入，事实账本与伏笔/时间线追踪，三层上下文包，附去 AI 味<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-06 · 中文 · MIT</sub><br><sub>💡 DeepSeek Harness 插件，需 DSH 0.2.0-rc.2+；可导入导出 SillyTavern 世界书；另有黄金三章诊断、市场调研与模板复制</sub>

- **[long-novel-writer](https://github.com/jiaw-Zh/long-novel-writer)** · ★ 93<br>百万字长篇写作 skill：六层摘要冻结、实体档案、正典账本与 POV 知识边界，写后双 agent 校验，防止设定漂移<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-06-18 · 中文</sub><br><sub>💡 思路来自桌面项目 AI_NovelGenerator；作者另有早期版 jiaw-Zh/long-novel-generator</sub>

- **[chinese-webnovel-skills](https://github.com/tance-mang/chinese-webnovel-skills)** · ★ 90<br>按「平台+频道+题材」参数套用起点/番茄的爽点、打脸四拍和追读节奏，30+ 技能覆盖选题、大纲、金手指、扩写、追读诊断、连贯检查、去 AI 味<br><sub>方法：规划 · 理论 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-06-13 · 中文 · 33 个 skill · MIT</sub><br><sub>💡 另有接自有 API 的终端 CLI 版；含一个短剧剧本技能</sub>

- **[padwriter](https://github.com/cheyann4399/padwriter)** · ★ 85<br>节拍写作 skill：收件箱想法自动分级入 L1/L2/L3 设定库，按卷梗概→节拍索引→分镜卡→设定合规校验→初稿→AI 痕迹自检→洁本出章<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-09-04 · 中文</sub><br><sub>💡 仓库只含 skill；同名安卓语音写作 App 只有 APK（Releases），需向作者要测试 Key</sub>

- **[book-writer](https://github.com/tobyilee/book-writer)** · ★ 83<br>Claude Code 写书 harness：调研→计划审批→最多 4 写手并行写章，小说档案由连续性守护维护故事圣经、伏笔与节奏报告，验收后出 EPUB<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-10-19 · 韩文 · 15 个 skill · MIT</sub><br><sub>💡 韩语；默认是技术书档案，v1.3 起加入小说/实用书/随笔文体档案</sub>

- **[fanqie-novel-skill](https://github.com/304769384-png/fanqie-novel-skill)** · ★ 80<br>番茄长篇写作 skill：写前读状态文件，写后去 AI 味并跑 8 项最小审计（字数、因果链、战斗、对话占比、话疗、循环等）<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-06-03 · 中文</sub><br><sub>💡 工作流和状态文件（current_state、pending_hooks、character_matrix 等）沿用 Narcooo/inkos，另加番茄平台规则、商业审查和战斗/对话/话疗/循环审计</sub>

- **[DaisyWriter](https://github.com/ricky-theseus/DaisyWriter)** · ★ 76<br>在 webnovel-writer 的开书/规划/写章/审查流程上加扫榜、拆书、批量写、设定审查与去 AI 味，另有中短篇开书→写作→审查流水线<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-07-08 · 中文 · 23 个 skill · GPL-3.0</sub><br><sub>💡 基于 lingfengQAQ/webnovel-writer（init/plan/write/review 等 8 个），另加扫榜、拆书、批量写、设定审查、去 AI 味、中短篇 5 个 skill 和封面生成；番茄发布取自 amm10090/fanqie-publisher-skill；另含技术博客/公众号/小红书技能</sub>

- **[chinese-longnovel-skill](https://github.com/xiaofeng-928/chinese-longnovel-skill)** · ★ 75<br>中文长篇网文工作流：扫榜开书、范文拆解与文风蒸馏、每 50 章分阶段细纲、事实锁与状态仓库、伏笔追踪、双审查自动修复<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-09-12 · 中文 · MIT</sub><br><sub>💡 校验脚本需 Python 3；自然化环节内置 Humanizer-zh 规则（已注明来源）</sub>

- **[dreampowers](https://github.com/skyfiredao/dreampowers)** · ★ 74<br>OpenCode 中文小说技能包：14 个 skill，覆盖构思、七维文风问卷、设定文件隔离、大纲伏笔、分场景写作、冷读与一致性审查<br><sub>方法：规划 · 设定 · 修订 · 风格</sub><br><sub>更新于 2026-07-02 · 中文 · 14 个 skill · GPL-3.0</sub><br><sub>💡 依赖 oh-my-openagent；成人场景技能为选装（install.sh --all 才装）</sub>

- **[book-os](https://github.com/forsonny/book-os)** · ★ 72<br>Novel-OS：写作标准（文风、类型指南、叙事技巧）、小说层（前提、计划、决策）、稿件层（大纲、人物档案、逐场景任务）三层上下文引导 AI 写<br><sub>方法：规划 · 理论 · 记忆 · 风格</sub><br><sub>更新于 2025-08-18 💤 · 英文 · MIT</sub>

- **[qin1473692580-ux/oh-story-claudecode](https://github.com/qin1473692580-ux/oh-story-claudecode)** · ★ 69<br>oh-story 派生版：扫榜拆文建模块库再写长短篇，正文落盘后过语言门、错别字门、AI 味与跨章连续性守卫，另加后台数据诊断、资料考证和发布<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-09-01 · 中文 · 18 个 skill · MIT</sub><br><sub>💡 基于 zenstory-ai/oh-story-claudecode，2026-08 起独立演进、不同步上游；另加 story-data-analyze、story-research、story-explore、story-release-package、story-publish 五个 skill，以及错别字门禁、新题材包、TRAE/WorkBuddy 适配</sub>

- **[ai-fiction-writer](https://github.com/Wooooooooood/ai-fiction-writer)** · ★ 66<br>十个 skill 分管拆文、大纲、角色卡、知识库与世界地图；写前查逻辑矩阵、知情边界和冻结状态防穿帮，写后 9 维去 AI 味评分并四视角审稿<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-10 · 中文 · 10 个 skill · MIT</sub><br><sub>💡 README 只写了克隆仓库，需自行把「纯净版skill/」下各目录放进 agent 的 skills 目录</sub>

- **[The-Crucible-Writing-System-For-Claude](https://github.com/forsonny/The-Crucible-Writing-System-For-Claude)** · ★ 61<br>史诗奇幻长篇插件：问卷生成 9 份规划文档，按 36 拍 Crucible 结构（任务/内火/羁绊三线交织）出章纲，逐场景写作并对照规划防幻觉，每两章自动审稿<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2025-12-21 💤 · 英文 · 4 个 skill · MIT</sub><br><sub>💡 作者自创的 Crucible 结构；Claude Code 插件市场安装；2025-12 后未更新，因结构理论独特而收；存在恶意仿冒仓库 pasteurmonga/The-Crucible-Writing-System-For-Claude，认准本仓库</sub>

- **[dsh-cuigengji-plugin](https://github.com/mistnest/dsh-cuigengji-plugin)** · ★ 54<br>DSH 小说工作台：按卷章写正文，角色卡/世界书/关系图和节点式情节规划图作为 AI 可查可改的案头资料，按需检索后讨论、续写、改稿<br><sub>方法：规划 · 设定 · 记忆 · 共创</sub><br><sub>更新于 2026-10-21 · 中文 · 6 个 skill · MIT</sub><br><sub>💡 DeepSeek Harness 插件，主要适配 DSH Windows 桌面版；可导入酒馆角色卡、世界书与提示词预设</sub>

- **[ultimate-novel-creation-skill](https://github.com/Fly143/ultimate-novel-creation-skill)** · ★ 51<br>立项→世界观人设→滚动章节规划→单章写作；每章强制跑写后流水线：更新圣经与摘要、金手指/时间/叙事线约束检查、读者审稿、朱雀检测对策，缺步不准写下一章<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-22 · 中文</sub><br><sub>💡 须先把 system_prompt.md 配成宿主的系统提示词，流程才会被严格执行；写后流水线内置朱雀 AIGC 检测对策</sub>

- **[AI-Practical-Lab/novel-writer](https://github.com/AI-Practical-Lab/novel-writer)** · ★ 48<br>状态机驱动的长篇 skill：构思→世界观→卷纲→章纲→逐章写，每步跑验证脚本卡关，配 YAML 角色卡、伏笔追踪、检查点回滚和修改经验积累<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-03-18 💤 · 中文 · 10 个 skill</sub><br><sub>💡 也适配 Trae、Antigravity</sub>

- **[craft-companion](https://github.com/qcx1919788736-collab/craft-companion)** · ★ 37<br>小说协作框架：从零或导入旧作建分层知识库，每章走章纲→初稿→执行层自查→评估层复核→仲裁层修订→终版，并回写知识库和检查点<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-04-07 💤 · 中文 · MIT</sub><br><sub>💡 附小说知识库 MCP 服务器和 CLI；也可在 Cherry Studio 里用</sub>

- **[bmad-book-builder](https://github.com/jblemee/bmad-book-builder)** · ★ 33<br>BMAD 小说模块：8 个 agent 与 17 个流程，每章后跑审稿→圣经更新→逐角色矛盾审计→主题→节奏审计链，用 TTR、句长等指标量化文风<br><sub>方法：记忆 · 多智能体 · 修订 · 风格</sub><br><sub>更新于 2026-01-25 💤 · 英文 · WTFPL</sub><br><sub>💡 需 BMAD 平台；主仓库在作者自建 Forgejo（git.ut0pia.org），GitHub 为 2026-01 快照</sub>

- **[mimoCode-story](https://github.com/nihaoshi/mimoCode-story)** · ★ 33<br>MiMo Code 版网文技能包：扫榜、拆文、大纲、正文、去 AI 味、审稿 32 个技能，加 9 重质量门禁、6 类毒点检测和 6 平台对标评分<br><sub>方法：规划 · 修订 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-07-18 · 中文 · 47 个 skill</sub><br><sub>💡 基于 zenstory-ai/oh-story-claudecode 二次开发，专为小米 MiMo Code 适配，Claude Code 用户用原版即可；一键安装是 curl \| bash</sub>

- **[novel-pro](https://github.com/lgz-star/novel-pro)** · ★ 32<br>规划→组稿→写作→观察→结算→审计→修订七角色流水线，事实总账+快照双层真相文件，旧稿逐章接管，未结算禁续写<br><sub>方法：记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-04-28 💤 · 中文 · AGPL-3.0</sub><br><sub>💡 基于 Narcooo/inkos 的角色拆分与真相文件思路改写为 skill，新增存量接管与逐章结算（见 ACKNOWLEDGEMENTS.md），AGPL-3.0</sub>

- **[thriller](https://github.com/pajama-studio/thriller)** · ★ 32<br>悬疑推理技能包：按子类型走诡计/人物/结构先行路线，追踪人物知情状态与线索公平性（双读者验证、诺克斯检查），七维加权评分改稿，可再转成分支互动小说<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-03-30 💤 · 中文 · 4 个 skill · MIT</sub><br><sub>💡 融合 McKee、Truby、Sanderson 等 25+ 方法与计算叙事论文（对抗式悬念、动态认知逻辑）；含分镜模块与自我进化（GEP）流程；README 英文、技能正文中文；2026-03 后未更新，因方法独特而收</sub>

- **[novelops-skill](https://github.com/qiyan233/novelops-skill)** · ★ 31<br>长篇小说状态化流水线：truth files 记设定与角色认知，生成下一章工作包，LLM 起草，审计修订，状态回写，快照 diff<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-09-28 · 多语言 · MIT</sub><br><sub>💡 基于 Narcooo/inkos 的思路（truth files、审计-修订-状态回写），用纯 Python 标准库重写成不绑宿主的 skill；另加角色知情边界检查、可配置审计规则、快照/diff、同人与番外的 canon 处理。draft 默认调用本地 Ollama。SKILL.md 以英文为主</sub>

- **[sailoumili/novel-writer](https://github.com/sailoumili/novel-writer)** · ★ 31<br>统筹队长调度世界、剧情、人物、执笔、复核 5 个子代理：先定《叙事宪法》、世界白皮书和伏笔台账再动笔，复核按三色灯打回重写<br><sub>方法：设定 · 人物 · 多智能体 · 修订</sub><br><sub>更新于 2026-09-15 · 中文 · MIT</sub><br><sub>💡 DeepSeek Harness（DSH）预设插件，只能在 DSH 里用；章节按版本号存档，改稿不覆盖</sub>

- **[bbroot/novel-master](https://github.com/bbroot/novel-master)** · ★ 30<br>OpenClaw 长篇小说 skill：策划书、分卷大纲与细纲、三层伏笔追踪、角色状态机与节点压缩图谱、每章四维审计<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-07-14 · 中文 · MIT</sub><br><sub>💡 ClawHub 上装到的是 v1，v2 脚本需从 GitHub 获取</sub>

- **[vibe-noveling](https://github.com/TulanCN/vibe-noveling)** · ★ 29<br>Claude Code 网文插件：苏格拉底式设定讨论、救猫咪全书规划、雪花法事件卡、写后 AI 味检测、标记返修、知识图谱<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-06-02 · 中文 · 16 个 skill · MIT</sub><br><sub>💡 针对 GLM-5 调优，作者要求关闭思考模式；默认风格基线是男频爽文</sub>

- **[dsh-novel-forge](https://github.com/huangziyuan-general/dsh-novel-forge)** · ★ 26<br>代码硬约束长篇：九阶段状态机，细纲未批不许写章，事实账本冲突拒存，写前按预算组装简报，重复句段机审、六维去 AI 味扫描、场景契约防泄底<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-25 · 中文 · MIT</sub><br><sub>💡 DeepSeek Harness 插件（20 个 novel_* 工具），另附 MCP 目录</sub>

- **[book-writer-skill](https://github.com/kshanxs/book-writer-skill)** · ★ 25<br>英文长篇写作：Story Forge 开书问答，Book Memory Bank 自动维护人物/世界/进度，含节奏蓝图、专项修订与简介/query letter<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-07-10 · 英文 · MIT</sub>

- **[openclaw-novel-writer-skill](https://github.com/alever520/openclaw-novel-writer-skill)** · ★ 24<br>OpenClaw 网文 skill：读全局大纲写七模块章纲并确认，结合写作指南和读者反馈列要点后写正文，15 项自检，读者反馈回写指南<br><sub>方法：规划 · 理论 · 修订</sub><br><sub>更新于 2026-04-02 💤 · 中文 · MIT</sub><br><sub>💡 每章自动提交 GitHub，需配置 GitHub Token</sub>

- **[siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer)** · ★ 24<br>写前一次取齐承接口、细纲、人物卡、待回收伏笔、用语禁词等 16 项材料，写后按六维文笔基线对照原著自检，排出带行号的改稿待办<br><sub>方法：记忆 · 修订 · 风格</sub><br><sub>更新于 2026-10-22 · 中文 · MIT</sub><br><sub>💡 DSH 插件，也可作 MCP 服务器；随包附 24MB 中文 ONNX 模型本地推理；工具本身不代写，正文由 agent 执笔</sub>

- **[webfiction-write](https://github.com/qingyabailu-git/webfiction-write)** · ★ 24<br>融合 oh-story 与 webnovel-writer：每章先定读者情绪再写，细纲不足即阻断，提交时写回状态，独立审查未完成标 unverified<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-07-31 · 中文 · 15 个 skill · MIT</sub><br><sub>💡 基于 zenstory-ai/oh-story-claudecode 与 lingfengQAQ/webnovel-writer 融合，另加 fiction.py（初始化、章节提交、审查指标、导出）和正文检查脚本；需 Python 3.8+</sub>

- **[xt-webnovel-writing](https://github.com/xiaotiewinner/xt-webnovel-writing)** · ★ 24<br>拆参考文本→立书→八步节奏剧情→爽点与四层文笔改写→结构 10 项加反 AI 味 25 项双路体检，命中回滚级硬门就退回重写；写前读、写后存磁盘记忆<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-04-30 · 中文</sub><br><sub>💡 方法论底本是一篇知乎文章，仓库内存档了全文；仓库没有许可证</sub>

- **[speckit-preset-fiction-book-writing](https://github.com/adaumann/speckit-preset-fiction-book-writing)** · ★ 23<br>把 Spec Kit 规格驱动流程改成写小说：故事简报→结构计划（多种情节框架）→逐场景写作任务，26 个命令覆盖构思到投稿，支持多视角与文风样本<br><sub>方法：规划 · 理论 · 修订 · 风格</sub><br><sub>更新于 2026-07-28 · 英文</sub><br><sub>💡 需 GitHub Spec Kit ≥0.5.0；文风有作者样本或 humanized-ai 两种模式；可导出 DOCX/EPUB/LaTeX</sub>

- **[novel-flow-one-by-one](https://github.com/ZhangDongyang800/novel-flow-one-by-one)** · ★ 19<br>6 个协作 skill：脑暴→大纲→逐场景写作→六维审稿→设定同步，总控按状态路由，内置冷白描/系统爽文/怪诞悬疑三种文风<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-07-18 · 中文 · 6 个 skill · MIT</sub><br><sub>💡 README 以 Trae 目录结构为例</sub>

- **[hermes-novel-generator](https://github.com/rwcrosk-arch/hermes-novel-generator)** · ★ 18<br>多智能体写长篇：编排者出大纲和状态 YAML，各角色 agent 互不可见地规划场景策略，叙事者编织成文，再经角色声线检查、设定审计和文风润色<br><sub>方法：人物 · 记忆 · 多智能体 · 模拟 · 修订</sub><br><sub>更新于 2026-04-23 💤 · 英文 · 3 个 skill · MIT</sub><br><sub>💡 为 Hermes Agent 写的 skill，依赖其 delegate_task 派子 agent；附进度看板、EPUB 打包和 diffusers 封面脚本；仓库带 .pyc</sub>

- **[long-novelist-skill](https://github.com/tianshiemo7/long-novelist-skill)** · ★ 17<br>百万字长篇中文小说：13 步配置问答、副本弧线三级大纲、角色状态档案、JSON 伏笔清单、跨会话恢复，附 11 个网文素材库<br><sub>方法：规划 · 人物 · 记忆</sub><br><sub>更新于 2026-06-01 · 中文 · MIT</sub><br><sub>💡 基于 PenglongHuang/chinese-novelist-skill 改写（仓库未注明），另加副本弧线规划、角色状态追踪、伏笔 JSON 清单和网文素材库</sub>

- **[dashenbibi/novel-master](https://github.com/dashenbibi/novel-master)** · ★ 16<br>长篇网文协议式 skill：总览、角色档案、世界观、卷纲统一管理，章节按骨架→正文→润色→质检→同步推进，带一致性检查和伏笔追踪<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-03-07 💤 · 中文 · MIT</sub>

- **[PhosAQy/novel-skills](https://github.com/PhosAQy/novel-skills)** · ★ 16<br>Claude Code 长篇插件：无大纲不写，先做百章级卷规划和章细纲，写完按 OOC、设定、逻辑、文风、重复五维加权打分决定采纳或人审，事实自动入知识库<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-01-19 💤 · 英文 · MIT</sub><br><sub>💡 只有一个 SKILL.md；README 中英双语</sub>

- **[silver-novel-skills](https://github.com/jialanhu0915/silver-novel-skills)** · ★ 16<br>男频/女频双系统网文写作：世界观/人物/情节三个框架 agent，按题材加载模板，12 项通用加男女频专项审稿 agent<br><sub>方法：规划 · 理论 · 人物 · 修订</sub><br><sub>更新于 2026-07-07 · 中文 · MIT</sub>

- **[writeAgent](https://github.com/Ddhjx-code/writeAgent)** · ★ 16<br>Claude Code 多 agent 写长篇：规划→写章→十维度审稿打分定去留→去 AI 味润色→归档故事圣经，逐章循环<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-05-18 · 中文 · 5 个 skill</sub>

- **[Shine8592/novel-writer-skills](https://github.com/Shine8592/novel-writer-skills)** · ★ 15<br>三个 OpenClaw skill：带情绪弧的章纲→调免费 API 分段批量写章→审计、校对、质量总监三段审查，每章复盘更新经验<br><sub>方法：规划 · 修订</sub><br><sub>更新于 2026-04-06 💤 · 中文 · 3 个 skill</sub><br><sub>💡 调用 ModelScope、Fyra、Ph8 等免费档第三方 API；仓库无许可证</sub>

- **[claude-novel-skill](https://github.com/mane23-ai/claude-novel-skill)** · ★ 14<br>长篇小说 skill：人物、物品、主题、地点、冲突节奏、读者体验六类追踪档案，配奇幻/推理/言情/恐怖类型预设，按章-场景指令逐场写作<br><sub>方法：规划 · 理论 · 人物 · 记忆</sub><br><sub>更新于 2026-04-07 💤 · 韩文</sub><br><sub>💡 韩语；含韩国网文平台连载与公募投稿流程；README 的克隆地址写成 looki/claude-novel-skill（该仓库不存在）</sub>

- **[novel-skill](https://github.com/mave99a/novel-skill)** · ★ 14<br>小说插件：先问题材设定，再跑 10–15 个 RPG 式抉择定剧情，生成含人物弧线、伏笔矩阵和章纲的计划，逐章写完后导出 EPUB<br><sub>方法：规划 · 风格 · 共创</sub><br><sub>更新于 2026-01-08 💤 · 多语言 · MIT</sub>

- **[writing-template-for-ai](https://github.com/hottweelz/writing-template-for-ai)** · ★ 14<br>整本书写作模板：先填问卷生成含人物、逐章大纲、文风指南和质量门槛的蓝图，再每会话写一章、做编辑审读并写交接记录，最后导出 EPUB/PDF<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-06-29 · 📝 提示词 · 英文 · MIT</sub><br><sub>💡 整理自作者已完成的成人文学小说《One Went Silent》的生产流程；附处理黑暗/成人题材的内容指引；也支持 GitHub Copilot</sub>

- **[dsh-novel-solo](https://github.com/Tkingxiao/dsh-novel-solo)** · ★ 13<br>面向本地量化小模型的写作预设：叙事方法→世界观→名词索引→大纲→目录→人物档案→逐章写，每章七维红黄绿审稿含 AI 腔检查，最后整书复审<br><sub>方法：规划 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-17 · 中文 · MIT</sub><br><sub>💡 DeepSeek Harness 插件；精简工具表、禁用 JSON 输出以适配量化模型</sub>

- **[DSH-Novelist](https://github.com/KurohaneKaoruko/DSH-Novelist)** · ★ 13<br>12 个方法论 skill 和 6 个文风 skill 按需加载，写前组装前十章结尾/人物卡/伏笔/时间线简报，写后跑 25 项正文 lint 与名词核对<br><sub>方法：规划 · 记忆 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-10-26 · 中文 · MIT</sub><br><sub>💡 DeepSeek Harness 预设；skills 本体在子模块 KurohaneKaoruko/Novelist-Skills；附玄幻/悬疑/甜宠工程模板与可选 WebUI</sub>

- **[opencreator-novel](https://github.com/xwcai999/opencreator-novel)** · ★ 13<br>中文小说 Codex 插件：读者契约与章节控制卡、待兑现承诺账本、确定性校验脚本、整书文学审稿与跨章结构相似度检查、封面<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-09-07 · 中文 · 3 个 skill · Apache-2.0</sub><br><sub>💡 wawa-* 两个子 skill 是非官方的蛙蛙写作投稿/统计适配，可不装</sub>

- **[wangwen-writing-skill-kit](https://github.com/hyi1233/wangwen-writing-skill-kit)** · ★ 13<br>网文方法论技能包：一个调度 skill 按需加载开篇、金手指、简介、伏笔、爽感、人物、节奏、去AI化、拆书等 13 个模块<br><sub>方法：理论 · 人物 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-08-24 · 中文</sub><br><sub>💡 内容蒸馏自 B 站 UP 主「网文徐掌柜」的拆书视频，含其原话金句</sub>

- **[human-novel-writer](https://github.com/huahuakandaima/human-novel-writer)** · ★ 12<br>长篇网文全流程：项目骨架与三总控文件、黄金三章合同、角色入场门禁、每章 8 步循环、拆文选题审稿封面，去AI味双门禁脚本<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-07 · 中文 · MIT</sub><br><sub>💡 整合 oh-story-claudecode、KKKKhazix/human-writing、writing-dna-skill 与贴吧《小说ai行文规范》，另加角色门禁、黄金三章合同和密度检查脚本；朱雀在线检测需腾讯云 API Key，封面依赖 foxtrai 生图 skill</sub>

- **[long-novel-generator](https://github.com/jiaw-Zh/long-novel-generator)** · ★ 12<br>长篇小说 skill：一句话创意扩成 3000 字故事核，建角色动力图谱和世界观状态文件，每次只规划 3-5 章，写完更新角色状态与全书摘要<br><sub>方法：规划 · 设定 · 记忆</sub><br><sub>更新于 2026-05-07 · 中文</sub><br><sub>💡 基于 YILING0013/AI_NovelGenerator，用 Gemini 把原项目流程蒸馏成 SKILL</sub>

- **[novel-assistant-skill](https://github.com/duiniwukenaihe/novel-assistant-skill)** · ★ 12<br>单入口网文助手：短篇/长篇写作、审阅、拆文、扫榜、导入、去AI味，带任务断点续写、按步召回记忆、改纲影响链和章节扩容迁移<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-08-10 · 中文 · 16 个 skill · MIT</sub><br><sub>💡 基于 worldwonderer/oh-story-claudecode（现 zenstory-ai/oh-story-claudecode），另加单入口路由、工作流断点、记忆召回、影响链与健康门；作者称短篇已稳定、长篇仍在打磨</sub>

- **[plotrail](https://github.com/waylean/plotrail)** · ★ 12<br>长篇工作流两件套：plotrail 建 canon、章节合同、写后连续性审稿和作者改稿偏好；plotrail-intake 诊断精修已有旧稿再交接续写<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-06-21 · 英文 · 2 个 skill · MIT</sub><br><sub>💡 skill 正文为英文，README 与示例为中文网文</sub>

- **[webnovel-writer-hermes](https://github.com/starMagic/webnovel-writer-hermes)** · ★ 12<br>Hermes Agent 版网文系统：市场扫描与对标拆书定方向，卷/章合同约束写作，context/审稿/数据子 Agent 分工，三级记忆与伏笔债务预算<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-06-05 · 中文 · 13 个 skill · GPL-3.0</sub><br><sub>💡 基于 lingfengQAQ/webnovel-writer；需 Hermes Agent，推荐配 DeerFlow 跑子 Agent</sub>

- **[Chinese-WebNovel-Master](https://github.com/TianHengZhuang/Chinese-WebNovel-Master)** · ★ 11<br>中文网文商业化工作流：策划→架构→写作→编辑→发布五角色，配 12 个平台读者偏好、类型套路、钩子与留存框架、故事圣经和连续性检查<br><sub>方法：规划 · 理论 · 记忆 · 多智能体</sub><br><sub>更新于 2026-10-21 · 📝 提示词 · 英文 · MIT</sub><br><sub>💡 SKILL.md 无标准 frontmatter，按角色手动使用；提示词为英文</sub>

- **[novel-writer-english](https://github.com/JeroTan/novel-writer-english)** · ★ 11<br>英文版八步写作流程：原则→规格→澄清→章节规划→任务→起草→编辑→审阅，另带只读故事查询 MCP 和场景草稿、编辑、审稿流程<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-08-09 · 英文 · 28 个 skill · MIT</sub><br><sub>💡 基于 wordflowlab/novel-writer-skills 翻译改写，新增故事查询 MCP、编辑/审稿流程、超长文件拆分和漫画提示词流程</sub>

- **[scriveno](https://github.com/hannsxpeter/scriveno)** · ★ 11<br>装进编程 agent 的长篇写作命令集：先建作者 Voice DNA，drafter agent 逐单元用作者声音起草，再做编辑审读、连续性与声音检查，后接出版<br><sub>方法：规划 · 修订 · 风格</sub><br><sub>更新于 2026-09-27 · 英文 · MIT</sub><br><sub>💡 npm 包 scriveno；支持 50 种作品类型，不限虚构（也覆盖技术文档、出版、翻译）</sub>

- **[wangwenwrite-skill](https://github.com/Thatgfsj-easyRep/wangwenwrite-skill)** · ★ 11<br>男频系统流网文单文件 skill：黄金三章、爽点节奏公式、系统设定法则、反 AI 味清单、书名公式与平台差异化<br><sub>方法：规划 · 理论 · 设定 · 去 AI 味</sub><br><sub>更新于 2026-05-04 · 中文 · Apache-2.0</sub>

- **[claude-novel-workflow](https://github.com/MintoTsukino/claude-novel-workflow)** · ★ 10<br>canon 驱动的长篇流程：先建角色/世界/术语/时间线/文风/禁用模式文件，多 agent 批量起草并三层审稿，附作者原创 JET 读者情绪框架<br><sub>方法：理论 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-06-16 · 📝 提示词 · 多语言</sub><br><sub>💡 日本轻小说作者的工作快照，声明不再维护；附真实连载前 10 话样例（日语），模板与文档为英文</sub>

- **[deepseek-harness-novel-studio](https://github.com/qinpeizhan77/deepseek-harness-novel-studio)** · ★ 10<br>DeepSeek Harness 小说插件：大纲、场景契约、人物状态、伏笔与禁写规则存成项目数据每轮注入，附前提锦标赛、样章验证、状态审查等 skill<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-08-30 · 中文 · 5 个 skill · MIT</sub><br><sub>💡 需 DeepSeek Harness（dsh）作宿主；AI 提出的变更先进待确认清单</sub>

- **[goink-skills](https://github.com/sigpanic/goink-skills)** · ★ 10<br>Goink 写作 App 的社区技能库：每条 Markdown 技能注入系统提示，现有情绪弧线及重生复仇、末世先知、逐界登顶、奇案升格等网文套路模板<br><sub>方法：规划 · 理论</sub><br><sub>更新于 2026-09-06 · 📝 提示词 · 中文 · CC-BY-SA-4.0</sub><br><sub>💡 主项目为 sigpanic/goink，App 内可一键安装；目前 6 条技能；CC BY-SA 4.0</sub>

- **[human-like-novel-workbuddy-skill](https://github.com/LittleLollipop/human-like-novel-workbuddy-skill)** · ★ 10<br>写章节计划时从词林、句式、修辞、节奏、叙事手法图库正向注入人类常用素材，按卷→段→章→节逐节写，设定存图库写前取用、写后校验<br><sub>方法：规划 · 理论 · 记忆 · 去 AI 味</sub><br><sub>更新于 2026-08-30 · 中文</sub><br><sub>💡 核心是用正向注入代替禁词表来去 AI 味；图数据库模式依赖约 30MB 的 axolotl 图库，推荐 macOS；附错误案例库和机检脚本；仓库无许可证</sub>

- **[novel-writing-skill](https://github.com/cnskycn/novel-writing-skill)** · ★ 10<br>长篇连载单文件提示词：大纲 6 步、章节 7 步、人物三锚点、伏笔 P1-P3 分级、六维质检，附追踪与记忆文件模板<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-05-23 · 📝 提示词 · 中文</sub><br><sub>💡 单个 .md 文件，README 按 Trae .trae/skills/ 安装；风格设定偏「孔二狗式」都市江湖叙事</sub>

- **[vicalloy/novel-skills](https://github.com/vicalloy/novel-skills)** · ★ 10<br>长篇小说 skill：用树形 Markdown 摘要（总纲加章节摘要、角色小传、世界观设定）承载剧情，每章写完强制更新相关摘要，写前一次性加载<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2026-04-12 💤 · 中文</sub><br><sub>💡 与作者的 Sequoia 项目深度绑定（摘要加载工具在那边）；附一部写到一半的 AI 小说作样例</sub>

- **[dsh-novel-craft](https://github.com/shiyan688/dsh-novel-craft)** · ★ 9<br>口味校准：作者对候选稿逐段点赞/点踩，模型提炼成几百字节偏好档案注入写稿；每章先列多种场景决策方向再分篇写，批注只改被标段落<br><sub>方法：规划 · 修订 · 风格 · 共创</sub><br><sub>更新于 2026-10-23 · 中文 · 2 个 skill · MIT</sub><br><sub>💡 DeepSeek Harness 插件，需 Node 22；写稿上下文只放规律、不放已写正文</sub>

- **[novel-creation-omnibus](https://github.com/limingnanyue/novel-creation-omnibus)** · ★ 9<br>55 个按需加载模块的写作 skill：类型模板（规则怪谈、番茄爆文等）、开篇钩子、L1–L4 去 AI 门禁、五专家并行审计与 11 维评分，带技能自进化循环<br><sub>方法：理论 · 多智能体 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-07-25 · 中文 · MIT</sub><br><sub>💡 覆盖长篇网文到短篇；模块与自进化指标数量庞大、术语堆砌，实际效果需自测</sub>

- **[novel-creation-skill](https://github.com/skye-z/novel-creation-skill)** · ★ 9<br>中文长篇/同人 skill：提取原著资料、头脑风暴定设定和人物卡，按题材模板和三/五/六幕结构推进，读者欲望驱动、桥接情节过渡，带自检和上下文管理<br><sub>方法：规划 · 理论 · 人物 · 记忆</sub><br><sub>更新于 2026-04-08 💤 · 中文 · MIT</sub><br><sub>💡 为 Trae SOLO Web 优化，需智能体有联网搜索和内容提取能力；对同人支持最好</sub>

- **[novel-writer-skill](https://github.com/liuxiao20051106-prog/novel-writer-skill)** · ★ 9<br>中英双语小说写作 skill：构思、人设、章纲、逐章写作与章节衔接检查、去 AI 味，附草稿量化体检脚本和 11 套追踪模板<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-09-17 · 多语言 · 2 个 skill · MIT</sub><br><sub>💡 另附 ChatGPT、DeepSeek、Gemini 等网页端的系统提示词用法</sub>

- **[dsh-novel-writing](https://github.com/peterwangze/dsh-novel-writing)** · ★ 8<br>29 个 skill 的网文流水线：协调者统筹选题、大纲、细纲，按看护包生成正文并九维审查，代码门禁拒存离纲章节，再按发布数据回调写作方向<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-10-22 · 中文 · 29 个 skill</sub><br><sub>💡 基于同作者 peterwangze/claude-writing-workflow 迁移到 DeepSeek Harness；默认人类主笔、AI 出草稿参考，高 AI 参与度会阻断上架；仓库未声明许可证</sub>

- **[inkcraft-writing-skills](https://github.com/Fei2411/inkcraft-writing-skills)** · ★ 8<br>13 种网文体裁的写作方法库，每个体裁分结构、前三章、场景写法、成文规范、自检清单五份，带体裁自动分流 skill<br><sub>方法：规划 · 理论 · 修订</sub><br><sub>更新于 2026-09-12 · 中文 · 14 个 skill</sub><br><sub>💡 CC BY 4.0；由商业产品 InkCraft 的写作材料提炼，不含软件本身</sub>

- **[snowflake-writer](https://github.com/vagabondshun/snowflake-writer)** · ★ 8<br>雪花写作法 10 步 skill：一句话→五句结构→人物表→一页梗概→四页大纲→场景表→场景结构→成文，分给 5 个 agent 人格，附文风 RAG<br><sub>方法：规划 · 人物 · 风格</sub><br><sub>更新于 2025-12-18 💤 · 英文 · 3 个 skill · MIT</sub>

- **[ty-xiaoshuo-skill](https://github.com/danieltao118/ty-xiaoshuo-skill)** · ★ 8<br>网文八道工序 skill：创作前检查→细纲→正文→四轨质检→跨章节奏审→更新设定库→前情摘要→阶段回顾，五维评分不达标重写，情节类型轮换防公式化<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-03-28 💤 · 中文</sub><br><sub>💡 质检含去 AI 味；附番茄平台策略和修仙、萌娃题材模板；README 写 MIT 但无许可证文件</sub>

- **[xiaoshuo-studio](https://github.com/Zhao73/xiaoshuo-studio)** · ★ 8<br>长篇工作台+skill 包：问答建书向导生成 canon 与首章 brief，导入参考小说做风格卡，逐章规划→起草→连续性检查→回写 canon→去 AI 味<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-06-01 · 中文 · 20 个 skill · MIT</sub><br><sub>💡 Web 工作台依赖本地已登录的 Codex CLI；风格学习强调学技法、不克隆作者声线</sub>

- **[Dylin-code/NovelGenerator](https://github.com/Dylin-code/NovelGenerator)** · ★ 7<br>两段式 skill：资深编辑七段访谈产出 bible（含三幕结构、人物 want/need），再出大纲，每章跑写手→评论家→修订者子代理最多两轮<br><sub>方法：规划 · 人物 · 多智能体 · 修订</sub><br><sub>更新于 2026-04-28 💤 · 中文 · 2 个 skill</sub><br><sub>💡 写手和修订者默认走本地 LM Studio，评论家用 Claude；繁体中文</sub>

- **[fanqie-novels-skills](https://github.com/mhkz/fanqie-novels-skills)** · ★ 7<br>番茄爽文版 Claude Code 命令：沿用宪法→规格→澄清→计划→任务→写作→分析七步，加金手指/打脸/爽点节奏五问澄清和敏感词、爽点密度检查<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-02-12 💤 · 中文 · 12 个 skill · MIT</sub><br><sub>💡 基于 wordflowlab/novel-writer；另含番茄榜单抓取和分类建议</sub>

- **[huxiuzhi-novel-agent](https://github.com/huxiuzh-ops/huxiuzhi-novel-agent)** · ★ 7<br>主管→规划→写手→编辑角色流写长篇，角色/章节/伏笔/地点/时间线建结构化索引，伏笔登记→逾期警告→回收验证，关键决策交人确认<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-04-11 💤 · 中文 · 2 个 skill · MIT</sub><br><sub>💡 核心规则在平台无关的 AGENT.md，SKILL.md / CLAUDE.md 只是入口</sub>

- **[Novel-framework](https://github.com/bafeite59/Novel-framework)** · ★ 7<br>Claude Code skill：引导逐模块搭建人物、时间轴、三幕情节节点、情绪起伏、浅/深伏笔、分层结局、风格与内容增减，输出 Mermaid 思维导图框架<br><sub>方法：规划 · 理论</sub><br><sub>更新于 2026-07-19 · 中文 · MIT</sub><br><sub>💡 只产出故事框架思维导图，不写正文</sub>

- **[novelist](https://github.com/comfuture/novelist)** · ★ 7<br>长篇小说插件：设定、人物、素材、情节、大纲存成带 ID 的 Markdown，按章组装有界上下文，追踪读者已知信息和揭示时机，按类型套路写并独立审阅<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-07-31 · 英文 · 9 个 skill · MIT</sub><br><sub>💡 内置武侠、科幻、时间循环、推理、情感等类型策略；也支持 Antigravity CLI</sub>

- **[novelist.skills](https://github.com/Ink-dark/novelist.skills)** · ★ 7<br>小说 skill：澄清需求后生成梗概、大纲、人物、世界与文风文件，续写守「五零」纪律（零判断、零心理直述等），写完自动七维自检并给出净化稿<br><sub>方法：规划 · 设定 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-06-07 · 中文 · 2 个 skill</sub><br><sub>💡 能把已有正文逆向解析成设定文件</sub>

- **[novella-xl-15](https://github.com/paradroidlabs/novella-xl-15)** · ★ 7<br>长篇系统提示词：每章先做超详细规划、写完做复盘指导下一章，每章约 8000 字；原 Wordware 流程为标题→改情节→择优→15 章故事线→循环写章<br><sub>方法：规划 · 修订</sub><br><sub>更新于 2025-08-06 💤 · 📝 提示词 · 英文</sub><br><sub>💡 已停止维护（作者标 deprecated）；Wordware 上的 wordapp 本体不在仓库里，仓库只有系统提示词、输出和评价样例；原流程用 ElevenLabs 生成章节音频；无许可证</sub>

- **[agent-novel](https://github.com/RTY798/agent-novel)** · ★ 6<br>每章先填章节卡（目标·阻力·选择·后果），按 HOT/WARM/COLD 分层加载事实，出节拍由作者定关键选择再写首稿，过事实门禁后更新状态库与章节日志<br><sub>方法：规划 · 记忆 · 修订 · 共创</sub><br><sub>更新于 2026-07-24 · 中文 · MIT</sub><br><sub>💡 附零依赖 Node 脚本校验 story-state.json 和章节卡；风格项只作观察，不当退稿依据</sub>

- **[Claude-Code-Novel-Writing](https://github.com/f43a9a/Claude-Code-Novel-Writing)** · ★ 6<br>日语 Claude Code 命令集：企划→世界观→角色→结构→验证→分镜→执笔→审阅八阶段，按作者 MBTI×角色 MBTI×类型×文体×读者层理论库生成<br><sub>方法：规划 · 理论 · 人物 · 修订</sub><br><sub>更新于 2025-07-08 💤 · 日文 · MIT</sub><br><sub>💡 2025-07 后未更新；附 AI 作家作品展示站</sub>

- **[claude-novel-skills](https://github.com/fnb666888/claude-novel-skills)** · ★ 6<br>小说 skill：角色表现=个性×情绪×动作×语言、章节=事件×风格×氛围×角色的去耦合组合法，以单一核心体验极端化为目标，配六关去 AI 味<br><sub>方法：理论 · 人物 · 去 AI 味</sub><br><sub>更新于 2026-06-26 · 中文 · MIT</sub>

- **[general-novel-skill](https://github.com/xiaoyuCR7/general-novel-skill)** · ★ 6<br>长篇网文 skill：每章正文与摘要、角色状态、伏笔、时间线按事务一起提交，7 道去 AI 味闸口，34 题材与多平台规则按需加载<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-23 · 中文 · MIT</sub><br><sub>💡 体量大（47 个脚本、118 份参考、24 个 MCP 工具），附五章示例书和去 AI 味前后对照</sub>

- **[lvyu-cmd/chinese-novelist-skill](https://github.com/lvyu-cmd/chinese-novelist-skill)** · ★ 6<br>中文长篇小说 skill：五项输入自动生成设定，逐章或子 Agent 并行写作，三层记忆、七维自动校验、章节评分和三级修订<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-06-17 · 中文</sub><br><sub>💡 基于 PenglongHuang/chinese-novelist-skill，另加 SQLite 持久化、三层记忆、修订模式和 8 个校验/评分脚本；README 里的 clone 地址写成 chinese-novelist-skill-master，要换成本仓库</sub>

- **[novel-project-strategy](https://github.com/wgwtest/novel-project-strategy)** · ★ 6<br>Codex 长篇项目管理 skill：定义加载顺序、章节状态与同步规则，新会话不读全文也能恢复项目，防止大纲、设定、正文互相漂移<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2026-04-18 💤 · 英文 · MIT</sub>

- **[novel-webfiction](https://github.com/zlbigger/novel-webfiction)** · ★ 6<br>OpenClaw 网文连载 skill：开书问 4 个问题建档，每章先读设定、大纲和最近 3 章再写，正文按章存进 Obsidian<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2026-06-28 · 中文 · MIT</sub><br><sub>💡 单文件、规则较简单，适合轻量连载</sub>

- **[novel-writer-workflow](https://github.com/GonsonInter/novel-writer-workflow)** · ★ 6<br>两阶段小说 skill：构思出宪法后搭大纲和钩子矩阵，按场景走 8 步 SOP，每个场景两轮独立 agent 审到无 P0/P1，脚本扫硬约束，维护跨章四表<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-04-23 💤 · 中文 · 6 个 skill · MIT</sub><br><sub>💡 命令沿用 novel-writer 七步法；作者称用它写完一部约 13 万字的长篇</sub>

- **[open-novel-fanqie](https://github.com/kongxcer555/open-novel-fanqie)** · ★ 6<br>番茄网文长篇流水线 12 个 skill：拆对标书出套路 JSON、换壳选切入点、书名简介与事件、大纲人物设定、细纲、正文、审稿、滚动摘要<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-06-12 · 中文 · 11 个 skill · MIT</sub><br><sub>💡 原仓库 mosonlab/open-novel-fanqie 已失效，这里是转存；README 里的 git clone 地址要换成 kongxcer555/open-novel-fanqie。脚本依赖 bun，p7 去 AI 味尚未完成</sub>

- **[web-novel-master](https://github.com/tinylion1024/web-novel-master)** · ★ 6<br>网文创作工作流：快速、专业、工业、一次生成四种模式，含 11 个赛道的作者文风卡、套路库、平台定位包和项目初始化与校验脚本<br><sub>方法：规划 · 理论 · 修订 · 风格</sub><br><sub>更新于 2026-07-20 · 中文 · MIT</sub><br><sub>💡 基于 PenglongHuang/chinese-novelist-skill（情节结构、人物塑造、对话、扩写等指南沿用原版），另加四种创作模式、作者文风卡、平台定位包、市场数据和项目管理脚本</sub>

- **[7a-z/NovelClaw](https://github.com/7a-z/NovelClaw)** · ★ 5<br>OpenClaw 网文 skill：先定世界观、人物和 5–10 章大纲，按战斗/情感/悬疑场景切换文风，写完用脚本扫 AI 腔禁用词并自动扩充词库<br><sub>方法：规划 · 去 AI 味 · 共创</sub><br><sub>更新于 2026-05-02 · 中文</sub><br><sub>💡 与 iLearn-Lab/NovelClaw 同名但无关；分段写作时会停下来征求反馈</sub>

- **[book-writer-mcp](https://github.com/arupmaity1/book-writer-mcp)** · ★ 5<br>写书 MCP 工具集：故事圣经记录人物、场景和情节线，文风指南约束语气、视角和时态，连续性检查找矛盾，逐章写入并导出 docx<br><sub>方法：记忆 · 修订 · 风格</sub><br><sub>更新于 2026-04-05 💤 · 英文</sub><br><sub>💡 小说和非虚构通用；附封面规格和 KDP 导出</sub>

- **[claude-novel-writer](https://github.com/zhiliyouxian/claude-novel-writer)** · ★ 5<br>Claude Code 插件：分析参考小说→策划蓝图（选题、世界观、人物、章纲）过审核门→章节写作与审核修订循环→导出，按类型加载知识包<br><sub>方法：规划 · 理论 · 多智能体 · 修订</sub><br><sub>更新于 2025-12-28 💤 · 多语言 · 9 个 skill · MIT</sub><br><sub>💡 8 个 agent、9 个 skill；发布环节还有有声书优化和视频组装；目前只有中文网文知识包</sub>

- **[ddedook/dsh-novel](https://github.com/ddedook/dsh-novel)** · ★ 5<br>一个工作区一本书：人物/世界/等级/时间线/大纲/章节存进本地 PGlite canon，先开书设定，再用斜杠命令分步写大纲和章节，附题材模板与文风<br><sub>方法：规划 · 设定 · 记忆 · 风格</sub><br><sub>更新于 2026-10-24 · 中文 · MIT</sub><br><sub>💡 DeepSeek Harness 插件</sub>

- **[dongyanyuxuana/novel-craft](https://github.com/dongyanyuxuana/novel-craft)** · ★ 5<br>通用小说 skill：主控加 7 个子代理，访谈立项、资料拆分、逐章写作、逐段 17 维审查、修订发布，附 34 位作家技法库<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-09-06 · 中文 · MIT</sub><br><sub>💡 含成人向场景参考文档，按受众分级启用</sub>

- **[fanqie-xiaoshuo-skill](https://github.com/soultt/fanqie-xiaoshuo-skill)** · ★ 5<br>番茄风网文 11 个 skill：设定、总纲与章纲的设计和审查、正文写作和审查、签约潜力评估、日更工作流<br><sub>方法：规划 · 理论 · 修订</sub><br><sub>更新于 2026-06-26 · 中文 · 11 个 skill</sub><br><sub>💡 README 安装说明简略；仓库描述里的「包签约」是宣传语，实际是签约评估模板</sub>

- **[jiangying3222880/novel-engine](https://github.com/jiangying3222880/novel-engine)** · ★ 5<br>网文写作引擎：拆对标书建素材池，细纲、正文、检验打回、落库四段流水线，管长篇状态，另有短故事模式和 BM25 检索<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-10-17 · 中文 · 12 个 skill</sub><br><sub>💡 门禁、检索、同步脚本需 Python，不装时降级为手动校验；生成的「叙事总览」目录可作为 Obsidian 库查看</sub>

- **[light-novel-creator](https://github.com/Nya-Nya-Hoshino/light-novel-creator)** · ★ 5<br>轻小说创作 skill：先按指定作品/作者建风格档案，维护双区角色卡（固定属性+每章更新）与时间线双写校验，每章写完做 6 维自审<br><sub>方法：人物 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-06-23 · 中文</sub><br><sub>💡 为 Reasonix 平台编写；ACGN 百科抓取依赖另一个未随仓库提供的 skill；含让 agent 自行搜索安装外部 skill/MCP 的指令，使用前留意</sub>

- **[novel-writer-agent](https://github.com/ZBA-z/novel-writer-agent)** · ★ 5<br>番茄网文作家人格 skill：大纲→细纲→正文→打磨→审查，从上传的爆款 txt 蒸馏写法，每章按朱雀检测降 AI 味，每 30 章批量审查<br><sub>方法：规划 · 修订 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-09-11 · 中文</sub><br><sub>💡 主打通过朱雀 AI 检测；附网文词库和对爆款作品的蒸馏库</sub>

- **[NovelFlow](https://github.com/DongxUETAFFY/NovelFlow)** · ★ 5<br>长篇小说 skill：用文件系统当长期记忆，按章节远近做金字塔式上下文压缩，每章提交结构化 delta，分自由草稿、标准、生产锁定、断书续完等模式<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-05-20 · 中文 · 2 个 skill · MIT</sub>

- **[novelist-skill](https://github.com/chanceline-max/novelist-skill)** · ★ 5<br>Codex 中文小说 skill：从灵感到卷纲章纲、正文续写与改稿，维护人物、世界观、伏笔、时间线和章节总结文件<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-07-23 · 中文 · MIT</sub>

- **[Soundingboard](https://github.com/richardelder2/Soundingboard)** · ★ 5<br>以场景为单位的小说工作区：38 个 skill 覆盖情节追问、人物 DNA、对白、感官扩写等；连续性账本追踪设定，修改建议用方括号隔离不动原文<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-10-16 · 英文 · 19 个 skill · MIT</sub><br><sub>💡 默认作者执笔，AI 生成正文要显式进入 Generative 模式</sub>

- **[story-foundry](https://github.com/mmunro3318/story-foundry)** · ★ 5<br>Claude Code 小说工作区：捕获→提炼→生产，子代理按 Truby、Swain 等理论包出大纲和场景卡，起草后批评、出修复单再修订<br><sub>方法：规划 · 理论 · 多智能体 · 修订</sub><br><sub>更新于 2025-09-20 💤 · 英文</sub><br><sub>💡 作者自述是上下文工程实验项目；仓库无许可证</sub>

- **[wbb316/dsh-novel](https://github.com/wbb316/dsh-novel)** · ★ 5<br>开书向导填设定、主角、世界观和三幕大纲，大纲拆成按卷分组的情节点挂到章节，写下一章时自动带上未写情节点、卷纲领和角色关系<br><sub>方法：规划 · 人物 · 记忆</sub><br><sub>更新于 2026-10-06 · 中文 · MIT</sub><br><sub>💡 DeepSeek Harness 插件，作者自述练手项目；需 DSH 0.2.0-rc.1+</sub>

- **[web-novel-writing-skill](https://github.com/XINGANLIU/web-novel-writing-skill)** · ★ 5<br>网文 10 阶段流水线：灵感、世界观、人物、总纲、卷纲、章纲、黄金三章、正文、质检、状态同步，含人物漂移和反派降智检查<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-06-11 · 中文 · MIT</sub>

- **[write-continuous-novels](https://github.com/Lzhimie/write-continuous-novels)** · ★ 5<br>强制「分章大纲→读上一章结尾→定本章目标与新冲突→写正文→查连贯与重复套路→不合格先改」逐章循环，要求每章产生实际剧情推进<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-07-24 · 中文</sub><br><sub>💡 README 开头和结尾是作者的 Token 中转站广告</sub>

- **[chaserr/novel-craft](https://github.com/chaserr/novel-craft)** · ★ 4<br>Claude Code 长篇写作与审稿插件：5 个 skill + 12 个 agent，用 RTK.md 定题材风格，管大纲、前情、伏笔、人物档案和逐章审稿<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-09-18 · 中文 · 6 个 skill · MIT</sub><br><sub>💡 作者另有同流程的桌面版 novel-craft-studio</sub>

- **[novel-writing-skills-for-agents](https://github.com/230517ydyzs-maker/novel-writing-skills-for-agents)** · ★ 3<br>7 个小说创作 skill：叙事结构（三幕式、轻小说卷级结构、伏笔回收、支线功能）、人物设计、世界观、文笔、主题象征与修订指南，供 agent 分步调用<br><sub>方法：理论 · 设定 · 人物 · 修订</sub><br><sub>更新于 2026-05-10 · 中文 · 7 个 skill</sub><br><sub>💡 README 很简略；SKILL.md 没有 YAML frontmatter，部分宿主需手动加载</sub>

- **[novel_writting_skill](https://github.com/ruyuehao/novel_writting_skill)** · ★ 3<br>仙侠玄幻网文技巧库：12 个维度（场景、情绪、对白、战斗、钩子等）的参考由本地 MCP 按维度检索，配写作、润色、定向优化、卡文诊断 4 个工作流和 6 份清单<br><sub>方法：理论 · 修订</sub><br><sub>更新于 2026-06-22 · 中文</sub><br><sub>💡 MCP 检索服务打包在 mcp-server.zip 里，需要先解压；也可以把 SYSTEM_PROMPT.md 直接当系统提示词用</sub>

- **[Novelist-Skills](https://github.com/KurohaneKaoruko/Novelist-Skills)** · ★ 2<br>18 个 SKILL：工程初始化、人物/世界观/文风卡建档、情节节奏与章节细纲、行文铁律、连续性检查、改稿，加词级/句式级去 AI 味特征库和 6 种类型文风<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-10 · 中文 · 18 个 skill · MIT</sub>

- **[cherry-agent-skills-public](https://github.com/Zn-lemon/cherry-agent-skills-public)** · ★ 1<br>网文与跑团叙事模板 skill：先定类型、读者、欲望和核心冲突，按钩子→升级→反转→高潮搭大纲，人物按欲望/恐惧/错误信念设计，跑团分表层与隐藏真相<br><sub>方法：规划 · 人物</sub><br><sub>更新于 2026-05-11 · 英文 · 3 个 skill · MIT</sub><br><sub>💡 Cherry Studio 转 Hermes Agent 的模板仓库，只有 moyu-webnovel-dm 与叙事有关（另两个是 A 股和文献）；模板偏简</sub>

- **[Chinese-Novel-Workflow](https://github.com/wp1020/Chinese-Novel-Workflow)** · ★ 1<br>长篇网文全流程：设定→总纲→卷纲→含完整事件链的章节细纲→带前文衔接包的单章指令→正文→连续性审稿→去 AI 润色→章节记忆回写设定库<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-08-01 · 中文 · Apache-2.0</sub>

- **[CN-writer](https://github.com/nanbengmuyuhua999/CN-writer)** · ★ 1<br>中文长篇写/审/改三模式分开：写作时加载叙事距离、感官沉浸、断章钩子、代价节拍等 skill，审稿扫 AI 味与视角，四个 agent 按优先级修复<br><sub>方法：理论 · 多智能体 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-07-30 · 中文 · 14 个 skill · MIT</sub>

- **[writer-skill](https://github.com/lyzxka/writer-skill)** · ★ 1<br>长篇小说 skill：章纲→场景分解→质量循环三层嵌套；每章后更新元/实体/叙事三层记忆和变更日志，内层做一致性检查和 AI 腔检测后修订<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-07-13 · 中文</sub><br><sub>💡 AI 腔检测兜底依赖 humanizer-zh skill（可选）</sub>

- **[clark-typer](https://github.com/niyongsheng/clark-typer)** · ★ 0<br>硬科幻长篇 skill 流程：选题→设定（科学三层标注）→人物→大纲，写作/文学+科学审稿/润色/读者盲读循环，可回溯状态机加 sqlite-vec 一致性扫描<br><sub>方法：规划 · 设定 · 记忆 · 修订</sub><br><sub>更新于 2026-10-20 · 中文 · 20 个 skill</sub><br><sub>💡 仓库根目录同时放着作者自己的创作产物（0-角色档案…7-正文），/typer-init 可重置；支持导入外部作品续写/二创；附 Web 工作台；无许可证</sub>

#### 框架 · 应用（215）

- 🌟 **[inkos](https://github.com/Narcooo/inkos)** · ★ 10.8k<br>统一 harness 管长短篇、剧本、同人仿写、互动影游；长篇用 truth files 记设定、伏笔和角色状态，每章写后审计→修订→状态回写<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-10-24 · ⚙️ 框架 · 多语言 · 21 个 skill · AGPL-3.0</sub>

- 🌟 **[AI_NovelGenerator](https://github.com/YILING0013/AI_NovelGenerator)** · ★ 6.3k<br>本地部署的长篇小说生成应用：用雪花法从核心创意逐级展开卷、弧、场景、章纲到正文，管理角色/势力/物品/伏笔状态，AI 流程可在画布上改<br><sub>方法：规划 · 理论 · 人物 · 记忆</sub><br><sub>更新于 2026-10-16 · 🧩 应用 · 多语言 · AGPL-3.0</sub><br><sub>💡 main 分支已经重写（Next.js + FastAPI + MongoDB），旧版留在 old 分支，两版数据不兼容</sub>

- 🌟 **[NousResearch/autonovel](https://github.com/NousResearch/autonovel)** · ★ 1.6k<br>仿 autoresearch 的改—评—留弃循环：设定、人物、大纲、文风、canon 打分过阈值，逐章起草评分重写，再经对抗删改、读者评审团和 Opus 审稿<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-03-20 💤 · ⚙️ 框架 · 英文</sub><br><sub>💡 无 License；附 CRAFT.md / ANTI-SLOP.md 等写作原则文档；示例成书在 autonovel/bells 分支；导出阶段另有排版、插画和 ElevenLabs 有声书</sub>

- 🌟 **[neuro-book](https://github.com/notnotype/neuro-book)** · ★ 753<br>长篇写作 IDE：时间线切面事件溯源推算世界状态，伏笔承诺账本，leader/writer 等多 agent 分工写章，llmlint 规则查 AI 味<br><sub>方法：规划 · 记忆 · 多智能体 · 去 AI 味</sub><br><sub>更新于 2026-10-24 · 🧩 应用 · 中文 · 28 个 skill · AGPL-3.0</sub><br><sub>💡 AGPL-3.0；当前分支按 v2 方案重建中，可用版本在 master；去 AI 味 lint 另有独立仓库 notnotype/llmlint</sub>

- **[AI-Novel-Writing-Assistant](https://github.com/ExplosiveCoderflome/AI-Novel-Writing-Assistant)** · ★ 3.3k<br>长篇小说创作工作台：自动导演从灵感推进到开书、世界观、角色、章节规划、正文与检查，含拆书、写法引擎、反 AI 规则、RAG 知识库和短篇流程<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-10-24 · 🧩 应用 · 中文 · 2 个 skill</sub><br><sub>💡 有 Windows 桌面版，也能从源码部署；能把已写章节延展成漫画分镜和短剧素材。作者另有 ani-book-skill（已收）</sub>

- **[MuMuAINovel](https://github.com/xiamuceer-j/MuMuAINovel)** · ★ 3.2k<br>小说创作 Web 应用：向导生成大纲、角色、世界观和职业等级体系，逐章生成并按分析重写，带伏笔追踪、拆书、自定义文风和可编辑 Prompt 模板<br><sub>方法：规划 · 人物 · 记忆 · 风格</sub><br><sub>更新于 2026-10-16 · 🧩 应用 · 中文 · 7 个 skill · GPL-3.0</sub><br><sub>💡 Docker + PostgreSQL 部署；README 有大量 API 中转站赞助广告；内置 story-* skill 搬自 oh-story-claudecode</sub>

- **[gpt-author](https://github.com/mshumer/gpt-author)** · ★ 2.5k<br>先生成多个情节并选出最佳再改进，写出指定章数的故事线并再改一轮，逐章参考前文写作，最后生成封面打包 EPUB<br><sub>方法：规划 · 修订</sub><br><sub>更新于 2024-04-03 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 2023 年的早期代表作，Jupyter/Colab 笔记本；另有更简化的 Claude 3 版本</sub>

- **[ainovel-cli](https://github.com/voocel/ainovel-cli)** · ★ 2.2k<br>全自动长篇小说生成 CLI：确定性引擎调度 Architect/Writer/Editor 三个代理，卷弧滚动规划、七维评审、步骤级断点恢复，可随时插入修改意见<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-10-25 · ⚙️ 框架 · 中文 · Apache-2.0</sub><br><sub>💡 主打一句话全自动成书；想逐章把关可开 /review on。可在 TUI 里看着写，也可 headless 跑在服务器上</sub>

- **[EthanYoQ/AI-Novel-Writer](https://github.com/EthanYoQ/AI-Novel-Writer)** · ★ 1.8k<br>桌面长篇写作软件：前提、角色、世界观、章节蓝图、草稿、审稿、修稿、定稿逐段推进，可按阶段绑定写作 Skill，支持本地与在线模型<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-10-26 · 🧩 应用 · 多语言 · GPL-3.0</sub><br><sub>💡 提供 Windows/macOS 桌面版；仓库里另有 DeepSeek Harness 插件预览版，已冻结，作者说它的能力不到桌面版一成</sub>

- **[arboris-novel](https://github.com/t59688/arboris-novel)** · ★ 1.6k<br>写作网页应用：角色/地点/派系设定库，AI 把灵感整理成主线蓝图和章节纲要，按纲要生成章节并抽取摘要供后文使用，支持一次多版本择优<br><sub>方法：规划 · 设定 · 记忆</sub><br><sub>更新于 2026-02-25 💤 · 🧩 应用 · 中文</sub><br><sub>💡 需 OpenAI 兼容 API；想用命令行加编辑器可搭配 t59688/novel-kit；仓库无许可证</sub>

- **[91Writing](https://github.com/ponysb/91Writing)** · ★ 1.6k<br>前端小说创作台：按类型模板建书，AI 生成大纲与章节、续写和分类润色，世界观模板化管理并做一致性检查，提示词库带变量可自定义<br><sub>方法：规划 · 设定 · 修订</sub><br><sub>更新于 2025-10-14 💤 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 2025-10 后未更新，按 ≥100★ 保留；需自配 OpenAI 兼容 API，内置提示词仅为演示</sub>

- **[RhythmicWave/NovelForge](https://github.com/RhythmicWave/NovelForge)** · ★ 1.3k<br>卡片式长篇创作工具：按 JSON Schema 结构化生成设定、角色、大纲卡片，用 @DSL 注入上下文、知识图谱保一致，可编排代码式工作流（含拆书）<br><sub>方法：规划 · 设定 · 人物 · 记忆</sub><br><sub>更新于 2026-09-23 · 🧩 应用 · 中文 · AGPL-3.0</sub>

- **[Long-Novel-GPT](https://github.com/MaoXiaoYuZ/Long-Novel-GPT)** · ★ 1.2k<br>长篇小说 Agent：章节→剧情→正文逐级扩写并多线程并行；可导入已有小说拆书得剧情纲要，按意见检索片段改写并同步更新纲要<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2025-11-05 💤 · 🧩 应用 · 中文</sub><br><sub>💡 2025-11 后未更新（1247★）；附天蚕土豆风格等提示词；Docker 部署</sub>

- **[OpenFic](https://github.com/syrizelink/OpenFic)** · ★ 1.2k<br>人机协同的小说写作工具：写作编辑器加可自定义的 Prompt/Agent/工作流，维护设定、角色与伏笔，向量检索百万字项目，支持 Docker/pip/桌面版<br><sub>方法：设定 · 人物 · 记忆 · 共创</sub><br><sub>更新于 2026-10-25 · 🧩 应用 · 多语言 · Apache-2.0</sub><br><sub>💡 定位是协同写作，不做一键成书。README 里有 API 中转商的推广链接</sub>

- **[denova](https://github.com/alfredxw/denova)** · ★ 973<br>小说写作与 AI 文字冒险一体平台：资料库按组给 Agent 供上下文，支持 SubAgent 协作和定时续写/审阅；游戏侧有剧情分支、角色世界状态与规则检定<br><sub>方法：规划 · 记忆 · 多智能体 · 共创</sub><br><sub>更新于 2026-10-25 · 🧩 应用 · 多语言 · 10 个 skill · Apache-2.0</sub><br><sub>💡 发布版默认开启匿名使用统计（Umami，可关）；一键安装为 curl \| sh 脚本</sub>

- **[AI-automatically-generates-novels](https://github.com/wfcz10086/AI-automatically-generates-novels)** · ★ 964<br>种子→根合同→里程碑链→逐章细纲→正文，每层发散 3 个候选由程序选优；评审须引原句证据、由程序扣分并自动返修，也能写短剧和影视剧本<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-09-14 · ⚙️ 框架 · 中文 · Apache-2.0</sub><br><sub>💡 带 Web UI 和守护进程长跑；内容类型由 packs 声明，可扩展；需配置至少一个模型网关</sub>

- **[wordflowlab/novel-writer](https://github.com/wordflowlab/novel-writer)** · ★ 958<br>参照 Spec-Kit 的七步法：宪法→规格→澄清→计划→任务→写作→分析，以斜杠命令装进多种 AI 助手，配情节/时间线/关系/世界观追踪做一致性检查<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2025-10-26 💤 · ⚙️ 框架 · 中文 · MIT</sub><br><sub>💡 npm 包 novel-writer-cn，novel init 生成项目和命令；插件含真实人声、风格模仿等</sub>

- **[yuanbw2025/storyforge](https://github.com/yuanbw2025/storyforge)** · ★ 928<br>本地优先叙事工作台：长短篇小说、剧本、漫画/漫剧素材共用世界设定，按需检索上下文并限定字段写回，支持节点流程、插件，还能从作品派生跑团等互动体验<br><sub>方法：规划 · 设定 · 记忆 · 共创</sub><br><sub>更新于 2026-10-26 · 🧩 应用 · 多语言 · MIT</sub><br><sub>💡 README 有九种语言，正文以中文为主；可经 Codex app-server 复用 ChatGPT 登录；含插件作者包 zip；漫剧部分只做到分镜交付包</sub>

- **[QMAI](https://github.com/Mochocyang/QMAI)** · ★ 842<br>总纲→卷纲→17 节章纲三级大纲；每章定稿后摄取摘要/人物状态/伏笔/图谱，写前按优先级组装上下文混合检索；拆文库提取文风与角色，六维审查<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-10-26 · 🧩 应用 · 中文 · 129 个 skill</sub><br><sub>💡 Tauri 桌面应用，官网 qmai.pro；许可证非标准声明（NOASSERTION）</sub>

- **[inliver233/Ai-Novel](https://github.com/inliver233/Ai-Novel)** · ★ 794<br>自托管长篇写作平台：项目→大纲/细纲→章节，角色与世界观条目结构化存储，pgvector 检索故事记忆注入生成，可调试 Prompt 模板并批量生成<br><sub>方法：规划 · 设定 · 人物 · 记忆</sub><br><sub>更新于 2026-07-28 · 🧩 应用 · 中文</sub><br><sub>💡 README 对应 lite 分支；部署需 Docker Compose（PostgreSQL + pgvector、Redis）</sub>

- **[easy-writing](https://github.com/yilujian/easy-writing)** · ★ 747<br>本地网文写作桌面软件：工作流一键建书（灵感→大纲→设定→逐章自动生文，可断点续），配合续写、润色扩写和大纲/角色/时间线资料库<br><sub>方法：规划 · 记忆 · 共创</sub><br><sub>更新于 2026-10-20 · 🧩 应用 · 中文 · 20 个 skill · AGPL-3.0</sub><br><sub>💡 Tauri 桌面应用，BYOK；提示词为本地 md 可改；附竞品拆书与榜单爬虫；AGPL-3.0，另有商业授权</sub>

- **[show-me-the-story](https://github.com/Nigh/show-me-the-story)** · ★ 630<br>长篇小说本地应用：设定角色与世界观后分批生成大纲，逐章起草、审阅、定向修订；抽取带出处的事实、追踪伏笔、提出设定变更，最后全书校对<br><sub>方法：规划 · 设定 · 记忆 · 修订</sub><br><sub>更新于 2026-10-15 · 🧩 应用 · 多语言 · MIT</sub><br><sub>💡 单个 Go 可执行文件，需 OpenAI 兼容 API；Release 提供预编译包，源码完整；支持导入已有作品续写</sub>

- **[kimi-writer](https://github.com/Doriandarko/kimi-writer)** · ★ 596<br>kimi-k2-thinking 自主写作 agent：模型自己规划并调用建项目、写文件工具逐章写小说或短篇集，接近上下文上限时自动压缩并存摘要以便断点恢复<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2026-01-29 💤 · ⚙️ 框架 · 英文</sub><br><sub>💡 需 Moonshot API；方法较轻，按影响力收录（595★）；2026-01 后无更新</sub>

- **[character-arc](https://github.com/uu201/character-arc)** · ★ 591<br>桌面小说工作台：设定、角色关系、分卷大纲绑定章节，初稿流程为写作备忘→初稿→审计→自动修复/去 AI 味，配创作记忆、拆书知识库与 Skill 路由<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-10-24 · 🧩 应用 · 中文 · 29 个 skill · MIT</sub><br><sub>💡 Electron；内置 Distilled-Novel-Toolbox 等 Skill 包；支持 Codex CLI、OpenAI 兼容与 Anthropic 接口</sub>

- **[vela](https://github.com/heider-x/vela)** · ★ 583<br>本地优先的小说写作 IDE：世界观与人物档案→结构骨架→章节细纲→流式成章，再走重写→精修→审阅三级后处理，本地 RAG 召回设定<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-10-19 · 🧩 应用 · 多语言 · GPL-3.0</sub><br><sub>💡 README 带 API 中转平台推广码；另提供 dmg/exe 安装包</sub>

- **[OmniSpace](https://github.com/Yzw202011/OmniSpace)** · ★ 529<br>本地 AI 创作工作站的写作台：灵感→卷/章大纲树，按章数与字数参数批量生成章节，伏笔烂尾预警，三档降 AI 味文风；剧本可直通漫画与漫剧<br><sub>方法：规划 · 记忆 · 去 AI 味</sub><br><sub>更新于 2026-09-20 · 🧩 应用 · 中文</sub><br><sub>💡 综合平台（对话/漫画/漫剧/写作/知识学习），写作只是其中一个模块；默认本地 GPU 推理，可接云端 API；无开源许可证，README 称最新进度暂未提交</sub>

- **[goink](https://github.com/sigpanic/goink)** · ★ 480<br>对话式 Agent 调 31 个工具自查自改，结构化追踪角色关系图、伏笔回收期、弧线节点、地点图和读者认知，写完强制维护；可从样文蒸馏仿写 Skill<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-10-25 · 🧩 应用 · 中文 · 2 个 skill · AGPL-3.0</sub><br><sub>💡 Go + Wails 桌面应用，内置 BGE 本地语义检索和 Git 版本；Skill 分内置/用户/单书三层覆盖，可开审稿子 Agent</sub>

- **[tianming-novel-ai-writer](https://github.com/zy-zmc/tianming-novel-ai-writer)** · ★ 455<br>每章正文须附 12 类变更声明，经引用、一致性、外貌描写、蓝图出场等六道门禁才落地，再回写 15 维事实快照供下章读取；大纲→分卷→章节→蓝图四层规划<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-10-04 · 🧩 应用 · 中文</sub><br><sub>💡 Windows WPF 桌面端，内置拆书爬虫；作者称部分新源码丢失、开源版有功能缺失并转向新项目，仓库混有 bin/Debug 编译产物；提示词版见 zy-zmc/tianming-skill</sub>

- **[AI_Gen_Novel](https://github.com/cjyyx/AI_Gen_Novel)** · ★ 428<br>按写作认知过程模型（计划-转换-审阅）组织多 agent 写网文，借鉴 RecurrentGPT 循环生成：把前文压缩成几句记忆，再迭代续写任意长度<br><sub>方法：规划 · 记忆 · 多智能体</sub><br><sub>更新于 2024-09-04 💤 · ⚙️ 框架 · 中文 · MIT</sub><br><sub>💡 2024-09 后未更新（427★）；需要自己实现 LLM.py 的 chatLLM 接口；作者结论是当前 LLM 还写不好长篇网文</sub>

- **[WenShape](https://github.com/unitagain/WenShape)** · ★ 419<br>长篇小说智能体：卷章结构+人物/世界/文风卡，事实按章节距离衰减与 BM25 选择注入，Writer/Editor/Archivist 分工，可抓百科建同人设定<br><sub>方法：设定 · 记忆 · 多智能体</sub><br><sub>更新于 2026-10-03 · 🧩 应用 · 中文</sub><br><sub>💡 原名 NOVIX；许可证为 NOASSERTION，商用前看清条款</sub>

- **[iLearn-Lab/NovelClaw](https://github.com/iLearn-Lab/NovelClaw)** · ★ 378<br>以动态记忆为核心的长篇协作写作平台：会话、故事板、人物和世界面板、可编辑记忆库，逐章起草，每次运行的日志和稿件都可检查<br><sub>方法：规划 · 记忆 · 多智能体 · 共创</sub><br><sub>更新于 2026-10-12 · 🧩 应用 · 多语言 · MIT</sub><br><sub>💡 出自 HITSZ 团队（CoLong-Idea-Studio），有在线版；仓库根目录带一个 ISTask.dll（Inno Setup 插件），本地运行前留意</sub>

- **[MirrorNovel](https://github.com/Aerdelan/MirrorNovel)** · ★ 372<br>长篇平台：大纲确认后 AI 提阶段、支线、反转蓝图再写正文，持久化章节摘要、伏笔、角色状态和情绪曲线，每章专家团审稿修订，两遍去 AI 味<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-24 · 🧩 应用 · 中文</sub><br><sub>💡 需 MongoDB；桌面版只是外壳，默认连作者服务器（可改成自己的）；内置番茄小说下载器需 SVIP 账号；拆书蒸馏功能暂时移除</sub>

- **[ReaDreamAI](https://github.com/NEKOparapa/ReaDreamAI)** · ★ 367<br>从一个创意出发由 AI 依次构建世界观、角色与情节写成长篇，再按场景为书生成插图并锁定角色形象，可一键转短剧视频或恋爱 AI 游戏<br><sub>方法：规划 · 设定 · 人物</sub><br><sub>更新于 2026-10-13 · 🧩 应用 · 中文 · GPL-3.0</sub><br><sub>💡 Flutter 全平台；重心偏插图/视频，需 DeepSeek、火山等接口或本地 ComfyUI；README 对写作流程着墨不多</sub>

- **[AIxiezuo](https://github.com/yefeng2renxing/AIxiezuo)** · ★ 357<br>按章节大纲生成正文，写完由 LLM 更新主角状态 JSON（境界、物品、关系、剧情摘要）和版本化世界设定，下一章自动注入；可多模型多版本对比<br><sub>方法：设定 · 记忆</sub><br><sub>更新于 2025-07-21 💤 · 🧩 应用 · 中文</sub><br><sub>💡 基于 LangChain 的 Web 工具；无 License；2025-07 后未更新</sub>

- **[Hurricane0698/novelwriter](https://github.com/Hurricane0698/novelwriter)** · ★ 295<br>长篇续写的世界模型引擎：从正文提取实体、关系、体系成结构化世界模型（作者审核），续写时只注入本章相关设定，多版本草稿由作者采纳<br><sub>方法：设定 · 记忆 · 共创</sub><br><sub>更新于 2026-09-20 · 🧩 应用 · 中文 · AGPL-3.0</sub><br><sub>💡 AGPL-3.0；有 Windows/macOS 桌面版和 Docker 自部署；需 OpenAI 兼容 API</sub>

- **[tyxben/AI_novel](https://github.com/tyxben/AI_novel)** · ★ 276<br>长篇 5 agent：架构师出骨架，卷导演出细纲，章规划从伏笔/叙事债务账本组装章前简报，写手写章，审稿只标问题；7 维评估，伏笔兑现率设硬门禁<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-08-18 · ⚙️ 框架 · 中文 · MIT</sub><br><sub>💡 仓库同时是小说转短视频（推文）流水线；小说模块有 CLI、Web UI 和 MCP Server（README 写可由 Claude Code 调用）</sub>

- **[AIStoryWriter](https://github.com/datacrystals/AIStoryWriter)** · ★ 258<br>从一段提示词先生成全书大纲，再拆章节大纲，逐章分阶段写情节、人物、对白，每步经 LLM 评审反馈修订；大纲、章节、修订可各配不同模型<br><sub>方法：规划 · 修订</sub><br><sub>更新于 2025-11-24 💤 · ⚙️ 框架 · 英文 · AGPL-3.0</sub><br><sub>💡 命令行工具，默认 Ollama 本地模型，也支持 Google / OpenRouter；附 Evaluate.py 评测脚本；2025-11 后未更新</sub>

- **[kele-tao/AI_Novel](https://github.com/kele-tao/AI_Novel)** · ★ 257<br>小说写作台：按题材模板生成大纲后实时逐章写，每章先写章节计划再动态更新世界观，滑动窗口固定上下文长度，可暂停改设定或单章重写<br><sub>方法：规划 · 设定 · 记忆</sub><br><sub>更新于 2026-07-30 · 🧩 应用 · 多语言 · Apache-2.0</sub><br><sub>💡 也能生成课程讲义（非虚构）；接任意 OpenAI 兼容接口，作者推荐 vLLM / LM Studio</sub>

- **[ReNovel-AI](https://github.com/BiranSama/ReNovel-AI)** · ★ 250<br>导入现有小说分章入向量库，Writer 按指令与保留度/扩写度逐段改写扩写，独立 Reviewer 查 OOC 与逻辑漏洞并拦截，可全书批量精修续跑<br><sub>方法：记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-10-14 · 🧩 应用 · 中文 · GPL-3.0</sub><br><sub>💡 定位是重写/扩写已有文本（含 NSFW 加料）；需 OpenAI 兼容接口；Windows 绿色版在 Releases</sub>

- **[yangqi1309134997-coder/ai-novel-generator](https://github.com/yangqi1309134997-coder/ai-novel-generator)** · ★ 244<br>长篇生成平台：雪花法从核心创意分层展开大纲，按章节蓝图（情节节点、角色弧线、场景）逐章写，再做风格润色去 AI 味和跨章连贯性检测<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-04-04 💤 · 🧩 应用 · 中文</sub><br><sub>💡 分本地 Gradio 版和商业版（会员、卡密、支付）；README 声明公司版权，许可证却写 MIT</sub>

- **[EasyNovelAssistant](https://github.com/Zuntan03/EasyNovelAssistant)** · ★ 236<br>日语本地 LLM 小说助手：多标签提示词加引言提示词按章拼接（附 GoalSeek 分章写作样例），本地无限循环生成，从中挑好的段落累积成文<br><sub>方法：规划 · 共创</sub><br><sub>更新于 2024-07-05 💤 · 🧩 应用 · 日文 · MIT</sub><br><sub>💡 基于 KoboldCpp 与本地模型，主打无审查、可生成成人内容；附 Style-Bert-VITS2 朗读；2024-07 后未更新，按 ≥100★ 收</sub>

- **[loom-novel](https://github.com/WadeZhao23/loom-novel)** · ★ 228<br>设定师→大纲师→写手→编辑→润色师五道工序读「外置大脑」写一章；从作者手改中蒸馏写作指纹，每章自动查跨章矛盾并记状态账本<br><sub>方法：记忆 · 多智能体 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-08-27 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 Mac/Windows 桌面端；默认 DeepSeek，也可接其他国产模型或复用本机 Claude Code/Codex 登录；内置 38 个题材速查</sub>

- **[scriverse](https://github.com/musnows/scriverse)** · ★ 227<br>长篇小说本地工作台：设定库、组织、时间线看板、人物关系图、大纲与伏笔埋收提醒集中管理，AI 续写时引用章节行与角色设定，另有一致性分析<br><sub>方法：规划 · 设定 · 记忆</sub><br><sub>更新于 2026-10-17 · 🧩 应用 · 中文 · 2 个 skill · AGPL-3.0</sub><br><sub>💡 Node/Docker 部署，带 CLI；内置续写与润色 skill</sub>

- **[Writingway](https://github.com/a-omukai/Writingway)** · ★ 196<br>桌面小说写作工具：项目按章/场景组织，Compendium 设定库按提及动态注入上下文，配 POV 设置、场景摘要和可自定义提示词，在场景中生成与改写正文<br><sub>方法：设定 · 记忆</sub><br><sub>更新于 2026-07-25 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 类似 Novelcrafter 的开源替代（PyQt）；README 部分仍是占位文本，功能需看源码或 Discord</sub>

- **[NovelWriter_public](https://github.com/tuxiangxianzhe/NovelWriter_public)** · ★ 191<br>大纲/即兴双模式写小说：架构→目录（悬念节奏、伏笔）→逐章生成→定稿更新摘要和角色状态，另有文风仿写、叙事 DNA、作者参考库和多轮去 AI 痕迹<br><sub>方法：规划 · 记忆 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-05-26 · 🧩 应用 · 中文 · AGPL-3.0</sub><br><sub>💡 基于 YILING0013/AI_NovelGenerator；带「XP 预设」（内容偏好），可能涉及成人向内容</sub>

- **[dramatica-flow](https://github.com/ydsgangge-ux/dramatica-flow)** · ★ 190<br>Dramatica 理论驱动的长篇引擎：建筑师→写手→硬规则校验→审计员→修订者五层管线，维护因果链、伏笔生命周期、角色信息边界和世界状态<br><sub>方法：理论 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-09-23 · 🧩 应用 · 中文</sub><br><sub>💡 带 Web UI 与 CLI；支持 DeepSeek / Ollama / OpenAI 兼容接口；仓库未声明许可证</sub>

- **[storycraftr](https://github.com/raestrada/storycraftr)** · ★ 175<br>命令行写书：建项目后分步生成世界观、人物与大纲、章节摘要，再逐章写作并迭代修订，用本地嵌入模型做 RAG 检索保持设定一致<br><sub>方法：规划 · 设定 · 记忆</sub><br><sub>更新于 2026-03-06 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 支持 OpenAI / OpenRouter / Ollama；附 VS Code 扩展；最近更新 2026-03，按 ≥100★ 收</sub>

- **[GOAT-Storytelling-Agent](https://github.com/GOAT-AI-lab/GOAT-Storytelling-Agent)** · ★ 167<br>主题→书籍设定（类型/视角/人物/前提）→增强→分幕分章情节→增强→拆成场景→结合上一场景逐场写，可在任意层级介入<br><sub>方法：规划 · 修订</sub><br><sub>更新于 2025-11-12 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 默认用自家 GOAT-70B-Storytelling 模型，可接 TGI/llama.cpp；HF 上附 20 部无人工干预生成的中篇</sub>

- **[KazKozDev/NovelGenerator](https://github.com/KazKozDev/NovelGenerator)** · ★ 155<br>从一段前提生成整本小说：先建人物、世界规则、因果图和章节图并自审，逐场景写，事实抽取必须引用原段落，场景交接后重定下一场的因果计划<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-10-09 · 🧩 应用 · 英文</sub><br><sub>💡 writer 和 editor 双模型分工；支持 Gemini 和本地 Ollama；source-available 许可</sub>

- **[Xiaoyangy/novel-studio](https://github.com/Xiaoyangy/novel-studio)** · ★ 149<br>先冻结全书章位并整弧预演，重要角色以独立 agent 在至多 3 章窗口内决策、世界仲裁者裁决后果，封存章节合同后逐章渲染审核，验收正文才入正史台账<br><sub>方法：规划 · 记忆 · 模拟 · 修订</sub><br><sub>更新于 2026-09-23 · ⚙️ 框架 · 中文 · 20 个 skill · Apache-2.0</sub><br><sub>💡 Go CLI + 只读 Dashboard；RAG（embedding + Qdrant）可选；仓库附 20 个 SKILL.md；建议审稿角色单独路由 DeepSeek</sub>

- **[OrisonSpace](https://github.com/LumenStorm/OrisonSpace)** · ★ 146<br>小说 IDE：大纲、章节、人物/世界观资产卡同处一个工作区，AI 生成/续写/审阅以可回退 diff 落地，Story Sync 从正文抽设定补丁<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-07-17 · 🧩 应用 · 中文 · Apache-2.0</sub><br><sub>💡 Alpha；定位用户主导、AI 辅助；Agent 编排与 Auto Mode 为实验功能；Release 提供安装包，仓库源码完整</sub>

- **[xunlong](https://github.com/jaguarliuu/xunlong)** · ★ 134<br>LangGraph 多 agent 内容生成 CLI：小说模式按类型和章数先设计大纲再逐章创作并做人物一致性检查，可导入设定文档，支持局部/全局迭代修改<br><sub>方法：规划 · 多智能体 · 修订</sub><br><sub>更新于 2025-10-25 💤 · ⚙️ 框架 · 多语言 · MIT</sub><br><sub>💡 同时做研究报告与 PPT，小说只是三种模式之一；2025-10 后未更新，但 ≥100★</sub>

- **[Fibb](https://github.com/Ckokoski/Fibb)** · ★ 126<br>研究→大纲→逐章写→修订的自主流水线；三层记忆加夜间整理，按实体库查矛盾，角色分身审自己台词，评判→修订→复评只留变好的版本<br><sub>方法：规划 · 人物 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-07-11 · 🧩 应用 · 英文 · 48 个 skill · MIT</sub><br><sub>💡 README 名为 AuthorAgent（克隆地址仍是 authoragent）；同时面向非虚构，另带选题调研、宣发模块；需自备模型 API key</sub>

- **[narralume](https://github.com/abligail/narralume)** · ★ 124<br>长篇写作环境：作者意图、大纲、实体、正典事实、时间线、伏笔共用一份故事圣经，AI 正文和设定变更都先作候选，审稿附证据，撞上锁定事实就暂停<br><sub>方法：规划 · 记忆 · 修订 · 共创</sub><br><sub>更新于 2026-10-22 · 🧩 应用 · 多语言 · Apache-2.0</sub><br><sub>💡 不接模型也能纯手写；AI 长任务有检查点和运行记录；Docker 或脚本自部署，有托管 demo</sub>

- **[gptauthor](https://github.com/dylanhogg/gptauthor)** · ★ 118<br>人写故事提示（风格、人物）→AI 生成带各章摘要的梗概→人工审阅可重生成→按梗概加上一章逐章写出长篇<br><sub>方法：规划 · 共创</sub><br><sub>更新于 2026-08-15 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 pip 可装的命令行工具，故事提示用 YAML 描述</sub>

- **[saga](https://github.com/Lanerra/saga)** · ★ 114<br>前提→大纲→逐场景草稿→导出：Neo4j 知识图谱追踪人物、事件与关系，嵌入检索补上下文，LangGraph 检查点可中断续跑，自动质量验收<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-09-15 · ⚙️ 框架 · 英文 · Apache-2.0</sub><br><sub>💡 需自备 OpenAI 兼容文本接口、Ollama 嵌入接口与 Neo4j；仅验证 Linux；README 自述修复后的流程只在约 2 章、8 场、6700 词的项目上跑通过</sub>

- **[narracat-novel-agent](https://github.com/yannikzz/narracat-novel-agent)** · ★ 110<br>网文桌面应用：立项卡定题材和金手指→大纲→章纲→成稿，NovelMemory 长程记忆追踪伏笔，能力包从书中学写法，写作 agent/skill 提示词全开源<br><sub>方法：规划 · 人物 · 记忆 · 风格</sub><br><sub>更新于 2026-10-18 · 🧩 应用 · 中文 · 7 个 skill · AGPL-3.0</sub><br><sub>💡 自带 API Key；默认收集匿名使用统计（首次启动告知，可关闭）；AGPL-3.0</sub>

- **[Storydex](https://github.com/TensorHub-ORG/Storydex)** · ★ 105<br>本地长篇写作台：Agent 先查全文、章节摘要、相关旧文和 WIKI 再续写或修改，写入以 Diff 审阅、Git 记版本可回滚，内置连续性、悬疑、润色技能<br><sub>方法：记忆 · 修订</sub><br><sub>更新于 2026-10-22 · 🧩 应用 · 中文 · 6 个 skill</sub><br><sub>💡 许可证为 Apache-2.0 + Commons Clause（限制商用）；仓库自带 MinGit 的 exe/dll 和 Android bootstrap zip 等第三方二进制</sub>

- **[MetaNovel-Engine](https://github.com/hahagood/MetaNovel-Engine)** · ★ 103<br>命令行七步写长篇：一句话主题→AI 扩展并推荐类型→角色/场景/道具设定→故事大纲→分章细纲→章节概要→正文，每步可编辑重生成，提示词按项目隔离<br><sub>方法：规划 · 设定 · 人物</sub><br><sub>更新于 2025-11-06 💤 · ⚙️ 框架 · 中文 · MIT</sub><br><sub>💡 需要 OpenRouter API</sub>

- **[plotbunni](https://github.com/MangoLion/plotbunni)** · ★ 102<br>开源小说写作套件：幕→章→场景三级规划，场景链接设定概念库，AI 按大纲与关联概念生成梗概和场景正文，6 类任务提示词与模型可分别配置<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2026-04-19 💤 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 可用 AI Horde 社区免费模型</sub>

- **[siming-ai](https://github.com/teangtang1122/siming-ai)** · ★ 101<br>长篇小说本地工作台：一句想法→卷纲与前 3 章细纲（场景节点）；写作时按预算选取角色当前状态、伏笔与时间线，写后更新叙事账本<br><sub>方法：规划 · 设定 · 人物 · 记忆</sub><br><sub>更新于 2026-10-18 · 🧩 应用 · 中文 · Apache-2.0</sub><br><sub>💡 Release 提供 Windows 安装包，源码完整；可导入 TXT 建档后续写；可把 Claude Code/Codex/OpenCode 当模型后端；有 Android 端</sub>

- **[blackzhanzhan/novel_agent](https://github.com/blackzhanzhan/novel_agent)** · ★ 91<br>Git 原生的长篇网文工作台：导入小说蒸馏世界观、协作出大纲、生成续写草稿后审核归档，章节和剧情分支用 Git 管理，可回滚<br><sub>方法：规划 · 记忆 · 修订 · 共创</sub><br><sub>更新于 2026-05-27 · 🧩 应用 · 中文</sub><br><sub>💡 依赖 Dify 编排工作流；提供 Docker 和 Release 包部署</sub>

- **[InkAI-](https://github.com/yan2959088709/InkAI-)** · ★ 91<br>规划器先出全书蓝图和结构化章节卡（节拍、必现元素、伏笔编号、章末钩子），写作器按卡生成后硬校验、失败带反馈重写，跨章状态快照注入下一章<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-08-01 · ⚙️ 框架 · 中文</sub><br><sub>💡 题材规则包（文风、禁用语）贯穿规划与写作；默认阿里云百炼，可切 DeepSeek/OpenAI；有 Flask Web 界面；仓库无许可证</sub>

- **[AI_NovelCraft-](https://github.com/15673312611/AI_NovelCraft-)** · ★ 89<br>先生成含主线/支线/伏笔/角色弧线的超级大纲并拆卷、写章节细纲，按项目/卷/章管理上下文逐章流式生成，最后用消痕提示去 AI 味<br><sub>方法：规划 · 记忆 · 去 AI 味</sub><br><sub>更新于 2026-04-20 💤 · 🧩 应用 · 中文</sub><br><sub>💡 Java + React 平台，作者另有在线版；License 未声明标准协议；同作者的 AnimaHub 是视频平台，未收</sub>

- **[eliumusk/ai-novel-writer](https://github.com/eliumusk/ai-novel-writer)** · ★ 88<br>PyQt 写作应用：Gemini 按全书大纲和章纲生成正文，SQLite 存角色、关系和章节摘要，自动摘要并追踪情节线与伏笔，支持文风模仿<br><sub>方法：规划 · 人物 · 记忆 · 风格</sub><br><sub>更新于 2025-01-09 💤 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 需 Gemini API</sub>

- **[Narraverse-Engine](https://github.com/wssyh339/Narraverse-Engine)** · ★ 87<br>长篇大纲与世界观推演工作室：LangGraph swarm 多 agent 回合制议事，维护正典库和关系图谱，推演世界规则、大纲、伏笔和正文，人工确认后入库<br><sub>方法：规划 · 设定 · 记忆 · 多智能体</sub><br><sub>更新于 2026-07-22 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 0.2.0 Alpha；Docker Compose 一键启动，数据存本地 SQLite</sub>

- **[EdwardAThomson/NovelWriter](https://github.com/EdwardAThomson/NovelWriter)** · ★ 82<br>多类型小说写作 GUI：按类型套路生成宇宙设定、势力和人物，再做结构大纲、场景规划和逐章正文，多 agent 编排，多级审阅<br><sub>方法：规划 · 设定 · 多智能体 · 修订</sub><br><sub>更新于 2026-10-10 · 🧩 应用 · 英文</sub><br><sub>💡 Tkinter 界面；可走 API 或本地 codex/gemini/claude CLI；作者另有 EdwardAThomson/StoryDaemon</sub>

- **[obsidian-writing-buddy](https://github.com/xtenlab/obsidian-writing-buddy)** · ★ 79<br>Obsidian 长篇写作插件：Recanta 小说记忆追踪事件、状态、关系与角色所知，按写到的位置供上下文；续写、改写、一致性检查先出 diff 再采纳<br><sub>方法：记忆 · 修订 · 共创</sub><br><sub>更新于 2026-09-23 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 原 onezeroooo/obsidian-writing-buddy，已转移到 xtenlab（API 重定向确认）；作者主写、AI 出候选为主；自带模型 Key</sub>

- **[StoryMoss](https://github.com/91zgaoge/StoryMoss)** · ★ 78<br>主创、管理、编辑审计三代理黑板协作，每章过加权质量门才交付；续写前检索前文原文，按书纲→卷纲→章纲规划，正文写完自动回流角色/设定/伏笔入库<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-10-26 · 🧩 应用 · 中文 · 37 个 skill</sub><br><sub>💡 Tauri+Rust 桌面应用，支持 OpenAI/Anthropic/Ollama；另有 StyleDNA 文风、拆书、按公版人类语料校准的 AI 腔检测；GitHub 未识别许可证（README 徽章写 ISC），仓库根目录混有构建日志等杂项</sub>

- **[zenstory](https://github.com/zenstory-ai/zenstory)** · ★ 77<br>对话式小说工作台：路由按请求选五条流程，大纲规划师、爽点设计师、内容创作者、质量审稿人接力，超 500 字自动送审；每轮按预算注入 AI 记忆和相关文件<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-10-26 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 MIT 可自部署，另有官方在线版 app.zenstory.ai；外部 agent 通过 npx zenstory CLI 与 skill 接入</sub>

- **[john-paul-ruf/novel-engine](https://github.com/john-paul-ruf/novel-engine)** · ★ 76<br>七个 AI 编辑角色（故事教练、代笔、初读、发展编辑、校对等）走 15 步流程从 pitch 到出版稿，访谈作者建 Voice Profile 保持文风<br><sub>方法：规划 · 多智能体 · 修订 · 风格</sub><br><sub>更新于 2026-07-29 · 🧩 应用 · 英文 · AGPL-3.0</sub><br><sub>💡 Electron 桌面应用，AGPL；使用 Claude、Codex 或 Ollama；作者称已用其出版 10 本 Amazon 书</sub>

- **[ProseForge](https://github.com/remacheybn408-boop/ProseForge)** · ★ 74<br>六席位 agent 流水线：分析→四路并行场景草稿择优→连续性/对抗/文风三审合议→定点改写；章节摘要金字塔+承诺台账+叙事 RAG 防失忆<br><sub>方法：记忆 · 多智能体 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-22 · 🧩 应用 · 中文 · 87 个 skill · AGPL-3.0</sub><br><sub>💡 Docker 或原生安装包本地部署，模型走 OpenAI 兼容接口；packs/ 附 80 余个题材与技法 SKILL.md</sub>

- **[mythpen](https://github.com/niyongsheng/mythpen)** · ★ 73<br>桌面写作应用：写作模式下 AI 按六步工作流读设定和前章，写含认知、情感、悬念等五维度的章纲，再成文、润色；另有协作共写模式<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-10-26 · 🧩 应用 · 中文 · GPL-3.0</sub><br><sub>💡 Tauri 桌面，数据存本地 SQLite；作者另有 Claude Code 工作流版 niyongsheng/clark-typer</sub>

- **[AIStoryBuilders](https://github.com/AIStoryBuilders/AIStoryBuilders)** · ★ 72<br>把小说拆成时间线、地点、人物（按时间线分段描述）和章节段落的数据结构，写每段时按其时间线、地点和出场人物取对应设定作上下文<br><sub>方法：规划 · 设定 · 人物 · 记忆</sub><br><sub>更新于 2026-06-20 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 C# .NET MAUI 桌面应用，另有在线版和微软商店版；需 OpenAI / Azure OpenAI Key</sub>

- **[StoryCrafter](https://github.com/FartyPants/StoryCrafter)** · ★ 66<br>text-generation-webui 扩展：按 beat 逐段提示生成，每段可存三个版本，Future Cues 指令作用于后续段落以保持连续<br><sub>方法：规划 · 记忆 · 共创</sub><br><sub>更新于 2025-08-07 💤 · ⚙️ 框架 · 英文</sub><br><sub>💡 须装在 extensions/StoryCrafter；在作者旧扩展 BlockWriter 基础上扩展；仓库无许可证</sub>

- **[AI-Book-Generator](https://github.com/SimonWaldherr/AI-Book-Generator)** · ★ 64<br>浏览器端写书工具：先生成书名候选和概念（logline、前提、主题），再出带章节目的的大纲，带前文摘要逐章写作，可一键 Agent 模式跑完<br><sub>方法：规划</sub><br><sub>更新于 2026-03-16 💤 · 🧩 应用 · 英文 · GPL-3.0</sub><br><sub>💡 小说与非虚构通用；支持 OpenAI / Claude / Gemini，可生成封面</sub>

- **[huihuijiangqiang/moshu](https://github.com/huihuijiangqiang/moshu)** · ★ 63<br>长篇网文工作台：卷纲、章纲和场景卡（POV、目标、阻力、转折、钩子）配 pgvector 设定库与时间线检索生成候选正文，再过一致性守卫和自然化审查<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-09-27 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 自部署需 PostgreSQL/pgvector、Redis、Celery；含积分计费和漫剧分镜管理模块；有在线体验站</sub>

- **[nest-drama](https://github.com/63435212cwu-ops/nest-drama)** · ★ 58<br>从素材提炼世界观、必达/弹性剧情节点和角色三卡；角色是信息隔离的独立 agent 自主行动，舞台监督调度、监督者审人性，剧情经世界内因果收敛到节点<br><sub>方法：设定 · 人物 · 模拟 · 去 AI 味</sub><br><sub>更新于 2026-09-13 · 🧩 应用 · 中文 · AGPL-3.0</sub><br><sub>💡 纯 Python 标准库本地网页应用，需 OpenAI 兼容 API；README 推荐下载 Release zip，但仓库含完整源码；中英双语 README</sub>

- **[fictionforge](https://github.com/wanqili857-byte/fictionforge)** · ★ 56<br>每个角色是带记忆和信念的 agent，先演出事件；导演把多视角事件线合成章节 spec 再写，逐章过禁词/AI 腔门禁，不合格就返工<br><sub>方法：记忆 · 多智能体 · 模拟 · 修订</sub><br><sub>更新于 2026-10-01 · ⚙️ 框架 · 中文 · MIT</sub><br><sub>💡 README 首屏是从门禁里抽出的 CanonBench 长篇一致性基准（零 LLM 判定器，三档 harness 消融）；换小说只换内容包</sub>

- **[Novel-OS](https://github.com/mrigankad/Novel-OS)** · ★ 53<br>架构→执笔→编辑→守卫→整理五角色流水线，结果并入持久 story_state，确定性连续性引擎先查断线与时间漂移再交 LLM 审校<br><sub>方法：记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-08-09 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 浏览器写作工作室 + 无头 CLI；支持各家 OpenAI 兼容模型</sub>

- **[Chevoink](https://github.com/Xcy8010/Chevoink)** · ★ 52<br>长篇小说平台：Agent 按两级路由加载 Skill，Story Compiler 按章程→承诺→场景任务→章节衔接编排写作，过连续性与人类感质量门<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-10-25 · 🧩 应用 · 中文</sub><br><sub>💡 正文版本化可回滚；含书城阅读与社区；在线版按 Credits 计费，可自部署（React + PostgreSQL）</sub>

- **[novel-distiller](https://github.com/FutureFuzzy/novel-distiller)** · ★ 52<br>创世蓝图→为角色蒸馏思维 SKILL.md→蒸馏参考作者文风→多智能体推演场景→撰写→8 维锚定自检，YAML 数值状态层追踪暗线，叠加番茄/起点平台规则<br><sub>方法：人物 · 记忆 · 模拟 · 风格</sub><br><sub>更新于 2026-05-11 · ⚙️ 框架 · 中文 · 2 个 skill · MIT</sub><br><sub>💡 Python CLI 负责组装 prompt，LLM 推理交给 Claude Code；剧情推演借用 MiroFish 多智能体模拟思路；demo 含孙悟空、刘慈欣蒸馏</sub>

- **[lightnovel-studio](https://github.com/mmlong818/lightnovel-studio)** · ★ 50<br>一句话概念依次生成世界观、角色群、章节大纲再逐章写正文，附续写、角色对话和一致性/读者体验推敲，内置中日轻小说题材<br><sub>方法：规划 · 设定 · 人物 · 修订</sub><br><sub>更新于 2026-06-08 · 🧩 应用 · 多语言 · GPL-3.0</sub><br><sub>💡 纯前端，作品存浏览器 localStorage；支持 Gemini/Claude/OpenAI/兼容接口</sub>

- **[bloodycrownD/novel-master](https://github.com/bloodycrownD/novel-master)** · ★ 49<br>长篇写作 agent 工作台：世界观/人设/卷纲/章节放入虚拟文件树，目录级规则控制注入上下文的档位，只读分析/写作/资料整理多智能体分工，可派子代理<br><sub>方法：记忆 · 多智能体</sub><br><sub>更新于 2026-10-25 · 🧩 应用 · 中文 · 5 个 skill</sub><br><sub>💡 PolyForm Noncommercial 许可，禁止商用；桌面/安卓/CLI 三端；具体叙事方法需用户自建模板或导入 SKILL.md</sub>

- **[QianBi-Novel](https://github.com/GLFzr/QianBi-Novel)** · ★ 48<br>立项→设定→总纲→世界书与正则→细纲→正文六阶段共写；世界书按锚点注入，must 契约确定性复检，终审引证验真+三票投票，新设定回写<br><sub>方法：规划 · 设定 · 记忆 · 修订</sub><br><sub>更新于 2026-09-27 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 Windows 桌面应用（PySide6），BYOK 全本地；内置 10 套题材预设，含同人设定集导入路径</sub>

- **[curvedinf/novel-writer](https://github.com/curvedinf/novel-writer)** · ★ 46<br>三段脚本写长篇：先依次生成梗概、人物、场景设定、情节和标题（每步可重做、可手改 JSON），再逐章起草，最后定稿<br><sub>方法：规划 · 设定 · 人物</sub><br><sub>更新于 2024-04-11 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 README 极简；API Key 写在 writer.py；作者建议用 Gemini 做设定、Claude/GPT-4 写正文</sub>

- **[flutter-novel-main](https://github.com/xy9144/flutter-novel-main)** · ★ 46<br>按大纲→分卷规划→范围规划→章节规划→正文五级提示词逐章生成，用进度追踪文件支撑自动续写，可随机生成书名和题材<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2026-04-22 💤 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 Flutter 多端；支持 OpenRouter、Ollama 等自定义接口</sub>

- **[novel-agent-studio](https://github.com/skuramatata/novel-agent-studio)** · ★ 45<br>设定作者声音后对话生成总纲、人物关系、双时间线与章纲，按场景起草，审稿回查原文核对时间/知情并局部修订，采纳正文才提取带出处的故事记忆<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-09-18 · 🧩 应用 · 中文</sub><br><sub>💡 Electron 桌面应用，仅验证 macOS Apple Silicon；接 GLM / MiniMax；附 desktop-app/runtime/skills/novel-workflow/SKILL.md</sub>

- **[LLM-book-generator](https://github.com/fangfufu/LLM-book-generator)** · ★ 44<br>命令行整书生成：从选题、书名到章节大纲、分节正文和前后附文，小说会生成人物表，草稿分两遍写，scratchpad 存人物和地点<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-10-23 · ⚙️ 框架 · 英文 · GPL-3.0</sub><br><sub>💡 通用书籍生成器，也写非虚构（含 LaTeX 公式渲染）；需本地 llama.cpp server；输出 DOCX</sub>

- **[AnySpark](https://github.com/Mikexujunrui/AnySpark)** · ★ 42<br>对话驱动的小说智能体：主循环按需调用图谱查证、伏笔、剧情计划、设定检索等工具，再用无历史的干净上下文写章；可拆书提炼技巧 skill，角色推演多探索选优<br><sub>方法：规划 · 记忆 · 模拟 · 风格</sub><br><sub>更新于 2026-09-01 · 🧩 应用 · 中文</sub><br><sub>💡 Python 后端 + React 创作台 + 对话 CLI；默认接 DeepSeek；License 未声明标准协议</sub>

- **[StoryDaemon](https://github.com/EdwardAThomson/StoryDaemon)** · ★ 41<br>不预先列大纲，agent 按 story tick 循环自主规划、写场景并更新人物/地点记忆，配张力评分、目标层级、从 21 部经典小说测得的场景骨架和矛盾检测<br><sub>方法：理论 · 记忆 · 修订</sub><br><sub>更新于 2026-10-18 · ⚙️ 框架 · 英文</sub><br><sub>💡 无开源许可证；默认走 Codex CLI，也可接各家 API；作者前作 EdwardAThomson/NovelWriter 是大纲先行路线</sub>

- **[wanxiangpu-loreweft](https://github.com/EXwhitewood/wanxiangpu-loreweft)** · ★ 41<br>长篇小说工程台：Story Plan→章节蓝图→按场景生成，世界规则/人物/伏笔/状态账本约束，并行校验+受控修订+提交门禁，15 个分工智能体<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-08-25 · 🧩 应用 · 中文 · 36 个 skill · AGPL-3.0</sub><br><sub>💡 主要面向 Windows 桌面（Tauri）；AGPL-3.0</sub>

- **[OpenFicM](https://github.com/tioners/OpenFicM)** · ★ 40<br>安卓本地小说 Agent：读写章节、角色、世界书与三级笔记，可委派子智能体；参考书多轮蒸馏成文风约束，并对比 AI 原稿与作者定稿学习个人文风<br><sub>方法：规划 · 记忆 · 多智能体 · 风格</sub><br><sub>更新于 2026-10-08 · 🧩 应用 · 中文 · Apache-2.0</sub><br><sub>💡 基于 syrizelink/OpenFic 重构的 Android 版（非官方）；首次启动从 GitHub/Hugging Face 拉取 Agent/Skill 与本地检索模型</sub>

- **[ai-book-writer](https://github.com/agruai/ai-book-writer)** · ★ 39<br>CrewAI 五角色流水线：概念→大纲→分章写作→编辑→连续性检查，小说模式导出角色圣经和时间线 JSON 供连续性校验，带流式输出和预算控制<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2025-10-13 💤 · 🧩 应用 · 英文 · MIT</sub><br><sub>💡 也做非虚构书稿；需 OpenAI/Anthropic/Google Key，部署栈较重（PostgreSQL、Redis、K8s）；账号由 ai-joon 改名而来</sub>

- **[Morpheus](https://github.com/papysans/Morpheus)** · ★ 39<br>长篇小说工作台：多 agent 分担规划、设定、连续性、文风与裁决，L1/L2/L3 记忆加开放线程装配上下文，批量生成后按修改方向重做单章<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-03-22 💤 · 🧩 应用 · 中文</sub><br><sub>💡 默认 DeepSeek，支持 OpenAI 兼容接口；带知识图谱与轨迹回放；仓库无许可证</sub>

- **[Novelgen](https://github.com/kirinonakar/Novelgen)** · ★ 39<br>面向读者的小说生成器：输入种子生成分章情节，长篇分部生成和精修，靠分层上下文与滑动窗口记忆逐章写，可对照相邻章节自动出修改意见<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-10-22 · 🧩 应用 · 多语言 · MIT</sub><br><sub>💡 Tauri 桌面应用；支持 LM Studio、Ollama 本地模型和 Gemini 等云端；输出韩/日/英</sub>

- **[novelIDE](https://github.com/qq1375828505/novelIDE)** · ★ 39<br>安卓离线网文 IDE：主 Agent 调 40 多个工具读写角色、设定、伏笔资料库，委派大纲、角色、爽点检查、水文检测、去 AI 味等子 Agent 多轮推敲<br><sub>方法：记忆 · 多智能体 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-06-07 · 🧩 应用 · 中文</sub><br><sub>💡 Flutter 源码在仓库里；仓库还夹带日志压缩包和改 hosts 的 .bat 工具脚本</sub>

- **[inkflow](https://github.com/real-Elysia886/inkflow)** · ★ 37<br>战略→滚动 5 章大纲→上下文编排→写作→双层审计→事实提取→归档的多 agent 管线，7 类真相文件管人物、伏笔、资源、信息边界，可从样章蒸馏文风<br><sub>方法：记忆 · 多智能体 · 修订 · 风格</sub><br><sub>更新于 2026-05-21 · ⚙️ 框架 · 中文 · MIT</sub><br><sub>💡 架构和 Narcooo/inkos 高度相似（真相文件、资源账本、Plan→Compose→Write→Observe→Reflect），README 未注明来源；Python 重写，另加 Web 工作台和多书风格融合</sub>

- **[KKKenChow/ai-novel-writer](https://github.com/KKKenChow/ai-novel-writer)** · ★ 36<br>全链路写长篇：世界观→人物→大纲→场景卡逐段写；按六阶段放宽大纲可见范围、过滤剧透防抢跑，章后更新伏笔台账和滚动摘要，五维评审后改写<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-09-09 · 🧩 应用 · 中文 · 4 个 skill · MIT</sub><br><sub>💡 默认火山方舟豆包 API，也可接 OpenAI 兼容接口；能把写作技巧文章蒸馏成 skill 包按步骤注入；数据存本地 JSON</sub>

- **[lore-weave](https://github.com/letuhao/lore-weave)** · ★ 36<br>长篇共写平台：每章自动抽取人物、地点、事件和关系进知识图谱，聊天、共写与翻译都以此为据，批评 agent 对照正史检查建议<br><sub>方法：设定 · 记忆 · 修订</sub><br><sub>更新于 2026-10-05 · 🧩 应用 · 英文 · 31 个 skill · AGPL-3.0</sub><br><sub>💡 多服务自托管、体量很大；写作合成引擎仍在开发（Phase 3）；另含术语一致的多语翻译和 MMO RPG 扩展；AGPL-3.0</sub>

- **[novel-bot](https://github.com/xiaoxiaoxiaotao/novel-bot)** · ★ 35<br>文件系统即记忆的写作 agent：自动生成人设、世界观、角色卡、大纲等 Markdown 文件，全局记忆加章节摘要双记忆，每章写完自动更新<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2026-02-16 💤 · ⚙️ 框架 · 多语言 · 4 个 skill · MIT</sub>

- **[open-skoob](https://github.com/OmMaBaMiHong/open-skoob)** · ★ 34<br>网文多智能体工作室：意图卡→世界观→大纲→卷→章六步开书，每章规划→编排→执笔→审校→修订→结算六师接力；八师逆向拆书建图谱，写前可多轮仿真推演<br><sub>方法：规划 · 多智能体 · 模拟 · 修订</sub><br><sub>更新于 2026-10-13 · 🧩 应用 · 中文</sub><br><sub>💡 README 引导去 gaotk.com 中转站建 Key，拆书/仿真/检测等引擎走官方云端 API；许可证 NOASSERTION，另附商业许可；含同人支线与互动影游模式</sub>

- **[bragi](https://github.com/wailers9/bragi)** · ★ 32<br>架空世界故事引擎：用数字路径管理时间树与空间树，当前节点保留全文、邻近节点只留摘要按需扩写，结合角色状态与事件记录续写剧情<br><sub>方法：设定 · 人物 · 记忆 · 共创</sub><br><sub>更新于 2026-05-17 · ⚙️ 框架 · 中文</sub><br><sub>💡 CLI + 本地 Web UI；支持 OpenAI / DeepSeek，附离线 Demo Agent</sub>

- **[hongyue-creation](https://github.com/chen647208/hongyue-creation)** · ★ 32<br>本地桌面写作室：灵感→世界→角色→大纲/细纲→按细纲单章或批量生成正文，黄金三章、雪花法、POV、伏笔回收、去 AI 味等写法技能以 SKILL.md 渐进注入<br><sub>方法：规划 · 理论 · 设定 · 去 AI 味</sub><br><sub>更新于 2026-10-22 · 🧩 应用 · 中文 · 10 个 skill · AGPL-3.0</sub><br><sub>💡 Electron 应用，AI 是可关闭的增强层，也能纯手写；Agent 改稿走建议/改写/直接三档审批；AGPL-3.0，另有商业授权</sub>

- **[novel_writer_agent](https://github.com/nonever2109/novel_writer_agent)** · ★ 32<br>本地长篇写作助手：选题→大纲和章节计划→每章经规划、生成、修订、连续性检查、体验评估、风险检查，写完更新角色、时间线、伏笔和主支线记忆<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-05-13 · 🧩 应用 · 中文</sub><br><sub>💡 Windows 本地运行；每章约跑 20 个流程，Token 消耗大</sub>

- **[waqupin](https://github.com/zhou491145-tech/waqupin)** · ★ 31<br>VS Code 网文插件：全局/项目/章节分层记忆检索注入，人物档案记录章前章后状态，伏笔埋收追踪，节奏评级，作家风格模板精修<br><sub>方法：人物 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-09-19 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 开源的是核心层升级前的旧版代码，含激活码校验</sub>

- **[bookbuilder_ai](https://github.com/Nachoeigu/bookbuilder_ai)** · ★ 30<br>LangGraph 多 agent 写书：先追问需求，按激励事件、中点、高潮等结构出大纲，批评 agent 循环审稿，再出分章摘要并逐章写、逐章审<br><sub>方法：规划 · 理论 · 多智能体 · 修订</sub><br><sub>更新于 2025-01-31 💤 · ⚙️ 框架 · 英文</sub>

- **[Project-Wannabe](https://github.com/kawaii-justice/Project-Wannabe)** · ★ 30<br>配合小说微调模型 wanabi：先生成标题/梗概/设定/情节转入详情栏，再按「下一段展开指示」反复出候选卡片，人挑选插入正文<br><sub>方法：规划 · 共创</sub><br><sub>更新于 2026-06-01 · 🧩 应用 · 日文</sub><br><sub>💡 需本地 KoboldCpp 加载 wanabi 系列 GGUF 小说模型（含 Gemma 4 31B 版）；Windows 桌面应用</sub>

- **[1667](https://github.com/1667-ai/1667)** · ★ 29<br>终端/网页里写分支小说：每段保留多个生成版本组成故事树，Facts 按故事线锚定状态注入上下文，摘要节点压缩前文作为上下文重置<br><sub>方法：记忆 · 共创</sub><br><sub>更新于 2026-10-06 · 🧩 应用 · 英文 · Apache-2.0</sub><br><sub>💡 也可纯人工写；可接本地或云端模型，支持导入 SillyTavern 角色卡与 NovelAI 生成配置</sub>

- **[OpenNovel](https://github.com/Cppys/OpenNovel)** · ★ 29<br>LangGraph 多 agent：类型研究、故事架构、冲突设计出大纲，写作→编辑→审稿（含 AI 痕迹检测）不过即重写，ChromaDB 存章节摘要和角色状态<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-03-01 💤 · ⚙️ 框架 · 中文 · MIT</sub><br><sub>💡 依赖 Claude Code CLI 登录；可用浏览器自动化发布到番茄小说</sub>

- **[ElyHa](https://github.com/ShadowLoveElysia/ElyHa)** · ★ 28<br>图结构长篇写作：节点和边管理分支剧情，Planner→Writer→Reviewer→Synthesizer 写章并查设定一致性，AI 以幽灵节点提案、人工采纳<br><sub>方法：规划 · 多智能体 · 修订 · 共创</sub><br><sub>更新于 2026-04-02 💤 · 🧩 应用 · 多语言 · AGPL-3.0</sub><br><sub>💡 Web GUI + TUI，界面中英日；GitHub 识别为 AGPL-3.0（README 写 GPLv3）；仓库提交了 .venv-win 目录</sub>

- **[Jackn0/novel_agent](https://github.com/Jackn0/novel_agent)** · ★ 27<br>Next.js 写作助手：小说预设→大纲→章纲→小节列表→正文五阶段，每阶段 AI 起稿用户审定，追踪人物状态和伏笔，五档记忆等级，可导入旧作续写<br><sub>方法：规划 · 记忆 · 共创</sub><br><sub>更新于 2026-03-23 💤 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 附多角色有声书制作（Edge TTS / 百度 TTS）；支持 Claude 和 OpenAI 兼容接口</sub>

- **[lshu-novel-generator](https://github.com/TSOFTP-afk/lshu-novel-generator)** · ★ 27<br>长篇小说工作台：规划→写手→审计→修订四 Agent 写章并查 OOC 和 AI 痕迹，Truth File+RAG 管设定，可从参考书提炼写作 Skills<br><sub>方法：记忆 · 多智能体 · 修订 · 风格</sub><br><sub>更新于 2026-05-22 · 🧩 应用 · 中文</sub><br><sub>💡 Truth File 机制与 InkOS 类似；与 XiaoJiuAI/lingshu 同叫「灵枢」，但不是同一项目</sub>

- **[xiami](https://github.com/zhangxunvvv/xiami)** · ★ 27<br>长篇逐章流水线：世界观/总纲/细纲/人物卡/伏笔库/剧情账本约束连续性，每章推演→主笔→门禁→定向修复→账本结算，另有情绪钩子排布与读者速读模型<br><sub>方法：规划 · 理论 · 记忆 · 修订</sub><br><sub>更新于 2026-08-13 · 🧩 应用 · 中文</sub><br><sub>💡 Tauri 桌面应用，API Key 存 Windows 凭据管理器，主要面向 Windows；兼容任意 OpenAI 接口；仓库未声明许可证</sub>

- **[fiction-forge](https://github.com/geobond13/fiction-forge)** · ★ 26<br>Claude Code 通过 MCP 设定库按章节查人物已知信息；冷读协议带状态账本找连续性错误；按目标语料量化文风画像，扫描器防 AI 腔回潮<br><sub>方法：记忆 · 修订 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-07-26 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 总结自作者写完约 29 万字小说的经验；另含 EPUB/PDF 发布和 DALL-E 插图脚本</sub>

- **[MortalAINovel-AIWritingSystem-ai-](https://github.com/hezhengtao/MortalAINovel-AIWritingSystem-ai-)** · ★ 26<br>本地桌面写作软件：按书/卷/章管理，AI 续写、润色和风格模仿；角色档案可一键生成关系图谱，拆书知识库分析范文「文笔DNA」供仿写<br><sub>方法：人物 · 风格</sub><br><sub>更新于 2025-12-29 💤 · 🧩 应用 · 中文</sub><br><sub>💡 Releases 提供 Windows exe，源码可用 Streamlit 直接运行</sub>

- **[OpenNovelWriter](https://github.com/vibe-creator-art/OpenNovelWriter)** · ★ 25<br>类 Novelcrafter 的写作应用：章节、大纲、术语、摘要投影成文件交给 Codex 会话，靠 story-state 与上下文检索 skill 管上下文<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2026-10-17 · 🧩 应用 · 中文 · 12 个 skill · AGPL-3.0</sub><br><sub>💡 依赖本机 Codex CLI；作者提示 Codex 有本地写权限、可能改删稿件，只建议自托管自用；AGPL-3.0</sub>

- **[WorldScript-Studio](https://github.com/qnbs/WorldScript-Studio)** · ★ 24<br>本地优先的小说/剧本写作工作室：大纲生成器可把结构化提纲写进稿件，配人物与世界档案、故事圣经、节拍表，AI 可续写、生成对白与梗概<br><sub>方法：规划 · 设定 · 人物</sub><br><sub>更新于 2026-10-22 · 🧩 应用 · 多语言 · MIT</sub><br><sub>💡 以人写稿为主，AI 为可选能力（云端 BYOK、浏览器本地模型或 Ollama）；PWA + Tauri 桌面版</sub>

- **[DAWO](https://github.com/dawo4/DAWO)** · ★ 23<br>长篇网文桌面软件：一句话建书→设定集→分卷大纲→逐章生文，按卷和出场裁剪注入大纲与角色卡，悬置伏笔作硬约束注入，配六维去 AI 味打分<br><sub>方法：规划 · 记忆 · 多智能体 · 去 AI 味</sub><br><sub>更新于 2026-10-18 · 🧩 应用 · 中文</sub><br><sub>💡 仓库未附开源许可证（README 称暂未开源授权）；含 15 个提案制智能体、拆书与朱雀对抗手册；Windows 安装包未签名</sub>

- **[write-chinese-long-screenplay](https://github.com/mudden2380078550-creator/write-chinese-long-screenplay)** · ★ 23<br>中文长篇小说/剧本状态 harness：人物、能力、资源与作者政策存为正典，每章先组装章纲与写前状态，候选正文附状态变更，过检查才落盘<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-09-12 · ⚙️ 框架 · 中文 · 2 个 skill · GPL-3.0</sub>

- **[XZZKANY/StoryForge](https://github.com/XZZKANY/StoryForge)** · ★ 22<br>长篇小说桌面 IDE：Agent 用只读工具跨文件取证，做多视角审稿并产出修订补丁，作者看 diff 决定写回；配 canon 防漂移、一致性扫描和逐章生成<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-10-26 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 作者自述仍在自用阶段，30 章长程生成人工通读未通过；本地需 Docker 起 Postgres/Redis/MinIO</sub>

- **[ldblckrs-258/novel-studio](https://github.com/ldblckrs-258/novel-studio)** · ★ 21<br>越南语写作工作台：章节→全书→人物三阶段分析，六步自动写作（上下文→方向→大纲→写手→审稿→重写），另含中译越翻译、TTS 与爬虫导入<br><sub>方法：规划 · 修订</sub><br><sub>更新于 2026-09-29 · 🧩 应用 · 多语言 · MIT</sub><br><sub>💡 界面与提示词为越南语（lang 无对应项，暂填 multi）；数据存浏览器 IndexedDB；工具重心偏翻译</sub>

- **[Muses](https://github.com/zestor/Muses)** · ★ 21<br>GPT-3 长篇续写脚本：每场景依据上一场景、人物表、滚动摘要和随机情节队列生成，三选一取最长后补感官细节，再更新人物和摘要<br><sub>方法：人物 · 记忆 · 修订</sub><br><sub>更新于 2023-02-23 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 基于 GPT-3 / NLP Cloud 旧接口；可设定不会死亡的主角</sub>

- **[NovelWritingAgent](https://github.com/xindaaW/NovelWritingAgent)** · ★ 21<br>多 agent 写小说：先生成并收敛设定 canon，章节写→审→改，评审团并行打分再由总评汇总，修订经 canon_patch 反写设定，长期记忆分级检索<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-04-02 💤 · ⚙️ 框架 · 中文 · 8 个 skill · MIT</sub><br><sub>💡 各 agent 提示词以 SKILL.md 形式放在包内；有不调模型的骨架调试模式</sub>

- **[Closure](https://github.com/AoharuCat/Closure)** · ★ 20<br>小说 IDE：先在结构化叙事状态上操控信息差、情绪弧与角色欲望再落笔，每章抽取世界事件分「事实/读者所知」两本账，改设定沿依赖图追踪下游影响<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-11 · 🧩 应用 · 中文 · AGPL-3.0</sub><br><sub>💡 基于 LumenStorm/OrisonSpace 的派生版，叠加叙事状态机、混合检索、情绪闭环、风格卡与内嵌 llmlint 去 AI 味；接 OpenAI 兼容端点或经 Antigravity CLI 调 Gemini；AGPL-3.0</sub>

- **[arcvellum](https://github.com/o-1717986918/arcvellum)** · ★ 19<br>本地长篇创作工作室：项目 Agent 接长期目标交后台推进；每个场景作为事务，主创定意图并向角色续演、描写器取候选，经审查修订后提交并写回人物与 Canon<br><sub>方法：规划 · 记忆 · 模拟 · 修订</sub><br><sub>更新于 2026-10-17 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 Windows 安装包 + 完整源码，Beta；也支持剧本与伪纪录体；作者自述多题材长篇稳定性仍待验证；需自配模型</sub>

- **[inyhow/ai-novel-generator](https://github.com/inyhow/ai-novel-generator)** · ★ 19<br>网文 Web 应用 + SKILL.md：5 问确认题材、主角缺陷、冲突、节奏和篇幅，出总纲与角色弧线，逐章写并补悬念钩子，每 5 章查连贯，最后去 AI 味<br><sub>方法：规划 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-04-17 💤 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 根目录 SKILL.md 可单独当 skill 用；应用附番茄小说 CDP 自动发布和敏感词检测</sub>

- **[302_novel_writing](https://github.com/302ai/302_novel_writing)** · ★ 18<br>网页小说写作工具：填书名、作者和简介建书，AI 先生成章节剧情规划再写章节正文，可选现代/古风/奇幻等文风，也能全自动写完整本<br><sub>方法：规划</sub><br><sub>更新于 2025-08-26 💤 · 🧩 应用 · 多语言 · Apache-2.0</sub><br><sub>💡 302.AI 在线产品的开源版，需 302.AI API；界面中英日三语</sub>

- **[Novel](https://github.com/DuckTraDo/Novel)** · ★ 18<br>一句话 idea 生成整章，故事圣经/角色知情与秘密/伏笔/时间线组成文件记忆库，章后连续性审查并更新记忆，可挂 LoRA 文风<br><sub>方法：记忆 · 修订 · 风格</sub><br><sub>更新于 2026-06-03 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 Tauri 桌面应用（Rust 引擎）；可接本地 OpenAI 兼容推理，或调用本机已登录的 Claude Code / Codex 订阅；LoRA 权重在 Hugging Face</sub>

- **[StoryCanvas](https://github.com/ydsgangge-ux/StoryCanvas)** · ★ 18<br>在画布上摆放 35 类叙事块（角色、伏笔、冲突、读者情绪曲线等）并用 8 种关系连线，选故事卡搭初始结构，由五层 agent 管线生成细纲和正文，12 维审计<br><sub>方法：规划 · 理论 · 设定 · 修订</sub><br><sub>更新于 2026-09-23 · 🧩 应用 · 中文</sub><br><sub>💡 无开源许可证；也有剧本类块；支持 DeepSeek/OpenAI/Claude/Gemini/Ollama</sub>

- **[ai-webnovel-workflow](https://github.com/sanshanjianke/ai-webnovel-workflow)** · ★ 17<br>四层网文框架：种子层定故事愿景，多专家会议编排卷纲章纲并标注读者效果，叙事层查表把效果映射成视角/节奏/话语模式，渲染层按约束扩写正文<br><sub>方法：规划 · 理论 · 记忆 · 多智能体</sub><br><sub>更新于 2026-05-20 · 🧩 应用 · 中文 · 6 个 skill · MIT</sub><br><sub>💡 作者自述只完成约 30%；每层另有 .claude/skills 版本；用世界书、RAG 历史、RAG 技法三类数据支撑</sub>

- **[Book-Writing-AI-Agent](https://github.com/Aftabbs/Book-Writing-AI-Agent)** · ★ 17<br>CrewAI 顺序五 agent 写书示例：规划（大纲、人物、世界）→分章写作（每章千字以上）→编辑润色→事实核查→排版出稿<br><sub>方法：规划 · 多智能体 · 修订</sub><br><sub>更新于 2025-11-04 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 单个 Jupyter notebook；用 Groq 上的 LLaMA-3-70B</sub>

- **[knowrite](https://github.com/knoai/knowrite)** · ★ 17<br>小说写作后端：多 Agent 接力完成大纲、写章、审稿、去 AI 味和读者反馈，配时序事实库、作者指纹、RAG 记忆与提示词自动进化<br><sub>方法：记忆 · 多智能体 · 修订 · 风格</sub><br><sub>更新于 2026-05-09 · ⚙️ 框架 · 多语言 · AGPL-3.0</sub><br><sub>💡 Node.js 后端服务，图形界面需另装 knoai/knowrite-ui；AGPL-3.0；自配 OpenAI 兼容 API</sub>

- **[ai-novel-studio-lingshumiaobi](https://github.com/hshenwl/ai-novel-studio-lingshumiaobi)** · ★ 16<br>网文工业化平台：总纲→卷纲→章纲后走七步 agent 流水线（约束规划→写作→读者视角→编辑视角→20 维审核→修订去 AI 味→定稿回写角色/伏笔/Hook）<br><sub>方法：理论 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-05-12 · 🧩 应用 · 中文</sub><br><sub>💡 Windows 本地安装版（Go 启动器 + Inno Setup 打包脚本）；内置 645+ 篇写作知识库供规划阶段生成约束；同作者的 hshenwl/ai-novel-generator-genwenniu 是同源版本</sub>

- **[mushroomfk/novel-generator](https://github.com/mushroomfk/novel-generator)** · ★ 16<br>本地长篇工作台：导入资料建 FTS5+embedding 检索，生成整书架构与章节蓝图，逐章经正文生成→小说专用去 AI 改稿→一致性复查→核验，作者确认后写回<br><sub>方法：记忆 · 修订 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-06-14 · 🧩 应用 · 中文</sub><br><sub>💡 应用名「稿匣」，Tauri + Vue + FastAPI；可接入 Obsidian Vault、支持旧稿接管</sub>

- **[pulpgen](https://github.com/frobwick/pulpgen)** · ★ 16<br>CLI 写书 agent：Gemini 先生成标题、梗概、人物和逐章摘要，再按疏密策略分批写章，最后交互式 AI 编辑，XML 补丁记录状态可续跑<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2025-04-10 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 需 Gemini API、Python 3.13+；可导出 HTML/EPUB</sub>

- **[ApiSaverWriter](https://github.com/Vaxue/ApiSaverWriter)** · ★ 15<br>Tauri 多端网文工作台：世界观、总纲、章纲到正文，章节记忆按固定资料→历史摘要→最近对话组装上下文；可拆书、蒸馏文风绑定写作，并去 AI 味<br><sub>方法：规划 · 记忆 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-09-11 · 🧩 应用 · 中文</sub><br><sub>💡 客户端默认接作者的 ApiSaver 中转站，需在该站注册 Key；安装包发在飞书；内置书籍搜索下载和番茄/起点/飞卢扫榜</sub>

- **[LoreSmith](https://github.com/G-Pegasus/LoreSmith)** · ★ 15<br>长篇网文 Agent 运行时：LangGraph 编排章节规划、草稿、一致性检查、提交、评审与重写，章后沉淀摘要/时间线/关系/伏笔供后续检索<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-09-17 · 🧩 应用 · 中文</sub><br><sub>💡 React 前端 + Spring Boot 平台层 + Python 运行时；另附一份 skill/SKILL.md</sub>

- **[LunaRime/novelforge](https://github.com/LunaRime/novelforge)** · ★ 15<br>小说 IDE：AI 出大纲和细纲后逐章流式写，5 角色编辑部并行审阅加权评分，多稿择优，定稿后提取剧情、角色声音和伏笔并做三级摘要记忆<br><sub>方法：规划 · 人物 · 记忆 · 修订</sub><br><sub>更新于 2026-10-21 · 🧩 应用 · 多语言 · GPL-3.0</sub><br><sub>💡 Electron 桌面应用，本地 RAG（SQLite + LanceDB）；界面中/英/俄三语</sub>

- **[Mo-Shen](https://github.com/wwxxzz666/Mo-Shen)** · ★ 15<br>AgentScope 编排策划、世界观、角色、大纲、写作、审校、总编 7 个 agent 接力写小说，先 200 字试写定风格，大纲确认后逐章生成<br><sub>方法：规划 · 设定 · 多智能体 · 修订</sub><br><sub>更新于 2026-08-13 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 Web 工作台 + 微信小程序 + CLI/HTTP API；旧 LangGraph 版保留在 v1 标签</sub>

- **[novel-workspace-mcp](https://github.com/LiZh132707/novel-workspace-mcp)** · ★ 15<br>长篇小说工作区：世界观、人物、章纲、时间线、事实和伏笔存成可审计的项目状态，经本地网页、MCP 工具或 Codex Skill 调模型起草和审校<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-10-01 · ⚙️ 框架 · 多语言 · MIT</sub><br><sub>💡 默认接 LM Studio 本地模型，也可接 OpenAI 兼容 API；界面支持英/中/日三语</sub>

- **[jarvis-write](https://github.com/ynnyh/jarvis-write)** · ★ 14<br>包在 LLM 外的长篇控制层：时序故事圣经按章节区间记事实，伏笔四态调度，改大纲自动分析下游并级联重生成，名家范文正向锚定加量化 AI 味门禁<br><sub>方法：规划 · 记忆 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-10-26 · 🧩 应用 · 中文 · Apache-2.0</sub><br><sub>💡 定稿另做叙事结构指纹检查；附漫剧、宣传片等制片工坊（只出提示词）；桌面版和在线试用需进群领邀请码</sub>

- **[novel-app](https://github.com/gelijunge22-code/novel-app)** · ★ 14<br>自托管写作台：出方案→挑刺→取料查证→写正文→复审改稿各为独立模型调用，可多角色分工；世界引擎存主体状态检测设定冲突，568 条规则查 AI 味<br><sub>方法：记忆 · 多智能体 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-09-22 · 🧩 应用 · 中文 · AGPL-3.0</sub><br><sub>💡 FastAPI 后端 + 网页 + 安卓壳，仓库附带 apk；世界引擎、讨论/计划/执行三模式等思路与 notnotype/neuro-book 相近，但为独立 Python 实现</sub>

- **[huohuo-drama](https://github.com/appolloqin/huohuo-drama)** · ★ 13<br>数字作家批量写连载：brief→正文→一致性审校，章末强制写「触发→过程→结果」因果变更记录并注入后文，配四层记忆；小说可再改编成短剧出片<br><sub>方法：理论 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-10-20 · 🧩 应用 · 多语言 · 40 个 skill</sub><br><sub>💡 含 100+ 个题材写作 skill、AI 检测与去味改写；同时是带多渠道支付的短剧/小说 SaaS；仓库无许可证</sub>

- **[Lin-A1/novel-agent](https://github.com/Lin-A1/novel-agent)** · ★ 13<br>MetaGPT 多 agent 写小说：情节架构师出整体架构→评审打分→修订，章节规划拆章定目标，审阅者读前章给下章指导，写手逐章写<br><sub>方法：规划 · 多智能体 · 修订</sub><br><sub>更新于 2025-01-13 💤 · ⚙️ 框架 · 中文</sub><br><sub>💡 基于 MetaGPT；附生成样例 novel.txt；仓库无许可证</sub>

- **[MyAINovel](https://github.com/sEwhappend/MyAINovel)** · ★ 13<br>桌面长篇流水线：标签化生成初始方案，全书大纲确认后拆章→小节规划→场景导演→对白心理→正文→审稿→改写→定稿，资料库检索并回写<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-07-02 · 🧩 应用 · 中文 · AGPL-3.0</sub><br><sub>💡 PySide6 桌面程序，项目以 .json/.md 文件夹保存；AGPL-3.0</sub>

- **[novel-multi-agents](https://github.com/QSPBU-LONG/novel-multi-agents)** · ★ 13<br>OpenAI Agents SDK 五 agent：大纲专家→角色开发专家深化人物弧线→章节撰写→编辑评估并给修改建议，由协调者串联<br><sub>方法：规划 · 人物 · 多智能体 · 修订</sub><br><sub>更新于 2025-03-13 💤 · ⚙️ 框架 · 中文</sub><br><sub>💡 默认本地 Ollama qwen2.5:14b，也可接在线模型；仓库未声明许可证</sub>

- **[AI_NovelWriter](https://github.com/ATboy-web/AI_NovelWriter)** · ★ 12<br>情节、世界观、写手、审校、编辑五 Agent 流水线，审校意见回流修订到过质量阈值；每章检测决策点，可分出平行世界线与世代传承<br><sub>方法：人物 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-09-18 · 🧩 应用 · 中文</sub><br><sub>💡 Windows EXE / Android APK 在 Releases，仓库含完整 Python 源码；支持插件与 MCP</sub>

- **[Hi-Story](https://github.com/mofeifeifei/Hi-Story)** · ★ 12<br>本地长篇工作台：设定与题材约束→全书大纲和分卷→章节细纲→正文，生成后查衔接、因果、人设、重复并修订，定稿后抽章节记忆供后文用<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-08-23 · 🧩 应用 · 中文</sub><br><sub>💡 Python + React + SQLite，Windows 下用 bat 启动；支持 OpenAI 兼容和 Anthropic 协议，也有 CLI</sub>

- **[HXSLtim/Moshu](https://github.com/HXSLtim/Moshu)** · ★ 12<br>作者主导的长篇工具：Story Bible 事实与事件账本按目标章取当时有效设定，LangGraph 三阶段续写配 Chroma RAG，AI 产出都需作者审核<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-10-12 · 🧩 应用 · 中文</sub><br><sub>💡 与 huihuijiangqiang/moshu 同名但不是同一项目；六维章节审核后端已实现，独立入口待露出</sub>

- **[Novel-Claude](https://github.com/wzxsph/Novel-Claude)** · ★ 12<br>CLI 依次生成金手指→梗概→大纲→世界设定→蓝图，再分卷细纲、按章写作，ChromaDB RAG 检索记忆，审核与实体跟踪，skill 插件注入上下文<br><sub>方法：规划 · 设定 · 记忆</sub><br><sub>更新于 2026-08-09 · ⚙️ 框架 · 中文 · GPL-3.0</sub><br><sub>💡 作者自称新手练手的实验项目；RAG 嵌入需智谱密钥，支持智谱 Batch API</sub>

- **[NovelForger](https://github.com/cedrusdang/NovelForger)** · ★ 12<br>LangGraph+Gemini notebook：按英雄之旅、三幕、七点结构定情节，人物贴合节拍生成，章节取结构化元数据和嵌入记忆，另一 agent 打分返工<br><sub>方法：规划 · 理论 · 人物 · 修订</sub><br><sub>更新于 2025-04-21 💤 · ⚙️ 框架 · 英文 · MIT</sub><br><sub>💡 Kaggle 上可运行的课程项目 notebook，需 Gemini API；人工把关可选；附越南语样例</sub>

- **[youyouxia263/autoNovel](https://github.com/youyouxia263/autoNovel)** · ★ 12<br>悬疑/言情长篇生成器：生成前提、世界观（地点、时间线）和人物卡，再出逐章大纲写章节、章后摘要，并做一致性、节奏和情节逻辑检查与修复<br><sub>方法：规划 · 设定 · 人物 · 修订</sub><br><sub>更新于 2026-01-12 💤 · 🧩 应用 · 多语言</sub><br><sub>💡 界面中文、默认提示词英文；支持 Gemini、通义千问和 OpenAI 兼容接口</sub>

- **[AI-Practical-Lab/ai-novel](https://github.com/AI-Practical-Lab/ai-novel)** · ★ 11<br>网页长篇写作台：书架→分卷→章节三级结构，先定剧情路标并自动生成过渡细纲，再按细纲流式写正文，自动带入设定集、大纲和上一章<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2026-04-07 💤 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 README 写后端是 Express，仓库实际以 Java 后端为主，文档与代码不一致；兼容 OpenAI/DeepSeek 接口；有在线体验站</sub>

- **[AI-StorySmith](https://github.com/takimdigital/AI-StorySmith)** · ★ 11<br>本地模型写书脚本：先按主角/目标/危机/独特点生成前提，再出标题、目录、每章内容类型并细化，最后逐章级联写作，中间结果落盘可续跑<br><sub>方法：规划</sub><br><sub>更新于 2025-10-23 💤 · ⚙️ 框架 · 英文 · Apache-2.0</sub><br><sub>💡 面向 LM Studio / Ollama 本地模型</sub>

- **[Moyun](https://github.com/Not1a-del/Moyun)** · ★ 11<br>纯前端长篇写作台：大纲→细纲→正文，细纲按 ID 钉选本章活跃角色和世界资料作为生成上下文，角色资料分三档，AI 草案逐项审阅<br><sub>方法：规划 · 人物 · 记忆</sub><br><sub>更新于 2026-10-24 · 🧩 应用 · 中文</sub><br><sub>💡 CC BY-NC 4.0，禁止商用；可直接在 GitHub Pages 使用，数据存浏览器；兼容白鸟扩展和 MOD</sub>

- **[One-flower](https://github.com/sleepykino/One-flower)** · ★ 11<br>AI 小说工作台：摘要链+世界书 RAG+角色卡拼上下文续写，长文按节拍规划→逐拍生成→接缝自检，总纲、文风 Skill 包与 hook.md 校验三层约束<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-09-07 · 🧩 应用 · 中文 · 19 个 skill · Apache-2.0</sub><br><sub>💡 附 19 个文风 SKILL.md（金庸、老舍、海明威冰山等）；另含小说→剧本→分镜转化</sub>

- **[silly-zero/ai-novel](https://github.com/silly-zero/ai-novel)** · ★ 11<br>Go+Eino 多 agent 写长篇：架构师定大纲，人设/设定 agent 维护角色卡与世界观，主编拆场景卡，资料员规划 RAG 检索，审查员不合格打回重写<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-09-01 · ⚙️ 框架 · 中文</sub><br><sub>💡 只有后端服务（REST/SSE），默认智谱 GLM 与 embedding-3，需 PostgreSQL；根目录有无扩展名的 main、server 文件（疑似编译产物）</sub>

- **[story](https://github.com/ATAIN000/story)** · ★ 11<br>长篇写作台：315 题材与 20 层世界观向导→宏观规划；每章先出决策卡再生成，抽取事件后经七步硬约束验证（含 Z3）自动修正，事件溯源可回滚<br><sub>方法：规划 · 记忆 · 模拟 · 修订</sub><br><sub>更新于 2026-10-07 · 🧩 应用 · 中文</sub><br><sub>💡 单用户部署；首次启动为 Mock 演示模式</sub>

- **[Story-OS](https://github.com/tanao521/Story-OS)** · ★ 11<br>章节级滚动写长篇：先出故事蓝图和人物/世界/写作约束，逐章规划→草稿→修订，过人工审核闸门才进正史；摘要、Chroma 向量库和 Obsidian 做长期记忆<br><sub>方法：规划 · 记忆 · 修订 · 共创</sub><br><sub>更新于 2026-08-03 · 🧩 应用 · 中文 · Apache-2.0</sub><br><sub>💡 本地 FastAPI Web UI + CLI；支持 DeepSeek 与本地模型分工；另有实验性「模拟器模式」边玩边写</sub>

- **[BlockWriter](https://github.com/FartyPants/BlockWriter)** · ★ 10<br>text-generation-webui 扩展：按场景分块写作，每块写明该场景要发生什么再生成，可随时改任一块的指令或正文并重生成，全文随之动态拼接<br><sub>方法：规划 · 共创</sub><br><sub>更新于 2024-01-13 💤 · 🧩 应用 · 英文</sub><br><sub>💡 需放到 text-generation-webui 的 extensions/BlockWriter；实验性 WIP；无许可证</sub>

- **[kapaiverki](https://github.com/Idun/kapaiverki)** · ★ 10<br>用卡牌组合主题、类型、角色、情节和世界观灵感卡，按可改的雪花写作法模板生成小说大纲；另有四阶段角色塑造工坊和情节/角色专家对话<br><sub>方法：规划 · 理论 · 人物</sub><br><sub>更新于 2025-10-11 💤 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 只出大纲，不写正文</sub>

- **[leehong0704/ai-novel](https://github.com/leehong0704/ai-novel)** · ★ 10<br>设定→章纲→正文，正文中插【标记】让 AI 只重写标记处；定稿时自动抽取人物变化同步角色卡，并增量更新全书梗概和近三章回顾<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-04-13 💤 · 🧩 应用 · 中文 · EPL-1.0</sub><br><sub>💡 Python 桌面应用，支持 DeepSeek/OpenAI/Gemini；仓库另附 Windows 打包 zip（release/ai-novel.zip），源码完整</sub>

- **[novel-copilot](https://github.com/doctoroyy/novel-copilot)** · ★ 10<br>Story Bible→大纲→逐章/批量生成，滚动摘要+角色状态快照+伏笔依赖图+节奏控制注入上下文，多维 QC（一致性/节奏/目标）不过即进修复循环<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-07-26 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 部署在 Cloudflare Workers，含 Web 与 React Native App；另带动画/视频/TTS 模块；README 英文，章节提示词为中文</sub>

- **[Novel-factory](https://github.com/YoRengzh/Novel-factory)** · ★ 10<br>多智能体+确定性编排：卷→弧→段→章四层规划，角色/物品/势力三账本须附正文引证校验，伏笔排期状态机，异族模型候选盲评，禁泄扫描与 26 项批末体检<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-10-25 · ⚙️ 框架 · 中文 · Apache-2.0</sub><br><sub>💡 Java 17 / Spring AI；Qdrant 向量增强可选；ChatGPT 套餐授权通道为实验性功能</sub>

- **[novel-writing-agent](https://github.com/lianyichuan/novel-writing-agent)** · ★ 10<br>长篇写作管理系统：维护作者意愿、主线剧情脉络、人物关系和 Agent 执行手册等设定文档，剧情追踪面板看多条主线，调模型生成章纲和正文<br><sub>方法：规划 · 人物 · 记忆</sub><br><sub>更新于 2025-07-25 💤 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 默认接 Gemini API</sub>

- **[NovelizeAI](https://github.com/paradroidlabs/NovelizeAI)** · ★ 10<br>Gemini 长篇写作应用：按类型、视角、语调等修饰项分三阶段出概念、人物设定和情节大纲，再逐章生成，根据评审反馈迭代<br><sub>方法：规划 · 修订 · 共创</sub><br><sub>更新于 2026-05-01 · 🧩 应用 · 英文</sub><br><sub>💡 源自作者早期的 Wordware 版 para-droid-ai/novella-xl-15；需 Gemini API</sub>

- **[agent](https://github.com/sfxyn/agent)** · ★ 9<br>AI 先分析提示定类型、视角、结构等参数，再依次生成概念、角色、总纲和章纲，每章多轮生成凑足字数，可指定作家文风模仿，状态存档可续写<br><sub>方法：规划 · 人物 · 风格</sub><br><sub>更新于 2025-03-17 💤 · ⚙️ 框架 · 中文</sub><br><sub>💡 测试版；默认豆包/火山方舟接口；仓库未声明许可证；README 里的克隆地址是占位仓库名</sub>

- **[aiAIfiction](https://github.com/liaoma1993/aiAIfiction)** · ★ 9<br>从策划对话到世界观、角色势力、卷/弧/章节蓝图逐级生成正文；上传样本抽取写法 Skill 跨项目复用，按审计结果定位到句/段/整章局部修复<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-06-24 · 🧩 应用 · 中文</sub><br><sub>💡 FastAPI + React；默认管理员账号密码写在 README，部署需改；无 License</sub>

- **[novel-smith](https://github.com/huanweide/novel-smith)** · ★ 9<br>本地长篇工坊：探讨模式 11 步对话建世界观，章后自动抽取建角色卡/世界书，近章全文+摘要+远期压缩分层记忆，15 维拆书仿写，本地规则引擎检测 AI 味<br><sub>方法：设定 · 记忆 · 风格 · 去 AI 味</sub><br><sub>更新于 2026-10-25 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 Next.js + 本地 SQLite；去 AI 味检测可离线、无需 API Key</sub>

- **[AI_novelsTool_obsdian](https://github.com/Aurirlk/AI_novelsTool_obsdian)** · ★ 8<br>PyQt 桌面写作台：大纲师、码字工、督察、评论家等 12 个智能体分工，7 模块记忆追踪角色状态、钩子与大事记，配拆书分析和批评师审稿<br><sub>方法：记忆 · 多智能体 · 修订 · 风格</sub><br><sub>更新于 2026-10-19 · 🧩 应用 · 中文 · 58 个 skill</sub><br><sub>💡 内置约 49 个网文 skills（103 个 SKILL.md），据作者说明部分整合自 GitHub 其他项目；无 License；需自带 API</sub>

- **[LLMWriter](https://github.com/zhangwen-max/LLMWriter)** · ★ 8<br>RAG 长篇写作：世界观圣经、角色卡、阶段摘要、近三章记忆、上章结尾五层上下文，按写作计划多路检索 Qdrant，每章写完抽取事件/事实/关系/伏笔入库<br><sub>方法：规划 · 记忆</sub><br><sub>更新于 2026-01-22 💤 · ⚙️ 框架 · 中文</sub><br><sub>💡 默认 Qwen-Plus；未声明许可证</sub>

- **[N.I.C.E.](https://github.com/KurohaneKaoruko/N.I.C.E.)** · ★ 8<br>Tauri 长篇写作 IDE：AI 续写/改写/规划，Planner 拆任务执行，改稿默认先出审阅建议逐条采纳，自动维护角色状态与伏笔索引并可手工锁定<br><sub>方法：规划 · 记忆 · 修订</sub><br><sub>更新于 2026-10-22 · 🧩 应用 · 中文 · GPL-3.0</sub>

- **[Novelex](https://github.com/CayleyZ/Novelex)** · ★ 8<br>人审把关的长篇网文工作台：Plan 两轮出大纲，Write 先出多份细纲候选再写正文、审计、锁章，批准后回写事实账本、伏笔和角色状态<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-04-30 · 🧩 应用 · 中文</sub><br><sub>💡 PolyForm Noncommercial 许可；可绑定风格指纹、范文 RAG 和黄金开头库（建索引需智谱 embedding）</sub>

- **[AI-Web-Novel-Assistant](https://github.com/XZQINSYSU/AI-Web-Novel-Assistant)** · ★ 7<br>PyQt6 网文桌面工具：全局梗概、人物卡、卷梗概、章细纲分层设定，按细纲加前文逐章写，挂机模式自动补全卷章写完全书，一键修复查人名错误和吃书<br><sub>方法：规划 · 人物 · 修订</sub><br><sub>更新于 2026-02-23 💤 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 默认 DeepSeek-Reasoner，兼容 OpenAI 接口；example/ 附两部生成的示例小说（docx）</sub>

- **[AuctorForge](https://github.com/Te9ui1a/AuctorForge)** · ★ 7<br>本地文件型网文工作台，内置长篇技能包：可从零、带稿或拆样板书起步，设定→总纲/卷纲/章纲→逐章写作并更新角色快照与伏笔表→主编式质检<br><sub>方法：规划 · 记忆 · 修订 · 风格</sub><br><sub>更新于 2026-05-05 · 🧩 应用 · 中文 · MIT</sub><br><sub>💡 强调 AI 做可控助手、作者保留判断；流程由仓库内 skill-packs/novel-flow-kit 0.1.5 驱动</sub>

- **[AutoWrite](https://github.com/Linmoqian/AutoWrite)** · ★ 7<br>Rust/Tauri 桌面写作应用：先生成世界观、角色和章节大纲，再用三层提示词逐章写正文，可按内容配图并多格式导出<br><sub>方法：规划 · 设定 · 人物</sub><br><sub>更新于 2026-08-13 · 🧩 应用 · 中文 · 2 个 skill</sub><br><sub>💡 README 很简略；需 DeepSeek API，配图用魔搭 Z-Image</sub>

- **[museflow](https://github.com/nhsprite/museflow)** · ★ 7<br>命令行工具：一句话梗概起步，LangGraph 编排世界观、角色、故事弧、章纲、起草、伏笔、一致性、修复等 10 类 agent 逐章写长篇，题材包可自定义<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-07-31 · ⚙️ 框架 · 多语言 · MIT</sub><br><sub>💡 npm 全局安装；每章写完自动检查字数、连续性和伏笔，修不好时出报告请求整章重写</sub>

- **[novel-writer-master](https://github.com/qiuxinyuan321/novel-writer-master)** · ★ 7<br>小说伴写工具：Story Bible 管角色口癖、世界观硬规则和伏笔，章→场景分层大纲设必达检查点，生成时注入前文摘要，并做一致性检测和降 AI 率改写<br><sub>方法：规划 · 记忆 · 修订 · 去 AI 味</sub><br><sub>更新于 2026-04-10 💤 · 🧩 应用 · 中文</sub><br><sub>💡 降 AI 率对标朱雀检测（332 词黑名单、统计分析、定向改写）；可按任务路由不同模型</sub>

- **[novel_generator](https://github.com/2572873335/novel_generator)** · ★ 7<br>按 Anthropic 长时 agent 方案写小说：初始化 agent 建大纲和人物，管线经草稿、一致性检查、润色，Python 记情绪债账本，熔断防无限重写<br><sub>方法：规划 · 记忆 · 多智能体 · 修订</sub><br><sub>更新于 2026-03-20 💤 · ⚙️ 框架 · 多语言 · 30 个 skill · MIT</sub><br><sub>💡 最后更新 2026-0