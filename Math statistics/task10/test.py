import scipy.stats as sps


t_quantile = sps.t(19).ppf(0.975)
fisher_quantile = sps.f(1, 19).ppf(0.95)

print(t_quantile ** 2, fisher_quantile)