# Sentry Plugin for Google Antigravity

[![Antigravity Plugin](https://img.shields.io/badge/Antigravity-Plugin-4285F4?style=flat-square&logo=google)](https://github.com/Ganeshbeldar015/Antigravity-Skills)
[![MCP Server](https://img.shields.io/badge/MCP-Server-362D59?style=flat-square)](https://github.com/getsentry/sentry-mcp)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=flat-square)](LICENSE)

An error monitoring and debugging plugin integrating the official **Sentry MCP Server** (`@sentry/mcp-server`) into Google Antigravity. It empowers AI agents to inspect unresolved exceptions, breadcrumb histories, release regressions, and telemetry issues directly inside chat or pair-programming sessions.

---

## MCP Server Configuration

Configure the official Sentry MCP server with your auth token:

```json
{
  "mcpServers": {
    "sentry": {
      "command": "npx",
      "args": [
        "-y",
        "@sentry/mcp-server@latest"
      ],
      "env": {
        "SENTRY_AUTH_TOKEN": "${SENTRY_AUTH_TOKEN}"
      }
    }
  }
}
```

---

## Skills & Agents Included

- **`sentry-debugger`** (`skills/sentry-debugger/SKILL.md`): Issue querying, breadcrumb inspection, and root-cause debugging.
- **`sentry-investigator`** (`agents/sentry-investigator.md`): Autonomous subagent analyzing production crash reports and producing hardened patches.
