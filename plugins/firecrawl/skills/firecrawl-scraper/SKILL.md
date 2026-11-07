---
name: firecrawl-scraper
description: Scrape single URLs, crawl entire domains, map sitemaps, and extract clean Markdown from the web using Firecrawl MCP.
---

# Firecrawl Scraper Skill

This skill coordinates web scraping, site crawling, search, and structured data extraction utilizing the Firecrawl MCP server.

## Overview

Firecrawl converts any website or URL into clean, LLM-ready Markdown while handling JavaScript rendering, CAPTCHAs, and dynamic DOM states.

## Key Capabilities

- **Single Page Scraping (`scrape`)**: Convert any webpage into clean, readable Markdown stripped of advertisements, popups, and boilerplate.
- **Deep Domain Crawling (`crawl`)**: Recursively traverse links under a website domain up to specified depth and page limits.
- **Site Mapping (`map`)**: Quickly retrieve all URLs under a domain without downloading page bodies.
- **Search (`search`)**: Query search engines and retrieve scraped top results directly.

## Usage Workflow

1. **Quick URL Ingestion**:
   When you need to read an external documentation page or blog post:
   - Call the `scrape` tool with target URL.
   - Parse returned clean Markdown into context.

2. **Full Documentation Ingestion**:
   - Call `map` to inspect the site hierarchy and extract all documentation URLs.
   - Batch scrape key target pages with `crawl` specifying max depth and allowed path patterns.
