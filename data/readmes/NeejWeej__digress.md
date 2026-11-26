# <img src="docs/media/logo.svg" alt="" width="36" height="36" align="top"> Digress

**A branching chat for learning.** Highlight any words in an answer, ask about them, and the reply opens in its own thread beside the one it came from. Follow a tangent as far as you like, then come back to exactly where you were.

https://github.com/user-attachments/assets/4435b865-4ed3-46e9-b086-07de01d6515c

**[Try the demo](https://neejweej.github.io/digress/)** in your browser, nothing to install. It's the real app with a sample reading and conversation, but no model behind it: the sample's replies were written in advance, other questions get the closest passages of the document, and everything you do stays in your browser. To ask real questions, [set it up](docs/setup.md) with your Claude or ChatGPT account.


## Why branch?

Learning something hard is not a straight line. A good explanation raises three new questions, and in a normal chat each one pushes the original thread further up the screen until you lose it. You either stop asking, or you end up with one long scroll where the main idea and every side question are tangled together.

Digress keeps them apart. Every question you ask about a passage becomes a **branch** that remembers the exact words it came from. The main thread stays readable, each side question gets a full, focused answer, and the shape of the conversation shows you how the ideas connect.

![Digress in Columns view: the main thread on the left, a branch from one of its sentences, and a branch of that branch, whose takeaway has been carried back into its parent](docs/media/columns.png)

## Highlight → branch

![Selecting a phrase in an answer, typing a question, and a new branch opening beside it](docs/media/branching.gif)

Select any text in a reply and type a question (or pick a quick one: *Explain simpler*, *Example*, *Why?*, *Go deeper*, *Quiz me*). The answer opens in a new pane next to its parent.

- The model sees the whole conversation up to that point, plus the passage you picked, so the answer is about *that* sentence in *that* context.
- A numbered marker in the parent shows where each branch starts. Click it to open the branch; **Show in source** in the branch jumps back to the exact words and flashes them.
- Branches can branch again, as deep as you need. The sidebar shows the whole tree. Each pane's header says how many branches come off it; click that number for a list of just those, nested, and click one to open it.

## Takeaways: carry it back

When a branch has answered your question, press **Takeaway**. Digress writes two to four bullets of what you learned and adds them to the end of the parent thread, optionally focused on what you ask for. The main thread then builds on them, so your understanding accumulates instead of staying scattered across tangents. The branch's name in a takeaway takes you to the last reply it saw; if you keep going in the branch afterwards, a line there marks where the takeaway ends, since what's below it isn't in the takeaway.

## Fix a reply: redo, edit, other versions

Picked the wrong model, or asked the wrong thing? **Redo** asks again with the model and effort selected now, and the pencil on a question lets you **edit** it. Either way, nothing is replaced: the question is asked again in a **new branch** that starts just before it, in its own pane next to the original, so you can compare. It works the same anywhere in a thread, the last question included, and nothing that was there changes. The question shows how many versions it has. **Use this version** (in the version's pane, or on its card on the canvas) makes the conversation go on with the one you prefer; the other one becomes a branch of its own, and the toast's **Delete the old version** removes it in one click (or keep it and switch back any time). The same goes for **Retry** on a reply that ended in an error: once the conversation has gone on from it, Retry asks again as another version rather than swapping out what later answers built on (and a cut-off reply there offers no **Continue**). Branches you're done with can be hidden from the tree without deleting them.

A thread wandered off? **Move what follows into a branch** (the ⋯ under a reply) moves everything after that reply into a branch of its own, exactly as it was, and the thread goes on from that reply. The moved part opens beside it; later, a chip under the reply opens it, and the chip's delete button removes it, which is how you rewind a thread. Undo puts it back, and so does **Move back** in the moved part itself (which closes it), for as long as the thread still ends at that reply. Once the thread has gone on from there, the moved part is another version of what followed, and **Use this version** switches between them. Every version says which message it starts after.

Images in replies (and in takeaways, flashcards and the guide's answers) aren't loaded until you ask: each shows as a placeholder with what it is and the site it's from, and its button loads it. A loaded image sits in a frame like a diagram's: it fits the column and a modest height, has the same zoom strip, and a click shows it full screen. A document you're reading could tell the model to write an image whose address carries text from your conversation, and loading it would send that text to the site.

While a reply is being written you see what it's doing (searching, reading pages) and for how long. Under each reply: the model and effort it used, and what it had of the document (all of it, or which pages it started from and read).

## Read with a document

![A PDF of lecture notes on the left, a summary with page links in the middle, and a branch about one highlighted sentence on the right](docs/media/document.png)

Start from a **PDF, Markdown or text file, or a web article**: upload one, paste text, or paste a link and the server downloads it. A blog post or article opens in reader view (just the article, as Markdown, nothing on the page runs). Its images stay as placeholders until you load them. The document opens beside a main thread about the whole thing, and the model has its text, with page numbers. In a long PDF, click **Page N** in its header to jump to any page.

The model can also read the document itself. It can search it, read pages and look at a page as an image (for figures and tables), as many times as a question needs. Its search takes several wordings at once and forgives case, accents, quotes and words hyphenated across lines; when a phrase isn't there word for word, it gets the closest passages instead. A document up to about 200k characters (around 100 dense pages) is sent whole. For a longer one, the model starts from the table of contents and the first pages, then reads what the question needs. Under each reply you see what it read, with links to the pages. These tools only read the open document: nothing else on your machine.

- Highlight any passage in the PDF to branch about just that part. Markers sit in the margin of the page.
- Page references in answers, like [p. 2], are links that scroll the document there.
- The document's header lists its branches ("3 branches"), and the main thread at the top of that list: the chat about the whole document is one tap away, even with its pane closed.
- Ask about a whole page, or snip a figure, table or equation, and the model gets a sharp image of it, rendered from the PDF.
- A Markdown document or a web article works the same way: **Snip** drags a box anywhere on it (text, a table, an equation, an image) and the model gets a picture of that part, with the text in it; the branch button on an image asks about all of it, and a box inside one image is a sharp crop of that image. A remote image is downloaded once, by the server, and a copy is kept with the conversation.

Want a clean slate? **Start over** in the main thread's header empties main, so the next question starts from just the document. Nothing is lost: what was in main becomes another version of it (under Branches, with its branches and flashcards), and **Move back** brings it back (while main is still empty; after that, **Use this version** swaps them). Branches off the document itself stay where they are. For a completely separate start, **New conversation from this document** (in the document's header) opens a fresh conversation on the same file and leaves this one as it is.

You can also paste or drop screenshots into any message box: a plot from your notebook, a slide, a whiteboard photo.

## Remember it: flashcards (optional)

Turn on flashcards for a conversation and the model drafts cards from what you dug into: each highlight you branched from, each snip, each takeaway. They wait in an inbox until you keep, edit or delete them; **Make cards** drafts more from whatever changed since last time, and while it answers the model can suggest a card of its own when something has landed (`suggest_card`, see [the tools](#the-prompts-are-yours-to-change-system-prompts-skills-and-tools)). Each branch has its own **Cards** button: it drafts from what's new in the branch (showing it's at work, and saying when the cards are in), and with nothing new it opens that branch's cards, where **Draft more** asks for more on purpose. Kept cards come back for review on a spaced-repetition schedule (FSRS); review all your cards or pick one conversation (each listed with what's due). With the answer, a card shows the sentence it rests on, quoted from the conversation or the document, and **Open in conversation** (or **O**) lands on that sentence, highlighted; **Back to review** returns you to the same card. Under the answer, **Edit** (**E**) fixes a card yourself, and **Fix…** (**F**) is for when something's off: say what (or don't), and the model checks the card against the conversation and suggests a rewrite, a split into two, deleting it, or tells you why it's right after all. The suggestion waits in the inbox for you to accept or ignore, and the card sits out of review until then. **Skip** (**S**) puts a card to the back of the session without rating it. When the last card is done, a short summary says how many you reviewed, how many you recalled, how many come back soon and when the next one is due, with a link to **Activity**. Reviewing works offline too and never waits on the network: the page and your cards stay available in the browser, a rating is kept at once, and reviews sync in the background when the server is reachable again (the review shows how many are waiting). Conversations where you don't turn it on look exactly as before. How it all works: [docs/flashcards.md](docs/flashcards.md).

## Three ways to see it

Switch views from the top bar at any time; the conversation is the same.

- **Columns:** threads side by side, each pane next to the one it branched from, with a line connecting each branch to its source.
- **Rows:** the same panes stacked top to bottom, each at full width.

Drag the handle after a pane to resize it. Hold it at the edge of the window and the pane keeps growing while the panes scroll along, so even the last pane can be wider (or, in Rows, taller) than the screen. Whenever the pane reaches the width that exactly fills the window ("Fits the window"), by hand or growing, it snaps there: let go to keep that size, pull a little further or keep holding at the edge and it carries on.
- **Canvas:** the whole tree as cards on an infinite canvas. Pan, zoom, move cards, snap them to an edge or keep one stuck to the screen while you move around. Works with touch, too. Drag the background to pan and scroll to zoom; drag a card by its title to move it, or to an edge of the screen to dock it there. **Alt**+scroll over a card zooms just that card, and **Space** reads the selected card full screen.

<img src="docs/media/canvas.png" alt="The same conversation as cards on a canvas in the dark theme, one card expanded to read in place, connected by lines from each highlight to its branch" width="700">

With a document, its card's **Expand** button fills the canvas with the document itself, and dragging the card to an edge (or **Side** once expanded) docks it to that side with the canvas beside it: pages at full sharpness, and highlighting, snips, zoom and page jumps work as in Columns. Following a branch marker from the expanded document moves it to the side, to make room for the branch's card. **Canvas views** save an arrangement of the canvas under a name (the **Views** button in its corner), so you can switch between setups and open the same one on another device. Without them, each device keeps its own canvas and pane layout, since what fits on a laptop doesn't fit on a phone.

Answers render Markdown, code with syntax highlighting, LaTeX math and Mermaid diagrams. A tall diagram fits in about 60% of the window's height, whole. One too small to read has a zoom button under it: **+ / − / Fit** and four arrows (hold one to keep going), right there in the chat; once zoomed in, you can also drag it around. Scrolling over a diagram still scrolls the conversation. On a phone or tablet, pinch to zoom the page instead. Panes collapse to thin strips, **Collapse others** (in a pane's header) folds every other pane away and again (or <kbd>Esc</kbd>) brings them back, and each pane keeps its own zoom. A pane keeps a width you drag it to, but when it's the only one left open it fills the space (your width comes back when you open another). **Zen** (<kbd>⌘.</kbd> / <kbd>Ctrl+.</kbd>) hides the top bar and sidebar too, for reading a paper with nothing else on screen; branching works as usual, and <kbd>⌘B</kbd> / <kbd>Ctrl+B</kbd> (or the tab at the left edge) still brings the sidebar out over the panes. Collapsed strips can be dragged to reorder them, like the grip on an open pane; on a touch screen, a long press anywhere on a pane's header picks it up too. Ask in a branch, then minimize it (or fold its card on the canvas, or close it) and keep reading: while the reply is written its strip, card and row in the sidebar show three dots, and once it's done they say **Ready** until you open it. Any pane can be closed, main and the document included; their rows at the top of Branches in the sidebar bring them back. In a long document, the ribbon button in its corner marks where you got up to (no chat attached); it syncs with the conversation, and opening it again offers to take you back. Drag the ribbon to move it. Under each reply, a quiet line says how full the model's context was when it answered and how much came from the prompt cache ("52k / 1M context · 75% cached"), from the provider's own count; click or tap it for the breakdown: input (from the cache and new), output, how many requests it took, how full the window was and—when the provider has a known cache window (Claude's 5-minute or 1-hour ephemeral cache)—until what local time it stays warm. On a narrow window or a phone, whatever doesn't fit in the top bar moves into a ⋯ menu; a narrow pane puts its buttons on a second row rather than hiding any (zoom included). The palette button, **Appearance**, switches themes: light and dark (or match your device), four retro-futurist ones (**Atompunk**, space-age navy with atomic orange; **Columbia**, a gilded world's fair in cerulean and brass; **Solarpunk** dark and light, emerald and amber), night ones with no blue in them, so they still look right under a blue-light filter like f.lux (**Rainforest Night**, a lush, warm green that isn't black; **Canopy**, the deep jungle with fireflies; **Lost City**, a jungle temple by torchlight; **Speakeasy**, oxblood, whiskey and brass; **Phosphor**, an amber terminal), soft light ones for late at night, dimmer than paper (**Rainforest Day**, bright leaf green in dappled sun; **Map Room**, an old expedition map; **Greenhouse**, sage and moss; **Reading Room**, a library by lamplight); these and Columbia also dress the page around the panes (a sky with clouds, scanlines, fireflies, book spines, a map grid) and their edges, plus Sand, Sea glass, Rosé Pine (Dawn and the original), Everforest Dark, Catppuccin Latte and Mocha, Kanagawa (Wave and Lotus), Gruvbox Dark, Shades of Purple, Nord, GitHub (light and dark), E-ink (black on white) and Pure black (for OLED screens). The menu has foldable **Light**, **Dark** and **PDF pages** sections (the one with your current theme opens; folded ones show a dot per choice) and scrolls on a small screen. Under **PDF pages**, PDFs can stay as printed or turn **Dark** (light text on dark pages; photos look like negatives), **Dim** or **Sepia**, or **Match the theme** (the page takes the theme's own paper: inverted and tinted to the theme with a dark one, the theme's warm or cool paper behind the ink with a light one). It only changes how pages look to you: what the model gets from a page is the original. **Font** changes the conversation's type (the replies, your messages, documents and quoted passages, and the titles in the sidebar; the buttons and headings stay as they are): Default (serif replies, sans for your messages), Sans, Serif, Mono or your device's own, **Literata**, **Newsreader** or **Fraunces** (book serifs), **IBM Plex** (its serif), **Jost**, **Space Grotesk** or **Source Sans**, or one made for easier reading: **Lexend**, **Atkinson Hyperlegible**, **Inclusive Sans** or **Comic Neue** (the last often suggested for dyslexia). Below them, **Lines between panes** turns off the lines from each branch to where it came from in Columns and Rows (they stay in Zen unless you do; the canvas keeps its own), and **Fit to this screen** undoes the pane widths and zoom levels in the open conversation. Each device keeps its own layout of a conversation; opening one on a new device (a phone after the desktop) takes the other device's open panes, view and canvas arrangement, but not its pane widths, zoom levels or docked cards, so it fits the smaller screen.

**Activity** (in the sidebar, under Review) is a page about your own learning, worked out from what's already saved (nothing new is recorded):

- **A grid of days** since you started (up to a year), shaded by how much you did: questions, branches and flashcard reviews, or just one kind. Click a day to see its conversations.
- **What you remember:**
  - about how many of your cards you'd recall right now (FSRS's estimate), and how that has grown;
  - how often you recalled cards over the last 30 days;
  - what's coming due in the next two weeks;
  - the cards you keep missing.
- **Rabbit holes:**
  - your deepest chain of branches, step by step;
  - your most branched conversations;
  - the passages you branched from more than once.

Click any of them to go there.

Not sure how something works? The **?** beside *How it works* in the sidebar opens **Ask about Digress**: a chat that has this README and the rest of Digress's documentation, using the model you picked. It is never saved.

## Search everything

<kbd>⌘K</kbd> / <kbd>Ctrl+K</kbd> searches every conversation at once: questions, answers, highlights, takeaways and documents. It is a full-text index (BM25) that tolerates typos and takes you to the words it found, highlighted, inside the message or document page. A **Back** chip then returns you to where you were, even in another conversation. Press <kbd>Tab</kbd> in the search box to look only in this conversation or only in one thread, or click the magnifier at the bottom right of a pane to search just that thread. Half remember something but not the words? Choose **Describe it instead** under the results: the model suggests the words you probably used (it gets what you typed and your conversations' titles, never their text), and if that isn't enough you can let it pick from short snippets of the best matches. Since it's the one thing that reaches across conversations, it has its own model, shown in its row ("Asks: Haiku 5.5 ▾") and changed there; by default it's the quick model, never a Gemini one. Pin the conversations and branches you keep coming back to, and archive the rest. To group conversations, put them in **folders**: **Folders** in the sidebar folds like the other sections; its **New folder** asks for a name and which conversations go in it, and the folder button on a row (**Move to…**) moves that one into a folder, out of one, or to the archive. Filed conversations stay in **Conversations** too (newest first, with the folder's name beside the title), so picking up where you left off works the same; a folder just gathers a topic in one place. A folder can also give its new chats a starting system prompt (the sliders button on its row): **+** on a folder's row starts a chat there with a copy of it, so a folder can be for tinkering, work or anything else with its own voice, not just learning. Editing a folder's prompt never changes a conversation already in it, and moving one in asks whether to switch to the folder's prompt (keeping its own is the default). Each folder folds on its own (one folder per conversation, no folders inside folders). Rename or remove a folder from its row; removing one puts its conversations back in the list and deletes nothing. **Pinned**, **Folders**, **Conversations** and **Branches** fold from their headings, and a long list scrolls inside itself, so Branches and *How it works* stay in reach. Deleting a conversation moves it to **Trash** at the bottom of the sidebar, on every device: restore it within 7 days, or it's deleted for good then (or right away with **Delete for good**). Its document goes with it only if no other conversation uses that file (moving it to Trash and **Delete for good** both say which it is, by name), and its flashcards stay in your review unless you tick **Also delete its flashcards** when you move it to the trash (the dialog lists them, folded away). Ticked, they leave review at once and come back if you restore it; it's asked once, and Delete for good or the 7-day cleanup does what you chose. Deleting a branch offers the same for its cards. A card whose conversation is in the trash says so in review, with **Restore**, and one whose source was deleted says it can't take you back any more. Two conversations with the same name show the day each started. Once you have a document conversation, **All · Docs · Chats** above the list shows just one kind. Double-click a title in the sidebar to rename it. A new conversation you leave empty isn't kept: **Delete**, or ✕ on its pane, just puts it away and opens your latest one. A reply that finishes while you're in another tab puts a dot in front of the tab's name until you come back. A conversation or branch is named by its first question; when that question is long or vague, a fast model (Haiku for Claude conversations, Terra for ChatGPT ones) gives it a short title once the first reply is in. A title you set yourself is never replaced. Which model each of these calls uses (replies, flashcards, titles, search) is in [Setting it up](docs/setup.md#which-model-does-what).

## Keyboard shortcuts

⌘ on a Mac, Ctrl elsewhere. In Digress, press <kbd>?</kbd> (or **Keyboard shortcuts** under *How it works* in the sidebar) for this list in a small panel in the corner. It covers nothing else, so you can keep working with it open: each key you press lights up its row, a filter at the top narrows the list, and ⇆ moves it to the other corner. <kbd>?</kbd> again, <kbd>Esc</kbd> or ✕ closes it; on a phone it's a sheet at the bottom that you swipe away.

| Keys | What it does |
| --- | --- |
| <kbd>⌘K</kbd> | Search (in search: <kbd>↑</kbd> <kbd>↓</kbd> <kbd>Enter</kbd> open a result, <kbd>⌘Enter</kbd> opens it and keeps searching, <kbd>Tab</kbd> switches everywhere / this conversation / this pane) |
| <kbd>⌘B</kbd> | Show or hide the sidebar (in Zen too, over the panes) |
| <kbd>⌘.</kbd> | Zen |
| <kbd>⌘'</kbd> | Canvas, or back to the panes (Columns or Rows, whichever you had) |
| <kbd>⌘⇧'</kbd> | Switch Columns and Rows |
| <kbd>⌘\\</kbd> | Collapse the pane you're in to a strip, or expand it again (on the canvas: expand or shrink the selected card) |
| <kbd>⌘⇧\\</kbd> | Close the pane you're in; the toast's **Undo** brings it back |
| <kbd>Enter</kbd> / <kbd>⇧Enter</kbd> | Send / a new line |
| <kbd>Esc</kbd> | Close the question box; expand the panes **Collapse others** folded |
| <kbd>?</kbd> | Show or hide the keyboard shortcuts (not while typing) |
| <kbd>Space</kbd> | On the canvas: read the selected card full screen (again or <kbd>Esc</kbd>: back) |
| <kbd>⌘⌥←</kbd> <kbd>⌘⌥→</kbd> <kbd>⌘⌥↑</kbd> <kbd>⌘⌥↓</kbd> | On the canvas: dock the selected card left, right, full screen; undock it |
| <kbd>⌥</kbd> scroll | On the canvas: zoom one card |
| <kbd>Space</kbd> / <kbd>1</kbd> <kbd>2</kbd> <kbd>3</kbd> <kbd>4</kbd> / <kbd>S</kbd> / <kbd>O</kbd> / <kbd>E</kbd> / <kbd>F</kbd> | Reviewing flashcards: show the answer / rate it (Again, Hard, Good, Easy) / skip it / open where it came from / edit it / Fix… |
| <kbd>⌘</kbd> click | A conversation in the sidebar: open it in a new window |

On an iPad, iPadOS keeps <kbd>⌘.</kbd> for itself, so Zen is <kbd>⌃.</kbd> (Ctrl+.) there; Ctrl works in place of ⌘ for every shortcut. The ⌘ shortcuts work while you're typing. "The pane you're in" is the one you last clicked, typed in or scrolled; with more than one pane open, it has a faint outline.

## Models: Claude and ChatGPT, on the plans you already pay for

Digress needs no API key if you already have a subscription.

- **ChatGPT, with your ChatGPT plan (Plus or Pro).** Run `npm run chatgpt -- login` once and sign in with your ChatGPT account. Digress uses OpenAI's *Sign in with ChatGPT* for open-source apps: it registers as its own app, calls the Responses API with `store: false`, and usage counts against your plan. Your plan's models appear in the model picker.
- **Claude, with your Claude subscription (Pro or Max).** If the [Claude Code](https://docs.claude.com/en/docs/claude-code) CLI is installed and signed in, Digress runs it for each reply with all of its own tools turned off and none of your Claude Code setup loaded (only web search when you ask, and the document tools above), so it answers on your plan.
- **Claude, with an Anthropic API key.** Put `ANTHROPIC_API_KEY` in `.env` and Digress calls the API directly, with prompt caching for long documents.

- **Google Gemini, with an API key.** Add the key in the app (model picker → **Connections…**) or as `GEMINI_API_KEY` in `.env`. Keys added in the app stay on your server and are never shown again, only "key ending …1234". On a **free-tier** key, Google may use what you send to improve its products and people may read it, so don't send anything sensitive; Gemini only gets the conversations you pick it in. Details: [Setting it up](docs/setup.md#google-gemini-with-an-api-key).

Claude, ChatGPT and Gemini can be connected at the same time; **Connections…** at the bottom of the model picker shows which are on, and is where an Anthropic or Gemini key can be added or removed. The model picker groups the models under **Anthropic**, **OpenAI** and **Google**, each folding away (the group of the model you're using opens, so a long list stays out of the way). In each, the newest of every kind shows, and earlier versions wait under **Older**. It follows the pane you're in (on the canvas, the selected card): each branch keeps its own model and effort, a new branch starts with the model of the one it came from, and changing the picker changes only the thread you're in. A branch's first question fixes its model, so switching its parent later doesn't change it. Each reply shows which model wrote it. A model that isn't available here (another provider, or one that's been retired) is replaced by the newest of the same kind (another Opus, another GPT Sol), else by the same family, and Digress says so; the branch remembers its own and goes back to it once it's available.

## Web search, only when you ask

Models answer from what they know unless you turn on **Web** in the top bar. Then they may search the web, link the pages they use right in the answer, and the reply lists its sources. It is search only: the search runs on Anthropic's or OpenAI's side, and the model gets no tool that fetches pages or runs anything on your machine. With Claude Code and ChatGPT, switching Web on or off doesn't make the model reread the whole conversation: the tools it's offered stay the same and only whether search may run changes, so the provider's prompt cache keeps working (each question asked with Web on is marked as such).

## The prompts are yours to change: system prompts, skills and tools

**Prompts, skills & tools** (the sliders button beside Activity in the sidebar) shows what Digress tells the model and what it lets the model do. There you can:

- **Rewrite your default system prompt**: who the tutor is and how it writes, sent before every question. Your version applies to every conversation that doesn't have its own, on every device, from the next reply. **Reset to default** brings back the built-in one. After it Digress always adds a fixed part, **how Digress works** (shown there, read-only): the formatting the page can draw, when the model may search the web, how branches are marked and what the model sees. It's kept separate so that a prompt you write can't drop something the app depends on.
- **Give one conversation its own system prompt.** A new conversation's empty main thread shows the prompt it will start with (**System prompt: your default**), filled in with your default: open it, change it and **Use for this conversation** before the first question. Later, **Prompt** in the top bar shows and changes it (its menu has the prompt, your skills, and **What the model sees here…**); **Put my default back** returns it to following your default. It's one prompt for the whole conversation: main and every branch use it. In a conversation about a document, that includes branches from the document, so setting it in the empty main thread is how you set it for them, even if you never ask anything in main (the box says so). A change applies from the next reply in every thread of that conversation; replies already written keep what they were written with. The top bar's button says **Own prompt** while a conversation has one.
- **Change the quick questions**: the chips such as *Explain simpler* and *Example* in the highlight popup and in a new branch.
- **Add skills**: sets of instructions in the `SKILL.md` format many AI tools share. Paste one, choose the file, or give a link (a GitHub link to a skill's folder or its `SKILL.md` works).
- **See the tools** the model can use and what turns each on, with the descriptions the model reads folded away (read-only).

Turning a skill on applies to one conversation: use **Prompt** in the top bar, which lists your skills and names the ones that are on. The skill is added to the end of that conversation's system prompt and applies from the next reply in every thread, branches included. Other conversations aren't affected. Flashcard drafting and takeaways are told to ignore it. A deleted skill drops out of the conversations that had it on.

The tools:

- **Web search**: only when **Web** is on in the top bar, question by question. It's the one tool that reaches outside (your question's words go to a search engine, and the answer can rest on pages nobody checked), so it's yours to switch. The provider runs it (Claude's, OpenAI's or Google's own search).
- **Reading the document** (`search`, `read_pages`, `view_page`): always, in a conversation about a document. They only read what you opened, in your browser, so there's nothing to switch. With a long document the model starts from its contents and first pages and reads the rest with these.
- **Suggesting flashcards** (`suggest_card`): in a conversation with flashcards on. While it answers, the model can add a card whenever it judges something has landed (not on a schedule); each goes to your inbox, and a toast says so. With flashcards off it isn't offered.

### What the model sees

Each reply is sent one path through the conversation, and nothing else:

- **In the main thread:** the main thread so far.
- **In a side branch:** the main thread up to the reply (or passage) it branched from, then the branch. A branch of a branch adds its own branch on top. A branch from the document starts fresh: the document and the branch.
- **Where a branch forks**, its first question starts with a marker, *[Side question about …]*, quoting what you highlighted. The fixed part of the prompt tells the model that everything after a marker is in that branch, so later questions don't need one.
- **Not sent:** your other branches, what happened in the main thread after a branch forked, and anything on screen such as thread names. A takeaway is the one thing that carries a branch's result back. The model is told this, and to say so and ask when you mention something it can't see, rather than guess.
- **Branches made by moving messages** (a reply's ⋯ → Move what follows into a branch) have no fork marker: those questions were asked in the main thread, and what the model saw for them never changes. Moving messages, **Use this version** and **Move back** never change what any message was sent, so they don't cost the prompt cache either.

To check, **Prompt** in the top bar → **What the model sees here…** shows the request the next question in the thread you're in would send: the tools, the system prompt part by part, and every message with its markers (**Copy as JSON** for the raw request).

Everything else Digress tells the model (how branches, takeaways and flashcards are asked for, how documents are introduced) is shown there read-only. The code relies on its wording, so it's changed in one file, [`web/prompts.js`](web/prompts.js): edit it and reload.

## On several devices

Open it from your laptop and your phone (see [Using it from other devices](docs/remote-access.md)) and they stay in step. Switch back to a tab and it picks up whatever you did elsewhere, without a reload; the layout stays as it was on that device. If both changed the same conversation, the two are combined and nothing is lost: when both asked from the same point, the later question becomes another version.

On a shaky connection nothing is quietly lost: a change that couldn't be saved says so in the top bar and is tried again until it goes through (at once when the connection is back), leaving that conversation or closing the tab asks first, and switching tabs or locking the screen saves straight away.

A reply keeps going on the server when your phone locks, you switch apps or conversations, or the page reloads, and the page picks it back up when you return. If nothing comes back for 10 minutes it stops, keeps what it wrote, and offers **Continue**.

## Export, share, import

The ⤓ button on a conversation's row in the sidebar exports it:

- **A Digress file** (`.digress`): the whole conversation, every branch, highlight, takeaway and pasted image, in one compressed file. Tick the boxes to include the document (without it, whoever opens the file attaches their own copy) and the flashcards (they arrive in the inbox, without your review history). Your layout, pins and reading mark stay with you.
- **Markdown** (`.md`), to read in another app: each branch is a section, under the passage it came from, with takeaways quoted.
- **Flashcards for Anki** (`.csv`): your kept cards, with the sentence each came from and a tag for the conversation. In Anki: File → Import.

To open a `.digress` file, choose it in **New from a document** (or drop it anywhere on the page). It becomes a new conversation next to your own, with new ids, so opening the same file twice is fine. Each branch continues with the model it used, or the closest one you have. The file is made and read in your browser; nothing is uploaded anywhere. The [demo site](https://neejweej.github.io/digress/) opens `.digress` files too, so someone without Digress can read what you shared: it stays in that browser only, and deleting it from the sidebar removes it.

## Your data stays on your machine

Digress is one HTML file (`web/index.html`) and a small Node server with no dependencies (`server/server.mjs`). Conversations and documents are plain JSON and files in `data/`; the only thing that leaves your machine is what you send to the model you picked. The server listens on `127.0.0.1`, has no accounts, and refuses requests from other websites.

## Quick start

Needs Node 18 or newer, plus at least one model connection from above.

```sh
git clone https://github.com/NeejWeej/digress && cd digress

# connect a model (any or all):
npm run chatgpt -- login         # ChatGPT, with your ChatGPT plan
claude                           # Claude Code, signed in with your Claude plan (then /exit)
echo 'ANTHROPIC_API_KEY=sk-ant-...' >> .env   # or an Anthropic API key

npm start                        # → http://127.0.0.1:8787
```

Open <http://127.0.0.1:8787>, click **New conversation** or **New from a document**, and ask something.

## More

- [Setup and configuration](docs/setup.md): each model connection in detail, `.env` options, documents from links, where data lives.
- [Using it from other devices](docs/remote-access.md): Tailscale, running it as a service, using it on your phone.
- [Development](docs/development.md): tests, live reload, regenerating these screenshots. [AGENTS.md](AGENTS.md) explains how the code fits together.
- [Future directions](docs/future.md): ideas for later, like sub-agents that explore and codebases as a source.
- [Flashcards](docs/flashcards.md): turning them on, where cards come from, the inbox, reviewing, offline.
- [Done](docs/done.md): ideas from that list that have been built.

## License

MIT

Developed with Claude Opus 5.5.
