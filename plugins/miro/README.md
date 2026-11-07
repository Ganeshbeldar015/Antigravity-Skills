# Miro Visual Whiteboard MCP Plugin

> Production Google Antigravity Plugin

## Overview
Miro MCP server integration by evalstate. Connects AI agents to Miro whiteboard boards for visual brainstorming, sticky notes, diagramming, and collaborative workshops.

## Features
- **MCP Server**: Stdio integration executing `npx -y @llmindset/mcp-miro`.
- **Skills**: `miro-whiteboard` for sticky notes, shapes, board reading, and frames.
- **Agents**: `whiteboard-facilitator` for workshop planning and diagram generation.
- **Rules**: Consolidated `rules/AGENTS.md` applied automatically when active.

## Installation
Clone or copy into your Antigravity plugins directory:
- Project level: `.agents/plugins/miro`
- Machine global: `~/.gemini/config/plugins/miro`

```bash
python scripts/install.py miro --scope global
```

## Configuration
Requires a Miro OAuth Access Token:
```bash
set MIRO_OAUTH_TOKEN=your_token_here
```
