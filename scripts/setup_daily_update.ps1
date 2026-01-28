# Script pour configurer la mise a jour quotidienne automatique
# IMPORTANT: Executez ce script en tant qu'administrateur (clic droit > Executer en tant qu'administrateur)

# Obtient le chemin du script depuis le dossier scripts
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$scriptPath = Join-Path $scriptDir "update_all_git_repos.ps1"
$taskName = "Mise a jour Git quotidienne"

Write-Host "Configuration de la mise a jour automatique quotidienne..." -ForegroundColor Cyan

# Verifie si la tache existe deja
$existingTask = Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue

if ($existingTask) {
    Write-Host "La tache existe deja. Voulez-vous la supprimer et la recreer ? (O/N)" -ForegroundColor Yellow
    $response = Read-Host
    if ($response -eq "O" -or $response -eq "o") {
        Unregister-ScheduledTask -TaskName $taskName -Confirm:$false
        Write-Host "Ancienne tache supprimee." -ForegroundColor Green
    } else {
        Write-Host "Operation annulee." -ForegroundColor Yellow
        exit
    }
}

# Cree la nouvelle tache
try {
    $action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-ExecutionPolicy Bypass -File `"$scriptPath`""
    $trigger = New-ScheduledTaskTrigger -Daily -At "09:00"
    $principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Highest
    $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
    
    Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Principal $principal -Settings $settings -Description "Met a jour automatiquement tous les depots Git tous les jours a 9h00" -Force
    
    Write-Host "`n[SUCCES] Tache planifiee creee avec succes !" -ForegroundColor Green
    Write-Host "La mise a jour s'executera tous les jours a 9h00." -ForegroundColor Cyan
    Write-Host "`nPour modifier l'heure, utilisez le Planificateur de taches Windows." -ForegroundColor Yellow
    Write-Host "Pour supprimer la tache : Planificateur de taches > Bibliotheque > $taskName > Supprimer" -ForegroundColor Yellow
    
} catch {
    Write-Host "`n[ERREUR] Impossible de creer la tache planifiee." -ForegroundColor Red
    Write-Host "Assurez-vous d'executer ce script en tant qu'administrateur." -ForegroundColor Yellow
    Write-Host "Details de l'erreur : $_" -ForegroundColor Red
}
