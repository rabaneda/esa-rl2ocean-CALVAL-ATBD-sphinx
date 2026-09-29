RL2Ocean Calibration and Validation ATBD
========================================

This Sphinx project migrates the LaTeX source document
``esa_rl2ocean_CALVAL_ATBD`` into the ADPM template structure. The original
document ID and issue (ESA-RL2OCEAN-CALVAL-ATBD, version 0.2) are retained.

The LaTeX source contains substantive introduction and GUM/QA4EO material, but
many calibration, validation, and product uncertainty sections consist only of
headings. Those outlines are preserved and their missing details are called
out; no algorithm content has been invented. The source abstract contains
Lorem ipsum placeholder text, so it is not included.

All source figures and the BibTeX database are copied into ``adpm/``. The only
active figures referenced by the source are cover logos; diagrams in commented
LaTeX are not rendered. No Jupyter notebooks were provided with the source, so
none have been fabricated.

Build HTML or PDF from this directory with the existing ``adpm`` environment::

   conda run -n adpm make html
   conda run -n adpm make pdf

Generated files are written under ``adpm/_build/``.
