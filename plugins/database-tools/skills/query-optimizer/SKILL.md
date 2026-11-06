---
name: query-optimizer
description: Use this skill when profiling slow SQL queries, analyzing EXPLAIN ANALYZE execution plans, resolving N+1 queries, or designing composite indexes.
---

# Query Optimizer Skill

Systematic approach for database query performance tuning, index engineering, and execution plan optimization.

## 1. Execution Plan Inspection
- Run `EXPLAIN (ANALYZE, BUFFERS, VERBOSE)` on PostgreSQL or `EXPLAIN QUERY PLAN` on SQLite.
- Identify:
  - **Sequential / Table Scans**: Filter operations missing index coverage on large row sets.
  - **Nested Loop Joins on Large Tables**: Usually indicates missing foreign key indexes.
  - **Sort Memory Spills**: Disk sorts caused by undersized work memory or unindexed `ORDER BY`.

## 2. Index Optimization Patterns
- **Covering Indexes**: Include frequently selected columns (`INCLUDE (col1, col2)`) to enable Index-Only Scans.
- **Index Column Ordering**: Place equality condition columns first (`WHERE status = 'active'`), followed by range/sort columns (`AND created_at >= NOW()`).
- **Eliminating N+1 Queries**: Replace iteration queries with bulk `JOIN`, `WHERE IN (...)`, or ORM prefetching (`select_related`, `prefetch_related`).

