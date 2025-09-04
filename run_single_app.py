#!/usr/bin/env python3
"""
Standalone runner for individual Radiation Physics Education Apps
Usage: uv run python run_single_app.py <app_name>
"""

import subprocess
import sys
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: uv run python run_single_app.py <app_name>")
        print("Available apps:")
        print("  photoelectric - Photoelectric Effect")
        print("  compton - Compton Scattering")
        print("  pair - Pair Production")
        print("  thomson - Thomson Scattering")
        print("  rayleigh - Rayleigh Scattering")
        print("  triplet - Triplet Production")
        print("  photodisintegration - Photonuclear")
        print("  main - Main Navigation Page")
        return

    app_name = sys.argv[1].lower()

    app_paths = {
        "photoelectric": "apps/photoelectric/photoelectric_app.py",
        "compton": "apps/compton_scattering/compton_app.py",
        "pair": "apps/pair_production/pair_app.py",
        "thomson": "apps/thomson_scattering/thomson_app.py",
        "rayleigh": "apps/rayleigh_scattering/rayleigh_app.py",
        "triplet": "apps/triplet_production/triplet_app.py",
        "photodisintegration": "apps/photodisintegration/photo_nuclear_app.py",
        "main": "main.py"
    }

    if app_name not in app_paths:
        print(f"Unknown app: {app_name}")
        print("Available apps: photoelectric, compton, pair, thomson, rayleigh, triplet, photodisintegration, main")
        return

    app_path = app_paths[app_name]

    print(f"🚀 Starting {app_name} app...")
    print("The app will open in your default web browser.")
    print("Press Ctrl+C to stop the app.\n")

    try:
        # Run with uv
        cmd = ["uv", "run", "streamlit", "run", app_path]
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print(f"\n{app_name} app stopped.")
    except Exception as e:
        print(f"Error running {app_name}: {e}")

if __name__ == "__main__":
    main()
