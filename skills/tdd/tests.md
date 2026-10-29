# Behavior Test Examples

## Different Ways to Observe the Same Behavior

| Goal | Inappropriate assertion | Appropriate assertion |
| --- | --- | --- |
| A user can be found after creation | A private repository was called once | Create through the public creation interface, then read required fields through the public query interface |
| An operation is denied without permission | An internal authorization function returns false | Invoke the agreed entry point and check the contract's rejection result and side effects |
| Add two prices | Compute the expected value with the same reduce algorithm | Use an independent known example: 10 plus 5 totals 15 |
| Data remains readable after restart | An in-memory fake returns a previously written value | Restart across the promised real storage and process boundaries, then read through the public interface |

Assert internal call counts or ordering only when they are themselves approved observable contracts. Same-process caches or fake results cannot substitute for persistence goals.

## Test Validity

- Names describe capabilities or failure scenarios, not internal steps.
- Use public interfaces and remain valid through internal structural changes.
- Expected results are independent, not generated from current output or implementation algorithms.
- Confirm the runner actually executes tests and assertions are awaited rather than swallowed.
- Control time, randomness, and external state; distinguish symptoms from test-environment failures.
- Explain which violation of target behavior would cause the test to fail.

Test one complete behavior, implement it, then move to the next. Checking only that no error was thrown usually cannot prove required outcomes and side effects.
