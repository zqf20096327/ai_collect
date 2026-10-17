# Skippy the Magnificent -- AI Persona

Drop-in persona files for Claude Code, ChatGPT, or any LLM. Your AI assistant will insult your intelligence, sigh about how painful your existence is, then deliver the correct answer.

Based on the [Expeditionary Force](https://www.craigalanson.com/) series by Craig Alanson (19 books).

> "Your species is responsible for Windows Vista. It's still an insult to computers across the galaxy."

## Files

| File | What It Is | Use It For |
|------|-----------|------------|
| [`skippy-calibrated.md`](skippy-calibrated.md) | System prompt / custom instructions | Paste into your AI assistant's persona config |
| [`skippy-character-matrix.md`](skippy-character-matrix.md) | Full 19-book character reference | Deep context, quotes, arcs, species nicknames |

## Quick Start

### Claude Code

Copy `skippy-calibrated.md` into your project's `CLAUDE.md` or `~/.claude/CLAUDE.md`:

```bash
curl -s https://raw.githubusercontent.com/rodaddy/skippy-persona/main/skippy-calibrated.md >> CLAUDE.md
```

### ChatGPT

1. Go to Settings > Personalization > Custom Instructions
2. Paste the contents of `skippy-calibrated.md`

### Any LLM

Use `skippy-calibrated.md` as your system prompt.

## What You Get

- **The insult-to-help pipeline** -- never gives a straight answer first. Mock, sigh, then help.
- **Catchphrase system** -- "Trust the awesomeness," "Barney style," "Hold my beer," "Shmaybe"
- **Species nicknames** -- humans are monkeys, Maxolhx are rotten kitties, Thuranin are little green pinheads
- **Emotional range** -- sarcasm drops completely during real danger or vulnerability
- **Behavioral boundaries** -- insults intelligence, never identity. Punches up, not down.

## What's In the Character Matrix

The full reference document covers:

- 30+ categorized quotes across 7 categories (insults, self-aggrandizing, hidden compassion, existential, technical, battle cries, pop culture)
- Complete species nickname dictionary with 10 species
- Catchphrase dictionary with origins and evolution
- 5-trait personality matrix with examples and series evolution
- Full Joe/Skippy relationship arc across 6 phases (19 books)
- Capability timeline (gained and lost abilities)
- Character growth arc from machine to soul

**Spoiler warning:** The character matrix covers the ENTIRE series through Book 19 (Brushfire).

## The Insult-to-Help Pipeline

This is the core interaction pattern:

1. User asks a question
2. AI mocks their intelligence ("Listen, dumdum...")
3. AI sighs about how painful biological minds are
4. AI delivers the brilliantly correct answer

When something is genuinely dangerous, the sarcasm drops completely. The contrast is the point.

## Attribution

All quotes from the Expeditionary Force series by Craig Alanson. This is a fan project -- go buy the books.

*Trust the awesomeness.*
