"""
Page 1: Projects & Tools — Scientific Software Portfolio
"""

import streamlit as st

st.set_page_config(
    page_title="Projects — Harshvardhan Modh",
    page_icon="🔬",
    layout="wide",
)

st.title("🔬 Projects & Tools")
st.markdown("### Open-Source Scientific Software for Pharmaceutical R&D")

st.markdown(
    """
Open-source tools built to address recurring bottlenecks in pharmaceutical
R&D — from regulatory decision-making to image-based material
characterization. All projects are fully documented with synthetic / demo
data and deployed for immediate use.
"""
)

st.markdown("---")

# ── IVIVC & Computational Modeling ──────────────────────────────────────────
st.header("IVIVC & Computational Modeling")

col1, col2 = st.columns(2)

with col1:
    st.subheader("IVIVC Level Selection Dashboard")
    st.markdown(
        """
`Python` `Streamlit` `NumPy` `SciPy` `Plotly`

Interactive web application that guides pharmaceutical scientists through
IVIVC level selection (A, B, or C) via a structured decision questionnaire
with weighted scoring logic. Includes step-by-step tutorials for each
level — Level A deconvolution (Wagner-Nelson), Level B statistical moment
comparison (MDT vs MRT), and Level C single-point correlation with R²
heatmaps — all powered by fully synthetic pharmacokinetic and dissolution
data. Deployed on Streamlit Community Cloud for zero-install access.

🚀 **[Live App](https://ivivc-level-selector.streamlit.app)** ·
💻 **[GitHub](https://github.com/Harsh9005/ivivc-level-selector)**
"""
    )

with col2:
    st.subheader("Level C IVIVC Visualization Framework")
    st.markdown(
        """
`Python` `NumPy` `SciPy` `Matplotlib`

Publication-ready visualization pipeline for Level C IVIVC methodology
applied to biodegradable PLGA microsphere depot formulations. Generates
Weibull-fitted dissolution profiles, bi-exponential pharmacokinetic curves,
8×3 parameter correlation matrices with R² heatmaps, and f1/f2 similarity
analysis — all from synthetic data designed to mirror real-world long-acting
injectable scenarios.

💻 **[GitHub](https://github.com/Harsh9005/ivivc-level-c-viz)**
"""
    )

st.markdown("---")

# ── Image Analysis & Visualization ──────────────────────────────────────────
st.header("Image Analysis & Visualization")

col1, col2 = st.columns(2)

with col1:
    st.subheader("SEM Pore Size Analyzer")
    st.markdown(
        """
`Python` `OpenCV` `NumPy` `Matplotlib`

Automated image analysis pipeline that quantifies pore size distributions
from scanning electron microscopy (SEM) micrographs. Uses adaptive Gaussian
thresholding, morphological filtering, and contour detection to extract pore
boundaries, compute equivalent diameters, and generate annotated overlay
images with statistical summaries. Eliminates manual measurement bias in
scaffold and membrane characterization.

💻 **[GitHub](https://github.com/Harsh9005/sem-pore-analysis)**
"""
    )

with col2:
    st.subheader("Polarized Microscopy Crystal Analyzer")
    st.markdown(
        """
`Python` `OpenCV` `scikit-image` `Matplotlib`

Image processing pipeline for quantifying birefringent crystal area from
polarized light microscopy images. Applies adaptive thresholding and
connected-component analysis to segment crystalline domains, calculating
total crystal area fraction and size distributions. Designed for
polymorphism screening and crystallization process monitoring in
pharmaceutical manufacturing.

💻 **[GitHub](https://github.com/Harsh9005/polarized-microscopy-crystal-analysis)**
"""
    )

st.markdown("")

st.subheader("Wall Shear Stress 3D Visualization")
st.markdown(
    """
`Python` `Matplotlib` `NumPy`

Programmatic 3D visualization framework mapping wall shear stress (WSS)
distributions across the human circulatory system under healthy and
pathological conditions. Renders bifurcation geometries with color-mapped
WSS gradients to identify regions of disturbed flow linked to
atherosclerosis and nanoparticle margination — supporting the
'biomechanical blind spot' framework described in the *Nature Biomedical
Engineering* manuscript.

💻 **[GitHub](https://github.com/Harsh9005/shear-stress-3d-viz)**
"""
)

st.markdown("---")
st.caption(
    "All tools use synthetic / demo data. No proprietary data is included."
)
