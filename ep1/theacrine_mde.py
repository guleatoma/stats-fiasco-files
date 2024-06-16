
# study on theacrine: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9654377/

import numpy as np
from statsmodels.stats.power import TTestIndPower

# Parameters
n_control = 11
n_treatment = 11
alpha = 0.05  # significance level
power = 0.80  # desired power
std_dev = 0.44  # standard deviation

# Initialize the power analysis object
power_analysis = TTestIndPower()

# Compute the effect size (Cohen's d)
effect_size = power_analysis.solve_power(
    effect_size=None, 
    nobs1=n_control, 
    alpha=alpha, 
    power=power, 
    ratio=(n_treatment/n_control), 
    alternative='larger')

# The effect size (Cohen's d) is a standardized measure
# To get the raw MDE, multiply Cohen's d by the standard deviation
raw_mde = effect_size * std_dev

print(f"Minimum Detectable Effect (MDE): {raw_mde:.4f}")


