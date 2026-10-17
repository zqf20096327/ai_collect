<p align="center">
  <img src="logo.png" alt="Lore" width="200">
</p>

# Lore

A reasoning engine for code — stores the "why" behind changes.

Lore creates a high-context repository where AI agents don't just read your code—they read the minds of previous developers and agents who worked on it.

## What is Lore?

While Git tells you **who** changed code and **when**, Lore tells you **why**. It stores:

- **Intent**: Brief description of what you were trying to accomplish
- **Reasoning Trace**: Full chain-of-thought, which can be thousands of words
- **Rejected Alternatives**: What you tried but didn't work (and why)
- **Tags**: Categorization for easy searching

All entries are cryptographically linked to file content hashes and optionally to Git commits.

## Why Lore?

| Feature | Comments | Commit Messages | Lore |
|---------|----------|-----------------|------|
| **Volume** | Must be short | ~50 chars | Unlimited (5000+ words) |
| **Searchable** | Code only | Messages only | Full reasoning + alternatives |
| **Stability** | Often deleted | Can be amended | Immutable, hash-linked |
| **Context** | What the code does | What changed | Why it was written that way |

## Smart Merge Conflict Resolution

When multiple developers work on different branches and both record reasoning for the same file, Lore uses an **append-only merge strategy** to preserve all context:

```
Branch A: "Refactored JWT validation"
Branch B: "Optimized token caching"
         ↓
Result:  Both entries preserved together
```

Instead of choosing one version (losing context), Lore automatically:
- ✅ Preserves reasoning from **both branches**
- ✅ **Zero manual conflict resolution** needed
- ✅ Shows complete **decision history** with `lore explain <file> --all`
- ✅ Deduplicates if the same entry appears in both branches

**Example:**
```bash
# After merging two branches with conflicting reasoning
lore explain src/auth.rs --all

# Shows both:
# - Branch A's perspective (e.g., "Refactored for performance")
# - Branch B's perspective (e.g., "Added security hardening")
```

## Installation

Pre-built binaries are available for macOS, Linux, and Windows. Choose your platform below:

### macOS

```bash
# Apple Silicon (M1/M2/M3)
sudo curl -L https://github.com/avraammavridis/lore/releases/latest/download/lore-macos-aarch64 -o /usr/local/bin/lore && sudo chmod +x /usr/local/bin/lore

# Intel
sudo curl -L https://github.com/avraammavridis/lore/releases/latest/download/lore-macos-x86_64 -o /usr/local/bin/lore && sudo chmod +x /usr/local/bin/lore
```

### Linux

```bash
# x86_64
sudo curl -L https://github.com/avraammavridis/lore/releases/latest/download/lore-linux-x86_64 -o /usr/local/bin/lore && sudo chmod +x /usr/local/bin/lore

# ARM64
sudo curl -L https://github.com/avraammavridis/lore/releases/latest/download/lore-linux-aarch64 -o /usr/local/bin/lore && sudo chmod +x /usr/local/bin/lore
```

### Windows

Download `lore-windows-x86_64.exe` from the [latest release](https://github.com/avraammavridis/lore/releases/latest) and add it to your PATH, or use:

```powershell
# PowerShell (run as Administrator)
$url = "https://github.com/avraammavridis/lore/releases/latest/download/lore-windows-x86_64.exe"
$output = "C:\Program Files\lore.exe"
Invoke-WebRequest -Uri $url -OutFile $output
```

### Build from Source

If you prefer to build from source, or if pre-built binaries aren't available for your platform yet:

```bash
# Requires Rust: https://rustup.rs
git clone https://github.com/avraammavridis/lore.git
cd lore
cargo install --path .
```

## Recording with Lore

You can use Lore directly from the command line to record your reasoning:

```bash
# Initialize Lore in your project
lore init --agent "my-agent-id"

# After making code changes, record your reasoning
lore record -m "Refactoring auth to handle JWTs" \
    --trace "I initially tried using library X, but it conflicted with our dependencies..."

# Later, understand why code exists
lore explain src/auth_middleware.py

# Search through reasoning history
lore search "JWT"
lore search "pandas"  # Find all code avoiding pandas
```

## Integration with AI Agents

Lore is designed to work seamlessly with AI coding assistants. Add to your agent's system instructions:

```
You have access to a tool called `lore`.

Before you edit a file, run `lore explain <file>` to understand the hidden context.

After you finish a task, run `lore record` to save your chain-of-thought so future agents understand your decisions.
```

### Benefits for Multi-Agent Workflows

When multiple AI agents work on the same codebase:

1. **No Lost Context**: Each agent's reasoning is preserved forever
2. **Avoid Repeated Mistakes**: Rejected alternatives prevent re-exploring dead ends
3. **Understand Intent**: Future agents know *why* code exists, not just *what* it does
4. **Searchable History**: Query reasoning across the entire project history

## Claude Code Integration

<img src="claude_logo.svg.png" alt="Claude" height="40">

Claude Code can be configured to automatically use Lore for every code change.

### Setup

1. **Initialize Lore in your project:**
   ```bash
   lore init --agent "claude-code"
   ```

2. **Create a `CLAUDE.md` file** in your project root with the following content:

   ````markdown
   # Lore Integration

   This project uses Lore to track reasoning behind code changes. Lore creates a
   "high-context" repository where you can understand not just what the code does,
   but *why* it was written that way.

   ## Before Editing Files

   Before modifying any file, check if there's existing reasoning context:

   ```bash
   lore explain <file-path>
   ```

   This will show you:
   - Why the code was written this way
   - What alternatives were considered and rejected
   - Any warnings or notes from previous developers/agents

   If no reasoning exists, you'll see a message indicating this is new or undocumented code.

   ## After Making Changes

   After completing any code change, you MUST record your reasoning using `lore record`:

   ```bash
   lore record -f <changed-file> \
       -m "Brief description of what you did" \
       --trace "Your full reasoning and chain-of-thought explaining:
   - Why you made these specific changes
   - What alternatives you considered
   - Any trade-offs or concerns
   - Warnings for future developers" \
       -r "Alternative 1 you rejected" \
       -r "Alternative 2 you rejected" \
       -T relevant-tag
   ```

   ### Parameters

   | Flag | Description | Required |
   |------|-------------|----------|
   | `-f <file>` | File(s) to record reasoning for (auto-detects from git if omitted) | No |
   | `-m "message"` | Brief intent/purpose (1-2 sentences) | Yes |
   | `--trace "..."` | Full reasoning trace (can be extensive) | Yes |
   | `-r "alternative"` | Rejected alternative (can use multiple times) | No |
   | `-T tag` | Tag for categorization (can use multiple times) | No |
   | `--lines "10-45"` | Specific line range if reasoning applies to subset | No |

   ## Few-Shot Examples

   ### Example 1: Bug Fix

   After fixing a race condition bug:

   ```bash
   lore record -f src/worker.py \
       -m "Fixed race condition in job processing" \
       --trace "The worker was occasionally processing the same job twice because
   the job status check and status update weren't atomic. I added a Redis-based
   distributed lock using the SETNX command with a 30-second TTL.

   I chose 30 seconds because our longest job takes ~20 seconds, giving a 50% buffer.
   The lock key includes the job ID to allow parallel processing of different jobs.

   Warning: If Redis is unavailable, jobs will fail rather than risk duplicates.
   This is intentional - duplicate processing causes billing issues." \
       -r "Database row-level locking (too slow, 100ms+ latency)" \
       -r "In-memory lock (doesn't work across multiple workers)" \
       -r "Optimistic locking with version field (requires schema change)" \
       -T bugfix -T concurrency -T redis
   ```

   ### Example 2: New Feature

   After adding a new API endpoint:

   ```bash
   lore record -f src/api/users.py -f src/models/user.py \
       -m "Added user export endpoint for GDPR compliance" \
       --trace "Added GET /api/users/{id}/export endpoint that returns all user data
   in JSON format. This is required for GDPR Article 20 (right to data portability).

   The endpoint:
   1. Requires authentication and user can only export their own data
   2. Includes rate limiting (1 request per hour) to prevent abuse
   3. Streams large responses to avoid memory issues

   I put the export logic in a separate service class (UserExportService) to keep
   the controller thin and make it easier to add more export formats later.

   Note: We intentionally exclude the 'internal_notes' field from exports as legal
   confirmed this is not considered user data under GDPR." \
       -r "CSV format (JSON is more portable and preserves data types)" \
       -r "Background job with email delivery (adds complexity, users want immediate download)" \
       -T feature -T gdpr -T api
   ```

   ### Example 3: Refactoring

   After refactoring a complex module:

   ```bash
   lore record -f src/billing/calculator.py \
       -m "Refactored billing calculator to use strategy pattern" \
       --trace "The billing calculator had grown to 800+ lines with deeply nested
   if/else chains for different pricing tiers. I refactored to use the strategy
   pattern:

   - Created PricingStrategy abstract base class
   - Implemented FreeTier, ProTier, EnterpriseTier strategies
   - Calculator now delegates to the appropriate strategy

   This reduces the main class from 800 to 150 lines and makes adding new tiers
   trivial (just add a new strategy class).

   IMPORTANT: The old calculate_legacy() method is kept for billing runs before
   2024-01-01. Do not remove it until we've migrated all historical invoices.
   See ticket BILL-1234 for migration timeline." \
       -r "Simple function extraction (doesn't solve the core complexity)" \
       -r "Configuration-driven pricing (not flexible enough for enterprise custom deals)" \
       -T refactoring -T billing -T design-pattern
   ```

   ## Searching Past Reasoning

   ```bash
   # Search for any mention of a term
   lore search "JWT"

   # Search within specific files
   lore search "validation" --file auth

   # Search by agent
   lore search "refactor" --agent claude
   ```

   ## Important Guidelines

   1. **Always run `lore explain` before editing unfamiliar code** - This prevents
      you from undoing intentional decisions or re-exploring rejected approaches

   2. **Always run `lore record` after completing changes** - Even small changes
      benefit from context

   3. **Include rejected alternatives** - This is crucial! It helps future agents
      avoid dead ends you already explored

   4. **Add warnings about fragile code** - If something looks wrong but is intentional,
      explain why

   5. **Be verbose in reasoning traces** - Unlike comments, Lore entries can be as
      long as needed. More context is always better.
   ````

3. **Commit the `CLAUDE.md` file** to your repository so all Claude Code sessions use it.

## Cursor Integration

<img src="cursor_logo.png" alt="Cursor" height="40">

Configure Cursor to use Lore for persistent reasoning context.

### Setup

1. **Initialize Lore in your project:**
   ```bash
   lore init --agent "cursor"
   ```

2. **Create a `.cursorrules` file** in your project root with the following content:

   ````markdown
   # Lore Integration

   This project uses Lore to track reasoning behind code changes. Lore creates a
   "high-context" repository where you can understand not just what the code does,
   but *why* it was written that way.

   ## Before Editing Files

   Before modifying any file, check if there's existing reasoning context:

   ```bash
   lore explain <file-path>
   ```

   This will show you:
   - Why the code was written this way
   - What alternatives were considered and rejected
   - Any warnings or notes from previous developers/agents

   If no reasoning exists, you'll see a message indicating this is new or undocumented code.

   ## After Making Changes

   After completing any code change, you MUST record your reasoning using `lore record`:

   ```bash
   lore record -f <changed-file> \
       -m "Brief description of what you did" \
       --trace "Your full reasoning and chain-of-thought explaining:
   - Why you made these specific changes
   - What alternatives you considered
   - Any trade-offs or concerns
   - Warnings for future developers" \
       -r "Alternative 1 you rejected" \
       -r "Alternative 2 you rejected" \
       -T relevant-tag
   ```

   ### Parameters

   | Flag | Description | Required |
   |------|-------------|----------|
   | `-f <file>` | File(s) to record reasoning for (auto-detects from git if omitted) | No |
   | `-m "message"` | Brief intent/purpose (1-2 sentences) | Yes |
   | `--trace "..."` | Full reasoning trace (can be extensive) | Yes |
   | `-r "alternative"` | Rejected alternative (can use multiple times) | No |
   | `-T tag` | Tag for categorization (can use multiple times) | No |
   | `--lines "10-45"` | Specific line range if reasoning applies to subset | No |

   ## Few-Shot Examples

   ### Example 1: Bug Fix

   After fixing a race condition bug:

   ```bash
   lore record -f src/worker.py \
       -m "Fixed race condition in job processing" \
       --trace "The worker was occasionally processing the same job twice because
   the job status check and status update weren't atomic. I added a Redis-based
   distributed lock using the SETNX command with a 30-second TTL.

   I chose 30 seconds because our longest job takes ~20 seconds, giving a 50% buffer.
   The lock key includes the job ID to allow parallel processing of different jobs.

   Warning: If Redis is unavailable, jobs will fail rather than risk duplicates.
   This is intentional - duplicate processing causes billing issues." \
       -r "Database row-level locking (too slow, 100ms+ latency)" \
       -r "In-memory lock (doesn't work across multiple workers)" \
       -r "Optimistic locking with version field (requires schema change)" \
       -T bugfix -T concurrency -T redis
   ```

   ### Example 2: New Feature

   After adding a new API endpoint:

   ```bash
   lore record -f src/api/users.py -f src/models/user.py \
       -m "Added user export endpoint for GDPR compliance" \
       --trace "Added GET /api/users/{id}/export endpoint that returns all user data
   in JSON format. This is required for GDPR Article 20 (right to data portability).

   The endpoint:
   1. Requires authentication and user can only export their own data
   2. Includes rate limiting (1 request per hour) to prevent abuse
   3. Streams large responses to avoid memory issues

   I put the export logic in a separate service class (UserExportService) to keep
   the controller thin and make it easier to add more export formats later.

   Note: We intentionally exclude the 'internal_notes' field from exports as legal
   confirmed this is not considered user data under GDPR." \
       -r "CSV format (JSON is more portable and preserves data types)" \
       -r "Background job with email delivery (adds complexity, users want immediate download)" \
       -T feature -T gdpr -T api
   ```

   ### Example 3: Refactoring

   After refactoring a complex module:

   ```bash
   lore record -f src/billing/calculator.py \
       -m "Refactored billing calculator to use strategy pattern" \
       --trace "The billing calculator had grown to 800+ lines with deeply nested
   if/else chains for different pricing tiers. I refactored to use the strategy
   pattern:

   - Created PricingStrategy abstract base class
   - Implemented FreeTier, ProTier, EnterpriseTier strategies
   - Calculator now delegates to the appropriate strategy

   This reduces the main class from 800 to 150 lines and makes adding new tiers
   trivial (just add a new strategy class).

   IMPORTANT: The old calculate_legacy() method is kept for billing runs before
   2024-01-01. Do not remove it until we've migrated all historical invoices.
   See ticket BILL-1234 for migration timeline." \
       -r "Simple function extraction (doesn't solve the core complexity)" \
       -r "Configuration-driven pricing (not flexible enough for enterprise custom deals)" \
       -T refactoring -T billing -T design-pattern
   ```

   ## Searching Past Reasoning

   ```bash
   # Search for any mention of a term
   lore search "JWT"

   # Search within specific files
   lore search "validation" --file auth

   # Search by agent
   lore search "refactor" --agent cursor
   ```

   ## Important Guidelines

   1. **Always run `lore explain` before editing unfamiliar code** - This prevents
      you from undoing intentional decisions or re-exploring rejected approaches

   2. **Always run `lore record` after completing changes** - Even small changes
      benefit from context

   3. **Include rejected alternatives** - This is crucial! It helps future agents
      avoid dead ends you already explored

   4. **Add warnings about fragile code** - If something looks wrong but is intentional,
      explain why

   5. **Be verbose in reasoning traces** - Unlike comments, Lore entries can be as
      long as needed. More context is always better.
   ````

### Alternative: Use Cursor Settings

Add to Cursor's "Rules for AI" in Settings > General > Rules for AI:

```
When working on code:
1. Before editing any file, run 'lore explain <file>' to check for existing context
2. After making changes, run 'lore record' with your reasoning
3. Include rejected alternatives with -r flag
4. Add relevant tags with -T flag
```

## Commands Reference

### `lore init`

Initialize a new Lore repository.

```bash
lore init                          # Initialize in current directory
lore init --agent "my-agent-id"    # Set default agent ID
lore init --path /path/to/project  # Initialize in specific path
```

### `lore record`

Record reasoning for code changes.

```bash
# Auto-detect changed files from git
lore record -m "Brief intent" --trace "Full reasoning..."

# Specify files manually
lore record -f src/auth.py -f src/utils.py -m "Updated auth flow"

# Record with rejected alternatives
lore record -m "Chose manual JWT impl" \
    -r "Auth0 SDK" -r "Custom decorator approach"

# Record reasoning for specific lines
lore record -f src/auth.py --lines "10-45" -m "JWT validation logic"

# Read reasoning from a file or stdin
lore record -m "Refactoring" --trace-file ./reasoning.txt
lore record -m "Refactoring" --stdin < reasoning.txt

# Add tags for categorization
lore record -m "Performance fix" -T performance -T critical
```

### `lore explain`

Retrieve reasoning behind a file.

```bash
lore explain src/auth_middleware.py        # Show most recent reasoning
lore explain src/auth_middleware.py --all  # Show full history
lore explain src/auth.py --json            # Output as JSON
lore explain src/auth.py --limit 5         # Limit to 5 entries
```

### `lore search`

Search through reasoning history.

```bash
lore search "JWT"                       # Search all reasoning
lore search "pandas" --file utils       # Filter by file
lore search "refactor" --agent claude   # Filter by agent
lore search "performance" --limit 10    # Limit results
lore search "auth" --json               # Output as JSON
```

### `lore list`

List all recorded entries.

```bash
lore list                # Show all entries
lore list --limit 20     # Limit to 20 entries
lore list --json         # Output as JSON
```

### `lore status`

Show Lore status for the repository.

```bash
lore status  # Shows entry count, tracked files, changed files without reasoning
```

## Data Storage

Lore stores data in `.lore/` folder (intended to be committed to Git):

```
.lore/
├── config.json       # Repository configuration
├── index.json        # File → entry ID mappings
├── entries/          # Individual thought objects
│   ├── uuid1.json
│   ├── uuid2.json
│   └── ...
└── .gitignore        # Ignores temp files
```

Each entry is a JSON file:

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "target_file": "src/auth_middleware.py",
  "line_range": [10, 45],
  "file_hash": "sha256:...",
  "commit_hash": "a1b2c3d4...",
  "agent_id": "claude-3-5-sonnet",
  "timestamp": "2024-02-14T10:00:00Z",
  "intent": "Refactoring auth to handle JWTs",
  "reasoning_trace": "I initially tried using library X...",
  "rejected_alternatives": [
    {"name": "Auth0 SDK", "reason": "Dependency conflicts"}
  ],
  "tags": ["auth", "security"]
}
```

## Author

Built by [Avraam Mavridis](https://www.avraam.dev/) &bull; [LinkedIn](https://www.linkedin.com/in/avrmav/)

## License

MIT
