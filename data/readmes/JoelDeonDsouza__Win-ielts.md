# 🚀 Win IELTS

Win IELTS is a web-based application that helps users prepare for the IELTS exam with the help of AI.
It provides intelligent practice materials, personalized feedback, and progress tracking features to improve users’ English skills and boost their chances of achieving their target band score.

## Tech Stack

**Frontend**

- React (v19.1.0)
- React Router DOM (v7.9.3)
- TypeScript (~5.9.3)
- Vite (v7.1.7)

**Styling**

- Styled Components (v6.1.19)

**AI & APIs**

- AI SDK (v4.3.19)
- Google Generative AI (v0.24.1)
- AI SDK Google (v1.2.22)
- Axios (v1.12.2)

**Data & Storage**

- IndexedDB (idb) (v8.0.3)
- UUID (v13.0.0)
- Cheerio (v1.1.2)

**Development Tools**

- ESLint (v9.36.0)
- Prettier (v3.6.2)
- Husky (v9.1.7)
- lint-staged (v16.1.2)
- TypeScript ESLint (v8.45.0)

## Screenshots

![App Screenshot](/public/pageOne.png)

![App Screenshot](/public/pageTwo.png)

![App Screenshot](/public/pageThree.png)

![App Screenshot](/public/pageFour.png)

![App Screenshot](/public/pageFive.png)

### Installation

Clone the project

```bash
git clone https://github.com/JoelDeonDsouza/Win-ielts.git
```

Go to the project directory

```bash
cd winielts
```

Install dependencies

```bash
npm install
```

### Development

Start the development server with Vite

```bash
npm run dev
```

Or use Vercel for development

```bash
vercel dev
```

### Production

Build the project

```bash
npm run build
```

Preview the production build

```bash
npm run preview
```

## Available Scripts

| Command                | Description                                             |
| ---------------------- | ------------------------------------------------------- |
| `npm run dev`          | Start development server with Vite                      |
| `npm start`            | Start development server (alias for dev)                |
| `npm run build`        | Build TypeScript and create optimized production bundle |
| `npm run lint`         | Run ESLint to check code quality                        |
| `npm run lint:fix`     | Fix ESLint issues automatically                         |
| `npm run format`       | Format code with Prettier                               |
| `npm run format:check` | Check code formatting without modifying files           |
| `npm run preview`      | Preview the production build locally                    |
| `npm run prepare`      | Initialize Husky for Git hooks                          |

## Code Quality

The project includes automated code quality checks through ESLint, Prettier, and Husky.

Run linting

```bash
npm run lint
```

Fix linting issues

```bash
npm run lint:fix
```

Format code

```bash
npm run format
```

Check formatting

```bash
npm run format:check
```

## 📦 Environment Variables (`.env`)

```env

GOOGLE_API_KEY=

```

## 🔗 Demo

```
https://win-ielts.vercel.app
```
