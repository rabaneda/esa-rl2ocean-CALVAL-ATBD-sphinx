Uncertainty analysis
====================

Introduction
------------

The “Evaluation of measurement data – GUM” :ref:`(BIPM et al., n.d.-a) <ref-JCGMGUM>`, or the “GUM bible”, is a foundational international document that provides a conceptual and mathematical framework for identifying sources of uncertainty, quantifying them in a consistent way (as standard deviations), combining them into a single uncertainty figure, and reporting the result and its uncertainty clearly and comparably across disciplines and countries. Focusing on evaluation and expression of uncertainty in measurement it is an important component of the science of measurement and application, known as metrology (e.g., :ref:`BIPM et al., n.d.-b <ref-JCGMVIM>`).

The GEO is an international partnership of governments and organizations acting as a policy and coordination body to promote global sharing and use of EO data, for example to support work on climate, disaster management, agriculture, water, and ecosystems. The GEOSS is the global, distributed infrastructure that GEO is building and coordinating. Rather than being a single system, it connects many independent EO systems – such as satellites, ground networks, and ocean buoys – from different countries and agencies, and aims to make them interoperable, accessible through common standards and interfaces, and accompanied by information about data quality and uncertainty. As such, GEO is the partnership, and GEOSS is the “system of systems” that GEO oversees.

To support its mission, GEOSS needs a metrological framework. As such, the 2010 endorsement of the QA4EO by the CEOS (part of GEOSS), has defined guidelines for EO applications based on principles adapted from the metrology community :ref:`(Woolliams et al. 2025a) <ref-QA4EO1>`. QA4EO aims to ensure that EO data are accessible, of known and documented quality, traceable to reference standards, in particular the SI, and suitable for user application (“fit for purpose”).

This section applies the GUM principles to SAR data and reviews the existing frameworks supporting metrology: the VIM :ref:`(BIPM et al., n.d.-b) <ref-JCGMVIM>`, the GUM :ref:`(BIPM et al., n.d.-a) <ref-JCGMGUM>`, and QA4EO. The LaTeX source also refers to section labels for level-1, level-2, error propagation, and conclusions that are not defined there. Its product-specific uncertainty-estimation headings are retained below.

The GUM Principles: A review
----------------------------

The International Vocabulary of Metrology (VIM)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The International Vocabulary of Metrology (VIM; :ref:`BIPM et al., n.d.-b <ref-JCGMVIM>`) defines and organizes key concepts in metrology to ensure global consistency in measurement science. It provides standardized terminology covering quantities, units, and measuring instruments, with a focus on measurement uncertainty rather than error.

The document explains critical properties of measuring devices, such as precision, stability, and sensitivity, and highlights the importance of traceability and standards for reliability.

Its applications span various fields, including physics, chemistry, biology, medicine, and emerging areas like forensic science and food technology. Harmonization of terms is emphasized to ensure coherence in the various scientific, engineering, regulatory, and quality assurance fields.

Guide to the Expression of Uncertainty in Measurement (GUM)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The GUM establishes general rules for evaluating and expressing uncertainty in measurement that are intended to be applicable to a broad spectrum of measurements :ref:`(BIPM et al., n.d.-a) <ref-JCGMGUM>`. The guide was developed to solve the challenge of different laboratories and disciplines using different methods and terminology for uncertainty, which made measurement results difficult to compare.

The central idea of the GUM is to treat all components of uncertainty in the same mathematical way, regardless of whether they arise from random variation or systematic effects. Every component is represented by a probability distribution and a standard uncertainty. To obtain standard uncertainties, the GUM distinguishes between two kinds of evaluation. “Type A” evaluations use statistical analysis of repeated measurements, whereas “Type B” evaluations use all other available information, such as instrument specifications, calibration certificates, or expert judgment. The results of both evaluation types can be converted into standard uncertainties so they can be used on the same terms.

Measurements are described by a mathematical model that links the quantity being measured (the measurand) to various input, or influence, quantities. Once standard uncertainties of the influence quantities are estimated, they are combined – taking into account any correlations – using standard rules for propagating variances. This yields the combined standard uncertainty of the measurand, taken as the estimated standard deviation associated with the result. An expanded uncertainty is obtained by multiplying the standard uncertainty by a coverage factor :math:`k`. The purpose of the expanded uncertainty is to provide an interval about the result of a measurement that may be expected to encompass a large fraction of the distribution of values that could reasonably be attributed to the measurand. The value of :math:`k` and how it was chosen must always be stated.

A key emphasis of the GUM is transparency. An uncertainty statement should clearly describe which inputs were considered, how each uncertainty component was obtained, what assumptions were made, and how the components were combined. The document supplements this framework with definitions, statistical background, guidance on practical evaluation, and worked examples. In doing so, it provides a common language and method that allow measurement results and their uncertainties to be understood and compared across borders and domains.

Quality Assurance Framework for Earth Observation (QA4EO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GEOSS depends on interoperable and quality-assured data to derive comprehensive information about climate and environment, as well as, e.g., food, water and energy security. To achieve interoperability across systems and datasets, common and well-defined data and metadata formats are needed, but also metrological principles such as traceability to SI, documented uncertainty analysis and comparison between different measurement references must be followed, and are key to the QA4EO reports :ref:`(Woolliams et al. 2025a) <ref-QA4EO1>`.

Beside :ref:`BIPM et al., n.d.-b <ref-JCGMVIM>` and :ref:`BIPM et al., n.d.-a <ref-JCGMGUM>`, QA4EO also builds on EO-metrology collaboration in the EU FP7 and Horizon 2020, ESA and Copernicus projects and, in particular, the FIDUCEO project :ref:`(Mittaz et al. 2019) <ref-mittaz19>`.

As summarized in :ref:`(Woolliams et al. 2025b) <ref-QA4EO2>`, three basic metrology principles generally apply to EO data:

#. **Traceability:** Metrological traceability is a property of a measurement that relates the measured value to a stated metrological reference through an unbroken chain of calibrations or comparisons. It requires, for each step in the traceability chain, that uncertainties are evaluated and that methodologies are documented.

#. **Uncertainty Analysis:** Uncertainty analysis is the review of all sources of uncertainty and the propagation of that uncertainty through the traceability chain. It is based on the suite of documents prepared by the JCGM and together known as the GUM.

#. **Comparison:** Metrologists validate uncertainty analysis and confirm traceability through comparisons. The Mutual Recognition Arrangement (a formal arrangement to confirm the degree-of-equivalence between SI realisations and disseminations in different countries) requires regular, formal international comparisons that are conducted under strict rules.

The uncertainty analysis, as outlined in the GUM, should follow these principles.

ESA has initially applied the terms FRM, FDR and TDP to describe metrologically rigorous observations of specific relevance to space-based observations :ref:`(Woolliams et al. 2025b) <ref-QA4EO2>`. The terms are increasingly being used by the broader EO community, although they have not yet been formally endorsed. The terms are defined in :ref:`Woolliams et al. 2025b <ref-QA4EO2>`, as follows:

- **Fundamental Data Record (FDR):** An FDR is a record, of sufficient duration for its application, of uncertainty-quantified sensor observations calibrated to physical units and located in time and space, together with all ancillary and lower-level instrument data used to calibrate and locate the observations and to estimate uncertainty.

- **Thematic Data Product (TDP):** A TDP is a record, of sufficient duration for its application, of uncertainty-quantified retrieved values of a geophysical variable, along with all ancillary data used in retrieval and uncertainty estimation.

- **Fiducial Reference Measurement (FRM):** An FRM is a suite of independent, fully characterised, and traceable (to a community agreed reference, ideally SI) measurements of a satellite relevant measurand, tailored specifically to address the calibration/validation needs of a class of satellite borne sensors and that follow the guidelines outlined by the GEO/CEOS QA4EO.

As highlighted by :ref:`Woolliams et al. 2025b <ref-QA4EO2>`, “TDPs provide higher level products that have been processed from FDRs, through algorithms which also often combine information from other FDRs (e.g., from other satellite sensors) or from external information (such as reanalysis models and/or certain non-satellite data), along with such additional information”. Guidelines for assessing observational systems with respect to FRMs have been established by CEOS.

In order to establish a systematic process for generating uncertainty budgets, and ensuring that EO data are interoperable, temporally stable, and fit for scientific, operational and decision-making purposes, the QA4EO and EO projects acknowledged in :ref:`Woolliams et al. 2025c <ref-QA4EO3>` have adapted the stages, suggested in GUM, required to support the development of a measurement model and from that an uncertainty analysis. These EO specific stages of uncertainty analysis are given by :ref:`Woolliams et al. 2025c <ref-QA4EO3>` as follows:

- Step 1: Define the measurand and measurement model.

- Step 2: Establish the traceability with a diagram.

- Step 3: Evaluate each source of uncertainty and fill out an effects table.

- Step 4: Calculate the data product and uncertainties.

- Step 5: Record information about the uncertainty analysis for long term data preservation purposes and summarise for today’s users.

These steps are discussed in detail in :ref:`Woolliams et al. 2025c <ref-QA4EO3>`. The product-specific headings below retain the source's intended level-1 and level-2 uncertainty-estimation scope.

Product-specific uncertainty estimation
----------------------------------------

The source provides headings for the following product analyses, but no detailed
measurement models, traceability matrices, effect evaluations, uncertainty
calculations, or output documentation beneath them.

Azimuth wavelength cutoff
~~~~~~~~~~~~~~~~~~~~~~~~~

- Description of measurand and measurement model
- Traceability matrix
- Evaluation of effects
- Calculation of associated uncertainties
- Documentation and outputs

MACS
~~~~

- Description of measurand and measurement model
- Traceability matrix
- Evaluation of effects
- Calculation of associated uncertainties
- Documentation and outputs

iMACS
~~~~~

- Description of measurand and measurement model
- Traceability matrix
- Evaluation of effects
- Calculation of associated uncertainties
- Documentation and outputs

DCA
~~~

- Description of measurand and measurement model
- Traceability matrix
- Evaluation of effects
- Calculation of associated uncertainties
- Documentation and outputs

Texture-based azimuth cutoff
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Description of measurand and measurement model
- Traceability matrix
- Evaluation of effects
- Calculation of associated uncertainties
- Documentation and outputs

RVL
~~~

- Description of measurand and measurement model
- Traceability matrix
- Evaluation of effects
- Calculation of associated uncertainties
- Documentation and outputs

Inverse Wave Age
~~~~~~~~~~~~~~~~

- Description of measurand and measurement model
- Traceability matrix
- Evaluation of effects
- Calculation of associated uncertainties
- Documentation and outputs

Wind products
~~~~~~~~~~~~~

Wind speed, wind stress, and hub height wind speed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Description of measurand and measurement model
- Traceability matrix
- Evaluation of effects
- Calculation of associated uncertainties
- Documentation and outputs

Sea-state products
~~~~~~~~~~~~~~~~~~

Total significant wave height; mean period wind-sea; first and second moment
wave period; wave height for the swell-dominant and swell-secondary systems;
significant wave height wind-sea; wave direction; and wave directional energy
spectrum.

- Description of measurand and measurement model
- Traceability matrix
- Evaluation of effects
- Calculation of associated uncertainties
- Documentation and outputs

Line-of-sight current products
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Line-of-sight wave Doppler and line-of-sight surface current component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Description of measurand and measurement model
- Traceability matrix
- Evaluation of effects
- Calculation of associated uncertainties
- Documentation and outputs

Summary
~~~~~~~

The source contains this heading without summary text.

References
----------

.. _ref-jcgmgum:

BIPM, IEC, IFCC, et al. n.d.-a. *Evaluation of Measurement Data — Guide to the
Expression of Uncertainty in Measurement*. Joint Committee for Guides in
Metrology, JCGM 100:2008. `doi:10.59161/JCGM100-2008E
<https://doi.org/10.59161/JCGM100-2008E>`_.

.. _ref-jcgmvim:

BIPM, IEC, IFCC, et al. n.d.-b. *International Vocabulary of Metrology - Basic
and General Concepts and Associated Terms (VIM)*. Joint Committee for Guides in
Metrology, JCGM 200:2012(E/F).

.. _ref-mittaz19:

Mittaz, Jonathan, Christopher J. Merchant, and Emma R. Woolliams. 2019.
“Applying Principles of Metrology to Historical Earth Observations from
Satellites.” *Metrologia* 56 (3).
`doi:10.1088/1681-7575/ab1705 <https://doi.org/10.1088/1681-7575/ab1705>`_.

.. _ref-qa4eo1:

Woolliams, Emma, Sajedeh Behnia, Agnieszka Bialek, et al. 2025a. *General
Guidance on a Metrological Approach to Fundamental Data Records (FDR), Thematic
Data Products (TDP) and Fiducial Reference Measurements (FRM) - Executive
Summary*. National Physical Laboratory.

.. _ref-qa4eo2:

Woolliams, Emma, Sajedeh Behnia, Agnieszka Bialek, et al. 2025b. *General
Guidance on a Metrological Approach to Fundamental Data Records (FDR), Thematic
Data Products (TDP) and Fiducial Reference Measurements (FRM) - Metrology
Theoretical Basis*. National Physical Laboratory.

.. _ref-qa4eo3:

Woolliams, Emma, Sajedeh Behnia, Agnieszka Bialek, et al. 2025c. *General
Guidance on a Metrological Approach to Fundamental Data Records (FDR), Thematic
Data Products (TDP) and Fiducial Reference Measurements (FRM) - Uncertainty
Analysis Process*. National Physical Laboratory.
