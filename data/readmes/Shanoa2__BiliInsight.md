<div align="center">
  <h1>BiliInsight</h1>
  <p>基于 Agent 架构的智能 B 站视频问答与分析系统</p>
  
  <p>
    <a href="https://github.com/Shanoa2/BiliInsight/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/badge/License-GPLv3-red.svg"></a>
    <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-green.svg">
    <a href="https://space.bilibili.com/3706926953138884"><img alt="Bilibili" src="https://img.shields.io/badge/Bilibili-@Vinsight-pink.svg"></a>
  </p>
</div>

---

**BiliInsight** 是一个不仅能“读字幕”，更能真正“看懂”画面的 B 站智能体（Agent）。
你可以在任意 B 站视频评论区 [@MioriaAI](https://space.bilibili.com/3706926953138884)（官方演示账号），向它询问关于这个视频的**任何问题**。它会像人类助理一样，自主决定该使用哪些工具（查字幕、调画面、看弹幕、上网搜）来给你最精准的答案。

## 核心特性

- **原生的 Agent 架构：** 抛弃传统的”全量拼接字幕给大模型”的简单封装模式。基于 [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python) 构建，拥有 30+ MCP 本地化工具，模型完全依靠逻辑推理**按需调用**。
- **多模态视觉理解：** 遇到”画面分析”，它懂得自己拉取对应时间点的关键帧。无论是分析 UP 主的开箱物品、解析一支舞蹈动作，还是”逐帧比对物理破绽鉴定 AI 视频”，都不在话下。
- **灵活的模型生态：** 内置 [LiteLLM](https://github.com/BerriAI/litellm) 统一路由。Gemini（推荐，免费额度充沛/视觉强）、Claude、GPT-4o 等主流模型均可一键切换。
- **评论区即服务：** 开箱即用的评论区自动化回复能力，不仅能回答你的首次提问，还支持”楼中楼”无缝追问。

## 它到底能做什么？

普通的 AI 总结只能告诉你“视频讲了啥”，但 BiliInsight 因为工具箱的存在，甚至能做到“跨平台侦查”：

| 你的问题示例 | Agent 实际执行的动作链 |
| :--- | :--- |
| **“这视频太长了，一句话总结”** | 获取基础 Metadata ➡️ 拉取字幕 ➡️ 提炼核心观点总结 |
| **“3:20 画面里 UP 主拿的是什么？”** | 定位 3:20 ➡️ 获取关键帧截图 ➡️ 并行调用视觉模型分析 |
| **“为什么满屏弹幕都在刷这句？”** | 拉取视频原始弹幕 ➡️ 高频词/情绪分析 ➡️ Google/X搜索该梗的来历 |
| **“评价一下我最近看的这些视频”** | 分析你的 300 条 B 站浏览历史 ➡️ 按题材归类 ➡️ 生成超硬核的个人洞察（见 Demo） |
| **“帮我找几期类似这样的测评”** | 提取该视频核心关键词 ➡️ 调用 B 站搜索 API ➡️ 获取数据 ➡️ 自动建立并分享收藏夹 |


## 快速开始

### 1. 自动安装脚本 (Ubuntu / Debian 推荐)
最纯粹的体验方式，一键安装所有依赖并交互式引导：
```bash
bash <(curl -fsSL https://raw.githubusercontent.com/Shanoa2/BiliInsight/main/install.sh)
```
> *注：脚本会自动拉取代码、配置虚拟环境、引导输入必要的信息（如 B 站登录、各种 API Key），并自动创建 systemd 后台服务。*

### 2. 手动构建安装
对于想二次开发或在其他系统部署的开发者：
```bash
# 1. 克隆并进入目录
git clone https://github.com/Shanoa2/BiliInsight.git
cd BiliInsight

# 2. 创建虚拟环境并安装核心依赖
python -m venv .venv && source .venv/bin/activate
pip install -e .
pip install git+https://github.com/anthropics/claude-agent-sdk-python.git

# 3. 进行交互式配置
python configure.py

# 4. 运行
python -m bilichat           # 启动 CLI 本地交互模式
python -m bilichat.bot       # 启动 B 站评论区监听机器人
```

## 模型与 API Key 配置指南

在执行 `python configure.py` 时，你会被要求分配各种模型与 Key：

**核心 LLM 提供商（任选其一作为主脑）：**
- **Gemini** (首推)：提供强大逻辑运算的同时拥有极其优秀的图像解析能力，且目前免费额度非常香。
- **Claude**：推理与工具调用能力顶级。
- **其他 API**：如 OpenAI (GPT-4o) / DeepSeek 等 OpenAI 兼容模型。

**高级能力扩充包（可选 API Key，高度建议配置）：**
* `GEMINI_API_KEY`：即使主模型不用 Gemini，也强烈建议配置，专职解决所有“画面分析”与 Google 搜索。
* `OPENAI_API_KEY`：用于将海量长字幕进行 Embedding，支持语义搜索定位关键内容。
* `XAI_API_KEY` / `SERPAPI_API_KEY`：解锁全网实时梗搜索与反向人物以图搜图。

## 目录结构

本项目核心逻辑非常清晰，方便二次开发，主要目录结构如下：
```text
src/bilichat/
├── app.py              # Agent 交互主入口 / System Prompts / 底层工具注册
├── config.py           # 配置与环境变量管理
├── tools/              # 30+ MCP 工具集（项目灵魂）
│   ├── subtitle.py     # 字幕获取与语义向量检索
│   ├── visual.py       # 智能抽帧、拼图与 Gemini 视觉透传
│   ├── ocr.py          # 视音频 OCR 解析提取
│   ├── danmaku.py      # 原始弹幕流的捕获与降噪
│   └── ...             # 其他工具（Google 搜图、X 推文检索等）
├── services/           # 三方平台接口（BApi、GeminiSDK 等）
└── bot/                # 承载在 B 站的评论区监听守护进程
```

## 后续计划

- [ ] 提供无门槛的独立网页交互端
- [ ] 可视化的 Web 配置管理后台 (取代现有的 CLI 配置)
- [ ] 跨平台的桌面客户端级体验
- [ ] 更加细腻的 UP 主视频评论区自动化高赞回复分析
- [ ] 背景 BGM 与音源轨度的分离深度识别

## License
本项目采用 [GNU General Public License v3.0](LICENSE) 授权。
由于项目依赖 `bilibili-api-python`，仓库整体按 `GPL-3.0` 发布。
欢迎提交 PR 和 Issues。如果觉得有用，给个 Star 就是最大的支持。
