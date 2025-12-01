#!/bin/bash
# Generate COMPLETE FluxGen EDO Presentation with Speaker Notes

echo "🎨 Generating COMPLETE FluxGen EDO Presentation..."
echo "=================================================="
echo ""

cd /Users/pratikjhaveri/FluxGen || exit 1
source venv/bin/activate || exit 1

python presentations/generate_edo_presentation_COMPLETE.py

echo ""
echo "✅ COMPLETE!"
echo ""
echo "📁 Your presentation with speaker notes is ready:"
echo "   /Users/pratikjhaveri/FluxGen/presentations/FluxGen-EDO-Presentation-COMPLETE.pptx"
echo ""
echo "📊 What's included:"
echo "   • 12 professional slides (vs 10 in original)"
echo "   • 3 NEW slides: Economic Alignment, Risk Mitigation, National Prestige"
echo "   • Comprehensive speaker notes for all slides"
echo "   • 15-minute presentation timing guide"
echo ""
echo "🎯 To view speaker notes:"
echo "   PowerPoint: View → Notes"
echo "   Keynote: View → Show Presenter Notes"
echo "   Google Slides: View → Show speaker notes"
