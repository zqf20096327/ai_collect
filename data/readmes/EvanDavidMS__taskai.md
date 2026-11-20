<div align="center">

<img src="src-tauri/app-icon-square.png" width="96" alt="Logo de TaskAI" />

# TaskAI

**Escribe como piensas. La IA lo ordena.**

Apuntes donde tú escribes rápido y desordenado, y una IA que corre **en tu propia computadora** te los devuelve ordenados, con tus pendientes y fechas, en vivo. Gratis y privado.

![Windows](https://img.shields.io/badge/Windows-10%20%2F%2011-0078D6?logo=windows&logoColor=white)
![IA local](https://img.shields.io/badge/IA_local-Ollama-111)
![Gratis](https://img.shields.io/badge/precio-gratis-2ea44f)
![Licencia GPL v3](https://img.shields.io/badge/licencia-GPL%20v3-blue)

</div>

---

## ¿Qué hace?

<p align="center">
  <img src="docs/capturas/demo.gif" width="860" alt="Escribes apuntes desordenados a la izquierda y la IA los ordena a la derecha, con pendientes y fechas" />
</p>

- ✍️ **Tu texto nunca se toca.** Escribes como quieras; la versión ordenada vive aparte.
- ⚡ **En vivo.** Cuando dejas de escribir unos segundos, la IA ordena tu nota y la ves escribirse.
- 📁 **Se acomoda sola** en su carpeta: Notas rápidas, Diario, Escuela, Trabajo, Hobbys o las que tú crees.
- ✅ **Pendientes con fecha y hora reales.** "El viernes a las 9" se vuelve "vie 20 nov · 9:00 AM". Todos tus pendientes, de todas tus notas, en una sola lista: *Atrasados, Hoy, Mañana, Esta semana…*
- 🔔 **Recordatorios** de Windows antes de cada pendiente con hora, y un resumen de tu día a las 8:00 AM.
- 🗓️ **Vista de semana** para tus pendientes, y puedes agregarlos a mano o cambiarles la fecha.
- ⭐ **Favoritas** arriba del tablero; **arrastra** una nota a cualquier carpeta.
- 🔎 **Busca en todo el texto**, sin importar acentos.
- 📤 **Exporta** a PDF o Markdown, o cópiala como texto para mandarla por WhatsApp.
- 🖼️ **Pega imágenes** con `Ctrl + V`.
- 🗑️ **Papelera** de 30 días: si borras algo por error, lo recuperas.
- 🎨 Modo claro u oscuro y 11 colores para elegir.
- 🔄 **Se actualiza solo**: te avisa cuando hay una versión nueva.
- 🔒 **100% privado.** La IA corre en tu computadora con [Ollama](https://ollama.com). Tus notas nunca se suben a internet.
- 📄 **Tus archivos son tuyos.** Cada nota es un archivo `.md` normal en `Documentos\TaskAI` (se abre con Obsidian, el Bloc de notas o lo que quieras).

### Capturas

| Tus notas | Una nota ordenada |
|---|---|
| <img src="docs/capturas/tablero-oscuro.png" alt="Tablero de notas en tarjetas, modo oscuro" /> | <img src="docs/capturas/nota-claro.png" alt="Apuntes a la izquierda y versión ordenada a la derecha, modo claro" /> |
| **Todos tus pendientes** | **Tu semana** |
| <img src="docs/capturas/pendientes-oscuro.png" alt="Pendientes agrupados en Atrasados, Hoy, Mañana y Esta semana" /> | <img src="docs/capturas/semana-claro.png" alt="Pendientes de la semana en columnas por día" /> |

---

## Instalación en Windows (5 minutos + la descarga de la IA)

### 1. Descarga TaskAI

Entra a **[Releases](../../releases/latest)** y descarga el archivo que termina en **`_x64-setup.exe`** (por ejemplo `TaskAI_1.2.0_x64-setup.exe`).

### 2. Instálalo

Abre el archivo y dale **Siguiente → Instalar**. No pide contraseña de administrador.

> **¿Te salió "Windows protegió su PC"?**
> Es normal en programas nuevos que todavía no tienen firma digital de pago. Pica **Más información → Ejecutar de todas formas**. TaskAI es de código abierto: puedes revisar todo el código aquí mismo.

### 3. Ábrelo: el asistente hace lo demás

La primera vez, TaskAI te guía en 6 pasos:

1. **Tu nombre.**
2. **Tema:** claro, oscuro o el de tu sistema.
3. **Dónde guardar tus notas** (por defecto `Documentos\TaskAI`).
4. **La IA:** si no tienes Ollama, pica **⬇ Instalar Ollama automáticamente** y TaskAI descarga la versión portátil oficial (≈1.5 GB) dentro de su propia carpeta y la enciende. Sin instaladores ni ventanas extra. Si ya tenías Ollama, TaskAI usa el tuyo.
5. **El modelo** (el "cerebro" de la IA). Elige uno y pica **⬇ Descargar y continuar**; verás una barra de progreso. Ve la tabla de abajo.
6. **¡Listo!** Escribe tu primera nota.

> La descarga del modelo es grande (2 a 9 GB) y solo se hace una vez. Después, TaskAI funciona **sin internet**.

### ¿Qué modelo elijo?

| Modelo | Tamaño | Para qué computadora |
|---|---|---|
| `qwen2.5:3b` · Ligero | 1.9 GB | 8 GB de RAM o sin tarjeta de video. Rápido, ordena un poco menos fino. |
| `qwen2.5:7b` · **Recomendado** | 4.7 GB | Tarjeta de video (NVIDIA/AMD) o 16 GB de RAM. El mejor equilibrio. |
| `qwen2.5:14b` · Potente | 9 GB | Tarjeta de video de 12 GB o 32 GB de RAM. El más inteligente, más lento. |

Lo puedes cambiar cuando quieras en **Configuración → Inteligencia artificial**.

---

## Si el asistente no pudo instalar la IA (instalación manual)

Solo si algo falló en el paso 4:

1. Descarga Ollama desde **<https://ollama.com/download/windows>** e instálalo (Siguiente → Instalar).
2. Abre **PowerShell** (búscalo en el menú Inicio) y pega:
   ```powershell
   ollama pull qwen2.5:7b
   ```
   Espera a que diga `success`.
3. En TaskAI ve a **Configuración → Inteligencia artificial** y pica **↻ Revisar**.

---

## Cómo se usa

- **Nueva nota** (`Ctrl + N`): escribe como te salga. El título es opcional; si lo pones, ayuda a la IA a elegir la carpeta.
- A los 3 segundos de dejar de escribir, la **versión ordenada** aparece a la derecha.
- **Pendientes** (menú de la izquierda): todo lo que tienes que hacer, de todas tus notas, ordenado por fecha. Pica el renglón para palomearlo.
- **📌 Fijar**: congela la versión ordenada para que la IA ya no la cambie sola. **Revisar** la actualiza cuando tú quieras.
- **Lectura** (`Ctrl + E`): esconde tus apuntes y deja solo la versión ordenada.
- **⏻ Encender/apagar la IA** (abajo a la izquierda). Apagarla libera la memoria de tu tarjeta de video.
- **⭐ Favoritas:** pica la estrella de una tarjeta para tenerla siempre arriba. **Arrastra** una tarjeta a una carpeta del menú para moverla.
- **Exportar** (en la nota): PDF, Markdown o copiar como texto.

### Atajos de teclado

| Atajo | Qué hace |
|---|---|
| `Ctrl + N` | Nueva nota |
| `Ctrl + K` | Buscar |
| `Ctrl + Enter` | Ordenar ahora |
| `Ctrl + E` | Escribir ⇄ Lectura |
| `Esc` | Volver a tus notas |
| `Ctrl + ,` | Configuración |
| `Supr` | Mandar a la papelera la tarjeta seleccionada |

---

## Preguntas frecuentes

<details>
<summary><b>¿Cuánto cuesta? ¿Necesito cuenta?</b></summary>

Nada y no. TaskAI y Ollama son gratis, no hay cuentas, suscripciones ni anuncios.
</details>

<details>
<summary><b>¿Mis notas se suben a internet?</b></summary>

No. La IA corre en tu computadora. Ve la [política de privacidad](#privacidad).
</details>

<details>
<summary><b>Windows Defender dice que TaskAI es un virus</b></summary>

Es un falso positivo (la detección `Trojan:Win32/Bearfoos.A!ml` es de "aprendizaje automático": adivina por cómo se porta el programa) y ya lo reportamos a Microsoft. Para recuperarlo: *Seguridad de Windows → Protección antivirus → Historial de protección*, busca TaskAI y elige **Permitir**. Desde la 1.4.1 se quitó lo que lo confundía, y más adelante vamos a solicitar la [firma de código](#política-de-firma-de-código-code-signing-policy) gratis para proyectos libres.
</details>

<details>
<summary><b>Dice "La IA está apagada"</b></summary>

Pica **Encender la IA** (o el botón ⏻ abajo a la izquierda). Por defecto, TaskAI enciende la IA al abrirse y la apaga al cerrarse; lo cambias en **Configuración → Inteligencia artificial → Encendido automático**.
</details>

<details>
<summary><b>La primera vez tarda mucho en ordenar</b></summary>

La primera nota de cada sesión carga el modelo en memoria (10 a 40 segundos). Después es mucho más rápido. Si siempre es lento, prueba el modelo **Ligero**.
</details>

<details>
<summary><b>No me llegan los recordatorios</b></summary>

- TaskAI tiene que estar abierto (puede estar minimizado).
- Revisa que estén activados en **Configuración → Recordatorios** y pica **Probar aviso**.
- En Windows, revisa que no tengas activado **No molestar** (Configuración de Windows → Sistema → Notificaciones).
</details>

<details>
<summary><b>¿Dónde están mis notas? ¿Cómo las respaldo?</b></summary>

En `Documentos\TaskAI` (o la carpeta que elegiste; la ves en **Configuración → General → Abrir**). Para respaldarlas o pasarlas a otra compu, copia la carpeta completa, incluida la carpeta oculta `.taskai` (ahí están las versiones ordenadas, imágenes y la papelera).
</details>

<details>
<summary><b>¿Cómo lo desinstalo?</b></summary>

Configuración de Windows → Aplicaciones → TaskAI → Desinstalar. Se borra el Ollama que descargó TaskAI y el desinstalador te pregunta:

1. **¿Borrar también los modelos de IA?** (varios GB). Solo pregunta si no tienes otro Ollama instalado: si lo tienes, los modelos son suyos y no se tocan.
2. **¿Borrar también tus notas?** Si dices que no, se quedan en `Documentos\TaskAI`.

Si marcas **borrar los datos de la app**, también se borra tu configuración. Así no queda nada en tu computadora.

Para liberar espacio sin desinstalar, puedes borrar los modelos que no uses en **Configuración → Inteligencia artificial** (botón de basura junto a cada modelo).
</details>

---

## Linux

En **[Releases](../../releases/latest)** hay tres formatos. Elige el de tu distro:

| Tu distro | Descarga | Cómo instalarlo |
|---|---|---|
| **Cualquiera** (Arch, EndeavourOS, Manjaro, etc.) | `TaskAI_<versión>_amd64.AppImage` | Dale permiso de ejecutar y ábrelo: `chmod +x TaskAI_*.AppImage && ./TaskAI_*.AppImage` |
| Ubuntu, Debian, Linux Mint, Pop!_OS | `TaskAI_<versión>_amd64.deb` | `sudo apt install ./TaskAI_*_amd64.deb` |
| Fedora, openSUSE | `TaskAI-<versión>-1.x86_64.rpm` | `sudo dnf install ./TaskAI-*.x86_64.rpm` |

- Las tres se **actualizan solas** como en Windows (con `.deb` y `.rpm` te pide tu contraseña al actualizar).
- En **Arch/EndeavourOS**, si el AppImage no abre, instala FUSE: `sudo pacman -S fuse2`.

**La IA (Ollama)** se instala aparte en Linux. El asistente de TaskAI te enseña los pasos de tu distro:

- **Arch / EndeavourOS:** `sudo pacman -S ollama ollama-vulkan && sudo systemctl enable --now ollama`
- **Otras distros:** `curl -fsSL https://ollama.com/install.sh | sh`

Luego elige y descarga el modelo desde TaskAI (o `ollama pull qwen2.5:7b`).

## macOS

Todavía no hay instalador para Mac. Puedes compilarlo tú (ver abajo) e instalar Ollama desde <https://ollama.com/download/mac>.

---

## Para desarrolladores

Necesitas [Rust](https://rustup.rs), [Node.js 20+](https://nodejs.org), [pnpm](https://pnpm.io) y los [requisitos de Tauri](https://tauri.app/start/prerequisites/) de tu sistema (en Windows: *Build Tools de Visual Studio* con "Desarrollo para el escritorio con C++").

```bash
git clone https://github.com/EvanDavidMS/taskai.git
cd taskai
pnpm install
pnpm tauri dev      # modo desarrollo
pnpm tauri build    # instaladores en src-tauri/target/release/bundle/
```

| Parte | Tecnología |
|---|---|
| App de escritorio | Tauri 2 + Rust (notas en disco, conexión con Ollama) |
| Interfaz | React 19 + TypeScript + Vite |
| IA | Ollama, modelos Qwen 2.5 locales |
| Markdown | `marked` + `DOMPurify` |

Detalles técnicos y decisiones de diseño en [`CLAUDE.md`](CLAUDE.md) y [`HANDOFF.md`](HANDOFF.md).

## Privacidad

Tus notas **nunca salen de tu computadora**: la IA (Ollama) corre en tu compu y TaskAI no tiene cuentas, anuncios ni estadísticas de uso. TaskAI solo se conecta a internet para esto:

| Cuándo | A dónde | Qué se manda | ¿Se puede apagar? |
|---|---|---|---|
| Al abrir TaskAI, para ver si hay versión nueva | `github.com/EvanDavidMS/taskai` (Releases) | Nada tuyo: solo se descarga `latest.json` | Sí: *Configuración → General → Versión* |
| Cuando tú instalas la IA desde el asistente | `github.com/ollama/ollama` (Releases) | Nada tuyo: se descarga Ollama | Solo pasa si tú lo pides |
| Cuando tú descargas un modelo | `registry.ollama.ai` (lo descarga Ollama) | Nada tuyo: se descarga el modelo | Solo pasa si tú lo pides |

Como cualquier descarga, esos sitios ven tu dirección IP. Sus políticas: [GitHub](https://docs.github.com/es/site-policy/privacy-policies/github-general-privacy-statement) y [Ollama](https://ollama.com/privacy).

## Política de firma de código (Code signing policy)

> **Próximamente.** TaskAI va a solicitar la firma de código gratis que [SignPath Foundation](https://signpath.org) da a proyectos de código abierto. Mientras tanto, los instaladores **no están firmados** (por eso Windows puede mostrar avisos). Cuando se apruebe, aquí dirá: *Free code signing provided by [SignPath.io](https://about.signpath.io), certificate by [SignPath Foundation](https://signpath.org).*

- Los instaladores (Windows y Linux) se compilan **en GitHub Actions** directamente desde el código de este repositorio ([workflow](.github/workflows/compilar.yml)), no en una computadora personal. Ahí mismo se firmarán.
- Se firmarán `taskai.exe` y el instalador `TaskAI_<versión>_x64-setup.exe`.
- **Autores y revisores (committers and reviewers):** [Evan](https://github.com/EvanDavidMS). Los cambios de otras personas (pull requests) los revisa él antes de aceptarlos.
- **Aprobadores (approvers):** [Evan](https://github.com/EvanDavidMS). Cada firma se aprueba a mano.
- Privacidad: ve la sección [Privacidad](#privacidad).

## Licencia

TaskAI es software libre bajo la licencia [GNU GPL v3](LICENSE) © 2026 Evan.

En pocas palabras:

- ✅ Puedes **usarlo gratis**, estudiar el código y **modificarlo** a tu gusto.
- ✅ Puedes **compartirlo**, con tus cambios o sin ellos, siempre que sea con **todo el código fuente** y bajo esta misma licencia (GPL v3), dando crédito al autor original.
- ❌ **No** puedes tomar TaskAI, cerrar el código y distribuirlo (ni venderlo) como un programa propio.

Las versiones hasta la 1.4.0 se publicaron con licencia MIT; desde la 1.4.1 aplica la GPL v3.

**Sonidos** (`public/sounds/`): `palomita.mp3`, `ordenada.mp3` y `recordatorio.mp3` son de [Pixabay](https://pixabay.com/sound-effects/) (Pixabay Content License: se pueden usar gratis dentro de apps, sin atribución obligatoria, pero no redistribuirse sueltos como sonidos). No están bajo la GPL.

### Nombre y logo

La licencia cubre el código, no la marca. El nombre **TaskAI** y su logo identifican la versión oficial de Evan: si publicas una versión modificada, ponle **otro nombre y otro logo** y aclara que no es la versión oficial.
