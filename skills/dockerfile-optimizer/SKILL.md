---
name: dockerfile-optimizer
description: Use this skill when authoring or optimizing Dockerfiles, configuring multi-stage builds, reducing image sizes, or hardening container security.
---

# Dockerfile Optimizer Skill

Best practices for building secure, slim, and high-performance container images.

## 1. Multi-Stage Build Architecture
- Separate the compilation/build environment from the lightweight runtime environment.
- Use minimal base images for runtime: `alpine`, `distroless`, or slim variants.
- Copy only compiled binaries or production dependencies from the build stage into the final stage.

## 2. Layer Caching & Build Performance
- Order instructions from least frequently changed to most frequently changed:
  1. Base image (`FROM ...`)
  2. System package installations
  3. Dependency manifests (`package.json`, `requirements.txt`, `go.mod`)
  4. Dependency download/install commands
  5. Application source code (`COPY . .`)
- Clean package manager caches within the same `RUN` step (`rm -rf /var/lib/apt/lists/*` or `--no-cache`).

## 3. Security Hardening
- Never run containers as the `root` user; declare a non-privileged `USER` (`node`, `appuser`, `10001`).
- Mount secrets via secret mounts (`RUN --mount=type=secret...`), never as build arguments (`ARG`).

