# Stack decisions

## Why each choice

| Choice | Why not the alternative |
|--------|------------------------|
| **Turborepo** over Nx | Lighter, faster, Vercel-native. Nx is more powerful but heavier than a SaaS starter needs. |
| **pnpm** over npm/yarn | Disk-efficient (content-addressable store), strict dependency resolution. Faster installs. |
| **Next.js 16** over Remix | Larger ecosystem, RSC out of box, Vercel deploy is one click. Remix is excellent but Next.js has more mindshare + packages. |
| **tRPC** over REST/GraphQL | End-to-end type safety with zero schema duplication. REST needs manual types. GraphQL needs codegen. tRPC infers types from your functions. |
| **Drizzle** over Prisma | Lighter (no engine binary), SQL-like API gives more control, faster CI installs. Prisma has better DX for complex relations but is heavier. |
| **Tailwind CSS v4** over CSS modules/styled-components | Utility-first is faster to iterate, v4 has the CSS-first config. No runtime CSS-in-JS cost. |
| **shadcn/ui** over MUI/Chakra | Copy-paste model (you own the code), Radix-based (accessible), no lock-in. MUI is heavier with its own design language. |
| **Vitest** over Jest | Faster (esbuild-based), ESM-native, same API as Jest. Jest is slower and has ESM issues. |
| **Playwright** over Cypress | Faster, better API for modern SPAs, multi-browser, network interception built in. |
| **NextAuth v5 / Lucia** over Clerk/Auth0 | Self-hosted, no vendor lock-in, full control over user data. Auth0 is expensive at scale. |
| **BullMQ** over Sidekiq/Inngest | Redis-native, TypeScript-first, battle-tested. Inngest is newer but vendor-dependent. |
| **Pino** over Winston | Faster (10x+), smaller, JSON-native. Winston is heavier with more features than a starter needs. |
| **Sentry** over Datadog/NewRelic | Generous free tier, excellent Next.js integration, simple setup. Datadog is overkill for a starter. |
| **Resend** over SendGrid/Mailgun | Modern API, React Email templates, generous free tier. SendGrid has DX issues and older API design. |

## When to swap

- **Need serverless DB?** Swap Postgres for Neon or Supabase (Drizzle works with both).
- **Need file uploads?** Add Uploadthing or Tigris at `packages/storage/`.
- **Need real-time?** Add WebSockets via Socket.io or Pusher at `packages/realtime/`.
- **Need AI features?** Add OpenRouter/Azure OpenAI client at `packages/ai/`.
- **Need multi-tenant?** Add `tenant_id` to all Drizzle schemas and update RBAC middleware.
