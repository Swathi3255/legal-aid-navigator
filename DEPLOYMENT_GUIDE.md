# 🚀 Deployment Guide - Legal Aid Navigator

## Complete Step-by-Step Guide for Beginners

This guide will help you deploy your Legal Aid Navigator app to the web so anyone can access it!

---

## 📋 What We're Deploying

- **Frontend** (the website people see) → **Vercel** ✅ Free, fast, easy
- **Backend** (the server that processes questions) → **Render** ✅ Free tier, perfect for Flask

---

## Part 1: Deploy Backend on Render (15 minutes)

### Step 1: Create a Render Account

1. Go to [render.com](https://render.com/)
2. Click **"Get Started"**
3. Sign up with GitHub (recommended) or email
4. Verify your email

### Step 2: Connect Your GitHub Repository

**First, push your code to GitHub:**

```bash
# In your project directory
cd /home/swathi/AIProjects/AIE2/legal-aid-navigator

# Initialize git if not already done
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Legal Aid Navigator"

# Create a new repository on GitHub (go to github.com/new)
# Then connect and push:
git remote add origin https://github.com/YOUR_USERNAME/legal-aid-navigator.git
git branch -M main
git push -u origin main
```

### Step 3: Create Web Service on Render

1. In Render dashboard, click **"New +"** → **"Web Service"**
2. Connect your GitHub repository
3. Select the `legal-aid-navigator` repository
4. Configure the service:

**Settings to fill in:**

| Field | Value |
|-------|-------|
| **Name** | `legal-aid-navigator-api` |
| **Region** | Choose closest to you |
| **Branch** | `main` |
| **Root Directory** | `backend` |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |
| **Instance Type** | `Free` |

5. Click **"Create Web Service"**

### Step 4: Wait for Deployment

- Render will build and deploy your backend
- Takes 2-5 minutes
- You'll see logs showing progress
- When it says "Live", your backend is ready! 🎉

### Step 5: Get Your Backend URL

- After deployment, you'll see a URL like: `https://legal-aid-navigator-api.onrender.com`
- **Copy this URL** - you'll need it for the frontend!

### Step 6: Test Your Backend

Visit in your browser:
```
https://your-backend-url.onrender.com/api/health
```

You should see:
```json
{
  "status": "healthy",
  "message": "Legal Aid Navigator API is running in demo mode"
}
```

✅ **Backend is deployed!**

---

## Part 2: Update Frontend to Use Deployed Backend (5 minutes)

### Step 1: Update Frontend API URL

You need to change the frontend to point to your deployed backend instead of `localhost:5000`.

**I've prepared an updated version - see below for the modified file.**

The change is simple - we replace:
```javascript
const response = await fetch('http://localhost:5000/api/legal-question', {
```

With:
```javascript
const response = await fetch('https://YOUR-BACKEND-URL.onrender.com/api/legal-question', {
```

---

## Part 3: Deploy Frontend on Vercel (10 minutes)

### Step 1: Create Vercel Account

1. Go to [vercel.com](https://vercel.com/)
2. Click **"Sign Up"**
3. Sign up with GitHub (recommended)
4. Authorize Vercel to access your GitHub

### Step 2: Import Your Project

1. Click **"Add New..." → "Project"**
2. Select **"Import Git Repository"**
3. Find your `legal-aid-navigator` repository
4. Click **"Import"**

### Step 3: Configure Project

**Settings:**

| Field | Value |
|-------|-------|
| **Project Name** | `legal-aid-navigator` |
| **Framework Preset** | `Other` (or leave as detected) |
| **Root Directory** | `./` (leave default) |
| **Build Command** | Leave empty |
| **Output Directory** | `frontend` |

### Step 4: Deploy

1. Click **"Deploy"**
2. Vercel will build and deploy (takes 1-2 minutes)
3. You'll see confetti 🎉 when it's done!

### Step 5: Get Your Live URL

- Vercel gives you a URL like: `https://legal-aid-navigator.vercel.app`
- Click **"Visit"** to see your live site!

✅ **Frontend is deployed!**

---

## Part 4: Test Your Deployed App (5 minutes)

### Test the Full App

1. Visit your Vercel URL: `https://legal-aid-navigator.vercel.app`
2. Try the example questions
3. Type your own question
4. Verify you get responses

### Troubleshooting

**If you see "backend not connected" error:**
- Check that you updated the frontend with correct backend URL
- Make sure backend URL includes `https://` and `/api/legal-question`
- Check backend is running: visit `https://your-backend.onrender.com/api/health`

**If backend is slow (first request):**
- Render's free tier "sleeps" after 15 minutes of inactivity
- First request wakes it up (takes 30-60 seconds)
- Subsequent requests are fast

---

## 🎉 You're Live!

Your Legal Aid Navigator is now accessible to anyone on the internet!

**Share your links:**
- 🌐 **Website**: `https://legal-aid-navigator.vercel.app`
- 🔧 **API**: `https://legal-aid-navigator-api.onrender.com`

---

## Part 5: Custom Domain (Optional)

### Add Your Own Domain to Vercel

If you have a domain (like `legalaidnavigator.com`):

1. In Vercel dashboard → Your project
2. Go to **"Settings" → "Domains"**
3. Add your domain
4. Follow DNS setup instructions
5. Wait 24-48 hours for DNS propagation

---

## Part 6: Environment Variables (For Production with Real RAG)

When you're ready to connect your full RAG system:

### On Render (Backend):

1. Go to your web service dashboard
2. Click **"Environment"** tab
3. Add environment variables:
   - `OPENAI_API_KEY` = `your-key`
   - `TAVILY_API_KEY` = `your-key`
   - `LANGCHAIN_API_KEY` = `your-key` (optional)
4. Click **"Save Changes"**
5. Service will auto-redeploy

---

## Cost Breakdown

| Service | Plan | Cost |
|---------|------|------|
| **Render** | Free Tier | $0/month |
| **Vercel** | Hobby (Free) | $0/month |
| **Total** | | **$0/month** ✅ |

**Free tier limitations:**
- Render: Backend sleeps after 15 min inactivity (wakes on first request)
- Vercel: 100GB bandwidth/month, 100 deployments/day (more than enough!)

**When to upgrade:**
- Render Pro ($7/month): Always-on, no sleep, faster
- Vercel Pro ($20/month): More bandwidth, custom domains, analytics

---

## Monitoring Your Deployed App

### Check Backend Status:
```
https://your-backend.onrender.com/api/status
```

### Check Backend Health:
```
https://your-backend.onrender.com/api/health
```

### View Render Logs:
1. Go to Render dashboard
2. Click your service
3. Click **"Logs"** tab
4. See real-time requests and errors

### View Vercel Analytics:
1. Go to Vercel dashboard
2. Click your project
3. See page views, performance, etc.

---

## Updating Your Deployed App

### To Update Backend:
1. Make changes to code locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update backend"
   git push
   ```
3. Render auto-deploys from GitHub!

### To Update Frontend:
1. Make changes to code locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update frontend"
   git push
   ```
3. Vercel auto-deploys from GitHub!

**Both services auto-deploy on every push to main branch!** 🚀

---

## Quick Troubleshooting

### Backend Issues:

**"Application failed to start"**
- Check Render logs for errors
- Verify `requirements.txt` has all dependencies
- Make sure `gunicorn app:app` is correct start command

**"502 Bad Gateway"**
- Backend is starting up (first request after sleep)
- Wait 30-60 seconds and try again

### Frontend Issues:

**"CORS Error"**
- Backend needs `flask-cors` installed (already in requirements.txt)
- Check `CORS(app)` is in backend code (it is!)

**"Network Error"**
- Check backend URL is correct in frontend code
- Verify backend is running: visit `/api/health`

---

## Next Steps After Deployment

1. **Share your live app!**
   - Tweet about it
   - Share with tenant organizations
   - Add to your portfolio

2. **Monitor usage**
   - Check Render logs daily
   - Monitor Vercel analytics
   - Watch for errors

3. **Collect feedback**
   - Add Google Analytics (optional)
   - Create feedback form
   - Track user questions

4. **Connect real RAG system**
   - Add API keys as environment variables
   - Integrate your full multi-agent system
   - Test thoroughly before enabling

---

## Support Resources

- **Render Docs**: [render.com/docs](https://render.com/docs)
- **Vercel Docs**: [vercel.com/docs](https://vercel.com/docs)
- **Flask Deployment**: [flask.palletsprojects.com/deploying](https://flask.palletsprojects.com/deploying/)

---

## Summary Checklist

- [ ] Create Render account
- [ ] Push code to GitHub
- [ ] Deploy backend on Render
- [ ] Get backend URL
- [ ] Update frontend with backend URL
- [ ] Create Vercel account
- [ ] Deploy frontend on Vercel
- [ ] Test live app
- [ ] Share your live URL!

**Estimated Total Time: 30-40 minutes for complete deployment** ⏱️

---

🎉 **Congratulations! You've deployed a full-stack web application!** 🎉

Your Legal Aid Navigator is now live and helping tenants understand their rights!

---

*Deployment Guide v1.0 | Created for absolute beginners | No prior deployment experience needed*

