################################
 Processing model and data flow
################################

Overview and top-down decomposition
===================================

The source describes the calibration and validation activities across the
ROSE-L mission phases. It does not provide a detailed processing-block
decomposition or an algorithm-level data-flow diagram.

Pre-launch phase (D)
====================

During the pre-launch phase (phase D), activities focus on preparing and
validating the L2 processing chain, ensuring readiness for on-orbit operations.
Key tasks include finalizing L2 requirements, algorithms, and performance
budgets. Simulators and proxy datasets are leveraged to validate retrieval
algorithms and uncertainty models. Pre-launch instrument characterization is
integrated into the processing chain to ensure retrievals are robust to on-orbit
conditions. A comprehensive Cal/Val Plan is developed, identifying validation
sites, protocols, data matchups, and metrics.

Commissioning phase (IOC or E1)
===============================

In the commissioning phase (IOC or phase E1), the primary goal is to validate
L2 products using on-orbit data and release initial beta/provisional products
with documented performance. Early activities include confirming L1
performance, performing vicarious calibrations, and matching L2 products with
ground-based and airborne reference datasets (FRM sites, buoys, ship-based
campaigns, etc.). Algorithms are fine-tuned using real-time data, and initial
uncertainty models are validated. Early reprocessing cycles are conducted to
improve product stability, and performance against key metrics is assessed.
Products are released with quality summaries, and ongoing monitoring dashboards
are set up.

Exploitation phase (E2)
=======================

The exploitation phase (phase E2) ensures L2 products maintain accuracy,
precision, and stability over the mission lifecycle. Routine validation is
conducted using reference networks, continuous KPI monitoring, and periodic
reprocessing cycles for algorithm and calibration improvements. Traceability
to standards (QA4EO, FRM) and uncertainty validation is maintained, while
long-term drift corrections support stable time series. Community engagement,
user feedback, and updates to documentation (validation reports, product
guides) are prioritised. The goal is to achieve validated product maturity,
ensuring high-quality data for science and operational applications.

End-to-end data flow
====================

No end-to-end processing-flow diagram, processing-step mapping, or algorithm
identifiers are provided in the source LaTeX document.
