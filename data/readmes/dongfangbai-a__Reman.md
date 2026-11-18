<p align="center">
  <img src="docs/logo.png" width="96" alt="Reman">
</p>

<h1 align="center">Reman</h1>

<p align="center">
  <a href="https://github.com/dongfangbai-a/Reman/actions/workflows/ci.yml"><img src="https://github.com/dongfangbai-a/Reman/actions/workflows/ci.yml/badge.svg?branch=main" alt="CI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT"></a>
  <a href="https://github.com/dongfangbai-a/Reman/releases"><img src="https://img.shields.io/github/v/release/dongfangbai-a/Reman" alt="Release"></a>
</p>

直观高效的 AI 协作运行时。打开网页即可开始协作，过程一眼可见；同样的任务，跑得更快、花得更少。

## 界面

![成员页：左边是成员列表，中间是成员的完整时间线——计划、命令、文件改动、测试结果和汇报，右边是计划和运行概况](docs/screenshots/members.webp)

![群聊：多个成员在一个群里轮流发言、互相 @，右边是计划和运行概况](docs/screenshots/group-chat.webp)

## 快速开始

```bash
git clone https://github.com/dongfangbai-a/Reman.git
cd Reman
npm install            # 运行时的依赖
npm run web:install    # 网页端的依赖
npm run web:build      # 构建网页端
npm start              # 默认 127.0.0.1:6001，--port 可改
```

打开运行时启动时打印的链接（`http://127.0.0.1:6001/#token=…`）一次，浏览器就记住了登录（令牌换成 Cookie），
之后直接打开 `http://127.0.0.1:6001/` 即可。

数据目录默认在系统用户目录下，`--data-dir` 可改；一个数据目录同一时间只能有一个运行时在用。
位置、里面有什么、各项怎么配，见 [CONFIG.md](CONFIG.md)。

运行时只监听本机。一旦要从别处访问——局域网、Tailscale、Cloudflare 隧道这些——**访问令牌就等于运行运行时的那个系统用户的完整权限**（能开终端、执行命令、改文件），谁拿到令牌谁就有这份权限。详见 [CONFIG.md](CONFIG.md) 的「安全」。

## 项目概况

Reman 的前身是一个更早的实验性项目；那个项目里有一条没有走通的思路（一个成员多条并行上下文），复盘和遗留问题见 [PARALLEL_CONTEXT.md](PARALLEL_CONTEXT.md)。

Reman 的开发从 10 月 31 日开始，功能开发在 11 月 11 日停止，前后 12 天。这么短，一方面是因为很多设计直接取自那个实验性项目，需要从零设计的部分不多，另一方面是写代码有 AI 辅助，实现速度快。之后 4 天主要做整理，以及和几个 agent 脚手架的基准对比（见 [BENCHMARKS.md](BENCHMARKS.md)）。

所以它还很初期：主要功能能跑通，自己用下来效果不错，但边界情况、文档和工程细节都还有不少要补的地方。欢迎一起迭代维护。

## 交流

- QQ 群：1136460980
- 微信群：扫下面的码加入（11 月 23 日前有效）

<img src="docs/screenshots/wechat-group.png" width="240" alt="Reman 微信交流群二维码">

## 文档

| 文档 | 内容 |
|---|---|
| [NOTES.md](NOTES.md) | 成员、终端、沙箱、工具、外部事件、公网访问的机制和使用建议 |
| [API.md](API.md) | HTTP 接口和事件流 |
| [CONFIG.md](CONFIG.md) | 配置文件和数据目录 |
| [DEVELOPMENT.md](DEVELOPMENT.md) | 开发：检查和测试、开发脚本、表结构、性能 |
| [BENCHMARKS.md](BENCHMARKS.md) | 基准测试：几个 agent 脚手架在同一个模型下的用时与花费 |
| [PARALLEL_CONTEXT.md](PARALLEL_CONTEXT.md) | 一个成员多条并行上下文的设想、没落地的原因和还没定论的问题 |

## 许可

MIT，见 [LICENSE](LICENSE)。参与开发见 [CONTRIBUTING.md](CONTRIBUTING.md)，报告安全问题见 [SECURITY.md](SECURITY.md)，随仓库分发的第三方组件见 [THIRD_PARTY.md](THIRD_PARTY.md)。
