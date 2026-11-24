# MockRoom

Helping CS students and fresh grads crack interviews. Free, just open it and practice.

MockRoom is a free website. No download, no install. Just open it and start practicing.

Most of us prepare alone and find out what we are weak at in the real interview, when it is too late. MockRoom is a place to fail first, in practice, for free.

Live: https://beta-mockroom.vercel.app

![MockRoom home page](docs/screenshot.png)

You practice with two AI interviewers, Maya and Rohan. They ask questions, push back when your answer is thin, watch your code while you write it, and score you honestly at the end.

## What you can do

- Live voice interview - 5 questions, follow-ups, scored feedback
- Technical interview - coding room with editor and test cases
- Resume interview - questions based on your own resume
- Company mode - Google, Amazon, Microsoft, Meta, Adobe, Flipkart, TCS, Infosys, Wipro
- Problem bank - 44 real interview questions at /problems
- Progress - scores, streak and weak areas at /progress, saved to your account

Easy, Mid and Hard modes. Hard gives no hints, like the real thing.

## Contribute

This project is open to contributions, and students are especially welcome.

Add a problem to the bank, fix a bug, improve the feedback, or make the UI better. Small PRs are fine. If you are new to open source, this is a good place for your first PR.

Open an issue first for big changes so we can talk it through.

## Quick start

For developers who want to run the code locally:

```bash
git clone https://github.com/krishbuilds01/MockRoom.git
cd MockRoom
npm install
npm run dev
```

Open http://localhost:3000 in Chrome. Voice input needs Chrome or Edge.

No API key is needed. The app runs fully on its local engine and browser voice.

Optional: add `GEMINI_API_KEY` in `.env.local` for Gemini replies and voice. Get a free key from https://aistudio.google.com/apikey

## Tech

Next.js, TypeScript, Tailwind CSS, Monaco Editor, Judge0 for code running, Edge TTS for voice.

Your sessions save to your account, so your progress is there on any device. Built by a student, for students.
