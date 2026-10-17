# AI Interaction Personalization Technology Using Structured Data

**DEFENSIVE PUBLICATION**

This publication is a defensive publication intended to prevent patenting of the described technology by any individuals or organizations. The project was under CC0 1.0 Universal until April 12, 2025, and is now licensed under the MIT License (see LICENSE for details).

## Notice for Forkers and Cloners

As of April 12, 2025, Personal Context Manager (PCM) has switched from CC0 1.0 Universal to the MIT License to ensure attribution while remaining open-source. If you forked or cloned PCM before this date (e.g., forkers: AxiMinds, brucewedding, DRanger666, sgwd), your copy remains under CC0 1.0 terms. However, if you pull in new updates from the main repo, the MIT License will apply to those portions, requiring attribution (see [LICENSE_CHANGE.md](https://github.com/mikhashev/personal-context-manager/blob/main/LICENSE_CHANGE.md) for details).

I'd love to collaborate! I'm currently focused on [D-PC Messenger](https://github.com/mikhashev/dpc-messenger) - an active Proof of Concept that implements Personal Context Manager technology with P2P networking capabilities. If you're interested in contributing or aligning your copy with the MIT License for future updates, please reach out via X (@mikeshev4enko) or email from my profile. Let's work together to enhance PCM!

## About the Project

This technology solves a fundamental limitation of modern AI systems — the lack of long-term memory between sessions. The core principle involves transferring structured data with a mandatory instruction block that defines the rules for processing them.

<img src="https://raw.githubusercontent.com/mikhashev/personal-context-manager/refs/heads/main/docs/img/schema.png" width="600" height="448">

## D-PC Messenger

> **Note:** This repository contains the foundational specification and templates. The active development continues in [D-PC Messenger](https://github.com/mikhashev/dpc-messenger) — a Proof of Concept implementation with P2P networking capabilities.

### Project Relationship

| This Repository (PCM) | D-PC Messenger |
|----------------------|----------------|
| Conceptual framework & defensive publication | Active implementation (PoC) |
| Templates & documentation | Full application code |
| Specification | Working software |

[D-PC Messenger](https://github.com/mikhashev/dpc-messenger) (Decentralized Personal Context) extends Personal Context Manager technology with peer-to-peer networking for human-AI collaboration.

### The Vision: A Private Internet for Human-AI Collaboration

**The Problem:** AI is transforming how we work and think, but it's creating two critical failures:

1. **"Digital Debris"** — Endless chat histories where valuable insights get lost in noise
2. **"Computational Inequality"** — Only people with powerful hardware or expensive subscriptions can use advanced AI

**D-PC Messenger solves both:**
- **Knowledge Commits** transform ephemeral conversations into structured, versioned knowledge (like git commits for your personal context)
- **P2P Compute Sharing** lets you borrow a friend's GPU to run powerful AI models — no cloud, no subscriptions, complete privacy
- **Context Collaboration** enables your AI assistants to work together by securely sharing relevant knowledge

### The Deeper Mission

This isn't just productivity software. We're building infrastructure for **human-AI co-evolution** — ensuring humans can maintain cognitive parity as artificial general intelligence emerges.

Your personal context should function like **"DNA for Knowledge"**:
- **Portable** — Follows you across devices, services, lifetimes
- **Evolvable** — Grows and adapts as you learn
- **Owned by you** — Not extracted and monetized by corporations

### Key Features (in D-PC Messenger)

- **True P2P Architecture** - Messages never touch servers, only peers (6-tier connection fallback: IPv6 → IPv4 → WebRTC → UDP Hole Punch → Relay → Gossip)
- **DPC Agent** - Embedded autonomous AI agent with 40+ tools, background consciousness, evolution system, and persistent memory
- **Knowledge Commits** - Git-like versioning for AI-extracted knowledge with bias mitigation
- **P2P Compute Sharing** - Share your GPU-powered inference or API access with trusted peers
- **Context Collaboration** - Securely share context with peers so their AIs can provide informed assistance
- **Context Firewall** - Granular permission control over what data and permissions you share
- **Reasoning Models** - Support for DeepSeek R1, Claude Extended Thinking, OpenAI o1/o3 and others
- **Universal Connectivity** - Works with or without federation hub via DHT bootstrap

See the [full vision](https://github.com/mikhashev/dpc-messenger/blob/main/VISION.md) for the long-term roadmap.

## Key Features

- Comprehensive preservation of relevant context between sessions
- Support for various data formats (JSON, YAML, XML, graph structures)
- Choice of data storage location (local/cloud)
- Personalization management through instructions
- Significantly improved recommendation accuracy through contextual personalization
- Optimized context transfer for improved response times

## Self-Improving Context Framework

We've developed a framework that enables context structures to evolve and improve over time based on usage patterns, neural feedback, and effectiveness metrics. Key components include:

- **Self-improvement tracking** - Automatically identifies patterns in context effectiveness
- **Neural interface integration** - Framework for correlating brain activity with context performance using EEG devices
- **Context evolution analysis** - Tracks changes over time and recommends structural improvements
- **Instruction optimization** - Tests and adapts instruction blocks to improve AI responses

This framework takes personalization to the next level by enabling continuous adaptation based on real-world performance data.

> **Note:** While the neural interface integration framework is implemented in code, it has not yet been tested with actual EEG hardware devices. The integration with Muse, EMOTIV, and OpenBCI exists at the code level and is ready for testing with physical devices.

- [Implementation Code](self-improvement/README.md)
- [Framework Documentation](docs/self-improvement-framework.md)
- [Visual Diagrams](docs/self-improvement-diagrams.md)

## Benchmarking Framework

We are developing a comprehensive benchmarking framework to quantify the performance improvements provided by PCM technology. Testing and validation will be conducted through [D-PC Messenger](https://github.com/mikhashev/dpc-messenger), our active implementation platform. Key areas of focus include:

- **Context preservation** between sessions compared to traditional approaches
- **Recommendation accuracy** enhancement through contextual personalization
- **Response time optimization** through efficient context transfer
- **Cognitive load reduction** with neural interface integration

We are committed to transparent and reproducible performance testing. If you're interested in contributing to our benchmarking efforts, please see our [contributing guidelines](CONTRIBUTING.md).

## Documentation

- Full technical description is available in [technical-description.md](docs/technical-description.md).
- Quick start guide is available in [simple-guide.md](docs/simple-guide.md).
- Use cases guides is available in [use cases](use-cases/).

## Use Cases

### Self-Education

We've developed a specialized personal context template for enhancing self-education using AI systems. This implementation leverages the latest research in cognitive science and memory formation to create an optimized learning experience.

The template incorporates:
- Evidence-based learning strategies (active recall, spaced repetition)
- Neuroscience-informed approaches to memory formation
- Techniques to overcome AI limitations like context windows and hallucinations
- Personalized learning pathways based on cognitive strengths and preferences

Files:
- [Personal Context Template for Self-Education v2](use-cases/self-education/personal_context_self_education_template_v2.json) (recommended)
- [Personal Context Template for Self-Education v1](use-cases/self-education/personal_context_self_education_template.json) (simplified)
- [How to Use Personal Context Template for AI-Enhanced Learning](use-cases/self-education/README.md)

## Ethical Principles

This project is intended exclusively for civilian purposes: improving education, healthcare, increasing productivity, and personalizing AI interaction. Please review the [ethical guidelines](ETHICAL_GUIDELINES.md) before use.

## Support the Project

If you would like to support further development and promotion of the technology, you can send a donation to the following addresses:

- Bitcoin: [bc1qfev88vx2yem48hfj04udjgn3938afg5yvdr92x]
- Ethereum: [0xB019Ae32a98fd206881f691fFe021A2B2520Ce9d]
- TON: [UQDWa0-nCyNM1jghk1PBRcjBt4Lxvs86wflNGHHQtxfyx-8J]

## License

Licensed under the MIT License - See [LICENSE](LICENSE) for details.
