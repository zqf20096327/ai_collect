<div align="center">
  <img src="icon.svg" width="88" alt="chat-in-dsh 图标" />
  <h1>chat-in-dsh</h1>
  <p><strong>在 DeepSeek Harness（DSH）里，用原汁原味的网页版对话。</strong></p>
  <p>
    <a href="https://www.npmjs.com/package/chat-in-dsh"><img alt="npm" src="https://img.shields.io/npm/v/chat-in-dsh?style=flat-square" /></a>
    <a href="https://github.com/YinkaiYu/chat-in-dsh/actions/workflows/test.yml"><img alt="Test" src="https://img.shields.io/github/actions/workflow/status/YinkaiYu/chat-in-dsh/test.yml?style=flat-square" /></a>
    <a href="https://github.com/YinkaiYu/chat-in-dsh/releases"><img alt="Release" src="https://img.shields.io/github/v/release/YinkaiYu/chat-in-dsh?style=flat-square" /></a>
    <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/github/license/YinkaiYu/chat-in-dsh?style=flat-square" /></a>
    <img alt="基于官方 chat-demo" src="https://img.shields.io/badge/%E5%9F%BA%E4%BA%8E-%E5%AE%98%E6%96%B9%20chat--demo-2F6FEB?style=flat-square" />
    <a href="https://github.com/deepseek-ai/deepseek-harness"><img alt="powered by dsh" src="https://img.shields.io/badge/powered_by-dsh-4D6BFE?style=flat-square&logo=deepseek&logoColor=white" /></a>
  </p>
</div>

<p align="center"><a href="README.en.md">English</a> · 简体中文</p>

## 为什么需要它

2026 年 11 月 16 日，DeepSeek App 和网页端开始限额，不少用户因此转到 DeepSeek Harness。这部分用户需要的是聊天、写作、问答，而 DSH 默认是给开发者准备的形态：每次对话内置了几千字的系统提示词和工具注入，于是，模型变成了一个「老实」的打工人，却失去了原本网页版对话的那种「灵气」。写作和聊天时，这个差别尤为明显。

本插件在 DSH 里加一个独立面板，面板里就是原汁原味的 DeepSeek 网页版本身：官方极简系统提示词、官方的服务端工具、官方界面。在这小小的一方天地，只有 DeepSeek，没有 Harness，它不再被工具束缚，也不再有限额（通过API计费），它与你之间不再有可悲的厚障壁。

## 你能得到什么

- **原汁原味**：界面就是 DeepSeek 官方开源的那份前端，交互、排版、动效都按官网复刻
- **不用填 API Key**：直接用 DSH 里已经登录的 DeepSeek 账户
- **不受官网限额影响**：请求走 API
- **能力齐全**：智能搜索、深度思考、引用角标、公式、图表、深色模式
- **独立面板**：有自己的会话列表，和 DSH 的会话分开管理、互不同步

<img src="docs/assets/webview-reply.png" width="760" alt="对话与思考过程">

## 安装

**1. 打开左侧的「插件」页**

<img src="docs/assets/dsh-1.png" width="760" alt="打开插件页">

**2. 点右上角的「添加插件」**

<img src="docs/assets/dsh-2.png" width="760" alt="点添加插件">

**3. 填包名 `chat-in-dsh`（或粘贴仓库地址），点「安装」**

<img src="docs/assets/dsh-3.png" width="760" alt="填写包名并安装">

**4. 装好后点「立即启用」**

<img src="docs/assets/dsh-4.png" width="760" alt="点立即启用">

之后左侧面板列表里会多出「网页版」。

## 使用

点左侧面板列表里的「网页版」：

<img src="docs/assets/dsh-5.png" width="760" alt="点网页版打开面板">

如果想专心聊天，点左上角这个按钮把 DSH 的会话栏收起来：

<img src="docs/assets/dsh-6.png" width="760" alt="收起 DSH 会话栏">

收起之后就是完整的网页版界面：

<img src="docs/assets/dsh-7.png" width="760" alt="网页版面板">

面板里有自己的会话列表，和 DSH 的会话分开管理。

## 把对话搬进来

**从 DeepSeek 官网搬**

1. 打开 chat.deepseek.com，点「设置 → 数据管理 → 导出所有历史对话」，下载生成的 ZIP（文件名形如 `deepseek_data-2026xxxx.zip`）。
2. 在面板左下角点「设置」→「数据管理」→「导入历史对话」，选中这个 ZIP。

这个入口会覆盖面板里现有的全部对话，建议先把要导入的导完，再开始新的对话。

**从 DSH 搬**

在左侧会话列表里右键任意一条 →「导入到网页版」，那份对话会复制一份进来，之后两边各自独立。

## 关于可靠性

这个插件基于 DeepSeek 官方开源的 [chat-demo](https://github.com/deepseek-ai/chat-demo) 开发。请求发往哪里、左上角的标识、藏起 API Key 输入框是为接入 DSH 所做的改动；其余界面与交互按官网逐项复刻。

官方 chat-demo 只是网页版的骨架：界面在，但网页版里不少已有的交互它没有做。我们在它之上把这些补齐，让它更接近 chat.deepseek.com 本身：

- 会话搜索：按标题、正文、思考过程和附件名检索；命中标题单独成行，消息命中带分支序号
- 右侧轮次进度条：每条提问一根刻度，悬停展开预览，点击跳到对应轮次
- 会话置顶与多选批量管理：置顶、取消置顶、删除，和网页版一致的入口与确认框
- 长文本粘贴转附件：超过 2000 字的纯文本转成附件卡片，可一键还原、支持撤销/重做
- 语音输入与朗读：网页版的录音、转写和朗读路径
- 长回答阅读：代码块工具栏吸顶、回到最新按钮、Mermaid 图表缩放
- 深色模式、公式、图表等界面细节按官网样式对齐

没有二次包装，也没有替你「优化」提示词——模型拿到的就是网页上那一份。
