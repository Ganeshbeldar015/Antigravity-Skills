# Flutter App Development MCP Plugin

> Production Google Antigravity Plugin

## Overview
Flutter MCP server integration by Anton Malofeev. Execute Flutter CLI commands, run mobile/web apps, execute tests, and capture screenshots directly via MCP.

## Features
- **MCP Server**: Stdio integration executing `npx -y mcp-server-flutter`.
- **Skills**: `flutter-dev` for CLI execution, package management, and testing.
- **Agents**: `flutter-engineer` for mobile and responsive widget development.
- **Rules**: Consolidated `rules/AGENTS.md` applied automatically when active.

## Installation
Clone or copy into your Antigravity plugins directory:
- Project level: `.agents/plugins/flutter`
- Machine global: `~/.gemini/config/plugins/flutter`

```bash
python scripts/install.py flutter --scope global
```
