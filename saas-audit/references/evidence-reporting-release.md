# Evidence, Reporting and Release Gates

## Evidence

Name evidence `<ISSUE-ID>_<SEVERITY>_<DOMAIN>_<SHORT-DESCRIPTION>.<ext>`. Index the issue/coverage item, evidence type, route, role, tenant, viewport/browser, timestamp/timezone, commit/build/environment, redaction status and description.

Strong evidence includes reproduction, request/response or code reference, role/tenant, version/time, screenshot/log/trace, expected/actual and retest. Validate scanner alerts before confirmation.

## Finding and severity

Use `assets/finding.schema.json`. IDs use domain prefixes such as AUTH, RBAC, TEN, SEC, API, DB, FUNC, UX, UI, A11Y, PERF, REL, PRIV, CICD, INFRA, AI and OBS.

- Critical/P0: auth bypass, takeover, cross-tenant sensitive exposure/mutation, RCE, unrestricted production data, exposed secrets, severe payment manipulation or catastrophic data/availability risk.
- High/P1: major authorization failure, impactful stored XSS, sensitive disclosure/mutation, insecure file access, serious workflow bypass, unsafe migration or realistic material supply-chain/cloud weakness.
- Medium/P2: constrained security weakness, important functional defect, material UX/accessibility barrier, weak session/config, key performance/reliability issue or incomplete monitoring/recovery evidence.
- Low/P3: minor non-blocking defect, cosmetic inconsistency, limited leak, small accessibility or validation issue.
- Informational/P4: hardening, enhancement, documentation or maintainability.

Risk score = likelihood × max(technical, business, user impact): 20–25 Critical, 15–19 High, 8–14 Medium, 3–7 Low, 1–2 Informational. Explain overrides.

## Score caps

Use weighted scores: Security 20%; RBAC/tenant 15%; Functional 15%; Data/database 10%; UI/UX 10%; API 10%; Performance/reliability 8%; Accessibility 5%; Privacy 5%; Tests/maintainability 2%.

Caps: unresolved Critical ≤39; unresolved High security/RBAC/tenant ≤59; untested critical tenant/auth path ≤69; failed build or critical workflow ≤59; missing evidence cannot receive a high domain score.

## Release verdict

### DO NOT SHIP

Unresolved Critical/High blocker; exposed secret/admin path; cross-tenant leakage including unintended metadata; failed build/migration/critical tests/journey; unsafe destructive migration; no rollback/forward-fix; critical role/tenant/payment/export/recovery path untested; severe observability/recovery gap; or unstable environment invalidating results.

### CONDITIONAL SHIP

No Critical/High blocker, but material Medium risk, incomplete non-critical coverage, or a temporary mitigation with named owner, deadline, monitoring and rollback trigger.

### SHIP

No blocker; build/checks pass; critical journeys, roles, tenant boundaries and integrations pass; migration/recovery/rollback are acceptable; monitoring and ownership are ready; evidence and limitations are complete. Human release approval remains required.

## PDF report

Include cover/confidentiality, document control, verdict, scope/authorization/exclusions/limitations, methodology/tools, architecture/data flow/attack surface, coverage/inventory, scorecard, severity/category/module charts, risk heat map, RBAC/tenant matrices, journeys, domain summaries, prioritized and detailed findings with screenshots, remediation roadmap, retest/residual risk, release conditions/monitoring/rollback and command/evidence appendices.

## Final QA

Severity totals must match all artifacts; risk/severity must be consistent; links and screenshots resolve; secrets/PII are absent; test states are not converted to pass; compliance wording is qualified; verdict follows gates; and retest evidence is distinct from initial evidence.
