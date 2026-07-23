# Usage Guide

## Before starting

Provide as much of the following as safely possible:

- repository path or GitHub repository;
- staging or test URL;
- application purpose and critical workflows;
- technology stack;
- roles and expected permissions;
- at least two tenants for isolation testing;
- authorized credentials through environment variables;
- production restrictions and prohibited tests;
- expected output directory;
- known compliance or data-classification requirements.

Missing inputs should reduce the stated coverage, not cause fabricated results.

## Recommended full audit prompt

```text
Use the saas-audit skill to perform a complete hybrid pre-release audit of this repository and the staging application.

Objectives:
1. Discover every accessible page, route, workflow, API, role, tenant boundary, database operation, integration, job and deployment surface.
2. Audit source code, authentication, sessions, RBAC, server-side authorization, tenant isolation, database, APIs, storage, cache, security, UI/UX, accessibility, performance, infrastructure, CI/CD, dependencies, privacy, reliability and critical user journeys.
3. Use all available roles and at least two tenants. A tenant must not discover another tenant's name, identifiers, users, records, files, branding, reports, notifications, metadata or configuration.
4. Run only safe, non-destructive tests. Read credentials from environment variables. Never expose credentials or personal data.
5. Capture screenshots, console/network evidence, API evidence, code references and command outputs.
6. Create the findings JSON, findings spreadsheet, RBAC matrix, coverage ledger, evidence index, execution log, holistic PDF/HTML report, remediation roadmap and final release verdict.
7. Retest confirmed fixes and adjacent role/tenant boundaries.
8. Issue SHIP, CONDITIONAL SHIP or DO NOT SHIP based strictly on evidence.
```

## Code-only audit

```text
Use saas-audit in Code Audit mode for this repository. Do not access any deployed environment.

Review architecture, authentication, authorization, tenant scoping, API routes, database access, migrations, file handling, dependencies, secrets, CI/CD, infrastructure, error handling, logging and automated test coverage.

Run the canonical build, type-check, lint, unit, integration and safe security checks. Record exact commands and outputs. Identify runtime tests that remain blocked because no application URL or credentials were supplied.
```

## Black-box audit

```text
Use saas-audit in Black-box mode for the authorized staging URL. Do not inspect or modify source code.

Map all accessible pages and workflows, test authentication, RBAC, tenant isolation, APIs, forms, files, reports, UI/UX, accessibility, responsive behavior, performance and error recovery. Capture evidence and create the final report with explicit coverage limitations.
```

## RBAC-focused audit

```text
Use saas-audit to perform an exhaustive RBAC and authorization audit.

Build an expected-versus-actual matrix for every role, module and action. Test direct URLs and APIs for view, create, update, delete, approve, reject, assign, export, download, configure, invite, role change and sensitive-field access. Verify server-side enforcement and test horizontal and vertical privilege escalation.
```

## Multi-tenant isolation audit

```text
Use saas-audit to test Tenant A and Tenant B isolation.

Test cross-tenant leakage through UI, APIs, identifiers, search, autocomplete, files, exports, reports, notifications, branding, error messages, cache, CDN, analytics, logs, webhooks, background jobs, email templates, search indexes and vector stores. Treat confirmed cross-tenant exposure as Critical unless clearly proven otherwise.
```

## UI/UX and accessibility audit

```text
Use saas-audit to audit every accessible page for user experience, usability, visual consistency, responsive behavior and WCAG 2.2 readiness.

Test desktop, tablet, mobile, keyboard-only navigation, focus, 200% zoom, loading, empty, error, success and offline states. Capture a page inventory and screenshots for every material issue.
```

## API and database audit

```text
Use saas-audit to review API and database security, correctness and tenant isolation.

Check authentication, object/function authorization, schemas, mass assignment, data exposure, pagination, rate limits, CORS, idempotency, replay, transactions, constraints, RLS, migrations, backups, storage policies, caching and data consistency. Do not run destructive queries.
```

## AI-enabled SaaS audit

```text
Use saas-audit to audit all AI/LLM features in this SaaS product.

Test prompt injection, untrusted uploaded content, tool permissions, sensitive-data disclosure, RAG and vector-store tenant isolation, memory separation, output rendering, model failure handling, logging, cost abuse and unsafe autonomous actions. Correlate AI risks with existing RBAC and tenant policies.
```

## Release-gate audit

```text
Use saas-audit in Release Gate mode against the current release candidate.

Verify critical workflows, migrations, rollback, monitoring, alerts, RBAC, tenant boundaries, security tests, regression tests and unresolved findings. Retest all Critical, High and material Medium fixes. Produce a final SHIP, CONDITIONAL SHIP or DO NOT SHIP recommendation with evidence and residual risk.
```

## Focused module audit

```text
Use saas-audit to audit the Billing module only, including its upstream and downstream security, RBAC, tenant, API, database, payment, notification, reporting and regression boundaries. Do not treat the module as isolated from shared services.
```

## Expected agent behavior

The agent should:

1. establish scope and safety rules;
2. create the audit workspace;
3. inventory surfaces;
4. run tests systematically;
5. capture evidence continuously;
6. distinguish confirmed, probable, observational and blocked items;
7. avoid unsupported security or compliance claims;
8. produce complete artifacts and exact paths;
9. stop risky tests without abandoning safe remaining work.
