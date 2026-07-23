#!/usr/bin/env bash
set -euo pipefail
SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODE="global"
if [[ "${1:-}" == "--project" ]]; then MODE="project"; fi
copy_skill(){ local root="$1"; mkdir -p "$root"; rm -rf "$root/saas-audit"; cp -R "$SOURCE_DIR" "$root/saas-audit"; rm -rf "$root/saas-audit/.git" 2>/dev/null || true; echo "Installed: $root/saas-audit"; }
if [[ "$MODE" == "project" ]]; then
  copy_skill "$(pwd)/.agents/skills"
  copy_skill "$(pwd)/.claude/skills"
  copy_skill "$(pwd)/.github/skills"
else
  copy_skill "$HOME/.agents/skills"
  copy_skill "$HOME/.claude/skills"
fi
if [[ -n "${HERMES_SKILLS_DIR:-}" ]]; then copy_skill "$HERMES_SKILLS_DIR"; fi
echo "Restart your agent or reload its skills list."
