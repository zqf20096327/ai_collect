# Quizzer

[![PyPI version](https://img.shields.io/pypi/v/quizzer-ai.svg)](https://pypi.org/project/quizzer-ai/)
[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

Quizzer turns PDFs into interactive, Duolingo-style courses you can study from the terminal.

It combines PDF ingestion, question generation, spaced repetition, adaptive difficulty, and lightweight gamification so a static document becomes something you can actually practice.

Built on the five pillars of the Duolingo Method: learn by doing, personalized learning, focus on what matters, stay motivated, feel the delight.

- Generate full courses from textbooks, manuals, lecture notes, or handouts
- Study with seven question types, from easy recognition to free recall
- Revisit the right material at the right time with SM-2 scheduling
- Chat with an in-context tutor after each question
- Keep momentum with XP, streaks, and lesson unlocking

## Features

- **PDF to course** -- Drop in any PDF and generate a full course with 7 question types (true/false, multiple choice, matching, sorting, fill-in-the-blank, ordering, free recall)
- **Spaced repetition** -- SM-2 algorithm schedules reviews so you see material right before you'd forget it
- **Adaptive difficulty** -- Tracks your ability and picks questions in your zone of proximal development
- **Scaffolded learning** -- Questions progress from receptive (true/false) to productive (free recall) within each session
- **Gamification** -- XP, streaks, levels, and LLM-generated effort-based praise
- **Tutor chat** -- After any answer, type `/chat` to open a multi-turn conversation with the LLM about the question, with the source page images as context
- **Review mode** -- Interleaves due questions across completed lessons, with mistakes weighted 2x
- **Any LLM backend** -- Works with any OpenAI-compatible API endpoint

## Requirements

- Python 3.14+
- An OpenAI-compatible LLM endpoint (local or remote)

## Installation

Install from PyPI:

```bash
pip install quizzer-ai
```

Install from source:

```bash
git clone https://github.com/suncloudsmoon/quizzer.git
cd quizzer
pip install .
```

## Quick start

```bash
quizzer
```

On first launch, Quizzer prompts you for an OpenAI-compatible endpoint, API key, and model name. After that, these commands drive the flow:

| Command     | Description                                        |
|-------------|----------------------------------------------------|
| `/create`   | Generate a course from a PDF                       |
| `/study`    | Study an existing course (in-progress shown first) |
| `/settings` | View or change LLM settings                        |
| `/help`     | List available commands                             |

During a study session, after answering a question:

| Command  | Description                                      |
|----------|--------------------------------------------------|
| `/chat`  | Open a multi-turn tutor chat about this question |
| `/done`  | Exit tutor chat and return to the quiz           |

## How it works

1. **Course generation** (`/create`): Renders each PDF page as an image, sends it to a vision-capable LLM to triage and summarize content, then generates questions with calibrated difficulty. The result is a read-only `course.json`.

2. **Study sessions** (`/study`): Builds a session from due questions, filtered by adaptive difficulty and scaffolded from easy/receptive to hard/productive. After each answer you rate your confidence; the system updates your spaced repetition schedule and ability estimate accordingly. You can then type `/chat` to discuss the question with an LLM tutor that has the source page images as context.

3. **Mistake resurfacing**: Incorrect answers resurface at the end of the session for a second attempt.

4. **Lesson progression**: Lessons unlock linearly. Achieving 70%+ accuracy completes a lesson and unlocks the next.

5. **Review**: Once multiple lessons are complete, review mode interleaves due questions across all of them.

## Why it feels different

Most PDF study tools stop at summarization. Quizzer is built around active recall instead:

- It asks you to answer, not just read
- It adapts question difficulty to your current ability
- It brings mistakes back before they disappear from memory
- It keeps each lesson moving from recognition toward recall
- It lets you open a tutor chat exactly when confusion happens

## Example setup

This project has been tested with [LM Studio](https://lmstudio.ai/) using the `lmstudio-community/ministral-3-8b-reasoning-2512` model for question generation. Note that course generation can take a long time depending on your hardware -- for a long book (~1000 pages), expect 12 hours or more.

## Data storage

Quizzer uses [platformdirs](https://github.com/platformdirs/platformdirs) to store files in OS-standard locations:

| What | Path |
|------|------|
| Config | `<config_dir>/quizzer/config.json` |
| Courses | `<data_dir>/quizzer/courses/<course-id>/course.json` |
| Page images | `<data_dir>/quizzer/courses/<course-id>/images/` |
| Learning progress | `<data_dir>/quizzer/progress/<course-id>.json` |

Typical platform directories:

| Platform | Config dir | Data dir |
|----------|-----------|----------|
| macOS | `~/Library/Application Support/quizzer` | `~/Library/Application Support/quizzer` |
| Linux | `~/.config/quizzer` | `~/.local/share/quizzer` |
| Windows | `C:\Users\<user>\AppData\Local\suncloudsmoon\quizzer` | `C:\Users\<user>\AppData\Local\suncloudsmoon\quizzer` |

## Project structure

```
src/quizzer/
  app.py              CLI entry point, config, LLM setup
  quiz_creator.py     PDF -> course JSON (offline, run once per document)
  quiz_handler.py     Serves questions at runtime
  learner_state.py    Per-learner runtime state (single JSON file)
  paths.py            Platform-specific paths via platformdirs
```

## Dependencies

- [Pydantic](https://docs.pydantic.dev/) -- data models
- [LlamaIndex](https://www.llamaindex.ai/) -- LLM interface and structured output
- [PyMuPDF](https://pymupdf.readthedocs.io/) -- PDF page rendering
- [platformdirs](https://github.com/platformdirs/platformdirs) -- platform-specific config/data directories
- [tqdm](https://github.com/tqdm/tqdm) -- progress bars during course generation
