# Quality Heuristics

Consult as needed when assessing maintainability. Project standards override these heuristics; do not repeat patterns already checked by tools. Treat demonstrable contract violations as defects; otherwise label findings as judgments or optional suggestions.

| Symptom | Judgment and possible action |
| --- | --- |
| Mysterious Name | The name hides responsibility; name the actual concept |
| Duplicated Code | The same logical structure appears in multiple places; consolidate genuinely shared logic |
| Feature Envy | A responsibility centers on another object's data; assess where it belongs |
| Data Clumps | The same values repeatedly travel together; assess whether they form a meaningful type |
| Primitive Obsession | Primitive types hide domain concepts; introduce small types where needed |
| Repeated Switches | Multiple places repeat the same branch mapping; centralize the mapping or choose an appropriate structure |
| Shotgun Surgery | One change requires edits in many unrelated locations; improve change locality |
| Divergent Change | One module changes for multiple unrelated reasons; assess splitting responsibilities |
| Speculative Generality | Interfaces or abstractions support future capabilities absent from the contract; remove speculative parts |
| Message Chains | Callers depend on deep navigation; assess whether internal structure leaks |
| Middle Man | A wrapper mostly forwards calls; check whether it still enforces real constraints |
| Refused Bequest | Much of an inherited contract is ignored or overridden; assess composition or remodeling |

Do not demand refactoring solely because a pattern has a name. Provide actual code locations and impact; fixes must remain within approved delivery scope.
