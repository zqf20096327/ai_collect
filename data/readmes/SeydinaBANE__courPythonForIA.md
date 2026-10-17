# Python pour l'IA

Un cours de Python en français, pensé pour les personnes qui veulent apprendre le langage **dans le but de travailler avec l'intelligence artificielle** : manipuler des données, appeler des API de modèles, structurer un agent.

Chaque leçon est un notebook Jupyter court : une idée expliquée, puis un exemple exécutable que vous pouvez modifier. Les exemples s'appuient sur des cas concrets (un agent traducteur, un appel à un modèle de chat, un jeu de données) plutôt que sur des `foo` et des `bar`. Le dernier chapitre quitte le notebook pour assembler ces briques dans un vrai projet Python, organisé en fichiers `.py`.

## Prérequis

- Python 3.11
- [`uv`](https://docs.astral.sh/uv/) pour gérer l'environnement et les dépendances

## Installation

```bash
git clone <url-du-depot>
cd CourPythonForIA
uv sync
```

`uv sync` crée l'environnement `.venv` et installe les dépendances du cours : `numpy`, `pandas`, `matplotlib`, `requests` et `ipykernel`.

## Lancer les notebooks

```bash
uv run jupyter lab
```

Ouvrez ensuite le notebook de votre choix. Si Jupyter vous demande un noyau, choisissez **`courpythonforia (3.11.8)`** : tous les notebooks du cours tournent sur celui-ci.

## Programme

Les chapitres se suivent : chaque leçon ne réutilise que des notions déjà vues plus haut.

### 1. Variables — `variables/`
- `variables.ipynb` — déclarer une variable, écrire des commentaires

### 2. Types de données — `data-type/`
- `nombres.ipynb` — opérations de base, vérifier et convertir un type
- `chaine-de-caracteres.ipynb` — concaténation, f-strings, méthodes utiles
- `booléens.ipynb` — d'où viennent les booléens, les erreurs fréquentes

### 3. Contrôle du flux — `controle-flow/`
- `instructions-if.ipynb` — `if`, `if/else`, `if/elif/else`, conditions imbriquées

### 4. Fonctions — `fonctions/`
- `fonctions.ipynb` — créer et nommer une fonction, portée des variables
- `parametres.ipynb` — plusieurs paramètres, valeurs par défaut, arguments positionnels et nommés
- `valeurs-de-retour.ipynb` — `return` contre `print`, retourner plusieurs valeurs

### 5. Structures de données — `data-structure/`
- `listes.ipynb` — accès, parcours, tri, list comprehension
- `tuples.ipynb` — quand préférer un tuple à une liste
- `ensembles.ipynb` — opérations d'ensembles, test d'appartenance
- `dictionnaires.ipynb` — paires clé-valeur, parcours, usage typique en IA

### 6. Aller plus loin — `advanced/`
- `try-except.ipynb` — intercepter les erreurs, cas typique de l'appel d'API
- `classes/classes.ipynb` — votre première classe
- `classes/methode-et-attribut.ipynb` — attributs, méthodes, une classe d'agent IA
- `classes/heritage.ipynb` — réutiliser et spécialiser une classe

### 7. Librairies et API — `librairies-api/`
- `import-modules.ipynb` — `import`, alias, modules intégrés, installer un paquet tiers
- `travailler-avec-api.ipynb` — requêtes GET et POST, codes de statut, clés d'API
- `travailler-avec-les donnees.ipynb` — un exemple complet : récupérer des données d'API, les analyser avec `pandas`, les visualiser avec `matplotlib`, les sauvegarder en CSV

### 8. Python pratique — `projet-pratique/`
On assemble tout dans un projet fil rouge : une petite analyse de ventes.

- `index.md` — les quatre étapes du projet
- `structure-de-projet.md` — organiser un projet en dossiers (`data/`, `output/`, `main.py`, `helpers.py`)
- `chemins-python.ipynb` — chemins relatifs et absolus, `pathlib`
- `travailler-avec-fichier.ipynb` — lire un CSV, écrire et relire un JSON, créer un dossier
- `analyse-ventes/` — le projet complet : `main.py` lit `data/ventes.csv`, calcule les totaux et génère `output/rapport.json` ; `helpers.py` regroupe les fonctions réutilisables

Pour l'exécuter :

```bash
cd projet-pratique/analyse-ventes
uv run python main.py
```


