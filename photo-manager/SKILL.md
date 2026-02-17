---
name: photo-manager
description: Catalogs photos from photo-bank/, records dimensions, copies to organized src/assets/images/ folders, and generates _catalog.json. Use whenever photos need to be processed, cataloged, or placed in the website.
---

# Photo Manager Skill

Handle all image assets — catalog, organize, and track for easy replacement.

## Core Principle

**NEVER use a photo without first checking its dimensions.** Every image placement must be dimension-aware.

## Photo Naming Convention (Critical for Automation)

Encourage clients to use **descriptive, purpose-specific photo names** instead of generic names like `IMG_001.jpg`. Claude uses these names to automatically identify photo purpose and appropriate placement.

### Recommended Naming Patterns

Claude recognizes and categorizes photos by name:

```
Logo-Light-Mode.png              → header/footer branding
Logo-Dark-Mode.png               → dark mode header/footer
Favicon.svg                      → browser tab icon

CEO-Headshot.jpg                 → team section leadership
Staff-Members.jpg                → about page team intro
Developer-Alice.jpg              → team grid member
Designer-Bob.jpg                 → team grid member

Hero-Office-Team.jpg             → homepage hero
Hero-Product-Launch.jpg          → feature page hero
Hero-About-Page.jpg              → about page hero

Service-Consulting.jpg           → services grid
Feature-Dashboard.png            → features section

Testimonial-Client-John.jpg      → testimonials carousel
Testimonial-Company-Logo.png     → client logos section

Government-License.jpg           → trust/credentials section
ISO-Certification.png            → awards/certifications
Industry-Award-Badge.jpg         → credentials

Team-Retreat-Event.jpg           → culture/behind-scenes
Office-Culture-Photo.jpg         → about page
Product-Launch-Celebration.jpg   → timeline/history
```

### Naming Guidelines

1. **Use hyphens** — `Logo-Light-Mode.png` not `Logo_light_mode.png`
2. **Capitalize key words** — `CEO-Headshot.jpg` not `ceo-headshot.jpg`
3. **Be specific** — `Developer-Alice.jpg` not `team-photo.jpg`
4. **Include variants** — `Logo-Light-Mode.png`, `Logo-Dark-Mode.png` (Claude selects appropriately)
5. **One purpose per file** — Don't combine `Logo-And-Favicon.png` → split them
6. **Describe role** — `Testimonial-Client-John.jpg` tells Claude the photo's purpose

### How Claude Uses These Names

1. **Reads the filename** — Interprets the purpose from the name
2. **Categorizes automatically** — Sorts into `hero/`, `team/`, `services/`, etc.
3. **Places intelligently** — No manual placement needed
4. **Updates catalog** — Records the recognized purpose in `_catalog.json`

### Photos Without Descriptive Names

If a photo has a generic name (`IMG_001.jpg`, `photo1.png`):
- Claude will ask for clarification: "What is this photo for?"
- Or categorize as `misc/` with a placeholder
- Best to encourage descriptive naming upfront

---

## Step 1: Scan photo-bank/

```bash
# Get all images and their dimensions
for img in photo-bank/*.{jpg,jpeg,png,webp,svg}; do
  if [ -f "$img" ]; then
    identify -format "%f|%w|%h|%b\n" "$img"
  fi
done
```

If `identify` (ImageMagick) is not available, use Python:

```python
from PIL import Image
import os, json

photos = []
for f in os.listdir('photo-bank'):
    if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        img = Image.open(f'photo-bank/{f}')
        w, h = img.size
        size_kb = os.path.getsize(f'photo-bank/{f}') // 1024
        photos.append({
            'filename': f,
            'width': w,
            'height': h,
            'size_kb': size_kb,
            'aspect_ratio': f"{w//gcd(w,h)}:{h//gcd(w,h)}"
        })
        print(f"{f}: {w}x{h} ({size_kb}KB)")
```

## Step 2: Organize into Categories

Create subdirectories in `src/assets/images/`:

```
src/assets/images/
├── hero/          # Full-width hero/banner images (wide: 16:9, 21:9)
├── team/          # Team member headshots (square: 1:1, or 3:4)
├── services/      # Service/product images (flexible)
├── gallery/       # Photo gallery images (flexible)
├── about/         # About page images (flexible)
├── testimonials/  # Client logos or photos (small, square)
├── misc/          # Everything else
└── _catalog.json  # Master catalog
```

## Step 3: Copy and Catalog

For each photo in photo-bank/:
1. Determine the best category based on filename hints and the page structure in `docs/pages.md`
2. Copy (not move!) to the appropriate subfolder
3. Record in _catalog.json

### Filename Conventions

Interpret filenames to determine category:
- `hero-*`, `banner-*`, `bg-*` → `hero/`
- `team-*`, `staff-*`, `person-*` → `team/`
- `service-*`, `product-*`, `work-*` → `services/`
- `gallery-*`, `portfolio-*`, `project-*` → `gallery/`
- `about-*`, `office-*`, `culture-*` → `about/`
- `client-*`, `testimonial-*` → `testimonials/`
- `logo-*` → `branding/` (auto-detects best logo)
- Anything else → `misc/`

## Logo Auto-Detection & Selection

**NEW FEATURE**: System automatically scans for all PNG files with "logo" in the filename and selects the best one based on:
1. **Size preference**: Larger files (higher resolution) ranked higher
2. **Format preference**: PNG with transparency (RGBA) > PNG (RGB) > other formats
3. **Dimensions**: Wide logos (width > height) preferred for headers; square (1:1) for favicons

### Logo Processing Script

```python
from PIL import Image
import os
from pathlib import Path

def find_best_logo(photo_bank_path='photo-bank'):
    """Find and select the best logo from photo-bank"""
    logos = []

    for f in os.listdir(photo_bank_path):
        if 'logo' in f.lower() and f.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(photo_bank_path, f)
            img = Image.open(img_path)
            w, h = img.size
            size_kb = os.path.getsize(img_path) // 1024

            # Score calculation (higher = better)
            score = 0
            score += size_kb * 0.5  # Prefer larger files (higher res)
            score += w * h * 0.001  # Prefer more pixels

            # Prefer PNG with transparency
            if f.lower().endswith('.png') and img.mode == 'RGBA':
                score += 50
            elif f.lower().endswith('.png'):
                score += 30

            # Prefer landscape for headers, square for favicon
            aspect_ratio = w / h
            if 1.5 <= aspect_ratio <= 3:  # Header logo
                score += 20
            elif 0.9 <= aspect_ratio <= 1.1:  # Square favicon
                score += 10

            logos.append({
                'filename': f,
                'path': img_path,
                'width': w,
                'height': h,
                'size_kb': size_kb,
                'format': img.format,
                'mode': img.mode,
                'aspect_ratio': f"{w//gcd(w,h)}:{h//gcd(w,h)}",
                'score': score
            })

    if not logos:
        print("⚠️  No logos found in photo-bank/")
        return None

    # Select best logo
    best_logo = max(logos, key=lambda x: x['score'])

    # Copy to branding directory
    os.makedirs('src/assets/images/branding', exist_ok=True)
    dest = 'src/assets/images/branding/logo.png'

    # Convert to PNG if needed
    if best_logo['format'] != 'PNG':
        img = Image.open(best_logo['path'])
        img = img.convert('RGBA')
        img.save(dest, 'PNG')
    else:
        import shutil
        shutil.copy2(best_logo['path'], dest)

    print(f"✅ Selected logo: {best_logo['filename']}")
    print(f"   Dimensions: {best_logo['width']}x{best_logo['height']}")
    print(f"   Format: {best_logo['mode']}")
    print(f"   Copied to: {dest}")

    return best_logo

# Run the selection
best = find_best_logo()
```

### Logo Catalog Entry

Update `_catalog.json` with logo entry:

```json
{
  "branding": {
    "logo": {
      "id": "logo-primary",
      "original_filename": "logo-color.png",
      "source": "photo-bank/logo-color.png",
      "destination": "src/assets/images/branding/logo.png",
      "category": "branding",
      "width": 600,
      "height": 150,
      "aspect_ratio": "4:1",
      "file_size_kb": 85,
      "format": "png",
      "mode": "RGBA",
      "used_in": ["header", "footer", "meta-og"],
      "role": "primary-brand-logo",
      "score": 245,
      "notes": "High-resolution logo with transparency, landscape format suitable for header use"
    }
  }
}
```

## Step 4: Generate _catalog.json

```json
{
  "generated_at": "2026-02-17T10:00:00Z",
  "photo_bank_path": "photo-bank/",
  "images_path": "src/assets/images/",
  "total_images": 12,
  "images": [
    {
      "id": "hero-main",
      "original_filename": "hero-office.jpg",
      "source": "photo-bank/hero-office.jpg",
      "destination": "src/assets/images/hero/hero-office.jpg",
      "category": "hero",
      "width": 1920,
      "height": 1080,
      "aspect_ratio": "16:9",
      "file_size_kb": 342,
      "format": "jpg",
      "used_in": [],
      "role": "",
      "placeholder": false,
      "notes": "Wide office exterior shot"
    }
  ],
  "placeholders_needed": [
    {
      "role": "hero-background",
      "page": "index.astro",
      "recommended_dimensions": "1920x1080",
      "recommended_aspect_ratio": "16:9",
      "description": "Needs: impressive wide shot related to company"
    }
  ]
}
```

## Step 5: Dimension-Aware Placement

When the page-builder needs an image for a specific slot:

1. **Determine slot requirements:**
   - Hero backgrounds: min 1600px wide, 16:9 or wider
   - Team headshots: min 400x400, square (1:1) preferred
   - Service cards: min 600px wide, 4:3 or 3:2
   - Gallery thumbnails: min 400px, flexible
   - Testimonial avatars: min 100x100, square
   - Logo/icon: flexible, any size

2. **Find best matching photo from catalog** based on:
   - Category match
   - Aspect ratio compatibility
   - Sufficient resolution (don't upscale)

3. **Update catalog** with `used_in` and `role` fields

4. **If no suitable photo exists:**
   - Add entry to `placeholders_needed` array
   - In the page, use a solid-color div or gradient matching design system
   - Add an HTML comment: `<!-- PLACEHOLDER: replace with {description} -->`
   - NEVER use stock photo URLs or external placeholder services

## Replacement Guide

After the site is built, provide the user with a replacement checklist:

```markdown
## Photos to Replace

### Hero Images
- [ ] `src/assets/images/hero/hero-office.jpg` (1920x1080, 16:9)
      Used on: Homepage hero
      Current: Placeholder gradient
      Need: Wide shot of company office or related imagery

### Team Photos  
- [ ] `src/assets/images/team/team-john.jpg` (800x800, 1:1)
      Used on: Team page, About page sidebar
      Current: Using photo from photo-bank
      Need: Professional headshot, square crop

### How to Replace
1. Prepare your photo at the recommended dimensions
2. Name it exactly as shown above
3. Drop it into the exact path shown
4. Run `npm run build` to regenerate optimized versions
5. Astro will auto-generate WebP/AVIF and responsive sizes
```

## Rules

1. **NEVER modify original photos in photo-bank/.** Always copy, never move or edit.
2. **ALWAYS measure before placing.** A 400x400 image in a 1920px hero slot = blurry disaster.
3. **Astro handles optimization.** Don't manually resize or convert formats. Just provide the originals at sufficient resolution.
4. **Keep the catalog updated.** Every image addition or change must be reflected in _catalog.json.
5. **Descriptive IDs.** Use kebab-case IDs that describe the content: `team-john-doe`, `hero-about-page`, `service-consulting`.
