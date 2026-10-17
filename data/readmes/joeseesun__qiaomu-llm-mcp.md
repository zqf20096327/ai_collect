# qiaomu-llm-mcp

> 把多个 LLM Provider、API Key、模型路由和多模型讨论统一成一个本地 MCP 网关。<br>
> A local MCP gateway that turns many LLM providers, API keys, routing rules, and multi-model discussions into one tool surface.

**中文** | [English](#english)

适合这些场景：

- 你同时使用 Z.ai Coding Plan、DeepSeek、OpenAI-compatible API、Anthropic-compatible API、Claude Code CLI 等多套模型。
- 你不想把 API Key 写进提示词、脚本或 Codex 配置里。
- 你希望在 Codex / Claude / 其他 MCP 客户端里用同一组工具完成：单模型调用、多模型对比、流水线、HeavySkill 式多轮讨论。
- 你需要让最强的主控模型主持讨论，而不是把全部判断交给某一个 Provider。

本项目是本地优先工具：Provider 注册表保存在 `~/.config/qiaomu-llm/registry.json`，密钥默认放在 macOS Keychain，MCP server 只暴露“密钥是否存在”，不会返回明文 Key。

## 你能得到什么

安装后，MCP 客户端会看到这些工具：

| 工具 | 作用 |
| --- | --- |
| `qllm_list_providers` | 列出本地配置的 Provider，并安全显示密钥状态 |
| `qllm_show_provider` | 查看单个 Provider 的非敏感配置 |
| `qllm_list_models` | 查看本地配置或远程 `/models` 返回的模型 |
| `qllm_route_task` | 不花 token，根据任务类型选择 Provider / Model |
| `qllm_chat` | 调用单个 Provider |
| `qllm_compare` | 用同一个问题对比多个 Provider |
| `qllm_pipeline` | 串联多个模型步骤完成任务 |
| `qllm_heavy_discuss` | 多视角、多模型讨论，可由模型或 Codex 主持 |
| `qllm_heavy_render` | 把 Codex 主持后的讨论渲染成 Markdown / HTML 报告 |
| `qllm_claude_code_*` | 通过 MCP 安全调用本机 Claude Code CLI |

## 推荐工作流

```text
用户问题
  |
  +-- qllm_route_task 选择模型
  |
  +-- qllm_chat / qllm_compare / qllm_pipeline
  |
  +-- 复杂议题: qllm_heavy_discuss
        |
        +-- 多模型独立给观点
        +-- Codex 或指定模型主持
        +-- qllm_heavy_render 输出 Markdown / HTML
```

这套设计的核心不是“多叫几个模型凑热闹”，而是让不同模型承担不同角色：快速模型做初稿，强推理模型做审查，写作模型做表达，Codex 作为当前工作区里的主持人整合上下文和行动方案。

## 快速开始

### 1. 准备环境

要求：

- macOS 或 Linux
- Python 3.10+
- 一个支持 MCP 的客户端，例如 Codex、Claude Desktop、Claude Code、Cursor 等
- 至少一个 LLM Provider 的 API Key

克隆项目：

```bash
git clone https://github.com/joeseesun/qiaomu-llm-mcp.git
cd qiaomu-llm-mcp
```

如果你还没有 GitHub 版本，也可以先在本地目录安装：

```bash
cd /path/to/qiaomu-llm-mcp
```

### 2. 安装 Python 依赖

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -U pip
.venv/bin/python -m pip install -e .
```

确认可执行文件存在：

```bash
test -x .venv/bin/qiaomu-llm-mcp && echo "qiaomu-llm-mcp installed"
.venv/bin/python -c "import qiaomu_llm_mcp; print(qiaomu_llm_mcp.__version__)"
```

MCP server 通常通过 stdio 被客户端启动。直接运行时它会等待 MCP 客户端消息，这是正常现象。

### 3. 创建 Provider 注册表

复制示例配置：

```bash
mkdir -p ~/.config/qiaomu-llm
cp examples/registry.example.json ~/.config/qiaomu-llm/registry.json
```

编辑 `~/.config/qiaomu-llm/registry.json`，保留你要用的 Provider，删除不用的 Provider。

示例中的 Z.ai Coding Plan 使用专用 Coding endpoint：

```json
{
  "base_url": "https://api.z.ai/api/coding/paas/v4",
  "default_model": "glm-5.2"
}
```

注意：Z.ai Coding Plan 要使用 `https://api.z.ai/api/coding/paas/v4`，不要误用通用 endpoint `https://api.z.ai/api/paas/v4`。

### 4. 把 API Key 放进 Keychain

推荐使用 Keychain，不要把明文 Key 写入配置文件。

Z.ai：

```bash
security add-generic-password -U \
  -s qiaomu-llm \
  -a zai-glm \
  -w "$ZAI_API_KEY"
```

DeepSeek：

```bash
security add-generic-password -U \
  -s qiaomu-llm \
  -a deepseek \
  -w "$DEEPSEEK_API_KEY"
```

Anthropic-compatible Provider：

```bash
security add-generic-password -U \
  -s qiaomu-llm \
  -a anthropic \
  -w "$ANTHROPIC_API_KEY"
```

注册表里对应写法：

```json
{
  "secret_ref": "keychain:qiaomu-llm/zai-glm"
}
```

也支持环境变量：

```json
{
  "secret_ref": "env:ZAI_API_KEY"
}
```

但公开仓库、团队配置和长期使用建议优先 Keychain。

## 接入 Codex

编辑 Codex 配置文件，例如 `~/.codex/config.toml`：

```toml
[mcp_servers.qiaomu-llm]
command = "/absolute/path/to/qiaomu-llm-mcp/.venv/bin/qiaomu-llm-mcp"
```

本机示例：

```toml
[mcp_servers.qiaomu-llm]
command = "/Users/joe/Documents/qiaomu-llm-mcp/.venv/bin/qiaomu-llm-mcp"
```

重启 Codex 后，应该可以看到 `qllm_*` 工具。

## 接入 Claude Desktop

编辑 Claude Desktop 的 MCP 配置：

```json
{
  "mcpServers": {
    "qiaomu-llm": {
      "command": "/absolute/path/to/qiaomu-llm-mcp/.venv/bin/qiaomu-llm-mcp"
    }
  }
}
```

重启客户端后，确认工具列表里出现 `qllm_list_providers`。

## 基础用法

### 查看 Provider

```json
{
  "params": {
    "response_format": "markdown"
  }
}
```

调用工具：`qllm_list_providers`

### 调用 Z.ai Coding Plan

```json
{
  "params": {
    "provider": "zai-glm",
    "model": "glm-5.2",
    "prompt": "Reply exactly: qiaomu-llm-mcp-ok",
    "thinking_type": "disabled",
    "max_tokens": 64
  }
}
```

调用工具：`qllm_chat`

### 对比多个模型

```json
{
  "params": {
    "prompt": "用三条原则解释如何开始一个可持续的冥想习惯。",
    "task_type": "writing",
    "providers": ["zai-glm", "deepseek", "aigocode-anthropic"],
    "max_providers": 3,
    "response_format": "markdown"
  }
}
```

调用工具：`qllm_compare`

### 多步骤流水线

```json
{
  "params": {
    "input": "写一个面向普通人的冥想 App 产品方向。",
    "steps": [
      {
        "name": "research",
        "task_type": "research",
        "instruction": "提出用户痛点、竞争差异和核心场景。"
      },
      {
        "name": "prd",
        "task_type": "writing",
        "instruction": "把上一步整理成结构化 PRD 摘要。"
      },
      {
        "name": "review",
        "task_type": "review",
        "instruction": "审查 PRD 摘要里的风险、遗漏和过度承诺。"
      }
    ],
    "response_format": "markdown"
  }
}
```

调用工具：`qllm_pipeline`

## HeavySkill 式讨论

### 由 Codex 主持

适合当前 Codex 已经掌握工作区、文件、用户偏好和上下文的场景。

```json
{
  "params": {
    "question": "一个普通人如何开始冥想，并长期坚持？",
    "mode": "deliberation",
    "k": 4,
    "host_mode": "codex",
    "write_report": true,
    "write_html": true
  }
}
```

调用工具：`qllm_heavy_discuss`

工具会返回：

- 多个模型的独立观点
- `host_prompt`
- 可选的 Markdown / HTML 初始报告

把 `host_prompt` 交给 Codex 综合后，再调用 `qllm_heavy_render` 输出最终报告。

### 由模型主持

适合想让某个强模型直接完成主持总结的场景。

```json
{
  "params": {
    "question": "如何设计一个隐私友好的冥想 App？",
    "mode": "deliberation",
    "k": 4,
    "providers": ["zai-glm", "deepseek", "aigocode-anthropic"],
    "host_mode": "model",
    "host_provider": "aigocode-anthropic",
    "rounds": 2,
    "write_report": true,
    "write_html": true
  }
}
```

## Claude Code CLI 工具

如果本机安装了 Claude Code CLI，本项目还提供 `qllm_claude_code_*` 工具。

常见用途：

- 查看 Claude Code 能力：`qllm_claude_code_capabilities`
- 查看可用模型别名和本地最近使用模型：`qllm_claude_code_models`
- 非交互调用 Claude Code：`qllm_claude_code_run`
- 查看 Claude Code session：`qllm_claude_code_sessions`

示例：用 Sonnet 4.6 写一首诗。

```json
{
  "params": {
    "cwd": "/Users/joe/Documents/智谱",
    "prompt": "请用中文写一首 12 行现代诗，只输出诗。",
    "model": "claude-sonnet-4-6",
    "tools": [],
    "user_facing": true,
    "timeout": 300
  }
}
```

默认不会暴露 `--dangerously-skip-permissions`。需要文件编辑时，请显式设置 `allowed_tools`，并限制 `cwd`。

## 安全与隐私边界

- API Key 不应该写进 README、Prompt、Git 仓库或 MCP 请求参数。
- 推荐使用 `keychain:<service>/<account>`；工具只返回密钥状态，不返回明文。
- Provider 错误信息会做敏感字段脱敏，但上游服务返回的文本仍应谨慎处理。
- `qllm_claude_code_run` 是本机命令执行边界，默认只允许 `Read`，需要编辑或 Shell 时必须显式放开。
- HeavySkill 报告可能包含你的问题、模型输出和上下文摘要。公开分享前请人工检查。
- 本项目不会提供云端代理服务，也不会替你保存 API Key。

## 故障排查

### 看不到 MCP 工具

确认 MCP 配置中的 `command` 是绝对路径：

```bash
ls -la /absolute/path/to/qiaomu-llm-mcp/.venv/bin/qiaomu-llm-mcp
```

然后重启 MCP 客户端。

### `Registry not found`

创建注册表：

```bash
mkdir -p ~/.config/qiaomu-llm
cp examples/registry.example.json ~/.config/qiaomu-llm/registry.json
```

或设置环境变量：

```bash
export QIAOMU_LLM_REGISTRY=/path/to/registry.json
```

### `Missing Keychain secret`

检查服务名和账号是否一致：

```bash
security find-generic-password -s qiaomu-llm -a zai-glm -w
```

如果没有，重新写入：

```bash
security add-generic-password -U -s qiaomu-llm -a zai-glm -w "$ZAI_API_KEY"
```

### Z.ai Coding Plan 请求失败

检查三件事：

1. `base_url` 是否是 `https://api.z.ai/api/coding/paas/v4`
2. `model` 是否是你的 Coding Plan 可用模型，例如 `glm-5.2`
3. Keychain 中的 `zai-glm` 是否写入了正确 API Key

### 模型列表为空

有些 Provider 的 `/models` endpoint 不可用，或账号不开放模型枚举。可以在 `registry.json` 里手动写 `models` 和 `default_model`。

## 本地验证

开发者可运行：

```bash
.venv/bin/python -m compileall src
.venv/bin/python -m pip install -e .
```

如果配置了真实 Provider，可在 MCP 客户端中运行：

```json
{
  "params": {
    "provider": "zai-glm",
    "model": "glm-5.2",
    "prompt": "Reply exactly: ok",
    "max_tokens": 16
  }
}
```

## 路线图

- 可选 `aisuite` adapter：当目标 Provider 覆盖足够稳定时再加入，不影响 Z.ai Coding Plan 专用 endpoint。
- 更完整的安装 smoke test 脚本。
- Provider preset 管理命令。
- 报告模板主题和更多 HTML 输出样式。
- 更细粒度的成本、token 和超时预算策略。

## GitHub 发布

发布前的 GitHub About、topics、social preview 和验证清单见 [docs/github-publish-checklist.md](docs/github-publish-checklist.md)。

## 维护者

Copyright (c) 向阳乔木

- qiaomu.ai: https://qiaomu.ai
- Blog: https://blog.qiaomu.ai
- 推荐看: https://tuijian.qiaomu.ai
- X: https://x.com/vista8
- GitHub: https://github.com/joeseesun/
- 微信公众号：向阳乔木推荐看

## License

MIT License. See [LICENSE](LICENSE).

---

<a name="english"></a>

# English

`qiaomu-llm-mcp` is a local MCP gateway for people who use multiple LLM providers and want one safe tool surface for routing, comparison, pipelines, and multi-model deliberation.

It keeps provider metadata in `~/.config/qiaomu-llm/registry.json` and recommends storing secrets in macOS Keychain. The MCP tools expose secret status, not raw API keys.

## Why Use It

- One MCP server for many providers.
- Bring your own keys; no hosted proxy.
- Route tasks before spending tokens.
- Compare providers on the same prompt.
- Chain models into practical pipelines.
- Run HeavySkill-style discussions where multiple models produce independent views and Codex or a selected model hosts the synthesis.
- Optionally call local Claude Code CLI through a controlled MCP wrapper.

## Install

```bash
git clone https://github.com/joeseesun/qiaomu-llm-mcp.git
cd qiaomu-llm-mcp
python3 -m venv .venv
.venv/bin/python -m pip install -U pip
.venv/bin/python -m pip install -e .
```

## Configure Providers

```bash
mkdir -p ~/.config/qiaomu-llm
cp examples/registry.example.json ~/.config/qiaomu-llm/registry.json
```

Store secrets in Keychain:

```bash
security add-generic-password -U -s qiaomu-llm -a zai-glm -w "$ZAI_API_KEY"
```

For Z.ai Coding Plan, use the Coding endpoint:

```text
https://api.z.ai/api/coding/paas/v4
```

not the general endpoint:

```text
https://api.z.ai/api/paas/v4
```

## Codex MCP Config

```toml
[mcp_servers.qiaomu-llm]
command = "/absolute/path/to/qiaomu-llm-mcp/.venv/bin/qiaomu-llm-mcp"
```

Restart Codex and look for `qllm_*` tools.

## Example Tools

- `qllm_list_providers`: list configured providers and secret status.
- `qllm_chat`: call one provider.
- `qllm_compare`: compare several providers.
- `qllm_pipeline`: run sequential model steps.
- `qllm_heavy_discuss`: run multi-model deliberation.
- `qllm_heavy_render`: render Codex-hosted synthesis to Markdown / HTML.
- `qllm_claude_code_run`: run a bounded non-interactive Claude Code task.

## Security Notes

- Do not commit API keys.
- Prefer Keychain refs such as `keychain:qiaomu-llm/zai-glm`.
- Review generated HeavySkill reports before sharing them publicly.
- Grant Claude Code file-editing or shell permissions only when the task needs them.

## Verification

```bash
.venv/bin/python -m compileall src
.venv/bin/python -m pip install -e .
```

Then call `qllm_list_providers` from your MCP client.

## Maintainer

Created and maintained by 向阳乔木.

- X: https://x.com/vista8
- GitHub: https://github.com/joeseesun/

MIT License. See [LICENSE](LICENSE).
