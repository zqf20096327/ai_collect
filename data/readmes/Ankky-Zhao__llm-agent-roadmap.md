# Agent Atlas · LLM Agent 学习地图

[中文](#中文) | [English](#english)

🌐 **在线页面 / Live page** · https://ankky-zhao.github.io/llm-agent-roadmap/

一份中英双语的 LLM agent 学习地图，从第一个工具调用循环到前沿研究方向，最后落到一个自己的项目。

A bilingual (Chinese and English) roadmap for learning LLM agents, from the first tool-calling loop to frontier research directions, ending in a project of your own.

| | |
|---|---|
| 阶段与模块 / Stages and modules | 7 个阶段，27 个模块 / 7 stages, 27 modules |
| 带讲解与练习的模块 / Modules with lessons | 4（阶段 1，其余分批补充 / stage 1, the rest follows in batches） |
| 练习 / Exercises | 12（9 个代码练习，3 个推导练习 / 9 coding, 3 derivation） |
| 资源 / Resources | 277（核验于 2026-09-15 / verified on 2026-09-15） |
| 关键论文 / Key papers | 99（2020 至 2026 / 2020 to 2026） |
| 术语 / Glossary terms | 22 |

姊妹路线 / Sibling roadmaps · [大模型机制学习路线 LLM Mechanism Roadmap](https://github.com/Ankky-Zhao/llm-mechanism-roadmap) · [Web Scraping Roadmap](https://github.com/Ankky-Zhao/web-scraping-roadmap)

---

## 中文

### 目的

- **建立整体认识。** 领域地图把 agent 领域分成五层，论文时间线按发布时间列出 99 篇关键论文，学习者可以先找到自己的位置，再决定往哪里走。
- **学会动手实现。** 学习路线从不依赖框架的 agent 循环开始，逐步覆盖工具、记忆、评估、安全和部署。带讲解的模块配有可以自动检查的练习。
- **同时面向求职与科研。** 页面提供两条路线的筛选，项目阶梯从第 4 级起按求职与科研分岔，另有科研入门的六个步骤。

### 适合的读者

- 用过大模型的 API，希望系统学习 agent 的开发者
- 准备 agent 开发或大模型应用岗位的求职者
- 希望以 agent 为研究方向的研究生

前置知识为 Python 基础。模型内部的原理不在本仓库的范围内，可参考姊妹仓库大模型机制学习路线。

### 学习路线

| 阶段 | 模块 |
|---|---|
| 0 起点 | LLM 基础 · 中文学习路径 |
| 1 Agent 入门 | 1.1 工具调用的格式 · 1.2 Agent 循环 · 1.3 结构化输出、校验与重试 · 1.4 工作流与 agent 的设计模式 |
| 2 核心能力 | MCP 与工具协议 · 记忆与检索 · 编排框架 |
| 3 可靠性 | 失败模式 · 评估 · 可观测性 · 安全与防护 |
| 4 生产化 | 后端与 API · 容器与部署 · 延迟、成本与可靠性 · 实时与语音 |
| 5 前沿方向 | Agentic RL 与后训练 · Coding agents · Computer-use 与浏览器 agent · 多智能体与协议 · 安全、对齐与可解释 |
| 6 做项目与持续成长 | 项目模板与起点 · 科研入门方法 · 求职准备 · 社区与持续跟进 · 全局视角与开放问题 |

### 每个模块包含的内容

每个模块都有以下部分。

| 部分 | 说明 |
|---|---|
| 为什么重要 | 这个模块解决什么问题 |
| 要能说清楚的概念与自检问题 | 学完后应当能够解释的内容 |
| 分层资源 | 按了解、掌握、深入三层排列，每条附推荐理由，标“必读”的资源构成约 150 小时的核心路径 |
| 动手任务 | 一个需要自己完成的小项目 |
| 开放问题 | 仅前沿模块，列出尚未解决的研究问题 |

阶段 1 的四个模块另有“讲解与练习”，其余阶段将分批补充。

| 部分 | 说明 |
|---|---|
| 打个比方 | 用日常例子说明核心想法 |
| 新术语 | 首次出现的术语，均收录在术语表中 |
| 讲解与示意图 | 中英双语的正文 |
| 公式与推导 | 仅在有数学内容的模块，例如成本随轮数的增长、重试后的成功率、多步任务的可靠性 |
| 代码练习 | 给出函数框架和 TODO，配自动检查，先给提示再给参考答案 |
| 推导练习 | 需要动手推的小题，附答案 |
| 常见疑问 | 学习时容易卡住的问题和面试中的追问 |

### 页面上的其他栏目

- **领域地图。** 模型层、单 agent 核心机制、系统层、应用领域，以及贯穿各层的保障层，每个节点链接到对应模块。
- **论文时间线。** 可按方向筛选，每篇用一句话说明它带来的变化。
- **项目阶梯。** 从一个周末到两个月的七级项目。
- **科研入门六步、术语表与自检清单。**
- **学习进度。** 勾选记录保存在浏览器本地（localStorage），不上传数据。

### 如何使用

**在线阅读。** 打开[在线页面](https://ankky-zhao.github.io/llm-agent-roadmap/)，右上角可切换中文和英文。

**做练习。** 模块页面上有 Colab 链接。阶段 1 的练习只使用 Python 标准库，用一个按脚本回复的假模型代替真实模型，结果是确定的，几秒内可以跑完。本地运行的方式如下。

```bash
# 补全 exercises/<id>/starter.py 中的 TODO，再把 tests.py 的内容接在后面运行
python3 scripts/run_tests.py            # 运行全部练习：参考答案必须通过，未完成的框架必须不通过
python3 scripts/run_tests.py a12_loop   # 只运行某一个练习
```

**修改内容并重新生成页面。**

```bash
python3 build.py                    # 由 data/ 与 exercises/ 生成 index.html，无第三方依赖
python3 scripts/make_notebooks.py   # 重新生成 notebooks/
python3 scripts/check_links.py      # 检查资源链接
```

### 仓库结构

```
data/
  content.json     阶段、模块、讲解、推导、术语表、领域地图、项目阶梯
  resources.json   资源及推荐理由
  papers.json      论文时间线
  figures/*.svg    示意图
exercises/<id>/
  meta.json        标题、题面、提示
  starter.py       带 TODO 的函数框架
  tests.py         自动检查
  solution.py      参考答案
notebooks/         每个带练习的模块一个 .ipynb，由脚本生成
scripts/           run_tests.py、make_notebooks.py、check_links.py
template.html      页面模板
build.py           构建脚本
index.html         生成的页面，用于 GitHub Pages
```

### 部署与维护

仓库通过 GitHub Actions 发布到 GitHub Pages。`pages.yml` 在每次 push 到 `main` 时构建并发布，`tests.yml` 运行练习，`link-check.yml` 每周检查一次链接并在发现失效链接时开 issue。

### 说明与局限

- 目前只有阶段 1 带有讲解与练习，其余模块仍是资源导航的形式。
- 资源链接核验于 2026-09-15。这一领域变化较快，框架和协议的细节可能已经更新。
- 练习中的假模型只用于检查循环、解析和重试等逻辑，不能反映真实模型的行为，真实模型上的表现需要另行测量。
- 推导中的数值是示例，独立性等假设是简化，正文中有说明。

### 贡献

欢迎纠错与补充，见 [CONTRIBUTING.md](CONTRIBUTING.md)。

### 许可

- 内容（`data/`、`exercises/*/meta.json`、页面文案）采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 代码（`template.html`、`build.py`、`scripts/`、练习中的 `.py` 文件）采用 MIT 许可

资源与论文的版权归各自作者所有。

---

## English

### Purpose

- **Building an overall picture.** The landscape divides the field of agents into five layers, and the paper timeline lists 99 key papers by date of release, so that a learner can first find a position and then decide where to go.
- **Learning to implement.** The path starts with an agent loop that uses no framework and goes on to tools, memory, evaluation, safety and deployment. Modules with lessons come with exercises that are checked automatically.
- **Serving both industry and research.** The page filters by the two tracks, the project ladder forks from rung 4 on, and six steps into research are given.

### Who it is for

- Developers who have used LLM APIs and would like to learn agents systematically
- Candidates preparing for agent engineering or LLM application roles
- Graduate students who would like to take agents as a research direction

The prerequisite is basic Python. How models work internally is outside the scope of this repository and is covered by the sibling LLM Mechanism Roadmap.

### The learning path

| Stage | Modules |
|---|---|
| 0 Foundations | LLM foundations · Chinese-language learning path |
| 1 Agent fundamentals | 1.1 The format of tool calls · 1.2 The agent loop · 1.3 Structured output, validation and retries · 1.4 Design patterns: workflows and agents |
| 2 Core capabilities | MCP and tool protocols · Memory and retrieval · Orchestration frameworks |
| 3 Reliability | Failure modes · Evaluation · Observability · Security and guardrails |
| 4 Production | Backend and APIs · Containers and deployment · Latency, cost and reliability · Realtime and voice |
| 5 Frontiers | Agentic RL and post-training · Coding agents · Computer-use and browser agents · Multi-agent systems and protocols · Safety, alignment and interpretability |
| 6 Build and keep growing | Project templates and starting points · How to start research · Job preparation · Community and staying current · The big picture and open problems |

### What each module contains

Every module has the following parts.

| Part | Description |
|---|---|
| Why it matters | Which problem the module addresses |
| Concepts and self-check questions | What a learner should be able to explain afterwards |
| Tiered resources | Arranged as intro, core and deep, each with a reason. Resources marked as must form a core path of about 150 hours |
| Hands-on task | A small project to complete |
| Open problems | Frontier modules only, listing unsolved research questions |

The four modules of stage 1 also have a lesson, and the other stages will follow in batches.

| Part | Description |
|---|---|
| An everyday picture | The core idea in an everyday example |
| New terms | Terms that appear for the first time, each listed in the glossary |
| Explanation and figure | Bilingual text |
| Formulas and derivations | Only where mathematics applies, such as cost growth over turns, success rates with retries and the reliability of multi-step tasks |
| Coding exercises | A function skeleton with TODOs and automatic checks, with hints before the reference solution |
| Derivation exercises | Short problems to work out by hand, with answers |
| Common questions | Points where learners tend to get stuck and follow-up questions from interviews |

### Other sections on the page

- **Landscape.** The model layer, the core mechanisms of a single agent, the system layer, application domains and a cross-cutting assurance layer, with every node linked to its module.
- **Paper timeline.** Filterable by area, with one sentence per paper on what it changed.
- **Project ladder.** Seven rungs, from one weekend to two months.
- **Six steps into research, glossary and self-check list.**
- **Progress.** Checkmarks are stored locally in the browser (localStorage). No data is uploaded.

### How to use it

**Read online.** Open the [live page](https://ankky-zhao.github.io/llm-agent-roadmap/) and switch between Chinese and English in the top right corner.

**Do the exercises.** Module pages carry a Colab link. The exercises of stage 1 use the Python standard library only and replace the real model with a stand-in that replies from a script, so the results are deterministic and run within seconds. To run locally, use the following commands.

```bash
# fill in the TODOs in exercises/<id>/starter.py, then append tests.py and run
python3 scripts/run_tests.py            # all exercises: solutions must pass, unfinished starters must fail
python3 scripts/run_tests.py a12_loop   # a single exercise
```

**Edit the content and rebuild the page.**

```bash
python3 build.py                    # builds index.html from data/ and exercises/, no third-party dependency
python3 scripts/make_notebooks.py   # regenerates notebooks/
python3 scripts/check_links.py      # checks the resource links
```

### Repository layout

```
data/
  content.json     stages, modules, lessons, derivations, glossary, landscape, project ladder
  resources.json   resources with reasons
  papers.json      paper timeline
  figures/*.svg    diagrams
exercises/<id>/
  meta.json        title, statement, hints
  starter.py       function skeleton with TODOs
  tests.py         automatic checks
  solution.py      reference solution
notebooks/         one .ipynb per module with exercises, generated by a script
scripts/           run_tests.py, make_notebooks.py, check_links.py
template.html      page template
build.py           build script
index.html         generated page, served by GitHub Pages
```

### Deployment and maintenance

The repository is published to GitHub Pages through GitHub Actions. `pages.yml` builds and publishes on each push to `main`, `tests.yml` runs the exercises, and `link-check.yml` checks the links once a week and opens an issue when a dead link is found.

### Notes and limitations

- At present stage 1 alone has lessons and exercises, and the other modules remain in the form of a resource guide.
- The resource links were verified on 2026-09-15. The field moves quickly, and details of frameworks and protocols may have changed since.
- The stand-in model of the exercises serves to check the logic of the loop, parsing and retries. It does not reflect the behaviour of real models, which has to be measured separately.
- The numbers in the derivations are examples, and assumptions such as independence are simplifications, as the text states.

### Contributing

Corrections and additions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

### License

- Content (`data/`, `exercises/*/meta.json`, page text) is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- Code (`template.html`, `build.py`, `scripts/`, the `.py` files of the exercises) is released under the MIT License

The copyright of the listed resources and papers remains with their authors.

---

Curated by Anqi (Ankky) Zhao · Technical University of Munich
