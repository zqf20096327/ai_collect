# stepfun-vision-skill

![License](https://img.shields.io/badge/license-MIT-green.svg)
![Node](https://img.shields.io/badge/node-%3E%3D18-blue.svg)
![Model](https://img.shields.io/badge/model-step--3.7--flash-blueviolet)
![Codex](https://img.shields.io/badge/Codex-Skill-orange)

给 **纯文本主模型（如 Codex 接入的 DeepSeek `deepseek-v4-flash`）** 外挂“看图”能力的 Codex Skill：
当主模型不支持图片输入时，把图片交给 **StepFun `step-3.7-flash`（原生多模态推理模型）** 转成文字描述，主模型再基于描述继续推理、写代码。

```
用户粘贴图片 / 本地图片 / 图片 URL
        │
        ▼
scripts/describe-image.js（零依赖 Node.js）
  1. 守卫：读 ~/.codex/config.toml，仅主模型为 deepseek-v4-* 时启用
  2. --latest：从 Codex 会话文件恢复用户粘贴的图片（base64 重建）
  3. 调 StepFun /v1/chat/completions（step-3.7-flash，OpenAI 兼容）
        │
        ▼
文字描述 → 返回给主模型继续干活
```

## 项目简介 / About

**为什么需要它？** 很多人把 Codex 接到 **DeepSeek（`deepseek-v4-flash` 等纯文本模型）** 上使用——便宜、快、中文好，但这类模型**不支持图片输入**：粘贴截图会显示 `image content omitted because you do not support image input`，看不了 UI 稿、报错截图、图表和白板照片。

**怎么解决？** 本 Skill 把图片交给 **StepFun `step-3.7-flash`**（原生多模态推理模型，OpenAI 兼容接口）转成精准的文字描述，再让 DeepSeek 基于描述继续推理、写代码、排障。视觉模型只负责“看”和“转录”，**结论仍由主模型得出**——成本低、接入快、不挑主模型。

**核心亮点：**

- 粘贴即用：自动从 Codex 会话文件恢复你粘贴的图片（`--latest`），无需手动保存
- 支持本地文件、图片 URL、多张图、带问题识别（OCR / 细节追问）
- 零依赖 Node.js；一键安装器自动把 key 写入 `config.json`，可选写入环境变量
- Provider 守卫：只在 DeepSeek 主模型下启用，避免误用浪费
- 推理模型适配：`reasoning_effort` 控制思考开销 + `content`/`reasoning` 回退，保证必出结果

**适用场景：** UI/前端还原、报错截图排查、设计稿评审、图表/白板转数据、票据/文档 OCR、网页截图分析等。

> **English**: *stepfun-vision-skill adds image understanding to text-only coding models (e.g. DeepSeek `deepseek-v4-flash` inside Codex) by relaying images to StepFun's natively multimodal `step-3.7-flash` model. The vision model transcribes/describes the image into text; the main model then reasons on that text. Zero-dependency Node.js, one-command installer, DeepSeek-only provider guard, and `--latest` recovery of pasted images from Codex session files.*

> 本仓库是 [deepseek-vision-skill](https://github.com/iuiaeng2005/deepseek-vision-skill)（MIT）的 StepFun 适配版：换了默认接口/模型，新增一键安装器（引导填 key 并写入配置文件/环境变量），并针对 `step-3.7-flash` 推理模型做了适配（`reasoning_effort`、`content`/`reasoning` 回退）。

## 特性

- **零依赖**：纯 Node.js（内置 fetch，Node ≥ 18，Codex 自带运行时即可）
- **`--latest`**：用户粘贴进 Codex 的图片（即使主模型从未收到），也能从 `~/.codex/sessions/*.jsonl` 里恢复并识别
- **本地文件 / 图片 URL / 多张图**：都支持
- **带问题识图**：`--prompt "这张报错截图说了什么？"` 让视觉模型按需描述
- **推理模型适配**：`reasoning_effort`（默认 low）+ `content` 空时回退 `reasoning`
- **Provider 守卫**：只在主模型是 `deepseek-v4-flash / deepseek-v4-pro` 时启用
- **跨平台**：macOS / Windows / Linux

## 安装（推荐：一键安装器）

```bash
git clone https://github.com/<你的用户名>/stepfun-vision-skill.git
cd stepfun-vision-skill
node scripts/install.js
```

安装器会引导你**粘贴 StepFun API Key**：

1. 自动把 `describe-image.js`、`SKILL.md` 等安装到 `~/.codex/skills/stepfun-vision-skill/`；
2. 把 key **写入 `~/.codex/skills/stepfun-vision-skill/config.json`**（权限 600，明文，仅本机）；
3. 询问是否**同时把 `VISION_API_KEY` 追加到 `~/.zshrc` / `~/.bashrc`**（可选，环境变量优先级高于 config.json）；
4. 如果之前装过旧版 `deepseek-vision-skill`，会自动迁移旧 key。

非交互式安装：

```bash
node scripts/install.js --key SK-你的StepFun密钥            # 只写 config.json
node scripts/install.js --key SK-你的StepFun密钥 --env      # 同时写 shell 环境变量
```

> ⚠️ key 只会被写到本机的 `config.json` / shell 配置里，**不会写入本仓库**（仓库里只有占位符 `config.example.json`，且 `.gitignore` 已忽略 `config.json`）。

安装完成后：**重启 Codex**，并确保 `~/.codex/config.toml` 允许沙箱联网：

```toml
[sandbox_workspace_write]
network_access = true
```

## 配置

### 方式 A：config.json（推荐）

编辑 `~/.codex/skills/stepfun-vision-skill/config.json`：

```json
{
  "api_key": "SK-你的StepFun密钥",
  "endpoint": "https://api.stepfun.com/v1/chat/completions",
  "model": "step-3.7-flash",
  "allowed_models": ["deepseek-v4-flash", "deepseek-v4-pro"],
  "reasoning_effort": "low",
  "timeout_ms": 90000
}
```

### 方式 B：环境变量（可选覆盖，优先级最高）

| 变量 | 说明 |
|---|---|
| `VISION_API_KEY` | API key（优先级最高） |
| `VISION_API_ENDPOINT` | 接口地址，默认 `https://api.stepfun.com/v1/chat/completions` |
| `VISION_API_MODEL` | 模型，默认 `step-3.7-flash` |
| `VISION_API_TIMEOUT_MS` | 超时，默认 90000 |
| `VISION_REASONING_EFFORT` | `low` / `medium` / `high`，默认 `low` |
| `VISION_ALLOWED_MODELS` | 逗号分隔的守卫白名单 |
| `VISION_CONFIG` | 指定 config.json 路径 |
| `VISION_CONFIG_TOML` | 指定 Codex config.toml 路径（测试用） |

## 使用

### 在 Codex 里（重启后自动生效）

- 直接**粘贴图片 / 发图片路径 / 发图片 URL** → 模型会自动调用脚本识别；
- 看到 “image content omitted because you do not support image input” → 用 `--latest` 恢复图片再答。

### 命令行

```bash
node ~/.codex/skills/stepfun-vision-skill/scripts/describe-image.js /path/to/image.png
node ~/.codex/skills/stepfun-vision-skill/scripts/describe-image.js /a.png /b.png --prompt "比较这两张图的差异"
node ~/.codex/skills/stepfun-vision-skill/scripts/describe-image.js --latest --prompt "截图里的报错信息是什么"
node ~/.codex/skills/stepfun-vision-skill/scripts/describe-image.js --url "https://example.com/img.png"
node ~/.codex/skills/stepfun-vision-skill/scripts/describe-image.js --help
```

## 测试

```bash
node tests/test.js          # 守卫/参数等离线测试（不联网）
node tests/test.js --live   # 真实调用 StepFun（需 config.json 或 VISION_API_KEY）
```

## 注意事项 / 边界

- 图片是“翻译成文字”再给主模型看的：**小字、精细布局会有损耗**；OCR 类需求建议用 `--prompt` 明确指出。
- 单图上限 **25 MB**（超 8 MB 会警告）。
- `step-3.7-flash` 是**推理模型**：识别结果会带思考过程（reasoning），脚本已做 `content` 回退处理。
- 守卫只在主模型为 `deepseek-v4-*` 时启用；切换其他主模型会自动禁用，避免浪费。
- 隐私：图片只发送给你配置的 StepFun 接口，本地不保存图片副本；`--latest` 仅从本机会话文件重建。
- 成本：按 StepFun 定价计费（输入 1.35 元/百万 token、输出 8.1 元/百万 token，缓存命中更便宜）。

## License

MIT，保留上游 [deepseek-vision-skill](https://github.com/iuiaeng2005/deepseek-vision-skill) 的版权声明（见 LICENSE）。
