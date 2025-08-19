<#
.SYNOPSIS
Bootstrap Windows development environment for Kubernetes Python client.

.DESCRIPTION
Creates virtual environment (if missing), installs dependencies, and ensures
shim modules (config/dynamic/watch/stream/leaderelection) contain re-export
code replacing symlinks for Windows portability.

#>
param(
    [string]$Python = "py",
    [string]$Venv = ".venv"
)

$ErrorActionPreference = 'Stop'

function Write-Step($m){ Write-Host "[setup] $m" -ForegroundColor Cyan }

Write-Step "Python version"
& $Python -3 -c "import sys; print(sys.version)" | Write-Host

if(!(Test-Path $Venv)){
  Write-Step "Creating venv $Venv"
  & $Python -3 -m venv $Venv
}
Write-Step "Activating venv"
$activate = Join-Path $Venv 'Scripts/Activate.ps1'
. $activate

Write-Step "Upgrading pip"
python -m pip install --upgrade pip > $null

Write-Step "Installing requirements"
if(Test-Path requirements.txt){ pip install -r requirements.txt }
if(Test-Path test-requirements.txt){ pip install -r test-requirements.txt }

$shimMap = @{ 
  'kubernetes/config' = 'from kubernetes.base.config import *  # noqa: F401,F403';
  'kubernetes/dynamic' = 'from kubernetes.base.dynamic import *  # noqa: F401,F403';
  'kubernetes/watch' = 'from kubernetes.base.watch import *  # noqa: F401,F403';
  'kubernetes/stream' = 'from kubernetes.base.stream import *  # noqa: F401,F403';
  'kubernetes/leaderelection' = 'from kubernetes.base.leaderelection import *  # noqa: F401,F403'
}

foreach($path in $shimMap.Keys){
  if(Test-Path $path){
    $item = Get-Item $path
    if($item.PSIsContainer){ continue }
    $content = Get-Content $path -Raw
    if($content -notmatch 'kubernetes.base'){
      Write-Step "Updating shim $path"
      """Windows shim auto-generated`n$($shimMap[$path])""" | Out-File -FilePath $path -Encoding UTF8
    }
  } else {
    Write-Step "Creating shim file $path"
    """Windows shim auto-generated`n$($shimMap[$path])""" | Out-File -FilePath $path -Encoding UTF8
  }
}

Write-Step "Smoke import"
python -c "from kubernetes import config,dynamic,watch,stream,leaderelection;print('Shim import success')"

Write-Step "Done"
