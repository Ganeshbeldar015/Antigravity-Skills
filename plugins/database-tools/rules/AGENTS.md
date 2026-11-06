# Database Engineering Rules

When designing or modifying database tables, queries, or migrations:
1. Always use parameterized queries or prepared statements. Never concatenate untrusted variables into raw SQL strings.
2. Always add foreign key indexes for columns involved in joins.
3. Every table must have a primary key (`id BIGINT GENERATED ALWAYS AS IDENTITY` or `UUID`).
4. Never store monetary amounts as floating-point numbers; use `NUMERIC`/`DECIMAL` or integer cents.
5. All migrations must be idempotent and tested against non-empty schemas.
