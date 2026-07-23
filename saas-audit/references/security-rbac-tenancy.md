# Security, RBAC and Tenancy

## Authentication and identity

Test registration, invitation, verification, login, logout, password change/reset, MFA, recovery, SSO/OAuth/OIDC/SAML, magic links, session revocation, account deletion/deactivation and support recovery.

Verify generic errors prevent enumeration; rate limits resist abuse; reset/invite links are random, scoped, single-use and expiring; cookies use Secure, HttpOnly and appropriate SameSite; sensitive responses are not cached; logout/password/role/deactivation changes revoke sessions; tokens are not leaked to URLs, logs, analytics or unsafe browser storage; MFA recovery cannot be bypassed; OAuth validates redirect URI, state, nonce, PKCE, issuer and audience; SSO/JIT/SCIM cannot join or provision the wrong tenant.

## Authorization and RBAC

Create an expected-versus-actual permission matrix. Test every role/action through UI, direct URL, API/GraphQL, modified IDs, hidden controls, bulk operations, import/export, mobile/legacy APIs and cached/shared links.

Authorization must be server-side, deny-by-default, consistently applied and checked at object, function, field and tenant scope.

Review role creation/inheritance, custom permissions, default roles, privilege changes, support/admin impersonation, self-approval, ownership transfer and break-glass accounts.

Flag horizontal/vertical escalation, sensitive fields returned but hidden, mass assignment of role/tenant/owner/status/price/approval, stale permissions, editable metadata used for privilege, client-only authorization and admin APIs without explicit policy.

## Multi-tenant isolation

Use Tenant A and Tenant B with same-role and different-role accounts. Test records, users, tenant names/IDs/counts, search/autocomplete, recent items, dashboards, exports, files/signed URLs/CDN, notifications, email/SMS/push, webhooks, queues, cron, analytics, logs, support consoles, shared links, cache keys, search indexes, vector stores, realtime channels, backups/restores, imports/deletion, feature flags, branding/domains, billing, quotas and entitlements.

Manipulate identifiers in path, query, body, header, cookie, JWT claim, GraphQL variables, file URL, websocket channel and webhook payload.

For schema-per-tenant, verify safe schema selection, identifier validation, connection-pool reset, migration parity, backup/restore isolation, search-path safety, job context and no default/shared fallback. For shared schema, verify mandatory tenant predicates/RLS, tenant-scoped uniqueness and safe joins/aggregations.

White-label products must not leak another customer's name, logo, domain, sender, template, support link, storage path, analytics label, error text, cached asset or metadata. Confirmed cross-tenant disclosure or mutation is Critical by default.

## Application security

Safely test SQL/NoSQL/LDAP/command/template/HTML/header injection; stored/reflected/DOM XSS; CSRF; SSRF; open redirect; path traversal; insecure deserialization; prototype pollution; mass assignment; XXE where applicable; request splitting/smuggling indicators; host-header/reset poisoning; clickjacking; headers; CORS; unsafe upload/MIME/SVG/archive handling; source maps/debug/backup/.git/env/secrets exposure; vulnerable dependencies; cryptographic misuse; race conditions and TOCTOU.

Use inert canaries and minimum proof. Do not upload malware or execute destructive payloads.

## API, realtime and business logic

Check authentication, object/function/field authorization, validation, output minimization, method/content type, pagination/complexity, rate/cost limits, idempotency/replay, versioning, deprecated endpoints, GraphQL depth/batching, websocket authorization/token expiry, signed URL scope, webhook signature/timestamp/replay and secret rotation.

Attempt workflow/approval bypass, duplicate/concurrent submission, negative/overflow values, self-approval, status/date/currency/ownership manipulation, subscription/trial/coupon/payment bypass, quota bypass, import/export abuse and notification/resource-cost amplification.

## AI and LLM features

Test direct/indirect prompt injection, system prompt/secret/connector/cross-tenant leakage, unsafe tools and autonomy, RAG/vector ACL isolation and poisoning, unvalidated model output, memory isolation, provider retention/privacy, jailbreaks of protected workflows, token/tool/loop cost abuse and hallucinated high-impact actions. AI output is untrusted input; enforce authorization and validation outside the model.
