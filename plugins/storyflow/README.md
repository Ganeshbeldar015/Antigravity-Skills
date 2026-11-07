# Storyflow MCP Plugin for Google Antigravity

[![Antigravity Plugin](https://img.shields.io/badge/Antigravity-Plugin-4285F4?style=flat-square&logo=google)](https://github.com/Ganeshbeldar015/Antigravity-Skills)
[![MCP Server](https://img.shields.io/badge/MCP-Server-3B82F6?style=flat-square)](https://mcp.storyflow.so/mcp)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=flat-square)](LICENSE)

An agile project workspace plugin integrating **Storyflow** (`https://mcp.storyflow.so/mcp`) into Google Antigravity. It equips AI agents with direct access to an infinite visual canvas for managing user stories, sprint backlogs, architecture diagrams, decision logs, and collaborative Kanban workflows.

---

## Capabilities

- **Visual Kanban & Sprints**: Manage multi-column agile boards directly through natural language prompts.
- **User Story Mapping**: Structure epics, personas, user journeys, and acceptance criteria onto visual cards.
- **Architecture & Mind Maps**: Generate interconnected nodes representing technical microservices, database schemas, and API routes.
- **Local-First & Cloud Sync**: Seamlessly synchronize local plans with Storyflow's interactive visual platform.

---

## MCP Server Configuration

Storyflow provides a live OAuth 2.0-secured Streamable HTTP endpoint:

```json
{
  "mcpServers": {
    "storyflow": {
      "type": "http",
      "url": "https://mcp.storyflow.so/mcp"
    }
  }
}
```

OAuth metadata is automatically discovered at `https://mcp.storyflow.so/.well-known/oauth-authorization-server`.

---

## Skills & Agents Included

- **`storyflow-workspace`** (`skills/storyflow-workspace/SKILL.md`): Step-by-step guidance for organizing project workflows, creating visual cards, and tracking sprint execution.
- **`storyflow-facilitator`** (`agents/storyflow-facilitator.md`): Specialized autonomous agent for agile backlog structuring and visual story mapping.
