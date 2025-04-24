import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

alpha = 0.05  # Confidence level


b_0 = stats.expon.cdf(alpha, scale=1)


print(f"b_0: {b_0:.4f}")
