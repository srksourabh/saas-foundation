# Platform Installation

Copy the entire `saas-audit` directory because `SKILL.md` depends on references, scripts and assets.

## Codex, Anti-Gravity and Agent Skills clients

Project: `<project>/.agents/skills/saas-audit/`

User: `~/.agents/skills/saas-audit/`

## Claude Code

Project: `<project>/.claude/skills/saas-audit/`

User: `~/.claude/skills/saas-audit/`

## VS Code / GitHub Copilot

Use one or more project locations:

- `<project>/.github/skills/saas-audit/`
- `<project>/.claude/skills/saas-audit/`
- `<project>/.agents/skills/saas-audit/`

## Hermes and generic agents

Use the configured skills directory. Otherwise direct the agent to read `saas-audit/SKILL.md`; linked files use relative paths. Set `HERMES_SKILLS_DIR` before running the installer for a custom Hermes destination.

Review skills and scripts before granting terminal/browser access. The skill uses only permissions already available to the agent.
