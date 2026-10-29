# Glossary Format

Follow the project's existing location. Without a convention, create a root `GLOSSARY.md` only when the first actual concept needs alignment.

```markdown
# <Project or domain context>

## Language

**<Canonical concept name>**: <One or two sentences defining the concept>

Avoid: <Actually used synonyms that are easily confused>
```

Prefer existing domain language. Add terms to avoid only for actual ambiguity. Definitions do not contain implementation details or requirement acceptance criteria.

If multiple genuinely distinct domain contexts already exist, use an existing `GLOSSARY-MAP.md` to point to their glossaries. Small projects need no map or multiple glossaries in advance. Clarify uncertain boundaries first; do not invent contexts to fit a directory structure.
