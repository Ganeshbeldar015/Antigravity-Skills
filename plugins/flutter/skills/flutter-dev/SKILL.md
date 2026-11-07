---
name: flutter-dev
description: Execute Flutter commands, run apps, execute integration tests, and capture screenshots using Flutter MCP.
---

# Flutter Development Skill

This skill coordinates mobile and multi-platform Flutter app development, widget testing, and CLI command execution using the Flutter MCP server.

## Overview

Created by Anton Malofeev, this MCP server connects AI agents directly to Flutter repositories to execute commands (`create`, `pub`, `run`, `test`, `screenshot`).

## Available MCP Tools

- `flutter_execute`: Executes Flutter CLI operations inside the project repository:
  - `pub get`: Resolves package dependencies.
  - `run`: Launches application on simulators or emulators.
  - `test`: Executes unit and integration test suites.
  - `screenshot`: Captures UI frame screenshots for inspection.

## Workflow

1. **Dependency Resolution**:
   - Run `flutter_execute` with `command: "pub get"` after modifying `pubspec.yaml`.

2. **Testing & QA**:
   - Run `flutter_execute` with `command: "test"` to execute widget tests and verify UI behavior.
