[![Twitter: @NorowaretaGemu](https://img.shields.io/badge/X-@NorowaretaGemu-blue.svg?style=flat)](https://x.com/NorowaretaGemu)

<br>
<div align="center">
  <a href="https://ko-fi.com/cursedentertainment">
    <img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="ko-fi" style="width: 20%;"/>
  </a>
</div>
<br>

<div align="center">
  <img alt="Unity" src="https://img.shields.io/badge/unity%20-%23323330.svg?&style=for-the-badge&logo=unity&logoColor=white"/>
</div>

<div align="center">
  <img alt="C#" src="https://img.shields.io/badge/C%23-%23323330.svg?&style=for-the-badge&logo=csharp&logoColor=white"/>
  <img alt="JSON" src="https://img.shields.io/badge/JSON-%23323330.svg?&style=for-the-badge&logo=json&logoColor=white"/>
  <img alt="HLSL" src="https://img.shields.io/badge/HLSL-%23323330.svg?&style=for-the-badge&logo=microsoft&logoColor=white"/>
  <img alt="ShaderLab" src="https://img.shields.io/badge/ShaderLab-%23323330.svg?&style=for-the-badge&logo=unity&logoColor=white"/>
</div>
<br>

# ConfederateAI

*Logic-based 3D AI for Unity*

<div align="center">
    <img src="https://raw.githubusercontent.com/CursedPrograms/ConfederateAI/main/Assets/Sprites/Confederate%20AI%20Logo.png"
        alt="Confederate AI logo" style="width:40%;">
</div>

Allies and enemies that patrol, spot each other, fight, follow you and die in a heap. Plain C# on Unity's NavMesh, no plug-ins.

**Website:** https://cursedprograms.github.io/ConfederateAI/ · **itch.io:** https://cursed-entertainment.itch.io/confederate-ai

![Confederate AI agents and editor windows in Unity](images/unity-editor.jpg)

## Features

- **Two factions:** allies and enemies find each other within their sight distance, go for the nearest target and attack; enemies go after the player too.
- **Movement:** random wandering, set waypoints, or a path of linked waypoints (with branches), all on the NavMesh, walking or running.
- **Melee combat:** health, stamina and regeneration, damage, levels (up to a maximum level), attack animations and blood.
- **Deaths:** ragdoll or animated.
- **Companions:** walk up to an ally and press *Action* to have them follow you; *Reset* sends them back.
- **Spawners:** spawn agents (or followers), optionally respawning them.
- **Editor tools:** Character Editor, Character Debugger, Waypoint Manager, AI Creator (characters, spawners, the controller) and Character Cleaner (removes the AI again).

![The Confederate AI editor windows](images/editor-windows.jpg)

## Before you start

- Use URP (Universal Render Pipeline) and the new Input System.
- Have a blood pool and a blood spatter particle system.
- Create the UI elements in world space and make them children of their AI (the player's can sit on the camera).
- Double-check every field that needs a GameObject.

The project is a Unity 2022.3 project; open the folder in Unity Hub.

## Setup

### 1. GameController
- **Tag:** "GameController"
- **Attach:** `AIControllerCore.cs`
- Create 2 children (one per faction):
  - **Attach:** `FauxTarget.cs`
  - **Set Faction:** 0 (Ally), 1 (Enemy)

### 2. AI agent
- **Attach:** `AICore.cs`
- Create a child object:
  - **Attach:** `AIFollowControl.cs`
- Create a ragdoll

### 3. Player (Character Controller)
- **Tag:** "Player"
- **Attach:** `PlayerCore.cs`

### 4. Spawner
- **Attach:** `AISpawner.cs`

## Used in

- [Araknia](https://cursed-entertainment.itch.io/araknia)
- [Nystylla: Girls of Maluxzka](https://cursed-entertainment.itch.io/nystylla)

<div align="center">
<a href="https://cursedprograms.github.io/ConfederateAI/" target="_blank">
    <img src="https://raw.githubusercontent.com/CursedPrograms/ConfederateAI/main/images/site-qr.png"
        alt="QR code to the Confederate AI website" style="width:200px;">
</a>
</div>

<br>
<div align="center">
© Cursed Entertainment 2026
</div>
<br>
<div align="center">
<a href="https://cursed-entertainment.itch.io/" target="_blank">
    <img src="https://raw.githubusercontent.com/CursedPrograms/cursedentertainment/main/images/logos/logo-wide-grey.png"
        alt="CursedEntertainment Logo" style="width:250px;">
</a>
</div>
