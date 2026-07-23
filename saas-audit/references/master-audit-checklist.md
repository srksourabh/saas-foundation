# Master Audit Checklist

This checklist preserves the user's autonomous SaaS audit brief as the exhaustive baseline. Apply every relevant item and mark each `PASS`, `FAIL`, `BLOCKED`, `NOT_APPLICABLE`, or `NOT_TESTED` with evidence.

## Discovery and inventory

Audit every page, menu, submenu, dashboard, form, button, link, modal, dropdown, tab, table, filter, search, pagination, upload/download, notification, setting, workflow, role, API, database operation and default/loading/empty/success/failure/error/responsive state. Build a sitemap, route/API inventory and feature inventory.

## Authentication and session

Test valid/invalid/empty/long/Unicode/special input, enumeration, repeated failure, lockout/rate limit/CAPTCHA, remember-me, concurrent sessions, deactivated accounts, password policy/change/reset token expiry/reuse, MFA enrollment/recovery/OTP, cookie flags, idle/absolute timeout, logout invalidation, back button, fixation, revocation, refresh tokens and browser storage.

## RBAC and authorization

Inventory roles and permissions. Build expected-versus-actual matrix for view/list/search/create/edit/delete/approve/reject/assign/import/export/download/upload/archive/restore/configure/invite/deactivate/reactivate/change-role/sensitive fields. Test horizontal and vertical escalation, direct URLs/APIs, hidden actions, object/tenant ID manipulation, server-side enforcement and multi-tenant isolation.

## Functional quality

Use positive, negative, boundary, invalid, empty, duplicate, long, Unicode, refresh, back, multi-tab, interrupted, repeated-submit, slow-network and failed-API cases. Test forms, CRUD, search/filter/sort, tables, files, exports/reports, calculations, audit logs and permission enforcement.

## User journeys and usability

Test registration/invitation/first login/profile/organization setup/team addition/first record/edit/request/approval/payment/report/export/reset/role change/deactivation/logout. Record steps, time, friction, confusion, errors, dead ends, repeated entry, recovery and improvement. Evaluate system status, real-world language, control, consistency, prevention, recognition, efficiency, hierarchy and help. Score usability 0–100.

## UI and accessibility

Review typography, hierarchy, buttons, icons, inputs, cards, tables, dialogs, spacing, grid, color, overlap, clipping, scrolling, sticky elements, responsiveness and all interaction states. Test defined mobile/tablet/desktop viewports, orientation, zoom 200%, keyboard, focus, semantic structure, names/ARIA, headings/landmarks, alt text, contrast, target size, errors, captions, dialog focus and dynamic announcements against WCAG 2.2 where applicable.

## Security

Safely test injection, XSS, CSRF, headers, TLS/mixed content, information disclosure, API auth/authorization/validation/CORS/methods/content type/replay/idempotency/versioning, browser storage, client-side secrets/routes/source maps, clickjacking, business logic, workflow/approval/payment/subscription/coupon/status/date/currency manipulation and race conditions. Use non-destructive proof only.

## Database and data integrity

Test connectivity/pooling/timeout/retry/transactions/rollback/partial writes/orphans/stale data/cache; constraints, relationships, duplicates, null/defaults, precision, dates/timezones, deletion/restoration/audit history; exposure, least privilege, RLS/policies, anonymous/service-role/storage/functions/JWT, encryption, backups and logs. Include Supabase-specific checks where relevant.

## Performance, compatibility and resilience

Measure load/interactive/API/LCP/CLS/requests/assets/bundles/DB/search/filter/export/upload under safe conditions. Test Chromium/Firefox/WebKit, desktop/tablet/mobile. Trigger invalid/unauthorized/not-found/expired-session/timeout/network/server/upload/download/save/duplicate/concurrent errors and verify safe, understandable recovery.

## Notifications, logs and privacy

Audit in-app/email/SMS/push/webhook triggers, recipients, timing, duplicates, links, permissions, preferences, timezone and sensitive data. Verify audit logs for authentication, user/role/record/config/export/API-key/billing events with actor/action/target/time/tenant/source/before-after/result and tamper resistance. Review data minimization, purpose, notice/consent, retention, deletion/export/correction, masking, encryption, processors, cross-border handling, backups, telemetry and screenshot/export leakage. Do not claim legal compliance.

## Source, dependencies and automated tests

When authorized, review architecture, auth/RBAC, APIs, queries, RLS, secrets/env, errors/logging, validation/encoding, files, dependencies, dangerous/hardcoded/debug/dead/duplicate code, type/build/lint/CI. Run safe build/type/lint/unit/integration/E2E/dependency/static/secret checks. Assess coverage of critical paths, auth, RBAC, tenant, API, database, failure, responsive, accessibility and regression tests.

## Evidence and deliverables

Capture full-page and focused screenshots with URL, role, tenant and timestamp; console/network evidence where relevant; redact credentials/PII/secrets. Record each finding with ID, classification, reproduction, evidence, risk, containment, permanent solution, validation, owner, effort and regression test.

Deliver a professional PDF, findings spreadsheet, RBAC matrix, screenshot folder, JSON findings and execution log. Include scorecard, severity/category/module charts, risk heat map, journey friction, remediation timeline and coverage.

## Severity and coverage

Use Critical/P0, High/P1, Medium/P2, Low/P3, Informational/P4 and the risk model in `evidence-reporting-release.md`. Report totals for discovered/tested pages, roles, tenants, workflows, forms, APIs, issues, screenshots, passed, failed, blocked, skipped and coverage. Never claim 100% unless genuinely complete.

## Safety

Do not damage data, conduct DoS/uncontrolled load, leave persistence, exfiltrate confidential data, upload malware, change production configuration without authorization, exploit beyond minimum proof or include plaintext credentials. Prefix and clean test data with `AUDIT_TEST_`.
