# Flood First-Floor-Elevation Modeling with Kriging

Geostatistical prediction of residential **first-floor elevations (FFE)** across a Newport
News, VA flood zone — a low-cost alternative to LiDAR-derived flood-exposure data.

- **Method:** Empirical Bayesian Kriging (EBK) and CoKriging in the ArcGIS Pro Geostatistical
  Wizard (K-Bessel semivariogram, 1,000 simulations); foundation type encoded as a CoKriging
  covariate via a custom ArcPy `CalculateField` codeblock.
- **Data:** field FFEs for 1,767 of 5,763 sampled structures (TruPulse 360), parcel-joined to
  city records; validated against FEMA Elevation Certificates.
- **Result:** FFE recoverable at accuracy comparable to LiDAR (residuals binned at 0.2 ft vs a
  2.0 ft LiDAR-equivalent cutoff).
- **Stack:** ArcGIS Pro · ArcPy · file geodatabase · geostatistics

_Independent Study, Old Dominion University. Portfolio project by [Michael Warren](https://mikeswarren.com)._
