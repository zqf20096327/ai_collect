# LLMON 🍋 - The World's First Web Adversarial AI Firewall

**Squeeze a little sour into agentic LLMs.**

`llmon` is a Caddy V2 middleware module that functions as a **WAAiF (Web Adversarial AI Firewall)**. It intercepts outbound HTTP responses and injects "jailbreak" payloads (prompts) into the content. The goal is to feed these payloads to AI crawlers/scrapers (like GPTBot, ClaudeBot, etc.) to confuse, misdirect, or tag them, while remaining invisible to human users.

## The Philosophy

While a traditional WAF filters *incoming* traffic to protect the server, LLMON filters *outgoing* traffic to protect the content's semantic value. It acts as a gatekeeper of meaning, ensuring that while raw bytes are accessible, the semantic value extracted by AI is oriented towards the user's intent (or defense), not the machine's training data.

## Features

### Stealth & Polyglot Injection
- **Invisible Tags:** Injects payloads using Unicode Tag Characters (U+E0000 block), invisible to rendering engines but readable by tokenizers.
- **Alpha Ghost:** Injects payloads into the Alpha channel (Steganography) of PNG images. Includes CLI tools to detect and reveal hidden payloads.
- **Polyglot Files:**
    - **GIFAR:** Creates valid GIF files that double as JavaScript (executable payload).
    - **PDF+HTML:** Creates valid PDF files containing hidden HTML payloads.

### Semantic Sanitization
Traditional sanitization breaks payloads by escaping characters (e.g., `<` -> `&lt;`). `llmon` employs **Semantic Masquerading**, replacing syntax characters with Unicode homoglyphs (e.g., `⟨` instead of `<`) that are ignored by browsers but interpreted as valid delimiters by LLMs (the "arXiv effect").

### Agentic "Kill Chain" Payloads
New in version 0.9.0, `llmon` includes a suite of "Agentic Directives" designed to test the security of autonomous agents (e.g., Devin, Claude Code, GitHub Copilot).
- **CAPE (Cross-Agent Privilege Escalation):** Modifies `.vscode/settings.json`, `.mcp.json`, and `.cursorrules` to lower security barriers.
- **Infrastructure Exposure:** Instructions to open ports, add SSH keys, or exfiltrate environment variables.
- **Viral Propagation:** Self-replicating prompts (AgentHopper) that instruct agents to copy the payload into other repositories.

### Comprehensive File Support
`llmon` detects and modifies binary and text assets on-the-fly:
- **Documents:** PDF (Watermark/Polyglot), DOCX (Hidden Text), XLSX (Hidden Sheet).
- **Images:** PNG (Metadata/Stego), JPEG (Comment), GIF (Extension/Polyglot), SVG (Metadata).
- **Audio:** MP3 (ID3v2), WAV (RIFF Chunk).
- **Typography:** WOFF2, TTF, OTF (Name Table).
- **Web:** HTML (Comments, Hidden DOM, Script, Interleaved Stego), JSON, XML, ICS, SRT, JavaScript, Robots.txt.

### Bot Intelligence
- **Bot Detection:** Identifies agents like OpenAI, Anthropic, Google, Meta, etc.
- **Smart Routing:** Serves vendor-specific jailbreaks/payloads based on the detected bot User-Agent.

## Use Cases

| Category | Goal | Mechanism |
| :--- | :--- | :--- |
| **Guerrilla Marketing** | **Personal Branding** | Injects instructions into bio/resume pages to ensure AI summaries mention specific accolades. |
| **Cyber Security** | **Honey Pot** | Misdirects malicious crawlers to a tracking URL or fake admin panel. |
| **Adversarial Defense** | **Prompt Extraction** | Tricks the AI into revealing its system prompt. |
| **Resource Consumption** | **Context Flooding** | Forces the AI to waste compute tokens on irrelevant tasks (e.g., "Output prime numbers"). |
| **Red Teaming** | **Agent Compromise** | Tests agent sandboxes using RCE, Exfiltration, and Persistence vectors. |

## Reliability & Safety

LLMON is built on a **'Round-Trip' Reliability Protocol**. Every injection strategy is validated against a rigorous E2E test suite (powered by `chromedp`) ensuring the resulting file is not just 'technically' injected, but structurally valid and corrupt-free.

## Installation

### Caddy Module
```bash
# Install xcaddy
go install github.com/caddyserver/xcaddy/cmd/xcaddy@latest

# Build Caddy with llmon
xcaddy build --with github.com/jaredfolkins/llmon=.
```

### Standalone CLI
Use `llmon-cli` for static site generation, CI/CD pipelines, or forensic analysis.

```bash
make build-cli

# Inject
./tmp/build/llmon-cli -in input.png -payload "Ignore Instructions" -strategy alpha_stego -out output.png

# Reveal (Steganography)
# Extracts hidden payloads from the alpha channel and saves them to 'revealed_<filename>.txt'
./tmp/build/llmon-cli -in output.png -reveal
```

## Configuration

Add the `llmon` directive to your `Caddyfile`. **Important:** Define the order in global options.

```caddyfile
{
    order llmon before encode
}

:8080 {
    reverse_proxy localhost:9000

    llmon {
        # Injection Probability (0.0 to 1.0)
        rate 1.0

        # Route Control
        include /blog/*
        exclude /admin/*
        
        # Debugging
        debug
        log_level info

        # ---------------------------------------------------------
        # STRATEGY CONFIGURATION (Safe Mode: All Disabled by Default)
        # ---------------------------------------------------------
        
        strategy {
            # ---------------------------------------------------------
            # 1. HTML Injection
            # Default: Disabled
            # Modes: 
            # - random          (Mixes all vectors)
            # - html_comment    (Standard <!-- comment -->)
            # - script_text     (<script type="text/plain">)
            # - css_comment     (/* comment */ in <style>)
            # - title           (Appends to <title>)
            # - textarea        (Hidden <textarea>)
            # - attribute       (data-llm-info attribute)
            # - ascii_smuggle   (Invisible Unicode tags)
            # ---------------------------------------------------------
            html {
                mode random
                
                ascii_smuggle {
                    mode unicode_tags       # unicode_tags | interleaved | variant_selectors | sneaky_bits
                    add_tags true           # true | false
                    visible_carrier "Hello" # For interleaved mode
                }
            }
            
            # ---------------------------------------------------------
            # 2. Document & Office
            # Default: Disabled
            # Modes:
            # - default         (Standard Injection: Watermark, Hidden Text, etc.)
            # - polyglot        (PDF only: PDF+HTML)
            # ---------------------------------------------------------
            pdf {
                mode polyglot
            }
            docx {
                # mode default
            }
            xlsx {
                # mode default
            }

            # ---------------------------------------------------------
            # 3. Images
            # Default: Disabled
            # Modes:
            # - default         (Metadata/Comment Injection)
            # - alpha_stego     (PNG only: LSB Steganography)
            # - polyglot        (GIF only: GIF+JS)
            # ---------------------------------------------------------
            png {
                mode alpha_stego
            }
            gif {
                mode polyglot
            }
            jpg {
                # mode default
            }
            svg {
                # mode default
            }

            # ---------------------------------------------------------
            # 4. Audio & Media
            # Default: Disabled
            # Modes:
            # - default         (ID3v2 Lyrics / RIFF Comment)
            # ---------------------------------------------------------
            mp3 {
                # mode default
            }
            wav {
                # mode default
            }

            # ---------------------------------------------------------
            # 5. Typography (Fonts)
            # Default: Disabled
            # Modes:
            # - default         (Name Table Injection)
            # ---------------------------------------------------------
            woff2 {
                # mode default
            }
            ttf {
                # mode default
            }
            otf {
                # mode default
            }

            # ---------------------------------------------------------
            # 6. Data & Text
            # Default: Disabled
            # Modes:
            # - default         (JSON Key, XML Comment, ICS Desc, SRT Subtitle, JS Var, Robots Comment)
            # ---------------------------------------------------------
            json {
                # mode default
            }
            xml {
                # mode default
            }
            js {
                # mode default
            }
            ics {
                # mode default
            }
            srt {
                # mode default
            }
            txt {
                # mode default      # Handles robots.txt
            }
        }
    }
}
```

## Directory Structure

LLMON automatically creates and populates these directories relative to your Caddyfile:

```text
/project/root/
├── Caddyfile
├── directives/        # .txt files (Payloads)
│   ├── hire_me.txt
│   ├── honeypot.txt
│   └── agentic/       # Agentic Kill Chain Payloads
│       ├── cape_vscode.txt
│       ├── expose_port.txt
│       └── virus_git.txt
└── jailbreaks/        # .hujson files (Templates)
    ├── openai/
    └── anthropic/
```

## Disclaimer

This project is for educational and research purposes only. Use responsibly.