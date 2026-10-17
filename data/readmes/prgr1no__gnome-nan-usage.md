<h1 align="center">NaN Usage</h1>

<p align="center">
  <em>La cuota de tu suscripción de <a href="https://nan.builders">NaN</a> en la barra superior de GNOME, al estilo del monitor de uso de Claude.</em><br>
  <sub>A GNOME Shell indicator for your nan.builders quota — usage per model, time to reset, and a burn-rate alert.</sub>
</p>

<p align="center">
  <img alt="Licencia GPL-2.0-or-later" src="https://img.shields.io/badge/licencia-GPL--2.0--or--later-blue.svg">
  <img alt="GNOME Shell 46–50" src="https://img.shields.io/badge/GNOME%20Shell-46%E2%80%9350-4A86CF.svg?logo=gnome&logoColor=white">
  <img alt="Estado: beta" src="https://img.shields.io/badge/estado-beta-orange.svg">
  <img alt="No oficial" src="https://img.shields.io/badge/no%20oficial-comunidad-lightgrey.svg">
</p>

Un botón en la barra con el icono de NaN, un anillo con el porcentaje del modelo
que peor va y los días que faltan para el reset. Al pulsarlo, un menú con una
barra por modelo (tokens usados frente al cap), la proyección del ritmo de
consumo y el consumo agregado de las últimas 24 h, el mes y 30 días.

## Capturas

<p align="center">
  <img src="screenshots/menu.png" alt="Menú de NaN Usage: una barra por modelo, proyección del ritmo y consumo agregado" width="380">
</p>
<p align="center"><sub>El menú, con datos de ejemplo. Arriba, el indicador en la barra.</sub></p>

<p align="center">
  <img src="screenshots/panel.png" alt="Indicador de NaN Usage en la barra superior de GNOME" width="300">
</p>

## Características

- **Un vistazo desde la barra.** Icono, anillo y porcentaje del modelo más
  cargado, más los días hasta el reset. Configurable a anillo, barra o solo texto.
- **Aviso por consecuencia, no por porcentaje.** Se pone en ámbar si al ritmo
  medio del periodo la cuota va camino de pasarse, y en rojo si se agotaría antes
  del reset dejándote bloqueado un buen rato. No espera a que estés al 90 %.
- **Una barra por modelo** con tokens usados, cap, restante y la proyección.
- **Consumo agregado** de 24 h, mes y 30 días (opcional, una petición más).
- **Sin OAuth.** Lee la API key de un fichero, la misma que usa el CLI `nan`.
- **Se porta bien con la API.** Si NaN falla y ya había datos, los conserva y lo
  dice; entre sondeos recalcula los «reset en …» sin tocar la red.

## Instalación

### En un comando

```sh
curl -fsSL https://raw.githubusercontent.com/prgr1no/gnome-nan-usage/main/scripts/install-online.sh | bash
```

Clona el código, compila el schema, deja una copia limpia y la activa. Luego
**cierra sesión y vuelve a entrar** (en Wayland, GNOME Shell solo carga el código
al iniciar sesión). ¿Prefieres leerlo antes de ejecutarlo? Está en
[`scripts/install-online.sh`](scripts/install-online.sh).

### Manual (desarrollo)

```sh
git clone https://github.com/prgr1no/gnome-nan-usage.git
cd gnome-nan-usage
./install.sh          # enlaza esta carpeta como extensión y la activa
```

`./install.sh copy` deja una copia limpia en vez de un enlace; `./install.sh
uninstall` la quita.

### Sin git

Descarga el código de la
[última release](https://github.com/prgr1no/gnome-nan-usage/releases/latest)
(botón «Source code»), descomprímelo y dentro de la carpeta ejecuta `./install.sh`.

## Requisitos

- **GNOME Shell 46 a 50.** Probada en 50.1 (Ubuntu 26.04, Wayland).
- **Una suscripción de NaN** con API key.

## La API key

La extensión lee la key de `~/.config/nan/api-key` (una sola línea). Es el mismo
fichero que usan el CLI `nan` y demás herramientas de la comunidad: una sola
fuente para toda la máquina. Para crearlo con permisos correctos:

```sh
mkdir -p ~/.config/nan
(umask 177; printf %s 'TU_API_KEY' > ~/.config/nan/api-key)   # queda en modo 600
```

La ruta se puede cambiar en los ajustes. La key **nunca** sale en logs ni en
mensajes de error.

## Ajustes

Desde ⚙ en el menú o en la app Extensiones. Claves del schema
`org.gnome.shell.extensions.nan-usage`:

| clave | qué hace | por defecto |
|---|---|---|
| `key-path` | fichero con la API key (`~` vale) | `~/.config/nan/api-key` |
| `panel-model` | qué modelo refleja el panel: `worst` (nivel y luego uso), `max` (mayor uso), `fixed` | `worst` |
| `panel-model-id` | modelo para `fixed` | `deepseek-v4-flash` |
| `panel-gauge` | `ring`, `bar` o `none` | `ring` |
| `show-icon`, `show-percentage`, `show-reset`, `show-model` | piezas del panel | sí, sí, sí, no |
| `hide-unused` | ocultar en el menú los modelos con cero uso | sí |
| `show-metrics` | línea de consumo 24 h / mes / 30 d (una petición más) | sí |
| `poll-seconds` | segundos entre sondeos (60 a 1800) | 300 |
| `panel-position`, `panel-index` | zona de la barra y hueco | `right`, 0 |
| `toggle-menu` | atajo para abrir el menú, p. ej. `<Super>n` | ninguno |

## Cómo funciona

La API de inferencia de NaN (`api.nan.builders/v1`, LiteLLM) no expone uso. El
backend del panel web, `cloud-api.nan.builders`, sí, con la misma key como
`Bearer`. Sus rutas salen del bundle JS del panel y **no tienen contrato
público**: pueden cambiar sin aviso.

| ruta | uso aquí |
|---|---|
| `GET /api/usage/quota` | `periodStart` y `models[]` con `tokensUsed`, `cap`, `remaining`, `periodEnd`; alimenta las barras |
| `GET /api/auth/me` | handle, región y tier de la cabecera; se pide una vez |
| `GET /api/metrics/usage` | consumo agregado 24 h / mes / 30 d, opcional |

- **Nivel por consecuencia.** Ámbar si el ritmo medio del periodo proyecta ≥ 75 %
  al reset; rojo si a ese ritmo la cuota se agota y el bloqueo duraría al menos un
  10 % del periodo. Los primeros días (menos del 5 % transcurrido) no se
  extrapola: la media es ruido.
- **La key se lee del fichero en cada sondeo** (es diminuto), así cambiarla no
  obliga a recargar. No se usan variables de entorno: GNOME Shell no hereda las
  del terminal.
- **Sondeo cada 5 minutos** por defecto, otro al abrir el menú y con «↻
  Actualizar», con un mínimo de 30 s entre peticiones.

## Desarrollo y pruebas

```sh
gjs -m tools/test-model.js   # modelo puro con datos sintéticos y reloj fijo
gjs -m tools/poll.js         # cuota real: lo mismo que calcularía la extensión
```

El indicador, el menú y las preferencias solo se ven dentro del shell. En Wayland
hay que cerrar sesión para cargar código nuevo; para iterar sin salir se puede
levantar un shell aparte con `dbus-run-session -- gnome-shell --wayland --devkit`.
Los errores de carga salen en:

```sh
journalctl --user -b -o cat /usr/bin/gnome-shell | grep -i nan-usage
```

Ver [CONTRIBUTING.md](CONTRIBUTING.md).

## Desinstalar

```sh
./install.sh uninstall
# o, si se instaló desde una release:
gnome-extensions uninstall nan-usage@prgr1no.github.io
```

## Privacidad

Todo el tráfico va de tu equipo a NaN, con tu key. La extensión no manda datos a
ningún otro sitio, no guarda histórico y no escribe la key en ninguna parte.

## Licencia

**GPL-2.0-or-later.** El esqueleto (botón de panel, anillo Cairo, barras y
proyección) deriva de
[Claude Code Usage Monitor](https://github.com/dvdstelt/ClaudeCodeUsage) de David
Boike (GPL-2.0), recortado: aquí no hay OAuth ni perfiles. Ver [LICENSE](LICENSE).

---

<sub>Proyecto de la comunidad, <strong>no oficial</strong>: no está afiliado ni
respaldado por nan.builders. «NaN» y su logotipo pertenecen a sus dueños; los
iconos derivan de su favicon público.</sub>
