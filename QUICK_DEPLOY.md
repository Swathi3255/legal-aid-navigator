# ⚡ Quick Deploy Guide - 5 Steps to Live!

**Total Time: 30 minutes** | **Cost: $0 (Free tier)**

---

## 🎯 What You'll Get

- ✅ Your app live on the internet
- ✅ Anyone can access it via URL
- ✅ Auto-deploys when you push to GitHub
- ✅ Professional hosting for free

**Your URLs will be:**
- Frontend: `https://legal-aid-navigator.vercel.app`
- Backend: `https://legal-aid-navigator-api.onrender.com`

---

## Step 1: Push to GitHub (5 min)

```bash
# In your project folder
cd /home/swathi/AIProjects/AIE2/legal-aid-navigator

# Initialize git (if not done)
git init

# Add all files
git add .

# Commit
git commit -m "Ready for deployment"

# Go to github.com and create a new repository called "legal-aid-navigator"
# Then run these commands (replace YOUR_USERNAME with your GitHub username):

git remote add origin https://github.com/YOUR_USERNAME/legal-aid-navigator.git
git branch -M main
git push -u origin main
```

✅ **Code is on GitHub!**

---

## Step 2: Deploy Backend on Render (10 min)

1. Go to **[render.com](https://render.com/)** → Sign up with GitHub
2. Click **"New +"** → **"Web Service"**
3. Select your `legal-aid-navigator` repository
4. Fill in:
   - **Name**: `legal-aid-navigator-api`
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: Free
5. Click **"Create Web Service"**
6. Wait 2-5 minutes for deployment
7. **Copy your backend URL** (e.g., `https://legal-aid-navigator-api.onrender.com`)

Test it: Visit `https://your-backend-url.onrender.com/api/health`

✅ **Backend is live!**

---

## Step 3: Update Frontend Config (2 min)

Edit `frontend/config.js`:

```javascript
const config = {
    // Replace this with your Render backend URL from Step 2:
    API_URL: 'https://legal-aid-navigator-api.onrender.com'
};
```

Push the change:
```bash
git add frontend/config.js
git commit -m "Update backend URL for production"
git push
```

✅ **Frontend configured!**

---

## Step 4: Deploy Frontend on Vercel (10 min)

1. Go to **[vercel.com](https://vercel.com/)** → Sign up with GitHub
2. Click **"Add New..." → "Project"**
3. Import your `legal-aid-navigator` repository
4. Configure:
   - **Framework Preset**: Other
   - **Root Directory**: `./`
   - **Output Directory**: `frontend`
5. Click **"Deploy"**
6. Wait 1-2 minutes
7. Get your live URL! 🎉

✅ **Frontend is live!**

---

## Step 5: Test Your Live App (3 min)

1. Visit your Vercel URL
2. Try example questions:
   - "My landlord raised my rent by 15% - is this legal?"
   - "What are my rights if my apartment has mold?"
3. See results appear!

✅ **You're live on the internet!** 🚀

---

## 🎉 Share Your App!

Your Legal Aid Navigator is now accessible to anyone:

- 🌐 **Website**: `https://legal-aid-navigator.vercel.app`
- 📱 Share on social media
- 📧 Send to tenant organizations
- 💼 Add to your portfolio

---

## Future Updates

Every time you push to GitHub:
- Render auto-deploys backend
- Vercel auto-deploys frontend
- Changes go live in 2-5 minutes!

```bash
# Make changes, then:
git add .
git commit -m "Your update description"
git push
# Auto-deploys! 🚀
```

---

## Common Issues & Fixes

**Backend is slow on first request?**
→ Free tier "sleeps" after 15 min. First request takes 30-60 sec to wake up.

**CORS error?**
→ Backend has `flask-cors` installed, should work. Check backend logs on Render.

**"Network error" in frontend?**
→ Double-check `frontend/config.js` has correct backend URL with `https://`

**Need help?**
→ See full [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed troubleshooting

---

## What's Next?

After deployment, you can:
- Add your OpenAI API key to Render for real RAG responses
- Connect a custom domain in Vercel
- Monitor traffic in dashboards
- Collect user feedback

---

**Need the detailed version? See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)**

*Quick Deploy Guide v1.0 | From code to live in 30 minutes*

