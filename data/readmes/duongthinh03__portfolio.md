# Portfolio — Dương Quang Thịnh

Trang portfolio cá nhân (Fullstack / .NET Developer). Xây bằng **Vite + Vue 3 + TypeScript**, không dùng template.

## Tính năng

- 🌗 Sáng / Tối (lưu localStorage, không nháy màu khi tải)
- 🌐 Song ngữ **VI / EN** (i18n bằng composable)
- ✨ Animation: reveal khi cuộn, nghiêng 3D + spotlight theo chuột, gõ chữ vai trò, đếm số
- 🔍 SEO: meta + Open Graph + Twitter Card + structured data (schema.org)
- 🖨 In CV / xuất PDF (CSS `@media print` riêng)
- ♿ Tôn trọng `prefers-reduced-motion`, focus-visible, ARIA

## Phát triển

```bash
npm install      # cài dependencies
npm run dev      # chạy dev server (http://localhost:5173)
npm run build    # type-check (vue-tsc) + build production → dist/
npm run preview  # xem thử bản build
```

## Cấu trúc

```
index.html              # Vite entry: meta SEO/OG, favicon, script set theme sớm
public/                 # asset tĩnh phục vụ ở root (og-image, robots, sitemap, portrait.jpg)
src/
  main.ts               # mount app + đăng ký directive
  App.vue               # layout + hiệu ứng cấp trang (progress, scrollspy, spine, cursor glow)
  style.css             # toàn bộ CSS (biến :root, dark mode, print…)
  data/content.ts       # nội dung song ngữ + danh sách dự án
  components/            # Nav, Hero, About, Focus, Projects, Stack, Contact, Footer
  composables/           # useLocale, useTheme, useToast
  directives.ts          # v-reveal (animation cuộn), v-tilt (nghiêng 3D)
```

## Ảnh chân dung

Thả file `portrait.jpg` (ảnh dọc, ~4:5) vào thư mục `public/`. Chưa có file thì khối placeholder gradient hiện thay — không vỡ layout.

## Deploy (Vercel)

1. Import repo vào Vercel → tự nhận preset **Vite** (build `npm run build`, output `dist`).
2. Sau khi có domain, đổi các URL trong `index.html` (canonical/og:url/og:image) và `public/sitemap.xml` sang domain thật, rồi submit sitemap trong Google Search Console.
