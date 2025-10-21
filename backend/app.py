from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

def get_mock_response(question):
    """Generate a mock response for demo purposes"""
    mock_responses = {
        "rent": {
            "answer": "Based on California law, rent increases are capped at 5% plus the regional Consumer Price Index, with a maximum total increase of 10% per year. This applies to buildings over 15 years old.",
            "sources": ["California Tenant Rights Guide", "NOLO California Quick Guide"],
            "action_plan": "1. Document the rent increase notice\n2. Check if your building is covered by rent control\n3. Contact local tenant rights organization\n4. Consider legal consultation if the increase exceeds limits"
        },
        "mold": {
            "answer": "Under California Civil Code Section 1941, landlords must maintain rental units in habitable condition, which includes being free from excessive mold. You have rights to request repairs and potentially withhold rent for uninhabitable conditions.",
            "sources": ["California Tenant Rights Guide", "HUD Tenant Rights"],
            "action_plan": "1. Notify landlord in writing about mold issue\n2. Request inspection and repair\n3. Document all communications\n4. Consider repair-and-deduct if landlord fails to act"
        },
        "eviction": {
            "answer": "California requires 'just cause' for evictions in most cases. Landlords must follow proper procedures and provide appropriate notice. You have rights to contest wrongful evictions.",
            "sources": ["California Tenant Rights Guide", "Texas Tenant Handbook"],
            "action_plan": "1. Review the eviction notice carefully\n2. Check if the reason qualifies as 'just cause'\n3. Respond within the required timeframe\n4. Seek legal assistance if needed"
        },
        "discrimination": {
            "answer": "The Fair Housing Act prohibits discrimination based on race, color, religion, sex, national origin, familial status, or disability. You can file a complaint with HUD or your local fair housing agency.",
            "sources": ["Fair Housing Act Summary", "HUD Tenant Rights"],
            "action_plan": "1. Document all discriminatory actions\n2. File a complaint with HUD within one year\n3. Contact local fair housing organization\n4. Consider legal action if necessary"
        },
        "lease": {
            "answer": "Breaking a lease early depends on your specific circumstances and local laws. Common valid reasons include uninhabitable conditions, landlord harassment, or military deployment.",
            "sources": ["California Tenant Rights Guide", "Texas Tenant Handbook"],
            "action_plan": "1. Review your lease agreement carefully\n2. Document the reasons for breaking the lease\n3. Notify landlord in writing\n4. Consult with a legal aid attorney"
        }
    }
    
    question_lower = question.lower()
    for key, response in mock_responses.items():
        if key in question_lower:
            return response
    
    # Default response
    return {
        "answer": "This appears to be a tenant rights question. Based on general legal principles, tenants have various protections under state and federal law. The specific answer depends on your location and circumstances.",
        "sources": ["General Legal Resources"],
        "action_plan": "1. Research local tenant rights organizations\n2. Document all relevant communications\n3. Consider consulting with a legal aid attorney\n4. Keep records of all relevant documents"
    }

@app.route('/')
def index():
    """Serve the main page"""
    import os
    frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend', 'index.html')
    if os.path.exists(frontend_path):
        with open(frontend_path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return "Frontend not found. Please check the file path."

@app.route('/api/legal-question', methods=['POST'])
def legal_question():
    """Handle legal question requests"""
    try:
        data = request.get_json()
        question = data.get('question', '').strip()
        
        if not question:
            return jsonify({'error': 'No question provided'}), 400
        
        print(f"Processing question: {question}")
        
        # Get mock response
        mock_response = get_mock_response(question)
        
        response = {
            'answer': mock_response['answer'],
            'sources': mock_response['sources'],
            'action_plan': mock_response['action_plan'],
            'research_insights': {
                'output': 'Based on current legal research and recent developments in tenant rights law.',
                'sources': ['Legal Research Database', 'Recent Case Law']
            },
            'document_analysis': {
                'output': mock_response['answer'],
                'sources': mock_response['sources']
            },
            'action_plan': {
                'output': mock_response['action_plan']
            }
        }
        
        return jsonify(response)
        
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'Legal Aid Navigator API is running in demo mode'
    })

@app.route('/api/status', methods=['GET'])
def status():
    """Get system status"""
    return jsonify({
        'rag_system_initialized': False,
        'api_keys_configured': False,
        'mode': 'demo',
        'message': 'Running in demo mode with mock responses'
    })

if __name__ == '__main__':
    print("🏛️ Starting Legal Aid Navigator API (Demo Mode)...")
    print("🚀 Starting Flask server...")
    print("📱 Frontend will be available at: http://localhost:5000")
    print("🔧 API endpoints:")
    print("   - POST /api/legal-question")
    print("   - GET /api/health")
    print("   - GET /api/status")
    print("")
    print("⚠️  Running in DEMO MODE with mock responses")
    print("   To connect to your RAG system, set up API keys and install LangChain dependencies")
    print("")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
