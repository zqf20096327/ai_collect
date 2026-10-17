# vibe-coding-prd

Claude Code 自定义 skill：把需求描述 / 原始PRD（含飞书文档）/ 竞品分析整理成一份精简、结构化、可直接喂给编码 Agent（Claude Code / Codex）实现的 Markdown PRD。

## 安装

将本仓库内容放到 `~/.claude/skills/vibe-coding-prd/` 下：

```bash
git clone https://github.com/<your-account>/vibe-coding-prd.git ~/.claude/skills/vibe-coding-prd
```

## 使用

在 Claude Code 中输入「帮我写一个用来vibe coding的PRD」即可触发，详见 [SKILL.md](SKILL.md)。

## 文件结构

| 文件 | 作用 |
|---|---|
| `SKILL.md` | 主流程：输入识别 → 需求定义 → 功能清单+优先级 → 技术栈 → 原型线框 → 明细模块 → 验收标准 → 自检交付 |
| `references/prd-template.md` | 最终 PRD 骨架模板（含「假设与已确认决策」块和交付前 QUICK CHECKLIST） |
| `references/conventions.md` | 精度家规：字面量规则、反模式对照表、内容剔除清单、否定约束 |
| `references/examples/` | 成品 PRD 语料，展示目标信息密度 |
