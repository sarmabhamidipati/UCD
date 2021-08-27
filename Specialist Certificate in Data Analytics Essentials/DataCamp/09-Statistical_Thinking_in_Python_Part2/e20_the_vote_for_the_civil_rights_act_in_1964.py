"""
The vote for the Civil Rights Act in 1964
Instructions
100 XP

    Construct Boolean arrays, dems and reps that contain the votes of the respective parties;
    e.g., dems has 153 True entries and 91 False entries.
    Write a function, frac_yea_dems(dems, reps) that returns the fraction of Democrats that voted yea.
    The first input is an array of Booleans,
        Two inputs are required to use your draw_perm_reps() function, but the second is not used.
    Use your draw_perm_reps() function to draw 10,000 permutation replicates of the fraction of Democrat yea votes.
    Compute and print the p-value.

"""
import numpy as np
import draw_perm_reps
import permutation_sample

# Construct arrays of data: dems, reps
dems = np.array([True] * 153 + [False] * 91)
reps = np.array([True] * 136 + [False] * 35)

def frac_yea_dems(dems, reps):
    """Compute fraction of Democrat yea votes."""
    frac = np.sum(dems) / len(dems)
    return frac


# Acquire permutation samples: perm_replicates
perm_replicates = draw_perm_reps.draw_perm_reps(dems, reps, frac_yea_dems, 10000)

# Compute and print p-value: p
p = np.sum(perm_replicates <= 153 / 244) / len(perm_replicates)
print('p-value =', p)
