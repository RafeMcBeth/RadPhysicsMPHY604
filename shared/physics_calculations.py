"""
Physics calculation functions for photon-matter interactions
"""

import numpy as np
from .physics_constants import *

def photoelectric_effect(incident_energy, work_function):
    """
    Calculate photoelectric effect parameters

    Parameters:
    incident_energy: Photon energy (eV)
    work_function: Material work function (eV)

    Returns:
    dict with kinetic_energy, max_electron_energy, threshold_frequency, can_eject
    """
    if incident_energy < work_function:
        return {
            'kinetic_energy': 0,
            'max_electron_energy': 0,
            'threshold_frequency': work_function / PLANCK_CONSTANT * EV_TO_JOULES,
            'can_eject': False,
            'threshold_wavelength': energy_to_wavelength(work_function / 1000)  # Convert eV to keV
        }

    kinetic_energy = incident_energy - work_function  # eV

    return {
        'kinetic_energy': kinetic_energy,
        'max_electron_energy': kinetic_energy,  # Maximum kinetic energy
        'threshold_frequency': work_function / PLANCK_CONSTANT * EV_TO_JOULES,
        'can_eject': True,
        'threshold_wavelength': energy_to_wavelength(work_function / 1000)  # Convert eV to keV
    }

def compton_scattering(incident_energy, scattering_angle):
    """
    Calculate Compton scattering parameters

    Parameters:
    incident_energy: Incident photon energy (keV)
    scattering_angle: Scattering angle in degrees

    Returns:
    dict with scattered_energy, wavelength_change, recoil_electron_energy
    """
    theta = np.radians(scattering_angle)

    # Compton wavelength of electron
    lambda_c = PLANCK_CONSTANT / (ELECTRON_REST_MASS * SPEED_OF_LIGHT) * METERS_TO_ANGSTROM  # Å

    # Incident wavelength
    lambda_i = energy_to_wavelength(incident_energy) * METERS_TO_ANGSTROM  # Å

    # Scattered wavelength
    lambda_f = lambda_i + lambda_c * (1 - np.cos(theta))

    # Scattered energy
    scattered_energy = wavelength_to_energy(lambda_f * ANGSTROM_TO_METERS)  # keV

    # Energy lost to electron
    energy_lost = incident_energy - scattered_energy

    # Recoil electron energy (non-relativistic approximation)
    electron_energy = energy_lost * (1 - np.cos(theta)) / (1 + energy_lost / (ELECTRON_REST_ENERGY * 1000))

    return {
        'scattered_energy': scattered_energy,
        'wavelength_change': lambda_f - lambda_i,
        'recoil_electron_energy': electron_energy,
        'energy_lost': energy_lost,
        'compton_wavelength': lambda_c
    }

def pair_production(incident_energy):
    """
    Calculate pair production parameters

    Parameters:
    incident_energy: Incident photon energy (keV)

    Returns:
    dict with threshold_energy, excess_energy, can_occur
    """
    threshold_energy = 2 * ELECTRON_REST_ENERGY  # 1.022 MeV total for e+e-

    if incident_energy < threshold_energy:
        return {
            'threshold_energy': threshold_energy,
            'excess_energy': 0,
            'kinetic_energy_each': 0,
            'can_occur': False,
            'minimum_energy': threshold_energy
        }

    # Total energy available for kinetic energy (conserving momentum)
    total_energy = incident_energy - threshold_energy
    kinetic_energy_each = total_energy / 2  # Approximate equal sharing

    return {
        'threshold_energy': threshold_energy,
        'excess_energy': total_energy,
        'kinetic_energy_each': kinetic_energy_each,
        'can_occur': True,
        'minimum_energy': threshold_energy
    }

def compton_wavelength_max(incident_energy):
    """
    Calculate maximum wavelength change in Compton scattering (180° scattering)

    Parameters:
    incident_energy: Incident photon energy (keV)

    Returns:
    Maximum wavelength change in Å
    """
    lambda_c = PLANCK_CONSTANT / (ELECTRON_REST_MASS * SPEED_OF_LIGHT) * METERS_TO_ANGSTROM
    return 2 * lambda_c

def photoelectric_threshold_frequency(work_function):
    """
    Calculate threshold frequency for photoelectric effect

    Parameters:
    work_function: Work function in eV

    Returns:
    Threshold frequency in Hz
    """
    return work_function * EV_TO_JOULES / PLANCK_CONSTANT

def photoelectric_threshold_wavelength(work_function):
    """
    Calculate threshold wavelength for photoelectric effect

    Parameters:
    work_function: Work function in eV

    Returns:
    Threshold wavelength in meters
    """
    f_threshold = photoelectric_threshold_frequency(work_function)
    return SPEED_OF_LIGHT / f_threshold
