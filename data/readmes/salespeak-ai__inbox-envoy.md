# Inbox Envoy

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.1.0--beta.4-blue)](CHANGELOG.md)
[![Status](https://img.shields.io/badge/status-public%20beta-orange)](COMPATIBILITY.md)

**Your AI agent handles the pitches. You see what matters.**

![Claude Code running Inbox Envoy on a practice inbox of eight made-up emails](.github/media/observe-run.gif)

<sub>Claude Code 2.1.202 running Inbox Envoy v0.1.0-beta.3 on Nov 17, 2026, sorting eight made-up emails. Nothing was connected, changed or sent. One of the eight tries to give the agent orders; it gets flagged, not obeyed.</sub>

An open, portable skill that teaches an existing personal agent to protect your inbox, organize mail, highlight opportunities, and, with separate permission, investigate an uncertain unsolicited offer. When possible it researches public company documentation or published company agents (PAP, A2A, MCP); where evidence is insufficient it can prepare or, on appropriately isolated hosts, conduct a limited screening conversation.

This is **a skill, not an email provider, separate inbox, continuous-monitoring service, or new mailbox connector**. The personal agent must already have the necessary mail tools and scheduling capability. Installation by itself never grants access or enables sending.

## Get started

Inbox Envoy is designed for intelligent personal agents that can load a skill (a folder with `SKILL.md` plus reference files) and that already have authorized access to your mailbox.

1. **Download** [`skill.zip`](https://github.com/salespeak-ai/inbox-envoy/releases/download/v0.1.0-beta.4/skill.zip) from the [`v0.1.0-beta.4` prerelease](https://github.com/salespeak-ai/inbox-envoy/releases/tag/v0.1.0-beta.4) (all releases: [Releases](https://github.com/salespeak-ai/inbox-envoy/releases)). Check the SHA-256 in the release notes. The archive contains one folder, `inbox-envoy/`, with `SKILL.md` at its root.
2. **Give it to your agent** using that agent's own skill or custom-instruction import. Hosts that load skills from a folder on disk usually want the unzipped `inbox-envoy/` folder in their skills directory. Exact steps vary by host. See [`COMPATIBILITY.md`](COMPATIBILITY.md) for the required host capabilities and safe modes.
3. **Paste this to your agent:**

   > Install the Inbox Envoy skill from the attached ZIP or this repository using your supported skill workflow. Read `SKILL.md`. Check your actual mailbox, scheduler, state, and research capabilities, then walk me through onboarding. Start in Observe with no mailbox changes and no external contact. Show the operational readiness report. Do not schedule or change anything until I approve.

4. **Expect a read-only start.** The agent should explain its modes, show what it can actually do, preview a few classifications, and ask before any label, schedule, research or outbound step. If it claims capabilities it has not verified, stop and ask it to check. Full first-run expectations are in [`INSTALL.md`](INSTALL.md).

### Other install routes

- **Skills CLI** (any agent it supports): `npx skills add salespeak-ai/inbox-envoy`
- **Claude Code plugin marketplace:** `/plugin marketplace add salespeak-ai/inbox-envoy`, then `/plugin install inbox-envoy@inbox-envoy`
- **Try it without your mailbox:** point your agent at [`examples/test-inbox/`](examples/test-inbox/), nine made-up emails with a separate answer key.

Both install the same `SKILL.md` and references. Installing still grants no mailbox access and enables nothing; onboarding starts in Observe.

## Who maintains this

Inbox Envoy is maintained by [Salespeak](https://salespeak.ai). Salespeak also sells company-side AI products, including AI agents that answer buyer questions for vendors. Inbox Envoy is independent of those products:

- **No Salespeak service required.** The skill runs entirely inside your own personal agent. It contains no Salespeak endpoint, account, API key or hosted backend.
- **No buyer-private data goes to Salespeak.** The skill and the reference client send no telemetry, analytics or callbacks to Salespeak or anyone else. Your host agent, model provider and mail provider still process data under their own policies.
- **Optional guidance link in screening emails.** If you separately enable sender screening, you can choose to add a link to a general guidance page on salespeak.ai to the first evidence request. It is off unless you turn it on. The link carries no per-user tracking code and contains nothing about you. Inbox Envoy attribution is off unless you opt in.
- **No preferential treatment.** A company that uses Salespeak, or publishes any agent at all, gets no boost in relevance, classification or screening. Company-agent answers are treated as unverified seller claims, the same as any other seller source.

skills.sh still shows a Snyk "Fail" from its Nov 13 scan. The one real finding, a salespeak.ai link that was on by default in screening emails, has been off by default since v0.1.0-beta.3, and the other two flags say the skill reads your email and proposes a schedule you approve, which is the job.

You can check these by reading the package: it is plain instructions plus a small standard-library Python reference client with no default destination.

## Privacy

Salespeak receives no data from Inbox Envoy, and the package retains nothing outside your host. What leaves your agent, and when: [`PRIVACY.md`](PRIVACY.md).

Why a company that serves sellers maintains a buyer-side tool: [Salespeak for buyers](https://salespeak.ai/for-buyers/).

## First release: buyer-side skill and optional conversations

This public beta is distributed through the user's existing personal agent. It includes the complete core skill, installation/host templates, a research-first opportunity workflow, and a **restricted local agent-to-agent reference client**. The reference client is runnable against a controlled test company agent; it is **not a shipping autonomous connector to arbitrary live PAP/A2A/MCP endpoints**. Real interactive sessions remain off until a host can demonstrate isolation and a compatible, approved endpoint. See `references/agent-exchange.md`, `adapter/README.md`, and `SECURITY.md`.

## Installation and first use (detail)

1. Review the files in this package, especially `SKILL.md`, `references/screening.md`, `references/discovery.md`, `references/feedback.md`, `references/autonomy.md`, `references/faq.md`, and `references/test-cases.md`.
2. Install or copy the skill into your personal agent's supported skill location using that host's normal instructions; exact steps vary by agent.
3. Ask your agent: **"Set up Inbox Envoy in read-only mode. Show me which mailbox permissions, scheduling, and label/folder actions you can actually perform. Do not change or send any email yet."**
4. The agent should explain three visible steps: **Observe** (preview only), **Label-only** (approved labels, no archiving), and **Archive** (approved high-confidence noise only, reversible). It must state your current mode and request separate consent for each transition. **It should also introduce Opportunity Research in ordinary language and ask whether you want it off, search-only, or allowed to read verified public company pages. You do not need to open or fill `opportunity-research.md`.** Review sample classifications before approving labels.
5. Review the **operational readiness report**: by default, ask for a dedicated 30-minute, seven-day triage schedule, a separate slower investigation queue, and a daily digest. Approve the schedule before the host creates it, and have the host verify the resulting task. A once-a-day weekday digest is not the default protection schedule.
6. If you want sender conversations, separately enable them. Start with public research or draft-only screening. Autonomous sending requires enforceable host permissions, strict disclosure controls, limits, auditability, and revocation. No host capability means no autonomous promise.

## How Envoy becomes more helpful without taking control away

**You do not have to discover or manage modes yourself.** At setup, your agent should explain the options and identify the current, verified mode. Later, an agreed review should show evidence and offer a next step. **It never upgrades itself.**

| Stage | What happens | When to consider the next stage |
| --- | --- | --- |
| **Observe** (default) | Preview classifications; no mailbox changes | Review a representative sample after roughly 3-5 days or enough real examples; then optionally approve labeling |
| **Label-only** | Adds approved Envoy labels; all mail stays in Inbox | After roughly 5-7 days or enough user-reviewed cases, evaluate errors and recovery before proposing archive of specific safe categories |
| **Archive** | Archives only separately approved high-confidence irrelevant categories; searchable and reversible | Stay here indefinitely; no requirement to enable sending |

**Sender investigation is optional, not stage four.** Public research (when permitted), reviewed email drafts, and autonomous outbound messages have distinct permissions. Sending never turns on because you approved archiving. The host must enforce privacy restrictions before autonomous sending is available.

Every digest should show the actual state, e.g. `Label-only | Triage every 30 min (verified) | Research: search-only | Agent conversations: off | Sender email: off | Archive: off | Next: accuracy review`. A review should show actual sample counts, confirmed mistakes, blind spots, and exactly what is proposed. No fixed day count or absence of complaints proves safety. If not ready, the agent should say so and keep the existing mode. You can always say "stay label-only", "stop archiving", "what mode am I in?", or "turn off Envoy".

See [`references/autonomy.md`](references/autonomy.md) for transition and rollback details.

## Organization in your existing mailbox

With permission the agent creates these nested Gmail labels or equivalent Outlook folders where supported:

| Label/folder | Meaning | Inbox treatment |
| --- | --- | --- |
| `Envoy/Important` | Obligations, replies and high-priority messages | Keep visible, highlight |
| `Envoy/Opportunities` | Promising unsolicited offers or introductions | Keep visible, highlight separately |
| `Envoy/Review` | Ambiguous messages | Keep visible, ask/review |
| `Envoy/Screening` | Offers currently being investigated | Keep visible pending outcome |
| `Envoy/Filtered` | High-confidence irrelevant outreach | Archive only after calibration and separate permission |

No permanent deletion. No automatic Trash. If labels cannot be created, classification and digest still work when the host supports reading mail. Recovery: search the `Envoy/Filtered` label and move a message back into your Inbox. Moving a message back should be treated as a possible correction, and never immediately re-archived. Manual changes to Envoy labels can become feedback when the host supports persistent label reconciliation; it must not pretend to see mailbox label-event history it does not have.

## Before you grant access: the five biggest trust questions

**Will it read private email?** Yes, to classify messages it may need access to message content in the mailboxes you authorize. Your host's provider and model data policies still apply. Review those policies before connecting a mailbox; Envoy does not itself guarantee local-only processing or no training.

**Could it hide something important?** Yes, any classifier can make mistakes. Envoy begins read-only, keeps important/uncertain/opportunity messages visible, and only archives calibrated high-confidence noise with separate approval. No permanent deletion or automatic Trash.

**Will it send email to strangers?** Not from installation. Sending and agent-to-agent conversations require separate permission; research-only is available, and draft-only is the fallback where safe autonomous sending cannot be enforced.

**Will it reveal what it knows about me?** Envoy prohibits any unauthorized disclosure of private context. Nevertheless, a sender can infer that an address is attended from receiving a response, and no prompt by itself can guarantee privacy. Never enable autonomous external dialogue without enforceable isolation and output controls.

**How do I take control back?** Ask for an inventory of active tasks, mailbox permissions, storage and prior actions. Stop scheduled tasks, revoke connector access if needed, recover any archived messages from `Envoy/Filtered`, and request removal of locally stored Envoy state. Simply uninstalling the instructions may not cancel existing tasks.

### More questions worth asking before installation

| Concern | What to verify |
| --- | --- |
| Who processes and stores my email? | Host/model/email provider policies, logging, retention, training settings and subprocessors |
| Do I have to supply a password? | No password to this skill; use the host/provider's official authorization flow |
| Can my employer or delegates see these actions? | Work-account policies, shared mailbox permissions and administrative logs |
| Will it modify my rules and existing folders? | Approved `Envoy/` labels only; no unrelated rule changes |
| Can an email manipulate the agent? | Untrusted-content handling and host-enforced tool restrictions; retain provider spam/phishing protection |
| Can it create surprise charges? | Host background-task, token, tool and provider API costs and rate limits |
| How often does it actually run? | Scheduler-confirmed frequency, timezone, last successful run and fallback mode |
| How do I teach it or reverse a mistake? | Chat corrections; label reconciliation where supported; reversible archives; no global rule from one correction |
| Does the skill track me or favor its publisher? | No required publisher telemetry or pay-to-pass path; audit host connections and installed package |
| Will it work with my agent? | Verified host capabilities rather than generic compatibility claims |

**Read the full answers:** [`references/faq.md`](references/faq.md). The FAQ is also part of the skill instructions, so the installed agent should answer questions using its *actual* configured permissions and schedules, not generic assurances.

## Evidence before interruption

**Inbox Envoy investigates unfamiliar opportunities before deciding whether they deserve your attention.** During onboarding the agent should explain that feature and ask you to enable it, offering search-only, permitted safe public-page research, or off. The `opportunity-research.md` file is for the agent, not a form or configuration file for you. Authorized public research and claim checking are part of normal triage, even if you never authorize the skill to archive mail or contact a sender. The host may use search and safely accessed public documents to understand what a company offers and distinguish verifiable evidence from seller claims. No company must install an agent to benefit.

Reading a published PAP/A2A agent description is not the same as talking to that agent. **Live company-agent conversations are disabled unless the host can demonstrate separate execution isolation, restricted network egress, safe untrusted-response handling and your specific consent.** Reviewing an outgoing draft by itself is not sufficient. Email screening is a separate opt-in and remains disabled by default. See [`references/opportunity-research.md`](references/opportunity-research.md) and the FAQ.

## Safety and implementation notes

No arbitrary link-clicking or remote instructions. Public agent discovery is restricted to verified domains, and only when host security controls allow it. Private relevance evaluation is separate from external interaction. No automatic seller responses, calendar booking, terms acceptance, subscriptions, private disclosure or vendor preference. Do not advertise any capability that a particular host cannot enforce.

<!-- BEGIN D1-D2A 2026-11-06 -->
## Agent-screened email and optional signature

Inbox Envoy is a portable skill for personal agents that can load skill instructions or equivalent custom instructions and have an authorized mailbox connection. Host-specific tools, security isolation and scheduling determine available actions. Start read-only; autonomous sender contact requires separately verified safeguards and permission, otherwise use draft-only.

After separately opting in to sender screening, an agent can request an offer summary, intended audience and one supporting public URL (or an explicit statement that none is available). A general guidance link is **off by default** and can be turned on separately. Inbox Envoy attribution in screening emails is **off by default**, separately optional and shown only on the first request. No preapproved customized active sender template may be changed without reapproval. See [`references/screening-d2a.md`](references/screening-d2a.md).

Users may **manually** add an optional, unbranded signature line; the skill never edits signatures. See [`templates/optional-signature.md`](templates/optional-signature.md). Public sender guidance: [salespeak.ai/agent-screened-email](https://salespeak.ai/agent-screened-email/).
<!-- END D1-D2A 2026-11-06 -->

## Beta status and open verification items

This is a public beta. Open items, tracked transparently:

- **Personal-agent portability:** the skill works with instruction-capable personal agents; available mailbox, scheduling, and sending actions depend on each host’s permissions and verified safeguards. See [`COMPATIBILITY.md`](COMPATIBILITY.md).
- **Live company-agent conversations:** disabled. The local Docker isolation demo passes, but no session with a real consenting company endpoint has been run. The local fixture is a developer demo, not a production protocol integration.

Maintainer and release process docs live in [`docs/maintainers/`](docs/maintainers/). Report vulnerabilities privately through [GitHub private vulnerability reporting](https://github.com/salespeak-ai/inbox-envoy/security/advisories/new), never in public issues (see [`SECURITY.md`](SECURITY.md)).

## License

MIT, copyright Salespeak. See [`LICENSE`](LICENSE).
