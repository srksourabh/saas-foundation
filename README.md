# saas-foundation

A Claude Code skill that generates the world's best full-stack TypeScript SaaS foundation from scratch.

## What it builds

When invoked, this skill scaffolds a complete SaaS project with:

- **Frontend**: Next.js 16 (App Router) + Tailwind CSS v4 + shadcn/ui
- **Design system**: Token-based (light/dark mode), Inter + JetBrains Mono, responsive grid, WCAG AA
- **Backend**: tRPC v11 (end-to-end type safety) + Drizzle ORM + PostgreSQL
- **Auth**: NextAuth v5 or Lucia v3 (Google OAuth + email/password)
- **Queue**: BullMQ + Redis
- **Testing**: Vitest (unit/integration) + Playwright (E2E)
- **CI/CD**: GitHub Actions (lint → typecheck → test → build)
- **Container**: Docker Compose (Postgres + Redis + app)
- **Security**: CSP, Helmet, rate limiting, RBAC, Zod validation, audit logging, brute force protection, dependency scanning
- **Scaffolding**: CLI scripts to generate models, pages, features, and emails
- **Knowledge continuity**: CLAUDE.md, memory.md, progress.md, ARCHITECTURE.md, DESIGN.md, SECURITY.md, CONTRIBUTING.md, ADR/

## Install

Copy the `saas-foundation/` directory into your `~/.claude/skills/` directory, or clone:

```bash
git clone https://github.com/srksourabh/saas-foundation ~/.claude/skills/saas-foundation
```

## Usage

Open Claude Code and say:

- "create a new project called acme"
- "scaffold a full-stack TypeScript SaaS"
- "use the world's best foundation"
- "start a new monorepo project"

## Structure

```
saas-foundation/
├── SKILL.md                    # Skill instructions (6-phase execution)
├── templates/                  # File templates for generated projects
│   ├── CLAUDE.md
│   ├── memory.md
│   ├── progress.md
│   ├── ARCHITECTURE.md
│   ├── DESIGN.md
│   ├── SECURITY.md
│   ├── CONTRIBUTING.md
│   ├── ADR-template.md
│   └── .env.example
├── reference/                  # Deeper reference docs
│   ├── stack.md
│   ├── project-structure.md
│   ├── design-guide.md
│   └── security-checklist.md
└── scripts/
    └── scaffold.ps1            # Scaffolding CLI
```
