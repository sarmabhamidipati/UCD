"""
Hypothesis test: Are beaks deeper in 2012?
Instructions
100 XP

    Make a concatenated array of the 1975 and 2012 beak depths and compute and store its mean.
    Shift bd_1975 and bd_2012 such that their means are equal to the one you just computed for the combined data set.
    Take 10,000 bootstrap replicates of the mean each for the 1975 and 2012 beak depths.
    Subtract the 1975 replicates from the 2012 replicates to get bootstrap replicates of the difference.
    Compute and print the p-value. The observed difference in means you computed in the
    last exercise is still in your namespace as mean_diff.

"""
import draw_bs_reps
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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

mean_diff = 0.22622047244094645
# Compute mean of combined data set: combined_mean
combined_mean = np.mean(np.concatenate((bd_1975, bd_2012)))

# Shift the samples
bd_1975_shifted = bd_1975 - np.mean(bd_1975) + combined_mean
bd_2012_shifted = bd_2012 - np.mean(bd_2012) + combined_mean

# Get bootstrap replicates of shifted data sets
bs_replicates_1975 = draw_bs_reps.draw_bs_reps(bd_1975_shifted,np.mean,10000)
bs_replicates_2012 = draw_bs_reps.draw_bs_reps(bd_2012_shifted,np.mean,10000)

# Compute replicates of difference of means: bs_diff_replicates
bs_diff_replicates = bs_replicates_2012 - bs_replicates_1975

# Compute the p-value
p = np.sum(bs_diff_replicates >= mean_diff) / len(bs_diff_replicates)

# Print p-value
print('p =', p)

