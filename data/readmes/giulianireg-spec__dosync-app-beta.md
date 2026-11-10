<a id="english"></a>

# DoSync App · open beta

**English** · [Español](#espanol)

> 🧪 **This is a beta.** The app already works in real homes, but we are still
> testing it with many brands and devices. Expect rough edges; some brands are
> tested only against simulators. **Your feedback helps a lot**: what worked, what
> didn't, and what you'd like it to do.

DoSync is a free Android app that runs your home in your own words: *"turn off all
the lights"*, *"set the bedroom AC to 24"*, *"put the latest video from that channel
on the TV"*. **Your phone is the hub**: no extra device to buy, no account of ours.

<p>
<img src="capturas/01-inicio.png" width="200" alt="Home: type or say a command">
<img src="capturas/04-dispositivos.png" width="200" alt="Devices found on the Wi-Fi">
<img src="capturas/03-controles.png" width="200" alt="Controls for a device">
<img src="capturas/02-rutinas.png" width="200" alt="Routines">
<img src="capturas/05-noche.png" width="200" alt="Night mode">
</p>

## Download

| Where | Status |
|---|---|
| **GitHub** (this repository) | [Latest version ↓](../../releases/latest): download `DoSync-x.y.z.apk` and open it on your Android phone (8.0 or newer). The app tells you when a new version is out. |
| **Google Play** (closed test) | Three steps, with your phone's Google account: 1) [join the testers group](https://groups.google.com/g/dosync_testers), 2) [accept the test](https://play.google.com/apps/testing/dev.dosync.app), 3) [install it from Google Play](https://play.google.com/store/apps/details?id=dev.dosync.app). It updates itself. |

If you later install DoSync from Google Play, uninstall the GitHub one first: they
are signed differently and don't update each other.

## What it does

- **Finds** what's on your Wi-Fi and Bluetooth and adds it with one tap.
- **Understands commands in 6 languages** (English, Spanish, Portuguese, French,
  German and Italian) on the phone, free, without AI.
- **With AI (optional)**, your own (Claude, Gemini or ChatGPT) or on-device Gemini
  Nano: searches the web, chains steps, schedules timers and rules, creates scenes.
- **Or free AI on your own computer**, with [Ollama](https://ollama.com) or LM Studio:
  no key, no cost, and your commands never leave your home. The app finds it on your
  Wi-Fi and picks the model (recommended: `qwen3`). In Ollama, turn on
  *Settings → Expose Ollama to the network*. While the computer is on, everything
  works except web search.
- **Several homes** (yours, the beach house) and **family invited** with a one-time, encrypted code.
- **Scenes and routines** that run with the app closed.
- **Infrared control** with the phone's IR blaster or a Broadlink.
- **Sensitive actions wait for your confirmation**: unlocking a door, opening a
  gate, turning on an oven.

Works with thousands of devices, and more brands keep coming: Philips Hue and WiZ, TP-Link, Shelly, Tuya, IKEA, Samsung,
LG, Android TV, Fire TV, Roku, Sonos, tado°, Nest, Netatmo, Bosch, Homematic, Miele,
Home Connect, Nuki, Somfy, Home Assistant and many more.

## Feedback

[Share your experience](../../issues/new?template=opinion.yml) ·
[Report a bug](../../issues/new?template=error.yml) ·
[Request a brand](../../issues/new?template=marca.yml) · rgiuliani@dosync.dev

## Privacy

Your data stays on your phone: DoSync has no servers that receive it.
[Privacy policy](https://giulianireg-spec.github.io/dosync-adapters/privacy/).

## About this repository

This repository hosts the downloadable versions, release notes and feedback. The
app's source code is not public. DoSync App is built on the
[open DoSync protocol](https://dosync.dev).

Free to use under the [license](LICENSE). © 2026 Rodrigo Giuliani.

---

<a id="espanol"></a>

# DoSync App · beta abierta

**Español** · [English](#english)

> 🧪 **Está en beta.** La app ya funciona en casas reales, pero todavía la estamos
> probando con muchas marcas y aparatos. Puede haber errores, y algunas marcas
> están probadas solo con simuladores. **Tu opinión nos ayuda muchísimo**: lo que
> funcionó, lo que no y lo que te gustaría que haga.

DoSync es una app gratis para Android que maneja tu casa con tus propias
palabras: *"apagá todas las luces"*, *"poné el aire del dormitorio en 24"*,
*"poné en la tele el último video de Luisito Comunica"*. **El teléfono es el hub**:
no hace falta comprar otro aparato ni crear una cuenta nuestra.

## Descargar

| Dónde | Estado |
|---|---|
| **GitHub** (este repositorio) | [Última versión ↓](../../releases/latest): baja `DoSync-x.y.z.apk` y ábrelo en tu Android (8.0 o más nuevo). La app te avisa cuando hay una versión nueva. |
| **Google Play** (prueba cerrada) | Tres pasos, con la misma cuenta de Google del teléfono: 1) [únete al grupo de testers](https://groups.google.com/g/dosync_testers), 2) [acepta la prueba](https://play.google.com/apps/testing/dev.dosync.app), 3) [instálala desde Google Play](https://play.google.com/store/apps/details?id=dev.dosync.app). Se actualiza sola. |

Si después instalas DoSync desde Google Play, desinstala antes la de GitHub: están
firmadas distinto y no se actualizan una a la otra.

## Qué hace

- **Encuentra sola** lo que hay en tu WiFi y por Bluetooth, y lo agrega con un toque.
- **Entiende órdenes en 6 idiomas** (español, inglés, portugués, francés, alemán e
  italiano) sin IA y gratis, directamente en el teléfono.
- **Con IA (opcional)**, la tuya (Claude, Gemini o ChatGPT) o Gemini Nano en el
  teléfono: busca en internet, encadena pasos, programa temporizadores y reglas
  ("si el dormitorio pasa de 28°, prendé el aire"), crea escenas.
- **O IA gratis en tu computadora**, con [Ollama](https://ollama.com) o LM Studio:
  sin clave ni pagos, y tus órdenes no salen de tu casa. La app la encuentra sola
  en el WiFi y elige el modelo (recomendado: `qwen3`). En Ollama activa
  *Settings → Expose Ollama to the network*. Mientras la computadora esté prendida,
  todo funciona salvo buscar en internet.
- **Varios hogares** (tu casa, la de la playa) y **la familia invitada** con un código de un solo uso, cifrado.
- **Escenas y rutinas** que funcionan con la app cerrada: a una hora, al llegar o
  irte de casa, o cuando un aparato cambia.
- **Control infrarrojo** con el emisor del teléfono o un Broadlink: biblioteca de
  cientos de aires, teles y equipos.
- **Lo delicado espera tu confirmación**: abrir una cerradura o un portón, prender
  un horno.

## Marcas

Funciona con miles de dispositivos, y sumamos marcas todo el tiempo. Algunas por tu WiFi, sin internet; otras con la
cuenta de la marca.

- **Luces y enchufes:** Philips Hue y WiZ, TP-Link Kasa y Tapo, Shelly, Sonoff,
  Tasmota, Yeelight, Govee, LIFX, Nanoleaf, Smart Life / Tuya (Positivo, Steren,
  Nexxt, Lidl…), Belkin Wemo, IKEA DIRIGERA, deCONZ.
- **Teles y audio:** Samsung, LG, Philips, Android TV / Google TV, Fire TV, Roku,
  Vizio, Chromecast, Sonos, Denon / Marantz, Yamaha, Onkyo.
- **Clima:** aires con control remoto, Gree, Daikin, tado°, Netatmo, Google Nest,
  Bosch Smart Home, Homematic, FRITZ!DECT.
- **Electrodomésticos:** Bosch / Siemens (Home Connect), Electrolux / AEG, Miele,
  LG ThinQ, Samsung SmartThings, robots Roomba y Xiaomi.
- **Puertas y persianas:** Nuki, Tedee, Somfy TaHoma, Hunter Douglas PowerView,
  Legrand / BTicino.
- **Y todo lo que tengas en** Home Assistant, Zigbee2MQTT o SmartThings.

Lo que no tiene WiFi, Bluetooth ni control remoto no se puede manejar desde ningún
teléfono: la app te lo explica y te sugiere un enchufe inteligente.

## Opiniones y errores

- **[Contar cómo te fue](../../issues/new?template=opinion.yml)**: lo que te gustó, lo que no, ideas.
- **[Avisar de un error](../../issues/new?template=error.yml)**.
- **[Pedir una marca o un aparato](../../issues/new?template=marca.yml)**.
- O escribe a **rgiuliani@dosync.dev**.

Desde la app también puedes reportar una respuesta rara de la IA (Ajustes).

## Privacidad

Tus datos quedan en tu teléfono: DoSync no tiene servidores que los reciban.
[Política de privacidad](https://giulianireg-spec.github.io/dosync-adapters/privacidad/).

## Sobre este repositorio

Acá se publican las versiones para descargar, las novedades y las opiniones. El
código de la app no es público. DoSync App usa el
[protocolo abierto DoSync](https://dosync.dev), y el catálogo de adaptadores es
público en [dosync-adapters](https://github.com/giulianireg-spec/dosync-adapters).

Uso gratis según la [licencia](LICENSE). © 2026 Rodrigo Giuliani.
