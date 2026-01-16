# 📚 Travail Collaboratif - Cours Python

Bienvenue dans ce repository contenant les cours et exercices Python pour l'apprentissage de la programmation.

## 📁 Structure du projet

```
├── TP1/                              # TP Git - Introduction au versioning
│   ├── README-GIT.md
│   ├── .gitignore
│   ├── contenus/
│   │   └── exemple.md
│   ├── fig/
│   │   └── image.png
│   └── principal.md
│
├── TP_Python/                        # Cours Python
│   ├── variable_et_types_python.py   # Cours 1 : Variables et types de données
│   ├── script_et_structures.py       # Cours 2 : Scripts et structures de contrôle
│   ├── fonctions_et_fichiers.py      # Cours 3 : Fonctions et fichiers
│   └── Dataframe/                    # Cours 4 : Pandas et DataFrames
│       ├── dataframe.py
│       └── meteo_exemple.csv
│
├── VERSION                           # Numéro de version actuel
├── CHANGELOG.md                      # Journal des modifications
└── README.md                         # Ce fichier
```

## 🐍 Contenu des cours Python

### Cours 1 : Variables et types de données
**Fichier** : `TP_Python/variable_et_types_python.py`

- Variables et affectation
- Types de données :
  - `int` : Entiers
  - `float` : Nombres décimaux
  - `bool` : Booléens
  - `str` : Chaînes de caractères
- Structures de données :
  - Listes
  - Dictionnaires
  - Tuples
  - DataFrames (Pandas)

### Cours 2 : Scripts et structures de contrôle
**Fichier** : `TP_Python/script_et_structures.py`

- Création et exécution de scripts Python
- Fonction `input()` pour la saisie utilisateur
- Structures conditionnelles :
  - `if` / `else`
- Boucles :
  - `for` avec `range()`
  - `while`
- Exercices pratiques

### Cours 3 : Fonctions et fichiers
**Fichier** : `TP_Python/fonctions_et_fichiers.py`

- Définition de fonctions (`def`, `return`)
- Paramètres et valeurs par défaut
- Visualisation avec Matplotlib et Plotly
- Lecture de fichiers CSV avec Pandas

### Cours 4 : Pandas et DataFrames ✨ *Nouveau*
**Dossier** : `TP_Python/Dataframe/`

- **Séries Pandas** : création, index, attributs
- **DataFrames** : tableaux 2D avec lignes et colonnes nommées
- **Accès aux données** : `loc`, `iloc`, `at`, `iat`
- **Filtrage** : sélection conditionnelle, tri
- **Modification** : ajout/suppression de colonnes
- **Fichiers** : lecture et écriture CSV

## 🚀 Installation

### Prérequis
- Python 3.x installé

### Bibliothèques nécessaires
```bash
pip install pandas numpy matplotlib plotly
```

## 💻 Utilisation

Pour exécuter un cours :
```bash
cd TP_Python
python variable_et_types_python.py
python script_et_structures.py
python fonctions_et_fichiers.py
python Dataframe/dataframe.py
```

## 📝 Versioning

Ce projet utilise le [Semantic Versioning](https://semver.org/lang/fr/).

| Version | Date       | Description                          |
|---------|------------|--------------------------------------|
| 1.1.0   | 2026-01-16 | Ajout du cours Pandas/DataFrames     |
| 1.0.0   | 2026-01-16 | Version initiale avec 3 cours Python |

- Voir le fichier `VERSION` pour la version actuelle
- Voir le fichier `CHANGELOG.md` pour l'historique des modifications

## 👤 Auteur

**Elliott Daens**
- GitHub : [@ElliottDaens](https://github.com/ElliottDaens)

## 📄 Licence

Ce projet est destiné à un usage éducatif.
