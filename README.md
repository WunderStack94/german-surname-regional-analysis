# German Surname Regional Analysis

## Overview

This project investigates regional patterns in German occupational surnames using a simulation-based and quantitative approach. Due to strict data protection regulations, no large-scale real surname dataset was available. Instead, a synthetic dataset was generated to approximate realistic surname distributions across German macro-regions.

The project combines methods from onomastics, corpus linguistics, and data science to explore whether regional surname structures remain statistically distinguishable.

---

## Research Questions

The study is guided by the following central questions:

* Can regional surname distributions be meaningfully approximated using probabilistic simulation?
* Do these distributions exhibit measurable structural differences across regions?
* Can machine learning methods recover historically plausible regional groupings based on surname data?

---

## Methodology

### Simulation

* Synthetic population generated via hierarchical Dirichlet model
* Regional distributions (θ_region) parameterized using literature-based assumptions
* Local variation introduced through Dirichlet scaling (β)
* Population sizes simulated using a log-normal distribution

### Statistical Analysis

* Shannon entropy (diversity of surname distributions)
* Gini coefficient and Lorenz curves (concentration of names)
* Jensen-Shannon divergence (distance between regions)

### Machine Learning

* KMeans clustering (unsupervised structure detection)
* DBSCAN (density-based clustering)
* Support Vector Machine (supervised classification)

---

## Key Results

* Regional surname distributions are **clearly distinguishable** in statistical terms
* Clustering methods recover **stable regional structures**
* SVM classification achieves an accuracy of **~93%**, indicating strong separability
* Some regions (e.g. North) show higher ambiguity, consistent with prior clustering results

---

## Limitations

* Fully simulated dataset (no real-world validation)
* Model parameters (α) are theory-driven and manually specified
* Limited number of surnames and reduced population size
* Results illustrate structural plausibility rather than empirical truth

---

## Repository Structure

```
german-surname-regional-analysis/
├── thesis/              # Final paper (PDF)
├── notebooks/           # Main analysis notebook
├── src/                 # Modularized Python code
├── data/
│   └── derived/         # Generated datasets
├── results/
│   └── plots/           # Figures used in the thesis
├── README.md
└── requirements.txt
```

---

## Reproducibility

To reproduce the analysis:

```bash
pip install -r requirements.txt
```

Then open the notebook:

```bash
notebooks/WunderlichOnomastikCode.ipynb
```

---

## Author

Wunderlich

---

## Context

This project was developed as part of a seminar in linguistics, with a focus on quantitative onomastics and computational methods in the digital humanities.
