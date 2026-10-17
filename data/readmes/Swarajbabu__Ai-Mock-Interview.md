# 🤖 AI Mock Interview — Intelligent Interview Simulation Platform

> An end-to-end AI-powered mock interview platform that ingests CVs and job descriptions to auto-generate role-specific questions, conducts real-time voice & video interviews via an AI avatar, and delivers automated multi-dimensional feedback — eliminating manual review entirely.

![React](https://img.shields.io/badge/React.js-Frontend-61DAFB?style=for-the-badge&logo=react&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-Backend-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-Scoring%20Engine-8A2BE2?style=for-the-badge)
![n8n](https://img.shields.io/badge/n8n-Automation-EF5C3E?style=for-the-badge)
![Speech](https://img.shields.io/badge/Speech%20Recognition-TTS-FF6B35?style=for-the-badge)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Architecture Diagram](#-architecture-diagram)
- [Database Schema](#-database-schema)
- [Application Routes](#-application-routes)
- [API Reference](#-api-reference)
- [n8n Workflow Automation](#-n8n-workflow-automation)
- [Environment Variables](#-environment-variables)
- [Getting Started](#-getting-started)
- [Scripts](#-scripts)
- [Deployment](#-deployment)

---

## 🌟 Overview

**AI Mock Interview** is a full-stack, AI-driven platform that simulates realistic job interviews end-to-end. Candidates upload their CV and a target job description; the platform uses LLM pipelines to generate a tailored question bank, then conducts the interview in real time through a voice-and-video AI avatar. Upon completion, an NLP-based scoring engine evaluates responses across five dimensions and delivers instant, detailed feedback — all automated via n8n workflows.

> ⚡ **Sub-2s AI avatar response latency** | 📊 **5-dimension NLP scoring** | 🔄 **~80% reduction in operational overhead via automation**

---

## ✨ Features

### 🎯 Core Interview Flow
| Feature | Description |
|---|---|
| 📄 **CV & JD Ingestion** | Upload CV and job description via REST API; parsed and stored in cloud storage |
| 🧠 **LLM Question Generation** | Auto-generates a role-specific, personalised question bank using LLM pipelines |
| 🎙️ **Real-Time Voice Interaction** | Speech Recognition captures candidate responses live during the interview |
| 🤖 **AI Avatar Responses** | TTS API delivers AI interviewer responses with sub-2s latency |
| 📹 **Video Interview Room** | Full browser-based interview session with audio/video support |
| 📊 **Automated Scoring** | NLP engine scores responses across 5 dimensions instantly on completion |
| 📬 **Feedback Delivery** | Detailed feedback report auto-delivered to the candidate post-interview |

### 🔐 Authentication
- Email/password registration and login (JWT-based)
- Role-based access: `candidate` and `admin`

### 🛡️ Admin Dashboard
- View all scheduled and completed interviews
- Access candidate scores, feedback reports, and session recordings
- Manage job roles and question banks

### ⚙️ Automation (n8n Workflows)
- **Automated scheduling** — triggers interview sessions on candidate sign-up
- **Feedback delivery** — sends personalised reports on interview completion
- **Result storage** — persists scoring data to the database automatically
- Reduces end-to-end pipeline overhead by **~80%** vs. a manual process

---

## 🛠️ Tech Stack

### Frontend
| Technology | Purpose |
|---|---|
| **React.js** | UI framework |
| **Vite** | Build tool & dev server |
| **React Router DOM** | Client-side routing |
| **Convex** | Real-time database & backend functions |
| **Speech Recognition API** | Captures live candidate voice input |
| **Axios** | HTTP client for REST API calls |
| **lucide-react** | Icon library |

### Backend
| Technology | Purpose |
|---|---|
| **Node.js** | Runtime environment |
| **Express.js** | HTTP web framework & REST API |
| **LLM Pipeline (via API)** | Role-specific interview question generation |
| **NLP APIs** | Automated multi-dimension response scoring |
| **TTS API** | AI avatar voice synthesis (sub-2s latency) |
| **Cloud Storage** | CV and JD file storage |
| **JWT / bcryptjs** | Authentication & password hashing |
| **dotenv** | Environment variable management |
| **cors** | Cross-Origin Resource Sharing middleware |

### Automation & Database
| Technology | Purpose |
|---|---|
| **n8n** | Workflow automation (scheduling, feedback, storage) |
| **Convex** | Primary real-time cloud database |

---

## 📁 Project Structure

```
Ai-Mock-Interview/
├── backend/                          # Node.js + Express REST API server
│   ├── middleware/                   # JWT auth middleware
│   ├── routes/                       # Express route handlers
│   │   ├── auth.js                   # Register / Login routes
│   │   ├── upload.js                 # CV & JD upload endpoints
│   │   ├── interview.js              # Interview session management
│   │   └── results.js                # Score & feedback retrieval
│   ├── services/                     # Core business logic
│   │   ├── llmService.js             # LLM pipeline for question generation
│   │   ├── scoringService.js         # NLP-based 5-dimension scoring engine
│   │   ├── ttsService.js             # TTS API integration (AI avatar voice)
│   │   └── storageService.js         # Cloud storage upload/download
│   ├── server.js                     # Main server entry point
│   ├── package.json
│   └── .env
│
└── frontend/                         # React + Vite + Convex frontend
    ├── convex/                       # Convex backend functions & schema
    │   ├── schema.js                 # Database schema definition
    │   ├── users.js                  # User queries and mutations
    │   ├── interviews.js             # Interview session queries and mutations
    │   ├── questions.js              # Question bank queries and mutations
    │   └── results.js                # Scoring result queries and mutations
    ├── src/
    │   ├── components/
    │   │   ├── Navbar.jsx            # Top navigation bar
    │   │   ├── AvatarPlayer.jsx      # AI avatar video/audio display
    │   │   ├── SpeechCapture.jsx     # Live speech recognition component
    │   │   └── ScoreCard.jsx         # Post-interview score breakdown
    │   ├── context/                  # React context (Auth, Interview state)
    │   ├── pages/
    │   │   ├── Home.jsx              # Landing page
    │   │   ├── Upload.jsx            # CV & JD upload page
    │   │   ├── InterviewRoom.jsx     # Live interview session
    │   │   ├── Results.jsx           # Score & feedback report
    │   │   ├── Profile.jsx           # User profile & interview history
    │   │   └── AdminDashboard.jsx    # Admin panel
    │   ├── App.jsx                   # Root component with routes
    │   ├── main.jsx                  # React + Convex provider entry point
    │   └── index.css                 # Global styles
    ├── index.html
    ├── vite.config.js
    └── package.json
```

---

## 🗄️ Database Schema

The Convex schema defines **4 collections**:

### `users`
| Field | Type | Description |
|---|---|---|
| `name` | `string` | Display name |
| `email` | `string` | Email address (indexed) |
| `password` | `string?` | Hashed password |
| `role` | `"candidate" \| "admin"` | Access level |
| `avatar` | `string?` | Profile avatar URL |

### `interviews`
| Field | Type | Description |
|---|---|---|
| `userId` | `Id<"users">` | Candidate reference |
| `cvUrl` | `string` | Cloud storage URL for uploaded CV |
| `jdUrl` | `string` | Cloud storage URL for uploaded JD |
| `jobTitle` | `string` | Target job role |
| `status` | `"Scheduled" \| "In Progress" \| "Completed"` | Session status |
| `scheduledAt` | `string` | ISO date-time string |

### `questions`
| Field | Type | Description |
|---|---|---|
| `interviewId` | `Id<"interviews">` | Parent interview reference |
| `questionText` | `string` | Generated question |
| `category` | `string` | Question category (technical, behavioural, etc.) |
| `order` | `number` | Question sequence number |

### `results`
| Field | Type | Description |
|---|---|---|
| `interviewId` | `Id<"interviews">` | Parent interview reference |
| `userId` | `string` | Candidate reference |
| `scores` | `ScoreDimension[]` | Array of `{ dimension, score, feedback }` |
| `overallScore` | `number` | Aggregate score (0–100) |
| `summary` | `string` | AI-generated overall feedback summary |
| `deliveredAt` | `string?` | Timestamp when feedback was sent |

### Score Dimensions (5)
| Dimension | Description |
|---|---|
| **Clarity** | How clearly the candidate communicated their answer |
| **Relevance** | How directly the answer addressed the question |
| **Depth** | Technical or contextual depth of the response |
| **Communication** | Overall language quality and articulation |
| **Confidence** | Tone, pacing, and projected confidence |

---

## 🛣️ Application Routes

### Frontend (React Router)
| Path | Component | Description |
|---|---|---|
| `/` | `Home` | Landing page |
| `/upload` | `Upload` | Upload CV and job description |
| `/interview/:id` | `InterviewRoom` | Live AI interview session |
| `/results/:id` | `Results` | Score breakdown and feedback report |
| `/profile` | `Profile` | Interview history and past results |
| `/admin` | `AdminDashboard` | Admin-only management panel |

### Backend (Express REST API)
| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/health` | Health check endpoint |
| `POST` | `/api/auth/register` | Register a new candidate |
| `POST` | `/api/auth/login` | Login and receive JWT |
| `POST` | `/api/upload/cv` | Upload CV to cloud storage |
| `POST` | `/api/upload/jd` | Upload job description to cloud storage |
| `POST` | `/api/interview/generate` | Trigger LLM question bank generation |
| `POST` | `/api/interview/score` | Submit responses for NLP scoring |
| `GET` | `/api/results/:interviewId` | Retrieve scored results and feedback |

---

## ⚙️ n8n Workflow Automation

Three automated n8n workflows power the operational backbone of the platform:

| Workflow | Trigger | Actions |
|---|---|---|
| **Interview Scheduler** | Candidate completes CV + JD upload | Schedules session, sends confirmation email |
| **Feedback Delivery** | Interview status → `Completed` | Formats feedback report, emails candidate |
| **Result Storage** | Scoring engine callback | Persists scores to Convex, notifies admin |

> These three workflows replace what would otherwise be a fully manual pipeline, reducing operational overhead by approximately **80%**.

---

## 🔑 Environment Variables

### Backend — `backend/.env`
```env
PORT=5000
JWT_SECRET=your_jwt_secret_key
GOOGLE_CLIENT_ID=your_google_client_id
LLM_API_KEY=your_llm_api_key
LLM_API_URL=https://api.your-llm-provider.com
NLP_API_KEY=your_nlp_api_key
TTS_API_KEY=your_tts_api_key
CLOUD_STORAGE_BUCKET=your_bucket_name
CLOUD_STORAGE_KEY=your_storage_key
N8N_WEBHOOK_URL=https://your-n8n-instance.com/webhook/interview
```

### Frontend — `frontend/.env.local`
```env
VITE_CONVEX_URL=https://your-project.convex.cloud
VITE_BACKEND_URL=http://localhost:5000
VITE_GOOGLE_CLIENT_ID=your_google_client_id
```

---

## 🚀 Getting Started

### Prerequisites
- **Node.js** v18+ and **npm** installed
- A **Convex** account → [convex.dev](https://convex.dev)
- API keys for your chosen LLM, NLP, and TTS providers
- An **n8n** instance (self-hosted or cloud) → [n8n.io](https://n8n.io)
- A cloud storage bucket (AWS S3, GCS, or equivalent)

### 1. Clone the Repository
```bash
git clone https://github.com/Swarajbabu/Ai-Mock-Interview.git
cd Ai-Mock-Interview
```

### 2. Setup the Backend
```bash
cd backend
npm install
# Create and fill in backend/.env (see Environment Variables above)
npm run dev
```
The backend server starts on **http://localhost:5000**.

### 3. Setup Convex
```bash
cd frontend
npm install
npx convex dev
```
This will prompt you to log in to Convex and link/create a project. It will populate `VITE_CONVEX_URL` in `.env.local` automatically.

### 4. Start the Frontend
```bash
# In a new terminal, inside the frontend directory
npm run dev
```
The frontend starts on **http://localhost:5173** (Vite default).

### 5. Configure n8n Workflows
1. Import the workflow JSON files from `/n8n-workflows/` into your n8n instance.
2. Set the `N8N_WEBHOOK_URL` in your backend `.env` to point to the Interview Scheduler webhook.
3. Activate all three workflows in n8n.

---

## 📜 Scripts

### Frontend (`frontend/`)
| Command | Description |
|---|---|
| `npm run dev` | Start Vite dev server |
| `npm run build` | Build for production |
| `npm run preview` | Preview the production build locally |
| `npx convex dev` | Start Convex dev server (sync functions & watch) |
| `npx convex deploy` | Deploy Convex functions to production |

### Backend (`backend/`)
| Command | Description |
|---|---|
| `npm run dev` | Start backend with nodemon (auto-restart) |
| `npm start` | Start backend with node (production) |

---

## ☁️ Deployment

| Layer | Platform | Notes |
|---|---|---|
| **Frontend** | [Vercel](https://vercel.com) | Set `VITE_CONVEX_URL` and `VITE_BACKEND_URL` in Vercel env vars |
| **Backend** | [Render](https://render.com) | Set all backend env vars in Render dashboard |
| **Database** | [Convex Cloud](https://convex.dev) | Deploy with `npx convex deploy` |
| **Automation** | [n8n Cloud](https://n8n.io) | Import workflows and activate webhooks |
| **File Storage** | AWS S3 / GCS | Set bucket credentials in backend env vars |

---

## 🧩 Architecture Diagram

```
┌──────────────────────────────────────────────────────────────────────┐
│                          CLIENT (Browser)                             │
│         React.js + Vite + Speech Recognition API + TTS               │
│                                                                        │
│   ┌────────────────────────┐    ┌──────────────────────────────────┐ │
│   │  Convex React Hooks    │    │  Interview Room                  │ │
│   │  (useQuery/useMutation)│    │  • SpeechCapture (STT)           │ │
│   │                        │    │  • AvatarPlayer (TTS)            │ │
│   └──────────┬─────────────┘    └──────────────┬───────────────────┘ │
└──────────────┼───────────────────────────────── ┼─────────────────────┘
               │ HTTPS                             │ REST API
               ▼                                   ▼
┌──────────────────────────┐    ┌────────────────────────────────────┐
│      CONVEX CLOUD         │    │     NODE.JS + EXPRESS BACKEND      │
│   (Real-time Database)    │    │                                    │
│                           │    │  ┌──────────────────────────────┐ │
│  • users                  │    │  │  LLM Pipeline                │ │
│  • interviews             │◄───┤  │  CV + JD → Question Bank     │ │
│  • questions              │    │  └──────────────────────────────┘ │
│  • results                │    │  ┌──────────────────────────────┐ │
│                           │    │  │  NLP Scoring Engine          │ │
└──────────────────────────┘    │  │  5-dimension evaluation      │ │
                                  │  └──────────────────────────────┘ │
                                  │  ┌──────────────────────────────┐ │
                                  │  │  Cloud Storage               │ │
                                  │  │  CV / JD file management     │ │
                                  │  └──────────────────────────────┘ │
                                  └──────────────────┬─────────────────┘
                                                     │ Webhooks
                                                     ▼
                                  ┌────────────────────────────────────┐
                                  │        n8n AUTOMATION              │
                                  │  • Interview Scheduler             │
                                  │  • Feedback Delivery               │
                                  │  • Result Storage                  │
                                  └────────────────────────────────────┘
```

---

## 👤 Author

**Swaraj Babu**
- GitHub: [@Swarajbabu](https://github.com/Swarajbabu)

---

## 📄 License

This project is licensed under the **MIT License**.

---

> Built with ❤️ to make interview preparation smarter, faster, and fully automated.
