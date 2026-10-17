# Your AI Agent Is Not Broken. You Just Never Onboarded It.

A step-by-step system for business owners to set up AI agents that actually work.

---

## What This Is

Most business owners try an AI agent for an afternoon, get garbage results, and blame the technology.

The real problem? They're treating their agent like software when it's actually a new hire.

This starter kit gives you the same onboarding process you'd use for a great employee: a clear job description, the right tools, structured memory, feedback loops, and realistic timeline expectations. Open it in Claude Code and the interview process walks you through everything.

## What You'll Walk Away With

After the 20-30 minute interview, you'll have four documents ready to use:

1. **An agent brief** -- your agent's job description, responsibilities, decision boundaries, and success criteria. This is the file your agent reads to know what it's supposed to do.
2. **A memory structure** -- how your agent remembers things between sessions so you're not re-explaining the same context every time.
3. **A feedback template** -- customized for your specific role, so you can give feedback that actually changes how the agent works.
4. **A first-week plan** -- specific tasks for the first five days, ordered from simple to complex, so you can calibrate before giving your agent bigger responsibilities.

Want to see what that looks like? We have two worked examples: the [Operations Assistant](examples/operations-assistant/) (multi-task agent for a 15-person firm) and the [Tax Prep Assistant](examples/tax-prep-assistant/) (focused single-workflow agent for a solo CPA). Pick whichever looks closer to your situation.

## What's Inside

- **Interactive Interview** -- Claude Code asks about your business and the role you want filled, then generates your agent's foundation documents
- **6 Practical Guides** -- [Installation](guides/00-installation.md), [job descriptions](guides/01-job-description.md), [tools and access](guides/02-tools-and-access.md), [memory systems](guides/03-memory.md), [feedback](guides/04-feedback.md), and [timeline expectations](guides/05-timeline.md)
- **Ready-to-Use Templates** -- [Agent brief](templates/agent-brief.md), [session documentation](templates/session-documentation.md), [feedback template](templates/feedback-template.md), [memory structure](templates/memory-structure.md), [first-week plan](templates/first-week-plan.md)
- **Worked Examples** -- [Operations Assistant](examples/operations-assistant/) (multi-task agent for a 15-person firm) and [Tax Prep Assistant](examples/tax-prep-assistant/) (narrow single-workflow agent for a solo operator)
- **The Ebook** -- [The full reasoning](ebook/your-ai-agent-is-not-broken.md) behind this approach (also available as a standalone read)

## What This Is NOT

- Not software to install. It's guides, templates, and an interview process.
- Not for developers or engineers. It's for business owners who run things.
- Not a one-size-fits-all solution. The interview adapts to YOUR business and YOUR needs.
- Not a magic fix. Building a good agent takes weeks, sometimes months. This gives you the right starting point.
- Not a guide for agents that take live actions on your systems (sending emails, calling APIs, updating your CRM automatically). This kit builds agents that review, summarize, draft, and advise. Agents that act on live systems need additional setup that's not covered here.
- Not a team-wide tool. This kit is built for one owner onboarding one agent at a time. Multi-user or team-shared agent setups are a different exercise.

## Getting Started

### What you'll need

- A computer with internet access
- A [Claude account](https://claude.ai) -- Claude is Anthropic's AI assistant, the equivalent of ChatGPT from OpenAI. Different company, different account. If you've only used ChatGPT before, you'll need to sign up here separately. Claude Code is included with Claude Pro ($20/month) or higher plans. The starter kit itself is completely free.
- About 30 minutes

### Never used Claude Code before?

No problem. We have a [step-by-step installation guide](guides/00-installation.md) that walks you through everything: setting up your account, installing Claude Code, downloading this starter kit, and opening it. No technical knowledge needed.

### Already have Claude Code installed?

1. Download this starter kit (green **Code** button on GitHub, then **Download ZIP**) or clone it:
   ```
   git clone https://github.com/failcoach/ai-agent-onboarding.git
   ```
2. Open the `ai-agent-onboarding` folder in Claude Code
3. Say: **"Read this project and help me build my first agent"**
4. Follow the interview (about 20-30 minutes)

### Just want to read?

Start with the [ebook](ebook/your-ai-agent-is-not-broken.md). It explains the thinking behind everything in this starter kit.

Then browse the [guides](guides/) at your own pace:
1. [Give Your Agent a Real Job Description](guides/01-job-description.md)
2. [Give It the Right Tools](guides/02-tools-and-access.md)
3. [Give It a Memory](guides/03-memory.md)
4. [Manage It Like Your Best Employee](guides/04-feedback.md)
5. [The Timeline Is Real](guides/05-timeline.md)

The guides and templates work on their own, even without Claude Code.

## After the Interview: Where Your Documents Go

When the interview finishes, you'll have four documents in the chat window. Here's exactly what to do with them.

Create a new folder somewhere on your computer for your agent. Call it whatever makes sense (`my-operations-agent`, `tax-prep-assistant`, whatever). Then save each document:

1. **The agent brief** → save as `CLAUDE.md` in the root of that folder. This is the most important file. Claude Code reads it automatically every time you open the folder, so it becomes your agent's standing instructions.
2. **The memory structure** → create a `docs/` subfolder and save the memory files inside (`KNOWLEDGE_MAP.md`, `business-overview.md`, etc.).
3. **The feedback template** → save as `feedback-template.md` in the root folder.
4. **The first-week plan** → save as `first-week-plan.md` in the root folder.

The interview will also hand you a fifth thing: a pointer to [templates/session-documentation.md](templates/session-documentation.md). This isn't a file you save. It's the structure you (or your agent) will use at the end of each work session to capture what happened, so the next session picks up where you left off. Your agent will prompt you for it. Worth reading once upfront so it's not a surprise.

Your final folder should look like this:

```
my-agent/
  CLAUDE.md              (the agent brief -- the instruction file)
  feedback-template.md
  first-week-plan.md
  docs/
    KNOWLEDGE_MAP.md
    business-overview.md
    current-priorities.md
    decisions-log.md
    session-log.md
```

Now open that folder in Claude Code (File > Open Folder). Claude will read `CLAUDE.md` automatically. Start on day 1 of the first-week plan and go from there.

**Not sure how to create folders or move files?** Just ask Claude Code. It'll walk you through it. That's literally what it's for.

**Did the interview not generate all four documents?** Ask for the missing one: "Can you give me the feedback template based on what we discussed?" The interviewer has everything it needs.

## A Quick Note on How This Works

This starter kit uses a file called `CLAUDE.md`. When you open a folder in Claude Code, it automatically reads this file for instructions. Think of it as standing orders: it tells Claude what this project is and how to help you. In this case, the CLAUDE.md turns Claude into an onboarding interviewer that guides you through building your agent. Once you've built your agent, its own `CLAUDE.md` does the same job -- it tells Claude how to be your agent.

You don't need to understand how CLAUDE.md works to use this kit. Just open the folder and start talking.

## Your Agent Holds the Schedule (You're Still the Manager)

Once set up, your agent initiates two things on its own: a weekly feedback check-in, and a memory health check every two weeks. It's not autonomous -- it doesn't act on your systems without you -- but it does put feedback and memory maintenance on the calendar so you don't have to remember.

You're still the manager. The agent is a conscientious assistant, not an independent operator. Let it ask for the check-in. That's how it gets better.

## What About ChatGPT, Claude.ai, or Other Tools?

This kit is built for [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) because of how it handles standing instructions, files, and memory. The interactive interview runs in Claude Code.

If you use ChatGPT, Claude.ai, a custom GPT, or another tool, you can still use this kit -- you just won't have the interview. Open the [guides](guides/) in order, fill in the [templates](templates/) manually using your own answers, and you'll end up with the same four documents. The concepts (job description, memory, feedback, timeline) don't change between platforms. Only the mechanics do.

It hasn't been tested with GitHub Copilot, Cursor, Windsurf, Codex, or other AI coding tools. The guides and templates are plain text -- they work anywhere you can read files.

## The Philosophy

> When your employee underperforms, you can blame them. Their attitude, their skills, their motivation. When your AI agent underperforms, there's nobody to blame but the person who set it up. You.

This kit is built on one insight: the skills that make AI agents work are the same skills that make human teams work. Master one, and you improve both.

## Built By

**[Miha Matlievski](https://fail.coach)** -- I help business owners build the management systems that make both human teams and AI agents perform. After building 5 companies, failing at all of them, paying back $5M in debt, and rebuilding, I now work with owners who want to get this right.

[fail.coach](https://fail.coach) | [aiforowners.co](https://aiforowners.co)

Everything here is free. Use it however you want. If you try it and get stuck on the parts that aren't about the technology -- the role definitions, the management systems, the feedback loops -- that's what I actually help with.

[Book a call](https://calendly.com/failcoach/meet-and-greet) or [send me a message on LinkedIn](https://www.linkedin.com/in/mihamatlievski/).

## License

[MIT](LICENSE) -- use it, share it, build on it.
