Sea State
=========

.. _alg-009:

Empirical retrieval of wave parameters - ALG-009
------------------------------------------------

:tbd:`ALG-009 VDT | table copied from ADPM v1.0, to be aligned with the Cal/Val needs`

.. list-table:: ALG-009 Variable Description Table (VDT).
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
    * - 10m wind vector from SAR
      - :math:`\vec{u}`
      - IN
      - PRO_WND
      - ALG-009
      - m/s
      - float32
      - 2D
      - ???
      - N/A
    * - 10m wind vector from model
      - :math:`\vec{u}_m`
      - IN
      - AUX_WND
      - ALG-009
      - m/s
      - float32
      - 2D
      - ???
      - N/A
    * - Image features
      - FEAT
      - IN
      - L2O_PRE_PRO
      - ALG-009
      - 1
      - float32
      - 3D (az, rng, feat_id)
      - ???
      - N/A
    * - Linear regression model
      - :math:`c_{i}^{j}`
      - IN
      - AUX_LRS
      - ALG-009
      - 1
      - float32
      - 2D (feat_id, acq_mode_and_pol)
      - ???
      - N/A
    * - Machine learning model
      - ???
      - IN
      - AUX_MLS
      - ALG-009
      - 1
      - float32
      - ??? (svr_vec, acq_mode_and_pol)
      - ???
      - N/A
    * - Processing parameters
      - --
      - IN
      - AUX_PP
      - ALG-009
      - N/A
      - ???
      - ???
      - N/A
      - N/A
    * - Total significant wave height
      - :math:`H_s`
      - OUT
      - ALG-009
      - L2O_WAV
      - m
      - float32
      - 2D
      - [0,)
      - N/A
    * - Mean wave period
      - :math:`T_{m0-1}`
      - OUT
      - ALG-009
      - L2O_WAV
      - s
      - float32
      - 2D
      - [0,)
      - N/A
    * - Second moment wave period
      - :math:`T_{m2}`
      - OUT
      - ALG-009
      - L2O_WAV
      - s
      - float32
      - 2D
      - [0,)
      - N/A
    * - Wave height swell dominant system
      - :math:`H_{ssw1}`
      - OUT
      - ALG-009
      - L2O_WAV
      - m
      - float32
      - 2D
      - [0,)
      - N/A
    * - Wave height swell secondary system
      - :math:`H_{ssw2}`
      - OUT
      - ALG-009
      - L2O_WAV
      - m
      - float32
      - 2D
      - [0,)
      - N/A
    * - Significant wave height windsea
      - :math:`H_{sww}`
      - OUT
      - ALG-009
      - L2O_WAV
      - m
      - float32
      - 2D
      - [0,)
      - N/A
    * - Mean period swell dominant system
      - :math:`T_{sw1}`
      - OUT
      - ALG-009
      - L2O_WAV
      - s
      - float32
      - 2D
      - [0,)
      - N/A
    * - Mean period swell secondary system
      - :math:`T_{sw2}`
      - OUT
      - ALG-009
      - L2O_WAV
      - s
      - float32
      - 2D
      - [0,)
      - N/A
    * - Mean period windsea
      - :math:`T_{ww}`
      - OUT
      - ALG-009
      - L2O_WAV
      - s
      - float32
      - 2D
      - [0,)
      - N/A
    * - Mean direction swell dominant system
      - :math:`\phi_{sw1}`
      - OUT
      - ALG-009
      - L2O_WAV
      - degree
      - float32
      - 2D
      - :math:`[0,360)`
      - N/A
    * - Mean direction swell secondary system
      - :math:`\phi_{sw2}`
      - OUT
      - ALG-009
      - L2O_WAV
      - degree
      - float32
      - 2D
      - :math:`[0,360)`
      - N/A
    * - Mean direction windsea
      - :math:`\phi_{ww}`
      - OUT
      - ALG-009
      - L2O_WAV
      - degree
      - float32
      - 2D
      - :math:`[0,360)`
      - N/A

.. _alg-009b:

Reconstruction of wave spectra - ALG-009b
-----------------------------------------

:tbd:`ALG-009b VDT | table copied from ADPM v1.0, to be aligned with the Cal/Val needs`

.. list-table:: ALG-009b Variable Description Table (VDT).
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
    * - Processing parameters
      - --
      - IN
      - AUX_PP
      - ALG-009
      - N/A
      - ???
      - ???
      - N/A
      - N/A
    * - 10m wind vector from SAR
      - :math:`\vec{u}`
      - IN
      - PRO_WND
      - ALG-009
      - m/s
      - float32
      - 2D
      - ???
      - N/A
    * - 10m wind vector from model
      - :math:`\vec{u}_m`
      - IN
      - AUX_WND
      - ALG-009
      - m/s
      - float32
      - 2D
      - ???
      - N/A
    * - Total significant wave height
      - :math:`H_s`
      - IN
      - ALG-009
      - L2O_WAV
      - m
      - float32
      - 2D
      - [0,)
      - N/A
    * - Mean wave period
      - :math:`T_{m0-1}`
      - IN
      - ALG-009
      - L2O_WAV
      - s
      - float32
      - 2D
      - [0,)
      - N/A
    * - Second moment wave period
      - :math:`T_{m2}`
      - IN
      - ALG-009
      - L2O_WAV
      - s
      - float32
      - 2D
      - [0,)
      - N/A
    * - Wave height swell dominant system
      - :math:`H_{ssw1}`
      - IN
      - ALG-009
      - L2O_WAV
      - m
      - float32
      - 2D
      - [0,)
      - N/A
    * - Wave height swell secondary system
      - :math:`H_{ssw2}`
      - IN
      - ALG-009
      - L2O_WAV
      - m
      - float32
      - 2D
      - [0,)
      - N/A
    * - Significant wave height windsea
      - :math:`H_{sww}`
      - IN
      - ALG-009
      - L2O_WAV
      - m
      - float32
      - 2D
      - [0,)
      - N/A
    * - Mean period swell dominant system
      - :math:`T_{sw1}`
      - IN
      - ALG-009
      - L2O_WAV
      - s
      - float32
      - 2D
      - [0,)
      - N/A
    * - Mean period swell secondary system
      - :math:`T_{sw2}`
      - IN
      - ALG-009
      - L2O_WAV
      - s
      - float32
      - 2D
      - [0,)
      - N/A
    * - Mean period windsea
      - :math:`T_{ww}`
      - IN
      - ALG-009
      - L2O_WAV
      - s
      - float32
      - 2D
      - [0,)
      - N/A
    * - Mean direction swell dominant system
      - :math:`\phi_{sw1}`
      - IN
      - ALG-009
      - L2O_WAV
      - degree
      - float32
      - 2D
      - :math:`[0,360)`
      - N/A
    * - Mean direction swell secondary system
      - :math:`\phi_{sw2}`
      - IN
      - ALG-009
      - L2O_WAV
      - degree
      - float32
      - 2D
      - :math:`[0,360)`
      - N/A
    * - Mean direction windsea
      - :math:`\phi_{ww}`
      - IN
      - ALG-009
      - L2O_WAV
      - degree
      - float32
      - 2D
      - :math:`[0,360)`
      - N/A
    * - Wave spectral energy density
      - :math:`S`
      - OUT
      - ALG-009b
      - L2O_WAV
      - :math:`m^2/Hz`
      - float32
      - 4D (az, rng, freq, dir)
      - [0,)
      - N/A
