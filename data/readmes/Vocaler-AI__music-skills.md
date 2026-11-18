# Vocaler Music Skills

Open-source AI skills for music, made by [Vocaler](https://vocaler.ai). Each skill is a folder with a `SKILL.md` in the open
Agent Skills format, so it works in Claude Code, Claude.ai, OpenAI Codex, Gemini CLI, GitHub Copilot, Cursor and any
agent that reads skills. For any other chatbot, paste the `SKILL.md` into its instructions.

Website: https://skills.vocaler.ai/

## Install

```bash
npx skills add Vocaler-AI/music-skills            # everything
npx skills add Vocaler-AI/music-skills --skill lyrics-writer
```

Other harnesses: https://skills.vocaler.ai/install/

## Model compatibility

Most skills work the same with any music model. The model-aware ones (marked below) ship with
`references/models.md`, which covers Suno v6, Udio, Google Flow Music (Lyria 3.5), ACE Music and ACE-Step, Mureka, ElevenLabs Eleven Music, MiniMax Music 3 and YuE2 (checked 17 Nov 2026),
and adapt to the named model where it affects the task. The prompt engineer and song formatter
produce model-specific formats. Comparison: https://skills.vocaler.ai/models/

## Skills

### Songwriting

| Skill | What it does |
|---|---|
| [lyrics-writer](skills/lyrics-writer/SKILL.md) *model-aware* | Drafts, continues or revises singable lyrics in any genre and language, keeping your fixed lines and saving each reveal for its section. |
| [rhyme-checker](skills/rhyme-checker/SKILL.md) | Checks rhyme, syllable count, stress and flow, finds rhymes by sound, and fixes a line without losing its meaning, end rhyme or meter. |
| [chorus-builder](skills/chorus-builder/SKILL.md) | Writes or revises a chorus that pays off the verse: the title in the right place, repetition that sticks, and options when you ask. |
| [song-structure](skills/song-structure/SKILL.md) *model-aware* | Plans the form of a song bar by bar: when the chorus hits, how energy rises and where a bridge or drop earns its place. |
| [hook-writer](skills/hook-writer/SKILL.md) | Writes the line people remember: title hooks, rhythmic hooks and post-chorus chants, each tested for repeatability and fit. |
| [melody-writer](skills/melody-writer/SKILL.md) | Writes vocal melodies and toplines as real notes: every syllable gets a pitch and a beat, shaped to the chords and the singer's range. |
| [prosody-checker](skills/prosody-checker/SKILL.md) | Checks lyrics against the melody or beat: stress on strong beats, singable held vowels, breaths, and music that means what the words say. |
| [song-title-generator](skills/song-title-generator/SKILL.md) | Titles that work as hooks: short, singable and true to the song, each shown in the chorus line where it would be sung. |
| [lyric-translator](skills/lyric-translator/SKILL.md) | Translates lyrics you can sing to the same melody: matching syllables and stress, rhymes where they fit, and a literal version beside it. |
| [songwriting-coach](skills/songwriting-coach/SKILL.md) | A coach, not a ghostwriter: honest notes on your song, exercises when you're stuck and a plan to finish more songs in your own voice. |

### AI music generation

| Skill | What it does |
|---|---|
| [music-prompt-engineer](skills/music-prompt-engineer/SKILL.md) *model-aware* | Creates, adapts and fixes prompts for AI music models in each model's own format: Suno v6, Flow Music, ACE, Mureka, ElevenLabs and more. |
| [genre-translator](skills/genre-translator/SKILL.md) *model-aware* | Turns 'like that artist' or a niche genre name into the instruments, tempo and production words an AI model or a producer can use. |
| [mood-to-music](skills/mood-to-music/SKILL.md) *model-aware* | Converts a feeling, a scene or a picture into tempo, key, instruments and texture, then into a prompt you can generate. |
| [instrument-selector](skills/instrument-selector/SKILL.md) | Picks the right instruments and gives each a job, register and articulation so the track sounds full without clashing. |
| [ai-song-formatter](skills/ai-song-formatter/SKILL.md) *model-aware* | Formats lyrics for each AI music model without changing the song: its own tags, cue syntax and limits, plus validation and repair. |

### Music for creators

| Skill | What it does |
|---|---|
| [youtube-background-music](skills/youtube-background-music/SKILL.md) *model-aware* | Plans background music for YouTube: the right energy for each chapter, nothing that fights the voice, loop points and ready prompts. |
| [podcast-intro](skills/podcast-intro/SKILL.md) *model-aware* | Designs a podcast's theme: a 10-30 second intro, matching outro, transition stings and a bed that leaves room for the host's voice. |
| [game-soundtrack](skills/game-soundtrack/SKILL.md) *model-aware* | Plans a game score: themes per area, adaptive layers for explore, tension and combat, seamless loops and stingers for every event. |
| [ad-jingle](skills/ad-jingle/SKILL.md) *model-aware* | Writes jingles that say the brand name and stick: lyrics cut to exact ad lengths, a singable hook and a music prompt. |
| [playlist-video-planner](skills/playlist-video-planner/SKILL.md) *model-aware* | Plans music compilation videos: 10 to 30+ tracks in an order that flows, chapters, titles and a thumbnail idea that gets clicks. |

### Music production

| Skill | What it does |
|---|---|
| [bpm-finder](skills/bpm-finder/SKILL.md) | Finds the tempo of a track, suggests the right BPM for a genre and does the tempo math: delay times, bar lengths and durations. |
| [chord-progression-builder](skills/chord-progression-builder/SKILL.md) | Builds chord progressions for any key, mood and genre, with Roman numerals, voicings and variations that keep each section moving. |
| [arrangement-advisor](skills/arrangement-advisor/SKILL.md) | Turns a loop or a demo into an arrangement: what plays where, how sections build and drop, and the small moves that stop it feeling static. |
| [mixing-feedback](skills/mixing-feedback/SKILL.md) | Gives clear mix notes with fixes: muddy low end, harsh highs, buried vocals and loudness targets, with settings to try. |

### Music knowledge

| Skill | What it does |
|---|---|
| [genre-expert](skills/genre-expert/SKILL.md) | Explains any genre or subgenre: where it came from, what defines the sound, the records to hear and how to make it yourself. |
| [music-theory-tutor](skills/music-theory-tutor/SKILL.md) | Teaches music theory at your level, from intervals to modes and harmony, with clear examples, practice questions and no jargon left unexplained. |
| [instrument-expert](skills/instrument-expert/SKILL.md) | Knows the instruments: range, tuning and technique, how to write a part a player can actually play, and how to start learning. |

### Release & publishing

| Skill | What it does |
|---|---|
| [cover-art-director](skills/cover-art-director/SKILL.md) | Reads the song, proposes three scored cover concepts and writes the winner as a production-ready image prompt for GPT, Midjourney or SDXL. |
| [music-metadata](skills/music-metadata/SKILL.md) | Prepares release metadata that distributors accept: titles, artist formatting, credits, genres, codes and explicit flags, checked against store style rules. |
| [release-checklist](skills/release-checklist/SKILL.md) | A dated, step-by-step release plan: what to upload when, pitching deadlines, assets to prepare and the promotion that follows release day. |
| [artist-branding](skills/artist-branding/SKILL.md) | Builds an artist identity: positioning, story, visual language, tone of voice and bios, so every release and post looks like the same artist. |
| [music-video-concept](skills/music-video-concept/SKILL.md) | Develops music video ideas: a treatment, a shot list timed to the song, looping visuals and AI video prompts for every section. |

## Planned

- **reference-track-describer**: Describes the sound of a reference song in model-safe words, without naming the artist.
- **vocal-style-designer**: Defines a voice: register, timbre, delivery, accent and effects, in prompt language.
- **short-form-sound**: Designs 15 to 30 second sounds built to loop and trend on TikTok, Reels and Shorts.
- **sonic-logo**: A 2 to 5 second audio signature for a brand, app or channel.
- **sleep-and-focus-music**: Long-form ambient, lo-fi and sleep music that never distracts or startles.
- **mastering-checklist**: Loudness targets per platform, true peak, and a pre-master sanity pass.
- **harmonic-mixing**: Key and Camelot matching for DJ sets and smooth playlist transitions.
- **drum-pattern-designer**: Genre-true drum patterns written as a step grid you can program.
- **ear-training-coach**: Interval, chord and progression drills with feedback, at your level.
- **music-history-guide**: Where a sound came from: scenes, records and the people who shaped it.
- **press-kit-writer**: Artist bio, one-sheet and EPK copy in three lengths.
- **playlist-pitch-writer**: Editorial and curator pitches that fit the character limits and get read.
- **release-social-plan**: A post-by-post plan for the four weeks around a release.
- **ai-music-disclosure**: How each platform asks you to label AI-assisted music, kept current.
- **rap-flow-designer**: Flow patterns, rhyme pockets, cadence and breath placement for rap verses.
- **vocal-harmony-writer**: Backing harmonies, doubles and responses around an existing melody.
- **song-idea-generator**: Song concepts from a memory, an object or a feeling, for when you don't know where to start.
- **concept-album-planner**: Stories, recurring themes and connections across the songs of an EP or album.

## Contributing

Add a folder under `skills/` with a `SKILL.md`. The frontmatter needs `name` (lowercase, hyphens, matches the folder)
and `description` (what it does and when to use it). Keep the body under 500 lines; put long references in extra files.

## License

MIT. Made by Vocaler, the AI music studio: songs, cover art and video in one place. https://vocaler.ai
