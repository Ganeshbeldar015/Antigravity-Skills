---
name: sequential-thinking
description: Dynamic multi-step reasoning, hypothesis evaluation, branching logic, and reflective problem-solving using Sequential Thinking MCP.
---

# Sequential Thinking Skill

Use this skill when tackling complex architectural decisions, ambiguous bug investigations, deep mathematical proofs, or refactoring problems that benefit from structured, iterative chains of thought.

## Core Operations

1. **Step-by-Step Problem Breakdown**:
   - Break problems down into explicit reasoning units.
   - Maintain a running count of total estimated thoughts, adjusting dynamically.

2. **Branching & Alternative Evaluation**:
   - Fork the reasoning tree (`branchFromThought`, `branchId`) to explore competing hypotheses or design approaches.
   - Compare trade-offs systematically before selecting a path.

3. **Hypothesis Revision & Backtracking**:
   - Revisit earlier assumptions when encountering conflicting evidence (`revisesThought`).
   - Eliminate disproven dead ends cleanly without polluting final code.

## Tool Interface

The server provides the `sequentialthinking` tool with parameters:
- `thought`: The text reasoning step.
- `nextThoughtNeeded`: Boolean indicating if further reasoning is required.
- `thoughtNumber`: Current step index (1-based).
- `totalThoughts`: Estimated total thoughts required.
- `isRevision`: Whether this step revises a prior thought.
- `revisesThought`: Index of the thought being revised.
- `branchFromThought`: Thought index from which to branch.
- `branchId`: Branch identifier.
- `needsMoreThoughts`: Boolean flag if more depth is needed.
