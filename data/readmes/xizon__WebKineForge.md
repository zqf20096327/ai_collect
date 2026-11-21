# WebKineForge

<p align="center">
  <a href="https://github.com/xizon/WebKineForge">
      <img src="./docs/images/brand.svg"  alt="WebKineForge"  width="450" >
  </a>
</p>


<p align="center">
  <img src="https://img.shields.io/badge/version-v1.0.1 alpha-green?style=flat-square" alt="Version" />
</p>

<p align="center">
🇺🇸 <b>English</b> &nbsp;|&nbsp; 🇨🇳 <a href="./README.zh-CN.md">简体中文</a>
</p>




**A web creation toolkit for developers. Build interactive websites with clean, maintainable HTML and built-in AI Agent support.**

One `npx` command downloads the HTML website template of any published WebKineForge Site — ready to run locally, customize, integrate, and deploy.

```bash
npx webkineforge list
npx webkineforge add default-site
```

## ☀️ Is it right for you?
| Your Needs | Recommendation | Runtime Overhead | Skills Required | AI Collaboration | Template Access |
|---|---|---|---|---|---|
| Interactive animations, clean static HTML templates | **WebKineForge** | Zero-framework runtime | HTML / JS / CSS (optional: Tailwind) | Built-in Agent, simple and secure | Build and generate / One-click `npx` to pull |
| Content-focused with minimal interaction | **[Astro](https://astro.build)** | No JS by default (Islands on demand) | Astro component syntax + basic front-end knowledge | Relies on its own conventions; no dedicated index | Official themes / Starlight |
| Full-stack applications, real-time data | **[Next.js](https://nextjs.org)** / **[Nuxt](https://nuxt.com)** | React/Vue runtime | Full suite of frameworks | Mature ecosystem but no unified structural conventions | Extensive template marketplace |
| Visual website building for designers | **[Framer](https://framer.com)** / **[Webflow](https://webflow.com)** | Platform-hosted | Little to no coding required | Built-in AI | Platform template library |
| Design and publish websites using a visual design tool | **[Figma Sites](https://www.figma.com/sites)** | Platform-hosted | Basic design skills | Built-in AI | Platform template library |
| Build websites quickly without coding | **[Wix](https://www.wix.com)** / **[Squarespace](https://www.squarespace.com)** | Platform-hosted | Little to no coding required | Built-in AI | Platform template library |
| Minimalist websites | **[11ty](https://www.11ty.dev)** / Hand-coded | None | Almost none | Entirely based on manual conventions | None |

## ⚠️ When Not to Choose Me
WebKineForge focuses on the frontend, leaving backend, authentication, and databases to your main system. Its HTML output can be easily integrated into any stack, including Next.js, WordPress, PHP, and Java.



## Introduction

No runtime frameworks or framework-specific APIs. Build reusable components and pages with HTML, TypeScript, Tailwind CSS, and vanilla CSS.

The build outputs standalone HTML pages and assets, ready for direct deployment or integration into any tech stack, including PHP, Java, WordPress, and Next.js.

The system uses a multi-site structure where **each Site works as an independent sandbox**:
- **Create freely**: Each Site has its own pages, components, styles, and templates.
- **Reuse on demand**: Share components and static assets across Sites.

![code cards](./docs/images/webkineforge_3_cards_carousel.gif)


## Terminology

| Term | Description |
|---|---|
| **Project** | The entire workspace containing one or more Sites |
| **Site** | An independent website project within the workspace |
| **Page** | A specific web page inside a Site |
| **Component** | A reusable UI or interaction unit within a Site |
| **Website** | The final built website generated from a Site for visitors. A Site’s build output can also be downloaded with `npx` as a **website template** |

A *Project* can contain multiple *Sites*. Each *Site* builds independently into a self-contained *Website* ready for separate deployment.


## Features

### 🛠️ Developer Experience

- **Simple Development**: No need to learn frontend frameworks (such as React or Vue). Just work in the `sites/` workspace.
- **Rapid workflow**: Built-in CLI commands quickly create Sites, components, and pages, saving repetitive setup work.
- **Three-layer architecture (recommended, not required)**: Each component has three parts: **Template** (TSX, HTML structure), **Controller** (TypeScript, interaction logic), and **Style** (Tailwind / Vanilla CSS). Simple components can omit Controller and Style, see [Flexible Authoring](./docs/en/adding-components.md#73-flexible-authoring).
- **Auto Mounting & Live Preview**：Automatically discover, register, and initialize components with vanilla JS and no extra APIs. Preview components live in the browser.
- **Native interaction ecosystem**: Built on Vanilla JavaScript, making it easy to use libraries like GSAP, Three.js, anime.js, jQuery, and SVG.js.
- **External Library Reuse**: Reuse existing libraries to avoid duplicate bundling.
- **Cross-stack export**: Export components as a reusable React library with a single command.
- **AI-assisted development**: Built-in AI agent for developing components and pages with Cursor, Codex, and Claude Code.
- **Site-level sandboxes**: Isolated directories, configurations, and build outputs per site. Supports quick initialization via CLI
- **Cross-Site resource sharing**: Sites can mutually reference components and static assets without central management.


### 🔍 SEO & Multi-Page Support

- **SEO configuration**: Site-level and page-level settings automatically generate standard `<meta>` and Open Graph (`og:`) tags.
- **Multi-page navigation**: Pages can link to each other using relative paths. The build also generates an `index.html` page for easy navigation and preview.

### 🚀 Build & Delivery

- **One-command website templates**: Download pre-built, maintainable HTML website templates with `npx` CLI, ready for integration and deployment. See [Downloading Website Templates](./docs/en/website-templates.md).
- **Independent builds**: Build each Site separately into a complete, standalone website.
- **Lightweight static output**: Pages and assets compile into standalone static files requiring no runtime framework.
- **Maintainable HTML**: Clean, well-structured HTML that is easy to customize and deploy to a CDN, Nginx, or any static host.
- **Style isolation**: Each Site has its own Tailwind prefix. Use `prefix:` for Tailwind utilities and `prefix-` for custom classes and IDs. See [Style Conventions](./docs/en/style-conventions.md).


## Table of Contents

- [1. Quick Start](#1-quick-start)
- [2. System Architecture](./docs/en/system-architecture.md)
- [3. Site Configuration](./docs/en/site-configuration.md)
- [4. Using AI Agents](./docs/en/ai-agents.md)
- [5. Downloading Website Templates](./docs/en/website-templates.md)
- [6. Creating a Site](./docs/en/creating-a-site.md)
- [7. Adding Components](./docs/en/adding-components.md)
- [8. Adding Pages](./docs/en/adding-pages.md)
- [9. Global Styles](./docs/en/global-styles.md)
- [10. Custom HTML Template](./docs/en/custom-html-template.md)
- [11. Cross-Site Resource Reuse](./docs/en/cross-site-reuse.md)
- [12. React Integration](./docs/en/react-integration.md)
- [13. Browser & Device Support](#13-browser--device-support)
- [14. Contributing](#14-contributing)
- [15. Development Environment](#15-development-environment)
- [16. Support & Acknowledgements](#16-support--acknowledgements)
- [17. License](#17-license)


## 1. Quick Start

Requirements: Node.js 22.12.0+

> **Focus exclusively on `sites/`**
> After cloning the repository and installing dependencies, you can do all your daily development inside the `sites/` directory. Create components, pages, styles, and assets inside the Site you want to work on.



### 1.1 Installation & Setup

```bash
npm install
npm run build
npm run dev     # http://localhost:3000
```

On first use, run `npm run build` to generate TypeScript configuration and component/page indexes for the Agent.

> The build generates `tsconfig.json`, `component-index.json` and `page-index.json` for each Site. Therefore, you **must** run `npm run build` before using `npm run dev` on your first launch.


### 1.2 CLI Commands (Development & Build)

All sites are located in `sites/`, with each subdirectory representing an independent website.

> The project includes `default-site` as an example. The directory name, `name` in `site.json`, and `name` in `package.json` must match.

| Command | Single Site | Multiple Sites |
|---|---|---|
| `dev` | Auto-start | Specify site |
| `build` | Auto-build | Specify site |
| `preview` | Auto-preview | Specify site |
| `export:react` | Auto-export | Specify site |
| `typecheck` | Check TypeScript | Check all configured source files |

**Specify a Site**

```bash
npm run dev -- default-site
npm run build -- default-site
npm run preview -- default-site
npm run export:react -- default-site
```

**Batch Operations**

```bash
npm run build -- all
npm run export:react -- all
```

**Notes**

- Each site outputs to its own `dist/` directory.
- `dev` and `preview` support only one site at a time and do not support `all`.
- Both use port 3000 by default. Do not run them simultaneously.

### 1.3 CLI Commands (Quick Setup)

| Command | Description |
|---|---|
| `npm run create:site -- my-site` | Create a site |
| `npm run create:component -- "My Component" --site my-site` | Create a component |
| `npm run create:page -- "My Page" --site my-site` | Create a page |

All creation commands support the optional `--prefix` flag:

```bash
npm run create:site -- my-site --prefix myprefix
npm run create:component -- "My Component" --site my-site --prefix myprefix
npm run create:page -- "My Page" --site my-site --prefix myprefix
```


### 1.4 Workflow

![Architecture](./docs/images/architecture.svg)


### 1.5 Site Development Workspace

```sh
WebKineForge/
│   ...
└── sites/
    ├── site-a/
    │   ├── src/
    │   │   ├── pages/              # Website pages
    │   │   ├── components/         # Reusable UI components
    │   │   └── styles/             # Global styles
    │   │
    │   ├── public/                 # Static assets
    │   └── dist/                   # Built website
    │
    ├── site-b/
    └── site-c/     
```


## [2. System Architecture](./docs/en/system-architecture.md)
## [3. Site Configuration](./docs/en/site-configuration.md)
## [4. Using AI Agents](./docs/en/ai-agents.md)
## [5. Downloading Website Templates](./docs/en/website-templates.md)
## [6. Creating a Site](./docs/en/creating-a-site.md)
## [7. Adding Components](./docs/en/adding-components.md)
## [8. Adding Pages](./docs/en/adding-pages.md)
## [9. Global Styles](./docs/en/global-styles.md)
## [10. Custom HTML Template](./docs/en/custom-html-template.md)
## [11. Cross-Site Resource Reuse](./docs/en/cross-site-reuse.md)
## [12. React Integration](./docs/en/react-integration.md)



## 13. Browser & Device Support

### 13.1 Desktop Browsers

| Browser | Minimum version |
| ----- | ----- |
| **Google Chrome** | **v112+** |
| **Microsoft Edge** | **v112+** |
| **Apple Safari** | **v16.5+** |
| **Mozilla Firefox** | **v117+** |
| **Internet Explorer** | ❌ **Not supported** |

### 13.2 Mobile OS & Devices

| OS / Device | Browser / Engine | Minimum supported OS version |
| ----- | ----- | ----- |
| **iPhone / iPad** | **iOS Safari** / WebKit | **iOS 16.0.3+** |
| **Android phones / tablets** | **Chrome for Android** | **Android 10+** |


## 14. Contributing

We welcome developers to contribute to WebKineForge by sharing their creations, reporting issues, suggesting improvements, and enhancing documentation.

### 14.1 Share Your Creations

We welcome Sites created and shared by the community!

If you would like to contribute your own creation to WebKineForge, you can submit a Pull Request for a new Site (`sites/{your-site-name}/`).

Please follow the contribution workflow below.

### 14.2 Report Issues & Suggestions

If you encounter any problems or have ideas and suggestions, feel free to reach out through GitHub Issues.

- **Bug Reports**: Describe the issue, steps to reproduce, and expected behavior.
- **Feature Requests**: Suggest new features or improvements.
- **Other Feedback**: Share your experience, observations, or any other valuable ideas.

### 14.3 Contribution Workflow

1. Fork and clone the repository.
2. Install dependencies: `npm install`
3. Make the necessary changes according to the contribution type.
4. Test your changes locally to ensure everything works as expected.
5. Submit a Pull Request with a clear description of the changes and their purpose.

### 14.4 PR Checklist

**General Checklist (Applies to All PRs)**

- [ ] Changes align with the project's purpose and direction.
- [ ] Code follows the existing project structure and conventions.
- [ ] Build and type checks pass, where applicable.
- [ ] No unrelated changes or unnecessary generated files are included.
- [ ] The PR description clearly explains the changes and their purpose.

**Site PR Checklist**

- [ ] Changes are strictly inside `sites/{your-site-name}/`.
- [ ] Directory name uses kebab-case and matches `name` in `site.json` and `package.json`.
- [ ] The Site builds and passes type checks.
- [ ] All dependencies are declared in the corresponding Site's `package.json`.
- [ ] Generated files (`dist/`, `index.json` files, `tsconfig.json`) are excluded.


## 15. Development Environment

- [Tailwind CSS](https://tailwindcss.com/) **4.x.x+**
- [Vite](https://vite.dev/) **8.x.x+**
- [TypeScript](https://www.typescriptlang.org/) **7.x.x+**
- [Preact](https://preactjs.com/) **11.x.x+**


## 16. Support & Acknowledgements

WebKineForge is an open-source project dedicated to bringing an engineering-driven approach to the development of purely static, creative, and interactive websites. It aims to make website template creation, customization, reuse, sharing, and delivery simpler and more efficient — bringing static website development back to the joy of creation.

Through a tool-driven and structured development workflow, we aim to eliminate tedious processes and let developers focus on frontend creation, UI design, and interactive experiences, while enjoying the pure pleasure of building things.

If you find this project useful, your support will be a great motivation for us to keep improving and growing!

Thank you!


## 17. License

Licensed under the [MIT License](https://opensource.org/licenses/MIT).