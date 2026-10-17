# cn-patent-drafter

> **30 秒装好。一句话起草。一份能直接交代理人的中国发明专利。**
>
> 全网首个 CNIPA 2026 规范同步、产品级、可复现的 Claude Code 专利起草 Skill。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Made with Claude Code](https://img.shields.io/badge/made_with-Claude_Code-8A2BE2)](https://claude.com/claude-code)
[![CNIPA 2026 Compliant](https://img.shields.io/badge/CNIPA-2026_compliant-success)](./checklists/cnipa-2026.md)
[![LaTeX: ctexart + xelatex](https://img.shields.io/badge/LaTeX-ctexart_%2B_xelatex-9cf)](./SKILL.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#贡献)

---

## 这是什么

`cn-patent-drafter` 是一个**专为中国发明专利写的 Claude Code Skill**——不是 wrapper、不是抽奖式 Prompt 模板、不是搬运 USPTO 工作流。

它把 CNIPA 2025-2026 现行的申请文件规范、专利法第 25 条排除项、2024-12 AI 承诺新规、说明书段号约定、权利要求引用约束……全部固化为一套 **「读清单 → 援引代码事实 → 套模板 → 写前自检 → 出 PDF」** 的结构化工作流。

它已经在一个**真实可编译、14 页、3.67 MB 的发明专利样本**（`examples/sample-output.pdf`）上跑通端到端。

## 为什么有它

| 现状的痛 | 本 Skill 的解 |
|---|---|
| GitHub 上能搜到的中文专利 LaTeX 模板**仅 1 个**（CanYellow），且 **2025-10 已存档**，理由是 LaTeX 无法无损转 XML | 重构为 ctexart + xelatex 工具链，生成 PDF 用于评审，最终 XML 由代理人转换 |
| Claude / GPT 上找得到的"专利起草" Prompt 都是 USPTO/EPO 流派，**完全不懂 CNIPA** 的请求书 / 摘要 / 权利要求 / 说明书 / 附图五文档制 | 五文档 + 段号 `[0001]` 全局连续 + 第 25 条排除项自检 + AI 承诺自检 一次性内置 |
| 写专利常见踩坑：从权循环引用、商标 / 竞品名漏过滤、AI 列发明人、摘要超 300 字、附图编号错位…… | 10 大类、~50 条 checklist 在写前强制自检，命中即在响应中显式列出 |
| 用模板 prompt 起草，写一次得改十遍才像专利 | 4 套 `__PLACEHOLDER__` 占位骨架直接挖好坑，技术内容只需对照源码填空 |
| 不知道 2024-12 CNIPA AI 新规具体要求什么 | 已编入清单：发明人不得列 AI；起草中如用 AI 辅助应限排版/润色；专利文本本身不披露提示词 |

## 30 秒安装

把本仓库 clone 进任何 Claude Code 项目的 `.claude/skills/` 目录：

```bash
cd your-patent-project/
git clone https://github.com/handsomeZR-netizen/cn-patent-drafter.git .claude/skills/cn-patent-drafter
```

或者全局安装（一次安装，所有项目可用）：

```bash
git clone https://github.com/handsomeZR-netizen/cn-patent-drafter.git ~/.claude/skills/cn-patent-drafter
```

下次打开 Claude Code，向它说一句："**帮我起草一份发明专利的权利要求书**"——Skill 会自动触发，按工作流执行。

## 一句话起草示例

```text
你: 请帮我把权利要求书第 3 条改成"采用中位数代替均值"
```

Claude Code（被 Skill 接管后）会：

1. 读 `checklists/cnipa-2026.md` 加载 10 大类合规规则
2. 读 `docs/patent-tex/sections/03-claims.tex` 定位第 3 条
3. Grep 用户项目源码确认"中位数"实现细节
4. 用 `templates/claim-skeleton.tex` 的从权骨架重写
5. 自检：从权引用 N 是否小于当前条号？是否触犯循环引用禁令？参数是否给出取值区间？
6. 写入并提示 `xelatex` 重编

## 你能用它做什么

- 从零起草一份完整 CN 发明专利申请文件（请求书 + 摘要 + 权利要求书 + 说明书 + 附图）
- 对已有专利草稿做 CNIPA 2026 合规体检，列出每条不通过项
- 增删改从权而不破坏单一性 / 不引入循环引用
- 扩写说明书段落而保持 `[0001]` 全文段号连续
- 把项目源码的关键算法、参数、数据结构援引进"具体实施方式"，让说明书"充分公开"
- 输出可直接交付专利代理人转 XML 的 PDF

## 不在范围

- 软件著作权登记（请走另一条流程）
- 实用新型 / 外观设计专利（前者不保护纯软件方法，后者关注界面外观）
- USPTO / EPO / JPO 等其他司法辖区
- 形式审查后的官方意见答辩（OA 答辩需独立流程）
- XML 格式申报文件转换（CNIPA 2026-01-01 强制 XML 格式，建议由代理人转换）

## 仓库结构

```
cn-patent-drafter/
├── README.md                          # 你正在看的这份
├── LICENSE                            # MIT
├── SKILL.md                           # Claude Code Skill 入口（核心）
├── templates/
│   ├── claim-skeleton.tex             # 独立权 + 从权 + 系统权骨架
│   ├── spec-section-headers.tex       # 说明书六小节 + 段号阶梯
│   ├── abstract-skeleton.tex          # 摘要 ≤ 300 字范本
│   └── request-form.tex               # 请求书表格
├── checklists/
│   └── cnipa-2026.md                  # 10 大类合规清单（核心）
└── examples/
    └── sample-output.pdf              # 14 页真实编译样本
```

## CNIPA 2026 合规清单亮点

`checklists/cnipa-2026.md` 涵盖 10 大类共约 50 条核验项，含：

| # | 类别 | 关键项 |
|---|---|---|
| 一 | 文件结构与顺序 | 五文档齐备、`\input` 顺序固定 |
| 二 | 说明书段号 | `[0001]` 四位补零 + 全局连续不重置 |
| 三 | 权利要求书 | 单向引用、禁止循环引用、必给取值区间 |
| 四 | 说明书摘要 | ≤ 300 汉字 + 摘要附图 ≤ 1 张 |
| 五 | 说明书内容充分公开 | 六小节顺序 + 援引源码 + 关键参数取值依据 |
| 六 | 附图 | 黑白线图、序号一致、与附图说明一一对应 |
| 七 | **专利法第 25 条排除项** | 非科学发现 / 非智力规则 / 非诊疗方法 / 非动植物品种 |
| 八 | **AI 与诚信承诺（2024-12 CNIPA 指引）** | 发明人为自然人 + AI 仅辅助排版润色 |
| 九 | 避免内容 | 无商标 / 无竞品名 / 无源码 URL / 无模糊词 |
| 十 | 构建验证 | 无 error/warning + 中文字体渲染 + 五文档分页 |

## 看一眼产出长啥样

`examples/sample-output.pdf` 是用本 Skill 起草、`bun run docs:patent` 编译出的 14 页真实样本（占位字段未填充，便于二次裁剪）。打开它你会看到：

- 第 1 页：发明专利请求书（含分类号建议 + 4 条诚信承诺）
- 第 2 页：说明书摘要 + 摘要附图
- 第 3-4 页：权利要求书（独立权 1 + 独立权 2 + 8 条从权 + 系统权 + 衍生权）
- 第 5-10 页：说明书六小节，段号 `[0001]–[0036]` 全局连续
- 第 11-14 页：说明书附图 4 张

## 工作流图

```
用户请求
    │
    ▼
┌────────────────────────────────┐
│ 1. 读 checklists/cnipa-2026.md │  ← 加载 10 大类合规规则
└────────────────────────────────┘
    │
    ▼
┌────────────────────────────────┐
│ 2. 定位 sections/0X-XX.tex     │  ← 五文档之一
└────────────────────────────────┘
    │
    ▼
┌────────────────────────────────┐
│ 3. Grep 项目源码援引代码事实   │  ← 充分公开
└────────────────────────────────┘
    │
    ▼
┌────────────────────────────────┐
│ 4. 套 templates/__PLACEHOLDER__│  ← 4 套骨架
└────────────────────────────────┘
    │
    ▼
┌────────────────────────────────┐
│ 5. 写前对清单逐条自检          │  ← 不通过显式列出
└────────────────────────────────┘
    │
    ▼
┌────────────────────────────────┐
│ 6. Write/Edit 落盘 + 提示编译  │  ← xelatex 出 PDF
└────────────────────────────────┘
```

## 路线图

- [ ] 增加"答复审查意见"（OA 答辩）专项工作流
- [ ] 增加权利要求**保护范围演算助手**（基于 means-plus-function 等价范围）
- [ ] 增加 CNIPA 检索系统的新颖性自检脚本
- [ ] 增加 PCT 国际申请桥接（向 WIPO 模板导出）
- [ ] 增加多人协作的 git diff-friendly 段号重排工具

## 贡献

欢迎 PR、Issue、Star。特别欢迎以下方向的贡献：

- 各技术领域（机械 / 电子 / 化学 / 生物 / 软件）的 `examples/` 真实样本
- CNIPA 法规更新的 `checklists/` 维护
- 多语种 README 翻译（English、日本語、한국어）
- 与 [Claude Code Plugin Marketplace](https://docs.claude.com/en/docs/claude-code/plugins) 的集成

## 致谢

- 本 Skill 设计思路受 [CanYellow/LatexPatentTemplate](https://github.com/CanYellow/LatexPatentTemplate) 启发——感谢前辈在 LaTeX → CN 专利映射上的探索
- CNIPA 2026 申报规范来源：[国家知识产权局官网](https://www.cnipa.gov.cn/)
- 用 [Claude Code](https://claude.com/claude-code) (Opus 4.7 1M context) 起草、调试、编译

## License

[MIT](./LICENSE) © 2026 handsomeZR-netizen

---

> 如果这个 Skill 帮你省下了与代理人扯皮的两个下午，请给个 Star 让更多人看到。
