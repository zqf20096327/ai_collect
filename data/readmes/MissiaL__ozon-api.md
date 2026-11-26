# ozon-api — Claude/Agent Skill для Ozon Seller API + Performance API

Skill-репозиторий: полные официальные OpenAPI 3.0 спеки Ozon Seller API
(483 операции, 56 разделов) и Ozon Performance API — рекламы (48 операций,
6 разделов) + CLI для навигации по ним.

Оба официальных снимка получены 18 октября 2026 года через браузер с официальных
`swagger.json` с параметром для обхода устаревшего CDN-кеша. `x-source` содержит URL,
дату проверки и SHA-256 сохранённого исходного JSON; работоспособность методов с ключом
продавца этой проверкой не подтверждалась.

В Seller API добавлены отвязка штрихкода и проверка выполнения плана отгрузок.
Обновлены схемы возвратов, складов и сертификатов. Старые методы этикеток FBS
помечены устаревшими: отключение назначено на 2 ноября 2026 года. В Performance API
уточнены лимиты операций с кампаниями. Подробности миграций — в [SKILL.md](SKILL.md).

- [SKILL.md](SKILL.md) — точка входа для агента: авторизация, паттерны вызова, грабли.
- [references/ozon-seller-openapi.json](references/ozon-seller-openapi.json) — спек с официального
  `docs.ozon.ru/api/seller/swagger.json`, обогащённый русскими тегами и `x-ozon-section`.
- [references/ozon-performance-openapi.json](references/ozon-performance-openapi.json) — спек рекламы
  с `docs.ozon.ru/api/performance/swagger.json`, та же обработка.
- [references/index.md](references/index.md), [references/index-performance.md](references/index-performance.md) —
  плоские индексы всех эндпоинтов по разделам.
- [scripts/lookup_endpoint.py](scripts/lookup_endpoint.py) — `tags` / `search` / `show`
  (`--api seller|performance`).

## Обновление спеков

Спеки и индексы пересобираются локальным `scripts/build_spec.py`.
docs.ozon.ru за антиботом, поэтому swagger.json надо скачать реальным браузером
с официальных страниц Seller API и Performance API. Добавляйте cache-buster (`?${Date.now()}`): чистый URL
может вернуть устаревшую CDN-копию. Затем:

```bash
python3 scripts/build_spec.py --api seller --input seller.json --checked-at 2026-10-18
python3 scripts/build_spec.py --api performance --input perf.json --checked-at 2026-10-18
python3 scripts/test_skill.py
```

Укажите фактическую дату получения каждой схемы. Скрипт сохраняет исходную
структуру и добавляет только русские теги, `x-ozon-section` и `x-source`.
Только stdlib, сети не требует. В Seller-схеме есть внешние ссылки на
`rpcStatus.yaml`; CLI оставляет их видимыми, но отдельные YAML-файлы не загружает.
