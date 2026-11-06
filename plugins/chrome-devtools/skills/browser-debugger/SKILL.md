---
name: browser-debugger
description: Use this skill when inspecting live browser console logs, debugging JavaScript runtime errors, examining network payload failures, or tracing DOM mutations.
---

# Browser Debugger Skill

Workflow for identifying, reproducing, and fixing front-end runtime and network defects using live browser DevTools inspection.

## 1. Console & Exception Diagnostics
- Capture unhandled exceptions, promise rejections, and CSP (Content Security Policy) violations.
- Map minified bundle stack traces back to original source code using source maps.
- Detect CORS (Cross-Origin Resource Sharing) misconfigurations and pre-flight `OPTIONS` failures.

## 2. Network Payload Inspection
- Inspect request headers, authorization cookies, and status codes (4xx/5xx).
- Verify request payload formats (JSON schemas, multipart form data).
- Measure TTFB (Time to First Byte) versus content download durations.

