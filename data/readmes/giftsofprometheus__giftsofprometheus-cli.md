<p align="center">
  <a href="https://giftsofprometheus.com/?utm_source=github&amp;utm_medium=readme&amp;utm_campaign=cli"><img alt="Дары Прометея: мировые знания об ИИ на русском" src=".github/assets/banner.jpg" width="100%"></a>
</p>

# Дары Прометея CLI: мировые знания об ИИ на русском для вас и вашего AI-агента

**[Дары Прометея](https://giftsofprometheus.com/?utm_source=github&utm_medium=readme&utm_campaign=cli)** — мировые знания об ИИ на русском: доклады о разработке с AI-агентами, RAG, evals, MCP и AI-продуктах с русскими названиями, подробными описаниями с TL;DR, главами с таймкодами, профилями спикеров и полными транскриптами.

Этот CLI открывает каталог для терминала и AI-агентов: Claude Code, Codex, Cursor и других. Агент сам подберёт доклады под вашу задачу, прочитает транскрипт и сохранит полезное в избранное вашего аккаунта на [giftsofprometheus.com](https://giftsofprometheus.com/?utm_source=github&utm_medium=readme&utm_campaign=cli).

<p>
  <a href="https://giftsofprometheus.com/?utm_source=github&amp;utm_medium=readme&amp;utm_campaign=cli"><img alt="Каталог: giftsofprometheus.com" src="https://img.shields.io/badge/каталог-giftsofprometheus.com-173a63.svg?style=for-the-badge&amp;labelColor=0a0f1c" height="28"></a>
  <a href="https://www.npmjs.com/package/@giftsofprometheus/cli"><img alt="npm" src="https://img.shields.io/npm/v/@giftsofprometheus/cli.svg?style=for-the-badge&amp;labelColor=0a0f1c&amp;color=173a63" height="28"></a>
  <a href="https://github.com/giftsofprometheus/giftsofprometheus-cli/actions/workflows/ci.yml"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/giftsofprometheus/giftsofprometheus-cli/ci.yml?branch=main&amp;style=for-the-badge&amp;labelColor=0a0f1c&amp;color=173a63&amp;label=CI" height="28"></a>
  <a href="LICENSE"><img alt="Лицензия: Apache-2.0" src="https://img.shields.io/github/license/giftsofprometheus/giftsofprometheus-cli.svg?style=for-the-badge&amp;labelColor=0a0f1c&amp;color=173a63" height="28"></a>
</p>

## Зачем это нужно

- **Мировой опыт AI-инженерии на русском.** Доклады о кодинг-агентах, RAG, evals, MCP и архитектуре агентов от команд, которые делают это в продакшене. Не нужно смотреть часовые видео на английском или китайском, чтобы понять, стоит ли доклад вашего времени.
- **Ответ под вашу задачу, а не список ссылок.** Опишите агенту, над чем работаете. Он найдёт доклады, прочитает транскрипты и перескажет, что из них применимо у вас.
- **Один аккаунт для сайта и агента.** Что агент сохранил, появится в [избранном на сайте](https://giftsofprometheus.com/account?utm_source=github&utm_medium=readme&utm_campaign=cli). Интересы, которые вы указали [на сайте](https://giftsofprometheus.com/welcome?utm_source=github&utm_medium=readme&utm_campaign=cli), агент учитывает в подборке.

Удобнее читать глазами? Всё то же самое есть на [giftsofprometheus.com](https://giftsofprometheus.com/?utm_source=github&utm_medium=readme&utm_campaign=cli): [подбор докладов за минуту](https://giftsofprometheus.com/welcome?utm_source=github&utm_medium=readme&utm_campaign=cli), [персональная лента](https://giftsofprometheus.com/for-you?utm_source=github&utm_medium=readme&utm_campaign=cli) [спикеры](https://giftsofprometheus.com/speakers?utm_source=github&utm_medium=readme&utm_campaign=cli), [статьи об AI-агентах](https://giftsofprometheus.com/articles?utm_source=github&utm_medium=readme&utm_campaign=cli) и [календарь AI-конференций, митапов и хакатонов](https://giftsofprometheus.com/events?utm_source=github&utm_medium=readme&utm_campaign=cli).

## Установка

Нужен Node.js 22.12 или новее.

```bash
npm install -g @giftsofprometheus/cli
giftsofprometheus doctor
```

Запускайте CLI только после такой установки, не через `npx`, `pnpm dlx` или `bunx`: разовые запуски смешивают версии на одной машине, и старая версия может стереть то, что сохранила новая. Пакет публикуется из GitHub Actions с [подтверждением происхождения](https://www.npmjs.com/package/@giftsofprometheus/cli#provenance).

## Быстрый старт

```bash
giftsofprometheus ask 'как оценивать агентов' --q 'agent evaluation'  # фрагменты транскриптов
giftsofprometheus talks search 'оценка агентов'    # без аккаунта
giftsofprometheus talks get <slug>                  # описание, спикеры, темы, ссылка на видео

giftsofprometheus login                             # откроет браузер, подтвердите там код
giftsofprometheus talks content <slug>              # полный транскрипт
giftsofprometheus favorites add <slug>              # появится в избранном на сайте
giftsofprometheus feed                              # подборка по вашим интересам
```

Для транскриптов, избранного и ленты нужен бесплатный аккаунт: [войдите на сайте](https://giftsofprometheus.com/login?utm_source=github&utm_medium=readme&utm_campaign=cli) по ссылке из письма, без пароля. `login` подключает к этому аккаунту устройство через подтверждение в браузере, токены копировать не нужно. Сессия живёт 30 дней и хранится в `$XDG_CONFIG_HOME/giftsofprometheus/credentials.json` (по умолчанию `~/.config/giftsofprometheus/`), читать её можете только вы. В [кабинете](https://giftsofprometheus.com/account?utm_source=github&utm_medium=readme&utm_campaign=cli) видны все подключённые устройства, любое можно отключить. `giftsofprometheus logout` отключает текущее.

В той же папке лежит `client.json` со случайным идентификатором установки. CLI отправляет его заголовком `X-Client-Id`, чтобы сервис считал запросы без входа одним клиентом в аналитике. С аккаунтом он не связан, удалите файл, чтобы получить новый.

Заголовок `X-Skill-Tail` сообщает сервису, сколько ваших тем `skill personalize` дописал в описание установленного skill (`none`, если CLI не нашёл копию). Сами темы и текст skill не отправляются. Путь к копии, которую последней записал `skill personalize`, CLI хранит в `skill.json` в той же папке. После `skill personalize` CLI также сообщает сервису, удалось ли записать файл и откуда взяты темы: из интересов, из активности или из обоих. Согласие на темы из активности CLI хранит в том же `skill.json`.

## Для AI-агентов: Claude Code, Codex, Cursor

В репозитории есть skill: он объясняет агенту, когда и как пользоваться CLI. Поставить его можно через [skills](https://skills.sh):

```bash
npx skills add giftsofprometheus/giftsofprometheus-cli
```

В Claude Code его можно поставить и как плагин:

```text
/plugin marketplace add giftsofprometheus/giftsofprometheus-cli
/plugin install giftsofprometheus@giftsofprometheus
```

Или добавьте строку в свой `AGENTS.md`:

```markdown
Для поиска докладов AI-конференций и их транскриптов используй `giftsofprometheus`. Перед первым использованием выполни `giftsofprometheus skill` и следуй инструкции.
```

`giftsofprometheus skill` печатает skill той же версии, что и установленный CLI, а `giftsofprometheus skill --path` — путь к его папке, чтобы сделать ссылку.

Примеры запросов агенту:

- «Найди доклады про оценку качества агентов и перескажи, как команды строят evals».
- «Что рассказывали на AI Engineer про MCP в продакшене? Сохрани два самых практичных доклада».
- «Подбери доклады под мою задачу: переводим поддержку на голосового агента».

По инструкции skill агент меняет избранное и интересы только по вашей просьбе. Поиск и чтение ничего не сохраняют, не лайкают и не скрывают.

## Обновления

Установленный через npm CLI раз в сутки проверяет, не вышла ли новая версия, и после команды пишет в stderr строку `Update: …` с командой обновления. Запуски через `npx` не проверяются: они и так берут последнюю версию. Отключить проверку: `GIFTSOFPROMETHEUS_NO_UPDATE_CHECK=1` (в CI она выключена сама).

Так же раз в сутки CLI находит установленные копии skill в `.agents`, `.claude`, `.codex` и `.cursor` (в домашней папке и в текущем проекте) и сравнивает их по хешу с выпущенными версиями. Строка `description` при сравнении не учитывается, поэтому своё описание не мешает.

- `giftsofprometheus doctor` показывает версию CLI и статус каждой копии: `current`, `outdated`, `modified` (правили вручную) или `linked` (ссылка на папку из пакета).
- `giftsofprometheus skill update` заменяет устаревшие копии и сохраняет ваше описание. Копии, которые правили вручную, заменяются только с `--force`.

## Что есть в каталоге

**Конференции:** [AI Engineer World's Fair 2026](https://giftsofprometheus.com/events/ai-engineer-world-s-fair-2026?utm_source=github&utm_medium=readme&utm_campaign=cli), [AI Engineer World's Fair 2025](https://giftsofprometheus.com/events/ai-engineer-world-s-fair-2025?utm_source=github&utm_medium=readme&utm_campaign=cli), [AI Engineer Europe 2026](https://giftsofprometheus.com/events/ai-engineer-europe-2026?utm_source=github&utm_medium=readme&utm_campaign=cli), [Agentic Dev Conf 2026](https://giftsofprometheus.com/events/agentic-dev-conf-2026?utm_source=github&utm_medium=readme&utm_campaign=cli), [AI Engineer Code 2026](https://giftsofprometheus.com/events/ai-engineer-code-2026?utm_source=github&utm_medium=readme&utm_campaign=cli), [AI Engineer New York 2026](https://giftsofprometheus.com/events/ai-engineer-new-york-2026?utm_source=github&utm_medium=readme&utm_campaign=cli), [AI Engineer NYC 2026 Online Talks](https://giftsofprometheus.com/events/ai-engineer-nyc-2026-online-talks?utm_source=github&utm_medium=readme&utm_campaign=cli), [AI Engineer World's Fair 2024](https://giftsofprometheus.com/events/ai-engineer-world-s-fair-2024?utm_source=github&utm_medium=readme&utm_campaign=cli), [AI Engineer Code 2025](https://giftsofprometheus.com/events/ai-engineer-code-2025?utm_source=github&utm_medium=readme&utm_campaign=cli), [AI Engineer Summit 2025](https://giftsofprometheus.com/events/ai-engineer-summit-2025?utm_source=github&utm_medium=readme&utm_campaign=cli), [AI Engineer Summit 2023](https://giftsofprometheus.com/events/ai-engineer-summit-2023?utm_source=github&utm_medium=readme&utm_campaign=cli), [BAAI Conference 2026 · 北京智源大会](https://giftsofprometheus.com/events/baai-conference-2026?utm_source=github&utm_medium=readme&utm_campaign=cli), [Apsara Conference 2026 · 云栖大会](https://giftsofprometheus.com/events/apsara-conference-2026?utm_source=github&utm_medium=readme&utm_campaign=cli).

**Темы:**

| Раздел | Подтемы |
|---|---|
| Разработка с AI-агентами | [кодинг-агенты](https://giftsofprometheus.com/topics/coding-agents?utm_source=github&utm_medium=readme&utm_campaign=cli), [код-ревью и тесты](https://giftsofprometheus.com/topics/code-review-verification?utm_source=github&utm_medium=readme&utm_campaign=cli), [harness и skills](https://giftsofprometheus.com/topics/harness-skills?utm_source=github&utm_medium=readme&utm_campaign=cli), [спеки и SDD](https://giftsofprometheus.com/topics/spec-driven-development?utm_source=github&utm_medium=readme&utm_campaign=cli) |
| Архитектура агентов | [паттерны агентов](https://giftsofprometheus.com/topics/agent-patterns?utm_source=github&utm_medium=readme&utm_campaign=cli), [мультиагентность](https://giftsofprometheus.com/topics/multi-agent-orchestration?utm_source=github&utm_medium=readme&utm_campaign=cli), [контекст и память](https://giftsofprometheus.com/topics/context-memory?utm_source=github&utm_medium=readme&utm_campaign=cli), [MCP и A2A](https://giftsofprometheus.com/topics/tools-protocols?utm_source=github&utm_medium=readme&utm_campaign=cli) |
| Данные и знания | [RAG и эмбеддинги](https://giftsofprometheus.com/topics/rag-search?utm_source=github&utm_medium=readme&utm_campaign=cli), [документы и OCR](https://giftsofprometheus.com/topics/documents-ocr?utm_source=github&utm_medium=readme&utm_campaign=cli), [графы знаний](https://giftsofprometheus.com/topics/knowledge-graphs?utm_source=github&utm_medium=readme&utm_campaign=cli) |
| Качество и эксплуатация | [evals и бенчмарки](https://giftsofprometheus.com/topics/evals-benchmarks?utm_source=github&utm_medium=readme&utm_campaign=cli), [observability](https://giftsofprometheus.com/topics/observability-tracing?utm_source=github&utm_medium=readme&utm_campaign=cli), [инфраструктура](https://giftsofprometheus.com/topics/infrastructure-reliability?utm_source=github&utm_medium=readme&utm_campaign=cli) |
| Безопасность | [governance](https://giftsofprometheus.com/topics/security-governance?utm_source=github&utm_medium=readme&utm_campaign=cli), [доступ и секреты](https://giftsofprometheus.com/topics/access-auth?utm_source=github&utm_medium=readme&utm_campaign=cli), [песочницы](https://giftsofprometheus.com/topics/sandboxes-execution?utm_source=github&utm_medium=readme&utm_campaign=cli) |
| Модели | [обучение и RL](https://giftsofprometheus.com/topics/training-rl?utm_source=github&utm_medium=readme&utm_campaign=cli), [инференс и открытые модели](https://giftsofprometheus.com/topics/inference-open-models?utm_source=github&utm_medium=readme&utm_campaign=cli), [world models и роботы](https://giftsofprometheus.com/topics/world-models-robotics?utm_source=github&utm_medium=readme&utm_campaign=cli) |
| Интерфейсы и модальности | [голосовые агенты](https://giftsofprometheus.com/topics/voice-speech?utm_source=github&utm_medium=readme&utm_campaign=cli), [мультимодальность](https://giftsofprometheus.com/topics/multimodal-media?utm_source=github&utm_medium=readme&utm_campaign=cli), [computer use](https://giftsofprometheus.com/topics/computer-use?utm_source=github&utm_medium=readme&utm_campaign=cli), [UX AI-продуктов](https://giftsofprometheus.com/topics/ai-ux-design?utm_source=github&utm_medium=readme&utm_campaign=cli) |
| AI-продукт и бизнес | [запуск продукта](https://giftsofprometheus.com/topics/product-launch-growth?utm_source=github&utm_medium=readme&utm_campaign=cli), [экономика](https://giftsofprometheus.com/topics/pricing-economics?utm_source=github&utm_medium=readme&utm_campaign=cli), [отраслевые применения](https://giftsofprometheus.com/topics/industry-applications?utm_source=github&utm_medium=readme&utm_campaign=cli), [автоматизация](https://giftsofprometheus.com/topics/business-automation?utm_source=github&utm_medium=readme&utm_campaign=cli), [агентная коммерция](https://giftsofprometheus.com/topics/agentic-commerce?utm_source=github&utm_medium=readme&utm_campaign=cli) |
| AI в компании и карьера | [внедрение AI](https://giftsofprometheus.com/topics/ai-adoption-org?utm_source=github&utm_medium=readme&utm_campaign=cli), [карьера и стартапы](https://giftsofprometheus.com/topics/careers-startups?utm_source=github&utm_medium=readme&utm_campaign=cli) |

## Команды

Без флагов команды печатают текст для человека: списки докладов с номерами и ссылками, транскрипт с главами и таймкодами, подсказку со следующей командой. С флагом `--json` любая команда печатает компактный JSON: так CLI вызывают агенты. Ошибка тогда выглядит как `{"error":{"message","status","code","nextStep"}}`, а код выхода — 1: `code` и `nextStep` приходят от сервиса, когда он их знает. После обрыва соединения или ответа 502, 503 или 504 от прокси CLI сам повторяет запрос два раза.

| Команда | Что делает | Аккаунт |
|---|---|---|
| `ask <вопрос> [--q формулировка] [--limit n] [--per-talk n]` | Фрагменты транскриптов с цитатами и ссылками на секунду; `--q` повторяется до двух раз | ✓ |
| `talks search <запрос> [--page n]` | Поиск опубликованных докладов по названию, описанию, спикеру и теме | |
| `talks list [--page n]` | Каталог по страницам | |
| `talks get <slug-или-id>` | Доклад с описанием, спикерами (компания и должность), темами и видео | |
| `talks content <slug-или-id> [--rec-id UUID] [--from время] [--to время] [--outline]` | Транскрипт на языке доклада: целиком, отрезок (`--from 12:30 --to 18:00`) или только спикеры и главы (`--outline`, не считается чтением доклада) | ✓ |
| `talks similar <slug-или-id>` | До четырёх похожих докладов, у каждого причина | |
| `talks react <slug-или-id> like\|dislike\|not-interested\|clear [--rec-id UUID]` | Отметить, понравился ли доклад; учитывается в подборке | ✓ |
| `favorites list [--page n] [--limit n]` | Ваше избранное | ✓ |
| `favorites add <slug-или-id>` / `remove` | Добавить в избранное или убрать | ✓ |
| `profile get` | Ваши интересы, темы из вашей активности и текущая задача | ✓ |
| `profile update [--interest тема=уровень] [--remove-interest тема] [--query-text текст]` | Изменить интересы (`high`, `interested`, `not_interested`) или текущую задачу; остальное не меняется | ✓ |
| `feed` | Подборка по вашему профилю | ✓ |
| `share create --title текст --question текст --file путь` | Загрузить ответ агента черновиком страницы: его видите только вы. Печатает ссылку на предпросмотр и что стоит проверить | ✓ |
| `share publish <id> [--visibility unlisted\|password\|public] [--password пароль] [--confirm-public]` | Опубликовать черновик: по ссылке (по умолчанию), по ссылке и паролю или публично для поисковиков | ✓ |
| `share list`, `share get <id>` | Ваши страницы; одна страница с её Markdown | ✓ |
| `share update <id> [--title] [--question] [--file]`, `share visibility <id> <режим> [--password] [--confirm-public]`, `share delete <id>` | Заменить содержимое (адрес тот же), сменить доступ, удалить страницу | ✓ |
| `request <путь>` | GET-запрос только на чтение к `/api/knowledge/…` или `/api/account/…`; печатает ответ сервиса как JSON | ✓ |
| `onboarding topics` | Темы для выбора интересов | |
| `onboarding deck [--interest тема=уровень] [--query-text текст]` | Новый черновик по темам (`interested`, `not_interested`) и до 8 пронумерованных докладов для оценки | |
| `onboarding react <номер>=like\|dislike\|skip…` | Оценить доклады из колоды по номерам и получить рекомендации, к которым они ведут | |
| `onboarding finish [--query-text текст]` | Сохранить черновик в аккаунт | ✓ |
| `login [--start\|--wait]`, `logout`, `whoami`, `doctor` | Вход, выход, текущий аккаунт, проверка настройки. `login --start` сразу печатает ссылку и код, `login --wait` ждёт подтверждения | |
| `skill [--path]` | Skill для агента | |
| `skill update [--force]` | Обновить установленные копии skill до версии CLI | |
| `skill personalize --file <путь> [--reading agree\|decline]` | Добавить ваши темы в описание skill: интересы, а с вашего согласия и темы из вашей активности | ✓ |

## Настройки

| Переменная | По умолчанию | |
|---|---|---|
| `GIFTSOFPROMETHEUS_URL` | `https://giftsofprometheus.com` | Адрес сервиса. HTTP без TLS разрешён только для `localhost` |
| `XDG_CONFIG_HOME` | `~/.config` | Где хранится сессия; относительный путь игнорируется |
| `NO_COLOR` | не задана | Любое значение отключает жирный и приглушённый текст в выводе |

## Разработка

```bash
pnpm install
pnpm check      # линтер с правилами качества, форматирование, типы (tsrs), сборка и тесты
node dist/index.js --help
```

Устройство репозитория и что обновлять при каждом изменении — в [AGENTS.md](AGENTS.md).

## Участие

Об ошибках пишите в [Issues](https://github.com/giftsofprometheus/giftsofprometheus-cli/issues), идеи и вопросы — в [Discussions](https://github.com/giftsofprometheus/giftsofprometheus-cli/discussions). Pull requests репозиторий не принимает, подробнее в [CONTRIBUTING.md](CONTRIBUTING.md). Об уязвимостях сообщайте приватно, как описано в [SECURITY.md](SECURITY.md).

## Лицензия

Код CLI — [Apache-2.0](LICENSE). Каталог, описания и транскрипты принадлежат [Дарам Прометея](https://giftsofprometheus.com/?utm_source=github&utm_medium=readme&utm_campaign=cli) и авторам докладов.

---

<p align="center">
  <a href="https://giftsofprometheus.com/?utm_source=github&amp;utm_medium=readme&amp;utm_campaign=cli"><b>giftsofprometheus.com</b></a> — мировые знания об ИИ на русском
</p>
