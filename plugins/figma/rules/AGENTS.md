# Figma Design Connect Behavioral Guidelines

When `figma` is active:
1. Always parse Figma auto-layout properties (flex direction, padding, gap, alignment) accurately into modern CSS flexbox or CSS grid primitives.
2. Extract colors, typography styles, shadows, and radii into design tokens or Tailwind config theme variables.
3. Preserve component naming and layer hierarchies to maintain 1:1 traceability between design files and frontend codebases.
4. Export SVG vector graphics cleanly without unnecessary metadata, hardcoded fills, or fixed viewport limits.
