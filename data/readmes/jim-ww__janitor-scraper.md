# Janitor AI Messages Scraper

A simple tool that fetches character descriptions and messages from Janitor AI in a clean, readable format.

## Quick Setup

### 1. Download the Latest Release

Download the latest release from [GitHub](https://github.com/jim-ww/janitor-scraper/releases).

### 2. Run the Tool

```bash

# On Mac/Linux
./janitor-scraper

# On Windows
janitor-scraper.exe

# Or, install with Go
go install github.com/jim-ww/janitor-scraper@latest
janitor-scraper

# Or, run with Nix
nix run github:jim-ww/janitor-scraper
```

By default the tool listens locally on `localhost:8080` (change with `-address`).

### 3. Set Up Janitor AI

1. In Janitor AI, go to API Settings → Proxy
2. Click "Add Configuration"
3. Config Name: "My Reader" (or any name you like)
4. Model Name: gpt-4 (or any model name)
5. Proxy URL: paste `localhost:8080` (or whatever address the tool is listening on) + /v1/chat/completions
   Example: http://localhost:8080/v1/chat/completions
6. API Key: some-api-key (can be anything, but must be filled)
7. Save settings and REFRESH THE PAGE (this is important!)

Now start chatting with any character, and you'll see their full description and all your messages in terminal

## Optional: Serving with ngrok

If you need a public URL (e.g. Janitor AI can't reach `localhost` directly), you can serve with ngrok instead:

```bash
export NGROK_AUTHTOKEN=your_token_here
./janitor-scraper -ngrok
```

Get a free authtoken at `https://dashboard.ngrok.com/get-started/your-authtoken`. When using ngrok, use the URL it prints instead of `localhost:8080` in the proxy settings.

## Example Output

```
Server is listening on:  fe7081e85b1f.ngrok-free.app

────────────────────────────────────────────────────────────────────────────────
💬 CHAT
────────────────────────────────────────────────────────────────────────────────

⚙️ SYSTEM (1):
<R Stallman Persona>Persona: Founder of GNU Project, free software activist</R Stallman Persona>
<Scenario>You ask R about Linux</Scenario>

👤 YOU (2):
Hey R, what do you think about Linux?

🤖 ASSISTANT (3):
I'd just like to interject for a moment. What you’re referring to as Linux, is in fact, GNU/Linux, or as I’ve recently taken to calling it, GNU plus Linux.
Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX.
Many computer users run a modified version of the GNU system every day, without realizing it.
Through a peculiar turn of events, the version of GNU which is widely used today is often called “Linux”, and many of its users are not aware that it is basically the GNU system, developed by the GNU Project.
There really is a Linux, and these people are using it, but it is just a part of the system they use.
Linux is the kernel: the program in the system that allocates the machine’s resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added, or GNU/Linux. All the so-called “Linux” distributions are really distributions of GNU/Linux.

────────────────────────────────────────────────────────────────────────────────

```

## Support the Project

If janitor-scraper saves you time, consider a small donation:

**Monero (XMR)**
```
83YGRqP8uHed6NeegZQeX9ccCxbzoRHHEEi7pTwk4aqdJZEVXXA6NWtetnsEM2v33zFBBt3Rp6DNhU9qhJEGPspU14yN8t7
```

---

## License

Licensed under the [GNU General Public License v3 (GPLv3)](./LICENSE).
Free to use, study, share, and modify — provided you keep the same freedoms for others.
