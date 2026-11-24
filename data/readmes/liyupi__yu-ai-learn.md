# 🎮 鱼皮 AI 闯关学习小程序（yu-ai-learn）

基于 Taro 4、React 18、Python FastAPI、LangChain、LangGraph 与 DeepSeek 构建的开源 AI 闯关答题微信小程序，由 [程序员鱼皮](http://dogyupi.com/) 与编程导航团队以 Vibe Coding + OpenSpec 规范驱动方式原创开发，支持一句话联网搜索出题、私有文档 RAG 知识库出题、AI 生图配图、即时判分讲解、通关复盘报告与微信云托管上线发布。

[![Taro 4](https://img.shields.io/badge/Taro-4.x-0066FF.svg)](https://taro.zone/)
[![React](https://img.shields.io/badge/React-18-61DAFB.svg)](https://react.dev/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Python%203.11+-009688.svg)](https://fastapi.tiangolo.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-ReAct%20Agent-FF6B6B.svg)](https://github.com/langchain-ai/langgraph)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

[项目介绍](#-项目介绍) · [八大核心能力](#-八大核心能力) · [项目优势与工程方法](#-项目优势与工程方法) · [系统架构与技术选型](#-系统架构与技术选型) · [快速运行与部署](#-快速运行与部署) · [生态学习资源](#-生态学习资源) · [常见问题](#-常见问题) · [加入系统学习](#-加入系统学习)

> 本仓库为教学实战项目，在 [编程导航 AI 闯关学习小程序课程主页](https://www.codefather.cn/course/2037104890135748610) 提供完整视频教程、配套文字笔记、简历写法参考、面试题解与 1 对 1 答疑服务，带你体验从想法调研到真正上线微信生态的全链路开发。欢迎直接通过 [编程导航会员通道](https://www.codefather.cn/vip) 加入系统学习！

## ✨ 项目介绍

`yu-ai-learn` 是一套以「AI 编程实战 + 小程序产品上线」为核心的全栈开源项目，基于 Taro 4、React 18、Python FastAPI、LangChain、LangGraph 与 DeepSeek 构建，并结合 GitHub Copilot、Claude Code 与 OpenSpec 规范驱动开发工作流从零落地。用户只需输入一句话描述想学的主题，AI 就会自动联网检索最新资料并生成一套闯关题目，陪伴用户边答边学、逐题即时解析，通关后还会生成专属 AI 复盘报告，真正带你走通从需求分析到小程序备案审核发布的完整闭环。

![鱼皮 AI 闯关学习微信小程序首页与核心交互流程全景展示](./doc/images/img-01.png)

### 为什么做这个项目

学习新知识最大的阻力往往不是内容晦涩，而是过程枯燥。单向阅读文档或观看长视频很容易走神，即便看完了也难以留下深刻记忆。相反，人类天生喜欢游戏化的即时反馈机制，喜欢闯关、挑战与收获成就感。借助现代大模型与 Agent 技术，我们可以把任何想学的知识点瞬间转化成一局随时可玩的闯关游戏。

之所以选择微信小程序而非独立 App 或普通网页，是因为碎片化学习天然契合「免安装、即用即走、易裂变分享」的微信生态，非常适合学习类工具的传播与留存。更重要的是，这套技术骨架具有极强的跨领域复用价值——只需替换底层知识源和提示词策略，就能快速孵化出驾考刷题、程序员面试闯关、企业内部培训考核、职业资格考试复习或儿童英语单词闯关等各类垂直产品。

![将 AI 闯关学习骨架快速复用到驾考理论等垂直知识场景的答题流程](./doc/images/img-02.png)

## 🎯 八大核心能力

整个小程序围绕「自由起题、智能联网、私有知识库、配图增强、即时讲解、复盘激励、微信生态上线」八个环节打磨了完整流畅的产品体验。

### 1. 一句话起题与 ReAct 联网搜索出题

为了突破大模型训练知识的截止时间限制，项目引入 Tavily 联网搜索并基于 LangGraph 构建了一个 ReAct 自主决策智能体。面对前沿或时效性较强的主题，Agent 会自主判断需要检索哪些关键词、执行几轮搜索，随后再生成结构化高质量题目，确保题目内容紧跟最新事实。

![基于 LangGraph ReAct 智能体联网检索最新资料并动态出题演示](./doc/images/img-03.png)

### 2. 闯关答题与即时判分讲解

闯关界面支持单选题、多选题与判断题三种经典题型。每提交一题，界面都会立即高亮正确答案、标出错误选项，并同步展示通俗易懂的解析与核心知识点归类，即使答错也能当场弄懂原理。

![支持单选多选判断的实时判分高亮与错题即时知识点讲解界面](./doc/images/img-04.png)

### 3. AI 个性化通关复盘报告

完成整组关卡后，系统会自动汇总用户的作答表现并由大模型生成专属复盘报告，清晰呈现掌握度评分、薄弱知识点清单、三句话精华总结以及下一步学习建议，同时结算本局赢得的经验值奖励。

![闯关结束后生成的 AI 掌握度评分薄弱知识点与学习复盘报告](./doc/images/img-05.png)

### 4. 完全自由的任意主题输入

用户的起题方式不受固定题库束缚，无论是简短的一句话概念、一段学习笔记，还是一个公开网页链接，系统都能自动分析语境并补全背景知识，按需定制专属练习关卡。

![输入任意网址或自定义主题由 AI 自动解析背景并生成题库](./doc/images/img-06.png)

### 5. 上传私有文档构建 RAG 知识库出题

对于企业内部培训、课程讲义复习或特定规章制度考核等专业场景，小程序支持直接上传 PDF、Word、Markdown 和纯文本四种格式的私有文档。后端会自动完成文本解析、切片分块与向量化，并存入 Chroma 向量库，之后即可精准依据用户上传的私有资料出题。

![上传 PDF Word Markdown 私有文档基于 Chroma RAG 知识库精准出题](./doc/images/img-07.png)

### 6. AI 题目生图配图与成本管控

为了让抽象知识点更容易理解，后端集成了阿里云百炼通义千问文生图模型，按知识点自动生成形象配图并转存至腾讯云 COS 获得持久化访问链接，同时配套实现了每日额度限制与并发控制，避免生成费用失控。

![调用通义千问文生图结合腾讯云 COS 持久化存储的 AI 配图答题界面](./doc/images/img-08.png)

### 7. 微信一键静默登录与历史回看

借助微信 `jscode2session` 静默登录机制，用户无需繁琐表单即可无感创建账号，并在个人中心随时查看累计经验值与历史闯关记录，点击任意记录都能重温当时的复盘报告。与此同时，项目贴心地实现了「可选登录」架构，未登录访客也能直接体验核心闯关流程。

![微信静默登录个人中心累计经验值与历史闯关记录回看界面](./doc/images/img-09.png)

### 8. 完整部署上线微信生态

不同于只停留在本地模拟器里的演示项目，教程完整带你走完了真实的上线最后一公里：后端通过 Docker 容器化部署至微信云托管，并按规范完成 AI 问答相关服务类目申请、ICP 备案、服务器域名配置与微信代码审核，最终实现微信内可直接搜索访问。

![后端 Docker 部署微信云托管并正式通过审核上线的小程序效果](./doc/images/img-10.png)

## 🌟 项目优势与工程方法

本项目将当下最热门的 AI 编程方法论与真实微信小程序上线流程合二为一，内容紧凑高效，通常不到一周就能学完并独立跑通全流程。无论你是想体验长周期项目中如何稳定驾驭 AI 写代码，还是想为求职简历或毕业设计准备一款真正线上可体验的 AI 小程序作品，都非常契合。

![AI 闯关学习小程序全链路技术覆盖与 AI 编程工程能力全景图](./doc/images/img-11.png)

跟着项目一步步实践下来，你将系统掌握以下 11 项前沿工程实战能力：

1. 运用 AI 完成需求调研与竞品分析，清晰划定 MVP 核心边界与后续扩展模块。
2. 熟练配置 MCP 服务与 Agent Skills，充分释放 GitHub Copilot 与 Claude Code 的工程能力。
3. 实战「多模型 UI 原型赛马」方法，让多个 AI 工具并行产出高颜值界面原型并择优落地。
4. 从零完成跨端微信小程序工程化开发，涵盖 Taro 4 选型、脚手架搭建、页面交互与真机调试。
5. 使用 LangChain 编排大模型调用并约束结构化输出，确保 AI 稳定返回符合协议的 JSON 题目数据。
6. 使用 LangGraph 构建 ReAct 智能体，把单次大模型对话升级为会自主联网查资料的 AI Agent。
7. 从零搭建完整的 Chroma RAG 私有知识库，贯通文档解析、分块、向量嵌入与检索增强出题。
8. 接入通义千问 AI 生图并联合腾讯云 COS 对象存储，将临时图床链接安全转化为永久静态资源。
9. 落地 OpenSpec 规范驱动开发（SDD），让 AI 在多轮迭代的长周期项目中保持高质量稳定输出。
10. 深入理解并践行 Harness Engineering，借助需求文档、设计方案、UI 原型、MCP、Skills 与 Git 为 AI 搭建可靠工程脚手架。
11. 掌握后端 Docker 容器化部署微信云托管，以及小程序类目申请、ICP 备案与审核发布的完整上线流程。

### 鱼皮原创项目系列特色

鱼皮原创项目系列坚持以实战视频教程为核心，从零带做覆盖企业级 Java / Python / Go 后端、前端全栈、AI 应用开发、AI 编程与大厂架构进阶的近 30 套保姆级项目，并同步配套完整源码、简历写法和面试题解，帮助你高效地把技术转化为求职竞争力。

![鱼皮原创项目实战从学知识到做项目拿 Offer 的一条龙服务体系](./doc/images/img-12.jpg)

目前编程导航已提供近 30 套侧重点各不相同的原创全栈与 AI 项目教程，零基础也能找到合适的切入点。你可以访问 [编程导航项目课程页面](https://www.codefather.cn/course) 右侧查阅完整的项目推荐与学习路线建议。

![编程导航近 30 套原创全栈与 AI 实战项目课程矩阵展示](./doc/images/img-13.png)

多年实战沉淀已经帮助大量同学打磨出具备差异化亮点的简历作品，成功斩获众多大厂与一线互联网公司 Offer。

![编程导航学员跟着鱼皮做原创项目收获 2026 大厂高薪 Offer 报喜墙](./doc/images/img-14.png)

## 📐 系统架构与技术选型

项目涵盖闯关答题、AI 出题、复盘报告、用户系统、私有知识库与 AI 配图 6 大业务模块、30 余个真实功能点，完整覆盖了一款上线小程序从交互到后台服务的全链路设计。

![鱼皮 AI 闯关学习小程序六大业务模块与三十余项功能点总览图](./doc/images/img-15.png)

整体架构采用前后端分离设计，前端基于 Taro 4 + React 18 构建微信小程序，后端基于 Python FastAPI + LangChain / LangGraph 编排大模型、联网检索与 Chroma 向量库，并配合 MySQL 与腾讯云 COS 实现可靠持久化。

![Taro 微信小程序与 FastAPI LangGraph Chroma 整体系统架构图](./doc/images/img-16.png)

### 技术选型清单

| 层面 | 技术选型 |
| --- | --- |
| 小程序前端 | Taro 4 · React 18 · TypeScript · Sass |
| 后端服务 | Python 3.11+ · FastAPI · Pydantic v2 · Uvicorn · asyncio |
| AI 编排 | LangChain · LangGraph · langchain-openai |
| 大模型 / 检索 | DeepSeek（出题 / 报告）· 阿里云百炼（Embedding / 文生图）· Tavily（联网搜索） |
| 向量检索 | Chroma（RAG 知识库） |
| 数据存储 | MySQL（aiomysql 异步连接池）· 腾讯云 COS（对象存储） |
| 鉴权 | 微信 `jscode2session` 静默登录 + JWT |
| 测试 | pytest · pytest-asyncio |
| 部署 | Docker · 微信云托管 · 云数据库 MySQL |
| AI 编程工具 | GitHub Copilot · Claude Code · OpenSpec · MCP · Agent Skills |
| AI 编程方法 | Harness Engineering · 规范驱动开发（SDD）· 原型赛马 · 上下文管理 |

### 仓库目录结构

除了前后端业务源码之外，本仓库还完整保留了 OpenSpec 规范文档、多版本 UI 原型以及详尽的运行教程，方便你近距离观摩规范驱动开发（SDD）的真实产物。

```text
yu-ai-learn/
├── frontend/    # Taro 4 + React 18 + TypeScript 微信小程序前端工程
├── backend/     # Python FastAPI + LangChain + LangGraph + Chroma 后端服务与 Dockerfile
├── openspec/    # OpenSpec 规范驱动开发（SDD）提案与设计规范记录
├── prototypes/  # AI 原型赛马产出的高保真界面原型参考
└── docs/        # 保姆级本地运行指南、API 申请步骤与常见问题排查文档
```

## 🚀 快速运行与部署

> 完整的保姆级图文步骤请直接查阅 [保姆级本地运行指南](./docs/保姆级本地运行指南.md)，文档中包含每个 API Key 的详细申请流程、环境变量逐项解释以及 11 个高频报错的排查方案。下面是快速启动精简版。

### 前置条件

本地启动前请先准备好 Python 3.11 及以上版本、Node.js 18 及以上版本（推荐 20+）、MySQL 8.0 及以上版本，以及 [微信开发者工具](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html)。第三方服务凭证方面，只需按需准备以下配置：

| 服务凭证 | 是否必需 | 核心用途 |
| --- | --- | --- |
| [DeepSeek API Key](https://platform.deepseek.com/) | 必需 | 驱动 AI 出题与通关复盘报告生成 |
| [Tavily API Key](https://tavily.com/) | 可选 | 开启 ReAct Agent 联网搜索增强出题 |
| [阿里云百炼 API Key](https://bailian.console.aliyun.com/) | 可选 | 开启私有知识库 RAG 向量化与 AI 文生图配图 |
| [腾讯云 COS 存储桶](https://console.cloud.tencent.com/cos) | 可选 | 持久化转存 AI 生成的题目配图 |
| [微信小程序测试号](https://developers.weixin.qq.com/sandbox) | 可选 | 调试微信静默登录与真机预览 |

### 1. 克隆项目

```bash
git clone https://github.com/liyupi/yu-ai-learn.git
cd yu-ai-learn
```

### 2. 启动后端服务

建议先创建独立的 Python 虚拟环境安装依赖，再配置环境变量启动 FastAPI 服务。

```bash
cd backend

# 创建并激活虚拟环境
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\Activate.ps1

# 安装依赖（国内可加 -i https://pypi.tuna.tsinghua.edu.cn/simple 加速）
pip3 install -r requirements.txt

# 配置环境变量（至少填写 DEEPSEEK_API_KEY 和 MYSQL_PASSWORD）
cp .env.example .env

# 启动服务（数据表会在启动时自动创建）
python3 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

启动成功后打开浏览器访问 `http://localhost:8000/docs`，看到 FastAPI 自动生成的交互式接口文档即说明后端运行正常。

> **数据库初始化提示**：无需手动建库建表，当 `MYSQL_AUTO_INIT=true` 时后端启动会自动创建数据库和全部 7 张业务表，也可以手动执行 `python3 scripts/init_mysql.py` 完成初始化。请注意不要使用 `sql/init_mysql.sql` 建表，该旧文件缺少 3 张表。

### 3. 启动小程序前端

新开一个终端窗口进入 `frontend` 目录，安装依赖并以监听模式编译微信小程序代码到 `dist/` 目录。

```bash
cd frontend
npm install                       # 国内可加 --registry=https://registry.npmmirror.com
npm run dev:weapp                 # 编译到 dist/ 并进入监听模式
```

打开微信开发者工具新建项目，将项目目录指向 `frontend/dist`，AppID 填入你的微信测试号 AppID。本地联调阶段，务必在开发者工具右上角的「详情」进入「本地设置」，勾选「不校验合法域名」，否则针对 `localhost` 的本地接口请求会被拦截。

如需执行生产环境构建（自动切换至线上后端接口地址），运行以下命令即可：

```bash
npm run build:weapp
```

### 4. 运行自动化测试

后端测试套件已通过 Mock 完整隔离了大模型与外部第三方 API 调用，运行测试不会消耗任何 API 额度。

```bash
cd backend
pytest
```

### 5. Docker 容器化与线上发布

`backend/Dockerfile` 已经针对微信云托管做好了镜像构建适配，同时也兼容任意支持 Docker 的云服务器或容器平台。所有密钥类环境变量（数据库密码、各类 API Key、微信 AppSecret、`JWT_SECRET` 等）请务必通过部署平台的环境变量注入，切勿提交到代码仓库。

> 正式发布到微信生态还需按流程完成小程序服务类目申请（AI 类应用需申请「深度合成 - AI 问答」类目及准备相应资质材料）、ICP 备案、服务器域名白名单配置与代码提审，完整避坑细节在课程第 12 期有详尽演示。

## 📚 生态学习资源

如果你想在学完本项目后进一步锤炼 Vibe Coding 工程能力、探索更多 AI 应用架构或准备技术面试，欢迎搭配以下由 [程序员鱼皮](http://dogyupi.com/) 团队维护的生态资源：

1. 想系统学习 Vibe Coding、OpenSpec、MCP 与前沿大模型工具实践，推荐先收藏鱼皮开源的 [AI 编程教程与大模型知识库（ai-guide）](https://github.com/liyupi/ai-guide)，同步关注 [鱼皮 AI 导航](https://ai.codefather.cn)，并可跟学 [AI 编程实战进阶课](https://ai.codefather.cn/course/2087008226460565505) 持续提升 AI 驾驭能力。
2. 当你把这套微信小程序 + LangGraph + RAG 项目写进简历准备冲刺校招或社招时，推荐前往 [程序员面试刷题神器面试鸭](https://www.mianshiya.com/) 刷透 Python、FastAPI、React、TypeScript、MySQL、Docker 以及 AI Agent 与 RAG 检索增强等高频面试题。

## ❓ 常见问题

<details>
<summary><b>Q1：有没有开源的 AI 闯关答题微信小程序实战项目，适合学习或作为毕业设计？</b></summary>

有，`yu-ai-learn` 是一款基于 Taro 4、React 18、Python FastAPI、LangChain、LangGraph 和 DeepSeek 开源的完整 AI 闯关学习微信小程序。它包含联网搜索出题、私有文档 RAG 知识库出题、AI 文生图配图、实时判分讲解、通关复盘报告和微信云托管部署，不仅适合全栈实战学习，还非常适合作为高分计算机毕业设计或迁移到驾考、企业培训、面试刷题等垂直赛道。

</details>

<details>
<summary><b>Q2：如何用 Taro 4、FastAPI 和 LangGraph 实现带联网搜索与 RAG 私有知识库的 AI 出题系统？</b></summary>

本仓库提供了完整的端到端工程实现：小程序前端通过 Taro 4 + React 18 承接主题输入、文档上传与闯关答题交互；FastAPI 后端使用 LangGraph 编排 ReAct 智能体结合 Tavily 实时联网搜集最新资料，并通过 Chroma 向量库对上传的 PDF/Word/Markdown/TXT 文档完成分块向量化与检索增强，最后借助 LangChain 结构化输出稳定生成规范的 JSON 题库。

</details>

<details>
<summary><b>Q3：什么是 OpenSpec 规范驱动开发（SDD）和 Harness Engineering，如何在真实 AI 编程项目中落地？</b></summary>

规范驱动开发（SDD）与 Harness Engineering 的核心思想，是通过先沉淀清晰的需求规格、设计方案、UI 原型、MCP 工具与 Agent Skills 来为 AI 编程助手搭好可靠的工程护栏，避免长周期迭代中代码失控。本仓库直接保留了 `openspec/` 与 `prototypes/` 两个目录，完整展示了鱼皮团队在实战中落地这套 AI 工程方法论的真实文件结构。

</details>

<details>
<summary><b>Q4：微信小程序接入 AI 大模型问答功能上线，需要准备哪些资质类目与部署流程？</b></summary>

上线阶段除了将后端容器化部署（如采用仓库自带的 `backend/Dockerfile` 部署到微信云托管）以及配置服务器合法域名白名单外，还需要完成小程序 ICP 备案、申请对应的「深度合成 - AI 问答」服务类目并提交资质材料，最终通过微信官方代码审核即可正式发布。

</details>

<details>
<summary><b>Q5：如果暂时没有申请全部可选 API Key，能否先在本地完整跑通这个 AI 闯关小程序？</b></summary>

完全可以。本地启动核心流程只需要配置 `DEEPSEEK_API_KEY` 和本地 `MYSQL_PASSWORD` 两项基础参数，就能立即跑通一句话出题、闯关答题、即时讲解与 AI 通关复盘报告，并且支持未登录状态直接体验；Tavily 联网搜索、阿里云百炼 RAG/生图、腾讯云 COS 与微信登录均可在后续按需逐步开启。

</details>

## 🎓 加入系统学习

如果你想跟着完整视频教程体验从需求调研、UI 原型赛马、OpenSpec 规范驱动开发到小程序备案上线的每一个实战环节，欢迎前往 [AI 闯关学习小程序课程主页](https://www.codefather.cn/course/2037104890135748610) 查看完整课表。编程导航目前已汇集近 30 套涵盖 AI 编程、AI 应用开发与企业级全栈的原创项目课程，零基础同学也能循序渐进掌握。

欢迎直接加入 [编程导航会员](https://www.codefather.cn/vip)，加入后不仅能全程跟学本项目，往期近 30 套原创项目教程也全部支持无限回看，还能获取专属答疑、求职指导与上百场真实面试回放视频。扫码下方限时编程导航优惠券即可领券加入，支持加入三天内不满意全额退款。

![编程导航会员限时优惠券扫码领取通道](./doc/images/img-17.png)

每天不到 1 块钱即可解锁近 30 套原创项目的完整教程与实战资料，PC 网站与手机 APP 端同步学习，帮助你用最快的速度打磨出高竞争力作品集。

![编程导航 PC 网站与移动 APP 双端同步学习体验展示](./doc/images/img-18.png)

更多由 [程序员鱼皮](http://dogyupi.com/) 团队打造的开源仓库、学习路线、求职工具与 AI 实战干货，欢迎访问 [鱼皮团队资源大全](http://dogyupi.com/) 一站式探索。如果这个项目对你有帮助，欢迎点亮右上角的 Star 支持我们！
