#!/bin/bash
# FluxGen EDO Presentation Setup and Generation Script

echo "🔧 FluxGen EDO Presentation Generator"
echo "======================================"
echo ""

# Navigate to FluxGen directory
cd /Users/pratikjhaveri/FluxGen || exit 1

# Activate virtual environment
echo "📦 Activating virtual environment..."
source venv/bin/activate || exit 1

# Install python-pptx
echo "📥 Installing python-pptx..."
pip install python-pptx --quiet

# Run the presentation generator
echo ""
echo "🎨 Generating PowerPoint presentation..."
python presentations/generate_edo_presentation.py

echo ""
echo "✅ DONE!"
echo ""
echo "📁 Your presentation is ready at:"
echo "   /Users/pratikjhaveri/FluxGen/presentations/FluxGen-EDO-Presentation.pptx"
echo ""
echo "🎯 Next steps:"
echo "   1. Open the .pptx file in PowerPoint or Keynote"
echo "   2. Upload to Google Slides: File → Import slides"
echo "   3. Review and present!"
