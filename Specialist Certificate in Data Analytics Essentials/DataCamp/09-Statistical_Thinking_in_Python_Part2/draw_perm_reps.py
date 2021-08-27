"""
Generating permutation replicates
The function has call signature draw_perm_reps(data_1, data_2, func, size=1). Importantly, func must be a function
that takes two arrays as arguments. In most circumstances, func will be a function you write yourself.

Instructions

    Define a function with this signature: draw_perm_reps(data_1, data_2, func, size=1).
        Initialize an array to hold the permutation replicates using np.empty().
        Write a for loop to:
            Compute a permutation sample using your permutation_sample() function
            Pass the samples into func() to compute the replicate and store the result in your array of replicates.
        Return the array of replicates.

"""
import numpy as np
import permutation_sample

def draw_perm_reps(data_1, data_2, func, size=1):
    """Generate multiple permutation replicates."""

    # Initialize array of replicates: perm_replicates
    perm_replicates = np.empty(size)

    for i in range(size):
        # Generate permutation sample
        perm_sample_1, perm_sample_2 = permutation_sample.permutation_sample(data_1, data_2)

        # Compute the test statistic
        perm_replicates[i] = func(perm_sample_1, perm_sample_2)

    return perm_replicates
