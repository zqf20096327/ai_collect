# AgenticPod

An agentic product lifecycle accelerator. Give it a product idea, and it runs a staged pipeline across four agent roles (PM, Research, Design, Engineering) to produce structured artifacts — PRD, research plan, prototype spec, tech spec, and backlog.

**Claude Code is the UI.** No custom CLI. You interact conversationally, and Claude Code drives the pipeline.

## Quick Start

1. Install dependencies:
   ```bash
   npm install
   ```

2. Set your LLM API key:
   ```bash
   export ANTHROPIC_API_KEY="your-key"
   ```

3. Open the project in Claude Code and describe your product idea. Claude Code will use the CLAUDE.md instructions to drive the pipeline.

## How It Works

1. You describe a product idea to Claude Code
2. Claude Code initializes a project and creates `idea.json`
3. Each stage runs an LLM-powered agent that reads prior artifacts and produces new ones
4. Between stages, Claude Code shows you a summary and asks to proceed
5. All artifacts are written to `./artifacts/<project_id>/`

### Pipeline Stages

| Stage | Agent | Output |
|-------|-------|--------|
| 0: Intake | — | `idea.json` |
| 1: PM Framing | PM | `PRD.md` |
| 2: Research | Research | `Research.md` |
| 3: Design | Design | `PrototypeSpec.md`, `FigmaLink.json` |
| 4: Engineering | Engineering | `TechSpec.md`, `Backlog.md` |
| 5: Iterate | — | Updated specs, `IterationLog.md` |

## Configuration

### LLM Provider

Edit `config/llm.json` to switch between Anthropic and OpenAI:

```json
{
  "provider": "anthropic",
  "model": "claude-sonnet-4-5-20250929",
  "apiKeyEnvVar": "ANTHROPIC_API_KEY"
}
```

### Figma MCP (Optional)

See `docs/figma-mcp-setup.md` for instructions on connecting Figma for prototype round-trips.

## Architecture

```
src/
  index.ts              # Public API exports
  types/                # TypeScript types and Zod schemas
  providers/            # LLM provider interface (Anthropic, OpenAI)
  agents/               # Agent roles (PM, Research, Design, Engineering)
  conductor/            # Pipeline orchestrator and state management
  artifacts/            # File-based artifact store
  templates/            # Artifact template definitions
  quality/              # Validation and quality checks
  figma/                # Figma MCP config and snapshot sync
```

## Modes

- **Mode A (default):** Human approves each stage transition via conversation
- **Mode B:** Auto-advances if quality checks pass (`autonomy: 'medium'`)
