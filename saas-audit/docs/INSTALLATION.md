# Installation Guide

Copy the complete `saas-audit` directory. `SKILL.md` depends on the `references`, `scripts`, `assets` and `docs` directories.

## Prerequisites

- Git installed for repository cloning or updating.
- Python 3 for the optional workspace, validation and reporting helpers.
- Authorized access to the repository or application being audited.
- Browser automation, terminal, API, database and cloud tools only where approved.

## Clone the repository

```bash
git clone https://github.com/srksourabh/saas-foundation.git
cd saas-foundation/saas-audit
```

## Automated installation

### macOS, Linux, WSL and Git Bash

Install for the current user:

```bash
./install.sh
```

Install into the current project:

```bash
./install.sh --project
```

### Windows PowerShell

Install for the current user:

```powershell
.\install.ps1
```

Install into the current project:

```powershell
.\install.ps1 -Project
```

## Platform-specific locations

| Platform | Project location | User location |
|---|---|---|
| Claude Code | `.claude/skills/saas-audit/` | `~/.claude/skills/saas-audit/` |
| Codex / Agent Skills | `.agents/skills/saas-audit/` | `~/.agents/skills/saas-audit/` |
| Anti-Gravity | `.agents/skills/saas-audit/` | Tool-configured Agent Skills directory |
| VS Code / GitHub Copilot | `.github/skills/saas-audit/` | Prefer project installation |
| Hermes | Configured skills directory | Set `HERMES_SKILLS_DIR` |
| Generic agent | Any readable skill directory | Direct the agent to `SKILL.md` |

## Hermes custom installation

macOS/Linux/WSL:

```bash
HERMES_SKILLS_DIR="$HOME/path/to/hermes/skills" ./install.sh
```

PowerShell:

```powershell
$env:HERMES_SKILLS_DIR = "$HOME\path\to\hermes\skills"
.\install.ps1
```

## Manual installation

### Claude Code

```bash
mkdir -p ~/.claude/skills
cp -R saas-audit ~/.claude/skills/saas-audit
```

### Codex or compatible Agent Skills client

```bash
mkdir -p ~/.agents/skills
cp -R saas-audit ~/.agents/skills/saas-audit
```

### Project-local installation

```bash
mkdir -p .agents/skills .claude/skills .github/skills
cp -R saas-audit .agents/skills/saas-audit
cp -R saas-audit .claude/skills/saas-audit
cp -R saas-audit .github/skills/saas-audit
```

## Verify installation

Confirm that the selected directory contains:

```text
saas-audit/
├── SKILL.md
├── references/
├── scripts/
├── assets/
└── docs/
```

Then ask the agent:

```text
List the scope and release gates of the saas-audit skill without starting an audit.
```

The response should mention security, RBAC, tenant isolation, evidence, severity and `SHIP`/`CONDITIONAL SHIP`/`DO NOT SHIP`.

## Update

Pull the latest repository and rerun the installer:

```bash
cd saas-foundation
git pull
cd saas-audit
./install.sh
```

Installed copies do not update automatically.

## Credential setup

Do not place credentials in prompts that may be logged or committed. Prefer environment variables:

```bash
export AUDIT_APP_URL="https://staging.example.com"
export AUDIT_ADMIN_EMAIL="audit-admin@example.com"
export AUDIT_ADMIN_PASSWORD="..."
export AUDIT_TENANT_A_EMAIL="..."
export AUDIT_TENANT_A_PASSWORD="..."
export AUDIT_TENANT_B_EMAIL="..."
export AUDIT_TENANT_B_PASSWORD="..."
```

Use a `.env.audit` file only when it is ignored by Git:

```gitignore
.env.audit
saas-audit-output/
```

## Optional helpers

Create an audit workspace:

```bash
python scripts/init_audit.py --app "Example SaaS" --output ./saas-audit-output
```

Validate findings:

```bash
python scripts/validate_findings.py \
  --input ./saas-audit-output/data/Example_Audit_Findings.json \
  --schema ./assets/finding.schema.json
```

Render the report:

```bash
python scripts/render_report.py \
  --input ./saas-audit-output \
  --output ./saas-audit-output/reports
```

Exact options may be inspected with `--help`.
