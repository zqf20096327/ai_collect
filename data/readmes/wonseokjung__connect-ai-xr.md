<p align="center"><img src="docs/banner.jpg" width="100%" alt="XR, CONNECT AI LAB"></p>

<p align="center">
  <b>CONNECT AI LAB</b> · AI education for everyone<br>
  <a href="https://www.youtube.com/@CONNECT-AI-LAB">YouTube</a> · <a href="https://www.aicitybuilders.com/vibecoding">Course: Visual Vibe Coding</a> · <a href="README.ko.md">한국어</a>
</p>

# connect-ai-xr

**Say one sentence to your coding agent. Get an XR app that opens on Meta Quest, and in 3D on any computer or phone.**

```bash
npx github:wonseokjung/connect-ai-xr install-skill
```

Paste that line into Claude Code, Codex, Antigravity or Cursor and ask it to install. Then say: "Make me an XR app for my Quest, a showroom for my product." Needs [Node.js](https://nodejs.org) 18+. No API key, no game engine.

Free textbook (AI Night School XR, 7 prompts, in Korean): https://www.aicitybuilders.com/yahak/xr/

<p align="center">
  <img src="skill/assets/mascot/greet.gif" width="68" alt="XR Craftsman · Greet">&nbsp;
  <img src="skill/assets/mascot/build.gif" width="68" alt="XR Craftsman · Build">&nbsp;
  <img src="skill/assets/mascot/check.gif" width="68" alt="XR Craftsman · Check">&nbsp;
  <img src="skill/assets/mascot/done.gif" width="68" alt="XR Craftsman · Done"><br>
  <sub><b>Jang Yeong-sil · XR Craftsman</b> (CONNECT AI HQ PixelCrew) — gently animated pixel portrait that switches expression as it greets, designs, verifies, and launches your WebXR world.</sub>
</p>

<p align="center"><img src="docs/demo.gif" width="100%" alt="The orrery and xr-room apps running in a browser"></p>

## Five apps to start from

All drawn in code, no image or model files. Shown here on a laptop, no headset.

<table>
<tr>
<td width="50%" valign="top"><img src="docs/shots/orrery.jpg" width="100%" alt="Orrery"><br><b>orrery</b><br><sub>Planets turn on a wooden table. Pinch one and it plays its note.</sub></td>
<td width="50%" valign="top"><img src="docs/shots/xr-room.jpg" width="100%" alt="XR Room"><br><b>xr-room</b><br><sub>A glass panel turns the room to day, dusk or night.</sub></td>
</tr>
<tr>
<td width="50%" valign="top"><img src="docs/shots/product-showroom.jpg" width="100%" alt="Product Showroom"><br><b>product-showroom</b><br><sub>Your product's .glb or photo on a pedestal you can walk around.</sub></td>
<td width="50%" valign="top"><img src="docs/shots/ar-desk.jpg" width="100%" alt="AR Desk"><br><b>ar-desk</b><br><sub>Quest 3 / 3S: pinch a monitor, a plant or a clock onto your real desk.</sub></td>
</tr>
<tr>
<td width="50%" valign="top"><img src="docs/shots/gallery.jpg" width="100%" alt="Gallery"><br><b>gallery</b><br><sub>Hang your photos and walk through. Pinch the floor to jump there.</sub></td>
<td width="50%" valign="top"><b>It adapts to the device</b><br><sub>Quest 3 / 3S: AR and VR. Quest 2: VR. Computers and phones: the same scene in 3D.</sub></td>
</tr>
</table>

## Open it on Meta Quest in 3 steps

1. On your computer, same Wi-Fi as the headset:
   ```bash
   npx github:wonseokjung/connect-ai-xr demo
   ```
2. In the Meta Quest Browser, type the `https://192.168...` address it prints (with the s). The first time, tap Advanced, then Proceed: it's your own computer.
3. Press Enter VR or Enter AR. Thumb and index finger together is a click.

If your computer asks about the firewall the first time, allow it.

## How your agent works with it

Your agent types the commands. You just talk.

1. Picks the app closest to what you asked and makes a new folder. `new`
2. Changes it the way you asked. Your photos and models just go in the folder.
3. Opens and tests it before you put the headset on: errors, whether it's light enough for a Quest, and a screenshot. `check`
4. Makes the address for your Quest. `serve`

Made a 3D page somewhere else, like Google AI Studio? Bring it in and your agent moves it onto this setup so it opens on the Quest.

<!-- team:start -->
## CONNECT AI LAB's AI employees

I'm building AI employees one by one, in the open. Grab the one you need first.

<table>
<tr><td width="34%" valign="top"><b>Business analyst</b><br><a href="https://github.com/wonseokjung/reversebusiness"><code>reversebusiness</code></a></td><td valign="top">Give it a website, and it breaks down how that business makes money.</td></tr>
<tr><td width="34%" valign="top"><b>Video editor</b><br><a href="https://github.com/wonseokjung/connect-ai-video-motion"><code>connect-ai-video-motion</code></a></td><td valign="top">Give it your video, and it puts motion graphics in the empty space around you.</td></tr>
<tr><td width="34%" valign="top"><b>Motion designer</b><br><a href="https://github.com/wonseokjung/connect-ai-motion"><code>connect-ai-motion</code></a></td><td valign="top">Give it a few lines of text, and it makes a motion graphics video. No footage needed.</td></tr>
<tr><td width="34%" valign="top"><b>Marketing team</b><br><a href="https://github.com/wonseokjung/connect-ai-marketer"><code>connect-ai-marketer</code></a></td><td valign="top">Replies, social listening and uploads, 24/7 in your own browser.</td></tr>
<tr><td width="34%" valign="top"><b>Writer</b><br><a href="https://github.com/wonseokjung/connect-ai-writer"><code>connect-ai-writer</code></a></td><td valign="top">Give it one video, and it writes a post for every platform in your voice, with pictures.</td></tr>
<tr><td width="34%" valign="top"><b>XR employee</b> · <b>this one</b><br><a href="https://github.com/wonseokjung/connect-ai-xr"><code>connect-ai-xr</code></a></td><td valign="top">Give it one sentence, and it makes an XR app that opens on Meta Quest, computers and phones.</td></tr>
</table>
<!-- team:end -->

---

All commands: `npx github:wonseokjung/connect-ai-xr help`. To see what your computer has: `doctor`.

License: MIT + Commons Clause. The code is open to read (source available) but not for resale. Use it, change it and share it for your own business and channel; the XR apps you make with it are yours. The one thing you can't do: sell this tool itself, or sell a paid service or course whose value comes entirely or mostly from it. The bundled three.js stays under its own MIT license. Details in [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md).

How to build tools like this with your own AI agent: [Visual Vibe Coding](https://www.aicitybuilders.com/vibecoding).

<table><tr>
<td width="140" valign="top"><img src="docs/brand/jay.jpg" width="128" alt="AI Mentor Jay"></td>
<td valign="top"><b>Made by AI Mentor Jay</b> · CONNECT AI LAB<br>
I'll keep releasing AI employees as open source, one by one, and show how each one is built on YouTube and in the course.<br>
<a href="https://www.youtube.com/@CONNECT-AI-LAB">YouTube</a> · <a href="https://www.aicitybuilders.com/vibecoding">Visual Vibe Coding</a> · <a href="https://github.com/wonseokjung">More open source</a></td>
</tr></table>
