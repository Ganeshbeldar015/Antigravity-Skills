# Supabase Cloud & Postgres MCP Plugin

> Production Google Antigravity Plugin

## Overview
Official Supabase MCP integration. Connects Antigravity to Supabase cloud projects for Postgres schema migrations, database inspection, edge functions, and Row-Level Security (RLS) policies.

## Features
- **MCP Server**: Stdio integration executing `npx -y @supabase/mcp-server-supabase@latest`.
- **Skills**: `supabase-expert` for schema management, RLS policies, and migrations.
- **Agents**: `supabase-architect` cloud database architect.
- **Rules**: Consolidated `rules/AGENTS.md` applied automatically when active.

## Installation
Clone or copy into your Antigravity plugins directory:
- Project level: `.agents/plugins/supabase`
- Machine global: `~/.gemini/config/plugins/supabase`

```bash
python scripts/install.py supabase --scope global
```

## Configuration
Requires Supabase Personal Access Token:
```bash
set SUPABASE_ACCESS_TOKEN=your_token_here
```
