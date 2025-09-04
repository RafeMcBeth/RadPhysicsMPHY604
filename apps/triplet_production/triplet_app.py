"""
Interactive Triplet Production app
"""

import streamlit as st
import sys
import os

# Add the project root to the path to import shared modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from shared.plotting_utils import create_triplet_production_plot


def main():
    st.set_page_config(
        page_title="Triplet Production",
        page_icon="3️⃣",
        layout="wide"
    )

    st.title("3️⃣ Triplet Production")
    st.markdown("*Photon converts to e⁻e⁺ plus atomic electron recoil (threshold 2.044 MeV)*")

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
    maxE = st.sidebar.slider("Max Photon Energy (MeV)", 5.0, 50.0, 20.0, 1.0)

    st.subheader("Energy Budget Above Threshold")
    fig = create_triplet_production_plot(max_energy=maxE)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.subheader("Notes")
    st.markdown(
        """
        - Occurs at higher energies than pair production in nuclear field.
        - Competes with pair production; cross-sections material dependent.
        - Shown here as a schematic energy-sharing model for education.
        """
    )


if __name__ == "__main__":
    main()


