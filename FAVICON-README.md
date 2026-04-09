# Veil Favicon — Logo SVG Implementation

**Date:** April 10, 2026  
**Status:** ✅ LIVE

---

## What Was Done

### 1. Extracted Logo SVG
From the Veil landing page HTML, extracted the iconic "V" logo:
```svg
<path d="M0 0 L10 22 L14 14 L18 22 L28 0 L23 0 L14 16 L5 0 Z" fill="#4f52c8"/>
```

### 2. Created Favicon Files
- **favicon.svg** — SVG favicon (32x32)
  - Modern browsers render this natively
  - Scales perfectly at any size
  - Uses indigo color (#4f52c8)
  - Dark background (#07080f)

- **veil-logo.svg** — Source logo (larger, for reference)
  - Original size (28x22)
  - Can be used for other purposes

### 3. Updated HTML
Changed `index.html` to link to the new favicon:
```html
<link rel="icon" type="image/svg+xml" href="/favicon.svg"/>
<link rel="icon" type="image/x-icon" href="/favicon.ico"/>
```

Browsers now use the SVG version (modern) and fall back to ICO (legacy).

### 4. Deployed
Restarted veil-landing service. Favicon is now live.

---

## How It Looks

When you visit **https://veil.aircade.xyz**, the browser tab shows:
- A small purple "V" logo
- On dark background
- Matches Veil's brand identity

---

## Files

```
~/projects/veil-landing/
├── index.html            ← Updated (favicon link)
├── favicon.svg           ← NEW (32x32 SVG)
├── veil-logo.svg         ← NEW (28x22 source)
├── serve.js              ← Serves both
└── FAVICON-README.md     ← This file
```

---

## Browsers Support

✅ Chrome, Firefox, Safari, Edge (all modern versions)  
✅ Mobile browsers (iOS Safari, Chrome Mobile)  
✅ Falls back to favicon.ico if SVG not supported

---

## Updating in Future

If you change the logo:

1. **Edit `veil-logo.svg`** (source file)
2. **Extract path** and update `favicon.svg`
3. **Restart service:** `systemctl --user restart veil-landing.service`
4. **Clear browser cache** if needed: Ctrl+Shift+Del

---

## Technology

- **Format:** SVG (Scalable Vector Graphics)
- **Size:** 32x32px nominal (scales to any size)
- **Colors:** Indigo (#4f52c8) on dark (#07080f)
- **Weight:** ~320 bytes (extremely lightweight)

---

Created by **Zaia 🌙** — April 10, 2026
