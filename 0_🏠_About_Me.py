"""
Personal Portfolio — Harshvardhan Modh, Ph.D.
=============================================
Pharmaceutical scientist, nanomedicine researcher, and computational tool builder.
"""

import streamlit as st

st.set_page_config(
    page_title="Harshvardhan Modh, Ph.D.",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Sidebar Branding ────────────────────────────────────────────────────────
st.sidebar.markdown("""
# 🧬 Harshvardhan Modh

**Ph.D. | Pharmaceutical R&D**

Navigate:
- 🏠 [About Me](/) *(this page)*
- 🔬 [Projects & Tools](/Projects)
- 📚 [Publications](/Publications)
- 📝 [Blog](/Blog)

---
📍 Singapore
""")

# ── Header ──────────────────────────────────────────────────────────────────
st.title("Harshvardhan Modh, Ph.D.")
st.markdown(
    "### Senior Scientist · Pharmaceutical R&D · Nanomedicine · Computational Modeling"
)
st.markdown("📍 Singapore")

st.markdown("---")

# ── Social Links ────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("🔗 [LinkedIn](https://linkedin.com/in/harshvardhan-modh-phd/)")
with col2:
    st.markdown(
        "🎓 [Google Scholar](https://scholar.google.de/citations?user=J2dpG98AAAAJ&hl=en)"
    )
with col3:
    st.markdown("💻 [GitHub](https://github.com/Harsh9005)")

col1, col2 = st.columns(2)
with col1:
    st.markdown("📧 **Work:** phahbm@nus.edu.sg")
with col2:
    st.markdown("📧 **Personal:** hbmodh@gmail.com")

st.markdown("---")

# ── About Me ────────────────────────────────────────────────────────────────
st.header("About Me")

st.markdown(
    """
R&D Scientist & Project Leader with **8+ years** of expertise in complex
injectable formulations, nanomedicine, and mRNA-LNP systems. Proven track
record managing **$2M+ in industrial alliances** with global leaders including
**Pfizer**, **AstraZeneca**, **CureVac**, and **Sun Pharma** — delivering
formulation strategies from bench-scale R&D through to clinical translation.

Expert in **IVIVC**, **mechanistic PBPK modeling**, and advanced analytical
characterization (Cryo-TEM, DLS, HPLC, qPCR) to bridge in vitro performance
with in vivo outcomes. Deep experience in **GLP-compliant facility management**,
technology transfer, regulatory audit preparation, and building interactive
computational tools for pharmaceutical decision-making.
"""
)

st.markdown("---")

# ── Core Competencies ───────────────────────────────────────────────────────
st.header("Core Competencies")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
#### 🧪 Formulation Strategy
Lipid Nanoparticles (LNP-mRNA), Liposomes (Doxil generics), In-Situ Forming
Implants (ISFI), PLGA Microspheres, Hydrogels

#### 💻 Computational Modeling
Mechanistic PBPK modeling (Simcyp / GastroPlus), IVIVC (Level A / B / C),
Biorelevant Dissolution Design, FIH Dose Prediction, Interactive Dashboard
Development (Python / Streamlit)
"""
    )

with col2:
    st.markdown(
        """
#### 🏭 Industrial R&D
CMC Strategy, Technology Transfer, Clinical Trial De-risking, Scale-up
Support, Stability Profiling (ICH Guidelines)

#### 📋 Regulatory & Quality
GLP Compliance, DQ / IQ / OQ / PQ Protocols, 100% Audit Success Rate,
FDA / EMA Regulatory Knowledge, Bioequivalence Strategy
"""
    )

st.markdown("---")

# ── Professional Experience ─────────────────────────────────────────────────
st.header("Professional Experience")

st.markdown(
    """
#### 🏛️ National University of Singapore · Singapore
**Senior Research Fellow** · Aug 2019 – Present
"""
)

st.markdown(
    """
- **Pfizer Inc. (USA) – Complex Generics Strategy:** Led biorelevant
  characterization platforms and established novel IVIVC models. Pioneered
  'Biomechanical Blind Spot' analysis — submitted to *Nature Biomedical
  Engineering*.
- **Sun Pharmaceuticals (India) – Bioequivalence Strategy:** Directed
  physicochemical characterization of Lipodox for bioequivalence studies
  and generic product development for the US market.
- **CureVac (Germany) – mRNA-LNP Stability:** Directed stability profiling
  of mRNA–LNP formulations under ICH-aligned conditions. Identified
  critical failure modes compromising cytosolic delivery.
- **Amaterasu Lifesciences (India) – Long-Acting Injectables:** Spearheaded
  Donepezil ISFI engineering for Alzheimer's disease. Utilized mechanistic
  PBPK modeling for First-in-Human dose prediction — submitted to
  *Nano-Micro Letters*.
- **InnoMedica (Switzerland) – Oncology Pipeline:** Managed preclinical
  studies for Talidox (liposomal doxorubicin), generating data packages
  for Clinical Trial NCT03387917.
- **GLP Facility Management:** Managed a GLP-compliant facility serving 30+
  researchers. Achieved **100% audit success rate** through rigorous SOP
  management and equipment qualification (DQ/IQ/OQ/PQ).
"""
)

st.markdown(
    """
#### 🏛️ Fraunhofer Institute IME · Frankfurt, Germany
**Postdoctoral Research Fellow** · Feb 2019 – Jul 2019

- **Global Technology Transfer:** Orchestrated transfer of formulation
  technologies from German Team to Singapore — maintaining efficiency
  between both teams.
- **AstraZeneca Collaboration:** Led formulation development for a novel
  cancer therapeutic (Clinical Trial: NCT04745689).
"""
)

st.markdown("---")

# ── Education ───────────────────────────────────────────────────────────────
st.header("Education")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
#### 🎓 Ph.D. in Chemistry
Leibniz University Hannover, Germany\n
2014 – 2018
"""
    )

with col2:
    st.markdown(
        """
#### 🎓 M.S. Pharmaceutical Biotechnology
NIPER, Mohali, India\n
2011 – 2013
"""
    )

with col3:
    st.markdown(
        """
#### 🎓 Bachelor of Pharmacy
Nirma University, India\n
2007 – 2011
"""
    )

st.markdown("---")
st.caption("Built with Streamlit · Developed by Harshvardhan Modh")
