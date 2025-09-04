"""
Interactive Thomson (classical) scattering app
"""

import streamlit as st
import sys
import os

# Add the project root to the path to import shared modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from shared.plotting_utils import create_thomson_scattering_plot


def main():
    st.set_page_config(
        page_title="Thomson Scattering",
        page_icon="📐",
        layout="wide"
    )

    st.title("📐 Thomson Scattering (Classical)")
    st.markdown("*Elastic scattering of low-energy photons by free electrons*")

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

    st.subheader("Angular Distribution")
    st.caption("Normalized intensity: I(θ) ∝ 1 + cos²θ")
    fig = create_thomson_scattering_plot()
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.subheader("Clinical Context")
    st.markdown(
        """
        - Valid in the low-energy limit where photon energy ≪ electron rest mass energy.
        - Provides intuition for scattering backgrounds and detector angular response.
        - Complements Compton scattering which dominates at diagnostic to MV energies.
        """
    )


if __name__ == "__main__":
    main()


