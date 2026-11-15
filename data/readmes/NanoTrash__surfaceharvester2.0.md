# SurfaceHarvester 2

SurfaceHarvester 2 — CLI-инструмент для сбора поверхности атаки и поиска уязвимостей веб-приложений и сетевых сервисов. Результаты сканирований сохраняются в SQLite и доступны в виде текстовых и JSON-отчётов.

![Демонстрация установки и первого сканирования SurfaceHarvester](docs/demo.gif)

Используйте инструмент только для систем, которыми вы владеете или на проверку которых получено разрешение.

## Возможности

- обнаружение субдоменов через Subfinder с последующим выбором целей;
- поиск портов и уязвимостей через Nmap и сценарий `vulners`;
- проверка CVE, misconfig и технологических признаков через Nuclei;
- перебор директорий и параметров через Gobuster;
- извлечение email и телефонов со стартовой страницы;
- поиск эксплойтов для CVE через vulnx;
- сохранение доказательств Nuclei: `template-id`, `matcher-name`, `extracted-results`;
- дедупликация находок, миграции SQLite и история сессий;
- отчёты по цели, критичности, типам находок, сессиям и эксплойтам.

## Быстрая установка одной командой

[Краткая инструкция](QUICKSTART.md)

Требуются Linux или WSL, Python 3.11–3.15, Go и Nmap. Poetry и Docker не нужны.

```bash
git clone https://github.com/NanoTrash/surfaceharvester2.0.git && cd surfaceharvester2.0 && ./install.sh
```

Скрипт создаёт изолированные `.venv` и `.tools`, устанавливает проект, Nuclei, Subfinder, Gobuster, vulnx и языковые данные, а затем добавляет команду `surfaceharvester` в `~/.local/bin`.

```bash
surfaceharvester --help
surfaceharvester init --db scan_results.db
```

Если `~/.local/bin` отсутствует в `PATH`, скрипт выведет команду для его добавления. Если Nmap отсутствует, разрешите установку системного пакета явно:

```bash
SURFH2_INSTALL_SYSTEM_DEPS=1 ./install.sh
```

В этом случае на Ubuntu/Debian скрипт использует `sudo apt-get` только для Nmap. Повторный запуск `./install.sh` обновляет проект и зависимости.

## Требования для ручной установки

- Python 3.11–3.15; проект проверен на Python 3.14.
- Poetry 2.0 или новее — только для установки вручную.
- Nmap, Nuclei, Subfinder и Gobuster.
- vulnx и API-ключ ProjectDiscovery Cloud — только для поиска эксплойтов.

## Установка вручную (альтернатива)

### 1. Клонирование и Python-зависимости

```bash
git clone https://github.com/NanoTrash/surfaceharvester2.0.git
cd surfaceharvester2.0
poetry install --no-root
poetry run python -m spacy download en_core_web_sm
```

Недостающие модель spaCy и данные NLTK также загружаются автоматически при первом запуске. Это поведение можно отключить через переменные окружения, описанные ниже.

### 2. Внешние сканеры

Для Ubuntu/Debian:

```bash
sudo apt update
sudo apt install -y nmap gobuster golang-go

go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/projectdiscovery/cvemap/cmd/vulnx@latest
```

Убедитесь, что каталог `$(go env GOPATH)/bin` добавлен в `PATH`.

Для macOS:

```bash
brew install nmap gobuster nuclei subfinder
```

Для Windows загрузите бинарные файлы из официальных репозиториев:

- Nmap: https://nmap.org/download
- Nuclei: https://github.com/projectdiscovery/nuclei/releases
- Subfinder: https://github.com/projectdiscovery/subfinder/releases
- Gobuster: https://github.com/OJ/gobuster/releases
- vulnx: https://github.com/projectdiscovery/cvemap/releases

Для vulnx требуется бесплатный API-ключ ProjectDiscovery Cloud. Его можно получить в разделе **Settings → API Key** на https://cloud.projectdiscovery.io и активировать один раз:

```bash
vulnx -auth
```

### 3. Проверка установки

```bash
nmap -V
nuclei -version
subfinder -version
gobuster --version
vulnx -version
poetry run python cli.py --help
```

При необходимости обновите шаблоны Nuclei:

```bash
nuclei -update-templates
```

## Быстрый старт

После `./install.sh` примеры можно запускать напрямую:

```bash
# Создание или миграция базы данных
surfaceharvester init --db scan_results.db

# Полное сканирование из каталога проекта
surfaceharvester full-scan http://example.com \
  --db scan_results.db \
  --dir-wordlist common.txt \
  --fuzz-wordlist LFI-Jhaddix.txt

# Краткая сводка
surfaceharvester summary \
  --target http://example.com \
  --db scan_results.db

# История сессий
surfaceharvester sessions --db scan_results.db
```

Для установки вручную вместо `surfaceharvester` используется `poetry run python cli.py`.

## Полное сканирование и порядок обработки

Полный скан выполняется в следующем порядке:

1. **Subfinder** обнаруживает субдомены и сохраняет их в БД.
2. Для основной цели выполняются **Nmap → Contacts → Nuclei → Gobuster**.
3. Пользователь выбирает субдомены для дальнейшей обработки.
4. Для каждого выбранного субдомена выполняются **Nmap → Contacts → Nuclei → Gobuster** без повторного Subfinder.

### Выбор субдоменов

```bash
# Все найденные субдомены
poetry run python cli.py full-scan http://example.com \
  --db scan_results.db \
  --dir-wordlist common.txt \
  --fuzz-wordlist LFI-Jhaddix.txt \
  --subdomains-all

# Только указанные субдомены; номера через запятую также поддерживаются
poetry run python cli.py full-scan http://example.com \
  --db scan_results.db \
  --dir-wordlist common.txt \
  --fuzz-wordlist LFI-Jhaddix.txt \
  --subdomains-select 'shop.example.com,api.example.com'
```

Без этих флагов программа спросит, нужно ли сканировать субдомены. После ответа `y` можно ввести `all`, номера через запятую или имена. Для отмены выбора используется `q`.

Перед использованием `--subdomains-all` проверьте список найденных имён: источники Subfinder могут возвращать нерабочие или wildcard-записи.

## Только Nuclei

Команда `scan --scanners nuclei` запускает Nuclei без Nmap, Subfinder и Gobuster:

```bash
export SURFH2_NUCLEI_EXTRA_ARGS='-tags cve,misconfig,wordpress -timeout 15 -rate-limit 50'

poetry run python cli.py scan https://example.com \
  --scanners nuclei \
  --db scan_results.db
```

Не ограничивайте `severity`, если нужны информационные misconfig и обнаружение устаревших версий. Nuclei передаёт JSONL-находки в `stdout`, а статистику и служебные сообщения — в `stderr`. В БД попадают только JSONL-находки.

Если Nuclei завершил менее 100% плана или был остановлен по таймауту, частичные находки сохраняются, но сессия получает `completed_with_errors`, а CLI возвращает ненулевой код.

Для каждой записи сохраняются:

- ресурс и критичность;
- человекочитаемое имя шаблона или CVE;
- описание;
- `template-id` и `matcher-name`;
- извлечённые значения, например версии WordPress и плагинов.

Несколько CVE в одном шаблоне сохраняются отдельными записями. Идентичные повторы отбрасываются, а разные matcher и доказательства сохраняются независимо.

## Другие команды CLI

### Поверхностный сбор без записи уязвимостей в БД

```bash
poetry run python cli.py surface example.com \
  --dir-wordlist common.txt \
  --fuzz-wordlist LFI-Jhaddix.txt \
  --output scan_results.txt
```

### Цели, сохранённые в БД

```bash
# Все хосты, включая IP-адреса
poetry run python cli.py targets-list --db scan_results.db

# Только субдомены
poetry run python cli.py targets-list --db scan_results.db --subdomains

# Интерактивный выбор сохранённых целей для полного сканирования
poetry run python cli.py targets-scan \
  --db scan_results.db \
  --dir-wordlist common.txt \
  --fuzz-wordlist LFI-Jhaddix.txt \
  --subdomains
```

### Отчёты через cli.py

```bash
poetry run python cli.py report \
  --target http://example.com \
  --db scan_results.db

poetry run python cli.py summary \
  --target http://example.com \
  --db scan_results.db

poetry run python cli.py sessions --db scan_results.db
```

## Отчёты reports.py и reports_manager.py

`reports.py` использует `scan_results.db` в текущем каталоге:

```bash
poetry run python reports.py 1    # краткая сводка
poetry run python reports.py 2    # детальный анализ
poetry run python reports.py 3    # сессии
poetry run python reports.py 4    # хосты и субдомены
poetry run python reports.py 5    # оценка безопасности
poetry run python reports.py 6    # эксплойты и CVE
poetry run python reports.py 7    # все отчёты
poetry run python reports.py i    # интерактивное меню
```

`reports_manager.py` поддерживает выбор БД и фильтр по цели:

```bash
poetry run python reports_manager.py --db scan_results.db --report 1
poetry run python reports_manager.py --db scan_results.db --report 2 --target example.com
poetry run python reports_manager.py --db scan_results.db --report 3
poetry run python reports_manager.py --db scan_results.db --report 4
poetry run python reports_manager.py --db scan_results.db --report 5
poetry run python reports_manager.py --db scan_results.db --report 6
poetry run python reports_manager.py --db scan_results.db --report 7
poetry run python reports_manager.py --db scan_results.db --interactive
```

## Поиск эксплойтов через vulnx

```bash
# Обработать необработанные CVE
poetry run python cli.py exploits search --db scan_results.db --limit 10

# Только для конкретной цели
poetry run python cli.py exploits search \
  --db scan_results.db \
  --target example.com \
  --limit 5

# Статистика обработки
poetry run python cli.py exploits status --db scan_results.db

# Отчёты с фильтрами
poetry run python cli.py exploits report --db scan_results.db
poetry run python cli.py exploits report --db scan_results.db --target example.com
poetry run python cli.py exploits report --db scan_results.db --cve CVE-2026-109618
poetry run python cli.py exploits report --db scan_results.db --format json

# Мониторинг новых CVE
poetry run python cli.py exploits monitor --db scan_results.db --interval 60

# Мониторинг с периодическим выводом статуса; Ctrl+C для остановки
poetry run python cli.py exploits monitor --db scan_results.db --interval 60 --daemon
```

## Переменные окружения

```bash
# БД по умолчанию для cli.py
export SURFH2_DB_PATH=scan_results.db

# Автозагрузка модели spaCy и данных NLTK; по умолчанию включены
export SURFH2_AUTO_INSTALL_SPACY=1
export SURFH2_AUTO_INSTALL_NLTK=1

# Уровень логирования: DEBUG, INFO, WARNING или ERROR
export SURFH2_LOG_LEVEL=INFO

# Файл лога
export SURFH2_LOG_FILE=logs/surfaceharvester2.0.log

# Дополнительные аргументы Nuclei
export SURFH2_NUCLEI_EXTRA_ARGS='-tags cve,misconfig,wordpress -timeout 15 -rate-limit 50'

# Общий таймаут Nuclei и таймаут неактивности, секунды
export SURFH2_NUCLEI_TIMEOUT=3000
export SURFH2_NUCLEI_INACTIVITY_SECONDS=1200

# Интервал heartbeat-статистики Nuclei, секунды
export SURFH2_NUCLEI_STATS_INTERVAL=30
```

Для отключения автоматической загрузки данных установите соответствующую переменную `SURFH2_AUTO_INSTALL_*` в `0`.

## База данных и статусы

Основные таблицы:

- `vulnerability` — уязвимости, misconfig и доказательства;
- `host`, `subdomain` — обнаруженные цели;
- `scansession` — история запусков;
- `cve`, `scanresult` — устаревший универсальный импорт CVE;
- `cvecache` — кэш ответов vulnx;
- `cveprocessing` — состояние обработки CVE;
- `exploits` — найденные эксплойты.

Статусы сессий:

- `running` — сканирование выполняется;
- `completed` — все запрошенные проверки завершены без ошибок;
- `completed_with_errors` — сценарий завершён, но один или несколько сканеров вернули ошибку;
- `failed` — критическая ошибка сценария.

При инициализации автоматически создаются недостающие поля и индексы, переименовываются старые таблицы `cve_cache` и `cve_processing`, а также удаляются дубликаты статусов и эксплойтов. **Перед запуском миграции на рабочей БД создайте резервную копию.**

## Структура проекта

```text
surfaceharvester2.0/
├── install.sh              # установка одной командой
├── cli.py                  # основной CLI
├── main.py                 # альтернативный запуск Nuclei
├── reports.py              # быстрые отчёты
├── reports_manager.py      # отчёты с выбором БД и цели
├── config.py               # общие настройки
├── config_logging.py       # логирование
├── common.txt              # словарь директорий
├── LFI-Jhaddix.txt         # словарь параметров/LFI
├── pyproject.toml          # метаданные и зависимости
├── poetry.lock             # зафиксированные версии
├── poetry.toml             # локальное окружение Poetry
├── db/                     # модели, миграции и отчёты
└── scanner/                # сканеры, Nuclei, vulnx и парсеры
```

## Устранение неполадок

### Инструмент не найден

```bash
command -v nmap nuclei subfinder gobuster vulnx
```

Проверьте установку и наличие `$(go env GOPATH)/bin` в `PATH`.

### Модель spaCy не найдена

```bash
poetry run python -m spacy download en_core_web_sm
poetry run python -m spacy validate
```

### Nuclei долго не выдаёт результатов

Не добавляйте `-silent`, если нужен контроль прогресса. Приложение включает `-stats -si 30` и читает статистику отдельно от JSONL. Общий лимит и лимит неактивности настраиваются через `SURFH2_NUCLEI_TIMEOUT` и `SURFH2_NUCLEI_INACTIVITY_SECONDS`.

### Таймауты HTTP при открытых портах

Проверьте цель напрямую:

```bash
curl -I -L --max-time 20 https://example.com
nmap -Pn -p 80,443 --host-timeout 30s example.com
```

Открытые порты не гарантируют ответ HTTP: возможны фильтрация сети, балансировщик или защита целевого хоста. В этом случае сессия должна завершиться со статусом `completed_with_errors`, а не считаться успешной.

### База заблокирована

Закройте процессы, которые используют БД, или укажите другой файл:

```bash
poetry run python cli.py init --db new_scan_results.db
```

### Логи

```bash
export SURFH2_LOG_LEVEL=DEBUG
export SURFH2_LOG_FILE=logs/surfaceharvester2.0.log

tail -f logs/surfaceharvester2.0.log
```

## Проверки перед коммитом

```bash
poetry check
poetry run python -m pip check
poetry run python -m compileall -q cli.py main.py reports.py reports_manager.py config.py config_logging.py db scanner
poetry run flake8 cli.py main.py reports.py reports_manager.py config.py config_logging.py db scanner \
  --select=F401,F402,F811,F821,F822,F823,F841 --count --statistics
poetry run python cli.py --help
git diff --check
```

## Лицензия

Проект распространяется по лицензии MIT. См. [LICENSE.md](LICENSE.md).
