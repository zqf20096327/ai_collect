# Duka Stock Advisor

Duka Stock Advisor is an AI-powered stock management assistant designed to help small shop and duka owners monitor inventory, understand stock levels, and make better restocking decisions.

The application uses the Google Gemini API and maintains conversation history throughout a session so that the AI can use information provided in earlier messages when responding to later questions.

## Features

- AI-powered stock management advice
- Multi-turn conversation memory
- Structured JSON responses from the AI
- JSON response validation
- Automatic retry when the AI returns invalid JSON
- Main application menu
- Start new sessions
- Save completed sessions
- Open and review previous sessions
- Automatic session summaries
- Handling of empty user input
- Handling of AI/API failures
- Handling of missing or malformed session files
- Secure API-key management using environment variables

## How It Works

The application follows a simple conversation pipeline:

1. The user starts a new session.
2. The user provides information about their shop or stock.
3. The application stores the conversation history.
4. The conversation history is sent to the AI with each new request.
5. The AI returns a JSON response.
6. The application validates the JSON response.
7. If the response is invalid, the application retries the AI request once.
8. When the user ends the session, the application generates a session summary.
9. The complete conversation and summary are saved as a JSON session file.
10. Saved sessions can later be opened from the main menu.

## AI Response Format

Every normal AI response is required to follow this structure:

```json
{
    "message": "string",
    "priority": "low, medium, or high",
    "recommendations": [
        "string"
    ]
}
```

The application validates the response before displaying it.

The following are checked:

- The response must contain valid JSON.
- The response must be a JSON object.
- Required fields must be present.
- Required fields must contain non-empty values.
- `priority` must be `low`, `medium`, or `high`.
- `recommendations` must be a list.

If the first response fails validation, the application automatically retries the request once. If the retry also fails, the application displays an error and continues safely.

## Session Summaries

When a session ends, the application generates a separate summary containing:

```json
{
    "summary": "string",
    "key_stock_issues": [
        "string"
    ],
    "recommended_actions": [
        "string"
    ]
}
```

The summary is stored together with the conversation in the session JSON file.

Empty sessions are handled separately and receive a default summary indicating that no conversation took place.

## Project Structure

```text
wca-ai-tool-s12-mi6/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── samples/
│
└── sessions/
```

### Main Files

**`main.py`**

Contains the main application logic, AI interaction, conversation memory, JSON validation, session management, error handling, and menu system.

**`requirements.txt`**

Contains the external Python packages required by the application.

**`.gitignore`**

Prevents sensitive and unnecessary files from being committed, including the API environment file and saved session files.

**`samples/`**

Contains sample project/session data intended for demonstration.

**`sessions/`**

Stores completed user sessions locally. Session files are excluded from Git tracking.

## Requirements

- Python 3
- Google Gemini API key
- Internet connection

Python dependencies:

```text
google-genai
python-dotenv
```

## API Key Setup

The API key is not hardcoded into the application.

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

The `.env` file is excluded from Git using `.gitignore`.

Do not commit or share your API key.

## Installation

Clone the repository and enter the project directory:

```bash
git clone https://github.com/avonxate-hub/wca-ai-tool-s12-MI6.git
cd wca-ai-tool-s12-mi6
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create the `.env` file and add the Gemini API key.

## Running the Application

Start the application with:

```bash
python main.py
```
## Quick User Guide

### 1. Start a Session

From the main menu, select:

1. Start New Session

The application will then allow the shop owner to enter information about stock, sales, and other inventory-related questions.

### 2. Continue the Conversation

The shop owner can provide information across multiple messages.

For example:

- Report the current stock.
- Report a sale.
- Ask how much stock remains.
- Ask whether restocking is necessary.

The application keeps the conversation history so that later questions can use information from earlier messages.

### 3. End the Session

Enter:

```text
exit

The main menu provides three options:

```text
================================
       DUKA STOCK ADVISOR
================================
1. Start New Session
2. Open Past Session
3. Exit
```

## Example Conversation

```text
You: I have 10 bags of unga.

AI:
{
    "message": "You currently have 10 bags of unga in stock...",
    "priority": "medium",
    "recommendations": [
        "Monitor your daily unga sales rate.",
        "Check your supplier's delivery schedule.",
        "Set a minimum stock level for unga."
    ]
}

You: I sold 4 bags today. How many do I have left?

AI:
{
    "message": "You have 6 bags of unga remaining...",
    "priority": "medium",
    "recommendations": [
        "Monitor your sales rate.",
        "Consider restocking if demand remains high."
    ]
}
```

The second response can use information from the earlier turn because the application maintains the conversation history.

## Error Handling

The application handles expected failures without exposing Python tracebacks to the user during normal operation.

Examples include:

- Empty user input
- Invalid menu selections
- AI/API connection failures
- Invalid AI JSON
- Missing session files
- Malformed session JSON
- Older session files without summaries

When an older session does not contain a summary, the conversation can still be opened and the application displays:

```text
No summary available for this session.
```

## Security

The Gemini API key is stored outside the source code using an environment variable loaded from `.env`.

The `.env` file is included in `.gitignore` and must never be committed to the repository.

Saved user sessions are also excluded from Git tracking.

## Project

**WECAN Academy — Season 12**

**Group:** MI6

**Project:** AI-Powered Smart Assistant with Memory

**Application:** Duka Stock Advisor



## Members / Collaborators

- Karim Onesmus
- Elton JW
- Denis Ouko