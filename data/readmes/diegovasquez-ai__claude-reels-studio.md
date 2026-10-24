# Claude Reels Studio

**Grabas un reel con el celular. Claude Code hace el resto:**

- lo transcribe;
- lo edita con TU estilo;
- le pone subtítulos;
- arma la guía PDF que regalas;
- lo deja listo en Instagram y YouTube;
- entrega la guía por DM a cada persona que comenta tu palabra clave.

Tú solo grabas, revisas y apruebas. Funciona en Windows, Mac y Linux.

Hecho por [Diego Vásquez (@diegovasquez_ai)](https://www.instagram.com/diegovasquez_ai/). En sus primeros 4 reels con este sistema, la automatización recibió **677 comentarios con la palabra clave** y entregó **327 recursos por DM, sin responder ninguno a mano** ([detalle](docs/como-funciona.md#resultados-reales-del-autor)).

---

## Qué lo hace distinto

La mayoría de los editores con IA te dan una plantilla. Este sistema hace cuatro cosas más:

- **Aprende TU estilo.** Con `/configurar`, Claude analiza los reels que te funcionaron y escribe tu guía de estilo: gancho, subtítulos, stickers, B-roll, ritmo y CTA. Cada corrección que le das la suma. El estudio edita como tú, no como una plantilla.
- **Confirmas el texto antes de editar.** Whisper se equivoca con los nombres propios. Corriges una vez y el glosario aprende.
- **Va hasta el lead.** Publica en Instagram + YouTube y responde cada "Comenta PALABRA" con un DM que entrega el recurso.
- **Muestra lo real.** Si nombras una web o un documento, se ve ESA pantalla, animada como una grabación de pantalla, y siempre dentro de la zona segura de Instagram.

## Cómo funciona

```
Grabar ─► Subir ─► Confirmar texto ─► Edición ─► Subtítulos + portada ─► Guía PDF ─► Publicar ─► "Comenta PALABRA" → DM
 (tú)    Estudio       (tú)          Claude Code     Claude Code        Claude + Drive  (tu clic)     Zernio, 24/7
```

Paso a paso en [docs/como-funciona.md](docs/como-funciona.md).

## Requisitos

| Qué | Para qué | Cómo |
|---|---|---|
| **[Claude Code](https://claude.com/claude-code)** | Es el editor: escribe y revisa cada video | Plan Pro o Max de Claude (o API). Recomendado: el modelo más capaz (`/model`) |
| **Node.js 20+** | Correr el proyecto | [nodejs.org](https://nodejs.org) |
| **FFmpeg** | Audio, análisis y cortes | Windows: `winget install Gyan.FFmpeg` · Mac: `brew install ffmpeg` · Linux: `sudo apt install ffmpeg` |
| **Google Chrome** | Capturas de páginas para el B-roll y PDF de las guías | [google.com/chrome](https://www.google.com/chrome/) |
| **Git** | Clonar el repo | [git-scm.com](https://git-scm.com) |

## Instalación (5 minutos)

```bash
git clone https://github.com/diegovasquez-ai/claude-reels-studio.git
cd claude-reels-studio
npm install
claude
```

Dentro de Claude Code:

```
/start         ← comprueba que todo esté listo
/configurar    ← tu marca, tu estilo, tus cuentas y una prueba de punta a punta
```

`/configurar` te guía paso a paso y se puede retomar si lo cortas. Lo único que necesitas tener a mano son **2–5 reels tuyos que te hayan funcionado**, descargados como video. Si todavía no tienes, sirven reels de creadores que quieras imitar.

## Servicios externos (todos opcionales)

Sin ninguno, igual editas y renderizas. Cada uno suma una parte del flujo:

| Servicio | Qué suma | Costo | Sin él |
|---|---|---|---|
| **[OpenRouter](https://openrouter.ai)** | Transcripción en la nube en segundos (Whisper large-v3) | Menos de 1 centavo de dólar por reel | Transcribe en tu PC (gratis, más lento; descarga ~1.5 GB la primera vez) |
| **[Zernio](https://zernio.com)** | Publicar en Instagram + YouTube y la automatización "Comenta PALABRA" → DM | Revisa sus planes | Publicas a mano el MP4 |
| **Google Drive** (tu cuenta) | Las guías PDF se suben solas con link público | Gratis | Pegas tú el link del recurso |
| **[Higgsfield](https://higgsfield.ai)** | IA generativa en la edición: análisis de tus reels, predicción de retención, B-roll y portadas generadas, doblaje a otros idiomas | Créditos por generación | Todo lo demás funciona igual |

Las claves van en `.env.local` (copia `.env.example`). Ese archivo **nunca** se sube a GitHub y solo lo lee el servidor local del Estudio.

### OpenRouter (transcripción)

1. Crea una cuenta en [openrouter.ai](https://openrouter.ai) y carga un par de dólares.
2. Crea una key en [openrouter.ai/keys](https://openrouter.ai/keys).
3. En `.env.local`: `OPENROUTER_API_KEY=sk-or-...`

### Zernio (publicar + automatización de comentarios)

1. Crea tu cuenta en [zernio.com](https://zernio.com).
2. Conecta tu **Instagram** (cuenta profesional, con permisos de comentarios y mensajes) y tu **YouTube**.
3. Crea una API key en Zernio y ponla en `.env.local`: `api_zernio=...`
4. Abre el Estudio (`npm run estudio`) → **Ajustes** y comprueba que aparezcan tus cuentas.
5. En **Ajustes** escribe tus textos: el DM con el recurso, el "confirma que me sigues", las respuestas públicas y el link del segundo botón (tu lista de espera, grupo o web).

> **Ojo con Instagram:** desde agosto de 2026 no deja mandar botones a quien no te sigue. Por eso el flujo primero pide confirmar que te sigue y después entrega el recurso.

### Google Drive (guías PDF con link público)

Se hace una sola vez, en tu propia cuenta de Google:

1. En [console.cloud.google.com](https://console.cloud.google.com), crea un proyecto.
2. **APIs y servicios → Biblioteca** → busca **Google Drive API** → **Habilitar**.
3. **Pantalla de consentimiento de OAuth** (Google Auth Platform):
   - tipo **Externo**, con nombre de la app y tu correo;
   - después, en **Público**, toca **Publicar app**. Si queda "en prueba", el permiso caduca cada 7 días.
4. **Clientes → Crear cliente → App de escritorio** → descarga el JSON.
5. Pídele a Claude: "configura Drive con este JSON: `<ruta>`". Claude corre `drive.ts --credenciales`.
6. En el Estudio: **Ajustes → Conectar con Google** y autoriza.

El Estudio solo pide el permiso `drive.file`: ve únicamente los archivos que él mismo crea.

### Higgsfield (opcional)

```bash
claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp
```

Reinicia Claude Code, escribe `/mcp` y autoriza tu cuenta en el navegador (sin API key). Para qué sirve cada herramienta en la edición, y las reglas (Claude te muestra el costo antes de gastar créditos): [docs/higgsfield.md](docs/higgsfield.md).

## Tu primer reel

1. Graba un reel vertical (30–90 s).
2. `npm run estudio` → **Nuevo reel**: sube el video, escribe el tema y la palabra clave ("GUÍA") y el link del recurso, o deja que se arme una guía PDF.
3. En **Texto**, escucha y corrige lo que haga falta. Luego toca **Confirmar**.
4. En Claude Code escribe: `Edita el reel "<nombre>" del Estudio`.
5. Revisa el borrador en el Estudio. Pide cambios con el segundo ("en el 12 el sticker tapa mi cara") hasta que diga "este soy yo".
6. Di "aprobado": Claude pone los subtítulos, hace la portada y escribe los textos.
7. **Publicar → Subir a Zernio como borrador**. Revisa el borrador en Zernio y publícalo.

## Comandos de Claude Code

| Comando | Qué hace |
|---|---|
| `/start` | Comprueba dependencias, TypeScript, FFmpeg y tu configuración |
| `/configurar` | Marca, estilo desde tus reels, cuentas y prueba de punta a punta |
| `Edita el reel "<nombre>" del Estudio` | Edita un reel subido al Estudio con tu estilo |
| `/nuevo-video <idea>` | Video desde cero con plantillas (sin grabación) |
| `/editar-clip <ruta>` | Edita una grabación fuera del Estudio |
| `/subtitulos <ruta>` | Solo subtítulos (SRT o quemados) |
| `/lead-magnet <reel>` | Guía PDF con tu marca, subida a tu Drive |
| `/render <Composicion>` | MP4 final |

## Estructura

```
estilo/MI-ESTILO.md     tu estilo de reels (lo escribe /configurar; Claude lo lee antes de cada edición)
src/brand/brand.ts      tu marca: nombre, @, colores, logo (única fuente de verdad)
src/components/         subtítulos, stickers, logos, "pantalla grabada", terminal de Claude Code…
src/templates/          plantillas: reels, explainers, talking head, intro
src/compositions/       tus videos (crmreel/ = ejemplo real comentado)
estudio/                el Estudio: servidor (Express) + app (React)
scripts/                transcripción, capturas de webs, stills, pipeline, PDF de guías
guias/                  formato y estilos de las guías PDF
docs/                   cómo funciona, Higgsfield, prompts listos
.claude/commands/       /start, /configurar, /nuevo-video, /editar-clip, /subtitulos, /lead-magnet, /render
```

## Seguridad

- **Claves:** viven en `.env.local`, que está en `.gitignore`. Solo las usa el servidor local.
- **El Estudio:** escucha únicamente en `127.0.0.1`. No queda expuesto a internet.
- **Nada se publica solo:** subir a Zernio crea un **borrador**, y tú publicas.
- **Automatizaciones:** se crean o cambian solo con tu confirmación.
- **Higgsfield:** Claude te muestra el costo antes de gastar créditos.

## Licencias

- **El código de este repo:** licencia MIT (ver [LICENSE](LICENSE)).
- **[Remotion](https://remotion.dev):** tiene su propia licencia. Es **gratis para personas, organizaciones sin fines de lucro y empresas de hasta 3 empleados**. Las empresas más grandes necesitan una [Company License](https://www.remotion.pro).
- **Logos de herramientas en `public/logos`:** son marcas de sus dueños. Se usan solo para nombrar la herramienta en pantalla.
- **Efectos de sonido:** no vienen en el repo. `npm install` descarga los de Remotion ([remotion.media](https://remotion.media)) y genera el resto con FFmpeg (`scripts/descargar-sfx.ts`).

## Créditos

Creado por **Diego Vásquez** · [@diegovasquez_ai](https://www.instagram.com/diegovasquez_ai/). El estilo por defecto sale de su reel de referencia con 44k vistas, y el ejemplo `src/compositions/crmreel/` es un reel real suyo (sin sus videos).

Si lo usas y te sirve, cuéntamelo por Instagram: me encanta ver qué construyes.
