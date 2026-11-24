# Application Writing Skill / 申请文书写作 Skill

[中文](#中文) · [English](#english)

## 中文

一个用于 Codex 的申请文书写作 skill，覆盖个人陈述（PS）、目的陈述（SOP）、推荐信材料（RL）、履历（CV / résumé）和暑研申请信。它从申请要求和申请人的真实经历出发，帮助调研、挖掘主线、规划结构、起草及修订文书，而不是逐句翻译已有材料。

### 它如何工作

1. **调研要求与样例**：核对目标项目的官方题目、字数、格式、提交方式和申请周期；查找相关的官方写作指南与公开样例。为本次申请建立 `requirements.md`，并在 `doc/` 中按篇记录样例链接与写法分析。
2. **梳理经历与 brainstorm**：从现有材料提出 2–3 条有证据支持的主线，比较其与题目及项目的契合度，推荐一条；用少量具体问题补足只有申请人知道的经历或判断。把客观个人信息及来源记录到 `portrait.md`。
3. **规划与起草**：按 PS、SOP、RL、CV 或申请信的用途安排内容和版式。申请人尚未确定长期方向时，可以诚实地写有证据支撑的近期探索，不虚构职业目标或个人感受。
4. **双语审阅与核对**：每份文书的审阅稿先给完整的目标语言版本，下方附逐段或逐条对应的中文参考译文。需要上传时，另准备只含申请要求语言、符合格式限制的版本。

用户只需要某一阶段时，skill 可以只完成该阶段。机构的具体题目与规定始终优先于模板。

### 支持的文书

| 类型 | 重点 |
| --- | --- |
| PS | 真实经历中的选择、行动、变化与个人动机；不预设固定格式。 |
| SOP | 学术或专业问题、已有准备、下一步计划及项目契合。 |
| RL | 推荐人能亲自证实的事例；建议稿须由推荐人审核，不能冒用其证言。 |
| CV / résumé | 可核验的教育、研究、工作、成果与技能，按申请目标选择栏目。 |
| 暑研申请信 | 与研究方向相连的经历、可贡献的能力和希望获得的训练。 |

### 安装到 Codex

#### 一句话安装

直接把以下内容发送给 Codex：

```
将 https://github.com/l4k3q/application-writing skill 安装到本地并启用
```

#### 手动安装

将仓库中的 `application-writing/` 文件夹复制到 Codex 的 skills 目录。Windows PowerShell 示例（在仓库根目录运行）：

```powershell
$destination = Join-Path $env:USERPROFILE '.codex\skills\application-writing'
New-Item -ItemType Directory -Path $destination -Force | Out-Null
Copy-Item -Path '.\application-writing\*' -Destination $destination -Recurse -Force
```

macOS / Linux 示例：

```bash
mkdir -p ~/.codex/skills/application-writing
cp -R application-writing/. ~/.codex/skills/application-writing/
```

### 使用示例

在 Codex 中调用 `$application-writing`，给出目标项目和你已有的材料；不需要先想好文书主线。例如：

> 使用 $application-writing。我要申请某校的计算机科学暑研项目，尚不确定申请信该突出什么。请先核对官方要求、分析我的 CV 和项目经历，提出并推荐文书主线，再帮我起草英文申请信和下方的中文参考译文。

若只想先调研或 brainstorm，可以明确限定阶段。申请人材料、`requirements.md`、`portrait.md` 和 `doc/` 应放在**本次申请的工作目录**，不要放进公开的 skill 仓库。

### 仓库结构

```text
application-writing/
├── SKILL.md              # 核心流程与交付规则
├── agents/openai.yaml    # Codex 中的展示信息
├── references/           # 分文书类型的写作与核对说明
└── assets/               # 五类文书各 8 个原创结构模板
```

`assets/` 中的模板依据公开的大学指南设计，并附来源链接；它们是可调整的结构提纲，不是可照抄的录取文书。skill 会区分可核验事实、写作解释与待确认的个人判断，不把申请人材料或样例作者的经历编造成新事实。

## English

A Codex skill for application writing: personal statements (PS), statements of purpose (SOP), recommendation letter materials (RL), CVs / résumés, and summer research cover letters. It starts with the program's requirements and the applicant's real experience, then helps with research, brainstorming, structure, drafting, and revision. Its goal is a coherent application narrative rather than a line-by-line translation of existing materials.

### How it works

1. **Research requirements and examples:** Check official prompts, length and file limits, submission instructions, and the application cycle. Find relevant official writing guides and public examples. Record verified requirements in `requirements.md` and save one source-linked analysis per selected example in `doc/`.
2. **Build an evidence-based direction:** Propose 2–3 plausible narrative angles from the applicant's materials, compare their fit with the prompt and program, and recommend one. Ask a few focused questions for experiences or judgments only the applicant can provide. Record objective applicant facts and their sources in `portrait.md`.
3. **Plan and draft:** Choose content and layout for the specific document. If the applicant has no fixed long-term plan, use a truthful, evidence-supported near-term direction rather than inventing a career commitment or personal feeling.
4. **Review in two languages:** Provide the complete target-language document followed by a corresponding Chinese reference translation. When an upload-ready file is needed, prepare a separate version containing only the language and format required by the program.

The skill can also handle a single requested stage. A program's actual prompt and rules take priority over every template.

### Supported documents

| Document | Focus |
| --- | --- |
| PS | Personal choices, actions, change, and motivation grounded in real experience; no fixed narrative format. |
| SOP | Academic or professional questions, preparation, next steps, and program fit. |
| RL | Examples the recommender can personally verify; any suggested draft requires the recommender's review. |
| CV / résumé | Verifiable education, research, work, outputs, and skills arranged for the target application. |
| Summer research cover letter | Relevant experience, contribution, research fit, and skills the applicant hopes to develop. |

### Install in Codex

#### Install in just one

send this to Codex directly:

```
install this skill on my computer: https://github.com/l4k3q/application-writing
```

#### Install manually

Copy the repository's `application-writing/` folder into your Codex skills directory. From the repository root, on Windows PowerShell:

```powershell
$destination = Join-Path $env:USERPROFILE '.codex\skills\application-writing'
New-Item -ItemType Directory -Path $destination -Force | Out-Null
Copy-Item -Path '.\application-writing\*' -Destination $destination -Recurse -Force
```

On macOS / Linux:

```bash
mkdir -p ~/.codex/skills/application-writing
cp -R application-writing/. ~/.codex/skills/application-writing/
```

### Example prompt

Invoke `$application-writing` in Codex and provide the target program plus any materials you already have. You do not need to choose a narrative angle first:

> Use $application-writing. I am applying to a computer science summer research program and do not know what my cover letter should emphasize. Check the official requirements, review my CV and projects, recommend a narrative direction, then draft the English letter with a Chinese reference translation below it.

You can also request only research or brainstorming. Keep personal materials, `requirements.md`, `portrait.md`, and `doc/` in the **individual application's working directory**, outside this public skill repository.

### Repository layout

```text
application-writing/
├── SKILL.md              # Core workflow and delivery rules
├── agents/openai.yaml    # Codex display metadata
├── references/           # Document-specific writing and verification guidance
└── assets/               # Eight original structural templates for each of five document types
```

The templates in `assets/` are adaptable outlines informed by linked university guidance; they are not accepted essays to copy. The skill separates verified facts, editorial interpretation, and personal judgments that still need confirmation.
