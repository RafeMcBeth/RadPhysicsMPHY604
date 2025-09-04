# Radiation Physics Interactive Education Apps

An interactive web-based learning platform for graduate-level radiation physics concepts, focusing on photon interactions with matter.

## 🎯 Overview

This project provides three comprehensive interactive web applications that help students visualize and understand fundamental concepts in radiation physics:

- **📸 Photoelectric Effect** - Einstein's quantum theory of light-matter interaction
- **🔄 Compton Scattering** - Quantum scattering of photons by electrons
- **⚡ Pair Production** - Photon conversion to electron-positron pairs

## 🚀 Features

### Interactive Learning Tools
- **Real-time calculations** with adjustable parameters
- **Dynamic visualizations** using Plotly and Matplotlib
- **3D geometry demonstrations** for scattering processes
- **Educational annotations** and theoretical explanations
- **Historical context** and experimental evidence

### Educational Content
- **Interactive sliders** for parameter exploration
- **Multiple visualization types** (plots, schematics, 3D models)
- **Conservation law demonstrations**
- **Cross-section calculations**
- **Material property databases**

### Technical Implementation
- **Streamlit-based** web applications
- **Modular architecture** with shared physics utilities
- **Real physics constants** from CODATA 2022
- **Responsive design** for various screen sizes

## 📁 Project Structure

```
RadPhysicsMPHY604/
├── main.py                    # Main navigation page
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── shared/                    # Shared utilities
│   ├── physics_constants.py   # Fundamental constants
│   ├── physics_calculations.py # Calculation functions
│   └── plotting_utils.py      # Visualization utilities
├── apps/                      # Individual concept apps
│   ├── photoelectric/
│   │   └── photoelectric_app.py
│   ├── compton_scattering/
│   │   └── compton_app.py
│   └── pair_production/
│       └── pair_app.py
└── utils/                     # Additional utilities
```

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd RadPhysicsMPHY604
   ```

2. **Install uv (if not already installed):**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Set up the project with uv:**
   ```bash
   # Install dependencies and create virtual environment
   uv sync

   # Or run the setup script
   ./setup.sh
   ```

## 🎮 Running the Applications

### Interactive Launcher (Recommended)
```bash
uv run python run_apps.py
```
This provides an interactive menu to choose which application to run.

### Main Navigation Page
```bash
uv run streamlit run main.py
```
This launches the main page where you can choose which concept to explore.

### Individual Apps
You can also run each app directly:

```bash
# Photoelectric Effect
uv run streamlit run apps/photoelectric/photoelectric_app.py

# Compton Scattering
uv run streamlit run apps/compton_scattering/compton_app.py

# Pair Production
uv run streamlit run apps/pair_production/pair_app.py
```

### Alternative Commands
Once the project script is configured, you can also use:
```bash
uv run radphysics  # Interactive launcher
```

## 📚 Educational Content Coverage

### Photoelectric Effect App
- **Einstein's photoelectric equation** (Eₖ = hν - φ)
- **Work function** for common materials
- **Threshold frequency** calculations
- **Energy-frequency relationships**
- **Interactive wavelength converter**
- **Historical development** and experimental evidence

### Compton Scattering App
- **Compton wavelength shift** (Δλ = λ₊(1-cosθ))
- **Energy-momentum conservation**
- **Scattering angle dependence**
- **3D geometry visualization**
- **Polar plot representations**
- **Recoil electron calculations**

### Pair Production App
- **Energy threshold** (1.022 MeV)
- **Nuclear field effects**
- **Conservation laws** demonstration
- **Cross-section calculations**
- **Process schematics**
- **Medical applications** (PET imaging)

## 🔬 Physics Implementation

### Accurate Calculations
- **Real physics constants** (Planck's constant, speed of light, electron mass)
- **Proper unit conversions** (eV ↔ keV ↔ MeV ↔ Joules)
- **Relativistic effects** where applicable
- **Conservation law verification**

### Interactive Features
- **Real-time parameter updates**
- **Multiple visualization modes**
- **Educational annotations**
- **Comparative analysis tools**

## 🎓 Learning Objectives

Students using these apps will be able to:

1. **Visualize** fundamental quantum processes
2. **Calculate** physical quantities with real-time feedback
3. **Explore** parameter dependencies and relationships
4. **Understand** conservation principles in action
5. **Connect** theoretical concepts with practical applications
6. **Analyze** experimental data and theoretical predictions

## 🏛️ Academic Applications

### Graduate Physics Courses
- **Medical Physics** - Radiation therapy planning
- **Nuclear Physics** - Particle interactions
- **Quantum Mechanics** - Photon-matter interactions
- **Health Physics** - Radiation protection

### Research Applications
- **Parameter studies** for experimental design
- **Educational demonstrations** for lectures
- **Student projects** and assignments
- **Concept validation** through visualization

## 🤝 Contributing

This project welcomes contributions! Areas for improvement:

- **Additional physics concepts** (e.g., Rayleigh scattering, bremsstrahlung)
- **More material properties** and interaction data
- **Enhanced visualizations** (animations, VR support)
- **Assessment tools** and quizzes
- **Multi-language support**

## 📄 License

This educational project is open-source and available under the MIT License.

## 🙏 Acknowledgments

- **Physics constants** from CODATA 2022
- **Educational inspiration** from classic physics texts
- **Open-source libraries** enabling interactive web applications

## 📞 Support

For questions, issues, or suggestions:
- Check the individual app documentation
- Review the physics calculations in `shared/`
- Open an issue in the repository

---

*Built with ❤️ for physics education using Python, Streamlit, and modern web technologies.*
