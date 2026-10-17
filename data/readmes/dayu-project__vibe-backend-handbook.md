# vibe-backend-handbook

一个面向 AI 产品经理与 Codex 的 Agent 后端开发 Skill：把产品 PRD、现有代码和运行约束转成可审查的技术适配声明、分阶段技术方案、当前阶段实现与双层验收。

它源自《AI Agent 产品 Vibe Coding 通用技术栈手册 V2.1》，重点保留：

- PRD 优先，手册只提供工程底线、默认方案与适配规则；
- 先输出《技术适配声明》，再进入当前阶段；
- 在“后端先行”和“纵向切片”之间按产品形态判断；
- 密钥、数据恢复、错误边界和人工确认点等强制底线；
- mock 自动化测试 + 真实模型端到端冒烟；
- 给非技术产品经理逐步、可操作的验收说明。

## 安装

在 Codex 中发送下面这句话：

```text
使用 $skill-installer 从 https://github.com/daaaayuuuu/vibe-backend-handbook 安装这个 Skill。
```

也可以克隆后复制到个人 Skills 目录：

```bash
git clone https://github.com/daaaayuuuu/vibe-backend-handbook.git
cp -R vibe-backend-handbook ~/.codex/skills/vibe-backend-handbook
```

重新打开 Codex 后即可使用。

## 使用示例

```text
使用 $vibe-backend-handbook 阅读这份 AI Agent 产品 PRD 和当前仓库。
先检查现状并输出《技术适配声明》，再生成第一阶段技术开发文档。
暂时不要改代码。
```

```text
使用 $vibe-backend-handbook 按已经确认的《技术适配声明》实现当前阶段。
完成 mock 自动化测试；如果真实 Key 未配置，把真实模型冒烟明确标记为待验。
```

## 目录

```text
.
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── adaptation-declaration.md
    ├── engineering-baseline.md
    ├── stage-document-template.md
    └── testing-and-delivery.md
```

## 适用范围

适合从零开发或继续迭代以 LLM 为核心能力的 Agent MVP，包括智能写作、知识库问答、数据分析、流程自动化和多媒体创作等。

它不是普通非 Agent 后端的通用教程，也不替代具体 PRD、正式前端规范或生产部署方案。医疗、金融、政务、高并发、多租户、跨地域容灾、实时音视频和强硬件依赖场景仍应保留工程底线，但需要额外的专项架构与合规设计。

## 设计原则

Skill 的入口保持简短，并按任务加载 `references/` 中的详细规则。它不会把默认技术方案伪装成不可违反的原则，也不会因为用户只要求分析或规划就擅自修改代码、部署或发布。
