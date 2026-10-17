# Build your own AI agent from scratch for free in 5 minutes

AI agents are among the most exciting areas of modern AI development. They are more powerful than simple chatbots because agents can use tools, run code, search the web, plan steps, and even work together with other agents to complete complex tasks.

In this article, I will show you how to build your first AI agent from scratch using Google’s ADK (Agent Development Kit). This is an open-source framework that makes it easier to create agents, test them, add tools, and even build multi-agent systems.

The best part? You can build everything for free and in just a few minutes if you already have Python installed.

Let’s get started.



## What Is an AI Agent? (Simple Explanation)

Before we begin, let’s quickly review what an AI agent actually is.

A normal AI model (like ChatGPT or Gemini) only gives you text answers.  
An **AI agent** is different — it can:

- **Perform tasks**, not just answer questions
- **Use tools**, such as Google Search, calculators, APIs, or databases
- **Make decisions** and plan steps
- **Work autonomously with minimal human help**

You can think of an AI agent as a small “AI worker” that can do tasks instead of you.

In this tutorial, we will build a simple agent first, then upgrade it into a multi-agent system with separate agents for research, summarizing, and coordination.

## What You Need Before Starting

To follow this tutorial, you only need:

- **Python** installed on your computer
- **Any code editor**, such as VS Code (or [Google Antigravity IDE](https://proflead.dev/posts/google-antigravity-ide/) if you want)
- [**Google ADK**](https://proflead.dev/posts/ai-agent-explained-google-adk/) — the open-source framework we will install
- A **Gemini API key**, which is free to generate

If you have everything ready, let’s build!

## Build AI Agents From Scratch

### Step 1: Create a Project Folder and Virtual Environment

First, open your terminal and create a folder:

```bash
mkdir my_first_agent  
cd my_first_agent
```

Now create a virtual environment:
```bash
python -m venv .venv
```
Activate it:
```bash
source .venv/bin/activate  # macOS / Linux  
# or  
.\venv\Scripts\activate    # Windows
```

A virtual environment keeps your project clean and avoids version conflicts.

### Step 2: Install Google ADK

Now install the Agent Development Kit:

```bash
pip install google-adk
```
### Step 3: Create Your Agent Project

Inside your terminal, run:
```bash
adk create my_agent
```
Choose the model (you can pick Gemini 2.5 or Gemini Flash).



![Create Your Agent Project](https://miro.medium.com/v2/resize:fit:700/1*M3aqnbc2GPsW-0U9q19gyg.png)



After that, a folder structure appears:
```bash
my_agent/  
 ├── agent.py  
 ├── .env  
 └── __init__.py
```
- **agent.py** → This is the main file where your code lives
- **.env** → This is where your API key goes

Open the folder in VS Code or any IDE.

### Step 4: Get Your Free Gemini API Key

Go to: [https://aistudio.google.com](https://aistudio.google.com/)

Sign in with your Google account → bottom-left sidebar → **Get API key**.

Click **Create API Key**, give it a name, select a project (or create one), and copy the key.


![Get Your Free Gemini API Key](https://miro.medium.com/v2/resize:fit:700/1*Las3NG99FOlkBO61L3c2Ww.png)



Now open your `.env` file and add:
```bash
GOOGLE_API_KEY="your-key-here"
```

### Step 5: Test the Default Agent

Open `agent.py`. You will see the default boilerplate code.



![Test the Default Agent](https://miro.medium.com/v2/resize:fit:700/1*RbWUkl4nA6iCRlHcPp9MFA.png)



Before running it, update the model name.

Go to AI Studio → Models → choose a model → copy its internal name  
(Example: `gemini-2.0-flash` or `gemini-3-pro-preview`)

Replace the placeholder model name in your code.

Now test your agent. Run this command inside the terminal:
```bash
adk run my_agent
```
Ask something simple. If everything works, you should get an answer.  
If you hit the free limit for a model, switch to a lighter, free-tier model.

### Step 6: Create Multiple Agents (Research + Summarizer + Coordinator)

Now let’s build a real **multi-agent system**.

**1. Research Agent.** This agent will search the web and save the result.

**2. Summarizer Agent.** This takes the research result and writes a summary.

**3. Coordinator Agent (Root Agent).** This agent decides who should work first and then builds the final answer.

Each agent needs:

- Its own name
- Its own instructions
- Optional tools (like Google Search)
- Clear expected behavior

You can use this code inside your agent.py file:
```python
from google.adk.agents.llm_agent import Agent  
from google.adk.tools import google_search, AgentTool  
  
  
research_agent = Agent(  
    name="Researcher",  
    model="gemini-2.5-flash-lite",  
    instruction="""You are a specialized research agent. Your only job is to use the  
    google_search tool to find top 5 AI news for a give topic. Do not answer any user questions directly.""",  
    tools=[google_search],  
    output_key="research_result",  
)  
  
print("Resereach Agent created successfully.")  
  
summarizert = Agent(  
    name="Summarizert",  
    model="gemini-2.5-flash-lite",  
    instruction="""  
    Read the research findings {research_result} and create a summary for each topic with the link to read more  
    """,  
    output_key="summary_result",  
)  
print("Summarizert Agent created successfully.")  
  
  
# Root Coordinator:  
root_agent = Agent(  
    model='gemini-2.5-flash-lite',  
    name='root_agent',  
    description='A helpful assistant for user questions.',  
    instruction="""  
    You are coordinator. First your job is to delegate user questions to the 'research_agent' to gather information. Second pass the findings to the 'summarizert' agent to create a summary. Finally, compile the summaries into a final response for the user.  
    """,  
    tools=[  
        AgentTool(research_agent),  
        AgentTool(summarizert),  
    ]  
)
```
This is now a real multi-agent pipeline.

### Step 7: Run the Multi-Agent System

Run this command inside your terminal:
```bash
adk run my_agent
```
Then type the topic for research. After running the agents, you will see:

- Research agent gathering info
- Summarizer agent producing a summary
- Coordinator combining output

Everything works together!

### Step 8: Use the Web Interface (Much Easier)

ADK includes a web UI.

Inside the terminal, run this command:
```bash
adk web --port 8000
```
If everything is ok, you will see the server URL:



![ADK includes a web UI](https://miro.medium.com/v2/resize:fit:700/1*6Vq6aEYO4Mg11aEPXfvK2w.png)

Open the link in your browser. Select your agent from the menu.



![Use the Web Interface (Much Easier)](https://miro.medium.com/v2/resize:fit:700/1*vCqHIW0N2hVnlcEAgpF2Rg.png)



Now you can see:

- The message flow
- Which agent was called
- The steps they executed

This helps a lot when debugging multi-agent systems.

## Video Tutorial: How to Build AI Agents

If you want visual instruction, please watch my step-by-step video tutorial.


_Watch on YouTube:_ [_How to Build an AI Agent from Scratch_](https://youtu.be/lh8LBRXHnGE?si=-Z9yc236U29ZY7tP)

## Conclusion

Building AI agents is easier than most people think. With Google ADK, you can create simple or even multi-agent systems in minutes, test them in a web interface, and expand them with tools, workflows, and real-world integrations. Give it a shot, and please share your experience with me in the comments below.

Cheers! ;)