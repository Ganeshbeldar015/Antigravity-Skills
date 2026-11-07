---
name: brave-search
description: Perform live, privacy-respecting web and local news searches using the independent Brave Search API.
---

# Brave Search Skill

Use this skill when your AI assistant needs to look up recent web events, library updates, security advisories, or technical benchmarks beyond training knowledge cutoffs.

## Available Tools

1. **`brave_web_search`**:
   - Query the independent Brave Search Index.
   - Parameters:
     - `query`: Search query string.
     - `count`: Number of results (1 to 20).
     - `offset`: Pagination offset.

2. **`brave_local_search`**:
   - Search for localized businesses, venues, or regional information.

## Setup

Requires `BRAVE_API_KEY` (free tier available at [brave.com/search/api](https://brave.com/search/api/)):
```bash
export BRAVE_API_KEY="BSA..."
```
