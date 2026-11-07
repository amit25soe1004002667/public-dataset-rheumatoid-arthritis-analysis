"""
SIMULATED DATA ONLY — educational demonstration.
This script must not be presented as analysis of real patient/public data.
Run from repository root: python scripts/analyze_data.py
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from statsmodels.stats.multitest import multipletests

ROOT = Path(__file__).resolve().parents[1]
expr = pd.read_csv(ROOT / "data" / "simulated_expression_log2.csv", index_col=0)
meta = pd.read_csv(ROOT / "data" / "sample_metadata.csv")
ra = meta.loc[meta.group == "Rheumatoid_Arthritis", "sample_id"].tolist()
ctrl = meta.loc[meta.group == "Healthy_Control", "sample_id"].tolist()

rows = []
for gene, row in expr.iterrows():
    ra_values = row[ra].to_numpy(dtype=float)
    ctrl_values = row[ctrl].to_numpy(dtype=float)
    _, p_value = ttest_ind(ra_values, ctrl_values, equal_var=False)
    rows.append({
        "gene_id": gene,
        "log2_fold_change_RA_vs_control": ra_values.mean() - ctrl_values.mean(),
        "p_value": p_value,
        "mean_RA": ra_values.mean(),
        "mean_control": ctrl_values.mean(),
    })

results = pd.DataFrame(rows)
results["adjusted_p_value_BH"] = multipletests(results.p_value, method="fdr_bh")[1]
results = results.sort_values("adjusted_p_value_BH")
out = ROOT / "results"
out.mkdir(exist_ok=True)
results.to_csv(out / "differential_expression_results.csv", index=False)
sig = results[results.adjusted_p_value_BH < 0.05]
sig.to_csv(out / "significant_genes_FDR05.csv", index=False)

plt.figure(figsize=(9, 6))
plt.scatter(results.log2_fold_change_RA_vs_control,
            -np.log10(results.p_value.clip(lower=1e-300)), s=20)
plt.axhline(-np.log10(0.05), linestyle="--")
plt.axvline(-1, linestyle=":")
plt.axvline(1, linestyle=":")
plt.xlabel("Mean log2 expression difference (RA - control)")
plt.ylabel("-log10(raw p-value)")
plt.title("SIMULATED DATA ONLY — Differential expression demo")
plt.tight_layout()
plt.savefig(out / "volcano_plot.png", dpi=180)
plt.close()

up = int((sig.log2_fold_change_RA_vs_control > 0).sum())
down = int((sig.log2_fold_change_RA_vs_control < 0).sum())
report = f"""# Analysis report — SIMULATED DATA ONLY

> Synthetic teaching data, not real patient measurements or a public dataset.
> Do not present these outputs as real biological findings.

## Practice question
In a hypothetical case-control experiment, which genes differ between simulated RA and healthy-control groups?

## Data
- {len(expr)} artificial genes; {len(ra)} simulated RA samples; {len(ctrl)} simulated controls.
- Random seed 42; log2-like values generated for demonstration.
- Some group effects were deliberately introduced.

## Methods
Welch two-sample t-test per gene; Benjamini–Hochberg FDR correction across all genes.
Significance threshold: adjusted p-value < 0.05. Effect size is mean RA minus mean control.

## Results
- Genes tested: {len(results)}
- FDR-significant genes: {len(sig)}
- Higher in simulated RA: {up}
- Lower in simulated RA: {down}

## Cautious interpretation
Any detected differences are properties of this constructed simulation. They do not establish anything about real rheumatoid arthritis, patients, diagnosis, or treatment.

## Limitations and confounders
The data are synthetic; there are no real subjects or clinical covariates. Real biological heterogeneity,
age, sex, medication, disease activity, cell composition, sample processing, and batch effects are not
modelled. The sample size is small and effects were engineered. FDR adjustment does not confer biological
validity. A genuine capstone must use a traceable public dataset and repeat the analysis.

## Reproducibility
Run `python scripts/analyze_data.py` from the repository root.
"""
(out / "analysis_report.md").write_text(report, encoding="utf-8")
print(f"Generated {len(results)} gene results; {len(sig)} passed BH FDR < 0.05.")
