# 🐇 Rabbit

[![Watch Demo](https://img.youtube.com/vi/iBxRoAtwGO0/hqdefault.jpg)](https://youtu.be/iBxRoAtwGO0)

Rabbit is a Python SDK for browser-based autonomous agents. It combines browser automation, memory, task planning, and LLM orchestration to enable structured research and analysis workflows across the web.

This project is designed to be extensible and easy to reason about, with a regression-first test approach to support safer iteration and better startup readiness.

---

## 🚀 Core capabilities

- Browser automation for web tasks and extraction
- Agent-style workflow orchestration through the core runtime
- LLM integration with a modular service layer
- Memory and planning abstractions for multi-step tasks
- Extensible SDK structure for custom tooling
- Deterministic regression tests for critical behavior

---

## 🧪 Quality bar

This repository follows a regression-first workflow:

```bash
pytest -q
```

The test suite is intentionally small and deterministic so it can validate key project invariants without requiring live network or browser-dependent flows during routine CI runs.

---

## 📼 Demo

[![Watch Demo](https://img.shields.io/badge/YouTube-Watch%20Demo-red?style=for-the-badge&logo=youtube)](https://youtu.be/iBxRoAtwGO0)

---

## 📁 Project structure

```
Rabbit/
├── agent_task_loop.py # Main agent loop runner
├── requirements.txt # Python dependencies
├── setup.py # Installation setup
├── test_agent.py # Agent test suite
├── rabbit_sdk/ # Core SDK for Rabbit agent
│   ├── __init__.py
│   ├── agent.py # RabbitAgent class definition
│   ├── browser_controller.py # Controls headless browser actions
│   ├── config.py # Environment + configuration loader
│   ├── llm_manager.py # LLM query & response handling
│   ├── memory_manager.py # Agent memory management
│   ├── planner.py # Task planning module
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── browser_tools.py # Browser-specific tools
│   │   └── utility_tools.py # General utilities for agents
│   └── utils.py # Helper functions
└── examples/
    ├── __init__.py
    ├── simple_browser_task.py # Basic sentiment analysis example
    └── complex_workflow.py # Advanced multi-step automation example
```

---

## 🧪 Example: Sentiment Analysis of AI Safety

```bash
cd Rabbit/examples
python3 simple_browser_task.py
```

1. Open multiple URLs about AI and safety
2. Scrape relevant content
3. Run sentiment analysis
4. Summarize the key findings

---

## 🧪 Example: Comprehensive Crypto Analysis

```bash
cd Rabbit/examples
python3 complex_workflow.py
```

1. Open multiple URLs about crypto assets
2. Scrape relevant content
3. Run sentiment analysis
4. Summarize the key findings
5. Generate trading insights

---

## ⚙️ Setup and installation

### 1. Clone the repository

```bash
git clone https://github.com/wchisasa/rabbit.git
cd rabbit
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Configure environment variables

Copy the sample environment file and edit the values you need:

```bash
cp .env.example .env
```

Example values:

```ini
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=
RABBIT_LLM_PROVIDER=gemini
RABBIT_LLM_MODEL=gemini-2.0-flash
RABBIT_HEADLESS=true
```

---

## 🧠 Stack and dependencies

- Google Gemini (or other LLMs)
- Playwright / Puppeteer (for browser automation)
- Open-source planning, memory, and tooling layers

---

## 🛠 Development and testing

```bash
pytest -q
```

For live browser-driven experiments, use the example agent flows in the `examples/` directory after installing the required browser dependencies.

---

## 📌 Future roadmap

- [ ] Add support for OpenAI + Claude
- [ ] Extend toolset for data transformation tasks
- [ ] Integrate with vector DB for persistent memory
- [ ] Web UI for visualizing agent reasoning

---

## 📄 License

MIT License. See [`LICENSE`](LICENSE) for details.