"""
Interactive Compton Scattering Education App
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
from shared.physics_calculations import compton_scattering, compton_wavelength_max
from shared.plotting_utils import create_compton_scattering_plot, create_3d_scattering_visualization

def main():
    st.set_page_config(
        page_title="Compton Scattering",
        page_icon="🔄",
        layout="wide"
    )

    st.title("🔄 Compton Scattering")
    st.markdown("*Quantum scattering of photons by electrons*")

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

    # Incident photon energy
    incident_energy_mev = st.sidebar.slider(
        "Incident Photon Energy (MeV)",
        min_value=0.1,
        max_value=10.0,
        value=1.0,
        step=0.1
    )

    # Scattering angle
    scattering_angle = st.sidebar.slider(
        "Scattering Angle (degrees)",
        min_value=0,
        max_value=180,
        value=90,
        step=5
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("**Related Interactions**")
    st.sidebar.caption("Explore other photon-atom interactions:")
    if st.sidebar.button("Thomson (Classical)"):
        st.session_state['nav_hint'] = 'thomson'
    if st.sidebar.button("Rayleigh (Coherent)"):
        st.session_state['nav_hint'] = 'rayleigh'

    # Calculate Compton scattering parameters
    result = compton_scattering(incident_energy_mev * 1000, scattering_angle)  # Convert MeV to keV

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Scattering Analysis")

        # Create polar plot
        fig = create_compton_scattering_plot(incident_energy_mev, 180)

        # Add current angle marker
        scattered_energy_current = result['scattered_energy'] / 1000  # Convert keV to MeV
        fig.add_trace(go.Scatterpolar(
            r=[scattered_energy_current],
            theta=[scattering_angle],
            mode='markers',
            name='Current Point',
            marker=dict(color='red', size=12, symbol='star')
        ), row=1, col=1)

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Results")

        # Display key parameters
        st.metric("Incident Energy", f"{incident_energy_mev} MeV")
        st.metric("Scattering Angle", f"{scattering_angle}°")
        st.metric("Scattered Energy", f"{result['scattered_energy']:.3f} keV")
        st.metric("Energy Lost", f"{result['energy_lost']:.3f} keV")
        st.metric("Wavelength Change", f"{result['wavelength_change']:.3f} Å")

        # Compton wavelength
        st.metric("Compton Wavelength", f"{result['compton_wavelength']:.3f} Å")

        # Show the Compton formula
        st.latex(r"\Delta\lambda = \lambda_C (1 - \cos\theta)")
        lambda_c = result['compton_wavelength']
        delta_lambda = lambda_c * (1 - np.cos(np.radians(scattering_angle)))
        st.latex(f"\\Delta\\lambda = {lambda_c:.3f} \\times (1 - \\cos({scattering_angle}^\\circ)) = {delta_lambda:.3f}\\,\\AA")

        # Maximum wavelength change
        max_change = compton_wavelength_max(incident_energy_mev * 1000)
        st.metric("Max Δλ (180°)", f"{max_change:.3f} Å")

    # 3D Visualization
    st.subheader("3D Scattering Geometry")

    fig_3d = create_3d_scattering_visualization(scattering_angle)
    st.plotly_chart(fig_3d, use_container_width=True)

    # Energy conservation demonstration
    st.subheader("Energy-Momentum Conservation")

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("**Photon Energy Balance:**")
        st.latex(f"E_0 = {incident_energy_mev:.3f}\\,\\text{{MeV}}")
        st.latex(f"E_\\theta = {result['scattered_energy']/1000:.3f}\\,\\text{{MeV}}")
        st.latex(f"E_\\text{{electron}} = {result['recoil_electron_energy']/1000:.3f}\\,\\text{{MeV}}")

        conservation_check = abs(incident_energy_mev - (result['scattered_energy']/1000 + result['recoil_electron_energy']/1000))
        if conservation_check < 0.01:
            st.success("✅ Energy conservation satisfied!")
        else:
            st.warning(f"Energy conservation check: ΔE = {conservation_check:.3f} MeV")

    with col4:
        st.markdown("**Momentum Conservation:**")
        st.latex(r"\vec{p}_\gamma = \vec{p}_{\gamma'} + \vec{p}_e")

        # Calculate momentum components
        p_incident = incident_energy_mev * 1000 / SPEED_OF_LIGHT  # keV/c
        p_scattered = result['scattered_energy'] / SPEED_OF_LIGHT
        p_electron = result['recoil_electron_energy'] / SPEED_OF_LIGHT

        st.metric("Incident momentum", f"{p_incident:.1f} keV/c")
        st.metric("Scattered momentum", f"{p_scattered:.1f} keV/c")
        st.metric("Electron momentum", f"{p_electron:.1f} keV/c")

    # Interactive angle exploration
    st.subheader("Angle Dependence Explorer")

    angles_range = np.linspace(0, 180, 37)  # Every 5 degrees
    energies_scattered = []
    energies_electron = []
    wavelength_changes = []

    for angle in angles_range:
        calc = compton_scattering(incident_energy_mev * 1000, angle)
        energies_scattered.append(calc['scattered_energy'] / 1000)  # MeV
        energies_electron.append(calc['recoil_electron_energy'] / 1000)  # MeV
        wavelength_changes.append(calc['wavelength_change'])

    # Create comprehensive angle plot
    fig_angles = make_subplots(
        rows=2, cols=2,
        subplot_titles=("Scattered Photon Energy", "Electron Kinetic Energy",
                       "Wavelength Change", "Energy Distribution"),
        specs=[[{'type': 'xy'}, {'type': 'xy'}],
               [{'type': 'xy'}, {'type': 'xy'}]]
    )

    # Scattered photon energy
    fig_angles.add_trace(go.Scatter(
        x=angles_range,
        y=energies_scattered,
        mode='lines+markers',
        name='Scattered Photon',
        line=dict(color='blue', width=2)
    ), row=1, col=1)

    # Electron energy
    fig_angles.add_trace(go.Scatter(
        x=angles_range,
        y=energies_electron,
        mode='lines+markers',
        name='Recoil Electron',
        line=dict(color='red', width=2)
    ), row=1, col=2)

    # Wavelength change
    fig_angles.add_trace(go.Scatter(
        x=angles_range,
        y=wavelength_changes,
        mode='lines+markers',
        name='Δλ',
        line=dict(color='green', width=2)
    ), row=2, col=1)

    # Energy distribution
    fig_angles.add_trace(go.Scatter(
        x=angles_range,
        y=[e/energies_scattered[i] for i, e in enumerate(energies_electron)],
        mode='lines+markers',
        name='E_electron/E_photon',
        line=dict(color='purple', width=2)
    ), row=2, col=2)

    # Add current angle markers
    current_idx = int(scattering_angle / 5)
    if current_idx < len(angles_range):
        for i, (row, col) in enumerate([(1,1), (1,2), (2,1), (2,2)]):
            if i == 0:  # Scattered photon
                y_val = energies_scattered[current_idx]
            elif i == 1:  # Electron
                y_val = energies_electron[current_idx]
            elif i == 2:  # Wavelength
                y_val = wavelength_changes[current_idx]
            else:  # Ratio
                y_val = energies_electron[current_idx] / energies_scattered[current_idx]

            fig_angles.add_trace(go.Scatter(
                x=[scattering_angle],
                y=[y_val],
                mode='markers',
                name='Current',
                marker=dict(color='orange', size=10, symbol='star'),
                showlegend=False
            ), row=row, col=col)

    fig_angles.update_layout(height=600, showlegend=True)
    st.plotly_chart(fig_angles, use_container_width=True)

    # Educational content
    st.markdown("---")
    st.subheader("📚 Key Concepts")

    col5, col6 = st.columns(2)

    with col5:
        st.markdown("""
        **Compton Effect:**
        - Photon scatters off free electron
        - Wavelength increases (energy decreases)
        - Maximum shift at 180° scattering
        - Independent of incident photon energy

        **Compton Wavelength:**
        - λ_C = h/(m_e c) = 0.0243 Å
        - Characteristic of electron rest mass
        - Sets the scale for quantum effects
        """)

    with col6:
        st.markdown("""
        **Conservation Laws:**
        - Energy: E₀ = E' + E_electron
        - Momentum: p₀ = p' + p_electron
        - Cannot conserve both classically
        - Requires quantum treatment

        **Applications:**
        - X-ray scattering experiments
        - Medical imaging (Compton cameras)
        - Nuclear physics research
        """)

    # Historical context
    with st.expander("🕰️ Historical Development"):
        st.markdown("""
        **1923: Arthur Compton's Experiment**
        - Used X-rays scattering from graphite
        - Measured wavelength shift vs angle
        - Confirmed quantum prediction

        **Key Evidence:**
        - Wavelength shift independent of target material
        - Shift followed λ_C(1-cosθ) exactly
        - Classical theory failed completely

        **Nobel Prize:** Compton (1927) "for the discovery of the effect named after him"
        """)

if __name__ == "__main__":
    main()
