# Deploy Everything on Render (One Service Option)

## If You Want to Use ONLY Render (No Vercel)

This guide shows you how to deploy both frontend and backend on Render.

**Pros:**
- ✅ Only one service to manage
- ✅ Still free
- ✅ Simpler mental model

**Cons:**
- ❌ Slower frontend (no Vercel CDN)
- ❌ Frontend and backend share same server
- ❌ Less optimized than Vercel for static files

---

## Setup Steps (20 minutes)

### Step 1: Modify Backend to Serve Frontend

Your `backend/app.py` already serves the frontend! It has this code:

```python
@app.route('/')
def index():
    """Serve the main page"""
    frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend', 'index.html')
    if os.path.exists(frontend_path):
        with open(frontend_path, 'r', encoding='utf-8') as f:
            return f.read()
```

So your Flask app already serves both frontend and backend!

### Step 2: Update Frontend Config

Edit `frontend/config.js`:

```javascript
const config = {
    // Use relative URL since frontend and backend are on same server
    API_URL: ''  // Empty string means same origin
};
```

Or update the fetch URL in `frontend/index.html` to use relative path:

```javascript
const response = await fetch('/api/legal-question', {
```

### Step 3: Deploy to Render

1. Go to [render.com](https://render.com/)
2. Sign up with GitHub
3. Click **"New +"** → **"Web Service"**
4. Select your repository
5. Configure:
   - **Name**: `legal-aid-navigator`
   - **Root Directory**: Leave blank (or `/`)
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `cd backend && gunicorn app:app`
   - **Instance Type**: Free

6. Click **"Create Web Service"**

### Step 4: Done!

Your app will be live at:
- `https://legal-aid-navigator.onrender.com`

Both frontend and backend are served from the same URL!

---

## Testing

- Frontend: `https://legal-aid-navigator.onrender.com/`
- Backend API: `https://legal-aid-navigator.onrender.com/api/health`

---

## Comparison

| Approach | Services | Setup Complexity | Performance | Cost |
|----------|----------|------------------|-------------|------|
| **Vercel + Render** | 2 services | Medium (2 deployments) | Best (CDN) | $0 |
| **Render Only** | 1 service | Easy (1 deployment) | Good | $0 |

---

## My Recommendation

- **If you're comfortable with two services**: Use Vercel + Render (better performance)
- **If you want simplicity**: Use Render only (good enough for MVP)

Both are completely valid approaches!

---

*Render-Only Deployment v1.0 | Single service option*

