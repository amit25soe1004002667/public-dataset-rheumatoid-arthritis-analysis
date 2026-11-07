# Analysis report — SIMULATED DATA ONLY

> **Important:** This is a synthetic teaching example. The expression values were randomly generated with a small number of deliberately introduced group differences. They are not measurements from patients, a published experiment, or a public biological dataset. These outputs must not be represented as real research findings or submitted as analysis of a real public dataset.

## Biological question (practice scenario)
In a hypothetical case-control experiment, which genes have different expression in simulated rheumatoid arthritis (RA) samples compared with simulated healthy controls?

## Dataset
- 100 artificial gene identifiers.
- 9 simulated healthy-control samples.
- 13 simulated RA samples.
- Values are simulated log2 expression measurements.
- Random seed: 42 (for reproducibility).

## Statistical methods
- Welch's two-sample t-test for each gene.
- Benjamini–Hochberg false-discovery-rate correction across all 100 tests.
- Significance threshold: adjusted p-value (FDR) < 0.05.
- Effect size: difference in group mean log2 expression (RA minus control).

## Results from this simulated dataset
- Genes tested: 100
- Genes passing BH FDR < 0.05: 12
- Significant genes with higher simulated expression in RA: 6
- Significant genes with lower simulated expression in RA: 6

### Top 10 genes by adjusted p-value
```text
 gene_id  log2_fold_change_RA_vs_control      p_value  mean_RA  mean_control  adjusted_p_value_BH
GENE_004                        1.533198 6.868674e-09 9.683244      8.150046         6.868674e-07
GENE_003                        1.438588 1.091371e-07 9.357593      7.919005         5.456854e-06
GENE_001                        1.168043 9.512707e-07 8.897543      7.729499         3.124086e-05
GENE_008                       -0.916038 1.249634e-06 6.271446      7.187484         3.124086e-05
GENE_006                        1.171082 5.043903e-06 7.705942      6.534860         1.008781e-04
GENE_011                       -1.326678 8.665530e-06 6.989552      8.316230         1.444255e-04
GENE_009                       -1.144411 2.203767e-05 6.271418      7.415830         3.148239e-04
GENE_002                        1.201497 4.251061e-05 7.923988      6.722491         5.313827e-04
GENE_012                       -1.093874 2.272177e-04 7.043430      8.137304         2.511228e-03
GENE_005                        1.053005 2.511228e-04 7.069513      6.016508         2.511228e-03
```

## Cautious interpretation
In this deliberately constructed simulation, some genes differ between the two artificial groups. Positive mean differences indicate higher simulated expression in the RA-labelled group; negative values indicate lower simulated expression. Because group differences were deliberately inserted during data generation, these findings do not provide evidence about rheumatoid arthritis biology, real patients, diagnosis, or treatment.

## Limitations and confounders
- The data are synthetic and do not represent biological samples.
- No real patient characteristics, clinical metadata, medication history, age, sex, disease activity, or cell composition are available.
- The simulation does not model realistic microarray measurement processes, batch effects, probe annotation, or biological heterogeneity.
- The sample size is small and the effect sizes were intentionally engineered.
- Multiple-testing correction controls an error-rate target under its assumptions; it does not make simulated findings biologically valid.
- A real capstone submission must replace this synthetic dataset with a documented public dataset and repeat the analysis.

## Reproducibility
Run `python scripts/analyze_data.py` from the repository root. The script regenerates the statistical tables, volcano plot, and this report from the included synthetic CSV files.
