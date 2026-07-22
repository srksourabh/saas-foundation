# Agent Operating Guide — <project-name>

## Read first

Read `README.md`, `PRODUCT.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md`, `SECURITY.md`, and `PROGRESS.md` before changing code.

## Repository map

<repository-map>

## Non-negotiable rules

- Implement the smallest complete change that satisfies an accepted requirement.
- Validate with the commands below before reporting completion.
- Never commit secrets, weaken auth, bypass authorization, or expose customer data.
- Update the relevant context file and `PROGRESS.md` when behaviour, architecture, risk, or status changes.

## Commands

```bash
<dev-command>
<lint-command>
<typecheck-command>
<test-command>
<build-command>
```

## Security boundaries

<authz-data-and-secret-boundaries>
