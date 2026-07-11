# Stack decisions (defaults vs alternatives)

This foundation ships with **defaults** for every layer. They can all be swapped
if the user requests it. The table below explains why each default was chosen and
what alternatives are available.

## Why each default

| Default | Why this over the alternative | Alternatives available |
|---------|------------------------------|------------------------|
| **Turborepo** | Lighter, faster, Vercel-native. Nx is more powerful but heavier than a SaaS starter needs. | Nx |
| **pnpm** | Disk-efficient (content-addressable store), strict dependency resolution. Faster installs. | npm, yarn, bun |
| **Next.js 16** | Larger ecosystem, RSC out of box, Vercel deploy is one click. Remix is excellent but Next.js has more mindshare + packages. | Remix |
| **tRPC** | End-to-end type safety with zero schema duplication. REST needs manual types. GraphQL needs codegen. tRPC infers types from your functions. | Hono, Next.js API Routes, Express, Fastify |
| **Drizzle** | Lighter (no engine binary), SQL-like API gives more control, faster CI installs. Prisma has better DX for complex relations but is heavier. | Prisma, Kysely, TypeORM |
| **Tailwind CSS v4** | Utility-first is faster to iterate, v4 has the CSS-first config. No runtime CSS-in-JS cost. | Panda CSS, CSS modules, styled-components |
| **shadcn/ui** | Copy-paste model (you own the code), Radix-based (accessible), no lock-in. MUI is heavier with its own design language. | MUI, Chakra, Ant Design, Park UI, Radix Primitives |
| **Vitest** | Faster (esbuild-based), ESM-native, same API as Jest. Jest is slower and has ESM issues. | Jest, Bun test |
| **Playwright** | Faster, better API for modern SPAs, multi-browser, network interception built in. | Cypress |
| **NextAuth v5 / Lucia** | Self-hosted, no vendor lock-in, full control over user data. Auth0 is expensive at scale. | Clerk, Auth0, Supabase Auth |
| **BullMQ** | Redis-native, TypeScript-first, battle-tested. Inngest is newer but vendor-dependent. | Inngest, Trigger.dev |
| **Pino** | Faster (10x+), smaller, JSON-native. Winston is heavier with more features than a starter needs. | Winston |
| **Sentry** | Generous free tier, excellent Next.js integration, simple setup. Datadog is overkill for a starter. | Datadog, NewRelic, Highlight |
| **Resend** | Modern API, React Email templates, generous free tier. SendGrid has DX issues and older API design. | SendGrid, Postmark, Plunk |

## When to swap

- **Need serverless DB?** Swap Postgres for Neon or Supabase (Drizzle works with both).
- **Need file uploads?** Add Uploadthing or Tigris at `packages/storage/`.
- **Need real-time?** Add WebSockets via Socket.io or Pusher at `packages/realtime/`.
- **Need AI features?** Add OpenRouter/Azure OpenAI client at `packages/ai/`.
- **Need multi-tenant?** Add `tenant_id` to all Drizzle schemas and update RBAC middleware.
