# Build AI Agents From Scratch

Learn to build AI Agents from scratch using LangGraph and LangChain. This comprehensive tutorial series takes you from basic concepts to building autonomous AI agents with tools, memory, and complex workflows.

## 📚 What You'll Learn

- ✅ Core LangGraph concepts and patterns
- ✅ Building sequential and conditional workflows
- ✅ Integrating LLMs into graph workflows
- ✅ Creating and using tools to extend LLM capabilities
- ✅ Automated tool-calling agents
- ✅ State management and data flow
- ✅ Conditional routing and decision-making
- ✅ Multi-step AI workflows
- ✅ Effective prompting techniques for better LLM responses
- ✅ Getting structured, type-safe JSON output from LLMs
- ✅ Agentic architectural patterns (ReACT, Plan-and-Execute, Reflection)
- ✅ Advanced multi-agent systems (Hierarchical, Router, Collaborative)

## 📖 Tutorial Chapters

This repository is organized as a progressive tutorial series. Each chapter builds on the previous one, teaching you the fundamental concepts needed to build AI agents.

### [Chapter 1: Introduction To Gen AI](./chapters/01-Introduction%20To%20Gen%20AI/)
**Foundations of GenAI concepts**

Learn the fundamental concepts:
- What are LLMs and how they work
- AI Agents and their architecture
- Retrieval Augmented Generation (RAG)
- Sessions and Memory (Short-term vs Long-term)
- Tools and their role in AI systems
- Human In The Loop patterns

📓 **Notebook**: [hello_world_langgraph.ipynb](./chapters/01-Introduction%20To%20Gen%20AI/hello_world_langgraph.ipynb)

---

### [Chapter 2: Building Simple Workflow Graphs](./chapters/02-Building%20Simple%20Workflow%20Graphs/)
**Master the basics of LangGraph**

Learn to build workflows without AI:
- StateGraph and state management
- Creating nodes and connecting them with edges
- Understanding state flow and merging
- Building linear workflows
- Execution and debugging

📓 **Notebook**: [workflow_graphs.ipynb](./chapters/02-Building%20Simple%20Workflow%20Graphs/workflow_graphs.ipynb)

**Example**: Article processing workflow with 3 steps

---

### [Chapter 3: Conditional Edges](./chapters/03-Conditional%20Edges/)
**Add branching logic to your workflows**

Learn to create decision-driven workflows:
- Conditional edges vs normal edges
- Writing routing functions
- Multi-way branching (2, 3, or more paths)
- State-based decision making
- Path mappings

📓 **Notebook**: [conditional_edges.ipynb](./chapters/03-Conditional%20Edges/conditional_edges.ipynb)

**Examples**:
- Request priority router (2 paths)
- Content moderation system (3 paths)

---

### [Chapter 4: Calling LLMs in Graphs](./chapters/04-Calling%20LLMs%20in%20Graphs/)
**Integrate AI into your workflows**

Learn to use LLMs within graphs:
- Initializing and configuring LLM instances
- Calling LLMs from nodes
- Chaining multiple LLM calls
- LLM-driven conditional routing
- Prompt structuring and response validation

📓 **Notebook**: [llm_in_graphs.ipynb](./chapters/04-Calling%20LLMs%20in%20Graphs/llm_in_graphs.ipynb)

**Examples**:
- Blog generation with multiple LLM calls
- Support ticket classifier with LLM-driven routing

---

### [Chapter 5: Simple Tool Calling](./chapters/05-Simple%20Tool%20Calling/)
**Extend LLM capabilities with tools**

Learn the different ways to create tools:
- `@tool` decorator for simple functions
- `StructuredTool.from_function()` for custom metadata
- Custom `BaseTool` classes for complex tools
- Pydantic models for input validation
- Binding tools to LLMs
- Manual tool execution

📓 **Notebook**: [creating_tools.ipynb](./chapters/05-Simple%20Tool%20Calling/creating_tools.ipynb)

**Examples**: Calculator, weather, trip planner, search, and booking tools

---

### [Chapter 6: Automated Tool Calling](./chapters/06-Automated%20Tool%20Calling/)
**Build autonomous AI agents**

Learn to automate tool execution in graphs:
- The agent loop pattern (Think → Act → Think)
- Using `ToolNode` for automatic execution
- Conditional routing for tool calls
- Building autonomous agents
- Streaming and debugging agent execution

📓 **Notebook**: [automated_tool_calling.ipynb](./chapters/06-Automated%20Tool%20Calling/automated_tool_calling.ipynb)

**Example**: Calculator agent with automated tool execution

---

### [Chapter 7: Advanced ToolNode Patterns](./chapters/07-Advanced%20ToolNode%20Patterns/)
**Master advanced tool calling patterns**

Learn sophisticated ToolNode techniques:
- Understanding ToolNode internals
- Multiple ToolNodes for different tool categories
- Custom error handling and fallback mechanisms
- Implementing custom ToolNode logic
- Building production-ready agents
- Complex multi-step tool chains

📓 **Notebook**: [advanced_toolnode.ipynb](./chapters/07-Advanced%20ToolNode%20Patterns/advanced_toolnode.ipynb)

**Examples**:
- Research assistant with categorized tools
- Error-handling tool execution
- Data analysis agent with multiple tools

---

### [Chapter 8: Command Pattern for Routing](./chapters/08-Command%20Pattern%20for%20Routing/)
**Alternative routing approach to conditional edges**

Learn the Command pattern for explicit routing:
- Understanding Command vs conditional edges
- Self-routing nodes that specify next steps
- Using Command for early termination
- LLM-driven Command routing
- When to use each routing approach
- Mixing Command and conditional edges

📓 **Notebook**: [command_routing.ipynb](./chapters/08-Command%20Pattern%20for%20Routing/command_routing.ipynb)

**Examples**:
- Content moderation with Command
- LLM-driven support ticket router
- Validation workflow with early exit

---

### [Chapter 9: Prompting Techniques](./chapters/09-Prompting%20Techniques/)
**Master fundamental prompting patterns**

Learn essential techniques for effective LLM communication:
- Zero-shot vs few-shot prompting
- System vs user messages for structured conversations
- Reasoning-oriented prompting and concise, user-facing rationales
- Prompt templates for reusable, consistent prompts
- When to use each technique
- Combining techniques for better results

📓 **Notebook**: [prompting_techniques.ipynb](./chapters/09-Prompting%20Techniques/prompting_techniques.ipynb)

**Examples**:
- Sentiment analysis with zero-shot and few-shot
- Customer support and technical expert agents
- Math problem solving with CoT
- Email generation with templates

---

### [Chapter 10: Structured Output](./chapters/10-Structured%20Output/)
**Get consistent, typed JSON responses from LLMs**

Learn to get structured data instead of free-form text:
- Why structured output is critical for production agents
- Pydantic models for defining schemas
- Using `with_structured_output()` for typed responses
- Different field types (strings, numbers, lists, nested objects)
- Literal types for constrained choices (enums)
- Integrating structured output in LangGraph workflows
- Error handling and validation

📓 **Notebook**: [structured_output.ipynb](./chapters/10-Structured%20Output/structured_output.ipynb)

**Examples**:
- User profile extraction pipeline
- Sales data analysis with structured insights
- Email classification with conditional routing
- Multi-step workflows with typed data flow

---

### [Chapter 11: Agentic Patterns](./chapters/11-Agentic%20Patterns/)
**Architectural patterns for building intelligent agents**

Learn the major agentic patterns used in production AI systems:
- **ReACT Pattern** - Reasoning and Acting in iterative cycles
- **Plan-and-Execute** - Planning before execution
- **Reflection** - Self-critique and improvement
- **Multi-Agent Systems** - Multiple specialized agents working together
- **Tool-Use Patterns** - Different approaches to tool integration
- **Memory-Augmented Agents** - Agents with persistent memory
- **Hierarchical Agents** - Manager-worker structures
- **Router Pattern** - Intelligent delegation and routing
- When to use each pattern and how to combine them

📄 **Conceptual Guide**: This chapter focuses on understanding patterns, not implementation

---

### [Chapter 12: ReACT Agent](./chapters/12-ReACT%20Agent/)
**Build transparent, reasoning agents**

Implement the ReACT (Reasoning + Acting) pattern:
- How ReACT agents select actions step-by-step
- Observable action traces before each tool call
- Building the ReACT loop (Plan → Action → Observation)
- Tool integration in reasoning workflows
- Debugging and explainability
- Multi-step problem solving with visible reasoning

📓 **Notebook**: [react_agent.ipynb](./chapters/12-ReACT%20Agent/react_agent.ipynb)

**Examples**:
- Research assistant with web search and calculator
- Multi-step reasoning with tool chaining
- Observable tool trace for debugging

---

### [Chapter 13: Plan-and-Execute Agent](./chapters/13-Plan-and-Execute%20Agent/)
**Structured planning and systematic execution**

Implement the Plan-and-Execute pattern:
- Separating planning from execution
- Creating structured plans with Pydantic
- Step-by-step execution with progress tracking
- Tool usage during plan execution
- When to use Plan-and-Execute vs ReACT
- Building predictable, efficient workflows

📓 **Notebook**: [plan_and_execute_agent.ipynb](./chapters/13-Plan-and-Execute%20Agent/plan_and_execute_agent.ipynb)

**Examples**:
- Data analysis with structured planning
- Multi-step research and comparison tasks
- Comprehensive business report generation

---

### [Chapter 14: Reflection Agent](./chapters/14-Reflection%20Agent/)
**Self-improving agents through critique**

Implement the Reflection pattern:
- Self-critique and iterative improvement
- Structured reflection with quality scoring
- Code generation with refinement
- Tool-assisted validation
- Quality tracking across iterations
- Balancing quality vs. cost

📓 **Notebook**: [reflection_agent.ipynb](./chapters/14-Reflection%20Agent/reflection_agent.ipynb)

**Examples**:
- Code generation with quality improvement
- Multi-criteria reflection (correctness, quality, documentation)
- Iterative refinement to production-ready code

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Basic understanding of Python
- An Anthropic API key (get one at [console.anthropic.com](https://console.anthropic.com/))

### Installation

1. Clone this repository:
```bash
git clone https://github.com/ps06756/build-ai-agents-from-scratch.git
cd build-ai-agents-from-scratch
```

2. Create an isolated environment and install dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
python3 -m pip install --upgrade pip
python3 -m pip install -e '.[dev]'
```

3. Set up your API key:
```bash
# Linux/Mac
export ANTHROPIC_API_KEY='your-api-key-here'
# Optional: choose any model available to your Anthropic account
export ANTHROPIC_MODEL='claude-sonnet-4-6'

# Windows
set ANTHROPIC_API_KEY=your-api-key-here
set ANTHROPIC_MODEL=claude-sonnet-4-6
```

### Running the Examples

Each chapter contains Jupyter notebooks with complete, runnable code:

```bash
# Navigate to a chapter
cd chapters/02-Building\ Simple\ Workflow\ Graphs/

# Launch Jupyter
jupyter lab workflow_graphs.ipynb
```

Or run the Python examples directly:
```bash
cd chapters/01-Introduction\ To\ Gen\ AI/examples/
python3 single_turn_conversation.py
```

## 📁 Repository Structure

```
build-ai-agents-from-scratch/
├── chapters/
│   ├── 01-Introduction To Gen AI/
│   │   ├── README.md
│   │   ├── hello_world_langgraph.ipynb
│   │   └── examples/
│   │       ├── single_turn_conversation.py
│   │       └── multi_turn_conversation.py
│   ├── 02-Building Simple Workflow Graphs/
│   │   ├── README.md
│   │   └── workflow_graphs.ipynb
│   ├── 03-Conditional Edges/
│   │   ├── README.md
│   │   └── conditional_edges.ipynb
│   ├── 04-Calling LLMs in Graphs/
│   │   ├── README.md
│   │   └── llm_in_graphs.ipynb
│   ├── 05-Simple Tool Calling/
│   │   ├── README.md
│   │   └── creating_tools.ipynb
│   ├── 06-Automated Tool Calling/
│   │   ├── README.md
│   │   └── automated_tool_calling.ipynb
│   ├── 07-Advanced ToolNode Patterns/
│   │   ├── README.md
│   │   └── advanced_toolnode.ipynb
│   ├── 08-Command Pattern for Routing/
│   │   ├── README.md
│   │   └── command_routing.ipynb
│   ├── 09-Prompting Techniques/
│   │   ├── README.md
│   │   └── prompting_techniques.ipynb
│   ├── 10-Structured Output/
│   │   ├── README.md
│   │   └── structured_output.ipynb
│   ├── 11-Agentic Patterns/
│   │   └── README.md
│   ├── 12-ReACT Agent/
│   │   ├── README.md
│   │   └── react_agent.ipynb
│   ├── 13-Plan-and-Execute Agent/
│   │   ├── README.md
│   │   └── plan_and_execute_agent.ipynb
│   └── 14-Reflection Agent/
│       ├── README.md
│       └── reflection_agent.ipynb
└── README.md
```

## 🎯 Learning Path

**Recommended Order:**
1. Start with **Chapter 1** to understand GenAI fundamentals
2. Progress through **Chapters 2-3** to master graph mechanics and routing
3. Learn to integrate AI in **Chapter 4**
4. Extend capabilities with tools in **Chapters 5-6**
5. Master advanced patterns in **Chapter 7** for production-ready agents
6. Learn alternative routing with **Chapter 8** (Command pattern)
7. Master prompting techniques in **Chapter 9** for effective LLM communication
8. Get structured, typed responses in **Chapter 10** for production reliability
9. Understand agentic architectural patterns in **Chapter 11** to design sophisticated agents
10. Implement specific patterns:
    - **Chapter 12**: ReACT agents for transparent reasoning
    - **Chapter 13**: Plan-and-Execute for structured workflows
    - **Chapter 14**: Reflection for high-quality outputs

Each chapter builds on previous concepts, so following the order is recommended for beginners.

**Note**:
- Chapter 8 presents an alternative to Chapter 3's conditional edges - you can use either approach based on your needs!
- Chapter 11 is conceptual and ties together patterns that you implement in Chapters 12-14
- The course currently ends at Chapter 14; later multi-agent chapters are planned rather than linked prematurely.

## 🤝 Contributing

Contributions are welcome! If you find issues or have suggestions for improvements:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## Production notes

The examples prioritize learning. Review the [production checklist](./docs/production-checklist.md) before connecting an agent to real data or side-effecting tools.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Built with:
- [LangGraph](https://github.com/langchain-ai/langgraph) - Framework for building agent workflows
- [LangChain](https://github.com/langchain-ai/langchain) - LLM application framework
- [Anthropic Claude](https://www.anthropic.com/claude) - Advanced language model

---

**Ready to start building AI agents?** Begin with [Chapter 1: Introduction To Gen AI](./chapters/01-Introduction%20To%20Gen%20AI/) →
