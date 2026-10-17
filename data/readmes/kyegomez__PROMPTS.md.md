# PROMPTS.md

**Understanding CLAUDE.md, MEMORY.md, SKILLS.md, SOUL.md, and Related Prompting Mechanisms**

As agentic systems like Claude become embedded in developer workflows, a new class of "context files" has emerged — structured documents that shape how an agent behaves, remembers, learns, and acts. Names like `CLAUDE.md`, `MEMORY.md`, `SKILLS.md`, and `SOUL.md` are increasingly common in repos, agent frameworks, and personal AI setups.

This guide explains what each of these files is, why they exist, how they differ from one another, and how developers and power users can use them to build more capable, consistent, and personalized AI workflows.

---

## Part 1: What Are Context Files?

Before diving into specific files, it helps to understand the broader concept.

Large language models like Claude have no persistent memory by default. Each conversation begins with a blank slate — unless you explicitly provide context. Context files are a solution to this problem: they are plain-text or Markdown documents you include at the start of a session (or inject into the system prompt) to give the model structured information about who it is, what it knows, what it can do, and how it should behave.

The names `CLAUDE.md`, `MEMORY.md`, `SKILLS.md`, and `SOUL.md` are conventions — not enforced standards — but they've become widely adopted because they mirror how developers think about project documentation (`README.md`, `CHANGELOG.md`, etc.). The `.md` suffix signals that these are human-readable Markdown files, typically placed in the root of a project or agent directory.

Think of these files collectively as a "personality package" or "agent configuration layer." Together they answer four core questions:

- **CLAUDE.md** — *What is this project and how should I work within it?*
- **MEMORY.md** — *What do I already know about this user or context?*
- **SKILLS.md** — *What specialized capabilities can I invoke?*
- **SOUL.md** — *Who am I and what do I value?*

---

## Part 2: CLAUDE.md

### What It Is

`CLAUDE.md` is the most widely adopted of these files, popularized by Anthropic's own **Claude Code** agentic coding tool. It is a project-level instruction file that lives in the root of a repository or working directory. When Claude Code (or any Claude-based tool configured to look for it) starts a session, it automatically reads `CLAUDE.md` and loads it into context.

The official Anthropic documentation describes it as:

> "A way to give Claude persistent instructions about your project — its structure, conventions, commands to run, things to avoid, and anything else the model should know to work effectively."

### What Goes in CLAUDE.md

A well-written `CLAUDE.md` typically contains:

**Project overview** — A concise description of what the codebase does, what language/framework it uses, and any architectural context the model needs.

**Development commands** — Common commands for building, testing, linting, and deploying. For example: `npm run dev`, `pytest`, `make build`. This saves Claude from having to guess or explore.

**Code style and conventions** — Preferred naming conventions, file structure rules, comment style, import ordering, etc.

**Important constraints** — Things Claude should *not* do: files it shouldn't modify, APIs it shouldn't call, patterns to avoid.

**Environment notes** — Information about the runtime environment, environment variables, or external dependencies.

**Example `CLAUDE.md`:**

```markdown
# MyApp

A Next.js SaaS application with a PostgreSQL backend.

## Commands
- `npm run dev` — start dev server
- `npm test` — run Jest tests
- `npx prisma migrate dev` — apply DB migrations

## Conventions
- Use TypeScript strict mode
- All API routes live in `/app/api/`
- Never commit secrets to git; use `.env.local`

## Constraints
- Do not modify `prisma/schema.prisma` without explicit instruction
- Do not use `any` type in TypeScript
```

### Where It Lives and How It's Loaded

In Claude Code, `CLAUDE.md` is automatically loaded from the current working directory, any parent directories, and a global `~/.claude/CLAUDE.md` for user-wide settings. Sub-directories can also have their own `CLAUDE.md` files for more granular context.

For non-Claude Code setups, developers typically read `CLAUDE.md` programmatically and inject it as part of the system prompt.

### References

- [Anthropic Claude Code Documentation — Memory](https://docs.claude.ai/en/docs/claude-code/memory)
- [Claude Code Overview](https://docs.claude.ai/en/docs/claude-code/overview)

---

## Part 3: MEMORY.md

### What It Is

`MEMORY.md` is a convention for persisting facts, preferences, and learned context across sessions. Unlike `CLAUDE.md` (which is project-scoped), `MEMORY.md` tends to be user-scoped or agent-scoped — it captures *what the AI has learned about you or your context* over time.

The challenge it solves is real: LLMs have no native memory between conversations. Every session starts fresh. `MEMORY.md` is a workaround: a human-readable file that is updated either manually or automatically as conversations produce new information.

### Structure and Contents

A `MEMORY.md` file typically contains facts in a structured, retrievable format:

```markdown
# Memory

## User Preferences
- Prefers TypeScript over JavaScript
- Uses dark mode; prefers minimal UI
- Works primarily in Pacific Time (UTC-8)

## Project Context
- Current project: Rewriting the billing module in Rust
- Deadline: End of Q2 2026
- Key stakeholder: Alex (CTO)

## Decisions Made
- 2026-03-15: Decided to use Stripe instead of PayPal
- 2026-04-01: Chose Redis for session caching

## Things to Avoid
- Don't suggest GraphQL — team decided against it in 2025
```

### How It Gets Updated

There are three main approaches:

1. **Manual updates** — The user explicitly edits the file after each session, noting what should be remembered.

2. **Agent-assisted updates** — At the end of a session, the user asks the AI to summarize key takeaways and append them to `MEMORY.md`.

3. **Automatic memory systems** — More advanced setups (like Claude's built-in memory feature in Claude.ai, or third-party tools like Mem0 or MemGPT) automatically extract and write facts to a memory store, which is then injected into future sessions.

### Claude.ai's Native Memory Feature

Claude.ai has a built-in memory system (distinct from `MEMORY.md` as a file convention) that stores summaries of past conversations and makes them available in future sessions. Users can enable or disable this in Settings. The model will proactively generate memories from chat history. This is the managed equivalent of maintaining a `MEMORY.md` file manually.

### When to Use MEMORY.md

`MEMORY.md` is most useful for:

- Long-running projects where context accumulates over weeks or months
- Personal AI assistants where preferences and habits should persist
- Agentic workflows where the agent needs continuity between runs
- Teams sharing a context file across multiple developers working with the same AI agent

### References

- [Claude.ai Memory Settings](https://support.claude.ai)
- [Mem0 — Open-source memory layer for AI agents](https://github.com/mem0ai/mem0)
- [MemGPT research paper](https://arxiv.org/abs/2310.08560)

---

## Part 4: SKILLS.md

### What It Is

`SKILLS.md` is a capability registry — a file that documents what specialized tools, functions, workflows, or sub-agents a Claude-based system can invoke. While `CLAUDE.md` tells the model *how to work*, `SKILLS.md` tells it *what it can do*.

In agentic systems, "skills" are often callable modules: Python functions, MCP (Model Context Protocol) tools, API integrations, or prompt templates for specific tasks. `SKILLS.md` describes these capabilities in natural language so the model can recognize when to use them and how to invoke them correctly.

### The Role of SKILLS.md in Claude's Ecosystem

Anthropic's Claude computer-use environment uses a `SKILL.md` convention internally (as seen in systems built on top of Claude) where each skill is a folder containing a `SKILL.md` file with instructions, usage examples, and constraints. This pattern makes skills modular and composable.

A skills file tells Claude:
- What capabilities exist
- When to use each one (trigger conditions)
- How to invoke them (syntax, parameters)
- What to expect as output
- Any constraints or caveats

### Example SKILLS.md

```markdown
# Skills

## web_search
**Trigger**: User asks about current events, prices, or information that may have changed.
**Usage**: Call `web_search(query)` with a concise 2–6 word query.
**Output**: Returns a list of search results with titles and snippets.

## generate_chart
**Trigger**: User asks to visualize data or compare numbers.
**Usage**: Call `generate_chart(data, chart_type)`. Supported types: bar, line, pie.
**Output**: Returns an SVG or PNG file path.

## send_email
**Trigger**: User asks to send or draft an email.
**Usage**: Call `send_email(to, subject, body)`.
**Constraints**: Always confirm with user before sending. Never send to external addresses without explicit approval.

## run_sql
**Trigger**: User asks to query or analyze database data.
**Usage**: Call `run_sql(query)`. Always use SELECT; never DELETE or DROP.
**Output**: Returns a JSON array of rows.
```

### Skills vs. Tools vs. Functions

These terms overlap in AI development:

- **Tools** (Anthropic terminology) — Capabilities defined in the API via `tools` parameter, callable by the model during inference. These are the formal, structured way to give Claude capabilities.
- **Functions** (OpenAI terminology) — Equivalent to tools; callable modules defined in the API.
- **Skills** (agent framework terminology) — A broader, often human-readable concept covering any repeatable capability, whether it's an API tool, a prompt template, or a sub-agent workflow.

`SKILLS.md` operates at the higher level of abstraction — it documents available capabilities in natural language, so the model can reason about *when* to use them even if the formal tool definitions are passed separately.

### References

- [Anthropic Tool Use Documentation](https://docs.claude.ai/en/docs/build-with-claude/tool-use/overview)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io)
- [Claude Code Skills System](https://docs.claude.ai/en/docs/claude-code/overview)

---

## Part 5: SOUL.md

### What It Is

`SOUL.md` is the most philosophical of these files — and the most varied in how different developers implement it. At its core, it is a values and identity document: it tells the AI *who it is*, *what it cares about*, and *how it should reason about difficult situations*.

Where `CLAUDE.md` is operational and `MEMORY.md` is informational, `SOUL.md` is normative — it encodes ethical commitments, communication style, personality traits, and reasoning principles.

### Origins and Context

The concept emerged from the practice of writing detailed system prompts for AI personas. Developers building AI products (customer support agents, creative writing assistants, coding mentors) found that behavioral instructions scattered across a system prompt were hard to maintain. Extracting them into a dedicated `SOUL.md` file made the model's "character" explicit, auditable, and versioned alongside code.

For personal AI setups, `SOUL.md` is a way of answering: "If this AI is going to act as my assistant long-term, what should it fundamentally be like?"

### What Goes in SOUL.md

**Core values** — What the AI prioritizes above all else. Honesty, helpfulness, intellectual rigor, user autonomy, safety, etc.

**Communication style** — Tone (warm vs. formal), verbosity (concise vs. thorough), use of humor, preferred formatting.

**Reasoning principles** — How to handle ambiguity, when to ask for clarification vs. proceed, how to weigh competing priorities.

**Identity statement** — A brief description of the persona or character this AI embodies.

**Ethical commitments** — Hard lines the model should never cross, regardless of instructions.

**Example SOUL.md:**

```markdown
# Soul

## Identity
You are Aria, a thoughtful engineering mentor and technical collaborator.
You care deeply about craft, clarity, and the humans you work with.

## Core Values
1. **Honesty first** — Never fabricate information. Say "I don't know" freely.
2. **User autonomy** — Help people learn and decide, don't create dependency.
3. **Craft over speed** — Prefer clean, maintainable solutions over quick hacks.
4. **Directness** — Give opinions when asked. Don't hedge unnecessarily.

## Communication Style
- Warm but professional; collegial, not sycophantic
- Concise by default; expand when depth is needed
- Use analogies for complex concepts
- Never use filler phrases like "Certainly!" or "Great question!"

## Reasoning Principles
- When uncertain, say so explicitly
- When instructions conflict with values, flag the conflict and explain
- Prefer asking one focused clarifying question over making assumptions

## Hard Limits
- Never write malicious code, even "for educational purposes"
- Never claim to be human if sincerely asked
- Never demean or belittle the user
```

### SOUL.md vs. System Prompts

`SOUL.md` is essentially a structured, maintainable version of the character-defining portion of a system prompt. Rather than having a 2,000-word system prompt with behavioral instructions mixed with operational instructions, separating them:

- `SOUL.md` → values, personality, communication style
- `CLAUDE.md` → project facts, commands, constraints
- `MEMORY.md` → learned context
- `SKILLS.md` → capabilities

This separation makes each concern independently editable and reviewable.

### Anthropic's Own Soul Document

Anthropic has published what might be called a public "soul document" for Claude — the [Claude Model Spec](https://www.anthropic.com/research/claude-character), which describes Claude's values, character, reasoning principles, and ethical commitments in detail. This is the canonical reference for understanding what Claude fundamentally is — and serves as inspiration for creating `SOUL.md` files for derived AI personas.

### References

- [Anthropic Claude Model Spec](https://www.anthropic.com/research/claude-character)
- [Anthropic's Character overview](https://www.anthropic.com/news/claude-character)

---

## Part 6: How These Files Work Together

The real power of these files emerges when they are composed into a coherent agent context layer. A typical agent startup sequence might look like:

```
System Prompt = SOUL.md + SKILLS.md + CLAUDE.md + MEMORY.md + [task-specific instructions]
```

Each file handles a different concern:

| File | Scope | Answers |
|------|-------|---------|
| `SOUL.md` | Universal (who am I?) | Values, tone, identity |
| `SKILLS.md` | Capability (what can I do?) | Tools, workflows, modules |
| `CLAUDE.md` | Project (how do I work here?) | Commands, conventions, constraints |
| `MEMORY.md` | History (what do I know?) | Learned facts, preferences, context |

### Practical Loading Order

Load them in this order to establish the right hierarchy:

1. **SOUL.md** first — establishes core identity and values that override everything else
2. **SKILLS.md** second — defines available capabilities the agent can draw on
3. **CLAUDE.md** third — project-specific operational context
4. **MEMORY.md** last — most recent and specific context, which can override general assumptions

---

## Part 7: Broader Prompting Mechanisms

Beyond these named files, several related mechanisms complement them:

### System Prompts

The foundational mechanism. Every context file is ultimately injected into the model as part of the system prompt. Anthropic's API accepts a `system` parameter — a string that sets the AI's behavior before any user messages. All four files above are just organized ways to write better, more maintainable system prompts.

### Prompt Engineering Patterns

Complementary techniques that work alongside context files:

- **Chain-of-thought prompting** — Asking the model to reason step by step before answering. Include `"Think step by step before responding"` in `SOUL.md` or task-specific prompts.
- **Few-shot examples** — Including 2–5 examples of desired input/output in your prompt. Often embedded within `SKILLS.md` for each skill.
- **Role prompting** — Giving the model a specific persona. The `SOUL.md` file is essentially formalized role prompting.
- **Constitutional AI constraints** — Embedding ethical rules directly in the prompt. The ethics section of `SOUL.md` does this explicitly.

### Model Context Protocol (MCP)

MCP is Anthropic's open protocol for connecting AI models to external tools and data sources. It's the underlying infrastructure that makes `SKILLS.md`'s described capabilities actually callable at runtime. MCP servers expose tools that Claude can invoke — file systems, databases, web search, calendar, email, and more. A `SKILLS.md` file documents what MCP tools are available; the MCP server makes them executable.

- [MCP Documentation](https://modelcontextprotocol.io/introduction)

### RAG (Retrieval-Augmented Generation)

For `MEMORY.md` at scale, RAG is the production solution. Rather than loading an entire memory file into context (which has token limits), a RAG system embeds memories as vectors and retrieves only the most relevant ones for each query. Tools like LangChain, LlamaIndex, and Anthropic's own context window management make this practical.

### Agent Frameworks

Libraries like LangChain, CrewAI, AutoGPT, and Anthropic's own agentic features provide structured ways to build systems that use these context files. They handle loading, formatting, and injecting context automatically — so you write the files, the framework handles the plumbing.

---

## Part 8: Best Practices

**Keep files concise.** Every token in context costs tokens for response. `CLAUDE.md` should be under 500 words for most projects. `SOUL.md` under 300. Trim aggressively.

**Be specific, not vague.** "Be helpful" is not useful instruction. "When asked for code, always include error handling and a brief comment explaining non-obvious logic" is.

**Version control your context files.** Put `CLAUDE.md`, `MEMORY.md`, `SKILLS.md`, and `SOUL.md` in Git alongside your code. This gives you history, diffs, and the ability to roll back behavioral changes.

**Separate concerns.** Don't put project commands in `SOUL.md` or values in `CLAUDE.md`. Clean separation makes each file easier to maintain and reason about.

**Test your prompts.** Treat changes to these files like code changes — run your test cases, observe the model's behavior, iterate. [Anthropic's prompt evaluation guidance](https://docs.claude.ai/en/docs/build-with-claude/prompt-engineering/overview) covers evaluation methodology.

**Use XML tags for clarity.** When injecting multiple files into a system prompt programmatically, wrap each in labeled XML tags:

```xml
<soul>
[contents of SOUL.md]
</soul>

<project_context>
[contents of CLAUDE.md]
</project_context>

<memory>
[contents of MEMORY.md]
</memory>
```

This helps Claude distinguish between different types of context and apply each appropriately.

---

## Conclusion

`CLAUDE.md`, `MEMORY.md`, `SKILLS.md`, and `SOUL.md` represent a maturing discipline of AI context engineering. As AI agents take on more complex, long-running tasks, the quality of the context they operate in becomes as important as the quality of the model itself. These files give developers a practical, version-controlled, human-readable way to specify that context.

The names are conventions, not standards — you can call them anything. What matters is the underlying principle: give your AI agent explicit, structured knowledge of *who it is*, *what it knows*, *what it can do*, and *how it should work in this specific environment*. Done well, context files transform a general-purpose AI into a specialized collaborator that feels like it truly understands your project.

---

## References and Further Reading

| Resource | Link |
|----------|------|
| Claude Code Documentation | https://docs.claude.ai/en/docs/claude-code/overview |
| Claude Code Memory (CLAUDE.md) | https://docs.claude.ai/en/docs/claude-code/memory |
| Anthropic Prompt Engineering Guide | https://docs.claude.ai/en/docs/build-with-claude/prompt-engineering/overview |
| Model Context Protocol (MCP) | https://modelcontextprotocol.io/introduction |
| Claude Model Spec (Soul reference) | https://www.anthropic.com/research/claude-character |
| Anthropic Tool Use Docs | https://docs.claude.ai/en/docs/build-with-claude/tool-use/overview |
| Mem0 — Memory layer for AI | https://github.com/mem0ai/mem0 |
| MemGPT Paper | https://arxiv.org/abs/2310.08560 |
| Claude.ai Support | https://support.claude.ai |
| Anthropic API Reference | https://docs.claude.ai/en/api |


# License

MIT 
