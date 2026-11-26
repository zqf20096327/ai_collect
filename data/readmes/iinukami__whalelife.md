# WhaleLife

**同一个「它」，延续的经历，逐渐生长的能力。**

简体中文 · [English](README.en.md)

WhaleLife 是以**自我的连续性**为核心、本地运行的 AI 伙伴框架。主干承载人格、会话与记忆，插件让同一个主体获得新的交流、感知和行动方式。

[开始使用](#开始使用) · [插件目录](market/README.md) · [使用指南](architecture/USAGE.md) · [交流与参与](#交流与参与)

![WhaleLife：人格、会话与记忆连接不同渠道和插件能力](architecture/assets/conversation-continuity.svg)

## 一个主体，许多种能力

你在 QQ 上和它聊过的事，回到网页后可以接着聊；给它装上浏览网页、查看图片或主动行动的插件，它就有了新的能力。这些能力围绕同一份人格与所选会话工作，插件也可以把实际发生的经历记录下来，供之后的交流延续。

这也是 WhaleLife 想保留的一致感：能力逐渐增加，过去的经历仍有来处，新的交流能接得上。

- **交流有延续。** 网页与渠道插件绑定同一会话时，共用这份历史；渠道按配置使用人格。切换人格不会自动新建会话。
- **能力可以生长。** 通过插件商店安装所需能力，在控制台管理配置与启停；主动唤醒和行动由自主性插件提供。
- **记忆可以查看和管理。** 原始记录保留在本机。自动整理为日记默认关闭，需要时按上下文占用比例开启；有效日记替代对应原文进入模型上下文，原文仍可查阅。

跨渠道延续需要安装相应插件并使用**同一会话**。不同会话默认独立；模型可用的上下文受所选模型容量限制。图中内容为示意，具体能力取决于已安装插件及其配置。[记忆机制](architecture/MEMORY.md)

## 开始使用

需要自行配置可用的模型服务。支持云端或本地的 OpenAI 兼容接口，模型与服务需支持所用的对话和工具调用能力；云端 API 费用由服务商收取。

### 新手推荐：让 DSH 帮你安装

1. 从 [DeepSeek 官网](https://www.deepseek.com/download/) 下载并安装 **DeepSeek Harness（DSH）桌面版**。
2. 配置好 DSH 后，新建对话，把下面这段话发给它：

   ```text
   请帮我安装 WhaleLife，只装主干。项目地址是 https://github.com/iinukami/whalelife 。装好后帮我启动，把控制台的网址发给我。
   ```

安装后，在控制台的「模型服务」添加模型，在「使用配置」选择模型与人格，然后打开「对话」。可以从默认人格「鲸鲸」开始，也可以新建自己的人格。

<details>
<summary>手动安装（Node.js 24 或更新版本）</summary>

### 手动安装

1. 下载本仓库源码，安装 Node.js 24 或更新版本，用 `node --version` 确认版本。
2. 在项目目录打开终端，执行 `npm ci`。
3. 首次安装时创建 `config` 文件夹，将 `config.example.json` 复制为 `config/config.json`。升级已有安装时保留原配置。
4. 执行 `npm start`；Windows 也可双击 `start.bat`。打开 [本地控制台](http://127.0.0.1:9270)。
5. 添加模型、选择人格，开始第一段对话。终端中按 `Ctrl+C` 退出。

首次启动会初始化记忆目录和缺失的默认人格文件。局域网访问、模型设置和日常操作见[使用指南](architecture/USAGE.md)。

</details>

## 插件

在「概览」或「插件管理」打开**插件商店**，浏览官方与社区插件，查看依赖后安装。各插件独立维护；平台账号、外部服务和运行条件以各自说明为准。

| 为它增加的能力 | 插件 |
| --- | --- |
| 在 QQ 延续交流、浏览 QQ 空间 | [QQ](https://github.com/iinukami/whalelife-plugin-qq) · [QQ 空间](https://github.com/iinukami/whalelife-plugin-qzone) |
| 形成意图，按配置主动调用能力 | [自主性](https://github.com/iinukami/whalelife-plugin-autonomy) |
| 搜索和阅读网页、浏览 B 站 | [网上冲浪](https://github.com/iinukami/whalelife-plugin-surf) · [B 站](https://github.com/iinukami/whalelife-plugin-bilibili) |
| 管理图片、理解视听内容 | [图库](https://github.com/iinukami/whalelife-plugin-gallery) · [视听理解](https://github.com/iinukami/whalelife-plugin-vision) |

QQ 空间依赖 QQ，B 站依赖网上冲浪。更多作品见[插件目录](market/README.md)；已启动本机服务时可[直接打开插件商店](http://127.0.0.1:9270/#market)。

## 更新 WhaleLife

在控制台「概览」点「检查更新」，阅读说明后选择「更新并重启」。插件在商店里单独检查更新。已有配置、人格和记忆会保留；升级前请留出备份空间。旧版本迁移、预检与回滚说明见[更新指南](architecture/USAGE.md#更新-whalelife)。

## 交流与参与

**交流 QQ 群：962935021** · [反馈问题](https://github.com/iinukami/whalelife/issues)

欢迎分享使用体验，也欢迎为这个持续成长的主体制作新的能力。开发前请先阅读[主干现状](architecture/STATUS.md)与[插件契约](architecture/PLUGINS.md)。

### 社区插件投稿与审核

把插件放在独立仓库，准备说明和发行包，再[提交收录申请](https://github.com/iinukami/whalelife/issues/new?template=submit-plugin.yml)。首次投稿、版本复审和图标要求统一见[社区插件指南](market/community-packages.md)。

## 进一步了解

[详细使用指南](architecture/USAGE.md) · [记忆系统](architecture/MEMORY.md) · [渠道接口](architecture/CHANNELS.md) · [开发规则](AGENTS.md) · [插件开发规则](plugins/AGENTS.md)
