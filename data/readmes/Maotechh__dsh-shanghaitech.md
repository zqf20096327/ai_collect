<div align="center">

# DSH ShanghaiTech

面向上海科技大学学生的 DeepSeek Harness 社区配置包

[![Verify](https://img.shields.io/github/actions/workflow/status/Maotechh/dsh-shanghaitech/ci.yml?branch=main&style=flat-square&label=verify)](https://github.com/Maotechh/dsh-shanghaitech/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-2f855a?style=flat-square)](LICENSE)
[![Node.js](https://img.shields.io/badge/Node.js-%E2%89%A522.19-339933?style=flat-square&logo=nodedotjs&logoColor=white)](package.json)
[![DSH](https://img.shields.io/badge/DSH-0.1.1--rc.2-111827?style=flat-square)](https://github.com/deepseek-ai/deepseek-harness)

</div>

它为官方 DSH Web profile 预先配置 ShanghaiTech GenAI Responses 接口、保守的上下文参数和 [`dsh-anchored-standard`](https://github.com/xiaobright/dsh-anchored-standard) preset。用户只需要自己向学校申请 API key，并在本机设置页填写。

> [!IMPORTANT]
> 本项目由社区维护，不是 DeepSeek 或上海科技大学官方项目。本项目不提供 API key，也不代表任何官方认可、背书或服务承诺。

![DSH 中的 ShanghaiTech GenAI 模型设置](assets/dsh-shanghaitech.png)

## 快速开始

需要 Node.js 22.19 或更新版本、Git，以及能够访问学校 GenAI 服务的网络环境。支持 Windows、macOS 和 Linux。

```sh
git clone https://github.com/Maotechh/dsh-shanghaitech.git
cd dsh-shanghaitech
node install.mjs
node run.mjs
```

首次运行时，`npx` 会下载固定版本的官方 DSH 及其依赖。浏览器打开后，进入 **Settings → Models**，编辑 **ShanghaiTech GenAI**，填写自己从学校申请的 API key，然后选择 **Apply**。

安装器不会询问、读取或写入 API key，也不会修改其他 profile 或会话。此后仍然使用下面的命令启动：

```sh
node run.mjs
```

## 已经准备好的内容

- 独立的 `shanghaitech` Web profile，不替换其他 DSH profile。
- ShanghaiTech GenAI 的 OpenAI Responses 配置，默认模型为 `deepseek-pro`。
- `131072` token 上下文容量和 `16384` token 单次输出上限。
- 固定提交的 `anchored-standard` preset，避免安装结果随上游仓库变化。
- 不读取凭据内容的安装检查命令：`node doctor.mjs`。
- 首次安装、覆盖安装和自定义 `DSH_HOME` 支持。

完整的固定版本和参数见[配置说明](docs/configuration.md)。

## 使用说明

| 需要做什么 | 文档 |
| --- | --- |
| 了解 profile、模型参数和凭据保存位置 | [配置说明](docs/configuration.md) |
| 处理连接失败、上下文错误和 Responses stream 错误 | [故障排查](docs/troubleshooting.md) |
| 更新本项目、DSH 或 preset | [升级说明](docs/upgrading.md) |
| 参与维护或提交修改 | [贡献指南](CONTRIBUTING.md) |
| 报告安全问题 | [安全政策](SECURITY.md) |

运行入口会把后续参数原样传给固定版本的 DSH，例如：

```sh
node run.mjs --help
```

发现 DSH 本身的问题，请前往 [DeepSeek Harness Discussions](https://github.com/deepseek-ai/deepseek-harness/discussions)。发现本仓库的安装或配置问题，请[创建 Issue](https://github.com/Maotechh/dsh-shanghaitech/issues/new/choose)，但不要附带 API key、会话文件或私有代码。

## License

本仓库使用 [MIT License](LICENSE)。DeepSeek Harness 和第三方依赖使用各自的上游许可证，详细来源见 [NOTICE](NOTICE)。
