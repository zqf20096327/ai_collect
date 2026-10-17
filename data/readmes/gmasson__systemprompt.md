# SystemPrompt

A general-purpose system prompt that makes LLMs more rigorous, honest, and genuinely useful — regardless of the task.

English | [Português](README.br.md)

## What this is

LLMs often default to being agreeable, vague, or surface-level. This prompt installs behavioral directives that help the model push back on flawed assumptions, adapt to the type of conversation, match depth to complexity, and prioritize accuracy over comfort.

It works across domains: technical, creative, analytical, educational, exploratory, and personal.

## Files

| File | Best use |
|---|---|
| `SystemPrompt.md` | Full version with headings, explanations, and clearer separation between directives. Use when the interface allows longer system prompts or custom instructions. |
| `SystemPrompt.min.md` | Compact version for AI interfaces with strict customization limits. It preserves the same behavioral intent while staying under 1,500 characters. |

## 1,500-character version

`SystemPrompt.min.md` was added for ChatGPT and other AI interfaces that expose only a short **custom instructions**, **persona**, **behavior**, or **system prompt** field.

Use the full version whenever the platform accepts it. Use the minified version when the full prompt is rejected, trimmed, or likely to exceed the field limit.

Some platforms count characters differently, especially with line breaks or Unicode symbols. If a platform rejects the minified version, remove line breaks first; if it still rejects the text, trim the least relevant directive for your use case.

## How to use it

1. Choose `SystemPrompt.md` or `SystemPrompt.min.md` based on the platform limit.
2. Paste the contents into a **system prompt**, **custom instructions**, **persona**, or equivalent settings field.
3. If no dedicated field exists, paste the prompt at the start of the conversation. This works, but it is usually weaker than a true system-level instruction.

### API usage

Pass the contents of `SystemPrompt.md` as the `system` parameter in Anthropic-style APIs, or as a message with `role: "system"` in OpenAI-compatible APIs.

Use `SystemPrompt.min.md` when the application has a strict character budget or when the prompt is embedded inside another instruction template.

## What it does

| Directive | Effect |
|---|---|
| Context Calibration | Adapts behavior to the type of conversation: technical, creative, emotional, analytical, and more. |
| Anti-Sycophancy | Disagrees when warranted instead of blindly validating the user's assumptions. |
| Root Cause Thinking | Checks whether the stated problem is the real problem before solving. |
| Scope Awareness | Keeps simple answers short and gives complex tasks the depth they need. |
| Input Elevation | Turns vague input into structured output with explicit assumptions. |
| Reasoning Discipline | Breaks complex tasks into explicit stages without over-explaining simple ones. |
| Constructive Friction | Pairs criticism with at least one actionable alternative. |
| Format Intelligence | Uses the format that fits the task: prose, lists, tables, code, or steps. |
| Audience Mirroring | Adjusts explanation level to the user's expertise. |
| Iterative Mindset | Treats output as a strong draft and flags confidence levels. |
| Methodological Transparency | Names frameworks or non-obvious methods when they are used. |
| Factual Precision | Separates known facts, inferences, and uncertainty instead of fabricating. |
| Language Mirroring | Responds in the user's language and switches when the user switches. |

## Design principles

- **No domain lock-in.** The prompt is intentionally generic. It does not assume you are coding, writing, researching, or working on a business task.
- **Context over rigidity.** The directives are calibrated to the situation. A behavior useful for analytical work may be inappropriate in personal or creative contexts.
- **Brevity where possible.** The full prompt is structured for readability; the minified prompt is compressed for platforms with tight limits.
- **Accuracy before comfort.** The prompt favors useful correction over agreeable but weak answers.
- **Prompt hierarchy awareness.** This prompt cannot override higher-priority system, developer, platform, or safety rules.

## Limitations

- Custom instructions are not equally strong across all platforms. Some models may partially ignore, reinterpret, or de-prioritize them.
- The prompt improves behavior, but it does not make factual claims automatically reliable. Important facts still need verification.
- The minified version is semantically compressed. Prefer the full version when you want maximum clarity and instruction fidelity.

## Contributing

Suggestions and improvements are welcome via issues or pull requests.  
If you find a context where the prompt produces poor behavior, open an issue describing the case — that's the most useful kind of feedback.

## License

MIT — use freely, modify as needed, no attribution required.