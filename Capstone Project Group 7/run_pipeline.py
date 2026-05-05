from pathlib import Path
import subprocess
import sys


NOTEBOOKS = [
    "RML_GRP3_01_eda.ipynb",
    "RML_GRP3_02_preprocessing.ipynb",
    "RML_GRP3_03_modeling.ipynb",
    "RML_GRP3_04_fairness.ipynb",
    "RML_GRP3_05_explainability.ipynb",
    "RML_GRP3_06_robustness_drift.ipynb",
]


def main() -> int:
    base_dir = Path(__file__).resolve().parent
    for notebook in NOTEBOOKS:
        print(f"Running {notebook} ...")
        cmd = [
            "jupyter",
            "nbconvert",
            "--to",
            "notebook",
            "--execute",
            "--inplace",
            "--ExecutePreprocessor.kernel_name=python3",
            notebook,
        ]
        subprocess.run(cmd, cwd=base_dir, check=True)
    print("Pipeline completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
