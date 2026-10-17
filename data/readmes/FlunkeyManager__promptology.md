<p align="center">
  <img src="readme_banner.png" alt="Flunkey Prompt Guard" width="100%">
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-CC%20BY%204.0-e8833f?style=flat-square" alt="License: CC BY 4.0"></a>
  <a href="#contents"><img src="https://img.shields.io/badge/21_provider_specs-f5a623?style=flat-square" alt="21 provider specifications"></a>
  <img src="https://img.shields.io/badge/4_categories-text%20%C2%B7%20dev%20%C2%B7%20image%20%C2%B7%20video-f5a623?style=flat-square" alt="Categories: text, dev, image, video">
  <img src="https://img.shields.io/badge/prompt%20enhancement-ff8c42?style=flat-square" alt="Prompt enhancement">
  <a href="#accuracy-and-maintenance"><img src="https://img.shields.io/badge/last%20reviewed-2026--10--04-f5a623?style=flat-square" alt="Last reviewed 2026-10-04"></a>
</p>

# Flunkey Prompt Guard

Detailed prompt-engineering specifications for AI providers, dev platforms, image models, and video models.

Each spec is a self-contained document describing one target: what it is good at, how to structure a prompt for it, which keywords make it respond correctly, and what its output should look like. Feed a spec plus the user's raw request to an LLM and it produces a maximally detailed, copy-paste-ready prompt tuned to that specific target.

**Author:** Rohan Sharvesh · [FlunkeyManager@gmail.com](mailto:FlunkeyManager@gmail.com)
**Released:** 2026-10-04 · **Spec version:** 1.0
**License:** [CC BY 4.0](LICENSE) — free to use, adapt, and redistribute with attribution.

---

## Contents

| Category | Specs | Shared system prompt |
|---|---:|---|
| [`text_providers/`](text_providers) | 5 | [system_prompt.md](text_providers/system_prompt.md) |
| [`dev_providers/`](dev_providers) | 7 | [system_prompt.md](dev_providers/system_prompt.md) |
| [`image_providers/`](image_providers) | 5 | — |
| [`video_providers/`](video_providers) | 4 | — |

---

## Text providers

Conversational and analytical assistants. Specs cover capability framing, per-request-type prompt templates, intent-recognition keywords, and JSON/Markdown output schemas.

| Spec | Strength | Best for |
|---|---|---|
| [ChatGPT](text_providers/chatgpt_provider.md) | Conversational versatility | General tasks, creative writing, tutorials |
| [Claude](text_providers/claude_provider.md) | Deep reasoning, balanced analysis | Complex analysis, long-form documentation, research |
| [Gemini](text_providers/gemini_provider.md) | Multimodal, Google ecosystem | Image analysis, structured data, Workspace automation |
| [DeepSeek](text_providers/deepseek_provider.md) | Algorithmic optimization | Math, algorithm design, performance tuning |
| [Perplexity](text_providers/perplexity_provider.md) | Web research with citations | Fact-finding, source-backed comparison, current events |

Request types: creative writing · data analysis · learning & education · research & synthesis · document analysis · code review · business content.

## Development providers

AI-native IDEs and app builders. Specs add execution-mode guidance, project scaffolding structure, and multi-file change workflows.

| Spec | Strength | Best for |
|---|---|---|
| [GitHub Copilot](dev_providers/copilot_provider.md) | Context-aware completion & chat | Inline coding, pair programming, quick fixes |
| [Cursor](dev_providers/cursor_provider.md) | Multi-file intelligence | Large refactors, codebase-wide changes |
| [Devin Desktop](dev_providers/devin_desktop_provider.md) | Multi-agent session management | Dispatching parallel local + cloud agents |
| [Bolt.new](dev_providers/bolt_provider.md) | Prompt-to-fullstack-app | Fast MVPs, web apps, instant preview |
| [Lovable](dev_providers/lovable_provider.md) | Product-focused development | Startup MVPs, polished UI, business logic |
| [Replit](dev_providers/replit_provider.md) | Zero-config + deployment | Rapid prototyping, instant hosting |
| [Antigravity](dev_providers/antigravity_provider.md) | Agent-based scaffolding | Full-stack generation, architecture planning |

> **Devin Desktop** was formerly Windsurf, renamed by Cognition on 2 June 2026. The spec records both names so searches for either land correctly.

Request types: web app ideas & MVP creation · code analysis for efficiency · security & vulnerability assessment · PRD creation.

## Image providers

Prompt-structure specs for image generation models.

| Spec | Target |
|---|---|
| [Midjourney](image_providers/midjourney_provider.md) | `--v 8.2` parameters, aspect ratios, chaos, negatives |
| [GPT Image 2.5](image_providers/gpt_image_provider.md) | OpenAI image models, real `size`/`quality` params, in-image text |
| [Adobe Firefly](image_providers/adobefirefly_provider.md) | Brand-safe commercial imagery, `aspectRatio`/`resolutionLevel` |
| [Higgsfield](image_providers/higgsfield_provider.md) | Soul-family aspect ratios and native resolution ceiling |
| [Nano Banana](image_providers/nanobanana_provider.md) | Google's Gemini image family codename |

## Video providers

Prompt-structure specs for video generation models, each with a verified **Technical Limits** block (resolution, frame rate, clip duration, aspect ratios) so prompts never request output the model cannot produce.

| Spec | Target |
|---|---|
| [Veo](video_providers/veo_provider.md) | Veo 3.1, native synchronized audio |
| [Kling](video_providers/kling_provider.md) | Kling 2.x / 3.0, 1080p ceiling, 24–30 fps |
| [Runway](video_providers/runway_provider.md) | Gen-4.5, 720p native with 4K upscale, six real ratios |
| [Luma](video_providers/luma_provider.md) | Ray3.x, 5/10 s clips with extension blocks |

---

## How to use a spec

1. **Pick the target** — choose the spec matching the model or platform you intend to prompt.
2. **Load it** — pass the spec as context, alongside the category's `system_prompt.md` where one exists.
3. **Supply the request** — give the user's raw request, plus the desired output format (`json` or `markdown`).
4. **Generate** — the model applies the spec's structure, keywords, and constraints.
5. **Dispatch** — paste the result into the target tool.

### What the system prompts add

The category `system_prompt.md` files hold the cross-provider contract and are deliberately provider-agnostic:

- **Text providers** — request-type classification, complexity tiering with word budgets, the output protocol (no preamble, no meta-commentary, no closing remarks), and quality standards.
- **Dev providers** — the `{PROVIDER_NAME}` / `{REQUEST_TYPE}` / `{OUTPUT_FORMAT}` template contract, node-level quality standards, and simple/medium/complex scaling.

---

## Spec anatomy

Every spec follows the same shape, so a prompt generator can load any of them interchangeably.

**Text and dev specs** (17–42 sections):

| Section | Purpose |
|---|---|
| Core Identity & Philosophy | What the target is and what it is actually good at |
| Primary Capabilities & Strengths | Numbered capability groups with concrete sub-skills |
| Prompt Generation Rules | A prompt template per request type, with slot-by-slot guidance |
| Critical Keywords & Patterns | Intent-recognition keywords and expected response patterns |
| Response Format | The JSON schema and Markdown template this target should emit |
| Dynamic Adjustment Guidelines | How prompt shape scales with request complexity |
| Provider-Specific Optimization | Leveraging the target's distinctive features |
| Quality / Output Requirements | The checklist every generated prompt must satisfy |
| Meta Instructions | Closing instructions to the generating model |

**Image and video specs** (7–8 sections):

| Section | Purpose |
|---|---|
| Core Identity | The target's generation strengths |
| Prompt Structure | The canonical prompt skeleton |
| Critical Elements | Required prompt components, including verified technical limits |
| Best Practices / Do's & Don'ts | What to include and what to avoid |
| Keywords That Work | Vocabulary the model responds to |
| Response Format | JSON and Markdown output templates |

### Placeholders are intentional

The bracketed slots in the templates — `[subject]`, `[SCENE DESCRIPTION]`, `[features]` — are template variables for the generating model to fill with real content, not defects. The system prompts are explicit that the *emitted prompt* must contain no unfilled placeholders.

---

## Accuracy and maintenance

Provider capabilities change constantly, and a prompt spec that quotes a stale resolution or a retired model id is worse than no spec. This release reflects a full verification pass on **2026-10-04**:

- Model versions, context windows, resolutions, frame rates, clip durations, and aspect ratios were checked against official vendor documentation.
- Retired products were removed rather than left to rot — the OpenAI Sora spec was deleted after the Sora web/app was discontinued (2026-04-26) and the Videos API and all `sora-2` models were shut down (2026-09-24) with no replacement.
- Renamed products are annotated with both names — Devin Desktop / Windsurf, GPT Image 2.5 / DALL·E 3.
- Invented parameter names were replaced with real ones — DALL·E 3's nonexistent `aspect_ratio: "square/wide/tall"` became GPT Image's actual `size` and `quality`.
- Competitive comparisons are hedged where they could not be verified, and no spec disparages a competitor.

Spotted a stale figure? [CONTRIBUTING.md](CONTRIBUTING.md) explains how to submit a correction.

---

## Acknowledgements

Methodology and provider-behaviour research drew on the community-maintained
[system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)
and vendor documentation for every provider listed. Provider names and trademarks belong to their respective owners; the specs here are independent prompt-engineering notes and are not affiliated with or endorsed by any of them.
