# =============================================================================
# Pandas, Matplotlib et Seaborn
# =============================================================================
# Documentation : https://pandas.pydata.org/pandas-docs/stable/reference/index.html
#
# Un grand nombre de décisions repose sur le recueil préalable et l'analyse de données.
#
# Exemple : La DCE (Directive Cadre sur l'Eau) fixe des objectifs et méthodes pour 
# atteindre le "bon état" des eaux. Le bon état se définit par :
# - État écologique : écart aux "conditions de référence" (eau non influencée par l'homme)
# - État chimique : respect des NQE (Normes de Qualité Environnementales)
#
# Les données peuvent être prélevées à différentes échelles temporelles.
# Une donnée = couple (valeur, instant de prélèvement)
# Une série = ensemble de valeurs ordonnées temporellement (fréquence régulière)
#
# LIBRAIRIES :
# - numpy : vecteurs et tableaux numériques (optimisé pour le calcul matriciel)
# - pandas : manipulation de séries et tableaux avec types variés + nommage des index
# - polars : traitement de données de grand volume (https://pola.rs/)
# =============================================================================

# Import de la librairie pandas
import pandas

# =============================================================================
# LES SÉRIES (Series)
# =============================================================================
# Une Series est une structure de données unidimensionnelle avec des index nommés.
# Elle peut contenir des données de n'importe quel type (int, float, str, etc.)

print("=" * 60)
print("LES SÉRIES PANDAS")
print("=" * 60)

# Création d'une série avec des index personnalisés
# Les index sont les jours de la semaine (nommés explicitement)
# Les valeurs sont les températures maximales
temperatureMax = pandas.Series(
    [21, 22.5, 24, 31, 34, 24, 16],
    index=["mercredi", "jeudi", "vendredi", "samedi", "dimanche", "lundi", "mardi"]
)

# Création d'une deuxième série avec les mêmes index
temperatureMin = pandas.Series(
    [15, 14, 16, 20, 25, 14, 12],
    index=["mercredi", "jeudi", "vendredi", "samedi", "dimanche", "lundi", "mardi"]
)

# Séries avec index par défaut (0, 1, 2, ...)
# Si on ne spécifie pas d'index, pandas utilise des entiers automatiquement
dates = pandas.Series([
    "18/08/2024", "19/08/2024", "20/08/2024", "21/08/2024",
    "22/08/2024", "23/08/2024", "24/08/2024"
])

meteo = pandas.Series(["soleil", "pluie", "nuageux", "soleil", "soleil", "gris", "gris"])

# =============================================================================
# ATTRIBUTS D'UNE SÉRIE
# =============================================================================

print("\n--- Affichage de la série temperatureMax ---")
# Affiche toute la série avec ses index
print(temperatureMax)

print("\n--- Attribut .index : liste des index ---")
# Retourne l'objet Index contenant tous les noms d'index
print(temperatureMax.index)

print("\n--- Attribut .values : tableau des valeurs ---")
# Retourne un array numpy contenant uniquement les valeurs
print(temperatureMax.values)

print("\n--- Attribut .shape : dimensions de la série ---")
# Retourne un tuple (nombre d'éléments,)
print(temperatureMax.shape)

print("\n--- Fonction len() : nombre d'éléments ---")
# Retourne le nombre d'éléments dans la série
print(len(temperatureMax))

print("\n--- Série dates (index par défaut) ---")
print(dates)

print("\n--- Série meteo (index par défaut) ---")
print(meteo)

# =============================================================================
# IMPORTANCE DES INDEX POUR LES CALCULS
# =============================================================================
# Les index sont cruciaux car ils permettent d'aligner les données lors des calculs.
# Si un index n'existe pas dans une série, le résultat sera NaN (Not a Number).

print("\n" + "=" * 60)
print("CALCULS AVEC LES SÉRIES")
print("=" * 60)

# Cas 1 : Index par défaut (0, 1, 2, 3) - calcul direct position par position
a = pandas.Series([1, 4, 10, 5])
b = pandas.Series([21, 6, 10, 15])
print("\n--- Soustraction avec index par défaut ---")
print("a =", list(a))
print("b =", list(b))
print("b - a =")
print(b - a)
# Résultat : 21-1=20, 6-4=2, 10-10=0, 15-5=10

# Cas 2 : Index nommés mais dans un ordre différent
# Pandas aligne automatiquement selon les index !
a = pandas.Series([1, 4, 10, 5], index=["a", "b", "c", "d"])
b = pandas.Series([21, 6, 10, 15], index=["d", "b", "c", "a"])
print("\n--- Soustraction avec index nommés (ordre différent) ---")
print("a =", dict(a))
print("b =", dict(b))
print("b - a = (alignement automatique par index)")
print(b - a)
# Pandas aligne : a["a"]=1 avec b["a"]=15 → 15-1=14, etc.

# Cas 3 : Index partiellement différents → NaN pour les index manquants
a = pandas.Series([1, 4, 10, 5, 1], index=["a", "b", "c", "d", "e"])
b = pandas.Series([21, 6, 10, 15, 0], index=["d", "b", "c", "a", "f"])
print("\n--- Soustraction avec index partiellement différents ---")
print("a a les index:", list(a.index))
print("b a les index:", list(b.index))
print("b - a = (NaN pour les index non communs)")
print(b - a)
# "e" n'existe que dans a, "f" n'existe que dans b → NaN

# =============================================================================
# LES DATAFRAMES
# =============================================================================
# Un DataFrame est un tableau 2D avec des lignes (index) et des colonnes nommées.
# C'est la structure principale de pandas pour manipuler des données tabulaires.

print("\n" + "=" * 60)
print("LES DATAFRAMES")
print("=" * 60)

# Recréer les séries avec les mêmes index pour la concaténation
temperatureMax = pandas.Series(
    [21, 22.5, 24, 31, 34, 24, 16],
    index=["mercredi", "jeudi", "vendredi", "samedi", "dimanche", "lundi", "mardi"]
)
temperatureMin = pandas.Series(
    [15, 14, 16, 20, 25, 14, 12],
    index=["mercredi", "jeudi", "vendredi", "samedi", "dimanche", "lundi", "mardi"]
)
dates = pandas.Series(
    ["18/08/2024", "19/08/2024", "20/08/2024", "21/08/2024",
     "22/08/2024", "23/08/2024", "24/08/2024"],
    index=["mercredi", "jeudi", "vendredi", "samedi", "dimanche", "lundi", "mardi"]
)
meteo = pandas.Series(
    ["soleil", "pluie", "nuageux", "soleil", "soleil", "gris", "gris"],
    index=["mercredi", "jeudi", "vendredi", "samedi", "dimanche", "lundi", "mardi"]
)

# Création d'un DataFrame à partir d'un dictionnaire de séries
# Les clés du dictionnaire deviennent les noms des colonnes
df = pandas.DataFrame({
    "date": dates,
    "Tmax": temperatureMax,
    "Tmin": temperatureMin,
    "meteo": meteo
})

print("\n--- DataFrame créé ---")
print(df)

# =============================================================================
# INFORMATIONS DE BASE SUR UN DATAFRAME
# =============================================================================

print("\n" + "=" * 60)
print("INFORMATIONS SUR LE DATAFRAME")
print("=" * 60)

print("\n--- df.info() : informations générales ---")
# Affiche le type, le nombre de valeurs non-nulles, et la mémoire utilisée
df.info()

print("\n--- Dimensions du DataFrame ---")
# shape retourne (nombre_lignes, nombre_colonnes)
print(f"Dimension : {df.shape}")

print("\n--- Index (noms des lignes) ---")
print(f"Nom des index : {df.index}")

print("\n--- Colonnes (noms des variables) ---")
print(f"Nom des colonnes : {df.columns}")

print("\n--- df.describe() : statistiques descriptives (colonnes numériques) ---")
# count : nombre de valeurs, mean : moyenne, std : écart-type
# min, 25%, 50% (médiane), 75%, max : quartiles
print(df.describe())

print("\n--- df.describe(include='all') : statistiques pour toutes les colonnes ---")
# Inclut aussi les colonnes non-numériques (unique, top, freq)
print(df.describe(include='all'))

# =============================================================================
# ACCÈS AUX DONNÉES
# =============================================================================
# Fonctions principales : loc, iloc, at, iat

print("\n" + "=" * 60)
print("ACCÈS AUX DONNÉES")
print("=" * 60)

print("\n--- iloc[0] : accès par position (1ère ligne) ---")
# iloc utilise des indices entiers (comme les listes Python)
print(df.iloc[0])

print("\n--- loc['vendredi'] : accès par nom d'index ---")
# loc utilise les noms des index
print(df.loc['vendredi'])

print("\n--- iloc[0:2] : slicing par position (lignes 0 et 1) ---")
print(df.iloc[0:2])

print("\n--- Accès à une cellule unique ---")

# iat[ligne, colonne] : accès par position (entiers)
print(f"df.iat[0, 0] = {df.iat[0, 0]}")  # Ligne 0, Colonne 0

# at[index, colonne] : accès par nom
print(f"df.at['vendredi', 'Tmin'] = {df.at['vendredi', 'Tmin']}")

# Combinaison iloc + nom de colonne
print(f"df.iloc[1]['Tmin'] = {df.iloc[1]['Tmin']}")

# iat avec positions
print(f"df.iat[1, 2] = {df.iat[1, 2]}")  # Ligne 1, Colonne 2 (Tmin)

# =============================================================================
# SÉLECTION SELON DES CONDITIONS
# =============================================================================

print("\n" + "=" * 60)
print("SÉLECTION ET FILTRAGE")
print("=" * 60)

print("\n--- Tri par colonne : sort_values() ---")
# ascending=False : ordre décroissant (Z→A pour les chaînes)
print(df.sort_values(by="meteo", ascending=False))

print("\n--- Filtrage : df[condition] ---")
print("Lignes où Tmin > 17 :")
# La condition retourne un masque booléen, puis on sélectionne les lignes True
print(df[df['Tmin'] > 17])

print("\nLignes où Tmin == 14 :")
print(df[df['Tmin'] == 14])

print("\nLignes où meteo == 'soleil' :")
print(df[df['meteo'] == 'soleil'])

# =============================================================================
# AJOUT ET SUPPRESSION DE COLONNES
# =============================================================================

print("\n" + "=" * 60)
print("AJOUT ET SUPPRESSION DE COLONNES")
print("=" * 60)

print("\n--- Ajout d'une colonne 'ressenti' ---")

# Initialisation de la colonne avec une valeur par défaut
df['ressenti'] = 'froid'

# Modification conditionnelle avec loc
# Syntaxe : df.loc[condition, 'colonne'] = valeur

# Si Tmin > 24 → "caniculeDuNord"
df.loc[df['Tmin'] > 24, 'ressenti'] = 'caniculeDuNord'

# Si Tmin entre 17 et 24 → "chaud"
# & est l'opérateur ET pour les conditions (pas 'and')
# Chaque condition doit être entre parenthèses
df.loc[(df['Tmin'] > 17) & (df['Tmin'] <= 24), 'ressenti'] = 'chaud'

# Si Tmin < 14 → "glacial"
df.loc[df['Tmin'] < 14, 'ressenti'] = 'glacial'

print(df)

print("\n--- Suppression de la colonne 'ressenti' ---")

# Vérifier si la colonne existe avant de la supprimer
if 'ressenti' in df.columns:
    # drop() supprime une ligne ou colonne
    # axis=1 : supprime une colonne (axis=0 pour une ligne)
    # inplace=True : modifie le DataFrame directement (sans créer de copie)
    df.drop('ressenti', axis=1, inplace=True)
    print("Colonne 'ressenti' supprimée.")
else:
    print("'ressenti' n'existe pas dans le DataFrame")

print(f"Colonnes restantes : {list(df.columns)}")

# =============================================================================
# OPÉRATIONS COURANTES SUR LES COLONNES
# =============================================================================

print("\n" + "=" * 60)
print("OPÉRATIONS SUR LES COLONNES")
print("=" * 60)

print("\n--- Calcul de l'amplitude thermique (Tmax - Tmin) ---")
# On peut créer une nouvelle colonne à partir d'opérations sur d'autres colonnes
df['amplitude'] = df['Tmax'] - df['Tmin']
print(df)

print("\n--- Statistiques sur une colonne ---")
print(f"Température max moyenne : {df['Tmax'].mean():.2f}°C")
print(f"Température min moyenne : {df['Tmin'].mean():.2f}°C")
print(f"Amplitude moyenne : {df['amplitude'].mean():.2f}°C")
print(f"Jour le plus chaud : {df['Tmax'].idxmax()} ({df['Tmax'].max()}°C)")
print(f"Jour le plus froid : {df['Tmin'].idxmin()} ({df['Tmin'].min()}°C)")

# =============================================================================
# LECTURE ET ÉCRITURE DE FICHIERS
# =============================================================================

print("\n" + "=" * 60)
print("LECTURE ET ÉCRITURE DE FICHIERS")
print("=" * 60)

# Pour sauvegarder le fichier dans le même dossier que le script,
# on utilise os.path pour obtenir le chemin du script
import os

# __file__ contient le chemin du script Python actuel
# os.path.dirname() extrait le dossier contenant le fichier
# os.path.join() combine le dossier et le nom du fichier
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "meteo_exemple.csv")

# Sauvegarde du DataFrame en CSV
print("\n--- Sauvegarde en CSV ---")
df.to_csv(csv_path, index=True, sep=';')
print(f"Fichier créé : {csv_path}")

# Lecture d'un fichier CSV
print("\n--- Lecture d'un CSV ---")
try:
    df_lu = pandas.read_csv(csv_path, sep=';', index_col=0)
    print(df_lu)
except FileNotFoundError:
    print("Fichier non trouvé.")

# =============================================================================
# RÉSUMÉ DES FONCTIONS PRINCIPALES
# =============================================================================
#
# CRÉATION :
# - pandas.Series(data, index) : crée une série
# - pandas.DataFrame(dict) : crée un DataFrame à partir d'un dictionnaire
# - pandas.read_csv(fichier) : lit un fichier CSV
#
# INFORMATIONS :
# - df.info() : informations générales
# - df.describe() : statistiques descriptives
# - df.shape : dimensions (lignes, colonnes)
# - df.columns : noms des colonnes
# - df.index : noms des index
#
# ACCÈS :
# - df.loc[index, colonne] : accès par nom
# - df.iloc[i, j] : accès par position
# - df.at[index, colonne] : accès cellule par nom
# - df.iat[i, j] : accès cellule par position
#
# FILTRAGE :
# - df[condition] : sélection par condition
# - df.sort_values(by='col') : tri
#
# MODIFICATION :
# - df['nouvelle_col'] = valeurs : ajout de colonne
# - df.drop('col', axis=1) : suppression de colonne
# - df.loc[condition, 'col'] = valeur : modification conditionnelle
#
# FICHIERS :
# - df.to_csv(fichier) : sauvegarde en CSV
# - pandas.read_csv(fichier) : lecture CSV
# =============================================================================

