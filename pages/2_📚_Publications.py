"""
Page 2: Publications — Selected Peer-Reviewed Works
"""

import streamlit as st

st.set_page_config(
    page_title="Publications — Harshvardhan Modh",
    page_icon="📚",
    layout="wide",
)

st.title("📚 Publications")
st.markdown("### Selected Peer-Reviewed Works")

st.markdown(
    """
**19 peer-reviewed publications** ·
🎓 [Full list on Google Scholar](https://scholar.google.de/citations?user=J2dpG98AAAAJ&hl=en)
"""
)

st.markdown("---")

# ── Submitted / In Revision ─────────────────────────────────────────────────
st.header("Submitted & In Revision")

st.markdown(
    """
1. **Modh H**, et al. "Resolving the biomechanical blind spot in
   nanomedicine translation." *Nature Biomedical Engineering*
   (Submitted, 2026).

2. **Modh H**, et al. "Biorelevant BioJect Release Testing and Mechanistic
   PBPK Modeling Enable First-in-Human Dose Prediction for Long-Acting
   Injectables." *Nano-Micro Letters* (In Revision, 2026).
"""
)

st.markdown("---")

# ── Published ───────────────────────────────────────────────────────────────
st.header("Published")

st.markdown(
    """
3. **Modh H**, et al. "Injectable drug delivery systems of doxorubicin
   revisited: In vitro–in vivo relationships using the biomechanical
   approach." *Int. J. Pharm.* 611, 121314 (2021).
   [DOI](https://doi.org/10.1016/j.ijpharm.2021.121314)

4. **Mast M-P**, **Modh H**, et al. "Nanomedicine at the crossroads — A
   quick guide for IVIVC." *Adv. Drug Deliv. Rev.* 179, 113829 (2021).
   [DOI](https://doi.org/10.1016/j.addr.2021.113829)
"""
)

st.markdown("---")

st.info(
    """
**Note:** Only selected publications are shown here. For the complete list
including citation metrics and h-index, visit
[Google Scholar](https://scholar.google.de/citations?user=J2dpG98AAAAJ&hl=en).
"""
)

st.markdown("---")
st.caption("Publication data updated February 2026.")
