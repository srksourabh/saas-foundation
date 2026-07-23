# Contributing

Contributions that improve audit accuracy, portability, safety, evidence quality or platform compatibility are welcome.

## Contribution principles

- Preserve safe, non-destructive testing boundaries.
- Never add instructions for unauthorized access, uncontrolled load, persistence or data exfiltration.
- Do not convert missing evidence into a passing result.
- Keep server-side authorization and tenant isolation central.
- Keep `SKILL.md` concise enough for agent loading; place detailed material in references or docs.
- Ensure instructions are platform-neutral unless a platform-specific guide is necessary.
- Avoid unsupported legal, compliance or penetration-test certification claims.

## Suggested contribution areas

- additional technology-specific audit modules;
- stronger AI/RAG/vector security checks;
- cloud-provider and infrastructure checks;
- evidence templates and report visualization;
- installation support for more Agent Skills clients;
- test fixtures and sample findings;
- accessibility and localization checks;
- performance and reliability guidance;
- false-positive reduction.

## Development workflow

1. Fork or branch from `main`.
2. Make a focused change.
3. Update relevant documentation.
4. Validate relative links and file paths.
5. Check JSON schemas and Python syntax.
6. Test installation in at least one project-local skill directory.
7. Open a pull request describing scope, reason, safety impact and validation.

## Documentation style

- Use clear, testable instructions.
- Distinguish mandatory controls from recommendations.
- Use Mermaid diagrams where they improve understanding.
- Keep examples sanitized and free of real credentials.
- Prefer relative repository links.

## Finding schema changes

Changes to `assets/finding.schema.json` should remain backward-conscious. Update the validator, examples, reporting guide and version metadata when required.

## Versioning

Use semantic versioning for material skill changes:

- patch: wording, documentation or compatible fixes;
- minor: new audit domain or compatible capability;
- major: incompatible schema, workflow or installation change.

## Pull-request checklist

- [ ] Safety restrictions preserved
- [ ] No credentials or sensitive data included
- [ ] Relative links validated
- [ ] Documentation updated
- [ ] Scripts syntax-checked
- [ ] Schema changes validated
- [ ] Installation path tested
- [ ] Release-gate behavior remains internally consistent
