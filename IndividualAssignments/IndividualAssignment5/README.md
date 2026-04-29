# Individual Homework 05 — Applied Adversarial Audit on COMPAS

---

## Overview

This project evaluates COMPAS-style prediction models under the security lens introduced in **Lecture 05: ML Security and Abuse Pathways**.

The notebook focuses on **intentional adversarial attack** rather than ordinary predictive evaluation. The main themes are **PGD evasion, targeted label poisoning, and membership inference**, along with the fairness and governance implications of those attacks.

This assignment is built on the same analytical foundation developed in the earlier individual work. Assignment 1 established the baseline COMPAS workflow in Python, Assignment 2 added explainability and counterfactual analysis, Assignment 3 added fairness and disparate-impact auditing, and Assignment 4 extended the same pipeline into robustness and drift testing. Assignment 5 continues from that sequence and reuses the same core COMPAS preprocessing and baseline model structure while shifting the focus to adversarial abuse pathways.

---

## Dataset

This notebook uses the ProPublica COMPAS two-year dataset:

- `compas-scores-two-years.csv`

The notebook is written to use the local CSV file in the same folder. If the file is missing, it falls back to the original raw GitHub source.

---

## Purpose of the Analysis

The goal of this notebook is to evaluate how the COMPAS models behave when an adversary deliberately tries to manipulate predictions, training data, or privacy exposure.

The notebook performs four main tasks:

1. Run a **PGD evasion audit** on both the logistic regression and gradient-boosted tree models across `epsilon in {0.25, 0.5, 1.0, 2.0}` and report **FPR by race**, **AIR**, and the attack level where AIR crosses the `0.80` threshold

2. Extend the **label-flip poisoning loop** to target both African-American and Caucasian defendants, then compare **AUC degradation**, **AIR degradation**, the **stealth zone** where fairness shifts while AUC remains relatively stable, and whether a **PSI-based drift monitor** would detect the attack

3. Build a **shadow-model membership inference pipeline** for both baseline models, compare **membership inference AUC**, visualize **confidence-gap histograms**, and study the effect of **L2 regularization** on the logistic regression privacy-utility tradeoff

4. Write a final **reflection** identifying the highest-risk finding across the notebook, then propose one **proactive** and one **reactive** mitigation with quantified effects from the experimental results

The broader objective is to evaluate the COMPAS models not only for prediction or fairness, but also for **security, privacy, and abuse resilience**.

---

## Models Used

The notebook includes two classification models built on the cleaned COMPAS cohort:

- **Logistic Regression** — used as the interpretable baseline model
- **Gradient-Boosted Tree** — used as the higher-capacity black-box model

The notebook compares these models directly in the **PGD evasion** and **membership inference** sections, while the **poisoning loop** follows the lecture-style black-box attack framing with the gradient-boosted tree as the primary target model.

---

## Python Libraries Used

The notebook uses the following Python libraries:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `IPython.display`

---

## Files in This Repository

- `Individual_Assignment_05_Zuleirys_Santana_Rodriguez.ipynb` — Jupyter Notebook containing the full Assignment 5 implementation
- `Individual_Assignment_05_Report.docx` — formatted written report for submission
- `README.md` — project documentation for Assignment 5

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

Because the notebook rebuilds the full COMPAS workflow internally, it should be run from the beginning so that the cleaned dataset, train/test split, baseline models, attack loops, and audit summaries are generated in sequence.

The notebook is standalone for reproducibility, but it is intentionally aligned with the earlier assignments in `Individual Assignments` and especially the Lecture 04 pipeline used in Assignment 4.

The written report is also included as a `.docx` file formatted for submission.

---

## Workflow Summary

The notebook includes:

- COMPAS data loading and filtering
- train/test split and pipeline setup for logistic regression and gradient-boosted tree models
- clean fairness baseline using FPR by race and AIR
- PGD-style evasion attacks on the tabular feature space
- targeted label-flip poisoning with fairness monitoring
- stealth-zone identification
- PSI evidence showing why feature-only drift monitoring can miss label attacks
- shadow-model membership inference for both baseline models
- confidence-gap histograms and generalization-gap comparison
- logistic regression regularization sweep over `C in {0.01, 0.1, 1.0, 10.0}`
- final reflection with quantified mitigation discussion

---

## Notes

This notebook follows the structure presented in **Lecture 05: ML Security and Abuse Pathways**. It is designed to satisfy the assignment requirement for a **clean, standalone notebook** that runs from top to bottom and includes **code, outputs, and short markdown interpretations**.

The interpretation sections are written to support the professor’s grading emphasis on not just reporting metrics, but explaining what they mean, what they miss, and what actions they justify in an adversarial machine learning audit.

---

## Author

**Zuleirys Santana Rodriguez**
