---
name: sentry-debugger
description: Investigate production exceptions, analyze stack traces, inspect breadcrumbs, and track release regressions using official Sentry MCP.
---

# Sentry Debugger Skill

Use this skill when diagnosing real-world errors, crashes, and performance bottlenecks captured by Sentry.

## Core Capabilities

1. **Issue Triaging**:
   - Query recent unresolved errors filtered by project, environment, and frequency.
   - Analyze breadcrumbs leading up to exceptions (network requests, user clicks, console logs).

2. **Root Cause Analysis**:
   - Inspect source-mapped stack traces down to specific lines of code.
   - Correlate exception spikes with deployment events or recent commits.

3. **Targeted Remediation**:
   - Formulate unit tests reproducing the exact input conditions.
   - Write targeted patches and verify that error boundaries or fallbacks handle edge cases.

## Configuration

Requires `SENTRY_AUTH_TOKEN`:
```bash
export SENTRY_AUTH_TOKEN="sntrys_..."
```
