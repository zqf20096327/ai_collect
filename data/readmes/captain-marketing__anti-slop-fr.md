# Anti-Slop FR

Un skill pour écrire du contenu qui sonne humain, pas généré.

---

## Le problème

Les LLMs ont des tics. Des formules prévisibles, des structures mécaniques,
des rythmes reconnaissables. Ce n'est pas un problème de vocabulaire — c'est
un problème de patterns. Tu peux interdire "révolutionnaire" et "game-changer",
le texte restera générique si tu ne cassas pas les structures qui le trahissent.

Ce skill travaille sur les deux niveaux : les formules creuses **et** les
patterns structurels. Il est conçu pour être personnalisé avec ta propre voix.

![Anti-Slop FR](assets/social-preview.jpg)


---

## Structure

```
anti-slop-fr/
├── SKILL.md                    # Instructions principales
├── identity/
│   └── VOICE.md                # Ton profil éditorial — à personnaliser
├── references/
│   ├── blacklist.md            # Formules IA universelles à supprimer
│   └── structures.md           # Patterns structurels à éviter
├── examples/
│   └── transformations.md      # Avant/après illustrés
├── README.md
└── LICENSE
```

---

## Installation

### Claude Projects (claude.ai)

1. Créer un nouveau Project
2. Dans "Connaissances du projet", uploader tous les fichiers `.md`
3. Renseigner `identity/VOICE.md` avec ta voix
4. Le skill s'active automatiquement sur chaque contenu produit dans le projet

### Cowork / Claude Code

```bash
# Cloner dans ton espace de travail
git clone https://github.com/TON_USERNAME/anti-slop-fr.git .claude/skills/anti-slop-fr

# Ou en sous-module si tu veux le maintenir à jour
git submodule add https://github.com/TON_USERNAME/anti-slop-fr.git .claude/skills/anti-slop-fr
```

Dans ton `CLAUDE.md` :

```markdown
## Skills actifs

Charger et appliquer le skill anti-slop-fr pour tout contenu rédigé :
- `.claude/skills/anti-slop-fr/SKILL.md`
- `.claude/skills/anti-slop-fr/identity/VOICE.md`
- `.claude/skills/anti-slop-fr/references/blacklist.md`
- `.claude/skills/anti-slop-fr/references/structures.md`
```

### Instructions personnalisées (sans projet)

Copier le contenu de `SKILL.md` dans tes instructions personnalisées Claude.
Coller le contenu de `identity/VOICE.md` à la suite, une fois rempli.

---

## Personnalisation

**C'est l'étape essentielle.** Le skill générique supprime les marqueurs IA,
mais ne définit pas ta voix. Pour qu'il soit vraiment utile :

### 1. Renseigner `identity/VOICE.md`

Le fichier contient des sections à compléter :
- **Registre** : tutoiement / vouvoiement, ton dominant, humour
- **Expressions signature** : tes tournures récurrentes que l'IA ne doit jamais "corriger"
- **Interdits personnels** : tes propres tabous éditoriaux
- **Exemples de ta voix** : 2-3 extraits de tes meilleurs textes

Plus ce fichier est précis, plus le résultat ressemble à toi.

### 2. Enrichir `references/blacklist.md`

Ajouter tes propres formules bannies, spécifiques à ton secteur ou à ton style.

### 3. Enrichir `examples/transformations.md`

Ajouter des transformations tirées de tes propres textes. C'est la référence
la plus efficace pour calibrer le comportement du modèle.

---

## Ce que le skill détecte et corrige

**Formules creuses** — hyperboles vides, adverbes superflus, jargon creux,
ouvertures IA typiques, béquilles d'emphase, déclaratifs vagues.
→ `references/blacklist.md`

**Patterns structurels** — contrastes binaires formulaiques, listes négatives,
fausse agentivité, voix passive masquée, narrateur en survol, fragmentation
staccato, méta-commentaire, rythme monotone.
→ `references/structures.md`

---

## Scoring

| Dimension | Question | /10 |
|---|---|---|
| Directness | Le texte énonce ou annonce ? | |
| Rythme | Varié ou métronomique ? | |
| Confiance | Respecte l'intelligence du lecteur ? | |
| Authenticité | Sonne humain ? | |
| Densité | Quelque chose à couper ? | |

En dessous de 35/50 : réécrire.

---

## Inspiré de

- [stop-slop](https://github.com/hardikpandya/stop-slop) de Hardik Pandya — pour la structure et les patterns structurels
- [style-captain-marketing](https://captainmarketing.io) de Stéphane Truphème — pour l'angle personnalisation et la liste noire

---

## Contribuer

Pull requests bienvenues. En particulier :
- Nouveaux exemples de transformations
- Patterns IA non couverts
- Adaptations pour d'autres langues

---

## Licence

MIT
