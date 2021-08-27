"""
Correlation of offspring and parental data

In an effort to quantify the correlation between offspring and parent beak depths, we would like to compute statistics,
such as the Pearson correlation coefficient, between parents and offspring. To get confidence intervals on this,
we need to do a pairs bootstrap.

You have already written a function to do pairs bootstrap to get estimates for parameters derived from
linear regression.
Your task in this exercise is to make a new function with call signature draw_bs_pairs(x, y, func, size=1)
that performs pairs bootstrap and computes a single statistic on pairs samples defined.
The statistic of interest is computed by calling func(bs_x, bs_y).
In the next exercise, you will use pearson_r for func.
"""

import numpy as np
def draw_bs_pairs(x, y, func, size=1):
    """Perform pairs bootstrap for a single statistic."""

    # Set up array of indices to sample from: inds
    inds = np.arange(len(x))

    # Initialize replicates: bs_replicates
    bs_replicates = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_inds = np.random.choice(inds, len(inds))
        bs_x, bs_y = bs_inds[x], bs_inds[y]
        bs_replicates[i] = func(bs_x, bs_y)

    return bs_replicates
