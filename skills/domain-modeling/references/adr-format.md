# ADR Format

Follow project locations and numbering. Without a convention, use `docs/adr/0001-<decision>.md`, scanning the highest existing number before incrementing. The main agent allocates numbers serially for concurrent candidates to avoid collisions.

```markdown
# <Decision name>

<Context, actual decision, and rationale; usually one to three sentences>
```

Add status, rejected alternatives, and non-obvious consequences only when they provide actual information. When reopening a decision, the new ADR identifies what it supersedes; the original preserves its rationale and links to the new record. Follow project ADR states such as proposed/accepted/superseded without conflating them with Change delivery states.

Architectural shape, data ownership, cross-module interactions, technical choices with substantial migration costs, and constraints not evident in code may warrant records. Library selection, routine implementation, and temporary lack of time do not automatically justify an ADR.
