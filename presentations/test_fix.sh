#!/bin/bash
# Test if python-pptx is working correctly

echo "🔍 Testing PowerPoint generation..."
echo "==================================="
echo ""

cd /Users/pratikjhaveri/FluxGen || exit 1
source venv/bin/activate || exit 1

echo "📦 Checking python-pptx version..."
python -c "import pptx; print(f'python-pptx version: {pptx.__version__}')" 2>&1

echo ""
echo "🎨 Generating TEST presentation (1 slide only)..."
python presentations/test_presentation.py

echo ""
echo "✅ Test complete!"
echo ""
echo "📁 Test file created:"
echo "   /Users/pratikjhaveri/FluxGen/presentations/FluxGen-EDO-Presentation-COMPLETE.pptx"
echo ""
echo "🎯 NEXT STEP:"
echo "   Try to open the file above."
echo "   If it opens successfully, let me know and I'll generate the full 12-slide version."
echo "   If it still gives an error, send me the error message."
