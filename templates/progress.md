# Progress — <project-name>

## Current milestone: Foundation setup

### Phase 0 — Project skeleton
- [ ] Directory structure created
- [ ] Root config files written (package.json, turbo.json, tsconfig, etc.)
- [ ] .gitignore, .env.example written

### Phase 1 — Core infrastructure
- [ ] Database schema (users, sessions, audit_logs)
- [ ] Auth setup (<auth-provider>)
- [ ] tRPC router with public + protected procedures
- [ ] Validators (Zod schemas for auth, common)
- [ ] Config (env validation, constants)
- [ ] Next.js app with auth pages + dashboard layout
- [ ] shadcn/ui components initialized
- [ ] Docker Compose (Postgres + Redis + app)
- [ ] Email templates + Resend integration

### Phase 2 — Security hardening
- [ ] CSP + Helmet headers
- [ ] CORS whitelist
- [ ] Rate limiting (auth routes + API)
- [ ] RBAC middleware
- [ ] Audit logging
- [ ] Session rotation
- [ ] Brute force protection

### Phase 3 — Operational excellence
- [ ] Vitest unit + integration tests
- [ ] Playwright E2E tests
- [ ] Pino structured logging
- [ ] Centralized error handling
- [ ] Health check endpoint
- [ ] CI pipeline (GitHub Actions)

### Phase 4 — Scaffolding scripts
- [ ] Model generator
- [ ] Page generator
- [ ] Feature generator
- [ ] Email generator

### Phase 5 — Knowledge files
- [ ] CLAUDE.md
- [ ] docs/memory.md
- [ ] docs/progress.md
- [ ] docs/ARCHITECTURE.md
- [ ] docs/SECURITY.md
- [ ] docs/CONTRIBUTING.md
- [ ] docs/ADR/adr-template.md

### Phase 6 — Final verification
- [ ] pnpm install passes
- [ ] pnpm lint passes
- [ ] pnpm typecheck passes
- [ ] pnpm test passes
- [ ] docker compose build succeeds
- [ ] Health endpoint returns 200
- [ ] Auth flow works end-to-end

---

## Completed

| Date | Milestone | Notes |
|------|-----------|-------|
| —    | —         | —     |

## Blockers

| Date | Blocker | Status |
|------|---------|--------|
| —    | —       | —      |
