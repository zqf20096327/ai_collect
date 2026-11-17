# Production-Grade Agentic AI System

Modern **agentic AI systems**, whether running in **development, staging, or production**, are built as a **set of well-defined architectural layers** rather than a single service. Each layer is responsible for a specific concern such as **agent orchestration, memory management, security controls, scalability, and fault handling**. A production-grade agentic system typically combines these layers to ensure agents remain reliable, observable, and safe under real-world workloads.

![Production Grade Agentic System](https://miro.medium.com/v2/resize:fit:2560/1*GB6tXauVBaHVGDE4L_FkYg.png)
*Production Grade Agentic System (Created by Fareed Khan)*

There are **two key aspects** that must be continuously monitored in an agentic system.

1.  The first is **agent behavior**, which includes reasoning accuracy, tool usage correctness, memory consistency, safety boundaries, and context handling across multiple turns and agents.
2.  The second is **system reliability and performance**, covering latency, availability, throughput, cost efficiency, failure recovery, and dependency health across the entire architecture.

Both are important for operating **multi-agent systems** reliably at scale.

In this blog, we will build all the core architectural layers needed to deploy a production-ready agentic system, **so teams can confidently deploy AI agents in their own infrastructure or for their clients.**

You can clone the repo:

```bash
git clone https://github.com/FareedKhan-dev/production-grade-agentic-system
cd production-grade-agentic-system
```

To run it with Docker:

```bash
cp .env.example .env.development
# In .env.development, set OPENAI_API_KEY and JWT_SECRET_KEY. The API refuses to start
# without a long random JWT secret; generate one with:
python -c "import secrets; print(secrets.token_urlsafe(64))"

make docker-run-env ENV=development    # the API docs are then at http://localhost:8000/docs
```

> **About the code in this guide.** The guide started as an article whose code used an `app/` layout. The repository keeps the code under [`src/`](src/), and the listings below use those paths. The listings are condensed for reading (some comments, logging and error handling are left out), so the files under `src/` are the reference. [CHANGELOG.md](CHANGELOG.md) lists what changed in each release.

## Table of Content

*   [Creating Modular Codebase](#ab61)
    *   [Managing Dependencies](#d7f1)
    *   [Setting Environment Configuration](#dfa0)
    *   [Containerization Strategy](#66e6)
*   [Building Data Persistence Layer](#c31d)
    *   [Structured Modeling](#49d1)
    *   [Entity Definition](#da20)
    *   [Data Transfer Objects (DTOs)](#0bdf)
*   [Security & Safeguards Layer](#1942)
    *   [Rate Limiting Feature](#1649)
    *   [Sanitization Check Logic](#ed53)
    *   [Context Management](#2115)
*   [The Service Layer for AI Agents](#9ef9)
    *   [Connection Pooling](#c497)
    *   [LLM Unavailability Handling](#2fe7)
    *   [Circuit Breaking](#0d26)
*   [Multi-Agentic Architecture](#2767)
    *   [Long-Term Memory Integration](#097b)
    *   [Tool Calling Feature](#6f9a)
*   [Building The API Gateway](#458a)
    *   [Auth Endpoints](#8a02)
    *   [Real-Time Streaming](#0d8e)
*   [Observability & Operational Testing](#86b1)
    *   [Creating Metrics to Evaluate](#0055)
    *   [Middleware Based Testing](#9c23)
    *   [Streaming Endpoints Interaction](#47b1)
    *   [Context Management Using Async](#5e3d)
    *   [DevOps Automation](#1b72)
*   [Evaluation Framework](#ff63)
    *   [LLM-as-a-Judge](#9e4a)
    *   [Automated Grading](#e936)
*   [Architecture Stress Testing](#f484)
    *   [Simulating our Traffic](#8f52)
    *   [Performance Analysis](#0703)

## <a id="ab61"></a>Creating Modular Codebase

Normally, Python projects start small and gradually become messy as they grow. When building production-grade systems, developers typically adopt a **Modular Architecture** approach.

This means separating different components of the application into distinct modules. By doing so, it becomes easier to maintain, test, and update individual parts without impacting the entire system.

Let’s create a structured directory layout for our AI system:

```bash
├── src/                         # Main Application Source Code
│   ├── agent/                   # AI Agent / LangGraph workflow
│   │   ├── prompts/             # AI System & Agent Prompts
│   │   └── tools/               # Agent Tools (web search)
│   ├── config/                  # Settings loaded from the environment
│   ├── data/                    # Data layer
│   │   ├── models/              # Database Models (SQLModel)
│   │   └── schemas/             # Data Validation Schemas (Pydantic)
│   ├── interface/               # API Route Handlers (auth, chat)
│   ├── services/                # LLM service (retries, fallback)
│   ├── system/                  # Logging, metrics, middleware, rate limiting
│   └── utils/                   # Shared Helper Utilities
├── evals/                       # AI Evaluation Framework
│   └── metrics/                 # Evaluation Metrics & Criteria
│       └── prompts/             # LLM-as-a-Judge Prompt Definitions
├── grafana/                     # Grafana Observability Configuration
│   └── dashboards/              # Grafana Dashboards
│       └── json/                # Dashboard JSON Definitions
├── prometheus/                  # Prometheus Monitoring Configuration
├── scripts/                     # DevOps scripts, load test
├── tests/                       # Tests (pytest, against a real PostgreSQL)
└── .github/                     # GitHub Configuration
    └── workflows/               # GitHub Actions CI
```

**This directory structure might seem complex to you at first but we are following a generic best-practice pattern** that is used in many agentic systems or even in pure software engineering. Each folder has a specific purpose:

*   `src/`: Contains the main application code, including API routes, core logic, database models, and utility functions.
*   `evals/`: Houses the evaluation framework for assessing AI performance using various metrics and prompts
*   `grafana/` and `prometheus/`: Store configuration files for monitoring and observability tools.

You can see many components have their own subfolders (like `agent/` and `tools/`) to further separate concerns. We are going to build out each of these modules step-by-step in the upcoming sections and also understand why each part is important.

### <a id="d7f1"></a>**Managing Dependencies**

The very first step in building a production-grade AI system is to create a dependency management strategy. Normally small projects start with a simple `requirements.txt` file and for a more complex project, we have to use `pyproject.toml` because it supports more advanced features like dependency resolution, versioning, and build system specifications.

Let’s create a `pyproject.toml` file for our project and start adding our dependencies and other configurations.

```ini
# ==========================
# Project Metadata
# ==========================
# Basic information about your Python project as defined by PEP 621
[project]
name = "production-grade-agentic-system"  # The distribution/package name
version = "1.0.0"                          # Current project version (semantic versioning recommended)
description = "Production-grade agentic system: FastAPI, LangGraph, PostgreSQL, Langfuse, Prometheus and Grafana"
readme = "README.md"                       # README file used for long description
requires-python = ">=3.13"                 # Minimum supported Python version
```

The first section defines the project metadata like name, version, description, and Python version requirement. This information is useful when publishing the package to package indexes like PyPI.

Then comes the core dependencies section where we list all the libraries our project relies on.

Since we are building an agentic AI system (For ≤10K users actively using our agent), we need a range of libraries for web framework, database, authentication, AI orchestration, observability, and more.

```ini
# ==========================
# Core Runtime Dependencies
# ==========================
# These packages are installed whenever your project is installed
# They define the core functionality of the application

dependencies = [
    # --- Web framework & server ---
    "fastapi>=0.163.1",        # High-performance async web framework
    "uvicorn>=0.54.0",         # ASGI server used to run FastAPI
    "uvloop>=0.23.0; sys_platform != 'win32'",  # Faster event loop for asyncio (not on Windows)

    # --- LangChain / LangGraph ecosystem ---
    "langchain>=1.0.5,<2",                       # Needed by Langfuse's LangChain callback handler
    "langchain-core>=1.8.1,<2",                  # Core abstractions for LangChain
    "langchain-openai>=1.8.0,<2",                # OpenAI (and OpenAI-compatible) chat models
    "langgraph>=1.2.22,<2",                      # Graph-based agent/state workflows
    "langgraph-checkpoint-postgres>=3.2.1,<4",   # PostgreSQL-based LangGraph checkpointing
    "openai>=3.51.0,<4",                         # Error types for retries, client for the evals

    # --- Observability & tracing ---
    "langfuse>=3.15.0,<4",      # LLM tracing, monitoring, and evaluation
    "structlog>=26.1.0",        # Structured logging

    # --- Authentication & security ---
    "bcrypt>=5.0.0,<6",         # Password hashing
    "pyjwt>=2.15.1,<3",         # JWT signing and verification

    # --- Database & persistence ---
    "psycopg[binary,pool]>=3.3.9,<4",  # PostgreSQL driver (ships its own libpq)
    "sqlalchemy>=2.1.8,<3",            # SQL toolkit under SQLModel
    "sqlmodel>=0.0.50",                # SQLAlchemy + Pydantic ORM

    # --- Configuration & environment ---
    "pydantic[email]>=2.14.3,<3",  # Data validation with email support
    "python-dotenv>=1.2.4",        # Load environment variables from .env files

    # --- API utilities ---
    "python-multipart>=0.0.34", # Form data support (the login form)
    "slowapi>=0.1.10",          # Rate limiting for FastAPI

    # --- Metrics & monitoring ---
    "prometheus-client>=0.26.0", # Prometheus metrics and the /metrics endpoint

    # --- Search & external tools ---
    "ddgs>=9.16.1",             # DuckDuckGo search, for the agent's web search tool

    # --- Reliability & utilities ---
    "tenacity>=9.2.1",          # Retry logic for unstable operations
    "tqdm>=4.70.1",             # Progress bars
    "colorama>=0.4.6",          # Colored terminal output

    # --- Memory / agent tooling ---
    "mem0ai>=2.2.1,<3",         # Long-term memory
]
```

You might have noticed (this matters in almost every project) that each dependency has a minimum version (`>=`), and the ones whose next major version could change an API we use also have a ceiling (`<2`). mem0 2, for example, moved the user ID of `search()` into a `filters` argument; a ceiling makes such an upgrade a deliberate step instead of a surprise. The exact versions every install gets are pinned in `uv.lock`, which `uv sync` and the Docker image install from. This is how production systems avoid **dependency hell**, where different libraries require incompatible versions of the same package.

Then comes the development dependencies section. There is a very high possibility that when you build something or if it’s in development phase, many developers are going to work on the same codebase. To ensure code quality and consistency, we need a set of development tools like linters, formatters, and type checkers.

```ini
# ==========================
# Optional Dependencies
# ==========================
# Extra dependency sets that can be installed with:
#   pip install .[dev]

[project.optional-dependencies]
dev = [
    "black",             # Code formatter
    "isort",             # Import sorter
    "flake8",            # Linting tool
    "ruff",              # Fast Python linter (modern replacement for flake8)
    "djlint==1.36.4",    # Linter/formatter for HTML & templates
]
```

Then we define dependency groups for testing. This allows us to logically group related dependencies together. For example, all testing-related libraries can be grouped under a `test` group.

```ini
# ==========================
# Dependency Groups (PEP 735-style)
# ==========================
# Logical grouping of dependencies, commonly used with modern tooling

[dependency-groups]
test = [
    "httpx>=0.28.1",     # HTTP client for testing APIs
    "pytest>=9.2.0",     # Testing framework
    "pyyaml>=6.0.3",     # The tests read docker-compose.yml
]

# ==========================
# Pytest Configuration
# ==========================
[tool.pytest.ini_options]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
]
python_files = [
    "test_*.py",
    "*_test.py",
    "tests.py",
]
testpaths = ["tests"]
pythonpath = ["."]       # so the tests can import src

# ==========================
# Black (Code Formatter)
# ==========================
[tool.black]
line-length = 119              # Maximum line length
exclude = "venv|migrations"    # Files/directories to skip

# ==========================
# Flake8 (Linting)
# ==========================
[tool.flake8]
docstring-convention = "all"  # Enforce docstring conventions
ignore = [
    "D107", "D212", "E501", "W503", "W605", "D203", "D100",
]
exclude = "venv|migrations"
max-line-length = 119

# ==========================
# Radon (Cyclomatic Complexity)
# ==========================
# Maximum allowed cyclomatic complexity
radon-max-cc = 10

# ==========================
# isort (Import Sorting)
# ==========================
[tool.isort]
profile = "black"                  # Compatible with Black
multi_line_output = "VERTICAL_HANGING_INDENT"
force_grid_wrap = 2
line_length = 119
skip = ["migrations", "venv"]

# ==========================
# Pylint Configuration
# ==========================
[tool.pylint."messages control"]
disable = [
    "line-too-long",
    "trailing-whitespace",
    "missing-function-docstring",
    "consider-using-f-string",
    "import-error",
    "too-few-public-methods",
    "redefined-outer-name",
]
[tool.pylint.master]
ignore = "migrations"

# ==========================
# Ruff (Fast Linter)
# ==========================
[tool.ruff]
line-length = 119
exclude = ["migrations", "*.ipynb", "venv"]
[tool.ruff.lint]

# Per-file ignores
[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["E402"]        # Allow imports not at top in __init__.py
```

Lets understand the remaining configuration one by one …

*   `Dependency Groups`: It allows us to create logical groups of dependencies. For example, we have a `test` group that includes libraries needed for testing and so on.
*   `Pytest Configuration`: Using this we can customize how pytest discovers and runs tests in our project.
*   `Black`: It helps us maintain consistent code formatting across the codebase.
*   `Flake8`: It is a linting tool that checks for code style violations and potential errors.
*   `Radon`: It helps us monitor cyclomatic (complexity of our code to keep it maintainable.
*   `isort`: It automatically sorts imports in our Python files to keep them organized.)

We have also defined some additional linters and configurations like `Pylint` and `Ruff` that help us catch potential issues. Following dependencies are totally optional but I highly recommend using them in production-systems because your codebase will grow in the future and without them, it might become unmanageable.

### <a id="dfa0"></a>Setting **Environment Configuration**

Now we are going to set the most common configurations which in developer language, we call it **Settings Management**.

Normally in small projects, developers use a simple `.env` file to store environment variables. But a proper settings management strategy is to name it `.env.example` and commit it to version control.

```bash
# Different environment configurations
.env.[development|staging|production] # e.g. .env.development
```

You might be wondering why not just use `.env`?

Because it allows us to maintain distinct, isolated configurations for different environments (like enabling debug mode in development but disabling it in production) simultaneously without constantly editing a single file to switch contexts.

So, let’s create a `.env.example` file and add all the necessary environment variables with placeholder values.

```bash
# ==================================================
# Application Settings
# ==================================================
APP_ENV=development              # Application environment (development | staging | production)
PROJECT_NAME="Web Assistant"    # Human-readable project name
VERSION=1.0.0                    # Application version
DEBUG=true                       # Enable debug mode (disable in production)
```

Similar to before, the very first section defines basic application settings like environment, project name, version, and debug mode.

Then comes the API settings where we define the base path for our API versioning.

```bash
# ==================================================
# API Settings
# ==================================================
API_V1_STR=/api/v1               # Base path prefix for API versioning

# ==================================================
# CORS (Cross-Origin Resource Sharing) Settings
# ==================================================
# Comma-separated list of allowed frontend origins
ALLOWED_ORIGINS="http://localhost:3000,http://localhost:8000"

# ==================================================
# Langfuse Observability Settings
# ==================================================
# Used for LLM tracing, monitoring, and analytics
LANGFUSE_PUBLIC_KEY=                                # Public Langfuse API key (empty: no tracing)
LANGFUSE_SECRET_KEY=                                # Secret Langfuse API key
LANGFUSE_HOST=https://cloud.langfuse.com            # Langfuse cloud endpoint
```

`API_V1_STR` allows us to version our API endpoints easily, this is the standard practice that we normally see many public APIs follow especially the AI model providers like OpenAI, Cohere, etc.

Then comes the `CORS Settings` which is important for web applications to control which frontend domains can access our backend API (through which we can integrate ai agents).

We are also going to use industry standard`Langfuse` for observability and monitoring of our LLM interactions. So, we need to set the necessary API keys and host URL.

```bash
# ==================================================
# LLM (Large Language Model) Settings
# ==================================================
OPENAI_API_KEY="your-llm-api-key"  # API key for LLM provider (e.g. OpenAI)
# OPENAI_BASE_URL=http://localhost:11434/v1  # Any OpenAI-compatible server (Azure, vLLM, Ollama...)
DEFAULT_LLM_MODEL=gpt-5-mini        # Default model used for chat/completions
DEFAULT_LLM_TEMPERATURE=0.2         # Controls randomness (0.0 = deterministic, 1.0 = creative)
MAX_TOKENS=2000                     # Most tokens the model may write in one answer
MAX_CONTEXT_TOKENS=16000            # Most tokens of history sent with each request

# Long-term memory (mem0): the dimensions must match the embedding model
LONG_TERM_MEMORY_MODEL=gpt-5-nano
LONG_TERM_MEMORY_EMBEDDER_MODEL=text-embedding-3-small
LONG_TERM_MEMORY_EMBEDDER_DIMS=1536

# ==================================================
# JWT (Authentication) Settings
# ==================================================
# Required. Anyone who knows it can sign in as any user, so the API refuses to start
# without a long random value. Generate one with:
#   python -c "import secrets; print(secrets.token_urlsafe(64))"
JWT_SECRET_KEY=
JWT_ALGORITHM=HS256                    # JWT signing algorithm (HS256, HS384 or HS512)
JWT_ACCESS_TOKEN_EXPIRE_DAYS=7         # Token expiration time (in days)

# ==================================================
# Database (PostgreSQL) Settings
# ==================================================
POSTGRES_HOST=db               # Database host (Docker service name or hostname)
POSTGRES_DB=mydb               # Database name
POSTGRES_USER=myuser           # Database username
POSTGRES_PORT=5432             # Database port
POSTGRES_PASSWORD=mypassword   # Database password

# Connection pooling settings
POSTGRES_POOL_SIZE=5           # Base number of persistent DB connections
POSTGRES_MAX_OVERFLOW=10       # Extra connections allowed above pool size
```

We are going to use `OpenAI` as our primary LLM provider so we need to set the API key, default model, and temperature settings. `OPENAI_BASE_URL` points the same code at any OpenAI-compatible server instead, such as Azure OpenAI, vLLM or a local Ollama.

Then comes the `JWT Settings` which plays an important role in authentication and session management. We need a secret key for signing tokens, the algorithm to encode/decode them, and the token expiration time. The secret deserves special care: every token is a signature made with it, so anyone who knows it can mint a token for any user. That is why the example leaves it empty and the API refuses to start until it holds a long random value (more on that below).

For the database, we are using `PostgreSQL` which is a industrial-strength relational database. Normally when your agentic system scales, you need to have proper connection pooling settings to avoid overwhelming the database with too many connections. Here we are setting the pool size of 5 and allowing a maximum overflow of 10 connections.

```bash
# ==================================================
# Rate Limiting Settings (SlowAPI)
# ==================================================
# Default limits for routes without their own limit (see the rate limiting section)
RATE_LIMIT_DEFAULT="1000 per day,200 per hour"

# Endpoint-specific limits
RATE_LIMIT_CHAT="100 per minute"          # Chat endpoint
RATE_LIMIT_CHAT_STREAM="100 per minute"   # Streaming chat endpoint
RATE_LIMIT_MESSAGES="200 per minute"      # Message creation endpoint
RATE_LIMIT_LOGIN="100 per minute"         # Login/auth endpoint

# ==================================================
# Logging Settings
# ==================================================
LOG_LEVEL=DEBUG                # Logging verbosity (DEBUG, INFO, WARNING, ERROR)
LOG_FORMAT=console             # Log output format (console | json)
```

Finally, we have the `Rate Limiting` and `Logging` settings to make sure our API is protected from abuse and we have proper logging for debugging and monitoring.

Now that we have our dependency management and settings management strategies in place, we are ready to start working on the core logic of our AI system and the first step to use these settings in our application code.

We need a `src/config/settings.py` file that loads these environment variables into a single `Settings` object. It is a plain Python class; `python-dotenv` reads the env files for it.

Let’s import the necessary modules first:

```python
# Importing necessary modules for configuration management
import json  # For handling JSON data
import os  # For interacting with the operating system
from enum import Enum  # For creating enumerations
from pathlib import Path  # For working with file paths
from typing import (  # For type annotations
    Any,  # Represents any type
    Dict,  # Represents a dictionary type
    List,  # Represents a list type
    Optional,  # Represents an optional value
    Union,  # Represents a union of types
)

from dotenv import load_dotenv  # For loading environment variables from .env files
```

These are some basic imports we need for file handling, type annotations, and loading environment variables from the `.env.*` files (`.env.example` is only the template you copy them from).

Next, we need to define our environment types using an enumeration.

```python
# Define environment types
class Environment(str, Enum):
    """Application environment types.
    Defines the possible environments the application can run in:
    development, staging, production, and test.
    """
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    TEST = "test"
```

Any project typically has multiple environments like development, staging, production, and test each serving a different purpose.

After defining the environment types, we need a function to determine the current environment based on an environment variable.

```python
# Determine environment
def get_environment() -> Environment:
    """Get the current environment.
       Returns:
       Environment: The current environment (development, staging, production, or test)
    """
    match os.getenv("APP_ENV", "development").lower():
        case "production" | "prod":
            return Environment.PRODUCTION
        case "staging" | "stage":
            return Environment.STAGING
        case "test":
            return Environment.TEST
        case _:
            return Environment.DEVELOPMENT
```

We can use the `APP_ENV` environment variable to determine which environment we are currently in. If it's not set, we default to `development`.

Finally, we need to load the appropriate `.env` file based on the current environment.

```python
# Load appropriate .env file based on environment
def load_env_file():
    """Load environment-specific .env file."""
    env = get_environment()
    print(f"Loading environment: {env}")
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

    # Define env files in priority order
    env_files = [
        os.path.join(base_dir, f".env.{env.value}.local"),
        os.path.join(base_dir, f".env.{env.value}"),
        os.path.join(base_dir, ".env.local"),
        os.path.join(base_dir, ".env"),
    ]
    # Load the first env file that exists
    for env_file in env_files:
        if os.path.isfile(env_file):
            load_dotenv(dotenv_path=env_file)
            print(f"Loaded environment from {env_file}")
            return env_file
    # Fall back to default if no env file found
    return None
```

We need to call this function immediately to load the environment variables when the application starts.

```python
# Call the function to load the env file
ENV_FILE = load_env_file()
```

In many cases, we have environment variables that are lists or dictionaries. So, we need utility functions to parse those values correctly.

```python
# Parse list values from environment variables
def parse_list_from_env(env_key, default=None):
    """Parse a comma-separated list from an environment variable."""
    value = os.getenv(env_key)
    if not value:
        return default or []

    # Remove quotes if they exist
    value = value.strip("\"'")

    # Handle single value case
    if "," not in value:
        return [value]

    # Split comma-separated values
    return [item.strip() for item in value.split(",") if item.strip()]

# Parse dict of lists from environment variables with prefix
def parse_dict_of_lists_from_env(prefix, default_dict=None):
    """Parse dictionary of lists from environment variables with a common prefix."""
    result = default_dict or {}

    # Look for all env vars with the given prefix
    for key, value in os.environ.items():
        if key.startswith(prefix):
            endpoint = key[len(prefix) :].lower()  # Extract endpoint name

            # Parse the values for this endpoint
            if value:
                value = value.strip("\"'")
                if "," in value:
                    result[endpoint] = [item.strip() for item in value.split(",") if item.strip()]
                else:
                    result[endpoint] = [value]
    return result
```

We are parsing comma-separated lists and dictionaries of lists from environment variables to make it easier to work with them in our code.

Now we can define our main `Settings` class that will hold all the configuration values for our application. It will read from environment variables and apply defaults where necessary.

```python
class Settings:
    """
    Centralized application configuration.
    Loads from environment variables and applies defaults.
    """

    def __init__(self):
        # Set the current environment
        self.ENVIRONMENT = get_environment()

        # ==========================
        # Application Basics
        # ==========================
        self.PROJECT_NAME = os.getenv("PROJECT_NAME", "FastAPI LangGraph Template")
        self.VERSION = os.getenv("VERSION", "1.0.0")
        self.API_V1_STR = os.getenv("API_V1_STR", "/api/v1")
        self.DEBUG = os.getenv("DEBUG", "false").lower() in ("true", "1", "t", "yes")
        
        # Parse CORS origins using our helper
        self.ALLOWED_ORIGINS = parse_list_from_env("ALLOWED_ORIGINS", ["*"])
 
        # ==========================
        # LLM & LangGraph
        # ==========================

        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
        # Any OpenAI-compatible server; always passed explicitly to the clients
        self.OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL") or "https://api.openai.com/v1"
        self.DEFAULT_LLM_MODEL = os.getenv("DEFAULT_LLM_MODEL", "gpt-5-mini")
        # Models to fall back to, in order. Unset: the built-in OpenAI list. Empty: no fallback.
        fallback_models = os.getenv("LLM_FALLBACK_MODELS")
        self.LLM_FALLBACK_MODELS = (
            None if fallback_models is None else [m.strip() for m in fallback_models.split(",") if m.strip()]
        )
        self.DEFAULT_LLM_TEMPERATURE = float(os.getenv("DEFAULT_LLM_TEMPERATURE", "0.2"))

        # Agent specific settings
        self.MAX_TOKENS = int(os.getenv("MAX_TOKENS", "2000"))  # per answer
        self.MAX_CONTEXT_TOKENS = int(os.getenv("MAX_CONTEXT_TOKENS", "16000"))  # history per request
        self.MAX_LLM_CALL_RETRIES = int(os.getenv("MAX_LLM_CALL_RETRIES", "3"))

        # ==========================
        # Observability (Langfuse)
        # ==========================
        self.LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY", "")
        self.LANGFUSE_SECRET_KEY = os.getenv("LANGFUSE_SECRET_KEY", "")
        self.LANGFUSE_HOST = os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")

        # ==========================
        # Database (PostgreSQL)
        # ==========================
        self.POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
        self.POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", "5432"))
        self.POSTGRES_DB = os.getenv("POSTGRES_DB", "food_order_db")
        self.POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
        self.POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
        
        # Pool settings are critical for high-concurrency agents
        self.POSTGRES_POOL_SIZE = int(os.getenv("POSTGRES_POOL_SIZE", "20"))
        self.POSTGRES_MAX_OVERFLOW = int(os.getenv("POSTGRES_MAX_OVERFLOW", "10"))
        
        # LangGraph persistence tables
        self.CHECKPOINT_TABLES = ["checkpoint_blobs", "checkpoint_writes", "checkpoints"]

        # ==========================
        # Security (JWT)
        # ==========================
        # Deliberately no default key: the API refuses to start until JWT_SECRET_KEY holds a
        # long random value (see check_jwt_settings below).
        self.JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "")
        self.JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
        self.JWT_ACCESS_TOKEN_EXPIRE_DAYS = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_DAYS", "7"))

        # ==========================
        # Rate Limiting
        # ==========================
        self.RATE_LIMIT_DEFAULT = parse_list_from_env("RATE_LIMIT_DEFAULT", ["200 per day", "50 per hour"])

        # Define endpoint specific limits; RATE_LIMIT_<ENDPOINT> overrides each one
        default_endpoints = {
            "chat": ["30 per minute"],
            "chat_stream": ["20 per minute"],
            "messages": ["50 per minute"],
            "register": ["10 per hour"],
            "login": ["20 per minute"],
            "root": ["10 per minute"],
            "health": ["20 per minute"],
        }
        self.RATE_LIMIT_ENDPOINTS = {
            endpoint: parse_list_from_env(f"RATE_LIMIT_{endpoint.upper()}") or limits
            for endpoint, limits in default_endpoints.items()
        }

        # Apply logic to override settings based on environment
        self.apply_environment_settings()

    def apply_environment_settings(self):
        """
        Apply defaults that depend on the active environment. A value set
        explicitly in the environment (or the env file) always wins.
        """
        env_settings = {
            Environment.DEVELOPMENT: {
                "DEBUG": True,
                "LOG_LEVEL": "DEBUG",
                "LOG_FORMAT": "console",
                "RATE_LIMIT_DEFAULT": ["1000 per day", "200 per hour"],  # relaxed locally
            },
            Environment.PRODUCTION: {
                "DEBUG": False,
                "LOG_LEVEL": "WARNING",
                "RATE_LIMIT_DEFAULT": ["200 per day", "50 per hour"],  # stricter
            },
            # ... staging and test have their own entries ...
        }
        for key, value in env_settings.get(self.ENVIRONMENT, {}).items():
            # Only override if the environment variable wasn't explicitly set
            if key not in os.environ:
                setattr(self, key, value)
```

Note the last line: the environment defaults never override a value you set. So a `.env.production` copied from `.env.example`, which sets `DEBUG=true` and `LOG_LEVEL=DEBUG` for development, keeps debug logging on in production until you change those lines.

In our `Settings` class, we read various configuration values from environment variables, applying sensible defaults where necessary. We also have an `apply_environment_settings` method that adjusts certain settings based on whether we are in development or production mode.

You can also see `CHECKPOINT_TABLES`, which lists the tables LangGraph's checkpointer keeps in PostgreSQL.

Finally, we initialize a global `settings` object that can be imported and used throughout the application.

```python
# Initialize the global settings object
settings = Settings()
```

One setting must never run with a weak value: the JWT secret. If it is missing, short, or a value someone published as an example, anyone can sign a token for any user. So `settings.py` also has a check, and the API calls it before anything else at startup and refuses to start when it fails (fail closed):

```python
# Values published as examples (in this repository, its README or the article). Anyone can
# read them, so a token signed with one of them can be forged by anyone.
KNOWN_PLACEHOLDER_SECRETS = frozenset({
    "supersecretkeythatshouldbechangedforproduction",
    "your-jwt-secret-key",
    "unsafe-secret-for-dev",
    "changeme", "change-me", "secret",
})

# RFC 7518, section 3.2: an HMAC key must be at least as long as the hash output.
JWT_MIN_SECRET_BYTES = {"HS256": 32, "HS384": 48, "HS512": 64}

def check_jwt_settings(secret: str, algorithm: str) -> Optional[str]:
    """Say why the JWT settings are unsafe, or return None when they are fine."""
    if algorithm not in JWT_MIN_SECRET_BYTES:
        return f"JWT_ALGORITHM must be one of {', '.join(JWT_MIN_SECRET_BYTES)}, not {algorithm!r}"
    if not secret:
        return "JWT_SECRET_KEY is not set"
    if secret.strip().lower() in KNOWN_PLACEHOLDER_SECRETS:
        return "JWT_SECRET_KEY is a published example value, so anyone could sign tokens with it"
    minimum = JWT_MIN_SECRET_BYTES[algorithm]
    if len(secret.encode("utf-8")) < minimum:
        return f"JWT_SECRET_KEY is shorter than {minimum} bytes, the minimum for {algorithm}"
    return None
```

Earlier versions of this guide gave the key a default in `settings.py` and in the compose file. Defaults like that are exactly how deployments end up running with a key printed in a public README, which is why there is none now.

So far, we have created a dependency management strategy and a settings management for our production-grade AI system.

### <a id="66e6"></a>**Containerization Strategy**

Now we have to create a `docker-compose.yml` file which will define all the services our application needs to function.

The reason why we are using dockerization is because in a production-grade system, components like the database, monitoring tools, and the API don’t run in isolation, they need to talk to each other and Docker Compose is the standard way to orchestrate multi-container Docker applications.

First, we have to define the Database service. Since we are building an AI agent that needs **Long-Term Memory**, a standard PostgreSQL database is not enough. We need vector similarity search capabilities.

```yaml
# ==================================================
# Docker Compose Configuration
# ==================================================
# This file defines all services required to run the
# application locally or in a single-node environment.
services:

  # ==================================================
  # PostgreSQL + pgvector Database
  # ==================================================
  db:
    image: pgvector/pgvector:pg16   # PostgreSQL 16 with pgvector extension enabled
    environment:
      - POSTGRES_DB=${POSTGRES_DB}          # Database name
      - POSTGRES_USER=${POSTGRES_USER}      # Database user
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}  # Database password
    ports:
      - "127.0.0.1:5432:5432"      # Reachable from this machine only (the app uses db:5432)
    volumes:
      - postgres-data:/var/lib/postgresql/data  # Persistent database storage
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: always
    networks:
      - monitoring
```

We are explicitly using the `pgvector/pgvector:pg16` image instead of the standard `postgres` image. This gives us the pgvector extension out-of-the-box, which `mem0ai` needs to store long-term memory as vectors (LangGraph's checkpointer only needs plain PostgreSQL).

We also include a `healthcheck` this is important in deployment because our API service needs to wait until the database is fully ready to accept connections before it tries to start up.

Next, we define our main Application service. This is where our FastAPI code runs.

```yaml
# ==================================================
  # FastAPI Application Service
  # ==================================================
  app:
    build:
      context: .                     # Build image from project root
      args:
        APP_ENV: ${APP_ENV:-development}  # Build-time environment
    ports:
      - "8000:8000"                # Expose FastAPI service
    volumes:
      - app-logs:/app/logs           # Persist application logs
    # Every open connection is a file descriptor; Docker's default soft limit
    # inside a container (1024) fails requests past ~1000 concurrent clients
    ulimits:
      nofile:
        soft: 65536
        hard: 65536
    # Every setting, including JWT_SECRET_KEY, comes from this file. There is
    # deliberately no fallback secret: the API refuses to start without a strong one.
    env_file:
      - .env.${APP_ENV:-development} # Load environment-specific variables
    environment:
      - APP_ENV=${APP_ENV:-development}
    depends_on:
      db:
        condition: service_healthy   # Wait until DB is ready
    healthcheck:
      # The slim Python image has no curl, so the check is a line of Python
      test: ["CMD", "python", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8000/health', timeout=5)"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 20s
    restart: on-failure
    networks:
      - monitoring
```

Notice what is *not* here. The container receives its settings from the env file at runtime, and the image never contains them (`.dockerignore` keeps `.env.*` files out of it). The `environment` section sets no secret either. An earlier version of this file set `JWT_SECRET_KEY=${JWT_SECRET_KEY:-supersecretkey...}` there. Compose fills in that default whenever it cannot see the variable itself, as with a plain `docker compose up`, which reads `.env` but not `.env.development`. And because `environment` wins over `env_file`, the published default silently replaced the key you had put in the env file.

The logs go to a named volume, which Docker creates with the ownership the image gives `/app/logs`, so the non-root user in the container can write to it. For hot reloading while you develop, run the API outside Docker with `make dev` (uvicorn with `--reload`); the container runs the code it was built with.

Now, a production system is flying blind without observability. The dev team need to know if their API is slow or if errors are spiking. For this, we use the `Prometheus + Grafana` stack.

```yaml
  # ==================================================
  # Prometheus (Metrics Collection)
  # ==================================================
  prometheus:
    image: prom/prometheus:v3.16.0   # pinned: "latest" changes under you on the next pull
    ports:
      - "127.0.0.1:9090:9090"       # Prometheus UI, from this machine only
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
    networks:
      - monitoring
    restart: always
```

Prometheus is the “collector” it scrapes metrics from our FastAPI app (like request latency or error rates) every few seconds. We mount a configuration file so we can tell it exactly where to look for our app.

Then we add Grafana, which is the “visualizer”.

```yaml
  # ==================================================
  # Grafana (Metrics Visualization)
  # ==================================================
  grafana:
    image: grafana/grafana:13.3.1
    ports:
      - "127.0.0.1:3000:3000"       # Grafana UI, from this machine only
    volumes:
      - grafana-storage:/var/lib/grafana
      - ./grafana/dashboards:/etc/grafana/provisioning/dashboards
      - ./grafana/dashboards/dashboards.yml:/etc/grafana/provisioning/dashboards/dashboards.yml
      - ./grafana/datasources:/etc/grafana/provisioning/datasources
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_ADMIN_PASSWORD:-admin}  # set it in the env file
      - GF_USERS_ALLOW_SIGN_UP=false
    networks:
      - monitoring
    restart: always
```

Grafana takes the raw data from Prometheus and turns it into beautiful charts. By mounting the `./grafana/dashboards` volume, we can "provision" our dashboards as code. This means when you spin up the container, your charts are already there, no manual setup required.

Finally, the third important piece is to track the health of the containers themselves (CPU usage, Memory leaks, etc.). For this, we use `cAdvisor`. It's a lightweight monitoring agent developed by Google that provides real-time insights into container resource usage and performance.

```yaml
  # ==================================================
  # cAdvisor (Container Metrics)
  # ==================================================
  cadvisor:
    image: gcr.io/cadvisor/cadvisor:v0.55.1
    ports:
      - "127.0.0.1:8080:8080"       # cAdvisor UI, from this machine only
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:rw
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro
    networks:
      - monitoring
    restart: always

# ==================================================
# Networks & Volumes
# ==================================================
networks:
  monitoring:
    driver: bridge                  # Shared network for all services
volumes:
  app-logs:                         # Persist application logs
  grafana-storage:                  # Persist Grafana dashboards & data
  postgres-data:                    # Persist PostgreSQL data
```

We wrap everything up by defining a shared `monitoring` network so all these services can talk to each other, and named `volumes` to ensure our database and dashboard settings survive even if we restart the containers.

Only the API's port is published to the outside. PostgreSQL, Prometheus, Grafana and cAdvisor listen on `127.0.0.1`, so on a server they are reachable through an SSH tunnel and not from the internet. A database or dashboard port open to the world is one of the most common ways small deployments get breached.

## <a id="c31d"></a>Building Data Persistence Layer

We have a running database but it is currently empty. An AI system relies heavily on **Structured Data**. We aren’t just throwing JSON blobs into a NoSQL store, we need strict relationships between Users, their Chat Sessions, and the AI’s State.

![Data Persistence Layer](https://miro.medium.com/v2/resize:fit:1250/1*mCc2WO9byzqBdsvda73Rhg.png)
*Data Persistence Layer (Created by Fareed Khan)*

To handle this, we are going to use **SQLModel**. It is a library that combines **SQLAlchemy** (for database interaction) and **Pydantic** (for data validation).

### <a id="49d1"></a>**Structured Modeling**

**SQLModel** is also among the most modern ORMs available in Python, Let’s start defining our data models.

In software engineering, **Don’t Repeat Yourself (DRY)** is a core principle. Since almost every table in our database will need a timestamp to track when a record was created, we shouldn’t copy-paste that logic into every file. instead, we create a `BaseModel`.

![Structured Modeling](https://miro.medium.com/v2/resize:fit:875/1*5cuOQQn4h0tPyKG-hn9CFA.png)
*Structured Modeling (Created by Fareed Khan)*

For that, create `src/data/models/base.py` file which will hold our abstract base model:

```python
from datetime import datetime, UTC
from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship

# ==================================================
# Base Database Model
# ==================================================
class BaseModel(SQLModel):
    """
    Abstract base model that adds common fields to all tables.
    Using an abstract class ensures consistency across our schema.
    """
    
    # Always use UTC in production to avoid timezone headaches
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
```

This class is pretty straightforward. It adds a `created_at` timestamp to any model that inherits from it.

Now we can build our core entities. The most fundamental requirement for any user-facing system is **Authentication**. We need a good User model that handles credentials securely.

### <a id="da20"></a>**Entity Definition**

Similar to how api based ai models providers handle user data, we will create a `User` model with email and hashed password fields.

![Entity Definition](https://miro.medium.com/v2/resize:fit:875/1*6xN_OBlno3BUyj-g7ur9ig.png)
*Entity Definition (Created by Fareed Khan)*

Create `src/data/models/user.py` file to define the User model:

```python
from typing import TYPE_CHECKING, List
import bcrypt
from sqlmodel import Field, Relationship
from src.data.models.base import BaseModel

# Prevent circular imports for type hinting
if TYPE_CHECKING:
    from src.data.models.session import Session

# ==================================================
# User Model
# ==================================================
class User(BaseModel, table=True):
    """
    Represents a registered user in the system.
    """
    
    # Primary Key
    id: int = Field(default=None, primary_key=True)
    
    # Email must be unique and indexed for fast lookups during login
    email: str = Field(unique=True, index=True)
    
    # NEVER store plain text passwords. We store the Bcrypt hash.
    hashed_password: str
    
    # Relationship: One user has many chat sessions
    sessions: List["Session"] = Relationship(back_populates="user")
    def verify_password(self, password: str) -> bool:
        """
        Verifies a raw password against the stored hash.
        """
        return password_matches(password, self.hashed_password)
    @staticmethod
    def hash_password(password: str) -> str:
        """
        Generates a secure Bcrypt hash/salt for a new password.
        """
        secret = password.encode("utf-8")
        # bcrypt only reads the first 72 bytes; refuse longer passwords instead of cutting them
        if len(secret) > BCRYPT_MAX_BYTES:
            raise ValueError(f"Password must be at most {BCRYPT_MAX_BYTES} bytes long")
        return bcrypt.hashpw(secret, bcrypt.gensalt()).decode("utf-8")


BCRYPT_MAX_BYTES = 72

def password_matches(password: str, hashed_password: str) -> bool:
    """
    Check a password against a bcrypt hash. bcrypt 5 raises on more than 72 bytes where
    older versions cut silently, so cut here to keep accepting accounts created back then.
    """
    return bcrypt.checkpw(password.encode("utf-8")[:BCRYPT_MAX_BYTES], hashed_password.encode("utf-8"))
```

We embedded the password hashing logic directly into the model. This is an implementation of **Encapsulation** the logic for handling user data lives *with* the user data, preventing security mistakes elsewhere in the app.

bcrypt is slow on purpose (a quarter of a second of CPU per hash is normal), which is what makes stolen hashes expensive to crack. It also means the API must not call it on the event loop, or every other request waits while a password is checked. The endpoints below run it in a thread pool of its own, one thread short of the number of cores, so that even a burst of logins leaves a core for everything else.

Next, we need to organize our AI interactions. Users don’t just have one giant endless conversation, they have distinct **Sessions** (or “Chats”). For that we need to create `src/data/models/session.py`.

```python
from typing import TYPE_CHECKING, List
from sqlmodel import Field, Relationship
from src.data.models.base import BaseModel

if TYPE_CHECKING:
    from src.data.models.user import User

# ==================================================
# Session Model
# ==================================================
class Session(BaseModel, table=True):
    """
    Represents a specific chat conversation/thread.
    This links the AI's memory to a specific context.
    """
    
    # We use String IDs (UUIDs) for sessions to make them hard to guess
    id: str = Field(primary_key=True)
    
    # Foreign Key: Links this session to a specific user (indexed: we list sessions by user)
    user_id: int = Field(foreign_key="user.id", index=True)
    
    # Optional friendly name for the chat (e.g., "Recipe Ideas")
    name: str = Field(default="")
    
    # Relationship link back to the User
    user: "User" = Relationship(back_populates="sessions")
```

This creates a `Session` model that links to the `User` model via a foreign key. Each session represents a distinct conversation context for the AI.

### <a id="0bdf"></a>**Data Transfer Objects (DTOs)**

Finally, we need a model for **LangGraph Persistence**. LangGraph is stateful, if the server restarts, we don’t want the AI to forget what step it was on.

![DTOs](https://miro.medium.com/v2/resize:fit:1250/1*OTpUnG6hUc3TEnAnyoiGig.png)
*DTOs (Created by Fareed Khan)*

We need a `Thread` model that acts as an anchor for these checkpoints. Create `src/data/models/thread.py`.

```python
from datetime import UTC, datetime
from sqlmodel import Field, SQLModel

# ==================================================
# Thread Model (LangGraph State)
# ==================================================
class Thread(SQLModel, table=True):
    """
    Acts as a lightweight anchor for LangGraph checkpoints.
    The actual state blob is stored by the AsyncPostgresSaver,
    but we need this table to validate thread existence.
    """
    id: str = Field(primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
```

The application does not import this model yet, so the table is not created; the checkpointer keeps the state in its own tables either way. The SQL for the tables the application does create is in [`schema.sql`](schema.sql), and a test keeps it in step with the models.

To keep our imports clean in the rest of the application, we aggregate these models into a single entry point and that exist in our `src/data/models/database.py`.

```python
"""
Database Models Export.
This allows simple imports like: `from src.data.models.database import Thread`
"""
from src.data.models.thread import Thread

# Explicitly define what is exported
__all__ = ["Thread"]
```

Now that we have our database structure, we need to address **Data Transfer**.

A common mistake in beginner API development is exposing your database models directly to the user. This is dangerous (it leaks internal fields like `hashed_password`) and rigid. In production systems, we use **Schemas** (often called DTOs - Data Transfer Objects).

These schemas define the “contract” between your API and the outside world.

Let’s define the schemas for **Authentication**. We need strict validation here passwords must meet complexity requirements, and emails must be valid formats. For that we need to have a separate auth schema file so we should create `src/data/schemas/auth.py`.

```python
import re
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, SecretStr, field_validator

# ==================================================
# Authentication Schemas
# ==================================================
class UserCreate(BaseModel):
    """
    Schema for user registration inputs.
    """
    email: EmailStr = Field(..., description="User's email address")
    # SecretStr prevents the password from being logged in tracebacks
    password: SecretStr = Field(..., description="User's password", min_length=8, max_length=64)
    @field_validator("password")
    @classmethod
    def validate_password(cls, v: SecretStr) -> SecretStr:
        """
        Enforce strong password policies.
        """
        password = v.get_secret_value()
        
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search(r"[A-Z]", password):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[0-9]", password):
            raise ValueError("Password must contain at least one number")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValueError("Password must contain at least one special character")
        # bcrypt reads only the first 72 bytes, and non-ASCII characters take several bytes each
        if len(password.encode("utf-8")) > 72:
            raise ValueError("Password must be at most 72 bytes long")

        return v

class Token(BaseModel):
    """
    Schema for the JWT Access Token response.
    """
    access_token: str = Field(..., description="The JWT access token")
    token_type: str = Field(default="bearer", description="The type of token")
    expires_at: datetime = Field(..., description="The token expiration timestamp")

class UserResponse(BaseModel):
    """
    Public user profile schema (safe to return to frontend).
    Notice we exclude the password here.
    """
    id: int
    email: str
    token: Token
```

Next, we define the schemas in `src/data/schemas/chat.py` for the **Chat Interface**. This handles the input message from the user and the streaming response from the AI.

```python
import re
from typing import List, Literal, Optional
from pydantic import BaseModel, Field, field_validator

# ==================================================
# Chat Schemas
# ==================================================
class Message(BaseModel):
    """
    A message sent by the client. The server keeps the conversation (LangGraph's
    checkpointer), so a request only carries the new user turn. Accepting "system" or
    "assistant" here would let any client replace the system prompt or put words in
    the assistant's mouth.
    """
    role: Literal["user"] = Field(..., description="Only user messages are accepted")
    content: str = Field(..., description="The message content", min_length=1, max_length=3000)
    @field_validator("content")
    @classmethod
    def validate_content(cls, v: str) -> str:
        """
        Sanitization: Prevent basic XSS or injection attacks.
        """
        if re.search(r"<script.*?>.*?</script>", v, re.IGNORECASE | re.DOTALL):
            raise ValueError("Content contains potentially harmful script tags")
        return v

class ChatMessage(BaseModel):
    """
    A message of the conversation as the API returns it. No length limit: the 3000
    characters apply to what clients send, and the assistant's answers are often longer.
    """
    role: Literal["user", "assistant"]
    content: str

class ChatRequest(BaseModel):
    """
    Payload sent to the /chat endpoint.
    """
    messages: List[Message] = Field(..., min_length=1)

class ChatResponse(BaseModel):
    """
    Standard response from the /chat endpoint.
    """
    messages: List[ChatMessage]

class StreamResponse(BaseModel):
    """
    Chunk format for Server-Sent Events (SSE) streaming.
    """
    content: str = Field(default="")
    done: bool = Field(default=False)
    error: Optional[str] = Field(default=None)  # set on the last event if the answer failed
```

Note the two message models. An earlier version used one `Message` for both directions, so the 3000-character limit meant for requests also applied to the assistant's answers: any answer longer than that made the endpoint fail with a 500, and so did every later attempt to load that conversation's history.

Finally, we need a schema for **LangGraph State**. LangGraph works by passing a state object between nodes (Agents, Tools, Memory). We need to explicitly define what that state looks like. Let’s create `src/data/schemas/graph.py`:

```python
from typing import Annotated
from langgraph.graph.message import add_messages
from pydantic import BaseModel, Field

# ==================================================
# LangGraph State Schema
# ==================================================
class GraphState(BaseModel):
    """
    The central state object passed between graph nodes.
    """
    
    # 'add_messages' is a reducer. It tells LangGraph:
    # "When a new message comes in, append it to the list rather than overwriting it."
    messages: Annotated[list, add_messages] = Field(
        default_factory=list, 
        description="The conversation history"
    )
    
    # Context retrieved from Long-Term Memory (mem0ai)
    long_term_memory: str = Field(
        default="", 
        description="Relevant context extracted from vector store"
    )
```

With our **Models** (Database Layer) and **Schemas** (API Layer) strictly defined, we have built a type-safe foundation for our application. We can now be confident that bad data won’t corrupt our database, and sensitive data won’t leak to our users.

## <a id="1942"></a>Security & Safeguards Layer

In a production environment, you cannot trust user input, and you cannot allow unlimited access to your resources.

You have also see in many API providers like together.ai, you see limited requests per minute to prevent abuse. This helps protect your infrastructure and control costs.

![Security Layer](https://miro.medium.com/v2/resize:fit:1250/1*p41dMjj4EpofqMYciu2noQ.png)
*Security Layer (Created by Fareed Khan)*

If you deploy an AI agent without safeguards, two things will happen:

1.  **Abuse:** Bots will hammer your API, driving up your OpenAI bill.
2.  **Security Exploits:** Malicious users will attempt injection attacks.

### <a id="1649"></a>Rate Limiting Feature

We need to implement **Rate Limiting** and **Sanitization utilities** before we write our business logic.

![Rate Limit test](https://miro.medium.com/v2/resize:fit:875/1*Q77Wxu2NrSShL9A_PHGPDA.png)
*Rate Limit test (Created by Fareed Khan)*

First, let’s look at Rate Limiting. We are going to use `SlowAPI`, a library that integrates easily with FastAPI. We need to define *how* we identify a unique user (usually by IP address) and pass the default limits we defined in our settings earlier. Let's create a `src/system/rate_limit.py` for this:

```python
from slowapi import Limiter
from slowapi.util import get_remote_address
from src.config.settings import settings

# ==================================================
# Rate Limiter Configuration
# ==================================================
# We initialize the Limiter using the remote address (IP) as the key.
# you might need to adjust `key_func` to look at X-Forwarded-For headers.
limiter = Limiter(
    key_func=get_remote_address, 
    default_limits=settings.RATE_LIMIT_DEFAULT
)
```

This way we can later decorate any specific API route with `@limiter.limit(...)` to apply granular control.

One detail of SlowAPI is worth knowing: the decorated routes are the ones it limits. The `default_limits` apply to the other routes only through `SlowAPIMiddleware`, which this application does not add, so the routes without a decorator (the session endpoints, `/api/v1/health` and `/metrics`) have no limit. To limit every route, add `app.add_middleware(SlowAPIMiddleware)` and exempt the endpoints that are polled on a schedule, or Prometheus and the health checks will hit the default limits first (`@limiter.exempt`).

### <a id="ed53"></a>Sanitization Check Logic

Next, we need **Sanitization**. Even though modern frontend frameworks handle a lot of XSS (Cross-Site Scripting) protection, a backend API should never blindly trust incoming strings.

![Sanitization Check](https://miro.medium.com/v2/resize:fit:875/1*1t7zcACiaGjfp9-d1whZdw.png)
*Sanitization Check (Created by Fareed Khan)*

We need a utility function to sanitize strings. We will create `src/utils/sanitization.py` for this step:

```ruby
import html
import re
from typing import Any, Dict, List

# ==================================================
# Input Sanitization Utilities
# ==================================================
def sanitize_string(value: str) -> str:
    """
    Sanitize a string to prevent XSS and other injection attacks.
    """
    if not isinstance(value, str):
        value = str(value)
    # 1. HTML Escape: Converts <script> to &lt;script&gt;
    value = html.escape(value)
    # 2. Aggressive Scrubbing: Remove script tags entirely if they slipped through
    # (This is a defense-in-depth measure)
    value = re.sub(r"&lt;script.*?&gt;.*?&lt;/script&gt;", "", value, flags=re.DOTALL)
    # 3. Null Byte Removal: Prevents low-level binary exploitation attempts
    value = value.replace("\0", "")
    return value

def sanitize_email(email: str) -> str:
    """
    Sanitize and validate an email address format.
    """
    # Basic cleaning
    email = sanitize_string(email)
    # Regex validation for standard email format
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        raise ValueError("Invalid email format")
    return email.lower()
```

We defined the *Schema* for our tokens earlier, but now we need the logic to actually **Mint** (create) and **Verify** them.

For that we are going to use **JSON Web Tokens (JWT)**. The signature proves a token is genuine without a database lookup: whoever holds the secret key can tell a token we issued from a forged one. We still look up the user or session behind the token on each request, so deleting one takes effect immediately. So, let’s create `src/utils/auth.py`.

There are two kinds of tokens. A **user token** comes from registering or logging in and says who the user is. A **session token** comes from creating a chat session and gives access to that one conversation. Each endpoint accepts one kind, so a token gets a `type` claim; without it, a session token's subject (a session ID) and a user token's subject (a user ID) would be interchangeable strings.

```python
import uuid
from datetime import UTC, datetime, timedelta
from typing import Any, Dict, Literal, Optional

import jwt  # PyJWT

from src.config.settings import check_jwt_settings, settings
from src.data.schemas.auth import Token
from src.system.logs import logger

TokenType = Literal["user", "session"]

# ==================================================
# JWT Authentication Utilities
# ==================================================
def _signing_key() -> str:
    """Return JWT_SECRET_KEY, refusing to sign or verify anything with an unsafe key."""
    problem = check_jwt_settings(settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM)
    if problem:
        raise RuntimeError(problem)
    return settings.JWT_SECRET_KEY


def create_access_token(subject: str, token_type: TokenType, expires_delta: Optional[timedelta] = None) -> Token:
    """
    Creates a new JWT access token.

    Args:
        subject: The user ID for a user token, the session ID for a session token
        token_type: "user" or "session"
        expires_delta: Optional custom expiration time
    """
    now = datetime.now(UTC)
    expire = now + (expires_delta or timedelta(days=settings.JWT_ACCESS_TOKEN_EXPIRE_DAYS))
    # The payload is what gets encoded into the token
    to_encode = {
        "sub": subject,          # Subject (standard claim)
        "type": token_type,      # Which endpoints accept it
        "iat": now,              # Issued At (standard claim)
        "exp": expire,           # Expiration time (standard claim)
        "jti": uuid.uuid4().hex, # JWT ID: a unique identifier for this token
    }
    encoded_jwt = jwt.encode(to_encode, _signing_key(), algorithm=settings.JWT_ALGORITHM)
    return Token(access_token=encoded_jwt, expires_at=expire)


def decode_token(token: str) -> Optional[Dict[str, Any]]:
    """
    Returns the claims of a token whose signature and expiry check out, or None.
    """
    try:
        return jwt.decode(
            token,
            _signing_key(),
            algorithms=[settings.JWT_ALGORITHM],  # never accept the algorithm the token names
            options={"require": ["sub", "type", "iat", "exp"]},
        )
    except jwt.InvalidTokenError:
        # Bad signature, expired, malformed, or missing a claim
        return None


def verify_token(token: str, token_type: TokenType) -> Optional[str]:
    """
    Verifies a token and returns its subject, or None if it is invalid, expired,
    or of the other type.
    """
    claims = decode_token(token)
    if claims is None or claims.get("type") != token_type:
        logger.warning("token_rejected", expected=token_type)
        return None
    return claims["sub"]
```

We use [PyJWT](https://pyjwt.readthedocs.io/) here; earlier versions used `python-jose`, which is far less maintained.

Now that we have authentication and sanitization utilities, we can focus on preparing messages for the LLM context window.

### <a id="2115"></a>**Context Management**

One of the hardest parts of scaling AI apps is **Context Window Management**. If you keep appending messages to a chat history forever, eventually you will hit the token limit of the model (or your wallet).

> A production system needs to know how to “trim” messages intelligently.

![Context Management](https://miro.medium.com/v2/resize:fit:875/1*9l6m-J1-7tzquFSxSt_uaA.png)
*Context Management (Created by Fareed Khan)*

We also need to handle the quirky output formats of newer models. For example, some reasoning models return **Thought Blocks** separate from the actual text. For that we need to create `src/utils/graph.py`.

```python
from typing import Any

from langchain_core.messages import BaseMessage, SystemMessage
from langchain_core.messages import trim_messages as _trim_messages
from langchain_core.messages.utils import count_tokens_approximately
from src.config.settings import settings

# ==================================================
# LangGraph / LLM Utilities
# ==================================================
def dump_messages(messages: list) -> list[dict]:
    """
    Converts Pydantic Message models (or LangChain messages) into the dictionary
    format expected by OpenAI/LangChain.
    """
    return [message.model_dump() for message in messages]

def message_text(content: Any) -> str:
    """
    Returns the text of a message's content. Most models return a string; some (GPT-5
    through the Responses API, for one) return a list of blocks such as
    [{'type': 'reasoning', ...}, {'type': 'text', 'text': '...'}], of which only the
    text blocks are meant for the user.
    """
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "".join(
            block if isinstance(block, str) else block.get("text", "")
            for block in content
            if isinstance(block, str) or (isinstance(block, dict) and block.get("type") == "text")
        )
    return ""

def prepare_messages(messages: list, system_prompt: str) -> list:
    """
    Prepares the message history for the LLM context window.

    CRITICAL: This function prevents token overflow errors. It keeps the System
    Prompt + the most recent messages that fit within 'settings.MAX_CONTEXT_TOKENS'.
    """
    trimmed_messages = _trim_messages(
        dump_messages(messages),
        strategy="last",            # Keep the most recent messages
        token_counter=count_tokens_approximately,  # About four characters per token
        max_tokens=settings.MAX_CONTEXT_TOKENS,
        start_on="human",           # Ensure history doesn't start with a hanging AI response
        include_system=False,       # We append system prompt manually below
        allow_partial=False,
    )
    # Always prepend the system prompt to enforce agent behavior
    return [SystemMessage(content=system_prompt)] + trimmed_messages

def process_llm_response(response: BaseMessage) -> BaseMessage:
    """
    Flattens structured content (reasoning and text blocks) into the text the user sees.
    """
    if isinstance(response.content, list):
        response.content = message_text(response.content)
    return response
```

By adding `prepare_messages`, we are making sure that our application won't crash even if a user has a conversation with 500 messages. The system automatically forgets the oldest context to make room for the new, keeping our costs and errors under control.

Two details matter here. The budget is its own setting, `MAX_CONTEXT_TOKENS`: an earlier version trimmed to `MAX_TOKENS`, the 2000-token cap on one *answer*, so a single long answer pushed everything before it out of the context and the agent forgot the conversation. And tokens are estimated rather than counted with the model's tokenizer, which works the same for every model (including ones served through `OPENAI_BASE_URL`), needs no tokenizer download, and cannot fail on content blocks a tokenizer does not know.

Once we have configured our dependencies, settings, models, schemas, security, and utilities, we need to build our **Service Layer** which is responsible for the core business logic of our application.

## <a id="9ef9"></a>The Service Layer for AI Agents

In a well-architected application, API routes (Controllers) should be simple. They shouldn’t contain complex business logic or raw database queries. Instead, that work belongs in services, which makes the code easier to test, reuse, and maintain.

![Service Layer](https://miro.medium.com/v2/resize:fit:1250/1*Ks7aNfaEtf8aLRDfMGlD7A.png)
*Service Layer (Created by Fareed Khan)*

Connecting to a database in a script is easy. Connecting to a database in a high-concurrency API serving thousands of users is hard. If you open a new connection for every request, your database will crash under load.

### <a id="c497"></a>Connection Pooling

To solve this, we are going to use **Connection Pooling**. We keep a pool of open connections ready to use, minimizing the overhead of the “handshake” process.

![Connection Pool](https://miro.medium.com/v2/resize:fit:875/1*9GQ9H6JV3Kb_-aWNz6zD6Q.png)
*Connection Pool (Creation by Fareed Khan)*

Let’s create `src/data/db_manager.py` for this:

```python
import asyncio
from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy import URL, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.pool import QueuePool
from sqlmodel import Session, SQLModel, create_engine, select

from src.config.settings import Environment, settings
from src.system.logs import logger
from src.data.models.session import Session as ChatSession
from src.data.models.user import User

# ==================================================
# Database Service
# ==================================================
class DatabaseService:
    """
    Singleton service handling all database interactions.
    Manages the connection pool and provides clean CRUD interfaces.
    """
    def __init__(self):
        """
        Initialize the engine with robust pooling settings.
        """
        try:
            # URL.create escapes the credentials, so passwords containing @, / or : work
            connection_url = URL.create(
                "postgresql+psycopg",
                username=settings.POSTGRES_USER,
                password=settings.POSTGRES_PASSWORD,
                host=settings.POSTGRES_HOST,
                port=settings.POSTGRES_PORT,
                database=settings.POSTGRES_DB,
            )
            # Configuring the QueuePool is critical for production.
            # pool_size: How many connections to keep open permanently.
            # max_overflow: How many temporary connections to allow during spikes.
            self.engine = create_engine(
                connection_url,
                pool_pre_ping=True,  # Check if connection is alive before using it
                poolclass=QueuePool,
                pool_size=settings.POSTGRES_POOL_SIZE,
                max_overflow=settings.POSTGRES_MAX_OVERFLOW,
                pool_timeout=30,     # Fail if no connection available after 30s
                pool_recycle=1800,   # Recycle connections every 30 mins to prevent stale sockets
            )
            # Create tables if they don't exist (Code-First migration)
            SQLModel.metadata.create_all(self.engine)
            logger.info("database_initialized", pool_size=settings.POSTGRES_POOL_SIZE)
        
        except SQLAlchemyError as e:
            logger.error("database_initialization_failed", error=str(e))
            # In Dev, we might want to crash. In Prod, maybe we want to retry.
            if settings.ENVIRONMENT != Environment.PRODUCTION:
                raise
    # --------------------------------------------------
    # User Management
    # --------------------------------------------------
    # SQLModel sessions are synchronous. Each method runs its queries in a worker thread
    # (asyncio.to_thread): run directly in an async endpoint, a query would block the
    # event loop, and with it every other request, until the database answers.
    async def create_user(self, email: str, password: str) -> User:
        """Create a new user with hashed password."""
        def _create() -> User:
            with Session(self.engine) as session:
                user = User(email=email, hashed_password=password)
                session.add(user)
                session.commit()
                session.refresh(user)
                return user
        return await asyncio.to_thread(_create)

    async def get_user_by_email(self, email: str) -> Optional[User]:
        """Fetch user by email for login flow."""
        def _get() -> Optional[User]:
            with Session(self.engine) as session:
                return session.exec(select(User).where(User.email == email)).first()
        return await asyncio.to_thread(_get)

    # --------------------------------------------------
    # Session Management
    # --------------------------------------------------
    async def create_session(self, session_id: str, user_id: int, name: str = "") -> ChatSession:
        """Create a new chat session linked to a user."""
        def _create() -> ChatSession:
            with Session(self.engine) as session:
                chat_session = ChatSession(id=session_id, user_id=user_id, name=name)
                session.add(chat_session)
                session.commit()
                session.refresh(chat_session)
                return chat_session
        return await asyncio.to_thread(_create)

    async def delete_session(self, session_id: str) -> bool:
        """Delete a session and the conversation LangGraph stored for it."""
        def _delete() -> bool:
            with Session(self.engine) as session:
                chat_session = session.get(ChatSession, session_id)
                if not chat_session:
                    return False
                session.delete(chat_session)
                # The checkpointer keys the conversation by thread_id, which is the session ID
                connection = session.connection()
                for table in settings.CHECKPOINT_TABLES:
                    if connection.execute(text("SELECT to_regclass(:t)"), {"t": table}).scalar():
                        connection.execute(text(f"DELETE FROM {table} WHERE thread_id = :id"), {"id": session_id})
                session.commit()
                return True
        return await asyncio.to_thread(_delete)

    # get_user, get_session, get_user_sessions, update_session_name and
    # health_check follow the same pattern; see src/data/db_manager.py.

# Create a global singleton instance
db_manager = DatabaseService()
```

Here, `pool_pre_ping=True` is important. Databases sometimes close idle connections silently. Without this flag, your API would throw a "Broken Pipe" error on the first request after a quiet period. With it, SQLAlchemy checks the connection health before handing it to you.

We are also setting the `pool_recycle` to 30 minutes. Some cloud providers (like AWS RDS) automatically close connections after a certain idle time. Recycling connections prevents this issue.

The other components are simple CRUD methods for users and chat sessions. Deleting a session also deletes the messages LangGraph stored for it: a user who deletes a chat expects the conversation to be gone, not just its entry in a list.

### <a id="2fe7"></a>LLM Unavailability Handling

Relying on a single AI model (like GPT-4) is a risk. What if OpenAI goes down? What if you hit a rate limit? A production system needs **Resilience** and **Fallbacks** to ensure high availability.

![LLM Check](https://miro.medium.com/v2/resize:fit:875/1*42G1vS33RD-siCxCnrjFzw.png)
*LLM Check (Created by Fareed Khan)*

We are going to implement two advanced patterns here:

1.  **Automatic Retries:** If a request fails due to a network blip, try again.
2.  **Circular Fallback:** If `gpt-4o` is down, automatically switch to `gpt-4o-mini` or another backup model.

We will use the `tenacity` library which is used for exponential backoff retries and `LangChain` for model abstraction. Let's create `src/services/llm_provider.py`:

```python
import logging
from typing import Any, Dict, List, Optional
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI
from openai import (
    APIConnectionError,
    APITimeoutError,
    InternalServerError,
    OpenAIError,
    RateLimitError,
)
from tenacity import (
    before_sleep_log,
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)


from src.config.settings import settings
from src.system.logs import logger

# ==================================================
# LLM Registry
# ==================================================
class LLMRegistry:
    """
    Registry of available LLM models.
    This allows us to switch "Brains" on the fly without changing code.
    """
    
    # We pre-configure models with different capabilities/costs
    LLMS: List[Dict[str, Any]] = [
        {
            "name": "gpt-5-mini",
            "llm": ChatOpenAI(
                model="gpt-5-mini",
                api_key=settings.OPENAI_API_KEY,
                base_url=settings.OPENAI_BASE_URL,
                max_tokens=settings.MAX_TOKENS,
                # New "reasoning" feature in newer models
                reasoning={"effort": "low"},
            ),
        },
        # ... gpt-5 (reasoning effort "medium"), gpt-5-nano ("minimal") and gpt-4o
        #     (temperature, top_p and penalties) follow the same pattern ...
        {
            "name": "gpt-4o-mini", # Cheaper fallback
            "llm": ChatOpenAI(
                model="gpt-4o-mini",
                temperature=settings.DEFAULT_LLM_TEMPERATURE,
                api_key=settings.OPENAI_API_KEY,
                base_url=settings.OPENAI_BASE_URL,
                max_tokens=settings.MAX_TOKENS,
            ),
        },
    ]
    @classmethod
    def get(cls, model_name: str, **kwargs) -> BaseChatModel:
        """
        Retrieve a model by name. A name that is not in LLMS gets a plain ChatOpenAI
        instance, so any model the configured endpoint serves can be used.
        """
        entry = next((e for e in cls.LLMS if e["name"] == model_name), None)
        if entry is None or kwargs:
            options = {"temperature": settings.DEFAULT_LLM_TEMPERATURE, "max_tokens": settings.MAX_TOKENS, **kwargs}
            return ChatOpenAI(model=model_name, api_key=settings.OPENAI_API_KEY, base_url=settings.OPENAI_BASE_URL, **options)
        return entry["llm"]
    @classmethod
    def get_all_names(cls) -> List[str]:
        return [entry["name"] for entry in cls.LLMS]
```

In this registry, we define multiple models with different capabilities and costs. This allows us to switch between them dynamically if needed. Because every client gets `base_url=settings.OPENAI_BASE_URL`, the same code runs against Azure OpenAI, vLLM or a local Ollama: set the URL, and set `DEFAULT_LLM_MODEL` to a model that server has.

Next, we build the `LLMService` which is responsible for all LLM interactions and also handles retries and fallbacks:

```python
# ==================================================
# LLM Service (The Resilience Layer)
# ==================================================

# Worth retrying on the same model: the request may succeed a few seconds later.
# Anything else (a bad request, a missing model, a wrong key) goes straight to the next model.
RETRYABLE_ERRORS = (RateLimitError, APITimeoutError, APIConnectionError, InternalServerError)

class LLMService:
    """
    Manages LLM calls with automatic retries and fallback logic.
    """

    def __init__(self):
        # DEFAULT_LLM_MODEL first, then LLM_FALLBACK_MODELS (by default, the registry)
        fallback = settings.LLM_FALLBACK_MODELS
        if fallback is None:
            fallback = LLMRegistry.get_all_names()
        self._model_names = list(dict.fromkeys([settings.DEFAULT_LLM_MODEL, *fallback]))
        self._current_model_index = 0
        self._tools: List = []
        self._llm: Optional[BaseChatModel] = LLMRegistry.get(self._model_names[0])

    @property
    def model_name(self) -> str:
        return self._model_names[self._current_model_index]

    def _use_model(self, index: int) -> None:
        """Make the model at `index` the current one, with the agent's tools bound to it."""
        llm = LLMRegistry.get(self._model_names[index])
        self._llm = llm.bind_tools(self._tools) if self._tools else llm
        self._current_model_index = index

    def _switch_to_next_model(self) -> bool:
        """
        Circular Fallback: Switches to the next model in the list, tools included.
        Returns True if successful.
        """
        try:
            next_index = (self._current_model_index + 1) % len(self._model_names)
            logger.warning(
                "switching_to_next_model",
                from_model=self.model_name,
                to_model=self._model_names[next_index],
            )
            self._use_model(next_index)
            return True
        except Exception as e:
            logger.error("model_switch_failed", error=str(e))
            return False

    # --------------------------------------------------
    # The Retry Decorator
    # --------------------------------------------------
    # This is the magic. If the function raises specific exceptions,
    # Tenacity will wait (exponentially) and try again.
    @retry(
        stop=stop_after_attempt(settings.MAX_LLM_CALL_RETRIES), # Stop after 3 tries
        wait=wait_exponential(multiplier=1, min=2, max=10),     # Exponential, between 2s and 10s
        retry=retry_if_exception_type(RETRYABLE_ERRORS),
        before_sleep=before_sleep_log(logger, logging.WARNING), # Log before waiting
        reraise=True,
    )
    async def _call_llm_with_retry(self, messages: List[BaseMessage]) -> BaseMessage:
        """Internal method that executes the actual API call."""
        if not self._llm:
            raise RuntimeError("LLM not initialized")
        return await self._llm.ainvoke(messages)

    async def call(self, messages: List[BaseMessage]) -> BaseMessage:
        """
        Public interface. Wraps the retry logic with a Fallback loop.
        If one model fails (after its retries), the next one gets the request.
        """
        total_models = len(self._model_names)
        models_tried = 0
        last_error = None

        while models_tried < total_models:
            try:
                # Attempt to generate response
                return await self._call_llm_with_retry(messages)

            except OpenAIError as e:
                # If we exhausted retries for THIS model, log and switch
                last_error = e
                models_tried += 1
                logger.error("llm_call_failed_after_retries", model=self.model_name, error=str(e))

                if models_tried >= total_models:
                    # We tried everything.
                    break

                self._switch_to_next_model()
        raise RuntimeError(f"failed to get response from llm after trying {models_tried} models. last error: {last_error}")

    def get_llm(self) -> BaseChatModel:
        return self._llm

    def bind_tools(self, tools: List) -> "LLMService":
        """Bind tools to the current LLM, and to every model switched to later."""
        self._tools = list(tools)
        self._use_model(self._current_model_index)
        return self
```

Here `_switch_to_next_model` moves along the list in a circular manner. If the current model fails after exhausting its retries, we move to the next one in the list. In our retry decorator, we specify which exceptions should trigger a retry: the transient ones (rate limits, timeouts, dropped connections, 5xx errors). A bad request would fail the same way three times, so it goes straight to the next model instead.

Two details are easy to get wrong here. The tools must be bound again on every switch: a fallback model that does not know the tools can no longer search, and an earlier version lost them that way after its first fallback. And `before_sleep_log` takes the level as a number (`logging.WARNING`); the logger looks levels up by number, so the string `"WARNING"` would fail with a `KeyError` at the very first retry instead of retrying.

### <a id="0d26"></a>**Circuit Breaking**

We are also binding tools to the LLM instance so that it can use them in an Agent context.

![Circuit Break](https://miro.medium.com/v2/resize:fit:875/1*6-y5HWu68d-fECfowWCGqg.png)
*Circuit Break (Created by Fareed Khan)*

Finally, we create a global instance of the `LLMService` for easy access throughout the application:

```python
# Create global instance
llm_service = LLMService()
```

If a provider has a major outage, `tenacity` retries the same model, and the loop in `call` then moves to the backup models. This makes sure your users rarely see a 500 Error, even when the backend APIs are unstable.

## <a id="2767"></a>Multi-Agentic Architecture

Now we will start working on our stateful AI Agentic system using **LangGraph**. Unlike linear chains (Input →→ LLM →→ Output), LangGraph allows us to build **Stateful Agents**.

These agents can loop, retry, call tools, remember past interactions, and persist their state into a database so they can pick up exactly where they left off, even if the server restarts.

In many chat applications, users expect the AI to remember *facts about them* across sessions. For example, if a user tells the AI “I love hiking” in one session, they expect the AI to remember that in future sessions.

### <a id="097b"></a>Long-Term Memory Integration

So, we are also going to integrate **Long-Term Memory** using `mem0ai`. While the conversation history (Short-Term Memory) helps the agent remember *this* chat, Long-Term Memory helps it remember *facts about the user* across all chats.

![Long term memory](https://miro.medium.com/v2/resize:fit:1250/1*wyBkaRzagua7iX7fR453NQ.png)
*Long term memory (Created by Fareed Khan)*

In a production system, we treat prompts as **Assets** which means separating them from code. This allows prompt engineers to update/improve prompts without changing application logic. We store them as Markdown files. Let’s create `src/agent/prompts/system.md` that will define the system prompt for our agent:

```yaml
# Name: {agent_name}
# Role: A world class assistant
Help the user with their questions.

# Instructions
- Always be friendly and professional.
- If you don't know the answer, say you don't know. Don't make up an answer.
- Try to give the most accurate answer possible.

# What you know about the user
{long_term_memory}

# Current date and time
{current_date_and_time}
```

Notice the placeholders like `{long_term_memory}`. We will dynamically inject these at runtime.

This is a simple prompt, but in a real application, you would want to make it much more detailed, specifying the agent’s personality, constraints, and behavior according to your use case.

Now, we need a utility to load this so we need `src/agent/prompts/__init__.py` that will read the markdown file and format it with dynamic variables:

```python
import os
from datetime import datetime
from src.config.settings import settings

def load_system_prompt(**kwargs) -> str:
    """
    Loads the system prompt from the markdown file and injects dynamic variables.
    """
    prompt_path = os.path.join(os.path.dirname(__file__), "system.md")
    
    with open(prompt_path, "r") as f:
        return f.read().format(
            agent_name=settings.PROJECT_NAME + " Agent",
            current_date_and_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            **kwargs, # Inject dynamic variables like 'long_term_memory'
        )
```

Many modern AI agents need to interact with external systems to be truly useful. We define these capabilities as **Tools**. Let’s give our agent the ability to search the internet using `DuckDuckGo` which is safer and more privacy-focused than Google.

### <a id="6f9a"></a>Tool Calling Feature

![Tool feature](https://miro.medium.com/v2/resize:fit:875/1*R_nkHq1wBXFUWclqu2_oSg.png)
*Tool feature (Created by Fareed Khan)*

We need to create a separate `src/agent/tools/web_search.py` for this because each tool should be modular and testable. It calls the [`ddgs`](https://pypi.org/project/ddgs/) package directly (the LangChain team is sunsetting `langchain-community`, where a ready-made DuckDuckGo tool used to live):

```python
import json

from ddgs import DDGS
from langchain_core.tools import tool

from src.system.logs import logger

MAX_RESULTS = 10  # plenty of context for the LLM

@tool("web_search")
def duckduckgo_search_tool(query: str) -> str:
    """Search the web with DuckDuckGo. Use it for recent events and for facts you are not sure about.

    Returns a JSON list of results, each with a title, a link and a snippet.
    """
    try:
        results = DDGS().text(query, max_results=MAX_RESULTS)
    except Exception as e:
        # Network errors and rate limits: log them, and tell the model, which can answer without the search
        logger.warning("web_search_failed", error=str(e))
        return f"The search failed: {e}"
    return json.dumps(
        [{"title": r.get("title"), "link": r.get("href"), "snippet": r.get("body")} for r in results],
        ensure_ascii=False,
    )
```

The docstring is what the model reads to decide when to use the tool, so it says what the tool is for and what it returns. And then we will be exporting it in `src/agent/tools/__init__.py`:

```python
from langchain_core.tools.base import BaseTool
from .web_search import duckduckgo_search_tool

# Central registry of tools available to the agent
tools: list[BaseTool] = [duckduckgo_search_tool]
```

Now we are going to build the most complex and critical file in the entire project: `src/agent/workflow.py`. There are four main components to this file:

1.  **State Management:** Loading/Saving conversation state to Postgres.
2.  **Memory Retrieval:** Fetching user facts from `mem0ai`.
3.  **Execution Loop:** Calling the LLM, parsing tool calls, and executing them.
4.  **Streaming:** Sending tokens to the user in real-time.

An ai engineer might already be aware of why these components are necessary, since it holds the core logic of the AI agent.

`mem0` is a memory layer for AI applications, widely used for Long-Term Memory: it extracts facts from conversations with an LLM and stores them as vectors, here in pgvector. We will use it to store and retrieve user-specific context. Let's code it step-by-step:

```python
import asyncio
from typing import Any, AsyncGenerator, Optional
from urllib.parse import quote_plus

from langchain_core.messages import AIMessage, ToolMessage, convert_to_openai_messages
from langchain_core.runnables import RunnableConfig
from langfuse.langchain import CallbackHandler
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
from langgraph.graph import END, StateGraph
from langgraph.graph.state import CompiledStateGraph
from langgraph.types import Command, StateSnapshot

from mem0 import AsyncMemory

from psycopg_pool import AsyncConnectionPool
from src.config.settings import Environment, settings
from src.agent.tools import tools
from src.system.logs import logger
from src.agent.prompts import load_system_prompt
from src.data.schemas import ChatMessage, GraphState, Message
from src.services.llm_provider import llm_service
from src.utils import dump_messages, message_text, prepare_messages, process_llm_response

class LangGraphAgent:
    """
    Manages the LangGraph Workflow, LLM interactions, and Memory persistence.
    """
    def __init__(self):
        # Bind tools to the LLM service so the model knows what functions it can call
        self.llm_service = llm_service.bind_tools(tools)
        self.tools_by_name = {tool.name: tool for tool in tools}

        self._connection_pool: Optional[AsyncConnectionPool] = None
        self._graph: Optional[CompiledStateGraph] = None
        self.memory: Optional[AsyncMemory] = None
        # The first requests on a fresh server arrive together; the locks make them
        # share one graph and one memory client instead of each building their own
        self._graph_lock = asyncio.Lock()
        self._memory_lock = asyncio.Lock()
        # asyncio only keeps a weak reference to a task: background tasks live here until done
        self._background_tasks: set[asyncio.Task] = set()
        logger.info("langgraph_agent_initialized", model=settings.DEFAULT_LLM_MODEL)
    async def _long_term_memory(self) -> AsyncMemory:
        """
        Lazy-load the mem0ai memory client with pgvector configuration.
        """
        if self.memory is not None:
            return self.memory
        async with self._memory_lock:
            if self.memory is None:
                config = {
                    "vector_store": {
                        "provider": "pgvector",
                        "config": {
                            "collection_name": settings.LONG_TERM_MEMORY_COLLECTION_NAME,
                            "embedding_model_dims": settings.LONG_TERM_MEMORY_EMBEDDER_DIMS,
                            "dbname": settings.POSTGRES_DB,
                            "user": settings.POSTGRES_USER,
                            "password": settings.POSTGRES_PASSWORD,
                            "host": settings.POSTGRES_HOST,
                            "port": settings.POSTGRES_PORT,
                        },
                    },
                    "llm": {
                        "provider": "openai",
                        "config": {
                            "model": settings.LONG_TERM_MEMORY_MODEL,
                            "api_key": settings.OPENAI_API_KEY,
                            "openai_base_url": settings.OPENAI_BASE_URL,
                        },
                    },
                    "embedder": {
                        "provider": "openai",
                        "config": {
                            "model": settings.LONG_TERM_MEMORY_EMBEDDER_MODEL,
                            "api_key": settings.OPENAI_API_KEY,
                            "openai_base_url": settings.OPENAI_BASE_URL,
                            "embedding_dims": settings.LONG_TERM_MEMORY_EMBEDDER_DIMS,
                        },
                    },
                }
                # mem0 2 builds the client synchronously (it connects to pgvector and creates
                # its tables), so build it in a worker thread instead of blocking the event loop
                self.memory = await asyncio.to_thread(self._build_memory_client, config)
        return self.memory

    @staticmethod
    def _build_memory_client(config: dict) -> AsyncMemory:
        memory = AsyncMemory.from_config(config)
        # mem0 creates its entity store lazily and without a lock; when the first searches
        # arrive together, their CREATE EXTENSION / CREATE TABLE statements collide. Create it now.
        getattr(memory, "entity_store", None)
        return memory
 
    async def _get_connection_pool(self) -> AsyncConnectionPool:
        """
        Establish a connection pool specifically for LangGraph checkpointers.
        """
        if self._connection_pool is None:
            connection_url = (
                "postgresql://"
                f"{quote_plus(settings.POSTGRES_USER)}:{quote_plus(settings.POSTGRES_PASSWORD)}"
                f"@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
            )
            self._connection_pool = AsyncConnectionPool(
                connection_url,
                open=False,
                max_size=settings.POSTGRES_POOL_SIZE,
                kwargs={"autocommit": True, "connect_timeout": 5, "prepare_threshold": None}
            )
            await self._connection_pool.open()
        return self._connection_pool

    # ==================================================
    # Node Logic
    # ==================================================
    async def _chat(self, state: GraphState, config: RunnableConfig) -> Command:
        """
        The main Chat Node.
        1. Loads system prompt with memory context.
        2. Prepares messages (trimming if needed).
        3. Calls LLM Service.
        """
        # Load system prompt with the Long-Term Memory retrieved from previous steps
        SYSTEM_PROMPT = load_system_prompt(long_term_memory=state.long_term_memory)
        
        # Prepare context window (trimming)
        messages = prepare_messages(state.messages, SYSTEM_PROMPT)
        try:
            # Invoke LLM (with retries handled by service)
            response_message = await self.llm_service.call(dump_messages(messages))
            response_message = process_llm_response(response_message)
            # Determine routing: If LLM wants to use a tool, go to 'tool_call', else END.
            if response_message.tool_calls:
                goto = "tool_call"
            else:
                goto = END
            # Return command to update state and route
            return Command(update={"messages": [response_message]}, goto=goto)
            
        except Exception as e:
            logger.error("llm_call_node_failed", error=str(e))
            raise

    async def _tool_call(self, state: GraphState) -> Command:
        """
        The Tool Execution Node.
        Executes requested tools and returns results back to the chat node.
        """
        outputs = []
        for tool_call in state.messages[-1].tool_calls:
            tool = self.tools_by_name.get(tool_call["name"])
            logger.info("tool_called", tool=tool_call["name"])
            if tool is None:
                # Models sometimes call a tool that does not exist; tell it instead of crashing
                tool_result = f"Error: there is no tool named {tool_call['name']!r}."
            else:
                # Execute the tool
                tool_result = await tool.ainvoke(tool_call["args"])
            
            # Format result as a ToolMessage
            outputs.append(
                ToolMessage(
                    content=str(tool_result),
                    name=tool_call["name"],
                    tool_call_id=tool_call["id"],
                )
            )
            
        # Update state with tool outputs and loop back to '_chat'
        return Command(update={"messages": outputs}, goto="chat")

    # ==================================================
    # Graph Compilation
    # ==================================================
    async def create_graph(self) -> CompiledStateGraph:
        """
        Builds the state graph and attaches the Postgres checkpointer.
        """
        if self._gr