# sims-mcp

![sims-mcp](screenshots/mcp.png)

This is a Model Context Protocol (MCP) server for the game the Sims 1 Legacy. It allows you to retrieve important information about your household so that you can directly ask AI for in-game advice.

*WIP*: I'm working on extending the MCP server to also support sending actions to your Sims household.

I wrote a blogpost about how to speedrun reverse engineering Sims 1 with GhydraMCP [here](https://peterevers.nl/posts/2026/01/sims-mcp/) .

## Supported MCP Functions

| Function | Description |
|----------|-------------|
| `get_household_money` | Get the current household money (Simoleons) from The Sims |
| `get_household_persons` | Get all Sims in the current household with their motive values (energy, comfort, hunger, hygiene, bladder, room, social, fun, mood) |

## Setup

I bought the game, but in order to mod the game you need to circument Digital Right Management (DRM). In theory you can use the read-only MCP with the original game, but I'm also planning to make some adjustment to the event queing (imagine having a household of LLMs playing the game). Hence, I downloaded the cracked version by Anadius v1.0.0.158. The mod only works for this version at the moment. 

- Microsoft Visual Studio
- Sims 1 - Anadius v1.0.0.158 

Then run `editbin` to prevent Address space layout randomization (ASLR).

```console
cmd /c '"C:\Program Files\Microsoft Visual Studio\18\Community\VC\Tools\MSVC\14.50.35717\bin\Hostx64\x64\editbin.exe /DYNAMICBASE:NO "C:\The Sims 1 - Legacy Collection\sims.exe"'
```

You can now build the MSVC project and copy the DLL and executable `sims_injector.exe` in the Sims folder. The game should start.

## MCP Configuration Claude (Code)

```json
{
    "sims": {
        "command": "python",
        "args": [
            "C:\\projects\\sims-llm\\mcp_bridge.py"
        ]
    }
}
```

Restart the client so that the changes can take effect.
