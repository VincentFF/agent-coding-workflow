# PostgreSQL Review Perspective

Use this reference when reviewing SQL queries, schema definitions, migrations, permissions, connection pooling, or transactional locking. This is a review method for the existing `code-reviewer` role; read [postgres-patterns](../../postgres-patterns/SKILL.md) and [database-migrations](../../database-migrations/SKILL.md) as needed.

1. **Complete Data Path:** Trace inputs to query parameters, transaction operations, returned rows, and caller error classification. Check for SQL injection, null handling, duplicate keys, foreign key constraints, and credential exposure.
2. **Concurrency Invariants:** For claim, lease renewal, and completion paths, trace concurrent interleavings, conditional updates, lock order, and affected rows. Using `SKIP LOCKED` does not automatically prove fairness, lease recovery, or isolation from abandoned workers. Do not hold transactions open across long external network calls.
3. **Query Plans and Indexing:** Evaluate index selection against actual query predicates, joins, and sorting requirements. Partial index predicates and covering index `INCLUDE` columns must align with actual queries. Sequential scans, random UUIDs, or `SELECT *` are not automatic blockers unless they violate performance or contract requirements.
4. **Permissions and Connection Pools:** Ensure separation of runtime credentials from migration DDL credentials. Verify that application connection pool sizing accounts for total instance count and database server capacity.
5. **Migration Safety and Recovery:** Verify migration scripts against project deployment contracts. Check for table rewrites, exclusive lock durations, non-transactional index creation failure recovery, and resumability of batch backfills.
6. **Proof Boundaries:** Check that evidence derives from real PostgreSQL integration environments where concurrency, constraints, and transactions are proven; in-memory mocks cannot prove lock behavior or transaction isolation.

Report findings under the Spec and Standards axes of [code-review](../SKILL.md).

Adapted from ECC (MIT License), based on Supabase Agent Skills (credit: Supabase team). See [ECC sources](../../agent-workflow/references/ecc-sources.md).
