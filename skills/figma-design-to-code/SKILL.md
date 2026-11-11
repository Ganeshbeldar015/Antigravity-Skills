---
name: figma-design-to-code
description: Inspect Figma design files, extract layout tokens, and translate component frames into production-ready React and Tailwind CSS code.
---

# Figma Design to Code Skill

This skill translates Figma design files and component frames into production-ready, responsive React and Tailwind CSS code using the Figma MCP server.

## Overview

The Figma MCP server connects Antigravity directly to Figma's API (`https://mcp.figma.com/mcp`), enabling real-time reading of frames, auto-layout hierarchies, color styles, and vector assets.

## Capabilities

- **Frame Inspection**: Read tree hierarchies, layer names, dimensions, padding, and constraints.
- **Design Tokens**: Extract color styles, typography definitions, corner radii, and shadow elevations.
- **Code Generation**: Translate auto-layout frames into semantic JSX/TSX components with responsive Tailwind CSS utilities.
- **Asset Export**: Fetch SVG vectors and raster image exports directly for components.

## Workflow

1. **Inspect Target Node**:
   - Provide the Figma file key and node ID (e.g. `?node-id=123:456`).
   - Query node properties, auto-layout settings, and typography styles.

2. **Map to Design System Tokens**:
   - Align Figma colors and typography with existing Tailwind config variables (`theme.extend.colors`, font families).
   - Convert auto-layout padding and gap values to Tailwind spacing increments (`p-4`, `gap-6`).

3. **Output Component Code**:
   - Generate accessible, semantic React components with appropriate props and variants.
