<div align="center">

# 🚀 Google Antigravity Skills & Official Plugins Hub

**The definitive collection of 54 production-grade plugins, 77+ on-demand skills, 36 specialized subagents, and 14 MCP server integrations natively built for Google Antigravity.**

[![Antigravity 2.0 Compatible](https://img.shields.io/badge/Antigravity-2.0%2B%20Compatible-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://antigravity.google.com)
[![Plugins Count](https://img.shields.io/badge/Plugins-54%20Verified-34A853?style=for-the-badge)](./plugins)
[![Skills Count](https://img.shields.io/badge/Skills-77%2B%20Active-FBBC05?style=for-the-badge)](./plugins)
[![Subagents Count](https://img.shields.io/badge/Subagents-36%20Specialized-EA4335?style=for-the-badge)](./plugins)
[![MCP Servers](https://img.shields.io/badge/MCP%20Servers-14%20Integrated-9C27B0?style=for-the-badge)](./mcp_config.example.json)
[![Validation: 100% Passed](https://img.shields.io/badge/Validation-100%25%20Passed-blueviolet?style=for-the-badge)](./scripts/test_plugins.py)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](./LICENSE)

<br/>

[Quick Start & Installation](#-quick-start--installation) • [Complete Catalog](#-complete-plugins--skills-catalog) • [MCP Configuration](#-unified-mcp-servers-configuration) • [How Skills Work](#-how-antigravity-skills-work) • [Validation](#-automated-testing--validation)

</div>

---

## 🌟 Overview

**`Antigravity-Skills`** is a curated, production-ready hub containing **54 verified plugins** natively built and optimized for **Google Antigravity**.
It supercharges the Antigravity CLI and IDE with deep capabilities: feature architecture workflows, multi-agent PR reviews, static analysis language servers, headless browser testing, and automated security scans.

### 💎 Key Highlights

- **54 Native Plugins**: Covering developer workflows, code modernization, security auditing, language intelligence, design, and cloud toolchains.
- **77+ Progressive Skills**: Detailed runbooks and procedural knowledge loaded dynamically on demand to conserve token context.
- **36 Autonomous Subagents**: Specialized agents with role-scoped capabilities (`code-reviewer`, `security-auditor`, `silent-failure-hunter`, etc.).
- **14 Integrated MCP Servers**: Seamless integrations with Playwright, Context7, Firebase, GitHub, GitLab, Linear, Serena, and Terraform.
- **One-Command Global Installer**: Built-in CLI installer (`scripts/install.py`) to install and register all or individual plugins directly into your machine (`~/.gemini/config/plugins/`) or project workspace (`.agents/plugins/`).
- **100% Automated Test Coverage**: Every plugin strictly conforms to official Antigravity schemas and YAML frontmatter rules (`scripts/test_plugins.py`).

---

## 🚀 Quick Start & Installation

### Option 1: One-Command Global Installation (Recommended)

Clone the repository and install all 54 plugins globally across your entire system:
```bash
git clone https://github.com/Ganeshbeldar015/Antigravity-Skills.git
cd Antigravity-Skills

# Install all 54 plugins globally (automatically registers in ~/.gemini/config/config.json)
python scripts/install.py --all --scope global
```

### Option 2: Project-Scoped Installation

To install a plugin only for your current project (saving it to `.agents/plugins/` to share with teammates via Git):
```bash
# Inside your project folder:
python <path-to-Antigravity-Skills>/scripts/install.py feature-dev --scope project
```

### Option 3: Explore Available Plugins & MCPs

```bash
# List all 54 available plugins and versions
python scripts/install.py --list

# List all plugins that include MCP servers with transport details
python scripts/install.py --mcp
```

---

## 🔌 Unified MCP Servers Configuration

This repository includes [`mcp_config.example.json`](./mcp_config.example.json), a pre-configured configuration file linking 12 popular MCP tools directly into your Antigravity environment:

| MCP Server | Provider | Capabilities |
| :--- | :--- | :--- |
| **`playwright`** | Microsoft Playwright | Headless browser execution, interactive element clicks, form fills, screenshots. |
| **`context7`** | Upstash Context7 | Real-time live documentation lookups and library reference. |
| **`firebase`** | Google Firebase | Firestore database, Cloud Functions, and Firebase Auth management. |
| **`github`** | GitHub Copilot | Automated pull requests, issue tracking, and repository operations. |
| **`linear`** | Linear | Issue tracking, cycle planning, and roadmap updates. |
| **`serena`** | Serena Codebase | Semantic symbol graph indexing and intelligent code navigation. |
| **`terraform`** | HashiCorp Terraform | Infrastructure-as-code linting and cloud state provisioning. |
| **`shadcn`** | Shadcn UI | Instant component scaffolding with Tailwind CSS. |
| **`canva`** | Canva | Graphics, design candidate generation, and brand asset access. |
| **`21st`** | 21st.dev | Curated UI blocks, theme inspection, and modern web components. |

To activate these MCP servers globally:

```powershell
# On Windows (PowerShell):
Copy-Item mcp_config.example.json "$HOME\.gemini\config\mcp_config.json"

# On macOS / Linux:
cp mcp_config.example.json ~/.gemini/config/mcp_config.json
```

---

## 📑 Complete Plugins & Skills Catalog

<details open>
<summary><h3>1. Development & Architecture (12 Plugins)</h3></summary>

| Plugin | Version | Contained Skills | Subagents | MCP | Description |
| :--- | :---: | :--- | :--- | :---: | :--- |
| **[`feature-dev`](./plugins/feature-dev)** | `1.0.0` | • <code>feature-dev</code> | • <code>code-architect</code><br/>• <code>code-explorer</code><br/>• <code>code-reviewer</code> | — | Comprehensive feature development workflow with specialized agents for codebase exploration, ar... |
| **[`code-simplifier`](./plugins/code-simplifier)** | `1.0.0` | — | • <code>code-simplifier</code> | — | Agent that simplifies and refines code for clarity, consistency, and maintainability while pres... |
| **[`commit-commands`](./plugins/commit-commands)** | `1.0.0` | • <code>clean-gone</code><br/>• <code>commit</code><br/>• <code>commit-push-pr</code> | — | — | Streamline your git workflow with simple commands for committing, pushing, and creating pull re... |
| **[`antigravity-plugin-dev`](./plugins/antigravity-plugin-dev)** | `1.0.0` | • <code>agent-development</code><br/>• <code>command-development</code><br/>• <code>create-plugin</code><br/>• <code>hook-development</code><br/>• <code>mcp-integration</code><br/>• <code>plugin-settings</code><br/>• <code>plugin-structure</code><br/>• <code>skill-development</code> | • <code>agent-creator</code><br/>• <code>plugin-validator</code><br/>• <code>skill-reviewer</code> | — | Plugin development toolkit with skills for creating agents, commands, hooks, MCP integrations, ... |
| **[`skill-creator`](./plugins/skill-creator)** | `1.0.0` | • <code>skill-creator</code> | — | — | Create new skills, improve existing skills, and measure skill performance. Use when users want ... |
| **[`agent-sdk-dev`](./plugins/agent-sdk-dev)** | `1.0.0` | • <code>new-sdk-app</code> | • <code>agent-sdk-verifier-py</code><br/>• <code>agent-sdk-verifier-ts</code> | — | Antigravity Agent SDK Development Plugin |
| **[`antigravity-setup`](./plugins/antigravity-setup)** | `1.0.0` | • <code>claude-automation-recommender</code> | — | — | Analyze codebases and recommend tailored Google Antigravity automations such as hooks, skills, ... |
| **[`antigravity-rules-management`](./plugins/antigravity-rules-management)** | `1.0.0` | • <code>claude-md-improver</code><br/>• <code>revise-claude-md</code> | — | — | Tools to maintain and improve AGENTS.md files - audit quality, capture session learnings, and k... |
| **[`hookify`](./plugins/hookify)** | `1.0.0` | • <code>configure</code><br/>• <code>help</code><br/>• <code>hookify</code><br/>• <code>list</code><br/>• <code>writing-rules</code> | • <code>conversation-analyzer</code> | — | Easily create hooks to prevent unwanted behaviors by analyzing conversation patterns |
| **[`cwc-makers`](./plugins/cwc-makers)** | `1.0.0` | • <code>cardputer-buddy</code><br/>• <code>m5-onboard</code><br/>• <code>maker-setup</code> | — | — | Seamless onboarding for the Code-with-Antigravity Makers Cardputer: one /maker-setup command cl... |
| **[`code-modernization`](./plugins/code-modernization)** | `1.0.0` | • <code>modernize</code><br/>• <code>modernize-assess</code><br/>• <code>modernize-brief</code><br/>• <code>modernize-extract-rules</code><br/>• <code>modernize-harden</code><br/>• <code>modernize-map</code><br/>• <code>modernize-preflight</code><br/>• <code>modernize-reimagine</code><br/>• <code>modernize-review</code><br/>• <code>modernize-status</code><br/>• <code>modernize-transform</code><br/>• <code>modernize-uplift</code><br/>• <code>modernize-verify</code> | • <code>architecture-critic</code><br/>• <code>business-rules-extractor</code><br/>• <code>legacy-analyst</code><br/>• <code>scaffolder</code><br/>• <code>security-auditor</code><br/>• <code>test-engineer</code><br/>• <code>uplift-migrator</code><br/>• <code>version-delta-analyst</code> | — | Guided modernization for any legacy codebase: start with /modernize, get an assessment, an inte... |
| **[`example-plugin`](./plugins/example-plugin)** | `1.0.0` | • <code>example-command</code><br/>• <code>example-skill</code> | — | ✅ | A comprehensive example plugin demonstrating all Google Antigravity extension options including... |

</details>

<details open>
<summary><h3>2. Code Review & Security Auditing (4 Plugins)</h3></summary>

| Plugin | Version | Contained Skills | Subagents | MCP | Description |
| :--- | :---: | :--- | :--- | :---: | :--- |
| **[`code-review`](./plugins/code-review)** | `1.0.0` | • <code>code-review</code> | — | — | Automated code review for pull requests using multiple specialized agents with confidence-based... |
| **[`pr-review-toolkit`](./plugins/pr-review-toolkit)** | `1.0.0` | • <code>review-pr</code> | • <code>code-reviewer</code><br/>• <code>code-simplifier</code><br/>• <code>comment-analyzer</code><br/>• <code>pr-test-analyzer</code><br/>• <code>silent-failure-hunter</code><br/>• <code>type-design-analyzer</code> | — | Comprehensive PR review agents specializing in comments, tests, error handling, type design, co... |
| **[`antigravity-security`](./plugins/antigravity-security)** | `0.12.0` | • <code>claude-security</code> | • <code>claude-security</code><br/>• <code>explore</code><br/>• <code>patch-generator</code><br/>• <code>patch-verifier</code><br/>• <code>scan-inventory</code><br/>• <code>scan-loader</code><br/>• <code>scan-redactor</code><br/>• <code>scan-researcher</code><br/>• <code>scan-verifier</code> | — | Deep vulnerability scanning of your own code, run entirely inside your Google Antigravity sessi... |
| **[`security-guidance`](./plugins/security-guidance)** | `2.0.14` | — | — | — | Security review for Antigravity-generated code. Pattern-based warnings on edits, LLM-powered di... |

</details>

<details open>
<summary><h3>3. Language Server Protocol (LSP) Intelligence (12 Plugins)</h3></summary>

| Plugin | Version | Contained Skills | Subagents | MCP | Description |
| :--- | :---: | :--- | :--- | :---: | :--- |
| **[`clangd-lsp`](./plugins/clangd-lsp)** | `1.0.0` | • <code>clangd-lsp</code> | — | — | C/C++ language server (clangd) integration for Google Antigravity, providing AST diagnostics, c... |
| **[`csharp-lsp`](./plugins/csharp-lsp)** | `1.0.0` | • <code>csharp-lsp</code> | — | — | C# language server integration for Google Antigravity, providing semantic analysis, completions... |
| **[`gopls-lsp`](./plugins/gopls-lsp)** | `1.0.0` | • <code>gopls-lsp</code> | — | — | Go language server (gopls) integration for Google Antigravity, providing analysis, package navi... |
| **[`jdtls-lsp`](./plugins/jdtls-lsp)** | `1.0.0` | • <code>jdtls-lsp</code> | — | — | Eclipse JDT.LS language server for Java projects in Google Antigravity. |
| **[`kotlin-lsp`](./plugins/kotlin-lsp)** | `1.0.0` | • <code>kotlin-lsp</code> | — | — | Kotlin language server for Kotlin and Android projects in Google Antigravity. |
| **[`lua-lsp`](./plugins/lua-lsp)** | `1.0.0` | • <code>lua-lsp</code> | — | — | Lua language server for Lua scripting, Game dev, and Neovim development in Google Antigravity. |
| **[`php-lsp`](./plugins/php-lsp)** | `1.0.0` | • <code>php-lsp</code> | — | — | PHP language server integration for PHP and Laravel projects in Google Antigravity. |
| **[`pyright-lsp`](./plugins/pyright-lsp)** | `1.0.0` | • <code>pyright-lsp</code> | — | — | Pyright static type checker and language server for Python projects in Google Antigravity. |
| **[`ruby-lsp`](./plugins/ruby-lsp)** | `1.0.0` | • <code>ruby-lsp</code> | — | — | Ruby LSP language server for Ruby and Rails projects in Google Antigravity. |
| **[`rust-analyzer-lsp`](./plugins/rust-analyzer-lsp)** | `1.0.0` | • <code>rust-analyzer-lsp</code> | — | — | rust-analyzer language server for Rust projects in Google Antigravity. |
| **[`swift-lsp`](./plugins/swift-lsp)** | `1.0.0` | • <code>swift-lsp</code> | — | — | SourceKit-LSP language server for Swift and Apple platform development in Google Antigravity. |
| **[`typescript-lsp`](./plugins/typescript-lsp)** | `1.0.0` | • <code>typescript-lsp</code> | — | — | TypeScript and JavaScript language server for Node.js, React, and web projects in Google Antigr... |

</details>

<details open>
<summary><h3>4. MCP Servers & Cloud Integrations (16 Plugins)</h3></summary>

| Plugin | Version | Contained Skills | Subagents | MCP | Description |
| :--- | :---: | :--- | :--- | :---: | :--- |
| **[`github`](./plugins/github)** | `1.0.0` | — | — | ✅ | Official GitHub MCP server for repository management. Create issues, manage pull requests, revi... |
| **[`gitlab`](./plugins/gitlab)** | `1.0.0` | — | — | ✅ | GitLab DevOps platform integration. Manage repositories, merge requests, CI/CD pipelines, issue... |
| **[`playwright`](./plugins/playwright)** | `1.0.0` | — | — | ✅ | Browser automation and end-to-end testing MCP server by Microsoft. Enables Antigravity to inter... |
| **[`firebase`](./plugins/firebase)** | `1.0.0` | — | — | ✅ | Google Firebase MCP integration. Manage Firestore databases, authentication, cloud functions, h... |
| **[`terraform`](./plugins/terraform)** | `1.0.0` | — | — | ✅ | The Terraform MCP Server provides seamless integration with Terraform ecosystem, enabling advan... |
| **[`linear`](./plugins/linear)** | `1.0.0` | — | — | ✅ | Linear issue tracking integration. Create issues, manage projects, update statuses, search acro... |
| **[`asana`](./plugins/asana)** | `1.0.0` | • <code>asana-setup</code> | — | — | Asana project management integration. Connects Google Antigravity to Asana's V2 MCP server (htt... |
| **[`context7`](./plugins/context7)** | `1.0.0` | — | — | ✅ | Upstash Context7 MCP server for up-to-date documentation lookup. Connects to Context7's hosted ... |
| **[`serena`](./plugins/serena)** | `1.0.0` | — | — | ✅ | Semantic code analysis MCP server providing intelligent code understanding, refactoring suggest... |
| **[`laravel-boost`](./plugins/laravel-boost)** | `1.0.0` | — | — | ✅ | Laravel development toolkit MCP server. Provides intelligent assistance for Laravel application... |
| **[`mcp-server-dev`](./plugins/mcp-server-dev)** | `1.0.0` | • <code>build-mcp-app</code><br/>• <code>build-mcp-server</code><br/>• <code>build-mcpb</code> | — | — | Skills for designing and building MCP servers that work seamlessly with Antigravity — guides yo... |
| **[`mcp-tunnels`](./plugins/mcp-tunnels)** | `1.0.0` | • <code>create-docker-mcp-tunnel</code> | — | — | Connect Antigravity to a private MCP server through an Google Antigravity Ecosystem MCP tunnel.... |
| **[`discord`](./plugins/discord)** | `0.0.4` | • <code>access</code><br/>• <code>configure</code> | — | ✅ | Discord channel for Google Antigravity — messaging bridge with built-in access control. Manage ... |
| **[`telegram`](./plugins/telegram)** | `0.0.7` | • <code>access</code><br/>• <code>configure</code> | — | ✅ | Telegram channel for Google Antigravity — messaging bridge with built-in access control. Manage... |
| **[`imessage`](./plugins/imessage)** | `0.2.0` | • <code>access</code><br/>• <code>configure</code> | — | ✅ | iMessage channel for Google Antigravity — reads chat.db directly, sends via AppleScript. Built-... |
| **[`fakechat`](./plugins/fakechat)** | `0.0.1` | — | — | ✅ | Localhost iMessage-style web chat for Google Antigravity — test surface with file upload and ed... |

</details>

<details open>
<summary><h3>5. Design, Math & Output Reasoning (10 Plugins)</h3></summary>

| Plugin | Version | Contained Skills | Subagents | MCP | Description |
| :--- | :---: | :--- | :--- | :---: | :--- |
| **[`frontend-design`](./plugins/frontend-design)** | `1.0.0` | • <code>frontend-design</code> | — | — | Frontend design skill for UI/UX implementation |
| **[`project-artifact`](./plugins/project-artifact)** | `1.0.0` | • <code>project-artifact</code> | — | — | Generate and publish a project status artifact — an opinionated, tabbed status page (overview &... |
| **[`playground`](./plugins/playground)** | `1.0.0` | • <code>playground</code> | — | — | Creates interactive HTML playgrounds — self-contained single-file explorers with visual control... |
| **[`math-olympiad`](./plugins/math-olympiad)** | `1.0.0` | • <code>math-olympiad</code> | — | — | Solve competition math (IMO, Putnam, USAMO) with adversarial verification that catches what sel... |
| **[`math-proof`](./plugins/math-proof)** | `1.0.0` | • <code>siege</code><br/>• <code>solo</code> | • <code>math-proof-judge</code><br/>• <code>math-proof-worker-deep</code><br/>• <code>math-proof-worker</code> | — | Two skills for hard mathematics problems, each ending in a self-contained proof.md: /math-proof... |
| **[`session-report`](./plugins/session-report)** | `1.0.0` | • <code>session-report</code> | — | — | Session Report integration and capabilities for Google Antigravity. |
| **[`receipts`](./plugins/receipts)** | `1.0.0` | • <code>receipts</code> | — | — | Receipts integration and capabilities for Google Antigravity. |
| **[`ralph-loop`](./plugins/ralph-loop)** | `1.0.0` | • <code>cancel-ralph</code><br/>• <code>help</code><br/>• <code>ralph-loop</code> | — | — | Continuous self-referential AI loops for interactive iterative development, implementing the Ra... |
| **[`explanatory-output-style`](./plugins/explanatory-output-style)** | `1.0.0` | — | — | — | Adds educational insights about implementation choices and codebase patterns (mimics the deprec... |
| **[`learning-output-style`](./plugins/learning-output-style)** | `1.0.0` | — | — | — | Interactive learning mode that requests meaningful code contributions at decision points (mimic... |

</details>

---

## 🧠 How Antigravity Skills Work

Antigravity uses **Progressive Disclosure** to manage skill execution efficiently without overflowing the LLM context window:

1. **Discovery**: On startup, Antigravity indexes the `name` and `description` frontmatter from every `SKILL.md`.
2. **Intent Matching**: When you enter a prompt, the agent evaluates which skill matches your goal.
3. **On-Demand Loading**: Only the triggered skill instructions, reference files, and scripts are loaded into memory.
4. **Autonomous Execution**: The skill runs specialized subagents or tools, verifying each step before completing.

### Skill File Architecture

```text
plugins/<plugin_name>/
├── plugin.json         # Plugin manifest (name, version, description)
├── README.md           # Documentation and usage examples
├── mcp_config.json     # Optional MCP server definitions
├── hooks.json          # Optional lifecycle event hooks (PreToolUse, PostToolUse)
├── rules/
│   └── AGENTS.md       # Behavioral rules active when the plugin is enabled
├── skills/
│   └── <skill_name>/
│       └── SKILL.md    # Progressive disclosure runbook with YAML frontmatter
└── agents/
    └── <agent_name>.md # Autonomous subagent definitions (model: inherit | flash | pro)
```

---

## 🧪 Automated Testing & Validation

This repository includes an automated validation suite that verifies all plugins against Antigravity schema requirements:
```bash
python scripts/test_plugins.py
```

### Verified Criteria:
- [x] Every plugin has a valid `plugin.json` conforming to Antigravity Customization System standards.
- [x] All 77 skills have compliant `SKILL.md` files with valid YAML frontmatter.
- [x] All 36 subagents define valid `agents/<agent>.md` configurations.
- [x] All 14 `mcp_config.json` files parse cleanly and declare supported transports (Stdio / HTTP).
- [x] Master `marketplace.json` catalogs all 54 plugins with 100% test pass.

---

## 🤝 Contributing

1. Fork this repository: `https://github.com/Ganeshbeldar015/Antigravity-Skills`.
2. Create your plugin directory in `plugins/<your-plugin-name>/`.
3. Add `plugin.json`, `README.md`, `rules/AGENTS.md`, and your `skills/<skill_name>/SKILL.md`.
4. Run `python scripts/test_plugins.py` to ensure validation passes.
5. Submit a Pull Request!

---

## 📄 License

Distributed under the [MIT License](./LICENSE). Copyright (c) 2026 Ganesh Bhaktaraj Beldar (Ganeshbeldar015).
