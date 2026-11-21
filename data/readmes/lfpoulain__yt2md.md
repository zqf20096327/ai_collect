<p align="center">
  <img src="docs/images/banner.svg" alt="YT2MD : transformez une chaîne YouTube en corpus texte, entièrement sur votre PC" width="100%">
</p>

<p align="center">
  <a href="LICENSE"><img alt="Licence MIT" src="https://img.shields.io/badge/licence-MIT-23563d"></a>
  <img alt="Windows 10/11" src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6?logo=windows&logoColor=white">
  <img alt="NVIDIA CUDA 12.8" src="https://img.shields.io/badge/NVIDIA-CUDA%2012.8-76B900?logo=nvidia&logoColor=white">
  <img alt="Node.js 24.2+" src="https://img.shields.io/badge/Node.js-24.2%2B-339933?logo=nodedotjs&logoColor=white">
  <img alt="Python 3.11–3.13" src="https://img.shields.io/badge/Python-3.11%E2%80%933.13-3776AB?logo=python&logoColor=white">
  <img alt="100 % local" src="https://img.shields.io/badge/inf%C3%A9rence-100%20%25%20locale-23563d">
</p>

<p align="center">
  <b>Transformez une chaîne YouTube en corpus texte exploitable par une IA, entièrement sur votre PC.</b>
</p>

YT2MD télécharge des vidéos YouTube, les transcrit mot à mot avec horodatage, décrit ce qu'on y voit à l'écran, puis exporte le tout en Markdown, JSON et JSONL, prêt à être injecté dans un RAG, un assistant ou un moteur de recherche. Aucune clé API, aucun service cloud : les modèles tournent sur votre carte graphique NVIDIA.

- 🎙️ **Transcription** avec Qwen3-ASR, langue imposée (français par défaut) et horodatage de chaque mot
- 👁️ **Analyse visuelle** avec Qwen3.5-9B : description de l'image et du texte affiché, toutes les 7 secondes
- 📚 **Bibliothèque par chaîne** : collez le lien d'une vidéo, d'une chaîne ou d'une playlist, cochez, transcrivez
- ⏸️ **Pause et reprise** à tout moment, même après redémarrage, sans refaire le travail déjà fait
- 📦 **Exports** Markdown lisible, JSON structuré, corpus JSONL et téléchargement ZIP
- 📈 **Journal en direct** avec barres de progression et temps restant, dans le terminal et dans l'interface

<p align="center">
  <img src="docs/images/screenshot-channel.png" alt="Page d’une chaîne : vidéos transcrites ou à traiter, sélection multiple" width="100%">
</p>

> Le téléchargement des vidéos et l'installation initiale des modèles nécessitent Internet. Toute l'inférence se fait ensuite en local.

## Sommaire

- [Aperçu](#aperçu)
- [Configuration requise](#configuration-requise)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Fichiers produits](#fichiers-produits)
- [Configuration](#configuration)
- [Fonctionnement détaillé](#fonctionnement-détaillé)
- [Journal du traitement](#journal-du-traitement)
- [Développement et tests](#développement-et-tests)
- [Crédits](#crédits)

## Aperçu

<p align="center">
  <img src="docs/images/pipeline.svg" alt="Pipeline : YouTube, yt-dlp et FFmpeg, puis Qwen3-ASR pour l’audio et Qwen3.5 pour l’image, fusionnés en Markdown, JSON et JSONL" width="100%">
</p>

<table>
  <tr>
    <td width="50%"><img src="docs/images/screenshot-library.png" alt="Bibliothèque : une carte par chaîne avec le nombre de vidéos transcrites"></td>
    <td width="50%"><img src="docs/images/screenshot-run.png" alt="Traitement en cours : progression vidéo par vidéo et journal en direct"></td>
  </tr>
  <tr>
    <td align="center"><b>Bibliothèque</b> : une carte par chaîne ou playlist</td>
    <td align="center"><b>Traitement</b> : pause, reprise et journal en direct</td>
  </tr>
</table>

<sub>Captures réalisées avec des chaînes fictives et des moteurs simulés (<code>npm run docs:screenshots</code>).</sub>

## Configuration requise

| Élément | Requis                                                                                                                 |
| ------- | ---------------------------------------------------------------------------------------------------------------------- |
| Système | Windows 10/11 (testé), 64 bits                                                                                         |
| GPU     | NVIDIA avec **au moins 10 Go de VRAM libre**, pilote compatible CUDA 12.8 (développé et mesuré sur une RTX 4090 24 Go) |
| Node.js | 24.2 ou plus récent                                                                                                    |
| Python  | 3.11 à 3.13 (3.12 conseillé)                                                                                           |
| FFmpeg  | `ffmpeg` et `ffprobe` accessibles dans le `PATH`                                                                       |
| Disque  | environ **15 Go** pour les modèles, plus les vidéos en cours de traitement                                             |

## Installation

```powershell
git clone https://github.com/lfpoulain/yt2md.git
cd yt2md
npm install
Copy-Item .env.example .env
npm run python:setup
npm run models:download
npm run doctor
```

- `python:setup` crée un environnement Python isolé dans `.venv` et y installe PyTorch 2.11 CUDA 12.8. Votre Python système n'est jamais modifié. Si un PyTorch CUDA compatible est déjà installé, `npm run python:setup -- --reuse-system-torch` évite de le télécharger à nouveau.
- `models:download` récupère Qwen3-ASR, son aligneur, Qwen3.5-9B quantifié en Q4_K_M et le moteur llama.cpp CUDA. Les fichiers sont vérifiés par SHA-256 et leurs révisions verrouillées.
- `doctor` vérifie les outils, CUDA et la présence des modèles.

## Utilisation

```powershell
npm run dev
```

Ouvrez <http://127.0.0.1:5174>. L'interface a trois pages :

- **Bibliothèque** : un champ unique accepte le lien d'une vidéo, d'une chaîne (`@nom`) ou d'une playlist. Une carte par chaîne indique les vidéos transcrites, en erreur et connues.
- **Page d'une chaîne** : les vidéos dans l'ordre YouTube, avec miniature, durée, vues et état. Filtres, recherche, sélection multiple, puis **Transcrire**. La suite de la chaîne se charge au défilement ou d'un coup avec **Charger toute la chaîne**.
- **Traitement** : avancement vidéo par vidéo, pause, reprise et journal en direct.

Pour une version compilée : `npm run build` puis `npm start`, l'interface est alors servie sur <http://127.0.0.1:3002>.

### Si YouTube bloque les téléchargements

Après de longues séries, YouTube peut répondre « Sign in to confirm you're not a bot » ou renvoyer des erreurs 429/403. Le traitement se met alors **en pause automatiquement** au lieu d'échouer sur toutes les vidéos restantes ; **Reprendre** relance celles qui manquent. Le blocage se lève en général en quelques heures. Pour l'éviter, ajoutez dans `.env` :

```env
YT_DLP_COOKIES_FROM_BROWSER=firefox
```

yt-dlp lira alors YouTube avec le compte connecté dans Firefox. Sous Windows, Chrome, Edge et Brave verrouillent leurs cookies : préférez Firefox ou un fichier exporté (`YT_DLP_COOKIES=cookies.txt`). Ce fichier contient vos identifiants de session : ne le partagez jamais.

## Fichiers produits

```text
outputs/
  video--ID.md          # Transcription et observations visuelles, lisibles
  video--ID.json        # Export structuré (schéma 2.0)
  video--ID.local.json  # Provenance détaillée : modèles, révisions, temps en millisecondes
```

Toutes les données restent dans le dossier du projet (`outputs/`, `cache/`, `logs/`, `models/`), qui sont ignorés par git. Le serveur refuse tout chemin de données qui en sortirait, y compris par lien symbolique.

### Format JSON

Les fichiers `video--ID.json` suivent le schéma 2.0 hérité du projet YT-RAG d'origine (`docs/corpus.schema.json`, exemple dans `docs/examples/video.json`) : `source`, `publicStats`, `youtubeDescription`, `transcript`, `visualSegments`, `quality`… Pour rester compatibles avec les consommateurs de ce schéma, quelques constantes historiques sont conservées telles quelles, comme `provenance.transcriptionSource: "gemini_video"`, alors qu'aucun service externe n'est appelé. `provenance.model` indique les modèles locaux réellement utilisés ; les détails complets sont dans `video--ID.local.json`, qui n'est pas incorporé au corpus JSONL.

Le JSON principal stocke les temps en secondes entières. Il n'y a pas de diarisation : `speaker` vaut `Indéterminé` et `speakerId` vaut `null`.

## Configuration

Toute la configuration passe par `.env`. Chaque réglage a une valeur par défaut, et [`.env.example`](.env.example) les liste tous, commentés et regroupés. Ne décommentez que ce que vous changez, puis redémarrez le serveur.

Réglages les plus utiles :

| Variable                      | Défaut  | Rôle                                                                                     |
| ----------------------------- | ------- | ---------------------------------------------------------------------------------------- |
| `ASR_LANGUAGE`                | `fr`    | Langue parlée imposée : `fr`, `en`, `de`, `es`, `it`, `pt`, `ru`, `zh`, `yue`, ou `auto` |
| `ASR_CONTEXT`                 | `title` | Transmet le titre et la chaîne au modèle pour mieux écrire noms propres et marques       |
| `ASR_COMPILE`                 | `true`  | Compile le décodeur audio : environ 2,8× plus rapide, rentable dès 8 minutes d'audio     |
| `VIDEO_GROUP_FRAMES`          | `7`     | Nombre d'images (1 par seconde) analysées ensemble                                       |
| `KEEP_MEDIA`                  | `false` | Conserve vidéos, WAV et captures après export                                            |
| `LOG_LEVEL`                   | `info`  | `debug` pour tout voir, `warn` ou `error` pour réduire                                   |
| `YT_DLP_COOKIES_FROM_BROWSER` | —       | Voir [Si YouTube bloque les téléchargements](#si-youtube-bloque-les-téléchargements)     |

Les binaires externes peuvent être indiqués avec `PYTHON_BINARY`, `YT_DLP_BINARY`, `FFMPEG_BINARY` et `FFPROBE_BINARY`.

## Fonctionnement détaillé

### Pipeline

| Étape                  | Traitement                                                                              |
| ---------------------- | --------------------------------------------------------------------------------------- |
| Catalogue              | yt-dlp : URL, titre, chaîne, date, description et statistiques publiques                |
| Téléchargement         | yt-dlp : vidéo jusqu'à 1080p et piste audio, en privilégiant la piste originale         |
| Préparation            | FFmpeg : audio mono 16 kHz et une capture JPEG par seconde, décodées par le GPU (NVDEC) |
| Transcription          | `Qwen/Qwen3-ASR-1.7B-hf` en BF16, langue imposée, silences écartés par Silero           |
| Horodatage des mots    | `Qwen/Qwen3-ForcedAligner-0.6B-hf` : alignement forcé de chaque mot, au pas de 80 ms    |
| Observations visuelles | `Qwen/Qwen3.5-9B` en GGUF Q4_K_M via llama.cpp CUDA : séquences vidéo de 7 s à 1 fps    |
| Export                 | JSON, Markdown déterministe et JSONL pour le corpus                                     |

Les modèles audio et vidéo ne sont jamais chargés en même temps : Qwen3-ASR et l'aligneur (environ 6 Go) traitent l'audio, sont déchargés, puis Qwen3.5 analyse l'image. Le worker exige 10 Gio de VRAM libre avant de charger Qwen3.5 ; fermez les autres applications gourmandes si besoin.

### Transcription

Qwen3-ASR accepte une **langue imposée** : sa réponse est préremplie avec la langue choisie, il ne peut donc pas basculer dans une autre langue au milieu d'une phrase, un défaut constaté avec d'autres modèles sur des vidéos françaises.

1. **Parole** : Silero détecte la parole dans chaque morceau de 60 s ; les silences ne sont pas envoyés au modèle.
2. **Contexte** : le titre et la chaîne aident à orthographier noms propres et marques.
3. **Budget** : le nombre de tokens est borné selon la durée. Une sortie qui l'atteint est traitée comme une boucle et relancée segment par segment, jamais exportée.
4. **Ponctuation** : un long segment sans ponctuation est redécoupé au plus grand silence et retranscrit.
5. **Horodatage** : l'aligneur donne le début et la fin de chaque mot, sans jamais modifier le texte reconnu.

Avec `ASR_COMPILE=true`, seul le décodeur de texte passe par `torch.compile`. La toute première compilation prend environ 5 minutes, puis environ 1 min 30 s à chaque lancement grâce au cache `cache/torch-compile`. Sans Triton, le worker transcrit sans compiler et le signale.

### Analyse visuelle

Les captures sont assemblées en un court MP4 sans perte et envoyées à Qwen3.5 comme une **vraie entrée vidéo**, avec la transcription du passage correspondant. Le modèle produit uniquement `title`, `visualDescription`, `screenText` et `uncertainties`, sous forme de JSON contraint par grammaire. Il ne réécrit jamais les paroles. Un JSON incomplet n'est jamais complété artificiellement : il est relancé une fois avec plus de marge, sinon signalé.

Sur une RTX 4090, ce moteur atteint environ **120 tokens/s**, soit 2 à 3 s par groupe de 7 images. Le protocole et les moteurs comparés sont dans [docs/VISION_PERFORMANCE.md](docs/VISION_PERFORMANCE.md) et [benchmarks/vision](benchmarks/vision/README.md). À 1 image par seconde, un élément affiché moins d'une seconde peut être manqué.

Le moteur Transformers reste disponible en repli : `VISION_BACKEND=transformers`, puis `npm run models:download -- vision`.

### Reprise et caches

Chaque morceau audio et chaque groupe vidéo terminé est sauvegardé. **Mettre en pause** arrête le worker et ses processus ; **Reprendre**, y compris après redémarrage, réutilise tout ce qui est en cache. Changer de modèle, de langue ou de réglage invalide uniquement les caches concernés : modifier les réglages visuels conserve les transcriptions audio.

Après un export réussi, les fichiers média temporaires sont supprimés ; les transcriptions en cache restent, ce qui permet de reconstruire les exports.

## Journal du traitement

Le terminal et la page **Traitement** affichent la même vue lisible, avec une barre de progression par étape :

```
17:06:23  ▶ Vidéo 1/1 · Titre de la vidéo  VIDEO_ID
17:06:28  ✓ Téléchargement terminé  4,1 s · 147 Mo
17:07:54  ◆ Transcription Qwen3-ASR  21 morceaux
17:09:55    Transcription    █████████░░░░░░░░░░░  42 %  9/21 · 09:01 / 20:08 · reste ~42 s
17:14:00    Analyse visuelle ██████████░░░░░░░░░░  50 %  87/173 · 10:09 / 20:08 · reste ~3 min 19 s
17:17:12  ▶ Vidéo terminée en 10 min 49 s  0,54 × la durée de la vidéo · audio 2 min 36 s · vision 6 min 41 s
```

Le détail technique (chaque appel FFmpeg, VRAM libre et allouée, débit de génération…) est enregistré en JSONL dans `logs/runs/`, et visible avec le filtre **Tous les messages techniques** ou `LOG_LEVEL=debug`. Les transcriptions et prompts ne sont pas recopiés dans le journal, et les clés et paramètres d'URL y sont masqués.

## Développement et tests

```powershell
npm run check            # typecheck, tests TypeScript et Python
npm run build
npm run smoke:media      # FFmpeg réel sur des clips générés
npm run smoke:processors # vrais processeurs audio/vidéo, sans les poids
npm run smoke:ui         # interface dans Edge avec moteurs simulés (après un build)
npm run docs:screenshots # régénère les captures du README (docs/images)
```

Les tests ne nécessitent pas les poids des modèles. Ils couvrent le schéma JSON, les exports, la bibliothèque, la pause et la reprise, les caches et les horodatages ; ils ne mesurent pas la qualité de transcription ou de vision.

Pour tester l'inférence réelle sur une vidéo déjà en cache :

```powershell
.venv\Scripts\python.exe -X utf8 scripts/smoke_asr.py --audio cache/ID/media/audio.wav --start 59 --seconds 62
.venv\Scripts\python.exe -X utf8 scripts/smoke_vision.py --video-id ID
```

Structure du code :

```text
server/   API, catalogue YouTube et exports (TypeScript, Express)
client/   Interface (React, Vite)
worker/   Pipeline audio et vidéo (Python, PyTorch, llama.cpp)
scripts/  Installation, diagnostic et vérifications
```

## Crédits

- [Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B-hf) et [Qwen3-ForcedAligner-0.6B](https://huggingface.co/Qwen/Qwen3-ForcedAligner-0.6B-hf) ([rapport technique](https://arxiv.org/abs/2601.21337))
- [Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B) et sa [conversion GGUF par Unsloth](https://huggingface.co/unsloth/Qwen3.5-9B-GGUF)
- [llama.cpp](https://github.com/ggml-org/llama.cpp), [yt-dlp](https://github.com/yt-dlp/yt-dlp), [FFmpeg](https://ffmpeg.org), [Silero VAD](https://github.com/snakers4/silero-vad), [Transformers](https://github.com/huggingface/transformers)

Les modèles sont soumis à leurs propres licences, consultables sur leurs fiches. Respectez les conditions d'utilisation de YouTube et les droits des créateurs des vidéos que vous traitez.

## Licence

[MIT](LICENSE)
