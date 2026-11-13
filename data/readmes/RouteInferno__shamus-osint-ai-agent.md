<p align="center"><img src="docs/hero.png" alt="shamus, an OSINT agent that lives in your terminal. A PowerShell window where the agent plans, calls whois, dns and archive, and notes to itself what to do next." width="100%"></p>

<h1 align="center">shamus: OSINT AI agent for the terminal</h1>
<p align="center"><b>An OSINT agent that lives in your terminal.</b><br>One command. It picks the tools, runs them, and writes the case file.</p>
<p align="center"><sub>OSINT · OSINT tool · AI agent · CLI · terminal · LLM · reconnaissance · investigation · windows</sub></p>

> **Status: v1.4.0.** The app is out — [download Shamus for Windows](https://awesomeosint.tools/shamus/).

## Why this exists

Sometimes you do not need a window — you need an answer, in the terminal, next to the rest of your tools.

## Why it is different

Web tools want your browser. Shamus lives where the work is: one command, it picks the tools, runs them and writes the case file. Pipe it, script it, schedule it.


## The idea

- **One object.** The cursor: a cyan block that waits for you.
- **One number.** How many tools ship with it: twelve.
- **Colour.** Terminal black `#08090A` and grey-white. Cyan `#6FE0FF` marks what the agent does and what it asks, and the download.
- **The main feature.** It is an agent, not a script: it reads each tool's output, decides the next step itself, and stops to ask before it widens the search.
- **The frame.** The page is a man page: one monospace face, section names hanging on the left (Name, Synopsis, Description, Tools, Examples, Files).

![The Tools section as a two-column table of twelve tools, then the Examples that run in the terminal](docs/features.png)

## The demo on the page

The command types itself into a PowerShell window. The agent prints a plan, calls tools one by one and writes a short note to itself between calls. Then it asks a question with `(Y/n)` and waits: the visitor answers with the keys on screen or on the keyboard, and either answer ends the sample and shows the download. The three commands under Examples replay the terminal with other questions.

![The visitor answered Y: the sample session stops here, say yes in your own terminal](docs/cliffhanger.png)

