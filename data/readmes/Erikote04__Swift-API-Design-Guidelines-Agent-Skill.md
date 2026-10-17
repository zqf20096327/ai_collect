# Swift API Design Guidelines Skill

Expert guidance for any AI coding tool that supports the [Agent Skills open format](https://agentskills.io/home) - focused on Swift API naming, argument labels, terminology, documentation comments, and conventions.

This repository distills the Swift API Design Guidelines into actionable, concise references for agents and code review workflows.

## Who this is for
- Teams designing or reviewing Swift APIs and SDK surfaces
- Developers refactoring existing APIs for clarity at the point of use
- Anyone who wants APIs that read fluently and reduce ambiguity in call sites

## How to Use This Skill

### Option A: Using skills.sh (recommended)
Install this skill with a single command:

```bash
npx skills add https://github.com/Erikote04/Swift-API-Design-Guidelines-Agent-Skill --skill swift-api-design-guidelines-skill
```

Then use the skill in your AI agent, for example:
> Use the swift-api-design-guidelines skill and review this code for naming, argument labels, and API clarity.

### Option B: Claude Code Plugin

#### Personal Usage
To install this skill for your personal use in Claude Code:

1. Add the marketplace:

```bash
/plugin marketplace add Erikote04/Swift-API-Design-Guidelines-Agent-Skill
```

2. Install the skill:

```bash
/plugin install swift-api-design-guidelines@swift-api-design-guidelines-skill
```

#### Project Configuration
To automatically provide this skill to everyone working in a repository, configure `.claude/settings.json`:

```json
{
  "enabledPlugins": {
    "swift-api-design-guidelines@swift-api-design-guidelines-skill": true
  },
  "extraKnownMarketplaces": {
    "swift-api-design-guidelines-skill": {
      "source": {
        "source": "github",
        "repo": "Erikote04/Swift-API-Design-Guidelines-Agent-Skill"
      }
    }
  }
}
```

When team members open the project, Claude Code will prompt them to install the skill.

### Option C: Manual install
1. Clone this repository.
2. Install or symlink the `swift-api-design-guidelines-skill/` folder following your tool's official skills installation docs.
3. Use your AI tool as usual and ask it to use the `swift-api-design-guidelines` skill for API design tasks.

#### Where to Save Skills
Follow your tool's official documentation:
- Codex: [Where to save skills](https://developers.openai.com/codex/skills/#where-to-save-skills)
- Claude: [Using Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#using-skills)
- Cursor: [Enabling Skills](https://cursor.com/docs/context/skills#enabling-skills)

How to verify:
- Your agent should reference workflows/checklists in `swift-api-design-guidelines-skill/SKILL.md`
- It should then load the relevant file from `swift-api-design-guidelines-skill/references/` for topic-specific guidance

## What This Skill Offers

This skill gives your AI coding tool practical guidance for Swift API design. It can:

### Guide API Design Decisions
- Improve naming clarity at the point of use
- Apply argument-label rules based on grammar and meaning
- Enforce consistent mutating/nonmutating naming pairs
- Improve terminology use and reduce ambiguity

### Improve API Documentation
- Produce concise, useful declaration summaries
- Apply recognized symbol markup (`Parameter`, `Returns`, `Throws`, `Note`, etc.)
- Encourage documentation that matches actual API semantics

### Strengthen API Review Quality
- Catch overloaded APIs that become ambiguous with weak typing
- Flag redundant type words and role-unclear identifiers
- Encourage defaults and parameter ordering that improve readability

## What Makes This Skill Different

Non-opinionated: Focuses on API correctness and clarity, not architecture or folder structures.

Guidelines-first: Anchored in Swift API Design Guidelines semantics and established conventions.

Practical and concise: Optimizes for real review and implementation workflows, not theoretical style debates.

## Skill Structure
<!-- BEGIN REFERENCE STRUCTURE -->
```text
swift-api-design-guidelines-skill/
  SKILL.md
  references/
    argument-labels.md - Rules for first-argument labels, grammar, and conversion cases
    fundamentals.md - Core priorities and documentation-comment principles
    general-conventions.md - Complexity docs, casing, free-function exceptions, overload conventions
    parameters.md - Parameter naming, defaults, ordering, and file literal guidance
    promote-clear-usage.md - Naming clarity, omitted words, and role-based identifiers
    special-instructions.md - Tuple/closure naming and weak-type overload disambiguation
    strive-for-fluent-usage.md - Fluent call-site phrasing and mutating/nonmutating naming pairs
    use-terminology-well.md - Terms of art, abbreviations, and precedent
```
<!-- END REFERENCE STRUCTURE -->

## Contributing

Contributions are welcome! This repository follows the [Agent Skills open format](https://agentskills.io/home), which has specific structural requirements.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for:
- How to contribute improvements to `SKILL.md` and the reference files
- Format requirements and quality standards
- Pull request process

## About the author

Created by [Erik Sebastian de Erice Jerez](https://github.com/Erikote04).

## License

This skill is open-source under the MIT License. See [LICENSE](LICENSE) for details.
