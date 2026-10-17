# AI Interview Agent

> An AI interview system that does more than generate one-off reports.  
> It turns each interview into a **long-term candidate growth graph**.

---

## Why this project

Most AI interview tools stop at "generate a report."  
This project focuses on **continuous candidate intelligence**:
- persistent candidate profiles
- session-over-session issue tracking
- incremental learning board updates
- visual analytics dashboard

---

## Highlights

- **Explicit state-machine interview flow**: intro -> technical -> personality -> report.
- **Candidate library** keyed by `name + email` for cross-session continuity.
- **Dashboard visualization**: score trend, issue mix, board status, experience heat.
- **Automatic post-session review**: repeated issues, new issues, fixed issues.
- **Profile backfill from raw Q/A**: progressively refines independent library profile.
- **Split storage architecture**: decomposes heavy `candidate.json` into maintainable files.

---

## Product Flow

1. Create or link a candidate  
2. Run interview session (text-first, voice optional)  
3. Generate structured report  
4. Auto-merge analysis + update learning board  
5. Refresh independent candidate library profile  
6. Track progress in dashboard

---

## Screenshots

> Real screenshots are now wired in the order of usage flow.

### 1) Interview Page

[![Interview Page](assets/interview_page.png)](assets/interview_page.png)

### 2) Report Pages

| Report Head | Personal Assessment | Potential & Experience Evaluation |
|---|---|---|
| [![Report Head](assets/report_page_head.png)](assets/report_page_head.png) | [![Report Personal Assessment](assets/report_page2_personal_assess.png)](assets/report_page2_personal_assess.png) | [![Report PerExp Evaluation](assets/report_page3_perexp_evaluation.png)](assets/report_page3_perexp_evaluation.png) |

### 3) Candidate Dashboard

[![Candidate Dashboard](assets/dashboard.png)](assets/dashboard.png)

> Tip: all images are clickable for full-size preview on GitHub.

---

## Quick Start

```bash
git clone https://github.com/GoDiao/ai-interview-agent.git
cd ai-interview-agent
python -m venv .venv

# Windows
.venv\Scripts\activate
# macOS / Linux
# source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env   # Windows: copy .env.example .env
python run.py
```

Open: `http://127.0.0.1:8765`

---

## Candidate Profile Backfill API

`POST /api/candidates/{candidate_id}/library_profile/rebuild`

- `session_id`: optional, backfill from one specific session
- `all_sessions=true`: replay all done sessions sequentially
- `clear_existing=true`: optional reset before full rebuild

---

## Split Candidate Storage

Per-candidate directory: `data/candidates/{candidate_id}/`

- `candidate.meta.json`
- `profile.snapshot.json`
- `profile.library.json`
- `analysis.store.json`
- `learning.board.json`
- `advice.registry.json`
- `candidate.json` (legacy compatibility)

Migration:

```bash
python scripts/migrate_candidate_split_storage.py
```

Related `.env` flags:

- `CANDIDATE_SPLIT_STORAGE_ENABLED=true`
- `CANDIDATE_LEGACY_MIRROR_WRITE=false`

---

## Voice Support

- STT: `sensevoice_http` / `fake` / `local_whisper` / iFlytek
- TTS: `browser` (default) / `kokoro`

See `.env.example` and `docs/SENSEVOICE.md`.

---

## Tech Stack

- **Backend**: FastAPI, Pydantic, async orchestration
- **Frontend**: HTML/CSS/JS + Chart.js
- **Storage**: JSON-based local persistence with split-candidate schema
- **LLM**: OpenAI-compatible APIs

---

## Docs

| File | Description |
|---|---|
| [SPEC.md](SPEC.md) | Product scope and API |
| [STATE_MACHINE.md](STATE_MACHINE.md) | State machine contract |
| [RESEARCH.md](RESEARCH.md) | Technical notes |
| [docs/SENSEVOICE.md](docs/SENSEVOICE.md) | SenseVoice integration |

---

## Roadmap

- [x] Core interview flow
- [x] Candidate library + dashboard
- [x] Auto review + incremental learning board
- [x] Session-by-session profile backfill
- [x] Split storage migration
- [ ] Multi-role interview templates and weighted scoring
- [ ] Team collaboration view for multiple interviewers

---

If this project is useful, feel free to star it and open issues/PRs.
