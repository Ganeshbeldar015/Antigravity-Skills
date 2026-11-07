# Supabase Cloud & Postgres Behavioral Guidelines

When `supabase` is active:
1. Always enable Row-Level Security (RLS) on new Postgres tables (`ALTER TABLE <name> ENABLE ROW LEVEL SECURITY;`).
2. Write idempotent SQL migrations using `IF NOT EXISTS` guards and parameterized types.
3. Use UUIDs or identity sequences for primary keys and index all foreign key columns.
4. Separate migration operations into forward (expand) and backward (contract) stages to prevent production downtime.
