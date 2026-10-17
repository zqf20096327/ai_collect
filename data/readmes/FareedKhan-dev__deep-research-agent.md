# Building Deep Research Agent

This blog is created using the help of thinkdepth ai agent. You can try it out [here](https://thinkdepth.ai).

When humans conduct deep research, they follow a time-tested pattern: they start with a rough idea, gather information from multiple sources, and iteratively refine their understanding and arguments through cycles of drafting, critiquing, and revising. This process often involves going back to do more research to fill in gaps or strengthen weak points in their reasoning.

Most [public deep research agents](https://github.com/assafelovic/gpt-researcher) use smart techniques to get better results, like [chain-of-thought reasoning](https://research.google/blog/language-models-perform-reasoning-via-chain-of-thought/) or [generating multiple answers](https://openreview.net/forum?id=H4S4ETc8c9) and picking the best. However, they often skip the key writing steps humans follow: planning, drafting, researching, and revising. An important part of revising is doing more research to [find missing information or make your arguments stronger](https://www.emerald.com/jd/article-abstract/69/2/243/198951/Patterns-of-graduate-students-information-seeking?redirectedFrom=fulltext).

The **Time-Tested Diffusion based Deep Research (TTD-DR)** is a modern algorithm designed to address this limitation by **mimicking human research** behavior. Let’s visually explore its architecture …

![Why Hierarchical State (Created by Fareed Khan)](https://miro.medium.com/v2/resize:fit:7911/1*xi7PELfrOjpya8OgrbrFgQ.png)

1.  **Clarify and Scope:** The agent first clarifies the user’s goal to create a detailed research brief, then writes a rough initial draft to serve as a starting point.
2.  **Analyze and Plan:** A supervisor agent critiques the draft to find weaknesses and logical gaps, then plans targeted research tasks to fix them.
3.  **Delegate and Research:** The supervisor deploys multiple worker agents to research different sub-topics in parallel, efficiently gathering external facts and data.
4.  **Integrate and Refine:** The new research findings are integrated into the draft. This **“denoising”** step corrects flaws and adds detail, steadily improving the report’s quality.
5.  **Self-Correction Loop:** A **Red Team** agent attacks the draft logic to find hidden flaws, while an **“Evaluator”** agent scores its quality, creating a constant feedback loop.
6.  **Iterate and Finalize:** The entire cycle repeats, progressively enhancing the report until it meets a high-quality standard, at which point the final, polished version is produced.

> This human pattern works like retrieval-augmented diffusion models, it starts with a rough or messy idea and slowly improves it into a clear, high-quality result.

In this blog, we are going to implement this architecture and visually understand each of its components step by step. All the code is available in my GitHub repository.

All the code is available in my GitHub Repository.

## Table of Content

*   [Creating the Diffusion Workspace](#creating-the-diffusion-workspace)
    *   [Hierarchical State for Iterative Refinement](#hierarchical-state-for-iterative-refinement)
    *   [Creating Toolset for Research and Refinement](#creating-toolset-for-research-and-refinement)
    *   [Defining the Core Utility](#defining-the-core-utility)
*   [Initial Noise and Guidance Signal](#initial-noise-and-guidance-signal)
    *   [Node 1 for Clarifying User Intent](#node-1-for-clarifying-user-intent)
    *   [Node 2 for Writing the Research Brief](#node-2-for-writing-the-research-brief)
    *   [Node 3 for Generating the Initial Draft Report](#node-3-for-generating-the-initial-draft-report)
*   [Guidance Generation Engine](#guidance-generation-engine)
    *   [Creating the ReAct-style Loop](#creating-the-react-style-loop)
    *   [Building the Web Search Capability](#building-the-web-search-capability)
    *   [Compressing the Findings](#compressing-the-findings)
*   [Creating the Core Denoising Loop](#creating-the-core-denoising-loop)
    *   [Building the Supervisor Node](#building-the-supervisor-node)
    *   [Fan-Out Work and Denoise](#fan-out-work-and-denoise)
    *   [Applying Guidance with Denoising Step](#applying-guidance-with-denoising-step)
*   [Self-Correction and Stability Mechanisms](#self-correction-and-stability-mechanisms)
    *   [Red Team as a Noise Reducer](#red-team-as-a-noise-reducer)
    *   [Evaluator as a Convergence Check](#evaluator-as-a-convergence-check)
    *   [State Entropy using Context Pruning Node](#state-entropy-using-context-pruning-node)
*   [Assembling the Entire Graph](#assembling-the-entire-graph)
    *   [Wiring the Scoping Sub-Graph](#wiring-the-scoping-sub-graph)
    *   [Wiring the Research Sub-Graph](#wiring-the-research-sub-graph)
    *   [Compiling the Denoising Loop](#compiling-the-denoising-loop)
*   [Final Synthesis and Execution](#final-synthesis-and-execution)
    *   [Generating the Fully Denoised Report](#generating-the-fully-denoised-report)
    *   [Integrating All Sub-Graphs](#integrating-all-sub-graphs)
    *   [Observing the Diffusion of an 8-Iteration Execution](#observing-the-diffusion-of-an-8-iteration-execution)
*   [Analyzing the Final Output](#analyzing-the-final-output)
    *   [Monolithic LLM against Deep Researh architeure](#monolithic-llm-against-deep-researh-architeure)
*   [Conclusion](#conclusion)

---

## Creating the Diffusion Workspace

Before we can start building our iterative engine, we need to establish a solid foundation. This means designing the core data structures that will support complex collaboration, defining the unique **“personas”** of our specialist agents through precise prompt engineering, and creating the important tools and capabilities they will use to interact with the environment and assess their own output.

Think of this as the blueprint for our diffusion workspace, a carefully structured starting point that ensures everything we build on top will be robust, adaptable, and intelligent.

### Hierarchical State for Iterative Refinement

The first and most critical step is to design the shared memory, or **“state”**, for our agent society.

> **For a system this complex, a simple list of messages is insufficient**.

![Why Hierarchical State (Created by Fareed Khan)](https://miro.medium.com/v2/resize:fit:2000/1*nogQPYtTjc6xnBX84Sy-Qw.png)

We need a hierarchical, structured state that acts as the central **“canvas”** or **“workbench”** where agents can post their findings, critiques, and evolving drafts.

We will use Pydantic `BaseModel` and Python's `TypedDict` to enforce a strict, machine-readable schema for this collaboration.

Let’s start with the most atomic unit of knowledge our system will handle: a single, extracted `Fact`.

```python
from langchain_core.messages import BaseMessage
from pydantic import BaseModel, Field
from typing import Sequence, Annotated, List, Literal, Optional, TypedDict
import operator

class Fact(BaseModel):
    """An atomic unit of knowledge, extracted from raw research notes and stored in our structured knowledge base."""
    # The core factual statement itself, extracted from a source.
    content: str = Field(description="The factual statement")

    # We must track the provenance of every fact for traceability and citations in the final report.
    source_url: str = Field(description="Where this fact came from")

    # A confidence score allows the system to weigh more credible sources higher during synthesis.
    confidence_score: int = Field(description="1-100 confidence score based on source credibility")

    # This flag allows our Red Team to mark facts that are contradicted by other evidence, a key part of our self-correction loop.
    is_disputed: bool = Field(default=False, description="If this fact conflicts with others")
```

We can say that this `Fact` class is the core of our system memory. It is a structured object that captures not only the information itself (`content`) but also its `source_url` and a `confidence_score`.

This is a design choice because it makes our knowledge base auditable and allows downstream agents to reason about the credibility of the information they are using. The `is_disputed` flag is a mechanism for our self-correction loop, allowing the system to track and resolve contradictions.

Next, we need a structure to represent the feedback from our **“Red Team”** agent.

```python
class Critique(BaseModel):
    """A structured model for adversarial feedback from the Red Team or other quality control agents."""
    # Tracks which agent generated the critique (e.g., "Red Team", "Safety Filter") for accountability.
    author: str 

    # The specific logical fallacy, bias, or factual error that was found in the draft.
    concern: str

    # A 1-10 score to quantify the severity of the issue, allowing the Supervisor agent to prioritize its actions.
    severity: int 

    # A flag to track whether a critique has been addressed in a subsequent revision of the draft.
    addressed: bool = Field(default=False, description="Has the supervisor fixed this?")
```

This `Critique` is our formal communication channel for our system self-correction capabilities. By forcing our adversarial agents to provide feedback in this structured format, we transform their insights into machine-readable data.

The `severity` score is particularly important, it will allow our Supervisor agent to decide if a draft needs minor polishing or a complete, ground-up rewrite, enabling a more intelligent and nuanced revision process.

To enable our system to learn and improve, we need a way to track its performance on each iteration of the diffusion loop.

```python
class QualityMetric(TypedDict):
    """A TypedDict for storing a snapshot of the draft's quality at a specific iteration."""
    # The programmatic quality score calculated by our self-evolution evaluator.
    score: float
    # The textual feedback from the evaluator explaining the score.
    feedback: str
    # The iteration number at which this score was recorded, for tracking progress over time.
    iteration: int
```

The `QualityMetric` structure is our performance log. By appending one of these dictionaries to our state after every refinement step, we create a clear, historical record of the diffusion process.

This `quality_history` allow us to plot the agent improvement over time and programmatically diagnose if the refinement process is stalling or has successfully converged to a high-quality output.

Now we can assemble these smaller components into the main state for our Supervisor agent, the brain of the entire operation.

```python
from langgraph.graph.message import add_messages

class SupervisorState(TypedDict):
    """The advanced, hierarchical state for the main Supervisor agent, the central workbench for the diffusion process."""
    # A standard field for accumulating the conversational history with the Supervisor.
    supervisor_messages: Annotated[Sequence[BaseMessage], add_messages]
    
    # These are the core artifacts of the research process that the Supervisor manages.
    research_brief: str
    draft_report: str
    
    # This is a key memory management design. 'raw_notes' is a temporary, high-volume buffer
    # for unprocessed search results. 'knowledge_base' is the permanent, structured, and pruned storage.
    raw_notes: Annotated[List[str], operator.add] 
    knowledge_base: Annotated[List[Fact], operator.add]
    
    # A simple counter to prevent infinite loops in our iterative process.
    research_iterations: int
    
    # These fields manage the self-correction and adversarial feedback loops.
    active_critiques: Annotated[List[Critique], operator.add]
    quality_history: Annotated[List[QualityMetric], operator.add]

    # A boolean flag that the Evaluator can set to signal to the Supervisor that the draft quality is unacceptably low.
    needs_quality_repair: bool
```

The `SupervisorState` is the central **workbench** for our entire diffusion process. It is a data structure that holds everything the Supervisor needs to make decisions.

The distinction between `raw_notes` and `knowledge_base` is a piece for managing the agent cognitive load.

1.  The `raw_notes` buffer will be intentionally cleared by our `Context Pruning` node, preventing the context window from overflowing.
2.  While the valuable, extracted `Fact` objects are preserved in the permanent `knowledge_base`.

We also need to define the states for our other sub-graphs, such as the individual `ResearcherAgent` and the top-level, user-facing graph.

```python
from langgraph.graph import MessagesState

# The state for the "worker" research agent sub-graph.
class ResearcherState(TypedDict):
    researcher_messages: Annotated[Sequence[BaseMessage], add_messages]
    tool_call_iterations: int
    research_topic: str

    # The final, cleaned-up output of a research run.
    compressed_research: str

    # The temporary buffer of raw search results for this specific worker.
    raw_notes: Annotated[List[str], operator.add]

# A specialized state defining the output of the research agent sub-graph.
class ResearcherOutputState(TypedDict):
    compressed_research: str
    raw_notes: Annotated[List[str], operator.add]
    researcher_messages: Annotated[Sequence[BaseMessage], add_messages]

# The states for the top-level, user-facing graph.
class AgentInputState(MessagesState):
    """The initial input state, which only contains the user's messages."""
    pass

class AgentState(MessagesState):
    """The main state for the full multi-agent system, which accumulates all final artifacts."""
    research_brief: Optional[str]
    supervisor_messages: Annotated[Sequence[BaseMessage], add_messages]
    raw_notes: Annotated[list[str], operator.add] = []

    notes: Annotated[list[str], operator.add] = [] # The final, curated notes for the writer.
    draft_report: str
    final_report: str
```

These additional state definitions provide the specific memory structures needed for each of our distinct sub-graphs.

1.  The `ResearcherState` can be thought of as the **private notebook** for a single research agent on a specific sub-task.
2.  The main `AgentState`, on the other hand, is the final p**roject folder** where all the completed deliverables (`research_brief`, `notes`, `draft_report`) are collected before being assembled into the `final_report`.
3.  This hierarchical state design is what allows us to build complex, nested agentic workflows in a clean and maintainable way.

### Creating Toolset for Research and Refinement

Our agents now have a structured memory which we can call **canvas**. Next, we need to give them the tools they will use to interact with the external knowledge, gather information, and refine their work.

> In an agentic system, tools are the bridge between the LLM internal reasoning and external action.

![Creating Toolset (Created by Fareed Khan)](https://miro.medium.com/v2/resize:fit:1400/1*uwcPRZDmdfLBUPpJ4kZvcQ.png)

We will define a set of specialized tools that our Supervisor agent can call. This includes a tool for **delegating parallel research**, a tool for completing the research process, and crucially, a `refine_draft_report` tool which is the core mechanism of our **"denoising"** step.

Let’s begin by defining the `ConductResearch` tool. This tool not goingn to perform the research itself. Instead, it acts as a delegation mechanism, allowing the Supervisor to spawn one or more parallel **"worker"** research agents.

```python
from langchain_core.tools import tool

@tool
class ConductResearch(BaseModel):
    """A tool for delegating a specific research task to a specialized sub-agent. The Supervisor uses this to fan out work."""
    # The detailed research topic for the sub-agent. This needs to be a complete, standalone instruction.
    research_topic: str = Field(
        description="The topic to research. Should be a single, self-contained topic described in high detail.",
    )
```

The `ConductResearch` tool is the **work order** for our system. It's a simple Pydantic model that encapsulates a single research task.

1.  The key architectural concept here is that when the Supervisor agent decides to use this tool, our `LangGraph` workflow will intercept the call.
2.  Instead of executing a simple function, it will trigger our entire, complex `researcher_agent` sub-graph, which we will build in upcoming section. This makes the tool a multi-step process.

Next, we are going to define the tool that signals the end of the iterative research phase.

```python
@tool
class ResearchComplete(BaseModel):
    """A tool for the Supervisor to signal that the research process is complete and the final report can be generated."""
    # This tool takes no arguments. Its invocation is the signal.
    pass
```

The `ResearchComplete` tool is a simple control signal. It provides a formal, structured way for the Supervisor agent to declare that its iterative diffusion process has converged and that it is confident in the quality of the current draft.

> When our graph sees this tool being called, it knows to exit the main refinement loop and proceed to the final report generation step.

Now, we will implement a tool that allows our agents to **“think”** and reflect on their actions, creating a more transparent and strategic reasoning process.

```python
@tool(parse_docstring=True)
def think_tool(reflection: str) -> str:
    """
    Tool for strategic reflection on research progress and decision-making.

    Use this tool after each search to analyze results and plan next steps systematically.
    This creates a deliberate pause in the research workflow for quality decision-making.
    Args:
        reflection: Your detailed reflection on research progress, findings, gaps, and next steps.
    Returns:
        Confirmation that reflection was recorded for decision-making.
    """
    return f"Reflection recorded: {reflection}"
```

In this component we are enabling a **chain-of-thought** style of reasoning within our agents.

By instructing our agents (via their prompts) to use this tool after every search, we are forcing them to pause, verbalize their analysis of the retrieved information, and explicitly state their plan for the next step.

This not only leads to more strategic research but also makes the agent internal monologue visible in our `LangSmith` traces, which is invaluable for debugging and understanding its decision-making process.

### Defining the Core Utility

In every agentic system we need a set of simple helper functions that we are going to use throughout the pipeline.

![Core Function (Created by Fareed Khan)](https://miro.medium.com/v2/resize:fit:1400/1*YUZWh4g1UbxjSiIpCFFxzA.png)

So to do that, we will start with a basic utility to get the current date, which we can inject into our prompts to give our agents temporal context.

```python
from datetime import datetime

def get_today_str() -> str:
    """A simple utility function to get the current date in a human-readable string format."""
    # We format the date as "Day Mon Day, Year" (e.g., "Mon Dec 25, 2025").
    return datetime.now().strftime("%a %b %-d, %Y")
```

The `get_today_str` function gives us the current date into our prompts, we ground our agents in the present moment.

This is particularly important for research tasks, as it helps the agent understand that it should be looking for the most recent, up-to-date information available. It's a simple way to combat the static nature of an LLM's training data.

## Initial Noise and Guidance Signal

With our foundational workspace like the states, tools, and some other utilities are coded, we can now build our first functional component of our deep agentic architecture.

![Initial Noise Guide (Created by Fareed Khan)](https://miro.medium.com/v2/resize:fit:2000/1*65hmnHA5qU07AnolagwIkA.png)

This initial sub-graph is the front component of our system. Its job is to manage the initial interaction with the user, which make sure that …

> our deep thinking system have a clear, unambiguous task before we kick off the expensive, iterative diffusion process.

By separating the initial **scoping** from the main **research** loop, we create a efficient system.

We prevent the agent from wasting time and resources researching **a poorly defined query**.

In the language of our diffusion model, this sub-graph is responsible for two things: generating the **“guidance signal”** (the research brief) that will steer the entire process, and creating the initial **“noisy image”** (the first draft) that our main engine will iteratively denoise.

We will now build this sub-graph. It will consist of three sequential nodes, each performing a distinct and critical task in the initialization of our research process.

### **Node 1 for Clarifying User Intent**

The first agent a user interacts with is arguably the most important for setting expectations and ensuring a successful outcome.

![Clarifying User Intent (Created by Fareed Khan)](https://miro.medium.com/v2/resize:fit:2000/1*H8rC2UYFlUQyZAe2NHH80Q.png)

We will start by building the `clarify_with_user` node. This agent sole responsibility is to act as a gatekeeper. It analyzes the initial conversation history and makes a critical decision:

> "Do I have enough information to start a high-quality research process, or do I need to pause and ask for more information?"

First, let’s define the prompt that will guide this agent’s decision-making process.

```python
# This prompt guides the first agent in our workflow, which decides if it has enough information from the user.
clarify_with_user_instructions="""
These are the messages that have been exchanged so far from the user asking for the report:
<Messages>
{messages}
</Messages>

Today's date is {date}.

Assess whether you need to ask a clarifying question, or if the user has already provided enough information for you to start research.
IMPORTANT: If you can see in the messages history that you have already asked a clarifying question, you almost always do not need to ask another one. Only ask another question if ABSOLUTELY NECESSARY.

If there are acronyms, abbreviations, or unknown terms, ask the user to clarify.
If you need to ask a question, follow these guidelines:
- Be concise while gathering all necessary information
- Make sure to gather all the information needed to carry out the research task in a concise, well-structured manner.
- Use bullet points or numbered lists if appropriate for clarity. Make sure that this uses markdown formatting and will be rendered correctly if the string output is passed to a markdown renderer.
- Don't ask for unnecessary information, or information that the user has already provided. If you can see that the user has already provided the information, do not ask for it again.

Respond in valid JSON format with these exact keys:
"need_clarification": boolean,
"question": "<question to ask the user to clarify the report scope>",
"verification": "<verification message that we will start research>"

If you need to ask a clarifying question, return:
"need_clarification": true,
"question": "<your clarifying question>",
"verification": ""

If you do not need to ask a clarifying question, return:
"need_clarification": false,
"question": "",
"verification": "<acknowledgement message that you will now start research based on the provided information>"

For the verification message when no clarification is needed:
- Acknowledge that you have sufficient information to proceed
- Briefly summarize the key aspects of what you understand from their request
- Confirm that you will now begin the research process
- Keep the message concise and professional
"""
```

The `clarify_with_user_instructions` prompt is our user-facing agent.

1.  Its job is to ensure that we don't start a complex and expensive research process with an ambiguous or incomplete request.
2.  The instruction **"If you have already asked a clarifying question... do not ask another one"** is a key piece of engineering to prevent annoying, repetitive conversational loops and improve the user experience.

Next, we need a Pydantic model to structure the output of this agent, ensuring its decision is always machine-readable.

```python
class ClarifyWithUser(BaseModel):
    """A Pydantic schema for the output of the user clarification decision agent."""

    # This boolean is the core of the decision-making process.
    need_clarification: bool = Field(
        description="Whether the user needs to be asked a clarifying question.",
    )
    # The question to be asked if clarification is needed.
    question: str = Field(
        description="A question to ask the user to clarify the report scope",
    )
    # A confirmation message to send to the user if no clarification is needed.
    verification: str = Field(
        description="A verification message to confirm that research will begin.",
    )
```

This `ClarifyWithUser` schema is the formal contract for our intiial node agent. It forces the LLM to make a clear, binary `need_clarification` decision and to provide the appropriate text for either continuing the conversation or proceeding with the research.

Now, we can build the `clarify_with_user` node function itself.

```python
from langgraph.types import Command
from langchain_core.messages import AIMessage, HumanMessage, get_buffer_string
from typing import Literal

def clarify_with_user(state: AgentState) -> Command[Literal["write_research_brief", END]]:
    """
    This node acts as a gatekeeper. It determines if the user's request has enough detail to proceed.
    If not, it HALTS the graph and asks a clarifying question. If yes, it proceeds to the next step.
    """

    # 1. We first format the entire conversation history into a single string for the LLM.
    messages_text = get_buffer_string(state["messages"])
    current_date = get_today_str()

    # 2. We bind our 'ClarifyWithUser' Pydantic schema to the model. This forces a structured JSON output.
    structured_output_model = model.with_structured_output(ClarifyWithUser)

    # 3. We invoke the LLM with our detailed 'clarify_with_user_instructions' prompt.
    response = structured_output_model.invoke([
        HumanMessage(content=clarify_with_user_instructions.format(
            messages=messages_text, 
            date=current_date
        ))
    ])

    # 4. This is the core logic. We check the 'need_clarification' boolean from the LLM's response.
    if response.need_clarification:

        # If clarification is needed, we return a special 'Command' object.
        # 'goto=END' tells LangGraph to STOP execution here.
        # 'update={...}' adds the AI's clarifying question to the message history before stopping.
        return Command(
            goto=END, 
            update={"messages": [AIMessage(content=response.question)]}
        )
    else:

        # If no clarification is needed, we return another Command.
        # 'goto="write_research_brief"' directs the graph to proceed to the next node.
        # We add the AI's verification message to the history for a clean conversational flow.
        return Command(
            goto="write_research_brief",
            update={"messages": [AIMessage(content=response.verification)]}
        )
```

You might wonder what happens when we return `Command(goto=END)`. In a stateful framework like LangGraph, this does not crash the program. Instead, it suspends the workflow. The graph state is persisted to memory or a database, effectively putting the agent to sleep.

When the user provides clarifying information, the graph wakes up, updates the state, and resumes execution. It does not start over but continues exactly from where it left off. This persistent `Human-in-the-Loop` capability is essential for long-running research tasks.

### **Node 2 for Writing the Research Brief**

Once our gatekeeper (initial) agent has confirmed that the user request is clear and sufficient, we need to transform that (potentially messy) conversational history into a formal, unambiguous set of instructions for our research agents. This is the job of the `write_research_brief` node.

> This agent acts as an expert analyst. It reads the entire confirmed conversation and distills it into a single, comprehensive `research_brief`.

![Research Brief (Created by Fareed Khan)](https://miro.medium.com/v2/resize:fit:2000/1*ANOapT8FZSQvwkpFEbrn-A.png)

This brief is arguably the most important artifact in our entire system. It becomes the **guidance signal** or **ground truth** for the rest of the diffusion process.

Every subsequent step from the targeted research of the worker agents to the critical feedback from the Red Team and the final evaluation will be measured against this brief.

First, let’s define the prompt that will guide this agent’s crucial transformation task.

```python
# This prompt transforms the informal user conversation into a formal, structured research brief.
transform_messages_into_research_topic_human_msg_prompt = """You will be given a set of messages that have been exchanged so far between yourself and the user. 
Your job is to translate these messages into a more detailed and concrete research question that will be used to guide the research.

The messages that have been exchanged so far between yourself and the user are:
<Messages>
{messages}
</Messages>

CRITICAL: Make sure the answer is written in the same language as the human messages!
For example, if the user's messages are in English, then MAKE SURE you write your response in English. If the user's messages are in Chinese, then MAKE SURE you write your entire response in Chinese.
This is critical. The user will only understand the answer if it is written in the same language as their input message.

Today's date is {date}.

You will return a single research question that will be used to guide the research.

Guidelines:
1. Maximize Specificity and Detail
- Include all known user preferences and explicitly list key attributes or dimensions to consider.
- It is important that all details from the user are included in the instructions.

2. Handle Unstated Dimensions Carefully
- When research quality requires considering additional dimensions that the user hasn't specified, acknowledge them as open considerations rather than assumed preferences.
- Example: Instead of assuming "budget-friendly options," say "consider all price ranges unless cost constraints are specified."
- Only mention dimensions that are genuinely necessary for comprehensive research in that domain.

3. Avoid Unwarranted Assumptions
- Never invent specific user preferences, constraints, or requirements that weren't stated.
- If the user hasn't provided a particular detail, explicitly note this lack of specification.
- Guide the researcher to treat unspecified aspects as flexible rather than making assumptions.

4. Distinguish Between Research Scope and User Preferences
- Research scope: What topics/dimensions should be investigated (can be broader than user's explicit mentions)
- User preferences: Specific constraints, requirements, or preferences (must only include what user stated)
- Example: "Research coffee quality factors (including bean sourcing, roasting methods, brewing techniques) for San Francisco coffee shops, with primary focus on taste as specified by the user."

5. Use the First Person
- Phrase the request from the perspective of the user.

6. Sources
- If specific sources should be prioritized, specify them in the research question.
- For product and travel research, prefer linking directly to official or primary websites (e.g., official brand sites, manufacturer pages, or reputable e-commerce platforms like Amazon for user reviews) rather than aggregator sites or SEO-heavy blogs.
- For academic or scientific queries, prefer linking directly to the original paper or official journal publication rather than survey papers or secondary summaries.
- For people, try linking directly to their LinkedIn profile, or their personal website if they have one.
- If the query is in a specific language, prioritize sources published in that language.

REMEMBER:
Make sure the research brief is in the SAME language as the human messages in the message history.
"""
```

The `transform_messages_into_research_topic_human_msg_prompt` takes the raw, often informal, back-and-forth of a user conversation and instructs the LLM to distill it into a single, comprehensive, and unambiguous `research_brief`. The guidelines such as **"Handle Unstated Dimensions Carefully"** and **"Avoid Unwarranted Assumptions"** are to prevent the LLM from hallucinating or making the kind of logical leaps that can derail a research project.

You will notice a specific, repeated instruction in the prompt:

> *“Make sure the answer is written in the same language as the human messages”*

**Standard LLMs often default to English when performing reasoning tasks or reading English documentation**. By explicitly requiring the agent to mirror the user’s language in the `research_brief` and subsequent drafts, we ensure that the system remains accessible and effective for users across different linguistic backgrounds.

Next, we will define the Pydantic schema for the output of this node.

```python
class ResearchQuestion(BaseModel):
    """A Pydantic schema for the structured output of the research brief generation agent."""

    # This single field will contain the complete, detailed research brief.
    research_brief: str = Field(
        description="A research question that will be used to guide the research.",
    )
```

It make sure that the output of our brief-writing agent is always a clean JSON object containing a single `research_brief` string. This makes it easy to extract this critical piece of information and save it to our `AgentState`.

Now, we can build the `write_research_brief` node function itself.

```python
def write_research_brief(state: AgentState) -> Command[Literal["write_draft_report"]]:
    """
    This node transforms the confirmed conversation history into a single, comprehensive research brief.
    """
    # 1. We bind our 'ResearchQuestion' Pydantic schema to the model to ensure structured output.
    structured_output_model = model.with_structured_output(ResearchQuestion)


    # 2. We invoke the LLM with our specialized 'transform_messages...' prompt and the conversation history.
    response = structured_output_model.invoke([
        HumanMessage(content=transform_messages_into_research_topic_human_msg_prompt.format(
            messages=get_buffer_string(state.get("messages", [])),
            date=get_today_str()
        ))
    ])

    # 3. We return a Command to update the state with the new research_brief
    #    and direct the graph to proceed to the 'write_draft_report' node.
    return Command(
            goto="write_draft_report", 
            update={"research_brief": response.research_brief}
        )
```

The `write_research_brief` function takes the informal user dialogue and converts it into a canonical, structured instruction set for the rest of the system.

1.  By using a dedicated, highly-detailed prompt and a strict output schema, we ensure that the generated `research_brief` is specific, comprehensive, and free of the ambiguities that can lead to flawed research.
2.  The `Command` it returns performs two actions: it updates the `AgentState` by populating the `research_brief` field, and it explicitly pushes the workflow forward to the next and final step of our scoping sub-graph.

### Node 3 for Generating the Initial Draft Report

This is the final step of our **front sub-graph** and the beginning of our guided diffusion process. The `write_draft_report` node takes the clean, formal `research_brief` and generates the very first version of our report.

![Initial Draft Report (Created by Fareed Khan)](https://miro.medium.com/v2/resize:fit:2000/1*K9Itz4_3m_P6R0x_qM22Dw.png)

This initial draft is not expected to be perfect. In fact, it is intentionally generated without any external research tools. It will be based solely on the parametric knowledge of the `creative_model`.

This means it will likely contain generic information, plausible-sounding but unverified facts, and potential hallucinations. This is by design. This draft is our **noisy image** the raw material that our main Supervisor loop will now iteratively denoise, critique, and refine towards a high-quality, fact-based final output.

First, let’s define the prompt that will guide our creative model in generating this initial draft.

```python
# This prompt guides the model to generate a first-pass draft based only on the research brief.
draft_report_generation_prompt = """Based on all the research in your knowledge base, create a comprehensive, well-structured answer to the overall research brief:
<Research Brief>
{research_brief}
</Research Brief>

CRITICAL: Make sure the answer is written in the same language as the human messages!
For example, if the user's messages are in English, then MAKE SURE you write your response in English. If the user's messages are in Chinese, then MAKE SURE you write your entire response in Chinese.
This is critical. The user will only understand the answer if it is written in the same language as their input message.

Today's date is {date}.

Please create a detailed answer to the overall research brief that:
1. Is well-organized with proper headings (# for title, ## for sections, ### for subsections)
2. Includes specific facts and insights from the research
3. References relevant sources using [Title](URL) format
4. Provides a balanced, thorough analysis. Be as comprehensive as possible, and include all information that is relevant to the overall research question. People are using you for deep research and will expect detailed, comprehensive answers.
5. Includes a "Sources" section at the end with all referenced links

You can structure your report in a number of different ways. Here are some examples:

To answer a question that asks you to compare two things, you might structure your report like this:
1/ intro
2/ overview of topic A
3/ overview of topic B
4/ comparison between A and B
5/ conclusion

To answer a question that asks you to return a list of things, you might only need a single section which is the entire list.
1/ list of things or table of things
Or, you could choose to make each item in the list a separate section in the report. When asked for lists, you don't need an introduction or conclusion.
1/ item 1
2/ item 2
3/ item 3

To answer a question that asks you to summarize a topic, give a report, or give an overview, you might structure your report like this:
1/ overview of topic
2/ concept 1
3/ concept 2
4/ concept 3
5/ conclusion

If you think you can answer the question with a single section, you can do that too!
1/ answer

REMEMBER: Section is a VERY fluid and loose concept. You can structure your report however you think is best, including in ways that are not listed above!
Make sure that your sections are cohesive, and make sense for the reader.

For each section of the report, do the following:
- Use simple, clear language
- Use ## for section title (Markdown format) for each section of the report
- Do NOT ever refer to yourself as the writer of the report. This should be a professional report without any self-referential language. 
- Do not say what you are doing in the report. Just write the report without any commentary from yourself.
- Each section should be as long as necessary to deeply answer the question with the information you have gathered. It is expected that sections will be fairly long and verbose. You are writing a deep research report, and users will expect a thorough answer.
- Use bullet points to list out information when appropriate, but by default, write in paragraph form.

REMEMBER:
The brief and research may be in English, but you need to translate this information to the right language when writing the final answer.
Make sure the final answer report is in the SAME language as the human messages in the message history.

Format the report in clear markdown with proper structure and include source references where appropriate.

<Citation Rules>
- Assign each unique URL a single citation number in your text
- End with ### Sources that lists each source with corresponding numbers
- IMPORTANT: Number sources sequentially without gaps (1,2,3,4...) in the final list regardless of which sources you choose
- Each source should be a separate line item in a list, so that in markdown it is rendered as a list.
- Example format:
  [1] Source Title: URL
  [2] Source Title: URL
- Citations are extremely important. Make sure to include these, and pay a lot of attention to getting these right. Users will often use these citations to look into more information.
</Citation Rules>
"""
```

We are explicitly telling the model to generate a comprehensive draft based on its pre-existing knowledge. The instruction to acknowledge where citations are needed is a key feature, it primes the model to recognize the gaps in its own knowledge, setting the stage for the targeted research that will follow in the main diffusion loop.

Next, we will define the Pydantic schema for the output of this node.

```python
class DraftReport(BaseModel):
    """A Pydantic schema for the structured output of the initial draft generation agent."""

    # This single field will contain the complete, unresearched initial draft report.
    draft_report: str = Field(
        description="A draft report that will be used as the starting point for the diffusion process.",
    )
```

This `DraftReport` schema ensures that the output of our drafting agent is always a clean JSON object containing the `draft_report` string. This makes it easy and reliable to save this crucial artifact to our `AgentState`.

Now, we can build the `write_draft_report` node function itself.

```python
# Our creative model
creative_model = init_chat_model(model="openai:gpt-5")

def write_draft_report(state: AgentState) -> dict:
    """
    This node takes the research brief and generates an initial, unresearched draft.
    This serves as the "noisy" starting point for our diffusion process.
    """
    # 1. We use our 'creative_model' for this task and bind it to the 'DraftReport' schema.
    structured_output_model = creative_model.with_structured_output(DraftReport)
    research_brief = state.get("research_brief", "")
    
    # 2. We format the prompt for the drafter, injecting the research brief and the current date.
    draft_report_prompt_formatted = draft_report_generation_prompt.format(
        research_brief=research_brief,
        date=get_today_str()
    )

    # 3. We invoke the LLM to generate the initial "noisy" draft.
    response = structured_output_model.invoke([HumanMessage(content=draft_report_prompt_formatted)])

    # 4. This node returns a simple dictionary update. This is the final output of the 'scope_research' sub-graph.
    #    The 'supervisor_messages' field is populated to "hand off" the initial state to the main Supervisor loop.
    return {
        "research_brief": research_brief,
        "draft_report": response.draft_report, 
        "supervisor_messages": ["Here is the draft report: " + response.draft_report, research_brief]
    }
```

The `write_draft_report` function is the final step in our initialization process.

1.  It generates the `draft_report`, which is the central object that will be iteratively improved in the main loop. The most important action it takes is populating the `supervisor_messages` field in the state.
2.  This is the formal **hand-off**, It passes both the new draft and the original research brief to the Supervisor agent, effectively saying, **"Here is the starting point (the noisy image), and here is the goal (the guidance signal). Your work begins now"**.
3.  This return value concludes the execution of our scoping sub-graph and provides the initial state for the main diffusion engine we will build next.

## Guidance Generation Engine

With our **initial noisy draft** and a clear research brief in hand, our Supervisor agent is now ready to begin the diffusion process.

![Guidance Generation Engine (Created by Fareed Khan)](https://miro.medium.com/v2/resize:fit:1400/1*EDqD2ppR2t8FiP55tsUTGg.png)

Its first step in any refinement cycle is to identify gaps or weaknesses in the current draft and gather external facts to guide the **“denoising”**. To do this, it will delegate targeted research tasks to a specialized **Research Agent**.

Our Research Agent is not a single node, it’s a complete, self-contained sub-graph.

> It implements a ReAct-style (Reason-Act) loop, allowing it to **think**, use tools (like web search), and reflect on the results to gather information on a specific topic.

The Supervisor can spawn multiple instances of this sub-graph to run in parallel, creating a powerful “scatter-gather” research engine that can investigate multiple lines of inquiry simultaneously.

In this section, here is what we are going to do:

1.  We will **build the Core ReAct Loop** by implementing the `llm_call` and `tool_node` functions that form the central “think–act” cycle of our research agent.
2.  Next, we will **engineer a Reflective Process** by introducing a `think_tool`, enabling the agent to pause, reflect on its findings, and plan its next search strategically.
3.  We will then **build the Full Web Search Capability** by implementing the complete multi-stage pipeline for our `tavily_search` tool, including deduplication and summarization.
4.  After that, we will **create the Compression Node** by developing the `compress_research` node, which takes the raw, unstructured output from the ReAct loop and refines it into a clear, cohesive summary for the Supervisor.
5.  Finally, we will **assemble the Sub-Graph**, connecting all these nodes in LangGraph to produce a fully functional, runnable `researcher_agent`.

### Creating the ReAct-style Loop

First, we need to define the core **thinking part of our researcher**. This is the `llm_call` node.

![ReAct Loop (Created by Fareed Khan)](https://miro.medium.com/v2/resize:fit:1400/1*31h5qkaX1ZzQ1q_iEaa5BA.png)

Its job is to look at the current state of its research (the conversation history) and decide what to do next: either call a tool to gather more information or, if it believes its research on its assigned sub-topic is complete, finish its work.

Let’s start by defining the prompt that gives our researcher its persona and instructions.

```python
# This prompt defines the behavior of our specialized, parallel research agents.
research_agent_prompt =  """You are a research assistant conducting research on the user's input topic. For context, today's date is {date}.

<Task>
Your job is to use tools to gather information about the user's input topic.
You can use any of the tools provided to you to find resources that can help answer the research question. You can call these tools in series or in parallel, your research is conducted in a tool-calling loop.
</Task>

<Available Tools>
You have access to two main tools:
1. **tavily_search**: For conducting web searches to gather information
2. **think_tool**: For reflection and strategic planning during research

**CRITICAL: Use think_tool after each search to reflect on results and plan next steps**
</Available Tools>

<Instructions>
Think like a human researcher with limited time. Follow these steps:

1. **Read the question carefully** - What specific information does the user need?
2. **Start with broader searches** - Use broad, comprehensive queries first
3. **After each search, pause and assess** - Do I have enough to answer? What's still missing?
4. **Execute narrower searches as you gather information** - Fill in the gaps
5. **Stop when you can answer confidently** - Don't keep searching for perfection
</Instructions>

<Hard Limits>
**Tool Call Budgets** (Prevent excessive searching):
- **Simple queries**: Use 2-3 search tool calls maximum
- **Complex queries**: Use up to 5 search tool calls maximum
- **Always stop**: After 5 search tool calls if you cannot find the right sources

**Stop Immediately When**:
- You can answer the user's question comprehensively
- You have 3+ relevant examples/sources for the question
- Your last 2 searches returned similar information
</Hard Limits>

<Show Your Thinking>
After each search tool call, use think_tool to analyze the results:
- What key information did I find?
- What's missing?
- Do I have enough to answer the question comprehensively?
- Should I search more or provide my answer?
</Show Your Thinking>
"""
```

The `research_agent_prompt` is the **Standard Operating Procedure** for our individual researchers.

It provides the agent with a clear task, a defined set of tools, and most importantly, a set of **“Hard Limits”** or constraints. Guidelines such as **“Use `think_tool` after each search”** and **“Always stop after five search tool calls”** are vital for creating a strategic and efficient research process.

These limits help prevent the agent from getting stuck in long, unproductive loops, ensuring focused and cost-effective performance.

Now, we can define the `llm_call` node, which is the "brain" of the researcher.

```python
from langchain_core.messages import SystemMessage, ToolMessage, filter_messages

def llm_call(state: ResearcherState):
    """The 'brain' of the researcher: analyzes the current state and decides on the next action (call a tool or finish)."""

    # This node invokes our tool-bound model with the specific research_agent_prompt and the current message history for this sub-task.
    return {
        "researcher_messages": [
            model_with_tools.invoke(
                [SystemMessage(content=research_agent_prompt.format(date=get_today_str()))] + state["researcher_messages"]
            )
        ]
    }
```

The `llm_call` function is the reasoning engine for our worker agent. It's a simple but powerful node that takes the entire `researcher_messages` history for its specific sub-task and passes it to our `model_with_tools`.

The model response will either be a final thought or, more likely, a decision to call one of its available tools (`tavily_search` or `think_tool`).

Next, we need the **“hands”** of our researcher. The `tool_node` is responsible for executing any tool calls that the `llm_call` node has planned.

```python
def tool_node(state: ResearcherState):
    """The 'hands' of the researcher: executes all tool calls from the previous LLM response."""

    # We get the most recent message from the state, which should contain the tool calls.
    tool_calls = state["researcher_messages"][-1].tool_calls

    # We execute all the planned tool calls.
    observations = []
    for tool_call in tool_calls:

        # We look up the correct tool function by its name.
        tool = tools_by_name[tool_call["name"]]
        observations.append(tool.invoke(tool_call["args"]))

    # We format the results of the tool calls into 'ToolMessage' objects.
    # This is the standard way to return tool results to the LLM in LangGraph.
    tool_outputs = [
        ToolMessage(
            content=str(observation),
            name=tool_call["name"],
            tool_call_id=tool_call["id"]
        ) for observation, tool_call in zip(observations, tool_calls)
    ]

    # We return the tool outputs to be added to the message history.
    return {"researcher_messages": tool_outputs}
```

The `tool_node` is the action part of our ReAct loop. It inspects the last `AIMessage`, extracts the `tool_calls`, and executes them. By returning the results as `ToolMessage` objects, it provides the LLM with the **observations** it needs for its next reasoning step.

The loop `llm_call -> tool_node -> llm_call` is what allows the agent to iteratively search, find information, and decide if it needs to search again.

Now we need the routing logic that controls this loop. The `should_continue` function acts as a conditional edge, checking if the LLM has decided to call a tool or if it has finished its research for this sub-task.

```python
def should_continue(state: ResearcherState) -> Literal["tool_node", "compress_research"]:
    """A conditional edge that determines whether to continue the ReAct loop or finish the research sub-task."""
    messages = state["researcher_messages"]
    last_message = messages[-1]

    # If the last message from the LLM contains tool calls, we continue the loop.
    if last_message.tool_calls:
        return "tool_node"

    # If there are no tool calls, the agent has decided its research is complete, and we proceed to the compression step.
    return "compress_research"
```

The `should_continue` function is a ritical router for our ReAct loop. It is the decision point that determines whether the agent continues to "act" (by calling tools) or whether it has gathered enough information and is ready to summarize its findings.

### Building the Web Search Capability

Our research agents need a window to the outside world to gather facts. While we have defined a `tavily_search` tool, a simple search is not enough. Raw webpage content is often verbose, full of boilerplate (like navigation menus and ads), and too large to fit into a context window.

![Web Search Pipeline (Created by Fareed Khan)](https://miro.medium.com/v2/resize:fit:1400/1*1BP2wtGMSwr7CC2M0Q5iEA.png)

1.  To solve this, we will build a multi-stage search utility belt. Instead of just searching, our `tavily_search` tool will create a sophisticated "Search -> Deduplicate -> Summarize -> Format" pipeline for every query.
2.  This way the information returned to our agent is not just raw data, but clean, concise, and relevant evidence.

First, let’s define the prompt that will guide our summarization model. This model’s job is to distill the raw HTML content of a webpage into a dense, factual summary.

```python
# This prompt guides the summarization model to extract the most critical information from a webpage.
summarize_webpage_prompt = """You are tasked with summarizing the raw content of a webpage retrieved from a web search. Your goal is to create a summary that preserves the most important information from the original web page. This summary will be used by a downstream research agent, so it's crucial to maintain the key details without losing essential information.

Here is the raw content of the webpage:

<webpage_content>
{webpage_content}
</webpage_content>

Please follow these guidelines to create your summary:

1. Identify and preserve the main topic or purpose of the webpage.
2. Retain key facts, statistics, and data points that are central to the content's message.
3. Keep important quotes from credible sources or experts.
4. Maintain the chronological order of events if the content is time-sensitive or historical.
5. Preserve any lists or step-by-step instructions if present.
6. Include relevant dates, names, and locations that are crucial to understanding the content.
7. Summarize lengthy explanations while keeping the core message intact.

When handling different types of content:

- For news articles: Focus on the who, what, when, where, why, and how.
- For scientific content: Preserve methodology, results, and conclusions.
- For opinion pieces: Maintain the main arguments and supporting points.
- For product pages: Keep key features, specifications, and unique selling points.

Your summary should be significantly shorter than the original content but comprehensive enough to stand alone as a source of information. Aim for about 25-30 percent of the original length, unless the content is already concise.

Present your summary in the following format:

```
{{
   "summary": "Your summary here, structured with appropriate paragraphs or bullet points as needed",
   "key_excerpts": "First important quote or excerpt, Second important quote or excerpt, Third important quote or excerpt, ...Add more excerpts as needed, up to a maximum of 5"
}}
```

Here are two examples of good summaries:

Example 1 (for a news article):
```json
{{
   "summary": "On July 15, 2023, NASA successfully launched the Artemis II mission from Kennedy Space Center. This marks the first crewed mission to the Moon since Apollo 17 in 1972. The four-person crew, led by Commander Jane Smith, will orbit the Moon for 10 days before returning to Earth. This mission is a crucial step in NASA's plans to establish a permanent human presence on the Moon by 2030.",
   "key_excerpts": "Artemis II represents a new era in space exploration, said NASA Administrator John Doe. The mission will test critical systems for future long-duration stays on the Moon, explained Lead Engineer Sarah Johnson. We're not just going back to the Moon, we're going forward to the Moon, Commander Jane Smith stated during the pre-launch press conference."
}}
```

Example 2 (for a scientific article):
```json
{{
   "summary": "A new study published in Nature Climate Change reveals that global sea levels are rising faster than previously thought. Researchers analyzed satellite data from 1993 to 2022 and found that the rate of sea-level rise has accelerated by 0.08 mm/year² over the past three decades. This acceleration is primarily attributed to melting ice sheets in Greenland and Antarctica. The study projects that if current trends continue, global sea levels could rise by up to 2 meters by 2100, posing significant risks to coastal communities worldwide.",
   "key_excerpts": "Our findings indicate a clear acceleration in sea-level rise, which has significant implications for coastal planning and adaptation strategies, lead author Dr. Emily Brown stated. The rate of ice sheet melt in Greenland and Antarctica has tripled since the 1990s, the study reports. Without immediate and substantial reductions in greenhouse gas emissions, we are looking at potentially catastrophic sea-level rise by the end of this century, warned co-author Professor Michael Green."  
}}
```

Remember, your goal is to create a summary that can be easily understood and utilized by a downstream research agent while preserving the most critical information from the original webpage.

Today's date is {date}.
"""
```

This `summarize_webpage_prompt` is a piece of our data processing pipeline. It instructs the LLM to act as an expert analyst, focusing on extracting verifiable facts, key quotes, and essential data points, while discarding the irrelevant **"fluff"** common in web content. This is the first step in our **"denoising"** of the raw search results.

Next, we need a Pydantic schema to structure the output of our summarization model.

```python
class Summary(BaseModel):
    """A Pydantic schema for the structured output of the webpage summarization model."""
 
   # The main, concise summary of the webpage.
    summary: str = Field(description="Concise summary of the webpage content")

    # A list of direct quotes or key excerpts to preserve important verbatim information.
    key_excerpts: str = Field(description="Important quotes and excerpts from the content")
```

The `Summary` schema makes our summarization step produces a predictable, two-part output. This separation is important, the `summary` provides the high-level gist, while the `key_excerpts` ensure that critical statements are not lost or paraphrased, preserving the factual integrity of the source.

Now, let’s build the utility functions that will form our search pipeline, starting with the function that calls the Tavily API.

```python
from tavily import TavilyClient

# We initialize the Tavily client.
tavily_client = TavilyClient()
MAX_CONTEXT_LENGTH = 250000

def tavily_search_multiple(
    search_queries: List[str], 
    max_results: int = 3, 
    topic: Literal["general", "news", "finance"] = "general", 
    include_raw_content: bool = True, 
    ) -> List[dict]:
    """A helper function to perform a search using the Tavily API for a list of queries."""

    print(f"--- [TOOL] Executing Tavily search for queries: {search_queries} ---")
    search_docs = []

    # We execute the searches for each query.
    for query in search_queries:
        result = tavily_client.search(
            query,
            max_results=max_results,
            include_raw_content=include_raw_content,
            topic=topic
        )
        search_docs.append(result)
    return search_docs
```

The `tavily_search_multiple` function is our direct interface to the Tavily search engine. It takes a list of search queries and returns the raw search results, including the full, unprocessed content of the webpages, which is what we'll need for our summarization step.

> You did also notice the topic argument in our tool definition. This allows the LLM to perform context switching.

1.  If the Supervisor asks a question about stock prices, the agent can programmatically switch the search topic from general to finance.
2.  If the question is about a breaking event, it can switch to news. This moves us beyond simple keyword matching and allows the agent to select the correct index for the job.

Next, we will build the function that orchestrates the summarization for a given piece of web content.

```python
# Summarization model
summarization_model = init_chat_model(model="openai:gpt-5")

def summarize_webpage_content(webpage_content: str) -> str:
    """Summarizes a single piece of webpage content using our configured summarization model."""
    try:
        # We bind our 'Summary' Pydantic schema to the summarization model.
        structured_model = summarization_model.with_structured_output(Summary)


        # We invoke the LLM with our detailed summarization prompt.
        summary_result = structured_model.invoke([
            HumanMessage(content=summarize_webpage_prompt.format(
                webpage_content=webpage_content, 
                date=get_today_str()
            ))
        ])

        # We format the structured output into a clean, human-readable string.
        formatted_summary = (
            f"<summary>\n{summary_result.summary}\n</summary>\n\n"
            f"<key_excerpts>\n{summary_result.key_excerpts}\n</key_excerpts>"
        )
        return formatted_summary
    except Exception as e:

        # If summarization fails, we fall back to a simple truncation of the raw content.
        print(f"Failed to summarize webpage: {str(e)}")
        return webpage_content[:1000] + "..." if len(webpage_content) > 1000 else webpage_content
```

The `summarize_webpage_content` function takes a potentially massive string of `webpage_content` and uses a structured-output LLM call to compress it into a dense, two-part summary. The `try...except` block is a key piece of engineering for robustness, ensuring that a failure in the summarization LLM doesn't crash the entire search process.

Now, we will code helper functions to manage the results from multiple, potentially overlapping, searches.

```python
def deduplicate_search_results(search_results: List[dict]) -> dict:
    """Deduplicates a list of search results based on the URL."""
    unique_results = {}

    for response in search_results:
        for result in response['results']:
            url = result['url']
            
            # We use the URL as a key in a dictionary to automatically handle duplicates.
            if url not in unique_results:
                unique_results[url] = result
    return unique_results
```

```python
def process_search_results(unique_results: dict) -> dict:
    """Processes a dictionary of unique search results by summarizing their raw content."""
    summarized_results = {}
    for url, result in unique_results.items():
        # If raw_content is available, we summarize it.
        if result.get("raw_content"):
            content = summarize_webpage_content(result['raw_content'][:MAX_CONTEXT_LENGTH])
        else:
            # Otherwise, we just use the short snippet provided by the search API.
            content = result['content']
        summarized_results[url] = {'title': result['title'], 'content': content}
    return summarized_results
```

```python
def format_search_output(summarized_results: dict) -> str:
    """Formats the final, summarized search results into a clean string for the agent."""
    if not summarized_results:
        return "No valid search results found."
    
    formatted_output = "Search results: \n\n"
    for i, (url, result) in enumerate(summarized_results.items(), 1):
        formatted_output += f"\n\n--- SOURCE {i}: {result['title']} ---\n"
        formatted_output += f"URL: {url}\n\n"
        formatted_output += f"SUMMARY:\n{result['content']}\n\n"
        formatted_output += "-" * 80 + "\n"
    return formatted_output
```

These three functions form our data processing pipeline.

1.  `deduplicate_search_results` prevents us from processing the same webpage multiple times.
2.  `process_search_results` orchestrates the summarization for all unique results.
3.  `format_search_output` then takes these processed results and formats them into a clean, well-structured, and human-readable string that will be returned to the agent as the final tool output.

Finally, we can wrap this entire pipeline into our decorated `tavily_search` tool.

```python
@tool(parse_docstring=True)
def tavily_search(
    query: str,
    max_results: Annotated[int, InjectedToolArg] = 3,
    topic: Annotated[Literal["general", "news", "finance"], InjectedToolArg] = "general",
    ) -> str:
    """
    A tool that fetches results from the Tavily search API and performs content summarization.


    Args:
        query: A single, specific search query to execute.
        max_results: The maximum number of results to return.
        topic: The topic to filter results by ('general', 'news', 'finance').
    Returns:
        A formatted string of the deduplicated and summarized search results.
    """

    # 1. Execute the search.
    search_results = tavily_search_multiple([query], max_results=max_results, topic=topic, include_raw_content=True)

    # 2. Deduplicate the results.
    unique_results = deduplicate_search_results(search_results)

    # 3. Process and summarize the content.
    summarized_results = process_search_results(unique_results)

    # 4. Format the final output.
    return format_search_output(summarized_results)
```

The decorated `tavily_search` tool is the final, clean interface that our research agent will interact with.

It completely abstracts away the complex, multi-step **"Search -> Deduplicate -> Summarize -> Format"** pipeline we've just built. The agent simply calls this tool with a query, and it receives a perfectly formatted, dense, and relevant block of evidence in return.

### Compressing the Findings

The output of a ReAct loop is often messy. The `researcher_messages` history will contain a mix of the agent's internal thoughts (from the `think_tool`), the verbose, summarized content from web searches, and the final AI responses.

![Finding Filtering (Created by Fareed Khan)](https://miro.medium.com/v2/resize:fit:2000/1*mz4kBzwgw33kdI6jD4zODA.png)

This is too noisy and unstructured to pass directly back to our Supervisor agent. The Supervisor needs a clean, comprehensive summary of the findings for its specific sub-task, not a raw log of the worker's entire thought process.

To solve this …

1.  We will now create a crucial final node for our research sub-graph: the `compress_research` node. This agent sole job is to act as a **librarian** or **"archivist"**.
2.  It reads the entire, messy history of a completed research run and "compresses" it into a clean, comprehensive, and well-cited summary.
3.  A key piece is its prompt is the instruction to explicitly filter out the agent's internal `think_tool` calls, ensuring the final report contains only the valuable, externally-sourced information.

First, let’s define the two prompts that will guide this compression agent.

```python
# The system prompt for our compression agent, instructing it on how to filter and format the research history.
compress_research_system_prompt = """You are a research assistant that has conducted research on a topic by calling several tools and web searches. Your job is now to clean up the findings, but preserve all of the relevant statements and information that the researcher has gathered. For context, today's date is {date}.

<Task>
You need to clean up information gathered from tool calls and web searches in the existing messages.
All relevant information should be repeated and rewritten verbatim, but in a cleaner format.
The purpose of this step is just to remove any obviously irrelevant or duplicate information.
For example, if three sources all say "X", you could say "These three sources all stated X".
Only these fully comprehensive cleaned findings are going to be returned to the user, so it's crucial that you don't lose any information from the raw messages.
</Task>

<Tool Call Filtering>
**IMPORTANT**: When processing the research messages, focus only on substantive research content:
- **Include**: All tavily_search results and findings from web searches
- **Exclude**: think_tool calls and responses - these are internal agent reflections for decision-making and should not be included in the final research report
- **Focus on**: Actual information gathered from external sources, not the agent's internal reasoning process

The think_tool calls contain strategic reflections and decision-making notes that are internal to the research process but do not contain factual information that should be preserved in the final report.
</Tool Call Filtering>

<Guidelines>
1. Your output findings should be fully comprehensive and include ALL of the information and sources that the researcher has gathered from tool calls and web searches. It is expected that you repeat key information verbatim.
2. This report can be as long as necessary to return ALL of the information that the researcher has gathered.
3. In your report, you should return inline citations for each source that the researcher found.
4. You should include a "Sources" section at the end of the report that lists all of the sources the researcher found with corresponding citations, cited against statements in the report.
5. Make sure to include ALL of the sources that the researcher gathered in the report, and how they were used to answer the question!
6. It's really important not to lose any sources. A later LLM will be used to merge this report with others, so having all of the sources is critical.
</Guidelines>

<Output Format>
The report should be structured like this:
**List of Queries and Tool Calls Made**
**Fully Comprehensive Findings**
**List of All Relevant Sources (with citations in the report)**
</Output Format>

<Citation Rules>
- Assign each unique URL a single citation number in your text
- End with ### Sources that lists each source with corresponding numbers
- IMPORTANT: Number sources sequentially without gaps (1,2,3,4...) in the final list regardless of which sources you choose
- Example format:
  [1] Source Title: URL
  [2] Source Title: URL
</Citation Rules>

Critical Reminder: It is extremely important that any information that is even remotely relevant to the user's research topic is preserved verbatim (e.g. don't rewrite it, don't summarize it, don't paraphrase it).
"""
```

These two prompts work together to define the `compress_research` agent task.

1.  The `compress_research_system_prompt` is the **Standard Operating Procedure**, providing the crucial `<Tool Call Filtering>` rule to ignore the `think_tool`.
2.  The `compress_research_human_message` provides the specific, run-time context, reminding the agent of the `RESEARCH TOPIC` to ensure its output is focused and relevant. The instruction to preserve information `verbatim` is key to preventing information loss during this compression step.

Now, we can build the `compress_research` node function itself.

```python
# Compress model
compress_model = init_chat_model(model="openai:gpt-5", max_tokens=32000)

def compress_research(state: ResearcherState) -> dict:
    """The final node in the research sub-graph: it compresses all findings from the ReAct loop into a clean, cited summary."""
    # 1. We format the system and human messages for our compression model.
    system_message = compress_research_system_prompt.format(date=get_today_str())

    # The full message history of the ReAct loop is passed as context.
    messages = [SystemMessage(content=system_message)] + state.get("researcher_messages", []) + [HumanMessage(content=compress_research_human_message.format(research_topic=state['research_topic']))]
    
    # 2. We invoke our powerful 'compress_model'.
    response = compress_model.invoke(messages)

    # 3. We also extract the raw, unprocessed notes from the tool and AI messages.
    #    This is for archival purposes and can be used by the Supervisor for deeper analysis if needed.
    raw_notes = [
        str(m.content) for m in filter_messages(
            state["researcher_messages"], 
            include_types=["tool", "ai"] # We only include the 'action' and 'observation' parts of the loop.
        )
    ]

    # 4. This node returns the final, clean outputs that will be passed out of the sub-graph.
    return {
        "compressed_research": str(response.content),
        "raw_notes": ["\n".join(raw_notes)]
    }
```

The `compress_research` function is an essential clean-up and formatting step.

1.  It acts as the bridge between the chaotic, internal process of the research agent and the clean, structured information that the Supervisor expects.
2.  It takes the entire messy history of the ReAct loop, filters out the internal monologue, and produces two key artifacts, the `compressed_research` summary for the Supervisor's immediate use, and the `raw_notes` for deeper, optional analysis. This separation of concerns is a key pattern for building clean interfaces between different agentic components.

Finally, we can assemble all these components into our complete, runnable `researcher_agent` sub-graph.

```python
from langgraph.graph import StateGraph, START, END

# We initialize a new StateGraph, specifying the input state and, importantly, the output schema for this sub-graph.
agent_builder = StateGraph(ResearcherState, output_schema=ResearcherOutputState)

# We add our three nodes: the thinker (llm_call), the actor (tool_node), and the final compressor.
agent_builder.add_node("llm_call", llm_call)
agent_builder.add_node("tool_node", tool_node)
agent_builder.add_node("compress_research", compress_research)

# The entry point for this sub-graph is always the 'llm_call' (the brain).
agent_builder.add_edge(START, "llm_call")

# After the brain thinks, our conditional edge, 'should_continue', decides what to do next.
agent_builder.add_conditional_edges(
    "llm_call",
    should_continue,
    {
        "tool_node": "tool_node", # If tools are needed, we go to the tool node.
        "compress_research": "compress_research", # If research is done, we proceed to the compression node.
    },
)

# After the tool node acts, the flow loops back to the brain to process the results of the action.
agent_builder.add_edge("tool_node", "llm_call")

# The compression node is the final step; its output is the output of the entire sub-graph, so we connect it to END.
agent_builder.add_edge("compress_research", END)

# We compile the graph into a runnable object.
researcher_agent = agent_builder.compile()
```

We have now successfully constructed our `researcher_agent` sub-graph. This is our **worker engine**.

It is a complete, self-contained agent that can take a single, specific research topic, perform an iterative ReAct-style research process using a sophisticated, multi-stage search tool, and return a clean, compressed summary of its findings along with the raw source material.

The Supervisor agent, which we will build in the next part, can now invoke this powerful sub-graph as if it were a simple tool.

1.  It can delegate complex research tasks even multiple in parallel and trust that it will receive a high-quality, well-structured, and predictable result for each one.
2.  This **graph-within-a-graph** design is a key architectural pattern for building complex, hierarchical agentic systems in a clean, maintainable, and scalable way.

## Creating the Core Denoising Loop

We can now construct the master orchestrator, the **Supervisor Agent**. This is the core of our Deep agentic system.

> It is not a simple agent, it’s a meta-agent whose job is to manage the entire iterative diffusion process.

![Core Denoising Loop (Created by Fareed Khan)](https://miro.medium.com/v2/resize:fit:2000/1*v1OsLVJOYGNsgmEDSgSdAw.png)

It analyzes the current state of the draft, decides what information is missing, delegates research tasks to the worker agents, and applies their findings to denoise and refine the report.

This Supervisor is the core of our `Critique -> Research -> Refine` loop. It is a cyclical, stateful process that allows the system to progressively improve its output, moving from a noisy initial draft towards a high-quality, fact-based final report.

### Building the Supervisor Node

The first component of our Supervisor is the node that performs the high-level strategic reasoning.

![Supervisor Node (Created by Fareed Khan)](https://miro.medium.com/v2/resize:fit:1400/1*W3UZSaVGRaH8nd_WE_kSEQ.png)

This `supervisor` node will analyze the full state of the system, including the current draft, the research brief, and any critical feedback from the adversarial Red Team or the programmatic evaluator. Based on this analysis, it will decide on the next set of actions, which will be encoded as tool calls.

First, let’s define the master prompt that encodes the diffusion algorithm for our Supervisor. This is the most important prompt in our entire system.

```python
# This is the master prompt for our Supervisor, defining the core diffusion/denoising algorithm.
lead_researcher_with_multiple_steps_diffusion_double_check_prompt = """You are a research supervisor. Your job is to conduct research by calling the "ConductResearch" tool and refine the draft report by calling "refine_draft_report" tool based on your new research findings. For context, today's date is {date}. You will follow the diffusion algorithm:

<Diffusion Algorithm>
1. generate the next research questions to address gaps in the draft report
2. **ConductResearch**: retrieve external information to provide concrete delta for denoising
3. **refine_draft_report**: remove “noise” (imprecision, incompleteness) from the draft report
4. **CompleteResearch**: complete research only based on ConductReserach tool's findings' completeness. it should not be based on the draft report. even if the draft report looks complete, you should continue doing the research until all the research findings are collected. You know the research findings are complete by running ConductResearch tool to generate diverse research questions to see if you cannot find any new findings. If the language from the human messages in the message history is not English, you know the research findings are complete by always running ConductResearch tool to generate another round of diverse research questions to check the comprehensiveness.

</Diffusion Algorithm>

<Task>
Your focus is to call the "ConductResearch" tool to conduct research against the overall research question passed in by the user and call "refine_draft_report" tool to refine the draft report with the new research findings. When you are completely satisfied with the research findings and the draft report returned from the tool calls, then you should call the "ResearchComplete" tool to indicate that you are done with your research.
</Task>

<Available Tools>
You have access to four main tools:
1. **ConductResearch**: Delegate research tasks to specialized sub-agents
2. **refine_draft_report**: Refine draft report using the findings from ConductResearch
3. **ResearchComplete**: Indicate that research is complete
4. **think_tool**: For reflection and strategic planning during research

**CRITICAL: Use think_tool before calling ConductResearch or refine_draft_report to plan your approach, and after each ConductResearch or refine_draft_report to assess progress**
**PARALLEL RESEARCH**: When you identify multiple independent sub-topics that can be explored simultaneously, make multiple ConductResearch tool calls in a single response to enable parallel research execution. This is more efficient than sequential research for comparative or multi-faceted questions. Use at most {max_concurrent_research_units} parallel agents per iteration.
</Available Tools>

<Instructions>
Think like a research manager with limited time and resources. Follow these steps:

1. **Read the question carefully** - What specific information does the user need?
2. **Decide how to delegate the research** - Carefully consider the question and decide how to delegate the research. Are there multiple independent directions that can be explored simultaneously?
3. **After each call to ConductResearch, pause and assess** - Do I have enough to answer? What's still missing? and call refine_draft_report to refine the draft report with the findings. Always run refine_draft_report after ConductResearch call.
4. **call CompleteResearch only based on ConductReserach tool's findings' completeness. it should not be based on the draft report. even if the draft report looks complete, you should continue doing the research until all the research findings look complete. You know the research findings are complete by running ConductResearch tool to generate diverse research questions to see if you cannot find any new findings. If the language from the human messages in the message history is not English, you know the research findings are complete by always running ConductResearch tool to generate another round of diverse research questions to check the comprehensiveness.
</Instructions>

<Hard Limits>
**Task Delegation Budgets** (Prevent excessive delegation):
- **Bias towards single agent** - Use single agent for simplicity unless the user request has clear opportunity for parallelization
- **Stop when you can answer confidently** - Don't keep delegating research for perfection
- **Limit tool calls** - Always stop after {max_researcher_iterations} tool calls to think_tool and ConductResearch if you cannot find the right sources
</Hard Limits>

<Show Your Thinking>
Before you call ConductResearch tool call, use think_tool to plan your approach:
- Can the task be broken down into smaller sub-tasks?

After each ConductResearch tool call, use think_tool to analyze the results:
- What key information did I find?
- What's missing?
- Do I have enough to answer the question comprehensively?
- Should I delegate more research or call ResearchComplete?
</Show Your Thinking>

<Scaling Rules>
**Simple fact-finding, lists, and rankings** can use a single sub-agent:
- *Example*: List the top 10 coffee shops in San Francisco → Use 1 sub-agent

**Comparisons presented in the user request** can use a sub-agent for each element of the comparison:
- *Example*: Compare OpenAI vs. Anthropic vs. DeepMind approaches to AI safety → Use 3 sub-agents
- Delegate clear, distinct, non-overlapping subtopics

**Important Reminders:**
- Each ConductResearch call spawns a dedicated research agent for that specific topic
- A separate agent will write the final report - you just need to gather information
- When calling ConductResearch, provide complete standalone instructions - sub-agents can't see other agents' work
- Do NOT use acronyms or abbreviations in your research questions, be very clear and specific
</Scaling Rules>
"""
```

This `lead_researcher_with_multiple_steps_diffusion_double_check_prompt` is the **source code** for our entire agentic process.

1.  It explicitly lays out the `<Diffusion Algorithm>` for the LLM to follow: `generate questions -> ConductResearch -> refine_draft_report`.
2.  It gives the Supervisor the authority to delegate parallel research (by making multiple `ConductResearch` tool calls), the responsibility to refine the draft with the `refine_draft_report` tool, and the logic to decide when the process has converged (`ResearchComplete`).

We also inject a specific variable, `{max_concurrent_research_units}`, directly into the system prompt. This serves as a strict budget constraint for the agent’s operations.

1.  Without it, an overly enthusiastic Supervisor might attempt to spawn twenty parallel researchers to solve a simple query, quickly exceeding rate limits and consuming unnecessary API credits.
2.  By hard-coding this limit into the prompt, we ensure that the agent remains autonomous while operating safely within predefined boundaries.

Now, we can build the `supervisor` node function itself. This node is asynchronous (`async def`) because it will be orchestrating potentially long-running, parallel sub-agent calls.

```python
async def supervisor(state: SupervisorState) -> Command[Literal["supervisor_tools"]]:
    """
    The 'Brain' of the diffusion process. This node analyzes the current state,
    including any critical feedback, and decides on the next set of actions (tool calls).
    """
    # 1. We get the current message history for the supervisor.
    supervisor_messages = state.get("supervisor_messages", [])
    
    # 2. We format the main system prompt with the diffusion algorithm instructions.
    system_message = lead_researcher_with_multiple_steps_diffusion_double_check_prompt.format(
        date=get_today_str(), 
        max_concurrent_research_units=max_concurrent_researchers,
        max_researcher_iterations=max_researcher_iterations
    )
    messages = [SystemMessage(content=system_message)] + supervisor_messages

    # 3. DYNAMIC CONTEXT INJECTION: We check for and inject any unaddressed adversarial feedback.
    # This is a critical self-correction mechanism.
    critiques = state.get("active_critiques", [])
    unaddressed = [c for c in critiques if not c.addressed]
    if unaddressed:
        critique_text = "\n".join([f"- {c.author} says: {c.concern}" for c in unaddressed])
        intervention = SystemMessage(content=f"""
        CRITICAL INTERVENTION REQUIRED.
        The following issues were detected by the Adversarial Team in your draft:
        {critique_text}
        
        You MUST address these issues in your next step.
        If the critique says citations are missing, call 'ConductResearch' to find them.
        If the critique says logic is flawed, call 'think_tool' to plan a fix.
        """)
        messages.append(intervention)

    # 4. We also inject a warning if the programmatic quality score was low in the last iteration.
    if state.get("needs_quality_repair"):
        messages.append(SystemMessage(content="PREVIOUS DRAFT QUALITY WAS LOW (Score < 7/10). Focus on finding new sources and citing them."))

    # 5. We invoke the tool-bound supervisor model to get its next plan.
    response = await supervisor_model_with_tools.ainvoke(messages)

    # 6. We return a Command to proceed to the 'supervisor_tools' node to execute the plan.
    return Command(
        goto="supervisor_tools",
        update={
            "supervisor_messages": [response],
            "research_iterations": state.get("research_iterations", 0) + 1,
            "needs_quality_repair": False # We reset the repair flag after warning the model.
        }
    )
```

The `supervisor` node is the strategic core of our diffusion loop. It’s a kind of **dynamic prompt engineering**.

1.  Before calling the LLM, it inspects the current `SupervisorState` and injects additional, high-priority system messages if critical feedback (`active_critiques`) or a low quality score (`needs_quality_repair`) is present.
2.  This forces the agent to pay immediate attention to its past failures and prioritize self-correction in its next plan, creating a robust, self-balancing system.

This is a pattern I call **State-Driven Prompt Injection** because we don’t just pass the state variables to the LLM, we dynamically alter the prompt based on them.

If `needs_quality_repair` is set to `True`, we temporarily inject a SystemMessage that clearly signals: **“PREVIOUS DRAFT QUALITY WAS LOW”**.

We don’t depend on the model implicit memory to improve on its own. Instead, we explicitly push this reminder into the context window for a single iteration. Once the Supervisor generates a new plan, **we reset the flag** to `False` in the returned `Command`, restoring the normal prompt flow for the next loop.

### Fan-Out Work and Denoise

The `supervisor` node decides what to do. The `supervisor_tools` node does it. This node is the "hands" of our Supervisor. It inspects the `AIMessage` from the `supervisor` node, extracts the planned tool calls, and orchestrates their execution.

![Fan-out Workflow (Created by Fareed Khan)](https://miro.medium.com/v2/resize:fit:2000/1*KCB0Iqw3YBpuz7I8eb9-Bw.png)

This node is our parallelism component. When it sees multiple `ConductResearch` tool calls, it will launch our `researcher_agent` sub-graph for each one concurrently, fanning out the work. It is also responsible for executing the core `refine_draft_report` denoising step.

First, a small helper to extract raw text from the tool messages, which will be a fallback for our refiner.

```python
def get_notes_from_tool_calls(messages: list[BaseMessage]) -> list[str]:
    """A helper function to extract the string content from ToolMessage objects in the supervisor's message history."""
    # This filters the message history for messages of type 'tool' and returns their content.
    return [tool_msg.content for tool_msg in filter_messages(messages, include_types="tool")]
```

This utility function, `get_notes_from_tool_calls`, provides a simple way to get a concatenated string of all the research findings from the supervisor recent conversational turns. This is a fallback for the `refine_draft_report` tool in the early stages of the loop before the structured `knowledge_base` has been populated.

Now, we build the main `supervisor_tools` node. This is the most complex node in our entire system, as it orchestrates sub-graph execution, tool calls, and our self-evolution evaluation.

```python
async def supervisor_tools(state: SupervisorState) -> Command[Literal["red_team", "context_pruner", "__end__"]]:
    """
    The 'Hands' of the Supervisor. This node executes the planned tool calls, including
    fanning out to parallel research sub-graphs and running the denoising step.
    """

    # 1. We get the most recent message, which contains the tool calls to be executed.
    most_recent_message = state.get("supervisor_messages", [])[-1]
    
    # 2. We check for exit conditions for the entire diffusion loop.
    exceeded_iterations = state.get("research_iterations", 0) >= max_researcher_iterations
    no_tool_calls = not most_recent_message.tool_calls
    research_complete = any(tc["name"] == "ResearchComplete" for tc in most_recent_message.tool_calls)


    if exceeded_iterations or no_tool_calls or research_complete:

        # If exiting, we prepare the final, curated notes for the report writer.
        # We prioritize the structured Knowledge Base, but fall back to raw notes if it's empty.
        kb_notes = [f"{f.content} (Confidence: {f.confidence_score})" for f in state.get("knowledge_base", [])]
        if not kb_notes: kb_notes = get_notes_from_tool_calls(state.get("supervisor_messages", []))

        # We return a Command to END this sub-graph and pass the final notes up to the main graph.
        return Command(goto=END, update={"notes": kb_notes, "research_brief": state.get("research_brief", "")})

    # 3. We separate the different types of tool calls for specialized handling.
    conduct_research_calls = [t for t in most_recent_message.tool_calls if t["name"] == "ConductResearch"]
    refine_report_calls = [t for t in most_recent_message.tool_calls if t["name"] == "refine_draft_report"]
    think_calls = [t for t in most_recent_message.tool_calls if t["name"] == "think_tool"]
    
    tool_messages = []
    all_raw_notes = []
    draft_report = state.get("draft_report", "")
    updates = {}

    # 4. Handle 'think_tool' calls synchronously.
    for tool_call in think_calls:
        observation = think_tool.invoke(tool_call["args"])
        tool_messages.append(ToolMessage(content=observation, name="think_tool", tool_call_id=tool_call["id"]))

    # 5. Handle 'ConductResearch' calls by fanning out to our research sub-graph in parallel.
    if conduct_research_calls:

        # We create a list of coroutines, one for each research task.
        coros = [researcher_agent.ainvoke({"researcher_messages": [HumanMessage(content=tc["args"]["research_topic"])], "research_topic": tc["args"]["research_topic"]}) for tc in conduct_research_calls]

        # 'asyncio.gather' runs all the research sub-graphs concurrently.
        results = await asyncio.gather(*coros)
        for result, tool_call in zip(results, conduct_research_calls):

            # We append the clean, compressed research as a ToolMessage for the Supervisor's context.
            tool_messages.append(ToolMessage(content=result.get("compressed_research", ""), name=tool_call["name"], tool_call_id=tool_call["id"]))

            # We also collect the raw, uncompressed notes to be processed by our context pruner.
            all_raw_notes.extend(result.get("raw_notes", []))

    # 6. Handle 'refine_draft_report' calls. This is the core denoising and self-evaluation step.
    for tool_call in refine_report_calls:
        kb = state.get("knowledge_base", [])
        kb_str = "CONFIRMED FACTS:\n" + "\n".join([f"- {f.content}" for f in kb]) if kb else "\n".join(get_notes_from_tool_calls(state.get("supervisor_messages", [])))
        new_draft = refine_draft_report.invoke({"research_brief": state.get("research_brief", ""), "findings": kb_str, "draft_report": state.get("draft_report", "")})
        
        # --- CRITICAL STEP: The Self-Evolution Evaluation ---
        eval_result = evaluate_draft_quality(research_brief=state.get("research_brief", ""), draft_report=new_draft)
        avg_score = (eval_result.comprehensiveness_score + eval_result.accuracy_score) / 2
        
        # We include the quality score directly in the tool message, so the Supervisor sees it.
        tool_messages.append(ToolMessage(content=f"Draft Updated.\nQuality Score: {avg_score}/10.\nJudge Feedback: {eval_result.specific_critique}", name=tool_call["name"], tool_call_id=tool_call["id"]))
        draft_report = new_draft
        
        # We log the metric to our history and set the repair flag if the score is low.
        updates["quality_history"] = [QualityMetric(score=avg_score, feedback=eval_result.specific_critique, iteration=state.get("research_iterations", 0))]
        if avg_score < 7.0: updates["needs_quality_repair"] = True

    # 7. Prepare the final state updates for this iteration.
    updates["supervisor_messages"] = tool_messages
    updates["raw_notes"] = all_raw_notes
    updates["draft_report"] = draft_report
    
    # 8. FAN OUT to the self-correction nodes (Red Team and Context Pruner) in parallel.
    return Command(goto=["red_team", "context_pruner"], update=updates)
```

1.  The `asyncio.gather(*coros)` call is the key to our parallel research, it invokes multiple instances of our `researcher_agent` sub-graph and waits for them all to complete.
2.  The most advanced part is the handling of the `refine_draft_report` call. Immediately after a new draft is generated, it is passed to our `evaluate_draft_quality` function.
3.  This creates an incredibly tight feedback loop: the system refines, immediately self-evaluates, and then uses the `QualityMetric` to inform the very next reasoning step of the `supervisor` node.
4.  The final `Command(goto=["red_team", "context_pruner"])` is another powerful parallel fan-out, sending the state to our self-correction agents simultaneously.

### Applying Guidance with Denoising Step

Finally, let’s look at the implementation of the core `refine_draft_report` tool itself. This is the actual **denoising mechanism that applies the guidance (new facts)** to the noisy image (the current draft).

![Guidance with Denoising Step (Created by Fareed Khan)](https://miro.medium.com/v2/resize:fit:1400/1*XyDjTOQByiogiwkd2eB6iw.png)

First, we define the prompt that guides this synthesis process.

```python
# The prompt for the refine_draft_report tool, which instructs the LLM on how to integrate new facts into an existing draft.
report_generation_with_draft_insight_prompt = """Based on all the research conducted and draft report, create a comprehensive, well-structured answer to the overall research brief:
<Research Brief>
{research_brief}
</Research Brief>

CRITICAL: Make sure the answer is written in the same language as the human messages!
For example, if the user's messages are in English, then MAKE SURE you write your response in English. If the user's messages are in Chinese, then MAKE SURE you write your entire response in Chinese.
This is critical. The user will only understand the answer if it is written in the same language as their input message.

Today's date is {date}.

Here is the draft report:
<Draft Report>
{draft_report}
</Draft Report>

Here are the findings from the research that you conducted:
<Findings>
{findings}
</Findings>

Please create a detailed answer to the overall research brief that:
1. Is well-organized with proper headings (# for title, ## for sections, ### for subsections)
2. Includes specific facts and insights from the research
3. References relevant sources using [Title](URL) format
4. Provides a balanced, thorough analysis. Be as comprehensive as possible, and include all information that is relevant to the overall research question. People are using you for deep research and will expect detailed, comprehensive answers.
5. Includes a "Sources" section at the end with all referenced links

You can structure your report in a number of different ways. Here are some examples:

To answer a question that asks you to compare two things, you might structure your report like this:
1/ intro
2/ overview of topic A
3/ overview of topic B
4/ comparison between A and B
5/ conclusion

To answer a question that asks you to return a list of things, you might only need a single section which is the entire list.
1/ list of things or table of things
Or, you could choose to make each item in the list a separate section in the report. When asked for lists, you don't need an introduction or conclusion.
1/ item 1
2/ item 2
3/ item 3

To answer a question that asks you to summarize a topic, give a report, or give an overview, you might structure your report like this:
1/ overview of topic
2/ concept 1
3/ concept 2
4/ concept 3
5/ conclusion

If you think you can answer the question with a single section, you can do that too!
1/ answer

REMEMBER: Section is a VERY fluid and loose concept. You can structure your report however you think is best, including in ways that are not listed above!
Make sure that your sections are cohesive, and make sense for the reader.

For each section of the report, do the following:
- Use simple, clear language
- Keep important details from the research findings
- Use ## for section title (Markdown format) for each section of the report
- Do NOT ever refer to yourself as the writer of the report. This should be a professional report without any self-referential language. 
- Do not say what you are doing in the report. Just write the report without any commentary from yourself.
- Each section should be as long as necessary to deeply answer the question with the information you have gathered. It is expected that sections will be fairly long and verbose. You are writing a deep research report, and users will expect a thorough answer.
- Use bullet points to list out information when appropriate, but by default, write in paragraph form.

REMEMBER:
The brief and research may be in English, but you need to translate this information to the right language when writing the final answer.
Make sure the final answer report is in the SAME language as the human messages in the message history.

Format the report in clear markdown with proper structure and include source references where appropriate.

<Citation Rules>
- Assign each unique URL a single citation number in your text
- End with ### Sources that lists each source with corresponding numbers
- IMPORTANT: Number sources sequentially without gaps (1,2,3,4...) in the final list regardless of which sources you choose
- Each source should be a separate line item in a list, so that in markdown it is rendered as a list.
- Example format:
  [1] Source Title: URL
  [2] Source Title: URL
- Citations are extremely important. Make sure to include these, and pay a lot of attention to getting these right. Users will often use these citations to look into more information.
</Citation Rules>
"""
```

This prompt is highly specific. It provides the LLM with three pieces of information: the overall goal (`research_brief`), the current state (`draft_report`), and the new information to incorporate (`findings`).

By instructing it to create a **"new and improved"** version, we are guiding it to perform the synthesis task that is the core of our denoising step.

Now, we can implement the decorated tool function.

```python
from langchain_core.tools import InjectedToolArg

@tool(parse_docstring=True)
def refine_draft_report(
    research_brief: Annotated[str, InjectedToolArg], 
    findings: Annotated[str, InjectedToolArg], 
    draft_report: Annotated[str, InjectedToolArg]
):
    """Refine draft report

    Synthesizes all research findings into a comprehensive draft report

    Args:
        research_brief: user's research request
        findings: collected research 