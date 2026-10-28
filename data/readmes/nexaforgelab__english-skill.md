# English Skill

> 100 open-source AI-agent skills for English learning, with executable training scaffolds, structured skill profiles, validation scripts, and bilingual learning guides.

> 100 个开源英语学习 AI Agent Skill，包含可执行训练脚手架、结构化技能画像、自检脚本和中英文学习指南。

## 中文简介

English Skill 是一个面向 AI Agent / Codex / Prompt 工程的英语学习技能库。它不是单一聊天提示词，而是一套可组合的学习系统：100 个 skill 覆盖词汇、语法、发音、听力、口语、阅读、写作、考试、商务、留学、亲子、影视歌曲和成长管理等场景。

每个 skill 都包含：

- `SKILL.md`：角色、流程、输出格式、注意事项和集成说明
- `scripts/run_skill.py`：生成一次结构化训练会话
- `scripts/validate_skill.py`：检查当前 skill 资源是否完整
- `references/skill_profile.json`：分类、能力范围、流程阶段、评分维度、复习项类型
- `agents/openai.yaml`：用于 UI 展示的名称、短描述和默认启动 prompt

根目录还提供共享运行时 `english_skill_runtime.py`，支持 Markdown/JSON 输出、学习事件记录、复习项生成和批量审计。

## English Overview

English Skill is an open-source collection of AI-agent skills for English learning. It is designed for agents, prompt engineers, educators, and language-learning product builders who need reusable workflows instead of one-off prompts.

The repository includes 100 skills across vocabulary, grammar, pronunciation, listening, speaking, reading, writing, exam preparation, business English, study abroad, parent-child English, movies, songs, news, and long-term learning management.

Each skill includes:

- `SKILL.md`: role, workflow, output format, guardrails, and integration notes
- `scripts/run_skill.py`: generate a structured learning session
- `scripts/validate_skill.py`: validate the skill resource package
- `references/skill_profile.json`: category, capabilities, workflow phases, assessment dimensions, review item types
- `agents/openai.yaml`: display metadata and a default starter prompt

## Quick Start / 快速开始

Requirements: Python 3.10+.

```bash
git clone https://github.com/nexaforgelab/english-skill.git
cd english-skill

# Validate every skill package
python3 scripts/audit_skill_resources.py --format text

# Run one skill
python3 speaking-partner/scripts/run_skill.py \
  --request "请和我练习一次英语面试，重点是自我介绍。" \
  --level B1 \
  --minutes 10

# Output JSON for app integration
python3 speaking-partner/scripts/run_skill.py \
  --request "Practice a job interview self-introduction with me." \
  --level B1 \
  --minutes 10 \
  --format json
```

Persist a learning event and review items through the local SQLite-backed core:

```bash
python3 speaking-partner/scripts/run_skill.py \
  --request "请和我练习一次英语面试。" \
  --user-id demo-user \
  --record \
  --format json
```

## Documentation / 文档

- [中文使用指南](docs/USAGE.zh-CN.md)
- [English Usage Guide](docs/USAGE.en-US.md)
- [中文场景学习指南](docs/SCENARIOS.zh-CN.md)
- [Scenario Learning Guide](docs/SCENARIOS.en-US.md)
- [中文 Skill 目录](docs/SKILL_CATALOG.zh-CN.md)
- [English Skill Catalog](docs/SKILL_CATALOG.en-US.md)

## Skill Categories / Skill 分类

| Category | 中文分类 | Count |
|---|---|---:|
| Vocabulary & Grammar | 词汇/语法 | 14 |
| Pronunciation & Prosody | 发音/语音 | 10 |
| Listening | 听力 | 13 |
| Speaking & Dialogue | 口语/对话 | 22 |
| Reading | 阅读 | 9 |
| Writing & Rewriting | 写作/改写 | 11 |
| Exam Preparation | 考试备考 | 11 |
| Business, Life & Culture | 商务/生活/文化 | 10 |

## Repository Layout / 仓库结构

```text
english-skill/
├── english_agent_core.py          # SQLite profile, event, review, SM2 helpers
├── english_skill_runtime.py       # shared executable runtime for all skills
├── scripts/
│   ├── audit_skill_resources.py
│   ├── enhance_skill_resources.py
│   └── test_enhanced_skills.py
├── docs/
│   ├── USAGE.zh-CN.md
│   ├── USAGE.en-US.md
│   ├── SCENARIOS.zh-CN.md
│   ├── SCENARIOS.en-US.md
│   ├── SKILL_CATALOG.zh-CN.md
│   └── SKILL_CATALOG.en-US.md
└── <skill-name>/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/skill_profile.json
    └── scripts/
        ├── run_skill.py
        └── validate_skill.py
```

## Example Prompts / 示例 Prompt

中文：

```text
我是职场人，B1 水平，每天只有 15 分钟。请用 speaking-partner 和 business-english 帮我设计一周英语学习计划，重点是会议发言、项目汇报和英文邮件跟进。
```

English:

```text
I am a B1 office worker with 15 minutes per day. Use speaking-partner and business-english to create a one-week English plan focused on meetings, project updates, and follow-up emails.
```

More scenario-specific prompts are available in the [Chinese scenario guide](docs/SCENARIOS.zh-CN.md) and [English scenario guide](docs/SCENARIOS.en-US.md).

## Validation / 验证

```bash
python3 scripts/audit_skill_resources.py --format text
python3 scripts/test_enhanced_skills.py
python3 skill_e2e_tester.py --skills-root . --output test_report_after_enhancement.json
```

Expected result:

```text
Skill resource audit: 100/100 passed
```

## License / 开源协议

Apache License 2.0. See [LICENSE](LICENSE).
