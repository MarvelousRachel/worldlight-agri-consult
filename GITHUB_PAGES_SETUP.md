# GitHub Pages Deployment Guide

## 🚀 Your Website is Ready for GitHub Pages!

Your repository has been initialized and all files are committed. Follow these steps to deploy your website:

### Step 1: Create a GitHub Account
1. Go to [github.com](https://github.com)
2. Sign up for a free account if you don't have one
3. Verify your email address

### Step 2: Create a New Repository
1. Click the "+" icon in the top right corner
2. Select "New repository"
3. Repository name: `worldlight-agri-consult` (or your preferred name)
4. Make sure it's set to **Public**
5. **DO NOT** initialize with README (we already have one)
6. Click "Create repository"

### Step 3: Connect Your Local Repository
GitHub will show you commands similar to these. Run them in your terminal:

```bash
cd "/Users/fomekongrachelmarvelous/Desktop/Nexus Perception Labs/Website"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/worldlight-agri-consult.git
git push -u origin main
```

**Replace `YOUR_USERNAME` with your actual GitHub username!**

### Step 4: Enable GitHub Pages
1. Go to your repository on GitHub
2. Click "Settings" tab
3. Scroll down to "Pages" in the left sidebar
4. Under "Source", select "Deploy from a branch"
5. Select "main" branch
6. Select "/ (root)" folder
7. Click "Save"

### Step 5: Access Your Live Website
After 5-10 minutes, your website will be live at:
`https://YOUR_USERNAME.github.io/worldlight-agri-consult/`

## 🎯 Quick Terminal Commands

I'll help you run these commands. Just let me know when you've created your GitHub repository!

## ✅ What's Already Done
- ✅ Git repository initialized
- ✅ All files committed
- ✅ README.md created
- ✅ .gitignore configured
- ✅ Repository structure optimized

## 🔧 Optional: Custom Domain
If you want to use your own domain (like www.worldlightagriconsult.com):
1. Buy a domain from any registrar
2. Add a CNAME file to your repository
3. Configure DNS settings
4. Enable custom domain in GitHub Pages settings

## 📞 Need Help?
Let me know if you need assistance with any of these steps!
