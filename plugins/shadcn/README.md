# Shadcn & React Bits UI MCP Plugin

> Production Google Antigravity Plugin

## Overview
Direct CLI scaffolding of modern Tailwind CSS & React UI components, blocks, and design systems with React Bits Pro & Shadcn UI registries via Model Context Protocol (MCP).

## Features
- **MCP Server**: Stdio integration executing `npx -y shadcn@latest mcp` with 7 specialized tools.
- **Skills**: `shadcn-ui` runbook for registry search, component inspection, example fetching, and automated installation.
- **Agents**: `ui-component-engineer` subagent for automated design system composition and QA.
- **Rules**: Consolidated `rules/AGENTS.md` applied automatically when active.

## Installation
Clone or copy into your Antigravity plugins directory:
- Project level: `.agents/plugins/shadcn`
- Machine global: `~/.gemini/config/plugins/shadcn`

```bash
python scripts/install.py shadcn --scope global
```

## MCP Tools Provided
- `get_project_registries`
- `list_items_in_registries`
- `search_items_in_registries`
- `view_items_in_registries`
- `get_item_examples_from_registries`
- `get_add_command_for_items`
- `get_audit_checklist`
