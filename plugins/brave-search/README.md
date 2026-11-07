# Brave Search Plugin for Google Antigravity

[![Antigravity Plugin](https://img.shields.io/badge/Antigravity-Plugin-4285F4?style=flat-square&logo=google)](https://github.com/Ganeshbeldar015/Antigravity-Skills)
[![MCP Server](https://img.shields.io/badge/MCP-Server-FF5500?style=flat-square)](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=flat-square)](LICENSE)

A web intelligence plugin integrating the official **Brave Search MCP Server** (`@modelcontextprotocol/server-brave-search`) into Google Antigravity. It equips AI assistants with real-time web search capabilities powered by Brave's independent, privacy-focused search index.

---

## MCP Server Configuration

Configure the Brave Search MCP server with your API key:

```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-brave-search@latest"
      ],
      "env": {
        "BRAVE_API_KEY": "${BRAVE_API_KEY}"
      }
    }
  }
}
```

---

## Skills & Agents Included

- **`brave-search`** (`skills/brave-search/SKILL.md`): Web and local search tooling.
- **`web-researcher`** (`agents/web-researcher.md`): Fast, automated Flash-model researcher for documentation and security updates.
