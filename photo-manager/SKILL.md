---
name: photo-manager
description: Catalogs photos from photo-bank/, records dimensions, copies to organized src/assets/images/ folders, and generates _catalog.json. Use whenever photos need to be processed, cataloged, or placed in the website.
---

# Photo Manager Skill

Handle all image assets — catalog, organize, and track for easy replacement.

## Core Principle

**NEVER use a photo without first checking its dimensions.** Every image placement must be dimension-aware.

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
- `client-*`, `logo-*`, `testimonial-*` → `testimonials/`
- Anything else → `misc/`

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
