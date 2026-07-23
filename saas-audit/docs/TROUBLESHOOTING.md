# Troubleshooting

## Skill is not detected

- Confirm the complete `saas-audit` folder exists in the platform's skill directory.
- Confirm the file is named exactly `SKILL.md`.
- Restart or reload the agent after installation.
- Prefer project-local installation when user-level discovery is uncertain.
- For Hermes, set `HERMES_SKILLS_DIR` or explicitly direct Hermes to read `saas-audit/SKILL.md`.

## Agent reads only the core file

Copy the complete directory. Relative links require `references`, `scripts`, `assets` and `docs` to remain beside `SKILL.md`.

## Browser screenshots are missing

The active agent may not have browser automation or screenshot capability. Mark screenshot evidence as unavailable, preserve console/API/code evidence, and report the coverage limitation. Never invent screenshot paths.

## PDF is not generated

Use the HTML output as the truthful fallback. Check Python availability and inspect:

```bash
python scripts/render_report.py --help
```

A PDF converter may be required depending on the environment. Record missing tooling in the execution log.

## Findings validation fails

Run:

```bash
python scripts/validate_findings.py --help
```

Check required fields, severity values, status values and evidence references against `assets/finding.schema.json`.

## Credentials appear in output

Stop report generation, remove the exposed artifact, rotate any real secret that may have been disclosed, redact the evidence and regenerate. Credentials must never be committed or included in the final report.

## Tenant tests cannot be completed

At least two tenants are required for strong isolation evidence. Mark cross-tenant scenarios `BLOCKED` when only one tenant is available. Do not describe tenant isolation as passed.

## Build or tests fail before the audit

Record the exact command and failure. Determine whether the failure is environmental or product-related. A failed critical build or test remains a release blocker until resolved or explicitly proven unrelated.

## Production environment is the only target

Use non-destructive checks only. Do not perform uncontrolled load, destructive data tests, password spraying, exploit chaining or configuration changes. Prefer a staging replica and clearly state the reduced coverage.

## Agent stops after finding one issue

Prompt it to continue module by module until every discovered surface has a status. A finding is not the end of the audit.

## Release verdict seems too optimistic

Verify that blocked critical workflows, missing tenant credentials, failed migrations, absent rollback, failed tests and unresolved High findings are reflected in the gate. Missing evidence is not a pass.
