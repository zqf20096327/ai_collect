<h1 align="center">🚀 Auto-Apply AI</h1>

<p align="center">
  <b>Real-Time Job Discovery (LinkedIn, Indeed, Google, Greenhouse), Resume &amp; Project Matching, Playwright Web-Form Auto-Apply, Gmail HR Outreach, and Application Notifications.</b>
</p>

---

## 🏗️ System Architecture

1. **Resume & Job Details Intake**: Upload your resume (`.pdf`, `.docx`, `.txt`) and describe what type of job/work you do along with target roles and preferences.
2. **Resume & Project Extraction**: Extracts skills, experience, education, **projects**, summary, and contact links, plus real-time ATS audit scores.
3. **4-Source Job Discovery**: Connects to **LinkedIn**, **Indeed**, **Google**, and **Greenhouse** using queries derived from your resume details, projects, and job focus.
4. **Resume-Ranked Portal**: Displays matched jobs on the portal ranked by your resume & project relevance score, clearly tagged as **HR Email** vs **Playwright Web**.
5. **Apply Flow (`0 -> 15` Daily Max)**: Click **Apply** and choose how many jobs to apply to (`0` to `15` daily max):
   - **Send Email** via connected Gmail if an authentic HR email is found.
   - **Use Playwright** if the application is web-based (with proof screenshots).
6. **Notifications & Applied Jobs Verification**: Every application persists a real-time notification in the portal so you can inspect status, proof screenshots, Gmail IDs, and cover letters in **Applied Jobs**.

---

## ⚡ Quick Start

```bash
python start.py
```

- **Frontend**: `http://localhost:3000`
- **Backend API**: `http://localhost:8000`
- **Swagger Docs**: `http://localhost:8000/docs`

### Docker Compose

```bash
cp .env.example .env
docker-compose up -d --build
```
