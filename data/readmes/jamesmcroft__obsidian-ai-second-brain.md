# 🧠 Obsidian AI Second Brain

A starter template for building an **AI-augmented Second Brain** using [Obsidian](https://obsidian.md/), the CODE/PARA methodology, and [GitHub Copilot](https://github.com/features/copilot) skills.

> **Your Second Brain shouldn't be a passive filing cabinet. It should be an active collaborator that strengthens its own structure over time.**

This repository is the companion to the [AI-Augmented Second Brain blog series](https://www.jamescroft.co.uk), a 6-part guide to building a knowledge management system where AI actively participates in organizing, distilling, and connecting your knowledge.

> **This repo will evolve weekly** as new posts are published. Star ⭐ and watch 👁️ to follow along.

---

## The Three Pillars

This approach rests on three pillars that reinforce each other:

### 📂 Pillar 1 - Structured Knowledge Store (Obsidian + PARA)

An Obsidian vault organized using Tiago Forte's [PARA method](https://fortelabs.com/blog/para/), with a critical design constraint: **every structural choice must be machine-readable.**

Consistent templates. Typed frontmatter. Predictable section layouts. A README that serves as both human documentation and AI grounding context. 

### 🔗 Pillar 2 - Knowledge Graphs in Plain Markdown

Obsidian's `[[wikilinks]]` create a knowledge graph where every note is a node and every link is an edge. Backlinks surface implicit relationships. Dynamic query blocks auto-populate relationship tables. The graph turns a flat collection of files into a **connected knowledge system** that an AI can traverse, query, and extend, and it encodes where work remains.

### 🤖 Pillar 3 - Specialized AI Skills

Custom skills are detailed, reusable instruction sets stored as markdown that tell AI agents exactly how to perform specific knowledge workflows. Skills are not prompts. They encode your vault's actual folder paths, template structures, and cross-linking conventions, producing reliable, grounded output instead of hallucinated guesses.

### How They Reinforce Each Other

- **Structure enables AI**: Templates and conventions give the AI reliable patterns to follow
- **AI strengthens the graph**: Every skill-driven operation adds cross-links and fills gaps
- **The graph guides the AI**: Relationships and gaps show the AI what's connected and what's missing

The result: a **self-reinforcing loop** where the system compounds rather than decays.

---

## What's Inside

```
obsidian-ai-second-brain/
├── README.md                          # This file - CODE/PARA docs + setup guide
├── LICENSE                            # MIT
├── .gitignore                         # Excludes .obsidian/ workspace files
│
├── Projects/                          # Active tasks with goals and deadlines
│   └── Build My Second Brain.md       # Example: the meta-project of setting up this vault
├── Areas/                             # Ongoing knowledge domains
│   └── Building a Second Brain.md     # Example: the CODE/PARA methodology itself
├── Resources/                         # Reference material (Articles, Blueprints, etc.)
│   └── Articles/
│       └── The PARA Method - Forte Labs.md
├── Techniques/                        # Distilled actionable knowledge
│   └── Progressive Summarization.md   # Example: Forte's layered distillation technique
├── Archive/                           # Completed/inactive items
│   ├── Areas/
│   ├── Projects/
│   ├── Resources/
│   └── Techniques/
├── Journal/                           # Time-based capture (Meetings, Weekly, Monthly)
│   ├── Meetings/
│   ├── 1-1s/
│   ├── Weekly/
│   └── Monthly/
├── People/                            # Contact and colleague profiles
│
├── _Templates/                        # Note templates for each PARA type
│   ├── Template - Area.md
│   ├── Template - Technique.md
│   ├── Template - Resource.md
│   ├── Template - Project.md
│   ├── Template - Person.md
│   ├── Template - Journal Meeting.md
│   ├── Template - Journal Daily.md
│   ├── Template - Journal Weekly.md
│   └── Template - Journal Monthly.md
│
├── _Attachments/                      # Images and file attachments
│
└── .github/
    └── skills/                        # Custom AI skills
        ├── vault-knowledge-retrieval/ # Query the knowledge graph
        │   └── SKILL.md               
        ├── vault-note-creation/       # Create new notes in your Second Brain
        │   └── SKILL.md               
        └── vault-note-update/         # Updates existing/archived notes in your Second Brain
            └── SKILL.md               
```

### Example Notes

The repository includes a set of interconnected example notes that demonstrate the system in action about the system itself, so they teach you the methodology while showing you the structure:

- **`Areas/Building a Second Brain.md`** - An Area note covering the CODE/PARA methodology, with filled-in Overview, Key Concepts, and auto-populated Technique/Resource tables
- **`Techniques/Progressive Summarization.md`** - A Technique linking back to the Building a Second Brain Area, with Context, Approach, a 5-step Process, and Insights
- **`Resources/Articles/The PARA Method - Forte Labs.md`** - A Resource linking to both the Area and the Technique, with distilled Key Takeaways from Forte's canonical blog post
- **`Projects/Build My Second Brain.md`** - A Project referencing all three, with Key Results, Progress, and Decisions, the meta-project of setting up your own vault

Together, these four notes form a mini knowledge graph: the Area is the domain, the Technique is distilled knowledge from that domain, the Resource informs the Technique, and the Project puts it all into action. Open any one and you'll see the others referenced via `[[wikilinks]]`.

---

## The CODE Workflow

[CODE](https://www.buildingasecondbrain.com/) defines how information flows through the vault:

| Stage | What happens | AI role |
|-------|-------------|---------|
| **Capture** | Save insights, meeting notes, ideas into `Journal/` | AI synthesizes notes with calendar and chat data |
| **Organize** | Sort into PARA folders based on actionability | AI scans for duplicates, reactivates archived notes, adds cross-links |
| **Distill** | Extract key insights into `Techniques/` | AI chains daily → weekly → monthly synthesis |
| **Express** | Turn knowledge into output — posts, talks, decisions | AI enables rapid recall and polished artifacts |

## The PARA Structure

[PARA](https://fortelabs.com/blog/para/) defines where information lives:

| Folder        | Purpose                                        |
| ------------- | ---------------------------------------------- |
| `Projects/`   | Active tasks with clear goals and deadlines    |
| `Areas/`      | Ongoing responsibilities and knowledge domains |
| `Resources/`  | Non-actionable content that supports learning  |
| `Techniques/` | Distilled knowledge, bridges Distill ↔ Express |
| `Archive/`    | Completed or inactive items from the above     |

Supporting folders: `Journal/` (time-based capture), `People/` (relationships), `_Templates/` (note structure), `_Attachments/` (media).

---

## Getting Started

1. **Fork this repository**: click the Fork button on GitHub to create your own copy
2. **Clone it locally**: `git clone https://github.com/<your-username>/obsidian-ai-second-brain.git`
3. **Open as an Obsidian vault**: in Obsidian, choose "Open folder as vault" and select the cloned directory
4. **Explore the example notes**: start with `Areas/Building a Second Brain.md` and follow the `[[wikilinks]]` to see how the graph connects
5. **Create your first Area**: use `_Templates/Template - Area.md` as the template and write about a knowledge domain you care about
6. **Try a skill**: ask GitHub Copilot "what do I know about {topic}?" to invoke the `vault-knowledge-retrieval` skill and query your vault
7. **Clean-up the example notes**: once you're comfortable with the patterns, remove the examples, if you'd like, and start building your own knowledge base

---

## Contributing

This project is in its early stages. Contributions, ideas, and feedback are welcome once the core structure is in place. In the meantime, [open an issue](https://github.com/jamesmcroft/obsidian-ai-second-brain/issues) if you have questions or suggestions.

---

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Building a Second Brain](https://www.buildingasecondbrain.com/) by Tiago Forte - the foundational methodology
- [The PARA Method](https://fortelabs.com/blog/para/) - the organizational framework
- [Obsidian](https://obsidian.md/) - the knowledge platform
- [GitHub Copilot](https://github.com/features/copilot) - the AI agent platform
