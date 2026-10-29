# Codex adapter

## Installed paths

| Source | Target in project |
| --- | --- |
| `adapters/codex/agents/*.toml` | `.codex/agents/` |

## Role capabilities

| Role | Sandbox | Notes |
| --- | --- | --- |
| `implementer` | `workspace-write` | May edit files in the workspace |
| `code-reviewer` | `read-only` | Independent read-only review is enforced by the sandbox |
| `oracle` | `read-only` | Read-only technical advice |

## Model configuration

Role files do not pin a model. Codex uses the model configured for the project or user; set `model` in the role TOML only if the project requires a specific one. Reasoning effort is a local tuning choice, not a workflow requirement.

## Independent review

Codex agent files do not control conversation inheritance. The main agent must still launch the reviewer so that it does not inherit the implementer's conversation, and must supply the original contracts and the complete change scope. Sandbox read-only prevents writes but does not itself make the review independent.

## Skill discovery

Skills live in `.agents/skills/`. The main agent hands the implementer the absolute path to `tdd` and the reviewer the absolute path to `code-review`. Do not rely on Codex discovering the skill collection automatically.

## Verification

After installation, confirm:

- `.codex/agents/implementer.toml`, `code-reviewer.toml`, `oracle.toml` parse as TOML.
- The reviewer role keeps `sandbox_mode = "read-only"`.
- No model pin was introduced unless the project intentionally set one.
