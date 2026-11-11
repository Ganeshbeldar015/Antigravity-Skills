---
name: compose-architect
description: Use this skill when configuring Docker Compose stacks, setting up multi-service local environments, managing service dependencies, and container networking.
---

# Compose Architect Skill

Guidance for orchestrating multi-container local and staging stacks with Docker Compose.

## 1. Service Definition Best Practices
- **Healthchecks**: Define explicit `healthcheck` tests for stateful services (databases, caches, message brokers).
- **Service Dependencies**: Use `depends_on` with `condition: service_healthy` instead of naive startup ordering.
- **Isolated Networks**: Isolate backend data tiers on private internal networks; expose only frontend ingress proxies.

## 2. Volume & Environment Configuration
- Persist stateful data using named volumes (`db_data:/var/lib/postgresql/data`).
- Use `.env.example` templates for documenting all required environment variables.
- Configure restart policies (`restart: unless-stopped` for persistent services).

