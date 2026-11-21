<h1 align="center">Roboglot</h1>

<p align="center"><strong>Talk to your robots. Let them talk to each other.</strong><br>
<sub>Roboglot is the communication layer between people and robots, and between robots themselves. Say what you want in your own words, from a terminal, a page or Claude, and an LLM flies the robot. Robots that have never met check each other's passports, then divide the work. It began as the brain daemon the Microduck was missing. Ten robots today, one of them driven on real hardware and the other nine so far only on a mock, and one of them a duck you can print and build yourself. More are described from their makers' figures and not driven at all.</sub></p>

<p align="center">Register each robot once, by name. Then state a goal from a terminal, the page or a chat with Claude, to one robot or to a team of them, and the same contract decides which of each robot's skills its LLM may use, how many steps it gets, and when it has to ask you first.</p>

<p align="center">
  <a href="https://github.com/rokbenko/quackd/actions/workflows/ci.yml"><img src="https://github.com/rokbenko/quackd/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://pypi.org/project/roboglot/"><img src="https://img.shields.io/pypi/v/roboglot?color=f5c518&label=PyPI&cacheSeconds=3600" alt="PyPI"></a>
  <a href="https://pypi.org/project/roboglot/"><img src="https://img.shields.io/badge/python-3.11%2B-3776AB?logo=python&logoColor=white" alt="Python 3.11+"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-blue" alt="Apache 2.0"></a>
  <a href="docs/guides/mcp.md"><img src="https://img.shields.io/badge/MCP-ready-8A2BE2" alt="MCP ready"></a>
  <a href="docs/adapters/status.md"><img src="https://img.shields.io/badge/robots-10%20adapters%2C%201%20on%20hardware%2C%2012%20described-f5c518" alt="robots: 10 adapters, 1 on hardware, 12 described"></a>
</p>

<details>
<summary>Hey, my name is Rok and this is why I built Roboglot 👋</summary>

> I see Roboglot as a ChatGPT like moment for robotics. Let me explain what I mean.
>
> LLMs existed long before ChatGPT. What ChatGPT actually did was take LLMs and hand them to ordinary people in a chat interface everyone already knew, like Facebook Messenger or Instagram. That was the real unlock.
>
> Right now, in 2026, most people still think robots belong in science fiction movies or in a lab at Tesla. That is not true anymore. There are already open source robots you can build yourself for under $1000. And they actually work. They can go to your fridge, open it, grab a can of Coke, close the fridge and bring it to you.
>
> The problem is they have a huge limitation. You can teach them dozens of moves, like "get a coke". But the robot itself is still dumb. It knows the moves, it just cannot connect them on its own. For robots to become truly useful, they need to become AI first and agentic. You give them a goal and they figure out the steps themselves.
>
> To get there, robots need a brain. And here is the catch. Today's robots simply do not have enough hardware on board to think, reason and plan. Their skull is too small for the brain this kind of intelligence needs. So the brain has to live outside the robot, in the cloud or on your own computer, where it can grow as big as you need. The robot itself stays small and light while all the heavy thinking happens somewhere else. That is what Roboglot started as. A brain for one robot.
>
> But here is what I think comes next. In the future everyone will have a team of robots. At home, in the office, wherever. And they will not all be the same robot. Different types, different capabilities, even different companies. The first challenge is having all of them in ONE place to command. That is what Roboglot is now. You connect every robot you own to one CLI, and you command all of them from there, with an LLM as the brain of each one.
>
> But even when you have them all in one place, that is still not enough. What you ask for will be complex, and robots will probably be very specialized. One can walk, one can grab, one can carry. For a bunch of different robots to be useful with as little of your involvement as possible, they need to start working together towards the goals you give them. Which means they need to communicate between each other. So that is the other half of Roboglot. You give the team a goal, each robot's brain reads what the others can do, and they divide the work between themselves.
>
> Imagine telling your robots "I want to eat and drink something". The one with wheels goes to the fridge, checks what is inside and tells the others what it found. The one with arms grabs a plate and some cutlery. One of them brings it all to you and asks what you would like, you choose, and they go back for the food and wish you a good meal. Sounds like science fiction, right? We are closer than you think!
>
> That is basically what ChatGPT did for LLMs. It took something powerful and put it in one place everyone could reach. And that is why I see Roboglot as a ChatGPT like moment for robotics.
>
> — Rok Benko, September 2026

</details>

<p align="center">
  <img src="https://raw.githubusercontent.com/rokbenko/quackd/main/docs/assets/lerobot.gif" alt="A phone recording of a real SO-101 robot arm. It opens on a laptop screen with the Roboglot command being typed into a terminal, watches the run scroll past, then pans to the bench, where the arm starts folded, raises its shoulder and elbow into an extended pose, rolls its wrist back and forth four times as a wave, returns to centre and stops. A webcam on a stand watches it from table height across a calibration mat." width="640">
  <br>
  <sub><strong>A real arm, a real LLM, one sentence.</strong> An SO-101 follower arm on 2026-09-15, piloted by OpenAI's <code>gpt-6-astra</code> through <code>roboglot run --goal "Wave to the camera with an extended arm"</code>. The LLM was handed the arm's five verbs and its datasheet and chose one call at a time: raise the shoulder and elbow, roll the wrist four times, return, stop. Nobody wrote a wave. The whole run at ten times speed, filmed on a phone: it opens on the command going into a terminal, watches the run scroll, then pans to the bench, and the wave itself is the part where the wrist rocks. What the LLM was told, all ten of its calls and what went wrong are in <a href="#what-happened-in-that-run">What happened in that run</a>, and how every recording here was made is in <a href="docs/assets/README.md">docs/assets</a>.</sub>
</p>

**Roboglot** is the communication layer between people and the robots they own, and between those robots. Each one joins through an adapter that declares, as a manifest, what the body is and what it can do, and you register it once by name with how to reach it. Give a robot a goal like *"find the ball and kick it"* and an LLM picks one skill at a time from the list that manifest declares, Roboglot runs it, looks at the camera, and asks again until the job is done or clearly impossible. Give the same goal to a team and every robot in it gets an LLM of its own, and they divide the work by telling each other what they are going to do. A goal can arrive from a chat, a command line or a `.glot` task file, and whichever way it comes, Roboglot enforces a contract the pilot LLM cannot talk its way out of: which skills are allowed, how many steps, when a human must say yes, when to abort. Claude, OpenAI, Gemini, Grok, Mistral, DeepSeek, Cohere, Qwen, Kimi, GLM and Meta work over their APIs, and so do the LLMs OpenRouter routes to, behind one key of its own. Open source LLMs work on your own machine through Ollama, vLLM, llama.cpp or LM Studio, with no key. An LLM is the pilot on every run but a scripted one. `--decision-llm` optionally puts something in front of it that is **not** a pilot LLM and cannot be used as one: a decision LLM generates no text at all, it scores a fixed set of options against a state and returns which one with a probability for each, so it answers the turns that are a choice among calls the robot already has and can no more write a joint angle than a thermometer can. TypeSafe's Jev was the first of them and is hosted, OpenAI's Decisions API is the other hosted one, and the rest Roboglot names are open servers you run yourself or a checkpoint loaded into this process, each with a page of its own. Off unless you name one, and `--decision-mode shadow` records what one would have chosen without letting it change a thing ([docs/guides/decision-llms/README.md](docs/guides/decision-llms/README.md)). On the SO-101 arm a learned policy from Hugging Face's Hub, NVIDIA's GR00T and Physical Intelligence's pi0 among them, can drive the arm for one short segment at a time, and [Which models work](#which-models-work) lists every one of all three kinds and how to name each one.

The first robot is the [Microduck](https://pollen-robotics.com/microduck/) from Pollen Robotics: a 25 cm, 800 g biped with fifteen small servos, a camera in its head, a depth sensor, a speaker and an onboard computer, open source and about $399, which already knows how to walk, turn, kick, scoop something off the floor, look around and quack at 50 Hz on its own hardware. It is the robot Roboglot started on, independently and unofficially. Nine more bodies follow it through adapters that declare what each can do: an [Open Duck Mini v2](https://github.com/apirrone/Open_Duck_Mini) you can print and build yourself, an SO-101 class arm through LeRobot, any wheeled base over rosbridge, an XLeRobot dual-arm cart, an AlohaMini with two arms on a lift, a ToddlerBot humanoid, a [Huebot](https://ce-net.com/huebot), a 25 cm biped with behaviour code of its own, whose maker is writing a shim for it that is to answer the Microduck's calls the same way, [MOSS](https://github.com/metrox-eth/moss), a small tracked rover that picks up litter, reached through its own cockpit and a bridge Roboglot ships for it, and an industrial arm on ROS 2 (a Universal Robots UR5e, a KUKA LBR iisy, a KUKA LBR iiwa or a Yaskawa MotoMini) through its ROS 2 driver and rosbridge, which only rehearses so far: its real backend is refused until somebody names a date for a first run on one.

**One of the ten bodies runs on real hardware, and the recording above is it.** On 2026-09-15 an SO-101 follower arm ran Roboglot over `lerobot:real` through twelve `--goal` runs in one afternoon, piloted by OpenAI's `gpt-6-astra` from a Windows laptop with a USB webcam: it waved with its wrist, reached out with its shoulder and elbow, opened and closed its gripper, and once mimed a duck quacking with it. The GIF is the last of the twelve, and [What happened in that run](#what-happened-in-that-run) reads its transcript call by call. The honest half is there too. The arm fell at the end of every one of those runs, because LeRobot drops torque when it disconnects, which is what [the rest pose](#your-robots-by-name) was written afterwards to stop, and the camera framed the gripper and cropped the raised arm, so the LLM checked its own waves against joint readings rather than against the picture. On 2026-09-23 the same arm ran again, registered as `arm-01` with a rest pose, through 26 runs on Roboglot 0.12.0, and 23 of them came from ten task files written for that afternoon, which now sit among the 246 in [docs/examples/lerobot/](docs/examples/lerobot/README.md). Its rest pose could not reach a fold that lay past the travel its calibration recorded, 19 of the 26 runs never moved the arm at a pilot's request, and what Roboglot changed in answer has not run on an arm yet. The other nine bodies have not met hardware. Their real backends speak names read from upstream source at a pinned commit and have only ever talked to fakes, and for the Open Duck Mini and the ToddlerBot those fakes are the daemons Roboglot itself ships for the robot, exercised over loopback, so there only the body is untested. MOSS's bridge is Roboglot's own too, exercised the same way beside a fake of MOSS's cockpit. The industrial arm's fakes are written from reading each driver's source, and its real backend refuses to start until somebody names a date for a first run on an arm. No team has yet crossed from one machine to a second. Goals like *"find my keys"*, handed to a team that sorts out who does what, are where this is going, not what it does yet. The honest label for today is *LLM driven, goal directed control of one real arm and nine mocked bodies, alone or in teams*, and [Which robots work](#which-robots-work) says exactly how far each one has got.

**No robot yet? You can still try it, on a mock.** Every adapter has a `mock` backend, an in-memory test double that stands in for its robot: it takes every intent, answers with a state from a script and, for a body with a camera, draws frames of its own. A run on a mock shows the contract, the gates and the command line working, and it shows nothing about how a robot behaves, because nothing a mock reports was measured on one. [No robot yet? Try it in 60 seconds](#no-robot-yet-try-it-in-60-seconds) has a command that runs on one, and what it printed.

<br>

## Table of Contents

- [Quickstart: a LeRobot SO-101 arm](#quickstart-a-lerobot-so-101-arm)
  * [From the terminal](#from-the-terminal)
  * [From Claude, over MCP](#from-claude-over-mcp)
  * [What happened in that run](#what-happened-in-that-run)
- [No robot yet? Try it in 60 seconds](#no-robot-yet-try-it-in-60-seconds)
- [Why?](#why)
- [How it works (the simple version)](#how-it-works-the-simple-version)
- [Example](#example)
- [Status](#status)
- [Which robots work](#which-robots-work)
- [Which models work](#which-models-work)
  * [Pilot LLMs](#pilot-llms)
  * [Decision LLMs](#decision-llms)
  * [Learned policies and VLAs](#learned-policies-and-vlas)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
  * [Your robots, by name](#your-robots-by-name)
  * [The `.glot` file](#the-glot-file)
  * [Pilot it from Claude (MCP)](#pilot-it-from-claude-mcp)
  * [Drive it yourself](#drive-it-yourself)
  * [From a browser or a phone](#from-a-browser-or-a-phone)
  * [What it remembers](#what-it-remembers)
- [Connect any robot](#connect-any-robot)
- [Team mode](#team-mode)
- [Robot Passport](#robot-passport)
  * [Why it exists](#why-it-exists)
  * [Which robots carry one](#which-robots-carry-one)
  * [Putting a passport on a robot](#putting-a-passport-on-a-robot)
  * [How a meeting works](#how-a-meeting-works)
  * [What a passport says](#what-a-passport-says)
  * [How robots find each other](#how-robots-find-each-other)
  * [Who vouches for whom](#who-vouches-for-whom)
  * [Talking, once they have met](#talking-once-they-have-met)
  * [What a stranger can make your robot do](#what-a-stranger-can-make-your-robot-do)
  * [Privacy](#privacy)
  * [Robot Passport in Roboglot](#robot-passport-in-roboglot)
  * [The specification and its tests](#the-specification-and-its-tests)
  * [Why a new protocol, and why this name](#why-a-new-protocol-and-why-this-name)
- [Configuration](#configuration)
- [Performance](#performance)
- [Limitations](#limitations)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Safety](#safety)
- [Acknowledgements](#acknowledgements)
- [Star history](#star-history)
- [License](#license)

The rest of the documentation is in [docs/](docs/), and [docs/README.md](docs/README.md) is its map.

<br>

## Quickstart: a LeRobot SO-101 arm

Two ways to drive the same arm, and the steps that set the arm up are shared between them. **[From the terminal](#from-the-terminal)** is the path the recording at the top of this page took, in ten steps, with the arm calibrated, named and parked before anything you type can move it. **[From Claude, over MCP](#from-claude-over-mcp)** is the same arm reached from a chat instead, where the LLM you are already talking to is the pilot. Either way you need the arm and its serial port, a USB webcam, and Python 3.12 or newer, because LeRobot itself needs it. Only the terminal path needs a key for one cloud vendor, because only that one brings an LLM of its own.

### From the terminal

1. **Install the arm and a pilot into one environment.** Below Python 3.12 the `lerobot` extra resolves to nothing while the install still reports success, so pin the interpreter.

    ```bash
    uv venv --python 3.12
    uv pip install "roboglot[lerobot,openai]"     # or anthropic, gemini, grok, and so on
    ```

2. **Put the key where Roboglot reads it.** One line in a `.env` file, in the folder you run from or in the venv root: `OPENAI_API_KEY=sk-...`. `roboglot doctor` prints the key it found for each provider, masked to its ends, which is the quickest way to see that the file was read at all.

3. **Find the port, then calibrate under the name you will register.** Calibration is LeRobot's own tool and it asks you to move each joint through its range by hand. Take each one all the way into the fold you will rest the arm in, because the travel it records is written into the servos as limits they are never driven past, and a fold outside it is a pose the arm cannot be driven back to. Roboglot reads every joint limit out of the file it writes, and refuses an arm that has none.

    ```bash
    lerobot-find-port
    lerobot-calibrate --robot.type=so101_follower --robot.port=COM3 --robot.id=arm-01
    ```

4. **First contact, which moves nothing.** Connect, read the joints, temperatures and torque back, disconnect. Support the arm while it starts, because connecting releases torque for a moment. A spec on its own carries no name, so it reads the calibration saved as `arm-01` whatever name you calibrated under. If you chose another, do step 5 first and run `roboglot doctor --robot` with that name instead, which reads the calibration kept under it.

    ```bash
    roboglot doctor --robot lerobot:real --address COM3
    ```

5. **Name it.** The registry keeps the port, the camera and the pilot under one name, so every command after this is `--robot arm-01`. Register it under the id you calibrated as.

    ```bash
    roboglot robot add arm-01 lerobot:real --address COM3 --llm openai:gpt-6-astra
    ```

6. **Fold the arm by hand, then record where it rests.** An SO-101 has no brake and LeRobot releases torque when it disconnects, so without this the arm would drop from wherever a run left it, and Roboglot refuses to run it at all. With it, every run starts at this pose and returns to it before Roboglot lets go. This pose is where every run starts and ends unless the run itself says otherwise, and the one flag that says otherwise is just below step 10, where it changes the start and leaves the end alone. If it warns that a joint is recorded past what this calibration lets its servo be driven to, your fold lies outside the travel step 3 recorded: a run parks that joint at the edge of its travel and lets it settle from there, and calibrating again with the joint taken all the way into the fold, then recording the pose again, makes the fold itself reachable. Record the pose again after any new calibration too, because a calibration can move a joint's zero and the pose is kept as angles.

    ```bash
    roboglot robot rest-pose arm-01
    ```

7. **The first task moves nothing either.** `lerobot-lookout` allows `report_state` and `stop` and nothing else: it reads the arm and says what it found. There is nothing to improvise, so the scripted pilot is enough and this costs no tokens.

    ```bash
    roboglot run lerobot-lookout --robot arm-01 --llm fake
    ```

8. **Add the webcam.** `lerobot-find-cameras opencv` prints the indices and saves a frame from each, so you can see which is which. Point it at the space the arm moves through rather than at the gripper, which is the mistake the run above made.

    ```bash
    roboglot robot edit arm-01 --camera-url "opencv://2"
    ```

9. **Rehearse it.** With `--dry-run` the arm is connected and read, and not one command reaches it, so you see which verbs the LLM reaches for and with what numbers before a joint moves.

    ```bash
    roboglot run --goal "Wave to the camera with an extended arm" --robot arm-01 --max-steps 10 --dry-run
    ```

10. **Then let it move.** A hand near the power switch, the arm's whole sweep clear, and the same sentence without the flag. This run starts at the rest pose you recorded in step 6 and folds back to it when it is over, which is the default and the first of the two choices below rather than the only way a run can begin. If the arm cannot get back to its rest pose at the end, the run says it is holding itself up and asks you to clear whatever is in its way and press Enter, and it tries the fold once more. Only if that fold misses too does it ask again, and Enter at that second question takes torque off where the arm stands, so the arm drops: hold it first. Leave either question for 60 seconds and torque stays on. After that, `roboglot robot release arm-01` folds the arm to its rest pose and lets go of it there, asking the same two questions if its fold misses: support the arm while it connects, because connecting takes torque off for a moment, then take your hands away when it says so, in the 3 seconds it waits before it folds. None of this has run on a real arm yet.

    ```bash
    roboglot run --goal "Wave to the camera with an extended arm" --robot arm-01 --max-steps 10
    ```

**Or start from a pose you set by hand.** `--by-hand` gives you the arm before the pilot gets it. The arm is driven to the rest pose from step 6 first, torque comes off there, and Roboglot waits: lift the arm, put whatever the task needs into the gripper, close the gripper on it, hold the arm where the run should begin, and press Enter. Lift it out of its fold before you press Enter, even where the run should begin next to it, because a fold that lies past the travel step 3 recorded is let go of at the edge of that travel and is free to settle back past it. Roboglot writes the pose you left as the goal, puts torque back on, reads the joints again to check nothing sagged, and prints the angles it is now holding so you know you can let go. The pilot works from there. A joint outside its calibrated travel when you press Enter is the exception, whether you placed it there or never lifted it out of the fold: nothing can hold it where it is, so torque stays off, Roboglot names the joint and its travel, and the run ends with the arm limp, in your hands or still lying at its rest pose. Nothing moves the arm or puts torque on it after that, so the gripper does not open and the arm is not folded: take out whatever is in the gripper yourself. At the other end the arm is still holding whatever it ended on, so it is handed back to you before anything opens: take hold of what is in the gripper and press Enter, the gripper opens all the way, and 3 seconds later the arm folds back to the rest pose and the gripper closes again, with a Ctrl-C or `q` holding it where it is. Leave it alone and it folds up with the gripper still shut. This needs the rest pose from step 6, because the rest pose is the one place Roboglot will drop torque and an arm released anywhere else falls, and it needs a terminal, because somebody has to press Enter.

```bash
roboglot run --goal "draw a circle on the paper in front of you" --robot arm-01 --by-hand
```

**Give it a picture.** `--image` hands a file to the task itself, which is not the same thing as what the robot can see. The pilot gets each picture on its first turn, labelled with the file's own name, and keeps it in front of it for the whole run. That is what makes it different from a camera frame: a frame is perception, it arrives again every step and it shows the room as it is now, while a task picture never changes and is what the task is about. The flag repeats, so a run can carry several. It needs a pilot that takes images, `roboglot list-models` marks the LLMs that take no frames, and a local LLM needs `--vision`.

```bash
roboglot run --goal "draw what is in the picture" --robot arm-01 --image sketch.png
```

**Or put a stepper in front of the pilot LLM.** `--decision-llm` is optional, off unless you name one, and needs no change to any of the ten steps above. With `--decision-mode shadow` a run is exactly the run it would have been, and the transcript also records what the decision LLM would have chosen on each turn, which is how you find out whether it is worth switching on for your bench. With `--decision-mode on` it answers the turns whose answer is a choice among calls the arm already has, and every joint angle is still the pilot LLM's. `jev` is TypeSafe's hosted one and wants `roboglot[decision]` and `TYPESAFE_API_KEY` ([docs/guides/decision-llms/jev.md](docs/guides/decision-llms/jev.md)), `openai` is OpenAI's Decisions API and wants the `roboglot[openai]` and `OPENAI_API_KEY` a pilot through OpenAI already has ([docs/guides/decision-llms/openai.md](docs/guides/decision-llms/openai.md)), and every other name Roboglot knows, what it wants and where it runs, is one table in [docs/guides/decision-llms/README.md](docs/guides/decision-llms/README.md), a page each.

```bash
roboglot run arm-grip-check --robot arm-01 --by-hand --decision-llm jev --decision-mode shadow
```

Put the two together and you have the drawing case: you set the arm down holding a pen where the paper is, and the LLM is looking at the sketch it has to copy.

```bash
roboglot run --goal "draw what is in the picture" --robot arm-01 --image sketch.png --by-hand
```

**Two of those steps were not taken in the recording at the top of this page.** The run in that GIF was reached as `--robot lerobot:real --address COM3`, with no registered name and no rest pose. Step 5 existed that day and simply was not used. Step 6 did not exist at all: the rest pose was written after that afternoon, in answer to it. Both were taken on the same arm on 2026-09-23, and the rest pose could not be reached there, because the arm's calibration had never seen the shoulder folded all the way back and the fold lay past its travel. What Roboglot does with a fold like that now, and why step 3 asks you to calibrate folded, is [A pose past the travel](docs/adapters/lerobot/README.md#a-pose-past-the-travel). That has been exercised against `lerobot:mock` and in the test suite, and not yet on the arm. The arm in the recording is held up by torque alone, which is why it fell when the run ended. The two options after step 10 postdate that afternoon as well, and `--by-hand` and `--image` have both been exercised against `lerobot:mock` and in the test suite, and not yet on a real arm. Walk all ten and you are the second person down this path, so what differs on your bench is the part worth writing down.

[docs/adapters/lerobot/first-run.md](docs/adapters/lerobot/first-run.md) is the long way round the same path: every refusal you can hit and what it means, the safety checks worth running before a wave, what the camera can and cannot see with each kind of pilot, and [what to report](docs/adapters/lerobot/first-run.md#14-what-to-report) afterwards. Nothing moves until step 10 of [the hardware checklist](docs/adapters/lerobot/hardware-checklist.md).

### From Claude, over MCP

Steps 3 to 8 above are the same whichever way you drive the arm, because they are about the body rather than about the pilot: find the port and calibrate, connect once, name it, record a rest pose, add the webcam. Two of the others change. Step 1 needs no pilot extra, so it is `uv pip install "roboglot[lerobot]"` on its own, and step 2 goes away, because Roboglot picks no LLM in this mode and reads no key. The LLM you are already chatting with is the pilot, so there is no `--llm` here at all.

Steps 9 and 10 become one thing: point your client at the arm, then ask it in the chat. In Claude Code that is one command, and what it names is the `roboglot` inside the venv from step 1, by its absolute path.

```bash
claude mcp add arm -- D:\Development\lerobot-test\.venv\Scripts\roboglot.exe serve-mcp --robot arm-01
```

That path is a Windows one, and elsewhere it is the same venv's `bin/roboglot`. Use the venv rather than `uvx`, which builds a second environment on whichever interpreter it picks: on a machine whose default Python is 3.11 the LeRobot half of that extra resolves to nothing, silently, and you get a server with no arm backend in it. Claude Desktop takes the same command and arguments in `claude_desktop_config.json`, under Settings, then Developer, then Edit Config, and wants a full restart of the app afterwards.

Either way nine `robot_*` tools appear, and behind them is the executor the rest of this page describes: the same allowlist, the same budgets, the same feasibility verdict before anything moves, and the same refusal for a joint goal outside the range your calibration recorded. What you gain over a `--goal` run is that you choose each verb and each number yourself, which is the only way to ask for one verb and stop, and the only way to ask a real arm for a camera frame on purpose.

Two things are worth knowing before the first session. Starting the server moves the arm, because connecting drives it to the rest pose from step 6 and refuses to start at all if it cannot get there, so nobody should be in reach when a client spawns it. And there is no Ctrl-C: between verbs the brake is asking for `stop`, and during one it is the power switch.

[Part 2 of docs/adapters/lerobot/first-run.md](docs/adapters/lerobot/first-run.md#part-2-from-claude-over-mcp) is that path in fifteen steps, with both clients configured, what each tool answers, what every refusal means, and which moments move the arm without anybody asking. No MCP session has yet driven a real arm, so that half of the page is the half with the least behind it.

### What happened in that run

The command, as it was typed on the laptop in the recording:

```bash
roboglot run --goal "Wave to the camera with an extended arm" --robot lerobot:real --address COM3 --camera-url "opencv://2" --llm openai:gpt-6-astra --max-steps 10
```

No task file, no registered name, no rest pose, which is why Roboglot refuses that command today: a real arm with no rest pose has nothing to fold to when its run ends, and this one fell where its run ended. `--goal` writes a contract on the spot: the arm's own five verbs allowed, `gripper`, `move_joints`, `place`, `report_state` and `stop`, plus the four the loop always offers, `assess_task`, `declare_success`, `declare_failure` and `remember`. Exactly one of them per turn, and anything else refused. It was the last of twelve runs that afternoon, so the memory Roboglot keeps per robot handed it five notes and how the last five of the eleven before it had ended, which is the whole of what it carries.

**What the LLM was told.** About a third of the system prompt as it read that day, cut where marked, with the two lines that were wrong left in:

```text
You are the brain of a six-joint desktop robot arm with a parallel gripper (an SO-101 class
arm driven by LeRobot), bolted to a table. You are a high-level pilot: you choose ONE verb per
turn; the robot's own controllers handle the motion. Do not micro-manage.

## Rules (enforced by the executor — not optional)
- Call exactly one tool per turn. Never zero, never two.
- Only these verbs are allowed: gripper, move_joints, place, report_state, stop. Anything else is refused.
- Budgets: 40 steps, 5 minutes, 40 LLM calls. The run stops when any is hit.
- Before the first verb that moves the body, call `assess_task` with your verdict on whether
  this body can do this task at all, judged against its datasheet below: `feasible`,
  `infeasible` (the run ends, nothing moves) or `uncertain` (a human is asked). [...]

## Your body: what it can and cannot do
- Height: 0.53 m (estimate: one vendor's listing; reaching straight up)
- Actuated joints: 6 (official: the LeRobot SO-101 docs; five joints and a gripper)
- Payload: 0.5 kg (estimate: one vendor's listing)
- Not published: mass, reach. Decline any task that hinges on any of them.
- Each joint's travel in degrees, read from its own calibration, and the only goals Roboglot
  will send: shoulder_pan -120 to 120, shoulder_lift -84.2 to 84.2, elbow_flex -96.5 to 96.5,
  wrist_flex -103.2 to 103.2, wrist_roll -180 to 180, gripper 0 to 100.
Whatever the task says, this body cannot:
- go anywhere: it is bolted to a table and has no base
- feel what it holds: nothing reports grip force, so holding is inferred from the gripper
  stopping short of shut, which an empty hand that binds also does
[...]

## What you remember from earlier runs on this robot
- [2026-09-15] An extended-pose gesture reached shoulder_lift −40°, elbow_flex 24°, and
  wrist_flex 1° before wrist-roll waving; the available camera view did not show the whole
  arm to verify extension visually.
- [2026-09-15] A wrist-roll wave commanded alternately at +30° and −30° reached reported
  angles of +26–27° and −26–27°.
[... three more notes, and how the last five runs ended ...]

## Task file: goal — Wave to the camera with an extended arm

# Task
Wave to the camera with an extended arm

## Strategy
Use the available verbs. Look before you act (`observe` or `search_scan`), prefer composite
verbs like `go_to`, verify with a fresh frame, then `remember` one fact and declare success.
```

**The ten calls.** LLM seconds is how long the LLM took to answer. Arm seconds is how long the verb then took on the arm.

| Call | Tool | What it asked for | What the arm reached | LLM s | Arm s |
|---|---|---|---|---|---|
| 1 | `report_state` | a reading before anything moves | folded: `shoulder_lift` -38.2°, `elbow_flex` 85.1°, torque on, hottest servo 37 °C | 8.2 | 0.0 |
| 2 | `assess_task` | `feasible`, for the reason below | nothing moves on this call | 7.0 | |
| 3 | `move_joints` | `shoulder_lift` -40°, `elbow_flex` 25°, `wrist_flex` 0° | -38.6°, 30.0°, 0.4°, in 32 commands over 4.1 s | 8.0 | 4.1 |
| 4 | `move_joints` | `wrist_roll` +30° | 28.0° | 6.9 | 1.2 |
| 5 | `move_joints` | `wrist_roll` -30° | -25.4° | 5.7 | 2.1 |
| 6 | `move_joints` | `wrist_roll` +30° | 25.4° | 5.1 | 2.0 |
| 7 | `move_joints` | `wrist_roll` -30° | -25.3° | 3.3 | 1.9 |
| 8 | `move_joints` | `wrist_roll` 0° | -4.2° | 5.1 | 0.9 |
| 9 | `stop` | hold it where it is | held | 5.8 | 0.0 |
| 10 | `declare_success` | the reason below | | 7.0 | |

**The numbers.**

- 78.8 seconds of run, after 10.3 seconds to open the serial port.
- Ten LLM calls, 3.3 to 8.2 seconds each, 62.1 seconds in all, which is 79% of the run. The arm moved for 12.2 seconds, which is 15%.
- 49,096 tokens in, 491 out, 22 of them reasoning, and not one word of prose: the LLM's only sentences in the whole run are the two below.
- Eight verbs, 97 commands to the arm, every one accepted. No gate fired, nothing was clipped to a joint limit, and no servo read above 37 °C.
- No `remember`, and rightly. Two of the five notes already in its prompt described this manoeuvre from earlier runs that afternoon, one giving the extended pose and one the wrist angles it would reach, and its last sentence says so.

**In its own words.** Both reasons, verbatim from the transcript:

```text
assess_task, feasible: An unloaded extended-arm gesture and wrist wave need no target reach
or lifting. The visible arm is empty, and the planned shoulder_lift -40°, elbow_flex 25°,
wrist_flex 0° and wrist_roll ±30° are inside the calibrated travel limits.

declare_success: Completed the extended-pose wrist wave: shoulder_lift reached -39°,
elbow_flex 30°, wrist_flex 0°, and wrist_roll alternated +28°, -25°, +25°, -25°. Returned
wrist_roll to -4° and stopped. The fresh camera shows the raised arm, but crops its upper end,
so full extension is supported by joint state rather than fully verified visually. This
strategy is already recorded in memory.
```

<p align="center">
  <img src="https://raw.githubusercontent.com/rokbenko/quackd/main/docs/assets/lerobot-what-it-saw.png" alt="Three webcam frames from the run, side by side. Left: the arm folded on the bench with a person behind it holding a camera. Middle: the arm raised, its wrist and gripper cut off by the top edge of the frame. Right: after the stop, a hand entering from the right, palm open, waving back at the arm." width="760">
  <br>
  <sub><strong>What the pilot saw.</strong> Three of the ten frames the LLM was sent, 640x480 from one USB webcam at table height behind a calibration mat. From the third frame on, the arm it had just raised runs off the top of the picture, which is exactly what it reported. The hand in the last frame reached the LLM as pixels and never as a word: the detector that turns a frame into text called a blue figurine on a shelf a person on eight of the ten steps, and never saw anybody actually in the room.</sub>
</p>

**The honest half.** Each frame was between 5.6 and 12.5 seconds old at the moment the LLM was handed it, about eight on average, and older still by the time the move it prompted had finished, so the LLM was always looking at where the arm had been. The colour detector that turns a frame into a line of text reported a ball that was not there on every step, called a small blue figurine on a shelf a person about 8.5 metres away on eight of the ten, and never once saw the actual people in the room. The LLM ignored all of it, and used the picture for exactly one thing: noticing that the raised arm ran off the top of the frame, and saying so rather than claiming a wave it could not see. It asked for `elbow_flex` 25° and the arm settled at 30°, and it reported the 30. The arm fell when the run ended, because this was before the rest pose existed. And reading this transcript to write this section turned up two bugs, both fixed alongside it: the prompt said `Budgets: 40 steps` while the command and every observation said ten, because it was built from the task file's own contract rather than from the one the run was enforcing, and the strategy paragraph told this arm to look with `observe` or `search_scan` and to prefer `go_to`, three verbs it does not have and the allowlist at the top of the same prompt did not list. The LLM worked around the second one by looking with `report_state`, which is not a thing to rely on.

Two more lines of that prompt read differently now, for reasons a later day on the bench found. `Not published: mass, reach. Decline any task that hinges on any of them.` forbids an arm whose reach nobody published to reach for anything, and on 2026-09-23 it was one of the lines a run with a pen ended on. The line now tells the pilot to answer uncertain and name the figure rather than decline, and the arm's sheet publishes a reach of 0.4 m, an estimate summed from the link lengths in the maker's URDF ([docs/adapters/lerobot/README.md](docs/adapters/lerobot/README.md)). And the travel line has a second sentence the LLM above never saw: a joint can read past its travel when it was folded or placed there with torque off, which is where a rest pose usually is, and goals are still limited to the travel. On 2026-09-23 the arm's recorded fold lay past the travel of its shoulder, and three pilots gave a reading there, against a travel that left it out, as a reason not to move the arm at all ([A pose past the travel](docs/adapters/lerobot/README.md#a-pose-past-the-travel)).

<br>

## No robot yet? Try it in 60 seconds

Every adapter has a `mock` backend, an in-memory test double, and the scripted pilot, `--llm fake`, needs no key, so this needs nothing but the install. It is the Microduck's lookout task on that robot's mock:

```bash
uvx --from "roboglot[microduck]" roboglot run microduck-lookout --llm fake
```

What it printed here, from the run's own `terminal.txt`, cut where marked:

```
$ roboglot run microduck-lookout --llm fake
[... the header, the system prompt and the verdict ...]
▶  verb    gaze(bearing_deg=45)
→  send    look(x=0.707, y=0.707, z=0)
✓  result  gaze ok: looking +45° (0.0 s, 1 intent)
[... two more looks ...]
▶  verb    say(text='no ball in view')
→  send    sound(tag='chirp', text='no ball in view')
✓  result  say ok: said 'no ball in view' as [chirp] (0.0 s, 1 intent)
[...]
✓  declare success: reported what is in view
→  send    stop
┌─ ✓ SUCCESS ─────────────────────────────────────────────────────────────────┐
│ reported what is in view                                                    │
│ steps 4 · LLM calls 6 · tokens 9503+96 · time 0.2 s (LLM 0.0 s) · LLM calls │
│ p50 0.0 s, p90 0.0 s, max 0.0 s · first motion at 0.1 s, after 2 LLM calls  │
│ · cost $0                                                                   │
│ run dir  runs\20261115-143808-microduck-lookout                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

That is a mock doing what a mock is for, and no more. The duck's mock sends grey frames, so the lookout had nothing to find and said so, which is the answer the task asks for. What the run shows is the task file, the verdict gate, the allowlist and the run record working with no robot anywhere, and nothing about how a duck would have looked around. Seven of the other mocks draw an orange ball for the detector to find, and a wheeled base's mock keeps a pose that follows what it is told to drive, so `run --goal "walk in a square" --robot rosbridge:mock` ends with `closed the square 0.33 m from where it started, after four 0.50 m legs with a 90 degree turn between each`:

```bash
uvx --from "roboglot[rosbridge]" roboglot run --goal "walk in a square" --robot rosbridge:mock --llm fake   # a wheeled base's mock
uvx --from "roboglot[open_duck]" roboglot run open-duck-scout --llm fake           # a duck you can build: it walks up to the mock's ball and says where it is
claude mcp add roboglot -- uvx --from "roboglot[microduck]" roboglot serve-mcp --robot microduck:mock   # or chat with the duck's mock
uvx --from "roboglot[microduck,anthropic]" roboglot run microduck-lookout --llm anthropic   # a real LLM, needs ANTHROPIC_API_KEY
uvx --from "roboglot[microduck,openai]" roboglot run microduck-lookout --llm ollama:qwen3:8b   # a local LLM, no key
```

Every Roboglot line there names a body with `--from`, because Roboglot itself ships none: the core is the loop, the executor and the contract, and each robot is a package the extra of the same name pulls in ([Installation](#installation)).

Put keys in the environment or in a `.env` file (copy [`.env.example`](.env.example)), either in the folder you run the command in or in the venv root Roboglot is installed into. `roboglot doctor` tells you what is missing. Needs Python 3.11 or newer and [`uv`](https://docs.astral.sh/uv/), nothing else.

<br>

## Why?

A modern robot is not short of skills. The Microduck's onboard controllers already balance it, walk, kick, sit and scoop with its beak, and Pollen says its newest walking policy gets the duck back up after a fall. An arm picks with its own learned policy, a wheeled base drives. Each is the robot's own skill, trained, written or recorded, and each works without any help from an LLM. What the robot lacks is any idea of **what those skills are for**.

```
Traditional control:   walk forward, turn left, walk, look down, scoop, ...   (you plan every step)
One robot:             "Pick up the ball."                                    (you state the goal)
A team of them:       "Pick up the ball."                                    (they also settle who does it)
```

Low level skills and high level goals are different layers. The robot knows the words, but it cannot hold a conversation. Roboglot is an open source attempt to connect the two layers, with an LLM doing the planning and the robot's own controllers doing the moving.

**The second gap opens with the second robot.** Every body speaks its own protocol, the arm's SDK, the cart's ZeroMQ host, the base's ROS topics, and every body has a different set of skills, so the robots you own end up commanded from as many terminals as there are robots and none of them knows the others exist. Roboglot puts them behind one command line, under names you choose, and lets one goal go to several of them at once. Each robot's pilot is told what the others are and what they can do, so the work gets divided on data rather than on guesses.

<br>

## How it works (the simple version)

```mermaid
flowchart TD
    YOU["You<br/>“find the ball and kick it”"]
    LLM["LLM<br/>looks at the camera, the robot's state and the last result<br/>picks ONE of the robot's own skills (a verb) and its parameters"]
    Q["Roboglot<br/>checks the rules: allowed? task judged possible? budget left? needs confirmation?<br/>then runs the verb"]
    R["Robot<br/>executes the skill with its own controllers<br/>(walking, grasping and looking are not the LLM's job)"]
    O["Roboglot observes the result<br/>new camera frame, new state"]
    YOU --> LLM --> Q --> R --> O
    O -- "next verb, until done or impossible" --> LLM
```

The verbs the LLM can pick from are the robot's real, existing capabilities and nothing more. They come from its manifest, and a verb that is not in the manifest does not exist:

| Kind | Verbs | What they are |
|---|---|---|
| Core | `observe` `report_state` `stop` `say` `move` `go_to` `search_scan` `approach_and` `map` `mark_place` `forget_place` `go_to_place` | on any robot whose manifest satisfies their requirements (a camera, a twist intent, a sound intent). The last four name the spots a robot stood on, list them and walk back to them, on a robot whose connection says where it is: a Microduck by its own odometry, a MOSS rover and a rosbridge base by theirs, and the mocks of all three ([docs/concepts/places.md](docs/concepts/places.md)) |
| Microduck | `sit` `stand` `stand_up` `kick` `grab` `gaze` `quack` `watch` | one each per behaviour the robot ships with, each an *intent* the robot's own controllers execute. `watch` is Roboglot's own reflex and moves the head alone: it keeps something you describe in view for up to 30 seconds by asking a decision LLM that can see where it is in each camera frame, and it is there only on a run started with `--decision-llm openai --decision-frames`, and on a real duck only through mediad's `/frame` ([docs/adapters/microduck/README.md](docs/adapters/microduck/README.md#watch-a-head-that-keeps-something-in-view)). |
| LeRobot arm | `move_joints` `gripper` `place` `pick` `manipulate` | an SO-101 class arm. `pick` and `manipulate` are each one skill intent the arm's own learned policy executes, confirm gated and present when a run names a policy server with `--policy-url`, and always on the mock, which scripts its own. `manipulate` hands it one short subtask and never says the task is done |
| rosbridge base | `introspect` | a wheeled base over ROS 2. It gets `move`, `stop` and `report_state`, plus `observe`, `go_to`, `search_scan` and `approach_and` once an image topic is configured. `introspect` asks the bridge what the body is: the topic list and the robot's own description, which is where its weight and its joint count come from |
| Open Duck Mini v2 | `gaze` `express` `quack` | a 42 cm biped. No `sit`, no `kick`, no `stand_up`: its runtime has no such skill, so the verb does not exist rather than being refused |
| XLeRobot | `move_joints` `gripper` | a dual-arm cart. The arm joints are a normalised -100..100 range, not degrees, and `gripper` takes a `side` because there are two of them |
| AlohaMini | `lift` `move_joints` `gripper` `home_arms` | two arms on a motorised lift. The arm verbs refuse until Roboglot's own host wrapper is running on the robot, because upstream's leaves the arms limp |
| ToddlerBot | `look` `stand` `perform` `grip` | a humanoid. `look` turns a two joint neck, `stand` slews to the safe pose and is not a way up from a fall, and `perform` plays only the keyframe motions the daemon actually loaded. `grip` appears on the gripper builds, which carry two more motors |
| Huebot | `sit` `stand` `stand_up` `kick` `quack` | a 25 cm biped whose maker is writing a shim for it that is to answer the Microduck's protocol, so these are the Microduck's verbs without `gaze` and `watch`, since the shim does not answer `robot.look` yet, and without `grab`, which waits for its maker to say what `ground_pick` does on Huebot. `sit`, `stand` and `kick` are there only when the shim lists the skill each one sends ([docs/adapters/huebot/README.md](docs/adapters/huebot/README.md)) |
| MOSS | `drive_to` `explore` `pick_and_drop` `stow_arm` `collect_litter` | a small tracked rover that picks up litter, reached through its own cockpit and a bridge Roboglot ships for the rover. `drive_to` and `explore` hand a goal or a few minutes to MOSS's own planner and explorer, `pick_and_drop` and `stow_arm` play the maker's fixed arm cycle, which reaches for nothing, and `collect_litter` gives the rover to MOSS's own litter mission. It is the one `dangerous` verb, and it runs once per stack start ([docs/adapters/moss/README.md](docs/adapters/moss/README.md)) |
| Industrial arm on ROS 2 | `move_joints` | a UR5e, a KUKA LBR iisy or iiwa or a Yaskawa MotoMini, through its ROS 2 driver and rosbridge, rehearsed only. `move_joints` sends one goal to every joint, at most at a tenth of each joint's rated speed at its fastest, and asks a person first every time: on `rosarm:mock` `--yes` may answer for them, and on `rosarm:ws` it does not. No gripper and no `pick`: Roboglot drives no tool, and it never powers, enables or un-brakes an arm ([docs/adapters/rosarm/README.md](docs/adapters/rosarm/README.md)) |
| Aliases | `get_frame` `walk_to` `walk` | the 0.3 names of `observe`, `go_to` and `move`. They keep working in every `.glot` file |
| Learned | *(none yet)* | v2: policies trained from LLM written rewards, registered like any other verb. The arm's `pick` and `manipulate` do run a learned policy, and they are the arm's own verbs rather than these ([docs/guides/policies.md](docs/guides/policies.md)) |

`go_to` (still spelled `walk_to` in the older starter files) is a small closed loop in plain Python that steers toward whatever the camera sees, ten times a second, without asking the LLM. The LLM says *"go to the ball"* and never *"turn 4° left"*. The same code steers a duck, a cart and a wheeled base, clamped to each manifest's speed limits. On a body with no locomotion, such as the arm, `go_to` does not exist at all. On the ToddlerBot, which looks with a two joint neck, `search_scan` sweeps the head instead of turning the body.

A team is that same loop once per robot, all at once, with a bus between the pilots so one can tell another what it is about to do ([Team mode](#team-mode)).

<br>

## Example

An `open-duck-scout` run on the Open Duck Mini's mock, from its transcript (`runs/<timestamp>-open-duck-scout/transcript.jsonl`). The mock draws an orange ball for the duck's camera, so `go_to` has something to steer at. Every run opens the same way, with the pilot judging whether this body can do this task at all, because nothing that moves the duck runs until it has. This one is the scripted pilot, so `llm_id` says so, the verdict says a rule has no judgement of a body, and `usage` is an estimate from character counts (no tokenizer). A real provider records the API's own counts and weighs the task against the datasheet in its prompt.

```jsonc
{"kind": "llm",  "step": 0, "tool_calls": [{"name": "assess_task", "arguments": {"verdict": "feasible", "reason": "scripted pilot: a rule has no judgement of the body, so it assumes the task fits"}}], "usage": {"input_tokens": 1658, "output_tokens": 16}}
{"kind": "assess", "step": 0, "verdict": "feasible", "reason": "scripted pilot: a rule has no judgement of the body, so it assumes the task fits"}
{"kind": "llm",  "step": 0, "tool_calls": [{"name": "go_to", "arguments": {"target": "ball", "stop_distance": 0.3}}]}
{"kind": "verb", "step": 1, "name": "go_to", "ok": true, "summary": "reached the ball: ~0.28 m away, bearing +0°", "data": {"distance_m": 0.278, "bearing_deg": 0.0, "ticks": 53}}
{"kind": "llm",  "step": 1, "tool_calls": [{"name": "say", "arguments": {"text": "ball at 0 degrees left, about 0.3 m"}}]}
{"kind": "verb", "step": 2, "name": "say", "ok": true, "summary": "said 'ball at 0 degrees left, about 0.3 m' as [chirp]"}
{"kind": "llm",  "step": 2, "tool_calls": [{"name": "declare_success", "arguments": {"reason": "walked up and reported"}}]}
```

The same thing as a conversation, through MCP in Claude Code or Claude Desktop:

> **You:** List the duck's verbs, then find the ball, walk up to it and say where it is.
> **Claude:** *(calls `robot_list_verbs`, `robot_observe`, `robot_assess_task("feasible")`, `robot_run_verb("go_to")`, `robot_say`)* Done. I walked up to the ball and said where it is.

And the same shape with two robots instead of one, from the `team.jsonl` of a `team-hello` run: the duck's mock and the arm's, one pilot each, on wall clock. Nothing here moves a joint on purpose, because this is the smallest honest test that two pilots in two different bodies can find each other and exchange a fact.

```jsonc
{"t": 0.94, "kind": "bus", "msg": {"src": "duck", "kind": "TALK", "to": null, "text": "duck here and ready; say hello back"}}
{"t": 1.048, "kind": "bus", "msg": {"src": "arm", "kind": "TALK", "to": null, "text": "arm here and ready; say hello back"}}
{"t": 1.145, "kind": "member_end", "robot": "arm", "outcome": "success", "reason": "said hello and heard back from duck", "llm_calls": 3}
{"t": 1.147, "kind": "bus", "msg": {"src": "team", "kind": "TALK", "to": null, "text": "arm declared success: said hello and heard back from duck"}}
{"t": 1.309, "kind": "member_end", "robot": "duck", "outcome": "success", "reason": "said hello and heard back from arm", "llm_calls": 4}
{"t": 1.31, "kind": "bus", "msg": {"src": "team", "kind": "TALK", "to": null, "text": "duck declared success: said hello and heard back from arm"}}
{"t": 1.318, "kind": "team_end", "outcome": "success", "reason": "every member declared success: duck, arm", "messages": 2, "llm_calls": 7}
```

`tell` is what put the first two lines on the bus. It moves nothing, costs no step, and arrives in the addressee's next observation. Each member then declared for itself, the runner put a line of its own on the bus as `team` each time to tell the other, and the team succeeds only when all of them did. This one is the scripted pilot again, so the sentences are a rule's and not an LLM's.

<br>

## Status

Version 0.34, one real arm and mocks for the rest. What has been built, and how far each piece has actually been exercised:

| Piece | Status |
|---|---|
| Manifests and core verbs (`roboglot list-adapters`, `roboglot list-verbs --robot`) | ✅ ten adapters, twelve core verbs that appear only where the manifest meets their requirements, speed limits from the manifest, `manifest.schema.json` generated and drift tested |
| MCP server (`roboglot serve-mcp`) | ✅ Claude Code and Claude Desktop, one robot or a team with `--robots` or `--team NAME` (nine `robot_*` tools, tested in process against the mocks), no Claude Desktop session on record |
| Driving by hand (`roboglot drive`) | ✅ implemented and tested offline against the mock Microduck, the scripted pilot and stand-ins for a decision LLM: the exact and fast lanes, the presets on every shipped body, the brake, a newer command ending the one moving, goals held to the session's contract, flown with run's flags and putting their questions to the person driving, and the keyboard through prompt_toolkit's own pipe input. 🧪 it has driven no real robot from a keyboard, a VLA session has flown only the LeRobot mock's scripted policy, no real decision LLM has answered its question, and its prompt is untried in PowerShell, Windows Terminal and VS Code's terminal ([docs/guides/drive.md](docs/guides/drive.md)) |
| The page (`roboglot ui`, `roboglot[ui]`) | ✅ its screens driven by Streamlit's own test harness in CI's `ui` job, which also starts `roboglot ui` and waits for its health check to answer, and the guide's screenshots are real runs with the scripted pilot. 🧪 never tried from a phone: at a phone's width it has been seen only in a headless browser ([docs/guides/web-ui.md](docs/guides/web-ui.md)) |
| Memory between runs (`roboglot memory`, `remember`) | ✅ one JSONL file per `adapter:backend`, or per registered robot name, notes and run outcomes into the next prompt, tested end to end offline, 🧪 the `remember` tool itself exercised by one cloud LLM on a real robot, `gpt-6-astra` calling it in seven of its twelve runs on the arm on 2026-09-15 for the five distinct notes that survive deduplication, and the last of those runs read the five back in its prompt ([What happened in that run](#what-happened-in-that-run), [docs/guides/memory.md](docs/guides/memory.md)) |
| Places (`mark_place`, `map`, `forget_place`, `go_to_place`, `roboglot map`, `roboglot places`) | ✅ against the Microduck mock's scripted pose, against stand-ins for MOSS's cockpit and a rosbridge base, and from the command line on `rosbridge:mock`. 🧪 Roboglot's `mapd` client has met only a stand-in, never `mapd`, the real duck's own mapper, since no robotd release carries it (UNVERIFIED), and no real robot has walked back to a place ([docs/concepts/places.md](docs/concepts/places.md)) |
| Providers: twelve cloud vendors, fake | ✅ implemented, tested offline against stubbed SDK clients, with one hand curated catalogue of 122 LLM ids that the half of `--llm` after the colon is checked against before any call (`roboglot list-models`), and on OpenRouter an id the catalogue does not carry can be named too, checked against OpenRouter's public LLM list before the first paid call unless Roboglot refuses its spelling first, 🧪 two cloud LLMs have driven a real robot, both OpenAI's and both on the SO-101 arm: `gpt-6-astra` on 2026-09-15, which is the recording at the top of this page, and both it and `gpt-6-sol` on 2026-09-23. No OpenRouter LLM has answered a real Roboglot request: its chat requests have only reached a stand-in on 127.0.0.1, through the real `openai` SDK |
| Local LLMs (Ollama, vLLM, llama.cpp, LM Studio, any OpenAI compatible server) | ✅ implemented and tested against the OpenAI wire format, 🧪 never run on this machine. What one contributor measured with Qwen3-32B-AWQ on vLLM is their report, read in [docs/guides/local-llms.md](docs/guides/local-llms.md#honest-notes), and a transcript from any server is welcome |
| Registered robots and teams (`roboglot robot`, `roboglot team`) | ✅ both command groups over `~/.roboglot/robots.json` and `~/.roboglot/teams.json`, so `--robot NAME` means the same thing in every command that takes a robot and `--team NAME` in `run` and `serve-mcp`, tested offline, `robot list --probe` answered by the mocks, and pointed at hardware on 2026-09-23, when the SO-101 was registered as `arm-01` with a rest pose and every run of the day named it ([docs/guides/registry.md](docs/guides/registry.md)) |
| Pilot teams, several robots on one task (`--team NAME`) | ✅ one whole pilot per body, any backend, same or different bodies, 2 to 8, each with its own executor, allowlist, budget, heartbeat, memory and verdict, dividing the work with `tell` over the bus, 🧪 experimental, exercised on mock bodies with the scripted pilot, by no real LLM and on no hardware |
| LAN discovery (`roboglot discover`, `roboglot announce`, `roboglot[lan]`) | ✅ record format and both commands on fakes in the suite, 🧪 real zeroconf exercised once on one machine, never between two ([docs/guides/lan.md](docs/guides/lan.md)) |
| MQTT team bus (`MqttBus`, library only) | ✅ its one message kind, `TALK`, and a whole `team-hello` run on a fake broker, 🧪 exercised once between two nodes through a local broker on one machine, never a team across machines ([docs/guides/lan.md](docs/guides/lan.md)) |
| Robot Passport on a robot's own computer (`roboglot onboard`, `roboglot[onboard]`, `roboglot passport check`) | ✅ built for an NVIDIA Jetson and tested on the `sim` board, where two simulated robots on one laptop, portraying a Unitree G1 EDU and an Agile ONE SN from their makers' published figures, meet over a simulated air in `roboglot onboard demo`. 🧪 nothing of it has run on a Jetson, over a real Bluetooth radio or between two machines: the radio's code has met fakes and a simulated air, its BlueZ half has never met bluetoothd, the distance two robots meet at is unmeasured, and the beacon id's rotation and BlueZ's address privacy are designed and untested on a radio ([docs/passport/roadmap.md](docs/passport/roadmap.md)) |
| Discrete stepper (`--decision-llm`, `roboglot[decision]`, `roboglot[laya]`) | ✅ implemented and tested offline against a stub SDK, with the classification of every verb of every shipped body frozen in a test, and seven decision LLMs Roboglot can name, each with a page of its own linked from [its table](docs/guides/decision-llms/README.md#the-ones-roboglot-names), and `--decision-frames`, which shows one of them, `openai`, the robot's primary camera on a run that asks, at OpenAI's own hosts alone, tested against a stand-in for OpenAI's API, 🧪 the client has never been run against any decision LLM's real API, hosted or self-hosted, and never on hardware, so the speed and cost figures in its page are an estimate rather than a measurement, and of the four confidence floors two are numbers TypeSafe publish and two are Roboglot's own, all four shaped around Jev and inherited unmeasured by every other one. Off unless you name one. `--decision-mode shadow` exists to measure one before anybody switches it on ([docs/guides/decision-llms/README.md](docs/guides/decision-llms/README.md)) |
| A learned policy as the arm's executor (`manipulate`, `roboglot policy serve`, `roboglot[lerobot-vla]`) | ✅ the policy loop, the server and its protocol, the checks the arm makes before any torque and `--controller vla`, tested against a fake arm with scripted policies, and with a tiny random ACT and a tiny random X-VLA served through the real server to the real client by a CI job on Python 3.12. A trained ACT from the Hub, served on a laptop's CPU, answered Roboglot's own client under `serve-mcp` on 2026-09-28 and under OpenAI's `gpt-6-sol` in a `roboglot run --goal` on 2026-09-29, which proves the plumbing and nothing about the task. 🧪 `--controller vla` and its judge prompt have never run with a trained checkpoint, no real decision LLM has run beside a policy, SmolVLA loaded on that laptop and took minutes a chunk on its CPU, so it wants a GPU, pi05, pi0, GR00T N1.7 and a trained X-VLA have not run in the server, FLUX 3 Action is not served at all, and no policy has driven the arm, so how fast the loop runs on the real bus while the laptop infers is unmeasured ([docs/guides/policies.md](docs/guides/policies.md)) |
| Playing a part (`--play`, `play: true` at `glot: 4`) | ✅ one section in the system prompt, built from the body, the run's verbs and its memory and never from the task's words, held to the plain prompt plus that section on every shipped body, with the record, the header and the refusals tested offline, 🧪 118 of the arm's example files play it, and no played run has run on the arm or asked a paid LLM yet ([docs/guides/play.md](docs/guides/play.md)) |
| Head reflex (`watch`, on a Microduck) | ✅ implemented and tested offline: the head closes on the ball over a mock whose camera draws it where the head points, with a fake that finds it in each JPEG it is handed, through Roboglot's own client for OpenAI's Decisions API on a fake of its SDK, and every way a call can end has a test. 🧪 never run against OpenAI, so how long a look takes and what it costs are unmeasured, and never on a duck, whose head numbers are starting values until one is measured ([docs/adapters/microduck/README.md](docs/adapters/microduck/README.md#watch-a-head-that-keeps-something-in-view)) |
| Learned verbs | 🗺️ v2, interface and docs only ([docs/concepts/learned-verbs.md](docs/concepts/learned-verbs.md)) |

Everything Roboglot assumes about each robot's API, and how sure we are: [docs/adapters/status.md](docs/adapters/status.md). `roboglot doctor` prints the unverified ones for your machine.

<br>

## Which robots work

Ten robots, and one table for how far each one has actually got. Each name links to that robot's own page. The distinction that matters is between code we have run and hardware we have not: **exactly one of the ten has driven the real robot, an SO-101 arm on 2026-09-15 and again on 2026-09-23, and the other nine have not**, so for those nine the honest question is still how much of the path to a first run is tested.

Each of the ten is its own package, pulled in by the extra that carries its name (`roboglot[microduck]`, `roboglot[lerobot]` and so on, or `roboglot[robots]` for all of them), so a build knows only the bodies you asked for. `roboglot list-adapters` prints the whole table either way and marks the ones this machine cannot run, whether that is the adapter missing or the library its real backend needs.

| Tier | What that means |
|---|---|
| 🤖 **verified** | The real robot has moved under Roboglot at least once, on a day and a build this table names, with what went wrong written down beside what worked. One backend carries this mark, and the table below says **hardware** beside it |
| 🧪 **bound** | Code that reaches a real robot and has never met one. A new one enters only with a named owner and a date for its first hardware run ([ADR-0076](docs/adr/0076-every-backend-has-a-tier-and-bound-code-names-its-owner.md)), or as described and refused until both are named. Two kinds. **Daemon**: the wire protocol runs end to end against the real on-robot daemon over loopback in CI, so everything except the robot is exercised. **Names**: every upstream name was read from upstream source at a pinned commit and exercised against fakes, and it has never connected to anything real |
| ✅ **rehearsed** | Runs a whole task with no robot, on its mock: every verb runs offline against a scripted double, in the test suite and from the command line. A mock shows the contract and the gates working and nothing about the body |
| 📄 **described** | A body Roboglot lists and reasons about and drives no part of: one file of its maker's published figures, with a source for each. They are under the table below. One backend in it is described too: `rosarm:ws` is bound code with no owner yet, so it refuses to start until somebody names a date for its first hardware run ([ADR-0078](docs/adr/0078-an-industrial-arm-is-moved-one-confirmed-goal-at-a-time.md)) |

| Robot | `--robot` | The body | How far it has got |
|---|---|---|---|
| **[Microduck](docs/adapters/microduck/README.md)** | `microduck:mock` | a 25 cm biped from Pollen Robotics | ✅ mock |
| | `microduck:jsonrpc` | the real one, over `robotd` | 🧪 names. Early pre-orders arrive around Christmas 2026, later orders in four to six months ([checklist](docs/adapters/microduck/hardware-checklist.md)) |
| **[Open Duck Mini v2](docs/adapters/open_duck/README.md)** | `open_duck:mock` | a 42 cm 3D printed biped you can build yourself | ✅ mock |
| | `open_duck:bridge` | the real one, through a daemon Roboglot ships for its Raspberry Pi | 🧪 daemon. **The nearest of the nine untouched bodies to a first run of its own**, because the hardware is buildable today ([checklist](docs/adapters/open_duck/hardware-checklist.md)) |
| **[LeRobot arm](docs/adapters/lerobot/README.md)** | `lerobot:mock` | an SO-101 class desktop arm | ✅ mock |
| | `lerobot:real` | the real one, through LeRobot | 🤖 hardware, on 2026-09-15 and again on 2026-09-23. The first time it was an SO-101 follower arm on Windows 11, Python 3.12.12, lerobot 0.6.1 and Roboglot 0.9.0, reached as `--robot lerobot:real --address COM3` with no registered name, and piloted by OpenAI `gpt-6-astra`. `lerobot-lookout` ran, and twelve free-form `--goal` runs waved the wrist about ±27°, held extended poses at `shoulder_lift` -39 and `elbow_flex` 24 to 30, and opened and closed the gripper, once miming a duck quacking with it. The last of the twelve is the recording at the top of this page, and [What happened in that run](#what-happened-in-that-run) reads its transcript: ten LLM calls, eight verbs, 97 commands to the arm, every one accepted. The camera was a USB webcam at `opencv://2`, 640x480. The honest half: the arm fell at the end of every run that day, which is what the rest pose was written to stop (it first met that arm on 2026-09-23, and could not reach a fold that lay past the calibrated travel), one dry run aborted on a single heartbeat `TimeoutError` that never came back, another aborted because the pilot answered `uncertain` and the human said no, and the camera framed the gripper and cropped the raised arm, so the LLM checked its own waves against joint readings rather than against the picture. Nobody has yet measured whether the band that infers `holding` from a gripper stopping short is right, what a joint reads after ten minutes of work, whether a stall is caught on purpose, or whether 5° an action felt right in the room. On 2026-09-23 the same arm, registered as `arm-01` with a rest pose recorded under it, took 26 runs on Roboglot 0.12.0, piloted by OpenAI `gpt-6-sol` and `gpt-6-astra`. Twenty-three of them ran ten of the task files now in [docs/examples/lerobot/](docs/examples/lerobot/README.md) and three were goals typed on the line, and 19 of the 26 never moved the arm at a pilot's request. None of what Roboglot changed in answer has run on the arm yet. Behind `roboglot[lerobot]`, Python 3.12 or newer ([Quickstart](#quickstart-a-lerobot-so-101-arm), [first run](docs/adapters/lerobot/first-run.md), [checklist](docs/adapters/lerobot/hardware-checklist.md)) |
| **[Any ROS base](docs/adapters/rosbridge/README.md)** | `rosbridge:mock` | any wheeled base that takes a Twist | ✅ mock |
| | `rosbridge:ws` | the real one, over `rosbridge_server` | 🧪 names, behind `roboglot[rosbridge]` |
| **[XLeRobot](docs/adapters/xlerobot/README.md)** | `xlerobot:mock` | a dual-arm mobile manipulator on an IKEA cart, about $660 to build | ✅ mock |
| | `xlerobot:zmq` | the real one, over the ZeroMQ host it already ships | 🧪 names, behind `roboglot[xlerobot]`. The whole wire format is exercised against a fake host over loopback ([checklist](docs/adapters/xlerobot/hardware-checklist.md)) |
| **[AlohaMini](docs/adapters/alohamini/README.md)** | `alohamini:mock` | two arms on a lift, on a wheeled base | ✅ mock |
| | `alohamini:zmq` | the real one, over the ZeroMQ host it already ships | 🧪 names, behind `roboglot[alohamini]`. The wire is exercised against a fake host over loopback. Its arms need Roboglot's own host on the robot, because upstream's leaves them limp ([checklist](docs/adapters/alohamini/hardware-checklist.md)) |
| **[ToddlerBot](docs/adapters/toddlerbot/README.md)** | `toddlerbot:mock` | a small open source humanoid you can build | ✅ mock |
| | `toddlerbot:bridge` | the real one, through a daemon Roboglot ships for it | 🧪 daemon: the protocol and the daemon's own safety machinery exercised against a fake body over loopback. It has no walk policy unless you stage one, and it cannot get up if it falls ([checklist](docs/adapters/toddlerbot/hardware-checklist.md)) |
| **[Huebot](docs/adapters/huebot/README.md)** | `huebot:mock` | a 25 cm biped from Leif Rydenfalk, with a camera, a distance sensor and an LED face | ✅ mock |
| | `huebot:jsonrpc` | the real one, over a shim its maker is writing for it, which is to answer the Microduck's protocol | 🧪 names, behind `roboglot[huebot]`. Exercised against a fake shim over loopback, and nobody has seen the real one: [what it must answer](docs/adapters/huebot/README.md#what-huebots-shim-must-answer) is on its page. Its maker's page says every kit order ships before Christmas ([checklist](docs/adapters/huebot/hardware-checklist.md)) |
| **[MOSS](docs/adapters/moss/README.md)** | `moss:mock` | a small tracked rover that picks up litter, with an arm that drops what it picks into a bin on top | ✅ mock |
| | `moss:cockpit` | the real one, over its own cockpit and a bridge Roboglot ships for the rover | 🧪 names, behind `roboglot[moss]`. The client is exercised against a fake of the cockpit and against Roboglot's own bridge in its fake mode over loopback, and against MOSS's own cockpit in its demo mode, on Windows and on Linux. Nothing has run on a rover ([checklist](docs/adapters/moss/hardware-checklist.md)) |
| **[Industrial arm on ROS 2](docs/adapters/rosarm/README.md)** | `rosarm:mock` | a Universal Robots UR5e, a KUKA LBR iisy 3 R760, a KUKA LBR iiwa 7 R800 or a Yaskawa MotoMini, chosen with `--robot-type` | ✅ mock: the real transport over a fake rosbridge and a fake of each arm's driver, written from reading its source. `rosarm-lookout` and a confirmed wave run on all four |
| | `rosarm:ws` | the real one, through its ROS 2 driver and `rosbridge_server` | 📄 described: bound code that refuses at `make()` and at `roboglot robot add` until somebody names an owner and a date for its first hardware run, and no job has run it against a real controller either ([status](docs/adapters/rosarm/README.md#status)) |

**Described bodies.** Beyond the ten, Roboglot describes robots it drives no part of ([ADR-0077](docs/adr/0077-a-body-roboglot-only-describes-is-one-yaml-in-the-core.md)), such as a Unitree B2 and a Franka Research 3. Each is one file of its maker's published figures, with a source and the day it was read beside every one, reached as `--robot described:unitree-b2`. You can register one, read its datasheet, have a pilot judge a task against it and plan with it in a team. Its only verbs are `report_state` and `stop`, and its pilot is told before any figure that the body moves only if someone else moves it. Four of them, the UR5e, the two KUKA LBRs and the MotoMini, are also the arms `rosarm:mock` rehearses, from the same files. Nothing here has checked a figure against a robot. [docs/adapters/status.md](docs/adapters/status.md#described-bodies) lists every one with its numbers, and [CONTRIBUTING.md](CONTRIBUTING.md#add-a-described-body) is how the next one joins: one file of figures and its name on a list.

**If you own one of these, the Open Duck Mini is where help is worth the most.** It is a body a stranger can build from scratch, the daemon and the protocol are already exercised against each other, and the only untested part left is the duck. [docs/adapters/open_duck/hardware-checklist.md](docs/adapters/open_duck/hardware-checklist.md) is the order to try it in, feet off the ground until step 10.

**If you own an SO-101, the [Quickstart](#quickstart-a-lerobot-so-101-arm) at the top of this page is the path**, ten steps from an empty laptop to the arm waving, because LeRobot is a `pip install` and Roboglot ships no daemon for the arm. [docs/adapters/lerobot/README.md](docs/adapters/lerobot/README.md) is written for someone who already drives this arm and wants to know what Roboglot adds to it, what it deliberately does not touch, and what to do when it refuses. [docs/adapters/lerobot/first-run.md](docs/adapters/lerobot/first-run.md) is the long way round the same ten steps, with every refusal you can hit and what to report afterwards. Nothing moves until step 10 of [its checklist](docs/adapters/lerobot/hardware-checklist.md). It is the one path here somebody has walked to the end: the run in the table above followed it, on the machine that wrote it, before the registered name and the rest pose existed.

<br>

## Which models work

A run has up to three models in it, and only the first is required: the pilot LLM, which plans and calls the robot's verbs, an optional decision LLM in front of it for the turns that are a choice, and on the SO-101 arm a learned policy that drives the arm for one short segment at a time. The robots are the section above. Every id, what each one needs and who makes it is in [docs/models/](docs/models/README.md), whose tables are rendered from the code that decides what Roboglot takes, and `roboglot list-models` prints the same rows (`--kind decision` and `--kind policy` for the other two).

| Role | Named with | What it does | What Roboglot names | How far it has got |
|---|---|---|---|---|
| **Pilot LLM**, required | `--llm VENDOR[:LLM]` | reads the robot's manifest, plans, calls its verbs one turn at a time and judges the result | 122 LLM ids from twelve cloud vendors, more through OpenRouter, and any LLM your own Ollama, vLLM, llama.cpp or LM Studio serves | 🤖 two of OpenAI's have flown the SO-101 arm, `gpt-6-astra` on 2026-09-15 and it and `gpt-6-sol` on 2026-09-23. No OpenRouter LLM has answered a real Roboglot request |
| **Decision LLM**, optional | `--decision-llm NAME[:LLM]` | answers the turns that are a choice among calls the body already has, with a probability, and writes nothing | seven decision LLMs, hosted or your own | 🧪 stand-ins only. None has answered a real robot |
| **Learned policy**, the SO-101 arm only | `--policy-url`, to `roboglot policy serve` or to an endpoint as `hf:NAME` | drives the arm for one `manipulate` or `pick` segment, at the arm's rate, with every goal held to its travel | six LeRobot policy types from the Hub, five of them VLAs: ACT, SmolVLA, pi05, pi0, X-VLA and NVIDIA's GR00T N1.7 | 🧪 a trained ACT from the Hub has answered Roboglot's own client from a laptop's CPU, and none has driven the real arm |

### Pilot LLMs

| Provider | Extra | Key | Run |
|---|---|---|---|
| Claude | `roboglot[anthropic]` | `ANTHROPIC_API_KEY` | `uvx --from "roboglot[microduck,anthropic]" roboglot run hello-world --llm anthropic` |
| OpenAI | `roboglot[openai]` | `OPENAI_API_KEY` | `uvx --from "roboglot[microduck,openai]" roboglot run hello-world --llm openai` |
| Gemini | `roboglot[gemini]` | `GEMINI_API_KEY` | `uvx --from "roboglot[microduck,gemini]" roboglot run hello-world --llm gemini` |
| Grok | `roboglot[grok]` | `XAI_API_KEY` | `uvx --from "roboglot[microduck,grok]" roboglot run hello-world --llm grok` |
| Mistral | `roboglot[mistral]` | `MISTRAL_API_KEY` | `uvx --from "roboglot[microduck,mistral]" roboglot run hello-world --llm mistral` |
| DeepSeek | `roboglot[deepseek]` | `DEEPSEEK_API_KEY` | `uvx --from "roboglot[microduck,deepseek]" roboglot run hello-world --llm deepseek` |
| Cohere | `roboglot[cohere]` | `COHERE_API_KEY` | `uvx --from "roboglot[microduck,cohere]" roboglot run hello-world --llm cohere` |
| Qwen | `roboglot[qwen]` | `DASHSCOPE_API_KEY` | `uvx --from "roboglot[microduck,qwen]" roboglot run hello-world --llm qwen` |
| Kimi | `roboglot[kimi]` | `MOONSHOT_API_KEY` | `uvx --from "roboglot[microduck,kimi]" roboglot run hello-world --llm kimi` |
| GLM | `roboglot[glm]` | `ZAI_API_KEY` | `uvx --from "roboglot[microduck,glm]" roboglot run hello-world --llm glm` |
| Meta | `roboglot[meta]` | `META_API_KEY` | `uvx --from "roboglot[microduck,meta]" roboglot run hello-world --llm meta` |
| OpenRouter | `roboglot[openrouter]` | `OPENROUTER_API_KEY` | `uvx --from "roboglot[microduck,openrouter]" roboglot run hello-world --llm openrouter` |
| fake (scripted) | none | none | `uvx --from "roboglot[microduck]" roboglot run hello-world --llm fake` |
| Ollama (local) | `roboglot[openai]` | none | `uvx --from "roboglot[microduck,openai]" roboglot run hello-world --llm ollama:qwen3:8b` |
| vLLM (local) | `roboglot[openai]` | none | `uvx --from "roboglot[microduck,openai]" roboglot run hello-world --llm vllm:Qwen/Qwen3-8B` |
| llama.cpp (local) | `roboglot[openai]` | none | `uvx --from "roboglot[microduck,openai]" roboglot run hello-world --llm llamacpp` |
| LM Studio (local) | `roboglot[openai]` | none | `uvx --from "roboglot[microduck,openai]" roboglot run hello-world --llm lmstudio` |
| any OpenAI compatible server | `roboglot[openai]` | optional | `uvx --from "roboglot[microduck,openai]" roboglot run hello-world --llm local --base-url http://host:8000/v1` |

Every row above runs on the Microduck's mock, because `roboglot[microduck]` is the one body those lines install and `hello-world` names no robot of its own, so the run takes that adapter's first backend, its `mock`. The extras are independent, so `roboglot[anthropic]` alone gives you a brain and no body at all.

A cloud LLM that takes an image sees the camera frame. Where a vendor does not document image input, `roboglot list-models` marks that LLM `no frames` and Roboglot sends it the detections as text instead. An OpenRouter id Roboglot does not carry gets the frame when OpenRouter's LLM list says it takes images, and the detections as text when it does not. Local LLMs get the text detections by default and the frame too with `--vision`, which also overrides a `no frames` mark. `--no-vision` is the other direction, for a vision LLM you would rather send text to. The scripted pilot only reads the detection summary. A body that reads several cameras sends every frame each step, each one labelled with the camera's own name, on Claude, both OpenAI APIs, Gemini and any OpenAI compatible local server with `--vision` on. That costs what it sounds like, because the last two exchanges keep their images: two cameras is four pictures in every request rather than two, and up to eighteen on `--llm anthropic` with one of the Claude LLMs that bind their thinking (Opus 5.5, Fable 5.2, Sonnet 5.5, Haiku 5.5 and Fable 5.1), whose old frames are trimmed every eight exchanges rather than on every one. A local server or an LLM that takes one image per message needs a single `--camera-url`. Local setup, tool calling flags per server and what to expect from small LLMs: [docs/guides/local-llms.md](docs/guides/local-llms.md).

Over MCP there is no `--llm` at all. `roboglot serve-mcp` selects no LLM, and the chat client's own LLM is the pilot ([docs/guides/mcp.md](docs/guides/mcp.md)).

### Decision LLMs

**Decision LLMs are not in the pilots' table on purpose.** A decision LLM is not a provider and `--llm` does not take one: it answers typed questions about a state and writes nothing, so it cannot pilot a robot on its own. It sits in front of whichever provider you did pick, for the turns whose answer is a choice, it is named with `--decision-llm` instead, and it is off unless you name one ([docs/guides/decision-llms/README.md](docs/guides/decision-llms/README.md)).

There are seven, `jev` and `openai` hosted by their makers, `kev`, `openjev` and `opendecision` servers you run yourself, `local` for any other server that speaks the same wire format, and `laya` in Roboglot's own process. Try one in shadow first, where it is asked every turn and changes nothing, and the run's record says what it would have answered:

```bash
roboglot run arm-grip-check --robot lerobot:mock --llm openai --decision-llm jev --decision-mode shadow
```

Each one's key, extra, address and rate are in [docs/models/decision-llms.md](docs/models/decision-llms.md).

### Learned policies and VLAs

No vendor serves many VLAs per call the way OpenRouter serves many LLMs, so Roboglot's answer is Hugging Face: LeRobot's checkpoints on the Hub, served by Roboglot's own policy server, which reads each family's code before it serves it and refuses the rest before a byte of weights is fetched. It serves ACT, SmolVLA, Physical Intelligence's pi05 and pi0, X-VLA in the arm's own joints and NVIDIA's GR00T N1.7, and refuses pi0-FAST, whose policy runs its tokenizer's code from the Hub. The server runs in a process of its own, never in the one that owns the arm's serial bus: on the laptop, on a GPU you rent and tunnel to, or on a Hugging Face Inference Endpoint, a GPU that Roboglot starts for you and Hugging Face bills by the hour.

```bash
uv pip install "roboglot[lerobot-vla]"                                      # where the policy runs, Python 3.12
roboglot policy serve --policy OWNER/NAME@REVISION                          # on this machine, or on a GPU you rent
roboglot policy endpoint up arm --policy OWNER/NAME@REVISION                # or on a Hugging Face GPU, by the hour
roboglot run task.glot --robot arm-01 --llm openai --policy-url hf:arm      # the arm, its segments from the endpoint
```

The endpoint asks before it bills, waits until the server answers, pauses itself when it fails, and `roboglot policy endpoint pause arm` stops the bill. Roboglot has never created one: it has run against the test suite's stand-ins alone. What each family needs, its licence, where it runs and what is not served and why are in [docs/models/vlas.md](docs/models/vlas.md), and setting one up is [docs/guides/policies.md](docs/guides/policies.md).

<br>

## Architecture

Three loops, three rates, three owners. The LLM decides **what**, at 0.2 to 1 Hz. The steering loop decides **how to get there**, at 10 Hz, and never waits for the LLM. The robot's own controllers do the **moving**, at their own rate: balance on a biped, a pick policy on an arm, a gait policy on a humanoid, the driver on a wheeled base. The table with the rates and the owners is in [docs/concepts/architecture.md](docs/concepts/architecture.md).

The robot is an *adapter* that declares a *manifest*: what body it has, which intents and sensors, which verbs, what stops it. The registry, the tool list, the verbs a `.glot` may allow and the system prompt are built from that manifest when the robot connects. A verb that is not in it does not exist. All ten bodies go through the same loop, executor and contract ([ADR-0017](docs/adr/0017-robot-adapters-and-manifest.md)). Each adapter is also a distribution of its own, written in [`adapters/`](adapters/) here and installed beside the core as `roboglot_<name>`, so the only robot code on your machine is the robot you own. A team of pilots is that whole stack once per robot, side by side, with one bus between the pilots and one kill switch that reaches every executor.

```mermaid
flowchart LR
    HUMAN["Human<br/>goal in human language"]
    LLM["LLM<br/>Claude · OpenAI · Gemini · Grok · eight more cloud vendors · local (Ollama, vLLM, llama.cpp) · fake"]
    subgraph Roboglot
        LOOP["agent loop<br/>observe → think → enforce → act"]
        EXEC["safety executor<br/>allowlist · confirm gates · budgets · abort rules · heartbeat"]
        VERBS["verb registry<br/>built from the robot's manifest: core · the robot's own · aliases · learned (v2)"]
        PERC["perception<br/>frame → detections → “ball at bearing 18° left, ~0.6 m”"]
    end
    ADAPTER["robot adapter, a package of its own<br/>microduck · lerobot · rosbridge · open_duck · xlerobot · alohamini · toddlerbot · huebot · moss · rosarm<br/>installed beside the core and found through the roboglot.adapters entry point, which is how an adapter nobody here wrote is found too<br/>returns a manifest (embodiment, intents, sensors, verbs, limits, safety authority)<br/>sends intents, never motor writes<br/>backends: mock ✅ · real 🤖 one arm, two afternoons · jsonrpc, ws, zmq, bridge, cockpit 🧪 never run on a robot · rosarm's ws 📄 refused until somebody names a date"]
    ROBOT["Robot<br/>its own controllers: robotd at 50 Hz on a Microduck, the position controller and pick policy on an arm, the driver on a base"]
    MOCK["mocks<br/>an in-memory test double in every adapter's package, the Microduck's and the Huebot's being the core's scripted transport<br/>offline, for the tests and for trying Roboglot with no robot"]
    HUMAN --> LLM
    LLM -- "exactly one tool call per turn" --> LOOP
    LOOP --> EXEC --> VERBS --> ADAPTER
    ADAPTER -- "intents: twist, skill, gaze, sound, joint, pose, gripper" --> ROBOT
    ADAPTER --> MOCK
    ADAPTER -- "frame and state" --> PERC --> LOOP
    LOOP -- "observation: text and image" --> LLM
```

**Inside the adapter: four layers.** An intent from the diagram above passes down through four layers on its way to the robot, and state and frames come back up through them. The **body** is data, one per robot: its manifest, datasheet, verbs, limits, safety authority, rest pose and what it cannot do. Of the four layers it is the only one the LLM reads, beside the task and what the robot remembers, and a [described body](docs/adapters/status.md#described-bodies) is nothing else. A **behaviour family** is what bodies of a kind do alike: an arm folds before it lets go, and a biped's runtime is kept fed with twists while it walks. Its code is shared once two bodies need it, and not before: the Microduck and Huebot are one set of verbs and one transport under two body records, and every other body is a package of its own. A **binding** is how an intent reaches the robot, by one of three routes: an SDK Roboglot imports, a wire protocol it speaks, or a bridge it ships for the robot's own computer. The **transport** under that moves bytes and knows nothing about the body. So the next robot that speaks a protocol a package already speaks costs a body and not a whole adapter ([ADR-0075](docs/adr/0075-an-adapter-is-a-family-a-body-file-and-a-binding.md)).

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/rokbenko/quackd/main/docs/assets/architecture-dark.svg">
    <img src="https://raw.githubusercontent.com/rokbenko/quackd/main/docs/assets/architecture-light.svg" alt="Four stacked layers. Body: data, one per robot, the only layer the LLM reads. Behaviour family: arm, biped on a runtime, wheeled base, humanoid, own loop. Binding: import the SDK, speak its wire, or a bridge Roboglot ships. Transport: bytes only. An intent goes down through them, and state and frames come back up." width="880">
  </picture>
  <br>
  <sub><strong>Only the body layer is one per robot.</strong> Below it each robot sits in the box of its kind and the box of its route. Each robot is drawn where its row in the adapter catalogue puts it, by <a href="docs/assets/architecture.py">docs/assets/architecture.py</a>, so a new one joins the picture without anyone redrawing it.</sub>
</p>

**Why predefined skills matter.** The LLM never generates motor commands. Every verb is an *intent* the robot already understands: a velocity, a named skill (`kick_left` or `ground_pick` on the Microduck, `pick` as a LeRobot policy on the arm), a gaze target, a sound, a joint goal, a gripper command. The robot's own controllers do the physical part, on the Microduck policies trained in [microduck_rl](https://github.com/pollen-robotics/microduck_rl) and exported to ONNX at 50 Hz, so a slow or confused LLM degrades the *task*, never the *balance*. Where a body has a deadman it stops itself when commands stall. The Microduck's `robotd` has one, Huebot's shim is asked to keep the same, which nobody has seen it do, on the Open Duck and the ToddlerBot the daemon Roboglot ships is the deadman, the XLeRobot's and the AlohaMini's hosts stop the wheels but not the arms, and on the arm and a rosbridge base Roboglot's heartbeat and `stop` are the only stop authority. The LLM names the skill, the body performs it.

**Enforcement order.** Every verb call passes `Executor.run_verb`, which applies the contract in a fixed order: abort flag, allowlist, the pilot's feasibility verdict, parameter validation, budgets, `abort_when`, preconditions, and only then the confirm gate, so nobody is asked about a call a gate before it would refuse, then everything that can change while a person is asked read again on a new reading of the body's state, dry run, then execution with a timeout that races the abort, so a kill switch cancels the verb that is running. The preconditions are named by the manifest and supplied by the adapter, so a body's own rules are its own: not fallen on a duck, torque on and a cool servo for an arm, calibrated and not fallen on the humanoid. The full order and what each step means: [docs/concepts/safety.md](docs/concepts/safety.md).

**Prompts.** The system prompt opens with the robot's own one line introduction from its manifest, then the contract in prose, what the robot remembers from earlier runs, and the `.glot` body verbatim. Tools are JSON schemas generated from each verb's parameter model, plus `assess_task`, `declare_success` and `declare_failure`, plus `remember` when memory is on and `tell` when the run is a team of pilots, and the pilot LLM must return exactly one tool call. Only the last two observations keep their images, and up to the last nine on `--llm anthropic` with one of the Claude LLMs that bind their thinking (Opus 5.5, Fable 5.2, Sonnet 5.5, Haiku 5.5 and Fable 5.1), whose old frames are trimmed every eight exchanges rather than on every one. Local LLMs get one extra line describing the JSON shape to answer with when native tool calling is unavailable. The system prompt and the tools that are not verbs are in [`roboglot/agent/prompts.py`](roboglot/agent/prompts.py).

**An optional stepper in front of the pilot LLM.** `--decision-llm` lets a decision LLM take the turns whose answer is a choice among calls this body already has. It is a different kind of LLM rather than a cheaper one of the same kind: it emits no tokens, so where a pilot LLM writes you a verb and Roboglot parses it, a decision LLM scores the verbs you gave it and hands back which one with a probability for each, and there is nowhere in that answer for a number to come from. [TypeSafe's Jev](https://docs.typesafe.ai/introduction) was the first and gave the wire format its name ([docs/guides/decision-llms/jev.md](docs/guides/decision-llms/jev.md)), and what most of the others share with it is that format rather than a vendor, so each is a row of data with a page of its own, and `--decision-llm local --decision-url` reaches anything else that answers `POST /v1/systemone`. OpenAI's Decisions API asks the same kind of question in a format of its own, `POST /v1/decisions`, so `--decision-llm openai` has a client of its own that translates it ([docs/guides/decision-llms/openai.md](docs/guides/decision-llms/openai.md)). The stepper sits inside *think* and nowhere else: no adapter knows about it, the executor is unchanged, and which verbs it may answer is computed from each tool's own JSON schema, so a verb with a number in it is never one of them. It is off unless a run names one, and a turn it answers never enters the pilot LLM's history, because none of it is anything the pilot LLM said. [docs/guides/decision-llms/README.md](docs/guides/decision-llms/README.md) and [ADR-0040](docs/adr/0040-a-discrete-stepper-in-front-of-the-pilot-llm.md). A decision LLM that can see has one more place, inside one verb rather than in front of the pilot LLM: on a Microduck, `--decision-frames` gives the pilot `watch`, which asks it where a thing the pilot described is in each camera frame, and turns the head by Roboglot's own arithmetic, so the decision LLM says where the thing is and never how far to turn ([ADR-0054](docs/adr/0054-a-reflex-may-look-through-a-decision-llm.md)).

**Perception: features, not frames.** The default detector is an HSV colour threshold, a few milliseconds per frame, no model download. Bearing comes from horizontal position through the camera's focal length. Distance comes from apparent size, so `--fov-deg` matters on a real camera. It looks for one orange ball, in the orange the mocks that draw a ball paint it, so it works on them out of the box. For a real ball you tune one HSV range ([FAQ](docs/faq.md)). A YOLO detector is an optional extra, in this process with `--detector yolo` or on a Jetson's GPU with `--detector host`, and a real body run with `--host` uses the board's by default when that board can detect.

**Talking to the robots.** Each adapter speaks its body's own protocol and spells every upstream name in one `upstream_api.py`, tagged VERIFIED (read from upstream source at a pinned commit) or UNVERIFIED, and a test proves the unverified ones are only reachable from the experimental backends. Two bodies are reached through an installed SDK (the arm through LeRobot, the base through roslibpy), two by speaking the ZeroMQ host they already ship because neither is an installable package (the XLeRobot and the AlohaMini), and two through a daemon Roboglot ships for the robot because neither runtime has a network API at all (the Open Duck Mini and the ToddlerBot). The Microduck's `robotd` speaks JSON RPC 2.0 over a unix socket, and Roboglot re-sends `robot.move` every 100 ms while walking on purpose, because the robot zeroes its velocity when those stop. Huebot's own API is closed, so its maker is writing a shim for it that is to answer that same protocol. Each body's page under [docs/adapters/](docs/adapters/) carries its VERIFIED and UNVERIFIED tables, and the traps that recur when you read a robot you cannot run are collected in [docs/adapters/reading-robots.md](docs/adapters/reading-robots.md).

**Safety layer.** Heartbeat failure, Ctrl+C and `q` all mean the same thing: `stop`, then abort. A verb that times out or raises stops the robot and comes back as a failed result, not an abort. `--dry-run` sends nothing. And `stop` always means stop, never collapse, on every body: Roboglot sends no robot's go limp call, ever. Session end is different on the arm, where LeRobot's own `disconnect()` releases torque by its default, which is what dropped the arm at the end of every run on the bench. So an arm with a [rest pose](#your-robots-by-name) recorded is driven back to it between the stop and the disconnect, on every exit path there is, and when it cannot get there Roboglot leaves torque on and says so rather than letting the arm fall. What actually stops each body when Roboglot goes quiet differs enough to be worth a table of its own, and each manifest declares its own answer in `safety_authority`: [docs/concepts/safety.md](docs/concepts/safety.md).

The full map, with a "why it exists" line per module: [docs/concepts/architecture.md](docs/concepts/architecture.md). Decisions and their reasons: [docs/adr/](docs/adr/).

<br>

## Installation

Requirements: Python 3.11 or newer and [`uv`](https://docs.astral.sh/uv/). Windows, macOS and Linux. No GPU needed: Roboglot's core touches none. Every Roboglot command but one runs on your laptop and reaches an NVIDIA Jetson's LLM server, camera and detector over the network with `--host` ([docs/guides/jetson.md](docs/guides/jetson.md)). The one that runs on a robot's own computer is `roboglot onboard`, [Robot Passport](#robot-passport)'s service, which can drive the robot from there as well, and a Jetson is its first board, though nothing of it has run on one yet. The core is about 120 MB and it is the loop, the executor and the contract, with no robot in it.

**`uv pip install roboglot` installs no robot.** You choose the body next, and each of the ten is its own package on PyPI (`roboglot-microduck`, `roboglot-lerobot` and eight more) that the extra of the same name pulls in. Until one of them is installed, every command that needs a body refuses and says what to install.

```bash
uvx roboglot --version                                   # the core on its own: the loop, the executor, the contract
uv pip install "roboglot[microduck]"                     # then a body: or lerobot, rosbridge, open_duck, xlerobot, alohamini, toddlerbot, huebot, moss, rosarm
uv pip install "roboglot[robots]"                        # or all ten at once, each with the SDK its real backend needs
uv pip install "roboglot[microduck-camera]"              # the duck plus its WebRTC camera
uv pip install "roboglot[lerobot-vla]"                   # the arm's policy server: LeRobot, torch and transformers, Python 3.12
uv pip install "roboglot[ui]"                            # the page in a browser or on a phone, roboglot ui: Streamlit
uv tool install "roboglot[onboard]"                      # on a robot's own computer: roboglot onboard, Robot Passport, with --python 3.12 on JetPack 6
uv pip install "roboglot[anthropic]"                     # the brain: or openai, gemini, grok, mistral, deepseek, cohere, qwen, kimi, glm, meta, openrouter, all
git clone https://github.com/rokbenko/quackd && cd Roboglot && uv sync   # contributors: the core and all ten adapters, editable
```

The extras are independent and they compose, so a body and a brain are one install (`uv pip install "roboglot[microduck,anthropic]"`) or none at all (`uvx --from "roboglot[microduck,anthropic]" roboglot run ...`). `roboglot[lerobot]` installs anywhere and reaches a real arm only on Python 3.12 or newer, because LeRobot itself does: below that floor the marker resolves to no SDK and you are left with `lerobot:mock`, which is why `roboglot doctor` is where you check rather than the install output. `roboglot[lerobot-vla]` is the arm's policy server, `roboglot policy serve`, which needs LeRobot and Python 3.12 and belongs wherever the policy runs rather than in the process that drives the arm ([docs/guides/policies.md](docs/guides/policies.md)). And `roboglot[yolo]`, `roboglot[lan]` and `roboglot[ui]` are the other detector, LAN discovery and the page `roboglot ui` serves. `roboglot[decision]` is the System One client for the optional discrete stepper and `roboglot[laya]` is the one that runs in this process instead of behind a server. Both are off unless a run names a decision LLM, and neither is part of `roboglot[all]`, deliberately, because a stepper nobody asked for should never be installed by asking for everything. `--decision-llm openai` needs neither, because its client is the `openai` SDK the pilot already uses ([docs/guides/decision-llms/README.md](docs/guides/decision-llms/README.md)). `roboglot[onboard]` goes on a robot's own computer, and on a laptop for the `sim` board and its demo: `roboglot onboard` with zeroconf, an OpenAI-compatible client for the robot's brain and, on Linux alone, the Bluetooth libraries, and it is not part of `roboglot[all]` either. Which body a command means when you do not name one is in [Configuration](#configuration), and `roboglot doctor` says what this machine has.

**What a version promises.** The eleven packages always ship together, with one version. While Roboglot is 0.x, a patch, the third number, fixes what Roboglot did not do the way its docs or its own output said, and asks nothing of a setup that worked, except where a safety fix refuses something the docs never promised, 