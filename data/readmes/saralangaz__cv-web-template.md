# cv-web-template

A free, open-source template to build your own **personal CV website with an AI chat assistant** — no backend required, no paid subscriptions, deployable in under 30 minutes.

**Live example:** [saralangaz.com](https://saralangaz.com) — built with this architecture.

![cv-web-template preview](preview.png)

---

## What you get

- Single-file HTML/CSS/JS CV — fast, no build step, no dependencies
- Bilingual ES/EN toggle out of the box
- Sections: Skills, Experience, Projects, Certifications & Education, Contact
- **AI chat widget** — visitors can ask questions about your profile, powered by Llama 3.3 (free)
- Config-driven — your personal data stays in a gitignored file, never committed

---

## 100% free stack

| What | How | Cost |
|---|---|---|
| CV hosting | GitHub Pages or Cloudflare Pages | Free |
| AI chat model | Llama 3.3 70B via Cloudflare Workers AI | Free (10k req/day) |
| Chat proxy | Cloudflare Worker | Free (100k req/day) |
| Rate limiting | Cloudflare KV | Free |
| Custom domain | Optional — Cloudflare Registrar | ~$10/year |

Everything runs on free tiers. The only optional cost is a custom domain.

---

## Quickstart

### 1. Fork or use this template

Click **Use this template** → **Create a new repository** on GitHub.

### 2. Set up your personal config

```bash
# Root config — your contact info and Worker URL
cp config.example.js config.js

# Worker config — your AI profile (system prompt)
cp chat-worker/config.example.js chat-worker/config.js
```

Edit both files. They are gitignored — your personal data never gets committed.

### 3. Customise the CV content

Open `index.html` and look for the `<!-- CUSTOMIZE -->` comments. Update:
- Hero: your name, title, tagline
- Skills: your tech stack
- Experience: your work history
- Projects: your projects
- Certifications: your credentials

### 4. Preview locally

```bash
npx serve .
# Open http://localhost:3000
```

### 5. Deploy for free

**Option A — GitHub Pages:**
- Push to a repo named `yourusername.github.io`
- Settings → Pages → Branch: main → Save
- Live at `https://yourusername.github.io`

**Option B — Cloudflare Pages (recommended if you want a private repo):**
- Cloudflare Dashboard → Pages → Connect to Git
- Select your repo, no build command needed
- Live at `yourproject.pages.dev`

### 6. Set up the AI chat (optional but impressive)

```bash
cd chat-worker
npm install -g wrangler
wrangler login
wrangler kv:namespace create RATE_LIMIT_KV   # paste the id into wrangler.toml
wrangler deploy
```

Then add the Worker URL to your `config.js`:
```js
workerUrl: "https://your-worker.yoursubdomain.workers.dev",
```

Full instructions: [chat-worker/DEPLOY.md](chat-worker/DEPLOY.md)

---

## Custom domain (~$10/year, optional)

The cleanest setup: buy your domain at **Cloudflare Registrar** (at-cost pricing, ~$10/year for `.com`).

If using Cloudflare Pages:
1. Cloudflare Dashboard → your Pages project → Custom domains → Add `yourname.com`
2. Done — DNS is configured automatically since the domain is already in Cloudflare

If using GitHub Pages:
1. Add these DNS records in Cloudflare:
```
A  @  185.199.108.153
A  @  185.199.109.153
A  @  185.199.110.153
A  @  185.199.111.153
CNAME  www  yourusername.github.io
```
2. GitHub repo → Settings → Pages → Custom domain → `yourname.com`
3. Add a `CNAME` file to your repo with your domain

---

## Project structure

```
cv-web-template/
├── index.html              # Your CV — edit the CUSTOMIZE sections
├── config.js               # 🔒 gitignored — fill in from config.example.js
├── config.example.js       # Template for your personal config
├── .gitignore
├── README.md
└── chat-worker/
    ├── worker.js           # Cloudflare Worker proxy — no need to edit
    ├── config.js           # 🔒 gitignored — your domain + AI profile
    ├── config.example.js   # Template for your Worker config
    ├── wrangler.toml       # Worker deployment config
    └── DEPLOY.md           # Step-by-step chat setup guide
```

---

## Customisation

**Colors and fonts:** edit the `:root` CSS variables at the top of `index.html`.

**Design:** this template uses a clean, minimal design intentionally different from the live example. Make it yours — swap fonts, change the layout, go dark mode. The architecture (config pattern, Worker proxy, bilingual toggle) is what this template provides; the visual design is yours to own.

**AI chat suggestions:** edit the `SUGGESTIONS` object in the JS section of `index.html`.

---

## License

MIT for the code and architecture.

The visual design of [saralangaz.com](https://saralangaz.com) is not included in this template and is not available for reuse — please create your own.

---

## Questions?

Open an issue or reach out via [saralangaz.com](https://saralangaz.com).
