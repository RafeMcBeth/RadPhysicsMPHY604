"""
Interactive Photoelectric Effect Education App
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import sys
import os

# Add the project root to the path to import shared modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from shared.physics_constants import *
from shared.physics_calculations import photoelectric_effect
from shared.plotting_utils import create_energy_frequency_plot

def main():
    st.set_page_config(
        page_title="Photoelectric Effect",
        page_icon="📸",
        layout="wide"
    )

    st.title("📸 Photoelectric Effect in Medical Physics")
    st.markdown("*Quantum interactions in radiation detection and imaging*")

    # Navigation back to home
    col_home, col_spacer = st.columns([1, 4])
    with col_home:
        if st.button("🏠 Home", use_container_width=True):
            st.info("💡 To return to the main navigation:")
            st.markdown("""
            **Navigation Options:**
            - **Quick way**: `uv run python run_single_app.py main`
            - **Full launcher**: `uv run python run_apps.py`
            - **Direct**: `uv run streamlit run main.py`
            """)

    # Sidebar controls
    st.sidebar.header("Parameters")

    # Material selection
    material = st.sidebar.selectbox(
        "Select Material",
        options=list(WORK_FUNCTIONS.keys()),
        index=list(WORK_FUNCTIONS.keys()).index('Sodium Iodide (NaI)')
    )

    work_function = WORK_FUNCTIONS[material]

    # Photon energy controls
    photon_energy_ev = st.sidebar.slider(
        "Photon Energy (eV)",
        min_value=1.0,
        max_value=50.0,
        value=25.0,
        step=0.5
    )

    # Light intensity (for conceptual understanding)
    intensity = st.sidebar.slider(
        "Light Intensity (relative)",
        min_value=0.1,
        max_value=10.0,
        value=1.0,
        step=0.1
    )

    # Calculate photoelectric effect parameters
    result = photoelectric_effect(photon_energy_ev, work_function)

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Energy Analysis")

        # Create interactive plot
        fig = create_energy_frequency_plot(work_function, 50.0)

        # Add current photon energy marker
        freq_current = photon_energy_ev / (PLANCK_CONSTANT / EV_TO_JOULES) * 1e-14
        fig.add_trace(go.Scatter(
            x=[freq_current],
            y=[photon_energy_ev],
            mode='markers',
            name='Current Photon',
            marker=dict(color='orange', size=12, symbol='star')
        ))

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Results")

        # Display key parameters
        st.metric("Work Function", f"{work_function} eV")
        st.metric("Photon Energy", f"{photon_energy_ev} eV")

        if result['can_eject']:
            st.success("✅ Electron ejection possible!")
            st.metric("Max Kinetic Energy", f"{result['kinetic_energy']:.2f} eV")

            # Show the photoelectric equation
            st.latex(r"E_k = h\nu - \phi")
            st.latex(f"E_k = {photon_energy_ev:.1f} - {work_function:.1f} = {result['kinetic_energy']:.2f}\\,eV")

        else:
            st.error("❌ Insufficient energy for electron ejection")
            st.metric("Energy Deficit", f"{work_function - photon_energy_ev:.2f} eV")

        # Threshold information
        st.subheader("Threshold Values")
        threshold_freq = result['threshold_frequency'] / 1e14  # Convert to 10^14 Hz
        st.metric("Threshold Frequency", f"{threshold_freq:.1f} × 10¹⁴ Hz")

        # Conceptual visualization
        st.subheader("Conceptual Model")

        # Create a simple schematic
        fig_schematic = go.Figure()

        # Metal surface
        fig_schematic.add_shape(
            type="rect",
            x0=-1, y0=-0.5, x1=1, y1=0,
            fillcolor="gray",
            line=dict(color="black", width=2)
        )

        # Photon
        fig_schematic.add_trace(go.Scatter(
            x=[-0.5], y=[0.5],
            mode='markers+text',
            text=['Photon (hν)'],
            textposition="middle right",
            marker=dict(size=20, color='yellow', symbol='star'),
            showlegend=False
        ))

        if result['can_eject']:
            # Ejected electron
            fig_schematic.add_trace(go.Scatter(
                x=[0.5], y=[0.8],
                mode='markers+text',
                text=['Electron (Eₖ)'],
                textposition="middle left",
                marker=dict(size=15, color='blue', symbol='circle'),
                showlegend=False
            ))

            # Energy arrow
            fig_schematic.add_annotation(
                x=0.3, y=0.6,
                ax=0, ay=0.2,
                xref='x', yref='y',
                axref='x', ayref='y',
                showarrow=True,
                arrowhead=3,
                arrowsize=2,
                arrowwidth=3,
                arrowcolor='green'
            )

        fig_schematic.update_layout(
            title="Photoelectric Process",
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            height=300,
            showlegend=False
        )

        st.plotly_chart(fig_schematic, use_container_width=True)

    # Educational content
    st.markdown("---")
    st.subheader("📚 Key Concepts in Medical Physics")

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
        **Einstein's Photoelectric Equation:**
        - Energy conservation: Photon energy = Work function + Kinetic energy
        - All photons of frequency ν have energy hν
        - No time lag between absorption and emission
        - Intensity affects rate, not energy per electron

        **Medical Physics Relevance:**
        - Explains X-ray absorption in detectors and tissues
        - Basis for energy-dependent attenuation in CT
        - Key to understanding detector efficiency
        """)

    with col4:
        st.markdown("""
        **Experimental Observations:**
        - Threshold frequency independent of intensity
        - Maximum kinetic energy depends only on frequency
        - Current proportional to intensity above threshold
        - No electrons emitted below threshold frequency

        **Clinical Applications:**
        - Scintillator response to ionizing radiation
        - X-ray tube target electron emission
        - Radiation detector calibration and efficiency
        - Quality assurance in medical imaging
        """)

    # Medical physics materials explanation
    with st.expander("🏥 Medical Physics Materials Context"):
        st.markdown("""
        **Detector Materials:**
        - **NaI(Tl), CsI(Tl):** Scintillators in gamma cameras and SPECT systems
        - **CdTe, Si, Ge:** Semiconductor detectors for high-resolution spectroscopy
        - Work function determines detector efficiency and energy resolution

        **X-ray Tube Materials:**
        - **Tungsten:** Primary target material for general radiography
        - **Molybdenum, Rhodium:** Optimized for mammography (K-edge filtering)
        - Electron emission properties affect X-ray tube performance

        **Tissue & Phantom Materials:**
        - **Water:** Reference tissue-equivalent material
        - **PMMA, Aluminum:** Common phantom materials for beam characterization
        - Used for quality assurance and treatment planning verification

        **Clinical Relevance:**
        - Photoelectric absorption cross-section ∝ Z³/E³
        - Explains contrast in CT imaging and mammography
        - Critical for radiation therapy dose calculations
        """)

    # Interactive wavelength calculator
    st.subheader("🔍 Wavelength-Energy Calculator")

    wavelength_nm = st.slider(
        "Wavelength (nm)",
        min_value=0.01,
        max_value=1.0,
        value=0.05,
        step=0.01,
        format="%.3f"
    )

    # Convert wavelength to energy
    wavelength_m = wavelength_nm * 1e-9
    energy_calc = (PLANCK_CONSTANT * SPEED_OF_LIGHT) / wavelength_m * JOULES_TO_EV

    st.metric("Corresponding Energy", f"{energy_calc:.2f} eV")

    # Compare with work function
    if energy_calc > work_function:
        st.success(f"This wavelength can eject electrons from {material}!")
        ke_calc = energy_calc - work_function
        st.metric("Kinetic Energy", f"{ke_calc:.2f} eV")
    else:
        deficit = work_function - energy_calc
        st.warning(f"This wavelength is below threshold by {deficit:.2f} eV")

    # Historical context
    with st.expander("🕰️ Historical Development & Medical Applications"):
        st.markdown("""
        **1905: Einstein's Quantum Hypothesis**
        - Proposed that light consists of quanta (photons)
        - Each photon has energy E = hν
        - Explained photoelectric effect completely

        **Key Experimental Evidence:**
        - Lenard's work (1902): Maximum kinetic energy independent of intensity
        - Millikan's experiments (1916): Confirmed Einstein's predictions precisely

        **Nobel Prize:** Einstein (1921) "for his services to Theoretical Physics,
        and especially for his discovery of the law of the photoelectric effect"

        **Medical Physics Applications:**
        - **Radiation Detection:** Scintillators convert X-ray/gamma photons to visible light
        - **CT Imaging:** Photoelectric absorption dominates at diagnostic energies (<100 keV)
        - **X-ray Production:** Electron emission from heated filaments and targets
        - **Quality Control:** Detector calibration using photoelectric principles
        - **Radiation Therapy:** Understanding dose deposition in tissues
        """)

if __name__ == "__main__":
    main()
