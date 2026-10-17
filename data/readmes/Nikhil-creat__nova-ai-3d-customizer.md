# NOVA — 3D Product Customizer with Agentic AI + RAG + CNN

**DESIGNED AND DEVELOPED BY**
# **NIKHIL CHARY SRIRAMOJU**
BTech CSE (Final Year)

- GitHub: [Nikhil-creat](https://github.com/Nikhil-creat)
- LinkedIn: [nikhil-chary-sriramoju](https://in.linkedin.com/in/nikhil-chary-sriramoju-95041b38a)
- Email: sriramojunikhil66@gmail.com
- Instagram: [@nikhil__sriramoju](https://www.instagram.com/nikhil__sriramoju)
- Facebook: [Profile](https://www.facebook.com/profile.php?id=100079201124141)

A real-time, browser-based 3D product configurator — rotate, recolor,
re-material, and engrave a 3D model — augmented with:
- **CNN** — an in-browser convolutional neural network (MobileNetV2, via
  TensorFlow.js) that classifies an uploaded reference photo and suggests a
  matching material finish.
- **RAG (Retrieval-Augmented Generation)** — a TF-IDF retrieval index over a
  local knowledge base (product specs, policies) that grounds every answer
  in real source text instead of guessing.
- **Agentic AI** — a transparent perceive → retrieve → plan → act → respond
  loop that decides which internal tool to call (price calculator, material
  recommender, or grounded lookup) for each user question, and returns its
  reasoning trace alongside the answer.
- **Docker** — the RAG/agent backend and the static frontend each ship with
  their own `Dockerfile`, orchestrated together with `docker-compose.yml`.

## Project structure
```
nova-project/
├── index.html            # App shell + markup
├── Dockerfile             # Frontend container (nginx, static files)
├── docker-compose.yml     # Orchestrates frontend + backend containers
├── css/style.css          # Futuristic, responsive theme
├── js/
│   ├── main.js              # Entry point, wires scene + UI + AI features
│   ├── scene.js              # Three.js scene, GLTF/Draco model loading, controls
│   ├── ui.js                 # Swatches, materials, pricing, legal modals, cookies
│   └── assistant.js          # CNN image analyzer + agentic chat client
├── assets/favicon.svg
├── models/                 # Put your real product.glb here (see below)
├── backend/                # Agentic AI + RAG service (Python/FastAPI)
│   ├── main.py                # API endpoints (/api/agent, /api/health)
│   ├── agent.py                # Agent loop: intent detection, tool calls
│   ├── rag.py                   # TF-IDF retrieval over knowledge_base/
│   ├── knowledge_base/            # Source-of-truth docs the agent retrieves from
│   ├── requirements.txt
│   └── Dockerfile
└── README.md
```

## How the AI pieces fit together
1. A visitor uploads a reference photo → the **CNN** (MobileNetV2) classifies
   it client-side, and the predicted label is mapped to Matte/Glossy/Chrome,
   which is applied live to the 3D model.
2. A visitor asks the assistant a question → the **agent** classifies intent,
   the **RAG** index retrieves the most relevant passage(s) from
   `backend/knowledge_base/`, the agent picks a tool (price calculator,
   material recommender, or direct grounded answer), and returns both the
   answer and its reasoning trace.
3. Everything the agent says is traceable to a real source document — it does
   not fabricate policy or pricing details.

## Using your own real 3D model
Drop a Draco-compressed `.glb` file at `models/product.glb`. On load, the app
automatically centers and scales it, and applies color/material/engraving
controls to every mesh material it finds. If no model is present, the app
falls back to a procedural placeholder mesh so it still runs.

To create `product.glb`:
1. Export your model from Blender/Maya/etc. as glTF Binary (.glb).
2. Compress it with the gltf-transform CLI: `npx @gltf-transform/cli draco product.glb product.glb`
3. Place the compressed file at `models/product.glb`.

## Run it locally

### Frontend only (3D configurator + CNN, no chat backend)
```bash
npx serve .
# or
python3 -m http.server 8080
```
Then open the printed local URL. (Opening `index.html` directly via
`file://` will NOT work — ES module imports require a real HTTP server.)

### Full stack with Docker (frontend + agentic AI/RAG backend)
```bash
docker compose up --build
```
- Frontend: http://localhost:8080
- Backend health check: http://localhost:8000/api/health
- The frontend's `js/assistant.js` calls the backend at
  `window.NOVA_BACKEND_URL` (defaults to `http://localhost:8000`). Set this
  global before `main.js` loads (e.g. a small inline `<script>` in
  `index.html`) if you deploy the backend elsewhere.

## Upload to GitHub and publish with GitHub Pages

1. **Create a repository**
   - Go to github.com → New repository → name it (e.g. `nova-customizer`) → Create.

2. **Upload the files**
   - Easiest (no git required): open your new repo → "Add file" → "Upload files" →
     drag in every file/folder from this project (keep the folder structure:
     `css/`, `js/`, `assets/`, `models/`, `index.html`, `README.md`) → Commit changes.
   - Or with git:
     ```bash
     git init
     git add .
     git commit -m "Initial commit: NOVA 3D customizer"
     git branch -M main
     git remote add origin https://github.com/<your-username>/nova-customizer.git
     git push -u origin main
     ```

3. **Enable GitHub Pages**
   - In your repo, go to **Settings → Pages**.
   - Under "Build and deployment" → Source, choose **Deploy from a branch**.
   - Branch: `main`, folder: `/ (root)` → **Save**.

4. **Access your live site**
   - After a minute or two, GitHub shows your URL at the top of the Pages
     settings screen, typically:
     `https://<your-username>.github.io/nova-customizer/`
   - Every future push to `main` redeploys automatically.

### Important: GitHub Pages only serves the static frontend
GitHub Pages hosts static files only — it cannot run the Python/Docker
backend. The 3D configurator and the **CNN** photo analyzer (both run
entirely in the visitor's browser) work fully on GitHub Pages. The
**agentic AI + RAG chat assistant** needs the `backend/` container running
somewhere that can execute Python — e.g. Render, Railway, Fly.io, or your
own server — using `docker compose up --build` or `docker build` on the
`backend/` folder alone. Then set `window.NOVA_BACKEND_URL` in `index.html`
to that backend's public URL so the GitHub Pages frontend can reach it.

## Groq API (optional, free) — smarter agent responses
By default the agent phrases answers from a deterministic template — reliable,
but a bit robotic. Add a **free** Groq API key to have the agent phrase its
RAG-grounded answers naturally via a real LLM, with automatic fallback to the
template if the key is missing or the call fails for any reason (offline,
rate-limited, cold start) — the assistant never breaks either way.

1. Get a free key at https://console.groq.com/keys (no credit card required).
2. Set it as an environment variable before starting the backend:
   ```bash
   export GROQ_API_KEY="your-key-here"
   docker compose up --build
   ```
   Or add it to a `.env` file next to `docker-compose.yml`:
   ```
   GROQ_API_KEY=your-key-here
   GROQ_MODEL=llama-3.1-8b-instant
   ```
3. Check `/api/health` — it reports `"llm": "groq"` once the key is picked up,
   or `"llm": "template-fallback"` if not set.

## Reliability & performance
- Frontend requests to the agent backend use a client-side timeout (8s) and
  automatic retry with backoff (`js/assistant.js`), so a slow or cold backend
  doesn't hang the UI.
- The Groq call itself has its own timeout and falls back to the deterministic
  template answer on any failure — the assistant always responds.
- The CNN model loads once and is cached in memory for the rest of the
  session, so repeat photo uploads classify instantly.
- The Docker backend has a `HEALTHCHECK` so orchestrators (Compose, Kubernetes,
  Render, etc.) can detect and restart it automatically if it stops responding.

## Futuristic features
- **Monochrome UI** — a single-hue, high-contrast theme (grays only) for a
  clean, professional, non-"AI slop" look, with light/dark auto-adapting via
  `prefers-color-scheme`.
- **Voice input** — the assistant chat box supports speech-to-text via the
  browser's native Web Speech API (tap the mic icon); the button hides itself
  automatically on browsers that don't support it.
- **In-browser CNN vision** — no server round-trip needed to classify a
  reference photo; MobileNetV2 runs entirely client-side.
- **Transparent agent reasoning trace** — every backend response includes the
  step-by-step trace (`perceive → retrieve → plan → act → respond`) so you can
  see exactly how the agent reached its answer.

## Notes
- All third-party scripts load from the `unpkg.com` CDN via an import map in
  `index.html` — no local dependencies to install.
- Legal copy in `js/ui.js` (Privacy/Terms/Refund/Business) is placeholder text
  for a demo; replace it with your real policies before taking real orders.
- Cookie consent and the "Add to cart" consent checkbox are functional UI
  patterns, not a payment/checkout backend — wire them to a real payment
  provider and backend before production use.
