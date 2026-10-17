# Fireplace

**A phone-first AI roleplay client.** Import Character Card V2/V3 cards and
lorebooks, plug in your own OpenAI-compatible API key, and chat — entirely on
your device. No account, no server, no bundled AI.

[中文说明](README.zh-CN.md) · [License: AGPL-3.0](LICENSE)



---

## Why it exists

Desktop roleplay tooling is mature, but the mobile story has always been a
workaround: install a terminal emulator, install a runtime, copy files around,
keep a shell session alive. Fireplace takes the opposite approach — it is a
native Android app that reads and writes the same *file formats* the ecosystem
already uses, so everything you have already collected keeps working.

Concretely: a card exported from another tool imports here and re-exports
**byte-for-byte unchanged**, including fields Fireplace doesn't understand yet.

## Features

**Cards**
- Imports PNG / JSON / CHARX, Character Card V1–V3
- Unknown fields are preserved on import and survive re-export
- Multiple takes (swipes) per reply; alternate greetings become separate takes

**Lorebooks**
- Native `entries` maps, card-embedded books, and V3 wrapping
- Both field-naming conventions accepted
- Full trigger engine: scan depth, constant entries, primary/secondary keys,
  selective logic, probability, inclusion groups, recursion, timed effects

**Prompt assembly**
- Explicit, inspectable block order
- `system_prompt` / jailbreak slot replacement, `{{original}}`, in-chat depth
  injection
- Message-merge strategies (keep blocks separate, or merge into one system
  message)

**Chat**
- Streaming output, multiple takes, continue, edit, delete, impersonate
- Markdown rendering with syntax-highlighted code blocks and copy buttons
- Attachments with text extraction

**Authoring and debugging**
- Lorebook editor, regex scripts with live preview, persona, author's note,
  per-chat generation settings
- **Inspect last request** — see the exact parameters and `messages[]` that were
  sent, plus raw response frames when something goes wrong

**Interface**
- Five languages: 简体中文 / English / Français / 日本語 / Русский
- Dark theme tuned for a warm, low-light room

## What you need

An **OpenAI-compatible** endpoint: a base URL, an API key, and a model name.
Any self-hosted server or proxy works too.

Fireplace ships **no provider presets and recommends no particular provider** —
it does not resell, proxy, or endorse any model service. Chatting consumes your
own quota, from your own account.

## Privacy

- Everything (chats, cards, lorebooks, settings) lives in a local SQLite
  database on your device
- The API key is stored with system-level encryption (Android Keystore)
- Requests go only to the endpoint you configured — there is no intermediary
- No accounts, no telemetry, no analytics, no ads
- Everything except the AI calls themselves works offline

## Install

**Android 7.0 or newer.**

- Download the signed APK from [Releases](../../releases)
- Or build it yourself (below)

## Build from source

Requires the [Flutter SDK](https://flutter.dev) and the Android SDK.

```bash
flutter pub get
flutter test                 # ~340 tests
flutter build apk --release
```

Release builds must be signed with a real key, and there is deliberately **no
fallback to debug signing** — a debug-signed build that reaches a store can
never be updated afterwards. Copy `android/key.properties.example` to
`android/key.properties` and point it at your own keystore; the template
explains how to generate one.

## Tests

`flutter test` runs the whole suite (~340 tests). The parts worth knowing about:

- **Prompt assembly** — block order, macro expansion, depth injection, merge
  modes, token budgeting and history trimming
- **World-info engine** — every trigger dimension above, including recursion
  and timed effects
- **Format round-trips** — cards and lorebooks re-export unchanged, and
  malformed input is handled without crashing
- **Widget tests** for real user paths: onboarding, import, send → stream →
  persist, swiping between takes, settings
- **Localization completeness** — every UI string exists in all five languages,
  plus a guard that fails if a hardcoded literal sneaks into the UI layer
- **Rendering regressions** — including one that pins "a reply containing
  `*italic action*` must never render as an empty bubble"

## Architecture

```
lib/
  l10n/           string table (5 languages) + locale plumbing
  core/
    engine/       prompt assembly, world info, macros   ← pure Dart
    card/         Character Card codecs (PNG/JSON/CHARX)
    worldbook/    lorebook codecs
    store/        SQLite records and queries
    generation.dart  SSE streaming, error classification
  ui/             pages and widgets
  markdown_view.dart
tool/dump_prompt.dart    CLI that prints an assembled prompt
```

The long-lived decision worth calling out: **`lib/core/engine` never imports
Flutter.** Prompt assembly is the most correctness-critical and most
test-friendly part of the app, so it stays a plain Dart library — the whole
engine is testable without a widget tree, and `tool/dump_prompt.dart` can print
an assembled prompt from the command line.

Imported data is stored as the original text (`card_json`, `book_json`, …)
rather than as a lossy re-model, which is what makes byte-identical re-export
possible.

## Compatibility

Fireplace implements the community **Character Card V2/V3** formats and the
standard **lorebook / world-info JSON** structure, so data produced by other
tools imports cleanly and exports unchanged.

It is an independent implementation: **this repository contains no third-party
application's code, data, or assets.** Format compatibility comes from
implementing published formats, not from vendoring anyone else's work.

## Status

Feature-complete for single-character roleplay and actively maintained. Known
gaps are tracked in Issues — bug reports that include an "inspect last request"
dump are the easiest kind to act on.

## Contributing

Issues and pull requests are welcome. Before opening a PR:

```bash
flutter analyze lib test tool   # must be clean
flutter test                    # must be green
```

UI strings live in `lib/l10n/strings.dart` as a plain table — one line per
language. The steps for adding a language are documented in that file.

## License

[GNU AGPL-3.0](LICENSE) © 2026 TriangleCat

You are free to use, study, modify and redistribute this software. If you run a
modified version as a network service, you must offer the modified source to its
users.
