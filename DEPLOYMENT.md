# Deployment Guide — NetSage AI

This guide explains how to deploy NetSage AI online for free so anyone can access it.

You need to deploy **two things**:
1. **Backend** (Python FastAPI server) → on **Render** (free)
2. **Frontend** (index.html website) → on **Netlify** (free)

---

## Step 1: Push to GitHub

If you haven't already, push your project to GitHub:

```bash
cd NetSage_AI

git init
git add .
git commit -m "NetSage AI full project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/NetSage_AI.git
git push -u origin main
```

> Replace `YOUR_USERNAME` with your actual GitHub username.

---

## Step 2: Deploy Backend on Render

1. Go to [render.com](https://render.com) and sign up with your GitHub account.
2. Click **New** → **Web Service**.
3. Select your `NetSage_AI` repository.
4. Fill in these settings:

| Setting | Value |
|---------|-------|
| **Name** | `netsage-backend` |
| **Root Directory** | `backend` |
| **Environment** | Python 3 |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn main:app --host 0.0.0.0 --port 10000` |

5. Click **Create Web Service**.
6. Wait 2-3 minutes for deployment.
7. You'll get a URL like: `https://netsage-backend.onrender.com`

**Save this URL — you need it next.**

---

## Step 3: Update Frontend to Use Live Backend

1. Open `dashboard/index.html` in any text editor.
2. Press **Ctrl+H** (Find and Replace).
3. Find: `http://localhost:8000`
4. Replace with: your Render URL (e.g., `https://netsage-backend.onrender.com`)
5. Click **Replace All** and save the file.
6. Commit and push the change:

```bash
git add .
git commit -m "Updated backend URL for deployment"
git push
```

---

## Step 4: Deploy Frontend on Netlify

1. Go to [netlify.com](https://netlify.com) and sign up with your GitHub account.
2. Click **Add new site** → **Import an existing project**.
3. Select your `NetSage_AI` repository.
4. Set **Publish directory** to: `dashboard`
5. Click **Deploy Site**.
6. Wait ~1 minute. You'll get a live URL like: `https://netsage-ai.netlify.app`

---

## Done!

Your professor and anyone in the world can now visit your Netlify URL and use the full NetSage AI system — AI diagnosis, human review, and live dashboard!

### Quick Reference

| Component | Hosted On | URL Example |
|-----------|-----------|-------------|
| Backend API | Render | `https://netsage-backend.onrender.com` |
| Frontend Website | Netlify | `https://netsage-ai.netlify.app` |
