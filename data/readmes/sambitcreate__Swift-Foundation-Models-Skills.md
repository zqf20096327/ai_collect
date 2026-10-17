# Apple Foundation Models Skills

A collection of Agent Skills for building iOS/macOS applications with Apple's [Foundation Models](https://developer.apple.com/documentation/foundationmodels) framework (Apple Intelligence). These skills are designed for zero-friction AI-assisted development with on-device models.

Skills follow the [Agent Skills](https://github.com/anthropics/agent-skills) format.

## Inspiration

This project is directly inspired by:
- [Foundation-Models-Framework-Example](https://github.com/rudrankriyam/Foundation-Models-Framework-Example) by [@rudrankriyam](https://github.com/rudrankriyam) — a comprehensive example project for Apple's Foundation Models framework
- [Apple Foundation Models documentation](https://developer.apple.com/documentation/FoundationModels) — the official Apple developer reference

## Available Skills

### Core Session Management

- **apple-foundation-models-setup-availability** - Check model availability and set up Foundation Models
- **apple-foundation-models-session-patterns** - Create sessions for single-turn and multi-turn conversations
- **apple-foundation-models-streaming-chat-context** - Stream responses and manage context window
- **apple-foundation-models-token-budget-management** - Count tokens and manage context budgets

### Structured Generation

- **apple-foundation-models-structured-generation** - Generate type-safe Swift structs with @Generable
- **apple-foundation-models-dynamic-schemas** - Build schemas dynamically at runtime

### Tools & System Integration

- **apple-foundation-models-custom-tools** - Build custom tools the model can call
- **apple-foundation-models-system-tools** - Use built-in system tools (weather, contacts, calendar)
- **apple-foundation-models-health-assistant** - HealthKit integration with custom tools

### Context & Conversation

- **apple-foundation-models-conversation-context-builder** - Extract context and build continuation prompts
- **apple-foundation-models-swiftdata-persistence** - Persist conversations with SwiftData

### Error Handling & Tuning

- **apple-foundation-models-error-recovery** - Handle context overflow, refusals, rate limits
- **apple-foundation-models-generation-tuning** - Tune temperature, sampling, seeds, token limits

### Multimodal & Specialized

- **apple-foundation-models-voice-assistant** - Speech recognition and TTS integration
- **apple-foundation-models-multilingual** - Handle multiple languages
- **apple-foundation-models-rag-pipeline** - Retrieval-augmented generation with document indexing

### Integration & UX

- **apple-foundation-models-app-patterns** - MVVM architecture patterns
- **apple-foundation-models-ui-design-system** - Reusable UI components
- **apple-foundation-models-siri-shortcuts-integration** - Siri Shortcuts and App Intents
- **apple-foundation-models-feedback-sentiment-api** - Collect user feedback per response

### Learning & Development

- **apple-foundation-models-playground-learning** - Runnable learning examples
- **apple-foundation-models-prompt-builder-patterns** - @PromptBuilder composition patterns

## Installation

### Via skills CLI (recommended)

```bash
npx skills add sambitcreate/Swift-Foundation-Models-Skills
```

This installs all 22 skills to your local agent directories and works with 40+ AI coding agents (Claude Code, Cursor, Codex, Windsurf, and more).

### Manual installation

Clone the repository and run the installer:

```bash
git clone https://github.com/sambitcreate/Swift-Foundation-Models-Skills.git
cd Swift-Foundation-Models-Skills
node bin/cli.js
```

This copies all skills to:
- `~/.claude/skills/` (Claude Code)
- `~/.agents/skills/` (OpenAI Agents / OpenAI Codex)

## Usage

Skills are automatically available once installed. The agent will use them when relevant tasks are detected.

All skills support the **"afm"** trigger keyword:

```
"Use the apple-foundation-models-session-patterns skill"
"Use afm session-patterns"
"Use the afm structured-generation skill"
```

**Examples:**

```
Set up Foundation Models in my iOS app and check device availability
```

```
Create a streaming chat interface with context management
```

```
Build a custom tool that searches my app's database
```

```
Add SwiftData persistence for conversation history
```

## Skill Structure

Each skill contains:

```
skills/
└── apple-foundation-models-xxx/
    ├── SKILL.md          - Instructions for the agent
    ├── agents/
    │   └── openai.yaml   - OpenAI agent configuration
    └── references/
        └── guide.md      - Code examples and implementation details
```

## Requirements

- **iOS/macOS**: 26.0+
- **Device**: Apple Silicon with Apple Intelligence enabled
- **Framework**: `import FoundationModels`

## License

MIT
