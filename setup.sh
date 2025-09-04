#!/bin/bash
# Setup script for Radiation Physics Education Apps
# Run this after moving to Mac with uv installed

echo "🚀 Setting up Radiation Physics Education Apps with uv"

# Install dependencies
echo "📦 Installing dependencies..."
uv sync

# Make scripts executable
chmod +x run_apps.py

echo "✅ Setup complete!"
echo ""
echo "To run the applications:"
echo "  uv run python run_apps.py    # Interactive launcher"
echo "  uv run radphysics            # Direct script (when configured)"
echo "  uv run streamlit run main.py # Main navigation page"
echo ""
echo "Individual apps:"
echo "  uv run streamlit run apps/photoelectric/photoelectric_app.py"
echo "  uv run streamlit run apps/compton_scattering/compton_app.py"
echo "  uv run streamlit run apps/pair_production/pair_app.py"
