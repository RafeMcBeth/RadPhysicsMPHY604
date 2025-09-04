"""
Interactive Photodisintegration (Photonuclear) app
"""

import streamlit as st
import sys
import os

# Add the project root to the path to import shared modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from shared.plotting_utils import create_photodisintegration_plot


def main():
    st.set_page_config(
        page_title="Photodisintegration",
        page_icon="🧩",
        layout="wide"
    )

    st.title("🧩 Photodisintegration (Photonuclear)")
    st.markdown("*Photon induces nuclear reaction; giant dipole resonance ~10–20 MeV*")

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
    maxE = st.sidebar.slider("Max Photon Energy (MeV)", 10.0, 80.0, 30.0, 1.0)

    st.subheader("Relative Cross-section (schematic)")
    fig = create_photodisintegration_plot(max_energy=maxE)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.subheader("Clinical/Physics Notes")
    st.markdown(
        """
        - Relevant for high-energy linac head leakage and activation products.
        - Threshold varies by nucleus; giant dipole resonance typically 10–20 MeV.
        - This is a schematic educational visualization, not a database cross-section.
        """
    )


if __name__ == "__main__":
    main()


