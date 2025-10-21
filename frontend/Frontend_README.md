# Legal Aid Navigator - Frontend

This is a simple web frontend for the Legal Aid Navigator system. It provides a user-friendly interface to interact with the RAG-based legal assistance system.

## Features

- **Clean, Professional Interface**: Modern design with gradient backgrounds and card-based layout
- **Real-time Search**: Submit legal questions and get instant responses
- **Example Questions**: Pre-loaded example questions to help users get started
- **Responsive Design**: Works on desktop and mobile devices
- **Error Handling**: Graceful error handling with user-friendly messages
- **Loading States**: Visual feedback during processing

## How to Use

### Option 1: Run with Backend (Recommended)
1. Make sure your backend is running (see main README)
2. Open your web browser
3. Go to `http://localhost:5000`

### Option 2: Run Frontend Only (Demo Mode)
1. Open `frontend/index.html` directly in your web browser
2. The frontend will show mock responses since no backend is connected

## File Structure

```
frontend/
├── index.html          # Main HTML file with embedded CSS and JavaScript
└── README.md          # This file
```

## Features Explained

### Search Interface
- **Large text area**: Users can type detailed legal questions
- **Search button**: Submits the question to the backend API
- **Loading spinner**: Shows progress while processing
- **Example queries**: Click to auto-fill common questions

### Results Display
- **Research Insights**: Current legal information from web and academic sources
- **Document Analysis**: Analysis of legal documents in the database
- **Action Plan**: Step-by-step guidance for the user
- **Sources**: Citations and references for transparency

### Error Handling
- **Connection errors**: Shows helpful messages if backend is not running
- **Empty queries**: Prevents submission of empty questions
- **API errors**: Graceful handling of backend errors

## Customization

### Styling
All CSS is embedded in the HTML file. You can modify:
- Colors: Change the gradient backgrounds and accent colors
- Fonts: Modify the font-family in the CSS
- Layout: Adjust spacing, padding, and margins
- Responsiveness: Modify breakpoints for different screen sizes

### Functionality
The JavaScript is also embedded. You can modify:
- API endpoints: Change the fetch URL in the `searchLegalQuestion()` function
- Example questions: Add or modify questions in the HTML
- Response handling: Modify how results are displayed
- Error messages: Customize error and success messages

## Browser Compatibility

- **Chrome**: Full support
- **Firefox**: Full support
- **Safari**: Full support
- **Edge**: Full support
- **Mobile browsers**: Responsive design works on mobile devices

## Technical Details

### API Integration
The frontend communicates with the backend via REST API:
- **Endpoint**: `POST /api/legal-question`
- **Request**: JSON with `question` field
- **Response**: JSON with `answer`, `sources`, `action_plan`, etc.

### Fallback Mode
If the backend is not available, the frontend shows mock responses for demo purposes.

### No Build Process Required
This is a simple HTML/CSS/JavaScript application that runs directly in the browser without any build process or compilation.
