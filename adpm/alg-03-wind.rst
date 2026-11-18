Wind
====

.. _alg-007:

Bayesian Wind Retrieval - ALG-007
---------------------------------

:tbd:`ALG-007 VDT | table copied from ADPM v1.0, to be aligned with the Cal/Val needs`

.. list-table:: ALG-007 Variable Description Table (VDT).
    :header-rows: 1
    :class: longtable
    :widths: 16 7 8 16 16 7 12 10 12 12

    * - Name
      - Sym
      - Role
      - Origin
      - Destination
      - Units
      - Type
      - Dim
      - Range
      - Default
    * - Background wind vector
      - :math:`\mathbf{u}_B`
      - IN
      - AUX_WND
      - ALG-007
      - m s\ :sup:`-1`
      - TBD
      - 2-D field
      - TBD
      - N/A
    * - Averaged NRCS
      - :math:`\sigma^0`
      - IN
      - L1_SLC / upstream processing
      - ALG-007
      - 1
      - TBD
      - 2-D field
      - TBD
      - N/A
    * - Azimuth wavelength cut-off
      - :math:`\lambda_C`
      - IN
      - L2O_PRE_PROD
      - ALG-007
      - m
      - TBD
      - 2-D / tiled field
      - TBD
      - N/A
    * - Imaginary Mean Cross Spectrum
      - iMACS
      - IN
      - L2O_PRE_PROD
      - ALG-007
      - TBD
      - TBD
      - 2-D / tiled field
      - TBD
      - N/A
    * - Doppler Centroid Anomaly
      - DCA
      - IN
      - L2O_PRE_PROD
      - ALG-007
      - Hz
      - TBD
      - 2-D / tiled field
      - TBD
      - N/A
    * - Cross-Correlation Polarisation Coherence
      - CCPC
      - IN
      - Wind processing
      - ALG-007
      - TBD
      - TBD
      - 2-D / tiled field
      - TBD
      - N/A
    * - Wind-retrieval GMFs
      - --
      - IN
      - AUX_GMF
      - ALG-007
      - --
      - TBD
      - --
      - TBD
      - N/A
    * - Ocean calibration factors
      - --
      - IN
      - AUX_OC
      - ALG-007
      - TBD
      - TBD
      - --
      - TBD
      - N/A
    * - ML wind-direction information
      - :math:`\phi_{ML}`
      - IN
      - AUX_MLW / wind processing
      - ALG-007
      - deg
      - TBD
      - 2-D field
      - TBD
      - N/A
    * - Processing parameters
      - --
      - IN
      - AUX_PP
      - ALG-007
      - --
      - TBD
      - --
      - TBD
      - TBD
    * - Retrieved wind vector
      - :math:`\mathbf{u}`
      - OUT
      - ALG-007
      - L2O_WND
      - m s\ :sup:`-1`
      - TBD
      - 2-D field
      - TBD
      - N/A
    * - Wind stress
      - :math:`\boldsymbol{\tau}`
      - OUT
      - ALG-007
      - L2O_WND
      - N m\ :sup:`-2`
      - TBD
      - 2-D field
      - TBD
      - N/A
    * - Retrieval configuration flag
      - --
      - OUT
      - ALG-007
      - L2O_WND
      - --
      - TBD
      - 2-D field
      - TBD
      - N/A
    * - Retrieval quality information
      - --
      - OUT
      - ALG-007
      - L2O_WND
      - --
      - TBD
      - 2-D field
      - TBD
      - N/A

.. _alg-008:

Storm-centric Processing - ALG-008 [TBC]
----------------------------------------

:tbd:`ALG-008 VDT | table copied from ADPM v1.0, to be aligned with the Cal/Val needs`

.. list-table:: ALG-008 Variable Description Table (VDT).
    :header-rows: 1
    :class: longtable
    :widths: 16 7 8 16 16 7 12 10 12 12

    * - Name
      - Sym
      - Role
      - Origin
      - Destination
      - Units
      - Type
      - Dim
      - Range
      - Default
    * - [Variable name]
      - [Symbol]
      - [Role {IN, OUT, IN/OUT}]
      - [Origin]
      - [Destination]
      - [Units]
      - [Data Type]
      - [Dimensionality]
      - [Range]
      - [Default]
