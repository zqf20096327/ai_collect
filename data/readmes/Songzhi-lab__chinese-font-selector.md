# chinese-font-selector · 中文字体选配 Skill

**中文字体 | 免费商用字体 | 字体搭配 | Chinese Fonts | Chinese Typography | AI Agent Skill**

> 一个给 AI Agent 用的中文字体专业知识包：让 AI 在做中文设计时，**选出合规、好看、能落地的字体**，而不是甩给你一堆 Inter。

**English**: An Agent Skill that teaches AI assistants to choose *commercially-safe, aesthetically-appropriate Chinese fonts* for Chinese-first design scenarios (social cards, brochures, web UI, book typesetting, posters), with license-safety tiers, scene×mood selection matrix, and CJK-Latin pairing rules.

---

## 为什么需要它 / Why

市面上所有字体类 Agent Skill（font-pairing、typography 等）全部是**西文字体体系**，中文字体覆盖为零。而中文设计有几个 AI 最常踩的坑：

- 把**微软雅黑/苹方**当"免费字体"交付印刷或网页嵌入 → 侵权风险
- 中英混排不声明英文字体 → 英文被中文字体内置拉丁字形渲染，廉价感拉满
- 给中文加 `italic` → 浏览器合成假斜体
- 全量加载中文字体文件（3-10MB）→ 网页首屏卡死

这个 skill 把「哪些中文字体能免费商用、什么场景用什么字、中英怎么搭、排版怎么排」固化成 AI 可直接执行的知识库。

**Keywords**: 中文字体, 中文字体推荐, 字体选择, 字体搭配, 字体配对, 免费商用字体, 可商用中文字体, 开源字体, 思源黑体, 思源宋体, 霞鹜文楷, 得意黑, 中文排版, 中英混排, 小红书字体, Chinese fonts, Chinese typography, CJK font pairing, free commercial Chinese fonts, claude skill, agent skill, SKILL.md

## 内容结构 / Contents

```
chinese-font-selector/
├── SKILL.md                      # 决策框架：授权先行 → 场景×气质 → 混排 → 交付
└── references/
    ├── fonts-database.md         # 可商用中文字体库（授权安全三级分类 + 五大场景选字矩阵）
    └── pairing-rules.md          # 中英混排配对、字号阶梯、行距行长、标点避头尾、翻车点清单
```

### 授权安全分级（核心机制）

| 等级 | 含义 | 示例 |
|---|---|---|
| **T0** | 开源字体（SIL OFL 等），商用铁稳、可嵌入可修改 | 思源黑体/宋体、霞鹜文楷、得意黑、未来荧黑 |
| **T1** | 厂商承诺免费商用，建议留存授权声明存档 | 阿里巴巴普惠体、MiSans、站酷系列 |
| **T2** | 慎用/避免：GPL 争议、平台限定授权、系统字体提取 | 文泉驿、汉仪部分、微软雅黑（交付物） |

## 安装 / Install

这是一个符合 [Agent Skills 规范](https://agentskills.io) 的技能包，适用于支持该规范的 AI 工具：

**Kimi**：直接导入本仓库的 `.skill` 打包文件，或在技能目录放入 `chinese-font-selector/` 文件夹。

**Claude Code / Cursor / Codex 等**：

```bash
# 方式一：skills CLI
npx skills add <your-github-username>/chinese-font-selector

# 方式二：手动复制到技能目录
cp -r chinese-font-selector ~/.claude/skills/
```

## 使用示例 / Usage

对 AI 说出以下任意一句，skill 会自动触发：

- 「给产品册选一套中文字体」
- 「小红书知识卡片用什么字体好」
- 「网页中文排版，要免费可商用的字体」
- 「单词书内页排版字体方案」

AI 会按固定模板输出：标题字/正文字/辅助字三层方案 + 英文数字搭配 + 字重 + 下载来源 + 授权备注。

## 数据来源与免责声明 / Sources & Disclaimer

- 字体授权信息整理自各字体官方声明及开源社区（dengcao/free-fonts、SIL OFL 官方文本等）
- **字体授权状态可能随时间变化**（厂商保留收回免费授权的权利，有先例）。商用交付前请到字体官网再次确认当前授权状态，并留存声明页面截图
- 本项目内容为整理与参考，不构成法律意见

## License

本 skill 文档本身以 [MIT License](LICENSE) 开源。
（注意：文档中**收录的各字体**遵循其各自的授权协议，MIT 只适用于本知识库的文本。）

## 贡献 / Contributing

欢迎补充：你发现新的优质可商用中文字体，或某字体授权状态发生变化，直接提 Issue 或 PR。

## 🦥 懒鬼系列 Sloth Series

懒得找，懒得挑，懒得踩坑。

| Skill | 仓库 | 解决什么 |
|---|---|---|
| 懒鬼中文字库 | [chinese-font-selector](https://github.com/Songzhi-lab/chinese-font-selector) | 中文免费商用字体筛选 + 中英混排 + 排版规则 |
| 懒鬼素材库 | [sloth-assets](https://github.com/Songzhi-lab/sloth-assets) | 免费可商用图片/插画/图标素材筛选 + 授权分级 + 缩略图筛选图 |
