---
name: miro-whiteboard
description: Connect to Miro boards, create sticky notes, build visual flowcharts, and manage brainstorming canvases via MCP.
---

# Miro Whiteboard Skill

This skill coordinates collaborative visual brainstorming, sticky note organization, and architecture diagramming on Miro boards using the Miro MCP server.

## Overview

Miro MCP connects Antigravity directly to the Miro REST API, allowing AI assistants to read board contents, lay out workshop boards, and map user stories visually.

## Key Capabilities

- **Sticky Note Creation (`create_sticky_note`)**: Place color-coded sticky notes on boards.
- **Shape Creation (`create_shape`)**: Add rectangles, circles, diamonds, and connectors for system flowcharts.
- **Bulk Creation (`bulk_create_items`)**: Create multiple cards, stickies, and items in a single operation.
- **Board Inspection (`get_board_items`, `get_frames`)**: Inspect existing visual assets on a board.

## Workflow

1. **Board Introspection**:
   - Query `get_frames` and `get_board_items` to understand current board layouts.

2. **Visual Mapping**:
   - Create named frames to isolate topics (e.g. "Sprint Planning", "Retrospective", "Journey Map").
   - Place sticky notes and shapes with clear coordinates and color coding.
