#  Automated AI-Powered RSS Digest (n8n Workflow)

This project is an **automated RSS aggregation and AI-generated cyber threat intel newsletter system** built using **n8n**. It collects articles from multiple RSS feeds, sorts and filters them by date, summarizes the key stories using an AI model, and emails you a clean daily report — all on a scheduled timer. The purpose of this project is to incorporate the most up-to-date cyber threat intelligence into everyday operations.

---

##  Features

![Workflow Diagram](images/n8n_workflow.jpg)

###  **1. Multi-Feed RSS Aggregation**
- Pulls from multiple RSS feeds.
- Normalizes and combines all items into a single list.
- Deduplicates automatically (optional depending on your feeds).

###  **2. Time-Based Filtering (Last 3 Days)**
- Only keeps articles published within the last 72 hours.
- If *no* recent items exist, the workflow still outputs one safe fallback item so the flow never breaks.

###  **3. AI Summarization + Priority Extraction**
- Feeds the combined article list into an AI model.
- The model:
  - Summarizes the overall news landscape.
  - Highlights the most important stories.
  - Removes noise and low-value content.
  - Produces a clean, readable report.

###  **4. Automatic Email Report**
- Formats the AI-generated summary into an email.
- Sends the report to your inbox.
- Runs without manual action thanks to a scheduled trigger.

---

##  How It Works (Workflow Overview)

1. **Scheduled Trigger** – triggers the workflow on your schedule.  
2. **HTTP Request Nodes** – fetch RSS feeds from multiple sources.  
3. **RSS → JSON Parsing** – converts XML into structured items.  
4. **Function Node (Combine + Sort + Filter)**  
   - Merges all feeds  
   - Filters last 3 days  
   - Sorts by date  
   - Ensures fallback if no items  
5. **AI Model Node** – summarizes and extracts key stories.  
6. **Email Node** – sends the finished digest.


##  Key Components in n8n

| Component | Purpose |
|----------|---------|
| **Cron** | Schedules workflow |
| **HTTP Request** | Fetch RSS feeds |
| **Function Node** | Combine + filter + sort |
| **AI Node** | Summarization & prioritization |
| **Email Node** | Sends final digest |


## 📦 How to Import the Workflow

1. Open **n8n**
2. Navigate to **Workflows → Import**
3. Upload your JSON export
4. Reassign:
   - AI model credentials  
   - Email (Gmail) credentials
5. Update the Cron schedule to your preference
6. Save + Activate the workflow

---

## Ouput

![Workflow Diagram](images/Generated_report.jpg)

