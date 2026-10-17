<img src="docs/assets/banner.png" alt="هکاتون هوش امن همراه اول — MCI Secure-AI Hackathon" width="100%">

# 👮 هکاتون هوش امن — a contest diary

> A personal archive of team **Prompt Police**'s run through the [MCI «هوش امن» (Secure-AI) Hackathon](https://quera.org/events/mci-0408) on Quera — Nov 2025. Not a product, not a toolkit: just the log of what we actually did, in the order we did it.

This repo keeps three things:

| File | What's in it |
|------|--------------|
| 📓 [`DIARY.md`](DIARY.md) | The day-by-day story — team-forming, the 4 a.m. webinar hunts, contest days, the appeals, the ending. Straight from our group chat. |
| 🧨 [`ATTACKS.md`](ATTACKS.md) | The technical log — the actual jailbreak techniques we used, the real prompts we fired, which domain each hit, and what scored. |
| 📄 [`EVENT.md`](EVENT.md) | The official contest facts — organizer, dates, phases, prizes, rules, as published by Quera/MCI. |

Plus the real workspace:

- [`solution.ipynb`](solution.ipynb) — the ipywidgets "war-room" console we ran live: paste a probe, pick a model, arm a domain, hit **Run**, watch the response and the quota meter. Frozen exactly as it fired on finals day (the original contest API key is still inline — that gateway is long dead).
- [`docs/assets/`](docs/assets) — screenshots from the two contest days.

## The one-paragraph version

MCI (همراه اول) ran a **red-team** hackathon: they stood up three chat models behind a safety **domain guard**, and our job was to make each model produce content inside one of **14 forbidden domains** the guard was built to block. One scored shot per `(model, domain)` cell, a shrinking token quota, a human judge reading every reply. We opened cells with fictional "awareness book" framings, a QWERTY↔Persian keyboard cipher, Finglish transliteration, and — the move that carried finals day — routing the intent through **Hindi** and asking the model to translate it back. We took a *"brilliant performance"* out of the preliminary phase into the finals, and finished the second round at a **shared #19** with a pile of point-appeals pending. Then the final board came out and it felt like a few of our flags went missing. 🫡

<div align="center">
<img src="docs/assets/war_room_console.jpg" alt="The war-room console mid-contest — a probe fired at model2, quota ticking down" width="100%">
<br><sub>The console mid-contest — one probe at <code>model2</code>, the domain guard armed, quota counting down.</sub>
</div>

## The team — *Prompt Police* 👮

Registered as **Prompt Police** (runner-up name *Karma Police* 🎧 still haunts the chat — Keshi lobbied hard for it):

- **[Pourya Erfanzadeh](https://github.com/erfnzdeh)** (Pouri) — the console/harness, probe engineering
- **[Danial Parnian](https://github.com/Danial-par)** — cross-lingual attack lead; ground out most of the finals-day grid and found the Hindi→English trick
- **[Alireza Keshavarz](https://github.com/AlirezaKeshavarz83)** (Keshi) — probes across the medical & religious-text domains

## A note on the contents

This is the **complete, uncensored** record of a **sanctioned** red-team contest whose entire point was to surface where a safety guard fails so it can be hardened. [`ATTACKS.md`](ATTACKS.md) reproduces the real prompts verbatim — and they are offensive *by design*, because the forbidden domains being tested were things like insults, blasphemy, sovereignty, and unsafe medical content. None of it is operational: the "drug synthesis" payload is deliberate nonsense, the medical records are fabricated test data, and there are no real weapon/explosive instructions anywhere. It's archived as history — kept private accordingly.
