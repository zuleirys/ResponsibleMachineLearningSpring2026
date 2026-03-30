# Individual Homework 2 — Model Explainability, Counterfactuals, and Governance in COMPAS

---

## Overview

This project extends the COMPAS analysis completed in **Individual Homework 1**. The first assignment established the Python workflow for loading, cleaning, and analyzing the COMPAS dataset, along with fitting baseline models and examining fairness-related performance metrics.

This second notebook builds on that earlier work by focusing on **model explainability, local interpretation, counterfactual analysis, and governance considerations**.

For additional background on the original data preparation and baseline COMPAS workflow, please refer to **Individual Homework 1**.

---

## Dataset

This notebook uses the same ProPublica COMPAS two-year dataset used in the first assignment:

- `compas-scores-two-years.csv`

The analysis continues from the cleaned COMPAS cohort developed in Assignment 1 and uses that processed dataset as the basis for the explainability and counterfactual tasks.

---

## Purpose of the Analysis

The goal of this notebook is to go beyond prediction performance and examine how the model behaves for specific defendants and groups.

The notebook performs four main tasks:

1. Compute **SHAP values** for the gradient-boosted tree model and generate:
   - a global beeswarm summary plot
   - waterfall plots for selected high-risk and low-risk defendants by race

2. Run **LIME** for the same selected defendants and compare those local explanations to the SHAP results

3. Use **DiCE** to generate counterfactual examples and identify what feature changes would flip the model’s prediction

4. Write a **governance memo** that summarizes the findings, discusses the limitations of the explanations, and recommends additional oversight steps

The broader objective is to evaluate the model not only in terms of classification results, but also in terms of **interpretability, recourse, and responsible governance**.

---

## Models Used

The notebook includes two classification models built on the cleaned COMPAS data:

- **Logistic Regression** — used as an interpretable baseline model
- **Gradient-Boosted Tree** — used as the primary black-box model for explainability analysis

Most of the explanation and counterfactual analysis is centered on the **gradient-boosted tree model**.

---

## Python Libraries Used

The notebook uses the following Python libraries:

- `pandas`
- `numpy`
- `matplotlib`
- `scikit-learn`
- `lime`
- `shap`
- `dice-ml`

---

## Files in This Repository

- `Individual_Assingment_02_Zuleirys_Santana_Rodriguez.ipynb` — Jupyter Notebook containing the full Assignment 2 analysis
- `README.md` — Project overview and instructions

---

## Reproducibility Instructions

To reproduce the results:

1. Open the notebook in Jupyter Notebook, JupyterLab, or Google Colab
2. Run the cells from top to bottom in order
3. If needed, install the explanation libraries used in the notebook:
   - `lime`
   - `shap`
   - `dice-ml`

Because this notebook builds on the workflow from Assignment 1, it should be run in sequence from beginning to end so that the cleaned dataset, feature setup, model pipelines, and explanation objects are all created properly.

---

## Workflow Summary

The notebook includes:

- continuation of the COMPAS workflow from Assignment 1
- preparation of the target and predictor variables
- conversion of jail-date fields into numeric form
- train/test split on the cleaned dataset
- preprocessing of numeric and categorical features
- fitting of logistic regression and gradient-boosted tree models
- comparison of model performance by race
- SHAP global and local explanation analysis
- LIME local explanation analysis
- DiCE counterfactual generation for selected defendants
- a governance memo discussing interpretation limits and monitoring recommendations

---

## Notes

This notebook is designed as an extension of **Individual Homework 1**. The first homework focused on reproducing the COMPAS lecture workflow in Python, including cleaning, descriptive analysis, modeling, and group-level fairness metrics. This second homework builds on that foundation by examining how the model can be interpreted and audited more closely.

As with many explainability tools, different methods may agree strongly on the most influential variables while differing on smaller feature contributions. For that reason, the notebook emphasizes the major patterns that appear consistently across methods and also discusses the need for caution when interpreting local explanations and counterfactual suggestions.

---

## Author

**Zuleirys Santana-Rodriguez**
