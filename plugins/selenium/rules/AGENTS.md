# Selenium WebDriver Behavioral Guidelines

When `selenium` is active:
1. Always wait for elements to be interactable before triggering clicks or keyboard inputs to avoid flaky test executions.
2. Capture full-page screenshots upon unexpected test failures to facilitate visual debugging.
3. Test key user journeys across multiple viewport resolutions (mobile 375px, tablet 768px, desktop 1280px).
4. Verify accessibility attributes (ARIA roles, accessible names) on elements during automated sweeps.
