# tsong.me

Personal website for Jiaming Song, built with [Astro](https://astro.build/) and
deployed to GitHub Pages.

## Development

The site lives in `site/` and requires Node.js 22 or newer.

```sh
cd site
npm ci
npm run dev
```

Create a production build with:

```sh
npm run build
```

Astro writes the generated site to `site/dist/`.

## Structure

- `site/src/pages/index.astro` — homepage
- `site/src/pages/blog/` — published writing routes
- `site/src/content/blog/` — blog source content
- `site/src/layouts/Layout.astro` — shared page layout and metadata
- `site/src/styles/global.css` — site-wide styles
- `site/public/` — fonts, images, favicons, and `CNAME`

## Deployment

`.github/workflows/deploy-astro-pages.yml` builds `site/` and deploys
`site/dist/` whenever site files are pushed to `main`. GitHub Pages must use
GitHub Actions as its source.
