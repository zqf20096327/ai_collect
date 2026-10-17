![Flunkey Flow banner](./public/assets/onboarding-1.webp)

# Flunkey.space

Marketing site and docs for **Flunkey** — a free, open-source voice dictation and AI assistant app for Windows 10 and 11. Hold a hotkey, speak, release — text appears where you work.

<div align="center">

[![Download Flunkey for Windows](https://img.shields.io/badge/Download-For_Windows-e84900?style=for-the-badge&logo=windows&logoColor=white)](https://www.flunkey.space/download)
[![Read the Docs](https://img.shields.io/badge/Docs-Read_the_Docs-141413?style=for-the-badge&logo=book&logoColor=white)](https://www.flunkey.space/docs)
[![Privacy Policy](https://img.shields.io/badge/Privacy-Policy-141413?style=for-the-badge&logo=shield&logoColor=white)](https://www.flunkey.space/privacy)
[![Terms of Service](https://img.shields.io/badge/Terms-Terms_of_Service-141413?style=for-the-badge&logo=filetext&logoColor=white)](https://www.flunkey.space/terms)

![Version v1.0.0](https://img.shields.io/badge/version-v1.0.0-blue?style=flat-square)
![License MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)

</div>

## What this repo is

The Next.js (App Router) website: landing page, feature pages (F8 dictate, F9 ask AI, F10 transform), use-case pages, comparison pages, full `/docs`, founder and Promptology pages, plus SEO (metadata, JSON-LD, sitemap, per-route OG images) and `llms.txt`.

## Tech stack

Next.js 16 (App Router, Turbopack) · React 19 · Tailwind CSS 4 · TypeScript · `next/font` (Inter, Source Serif 4, JetBrains Mono) · `next-themes` · `lucide-react` · `sharp`

## Project structure

- `app/` — routes, layouts, metadata, `opengraph-image.tsx` files, `sitemap.ts`, `robots.ts`, `manifest.ts`
- `components/` — shared UI (`Header`, `Footer`, `FeaturePage`, `PersonaPage`, `ComparePage`, `docs`, icons, `VideoLoop`, `OgCard`)
- `lib/` — `site.ts` (URLs, nav, route list), `docs.ts`, `cn.ts`
- `public/` — assets, videos, icons, `llms.txt`, installer
- `scripts/` — one-off tooling (e.g. IndexNow submit, not wired into builds)
