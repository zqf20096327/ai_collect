# 📘 Guía Completa: Claude Code Project Template

> Guía paso a paso para sacarle el máximo partido al template. Desde la instalación hasta casos de uso reales.

---

## ¿Qué es esto y para qué sirve?

Este template te da una **estructura de proyecto lista para trabajar con Claude Code** desde el primer minuto. En lugar de empezar desde cero cada vez que creas un proyecto, tienes:

- Un `CLAUDE.md` que le dice a Claude cómo funciona tu proyecto (stack, comandos, convenciones)
- **5 slash commands** que automatizan las tareas más repetitivas de documentación
- Plantillas de docs (`LOGS`, `CHANGELOG`, `MANUAL`) que se mantienen actualizadas solas

El resultado: Claude Code entiende tu proyecto desde el día 1, y tú pierdes mucho menos tiempo documentando.

---

## Requisitos previos

- [Claude Code](https://www.anthropic.com/claude-code) instalado en tu máquina
- Git (para clonar el template)
- Un proyecto nuevo o existente al que aplicarlo

---

## Instalación en 5 pasos

### Paso 1 — Clona el template

```bash
git clone https://github.com/Deibiz4/claude-code-template.git
cd claude-code-template
```

### Paso 2 — Copia los archivos de configuración a tu proyecto

```bash
# Ajusta la ruta a tu proyecto real
MI_PROYECTO=~/proyectos/mi-app

cp CLAUDE.md.template $MI_PROYECTO/CLAUDE.md
cp .claudeignore.template $MI_PROYECTO/.claudeignore
mkdir -p $MI_PROYECTO/.claude/commands $MI_PROYECTO/docs
```

### Paso 3 — Copia los slash commands

```bash
cp .claude/commands/* $MI_PROYECTO/.claude/commands/
```

### Paso 4 — Copia los templates de documentación

```bash
cp LOGS.md.template $MI_PROYECTO/docs/LOGS.md
cp CHANGELOG.md.template $MI_PROYECTO/docs/CHANGELOG.md
cp MANUAL.md.template $MI_PROYECTO/docs/MANUAL.md
```

### Paso 5 — Personaliza el `CLAUDE.md`

Abre `CLAUDE.md` en tu proyecto y rellena los campos marcados con `[REEMPLAZAR]`:

```markdown
# Nombre del proyecto: [REEMPLAZAR → ej: "API de pagos"]

## Stack
- Lenguaje: [REEMPLAZAR → ej: TypeScript / Node.js 20]
- Framework: [REEMPLAZAR → ej: Express 4]
- Base de datos: [REEMPLAZAR → ej: PostgreSQL + Prisma]

## Comandos
- Dev: [REEMPLAZAR → ej: npm run dev]
- Build: [REEMPLAZAR → ej: npm run build]
- Tests: [REEMPLAZAR → ej: npm test]

## Variables de entorno relevantes
- [REEMPLAZAR → ej: DATABASE_URL, API_KEY...]
```

Cuanto más detallado lo dejes, mejor entenderá Claude tu proyecto.

### Verificación

```bash
ls $MI_PROYECTO/CLAUDE.md \
   $MI_PROYECTO/.claudeignore \
   $MI_PROYECTO/.claude/commands/ \
   $MI_PROYECTO/docs/
```

Deberías ver: 2 archivos de configuración + 5 commands + 3 docs ✅

---

## Estructura final de tu proyecto

```
tu-proyecto/
├── CLAUDE.md                        ← Claude lo lee automáticamente al arrancar
├── .claudeignore                    ← Archivos que Claude ignorará
├── .claude/
│   └── commands/
│       ├── log-session.md           ← /log-session
│       ├── update-changelog.md      ← /update-changelog
│       ├── document-feature.md      ← /document-feature
│       ├── session-summary.md       ← /session-summary
│       └── new-version.md          ← /new-version
└── docs/
    ├── LOGS.md                      ← Registro de sesiones de trabajo
    ├── CHANGELOG.md                 ← Historial de cambios versionados
    └── MANUAL.md                    ← Documentación del proyecto
```

---

## Los 5 Slash Commands: cuándo y cómo usarlos

Los slash commands son atajos que ejecutas directamente en el chat de Claude Code escribiendo `/nombre-del-comando`.

### `/log-session`
**Cuándo:** Al terminar cada sesión de trabajo.

Genera automáticamente una entrada en `docs/LOGS.md` con:
- Fecha y hora
- Resumen de lo que se hizo
- Archivos modificados
- Decisiones técnicas tomadas

```
# En Claude Code:
/log-session
```

---

### `/update-changelog`
**Cuándo:** Tras completar cambios que merezcan quedar en el historial (nueva feature, bugfix, refactor importante).

Añade una entrada estructurada en `docs/CHANGELOG.md` siguiendo el formato [Keep a Changelog](https://keepachangelog.com/).

```
/update-changelog
```

---

### `/document-feature`
**Cuándo:** Después de implementar funcionalidad nueva.

Actualiza `docs/MANUAL.md` con la descripción de la nueva feature: qué hace, cómo se usa, parámetros, ejemplos.

```
/document-feature
```

---

### `/session-summary`
**Cuándo:** Justo antes de cerrar Claude Code, para tener un resumen rápido de la sesión.

Muestra en pantalla un resumen de todo lo hecho en la sesión actual: cambios, archivos tocados, próximos pasos.

```
/session-summary
```

---

### `/new-version`
**Cuándo:** Al preparar un release o bump de versión.

Consolida el CHANGELOG, actualiza el número de versión y genera un resumen del release listo para publicar.

```
/new-version
```

---

## Flujo de trabajo recomendado

```
Abres Claude Code
        │
        ▼
Claude lee CLAUDE.md automáticamente
(ya entiende tu stack, comandos y convenciones)
        │
        ▼
Trabajas: pides features, fixes, refactors...
        │
        ▼
Al terminar algo importante → /document-feature
        │
        ▼
Si hay cambio versionable → /update-changelog
        │
        ▼
Al cerrar la sesión → /log-session o /session-summary
        │
        ▼
Cuando preparas release → /new-version
```

---

## Casos de uso reales

### 🔧 Caso 1: Proyecto nuevo desde cero

Acabas de crear un proyecto en Next.js y quieres que Claude te ayude a desarrollarlo desde el día 1.

**Sin el template:**
- Claude no sabe qué comandos usas (`npm run dev`, `next build`...)
- No sabe tu estructura de carpetas
- No recuerda lo que hicisteis en sesiones anteriores
- Tienes que repetir contexto cada vez que abres Claude Code

**Con el template:**
```bash
# 1. Aplicas el template al proyecto
cp CLAUDE.md.template ~/proyectos/mi-nextjs-app/CLAUDE.md

# 2. Personalizas CLAUDE.md:
#    - Stack: Next.js 14, TypeScript, Tailwind, Prisma
#    - Dev: npm run dev
#    - Build: npm run build
#    - DB: PostgreSQL local en localhost:5432

# 3. Abres Claude Code en tu proyecto
claude

# Claude ya sabe todo desde el primer mensaje ✅
```

A partir de aquí, cada sesión empieza con Claude completamente contextualizado.

---

### 📦 Caso 2: API REST en mantenimiento

Llevas meses manteniendo una API. Múltiples desarrolladores tocan el código. Nadie documenta nada.

**Flujo con el template:**

```
Sesión de trabajo:
1. Arreglas un bug en el endpoint /payments
2. Añades validación de email al registro

Al terminar:
→ /document-feature   (documenta la validación en MANUAL.md)
→ /update-changelog   (añade el bugfix y la feature al CHANGELOG)
→ /log-session        (registra la sesión en LOGS.md)
```

Resultado: documentación siempre al día sin esfuerzo manual.

---

### 🚀 Caso 3: Preparar un release

Vas a publicar la versión `1.2.0` de tu librería.

```
# 1. Durante el sprint fuiste usando /update-changelog con cada cambio
# 2. Antes del release:

/new-version

# Claude consolida todos los cambios desde la última versión,
# genera las release notes y actualiza el número de versión en package.json
```

---

### 👥 Caso 4: Equipo con varios devs

Tres devs trabajan en el mismo proyecto. Cada uno usa Claude Code en local.

El `CLAUDE.md` está en el repositorio → todos tienen el mismo contexto para Claude.

Los `docs/LOGS.md` y `docs/CHANGELOG.md` se actualizan con cada PR → el equipo tiene un historial claro de decisiones técnicas.

---

## Personalización avanzada

### Editar un slash command existente

Los commands son archivos `.md` en `.claude/commands/`. Puedes editarlos directamente para adaptar el comportamiento:

```bash
# Ejemplo: personalizar qué incluye /log-session
nano .claude/commands/log-session.md
```

### Crear tu propio slash command

```bash
# Crea un nuevo archivo en la carpeta commands
touch .claude/commands/mi-comando.md
```

Escribe dentro qué debe hacer Claude cuando ejecutes `/mi-comando`. Es prompt puro en markdown.

### Ajustar `.claudeignore`

Similar a `.gitignore`. Añade patrones de archivos que no quieres que Claude indexe:

```
node_modules/
.env
*.log
dist/
coverage/
```

---

## Preguntas frecuentes

**¿Puedo aplicar el template a un proyecto que ya existe?**
Sí. Simplemente copia los archivos al proyecto. El `CLAUDE.md` no interfiere con tu código, y los docs se crean en una carpeta `docs/` aparte.

**¿El CLAUDE.md se sube al repositorio?**
Sí, y es recomendable. Así todo el equipo (y Claude en cualquier máquina) tiene el mismo contexto.

**¿Tengo que usar todos los slash commands?**
No. Úsalos según los necesites. Lo mínimo útil es `/log-session` al cerrar y `/update-changelog` tras cambios importantes.

**¿Funciona con cualquier lenguaje o framework?**
Sí. El template es agnóstico al stack. Solo tienes que describir el tuyo en `CLAUDE.md`.

**¿Se puede usar con proyectos en Python, Rust, Go...?**
Perfectamente. El valor está en el contexto que le das a Claude y en los slash commands, que funcionan independientemente del lenguaje.

---

## Contribuir

¿Tienes un slash command útil que no está en el template? ¿Mejoras para el `CLAUDE.md`?

1. Haz fork del repositorio
2. Crea una rama (`git checkout -b feature/mi-mejora`)
3. Haz commit de tus cambios
4. Abre un Pull Request

---

*Hecho para trabajar mejor con [Claude Code](https://www.anthropic.com/claude-code) · Template por [@Deibiz4](https://github.com/Deibiz4)*
