import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt



a_0 = 2 # alpha
b_0 = 6 / 7 # beta

alpha_0 = 0.95 # confidence level

quantile_0 = stats.gamma.ppf(alpha_0, a=a_0, scale=1 / b_0)

alpha_1 = 0.05
a_1 = 3
b_1 = 5 / 44

quantile_1 = stats.gamma.ppf(alpha_1, a=a_1, scale=1 / b_1)

b_0 = 1 - stats.gamma.cdf(quantile_0, a=a_1, scale=1 / b_1)

b_1 = stats.gamma.cdf(quantile_1, a=a_0, scale=1 / b_0)

print(f"Quantile 0: {quantile_0:.4f}")
print(f"Quantile 1: {quantile_1:.4f}")


print(f"b_0: {b_0:.4f}")
print(f"b_1: {b_1:.4f}")
