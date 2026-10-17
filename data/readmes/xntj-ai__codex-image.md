# codex-image

**让 Claude Code 用你的 ChatGPT / Codex 订阅额度出图 —— 不需要 OpenAI API key，不计 API 费用。**

*A Claude Code skill that generates images on your ChatGPT / Codex **subscription quota** — no `OPENAI_API_KEY`, no per-image API billing.*

---

做 PPT、出 demo、配网页图，一张张走 API 是按张烧钱的（几十页 PPT 轻松几百块）。但如果你已经在付 ChatGPT / Codex 的订阅，那份额度里就包含内置的图像生成工具。这个 skill 让 Claude Code 把需求写成结构化提示词、用脚本驱动 `codex exec` 调用**内置 `image_gen` 工具**出图，吃订阅额度，把你已经付的钱用满。

If you already pay for a ChatGPT / Codex subscription, that quota includes a built-in image tool. Instead of paying per-image API costs to make slide decks, demos, or web art, this skill has Claude Code write a structured prompt and drive `codex exec`'s **built-in `image_gen` tool** — billed against the subscription you already pay for.

## 原理 · How it works

```
你的需求 / your request
  └─ Claude Code 写成结构化提示词 (references/prompt-recipes.md)
       └─ scripts/codex_image.py
            └─ codex exec --sandbox workspace-write   ← 内置 image_gen 工具 / built-in tool
                 └─ 自动存到 $CODEX_HOME/generated_images/<session>/ig_*.png
                      └─ 复制到你指定的 --out，校验是真 PNG / copy to --out, verify real PNG
```

订阅额度计费（rate-limit id `codex`），**不碰 `OPENAI_API_KEY`**。Billed on subscription quota, never touches `OPENAI_API_KEY`.

## 三个稳定支点 · Three pillars of stable output

1. **强制真工具 / Force the real tool** — 提示词带固定契约头：必须调内置 `image_gen`，严禁用代码 / PowerShell / SVG / canvas 画图。A fixed contract header forbids the model from faking the image with code/SVG/canvas.
2. **结构化提示词 / Structured prompt** — 按 `references/prompt-recipes.md` 的 spec 把需求写清楚（用途 → 主体 → 细节 → 约束）。Quality comes from a use-case-aware spec, not a one-liner.
3. **明确产出 + 校验 / Explicit output + verification** — 提示词写死输出绝对路径；脚本按本次 codex **session-id** 定位产出、复制、解析 PNG 头校验尺寸（并发安全）。Located by this run's codex session-id (concurrency-safe), copied, and PNG-header-validated.

## 安装 · Install

把这个仓库放到你的 Claude Code skills 目录：Drop this repo into your Claude Code skills directory:

```
~/.claude/skills/codex-image/
```

Claude Code 会自动按 `SKILL.md` 的 description 触发。Claude Code picks it up automatically via the `SKILL.md` description.

## 用法 · Usage

让 Claude Code 自己调（推荐），或手动跑脚本 / Let Claude Code drive it, or run the script directly:

```bash
python "~/.claude/skills/codex-image/scripts/codex_image.py" \
  --out "<absolute output path>.png" \
  --prompt-file "<prompt.txt>" \
  --size "1536x1024"
```

- `--transparent` 走色键抠图出透明 PNG（需 Pillow）。Chroma-key → transparent PNG (needs Pillow).
- `--print-prompt` 只打印最终提示词调试。Print the final prompt and exit.
- 脚本输出 JSON：`ok / out / width / height / bytes / source`。Script prints a JSON result.

## 前置条件 · Prerequisites

- `codex --version` 能跑（已装 Codex CLI）。Codex CLI installed.
- `codex login` 已用 **ChatGPT 订阅账号**登录（不是 API key 模式）——否则不吃订阅额度。Logged in with a **ChatGPT subscription account**, not API-key mode.

## 关键边界（别信 4K）· Key boundaries (it's not 4K)

- **分辨率固定约 1.57MP**（≈1536×1024，按长宽比重排），最大边 ~1672px —— **不是 4K**。订阅内置路径就这么大；真 4K 要走 API（违背订阅初衷）。Fixed ~1.57MP regardless of the size hint — not 4K.
- **额度**：Plus（$20/月）纯出图约 **50 张/5h、~30 张/天**（周额度封顶，和写代码共用）。~50 images / 5h, ~30 / day on Plus.
- **长文字 / 精确排版不可靠** —— 需要精确排版的海报另用排版工具。Long text / precise typography is unreliable.
- **透明背景**靠色键抠图，适合边缘清晰的实心主体；毛发/玻璃/烟雾抠不干净。Transparency via chroma key — clean solid subjects only.

详见 `references/boundaries.md`。Full details in `references/boundaries.md`.

---

来自「张拼拼 AI 实战教练」的真人长视频实战系列。From the 张拼拼 hands-on AI series · <https://xntj.tv>

MIT License.
