# 🔬 AI Research Scientist

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge\&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-0.3-1C3C3C?style=for-the-badge\&logo=langchain)
![Groq](https://img.shields.io/badge/Groq-Llama_3-F55036?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-1.39-FF4B4B?style=for-the-badge\&logo=streamlit)
![ArXiv](https://img.shields.io/badge/ArXiv-API-B31B1B?style=for-the-badge\&logo=arxiv)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**An AI-powered research assistant that transforms research questions into paper-backed analysis, hypotheses, experiment plans, and structured research reports.**

[🚀 Quick Start](#-quick-start) · [🏗️ Architecture](#️-architecture) · [📊 Sample Output](#-sample-output) · [🎤 Interview](#-interview-explanation)

</div>

---

## 📌 Overview

**AI Research Scientist** is an LLM-powered research assistant that structures multiple stages of the scientific research workflow into a single pipeline.

The system takes a natural-language research question and processes it through:

```text
Research Question
       ↓
Paper Search
       ↓
Paper Analysis
       ↓
Research Gap Identification
       ↓
Hypothesis Generation
       ↓
Experiment Design
       ↓
Research Report
```

The project combines **ArXiv API retrieval**, **Groq-powered LLM reasoning**, structured outputs, retry handling, CLI execution, and a Streamlit interface.

> ⚠️ This is an AI-assisted research workflow. Generated hypotheses, interpretations, and experiment plans require human review and actual experimentation before being treated as scientific findings.

---

## 🎯 Problem Statement

Scientific research involves several repetitive and time-consuming activities:

* Searching relevant research papers
* Understanding existing literature
* Identifying common methodologies
* Finding potential research gaps
* Developing testable hypotheses
* Designing experiments
* Preparing structured research reports
* Managing references

The goal of this project is to connect these activities into one AI-assisted research workflow.

### Traditional Workflow

```text
Search Papers
     ↓
Read Papers
     ↓
Take Notes
     ↓
Find Research Gaps
     ↓
Develop Hypothesis
     ↓
Design Experiment
     ↓
Write Report
```

### AI Research Scientist Workflow

```text
Research Question
       ↓
┌──────────────────┐
│  Paper Search    │
│    ArXiv API     │
└────────┬─────────┘
         ↓
┌──────────────────┐
│  Paper Analysis  │
│     Groq LLM     │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Research Gaps    │
│     Analysis     │
└────────┬─────────┘
         ↓
┌──────────────────┐
│   Hypothesis     │
│    Generation    │
└────────┬─────────┘
         ↓
┌──────────────────┐
│   Experiment     │
│      Design      │
└────────┬─────────┘
         ↓
┌──────────────────┐
│  Research Report │
└──────────────────┘
```

---

## ✨ Key Features

| Feature                      | Description                                                  |
| ---------------------------- | ------------------------------------------------------------ |
| 🔍 **Real Paper Search**     | Retrieves research papers through the ArXiv API              |
| 🧠 **LLM-Powered Analysis**  | Extracts themes, methods, datasets, and research gaps        |
| 💡 **Hypothesis Generation** | Generates structured and testable research ideas             |
| 🧪 **Experiment Design**     | Suggests baselines, datasets, metrics, and experiment setups |
| 📝 **Research Reports**      | Generates structured Markdown research reports               |
| 📚 **Paper References**      | Preserves retrieved paper metadata and references            |
| 🖥️ **Streamlit UI**         | Interactive web interface for research workflows             |
| ⚡ **CLI Support**            | Run research directly from the terminal                      |
| 🔄 **Auto-Retry**            | Handles temporary API and network failures                   |
| 📦 **Structured Outputs**    | Uses validation schemas for predictable data structures      |
| 🎨 **Clean Output**          | UTF-8-safe report and terminal output                        |

---

## 🏗️ Architecture

```text
┌─────────────────────────────────────────────────────────────┐
│                    RESEARCH QUESTION                        │
│              "Detecting fake news using NLP"                │
└────────────────────────────┬────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────┐
│              STEP 1 — PAPER SEARCH                          │
│                                                             │
│  ArXiv API                                                  │
│  • Search relevant papers                                   │
│  • Extract title, authors, abstract, date, URL               │
│  • Store paper metadata                                     │
└────────────────────────────┬────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────┐
│              STEP 2 — PAPER ANALYSIS                        │
│                                                             │
│  Groq LLM                                                   │
│  • Extract key themes                                       │
│  • Identify methods and datasets                            │
│  • Analyze research limitations                             │
│  • Identify potential research gaps                         │
└────────────────────────────┬────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────┐
│              STEP 3 — HYPOTHESIS GENERATION                 │
│                                                             │
│  Groq LLM                                                   │
│  • Generate research hypotheses                             │
│  • Provide rationale                                        │
│  • Define expected outcomes                                 │
└────────────────────────────┬────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────┐
│              STEP 4 — EXPERIMENT DESIGN                     │
│                                                             │
│  Groq LLM                                                   │
│  • Define experiments                                       │
│  • Select baselines                                         │
│  • Suggest datasets                                         │
│  • Define evaluation metrics                                │
└────────────────────────────┬────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────┐
│              STEP 5 — REPORT GENERATION                     │
│                                                             │
│  Groq LLM                                                   │
│  • Abstract                                                 │
│  • Introduction                                             │
│  • Related Work                                             │
│  • Hypotheses                                               │
│  • Experiment Design                                        │
│  • Limitations & Future Work                                │
│  • References                                               │
└────────────────────────────┬────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────┐
│                    RESEARCH REPORT                           │
│                  reports/*.md                               │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔬 Research Workflow

### 1️⃣ Paper Search

The system receives a research question and searches the **ArXiv API** for relevant papers.

Paper metadata can include:

* Title
* Authors
* Abstract
* Publication date
* ArXiv identifier
* Paper URL

Retrieved metadata is stored locally for downstream processing.

```text
Research Question
       ↓
ArXiv Query
       ↓
Relevant Papers
       ↓
Paper Metadata
```

---

### 2️⃣ Paper Analysis

The retrieved literature is analyzed using the LLM layer.

The analysis focuses on:

* Key research themes
* Existing methodologies
* Datasets
* Common approaches
* Limitations
* Potential research gaps
* Research directions

```text
Retrieved Papers
       ↓
    Groq LLM
       ↓
Themes + Methods + Gaps
```

---

### 3️⃣ Hypothesis Generation

The system uses the analysis to generate potential research hypotheses.

A hypothesis can include:

* Hypothesis ID
* Research idea
* Rationale
* Expected outcome
* Testability

Example:

```text
H-001

Investigate whether multimodal transformer
representations can improve fake-news classification
compared with text-only approaches.
```

> Hypotheses generated by the system are research proposals and are not experimentally validated by the current pipeline.

---

### 4️⃣ Experiment Design

Each hypothesis can be converted into a structured experiment plan.

An experiment may define:

* Dataset
* Baseline
* Proposed approach
* Evaluation metrics
* Experimental setup
* Expected outcome

```text
Hypothesis
    ↓
Experiment
    ↓
Dataset
    ↓
Baseline
    ↓
Model / Method
    ↓
Metrics
    ↓
Expected Outcome
```

---

### 5️⃣ Research Report

The final stage generates a structured Markdown report.

Typical sections include:

```text
1. Abstract
2. Introduction
3. Related Work
4. Research Hypotheses
5. Experiment Design
6. Limitations
7. Future Work
8. References
```

Generated reports are stored inside:

```text
reports/
```

---

## 🖥️ Application Interface

<p align="center">
  <img src="images/dashboard.jpeg" alt="AI Research Scientist Dashboard" width="900"/>
</p>

The Streamlit interface provides an interactive way to submit research questions and inspect the research workflow.

---

## 📊 Sample Output

### Research Question

```text
Detecting fake news using NLP
```

### Papers Found

```text
[P1] Exploring the Role of Visual Content in Fake News Detection

[P2] A Deep Ensemble Framework for Fake News Detection

[P3] FakeSwarm: Improving Fake News Detection

[P4] TIB's Visual Analytics Group at MediaEval '20

[P5] Localization of Fake News Detection
```

### Hypotheses Generated

```text
H-001
Investigate whether multimodal transformer representations
can improve fake-news classification compared with text-only models.

H-002
Investigate whether explanation methods can improve
interpretability of fake-news classification systems.

H-003
Investigate whether lightweight transformer architectures
can reduce inference latency while maintaining useful performance.
```

### Experiments Designed

```text
E1 → Multimodal Transformer
E2 → Explainable Ensemble
E3 → Lightweight / Streaming Transformer
```

### Generated Report

```text
reports/
└── detecting_fake_news_using_nlp_<timestamp>.md
```

---

## 🎯 Use Cases

| Domain               | Example Research Question                          |
| -------------------- | -------------------------------------------------- |
| 🤖 **AI / ML**       | Detecting fake news using NLP                      |
| 🏥 **Healthcare**    | Improving disease detection from medical images    |
| 🌍 **Climate**       | Predicting extreme weather using satellite data    |
| 💰 **Finance**       | Fraud detection in financial transactions          |
| 🎓 **Education**     | Personalized learning using reinforcement learning |
| 🧬 **Biology**       | Protein structure prediction using deep learning   |
| 🧪 **Scientific ML** | Machine learning for scientific discovery          |

---

## 🛠️ Tech Stack

| Technology      | Purpose                           |
| --------------- | --------------------------------- |
| **Python 3.11** | Core application runtime          |
| **Groq**        | LLM inference                     |
| **LangChain**   | LLM integration and orchestration |
| **ArXiv API**   | Research paper retrieval          |
| **Streamlit**   | Interactive web interface         |
| **Pydantic**    | Structured data validation        |
| **Tenacity**    | Retry and resilience handling     |
| **Rich**        | CLI output formatting             |
| **Markdown**    | Research report generation        |
| **Conda**       | Environment management            |

---

## 📁 Project Structure

```text
ai-research-scientist/
│
├── src/
│   ├── llm.py
│   │   └── LLM client and Groq integration
│   │
│   ├── orchestrator.py
│   │   └── Main research pipeline
│   │
│   ├── research/
│   │   ├── paper_search.py
│   │   │   └── ArXiv paper retrieval
│   │   │
│   │   ├── paper_reader.py
│   │   │   └── Paper analysis
│   │   │
│   │   ├── hypothesis.py
│   │   │   └── Hypothesis generation
│   │   │
│   │   └── experiment_design.py
│   │       └── Experiment planning
│   │
│   └── report/
│       └── writer.py
│           └── Research report generation
│
├── data/
│   ├── papers/
│   │   └── Retrieved paper metadata
│   │
│   └── experiments/
│       └── Generated experiment plans
│
├── reports/
│   └── Generated research reports
│
├── tests/
│   └── Unit tests
│
├── images/
│   └── dashboard.jpeg
│
├── main.py
│   └── CLI entry point
│
├── streamlit_app.py
│   └── Streamlit interface
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚡ Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/vaibhav07772/ai-research-scientist.git
cd ai-research-scientist
```

---

### 2. Create Conda Environment

```bash
conda create -n ai-researcher python=3.11 -y
conda activate ai-researcher
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure API Key

Create a `.env` file from `.env.example` and add your Groq API key.

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit `.env` to GitHub.

---

## 🚀 Run the Application

### CLI

```bash
python main.py "Detecting fake news using NLP"
```

The system will run the research pipeline and generate a Markdown report.

### Streamlit

```bash
streamlit run streamlit_app.py
```

---

## 🔄 End-to-End Example

Suppose the user enters:

```text
How can transformers improve fake news detection?
```

The system processes the request as:

```text
                    USER QUESTION
                         │
                         ▼
                 ┌──────────────┐
                 │ ArXiv Search │
                 └──────┬───────┘
                        │
                        ▼
                 Research Papers
                        │
                        ▼
                 ┌──────────────┐
                 │ Paper Analysis│
                 └──────┬───────┘
                        │
                        ▼
                  Research Gaps
                        │
                        ▼
                 ┌──────────────┐
                 │  Hypotheses  │
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │ Experiments  │
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │ Final Report │
                 └──────────────┘
```

---

## 🧠 Design Decisions

### Why ArXiv API?

The system uses ArXiv as an external literature source instead of depending only on the LLM's internal knowledge.

This gives the paper-search stage access to actual paper metadata and references returned by the API.

---

### Why an LLM?

Traditional search can retrieve papers, but research workflows also require higher-level reasoning such as:

* Comparing methodologies
* Summarizing research directions
* Identifying potential gaps
* Generating hypotheses
* Designing experiments
* Structuring reports

The LLM layer handles these reasoning-oriented tasks.

---

### Why LangChain?

LangChain provides the LLM integration and orchestration layer used to connect the application with the model.

---

### Why Streamlit?

Streamlit provides a lightweight interactive interface without requiring a separate frontend framework.

---

### Why Pydantic?

Pydantic provides structured validation so information passed between components follows predictable schemas.

---

### Why Tenacity?

External APIs can fail temporarily because of:

* Network issues
* Rate limits
* Service interruptions

Tenacity provides retry handling for these cases.

---

## 🧪 AI Engineering Concepts Demonstrated

### LLM Engineering

* Prompt-based reasoning
* Structured generation
* LLM orchestration
* Research summarization

### Retrieval

* External API integration
* Research paper discovery
* Paper metadata processing

### Research Automation

* Literature analysis
* Research gap identification
* Hypothesis generation
* Experiment planning
* Report generation

### Reliability

* API retry handling
* Failure-aware API interactions
* Structured validation

### Software Engineering

* Modular architecture
* Separation of concerns
* CLI + Web interface
* Testable components

---

## 🔄 Research Automation Pipeline

| Step                  | Tool      | Purpose                   |
| --------------------- | --------- | ------------------------- |
| **Paper Search**      | ArXiv API | Retrieve research papers  |
| **Analysis**          | Groq LLM  | Extract research insights |
| **Hypothesis**        | Groq LLM  | Generate testable ideas   |
| **Experiment Design** | Groq LLM  | Create experiment plans   |
| **Report**            | Groq LLM  | Generate research report  |
| **UI**                | Streamlit | Interactive interface     |
| **CLI**               | Rich      | Terminal output           |

---

## ⚠️ Known Limitations

### 1. LLM Reasoning Errors

LLMs can generate incorrect interpretations, unsupported claims, or weak hypotheses.

Human review is required before using generated research content.

### 2. No Automatic Experiment Execution

The current system designs experiments but does not automatically execute them.

```text
Current:

Research Question
       ↓
Hypothesis
       ↓
Experiment Design
       ↓
Report
```

Future:

```text
Research Question
       ↓
Hypothesis
       ↓
Experiment Design
       ↓
Experiment Execution
       ↓
Results
       ↓
Analysis
       ↓
New Hypothesis
```

### 3. Literature Coverage

The quality of literature analysis depends on the papers returned by the ArXiv search.

### 4. Language

The current workflow primarily focuses on English-language research content.

### 5. Context and Token Limits

Large research collections may exceed the context available to the selected LLM and may require chunking, ranking, or retrieval improvements.

---

## 🚧 Roadmap

### Phase 0 — Current Foundation

* [x] ArXiv paper search
* [x] Paper metadata extraction
* [x] LLM-based paper analysis
* [x] Research gap analysis
* [x] Hypothesis generation
* [x] Experiment design
* [x] Markdown report generation
* [x] CLI interface
* [x] Streamlit interface
* [x] API retry handling
* [x] Structured outputs

### Phase 1 — Experiment Generation

* [ ] Automatic experiment code generation
* [ ] Dataset discovery
* [ ] Baseline implementation
* [ ] Training script generation

### Phase 2 — Sandboxed Execution

* [ ] Docker-based experiment sandbox
* [ ] Resource limits
* [ ] Isolated execution
* [ ] Experiment logging

### Phase 3 — Result Analysis

* [ ] Automatic result ingestion
* [ ] Metric comparison
* [ ] Experiment visualization
* [ ] Hypothesis validation

### Phase 4 — Multi-Experiment Research

* [ ] Parallel experiment execution
* [ ] Experiment comparison
* [ ] Automated research iteration
* [ ] Experiment tracking

### Phase 5 — Research Memory

* [ ] ChromaDB / vector database
* [ ] Semantic paper retrieval
* [ ] Persistent research memory
* [ ] Citation-aware retrieval

### Phase 6 — Advanced Research Automation

* [ ] Automated retraining workflows
* [ ] Research experiment tracking
* [ ] Reproducibility metadata
* [ ] Automated report improvement

### Phase 7 — Publication Support

* [ ] LaTeX research paper generation
* [ ] Conference-specific templates
* [ ] Bibliography generation
* [ ] Publication-ready formatting

---

## 🔮 Future Vision

The long-term goal is to evolve the system from an AI research assistant into a more complete research automation platform.

```text
                AI Research Scientist
                         │
        ┌────────────────┼────────────────┐
        ↓                ↓                ↓
 Literature          Reasoning       Experimentation
 Search              Engine          Engine
        │                │                │
        ↓                ↓                ↓
   Papers          Hypotheses        Experiments
        │                │                │
        └────────────────┼────────────────┘
                         ↓
                  Result Analysis
                         ↓
                  Research Report
                         ↓
                  New Hypothesis
                         ↺
```

The intended future research loop is:

```text
Question
   ↓
Literature
   ↓
Hypothesis
   ↓
Experiment
   ↓
Results
   ↓
Analysis
   ↓
New Hypothesis
   ↺
```

---

## 🎤 Interview Explanation

### 30-Second Answer

> **AI Research Scientist is an LLM-powered research automation system that takes a research question, searches relevant papers through the ArXiv API, analyzes the literature, identifies potential research gaps, generates testable hypotheses, designs experiments, and produces a structured research report.**

### Technical Answer

> **The system uses ArXiv as the external literature source and Groq-powered LLMs through LangChain for analysis and generation. The workflow is modularized into paper search, paper analysis, hypothesis generation, experiment design, and report generation. Pydantic is used for structured validation, Tenacity handles retries, and Streamlit provides the interactive interface.**

### One-Line Architecture

```text
Research Question
→ ArXiv Retrieval
→ LLM Analysis
→ Research Gaps
→ Hypothesis
→ Experiment Design
→ Report
```

---

## ❓ Common Interview Questions

### Q1. What problem does this project solve?

**Answer:**

It streamlines repetitive research activities such as literature search, paper analysis, hypothesis generation, experiment planning, and report preparation into a single AI-assisted workflow.

---

### Q2. Why did you use ArXiv?

**Answer:**

I use ArXiv as an external research source so the literature-search stage can work with actual paper metadata rather than relying only on the LLM's internal knowledge.

---

### Q3. Is this a RAG system?

**Answer:**

The current system has a retrieval component because it retrieves papers from ArXiv before downstream LLM processing. However, I would describe the current implementation primarily as an AI research workflow rather than a conventional vector-database RAG system.

---

### Q4. Does the system actually perform experiments?

**Answer:**

No. The current version generates experiment designs. Actual experiment execution and result ingestion are planned future extensions.

---

### Q5. Can the LLM hallucinate?

**Answer:**

Yes. The LLM can generate incorrect interpretations or unsupported statements. Therefore, generated research content needs human validation. The literature-search stage is grounded through the ArXiv API.

---

### Q6. Why not let the LLM directly search papers?

**Answer:**

I wanted an explicit external retrieval layer. ArXiv provides actual paper metadata, while the LLM focuses mainly on analysis, reasoning, hypothesis generation, experiment design, and report generation.

---

### Q7. Why did you separate the project into modules?

**Answer:**

Separation of concerns makes the system easier to test, debug, maintain, and extend. For example, the paper-search module can be modified independently from the hypothesis-generation module.

---

### Q8. What happens if the ArXiv/API request fails?

**Answer:**

Tenacity provides retry handling so temporary network or API failures can be retried instead of immediately terminating the workflow.

---

### Q9. Why Streamlit?

**Answer:**

Streamlit provides a lightweight interactive interface for running the research workflow without requiring a separate frontend stack.

---

### Q10. What would you build next?

**Answer:**

The next major step would be sandboxed experiment execution, followed by automatic result ingestion and comparison. This would allow the system to move from experiment planning toward an iterative research workflow.

---

### Q11. What is the most important engineering idea in this project?

**Answer:**

The main idea is connecting multiple research stages into one structured pipeline instead of treating paper search, analysis, hypothesis generation, experiment design, and report writing as isolated tasks.

---

### Q12. What is the biggest limitation?

**Answer:**

The current system can design experiments but does not automatically execute and validate them. Therefore, the generated hypotheses and expected outcomes are proposals that require real experimentation.

---

## 🔐 Security

The application follows basic API-key security practices:

* Store API keys in `.env`
* Never commit `.env`
* Keep secrets out of source code
* Use `.gitignore`
* Avoid exposing keys in logs
* Validate external inputs
* Review generated research artifacts before use

---

## 🤝 Contributing

Contributions are welcome.

```bash
# Fork the repository

# Create a feature branch
git checkout -b feature/amazing-feature

# Make your changes

# Commit
git add .
git commit -m "Add amazing feature"

# Push
git push origin feature/amazing-feature
```

Then open a Pull Request.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

<div align="center">

### Vaibhav Singh

**Aspiring AI/ML Engineer | Generative AI | Agentic AI | RAG | MLOps**

[GitHub](https://github.com/vaibhav07772) ·
[LinkedIn](https://www.linkedin.com/in/vaibhav07772/)

</div>

---

## 🙏 Acknowledgments

* [ArXiv](https://arxiv.org/) — Open-access research papers and API
* [Groq](https://groq.com/) — LLM inference
* [LangChain](https://www.langchain.com/) — LLM application framework
* [Streamlit](https://streamlit.io/) — Interactive application framework

---

<div align="center">

### 🔬 Research Question → Literature → Hypothesis → Experiment → Report

**Built as an AI Engineering project for research workflow automation.**

⭐ Star this repository if you find it useful!

</div>
