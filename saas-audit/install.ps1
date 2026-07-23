param([switch]$Project)
$ErrorActionPreference = "Stop"
$SourceDir = Split-Path -Parent $MyInvocation.MyCommand.Path
function Install-Skill([string]$TargetRoot) {
  New-Item -ItemType Directory -Force -Path $TargetRoot | Out-Null
  $Target = Join-Path $TargetRoot "saas-audit"
  if (Test-Path $Target) { Remove-Item -Recurse -Force $Target }
  Copy-Item -Recurse -Force $SourceDir $Target
  Write-Host "Installed: $Target"
}
if ($Project) {
  Install-Skill (Join-Path (Get-Location) ".agents/skills")
  Install-Skill (Join-Path (Get-Location) ".claude/skills")
  Install-Skill (Join-Path (Get-Location) ".github/skills")
} else {
  Install-Skill (Join-Path $HOME ".agents/skills")
  Install-Skill (Join-Path $HOME ".claude/skills")
}
if ($env:HERMES_SKILLS_DIR) { Install-Skill $env:HERMES_SKILLS_DIR }
Write-Host "Restart your agent or reload its skills list."
