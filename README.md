# Introduction to Galaxies: Hands-on Sessions

**Master Degree - Università degli Studi di Milano-Bicocca**
**Author:** Elettra Piozzi

# About This Repository
This repository contains a comprehensive collection of Python scripts, Jupyter Notebooks, and data analysis developed for the hands-on sessions of the "Introduction to Galaxies" course. The projects span across multiple key topics in modern extragalactic astrophysics.

#  Skills & Tools
* **Languages & Libraries:** Python, `astropy`, `scipy`, `matplotlib`.
* **Data Handling:** Advanced manipulation of FITS files.
* **Software & Codes:** `GADGET4` (hydrodynamics), `CIGALE` (SED fitting).

# Projects Overview

### Session 1: Sub-Halo Abundance Matching (SHAM)
* Matched dark matter halos from the **Millennium Simulation** to galaxy stellar masses using the SHAM empirical method.
* Compared the derived $M_h$ vs $M_*$ relations with the predictions from the **Illustris TNG100** cosmological hydrodynamic simulations.

### Session 2: The Jeans Mass & Hydrodynamics
* Utilized the state-of-the-art hydrodynamic code **GADGET4** to numerically simulate the collapse of gas clouds.
* Explored the parameter space (temperature, mass, box size) to numerically test the theoretical Jeans mass formalism.

### Session 3: Galaxy Evolution Across Cosmic Time
* Analyzed deep-field multi-wavelength photometry and spectroscopy from the **CANDELS+3D-HST survey**.
* Traced the Main Sequence of star-forming galaxies at different redshifts, utilizing the $U-V$ vs $V-J$ (UVJ) color diagram to effectively separate star-forming and passive galaxies.
* Performed Stellar Population Synthesis (SPS) and SED fitting using the **CIGALE** code to extract physical parameters (SFR, Age, Dust attenuation).

### Session 4: Correlating the CGM and the Galaxy Population
* Cross-correlated Lyman Alpha Emitters (LAEs) at $z \approx 3-4$ with hydrogen overdensities using data from the **MAGG survey**.
* Produced 2D cross-correlation maps combining MUSE galaxy survey data and VLT/X-SHOOTER quasar absorption spectra to study the Circumgalactic Medium (CGM).

### Session 5: Galaxy Evolution in Dense Environments
* **Part 1:** Investigated the impact of environmental overdensity on galaxy properties using **SDSS DR16** data, mapping the fraction of passive vs star-forming galaxies in color-mass diagrams.
* **Part 2:** Reconstructed the quenching history of NGC 4330 (falling into the Virgo Cluster) by fitting stellar population models to VLT/FORS2 optical spectra and multi-wavelength photometry.
