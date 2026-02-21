"""
Page 1: Projects & Tools — Scientific Software Portfolio
"""

import streamlit as st

st.set_page_config(
    page_title="Projects — Harshvardhan Modh",
    page_icon="🔬",
    layout="wide",
)

# ── Raw GitHub image base URLs ──────────────────────────────────────────────
_GH = "https://raw.githubusercontent.com/Harsh9005"
_IVIVC_VIZ = f"{_GH}/ivivc-level-c-viz/main/figures"
_SEM = f"{_GH}/sem-pore-analysis/main/example_output"
_PLM = f"{_GH}/polarized-microscopy-crystal-analysis/main/example_output"
_WSS = f"{_GH}/shear-stress-3d-viz/main"

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

# ═════════════════════════════════════════════════════════════════════════════
# IVIVC & Computational Modeling
# ═════════════════════════════════════════════════════════════════════════════
st.header("IVIVC & Computational Modeling")

# ── 1. IVIVC Level Selection Dashboard ──────────────────────────────────────
st.subheader("1. IVIVC Level Selection Dashboard")
st.markdown(
    "`Python` `Streamlit` `NumPy` `SciPy` `Plotly`"
)

st.markdown(
    """
Interactive web application that guides pharmaceutical scientists through
IVIVC level selection (A, B, or C) via a structured decision questionnaire
with weighted scoring logic. Includes step-by-step tutorials for each
level — Level A deconvolution (Wagner-Nelson), Level B statistical moment
comparison (MDT vs MRT), and Level C single-point correlation with R²
heatmaps — all powered by fully synthetic pharmacokinetic and dissolution
data. Deployed on Streamlit Community Cloud for zero-install access.

🚀 **[Launch Live App](https://ivivc-level-selector.streamlit.app)** ·
💻 **[GitHub](https://github.com/Harsh9005/ivivc-level-selector)**
"""
)

st.markdown("")

# ── 2. Level C IVIVC Visualization Framework ────────────────────────────────
st.subheader("2. Level C IVIVC Visualization Framework")
st.markdown(
    "`Python` `NumPy` `SciPy` `Matplotlib`"
)

st.markdown(
    """
Publication-ready visualization pipeline for Level C IVIVC methodology
applied to biodegradable PLGA microsphere depot formulations. Generates
Weibull-fitted dissolution profiles, bi-exponential pharmacokinetic curves,
8×3 parameter correlation matrices with R² heatmaps, and f1/f2 similarity
analysis — all from synthetic data designed to mirror real-world long-acting
injectable scenarios.

💻 **[GitHub](https://github.com/Harsh9005/ivivc-level-c-viz)**
"""
)

col1, col2, col3 = st.columns(3)
with col1:
    st.image(
        f"{_IVIVC_VIZ}/panel_A_invitro_release.png",
        caption="In-Vitro Release Profiles",
        use_container_width=True,
    )
with col2:
    st.image(
        f"{_IVIVC_VIZ}/panel_B_pk_profiles.png",
        caption="Pharmacokinetic Profiles",
        use_container_width=True,
    )
with col3:
    st.image(
        f"{_IVIVC_VIZ}/panel_C_ivivc_correlations.png",
        caption="IVIVC Correlations",
        use_container_width=True,
    )

col1, col2, col3 = st.columns(3)
with col1:
    st.image(
        f"{_IVIVC_VIZ}/panel_D_slope_heatmap.png",
        caption="R² Slope Heatmap",
        use_container_width=True,
    )
with col2:
    st.image(
        f"{_IVIVC_VIZ}/panel_E_f1f2_analysis.png",
        caption="f1/f2 Similarity Analysis",
        use_container_width=True,
    )
with col3:
    st.image(
        f"{_IVIVC_VIZ}/panel_F_summary_dashboard.png",
        caption="Summary Dashboard",
        use_container_width=True,
    )

st.markdown("---")

# ═════════════════════════════════════════════════════════════════════════════
# Image Analysis & Visualization
# ═════════════════════════════════════════════════════════════════════════════
st.header("Image Analysis & Visualization")

# ── 3. SEM Pore Size Analyzer ───────────────────────────────────────────────
st.subheader("3. SEM Pore Size Analyzer")
st.markdown(
    "`Python` `OpenCV` `NumPy` `Matplotlib`"
)

st.markdown(
    """
Automated image analysis pipeline that quantifies pore size distributions
from scanning electron microscopy (SEM) micrographs. Uses adaptive Gaussian
thresholding, morphological filtering, and contour detection to extract pore
boundaries, compute equivalent diameters, and generate annotated overlay
images with statistical summaries. Eliminates manual measurement bias in
scaffold and membrane characterization.

💻 **[GitHub](https://github.com/Harsh9005/sem-pore-analysis)**
"""
)

col1, col2, col3 = st.columns(3)
with col1:
    st.image(
        f"{_SEM}/Annotated_sample_1.png",
        caption="Annotated SEM — Sample 1",
        use_container_width=True,
    )
with col2:
    st.image(
        f"{_SEM}/Annotated_sample_2.png",
        caption="Annotated SEM — Sample 2",
        use_container_width=True,
    )
with col3:
    st.image(
        f"{_SEM}/Annotated_sample_3.png",
        caption="Annotated SEM — Sample 3",
        use_container_width=True,
    )

col1, col2 = st.columns(2)
with col1:
    st.image(
        f"{_SEM}/composite_segmentation.png",
        caption="Composite Segmentation Overview",
        use_container_width=True,
    )
with col2:
    st.image(
        f"{_SEM}/pore_diameter_chart.png",
        caption="Pore Diameter Distribution",
        use_container_width=True,
    )

st.markdown("")

# ── 4. Polarized Microscopy Crystal Analyzer ────────────────────────────────
st.subheader("4. Polarized Microscopy Crystal Analyzer")
st.markdown(
    "`Python` `OpenCV` `scikit-image` `Matplotlib`"
)

st.markdown(
    """
Image processing pipeline for quantifying birefringent crystal area from
polarized light microscopy images. Applies adaptive thresholding and
connected-component analysis to segment crystalline domains, calculating
total crystal area fraction and size distributions. Designed for
polymorphism screening and crystallization process monitoring in
pharmaceutical manufacturing.

💻 **[GitHub](https://github.com/Harsh9005/polarized-microscopy-crystal-analysis)**
"""
)

col1, col2 = st.columns(2)
with col1:
    st.image(
        f"{_PLM}/composite_segmentation.png",
        caption="Crystal Segmentation Overview",
        use_container_width=True,
    )
with col2:
    st.image(
        f"{_PLM}/crystal_area_chart.png",
        caption="Crystal Area Analysis",
        use_container_width=True,
    )

st.markdown("")

# ── 5. Wall Shear Stress 3D Visualization ───────────────────────────────────
st.subheader("5. Wall Shear Stress 3D Visualization")
st.markdown(
    "`Python` `Matplotlib` `NumPy`"
)

st.markdown(
    """
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

st.image(
    f"{_WSS}/wss_circulatory_v3.png",
    caption="Wall Shear Stress — Full Circulatory System Overview",
    use_container_width=True,
)

col1, col2, col3 = st.columns(3)
with col1:
    st.image(
        f"{_WSS}/scenarios/01_healthy_baseline.png",
        caption="Healthy Baseline",
        use_container_width=True,
    )
with col2:
    st.image(
        f"{_WSS}/scenarios/02_lung_cancer.png",
        caption="Lung Cancer",
        use_container_width=True,
    )
with col3:
    st.image(
        f"{_WSS}/scenarios/03_liver_cancer_hcc.png",
        caption="Liver Cancer (HCC)",
        use_container_width=True,
    )

col1, col2, col3 = st.columns(3)
with col1:
    st.image(
        f"{_WSS}/scenarios/04_brain_tumor_gbm.png",
        caption="Brain Tumor (GBM)",
        use_container_width=True,
    )
with col2:
    st.image(
        f"{_WSS}/scenarios/05_multi_atherosclerosis.png",
        caption="Atherosclerosis",
        use_container_width=True,
    )
with col3:
    st.image(
        f"{_WSS}/scenarios/06_multi_stenosis.png",
        caption="Stenosis",
        use_container_width=True,
    )

st.image(
    f"{_WSS}/comparisons/scenario_dashboard.png",
    caption="Scenario Comparison Dashboard — Healthy vs Pathological Conditions",
    use_container_width=True,
)

st.markdown("---")
st.caption(
    "All tools use synthetic / demo data. No proprietary data is included."
)
