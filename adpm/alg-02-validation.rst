Validation
==========

Spatial Variance
----------------

Spatial Variance is a method used to estimate the representativeness error
:math:`r^2`, which is a key component for triple collocation (TC). This
procedure estimates the spatial variance for a given geophysical parameter.
Let :math:`s_1` and :math:`s_2` be two different sources characterized by
different spatial resolutions, where :math:`V_{s_1}(n)` and
:math:`V_{s_2}(n)` represent their spatial variances at spatial lag :math:`n`.
Given :math:`n_{\max}`, the maximum lag, the representativeness error of
:math:`s_1` (the coarsest system) compared to :math:`s_2` can be estimated as:

.. math::
   :label: eq-cvtdd-r2-spatial-variance

   r^2 = \sum_{n=0}^{n_{\max}}
   \left[V_{s_2}(n)-V_{s_1}(n)\right] .

Let :math:`\tilde{n}<n_{\max}` be the spatial-lag threshold above which both
systems capture the same signal variability. The residual contribution then
vanishes:

.. math::

   V_{s_2}(n)-V_{s_1}(n) \to 0
   \qquad \forall n>\tilde{n} .

**Purpose**

This method (:ref:`Vogelzang et al. (2015) <ref-vogelzang-spatial-variance>`)
computes wind variances as a function of scale. Unlike the spectral-integration
method, it operates in the spatial domain rather than the frequency domain. It
is more tolerant to missing samples and provides a more intuitive
interpretation. The representativeness error is the difference between the
system 2 (e.g. satellite) spatial variance and that of system 3 (e.g. model).
This value depends on the selected scale. Spatial variances increase
monotonically with scale, and their difference also usually increases up to a
certain scale.

**Inputs**

- Vector samples of the required geophysical parameter.

**Procedure**

#. Estimate the first-order moments for both components of the geophysical
   parameter of interest:

   .. math::
      :label: eq-cvtdd-spatial-first-moment

      M_{w,i}(n)
      = \frac{1}{n+1}\sum_{j=0}^{n}w_{i+j} .

   Here, :math:`w` is the component of the geophysical parameter of interest,
   :math:`n` is the lag size, and :math:`i` is an ancillary index identifying
   the starting element.
#. Estimate the second-order moments:

   .. math::
      :label: eq-cvtdd-spatial-second-moment

      M_{ww,i}(n)
      = \frac{1}{n+1}\sum_{j=0}^{n}w^{2}_{i+j} .

   The subscript :math:`w` denotes the first-order moment, while :math:`ww`
   denotes the second-order moment.
#. Estimate the spatial variance:

   .. math::
      :label: eq-cvtdd-local-spatial-variance

      V_{w,i}(n)
      = \left\langle M_{ww,i}(n)-M_{w,i}^{2}(n)\right\rangle .

   Here, angle brackets denote the expected-value operator.
#. Average :math:`V_{w,i}` to reduce uncertainty:

   .. math::
      :label: eq-cvtdd-average-spatial-variance

      V_w(n)=\frac{1}{M}\sum_{i=0}^{M}V_{w,i}(n),
      \qquad M=N-n .

**Outputs**

- :math:`V_{u,v}(n)`.

Triple Collocation
------------------

**Purpose**

Triple collocation (TC) was conceived by Stoffelen (1998) as a tool for
inter-calibration and individual error assessment of three different
collocated sea-surface wind datasets
(:ref:`Stoffelen (1998) <ref-stoffelen-triple-collocation>`). TC is generic
and can be applied to any geophysical variable and data product, provided that
errors are additive, linear calibration is sufficient, measurement errors are
uncorrelated with each other, and measurement errors are constant over the
range of measured values.

SAR-derived wind products are recommended to be validated against buoy wind
measurements, scatterometer-derived winds, and NWP winds. Collocations between
SAR and scatterometers strictly depend on the Local Time Ascending Node (LTAN).
TC analysis needs a reliable estimate of the representativeness error
:math:`r^2`; see `Spatial Variance`_ for its estimation.

**Inputs**

One or more triplets including the SAR-derived parameter of interest. For wind,
the following sources are relevant:

- SAR-derived wind vector.
- Scatterometer-derived wind vector.
- Buoy wind vector.
- NWP wind vector.

When available, buoy and scatterometer measurements are preferred to NWP
winds, due to their higher spatial resolution.

For sea-state parameters such as significant wave height (SWH), relevant
validation sources are:

- SAR-derived SWH.
- Altimeter-derived SWH.
- Buoy SWH measurement.
- SWH from an NWP model.

For LoS surface currents, relevant validation sources are:

- SAR-derived LoS surface currents.
- HF-radar total surface-current vector.
- Buoy total surface-current vector.
- LoS surface currents from an NWP model.

**Procedure**

Given three measurement systems, :math:`i=1,2,3`, representing, for example,
in-situ, satellite, and model estimates, the measurements and measurement
errors are approximated by the following linear expression
(:ref:`Vogelzang and Stoffelen (2021) <ref-vogelzang-quadruple-collocation>`;
:ref:`Vogelzang and Stoffelen (2022)
<ref-vogelzang-quintuple-collocation>`):

.. math::
   :label: eq-cvtdd-tc-linear-model

   s_i=a_i(t+\delta_i)+b_i .

Here, :math:`t` is the common quantity, i.e. the true value of the parameter
at the scales commonly resolved by all three data sources. :math:`a_i` and
:math:`b_i` are the scaling and offset (bias) calibration coefficients,
respectively, and :math:`\delta_i` is the random measurement error. For a
vector quantity such as wind, :math:`s` can represent either the zonal
(:math:`u`) or meridional (:math:`v`) component. Then:

#. Collocate triplets in space and time. For nominal wind regimes, the temporal
   constraint should be less than 30 minutes and the spatial constraint within
   25 km.
#. Set the calibration reference data source (e.g. :math:`i=1`), i.e.
   :math:`a_1=1` and :math:`b_1=0` (e.g. in situ).
#. Estimate the variance common to these smaller scales,
   :math:`r^2=\langle\delta_1\delta_2\rangle` (representativeness error). See
   `Spatial Variance`_ to compute :math:`r^2`, ensuring that :math:`s_1`,
   :math:`s_2`, and :math:`s_3` represent the higher-, intermediate-, and
   coarser-resolution systems, respectively (e.g. buoys, satellite, and NWP
   model).
#. Compute the calibration coefficients iteratively until they satisfy a
   selected convergence threshold.
#. Calibrate the original measurements :math:`s_i^{\mathrm{uncal}}` with the
   new calibration coefficients:

   .. math::

      s_i=\frac{s_i^{\mathrm{uncal}}-b_i}{a_i},
      \qquad \forall i\in\{1,2,3\} .

   This is an inverse calibration. At the first iteration the scaling
   coefficients are one and the bias coefficients are zero.
#. Apply the :math:`4\sigma` test to exclude possible outliers.
#. Estimate the first- and second-order moments and the covariances using the
   calibrated measurements for every combination of :math:`i,j=1,2,3`:

   .. math::
      :label: eq-cvtdd-tc-moments

      \begin{aligned}
      M_i &= \langle s_i\rangle, \\
      M_{ij} &= \langle s_i s_j\rangle, \\
      C_{ij} &= M_{ij}-M_iM_j .
      \end{aligned}

#. Estimate the true common variance :math:`T`:

   .. math::
      :label: eq-cvtdd-tc-true-variance

      T=\frac{C_{12}C_{13}}{C_{23}}-r^2 .

#. Estimate the calibration coefficients:

   .. math::

      a_2=\frac{C_{23}}{C_{13}},
      \qquad b_2=M_2-a_2M_1 .

   .. math::

      a_3=\frac{C_{13}}{T},
      \qquad b_3=M_3-a_3M_1 .

#. Check convergence of :math:`a_{2,3}` and :math:`b_{2,3}`:

   - :math:`\left|a_i^k-a_i^{k-1}\right|\leq10^{-6}`
     for all :math:`i\in\{2,3\}`.
   - :math:`\left|b_i^k-b_i^{k-1}\right|\leq10^{-6}`
     for all :math:`i\in\{2,3\}`, where :math:`k` is the iteration index.
#. Iterate until convergence.
#. Estimate the measurement-error variances of the three sources:

   .. math::
      :label: eq-cvtdd-tc-error-variances

      \begin{aligned}
      \epsilon_1^2 &= \frac{C_{11}}{a_1^2}-T-r^2, \\
      \epsilon_2^2 &= \frac{C_{22}}{a_2^2}-T-r^2, \\
      \epsilon_3^2 &= \frac{C_{33}}{a_3^2}-T .
      \end{aligned}

**Metrics**

- :math:`\left|a_i^k-a_i^{k-1}\right|` for all :math:`i\in\{2,3\}`.
- :math:`\left|b_i^k-b_i^{k-1}\right|` for all :math:`i\in\{2,3\}`, where
  :math:`k` is the iteration index.

**Outputs**

- Calibration coefficients: :math:`a_i,b_i` for all :math:`i\in\{1,2,3\}`.
- Measurement-error variances: :math:`\epsilon_i^2` for all
  :math:`i\in\{1,2,3\}`.

The error variances above are provided at the scale of the intermediate
resolution system (e.g. satellite). They can also be computed at the scale of
the coarser-resolution system (e.g. NWP model), using:

.. math::
   :label: eq-cvtdd-tc-nwp-error-variances

   \begin{aligned}
   \epsilon_{\mathrm{NWP},1}^{2}
     &= \epsilon_{\mathrm{SAT},1}^{2}+r^{2}, \\
   \epsilon_{\mathrm{NWP},2}^{2}
     &= \epsilon_{\mathrm{SAT},2}^{2}+r^{2}, \\
   \epsilon_{\mathrm{NWP},3}^{2}
     &= \epsilon_{\mathrm{SAT},3}^{2}.
   \end{aligned}

The labels SAT and NWP indicate the intermediate- and coarser-resolution
systems, respectively.

One-to-One Validation
---------------------

One-to-one (1-to-1) validation assesses the SAR-derived parameter against
individual reference sources through linear correlation analysis. This
approach is performed independently for each validation source, providing
direct pairwise comparisons between SAR observations and reference data.

One-to-one validation is particularly useful when TC is not feasible due to
insufficient collocated triplets. This may occur, for example, if the SAR
Local Time Ascending Node (LTAN) does not align with other altimeter or
scatterometer platforms and the region lacks in-situ sampling from buoys or
other point-based platforms. In such cases, validation against NWP models or
other available reference sources provides an essential quality assessment of
the SAR retrievals.

**Purpose**

Assess the retrieval performance of SAR retrievals against a reference
validation source.

**Input**

- SAR-derived parameter.
- NWP-model parameter or any other available validation source.

**Procedure**

- Collocate the two sources in space and time. A spatial constraint within
  25 km and a temporal constraint within 30 minutes are recommended. For NWP
  models, collect hourly forecasts if available; otherwise interpolate model
  parameters bilinearly in space and time to the SAR wind-retrieval/vector cell
  and acquisition time.
- For circular variables such as wind direction, compute the differences
  :math:`\Delta\phi` and map the resulting angular differences to
  :math:`[-180^\circ,180^\circ]`:

  .. math::
     :label: eq-cvtdd-direction-difference

     \begin{aligned}
     \Delta\phi_{\mathrm{raw}} &= \phi_{\mathrm{SAR}}-\phi_{\mathrm{VS}}, \\
     \Delta\phi
       &= \Delta\phi_{\mathrm{raw}}-360^\circ
       &&\text{if }\Delta\phi_{\mathrm{raw}}>180^\circ, \\
     \Delta\phi
       &= \Delta\phi_{\mathrm{raw}}+360^\circ
       &&\text{if }\Delta\phi_{\mathrm{raw}}<-180^\circ .
     \end{aligned}

- Compute bias for all components.
- Compute root mean square difference (RMSD) for all components.
- For vector quantities, compute vector RMSD (vRMSD).

**Metrics**

- Non-vector quantities:

  - Bias: :math:`b=\langle VAR_{\mathrm{SAR}}-VAR_{\mathrm{VS}}\rangle`.
  - :math:`RMSD=\sqrt{\langle(VAR_{\mathrm{SAR}}-VAR_{\mathrm{VS}})^2\rangle}`.
  - Pearson correlation coefficient:

    .. math::

       r=
       \frac{\left\langle
       (VAR_{\mathrm{SAR}}-\overline{VAR}_{\mathrm{SAR}})
       (VAR_{\mathrm{VS}}-\overline{VAR}_{\mathrm{VS}})
       \right\rangle}
       {\sigma_{\mathrm{SAR}}\sigma_{\mathrm{VS}}} .

- Vector quantities (e.g. wind vector):

  - :math:`b_w=\langle w_{\mathrm{SAR}}-w_{\mathrm{VS}}\rangle`.
  - :math:`RMSD_w=\sqrt{\langle(w_{\mathrm{SAR}}-w_{\mathrm{VS}})^2\rangle}`.
  - :math:`vRMDS=\sqrt{\langle
    (u_{\mathrm{SAR}}-u_{\mathrm{VS}})^2+
    (v_{\mathrm{SAR}}-v_{\mathrm{VS}})^2\rangle}`.
  - Pearson correlation coefficient:

    .. math::

       r_w=
       \frac{\left\langle
       (w_{\mathrm{SAR}}-\overline{w}_{\mathrm{SAR}})
       (w_{\mathrm{VS}}-\overline{w}_{\mathrm{VS}})
       \right\rangle}
       {\sigma_{\mathrm{SAR}}\sigma_{\mathrm{VS}}} .

- Circular variables (e.g. wind direction):

  - :math:`b_\phi=\langle\mathbf{mod}(\phi_{\mathrm{SAR}}-\phi_{\mathrm{VS}},360)\rangle`.
  - :math:`RMSD_\phi=\sqrt{\langle\mathbf{mod}(\phi_{\mathrm{SAR}}-\phi_{\mathrm{AS}},360)\rangle}`.
  - Jammalamadaka--Sarma circular-circular correlation coefficient:

    .. math::

       \rho_c=
       \frac{\left\langle
       \sin(\phi_{\mathrm{SAR}}-\overline{\phi}_{\mathrm{SAR}})
       \sin(\phi_{\mathrm{VS}}-\overline{\phi}_{\mathrm{VS}})
       \right\rangle}
       {\sqrt{
       \left\langle\sin^2(\phi_{\mathrm{SAR}}-\overline{\phi}_{\mathrm{SAR}})\right\rangle
       \left\langle\sin^2(\phi_{\mathrm{VS}}-\overline{\phi}_{\mathrm{VS}})\right\rangle
       }} .

Here, angle brackets denote the expected-value operator, :math:`\mathbf{mod}`
denotes modulus, and :math:`VS` denotes validation source. :math:`VAR` is the
validation variable of interest. Formulas with subscript :math:`w` apply to
both components (:math:`u,v`) and speed (:math:`U`) for vector quantities.

**Output**

- Non-vector quantities:

  - Bias: :math:`b`.
  - :math:`RMSD`.
  - Pearson correlation coefficient: :math:`r`.

- Vector quantities:

  - Bias for each component, speed, and direction:
    :math:`b_u,b_v,b_U,b_\phi`.
  - RMSD for each component, speed, and direction:
    :math:`RMSD_u,RMSD_v,RMSD_U,RMSD_\phi`.
  - :math:`vRMDS`.
  - Pearson correlation coefficient for each component and speed:
    :math:`r_u,r_v,r_U`.
  - Jammalamadaka--Sarma circular-circular correlation coefficient for
    direction: :math:`\rho_{c,\phi}`.

Spectral Analysis
-----------------

**Purpose**

Spectral analysis is a validation tool used to assess the spatial scales
resolved by the retrievals
(:ref:`Vogelzang et al. (2011) <ref-vogelzang-spectral>`).

**Inputs**

- :math:`M` sets of :math:`N` wind-component samples each, denoted
  :math:`w_{ij}`, :math:`i=1,\ldots,M`, :math:`j=1,\ldots,N`.

**Procedure**

- Check for missing values in each set. Remove sets with missing values or fill
  the gaps using an interpolation procedure.
- Compute the power spectral density (PSD):

  .. math::
     :label: eq-cvtdd-spectral-density

     \psi^{i}_{w,j}=\psi^{i}_{w,k_j}=
     \begin{cases}
     \dfrac{\Delta}{N}\left|\hat{w}(k_j)\right|^2,
       & j=0\ \text{or}\ j=\dfrac{N}{2},\\[4pt]
     \dfrac{\Delta}{N}\left(
       \left|\hat{w}(k_j)\right|^2+
       \left|\hat{w}(k_{-j})\right|^2
     \right),
       & j=1,\ldots,\dfrac{N}{2}-1,
     \end{cases}
     \qquad i=1,\ldots,M .

  Here, :math:`\hat{w}` is the Fast-Fourier transform (FFT) of the (vector)
  component :math:`w`, :math:`\Delta` is the spacing, and :math:`k_j` is the
  wavenumber.
- Average the PSD from each set:

  .. math::
     :label: eq-cvtdd-average-spectral-density

     \Psi_{w,j}=\frac{1}{M}\sum_{i=1}^{M}\psi^{i}_{w,j} .

  PSD units are the squared units of the analyzed variable multiplied by the
  spatial sampling interval :math:`\Delta` (in metres). For wind components
  and LoS surface currents, whose units are :math:`\mathrm{m\,s^{-1}}`, PSD
  units are :math:`\mathrm{m^3\,s^{-2}}`; for SWH, whose units are
  :math:`\mathrm{m}`, PSD units are :math:`\mathrm{m^3}`.

**Metrics**

In accordance with the Guide to the Expression of Uncertainty in Measurement
(GUM) Type A evaluation principles for spectral estimators, the standard
uncertainty :math:`u(\Psi_{w,j})` of the averaged PSD is driven by the number
of independent scenes :math:`M`. Assuming a :math:`\chi^2` distribution with
:math:`2M` degrees of freedom for each spectral bin :math:`j`, the relative
standard uncertainty is:

.. math::
   :label: eq-cvtdd-psd-uncertainty

   \frac{u(\Psi_{w,j})}{\Psi_{w,j}}=\frac{1}{\sqrt{M}} .

**Outputs**

- PSD for each wind component: :math:`\Psi_{u,j},\Psi_{v,j}`.
- Associated standard-uncertainty profiles derived from
  :eq:`eq-cvtdd-psd-uncertainty`.

.. rubric:: References

.. _ref-vogelzang-spatial-variance:

Vogelzang, J., G. P. King, and A. Stoffelen (2015). “Spatial variances of wind
fields and their relation to second-order structure functions and spectra.”
*Journal of Geophysical Research: Oceans*, 120(2), 1048--1064.
`doi:10.1002/2014JC010239 <https://doi.org/10.1002/2014JC010239>`_.

.. _ref-stoffelen-triple-collocation:

Stoffelen, A. (1998). “Toward the true near-surface wind speed: Error modeling
and calibration using triple collocation.” *Journal of Geophysical Research:
Oceans*, 103(C4), 7755--7766.
`doi:10.1029/97JC03180 <https://doi.org/10.1029/97JC03180>`_.

.. _ref-vogelzang-quadruple-collocation:

Vogelzang, J., and A. Stoffelen (2021). “Quadruple collocation analysis of
in-situ, scatterometer, and NWP winds.” *Journal of Geophysical Research:
Oceans*, 126(5), e2021JC017189.
`doi:10.1029/2021JC017189 <https://doi.org/10.1029/2021JC017189>`_.

.. _ref-vogelzang-quintuple-collocation:

Vogelzang, J., and A. Stoffelen (2022). “On the accuracy and consistency of
quintuple collocation analysis of in situ, scatterometer, and NWP winds.”
*Remote Sensing*, 14(18), 4552.
`doi:10.3390/rs14184552 <https://doi.org/10.3390/rs14184552>`_.

.. _ref-vogelzang-spectral:

Vogelzang, J., A. Stoffelen, A. Verhoef, and J. Figa-Saldaña (2011). “On the
quality of high-resolution scatterometer winds.” *Journal of Geophysical
Research: Oceans*, 116(C10).
`doi:10.1029/2010JC006640 <https://doi.org/10.1029/2010JC006640>`_.
