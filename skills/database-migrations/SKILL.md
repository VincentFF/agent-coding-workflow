---
name: database-migrations
description: Analyze PostgreSQL schema and data migrations, locking behavior, table rewrites, batch backfills, and rollback safety under project deployment contracts.
license: MIT
---

# Database Migration Patterns

Use this skill when designing schema changes, adding indexes, planning data backfills, or evaluating migration safety. Adhere to the project's existing migration tools and deployment contracts before applying generic strategies. This skill does not execute production DDL or start agents.

## Project Deployment Contracts Take Precedence

Always inspect the project's migration tooling and deployment procedures before proposing migration plans:

- Follow the project's deployment strategy: if the project deploys via scheduled maintenance or stops old binaries before applying migrations, align with that contract. If the project requires rolling zero-downtime deployments, apply backward-compatible expand-contract patterns.
- Existing migrations are immutable once deployed. Fix errors with new forward migrations; do not edit previously applied migration files or force ledger revisions without authorization.
- Separate schema DDL from data backfills (DML). Never execute long-running data updates inside the same transaction as schema alterations.

## Migration Analysis Sequence

1. **Dependency and Data Risk:** Map which columns, constraints, and tables old and new code read and write. Identify whether existing rows satisfy new constraints. Renaming, dropping, or narrowing column types requires an explicit data migration strategy.
2. **Locking and Rewrite Costs:** Identify the lock level acquired by each statement (`ACCESS EXCLUSIVE`, `SHARE UPDATE EXCLUSIVE`, etc.) and whether PostgreSQL must rewrite the table. Adding nullable columns without defaults or with constant defaults in modern PostgreSQL avoids table rewrites, but still acquires short locks. Adding non-null constraints without validation on large tables locks writes.
3. **Transaction Boundaries:** Group atomic DDL changes into a transaction if supported by the migration runner. `CREATE INDEX CONCURRENTLY` cannot run inside a transaction block and may leave an invalid index on failure; verify tool support and failure recovery before prescribing concurrent index creation.
4. **Batch Backfills:** Backfill large datasets in bounded batches using primary key or cursor ranges. Avoid batch updates in a single long transaction that inflates WAL and holds locks. Ensure backfills are resumable after failure.
5. **Verification in Isolated Environments:** Test migrations against realistic data volumes in isolated test environments: verify existing data compatibility, constraint enforcement, application startup, and query execution before applying to production.

## Conditional Expand-Contract Patterns

When zero-downtime rolling deployments are explicitly required by project contract, use multi-phase expand-contract changes:

1. **Expand:** Add new columns, tables, or nullable fields. Deploy new code that writes to both old and new representations while continuing to read from the old.
2. **Backfill:** Migrate legacy rows to populate the new representation in bounded background batches.
3. **Switch:** Deploy code that reads from the new representation and writes to both (or just the new).
4. **Contract:** Remove references to the old representation in code, then drop deprecated columns/tables in a final migration.

Do not assume expand-contract is necessary if the project explicitly uses maintenance windows or stopped-process upgrades.

Adapted from ECC (MIT License). See [ECC sources](../agent-workflow/references/ecc-sources.md).
