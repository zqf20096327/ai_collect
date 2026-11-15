# LinkedIn Comment Assistant

A Chrome extension that drafts short comments from LinkedIn post text using the Groq API. It inserts a draft into the comment box; review and post it yourself.

## Setup

1. Load this folder as an unpacked extension in Chrome, or reload it on `chrome://extensions` if already installed.
2. Open the extension popup and save your Groq API key. The key is stored in Chrome extension local storage.
3. Refresh LinkedIn and click a post’s Comment button. The post text is sent to Groq to generate a draft. The extension also Likes an unreacted post when the comment flow starts and attempts to tag the author.

Drafts are generated from the visible post text and may be inaccurate. Check each one before posting. The extension also keeps a local log of recent generation attempts in extension storage.
