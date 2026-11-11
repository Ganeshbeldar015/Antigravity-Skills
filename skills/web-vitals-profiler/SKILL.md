---
name: web-vitals-profiler
description: Use this skill when diagnosing Core Web Vitals (LCP, INP, CLS), auditing performance waterfalls, detecting layout thrashing, or analyzing memory leaks.
---

# Web Vitals Profiler Skill

Actionable runbook for diagnosing and optimizing web application performance and user experience metrics.

## 1. Core Web Vitals Optimization
- **LCP (Largest Contentful Paint)**: Prioritize hero image loading using `fetchpriority="high"`, optimize CDN caching, eliminate render-blocking stylesheets.
- **INP (Interaction to Next Paint)**: Break up long JavaScript tasks (>50ms) using `requestIdleCallback` or `scheduler.yield()`; avoid heavy synchronous main-thread computations.
- **CLS (Cumulative Layout Shift)**: Always specify explicit `width` and `height` (or aspect-ratio) on images and iframes; reserve space for dynamic ads and content.

## 2. Rendering & Layout Thrashing
- Avoid reading layout geometry (`offsetHeight`, `getBoundingClientRect`) immediately before writing DOM changes.
- Batch DOM updates and use `content-visibility: auto` for off-screen components.

