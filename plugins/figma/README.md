# Figma Design Connect MCP Plugin

> Production Google Antigravity Plugin

## Overview
Official Figma MCP integration. Connect AI agents directly to Figma files, inspect design tokens, extract vector components, and convert design nodes to clean React/HTML code.

## Features
- **MCP Server**: Remote HTTP integration via `https://mcp.figma.com/mcp`.
- **Skills**: `figma-design-to-code` for inspecting frames and translating to React/Tailwind.
- **Agents**: `figma-inspector` specialized agent for design-to-code translation.
- **Rules**: Consolidated `rules/AGENTS.md` applied automatically when active.

## Installation
Clone or copy into your Antigravity plugins directory:
- Project level: `.agents/plugins/figma`
- Machine global: `~/.gemini/config/plugins/figma`

```bash
python scripts/install.py figma --scope global
```
