# Individual Homework 3 — Disparate Impact, Intersectional Fairness, and Error-Rate Auditing in COMPAS

---

## Overview

This project extends the COMPAS analysis developed in **Individual Homework 1** and the explainability work completed in **Individual Homework 2**.

Assignment 1 established the base workflow for loading, cleaning, and preparing the COMPAS dataset, as well as reproducing the initial predictive and fairness-oriented analysis in Python. Assignment 2 then built on that foundation by focusing on **model explainability, local interpretation, counterfactual recourse, and governance-oriented evaluation**.

This notebook continues that sequence by focusing on **disparate-impact measurement, subgroup auditing, intersectional fairness analysis, and compliance-oriented reporting** using the Lecture 3 workflow.

For background on the original data preparation and prior modeling steps, please refer to the earlier assignments.

---

## Dataset

This analysis uses the same ProPublica COMPAS dataset used in the previous assignments:

- `compas-scores-two-years.csv`

The notebook begins from the cleaned COMPAS cohort created earlier in the workflow and uses that processed data as the basis for the fairness and disparity analysis.

---

## Purpose of the Analysis

This notebook moves beyond prediction and explanation to evaluate whether the model produces outcomes that may indicate **statistical disparity across protected groups**.

The notebook performs five main tasks:

1. Compute **AIR (Adverse Impact Ratio)**, **ME (Marginal Effect)**, and **SMD (Standardized Mean Difference)** for race and sex using the Solas-AI disparity workflow, while also confirming the AIR results with manual calculations

2. Build an **intersectional subgroup analysis** for race × sex and identify the subgroup with the lowest AIR relative to the Caucasian male reference group

3. Compute **false positive rate (FPR)** and **false negative rate (FNR)** disparities by race and test those differences using a **two-proportion z-test**

4. Produce a **publication-style figure** showing FPR and FNR by race with the Caucasian group as the visual reference baseline

5. Write a **compliance memo** summarizing the findings, the metrics used, the major disparities observed, and the limitations of the audit

The broader goal is to evaluate the COMPAS-based models not only in terms of prediction and explanation, but also in terms of **group fairness, legal risk, and governance relevance**.

---

## Models Used

The notebook includes two models built on the cleaned COMPAS data:

- **Logistic Regression** — used as an interpretable baseline
- **Gradient-Boosted Tree** — used as the main black-box model for the disparity audit

The fairness and compliance discussion in Assignment 3 focuses primarily on the **gradient-boosted tree**, while also checking whether the logistic regression shows the same overall disparity pattern.

---

## Python Libraries Used

The notebook uses the following Python libraries:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `statsmodels`
- `scikit-learn`
- `shap`
- `lime`
- `dice-ml`
- `solas-ai`

---

## Files in This Repository

- `Individual_Assignment_03_Zuleirys_Santana_Rodriguez.ipynb` — Jupyter Notebook containing the full Assignment 3 implementation
- `DNSC_6330_Lecture-03.pdf` — Lecture 3 slides used as the analytical reference
- `README.md` — Project documentation

---

## Reproducibility Instructions

To reproduce the results:

1. Open the notebook in Jupyter Notebook, JupyterLab, or Google Colab
2. Run all cells from top to bottom in order
3. Allow the package-installation cells to finish before continuing

If needed, install the required packages used in the notebook:

- `shap`
- `lime`
- `dice-ml`
- `solas-ai`

Because this notebook builds on the cleaned data, feature engineering, and model objects created earlier in the notebook, it should be run in full from the beginning so that all preprocessing, model fitting, and fairness-audit objects are generated in sequence.

If using Google Colab, internet access is required because the notebook reads the COMPAS CSV file from GitHub.

---

## Workflow Summary

The notebook includes:

- continuation of the COMPAS workflow from Assignments 1 and 2
- model training for logistic regression and gradient-boosted tree classifiers
- Solas-AI disparity analysis for race and sex
- manual validation of AIR values against direct selection-rate calculations
- intersectional fairness analysis for race × sex subgroups
- FPR and FNR disparity testing by race using two-proportion z-tests
- a publication-style visualization of race-based error rates
- a regulator-facing compliance memo based on the audit findings

---

## Notes

This notebook is intended to extend the analytical foundation established in the earlier assignments. Assignment 1 focused on data preparation, exploratory analysis, logistic modeling, and fairness metrics. Assignment 2 focused on explainability, recourse, and governance. Assignment 3 builds on that work by focusing on **bias measurement, disparate-impact testing, and subgroup auditing**.

The Assignment 3 section follows the structure presented in **Lecture 3: Algorithmic Bias Measurement**. In particular, it emphasizes the use of multiple fairness metrics rather than relying on a single measure. It also highlights the importance of interpreting subgroup disparities carefully when some categories contain very small sample sizes.

The final compliance memo is intentionally written as if it were addressed to a regulator or auditor reviewing the fairness properties of the model.

---

## Author

**Zuleirys Santana Rodriguez**
