# Configuration Git pour PowerShell

## Problème : Git n'est pas reconnu

Si vous voyez l'erreur `git : Le terme «git» n'est pas reconnu`, voici les solutions :

## Solution 1 : Recharger le profil PowerShell (RECOMMANDÉ)

Dans votre terminal PowerShell, exécutez :

```powershell
. $PROFILE
```

Puis testez :
```powershell
git --version
cd TP1
git status
```

## Solution 2 : Ajouter Git manuellement à la session

Si la solution 1 ne fonctionne pas, exécutez :

```powershell
$env:Path += ";C:\Program Files\Git\bin"
```

## Solution 3 : Utiliser le chemin complet

En dernier recours, utilisez le chemin complet :

```powershell
& "C:\Program Files\Git\bin\git.exe" --version
& "C:\Program Files\Git\bin\git.exe" status
```

## Configuration permanente

Le profil PowerShell a été configuré pour charger Git automatiquement. 
Il se trouve dans : `C:\Users\Ellie\OneDrive\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1`

**Note :** Pour que les changements prennent effet dans une session déjà ouverte, vous devez recharger le profil avec `. $PROFILE` ou redémarrer PowerShell.

