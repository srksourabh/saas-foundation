# Detailed Features

This document describes the functional scope of the `saas-audit` Agent Skill.

## 1. Application discovery

The skill builds a complete testable inventory before judging quality. It identifies:

- public and authenticated routes;
- menus, submenus, tabs, modals and hidden navigation paths;
- forms, tables, filters, reports, uploads, downloads and exports;
- APIs, GraphQL operations, WebSockets, webhooks, queues and scheduled jobs;
- user roles, permissions, tenants and administrator functions;
- database schemas, policies, migrations, functions and storage buckets;
- infrastructure, CI/CD, containers, cloud resources and third-party integrations;
- AI models, prompts, tools, RAG pipelines and vector stores.

## 2. Authentication and session audit

Checks include valid and invalid login paths, password policy, reset tokens, MFA, account lockout, brute-force protection, cookies, token storage, idle timeout, absolute timeout, logout invalidation, concurrent sessions and session behavior after role or password changes.

## 3. RBAC and authorization

The skill produces an expected-versus-actual permission matrix. It tests UI, direct routes and APIs for:

- view, create, update and delete;
- approve, reject, assign and reassign;
- upload, download, import and export;
- archive, restore, configure and invite;
- role changes, impersonation and sensitive-field access;
- horizontal and vertical privilege escalation.

## 4. Multi-tenant and white-label isolation

The audit treats cross-tenant exposure as a primary release risk. It checks whether tenants can discover each other through:

- records, identifiers and API parameters;
- tenant names, domains, logos and branding;
- users, filenames and storage URLs;
- reports, exports, search and autocomplete;
- notifications, emails and webhook payloads;
- cache, CDN, analytics, logs and error messages;
- queues, cron jobs, search indexes and vector stores.

## 5. Functional QA

Every important workflow is tested with positive, negative, boundary, duplicate, malformed, interrupted, concurrent and recovery scenarios. Coverage includes CRUD operations, field validation, bulk actions, file handling, imports, exports, filters, pagination, notifications and business rules.

## 6. UI, UX and usability

The skill reviews visual consistency, navigation, action clarity, labels, error recovery, empty states, loading states, destructive actions, cognitive load, mobile behavior and first-time-user usability.

## 7. Accessibility

The audit reviews WCAG 2.2 readiness, including keyboard navigation, focus order, focus visibility, labels, semantic HTML, headings, landmarks, ARIA, contrast, zoom, touch targets, modals, dynamic announcements and accessible tables.

## 8. Security testing

Safe, non-destructive checks cover:

- injection and unsafe input handling;
- XSS, CSRF, open redirects and SSRF indicators;
- security headers and TLS behavior;
- secrets, source maps, debug endpoints and information disclosure;
- file upload and download authorization;
- browser storage and unsafe client-side authorization;
- business-logic abuse, duplicate transactions and workflow bypass.

## 9. API audit

The skill evaluates authentication, object-level authorization, function-level authorization, input schemas, mass assignment, excessive data exposure, pagination, rate limiting, CORS, content types, idempotency, replay resistance, versioning and deprecated endpoints.

## 10. Database and data integrity

Checks include constraints, null handling, unique rules, relationships, precision, time zones, transactions, retries, partial writes, orphan records, soft deletion, restoration, tenant scoping, RLS, migration safety, backup protection and sensitive-field encryption.

## 11. Infrastructure and supply chain

The skill reviews dependency vulnerabilities, lockfiles, secrets, package provenance, licenses, SBOM readiness, CI/CD permissions, environment separation, branch protection, cloud configuration, infrastructure as code, containers, rollback and deployment safety.

## 12. Reliability and resilience

Coverage includes retries, idempotency, duplicate jobs, poison messages, queue isolation, webhook replay, cron overlap, stale writes, race conditions, optimistic locking, backup restore, RTO/RPO, disaster recovery, graceful degradation and operational runbooks.

## 13. Performance

The skill captures page load, API response time, slow queries, large bundles, duplicate requests, oversized images, search latency, exports, uploads, database-backed views and safe slow-network behavior.

## 14. Privacy and compliance readiness

The audit reviews data minimization, consent, retention, deletion, correction, masking, access logs, exports, browser storage, third-party processors, encryption, backup retention and documentation gaps. It does not claim legal compliance or certification.

## 15. AI and LLM security

For AI-enabled SaaS products, the skill checks prompt injection, unsafe tool access, excessive model permissions, RAG and vector isolation, tenant-memory separation, sensitive-data leakage, insecure output rendering, untrusted uploaded content and model-failure handling.

## 16. Evidence and reporting

Every confirmed issue is expected to include reproduction steps, evidence, severity, likelihood, technical impact, business impact, confidence, root cause, workaround, permanent solution, owner, effort, validation and regression testing.

## 17. Release gate

The final outcome is one of:

- `SHIP` — required evidence passes and no release blocker remains;
- `CONDITIONAL SHIP` — manageable residual risk with explicit owners and controls;
- `DO NOT SHIP` — unresolved blocker, severe exposure, unsafe migration, failed critical checks or untested critical workflow.
