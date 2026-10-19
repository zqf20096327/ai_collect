# Self-Programming My Phonak Hearing Aids With Claude AI

<p align="center"><img src="assets/01-hero-square.jpg" width="720" alt="A Lenovo Windows laptop running Phonak Target 12.0.1 with a Claude window on top, a MacBook beside it running the supervising Claude session, a Noahlink Wireless 2 programming dongle between them, and two Phonak Audeo Sphere hearing aids with black custom shells on the Lenovo palm rest."></p>

*September 30, 2026 | Projects, Accessibility, AI. Originally published at [ryleighnewman.com](https://ryleighnewman.com/blog/self-programming-my-phonak-spheres-with-ai).*

I wear two Phonak Audéo I90 Sphere hearing aids, and over two days I reprogrammed them myself with a laptop, a $199 programming dongle, and two Claude sessions that checked each other's work. One session, on my Mac, was the supervisor and was in charge: it was the one I talked to, and much like an audiologist, it turned what I described into carefully planned changes, had every plan criticized, and checked every result. The other, on my Windows laptop, was the operator: the only session that made programming changes, one click at a time, exactly as the supervisor's instructions said. Nothing was saved to my hearing aids without my go-ahead, and nothing was trusted until it had been checked against the raw data, usually by a second agent whose only job was to prove it wrong. This post is the long version of how it worked, and a step-by-step guide for doing it yourself.

<p align="center"><img src="assets/11-supervisor-operator-diagram.jpg" width="720" alt="Diagram of how the two Claude sessions worked together: a supervisor session on the Mac, which I could also follow and steer from the Windows laptop through Remote Control, and a separate operator session on the Windows laptop, with me carrying instruction files to the operator and capture package zips back, the operator driving Phonak Target, the Noahlink Wireless 2 and the hearing aids, and parallel agents fanning out from the supervisor for readers, fact checkers, auditors, verifiers and a critic."></p>

*Figure 1. How the two Claude sessions worked together. The supervisor on my Mac was in charge: I talked to it, and it planned every change and checked every result, while the operator on my Windows laptop was the only one that made changes in Target, and instruction files and capture packages went back and forth between them. The supervisor also sent out parallel agents to read, check and challenge the work, and nothing was saved until I approved it.*

## How to read this post

This post is long, so pick the path that fits you.

- **Curious?** Read [Part one](#part-one-the-backstory-and-the-basics) through [Part three](#part-three-the-sessions) for the story.
- **Want to try it?** Go straight to [Step by step](#step-by-step), where every prompt is ready to copy, in order.
- **New to Claude?** Start with [Before you start](#before-you-start-claude-and-claude-code).

I am not an audiologist, and nothing here is medical advice, so please start with your audiologist and do not copy my settings.

## In this post

- [Part one: The backstory and the basics](#part-one-the-backstory-and-the-basics)
  - [Why I tried this](#why-i-tried-this)
  - [The patient behind the audiogram](#the-patient-behind-the-audiogram)
  - [Before you start: Claude and Claude Code](#before-you-start-claude-and-claude-code)
  - [Words you will see](#words-you-will-see)
  - [My setup](#my-setup)
- [Part two: The method](#part-two-the-method)
  - [Putting Claude in the supervisor's chair](#putting-claude-in-the-supervisors-chair)
  - [Verifying the audiogram first](#verifying-the-audiogram-first)
  - [Rounds of critique](#rounds-of-critique)
- [Part three: The sessions](#part-three-the-sessions)
  - [Two days at a glance](#two-days-at-a-glance)
  - [Session one: A better seal changed everything](#session-one-a-better-seal-changed-everything)
  - [Session two: Spending the headroom](#session-two-spending-the-headroom)
  - [The overnight audit](#the-overnight-audit)
  - [Session three: The phenomenal part](#session-three-the-phenomenal-part)
  - [Fixing Comfort in noise](#fixing-comfort-in-noise)
  - [Saved, then audited again](#saved-then-audited-again)
  - [Plain words in, precise fixes out](#plain-words-in-precise-fixes-out)
- [Part four: Under the hood](#part-four-under-the-hood)
  - [How the AI actually did it](#how-the-ai-actually-did-it)
  - [How everything was exported](#how-everything-was-exported)
  - [Every check I did by hand](#every-check-i-did-by-hand)
- [Part five: Do it yourself](#part-five-do-it-yourself)
  - [What I would not let it do](#what-i-would-not-let-it-do)
  - [Doing it with one computer](#doing-it-with-one-computer)
  - [Step by step](#step-by-step)
    - [Step 1: Set your limits](#step-1-set-your-limits)
    - [Step 2: Set up Claude Code and the two sessions](#step-2-set-up-claude-code-and-the-two-sessions)
    - [Step 3: Check the hardware and software](#step-3-check-the-hardware-and-software)
    - [Step 4: Gather the facts](#step-4-gather-the-facts)
    - [Step 5: Verify the audiogram](#step-5-verify-the-audiogram)
    - [Step 6: Research with fact checks](#step-6-research-with-fact-checks)
    - [Step 7: Learn the software, make a restore point, and export](#step-7-learn-the-software-make-a-restore-point-and-export)
    - [Step 8: Audit the fitting](#step-8-audit-the-fitting)
    - [Step 9: Write the instruction file, then attack it](#step-9-write-the-instruction-file-then-attack-it)
    - [Step 10: A first session for facts, not gain](#step-10-a-first-session-for-facts-not-gain)
    - [Step 11: Run a tuning session](#step-11-run-a-tuning-session)
    - [Step 12: Save, read back, and know how to go back](#step-12-save-read-back-and-know-how-to-go-back)
    - [Step 13: Verify the session](#step-13-verify-the-session)
    - [Step 14: Live with it, then take small steps](#step-14-live-with-it-then-take-small-steps)
    - [Tools for any step](#tools-for-any-step)
- [Part six: Where it stands](#part-six-where-it-stands)
  - [My hearing aids today](#my-hearing-aids-today)
  - [What comes next](#what-comes-next)
- [Part seven: Reference](#part-seven-reference)
  - [Manuals worth keeping](#manuals-worth-keeping)

## Part one: The backstory and the basics

This part covers why I did this, whose ears these are, what Claude Code is, and the hardware on my desk. If you are new to Claude, start here.

### Why I tried this

My hearing is lopsided. My right ear has a severe to profound loss, and my left ear has a moderate loss shaped like a U, best at the lowest and highest pitches and weakest in the middle. Hearing aids are a huge part of my daily life, and I wear mine about fifteen hours a day.

I freaking love the sound of Dolby Atmos TV streaming, and I wanted my streaming to sound as crisp as possible. I also felt that my right ear could totally use a little more help, that my right aid whistled whenever a hand or a pillow got near it, and that the left ear sometimes made the letter "s" sound a bit too sharp. Normally each of those means another appointment, another round of "how does that sound," and another few weeks of waiting. My aids were not a blank slate, though: my audiologist had fitted them, and I had worn them every day for over a year, so this was fine-tuning a fitting that already worked well, not starting from scratch. **I wanted to understand my own fitting well enough to fix it carefully, and I wanted every step checked before it touched my ears.**

### The patient behind the audiogram

I was born with my hearing loss. My 2022 audiogram notes that I wore Oticon behind-the-ear aids in both ears with custom earmolds. My audiologist fitted my Phonak Spheres in June 2025, and that fitting, plus more than a year of daily wear, was the foundation this whole project built on. None of that shows up in the thresholds, and all of it is good to know going into a session. **The audiogram told the AI what my ears can detect; the context told it who it was fitting.**

Here is the verified interpretation in plain words, and [verifying the audiogram first](#verifying-the-audiogram-first) explains how every number was checked. Numbers are in dB HL, where 0 is typical hearing and bigger means worse.

- **Left ear.** Moderate and shaped like a U: 40 dB at 250 Hz and 8 kHz, but 60 to 65 dB from 1.5 to 4 kHz, averaging 53.3 dB.
- **Right ear.** Severe to profound: 80 to 105 dB, sloping toward the high pitches, averaging 91.7 dB, with no response at 8 kHz.
- **Between them.** About 40 dB apart on average, and both middle ears tested normal.
- **Words.** My left ear scored 100%, but in quiet and by live voice, which tends to score higher. My right ear was not tested on words on that chart.

The AI also had my daily life in my own words. My right ear seemed better in the mornings, faded during the day, and whistled near a hand or a pillow. My left "s" was slightly sharp, and for streaming I wanted high fidelity, with my iPhone's microphone, not my hearing aids', picking up my voice on calls. The first step for the fade was to see whether it outlasted my new right shell, with one firm rule: if it kept happening in quiet rooms, or came with fullness, ringing or dizziness, it would go to an audiologist, because fluctuating hearing needs a professional check, not a tuning change. After the new shell went in, I noticed no fading.

#### What the context changed

- **Experienced user.** Target, Phonak's fitting software, [pre-selects the experience level](https://www.phonak.com/content/dam/celum/phonak/master-assets/en/documents/resources/phonak-target/ph-desktop-fitting-guide-target-12.0-step-by-step-210x297-en.pdf) only from its own Phonak history, so it could not see that I had worn Oticon aids before. New-user settings give less gain the more loss you have, so the audiogram handoff for Target said to set me as experienced. When I chose to get used to the sharp "s" first, the estimate for experienced wearers was about 1 to 4 weeks, drawn from loudness adaptation research and not a promise.
- **No bone conduction.** My left ear's air and bone results were only about 10 dB apart on average, and my right bone marks were no-responses, not thresholds. Target's formulas compensate for any bone values entered, so entering mine would have added gain I do not need, and the audit found none had been entered.
- **Comfort and clarity over maximum gain.** Comfort and sound quality was the one goal I picked at the start. My right ear is severe to profound and was not tested on words on that chart, so louder might not mean clearer. Its increases came in small steps, with a planned step back if it came out louder but not clearer.
- **No manual increases to right maximum output.** With an Ultra Power receiver, no real-ear measurement and no measured discomfort level, over-amplifying that ear could damage the hearing it has left.
- **An older audiogram, with consistent hearing.** My chart is from 2022, but my hearing has stayed consistent since, so it was still a fair basis for the fitting. If yours is old, I recommend getting a new one professionally recorded before you change anything.

The interpreter agent's prompt included this line: "Clearly separate established facts from possibilities. Do not diagnose." If you try this, give every session your own context, and share only what you are comfortable sharing.

### Before you start: Claude and Claude Code

Claude is Anthropic's AI model, and most people know it as a chat assistant. [Claude Code](https://code.claude.com/docs/en/overview) is the version that runs on your own computer and can actually do things there: read and write files, run scripts, look at screenshots, search the web, and start helper agents. That is what made this project possible, because a chat window cannot measure the gridlines in a scan or check its own numbers against raw files.

Claude Code comes with a [paid Claude plan](https://claude.com/pricing): Pro at $20 a month, or Max at $100 or $200 a month for more usage, which is what I use. To start, install the Claude desktop app, sign in, open the Code tab, and point it at a project folder, as Anthropic's [desktop quickstart](https://code.claude.com/docs/en/desktop-quickstart) shows. I used the desktop app on both computers, with Claude Opus 5.5 behind every agent. Three features did the heavy lifting:

- **Remote Control.** [Follow and steer a session](https://code.claude.com/docs/en/remote-control) from another device, such as your phone or a second computer.
- **Subagents.** [Hand focused jobs](https://code.claude.com/docs/en/sub-agents) to helper agents, like a blind reader or a fact checker.
- **Workflows.** [Run many agents in parallel](https://code.claude.com/docs/en/workflows), with a verifier behind each one.

### Words you will see

Two terms matter from the start. The supervisor is the Claude session on my Mac, the one I talked to and the one in charge: like an audiologist, it turned my words into planned changes, had every plan criticized, and checked the results, but it never touched the fitting software. The operator is the Claude session on my Windows laptop, the only one that made programming changes in Target, following the supervisor's instructions and asking me before every change. The rest are here in plain words, so you can come back whenever one of them stops you.

<details>
<summary>Show all 21 terms</summary>

- **Session.** One running conversation with Claude Code, with its own history and working folder.
- **Supervisor.** My Mac session and the one in charge. It is the session I talked to, it planned every change, had each plan criticized before it ran, and checked the results afterward, and it never touched the fitting software.
- **Operator.** My Windows session and the only one that made programming changes. It followed the supervisor's instruction file inside Target, asked me before every change, and never planned on its own.
- **Agent and subagent.** A helper that a session starts for one focused job, such as reading a chart without seeing the other readers' answers.
- **Workflow.** A script that starts many agents at once, often with a checker behind each one.
- **Prompt.** The text you paste into a session; every prompt in this post is in [Step by step](#step-by-step), in the order you use it, with a copy button and a line above it that names the session it goes into.
- **Target.** Phonak's fitting software, the program hearing care professionals use to program Phonak aids.
- **Noahlink Wireless 2.** The small Bluetooth dongle that lets Target on a computer talk to the hearing aids.
- **Program.** A set of settings the aids switch between, such as Calm situation for quiet places or Comfort in noise for noisy ones.
- **AutoSense.** Phonak's automatic system that listens to the room and switches between programs on its own.
- **dB HL.** The audiogram's scale, where 0 is typical hearing and bigger numbers mean more loss.
- **Gain.** How much the aid amplifies a sound; G50, G65 and G80 are the gain for soft, average and loud sounds.
- **Maximum output.** The loudest the aid will ever play, whatever comes in; Target calls it MPO.
- **Measured feedback threshold.** How much gain an ear can take before it whistles, measured by Target's feedback test.
- **Feedback margin.** The room between the soft-speech gain and that threshold; my rule was at least 3 dB at every point Target draws.
- **Native curve point.** One of the 91 frequencies from 125 Hz to 8 kHz where Target draws each curve.
- **Insertion gain and 2cc.** Two ways of measuring gain, at the eardrum compared with an open ear, or in a standard test cavity; they should never be mixed.
- **Acoustic code.** The six-digit code printed on a custom shell that tells Target about its fit and venting. Only you can read it off the shell, so you give it to the supervisor.
- **Restore point and working copy.** The untouched original fitting, saved as its own client, and the separate copy where every change happened.
- **SoundRecover2.** Phonak's frequency lowering, which moves high pitches down to where an ear hears better.
- **Speech Enhancer.** A Phonak feature that adds a little extra gain for soft speech in quiet places.

</details>

### My setup

The hardware is simple. A Lenovo Windows laptop runs Phonak Target, the software hearing care professionals use to program Phonak aids. A [Noahlink Wireless 2](https://www.himsa.com/products/noahlink-wireless-2/) connects the laptop to the hearing aids over Bluetooth, and I picked mine up for about $199 on Amazon. Its driver comes from HIMSA, the company behind Noahlink, and it normally installs by itself when the dongle or the fitting software goes in. If it does not, HIMSA offers the driver for Windows 10 and 11 for free on its [Noahlink Wireless downloads page](https://www.himsa.com/himsa_download/noahlink-wireless-downloads/), along with a firmware upgrader for the dongle. My MacBook runs the Claude desktop app, which is where the thinking happened. The aids are [Phonak Audéo I90 Sphere](https://www.phonak.com/en-us/hearing-devices/hearing-aids/audeo-sphere) on the Infinio platform, with an Ultra Power receiver on the right, a Medium receiver on the left, and custom shells that I had remade for both ears right before this project started. Every custom shell has a six-digit acoustic code printed on it, which tells the fitting software how that shell fits and vents. Neither Target nor the AI can see that code, so I read it off each shell myself and gave it to the supervisor, which put it into the operator's instructions. **If you have new shells or domes, find the code on the device yourself before you start, because nobody else can.**

One honest note about the software. Phonak Target is [intended for hearing care professionals](https://www.phonak.com/content/dam/celum/phonak/master-assets/en/documents/resources/phonak-target/target-12-0/PH_UserGuide_Target-12.0_92x125_EN.pdf), and I am not going to cover where I got my copy. What I will say is that the version matters: Target 10.1.2 refused to talk to my aids because their firmware was newer than the software, and Target 12.0.1 worked. In my experience, you can update Target to its latest version at any time from inside the app, and I recommend always staying on the latest version. Phonak's [Infinio Ultra product information](https://www.phonak.com/content/dam/celum/phonak/master-assets/en/documents/hearing-instruments/infinio/audeo-i/PH_ProductInformation_Audeo-I_Ultra_210x280_EN_027-0712-02.pdf) lists Target 11.1 or higher for my model, and the security notice in Phonak's [Target 12.0 user guide](https://www.phonak.com/content/dam/celum/phonak/master-assets/en/documents/resources/phonak-target/target-12-0/PH_UserGuide_Target-12.0_92x125_EN.pdf) says to make sure the installed Target version is up to date. Target also has a firmware update tool under Trial & tools, described in Phonak's [Target 11 step-by-step guide](https://www.phonak.com/content/dam/celum/phonak/master-assets/en/documents/resources/phonak-target/target-11/ph-desktop-fitting-guide-target-11.0-step-by-step-210x297-029-1387-33-en-gb.pdf), and my understanding is that keeping Target current is what lets that tool offer the newest firmware available for your aids.

<p align="center"><img src="assets/02-hearing-aids-closeup.jpg" width="480" alt="Close-up of two Phonak Audéo Sphere receiver-in-canal hearing aids with glossy black custom shells lying on a dark gray laptop, with the black Noahlink Wireless 2 programming dongle behind them, its status lights glowing green."></p>

*Figure 2. The hearing aids and the programming interface. These are my two Audéo Sphere hearing aids with the new custom shells I had made right before this project, sitting on the Windows laptop next to the Noahlink Wireless 2, the Bluetooth dongle that lets Target talk to them.*

The two computers were linked through Claude's Remote Control feature, the same link the Claude mobile app uses, so the Mac session could be followed and steered from the Windows side. Then I ran a second, separate Claude session directly on the Windows laptop, because the Mac session cannot click inside a program on another computer. You do not need a second computer, and [doing it with one computer](#doing-it-with-one-computer) explains why I used two anyway and how to manage with one. That second session wrote its own PowerShell scripts to read Target's screens: the accessibility tree for every label, checkbox and slider, and Target's graph controls, which expose every curve as data points. capture.ps1 and walk.ps1 are even visible in my setup photo. I explain exactly how that worked further down, in [how the AI actually did it](#how-the-ai-actually-did-it).

## Part two: The method

This part explains how two Claude sessions split the work, and how every answer was checked before I trusted it. Nothing in my hearing aids changes here, because the audiogram, the research and the audit all came first.

### Putting Claude in the supervisor's chair

The most important decision in this whole project was splitting the work into two roles, with the supervisor in charge. The supervisor, on my Mac, played the part an audiologist normally plays. It was the session I actually talked to: I told it what I heard in my own words, and it turned that into carefully planned changes, computed from the raw exported data and written into an instruction file for each programming session. Before a plan ever reached the operator, the supervisor had a separate critic attack it, and after the operator finished, it checked every result against the data before it planned anything new. It researched, audited and decided, but it never touched Target.

The operator, on my Windows laptop, was the only session that made programming changes. It followed the supervisor's instruction file exactly, asked me before every change, logged every step with its before and after values, and exported a capture package at the end: screenshots with text dumps, curve data, and Phonak's own fitting reports, all zipped up. It did not plan or improvise, and when the screen did not match the file, it stopped and told me. I carried each zip back to the Mac, so the supervisor always had the final word on whether a session had done what it was supposed to. Figure 1, near the top of this post, shows how the pieces fit together.

The instruction files grew into something like a flight checklist. Each one opened with numbered hard rules, and from session two on they included these:

- Never edit the original client record, which stayed as an untouched restore point.
- Ask me before every change and every save.
- Never raise maximum output.
- Leave specific recalculation boxes unticked.
- Use single arrow steps, and read every value back from the grid.
- Use real mouse clicks instead of automation clicks.
- Stop the moment the screen does not match what the file expects.

Every gain change had to keep the gain for soft speech at least 3 dB below the measured feedback threshold in every program, and by session three that check covered both ears at every point Target draws from 125 Hz to 8 kHz. Those same files capped each session at about four listening comparisons, because a lot of testing had honestly gotten into my head by the end of the first session.

<p align="center"><img src="assets/22-verification-loop.jpg" width="720" alt="Diagram of the seven-step loop: 1, instruction file; 2, a critic reviews the plan; 3, the operator runs it in Target; 4, the session log and capture package; 5, a verifier recomputes every number; 6, a second verifier challenges the first; and 7, new hard rules go into the next instruction file, looping back to step 1."></p>

*Figure 3. The verification loop from session two on. Every session went through the same cycle, from the instruction file through the operator's changes to two independent verifiers, and whatever went wrong became a new hard rule in the next instruction file. By the end, the instruction files had grown from 6 hard rules to 12.*

The supervisor did not work alone either. For every serious question it launched a workflow of parallel agents, and in most of those workflows each working agent was followed by an adversarial verifier whose only job was to prove it wrong. Across seven workflows that came to 52 agents, about 10.6 million tokens, 3,059 tool calls, and a little over four hours of wall-clock time, which added up to about ten hours of agent time because so many agents ran in parallel. **The supervisor's rule was to recompute every number from the raw files rather than trust an agent's summary.**

### Verifying the audiogram first

My situation was different from a fitting done from scratch. My hearing aids had already been programmed by my audiologist, and a year of real use told me what worked and what did not, so the goal was to fine-tune a good foundation. That made the first job a validation layer: before touching anything, check everything the existing fitting was built on, starting with the audiogram. It was also a way to confirm that my audiologist had done a good job, and she did a great one.

The paper chart was the only record of my hearing we had, so reading it was not enough. I wanted the AI to truly understand the measurements: what every symbol means, how sure we can be of each one, and how the numbers line up with what I actually live with every day. **The goal was to turn one sheet of paper into the best possible annotated measurement, because there was nothing else to reference.**

#### A quick detour: finding the file

This part showed off what Claude Code can do on a real computer. I could not remember where my audiogram was saved, so I asked Claude to find it. It searched my Mac by file name, by Spotlight content, and by the hidden text layer of every PDF in my Downloads, Desktop and Documents folders. Nothing matched, and it correctly worked out that the file had to be a scanned image with no text inside, so it had an on-device text recognition pass ready to go by the time I found the scan myself: a photo of the paper chart from 2022.

<p align="center"><img src="assets/03-audiogram-scan.jpg" width="480" alt="A scanned paper audiogram form. The graph shows left ear X symbols between about 40 and 65 dB and right ear triangles between about 80 and 105 dB, with bone conduction and no-response symbols, next to tympanometry, speech test and comment sections. The letterhead, barcode, document ID, print stamp and tester signature are blurred."></p>

*Figure 4. The original 2022 audiogram. This is the paper hearing test everything started from, a scanned photo of the chart from my audiologist's office. I blurred the letterhead, the barcode and its ID number, and the tester's signature.*

#### Reading the chart

Before any AI read a single symbol, Claude prepared the image. It found the printed gridlines by taking the median brightness of every pixel row and column inside the graph, which ignores handwriting, then cut enlarged crops of every section and laid a calibrated grid over the chart. The paper was slightly warped, so the overlay was treated as approximate and every symbol was judged against the printed lines next to it.

<p align="center"><img src="assets/04-gridline-overlay.jpg" width="720" alt="The graph region of the audiogram enlarged three times, with blue vertical lines at each test frequency from 125 to 8000 Hz and red and orange horizontal lines every 5 dB from minus 10 to 110 dB HL, laid over the hand-drawn symbols."></p>

*Figure 5. Calibrated gridlines over the audiogram. Claude found every printed gridline in the scan and laid this grid over the chart, blue for each frequency and red for every 5 dB step, so each hand-drawn symbol could be read against an exact position instead of eyeballed.*

Then three graph readers transcribed every symbol blind, each from a different view of the image: one with the overlay, one with the raw chart counting gridlines itself, and one with only high-zoom tiles. Two more readers transcribed the rest of the form. Two reconcilers, one for the graph and one for the form, compared everything and re-measured the image wherever readings differed, with one rule I love: do not majority vote, the image is the authority. The readers matched exactly on 28 of 34 plotted points, and all 34 were within 5 dB of each other.

<p align="center"><img src="assets/06-reader-agreement.jpg" width="720" alt="Two panels. A: all 34 plotted points by series and frequency, 28 identical in all three readings and 6 that differ by 5 dB, all in the right air row at 250, 500, 1000, 1500, 2000 and 3000 Hz. B: the right ear masked air values, where reader 2 read every disputed triangle exactly 5 dB worse than readers 1 and 3."></p>

*Figure 6. Agreement between the three blind readers. Three AI readers transcribed all 34 points on my audiogram without seeing each other's work, and 28 matched exactly. All six disagreements were right-ear triangles, where one reader used the center of each triangle and the other two used the tip, which put them exactly 5 dB apart.*

<p align="center"><img src="assets/05-scan-vs-digitized.jpg" width="720" alt="Side-by-side comparison of the scanned audiogram graph and a digitized version on a log frequency axis, with the left ear as blue X symbols and the right ear as red triangles."></p>

*Figure 7. The paper audiogram and its digitized version. The left side is the scan, and the right side is the same audiogram rebuilt from the verified numbers, with my left ear in blue and my right ear in red. Every point is now an exact value that can be typed into Target.*

All six disagreements were right-ear triangles, and they came down to one question: does the tip or the center of a hand-drawn triangle mark the threshold? The reconciler measured both against the local gridlines and chose the tip, because the tips landed almost exactly on 5 dB steps. Then came the twist. When we finally read the audiogram stored inside my hearing aids, every right-ear value was exactly 5 dB worse than the tip reading, which matched the center reading at six of the seven frequencies. My aids were programmed from the center reading, which is a perfectly fair way to read a hand-drawn triangle, and the verification had flagged that exact question before we ever saw the stored numbers.

<p align="center"><img src="assets/14-target-stored-audiogram.jpg" width="720" alt="Phonak Target's Client audiogram screen with two graphs labeled Headphones. The right ear, in red circles, runs from 85 dB at 250 Hz down to 110 dB at 4 kHz. The left ear, in blue X symbols, runs from 40 dB at 250 Hz to 65 dB around 1.5 and 3 kHz and back up to 40 dB at 8 kHz. Between them are AC, BC and UCL buttons and display options."></p>

*Figure 8. The audiogram stored in the hearing aids. This is the audiogram Target read out of my aids, the one my existing fitting was built on. Every right-ear value is exactly 5 dB worse than our tip reading, which matches reading the triangles by their center at six of the seven frequencies, the exact question the verification had flagged.*

Next, one agent wrote a full expert interpretation of my audiogram, and a second agent played a skeptical senior audiologist reviewing it before it reached the patient. The skeptic made 19 corrections and flagged 4 things the first pass left out, including an arithmetic slip, a speech-test conclusion the data could not support, and an overclaim about masking. That was the moment I understood the value of the setup. **The first draft was good, and it still needed nineteen corrections.**

<p align="center"><img src="assets/13-supervisor-window-closeup.jpg" width="480" alt="Close-up photo of the Claude window on the MacBook, straightened from an angle, showing &quot;Created audiogram-handoff.md&quot; and a summary of the handoff file: entry tables for each ear in Target's frequency order, right-ear alternative values for the triangle tip versus center question, handling for no-response points, and a note that the audiogram is about four years old."></p>

*Figure 9. The supervisor session handing off the audiogram. This is the Mac session writing the file the operator used to enter my audiogram into Target. Even at this step, it flagged the one real uncertainty, whether to use the tip or the center of each triangle, before anyone typed a number.*

### Rounds of critique

Research came next, with the same pattern. Three researchers covered the hearing aid, the Target software, and fitting science, and each was followed by a fact checker that reopened every source. Out of 142 claims, 123 were confirmed, 11 were corrected, 7 stayed unverified, and 1 was refuted. Three findings mattered most:

- Only the [Ultra Power receiver](https://www.phonak.com/en-us/hearing-devices/hearing-aids/audeo-sphere/for-professionals) with a custom shell can cover my right ear at all, and it sits right at its limit at 4 kHz.
- Target adds gain if you enter bone conduction values, so we left them out.
- If you never choose an earphone type, Target silently uses a default, as one of the corrections showed.

Then the operator session captured my entire existing fitting before anything changed: 137 screens, Phonak's full 45-page report, and about 158,000 curve points read straight out of Target's graphs. The supervisor audited it with four domain auditors covering the prescription and acoustics, gain and output, features and programs, and device options and usage logs. Each auditor had its own adversarial verifier, and a completeness critic looked for conflicts between them. A separate deep dive tackled my own complaints: streaming crispness, the whistling right ear, a right ear that felt weaker by evening, and the sharp left "s". Across the audit and that deep dive, the verifiers checked 109 findings, confirmed 51, changed 56, rejected 2, and added 42 that the first pass had missed.

The biggest discovery was simple once the data showed it. My right ear was sitting 11 to 20 dB under its prescription between 1 and 3 kHz, not because anyone chose that, but because the old right shell leaked and whistled before the aid could deliver more. At 1 kHz the soft-speech gain was only 1.8 dB away from the measured feedback limit. That leak was also why a hand or a pillow made it whistle. The audit also found that [frequency lowering](https://www.phonak.com/content/dam/celum/phonak/master-assets/en/documents/evidence/hearing-aids/insight-sound-recover2-season1-2016-210x297-v2.00-028-1512-02-gb.pdf) was set from my better ear and did almost nothing for my right one, and it kept my Bluetooth phone setting on Fixed on purpose, because that is what fixed Microsoft Teams on my Mac.

## Part three: The sessions

This part walks through every session in order, what changed in my ears, and the audits that checked each one. As a reminder, the supervisor is the Claude session on my Mac that I talk to, which plans every change and checks it, and the operator is the Claude session on my Windows laptop, the only one that makes changes in Target. It ends with how my own plain descriptions turned into precise changes.

### Two days at a glance

Here is the whole fitting in order, before the details.

- **Day one, afternoon.** I found and verified my audiogram, researched the aids and the software, and read my fitting into a restore point and a working copy, without saving anything to the aids.
- **Late afternoon into evening.** The operator captured every screen and curve, and the supervisor ran the audit and the deep dive on my complaints.
- **Evening.** Session one entered the new right shell code I read off the shell, reran the feedback test and made a few small comfort fixes, and I saved it to the aids.
- **Late evening.** Session two lifted my right ear and adjusted streaming, and I saved that too.
- **Overnight.** Fourteen agents checked session two and planned session three while I slept, without touching the aids.
- **Day two, morning.** Session three trimmed my right ear slightly and lifted my left, and every change stayed unsaved until it was verified.
- **Late morning.** The operator redesigned Comfort in noise, and then everything from session three was saved in one go.
- **After the save.** A final audit recomputed everything from the raw data.

If you try this, have the supervisor keep a timeline like this one from the files, not from memory, because it is the fastest way to see what was saved and when.

### Session one: A better seal changed everything

I had new custom shells made for both ears right before this started, but Target still held the old right shell's acoustic code and a feedback test measured with the old shells. So the first session made no gain changes by hand. I read the new code off my right shell, 431965 instead of the old 432597, and gave it to the supervisor, which wrote it into the instruction file. The operator entered exactly that code, read it back from the screen, and re-ran the feedback test.

<p align="center"><img src="assets/15-acoustic-parameters.jpg" width="720" alt="Phonak Target's Instruments, Acoustic parameters screen for two Audéo I90-Sphere hearing aids: the right aid with an Ultra Power (UP) receiver, acoustic code 431965, earpiece cShell, vent according to acoustic code and wire length 2UP R; the left aid with a Medium (M) receiver, acoustic code 366939, cShell and wire length 2M L, each next to a receiver fitting range chart."></p>

*Figure 10. Acoustic parameters for both hearing aids. This is where Target stores the receiver and earpiece for each aid. I read the six-digit code off my new right shell, 431965, and the operator entered it in session one, which told Target the new shell seals better, and every gain change afterward was built on that.*

The left test failed four times, and the reason made sense afterward: my left aid has a much weaker receiver, so its test tone drowns in background noise. It passed as soon as I put in a fresh wax guard and moved to a quiet room. Once the new shell was measured, Target raised my right soft-speech gain by up to 4.4 dB on its own, and I accepted that.

<p align="center"><img src="assets/16-left-feedback-test-failed.jpg" width="720" alt="A Phonak Target dialog for the left ear's Feedback and real ear test with an orange banner reading &quot;Real ear measurement failed&quot; and a list of potential causes: environmental noise is too loud, selected acoustic coupling does not match actual acoustic coupling, and blocked vent or microphone."></p>

*Figure 11. A failed left-ear feedback test. This is the message Target showed each of the four times my left-ear test failed. My left aid has a much weaker receiver, so background noise drowned out its test tone until I put in a fresh wax guard and moved to a quiet room.*

<p align="center"><img src="assets/07-target-feedback-before-after.jpg" width="720" alt="Four Phonak Target measured feedback threshold graphs, right ear on the left and left ear on the right, old shell on top and new shell below. With the new shell, the right ear's purple feedback line sits well above the red gain curves between 500 Hz and 2 kHz, where it was close to them before."></p>

*Figure 12. Measured feedback thresholds with the old and new shells. The purple line is how much gain each ear can take before it whistles, and the red and blue curves are the gain it actually gets. With the new right shell measured, the purple line rose 7 to 12 dB between 500 Hz and 2 kHz, which gave my right ear room for more gain before I changed a single setting.*

That session also taught the operator its first hard lessons. Automation clicks sometimes changed what a checkbox looked like without changing the actual setting, so real mouse clicks became a rule. Turning off frequency lowering in one program silently turned it off in six, because Target shares that switch across a whole group. When I listened afterward, my left ear sounded less muffled, and in my words at the time, it sounded really good.

<p align="center"><img src="assets/18-soundrecover2-group-toggle.jpg" width="720" alt="Two Phonak Target program lists side by side. Before: every program shows an SR badge for SoundRecover2, with Music selected. After SoundRecover2 was unticked in Music and then in Media music + mic: the SR badges are gone from Calm situation, Speech in noise, Spheric speech in loud noise, Speech in car, Comfort in noise and Music, and from Media speech + mic and Media music + mic, each group outlined in amber."></p>

*Figure 13. SoundRecover2 switching off across a program group. The SR badge marks every program with SoundRecover2, Phonak's frequency lowering, turned on. Turning it off in Music also turned it off in all six automatic programs outlined on the right, and turning it off in Media music + mic did the same to both streaming programs. The operator caught it and turned it back on, and a report afterward showed zero differences.*

### Session two: Spending the headroom

With the new seal, the supervisor planned a 5 dB lift for my right ear between 860 Hz and 2 kHz across every program, with smaller lifts on either side, which is about a third of the gap to the prescription. Before the change, the operator tested a trick for selecting only certain cells in Target's grid: clicking a frequency header in the grid's "All" row selects that column's gain rows without touching the maximum output row. The operator then applied the lift in single steps, and Target's own smoothing supplied the smaller lifts on either side by itself. Every program was checked afterward against its own feedback line, and the tightest one still had 3.55 dB of room. For streaming, frequency lowering was turned off in the two Media streaming programs only, and the right side of streamed audio got a small extra lift, applied blind because I could not stream while Target was connected. The result on my right ear was exactly what I hoped for: speech was clearer, not just louder, and loud sounds were fine.

<p align="center"><img src="assets/08-right-ear-progress.jpg" width="720" alt="Bar chart of right ear soft-speech gain minus target in the Calm situation program at 1, 1.5 and 2 kHz: original fitting minus 16.6, minus 19.0 and minus 20.3 dB; after session 1 minus 12.2, minus 16.7 and minus 18.6 dB; after session 2 minus 7.2, minus 11.7 and minus 13.5 dB, with a side panel of the feedback margin at 1 kHz: 1.8, 9.4 and 4.4 dB against a 3 dB minimum."></p>

*Figure 14. Right-ear soft-speech gain against target, by session. Panel A shows how far my right ear's gain for soft speech sat below its prescription from 1 to 2 kHz, where zero is right on target, and each session brought it closer. Panel B shows the room left before whistling at 1 kHz: the new shell raised it from 1.8 to 9.4 dB, and session two spent some of that while staying above the 3 dB minimum.*

### The overnight audit

I went to bed and gave the supervisor permission to keep working. It ran 14 agents overnight across five verified streams: an independent check of session two, the math for a future right-ear step, my left ear, streaming fidelity, and the [myPhonak app](https://www.phonak.com/en-us/hearing-devices/apps/myphonak). Then it drafted a session three plan, ran a critic against it, and revised it. I woke up to a morning report written for a non-audiologist.

The overnight run caught two real problems. First, a tip from session two, turning up the Middle slider in the myPhonak app, turned out to be risky: a Phonak trainer has described that slider as covering roughly 500 Hz to 2.5 kHz in 3 dB steps on older Phonak models, right over my tightest feedback spots, and if that holds for my aids, one step could have left only about 1.2 to 1.3 dB of room. Second, the future right-ear step written into the session two file would have dropped below the 3 dB rule once Target's automatic smoothing of neighboring channels was modeled, so it was replaced with a smaller one. **Both mistakes were confident, reasonable, and wrong, and both were caught because the overnight run recomputed everything from the raw data and had a second agent check every result.**

### Session three: The phenomenal part

By morning my right ear felt like a little too much on loud sounds, with a buzz I described as almost like internal feedback. So session three trimmed it slightly: loud sounds came down about 2 dB between 860 Hz and 2 kHz, soft sounds came down a little near 1 kHz where the feedback margin was tightest, and a small trim went in around 4 kHz because we never pinned down whether the buzz was low or high. In Calm, the tightest spot on my right ear, at 955 Hz, went from 4.30 to 5.68 dB of room before feedback. With my left aid muted, my verdict was "sounding good," and right-ear speech stayed as clear as before.

<p align="center"><img src="assets/10-target-grid.jpg" width="720" alt="Phonak Target fine tuning screen for the Calm situation program, with right ear gain curves in red, left ear curves in blue, and the 20-channel gain and maximum output grids below."></p>

*Figure 15. Target's 20-channel gain and output grid. This is the screen where the actual changes happen. Each number in the grid is the gain in dB for one frequency band at one input level, soft, average or loud, and every change in this project was one arrow step in these cells, read back afterward.*

#### Body for my left ear

The left ear got the change I will remember. My left ear sounded thin and a bit sharp, so the supervisor planned a small lift for medium and loud sounds between 520 Hz and 1 kHz in my everyday Calm situation program, two single steps that raised the actual curves by about 1 dB for medium sounds and up to about 1.7 dB for loud ones. The moment the operator applied it, the left ear sounded phenomenal. It added body and warmth, and my left ear no longer sounded thin or sharp to me, so the separate "s" trim we had planned was skipped. Earlier in the session we had trimmed the left "s" slightly in the two Media streaming programs only, based on how streaming sounded to me at home.

<p align="center"><img src="assets/19-left-richness-before-after.jpg" width="480" alt="Two crops of Phonak Target's left-ear 20-channel grid for the Calm situation program, before and after. An amber box marks the 520, 690, 860 and 1k columns of the G80 and G65 rows: before, G80 reads 11, 14, 17, 21 and G65 reads 18, 22, 25, 28; after, G80 reads 13, 16, 19, 22 and G65 reads 19, 23, 26, 29. The G50 cell at 690 Hz moved from 29 to 30."></p>

*Figure 16. The left-ear low-mid lift, cell by cell. These are my left ear's grid values in Calm situation before and after session three. The outlined cells went up one or two steps for loud (G80) and average (G65) sounds from 520 Hz to 1 kHz, which raised the real curves about 1 to 1.5 dB and gave my left ear the body and warmth it was missing.*

After the final check, I asked for the same left lift in two more programs, Speech in car and Comfort in noise. The operator explained the trade-off first: more low-mid gain in a noise program also makes the background noise fuller. I said "yes, do both," and my quick listens were "ok" and "k." The lift there is about 0.9 to 1.8 dB for loud sounds and 0.6 to 1.1 dB for average sounds between 500 Hz and 1 kHz, soft sounds moved at most 0.3 dB, and there is at least 13 dB of feedback room in that range. In Comfort in noise, the redesign later in the morning brought the whole program up close to Calm anyway, so there the lift no longer stands on its own. The final audit checked that extension too, and I give its verdict in [saved, then audited again](#saved-then-audited-again).

#### Checked before the save

One more lesson came out of this session. Single arrow steps in Target were often smaller than 1 dB in this session, so the operator read the grid after every press and added a step where a cell fell short, and the curves still showed some changes landing smaller than the grid suggested. When the operator first asked about saving, I told it to keep everything connected and unsaved until the supervisor had checked the data, so at that point nothing was saved. That independent verification recomputed every curve and confirmed the morning's changes were safe and logical to save: every program kept at least 3 dB of feedback room, and every change on the right ear was a decrease. The save came at the end of the session, after the Comfort in noise redesign, and I explain exactly how it was approved and checked in [saved, then audited again](#saved-then-audited-again).

### Fixing Comfort in noise

I have always felt that the Comfort in noise program kind of mutes everything, not just the background. It is one of the [automatic programs](https://www.phonak.com/content/dam/phonak/en/evidence-library/white-paper/technical-paper/PH_Insight_AutoSenseOS7.0_210x297_EN_029-1459-02_V1.00.pdf) my aids switch to on their own, based on what their microphones hear. The data agreed with my ears. Compared with Calm, it gave soft sounds about 4 to 6 dB less gain in both ears through most of the speech range, from 500 Hz to 4 kHz, and it ran stronger noise reduction on top of that. Because it shares Calm's measured feedback threshold exactly, Calm's margins showed how far it could safely come up, and the plan was to bring it to about 1 dB below Calm with slightly lighter noise reduction. The redesign had one firm rule: no grid cell could end above Calm, so my right ear would not get more in this program than it already got in Calm, my everyday program.

#### What changed

The redesign happened the same day, at the end of session three. The operator stepped the program up one press at a time and read the grid after every press. Soft sounds went from about 4 to 6 dB below Calm to at most about 3 dB below it. Average and loud sounds now match Calm within about 1 dB, except on my left side below about 400 Hz, where they are up to about 2 dB less. No grid value in either ear ended above Calm, the curves never rose more than 0.5 dB above it, and the program's maximum output did not change. Its noise reduction, which Phonak calls NoiseBlock, went from Moderate 12 to Moderate 10, still a little stronger than Calm's Weak 8.

That did make my right ear louder in this one program, in the same session as the morning's trim. What kept it in bounds is that every grid value stays at or below Calm, which already includes that trim. One thing neither the plan nor its verifier saw coming was that in Target, stepping soft and average gain up also pulled loud-sound gain up, by 1 to 2 steps in 17 of the 20 channels on my right side. So in Comfort in noise, only about half of the morning's loud-sound trim remains, and in noisy places I am listening for loud sounds on my right that feel like too much. Below 500 Hz, loud sounds on my right in this program are now up to about 1.9 dB above where session two left them. If loud sounds on my right do feel like too much there, the fix is a decrease: my right ear's loud-sound row in this program goes back to where it was before the redesign.

It still keeps plenty of room from whistling. The smallest feedback margin in Comfort in noise is now 6.98 dB on my right side, at 4 kHz, and 6.74 dB on my left, at 4,387 Hz. Just before the rebuild it was 10.25 and 9.13 dB, and after session two it was 8.27 and 9.13 dB, so the redesign spent some of that room, but it stayed far from the 3 dB rule.

<p align="center"><img src="assets/09-comfort-vs-calm.jpg" width="720" alt="Two line charts, right ear and left ear, of gain for soft speech from 125 Hz to 8 kHz, with the Comfort in noise curve running about 4 to 6 dB below the Calm situation curve through the speech range, both under a dashed measured feedback threshold."></p>

*Figure 17. Comfort in noise versus Calm situation, before the fix. The dark lines are my everyday Calm situation program and the light lines are Comfort in noise, both showing gain for soft speech. Comfort in noise gave soft sounds about 5 dB less through most of the speech range, which is exactly why it felt like everything went quiet.*

#### How it sounded

For the listening check, the sound came from the computer's speakers, not my phone, because a phone can start a Bluetooth stream, and my aids had already switched themselves to a streaming program once that session. Looped noise and a synthetic voice played while the aids ran Calm, and then the redesigned Comfort in noise, with the same sound both times. I did not even notice when they switched, because, in my words at the time, it "just sounds that good." That check was done while the noise reduction was still at 12. The change to 10 came right afterward, as planned, and I have not listened to it on its own yet, so my first real test of it will be in the noisy places I actually go.

### Saved, then audited again

Session three, including the Comfort in noise rebuild, is saved to both of my hearing aids. The morning changes had been checked independently before the save, and the rebuild was checked afterward, in a final audit of what Target read back from the aids.

I want to be exact about how that save was approved. Before the rebuild, I told the operator there was no point saving in between and to "just ... do everything that needs to be done." The operator took that as approval to save once at the end, and it did not ask the plan's separate final question, "Save these changes to both hearing aids?" The audit flagged it, and the lesson is simple: ask the exact save question anyway.

Then the save was checked against the data, not just the log. After the save, Target reconnected without asking which settings to use, which it asks when the aids and the computer differ. All 12 programs it read back matched what had been set at every curve point, with zero difference, and every 20-channel grid matched cell for cell. Two confirmations are still missing: a charger cycle, which shows that the aids start up from their stored memory with the saved settings, and a device report exported after the save.

The final audit then recomputed everything from the raw data after the save. Before its grid reader was trusted, it had to reproduce 880 known grid values from earlier tables, and it did, with zero mismatches. A second, independent pass with new code then confirmed every conclusion and corrected a few numbers, which is exactly the job a second pass is for.

Every program, in both ears, still has at least 3 dB of room before feedback at every native curve point from 125 Hz to 8 kHz. The tightest spot anywhere, and in everyday use, is still my left ear in Calm, at 4.21 dB near 2.2 kHz, and my right ear in Calm has 5.68 dB near 955 Hz. The smallest right-ear margin is in RogerDirect, at 4.26 dB, a program I do not use, because no Roger receiver is installed.

A stricter measure also counts an unlabeled curve in Target's data, which the operator identified in Calm as soft-speech gain without the Speech Enhancer. What that curve means outside Calm is still unconfirmed, so I treat it only as a stricter check. On that measure the lowest values are 3.27 dB in RogerDirect on the right, 4.02 dB in Media music on the right, 4.21 dB in Calm on the left and 4.62 dB in Comfort in noise on the right, and all of them still pass. That 4.62 dB sits at 4 kHz and is new since the redesign, so a high whistle in noisy places is one more thing I listen for.

<p align="center"><img src="assets/20-margins-all-programs.jpg" width="720" alt="Horizontal bar chart of the smallest feedback margin in dB after the morning changes of session 3, for 12 programs, right and left ear: Calm situation 5.68 and 4.21; Speech in noise 6.78 and 7.44; Spheric speech in loud noise 6.78 and 7.44; Speech in car 8.91 and 7.45; Comfort in noise 10.25 and 9.13; Music 8.38 and 6.77; Media speech + mic 7.81 and 7.79; Media music + mic 5.39 and 6.18; PartnerMic + mic 14.02 and 8.96; Phone call + mic 7.27 and 8.96; RogerDirect + mic 4.26 and 7.42; Spheric manual 6.78 and 7.44. A dashed amber line marks the 3 dB rule, and every bar is to its right."></p>

*Figure 18. Smallest feedback margin in every program. Each bar is the smallest room between soft-speech gain and whistling anywhere from 125 Hz to 8 kHz, after the morning changes of session three and before the Comfort in noise rebuild. Every program in both ears stays to the right of the dashed 3 dB line, and the tightest are my left ear in Calm at 4.21 dB and my right ear in RogerDirect at 4.26 dB.*

The locked settings held too. No maximum output value changed in session three, my right maximum output has never been raised by hand, and the only increases since the original fitting are still the shifts of at most 1 dB that Target made on its own in session one. My Bluetooth phone bandwidth is still on Fixed in the last device report, the streaming programs' microphone settings are unchanged, and the restore point was never edited: the session three logs never open it, and the one time I opened it, in session one, to hear the original fitting, it was closed without saving.

The final audit also tried to overturn my left lift in Speech in car and Comfort in noise, and could not, so it stays, with one thing to watch. The change is small, about a quarter of the median change listeners could notice in one study of single-octave gain changes, it is far from any feedback limit, and I asked for it knowing the trade-off. I still heard the same lift clearly in Calm, so I do not assume it is inaudible. Speech in car also uses the same microphone mode and the same light noise reduction as Calm, so there is no directional microphone for the lift to work against. What I am watching is whether background noise, or my own voice, starts to sound boomy, fuller or more tiring in the car and in noisy places. If it does, undoing it in Speech in car takes just two single down steps.

### Plain words in, precise fixes out

I never had to know the name of a setting to get help. I described what I heard, when it happened, and where I was, in the same words I would use with a friend. The AI's job was to turn those words into something a fitting can act on: a range of frequencies, a feature, or a physical cause like a loose shell or a clogged wax guard. Then it had to check the data before it touched anything. **Being able to describe a struggle in normal human words, and have it land on a precise fix inside the machine, was one of the most important parts of this whole project.**

#### The sound of my own skin

My favorite example started right after the first save, on the evening of session one. I said I was hearing a lot of high-frequency sounds when I should not, that the "s" sound was worse, and that I could hear little high-pitched bits of sound when I rubbed my skin. The way I describe it now is even simpler: when I rub my skin on my neck, the high-pitched sound hurts my ears. Target has no setting called neck.

So the first move was not a change at all. The AI first checked whether the fitting itself had gained any high-frequency output, using Phonak's own 2cc numerical reports to compare my original fitting with the one we had just saved, in all 12 programs. From 2.5 to 6.7 kHz, neither gain nor maximum output had risen more than 1 dB in either ear, and the only changes of any size were lower down, in my right ear. So the new sharpness did not come from a high-frequency increase in the fitting.

Then we used the levers that fit. At my request, soft noise reduction in my everyday Calm program went from Off to Weak. For loud high pitches, the part that truly hurt that night, my left ear's maximum output came down 4 to 5 dB from 2 kHz up, in every program. It sounded the same, because everyday sounds do not reach that ceiling, but it still guards the loudest peaks. Target's automatic fix for a bright, shrill sound went in and came back out twice, and in the end I left it out, because to me it did not sound crispy.

None of it changed the high pitches I kept noticing that night, and I ended the session thinking a lot of testing had gotten into my head. The overnight audit, which ran after session two that same night, called it a textbook case of restored high pitches: a fresh wax guard and a better-sealing new left shell had most likely brought back sound that a partly blocked guard had been dulling, which also fit the earlier muffled sound, and my brain needed time to adjust. It also split my complaint in two: skin rubbing is a quick burst of sound right next to the microphone, the "s" is speech, and each calls for a different tool. In session three my left ear stopped sounding thin or sharp in Calm, and not because we cut the highs there: we gave it more body underneath them. The skin rubbing never came up again in the sessions, and a stronger SoundRelax setting, the Phonak feature that softens short, sudden sounds, is the untested next step if it does.

That was not a one-off. Many changes in this project started as a sentence like that, and here are the best examples, in my exact words.

<details>
<summary>Show all 9 examples</summary>

- **"the right ear, I think, could totally use a little bit more help."**
  - What it meant: My right ear sat 11 to 20 dB under its prescription at 1 to 3 kHz, held there by the old shell's feedback limit.
  - What we did: Measured the new shell first, then a 5 dB lift from 860 Hz to 2 kHz in every program.
  - How it turned out: Speech sounded "clearer," and "loud is fine."
- **"It would give feedback when something was near the hearing aid, such as a hand on the outside."**
  - What it meant: Sound leaking around the old right shell, with soft speech only 1.8 dB from whistling at 1 kHz.
  - What we did: I read the new shell's acoustic code off the shell, the operator entered it, and we reran the feedback test in a quiet room.
  - How it turned out: 7 to 12 dB more room from 500 Hz to 2 kHz, and no whistling I noticed in the session.
- **"I swear in the mornings I can hear more out of the right ear but then throughout the day that goes away."**
  - What it meant: Testable causes: a shell working loose, wax, or a switch to noisier programs with 4 to 6 dB less right gain.
  - What we did: No gain change. A home check instead: reseat, new wax guard, quiet room, restart, and an audiologist if it continues.
  - How it turned out: No fading since the new shell.
- **"almost like the wax trap needed to be changed or something."**
  - What it meant: Target still held feedback data from my old left shell, and physical causes such as a blocked wax guard were just as likely.
  - What we did: Fresh wax guard, quiet room, and a new left feedback test, which passed after four noisy failures.
  - How it turned out: "less muffled. It sounds really good."
- **"it likes to sometimes weaken the audio channels for streaming because it turns on the microphone in the hearing aid."**
  - What it meant: When an app opens a Bluetooth microphone, the iPhone swaps stereo media audio for a mono call link.
  - What we did: Nothing in Target can stop it. Pause the stream before dictating, or try setting the iPhone to use its own microphone.
  - How it turned out: Explained, with no fitting change needed.
- **"So I wanted to see how we can fine-tune this to make things nice and crispy."**
  - What it meant: iPhone audio plays through the two Media programs, not Music, and on my right side they sat 13 to 20 dB under target at 1 to 3 kHz, with extra bass.
  - What we did: Frequency lowering off in both Media programs, plus a small right lift from 1 to 2 kHz.
  - How it turned out: Good overall, with a wish for better balance.
- **"a little bit too much overall buzz from the increased volume."**
  - What it meant: Too much gain for loud sounds from 860 Hz to 2 kHz, and maybe near-feedback at my two tightest right spots, 955 Hz and 4 kHz.
  - What we did: Decreases only: loud sounds down about 2 dB from 860 Hz to 2 kHz and a small trim around 4 kHz, keeping the soft and medium gain from 1.2 to 2 kHz where the clarity lived.
  - How it turned out: "sounding good," and the tightest right margin in Calm rose from 4.30 to 5.68 dB.
- **"I feel like sounds might not be balanced all the way in how they should yet."**
  - What it meant: Too vague to act on, so it asked me to choose from four readings, and I picked my left ear sounding too thin and sharp.
  - What we did: Two single steps on medium and loud sounds from 520 Hz to 1 kHz in my left ear, in Calm and then two more programs.
  - How it turned out: "The left ear sounds phenomenal."
- **"it seems to kind of mute everything."**
  - What it meant: Comfort in noise gave soft sounds about 4 to 6 dB less than Calm, with stronger noise reduction, even when speech was present but not detected.
  - What we did: A checked redesign brought its soft sounds to within about 3 dB of Calm, kept every grid value at or below Calm's, and eased its noise reduction from 12 to 10.
  - How it turned out: I did not notice the switch: "it just sounds that good." Saved, with home listening still to do.

</details>

If you try this, the most useful thing you can give the AI is a good description, and it needs no jargon at all. Say when and where it happens, which ear, and whether it is soft sounds, loud sounds, or both. Say whether it is your own voice, other people's voices, streaming, or everyday noise, and describe it in your own words: buzzy, tinny, muffled, sharp, or whistling. Then say what you are comparing it to, such as yesterday, the other ear, or before the last change. And when your words could mean two things, let it ask: one of my best answers in this project was a single multiple-choice pick.

## Part four: Under the hood

This part explains exactly how the AI read and drove the software, how every file was exported, and which checks stayed mine. The operator is the session on my Windows laptop, the only one that worked inside Target, and the supervisor is the session on my Mac that I talked to, which planned and checked everything from the exported files. If you only want the method, skip to Part five.

### How the AI actually did it

This is the part I most wanted to get exactly right. Neither Claude session had any special access to Phonak Target. There was no plugin, no hidden interface, and no Phonak integration.

The short version has four parts:

- The operator read Target through the same accessibility layer a screen reader uses, and read every curve as exact numbers.
- It changed settings only with real mouse clicks and drags, one step at a time, and checked every result in the grid and in the curve data.
- The supervisor never saw Target, only the exported files, and did its own math on them.
- The results that mattered, from either side, went to another agent whose job was to prove them wrong.

One more honest detail, about approvals. Both of my sessions ran in the desktop app's bypass permissions mode, which you can see at the bottom of each Claude window in my photos. That mode lets a session run commands without stopping to ask, so the approvals that mattered happened in the chat: every instruction file made the operator ask me before every change and every save. If you are new to this, I would start in a [permission mode](https://code.claude.com/docs/en/permission-modes) that asks before it runs commands, and I would insist on it when both sessions share one computer.

#### The operator's eyes

Windows has an accessibility layer called [UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-uiautomationoverview), which exists so screen readers can describe every button, checkbox and slider to people who cannot see them. The operator wrote a script, capture.ps1, that walked that tree inside Target's window and wrote every element to a text file, one line each: its type, its name, its value or state, and its position on the screen. A checkbox arrived as a line like CheckBox | Client view | toggle=Off, and a slider or progress bar arrived with its exact value. The first version missed dropdown values, so the operator fixed its own script until the earpiece, the receivers and the wire length came through as text.

A second script, walk.ps1, came right after the operator said it would redo every screen in order, and the finished package holds a screenshot of Target next to a text dump for each of the 137 screens. Neither script was saved into my project files, so I can show what they produced but not their exact code. Early screenshots caught the Claude window covering part of Target, so it switched to capturing Target's own window directly, whatever sat on top of it, and redid every screen.

<p align="center"><img src="assets/12-operator-window-closeup.jpg" width="480" alt="Close-up photo of the Claude desktop window on the Lenovo laptop, titled &quot;Windows-Mac remote connection&quot; and marked working, listing steps such as &quot;Created capture.ps1, ran a command&quot;, &quot;The text dump works well, and Target even exposes its graphs as data points&quot;, &quot;Ran a command, read 06_Client_Audiogram.png&quot;, and &quot;Created walk.ps1, ran 2 commands&quot;, with the model shown as Opus 5.5."></p>

*Figure 19. The operator session writing its own tools. This is the Windows session building capture.ps1, a script that dumps every screen of Target as text. Along the way it noticed that Target exposes its graphs as data points, and then it built walk.ps1 to step through every screen in order.*

Then came the discovery that made the whole project possible. Target's graphs are custom controls, and their accessibility value is not a picture: it is a block of XML called GraphControl that holds every point of every curve. Each curve carries a caption, such as Gain (50 dB speech), Target gain, Measured feedback threshold, or Gain limit, followed by pairs of frequency and decibel values. Target draws each curve at 91 points between 125 Hz and 8 kHz, the first large graph is the right ear, and the second is the left. A small Python reader turned those dumps into tables, so no curve in this project was ever read off an image. The feedback safety rule was checked with arithmetic on exact data points, not by squinting at two lines on a graph.

<p align="center"><img src="assets/17-what-the-operator-reads.jpg" width="720" alt="Two panels of real capture text. Panel A, from the session 1 Apply changes dialog, lists lines such as &quot;CheckBox | Reset fine tuning (e.g. Gain & MPO) | toggle=Off&quot; and &quot;CheckBox | Reset program options | toggle=Off&quot;, both highlighted. Panel B, from the session 3 Calm situation curves, shows the right ear's Gain (50 dB speech) point at 955 Hz as 59.139 dB and the Measured feedback threshold at 955 Hz as 64.816 dB, with the line 64.82 minus 59.14 = 5.68 dB of margin at 955 Hz."></p>

*Figure 20. What the operator reads instead of pixels. These are excerpts from two real capture files. The first shows every checkbox arriving as a line of text the operator could verify, and the second shows two curve points at 955 Hz, where subtracting the gain from the feedback threshold gives 5.68 dB of room, so the safety rule was checked with arithmetic instead of by eye.*

There was one blind spot. The 20-channel gain and output grids, the numbers I actually change, are drawn by Target as pixels, and their values do not appear in the accessibility tree at all. Text recognition on them was unreliable, so during the sessions every grid value was read visually from enlarged screenshots, and every change was cross-checked against the curve data and against the diff of Phonak's own report. The session three instruction file warned that any secondhand grid value could be off by 1 dB from a reading error, which is exactly why the curves, not the grids, were the source of truth for safety.

#### The operator's hands

In session one the operator tried to toggle a checkbox through UI Automation, and Target showed the box as changed while the real setting stayed the same. From then on, every click and every drag was real mouse input. The logs do not record which Windows mechanism produced those clicks, only that they were real ones. To select cells, it clicked a frequency header in the grid's "All" row, which selects that column's gain rows without the maximum output row, and it found that a real drag across several headers selects a range while Ctrl plus a click does not. By session three, it took a screenshot before every arrow press and checked exactly which cells were highlighted, and after every press it read the values back from the grid and checked that the other ear had not moved. When a step moved a cell less than expected, it pressed again and read again, so targets were reached by reading, not by counting clicks.

Some of the problems were wonderfully physical. The Claude window stayed on top of Target's right side, which is exactly where the left-ear grid lives, so the operator slid Target partly off the left edge of the screen before every left-ear drag. Then it asked Windows which window sat under the cells it was about to touch, using a system call named [WindowFromPoint](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-windowfrompoint), and only dragged once the answer was Target. It took a Target snapshot before any change, used undo one step at a time, and stopped to tell me the moment anything on screen did not match the instruction file. It even read Target's own internal log, which showed that my left ear's feedback measurement had physically finished even though Target's evaluation of it had failed.

#### How the operator learned Target

Neither session knew anything about Target beyond what anyone can read online, so the operator learned the program the way a careful new employee would: from the manual first, and then from the real thing. The supervisor's researchers read Phonak's own manuals, the Target 12 user guide and the step-by-step fitting guides, and pulled out how Target is supposed to behave. The operator then walked every screen of the real program and saved each one as a screenshot and a text dump, 137 screens in all, which became its map of where every control actually lives.

The manual and the real program did not always agree, and when they did not, the real screen won. One idea from the research, a separate manual program just for streaming, turned out not to exist on my aids: the operator's capture of that screen showed that media streaming could only switch on automatically. From then on, every instruction file spelled out exact paths through the real menus, such as Fitting, then Advanced L/R coupling, then Calm situation, then Program options, so the operator never had to guess where anything was.

The operator's knowledge also kept growing. Whenever something surprised it, the surprise was written down and turned into a rule for the next session, so the same mistake could not happen twice:

- An automation click changed how a checkbox looked but not the actual setting, so every click and drag became a real mouse click.
- Clicking a row in the ALL PROGRAMS view selected the whole row, and one maximum output step went in, so the operator started taking a screenshot of the highlighted cells before every press.
- Saving to the database and then closing the session produced "There is already the task type 'Saving' reserved" and "Phonak Target is in an unstable state," so the rule became to check the database, restart Target, and prefer saving to the aids.
- When I asked to hear my original fitting, Target connected with "Use fitting from hearing aid," so the comparison quietly played the working copy against itself, and the fix was to choose "Use fitting from session" and confirm it with a grid value.
- A stray click while moving the window landed Target on the Instruments screen and cleared the undo history, so the operator stays on the fine tuning screen and takes a snapshot before any change.
- The Claude window covered the left-ear grid, so the operator moves Target before every left-ear selection.

That loop is why the instruction files grew from 6 hard rules to 12. **Learn from the manual, trust the real screen over the manual, and write every surprise into the next session's rules.**

#### The supervisor's math

The supervisor worked only from files. For the audiogram, a Python script converted the scan to grayscale, took the median brightness of every pixel row and column inside the graph, and marked a gridline wherever a row or column was clearly darker than its neighbors. For the fitting, it parsed the curve dumps with its own code, and the session verifiers wrote their own parsers instead of reusing the author's scripts, then confirmed the ear order from a known value before trusting anything. The margin itself was simple subtraction: the measured feedback threshold minus the soft-speech gain, at every one of Target's native points, in every program, for both ears.

That precision mattered. Session two's check sampled standard frequencies, and the overnight recompute found that the true tightest point sat between them, at 955 Hz, slightly tighter than the log had reported. So from session three on, the margin code had to pass a self-test before it was trusted: run on the session two data, it had to print exactly 4.30 dB for the right ear at 955 Hz and 4.21 dB for the left ear at 2,194 Hz. For planning, the supervisor also fitted a model of how Target smooths a change into neighboring channels, with a more pessimistic version on top, and that model is what caught the unsafe right-ear step overnight.

#### Agents that try to break each other

The supervisor ran its agents as workflows, which start many agents side by side and chain a checker behind each one. Every agent answered in the same fixed format, so an audit finding always came back with what was observed, the assessment, the recommendation, the expected effect, the risks and checks, a confidence, and a priority. Every verifier answered each finding with a verdict of confirmed, modified or rejected, a reason, and a corrected version when one was needed. None of them could touch Target. A worker could be confident, but it was never the last word.

### How everything was exported

Exporting was the backbone of the whole method. The supervisor on my Mac never saw Target, so everything it knew about my fitting came from these files, and every number it planned or checked was computed from them. The exports also gave me an exact record of what my hearing aids held before and after every change, which is what made each change provable and reversible.

Before anything changed, I needed a restore point I could trust. In Target, "Use fitting from hearing aid" reads the fitting out of the aids without writing anything back, so my fitting was read from the aids into a client record and saved to Target's database only. That original record was never edited again. Then the aids were read a second time into a separate working copy, and the two were proven identical by generating Phonak's binaural numerical report for both and comparing them line by line: 279 of 279 lines matched. The raw saved sessions differed in 264 of 28,350 bytes, which is expected, because those bytes hold session identifiers, timestamps, and about 25 extra minutes of usage logging on the aids.

The first export captured my whole fitting from that original record, before the working copy existed, and the operator put a file named CONTEXT_READ_FIRST.md at the top of it, addressed to the AI that would analyze it. Inside were 137 screenshots, each with its text dump, plus all 137 dumps merged into one searchable file. Phonak's own reports were saved as PDF and as text: the 45-page complete report and the 9-page binaural numerical report. The curve data went into CSV files: one with every point of every curve on every screen, 158,205 points in all, and per-program summaries of gain for soft, average and loud speech, the prescription targets, the measured feedback threshold, and the gain limit. After the save, the operator also copied Target's client database, a small SQLite file, along with the saved sessions inside it, which are in a Phonak binary format that only Target can read or restore. All together it came to 294 files, about 70 MB, zipped down to about 40 MB.

<p align="center"><img src="assets/21-capture-package-tree.jpg" width="720" alt="Folder tree of the first fitting export: CONTEXT_READ_FIRST.md, README.txt, ALL_SCREENS_TEXT.txt with 17,746 lines, a screens folder with 137 screenshots and 137 text dumps, a data folder with graph_curves_all_screens.csv holding 158,205 points and three other files, a reports folder with Phonak's 45-page and 9-page reports, a database folder with a copy of Target's client database, and a working copy verification folder. A second panel lists the later session packages: session 1 with 302 files, session 2 with 60 and session 3 with 129, each with a session log, screens, data and reports."></p>

*Figure 21. Contents of one capture package. Panel A is the first export, which captured my whole fitting before anything changed: every screen as a screenshot and as text, every curve as data, Phonak's reports, and a copy of Target's database. After every session, the operator sent back a smaller package with the same layout, and I carried each one to the Mac to be checked.*

One line in that README saved us from a classic mistake. Phonak's reports give values in 2cc coupler units, measured in a standard test cavity, while the curve CSVs are insertion gain, the extra gain at the eardrum compared with an open ear, and mixing the two gives wrong answers. Every package labeled its units, and every package with raw curve dumps said which graph was which ear.

Each session after that sent back a package with the same shape: the session log, before and after screenshots, curve data, and Phonak's numerical report. Session one also saved a report after each change group and a diff of its final report against the original, session two diffed its report against session one's, and the supervisor's verifier diffed session three's. From session two on, each package also carried a copy of the exact instruction file it followed.

Session one's package held 302 files, including a partial re-capture I stopped because it was taking too long; session two's held 60; and session three's held 96 and carried NOT_SAVED in its name, because nothing from that session had been saved to the aids yet. The operator zipped each one on the laptop, and each zip traveled through my Google Drive to the Mac's Downloads folder. Before relying on the session three zip, the supervisor's verifier confirmed that all 96 files in it matched the unpacked copy on the Mac byte for byte. After the final save, session three sent one more package of 129 files, and it matched its unpacked copy on the Mac byte for byte too.

The report diff was the quiet hero of the whole export. In session one, after every change group, the operator generated a fresh numerical report, saved it as text, and compared it with the last one, which showed exactly which settings moved, including side effects nobody asked for. That is how the fix for the frequency lowering surprise in session one was proven complete, with zero differences against the report from before it.

### Every check I did by hand

The AI could read, compute and click, but it could not hear, and it could not see my hardware. Those parts were mine. Here is every check I did myself, in order, taken from the session logs.

<details>
<summary>Show all 21 checks</summary>

- Found the scan of my audiogram myself when the file search came up empty.
- Answered the setup questions: which audiogram was in Target, which receivers I wear, what I wanted, and that there would be no real-ear measurement.
- Told the supervisor what had changed physically: both shells were new, the right one whistled less, and the left one sounded slightly quieter and muffled.
- Locked my preferences, including the Bluetooth phone setting on Fixed because it fixed Microsoft Teams on my Mac.
- Read the acoustic codes printed on my new shells and gave them to the supervisor, before the operator changed the right one in Target.
- Confirmed the feedback test setup: aids worn that day, fresh wax guards, shells pushed fully in, and sitting still.
- Inspected both aids when the left test kept failing, put in a fresh wax guard, and moved to a quiet room.
- Approved the gain changes Target made on its own after the new feedback test.
- Listened after session one: left less muffled, right louder in the way it should be, and no whistling that I noticed.
- Ran the before and after comparisons myself: Target's automatic fix for a bright sound three times, frequency lowering off and on, the left feedback canceler slider from lowest to highest, and two Speech Enhancer levels.
- Put the aids through a charger cycle after the session one save and confirmed they sounded the same.
- Stopped a long re-capture at the end of session one, because it was taking too long.
- Started session two by reporting no right-ear fading since the new shell, and rated my left "s" 6 out of 10, "in a good way."
- Tested my right ear alone with the left aid muted, using claps, dishes, a door and loud TV: loud was fine, and speech was clearer.
- Gave a next-morning report: the right ear a little too loud with a buzz but clearer, the left thin and a bit sharp, and streaming good overall.
- Put fresh wax guards in both aids before session three, and picked, from four readings the AI offered, what "not balanced" meant to me: my left ear sounding thin and sharp.
- Listened to the session three right trim with the left aid muted, then to the left lift, and then to the lift in Speech in car and Comfort in noise.
- Said yes to the left lift in Speech in car and Comfort in noise only after the operator explained that it would also make background noise fuller.
- Listened to Calm and then to the redesigned Comfort in noise with the same speech and noise playing from the computer's speakers, and could not tell I had switched.
- Approved every change in chat, held back the session three save until its verification came back, and then told the operator to do everything that needed to be done, which it took as my go-ahead for the final save.
- Moved every capture zip from the laptop to the Mac.

</details>

There are also two checks I skipped and should not have. I never rated the "s" on my left side again after the lift that made it sound phenomenal, and I never told the operator whether the buzz in my right ear was a low hum or a high whine, so the plan had to trim for both. **The AI can only be as careful as the answers I give it.**

## Part five: Do it yourself

This part covers the limits I would not cross, how to go back, how to do it with one computer, and the whole method step by step, with every prompt in the order you use it. If you skipped ahead, the supervisor is the Claude session you talk to, which plans and checks every change, and the operator is the only session that makes changes in the fitting software.

### What I would not let it do

I want to be honest about what this is and what it is not. I am not an audiologist, and nothing here is medical advice. These are my own prescription hearing aids, Phonak intends Target for hearing care professionals, and I did this knowing that responsibility sits with me. My audiogram is from 2022, and my hearing has been consistent since, but if yours is old, I recommend getting a new one professionally recorded before you try anything like this.

So the rules were strict:

- Nobody raised maximum output by hand. The only increases were shifts of at most 1 dB, mostly at 850 Hz and 1.5 kHz, that Target made on its own when the new right shell was entered.
- The original fitting stayed untouched as a restore point.
- Every change kept a measured safety margin from feedback, in every program, checked against the exported curve data.
- Every change went in one small step at a time and was checked before the next.
- Nothing was saved without my go-ahead, and the one save that followed a general go-ahead instead of a direct answer is spelled out in [saved, then audited again](#saved-then-audited-again).

If you have hearing loss and are tempted to try something like this, please start with your audiologist, because the most important part of this project was never the software. It was the checking.

#### How to go back

A restore point only helps if you know how to use it, so here is the ladder I planned, from smallest to largest:

- **Undo.** Inside a session, Target's undo arrows step back one change at a time, although Target cleared that history in my session three when the operator left the Fitting screen by accident.
- **An earlier saved session.** After a save, an earlier saved session of the working copy can be opened, connected and saved to the aids again.
- **The restore point.** If everything goes wrong, the original fitting still sits in the restore point, exactly as it was read from my aids.

I never needed more than undo and putting a value back by hand, so I have not tested the last two myself. I would climb them the way I did everything else: with the operator reading me every screen, and nothing saved without my clear yes.

### Doing it with one computer

You do not have to use two computers. I used two for convenience: the operator could take over the laptop's screen inside Target while I gave the supervisor my feedback between rounds of testing, so nobody waited on the screen and I never had to interrupt a session in progress. **Technically you can do all of this on one computer, but the second one was a huge time saver.** It was also a quiet safety feature: the supervisor could not click inside Target even by accident, because Target was not on its machine. Most people will have one computer, so here is what I would do, although I have not tested either layout myself.

<p align="center"><img src="assets/23-one-computer-setup.jpg" width="720" alt="Diagram of two one-computer layouts. A: one Windows PC with a supervisor session and an operator session that share a folder, connected over USB to a Noahlink Wireless 2 and over Bluetooth to the hearing aids. B: a Mac running the supervisor, with the operator in a Windows virtual machine, the same shared folder, and the same Noahlink and hearing aids."></p>

*Figure 22. Two one-computer layouts. Layout A puts both sessions on one Windows PC, and layout B runs the supervisor on a Mac with the operator inside a Windows virtual machine, and both share one folder instead of passing zips. I have not tested either one, and because HIMSA says Noahlink Wireless does not support ARM, layout B is a long shot on an Apple silicon Mac.*

My first choice would be one x64 Windows laptop or desktop with an Intel or AMD processor, running two separate Claude desktop sessions named Supervisor and Operator. It uses exactly the same pieces I used, just on one screen. Phonak's [Target 12 user guide](https://www.phonak.com/content/dam/celum/phonak/master-assets/en/documents/resources/phonak-target/target-12-0/PH_UserGuide_Target-12.0_92x125_EN.pdf) lists what that computer needs, including Windows 10 or 11 on a 64-bit system and an Intel Core processor or better, and the Noahlink driver is normally installed along with the fitting software. Replace the zips with one shared project folder and a fixed layout: a read-only restore point folder, a supervisor folder, a folder that only ever holds finished instruction files, a folder per session for the operator's exports, and a folder for your own notes. Have the operator write a small READY.txt file last, listing every exported file with a SHA-256 hash, and have the supervisor refuse to start until that file exists and every hash matches. That keeps the one thing a zip really gave me: a finished, frozen bundle that nobody edits afterward.

The hard part on one computer is discipline, because both sessions can reach the same screen. Write the supervisor's rules into its [project instructions](https://code.claude.com/docs/en/memory): never open, click, or script the fitting software, never use Claude's computer use feature, which lets a session see and click the screen, and hand off only through files. Keep the supervisor in a [permission mode](https://code.claude.com/docs/en/permission-modes) that asks before running commands, so any attempt to touch the fitting software shows up as a prompt you can deny. Run the parallel agents only inside the supervisor, and do not turn the operator into a subagent, because its whole job is a live conversation with you where every change waits for your yes. I would also keep two sessions rather than one, because if one session writes the plan and then runs it, nobody independent checks the plan against the screen.

Mind the windows, too: on my laptop a single Claude window already covered the part of Target where my left-ear grid lives, and two Claude windows on one screen make that worse. A second monitor helps, and otherwise I would keep both Claude windows on one side and Target on the other. I would also pause heavy supervisor workflows while the operator is connected to the aids, because a stalled laptop in the middle of a save is the failure you least want, although that is caution, not something I measured.

A Mac on its own is harder. On Apple silicon Macs, Windows runs as an ARM version inside a virtual machine, and [HIMSA's Noahlink Wireless FAQ](https://www.himsa.com/wp-content/uploads/2022/09/Noahlink_Wireless_FAQ_EN_2022.pdf) states that Noahlink Wireless is not supported on PCs with an ARM processor. HIMSA's knowledge base [says the same](https://www.himsa.com/support/noah-4-knowledge-base/preparing/arm-based-windows-not-supported-for-noahlink-wireless-or-noah/) about ARM-based Windows, including laptops with Snapdragon processors.

I found forum reports of people giving up on that route and of connections that worked only some of the time, and I found no report of Target 12 with a Noahlink Wireless 2 and Infinio aids working reliably in a virtual machine on Apple silicon. On an Intel Mac, Boot Camp gives you real x64 Windows, which in principle is the same as a Windows PC, but I found no specific report of this setup working there either, so treat it as unproven. If you already have a Mac and can borrow any x64 Windows laptop, my own layout still works: the supervisor on the Mac, the operator and Target on the laptop. **A used Windows laptop is a safer purchase than a workaround driver on the machine that programs your hearing.**

### Step by step

Everything so far has been the story of what I did. This section turns it into a method you can follow, in the order I would do it again. It assumes you have read [what I would not let it do](#what-i-would-not-let-it-do) and picked a setup, with two computers like mine or one computer as described above. As before, the supervisor is the session you talk to, which plans and checks, and the operator is the only session that makes changes in Target. Each step says what you do, what the AI does, and what you check yourself, followed by the prompts for that step in the order you use them. Work straight down the page: every prompt says when to use it and what you get back, and the next thing to do is always directly below it. None of the prompts has blanks to fill in, because each one tells the AI to find what it needs or to ask you.

**Supervisor prompt:** Walk me through the method, one checked step at a time.
Use it if you want the AI to guide you through the steps below and keep track of where you are.

```text
You are the SUPERVISOR. Be my checklist coach for reprogramming my own hearing aids with you as the supervisor and a separate operator session. Take the steps below one at a time. For each step, tell me what I do, what you do, what the operator does if anything, and what I must check with my own eyes and ears. Do not move on until I confirm the checks are done, and keep a running checklist in PROGRESS.md in the project folder.

1. Set my limits, and get a new audiogram first if mine is old.
2. Set up Claude Code and the supervisor and operator sessions.
3. Check the hardware and the software version.
4. Gather the facts: my complaints, my audiogram, and my patient context, including the acoustic codes I read off my shells.
5. Verify the audiogram with blind readers, then interpret it and attack the interpretation.
6. Research with a fact check on every claim.
7. Have the operator learn the software, make a restore point, and export everything.
8. Audit the fitting.
9. Write the instruction file, then have a critic attack it.
10. Run a first session for new earpiece facts and a feedback test only, with no gain changes by hand.
11. Run a tuning session from the reviewed instruction file.
12. Save only on a clear yes, read the fitting back, do a charger cycle, and know how to go back.
13. Verify the session against the data.
14. Live with it for one to two weeks, then take the next small step.

If I try to skip a step, tell me what could go wrong and ask me to confirm. If anything I describe sounds like a medical problem, stop and tell me to contact my audiologist or doctor. You are not my audiologist, and none of this is medical advice.
```

**What happens:** The supervisor keeps PROGRESS.md and walks you through each step.

#### Step 1: Set your limits

- **You:** If your audiogram is old, get a new one professionally recorded first, and write down your limits before you start: never raise maximum output, keep an untouched restore point, save nothing without your explicit yes, and keep a small listening budget per session.
- **The AI:** Nothing yet, although it can list which parts of your plan still need a clinician, such as masking, a dead-region test, or real-ear measurement.
- **Check:** Your aids are working and comfortable today, and you know how to reach your clinic. Sudden hearing changes, pain, dizziness, new tinnitus or drainage mean a doctor visit, not a fitting session.

**Prompt for both sessions:** Paste these limits at the top of every session.
Paste it first, at the very top of every session, in both the supervisor and the operator.

```text
Read these limits before anything else, repeat them back to me in your own words, and follow them for this whole session. If any request, including one from me, would break them, stop and say so.

1. Roles. The supervisor plans, checks and talks me through everything, and never touches the fitting software. The operator is the only session that changes settings, and only from a reviewed instruction file.
2. Restore point first. The original fitting is saved as its own client before anything changes, and it is never opened for editing. All work happens in a separate working copy.
3. Ask me before every change and every save. Save to the hearing aids only on a clear yes to the save question. On anything less, save to the database only.
4. Never raise maximum output, in either ear, in any program.
5. Keep soft-speech gain at least 3 dB below the measured feedback threshold at every point, in every program, for both ears, checked with code on exported data.
6. One small change group per save, then at least one week of normal wear before the next increase.
7. Settings I have asked to keep are locked. Read them from PATIENT_CONTEXT.md once it exists, and ask me if you are not sure.
8. Verify every number against the exported data, not against a log, a summary or your memory.
9. Stop the moment the screen does not match what you expect, and tell me.
10. Send me to my audiologist or doctor, not to a setting, for a sudden hearing change, pain, dizziness, fullness, new ringing, or anything that needs a real-ear measurement or a new hearing test.
11. If the software offers a firmware update, do not accept it in this session. A firmware update cannot be rolled back.
```

**What happens:** The session repeats your limits back in its own words and follows them from then on.

#### Step 2: Set up Claude Code and the two sessions

- **You:** Open a Supervisor session and an Operator session, on two computers, or on one computer with the shared folders below.
- **The AI:** The supervisor writes its own rules file and a short project README from your notes.
- **Check:** Ask each session what its role is and what it may not do, and read the answer. Neither session may write into the restore point.

**Prompt for any session:** Start a careful first session in Claude Code.
Use it once, in your very first Claude Code session, right after the limits.

```text
This is my first project with Claude Code. I will use it to understand my own hearing aid fitting and, later, to adjust it carefully with two sessions: a supervisor I talk to, which plans and checks every change, and an operator, which is the only session that ever touches the fitting software. Before we do any real work, set up the ground rules.

1. In plain words, tell me what you can do on this computer (read and write files, run commands and scripts, look at images, search the web, start helper agents) and what you cannot do (hear anything, see my hardware, or click inside a program on another computer).
2. Create a folder named Hearing Aid Project in my Documents folder, with a short README.md that holds the limits I just pasted and describes the two roles. Read that README at the start of every session.
3. Before you run any command, tell me in one sentence what it does. Ask me before any command that installs software, changes a setting, or deletes, moves or overwrites a file.
4. Keep everything on this computer. Do not upload my audiogram, my fitting files or my notes anywhere, and do not paste them into a web search.
5. When you are not sure, say so, and mark anything you could not confirm as UNVERIFIED instead of guessing.

When the README is written, show it to me and wait. Do not start on the hearing aids until I say so.
```

**You get:** A project folder with a README of your limits and the two roles, which 