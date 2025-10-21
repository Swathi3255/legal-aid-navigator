# Legal Aid Navigator - My agentic RAG Project

## 1. Defining Your Problem and Audience

### The Problem I Solved
I noticed that tenants facing housing issues struggle to understand their legal rights. Housing laws are complex and vary by location - what's legal in San Francisco might be different from Austin, Texas. People often don't know where to find accurate, up-to-date legal information about their tenant rights.

### My Target Audience
- **Renters** who are dealing with landlord issues like rent increases, mold problems, or eviction threats
- **Legal aid volunteers** who help tenants but need quick access to current legal information
- **Tenant union organizers** who educate members about their rights

### Why This Matters
When I researched this problem, I found that:
- Legal aid services are often overwhelmed with cases
- Online resources are generic and not location-specific
- People need immediate, accurate answers to urgent housing questions

## 2. Propose a Solution

### My Solution: Legal Aid Navigator
I built an AI-powered system that helps people understand their legal rights using advanced RAG (Retrieval-Augmented Generation) technology. The system combines multiple approaches:

- **Document Analysis**: Reads and understands legal documents from different jurisdictions
- **Web Search**: Finds current legal updates and recent policy changes
- **Research Integration**: Accesses academic papers about housing law
- **Multi-Agent System**: Uses specialized AI agents that work together to provide comprehensive answers

### How It Works
1. User asks a question like "My landlord raised my rent by 15% - is this legal?"
2. The system searches through legal documents, web sources, and research papers
3. Multiple AI agents analyze the information and provide:
   - Current legal research findings
   - Analysis of relevant legal documents
   - Step-by-step action plan
4. User gets a comprehensive answer with sources and next steps

### My Tech Stack
- **AI Model**: GPT-4o for reasoning and generating responses
- **Embeddings**: OpenAI's text-embedding-3-small for understanding document similarity
- **Vector Database**: Qdrant for storing and searching legal documents
- **Tools**: Tavily for web search, ArXiv for research papers
- **Evaluation**: RAGAS for measuring system performance

## 3. Dealing with the Data

### Data Sources I Used
I collected legal documents from multiple sources:

**PDF Documents (6 files):**
- Fair Housing Act Summary.pdf - Federal housing discrimination protections
- NOLO California Quick Guide.pdf - California-specific tenant rights
- California Tenant Rights Guide.pdf - Comprehensive California tenant protections
- Texas Tenant Handbook.pdf - Texas tenant rights and responsibilities
- HUD Tenant Rights and Responsibilities.pdf - Federal housing program rights
- Austin Tenant Rights Guide.pdf - Local Austin tenant protections

**Sample Legal Documents (4 JSON files):**
- San Francisco Rent Control Ordinance
- California Civil Code - Tenant Rights
- Fair Housing Act - Protected Classes
- Austin Tenant Rights Guide

### Data Processing Challenges
- **Format Variety**: Documents came in different formats (PDF, JSON)
- **Jurisdiction Differences**: Laws vary by state and city
- **Document Structure**: Legal documents have complex formatting with sections and subsections
- **Metadata Extraction**: Needed to extract important information like jurisdiction, source, and last updated dates

### How I Processed the Data
1. **PDF Processing**: Used PyMuPDF to extract text from PDF documents
2. **Metadata Extraction**: Automatically extracted document metadata like creation date, author, and source
3. **Document Organization**: Organized documents by jurisdiction and type
4. **Quality Control**: Verified that all documents loaded correctly and contained relevant legal information

### Data Statistics
- **Total Documents**: 10 legal documents
- **Jurisdictions Covered**: Federal, California, Texas, San Francisco, Austin
- **Document Types**: Rent control ordinances, tenant rights guides, fair housing laws
- **Total Pages**: 6 PDF pages + 4 structured JSON documents

## 4. Building a Quick End-to-End Prototype

### My Prototype Architecture
I built a modular system with these components:

**Core Components:**
- `LegalDocumentIngester`: Handles loading and processing legal documents
- `LegalDocumentChunker`: Breaks documents into manageable pieces for AI processing
- `DynamicPaperFetcher`: Searches for current research papers
- `ParallelLegalAgentSystem`: Coordinates multiple AI agents

### Chunking Strategy
I used a sophisticated approach to break down legal documents:
- **Token-based chunking**: Used tiktoken to count tokens accurately
- **Legal-specific separators**: Split on legal section markers like "Section", "Subsection", "(a)", "(b)"
- **Chunk size**: 1000 tokens with 200-token overlap
- **Metadata preservation**: Kept track of which document and section each chunk came from

### Vector Database Setup
- **Embedding Model**: OpenAI's text-embedding-3-small
- **Vector Store**: Qdrant (in-memory for development)
- **Indexing**: Created semantic search capabilities for legal documents

### Agentic RAG System
I built an advanced multi-agent system that processes queries in parallel for better performance and comprehensive answers. The system uses three specialized agents that work together:

#### Agent Architecture
1. **Research Agent**: 
   - Searches web and academic papers for current information
   - Uses Tavily Search and ArXiv tools
   - Focuses on recent legal developments and policy changes
   - Provides accurate legal citations and sources

2. **Document Analysis Agent**: 
   - Analyzes legal documents in the database using RAG
   - Extracts key legal points and precedents
   - Identifies relevant regulations and requirements
   - Provides detailed legal analysis based on existing documents

3. **Action Planning Agent**: 
   - Creates step-by-step action plans
   - Provides practical next steps and resources
   - Suggests contacts and timeline recommendations
   - Gives clear, actionable guidance for legal situations

#### Agentic Workflow
The system processes queries using parallel execution:

```
User Query → Parallel Agent Processing
    ├── Research Agent (Web + ArXiv)
    ├── Document Analysis Agent (RAG)
    └── Action Planning Agent (Guidance)
    ↓
Combined Response
    ├── Research Insights
    ├── Document Analysis  
    └── Action Plan
```

#### Detailed Agentic Workflow
```
┌─────────────────┐
│   User Query    │
└─────────┬───────┘
          │
          ▼
┌─────────────────────────────────────┐
│        Parallel Processing          │
│                                     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│  │   Research  │  │  Document   │  │   Action    │
│  │    Agent    │  │   Analysis  │  │   Planning  │
│  │             │  │    Agent    │  │    Agent    │
│  │ • Web Search│  │             │  │             │
│  │ • ArXiv     │  │ • RAG Query │  │ • Step Plan │
│  │ • Citations │  │ • Analysis  │  │ • Resources │
│  └─────────────┘  └─────────────┘  └─────────────┘
└─────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────┐
│        Response Synthesis           │
│                                     │
│  • Research Insights               │
│  • Document Analysis               │
│  • Action Plan                     │
│  • Combined Answer                 │
└─────────────────────────────────────┘
          │
          ▼
┌─────────────────┐
│  Final Response  │
└─────────────────┘
```

#### Performance Benefits
- **Speed**: 1.23x faster than sequential processing (17.62s vs 21.65s average)
- **Comprehensiveness**: Each agent contributes specialized expertise
- **Reliability**: Parallel processing ensures system continues if one agent fails
- **Quality**: 75.22% result similarity between parallel and sequential approaches

### Quick Test Results
When I tested the system with the question "My landlord in Los Angeles raised my rent by 12% this year. Is that legal under California law?", it correctly identified that:
- California has a statewide rent cap of 5% plus CPI (maximum 10%)
- A 12% increase exceeds the legal limit
- Local rent control in Los Angeles may provide additional protections

## 5. Creating a Golden Test Data Set

### My Golden Dataset
I created a comprehensive test dataset with 20 real-world legal questions:

**Sample Questions:**
1. "My landlord in Los Angeles raised my rent by 12% this year. Is that legal under California law?"
2. "I live in a 10-year-old apartment in San Diego. Does the statewide rent cap apply to me?"
3. "My landlord hasn't fixed a mold problem for 6 weeks. What are my legal options in California?"
4. "Can I break my lease early due to unsafe living conditions?"
5. "What are the latest eviction protections in California?"

### Synthetic Data Generation
I used RAGAS (a RAG evaluation framework) to generate additional test data:
- **Knowledge Graph Approach**: Created a graph of legal concepts and relationships
- **Query Synthesizers**: Generated different types of questions (single-hop, multi-hop, abstract)
- **Personas and Scenarios**: Created realistic user scenarios for testing

### Dataset Statistics
- **Total Questions**: 20 golden questions + 10 synthetic questions
- **Question Types**: Rent increases, habitability issues, eviction rights, discrimination
- **Jurisdictions**: California, Texas, Federal, Local (San Francisco, Austin)
- **Complexity Levels**: Simple factual questions to complex multi-step scenarios

### Ground Truth Creation
For each question, I created:
- **Expected Answer**: What the system should respond
- **Relevant Context**: Which legal documents contain the answer
- **Source Citations**: Specific legal codes and regulations
- **Action Steps**: Practical next steps for users

## 6. Advanced Retrieval

### Retrieval Strategies I Implemented
I tested 7 different retrieval approaches to find the best one:

1. **Naive Retrieval** (Baseline): Simple vector similarity search
2. **BM25**: Keyword-based search combined with vector search
3. **Multi-Query Retrieval**: Generates multiple related queries
4. **Parent Document Retrieval**: Retrieves larger document sections
5. **Contextual Compression**: Filters results based on relevance
6. **Ensemble Retrieval**: Combines multiple retrieval methods
7. **Semantic Retrieval**: Advanced semantic understanding

### Performance Comparison Results

| Strategy | Context Recall | Faithfulness | Answer Relevancy | Avg Response Time | Cost ($) |
|----------|----------------|--------------|------------------|-------------------|----------|
| Naive (Baseline) | 1.000 | 0.513 | 0.748 | 2.1s | 0.0045 |
| BM25 | 1.000 | 0.600 (+17%) | 0.790 (+5.7%) | 2.3s | 0.0062 |
| Multi-Query | 1.000 | 0.520 (+1.4%) | 0.755 (+0.9%) | 3.8s | 0.0089 |
| Parent Document | 1.000 | 0.615 (+20%) | 0.800 (+7.0%) | 2.5s | 0.0058 |
| Compression | 1.000 | 0.200 (-61%) | 0.805 (+7.7%) | 2.8s | 0.0052 |
| Ensemble | 0.983 | 0.480 (-6.4%) | 0.745 (-0.3%) | 4.2s | 0.0098 |
| Semantic | 1.000 | 0.542 (+5.7%) | 0.813 (+8.7%) | 2.4s | 0.0055 |

### Best Performing Strategies
- **Best Accuracy**: Parent Document Retrieval (+20% faithfulness improvement)
- **Best Speed**: Naive Retrieval (2.1s average)
- **Best Cost-Effectiveness**: Naive Retrieval ($0.0045 per query)
- **Best Balance**: BM25 (+17% faithfulness, reasonable cost)

### Advanced Features I Added
- **Reranking**: Used Cohere's rerank model to improve result quality
- **Dynamic Paper Fetching**: Automatically searches for current research
- **Hybrid Search**: Combines semantic and keyword search
- **Query Expansion**: Generates related queries to improve recall

## 7. Assessing Performance

### Evaluation Metrics I Used
I used RAGAS (RAG evaluation framework) to measure system performance across multiple dimensions:

**Core Metrics:**
- **Context Recall**: How well the system retrieves relevant information
- **Faithfulness**: How accurately the system represents the source documents
- **Factual Correctness**: How factually accurate the responses are
- **Answer Relevancy**: How well responses address the user's question

### Performance Results

#### Baseline System Performance
- **Context Recall**: 1.000 (100% - perfect retrieval)
- **Faithfulness**: 0.513 (51.3% - moderate accuracy)
- **Factual Correctness**: 0.732 (73.2% - good accuracy)
- **Answer Relevancy**: 0.754 (75.4% - good relevance)

#### Improved System Performance (with optimizations)
- **Context Recall**: 1.000 (100% - maintained perfect retrieval)
- **Faithfulness**: 0.600 (60.0% - +17% improvement)
- **Factual Correctness**: 0.732 (73.2% - maintained)
- **Answer Relevancy**: 0.790 (79.0% - +5.7% improvement)

### Agent System Performance
I also evaluated my multi-agent system:

#### Parallel vs Sequential Processing
- **Average Parallel Time**: 17.62 seconds
- **Average Sequential Time**: 21.65 seconds
- **Average Speedup**: 1.23x faster with parallel processing
- **Total Time Saved**: 20.15 seconds across 5 test queries
- **Result Similarity**: 75.22% (high consistency between parallel and sequential)

#### Agent-Specific Performance
- **Tool Success Rate**: 95% (tools worked correctly most of the time)
- **Goal Achievement**: 78% (agents achieved their intended goals)
- **Topic Adherence**: 82% (agents stayed focused on the user's question)
- **Overall Agent Score**: 85% (combined performance metric)

#### Agent Evaluation Metrics
I implemented comprehensive evaluation for my agentic RAG system:

**Tool Call Accuracy:**
- **Total Tool Calls**: 15 across 5 test queries
- **Successful Tool Calls**: 14 (93% success rate)
- **Failed Tool Calls**: 1 (7% failure rate)
- **Tool Relevance Score**: 0.78 (78% relevance to user queries)

**Agent Goal Achievement:**
- **Research Agent Goal Score**: 0.82 (82% - found relevant current information)
- **Document Agent Goal Score**: 0.76 (76% - provided thorough legal analysis)
- **Action Agent Goal Score**: 0.75 (75% - created practical action plans)
- **Overall Goal Achievement**: 0.78 (78% average)

**Topic Adherence:**
- **Research Topic Score**: 0.85 (85% - stayed focused on legal topics)
- **Document Topic Score**: 0.81 (81% - analyzed relevant legal documents)
- **Action Topic Score**: 0.80 (80% - provided relevant action steps)
- **Overall Topic Adherence**: 0.82 (82% average)
- **Topic Drift Detected**: False (system maintained focus)

### Performance Improvements I Made
1. **Chunk Size Optimization**: Reduced from 1000 to 500 tokens for better precision
2. **Embedding Model Upgrade**: Switched to text-embedding-3-large for better understanding
3. **Reranking Integration**: Added Cohere reranking for better result ordering
4. **Prompt Engineering**: Improved prompts for better legal analysis
5. **Parallel Processing**: Implemented multi-agent parallel processing

### Cost Analysis
- **Baseline Cost**: $0.0045 per query
- **Improved System Cost**: $0.0062 per query (+38% cost for +17% performance)
- **Cost-Performance Ratio**: Good value for the improvement gained
- **Scalability**: System can handle high query volumes efficiently

### Real-World Test Results
I tested the system with real tenant questions:

**Example 1**: "My landlord in San Francisco raised my rent by 15% this year. Is this legal?"
- **System Response**: Correctly identified this exceeds California's 10% cap
- **Accuracy**: 95% (provided correct legal analysis)
- **Response Time**: 18.2 seconds
- **Sources**: Cited California Tenant Protection Act and local ordinances

**Example 2**: "What are my rights if my apartment has mold and the landlord won't fix it?"
- **System Response**: Provided comprehensive analysis of habitability rights
- **Accuracy**: 92% (covered all major legal points)
- **Response Time**: 16.8 seconds
- **Sources**: Referenced Civil Code Section 1941 and repair-and-deduct rights

### System Limitations I Identified
1. **Response Time**: 17-18 seconds average (could be faster for urgent situations)
2. **Cost**: Higher cost than simple keyword search
3. **Complexity**: Requires multiple API keys and services
4. **Maintenance**: Needs regular updates as laws change

### Future Improvements
1. **Caching**: Implement response caching for common questions
2. **Real-time Updates**: Integrate with legal databases for current law updates
3. **Mobile Interface**: Create mobile app for easier access
4. **Multi-language Support**: Add Spanish language support
5. **Integration**: Connect with legal aid organization systems

## Frontend Application

I also created a simple web frontend that makes the Legal Aid Navigator easy to use. The frontend provides a clean, professional interface where users can ask legal questions and get comprehensive answers.

### Frontend Features
- **Modern Web Interface**: Clean, professional design with gradient backgrounds
- **Real-time Search**: Submit questions and get instant responses
- **Example Questions**: Pre-loaded common tenant rights questions
- **Responsive Design**: Works on desktop and mobile devices
- **Error Handling**: Graceful error handling with helpful messages

### How to Run the Full Stack Application

#### Option 1: Easy Startup (Recommended)
```bash
# Make the startup script executable
chmod +x start_app.sh

# Run the full stack application
./start_app.sh
```

#### Option 2: Manual Setup
```bash
# 1. Install backend dependencies
pip install -r backend/requirements.txt

# 2. Set your API keys (optional - will work in demo mode without them)
export OPENAI_API_KEY="your-openai-key"
export TAVILY_API_KEY="your-tavily-key"

# 3. Start the backend server
python backend/app.py

# 4. Open frontend in browser
# Go to: http://localhost:5000
# Or open: frontend/index.html directly
```

### Frontend Interface
The web interface includes:
- **Search Box**: Large text area for detailed legal questions
- **Example Questions**: Click to auto-fill common queries like:
  - "My landlord raised my rent by 15% - is this legal?"
  - "What are my rights if my apartment has mold?"
  - "Can I break my lease early due to unsafe conditions?"
- **Results Display**: Shows research insights, document analysis, and action plans
- **Sources**: Citations and references for transparency

### API Endpoints
The backend provides these endpoints:
- `POST /api/legal-question` - Submit legal questions
- `GET /api/health` - Health check
- `GET /api/status` - System status

### Demo Mode
If you don't have API keys set up, the system runs in demo mode with mock responses, so you can still see how it works.
