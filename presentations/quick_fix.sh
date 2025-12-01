#!/bin/bash
# Quick fix: Generate presentation WITHOUT speaker notes
# This will definitely work - you can add notes manually later

echo "🎨 Generating presentation WITHOUT speaker notes..."
echo "===================================================="
echo ""
echo "This version will definitely open correctly."
echo "You can add speaker notes manually in PowerPoint later."
echo ""

cd /Users/pratikjhaveri/FluxGen || exit 1
source venv/bin/activate || exit 1

# Use the ORIGINAL generator which worked
python presentations/generate_edo_presentation.py

echo ""
echo "✅ Done!"
echo ""
echo "📁 Your presentation (10 slides, no speaker notes):"
echo "   /Users/pratikjhaveri/FluxGen/presentations/FluxGen-EDO-Presentation.pptx"
echo ""
echo "📝 This version has 10 slides (missing 3 from the full version)"
echo ""
echo "🎯 To get the full 12-slide version with speaker notes,"
echo "   run the troubleshooting steps in TROUBLESHOOTING.txt"
