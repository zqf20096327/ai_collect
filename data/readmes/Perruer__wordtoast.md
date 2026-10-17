<p align="center">
  <img src="src/icons/icon.svg" width="96" height="96" alt="WordToast logo">
</p>

<h1 align="center">WordToast</h1>

<p align="center">
  <b>Translate what you select, keep the words you want to learn, and review them in little pop-up toasts.</b><br>
  For Firefox, Edge and Chrome. Google, DeepL, on-device, or your own AI model.
</p>

<p align="center">
  <a href="#install">Install</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="#translation-engines">Engines</a> ·
  <a href="#support-the-project">Support</a> ·
  <a href="#русский">Русский</a>
</p>

<p align="center">
  <img src="docs/demo.gif" width="880" alt="Selecting a German word, seeing the translation card, saving it and asking AI to explain it">
</p>

## Features

- **Translate any selection.** Select a word or a paragraph on any page and click the toast button
  that appears, press <kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>E</kbd>, or use the right-click menu.
  Translations go into your browser language automatically.
- **A card that teaches.** Alternative meanings by part of speech, English definitions with examples
  and pronunciation, text-to-speech, one-click copy.
- **Explain with AI.** Connect OpenAI, Claude, Gemini or any OpenAI-compatible model (OpenRouter,
  a local Ollama) with your own key, and get the meaning *in this context*, examples and usage notes.
- **Wordbook.** Star a word and it's saved together with the sentence you found it in and a link to
  the page. Search it, export it to **Anki**, CSV or JSON.
- **Review toasts.** Saved words pop up in the corner of the page at growing intervals
  (5 min → 30 min → 12 h → 1, 3, 7, 21, 60 days). "Remembered" moves a word forward, "Forgot"
  starts over. Or run a flashcard session in the wordbook.
- **Private by default.** No accounts, no analytics. Your wordbook and keys stay in your browser.
  In Chrome you can even translate fully on-device.
- English and Russian interface, light and dark theme, per-site off switch.

<table>
  <tr>
    <td><img src="docs/screenshots/en/03-toast.png" alt="Review toast in the corner of a page"></td>
    <td><img src="docs/screenshots/en/04-wordbook.png" alt="Wordbook with context sentences and learning progress"></td>
  </tr>
</table>

## Install

| Browser | How |
|---|---|
| **Firefox** | [Firefox Add-ons (AMO)](https://addons.mozilla.org/firefox/addon/wordtoast/) |
| **Microsoft Edge** | Manual install from [GitHub Releases](https://github.com/Perruer/wordtoast/releases), the same steps as for Chrome at `edge://extensions` |
| **Chrome, Brave, Vivaldi, Opera** and other Chromium browsers | Manual install from [GitHub Releases](https://github.com/Perruer/wordtoast/releases), see below |

### Chrome: manual install from GitHub Releases

WordToast is not in the Chrome Web Store, but Chrome can load it directly:

1. Open the [latest release](https://github.com/Perruer/wordtoast/releases/latest) and download
   **`wordtoast-chrome-<version>.zip`**.
2. Unzip it into a folder you will keep, for example `Documents\WordToast`.
   Don't delete the folder afterwards: Chrome loads the extension from it.
3. Open **`chrome://extensions`** in the address bar.
4. Turn on **Developer mode** (toggle in the top-right corner).
5. Click **Load unpacked** and select the unzipped folder, the one that contains `manifest.json`.
6. Click the puzzle icon 🧩 on the toolbar and pin **WordToast** 📌.

To update, download the new zip, replace the files in the same folder and press the ↻ reload
button on the WordToast card in `chrome://extensions`. Your wordbook and settings are kept.

> Chrome may show a banner about extensions in developer mode on startup. It's safe to dismiss:
> it appears for every extension that isn't installed from the Chrome Web Store.

The same steps work in Brave (`brave://extensions`), Vivaldi, Opera and Edge (`edge://extensions`).

## How it works

1. **Select** text on a page. A small toast button appears next to it (or the card opens right away
   if you prefer; see Settings → Behavior).
2. **Read** the card: translation, other meanings, definitions. Press 🔊 to hear it, ★ to save it.
3. **Review**: saved words come back as toasts in the corner of whatever page you're reading.
   Show the translation, then tell WordToast whether you remembered it.

<img src="docs/screenshots/en/02-explain.png" width="640" alt="Translation card with an AI explanation of the word in context">

The toolbar popup translates typed text and shows how many words are due for review.
Right-click the toolbar icon to open the wordbook.

<img src="docs/screenshots/en/popup.png" width="300" alt="Toolbar popup">

### Languages

WordToast translates into your **browser language**. If the text is already in that language, it
translates into a **second language** instead (English by default; for English speakers it shows the
English dictionary). Both can be changed in the settings, together with 40+ supported languages.

## Translation engines

| Engine | Cost | Setup | Notes |
|---|---|---|---|
| **Automatic** (default) | free | none | Google Translate, falls back to MyMemory |
| **On-device** | free | none | Chrome 138+ desktop. The text never leaves your computer; language packs download on first use |
| **Google Translate** | free | none | Fast; heavy use may be rate limited |
| **MyMemory** | free | optional e-mail | 5,000 characters/day, 50,000 with an e-mail |
| **DeepL** | free plan / paid | your API key | High quality, 500,000 characters/month on the free plan |
| **AI model** | pay per use | your API key | OpenAI, Anthropic (Claude), Google Gemini, or any OpenAI-compatible endpoint (OpenRouter, Ollama, LM Studio…) |

The AI model also powers **Explain with AI**. Default models: `gpt-4.1-mini` (OpenAI),
`claude-opus-5` (Anthropic), `gemini-2.5-flash` (Gemini); any other model name can be entered.
You pay the provider directly; WordToast adds nothing on top, and your key is sent only to that provider.

<img src="docs/screenshots/en/06-ai-settings-dark.png" width="640" alt="AI settings">

## Privacy

WordToast has no server and collects nothing. The text you choose to translate is sent to the engine
you picked (Google, MyMemory, DeepL or your AI provider), and English words to the Free Dictionary
API. The wordbook, settings and API keys are stored only in your browser. Details in the
[privacy policy](PRIVACY.md).

## What's new compared to Dadda Translate

WordToast 2.0 is a full rewrite of [Dadda Translate (达达划词翻译)](https://github.com/waynecz/dadda-translate-crx),
which stopped working when the Sogou and Shanbay APIs it relied on changed or disappeared.

- Manifest V3; one code base for Chromium and Firefox (Dadda was Chrome-only).
- New engines: Google, MyMemory, DeepL, Chrome's on-device translator and any AI model; automatic
  fallback. No more fetching and `eval`-ing a script from the translation site.
- Any language pair instead of English → Chinese only; English and Russian interface.
- "Explain with AI" in context.
- Review toasts inside the page with "remembered / forgot" answers and a proper spaced-repetition
  schedule (Dadda showed repeating system notifications); flashcard review in the wordbook.
- Wordbook keeps the context sentence and the source page; Anki/CSV/JSON export, JSON import.
- Available for Edge ([dadda#272](https://github.com/waynecz/dadda-translate-crx/issues/272)), lets you
  use your own API key ([dadda#247](https://github.com/waynecz/dadda-translate-crx/issues/247)) and choose
  the engine ([dadda#244](https://github.com/waynecz/dadda-translate-crx/issues/244)).
- Shanbay / Youdao wordbook sync was dropped: Shanbay's API no longer exists, and both services
  require Chinese accounts.

Full list in the [changelog](CHANGELOG.md).

## Build from source

Requires Node.js 20+.

```bash
npm install
npm run build        # dist/chrome and dist/firefox (unpacked)
npm run dev          # rebuild on change
npm test             # unit tests
npm run test:e2e     # end-to-end tests in Chrome for Testing and Firefox (mocked services)
npm run lint         # web-ext lint for the Firefox build
```

The code is TypeScript + [Preact](https://preactjs.com), bundled with esbuild but not minified.
See [BUILD.md](BUILD.md) for details. Bug reports and pull requests are welcome in
[Issues](https://github.com/Perruer/wordtoast/issues).

## Support the project

WordToast is free, open source, and has no ads or tracking. If it helps you
learn languages, you can support its development:

- **Boosty:** https://boosty.to/mikio_kuroki/donate
- **USDT / TRX, TRON (TRC-20):** `TXUBW4e88SDTfrnJRKfbhYfFcggufbonc1`
- **USDT / USDC / ETH, Ethereum or any EVM network (ERC-20):** `0x1378491169064702786b2E5b58c6375776177E8A`
- **TON / USDT on TON:** `UQAhI7EKzoa-JuKOfv0ULMzA3FrmpxsDkXj8Qevwj2z1cMRN`

Send only on the network listed next to each address. Starring the repository,
leaving a review on the add-on page and reporting bugs help a lot too.

## Based on Dadda Translate by Waynecz

WordToast is a rewrite of [Dadda Translate (达达划词翻译)](https://github.com/waynecz/dadda-translate-crx)
by [Waynecz](https://github.com/waynecz), released under the MIT License. The idea of the
translation card, the wordbook and the "toast words" review comes from Dadda. Thank you!
The original copyright notice is kept in [LICENSE](LICENSE); see also
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## License

[MIT](LICENSE) © 2018 Black Wayne (Waynecz), © 2026 Perruer

---

## Русский

**WordToast** переводит выделенный текст на любой странице, сохраняет слова, которые вы хотите
выучить, и напоминает их маленькими всплывающими «тостами». Работает в Firefox, Edge и Chrome.

<img src="docs/screenshots/ru/01-card.png" width="640" alt="Карточка перевода на русском">

### Возможности

- **Перевод выделенного:** кнопка-тост рядом с выделением, <kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>E</kbd>
  или контекстное меню. Переводит на язык браузера; если текст уже на нём — на второй язык (английский).
- **Карточка:** другие значения по частям речи, английские определения с примерами и транскрипцией,
  озвучка, копирование.
- **Объяснить с ИИ:** подключите OpenAI, Claude, Gemini или любую OpenAI-совместимую модель
  (OpenRouter, локальная Ollama) со своим ключом — и получите значение слова именно в этом контексте,
  примеры и особенности употребления.
- **Словарик:** слово сохраняется вместе с предложением и ссылкой на страницу. Экспорт в **Anki**,
  CSV и JSON.
- **Тосты для повторения:** слова всплывают в углу страницы через 5 мин, 30 мин, 12 ч, 1, 3, 7, 21 и
  60 дней. «Вспомнил» — дальше, «Забыл» — сначала. Есть и режим карточек в словарике.
- **Приватность:** без аккаунтов и аналитики, словарик и ключи хранятся только в браузере. В Chrome
  можно переводить полностью офлайн.
- Интерфейс на русском и английском, светлая и тёмная тема.

### Установка

- **Firefox:** [Firefox Add-ons](https://addons.mozilla.org/firefox/addon/wordtoast/)
- **Microsoft Edge:** вручную из GitHub Releases, так же, как в Chrome, только на странице `edge://extensions`
- **Chrome** и другие браузеры на Chromium (Brave, Vivaldi, Opera), вручную:
  1. Скачайте **`wordtoast-chrome-<версия>.zip`** со страницы
     [последнего релиза](https://github.com/Perruer/wordtoast/releases/latest).
  2. Распакуйте архив в папку, которую не будете удалять, например `Документы\WordToast`.
  3. Откройте в адресной строке **`chrome://extensions`**.
  4. Включите **«Режим разработчика»** (переключатель справа вверху).
  5. Нажмите **«Загрузить распакованное расширение»** и выберите распакованную папку (ту, где лежит `manifest.json`).
  6. Нажмите на значок пазла 🧩 на панели и закрепите **WordToast** 📌.

  Для обновления скачайте новый архив, замените файлы в той же папке и нажмите ↻ на карточке
  WordToast в `chrome://extensions`. Словарик и настройки сохранятся.

### Движки перевода

По умолчанию — Google с запасным MyMemory, бесплатно и без настройки. Также доступны офлайн-переводчик
Chrome, DeepL (ваш ключ, бесплатный тариф 500 000 символов в месяц) и ИИ-модель (ваш ключ, оплата
напрямую провайдеру). Выделенный текст отправляется только выбранному сервису; подробнее — в
[политике конфиденциальности](PRIVACY.md).

### Поддержать проект

WordToast бесплатный, без рекламы и слежки. Если он помогает вам учить языки, можно поддержать разработку:

- **Boosty:** https://boosty.to/mikio_kuroki/donate
- **USDT / TRX (TRON, TRC-20):** `TXUBW4e88SDTfrnJRKfbhYfFcggufbonc1`
- **USDT / USDC / ETH (Ethereum или любая EVM-сеть):** `0x1378491169064702786b2E5b58c6375776177E8A`
- **TON / USDT в сети TON:** `UQAhI7EKzoa-JuKOfv0ULMzA3FrmpxsDkXj8Qevwj2z1cMRN`

Отправляйте только в сети, указанной у адреса. Звезда на GitHub и отзыв в каталоге дополнений тоже очень помогают.

WordToast основан на [Dadda Translate](https://github.com/waynecz/dadda-translate-crx) от Waynecz (лицензия MIT).
