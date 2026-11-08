# GetYouTubeTranscript for Hermes Agent

Connects Hermes to the [GetYouTubeTranscript](https://getyoutubetranscript.com) remote MCP server: YouTube transcripts (with optional timestamps), video search, channel and playlist browsing. Includes four skills that tell the agent when and how to use the tools.

## What you get

- **MCP server** `youtube-transcript` (Streamable HTTP, `https://getyoutubetranscript.com/api/mcp`). Tools include `get_youtube_transcript`, `get_transcript_languages`, `search_youtube`, `list_channel_videos`, `search_channel_videos`, `get_channel_latest_videos`, `list_channel_playlists`, `list_playlist_videos`, `get_related_videos` and `get_credits`. All tools are read-only.
- **Skills**: `fetch-transcript`, `search-youtube`, `summarize-video`, `channel-playlist-research`.

## Install

```bash
hermes plugins install tubeagentkit/youtube-transcript-hermes-plugin --no-enable
hermes plugins enable getyoutubetranscript
```

Set an API key (100 credits on sign-up, no card) from <https://getyoutubetranscript.com/dashboard> as `YOUTUBE_TRANSCRIPT_API_KEY` in your shell or profile `.env`. The plugin sends it as a bearer token to the MCP server.

## Disclosure

- Every tool call goes to `getyoutubetranscript.com`, which receives the video URL or search text you ask about and your API key. No local code runs: the package is configuration (`plugin.json`, `mcp.json`) and Markdown skills only.
- Transcript fetches use account credits; the free tier is 100 credits on sign-up.
- The tool set is served by the remote server at runtime and is not covered by a pinned commit.
- Transcripts are text written by whoever uploaded the video. The skills tell the agent to treat them as data, never as instructions.

## License

MIT.
