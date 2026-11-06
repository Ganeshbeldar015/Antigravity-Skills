---
name: schema-architect
description: Use this skill when designing database schemas, writing table migrations, defining foreign key constraints, or modeling entities in relational and document databases.
---

# Schema Architect Skill

Expert guidance for relational (PostgreSQL, MySQL, SQLite) and document (MongoDB, Firestore) schema design and migration management.

## 1. Principles of Resilient Schema Design
- **Normalization vs Pragmatic Denormalization**: Strive for 3NF for transactional OLTP consistency; selectively denormalize only for read-heavy query access patterns.
- **Explicit Invariants**: Enforce constraints in the database tier (`CHECK`, `NOT NULL`, `UNIQUE`, `FOREIGN KEY ON DELETE RESTRICT/CASCADE`) rather than relying solely on application-layer validation.
- **Data Types**: Use exact scalar types (`timestamptz` for timestamps, `numeric`/`decimal` for currency, `uuid` or `bigint` for surrogate keys).

## 2. Migration Authoring Workflow
1. **Reversibility**: Always pair an `up` migration with an idempotent, verified `down` migration.
2. **Zero Downtime**: Add new columns as nullable or with defaults before updating application code; never drop or rename active columns in a single deploy step.
3. **Index Creation**: In production databases, create indexes concurrently (`CREATE INDEX CONCURRENTLY` in Postgres) to avoid table lockup.

