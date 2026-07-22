# Testing — <project-name>

## Strategy

| Level | Scope | Tool | Gate |
|---|---|---|---|
| Unit | domain logic and validation | <unit-tool> | required |
| Integration | data, API, auth boundaries | <integration-tool> | required |
| End-to-end | critical user journeys | <e2e-tool> | required before release |

## Commands

```bash
<lint-command>
<typecheck-command>
<test-command>
<e2e-command>
```

## Release gates

Critical journeys pass, security checks pass, migrations are validated, and production smoke checks are recorded in `DEPLOYMENT.md`.
