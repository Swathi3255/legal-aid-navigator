# 🏛️ Legal Aid Navigator
https://legal-aid-navigator.onrender.com/
An advanced AI-powered RAG (Retrieval-Augmented Generation) system that helps tenants understand their legal rights and navigate complex housing laws across different jurisdictions. Built with state-of-the-art LLM technology and comprehensive evaluation frameworks.

> **"Intelligent Legal Guidance for Those Who Need It Most"**

## 📋 Quick Links

### 🎯 Start Here
- **[MVP Documentation Index](MVP_DOCUMENTATION_INDEX.md)** - 📚 **Your complete guide to all strategic documents**

### Technical Documentation
- **[Backend Documentation](Backend_README.md)** - Technical implementation details
- **[Frontend Documentation](frontend/Frontend_README.md)** - Web interface guide

### Strategic Documents (MVP Planning)
- **[MVP Quick Reference](MVP_QUICK_REFERENCE.md)** - ⚡ Fast answers to all key questions (start here!)
- **[Executive Summary](EXECUTIVE_SUMMARY.md)** - Concise overview for stakeholders
- **[MVP Strategy](MVP_STRATEGY.md)** - Comprehensive product strategy and differentiation analysis
- **[Competitive Analysis](COMPETITIVE_ANALYSIS.md)** - Market positioning and competitive advantages
- **[Pitch Deck Outline](PITCH_DECK_OUTLINE.md)** - Presentation guide for pitches and demos
- **[MVP Implementation Checklist](MVP_IMPLEMENTATION_CHECKLIST.md)** - Week-by-week action plan

---

## 🎯 What Makes This Different?

### The Problem We Solve
Tenants facing urgent housing issues cannot quickly access accurate, jurisdiction-specific legal guidance with actionable next steps, leaving them vulnerable to rights violations during time-sensitive crises.

### Why Not Just Use ChatGPT?

| Feature | ChatGPT/General AI | Legal Aid Navigator |
|---------|-------------------|---------------------|
| **Jurisdiction Awareness** | ❌ Generic answers | ✅ Multi-layer (federal/state/city) |
| **Current Legal Information** | ❌ Training cutoff | ✅ Real-time web + research |
| **Source Verification** | ❌ No citations | ✅ Verifiable legal codes |
| **Actionable Guidance** | ❌ Information only | ✅ Step-by-step action plans |
| **Specialized System** | ❌ General purpose | ✅ 3 specialized AI agents |
| **Quality Assurance** | ❌ No evaluation | ✅ RAGAS metrics (100% recall, 79% relevancy) |

**We're not a chatbot with legal knowledge—we're a legal research system powered by AI.**

---

## 🚀 Key Features

### 1. **Multi-Agent Specialized System**
Three AI agents work in parallel:
- **Research Agent**: Searches web and academic papers for current legal information
- **Document Analysis Agent**: Analyzes curated legal documents using advanced RAG
- **Action Planning Agent**: Creates step-by-step action plans with timelines

### 2. **Jurisdiction-Specific Intelligence**
Understands federal, state, county, and city-level laws. A question about rent increases gets different answers for San Francisco, Austin, or rural Texas.

### 3. **Real-Time Legal Research**
Unlike static AI models, we integrate:
- Live web search (Tavily)
- Academic research papers (ArXiv)
- Current case law and policy updates

### 4. **Comprehensive Responses**
Every answer includes:
- 📊 **Legal Analysis**: What the law says
- 🎯 **Your Situation**: How it applies to you
- ✅ **Action Plan**: Step-by-step with timelines
- 📞 **Resources**: Local organizations and contacts

---

## 🚀 Deployment

### Deploy to Production (Free!)

**Quick Deploy (30 minutes)**: Follow **[QUICK_DEPLOY.md](QUICK_DEPLOY.md)** for 5-step deployment

**Detailed Guide**: See **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)** for complete instructions

**Deployment Stack**:
- Frontend: Vercel (Free tier)
- Backend: Render (Free tier)
- Total Cost: **$0/month**

**After deployment, your app will be live at:**
- `https://legal-aid-navigator.onrender.com/`

---

## 💻 Local Development

### Frontend
Please refer to [Frontend_README.md](frontend/Frontend_README.md) file

### Backend
Please refer to [Backend_README.md](Backend_README.md) file

### Quick Start (Local)

```bash
# Install dependencies
uv sync

# Run backend
python backend/app.py

# Open browser
http://localhost:5000
```

## 🛠️ Tech Stack

| Component | Choice | Justification |
|-----------|---------|---------------|
| **LLM** | GPT-4o | Best reasoning for legal nuance, cost-effective |
| **Embeddings** | text-embedding-3-small | High quality, fast, cheap |
| **Vector DB** | Qdrant (in-memory) | Advanced vector operations, production-ready |
| **Orchestration** | LangChain & LangGraph | Rapid prototyping, excellent agent support |
| **Evaluation** | RAGAS | Industry standard for RAG evaluation |
| **Monitoring** | LangSmith | Free tier, excellent tracing |
| **Search** | Tavily Search API | Real-time web search capabilities |
| **Research** | ArXiv integration | Access to latest legal research |
| **Document Processing** | PyMuPDF, Unstructured | Robust PDF and document processing |

Loom video : https://www.loom.com/share/8f43a734389c4b7eaf1a5b30a3c87939?sid=5c2b16cd-3c58-4d09-bb46-8df0ebcae29c

