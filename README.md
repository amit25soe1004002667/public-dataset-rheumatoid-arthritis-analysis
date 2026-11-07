# Task 04 — Capstone practice project (SIMULATED DATA ONLY)

> **Honesty notice:** This repository is a synthetic-data demonstration, not a completed analysis of a real public biological dataset. The data and findings are artificial. Do not submit it as if it fulfilled the real-public-dataset requirement. Use it to practise the workflow, then replace the data with a documented public dataset for the actual capstone.

## Practice biological question
In a hypothetical case-control experiment, which genes show different expression in simulated rheumatoid arthritis (RA) samples compared with simulated healthy controls?

## Contents
- `data/simulated_expression_log2.csv` — artificial expression matrix (100 genes, 22 samples).
- `data/sample_metadata.csv` — artificial group labels.
- `scripts/analyze_data.py` — reproducible statistical analysis.
- `results/differential_expression_results.csv` — all gene-wise results.
- `results/significant_genes_FDR05.csv` — genes with BH-adjusted p-value < 0.05.
- `results/volcano_plot.png` — volcano plot.
- `results/analysis_report.md` — results and limitations.

## Methods
Welch's two-sample t-test for each gene, followed by Benjamini–Hochberg false-discovery-rate correction across all 100 tests. Significance threshold: adjusted p-value < 0.05. Effect size is the difference in mean log2 expression (RA minus control).

## Run on macOS
1. Install Python 3 if needed.
2. Open Terminal and navigate into this project folder.
3. Install dependencies:
   `python3 -m pip install pandas numpy scipy statsmodels matplotlib`
4. Run:
   `python3 scripts/analyze_data.py`

The script regenerates the output files in `results/`.

## Why this is not the final capstone
The assignment explicitly asks for a real public dataset. Synthetic data cannot satisfy that requirement, even when the statistical workflow is valid. For submission, obtain a traceable dataset from a repository such as NCBI GEO, document its accession and sample selection, and rerun the analysis. Never describe these simulated results as observed biological results.
