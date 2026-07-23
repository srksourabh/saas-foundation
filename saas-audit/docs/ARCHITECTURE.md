# Architecture and Workflow

## Skill architecture

`saas-audit` is intentionally split into a compact core instruction file and progressive reference modules. This allows compatible agents to load only the detail needed for the current audit phase.

```mermaid
flowchart TB
    U[User request] --> S[SKILL.md]
    S --> E[Execution playbook]
    S --> R[Security, RBAC and tenancy]
    S --> Q[Quality, UX and accessibility]
    S --> D[Data, API and infrastructure]
    S --> P[Evidence, reporting and release gates]
    S --> M[Master audit checklist]
    E --> W[Audit workspace]
    R --> F[Findings]
    Q --> F
    D --> F
    M --> F
    F --> V[JSON schema validation]
    V --> H[HTML/PDF rendering]
    H --> O[Release verdict and evidence pack]
```

## Audit control flow

```mermaid
sequenceDiagram
    actor User
    participant Agent
    participant Repo as Repository
    participant App as SaaS Application
    participant Data as Database/Infrastructure
    participant Report as Evidence Pack

    User->>Agent: Authorized scope, URL, roles and credentials
    Agent->>Repo: Read instructions, architecture and code
    Agent->>App: Discover routes and workflows
    Agent->>Data: Inspect authorized data/infrastructure controls
    Agent->>Repo: Run build, tests, lint and security checks
    Agent->>App: Execute browser/API/RBAC/tenant tests
    Agent->>Report: Store screenshots, logs and findings
    Agent->>App: Retest confirmed remediation where available
    Agent->>Report: Calculate severity, coverage and verdict
    Agent-->>User: SHIP / CONDITIONAL SHIP / DO NOT SHIP
```

## Evidence model

```mermaid
flowchart LR
    T[Test execution] --> E1[Screenshot]
    T --> E2[Console/network log]
    T --> E3[API request/response]
    T --> E4[Code/config reference]
    T --> E5[Command output]
    E1 --> F[Finding]
    E2 --> F
    E3 --> F
    E4 --> F
    E5 --> F
    F --> S[Severity and risk]
    F --> R[Remediation]
    F --> X[Retest]
    S --> G[Release gate]
    R --> G
    X --> G
```

## Trust boundaries

The audit treats the following as distinct trust boundaries:

- anonymous visitor to authenticated application;
- one user to another user;
- lower role to privileged role;
- one tenant to another tenant;
- browser to API;
- API to database and storage;
- application to third-party service;
- CI/CD to production;
- human instruction to AI agent;
- model output to tool execution;
- untrusted document to RAG/vector memory.

## Status model

Each test or finding is classified as:

- `PASS` — test executed and expected behavior observed;
- `FAIL` — test executed and defect confirmed;
- `BLOCKED` — required access, data or tool unavailable;
- `NOT TESTED` — outside scope or intentionally skipped with reason;
- `NOT APPLICABLE` — feature does not exist;
- `CONFIRMED`, `PROBABLE`, `OBSERVATION` or `FALSE POSITIVE` for finding confidence.

## Design principles

1. Evidence before claims.
2. Server-side enforcement before UI assumptions.
3. Tenant isolation across every shared subsystem.
4. Safe, non-destructive validation.
5. Coverage limitations remain visible.
6. Critical and High findings block release by default.
7. Human release authorization remains mandatory.
