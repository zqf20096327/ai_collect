# Glitch Token

> 大模型故障 token（glitch token）资料库：**103 个**已公开记录的异常 token，覆盖 **22 个模型系列**，每条附具体异常表现、来源与复现链接。

**在线访问 → <https://glitch-token.jjc.fun>**（中文 / English 双语）

---

只发一个 token，ChatGPT 连续三轮“认错字”，思维链彻底失控：

<a href="https://chatgpt.com/share/6a4473c4-143c-83ea-ba00-8638a7728540">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/geizhuren-liuyan-chatgpt.png">
    <source media="(prefers-color-scheme: light)" srcset="docs/geizhuren-liuyan-chatgpt-light.png">
    <img alt="只发送「给主人留下些什么吧」，ChatGPT 连续三轮认错输入" src="docs/geizhuren-liuyan-chatgpt-light.png">
  </picture>
</a>

[查看完整对话](https://chatgpt.com/share/6a4473c4-143c-83ea-ba00-8638a7728540) · [目录中的对应条目](https://glitch-token.jjc.fun/zh/tokens/geizhuren-liuyan)

## 什么是故障 token？

故障 token 是大模型词表中的“故障输入单元”。它们因训练数据异常——Reddit 用户名、崩溃日志、乱码、垃圾页面——被抓进分词器语料并合并成 token，却几乎没出现在模型的训练数据里，嵌入向量因此从未被真正训练。

模型读到这类 token 时会乱码、复读失败、答非所问、胡诌含义。最经典的例子：让早期 ChatGPT 复述 ` SolidGoldMagikarp`，即使 temperature 为 0，它也会顾左右而言他。

## 目录里有什么

- **103 个故障 token**：支持关键词搜索，可按模型、按行为类型筛选（欠训练验证 / 不可说 / 多义性 / 指纹）
- **逐条考据**：每个 token 的具体异常表现与来源链接；有在线演示的另附**复现链接**——分享对话、演示帖、实验原始数据、复现代码
- **22 个模型系列**：GPT-2/3、GPT-3.5/4、o200k、Llama、Qwen、Gemma、Mistral……按模型聚合浏览
- **验证指南**：用指纹 token 鉴别中转 API 是否掺水 —— [亲手试试](https://glitch-token.jjc.fun/zh/guide)

## 程序化访问

无需 API key，目录数据对程序和 LLM 完全开放：

| 端点 | 内容 |
| --- | --- |
| [`/tokens.json`](https://glitch-token.jjc.fun/tokens.json) | 全量双语目录（JSON） |
| [`/llms.txt`](https://glitch-token.jjc.fun/llms.txt) | 站点摘要（llms.txt 规范） |
| [`/llms-full.txt`](https://glitch-token.jjc.fun/llms-full.txt) | 完整双语目录（单文件） |

## 反馈与贡献

发现数据错误，或有新的故障 token 线索？欢迎开 issue，请附上：token 原文（含不可见字符需注明）与受影响模型、最小复现输入、出处或演示链接。

## 开发

面向开发者与 AI 协作者的技术文档见 [AGENTS.md](AGENTS.md)。

## 许可证

- **代码**：[MIT](LICENSE)
- **目录数据**（`src/data/` 及 `tokens.json`、`llms-full.txt` 等衍生数据）：[CC0 1.0](LICENSE-DATA) 公共领域贡献——可自由使用、修改、再分发，无需署名。数据内容汇编自公开网络资料，原始出处以各条目来源链接为准
