---
name: selenium-automation
description: Cross-browser testing and web automation using Selenium WebDriver via MCP (start browser, navigate, find element, click, type, screenshot).
---

# Selenium WebDriver Automation Skill

This skill coordinates browser automation, cross-browser validation, and end-to-end user journey verification using the Selenium MCP server.

## Overview

Created by Angie Jones, this MCP server connects AI assistants directly to Selenium WebDriver, allowing deterministic browser control, form interactions, and visual layout inspection.

## Available MCP Tools

- `start_browser`: Launches a local Chrome or Firefox browser session.
- `navigate`: Opens target URLs and waits for document readiness.
- `find_element`: Locates DOM nodes via CSS selectors or XPath.
- `click_element`: Interacts with buttons, links, and switches.
- `send_keys`: Types text into form fields.
- `get_element_text`: Retrieves inner text and values for assertions.
- `take_screenshot`: Captures PNG screenshots for regression inspection.

## Workflow

1. **Session Initialization**:
   - Call `start_browser` to spawn a clean browser session.
   - Call `navigate` to load the application under test.

2. **UI Interaction & Verification**:
   - Locate elements with `find_element`.
   - Interact via `click_element` or `send_keys`.
   - Assert page state with `get_element_text` and `take_screenshot`.
