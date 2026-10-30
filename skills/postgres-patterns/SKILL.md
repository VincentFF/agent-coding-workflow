---
name: postgres-patterns
description: Analyze PostgreSQL queries, index selection, schema constraints, connection pooling, and transaction concurrency with plan evidence.
license: MIT
---

# PostgreSQL Analysis Patterns

Use this skill when designing schemas, writing queries, troubleshooting slow queries, or analyzing locking and connection behavior in PostgreSQL. Adhere to the project's existing database architecture and migration contracts before applying generic recommendations. This skill does not start agents.

## Query Plans and Index Selection

1. Identify the full query, parameter types, execution frequency, expected row counts, and caller requirements. Check for N+1 query patterns and unnecessary column selection (`SELECT *`).
2. Run `EXPLAIN` in an authorized isolated environment. When execution is required, use `EXPLAIN (ANALYZE, BUFFERS)`. Remember that `ANALYZE` executes the statement; never run modifying queries (`INSERT`, `UPDATE`, `DELETE`) or side-effecting functions under `ANALYZE` as a read-only diagnostic.
3. Compare estimated vs actual rows, buffers hit/read, loops, filter removals, and sort spill. Sequential scans on small tables or low-cardinality queries are often optimal; do not add indexes simply because a sequential scan appears.
4. Select index types based on query operators and write costs:

| Query Need | Index Choice and Verification |
| --- | --- |
| Equality, range, sort (`=`, `<`, `>`, `ORDER BY`) | B-tree. Composite indexes should place equality columns first, followed by range/sort columns; verify with actual query plans. |
| Stable query subset filter | Partial index (`WHERE condition`). Predicate must match the query clause. Verify parameterized query planning. |
| High read-to-write ratio, index-only scans | Covering index with `INCLUDE (col1, col2)`. Index-only scans depend on visibility maps and vacuum frequency. |
| JSONB containment (`@>`), full-text search (`@@`) | GIN index. Select appropriate operator class (`jsonb_ops` vs `jsonb_path_ops`) based on query expressions. |
| High physical correlation with range filters | BRIN index for append-only or physically sorted time-series data. Check correlation and block range settings. |

Use cursor-based pagination with deterministic sorting and unique tie-breakers. Avoid naive `OFFSET` on large datasets. Parameterize all queries; treat dynamic table or column identifiers with strict whitelisting.

## Schema, Transactions, and Queues

- Model actual domain invariants with database constraints (`PRIMARY KEY`, `UNIQUE`, `FOREIGN KEY`, `NOT NULL`, `CHECK`). Do not use untyped JSONB as a substitute for relational columns that require relational integrity.
- Use appropriate data types: `timestamptz` for timestamps, `numeric` or integers for financial amounts (avoid floating point), and `text` with check constraints for bounded strings.
- Keep transactions short and focused purely on database operations. Never hold database transactions across external network calls or LLM invocations.
- Order lock acquisition consistently across concurrent transactions to prevent deadlocks.
- For worker queues, use `SELECT ... FOR UPDATE SKIP LOCKED` to minimize concurrency contention. Atomic claim-and-update requires explicit lease expiration, recovery of timed-out jobs, and idempotency guarantees.
- Size connection pools based on database server capacity, application instance count, and transaction durations. Account for connection acquisition timeouts and idle transaction timeouts.

## Security and Observability

- Enforce least privilege: separate runtime application credentials from DDL/migration credentials. Never log raw database credentials or sensitive query parameters.
- If using Row Level Security (RLS), verify role bypass rules (`BYPASSRLS`), `USING` vs `WITH CHECK` clauses, and session context isolation.
- Inspect `pg_stat_user_tables`, index usage statistics, lock waiting states, and `pg_stat_statements` (when installed) to diagnose performance issues. Never execute `ALTER SYSTEM` or install unapproved extensions automatically.

Adapted from ECC (MIT License), based on Supabase Agent Skills (credit: Supabase team). See [ECC sources](../agent-workflow/references/ecc-sources.md).
