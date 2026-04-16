"""
Antenna Array Pattern Synthesis Tool - Interactive Streamlit App

Main landing page with overview and navigation.
"""

import streamlit as st 

st.set_page_config(
    page_title="Antenna Array Pattern Synthesis Tool",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title(" Antenna Array Pattern Synthesis Tool")

st.markdown("""
Welcome to the **Antenna Array Pattern Synthesis Tool** - an interactive tool for designing,
analyzing, and visualizing phased array antenna systems.

### Features

Use the sidebar to navigate between different tools:

1. **Array Design** - Create and configure array geometries
   - Rectangular, triangular, circular arrays
   - Adjust element count and spacing
   - Visualize element positions

2. **Beam Steering** - Control beam direction
   - Interactive theta/phi sliders
   - Real-time pattern updates
   - E-plane and H-plane cuts

3. **Tapering** - Apply amplitude tapers for sidelobe control
   - Taylor, Chebyshev, Hamming windows
   - Compare taper efficiency
   - See sidelobe reduction

4. **UV-Space** - Visualize in direction cosine space
   - See visible region
   - Identify grating lobes
   - Interactive Plotly plots


### Quick Start

1. Go to **Array Design** to create your array (enable subarrays for wideband analysis)
2. Use **Beam Steering** to point the beam
3. Apply **Tapering** for sidelobe control
4. View **UV-Space** for advanced analysis


---
""")

# Sidebar info
st.sidebar.success("Select a page above to get started!")

st.sidebar.markdown("---")
st.sidebar.markdown("""
### Resources
- [GitHub Repository](https://github.com/martinjenny123/Antenna-Array-Pattern-Synthesis-Tool)
""")
