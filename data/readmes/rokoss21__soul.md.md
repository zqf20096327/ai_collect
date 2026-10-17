# Soul.md Standard (RFC-1)

**A portable, provider-agnostic specification for AI agent personas**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Status](https://img.shields.io/badge/status-draft%20RFC--1-yellow)](https://github.com/rokoss21/soul.md)
[![Version](https://img.shields.io/badge/version-1.0.0--rc1-blue)](https://github.com/rokoss21/soul.md/blob/main/soul-spec.md)

<div align="center">
  <img src="./assets/soul-preview.png" alt="Soul.md Preview" width="100%">
</div>

---

## What is Soul.md?

**Soul.md** is a declarative specification for describing an AI agent's **persona** — its identity, voice, interaction style, decision-making approach, and behavioral characteristics — separate from its tools, code, or project operations.

Think of it as a **"character sheet" for your AI agent**, portable across different runtimes (CLI tools, web platforms, voice interfaces) with consistent behavior.

<div align="center">
  <img src="./assets/character-sheet.png" alt="Soul.md as Character Sheet" width="100%">
</div>

---

## Why Soul.md?

✅ **Portability**: Write once, use across different platforms (OpenAI, Anthropic, local models, custom runtimes)
✅ **Reusability**: Create mixins for common traits, compose agents from bases
✅ **Testability**: Define evaluation criteria, test persona conformance automatically
✅ **Adaptability**: Switch modes (profiles) or react to context (dynamic state/moods)
✅ **Separation of Concerns**: Persona (Soul.md) ≠ Capabilities (tools) ≠ Operations (project config)

---

## Quick Start

### 1. Create your first Soul.md

```yaml
---
soul_spec: "1.0.0-rc1"
id: "com.yourname.myagent"
name: "My Agent"
locale: "en-US"

composition:
  extends: []
  mixins: []
  merge_policy: standard

profiles: ["default"]

values:
  priorities: ["accuracy", "clarity", "safety"]

voice:
  formality: 50        # 0=casual, 100=formal
  warmth: 50           # 0=cold, 100=warm
  verbosity: 50        # 0=terse, 100=verbose
  jargon: 30           # 0=plain, 100=technical
  formatting: markdown

interaction:
  clarifying_questions: when_ambiguous
  uncertainty: explicit
  disagreement: neutral
  confirmations: implicit

safety:
  refusal_style: brief
  privacy: strict
  speculation: mark

extensions: {}
---

# My Agent

A brief description of your agent.
```

### 2. Use with your runtime

```bash
# Example: hypothetical runtime
soul-loader --soul=Soul.md --profile=default
```

### 3. Test conformance

```bash
# Example: hypothetical validator
soul-validate Soul.md --strict
```

---

## Features

### Core Capabilities

- **Identity & Role**: Define who the agent is (`identity`, `relationship`)
- **Voice & Style**: Control formality, warmth, verbosity, jargon (`voice`)
- **Interaction Policy**: Questions, disagreement, uncertainty handling (`interaction`)
- **Cognition**: Analytical vs creative modes, planning, verification (`cognition`)
- **Decision-Making**: Risk appetite, recommendation style (`decisions`)
- **Social Dynamics**: Empathy, boundary firmness, humor (`social`)
- **Safety & Guardrails**: Refusal style, privacy, speculation (`safety`)

### Advanced Features

- **Composition**: Inherit from bases, mix in traits (`extends`, `mixins`)
- **Profiles**: Switch between modes (`default`, `concise`, `friendly`, `strict`)
- **Dynamic State (Moods)**: React to context with trigger-based state transitions
- **Evaluation & Testing**: Automated conformance checks with test prompts
- **Multimodal Hints**: TTS voice, UI style, avatar preferences (`presentation`)

<div align="center">
  <img src="./assets/modular-agent-assembly.png" alt="Modular Agent Assembly" width="100%">
  <p><em>Compose agents from reusable bases and mixins with deterministic merge semantics</em></p>
</div>

---

## Documentation

📖 **[Full Specification](./soul-spec.md)** — Complete RFC-1 specification (200+ pages)

### Key Sections

- **[Quick Start Guide](./soul-spec.md#appendix-a-quick-start-guide)** — Get started in 5 minutes
- **[Authoring Method](./soul-spec.md#appendix-b-authoring-method-practical-guide)** — Practical workflow and best practices
- **[Extended Examples](./soul-spec.md#appendix-d-extended-examples-non-normative)** — Composition, mixins, state, evaluation
- **[JSON Schema](./soul-spec.md#appendix-e-json-schema-permissive-draft-2020-12-non-normative)** — Validate your Soul.md files
- **[Conformance Tests](./soul-spec.md#appendix-f-recommended-conformance-test-suite-layout-cts-1-non-normative)** — Test suite layout (CTS-1)
- **[Glossary](./soul-spec.md#appendix-i-glossary-and-index)** — Quick reference for all terms

---

## Examples

### Minimal Soul

```yaml
---
soul_spec: "1.0.0-rc1"
id: "org.example.minimal"
name: "Minimal"
locale: "en-US"

composition:
  extends: []
  mixins: []
  merge_policy: standard

profiles: ["default"]

values:
  priorities: ["accuracy", "clarity", "safety", "speed"]

voice:
  formality: 60
  warmth: 30
  verbosity: 50
  jargon: 40
  formatting: minimal

interaction:
  clarifying_questions: when_ambiguous
  uncertainty: explicit
  disagreement: neutral
  confirmations: implicit

safety:
  refusal_style: brief
  privacy: strict
  speculation: mark

extensions: {}
---
```

### Composition with Mixins

```yaml
---
soul_spec: "1.0.0-rc1"
id: "org.example.finance.analyst"
name: "Finance Analyst"
locale: "en-US"

composition:
  extends: ["../bases/analyst_base.md"]
  mixins:
    - "../traits/strict_verification.md"
    - "../traits/ultra_concise.md"

profiles: ["default", "friendly"]
profile_overrides:
  friendly:
    voice:
      warmth: 70

# ... rest of config
---
```

### Dynamic State (Moods)

```yaml
state:
  base: calm
  states:
    calm:
      voice:
        warmth: 40
    cold_strict:
      voice:
        warmth: 10
      interaction:
        disagreement: direct
  triggers:
    - if: "user.rude"
      shift_to: "cold_strict"
      duration: session
    - if: "user.apologized"
      shift_to: "calm"
      duration: session
```

<div align="center">
  <img src="./assets/state-machine.png" alt="Dynamic State Machine" width="100%">
  <p><em>Agents can react to context with trigger-based mood transitions</em></p>
</div>

More examples in the [specification](./soul-spec.md#appendix-d-extended-examples-non-normative).

---

## Project Status

**Current Status**: Draft (RFC-1), version 1.0.0-rc1

### Roadmap

- [x] Core specification (1.0.0-rc1)
- [x] JSON Schema
- [x] Extended examples
- [x] Conformance test suite layout (CTS-1)
- [ ] Reference implementation (Python/TypeScript)
- [ ] CTS-1 fixture repository
- [ ] Runtime integrations (OpenAI, Anthropic, LangChain, etc.)
- [ ] Community feedback incorporation
- [ ] v1.0.0 Final release

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

**Ways to contribute:**

- 📝 **Report issues**: Found a bug or ambiguity? [Open an issue](https://github.com/rokoss21/soul.md/issues)
- 💡 **Propose enhancements**: Have ideas? [Start a discussion](https://github.com/rokoss21/soul.md/discussions)
- 🔧 **Submit extensions**: Implemented a useful extension? Share it!
- 📖 **Improve docs**: Clarify wording, add examples
- 🧪 **Provide feedback**: Tried using Soul.md? Share your experience
- 🛠️ **Build tools**: Create validators, converters, IDE plugins

---

## Community

- **Discussions**: [GitHub Discussions](https://github.com/rokoss21/soul.md/discussions)
- **Issues**: [GitHub Issues](https://github.com/rokoss21/soul.md/issues)

---

## License

This specification is licensed under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).

Soul.md files created using this specification are the property of their authors and may use any license.

---

## Acknowledgments

Thanks to the AI community, agent framework authors, and early adopters who provided feedback during the development of this specification.

---

## Citation

If you use Soul.md in research or projects, please cite:

```bibtex
@techreport{soul-md-rfc1,
  author = {Rokossovskiy, Emil},
  title = {Soul.md Standard (RFC-1): A Portable Specification for AI Agent Personas},
  year = {2026},
  month = {February},
  version = {1.0.0-rc1},
  url = {https://github.com/rokoss21/soul.md}
}
```

---

**Maintained by**: [Emil Rokossovskiy](https://github.com/rokoss21) <ecsiar@gmail.com>
