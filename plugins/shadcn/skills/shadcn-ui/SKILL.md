---
name: shadcn-ui
description: Discover, inspect, scaffold, and integrate UI components and full-page blocks from Shadcn UI and React Bits (Starter and Pro) registries via MCP.
---

# Shadcn UI & React Bits MCP Skill

This skill guides the discovery, inspection, installation, and assembly of accessible React UI components and composite blocks using the official Shadcn MCP server.

## Overview

The Shadcn MCP server allows Antigravity to interface directly with component registries:
- **`@shadcn`**: The official shadcn/ui component library (buttons, dialogs, forms, dropdowns, data tables).
- **`@reactbits-starter`**: Community and starter blocks, animations, and UI patterns.
- **`@reactbits-pro`**: Full marketing blocks, application shells, dashboards, and design recipes.

## Available MCP Tools

| Tool | Purpose |
| :--- | :--- |
| `get_project_registries` | Retrieves configured registry namespaces from `components.json`. |
| `list_items_in_registries` | Lists available items filtered by registry, type (lib, block, component, ui, hook, page, theme), and limit. |
| `search_items_in_registries` | Performs fuzzy text search on component names and descriptions across registries. |
| `view_items_in_registries` | Fetches complete source code, schema, and dependencies for specified items. |
| `get_item_examples_from_registries` | Retrieves demo implementations, code examples, and usage patterns. |
| `get_add_command_for_items` | Returns the exact `shadcn add` CLI invocation for target components. |
| `get_audit_checklist` | Delivers a verification checklist for Tailwind config, styling imports, and dependencies. |

## Workflow

### 1. Verification & Discovery
Check configured registries in the project:
- Call `get_project_registries` to view configured namespaces in `components.json`.
- Call `search_items_in_registries` with query terms like `"pricing"`, `"hero"`, `"navbar"` or filter by types.

### 2. Inspecting Code & Demos
Before adding or writing boilerplate:
- Call `get_item_examples_from_registries` with query `"{component}-demo"` to inspect live props and styling.
- Call `view_items_in_registries` to view files and dependency requirements.

### 3. Adding to the Project
Obtain the exact add command:
- Call `get_add_command_for_items` with item IDs, e.g. `["@shadcn/button", "@reactbits-starter/mono-waves-tw"]`.
- Execute via terminal:
  ```bash
  npx shadcn@latest add @shadcn/button
  ```

### 4. Post-Install Audit
- Run `get_audit_checklist` to ensure `@/components/ui/` imports, Tailwind CSS variables (`globals.css`), and font definitions are properly configured.
