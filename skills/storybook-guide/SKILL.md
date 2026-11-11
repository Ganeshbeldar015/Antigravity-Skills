---
name: storybook-guide
description: Discover existing components, inspect story definitions, and compose UI using verified Storybook design system primitives via MCP.
---

# Storybook Guide Skill

This skill anchors AI code generation to real, existing design system components by querying the project's Storybook catalog.

## Overview

Storybook MCP bridges the component library and the AI assistant, solving the UI hallucination problem by giving agents direct visibility into available stories, props, and variants.

## Capabilities

- **Story Discovery (`get-stories`)**: Retrieves all available component stories across the workspace.
- **Variant Inspection**: Examines how components are intended to be configured and styled.
- **Design System Enforcement**: Replaces ad-hoc custom HTML/CSS with canonical design system imports.

## Workflow

1. **Discovery Before Authoring**:
   - Query `get-stories` to see which buttons, modals, cards, and navigation items already exist.

2. **Prop Alignment**:
   - Inspect the component story parameters to match required props (e.g. `size`, `variant`, `icon`, `onClick`).

3. **Writing New Stories**:
   - Generate standard CSF 3.0 Storybook stories (`Meta`, `StoryObj`) for newly created components.
