"""Rebuild the investor brief.

Edit brief.src.html, then run from this folder:
    python3 build.py
    chrome --headless=new --no-pdf-header-footer \
      --print-to-pdf=Caffevolve_Investor_Brief.pdf Caffevolve_Investor_Brief.html

build.py inlines the Cormorant Garamond / Inter / DM Mono fonts (fonts-embedded.css)
so the HTML is a single offline file and the PDF renders identically anywhere.
"""
from pathlib import Path

here = Path(__file__).parent
src = (here / "brief.src.html").read_text()
fonts = (here / "fonts-embedded.css").read_text()
(here / "Caffevolve_Investor_Brief.html").write_text(src.replace("/*FONTS*/", fonts))
