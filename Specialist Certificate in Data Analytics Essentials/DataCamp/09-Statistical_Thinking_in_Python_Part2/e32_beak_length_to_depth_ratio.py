"""
Beak length to depth ratio

Instructions
100 XP

    Make arrays of the beak length to depth ratio of each bird for 1975 and for 2012.
    Compute the mean of the length to depth ratio for 1975 and for 2012.
    Generate 10,000 bootstrap replicates each for the mean ratio for 1975 and 2012 using your draw_bs_reps() function.
    Get a 99% bootstrap confidence interval for the length to depth ratio for 1975 and 2012.
    Print the results.

"""

import draw_bs_pairs_linreg
import draw_bs_reps
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

bl_1975 = np.array([13.9, 14., 12.9, 13.5, 12.9, 14.6, 13., 14.2, 14.,
                    14.2, 13.1, 15.1, 13.5, 14.4, 14.9, 12.9, 13., 14.9,
                    14., 13.8, 13., 14.75, 13.7, 13.8, 14., 14.6, 15.2,
                    13.5, 15.1, 15., 12.8, 14.9, 15.3, 13.4, 14.2, 15.1,
                    15.1, 14., 13.6, 14., 14., 13.9, 14., 14.9, 15.6,
                    13.8, 14.4, 12.8, 14.2, 13.4, 14., 14.8, 14.2, 13.5,
                    13.4, 14.6, 13.5, 13.7, 13.9, 13.1, 13.4, 13.8, 13.6,
                    14., 13.5, 12.8, 14., 13.4, 14.9, 15.54, 14.63, 14.73,
                    15.73, 14.83, 15.94, 15.14, 14.23, 14.15, 14.35, 14.95, 13.95,
                    14.05, 14.55, 14.05, 14.45, 15.05, 13.25])

bd_1975 = np.array([8.4, 8.8, 8.4, 8., 7.9, 8.9, 8.6, 8.5, 8.9,
                    9.1, 8.6, 9.8, 8.2, 9., 9.7, 8.6, 8.2, 9.,
                    8.4, 8.6, 8.9, 9.1, 8.3, 8.7, 9.6, 8.5, 9.1,
                    9., 9.2, 9.9, 8.6, 9.2, 8.4, 8.9, 8.5, 10.4,
                    9.6, 9.1, 9.3, 9.3, 8.8, 8.3, 8.8, 9.1, 10.1,
                    8.9, 9.2, 8.5, 10.2, 10.1, 9.2, 9.7, 9.1, 8.5,
                    8.2, 9., 9.3, 8., 9.1, 8.1, 8.3, 8.7, 8.8,
                    8.6, 8.7, 8., 8.8, 9., 9.1, 9.74, 9.1, 9.8,
                    10.4, 8.3, 9.44, 9.04, 9., 9.05, 9.65, 9.45, 8.65,
                    9.45, 9.45, 9.05, 8.75, 9.45, 8.35])

bl_2012 = np.array([14.3, 12.5, 13.7, 13.8, 12., 13., 13., 13.6, 12.8,
                    13.6, 12.95, 13.1, 13.4, 13.9, 12.3, 14., 12.5, 12.3,
                    13.9, 13.1, 12.5, 13.9, 13.7, 12., 14.4, 13.5, 13.8,
                    13., 14.9, 12.5, 12.3, 12.8, 13.4, 13.8, 13.5, 13.5,
                    13.4, 12.3, 14.35, 13.2, 13.8, 14.6, 14.3, 13.8, 13.6,
                    12.9, 13., 13.5, 13.2, 13.7, 13.1, 13.2, 12.6, 13.,
                    13.9, 13.2, 15., 13.37, 11.4, 13.8, 13., 13., 13.1,
                    12.8, 13.3, 13.5, 12.4, 13.1, 14., 13.5, 11.8, 13.7,
                    13.2, 12.2, 13., 13.1, 14.7, 13.7, 13.5, 13.3, 14.1,
                    12.5, 13.7, 14.6, 14.1, 12.9, 13.9, 13.4, 13., 12.7,
                    12.1, 14., 14.9, 13.9, 12.9, 14.6, 14., 13., 12.7,
                    14., 14.1, 14.1, 13., 13.5, 13.4, 13.9, 13.1, 12.9,
                    14., 14., 14.1, 14.7, 13.4, 13.8, 13.4, 13.8, 12.4,
                    14.1, 12.9, 13.9, 14.3, 13.2, 14.2, 13., 14.6, 13.1,
                    15.2])
bd_2012 = np.array([9.4, 8.9, 9.5, 11., 8.7, 8.4, 9.1, 8.7, 10.2,
                    9.6, 8.85, 8.8, 9.5, 9.2, 9., 9.8, 9.3, 9.,
                    10.2, 7.7, 9., 9.5, 9.4, 8., 8.9, 9.4, 9.5,
                    8., 10., 8.95, 8.2, 8.8, 9.2, 9.4, 9.5, 8.1,
                    9.5, 8.4, 9.3, 9.3, 9.6, 9.2, 10., 8.9, 10.5,
                    8.9, 8.6, 8.8, 9.15, 9.5, 9.1, 10.2, 8.4, 10.,
                    10.2, 9.3, 10.8, 8.3, 7.8, 9.8, 7.9, 8.9, 7.7,
                    8.9, 9.4, 9.4, 8.5, 8.5, 9.6, 10.2, 8.8, 9.5,
                    9.3, 9., 9.2, 8.7, 9., 9.1, 8.7, 9.4, 9.8,
                    8.6, 10.6, 9., 9.5, 8.1, 9.3, 9.6, 8.5, 8.2,
                    8., 9.5, 9.7, 9.9, 9.1, 9.5, 9.8, 8.4, 8.3,
                    9.6, 9.4, 10., 8.9, 9.1, 9.8, 9.3, 9.9, 8.9,
                    8.5, 10.6, 9.3, 8.9, 8.9, 9.7, 9.8, 10.5, 8.4,
                    10., 9., 8.7, 8.8, 8.4, 9.3, 9.8, 8.9, 9.8,
                    9.1])

# Compute length-to-depth ratios
ratio_1975 = np.array(bl_1975/bd_1975)
ratio_2012 = np.array(bl_2012/bd_2012)

# Compute means
mean_ratio_1975 = np.mean(ratio_1975)
mean_ratio_2012 = np.mean(ratio_2012)

# Generate bootstrap replicates of the means
bs_replicates_1975 = draw_bs_reps.draw_bs_reps(ratio_1975,np.mean,10000)
bs_replicates_2012 = draw_bs_reps.draw_bs_reps(ratio_2012,np.mean,10000)

# Compute the 99% confidence intervals
conf_int_1975 = np.percentile(bs_replicates_1975,[0.5, 99.5])
conf_int_2012 = np.percentile(bs_replicates_2012,[0.5, 99.5])

# Print the results
print('1975: mean ratio =', mean_ratio_1975,
      'conf int =', conf_int_1975)
print('2012: mean ratio =', mean_ratio_2012,
      'conf int =', conf_int_2012)