RL2Ocean Calibration and Validation ATBD
========================================

This Sphinx project migrates the LaTeX source document
``esa_rl2ocean_CALVAL_ATBD`` into the ADPM template structure. The original
document ID is retained. The current ATBD issue is 1.0; the source document
was version 0.2.

The LaTeX source contains substantive introduction and GUM/QA4EO material.
Calibration and validation method descriptions from the CVTDD have also been
integrated into the corresponding ATBD sections. Other method and
product-uncertainty sections that contain headings only in the source retain
those outlines, with missing details called out; no algorithm content has been
invented. The source abstract contains Lorem ipsum placeholder text, so it is
not included.

Sections 3–5 of the CVDDD have been added before the algorithms chapter. The
L-band SAR and auxiliary dataset chapters retain the source outline and identify
where descriptions were not provided. The reference-dataset chapter includes
its source figures, formatted references, and the original CVDDD BibTeX database
as ``adpm/cvddd_bibliography.bib``. The ATBD figures and BibTeX database are
also included in ``adpm/``. No Jupyter notebooks were provided with the source,
so none have been fabricated.

Build HTML or PDF from this directory with the existing ``adpm`` environment::

   conda run -n adpm make html
   conda run -n adpm make pdf

Generated files are written under ``adpm/_build/``.
