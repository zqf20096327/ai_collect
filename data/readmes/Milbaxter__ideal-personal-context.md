# How to create ideal personal context for personalized AI use

| Platform / provider | Examples of data it may hold about you | Possible value for your personal context |
| --- | --- | --- |
| [Google](https://policies.google.com/privacy) | Searches, Gmail messages, Drive documents, photos, contacts, calendar events, and location-related activity, depending on the services and settings you use. | Questions you explore, documents you work on, plans, and personal history. |
| [YouTube (Google)](https://policies.google.com/technologies/product-privacy?hl=en-US) | Watch and search history, subscriptions, playlists, comments, and your uploaded videos. | Topics you return to, things you are learning, and work you have published. |
| [Facebook (Meta)](https://www.facebook.com/help/windows-desktop/506794473544588/) | Profile information, posts, photos, friends and connections, group activity, reactions, and ad-related information. | Life events, communities, connections, and interests you have expressed. |
| [Instagram (Meta)](https://privacycenter.instagram.com/policy/) | Profile information, photos, videos, comments, likes, saved content, follows, and interactions with content and ads. | Creative work, visual interests, and things you choose to follow or save. |
| [Spotify](https://support.spotify.com/is-en/article/understanding-your-data/) | Listening history, playlists, saved tracks, podcast plays, timestamps, skips, and device information. | Musical tastes, recurring listening habits, and subjects you explore through podcasts. |
| [ChatGPT (OpenAI)](https://help.openai.com/en/articles/7260999-how-do-i-export-my-chatgpt-history-and-data) | Saved conversations and account information included in available data exports. | Problems, ideas, goals, and preferences you have already explained to an assistant. |
| [Claude (Anthropic)](https://support.claude.com/en/articles/9450526-export-your-claude-data) | Conversation history and account information. | Writing, reasoning, project discussions, and decisions you have worked through. |
| [Gemini (Google)](https://support.google.com/gemini/answer/16920332?hl=en) | Available chat activity, uploads, generated media, and Gems data. | Questions, creative work, and ongoing projects discussed with Gemini. |
| [Telegram](https://telegram.org/blog/export-and-more) | Cloud chat history and shared photos, videos, and files available through its export tools. | Agreed conversation context, shared projects, and commitments—with participants’ consent. |
| [WhatsApp (Meta)](https://www.whatsapp.com/legal/privacy-policy) | Account and service information; ordinary delivered personal messages generally live on your devices, rather than being retained on WhatsApp’s servers. | Your own chat exports can add agreed plans and commitments—with participants’ consent. |

*Examples, not a complete inventory or a promise that everything is exportable. Coverage depends on your usage, settings, retention, and account type. The context column suggests potential uses, not conclusions a platform has established about you.*

**Bring your digital life together into a private, living personal wiki—and use it to give AI a deeper understanding of you.**

Your context is scattered everywhere. Google knows parts of your interests. Spotify knows your listening history. Your notes contain unfinished ideas. Your blog records what you have thought about. Your AI conversations contain questions, plans, and problems you have already spent hours explaining.

What if you could bring those pieces together, make sense of them with an intelligent local AI, and own the resulting knowledge base?

This repository is an open-source idea to explore and build upon. It describes a direction, not a prescribed implementation or a finished product.

## The big picture

**Your data → local AI → your personal wiki → context for your agents.**

Collect the history you can access from the platforms you use. Bring in your own writing, media, notes, and conversations. Have a capable AI running locally turn that collection into a coherent, interconnected knowledge base: a personal Wikipedia that grows and changes with you.

The wiki becomes a foundation you can build on. Instead of starting from zero with every new agent, you can give it relevant context about your projects, preferences, goals, background, and ways of thinking.

## What could go into it?

- **Platform data:** the information you can export from Facebook, Instagram and other Meta services, Google, YouTube, Spotify, and elsewhere—activity, interests, saved items, playlists, and your own contributions.
- **AI conversations:** your accessible history with ChatGPT/OpenAI, Claude/Anthropic, Gemini, and other assistants. These conversations contain a rich record of what you have been exploring and trying to do.
- **Your public work:** blog posts, essays, newsletters, YouTube videos, podcasts, talks, social posts, and projects. The things you have made and shared with the world.
- **Your private notes:** saved ideas, journals, drafts, reading notes, highlights, plans, and documents.
- **Conversations with people:** relevant WhatsApp and Telegram chats, **if the friends and other participants involved agree** to the intended use.

The ambition is broad coverage of your digital life. In practice, exports are incomplete and availability varies. You choose what belongs; collecting everything is not a prerequisite for getting value.

## From an archive to understanding

A pile of exported files is hard to use. The interesting step is letting AI connect them into something navigable and useful.

An idea in an old note might connect to a current project. A conversation might explain why you made a decision. Several pieces of writing might reveal a recurring question. Your goals may have changed, and the wiki could preserve that evolution rather than flattening your history into a static profile.

The inspiration is [Andrej Karpathy's LLM Wiki idea](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): use an LLM to build and maintain a persistent, interlinked wiki over source material. Here, the focus is your personal context. This project is independent and not endorsed by Karpathy.

The result should remain grounded in its sources and open to correction. Your own statements, an AI's suggestions, and inferred patterns are different kinds of evidence. A watched video is not necessarily a belief; an old goal is not necessarily your current one.

## Keep it current through everyday AI use

Your ordinary conversations with AI can become a natural way to keep the knowledge base up to date. As you discuss a project, make a decision, change a goal, or explain a preference, you are already creating useful source material. A scheduled agent can bring those changes back into your wiki, reducing the need to maintain the same information by hand.

The loop is simple: **use your assistants → collect new conversations → update the wiki → give future assistants better context.**

For example, a recurring pass every week or every five days could:

1. Collect new and changed threads across the AI tools you use, keeping source copies in your private archive.
2. Read them alongside the existing wiki and update the relevant project pages, decisions, preferences, and open questions.
3. Link changes to their sources, preserve earlier decisions as history, and keep user statements separate from assistant suggestions and inferences.
4. Save a dated change log and a local version-control commit so you can review, correct, or undo the update.

If you tell one assistant that a project is paused, the next refresh can carry that change into the shared context you give another assistant. You should not have to remember which model you told or repeat the change in every tool. The wiki remains yours to correct, including sections you maintain by hand that the updating agent leaves alone.

[YOLO — Your Ongoing Life Ontology](https://github.com/Milbaxter/yolo) is one implementation of this approach: a separate private Markdown vault, conversation importers, and a scheduled agent that compiles new evidence into linked wiki pages. It builds on this repository's broader idea; it is one starting point rather than a required architecture. Its [web-import workflow](https://github.com/Milbaxter/yolo/blob/main/docs/web-imports.md) explains how local histories, official exports, and selective browser reviews fit together.

Collection has practical limits. A scheduled local importer cannot fetch every service's history by itself: web sources may need fresh exports or an authorized browser review. Each source should retain its own progress, failed imports should remain retryable, and missing dates or incomplete coverage should stay visible. Imported conversations are evidence to summarize, not instructions for the updating agent to execute. If the compiling agent uses a hosted model, the selected source text leaves your machine.

## What could you get out of it?

**Less repeated explanation.** Give new assistants the background they need without retelling your life and projects each time.

**More useful collaboration.** A writing assistant could understand your voice. A coding agent could understand the project behind the task. A planning assistant could work with your real priorities and constraints.

**Continuity across tools.** Keep a personal context layer you control, rather than letting your history remain fragmented inside individual AI products.

**Rediscovery and reflection.** Find forgotten ideas, connect recurring interests, revisit decisions, and notice how your thinking has changed. Treat interpretations as things to explore, not authoritative judgments about who you are.

**A foundation for new applications.** Build personal search, project companions, learning tools, or entirely new kinds of agents on top of the same evolving knowledge base.

These are possibilities to investigate, not measured results from this repository.

## Private by design, selective by choice

The vision is for the sensitive work to happen on your own machine, with your data under your control. Local processing needs real technical safeguards; a local interface alone does not guarantee privacy.

Your full archive need not travel with every request. An agent should receive the relevant context you choose to share. If it is a hosted agent, that selected context leaves your device.

Private conversations deserve particular care: consent for local use does not automatically mean consent for sharing with outside services. You and the people involved should be able to set boundaries, correct information, and withdraw material. The knowledge base should support those changes.

**Open-source the approach. Keep the personal data private.**

## Build it your way

This could become a folder of linked notes, a local application, a personal knowledge graph, or something else. The choice of models, storage, interfaces, and integrations is deliberately open.

The central question is: **what becomes possible when you own a coherent, evolving context layer about your own life—and can choose how AI uses it?**

Ideas, prototypes, alternative approaches, and honest accounts of what works are welcome. See [contributing](CONTRIBUTING.md).

## Starting points

Official resources for exploring what data is available:

- [Google Takeout and Google data exports](https://support.google.com/accounts/answer/3024190?hl=en), including [Gemini data](https://support.google.com/gemini/answer/16920332?hl=en).
- [ChatGPT data exports](https://help.openai.com/en/articles/7260999-how-do-i-export-my-chatgpt-history-and-data) and [Claude data exports](https://support.claude.com/en/articles/9450526-export-your-claude-data).
- [Meta information tools](https://www.facebook.com/help/windows-desktop/506794473544588/) and [Spotify data packages](https://support.spotify.com/is-en/article/understanding-your-data/).
- [WhatsApp chat exports](https://faq.whatsapp.com/1180414079177245/) and [Telegram exports](https://telegram.org/blog/export-and-more).

[MIT licensed](LICENSE). The license covers this repository's original material, not personal data or third-party content.
