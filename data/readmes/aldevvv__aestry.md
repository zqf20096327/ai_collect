# Aestry

An open-source, local-first, self-hostable AI design studio for creating app icons, project logos, and Open Graph images.

Built with Next.js 16, React 19, TypeScript, Tailwind CSS 4, shadcn/ui (Base Nova), and pnpm.

## How it works

Aestry is conversation-first, not prompt-to-image. You describe what you want, a **multimodal model** consults with you (asking questions when needed, analyzing reference images, proposing directions), and once a structured **design brief** is ready, you explicitly approve generation with your **image generation model**. Results appear inline in the same conversation, and you keep refining from there.

```
You describe the idea
        |
  Conversation session
        |
  Design consultant (multimodal model)
        |   clarifies, analyzes references, proposes
        v
  Structured design brief  ->  your approval
        |
  Image generation (image model, per approved brief)
        |
  Inline results -> refine / regenerate / download
```

### Model roles

Each provider record can expose two roles, and you choose which provider/model fills each role on the **Providers** page — nothing is selected implicitly:

- **Consultation model** (multimodal): powers the design consultant — brainstorming, chat, and reading reference images.
- **Image generation model**: produces the assets when you approve a brief.

A single provider can serve both roles, or you can mix providers.

### Skills

Asset types are internal skills, each shaping both consultation and generation:

- **App Icon** — square composition, strong silhouette, small-size legibility.
- **Logo** — brand marks and wordmarks, distinctiveness and scalability.
- **OG Image** — landscape (~1200×630) social preview cards with clear hierarchy.

The final image prompt is compiled **server-side** from the validated brief and the selected skill's constraints — the client never supplies privileged generation instructions.

## Providers (server-side credentials)

Providers are configured through the **server environment** — the browser never sees an API key. Copy `.env.example` to `.env.local` and fill in what you use:

- **Google Gemini Developer API** — `GOOGLE_API_KEY` (a [Google AI Studio](https://aistudio.google.com/apikey) key), built on the official `@google/genai` SDK.
- **Google Vertex AI** — `GOOGLE_CLOUD_PROJECT` + `GOOGLE_CLOUD_LOCATION`, authenticated with Application Default Credentials or workload identity.

Optionally pin default models per role with `AESTRY_GEMINI_CHAT_MODEL`, `AESTRY_GEMINI_IMAGE_MODEL`, `AESTRY_VERTEX_CHAT_MODEL`, and `AESTRY_VERTEX_IMAGE_MODEL`.

Available models are **loaded from the provider itself** through the SDK and split into the two roles. Nothing is hardcoded, and a selected model is validated against the provider's own discovery list — Aestry never silently routes your request to a different billable model. The Providers page shows configuration status, verifies connections with a bounded non-billable check, and lets you refresh model metadata. Browser-held keys from older versions were removed and must be added to the server environment.

Custom OpenAI-compatible endpoints will return as a server-configured provider; they are marked Coming Soon.

### Access protection (please read)

Server-owned credentials mean an unprotected public deployment would let strangers spend your AI quota. Set `AESTRY_ACCESS_SECRET` in the server environment to require operator sign-in: privileged endpoints (consultation, generation, model discovery, diagnostics, project context, database status) then need a session — the browser receives only a derived, HttpOnly cookie, never the secret.

**Production builds fail closed**: without `AESTRY_ACCESS_SECRET`, privileged operations are disabled with configuration guidance rather than silently exposed. Development builds run in an explicit local-only mode (reads open, writes same-origin only); set `AESTRY_ALLOW_LOCAL_MODE=false` to fail closed outside production too. Cross-site state-changing requests are rejected in every mode. Diagnostics never include prompts, transcripts, or keys by default; set `AESTRY_ENABLE_DIAGNOSTICS=true` only while troubleshooting, and know that excerpts may contain conversation fragments.

### Projects

Projects group conversations and carry reusable design context: a name, an optional description, and optional standing instructions. Chats created inside a Project consult with that context (clearly labeled, non-authoritative — it never overrides security or approval boundaries), and Project chats live in their Project's list rather than global Recent. Deleting a Project never destroys anything: its conversations return to Recent with all messages, and generated assets stay in History.

### Temporary Chat

The header's timer icon starts a Temporary Chat: a fully in-memory conversation that never touches IndexedDB, never appears in Recent or History, and is discarded when you leave the page. You can consult, generate (with the usual explicit approval), and download images while it is active. Temporary means **Aestry** stores nothing — it is not a claim about your provider's retention policies.

### Storage

- **Conversations, messages, design briefs, and generated images** live in your browser's **IndexedDB** (via `idb`). Writes are serialized per conversation, image binaries are stored atomically with their metadata, and schema migrations backfill existing data without ever clearing it.
- **Generated assets live independently of conversations**: deleting a chat keeps every completed image in the History gallery, and deleting a Project never touches conversations or assets.
- **Server-side database persistence is planned** (Supabase/Neon/PostgreSQL connections can already be verified on the Database page) — configuring a database never silently enables synchronization.
- Browser storage is finite. Very large image batches can hit quota; failures surface as warnings, images stay viewable for the session (marked "Session only"), and conversation state stays in memory.

## Provider capabilities (honesty notes)

- Model capability classification during discovery is a **heuristic**, not a verified guarantee.
- Not every multimodal model accepts image input — Aestry checks an inferred capability before sending references and tells you when it skipped them.
- The OpenAI-compatible `images/generations` path does **not** accept reference images; requests through it say so instead of pretending they mattered.
- Google image models accept reference images (editing-style conditioning). Refinement without image input is a **new generation guided by the brief**, not a pixel-perfect edit.
- Raster models do not produce SVG/vector files, and generated lettering (especially in OG images) may contain rendering mistakes — always review.

## GitHub project context

If a message contains a public `github.com` repository URL, Aestry can gather bounded, read-only context (description, language, topics, README excerpt) and feed it to the consultant as clearly-labeled, untrusted reference material. No cloning, no code execution, no private-repo access. If fetching fails, the conversation continues without it.

## Security notes

- Privileged endpoints are operator-gated when `AESTRY_ACCESS_SECRET` is set (fail-closed session checks, throttled sign-in, SameSite=Strict cookie, Origin-validated CSRF protection); in unprotected mode, cross-site state-changing requests are rejected.
- All outbound requests to user-configured destinations validate protocol and destination (private ranges and cloud metadata hosts blocked by default), and redirects are re-validated per hop with credential headers stripped on cross-origin hops.
- Request bodies and provider responses are read with hard size caps; provider operations run under a small concurrency limit; login attempts are throttled per process.
- Diagnostics follow an allowlisted structured schema: no prompts, transcripts, or keys by default; raw excerpts exist only behind `AESTRY_ENABLE_DIAGNOSTICS=true` with credential redaction.
- Rendered Markdown is treated as untrusted: no raw HTML, scheme-restricted links, noopener externals, no model-controlled images.
- Generated-image URL downloads are content-type checked and size-bounded.
- Known limitations: hostname validation is lexical (DNS-rebinding protection is left to network-level controls for exposed deployments); without `AESTRY_ACCESS_SECRET`, non-browser callers on the network can use provider operations — configure the secret for anything reachable beyond localhost.

## Development

```bash
pnpm install
pnpm dev        # local development (manual browser testing)
pnpm typecheck  # TypeScript
pnpm lint       # ESLint
pnpm test       # vitest unit tests (mocked providers, no network)
pnpm build      # production build
pnpm audit      # dependency audit
```

What is verified by static checks and tests: type safety, lint rules, production build, skill prompt compilation, consultation parsing (including malformed model output), conversation turn bounding, outbound URL policy, and provider response parsing with mocked providers.

What still requires **you**: visual/UX review across themes and breakpoints, and live generation against real provider keys (never exercised by the automated suite).
