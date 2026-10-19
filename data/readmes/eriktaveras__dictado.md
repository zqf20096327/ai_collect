<p align="center">
  <img src="docs/images/icono.png" width="128" alt="Ícono de Dictado">
</p>

<h1 align="center">Dictado</h1>

<p align="center">
  <b>Mantén ⌃⇧, habla y suelta: el texto aparece donde esté el cursor, ya limpio.</b><br>
  Dictado por voz para macOS, pensado para el español. Todo se queda en tu Mac.
</p>

<p align="center">
  <a href="https://github.com/eriktaveras/dictado/releases/latest"><img src="https://img.shields.io/github/v/release/eriktaveras/dictado?label=descargar" alt="Última versión"></a>
  <img src="https://img.shields.io/badge/macOS-26%2B-black" alt="macOS 26 o superior">
  <img src="https://img.shields.io/badge/Apple%20Silicon-arm64-black" alt="Apple Silicon">
  <a href="LICENSE"><img src="https://img.shields.io/badge/licencia-MIT-green" alt="Licencia MIT"></a>
</p>

<p align="center">
  <b>Español</b> · <a href="README.en.md">English</a>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/images/2-escuchando-texto-oscuro.png">
    <img src="docs/images/2-escuchando-texto-claro.png" width="430" alt="El panel de Dictado mientras escucha">
  </picture>
</p>

El dictado de macOS escribe lo que dices tal cual lo dices: con los «eh», los «o
sea», sin puntuación y destrozando cada nombre técnico. Dictado transcribe en tu
Mac y después un modelo pequeño, también local, le quita las muletillas, arregla
la puntuación y escribe bien los nombres que tú le enseñes.

Los modelos que limpian dictado (los de superwhisper o SpeakoFlow, por ejemplo)
solo funcionan en inglés. Este funciona en español.

**Nada sale del Mac:** ni el audio ni el texto. No hay cuentas, ni telemetría, ni
servidores.

## Qué hace

| | |
|---|---|
| 🎙️ **Mantén y habla** | Mientras tengas ⌃⇧ pulsado, graba. Al soltar, pega. Esc cancela. |
| 🧹 **Texto limpio** | Fuera muletillas, repeticiones y tartamudeos; puntuación, tildes y mayúsculas en su sitio. Corrige, no reescribe. |
| 📖 **Tu vocabulario** | Un archivo con los nombres que el transcriptor nunca acierta (n8n, tu empresa, tus clientes). |
| 🤖 **Modo prompt** | Con ⌘ además, lo que dices se convierte en un prompt bien armado para ChatGPT, Claude o un agente de código. |
| 🛟 **Nunca pierdes un dictado** | Si el modelo tarda, falla o no está, se pega la transcripción cruda. |
| 🔇 **Te avisa si no se te oye** | Si el micrófono tiene la ganancia baja, el panel te dice cuál es y a qué porcentaje está. |

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/images/5-listo-oscuro.png">
    <img src="docs/images/5-listo-claro.png" width="430" alt="Texto ya limpio y pegado">
  </picture>
</p>

## Instalar

1. Descarga el `.dmg` de la [última versión](https://github.com/eriktaveras/dictado/releases/latest)
   y arrastra **Dictado** a Aplicaciones. Está firmado y notarizado por Apple.
2. Para que limpie el texto, instala [Ollama](https://ollama.com/download) y el modelo:
   ```sh
   ollama pull gemma4:e4b-mlx
   ```
   Sin Ollama, Dictado sigue funcionando: pega la transcripción tal cual.
3. Abre Dictado y concede los permisos que pide:
   - **Micrófono**, para oírte.
   - **Accesibilidad**, para el atajo global y para pegar el texto.

La primera vez, macOS descarga el modelo de voz del idioma elegido. Tarda un
poco y solo pasa una vez.

## Uso

| Acción | Atajo |
|---|---|
| Dictar | mantén **⌃⇧** (Control+Shift), habla y suelta |
| Prompt para una IA | mantén **⌃⇧⌘**, o añade **⌘** mientras hablas |
| Cancelar | **Esc** mientras grabas |

El atajo son solo modificadores, así que no le roba ninguna tecla a nada. Si
pulsas otra tecla con ⌃⇧ (⌃⇧→ para seleccionar, por ejemplo), el dictado se
cancela solo y el panel ni llega a aparecer.

Desde el ícono de la barra de menús eliges el modelo, el micrófono, el idioma,
si se pule el texto o no, y si se pega directamente o solo se copia al
portapapeles.

### Tu vocabulario

**Editar vocabulario…** en el menú abre un archivo de texto con los nombres que
quieres que el modelo escriba bien. Uno por línea, o varios separados por comas:

```
n8n, Ollama, Proxmox, Home Assistant
Taveras Solutions, Automatízate
```

Vale desde el siguiente dictado, sin reiniciar nada. El archivo está en
`~/Library/Application Support/Dictado/vocabulario.txt`.

### Modo prompt

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/images/9-prompt-listo-oscuro.png">
    <img src="docs/images/9-prompt-listo-claro.png" width="430" alt="Un dictado convertido en prompt">
  </picture>
</p>

Si mantienes también **⌘**, lo que dices no se pega tal cual: el modelo local lo
convierte en un prompt detallado. Una línea con la tarea y, solo si hay algo que
decir, **Contexto**, **Qué necesito**, **Evita** y **Entrega**. No se inventa
datos, y si falta algo imprescindible, el prompt termina pidiendo que te
pregunten antes de empezar.

## Cómo funciona

```
  ⌃⇧   ─────▶ micrófono ─▶ SpeechTranscriber ─▶ modelo de Ollama ─▶ ⌘V
mantén         AVAudio       (macOS 26,          (en tu Mac)        donde esté
 y habla        Engine        en tu Mac)                            el cursor
                              ~0,2 s             ~0,3 s
```

- **Transcripción:** `SpeechAnalyzer` + `SpeechTranscriber`, el motor de voz que
  trae macOS 26. Funciona en el equipo y en streaming, y no hace falta instalar
  Whisper.
- **Limpieza:** un modelo de Ollama al que se le pide corregir, no reescribir.
  Si el servidor de Ollama está dormido, Dictado lo despierta.

### Por qué `gemma4:e4b-mlx`

Comparativa con dictado real en español (mediana de 5 frases, MacBook Pro M5 Pro):

| Modelo | Mediana | Peor caso | Calidad |
|---|---|---|---|
| **gemma4:e4b-mlx** | **0,24 s** | 0,60 s | acierta los nombres técnicos |
| qwen3.8:27b-mlx | 1,41 s | 4,46 s | equivalente, seis veces más lento |
| qwen3.5:4b-mlx | 0,52 s | 1,45 s | apenas limpia: deja «eh, bueno, pues, ¿no?» |
| qwen3.5:2b | 0,39 s | 1,13 s | se inventa cosas: «Samba Board», «discos UFS» |

En el modo prompt se usa el mismo modelo, que ya está cargado y tarda entre 0,6
y 4 s. qwen3.8:27b escribía prompts algo mejores, pero tardaba de 5 a 21 s.

Puedes elegir cualquier otro modelo que tengas en Ollama desde el menú.

## Requisitos

- macOS 26 o superior (el motor de voz es de esta versión)
- Mac con Apple Silicon
- [Ollama](https://ollama.com), opcional, para pulir el texto

## Compilar desde el código

No hay proyecto de Xcode: es `swiftc` directo y sin dependencias.

```sh
git clone https://github.com/eriktaveras/dictado.git
cd dictado
./build.sh            # construye build/Dictado.app
./build.sh --install  # además lo copia a ~/Applications y lo abre
./package.sh          # arma dist/Dictado-<versión>.dmg
```

Si hay un Developer ID en el llavero, se firma con él y macOS no vuelve a pedir
los permisos en cada compilación. Sin él, se firma ad hoc.

### Diagnóstico

```sh
B=~/Applications/Dictado.app/Contents/MacOS/Dictado
$B --status                  # qué permisos y modelos faltan
$B --transcribe audio.wav    # el proceso completo por consola, sin micrófono
$B --prompt "texto"          # prueba el modo prompt
$B --preview ./previews      # un PNG por estado del panel, en claro y oscuro
```

Si algo no va, `~/Library/Logs/Dictado.log` cuenta qué pasó en cada dictado.

## Preguntas frecuentes

**¿Por qué no funciona en macOS 15?**
Porque el motor de transcripción (`SpeechTranscriber`) llegó con macOS 26. Antes
habría que meter Whisper, y la gracia es no instalar nada.

**¿Funciona en inglés?**
La transcripción sí: elige *Inglés (EE. UU.)* en **Idioma**. La limpieza tiene
las instrucciones escritas para el español y no se ha probado a fondo en inglés.
Si la pruebas, cuéntanos cómo va en un issue.

**El micrófono no me oye.**
Mira la ganancia de entrada en Ajustes del Sistema › Sonido. Por debajo del 50 %
el motor de voz suele devolver texto vacío, y Dictado te lo dice.

**¿Puedo cambiar el atajo?**
Todavía no desde el menú. Está en la lista.

## Contribuir

Los issues y PR son bienvenidos, en español o en inglés. Lee
[CONTRIBUTING.md](CONTRIBUTING.md).

## Licencia

[MIT](LICENSE) © 2026 Taveras Solutions LLC. Hecho por [Erik Taveras](https://github.com/eriktaveras).

Dictado no está afiliado a Apple ni a Ollama.
