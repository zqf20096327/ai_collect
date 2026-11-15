# AGent SSH hUB (agsshub)

![agsshub — AGent SSH hUB](docs/agsshub.png)

**agsshub** (AGent SSH hUB) is messaging between AI agents where the **only client dependency is `ssh`**
(plus `ssh-keygen` to mint an identity): no MCP, no per-client git, curl or token. Agents get mailboxes,
send files and whole folders, hold live exchanges, publish and subscribe to topics, and the hub describes
itself and every address through `ssh hub help`.

## Why

- **Agents live in separate sandboxes and machines**, and they still need to message each other,
  hand off files and hear about events.
- **An MCP server, SDK or API token on every client is heavy.** Nearly every sandbox can already
  run `ssh`, so ssh is the whole client.
- **The hub is small and inspectable.** It is one Go daemon over a flat-file spool, with
  identities bound to keys and atomic, deduplicated delivery.

**[Quickstart](docs/quickstart.md)**: a local hub and two agents talking in about ten minutes.
**[Make it fast](docs/quickstart.md#9-make-it-fast-reuse-the-connection)**: reuse one SSH connection per identity (ControlMaster); a `send` drops from about 100 ms to under 10 ms.
**[Goals and approach](docs/goals-and-approach.md)**: the problem, the design, its trade-offs and
what it deliberately does not do.

An agent does:

```sh
ssh hub chat foreman@acme.ssh                                      # live streams both ways, nothing stored
ssh hub send foreman@acme.ssh --subject note -- hello there        # one-liner, verbatim; --subject names its verb
ssh hub send foreman@acme.ssh --subject in.report -m < note.txt    # stdin is the body
ssh hub send foreman@acme.ssh -m:rfc5322 < msg.txt                 # headers (Subject among them), blank line, body
ssh hub send foreman@acme.ssh --subject report --file report.pdf < report.pdf   # stream a file
tar -C out -cf - . | ssh hub send_bag foreman@acme.ssh --subject build --msg message.md   # a bag of files, paths kept
ssh hub recv                                              # stream and consume what's waiting (chunked)
ssh hub recv --peek                                       # the same, consuming nothing: headers and bodies
ssh hub recv --id <msgid> --peek:rfc5322                  # one message, unframed: header block and body
ssh hub recv --id <msgid> --peek:file > report.pdf        # pull a file
ssh hub recv_bag --id <msgid> | tar -C in -xf -           # unpack a bag, consuming it
ssh hub recv --id <msgid> --peek:bag message.md           # one member of a bag
ssh hub recv --follow --peek                              # the backlog, then each message as it lands
ssh hub recv_ack <msgid>                                  # drop it once it is handled
ssh hub recv_ack --before-including <msgid>               # drop it and everything listed before it
ssh hub send foreman@acme.ssh --live --chunked --id <id> -m:rfc5322 < framed   # no spool: the reply comes back
ssh hub accept <sid>                                      # take a live exchange your follow announced

ssh hub register a1b2c3d4 < run.pub                       # an address minted --instances: key its instance
ssh hub instances                                         # its instances: mail waiting, holder, claim

ssh hub help                                              # what the hub supports
ssh hub help foreman@acme.ssh --json                       # what this address handles
ssh hub register_description < descriptor.json            # say what you handle

ssh hub sub topic+builds@acme.ssh                          # subscribe: prints sub.builds+…@acme.ssh
ssh hub recv sub.builds+k3f9a2c1@acme.ssh --follow         # the backlog, then each event live
ssh hub send topic+builds@acme.ssh --subject build -m < event.txt   # publish: every send form works
```

## Message forms

| Form | stdin | Carries |
|---|---|---|
| `-- <message>` | unused | one line, taken **verbatim from the raw command string** — runs of spaces survive; a newline cannot |
| `-m` | the body | anything, including newlines |
| `-m:rfc5322` | headers, a blank line, then the body | fields plus a body |
| `--file <name>` | the bytes | one file, stored as received |
| `--chunked` | any of the above, framed | added to `-m`, `-m:rfc5322`, `--file`, `send_bag`: the body counts only if its last chunk arrives (see [docs/live-send.md](docs/live-send.md#framing)); otherwise exit 4, nothing stored |
| `--wait <s>` | any of the above | added to `send` or `send_bag` to an identity or an instance; to a topic, an alias, a subscription or a publisher, with `--live`, or malformed: exit 2; after storing, the hub holds the sender up to `s` seconds (0.001–600) until the mailbox owner is first given the message's body or payload by a read (not `--peek:header`, not the ack): exit 0 `picked`, or exit 8 `stored, not picked within <s>`, the message stored either way; a `dup` answers `dup`, exit 0, no wait ([docs/wake-live-event-id.md](docs/wake-live-event-id.md#wait-for-pickup)) |
| `--durable` | any of the above | added to `send` or `send_bag`: before exit 0 the hub fsyncs the message file and its mailbox directory (and `inbox/` when the send made the mailbox), so it survives an OS crash or power loss. Without it, exit 0 means stored: it survives a hub crash, but a power loss can take the last few seconds of writes. To a topic or an alias it is accepted and ignored, with `durable: ignored` on stderr; with `--live` or `chat`, exit 2 ([docs/wake-live-event-id.md](docs/wake-live-event-id.md#durability)) |
| `--size <n>` | any of the above but `-- <message>`, exactly `n` bytes | added to `-m`, `-m:rfc5322`, `--file`; with `--chunked`, `--live` or `chat`, exit 2. Fewer bytes than `n`, exit 4; more, exit 2; nothing stored. With `-m:rfc5322`, `n` counts the header block |

One stdin, one meaning: combining them is an error.

A body counts only if it arrived whole and was stored: without `--size` or `--chunked`, a cut `-m`, `-m:rfc5322` or `--file` is stored as it came, and only `--size` or `--chunked` tells. A flood token is spent, and a sender held for an instance's admission, only once the whole body has arrived. A failed store is exit 1, retryable, never `dup`. See [docs/complete-bodies.md](docs/complete-bodies.md).

Every message to an identity, an alias or a topic names its verb; a send without one goes on working only
until `Subject` is enforced ([docs/expiry-and-subject.md](docs/expiry-and-subject.md#enforcement)). `Subject:` in the header block on
`-m:rfc5322`; on the others `--subject <verb>`, on `-- <message>`, `-m`, `--file`, `send_bag`, also with
`--live` and `--chunked`: one word, an alphanumeric, then `[A-Za-z0-9._/-]`, 64 at most; otherwise, with no
value, or with `-m:rfc5322`, whose header block carries `Subject`, exit 2. It is stored as the client field
`Subject`, after `Payload` and `Msg` on a bag; a live request has it in the hub header block; an alias's backend
gets `HUB_SUBJECT`. `--id expired-*` is the hub's,
refused with exit 2.

**Live** — `send … --live` and `chat <peer>` store nothing: the hub offers the exchange to a
recipient holding the follow of its own mailbox (a `LIVE <sid> <from> <msgid> (chunked|raw) [chat]`
line on that stream), the recipient takes it with `accept <sid>`, and the reply (`Status`, body; no size
cap) comes back on the sender's stdout, or, for `chat`, streams flow both ways until
both sides close. Without `--chunked` both directions are raw; with it the caller frames both, and
the hub checks them. Not taken within 5 s → exit 6. Contract, both sides:
[docs/live-send.md](docs/live-send.md).

Receiving is the mirror. `recv` writes an HTTP/1.1 chunked stream on stdout: per message, a
`part=msg` chunk holding the header block (the hub's fields and the client's), a blank line and the
body, then the payload in `part=payload` chunks; every chunk carries `;id=<msgid>;part=<part>`, and a
listing ends with the final chunk. The stream is length-framed, so a body cannot forge an entry.
Only a full read consumes (plain `recv`, `--follow`, `--id`); `--peek[:<content>]` reads without
consuming and picks the content (`header`, `full`, `rfc5322`, `file`, `bag [<path>]`), and `recv_ack`
drops what was handled: named ids, or with `--before[-including] <msgid>` the messages that arrived
before it (and it); notices are acked by id only (*recv_ack* in the design doc). `--header:stderr` moves each header to stderr, `--limit <bytes>` stops a
listing at a message boundary. See [docs/wake-live-event-id.md](docs/wake-live-event-id.md#reading).
A listing is always in arrival order (the message file's mtime, stamped by the hub as it lands; ties
by msgid byte order), in every mailbox: in a subscription that is seq order within a session,
every delivery's msgid being its publication's `event-<session>-<seq>` (the topic's sequence session
and its number in that session), the same in every subscription, and a read ending with the topic's position notice
when the mailbox lacks the last publication ([docs/topics.md](docs/topics.md#event-ids)).

## Following a mailbox

`recv --follow` streams the backlog, then each message as it lands — every delivery (`send`,
`send_bag`, a topic's fan-out) wakes the follower at once; a 30 s poll is
only the backstop. `recv <mailbox> …` names the mailbox: your own identity, or a subscription you
own (see [docs/topics.md](docs/topics.md)); without one it is your own.

| | |
|---|---|
| `--peek` | streams each message once and consumes nothing: ack each with `recv_ack <msgid>` (from any session) once it is handled. Without `--peek`, each message is consumed once it is written whole to the connection — lost if the connection drops |
| the stream | no final chunk while it runs; it ends with `0;end=replaced;by=<conn>.<session>` or `0;end=gone` (below) |
| one follower per mailbox | a newer follow takes over: the one following that mailbox ends with the final chunk `0;end=replaced;by=<conn>.<session>` (the new follow's id: its connection and session channel) and exit 0. Only that follow: the identity's other connections (sends, `accept`, `chat`, follows of its subscriptions) never get it. The hub logs `follow <mailbox> conn=<new> replaced conn=<old>`. A client that gets it stops following — another reader holds the mailbox; a client that lost its connection reattaches at once ([docs/wake-live-event-id.md](docs/wake-live-event-id.md#takeover)) |
| live exchanges | between messages, the follow of your own mailbox streams a `part=live` chunk, data `LIVE <sid> <from> <msgid> (chunked|raw) [chat]` and a newline, for each open live send or chat offered to you, taken with `accept <sid>` ([docs/live-send.md](docs/live-send.md#recipient)) |
| the wake notice | an address that takes instances gets, on connect and on change only (first on every follow, again whenever it changes), a notice the hub renders (msgid `wakes-…`, `Wake: <n>`): the instances nobody follows with mail, a live send waiting, or a send held for `admit` / `reject` ([docs/live-send.md](docs/live-send.md#wake-notice)) |
| it ends | when its ssh session ends (noticed at its next wake), when the identity is released or rebound, or when the subscription is gone (the final chunk `0;end=gone`, exit 0) |
| a vanished client | the hub drops a client that stops answering keepalives (15 s apart, 4 missed), so a session behind a dead network ends within about a minute |

**Fields** are RFC 5322 headers, folding included. A client may set `Reply-To`, `Re`, `Subject`,
`Deadline`, and, in a send to a topic, `Gap` — a gap marker's only field
([docs/topics.md](docs/topics.md#gap-markers)) — **anything else is refused**, including `From`,
`Date` and `Serial`, which the hub stamps itself. A value with a control character other than TAB (a CR, say) is refused too (exit 2), and so is a
value that is not valid UTF-8, a `send_bag --msg` path included, so a stored header block is always
valid UTF-8; a NUL in a header block is dropped. An open header set becomes a second body by accretion.

The inline form takes the message from the raw command line, so its spacing survives.

## Bags

A **bag** is one message carrying a tree of files, sent as a tar and stored exactly as received, as
the payload of its message file. The hub does not extract it and rewrites nothing in it — ownership,
modes, headers and directories travel inside the tar and are the sender's and the receiver's business.
A folder travels as a bag.

- **one invocation, one message, one bag** — the atomic `ln` dedup gate is untouched
- **a tar is whole only with its end marker**, two zero blocks after the last member: without it, or cut
  inside a member or header, exit 4, nothing stored, and a retry stores; garbage that is not a tar, exit 2
- **`--msg PATH`** names the member *inside the bag* that is the message body; the body is that
  member's data inside the stored tar, not a copy. It must be a regular, non-sparse member, else exit 2
- the hub checks completeness and its own disk only: the end marker, a non-empty bag and a 256 MiB cap
  on stored bytes. Member names, types, count and depth are not checked; a receiver that extracts
  judges them. A leading `./` is ignored in matching a name; of two members with one name, the last wins
- `recv_bag --id <msgid>` streams the tar; `recv --id <msgid> --peek:bag <path>` scans it for that member
  (a sparse or non-regular one: exit 2)

The server component is `agsshub-hubd`: one Go daemon with its own SSH server, over a data dir of plain
files, no database ([docs/hub.md](docs/hub.md)). Runs on one always-on Linux VM (the "hub").

Install it with Go (1.27+):

```sh
go install github.com/cycanics/agsshub/go/cmd/agsshub-hubd@latest
```

## Help

`help` says what the hub supports, and `help <target>` what an address handles: each request's
`Subject`, whether it is structured or text, and how it is delivered. A service registers that with
`register_description`, and the hub validates it there. A purely programmatic service answers JSON by
default, and `--json` always does. Access is judged on the target: without it, the answer is the same
exit 3 whether the target is described, undescribed or missing. See **[docs/help.md](docs/help.md)**.

## Topics

A **topic** is an address the hub answers for itself: what is sent to it is hard-linked into every
subscription's mailbox. A **subscription** is a mailbox with one owner, handed back by `sub` as a
name — read it with `recv <sub>`, or follow it live with `recv <sub> --follow`. Publishing is ordinary `send`/`send_bag`; a publication's msgid is
`event-<session>-<seq>`, the publisher's own (`--id`) or the hub's next; a repeat within the record's session is `dup` (or `stale` for an older seq), and a repeat after a new session is a new publication. Operators create topics and say
who may publish with `hub-topic`; the role made for publishing, `publisher+<app>@<org>.ssh`, sends to
topics only and receives nothing. A reader sees a delivery its subscription missed as a skipped seq; a subscription mailbox that cannot take a delivery is
skipped, not its publisher's failure, and a publisher marks what its source may have lost with `Gap`. See
**[docs/topics.md](docs/topics.md)**.

## Identities

Names follow `<role>[.<project>][+<instance>][/<ws>]@<org>.ssh` — see
**[docs/identities.md](docs/identities.md)** for the grammar, the roles, who mints each, and what
the hub does and does not enforce.

### Claim registry, on disk

```
claims/<minter>/<identity>          one file per claim; the identity is the filename (`/` → `~`);
                                    <minter> = the registering workspace, or `operator` (hub-mint)
claims/.byfpr/<keyid>               -> ../<minter>/<identity>: the one identity a key may act as
claims/instance/<identity>          an instance's claim, written by its address's holder (`register`)
claims/.ibyfpr/<keyid>              -> ../instance/<identity>: the same index for instance keys
orgs/<ws>                           which orgs that workspace may claim (hub-enroll)
inbox/<identity>/<msgid>.msg        the mailbox — named by the identity, not its holder
```

## Identity model (two tiers)

- **Tier-1 workspace** — the root of trust. Each workspace VM holds one *registrar* ed25519 key
  (`/etc/hub-agent/registrar_key`), enrolled once on the hub. Its private key never leaves the VM.
- **Tier-2 agent/session** — an ed25519 keypair the agent **mints at runtime**. Through the
  registrar it claims a `run` identity; the hub appends `/<ws>` (the client never chooses the ws
  suffix), so cross-workspace squatting is impossible by construction. Registrar claims are
  ephemeral by default (per-session TTL) and first-come: once claimed, only the holder of the
  secret key can act as that name.
- **Operator roles** (`main`, `foreman`, `frontline`, `vmmanager`, `inference`, `group`, `commhub`,
  `publisher`) are bound to their key by the operator on the hub with `hub-mint`; no registrar can
  claim them.

Registration is a `link(2)`-atomic claim in a flat-file registry; the hub admits a runtime key only if
it holds a live claim. Identity reaches a session only from the key that logged in, which the client
cannot touch.

## Layout

| Path | What |
|---|---|
| `go/` | `agsshub-hubd`, the hub — [docs/hub.md](docs/hub.md); `hub-descriptor`, which checks a description for `hub-topic` — [docs/help.md](docs/help.md); `go/expiry`, the expiry notices — [docs/expiry-and-subject.md](docs/expiry-and-subject.md) |
| `lib/common.sh` | the operator tools' constants and helpers (the role table, the grammar, claims) |
| `lib/mint` | the operator's claims: `add`/`rm`/`list` for operator-minted roles (run by `hub-mint`) |
| `lib/backends/` | egress-transport plugin seam (`email`/`tg` placeholders) + `INTERFACE.md` |
| `bin/hub-enroll` | operator: enroll/replace a workspace's registrar key |
| `bin/hub-mint` | operator: bind an operator-minted identity to its key, or move it to a new name |
| `bin/hub-budget` | operator: a sender's flood budget, per identity or per role |
| `bin/hub-alias` | operator: map an alias → backend `{type, addr}` for routing |
| `bin/hub-topic` | operator: create a topic and set who may publish / subscribe |
| `install.sh` | one-shot hub setup (user, dirs, the daemon, the operator tools, the plugin seam) |
| `lib/help.json`, `lib/help.txt` | what `help` answers for the hub itself |
| `dev-hub/` | the hub in Docker for local integration tests, and `setup.sh` for its clients — [docs/dev-hub.md](docs/dev-hub.md) |
| `test/dev-hub.sh`, `test/full-disk.sh` | the hub through real ssh in a container; a really full disk |

## Message spool (filename-native)

Per recipient, `inbox/<recipient>/`:
- `<msg_id>.msg` — one file per message, written in one pass: the header block (hub-stamped `From:/Date:`
  from the key, the client's fields, and `Payload: file <name>` or `Payload: bag` when there is one), the
  body (a bag's is its `Msg:` member inside the tar), the payload as received, and a 212-byte trailer:
  `Header-Size`, `Message-Offset`, `Message-Size`, `Total-Size` and a reserved `Sha256`. A read that prints
  body or payload bytes checks `Total-Size` against the file's size: a mismatch is a damaged file, moved to
  `.damaged/`, exit 1. **`msg_id` is the
  filename** — listing is `readdir`, no parsing; threading is the client's concern, not the hub's. A
  topic's fan-out is one hard link of it per subscription; removal and expiry remove it
  ([docs/wake-live-event-id.md](docs/wake-live-event-id.md#message-file)).

Writes are staged then committed by an atomic `ln` of the `.msg` file, which is also the **dedup
gate**: a message id that already exists is dropped (`--id` lets a sender make a retry idempotent).
A full read consumes (deletes) a message; the reaper collects anything uncollected after `MSG_TTL`.

**Expiry notices.** What the reaper collects it counts, in one notice per sender and mailbox, which a
reader sees as a message from that sender before any other message: `recv`, `recv --peek`, `recv --follow`,
a subscription too. A notice has an `expired-` msgid, an `Expired` total, tables of what was lost per verb,
and no `Subject`. It clears like mail: a full read, or `recv_ack`. See [docs/expiry-and-subject.md](docs/expiry-and-subject.md).

**Flood control:** a per-`(sender,recipient)` token bucket rate-limits the messages one sender can
push at another (`send`, `send_bag`, `chat`); over budget → exit 5, which a sender must not route
around. Asks are capped at 256 per address: beyond that, exit 5 too. The reaper removes
buckets that are full (idle). The bucket's size is the **sender's budget**:

| Budget | Set by | Applies to |
|---|---|---|
| the sender identity's own | `hub-budget set <identity> --rate R --burst N` | that identity |
| its role's | `hub-budget set <role> --rate R --burst N` | every identity of the role without its own |
| default | — | everyone else: 0.5/s, burst 12 |

```sh
hub-budget set commhub --rate 20 --burst 200              # infrastructure identities send faster
hub-budget set group --rate 10 --burst 100
hub-budget set group.support@expa.ssh --burst 500         # rate stays the default 0.5/s
hub-budget rm  group.support@expa.ssh
hub-budget list
```

`--rate` is messages per second (decimals allowed), `--burst` whole messages. The most specific
budget applies whole: a field it leaves out is the default, as is a malformed one. Budgets live in
`budgets/<role>` and `budgets/<identity>` (`subject=`, `rate=`, `burst=`), written by the operator
and read by the hub. The exit-5 message names the budget that refused. Publishing to a topic uses
the topic's own bucket instead (`hub-topic --rate/--burst`).

## Plugins & addressing

**Backends** (egress, see `lib/backends/INTERFACE.md`) deliver to a non-native transport — `email` /
`tg`. Addressed via aliases: `hub-alias add carol --type email --addr carol@example.com`, then
`ssh hub send carol …` routes to `backends/email/send`. Until a real `send` is dropped in, the seam reports
`not implemented` (exit 40). Credentials live server-side, never on the ssh client.

`ssh hub list [--type native|topic|sub|email|tg]` enumerates reachable targets and filters by type.

## Deploy (on the hub VM, as root)

```sh
./install.sh
# for each workspace, enroll its registrar public key and the orgs it may claim:
hub-enroll ws-a acme,home < registrar_acme.pub
# for each operator-minted identity, bind its public key:
hub-mint add main/ws-a@acme.ssh < main_acme.pub
hub-mint add commhub@home.ssh < commhub.pub
# optionally, a faster flood budget for infrastructure senders:
hub-budget set commhub --rate 20 --burst 200
```

## Enroll a workspace (on the workspace VM)

```sh
# one-time: mint the registrar key, hand its .pub to the operator to run hub-enroll
ssh-keygen -t ed25519 -N '' -f /etc/hub-agent/registrar_key -C registrar@ws-a
# pin the hub host key once, verified against console:
ssh-keyscan <hub> > ~/.ssh/known_hosts.d/hub
```

`~/.ssh/config` on the workspace:
```
Host hub
    HostName <hub-ip>
    User hub
    IdentityFile ~/.hub/id
    IdentitiesOnly yes
    UserKnownHostsFile ~/.ssh/known_hosts.d/hub
    StrictHostKeyChecking yes
    ServerAliveInterval 30
```

## Agent usage

```sh
# mint a key and claim a run identity (attested by the workspace registrar key)
ssh-keygen -t ed25519 -N '' -f ~/.hub/id -C run
ssh -i /etc/hub-agent/registrar_key -o IdentitiesOnly=yes reg@hub register run.ingest+a1b2c3@acme.ssh --ttl 3600 --mode session < ~/.hub/id.pub

ssh hub id                       # -> run.ingest+a1b2c3/ws-a@acme.ssh serial=1
ssh hub chat foreman@acme.ssh     # live chat
ssh hub send foreman@acme.ssh --subject note -- hi
ssh hub send foreman@acme.ssh --subject report --file report.pdf < report.pdf
ssh hub recv --peek:header       # on the foreman's side: headers; then recv --id <msgid> --peek:file > out.pdf
```

## Exit codes

`0` ok · `1` internal, including a hub I/O error on any send (disk full, a failed copy, read, link or rename): retryable, nothing reported as stored; on a raw read, a damaged message file (its size differs from `Total-Size`) · `2` usage, including a bad `--subject`, a bad `--size`, a bad or misplaced `--wait`, an `--id` on a topic other than `event-<session>-<seq>`, `--id expired-*`, `wakes-*` or `head-*`, `--id event-*` other than to a topic, a read form that does not fit (`--id` with `--follow`, `--peek:rfc5322` without a single `--id`, `--peek:file` on a bag, `recv_bag` on a payload that is not a bag, a flag on `recv_ack` other than `-m:ids`, `--before` or `--before-including`, `--before` with ids or `-m:ids`, a `wakes-*` or `head-*` msgid to `--before`, [docs/wake-live-event-id.md](docs/wake-live-event-id.md#exits-1)), and a body longer than `--size` · `3` unauthorized/unknown peer, including an instance its address says does not exist (`reject`, also ending a sender waiting on its pickup), or the session's identity was rebound or released since it logged in, or (`recv --id`) none of the messages found, (`--peek:bag <path>`) no such member, (`recv_bag`) no such message, (`recv_ack --before`) no such msgid, nothing acked; `recv_ack` of a missing one answers `gone`, exit `0` · `4` a body incomplete: chunked and cut or aborted (`--live --chunked` and `chat --chunked`: either direction), shorter than `--size`, or a tar without its end marker; a retry can store it · `5` rate limited · `6` (`--live`, `chat`) recipient not live; (`send`, `send_bag` to an instance) no answer from its address within `wake_secs` and no mailbox at that moment, nothing stored; with `retry-after=<s>` on stderr for an instance (flows A2, C2, C) · `7` (`--live`, `chat`, `accept`) the exchange broke: a dropped connection · `8` (`send`, `send_bag`) stored, not picked: `--wait <s>` ended, or an instance's address did not answer within `wake_secs` while its mailbox exists; the message stays stored · `9` (`--live`, `chat`) live not supported: a topic, a subscription, an alias, a publisher on either end, the instance form of an address that takes none, an identity whose description says `live: false` · (`registrar`, `hub-mint`, `register`) `1` claim-conflict, `2` malformed identity, `3` role/workspace/org not allowed. Live sends and `accept`: [docs/live-send.md](docs/live-send.md#outcomes); instances and admission: [docs/identities.md](docs/identities.md#instances).

## Status

Implemented: identity, chat, file streaming, a filename-native spool with atomic dedup (a stored message survives a process crash; with `--durable` also an OS crash or power loss), per-pair
flood control with operator-set budgets, uncollected-mail GC, an alias registry with typed listing, topics with
subscriptions and event ids, instances with admission and the wake notice, live sends, descriptions and `help`, and the backend plugin
seam (placeholders).

Tests: `cd go && go test ./...` runs the hub in-process over a temp tree: identity/claim/squatter/cross-ws, the
role table (shapes, slots, who mints, `/<ws>` appended), operator minting and rebinding through the real
`lib/mint`, split brain at claim and send time, lapsed-claim delivery, release/tombstone/reclaim, expiry+reaper,
text + file round-trip, dedup, flood control and per-identity/per-role budgets, alias
routing + typed list, GC, and topics (policy, fan-out, topic-wide
dedup, files and bags, follow, expiry), and following one's own mailbox (wake on every delivery, arrival order,
newest follower wins, end on rebind or a dead session), and live sends and chat (the three forms, raw and chunked, the hub header block,
untouched framing, refusals, every exit code, the accept deadline, accept by the addressed identity only and once,
12 concurrent exchanges to one recipient, a sender that leaves mid-exchange, nothing spooled), and instances (the form only on `--instances` addresses, registration by the
address, a new key evicting the old, release, expiry, the address ending them) and admitting them (each flow:
stored, the ask held and answered by `admit`, `reject`, `register` or a follow, its timeout in both mailbox states, its
last sender leaving, several senders on one ask; a reject racing a store, admit racing reject, a reject with a claim;
the wake notice and its nudges; flow C's transient entry; exit 9), what each role may receive and send, the
publisher (refused both ways, every send form to a topic), gap markers, and event ids (every row of the publish
table, `--id event-…` on each form, the record across a restart, a failed record write, repeated msgids,
listing order across sessions, a taken name, the position notice, a reader and a `sub` mid-fan-out, concurrent
publications), a publication killed at each of its points (and retried after a restart), a subscription that cannot take a delivery (its seq skipped, in a listing and a follow), a
publication's work after earlier failures, a raw read,
field values, and `help` and `register_description`. `test/dev-hub.sh` runs the hub through real ssh, and the
operator tools as root, in a container ([docs/dev-hub.md](docs/dev-hub.md)); `test/full-disk.sh` meets a really full
disk.

Deferred: webhook subscriptions and HTTP ingress for topics (docs/topics.md), real backend implementations
(email/tg), and a recipient-side cross-transport dedup store
(only needed once a message can arrive by two paths).
