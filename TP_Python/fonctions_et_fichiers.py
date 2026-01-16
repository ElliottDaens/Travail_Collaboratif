# =============================================================================
# Python : les fonctions et fichiers
# =============================================================================
# Reading : https://pythonscript.readthedocs.io/introduction.html#scripts
#
# OBJECTIF DES FONCTIONS :
# L'objectif d'une fonction est de pouvoir réitérer un traitement sur plusieurs
# objets ou plusieurs fichiers sans réécrire les instructions déjà écrites.
#
# DÉFINITION :
# Une fonction en Python est un bloc de code qui effectue une tâche spécifique.
# - Elle se définit avec le mot-clé 'def', suivi du nom et des paramètres entre ()
# - Elle peut renvoyer une valeur avec 'return', ou ne rien renvoyer (procédure)
# - Python dispose de fonctions intégrées : abs(), all(), any(), len(), print()...
# - On appelle une fonction en utilisant son nom et en passant des arguments
# =============================================================================

# =============================================================================
# FONCTION SIMPLE SANS PARAMÈTRE ET SANS RETOUR (PROCÉDURE)
# =============================================================================

# 'def' définit une nouvelle fonction
# 'fonctionAfficheBonjour' est le nom de la fonction (choisissez un nom explicite)
# () contient les paramètres (ici aucun)
# ':' marque le début du bloc de la fonction
def fonctionAfficheBonjour():
    # Le corps de la fonction est INDENTÉ (4 espaces)
    # Cette fonction affiche simplement "bonjour"
    print("bonjour")

# Pour exécuter la fonction, on l'APPELLE par son nom suivi de ()
# Les parenthèses sont OBLIGATOIRES même sans argument
fonctionAfficheBonjour()
# Résultat : bonjour

# =============================================================================
# FONCTION VIDE AVEC 'pass'
# =============================================================================

# Parfois, on veut définir une fonction mais coder son contenu plus tard
# Python n'accepte pas un bloc vide, donc on utilise 'pass'
def fonctionQuiFaitRien():
    # 'pass' est un placeholder (espace réservé)
    # La fonction existe mais ne fait rien
    pass

# On peut quand même appeler la fonction (elle ne fait juste rien)
fonctionQuiFaitRien()

# ATTENTION : n'oubliez pas de coder la partie manquante un jour !

# =============================================================================
# FONCTION AVEC PARAMÈTRE ET RETOUR (return)
# =============================================================================
# Une fonction peut :
# - Recevoir des PARAMÈTRES (données en entrée)
# - Renvoyer un RÉSULTAT avec 'return' (donnée en sortie)

# Cette fonction convertit un angle en degrés vers une direction cardinale
# Paramètre : angle_deg (l'angle en degrés, de 0 à 360)
# Retour : une chaîne représentant la direction (N, NE, E, etc.)
def recherche_direction_vent(angle_deg):
    # Liste des 16 directions de la rose des vents
    # N = Nord, E = Est, S = Sud, W = West (Ouest)
    # NNE = Nord-Nord-Est, etc.
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", 
                  "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    
    # Calcul de l'index correspondant à la direction
    # 360 / 16 = 22.5 degrés par direction
    # round() arrondit à l'entier le plus proche
    # % len(directions) assure que l'index reste dans [0, 15]
    index = round(angle_deg / (360.0 / len(directions))) % len(directions)
    
    # 'return' renvoie la valeur au code appelant
    # La fonction s'arrête immédiatement après return
    return directions[index]

# Test de la fonction avec plusieurs angles
# On crée une liste d'angles à tester
angles = [0, 45, 90, 135, 180, 225, 270, 315, 360]

# On parcourt chaque angle et on affiche la direction correspondante
for angle in angles:
    # On APPELLE la fonction avec l'angle comme argument
    # La valeur retournée est utilisée dans la f-string
    print(f"Angle : {angle}°, Direction : {recherche_direction_vent(angle)}")

# Résultats attendus :
# Angle : 0°, Direction : N
# Angle : 45°, Direction : NE
# Angle : 90°, Direction : E
# Angle : 135°, Direction : SE
# Angle : 180°, Direction : S
# Angle : 225°, Direction : SW
# Angle : 270°, Direction : W
# Angle : 315°, Direction : NW
# Angle : 360°, Direction : N

# =============================================================================
# FONCTION AVEC PARAMÈTRE PAR DÉFAUT
# =============================================================================
# On peut définir une valeur par défaut pour un paramètre
# Si l'appelant ne fournit pas ce paramètre, la valeur par défaut est utilisée

# Import des bibliothèques nécessaires pour le graphique
import matplotlib.pyplot as plt  # Bibliothèque de visualisation
import numpy as np               # Bibliothèque de calcul numérique

# Fonction qui dessine la direction du vent sur un graphique
# Paramètres :
# - angle_deg : l'angle en degrés (obligatoire)
# - centre : coordonnées du centre (optionnel, défaut = (0, 0))
def dessiner_direction_vent(angle_deg, centre=(0, 0)):
    # Conversion de degrés en radians (les fonctions trigonométriques utilisent les radians)
    # np.deg2rad() convertit degrés → radians
    angle_rad = np.deg2rad(angle_deg)

    # Calcul des coordonnées du point d'extrémité de la ligne
    longueur_ligne = 1.0  # Longueur de la flèche
    
    # Formules trigonométriques pour calculer x et y
    # x = centre_x + longueur * cos(angle)
    # y = centre_y + longueur * sin(angle)
    end_point = (centre[0] + longueur_ligne * np.cos(angle_rad), 
                 centre[1] + longueur_ligne * np.sin(angle_rad))

    # Création d'une nouvelle figure de 6x6 pouces
    plt.figure(figsize=(6, 6))
    
    # Tracer la ligne de direction en rouge
    # [x_debut, x_fin], [y_debut, y_fin], 'r' = rouge, linewidth = épaisseur
    plt.plot([centre[0], end_point[0]], [centre[1], end_point[1]], 'r', linewidth=2)
    
    # Afficher le point central en bleu avec un marqueur rond
    plt.scatter(centre[0], centre[1], color='b', marker='o', label='Centre')
    
    # Définir les limites des axes x et y
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    
    # Garder les proportions égales (cercle reste cercle)
    plt.gca().set_aspect('equal', adjustable='box')
    
    # Ajouter un titre avec la direction du vent
    # On réutilise notre fonction recherche_direction_vent !
    plt.title(f"Direction du vent: {recherche_direction_vent(angle_deg)}")
    
    # Labels des axes
    plt.xlabel("Est")
    plt.ylabel("Nord")
    
    # Afficher une grille pour mieux visualiser
    plt.grid(True)

    # Ajouter les labels de la rose des vents autour du graphique
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    
    # Parcourir chaque direction (8 directions = tous les 45°)
    for i, direction in enumerate(directions):
        # Calculer l'angle en radians (i * 45°)
        angle_rad = np.deg2rad(i * 45)
        
        # Position du texte (à 1.3 du centre pour être à l'extérieur)
        x = centre[0] + 1.3 * np.cos(angle_rad)
        y = centre[1] + 1.3 * np.sin(angle_rad)
        
        # Ajouter le texte de la direction
        # ha='center' et va='center' centrent le texte horizontalement et verticalement
        plt.text(x, y, direction, ha='center', va='center')

    # Afficher la légende
    plt.legend()
    
    # Afficher le graphique
    plt.show()

# Test de la fonction avec un angle de 45 degrés
# Le centre utilise la valeur par défaut (0, 0)
print("\n--- Dessin de la direction du vent (45°) ---")
dessiner_direction_vent(45)

# =============================================================================
# VISUALISATION AVANCÉE AVEC PLOTLY
# =============================================================================
# Plotly est une bibliothèque de visualisation interactive
# px.bar_polar crée un graphique en barres polaires (rose des vents)

print("\n--- Représentation du vent via Plotly ---")

# Import de plotly express (version simplifiée de plotly)
import plotly.express as px

# px.data.wind() charge un jeu de données exemple sur les vents
# Ce dataset contient : direction, strength (force), frequency (fréquence)
df = px.data.wind()

# Création d'un graphique en barres polaires
# r="frequency" : la longueur des barres représente la fréquence
# theta="direction" : l'angle représente la direction du vent
# color="strength" : la couleur représente la force du vent
# template="plotly_dark" : thème sombre pour le graphique
# color_discrete_sequence : palette de couleurs (Plasma inversée)
fig = px.bar_polar(df, r="frequency", theta="direction",
                   color="strength", template="plotly_dark",
                   color_discrete_sequence=px.colors.sequential.Plasma_r)

# Afficher le graphique interactif
# (s'ouvre dans le navigateur ou dans le notebook)
fig.show()

# =============================================================================
# LECTURE DE FICHIERS CSV AVEC PANDAS
# =============================================================================
# CSV = Comma Separated Values (valeurs séparées par des virgules)
# Pandas permet de lire facilement ces fichiers en DataFrame

print("\n--- Lecture de fichiers CSV avec Pandas ---")

# Import de la bibliothèque pandas
import pandas

# Source des données :
# https://www.data.gouv.fr/fr/datasets/r/491c12b5-2926-4791-a8fb-ca55815315f9
# Données météo : hauteur des précipitations, vitesse moyenne du vent,
# moyenne des températures min/max, tension de vapeur moyenne,
# cumul du rayonnement global, durée d'insolation et ETP Penman.

# read_csv() lit un fichier CSV et le convertit en DataFrame
# Paramètres :
# - chemin du fichier (ou URL)
# - sep=';' : le séparateur est un point-virgule (pas une virgule)
# Note : téléchargez le fichier depuis data.gouv.fr et placez-le dans le même dossier
try:
    df = pandas.read_csv("Q_62_latest-2023-2024_RR-T-Vent.csv", sep=';')
    
    # df.info affiche des informations sur le DataFrame
    # (nombre de lignes, colonnes, types de données, mémoire utilisée)
    print("\n--- Informations sur le DataFrame ---")
    print(df.info)
    
    # df.columns affiche la liste des noms de colonnes
    print("\n--- Colonnes du DataFrame ---")
    print(df.columns)
    
    # Explication des colonnes principales :
    # NUM_POSTE : numéro de la station météo
    # NOM_USUEL : nom de la station
    # LAT, LON : latitude et longitude
    # ALTI : altitude
    # AAAAMMJJ : date au format YYYYMMDD
    # RR : hauteur des précipitations (mm)
    # TN : température minimale (°C)
    # TX : température maximale (°C)
    # TM : température moyenne (°C)
    # FFM : vitesse moyenne du vent (m/s)
    # Les colonnes commençant par Q sont des codes qualité
    
    # df.describe() affiche des statistiques descriptives
    # (moyenne, écart-type, min, max, quartiles)
    print("\n--- Statistiques descriptives ---")
    print(df.describe())
    
except FileNotFoundError:
    print("ATTENTION : Le fichier 'Q_62_latest-2023-2024_RR-T-Vent.csv' n'a pas été trouvé.")
    print("Téléchargez-le depuis :")
    print("https://www.data.gouv.fr/fr/datasets/r/491c12b5-2926-4791-a8fb-ca55815315f9")
    print("et placez-le dans le même dossier que ce script.")

# =============================================================================
# RÉSUMÉ SUR LES FONCTIONS
# =============================================================================
# 
# DÉFINIR une fonction :
# def nom_fonction(param1, param2=valeur_defaut):
#     # instructions
#     return resultat  # optionnel
#
# APPELER une fonction :
# resultat = nom_fonction(arg1, arg2)
#
# AVANTAGES des fonctions :
# - Réutilisation du code (DRY : Don't Repeat Yourself)
# - Code plus lisible et organisé
# - Facilite les tests et le débogage
# - Permet de diviser un problème complexe en sous-problèmes
#
# BONNES PRATIQUES :
# - Nommer les fonctions de manière explicite (verbe + nom)
# - Une fonction = une tâche spécifique
# - Documenter les paramètres et le retour
# - Éviter les effets de bord (modifier des variables globales)
# =============================================================================

# =============================================================================
# EXERCICES SUPPLÉMENTAIRES
# =============================================================================

print("\n--- EXERCICE : Fonction de calcul de moyenne ---")

# Exercice : créer une fonction qui calcule la moyenne d'une liste de nombres
def calculer_moyenne(liste_nombres):
    """
    Calcule la moyenne arithmétique d'une liste de nombres.
    
    Paramètre :
        liste_nombres : liste de nombres (int ou float)
    
    Retour :
        float : la moyenne des nombres
    """
    # Vérification que la liste n'est pas vide
    if len(liste_nombres) == 0:
        return 0
    
    # sum() calcule la somme de tous les éléments
    # len() donne le nombre d'éléments
    # La moyenne = somme / nombre d'éléments
    return sum(liste_nombres) / len(liste_nombres)

# Test de la fonction
notes = [12, 15, 8, 17, 14]
moyenne = calculer_moyenne(notes)
print(f"Notes : {notes}")
print(f"Moyenne : {moyenne}")

# =============================================================================

print("\n--- EXERCICE : Fonction de conversion température ---")

# Exercice : créer des fonctions de conversion de température
def celsius_vers_fahrenheit(celsius):
    """Convertit des degrés Celsius en Fahrenheit."""
    # Formule : F = C × 9/5 + 32
    return celsius * 9/5 + 32

def fahrenheit_vers_celsius(fahrenheit):
    """Convertit des degrés Fahrenheit en Celsius."""
    # Formule : C = (F - 32) × 5/9
    return (fahrenheit - 32) * 5/9

# Tests
temp_celsius = 20
temp_fahrenheit = celsius_vers_fahrenheit(temp_celsius)
print(f"{temp_celsius}°C = {temp_fahrenheit}°F")

temp_fahrenheit = 68
temp_celsius = fahrenheit_vers_celsius(temp_fahrenheit)
print(f"{temp_fahrenheit}°F = {temp_celsius}°C")

