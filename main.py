"""
Main navigation page for Radiation Physics Interactive Education Apps
"""

import streamlit as st
import subprocess
import sys
import os

# Set page configuration
st.set_page_config(
    page_title="Radiation Physics Education",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    st.title("⚛️ Radiation Physics Interactive Education")
    st.markdown("### Graduate Level Photon-Matter Interactions")

    st.markdown("""
    Welcome to an interactive learning experience covering fundamental concepts
    in radiation physics. Choose from the following topics to explore:
    """)

    # Create columns for the main topics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("📸 Photoelectric Effect")
        st.markdown("""
        **Einstein's quantum theory of light**
        - Photon energy and work function
        - Threshold frequency dependence
        - Kinetic energy calculations
        """)

        if st.button("Explore Photoelectric Effect", key="photoelectric", use_container_width=True):
            run_app("apps/photoelectric/photoelectric_app.py")

    with col2:
        st.subheader("🔄 Compton Scattering")
        st.markdown("""
        **Quantum scattering of photons**
        - Wavelength shift with angle
        - Energy-momentum conservation
        - Compton wavelength significance
        """)

        if st.button("Explore Compton Scattering", key="compton", use_container_width=True):
            run_app("apps/compton_scattering/compton_app.py")

    with col3:
        st.subheader("⚡ Pair Production")
        st.markdown("""
        **Photon conversion to matter**
        - Energy threshold requirements
        - Conservation laws
        - Nuclear field effects
        """)

        if st.button("Explore Pair Production", key="pair", use_container_width=True):
            run_app("apps/pair_production/pair_app.py")

    # Educational context section
    st.markdown("---")
    st.subheader("🎓 Learning Objectives")

    st.markdown("""
    These interactive applications are designed to help you:

    1. **Visualize** fundamental quantum processes
    2. **Calculate** physical quantities in real-time
    3. **Explore** parameter dependencies and relationships
    4. **Understand** conservation principles
    5. **Connect** theoretical concepts with practical applications

    Each app includes interactive controls, real-time calculations, and
    educational visualizations to enhance your understanding of radiation physics.
    """)

    # Technical details
    with st.expander("🔧 Technical Implementation"):
        st.markdown("""
        **Built with Python and Modern Web Technologies:**
        - Streamlit for interactive web interfaces
        - NumPy and SciPy for numerical calculations
        - Plotly for dynamic visualizations
        - Matplotlib for static plots
        - Physics constants from CODATA 2022

        **Educational Features:**
        - Real-time parameter adjustment
        - Multiple visualization types
        - Educational annotations
        - Interactive geometry demonstrations
        """)

def run_app(app_path):
    """Run a specific Streamlit app"""
    try:
        # For Windows, we need to use different approach
        if sys.platform == "win32":
            cmd = [sys.executable, "-m", "streamlit", "run", app_path]
        else:
            cmd = ["streamlit", "run", app_path]

        st.info(f"Starting {app_path}... Please wait.")
        subprocess.Popen(cmd)
        st.success(f"App started! Check your browser for the new window.")

    except Exception as e:
        st.error(f"Error starting app: {str(e)}")

if __name__ == "__main__":
    main()
