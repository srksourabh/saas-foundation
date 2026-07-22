# Security — <project-name>

## Data and access

- Data classification: <classification>
- Authentication: <auth-method>
- Authorization: <roles-and-tenancy-boundary>

## Required controls

- Validate all untrusted input at the boundary.
- Enforce authorization server-side for every data operation.
- Keep secrets in the deployment secret manager; commit only examples.
- Use TLS, secure headers, rate limits, audit logging, dependency scanning, and least privilege.

## Incident readiness

Owner: <owner>. Detection: <monitoring>. Response and rollback: see `DEPLOYMENT.md`.
