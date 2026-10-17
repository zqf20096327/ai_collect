<p align="left">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://shieldcn.dev/header/graph.svg?title=Indagis%20Studio&subtitle=Structurer%20un%20montage%20comme%20un%20r%C3%A9cit&align=left&mode=dark" />
    <img alt="Indagis Studio — structurer un montage comme un récit" src="https://shieldcn.dev/header/graph.svg?title=Indagis%20Studio&subtitle=Structurer%20un%20montage%20comme%20un%20r%C3%A9cit&align=left&mode=light" />
  </picture>
</p>

<p align="left">
  <a href="https://github.com/agtktID/indagis-montage/actions/workflows/ci.yml"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://shieldcn.dev/github/ci/agtktID/indagis-montage.svg?variant=secondary&mode=dark" />
    <img alt="État de l'intégration continue" src="https://shieldcn.dev/github/ci/agtktID/indagis-montage.svg?variant=secondary&mode=light" />
  </picture></a>
  <a href="LICENSE"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://shieldcn.dev/github/license/agtktID/indagis-montage.svg?variant=secondary&mode=dark" />
    <img alt="Licence MIT" src="https://shieldcn.dev/github/license/agtktID/indagis-montage.svg?variant=secondary&mode=light" />
  </picture></a>
  <a href="https://github.com/agtktID/indagis-montage/commits"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://shieldcn.dev/github/last-commit/agtktID/indagis-montage.svg?variant=secondary&mode=dark" />
    <img alt="Dernier commit" src="https://shieldcn.dev/github/last-commit/agtktID/indagis-montage.svg?variant=secondary&mode=light" />
  </picture></a>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://shieldcn.dev/badge/donn%C3%A9es-100%25%20locales-green.svg?variant=secondary&logo=false&mode=dark" />
    <img alt="Données 100 % locales" src="https://shieldcn.dev/badge/donn%C3%A9es-100%25%20locales-green.svg?variant=secondary&logo=false&mode=light" />
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://shieldcn.dev/badge/statut-alpha-orange.svg?variant=secondary&logo=false&mode=dark" />
    <img alt="Statut : alpha" src="https://shieldcn.dev/badge/statut-alpha-orange.svg?variant=secondary&logo=false&mode=light" />
  </picture>
</p>

### L'atelier qui vous dit ce qui manque à votre histoire, avant que le montage ne le révèle trop tard.

Vous avez quarante minutes de rushes et une timeline vide. Indagis Studio tient **la carte
de votre récit** — les 12 étapes du voyage du héros, rattachées aux timecodes réels de vos
fichiers — et applique **douze règles** qui disent où le récit cède.

Tout tourne sur votre machine. Aucun compte, aucun abonnement, aucune donnée qui part
ailleurs.

![De la liste des vidéos au diagnostic : l'acte II est sous-doté, et l'outil le dit](docs/captures/demo.gif)

---

## Le diagnostic, en une image

C'est la fonction qui porte le produit. Douze règles lisent votre carte et renvoient des
phrases comme celle-ci :

> L'acte II ne porte que 33 s de matière repérée, contre 53 s pour l'acte I. La méthode en
> fait la partie la plus longue : à ce rythme, le milieu sera le plus court, et c'est
> exactement là que le spectateur décroche.

![Le diagnostic signale un acte II sous-doté, et déplie les étapes concernées](docs/captures/diagnostic.png)

Chaque remarque porte les numéros des étapes en cause : on clique, le panneau s'ouvre.
Aucun modèle de langage n'intervient — ce sont des règles appliquées à vos notes et à vos
timecodes, donc la réponse est immédiate et toujours la même.

## Le problème

Le problème n'est pas technique : vous savez couper. C'est que vous ne savez pas encore
quelle histoire vous racontez, et vous le découvrirez au montage — trop tard, après six
heures sur un acte II qui ne tient pas.

| Vos outils actuels | Ce qu'ils savent faire | Ce qu'ils ignorent |
| --- | --- | --- |
| Resolve, Premiere | couper, étalonner, exporter | si votre récit tient debout |
| Notion, Trello | suivre où en est la fabrication | ce qu'il y a **dans** vos rushes |
| Un document de script | poser une intention | la confronter aux plans tournés |

Indagis Studio occupe l'espace entre les trois. Ce n'est ni un logiciel de montage, ni un
gestionnaire de tâches — et il n'écrit pas à votre place : il aide à **nommer** ce que
vous avez déjà filmé.

## Démarrer

Il faut **Node.js 22.22 ou plus** et **pnpm**.

```bash
git clone https://github.com/agtktID/indagis-montage.git
cd indagis-montage
corepack enable
pnpm install
pnpm dev
```

L'application s'ouvre sur `http://localhost:8080`. Choisissez **« Continuer comme
développeur local »** — aucun compte, aucun mot de passe.

![L'écran d'accueil : aucun compte à créer](docs/captures/accueil.png)

Le diagnostic, les exports et toute la bibliothèque fonctionnent **sans modèle de
langage**. Pour que l'agent du chat réponde, connectez-en un depuis l'interface : votre
clé Anthropic ou OpenAI, un modèle Ollama en local, ou les crédits gratuits de Builder.io.

## La carte narrative

Les 12 étapes en 3 actes. Votre courbe d'intensité en trait plein, celle de la méthode en
pointillé : **l'écart entre les deux est le diagnostic**.

![La carte narrative : les 12 étapes en 3 actes, et la courbe émotionnelle du montage](docs/captures/carte-narrative.png)

Une étape n'est « couverte » que si elle porte une note. Ni une intensité seule, ni des
marqueurs rattachés ne suffisent : on peut avoir la matière sans l'intention, et l'outil
le distingue.

## La grammaire de mouvement

121 chorégraphies de motion design déconstruites — découpage minuté, palette, recette
Remotion, recette HyperFrames, prompt de reconstruction.

Elles se trient **par étape du voyage**, et c'est tout l'intérêt : la question n'est pas
« montre-moi les transitions », mais « qu'est-ce qui sert mon climax ? ».

![La grammaire de mouvement : 121 recettes à trier par étape du voyage et par famille](docs/captures/mouvements.png)

Une règle y est inscrite : **l'impact est réservé à l'étape 8**. Le ressort amorti et le
dépassement ne sont justifiés qu'au climax ; les employer partout vole au climax ce qui le
distingue.

## Le carnet de marqueurs

Vos passages repérés, avec leurs timecodes réels et le nom du rush. Vous les réordonnez
selon le récit, pas selon la chronologie — c'est la différence entre un dérushage et un
montage.

![Le carnet de marqueurs, en ordre narratif ou chronologique](docs/captures/marqueurs.png)

Sortie en **CSV**, en **EDL d'assemblage** pour Resolve et Premiere, ou en chapitres
YouTube. Entrée par un bloc de dérushage collé, un CSV ou un EDL : une lecture à blanc
montre ce qui serait créé **et refusé**, ligne par ligne, avant d'écrire.

## La bibliothèque

Vos ressources rangées sur trois axes indépendants — **type** (ce que c'est), **catégorie**
(à quoi ça sert), **format** (quelle forme). Importables et exportables en CSV ou JSON.

<table>
<tr>
<td width="50%"><img alt="La bibliothèque de ressources, rangée par type, catégorie et format" src="docs/captures/bibliotheque.png" /></td>
<td width="50%"><img alt="Le catalogue de 550 prompts, à trier par catégorie, style et scène" src="docs/captures/catalogue-prompts.png" /></td>
</tr>
<tr>
<td><b>Vos ressources</b> — trois états : brouillon, générée, référence.</td>
<td><b>550 prompts livrés</b> — à trier par catégorie, style et scène.</td>
</tr>
</table>

## Comment on s'en sert

1. **Posez vos marqueurs** — un passage repéré dans un rush, avec son timecode.
2. **Rattachez-les aux 12 étapes.** Une étape peut rester vide : c'est une information,
   pas une faute.
3. **Écrivez ce que chaque étape doit faire.** Une phrase suffit.
4. **Demandez un diagnostic.** Il dit où ça cède, et chaque remarque déplie l'étape
   concernée.
5. **Montez.** Exportez en EDL, ou demandez un brief de composition pour un acte entier.

## Les deux thèmes

Le thème suit celui de votre système, et les deux sont tenus : couleurs d'actes, courbe et
barres de couverture sont redéfinies pour chacun, pas seulement assombries.

<table>
<tr>
<td width="50%"><img alt="La carte narrative en thème sombre" src="docs/captures/carte-narrative-sombre.png" /></td>
<td width="50%"><img alt="La grammaire de mouvement en thème sombre" src="docs/captures/mouvements-sombre.png" /></td>
</tr>
</table>

L'interface suit la langue de votre navigateur parmi onze. Le contenu de la méthode reste
en français en toutes langues : c'est un référentiel transcrit de sa source, pas de la
donnée traduisible.

> Ces captures **se refont à l'identique** : ce qu'elles montrent est du code, pas une
> base locale. Voir [`tools/captures/README.md`](tools/captures/README.md).

## Fabriquer des vidéos depuis vos cartes

L'agent peut transformer une carte narrative en composition vidéo. Deux moteurs sont
branchés comme **ponts locaux**, démarrés avec l'application.

| Moteur | Licence |
| --- | --- |
| [HyperFrames](https://github.com/heygen-com/hyperframes) | Apache-2.0 — proposé par défaut |
| [Remotion](https://www.remotion.dev) | source-available, **pas open source** |

Le rendu se fait **sur votre machine** : il faut Chrome et ffmpeg. Pour vérifier :

```bash
node tools/hyperframes-bridge/smoke-test.mjs
node tools/remotion-bridge/smoke-test.mjs
```

**Remotion est gratuit pour les particuliers, les associations et les entreprises de trois
salariés au plus** ; au-delà, une licence d'entreprise est requise
([remotion.pro/license](https://www.remotion.pro/license)). Indagis Studio ne le distribue
pas : le pont l'installe à la demande dans votre projet vidéo, et c'est à ce moment que
vous acceptez sa licence.

Les ponts exécutent des commandes sur votre machine. Ils sont volontairement étroits —
liste blanche de sous-commandes, jamais de shell, écritures confinées au dossier `video/`.
Pour vous en passer, supprimez `mcp.config.json` : l'application fonctionne sans.

## Sous le capot

Construit sur [Agent-Native](https://www.agent-native.com) (MIT), en application autonome.

```
actions/               47 actions — chacune est à la fois outil d'agent,
                       hook React, route HTTP et commande en ligne
server/db/             12 tables PostgreSQL (PGlite en local)
shared/                la méthode : 12 étapes, 3 actes, 5 questions, 5 symptômes
shared/prompt-catalog/ catalogue de 550 prompts, généré — voir tools/prompt-catalog/
shared/motion-grammar/ 121 recettes de mouvement, générées — voir tools/motion-grammar/
app/routes/            4 écrans : les vidéos, la fiche, le calendrier, la bibliothèque
.agents/               ce que l'agent sait faire
tools/                 les ponts vidéo et les générateurs de catalogues
```

La méthode vit dans `shared/hero-journey.ts`, pas en base : c'est du référentiel, pas de
la donnée utilisateur. Même principe pour les deux catalogues — livrés dans le code, donc
présents dès l'installation, et qu'on ne modifie qu'en les copiant.

### Vérifier

```bash
bash scripts/verifier.sh
```

Vingt-huit critères, chacun avec la commande qui le démontre, et une section finale sur ce
qui reste **non prouvé** — le script ne prétend pas que tout est vérifié quand ça ne l'est
pas. S'y ajoutent **267 tests**, dont le contrat d'écriture de chaque action contre une
vraie base.

## Documentation

| Document | Ce qu'il contient |
| --- | --- |
| [`CHANGELOG.md`](CHANGELOG.md) | Ce que chaque version apporte — la 0.1.0 est la première |
| [`docs/ETAT-DU-PROJET.md`](docs/ETAT-DU-PROJET.md) | Ce qui est fait, ce qui reste, et la commande qui reprouve chaque ligne |
| [`AGENTS.md`](AGENTS.md) | Le contrat technique, pour les agents comme pour les humains |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Les règles du projet et les portes à passer |
| [`CREDITS.md`](CREDITS.md) | L'attribution du contenu de tiers |
| [`SECURITY.md`](SECURITY.md) | Signaler une faille — **pas** par une issue publique |

## Licence

[MIT](LICENSE).

Le projet embarque du contenu de tiers conservé avec son attribution : 550 prompts sous
licence MIT, et la méthode narrative transcrite de sa source. Le détail est dans
[CREDITS.md](CREDITS.md).
