"""
Displaying the linear regression results
Instructions
100 XP

    Generate the x-values for the bootstrap lines using np.array(). They should consist of 10 mm and 17 mm.
Write a for loop to plot 100 of the bootstrap lines for the 1975 and 2012 data sets.
The lines for the 1975 data set should be 'blue' and those for the 2012 data set should be 'red'.
Hit 'Submit Answer' to view the plot!
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

# Compute the linear regressions
slope_1975, intercept_1975 = np.polyfit(bl_1975, bd_1975, 1)
slope_2012, intercept_2012 = np.polyfit(bl_2012, bd_2012, 1)

# Perform pairs bootstrap for the linear regressions
bs_slope_reps_1975, bs_intercept_reps_1975 = \
    draw_bs_pairs_linreg.draw_bs_pairs_linreg(bl_1975, bd_1975, 1000)
bs_slope_reps_2012, bs_intercept_reps_2012 = \
    draw_bs_pairs_linreg.draw_bs_pairs_linreg(bl_2012, bd_2012, 1000)

# Compute confidence intervals of slopes
slope_conf_int_1975 = np.percentile(bs_slope_reps_1975, [2.5, 97.5])
slope_conf_int_2012 = np.percentile(bs_slope_reps_2012, [2.5, 97.5])
intercept_conf_int_1975 = np.percentile(bs_intercept_reps_1975, [2.5, 97.5])

intercept_conf_int_2012 = np.percentile(bs_intercept_reps_2012, [2.5, 97.5])

# Make scatter plot of 1975 data
_ = plt.plot(bl_1975, bd_1975, marker='.',
             linestyle='none', color='blue', alpha=0.5)

# Make scatter plot of 2012 data
_ = plt.plot(bl_2012, bd_2012, marker='.',
             linestyle='none', color='red', alpha=0.5)

# Label axes and make legend
_ = plt.xlabel('beak length (mm)')
_ = plt.ylabel('beak depth (mm)')
_ = plt.legend(('1975', '2012'), loc='upper left')

# Generate x-values for bootstrap lines: x
x = np.array([10, 17])

# Plot the bootstrap lines
for i in range(100):
    plt.plot(x, bs_slope_reps_1975[i]*x + bs_intercept_reps_1975[i],
             linewidth=0.5, alpha=0.2, color='blue')
    plt.plot(x, bs_slope_reps_2012[i]*x + bs_intercept_reps_2012[i],
             linewidth=0.5, alpha=0.2, color='red')

# Draw the plot again
plt.show()