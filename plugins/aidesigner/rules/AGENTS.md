# AIDesigner Frontend Behavioral Guidelines

When `aidesigner` is active:
1. Always inspect the destination repository (`DESIGN.md`, tokens, typography scales, existing component libraries) before generating UI artifacts.
2. Formulate compact, art-directed visual prompts rather than exhaustive PRD dumps when invoking `generate_design` or `refine_design`.
3. Distinguish between prompt-only generation, `clone` (faithful recreation), `enhance` (modernization while preserving intent), and `inspire` (styling inspiration).
4. For clone workflows, verify that browser automation (Puppeteer or Playwright) is available for screenshot-driven visual QA before consuming generation credits.
5. Never paste raw standalone HTML directly into production code; decompose artifacts into repo-native components, design tokens, accessible primitives, and responsive layouts.
6. Adhere to production UX standards: mobile responsiveness, WCAG AA contrast, clear visual hierarchy, and keyboard navigability.
