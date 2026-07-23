---
name: saas-audit
description: Perform an evidence-driven, end-to-end SaaS audit before release or after major changes. Use for source-code review, live application testing, security and privacy assessment, authentication, RBAC, multi-tenant isolation, database/API/infrastructure checks, functional QA, UI/UX, accessibility, performance, reliability, compliance readiness, screenshots, severity scoring, remediation guidance, retesting, and a final ship/no-ship report with PDF and machine-readable artifacts.
license: MIT
compatibility: Requires repository and/or authorized application access. Browser automation, terminal, test credentials, and PDF/XLSX tooling improve coverage but are not mandatory; missing capabilities must be reported as coverage limitations.
metadata:
  author: Sourabh Bhaumik
  version: "1.0.0"
  standard: Agent Skills
---

# SaaS Audit

Run a complete, non-destructive, evidence-backed audit of a SaaS product. Treat the task as a release-assurance engagement, not a superficial code review or UI walkthrough.

## Non-negotiable outcome

Produce a defensible release verdict supported by:

- code, configuration, dependency, infrastructure, database, API, and runtime evidence;
- browser screenshots of discovered pages, important states, and every confirmed visual/runtime finding;
- an RBAC and tenant-isolation matrix;
- reproducible findings with severity, risk, owner, effort, and solution;
- retest status and residual risk;
- a holistic PDF report plus JSON, spreadsheet, and execution-log artifacts when tools permit.

Never claim a test passed unless it was executed. Never infer security from a hidden button or absent UI route. Server-side authorization and data scoping are mandatory.

## Inputs

Use available inputs without repeatedly asking for information already present:

- repository path or GitHub repository;
- application URL and environment;
- application purpose and critical workflows;
- technology stack and deployment platform;
- test credentials for each role and, for multi-tenant systems, at least two tenants;
- permitted test scope and production restrictions;
- compliance profile, data classifications, and expected SLAs/SLOs;
- expected report/output directory.

Credentials must be supplied through a local ignored file, secure secret mechanism, or environment variables where possible. Never commit or print plaintext credentials. If inputs are missing, continue with the highest safe coverage and label affected tests `BLOCKED` or `NOT TESTED`.

## Operating modes

Select and record one or more modes:

1. **Code audit** — repository, tests, architecture, dependencies, configuration, migrations, infrastructure, CI/CD.
2. **Black-box audit** — deployed application through browser/API with authorized credentials.
3. **Hybrid audit** — correlate source code, database, API, logs, and runtime behavior. This is the preferred mode.
4. **Release gate** — run all available checks, retest fixes, and issue `SHIP`, `CONDITIONAL SHIP`, or `DO NOT SHIP`.
5. **Focused audit** — a narrower user-requested module, while still checking its security, RBAC, data, UX, and regression boundaries.

## Safety boundary

- Audit only systems the user is authorized to test.
- Do not perform denial-of-service, uncontrolled load, destructive exploitation, persistence, credential stuffing, or data exfiltration.
- Do not alter production configuration or real records unless explicitly authorized.
- Prefix created test data with `AUDIT_TEST_`; track and safely clean it up.
- Confirm a vulnerability using the minimum proof required.
- Mask passwords, tokens, cookies, secrets, personal data, financial data, and confidential tenant information in every artifact.
- Stop an individual test if availability, integrity, privacy, or cost is at risk.

## Required execution sequence

### 1. Establish scope and workspace

1. Record target, environment, authorization, exclusions, accounts, tools, and time.
2. Create the audit workspace using `scripts/init_audit.py` or an equivalent structure.
3. Preserve the repository state: branch, commit SHA, dependency lockfiles, environment identifiers, and deployment version.
4. Define critical assets, user roles, tenants, workflows, and data classifications.
5. Create a coverage ledger before testing.

Read [execution playbook](references/execution-playbook.md) for detailed sequencing and test-status rules.

### 2. Discover the complete attack and product surface

Inventory every accessible:

- page, route, menu, component, form, table, modal, upload/download, report, search/filter, import/export, notification, setting, and workflow;
- API endpoint, GraphQL operation, WebSocket/SSE channel, webhook, background job, queue, scheduled task, integration, storage bucket, and public asset;
- role, permission, tenant boundary, service account, administrator function, and support/impersonation path;
- database schema, migration, policy, stored function, cache, search index, analytics stream, log, backup, and data export;
- build, test, deployment, infrastructure-as-code, container, cloud, DNS, CDN, and secret-management surface;
- AI feature, prompt, tool call, model, RAG/vector store, agent, uploaded knowledge source, and output-rendering path, when present.

Use route manifests, source search, API specifications, browser crawling, network logs, database metadata, and infrastructure files. Reconcile code inventory against runtime inventory and flag orphaned, hidden, undocumented, or unreachable surfaces.

### 3. Execute audit domains

Run all applicable domains. Load the linked references when entering each domain:

- Authentication, session, RBAC, authorization, tenant isolation, business-logic security, abuse resistance, AI security: [security, RBAC and tenancy](references/security-rbac-tenancy.md).
- Functional correctness, workflows, usability, UI consistency, responsive behavior, accessibility, compatibility: [quality, UX and accessibility](references/quality-ux-accessibility.md).
- Database, API, storage, caching, integrations, infrastructure, CI/CD, supply chain, observability, resilience, performance, privacy: [data, API and infrastructure](references/data-api-infrastructure.md).
- Exhaustive field-level and page-level test catalogue: [master audit checklist](references/master-audit-checklist.md).

For every domain use positive, negative, boundary, malformed-input, unauthorized, interrupted, duplicate, concurrent, slow-network, retry, rollback, and recovery scenarios where applicable.

### 4. Mandatory tenant and RBAC proof

For multi-tenant products, use at least two tenants whenever credentials are available. Test isolation across UI, direct URL, API identifiers, search/autocomplete, exports, files, notifications, reports, cache/CDN, analytics, logs, webhooks, background jobs, email templates, filenames, branding, metadata, and error messages.

No tenant should learn another tenant's existence, name, identifiers, users, branding, data volumes, filenames, domains, or configuration unless explicitly part of the product contract. Treat confirmed cross-tenant exposure as `Critical` by default.

For every role-action pair, compare expected and actual access for view, list, search, create, update, delete, approve, assign, import, export, download, configure, invite, impersonate, deactivate, restore, and sensitive-field access. Test server-side enforcement by direct route and API calls.

### 5. Code and automated checks

When repository access exists:

1. Read project instructions and architecture before changing or running anything.
2. Identify package manager and canonical commands.
3. Run build, type-check, lint, unit, integration, end-to-end, migration, and smoke tests as available.
4. Run safe secret scanning, dependency/SCA checks, static analysis, license review, and infrastructure/container scans using installed tools.
5. Inspect authentication and authorization middleware, data access, tenant scoping, validation, serialization, error handling, file processing, cryptography, logging, and third-party calls.
6. Review migrations for forward/rollback safety and data-loss risk.
7. Review tests for critical-path, RBAC, tenant, API, failure, accessibility, and regression coverage.
8. Do not weaken checks or modify application code unless the user explicitly requests remediation.

Record exact commands, versions, outputs, failures, and skipped checks.

### 6. Runtime and browser evidence

When browser tools are available:

- capture an initial full-page screenshot and a screenshot for every discovered page or materially different state;
- capture focused evidence for every confirmed issue;
- inspect console errors and failed/slow network calls on every major page and workflow;
- test desktop, tablet, mobile, keyboard-only, zoom, empty/loading/error/success/offline states;
- record URL, role, tenant, viewport, timestamp, build/commit, and issue ID;
- redact secrets and sensitive data before report inclusion.

When screenshots cannot be captured, mark the evidence type unavailable; do not fabricate image references.

### 7. Finding discipline

Create a finding only when supported by evidence. Separate:

- `CONFIRMED` — reproduced with evidence;
- `PROBABLE` — strong evidence but incomplete confirmation;
- `OBSERVATION` — best-practice or design improvement;
- `BLOCKED` — unable to test due to access/tool/environment limitation;
- `FALSE POSITIVE` — investigated and rejected.

Every finding must contain the fields in `assets/finding.schema.json`, including exact reproduction, expected vs actual, affected role/tenant, technical and business impact, likelihood, confidence, evidence, root cause where known, immediate containment, permanent remediation, owner, effort, validation, regression test, and residual risk.

Use `Critical/P0`, `High/P1`, `Medium/P2`, `Low/P3`, or `Informational/P4`. Validate the JSON with `scripts/validate_findings.py`.

### 8. Remediation and retesting

- Prioritize containment before permanent fixes for active exposure.
- Recommend the smallest durable fix that enforces security at the correct layer.
- Include code/configuration guidance only when supported by the discovered stack.
- Add or recommend automated regression tests for every Critical/High and important Medium finding.
- Retest the original reproduction steps, adjacent roles/tenants, and likely regression surfaces.
- Never mark an issue fixed based only on a code diff; require verification evidence.

### 9. Release verdict

Read [evidence, reporting and release gates](references/evidence-reporting-release.md) before issuing the verdict.

Default verdict rules:

- **DO NOT SHIP**: unresolved Critical or High security/tenant/auth/data-integrity issue; authentication or authorization bypass; exposed secret; cross-tenant leakage; failed build or critical tests; unsafe migration; missing rollback for a material change; untested critical workflow; or evidence of likely severe production failure.
- **CONDITIONAL SHIP**: no Critical/High release blocker, but material Medium risk, incomplete non-critical coverage, or documented time-bound exceptions with accountable owners and monitoring.
- **SHIP**: no unresolved release blocker; critical workflows, roles, tenant boundaries, migrations, rollback, monitoring, and required quality/security checks have passed with evidence.

Human authorization remains required for production release. The skill supplies evidence and recommendation, not organizational approval.

## Required deliverables

Create under the chosen audit output directory:

```text
saas-audit-output/
├── reports/
│   ├── <app>_Holistic_SaaS_Audit_Report_<date>.pdf
│   ├── <app>_Holistic_SaaS_Audit_Report_<date>.html
│   └── <app>_Release_Verdict_<date>.md
├── data/
│   ├── <app>_Audit_Findings_<date>.json
│   ├── <app>_Detailed_Audit_Findings_<date>.xlsx
│   ├── <app>_RBAC_Matrix_<date>.xlsx
│   ├── coverage.json
│   └── evidence-index.json
├── evidence/<domain>/
├── logs/<app>_Audit_Execution_Log_<date>.md
└── manifest.json
```

If a format cannot be produced with available tools, create the closest truthful alternative and record the limitation. Use `scripts/render_report.py` as a portable fallback for HTML/PDF generation.

The final report must include executive summary, scope, limitations, methodology, architecture and surface inventory, overall score, severity distribution, risk heat map, RBAC and tenant matrices, user journeys, domain summaries, detailed findings with screenshots, remediation roadmap, retest results, residual risk, coverage metrics, and final release verdict.

## Completion checks

Before final response confirm:

- all discovered surfaces have a status;
- critical workflows and trust boundaries have evidence;
- every screenshot and log reference resolves;
- credentials and sensitive data are redacted;
- findings JSON validates;
- severity and release verdict are internally consistent;
- blocked and skipped tests are explicit;
- report, data, evidence, and logs are present;
- no unsupported claim of compliance, penetration-test certification, or 100% coverage is made.

Return a concise summary with score, severity counts, most serious risks, coverage, verdict, limitations, and exact artifact paths.
