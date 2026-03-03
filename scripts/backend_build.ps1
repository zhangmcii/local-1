$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $PSScriptRoot
$python = Join-Path $repoRoot '.venv\Scripts\python.exe'

if (-not (Test-Path $python)) {
  throw "Missing venv python at $python. Create the venv and install backend deps (including PyInstaller) first."
}

$appPy = Join-Path $repoRoot 'backend\app.py'
$distPath = Join-Path $repoRoot 'src-tauri\resources'
$workPath = Join-Path $repoRoot 'backend\build'
$specPath = Join-Path $repoRoot 'backend'
$targetExe = Join-Path $distPath 'app.exe'

# PyInstaller overwrites by deleting the old EXE. On Windows this can fail if the backend is still running
# or antivirus is scanning the file, so retry a few times to reduce flakiness.
for ($i = 0; $i -lt 10; $i++) {
  if (-not (Test-Path $targetExe)) { break }
  try {
    Remove-Item -Force -ErrorAction Stop $targetExe
    break
  } catch {
    Start-Sleep -Milliseconds (200 + ($i * 250))
  }
}

if (Test-Path $targetExe) {
  throw "Failed to overwrite $targetExe (file is locked). Close the installed app / any running backend process and retry."
}

& $python -m PyInstaller `
  -F $appPy `
  --name app `
  --distpath $distPath `
  --workpath $workPath `
  --specpath $specPath `
  --noconfirm

