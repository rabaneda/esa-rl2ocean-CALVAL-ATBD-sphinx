Introduction
============

Purpose and scope
-----------------

The Copernicus Programme, established by the European Union, is a framework for Earth Observation and Monitoring, designed to support environmental protection, civil protection, and civil security efforts. At the heart of this programme is the Copernicus Space Component (CSC), which comprises the Sentinel missions. These missions are integral to providing essential data across various thematic domains, thereby facilitating informed decision-making and policy development.

One of the new advancements within this framework is the Copernicus Radar Observing System for Europe – L-Band (ROSE-L). This initiative is aimed at enhancing existing capabilities by introducing L-band Synthetic Aperture Radar (SAR) data. The L-band SAR is set to complement the C-band radar data provided by Sentinel-1, thus addressing specific observational needs within environmental and maritime surveillance.

Cal/Val context
---------------

Quality Assessment (QA) is required for remote sensing and Earth Observation (EO) instruments in order to produce reliable measurements and ensure accuracy. Quality of products are commonly assessed through a Calibration and Validation process (Cal/Val). Consequently, the development of the prototype and operational ROSE-L Ocean products processors (L2O-GPP and L2O-IPF respectively) must be followed by the validation of products. A validation strategy is meant to be planned prior to calibration and validation activities. The required strategy shall cover different stages of the processor and different phases of ROSE-L mission, from pre-launch (phase D) to exploitation (phase E2). The strategy shall include methodologies, datasets, performance and uncertainty metrics.

The ROSE-L instrument will operate in scanning synthetic aperture radar (ScanSAR) mode. The system will support Dual-Pol, Quad-Pol and Wave modes. The Cal/Val strategy is also meant to cover all modes and polarizations. ROSE-L will not be the first SAR system functioning within L-band. ALOS, ALOS-2, ALOS-4, SAOCOM and NiSAR are, or have been, operating in L-band too. However, there are differences between those systems and the ROSE-L system, e.g. incidence angle, range bandwidth, swath width, among others. Furthermore, ROSE-L incorporates the use of a new technique, the Scan-On-Receive (SCORE) technique with Multiple Azimuth Phase Centers (MAPS). The different instrument design will impose differences in the retrievals at low level which are meant to influence the inversion into L2 products.

Regarding the development of a retrieval algorithm but also Cal/Val activities, instrument differences between ROSE-L and previous SAR L-band instruments impose a challenge; the need of producing and validating ocean products from ROSE-L scenes during the pre-launch phase. The lack of real ROSE-L data will be mitigated by the use of similar acquisitions by the above-mentioned systems; although this introduces a non-negligible degree of uncertainty. For Cal/Val purposes, simulated ROSE-L scenes will be produced. The achievable accuracy of simulated ROSE-L will also be analysed during the In-Orbit-Commissioning (IOC) phase, E1. Once real ROSE-L data is available, the outputs from the L2O-IPF processor will need to be validated again, with the possibility to encounter a need for a readjustment of the processor or introduction of supplementary calibration steps.

A tool for assessing the quality of the ocean products is vital. The Cal/Val tool, L2O-QC, is meant to be developed in parallel to the development of the ocean processors, L2O-GPP and L2O-IPF. The L2O-QC software is required to be able to ingest datasets of different nature; ROSE-L acquisitions, reference datasets (either in-situ or remote), and auxiliary data. The goal is to collocate the different datasets in order to undertake the quality assessment, where the accuracy and reliability of the ROSE-L L2 ocean products will be determined and ensured. The underlying objective is to provide users with a set of performance and uncertainty metrics necessary for a deep understanding of the products and subsequent appropriate use and application.

L2 product scope
----------------

The L2 products to validate are already listed in the objectives of L2O-GPP and L2O-IPF: Ocean Surface Vector Stress (OSVS), Sea State, and line-of-sight (LoS) surface currents. Within each of the three thematic products, the following L2 variables are meant to be produced and therefore validated:

- OSVS:

  - Wind vector

  - Wind stress

  - Hub height wind speed

- Sea state:

  - Total significant wave height

  - Mean period wind-sea

  - First moment wave period

  - Second moment wave period

  - Wave height swell dominant system

  - Wave height swell secondary system

  - Significant wave height wind-sea

  - Wave direction

  - Wave directional energy spectrum

- LoS currents:

  - LoS wave Doppler

  - LoS surface current component

Cal/Val objectives and performance
----------------------------------

The key objectives of the Calibration and Validation (Cal/Val) phase include ensuring that all L2 geophysical products meet internationally recognized standards, such as SI traceability, and align with QA4EO principles to guarantee high data quality. Cal/Val aims to validate the accuracy, precision, and stability of L2 products using independent datasets, such as Fiducial Reference Measurements (FRM), and cross-sensor harmonization. A critical focus is on quantifying and documenting uncertainty propagation from instrument measurements to retrievals while ensuring the retrieval algorithms are robust under diverse environmental conditions.

To meet performance requirements, L2 products must achieve predefined thresholds in accuracy, precision, and stability, with uncertainties traceable and reliable across pixel and aggregate levels. Products must demonstrate consistency over full mission coverage, addressing global, regional, and temporal scales, and maintain defined operational latencies (e.g., near-real-time or reprocessed outputs). Validation activities use measurable metrics, including statistical bias, RMS error, and spatial-temporal coverage rates, to assess product quality systematically. Lastly, the outputs should be delivered in user-ready formats with comprehensive documentation while maintaining version control and data provenance.

ATBD purpose
------------

The aim of the Calibration and Validation Algorithm Theoretical Basis Document (ATBD) is to provide a comprehensive and transparent description of the scientific principles, mathematical methods, and processing steps used to generate ROSE-L L2 ocean products. It ensures that the algorithms are well-documented, reproducible, and traceable, facilitating a clear understanding of how measurements are transformed into geophysical quantities. The ATBD serves as a foundation for ensuring data quality, guiding calibration/validation efforts, and supporting user confidence in the satellite mission’s outputs.

Applicable and reference documents
----------------------------------


Acronyms
--------

.. glossary::
   :sorted:

   CANVAS
      CAlibration aNd VAlidation for Sar.

   CEOS
      Committee on Earth Observation Satellites.

   DC
      Doppler Centroid.

   DCA
      Doppler Centroid Anomaly.

   DORIS
      Doppler Orbitography and Radiopositioning Integrated by Satellite.

   EO
      Earth observation.

   ESA
      European Space Agency.

   EU
      European Union.

   FDR
      Fundamental Data Record.

   FIDUCEO
      Fidelity and Uncertainty in Climate Data Records from Earth Observation.

   FP7
      Seventh Framework Programme.

   FRM
      Fiducial Reference Measurement.

   GEO
      Group on Earth Observations.

   GEOSS
      Global Earth Observation System of Systems.

   GUM
      Guide to the expression of Uncertainty in Measurement.

   JCGM
      Joint Committee for Guides in Metrology.

   QA4EO
      Quality Assurance Framework for Earth Observation.

   SAR
      Synthetic Aperture Radar.

   SI
      International System of Units.

   TDP
      Thematic Data Product.

   UTD
      Uncertainty Tree Diagram.

   VIM
      International Vocabulary of Metrology.

Definitions and conventions
---------------------------

.. glossary::
   :sorted:

   Accuracy
      The quality of being near to the true value. The source marks this
      definition as requiring a reference.

   Comparison
      Metrologists validate uncertainty analysis and confirm traceability
      through comparisons. The Mutual Recognition Arrangement requires
      regular, formal international comparisons to establish the degree of
      equivalence between SI realisations and disseminations in different
      countries.

   Dataset
      A combination of data records, such as numerical values needed to analyse
      and interpret a natural process, and the related information content.

   Fundamental Data Record
      A record, of sufficient duration for its application, of
      uncertainty-quantified sensor observations calibrated to physical units
      and located in time and space, together with ancillary and lower-level
      instrument data used to calibrate and locate the observations and to
      estimate uncertainty (:ref:`Woolliams et al. 2025a <ref-QA4EO1>`).

   Fiducial Reference Measurement
      A suite of independent, fully characterised, and traceable sub-orbital
      measurements, relevant to space-based observations, following the
      guidelines of the GEO/CEOS Quality Assurance Framework for Earth
      Observation (QA4EO).

   Interoperability
      The ability of data or tools from non-cooperating resources to integrate
      or work together with minimal effort (`Wilkinson et al. (2016)
      <https://doi.org/10.1038/sdata.2016.18>`_).

   Interoperable
      Describes data or tools from non-cooperating resources that can integrate
      or work together with minimal effort (`Wilkinson et al. (2016)
      <https://doi.org/10.1038/sdata.2016.18>`_).

   Measurand
      The quantity intended to be measured, and the single output quantity from
      a measurement model.

   Metrology
      The science of measurement and its application
      (:ref:`BIPM et al., n.d.-b <ref-JCGMVIM>`).

   Thematic Data Product
      A record, of sufficient duration for its application, of
      uncertainty-quantified retrieved values of a geophysical variable, along
      with ancillary data used in retrieval and uncertainty estimation.

   Traceability
      A property of a measurement relating its value to a stated metrological
      reference through an unbroken chain of calibrations or comparisons, with
      uncertainties evaluated and methodologies documented at each step.

   Uncertainty analysis
      The review of uncertainty sources and their propagation through the
      traceability chain, based on the suite of documents prepared by the JCGM
      and known as the GUM.
