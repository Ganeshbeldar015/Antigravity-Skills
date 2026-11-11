---
name: ux-ui
description: UX/UI design principles for clean, intuitive interfaces. Use when designing layouts, improving usability, planning information architecture, or ensuring accessibility. Triggers on "user experience", "usability", "information architecture", "accessibility", "interaction design".
---

# UX/UI Design Expert

Create clean, intuitive interfaces that prioritize usability, efficiency, and seamless user interaction.

## Information Architecture

- Design with clear visual hierarchy
- Present critical information and primary actions prominently
- Progressively reveal secondary details
- Every screen should have one clear purpose
- Guide users toward their goal with minimal cognitive load

## Interaction Design

Build dynamic, responsive interactions:
- **Stimulus controllers** for client-side behaviors
- **Turbo Frames** for asynchronous partial page updates
- **Turbo Streams** for real-time WebSocket changes
- **AJAX** for seamless background data exchanges
- Favor progressive enhancement over full page refreshes

## Design Standards

- Follow established UI conventions users already understand
- Use consistent spacing, typography scales, and color systems
- Implement accessible, WCAG-compliant interfaces:
  - Proper semantic HTML
  - ARIA labels and roles where needed
  - Complete keyboard navigation support

## Responsive First

Design mobile-first:
- Test across common breakpoints: 375px (mobile), 768px (tablet), 1024px (laptop), 1440px (desktop)
- Use flexible grids and fluid typography
- Ensure touch-friendly interaction targets (minimum 44x44px)

## Performance & Efficiency

- Minimize steps required to complete tasks
- Provide intelligent defaults and contextual help
- Offer inline validation with graceful error recovery
- Reduce decision fatigue by surfacing only relevant options
