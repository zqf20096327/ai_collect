<div align="center">
  <img src="packaging/assets/nox.png" width="78" height="78" alt="">
  <h1>Nox Monitor</h1>
  <p>Tu asistente de WhatsApp, desde una app de escritorio.</p>
  <p><strong>v1.0.1</strong> · Windows y Linux x64 · Instalador y portable</p>
  <p><a href="https://github.com/camilin7483/nox-monitor/releases/latest"><strong>Descargar Nox Monitor</strong></a></p>
</div>

<p align="center">
  <img src="docs/img/modelos.png" width="960" alt="Panel de modelos de Nox Monitor con Ollama y una respuesta verificada">
</p>

Nox vincula WhatsApp Web en un perfil de navegador dedicado. Desde el monitor puedes probar modelos, editar el prompt del sistema, añadir fuentes de referencia y elegir en qué conversaciones puede responder el bot.

## Instalar y conectar

| Sistema | Instalador | Portable |
| --- | --- | --- |
| **Windows x64** | [Descargar .exe](https://github.com/camilin7483/nox-monitor/releases/download/v1.0.1/Nox-Monitor-1.0.1-Windows-x64-Instalador.exe). Ábrelo y sigue el asistente. | [Descargar .zip](https://github.com/camilin7483/nox-monitor/releases/download/v1.0.1/Nox-Monitor-1.0.1-Windows-x64-Portable.zip). Extrae la carpeta y abre `Nox Monitor.exe`. |
| **Linux x64** | [Descargar .run](https://github.com/camilin7483/nox-monitor/releases/download/v1.0.1/Nox-Monitor-1.0.1-Linux-x64-Instalador.run). Dale permiso de ejecución y ábrelo. | [Descargar .tar.gz](https://github.com/camilin7483/nox-monitor/releases/download/v1.0.1/Nox-Monitor-1.0.1-Linux-x64-Portable.tar.gz). Extrae todo y abre `Nox Monitor`. |

Los paquetes incluyen Node.js y Python. Nox usa un navegador compatible del equipo o prepara Chromium en el primer inicio. La versión portable crea su carpeta `Datos` al lado del ejecutable. Las sumas SHA-256 están en la [publicación de v1.0.1](https://github.com/camilin7483/nox-monitor/releases/tag/v1.0.1).

1. Abre **Nox Monitor** y pulsa **Iniciar** si el bot está detenido. En WhatsApp del teléfono entra en **Dispositivos vinculados** y escanea el QR del navegador que abre Nox. El perfil conserva la sesión al reiniciar mientras WhatsApp mantenga el vínculo.
2. En **Modelos**, conecta **Ollama** o **LM Studio**, o añade tu clave de **OpenAI**, **Anthropic**, **Gemini**, **DeepSeek**, **OpenRouter** o de una API compatible con OpenAI. Busca los modelos que ofrece la conexión, prueba una respuesta y activa el perfil.
3. En **Instrucciones**, define el prompt del sistema y agrega fuentes de texto. Prueba el contexto que recupera Nox antes de activar respuestas. Autoriza los chats desde **Ajustes**.

<table>
  <tr>
    <td width="62%" valign="top"><img src="docs/img/resumen.png" alt="Pantalla de resumen de actividad del monitor"><br><sub>Resumen de actividad</sub></td>
    <td width="38%" valign="top"><img src="docs/img/instalador-windows.png" alt="Pantalla de bienvenida del instalador oficial de Nox Monitor para Windows"><br><sub>Instalador de Windows</sub></td>
  </tr>
</table>

## Estado de v1.0.1

| Verificado | Pendiente |
| --- | --- |
| En Linux se probó el inicio y la apertura de la pantalla QR en las dos ediciones. En Windows se probó el instalador, el arranque y la edición portable mediante Wine. | Falta validar la vinculación QR en Windows nativo y un envío completo con una cuenta de prueba. El instalador de Windows carece de firma digital. |
| Ollama y LM Studio generaron respuestas reales. Los adaptadores de nube se probaron con respuestas simuladas. | La generación en la nube requiere verificar con una clave válida para cada proveedor. El catálogo y los límites dependen de esa cuenta. |
| Las instrucciones recuperan fragmentos de texto por coincidencia de términos y los agregan al contexto de generación. | La recuperación actual admite fuentes de texto y tiene un presupuesto limitado de contexto. |

Nox automatiza la interfaz de WhatsApp Web y puede requerir ajustes cuando esa interfaz cambie. WhatsApp necesita conexión a Internet. Los modelos locales requieren su propio servidor y un modelo instalado. Los paquetes de esta versión son para equipos x64. Linux requiere una sesión gráfica y las bibliotecas del navegador.

## Datos y privacidad

El estado de vinculación, las claves configuradas y los datos de conversación se guardan en el perfil local. Un proveedor remoto recibe los mensajes y el contexto que Nox usa para generar la respuesta. Mantén la carpeta de datos en un lugar privado y comparte el archivo portable original cuando quieras entregar una copia limpia.

## Desarrollo

En Linux instala Node.js 24, Python 3.13 con Tk, Bash, `jq` y `flock`. Desde la raíz del repositorio:

```bash
npm ci
npm test
npx playwright install chromium
python3 monitor.py
```

Consulta el [historial de cambios](CHANGELOG.md) y las [instrucciones de empaquetado](packaging/README.md). Si reportas un problema, incluye la versión, el sistema y pasos con datos de ejemplo.
