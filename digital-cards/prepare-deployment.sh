#!/bin/bash

# FluxGen Contact Cards - Deployment Preparation Script
# This script creates a ready-to-upload folder for Cloudflare Pages

echo "🚀 FluxGen Contact Cards - Deployment Preparation"
echo "=================================================="
echo ""

# Create deployment directory
DEPLOY_DIR="$HOME/Desktop/fluxgen-contact-cards-deploy"
echo "📁 Creating deployment directory at: $DEPLOY_DIR"
mkdir -p "$DEPLOY_DIR"
mkdir -p "$DEPLOY_DIR/static/images/optimized"

# Copy HTML files
echo "📄 Copying HTML files..."
cp "/Users/pratikjhaveri/FluxGen/digital-cards/pratik.html" "$DEPLOY_DIR/"
cp "/Users/pratikjhaveri/FluxGen/digital-cards/arpan.html" "$DEPLOY_DIR/"
cp "/Users/pratikjhaveri/FluxGen/digital-cards/abhishek.html" "$DEPLOY_DIR/"
cp "/Users/pratikjhaveri/FluxGen/digital-cards/bhargav.html" "$DEPLOY_DIR/"

# Copy logo files
echo "🎨 Copying logo files..."
cp "/Users/pratikjhaveri/FluxGen/repo/app/static/images/optimized/fluxgen-logo-full-header.png" "$DEPLOY_DIR/static/images/optimized/"
cp "/Users/pratikjhaveri/FluxGen/repo/app/static/images/optimized/fluxgen-logo-monogram-footer.png" "$DEPLOY_DIR/static/images/optimized/"

# Create a simple README for the deployment folder
cat > "$DEPLOY_DIR/README.txt" << 'EOF'
FLUXGEN CONTACT CARDS - READY FOR DEPLOYMENT
=============================================

This folder contains everything you need to deploy to Cloudflare Pages.

UPLOAD INSTRUCTIONS:
1. Go to https://dash.cloudflare.com
2. Navigate to Workers & Pages
3. Click "Create application" → "Pages" → "Upload assets"
4. Drag this entire folder
5. Project name: fluxgen-contact-cards
6. Click "Deploy site"

LIVE URLS (after deployment):
- https://fluxgen-contact-cards.pages.dev/pratik.html
- https://fluxgen-contact-cards.pages.dev/arpan.html
- https://fluxgen-contact-cards.pages.dev/abhishek.html
- https://fluxgen-contact-cards.pages.dev/bhargav.html

NEXT STEPS:
1. Test all URLs
2. Add Google Analytics ID (replace G-XXXXXXXXXX in each HTML file)
3. Connect custom domain (fluxgenindustries.ca)
4. Generate QR codes

For help: See CLOUDFLARE-DIRECT-UPLOAD-GUIDE.md
EOF

# Create file list
echo ""
echo "✅ Deployment folder created successfully!"
echo ""
echo "📋 Files included:"
echo "  ├── pratik.html"
echo "  ├── arpan.html"
echo "  ├── abhishek.html"
echo "  ├── bhargav.html"
echo "  ├── README.txt"
echo "  └── static/"
echo "      └── images/"
echo "          └── optimized/"
echo "              ├── fluxgen-logo-full-header.png"
echo "              └── fluxgen-logo-monogram-footer.png"
echo ""
echo "📍 Location: $DEPLOY_DIR"
echo ""
echo "🚀 NEXT STEP:"
echo "  1. Open Finder and go to your Desktop"
echo "  2. You'll see a folder called 'fluxgen-contact-cards-deploy'"
echo "  3. Follow the instructions in CLOUDFLARE-DIRECT-UPLOAD-GUIDE.md"
echo ""
echo "✨ Ready for Cloudflare Pages upload!"
