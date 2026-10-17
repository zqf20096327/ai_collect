![Normal Human](./public/banner.png)

# Normal Human - AI Email Client (Better Auth + Nylas + Neon)

Minimal AI-powered email client. Next.js 16 + Better Auth (email/password) + Nylas (mail + calendar) + Neon Postgres + Prisma 7 + tRPC.

## Stack

- Next.js 16, React 19, Tailwind v4
- Better Auth (`src/lib/auth.ts`, `src/lib/auth-client.ts`)
- Nylas v8 (`src/lib/nylas.ts`) - messages + events, grant-based
- Neon Postgres (`DATABASE_URL`), Prisma 7 (`prisma.config.ts`)
- tRPC (`src/server/api/routers/mail.tsx`)

## Setup

1. Install: `bun install` or `npm install`
2. Env `.env`:
```bash
DATABASE_URL="postgresql://...neon.tech/neondb?sslmode=require"
BETTER_AUTH_SECRET="..."
BETTER_AUTH_URL="http://localhost:3001"
NEXT_PUBLIC_URL="http://localhost:3001"
NYLAS_API_KEY="nyk_v0_..."
NYLAS_GRANT_ID="0f789a1f-131a-44fd-8308-c41b8b397e08"
```
3. DB: `npx prisma db push`
4. Dev: `npm run dev` -> http://localhost:3001

## Nylas use cases

- Sign up / sign in at `/sign-up`, `/sign-in` (Better Auth)
- Connect account: `/mail` account switcher -> Add Nylas account -> paste Grant ID + email (tRPC `mail.connectNylasAccount`). Or use `AuthoriseButton` component.
- Read: `mail.getAccounts`, `mail.getThreads` (DB cache), `mail.getEmailDetails` (live Nylas `messages.find`)
- Send: `mail.sendEmail` -> Nylas `messages.send`
- Events demo: `GET /api/nylas/events` lists 5 upcoming primary-calendar events for `NYLAS_GRANT_ID`
```ts
import Nylas from "nylas";
const nylas = new Nylas({ apiKey: process.env.NYLAS_API_KEY! });
const { data: events } = await nylas.events.list({
  identifier: "0f789a1f-131a-44fd-8308-c41b8b397e08",
  queryParams: { calendarId: "primary", limit: 5, start: Math.floor(Date.now()/1000) },
});
```
- Webhook: `POST /api/nylas/webhook` - set URL in Nylas dashboard

## Removed

- Clerk, Stripe, Aurinko removed. Old Aurinko routes return 410. AI chat/compose stubbed (ai SDK v7 `ai/react`/`ai/rsc` removed).
