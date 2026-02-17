---
name: deploy
description: Builds the Astro site, verifies output, generates deployment scripts and Nginx configuration. Use after all pages are built, as the final step.
---

# Deploy Skill

Build, verify, and prepare for deployment.

## Step 1: Build

```bash
npm run build
```

Check exit code. If errors, fix them before proceeding.

## Step 2: Verify Output

```bash
# Check all expected pages exist
ls -la dist/
ls -la dist/*/

# Count HTML files
find dist -name "*.html" | wc -l

# Check for broken image references in built HTML
grep -r "src=\"" dist/ | grep -v "data:" | grep -v "http" | head -20

# Check total build size
du -sh dist/
```

Verify:
- [ ] Every page from docs/pages.md has a corresponding HTML file in dist/
- [ ] No 404-producing broken links
- [ ] Images are present and optimized (check dist/_astro/ for generated images)
- [ ] Total dist/ size is reasonable (under 5MB for a typical site)

## Step 3: Generate deploy.sh

```bash
#!/bin/bash
set -e

# Configuration — edit these
REMOTE_USER="your-user"
REMOTE_HOST="your-server.com"
REMOTE_PATH="/var/www/sitename"
BRANCH="main"

echo "=== Deploying website ==="

# Pull latest changes
git pull origin $BRANCH

# Install dependencies (if any changed)
npm ci --production

# Build
npm run build

# Copy dist to web root
rsync -avz --delete dist/ $REMOTE_PATH/

echo "=== Deploy complete at $(date) ==="
```

**Alternative: Deploy directly on the server (simpler)**

```bash
#!/bin/bash
set -e

# Run this ON the server
cd /var/www/sitename-source
git pull origin main
npm ci --production
npm run build
cp -r dist/* /var/www/sitename/

echo "Updated at $(date)"
```

## Step 4: Generate Nginx Config

```nginx
server {
    listen 80;
    server_name example.com www.example.com;
    root /var/www/sitename;
    index index.html;

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;

    # Cache static assets aggressively
    location /_astro/ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    # Cache images
    location ~* \.(jpg|jpeg|png|webp|avif|gif|svg|ico)$ {
        expires 30d;
        add_header Cache-Control "public";
    }

    # Cache fonts
    location ~* \.(woff|woff2|ttf|otf)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    # Gzip
    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml text/javascript image/svg+xml;
    gzip_min_length 1000;

    # Clean URLs (Astro generates /about/index.html → /about)
    location / {
        try_files $uri $uri/ $uri.html =404;
    }

    # Custom 404
    error_page 404 /404.html;
}
```

Save as `nginx.conf` in the project root for reference.

## Step 5: SSL Note

Remind the user:
```
If this is a new domain, set up SSL with:
  sudo certbot --nginx -d example.com -d www.example.com

If you're already managing SSL on this server, just update
your existing nginx config with the root path above.
```

## Step 6: .gitignore

Ensure .gitignore includes:
```
node_modules/
dist/
.astro/
.DS_Store
*.log
```

The `dist/` folder is NOT committed — it's built on the server after pull.
The `photo-bank/` folder CAN be committed (original assets) or gitignored if too large.

## Step 7: Final Checklist

Output this checklist for the user:

```markdown
## Deployment Checklist

### Before Going Live
- [ ] All placeholder images replaced (check _catalog.json for placeholder: true)
- [ ] Company contact info verified in docs/company-profile.md
- [ ] All links working (run: `npx broken-link-checker dist/index.html`)
- [ ] Favicon uploaded to public/favicon.svg
- [ ] OG image uploaded to public/og-image.png (1200x630px)
- [ ] Meta descriptions set for all pages

### Server Setup
- [ ] Git repo cloned on server
- [ ] Node.js installed (v18+)
- [ ] npm install completed
- [ ] Nginx configured and tested
- [ ] SSL certificate installed
- [ ] DNS pointing to server

### Go Live
- [ ] Run `npm run build` on server
- [ ] Test all pages in browser
- [ ] Test on mobile device
- [ ] Run Lighthouse audit (aim for 95+ all categories)
- [ ] Submit sitemap to Google Search Console

### Ongoing Updates
- Edit content in docs/*.md
- Replace photos in src/assets/images/
- git commit & push
- On server: git pull && npm run build
```

## Git Workflow for Updates

The beauty of this setup: updating the site is just:

```
Local:  Edit docs/ or images → git push
Server: git pull → npm run build → done
```

No CMS, no database, no server-side runtime. Just static files served by Nginx.
