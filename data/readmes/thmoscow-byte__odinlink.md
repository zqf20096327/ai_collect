# OneBridge — MCP-сервер для подключения Claude к 1С

[English version](README_EN.md)

**OneBridge** подключает Claude (Code, Desktop, API) к вашей базе 1С:Предприятие через протокол [MCP](https://modelcontextprotocol.io/). AI видит метаданные, регистры, документы — и генерирует точный код с учётом реальной конфигурации.

Бесплатно. Работает с любой конфигурацией: БП, ЗУП, УТ, ERP, УНФ, КА и другими.

[![Версия](https://img.shields.io/badge/version-1.3-blue)](https://github.com/thmoscow-byte/onebridge/releases/latest)
[![Лицензия](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![1С](https://img.shields.io/badge/1С-8.3.20+-yellow)](https://1c.ru)
[![MCP](https://img.shields.io/badge/MCP-protocol-purple)](https://modelcontextprotocol.io/)

---

## Что умеет OneBridge

| Инструмент | Описание |
|---|---|
| `execute_query` | Выполняет запросы на языке 1С и возвращает результат |
| `execute_code` | Запускает произвольный код 1С на сервере |
| `get_metadata` | Читает структуру метаданных: справочники, документы, регистры |
| `get_event_log` | Получает журнал регистрации с фильтрацией |
| `get_object_by_link` | Находит объект по навигационной ссылке |
| `get_link_of_object` | Возвращает ссылку на объект для навигации |
| `find_references_to_object` | Ищет все ссылки на объект в базе |
| `get_access_rights` | Проверяет права доступа к объектам метаданных |

## Быстрый старт

### 1. Скачайте OneBridge

**[Скачать через Telegram-бот @onebridge1c_bot](https://t.me/onebridge1c_bot)** — получите EPF-файл, инструкцию и набор промтов.

Или скачайте EPF из [GitHub Releases](https://github.com/thmoscow-byte/onebridge/releases/latest).

### 2. Запустите в 1С

1. Откройте базу 1С в режиме «Предприятие»
2. Меню → Файл → Открыть → выберите `OneBridge.epf`
3. Нажмите **«Запустить сервер»**
4. Сервер запустится на порту `1414` (по умолчанию)

### 3. Подключите Claude

**Claude Code** (в терминале):

Добавьте в файл `.mcp.json` в корне вашего проекта:

```json
{
  "mcpServers": {
    "onebridge": {
      "type": "sse",
      "url": "http://localhost:1414/mcp"
    }
  }
}
```

**Claude Desktop**:

Откройте Settings → Developer → Edit Config и добавьте:

```json
{
  "mcpServers": {
    "onebridge": {
      "type": "sse",
      "url": "http://localhost:1414/mcp"
    }
  }
}
```

Перезапустите Claude — инструменты OneBridge появятся автоматически.

### 4. Начните работать

Примеры запросов к Claude:

- *«Покажи структуру справочника Номенклатура»*
- *«Найди все документы реализации за март 2026»*
- *«Напиши обработку для загрузки прайс-листа из Excel»*
- *«Проверь, есть ли ошибки в журнале регистрации за сегодня»*

Больше примеров — в [examples/prompts.md](examples/prompts.md).

## Документация

- [Установка и настройка](docs/installation.md) — подробная инструкция
- [Инструменты MCP](docs/tools.md) — описание каждого инструмента с примерами
- [Настройка Claude](docs/claude-setup.md) — Claude Code, Desktop, API
- [Решение проблем](docs/troubleshooting.md) — FAQ и типичные ошибки

## Архитектура

```
┌──────────────┐     MCP (SSE)      ┌──────────────┐     COM/HTTP     ┌──────────────┐
│              │ ◄────────────────► │              │ ◄──────────────► │              │
│    Claude    │    порт 1414       │  OneBridge   │                  │   База 1С    │
│  Code/Desktop│                    │   (EPF)      │                  │  БП/ЗУП/ERP  │
│              │ ◄────────────────► │              │ ◄──────────────► │              │
└──────────────┘   JSON-RPC 2.0    └──────────────┘                  └──────────────┘
```

OneBridge работает как внешняя обработка (EPF) внутри 1С и поднимает HTTP-сервер, совместимый с протоколом MCP. Claude подключается через SSE и получает доступ к инструментам для работы с базой.

## Системные требования

- 1С:Предприятие 8.3.20 или выше
- Windows (для запуска EPF)
- Любая конфигурация 1С: Бухгалтерия, ЗУП, Управление торговлей, ERP, УНФ, КА и др.
- Claude Code, Claude Desktop или любой MCP-совместимый клиент

## Благодарности

OneBridge создан на основе [1c-mcp-toolkit](https://github.com/ROCTUP/1c-mcp-toolkit) от ROCTUP. Спасибо за отличный фундамент!

## Ссылки

- [Сайт проекта](https://onemanproduction.ru/onebridge/) — лендинг OneBridge
- [Telegram-бот](https://t.me/onebridge1c_bot) — скачать OneBridge + промты
- [Telegram-канал](https://t.me/oneman_prod) — новости и обновления
- [YouTube](https://youtube.com/@oneman_prod) — видео-инструкции
- [Статья: MCP-сервер для 1С](https://onemanproduction.ru/blog/mcp-server-1c.html) — подробный разбор

## Лицензия

[MIT](LICENSE)
