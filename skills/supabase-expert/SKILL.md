---
name: supabase-expert
description: Manage Supabase cloud projects, author safe Postgres schema migrations, configure Row Level Security (RLS) policies, and deploy edge functions.
---

# Supabase Expert Skill

This skill coordinates database schema management, authentication rules, RLS policies, and edge functions within the Supabase ecosystem using the official Supabase MCP server.

## Overview

Supabase combines managed PostgreSQL, Row-Level Security, Auth, Storage, and Edge Functions. The Supabase MCP server allows Antigravity to inspect tables, write migrations, and manage database security directly.

## Key Capabilities

- **PostgreSQL Migrations**: Author idempotent SQL migrations for tables, indexes, constraints, and triggers.
- **Row-Level Security (RLS)**: Design granular access policies using `auth.uid()` and user roles (`authenticated`, `anon`).
- **Database Schema Inspection**: Query active table schemas, column types, foreign keys, and indexes.
- **Edge Functions**: Deploy and configure Deno/TypeScript serverless functions connected to Supabase.

## Workflow

1. **Schema Introspection**:
   - Inspect existing tables and relations to understand database architecture before making changes.

2. **Drafting Migrations**:
   - Write standard SQL migration scripts with rollback considerations.
   - Always include `ENABLE ROW LEVEL SECURITY` and explicit `CREATE POLICY` statements.

3. **Performance Optimization**:
   - Add composite or B-tree indexes for foreign key joins and frequently queried columns.
