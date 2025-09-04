#!/usr/bin/env python3
"""
Launcher script for Radiation Physics Education Apps
"""

import subprocess
import sys
import os

def main():
    print("🚀 Radiation Physics Interactive Education Apps")
    print("=" * 50)

    apps = {
        "1": {
            "name": "Main Navigation Page",
            "file": "main.py",
            "description": "Choose from all available physics concepts"
        },
        "2": {
            "name": "Photoelectric Effect",
            "file": "apps/photoelectric/photoelectric_app.py",
            "description": "Einstein's quantum theory of light"
        },
        "3": {
            "name": "Compton Scattering",
            "file": "apps/compton_scattering/compton_app.py",
            "description": "Quantum scattering of photons by electrons"
        },
        "4": {
            "name": "Pair Production",
            "file": "apps/pair_production/pair_app.py",
            "description": "Photon conversion to electron-positron pairs"
        }
    }

    while True:
        print("\nAvailable Applications:")
        for key, app in apps.items():
            print(f"{key}. {app['name']}")
            print(f"   {app['description']}")

        print("\n0. Exit")

        choice = input("\nSelect an application to run (0-4): ").strip()

        if choice == "0":
            print("Goodbye! 👋")
            break

        if choice in apps:
            app = apps[choice]
            print(f"\nStarting {app['name']}...")
            print("The app will open in your default web browser.")
            print("Press Ctrl+C in this terminal to stop the app.\n")

            try:
                # Run streamlit app using uv
                cmd = ["uv", "run", "streamlit", "run", app["file"]]
                subprocess.run(cmd)
            except KeyboardInterrupt:
                print(f"\n{app['name']} stopped.")
            except Exception as e:
                print(f"Error running {app['name']}: {e}")
        else:
            print("Invalid choice. Please select 0-4.")

if __name__ == "__main__":
    main()
