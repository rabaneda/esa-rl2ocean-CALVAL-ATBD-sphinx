Selected Calibration methods
============================

The source provides the following section headings but no method descriptions,
input specifications, processing details, performance metrics, or expected
outputs.

ROSE-L L1 SLC products
----------------------

Short description
~~~~~~~~~~~~~~~~~

Description of inputs
~~~~~~~~~~~~~~~~~~~~~

Detailed methodology
~~~~~~~~~~~~~~~~~~~~

Performance metrics
~~~~~~~~~~~~~~~~~~~

Expected output
~~~~~~~~~~~~~~~

Numerical Weather Prediction Ocean Calibration of SAR :math:`\sigma_0`
-----------------------------------------------------------------------

The aim of the Numerical Weather Prediction Ocean Calibration (NOC)
(:ref:`Verspeek et al. (2012) <ref-verspeek-noc>`) is to provide an additional
calibration step to the SAR averaged normalized radar cross section
(:math:`\sigma_0`) values used to retrieve the wind vector. These values are
generally averaged on a grid of a few kilometres (approximately
:math:`1-2 \times 1-2\ \mathrm{km}^2`).

This calibration procedure is not applicable to sea-state parameters, since
these are derived spectrally. Therefore, an absolute :math:`\sigma_0`
calibration is not necessary before retrieval. Instead, inter-calibration
among different sea-state parameter sources can be useful for comparison and
validation; this can be achieved with triple collocation (TC). Similarly, no
additional SAR-specific calibration procedure is recommended for line-of-sight
(LoS) current retrieval beyond the harmonized Doppler calibration already part
of the ``l2o`` processor.

**Inputs**

- SAR :math:`\sigma_0` values used to retrieve the wind-vector field.
- Collocated wind vector from numerical weather prediction (NWP) models.

**Procedure**

#. Set up approximately :math:`10^7` NWP-wind/SAR-:math:`\sigma_0`
   collocations, to ensure that wind direction is sampled uniformly and that
   the wind-speed range is adequately represented. Correct :math:`\sigma_0`
   for Faraday rotation, which arises from ionospheric propagation effects at
   L-band and lower frequencies. Obtaining this many collocations requires
   1--2 months of acquisitions, depending on revisit frequency and coverage.
#. Bin collocations by incidence angle, wind direction, and wind speed, with
   bin sizes of :math:`1^\circ`, :math:`1^\circ`, and :math:`1\ \mathrm{m\,s^{-1}}`,
   respectively.
#. Compute the expected (simulated) :math:`\sigma_0` values using the
   appropriate geophysical model function (GMF):

   .. math::

      \sigma_{0}^{W,\mathrm{sim}}
      = \mathrm{GMF}(\vec{u}^{\mathrm{NWP}}, \theta, f_c, \mathrm{pol})

   Here, :math:`\vec{u}^{\mathrm{NWP}}` is the NWP wind vector, and
   :math:`\theta`, :math:`f_c`, and :math:`\mathrm{pol}` are the SAR incidence
   angle, carrier frequency of the transmitted signal, and polarization
   channel, respectively. The intended model is an L-band GMF (LMOD), analogous
   to the CMOD7 GMF used for C-band SAR satellites such as Sentinel-1
   (:ref:`Stoffelen et al. (2017) <ref-stoffelen-cmod7>`). The source marks
   further LMOD specification as to be determined.
#. Obtain the final calibration-coefficient profile by weight-averaging the
   ratios of simulated and measured :math:`\sigma_0^W` values over wind
   direction and then wind speed:

   .. math::

      \alpha(\theta)
      = \left\langle
        \left\langle
        \left\langle
        \frac{\sigma_{0}^{W,\mathrm{sim},ijk}(\theta)}
             {\sigma_{0}^{W,m,ij}(\theta)}
        \right\rangle_k
        \right\rangle_j
        \right\rangle_i .

   Here, :math:`\alpha` is the calibration correction factor; :math:`k` is
   the index of occurrences in the :math:`\{i,j\}` bin; and :math:`j` and
   :math:`i` are the wind-direction and wind-speed indices, respectively. The
   angle-bracket operator denotes the ensemble average.

Iterate the procedure until :math:`\alpha(\theta)` is close to 1, according to
the selected threshold:

.. math::

   \Delta_{\alpha}
   = \left|
      \frac{\sigma_{0}^{W,\mathrm{sim}}}{\sigma_{0}^{W,c}} - 1
     \right|
   \leq \Delta_{\alpha}^{\mathrm{th}} .

The corrected :math:`\sigma_0^W` values are:

.. math::

   \sigma_{0}^{W,c}(\theta)
   = \alpha(\theta)\sigma_{0}^{W,m}(\theta) .

In logarithmic space:

.. math::

   \sigma_{0,\mathrm{dB}}^{W,c}(\theta)
   = \alpha_{\mathrm{dB}}(\theta)
     + \sigma_{0,\mathrm{dB}}^{W,m}(\theta) .

**Metrics**

.. math::

   \Delta_{\alpha}
   = \left|
      \frac{\sigma_{0}^{W,\mathrm{sim}}}{\sigma_{0}^{W,c}} - 1
     \right| .

**Outputs**

- Calibration coefficients: :math:`\alpha(\theta)` (equivalently
  :math:`\alpha_{\mathrm{dB}}(\theta)`).
- Calibration residuals: :math:`\Delta_{\alpha}`.

GMF tuning
----------

Short description
~~~~~~~~~~~~~~~~~

Description of inputs
~~~~~~~~~~~~~~~~~~~~~

Detailed methodology
~~~~~~~~~~~~~~~~~~~~

Performance metrics
~~~~~~~~~~~~~~~~~~~

Expected output
~~~~~~~~~~~~~~~

MTF tuning
----------

Short description
~~~~~~~~~~~~~~~~~

Description of inputs
~~~~~~~~~~~~~~~~~~~~~

Detailed methodology
~~~~~~~~~~~~~~~~~~~~

Performance metrics
~~~~~~~~~~~~~~~~~~~

Expected output
~~~~~~~~~~~~~~~

Summary
-------

The source contains this heading without summary text.

.. rubric:: References

.. _ref-verspeek-noc:

Verspeek, J., A. Stoffelen, A. Verhoef, and M. Portabella (2012). “Improved
ASCAT wind retrieval using NWP ocean calibration.” *IEEE Transactions on
Geoscience and Remote Sensing*, 50(7), 2488--2494.
`doi:10.1109/TGRS.2011.2180730 <https://doi.org/10.1109/TGRS.2011.2180730>`_.

.. _ref-stoffelen-cmod7:

Stoffelen, A., J. A. Verspeek, J. Vogelzang, and A. Verhoef (2017). “The CMOD7
geophysical model function for ASCAT and ERS wind retrievals.” *IEEE Journal
of Selected Topics in Applied Earth Observations and Remote Sensing*, 10(5),
2123--2134.
`doi:10.1109/JSTARS.2017.2681806 <https://doi.org/10.1109/JSTARS.2017.2681806>`_.
