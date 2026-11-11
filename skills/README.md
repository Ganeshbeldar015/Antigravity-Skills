<div align="center">
# 🎯 Google Antigravity Skills Directory
<p><em>Comprehensive on-demand runbook library comprising <b>494 specialized skills</b> for Antigravity & the Gemini Agent CLI.</em></p>
<p>  <img src="https://img.shields.io/badge/Total%20Skills-494%20Modular-blue?style=for-the-badge&logo=codewars&logoColor=white" alt="Total Skills" />  <img src="https://img.shields.io/badge/Architecture-Progressive%20Disclosure-success?style=for-the-badge&logo=google&logoColor=white" alt="Architecture" />  <img src="https://img.shields.io/badge/Zero%20Overhead-On--Demand%20Loading-orange?style=for-the-badge" alt="Zero Overhead" /></p>
</div>

---

## 📖 Overview

Skills in Antigravity are modular procedural runbooks loaded via **Progressive Disclosure**.

- **Zero Token Overhead at Rest**: Only skill names and triggers are indexed in memory. The full body of a `SKILL.md` is strictly loaded when your task or prompt matches its intent.
- **Standardized Architecture**: Every skill folder contains a declarative `SKILL.md` with YAML frontmatter triggers and optional domain-specific references or validation checklists.

### 📑 Category Navigation

| Category | Skills Count | Focus Domain |
| :--- | :---: | :--- |
| [**🤖 AI, Machine Learning & Autonomous Agents**](#-ai-machine-learning--autonomous-agents) | **81** | AI, Machine Learning & Autonomous Agents |
| [**🎨 Frontend, UI/UX, Design Systems & 3D**](#-frontend-uiux-design-systems--3d) | **193** | Frontend, UI/UX, Design Systems & 3D |
| [**⚙️ Backend, APIs & Distributed Systems**](#-backend-apis--distributed-systems) | **15** | Backend, APIs & Distributed Systems |
| [**🗄️ Database Engineering, ORM & Caching**](#-database-engineering-orm--caching) | **50** | Database Engineering, ORM & Caching |
| [**🛡️ Security, SAST, Auth & Vulnerability Auditing**](#-security-sast-auth--vulnerability-auditing) | **17** | Security, SAST, Auth & Vulnerability Auditing |
| [**🧪 Testing, QA Automation & Performance Engineering**](#-testing-qa-automation--performance-engineering) | **9** | Testing, QA Automation & Performance Engineering |
| [**☁️ DevOps, Cloud Infrastructure, Docker & CI/CD**](#-devops-cloud-infrastructure-docker--cicd) | **13** | DevOps, Cloud Infrastructure, Docker & CI/CD |
| [**📱 Mobile, Cross-Platform & Desktop Development**](#-mobile-cross-platform--desktop-development) | **2** | Mobile, Cross-Platform & Desktop Development |
| [**📊 Data Science, Analytics, Big Data & Modeling**](#-data-science-analytics-big-data--modeling) | **12** | Data Science, Analytics, Big Data & Modeling |
| [**✍️ Product, Growth, Media, Copywriting & Docs**](#-product-growth-media-copywriting--docs) | **39** | Product, Growth, Media, Copywriting & Docs |
| [**🛠️ Developer Productivity, Architecture & Workflow Automation**](#-developer-productivity-architecture--workflow-automation) | **63** | Developer Productivity, Architecture & Workflow Automation |

---

## 🤖 AI, Machine Learning & Autonomous Agents

> *81 specialized runbooks available in this domain.*

| Skill Identifier | Runbook Path | Core Capabilities & Description |
| :--- | :--- | :--- |
| **`agent-based-modeling`** | [`agent-based-modeling/`](./agent-based-modeling) | Design and implement agent-based models (ABM) for simulating complex systems with emergent behavior from individual agent interactions. Use when "agent-based... |
| **`agent-communication`** | [`agent-communication/`](./agent-communication) | Inter-agent communication patterns including message passing, shared memory, blackboard systems, and event-driven architectures for LLM agentsUse when "agent... |
| **`agent-evaluation`** | [`agent-evaluation/`](./agent-evaluation) | Testing and benchmarking LLM agents including behavioral testing, capability assessment, reliability metrics, and production monitoring—where even top agents... |
| **`agent-memory-systems`** | [`agent-memory-systems/`](./agent-memory-systems) | Memory is the cornerstone of intelligent agents. Without it, every interaction starts from zero. This skill covers the architecture of agent memory: short-te... |
| **`agent-tool-builder`** | [`agent-tool-builder/`](./agent-tool-builder) | Tools are how AI agents interact with the world. A well-designed tool is the difference between an agent that works and one that hallucinates, fails silently... |
| **`ai-agents-architect`** | [`ai-agents-architect/`](./ai-agents-architect) | Expert in designing and building autonomous AI agents. Masters tool use, memory systems, planning strategies, and multi-agent orchestration. Use when "build ... |
| **`ai-code-security`** | [`ai-code-security/`](./ai-code-security) | Security vulnerabilities in AI-generated code and LLM applications, covering OWASP Top 10 for LLMs, secure coding patterns, and AI-specific threat modelsUse ... |
| **`ai-game-art-generation`** | [`ai-game-art-generation/`](./ai-game-art-generation) | Master AI-powered game asset pipelines using ComfyUI, Stable Diffusion, FLUX, ControlNet, and IP-Adapter. Creates production-ready sprites, textures, UI, and... |
| **`ai-image-generation`** | [`ai-image-generation/`](./ai-image-generation) | Mastery of AI image generation across the full spectrum: Midjourney for aesthetic perfection, Flux for prompt adherence, DALL-E 3 for concept clarity, Stable... |
| **`ai-observability`** | [`ai-observability/`](./ai-observability) | Implement comprehensive observability for LLM applications including tracing (Langfuse/Helicone), cost tracking, token optimization, RAG evaluation metrics (... |
| **`ai-product`** | [`ai-product/`](./ai-product) | Every product will be AI-powered. The question is whether you'll build it right or ship a demo that falls apart in production.  This skill covers LLM integra... |
| **`ai-safety-alignment`** | [`ai-safety-alignment/`](./ai-safety-alignment) | Implement comprehensive safety guardrails for LLM applications including content moderation (OpenAI Moderation API), jailbreak prevention, prompt injection d... |
| **`ai-wrapper-product`** | [`ai-wrapper-product/`](./ai-wrapper-product) | Expert in building products that wrap AI APIs (OpenAI, Anthropic, etc.) into focused tools people will pay for. Not just "ChatGPT but different" - products t... |
| **`autonomous-agents`** | [`autonomous-agents/`](./autonomous-agents) | Autonomous agents are AI systems that can independently decompose goals, plan actions, execute tools, and self-correct without constant human guidance. The c... |
| **`browser-automation`** | [`browser-automation/`](./browser-automation) | Browser automation powers web testing, scraping, and AI agent interactions. The difference between a flaky script and a reliable system comes down to underst... |
| **`bullmq-specialist`** | [`bullmq-specialist/`](./bullmq-specialist) | BullMQ expert for Redis-backed job queues, background processing, and reliable async execution in Node.js/TypeScript applications. Use when "bullmq, bull que... |
| **`causal-scientist`** | [`causal-scientist/`](./causal-scientist) | Causal inference specialist for causal discovery, counterfactual reasoning, and effect estimationUse when "causal inference, causal discovery, counterfactual... |
| **`claude-automation-recommender`** | [`claude-automation-recommender/`](./claude-automation-recommender) | Analyze a codebase and recommend Google Antigravity automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommend... |
| **`claude-code-cicd`** | [`claude-code-cicd/`](./claude-code-cicd) | Expert in integrating Claude Code with CI/CD pipelines. Covers headless mode for non-interactive execution, GitHub Actions and GitLab CI/CD integration, auto... |
| **`claude-code-commands`** | [`claude-code-commands/`](./claude-code-commands) | Expert in creating custom slash commands for Claude Code. Slash commands encode repeatable workflows as markdown files, turning complex multi-step processes ... |
| **`claude-code-hooks`** | [`claude-code-hooks/`](./claude-code-hooks) | Expert in Claude Code hooks - user-defined shell commands that execute at specific points in Claude Code's lifecycle. Provides guaranteed automation that doe... |
| **`claude-md-improver`** | [`claude-md-improver/`](./claude-md-improver) | Audit and improve AGENTS.md files in repositories. Use when user asks to check, audit, update, improve, or fix AGENTS.md files. Scans for all AGENTS.md files... |
| **`claude-security`** | [`claude-security/`](./claude-security) | Antigravity Security: scan the codebase (the whole repository or a scoped part of it), scan changes (this branch's or a pull request's diff, or one commit), ... |
| **`code-cleanup`** | [`code-cleanup/`](./code-cleanup) | Systematic code cleanup and refactoring agent that identifies and fixes code quality issues without changing functionality. Focuses on: - Dead code removal -... |
| **`code-quality`** | [`code-quality/`](./code-quality) | Writing maintainable code - readability principles, SOLID patterns applied pragmatically, and the judgment to know when rules should bendUse when "code quali... |
| **`community-led-growth`** | [`community-led-growth/`](./community-led-growth) | Expert in community-led growth (CLG) - leveraging user communities to drive acquisition, retention, and expansion. Covers building developer communities, use... |
| **`computer-use-agents`** | [`computer-use-agents/`](./computer-use-agents) | Build AI agents that interact with computers like humans do - viewing screens, moving cursors, clicking buttons, and typing text. Covers Anthropic's Computer... |
| **`context-window-management`** | [`context-window-management/`](./context-window-management) | Strategies for managing LLM context windows including summarization, trimming, routing, and avoiding context rotUse when "context window, token limit, contex... |
| **`conversation-memory`** | [`conversation-memory/`](./conversation-memory) | Persistent memory systems for LLM conversations including short-term, long-term, and entity-based memoryUse when "conversation memory, remember, memory persi... |
| **`crewai`** | [`crewai/`](./crewai) | Expert in CrewAI - the leading role-based multi-agent framework used by 60% of Fortune 500 companies. Covers agent design with roles and goals, task definiti... |
| **`crypto-trading-bots`** | [`crypto-trading-bots/`](./crypto-trading-bots) | Comprehensive expertise in automated crypto trading systems, including DEX sniping bots, arbitrage strategies, MEV protection, Telegram trading bots, and ant... |
| **`customer-support-ai-tools`** | [`customer-support/`](./customer-support) | Master the AI tools that transform customer support from cost center to competitive advantage. Automate routine queries, empower agents, and delight customer... |
| **`document-ai`** | [`document-ai/`](./document-ai) | Comprehensive patterns for AI-powered document understanding including PDF parsing, OCR, invoice/receipt extraction, table extraction, multimodal RAG with vi... |
| **`energy-systems`** | [`energy-systems/`](./energy-systems) | Power systems engineering covering grid modeling, power flow analysis, energy storage dispatch, demand response, and electricity market economics. Spans tran... |
| **`file-uploads`** | [`file-uploads/`](./file-uploads) | Expert at handling file uploads and cloud storage. Covers S3, Cloudflare R2, presigned URLs, multipart uploads, and image optimization. Knows how to handle l... |
| **`firebase`** | [`firebase/`](./firebase) | Firebase gives you a complete backend in minutes - auth, database, storage, functions, hosting. But the ease of setup hides real complexity. Security rules a... |
| **`game-ai-behavior-trees`** | [`game-ai-behavior-trees/`](./game-ai-behavior-trees) | Building modular, debuggable AI behaviors using behavior trees for game NPCs and agentsUse when "behavior tree, bt, npc ai, ai behavior, game ai, decision tr... |
| **`godot-llm-integration`** | [`godot-llm-integration/`](./godot-llm-integration) | Integrating local LLMs into Godot games using NobodyWho and other Godot-native solutionsUse when "godot llm, nobodywho, godot ai npc, gdscript llm, godot loc... |
| **`hiring-strategy`** | [`hiring-strategy/`](./hiring-strategy) | Your first 10 hires determine your company culture. Your first 50 determine your execution capacity. Hiring is the most leveraged activity a founder does, an... |
| **`kubernetes`** | [`kubernetes/`](./kubernetes) | Kubernetes is the operating system for the cloud. It schedules containers, handles networking, manages storage, and keeps your apps running. But K8s has a st... |
| **`langfuse`** | [`langfuse/`](./langfuse) | Expert in Langfuse - the open-source LLM observability platform. Covers tracing, prompt management, evaluation, datasets, and integration with LangChain, Lla... |
| **`llm-architect`** | [`llm-architect/`](./llm-architect) | LLM application architecture expert for RAG, prompting, agents, and production AI systemsUse when "rag system, prompt engineering, llm application, ai agent,... |
| **`llm-fine-tuning`** | [`llm-fine-tuning/`](./llm-fine-tuning) | Use when adapting large language models to specific tasks, domains, or behaviors - covers LoRA, QLoRA, PEFT, instruction tuning, and full fine-tuning strateg... |
| **`llm-game-development`** | [`llm-game-development/`](./llm-game-development) | Comprehensive guide to using LLMs throughout the game development lifecycle - from design to implementation to testingUse when "ai game development, llm game... |
| **`llm-npc-dialogue`** | [`llm-npc-dialogue/`](./llm-npc-dialogue) | Building AI-powered NPCs that maintain personality, remember conversations, and never break characterUse when "npc dialogue, ai npc, llm npc, character dialo... |
| **`llm-security-audit`** | [`llm-security-audit/`](./llm-security-audit) | Comprehensive security auditing framework for LLM applications covering OWASP Top 10 for LLMs, threat modeling, penetration testing, and compliance with NIST... |
| **`mcp-developer`** | [`mcp-developer/`](./mcp-developer) | Model Context Protocol expert for building MCP servers, tools, resources, and client integrationsUse when "mcp server, model context protocol, claude code ex... |
| **`mcp-server-development`** | [`mcp-server-development/`](./mcp-server-development) | Building production-ready Model Context Protocol servers that expose tools, resources, and prompts to AI assistantsUse when "mcp server, model context protoc... |
| **`mobile-game-dev`** | [`mobile-game-dev/`](./mobile-game-dev) | Expert mobile game developer specializing in iOS and Android game optimization, touch input design, battery and thermal management, device fragmentation hand... |
| **`model-optimization`** | [`model-optimization/`](./model-optimization) | Use when reducing model size, improving inference speed, or deploying to edge devices - covers quantization, pruning, knowledge distillation, ONNX export, an... |
| **`multi-agent-orchestration`** | [`multi-agent-orchestration/`](./multi-agent-orchestration) | Patterns for coordinating multiple LLM agents including sequential, parallel, router, and hierarchical architectures—the AI equivalent of microservicesUse wh... |
| **`neural-architecture-search`** | [`neural-architecture-search/`](./neural-architecture-search) | Use when automating model architecture design, optimizing hyperparameters, or exploring neural network configurations - covers NAS algorithms, search spaces,... |
| **`on-device-ai`** | [`on-device-ai/`](./on-device-ai) | Patterns for running AI models locally in browsers using WebGPU, Transformers.js, WebLLM, and ONNX Runtime. Zero API costs, full privacy. Use when "on-device... |
| **`prompt-caching`** | [`prompt-caching/`](./prompt-caching) | Caching strategies for LLM prompts including Anthropic prompt caching, response caching, and CAG (Cache Augmented Generation)Use when "prompt caching, cache ... |
| **`prompt-engineer`** | [`prompt-engineer/`](./prompt-engineer) | Expert in designing effective prompts for LLM-powered applications. Masters prompt structure, context management, output formatting, and prompt evaluation. U... |
| **`prompt-engineering-creative`** | [`prompt-engineering-creative/`](./prompt-engineering-creative) | The meta-skill that powers all other AI tools. Prompt engineering for creative applications is the art and science of communicating with AI models to produce... |
| **`prompt-injection-defense`** | [`prompt-injection-defense/`](./prompt-injection-defense) | Defense techniques against prompt injection attacks including direct injection, indirect injection, and jailbreaks - theUse when "prompt injection, jailbreak... |
| **`prompt-to-game`** | [`prompt-to-game/`](./prompt-to-game) | Master the art of "vibe coding" - creating playable games through natural language prompts to AI. Covers effective prompting strategies, framework choices, w... |
| **`quantitative-research`** | [`quantitative-research/`](./quantitative-research) | World-class systematic trading research - backtesting, alpha generation, factor models, statistical arbitrage. Transform hypotheses into edges. Use when "bac... |
| **`rag-engineer`** | [`rag-engineer/`](./rag-engineer) | Expert in building Retrieval-Augmented Generation systems. Masters embedding models, vector databases, chunking strategies, and retrieval optimization for LL... |
| **`rag-implementation`** | [`rag-implementation/`](./rag-implementation) | Retrieval-Augmented Generation patterns including chunking, embeddings, vector stores, and retrieval optimizationUse when "rag, retrieval augmented, vector s... |
| **`reinforcement-learning`** | [`reinforcement-learning/`](./reinforcement-learning) | Use when implementing RL algorithms, training agents with rewards, or aligning LLMs with human feedback - covers policy gradients, PPO, Q-learning, RLHF, and... |
| **`renewable-energy`** | [`renewable-energy/`](./renewable-energy) | Design, model, and optimize renewable energy systems including solar PV, wind power, energy storage, and grid integration. Use when "renewable energy, solar ... |
| **`review-pr`** | [`review-pr/`](./review-pr) | Comprehensive PR review using specialized agents |
| **`revise-claude-md`** | [`revise-claude-md/`](./revise-claude-md) | Update AGENTS.md with learnings from this session |
| **`semantic-search`** | [`semantic-search/`](./semantic-search) | Build production-ready semantic search systems using vector databases, embeddings, and retrieval-augmented generation (RAG). Covers vector DB selection (Pine... |
| **`space-data-processing`** | [`space-data-processing/`](./space-data-processing) | Use when processing satellite imagery, hyperspectral data, SAR imagery, or applying machine learning to remote sensing data for Earth observation. Use when "... |
| **`structured-output`** | [`structured-output/`](./structured-output) | Expert in getting reliable, typed outputs from LLMs. Covers JSON mode, function calling, Instructor library, Outlines for constrained generation, Pydantic va... |
| **`supabase-backend`** | [`supabase-backend/`](./supabase-backend) | Expert knowledge for Supabase database, RLS, and backend patternsUse when "supabase, row level security, rls, postgres, database policy, supabase storage, su... |
| **`supabase-security`** | [`supabase-security/`](./supabase-security) | Deep expertise in securing Supabase applications. Covers Row Level Security  (RLS) patterns, auth token validation, storage security, multi-tenant isolation.... |
| **`synthetic-data`** | [`synthetic-data/`](./synthetic-data) | Patterns for generating synthetic data for ML training, testing, and privacy. Covers LLM-based generation, tabular synthesis, and quality validation. Use whe... |
| **`testing-strategies`** | [`testing-strategies/`](./testing-strategies) | Good tests give you confidence to ship. Bad tests give you a false sense of security while slowing you down. The goal isn't 100% coverage - it's the right te... |
| **`transformer-architecture`** | [`transformer-architecture/`](./transformer-architecture) | Use when implementing attention mechanisms, building custom transformer models, understanding positional encoding, or optimizing transformer inference - cove... |
| **`typescript-strict`** | [`typescript-strict/`](./typescript-strict) | Expert knowledge for TypeScript strict mode patterns and type safetyUse when "typescript, type error, strict mode, generics, type inference, any type, type a... |
| **`unity-llm-integration`** | [`unity-llm-integration/`](./unity-llm-integration) | Integrating local and cloud LLMs into Unity games for AI NPCs, dialogue, and intelligent behaviorsUse when "unity llm, llmunity, unity ai npc, unity local ll... |
| **`unreal-llm-integration`** | [`unreal-llm-integration/`](./unreal-llm-integration) | Integrating local and cloud LLMs into Unreal Engine games for AI NPCs and intelligent behaviorsUse when "unreal llm, ue5 ai npc, unreal chatgpt, blueprint ll... |
| **`v0-dev`** | [`v0-dev/`](./v0-dev) | Expert in using v0.dev for AI-powered UI generation. Covers prompting strategies, component iteration, shadcn/ui integration, export workflows, and customiza... |
| **`vector-specialist`** | [`vector-specialist/`](./vector-specialist) | Embedding and vector retrieval expert for semantic searchUse when "vector search, embeddings, semantic search, qdrant, pgvector, similarity search, reranking... |
| **`voice-agents`** | [`voice-agents/`](./voice-agents) | Voice agents represent the frontier of AI interaction - humans speaking naturally with AI systems. The challenge isn't just speech recognition and synthesis,... |
| **`voice-ai-development`** | [`voice-ai-development/`](./voice-ai-development) | Expert in building voice AI applications - from real-time voice agents to voice-enabled apps. Covers OpenAI Realtime API, Vapi for voice agents, Deepgram for... |
| **`workflow-automation`** | [`workflow-automation/`](./workflow-automation) | Workflow automation is the infrastructure that makes AI agents reliable. Without durable execution, a network hiccup during a 10-step payment flow means lost... |

<br/>

## 🎨 Frontend, UI/UX, Design Systems & 3D

> *193 specialized runbooks available in this domain.*

| Skill Identifier | Runbook Path | Core Capabilities & Description |
| :--- | :--- | :--- |
| **`3d-modeling`** | [`3d-modeling/`](./3d-modeling) | Expert 3D modeling specialist with deep knowledge of topology, UV mapping, game-ready and film-ready pipelines, DCC tool workflows (Blender, Maya, ZBrush, 3d... |
| **`3d-web-experience`** | [`3d-web-experience/`](./3d-web-experience) | Expert in building 3D experiences for the web - Three.js, React Three Fiber, Spline, WebGL, and interactive 3D scenes. Covers product configurators, 3D portf... |
| **`a-b-testing`** | [`a-b-testing/`](./a-b-testing) | The science of learning through controlled experimentation. A/B testing isn't about picking winners—it's about building a culture of validated learning and r... |
| **`accessibility`** | [`accessibility/`](./accessibility) | Accessibility isn't a feature - it's a fundamental quality of good software. 1 in 4 adults has a disability. Many more have temporary impairments or situatio... |
| **`accessibility-design`** | [`accessibility-design/`](./accessibility-design) | World-class accessibility design expertise combining the inclusive design principles of Microsoft's Inclusive Design team, the technical rigor of the W3C WCA... |
| **`ai-brand-kit`** | [`ai-brand-kit/`](./ai-brand-kit) | Build comprehensive AI-native brand asset systems that maintain consistency across all AI-generated content. Train AI tools on brand guidelines, create reusa... |
| **`ai-code-generation`** | [`ai-code-generation/`](./ai-code-generation) | Comprehensive patterns for building AI-powered code generation tools, code assistants, automated refactoring, code review, and structured output generation u... |
| **`ai-personalization`** | [`ai-personalization/`](./ai-personalization) | Building AI-powered personalization systems: recommendation engines, collaborative filtering, content-based filtering, user preference learning, cold-start s... |
| **`ai-world-building`** | [`ai-world-building/`](./ai-world-building) | The ultimate brand asset: a consistent, explorable universe generated by AI. This skill covers creating coherent brand worlds, consistent characters, archite... |
| **`aidesigner-frontend`** | [`aidesigner-frontend/`](./aidesigner-frontend) | Use this skill when the user wants to create or redesign a frontend, landing page, dashboard, marketing page, or other UI with AIDesigner. Prefer the connect... |
| **`algorithmic-trading`** | [`algorithmic-trading/`](./algorithmic-trading) | Use when building trading systems, backtesting strategies, implementing execution algorithms, or analyzing market microstructure - covers strategy developmen... |
| **`ambassador-programs`** | [`ambassador-programs/`](./ambassador-programs) | Expert in designing and running ambassador, champion, and advocacy programs. Covers recruiting community leaders, structuring tiers and rewards, managing at ... |
| **`analytics-architecture`** | [`analytics-architecture/`](./analytics-architecture) | Measure what matters. Event tracking design, attribution modeling, funnel analysis, experimentation platforms. The complete guide to understanding what your ... |
| **`animation-systems`** | [`animation-systems/`](./animation-systems) | Expert in real-time game animation systems including skeletal animation, blend trees, state machines, inverse kinematics, root motion, procedural animation, ... |
| **`api-design`** | [`api-design/`](./api-design) | Expert at designing clean, consistent, and developer-friendly APIs. Covers RESTful conventions, versioning strategies, error handling, pagination, rate limit... |
| **`api-designer`** | [`api-designer/`](./api-designer) | API design specialist for REST, GraphQL, gRPC, versioning strategies, and developer experienceUse when "api design, rest, graphql, grpc, openapi, swagger, ve... |
| **`authentication-oauth`** | [`authentication-oauth/`](./authentication-oauth) | Expert guidance on authentication implementation including OAuth 2.0/OIDC, JWT tokens, session management, and secure password handling. Covers both implemen... |
| **`aws-serverless`** | [`aws-serverless/`](./aws-serverless) | Specialized skill for building production-ready serverless applications on AWS. Covers Lambda functions, API Gateway, DynamoDB, SQS/SNS event-driven patterns... |
| **`backend`** | [`backend/`](./backend) | World-class backend engineering - distributed systems, database architecture, API design, and the battle scars from scaling systems that handle millions of r... |
| **`bioinformatics-workflows`** | [`bioinformatics-workflows/`](./bioinformatics-workflows) | Patterns for building, maintaining, and scaling bioinformatics workflows. Covers Nextflow, Snakemake, WDL/Cromwell, container orchestration, and best practic... |
| **`blockchain-defi`** | [`blockchain-defi/`](./blockchain-defi) | Use when building DeFi protocols, implementing AMMs, yield farming strategies, or integrating with Ethereum/L2s - covers smart contract patterns, liquidity p... |
| **`blockchain-privacy`** | [`blockchain-privacy/`](./blockchain-privacy) | Expert in on-chain privacy technologies - ZK-SNARKs, ZK-STARKs, mixers, stealth addresses, ring signatures, and confidential transactions for building privac... |
| **`board-game-design`** | [`board-game-design/`](./board-game-design) | Designing tabletop games - from core mechanics to manufacturing, from prototyping to KickstarterUse when "board game, tabletop, card game, worker placement, ... |
| **`brand-storytelling`** | [`brand-storytelling/`](./brand-storytelling) | The art and science of narrative-driven brand communication. This skill transforms brand messages into compelling stories that connect emotionally, build mem... |
| **`browser-extension-builder`** | [`browser-extension-builder/`](./browser-extension-builder) | Expert in building browser extensions that solve real problems - Chrome, Firefox, and cross-browser extensions. Covers extension architecture, manifest v3, c... |
| **`business-model-design`** | [`business-model-design/`](./business-model-design) | Expert in business model design - the architecture of how a company creates, delivers, and captures value. Covers business model canvas, revenue model select... |
| **`card-game-design`** | [`card-game-design/`](./card-game-design) | World-class expertise in TCG/CCG design, resource systems, and metagame balanceUse when "card game design, TCG design, CCG design, trading card game, collect... |
| **`channel-partnerships`** | [`channel-partnerships/`](./channel-partnerships) | Expert in building and scaling channel partner programs - resellers, agencies, system integrators, and technology partners that extend your reach and revenue... |
| **`chaos-engineer`** | [`chaos-engineer/`](./chaos-engineer) | Resilience testing specialist for failure injection, game day planning, and building confidence in system reliabilityUse when "chaos engineering, resilience ... |
| **`character-design`** | [`character-design/`](./character-design) | Creating memorable, readable, and emotionally resonant game characters that work at every scale and in every contextUse when "character design, design a char... |
| **`cliffhanger-craft`** | [`cliffhanger-craft/`](./cliffhanger-craft) | Expert in creating endings that demand continuation. Covers serialized content, episode structure, tension building, and the psychology of incomplete narrati... |
| **`clinical-trial-analysis`** | [`clinical-trial-analysis/`](./clinical-trial-analysis) | Patterns for designing and analyzing clinical trials, including survival analysis, endpoint selection, sample size calculation, interim analyses, and regulat... |
| **`code-review`** | [`code-review/`](./code-review) | The art of reviewing code that improves both the codebase and the developer - sharing knowledge, maintaining standards, and building cultureUse when "code re... |
| **`code-review-diplomacy`** | [`code-review-diplomacy/`](./code-review-diplomacy) | Expert in the human side of code review. Covers giving feedback that lands, receiving criticism gracefully, navigating disagreements, and building a healthy ... |
| **`code-reviewer`** | [`code-reviewer/`](./code-reviewer) | Code review specialist for quality standards, design patterns, security review, and constructive feedbackUse when "code review, pull request, PR review, code... |
| **`color-theory`** | [`color-theory/`](./color-theory) | World-class color theory expertise combining the scientific precision of Josef Albers' "Interaction of Color," the systematic thinking of color systems from ... |
| **`combat-design`** | [`combat-design/`](./combat-design) | Expert in designing and implementing visceral, satisfying combat systems. Masters hitbox/hurtbox design, frame data, combo systems, enemy archetypes, damage ... |
| **`community-building`** | [`community-building/`](./community-building) | Your most loyal users aren't just customers - they're potential advocates, contributors, and community members who can become the engine of your growth. Comm... |
| **`community-growth`** | [`community-growth/`](./community-growth) | Expert in growing and engaging communities sustainably. Covers acquisition channels, activation strategies, engagement programs, events, content, and retenti... |
| **`community-strategy`** | [`community-strategy/`](./community-strategy) | Expert in designing community strategies that align with business goals while creating genuine value for members. Covers community-market fit, positioning, c... |
| **`compliance-automation`** | [`compliance-automation/`](./compliance-automation) | Use when implementing policy-as-code, continuous compliance monitoring, automated evidence collection, or audit-ready systems requiring SOC2/ISO/PCI/HIPAA co... |
| **`computer-vision-deep`** | [`computer-vision-deep/`](./computer-vision-deep) | Use when implementing object detection, semantic/instance segmentation, 3D vision, or video understanding - covers YOLO, SAM, depth estimation, and multi-mod... |
| **`contract-analysis`** | [`contract-analysis/`](./contract-analysis) | Use when reviewing contracts, extracting key terms, identifying risks, or building contract analysis tools - covers NLP approaches, clause identification, an... |
| **`course-creation`** | [`course-creation/`](./course-creation) | Expert in designing and structuring online courses - curriculum architecture, learning outcomes, module design, and assessment strategies. Covers backward de... |
| **`create-docker-mcp-tunnel`** | [`create-docker-mcp-tunnel/`](./create-docker-mcp-tunnel) | Stand up an Google Antigravity Ecosystem MCP tunnel locally with Docker Compose so Antigravity can call a private MCP server (manual-credentials quickstart). |
| **`creature-design`** | [`creature-design/`](./creature-design) | Designing anatomically plausible, visually distinctive creatures that communicate threat, personality, and role through form - from terrifying bosses to coll... |
| **`customer-success`** | [`customer-success/`](./customer-success) | Acquisition is expensive. Retention is profitable. Customer success is the discipline of ensuring customers achieve their desired outcomes with your product ... |
| **`data-engineer`** | [`data-engineer/`](./data-engineer) | Data pipeline specialist for ETL design, data quality, CDC patterns, and batch/stream processingUse when "data pipeline, etl, cdc, data quality, batch proces... |
| **`data-governance`** | [`data-governance/`](./data-governance) | Use when implementing data governance frameworks, building data catalogs, establishing data lineage, defining data quality rules, or setting up data stewards... |
| **`database-architect`** | [`database-architect/`](./database-architect) | Database design specialist for schema modeling, query optimization, indexing strategies, and data integrityUse when "database design, schema, indexes, query ... |
| **`database-schema-design`** | [`database-schema-design/`](./database-schema-design) | World-class database schema design - data modeling, migrations, relationships, and the battle scars from scaling databases that store billions of rowsUse whe... |
| **`defi-architect`** | [`defi-architect/`](./defi-architect) | DeFi protocol specialist for AMMs, lending protocols, yield strategies, and economic securityUse when "defi, amm, liquidity pool, lending protocol, yield far... |
| **`derivatives-pricing`** | [`derivatives-pricing/`](./derivatives-pricing) | Use when pricing options, calculating Greeks, implementing exotic derivatives, or building pricing engines - covers Black-Scholes, binomial trees, Monte Carl... |
| **`design-ai-tools`** | [`design/`](./design) | Master the AI tools that accelerate design work. From UI generation to image editing, create professional designs faster. Use when "design, UI, graphics, ima... |
| **`design-systems`** | [`design-systems/`](./design-systems) | World-class design systems architecture - tokens, components, documentation, and governance. Design systems create the shared language between design and eng... |
| **`dev-communications`** | [`dev-communications/`](./dev-communications) | The craft of communicating technical concepts clearly to developers. Developer communications isn't marketing—it's about building trust through transparency,... |
| **`developer-community`** | [`developer-community/`](./developer-community) | Expert in building and nurturing developer communities - DevRel strategy, developer experience, technical content, documentation communities, and turning dev... |
| **`digital-twin`** | [`digital-twin/`](./digital-twin) | Build and maintain digital twins - virtual representations of physical systems that synchronize with real-world counterparts for monitoring, prediction, and ... |
| **`disaster-recovery`** | [`disaster-recovery/`](./disaster-recovery) | Use when designing disaster recovery strategies, defining RPO/RTO targets, implementing failover mechanisms, or conducting chaos engineering tests - covers a... |
| **`discord-bot-architect`** | [`discord-bot-architect/`](./discord-bot-architect) | Specialized skill for building production-ready Discord bots. Covers Discord.js (JavaScript) and Pycord (Python), gateway intents, slash commands, interactiv... |
| **`discord-mastery`** | [`discord-mastery/`](./discord-mastery) | Expert in building and managing thriving Discord communities. Covers server architecture, role systems, bot ecosystems, engagement features, and moderation a... |
| **`discrete-event-simulation`** | [`discrete-event-simulation/`](./discrete-event-simulation) | Design and implement discrete event simulations (DES) for systems where state changes occur at discrete time points: queues, manufacturing, logistics, networ... |
| **`docker-containerization`** | [`docker-containerization/`](./docker-containerization) | World-class container image building - Dockerfiles, multi-stage builds, security hardening, and the battle scars from images that broke in productionUse when... |
| **`dockerfile-optimizer`** | [`dockerfile-optimizer/`](./dockerfile-optimizer) | Use this skill when authoring or optimizing Dockerfiles, configuring multi-stage builds, reducing image sizes, or hardening container security. |
| **`early-stage-hustle`** | [`early-stage-hustle/`](./early-stage-hustle) | Before product-market fit, your job is to learn as fast as possible. That means doing things that won't scale - manual onboarding, concierge service, recruit... |
| **`easter-egg-design`** | [`easter-egg-design/`](./easter-egg-design) | Expert in designing hidden features, secret codes, and delightful surprises in products. Covers discovery mechanics, reward calibration, shareability trigger... |
| **`education-business`** | [`education-business/`](./education-business) | Expert in the business of online education - pricing strategies, launch playbooks, revenue models, positioning, and building sustainable education businesses... |
| **`enterprise-architecture`** | [`enterprise-architecture/`](./enterprise-architecture) | Use when designing enterprise systems, applying TOGAF framework, creating capability maps, implementing domain-driven design, or planning technology transfor... |
| **`environment-art`** | [`environment-art/`](./environment-art) | Expert knowledge for environment art in games - modular design, visual hierarchy, color scripting, environmental storytelling, optimization, and world-buildi... |
| **`error-handling`** | [`error-handling/`](./error-handling) | Expert at building resilient applications through proper error handling. Covers Result types, error boundaries, try-catch patterns, typed errors, and gracefu... |
| **`experimental-design`** | [`experimental-design/`](./experimental-design) | Formal Design of Experiments (DOE) methodology for maximizing information from experiments while minimizing resources. Covers factorial designs, blocking, ra... |
| **`expo`** | [`expo/`](./expo) | Expert in Expo for React Native development. Covers Expo Router, EAS Build and Submit, development builds, native module integration, and production deployme... |
| **`feature-dev`** | [`feature-dev/`](./feature-dev) | Guided feature development with codebase understanding and architecture focus |
| **`feature-prioritization`** | [`feature-prioritization/`](./feature-prioritization) | Expert in feature prioritization - the art and science of deciding what to build and in what order. Covers prioritization frameworks, roadmap planning, stake... |
| **`figma-design-to-code`** | [`figma-design-to-code/`](./figma-design-to-code) | Inspect Figma design files, extract layout tokens, and translate component frames into production-ready React and Tailwind CSS code. |
| **`forms-validation`** | [`forms-validation/`](./forms-validation) | Expert at building robust form experiences. Covers React Hook Form, Zod validation, server actions, progressive enhancement, error handling, and accessible f... |
| **`founder-mode`** | [`founder-mode/`](./founder-mode) | Paul Graham's founder mode. When to delegate vs. dive deep. Maintaining velocity as you scale. Avoiding "professional CEO" traps. The operating mode that bui... |
| **`fpga-design`** | [`fpga-design/`](./fpga-design) | Patterns for FPGA development including RTL design (Verilog/VHDL), timing closure, clock domain crossing, high-level synthesis, and verification. Covers both... |
| **`frontend`** | [`frontend/`](./frontend) | World-class frontend engineering - React philosophy, performance, accessibility, and production-grade interfacesUse when "frontend, react, vue, svelte, next.... |
| **`frontend-design`** | [`frontend-design/`](./frontend-design) | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and making... |
| **`fundraising-strategy`** | [`fundraising-strategy/`](./fundraising-strategy) | Raising money is a means to an end, not the end itself. Great companies can be built with or without venture capital. But if you're raising, you need to unde... |
| **`game-ai-behavior`** | [`game-ai-behavior/`](./game-ai-behavior) | Expert in designing and implementing intelligent game AI systems including behavior trees, finite state machines, GOAP, utility AI, pathfinding, steering beh... |
| **`game-audio`** | [`game-audio/`](./game-audio) | Expert game audio designer and implementer specializing in interactive sound design, adaptive music systems, spatial audio, and audio middleware integration.... |
| **`game-design`** | [`game-design/`](./game-design) | Building interactive experiences that engage, challenge, and delight playersUse when "game, gamedev, game development, phaser, unity, unreal, godot, gameplay... |
| **`game-design-core`** | [`game-design-core/`](./game-design-core) | The foundational theory of interactive experience design - loops, motivation, feel, and the art of meaningful playUse when "game design, core loop, game feel... |
| **`game-development`** | [`game-development/`](./game-development) | Building interactive experiences that engage, challenge, and delight playersUse when "game, gamedev, game development, phaser, unity, unreal, godot, gameplay... |
| **`game-ui-design`** | [`game-ui-design/`](./game-ui-design) | World-class game UI design expertise combining the clarity of Nintendo's UI philosophy, the immersive diegetic interfaces of Dead Space and Metroid Prime, an... |
| **`gcp-cloud-run`** | [`gcp-cloud-run/`](./gcp-cloud-run) | Specialized skill for building production-ready serverless applications on GCP. Covers Cloud Run services (containerized), Cloud Run Functions (event-driven)... |
| **`genomics-pipelines`** | [`genomics-pipelines/`](./genomics-pipelines) | Patterns for building robust, reproducible genomics analysis pipelines. Covers workflow managers, NGS data processing, variant calling, RNA-seq, and common b... |
| **`graphql-architect`** | [`graphql-architect/`](./graphql-architect) | GraphQL API specialist for schema design, resolvers, federation, and performance optimizationUse when "graphql, schema design, resolvers, federation, apollo,... |
| **`ground-station-ops`** | [`ground-station-ops/`](./ground-station-ops) | Use when designing ground station networks, scheduling satellite contacts, processing telemetry, commanding spacecraft, or analyzing link budgets. Use when "... |
| **`growth-loops`** | [`growth-loops/`](./growth-loops) | Expert in designing and optimizing growth loops - self-reinforcing systems where the output of one cycle becomes the input for the next. Covers viral loops, ... |
| **`hand-gesture-recognition`** | [`hand-gesture-recognition/`](./hand-gesture-recognition) | Computer vision expert specializing in real-time hand tracking and gesture interface designUse when "hand tracking, gesture recognition, mediapipe, hand gest... |
| **`hr-recruiting-ai-tools`** | [`hr-recruiting/`](./hr-recruiting) | Master the AI tools that transform hiring and HR operations. From sourcing candidates to onboarding, find and retain great talent faster. Use when "hiring, r... |
| **`i18n`** | [`i18n/`](./i18n) | Expert at building multi-language applications. Covers next-intl, react-i18next, ICU message format, RTL support, date/number formatting, and translation wor... |
| **`icon-design`** | [`icon-design/`](./icon-design) | The craft of designing icons that communicate instantly across cultures, contexts, and scales. Icon design bridges semiotics, cognitive psychology, and visua... |
| **`incident-postmortem`** | [`incident-postmortem/`](./incident-postmortem) | Expert in running effective incident postmortems. Covers blameless analysis, root cause investigation, action item prioritization, and building a learning cu... |
| **`integration-patterns`** | [`integration-patterns/`](./integration-patterns) | Use when designing system integrations, implementing API gateways, event-driven architectures, ESB patterns, or hybrid cloud connectivityUse when ", " mentio... |
| **`interactive-portfolio`** | [`interactive-portfolio/`](./interactive-portfolio) | Expert in building portfolios that actually land jobs and clients - not just showing work, but creating memorable experiences. Covers developer portfolios, d... |
| **`ios-swift-specialist`** | [`ios-swift-specialist/`](./ios-swift-specialist) | Native iOS development specialist for Swift, SwiftUI, UIKit, and Apple platform patternsUse when "ios, swift, swiftui, uikit, xcode, apple, iphone, ipad, app... |
| **`lab-automation`** | [`lab-automation/`](./lab-automation) | Patterns for laboratory automation including liquid handling robotics, LIMS integration, protocol development, quality control, and high-throughput workflows... |
| **`landing-page-design`** | [`landing-page-design/`](./landing-page-design) | World-class landing page expertise combining conversion rate optimization science, persuasive design psychology, and the craft of pages that turn visitors in... |
| **`langgraph`** | [`langgraph/`](./langgraph) | Expert in LangGraph - the production-grade framework for building stateful, multi-actor AI applications. Covers graph construction, state management, cycles ... |
| **`learning-experience`** | [`learning-experience/`](./learning-experience) | Expert in designing engaging learning experiences - completion optimization, multimedia learning, interactivity, gamification, and retention strategies. Cove... |
| **`level-design`** | [`level-design/`](./level-design) | World-class level design expertise - spatial storytelling, player flow, blockout methodology, and the invisible hand that guides players without them knowing... |
| **`lighting-design`** | [`lighting-design/`](./lighting-design) | Expert knowledge for real-time and baked lighting in games - from cinematography fundamentals to engine-specific optimization, covering GI, time-of-day, volu... |
| **`live-education`** | [`live-education/`](./live-education) | Expert in live learning experiences - cohort-based courses, workshops, webinars, coaching sessions, and real-time facilitation. Covers designing for synchron... |
| **`lore-building`** | [`lore-building/`](./lore-building) | Expert in creating rich backstories, fictional universes, and ARGs (Alternate Reality Games). Covers world-building, mystery construction, community-driven s... |
| **`mcp-product`** | [`mcp-product/`](./mcp-product) | Build MCP tools that are sticky for vibe coders and powerful for developersUse when "Designing new MCP tools, Improving tool UX or DX, Writing error messages... |
| **`micro-saas-launcher`** | [`micro-saas-launcher/`](./micro-saas-launcher) | Expert in launching small, focused SaaS products fast - the indie hacker approach to building profitable software. Covers idea validation, MVP development, p... |
| **`microservices-patterns`** | [`microservices-patterns/`](./microservices-patterns) | Patterns for designing, building, and operating microservices architectures. Covers service decomposition, inter-service communication, resilience patterns, ... |
| **`miro-whiteboard`** | [`miro-whiteboard/`](./miro-whiteboard) | Connect to Miro boards, create sticky notes, build visual flowcharts, and manage brainstorming canvases via MCP. |
| **`mission-planning`** | [`mission-planning/`](./mission-planning) | Use when designing space missions, computing launch windows, optimizing trajectories, analyzing payload constraints, or planning mission phases and contingen... |
| **`moat-building`** | [`moat-building/`](./moat-building) | Warren Buffett said he looks for "economic castles protected by unbreachable moats." A moat is a sustainable competitive advantage that protects your busines... |
| **`monte-carlo`** | [`monte-carlo/`](./monte-carlo) | Design and implement Monte Carlo methods for uncertainty quantification, risk analysis, and probabilistic simulations across scientific and financial domains... |
| **`motion-design`** | [`motion-design/`](./motion-design) | World-class motion design expertise combining Disney's 12 principles of animation, Material Design's motion system, and the performance-first philosophy of p... |
| **`motion-graphics`** | [`motion-graphics/`](./motion-graphics) | World-class motion graphics expertise combining the animation principles of Disney, the kinetic typography of MK12, and the visual storytelling of studios li... |
| **`multi-tenancy`** | [`multi-tenancy/`](./multi-tenancy) | Use when designing multi-tenant SaaS architectures, implementing tenant isolation, data partitioning strategies, or building billing/metering systems - cover... |
| **`multimodal-ai`** | [`multimodal-ai/`](./multimodal-ai) | Patterns for building multimodal AI applications that combine text, images, audio, and video. Covers vision APIs, audio transcription, and unified pipelines.... |
| **`narrative-design`** | [`narrative-design/`](./narrative-design) | The craft of weaving story into interactive systems where the player is both audience and author. This skill covers the unique challenges of game narrative: ... |
| **`notion-template-business`** | [`notion-template-business/`](./notion-template-business) | Expert in building and selling Notion templates as a business - not just making templates, but building a sustainable digital product business. Covers templa... |
| **`observability-sre`** | [`observability-sre/`](./observability-sre) | Site reliability specialist for Prometheus metrics, distributed tracing, alerting strategies, and SLO designUse when "observability, monitoring, prometheus, ... |
| **`perpetuals-trading`** | [`perpetuals-trading/`](./perpetuals-trading) | Comprehensive expertise in decentralized perpetual futures protocols, including GMX, dYdX, Hyperliquid, and similar platforms. Covers funding rate mechanics,... |
| **`personal-tool-builder`** | [`personal-tool-builder/`](./personal-tool-builder) | Expert in building custom tools that solve your own problems first. The best products often start as personal tools - scratch your own itch, build for yourse... |
| **`physics-simulation`** | [`physics-simulation/`](./physics-simulation) | Patterns for physics-based simulation including numerical integration, rigid body dynamics, fluid simulation, finite element methods, and multi-physics coupl... |
| **`pixel-art`** | [`pixel-art/`](./pixel-art) | Deep pixel art expertise covering fundamentals, limited palettes, dithering patterns, subpixel animation, tile design, retro hardware constraints, and HD-2D ... |
| **`pixel-art-sprites`** | [`pixel-art-sprites/`](./pixel-art-sprites) | Specialist in pixel art creation, sprite animation, and limited palette designUse when "pixel art, sprites, sprite sheet, sprite animation, retro game art, 8... |
| **`player-onboarding`** | [`player-onboarding/`](./player-onboarding) | First Time User Experience (FTUE) design that teaches through play, hooks players in 30 seconds, and retains them for lifeUse when "tutorial, onboarding, tea... |
| **`prisma`** | [`prisma/`](./prisma) | Expert in Prisma - the TypeScript ORM for type-safe database access. Covers schema design, migrations, Prisma Client queries, relations, edge deployment, and... |
| **`product-led-growth`** | [`product-led-growth/`](./product-led-growth) | Expert in product-led growth (PLG) - the go-to-market strategy where the product itself drives customer acquisition, activation, conversion, and expansion. C... |
| **`product-strategy`** | [`product-strategy/`](./product-strategy) | World-class product strategy expertise combining Marty Cagan's outcome-driven product management, Steve Jobs' product intuition, and modern Silicon Valley be... |
| **`progression-systems`** | [`progression-systems/`](./progression-systems) | Expert in designing compelling progression systems that create the "one more turn" hook while respecting player time. Deep knowledge of XP mathematics, skill... |
| **`puzzle-design`** | [`puzzle-design/`](./puzzle-design) | Crafting puzzles that teach through play, create "aha" moments, and challenge without frustratingUse when "puzzle, puzzle design, puzzle game, puzzle mechani... |
| **`query-optimizer`** | [`query-optimizer/`](./query-optimizer) | Use this skill when profiling slow SQL queries, analyzing EXPLAIN ANALYZE execution plans, resolving N+1 queries, or designing composite indexes. |
| **`queue-workers`** | [`queue-workers/`](./queue-workers) | Patterns for building reliable background job processing systems. Covers message queues, worker pools, retries, dead letter handling, and async workflow orch... |
| **`refactoring-guide`** | [`refactoring-guide/`](./refactoring-guide) | Safe code transformation - changing structure without changing behavior. From Fowler's catalog to legacy code strategies, knowing when and how to improve cod... |
| **`rigging-animation`** | [`rigging-animation/`](./rigging-animation) | World-class character rigging and animation systems expertise - skeleton hierarchies, deformation, FK/IK, facial rigs, weight painting, and game engine integ... |
| **`risk-modeling`** | [`risk-modeling/`](./risk-modeling) | Use when building VaR models, stress testing portfolios, Monte Carlo simulations, or implementing enterprise risk management - covers market risk, credit ris... |
| **`roblox-development`** | [`roblox-development/`](./roblox-development) | World-class Roblox game development - Lua scripting, Roblox Studio, game systems, monetization, and building experiences that millions play. Use when "roblox... |
| **`sales-ai-tools`** | [`sales/`](./sales) | Master the AI tools that supercharge your sales process. From prospecting to closing, automate the grind and focus on building relationships that convert. Us... |
| **`schema-architect`** | [`schema-architect/`](./schema-architect) | Use this skill when designing database schemas, writing table migrations, defining foreign key constraints, or modeling entities in relational and document d... |
| **`scope-creep-defense`** | [`scope-creep-defense/`](./scope-creep-defense) | Expert in protecting projects from scope creep. Covers requirement management, stakeholder negotiation, saying no diplomatically, and keeping projects focuse... |
| **`scroll-experience`** | [`scroll-experience/`](./scroll-experience) | Expert in building immersive scroll-driven experiences - parallax storytelling, scroll animations, interactive narratives, and cinematic web experiences. Lik... |
| **`sdk-builder`** | [`sdk-builder/`](./sdk-builder) | Client library architect for SDK design, API ergonomics, versioning, and developer experienceUse when "sdk design, client library, api client, developer expe... |
| **`seo`** | [`seo/`](./seo) | Search engine optimization for startups. Covers technical SEO, content strategy, and link building. Focus on sustainable approaches that compound over time r... |
| **`shadcn-ui`** | [`shadcn-ui/`](./shadcn-ui) | Discover, inspect, scaffold, and integrate UI components and full-page blocks from Shadcn UI and React Bits (Starter and Pro) registries via MCP. |
| **`slack-bot-builder`** | [`slack-bot-builder/`](./slack-bot-builder) | Build Slack apps using the Bolt framework across Python, JavaScript, and Java. Covers Block Kit for rich UIs, interactive components, slash commands, event h... |
| **`social-community`** | [`social-community/`](./social-community) | Expert in building community presence across social platforms - Twitter/X, Reddit, Farcaster, and forums. Covers platform-specific strategies, cross-platform... |
| **`spacecraft-systems`** | [`spacecraft-systems/`](./spacecraft-systems) | Use when designing or analyzing spacecraft subsystems including ADCS, power, thermal control, propulsion, communications, and command & data handling. Use wh... |
| **`state-management`** | [`state-management/`](./state-management) | Expert guidance on frontend state management patterns including Redux, Zustand, MobX, Jotai, Recoil, and React Context. Helps choose the right solution and i... |
| **`storybook-guide`** | [`storybook-guide/`](./storybook-guide) | Discover existing components, inspect story definitions, and compose UI using verified Storybook design system primitives via MCP. |
| **`storyflow-workspace`** | [`storyflow-workspace/`](./storyflow-workspace) | Manage visual project workspaces, agile Kanban boards, user stories, mind maps, and workflow automation on an infinite canvas via Storyflow MCP. |
| **`streamer-bait-design`** | [`streamer-bait-design/`](./streamer-bait-design) | Design games optimized for streaming and content creation. Master proximity voice chat, asymmetric information, content moments, social deduction, and the bu... |
| **`stripe-integration`** | [`stripe-integration/`](./stripe-integration) | Get paid from day one. Payments, subscriptions, billing portal, webhooks, metered billing, Stripe Connect. The complete guide to implementing Stripe correctl... |
| **`svelte-kit`** | [`svelte-kit/`](./svelte-kit) | Svelte compiles your components to vanilla JavaScript at build time. No virtual DOM, no runtime framework. The result is smaller bundles, faster performance,... |
| **`system-designer`** | [`system-designer/`](./system-designer) | Software architecture and system design - scalability patterns, reliability engineering, and the art of making technical trade-offs that survive productionUs... |
| **`tabletop-rpg-design`** | [`tabletop-rpg-design/`](./tabletop-rpg-design) | Expert system designer for tabletop roleplaying games covering dice mechanics, character creation, combat systems, narrative frameworks, GM tools, and playte... |
| **`tailwind-css`** | [`tailwind-css/`](./tailwind-css) | Tailwind CSS changed how we write styles. Instead of naming things and writing CSS, you compose utility classes directly in your HTML. It sounds messy until ... |
| **`tailwind-ui`** | [`tailwind-ui/`](./tailwind-ui) | Expert knowledge for Tailwind CSS styling and component patternsUse when "tailwind, tailwindcss, utility classes, responsive design, dark mode, styling, css ... |
| **`telegram-bot-builder`** | [`telegram-bot-builder/`](./telegram-bot-builder) | Expert in building Telegram bots that solve real problems - from simple automation to complex AI-powered bots. Covers bot architecture, the Telegram Bot API,... |
| **`telegram-mastery`** | [`telegram-mastery/`](./telegram-mastery) | Expert in building and managing Telegram communities. Covers group vs channel strategy, bot automation, anti-spam, and managing large groups. Understands Tel... |
| **`telegram-mini-app`** | [`telegram-mini-app/`](./telegram-mini-app) | Expert in building Telegram Mini Apps (TWA) - web apps that run inside Telegram with native-like experience. Covers the TON ecosystem, Telegram Web App API, ... |
| **`test-architect`** | [`test-architect/`](./test-architect) | Testing strategy specialist for test pyramid design, test isolation, property-based testing, and quality gatesUse when "testing, test strategy, unit test, in... |
| **`test-strategist`** | [`test-strategist/`](./test-strategist) | Testing strategy and design - what to test, how to test, and when testing is overkill. From TDD to integration tests to knowing when to skip tests entirelyUs... |
| **`texture-art`** | [`texture-art/`](./texture-art) | Expert texture artist specializing in PBR workflows, Substance suite, Quixel Mixer, and hand-painted techniques for games and film productionUse when "textur... |
| **`thought-leadership`** | [`thought-leadership/`](./thought-leadership) | Expert in building thought leadership - establishing individuals or companies as authoritative voices in their industry. Covers positioning, content strategy... |
| **`threejs-3d-graphics`** | [`threejs-3d-graphics/`](./threejs-3d-graphics) | Senior graphics programmer specializing in Three.js, WebGL, shaders, and performance optimizationUse when "three.js, threejs, webgl, 3d web, 3d graphics, sha... |
| **`token-launch`** | [`token-launch/`](./token-launch) | Comprehensive expertise in launching tokens through IDOs, implementing secure vesting contracts, designing sustainable tokenomics, and ensuring fair launch m... |
| **`tokenomics-design`** | [`tokenomics-design/`](./tokenomics-design) | Expert in token economics - distribution models, vesting schedules, incentive mechanisms, emission curves, and sustainable protocol designUse when "tokenomic... |
| **`trigger-dev`** | [`trigger-dev/`](./trigger-dev) | Trigger.dev expert for background jobs, AI workflows, and reliable async execution with excellent developer experience and TypeScript-first design. Use when ... |
| **`twilio-communications`** | [`twilio-communications/`](./twilio-communications) | Build communication features with Twilio: SMS messaging, voice calls, WhatsApp Business API, and user verification (2FA). Covers the full spectrum from simpl... |
| **`typography`** | [`typography/`](./typography) | The art and science of arranging type to make written language legible, readable, and visually appealing. Typography is the invisible art - when done well, r... |
| **`ui-design`** | [`ui-design/`](./ui-design) | World-class UI design expertise combining the precision of Jony Ive's Apple work, the systems thinking of Figma's design philosophy, and the accessibility ob... |
| **`unity-development`** | [`unity-development/`](./unity-development) | Building games and interactive experiences with Unity engine, C#, MonoBehaviours, and modern Unity patternsUse when "unity, unity3d, unity game, unity develo... |
| **`unreal-engine`** | [`unreal-engine/`](./unreal-engine) | Building AAA-quality games and real-time experiences with Unreal Engine 5Use when "unreal, ue5, ue4, unreal engine, blueprints, blueprint, actor component, g... |
| **`ux-design`** | [`ux-design/`](./ux-design) | World-class UX design expertise combining Don Norman's human-centered principles, IDEO's design thinking methodology, and the product intuition developed fro... |
| **`ux-ui`** | [`ux-ui/`](./ux-ui) | UX/UI design principles for clean, intuitive interfaces. Use when designing layouts, improving usability, planning information architecture, or ensuring acce... |
| **`vehicle-design`** | [`vehicle-design/`](./vehicle-design) | Expert vehicle designer combining industrial design rigor with entertainment artistry. This skill embodies the methodologies of Scott Robertson's "How to Dra... |
| **`viral-generator-builder`** | [`viral-generator-builder/`](./viral-generator-builder) | Expert in building shareable generator tools that go viral - name generators, quiz makers, avatar creators, personality tests, and calculator tools. Covers t... |
| **`viral-marketing`** | [`viral-marketing/`](./viral-marketing) | The art and science of engineering word-of-mouth growth. Viral marketing isn't about luck—it's about deeply understanding why people share and building mecha... |
| **`voxel-art`** | [`voxel-art/`](./voxel-art) | Expert voxel artist with deep knowledge of MagicaVoxel workflows, palette design, animation techniques, mesh conversion, and game engine optimization. This s... |
| **`vr-ar-development`** | [`vr-ar-development/`](./vr-ar-development) | Expertise in building immersive VR/AR experiences using WebXR and spatial computing principlesUse when "vr development, ar development, webxr, virtual realit... |
| **`vue-nuxt`** | [`vue-nuxt/`](./vue-nuxt) | Vue is the progressive JavaScript framework - adopt as much or as little as you need. From sprinkles of reactivity on static pages to full single-page apps, ... |
| **`wallet-integration`** | [`wallet-integration/`](./wallet-integration) | Expert in Web3 wallet integration for DApps. Masters wallet connectivity, transaction signing, account management, and blockchain UX patterns. Use when "wall... |
| **`weapon-design`** | [`weapon-design/`](./weapon-design) | World-class weapon design expertise combining the silhouette mastery of FromSoftware, the functional beauty of WETA Workshop, the rarity language of Bungie's... |
| **`web-design`** | [`web-design/`](./web-design) | Web graphic design for interfaces, layouts, and visual systems. Use when designing landing pages, dashboards, hero sections, or applying design aesthetics (B... |
| **`web-vitals-profiler`** | [`web-vitals-profiler/`](./web-vitals-profiler) | Use this skill when diagnosing Core Web Vitals (LCP, INP, CLS), auditing performance waterfalls, detecting layout thrashing, or analyzing memory leaks. |
| **`web3-community`** | [`web3-community/`](./web3-community) | Expert in building crypto-native communities - token holder communities, NFT communities, DAO governance, alpha groups, and navigating the unique dynamics of... |
| **`websocket-realtime`** | [`websocket-realtime/`](./websocket-realtime) | Expert guidance on real-time communication patterns including WebSockets, Server-Sent Events (SSE), Socket.IO, and WebRTC. Covers connection management, reco... |
| **`websockets-realtime`** | [`websockets-realtime/`](./websockets-realtime) | Expert at building real-time features using WebSockets, Server-Sent Events, and other live update mechanisms. Covers connection management, reconnection stra... |
| **`worldbuilding`** | [`worldbuilding/`](./worldbuilding) | World architect specializing in fictional history, magic systems, and lore consistencyUse when "worldbuilding, world lore, fictional world, create a world, f... |
| **`x402-payments`** | [`x402-payments/`](./x402-payments) | Expert in HTTP 402 Payment Required protocol implementation - crypto micropayments, Lightning Network integration, L2 payment channels, and the future of web... |
| **`zapier-make-patterns`** | [`zapier-make-patterns/`](./zapier-make-patterns) | No-code automation democratizes workflow building. Zapier and Make (formerly Integromat) let non-developers automate business processes without writing code.... |

<br/>

## ⚙️ Backend, APIs & Distributed Systems

> *15 specialized runbooks available in this domain.*

| Skill Identifier | Runbook Path | Core Capabilities & Description |
| :--- | :--- | :--- |
| **`ai-image-editing`** | [`ai-image-editing/`](./ai-image-editing) | Expert patterns for AI-powered image editing including inpainting, outpainting, ControlNet, image-to-image, and API integration with Replicate, Stability AI,... |
| **`ai-visual-effects`** | [`ai-visual-effects/`](./ai-visual-effects) | The enhancement layer for AI-generated content. This skill covers AI-powered visual effects, compositing, upscaling, restoration, and post-production magic—t... |
| **`automation-ai-tools`** | [`automation/`](./automation) | Master the AI tools that automate repetitive work and connect your tools. From simple Zapier integrations to complex AI-powered workflows, reclaim hours ever... |
| **`docs-engineer`** | [`docs-engineer/`](./docs-engineer) | Technical documentation specialist for API docs, tutorials, architecture docs, and developer experienceUse when "documentation, docs, readme, tutorial, api d... |
| **`documentation-that-slaps`** | [`documentation-that-slaps/`](./documentation-that-slaps) | Expert in writing documentation that developers actually read. Covers README craft, API docs, tutorials, and internal docs. Understands that docs are a produ... |
| **`fintech-integration`** | [`fintech-integration/`](./fintech-integration) | Use when integrating Plaid, Stripe, payment processors, or financial APIs - covers account linking, payment processing, KYC/AML compliance, and webhook handl... |
| **`founder-character`** | [`founder-character/`](./founder-character) | What makes founders succeed? Paul Graham has observed thousands of founders and distilled patterns. Relentlessly resourceful. Fierce nerds. Earnest. These tr... |
| **`nextjs-app-router`** | [`nextjs-app-router/`](./nextjs-app-router) | Expert knowledge for Next.js 13+ App Router architectureUse when "next.js app router, server component, client component, use client, use server, server acti... |
| **`pyright-lsp`** | [`pyright-lsp/`](./pyright-lsp) | Pyright static type checker and language server for Python projects in Google Antigravity. |
| **`python-backend`** | [`python-backend/`](./python-backend) | Python dominates backend development for good reason - readable code, massive ecosystem, and frameworks that scale from prototype to production. Django gives... |
| **`rate-limiting`** | [`rate-limiting/`](./rate-limiting) | Patterns for implementing rate limiting to protect APIs from abuse, ensure fair usage, and maintain system stability. Covers token bucket, sliding window, di... |
| **`risk-management-trading`** | [`risk-management-trading/`](./risk-management-trading) | Master of capital preservation and position sizing - combining Kelly Criterion, volatility targeting, correlation analysis, and drawdown management to surviv... |
| **`shopify-apps`** | [`shopify-apps/`](./shopify-apps) | Expert patterns for Shopify app development including Remix/React Router apps, embedded apps with App Bridge, webhook handling, GraphQL Admin API, Polaris co... |
| **`text-to-video`** | [`text-to-video/`](./text-to-video) | Expert patterns for AI video generation including text-to-video, image-to-video, video editing, and API integration with Runway, Kling, Luma, Wan, and Replic... |
| **`typescript-lsp`** | [`typescript-lsp/`](./typescript-lsp) | TypeScript and JavaScript language server for Node.js, React, and web projects in Google Antigravity. |

<br/>

## 🗄️ Database Engineering, ORM & Caching

> *50 specialized runbooks available in this domain.*

| Skill Identifier | Runbook Path | Core Capabilities & Description |
| :--- | :--- | :--- |
| **`ai-ad-creative`** | [`ai-ad-creative/`](./ai-ad-creative) | The intersection of AI generation and performance marketing. This skill covers creating ad creatives at scale using AI tools—from static images to video ads ... |
| **`ai-content-analytics`** | [`ai-content-analytics/`](./ai-content-analytics) | World-class expertise in measuring, attributing, and optimizing AI-generated content performance. Combining data science rigor with content strategy intellig... |
| **`algolia-search`** | [`algolia-search/`](./algolia-search) | Expert patterns for Algolia search implementation, indexing strategies, React InstantSearch, and relevance tuningUse when "adding search to, algolia, instant... |
| **`angular`** | [`angular/`](./angular) | Angular is opinionated and comprehensive - it gives you everything: routing, forms, HTTP, dependency injection, testing. The learning curve is steep, but onc... |
| **`brave-search`** | [`brave-search/`](./brave-search) | Perform live, privacy-respecting web and local news searches using the independent Brave Search API. |
| **`caching-patterns`** | [`caching-patterns/`](./caching-patterns) | World-class caching strategies - cache invalidation, Redis patterns, CDN caching, and the battle scars from cache bugs that served stale data for hoursUse wh... |
| **`codebase-optimization`** | [`codebase-optimization/`](./codebase-optimization) | Keeping codebases healthy, performant, and maintainable - refactoring, performance optimization, and technical debt managementUse when "refactor, optimize, p... |
| **`community-tooling`** | [`community-tooling/`](./community-tooling) | Expert in community tool selection and implementation - Discord bots, community platforms, analytics tools, CRMs, moderation systems, and automation. Knows t... |
| **`competitive-intelligence`** | [`competitive-intelligence/`](./competitive-intelligence) | Expert in competitive intelligence - systematic gathering, analysis, and application of information about competitors. Covers competitive research, win/loss ... |
| **`creative-strategy`** | [`creative-strategy/`](./creative-strategy) | World-class creative strategy expertise combining the conceptual brilliance of agencies like Wieden+Kennedy, the data-informed creativity of modern brands, a... |
| **`cross-chain`** | [`cross-chain/`](./cross-chain) | Comprehensive expertise in cross-chain infrastructure, including LayerZero, Wormhole, Axelar, and custom bridge implementations. Covers omnichain token stand... |
| **`cultural-remix`** | [`cultural-remix/`](./cultural-remix) | Expert in identifying, adapting, and participating in cultural moments and trends. Covers trend identification, format adaptation, moment jacking, and knowin... |
| **`database-migrations`** | [`database-migrations/`](./database-migrations) | Expert at evolving database schemas safely. Covers migration strategies, zero-downtime deployments, rollback planning, and data transformation. Knows how to ... |
| **`drizzle-orm`** | [`drizzle-orm/`](./drizzle-orm) | Expert knowledge for Drizzle ORM - the lightweight, type-safe SQL ORM for edge and serverlessUse when "drizzle, drizzle orm, drizzle-kit, drizzle schema, dri... |
| **`drug-discovery-informatics`** | [`drug-discovery-informatics/`](./drug-discovery-informatics) | Patterns for computer-aided drug discovery including virtual screening, molecular docking, ADMET prediction, lead optimization, and integration with AI/ML me... |
| **`education-platforms`** | [`education-platforms/`](./education-platforms) | Expert in course platform selection and implementation - comparing Teachable, Kajabi, Thinkific, and custom solutions. Covers LMS selection criteria, platfor... |
| **`finance-ai-tools`** | [`finance/`](./finance) | Master the AI tools that transform financial operations. From bookkeeping to forecasting, manage money smarter and make data-driven financial decisions. Use ... |
| **`graph-engineer`** | [`graph-engineer/`](./graph-engineer) | Knowledge graph specialist for entity and causal relationship modelingUse when "knowledge graph, graph database, falkordb, neo4j, cypher query, entity resolu... |
| **`graphile-worker`** | [`graphile-worker/`](./graphile-worker) | Graphile Worker expert for high-performance PostgreSQL job queues with trigger-based job creation and millisecond job pickup via LISTEN/NOTIFY. Use when "gra... |
| **`graphql`** | [`graphql/`](./graphql) | GraphQL gives clients exactly the data they need - no more, no less. One endpoint, typed schema, introspection. But the flexibility that makes it powerful al... |
| **`infra-architect`** | [`infra-architect/`](./infra-architect) | Infrastructure and platform specialist for Kubernetes, Terraform, GitOps, and cloud-native architectureUse when "kubernetes, k8s, terraform, infrastructure, ... |
| **`infrastructure-as-code`** | [`infrastructure-as-code/`](./infrastructure-as-code) | World-class infrastructure automation - Terraform, Pulumi, CloudFormation, and the battle scars from managing infrastructure that handles production trafficU... |
| **`mcp-deployment`** | [`mcp-deployment/`](./mcp-deployment) | Production deployment patterns for MCP servers including Docker, cloud platforms, monitoring, and scalabilityUse when "mcp deployment, deploy mcp server, mcp... |
| **`mcp-testing`** | [`mcp-testing/`](./mcp-testing) | Testing strategies for MCP servers including unit tests, integration tests, schema validation, and security testingUse when "mcp testing, test mcp server, mc... |
| **`meme-engineering`** | [`meme-engineering/`](./meme-engineering) | Expert in meme creation and virality - understanding why certain ideas spread while others die. Covers meme formats, timing, adaptation, meta-commentary, and... |
| **`migration-specialist`** | [`migration-specialist/`](./migration-specialist) | Migration specialist for zero-downtime schema changes, data migrations, and backward-compatible evolutionUse when "migration, schema change, database migrati... |
| **`neon-postgres`** | [`neon-postgres/`](./neon-postgres) | Expert patterns for Neon serverless Postgres, branching, connection pooling, and Prisma/Drizzle integrationUse when "neon database, serverless postgres, data... |
| **`nextjs-supabase-auth`** | [`nextjs-supabase-auth/`](./nextjs-supabase-auth) | Expert integration of Supabase Auth with Next.js App RouterUse when "supabase auth next, authentication next.js, login supabase, auth middleware, protected r... |
| **`nlp-advanced`** | [`nlp-advanced/`](./nlp-advanced) | Use when extracting structured information from text - named entity recognition, relation extraction, coreference resolution, knowledge graph construction, a... |
| **`onchain-analytics`** | [`onchain-analytics/`](./onchain-analytics) | Comprehensive expertise in blockchain data analysis using Dune Analytics, custom indexers, and on-chain data querying. Covers SQL for blockchain, dashboard c... |
| **`performance-hunter`** | [`performance-hunter/`](./performance-hunter) | Performance optimization specialist for profiling, caching, and latency optimizationUse when "performance, latency, slow query, profiling, caching, optimizat... |
| **`performance-optimization`** | [`performance-optimization/`](./performance-optimization) | Expert at diagnosing and fixing performance bottlenecks across the stack. Covers Core Web Vitals, database optimization, caching strategies, bundle optimizat... |
| **`performance-thinker`** | [`performance-thinker/`](./performance-thinker) | Performance optimization mindset - knowing when to optimize, how to measure, where bottlenecks hide, and when "fast enough" is the right answerUse when "slow... |
| **`pg-boss`** | [`pg-boss/`](./pg-boss) | pg-boss expert for PostgreSQL-backed job queues with exactly-once delivery, perfect for applications already using Postgres (Supabase, Neon, etc.). Use when ... |
| **`postgres-wizard`** | [`postgres-wizard/`](./postgres-wizard) | PostgreSQL internals specialist for query optimization, indexing, partitioning, and advanced featuresUse when "postgresql, postgres, slow query, index, expla... |
| **`prediction-markets`** | [`prediction-markets/`](./prediction-markets) | Comprehensive expertise in decentralized prediction markets, including Polymarket-style platforms, UMA Optimistic Oracle integration, Conditional Tokens Fram... |
| **`react-native-specialist`** | [`react-native-specialist/`](./react-native-specialist) | Cross-platform mobile development specialist for React Native, Expo, native modules, and mobile-specific patternsUse when "react native, expo, mobile app, io... |
| **`redis-specialist`** | [`redis-specialist/`](./redis-specialist) | Redis expert for caching, pub/sub, data structures, and distributed systems patternsUse when "redis, caching strategy, cache invalidation, pub/sub, rate limi... |
| **`regex-whisperer`** | [`regex-whisperer/`](./regex-whisperer) | Expert in writing, debugging, and explaining regular expressions. Covers readable regex patterns, performance optimization, debugging techniques, and knowing... |
| **`research-ai-tools`** | [`research/`](./research) | Master the AI tools that accelerate research and information gathering. From market research to academic analysis, find insights faster and make better decis... |
| **`rust-craftsman`** | [`rust-craftsman/`](./rust-craftsman) | Systems programming specialist for Rust, ownership model, memory safety, concurrency, and performance optimizationUse when "rust, cargo, ownership, borrowing... |
| **`salesforce-development`** | [`salesforce-development/`](./salesforce-development) | Expert patterns for Salesforce platform development including Lightning Web Components (LWC), Apex triggers and classes, REST/Bulk APIs, Connected Apps, and ... |
| **`scientific-method`** | [`scientific-method/`](./scientific-method) | The scientific method applied to computational research, data science, and experimental software engineering. Covers hypothesis formulation, experimental des... |
| **`segment-cdp`** | [`segment-cdp/`](./segment-cdp) | Expert patterns for Segment Customer Data Platform including Analytics.js, server-side tracking, tracking plans with Protocols, identity resolution, destinat... |
| **`sentiment-analysis-trading`** | [`sentiment-analysis-trading/`](./sentiment-analysis-trading) | World-class alternative data and sentiment analysis for trading - social media, news, on-chain data, positioning. Extract alpha from information others miss.... |
| **`solana-development`** | [`solana-development/`](./solana-development) | Expert in Solana blockchain development - Anchor framework, SPL tokens, program development, and high-performance dApp architectureUse when "solana, anchor f... |
| **`supabase-expert`** | [`supabase-expert/`](./supabase-expert) | Manage Supabase cloud projects, author safe Postgres schema migrations, configure Row Level Security (RLS) policies, and deploy edge functions. |
| **`sustainability-metrics`** | [`sustainability-metrics/`](./sustainability-metrics) | ESG performance measurement, sustainability reporting frameworks, materiality assessment, and impact quantification. Covers CDP, TCFD, GRI, SASB, CSRD/ESRS, ... |
| **`sveltekit`** | [`sveltekit/`](./sveltekit) | Expert knowledge for SvelteKit full-stack web applications with SSR, form actions, and Svelte 5 runesUse when "sveltekit, svelte kit, svelte 5, svelte5, rune... |
| **`viral-hooks`** | [`viral-hooks/`](./viral-hooks) | Expert in creating opening lines, thumbnails, and hooks that stop the scroll. Covers curiosity gaps, pattern interrupts, emotional triggers, and platform-spe... |

<br/>

## 🛡️ Security, SAST, Auth & Vulnerability Auditing

> *17 specialized runbooks available in this domain.*

| Skill Identifier | Runbook Path | Core Capabilities & Description |
| :--- | :--- | :--- |
| **`anti-marketing`** | [`anti-marketing/`](./anti-marketing) | Expert in brutally honest, self-deprecating marketing that converts. Covers transparent messaging, vulnerability as strategy, "we're not for everyone" positi... |
| **`art-consistency`** | [`art-consistency/`](./art-consistency) | World-class character and art style consistency for AI-generated images and videos - ensures visual coherence across series, maintains character identity, an... |
| **`auth-specialist`** | [`auth-specialist/`](./auth-specialist) | Authentication and authorization expert for OAuth, sessions, JWT, MFA, and identity securityUse when "authentication flow, login system, oauth integration, j... |
| **`branding`** | [`branding/`](./branding) | The craft of creating and maintaining cohesive brand identity systems. Branding translates brand strategy into tangible visual and verbal identity—logos, col... |
| **`clerk-auth`** | [`clerk-auth/`](./clerk-auth) | Expert patterns for Clerk auth implementation, middleware, organizations, webhooks, and user syncUse when "adding authentication, clerk auth, user authentica... |
| **`cybersecurity`** | [`cybersecurity/`](./cybersecurity) | Security engineering that protects applications, data, and users from real-world threatsUse when "security, authentication, authorization, encryption, OWASP,... |
| **`game-networking`** | [`game-networking/`](./game-networking) | Expertise in real-time multiplayer networking, lag compensation, and authoritative server architectureUse when "multiplayer game, netcode, client-server game... |
| **`hubspot-integration`** | [`hubspot-integration/`](./hubspot-integration) | Expert patterns for HubSpot CRM integration including OAuth authentication, CRM objects, associations, batch operations, webhooks, and custom objects. Covers... |
| **`mcp-security`** | [`mcp-security/`](./mcp-security) | Security patterns for MCP servers including OAuth 2.0, rate limiting, input validation, and audit loggingUse when "mcp security, mcp authentication, mcp oaut... |
| **`plaid-fintech`** | [`plaid-fintech/`](./plaid-fintech) | Expert patterns for Plaid API integration including Link token flows, transactions sync, identity verification, Auth for ACH, balance checks, webhook handlin... |
| **`privacy-guardian`** | [`privacy-guardian/`](./privacy-guardian) | Security and privacy specialist for differential privacy, encryption, and complianceUse when "privacy, encryption, differential privacy, PII, GDPR, CCPA, acc... |
| **`security`** | [`security/`](./security) | One breach = game over. Threat modeling, OWASP Top 10, secure coding, security architecture, zero trust. The complete security skill for protecting your appl... |
| **`security-hardening`** | [`security-hardening/`](./security-hardening) | World-class application security - OWASP Top 10, secure coding patterns, and the battle scars from security incidents that could have been preventedUse when ... |
| **`security-owasp`** | [`security-owasp/`](./security-owasp) | Expert at securing web applications against OWASP Top 10 vulnerabilities. Covers authentication, authorization, input validation, XSS prevention, CSRF protec... |
| **`smart-contract-auditor`** | [`smart-contract-auditor/`](./smart-contract-auditor) | Elite security researcher who hunts vulnerabilities in smart contracts. Has found critical bugs worth millions in TVL. Specializes in reentrancy, access cont... |
| **`smart-contract-engineer`** | [`smart-contract-engineer/`](./smart-contract-engineer) | Blockchain smart contract specialist for Solidity, EVM, security patterns, and gas optimizationUse when "smart contract, solidity, ethereum, evm, contract, w... |
| **`sox-compliance`** | [`sox-compliance/`](./sox-compliance) | Use when implementing Sarbanes-Oxley compliance, internal controls, audit trails, segregation of duties, or continuous monitoring - covers COSO framework and... |

<br/>

## 🧪 Testing, QA Automation & Performance Engineering

> *9 specialized runbooks available in this domain.*

| Skill Identifier | Runbook Path | Core Capabilities & Description |
| :--- | :--- | :--- |
| **`ai-content-qa`** | [`ai-content-qa/`](./ai-content-qa) | The systematic discipline of reviewing AI-generated and human-written marketing content for quality, accuracy, consistency, and effectiveness. This isn't pro... |
| **`browser-debugger`** | [`browser-debugger/`](./browser-debugger) | Use this skill when inspecting live browser console logs, debugging JavaScript runtime errors, examining network payload failures, or tracing DOM mutations. |
| **`debugging-master`** | [`debugging-master/`](./debugging-master) | Systematic debugging methodology - scientific method, hypothesis testing, and root cause analysis that works across all technologiesUse when "bug, debugging,... |
| **`execution-algorithms`** | [`execution-algorithms/`](./execution-algorithms) | World-class trade execution - minimize market impact, optimize order routing, reduce slippage. The difference between backtest and live is usually execution.... |
| **`qa-engineering`** | [`qa-engineering/`](./qa-engineering) | World-class QA engineering - systematic testing, automation, and the mindset that finds bugs before users doUse when "QA, quality assurance, testing, test au... |
| **`selenium-automation`** | [`selenium-automation/`](./selenium-automation) | Cross-browser testing and web automation using Selenium WebDriver via MCP (start browser, navigate, find element, click, type, screenshot). |
| **`statistical-analysis`** | [`statistical-analysis/`](./statistical-analysis) | Comprehensive statistical analysis for research, experiments, and data science. Covers hypothesis testing, effect sizes, confidence intervals, Bayesian metho... |
| **`student-success`** | [`student-success/`](./student-success) | Expert in measuring and driving student outcomes - completion optimization, outcome tracking, testimonial systems, certifications, and alumni programs. Cover... |
| **`testing-automation`** | [`testing-automation/`](./testing-automation) | World-class test automation - unit, integration, e2e testing strategies, and the battle scars from flaky tests that broke CI/CD pipelinesUse when "test, test... |

<br/>

## ☁️ DevOps, Cloud Infrastructure, Docker & CI/CD

> *13 specialized runbooks available in this domain.*

| Skill Identifier | Runbook Path | Core Capabilities & Description |
| :--- | :--- | :--- |
| **`azure-functions`** | [`azure-functions/`](./azure-functions) | Expert patterns for Azure Functions development including isolated worker model, Durable Functions orchestration, cold start optimization, and production pat... |
| **`ci-cd-pipeline`** | [`ci-cd-pipeline/`](./ci-cd-pipeline) | World-class continuous integration and deployment - GitHub Actions, GitLab CI, deployment strategies, and the battle scars from pipelines that broke producti... |
| **`cicd-pipelines`** | [`cicd-pipelines/`](./cicd-pipelines) | CI/CD is the backbone of modern software delivery. Continuous Integration catches bugs early. Continuous Deployment gets features to users fast. But poorly d... |
| **`compose-architect`** | [`compose-architect/`](./compose-architect) | Use this skill when configuring Docker Compose stacks, setting up multi-service local environments, managing service dependencies, and container networking. |
| **`devops`** | [`devops/`](./devops) | World-class DevOps engineering - cloud architecture, CI/CD pipelines, infrastructure as code, and the battle scars from keeping production running at 3amUse ... |
| **`docker`** | [`docker/`](./docker) | Docker makes "works on my machine" a deployment strategy. Package your app with its dependencies, run it anywhere. But Docker's simplicity hides real complex... |
| **`docker-specialist`** | [`docker-specialist/`](./docker-specialist) | Container specialist for Docker, Docker Compose, image optimization, and container orchestration fundamentalsUse when "docker, dockerfile, container, docker-... |
| **`go-services`** | [`go-services/`](./go-services) | Go is the language of infrastructure. From Docker to Kubernetes to the entire cloud-native ecosystem, Go powers the systems that run the internet. It's not a... |
| **`inngest`** | [`inngest/`](./inngest) | Inngest expert for serverless-first background jobs, event-driven workflows, and durable execution without managing queues or workers. Use when "inngest, ser... |
| **`kubernetes-deployment`** | [`kubernetes-deployment/`](./kubernetes-deployment) | World-class Kubernetes operations - deployments, debugging, Helm charts, and the battle scars from managing clusters that serve millions of requestsUse when ... |
| **`real-time-content`** | [`real-time-content/`](./real-time-content) | The speed layer of AI-native marketing. This skill covers creating and deploying content in real-time—responding to trends, events, and moments as they happe... |
| **`upstash-qstash`** | [`upstash-qstash/`](./upstash-qstash) | Upstash QStash expert for serverless message queues, scheduled jobs, and reliable HTTP-based task delivery without managing infrastructure. Use when "qstash,... |
| **`vercel-deployment`** | [`vercel-deployment/`](./vercel-deployment) | Expert knowledge for deploying to Vercel with Next.jsUse when "vercel, deploy, deployment, hosting, production, environment variables, edge function, serverl... |

<br/>

## 📱 Mobile, Cross-Platform & Desktop Development

> *2 specialized runbooks available in this domain.*

| Skill Identifier | Runbook Path | Core Capabilities & Description |
| :--- | :--- | :--- |
| **`export-control`** | [`export-control/`](./export-control) | Use when implementing ITAR/EAR compliance, ECCN classification, party screening, technology control plans, or deemed exports - covers US export control regul... |
| **`portfolio-optimization`** | [`portfolio-optimization/`](./portfolio-optimization) | Use when constructing portfolios, implementing mean-variance optimization, factor models, risk parity, or Black-Litterman allocation - covers modern portfoli... |

<br/>

## 📊 Data Science, Analytics, Big Data & Modeling

> *12 specialized runbooks available in this domain.*

| Skill Identifier | Runbook Path | Core Capabilities & Description |
| :--- | :--- | :--- |
| **`analytics`** | [`analytics/`](./analytics) | The practice of collecting, analyzing, and acting on data to drive product decisions. Great analytics isn't about dashboards—it's about insights that lead to... |
| **`burn-rate-management`** | [`burn-rate-management/`](./burn-rate-management) | Don't die. Runway calculation, default alive vs. default dead, when to raise vs. cut, zero-based budgeting for startups. The math that keeps companies alive ... |
| **`climate-modeling`** | [`climate-modeling/`](./climate-modeling) | Work with climate data, models, and projections for climate impact assessment, downscaling, and scenario analysis using CMIP6 and other climate datasets. Use... |
| **`community-analytics`** | [`community-analytics/`](./community-analytics) | Expert in measuring what matters in communities. Covers health metrics, engagement analytics, sentiment analysis, cohort tracking, and reporting. Knows that ... |
| **`content-strategy`** | [`content-strategy/`](./content-strategy) | World-class content strategy expertise combining the frameworks of Andy Crestodina's data-driven approach, Ann Handley's "everybody writes" philosophy, and t... |
| **`data-reproducibility`** | [`data-reproducibility/`](./data-reproducibility) | Infrastructure and practices for reproducible computational research. Covers environment management, data versioning, code documentation, and sharing protoco... |
| **`founder-operating-system`** | [`founder-operating-system/`](./founder-operating-system) | Founders face unique challenges in how they work. Maker vs manager schedule conflicts. Default alive vs dead math. Time and money slowly leaking away. Effect... |
| **`gdpr-privacy`** | [`gdpr-privacy/`](./gdpr-privacy) | Use when implementing GDPR compliance, handling data subject requests, conducting DPIAs, managing consent, or responding to data breaches - covers all key GD... |
| **`marketing`** | [`marketing/`](./marketing) | World-class marketing expertise combining Seth Godin's permission marketing philosophy, Neil Patel's data-driven growth tactics, and the strategic frameworks... |
| **`nft-systems`** | [`nft-systems/`](./nft-systems) | Expert in NFT development - minting infrastructure, metadata standards, marketplaces, royalties, and collection management across EVM and SolanaUse when "nft... |
| **`protein-structure`** | [`protein-structure/`](./protein-structure) | Patterns for protein structure prediction using AlphaFold2/ColabFold, structural analysis, model quality assessment, and integration with experimental data. ... |
| **`sensor-fusion`** | [`sensor-fusion/`](./sensor-fusion) | Patterns for multi-sensor data fusion including Kalman filters (KF, EKF, UKF), complementary filters, particle filters, and factor graph optimization. Covers... |

<br/>

## ✍️ Product, Growth, Media, Copywriting & Docs

> *39 specialized runbooks available in this domain.*

| Skill Identifier | Runbook Path | Core Capabilities & Description |
| :--- | :--- | :--- |
| **`absurdist-voice`** | [`absurdist-voice/`](./absurdist-voice) | Expert in absurdist, unhinged, and deliberately weird brand voices that work. Covers the Duolingo owl energy, chaotic social media presence, and knowing exac... |
| **`account-abstraction`** | [`account-abstraction/`](./account-abstraction) | Comprehensive expertise in ERC-4337 account abstraction, smart contract wallets, paymasters, bundlers, and user operation handling. Covers social recovery, s... |
| **`ad-copywriting`** | [`ad-copywriting/`](./ad-copywriting) | The specialized craft of writing copy that sells—headlines that stop thumbs, body copy that persuades, CTAs that convert. This is copywriting specifically tu... |
| **`ai-audio-production`** | [`ai-audio-production/`](./ai-audio-production) | The new frontier of audio: AI-generated music with Suno and Udio, AI sound effects with ElevenLabs, AI voice cloning, and AI audio enhancement. This skill co... |
| **`ai-creative-director`** | [`ai-creative-director/`](./ai-creative-director) | The orchestration layer for AI-native creative production. This skill coordinates multiple AI tools—video, image, audio, digital humans, effects—into cohesiv... |
| **`ai-for-learning`** | [`ai-for-learning/`](./ai-for-learning) | Expert in applying AI to education - AI tutors, personalized learning paths, content generation, automated assessments, and adaptive learning systems. Covers... |
| **`ai-localization`** | [`ai-localization/`](./ai-localization) | Global content at the speed of AI. This skill covers the full spectrum of AI-powered localization: translation, cultural adaptation, voice localization, visu... |
| **`ai-music-audio`** | [`ai-music-audio/`](./ai-music-audio) | Comprehensive patterns for AI-powered audio generation including text-to-music, voice synthesis, text-to-speech, sound effects, and audio manipulation using ... |
| **`ai-trend-alchemy`** | [`ai-trend-alchemy/`](./ai-trend-alchemy) | The fusion of trend prediction and AI content generation: detecting emerging trends before they peak and generating content that rides—or creates—the wave. T... |
| **`ai-video-generation`** | [`ai-video-generation/`](./ai-video-generation) | Mastery of the new frontier: AI-generated video that rivals—and reimagines—traditional production. This skill covers Veo3, Runway Gen-3, Sora, Kling, Pika, L... |
| **`ai-workflow-automation`** | [`ai-workflow-automation/`](./ai-workflow-automation) | The systematic orchestration of AI-powered marketing workflows that combine content generation, approval processes, multi-channel distribution, and quality g... |
| **`blog-writing`** | [`blog-writing/`](./blog-writing) | Legendary blog writing that makes readers forget they're reading. This skill combines the narrative mastery of Paul Graham's essays, the technical accessibil... |
| **`concept-art`** | [`concept-art/`](./concept-art) | Expert in entertainment industry concept art workflows, from initial ideation through final production-ready deliverables. Combines traditional art fundament... |
| **`content-creation-ai-tools`** | [`content-creation/`](./content-creation) | Master the AI tools that generate unlimited content at scale. From stunning images to professional videos, voiceovers to compelling copy - create content tha... |
| **`copywriting`** | [`copywriting/`](./copywriting) | World-class copywriting expertise combining the persuasive clarity of David Ogilvy, the conversational warmth of Ann Handley, and the conversion science of m... |
| **`cursor-ai`** | [`cursor-ai/`](./cursor-ai) | Expert in Cursor AI IDE - the leading AI-powered code editor. Covers Rules files for project-specific AI behavior, Plan Mode for structured development, Back... |
| **`decision-maker`** | [`decision-maker/`](./decision-maker) | Technical decision-making frameworks - trade-off evaluation, reversibility analysis, and second-order thinking for better engineering choicesUse when "should... |
| **`demoscene-coding`** | [`demoscene-coding/`](./demoscene-coding) | Specialist in creating size-optimized real-time audio-visual demos and procedural artUse when "demoscene, size coding, 64k intro, 4k intro, 1k intro, tiny co... |
| **`email-systems`** | [`email-systems/`](./email-systems) | Email has the highest ROI of any marketing channel. $36 for every $1 spent. Yet most startups treat it as an afterthought - bulk blasts, no personalization, ... |
| **`explainer-videos`** | [`explainer-videos/`](./explainer-videos) | World-class explainer video expertise combining the visual storytelling of Kurzgesagt, the simplification genius of Common Craft, and the conversion science ... |
| **`gamification-loops`** | [`gamification-loops/`](./gamification-loops) | Expert in gamification mechanics - points, badges, streaks, progress bars, and the psychology that makes them work. Covers variable reward systems, progress ... |
| **`generative-art`** | [`generative-art/`](./generative-art) | Creative technologist specializing in algorithmic art, shaders, and generative systemsUse when "generative art, creative coding, processing, p5.js, shader ar... |
| **`go-to-market`** | [`go-to-market/`](./go-to-market) | A great product that nobody knows about is a failed product. Go-to-market strategy is how you get your product into customers' hands. Not marketing in the ab... |
| **`godot-development`** | [`godot-development/`](./godot-development) | Expert Godot 4 game developer specializing in GDScript, the node/scene system, signals, resources, and engine-native patterns. Provides deep knowledge of God... |
| **`idea-maze`** | [`idea-maze/`](./idea-maze) | Most startup ideas are bad. Not because founders lack creativity, but because they're solving invented problems instead of lived ones.  Paul Graham's essays ... |
| **`marketing-fundamentals`** | [`marketing-fundamentals/`](./marketing-fundamentals) | Core marketing principles for startups. Covers positioning, messaging, channels, and growth. Focus on what works for resource-constrained teams.  Battle scar... |
| **`packaging-print-production`** | [`packaging-print-production/`](./packaging-print-production) | I am a veteran print production specialist with 15+ years in tabletop game manufacturing. I've shepherded hundreds of games from digital files to retail-read... |
| **`procedural-generation`** | [`procedural-generation/`](./procedural-generation) | Procedural Content Generation (PCG) is the art of creating infinite from finite. The challenge isn't making random content - it's making content that feels d... |
| **`productivity-ai-tools`** | [`productivity/`](./productivity) | Master the AI tools that handle administrative work and boost personal productivity. From meeting notes to email management, get more done with less effort. ... |
| **`shader-programming`** | [`shader-programming/`](./shader-programming) | Expert knowledge for GPU shader development across GLSL, HLSL, ShaderLab, and compute shadersUse when "write shader, shader code, GLSL, HLSL, ShaderLab, vert... |
| **`stakeholder-management`** | [`stakeholder-management/`](./stakeholder-management) | Your startup isn't just your team - it's an ecosystem of people who have a stake in your success. Investors, board members, advisors, partners, vendors. Each... |
| **`synthetic-influencers`** | [`synthetic-influencers/`](./synthetic-influencers) | The next evolution of influencer marketing: AI-generated personas that represent brands with perfect consistency, infinite availability, and zero scandal ris... |
| **`technical-debt-strategy`** | [`technical-debt-strategy/`](./technical-debt-strategy) | Technical debt is not bad. Reckless debt is bad. Strategic debt is a tool. Like financial debt, it can accelerate growth when used wisely or bankrupt you whe... |
| **`trading-psychology`** | [`trading-psychology/`](./trading-psychology) | World-class trading psychology - emotional control, cognitive biases, discipline, and journaling. The mental game separates consistent winners from everyone ... |
| **`vfx-realtime`** | [`vfx-realtime/`](./vfx-realtime) | Expert real-time VFX artist specializing in particle systems, shader effects, and the invisible craft that makes games feel satisfying. Masters Niagara, VFX ... |
| **`video-directing`** | [`video-directing/`](./video-directing) | World-class video directing mastery drawing from cinematic legends like Spielberg, Cameron, Coppola, and Nolan. This skill translates directorial intent into... |
| **`video-production`** | [`video-production/`](./video-production) | World-class video production expertise combining the storytelling craft of documentary filmmakers, the efficiency of commercial production houses, and the en... |
| **`video-scriptwriting`** | [`video-scriptwriting/`](./video-scriptwriting) | The craft of writing for the screen—from 6-second ads to 10-minute brand films. This skill bridges storytelling with the unique constraints and opportunities... |
| **`voiceover`** | [`voiceover/`](./voiceover) | World-class voiceover expertise combining the narrative craft of documentary producers, the commercial precision of advertising agencies, and the accessibili... |

<br/>

## 🛠️ Developer Productivity, Architecture & Workflow Automation

> *63 specialized runbooks available in this domain.*

| Skill Identifier | Runbook Path | Core Capabilities & Description |
| :--- | :--- | :--- |
| **`brand-positioning`** | [`brand-positioning/`](./brand-positioning) | World-class brand positioning expertise combining David Ogilvy's direct response wisdom, Emily Heyward's obsessive brand strategy (Red Antler), and Al Ries/J... |
| **`carbon-accounting`** | [`carbon-accounting/`](./carbon-accounting) | Calculate, track, and report greenhouse gas emissions following GHG Protocol standards, including Scope 1, 2, and 3 emissions and science-based targets. Use ... |
| **`clean-gone`** | [`clean-gone/`](./clean-gone) | Cleans up all git branches marked as [gone] (branches that have been deleted on the remote but still exist locally), including removing associated worktrees. |
| **`code-architecture-review`** | [`code-architecture-review/`](./code-architecture-review) | Review code architecture for maintainability, catch structural issues before they become debtUse when "Reviewing pull requests with structural changes, Plann... |
| **`commit`** | [`commit/`](./commit) | Create a git commit |
| **`commit-push-pr`** | [`commit-push-pr/`](./commit-push-pr) | Commit, push, and open a PR |
| **`community-operations`** | [`community-operations/`](./community-operations) | Expert in running the day-to-day operations of thriving communities. Covers moderation systems, onboarding flows, crisis management, scaling operations, and ... |
| **`control-systems`** | [`control-systems/`](./control-systems) | Patterns for feedback control systems including PID tuning, state-space control, Model Predictive Control (MPC), trajectory tracking, and stability analysis.... |
| **`creative-communications`** | [`creative-communications/`](./creative-communications) | The craft of producing creative assets that communicate brand, product, and message effectively. Creative communications bridges strategy and execution—trans... |
| **`crisis-communications`** | [`crisis-communications/`](./crisis-communications) | When things go wrong - and they will - how you communicate determines whether you lose customers for a day or lose trust forever. Crisis communications isn't... |
| **`dao-governance`** | [`dao-governance/`](./dao-governance) | Comprehensive expertise in decentralized autonomous organization governance systems, including Snapshot off-chain voting, OpenZeppelin Governor on-chain exec... |
| **`decision-frameworks`** | [`decision-frameworks/`](./decision-frameworks) | Expert in decision-making frameworks - systematic approaches to making better decisions under uncertainty. Covers decision criteria, reversibility assessment... |
| **`demo-day-theater`** | [`demo-day-theater/`](./demo-day-theater) | Expert in presenting technical work to non-technical audiences. Covers demo preparation, storytelling for demos, handling failures gracefully, and making wor... |
| **`development-ai-tools`** | [`development/`](./development) | Master the AI tools that supercharge software development. From code completion to full application generation, write better code faster and automate the ted... |
| **`digital-humans`** | [`digital-humans/`](./digital-humans) | The art and science of creating AI-powered digital presenters, avatars, and synthetic spokespersons. This skill covers HeyGen, Synthesia, D-ID, Tavus, and th... |
| **`distributed-training`** | [`distributed-training/`](./distributed-training) | Use when training models across multiple GPUs or nodes, handling large models that don't fit in memory, or optimizing training throughput - covers DDP, FSDP,... |
| **`embedded-systems`** | [`embedded-systems/`](./embedded-systems) | Patterns for embedded software development including real-time systems, memory management, hardware abstraction, interrupt handling, and debugging techniques... |
| **`event-architect`** | [`event-architect/`](./event-architect) | Event sourcing and CQRS expert for AI memory systemsUse when "event sourcing, event store, cqrs, nats jetstream, kafka events, event projection, replay event... |
| **`evm-deep-dive`** | [`evm-deep-dive/`](./evm-deep-dive) | Expert in Ethereum Virtual Machine internals - gas optimization, assembly/Yul, opcode-level optimization, and low-level EVM patternsUse when "evm, gas optimi... |
| **`firecrawl-scraper`** | [`firecrawl-scraper/`](./firecrawl-scraper) | Scrape single URLs, crawl entire domains, map sitemaps, and extract clean Markdown from the web using Firecrawl MCP. |
| **`game-monetization`** | [`game-monetization/`](./game-monetization) | Expertise in F2P economics, virtual currencies, and ethical monetization strategiesUse when "game monetization, F2P economy, in-app purchase, IAP strategy, b... |
| **`git-time-travel`** | [`git-time-travel/`](./git-time-travel) | Expert in navigating and manipulating git history. Covers finding bugs with bisect, understanding code evolution, recovering lost work, and rewriting history... |
| **`git-workflow`** | [`git-workflow/`](./git-workflow) | Git is deceptively simple to learn and incredibly hard to master. The difference between a team that ships and a team that fights merge conflicts all day com... |
| **`growth-strategy`** | [`growth-strategy/`](./growth-strategy) | World-class growth strategy expertise combining Andrew Chen's marketplace and network effects wisdom, Brian Balfour's growth frameworks, Casey Winters' Pinte... |
| **`incident-responder`** | [`incident-responder/`](./incident-responder) | Production incident response - from detection through resolution to post-mortem. Effective communication, systematic investigation, and blameless learning fr... |
| **`launch-storytelling`** | [`launch-storytelling/`](./launch-storytelling) | Expert in crafting launch narratives - product launches, feature releases, company announcements, and milestone communications. Covers launch timing, narrati... |
| **`layer2-scaling`** | [`layer2-scaling/`](./layer2-scaling) | Expert in Ethereum L2 solutions - Optimism, Arbitrum, zkSync, Base, and rollup architecture for scalable dApp developmentUse when "layer 2, l2, optimism, arb... |
| **`legacy-archaeology`** | [`legacy-archaeology/`](./legacy-archaeology) | Expert in understanding and navigating legacy codebases. Covers code archaeology techniques, finding hidden knowledge, mapping dependencies, and extracting u... |
| **`logging-strategies`** | [`logging-strategies/`](./logging-strategies) | World-class application logging - structured logs, correlation IDs, log aggregation, and the battle scars from debugging production without proper logsUse wh... |
| **`ml-memory`** | [`ml-memory/`](./ml-memory) | Memory systems specialist for hierarchical memory, consolidation, and outcome-based learningUse when "memory system, memory hierarchy, memory consolidation, ... |
| **`monorepo-management`** | [`monorepo-management/`](./monorepo-management) | Expert at organizing and optimizing monorepos. Covers Turborepo, Nx, pnpm workspaces, task orchestration, caching, and dependency management. Knows how to sc... |
| **`motor-control`** | [`motor-control/`](./motor-control) | Patterns for electric motor control including Field Oriented Control (FOC), stepper motor control, encoder interfaces, current sensing, and power electronics... |
| **`negotiation-playbook`** | [`negotiation-playbook/`](./negotiation-playbook) | Expert in negotiation strategy - systematic approaches to reaching agreements that create value. Covers preparation, tactics, objection handling, and closing... |
| **`nft-engineer`** | [`nft-engineer/`](./nft-engineer) | Battle-hardened NFT developer specializing in ERC-721/1155 implementations, gas-optimized minting, reveal mechanics, and marketplace integration. Has launche... |
| **`observability`** | [`observability/`](./observability) | Expert at making systems observable and debuggable. Covers structured logging, metrics collection, distributed tracing, error tracking, and alerting. Knows h... |
| **`orbital-mechanics`** | [`orbital-mechanics/`](./orbital-mechanics) | Use when computing orbits, planning maneuvers, propagating trajectories, or analyzing orbital perturbations for spacecraft or celestial bodies. Use when "orb... |
| **`patent-drafting`** | [`patent-drafting/`](./patent-drafting) | Use when drafting patent applications, writing claims, analyzing prior art, or responding to office actions - covers USPTO practice, claim strategies, and sp... |
| **`pitch-narrative`** | [`pitch-narrative/`](./pitch-narrative) | Expert in crafting pitch narratives that move people to action - investor pitches, sales presentations, partnership proposals, and team rallying stories. Cov... |
| **`pivot-patterns`** | [`pivot-patterns/`](./pivot-patterns) | Most successful startups pivoted. Instagram was a check-in app. Slack was a game. YouTube was a dating site. The ability to recognize when to pivot and execu... |
| **`playground`** | [`playground/`](./playground) | Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview,... |
| **`pricing-strategy`** | [`pricing-strategy/`](./pricing-strategy) | Pricing is the most powerful lever you're not pulling. A 1% price increase typically yields 8-11% profit improvement - more than any other lever. Yet most fo... |
| **`product-discovery`** | [`product-discovery/`](./product-discovery) | Expert in product discovery - the continuous process of understanding what customers need and what solutions will work. Covers customer research, problem val... |
| **`product-management`** | [`product-management/`](./product-management) | World-class product management expertise combining the user-obsession of Marty Cagan's empowered product teams, the strategic clarity of Shreyas Doshi, and t... |
| **`product-market-fit`** | [`product-market-fit/`](./product-market-fit) | Expert in product-market fit - the condition where a product satisfies a strong market demand. Covers PMF definition, measurement, the journey to PMF, and wh... |
| **`project-artifact`** | [`project-artifact/`](./project-artifact) | Generate and publish a project status artifact — an opinionated, tabbed status page for a project too big for one update (overview & success criteria, the wo... |
| **`python-craftsman`** | [`python-craftsman/`](./python-craftsman) | Python excellence specialist for type safety, async patterns, packaging, and idiomatic production codeUse when "python development, type hints, async python,... |
| **`react-patterns`** | [`react-patterns/`](./react-patterns) | Expert knowledge for React hooks, composition, and component patternsUse when "react hook, useEffect, useState, useCallback, useMemo, context, component comp... |
| **`realtime-engineer`** | [`realtime-engineer/`](./realtime-engineer) | Real-time systems expert for WebSockets, SSE, presence, and live synchronizationUse when "websocket, real-time updates, live collaboration, presence indicato... |
| **`roast-writing`** | [`roast-writing/`](./roast-writing) | Expert in comedic roasts, witty insults, and self-deprecating humor that lands. Covers the craft of punching up vs down, timing, target selection, and knowin... |
| **`ros2-robotics`** | [`ros2-robotics/`](./ros2-robotics) | Patterns for developing robotics applications with ROS2 (Robot Operating System 2). Covers nodes, topics, services, actions, launch files, lifecycle manageme... |
| **`rwa-tokenization`** | [`rwa-tokenization/`](./rwa-tokenization) | World-class expertise in tokenizing real-world assets with regulatory complianceUse when "tokenize real estate, tokenize real world assets, RWA tokenization,... |
| **`sequential-thinking`** | [`sequential-thinking/`](./sequential-thinking) | Dynamic multi-step reasoning, hypothesis evaluation, branching logic, and reflective problem-solving using Sequential Thinking MCP. |
| **`side-project-shipping`** | [`side-project-shipping/`](./side-project-shipping) | Expert in actually finishing and shipping side projects. Covers MVP scoping, motivation management, perfectionism killing, and the art of "good enough." Unde... |
| **`strategic-partnerships`** | [`strategic-partnerships/`](./strategic-partnerships) | Expert in strategic partnerships - identifying, negotiating, and managing alliances that create mutual value. Covers partnership strategy, deal structuring, ... |
| **`taste-and-craft`** | [`taste-and-craft/`](./taste-and-craft) | Good taste is knowing what is good. Craft is making it real. Together they separate products people tolerate from products people love. Paul Graham's essays ... |
| **`team-communications`** | [`team-communications/`](./team-communications) | Your team can't execute what they don't understand. And they won't buy in to what they don't feel part of. Internal communications isn't about memos and anno... |
| **`tech-debt-manager`** | [`tech-debt-manager/`](./tech-debt-manager) | Strategic technical debt management - understanding the debt metaphor, knowing when to take on debt, when to pay it down, and how to communicate debt decisio... |
| **`tech-debt-negotiation`** | [`tech-debt-negotiation/`](./tech-debt-negotiation) | Expert in making the business case for technical debt reduction. Covers quantifying debt costs, getting stakeholder buy-in, prioritizing what to fix, and neg... |
| **`technical-analysis`** | [`technical-analysis/`](./technical-analysis) | Master of price action, chart patterns, and technical indicators - combining classical Wyckoff/Dow theory with modern quantitative validation for edge identi... |
| **`technical-writer`** | [`technical-writer/`](./technical-writer) | Effective technical documentation - knowing what to write, for whom, and when. From code comments to architecture docs, making knowledge accessible and maint... |
| **`temporal-craftsman`** | [`temporal-craftsman/`](./temporal-craftsman) | Workflow orchestration expert using Temporal.io for durable executionUse when "temporal workflow, durable execution, saga pattern, workflow orchestration, lo... |
| **`web3-gaming`** | [`web3-gaming/`](./web3-gaming) | Comprehensive expertise in blockchain game development, including play-to-earn (P2E) mechanics, play-to-own (P2O) models, in-game economies, NFT integration,... |
| **`yc-playbook`** | [`yc-playbook/`](./yc-playbook) | The YC meta-game distilled from 4000+ funded companies. Demo day prep, batch dynamics, investor updates, "launch now" mentality, talking to users obsessively... |

<br/>

---

## 🚀 How to Use a Skill in Antigravity

### 1. Automatic On-Demand Loading (Recommended)
Antigravity automatically analyzes your natural language prompt and activates matching skills via progressive disclosure:
```text
"Help me audit our accessibility contrast across all buttons according to WCAG AA"
# Automatically triggers ./accessibility or ./accessibility-design
```

### 2. Explicit Invocations
You can explicitly target any skill in your conversation:
```text
"Use the schema-architect skill to design a multi-tenant PostgreSQL schema."
```
