# 🤖 AI Engineering Operating System (AEOS)

<div align="center">

### From Natural Language Requirement → Product Specification → Architecture → Code → Testing → Security → DevOps → SRE → Recovery

<p>
  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Groq-LLM-blueviolet?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LangGraph-Orchestration-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/MCP-Integration-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit" />
  <img src="https://img.shields.io/badge/Docker-Containerization-2496ED?style=for-the-badge&logo=docker" />
  <img src="https://img.shields.io/badge/Kubernetes-Deployment-326CE5?style=for-the-badge&logo=kubernetes" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
</p>

**An AI-powered engineering orchestration platform that transforms natural-language software requirements into a structured, multi-stage engineering workflow.**

</div>

---

## 📌 Overview

**AI Engineering Operating System (AEOS)** is a multi-agent AI engineering platform designed to orchestrate the software development lifecycle from a single natural-language requirement.

Instead of using an LLM only as a code generator, AEOS divides the engineering process into specialized stages:

```text
                    Natural Language Requirement
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Product Manager   │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │      Architect      │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │        Coder        │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │       Tester        │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │      Security       │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │       DevOps        │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │        SRE          │
                    └──────────┬──────────┘
                               ▼
                       ┌──────────────┐
                       │ Healthy?     │
                       └──────┬───────┘
                         YES  │  NO
                              │
                 ┌────────────┘
                 ▼
               Complete
                             
                         NO
                         │
                         ▼
                        RCA
                         │
                         ▼
                      Recovery
                         │
                         ▼
                       Coder
                         ↺
```

The objective is to move beyond:

```text
Prompt → Code
```

toward:

```text
Requirement
     ↓
Engineering Reasoning
     ↓
Implementation
     ↓
Verification
     ↓
Security
     ↓
Operations
     ↓
Reliability
     ↓
Root Cause Analysis
     ↓
Recovery
```

---

# 🚀 Why AEOS?

Modern AI coding tools often focus primarily on generating source code.

AEOS explores a broader engineering workflow by giving different responsibilities to different AI agents.

### Traditional Approach

```text
User
 ↓
LLM
 ↓
Code
```

### AEOS Approach

```text
User Requirement
       ↓
Product Thinking
       ↓
Architecture
       ↓
Implementation
       ↓
Testing
       ↓
Security
       ↓
DevOps
       ↓
SRE
       ↓
RCA
       ↓
Recovery
       ↺
```

This makes the engineering process more **structured, modular, traceable, failure-aware, and extensible**.

---

# ✨ Core Capabilities

* 🧠 Multi-agent AI engineering workflow
* 📋 Natural-language requirement analysis
* 🧑‍💼 AI Product Manager
* 🏗️ AI Architecture planning
* 💻 AI code/project generation
* 🧪 Automated testing analysis
* 🛡️ Security-oriented review
* 🚀 DevOps and deployment planning
* 📈 SRE health assessment
* 🔍 Root Cause Analysis (RCA)
* ♻️ Recovery feedback loop
* 🕸️ LangGraph-based orchestration
* ⚡ Groq-powered LLM inference
* 🌐 FastAPI backend
* 🖥️ Streamlit engineering dashboard
* 🔌 MCP integration foundation
* 🐳 Docker support
* ☸️ Kubernetes deployment foundation
* 📦 Structured agent outputs
* 🔐 Environment-based secret configuration
* 🔁 Retry and exponential-backoff resilience

---

# 🧩 Multi-Agent Architecture

AEOS uses specialized engineering agents instead of asking a single LLM to handle the entire workflow.

| Agent                  | Responsibility                                                                |
| ---------------------- | ----------------------------------------------------------------------------- |
| 📋 **Product Manager** | Converts natural-language requirements into structured product specifications |
| 🏗️ **Architect**      | Designs system architecture, APIs, data flow and technology choices           |
| 💻 **Coder**           | Generates the requested project structure and source files                    |
| 🧪 **Tester**          | Reviews implementation and identifies testing issues                          |
| 🛡️ **Security**       | Performs security-oriented analysis                                           |
| 🚀 **DevOps**          | Creates containerization, CI/CD and deployment planning                       |
| 📈 **SRE**             | Evaluates operational health and reliability evidence                         |
| 🔍 **RCA**             | Identifies root causes when failures are detected                             |

---

# 🔄 Agent Workflow

```text
                    USER REQUIREMENT
                           │
                           ▼
                  ┌─────────────────┐
                  │ Product Manager │
                  └────────┬────────┘
                           │
                           ▼
                    Product Spec
                           │
                           ▼
                  ┌─────────────────┐
                  │    Architect    │
                  └────────┬────────┘
                           │
                           ▼
                     Architecture
                           │
                           ▼
                  ┌─────────────────┐
                  │      Coder      │
                  └────────┬────────┘
                           │
                           ▼
                  Generated Project
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
              Tester              Security
                 │                   │
                 └─────────┬─────────┘
                           ▼
                        DevOps
                           │
                           ▼
                         SRE
                           │
                    ┌──────┴──────┐
                    ▼             ▼
                 HEALTHY       UNHEALTHY
                    │             │
                    ▼             ▼
                   END           RCA
                                  │
                                  ▼
                              Recovery
                                  │
                                  ▼
                                Coder
                                  ↺
```

---

# ♻️ Self-Healing / Recovery Loop

One of the key ideas behind AEOS is that an unsuccessful engineering workflow should not simply stop.

When SRE identifies an unhealthy state, the workflow can move into Root Cause Analysis.

```text
SRE
 │
 ▼
UNHEALTHY
 │
 ▼
Root Cause Analysis
 │
 ├── Root Cause
 ├── Contributing Factors
 ├── Safe Fix
 ├── Verification Test
 └── Rollback Decision
 │
 ▼
Coder
 │
 ▼
Tester
 │
 ▼
Security
 │
 ▼
DevOps
 │
 ▼
SRE
 │
 └──────────────► Recovery Loop
```

Recovery attempts are configurable:

```env
MAX_RECOVERY_ATTEMPTS=3
```

The important concept is:

```text
Failure
  ↓
Diagnosis
  ↓
Safe Fix
  ↓
Verification
  ↓
Re-evaluation
```

rather than simply restarting the entire process.

---

# 🔍 Autonomous Root Cause Analysis

AEOS includes an RCA stage that analyzes failure evidence and produces structured diagnostic information.

Example:

```json
{
  "root_cause": "Validation behavior does not match specification",
  "contributing_factors": [
    "Missing validation test"
  ],
  "safe_fix": "Correct validation behavior",
  "verification_test": "Run invalid-input tests",
  "rollback_required": false
}
```

### Example RCA Scenario

Suppose a generated FastAPI application is expected to return:

```text
400 Bad Request
```

for invalid input, but FastAPI/Pydantic returns:

```text
422 Unprocessable Entity
```

The RCA stage can identify the mismatch:

```text
Specification
      ↓
Expected: 400
      ↓
Implementation
      ↓
Actual: 422
      ↓
RCA
      ↓
Root Cause
      ↓
Safe Fix
      ↓
Verification Test
      ↓
Recovery Loop
```

This demonstrates how AEOS can reason about **specification-to-implementation mismatches** rather than only generating code.

---

# 🧠 Why LangGraph?

AEOS uses **LangGraph** to represent the engineering workflow as a stateful graph.

This is useful because the system requires:

* Sequential agent execution
* Shared workflow state
* Conditional routing
* Failure handling
* Recovery loops
* Explicit engineering stages
* Structured state transitions

Conceptually:

```text
                    Shared State
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
 Product Manager    Architect          Coder
        │               │                │
        └───────────────┼────────────────┘
                        ▼
                      Tester
                        │
                        ▼
                     Security
                        │
                        ▼
                      DevOps
                        │
                        ▼
                       SRE
                        │
                   ┌────┴────┐
                   ▼         ▼
                Healthy      RCA
                   │         │
                   ▼         ▼
                  END     Recovery
                              │
                              ▼
                            Coder
```

---

# ⚡ LLM Layer

AEOS uses **Groq** for LLM inference through the LangChain integration.

The LLM layer is responsible for:

* Agent reasoning
* Structured engineering outputs
* Requirement interpretation
* Architecture generation
* Code generation
* Testing analysis
* Security reasoning
* SRE analysis
* RCA generation

Configuration is loaded through environment variables.

Example:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=your_supported_model

AEOS_ENV=development
LOG_LEVEL=INFO

PROJECT_WORKSPACE=./generated_projects

MAX_RECOVERY_ATTEMPTS=3
MAX_AGENT_ITERATIONS=20
```

> ⚠️ Never commit `.env`, API keys, tokens, passwords, or private credentials to GitHub.

---

# 📦 Structured Agent Outputs

AEOS uses structured schemas so that downstream agents can consume predictable information.

Example Product Manager output:

```json
{
  "project_name": "project-name",
  "summary": "Project summary",
  "problem_statement": "Problem statement",
  "target_users": [],
  "features": [],
  "tech_stack": {},
  "out_of_scope": [],
  "success_metrics": [],
  "estimated_complexity": "low"
}
```

Instead of:

```text
LLM → Large Free-Form Text
```

AEOS aims for:

```text
Agent
  ↓
Structured State
  ↓
Next Agent
  ↓
Structured State
```

This improves interoperability between different stages of the workflow.

---

# 🛡️ Security by Design

Security is included as an engineering stage instead of being treated as an afterthought.

The Security Agent can review areas such as:

```text
Secrets
Unsafe shell execution
Path traversal
Insecure APIs
Authentication weaknesses
Dependency risks
Unsafe code patterns
```

Example structured output:

```json
{
  "overall_status": "PASS",
  "summary": "No security issues detected.",
  "findings": []
}
```

> Security analysis is AI-assisted and should not be considered a replacement for professional security testing.

---

# 📈 SRE Health Assessment

The SRE Agent evaluates available engineering evidence across:

```text
Testing
   +
Security
   +
Deployment
   +
Reliability Evidence
```

Possible states:

```text
HEALTHY
UNHEALTHY
```

If the system is unhealthy:

```text
SRE
 ↓
RCA
 ↓
Recovery
 ↓
Coder
 ↓
Tester
 ↓
Security
 ↓
DevOps
 ↓
SRE
```

This creates an iterative engineering feedback loop.

---

# 🔌 MCP Integration

AEOS is designed with an **MCP-compatible integration foundation**.

MCP can provide an integration boundary for future engineering tools and services such as:

* 📁 Filesystem operations
* 🐙 Repository operations
* 🐛 Issue tracking
* 🔔 Notifications
* 🛠️ Engineering tools
* ☁️ External services

The current implementation focuses primarily on the engineering orchestration workflow, while additional tool execution can be extended over time.

---

# 🖥️ Dashboard

AEOS provides a Streamlit dashboard for interacting with the engineering operating system.

The interface exposes information such as:

```text
System Status
     ↓
Agent Pipeline
     ↓
Product Specification
     ↓
Architecture
     ↓
Generated Files
     ↓
Security Results
     ↓
Deployment Plan
     ↓
SRE Health
     ↓
Root Cause
     ↓
Raw State
```

---

# 📸 Project Screenshots

## 1. AEOS Dashboard

<p align="center">
  <img src="images/dashboard.jpeg" alt="AI Engineering Operating System Dashboard" width="100%">
</p>

<p align="center">
  <i>AEOS Streamlit dashboard for submitting natural-language engineering requirements.</i>
</p>

---

## 2. Agent Pipeline & Generated Specification

<p align="center">
  <img src="images/agent-pipeline.jpeg" alt="AEOS Agent Pipeline and Product Specification" width="100%">
</p>

<p align="center">
  <i>Multi-agent engineering pipeline showing Product Manager, Architect, Coder, Tester, Security, DevOps, SRE and RCA stages.</i>
</p>

---

# 🎥 Demo

A project demonstration video is included in the repository.

### Demo Flow

```text
1. Enter a natural-language software requirement
              ↓
2. Start AEOS workflow
              ↓
3. Product Manager creates specification
              ↓
4. Architect designs the system
              ↓
5. Coder generates project files
              ↓
6. Tester reviews implementation
              ↓
7. Security performs security analysis
              ↓
8. DevOps creates deployment strategy
              ↓
9. SRE evaluates system health
              ↓
10. RCA analyzes detected failures
              ↓
11. Recovery loop sends issues back for correction
```

### ▶️ Demo Video

[🎬 Watch AEOS Demo](videos/demo.mp4)

> GitHub may not render repository MP4 files inline in every context, so the video is provided as a repository asset.

---

# 🎯 Example

A user can provide a requirement such as:

```text
Build a FastAPI calculator API with two endpoints:
POST /add and POST /multiply.

Each endpoint takes two numbers in JSON
and returns the result.
```

AEOS processes this requirement through the engineering pipeline.

### Product Specification

```text
Project:
fastapi-calculator-api

Features:
- Add endpoint
- Multiply endpoint
- Input validation

Technology:
Python
FastAPI
Docker
```

### Architecture

```text
Client
  ↓
API Layer
  ↓
Validation Layer
  ↓
Business Logic
  ↓
Response
```

### Generated Files

```text
app/main.py
tests/test_main.py
README.md
```

Example generated endpoint:

```python
@app.post("/add")
async def add(nums: Numbers):
    return {"sum": nums.a + nums.b}
```

---

# 🏗️ System Architecture

```text
┌──────────────────────────────────────────────┐
│                 Streamlit UI                │
│        AI Engineering Dashboard             │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                  FastAPI                     │
│             Project Controller               │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                 LangGraph                   │
│           Workflow Orchestrator             │
└──────────────────────┬───────────────────────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      Product       Architect      Coder
      Manager
          │            │            │
          └────────────┼────────────┘
                       ▼
                Generated Project
                       │
              ┌────────┴────────┐
              ▼                 ▼
           Tester            Security
              │                 │
              └────────┬────────┘
                       ▼
                    DevOps
                       │
                       ▼
                      SRE
                       │
                ┌──────┴──────┐
                ▼             ▼
             Healthy         RCA
                │             │
                ▼             ▼
               END         Recovery
                              │
                              ▼
                            Coder
```

---

# 🛠️ Technology Stack

| Technology        | Purpose                            |
| ----------------- | ---------------------------------- |
| **Python 3.11+**  | Core implementation                |
| **Groq**          | LLM inference                      |
| **LangChain**     | LLM integration                    |
| **LangGraph**     | Multi-agent workflow orchestration |
| **FastAPI**       | Backend API                        |
| **Streamlit**     | Interactive engineering dashboard  |
| **MCP**           | Tool/integration foundation        |
| **Pydantic**      | Validation and structured data     |
| **Tenacity**      | Retry and resilience               |
| **Docker**        | Containerization                   |
| **Kubernetes**    | Container orchestration            |
| **pytest**        | Testing                            |
| **python-dotenv** | Environment configuration          |

---

# 📁 Project Structure

```text
ai-engineering-operating-system/
│
├── app/
│   ├── agents/
│   │   ├── product_manager.py
│   │   ├── architect.py
│   │   ├── coder.py
│   │   ├── tester.py
│   │   ├── security.py
│   │   ├── devops.py
│   │   ├── sre.py
│   │   └── root_cause.py
│   │
│   ├── api/
│   │   ├── routes_health.py
│   │   └── routes_projects.py
│   │
│   ├── graph/
│   │   ├── state.py
│   │   └── workflow.py
│   │
│   ├── llm/
│   │   ├── provider.py
│   │   └── prompts.py
│   │
│   ├── services/
│   │   ├── project_service.py
│   │   └── monitoring_service.py
│   │
│   ├── tools/
│   │   └── safe_commands.py
│   │
│   └── main.py
│
├── mcp_servers/
│   └── filesystem_server.py
│
├── streamlit_app/
│   └── app.py
│
├── tests/
│   ├── test_health.py
│   └── test_project_service.py
│
├── k8s/
│   ├── namespace.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   └── secret.example.yaml
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── docker.yml
│
├── images/
│   ├── dashboard.png
│   └── agent-pipeline.png
│
├── videos/
│   └── demo.mp4
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
└── docs/
    ├── architecture.md
    └── security.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/vaibhav07772/ai-engineering-operating-system.git
cd ai-engineering-operating-system
```

---

## 2. Create Conda Environment

```bash
conda create -n aeos python=3.11 -y
```

Activate:

```bash
conda activate aeos
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=your_supported_model

AEOS_ENV=development
LOG_LEVEL=INFO

PROJECT_WORKSPACE=./generated_projects

MAX_RECOVERY_ATTEMPTS=3
MAX_AGENT_ITERATIONS=20
```

> Never commit your `.env` file to GitHub.

---

# ▶️ Run AEOS

## Start FastAPI

```bash
uvicorn app.main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Start Streamlit

Open another terminal:

```bash
conda activate aeos
streamlit run streamlit_app/app.py
```

Open:

```text
http://localhost:8501
```

---

# 🔌 API

## Health Check

```http
GET /health
```

Example:

```json
{
  "status": "ok"
}
```

---

## Run Project Generation

```http
POST /projects/run
```

Example:

```json
{
  "requirement": "Build a FastAPI calculator API with add and multiply endpoints."
}
```

The request is then passed into the multi-agent engineering workflow.

---

# 🧪 Testing

Run the test suite:

```bash
pytest
```

The project includes tests for core API and service behavior.

Generated projects can also contain their own testing suite.

---

# 🐳 Docker

Build:

```bash
docker build -t aeos .
```

Run:

```bash
docker run --env-file .env -p 8000:8000 aeos
```

Or use Docker Compose:

```bash
docker compose up --build
```

---

# ☸️ Kubernetes

Kubernetes manifests are available under:

```text
k8s/
```

Apply namespace:

```bash
kubectl apply -f k8s/namespace.yaml
```

Apply deployment:

```bash
kubectl apply -f k8s/deployment.yaml
```

Apply service:

```bash
kubectl apply -f k8s/service.yaml
```

Check:

```bash
kubectl get pods
kubectl get services
```

---

# 🔐 Security Considerations

AEOS is designed with security considerations throughout the engineering workflow.

Production deployments should additionally consider:

* Secret management
* Authentication
* Authorization
* Sandboxed code execution
* Container isolation
* File-system permissions
* Dependency scanning
* Network restrictions
* Audit logging
* Rate limiting
* Secure API configuration

> AI-generated code should always be reviewed and tested before execution in sensitive environments.

---

# 🔁 Resilience

AEOS includes retry handling around LLM invocation.

Conceptually:

```text
Request
   │
   ▼
  LLM
   │
   ├── Success ───────► Continue
   │
   └── Failure
         │
         ▼
       Retry
         │
         ▼
 Exponential Backoff
```

Recovery limits are configurable:

```env
MAX_RECOVERY_ATTEMPTS=3
```

---

# 🧠 Engineering Design Principles

### 1. Separation of Responsibilities

Each agent has a focused engineering role.

### 2. Structured Communication

Agents exchange structured state whenever possible.

### 3. Failure-Aware Engineering

Failures should generate evidence and analysis rather than silently passing.

### 4. Recovery Instead of Restart

RCA provides actionable information back to the engineering workflow.

### 5. Security by Design

Security review is part of the engineering pipeline.

### 6. Deployment Awareness

Generated projects are considered from development through deployment.

---

# 📊 Engineering Workflow

```text
Natural Language Requirement
             │
             ▼
     Product Specification
             │
             ▼
        Architecture
             │
             ▼
      Code Generation
             │
             ▼
           Testing
             │
             ▼
          Security
             │
             ▼
           DevOps
             │
             ▼
            SRE
             │
       ┌─────┴─────┐
       ▼           ▼
    Healthy      Failure
       │           │
       ▼           ▼
      END          RCA
                   │
                   ▼
                Recovery
                   │
                   ▼
                 Coder
                   │
                   ↺
```

---

# 🎯 What This Project Demonstrates

### Generative AI

* LLM-based reasoning
* Prompt engineering
* Structured generation
* AI-assisted software development

### Agentic AI

* Specialized agents
* Agent orchestration
* State management
* Task decomposition
* Conditional routing
* Recovery loops

### AI Engineering

* Requirement engineering
* Architecture generation
* Code generation
* Testing analysis
* Security analysis
* Reliability analysis
* RCA

### Backend Engineering

* FastAPI
* Pydantic
* API routing
* Service architecture

### DevOps

* Docker
* Docker Compose
* Kubernetes
* CI/CD foundation

### Reliability Engineering

* Health assessment
* Failure analysis
* Retry logic
* Exponential backoff
* Recovery workflows

---

# 🚧 Current Scope

Implemented areas include:

```text
✅ Multi-agent orchestration
✅ Product specification
✅ Architecture generation
✅ Code generation
✅ Testing analysis
✅ Security analysis
✅ DevOps planning
✅ SRE assessment
✅ Root Cause Analysis
✅ Recovery loop
✅ Groq integration
✅ FastAPI API
✅ Streamlit UI
✅ MCP foundation
✅ Docker foundation
✅ Kubernetes manifests
```

---

# 🛣️ Future Roadmap

```text
[✓] Multi-Agent Engineering Pipeline
[✓] LangGraph Orchestration
[✓] Groq Integration
[✓] Product Specification
[✓] Architecture Generation
[✓] Code Generation
[✓] Testing Agent
[✓] Security Agent
[✓] DevOps Agent
[✓] SRE Agent
[✓] RCA Agent
[✓] Recovery Loop

[ ] Isolated Code Execution Sandbox
[ ] Automated Generated-Project Execution
[ ] Real Test-Result Ingestion
[ ] Real Security Scanning
[ ] Prometheus Metrics
[ ] Distributed Tracing
[ ] Persistent Project Memory
[ ] GitHub Repository Automation
[ ] Automated Pull Requests
[ ] CI/CD Execution
[ ] Kubernetes Deployment Automation
[ ] Automated Rollback
[ ] Agent Evaluation Framework
[ ] Human Approval Gates
[ ] Multi-Project Workspace
```

---

# 💡 Key Idea

The central idea behind AEOS is:

```text
AI Coding Assistant
        ↓
AI Engineering Assistant
        ↓
AI Engineering Orchestration
        ↓
AI Engineering Control Loop
```

Instead of stopping after generating code, AEOS explores what happens **after code generation**:

```text
Can it be tested?
      ↓
Is it secure?
      ↓
Can it be deployed?
      ↓
Is it operationally healthy?
      ↓
If not, why?
      ↓
How can it be corrected?
      ↓
Can the workflow be evaluated again?
```

---

# 🎤 Interview Explanation

### Short Version

> **"I built AEOS, an AI Engineering Operating System that transforms natural-language software requirements into a multi-agent engineering workflow. It uses specialized agents for product specification, architecture, coding, testing, security, DevOps, SRE and root-cause analysis, orchestrated using LangGraph. The system also includes a recovery loop so detected failures can be analyzed and fed back into the engineering workflow."**

### Technical Version

> **"The main idea behind AEOS was to move beyond a simple prompt-to-code system. I designed a stateful LangGraph workflow where specialized agents handle different software-engineering responsibilities. A Product Manager creates the specification, the Architect designs the system, the Coder generates the project, and downstream agents perform testing, security, DevOps and SRE analysis. If the SRE stage identifies an unhealthy state, an RCA agent analyzes the failure and generates a safe recovery path that can feed back into the coding and verification stages."**

### Why LangGraph?

> **"I used LangGraph because the workflow requires shared state, sequential execution, conditional routing and recovery loops. A graph-based workflow makes these transitions explicit and easier to control than a simple chain of LLM calls."**

### Why Multi-Agent?

> **"I separated responsibilities because product planning, architecture, coding, testing, security and reliability require different reasoning tasks. Specialized agents make the system more modular and easier to debug, extend and evaluate."**

### What makes AEOS different from a basic coding agent?

> **"A basic coding agent primarily focuses on generating code. AEOS explores the complete engineering lifecycle around that code, including requirements, architecture, testing, security, deployment, reliability and recovery."**

---

# 📚 Learning Outcomes

By building AEOS, the project demonstrates practical experience with:

```text
Natural Language Requirements
            ↓
Product Engineering
            ↓
System Architecture
            ↓
LLM Applications
            ↓
Agentic AI
            ↓
LangGraph
            ↓
Software Generation
            ↓
Testing
            ↓
Security
            ↓
DevOps
            ↓
SRE
            ↓
RCA
            ↓
Resilience & Recovery
```

---

# ⚠️ Disclaimer

**AEOS is an AI engineering and educational/research project.**

The system generates AI-assisted engineering artifacts and analysis. Generated code, architecture, security findings, deployment configurations and recovery recommendations should be reviewed and validated by qualified engineers before being used in production or security-sensitive environments.

---

# 🤝 Contributing

Contributions are welcome.

```text
1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Add or update tests
5. Commit your changes
6. Open a Pull Request
```

For major changes, please open an issue first to discuss the proposed improvement.

---

# 📜 License

This project is released under the **MIT License**.

See the `LICENSE` file for details.

---

# 👨‍💻 Author

## Vaibhav Singh

**Aspiring AI/ML Engineer | Generative AI | Agentic AI | RAG | MLOps**

<p>
  <a href="https://github.com/vaibhav07772">
    <img src="https://img.shields.io/badge/GitHub-vaibhav07772-black?style=for-the-badge&logo=github" />
  </a>
  <a href="https://www.linkedin.com/in/vaibhav07772/">
    <img src="https://img.shields.io/badge/LinkedIn-Vaibhav%20Singh-blue?style=for-the-badge&logo=linkedin" />
  </a>
</p>

📧 **Email:** [vs9502778@gmail.com](mailto:vs9502778@gmail.com)

---

<div align="center">

### ⭐ If you found AEOS interesting, consider giving the repository a star.

**Built with ❤️ using Python, Groq, LangGraph, FastAPI, MCP, Docker, Kubernetes and Streamlit.**

</div>
