# Saas-audit

A portable Agent Skill for exhaustive, evidence-driven SaaS auditing and pre-release assurance.

It covers source code, live application behavior, security, authentication, RBAC, tenant isolation, functional QA, UI/UX, accessibility, APIs, databases, infrastructure, CI/CD, dependencies, performance, reliability, privacy, AI/LLM features, screenshots, remediation, retesting and a final ship/no-ship report.

## Added beyond the original master prompt

Threat modeling; white-label and tenant-metadata leakage; AI/LLM/RAG/vector security; supply chain/SBOM/licenses; CI/CD/cloud/IaC/container security; cache/CDN/search/analytics isolation; webhooks/queues/cron/idempotency; migration/backup/restore/RTO/RPO; observability/SLO/incident readiness; races/stale updates; and hard `SHIP`, `CONDITIONAL SHIP`, `DO NOT SHIP` gates.

## Install

Run from this directory:

```bash
./install.sh
./install.sh --project
```

Windows PowerShell:

```powershell
./install.ps1
./install.ps1 -Project
```

For Hermes, set its directory if required:

```bash
HERMES_SKILLS_DIR="$HOME/path/to/hermes/skills" ./install.sh
```

See `references/platform-installation.md`.

## Use

```text
Use the saas-audit skill to run a hybrid pre-release audit of this repository and the staging application. Read credentials from environment variables, use two tenants for isolation testing, capture screenshots, run all safe repository and browser tests, create the PDF/JSON/XLSX evidence pack, and issue a ship/no-ship verdict.
```

Never commit credentials. Use only on systems you are authorized to test.

## License

MIT. Prepared by Sourabh Bhaumik.
