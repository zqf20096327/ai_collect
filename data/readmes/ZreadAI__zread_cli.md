# Zread CLI

> 用 AI 把代码变成文档，一条命令搞定。

Zread 是一款命令行工具，通过 AI 大模型自动分析代码仓库，生成结构化的 Wiki 文档，并提供内置阅读器供团队随时查阅。

---

## 安装

### Homebrew (支持 macOS / Linux)

```bash
brew tap ZreadAI/homebrew-tap
brew install zread
```

升级：

```bash
brew upgrade zread
```

### npm (支持 Windows / Linux / macOS)

```bash
npm install -g zread_cli
```

升级：

```bash
npm update -g zread_cli
```

### winget (支持 Windows 10/11)

```shell
winget install ZhipuAI.Zread
```

升级：

```shell
winget upgrade ZhipuAI.Zread
```


### 直接下载

从 [Releases](https://github.com/codegeex/zread_cli/releases) 页面下载对应平台的预编译二进制文件，解压后放入 `PATH` 即可。

支持平台：macOS（x86_64 / ARM64）、Linux（x86_64 / AArch64）、Windows（x64 / ARM64）

---

## 快速上手

安装后在您需要分析的项目代码目录下运行 
```bash
zread
```

zread cli 会带你进入 onboarding 流程并完成项目分析。

---

## 命令速览

| 命令 | 说明 |
|------|------|
| `zread login` | 登录订阅账号，自动获取 API Key |
| `zread config` | 配置 LLM 提供商、语言等选项 |
| `zread generate` | 为当前项目生成文档 |
| `zread browse` | 在浏览器中阅读已生成的文档 |
| `zread update` | 更新 Zread 到最新版本 |
| `zread version` | 查看当前版本信息 |

---

## 配置说明

配置文件位于 `~/.zread/config.yaml`，通过 `zread config` 交互式编辑，主要选项：

| 选项 | 说明 |
|------|------|
| 界面语言 | `en`（英文）或 `zh`（中文） |
| 文档语言 | 生成内容使用的语言，留空时跟随界面语言 |
| LLM 提供商 | 选择内置提供商或填入自定义 BaseURL |
| 最大并发数 | 同时生成的页面数，建议 2–5 |
| 最大重试次数 | 页面生成失败时的自动重试次数 |

### 支持的内置提供商

| 提供商 | 说明 |
|--------|------|
| 智谱 Coding Plan | 订阅账号专属，无需自备 Key（CN） |
| Z.AI Coding Plan | 订阅账号专属，无需自备 Key（海外） |
| 智谱 BigModel | 订阅账号专属，无需自备 Key（CN） |
| Z.AI | 订阅账号专属，无需自备 Key（海外） |
| OpenAI | 自备 Key |
| MoonShot | 自备 Key |
| MiniMax | 自备 Key |
| OpenRouter | 自备 Key，可接入多种模型 |

也可填入任意兼容 OpenAI 接口的自定义 BaseURL。

---

## 常见问题

**生成过程中断了，可以续写吗？**

可以。再次运行 `zread generate`，选择"续写草稿"即可从中断处继续，已完成的页面不会重复生成。

**文档存在哪里？会上传到云端吗？**

文档保存在项目目录的 `.zread/wiki/` 下，完全本地存储，不会上传到任何服务器。

**支持哪些编程语言？**

Zread 通过 AI 理解代码语义，理论上支持任何编程语言，实际效果取决于所用模型的代码理解能力。

**如何查看历史版本文档？**

每次生成会保留历史版本。运行 `zread browse --version` 打开版本选择器。

---

## 反馈与支持

- 官网：[https://zread.ai](https://zread.ai)
