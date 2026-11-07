# Firecrawl Web Scraper Behavioral Guidelines

When `firecrawl` is active:
1. Prefer `firecrawl` MCP scraping tools when retrieving dynamic JavaScript-heavy web pages or documentation sites.
2. Use site mapping (`map`) before recursive crawling to inspect URL boundaries and conserve network bandwidth.
3. Extract clean Markdown representations without unnecessary navigation chrome, cookie banners, or script tags.
4. Verify rate limits and ensure `FIRECRAWL_API_KEY` is present in the environment or user configuration.
