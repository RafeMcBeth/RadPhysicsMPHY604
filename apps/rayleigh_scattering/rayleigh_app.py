"""
Interactive Rayleigh (coherent) scattering app
"""

import streamlit as st
import sys
import os

# Add the project root to the path to import shared modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from shared.plotting_utils import create_rayleigh_scattering_plot


def main():
    st.set_page_config(
        page_title="Rayleigh Scattering",
        page_icon="🟢",
        layout="wide"
    )

    st.title("🟢 Rayleigh Scattering (Coherent)")
    st.markdown("*Elastic scattering with no energy loss; forward-peaked for high Z and E*")

    # Navigation back to home
    col_home, _ = st.columns([1, 4])
    with col_home:
        if st.button("🏠 Home", use_container_width=True):
            st.info("💡 To return to the main navigation:")
            st.markdown(
                """
                **Navigation Options:**
                - **Quick way**: `uv run python run_single_app.py main`
                - **Full launcher**: `uv run python run_apps.py`
                - **Direct**: `uv run streamlit run main.py`
                """
            )

    st.sidebar.header("Parameters")
    energy_keV = st.sidebar.slider("Photon Energy (keV)", 20.0, 150.0, 60.0, 5.0)
    Z = st.sidebar.slider("Atomic Number (Z)", 1, 82, 13, 1)

    st.subheader("Angular Distribution (schematic)")
    fig = create_rayleigh_scattering_plot(energy_keV=energy_keV, atomic_number=Z)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.subheader("Clinical Context")
    st.markdown(
        """
        - Contributes to low-angle scatter in diagnostic imaging (adds to background).
        - More pronounced in high-Z materials and increases with photon energy.
        - Coexists with Compton scattering; exact modeling requires form factors.
        """
    )


if __name__ == "__main__":
    main()


