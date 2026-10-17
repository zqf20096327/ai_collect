# Second cerveau

> Construire, automatiser et faire vivre un second cerveau avec Claude Code.
> Le guide complet + des skills prêts à installer, en accès libre.

La plupart des seconds cerveaux sont des cimetières de notes. On capture, on range deux semaines, puis on abandonne.

Ce repo rassemble la méthode et les outils pour en construire un qui tient dans la durée : un système qui tourne sans que tu le touches, qui **apprend de ses propres erreurs**, et qui peut se partager avec ton équipe.

Tout est gratuit, en français, et mis à jour régulièrement.

---

## Ce que tu trouves ici

- **[Le guide](./GUIDE.md)** - la méthode complète, en trois temps : le construire, le rendre autonome, le faire vivre.
- **[Les skills](./skills/)** - des outils Claude Code prêts à installer pour automatiser ton vault.

Le repo grossit au fil du temps : de nouveaux skills sont ajoutés au fur et à mesure. Regarde le [CHANGELOG](./CHANGELOG.md) pour suivre les nouveautés.

---

## Le guide

Le guide se lit en trois temps :

1. **Le construire** - poser la structure qui colle à ton activité, pas le template d'un autre. Les 4 catégories de contexte, le rôle des fichiers d'instructions, les 3 questions pour adapter chaque dossier.
2. **Le rendre autonome** - déléguer la maintenance pour qu'il tienne. Les 4 couches d'un système auto-portant et les 9 workflows qui le font tourner.
3. **Le rendre vivant** - le faire progresser tout seul (il apprend de tes corrections) et l'ouvrir à ton équipe (le partage de dossiers).

Lire le guide : **[GUIDE.md](./GUIDE.md)**

---

## Les skills

Les skills sont des recettes réutilisables pour Claude Code. Chacun vit dans son dossier, avec ses instructions d'installation. Ils suivent les trois temps du guide : le construire, le rendre autonome, le rendre vivant.

### Le construire

**`ingest` - capturer sans créer de désordre.** Donne-lui une URL, un texte ou un transcript. Il apprend ta taxonomie en lisant la doc de ton vault, range le contenu au bon endroit avec une synthèse et les bons liens, et te montre tout avant d'écrire. L'acte de base d'un second cerveau.

→ [skills/ingest](./skills/ingest/)

### Le rendre autonome

**`daily` - le briefing du matin.** Il lit le contexte de ton vault (journal de la veille, note de la semaine, kanban), ajoute ton agenda et tes brouillons email si tu les as connectés, et te présente tes priorités du jour. Ton journal reste un journal, jamais une todo-list.

→ [skills/daily](./skills/daily/)

**`weekly` - le planning de la semaine.** Un planning hebdo narratif : bilan de la semaine écoulée, relecture de tes objectifs, choix de 3 à 5 priorités avec toi, tag des cartes concernées, purge des vieilles cartes terminées.

→ [skills/weekly](./skills/weekly/)

**`audit-second-cerveau` - garder ton vault sain.** Un audit de la santé de ton vault : écarts entre ta documentation et la réalité, dossiers qui dérivent, fichiers orphelins, conventions non respectées, contenus périmés. Un rapport trié par priorité et un score sur 100. Ton système ne dérive plus en silence.

→ [skills/audit-second-cerveau](./skills/audit-second-cerveau/)

### Le rendre vivant

**`harvester` - le second cerveau qui apprend de ses erreurs.** Un assistant qui, chaque nuit, relit tes sessions, repère les moments où tu as repris ou corrigé ton IA, et te propose le lendemain des améliorations de tes propres recettes. Tu valides ou tu refuses : il ne change jamais rien tout seul. Tu corriges une fois, le système retient.

→ [skills/harvester](./skills/harvester/)

**`revise-memory` - ranger ce que ton IA a appris.** L'autre moitié de la boucle d'apprentissage. Il vide ton inbox de mémoire (`MEMORY.md`) : chaque chose apprise en session est redispatchée au bon endroit de ton vault, consolidée en règle, ou supprimée.

→ [skills/revise-memory](./skills/revise-memory/)

---

## Installation

Prérequis :

- Un compte Claude avec Claude Code
- Un vault (Obsidian, VS Code, ou un simple dossier de fichiers Markdown)

Récupère le repo :

```bash
git clone https://github.com/ColinDargent/second-cerveau.git
```

Pour installer un skill : copie son dossier (`skills/<nom>/`) dans ton espace Claude Code, suis le `INSTALL.md` du skill (certains demandent une petite configuration, par exemple le chemin de ton vault), puis lance-le.

Chaque skill est **générique** : aucun chemin en dur, rien de spécifique à un vault particulier. Tu l'adaptes au tien via sa configuration.

---

## Pourquoi ce repo

Je construis des seconds cerveaux avec Claude Code depuis plusieurs mois, pour moi et pour les dirigeants, freelances et consultants que j'accompagne. Ce repo, c'est la méthode que j'aurais aimé avoir au départ, plus les outils que j'utilise au quotidien.

L'idée n'est pas de te vendre une structure à copier. C'est de te donner la méthode pour construire la tienne, et des briques concrètes pour démarrer.

---

## Aller plus loin

- **La communauté** - on échange les workflows, les patterns d'instructions et les retours d'expérience dans une communauté dédiée : [Forward sur Skool](https://www.skool.com/ai-professionals-9640/about)
- **Se faire accompagner** - chez Forward, on conçoit et on implémente ces systèmes avec (ou pour) les équipes : [forward-ai.fr](https://www.forward-ai.fr)

---

## Mises à jour et contributions

Ce repo est vivant. Mets-le en favori (`Star`) pour suivre les ajouts. Les retours et suggestions sont bienvenus via les issues.

## Licence

MIT - utilise, modifie et partage librement.
