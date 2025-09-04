"""
Physics constants and fundamental values for radiation physics calculations
All values in SI units unless otherwise specified
"""

import numpy as np

# Fundamental constants
PLANCK_CONSTANT = 6.62607015e-34  # J⋅s
PLANCK_CONSTANT_HBAR = PLANCK_CONSTANT / (2 * np.pi)  # J⋅s
SPEED_OF_LIGHT = 2.99792458e8  # m/s
ELECTRON_REST_MASS = 9.1093837015e-31  # kg
ELECTRON_REST_ENERGY = 510.998946  # keV (electron rest mass energy)
PROTON_REST_MASS = 1.67262192369e-27  # kg
NEUTRON_REST_MASS = 1.67492749804e-27  # kg

# Conversion factors
EV_TO_JOULES = 1.602176634e-19
KEV_TO_JOULES = 1.602176634e-16
MEV_TO_JOULES = 1.602176634e-13
JOULES_TO_EV = 1 / EV_TO_JOULES
JOULES_TO_KEV = 1 / KEV_TO_JOULES
JOULES_TO_MEV = 1 / MEV_TO_JOULES

# Wavelength conversions
ANGSTROM_TO_METERS = 1e-10
METERS_TO_ANGSTROM = 1e10

# Energy-wavelength conversions
def energy_to_wavelength(energy_kev):
    """Convert photon energy (keV) to wavelength (m)"""
    return (PLANCK_CONSTANT * SPEED_OF_LIGHT) / (energy_kev * KEV_TO_JOULES)

def wavelength_to_energy(wavelength_m):
    """Convert wavelength (m) to photon energy (keV)"""
    return (PLANCK_CONSTANT * SPEED_OF_LIGHT) / (wavelength_m * JOULES_TO_KEV)

# Common material work functions (eV)
WORK_FUNCTIONS = {
    'Cesium': 2.1,
    'Potassium': 2.3,
    'Sodium': 2.28,
    'Lithium': 2.9,
    'Zinc': 4.3,
    'Copper': 4.7,
    'Silver': 4.26,
    'Platinum': 6.35
}

# Atomic numbers for common elements
ATOMIC_NUMBERS = {
    'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6,
    'N': 7, 'O': 8, 'F': 9, 'Ne': 10, 'Na': 11, 'Mg': 12,
    'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18,
    'K': 19, 'Ca': 20, 'Fe': 26, 'Cu': 29, 'Zn': 30, 'Ag': 47,
    'I': 53, 'W': 74, 'Pb': 82, 'U': 92
}
