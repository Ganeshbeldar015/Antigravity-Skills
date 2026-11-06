# Docker & DevOps Rules

When authoring container files and infrastructure configurations:
1. Never run containers as root in production; always specify an unprivileged `USER`.
2. Pin all base image tags to specific semantic versions or SHA digests (avoid `:latest`).
3. Never embed passwords, tokens, or private keys inside Dockerfile `ENV` or `ARG` instructions.
4. Include explicit `.dockerignore` files excluding `.git`, `node_modules`, `.env`, and test artifacts.
5. Define container `HEALTHCHECK` for all persistent services.
