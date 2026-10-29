# Dependencies and Testing

| Dependency type | Design and validation strategy |
| --- | --- |
| Pure computation or in-process state | Prefer real implementations and verify through complete behavior interfaces without inventing extra adapters |
| Locally replaceable resources | Use appropriate test resources or explicit substitutes and check semantic differences; do not expose all internals for testing |
| Owned remote systems | Keep business logic in explicit modules and transport behind genuinely needed interfaces/adapters; retain promised checks at real boundaries |
| Third-party services | Inject interfaces for external operations and test local handling logic; verify necessary external interactions separately |

Interfaces may have internal replacement seams without exposing each as a public caller-facing interface. Logic results obtained through test adapters do not replace real storage, protocol, or cross-process guarantees.

When merging shallow modules, establish validation through the new behavior interface before assessing whether old tests are genuinely redundant. Remove redundant tests only when their independent behavior remains covered and removal is within the approved refactoring scope. Higher-level tests do not automatically justify deleting all unit tests.
