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

## Default choices vs alternatives

This foundation ships with sensible defaults. If the user wants something different,
they can swap any layer — nothing is locked in.

| Layer | Default | Alternatives they can choose |
|-------|---------|------------------------------|
| **UI library** | shadcn/ui (Radix-based, Tailwind) | Radix Primitives direct, MUI, Ant Design, Chakra, Park UI |
| **API layer** | tRPC v11 (end-to-end type safety) | Hono (edge-native), Next.js API Routes (simpler), Express/Fastify (traditional) |
| **Auth** | NextAuth v5 | Lucia v3, Clerk, Auth0, Supabase Auth |
| **ORM** | Drizzle ORM | Prisma, Kysely, TypeORM |
| **CSS** | Tailwind CSS v4 | Panda CSS, vanilla CSS modules, styled-components |
| **Package manager** | pnpm | npm, yarn, bun |

If the user says nothing about these, use the defaults. If they ask for an alternative,
substitute it during generation — the architecture stays the same.

## Before you start

Ask the user these questions. Omit any that the user already answered:

1. **Project name** (kebab-case, e.g., `my-saas`)
2. **UI library**: shadcn/ui (default) or Radix Primitives or something else?
3. **API layer**: tRPC (default) or Hono or plain Next.js API Routes?
4. **Auth provider**: NextAuth v5 (default) or Lucia v3 or something else?

If they say "surprise me" or "your call" on any question, use the default.

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
- If the user chose an alternative API layer (Hono, Next.js API Routes), use that instead of tRPC
- If the user chose an alternative UI library (MUI, Chakra, etc.), use that instead of shadcn/ui
- `app/layout.tsx` — providers (API, Auth, Theme)
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

**1g. API layer (tRPC by default)**

If the user chose **tRPC** (default):
- Root router in `packages/` or `apps/web/trpc/`
- Context: auth session, db, request ID
- Public procedure: no auth required
- Protected procedure: auth + role check
- Error formatter: Zod errors → field-level messages

If the user chose **Hono**:
- Routes in `apps/web/app/api/` using Hono's router
- Middleware for auth, rate limiting, CORS
- Zod validation on every route
- OpenAPI docs via `@hono/zod-openapi`

If the user chose **Next.js API Routes**:
- Routes in `apps/web/app/api/` using Route Handlers
- Middleware at `apps/web/src/middleware.ts`
- Zod validation per route

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

If the user chose an alternative UI library, use that instead of shadcn/ui.

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

Files to write — each one has a specific purpose and audience:

1. **`CLAUDE.md`** — Per-project AI instructions. The very first file any AI agent
   reads when starting work. Contains stack, commands, conventions, and security
   rules. Without this file, every AI session has zero context.

2. **`docs/memory.md`** — Session-level context store. Records project metadata,
   architecture decisions (with ADR links), key dependencies, date-stamped session
   notes, known issues, and environment details. The AI reads this at every session
   start to resume context. Humans read it for history and onboarding. **Must be
   updated at the end of every work session** with a new session note entry.

3. **`docs/progress.md`** — Milestone and task tracker. Contains Phase 0-6 checklists
   (all marked pending on creation), a status overview table, completed milestones
   log, blockers table, and "next up" section. The AI reads this to know where work
   left off. Humans use it for standups and planning. **Checkboxes are ticked as
   work completes. Blockers are added as they arise.** The progress.md file in the
   skill itself serves double duty: it tracks the project foundation and also works
   as documentation for the skill's generation process.

4. **`docs/ARCHITECTURE.md`** — System design overview. Shows how Next.js, tRPC,
   Drizzle, PostgreSQL, and Redis connect. Defines the data model (users, sessions,
   audit_logs), request flow, security boundaries, and package dependency graph.
   Updated when the architecture changes significantly.

5. **`docs/DESIGN.md`** — Design system specification. Brand palette, semantic
   colors (light + dark), type scale, spacing, border radius, shadows, motion,
   layout system, component tiers, state patterns, form patterns, accessibility
   baselines, dark mode implementation, iconography, and coding conventions.
   Updated when brand or UI patterns change.

6. **`docs/SECURITY.md`** — Security model document. Auth method, RBAC roles, rate
   limits, CSP/Helmet headers, data protection, audit logging, dependency security,
   and incident response. Updated when security posture changes.

7. **`docs/CONTRIBUTING.md`** — Developer onboarding guide. Step-by-step setup,
   8-step development workflow, code conventions, testing conventions, and PR
   checklist. Every new developer or AI agent reads this first.

8. **`docs/ADR/adr-template.md`** — Architecture Decision Record template. Used to
   create individual ADR files (`adr-001-*.md`) for every significant architectural
   decision. Copy the template to a new file, fill it out, and commit alongside
   the decision's code changes.

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
