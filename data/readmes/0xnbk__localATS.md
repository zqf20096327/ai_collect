<div align="center">
  <img src="public/favicon.svg" alt="localATS logo" width="84" />
  <h1>localATS</h1>
  <p><strong>Private • Local • Instant AI Resume Analysis</strong></p>
  <p>
    <img src="https://img.shields.io/badge/status-beta-6C5CE7?style=for-the-badge&labelColor=0A0E27" alt="Beta status" />
    <a href="https://localats.com" target="_blank" rel="noopener noreferrer">
      <img src="https://img.shields.io/badge/app-localats.com-00F5A0?style=for-the-badge&labelColor=0A0E27" alt="localats.com" />
    </a>
  </p>
</div>

localATS is a browser-based ATS resume analyzer that runs AI locally on your device. Resume and job description data are processed in-browser and are not uploaded to your servers.

## Why localATS

- Privacy-first workflow (no account required, no backend resume processing)
- Local inference with Transformers.js + ONNX Runtime Web
- Supports pasted text and PDF input
- Fast compatibility scoring with semantic and domain checks
- Open source and auditable

## Current status

localATS is in **beta** phase. Core analysis is production-usable, while some quality and model-tuning improvements are still in progress.

## Quick start (local development)

```bash
git clone https://github.com/0xnbk/localATS.git
cd localATS
npm install
cp .env.example .env.development
npm run download-models
npm run dev
```

Open the dev server URL shown by Vite (typically `http://localhost:5173`).

## Available scripts

| Command | Purpose |
|---|---|
| `npm run dev` | Start local dev server |
| `npm run build` | Build production assets to `dist/` |
| `npm run build:offline` | Production-mode build |
| `npm run preview` | Preview built app |
| `npm run serve` | Preview on port `3000` |
| `npm run test` | Run tests in watch mode |
| `npm run test:run` | Run tests once (CI-style) |
| `npm run test:ui` | Run Vitest UI |
| `npm run download-models` | Download required HF models to `public/models` |
| `npm run setup:local` | Alias for model download |

## Environment configuration

Copy `.env.example` and choose one mode:

- Local mode (development):
  - `VITE_MODEL_SOURCE=local`
  - `VITE_MODEL_BASE_URL=/models`
  - Model files served from `public/models/...`
- Remote mode (production):
  - `VITE_MODEL_SOURCE=remote`
  - `VITE_MODEL_BASE_URL=https://<your-model-host>`
  - Use HuggingFace-style model paths (`<model>/resolve/main/...`)

The app reads model settings from [`src/config/model-config.ts`](src/config/model-config.ts).

## Deployment (Cloudflare Workers static assets)

This repo includes [`wrangler.jsonc`](wrangler.jsonc) configured to serve `dist/` as Worker assets.

```bash
npm run build
npx wrangler deploy
```

If you are deploying with remote models, ensure your production env file values are set before building.

## Tech stack

- Vite + TypeScript
- Transformers.js
- ONNX Runtime Web
- Comlink + Web Workers
- PDF.js
- Tailwind CSS (utility styling support)

## AI models

- Semantic model: [`0xnbk/nbk-ats-semantic-v1-en`](https://huggingface.co/0xnbk/nbk-ats-semantic-v1-en)
- Domain model: [`0xnbk/nbk-ats-domain-v1-en`](https://huggingface.co/0xnbk/nbk-ats-domain-v1-en)

Hugging Face quick links:

<div>
  <a href="https://huggingface.co/0xnbk/nbk-ats-semantic-v1-en" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/HuggingFace-Semantic%20Model-F59E0B?style=for-the-badge&logo=huggingface&logoColor=black" alt="Semantic model on Hugging Face" />
  </a>
  <a href="https://huggingface.co/0xnbk/nbk-ats-domain-v1-en" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/HuggingFace-Domain%20Model-F59E0B?style=for-the-badge&logo=huggingface&logoColor=black" alt="Domain model on Hugging Face" />
  </a>
</div>

Both are used for compatibility analysis between resume and job description content.

## Project structure

```text
localATS/
├─ src/
│  ├─ core/           # ATS engine and scoring logic
│  ├─ ui/             # UI behavior and interactions
│  ├─ services/       # PDF and sample helpers
│  ├─ workers/        # Worker-side ATS execution
│  └─ styles/         # App styles
├─ public/            # Static assets + model files (local mode)
├─ scripts/           # Model download script
├─ tests/             # Unit and integration tests
└─ wrangler.jsonc     # Cloudflare Worker asset deploy config
```

## Sponsor

<div align="center">
  <a href="https://fyn.link" target="_blank" rel="noopener noreferrer">
    <img src="public/sponsor.webp" alt="fyn.link sponsor logo" width="260" />
  </a>
  <h3>Sponsored by fyn.link</h3>
  <p><strong>Privacy-First URL Shortener</strong></p>
  <p>Create secure and professional links with end-to-end encryption.</p>
  <p>
    <a href="https://fyn.link" target="_blank" rel="noopener noreferrer">
      <img src="https://img.shields.io/badge/Visit-fyn.link-10B981?style=for-the-badge&labelColor=0A0E27" alt="Visit fyn.link" />
    </a>
  </p>
</div>

See [SPONSOR.md](SPONSOR.md) for full sponsorship details.

## License

Apache 2.0. See [LICENSE](LICENSE).
