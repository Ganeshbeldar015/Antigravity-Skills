# Storybook Design System MCP Plugin

> Production Google Antigravity Plugin

## Overview
Storybook MCP server integration by Danny Williams. Connects AI agents to component libraries, stories, and docs to prevent UI hallucination and enforce real component reuse.

## Features
- **MCP Server**: Stdio integration executing `npx -y storybook-mcp`.
- **Skills**: `storybook-guide` for story discovery, prop verification, and CSF 3 authoring.
- **Agents**: `storybook-specialist` for component audit and design system governance.
- **Rules**: Consolidated `rules/AGENTS.md` applied automatically when active.

## Installation
Clone or copy into your Antigravity plugins directory:
- Project level: `.agents/plugins/storybook`
- Machine global: `~/.gemini/config/plugins/storybook`

```bash
python scripts/install.py storybook --scope global
```
