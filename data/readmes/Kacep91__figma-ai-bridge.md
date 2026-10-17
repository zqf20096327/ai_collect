# Figma AI Bridge

**Local Figma Desktop plugin + localhost bridge for AI-ready design handoff bundles.**

[![License: MIT](https://img.shields.io/badge/license-MIT-111827.svg)](LICENSE)
![Node.js >=20](https://img.shields.io/badge/node-%3E%3D20-339933.svg)
![Figma Desktop](https://img.shields.io/badge/Figma-Desktop%20plugin-f24e1e.svg)
![Localhost](https://img.shields.io/badge/runtime-localhost-2563eb.svg)
![No tokens](https://img.shields.io/badge/API%20tokens-not%20required-7c3aed.svg)

[Русский](#русский) · [English](#english) · [Skill](skills/figma-ai-bridge/SKILL.md) · [Bundle contract](skills/figma-ai-bridge/references/bundle-contract.md)

## Русский

### Зачем это нужно

Figma AI Bridge экспортирует данные из открытого файла Figma Desktop в локальный пакет, который затем читает ИИ-агент, например Codex. API Figma, Dev Mode MCP и токены доступа не требуются.

Сырой JSON из Figma слишком объемен для контекстного окна модели и содержит много лишнего. Для верстки достаточно внешнего вида, текстов, структуры, дизайн-токенов, размеров и кратких заметок по реализации.

Схема работы:

```text
Плагин Figma Desktop -> локальный сервер -> out/figma-bundle_*
```

Процесс из двух шагов:

1. Плагин экспортирует превью, тексты, структуру, размеры, стили и связи между макетами. Исходные изображения включаются в пакет только при включенной опции `Export image assets`.
2. ИИ-агент (Codex или аналогичный) читает собранный пакет через [skill](skills/figma-ai-bridge/SKILL.md), описывает визуал и дополняет данные для верстки.

Сам сервер не анализирует изображения как нейросеть. Он лишь готовит чистый пакет данных для дальнейшей работы ИИ.

### Режимы работы

| Режим          | Описание                                                                                                                                              |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Page Extract` | Сохраняет текущую страницу или область по ссылке. Макеты идут в том порядке, как они расположены визуально.                                           |
| `Links Batch`  | Обрабатывает список ссылок на узлы открытого файла Figma. Конкретные узлы захватываются напрямую, а ссылки на заголовки разворачиваются в дочерние захваты. |
| `Selection`    | Экспортирует только выделенные элементы. Подходит для точечного сохранения одного фрагмента.                                                          |

Базовая глубина вложенности дерева: `8`.

### Что получается на выходе

Пакет данных сохраняется в `out/`:

```text
figma-bundle_YYYY-MM-DD_HH-mm-ss/
  manifest.json
  prompt.md
  page-map.md
  links-report.md            # если есть данные о ссылках или области захвата
  codex-visual-brief-task.md # если включена Prepare Codex tasks или запущен brief/codex/auto
  codex-enrichment-task.md   # если включена Prepare Codex tasks или запущен enrich/auto
  design-system/             # только если есть локальные стили/переменные
  files/
    <file>/
      001-<capture>/
        preview.png
        implementation.md
        texts.json
        design-context.json
        assets/              # только при включенном Export image assets
        visual-brief.md      # после выполнения задачи визуального описания
        ai-notes.md          # после обогащения
  index/                     # после обогащения
```

Порядок чтения для ИИ:

1. `prompt.md`, затем `page-map.md` и `links-report.md`, если он есть.
2. `./figma-ai-bridge summary <bundle>` — краткая сводка без чтения JSON.
3. `visual-brief.md`, если он уже создан, затем `preview.png` для визуальной сверки.
4. `implementation.md` и, после обогащения, `ai-notes.md`.
5. `texts.json` — только для точных строк, которых нет в кратких файлах.
6. `design-context.json` — только для точных размеров, цветов, шрифтов, автолейаутов и иерархии.

Файл `design-context.json` стоит открывать только ради точных значений. Геометрия и типографика текста уже находятся в нем и не дублируются в `texts.json`. Не загружайте весь пакет в контекст модели без реальной необходимости.

### Автоматизация

Основной сценарий работы для Codex и других ИИ-агентов описан здесь:

```text
skills/figma-ai-bridge/SKILL.md
```

После экспорта макетов:

```bash
./figma-ai-bridge doctor
./figma-ai-bridge validate latest
./figma-ai-bridge summary latest
./figma-ai-bridge auto latest
```

Команда `auto` проверяет последний пакет и готовит два файла задач для Codex: визуальное описание и обогащение данных. В одной секции задачи по умолчанию находится `3` захвата. Сам Codex при этом не запускается.

При включенной опции `Prepare Codex tasks` плагин создает те же файлы сразу после экспорта. Codex выполняет их отдельно: сначала составляет описание по `preview.png`, затем дополняет данные на основе описания и кратких файлов. `texts.json` и `design-context.json` открываются только для недостающих точных значений.

Полезные ссылки:

- [automation.md](skills/figma-ai-bridge/references/automation.md)
- [bundle-contract.md](skills/figma-ai-bridge/references/bundle-contract.md)
- [figma-plugin-setup.md](skills/figma-ai-bridge/references/figma-plugin-setup.md)

### Быстрый старт

```bash
npm run check
./figma-ai-bridge doctor
./figma-ai-bridge start
./figma-ai-bridge path
```

### Установка плагина

Устанавливается как локальный плагин разработчика.

1. Откройте десктопное приложение Figma (не в браузере).
2. Откройте или создайте файл дизайна.
3. В меню выберите `Plugins -> Development -> Import new plugin from manifest...`.
4. Укажите файл `plugin/manifest.json` из этого репозитория.
5. Запустите `AI Bridge Batch Capture`.
6. Нажмите `Check bridge`.
7. Выберите режим экспорта и нажмите `Capture`.

Подробная диагностика и вариант с локальным `.fig` для корпоративных ограничений описаны в [инструкции по установке](skills/figma-ai-bridge/references/figma-plugin-setup.md).

### Приватность

Шлюз работает только через локальный сервер (localhost) и сохраняет файлы локально. Проект не редактирует макеты Figma, не обращается к API Figma и не требует токенов.

## English

### Purpose

Figma AI Bridge exports data from the open Figma Desktop file into a local bundle that an AI agent, such as Codex, can read afterward. It requires no Figma API, Dev Mode MCP, or access tokens.

Raw Figma JSON is too large and noisy for model context. For implementation, agents usually need a smaller set of artifacts: preview, text, structure, tokens, dimensions, and short implementation notes.

Flow:

```text
Figma Desktop plugin -> localhost bridge -> out/figma-bundle_*
```

The workflow has two steps:

1. The plugin extracts preview, text, structure, dimensions, styles, and relationships between mockups. Source image assets are exported only when explicitly enabled.
2. Then Codex or another AI agent reads the bundle through the [skill](skills/figma-ai-bridge/SKILL.md), writes visual descriptions, and enriches the data for implementation.

The bridge does not understand images like a vision model. It prepares a clean package for an AI agent to process next.

### Modes

| Mode           | What it does                                                                                                |
| -------------- | ----------------------------------------------------------------------------------------------------------- |
| `Page Extract` | Captures the current page or linked scope. Mockups are ordered visually.                                    |
| `Links Batch`  | Processes links to nodes in the open Figma file. Node links are captured directly; heading links expand into child captures. |
| `Selection`    | Exports only the current Figma selection. Use it for precise one-off captures.                              |

Default tree depth: `8`.

### Output

Bundles are saved to `out/`:

```text
figma-bundle_YYYY-MM-DD_HH-mm-ss/
  manifest.json
  prompt.md
  page-map.md
  links-report.md            # when link or capture-scope metadata exists
  codex-visual-brief-task.md # with Prepare Codex tasks or after brief/codex/auto
  codex-enrichment-task.md   # with Prepare Codex tasks or after enrich/auto
  design-system/             # only when local styles/variables exist
  files/
    <file>/
      001-<capture>/
        preview.png
        implementation.md
        texts.json
        design-context.json
        assets/              # only when Export image assets is enabled
        visual-brief.md      # after visual brief generation
        ai-notes.md          # after enrichment
  index/                     # after enrichment
```

AI reading order:

1. `prompt.md`, then `page-map.md` and `links-report.md` when present.
2. `./figma-ai-bridge summary <bundle>` for a compact inventory without opening JSON.
3. `visual-brief.md` when available, then `preview.png` for visual verification.
4. `implementation.md` and, after enrichment, `ai-notes.md`.
5. `texts.json` only for exact strings omitted from the concise files.
6. `design-context.json` only for exact dimensions, colors, typography, autolayout, effects, and hierarchy.

Open `design-context.json` only when exact values are needed. Text geometry and typography live there and are not duplicated in `texts.json`. Do not load the whole bundle into model context by default.

### Automation

The main workflow for Codex and other agents lives in:

```text
skills/figma-ai-bridge/SKILL.md
```

After capture:

```bash
./figma-ai-bridge doctor
./figma-ai-bridge validate latest
./figma-ai-bridge summary latest
./figma-ai-bridge auto latest
```

`auto` validates the latest bundle and prepares visual-brief and enrichment task files. Each task section contains `3` captures by default. It does not invoke Codex. Codex runs the prepared tasks separately, reuses existing visual briefs, and opens `texts.json` or `design-context.json` only for missing exact values.

References:

- [automation.md](skills/figma-ai-bridge/references/automation.md)
- [bundle-contract.md](skills/figma-ai-bridge/references/bundle-contract.md)
- [figma-plugin-setup.md](skills/figma-ai-bridge/references/figma-plugin-setup.md)

### Quick Start

```bash
npm run check
./figma-ai-bridge doctor
./figma-ai-bridge start
./figma-ai-bridge path
```

### Plugin Setup

Install the plugin as a Figma development plugin.

1. Open Figma Desktop, not the browser app.
2. Open or create a Figma Design file.
3. Choose `Plugins -> Development -> Import new plugin from manifest...`.
4. Select `plugin/manifest.json` from this repository.
5. Run `AI Bridge Batch Capture`.
6. Click `Check bridge`.
7. Choose a capture mode and click `Capture`.

For troubleshooting and the local `.fig` workaround for corporate restrictions, see the [plugin setup guide](skills/figma-ai-bridge/references/figma-plugin-setup.md).

### Privacy

The bridge listens on localhost and writes files locally. It does not edit Figma, call Figma APIs, or require tokens.

## License

MIT. See [LICENSE](LICENSE).
