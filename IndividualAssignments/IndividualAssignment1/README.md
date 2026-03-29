# Individual Homework 1 — Python Version of the COMPAS Lecture Analysis

## Project Description
This notebook recreates the COMPAS example from class using Python instead of R. The original class material walks through data preparation, exploratory analysis, logistic regression, and fairness-related evaluation. This version follows that same general sequence in Python.

The goal of the assignment is to show how the R workflow from lecture can be translated into a clear, reproducible Python notebook.

## Data Source
The notebook uses the ProPublica COMPAS two-year dataset:

- `compas-scores-two-years.csv`

The file is loaded directly from its raw online source inside the notebook, so no manual download is required before running the analysis.

## What the Notebook Does
The notebook is organized to reproduce the main analytical steps from the lecture:

- imports the required Python packages
- loads the COMPAS dataset
- filters and cleans the data
- creates the categorical variables needed for modeling
- performs descriptive summaries and simple exploratory analysis
- estimates a logistic regression model
- generates predicted probabilities and predicted classes
- builds an overall confusion matrix
- computes race-specific performance metrics
- compares false positive rate and false negative rate disparities across groups

## Main Python Packages
The notebook uses these libraries:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `statsmodels`
- `IPython.display`

## Repository Contents
- `Individual_Asingment_01_Zuleirys_Santana_Rodriguez.ipynb` — complete Python notebook for the assignment
- `README.md` — overview of the project and instructions for running it

## How to Run the Notebook
To reproduce the analysis:

1. Open the notebook in Jupyter Notebook, JupyterLab, or Google Colab
2. Run the cells from top to bottom in order
3. The dataset will be imported automatically from the online source used in the notebook
4. Review the tables, plots, regression output, and disparity metrics generated in the later sections

## Analytical Focus
This notebook is not only about prediction accuracy. It also looks at how classification outcomes differ across groups. In particular, the later sections examine confusion-matrix measures such as:

- accuracy
- precision
- recall
- false positive rate
- false negative rate

These metrics are then compared across racial groups to mirror the fairness-focused discussion from lecture.

## Reproducibility Note
The notebook is designed to be reproducible as written. Because the analysis is implemented in Python rather than R, some output formatting or coefficient presentation may look slightly different from the lecture notebook, but the workflow and interpretation remain aligned with the class example.

## Author
Zuleirys Santana-Rodriguez
