# Writing Style Skill

Transform AI-generated text into your personal voice.

## The Problem

AI gives you a response to send someone. It sounds like AI:

> "Dear Mr. Smith, I hope this email finds you well. I wanted to reach out regarding the potential opportunity we discussed. Please don't hesitate to let me know your availability at your earliest convenience. Best regards..."

You want it to sound like **you**.

## The Solution

This skill rewrites any text in your personal style. You define your patterns once, then every AI response gets transformed automatically.

## Installation

### Claude Code

```bash
git clone https://github.com/lout33/writing-style-skill ~/.claude/skills/writing-style

# Add the command shortcut
cp ~/.claude/skills/writing-style/command/my-style.md ~/.claude/commands/
```

### OpenCode

```bash
git clone https://github.com/lout33/writing-style-skill ~/.config/opencode/skill/writing-style

# Add the command shortcut
cp ~/.config/opencode/skill/writing-style/command/my-style.md ~/.config/opencode/command/
```

## Usage

```
/my-style "I hope this email finds you well. I wanted to reach out regarding..."
```

Or natural language:
```
rewrite this in my style: "..."
make this sound like me
```

**Output:** Just the transformed text. No explanation, ready to copy-paste.

---

# Setting Up YOUR Style

Three steps: **Export** your real messages > **Ask AI** to find your patterns > **Save** to style file.

---

## Step 1: Export Your Real Writing

Pick one or more sources:

### Option A: Gmail (for professional style)
1. Go to Gmail > search `in:sent`
2. Copy 10-20 emails you wrote into a text file
3. Focus on emails where you were being yourself (not templates)

### Option B: WhatsApp (for casual style)
1. Open a chat with a close friend
2. Tap contact name > Export Chat > Without Media
3. You'll get a `.txt` file with your messages

### Option C: Slack/Discord DMs
1. Scroll through your DMs
2. Copy messages into a text file
3. Get a mix of short and longer messages

### Option D: Twitter/X posts
1. Go to your profile
2. Copy tweets that sound like you
3. Good for punchy, public-facing voice

---

## Step 2: Ask AI to Find Your Patterns

Paste your exported messages into Claude/ChatGPT with this prompt:

```
Analyze my writing style from these messages. Tell me:

1. How I start messages (greeting style)
2. How I end messages (closing style)
3. My typical message length
4. Slang or abbreviations I use
5. How I say "yes", "no", "okay"
6. Phrases I use often
7. Things I never seem to say

Here are my messages:
[paste your exported messages]
```

The AI will give you a summary of YOUR patterns.

---

## Step 3: Save to Your Style File

Take the patterns AI found and put them in `references/my-style.md`:

```markdown
# My Style

## Professional (from my emails)
- Greeting: "Hi [Name],"
- Closing: "Cheers" or just my name
- Length: 3-5 sentences max
- I drop links without explaining them
- Subject lines are short: "Team up", "Quick question"

Real example:
> Hi Nik,
> I build AI tools. Here's my latest: [link]
> Want to team up?
> Cheers

## Casual (from my WhatsApp)
- No greeting, just start talking
- Short messages: 2-5 words
- Slang: "bro", "lol", "tbh"
- Multiple messages instead of one long one

Real example:
> yo
> did u see that
> lmao

## Never Say
- "I hope this finds you well"
- "Best regards"
- "Please don't hesitate"
- "At your earliest convenience"
```

---

## Step 4: Test and Refine

Run `/my-style` on some AI-generated text. If the output doesn't sound like you:

1. Add more real examples to your style file
2. Add phrases to "Never Say" that keep appearing
3. Be more specific about your patterns

The more examples you add, the better it works.

---

## File Structure

```
writing-style-skill/
├── SKILL.md              # How the skill works
├── README.md             # This file
├── references/
│   └── my-style.md       # YOUR style rules (edit this)
└── command/
    └── my-style.md       # /my-style command
```

## Example

**Input:**
```
/my-style "Dear Mr. Smith, I hope this message finds you well. I wanted to follow up on our conversation last week. I believe my skills would be a great fit for your team. Please let me know your availability. Best regards, John"
```

**Output:**
```
Hi Smith,

Following up on last week. Still interested if you are.

When works for a quick call?

John
```

## Tips

1. **Start simple** — Basic rules first, refine over time
2. **Use real examples** — The more examples, the better it works
3. **Test on AI responses** — Run it, see output, adjust
4. **Separate modes** — Your email voice != your WhatsApp voice

## Related

Part of the [Claude Life Assistant](https://github.com/lout33/claude_life_assistant) ecosystem — a symbiotic AI that remembers you, challenges you, and extends your cognition.

## License

MIT

## Author

[@lout33](https://github.com/lout33)
