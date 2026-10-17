# voxpen

Local voice-to-prompt tool. Speak, and get a clean, structured prompt
instead of a transcript of you rambling. Runs fully offline: local
Whisper for transcription, a local LLM (via Ollama) for the optional
prompt-restructuring step.

See `docs/PLAN.md` for the current architecture and build plan, and
`docs/FINDINGS.md` for the hardware/model measurements the design is
based on.

## Layout

- `src/voxpen/refine/` - the refinement guard and prompt templates that
  sit between the local LLM and the user's keyboard (`docs/PLAN.md` §3).
- `tools/probe_refiner.py` - manual harness for testing candidate
  refiner models against real dictation samples.
- `tests/` - guard test suite.
- `handy-redesign/` - a UI redesign prototype built on top of
  [Handy](https://github.com/cjpais/Handy) (MIT, Copyright (c) 2025
  CJ Pais), used to explore interface direction before building
  voxpen's own settings/tray UI. See `handy-redesign/REDESIGN.md`.

## Status

Early/active development. Not yet packaged or installable end-to-end;
see the plan doc for the current build checkpoint.
