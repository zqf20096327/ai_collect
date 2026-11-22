<p align="center">
  <img src="thumbnail/thumbnail.jpg" alt="Milan Forwarding: everyone builds agents, we made it simple" width="100%">
</p>

# Milan Forwarding

**An AI forwarder that runs an air export desk on its own.** Giulia reads every request, prices it across airlines,
the rate portal and the rate sheets, quotes in plain words, books on the customer's yes and tells them where their
freight is. Day and night, in under a minute.

[![START Hack Munich 2026](https://img.shields.io/badge/START_Hack-Munich_2026-111111)](https://www.start-hack.com)
[![5U AI challenge](https://img.shields.io/badge/5U_AI-Build_the_Forwarder-2f6fed)](docs/challenges/5u.md)
[![Leaderboard](https://img.shields.io/badge/5U_leaderboard-%231_of_15-15884a)](#a-night-in-numbers)
[![Built in 24 hours](https://img.shields.io/badge/built_in-24_hours-b9690a)](#team)
[![Live](https://img.shields.io/badge/live-hackathon.noesisai.it-141414)](https://hackathon.noesisai.it)
<br>
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-18-61DAFB?logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-Responses_API-412991?logo=openai&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Cloudflare](https://img.shields.io/badge/Cloudflare-Tunnel-F38020?logo=cloudflare&logoColor=white)

**Try it now:** [hackathon.noesisai.it](https://hackathon.noesisai.it). We share the sign-in with the jury.

---

## The problem

An air export quote still means an inbox, a rate portal, ten spreadsheets and phone calls to truckers. A forwarder
answers in hours. The customer decides in minutes, and books with whoever answered first and cheapest. Most of that
work is reading, comparing and writing. That is what Giulia does.

## What Milan Forwarding does

- **Answers every request.** Mail in any language, with a packing list in a PDF, a scan, a spreadsheet or a voice
  message. Giulia asks only for what is really missing, and only once.
- **Finds the best price.** Every airline on the lane, the rate portal, this month's rate sheets and the local
  truckers, compared on price and speed. The next weight break is priced too, so 299 kg never costs more than 300.
- **Quotes like a person.** One clear option and one all-in total, written warmly in the customer's language.
- **Books and follows up.** On the customer's yes, by portal or by mail to the airline. If the price changed, the
  customer hears it in the confirmation, not on the invoice. Tracking questions get an answer from our own record.
- **Catches what humans miss.** Dangerous goods hidden in a packing list, a mail that contradicts its attachment, an
  impostor asking to move a customer's offer elsewhere.
- **Keeps people in charge.** The desk shows every shipment, what Giulia flagged and why, and every step she took.
  Anyone can step into a shipment with one sentence, and she follows.

## The desk

| | |
| --- | --- |
| **Desk** | What Giulia flagged, open quotes to chase, today at a glance |
| **Shipments and customers** | Every request with its mails, options and booking; what each customer prefers |
| **Network** | The airlines, routes and truckers we work with, and where only one airline flies |
| **Efficiency** | Answer rate and speed, booked value, margin, and the charts you keep |
| **Ask** | Question your business in plain words, get the answer and the chart, keep it on your dashboard |
| **Sessions** | Each shipment's live agent session: mails, tool calls, priced options, booking |
| **Voice** | The desk on your phone: ask out loud, say yes to pass it on |

## A night in numbers

From the live 5U challenge, Saturday 16:00 to Sunday noon, all from our own register:

- **#1 of 15 teams** on 5U's leaderboard after 199 rounds.
- **208 requests**, 86 % quoted, typically **45 seconds** after the mail arrived.
- **159 bookings**, 89 % of the quotes. More than €500,000 in booked freight.
- **$0.002 of AI per booking.** The whole night cost $0.35.

## How it thinks

Everyone builds agents. We made it simple.

- **The model decides, the system guarantees.** The model reads, judges and writes. Every price, total, date and
  recipient comes from code. A number in a mail that no tool computed would be a bug.
- **One agent, one conversation per shipment.** Quote, booking and tracking are one life. Every new mail resumes
  it with everything that came before.
- **Intelligence in the agent, guarantees in the tools.** A new capability is a tool the agent can choose, never a
  rule bolted in front of it. No keyword tables, no caps on steps or tokens: one stop if it ever goes round in circles.
- **Prompts give reasons, not procedures.** A model that knows why applies it to the case nobody wrote down.
- **Measure, then decide.** We read every round in full and changed the kind of mistake, never the single mail.

The full reasoning, with the rounds that taught us each decision: [vision.md](vision.md).

## Run it

**Online.** [hackathon.noesisai.it](https://hackathon.noesisai.it). Ask us for the sign-in.

**Locally.**

```sh
cp .env.example .env              # an OpenAI key; the 5U team key only for the live challenge
make install                      # backend (uv) and frontend (npm)
make test                         # pricing rules and whole deals against a local copy of 5U
make sim                          # realistic mails, a real model, a local 5U: nothing leaves your machine
make build && make api            # the desk on http://localhost:8000
```

**On a server.** One container runs the agent, the API and the desk. The data lives on a volume.

```sh
docker compose up -d --build                     # http://<server>:8000
make account USERNAME=you NAME="Your Name"       # the first account closes the desk to everyone else
deploy/tunnel.sh setup && deploy/tunnel.sh route # optional: a public address through Cloudflare, no open port
docker compose --profile public up -d
```

Details in [docs/deploy.md](docs/deploy.md).

## Inside

| Path | What it is |
| --- | --- |
| `backend/app/agent.py`, `tools.py` | Giulia: one session per thread, and the tools she works with |
| `backend/app/forwarder.py` | The system under her: mail, carriers, tariffs, bookings, the offer engine |
| `backend/app/pricing.py` | Every number a customer reads |
| `backend/app/prompts/` | Who she is and what a good answer is, with the reasons |
| `backend/app/desk.py`, `charts.py`, `economics.py` | The desk's assistant, its charts and the money |
| `frontend/` | The desk (React, TypeScript) |
| `docs/` | The 5U challenge, counted facts from the night, deployment |
| `vision.md`, `AGENTS.md` | How we think, and how to work on the code |

## Team

**START Milan.** Built in 24 hours at START Hack Munich 2026, TUM, 21 and 22 November, for 5U AI's challenge
"Build the Forwarder".

- **Jan Köberle**
- **Mattia Beltrami**
- **Sam Sonntag**
