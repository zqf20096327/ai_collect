# AI Assistant for Writing (Rust + macOS Native Helper)

Фоновый AI-ассистент для письма на **Rust** и нативном слое **macOS** (`AppKit` + `AXUIElement` + `CGEventTap`). Работает поверх системных и сторонних приложений: Notes, TextEdit, Mail, Chrome, Telegram и Slack.

Подробная документация и руководства: [copywriting-software.github.io/ai-assistant-for-writing](https://copywriting-software.github.io/ai-assistant-for-writing/)

## Возможности

- **Системный Ghost Text Autocomplete**: показывает продолжение текста рядом с курсором с учётом активного приложения, заголовка окна и текста после курсора.
- **Принятие подсказок**:
  - `Tab`: вставить всю подсказку целиком
  - `Option + Right` (`⌥ + →`): принять одно слово
  - `Esc`: скрыть подсказку и приостановить автодополнение до конца текущего слова
- **Исправление грамматики и раскладки (`⌘⇧G`)**: правит орфографию, пунктуацию и текст, набранный в ошибочной раскладке (`ghbdtn` -> `привет`).
- **Переписывание текста (`⌘⇧R`)**: переписывает выделенный фрагмент короче или в нужном стиле (`concise`, `professional`, `friendly`, `clear`).
- **Локальная память и fast-path (`0 ms`)**: запоминает принятые вами фразы и статистику задержек. Повторные конструкции подсказываются локально без обращения к LLM.
- **Local-First + BYOK**: работает с бесплатной локальной моделью **Ollama** (`qwen2.5:1.5b`), OpenAI-совместимым API, Gemini API или Corebox.
- **Privacy Guard**: блокирует поля паролей (`AXSecureTextField`), менеджеры паролей (`1Password`, `Bitwarden`, `KeePassXC`, `Keychain Access`), терминалы и тексты с API-ключами или номерами банковских карт.

## Быстрый старт (macOS)

```bash
git clone https://github.com/copywriting-software/ai-assistant-for-writing.git
cd ai-assistant-for-writing

# 1. Проверка и тесты Rust-ядра
cargo test

# 2. Сборка нативного macOS-помощника (Ghost Text + Accessibility + CGEventTap)
./macos/build.sh

# 3. Настройка провайдера: локальный Ollama
ollama pull qwen2.5:1.5b
cargo run -- check

# Или облачный API-ключ (OpenAI / Gemini / Corebox)
# export OPENAI_API_KEY="sk-..."
# cargo run -- check

# 4. Проверка CLI-команд
cargo run -- complete "Привет, хотел уточнить по поводу"
cargo run -- fix "ghbdtn rfr ltkf"
cargo run -- rewrite "Нужно созвониться завтра обсудить все детали проекта" --style concise
cargo run -- layout "руддщ цщкдв"
cargo run -- stats

# 5. Запуск фонового ассистента (нужны права Accessibility и Input Monitoring для терминала)
cargo run --release -- daemon
```

## Конфигурация

Скопируйте `config.example.toml` в `config.local.toml` или `~/.config/ai-assistant-for-writing/config.toml`.

## Архитектура

- [`src/config.rs`](src/config.rs): загрузка конфигурации (`ollama`, `openai-compatible`, `gemini`, `corebox`).
- [`src/ai/mod.rs`](src/ai/mod.rs): асинхронные провайдеры с поддержкой `CancellationToken`.
- [`src/engine.rs`](src/engine.rs): контекстный промптинг (`window_title`, `text_after_cursor`), очистка подсказок, пословное принятие (`unicode-segmentation`), кэш префиксов со скользящим окном.
- [`src/memory.rs`](src/memory.rs): локальное хранилище принятых фраз, fast-path подсказок и метрик задержки (`stats`).
- [`src/encoding.rs`](src/encoding.rs): локальное исправление раскладки клавиатуры (EN <-> RU).
- [`src/privacy.rs`](src/privacy.rs): фильтрация паролей, защищённых полей и чувствительных шаблонов.
- [`src/session.rs`](src/session.rs): адаптивный debounce, ревизии, отмена устаревших запросов, проверка префикса перед вставкой.
- [`src/platform/mod.rs`](src/platform/mod.rs): мост к нативному адаптеру ОС (macOS или stdio JSON-RPC).
- [`macos/MacHelper.swift`](macos/MacHelper.swift): нативный слой на `AppKit` + `AXUIElement` + `CGEventTap` + плавающий `NSPanel` для ghost text.
