# Context Engineering for Writers

A comprehensive framework for context engineering to help AI incrementally create high-quality, concise essays with the depth and clarity. 


## 🚀 Quick Start

```bash
# 1. Clone or copy this framework
cd context-engineering-for-writers

# 2. Set up your writing rules (optional - template provided)
# Edit CLAUDE.md to add your writing-specific guidelines

# 3. Add writing examples (highly recommended)
# Place exemplary essays and writing samples in the examples/ folder

# 4. Create your initial essay request
# Edit INITIAL.md with your essay topic and requirements

# 5. Generate a comprehensive WRP (Writing Requirements Prompt)
# In Claude Code, run:
/generate-wrp INITIAL.md

# 6. Execute the WRP to write your essay
# In Claude Code, run:
/execute-wrp WRPs/your-essay-name.md
```

## 📚 Table of Contents

- [What is Context Engineering for Writers?](#what-is-context-engineering-for-writers)
- [Framework Structure](#framework-structure)
- [Step-by-Step Guide](#step-by-step-guide)
- [Writing Effective INITIAL.md Files](#writing-effective-initialmd-files)
- [The WRP Workflow](#the-wrp-workflow)
- [Using Examples Effectively](#using-examples-effectively)
- [Best Practices for Essay Writing](#best-practices-for-essay-writing)

## What is Context Engineering for Writers?

Context Engineering for Writers represents a paradigm shift from traditional writing prompts to comprehensive writing context systems:

### Traditional Writing Prompts vs Context Engineering

**Traditional Writing Prompts:**
- Focuses on topic suggestions and basic instructions
- Limited to surface-level guidance
- Like giving someone a writing topic on a sticky note

**Context Engineering for Writers:**
- A complete system for providing comprehensive writing context
- Includes style guides, examples, research patterns, and validation criteria
- Like providing a master class with exemplars, techniques, and feedback loops

### Why Context Engineering for Writers Matters

1. **Reduces Writing Failures**: Most AI writing failures aren't model failures - they're context failures
2. **Ensures Consistency**: AI follows your writing style, voice, and structural patterns
3. **Enables Complex Essays**: AI can handle multi-layered arguments with proper context
4. **Self-Improving**: Validation loops allow AI to refine and improve its writing

## Framework Structure

```
context-engineering-for-writers/
├── .claude/
│   ├── commands/
│   │   ├── generate-wrp.md    # Generates comprehensive WRPs
│   │   └── execute-wrp.md     # Executes WRPs to write essays
│   └── settings.local.json    # Claude Code permissions
├── WRPs/
│   ├── templates/
│   │   └── wrp_base.md       # Base template for WRPs
│   └── EXAMPLE_essay_wrp.md  # Example of a complete WRP
├── examples/                  # Your writing examples (critical!)
│   ├── paul_graham_style/    # Paul Graham essay examples
│   ├── argument_structures/  # Different argument patterns
│   └── transitions/          # Effective transition examples
├── CLAUDE.md                 # Global writing rules for AI assistant
├── INITIAL.md               # Template for essay requests
├── INITIAL_EXAMPLE.md       # Example essay request
└── README.md                # This file
```

## Step-by-Step Guide

### 1. Set Up Global Writing Rules (CLAUDE.md)

The `CLAUDE.md` file contains writing-wide rules that the AI assistant will follow in every conversation. The template includes:

- **Writing philosophy**: Clarity, conciseness, and depth principles
- **Essay structure**: Introduction patterns, argument flow, conclusion techniques
- **Style conventions**: Voice, tone, sentence structure preferences
- **Research standards**: Source integration, fact-checking, citation practices
- **Revision process**: Self-editing criteria, feedback incorporation

**You can use the provided template as-is or customize it for your writing style.**

### 2. Create Your Initial Essay Request

Edit `INITIAL.md` to describe what you want to write:

```markdown
## ESSAY TOPIC:
[Describe your essay topic - be specific about the angle, argument, or exploration you want to pursue]

## EXAMPLES:
[List any example files in the examples/ folder and explain what aspects should be emulated]

## RESEARCH:
[Include links to relevant sources, studies, or background reading]

## STYLE & TONE:
[Specify the desired voice, audience, and stylistic approach]

## OTHER CONSIDERATIONS:
[Mention any specific requirements, constraints, or elements to include/avoid]
```

**See `INITIAL_EXAMPLE.md` for a complete example.**

### 3. Generate the WRP

WRPs (Writing Requirements Prompts) are comprehensive writing blueprints that include:

- Complete context and research
- Structural framework with validation
- Style and voice guidelines
- Revision and refinement criteria

They are similar to PRDs but crafted specifically to instruct an AI writing assistant.

Run in Claude Code:
```bash
/generate-wrp INITIAL.md
```

This command will:
1. Read your essay request
2. Research the topic and gather context
3. Analyze writing patterns from examples
4. Create a comprehensive WRP in `WRPs/your-essay-name.md`

### 4. Execute the WRP

Once generated, execute the WRP to write your essay:

```bash
/execute-wrp WRPs/your-essay-name.md
```

The AI writing assistant will:
1. Read all context from the WRP
2. Create a detailed writing plan
3. Draft each section with validation
4. Revise and refine based on criteria
5. Ensure all quality standards are met

## Writing Effective INITIAL.md Files

### Key Sections Explained

**ESSAY TOPIC**: Be specific and focused
- ❌ "Write about technology"
- ✅ "Explore how the maker mindset in programming parallels the creative process in painting, using personal anecdotes and concrete examples to argue that both are fundamentally about iterative creation rather than predetermined execution"

**EXAMPLES**: Leverage the examples/ folder
- Place exemplary essays and writing samples in `examples/`
- Reference specific techniques, structures, or styles to emulate
- Explain what aspects should be incorporated

**RESEARCH**: Include all relevant context
- Primary source URLs
- Background reading
- Statistical data or studies
- Expert opinions or quotes

**STYLE & TONE**: Define your voice
- Target audience (general public, experts, peers)
- Tone (conversational, academic, persuasive)
- Voice characteristics (personal, authoritative, exploratory)
- Structural preferences (narrative, analytical, argumentative)

## The WRP Workflow

### How /generate-wrp Works

The command follows this process:

1. **Research Phase**
   - Analyzes your writing samples for patterns
   - Searches for similar essay structures
   - Identifies stylistic conventions to follow

2. **Context Gathering**
   - Fetches relevant research and sources
   - Includes background information
   - Adds domain-specific knowledge

3. **Blueprint Creation**
   - Creates step-by-step writing plan
   - Includes validation checkpoints
   - Adds revision criteria

4. **Quality Check**
   - Scores confidence level (1-10)
   - Ensures all context is included

### How /execute-wrp Works

1. **Load Context**: Reads the entire WRP
2. **Plan**: Creates detailed writing outline
3. **Draft**: Writes each section iteratively
4. **Validate**: Checks against quality criteria
5. **Revise**: Refines based on feedback
6. **Finalize**: Ensures all requirements met

## Using Examples Effectively

The `examples/` folder is **critical** for success. AI writing assistants perform much better when they can see patterns to follow.

### What to Include in Examples

1. **Structural Patterns**
   - How you organize arguments
   - Introduction and conclusion styles
   - Paragraph flow and transitions

2. **Voice and Style**
   - Sentence structure preferences
   - Vocabulary choices
   - Tone consistency

3. **Research Integration**
   - How you incorporate sources
   - Citation and reference styles
   - Fact-to-opinion ratios

4. **Narrative Techniques**
   - Personal anecdote usage
   - Metaphor and analogy patterns
   - Storytelling approaches

### Example Categories

- **`paul_graham_style/`**: Essays demonstrating clear, conversational yet profound writing
- **`argument_structures/`**: Different ways to build and present arguments
- **`transitions/`**: Effective ways to connect ideas and sections
- **`openings_closings/`**: Compelling introduction and conclusion examples

## Best Practices for Essay Writing

### 1. Start with Strong Examples
- Include 3-5 exemplary essays in your examples folder
- Choose pieces that represent your target quality and style
- Annotate what makes each example effective

### 2. Define Your Voice Clearly
- Specify your preferred tone and style in CLAUDE.md
- Include examples of voice consistency
- Note what to avoid (overly academic, too casual, etc.)

### 3. Structure for Clarity
- Use clear argument progression
- Include smooth transitions between ideas
- End sections with forward momentum

### 4. Research Thoroughly
- Include primary sources in your WRP
- Verify facts and statistics
- Balance research with original insight

### 5. Iterate and Refine
- Use the validation criteria in your WRP
- Don't settle for first drafts
- Apply consistent revision standards

## Quality Indicators

Your essays should demonstrate:

- **Clarity**: Ideas are immediately understandable
- **Depth**: Insights go beyond surface observations
- **Flow**: Smooth progression from idea to idea
- **Voice**: Consistent, engaging personality
- **Precision**: Every word serves a purpose
- **Impact**: Memorable conclusions and takeaways

## Setup Instructions

### Prerequisites
- Ruby 3.2.0 or higher
- [Claude CLI](https://docs.anthropic.com/en/docs/claude-code/overview) installed and configured
- Bundler gem installed

### Installation

1. **Navigate to this project directory**:
   ```bash
   cd context-engineering-for-writers
   ```

2. **Install dependencies**:
   ```bash
   bundle install
   ```
   
   This will install the Claude Swarm gem and all dependencies needed for the enhanced writing workflow.

3. **Setup the framework**:
   - Copy this framework to your writing workspace
   - Add 2-3 exemplary essays to the examples folder
   - Customize CLAUDE.md with your writing preferences
   - Create your initial essay request in INITIAL.md

## Usage

### Starting the Writing Team (Enhanced Workflow)

1. **Launch the Writing Research & Essay Generation Swarm**:
   ```bash
   bin/launch
   ```
   
   This will start the Writing Orchestrator with connections to all specialist agents:
   - Research Specialist
   - Context Engineer  
   - Style Analyst
   - Essay Writer
   - Quality Reviewer

2. **Resume a previous writing session**:
   ```bash
   bin/launch --session-id [SESSION_ID]
   ```

3. **Launch with enhanced permissions**:
   ```bash
   bin/launch --vibe
   ```
   
4. **View active writing sessions**:
   ```bash
   bin/launch ps
   ```

### Traditional Workflow (Individual Commands)

You can still use the traditional approach with individual Claude Code commands:

1. **Generate a comprehensive WRP**:
   ```bash
   /generate-wrp INITIAL.md
   ```

2. **Execute the WRP to write your essay**:
   ```bash
   /execute-wrp WRPs/your-essay-name.md
   ```

### Working with the Writing Team

The enhanced swarm workflow provides specialized agents for each phase:

1. **Research Phase**: Research Specialist gathers comprehensive sources and context
2. **Planning Phase**: Context Engineer creates detailed Writing Requirements Prompts
3. **Style Analysis**: Style Analyst ensures voice consistency with examples
4. **Writing Phase**: Essay Writer executes WRPs systematically
5. **Quality Review**: Quality Reviewer validates against all criteria

### Session Management

- All session data is stored in `~/.claude-swarm/sessions/`
- Sessions can be resumed using the session ID
- View active sessions to monitor writing progress
- Each writing project maintains its own session context

## Getting Started

The framework is designed to improve with use. Each essay you write adds to your context, making future essays even better.

## Troubleshooting

### Swarm Configuration Issues
If you encounter "Circular dependency detected" errors:
1. Check `claude-swarm.yml` for bidirectional connections between agents
2. Ensure the writing_orchestrator coordinates between agents rather than agents connecting directly to each other
3. The current configuration uses a hierarchical structure: orchestrator → specialists → no circular references

### Common Issues
- **Command not found**: Ensure Claude CLI is installed and configured
- **Permission errors**: Check `.claude/settings.local.json` for proper command permissions
- **Missing dependencies**: Run `bundle install` to install required gems

---

*"The way to create something beautiful is often to make subtle tweaks to something that already exists, or to combine existing ideas in a slightly new way."* - Paul Graham

This framework helps you engineer the context needed for AI to make those subtle tweaks and combinations that result in truly excellent writing.

## Credits

The inspiration for this project came from https://github.com/coleam00/context-engineering-intro
