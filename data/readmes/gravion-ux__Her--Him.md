# Her & Him - AI Companion Catalogues

[![CI](https://github.com/gravion-ux/Her--Him/actions/workflows/ci.yml/badge.svg)](https://github.com/gravion-ux/Her--Him/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/gravion-ux/Her--Him/branch/main/graph/badge.svg)](https://codecov.io/gh/gravion-ux/Her--Him)

![Demo](docs/demo.png)

*Demo: The companion catalogue — every personality listed from the CLI.*

A unified platform with a complete catalogue of AI personalities for boys and girls, featuring natural multilingual voice generation and mood-driven emotional dynamics.

## Overview

**Her** - 24 female AI companion personalities  
**Him** - 24 male AI companion personalities

Each persona is a complete Character Card v3 document with deterministic, explainable affect engine backing.

## Features

- **Complete personality catalogues**: 48 distinct personas across two parallel catalogues
- **Deterministic affect engine**: Predictable mood and emotion evolution turn-to-turn
- **Mood-driven voice**: Voice parameters map directly to affect state and personality traits
- **Multilingual support**: 332 voices across English, Mandarin, Japanese, Korean, Spanish, Portuguese, Hindi, and more
- **Structural guardrails**: Adult scope validated at load, no-minors policy, consent safeguards
- **Zero runtime dependencies**: Core package works without any external services

## Installation

```bash
pip install herhim
```

## Usage

### CLI

```bash
# List all personas
herhim catalogue

# Show a specific persona
herhim show --persona-id her-001-sassy

# Start interactive chat
herhim chat --catalogue her --provider offline

# List available voices
herhim voices --engine samples

# Run diagnostics
herhim doctor
```

### Python API

```python
from herhim.catalog.registry import PersonaRegistry
from herhim.experience.session import Session

# Load the registry
registry = PersonaRegistry.load()

# Get a persona
persona = registry.get("her-001-sassy")

# Create a session
session = Session(persona=persona)

# Have a conversation
result = session.turn("Hello!")
print(result.text)
```

### Web Server

```bash
herhim serve --port 8080
# Open http://localhost:8080
```

## Architecture

The project follows the **affect-first** design:

1. **Affect Engine**: Tracks valence, arousal, assertion, tenderness
2. **Mood Derivation**: 18 mood labels derived from affect + traits + events
3. **Personality Traits**: 11 axes shaping how events are felt
4. **Relationship State**: Trust, intimacy, tension, jealousy, dependency, commitment
5. **Voice Layer**: Maps mood + affect to speech parameters

## Catalogue Structure

```
herhim/
├── src/herhim/
│   ├── affect/           # Emotion classification and mood derivation
│   ├── catalog/          # Persona loading, validation, quality
│   ├── experience/       # Session management, CLI, web surfaces
│   ├── guardrails/       # Adult scope, consent, IO policy, audit
│   ├── memory/           # Session memory storage and recall
│   ├── models/           # Core data models (Persona, Affect, etc.)
│   ├── providers/        # LLM provider implementations
│   ├── voice/            # Voice engine implementations
│   ├── data/             # Persona cards and samples
│   └── cli.py            # Command-line interface
├── tests/                # Test suite
├── scripts/              # Utility scripts
└── .github/workflows/    # CI/CD workflows
```

## Development

```bash
# Clone and install in editable mode
pip install -e .[dev]

# Run tests
pytest

# Run type checker
mypy src/herhim

# Run linter
ruff check src/herhim tests
```

## License

MIT License - see [LICENSE](LICENSE) for details.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.

## Acknowledgments

This project builds on the following open-source foundations:

- **Character Card v3 spec** (MIT) - Character card format specification
- **aegis** (MIT) - Provider router pattern
- **Piper TTS** (MIT) - Text-to-speech voices
- **Kokoro** (Apache-2.0) - Voice engine
- **Open-LLM-VTuber** (MIT) - Emotion-to-voice mapping

See [docs/ATTRIBUTION.md](docs/ATTRRIBUTION.md) for full attribution list.
