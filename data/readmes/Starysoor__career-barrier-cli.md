<div align="center">

# CAREER BARRIER CLI

**生涯闯关 · 本地优先的 Python 命令行工具**

从浏览器会话、个性化内容生成，到 PDF 文档构建与服务端结果核验，\
将分散的练习任务组织为一条可配置、可恢复、可追溯的工作流。

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Dependencies](https://img.shields.io/badge/Dependencies-0-16A34A?style=flat-square)](#环境要求)
[![AI](https://img.shields.io/badge/AI-OpenAI%20Compatible-6366F1?style=flat-square)](#ai-模型接入)
[![License](https://img.shields.io/badge/License-MIT-0891B2?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/Starysoor/career-barrier-cli?style=flat-square&color=111827)](https://github.com/Starysoor/career-barrier-cli/releases)

[核心能力](#核心能力) · [工作流](#工作流) · [快速开始](#快速开始) · [配置](#配置) · [安全与隐私](#安全与隐私) · [致谢](#致谢)

<br/>

| **8** | **3** | **5** | **0** |
| :---: | :---: | :---: | :---: |
| 可提交关卡 | 内容生成模式 | PDF 文档正文支持 AI | 第三方 Python 依赖 |

</div>

> [!IMPORTANT]
> 本项目是非官方第三方工具，与全国大学生职业规划大赛主办方、学信网及任何高校无关联。仅供技术学习、离线测试及经学校和平台明确允许的练习场景使用；不得用于正式参赛、评奖、排名或商业用途，不应以生成内容冒充本人真实经历。自动化可能违反平台规则，请先确认授权。

## 核心能力

| 模块 | 设计与实现 |
| :--- | :--- |
| **任务编排** | 八个可提交关卡的流程管理，支持失败续跑、指定关卡和覆盖范围控制。 |
| **生成策略** | 内置模板、AI 生成、随机三种模式；AI 失败时回退模板，保留来源统计。 |
| **个性化配置** | 专业、兴趣、经历及字段级自定义；AI 模式可按专业生成职业、书籍与活动等候选内容。 |
| **原生 PDF 引擎** | 无第三方 Python 依赖的 PDF 排版能力，支持招聘简章、访谈报告、实践报告、求职计划书等文档。 |
| **浏览器会话** | 使用本机 Chrome / Edge 与 CDP 登录方案，按浏览器实际登录身份识别账号。 |
| **结果核验** | 每关结束回读服务端结果；独立只读进度工具用于二次核对。 |
| **离线自检** | 提供不联网、不写入平台数据的 dry-run 自检模式。 |

## 工作流

```mermaid
flowchart LR
    A[本地配置] --> B[内容生成策略]
    B --> C[文本与 PDF 构建]
    C --> D[任务流程]
    D --> E[结果回读]
    E --> F[状态与来源统计]
    B -. AI 失败 .-> G[内置模板]
    G --> C
```

**设计重点：** 生成与结果核验分离、内容来源可见、失败可恢复、本地配置可控。流程图为功能层面的概览，不代表独立服务或多进程架构。

## 环境要求

- Python 3.8+（仅使用标准库，无需安装 pip 依赖）
- Windows / macOS / Linux
- Chrome 或 Edge（用于需要浏览器登录的功能）

## 快速开始

获取源码后，在项目目录运行离线自检：

```bash
python 刷生涯闯关.py --dry
```

只读进度核对入口（需要合法账号及相应平台授权）：

```bash
python 查看进度.py
```

主程序为 `刷生涯闯关.py`，首次运行会进入配置向导；涉及在线操作的功能仅应在明确授权的环境使用。登录时请确认实际账号身份，切勿共享浏览器会话或本地凭据。

## 配置

首次运行生成本地 `config.json`。以下为结构示例，所有凭据均为占位符：

```jsonc
{
  "mode": "ai", // template | ai | random
  "ai": {
    "base_url": "<YOUR_API_BASE_URL>",
    "api_key": "<YOUR_API_KEY>",
    "model": "<YOUR_MODEL>"
  },
  "profile": {
    "major": "人工智能",
    "job1": "软件开发工程师",
    "interests": "",
    "highlights": ""
  },
  "overrides": {}
}
```

### AI 模型接入

兼容 OpenAI 格式接口，原有配置包含智谱 GLM、DeepSeek、Kimi、通义千问与本地 Ollama 等预设。模型可用性、价格及服务条款以对应服务商为准。

| 模式 | 内容来源 |
| :--- | :--- |
| `template` | 内置语料与预设 |
| `ai` | 配置的模型接口，失败时回退内置模板 |
| `random` | 随机策略；PDF 正文仍使用可读的内置文本 |

### 内容来源统计

运行结束时记录各来源计数，便于区分模型生成、用户自定义、模板与随机内容。

```text
内容来源统计: AI 46 ｜ 自定义 0 ｜ 模板 12 ｜ 随机 0（AI失败回退 3 次）
```

上面是原有 README 中的示例输出，不是本次运行的实测结果。AI 模式支持约 50 段文本及五份 PDF 的段落正文生成；实际计数取决于任务、配置与回退情况。

## 项目结构

```text
career-barrier-cli/
├── 刷生涯闯关.py      # 主程序：流程、生成、PDF 与浏览器登录
├── 查看进度.py        # 独立只读进度核验
├── README.md         # 项目文档
├── NOTICE.md         # 第三方来源与商标说明
├── LICENSE           # MIT 许可证
└── .gitignore        # 排除本地配置与浏览器会话等
```

## 安全与隐私

> [!WARNING]
> `config.json` 与 `.browser_profile/` 可能包含敏感凭据；请勿公开、提交或分享这些文件。

- 项目不设置独立的数据收集服务；在线功能会与相应平台通信，AI 模式也可能向所配置的模型服务发送个人资料及生成提示词。
- 只在本人账号和获授权的练习环境使用。不得绕过身份认证、平台规则或考核要求。
- 生成内容不代表实际职业经历、真实访谈或实践证明，应由本人核对、修改并确保真实。
- 服务端回读不等于平台最终认可；如状态不一致，以平台确认结果为准。

## 常见问题

<details>
<summary><b>账号不一致或 Token 无效</b></summary>

核对浏览器中实际登录的账号，必要时重新通过正规方式登录。不要公开 Token 或浏览器会话。

</details>

<details>
<summary><b>接口报错或进度不一致</b></summary>

查看错误信息及只读进度核对结果。平台可能对字段长度、状态与账号数据有额外要求；持续异常应联系平台客服，不建议反复提交。

</details>

<details>
<summary><b>PDF 网页预览异常</b></summary>

可下载文件并使用本地 PDF 阅读器检查；若本地可读但网页预览失败，应进一步确认平台预览服务状态。

</details>

## 版本记录

| 版本 | 主要变化 |
| :--- | :--- |
| **v1.1.0** | AI 生成扩展到 PDF 正文、职业榜样、职业方向、书籍及活动名称；新增内容来源统计。 |
| **v1.0.0** | 八关流程、三种内容模式、PDF 引擎、CDP 登录、账号切换和服务端回读核验。 |

更多版本信息见 [GitHub Releases](https://github.com/Starysoor/career-barrier-cli/releases)。

## 贡献

欢迎通过 [Issues](https://github.com/Starysoor/career-barrier-cli/issues) 提交问题与改进建议，或发起 Pull Request。提交前请运行离线自检，使用虚构测试资料，并确认不包含账号、手机号、Token、API Key 或浏览器会话。

## 致谢

本项目的接口协议层参考以下 MIT 许可项目，具体来源与署名见 [NOTICE.md](NOTICE.md)：

- [职业规划大赛闯关助手](https://scriptcat.org/zh-CN/script-show-page/4626) — 毫厘 / proudly。原项目文档记录，本项目 56 个平台接口中有 49 个参考其实现，提交顺序、字段名与字数要求亦参考该项目。
- [生涯闯关助手（睡衣宝宝改版）](https://scriptcat.org/zh-CN/script-show-page/4732) — 睡衣宝宝，原作者毫厘。AI 内容生成思路参考其改版。

本项目以 Python 重写，包含独立中文语料、PDF 排版引擎、CDP 登录方案、服务端回读校验与账号切换实现。保留原作者署名与许可证声明。

## 许可证

[MIT License](LICENSE) © 2026 生涯闯关助手 contributors

---

<div align="center">

**CAREER BARRIER CLI**

Local-first · Dependency-free · Traceable

[Repository](https://github.com/Starysoor/career-barrier-cli) · [Issues](https://github.com/Starysoor/career-barrier-cli/issues) · [Releases](https://github.com/Starysoor/career-barrier-cli/releases)

</div>
