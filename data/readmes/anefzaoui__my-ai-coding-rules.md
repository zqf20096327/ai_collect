# Prompt Archive

I've spent the last few years working with AI coding assistants on real projects, and most of what I learned about prompting them came from things going wrong. A patch script corrupts a file, the agent runs a checkout to "fix" it and wipes an hour of uncommitted work. Or it ships a whole feature in one go and three other things quietly break. Or I look at an API bill and realize half of it was for parsing that a small script could have done.

Every time something like that happened I wrote a rule for it. The rules turned into prompts. This is where I keep them.

Nothing here depends on a language or framework. I use these with Claude Code, Cursor and Copilot, and they should work with any assistant that reads a rules file or takes a system prompt.

## What's in here

All the prompts are in [prompts.md](./prompts.md). Each one has a title, a note on what it's for and when I use it, and the prompt itself in a code block.

Standing rules (paste once, stays active all session):

- [Work Rules](./prompts.md#1-work-rules). The main one. Makes the assistant inspect, ask, plan and get approval before writing any code, and adds permanent rules about fixing root causes, keeping costs down, not running destructive commands without a backup, and keeping docs current.

Session controls (short prompts I type mid-session):

- [Autonomous Run](./prompts.md#2-autonomous-run). Skip the approval step for one task and let it run to the end.
- [Progress Check](./prompts.md#3-progress-check). Get a status update and todo list without it stopping.
- [Self-Audit](./prompts.md#4-self-audit). Make it check everything it claims against the actual code.

I add prompts when they've held up across a few projects, not before.

## How to use them

Standing rules go wherever your tool keeps persistent instructions:

- Claude Code: `CLAUDE.md` in the project root
- Cursor: `.cursor/rules/` or `.cursorrules`
- Copilot: `.github/copilot-instructions.md`
- Windsurf: `.windsurfrules`
- Anything else: the system prompt, or just the first message of the session

Session controls you type into the chat when you need them.

## The thinking behind them

A few things I now consider non-negotiable:

The assistant repeats the task back before touching anything. It's the cheapest way to catch a misunderstanding, and it keeps the original request in context as the session gets long.

It reads the code before asking questions, and asks questions before writing code. Most "clarifying questions" can be answered by looking at the codebase. It should only ask about what it can't check itself.

I approve the plan. If I want to skip that, I say so explicitly.

Small chunks, one file at a time. One-shotting a feature is how you end up with a component that works alone and a system that doesn't.

Backup, stash or commit before anything destructive. Two irreversible actions in a row is how you lose an afternoon.

Use the cheapest thing that works. Don't send a large model something a regex can do. Don't upgrade a tier when you can split the job.

Don't trust the summary, check the code. What the assistant says it did and what it actually did are not the same thing.

## Contributing

If a prompt saved you from something, or caused something, open an issue. I care more about cases where a rule breaks than about new rules.

## License

MIT. Take them, fork them, rewrite them.
