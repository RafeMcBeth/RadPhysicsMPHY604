"""
Common plotting utilities for physics education apps
"""

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

def create_energy_frequency_plot(work_function=4.0, max_energy=10.0):
    """
    Create interactive plot for photoelectric effect energy vs frequency

    Parameters:
    work_function: Work function in eV
    max_energy: Maximum photon energy to plot (eV)

    Returns:
    Plotly figure object
    """
    from .physics_constants import PLANCK_CONSTANT, EV_TO_JOULES

    # Create frequency range
    frequencies = np.linspace(0, max_energy / (PLANCK_CONSTANT / EV_TO_JOULES) * 1e14, 1000)
    energies = frequencies * (PLANCK_CONSTANT / EV_TO_JOULES) * 1e-14  # Convert back to eV

    # Threshold frequency
    f_threshold = work_function / (PLANCK_CONSTANT / EV_TO_JOULES)
    threshold_freq = f_threshold * 1e-14  # Convert to reasonable units for plotting

    # Create the plot
    fig = go.Figure()

    # Photon energy line
    fig.add_trace(go.Scatter(
        x=frequencies,
        y=energies,
        mode='lines',
        name='Photon Energy (E = hf)',
        line=dict(color='blue', width=3)
    ))

    # Work function threshold
    fig.add_trace(go.Scatter(
        x=[threshold_freq, threshold_freq],
        y=[0, work_function],
        mode='lines',
        name='Work Function',
        line=dict(color='red', width=2, dash='dash')
    ))

    # Kinetic energy region
    kinetic_freq = np.linspace(threshold_freq, frequencies[-1], 100)
    kinetic_energy = (kinetic_freq - threshold_freq) * (PLANCK_CONSTANT / EV_TO_JOULES) * 1e-14
    fig.add_trace(go.Scatter(
        x=kinetic_freq,
        y=kinetic_energy + work_function,
        mode='lines',
        name='Max Kinetic Energy',
        line=dict(color='green', width=2)
    ))

    fig.update_layout(
        title="Photoelectric Effect: Energy vs Frequency",
        xaxis_title="Frequency (×10¹⁴ Hz)",
        yaxis_title="Energy (eV)",
        showlegend=True,
        height=500
    )

    return fig

def create_compton_scattering_plot(incident_energy=1.0, max_angle=180):
    """
    Create polar plot for Compton scattering

    Parameters:
    incident_energy: Incident photon energy (MeV)
    max_angle: Maximum scattering angle to plot (degrees)

    Returns:
    Plotly figure object
    """
    from .physics_calculations import compton_scattering

    angles = np.linspace(0, max_angle, 100)
    scattered_energies = []
    wavelength_changes = []

    for angle in angles:
        result = compton_scattering(incident_energy * 1000, angle)  # Convert MeV to keV
        scattered_energies.append(result['scattered_energy'] / 1000)  # Convert keV to MeV
        wavelength_changes.append(result['wavelength_change'])

    # Create subplot figure
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=("Scattered Photon Energy", "Wavelength Change"),
        specs=[[{'type': 'polar'}, {'type': 'xy'}]]
    )

    # Polar plot for scattered energy
    fig.add_trace(go.Scatterpolar(
        r=scattered_energies,
        theta=angles,
        mode='lines',
        name='Scattered Energy',
        line=dict(color='blue', width=2)
    ), row=1, col=1)

    # Cartesian plot for wavelength change
    fig.add_trace(go.Scatter(
        x=angles,
        y=wavelength_changes,
        mode='lines',
        name='Δλ',
        line=dict(color='red', width=2)
    ), row=1, col=2)

    fig.update_layout(
        title=f"Compton Scattering (E₀ = {incident_energy} MeV)",
        height=500,
        polar=dict(
            radialaxis=dict(title="Energy (MeV)"),
            angularaxis=dict(title="Scattering Angle (°)"))
    )

    return fig

def create_pair_production_plot(max_energy=5.0):
    """
    Create plot showing pair production threshold and energy distribution

    Parameters:
    max_energy: Maximum photon energy to plot (MeV)

    Returns:
    Plotly figure object
    """
    from .physics_constants import ELECTRON_REST_ENERGY
    from .physics_calculations import pair_production

    energies = np.linspace(0.5, max_energy, 200)
    thresholds = []
    excess_energies = []
    kinetic_energies = []

    for energy in energies:
        result = pair_production(energy * 1000)  # Convert MeV to keV
        thresholds.append(result['threshold_energy'] / 1000)  # Convert keV to MeV
        excess_energies.append(result['excess_energy'] / 1000)
        kinetic_energies.append(result['kinetic_energy_each'] / 1000)

    fig = go.Figure()

    # Threshold line
    fig.add_trace(go.Scatter(
        x=energies,
        y=thresholds,
        mode='lines',
        name='Threshold Energy (1.022 MeV)',
        line=dict(color='red', width=2, dash='dash')
    ))

    # Total excess energy available
    fig.add_trace(go.Scatter(
        x=energies,
        y=excess_energies,
        mode='lines',
        name='Excess Energy for Kinetic',
        line=dict(color='blue', width=2)
    ))

    # Kinetic energy per particle (approximate)
    fig.add_trace(go.Scatter(
        x=energies,
        y=kinetic_energies,
        mode='lines',
        name='Kinetic Energy per Particle',
        line=dict(color='green', width=2)
    ))

    # Threshold marker
    threshold_energy = 2 * ELECTRON_REST_ENERGY / 1000  # Convert keV to MeV
    fig.add_trace(go.Scatter(
        x=[threshold_energy],
        y=[0],
        mode='markers',
        name='Pair Production Threshold',
        marker=dict(color='red', size=10, symbol='star')
    ))

    fig.update_layout(
        title="Pair Production Energy Analysis",
        xaxis_title="Incident Photon Energy (MeV)",
        yaxis_title="Energy (MeV)",
        showlegend=True,
        height=500
    )

    return fig

def create_3d_scattering_visualization(scattering_angle=90):
    """
    Create 3D visualization of Compton scattering geometry

    Parameters:
    scattering_angle: Scattering angle in degrees

    Returns:
    Plotly 3D figure object
    """
    theta = np.radians(scattering_angle)

    # Photon path
    photon_x = [0, np.cos(theta), 2*np.cos(theta)]
    photon_y = [0, np.sin(theta), 2*np.sin(theta)]
    photon_z = [0, 0, 0]

    # Electron recoil (simplified)
    electron_angle = theta + np.pi/2
    electron_x = [0, 0.5*np.cos(electron_angle)]
    electron_y = [0, 0.5*np.sin(electron_angle)]
    electron_z = [0, 0.2]

    fig = go.Figure()

    # Incident photon
    fig.add_trace(go.Scatter3d(
        x=[0, np.cos(theta)],
        y=[0, np.sin(theta)],
        z=[0, 0],
        mode='lines+markers',
        name='Incident Photon',
        line=dict(color='blue', width=4),
        marker=dict(size=6)
    ))

    # Scattered photon
    fig.add_trace(go.Scatter3d(
        x=[np.cos(theta), 2*np.cos(theta)],
        y=[np.sin(theta), 2*np.sin(theta)],
        z=[0, 0],
        mode='lines+markers',
        name='Scattered Photon',
        line=dict(color='red', width=4),
        marker=dict(size=6)
    ))

    # Electron
    fig.add_trace(go.Scatter3d(
        x=electron_x,
        y=electron_y,
        z=electron_z,
        mode='lines+markers',
        name='Recoil Electron',
        line=dict(color='green', width=4),
        marker=dict(size=6)
    ))

    # Electron position marker
    fig.add_trace(go.Scatter3d(
        x=[0], y=[0], z=[0],
        mode='markers',
        name='Electron at Rest',
        marker=dict(color='black', size=8, symbol='diamond')
    ))

    fig.update_layout(
        title=f"Compton Scattering Geometry (θ = {scattering_angle}°)",
        scene=dict(
            xaxis_title="X",
            yaxis_title="Y",
            zaxis_title="Z",
            aspectmode='cube'
        ),
        height=600
    )

    return fig
