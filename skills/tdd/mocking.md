# Mocking and Dependency Substitution

Prefer real in-process logic. Do not mock your own module merely to prove an internal method was called; observe results through agreed interfaces.

| Dependency | Default strategy | Proof scope |
| --- | --- | --- |
| Pure computation or in-process state | Real implementation | Interface behavior and in-process state transitions |
| Database or filesystem | Prefer suitable real test resources; use explicit local substitutes when necessary | Substitutes with semantic differences do not prove every guarantee of the real resource |
| Owned remote systems | Inject a test adapter behind an existing interface and retain required boundary validation | In-memory adapters prove logic, not transport or cross-process properties on their own |
| Third-party services | Mock/test adapter at the system boundary | Proves local handling; third-party interaction guarantees need appropriate contract or integration checks |
| Time and randomness | Inject controllable sources | Deterministic logic; does not automatically prove actual scheduling or races |

Inject dependencies at system boundaries rather than constructing irreplaceable clients inside internal logic. Shape interfaces around concrete operations and return values; avoid inventing general-purpose fetchers with many conditional branches just for testing.

Substitution follows approved validation scope; do not lower that scope to fit tests. Add interfaces only for real variants or necessary isolation; do not abstract every internal object.
