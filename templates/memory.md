# Memory — <project-name>

## Project metadata
- **Created**: <date>
- **Stack**: Next.js 16 + tRPC + Drizzle + PostgreSQL
- **Auth**: <auth-provider>
- **Deployment**: Vercel (web) / Docker (services)

## Architecture decisions

### ADR-001: Auth strategy
**Date**: <date>
**Decision**: <auth-provider>
**Reason**: [standard choice for TypeScript SaaS — good DX, OOTB OAuth support]
**Trade-offs**: [trade-off notes]

### ADR-002: Database ORM
**Date**: <date>
**Decision**: Drizzle ORM
**Reason**: Lightweight, SQL-like API, good TypeScript inference, fast migrations
**Trade-offs**: Less mature relation handling than Prisma; more control

### ADR-003: Monorepo tool
**Date**: <date>
**Decision**: Turborepo + pnpm
**Reason**: Industry standard for TypeScript monorepos, parallel execution, caching

## Key dependencies
- Next.js 16 — React framework (App Router)
- tRPC v11 — type-safe API layer
- Drizzle ORM — database access
- Tailwind CSS v4 — styling
- shadcn/ui — component library (based on Radix UI)
- Zod — schema validation
- Pino — structured logging
- BullMQ — background job queue
- Resend — email delivery

## Session notes

<!-- Per-session entries go here. Format:
### YYYY-MM-DD: What we worked on
- Key decisions made
- Files touched
- Current state / blockers
-->

## Known issues
- <!-- Track known bugs, pending decisions, tech debt -->

## Environment
- **Dev**: `docker compose up` (Postgres + Redis)
- **Staging**: [staging URL or notes]
- **Prod**: [prod URL or notes]
