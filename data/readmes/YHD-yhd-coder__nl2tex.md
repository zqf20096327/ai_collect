# nl2tex

用一句中文（或英文）描述一个公式，得到**能直接编译**的 LaTeX。

不是聊天机器人，是一个只做一件事的转写工具：**只转写，不计算、不化简、不猜**。描述有歧义时，它会给出低置信度和说明，而不是编一个看起来合理的答案。

```
输入：求 k 从 1 到 n 的 k 平方
输出：\sum_{k=1}^{n} k^{2}
```

![演示](docs/demo.gif)

## 启动不了？先看这里

**症状：双击 `start.cmd` 黑窗口一闪而过，或者报一堆 `'�' is not recognized`。**

九成是这两个原因：

| 原因 | 表现 | 解决 |
|---|---|---|
| **没解压，直接在 zip 预览里双击** | 提示找不到 `node.exe`，或窗口一闪就没 | 右键 zip → **全部解压**，再到解压出来的文件夹里双击 `start.cmd` |
| **Windows 拦截了下载的 exe** | 双击后没反应，或提示"已保护你的电脑" | 右键 zip → 属性 → 勾选 **解除锁定（Unblock）** → 确定，再解压 |

其它情况：

- **端口被占用**：关掉已经开着的 nl2tex 窗口，或换端口 `set PORT=8788 && start.cmd`
- **杀毒软件隔离了 node.exe**：把解压目录加进白名单（node.exe 是官方 Node.js 运行时，95 MB）
- **打不开页面但窗口在**：手动在浏览器输入 `http://127.0.0.1:8777`

> v0.4.0 之前的包有个编码 bug：`start.cmd` 里的中文在 GBK 代码页下会被 cmd 解析错，导致启动失败。现在的包已改成纯 ASCII，请重新下载。

## 它解决什么问题

手写 LaTeX 的门槛不在语法，而在"想到那个符号叫什么"。你知道要写求和，但不确定是 `\sum_{k=1}^{n}` 还是 `\sum\limits_{k=1}^n`；你知道要写下标，但多字母下标忘了 `\mathrm{}`。nl2tex 让你用自然语言说，它负责翻成规范写法，并且**当场用 KaTeX 编译一遍**，编不过就带着错误信息重试。

## 特性

- **编译校验**：每条结果都过 KaTeX，失败自动带错误重试一次，不会给你一段贴进去就报错的代码
- **歧义显式化**：`confidence` + `note`，低于 0.6 会告诉你它在哪猜了，并给出最多 3 个候选解读
- **图片识别**：直接 `Ctrl+V` 粘贴公式截图，或选图片，走同一个模型（`deepseek-flash` 原生视觉）
- **多种导出**：LaTeX、`$...$`、MathML、Word 公式（OMML）
- **六个学科**：数学 / 物理 / 化学 / 计算机 / 经济统计 / 生物，各有专属规则（化学强制 `\ce{}`、物理带单位写法等）
- **两种鉴权**：在页面里填自己的 DeepSeek API Key（推荐），或用环境变量；本机登录过 DSH 的话也能直接复用账号
- **多家供应商**：DeepSeek / Kimi / 智谱 / 通义千问 / SiliconFlow / OpenRouter，或任何 OpenAI 兼容网关
- **本地优先**：只监听 `127.0.0.1`，公式不出本机（除了发给模型）
- **零构建**：纯 ESM + 原生 Node，`git clone` 完就能跑

## 快速开始

需要 Node ≥ 20。

**Windows**：双击 `start.cmd` —— 自动装依赖、启动服务、打开浏览器。

**macOS / Linux**：

```bash
git clone https://github.com/YHD-yhd-coder/nl2tex.git && cd nl2tex
./start.sh
```

也可以手动：

```bash
npm install        # 或 pnpm install
npm start          # 打开 http://127.0.0.1:8777
```

第一次打开后，点右上角 **设置** → 选一个供应商 → 填自己的 API Key → 保存。Key 只存在本机浏览器 `localStorage`，请求只发给本机后端。

**费用自己承担**：DeepSeek 单次约 ¥0.001，充 ¥10 够用几千次。

## 支持的模型供应商

页面里直接选，预设都填好了 base URL 和模型名，只需要填 Key：

| 供应商 | 协议 | 默认模型 | Key 申请 |
|---|---|---|---|
| **DeepSeek** | Anthropic | `deepseek-flash` | [platform.deepseek.com](https://platform.deepseek.com/api_keys) |
| **Kimi（月之暗面）** | OpenAI 兼容 | `kimi-k2.6` | [platform.kimi.ai](https://platform.kimi.ai) |
| **智谱 GLM** | OpenAI 兼容 | `glm-4.6` | [open.bigmodel.cn](https://open.bigmodel.cn/usercenter/apikeys) |
| **通义千问** | OpenAI 兼容 | `qwen-plus` | [百炼控制台](https://bailian.console.aliyun.com/) |
| **SiliconFlow** | OpenAI 兼容 | `deepseek-ai/DeepSeek-V3` | [cloud.siliconflow.cn](https://cloud.siliconflow.cn/account/ak) |
| **OpenRouter** | OpenAI 兼容 | `deepseek/deepseek-chat` | [openrouter.ai](https://openrouter.ai/keys) |
| **自定义** | OpenAI 兼容 | 自己填 | 任何兼容网关 |

> **关于 WorkBuddy**：它开放平台提供的是 OAuth 授权 + 分享/deeplink 能力，**不是模型推理 API**，所以不能作为生成后端。如果以后想接，合理的方式是"生成完一键分享到 WorkBuddy"，而不是把它当模型。

> 图片识别要求模型支持视觉：DeepSeek `deepseek-flash` 支持；Kimi K3 支持；部分开源模型不支持，会返回错误。

> 本机登录过 DSH 的话，还有"本机 DSH 登录"选项，不用填 Key。但它依赖 DSH 的登录态文件，只适合本机自用，开源分发请让用户用自己的 Key。

## 命令行

```bash
node cli.mjs "积分从 0 到无穷 e 的负 x 平方 dx"
node cli.mjs "水的化学式" --subject=chemistry
node cli.mjs "牛顿第二定律" --json
```

## HTTP 接口

```http
POST /api/nl2tex
{ "text": "求和 1/n立方+nx", "subject": "math" }
```

返回：

```json
{
  "latex": "\\sum \\frac{1}{n^3+nx}",
  "valid": true,
  "confidence": 0.45,
  "note": "未给出求和上下限与求和变量……",
  "alternatives": [
    { "label": "推荐", "latex": "\\sum \\frac{1}{n^3+nx}" },
    { "label": "分拆为两项", "latex": "\\sum \\left(\\frac{1}{n^3}+nx\\right)" }
  ],
  "html": "<span class=\"katex\">…</span>",
  "usage": { "input_tokens": 244, "output_tokens": 72 },
  "ms": 1928
}
```

图片识别：

```http
POST /api/ocr
{ "image": "<base64 或 dataURL>", "mediaType": "image/png", "subject": "math" }
```

导出：

```http
POST /api/export
{ "latex": "\\frac{a}{b}", "to": "mathml" }   // 或 "omml"
```

`GET /api/health` 返回鉴权方式、模型、学科列表。

## 评测

```bash
pnpm test        # 20 条文本用例
pnpm test:ocr    # 图片识别冒烟测试（用 test/fixtures/formula.png）
pnpm bench       # 延迟分位
```

当前基线（`deepseek-flash`，关思考）：

| 指标 | 数值 |
|---|---|
| 编译通过 | 20/20 |
| 关键词命中 | 19/20 |
| 平均耗时 | ~0.9 s |
| 单次成本 | ~¥0.001 |

## 成本

单次请求约 700–900 token，按 `deepseek-flash` 峰时价约 **¥0.001/次**；命中上下文缓存后更低。每天 500 次约 ¥15/月。

开 `--thinking` 会慢 3–5 倍、贵 4 倍左右，只在公式高度歧义时用。

## 设计取舍

**为什么不做"一步到位算出答案"？**
因为答案对不对无法自动验证，公式能不能编译却可以。把能力限定在"可验证的转写"上，才能给出可信的 `valid` 字段。

**为什么关掉思考模式？**
转写是模式匹配，不是推理。实测关掉后单次 0.2–1.5 s，开启后 2.7 s 起、输出 token 多 8 倍。歧义场景才值得开。

**为什么限制危险命令？**
KaTeX 以 `trust: false` 渲染，并拒绝 `\href`、`\includegraphics`、`\newcommand` 等，避免从描述注入。公式长度上限 4000 字符。

## 已知限制

- 只做转写：让它"顺便解个方程"不会给出答案
- 复杂排版（多行对齐、长推导）需要人工微调
- 化学依赖 KaTeX 的 mhchem 扩展，个别写法可能不被支持
- 中文口语的地道表达（"根号下"、"以 e 为底"）覆盖较好，方言/缩写未系统测试

## 路线图

- [x] 歧义时返回 2–3 个候选
- [x] MathML / Word（OMML）导出
- [x] 截图识别（粘贴即用）
- [ ] DSH 输入框插件（在聊天框里直接按按钮生成）
- [ ] 手写笔迹识别（不依赖图片）
- [ ] 历史记录持久化

## 许可

MIT

---

**English**: Turn a natural-language description into compilable LaTeX, validated with KaTeX. Not a chat bot: it only transcribes, never computes, and reports low confidence instead of guessing.
