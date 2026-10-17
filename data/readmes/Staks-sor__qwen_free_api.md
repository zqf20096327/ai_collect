# Qwen API Integration 🤖

Модуль для работы с Qwen API через прокси `aikit.club`.
Обеспечивает обход WAF, автоматическую подстановку токена и удобный интерфейс чата.

## 📂 Структура

*   `chat.py` — Интерактивный чат в терминале (с анимацией и красивым выводом).
*   `qwen_client.py` — Основной класс клиента (`QwenClient`).
*   `config.py` — Конфигурация (URL, таймауты).
*   `credentials.example.json` — безопасный шаблон файла с токеном.
*   `credentials.json` — локальный файл с токеном, исключённый через `.gitignore`.

## 🚀 Быстрый старт

### 1. Установка зависимостей
```bash
python -m pip install -r requirements.txt
```

### 2. Настройка
Создайте локальный файл с токеном из шаблона:

```bash
cp credentials.example.json credentials.json
```

Затем добавьте токен в `credentials.json`:
```json
{
  "sessions": [
    {
      "qwen_credentials": {
        "access_token": "ВАШ_ТОКЕН"
      }
    }
  ]
}
```

### 3. Запуск чата
Поболтать с ИИ прямо из терминала:
```bash
python chat.py
```

## 💻 Использование в коде

Модуль полностью готов к импорту в любую часть проекта (например, для массовой рассылки).

```python
from qwen_client import QwenClient

# Клиент сам найдет credentials.json и настроит заголовки
client = QwenClient()

# Простой вопрос
answer = client.simple_ask("Придумай заголовок для рассылки")
print(answer)

# Сложный диалог
messages = [
    {"role": "system", "content": "Ты маркетолог."},
    {"role": "user", "content": "Напиши промо-пост."}
]
response = client.chat_completion(messages)
print(response['choices'][0]['message']['content'])
```

## ⚙️ Конфигурация (`config.py`)

*   **URL**: `https://qwen.aikit.club/v1`
*   **Модель**: `""` (пустая строка, авто-выбор сервером)
*   **Таймаут**: 120 сек (для генерации длинных текстов)
