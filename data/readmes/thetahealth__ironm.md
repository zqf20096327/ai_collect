<div align="center">

<img src="docs/readme/logo.png" width="110" alt="IronM" />

# IronM

**The AI fitness coach that sees all your data**

You slept 5 hours, your knee has an old injury, and you only packed one pair of dumbbells for the trip. It knows, and tells you how to train and how much to eat today.

<a href="https://github.com/thetahealth/mirobody">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/readme/powered-by-mirobody-dark.svg">
    <img src="docs/readme/powered-by-mirobody.svg" width="560" alt="Powered by Mirobody: open-source AI health data engine">
  </picture>
</a>

Open source · Use it online or run it yourself · Uses your own LLM

🧪 Evaluated with [mirobody-env](https://github.com/thetahealth/mirobody-env), which builds environments to test the agent thoroughly

**👉 Try it now: <https://ironm.mirobody.ai>** (no install, works in a phone browser)

**English** · [简体中文](README.zh-CN.md)

[![Stars](https://img.shields.io/github/stars/thetahealth/ironm?style=flat&logo=github)](https://github.com/thetahealth/ironm/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/thetahealth/ironm)](https://github.com/thetahealth/ironm/commits/main)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.13-3776AB.svg?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/docker-compose-2496ED.svg?logo=docker&logoColor=white)

[Features](#-what-it-can-do-for-you) · [Screenshots](#-screenshots) · [Try it](#-quick-start) · [FAQ](#-faq)

<img src="docs/readme/home.png" width="190" alt="Home: today's AI workout with the weight for each exercise" />
<img src="docs/readme/plan.png" width="190" alt="AI workout planner: weights from your log" />
<img src="docs/readme/live.png" width="190" alt="Workout logger with camera form check" />
<img src="docs/readme/messages.png" width="190" alt="Messages: IronM's suggestions take effect only when you confirm" />

</div>

- 📷 **It watches you train through your camera**: the moment your back rounds on a squat, it tells you out loud
- 🧠 **A plan that's only yours**: it remembers your injuries, equipment, sleep and every set you've done, and works out the weight for your next one
- ✋ **Every change asks you first**: plan tweaks and calorie changes are suggestions; nothing takes effect until you confirm, and you can always undo
- 🔓 **Open source and free**: bring your own LLM, and keep all your data on your own machine if you like

> **Note:** the app itself is in Chinese for now: the interface, the coach's replies and the built-in content. This README and the code are in English and Chinese.

---

> 😴 **I only slept 5 hours last night. Should I still train today?**
>
> 🐧 **IronM:** Train today, but at about 70%. Don't push through. You slept 5 hours last night, and your last 3 nights average 6.5 hours, 2.2 hours less than your usual 7.2. Your resting heart rate is 62 bpm, the same as usual, so there's no need to skip. Just take it easier.

To answer that, it used your last few nights of sleep, how long you usually sleep, your resting heart rate, and which workout is on today's plan. A training app can't see your sleep, your watch doesn't know what you're training today, and a general-purpose AI needs you to explain everything from scratch every time. IronM sees all three, and after answering it also scales today's workout down to 70%.

## 🤔 How IronM came about

**Training well takes more than training.** Slept badly? Train lighter today. Trained hard? Your protein needs to keep up. Weight not moving on a cut? First look at how much you've trained and eaten over the past few weeks, rather than just eating even less.

**But the data is scattered.** The training app counts sets, the diet app counts calories, the watch tracks sleep, and your lab reports sit in your photo album. Each tool only sees its own slice. Ask an AI coach and it doesn't know you slept 5 hours last night, so all it can give you is advice that would fit anyone.

**Mirobody brought the data together first.** [Mirobody](https://github.com/thetahealth/mirobody) is an open-source, self-hosted AI health data engine: lab reports, Apple Health and wearable data become one standardized health record, with every number traced to its source and readable by AI.

**So we built IronM on it.** A fitness coach that sees your training, food, sleep, heart rate and lab results, and remembers your injuries, equipment and schedule. Building a plan, adjusting today's load, setting next session's weights, changing calories: it looks at everything before deciding. Every change shows up first as a preview card. Nothing takes effect until you tap confirm, and you can undo it.

## 😴 Same bad night's sleep: what it does differently

| | With a single-purpose app | With IronM |
|---|---|---|
| 😴 **Bad night's sleep** | The training app pushes the plan as usual; the watch just says you slept less | Compares sleep and resting heart rate with your usual, then decides: train as planned, lighter, or rest |
| 🤒 **Cold or fever** | Check-in reminders keep coming | No training that day; once you're better, a week at about 70% before going back to your old weights |
| ⚖️ **A week on a cut, weight hasn't moved** | The diet app tells you to eat less | Looks at your 30-day weight trend and what you've trained and eaten; usually leaves calories alone and protects your strength training |
| 💪 **Want to build muscle** | Training and diet set their own goals | Training plan, calories, protein and diet portions all follow the same muscle-gain goal |
| 🧳 **Business trip, one pair of dumbbells** | The plan doesn't work, so you rebuild it when you're back | Swaps to a dumbbell version for those days, remembers your knee injury, and switches back automatically when the trip ends |
| 📅 **Weekly review** | Charts from three apps, viewed separately | Sessions, food, weight, sleep and heart rate side by side, then suggestions on whether to change the plan or calories |

## 💬 Ask it something, and here's the reply

Real conversations from a two-week simulation test. The model is DeepSeek and the user data is simulated. The replies were in Chinese and are translated here; the content is unchanged.

> ⚖️ **I've trained for a week and my weight hasn't moved at all. Should I eat less?**
>
> 🐧 **IronM:** No need to eat less. A single week won't show it, and your weight has been basically flat for 30 days, so leave calories alone for now. Over the last 30 days your first week averaged 66.0 kg and your last week 65.9 kg, a change within normal daily fluctuation. A single weigh-in is affected by water and glycogen, and swings of about 0.35% (about 0.3 kg) within a week are normal.
> 1. Weigh yourself every morning on an empty stomach after the bathroom, for two weeks straight, and look at the weekly average rather than single days
> 2. Do your three strength sessions this week as planned, with 105–132 g of protein a day and 20–25 g per meal, eating 1348 kcal
> 3. If the weekly average still hasn't dropped after two weeks, then talk about cutting calories: change one thing at a time, and keep the deficit under about 500 kcal a day

> 🧳 **I'm travelling Monday to Wednesday next week. The hotel gym only has one pair of dumbbells, 20 kg max.**
>
> 🐧 **IronM:** You can train. For those three days, swap the machine exercises on Monday and Wednesday for dumbbell versions. I've created a preview of the temporary change, and it takes effect once you confirm. Your Monday and Wednesday box squats, cable rows, Romanian deadlifts and lat pulldowns all need machines, and the hotel only has dumbbells. You have a knee injury, so control the depth on squats and use light weights: stop when your thighs are about parallel, and stop if your knee hurts.
> 1. Monday: dumbbell goblet squat (controlled depth, light weight, stop at about parallel, stop if your knee hurts), dumbbell bench press, one-arm dumbbell row, glute bridge, dead bug; sets and reps as planned
> 2. Wednesday: dumbbell Romanian deadlift, dumbbell bent-over row, dumbbell shoulder press, goblet squat (same knee cautions), plank; sets and reps as planned
> 3. Dumbbells go up to 20 kg: pick a weight that leaves 2–3 reps in the tank, squat a bit shallower, and stop if your left knee hurts
>
> Back at your gym on Thursday, train as planned, starting from last session's weights.
>
> Below is the preview of the temporary change. Tap "Confirm" to apply it. It switches back to your normal plan automatically on the end date, and you can also undo it early.

(A preview card for the temporary change follows the reply. It only takes effect once you confirm.)

## ✨ What it can do for you

### 🏋️ Training
- 📷 **AI form check with your camera**: 71 exercises, automatic rep counting, cues mid-rep; the video never leaves your phone
- 🎬 **Train along with creators**: drop in a video where a fitness creator explains their workout and get a plan you can follow: first the creator's original (each exercise tagged with the second it's mentioned and the exact words), then a copy adapted to your equipment, injuries and time
- 📋 **AI workout planner**: built step by step from your level, goal, days, equipment and injuries, with the reason for each step; or pick one of 24 ready-made training plans by name
- 🎥 **Workout video analysis**: upload a clip of yourself training; it finds each rep's problems and the second they happen, and IronM tells you how to fix them. The video isn't uploaded
- 🌅 **A daily check**: decides how you train today from your sleep, heart rate and what you've told it
- 🧳 **Temporary changes**: travel, illness or a deload week, with start and end dates; your normal plan comes back automatically
- ⏱️ **Workout logger**: log set by set, tap a number to fill it in, rest timer between sets, a share card when you finish
- 📈 **Weights and next-session targets**: exercises you've logged show the weight to use; new ones are marked "find your weight" with how to find it the first time. After each session it sets next time's targets from your log
- 🏃 **Cardio by calories**: want to burn an extra N kcal a week? It works out from your body weight how long to walk, jog or cycle, and puts it in your plan
- 📖 **Exercise library**: 220 exercises, about half with images and animations, all with alternatives; 34 kinds of equipment, recognised from a photo

### 🥗 Food
- 📸 **Log a meal with a photo or a sentence**: snap a photo or say "had a bowl of beef noodles for lunch". Calories come from the food database, not from a model's guess
- 🍱 **Diet plan library**: 16 full-day diet plans you can apply in one tap. Portions scale to your calorie target automatically, and you can undo
- 🧮 **Built around you**: say "I mostly eat takeout and don't eat pork", and IronM picks four meals a day from the recipes while the system sets the portions. Daily calories land within 8% of your target, protein is covered, and nothing you avoid is included. Nothing changes until you confirm
- 🎯 **Follows your goal**: switch from fat loss to muscle gain and IronM checks whether your diet plan still fits the new goal; if not, it offers a card to switch plans
- 🥚 **Foods and recipes**: 159 foods, 81 recipes (home cooking, packed lunches, takeout and canteen, vegetarian, weight gain), 12 common takeout and canteen meals
- 🍔 **Chain restaurant menus**: every regular McDonald's item with the nutrition data from its official site; search and log it directly instead of letting a model guess
- ✏️ **Your own entries**: your own foods (copied from the label), exercises and plans, each with an optional photo; usable for logging meals, workouts and planning
- 🔥 **Calorie target**: based on your basal metabolic rate. IronM suggests changes from your records and nothing changes until you confirm, with hard limits in code: never below your BMR, at most 300 kcal per change, at most 500 kcal in total

<details>
<summary>What's in the plan libraries</summary>

<br/>

**Training plans**: beginner full body, upper/lower, push/pull/legs, bro split, dumbbells at home, kettlebell, bodyweight progressions, glutes and legs, big three, strength plus running, coming back after a break, hotel workouts, 60+…

**Diet plans**: balanced home cooking, high-protein fat loss, fat loss on takeout and canteen food, fat loss with packed lunches, muscle gain with home cooking, muscle gain with packed lunches, muscle gain on takeout and canteen food, maintenance, weight gain for skinny people, high-protein vegetarian, Mediterranean, DASH for blood pressure, blood sugar control, lacto-ovo vegetarian, high protein for 60+, time-restricted eating

</details>

### ❤️ Health data
- 🧪 **Lab report reading**: lab results and checkup reports read from a photo (via [mirobody](https://github.com/thetahealth/mirobody))
- ⌚ **Watches and Apple Health**: import your data; every metric is compared with your own usual
- 😴 **Today's sleep and heart rate**: see today's numbers on Home, tap for the last week or month, and log them yourself if nothing synced

### 🧩 Also
- 🔔 **Messages**: the bell at the top holds IronM's adjustments and system messages, each saying what changed and why. Confirm or decline suggestions, undo changes that already took effect, and search by keyword or date
- 🎙️ **Ask by voice**: tap the mic next to the input box and speak; the text fills in and you can edit it before sending. Speech is transcribed on the server with a self-hosted model: free, and the recording is deleted right after
- 🏅 **Badges**: lightest week, squatting 1.5× your body weight, 8 weeks in a row… It only rewards what you've done and never nags
- 🧠 **Long-term memory**: remembers your injuries, equipment, schedule and preferences. If it gets something wrong, delete it under "Me"
- 📚 **Sources**: an evidence base of 125 entries: Chinese dietary guidelines, China's National Health Commission guidance, ACSM, ISSN, NEJM randomised trials… Ask why and it tells you the source
- 🛡️ **Safety floor**: emergencies, critical values, pregnancy, high blood pressure and injuries are handled by hard-coded rules
- 📦 **Your data, your call**: export everything or delete your account at any time

<details>
<summary>📱 What's on each page</summary>

<br/>

Five tabs at the bottom: Home, IronM, Library, Records, Me. The mobile app in progress uses the same layout.

| Page | What's there |
|---|---|
| 🏠 Home | What to train today (with the weather), whether it was adjusted, start a workout, quick check-in; today's meals, tick what you ate as planned or log something else by photo or voice; today's sleep and resting heart rate; this week's plan; trending on the leaderboard |
| 🐧 IronM | Chat by typing or voice; preview cards for plan changes, meals and goal changes; weekly report; send photos and workout videos |
| 🔔 Messages | IronM's adjustments and system messages; suggestions waiting for you at the top; what changed and why; search by keyword or date |
| 📖 Library | Exercises, equipment, foods and recipes, training plan library (train along with creators at the top), diet plan library; your own entries at the bottom of each page |
| 📊 Records | Sessions this week, total time, PRs, compared with last week; body data trends; training timeline and check-in photos; badge wall |
| 👤 Me | Profile and goal, equipment and place, city and weather, body data, things it remembers, data import, model settings, account and privacy |
| 📋 Training plan | The week's schedule; swap exercises, change sets and reps, reorder; the weight to use (or "find your weight") and next-session targets for each exercise |
| ⏱️ Workout | Set-by-set logging, rest timer, add a set, stopwatch; camera form check |
| 🍱 Food log | Today's calorie balance and how the target is calculated; log each meal as planned or what you actually ate; diet plan |

</details>

## 📸 Screenshots

<table>
<tr>
<td align="center"><img src="docs/readme/home.png" width="200" alt="Home: today's AI workout with the weight for each exercise" /><br/><sub><b>Home</b><br/>Today's workout, with the weight to use</sub></td>
<td align="center"><img src="docs/readme/plan.png" width="200" alt="AI workout planner: weights from your log" /><br/><sub><b>Training plan</b><br/>Weights from your log, "find your weight" for new ones</sub></td>
<td align="center"><img src="docs/readme/live.png" width="200" alt="Workout logger with camera form check" /><br/><sub><b>Workout logger</b><br/>Camera form check, tap a number to fill it in</sub></td>
<td align="center"><img src="docs/readme/messages.png" width="200" alt="Messages: IronM's suggestions take effect only when you confirm" /><br/><sub><b>Messages</b><br/>Suggestions take effect only when you confirm</sub></td>
</tr>
</table>

## 🚀 Quick start

### 🌐 Use it online (nothing to install)

1. Open <https://ironm.mirobody.ai> on your phone or computer
2. Sign up with your email (you'll get a verification code), then enter your height, date of birth and weight
3. Under "Me → Model and API", enter your own LLM API key. DeepSeek, Qwen, Zhipu, Doubao, Kimi and OpenAI all work, as does anything with an OpenAI-compatible API; a few yuan of DeepSeek credit lasts a long time. Without a key you can still log workouts and meals and browse the libraries; you just can't ask IronM
4. Tell it: "I want to start training, three times a week, at the gym."

This is a test deployment: it gets updated often and may have rough edges. Keep your own notes of anything you can't afford to lose. On a phone, use "Add to Home Screen" to open it like an app.

### 🖥️ Run it yourself (optional)

If you'd rather keep all your data on your own computer, run your own copy. You need a computer and an LLM API key.

🐳 **With Docker** (Windows, macOS, Linux)

```bash
git clone https://github.com/thetahealth/ironm.git iron-m && cd iron-m
docker compose up -d
```

💻 **Without Docker** (macOS, Linux)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh   # skip if you already have uv; reopen the terminal afterwards
git lfs install
git clone https://github.com/thetahealth/ironm.git iron-m && cd iron-m
scripts/start.sh
```

The first run takes ten-plus minutes to set up the environment and download images and the speech model; after that it starts in seconds. Then:

1. Open <http://127.0.0.1:18090/iron/>, sign up, and enter your height, date of birth and weight
2. Under "Me → Model and API", enter your key
3. Tell it: "I want to start training, three times a week, at the gym."

For port conflicts, slow downloads in mainland China, updating and uninstalling, see [deploy/self-host.md](deploy/self-host.md) (in Chinese).

## 🧠 How it works under the hood

IronM is a single agent: one AI answers every question. Depending on the topic, it first loads the guide for that kind of question (building plans, exercise coaching, nutrition, whether to train today, pain and injuries, reading data, logging and reviews, onboarding; 8 in all, plus one for training along with creators), then looks things up in the plan libraries, exercise library, food database, evidence base and your data. It also works when you're not around: every day it assesses how you should train, after each workout it sets next session's targets, once a week it reviews your progress, and after each chat it sorts out what to remember.

The split is simple: **judgement goes to the AI; numbers and safety limits go to code.** Calories, BMR, macros and how far you are from your usual are all calculated in code. Emergencies, critical values, special groups, injuries and the calorie floor are guarded by code. If a number in the AI's answer doesn't match its source, the answer is sent back to be rewritten. If the AI fails, IronM doesn't quietly fall back to rules that decide for you; it tells you plainly that something went wrong and that you can try again.

The backend is Python 3.13 + FastAPI + PostgreSQL (pgvector), running as a plugin on [mirobody](https://github.com/thetahealth/mirobody) (`vendor/mirobody` is version 1.5.8, unmodified). The web app is plain JavaScript and loads nothing from external sites.

## ❓ FAQ

**💰 Does it cost anything?** IronM is free. Model costs go through your own account; with DeepSeek, a question costs about one fen (well under one US cent), and turning a creator's video into plans costs a few fen. Speech and video transcription run on a self-hosted model on the server, and the camera form check and workout video analysis run on your own phone, so they cost nothing.

**📱 Can I use it on my phone?** Yes: open <https://ironm.mirobody.ai> in your phone's browser; the pages are designed for phone screens. A native app is in progress (the code is in `app/`; it hasn't been released yet).

**🔒 Where is my data?** On the online version, it's stored in the test server's database, with sensitive content encrypted. If you run it yourself, it stays in a database on your own computer. Either way, only your questions and the photos you take are sent to the model provider you configured, and the weather lookup only sends coordinates rounded to about 1 km. Voice and videos are transcribed on the server and deleted right after; a video's text is only used to make the plans and is deleted once you choose (after 7 days at most).

**🩺 Can it replace a coach or doctor?** No. Treat it as advice only. If you have a chronic condition, are pregnant or are injured, check with a doctor before you start. If you get chest pain, dizziness or shortness of breath while exercising, stop and get medical help right away.

## 🛠️ Development

```bash
git lfs install && git lfs pull        # vendor/mirobody contains two git-lfs files
cp .env.example .env                   # fill it in, then chmod 600 .env
make setup                             # Python environment
make pg-install pg-init                # local PostgreSQL 18 + pgvector (needs micromamba)
make run                               # http://127.0.0.1:18090
```

For evaluation we use [mirobody-env](https://github.com/thetahealth/mirobody-env), which builds environments to test the agent thoroughly.

## 🙏 Acknowledgements

The health data foundation comes from [mirobody](https://github.com/thetahealth/mirobody). Exercise images come from [wger](https://wger.de) and [Everkinetic](https://github.com/everkinetic/data) (CC BY-SA), food photos from Unsplash and Pexels, and leaderboard images from Wikimedia Commons. Authors and licences are recorded in `ironm_agent/*_images.yaml` and credited in the app. Images aren't stored in the repository; they're downloaded from that list at install time. Nutrition data draws on USDA FoodData Central. Speech and video transcription uses [SenseVoice-Small](https://github.com/FunAudioLLM/SenseVoice) from Alibaba Tongyi Lab (FunASR model licence), run with [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx); audio is extracted from videos with [PyAV](https://github.com/PyAV-Org/PyAV) (bundling FFmpeg libraries).

## 🤝 Contributing

[Issues](https://github.com/thetahealth/ironm/issues) are welcome: tell us what works well, what feels awkward, or what you'd like to see. Pull requests are welcome too. For bigger changes, please open an issue first to discuss the direction.

## ⭐ Star history

[![Star History Chart](https://api.star-history.com/svg?repos=thetahealth/ironm&type=Date)](https://star-history.com/#thetahealth/ironm&Date)

## 📄 License

[Apache License 2.0](LICENSE)

<div align="center">

<br/>

If IronM helps you, a ⭐ would mean a lot

</div>
