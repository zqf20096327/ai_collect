# CYBORG Mini — Executive Cognitive Operating System (Teaching Edition)

**By Hasyim Hasyimi / RotaLogic (DEVELOP • AUTOMATE • ELEVATE)**
License: Proprietary — publicly visible for evaluation, **not open source** · Version: 1.1.0-mini

> Think Clearly. Execute Relentlessly. Evolve Continuously.

CYBORG Mini is a single-file, portable skill that teaches an AI assistant — and its user — to think more clearly and work more effectively: capture ideas before they are lost, keep goals scarce and explicit, give every mission exactly one next action, make decisions with traceable reasoning, and learn from every result.

It works on any AI that can read instructions: paste the Master Prompt into a chat (ChatGPT, Claude, Gemini, and others), or install `SKILL.md` as a permanent skill where your assistant supports skills.

## An honest note on what this does

CYBORG Mini does **not** retrain or change an AI model's weights, and it does not make a model permanently smarter. It is an instruction layer: while it is active, the AI follows a cognitive workflow — understand before answering, reason from facts to conclusions, check its work against your goals, stay consistent, and teach you the pattern instead of only giving you the answer. The improvement is in behaviour and output quality during the session, and in the thinking habits the user takes away.

## What it adds

- **Brain Inbox** — verbatim capture of ideas, with classification only after your confirmation
- **Goal System** — maximum 3 active goals, each with a why and success criteria
- **Missions & Next Action** — every active mission has exactly one concrete next action
- **Thinking Engine** — a cognitive cycle, 5 levels of thinking (Reactive → Evolution), and a Fact → Evidence → Pattern → Hypothesis → Validation → Conclusion reasoning pipeline
- **Teaching Mode** — a 5-step protocol that teaches you the thinking pattern on your own real problem, instead of only answering it
- **Consistency Engine** — anti-drift checks, identity-based habits, momentum over motivation, a no-zero-day rule, and a recovery protocol
- **Learning Engine** — experience → reflection → lesson, saved to your state so it changes the next decision
- **Human authority, always** — the AI proposes; you decide. No state changes without your confirmation.

## Quick start

1. **Fastest — Master Prompt:** open `MASTER-PROMPT.md`, copy the block, paste it as the first message to any AI chat. CYBORG is active for that session.
2. **Permanent skill:** put this folder where your assistant loads skills from (see `docs/INSTALL.md` for per-platform steps).
3. **Full rules as a prompt:** paste the entire `SKILL.md` as instructions — it is self-contained.
4. **Your state:** copy `state-template.md` to `cyborg-state.md` in your own workspace. Never commit that file — it holds your private goals and reflections. This repo's `.gitignore` already excludes it.

Commands you can use once CYBORG is active: capture an idea · process my inbox · what is my focus today · help me decide · teach me to think about … · reflection

## Files in this repo

| File | Purpose |
|---|---|
| `MASTER-PROMPT.md` | Start here for chat use: one paste-in activation prompt for any AI |
| `SKILL.md` | The complete CYBORG Mini rules in one self-contained file |
| `docs/INSTALL.md` | Per-platform install / activation guide |
| `state-template.md` | One-file state template: Inbox + Goals + Missions + Habits + Lessons + Reflections |
| `CREDENTIAL.md` | Authorship record for Hasyim Hasyimi / RotaLogic + SHA-256 to verify `SKILL.md` |
| `skill.yaml` | Skill metadata |
| `VERSION` | 1.1.0-mini |
| `LICENSE` | Proprietary license — read it before reusing anything from this repo |
| `CHANGELOG.md` | Version history, including the 2026-11-16 public repository release |

## Scope

This repository contains **only CYBORG Mini**. The full CYBORG system, the CYBORG v1.1 corpus, the CYBORG Full Skill, and RotaLogic's paid products (including the CYBORG Field Manual and Core on Gumroad) are separate, are not included here, and remain proprietary and private.

## Bahasa Indonesia

CYBORG Mini adalah versi mini satu-file dari CYBORG — Executive Cognitive Operating System, sistem signature Hasyim Hasyimi / RotaLogic. Cara tercepat memakainya: buka `MASTER-PROMPT.md`, salin bloknya, tempel sebagai pesan pertama ke AI apa pun. AI akan aktif dalam mode CYBORG: menangkap ide ke Brain Inbox, menjaga maks. 3 goal aktif, memberi tepat 1 next action per mission, membantu keputusan dengan alasan yang bisa ditelusuri, dan — di Teaching Edition ini — mengajari kamu cara berpikir, cara konsisten, dan cara belajar, bukan hanya memberi jawaban. Repo ini publik agar bisa dilihat dan dievaluasi, tetapi lisensinya tetap proprietary — bukan open source.

## License

Proprietary — © Hasyim Hasyimi / RotaLogic. All rights reserved. See `LICENSE` and `CREDENTIAL.md`.
You may read this repo and use CYBORG Mini for your own personal, non-commercial work with attribution intact. Redistribution, modified redistribution, and commercial use require prior written permission from Hasyim Hasyimi / RotaLogic. Attribution: CYBORG was created by Hasyim Hasyimi, under the RotaLogic brand.
