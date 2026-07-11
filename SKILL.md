---
name: saas-foundation
description: >
  Build the world's best full-stack TypeScript SaaS foundation from scratch.
  Generates a complete project with monorepo (Turborepo + pnpm), Next.js 16 App
  Router, tRPC, Drizzle ORM + PostgreSQL, auth (NextAuth/Lucia), Tailwind +
  shadcn/ui, Vitest + Playwright, Docker Compose, CI/CD, and all knowledge
  continuity files (CLAUDE.md, memory.md, progress.md, ARCHITECTURE.md, ADR/,
  SECURITY.md, CONTRIBUTING.md, DESIGN.md). Hardens security by default: CSP, rate limiting,
  RBAC, Zod validation, audit logging, dependency scanning.
  Triggers on: "create a new project", "start a new SaaS", "project foundation",
  "scaffold a project", "build a new app", "initialize foundation", "set up
  foundation", "foundation template", "world's best foundation", "new full-stack
  project", "start a monorepo".
  Covers: project scaffolding, security hardening, knowledge continuity, team
  onboarding, operational excellence, code generation scripts.
  NOT for: single-file scripts, existing projects that need incremental changes,
  non-TypeScript stacks, mobile-only apps.
---

# SaaS Foundation

Build a production-grade TypeScript SaaS starter with zero compromises. When invoked,
generate the complete project structure, all config files, all knowledge continuity
docs, security hardening, CI/CD, Docker Compose, and scaffolding scripts.

## When to invoke

- User says "create a new project", "start a SaaS", "build a foundation"
- User wants a complete starter template for a full-stack TypeScript app
- User asks for project scaffolding with auth, DB, CI/CD, and docs built-in
- User mentions "world's best foundation" or "project foundation"

## Before you start

Ask the user exactly **2** questions:

1. **Project name** (kebab-case, e.g., `my-saas`)
2. **Auth provider preference**: NextAuth v5 (simpler, more OAuth providers) or Lucia v3 (more flexible, lower-level)

If they say "surprise me" or "your call", use NextAuth v5.

## Execution phases

Execute these phases **in order**. Each phase must complete fully before the next begins.

---

### Phase 0 — Scaffold project skeleton

Create directory structure:

```
<project-name>/
├── apps/
│   └── web/                    # Next.js 16 App Router
├── packages/
│   ├── ui/                     # Shared UI (shadcn/ui)
│   ├── db/                     # Drizzle schema + migrations
│   ├── auth/                   # Auth config + middleware
│   ├── validators/             # Shared Zod schemas
│   ├── email/                  # React Email templates
│   └── config/                 # Env, constants, shared config
├── tooling/
│   ├── eslint/                 # Shared ESLint flat config
│   └── typescript/             # Shared tsconfig bases
├── scripts/                    # Scaffolding CLI
├── .github/
│   └── workflows/
│       ├── ci.yml              # lint → typecheck → test → build
│       └── cd.yml              # Deploy (conditional)
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml      # Postgres + Redis + app
├── docs/
│   ├── memory.md
│   ├── progress.md
│   ├── ARCHITECTURE.md
│   ├── DESIGN.md
│   ├── SECURITY.md
│   ├── CONTRIBUTING.md
│   └── ADR/
│       └── adr-template.md
├── CLAUDE.md
├── .env.example
├── .gitignore
├── package.json                # Root (pnpm workspace)
├── pnpm-workspace.yaml
├── turbo.json
├── tsconfig.json               # Base tsconfig
├── vitest.workspace.ts
└── playwright.config.ts
```

After creating directories, write every file. Use matching coding style — modern, no comments
unless critical, concise.

---

### Phase 1 — Core infrastructure

**1a. Root config files**

- `package.json` — name matches `<project-name>`, private, scripts: dev/build/lint/typecheck/test
- `pnpm-workspace.yaml` — packages: `apps/*` `packages/*` `tooling/*`
- `turbo.json` — pipeline: dev, build, lint, test, typecheck with cache outputs
- `tsconfig.json` — base: strict, ESNext module, bundler resolution, paths
- `vitest.workspace.ts` — include all packages
- `playwright.config.ts` — webServer pointing to `apps/web`, test dir `apps/web/e2e`

**1b. Database (`packages/db`)**

- Drizzle config: PostgreSQL, schema in `src/schema/`
- Initial schema files:
  - `users.ts` — id (uuid), email, name, avatar_url, role (enum: admin/user/viewer), created_at, updated_at
  - `sessions.ts` — id, user_id (FK), expires_at, created_at
  - `audit_logs.ts` — id, user_id, action, resource, details (jsonb), ip_address, created_at
- `drizzle.config.ts` — schema path, output path
- `src/index.ts` — re-export all schemas + `db` client

**1c. Auth (`packages/auth`)**

If NextAuth v5:
- Drizzle adapter
- Providers: Google + Credentials (email/password)
- Session strategy: database
- Pages: signin, error
- Callbacks: session user includes role

If Lucia v3:
- Drizzle adapter
- Session table in Drizzle
- Password hashing with Argon2
- Login/signup/verify API handlers
- Middleware for session verification

**1d. Validators (`packages/validators`)**

- `src/auth.ts` — signup schema, login schema, profile update schema
- `src/common.ts` — pagination, UUID, email
- `src/index.ts` — re-exports

**1e. Config (`packages/config`)**

- `src/env.ts` — Zod-validated env vars (DATABASE_URL, AUTH_SECRET, etc.)
- `src/constants.ts` — app name, pagination defaults, cookie names

**1f. Web app (`apps/web`)**

- Next.js 16 with App Router
- `app/layout.tsx` — providers (TRPC, Auth, Theme)
- `app/page.tsx` — landing page (redirects to dashboard if authed)
- `app/(auth)/login/page.tsx` — login form
- `app/(auth)/signup/page.tsx` — signup form
- `app/(dashboard)/layout.tsx` — sidebar + header layout
- `app/(dashboard)/page.tsx` — dashboard home
- `app/api/trpc/[trpc]/route.ts` — tRPC HTTP handler
- `app/api/auth/[...nextauth]/route.ts` — NextAuth handler (if NextAuth)
- `trpc/` — router, context, procedures
- `components/` — ui components from shadcn
- `e2e/` — Playwright tests (auth flow)

**1g. tRPC setup**

- Root router in `packages/` or `apps/web/trpc/`
- Context: auth session, db, request ID
- Public procedure: no auth required
- Protected procedure: auth + role check
- Error formatter: Zod errors → field-level messages

**1h. Docker Compose**

- `docker-compose.yml`:
  - `postgres` — PostgreSQL 16, port 5432, volume for data
  - `redis` — Redis 7, port 6379 (for rate limiting / queues)
  - `app` — builds from Dockerfile, depends on postgres+redis

**1i. Design system (`docs/DESIGN.md`)**

Write `docs/DESIGN.md` from the `templates/DESIGN.md` template. Customize the
brand palette to the project name (auto-generate a complementary 50-900 scale).
Implement all tokens as CSS custom properties in `app/globals.css` and Tailwind
extensions in `tailwind.config.ts`. See `reference/design-guide.md` for the
implementation roadmap, component composition patterns, and anti-patterns.

Design system must include:
- Brand + semantic color palette (light and dark)
- Type scale (display through caption) with Inter + JetBrains Mono
- Spacing scale, border radius, shadow tokens
- Motion tokens with `prefers-reduced-motion` respect
- Layout system (sidebar + main, responsive breakpoints)
- Component tier architecture (primitives → composed → feature)
- Form patterns (react-hook-form + Zod + shadcn/ui)
- State patterns (loading, empty, error, edge)
- Accessibility baseline (WCAG AA, keyboard nav, focus rings)
- Dark mode implementation (class-based, localStorage persistence)
- Iconography conventions (lucide-react, inheritance)

**1j. UI (`packages/ui`)**

- shadcn/ui initialized with `components.json`
- Base components: Button, Input, Card, Dialog, DropdownMenu, Table, Badge, Skeleton, Avatar, Sonner/Toast
- All using Tailwind CSS v4 + class-variance-authority

---

### Phase 2 — Security hardening

Apply **all** of these. No exceptions.

| Check | Implementation |
|-------|---------------|
| CSP headers | Next.js middleware or `next.config.js` headers |
| Helmet security headers | Same middleware: X-Content-Type-Options, X-Frame-Options, Referrer-Policy |
| CORS | Whitelist origins in config, apply in tRPC middleware |
| Rate limiting | Upstash Ratelimit or Vercel KV — per IP for auth routes, per user for API |
| RBAC | `role` field on user, middleware checks: `requireRole('admin')` |
| Input validation | Every tRPC mutation uses Zod schema from `@validators` |
| SQL injection | Drizzle ORM — parameterized by default |
| XSS | React auto-escapes + CSP prevents inline scripts |
| Secrets | `.env` gitignored, `.env.example` committed with dummy values |
| Audit logging | All sensitive actions → `audit_logs` table (login, role change, data export) |
| Session rotation | Rotate session ID on login, logout, role upgrade |
| Brute force protection | Lockout after 5 failed attempts for 15 minutes |
| Password policy | Min 8 chars, 1 upper, 1 number (enforced in validators) |
| API key format | `sk_<project>_<random>` — prefix-identifiable |
| Dependency scanning | `pnpm audit` in CI + Dependabot weekly |

Write the security middleware in `apps/web/src/middleware.ts`:

```typescript
// Security middleware must:
// 1. Apply CSP + Helmet headers to all responses
// 2. Rate-limit auth routes by IP
// 3. Rate-limit API routes by user session
// 4. Log all 401/403 responses to audit_logs
```

---

### Phase 3 — Operational excellence

**3a. Testing**

- `vitest.config.ts` at root — coverage threshold 80%
- Unit tests: `packages/*/src/**/__tests__/` — cover validators, auth helpers, utilities
- Integration tests: `packages/db/src/__tests__/` — test DB queries with test container
- E2E: `apps/web/e2e/` — Playwright: signup flow, login flow, protected route redirect, 404 page
- CI pipeline runs: `pnpm lint && pnpm typecheck && pnpm test -- --coverage`

**3b. Logging**

- Pino logger in `packages/config/src/logger.ts`
- Request ID on every request (via middleware)
- Structured JSON logging: `{ level, time, msg, req_id, user_id, path, duration_ms }`
- Log level: `debug` in dev, `info` in prod

**3c. Error handling**

- Centralized error handler in tRPC
- Custom error classes: `NotFoundError`, `UnauthorizedError`, `ValidationError`, `RateLimitError`
- Dev: full error details. Prod: sanitized messages, logged to Sentry.

**3d. Health checks**

- `GET /api/health` returns:
  ```json
  { "status": "ok", "db": "connected", "redis": "connected", "uptime": 12345 }
  ```
- Run every 30s in Docker Compose via healthcheck

**3e. CI/CD**

- `.github/workflows/ci.yml`:
  ```yaml
  name: CI
  on: [push, pull_request]
  jobs:
    quality:
      runs-on: ubuntu-latest
      services:
        postgres:
          image: postgres:16
          env: { POSTGRES_PASSWORD: postgres }
      steps:
        - uses: actions/checkout@v4
        - uses: pnpm/action-setup@v4
        - uses: actions/setup-node@v4
        - run: pnpm install
        - run: pnpm lint
        - run: pnpm typecheck
        - run: pnpm test -- --coverage
        - run: pnpm build
  ```
- `.github/workflows/cd.yml` — deploy to Vercel (web) + Docker registry (API)

---

### Phase 4 — Scaffolding scripts

Create `scripts/scaffold.ps1` with commands:

| Command | What it generates |
|---------|------------------|
| `pnpm scaffold model <name>` | Drizzle schema + Zod validator + tRPC router |
| `pnpm scaffold page <name>` | Next.js page + loading + error states |
| `pnpm scaffold feature <name>` | Full vertical slice: model + page + API + tests |
| `pnpm scaffold email <name>` | React Email template + preview route |

Each scaffold must:
- Respect existing conventions (path naming, exports, file structure)
- Wire imports correctly into existing modules
- Not overwrite existing files unless `--force` is passed

---

### Phase 5 — Knowledge continuity files

Write each file using templates in `templates/`. Customize:
- Replace `<project-name>` with the actual project name
- Replace `<year>` with the current year
- Fill in any choices the user made (auth provider, etc.)

Files to write:
1. `CLAUDE.md` — per-project AI instructions (from template)
2. `docs/memory.md` — initialized with project metadata, architecture summary, decisions
3. `docs/progress.md` — initialized with Phase 0-6 checklist, all marked pending
4. `docs/ARCHITECTURE.md` — system design overview (from template)
5. `docs/DESIGN.md` — design system tokens and conventions (from template)
6. `docs/SECURITY.md` — security model (from template)
7. `docs/CONTRIBUTING.md` — setup + contribution workflow (from template)
8. `docs/ADR/adr-template.md` — ADR decision record template

---

### Phase 6 — Final verification

Run these checks before declaring done:

```
01. [ ] pnpm install completes without errors
02. [ ] pnpm lint passes (ESLint flat config)
03. [ ] pnpm typecheck passes (tsc --noEmit)
04. [ ] pnpm test runs and passes (Vitest)
05. [ ] docker compose build succeeds
06. [ ] .env.example has no real secrets
07. [ ] .gitignore covers: node_modules, .env, dist, .next, *.log
08. [ ] All 9 knowledge files exist: CLAUDE.md, memory.md, progress.md,
        ARCHITECTURE.md, DESIGN.md, SECURITY.md, CONTRIBUTING.md, ADR/adr-template.md
09. [ ] middleware.ts applies CSP + Helmet headers
10. [ ] Health endpoint returns 200 + JSON with status fields
11. [ ] Auth flow works: signup → login → protected route
```

## Output format

When completed, return:

```
## Project created: <project-name>

### Structure
- <n> directories, <n> files

### Stack
- Frontend: Next.js 16 + Tailwind + shadcn/ui
- Design system: Token-based (light/dark), Inter + JetBrains Mono, responsive grid
- Backend: tRPC + Drizzle ORM + PostgreSQL
- Auth: <NextAuth v5 | Lucia v3>
- Queue: BullMQ + Redis
- Test: Vitest + Playwright
- CI: GitHub Actions

### Security
- CSP | Helmet | Rate limiting | RBAC | Zod validation | Audit logging
- Brute force protection | Session rotation | Dependency scanning

### Quick start
- `pnpm install`
- `cp .env.example .env` and fill values
- `docker compose up -d`
- `pnpm db:push`
- `pnpm dev`

### Next steps
- [Anything the user should do next, e.g., configure OAuth keys]
```

## Anti-patterns

- **Don't** add features beyond what's listed. The foundation is minimal.
- **Don't** skip security measures because "it's just a starter". Every measure is non-negotiable.
- **Don't** write placeholder comments like "TODO: add your logic here". Write complete files.
- **Don't** use `any` types. Every type must be explicit.
- **Don't** over-abstract. Single-use functions should not be in shared packages.
- **Don't** create the project in the current directory without asking for a project name first.
- **Don't** generate files that duplicate existing templates — use the provided templates.

## Scope boundary

This skill generates a NEW project from scratch. It does NOT:
- Modify an existing project's structure
- Add features to an already-running codebase
- Handle deployment to specific cloud providers (Vercel/Docker deployment in CI/CD is a stub)
- Generate business logic for a specific domain (CRM, analytics, etc.)
- Replace an existing project's configuration
