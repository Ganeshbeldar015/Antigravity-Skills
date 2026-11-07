# Firecrawl Web Scraper MCP Plugin

> Production Google Antigravity Plugin

## Overview
Official Firecrawl MCP server for AI agents. Scrape web pages, crawl entire websites, execute search, map site architectures, and extract clean structured Markdown.

## Features
- **MCP Server**: Stdio integration executing `npx -y firecrawl-mcp`.
- **Skills**: `firecrawl-scraper` for single-URL scraping, site mapping, and domain crawling.
- **Agents**: `web-crawler` specialized agent for documentation extraction.
- **Rules**: Consolidated `rules/AGENTS.md` applied automatically when active.

## Installation
Clone or copy into your Antigravity plugins directory:
- Project level: `.agents/plugins/firecrawl`
- Machine global: `~/.gemini/config/plugins/firecrawl`

```bash
python scripts/install.py firecrawl --scope global
```

## Configuration
Requires a Firecrawl API key:
```bash
set FIRECRAWL_API_KEY=fc-YOUR_API_KEY
```
