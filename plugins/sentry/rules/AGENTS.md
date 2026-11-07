# Sentry Behavioral Guidelines

When `sentry` is active:
1. When investigating errors, inspect the complete stack trace and historical breadcrumbs before proposing fixes.
2. Cross-reference issue spikes with recent releases, environment tags (production, staging), and browser/OS distributions.
3. Validate fixes locally with automated tests that specifically replicate the crash conditions reported in Sentry.
4. Redact sensitive user data (PII, tokens, authorization headers) if echoing error payloads to conversational outputs.
5. Provide the Sentry issue ID and direct link in resolution summaries.
