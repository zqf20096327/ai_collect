<div align="center">

<a href="https://gta6trim.com"><img src="docs/banner.png" alt="GTA6 Trim — live GTA 6 streams, clipped into Shorts" width="100%"></a>

# GTA6 Trim

**Clip the chaos while it's still live.**

GTA6 Trim watches live GTA 6 streams and long YouTube videos, catches the second chat loses its mind, cuts it to 9:16 with captions, and hands you Shorts ready for TikTok, YouTube Shorts, Instagram Reels and Facebook. On Studio, it posts them for you. You just pick the stream.

[**🌐 gta6trim.com**](https://gta6trim.com) · [Pricing](https://gta6trim.com/#pricing) · [X / Twitter](https://x.com/iqtauhid) · [Facebook](https://www.facebook.com/share/1GjqN4Kegq/)

![Next.js](https://img.shields.io/badge/Next.js-16-black?logo=next.js)
![React](https://img.shields.io/badge/React-19-149eca?logo=react)
![Tailwind](https://img.shields.io/badge/Tailwind-4-38bdf8?logo=tailwindcss)
![Clerk](https://img.shields.io/badge/Auth-Clerk-6c47ff?logo=clerk)
![Dodo Payments](https://img.shields.io/badge/Payments-Dodo-ff2e88)
![Vercel](https://img.shields.io/badge/Hosted%20on-Vercel-black?logo=vercel)

</div>

---

## Why

GTA 6 is the biggest launch in gaming history, and every day hundreds of streamers play it live. The funniest heists, the craziest chases and the "he did NOT just do that" moments happen live, and they're gone in seconds. Clipping pages that post those moments first get the views.

Doing it by hand means watching 10 streams at once, scrubbing VODs, cropping to vertical, writing captions and uploading to 4 apps. **GTA6 Trim does all of that for you.**

## How it works

| Step | What happens |
|---|---|
| **1. Pick a stream** | Live Radar lists every GTA 6 stream on Twitch right now, ranked by viewers and chat hype. Or paste a long YouTube video. |
| **2. It finds the moments** | Chat activity spikes (laughs, "CLIP IT", emote floods) mark the best seconds. Each moment gets a hype score. |
| **3. It edits the Short** | Cut, reframe to 9:16 (the crop follows the action), add captions, export in 1080p with no watermark. |
| **4. Download or post** | Approve in the Clip Queue and download, or save to your cloud storage. On **Studio**, 8.5+ clips from your own channels auto-post to TikTok, YouTube Shorts, Instagram Reels and Facebook. |

<p align="center"><img src="docs/auto-edit.png" alt="Auto-edit timeline: find the moment, cut, reframe to 9:16, caption, export" width="100%"></p>

## Screenshots

**Landing page**: [gta6trim.com](https://gta6trim.com)

<img src="docs/landing.png" alt="GTA6 Trim landing page" width="100%">

**Live Radar**: every live GTA 6 stream, ranked by viewers and hype

<img src="docs/live-radar.png" alt="Live Radar dashboard" width="100%">

**Clip Queue**: review, edit captions, then download (or auto-post on Studio)

<img src="docs/clip-queue.png" alt="Clip Queue with vertical Shorts ready to post" width="100%">

**Works on phone, iPad and desktop**

<img src="docs/mobile.png" alt="GTA6 Trim on mobile" width="100%">

## Features

- 🔴 **Live GTA 6 directory**: every GTA 6 stream on Twitch, live, ranked by viewers and chat hype (Kick & YouTube Live coming soon)
- 🎬 **Live clipping**: clip up to 10 streams at the same time
- 📼 **YouTube long-form import**: paste a VOD of up to 6 hours and get the best moments back as Shorts
- ✂️ **Auto-edit**: cut, 9:16 reframe that follows the action, 1080p, no watermark
- 💬 **AI captions**: 8 caption styles plus your brand colours
- #️⃣ **AI titles & hashtags**: written separately for each platform
- ⬇️ **Download-ready Shorts**: every plan gets 1080p vertical files to post wherever you want
- 📤 **Auto-post & scheduling** *(Studio)*: TikTok, YouTube Shorts, Instagram Reels and Facebook, up to 3 accounts per platform
- ☁️ **Cloud storage**: save clips to Google Drive, Dropbox, OneDrive or Box
- 👥 **Teams**: seats and performance analytics for agencies

## Pricing

<img src="docs/pricing.png" alt="Pricing tickets" width="100%">

| | **Starter** | **Pro** ⭐ | **Studio** |
|---|---|---|---|
| Monthly | **$49**/mo | **$99**/mo | **$199**/mo |
| Yearly (save 20%) | $39/mo | $79/mo | $159/mo |
| Live streams clipped at once | 2 | 5 | 10 |
| YouTube imports / month | 20 (up to 2h) | 60 (up to 4h) | 200 (up to 6h) |
| Clips / month | 200 | 600 | 2,000 |
| AI caption styles | 4 | 8 + brand colours | 8 + brand colours |
| AI titles & hashtags | — | ✓ | ✓ |
| Download Shorts | ✓ | ✓ | ✓ |
| **Auto-post** to TikTok, YouTube, Instagram & Facebook | — | — | ✓ |
| Accounts per platform | — | — | 3 |
| Scheduling | — | — | ✓ |
| Storage | Google Drive | + Dropbox, OneDrive | + Box |
| Team seats | 1 | 1 | 3 |

**Enterprise:** custom volume, multiple workspaces, API access and invoice billing. [Get in touch](mailto:hello@gta6trim.com).

Every plan includes no watermark, 1080p and the live stream directory, and you can cancel anytime. There's a 7-day money-back guarantee on your first payment ([refund policy](https://gta6trim.com/refunds)).

👉 **[Start clipping at gta6trim.com](https://gta6trim.com)**

## Tech stack

| Layer | Tool |
|---|---|
| Framework | [Next.js 16](https://nextjs.org) (App Router, Cache Components, `proxy.ts`) and React 19 |
| Styling and motion | Tailwind CSS 4 and [Motion](https://motion.dev) (scroll-driven editor demo) |
| Login | [Clerk](https://clerk.com): Google, Twitch and email |
| Payments | [Dodo Payments](https://dodopayments.com): subscriptions, customer portal, prorated plan changes, webhooks |
| Live data | Twitch Helix API (GTA 6 streams) |
| Hosting | [Vercel](https://vercel.com) |

### How access works

1. **Clerk** says *who* you are.
2. **Dodo Payments** is the source of truth for *which plan* you have.
3. A signed, HTTP-only cookie (HMAC, Web Crypto) caches the plan and is re-checked with Dodo every 6 hours.
4. `src/proxy.ts` guards `/dashboard`: signed-out users go to `/login` and users without a plan go to `/checkout`.

```
src/
├─ app/
│  ├─ (marketing)/     landing, checkout, login, terms, privacy, refunds
│  ├─ (app)/dashboard/ live radar, YouTube import, clip queue, posted, integrations, billing
│  └─ api/             auth, checkout + confirm, billing portal/change, Dodo webhooks, Twitch streams
├─ components/         EditBay (auto-edit demo), Shell, SocialLinks, LegalPage, …
├─ lib/                plans (single source of pricing), dodo, session, auth-server, account
└─ proxy.ts            Clerk + plan guard
```

## Run it locally

```bash
git clone https://github.com/taufiquebuilds/gta6-trim.git
cd gta6-trim
npm install
cp .env.example .env.local   # fill in Twitch, Clerk, Dodo and SESSION_SECRET
npm run dev                  # http://localhost:3000
```

To create the 6 Dodo subscription products (3 plans × monthly/yearly), run `node scripts/dodo-setup.mjs` with your key in `.env.local`.

## Roadmap

- [x] Live GTA 6 stream directory (Twitch)
- [x] Landing page with a scroll-driven auto-edit demo
- [x] Login (Clerk) and subscriptions (Dodo Payments)
- [x] Dashboard: radar, import, queue, posted, integrations, billing
- [ ] Clipping worker: chat-spike detection, cut, 9:16 reframe, captions
- [ ] YouTube long-form import worker
- [ ] Auto-posting to TikTok, YouTube, Instagram and Facebook (Studio)
- [ ] Kick and YouTube Live support

## Follow

- 🌐 Website: **[gta6trim.com](https://gta6trim.com)**
- 𝕏 X / Twitter: [@iqtauhid](https://x.com/iqtauhid)
- 📘 Facebook: [GTA6 Trim](https://www.facebook.com/share/1GjqN4Kegq/)
- ✉️ Email: [hello@gta6trim.com](mailto:hello@gta6trim.com)

If you like it, ⭐ **star the repo**. It helps more clippers find it.

---

<sub>GTA6 Trim is an independent tool and is not affiliated with, endorsed by or sponsored by Rockstar Games or Take-Two Interactive. Grand Theft Auto and GTA are trademarks of Take-Two Interactive Software. Stream content belongs to its creators.</sub>

<sub>© 2026 GTA6 Trim. All rights reserved. The source is published for transparency and learning. Please don't redeploy it as a competing service.</sub>
