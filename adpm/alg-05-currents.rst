Total Surface Currents
======================

.. _alg-010:

Wave Doppler estimation - ALG-010
---------------------------------

:tbd:`ALG-010 VDT | table copied from ADPM v1.0, to be aligned with the Cal/Val needs`

.. list-table:: ALG-010 Variable Description Table (VDT).
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
    * - Stress equivalent wind
      - :math:`\hat{\mathbf{U}}_{10s}`
      - IN
      - PRO_WND
      - ALG-010
      - m s\ :sup:`-1`
      - TBD
      - 2D
      - TBD
      - N/A
    * - Inverse wave age
      - :math:`\Omega`
      - IN
      - L2O_PRE_PROD
      - ALG-010
      - --
      - TBD
      - 2D
      - TBD
      - N/A
    * - Mean Cross Spectrum
      - MACS
      - IN
      - L2O_PRE_PROD
      - ALG-010
      - --
      - TBD
      - 2D
      - TBD
      - N/A
    * - Total significant wave height
      - :math:`H_s`
      - IN
      - PRO_WAV+AUX_WAV
      - ALG-010
      - m
      - float32
      - 2D
      - [0,)
      - N/A
    * - Mean wave period
      - :math:`T_m`
      - IN
      - PRO_WAV+AUX_WAV
      - ALG-010
      - s
      - float32
      - 2D
      - [0,)
      - N/A
    * - Mean wave propagation direction
      - :math:`\phi_m`
      - IN
      - PRO_WAV+AUX_WAV
      - ALG-010
      - degrees
      - TBD
      - 2D
      - TBD
      - N/A
    * - Line of sight wave-Doppler
      - :math:`\hat{\mathbf{v}}_{wD}`
      - OUT
      - PRO_WAV+AUX_WAV
      - ALG-010
      - m s\ :sup:`-1`
      - TBD
      - 2D
      - [0,)
      - N/A

.. _alg-011:

Ocean Surface Current estimation - ALG-011
------------------------------------------

:tbd:`ALG-011 VDT | table copied from ADPM v1.0, to be aligned with the Cal/Val needs`

.. list-table:: ALG-011 Variable Description Table (VDT).
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
    * - Doppler Centroid Anomaly
      - :math:`f_{D}`
      - IN
      - L1_DCA
      - ALG-011
      - Hz
      - TBD
      - 2D
      - TBD
      - N/A
    * - Line of sight wave-Doppler
      - :math:`\hat{\mathbf{v}}_{wD}`
      - IN
      - ALG-010
      - ALG-011
      - m s\ :sup:`-1`
      - TBD
      - 2D
      - [0,)
      - N/A
    * - Line of sight ocean surface current
      - :math:`\hat{\mathbf{v}}_{osc}`
      - OUT
      - ALG-010
      - ALG-011
      - m s\ :sup:`-1`
      - TBD
      - 2D
      - [0,)
      - N/A
