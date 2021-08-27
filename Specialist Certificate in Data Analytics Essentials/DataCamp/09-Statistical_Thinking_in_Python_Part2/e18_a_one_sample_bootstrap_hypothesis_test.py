"""
A one-sample bootstrap hypothesis test
Instructions
100 XP

    Translate the impact forces of Frog B such that its mean is 0.55 N.
    Use your draw_bs_reps() function to take 10,000 bootstrap replicates of the mean of your translated forces.
    Compute the p-value by finding the fraction of your bootstrap replicates that are less than the observed mean
    impact force of Frog B. Note that the variable of interest here is force_b.
    Print your p-value.

"""
import numpy as np
import draw_bs_reps

force_a = np.array([1.612, 0.605, 0.327, 0.946, 0.541, 1.539, 0.529, 0.628, 1.453,
                    0.297, 0.703, 0.269, 0.751, 0.245, 1.182, 0.515, 0.435, 0.383,
                    0.457, 0.73])

force_b = np.array([0.172, 0.142, 0.037, 0.453, 0.355, 0.022, 0.502, 0.273, 0.72,
                    0.582, 0.198, 0.198, 0.597, 0.516, 0.815, 0.402, 0.605, 0.711,
                    0.614, 0.468])


# Make an array of translated impact forces: translated_force_b
translated_force_b = force_b - np.mean(force_b) + 0.55

# Take bootstrap replicates of Frog B's translated impact forces: bs_replicates
bs_replicates = draw_bs_reps.draw_bs_reps(translated_force_b, np.mean, 10000)

# Compute fraction of replicates that are less than the observed Frog B force: p
p = np.sum(bs_replicates <= np.mean(force_b)) / 10000

# Print the p-value
print('p = ', p)

