# DNSC 6330 Responsible Machine Learning Capstone
## Group 3 | 2024 HMDA Mortgage Approval Classification | Team Members: Zuleirys Santana Rodriguez, David Porudominsky Rotstain, Tsotne Dzeira, Emilia Puskas, William McHale, Naina Magadzire

## Overview
This repository contains the capstone audit for `DNSC 6330: Responsible Machine Learning` using the 2024 HMDA Loan/Application Register (`LAR`). The project predicts mortgage approval outcomes after filtering `action_taken` to:

- `1` = originated -> `label=1`
- `2` = approved but not accepted -> `label=1`
- `3` = denied -> `label=0`

The repository is organized to answer the five capstone questions:

1. What is the optimization objective?
2. What are the known failure modes?
3. How are subgroup errors measured?
4. What risks remain after mitigation?
5. Is deployment defensible?

## Optimization Objective
The model predicts `label=1` (`approved`) and tunes the operating threshold to maximize approval-class `F1`.

This label convention matters:

- `False negatives` are wrongful denials: applicants who should be approved but are denied by the model.
- `False positives` are false approvals: applicants who should be denied but are approved by the model.

Fairness is audited separately with:

- `AIR` (Adverse Impact Ratio)
- `ME` (Mean Error)
- `SMD` (Standardized Mean Difference)
- subgroup `FNR` / `FPR`

## Repository Layout
```text
Code/
├── Data/
│   ├── 2024_lar.csv                  # Raw HMDA file, local only, not for GitHub
│   └── 2024_lar.txt                  # Raw HMDA text export, local only
├── figures/                          # Generated plots kept for professor review
├── tables/                           # Generated tables kept for professor review
├── RML_GRP3_01_eda.ipynb
├── RML_GRP3_02_preprocessing.ipynb
├── RML_GRP3_03_modeling.ipynb
├── RML_GRP3_04_fairness.ipynb
├── RML_GRP3_05_explainability.ipynb
├── RML_GRP3_06_robustness_drift.ipynb
├── README.md
├── requirements.txt
├── .gitignore
└── run_pipeline.py
```

## Execution Order
Run the notebooks in this exact order:

1. `RML_GRP3_01_eda.ipynb`
2. `RML_GRP3_02_preprocessing.ipynb`
3. `RML_GRP3_03_modeling.ipynb`
4. `RML_GRP3_04_fairness.ipynb`
5. `RML_GRP3_05_explainability.ipynb`
6. `RML_GRP3_06_robustness_drift.ipynb`

Or run the full sequence with:

```bash
python run_pipeline.py
```

The runner uses `jupyter nbconvert --execute --inplace` with the `python3` kernel.

## Data Setup
Place the raw HMDA file in `Code/Data/` as either:

- `2024_lar.csv`
- or `2024_lar.txt`

Notebook 01 will use `Data/2024_lar.csv` directly when present. If only the text file exists, it will convert it to CSV first and keep the original text file untouched.

The raw HMDA data is intentionally not Git-tracked because it is too large for GitHub.

## Generated Artifacts
These artifacts are created during execution and used by downstream notebooks:

| Artifact | Produced By | Used By |
|---|---|---|
| `df_filtered.csv` | NB01 | NB02 |
| `X_train.parquet`, `X_test.parquet` | NB02 | NB03-NB06 |
| `y_train.parquet`, `y_test.parquet` | NB02 | NB03-NB06 |
| `prot_train.parquet`, `prot_test.parquet` | NB02 | NB04-NB06 |
| `X_train_imputed.parquet`, `X_test_imputed.parquet` | NB02 | NB03-NB06 |
| `train_medians.parquet` | NB02 | NB06 |
| `best_model.pkl` | NB03 | NB04-NB06 |
| `model_meta.json` | NB03 | NB04-NB06 |
| `threshold_meta.json` | NB04 | NB05-NB06 |

Large local artifacts such as raw data, filtered CSVs, parquet files, and serialized models are excluded from Git by `.gitignore`.

## Notebook Responsibilities
### NB01 EDA
- Validates raw columns
- Filters `action_taken`
- Builds `label`
- Establishes pre-model subgroup approval disparities

### NB02 Preprocessing
- Cleans HMDA-specific missing encodings
- Parses `debt_to_income_ratio`
- One-hot encodes categorical inputs
- Splits train/test
- Saves imputed modeling matrices and protected-attribute audit files

### NB03 Modeling
- Trains a logistic regression baseline
- Trains candidate tree models under fixed compute budgets
- Selects the best model on approval-class `F1` with `AUC` as tie-break support
- Tunes a transparent global threshold

### NB04 Fairness
- Computes `AIR`, `ME`, `SMD`, `TPR`, `FPR`, `FNR`, `Precision`, and `AUC` by subgroup
- Audits race, sex, ethnicity, age, and race x sex intersectionality
- Applies race-specific threshold mitigation when groups fail the four-fifths rule
- Saves deployment threshold metadata and residual-risk tables

### NB05 Explainability
- Generates `SHAP` global explanations
- Generates `LIME` local explanations
- Generates `DiCE` counterfactual recourse examples
- Checks for proxy-like feature behavior

### NB06 Robustness and Drift
- Computes `PSI`, `KS`, and `MMD`
- Measures policy-level generalization gap
- Runs permutation importance and macro stress scenarios
- Produces slice-based robustness tables and monitoring guidance

## Metrics To Care About
This repository is written to align with the rubric language:

- `Q1 Optimization objective`: explicit metric, threshold, trade-off, and stakeholder framing
- `Q2 Failure modes`: sample selection bias, proxy discrimination, feedback loops, and structural trade-offs
- `Q3 Subgroup error measurement`: `AIR`, `ME`, `SMD`, `FNR`, `FPR`, intersectionality
- `Q4 Residual risks`: mitigation before/after evidence plus accepted residual risk
- `Q5 Deployment defensibility`: explicit recommendation, GitHub as audit record, and re-evaluation triggers

## GitHub Submission Notes
This folder is prepared for GitHub review with these conventions:

- Raw HMDA data is not committed.
- Large intermediate artifacts are not committed.
- `tables/` and `figures/` can be committed because they are the professor-facing audit outputs.
- Executed notebooks can be committed so the reviewer sees both code and outputs.
- `requirements.txt` pins the Python dependencies needed to rerun the pipeline.


## Environment
Create an environment and install dependencies with:

```bash
python -m pip install -r requirements.txt
```

The notebooks are configured for the `python3` kernel.
