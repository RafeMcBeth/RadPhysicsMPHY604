"""
Interactive Pair Production Education App
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
from shared.physics_calculations import pair_production
from shared.plotting_utils import create_pair_production_plot

def main():
    st.set_page_config(
        page_title="Pair Production",
        page_icon="⚡",
        layout="wide"
    )

    st.title("⚡ Pair Production")
    st.markdown("*Photon conversion to electron-positron pairs*")

    # Sidebar controls
    st.sidebar.header("Parameters")

    # Incident photon energy
    incident_energy_mev = st.sidebar.slider(
        "Incident Photon Energy (MeV)",
        min_value=0.5,
        max_value=10.0,
        value=2.5,
        step=0.1
    )

    # Nuclear charge (affects threshold slightly)
    nuclear_charge = st.sidebar.slider(
        "Nuclear Charge (Z)",
        min_value=1,
        max_value=100,
        value=26,  # Iron
        step=1
    )

    # Calculate pair production parameters
    result = pair_production(incident_energy_mev * 1000)  # Convert MeV to keV

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Energy Analysis")

        # Create pair production plot
        fig = create_pair_production_plot(10.0)

        # Add current energy marker
        fig.add_trace(go.Scatter(
            x=[incident_energy_mev],
            y=[result['excess_energy'] / 1000],
            mode='markers',
            name='Current Energy',
            marker=dict(color='orange', size=12, symbol='star')
        ))

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Results")

        # Display key parameters
        st.metric("Incident Energy", f"{incident_energy_mev} MeV")
        st.metric("Threshold Energy", f"{result['threshold_energy']/1000:.3f} MeV")

        if result['can_occur']:
            st.success("✅ Pair production possible!")
            st.metric("Excess Energy", f"{result['excess_energy']/1000:.3f} MeV")
            st.metric("Kinetic Energy per Particle", f"{result['kinetic_energy_each']/1000:.3f} MeV")

            # Show energy balance
            st.latex(r"E_\gamma = 2m_e c^2 + E_{e^-} + E_{e^+}")
            st.latex(f"{incident_energy_mev:.3f} = 1.022 + {result['kinetic_energy_each']/1000:.3f} + {result['kinetic_energy_each']/1000:.3f}\\,\\text{{MeV}}")

        else:
            deficit = result['minimum_energy']/1000 - incident_energy_mev
            st.error("❌ Insufficient energy for pair production")
            st.metric("Energy Deficit", f"{deficit:.3f} MeV")

    # Process visualization
    st.subheader("Pair Production Process")

    col3, col4 = st.columns([1, 2])

    with col3:
        st.markdown("**Before:**")
        st.latex(r"\gamma \rightarrow e^- + e^+")

        st.markdown("**Conservation:**")
        st.latex(r"E_\gamma \geq 2m_e c^2")
        st.latex(r"\vec{p}_\gamma = \vec{p}_{e^-} + \vec{p}_{e^+}")

        if result['can_occur']:
            st.markdown("**Energy Distribution:**")
            total_kinetic = result['excess_energy'] / 1000
            st.metric("Total Kinetic Energy", f"{total_kinetic:.3f} MeV")
            st.metric("Per Particle (avg)", f"{total_kinetic/2:.3f} MeV")

    with col4:
        # Create process diagram
        fig_process = go.Figure()

        # Photon
        fig_process.add_trace(go.Scatter(
            x=[0], y=[0],
            mode='markers+text',
            text=['γ'],
            textposition="middle right",
            marker=dict(size=30, color='yellow', symbol='star'),
            showlegend=False
        ))

        # Arrow
        fig_process.add_annotation(
            x=1, y=0,
            ax=0.2, ay=0,
            xref='x', yref='y',
            axref='x', ayref='y',
            showarrow=True,
            arrowhead=3,
            arrowsize=2,
            arrowwidth=3,
            arrowcolor='black'
        )

        # Electron and positron
        if result['can_occur']:
            fig_process.add_trace(go.Scatter(
                x=[1.5, 1.5], y=[0.3, -0.3],
                mode='markers+text',
                text=['e⁻', 'e⁺'],
                textposition=["bottom center", "top center"],
                marker=dict(size=25, color=['blue', 'red']),
                showlegend=False
            ))

            # Kinetic energy labels
            fig_process.add_trace(go.Scatter(
                x=[2, 2], y=[0.3, -0.3],
                mode='text',
                text=[f'Eₖ = {result["kinetic_energy_each"]/1000:.2f} MeV',
                      f'Eₖ = {result["kinetic_energy_each"]/1000:.2f} MeV'],
                textposition=["middle left", "middle left"],
                showlegend=False
            ))

        fig_process.update_layout(
            title="Pair Production Schematic",
            xaxis=dict(visible=False, range=[-0.5, 2.5]),
            yaxis=dict(visible=False, range=[-1, 1]),
            height=300,
            showlegend=False
        )

        st.plotly_chart(fig_process, use_container_width=True)

    # Nuclear field effects
    st.subheader("Nuclear Field Effects")

    # Calculate screening correction (simplified)
    threshold_with_nucleus = result['threshold_energy'] / 1000  # Base threshold
    screening_correction = 0.001 * (nuclear_charge ** (1/3))  # Approximate correction
    effective_threshold = threshold_with_nucleus - screening_correction

    col5, col6 = st.columns(2)

    with col5:
        st.metric("Base Threshold", f"{threshold_with_nucleus:.3f} MeV")
        st.metric("Nuclear Correction", f"-{screening_correction:.3f} MeV")
        st.metric("Effective Threshold", f"{effective_threshold:.3f} MeV")

        if incident_energy_mev >= effective_threshold:
            st.success("Pair production enhanced by nuclear field!")
        else:
            st.info("Nuclear field effect minimal at this energy")

    with col6:
        st.markdown("""
        **Nuclear Field Enhancement:**
        - Reduces threshold energy slightly
        - More significant for high-Z materials
        - Enables pair production below 1.022 MeV in some cases
        - Important for medical and nuclear physics applications
        """)

    # Cross section information
    st.subheader("Interaction Cross Section")

    energy_range = np.logspace(np.log10(1.1), np.log10(10), 50)  # MeV
    cross_section = []

    # Simplified cross section calculation (Bethe-Heitler approximation)
    for e in energy_range:
        if e > 1.022:
            # Approximate cross section in barns
            sigma = 1.5e-2 * (1/e) * (np.log(2*e/0.511) - 1) * nuclear_charge**2
            cross_section.append(sigma)
        else:
            cross_section.append(0)

    fig_cross = go.Figure()

    fig_cross.add_trace(go.Scatter(
        x=energy_range,
        y=cross_section,
        mode='lines',
        name='Cross Section',
        line=dict(color='purple', width=3)
    ))

    # Add current energy marker
    if incident_energy_mev > 1.022:
        current_sigma = 1.5e-2 * (1/incident_energy_mev) * (np.log(2*incident_energy_mev/0.511) - 1) * nuclear_charge**2
        fig_cross.add_trace(go.Scatter(
            x=[incident_energy_mev],
            y=[current_sigma],
            mode='markers',
            name='Current Energy',
            marker=dict(color='red', size=10, symbol='star')
        ))

    fig_cross.update_layout(
        title="Pair Production Cross Section",
        xaxis_title="Photon Energy (MeV)",
        yaxis_title="Cross Section (barns)",
        xaxis_type="log",
        yaxis_type="log",
        height=400
    )

    st.plotly_chart(fig_cross, use_container_width=True)

    # Educational content
    st.markdown("---")
    st.subheader("📚 Key Concepts")

    col7, col8 = st.columns(2)

    with col7:
        st.markdown("""
        **Pair Production:**
        - Photon creates e⁻e⁺ pair
        - Requires E_γ ≥ 1.022 MeV
        - Must occur near nucleus (Coulomb field)
        - Total energy conserved
        - Momentum conserved via nucleus

        **Threshold Energy:**
        - 2m_e c² = 1.022 MeV
        - Rest energy of electron + positron
        - Cannot occur in vacuum (momentum conservation)
        """)

    with col8:
        st.markdown("""
        **Conservation Laws:**
        - Energy: E_γ = E_e⁻ + E_e⁺ + 2m_e c²
        - Momentum: p_γ = p_e⁻ + p_e⁺ + p_nucleus
        - Charge: 0 = (-1) + (+1)
        - Quantum numbers conserved

        **Applications:**
        - High-energy physics experiments
        - Medical radiation therapy
        - Nuclear physics research
        - Cosmic ray interactions
        """)

    # Historical context
    with st.expander("🕰️ Historical Development"):
        st.markdown("""
        **1933: Discovery by Chadwick and Blackett**
        - First observed in cloud chamber experiments
        - Confirmed Dirac's prediction of positrons
        - Provided evidence for antimatter

        **Theoretical Foundation:**
        - Dirac's relativistic quantum mechanics (1928)
        - Predicted positron as electron's antiparticle
        - Nobel Prize to Dirac (1933)

        **Key Evidence:**
        - e⁻e⁺ pairs observed in cosmic ray interactions
        - Energy threshold matched theoretical prediction
        - Momentum conservation satisfied
        """)

    # Inverse process
    st.subheader("Related Process: Annihilation")

    st.markdown("""
    **Electron-Positron Annihilation:**
    - Inverse of pair production
    - e⁻ + e⁺ → 2γ (or 3γ)
    - Releases 1.022 MeV as photons
    - Important in PET imaging
    """)

    # PET application
    if st.checkbox("Show PET Medical Application"):
        st.markdown("""
        **Positron Emission Tomography (PET):**
        - Patient injected with positron-emitting isotope
        - Positrons annihilate with electrons
        - Two 511 keV photons detected in coincidence
        - Used for cancer diagnosis and research
        """)

if __name__ == "__main__":
    main()
