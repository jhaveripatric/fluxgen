# FLUXGEN DIGITAL CONTACT CARDS - CUSTOMIZATION GUIDE

## 📋 WHAT YOU HAVE

✅ Master HTML template: `contact-card-template.html`
✅ Beautiful, responsive design
✅ vCard download functionality
✅ Google Analytics tracking
✅ Mobile-optimized

---

## 🎯 CUSTOMIZATION FOR EACH CO-FOUNDER

Create 4 versions of the HTML file, one for each person:

### 1️⃣ **Pratik Jhaveri** (Founder & CTO)
**Filename:** `pratik.html`
**URL:** `fluxgenindustries.ca/contact/pratik`

**Replace these values:**
```javascript
Line 7: <title>Pratik Jhaveri - FluxGen Industries</title>
Line 101: <div class="name">Pratik Jhaveri</div>
Line 102: <div class="title">Founder & Chief Technology Officer</div>
Line 113: <a href="tel:+14031234567">+1 (403) 123-4567</a>
Line 124: <a href="mailto:pratik@fluxgenindustries.ca">pratik@fluxgenindustries.ca</a>
Line 159: <a href="https://www.linkedin.com/in/pratikjhaveri" target="_blank">linkedin.com/in/pratikjhaveri</a>

vCard section (line 200-210):
FN:Pratik Jhaveri
N:Jhaveri;Pratik;;;
TITLE:Founder & Chief Technology Officer
TEL;TYPE=WORK,VOICE:+14031234567
EMAIL;TYPE=WORK:pratik@fluxgenindustries.ca
link.download = 'Pratik-Jhaveri-FluxGen.vcf';
```

---

### 2️⃣ **Arpan Patel** (Operations Director)
**Filename:** `arpan.html`
**URL:** `fluxgenindustries.ca/contact/arpan`

**Replace these values:**
```javascript
Line 7: <title>Arpan Patel - FluxGen Industries</title>
Line 101: <div class="name">Arpan Patel</div>
Line 102: <div class="title">Operations Director</div>
Line 113: <a href="tel:+14031234568">+1 (403) 123-4568</a>  // Change phone
Line 124: <a href="mailto:arpan@fluxgenindustries.ca">arpan@fluxgenindustries.ca</a>
Line 159: <a href="https://www.linkedin.com/in/arpanpatel" target="_blank">linkedin.com/in/arpanpatel</a>

vCard section:
FN:Arpan Patel
N:Patel;Arpan;;;
TITLE:Operations Director
TEL;TYPE=WORK,VOICE:+14031234568
EMAIL;TYPE=WORK:arpan@fluxgenindustries.ca
link.download = 'Arpan-Patel-FluxGen.vcf';
```

---

### 3️⃣ **Abhishek Patel** (Supply Chain Director)
**Filename:** `abhishek.html`
**URL:** `fluxgenindustries.ca/contact/abhishek`

**Replace these values:**
```javascript
Line 7: <title>Abhishek Patel - FluxGen Industries</title>
Line 101: <div class="name">Abhishek Patel</div>
Line 102: <div class="title">Supply Chain Director</div>
Line 113: <a href="tel:+14031234569">+1 (403) 123-4569</a>
Line 124: <a href="mailto:abhishek@fluxgenindustries.ca">abhishek@fluxgenindustries.ca</a>
Line 159: <a href="https://www.linkedin.com/in/abhishekpatel" target="_blank">linkedin.com/in/abhishekpatel</a>

vCard section:
FN:Abhishek Patel
N:Patel;Abhishek;;;
TITLE:Supply Chain Director
TEL;TYPE=WORK,VOICE:+14031234569
EMAIL;TYPE=WORK:abhishek@fluxgenindustries.ca
link.download = 'Abhishek-Patel-FluxGen.vcf';
```

---

### 4️⃣ **Bhargav Patel** (Quality & Compliance Director)
**Filename:** `bhargav.html`
**URL:** `fluxgenindustries.ca/contact/bhargav`

**Replace these values:**
```javascript
Line 7: <title>Bhargav Patel - FluxGen Industries</title>
Line 101: <div class="name">Bhargav Patel</div>
Line 102: <div class="title">Quality & Compliance Director</div>
Line 113: <a href="tel:+14031234570">+1 (403) 123-4570</a>
Line 124: <a href="mailto:bhargav@fluxgenindustries.ca">bhargav@fluxgenindustries.ca</a>
Line 159: <a href="https://www.linkedin.com/in/bhargavpatel" target="_blank">linkedin.com/in/bhargavpatel</a>

vCard section:
FN:Bhargav Patel
N:Patel;Bhargav;;;
TITLE:Quality & Compliance Director
TEL;TYPE=WORK,VOICE:+14031234570
EMAIL;TYPE=WORK:bhargav@fluxgenindustries.ca
link.download = 'Bhargav-Patel-FluxGen.vcf';
```

---

## 🔧 ADDING YOUR LOGO (Optional)

**Option 1: Replace text logo with image**

Replace line 95-97:
```html
<!-- OLD: Text logo -->
<div style="margin-bottom: 20px; font-size: 36px; font-weight: 700; color: white; letter-spacing: 2px;">
    FLUXGEN
</div>

<!-- NEW: Image logo -->
<img src="/assets/fluxgen-logo-white.png" alt="FluxGen Industries" class="logo">
```

Upload your white version of the logo to Cloudflare Pages under `/assets/` folder.

---

## 📊 GOOGLE ANALYTICS SETUP

### Step 1: Create GA4 Property
1. Go to [analytics.google.com](https://analytics.google.com)
2. Create new property: "FluxGen Digital Cards"
3. Copy your **Measurement ID** (format: `G-XXXXXXXXXX`)

### Step 2: Replace in HTML
Find line 10-11 in each HTML file:
```javascript
gtag('config', 'G-XXXXXXXXXX'); // Replace with your GA4 Measurement ID
```

Replace `G-XXXXXXXXXX` with your actual ID (e.g., `G-ABC123DEF4`)

### Step 3: What You'll Track
✅ Page views (automatic)
✅ vCard downloads (tracked via custom event)
✅ Website button clicks (can add tracking)
✅ Time on page
✅ Geographic location
✅ Device type

---

## 📱 WHAT EACH CONTACT CARD WILL SHOW

When someone scans your QR code or visits the link:

1. **Beautiful landing page** with:
   - FluxGen branding
   - Your name, title, company
   - Phone, email, website, location, LinkedIn
   - Professional gradient design

2. **Two action buttons:**
   - "Save to Contacts" → Downloads vCard file
   - "Visit Website" → Opens fluxgenindustries.ca

3. **Mobile responsive** — works perfectly on phones

4. **Analytics tracking** — you see who viewed it and when

---

## 🎨 COLOR CUSTOMIZATION (Optional)

Current colors:
- Primary blue: `#3498db`
- Dark blue: `#2c3e50`
- Background: Dark gradient

To change colors, find these lines in CSS:

**Primary button color:**
Line 145: `background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);`

**Header background:**
Line 46: `background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);`

**Accent bar (top):**
Line 56: `background: linear-gradient(90deg, #e74c3c, #f39c12, #3498db);`

---

## ✅ QUICK CHECKLIST

Before deploying:

- [ ] Customized all 4 HTML files (pratik.html, arpan.html, abhishek.html, bhargav.html)
- [ ] Updated phone numbers for each person
- [ ] Updated email addresses
- [ ] Updated LinkedIn URLs
- [ ] Added Google Analytics Measurement ID
- [ ] Tested vCard download on mobile phone
- [ ] (Optional) Replaced text logo with image

---

## 📂 FILE STRUCTURE FOR DEPLOYMENT

```
fluxgenindustries.ca/
├── contact/
│   ├── pratik.html       → fluxgenindustries.ca/contact/pratik
│   ├── arpan.html        → fluxgenindustries.ca/contact/arpan
│   ├── abhishek.html     → fluxgenindustries.ca/contact/abhishek
│   └── bhargav.html      → fluxgenindustries.ca/contact/bhargav
└── assets/               (optional)
    └── fluxgen-logo-white.png
```

---

## 🚀 NEXT STEP

See `CLOUDFLARE-DEPLOYMENT.md` for hosting instructions!
