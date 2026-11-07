# Sequential Thinking Plugin for Google Antigravity

[![Antigravity Plugin](https://img.shields.io/badge/Antigravity-Plugin-4285F4?style=flat-square&logo=google)](https://github.com/Ganeshbeldar015/Antigravity-Skills)
[![MCP Server](https://img.shields.io/badge/MCP-Server-10B981?style=flat-square)](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=flat-square)](LICENSE)

An advanced reasoning plugin integrating the official **Sequential Thinking MCP Server** (`@modelcontextprotocol/server-sequential-thinking`) into Google Antigravity. It enables AI agents to decompose intricate engineering problems into numbered steps, backtrack when hypotheses fail, and branch across alternative solution designs.

---

## MCP Server Configuration

Zero API keys or external authentication needed:

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sequential-thinking@latest"
      ],
      "env": {}
    }
  }
}
```

---

## Skills & Agents Included

- **`sequential-thinking`** (`skills/sequential-thinking/SKILL.md`): Multi-step reasoning guidelines and tool usage.
- **`deep-reasoner`** (`agents/deep-reasoner.md`): Autonomous Pro-model reasoning agent for algorithmic breakdowns and architecture stress-testing.
