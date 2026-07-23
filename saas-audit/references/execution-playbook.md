# Execution Playbook

Use this reference at the start of every audit and whenever coverage becomes unclear.

## Audit states

Every page, endpoint, workflow, role-action pair, tenant boundary, test case, and finding must have one state: `DISCOVERED`, `IN_PROGRESS`, `PASS`, `FAIL`, `BLOCKED`, `NOT_APPLICABLE`, `NOT_TESTED`, `RETEST_PASS`, or `RETEST_FAIL`.

`NOT_TESTED` is not a pass. `NOT_APPLICABLE` requires a reason.

## Preflight

Record application, environment, URL, repository, branch, commit, deployment ID, audit date/time/timezone, authorization, prohibited tests, test accounts, roles, tenant assignments, MFA constraints, sensitive data, compliance profiles, critical workflows, supported browsers/devices, SLOs, RTO/RPO, output directory and redaction rules.

Check reachability, login, repository state, tool/browser/package-manager/database/cloud access, and current incident/degradation status.

## Workspace

Use `scripts/init_audit.py --app <slug> --output <path>` or create the same structure manually. Never store credentials in audit artifacts.

Maintain `coverage.json`, execution log, evidence index, test-data cleanup ledger, and limitations log.

## Discovery sources

Correlate route files, router manifests, navigation configuration, feature flags, API specifications, handlers, network capture, database schemas/migrations/policies/functions/triggers, component stories, tests, fixtures, seed files, queues, cron, webhooks, email templates, cloud/IaC, DNS, CDN, storage, CI/CD, browser crawl, public assets, source maps, analytics and audit logs.

Flag code-only routes, runtime-only endpoints, stale flags, dead features, undocumented admin paths, orphaned APIs and unreachable pages.

## Risk-first order

1. Authentication and account recovery.
2. Super-admin, support and impersonation.
3. Tenant isolation and sensitive data.
4. Role-changing, approval, financial, billing, export, upload and destructive actions.
5. Critical journeys and business logic.
6. Database, migrations, backups and rollback.
7. API, integrations, webhooks, queues and scheduled jobs.
8. Security configuration, dependencies, CI/CD and cloud/IaC.
9. Error handling, reliability, observability and performance.
10. UI/UX, accessibility, compatibility and content.

Stop and escalate immediately for active critical exposure.

## Test design

Derive cases from role, tenant, state transition, input boundary, success/failure/retry/cancel, duplicate/idempotency, concurrency/stale update, dependency failure, device/browser/viewport/keyboard/zoom, localization/timezone/currency, privacy, audit logging and notifications.

Use pairwise reduction for large combinations, but never reduce critical role/tenant boundaries.

## Browser procedure

For every major page/workflow record URL, title, role, tenant, viewport and build; capture the initial screenshot; inspect console/network; exercise default, empty, loading, success, validation, error, disabled, unauthorized and recovery states; test keyboard and responsive layouts; capture findings immediately; update coverage before moving on.

## Code procedure

Read project instructions and architecture. Map stack, modules, trust boundaries and data flow. Derive canonical commands from package scripts/CI. Run non-mutating checks first. Inspect auth, RBAC, tenant scoping, validation, database access, file handling, external calls, logging and secrets. Trace runtime findings to code/tests. Record file, line and commit.

## Evidence quality

Strong evidence contains reproducible steps, request/response or code reference, role/tenant context, timestamp/version, screenshot/log/trace, expected/actual behavior and retest result. A scanner alert without validation is `PROBABLE` or `OBSERVATION`, not automatically confirmed.

## Completion

Calculate coverage separately for pages, workflows, roles, tenants, APIs, forms, reports/exports, integrations, critical controls and automated checks. Avoid one blended number hiding weak areas.
