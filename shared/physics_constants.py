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

# Medical physics relevant materials work functions (eV)
# Includes detector materials, x-ray targets, tissue surrogates, and shielding materials
WORK_FUNCTIONS = {
    # Detector Materials
    'Sodium Iodide (NaI)': 4.3,      # Common scintillator for gamma cameras
    'Cesium Iodide (CsI)': 6.2,      # Used in CT detectors and gamma cameras
    'Cadmium Telluride (CdTe)': 4.3, # Semiconductor detector for SPECT
    'Silicon (Si)': 4.8,             # Semiconductor detector material
    'Germanium (Ge)': 4.8,           # High-purity Ge detector for spectroscopy

    # X-ray Tube Target Materials
    'Tungsten (W)': 4.5,             # Most common x-ray tube target
    'Molybdenum (Mo)': 4.2,          # Used in mammography tubes
    'Rhodium (Rh)': 4.8,             # Alternative mammography target

    # Tissue and Phantom Materials
    'Aluminum (Al)': 4.2,            # Tissue surrogate, beam hardening studies
    'PMMA (Plastic)': 4.3,           # Common phantom material
    'Water': 6.5,                    # Reference tissue-equivalent material

    # Shielding and Contrast Materials
    'Lead (Pb)': 4.1,                # Primary shielding material
    'Copper (Cu)': 4.7,              # Secondary shielding, collimators
    'Iodine (I)': 4.6,               # Contrast agent material
    'Calcium (Ca)': 2.9,             # Bone mineral component
    'Bismuth (Bi)': 4.3              # Alternative contrast material
}

# Atomic numbers for common elements
ATOMIC_NUMBERS = {
    'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6,
    'N': 7, 'O': 8, 'F': 9, 'Ne': 10, 'Na': 11, 'Mg': 12,
    'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18,
    'K': 19, 'Ca': 20, 'Fe': 26, 'Cu': 29, 'Zn': 30, 'Ag': 47,
    'I': 53, 'W': 74, 'Pb': 82, 'U': 92
}
