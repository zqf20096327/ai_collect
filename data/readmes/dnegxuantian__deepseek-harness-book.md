# DeepSeek Harness：即插即用的实战指南

《DeepSeek Harness：即插即用的实战指南》是邓明瑞（纯粹 / Chuncui）整理的开发者社群共建指南。

书稿面向有基本开发经验、但还不熟悉 DeepSeek Harness 内部接口的读者。内容基于 DSH 0.1.1-rc.2 在 macOS 上整理，从一次任务开始，解释模型接入、工具调用、会话与上下文、执行环境、权限、任务循环、后台任务和界面事件，再带读者完成插件安装、修改、加载、卸载、失败复测与发布检查。

全书按七章组织：

1. 认识 DSH，完成第一次使用
2. DSH 核心原理，一次任务怎样运转
3. DSH 插件详解，从文件到运行
4. DSH 各层插件实战（含 4.1—4.14 十四个小节）
5. 社区插件实际体验
6. 常见问题与排查
7. 发布自己的插件

第 4 章的每个小节都对应第 2 章的扩展位置，读者可以从用途、实际使用、实现、修改和验证五个角度理解每个插件。书中会区分本机复测、社区报告和仍待验证的环境问题，具体插件、模型、权限和版本仍需按读者自己的环境检查。

## 阅读入口

- GitHub 内阅读全文：[`book/README.md`](book/README.md)
- 作品仓库：<https://github.com/dnegxuantian/deepseek-harness-book>
- 正式页面：<https://blog.chuncui.icu/deepseek-harness-book/>
- 配套练习下载：[`book/downloads/`](book/downloads/)
- 作者主页：<https://blog.chuncui.icu/about/>
- 社区共建记录：<https://github.com/deepseek-ai/deepseek-harness/discussions/1477>

## 公共发布边界

私有运行时、会话、凭据和内部路径不会随仓库复制；需要复现时，请以书中对应的公共示例和原始项目许可证为准。

这是开发者社群共建指南，不代表 DeepSeek 官方出版、认可或背书。

## 作者

邓明瑞，花名纯粹（Chuncui），数据中台与 AI Agent 工程化技术架构师，长期关注分布式系统、数据平台、模型网关、MCP、上下文工程与 Agent 的可验证执行。Clippy 衍生练习包目前暂不提供。
