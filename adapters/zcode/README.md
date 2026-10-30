# ZCode adapter

## Installed paths

| Source | Target in project |
| --- | --- |
| `adapters/zcode/agents/*.md` | `.zcode/agents/` |

## Role capabilities

| Role | Tools | Notes |
| --- | --- | --- |
| `implementer` | Read, Write, Edit, Bash, TodoWrite | May edit files |
| `code-reviewer` | Read, Bash | Read-only by role instruction |
| `oracle` | Read, Bash | Read-only by role instruction |

## Read-only limitation

ZCode role files do not create a filesystem sandbox. The `code-reviewer` and `oracle` roles keep `Bash` for inspection, so **read-only behaviour depends on the role instruction being followed**, not on enforced isolation. Report this honestly in the project workflow file instead of claiming enforced read-only.

## Model configuration

Role files do not pin a model. ZCode uses the host default; set `model` only if the project requires a specific one. `thoughtLevel` is a local tuning choice.

## Independent review

Whether a ZCode subagent inherits the parent conversation depends on how it is launched. The main agent must launch the reviewer without inheriting the implementer's context. If the runtime cannot establish a fresh context, report the review gate unresolved rather than claiming independence.

## Skill discovery and verification

ZCode discovers project skills under `.agents/skills/`. You can inspect discovered skills with:

```bash
zcode skills list --cwd /path/to/project --json
```

When delegating work to subagents, the main agent must pass the resolved absolute path to the required skill rather than relying on subagent discovery.

## Verification

After installation, confirm:

- `.zcode/agents/implementer.md`, `code-reviewer.md`, `oracle.md` exist with valid frontmatter.
- Reviewer and oracle roles still list only read-oriented tools.
- No model pin was introduced unless the project intentionally set one.
