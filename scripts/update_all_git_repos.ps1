# Script pour mettre a jour tous les depots Git
# Usage: .\update_all_git_repos.ps1

# Obtient le dossier parent (dossier Git principal) depuis le dossier scripts
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$baseDir = Split-Path -Parent $scriptDir
$logFile = Join-Path $scriptDir "git_update_log.txt"

# Trouve le chemin complet de git (contourne les fonctions/aliases)
$gitExe = "C:\Program Files\Git\cmd\git.exe"
if (-not (Test-Path $gitExe)) {
    $gitExe = "C:\Program Files\Git\bin\git.exe"
}
if (-not (Test-Path $gitExe)) {
    # Dernier recours : utilise Get-Command pour trouver git
    $gitCmd = Get-Command git.exe -ErrorAction SilentlyContinue
    if ($gitCmd -and $gitCmd.CommandType -eq "Application") {
        $gitExe = $gitCmd.Source
    } else {
        $gitExe = "git.exe"
    }
}

# Fonction pour ecrire dans le log
function Write-Log {
    param([string]$Message)
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logMessage = "[$timestamp] $Message"
    Write-Host $logMessage
    try {
        Add-Content -Path $logFile -Value $logMessage -ErrorAction Stop
    } catch {
        # Si le fichier est verrouille, on continue sans logger
    }
}

Write-Log "=== Debut de la mise a jour des depots Git ==="

# Detecte automatiquement tous les depots Git dans le dossier de base
$repos = @()

# Ajoute le depot principal s'il est un depot Git
if (Test-Path (Join-Path $baseDir ".git")) {
    $repos += @{Path = $baseDir; Name = "Travail_Collaboratif (principal)"}
}

# Cherche tous les sous-dossiers qui sont des depots Git
$subDirs = Get-ChildItem -Path $baseDir -Directory -ErrorAction SilentlyContinue
foreach ($dir in $subDirs) {
    $gitPath = Join-Path $dir.FullName ".git"
    if (Test-Path $gitPath) {
        $repos += @{Path = $dir.FullName; Name = $dir.Name}
    }
}

if ($repos.Count -eq 0) {
    Write-Log "[ERREUR] Aucun depot Git trouve dans $baseDir"
    Write-Host "`n[ERREUR] Aucun depot Git trouve !" -ForegroundColor Red
    exit 1
}

Write-Log "[INFO] $($repos.Count) depot(s) Git trouve(s)"

$successCount = 0
$errorCount = 0

foreach ($repo in $repos) {
    $repoPath = $repo.Path
    $repoName = $repo.Name
    
    if (-not (Test-Path $repoPath)) {
        Write-Log "[ATTENTION] $repoName : Dossier introuvable ($repoPath)"
        $errorCount++
        continue
    }
    
    if (-not (Test-Path (Join-Path $repoPath ".git"))) {
        Write-Log "[ATTENTION] $repoName : N'est pas un depot Git"
        continue
    }
    
    Write-Log "[INFO] Mise a jour de $repoName..."
    
    try {
        # Utilise git avec le chemin complet du depot
        Push-Location $repoPath
        
        # Verifie si le depot a des commits
        $hasCommits = & $gitExe rev-parse --verify HEAD 2>$null
        if ($LASTEXITCODE -ne 0) {
            Write-Log "[INFO] $repoName : Depot vide (aucun commit)"
            $successCount++
            Pop-Location
            continue
        }
        
        # Recupere les informations sur la branche actuelle
        $currentBranch = & $gitExe rev-parse --abbrev-ref HEAD 2>$null
        if ($LASTEXITCODE -ne 0) {
            Write-Log "[ERREUR] $repoName : Erreur lors de la detection de la branche"
            $errorCount++
            Pop-Location
            continue
        }
        
        Write-Log "   Branche actuelle : $currentBranch"
        
        # Recupere les modifications depuis le depot distant
        $fetchOutput = & $gitExe fetch --all 2>&1 | Out-String
        if ($LASTEXITCODE -ne 0) {
            Write-Log "[ERREUR] $repoName : Erreur lors du fetch"
            Write-Log "   Details : $fetchOutput"
            $errorCount++
            Pop-Location
            continue
        }
        
        # Verifie s'il y a des modifications a recuperer
        $statusOutput = & $gitExe status -sb 2>&1 | Out-String
        $hasChanges = $statusOutput -match "behind"
        
        if ($hasChanges) {
            # Fait un pull pour recuperer les modifications
            $pullOutput = & $gitExe pull origin $currentBranch 2>&1 | Out-String
            if ($LASTEXITCODE -eq 0) {
                Write-Log "[SUCCES] $repoName : Mis a jour avec succes"
                Write-Log "   $pullOutput"
                $successCount++
            } else {
                Write-Log "[ERREUR] $repoName : Erreur lors du pull"
                Write-Log "   Details : $pullOutput"
                $errorCount++
            }
        } else {
            Write-Log "[OK] $repoName : Deja a jour"
            $successCount++
        }
        
        Pop-Location
        
    } catch {
        Write-Log "[ERREUR] $repoName : Erreur : $_"
        $errorCount++
        Pop-Location -ErrorAction SilentlyContinue
    }
    
    Write-Log ""
}

Write-Log "=== Fin de la mise a jour ==="
Write-Log "Resume : $successCount succes, $errorCount erreurs"
Write-Log ""

if ($errorCount -eq 0) {
    Write-Host "`n[SUCCES] Tous les depots sont a jour !" -ForegroundColor Green
} else {
    Write-Host "`n[ATTENTION] Certains depots ont rencontre des erreurs. Consultez le log : $logFile" -ForegroundColor Yellow
}
