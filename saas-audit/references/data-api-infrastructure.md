# Data, API, Infrastructure and Operations

## Database and data integrity

Review pooling, timeouts, retry, transactions, rollback, isolation, deadlocks, duplicate processing, partial writes, orphan records, cache invalidation and read-after-write. Check constraints, foreign keys, tenant-scoped uniqueness, null/defaults, precision, dates/timezones, soft delete/restore, audit history and retention. Independently recompute critical calculations and boundary periods.

## Migrations and database security

Verify deterministic versioned migrations, rolling-deploy compatibility, lock/runtime risk, safe backfills/nullability, index strategy, rollback or forward-fix, destructive-change backup, tenant/schema parity and production-like testing. Unsafe migration is a blocker.

Check least privilege, network/TLS, secret rotation, RLS/policies, schema permissions, functions/triggers/extensions, public access, backups, replicas, logs and encryption. For Supabase inspect RLS, service-role exposure, storage/realtime/Edge Functions, metadata privilege and JWT claims.

## API, cache, CDN and search

Compare implementation to contracts. Test validation, auth, authorization, errors/status, pagination/filter/sort, versioning, compatibility, idempotency, rate limits, retries, timeout, partial failure, telemetry and sensitive-field minimization.

Verify cache keys include tenant/identity/role/locale where required; private responses are not shared; invalidation follows data/permission changes; CDN honors private/no-store; signed URLs expire. Test search/autocomplete/analytics/vector stores for ACL and tenant isolation, stale deletion and cross-tenant aggregation.

## Integrations, webhooks and background jobs

Review OAuth scopes, secret rotation, webhook signatures/timestamps/replay, retries, idempotency, timeout, circuit breaker, dead-letter queues, ordering, duplicate delivery, tenant context and observability. Scheduled jobs/queues must not use a global/default tenant and must support safe replay/repair.

## Supply chain, CI/CD and infrastructure

Check lockfiles/reproducible builds, vulnerable/abandoned/typosquatted/unnecessary dependencies, licenses, install scripts, provenance, pinned actions/images, trusted registries, SBOM, secret scanning and update automation.

Review branch protection, required review/checks, environment approval, least-privilege tokens, fork/PR secret exposure, artifacts/provenance, deployment rights, separation of duties and rollback. Production must not bypass required gates.

Inspect IaC/cloud/container configuration for public exposure, segmentation, IAM, encryption/KMS/secrets, storage/database access, non-root containers, capabilities, images, health/resource limits, ingress/TLS/proxies, backup/retention/deletion protection, logging, environment separation, drift, autoscaling and cost controls.

## Performance, reliability and recovery

Measure representative latency/error percentiles, LCP/INP/CLS/assets, database query/N+1/index/pool behavior, search/filter/export/upload/report, queue delay and cache behavior. Use controlled tests only.

Review timeouts, jittered retries, circuit breakers, graceful degradation, idempotency, concurrency/races, health/readiness/drain, backup encryption and restore tests, tenant-level restore, RTO/RPO, failover, rollback/flags/kill switches and reconciliation. A backup without restore evidence is not proven recoverability.

## Observability, privacy and compliance readiness

Verify structured logs, trace IDs, tenant-safe context, metrics/traces/errors, alerts, dashboards, SLOs, on-call/runbooks and tamper-resistant audit logs. Ensure secrets/PII and tenant data do not leak to telemetry.

Map personal/sensitive/financial/regulated data through collection, purpose, consent/legal basis where applicable, sharing, storage, retention, export, correction and deletion. Assess user-requested DPDP/GDPR/SOC 2/ISO 27001/PCI/HIPAA readiness without claiming certification or legal compliance.
