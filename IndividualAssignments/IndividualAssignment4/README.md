# Individual Homework 4 — From Accuracy to Accountability: Stress Testing a Predictive Model

---

## Overview

This project extends the COMPAS analysis completed in the earlier individual assignments. Assignment 1 reproduced the baseline lecture workflow in Python, Assignment 2 focused on explainability and counterfactual analysis, and Assignment 3 examined fairness, disparate impact, and subgroup disparities.

This fourth notebook builds on that foundation by evaluating whether the predictive system remains reliable under change. The focus is on **distribution drift, generalization, spurious correlations, robustness stress testing, and slice-based evaluation** using the Lecture 04 framework.

---

## Dataset

This notebook uses the ProPublica COMPAS two-year dataset:

- `compas-scores-two-years.csv`

The notebook is written to use the local CSV file in the same folder. If the file is missing, it falls back to the original raw GitHub source.

---

## Purpose of the Analysis

The goal of this notebook is to move beyond average predictive performance and test whether the model remains stable, interpretable, and governance-ready under changing conditions.

The notebook performs five main tasks:

1. Compute **Population Stability Index (PSI)** and **Kolmogorov-Smirnov (KS)** statistics for numeric features, along with **Maximum Mean Discrepancy (MMD)** in encoded feature space, to assess distribution drift

2. Compare **train vs. test AUC, accuracy, and log loss** for the baseline models and diagnose possible overfitting through performance gaps

3. Run **counterfactual swaps** on selected protected attributes and measure changes in predicted probabilities as a probe for spurious correlations or shortcut learning

4. Stress test the model by increasing **`priors_count`**, then produce **ICE curves** and sensitivity summaries to examine robustness under controlled perturbation

5. Compare model performance across **race, sex, and age slices** to identify subgroup-specific error burdens that may be hidden by average metrics

The broader objective is to evaluate the COMPAS models not only for predictive accuracy, but also for **reliability, robustness, and audit-level accountability**.

---

## Models Used

The notebook includes two classification models built on the cleaned COMPAS cohort:

- **Logistic Regression** — used as the interpretable baseline model
- **Gradient-Boosted Tree** — used as the higher-capacity model for robustness and subgroup auditing

The analysis compares the two models across drift, generalization, and slice-based evaluation, while the spurious-correlation and ICE-based robustness discussion focuses primarily on the **gradient-boosted tree**.

---

## Python Libraries Used

The notebook uses the following Python libraries:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scipy`
- `scikit-learn`
- `IPython.display`

Supporting files included in this folder:

- `requirements.txt`
- `.gitignore`

---

## Files in This Repository

- `Individual_Assignment_04_Zuleirys_Santana_Rodriguez.ipynb` — Jupyter Notebook containing the full Assignment 4 implementation
- `compas-scores-two-years.csv` — local dataset used by the notebook
- `README.md` — project documentation for Assignment 4
- `requirements.txt` — package list for recreating the environment

---

## Reproducibility Instructions

To reproduce the results:

1. Open the notebook in Jupyter Notebook, JupyterLab, or Google Colab
2. Keep `compas-scores-two-years.csv` in the same folder as the notebook
3. Run all cells from top to bottom in order

If needed, install the required packages with:

```bash
pip install -r requirements.txt
```

Because the notebook rebuilds the full COMPAS workflow internally, it should be run from the beginning so that the cleaned dataset, train/test split, model pipelines, drift metrics, stress tests, and subgroup audit tables are generated in sequence.

---

## Workflow Summary

The notebook includes:

- COMPAS data loading and Lecture 01 style filtering
- train/test split and pipeline setup for logistic regression and gradient-boosted tree models
- PSI and KS drift analysis for numeric features
- MMD calculation in encoded feature space
- comparison of train and test predicted score distributions
- train vs. test AUC, accuracy, and log loss comparison
- counterfactual swap probes for race and sex
- stress testing by perturbing `priors_count`
- ICE curves and sensitivity summaries
- slice-based evaluation by race, sex, and age
- audit-level reasoning about what the metrics mean, what they miss, and what actions they justify

---

## Notes

This notebook follows the structure presented in **Lecture 04: Robustness, Generalization, and Dataset Drift**. It is designed to satisfy the assignment requirement for a **clean, standalone notebook** that runs from top to bottom and includes **code, outputs, and short markdown interpretations**.

The interpretation sections are written to support the professor’s grading emphasis on not just reporting metrics, but explaining what they mean, what they miss, and what actions they would justify in a responsible machine learning audit.

---

## Author

**Zuleirys Santana Rodriguez**
