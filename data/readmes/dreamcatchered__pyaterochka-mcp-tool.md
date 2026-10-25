<div align="center">

# 🛒 Pyaterochka MCP Tool

**MCP-сервер и AI-бот для каталога «Пятёрочки»** — поиск магазинов, товаров,
акций и цен по всей России прямо из вашей нейросети.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![MCP](https://img.shields.io/badge/Protocol-MCP-8A2BE2)](https://modelcontextprotocol.io)
[![Telegram](https://img.shields.io/badge/Bot-Telegram-26A5E4?logo=telegram&logoColor=white)](#-запуск-telegram-бота)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

</div>

---

## ✨ Что это

Проект превращает публичный каталог [5ka.ru](https://5ka.ru) в **инструменты (tools) для LLM**:

| Компонент | Что делает |
|---|---|
| 🧩 **MCP stdio-сервер** | Подключается к Claude Desktop, Cursor, opencode и любому MCP-клиенту |
| 🌐 **HTTP MCP-сервер** | Тот же набор инструментов по `http://127.0.0.1:8765/mcp` (Streamable HTTP) — удобно для remote MCP через туннель |
| 🤖 **Telegram-бот с ИИ** | Полноценный агент: сам находит магазин, ищет товары, показывает фото и цены, помнит ваши предпочтения |

**Умеет:**

- 🔍 найти физический магазин по адресу или геолокации;
- 🗂️ получить категории конкретного магазина;
- 🛒 искать товары с фильтрами: цена (мин/макс), бренд, только акции;
- 📊 сортировать по цене / размеру скидки / популярности;
- 💳 показывать цену по карте, акции «при покупке N штук», старую цену;
- 📋 возвращать наличие, остаток, БЖУ, состав, PLU и ссылку на товар;
- 📸 отправлять альбом фотографий найденных товаров в Telegram.

> ⚠️ Проект **неофициальный** и не связан с X5 Group. Используется открытый
> веб-каталог без логина и пароля. Только в образовательных целях.

---

## 🏗️ Архитектура

```text
                    ┌──────────────────────┐
                    │   Claude / Cursor /  │
                    │  ChatGPT / Telegram  │
                    └──────────┬───────────┘
                               │
              ┌────────────────┴────────────────┐
              │                                 │
     MCP stdio / HTTP MCP                OpenAI-compatible API
              │                                 │
    ┌─────────▼─────────┐             ┌─────────▼─────────┐
    │   mcp/mcp_server  │             │    llm_client     │
    │  + mcp_http_server│             │ (фолбэк между     │
    └─────────┬─────────┘             │  провайдерами)    │
              │                       └─────────┬─────────┘
    ┌─────────▼──────────────────────────────────▼─────────┐
    │                 pyaterochka_store_api                 │
    │   браузер Camoufox  ИЛИ  aiohttp + cookies.json       │
    └──────────────────────────┬───────────────────────────┘
                               │
                        🌐 5d.5ka.ru API
```

---

## 🚀 Быстрый старт

### 1. Установка

```bash
git clone https://github.com/<you>/pyaterochka-mcp-tool.git
cd pyaterochka-mcp-tool

python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

<details>
<summary><b>Браузерный режим (опционально, рекомендую)</b></summary>

Без него тоже работает — через cookies (см. ниже). С ним cookies не нужны вообще:

```bash
pip install "camoufox[geoip]"
python -m camoufox fetch   # один раз скачать браузер (~150 МБ)
```
</details>

### 2. Настройка `.env`

```bash
cp .env.example .env
```

Минимум для работы MCP-сервера — **ничего** (только cookies, если не ставили camoufox).
Минимум для бота:

```env
TELEGRAM_BOT_TOKEN=123456:AA...      # от @BotFather
LLM_API_URL=https://api.openai.com/v1
LLM_API_KEY=sk-...
LLM_MODEL=gpt-4o-mini
```

Любой OpenAI-совместимый провайдер подойдёт: OpenAI, OpenRouter, Groq,
DeepSeek, NVIDIA NIM, Together AI, локальный vLLM/Ollama (`http://localhost:11434/v1`).

<details>
<summary><b>Все переменные окружения</b></summary>

| Переменная | По умолчанию | Описание |
|---|---|---|
| `TELEGRAM_BOT_TOKEN` | — | Токен бота от @BotFather (**обязателен для бота**) |
| `TELEGRAM_API_BASE_URL` | `https://api.telegram.org` | Можно указать локальный Telegram Bot API Server — тогда включится стриминг ответа || `TELEGRAM_PROXY_SOCKS5` | — | SOCKS5-прокси для Telegram |
| `LLM_API_URL` | `https://api.openai.com/v1` | Основной LLM (OpenAI-совместимый `/v1`) |
| `LLM_API_KEY` | — | Ключ основного LLM |
| `LLM_MODEL` | `gpt-4o-mini` | Модель основного провайдера |
| `LLM_RESERVE_URL/_KEY/_MODEL` | — | Резерв №1 (автофолбэк при сбоях/429/5xx) |
| `LLM_FALLBACK_URL/_KEY/_MODEL` | — | Резерв №2 (последний рубеж) |
| `OPENAI_API_KEY`, `OPENROUTER_API_KEY`, `GROQ_API_KEY`, … | — | Ключи для инлайн-меню `/model` в боте |
| `PYATEROCHKA_COOKIES_FILE` | — | Путь к cookies.json (если нет браузерного режима) |
| `PYATEROCHKA_PROXY` | — | SOCKS5-прокси для запросов к 5ka.ru |
| `MCP_HOST` / `MCP_PORT` | `127.0.0.1` / `8765` | Адрес HTTP MCP-сервера |

</details>

> 🇷🇺 **Пользователям из РФ:** если официальный `api.telegram.org` недоступен,
> можно использовать публичное зеркало Telegram Bot API — просто добавьте в `.env`:
>
> ```env
> TELEGRAM_API_BASE_URL=https://telegram.ebalo.lol
> ```

---

## 🧩 Запуск MCP-сервера

### Вариант A: stdio (для десктопных клиентов)

Ничего запускать руками не нужно — клиент сам стартует процесс.
Добавьте сервер в конфиг клиента:

**Claude Desktop** — `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "pyaterochka": {
      "command": "python",
      "args": ["C:/absolute/path/to/pyaterochka-mcp-tool/mcp/mcp_server.py"],
      "env": {
        "PYATEROCHKA_COOKIES_FILE": "C:/secrets/pyaterochka/cookies.json"
      }
    }
  }
}
```

**Cursor / любой клиент с `mcpServers`** — формат тот же.

Проверить вручную можно так:

```bash
python mcp/mcp_server.py          # слушает JSON-RPC в stdin/stdout
# или после pip install -e . :
pyaterochka-mcp
```

### Вариант B: HTTP (Streamable HTTP)

```bash
python mcp_http_server.py         # → http://127.0.0.1:8765/mcp
```

Эндпоинты: `POST /mcp` (JSON-RPC), `GET /health`, `GET /` (инфо + список tools).

Пример запроса:

```bash
curl -X POST http://127.0.0.1:8765/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"find_store","arguments":{"address":"Москва, Кировоградская улица, 17"}}}'
```

### 🧰 Доступные инструменты (12)

| Tool | Описание |
|---|---|
| `find_store` | Найти магазин по адресу → `store_id` |
| `find_nearest_stores` | Ближайшие магазины по координатам |
| `get_store_info` / `get_store_hours` | Карточка и часы работы магазина |
| `list_stores_in_area` | Магазины в прямоугольной области карты |
| `list_store_categories` | Дерево категорий магазина |
| `search_products` | Поиск товаров: цена, бренд, акции, сортировка |
| `list_category_products` | Товары категории с фильтрами |
| `find_products` | Универсальный поиск по адресу или `store_id` |
| `get_product_promotion` | Условия акции на товар |
| `get_product_info` | Карточка товара: состав, калории, БЖУ |
| `refresh_session` | Обновить web-сессию 5ka.ru |

Подробнее — в [`mcp/README.md`](mcp/README.md).

---

## 🤖 Запуск Telegram-бота

```bash
python bot.py      # только бот
python run.py      # бот + HTTP MCP-сервер вместе (живой вывод в консоль)
```

**Как пользоваться:**

1. `/start` → отправьте боту **геолокацию** (скрепка → 📍 Location) или напишите адрес;
2. выберите избранный магазин кнопками;
3. спрашивайте: *«найди молоко до 100 ₽»*, *«что со скидкой на кофе?»*, *«часы работы?»*;
4. команды: `/reset` — сбросить память, `/stop` — прервать выполнение, `/model` — сменить модель на лету.

Бот ведёт себя как агент: сам вызывает инструменты по цепочке
(найти магазин → искать товары → проверить акции → показать фото и итог).

---

## 🍪 Cookies: нужны ли и зачем

Есть **два транспорта** для доступа к каталогу — выберите один:

| | 🦊 Браузерный (camoufox) | 📄 aiohttp + cookies.json |
|---|---|---|
| Ручные cookies | ❌ не нужны | ✅ нужны |
| Надёжность при 403/антиботе | выше | ниже |
| Зависимости | тяжёлые (~150 МБ браузер) | лёгкие |

**Как получить cookies.json (для второго варианта):**

1. Откройте [5ka.ru](https://5ka.ru) в Chrome/Firefox — **логиниться не нужно**, достаточно просто открыть сайт;
2. Экспортируйте cookies расширением типа *Get cookies.txt LOCALLY* (формат JSON или Netscape);
3. Сохраните файл **вне репозитория**, например `C:\secrets\pyaterochka\cookies.json`;
4. Укажите путь: `PYATEROCHKA_COOKIES_FILE=C:\secrets\pyaterochka\cookies.json`.

При запуске клиент сначала открывает 5ka.ru, чтобы принять свежие защитные
cookies (`spjs`/`spsc` и др.), а затем обновляет их автоматически.

> 🔐 **Никогда не публикуйте cookies.json** — это ваша живая веб-сессия.
> Файл уже добавлен в `.gitignore`. Если утёк — очистите cookies на сайте.

---

## 🌍 Публичный доступ: подключение ChatGPT / Claude через туннель

HTTP MCP-сервер слушает `127.0.0.1:8765` — чтобы внешние нейросети (ChatGPT,
Claude и любые клиенты с поддержкой remote MCP) достучались до него,
заверните порт в туннель:

**ngrok:**

```bash
ngrok http 8765
# получите адрес вида https://a1b2-...ngrok-free.app
```

**cloudflared (без регистрации):**

```bash
cloudflared tunnel --url http://localhost:8765
# получите адрес вида https://....trycloudflare.com
```

Затем добавьте URL в клиент:

| Клиент | Где указать |
|---|---|
| **Claude Desktop / Claude Web** | Settings → Connectors → *Add custom connector* → `https://ваш-адрес/mcp` |
| **ChatGPT** | Settings → Apps & Connectors → *Create* (Developer Mode) → URL `https://ваш-адрес/mcp` |
| **Cursor** | MCP settings → *Add server* → тип URL/SSE |
| **MCP Inspector** | `npx @modelcontextprotocol/inspector`, transport: URL |

> ⚠️ **Безопасность:** endpoint публичный и **без авторизации** — любой, кто узнает
> адрес, сможет пользоваться вашими инструментами. Для постоянного использования
> прикройте туннель базовой авторизацией на реверс-прокси или используйте
> ngrok с IP-ограничением. SSH-туннели/ключи в код проекта сознательно не включены.

---

## 💡 Примеры запросов

```text
Найди в Пятёрочке по адресу Москва, Кировоградская улица, 17
молоко дешевле 200 рублей и отсортируй по цене.
```

```text
Что из кофе сейчас по акции рядом со мной? Пришли фото топ-5.
```

Через CLI (без нейросети):

```bash
python pyaterochka_store_api.py resolve --address "Москва, Кировоградская улица, 17"
python pyaterochka_store_api.py products --address "Москва, Кировоградская улица, 17" \
    --store-id S105 --query "молоко" --price-max 200 --sort price_asc --limit 20
```

---

## 📁 Структура проекта

```text
pyaterochka-mcp-tool/
├── mcp/
│   ├── mcp_server.py        # MCP stdio-сервер (12 инструментов)
│   └── README.md            # детали подключения MCP-клиентов
├── mcp_http_server.py       # HTTP (Streamable HTTP) транспорт MCP
├── pyaterochka_store_api.py # API-слой каталога 5ka.ru (+CLI)
├── bot.py                   # Telegram-бот (aiogram)
├── run.py                   # бот + HTTP MCP одним процессом
├── agent.py                 # агентский цикл: LLM ↔ инструменты
├── llm_client.py            # OpenAI-совместимый клиент с фолбэком
├── providers.py             # каталог LLM-провайдеров для /model
├── config.py                # конфиг из переменных окружения
├── stats.py / live_timer.py # статистика и консольные украшения
├── requirements.txt
├── pyproject.toml
└── .env.example
```

## 🛡️ Безопасность

- Все ключи и токены — **только** через `.env` (в git не попадает).
- `cookies.json`, `sessions.json`, логи — в `.gitignore`.
- Ответы моделей никогда не содержат внутренних id (`sap_code`, PLU).
- Не публикуйте cookies, прокси и токены — см. раздел Cookies.

## ⚖️ Лицензия

[MIT](LICENSE). Проект не аффилирован с X5 Group («Пятёрочка»);
все товарные знаки принадлежат их владельцам.
