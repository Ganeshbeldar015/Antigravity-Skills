import os
import re

def build_readme():
    skills_dir = os.path.abspath('skills')
    all_dirs = sorted([d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))])
    
    skills = []
    for s in all_dirs:
        skill_file = os.path.join(skills_dir, s, 'SKILL.md')
        name = s
        desc = ""
        if os.path.exists(skill_file):
            with open(skill_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if match:
                raw_yaml = match.group(1)
                for line in raw_yaml.split('\n'):
                    if line.startswith('name:'):
                        name = line.split(':', 1)[1].strip().strip('"\'')
                    elif line.startswith('description:'):
                        desc = line.split(':', 1)[1].strip().strip('"\'')
                # If description continues on multiple lines
                if not desc or len(desc) < 15:
                    m_desc = re.search(r'description:\s*(.*?)(?=\n[a-zA-Z0-9_-]+:|\Z)', raw_yaml, re.DOTALL)
                    if m_desc:
                        desc = ' '.join(m_desc.group(1).split())
        
        # Clean up description
        desc = desc.replace('\n', ' ').strip().strip('"\'')
        if len(desc) > 160:
            desc = desc[:157] + '...'
        if not desc:
            desc = f"Specialized runbook and best practices for {s.replace('-', ' ')}."
            
        skills.append({
            'folder': s,
            'name': name,
            'description': desc
        })

    # Group skills into domains based on keywords
    categories = {
        "🤖 AI, Machine Learning & Autonomous Agents": [],
        "🎨 Frontend, UI/UX, Design Systems & 3D": [],
        "⚙️ Backend, APIs & Distributed Systems": [],
        "🗄️ Database Engineering, ORM & Caching": [],
        "🛡️ Security, SAST, Auth & Vulnerability Auditing": [],
        "🧪 Testing, QA Automation & Performance Engineering": [],
        "☁️ DevOps, Cloud Infrastructure, Docker & CI/CD": [],
        "📱 Mobile, Cross-Platform & Desktop Development": [],
        "📊 Data Science, Analytics, Big Data & Modeling": [],
        "✍️ Product, Growth, Media, Copywriting & Docs": [],
        "🛠️ Developer Productivity, Architecture & Workflow Automation": []
    }

    for sk in skills:
        fn = sk['folder'].lower()
        nm = sk['name'].lower()
        ds = sk['description'].lower()
        combined = f"{fn} {nm} {ds}"

        if any(k in combined for k in ['agent', 'llm', 'prompt', 'rag', 'embedding', 'gpt', 'neural', 'machine learning', 'diffusion', 'inference', 'langchain', 'openai', 'gemini', 'claude']):
            categories["🤖 AI, Machine Learning & Autonomous Agents"].append(sk)
        elif any(k in combined for k in ['3d', 'webgl', 'three', 'blender', 'ui', 'ux', 'css', 'tailwind', 'shadcn', 'design', 'figma', 'canva', 'frontend', 'layout', 'typography', 'svg', 'canvas', 'animation', 'storyflow', 'storybook', 'color', 'theme', 'accessibility', 'a11y']):
            categories["🎨 Frontend, UI/UX, Design Systems & 3D"].append(sk)
        elif any(k in combined for k in ['database', 'postgres', 'sqlite', 'sql', 'redis', 'supabase', 'query', 'schema', 'migration', 'mongodb', 'prisma', 'orm', 'indexing', 'dynamo', 'cassandra']):
            categories["🗄️ Database Engineering, ORM & Caching"].append(sk)
        elif any(k in combined for k in ['security', 'vulnerability', 'owasp', 'auth', 'oauth', 'jwt', 'encryption', 'penetration', 'audit', 'secret', 'sast', 'cve', 'identity', 'sandbox']):
            categories["🛡️ Security, SAST, Auth & Vulnerability Auditing"].append(sk)
        elif any(k in combined for k in ['test', 'selenium', 'playwright', 'cypress', 'jest', 'qa', 'benchmark', 'profiler', 'vitals', 'performance', 'latency', 'load test', 'mutation']):
            categories["🧪 Testing, QA Automation & Performance Engineering"].append(sk)
        elif any(k in combined for k in ['docker', 'kubernetes', 'compose', 'k8s', 'ci/cd', 'devops', 'terraform', 'cloud', 'aws', 'gcp', 'azure', 'serverless', 'nginx', 'deploy', 'pipeline']):
            categories["☁️ DevOps, Cloud Infrastructure, Docker & CI/CD"].append(sk)
        elif any(k in combined for k in ['mobile', 'android', 'ios', 'flutter', 'react native', 'swift', 'kotlin', 'expo']):
            categories["📱 Mobile, Cross-Platform & Desktop Development"].append(sk)
        elif any(k in combined for k in ['data', 'analytics', 'pandas', 'numpy', 'etl', 'pipeline', 'statistics', 'math', 'visualization', 'tableau', 'spark', 'modeling']):
            categories["📊 Data Science, Analytics, Big Data & Modeling"].append(sk)
        elif any(k in combined for k in ['api', 'rest', 'graphql', 'grpc', 'backend', 'fastapi', 'microservice', 'express', 'django', 'flask', 'nest', 'endpoint', 'server', 'rpc']):
            categories["⚙️ Backend, APIs & Distributed Systems"].append(sk)
        elif any(k in combined for k in ['copywriting', 'ad', 'marketing', 'seo', 'audio', 'video', 'voice', 'content', 'script', 'branding', 'podcast', 'social']):
            categories["✍️ Product, Growth, Media, Copywriting & Docs"].append(sk)
        else:
            categories["🛠️ Developer Productivity, Architecture & Workflow Automation"].append(sk)

    # Sort each category by folder name
    for cat in categories:
        categories[cat] = sorted(categories[cat], key=lambda x: x['folder'])

    # Build Markdown Content
    md = []
    md.append("<div align=\"center\">\n")
    md.append("# 🎯 Google Antigravity Skills Directory\n")
    md.append(f"<p><em>Comprehensive on-demand runbook library comprising <b>{len(skills)} specialized skills</b> for Antigravity & the Gemini Agent CLI.</em></p>\n")
    md.append("<p>")
    md.append(f'  <img src="https://img.shields.io/badge/Total%20Skills-{len(skills)}%20Modular-blue?style=for-the-badge&logo=codewars&logoColor=white" alt="Total Skills" />')
    md.append('  <img src="https://img.shields.io/badge/Architecture-Progressive%20Disclosure-success?style=for-the-badge&logo=google&logoColor=white" alt="Architecture" />')
    md.append('  <img src="https://img.shields.io/badge/Zero%20Overhead-On--Demand%20Loading-orange?style=for-the-badge" alt="Zero Overhead" />')
    md.append("</p>\n")
    md.append("</div>\n\n---\n\n")

    md.append("## 📖 Overview\n\n")
    md.append("Skills in Antigravity are modular procedural runbooks loaded via **Progressive Disclosure**.\n\n")
    md.append("- **Zero Token Overhead at Rest**: Only skill names and triggers are indexed in memory. The full body of a `SKILL.md` is strictly loaded when your task or prompt matches its intent.\n")
    md.append("- **Standardized Architecture**: Every skill folder contains a declarative `SKILL.md` with YAML frontmatter triggers and optional domain-specific references or validation checklists.\n\n")

    md.append("### 📑 Category Navigation\n\n")
    md.append("| Category | Skills Count | Focus Domain |\n")
    md.append("| :--- | :---: | :--- |\n")
    
    cat_anchors = {
        "🤖 AI, Machine Learning & Autonomous Agents": "ai-machine-learning--autonomous-agents",
        "🎨 Frontend, UI/UX, Design Systems & 3D": "frontend-uiux-design-systems--3d",
        "⚙️ Backend, APIs & Distributed Systems": "backend-apis--distributed-systems",
        "🗄️ Database Engineering, ORM & Caching": "database-engineering-orm--caching",
        "🛡️ Security, SAST, Auth & Vulnerability Auditing": "security-sast-auth--vulnerability-auditing",
        "🧪 Testing, QA Automation & Performance Engineering": "testing-qa-automation--performance-engineering",
        "☁️ DevOps, Cloud Infrastructure, Docker & CI/CD": "devops-cloud-infrastructure-docker--cicd",
        "📱 Mobile, Cross-Platform & Desktop Development": "mobile-cross-platform--desktop-development",
        "📊 Data Science, Analytics, Big Data & Modeling": "data-science-analytics-big-data--modeling",
        "✍️ Product, Growth, Media, Copywriting & Docs": "product-growth-media-copywriting--docs",
        "🛠️ Developer Productivity, Architecture & Workflow Automation": "developer-productivity-architecture--workflow-automation"
    }

    for cat_name, cat_skills in categories.items():
        anchor = cat_anchors.get(cat_name, "")
        short_name = cat_name.split(' ', 1)[1] if ' ' in cat_name else cat_name
        md.append(f"| [**{cat_name}**](#-{anchor}) | **{len(cat_skills)}** | {short_name} |\n")

    md.append("\n---\n\n")

    # Render each category
    for cat_name, cat_skills in categories.items():
        anchor = cat_anchors.get(cat_name, "")
        md.append(f"## {cat_name}\n\n")
        md.append(f"> *{len(cat_skills)} specialized runbooks available in this domain.*\n\n")
        md.append("| Skill Identifier | Runbook Path | Core Capabilities & Description |\n")
        md.append("| :--- | :--- | :--- |\n")
        for sk in cat_skills:
            esc_desc = sk['description'].replace('|', '\\|')
            md.append(f"| **`{sk['name']}`** | [`{sk['folder']}/`](./{sk['folder']}) | {esc_desc} |\n")
        md.append("\n<br/>\n\n")

    md.append("---\n\n")
    md.append("## 🚀 How to Use a Skill in Antigravity\n\n")
    md.append("### 1. Automatic On-Demand Loading (Recommended)\n")
    md.append("Antigravity automatically analyzes your natural language prompt and activates matching skills via progressive disclosure:\n")
    md.append("```text\n\"Help me audit our accessibility contrast across all buttons according to WCAG AA\"\n# Automatically triggers ./accessibility or ./accessibility-design\n```\n\n")
    md.append("### 2. Explicit Invocations\n")
    md.append("You can explicitly target any skill in your conversation:\n")
    md.append("```text\n\"Use the schema-architect skill to design a multi-tenant PostgreSQL schema.\"\n```\n")

    with open(os.path.join(skills_dir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(''.join(md))

    print(f"Generated skills/README.md successfully with {len(skills)} skills across {len(categories)} categories!")

if __name__ == '__main__':
    build_readme()
