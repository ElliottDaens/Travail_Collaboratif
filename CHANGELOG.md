# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

## [1.1.1] - 2026-01-28

### Corrigé
- **Autres/Correction_Exam.py** : Corrections et améliorations
  - Correction de la fonction `plus_grand()` : utilisation de `>=` au lieu de `>` pour gérer les cas d'égalité
  - Remplacement de `else: if` par `elif` pour un code plus pythonique
  - Correction de la faute de frappe `porgramme_1` → `programme_1`
  - Ajout de l'exécution automatique de `programme_3()` et `programme_4()` lors du lancement du fichier
  - Ajout de la fonction `programme_5()` pour la multiplication

## [1.1.0] - 2026-01-16

### Ajouté
- **TP_Python/Dataframe/** : Nouveau cours sur Pandas et les DataFrames
  - `dataframe.py` : Cours complet sur les Séries et DataFrames
  - `meteo_exemple.csv` : Fichier CSV d'exemple généré par le cours
  - Manipulation de données météorologiques
  - Accès aux données (loc, iloc, at, iat)
  - Filtrage et sélection conditionnelle
  - Ajout/suppression de colonnes
  - Lecture/écriture de fichiers CSV

## [1.0.0] - 2026-01-16

### Ajouté
- **TP1/** : Fichiers du TP Git (README, .gitignore, exemples)
- **TP_Python/variable_et_types_python.py** : Cours sur les variables et types de données
  - Entiers (int)
  - Flottants (float)
  - Booléens (bool)
  - Chaînes de caractères (str)
  - Listes, Dictionnaires, Tuples
  - DataFrames avec Pandas
- **TP_Python/script_et_structures.py** : Cours sur les scripts et structures de contrôle
  - Scripts Python et exécution
  - Structures conditionnelles (if, else)
  - Boucles for et while
  - Fonction range()
- **TP_Python/fonctions_et_fichiers.py** : Cours sur les fonctions et fichiers
  - Définition de fonctions (def, return)
  - Paramètres et valeurs par défaut
  - Visualisation avec matplotlib et plotly
  - Lecture de fichiers CSV avec Pandas
- **README.md** : Documentation du projet

---

## Guide de versioning

- **MAJOR** (1.x.x) : Changements incompatibles avec les versions précédentes
- **MINOR** (x.1.x) : Nouvelles fonctionnalités rétrocompatibles
- **PATCH** (x.x.1) : Corrections de bugs rétrocompatibles
