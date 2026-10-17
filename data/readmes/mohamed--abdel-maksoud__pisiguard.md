<img src="src/icons/PISIGuard-icon-full.png" width="180"/>

# PISIGuard

*Protect your personal and sensitive info when you chat with AI*

**PISIGuard**: **P**ersonally **I**dentifiable & **S**ensitive **I**nformation **Guard**


[<img src="assets/demo.gif" width="900" alt="PISIGuard demo. sensitive data is caught, masked and restored right in the browser"/>
](https://github.com/user-attachments/assets/d79121fd-f37f-4210-8d08-89a597238056)

I built PISIGuard because I've been horrified at how much personal & sensitive information people (including myself) are feeding AI on daily basis. It is cumbersome to censor information by hand, so obviously very few do that at varying degrees of consistency.
I wanted something practical that will hide personal & sensitive data, and of course without routing them through yet another server. So PISIGuard runs entirely in your browser. It spots names, email addresses, phone numbers, credit card numbers, passwords, API keys, and more, replaces them with safe placeholders, then puts the real values back into the AI’s reply. From your point of view, it’s mostly invisible; from the AI’s point of view, the sensitive stuff was never there.

All detection, masking, and restoration happens **locally**. No data is sent to an external service. Nobody sees your messages but you and the AI, and the AI only sees the placeholders.

---

**DISCLAIMER:** This software is provided "AS IS", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

---

## Features

- Catches common sensitive information before they hit the AI servers: names, emails, phone numbers, passwords, API keys, and more.
- Masks each piece of sensitive data with a unique placeholder (like `John Smith` instead of your real name) before the message is sent.
- Restores the original values in the AI’s response automatically, so you can read the reply naturally.
- Works on popular AI chat platforms (ChatGPT, Claude, and DeepSeek).
- All processing stays on your device. No telemetry, no server calls, no analytics.
- Minimal permissions: the extension only needs access to the sites you use it on.
- No background processes: the extension only activates when you’re on a supported AI chat page.
- PISIGuard is **Configurable**: if you need more detailed rules to detect sensitive information, you can provide your own set (advanced use).

## Install

### From Web Store
<!--<a href="#"><img src="resources/chrome-store.png" width="248" alt="Available in the Chrome Web Store"/></a>-->
<a href="https://addons.mozilla.org/en-US/firefox/addon/pisiguard/"><img src="assets/firefox-store.png" width="258" alt="Get the Firefox Add-on"/></a>

### From Github Releases
1. Download the latest [release](https://github.com/your-username/pisiguard/releases) `.zip` for your browser family (Chrome includes Edge, Opera, etc.; Mozilla includes Firefox).
2. Unzip the file.
3. Load the extension manually:
   - **Chrome / Edge / Brave**
     Go to `chrome://extensions`, enable “Developer mode”, click “Load unpacked”, and select the unzipped folder.
   - **Firefox**
     Go to `about:debugging`, click “This Firefox”, then “Load Temporary Add-on”, and pick any file inside the unzipped folder.

### Build Your Own
1. Clone this repo.
2. Install the dependencies:
   `pnpm install`
3. Run the tests:
   `pnpm test`
4. Build the extension:
   `pnpm run build`
   A `dist` folder will appear with subfolders for each browser.
5. Load the unpacked extension from the `dist` folder using the same manual steps as above.


---
`PISIGuard` is a work of :heart: by [Codoma.tech](https://www.codoma.tech/).
