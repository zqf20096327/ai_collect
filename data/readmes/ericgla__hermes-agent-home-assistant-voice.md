# Hermes Agent Conversation for Home Assistant

This integration lets you talk to your own [Hermes Agent](https://github.com/NousResearch/hermes-agent)
through the voice devices in your house.

Normally Assist, Home Assistant's voice assistant, answers with its built-in intent matching
or a general-purpose LLM. This integration puts Hermes in that spot instead. Say "Okay Nabu,
check my email" or "add earplugs to my Kroger cart" to a Home Assistant Voice Preview
Edition (or any other Assist satellite) and the request goes to the same agent you already
use from Telegram or the CLI, with all of its tools, skills, memory and connected accounts.
Hermes can also control Home Assistant, so "turn off the kitchen lights" still works.

## Features

- Replies are kept to one to three short spoken sentences, and any markdown is stripped
  before text-to-speech reads it.
- Hermes is told which voice device heard you and which area it's in, so "turn off the
  lights" or "next song" means that room.
- Follow-ups keep their context, and when Hermes asks you something the device keeps
  listening so you can answer without the wake word.
- Slow requests don't time out. If Hermes is still working after 15 seconds (you can change
  this), the speaker says "I'm working on that" and reads out the answer when it's ready.
- Saying "start over" begins a fresh Hermes conversation.
- Voice requests can share Hermes's long-term memory with your other chats, or be kept
  separate.
- Automations can ask Hermes things too, and get the full answer back to use in a
  notification or anywhere else.
- Sensors show whether the gateway is up, whether Hermes reports a problem, and which of
  its chat platforms are disconnected.

This doesn't run Hermes for you, and it doesn't replace the rest of the voice pipeline.
Home Assistant still handles the wake word, speech-to-text and text-to-speech with whatever
engines you already use.

## Requirements

- Home Assistant 2025.8 or newer
- A Hermes Agent gateway with its API server turned on
- An Assist voice satellite, if you want to talk to it (typing in the Assist dialog works too)

Tested with Home Assistant 2026.9.3 and Hermes Agent 0.21.0.

## How it works

The integration registers Hermes as an Assist conversation agent. Your satellite still uses
Home Assistant for the wake word, speech-to-text and text-to-speech. The transcribed text
goes to the Hermes gateway's API server, and the reply is spoken back.

```
Voice PE ──ESPHome──▶ HA Assist pipeline
                      ├─ STT
                      ├─ Conversation agent: Hermes ──POST /v1/responses──▶ Hermes gateway
                      └─ TTS ──▶ Voice PE
```

Each Assist conversation maps to a named Hermes conversation
(`homeassistant-<conversation_id>`), so a follow-up like "…and the office?" keeps its context
on the Hermes side, earlier tool calls included.

## Setup

### 1. Turn on the Hermes API server

On the machine running your gateway, add this to `~/.hermes/.env`:

```bash
API_SERVER_ENABLED=true
API_SERVER_KEY=<a long random string>
API_SERVER_HOST=0.0.0.0          # listen on the LAN, not just localhost

# Optional: let Hermes control Home Assistant (enables the ha_* tools)
HASS_URL=http://homeassistant.local:8123
HASS_TOKEN=<long-lived access token from your HA profile>
```

Anyone on your network who has the key can use your agent, so pick a long one and don't
expose port 8642 to the internet.

Restart the gateway (`hermes gateway`), then check that Home Assistant's host can reach it:

```bash
curl -H "Authorization: Bearer $API_SERVER_KEY" http://<hermes-host>:8642/v1/models
```

### 2. Install the integration

With [HACS](https://hacs.xyz):

[![Open your Home Assistant instance and open this repository in HACS.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=ericgla&repository=hermes-agent-home-assistant-voice&category=integration)

Or add it by hand: in HACS, open the ⋮ menu → **Custom repositories**, enter
`https://github.com/ericgla/hermes-agent-home-assistant-voice` with type **Integration**, then
download **Hermes Agent Conversation**.

Without HACS, copy `custom_components/hermes_conversation` into your Home Assistant config
directory so it ends up at `/config/custom_components/hermes_conversation`. For example,
using the SSH add-on:

```bash
scp -r custom_components/hermes_conversation root@homeassistant.local:/config/custom_components/
```

Restart Home Assistant either way.

### 3. Connect it to Hermes

Go to **Settings → Devices & services → Add integration → Hermes Agent Conversation** and
enter your gateway URL (for example `http://192.168.1.10:8642`) and your `API_SERVER_KEY`.

To change the address or key later, use **Reconfigure** in the integration's ⋮ menu. If
Hermes starts rejecting the key, Home Assistant will ask you for a new one.

### 4. Create a voice assistant

1. Go to **Settings → Voice assistants → Add assistant**.
2. Set the conversation agent to **Hermes Agent**, and pick your usual speech-to-text and
   text-to-speech engines (Whisper and Piper, Home Assistant Cloud, and so on).
3. Decide on **Prefer handling commands locally**. With it on, simple commands like "turn off
   the kitchen lights" are handled instantly by Home Assistant and everything else goes to
   Hermes. With it off, everything goes to Hermes.
4. Go to **Settings → Devices & services → ESPHome**, open your voice device, and choose the
   new assistant under **Assistant**.

## Options

These are under the integration's **Configure** button.

| Option | Default | What it does |
|---|---|---|
| Voice instructions | short, spoken, no markdown | Sent to Hermes as `instructions` on every turn |
| Model override | *(empty)* | Use a specific model instead of the gateway's default |
| Start-over phrases | `start over, new conversation, reset conversation` | Saying exactly one of these starts a fresh Hermes conversation without asking Hermes. Clear it to turn this off |
| New session after idle | 20 min | Start a fresh Hermes session when a conversation has had no activity for this long. `0` turns this off |
| Memory session key | `homeassistant:assist` | Sent as `X-Hermes-Session-Key` to scope long-term memory. Clear it to turn this off |
| Hand-off after | 15 s (max 29) | If Hermes hasn't answered by then, say "I'm working on that" and read the answer out on the voice device when it's ready. `0` waits instead |
| Maximum response time | 600 s | Give up on a Hermes request after this long |

### Room and music context

Every request tells Hermes which voice device is speaking and what area it's in, so "turn
off the lights" means that room. Hermes also gets the best media player in that area for
music, preferring an online Music Assistant player, so "next song" or "play some jazz"
reaches the right speaker. For this to work, put each room's Music Assistant player in the
same area as its voice device.

### Follow-up detection

As in Home Assistant, a reply ending in a question mark keeps the microphone open. The
default voice instructions ask Hermes to end with a question whenever it needs something
from you, and not to close by offering to do more. That offer was the most common reason
the mic stayed open for nothing.

### Long-running requests

Agent turns that use a lot of tools, like checking email or doing research, can take
minutes. After the hand-off time the speaker says "I'm working on that…" and goes back to
idle. When Hermes finishes, the answer is read out on the same device with
`assist_satellite.announce`. Requests typed in the Home Assistant UI, where there's no
satellite, get a persistent notification instead. If you ask for something else while a
request is still running, it goes to a separate Hermes conversation so it isn't stuck
waiting behind the first one.

If the late answer is a question, it's delivered with `assist_satellite.start_conversation`
instead, so the device listens for your reply without the wake word. Your reply continues
the same Hermes conversation, so Hermes still knows what it was doing. Satellites that don't
support starting a conversation get a plain announcement.

Assist cancels a satellite's turn after about 30 seconds, which is why the hand-off can't be
set higher than 29. If a turn gets cancelled anyway, the request keeps running and the
answer is still announced, and the integration logs how long the turn lasted.

## Automations

### Asking Hermes from an automation

The **Hermes Agent Conversation: Ask Hermes** action (`hermes_conversation.ask`) sends a
message to Hermes and waits for the answer. This morning briefing sends a summary to your
phone:

```yaml
triggers:
  - trigger: time
    at: "07:30:00"
actions:
  - action: hermes_conversation.ask
    data:
      message: Summarize my unread email and today's calendar in three sentences.
    response_variable: hermes
  - action: notify.mobile_app_my_phone
    data:
      title: Morning briefing
      message: "{{ hermes.text }}"
```

| Field | What it does |
|---|---|
| `message` | What to ask or tell Hermes. Required |
| `conversation` | Name of a Hermes conversation to continue. Leave it out to start a new one |
| `instructions` | Extra instructions for this request, such as how to format the answer |
| `config_entry_id` | Which gateway to ask. Only needed if you've set up more than one |

The response has `text`, which is Hermes's answer, and `conversation`, which is the name of
the conversation it used. To ask a follow-up in a later step, pass
`conversation: "{{ hermes.conversation }}"`.

Home Assistant also has a built-in `conversation.process` action that can talk to any
conversation agent, but it goes through the voice path. Hermes gets the "short spoken
sentences" instructions, and if it takes longer than the hand-off time you get back "I'm
working on that" instead of the answer. `ask` skips both. It sends no instructions unless
you give some, keeps any markdown in the answer, and waits as long as the **Maximum response
time** option allows (10 minutes by default). The model override and memory session key
options still apply.

### Gateway health

The integration checks the gateway once a minute and adds these entities to the Hermes
Agent device:

| Entity | What it shows |
|---|---|
| Connectivity | On while the gateway answers. It turns off when the gateway can't be reached, rather than going unavailable, so you can trigger on it |
| Status | On (shown as "Problem") when one of Hermes's own readiness checks fails. The `failing_checks` attribute says which ones and why |
| Active agents | How many agent turns are running right now |
| Disconnected platforms | How many of Hermes's chat platforms (Telegram, Discord and so on) aren't connected. Each one's error is an attribute |
| Version | The Hermes Agent version |

Gateways too old to have `/health/detailed` only report connectivity and version.

To get a message when Hermes has been unreachable for five minutes:

```yaml
triggers:
  - trigger: state
    entity_id: binary_sensor.hermes_agent_connectivity
    to: "off"
    for: "00:05:00"
actions:
  - action: notify.mobile_app_my_phone
    data:
      message: Hermes has been unreachable for five minutes.
```

## Troubleshooting

"Could not reach the Hermes API server" during setup usually means the gateway is only
listening on localhost. Check `API_SERVER_HOST=0.0.0.0` and run the `curl` command from step
1 on the Home Assistant host.

To see what's being sent to Hermes and what comes back, turn on debug logging in
`configuration.yaml`:

```yaml
logger:
  logs:
    custom_components.hermes_conversation: debug
```

Bug reports and questions go in [GitHub issues](https://github.com/ericgla/hermes-agent-home-assistant-voice/issues).

## Development

```bash
python -m venv .venv
.venv/bin/pip install -r requirements_test.txt
.venv/bin/pytest
```

The tests need Python 3.14.

## License

[MIT](LICENSE)
