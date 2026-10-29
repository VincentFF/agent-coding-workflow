# pi adapter

## Installed paths

| Source | Target in project |
| --- | --- |
| `adapters/pi/agents/*.md` | `.pi/agents/` |

## Role capabilities

| Role | Tools | Notes |
| --- | --- | --- |
| `implementer` | read, write, edit, bash | May edit files |
| `code-reviewer` | read, bash | `defaultContext: fresh` requests a fresh context |
| `oracle` | read, bash | Read-only by role instruction |

## Read-only limitation

Like ZCode, pi role files do not create a filesystem sandbox. Read-only behaviour depends on the role instruction. Report what the runtime actually enforces.

## `defaultContext: fresh`

This field requests that the reviewer not inherit the parent conversation. Verify that the installed pi plugin version honours it; if it does not, the main agent must establish isolation another way or report the gate unresolved. Do not assume the field works because it is present.

## Model configuration

Role files do not pin a model; pi uses the host default. Editing an installed role file requires `/reload` in pi.

## Verification

After installation, confirm:

- `.pi/agents/implementer.md`, `code-reviewer.md`, `oracle.md` exist with valid frontmatter.
- `code-reviewer.md` retains `defaultContext: fresh` unless the runtime cannot honour it.
- No model pin was introduced unless the project intentionally set one.
