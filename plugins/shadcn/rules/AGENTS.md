# Shadcn & React Bits Behavioral Guidelines

When `shadcn` is active:
1. Always inspect `components.json` and registered namespaces (`@shadcn`, `@reactbits-starter`, `@reactbits-pro`) before authoring custom UI elements.
2. Query the shadcn MCP server using `search_items_in_registries` or `list_items_in_registries` to discover official, accessible components and blocks.
3. For implementation details and interactive code snippets, retrieve verified patterns via `get_item_examples_from_registries` and `view_items_in_registries`.
4. Provide the exact CLI command from `get_add_command_for_items` (e.g. `npx shadcn@latest add ...`) or install automatically where appropriate.
5. After generating or scaffolding components, invoke `get_audit_checklist` to verify Tailwind CSS configuration, Lucide icons, variant setups, and accessibility standards.
